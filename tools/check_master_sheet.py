#!/usr/bin/env python3
"""Check `A7 Master Sheet 2026-27.xlsx` against its sources, independently of the generator.

    python3 tools/master_sheet.py && python3 <xlsx skill>/scripts/recalc.py "<xlsx>" && python3 tools/check_master_sheet.py

Parses every source its own way (not with master_sheet.py's helpers) and reads the recalculated
values: every row, date, weekday and due date against the calendar; every link against the git
tree (and each deck's title slide against its row); every built lesson's target, question, vocabulary,
closure and MTRs against its spec; the benchmark wording against the Source of Truth; the Math
Nation lessons against the book's contents; the IXL tracker against the due-date sheet; each unit
test's question map and points against its spec; the month grid against the school days; no
LaTeX left anywhere. With Florida's B.E.S.T. standards text present (outside the repo, at
/root/best), also checks the MTR titles and that every Source of Truth statement is complete and
verbatim. Exit status 1 on any problem."""
import os, re, sys, csv, glob, hashlib, unicodedata, subprocess, datetime, urllib.parse, importlib.util, collections, io, contextlib
import pymupdf
from openpyxl import load_workbook
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
XLSX = sys.argv[1] if len(sys.argv) > 1 else f"{ROOT}/a7/reference/A7 Master Sheet 2026-27.xlsx"
REF = f"{ROOT}/a7/reference"
BASE = "https://github.com/croix18/croix18-windy-hill-a7/"
P = []
def bad(*a): P.append(" ".join(str(x) for x in a))
# what the next commit will hold: the index and every file on disk that git does not ignore (push.sh
# commits with `git add -A`), so the check can run before the commit it guards. -z: names with
# commas and spaces come back unquoted.
tracked = {t for t in subprocess.run(["git", "-C", ROOT, "ls-files", "-z", "-c", "-o", "--exclude-standard"],
                                     capture_output=True, text=True).stdout.split("\0")
           if t and os.path.exists(os.path.join(ROOT, t))}
PKG = "a7/packages/"
URL_MAX = 255
DRIVE = "https://drive.google.com/drive/search?q="
# Everything Drive will hold once the packages are in it: every file the commit keeps under the
# packages folder, and every folder above one.
PKG_FILES = sorted(t for t in tracked if t.startswith(PKG))
PKG_DIRS = sorted({"/".join(t.split("/")[:k]) for t in PKG_FILES for k in range(3, t.count("/") + 1)})
def words(s): return re.findall(r"[a-z0-9]+", s.lower())
def holds(title, phrase):
    """Does a title hold a phrase, word for word, as Drive's title search reads it? (The last word may
    be the start of a longer one: Drive matches a word by its beginning.)"""
    t, ph = words(title), words(phrase)
    return any(t[k:k + len(ph) - 1] == ph[:-1] and t[k + len(ph) - 1].startswith(ph[-1]) for k in range(len(t) - len(ph) + 1)) if ph else False
def found(url, where):
    """What a Drive search link finds among the packages: (is it a folder search, the paths found)."""
    q = urllib.parse.unquote(url[len(DRIVE):])
    phrases = re.findall(r'title:"([^"]*)"', q); folder = q.endswith(" type:folder")
    if len(phrases) != 1 or f'title:"{phrases[0]}"' + (" type:folder" if folder else "") != q: bad(f"{where}: a Drive search this check cannot read:", q); return folder, []
    return folder, [t for t in (PKG_DIRS if folder else PKG_FILES) if holds(t.rsplit("/", 1)[-1], phrases[0])]
def only_name(path):
    """Does the name alone say which file this is, anywhere in his Drive (so a search finds it alone, and
    a code can be made from it)? A unit's folder; or a document named for its course that no other
    package path shares. A bare name — a lesson folder "2.01", a START HERE — does not."""
    parts = path.split("/"); n = parts[-1]
    return len(parts) == 3 or (n.startswith(parts[2].split(" ")[0] + " ") and sum(1 for t in PKG_FILES + PKG_DIRS if t.rsplit("/", 1)[-1] == n) == 1)
def filed(name): return "k" + hashlib.md5(unicodedata.normalize("NFC", name).encode("utf-8")).hexdigest()[:12]
def codes_of(path):
    """The codes the Drive tab may file a package path under: its name, when no other path has it (a
    unit's folder always may); and "<unit folder>/<name>" when it sits directly in its unit's folder."""
    parts = path.split("/"); name = parts[-1]; out = []
    if only_name(path): out.append(filed(name))
    if len(parts) == 4: out.append(filed(parts[2] + "/" + name))
    return out
