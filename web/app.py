"""
Minimal web app to browse favorite Python files from this project.

Endpoints:
  GET  /                       -> static index.html
  GET  /static/*               -> static assets
  GET  /api/favorites          -> favorite items (q= prefix, tags= csv, category=)
  GET  /api/all                -> all .py files under src/ (same filters)
  GET  /api/tags               -> {favorites: {tag: count}, all: {tag: count}}
  GET  /api/categories         -> {name: count} for the current list
  GET  /api/file?path=...      -> file contents (text/plain), path-validated

Run:
  uv run uvicorn web.app:app --reload
  # or
  python -m uvicorn web.app:app --reload
"""
from __future__ import annotations

import json
import mimetypes
from collections import Counter
from pathlib import Path
from typing import Iterable

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse, JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "src"
FAVORITES_FILE = ROOT / "favorites.json"
STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(title="PythonPractice Browser", version="0.1.0")


# ---------- helpers ----------

def _category_for(rel_path: str) -> str:
    """First directory under src/, e.g. 'src/amazon/foo.py' -> 'amazon'."""
    parts = Path(rel_path).parts
    if len(parts) >= 2 and parts[0] == "src":
        return parts[1]
    return ""


def _all_tags(items: list[dict]) -> dict[str, int]:
    """Return {tag: count} across the given items."""
    c: Counter[str] = Counter()
    for it in items:
        for t in it.get("tags") or []:
            c[t] += 1
    return dict(sorted(c.items(), key=lambda kv: (-kv[1], kv[0])))


# ---------- favorites persistence ----------

# Set of paths currently favorited. Refreshed on every read of favorites.json
# so manual edits are picked up without restart.
def _fav_paths() -> set[str]:
    return {it["path"] for it in load_favorites() if it.get("path")}


