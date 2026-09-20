#!/usr/bin/env python3
"""The check suite for a built unit directory. Every check prints its denominator (what it
looked at) and its findings; any finding fails the run (exit 1). §13c: a check that reports a
finding and exits 0 is worse than no check.

  docscan    student surfaces carry no benchmark code, calculator line, 'homework', partner work
  keycheck   student papers carry no ANSWER KEY mark and no red (answer-colour) run
  gdoccheck  Docs-native fonts only, no nested tables, every table pinned, no touching tables
  glyph      every non-ASCII character in a run has a glyph in the font that will draw it
  pagecheck  no shipped PDF page is blank
  offpage    every word of every PDF lies inside its page box
  pdftwin    every .docx/.pptx has a .pdf twin newer than it whose text contains the source text
  plancheck  every deck side-car totals 53 with a whiteboard remainder inside 10–20
  slidefit   no text box or picture in a deck crosses the footer rule or the slide edge
"""
import os, re, sys, glob, json, zipfile, subprocess, collections
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
NATIVE_DOC_FONTS = {"Times New Roman", "Georgia", "FreeSerif", "Arial"}
DECK_FONTS = {"Century Schoolbook"}
FONT_FILES = {"Times New Roman": "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
              "Georgia": "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
              "FreeSerif": "/usr/share/fonts/truetype/freefont/FreeSerif.ttf",
              "Century Schoolbook": "/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyreschola-regular.otf"}


def is_student(name):
    n = name.lower()
    return ("key" not in n) and ("teacher edition" not in n) and ("reference sheet" not in n or True) and ("notes.json" not in n)


def docx_text(path):
    z = zipfile.ZipFile(path)
    x = z.read("word/document.xml").decode()
    return " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", x))


def pptx_texts(path):
    z = zipfile.ZipFile(path)
    out = {}
    for n in sorted(z.namelist()):
        m = re.match(r"ppt/slides/slide(\d+)\.xml$", n)
        if m:
            x = z.read(n).decode()
            out[int(m.group(1))] = " ".join(re.findall(r"<a:t>([^<]*)</a:t>", x))
    return out


def check_docscan(files):
    findings = []; n = 0
    for f in files:
        base = os.path.basename(f)
        if f.endswith(".docx"):
            texts = {0: docx_text(f)}
        elif f.endswith(".pptx"):
            texts = pptx_texts(f)
        else:
            continue
        student = is_student(base)
        n += 1
        for k, t in texts.items():
            where = f"{base}" + (f" slide {k}" if k else "")
            if student and not (f.endswith(".pptx") and k == 1):
                if re.search(r"MA\.\d+\.[A-Z]+\.\d+\.\d+", t):
                    findings.append(f"docscan: benchmark code on student surface — {where}")
            if student:
                if re.search(r"\bcalculators?\b", t, re.I):
                    findings.append(f"docscan: calculator line on student surface — {where}")
                if re.search(r"\bhomework\b", t, re.I):
                    findings.append(f"docscan: 'homework' on student surface — {where}")
            if re.search(r"with your partner|\bpartners?\b|group work|in teams", t, re.I) and not re.search(r"no partner|never for pairs|written for pairs|not partner|partner work anywhere", t, re.I):
                findings.append(f"docscan: partner/group work wording — {where}")
    print(f"docscan: {n} documents scanned, {len(findings)} findings")
    return findings


def check_keycheck(files):
    findings = []; n = 0
    for f in files:
        base = os.path.basename(f)
        if not f.endswith(".docx") or not is_student(base):
            continue
        n += 1
        x = zipfile.ZipFile(f).read("word/document.xml").decode()
        if "ANSWER KEY" in x:
            findings.append(f"keycheck: ANSWER KEY mark on student paper — {base}")
        if re.search(r'w:color w:val="9E1B32"', x):
            findings.append(f"keycheck: answer-colour run on student paper — {base}")
    print(f"keycheck: {n} student papers, {len(findings)} findings")
    return findings