def blob_url(path): return BASE + "blob/main/" + urllib.parse.quote(path, safe="/,()")
def canonical(kind, path): return BASE + ("tree" if kind == "tree" else "blob") + "/main/" + urllib.parse.quote(path, safe="/,()")
# The two editions of the workbook. GitHub's: a link is the cell's own hyperlink to the repository.
# Drive's (the one Croix gets): a link cell reads =HYPERLINK(Links!$X$n,"text"), and that Links cell
# looks the document's Drive address up by its code in the hidden Drive tab, with a search for the
# file's exact name to fall back on. read_links() takes every such cell apart — the code must be the
# code of one package path, the fallback must find that same path and nothing else, the address the
# file last calculated must be what the Drive tab gives — and then hands the rest of this check the
# link as the repository path it means, so everything below holds both editions to the same rules.
DRIVE_MODE = False
LIVE = {}                                   # (sheet, cell) -> {text, kind: blob|tree|search, path, code, fallback, url}
DTAB = {}                                   # the workbook's Drive tab: code -> Drive id
CELL = re.compile(r'=HYPERLINK\(Links!\$([A-Z]+)\$(\d+),"((?:[^"]|"")*)"\)')
LOOK = re.compile(r'=IFERROR\("(https://drive\.google\.com/file/d/|https://drive\.google\.com/drive/folders/)"&VLOOKUP\("(k[0-9a-f]{12})",Drive!\$A:\$B,2,0\)(&"/view")?,"([^"]+)"\)')
def read_links(wb, wbf):
    global DRIVE_MODE
    DRIVE_MODE = "Drive" in wb.sheetnames
    if not DRIVE_MODE:
        return
    dt = [[c for c in r] for r in wb["Drive"].iter_rows(values_only=True) if any(c is not None for c in r)]
    if not dt or dt[0][0] != "windy-hill-drive" or wb["Drive"].sheet_state != "hidden": bad("the Drive tab is not a hidden tab that opens with windy-hill-drive")
    for r in dt[1:]:
        if not re.fullmatch(r"k[0-9a-f]{12}", str(r[0])) or not re.fullmatch(r"[A-Za-z0-9_-]{20,60}", str(r[1])) or r[0] in DTAB: bad("Drive tab line", r[:2]); continue
        DTAB[r[0]] = r[1]
    keyed = {}
    for t in PKG_FILES + PKG_DIRS:
        for c in codes_of(t):
            if c in keyed: bad("two package paths share a code:", t, keyed[c])
            keyed[c] = t
    used = collections.Counter()
    for s in wbf:
        for row in s.iter_rows():
            for x in row:
                where = f"{s.title} {x.coordinate}"
                if x.hyperlink and x.hyperlink.target: bad(f"{where}: a fixed link in a workbook whose links are looked up:", x.hyperlink.target)
                if s.title in ("Today", "Links", "Drive") or not (isinstance(x.value, str) and x.value.startswith("=HYPERLINK(")): continue
                m = CELL.fullmatch(x.value)
                if not m: bad(f"{where}: a link this check cannot read:", x.value); continue
                at = f"{m[1]}{m[2]}"; used[at] += 1
                text = m[3].replace('""', '"'); src = wbf["Links"][at].value; url = wb["Links"][at].value
                if wb[s.title][x.coordinate].value != text: bad(f"{where}: reads", wb[s.title][x.coordinate].value, "but its formula says", text)
                if x.font.underline != "single": bad(f"{where}: a link that does not look like one")
                if not isinstance(url, str) or len(url) > URL_MAX: bad(f"{where}: its address is not text of at most {URL_MAX} characters"); continue
                lm = LOOK.fullmatch(src) if isinstance(src, str) else None
                if lm:
                    head, code, view, fb = lm.groups(); folder = head.endswith("folders/")
                    if folder == bool(view): bad(f"{where}: a folder's address ending /view, or a file's without it")
                    path = keyed.get(code)
                    if not path: bad(f"{where}: its code is no package file's:", code); continue
                    if (path in PKG_DIRS) != folder: bad(f"{where}: a file looked up as a folder, or the other way round:", path); continue
                    if len(fb) > URL_MAX: bad(f"{where}: a fallback of {len(fb)} characters")
                    fb_folder, hits = found(fb, where); unit = "/".join(path.split("/")[:3])
                    if only_name(path):
                        if hits != [path] or fb_folder != folder: bad(f"{where}: its fallback search should find {path} alone; it finds", hits[:3])
                    elif not fb_folder or hits != [unit]: bad(f"{where}: {path} shares its name, so its fallback should open the unit's folder; it finds", hits[:3])
                    want = head + DTAB[code] + ("" if folder else "/view") if code in DTAB else fb
                    if url != want: bad(f"{where}: the file last calculated {url}; the Drive tab gives {want}")
                    LIVE[(s.title, x.coordinate)] = dict(text=text, kind="tree" if folder else "blob", path=path, code=code, fallback=fb, url=url, direct=code in DTAB)
                    wb[s.title][x.coordinate].hyperlink = canonical("tree" if folder else "blob", path)
                elif isinstance(src, str) and src.startswith(DRIVE):       # a search and nothing else
                    if url != src: bad(f"{where}: the file last calculated {url} for a plain search")
                    folder, hits = found(src, where)
                    LIVE[(s.title, x.coordinate)] = dict(text=text, kind="tree" if folder else "search", path=hits[0] if folder and len(hits) == 1 else None, code=None, fallback=src, url=url, hits=hits, direct=False)
                    if folder:
                        if len(hits) != 1: bad(f"{where}: a folder search that finds {len(hits)} folders"); continue
                        wb[s.title][x.coordinate].hyperlink = canonical("tree", hits[0])
                else:
                    bad(f"{where}: its Links cell {at} holds neither a lookup nor a search:", str(src)[:80])
    # nothing on the Links tab that no cell opens, and nothing opened twice
    wl = wbf["Links"]; n = [c.value for c in wl[1]].index("Where")           # the grid ends two columns before "Where"
    for row in wl.iter_rows(min_row=2):
        for x in list(row[1:n - 1]) + [row[n + 2]]:
            if x.value is not None and used[x.coordinate] != 1: bad(f"Links {x.coordinate}: opened by {used[x.coordinate]} cells")
        if row[n].value is not None or row[n + 2].value is not None:
            m = re.fullmatch(r"'([^']+)'!([A-Z]+\d+)", str(row[n].value))
            hit = LIVE.get((m[1], m[2])) if m else None
            cell = wbf[m[1]][m[2]].value if m and m[1] in wbf.sheetnames else None
            if not hit or cell != '=HYPERLINK(Links!$%s$%d,"%s")' % (row[n + 2].column_letter, row[n + 2].row, str(row[n + 1].value).replace('"', '""')): bad(f"Links row {row[n].row}: {row[n].value} does not open it, or reads something else")
    if any(c not in keyed for c in DTAB): pass   # the Drive tab may hold more than this course's files (the other course's): not an error
