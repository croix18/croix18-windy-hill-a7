#!/usr/bin/env python3
"""Build the unit-wide documents: python3 build_unit.py u3/unit.py  → out/u3/"""
import sys, os, importlib.util, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import unitbuild
spec = importlib.util.spec_from_file_location("unit", sys.argv[1])
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
unit = os.path.basename(os.path.dirname(os.path.abspath(sys.argv[1])))
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", unit)
out = unitbuild.build_unit(m.U, outdir)
for k, path in out.items():
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", outdir, path],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pdf = path.rsplit(".", 1)[0] + ".pdf"
    assert os.path.exists(pdf), pdf
    print("built", os.path.basename(path), "+ pdf")
