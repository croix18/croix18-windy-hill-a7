#!/usr/bin/env python3
"""The live half of the master sheet's links, which the committed workbook cannot show.

As committed the workbook's hidden Drive tab is empty — the script in Croix's Google account fills
it, in his Drive — so every link in it calculates to its fallback, the search. This test plays the
script's part: it writes a Drive tab as the script would (a code and a made-up Drive id for every
document and folder the packages hold, EXCEPT one unit, as if that unit were not in his Drive
yet), builds the workbook with it, has LibreOffice calculate it, and runs the check. Every link of
a listed document must come out as that document's own address; every link of the missing unit as
its search; nothing as an error.

    python3 tools/test_live_links.py        # needs LibreOffice; about a minute

Not part of tools/check.sh (CI has no LibreOffice). Run it after changing how a link is written."""
import os, re, sys, glob, shutil, hashlib, tempfile, subprocess, unicodedata
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PKG = next(p for p in ("m7/packages", "a7/packages") if os.path.isdir(os.path.join(ROOT, p)))
SOFFICE = shutil.which("soffice") or shutil.which("libreoffice") or sys.exit("needs LibreOffice")
code = lambda name: "k" + hashlib.md5(unicodedata.normalize("NFC", name).encode("utf-8")).hexdigest()[:12]
fake_id = lambda path: "1" + hashlib.sha1(path.encode("utf-8")).hexdigest()[:32]
files = [t for t in subprocess.run(["git", "-C", ROOT, "ls-files", "-z", "-c", "-o", "--exclude-standard", PKG], capture_output=True, text=True).stdout.split("\0") if t]
units = sorted({t[len(PKG) + 1:].split("/")[0] for t in files})
missing = units[-1]                                   # the newest unit is "not uploaded yet"
names = [os.path.basename(t) for t in files]
rows = {}
for t in files:
    parts = t[len(PKG) + 1:].split("/"); name = parts[-1]; unit = parts[0]
    if unit == missing:
        continue
    rows[code(unit)] = fake_id(f"{PKG}/{unit}")
    if names.count(name) == 1 and name.startswith(unit.split(" ")[0] + " "):     # named for its course, and the only one
        rows[code(name)] = fake_id(t)
    if len(parts) == 2:
        rows[code(unit + "/" + name)] = fake_id(t)
    else:
        rows[code(unit + "/" + parts[1])] = fake_id(f"{PKG}/{unit}/{parts[1]}")
tmp = tempfile.mkdtemp(prefix="live")
tab = os.path.join(tmp, "drive_tab.csv")
with open(tab, "w", encoding="utf-8", newline="") as f:
    f.write(f"windy-hill-drive,v2,2026-10-05T12:00Z,{len(rows)}\n" + "".join(f"{k},{v}\n" for k, v in sorted(rows.items())))
built = os.path.join(tmp, "in.xlsx"); out = os.path.join(tmp, "out")
r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "master_sheet.py"), built, "--drive-tab", tab], capture_output=True, text=True)
if r.returncode: sys.exit("the generator failed:\n" + r.stderr[-800:])
subprocess.run([SOFFICE, "--headless", "--convert-to", "xlsx:Calc MS Excel 2007 XML", "--outdir", out, built], capture_output=True, env=dict(os.environ, HOME=tmp), timeout=300)
r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "check_master_sheet.py"), os.path.join(out, "in.xlsx")], capture_output=True, text=True)
line = next((l for l in r.stdout.split("\n") if l.startswith("links:")), "")
m = re.search(r"\((\d+) lines there: (\d+) open the document itself, (\d+) fall back", line)
shutil.rmtree(tmp, ignore_errors=True)
print(line)
problems = []
if r.returncode: problems.append("the check found problems:\n" + "\n".join(r.stdout.strip().split("\n")[-8:]) + r.stderr[-400:])
if not m: problems.append("the check did not report live links")
elif not (int(m[1]) == len(rows) and int(m[2]) > 0 and int(m[3]) > 0): problems.append(f"expected {len(rows)} lines, some documents opened directly and {missing}'s by search")
print("\n".join(problems) if problems else f"live links: with every unit but '{missing}' in the stand-in Drive tab, the listed documents open by their own address and the rest by search; 0 problems")
sys.exit(1 if problems else 0)