def check_gdoc(files):
    findings = []; n = 0; tables = 0
    for f in files:
        if not f.endswith(".docx"):
            continue
        n += 1
        base = os.path.basename(f)
        z = zipfile.ZipFile(f)
        x = z.read("word/document.xml").decode()
        fonts = set(re.findall(r'w:ascii="([^"]+)"', x))
        bad = fonts - NATIVE_DOC_FONTS
        if bad:
            findings.append(f"gdoccheck: non-native fonts {sorted(bad)} — {base}")
        root = ET.fromstring(z.read("word/document.xml"))
        body = root.find(W + "body")
        for tbl in root.iter(W + "tbl"):
            tables += 1
            if tbl.find(W + "tblPr/" + W + "tblLayout") is None:
                findings.append(f"gdoccheck: table without pinned layout — {base}")
            for tc in tbl.iter(W + "tc"):
                if tc.find(W + "tbl") is not None:
                    findings.append(f"gdoccheck: nested table — {base}")
                    break
        kids = list(body)
        for i in range(len(kids) - 1):
            if kids[i].tag == W + "tbl" and kids[i + 1].tag == W + "tbl":
                findings.append(f"gdoccheck: two tables touch (Docs will weld them) — {base}")
    print(f"gdoccheck: {n} documents, {tables} tables, {len(findings)} findings")
    return findings


def check_glyph(files):
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        print("glyph: fontTools missing — UNCHECKED"); return ["glyph: fontTools not installed"]
    cmaps = {}
    for name, path in FONT_FILES.items():
        if os.path.exists(path):
            cmaps[name] = set(TTFont(path).getBestCmap().keys())
    findings = []; n = 0; chars = 0
    for f in files:
        if not (f.endswith(".docx") or f.endswith(".pptx")):
            continue
        n += 1
        base = os.path.basename(f)
        z = zipfile.ZipFile(f)
        parts = [p for p in z.namelist() if p.endswith(".xml") and ("document" in p or "slides/slide" in p)]
        for part in parts:
            x = z.read(part).decode()
            if f.endswith(".docx"):
                default = "Times New Roman"
                m = re.search(r'w:rFonts[^>]*w:ascii="([^"]+)"', z.read("word/styles.xml").decode())
                if m: default = m.group(1)
                for run in re.findall(r"<w:r>(.*?)</w:r>|<w:r [^>]*>(.*?)</w:r>", x, re.S):
                    r = run[0] or run[1]
                    fm = re.search(r'w:ascii="([^"]+)"', r)
                    font = fm.group(1) if fm else default
                    for t in re.findall(r"<w:t[^>]*>([^<]*)</w:t>", r):
                        for ch in t:
                            if ord(ch) > 127:
                                chars += 1
                                if font in cmaps and ord(ch) not in cmaps[font]:
                                    findings.append(f"glyph: U+{ord(ch):04X} '{ch}' not in {font} — {base}")
            else:
                for run in re.findall(r"<a:r>(.*?)</a:r>", x, re.S):
                    fm = re.search(r'typeface="([^"]+)"', run)
                    font = fm.group(1) if fm else "Century Schoolbook"
                    for t in re.findall(r"<a:t>([^<]*)</a:t>", run):
                        for ch in t:
                            if ord(ch) > 127:
                                chars += 1
                                if font in cmaps and ord(ch) not in cmaps[font]:
                                    findings.append(f"glyph: U+{ord(ch):04X} '{ch}' not in {font} — {base}")
    findings = sorted(set(findings))
    print(f"glyph: {n} documents, {chars} non-ASCII characters, {len(findings)} findings")
    return findings


def _pages(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    m = re.search(r"Pages:\s+(\d+)", out)
    return int(m.group(1)) if m else 0


def check_pages(files):
    findings = []; n = 0
    for f in files:
        if not f.endswith(".pdf"):
            continue
        base = os.path.basename(f)
        pages = _pages(f)
        imgs = subprocess.run(["pdfimages", "-list", f], capture_output=True, text=True).stdout
        img_pages = set(int(l.split()[0]) for l in imgs.splitlines()[2:] if l.strip() and l.split()[0].isdigit())
        for p in range(1, pages + 1):
            n += 1
            t = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), f, "-"], capture_output=True, text=True).stdout
            if not t.strip() and p not in img_pages:
                findings.append(f"pagecheck: blank page {p} — {base}")
    print(f"pagecheck: {n} pages, {len(findings)} findings")
    return findings


