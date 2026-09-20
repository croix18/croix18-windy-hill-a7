#!/usr/bin/env python3
"""Install the built Unit 3 outputs into the package folder and write 00 - START HERE.md.
python3 install_unit3.py   (run after every lesson and the unit documents have been built and checked)
"""
import os, re, shutil, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.tekit import plan_from_sidecar

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "u3")
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PKG = os.path.join(REPO, "a7", "packages", "A7 Unit 3 - Exponents and Scientific Notation")
REF = os.path.join(REPO, "a7", "reference")

LESSONS = [  # code, label, title, benchmark, the line that carries the day
    ("3.01", "3.01", "Product Laws of Exponents", "MA.7.NSO.1.1", "Same base, add — and the base has to match."),
    ("3.02", "3.02", "Quotient Laws of Exponents", "MA.7.NSO.1.1", "Same base, subtract — and exponent 0 is not 0."),
    ("3.03", "3.03", "Exponential Expressions", "MA.7.NSO.1.1", "Two plans, one value — the order is yours."),
    ("3.04", "3.04", "Negative Exponent Law", "MA.8.NSO.1.3", "Reciprocal, not opposite."),
    ("3.05", "3.05", "Applying Exponent Laws", "MA.8.NSO.1.3", "Flip the numbers, not the sign."),
    ("3.06", "3.06–07", "Evaluating and Equivalent Expressions", "MA.8.NSO.1.3", "Rewrite the base to compare."),
    ("3.T1", "T-A1", "Exponent Laws with Variable Bases", "MA.8.AR.1.1", "Everything inside the parentheses gets the exponent — the number included."),
    ("3.T2", "T-A2", "Negative Exponents with Variable Bases", "MA.8.AR.1.1", "Only the factor wearing the negative exponent moves."),
    ("3.08", "3.08", "Writing Large Numbers in Scientific Notation", "MA.8.NSO.1.4", "One nonzero digit in front of the decimal point."),
    ("3.09", "3.09", "Writing Small Numbers in Scientific Notation", "MA.8.NSO.1.4", "The exponent counts places, not zeros."),
]

FOLDERS = ["Question Banks", "Slides", "Handouts", "Assessments", "Answer Keys", "Teacher Editions", "Reference"]


