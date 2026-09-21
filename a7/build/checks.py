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
  telength   ruling 26: no teacher's edition runs past four printed pages
  plancheck  every deck side-car totals 53 with a whiteboard remainder inside 10–20
  footer     nothing but the footer itself renders below a slide's footer rule
  slidefit   no text box or picture in a deck crosses the footer rule or the slide edge
  overlap    on a rendered slide, no two lines of text collide and no figure sits on any words
  imagedrift every image embedded in a .docx or .pptx is a file in the figure library, byte for byte
  suitecheck HOUSE STYLE's suite:a7 tables name every check this file and the build run, and only those
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
    # Teacher surfaces: keys, the Teacher Edition, and (ruling 25) the Lesson Plan, which carries
    # benchmark codes, the calculator note and the answers in red by design.
    return ("key" not in n) and ("teacher edition" not in n) and ("lesson plan" not in n) and ("notes.json" not in n)


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
                # HOUSE STYLE §13b: "describing what the FAST platform provides is a different thing and
                # belongs on the reference sheet" — the Reference Sheet may name the on-screen calculator.
                if re.search(r"\bcalculators?\b", t, re.I) and "Reference Sheet" not in base:
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


def check_telength(files):
    """Ruling 26: the teacher's edition is four pages or fewer, printed. A longer one is cut,
    not shrunk — so this is a content finding, never a reason to change the font."""
    findings = []; n = 0
    for f in files:
        base = os.path.basename(f)
        if not (base.endswith(".pdf") and "Teacher Edition" in base):
            continue
        n += 1
        pp = _pages(f)
        if pp > 4:
            findings.append(f"telength: {base} runs {pp} pages; ruling 26 caps the teacher's edition at 4 — cut it, do not shrink it")
    print(f"telength: {n} teacher's editions measured, {len(findings)} findings")
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


def check_footer(files):
    """Nothing but the footer may sit below a slide's footer rule. deckkit refuses a text box
    whose DECLARED height crosses the rule, but a box sized for one line that wraps to two slips
    past that guard, so the rendered PDF is checked too. The footer's own words are the ones that
    appear below the rule on every slide of the deck; anything else down there is a spill."""
    FOOT_PT = 6.78 * 72
    findings = []; n = 0
    WORD = re.compile(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>')
    for f in files:
        base = os.path.basename(f)
        if not (f.endswith(".pdf") and "Slides" in base):
            continue
        html = subprocess.run(["pdftotext", "-bbox", f, "-"], capture_output=True, text=True).stdout
        pages = re.findall(r'<page width="[\d.]+" height="[\d.]+">(.*?)</page>', html, re.S)
        # yMAX, not yMin: a wrapped line hangs below the rule while its top is still above it
        below = [[m.group(5) for m in WORD.finditer(p) if float(m.group(4)) > FOOT_PT + 2] for p in pages]
        if not below:
            continue
        common = set(below[0])
        for b in below[1:]:
            common &= set(b)
        for i, b in enumerate(below):
            n += len(b)
            extra = [w for w in b if w not in common and not w.strip().isdigit()]
            if extra:
                findings.append(f"footer: {' '.join(extra)[:60]!r} sits below the footer rule — {base} slide {i + 1}")
    print(f"footer: {n} words below the rule, {len(findings)} findings")
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


def check_overlap(files):
    """§13 item 7: two checks the bbox and the eye both miss — text drawn over text, and a figure
    drawn over words — read from the RENDERED slide PDF. A filled panel or a drawn rule is an
    image too, and text sits on those by design; they are told apart from a figure by their
    pixels (a flat fill has no ink), and the count skipped is printed as part of the denominator.
    Thresholds: two lines collide when their boxes share more than 0.38 of the shorter line's
    height (a wrapped continuation line shares none — it sits below); a figure collides with a
    line when the shared area is more than 15% of the smaller of the two."""
    import io as _io, itertools
    try:
        import pymupdf
        from PIL import Image, ImageStat
    except ImportError as e:
        return [f"overlap: cannot run ({e})"]
    findings = []; nl = nf = npanel = 0; ndecks = 0
    for f in files:
        if not f.endswith("Slides.pdf"):
            continue
        ndecks += 1
        base = os.path.basename(f)
        d = pymupdf.open(f); flat = {}
        def is_flat(xref):
            if xref not in flat:
                try:
                    im = Image.open(_io.BytesIO(d.extract_image(xref)["image"])).convert("L")
                    flat[xref] = ImageStat.Stat(im).stddev[0] < 3.0
                except Exception:
                    flat[xref] = False
            return flat[xref]
        for pno, pg in enumerate(d, 1):
            lines = []
            for b in pg.get_text("dict")["blocks"]:
                if b["type"] != 0:
                    continue
                for ln in b["lines"]:
                    t = "".join(sp["text"] for sp in ln["spans"]).strip()
                    if t:
                        lines.append((pymupdf.Rect(ln["bbox"]), t))
            figs = []
            for im in pg.get_image_info(xrefs=True):
                if im.get("xref") and is_flat(im["xref"]):
                    npanel += 1
                    continue
                figs.append(pymupdf.Rect(im["bbox"]))
            nl += len(lines); nf += len(figs)
            for (ra, ta), (rb, tb) in itertools.combinations(lines, 2):
                x = ra & rb
                if not x.is_empty and x.height > 0.38 * min(ra.height, rb.height) and x.width > 1:
                    findings.append(f"overlap: text on text, {base} slide {pno}: {ta[:40]!r} ~ {tb[:40]!r}")
            for (ra, ta), rf in itertools.product(lines, figs):
                x = ra & rf
                if not x.is_empty and x.width > 2 and x.height > 2 and x.get_area() > 0.15 * min(ra.get_area(), rf.get_area()):
                    findings.append(f"overlap: figure on text, {base} slide {pno}: {ta[:40]!r} under a figure at {[round(v) for v in rf]}")
    if ndecks == 0:
        findings.append("overlap: examined NO decks")
    print(f"overlap: {ndecks} decks, {nl} text lines, {nf} figures ({npanel} panels and rules skipped as flat fills), {len(findings)} findings")
    return findings


def check_imagedrift(files):
    """§13's imagedrift: a document embeds a COPY of each figure at build time. Every embedded image
    must be, byte for byte, a file in figs/ — otherwise the document was built from a figure the
    library no longer has (an orphan) or from an older rendering of one (drift), and rebuilding it
    would change what students see."""
    import hashlib
    figs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
    lib = set()
    for p in glob.glob(os.path.join(figs, "*.png")):
        with open(p, "rb") as fh:
            lib.add(hashlib.sha256(fh.read()).hexdigest())
    findings = []; ndocs = nimg = 0
    for f in files:
        if not f.endswith((".docx", ".pptx")):
            continue
        ndocs += 1
        z = zipfile.ZipFile(f)
        for n in z.namelist():
            if "/media/" not in n:
                continue
            nimg += 1
            if hashlib.sha256(z.read(n)).hexdigest() not in lib:
                findings.append(f"imagedrift: {os.path.basename(f)} embeds {n}, which is not in the figure library")
    if ndocs == 0 or nimg == 0:
        findings.append(f"imagedrift: examined {ndocs} documents and {nimg} images — a check that examined nothing cannot be clean")
    print(f"imagedrift: {ndocs} documents, {nimg} embedded images against {len(lib)} library files, {len(findings)} findings")
    return findings


SUITE_DOC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "reference", "HOUSE STYLE.md")
BUILD_GATES = ("mathcheck", "distractorcheck", "capcheck", "rulingcheck")


