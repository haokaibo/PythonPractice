"""
Build a fully static snapshot of the PythonPractice browser for GitHub Pages.

Unlike `web/app.py` (which serves live queries against src/ and
favorites.json), this script runs once at CI-build time and writes
everything a static host needs:

  dist/
  ├── index.html            # copied from web/static/index.html
  ├── static/
  │   ├── style.css         # copied from web/static/style.css
  │   └── app.js            # copied from web/static/app.static.js (NOT app.js!)
  ├── api/
  │   ├── all.json          # every .py file under src/, with favorited flags
  │   ├── favorites.json    # favorites.json contents, decorated the same way
  │   └── tags.json         # {favorites: {tag: count}, all: {tag: count}}
  └── src/                  # full copy of src/, so file contents can be
                             # fetched directly at their own relative path

Run:
    python scripts/build_static.py --out dist
"""
from __future__ import annotations

import argparse
import json
import shutil
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "src"
FAVORITES_FILE = ROOT / "favorites.json"
WEB_STATIC_DIR = ROOT / "web" / "static"


# ---------- ported from web/app.py (kept in lockstep with it) ----------

def category_for(rel_path: str) -> str:
    """First directory under src/, e.g. 'src/amazon/foo.py' -> 'amazon'."""
    parts = Path(rel_path).parts
    if len(parts) >= 2 and parts[0] == "src":
        return parts[1]
    return ""


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
            "category": category_for(rel),
        })
    return out


def load_favorites() -> list[dict]:
    if not FAVORITES_FILE.exists():
        return []
    data = json.loads(FAVORITES_FILE.read_text(encoding="utf-8"))
    items = data.get("items", [])
    for it in items:
        it.setdefault("tags", [])
        it["category"] = category_for(it.get("path", ""))
    return items


def all_tags(items: list[dict]) -> dict[str, int]:
    c: Counter[str] = Counter()
    for it in items:
        for t in it.get("tags") or []:
            c[t] += 1
    return dict(sorted(c.items(), key=lambda kv: (-kv[1], kv[0])))


def decorate_with_fav(items: list[dict], fav_paths: set[str]) -> list[dict]:
    for it in items:
        it["favorited"] = it.get("path") in fav_paths
    return items


# ---------- build ----------

def build(out_dir: Path) -> None:
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    # 1. static assets — note app.js comes from app.static.js, not app.js.
    #    app.js (in web/static/) stays the dynamic version used by
    #    `uvicorn web.app:app --reload` for local dev; it never ships.
    static_out = out_dir / "static"
    static_out.mkdir()
    shutil.copy(WEB_STATIC_DIR / "style.css", static_out / "style.css")
    static_app_js = WEB_STATIC_DIR / "app.static.js"
    if not static_app_js.exists():
        raise SystemExit(
            "web/static/app.static.js not found — this is the static-build "
            "frontend, separate from the dynamic web/static/app.js used by "
            "the local FastAPI server."
        )
    shutil.copy(static_app_js, static_out / "app.js")

    # 2. index.html — unchanged, it already uses relative paths
    #    (./static/..., ./api/...) so it works the same from any host.
    shutil.copy(WEB_STATIC_DIR / "index.html", out_dir / "index.html")

    # 3. full source tree, so `fetch('./src/amazon/foo.py')` just works
    shutil.copytree(SRC_DIR, out_dir / "src")

    # 4. pre-computed API responses
    favorites = load_favorites()
    fav_paths = {it["path"] for it in favorites if it.get("path")}
    all_items = decorate_with_fav(iter_py_files(), fav_paths)
    favorites = decorate_with_fav(favorites, fav_paths)

    api_out = out_dir / "api"
    api_out.mkdir()
    (api_out / "all.json").write_text(
        json.dumps(all_items, ensure_ascii=False), encoding="utf-8")
    (api_out / "favorites.json").write_text(
        json.dumps(favorites, ensure_ascii=False), encoding="utf-8")
    (api_out / "tags.json").write_text(
        json.dumps({"favorites": all_tags(favorites), "all": all_tags(all_items)},
                   ensure_ascii=False),
        encoding="utf-8")

    print(f"Built static site -> {out_dir}  "
          f"({len(all_items)} files, {len(favorites)} favorites)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="dist", help="output directory")
    args = parser.parse_args()
    build((ROOT / args.out).resolve())
