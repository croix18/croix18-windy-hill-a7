#!/usr/bin/env python3
"""Install a built unit into its package folder, write 00 - START HERE.md, and zip it for delivery.
    python3 install_unit.py u3            (build_all.py u3 --install ends here)

Run after build_all.py reports `checks: 0 findings`. The package folder is deleted and rebuilt from
out/<unit>/ every time — never edit it by hand. The layout, the copying (each file compared byte
for byte with the build) and the zips are the shared kit's (lib/packkit.py — one layout for both
courses, by lesson: Croix, 4 October 2026); this file is A7's own: where the packages live, which
reference documents travel with a unit, and what START HERE says.

    a7/packages/A7 Unit 3 - Exponents and Scientific Notation/
        00 - START HERE.md
        All Slides/                    A7 Unit 3 … - All Slides.pptx and its PDF (no HTML: ruling 41)
        Lessons/3.08/                  A7 3.08 Writing Large Numbers in Scientific Notation - Slides,
                                       Teacher Edition, Lesson Plan, Independent Set,
                                       Question Bank, Additional Question Bank (docx/pptx and pdf)
        Lessons/…/Keys/                that lesson's three answer keys — never beside a student page
        Review/    Assessment/    Handouts/    Reference/
    a7/packages/zips/   (git-ignored)  A7 Unit 3 - Complete.zip (and in parts when over the upload
                                       limit), one per lesson, A7 Unit 3 - Lessons.zip,
                                       A7 Unit 3 - Review and Assessment.zip
"""
import os, re, sys, glob, shutil, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib.profile import C
from lib import names, packkit
import bank_file

UNITDIR = os.path.basename(sys.argv[1].rstrip("/")) if len(sys.argv) > 1 else ""
if UNITDIR.endswith(".py"):                      # the older call, install_unit.py u3/manifest.py
    UNITDIR = os.path.basename(os.path.dirname(os.path.abspath(sys.argv[1])))
if not re.fullmatch(r"u\d+", UNITDIR):
    raise SystemExit("usage: python3 install_unit.py u3")
U = int(UNITDIR[1:])
OUT = os.path.join(HERE, "out", UNITDIR)
A7 = os.path.dirname(HERE)                               # the a7/ folder
REPO = os.path.dirname(A7)
REF = os.path.join(A7, "reference")
PACKAGES = os.path.join(A7, "packages")
ZIPS = os.path.join(PACKAGES, "zips")
TITLE = names.unit_title(U)
PKG = os.path.join(PACKAGES, packkit.package_folder(U))


def load(path, name):
    sp = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m


M = load(os.path.join(HERE, UNITDIR, "manifest.py"), "manifest").M
if M["unit"] != U:
    raise SystemExit(f"{UNITDIR}/manifest.py says unit {M['unit']}")
LESSONS = M["lessons"]                                   # (code, label, title, benchmark, the day's line), teaching order
_by_code = {m.L["code"]: m.L for m in (load(f, "l") for f in sorted(glob.glob(os.path.join(HERE, UNITDIR, "l[0-9][0-9].py"))))}
if set(_by_code) != {row[0] for row in LESSONS}:
    raise SystemExit(f"lesson specs and manifest disagree about {sorted(set(_by_code) ^ {row[0] for row in LESSONS})}")
SPECS = [_by_code[row[0]] for row in LESSONS]

def reference_files():
    """[(source path, name in the package's Reference/)]."""
    ustem = names.unit_stem(U)
    out = [(bank_file.write(UNITDIR), None),
           (os.path.join(REF, f"{ustem} - Audit.md"), None),
           (os.path.join(REF, "A7 Scope and Sequence 2026-27.md"), None),
           (os.path.join(REF, "A7 IXL Due Dates 2026-27.md"), None),
           (os.path.join(REF, "Florida BEST Grade 8 - Source of Truth.md"), None)]
    return [(src, dst or os.path.basename(src)) for src, dst in out]


def install():
    placed = packkit.install(OUT, PKG, SPECS)
    os.makedirs(os.path.join(PKG, "Reference"), exist_ok=True)
    for src, name in reference_files():
        if not os.path.exists(src):
            raise SystemExit(f"reference document missing: {src}")
        shutil.copy2(src, os.path.join(PKG, "Reference", name))
    return placed


def timing_rows():
    label = {row[0]: row[1] for row in LESSONS}
    return [(label[code], other, wb, ixl, tot) for code, other, wb, ixl, tot in packkit.timing_rows(SPECS, OUT)]


