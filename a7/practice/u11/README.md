# A7 Unit 11 practice test (student page)

Built 14 Nov 2026 on the practice-test kit (`../kit/README.md`, Windmill c2aa88d — one question at a time, as on the FAST), which
holds everything common to every unit's page: sets, the two modes, the pager, the coach card, the help ladder, Try a similar one,
scoring, saved progress, Print, the calculators, and the checks that run in a real browser.

- **Not published from the build session.** The page is `unit-11-practice-test.html` (the claude.ai artifact body) and
  `A7 Unit 11 Practice Test.html` (the same page as one complete file, for the class website or Google Sites).
- **The teacher copy** (`teacher/`) is the student page plus the kit's teacher bar. Ruling 49: the Unit 11 test is a random set
  of this page (Tests A and B, make-ups, and the all-multiple-choice make-up of 14 Nov). Never on Google Sites.

## What it is

One page, **14 questions, 18 points**, four parts in the order and weights of the practice paper (`a7/build/u11/unit.py`, the
test's blueprint): 9 / 2 / 2 / 5 — MA.8.AR.2.1, AR.4.1, AR.4.2, AR.4.3. New numbers every set (`#set-4821` opens set 4821).
Every equation is generated FROM its solution and its shape, then solved again (coach.js re-derives every worked line from the
equation's pieces; `u11_check.js` and `verify.py` solve it a third and a fourth way). FAST house style: "An equation is shown.",
the equation on its own line, "What is the value of n?", and a box that already says "n =".

1. Like terms and one distribution, a(bn + c) ± dn = r (or dn + a(bn + c) = r); a whole, nonzero solution.
2. Variables on both sides, ah + b = ch + d, the larger multiplier on either side; a negative whole solution.
3. Parentheses on both sides with a FRACTION in front of one (½, ⅓, ¼, ⅔, ¾ or a negative one), f(bm + q) = r(m + t): every
   term the fraction multiplies comes out whole; the solution whole, or a half (the lead's change of 14 Nov).
4. A decimal distributed, k(av + b) = cv + d, k one of 0.2, 0.4, 0.5, 1.5, 2.5 or a negative of one; most sets have a product
   that is not whole (2.4k, 7.5); the solution whole or a half — the 21% FAST skill.
5. How many solutions: three equations, one of each ending in a random order, each a choice of One / No / Infinitely many; the
   one with one solution is x = 0 in about a third of sets, and its worked solution and walk find the value.
6. Fill the box: no solution (the number multiplying x), or infinitely many (that number with the same constant already there,
   or the constant itself) — the generator varies which.
7. Two plans that cost the same (storage, gym, pool pass, kayaks, art classes): a fee and a smaller price each time against a
   larger price and no fee or a smaller fee; the count whole, 2–15, and sensible in its story.
8. **Select ALL the systems that have (a, b) as a solution** (the lead's change of 14 Nov): one pair, five systems solved for y
   with integer multipliers (1 and −1 among them, the two different), two or three right; each wrong system is true for the
   pair in exactly one of its equations. The stem never says how many.
9. Is (x, y) a solution of the system shown? The verdict with its reason: yes — both true; no — false in the first; no — false
   in the second; yes — it makes one of them true (one is not enough). The pair is on one line only, or the solution.
10. The graph of two lines that intersect at a grid point inside the window: how many solutions (a choice). A horizontal line
    (y = 4) is one of the two in about one set in six.
11. Parallel lines, or one line for both equations written two ways (y = a(x + c) + d and y = ax + b; the stem says both
    graph as the one line shown) — Florida's same-line case: none or infinitely many.
12. The solution read from the graph (whole-number point of intersection, negative coordinates allowed; ½ may multiply x; a
    horizontal line about one set in six).
13. Two tables of values (x = 0…5): (a) the value missing from the first, (b) the solution — the one column where both agree.
14. (a) A story (one saves and one spends; two savers; two plants) with its graph, axes named and scaled by 5 or 10 (2 or 5 cm):
    when the two are equal and what both are, whole numbers on grid lines; (b) **its own graph**, a second system whose point of
    intersection has thirds-, fifths-, sixths- or sevenths-type coordinates at least 0.15 from every grid and half-grid line,
    estimated to the nearest tenth: right when x and y are each **within 0.1** of the exact point (the lead's change of 14 Nov;
    audit E15), so no grid or half-grid point is ever inside the accepted range, nor the swapped pair; the half lines are drawn
    pale.

**Figures** (`fig.js`): every line is drawn from its own m and b and clipped to the window; the first solid, the second dashed
and teal, told apart without colour, with a legend; a grid square at least 14 px at 390 px; axis numbers every 1 or 2. The
`<svg>` carries its window and scale, so the checks read every line back onto its equation.

**What the page cannot do as asked (the kit):** a part has one answer box. Question 12's paper says "Give its x and its y"; the
page asks for the ordered pair in one box labelled "as an ordered pair (x, y)" and reads (4, −2), 4, −2 or x = 4, y = −2 — two
boxes for one point is not something the kit's parts allow (a second box would be a second point). Questions 13(b), 14(a) and
14(b) are one box each too.

**The coach** names the unit's mistakes: the number in front distributed to the first term only (and the second only, for a
decimal); the sign of a negative multiplier lost; the like term left out or added the wrong way; the x-terms added instead of
taken from both sides; the number added undone the wrong way; stopping before dividing; dividing the fee by one price; a = a
read as no solution or as x = 0, x = 0 read as no solution; one equation true taken as enough; the coordinates swapped; the
point where one line meets the y- or x-axis; the column where two tables are only close; the nearest grid point for an estimate.
No false equation is printed as a line of work: "14 = −14 — never true" is an ending said in words. Multiplication is written
with parentheses or a dot, never × (no Hint either: the kit's arithmetic hints have × turned into ·). No "slope", no
"y-intercept": "the number multiplying x", "point of intersection".

## Ruling 43

The page never asks an equation, a system or a story that a lesson (warm-ups, notes, examples and Your Turns, whiteboards,
independent sets, banks), the review, the reference sheet or the practice paper shows. `shown43.py` reads them out of the specs
themselves (`a7/build/u11/l01–l08.py`, `unit.py`): 632 equations (the sizes of the printed numbers and the ending), 192
systems, 523 stories (a string with money or a rate in it). `python3 shown43.py --emit` writes `shown.js`, which the engine steers by; `u11_check.js` holds every set
to `shown.js` from the printed words, and `verify.py` reads the specs again on its own. Re-run `--emit` whenever a lesson changes.

## Variety (ruling 49)

Every part has at least 100 versions over set numbers 1–20,000; nothing is allowed under the floor. The fewest are Q11 (1,242)
and Q10 (2,013) — their lines are drawn from small multipliers to stay readable on a phone — then Q14(a) (2,242).

## The checks (`python3 ../kit/check/run.py .` runs them, then the lock, the variety floor and the browser checks)

| | |
|---|---|
| `u11_check.js` | 3,000 sets read back from their printed words with its own polynomial reader and exact arithmetic: the shape of the test (titles and the tracker's points read from `unit.py`; a marked constant holds the kinds of question); every equation solved; every key typed back in several forms; every named mistake typed, wrong and named; every worked line an equation with the first one's solutions; every Hint number step's arithmetic, no Hint stating its answer, one right option per Hint choice with a reason for each wrong one; every arithmetic claim in every sentence (≈ 230,000); Q8's pair in all ten equations; Q9's verdict and reason; every graph's lines, window, crossing and axis numbers read back from the SVG; every table value; Q14(b)'s tolerance; no ×, "slope" or "intercept" anywhere; ruling 43 against `shown.js`. Writes `dump.json`. |
| `verify.py` | The sympy oracle over the rendered HTML of 1,500 sets: every equation, box, story, pair, system, graph line, table and estimate worked again; every worked line and Hint step; every paper choice; ruling 43 from the specs; the test's sections and points. |
| `plant_check.py` | 43 planted errors (wrong keys in every question, a printed sign, a fraction's reciprocal, a decimal off the list, Q8's key and clean rule weakened together, a tolerance of 0.2, a crossing on a half line, a line drawn a unit high, a dashed line drawn solid, the axis numbered a step off, a grid too small, the worked lines distributing to one term, a Hint stating its answer, ×, "slopes", a mistake marked right, the paper offering the key as a wrong answer …): every one must be caught. |
| `mc_check.js` | 3,000 sets: three wrong answers for every typed part, in the key's shape, never the key, never inside an estimate's tolerance, each a named mistake or (counted) a value one away. |
| `show_set.js` | not a check: `node show_set.js 4821` prints one set with all its help, for reading it as a student does. |
