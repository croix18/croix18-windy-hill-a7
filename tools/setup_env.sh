#!/usr/bin/env bash
# One-shot environment setup for a fresh Claude session (Ubuntu/Debian container).
# Installs everything the A7 build system needs, then verifies it. Safe to re-run.
#   bash tools/setup_env.sh
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== apt packages"
export DEBIAN_FRONTEND=noninteractive
sudo_() { if [ "$(id -u)" = 0 ]; then "$@"; else sudo "$@"; fi; }
sudo_ apt-get update -qq
sudo_ apt-get install -y -qq --no-install-recommends \
  libreoffice-writer libreoffice-impress libreoffice-core \
  poppler-utils \
  fonts-liberation fonts-liberation2 fonts-dejavu fonts-freefont-ttf fonts-texgyre \
  fontconfig >/dev/null
fc-cache -f >/dev/null || true

echo "== python packages"
pip install -q --break-system-packages python-docx python-pptx matplotlib sympy fonttools pymupdf pillow

echo "== verify"
python3 - <<'EOF'
import shutil, subprocess, sys
ok = True
for mod in ("docx", "pptx", "matplotlib", "sympy", "fontTools", "pymupdf", "PIL"):
    try:
        __import__(mod)
    except Exception as e:
        print("MISSING python module:", mod, e); ok = False
for exe in ("soffice", "pdftotext", "pdfimages", "pdftoppm", "pdfinfo", "fc-list"):
    if not shutil.which(exe):
        print("MISSING executable:", exe); ok = False
fonts = subprocess.run(["fc-list"], capture_output=True, text=True).stdout
for name in ("Liberation Serif", "DejaVu Serif", "FreeSerif", "TeX Gyre Schola", "Liberation Sans"):
    if name not in fonts:
        print("MISSING font:", name); ok = False
# STIX ships inside matplotlib (mathtext); confirm it renders
import matplotlib; matplotlib.use("Agg")
from matplotlib import mathtext
mathtext.MathTextParser("path").parse(r"$2^{-3}$")
print("environment OK" if ok else "environment INCOMPLETE"); sys.exit(0 if ok else 1)
EOF

echo "== git"
git config user.name "Croix Shaffer"
git config user.email "268190892+croix18@users.noreply.github.com"
if [ ! -f .github-token ]; then
  echo "NOTE: no .github-token yet. Ask Croix for the fine-grained token, then:"
  echo "      printf '%s' '<token>' > .github-token && chmod 600 .github-token"
  echo "      Never paste it into a commit, a remote URL, or a chat log."
fi
echo "done. Smoke test (about ten minutes):  cd a7/build && python3 build_all.py u3"
