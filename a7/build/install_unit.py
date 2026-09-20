#!/usr/bin/env python3
"""Install a unit's built outputs into its package folder and write 00 - START HERE.md.
    python3 install_unit.py u3/manifest.py
Run after every lesson and the unit documents have been built and checks.py reports 0 findings.
The package folder is deleted and rebuilt from out/<unit>/ every time — never edit it by hand.
"""
import os, re, shutil, sys, json, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.tekit import plan_from_sidecar

_spec = importlib.util.spec_from_file_location("manifest", sys.argv[1])
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
M = _m.M
HERE = os.path.dirname(os.path.abspath(__file__))
UNITDIR = os.path.basename(os.path.dirname(os.path.abspath(sys.argv[1])))
OUT = os.path.join(HERE, "out", UNITDIR)
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PKG = os.path.join(REPO, "a7", "packages", M["folder"])
REF = os.path.join(REPO, "a7", "reference")
LESSONS = M["lessons"]
U = M["unit"]


FOLDERS = ["Question Banks", "Independent Sets", "Slides", "Handouts", "Assessments", "Answer Keys", "Teacher Editions", "Lesson Plans", "Reference"]


def dest_folder(name):
    if name.endswith(".pptx") or (name.endswith(".pdf") and "Slides" in name):
        return "Slides"
    if " Key." in name:
        return "Answer Keys"
    if "Teacher Edition" in name:
        return "Teacher Editions"
    if "Lesson Plan" in name:
        return "Lesson Plans"
    if "Independent Set" in name:
        return "Independent Sets"
    if "Reference Sheet" in name:
        return "Handouts"
    if "Unit Review" in name or "Unit Assessment" in name:
        return "Assessments"
    if "Question Bank" in name:
        return "Question Banks"
    return None


def install():
    if os.path.exists(PKG):
        shutil.rmtree(PKG)
    for f in FOLDERS:
        os.makedirs(os.path.join(PKG, f), exist_ok=True)
        if f != "Reference":
            os.makedirs(os.path.join(PKG, "PDFs", f), exist_ok=True)
    n = 0
    for name in sorted(os.listdir(OUT)):
        if name.endswith(".json"):
            continue
        folder = dest_folder(name)
        if folder is None:
            raise SystemExit(f"unplaced file: {name}")
        if name.endswith(".pdf"):
            shutil.copy2(os.path.join(OUT, name), os.path.join(PKG, "PDFs", folder, name))
        else:
            shutil.copy2(os.path.join(OUT, name), os.path.join(PKG, folder, name))
        n += 1
    # reference material (not handouts)
    bank = os.path.join(REPO, "a7", f"unit{U:02d}", f"BANK - Unit {U}.md")
    for src, dst in [(os.path.join(REPO, M["audit_src"]), f"UNIT {U} AUDIT - Math Nation package.md"),
                     (bank, f"BANK - Unit {U}.md"),
                     (os.path.join(REF, "A7 SCOPE AND SEQUENCE 2026-27.md"), "A7 SCOPE AND SEQUENCE 2026-27.md"),
                     (os.path.join(REF, "A7 IXL DUE DATES 2026-27.md"), "A7 IXL DUE DATES 2026-27.md"),
                     (os.path.join(REF, "Florida BEST Grade 8 - Source of Truth.md"), "Florida BEST Grade 8 - Source of Truth.md")]:
        shutil.copy2(src, os.path.join(PKG, "Reference", dst))
    return n


def timing_rows():
    rows = []
    for code, label, title, bm, line in LESSONS:
        side = os.path.join(OUT, f"A7 {code}  Slides.notes.json")
        plan, wb, _, blocks = plan_from_sidecar(side)
        fixed = sum(m for seg, rng, m in plan if seg not in ("Whiteboards", "IXL"))
        ixl = sum(m for seg, rng, m in plan if seg == "IXL")
        rows.append((label, fixed, wb, ixl, fixed + wb + ixl))
    return rows


