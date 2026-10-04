#!/usr/bin/env python3
"""The 4 October 2026 renaming, as a record and as the rule it followed.

Croix: "Can you normalize all of the naming conventions in a7 and m7. I have file names with all
sorts of stuff. It's tough to find what I need sometimes." He chose the title in every name, unit
folders organised by lesson in both courses, and every scope: the current units, the older
packages, the reference documents and everything else.

The current units (built by the kit) took their new names from the build itself (lib/names.py,
lib/packkit.py). This script is for everything the build does not write: it maps each OLD path to
its NEW path by the same rule, moves the file with `git mv` (nothing inside a file changes), and
writes the old-to-new list — for the current units too, so a copy already in Drive under an old
name can be matched to its new one.

    python3 tools/legacy/rename_2026_10_04.py a7|m7 --list      print the plan, change nothing
    python3 tools/legacy/rename_2026_10_04.py a7|m7 --apply     git mv, then write the list
    python3 tools/legacy/rename_2026_10_04.py a7|m7 --relist    write the list again from the commit
                                                               before the renaming (nothing moves)

The same file is kept in both course repositories. It has been run; running it again finds
nothing left to move.
"""
import os, re, sys, csv, subprocess

SEP = " - "
COURSE = sys.argv[1] if len(sys.argv) > 1 else ""
PFX = {"a7": "A7", "m7": "M7"}.get(COURSE) or sys.exit(__doc__)
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

UNITS = {
    "A7": {1: "Equations and Inequalities", 2: "Real Numbers, Square Roots and Cube Roots",
           3: "Exponents and Scientific Notation", 4: "Solving Problems with Rational Numbers"},
    "M7": {2: "Probability", 3: "Operations with Rational Numbers", 4: "Area",
           5: "Scaling With Proportional Relationships"},
}[PFX]

# lesson titles: A7 Units 1-2 from their START HERE pages, M7 Units 2-3 from the decks' own title
# slides; the current units' from their specs (typed here so the list can be written without the build)
TITLES = {
    "A7": {
        "1.01": "Rewriting Numbers", "1.02": "Repeating Decimals to Fractions", "1.03": "Two-Step Equations",
        "1.04": "Two-Step Equations in Context", "1.05": "Solving Problems with Equations",
        "1.06": "Writing Equations from Contexts", "1.07": "Writing and Solving Equations",
        "1.08": "Determining Solutions to Inequalities", "1.09": "Inequalities with the Distributive Property",
        "1.10": "Inequalities in Real-World Contexts",
        "2.01": "Square Values", "2.02": "Square Values and Square Roots", "2.03": "Cube Values",
        "2.04": "Approximating Irrational Numbers", "2.05": "Rational and Irrational Numbers on the Number Line",
        "2.06": "Plotting, Ordering and Comparing Real Numbers",
        "3.01": "Product Laws of Exponents", "3.02": "Quotient Laws of Exponents", "3.03": "Exponential Expressions",
        "3.04": "Negative Exponent Law", "3.05": "Applying Exponent Laws", "3.06": "Evaluating and Equivalent Expressions",
        "3.T1": "Exponent Laws with Variable Bases", "3.T2": "Negative Exponents with Variable Bases",
        "3.08": "Writing Large Numbers in Scientific Notation", "3.09": "Writing Small Numbers in Scientific Notation",
        "4.01": "Adding and Subtracting in Scientific Notation", "4.02": "Multiplying and Dividing in Scientific Notation",
        "4.04": "Real-World Problems and Significant Digits", "4.05": "Evaluating Expressions with Radicals",
        "4.06": "Order of Operations with Radicals", "4.07": "Real-World Order of Operations",
    },
    "M7": {
        "2.01": "Exploring Sample Space", "2.02": "Determining Sample Space", "2.03": "Rewriting Numbers in Equivalent Forms",
        "2.04": "Converting Between Repeating Decimals and Fractions", "2.05": "Probability", "2.06": "Comparing Probabilities",
        "2.07": "Experimental and Theoretical Probability", "2.08": "Small and Large Numbers of Trials",
        "2.09": "Probabilities from Simulations",
        "3.01": "Adding Rational Numbers", "3.02": "Subtracting Rational Numbers", "3.03": "Multiplying Rational Numbers",
        "3.04": "Dividing Rational Numbers", "3.05": "Real-World Problems (Adding and Subtracting)",
        "3.06": "Real-World Problems (Multiplying and Dividing)", "3.07": "Real-World Problems (Three or More Steps)",
        "3.08": "Real-World Problems (Putting It Together)",
        "4.01": "Deriving Area Formulas", "4.02": "Finding the Area of Trapezoids, Parallelograms and Rhombi",
        "4.03": "Finding the Area of Polygons", "4.04": "Finding the Area of Composite Figures",
        "4.05": "Exploring Relationships in Circles", "4.06": "Finding Circumference",
        "4.07": "Finding the Radius and Diameter from the Circumference", "4.08": "Exploring the Area of a Circle",
        "4.09": "Fractional Parts of a Circle", "4.10": "Circumference or Area",
        "5.01": "Random Samples vs. Population", "5.02": "Determining Probability",
        "5.03": "Making Population Predictions (Part 1)", "5.04": "Making Population Predictions (Part 2)",
        "5.05": "Scale Factors (Perimeter)", "5.06": "Scale Factors (Area)", "5.07": "Scale Drawings",
        "5.08": "Dimensions and Perimeters", "5.09": "Dimensions and Areas", "5.10": "Real-World Scale Drawings",
    },
}[PFX]

