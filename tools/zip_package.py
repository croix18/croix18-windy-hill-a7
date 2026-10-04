#!/usr/bin/env python3
"""Zip a unit's package folder for delivery — for the units no build writes (made before the kit).
    python3 tools/zip_package.py 1 2
A unit the kit builds is zipped by its install (build_all.py uN --install); this is the same code
(lib/packkit.py), so the zips are named and split the same way: "<COURSE> Unit N - Complete.zip"
(and in parts when it is over the upload limit), one per lesson, Lessons, Review and Assessment.
They go to a7/packages/zips/, which git ignores — they are regenerable."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "a7", "build"))
from lib import packkit

PACKAGES = os.path.join(ROOT, "a7", "packages")
for n in [int(a) for a in sys.argv[1:]] or [1,2]:
    pkg = os.path.join(PACKAGES, packkit.package_folder(n))
    if not os.path.isdir(pkg):
        raise SystemExit(f"no package folder for unit {n}: {pkg}")
    made = packkit.zips(pkg, os.path.join(PACKAGES, "zips"), n)
    print(f"unit {n}: {len(made)} zips")
    for z in made:
        print(f"   {os.path.getsize(os.path.join(PACKAGES, 'zips', z)) / 2 ** 20:6.1f} MB  {z}")