def dest_folder(name):
    if name.endswith(".pptx") or (name.endswith(".pdf") and "Slides" in name):
        return "Slides"
    if " Key." in name:
        return "Answer Keys"
    if "Teacher Edition" in name:
        return "Teacher Editions"
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
    for src, dst in [(os.path.join(REPO, "a7", "unit03", "UNIT 3 AUDIT.md"), "UNIT 3 AUDIT - Math Nation package.md"),
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
    A("# A7 Unit 3 — Exponents and Scientific Notation")
    A("")
    A("Windy Hill Middle School · course 1205050 · ten teaching days (nine book lessons, merged to eight, plus the two Thread A days), a review, a two-period assessment.")
    A("")
    A("Nothing exists until it is committed. This folder is generated from `a7/build/u3/` by `install_unit3.py`; edit the specs and rebuild rather than editing these files by hand.")
    A("")
    A("---")
    A("")
    A("## How the files are named")
    A("")
    A("**`A7 <unit>.<lesson>  <what it is>`** — two spaces before the type, two-digit lesson numbers. `A7 3.04  Question Bank` is Accelerated grade 7, Unit 3, Lesson 4, the question bank. The two Thread A days are `A7 3.T1` and `A7 3.T2` (they are MA.8.AR.1.1, woven into this unit under ruling 14, and carry no book lesson number). Unit-wide documents drop the lesson number: `A7 3  Unit Review`, `A7 3  Unit Assessment`, `A7 3  Reference Sheet`.")
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
    A("| **Teacher Editions** | One per lesson: Read This First, the timing table read from the deck, slide-by-slide notes, the whiteboard round with the named wrong answers, what changed from Math Nation. |")
    A("| **PDFs** | A mirror of the six folders above, same filenames. This is what gets printed and posted. |")
    A("| **Reference** | Not handouts: the Math Nation package audit, the scope and sequence, the IXL due-date sheet, the Grade 8 source of truth. |")
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
    A("| — | Unit Review | all four | unscored; the SSDD block is named on the key only |")
    A("| — | Unit Assessment, day 1 | MA.7.NSO.1.1, MA.8.NSO.1.3 | 19 points |")
    A("| — | Unit Assessment, day 2 | MA.8.AR.1.1, MA.8.NSO.1.4 | 20 points |")
    A("")
    A("Book order with Thread A woven in after 3.07 (ruling 14): the laws are complete on numbers before they are restated on letters, and both are complete before scientific notation. Math Nation's 3.6 and 3.7 are one period here (3.06–07). MA.7.NSO.1.1 is grade 7 content the Grade 8 FAST assumes; the other three benchmarks report under Number Sense and Operations (8.NSO.1.3, 8.NSO.1.4) and Algebraic Reasoning (8.AR.1.1).")
    A("")
    A("---")
    A("")
    A("## How a period runs (rulings 10–12)")
    A("")
    A("Title and learning target (1 min) → warm-up, four spaced-retrieval questions (5) → notes (10–11) → two worked examples with a Your Turn each (10) → **nine whiteboard questions**, question 9 written (the remainder) → IXL, the last five minutes. Every wrong option on every multiple-choice item is a named error with its benchmark cited, in the Teacher Edition and on the keys (§16 rule 4).")
    A("")
    A("## Timing")
    A("")
    A("<!-- timing table: generated by install_unit3.py from the deck side-cars. Do not edit by hand. -->")
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
    A("- **One point per lettered part, no partial credit.** The assessment key carries a `Scoring:` line under every question and a per-benchmark Score Tracker at the end.")
    A("- **No benchmark codes on student pages.** The deck title slide and the keys and Teacher Editions carry them.")
    A("- **Opens cleanly in Google Docs.** Every document is a fixed-width table layout with no nested tables and a spacer after every block; fonts are Times New Roman / Georgia / Arial with FreeSerif for the bubbles only.")
    A("- **Every answer is re-derived by machine at build time.** Every item carries a `check` that sympy evaluates (variable bases as symbols); every multiple-choice distractor must name its error; every scientific-notation coefficient is scanned for the [1, 10) rule; the build refuses on any finding. The post-build suite (`checks.py`) then reads the rendered PDFs for off-page text, glyph coverage, Google-Docs layout rules and the timing plan.")
    A("- **Math Nation's copyrighted pages are not in this repository.** The audit in `Reference/` records what was checked and what was found; the items here are a mix of the book's (verified) and original ones, aligned to the benchmark text and the B1G-M first.")
    A("")
    A("---")
    A("")
    A("## Before the unit starts")
    A("")
    A("- **Seven defects in the Math Nation package are not reproduced here.** Practice L1 #7 (key 104,796 → 104,976), Additional Practice L8 #2 (10⁶ + 10⁴ keyed 101000 → 1,010,000), Additional Practice L9 #3 (malformed item, wrong key), Homework L3 #7 (4,046 → 4,096), Homework L9 #4b (3 → 1,000), Homework L9 #4c (item unsound; keyed 3,000, true ratio ≈ 527), Homework L9 #5 (two matching rows equal). `Reference/UNIT 3 AUDIT - Math Nation package.md` has the page numbers.")
    A("- **Three things the state guide expects that the book never asks are in every relevant bank and on the assessment:** unknown-exponent items (7ⁿ ÷ 7² = 343), the −b versus b⁻¹ contrast in writing, and calculator E notation with comparisons that cross from very large to very small.")
    A("- **The assessment is two periods, 39 points, one question map.** Day 1 is numerical (sections 1–2, 19 points); day 2 is variable bases and scientific notation (sections 3–4, 20 points). Numbering runs straight through; the key's Score Tracker maps every question to its benchmark.")
    A("- **The Reference Sheet is the only handout.** Give it out at 3.04 or earlier; it is the document students study from. It does not go into the test.")
    A("")
    A(f"Installed: {n_files} files from the build, plus this page and the Reference folder.")
    A("")
    with open(os.path.join(PKG, "00 - START HERE.md"), "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    n = install()
    start_here(n)
    print(f"installed {n} files into {PKG}")