def start_here(placed):
    t = timing_rows()
    dates, review_day, exam_days, plan_as_of = packkit.calendar(U, HERE)
    day = packkit.day
    unit_deck = names.unit(U, "All Slides", "pptx")
    example = SPECS[min(3, len(SPECS) - 1)]
    lines = []
    A = lines.append
    A(f"# A7 Unit {U} — {TITLE}")
    A("")
    A(f"Windy Hill Middle School · course {C.COURSE_CODE} · {M['summary']}.")
    A("")
    if dates:
        first, last = min(dates.values()), max(dates.values())
        when = f"lessons {day(first)} – {day(last)}"
        if exam_days:
            when += f", the assessment {day(exam_days[0])}" + (f" and {day(exam_days[-1])}" if len(exam_days) > 1 else "")
        A(f"**By the plan** (Windmill's spine as of {plan_as_of}; `tools/scope_calendar.py` is its source): {when}, "
          f"{first.year if first.year == last.year else str(first.year) + '–' + str(last.year)}. "
          "The dates move when the as-run log does (the plan follows the class), and a day is logged from the phone view of the plan.")
        A("")
    A(f"Nothing exists until it is committed. This folder is generated from `a7/build/{UNITDIR}/` by `install_unit.py`; edit the specs and rebuild rather than editing these files by hand.")
    A("")
    A("---")
    A("")
    A("## How the files are named")
    A("")
    A(f"**Course, number, title, then what it is** — `{names.lesson(example, 'Slides', 'pptx')}`, "
      f"`{names.lesson(example, 'Question Bank', 'docx')}`, `{names.lesson(example, 'Question Bank', 'docx', key=True)}`. "
      f"Unit-wide files carry the unit instead of a lesson: `{unit_deck}`, `{names.unit(U, 'Test', 'docx')}`, "
      f"`{names.unit(U, 'Test', 'docx', key=True)}`, `{names.unit(U, 'Review', 'docx')}`, `{names.unit(U, 'Reference Sheet', 'docx')}`. "
      "Single spaces, pieces joined by ` - `, two-digit lesson numbers so everything sorts in teaching order. "
      f"The same pattern in both courses (Croix, 4 October 2026). {M.get('naming_note', '')}")
    A("")
    A("---")
    A("")
    A("## Where everything lives")
    A("")
    A("| Folder | What is in it |")
    A("|---|---|")
    A(f"| **All Slides** | `{unit_deck}` — the whole unit in one PowerPoint, in teaching order; each lesson keeps its own "
      "slide numbers, so the Teacher Edition lines up. **A deck is its Slides file** (ruling 41, 5 October 2026): there is "
      "no HTML deck and no console. **To teach from one in Deckhand**: upload the lesson's `Slides.pptx` (or this file) to "
      "Google Drive, open it — it opens as Google Slides — and paste that link into Deckhand's Slides card; the pen and "
      "the timers are Deckhand's. The slides are set in Lexend, which Google Slides has, so they arrive as built. A board "
      "is two slides: the question, then the same question with its steps and its answer. |")
    A("| **Lessons** | **One folder per lesson, named by its number (`3.08`; the title is in every file's name), everything for that day in it**, each document with its PDF beside it (the PDF is what gets printed and posted). *Slides* — the lesson's own deck, a `.pptx` (upload it to Drive and it opens as Google Slides; paste that link into Deckhand's Slides card). *Teacher Edition* — three or four pages, read in twenty minutes (ruling 26): page 1 is the period (benchmark with its Must and Must-not lines, the target, the MTRs, the timing table, the three sentences to say out loud), then one line per slide, each board carrying its answer, its named distractors and the split-board move, and Misconceptions to Watch at the end. *Lesson Plan* — the Florida-format plan (ruling 25): standards, the MTRs with their evidence, the sequence read from the deck, gradual release, higher-order questions with DOK, checks for understanding with the response to each, differentiation. *Independent Set* — the six questions written in silence (ruling 21). *Question Bank* and *Additional Question Bank* — retired worksheets are question banks (ruling 11): draw from them for practice, exit tickets or re-teaching. |")
    A("| **Lessons / … / Keys** | Inside each lesson's folder: that lesson's three answer keys and nothing else. |")
    A("| **Review** | The Unit Review and its key (unscored; it goes home as practice — ruling 27a, A7 has no review day). |")
    A("| **Assessment** | The unit test (one paper, two periods) and its key. |")
    A("| **Handouts** | The Reference Sheet. Students study from it; it may NOT be used on the assessment (ruling 13). There is no study guide (ruling 11). |")
    A(f"| **Reference** | Not handouts: `{names.unit(U, 'Question Bank', 'md')}` (how each question bank varies, what the audit found, what changed from the book, and every bank answer — ruling 26 moved this out of the teacher's edition), the Math Nation package audit, the scope and sequence, the IXL due-date sheet, the Grade 8 source of truth. |")
    A("")
    A("**Nothing with an answer printed on it sits beside a student page:** a lesson's keys are in its `Keys` folder, and every such file says Key in its name.")
    A("")
    A("---")
    A("")
    A("## Unit at a glance")
    A("")
    A("| Day | Planned | Lesson | Benchmark | The line that carries the day |")
    A("|---|---|---|---|---|")
    for code, label, title, bm, line in LESSONS:
        k = code if code in dates else _by_code[code].get("plan_code")      # a thread day is T-A1 in the plan
        when = day(dates[k]) if k in dates else "—"
        A(f"| {label} | {when} | {title} | {bm} | {line} |")
    n_bm = len({l[3] for l in M["lessons"]})
    A(f"| — | — | Unit Review | all {('two', 'three', 'four', 'five', 'six')[n_bm - 2] if 2 <= n_bm <= 6 else n_bm} | unscored, sent home as practice (ruling 27a); the SSDD block is named on the key only |")
    _bms, _pts = M["assessment"]
    A(f"| — | {' and '.join(packkit.day(d) for d in exam_days) if exam_days else '—'} | Unit Assessment — two periods, one paper | {_bms} | {_pts} points |")
    A("")
    A(M["order_note"])
    A("")
    A("---")
    A("")
    A("## How a period runs (rulings 10–12)")
    A("")
    A("Title and learning target (1 min) → warm-up, four spaced-retrieval questions (5) → notes (10–11) → two worked examples with a Your Turn each (10) → **nine whiteboard questions**, question 9 written (the remainder, 10\u201320) \u2192 the **independent set**, six questions written in silence (6, ruling 21) \u2192 IXL, the last five minutes. Every wrong option on every multiple-choice item is a named error with its benchmark cited, in the Teacher Edition and on the keys (§16 rule 4).")
    A("")
    A("## Timing")
    A("")
    A("<!-- timing table: generated by install_unit.py from the deck side-cars. Do not edit by hand. -->")
    A("")
    A("| Lesson | Teaching (title, warm-up, notes, examples) | Whiteboard round | IXL | Total |")
    A("|---|---|---|---|---|")
    for label, fixed, wb, ixl, tot in t:
        A(f"| {label} | {fixed} min | {wb} min | {ixl} min | {tot} min |")
    wbs = [r[2] for r in t]
    A("")
    A(f"The whiteboard round is the remainder — {min(wbs)}–{max(wbs)} minutes across the unit — and the build refuses any plan whose remainder falls outside 10–20. Every plan totals 53 exactly. There is no shortened variant; short days are absorbed by the person in the room.")
    A("")
    A("<!-- end timing table -->")
    A("")
    A("---")
    A("")
    A("## Standing decisions baked into these files")
    A("")
    A("- **No partner or group work anywhere.** Math Nation's explorations and collaborations are taught from the front; its partner-discussion tasks are written whiteboard questions.")
    A("- **Calculators: allowed on everything, and nothing about them is printed on any student page.** The one exception the house style allows is the Reference Sheet's description of what the FAST platform provides (an on-screen scientific calculator) — that is a description, not a permission line.")
    A("- **Old-school textbook styling.** No commentary panels, no grey bars, no clip art. American spellings.")
    A("- **One point per lettered part, no partial credit**, with follow-through credit (ruling 19): a later part earns its point when the right operation is applied to the student's own earlier value, where that work is on the page. The key carries a `Scoring:` line under every question and a per-benchmark Score Tracker at the end.")
    A("- **The assessment is one paper over two class periods** (ruling 27). Students stop when the period ends and continue from where they stopped; there is no Day 1 / Day 2 paper and no such heading. Two questions are **transfer items** (ruling 18) — same benchmark, a surface that appears on no review and in no question bank — and the key names them.")
    A("- **No benchmark codes on student pages.** The deck title slide and the keys and Teacher Editions carry them.")
    A("- **Opens cleanly in Google Docs.** Every document is a fixed-width table layout with no nested tables and a spacer after every block; fonts are Times New Roman / Georgia / Arial with FreeSerif for the bubbles only.")
    A("- **Every answer is re-derived by machine at build time.** Every item carries a `check` that sympy evaluates (variable bases as symbols); every multiple-choice distractor must name its error; every scientific-notation coefficient is scanned for the [1, 10) rule; the build refuses on any finding. The post-build suite (`checks.py`) then reads the rendered PDFs for off-page text, glyph coverage, Google-Docs layout rules and the timing plan.")
    A("- **Math Nation's copyrighted pages are not in this repository.** The audit in `Reference/` records what was checked and what was found; the items here are a mix of the book's (verified) and original ones, aligned to the benchmark text and the B1G-M first.")
    A("")
    A("---")
    A("")
    A("## Before the unit starts")
    A("")
    for b in M["before_unit"]:
        A("- " + b)
    A("")
    A(f"Installed: {len(placed)} files from the build, plus this page and the Reference folder.")
    A("")
    with open(os.path.join(PKG, "00 - START HERE.md"), "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    if not os.path.isdir(OUT):
        raise SystemExit(f"nothing built in {OUT}")
    placed = install()
    start_here(placed)
    made = packkit.zips(PKG, ZIPS, U)
    print(f"installed {len(placed)} files into {os.path.relpath(PKG, REPO)}; {len(made)} zips in {os.path.relpath(ZIPS, REPO)}")