# what an old name called a thing -> (what it is now, key?, worked answers?)
LESSON_KIND = {
    "Slides": ("Slides", 0), "Teacher Edition": ("Teacher Edition", 0), "Lesson Plan": ("Lesson Plan", 0),
    "Question Bank": ("Question Bank", 0), "Question Bank Key": ("Question Bank", 1),
    "Question Bank - Additional": ("Additional Question Bank", 0), "Question Bank - Additional Key": ("Additional Question Bank", 1),
    # ruling 11: a retired worksheet is a question bank, and its key is that bank's key
    "Worksheet": ("Question Bank", 0), "Worksheet Key": ("Question Bank", 1),
    "Additional Practice Key": ("Additional Question Bank", 1),
    "Independent Set": ("Independent Set", 0), "Independent Set Key": ("Independent Set", 1),
    "Circuit": ("Circuit", 0), "Circuit Key": ("Circuit", 1),
    "Handout": ("Handout", 0), "Handout Key": ("Handout", 1), "Record Sheet": ("Record Sheet", 0),
}
UNIT_KIND = {   # old tail -> (folder, new tail)
    "Unit Slides": ("All Slides", "All Slides"), "All Slides": ("All Slides", "All Slides"),
    "Reference Sheet": ("Handouts", "Reference Sheet"), "Study Guide": ("Handouts", "Study Guide"),
    "Vocabulary Reference": ("Handouts", "Vocabulary Reference"),
    "Unit Review": ("Review", "Review"), "Unit Review Key": ("Review", "Review - Key"),
    "Unit Review  Slides": ("Review Day", "Review Day - Slides"),
    "Unit Review  Teacher Edition": ("Review Day", "Review Day - Teacher Edition"),
    "Unit Review  Lesson Plan": ("Review Day", "Review Day - Lesson Plan"),
    "Unit Assessment": ("Assessment", "Test"), "Unit Assessment Key": ("Assessment", "Test - Key"),
    "Unit Assessment  Worked Answers": ("Assessment", "Test - Worked Answers"),
    "Practice Test": ("Assessment/Practice Test", "Practice Test"), "Practice Test Key": ("Assessment/Practice Test", "Practice Test - Key"),
    "Practice Test  Worked Answers": ("Assessment/Practice Test", "Practice Test - Worked Answers"),
    "Quiz 1": ("Assessment/Quiz 1", "Quiz 1"), "Quiz 1 Key": ("Assessment/Quiz 1", "Quiz 1 - Key"),
}
for _f in "AB":
    UNIT_KIND[f"Unit Assessment  Form {_f}"] = (f"Assessment/Form {_f}", f"Test Form {_f}")
    UNIT_KIND[f"Unit Assessment  Form {_f} Key"] = (f"Assessment/Form {_f}", f"Test Form {_f} - Key")
    UNIT_KIND[f"Unit Assessment  Form {_f}  Worked Answers"] = (f"Assessment/Form {_f}", f"Test Form {_f} - Worked Answers")


def unit_folder(n):
    return f"{PFX} Unit {n} - {UNITS[n]}"


