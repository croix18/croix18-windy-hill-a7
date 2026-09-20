#!/usr/bin/env python3
"""Build one lesson: python3 build_lesson.py u3/l01.py  → out/u3/"""
import sys, os, importlib.util, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import lessonbuild
spec = importlib.util.spec_from_file_location("lesson", sys.argv[1])
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
unit = os.path.basename(os.path.dirname(os.path.abspath(sys.argv[1])))
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", unit)
out = lessonbuild.build_lesson(m.L, outdir)
# every document gets its PDF twin, each converted by its own command (§0: rebuild each file alone)
for k, path in out.items():
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", outdir, path],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pdf = path.rsplit(".", 1)[0] + ".pdf"
    assert os.path.exists(pdf), pdf
    print("built", os.path.basename(path), "+ pdf")