def linked(cell):
    """Does the cell open something — a document, a folder, or a search?"""
    return bool(cell.hyperlink) or (cell.parent.title, cell.coordinate) in LIVE
def target(url, where):
    """(kind, path): 'blob' a document, 'tree' a folder."""
    if not url.startswith(BASE): bad(f"{where}: foreign link", url); return None, None
    kind, rest = url[len(BASE):].split("/main/", 1); path = urllib.parse.unquote(rest)
    if kind == "blob" and path not in tracked: bad(f"{where}: links a file the commit will not hold:", path)
    if kind == "tree" and not any(t.startswith(path + "/") for t in tracked): bad(f"{where}: links an empty folder:", path)
    return kind, path
def every_link(cell, where):
    """Any link, on any tab: it reaches something the commit holds, it is not longer than URL_MAX (a
    longer one is cut off when the sheet is saved; a looked-up link's own lengths are held in
    read_links), and only a cell that reads "in folder" or "folder" may open a folder in place of a
    document."""
    url = cell.hyperlink.target
    if not DRIVE_MODE and len(url) > URL_MAX: bad(f"{where}: a link of {len(url)} characters")
    kind, path = target(url, where)
    if kind == "blob" and cell.value in ("in folder", "folder"): bad(f"{where}: says '{cell.value}' but opens a file")
    if kind == "tree" and cell.value not in ("in folder", "folder"): bad(f"{where}: opens a folder but reads", cell.value)
    return kind, path
def meant(path, start, tail, where):
    """A document's link that opens a folder instead: right only when no link reaches the file itself —
    on GitHub because its address would be too long, in Drive because it has no code of its own.
    Returns the one file in that folder the link stands for."""
    hits = [t for t in tracked if t.startswith(path + "/") and "/" not in t[len(path) + 1:]
            and t.rsplit("/", 1)[-1].startswith(start) and t.endswith(tail)
            and t.rsplit("/", 1)[-1].count(" - ") == tail.count(" - ")]
    if len(hits) != 1: bad(f"{where}: the folder holds {len(hits)} files it could mean", path); return None
    if DRIVE_MODE:
        if codes_of(hits[0]): bad(f"{where}: opens the folder though the file has a code of its own", hits[0])
    elif len(blob_url(hits[0])) <= URL_MAX: bad(f"{where}: opens the folder though the file's own link fits", hits[0])
    return hits[0]
def held(cell, start, tail, where):
    """The document a cell links, by what its name starts and ends with; None when there is no link."""
    if not cell.hyperlink: return None
    kind, path = every_link(cell, where)
    if kind is None: return None
    if kind == "tree":
        if cell.value != "in folder": bad(f"{where}: a document's link opens a folder but reads", cell.value); return None
        path = meant(path, start, tail, where)
        if path is None: return None
    name = path.rsplit("/", 1)[-1]
    if not (name.startswith(start) and name.endswith(tail) and name.count(" - ") == tail.count(" - ")):
        bad(f"{where} ->", name, f"(wanted {start}… {tail})")
    return path if path in tracked else None          # a file the commit will not hold is already reported
def folder_ok(cell, want, where):
    """A folder's link: the folder itself — or, in Drive, where it has no code of its own, the unit's
    folder that holds it, and the cell then reads "in folder"."""
    kind, path = every_link(cell, where)
    if kind is None: return
    if DRIVE_MODE and not codes_of(want):
        unit = "/".join(want.split("/")[:3])
        if (kind, path, cell.value) != ("tree", unit, "in folder"): bad(f"{where}: should open the unit's folder and read 'in folder'", path, cell.value)
    elif (kind, path, cell.value) != ("tree", want, "folder"): bad(f"{where}: should open", want, "and read 'folder'; opens", path, "reads", cell.value)
MON = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
def d(s):
    m, day = s.split()[-2:]; return datetime.date(2026 if MON[m] >= 7 else 2027, MON[m], int(day))
def D(v): return v.date() if isinstance(v, datetime.datetime) else v
def norm(s): return re.sub(r"[^a-z0-9]", "", s.lower())

# ---------------- sources, parsed independently
cal = [[c.strip() for c in l.strip().strip("|").split("|")] for l in open(f"{REF}/A7 Scope and Sequence 2026-27.md", encoding="utf-8") if l.startswith("| ") and not l.startswith("| Date")]
due = [[c.strip() for c in l.strip().strip("|").split("|")] for l in open(f"{REF}/A7 IXL Due Dates 2026-27.md", encoding="utf-8") if l.startswith("| ") and not l.startswith("| Assigned")]
sot_txt = open(f"{REF}/Florida BEST Grade 8 - Source of Truth.md", encoding="utf-8").read()
SOT = {}
for m in re.finditer(r"^\*\*(MA\.[\w.]+)\*\* — (.+)$", sot_txt, re.M):
    SOT[m.group(1)] = re.sub(r"\*", "", m.group(2)).strip()
toc_txt = open(f"{REF}/A7 IXL Skill Plan and Book Contents.md", encoding="utf-8").read()
STD = "/root/best/std/mathbeststandardsfinal/mathbeststandardsfinal.txt"
std = open(STD, encoding="utf-8", errors="replace").read() if os.path.exists(STD) else None
std_n = norm(std.replace(" - ", "-")) if std else None
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, os.path.join(ROOT, "a7", "build"))
import tex2text
with contextlib.redirect_stdout(io.StringIO()):
    import scope_calendar as SC