def new_place(old_base):
    """(subfolder inside the unit's folder, new file name, unit number) for a file named the old
    way — "A7 3.01  Question Bank Key.docx", "M7 4  Unit Assessment  Form A.pdf" — or None."""
    stem, ext = os.path.splitext(old_base)
    m = re.match(rf"^{PFX} (\d+)\.(\w\d|\d\d)  (.+)$", stem)
    if m:
        code = f"{m.group(1)}.{m.group(2)}"
        if code not in TITLES or m.group(3) not in LESSON_KIND:
            return None
        kind, key = LESSON_KIND[m.group(3)]
        # the lesson's folder is its number only: the title is in the unit's folder and in the file's
        # name already, and three times over a path does not fit Windows' 260 characters
        folder = f"Lessons/{code}" + ("/Keys" if key else "")
        return folder, f"{PFX} {code} {TITLES[code]}{SEP}{kind}{SEP + 'Key' if key else ''}{ext}", int(m.group(1))
    m = re.match(rf"^{PFX} (\d+)  (.+)$", stem)
    if m and int(m.group(1)) in UNITS and m.group(2) in UNIT_KIND:
        n = int(m.group(1))
        folder, tail = UNIT_KIND[m.group(2)]
        return folder, f"{PFX} Unit {n} {UNITS[n]}{SEP}{tail}{ext}", n
    return None


def git(*a):
    return subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True)


def tracked(prefix):
    """The files under a folder: as they stand now, or (--relist) as they stood before the renaming."""
    if "--relist" in sys.argv:
        out = git("ls-tree", "-r", "--name-only", "-z", OLD_COMMIT, "--", prefix).stdout
    else:
        out = git("ls-files", "-z", "--", prefix).stdout
    return [p for p in out.split("\0") if p]


# ---- the plans ------------------------------------------------------------------------------------
def u(n, what):
    return f"{PFX} Unit {n} {UNITS[n]}{SEP}{what}"


REF = {
    "A7": {
        "A7 IXL DUE DATES 2026-27.md": "A7 IXL Due Dates 2026-27.md",
        "A7 SCOPE AND SEQUENCE 2026-27.md": "A7 Scope and Sequence 2026-27.md",
        "SCOPE AND SEQUENCE 2026-2027.md": "County Scope and Sequence 2026-27.md",
        "MATH NATION A7 BOOK - table of contents and IXL plan.md": "A7 IXL Skill Plan and Book Contents.md",
        "UNIT AUDIT.md": "M7 Unit Audit.md",
        "PAGE BREAKS - for Croix.md": "A7 Page Breaks.md",
        "B1G-M BACKBONE.md": "A7 B1G-M Backbone.md",
        "B1G-M READING NOTES.md": "A7 B1G-M Reading Notes.md",
    },
    "M7": {
        "SCOPE AND SEQUENCE 2026-2027 - M7 as run.md": "M7 Scope and Sequence 2026-27.md",
        "SCOPE AND SEQUENCE 2026-2027.md": "County Scope and Sequence 2026-27.md",
        "IXL DUE DATES 2026-2027 - M7.csv": "M7 IXL Due Dates 2026-27.csv",
        "IXL SKILL PLAN.md": "M7 IXL Skill Plan.md",
        "UNIT AUDIT.md": "M7 Unit Audit.md",
        "ALIGNMENT - B1G-M Grade 7.md": "M7 B1G-M Alignment.md",
        "PROGRESS REPORT - 27 September 2026.md": "M7 Progress Report 2026-09-27.md",
        "A7 BUILD SYSTEM - review and adoption plan.md": "M7 Note - A7 Build System Review and Adoption Plan.md",
        "FOR A7 - apply rulings 20-28.md": "M7 Note - Rulings 20-28 for A7.md",
    },
}[PFX]
if PFX == "M7":
    REF.update({"BANK - Unit 4.md": u(4, "Question Bank") + ".md", "BANK - Unit 5.md": u(5, "Question Bank") + ".md",
                "UNIT 5 AUDIT.md": u(5, "Audit") + ".md", "AUDIT - Unit 4 Lessons 7-10.md": u(4, "Audit (Lessons 7-10)") + ".md"})


def package_moves(old_pkg, units, also_pdfs=True):
    """Moves for one old by-type package folder holding the given units: every file named the old
    way goes to its unit's by-lesson folder; the package's Reference/ documents take their new names."""
    moves, left = [], []
    for p in tracked(old_pkg + "/"):
        rel = p[len(old_pkg) + 1:]
        base = os.path.basename(p)
        np_ = new_place(base)
        if np_ and np_[2] in units:
            folder, name, n = np_
            moves.append((p, f"{os.path.dirname(old_pkg)}/{unit_folder(n)}/{folder}/{name}"))
        elif rel.startswith("Reference/") and len(units) == 1:
            n = units[0]
            wc = re.match(r"What Was Changed - (.+)\.md$", base)
            new = REF.get(base) or (u(n, f"What Was Changed ({wc.group(1)})") + ".md" if wc else base)
            moves.append((p, f"{os.path.dirname(old_pkg)}/{unit_folder(n)}/Reference/{new}"))
        else:
            left.append(p)
    return moves, left


