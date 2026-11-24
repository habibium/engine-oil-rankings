#!/usr/bin/env bash
# Regenerates output/*.pdf and output/*.png from data/*.json (one set of three rankings per grade).
# Needs Python 3, Google Chrome (or Chromium) and ImageMagick 7.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/output"
BUILD="$ROOT/build/images"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
rm -rf "$BUILD"
mkdir -p "$BUILD" "$OUT"

python3 -B "$ROOT/src/build_images.py" "$BUILD"

chrome() {
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --no-first-run \
    --no-default-browser-check --user-data-dir="$ROOT/build/chrome-profile" "$@" >/dev/null 2>&1
}

for page in "$BUILD"/*.html; do
  name="$(basename "$page" .html)"
  # The page sets its own @page size, so the PDF is one page with no header or footer.
  chrome --no-pdf-header-footer --window-size=2048,1600 --print-to-pdf="$OUT/$name.pdf" "file://$page"
  chrome --force-device-scale-factor=2 --window-size=2048,2300 --screenshot="$BUILD/$name-raw.png" "file://$page"
  magick "$BUILD/$name-raw.png" -fuzz 1% -trim +repage -bordercolor '#fcfcfb' -border 88 \
    -filter Lanczos -resize 2048x "$OUT/$name.png"
  echo "wrote output/$name.{pdf,png}"
done