def check_suite(files):
    """HOUSE STYLE §13c: a list of what a system does is a claim about that system, and any list a
    script could derive must be derived. The suite:a7 block carries two tables — the build gates
    and this file's checks. Each must name every check that runs, and only those."""
    findings = []
    try:
        txt = open(SUITE_DOC, encoding="utf-8").read()
    except OSError as e:
        return [f"suitecheck: cannot read HOUSE STYLE ({e})"]
    m = re.search(r"<!-- suite:a7.*?-->(.*?)(?=\n## |\n<!-- suite:)", txt, re.S)
    if not m:
        return ["suitecheck: no suite:a7 block in HOUSE STYLE"]
    block = m.group(1)
    def rows(label):
        t = re.search(r"\| *" + re.escape(label) + r" *\|.*?\n\|[-| ]+\|\n((?:\|.*\n)+)", block)
        return [] if not t else re.findall(r"^\| *`([a-z]+)`", t.group(1), re.M)
    have_build = rows("gate (A7, at build)")
    have_docs = rows("check (A7, checks.py)")
    want_docs = [fn.__name__.replace("check_", "") for fn in RUN_LIST]
    alias = {"gdoc": "gdoccheck", "pages": "pagecheck", "plan": "plancheck", "suite": "suitecheck"}
    want_docs = [alias.get(n, n) for n in want_docs]
    for missing in [n for n in BUILD_GATES if n not in have_build]:
        findings.append(f"suitecheck: build gate `{missing}` runs but has no row in HOUSE STYLE's suite:a7 table")
    for extra in [n for n in have_build if n not in BUILD_GATES]:
        findings.append(f"suitecheck: HOUSE STYLE names build gate `{extra}`, which nothing runs")
    for missing in [n for n in want_docs if n not in have_docs]:
        findings.append(f"suitecheck: `{missing}` runs in checks.py but has no row in HOUSE STYLE's suite:a7 table")
    for extra in [n for n in have_docs if n not in want_docs]:
        findings.append(f"suitecheck: HOUSE STYLE names `{extra}`, which checks.py does not run")
    cnt = re.search(r"checks\.py` \((\w+)", block)
    words = {"eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16}
    if cnt and words.get(cnt.group(1)) not in (None, len(want_docs)):
        findings.append(f"suitecheck: HOUSE STYLE says checks.py runs {cnt.group(1)}; it runs {len(want_docs)}")
    print(f"suitecheck: {len(have_build)} gate rows and {len(have_docs)} check rows read against {len(BUILD_GATES)} gates and {len(want_docs)} checks, {len(findings)} findings")
    return findings


RUN_LIST = (check_docscan, check_keycheck, check_gdoc, check_glyph, check_pages, check_offpage, check_pdftwin,
            check_telength, check_footer, check_plan, check_slidefit, check_overlap, check_imagedrift, check_suite)


def run(outdir):
    files = sorted(glob.glob(os.path.join(outdir, "*")))
    print(f"checks over {outdir}: {len(files)} files — " + ", ".join(f"{k} {v}" for k, v in collections.Counter(os.path.splitext(f)[1] for f in files).items()))
    findings = []
    for chk in RUN_LIST:
        findings += chk(files)
    for f in findings:
        print("  FINDING", f)
    print(f"checks: {len(findings)} findings")
    return findings


if __name__ == "__main__":
    fs = run(sys.argv[1])
    sys.exit(1 if fs else 0)