def plan():
    moves, left = [], []
    if PFX == "A7":
        for n in (1, 2):
            m, l = package_moves(f"a7/packages/{unit_folder(n)}", [n]); moves += m; left += l
        for old, new in REF.items():
            moves.append((f"a7/reference/{old}", f"a7/reference/{new}"))
        for n, d in ((3, "unit03"), (4, "unit04")):
            for old, what in ((f"BANK - Unit {n}.md", "Question Bank"), (f"UNIT {n} AUDIT.md", "Audit"),
                              (f"UNIT {n} AUDIT - working log.md", "Audit Working Log"),
                              (f"UNIT {n} PRE-AUDIT - standards side.md", "Audit (Standards Side)")):
                moves.append((f"a7/{d}/{old}", f"a7/reference/{u(n, what)}.md"))
        moves.append(("m7/IXL SKILL PLAN - Math Nation Grade 7 (on-level).md", "a7/reference/M7 IXL Skill Plan.md"))
        fc = "a7/for Croix"
        for ext in ("docx", "pdf"):
            moves += [(f"{fc}/PLC/Essential Benchmark Learning Plan - MA.7.AR.2.2.{ext}", f"{fc}/PLC/M7 Essential Benchmark Learning Plan MA.7.AR.2.2.{ext}"),
                      (f"{fc}/early finishers/Power Up - early finishers.{ext}", f"{fc}/Early Finishers/A7 Power Up.{ext}"),
                      (f"{fc}/early finishers/Power Up - ANSWER KEY.{ext}", f"{fc}/Early Finishers/A7 Power Up - Key.{ext}"),
                      (f"{fc}/early finishers/Power Up review - early finishers.{ext}", f"{fc}/Early Finishers/A7 Power Up Review.{ext}"),
                      (f"{fc}/early finishers/Power Up review - ANSWER KEY.{ext}", f"{fc}/Early Finishers/A7 Power Up Review - Key.{ext}"),
                      (f"{fc}/syllabus/A7 Syllabus 2026-27.{ext}", f"{fc}/Syllabus/A7 Syllabus 2026-27.{ext}")]
        for f in ("build_powerup.js", "build_powerup_review.js", "data.json"):
            moves.append((f"{fc}/early finishers/{f}", f"{fc}/Early Finishers/{f}"))
        moves.append((f"{fc}/syllabus/build_syllabus.js", f"{fc}/Syllabus/build_syllabus.js"))
    else:
        sept = "m7/packages/M7 Units 2-4 - 14 September package"
        gone = "m7/archive/14 September package - superseded"
        deliv = "m7/archive/deliveries to 4 October"
        pk = "m7/packages"
        superseded = {f"M7 3.0{k}  {t}" for k in (5, 6, 7, 8) for t in ("Slides.pptx", "Teacher Edition.docx")} | \
                     {"M7 3  Unit Review.docx", "M7 3  Unit Review Key.docx", "M7 3  Unit Assessment.docx", "M7 3  Unit Assessment Key.docx"}
        for p in tracked(sept + "/"):
            rel, base = p[len(sept) + 1:], os.path.basename(p)
            np_ = new_place(base)
            if np_ and np_[2] in (2, 3) and base not in superseded:
                folder, name, n = np_
                moves.append((p, f"{pk}/{unit_folder(n)}/{folder}/{name}"))
            else:                      # Unit 4 as first delivered, the September versions the recut replaced, START HERE
                moves.append((p, f"{gone}/{rel}"))
        # Unit 3's later deliveries are its current files
        for p in tracked(deliv + "/"):
            rel, base = p[len(deliv) + 1:], os.path.basename(p)
            np_ = new_place(base)
            current = (("/" not in rel and re.match(r"M7 3\.0[5-8]  (Slides|Teacher Edition)\.", base))
                       or rel.startswith("Unit 3/")
                       or (rel.startswith("Unit 3 review day/M7 3  Unit Review")))
            if current and np_:
                folder, name, n = np_
                moves.append((p, f"{pk}/{unit_folder(n)}/{folder}/{name}"))
        for old, new in REF.items():
            moves.append((f"m7/reference/{old}", f"m7/reference/{new}"))
        fc = "m7/for Croix"
        for ext in ("docx", "pdf"):
            moves += [(f"{fc}/Learning plans/Essential Benchmark Learning Plan - MA.7.AR.2.2.{ext}", f"{fc}/Learning Plans/M7 Essential Benchmark Learning Plan MA.7.AR.2.2.{ext}"),
                      (f"{fc}/Learning plans/Exit Tickets - MA.7.AR.2.2.{ext}", f"{fc}/Learning Plans/M7 Exit Tickets MA.7.AR.2.2.{ext}"),
                      (f"{fc}/Learning plans/Exit Tickets Key - MA.7.AR.2.2.{ext}", f"{fc}/Learning Plans/M7 Exit Tickets MA.7.AR.2.2 - Key.{ext}"),
                      (f"{fc}/PROGRESS REPORT - 27 September 2026.{ext}", f"{fc}/M7 Progress Report 2026-09-27.{ext}")]
        moves.append((f"{fc}/VERIFICATION - Essential Benchmark Learning Plan MA.7.AR.2.2.md",
                      f"{fc}/Learning Plans/M7 Essential Benchmark Learning Plan MA.7.AR.2.2 - Verification.md"))
    return moves, left