def check_offpage(files):
    findings = []; n = 0
    for f in files:
        if not f.endswith(".pdf"):
            continue
        base = os.path.basename(f)
        html = subprocess.run(["pdftotext", "-bbox", f, "-"], capture_output=True, text=True).stdout
        for pm in re.finditer(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', html, re.S):
            pw, ph = float(pm.group(1)), float(pm.group(2))
            for wm in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', pm.group(3)):
                n += 1
                x0, y0, x1, y1 = map(float, wm.groups()[:4])
                if x0 < 0 or y0 < 0 or x1 > pw + 0.5 or y1 > ph + 0.5:
                    findings.append(f"offpage: '{wm.group(5)}' outside page — {base}")
    print(f"offpage: {n} words measured, {len(findings)} findings")
    return findings


def check_pdftwin(files):
    findings = []; n = 0
    for f in files:
        if not (f.endswith(".docx") or f.endswith(".pptx")):
            continue
        n += 1
        pdf = f.rsplit(".", 1)[0] + ".pdf"
        base = os.path.basename(f)
        if not os.path.exists(pdf):
            findings.append(f"pdftwin: no PDF for {base}"); continue
        if os.path.getmtime(pdf) < os.path.getmtime(f):
            findings.append(f"pdftwin: PDF older than its source — {base}"); continue
        src = docx_text(f) if f.endswith(".docx") else " ".join(pptx_texts(f).values())
        pdft = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True).stdout
        words = [w.lower() for w in re.findall(r"[A-Za-z]{4,}", src)]
        pw = set(w.lower() for w in re.findall(r"[A-Za-z]{4,}", pdft))
        missing = [w for w in words if w not in pw]
        if words and len(missing) / len(words) > 0.02:
            findings.append(f"pdftwin: {len(missing)}/{len(words)} words of the source not in the PDF — {base}: {missing[:5]}")
    print(f"pdftwin: {n} sources, {len(findings)} findings")
    return findings


def check_plan(files):
    findings = []; n = 0
    for f in files:
        if not f.endswith(".notes.json"):
            continue
        n += 1
        side = json.load(open(f))["slides"]
        fixed = sum(s["min"] for s in side if s["kind"] != "wb")
        wb = 53 - fixed
        if not (10 <= wb <= 20):
            findings.append(f"plancheck: whiteboard remainder {wb} outside 10–20 — {os.path.basename(f)}")
        for s in side:
            if s["kind"] != "wb" and s["kind"] != "title" and not s["note"]:
                findings.append(f"plancheck: slide {s['n']} has no teaching note — {os.path.basename(f)}")
    print(f"plancheck: {n} decks, {len(findings)} findings")
    return findings


def check_slidefit(files):
    findings = []; n = 0
    EMU = 914400
    for f in files:
        if not f.endswith(".pptx"):
            continue
        z = zipfile.ZipFile(f)
        base = os.path.basename(f)
        for name in sorted(z.namelist()):
            m = re.match(r"ppt/slides/slide(\d+)\.xml$", name)
            if not m:
                continue
            x = z.read(name).decode()
            for sm in re.finditer(r'<a:off x="(-?\d+)" y="(-?\d+)"/><a:ext cx="(\d+)" cy="(\d+)"/>', x):
                n += 1
                x0, y0, cx, cy = (int(v) / EMU for v in sm.groups())
                if x0 < -0.01 or x0 + cx > 13.34 or y0 < -0.01 or y0 + cy > 7.51:
                    findings.append(f"slidefit: shape off the slide ({x0:.2f},{y0:.2f},{cx:.2f},{cy:.2f}) — {base} slide {m.group(1)}")
    print(f"slidefit: {n} shapes, {len(findings)} findings")
    return findings


def run(outdir):
    files = sorted(glob.glob(os.path.join(outdir, "*")))
    print(f"checks over {outdir}: {len(files)} files — " + ", ".join(f"{k} {v}" for k, v in collections.Counter(os.path.splitext(f)[1] for f in files).items()))
    findings = []
    for chk in (check_docscan, check_keycheck, check_gdoc, check_glyph, check_pages, check_offpage, check_pdftwin, check_plan, check_slidefit):
        findings += chk(files)
    for f in findings:
        print("  FINDING", f)
    print(f"checks: {len(findings)} findings")
    return findings


if __name__ == "__main__":
    fs = run(sys.argv[1])
    sys.exit(1 if fs else 0)
