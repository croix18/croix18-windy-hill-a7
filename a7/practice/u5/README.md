# A7 Unit 5 practice test (student page)

The Unit 5 practice page on the shared kit (`../kit/`). Ruling 55 (Croix, 25 Oct 2026: *"Yes I still want the interactive
practice page on all the units regardless of review day or not."*): A7 Unit 5 has no review day (ruling 27a — its review goes
home on paper Tue 3 Nov), and it was built before ruling 49, so its test is the printed **Form A and Form B** (Thu 5 Nov
2026). This page is practice for them, in the practice form's shapes and order (`a7/build/u5/unit.py`), with the test's
points (MA.7.GR.1.5 10, MA.7.AR.3.3 8, MA.7.AR.4.5 6) — never their numbers.

## What it is
Nineteen questions, 24 points (one point per lettered part), in the test's three named sections (ruling 54):
1. **Scale Drawings and Scale Factors** — Q1 a scale factor from one pair of sides, the copy bigger; Q2 the copy smaller (k in
   quarters or fifths, as the forms' 2.5, 1.5, 0.4, 0.25); Q3 select all that is true of a copy at scale factor k (sides and
   perimeter × k, area × k², the angles unchanged); Q4 a rectangle scaled by k, (a) the copy's perimeter, (b) its area; Q5 k
   from two areas (a perfect-square ratio); Q6 a floor plan, (a) the real length of one wall, (b) the room's real area — the
   scale per 1 inch (1 in : 5 ft) or a fraction of an inch (¼ in : 1 ft, ½ in : 3 ft); Q7 a real wall drawn on a plan; Q8 a
   plan's real area (the practice form's bare version of transfer item 1, in square feet).
2. **Converting Across Systems** — Q9 inches to centimeters; Q10 select the two expressions that convert (any pair of the FAST
   sheet's lines, either way); Q11 yards to centimeters through feet and inches; Q12 kilograms to pounds or pounds to
   kilograms (Form A asks one, Form B the other); Q13 gallons to liters; Q14 the closest area in a square unit across systems;
   Q15 an exchange rate printed and dated on the question, (a) dollars to the currency, (b) back.
3. **Multi-Step Proportion Problems** — Q16 (a) miles on a full tank, (b) tanks for a trip, part of a tank counted as a tank;
   Q17 a recipe, (a) the amount for new servings, (b) the servings from what is on hand; Q18 a three-part mixture's whole from
   one part; Q19 two speeds in two units, which is faster (the practice form's bare version of transfer item 2). On paper
   Q19 is written; here it is a choice of four sentences, each with its own conversion — the right one, comparing the numbers
   as they stand, dividing by 1.61, and converting the km/h the wrong way — and in half the sets the bigger number is the
   slower one.
- **Every conversion ratio is the FAST reference sheet's** (the unit's outline, decision 1), printed on the question; the words
  are the test's (the abbreviations as the paper prints them).
- **The test's numbers are not on the page** (the kit's rule of 24 Oct 2026). The page never draws a question of Form A or
  Form B — nor the test's rectangles at any scale factor, nor its transfer items' room and speeds — and holds them only as
  hashes (`engine.js` `FORMS_H`); `test_forms.js` has them, for the checks alone, and the kit refuses to build a page that
  holds it.
- **Ruling 43:** never the numbers a lesson showed — 5.01–5.10's warm-ups, notes, worked examples and Your Turns, and the worked
  numbers of the unit's reference sheet (`engine.js` `SHOWN_SRC`, each with where it comes from). **Nor the take-home papers:**
  no set repeats a question of the practice test or of the review (`HOME_SRC`), so every question is new.

## How answers are typed, and how they are read
- **Just the number;** its unit is beside the box ("k =" before it on Q1, Q2 and Q5; "$" on Q15(b)). The unit typed too is
  fine (`150 ft²`, `150 ft^2`, `150 sq ft`, `6 cups of rice`), as are `k = 2.5`, `$50`, `about …`, commas between thousands,
  a fraction (`5/2`), a mixed number with a space (`3 3/4`), ¾ and the other Unicode fractions.
- **Almost** (right, not finished): the key rounded — every answer here comes out exactly (2.54 is exact; money to the cent);
  a fraction not in simplest form; arithmetic left undone. A mixed number with no space (`33/4` for 3¾) or with a hyphen is not
  counted: "Did you mean 3 3/4?"
- **The sheet's other ratio is right, with a note** (the reference sheet: "Both directions are on the sheet, and both are
  accepted."): 7 ÷ 0.39 ≈ 17.95 on Q9, and the same on Q11–Q13, as the forms' keys give it.
- **Follow-through** (ruling 19; the test's 6(b) and 16(b)): the right step done to the student's own wrong part (a) is "your
  method is right — fix part (a) first" while practising, and earns the point in *Like the real test*, as on paper.
- **The coach** names each modelled mistake ("That is what you get if you multiplied the plan's area by the rate once…"):
  copy ÷ original the wrong way, adding, the area × k, the area ratio taken for k, the scale not read per 1 inch, the ratio the
  wrong way round (the estimate catches it), a chain stopped early, the square unit with the ratio once, the rate multiplied
  both ways, a part of a tank not counted, k not found from the yields, one part of a mixture for the whole. Hints are one small
  step at a time; no part (b) Hint asks for part (a)'s number (the M7 Unit 9 review); Show me how is the worked solution,
  every line equal to the answer.

## Checks (Rule 0) — `python3 ../kit/check/run.py .` runs them all, then builds
```
node u5_check.js 3000 1500    # 3,000 sets: every question read back from its printed words, ALL SOUND
python3 verify.py             # independent sympy oracle over dump.json, the forms and the lessons
python3 plant_check.py        # planted errors: every one caught
```
`u5_check.js` reads every question back **from the text the page prints** with its own reader and works the key out again;
checks the shape of the test against `build/u5/unit.py`; types every key back several ways and it must be right; the key
rounded, unsimplified and unfinished must be *Almost*; a mixed number run together must be "Did you mean"; the other ratio
must be right with its note; every modelled mistake typed must be wrong and named by its own words; near misses and the minus
sign never right; follow-through recognised, and right in test mode; the clean rule (no mistake, printed number or other part
is an answer); every worked line equal to the answer; every Hint choice one right option with a reason for each wrong one, no
Hint states its own answer, and no part (b) Hint asks for part (a)'s number; every arithmetic claim anywhere recomputed
(chains, ≈ to its places, comparisons); every choice keyed by its own math, every select-all subset tried. `verify.py` reads it
all again in sympy from what a student sees; checks every printed ratio is the FAST sheet's; reads Form A, Form B, the
practice test and the review out of `unit.py` with the same reader — `test_forms.js` must be exactly the forms, its reader
must agree with every answer on the forms' keys, and no set may draw any of them; and reads **what the lessons showed out of
the lesson specs themselves** (`build/u5/l*.py`: the warm-ups, notes, examples, Your Turns, their figures and check tuples,
and the reference sheet), as the page's own keys — independent of the engine's list (the M7 Unit 9 review asked for exactly
this) — and fails any set that asks one. Its fixed text (notes and messages) holds no test answer. Then the kit's lock (sets
1–300), variety (100 versions a part; Q3, a value of k alone, is allowed at 11 with its reason in `unit.json`) and browser
checks. The teacher copy (`teacher/`) prints Form A and Form B from `unit.py`.

`contentVersion` 1. Bump it in `unit.js` if any set's questions change after students have used the page.
