# Python Practice

A collection of Python solutions to algorithm and interview problems, organized
by source (LeetCode, AlgoExpert, Amazon, Facebook, Google, Microsoft, freeCodeCamp, etc.).
A small web browser is included for fast lookup and personal bookmarking.

## Layout

```
.
├── src/                # All problem solutions, grouped by source folder
│   ├── leetcode/
│   ├── algoexpert/
│   ├── amazon/
│   ├── facebook/
│   ├── google/
│   ├── microsoft/
│   ├── freecodecamp/
│   └── .../
├── favorites.json      # User-managed list of bookmarked files
├── web/                # Local browser UI for the project
│   ├── app.py          # FastAPI server
│   └── static/         # index.html, app.js, style.css
├── build.sh            # Wrapper: build the static site into dist/
├── pyproject.toml      # Project metadata + dependencies
└── .venv/              # Local virtual environment (not committed)
```

## Quick start

The web UI lives in `web/` and is built on FastAPI. It reads Python files from
`src/` and the bookmark list from `favorites.json` at the repo root.

Shortest path: `./build.sh` — builds the static site, sets up the venv if
needed, starts the server, and opens the browser (see
[Static site build](#static-site-build-github-pages) below).

Manual steps:

```bash
# 1. create / activate a virtualenv (Python 3.13+)
python3.13 -m venv .venv
source .venv/bin/activate

# 2. install dependencies
pip install fastapi 'uvicorn[standard]'

# 3. start the server
python -m uvicorn web.app:app --reload

# 4. open in a browser
open http://127.0.0.1:8000
```

## Web UI features

- **Two tabs**:
  - `★ Favorites` — files listed in `favorites.json` (the bookmark view).
  - `All files` — every `.py` file under `src/`, grouped by source folder.
- **Google-style search box** with fuzzy subsequence matching against file
  names, sorted by how tightly the matched characters cluster in the name.
  Results are highlighted in real time as you type.
- **Category filter** to focus on a single source folder.
- **Tag chips** (on the Favorites tab) for AND-filtering by tags.
- **Collapsible groups** by category in the result list.
- **Favorite toggle**: click the ☆ / ★ on the right of any list item to add or
  remove it from `favorites.json`. State is persisted server-side and survives
  page reloads.
- **Keyboard navigation**:
  - `/` focus the search box
  - `↑` / `↓` move the selection
  - `Enter` open the selected file
  - `Esc` clear the search or the selection
- **Syntax-highlighted viewer** with line numbers (Prism.js, lazy-loaded from
  a CDN).

## Static site build (GitHub Pages)

`scripts/build_static.py` generates a fully static snapshot of the browser
into `dist/` — no server needed. It copies the frontend (using the static
frontend `web/static/app.static.js`), copies the whole `src/` tree, and
pre-computes the API responses (`api/all.json`, `api/favorites.json`,
`api/tags.json`) with the current favorite flags baked in.

Use the wrapper script (from the repo root):

```bash
# build into dist/ (default), then start the local FastAPI server
./build.sh

# build into a custom output directory, then start the server
./build.sh my-out

# build only, do not start the server
./build.sh --build-only
```

What it does, in order:

1. Runs `python scripts/build_static.py --out <dir>` (prefers the project's
   `.venv` python; the build itself needs no dependencies — stdlib only).
2. Creates `.venv` with `python3.13 -m venv` if it doesn't exist, activates it.
3. Installs `fastapi` and `uvicorn[standard]`.
4. Starts `uvicorn web.app:app --reload` in the background, opens
   `http://127.0.0.1:8000` in your browser, and stays in the foreground —
   press `Ctrl+C` to stop the server.

After building you can preview locally without any server:

```bash
open dist/index.html   # or any static file server, e.g. `python3 -m http.server -d dist`
```

Pushing to `master` also triggers `.github/workflows/deploy-pages.yml`, which
runs the same build in CI and deploys `dist/` to GitHub Pages.

## Bookmarks

`favorites.json` at the repo root is the single source of truth. It looks like:

```json
{
  "items": [
    {
      "path":  "src/microsoft/wildcard_matching.py",
      "title": "Wildcard Matching",
      "tags":  ["string", "greedy", "two-pointers"],
      "note":  "Classic LeetCode 44. Greedy O(m+n) avoids regex TLE."
    }
  ]
}
```

You can either:

- Edit the file by hand and refresh the page, or
- Click the ☆ in the UI to toggle entries (the server writes the file for you).

## API endpoints (for reference)

| Method | Path                              | Purpose                                      |
| ------ | --------------------------------- | -------------------------------------------- |
| GET    | `/`                               | Static `index.html`                          |
| GET    | `/api/favorites?q=&tags=&category=` | Bookmarked items, with the same filters    |
| GET    | `/api/all?q=&category=`           | All `.py` files under `src/`                 |
| GET    | `/api/categories?scope=all\|favorites` | `{category: count}` for the dropdown     |
| GET    | `/api/tags`                       | Tag frequencies per tab                      |
| GET    | `/api/file?path=...`              | Raw file contents (path is sandboxed to `src/`) |
| POST   | `/api/favorites/toggle`           | Add or remove a path from `favorites.json`  |

## Source folders

| Folder       | Description                                                |
| ------------ | ---------------------------------------------------------- |
| `leetcode/`  | LeetCode problems (recursion, recursion_ii, etc.)          |
| `algoexpert/`| AlgoExpert problems, grouped by topic                      |
| `amazon/`    | Interview problems attributed to Amazon                    |
| `facebook/`  | Interview problems attributed to Facebook                  |
| `google/`    | Interview problems attributed to Google                    |
| `microsoft/` | Interview problems attributed to Microsoft                 |
| `freecodecamp/` | freeCodeCamp challenges                                 |
| `basic/`     | Introductory exercises                                      |
| `HeadFirstPython/` | Exercises from *Head First Python*                    |
| `AvifToPng/` | Small utility scripts                                      |

## Notes

- Path traversal is blocked at the API level: only paths under `src/` resolve.
- The web UI is a local dev tool; there is no auth and it binds to `127.0.0.1`
  by default. Do not expose it on a public network.