specs = {}
for f in glob.glob(f"{ROOT}/a7/build/u*/l*.py"):
    s = importlib.util.spec_from_file_location("m", f); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); specs[m.L["code"]] = m.L
stem = lambda code, u: (f"{u}.T{code[-1]}" if code.startswith("T-") else re.split(r"[+–]", code)[0])

wb = load_workbook(XLSX, data_only=True)
wbf = load_workbook(XLSX)                  # formulas
read_links(wb, wbf)
print("tabs:", [s.title + ("(hidden)" if s.sheet_state == "hidden" else "") for s in wb])

# ---------------- Scope & Sequence
ws = wb["Scope & Sequence"]; hdr = [c.value for c in ws[1]]; H = {h: i for i, h in enumerate(hdr)}
rows = list(ws.iter_rows(min_row=2))
if len(rows) != len(cal): bad("scope rows", len(rows), "calendar", len(cal))
prev = None; nlinks = 0; built_rows = 0
FILE = {}                                  # (row, column) -> the document a lesson's link stands for
OPENS = {}                                 # (row, column) -> what any link on the row opens
for i, (cells, c) in enumerate(zip(rows, cal), 2):
    v = {h: cells[j].value for h, j in H.items()}
    dt = D(v["Date"])
    if dt != d(c[0]): bad(f"r{i} date")
    if dt.strftime("%a") != c[1][:3]: bad(f"r{i} weekday", dt, c[1])
    if prev and dt <= prev: bad(f"r{i} order")
    prev = dt
    if v["Day"] != c[1] or (v["Unit"] or "") != (int(c[2]) if c[2] else "") or v["Lesson"] != c[3]: bad(f"r{i} day/unit/code")
    want = re.sub(r"\*", "", re.sub(r"^\*{1,2}\w+\*{1,2}\s*", "", c[4])).strip()
    if v["What is taught"] != want: bad(f"r{i} taught", repr(v["What is taught"])[:60], repr(want)[:60])
    if (v["Benchmark"] or "") != c[5] or (v["IXL skills — all required, code"] or "") != c[6]: bad(f"r{i} bm/ixl")
    if (D(v["IXL due"]) if v["IXL due"] else "") != (d(c[7]) if c[7] else ""): bad(f"r{i} due")
    code, u = c[3], int(c[2]) if c[2] else None
    exam = bool(re.fullmatch(r"[\d/]+\.X\d", code))
    # links
    for h in hdr[5:16]:
        cell = cells[H[h]]
        if cell.hyperlink:
            nlinks += 1
            kind, path = every_link(cell, f"r{i} {code} {h}")
            if kind is None: continue
            OPENS[(i, h)] = path
            if h == "Unit folder":
                if kind != "tree" or not path.startswith(f"a7/packages/A7 Unit {u} - ") or path.count("/") != 2 or cell.value != "folder": bad(f"r{i} {code}: not its unit's folder", path, cell.value)
            if h != "Unit folder" and not exam and code != "spiral":
                s = stem(code, u)
                # the by-lesson layout (4 Oct 2026): "A7 <s> <Title> - <kind>[ - Key].<ext>"; the title is in
                # the name, so a link is held to its number and to what the file is
                want_tail = {"Slides (PDF)": " - Slides.pdf", "Slides (PowerPoint)": " - Slides.pptx",
                             "Teacher Edition": " - Teacher Edition.pdf", "Lesson Plan": " - Lesson Plan.pdf",
                             "Question Bank": " - Question Bank.pdf", "Bank key": " - Question Bank - Key.pdf",
                             "Bank – Additional": " - Additional Question Bank.pdf",
                             "Additional key": " - Additional Question Bank - Key.pdf",
                             "Independent Set": " - Independent Set.pdf", "Independent key": " - Independent Set - Key.pdf"}[h]
                if kind == "tree":                         # the file's own link would not fit: its folder
                    if cell.value != "in folder": bad(f"r{i} {code} {h}: opens a folder but reads", cell.value)
                    path = meant(path, f"A7 {s} ", want_tail, f"r{i} {code} {h}")
                    if path is None: continue
                FILE[(i, h)] = path
                name = path.rsplit("/", 1)[-1]
                if not (name.startswith(f"A7 {s} ") and name.endswith(want_tail) and name.count(" - ") == want_tail.count(" - ")):
                    bad(f"r{i} {code} {h} ->", name)
                if f"/Lessons/{s}/" not in path: bad(f"r{i} {code} {h} not in its lesson's folder", path)
                if not path.startswith(f"a7/packages/A7 Unit {u} - "): bad(f"r{i} wrong unit folder", path)
    # a lesson's row searches Drive for everything named for it: ours, his copies, his own files
    EVERY = "Everything for this lesson"; ev = LIVE.get((ws.title, cells[H[EVERY]].coordinate))
    if DRIVE_MODE and not exam and code not in ("spiral", "flex", "extra", "off") and not code.startswith("PM"):
        phrase = f"A7 {stem(code, u)}"
        if not ev or ev["kind"] != "search" or ev["text"] != "search" or ev["url"] != DRIVE + urllib.parse.quote(f'title:"{phrase}"', safe=":"): bad(f"r{i} {code}: its search for everything named for the lesson", ev and ev["url"])
        elif any(not holds(t.rsplit("/", 1)[-1], phrase) for t in PKG_FILES if f"/Lessons/{stem(code, u)}/" in t and t.startswith(f"a7/packages/A7 Unit {u} - ")): bad(f"r{i} {code}: its search would miss one of the lesson's own files")
    elif ev or cells[H[EVERY]].value is not None: bad(f"r{i} {code}: a search for a day that is not a lesson (or in a GitHub workbook)")
    if exam or code == "spiral":
        t1 = OPENS.get((i, "Slides (PDF)")); t2 = OPENS.get((i, "Bank key"))
        if u in (3, 4):
            w1, w2 = (" - Test.pdf", " - Test - Key.pdf") if exam else (" - Review.pdf", " - Review - Key.pdf")
            sub = "Assessment" if exam else "Review"
            if not (t1 and t1.endswith(w1) and t1.startswith(f"a7/packages/A7 Unit {u} - ") and f"/{sub}/A7 Unit {u} " in t1) or not (t2 and t2.endswith(w2) and f"/{sub}/A7 Unit {u} " in t2): bad(f"r{i} {code} paper/key links")
    lesson_like = not exam and code not in ("spiral", "flex", "extra", "off") and not code.startswith("PM")
    if u in (3, 4) and lesson_like:
        built_rows += 1
        missing = [h for h in hdr[5:16] if not cells[H[h]].hyperlink]
        if missing: bad(f"r{i} {code} missing links", missing)
        L = specs[stem(code, u)]
        if v["Learning target"] != L["target"] or v["Essential question"] != L["essential"]: bad(f"r{i} target/EQ")
        if v["Vocabulary"] != ", ".join(t for t, _ in L["vocab"]): bad(f"r{i} vocab")
        b9 = L["whiteboard"][8]
        if v["Closure question (board 9)"] != b9["qtext"] or v["Closure answer"] != b9["answer"]: bad(f"r{i} closure")
        mt = v["MTRs (tap for where they show up)"].split("\n")
        if [x.split(" ")[0] for x in mt] != [f"MA.K12.{k}" for k, _ in L["mtr"]]: bad(f"r{i} MTR codes")
        for x in mt:
            title = x.split(" ", 1)[1]
            if std_n and norm(title) not in std_n: bad(f"r{i} MTR title not in the standards:", title)
        if not cells[H["MTRs (tap for where they show up)"]].comment or not cells[H["Closure question (board 9)"]].comment: bad(f"r{i} comment missing")
        # slide 1 names the lesson
        pth = FILE.get((i, "Slides (PDF)"))            # None: the link is already reported
        if pth and pth in tracked:
            head = pymupdf.open(f"{ROOT}/{pth}")[0].get_text().split("\n")[0].strip()
            lab = L.get("label") or f"Lesson {L['lesson_no']}"
            if head != f"GRADE 7 ACCELERATED  ·  UNIT {u}  ·  {lab.upper()}": bad(f"r{i} slide 1 reads", head)
    if u and u >= 5 and lesson_like:
        if v["Slides (PDF)"] != "not built yet" or any(cells[H[h]].hyperlink for h in hdr[5:16]): bad(f"r{i} unbuilt row")
    # benchmark wording
    for part in (v["Benchmark wording"] or "").split("\n\n"):
        if not part: continue
        code_b, text_b = part.split(" — ", 1)
        if code_b in SOT:
            if text_b != SOT[code_b]: bad(f"r{i} wording differs for", code_b)
        elif not (code_b.startswith("MA.912") or re.fullmatch(r"MA\.\d+\.[A-Z]+\.\d+", code_b)): bad(f"r{i} unknown benchmark", code_b)
    toks = [b.strip() for b in c[5].split("·") if b.strip()]
    got = [p.split(" — ")[0] for p in (v["Benchmark wording"] or "").split("\n\n") if p]
    exp = []
    for b in toks:
        m = re.fullmatch(r"(\d+)\.([A-Z]+)\.(\d+)\.(\d+)–(\d+)\.(\d+)", b)
        exp += [f"MA.{m[1]}.{m[2]}.{m[3]}.{k}" for k in range(int(m[4]), int(m[6]) + 1)] if m else ["MA." + b]
    if got != exp: bad(f"r{i} wording codes", got, exp)
    # Math Nation lessons: each line 'N.M Title' must be a lesson of the book, and match the calendar code
    mn = [x for x in (v["Math Nation lesson(s)"] or "").split("\n") if x]
    for x in mn:
        if x not in toc_txt: bad(f"r{i} MN line not in the book's contents:", x)
    nums = [t for x in mn for t in re.findall(r"^(\d+\.\d+)(?: / (\d+\.\d+))?", x)[0] if t]
    if lesson_like:
        if code.startswith("T-"):
            want = {"T-A1": ["14.1", "14.2"], "T-A2": ["14.3", "14.4"], "T-B1": ["16.1"], "T-B2": ["16.2"], "T-C1": ["17.1"], "T-C2": ["17.2", "17.3"]}[code]
        else:
            mm = re.match(r"(\d+)\.(\d+)(.*)$", code); U_, a, rest = int(mm[1]), int(mm[2]), mm[3]
            extra = [int(x) for x in re.findall(r"\d+", rest)]
            want = [a] + extra if "–" not in rest else list(range(a, extra[-1] + 1))
            want = [f"{U_}.{k}" for k in want]
        want = [w for w in want if re.search(r"(?m)(^|[/·] )" + re.escape(w) + r"( |$)", toc_txt)]
        if nums != want: bad(f"r{i} {code} book lessons", nums, want)
