#!/usr/bin/env bash
# Build the static site (for GitHub Pages), then start the local dev server.
#
# Usage:
#   ./build.sh                # build into dist/, then start the FastAPI server
#   ./build.sh my-out         # build into my-out/, then start the server
#   ./build.sh --build-only   # build only, do not start the server
#
# Press Ctrl+C to stop the server.
set -euo pipefail

cd "$(dirname "$0")"

# ---------- 1. build the static site ----------
if [[ -x .venv/bin/python ]]; then
  PY=.venv/bin/python
else
  PY=python3
fi

OUT="${1:-dist}"
if [[ "$OUT" == "--build-only" ]]; then
  OUT=dist
  NO_SERVER=1
else
  NO_SERVER=0
fi

"$PY" scripts/build_static.py --out "$OUT"

if [[ "$NO_SERVER" -eq 1 ]]; then
  echo "Static build done (server not started)."
  exit 0
fi

# ---------- 2. create / activate a virtualenv (Python 3.13+) ----------
if [[ ! -d .venv ]]; then
  python3.13 -m venv .venv
fi
source .venv/bin/activate

# ---------- 3. install dependencies ----------
pip install -q fastapi 'uvicorn[standard]'

# ---------- 4. start the server and open a browser ----------
python -m uvicorn web.app:app --reload &
SERVER_PID=$!
trap 'kill "$SERVER_PID" 2>/dev/null || true' INT TERM
sleep 2   # give the server a moment to boot
open http://127.0.0.1:8000
echo "Server running at http://127.0.0.1:8000  (Ctrl+C to stop)"
wait "$SERVER_PID"
