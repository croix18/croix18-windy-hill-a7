#!/usr/bin/env python3
"""Rebuild a whole unit from its specs, run the check suite, and (with --install) install it.
    python3 build_all.py u3 [--install]
Use it in a fresh clone (the PDFs are git-ignored, so checks.py needs every twin regenerated),
and as the last step before a unit ships. Order: every lNN.py, then unit.py, then checks.py.
"""
import os, sys, glob, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
unit = sys.argv[1].rstrip("/")
specs = sorted(glob.glob(os.path.join(HERE, unit, "l[0-9][0-9].py")))
if not specs:
    raise SystemExit(f"no lesson specs in {unit}/")
for s in specs:
    print("==", os.path.basename(s))
    subprocess.run([sys.executable, os.path.join(HERE, "build_lesson.py"), s], check=True)
u = os.path.join(HERE, unit, "unit.py")
if os.path.exists(u):
    print("== unit.py")
    subprocess.run([sys.executable, os.path.join(HERE, "build_unit.py"), u], check=True)
print("== checks")
r = subprocess.run([sys.executable, os.path.join(HERE, "checks.py"), os.path.join(HERE, "out", unit)])
if r.returncode:
    raise SystemExit("checks failed — fix before installing")
if "--install" in sys.argv:
    m = os.path.join(HERE, unit, "manifest.py")
    subprocess.run([sys.executable, os.path.join(HERE, "install_unit.py"), m], check=True)
print("build_all: done")
