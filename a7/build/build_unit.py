#!/usr/bin/env python3
"""Build the unit-wide documents: python3 build_unit.py u3/unit.py  → out/u3/"""
import sys, os, glob, importlib.util, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import unitbuild, lessonbuild
spec = importlib.util.spec_from_file_location("unit", sys.argv[1])
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
unit = os.path.basename(os.path.dirname(os.path.abspath(sys.argv[1])))
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", unit)
out = unitbuild.build_unit(m.U, outdir)
# the whole unit as one deck, in the manifest's teaching order
here = os.path.dirname(os.path.abspath(sys.argv[1]))
ms = importlib.util.spec_from_file_location("manifest", os.path.join(here, "manifest.py"))
mm = importlib.util.module_from_spec(ms); ms.loader.exec_module(mm)
specs = {}
for f in sorted(glob.glob(os.path.join(here, "l[0-9]*.py"))):
    ls = importlib.util.spec_from_file_location("lesson", f)
    lm = importlib.util.module_from_spec(ls); ls.loader.exec_module(lm)
    specs[lm.L["code"]] = lm.L
order = mm.M["lessons"]
missing = set(specs) ^ {row[0] for row in order}
if missing:
    raise SystemExit(f"unit deck: lesson specs and manifest disagree about {sorted(missing)}")
out["unit_deck"] = lessonbuild.build_unit_deck([specs[row[0]] for row in order],
                                               [(row[1], row[2]) for row in order], m.U, outdir)
for k, path in out.items():
    if path.endswith(".html"):          # the HTML deck is its own final form (prints from the browser)
        print("built", os.path.basename(path)); continue
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", outdir, path],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pdf = path.rsplit(".", 1)[0] + ".pdf"
    assert os.path.exists(pdf), pdf
    print("built", os.path.basename(path), "+ pdf")
