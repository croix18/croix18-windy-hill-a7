# State of the work — 25 October 2026 (read this first)

## 25 October, late morning — the kit's open items closed; Units 4–6 reinstalled; the website up to date

Croix, 9:15 am: *"Fix the kit, fix units 4 and 5 … Don't move on yet to unit 11."* Then 9:36: *"Yes please see to each
one of those issues. I give you permission to edit and to make fixes on the website."*
- **The kit (Windmill):** `7611a99` — a test paper says how long its test is: the plan's test days for the unit, else
  `EXAM_PERIODS` (1 in `a7/build/course.py`, ruling 51); the teacher copy's printed test the same, with no "Answer:"
  lines; the Lesson Plan's Notes row without the exponents unit's "Expand once per law". `02de689` — figures on a Lexend
  paper lettered in Lexend (ruling 46); the division Hint never states its answer (for 45 ÷ 3 it said "45 − 30 = 15 is
  left"; `check/hints.js` now reads 400,000 of them); the teacher bar's wording. Both sit on the head engineer's ruling 53
  (`fbac773`, IXL due by the unit test), which every unit below is built on.
- **Units 4 and 5 rebuilt and installed at 0 findings:** every form reads "one class period" (Unit 4's test is Mon
  26 Oct; its two forms were also sent to Croix); Unit 5's Reference Sheet prints "scale factor (k)" (its "($k$)" showed
  its dollar signs).
- **Unit 6 — triangles named by their corners** (the FAST reader's note): 6.07's Notes II teaches "triangle ABC is
  similar to triangle DEF" — the order of the letters is the matching; board 2 is a named turned pair (now 6-8-9 and
  18-24-27, so the small triangle's letters clear its lengths); independent question 2 gives names and lengths only. The
  practice paper's question 12, the Review's Part F question and the Reference Sheet name their triangles; half the
  practice page's question-12 sets do, the corners lettered, Show me how and the Hint using the letters; the oracle works
  x out by the letters and by size and they must agree; 33 of 33 planted errors caught; content version 2 (audit §8).
  Rebuilt and installed at 0 findings.
- **Practice pages rebuilt on the new kit:** Units 3, 4 and 6 and their teacher copies (every check passed).
- **Unit 3's package is not rebuilt:** today's kit counts a vocabulary minute, and 3.01's whiteboard round would drop to
  9 minutes (the floor is 10), so a rebuild means re-timing lessons already taught. Its test (15 Oct) is over; print a
  Unit 3 make-up from the teacher copy, which is fixed. Its package papers still say "two class periods".
- **The stale kit copy at the top of `a7/` is removed** (52 files, 24 Oct; nothing read it).
- **The website** (mrshaffer-site, Croix's permission at 9:36): A7 published from this commit — every unit's package
  (Units 4–6 rebuilt; Unit 6 for the first time), the practice pages and teacher copies of Units 3, 4 and 6, and the
  web slides. The site's commit and its deploy are in the Windmill HANDOFF.
- **Windmill:** `7611a99`, `02de689`; the HANDOFF entry after the site.

## 25 October — A7 Unit 6 and Thread B are built, reviewed and installed

The kickoff ("KICKOFF — A7 Unit 6 and Thread B", followed step by step) made this the build chat for **Unit 6,
Relationships in Triangles** (taught Fri 6 – Mon 16 Nov, the test Tue 17 Nov) and **Thread B** (Wed 18 – Thu 19 Nov,
after the test and not on it). Ruling 52 moved the year mid-build (Unit 11 in December; slope is Unit 10).

- **Built (`a7/build/u6/`, 0 gate findings):** 6.01 (book 6.01–02 merged, MA.8.GR.1.3), 6.03 and 6.04 (GR.1.1), 6.05 and
  6.06 (GR.1.2), 6.07 (book 6.07–08 merged, GR.2.4), Thread B 6.T1 (T-B1, GR.1.4, the 43-minute Wednesday) and 6.T2
  (T-B2, GR.1.5); `u6/unit.py` — the Reference Sheet (the state's two theorems as the FAST sheet prints them), the Review
  (home Mon 16 Nov; A7 has no review day) and the **Practice Test alone, as the test's blueprint** (ruling 49: the unit
  test is a random set of the practice page; 14 questions, 18 points, 3 / 6 / 6 / 3, one period, ruling 51).
- **Installed** (`a7/packages/A7 Unit 6 - Relationships in Triangles/`): `build_all.py u6 --install` at 0 gate and 0 check
  findings on Windmill `c9c3e8a`, and again later that day on `02de689` (above); the master sheet regenerated, 0
  problems.
- **The practice page (`a7/practice/u6/`), built:** `A7 Unit 6 Practice Test.html` and the teacher copy
  (`teacher/A7 Unit 6 Teacher Copy.html`), each with its CHECKED. Its checks — `u6_check.js` (3,000 sets), `verify.py` (a
  sympy oracle that reads every question back from what a student sees), 31 planted errors — the stability lock, the
  variety floor and the kit's browser check pass. The teacher copy prints the test as 1–5 random sets with the paper's
  shape (no set number on a student's sheet; points; the key with its set number and the score tracker). Published on
  25 Oct with Croix's permission (above).
- **The unit's standing decisions** (audit §6): every square root a student takes has a whole radicand up to 225
  (Clarification 3, read literally), so a whole hypotenuse is 5, 10, 13 or 15; no radicand on the papers has a square
  factor; no distance formula (a slanted distance is its right triangle on the grid); every mirror and nested item says
  its triangles are similar.
- **Reviewed before shipping** (kickoff step 7): an explicit-instruction reviewer, an adversarial critic and a Florida FAST
  item-writing educator, each alone — 8 blockers (5 different), 41 fixes, 31 notes, with the fixes, in the audit's §8
  (`a7/reference/A7 Unit 6 Relationships in Triangles - Audit.md`).
- **The kit, fixed with Croix's permission** ("Fix it. I give you permission", 25 Oct) in Windmill `c9c3e8a`: `deckkit`
  gives a wrapping IXL skill name the rows it needs (T-B1's two long names overprinted the next row, so the unit could
  not install); the practice kit's printed test has the paper's shape and no set number on the student's sheet; its
  browser check reads "&lt;" as "<". Vendored here (`tools/vendor_windmill.py`; `practice_kit.py --vendor`).
- **Commits:** `943d42c7` audit and outlines · `5543d4a5` 6.01 · `f26614d3` 6.03 · `4f76e0b6` 6.04 · `a5222251` 6.05 ·
  `64677830` 6.06 · `1b8682be` 6.07 · `a1d0d7b7` T-B1 · `9f55139e` T-B2 · `b8ff3013` unit documents · `292d4c00` the
  practice page · `b5638493` the review pass · `28e8a92c` the notes before the install · then the install and the built
  page, on Windmill `c9c3e8a`.
- **Open:** nothing from the kit list (all fixed, above). Unit 3's package papers still say "two class periods" (above).
  The Windmill HANDOFF's own open items (publish_web.py and unreviewed units) are not A7's.
- **Next:** Unit 11, Solving Equations and Systems (MA.8.AR.2.1, AR.4.1–4.3) — taught Mon 30 Nov – Thu 10 Dec, the test
  Fri 11 Dec; due 23 Nov, the same procedure in `u11/`.
