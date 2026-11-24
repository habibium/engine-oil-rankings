#!/usr/bin/env bash
# Regenerates output/*.pdf and output/*.png from src/data.json.
# Needs Python 3, Google Chrome (or Chromium) and ImageMagick 7.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/src"
OUT="$ROOT/output"
BUILD="$ROOT/build"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
mkdir -p "$BUILD" "$OUT"

python3 -I "$SRC/gen.py" "$SRC" "$SRC/data.json" "$SRC/template.html" "$BUILD"

chrome() {
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --no-first-run \
    --no-default-browser-check --user-data-dir="$BUILD/chrome-profile" "$@" >/dev/null 2>&1
}

for k in protection performance value; do
  html="file://$BUILD/$k.html"
  # The page sets its own @page size, so the PDF is one page with no header or footer.
  chrome --no-pdf-header-footer --window-size=2048,1600 --print-to-pdf="$OUT/10w30-oils-ranked-by-$k.pdf" "$html"
  chrome --force-device-scale-factor=2 --window-size=2048,2300 --screenshot="$BUILD/$k-raw.png" "$html"
  magick "$BUILD/$k-raw.png" -fuzz 1% -trim +repage -bordercolor '#fcfcfb' -border 88 \
    -filter Lanczos -resize 2048x "$OUT/10w30-oils-ranked-by-$k.png"
  echo "wrote output/10w30-oils-ranked-by-$k.{pdf,png}"
done
