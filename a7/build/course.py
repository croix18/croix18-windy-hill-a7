"""What is A7's own, in one place. The build kit (lib/, checks.py, the drivers) is shared with the
on-level course and published from croix18/Windmill; everything this course settles for itself is
a name here. `python3 -m lib.profile` prints the whole profile and marks what this file sets.
"""
COURSE = "Grade 7 Accelerated"     # printed on every footer and eyebrow
PREFIX = "A7"                      # file names: "A7 3.01 Product Laws of Exponents - Slides.pptx"
COURSE_CODE = "1205050"
COURSE_KEY = "acc"                 # the key Windmill's spine and room use for this course
GRADE_FAST = "Grade 8 FAST"
# The units' titles: every unit-wide file and folder is named from here (lib/names.py), and
# unit.py's own title must agree. Add a unit here before building it.
UNITS = {1: "Equations and Inequalities", 2: "Real Numbers, Square Roots and Cube Roots",
         3: "Exponents and Scientific Notation", 4: "Solving Problems with Rational Numbers"}
IXL_SMARTSCORE = 67                # ruling 28 — 67 accelerated, 60 on-level (Croix, 20 Sep)

SET = "handout"                    # ruling 21: the six questions are a printed page and its key
STEPS = "required"                 # ruling 39: every answer slide shows its steps (all of Units 3 and 4 written, 5 October)
CLOSE = False
BANK = "docx"                      # Question Bank and Question Bank - Additional, each with a key
TE_STYLE = "lines"
PLAN_STYLE = "sections"
SLOTS = "exponent"                 # §2a: base blue, exponent orange, read off the layout
CAPS = ("fracexp", "sci", "gap", "radicand")     # MA.8.NSO.1.5 and 1.7's boundaries are taught here

SUITE_DOC = "../reference/HOUSE STYLE.md"
SUITE_BLOCK = "suite:a7"
