# A7 Unit 4 practice test (student page)

Croix (16 Oct 2026): *"Can you build the a7 unit 4 practice?"* Built on the practice-test kit (`../kit/README.md`), which
holds everything common to every unit's page: sets, the two modes, the coach card, Hint, Show me how, Try another, scoring,
the clock, saved progress, Print, the keypad and the checks that run in a real browser.

- **Published:** the claude.ai artifact *A7 Unit 4 Practice Test* (https://claude.ai/artifact/YJ2zpoFWzqc9mueqRVmwoX), and
  `A7 Unit 4 Practice Test.html` — the same page as one complete file — for the embed on his Google Site. Updating the embed
  in place keeps the address the students already have.
- **The teacher copy** (`teacher/`) is a separate private artifact: the student page plus both test forms printed with their
  keys. It is never put on Google Sites.

## What it is

- One page, **29 points**, three parts in the order and weights of the Unit 4 test (12 / 4 / 13), the same questions in the
  same positions, new numbers every set (`#set-4821` opens set 4821).
- **No question is one from the test** — Form A, Form B, or either written backwards. Every question carries its test
  numbers in `TEST` (engine.js) and a set that hits one draws again.
- **The two transfer items are replaced** (Croix, 16 Oct: "Same-skill stand-ins"): Q6 is the review's rate-times-time word
  problem, Q15 is evaluating a·x² at a negative x.

## No significant digits (21 Oct 2026, contentVersion 3)

Croix: *"Remove the questions pertaining to significant digits. Add, subtract, multiply and dividing scientific notation is
fine but anything asking how many significant digits should be removed."*

- **Part 2 is now *Real-World Problems in Scientific Notation*:** Q7 the area of a plate (multiply) and the speed of a vehicle
  (divide), Q8 the sum of two lengths and the difference of two masses (one power of ten apart). Every answer is the exact
  value in scientific notation, as on the test, and Part 2 says "Do not round." (the class learned on 20 Oct, in 4.04, to round
  measured answers). Gone: counting significant digits, both explain-the-rule questions, and the significant-digit multiple
  choice. A rounded answer is told so: "That is the answer rounded. Do not round: write every digit of the exact value."
- **Kept, unchanged:** every question in Part 1 and Part 3. Part 3's questions keep their 16 Oct slot names (`q12` … `q18`,
  now numbered 9 to 15), so a set keeps its Part 3 questions. Q6 lost the ".0" of its second number (it was there for
  significant digits).
- Same day: the √(a + b) question excludes Form B's numbers in both orders (√(64 + 36) was getting through), and the
  exclusion list carries Form B's corrected Devon question (3.4 × 10⁴, a gap of 2; the test had 10³, a gap of 3).
- Saved answers on the old sets are cleared with a notice — the kit does that whenever `contentVersion` goes up.

## The checks (`unit.json`; `python3 ../kit/check/run.py .` runs them all, then the lock and the browser checks)

The 16–19 Oct checks were lost with the session that wrote them; these replaced them on 21 Oct.

| | |
|---|---|
| `u4_check.js` | 3,000 sets: the shape of the test (titles read from `build/u4/unit.py`); every key typed back is right, with its unit too; every modelled mistake typed is wrong and named; the unfinished, standard-form and calculator forms are "Almost"; the clean rule, checked on its own; every worked line and Hint step carries the answer; every Hint choice has one right option and a reason for each wrong one; no Hint states its own answer; multiple choice and select-all mark their keys; no question is the test's. Writes `dump.json`. |
| `verify.py` | The independent check: every question read back from the HTML a student sees and worked again in exact fractions; every key, worked line and Hint step compared; Forms A and B read from the test spec's TeX — each of their 54 questions must be in the exclusion list, and no practice part may print its test part's numbers (in any order, for a sum or a product). |
| `plant_check.py` | 14 planted errors (a key off by a power, a misprinted exponent, a wrong worked line, a Hint expecting the wrong number, an exclusion dropped, the clean rule weakened, "Almost" marked right, …): the checks must catch every one. |