print(f"scope: {len(rows)} rows, {nlinks} links, {built_rows} built lesson rows checked field by field")

# ---------------- Source of Truth statements: complete and verbatim against the official stext
# Two statements cannot be matched automatically and were checked by eye against the published pages
# on 21 Sep 2026: the PDF stext loses the superscripts in 8.AR.2.3 (x² = p, x³ = q), and a fraction
# from 7.NSO.1.1's clarification spills into 7.NSO.1.2.
SEEN = {"MA.8.AR.2.3", "MA.7.NSO.1.2"}
if std:
    import unicodedata
    raw = unicodedata.normalize("NFKC", std)
    CODE = r"MA\s*\.\s*(?:K12|\d+)\s*\.\s*[A-Z](?:\s*[A-Z])*\s*\.\s*\d+\s*\.\s*\d+(?!\s*\.\s*\d)"
    lines = []
    for l in raw.splitlines():
        if re.match(r"\s*=====.*page \d+ =====", l):
            lines.append("¶"); continue                  # a page break is a boundary
        lines.append(re.sub(CODE, " ", l))
    stext = re.sub(r"\s+-\s+", "-", " ".join(lines))
    out, pos = [], []
    for i, ch in enumerate(stext):
        c = ch.lower()
        if c.isascii() and c.isalnum():
            out.append(c); pos.append(i)
    T = "".join(out)
    path = os.path.join(REF, "Florida BEST Grade 8 - Source of Truth.md")
    sotn = unicodedata.normalize("NFKC", open(path, encoding="utf-8").read())
    SOTN = {m.group(1): re.sub(r"\*", "", m.group(2)).strip() for m in re.finditer(r"^\*\*(MA\.[\w.]+)\*\* — (.+)$", sotn, re.M)}
    good = 0; report = []
    for k, t in SOTN.items():
        n = "".join(c for c in t.lower() if c.isascii() and c.isalnum())
        starts = [m.start() for m in re.finditer(re.escape(n), T)]
        ok = False; ctx = None
        for j in starts:
            a, b = pos[j], pos[j + len(n) - 1] + 1
            before, after = stext[max(0, a - 70):a], stext[b:b + 60]
            bnd_before = re.search(r"([.?:¶)]|^)\s*$", before) or re.search(r"MA\.\d+\.[A-Z]+\.\d+\s+[A-Z][^.]*\.\s*$", before)
            bnd_after = re.match(r"\s*(\.|¶|Example|Benchmark|Clarification|MA\.|$)", after)
            ctx = (before, after)
            if bnd_before and bnd_after:
                ok = True; break
        if ok: good += 1
        else: report.append((k, t, ctx, len(starts)))
    print(f"Source of Truth: {good} of {len(SOTN)} statements complete and verbatim; {len(report)} checked by eye: {[k for k, *_ in report]}")
    for k, t, ctx, n in report:
        if k not in SEEN: bad("Source of Truth statement not complete/verbatim:", k, t)