def start_here(n_files):
    t = timing_rows()
    lines = []
    A = lines.append
    A(f"# A7 Unit {U} — {M['title']}")
    A("")
    A(f"Windy Hill Middle School · course 1205050 · {M['summary']}.")
    A("")
    A(f"Nothing exists until it is committed. This folder is generated from `a7/build/{UNITDIR}/` by `install_unit.py`; edit the specs and rebuild rather than editing these files by hand.")
    A("")
    A("---")
    A("")
    A("## How the files are named")
    A("")
    A(f"**`A7 <unit>.<lesson>  <what it is>`** — two spaces before the type, two-digit lesson numbers. `A7 {U}.04  Question Bank` is Accelerated grade 7, Unit {U}, Lesson 4, the question bank. {M.get('naming_note', '')} Unit-wide documents drop the lesson number: `A7 {U}  Unit Review`, `A7 {U}  Unit Assessment`, `A7 {U}  Reference Sheet`.")
    A("")
    A("---")
    A("")
    A("## Where everything lives")
    A("")
    A("| Folder | What is in it |")
    A("|---|---|")
    A("| **Question Banks** | Per lesson: the Question Bank and the Question Bank – Additional. Retired worksheets are question banks (ruling 11): draw from them for practice, exit tickets or re-teaching; nothing in here has an answer on it. |")
    A("| **Slides** | The decks, as `.pptx`. No speaker notes — the notes live in the Teacher Edition (ruling 12). |")
    A("| **Handouts** | The Reference Sheet. Students study from it; it may NOT be used on the assessment (ruling 13). There is no study guide (ruling 11). |")
    A("| **Assessments** | Unit Review (unscored) and Unit Assessment (two periods) — student copies. |")
    A("| **Answer Keys** | Every key in the unit, without exception. |")
    A("| **Teacher Editions** | One per lesson, **four pages, read in twenty minutes** (ruling 26). Page 1 is the period — benchmark with its Must and Must-not lines, the target, the MTRs, the timing table and the three sentences to say out loud. Then one line per slide, each board carrying its answer, its named distractors and the split-board move. Misconceptions to Watch at the end. |")
    A("| **PDFs** | A mirror of the six folders above, same filenames. This is what gets printed and posted. |")
    A("| **Lesson Plans** | One Florida-format plan per lesson (ruling 25): standards, the MTRs with their evidence, the sequence read from the deck, gradual release, higher-order questions with DOK, checks for understanding with the response to each, differentiation. |")
    A("| **Reference** | Not handouts: `BANK - Unit N.md` (how each question bank varies, what the audit found, what changed from the book, and every bank answer — ruling 26 moved this out of the teacher's edition), the Math Nation package audit, the scope and sequence, the IXL due-date sheet, the Grade 8 source of truth. |")
    A("")
    A("**Nothing with an answer printed on it sits outside `Answer Keys`.**")
    A("")
    A("---")
    A("")
    A("## Unit at a glance")
    A("")
    A("| Day | Lesson | Benchmark | The line that carries the day |")
    A("|---|---|---|---|")
    for code, label, title, bm, line in LESSONS:
        A(f"| {label} | {title} | {bm} | {line} |")
    n_bm = len({l[3] for l in M["lessons"]})
    A(f"| — | Unit Review | all {('two', 'three', 'four', 'five', 'six')[n_bm - 2] if 2 <= n_bm <= 6 else n_bm} | unscored; the SSDD block is named on the key only |")
    _bms, _pts = M["assessment"]
    A(f"| — | Unit Assessment — two periods, one paper | {_bms} | {_pts} points |")
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
    A(f"Installed: {n_files} files from the build, plus this page and the Reference folder.")
    A("")
    with open(os.path.join(PKG, "00 - START HERE.md"), "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    n = install()
    start_here(n)
    print(f"installed {n} files into {PKG}")
