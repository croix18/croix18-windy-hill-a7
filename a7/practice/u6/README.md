# A7 Unit 6 practice test (student page)

Built 25 Oct 2026 from the Unit 6 kickoff (step 6), on the practice-test kit (`../kit/README.md`), which holds everything
common to every unit's page: sets, the two modes, the coach card, Hint, Show me how, Try another, scoring, the clock, saved
progress, Print, and the checks that run in a real browser.

- **Not published from the build chat.** The kickoff keeps publishing with Croix: the page is `unit-6-practice-test.html` (the
  claude.ai artifact body) and `A7 Unit 6 Practice Test.html` (the same page as one complete file, for the embed on his Google
  Site).
- **The teacher copy** (`teacher/`) is the student page plus the kit's teacher bar. Ruling 49: the Unit 6 test is a random set
  of this page, so the bar prints 1–5 forms, each a different set headed as the test, every key on its own page. It is never put
  on Google Sites.

## What it is

- One page, **14 questions, 18 points**, four parts in the order and weights of the Unit 6 test (`a7/build/u6/unit.py`, the
  practice test as the test's blueprint, ruling 49): 3 / 6 / 6 / 3 — MA.8.GR.1.3, 1.1, 1.2, 2.4. New numbers every set
  (`#set-4821` opens set 4821). Ruling 51: one period. Thread B (angle facts) is not on the test, so it is not here.
- **The questions** (each the test's, in its place):
  1. Which set of side lengths can form a triangle? — one set lies flat (a + b = c), one fails only when the two *shorter*
     sides are added, one fails when the longest is added to another.
  2. Select ALL the right triangles — five sets, one to three right; one right set always lists its longest side first (the set a
     student who tests the last number misses); the wrong ones are a near miss, three numbers in a row, two legs of a triple with
     the wrong third side, a triangle that is not right, and one that lies flat.
  3. The range of the third side — the right inequality, "between the two sides", ≤ for <, and 0 for the lower end.
  4. (a) a whole hypotenuse, (b) a whole leg.  5. A hypotenuse to the nearest tenth.  6. Which equation finds x (a right
     triangle drawn to scale, turned and flipped; its doubling choice is a² + x² = 2 · c, and no leg is a sliver or under 3).
     7. A path across a garden, lawn, patio, playground or courtyard, its two sides in either order ("9 meters by 13 meters"),
     each place at a real size: the path to the nearest tenth, and how much shorter it is than two sides (follow-through from
     part a, ruling 19).
  8. A distance read from two points on a grid (whole).  9. A distance from two coordinates to the nearest tenth.  10. A right
     triangle on the grid: (a) the side that crosses an axis, (b) the perimeter to the nearest tenth (follow-through).
     11. A town map: along the streets, and in a straight line.
  12. A pair of similar triangles, the copy turned or flipped: find x (never sides a, b, c with b² = ac, whose copy's two
     sides could be matched two ways).  13. A shadow (most sets; a man or woman 5 to 6 ft tall, a child 4 to 5.5 ft) or a
     mirror on the ground (the lesson's second setting, and the words say "The two right triangles are similar."): how tall?
     14. Which triangle is similar — the scale copy, every side plus one number, two sides scaled and the third off, and two of
     the first triangle's own sides; every choice lists its sides from shortest to longest.
- **The words are the state's.** A length is written out in the words ("9 inches", never "9 in", which reads as a word); a
  rounded answer is asked with the state's own sentence, "Round your answer to the nearest tenth."; select-all says "Select ALL".
- **The unit's bounds on every question** (the lesson outlines' standing decisions): a square root a student takes is of a whole
  number up to 225 (MA.8.GR.1.1/1.2 Clarification 3), so a whole hypotenuse is 5, 10, 13 or 15; no distance formula — a slanted
  distance is the right triangle on the grid, and every grid segment crosses an axis; the converse tests the longest side;
  similar triangles by the scale factor k. A length asked "to the nearest tenth" may come from a radicand with a square factor
  (√72): the decimal is the answer, and no line prints the radical (it says "the square root of 72"), so the page never shows
  an unsimplified radical.
- **The coach names the unit's mistakes:** adding the legs; the forgotten square root; adding the squares for a leg (longer
  than the hypotenuse); the hypotenuse taken as a leg; subtracting across zero; counting grid lines instead of spaces; cutting
  the decimal off instead of rounding, or rounding to a whole number; matching similar sides by where they sit on the page;
  adding instead of multiplying; matching a height with a shadow. "Almost" for the exact root of a tenth answer, a longer
  decimal that rounds to it, and √169 for 13.
- **Figures are drawn to their own numbers** (`fig.js`, the M7 Unit 4 board grown for a coordinate plane): the pale grid may sit
  under a label; the axes, every side and every point may not. The axes' numbers sit outside the plane below and to the left;
  a point's name ("A(−7, 1)", as on the paper) may hang over the top or right edge, and the plane widens until every label has
  a clear place. A leg that crosses the other axis keeps its number off that axis (6.05 Notes III, 24 Oct). Lexend has no
  italics (ruling 46): the words on a figure and the axes' x and y are upright.

## Variety (ruling 49)

Every part has at least 100 versions over set numbers 1–20,000 except two, allowed in `unit.json` with their reasons: **2.1a**,
a whole hypotenuse — four triangles within the radicand bound, legs either way round: 8 versions; **2.1b**, a whole leg — the
21 right triangles with c² − a² a square of 15 or less. (2.3, the equation choice, has 110 versions; 2.4, the path across a
place at a real size, 106 — its sides in either order; 3.1's answer is one of the four whole distances, but its two points
come in 2,219 placements.)

## The checks (`unit.json`; `python3 ../kit/check/run.py .` runs them all, then the lock, the variety floor and the browser checks)

| | |
|---|---|
| `u6_check.js` | 3,000 sets: the shape of the test (titles read from `build/u6/unit.py`); every key typed back is right, with its unit and with "about"; every modelled mistake typed is wrong and named (a mistake that ends on a root, typed to the tenth or the hundredth); the exact root and the longer decimal are "Almost", the cut-off decimal wrong; the clean rule, checked on its own; follow-through from a wrong part (a), its value worked out here and not taken from the coach; every worked line and Hint step carries the answer; no Hint asks for a number no one can type or gives its own answer away; every Hint choice has one right option and a reason for each wrong one; every arithmetic claim in every sentence is true, chains, √ and cut-off decimals ("√218 = 14.764…") included, and no fraction is printed; every figure and picture: each label states the length drawn, sits nearest its own segment, crosses no line, covers no point or number and touches no other label. Writes `dump.json`. |
| `verify.py` | The independent check: every question read back from what a student sees — words, choices, the figure's labels — and worked again exactly in sympy; every key, worked line, rounding sentence ("the hundredths digit is 4, so the tenths digit stays") and Hint step compared; the unit's bounds checked from the words; the test's sections, kinds of question and points matched. |
| `plant_check.py` | 31 planted errors (a key off by one, a tenth cut off, a side left out of the perimeter, a mislabelled figure, a copy drawn to the wrong size, a wrong hundredths digit, a wrong cut-off decimal, a Hint across zero off by one, a fraction in a reason, the clean rule weakened, "Almost" marked right, a follow-through gone wrong, a garden 1 m wide, a grown-up 4 ft tall, a mirror whose words drop "similar", …): the checks must catch every one. |