# ---------------- Links (hidden): one row per Scope row, the address each of its link cells opens
wl = wb["Links"]; long_ = 0
LCOLS = hdr[5:17]
lrows = list(wl.iter_rows(min_row=2, max_row=len(rows) + 1))
if len(lrows) != len(rows) or [c.value for c in wl[1]][:len(LCOLS) + 1] != ["Date"] + LCOLS: bad("Links tab shape")
for i, (cells, lrow) in enumerate(zip(rows, lrows), 2):
    if D(lrow[0].value) != D(cells[0].value): bad(f"Links r{i} date")
    for j, h in enumerate(LCOLS, 1):
        b = lrow[j].value
        if DRIVE_MODE:                           # read_links has held each address; here: a cell and its address go together
            hit = LIVE.get((ws.title, cells[H[h]].coordinate))
            if (hit["url"] if hit else None) != b: bad(f"Links r{i} {h} mismatch")
            if hit and wbf[ws.title][cells[H[h]].coordinate].value != '=HYPERLINK(Links!$%s$%d,"%s")' % (lrow[j].column_letter, i, hit["text"]): bad(f"Links r{i} {h}: the cell does not open its own row's address")
        else:
            a = cells[H[h]].hyperlink.target if cells[H[h]].hyperlink else None
            if a != b: bad(f"Links r{i} {h} mismatch")
        if b and len(b) > URL_MAX: long_ += 1
if long_: bad(f"{long_} URLs longer than {URL_MAX} characters (HYPERLINK limit)")

# ---------------- IXL tracker
wi = wb["IXL tracker"]; irows = [r for r in wi.iter_rows(min_row=5) if r[0].value is not None]
if len(irows) != len(due): bad("IXL rows", len(irows), len(due))
for k, (r, x) in enumerate(zip(irows, due), 1):
    if r[0].value != k or D(r[1].value) != d(x[0]) or r[2].value != x[1] or r[3].value != x[2] or D(r[6].value) != d(x[3]) or r[5].value != 67: bad(f"IXL #{k} fields")
    if r[4].value != ", ".join(re.findall(r"\(([A-Z0-9]{3})\)", x[2])): bad(f"IXL #{k} codes", r[4].value)
    if r[9].value != "upcoming" and d(x[0]) > datetime.date.today(): bad(f"IXL #{k} status", r[9].value)
    loc = r[2].hyperlink.location if r[2].hyperlink else None
    m = re.fullmatch(r"'Scope & Sequence'!D(\d+)", loc or "")
    if not m or D(ws.cell(row=int(m[1]), column=1).value) != d(x[0]) or not x[1].startswith(ws.cell(row=int(m[1]), column=4).value): bad(f"IXL #{k} internal link", loc)
print(f"IXL tracker: {len(irows)} assignments")

# ---------------- Unit tests
wt = wb["Unit tests"]
from lib import unitbuild
exam_dates = collections.defaultdict(list)
for c in cal:
    if re.fullmatch(r"[\d/]+\.X\d", c[3]): exam_dates[c[3].split(".X")[0]].append(d(c[0]))
