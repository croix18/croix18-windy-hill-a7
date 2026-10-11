# A7 Unit 3 practice test (student page)

Croix asked (10 Oct 2026): *"Can you build out a practice test tool that students can use to practice the
test style questions. It should have different numbers than the test."*

Published as the private artifact **"Unit 3 Practice Test"** in Croix's claude.ai gallery. Students can
open it only after he shares it (Share → link; a public link if students have no Claude accounts).

## What it is

- One page, 36 points, four parts in the order and weights of the real Unit 3 test (9 / 9 / 8 / 10),
  the same question types: single power, value, positive exponents, monomials, scientific notation,
  standard form, "how many times larger", E-notation, MC and select-all.
- **Numbers are generated from a set number (1–99999).** `#set-4821` in the link opens set 4821, so a
  teacher can say "everyone do set 4821". "New set" picks a random one.
- **No question on the real test can appear** — every question is written out and compared with the
  test's 36 (`testSet()` in engine.js); a set that hits one is regenerated. Q4 also never uses the
  test's 125 = 5³.
- Two modes: **Check as I go** (Check button, feedback, "Show me how" steps) and **Like the real test**
  (no feedback until "Finish & mark"). Score = right on the first try; time on a stopwatch.
- Answers stay in the student's browser (localStorage, per set). No names, nothing sent anywhere.

## The coach (version 2, 10 Oct 2026)

Croix: *"strengthen that some more both in terms of the explanation and show mes. I want it to adapt perfectly to whatever they
submit and explain exactly where they went wrong and how to solve it next time."*

`coach.js` turns a wrong or nearly-right answer into feedback, in this order:
1. **Typing slips** (missing ^ as in `h3`, `10 5` for 10^5, calculator `E`, two ^ in a row, an equation for n not yet solved) —
   explained and **not counted** as a try.
2. **Exact mistakes**: each question family has mistake models (multiplied the exponents, multiplied the bases, raised only the
   top, dropped the minus sign, moved the 8 to the bottom too, counted the zeros, subtracted the numbers in "how many times", …).
   One fires only when the typed answer has that mistake's exact value AND its shape (a single power must have the same base and
   exponent; whole-number fractions must match as written; negative exponents present in both or neither). The sentence is
   "That is what you get if you …", with the student's numbers.
3. **Piece by piece**: base vs exponent; number part vs each letter's exponent (monomials); first number vs exponent (scientific
   notation); digits vs decimal place (standard form); number vs power of 10 ("how many times"). Each piece is called right or
   explained.
4. **Facts**: wrong sign (with "nothing here is negative" when true), upside down, both top and bottom negative, "check it: if
   n = 4 then …".
Every wrong answer also shows **Next time:** the family's rule. **Hint** reveals the worked solution one step at a time;
**Show me how** reveals it all and marks the step where the student's answer went off. A hint used before the first check
means that question can't count as right on the first try.

Worked solutions (`solution(part)`) are chains: every step's expression equals the question (the n-equation: true at the
answer), the last is the answer. Saved state moved to `v2` (the per-question record changed shape).

## Version 3 (10 Oct 2026): help me solve, try another, one part, pictures

Croix picked four upgrades and said Help-me-solve must be *"an option or like a help me solve this type thing"*, not the default.
- **Help me solve this — REMOVED from the page 11 Oct 2026.** Croix: *"I don't like the help me solve this. It doesn't really make
  sense."* The button is gone (ui.js `if (false && …)`); `checkWork` and its tests stay in coach.js in case it comes back in
  another form. Don't re-add it without asking him. What it was (button on every typed question): the student types work one step per line; `checkWork` marks each
  line ✓ if it equals the question (equations: true at the right n and not at other values — `n^2 = 36` is refused). The first
  unequal line gets: for the very first step, the exact mistake list; after that, only true comparisons with the line before
  ("this is 3^2, what comes before it equals 3^3"; number part / each letter's exponent) plus the step to take. "Use my last
  line as my answer" fills the box. Using it before the first check counts as help (no first-try point).
- **Try another like this**: after a miss, a fresh question of the same kind at the same position from another generated set
  (never the same question again); two right first-try in a row clears it from "misses".
- **Practice menu**: whole test; one part (two rounds, round 2 never repeats a round-1 question); my misses (positions missed
  on the first try, saved on the device, with new numbers in two rounds).
- **Pictures** (`visual.js`, "See why it works", shown with the full solution or once right — they state the answer):
  factor tiles, copies grid, cancelling factors, the ladder of powers (÷ base each step), pairs of negatives, copies of a
  product, and the decimal-point hop. Every count/value is re-derived by `coach_check.js`, which also proves it catches planted
  picture errors.
- Saved state `v3` (keys per set and practice choice). Third adversarial review: 10 defects + low items, all fixed and pinned.

## Walk me through it (11 Oct 2026)

Croix asked for a guided walkthrough in place of Help me solve. `walk.js`: each question becomes 1–5 small steps — tap an
option (a wrong tap says why and stays crossed out) or type one plain number (`readNum` takes only a number or fraction, so
typing the question back doesn't count; "how many places" accepts the size with or without the sign). After each step the
work so far is shown; the walk ends at the answer with "Now type it in the answer box". A Close button; opening it before the
first check counts as help (the panel says so). Options that would give the same number for particular values (2 + 2 = 2 × 2,
(1/4)^2 with "only the bottom", 4 ÷ 2 = 4 − 2) are left out for those values.
Checked by coach_check.js: one right option per tap, a reason on every wrong option, every typed answer re-derived from its own
question text ("What is 9 + 8?" → 17), every shown line equal to the question, the walk ending at the finished answer, plus
87/87 planted errors caught and pins for the fourth review's findings (e.g. negDen no longer offers "a negative number", which
is true for odd powers).

## Marking

`mark(part, typed)` in engine.js reads what was typed (^ powers, / fractions, × or x for times in
scientific notation, unicode superscripts, commas, "n = 5", work joined with "=") and compares exact
values (BigInt rationals; letters are checked at four rational points). Then it checks the FORM each
question asks for ("right value, fix the form" is shown as *Almost* and loses the first-try point, as it
would on paper). Ambiguous input like `4/m^6n^2` is not guessed: the student is asked for parentheses.

## Checks (run all after any change; Rule 0: student-facing math must be sound)

```
node test_engine.js 20000     # 20,000 sets: every key typed back is marked right; mistakes never right;
                              # MC distinct with one key; points 9/9/8/10; no test question; ~120 pinned
                              # reader cases (incl. every defect from the 10 Oct adversarial review)
python3 verify.py             # independent sympy re-check of 4,000 sets from dump.json (exact rationals)
node steps_check.js           # every "a + b = c", "b^k = v" claim in steps/messages recomputed (20,000 sets)
node look3.js                 # Playwright: types every key into the page for 4 sets → 36/36
node coach_check.js 1500      # coach: every solution step = the question; every mistake model typed back gets its own words;
                              # ~670,000 near-miss answers fuzzed; every arithmetic chain in any sentence recomputed; no
                              # hyphen-as-minus; plus pinned cases for every defect from the coach review
python3 verify_coach.py       # independent sympy check of 52,500 worked solutions
python3 build.py              # → unit-3-practice-test.html (artifact body) and preview.html
```

The independent check found one real bug before publishing: `decStr` (exact decimal writer) halved
some small numbers (7.8 × 10⁻⁸ shown as 0.000000039). Fixed and brute-forced.

To republish: `python3 build.py`, then publish `unit-3-practice-test.html` to the same artifact URL
(see the Windmill HANDOFF for it). Bump `VER` in ui.js if generators change, so old saved sets reset.