def current_unit_list():
    """Old name -> new name for the units the build rewrote (they are regenerated, not moved): read
    from the package trees as they stood in the commit before the renaming."""
    rows = []
    base = "a7/packages" if PFX == "A7" else "m7/packages"
    for n in ((3, 4) if PFX == "A7" else (4, 5)):
        old_pkg = f"{base}/{unit_folder(n)}"
        for p in git("ls-tree", "-r", "--name-only", "-z", OLD_COMMIT, "--", old_pkg + "/").stdout.split("\0"):
            if not p:
                continue
            ob = os.path.basename(p)
            # M7's packages were already by lesson, under names of the old kind
            np_ = new_place(ob.replace(" Handout Key", "  Handout Key") if False else ob)
            if np_:
                rows.append((p, f"{base}/{unit_folder(n)}/{np_[0]}/{np_[1]}"))
            elif ob.startswith("BANK - Unit"):
                rows.append((p, f"{base}/{unit_folder(n)}/Reference/{u(n, 'Question Bank')}.md"))
            elif "/Reference/" in p and PFX == "A7":
                m = re.match(r"UNIT (\d) AUDIT - Math Nation package\.md", ob)
                new = (u(n, "Audit") + ".md") if m else REF.get(ob, ob)
                rows.append((p, f"{base}/{unit_folder(n)}/Reference/{new}"))
    return rows


OLD_COMMIT = {"A7": "0ba8b9e", "M7": "3cba2d6"}[PFX]      # each repository's head before the renaming

def write_list(rows):
    ref = f"{'a7' if PFX == 'A7' else 'm7'}/reference/{PFX} Rename List 2026-10-04.csv"
    with open(os.path.join(ROOT, ref), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["old path", "old name", "new name", "new path"])
        for a, b in rows:
            w.writerow([a, os.path.basename(a), os.path.basename(b), b])
    return ref


if __name__ == "__main__":
    moves, left = plan()
    if "--relist" in sys.argv:
        was = set(git("ls-tree", "-r", "--name-only", "-z", OLD_COMMIT).stdout.split("\0"))
        rows = sorted({(a, b) for a, b in moves if a != b and a in was} | set(current_unit_list()))
        unknown = [a for a, b in rows if a not in was]
        if unknown:
            sys.exit(f"the list names {len(unknown)} old files the commit does not have, e.g. {unknown[:3]}")
        missing = [b for a, b in rows if not os.path.exists(os.path.join(ROOT, b))]
        if missing:
            sys.exit(f"the list names {len(missing)} files that are not there, e.g. {missing[:3]}")
        print(f"wrote {write_list(rows)} ({len(rows)} rows; every new path exists)")
        sys.exit(0)
    moves = [(a, b) for a, b in moves if a != b and os.path.exists(os.path.join(ROOT, a))]
    targets = [b for a, b in moves]
    dup = sorted({b for b in targets if targets.count(b) > 1})
    clash = sorted(b for a, b in moves if os.path.exists(os.path.join(ROOT, b)))
    if dup or clash:
        sys.exit(f"refused: two files would take one name {dup[:5]} / a target already exists {clash[:5]}")
    if "--list" in sys.argv or "--apply" not in sys.argv:
        for a, b in moves:
            print(f"{a}\n   -> {b}")
        print(f"\n{len(moves)} moves; {len(left)} files in the old packages keep their place:")
        for p in left:
            print("   ", p)
        sys.exit(0)
    for a, b in moves:
        os.makedirs(os.path.dirname(os.path.join(ROOT, b)), exist_ok=True)
        r = git("mv", a, b)
        if r.returncode:
            sys.exit(f"git mv failed: {a} -> {b}: {r.stderr.strip()}")
    rows = sorted(moves + current_unit_list())
    print(f"moved {len(moves)} files; wrote {write_list(rows)} ({len(rows)} rows)")