cal_rows = {r[0].value: r for r in wt.iter_rows(min_row=4, max_row=25) if isinstance(r[0].value, str) and r[0].value.startswith("Unit ")}
for k, ds in exam_dates.items():
    r = cal_rows.get(f"Unit {k}")
    if not r or [D(r[1].value), D(r[2].value)] != ds: bad("test dates", k, ds)
units = {}
for f in glob.glob(f"{ROOT}/a7/build/u*/unit.py"):
    s = importlib.util.spec_from_file_location("m", f); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    U = [v for v in vars(m).values() if isinstance(v, dict) and "assessment" in v][0]; units[U["unit"]] = U
for u, U in sorted(units.items()):
    if cal_rows[f"Unit {u}"][3].value != U["assessment"]["total"]: bad(f"Unit {u} points", cal_rows[f'Unit {u}'][3].value)
    # the item table under the Unit u heading
    start = next(r[0].row for r in wt.iter_rows() if r[0].value == f"Unit {u} test — question map")
    items = []
    for r in wt.iter_rows(min_row=start + 3):
        if not isinstance(r[0].value, int): break
        items.append(r)
    n = 0; exp = []
    for sec in U["assessment"]["sections"]:
        for it in sec["items"]:
            if it.get("heading"): continue
            n += 1; pts = len(it["parts"]) if it.get("parts") else 1
            exp.append((n, pts, sec["benchmark"], bool(it.get("transfer")), "Multiple choice" if it.get("choices") else ("Parts" if it.get("parts") else "Written")))
    got = [(r[0].value, r[2].value, r[4].value, r[6].value == "yes", r[5].value) for r in items]
    if got != exp: bad(f"Unit {u} item map differs")
    summ = {wt.cell(row=start + 2 + k, column=9).value: wt.cell(row=start + 2 + k, column=10).value for k in range(1, 6)}
    for bm, pts in U["assessment"]["tracker"].items():
        if summ.get(bm) != pts: bad(f"Unit {u} {bm} points", summ.get(bm), pts)
    print(f"Unit {u} test: {len(items)} questions, {sum(x[1] for x in exp)} points; by benchmark {U['assessment']['tracker']} matches the sheet")

# ---------------- Standards
wsd = wb["Standards"]; srows = list(wsd.iter_rows(min_row=2))
codes_seen = [r[0].value for r in srows]
if len(set(codes_seen)) != len(codes_seen): bad("duplicate standards rows")
if set(SOT) - set(codes_seen): bad("SoT benchmark missing from Standards", set(SOT) - set(codes_seen))
test_pts = {bm: p for U in units.values() for bm, p in U["assessment"]["tracker"].items()}
for r in srows:
    code = r[0].value
    if code in SOT and r[2].value != SOT[code]: bad("Standards wording", code)
    want_pts = test_pts.get(code, "")
    if (r[9].value if r[9].value is not None else "") != want_pts: bad("Standards points", code, r[9].value, want_pts)
    short = code[3:]
    days = [c for c in cal if not c[3].startswith("PM") and short in [b.strip() for b in c[5].split("·")]]
    if days:
        if D(r[6].value) != min(d(c[0]) for c in days) or D(r[7].value) != max(d(c[0]) for c in days): bad("Standards first/last", code)
        for c in days:
            if f"{c[3]} (" not in (r[5].value or ""): bad("Standards taught-on misses", code, c[3])
print(f"Standards: {len(srows)} benchmarks")

# ---------------- Month calendar: every class day once, in its weekday column; holidays marked
wm = wb["Month calendar"]; seen = collections.Counter(); month = None
for row in wm.iter_rows():
    a = row[0].value
    if isinstance(a, str) and re.fullmatch(r"[A-Z][a-z]+ \d{4}", a):
        month = datetime.datetime.strptime(a, "%B %Y").date(); continue
    for j, cell in enumerate(row[:5]):
        if not isinstance(cell.value, str) or not re.match(r"^\d+", cell.value): continue
        dn = int(re.match(r"^(\d+)", cell.value)[1]); day = month.replace(day=dn)
        if day.weekday() != j: bad("calendar weekday", day, j)
        body = cell.value.split("\n", 1)[1] if "\n" in cell.value else ""
        seen[day] += 1
        c = next((x for x in cal if d(x[0]) == day), None)
        if c:
            if f"   {c[3]}\n" not in cell.value + "\n" and not cell.value.startswith(f"{dn}   {c[3]}"): bad("calendar code", day, cell.value[:30])
        elif day in SC.hol:
            if body != "No school": bad("holiday not marked", day, body)
        elif day >= datetime.date(2027, 5, 3) and day in SC.days:
            if body != "PM3 window": bad("PM3 day", day, body)
        elif day > SC.end:
            bad("labelled a day after school ends", day)
        elif day < SC.start:
            if body != "Units 1–2": bad("pre-plan day", day)
        else:
            bad("calendar day with no source", day, cell.value)
for c in cal:
    if seen[d(c[0])] != 1: bad("class day not once in the grid", c[0], seen[d(c[0])])
wkdays = [SC.start + datetime.timedelta(k) for k in range((SC.end - SC.start).days + 1)]
for day in wkdays:
    if day.weekday() < 5 and seen[day] != 1: bad("weekday missing from grid", day)
print(f"month calendar: {sum(seen.values())} weekday cells")

# ---------------- Vocabulary
wv = wb["Vocabulary"]; vrows = [r for r in wv.iter_rows(min_row=2) if r[3].value]
exp = [(t, tex2text.text(df)) for code in sorted(specs, key=lambda c: min(d(x[0]) for x in cal if stem(x[3], int(x[2]) if x[2] else 0) == c)) for t, df in specs[code]["vocab"]]
if [(r[3].value, r[4].value) for r in vrows] != exp: bad("vocabulary differs")
print(f"vocabulary: {len(vrows)} terms")

