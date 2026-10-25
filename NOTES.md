# State of the work — 25 October 2026 (read this first)

## 25 October — A7 Unit 6 and Thread B are built and reviewed; the install waits on the kit

The kickoff ("KICKOFF — A7 Unit 6 and Thread B", followed step by step) made this the build chat for **Unit 6,
Relationships in Triangles** (taught Fri 6 – Mon 16 Nov, the test Tue 17 Nov) and **Thread B** (Wed 18 – Thu 19 Nov,
after the test and not on it). Ruling 52 moved the year mid-build (Unit 11 in December; slope is Unit 10).

- **Built (`a7/build/u6/`, 0 gate findings):** 6.01 (book 6.01–02 merged, MA.8.GR.1.3), 6.03 and 6.04 (GR.1.1), 6.05 and
  6.06 (GR.1.2), 6.07 (book 6.07–08 merged, GR.2.4), Thread B 6.T1 (T-B1, GR.1.4, the 43-minute Wednesday) and 6.T2
  (T-B2, GR.1.5); `u6/unit.py` — the Reference Sheet (the state's two theorems as the FAST sheet prints them), the Review
  (home Mon 16 Nov; A7 has no review day) and the **Practice Test alone, as the test's blueprint** (ruling 49: the unit
  test is a random set of the practice page; 14 questions, 18 points, 3 / 6 / 6 / 3, one period, ruling 51).
- **The practice page (`a7/practice/u6/`):** its sources and checks — `u6_check.js` (3,000 sets), `verify.py` (a sympy
  oracle that reads every question back from what a student sees), 31 planted errors — the stability lock and the
  variety floor; the teacher copy beside it (`teacher/`). **Not built:** the kit's browser check misreads "&lt;" in a
  choice and fails a correct page. Publishing stays with Croix.
- **The unit's standing decisions** (audit §6): every square root a student takes has a whole radicand up to 225
  (Clarification 3, read literally), so a whole hypotenuse is 5, 10, 13 or 15; no radicand on the papers has a square
  factor; no distance formula (a slanted distance is its right triangle on the grid); every mirror and nested item says
  its triangles are similar.
- **Reviewed before shipping** (kickoff step 7): an explicit-instruction reviewer, an adversarial critic and a Florida FAST
  item-writing educator, each alone — 8 blockers (5 different), 41 fixes, 31 notes, with the fixes, in the audit's §8
  (`a7/reference/A7 Unit 6 Relationships in Triangles - Audit.md`). After the fixes: gates 0; `checks.py` 4, all the
  kit's IXL rows below; the page's checks sound; the master sheet 0 problems.
- **Not installed:** `build_all.py u6 --install` refuses while `checks.py` has findings, and its only four are the kit's —
  `deckkit` sets IXL rows at a fixed 0.36 in, so T-B1's two long skill names overprint the next row (slide 35; All Slides
  247). Reported; not edited, not acked. When the fix lands: vendor (`tools/vendor_windmill.py`), `build_all.py u6
  --install`, the master sheet, push; then build the page and the teacher copy (`practice/kit/check/run.py`).
- **Commits:** `943d42c7` audit and outlines · `5543d4a5` 6.01 · `f26614d3` 6.03 · `4f76e0b6` 6.04 · `a5222251` 6.05 ·
  `64677830` 6.06 · `1b8682be` 6.07 · `a1d0d7b7` T-B1 · `9f55139e` T-B2 · `b8ff3013` unit documents · `292d4c00` the
  practice page · `b5638493` the review pass.
- **Open — the kit (Windmill), reported to Croix:** the IXL rows above; `practice/kit/check/page.js` reads "&lt;" twice;
  the teacher copy's random test prints "Set N" on the student header (and `#set-N` on the student page opens that set
  with its worked answers), with no points, no follow-through line, no Score Tracker, and "Answer:" labels; `plankit`
  prints the exponents unit's "Expand once per law" in every Lesson Plan; printed figures are lettered in STIX on Lexend
  papers (ruling 46); the practice kit's core Hint can give a division's answer away (Unit 6 wraps it).
- **Open — elsewhere:** the A7 Unit 5 Reference Sheet prints "scale factor ($k$)" with its dollar signs showing; a stale
  tracked copy of the build kit sits at the top of `a7/` (`a7/lib/`, `a7/build_all.py` …, stamped Windmill `90fd2c4`)
  beside the real one in `a7/build/`.
- **Next:** Unit 11, Solving Equations and Systems (MA.8.AR.2.1, AR.4.1–4.3) — taught Mon 30 Nov – Thu 10 Dec, the test
  Fri 11 Dec; due 23 Nov, the same procedure in `u11/`.
