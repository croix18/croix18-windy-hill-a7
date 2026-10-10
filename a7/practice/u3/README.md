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
python3 build.py              # → unit-3-practice-test.html (artifact body) and preview.html
```

The independent check found one real bug before publishing: `decStr` (exact decimal writer) halved
some small numbers (7.8 × 10⁻⁸ shown as 0.000000039). Fixed and brute-forced.

To republish: `python3 build.py`, then publish `unit-3-practice-test.html` to the same artifact URL
(see the Windmill HANDOFF for it). Bump `VER` in ui.js if generators change, so old saved sets reset.