# ---------------- Units
wu = wb["Units"]; counts = collections.Counter(int(c[2]) for c in cal if c[2])
for r in wu.iter_rows(min_row=2, max_row=18):
    u = r[0].value
    if counts.get(u) and r[4].value != counts[u]: bad("Units periods", u, r[4].value, counts[u])
    for x in r[6:]:
        if x.hyperlink: every_link(x, f"Units {x.coordinate}")
    base_u = next(("/".join(t.split("/")[:3]) for t in tracked if t.startswith(f"a7/packages/A7 Unit {u} - ")), None)
    if base_u:                                             # the two folder columns open this unit's folders
        if r[6].hyperlink: folder_ok(r[6], base_u, f"Units {r[6].coordinate}")
        else: bad(f"Units, Unit {u}: no package folder link")
        deck = f"{base_u}/All Slides" if any(t.startswith(f"{base_u}/All Slides/") for t in tracked) else f"{base_u}/Lessons"
        if r[13].hyperlink: folder_ok(r[13], deck, f"Units {r[13].coordinate}")
        else: bad(f"Units, Unit {u}: no slides folder link")
DECK = {2: " - Slides.pdf", 3: " - Teacher Edition.pdf", 4: " - Question Bank.pdf", 5: " - Additional Question Bank.pdf",
        6: " - Question Bank - Key.pdf", 7: " - Additional Question Bank - Key.pdf"}
if [c.value for c in wb["Units 1–2 decks"][1]] != ["Unit", "Lesson", "Slides (PDF)", "Teacher Edition", "Question Bank", "Question Bank – Additional", "Bank key", "Additional key"]: bad("Units 1–2 decks header")
ndeck = nfolder = 0
lessons12 = sorted({(int(m[1]), m[2]) for t in tracked for m in [re.match(r"a7/packages/A7 Unit ([12]) - [^/]+/Lessons/([^/]+)/", t)] if m})
drows = [r for r in wb["Units 1–2 decks"].iter_rows(min_row=2) if r[0].value is not None]
if [(r[0].value, r[1].value) for r in drows] != lessons12: bad("Units 1–2 decks: the rows are not the lesson folders of Units 1 and 2")
for r in drows:
    for j, x in enumerate(r):
        if j < 2: continue
        where = f"Units 1–2 decks {x.coordinate}"
        sub = "/Keys" if j >= 6 else ""
        have = [t for t in tracked if re.match(rf"a7/packages/A7 Unit {r[0].value} - [^/]+/Lessons/{re.escape(r[1].value)}{sub}/A7 {re.escape(r[1].value)} [^/]*$", t)
                and t.endswith(DECK[j]) and t.rsplit("/", 1)[-1].count(" - ") == DECK[j].count(" - ")]
        if not x.hyperlink:
            if have: bad(where, "links nothing though the package holds", have[0])
            continue
        kind, path = every_link(x, where)
        if kind is None: continue
        if kind == "tree":
            if x.value != "in folder": bad(f"{where}: opens a folder but reads", x.value)
            path = meant(path, f"A7 {r[1].value} ", DECK[j], where); nfolder += 1
            if path is None: continue
        ndeck += 1
        if [path] != have: bad(f"{where} ->", path)
print(f"Units 1–2 decks: {len(drows)} lessons, {ndeck} document links checked by number and kind; {nfolder} open the lesson's folder (the file's own link would be over {URL_MAX})")
for r in wb["Unit tests"].iter_rows():
    for x in r:
        if x.hyperlink and x.hyperlink.target: every_link(x, f"Unit tests {x.coordinate}")

# ---------------- whole workbook: no LaTeX left, one font, no error strings
about = "\n".join(str(r[0].value or "") for r in wb["About"].iter_rows())
for s in wbf:
    for row in s.iter_rows():
        for x in row:
            y = wb[s.title][x.coordinate]                      # the same cell with the link read_links gave it
            if y.hyperlink and y.hyperlink.target: every_link(y, f"{s.title} {x.coordinate}")   # every link in the file, on any tab
            vals = [x.value] if isinstance(x.value, str) and not x.value.startswith("=") else []
            if x.comment: vals.append(x.comment.text)
            for t in vals:
                if re.search(r"\$|\\[a-z]+|\{|\}", t): bad("LaTeX left in", s.title, x.coordinate, t[:60])
            if x.value is not None and x.font.name != "Arial": bad("font", s.title, x.coordinate, x.font.name)
for s in wb:
    for row in s.iter_rows():
        for x in row:
            if isinstance(x.value, str) and re.fullmatch(r"#(REF!|VALUE!|NAME\?|N/A|DIV/0!|NUM!)", x.value): bad("error value", s.title, x.coordinate)
if DRIVE_MODE:
    kinds = collections.Counter("search" if v["kind"] == "search" else ("direct" if v["direct"] else "lookup") for v in LIVE.values())
    print(f"links: Google Drive, live — {kinds['direct'] + kinds['lookup']} looked up in the Drive tab ({len(DTAB)} lines there: {kinds['direct']} open the document itself, {kinds['lookup']} fall back to a search for its exact name), {kinds['search']} lesson searches")
    for want in ("they are live", "My versions", "Everything for this lesson", "is a search for the file's exact name instead"):
        if want not in about: bad("About does not say:", want)
    if [x.title for x in wb][-2:] != ["Links", "Drive"]: bad("the Links and Drive tabs are not last")
else:
    print("links: GitHub")
print("\n".join(P) if P else "no problems"); print(len(P), "problems")
sys.exit(1 if P else 0)