def _save_favorites(items: list[dict]) -> None:
    FAVORITES_FILE.write_text(
        json.dumps({"items": items}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _decorate_with_fav(items: list[dict]) -> list[dict]:
    favs = _fav_paths()
    for it in items:
        it["favorited"] = it.get("path") in favs
    return items


# ---------- favorites ----------

def load_favorites() -> list[dict]:
    if not FAVORITES_FILE.exists():
        return []
    with FAVORITES_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
    items = data.get("items", [])
    for it in items:
        it.setdefault("tags", [])
        it["category"] = _category_for(it.get("path", ""))
    return items


def _fuzzy_match(needle: str, haystacks: list[str]) -> bool:
    """
    Subsequence match: the chars of `needle` must appear IN ORDER in ANY
    ONE of the haystacks (case-insensitive). Empty needle matches
    anything.

    Examples (needle='abc'):
      'a_b_c'  match (a, then b, then c, in order)
      'axbxc'  match
      'xabcx'  match
      'acb'    no match (wrong order)
      'ab'     no match (missing char)
    """
    if not needle:
        return True
    needle = needle.lower()
    for hay in haystacks:
        i = 0
        for ch in needle:
            j = hay.find(ch, i)
            if j < 0:
                break
            i = j + 1
        else:
            return True
    return False


def _fuzzy_score(needle: str, haystack: str) -> int:
    """
    Lower is better. Returns the span (last_match - first_match) of the
    matched chars in `haystack`. Returns +inf if no match.
    """
    if not needle:
        return 0
    needle = needle.lower()
    hay = haystack.lower()
    i = 0
    first = None
    last = -1
    for ch in needle:
        j = hay.find(ch, i)
        if j < 0:
            return 10**9
        if first is None:
            first = j
        last = j
        i = j + 1
    return last - first


def _filter(
    items: list[dict],
    q: str = "",
    tags: list[str] | None = None,
    category: str = "",
) -> list[dict]:
    """
    Apply, in order:
      1. category (exact, "" means any)
      2. tags       (ALL must match; AND semantics)
      3. q          (fuzzy subsequence match against title, basename, and
                     the path itself; chars must appear in order)
    """
    tags = [t for t in (tags or []) if t]
    q = q.strip().lower()

    out = []
    for it in items:
        if category and it.get("category") != category:
            continue
        if tags:
            have = set(it.get("tags") or [])
            if not all(t in have for t in tags):
                continue
        if q:
            # Only search the basename (filename). Directory names and
            # titles are too noisy — e.g. 'string' used to match
            # 'binary_search.py' because the parent dir 'searching'
            # contains r-i-n-g.
            basename = Path(it.get("path") or "").name.lower()
            score = _fuzzy_score(q, basename)
            if score >= 10**9:
                continue
            it["_score"] = score
        out.append(it)

    if q:
        # Best matches (smallest span) first. The basename of a true
        # positive like 'string_to_integer.py' for needle 'string' has
        # span 5; a noisy one like 'pascal_triangle.py' has span 10.
        out.sort(key=lambda it: it["_score"])
    return out


@app.get("/api/favorites")
def api_favorites(
    q: str = Query(""),
    tags: str = Query("", description="comma-separated AND filter"),
    category: str = Query(""),
):
    items = load_favorites()
    items = _filter(items, q, [t.strip() for t in tags.split(",") if t.strip()], category)
    return _decorate_with_fav(items)


# ---------- all .py files (for the "all" tab) ----------

def iter_py_files() -> list[dict]:
    out = []
    for p in sorted(SRC_DIR.rglob("*.py")):
        if p.name == "__init__.py":
            continue
        rel = p.relative_to(ROOT).as_posix()
        out.append({
            "path": rel,
            "title": p.stem.replace("_", " ").title(),
            "tags": [],
            "category": _category_for(rel),
        })
    return out


@app.get("/api/all")
def api_all(
    q: str = Query(""),
    tags: str = Query(""),
    category: str = Query(""),
):
    items = _filter(iter_py_files(), q, [t.strip() for t in tags.split(",") if t.strip()], category)
    return _decorate_with_fav(items)


@app.post("/api/favorites/toggle")
def api_favorites_toggle(payload: dict):
    """
    Toggle favorite status for a file path.
    Body: {"path": "src/.../foo.py", "title": "...", "tags": [...], "note": "..."}
    The title/tags/note are required for ADD so the user-supplied metadata
    is preserved; on REMOVE only `path` is used.
    Returns: {"favorited": true|false, "path": "..."}
    """
    rel_path = (payload or {}).get("path", "").strip()
    if not rel_path:
        raise HTTPException(400, "path is required")

    # Security: only files under src/ can be favorited
    candidate = (ROOT / rel_path).resolve()
    try:
        candidate.relative_to(SRC_DIR.resolve())
    except ValueError:
        raise HTTPException(403, "path outside src/ is not allowed")

    items = load_favorites()
    idx = next((i for i, it in enumerate(items) if it.get("path") == rel_path), -1)

    if idx >= 0:
        items.pop(idx)
        favorited = False
    else:
        new_item = {
            "path":  rel_path,
            "title": (payload.get("title") or Path(rel_path).stem.replace("_", " ").title()),
            "tags":  list(payload.get("tags") or []),
            "note":  payload.get("note", ""),
        }
        items.append(new_item)
        favorited = True

    _save_favorites(items)
    return JSONResponse({"favorited": favorited, "path": rel_path,
                         "total": len(items)})


# ---------- tag & category catalogs (drive the chip bars) ----------

@app.get("/api/tags")
def api_tags():
    """Tag frequencies per tab. The 'all' tab is sparse (only favorites have tags)."""
    return {
        "favorites": _all_tags(load_favorites()),
        # The 'all' tab synthesizes tags from the first path segment for
        # quick discovery, but keeps the favorites tags too if any.
        "all": _all_tags(iter_py_files()),
    }


@app.get("/api/categories")
def api_categories(scope: str = Query("all", pattern="^(all|favorites)$")):
    src = load_favorites() if scope == "favorites" else iter_py_files()
    c: Counter[str] = Counter()
    for it in src:
        cat = it.get("category") or ""
        if cat:
            c[cat] += 1
    return dict(sorted(c.items(), key=lambda kv: (-kv[1], kv[0])))


# ---------- file contents ----------

def _safe_resolve(rel_path: str) -> Path:
    """Resolve `rel_path` and refuse to escape SRC_DIR."""
    if not rel_path:
        raise HTTPException(400, "path is required")
    candidate = (ROOT / rel_path).resolve()
    try:
        candidate.relative_to(SRC_DIR.resolve())
    except ValueError:
        raise HTTPException(403, "path outside src/ is not allowed")
    if not candidate.is_file():
        raise HTTPException(404, "file not found")
    return candidate


@app.get("/api/file")
def api_file(path: str = Query(..., description="Relative path under src/")):
    p = _safe_resolve(path)
    mime, _ = mimetypes.guess_type(p.name)
    return PlainTextResponse(p.read_text(encoding="utf-8"),
                             media_type=mime or "text/plain")


# ---------- static ----------

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web.app:app", host="127.0.0.1", port=8000, reload=True)
