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
the equation on its own line, "What value of n makes the equation true?", and a box that already says "n =". Every stem is
in the words of the paper's own question since its review pass (below, "14 Nov 2026, evening").

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
9. Is (x, y) a solution of the system? Four options, each a verdict with a claim about THIS pair: "Yes — it makes both
   equations true", "No — it makes only y = … true" (once for each equation), "No — it makes neither equation true". The four
   claims are the four ways a pair can sit, so exactly one option is true for every pair; the pair is the solution, on one
   line only, or (about one set in seven) on neither.
10. The graph of two lines that intersect at a grid point inside the window: how many solutions (a choice). A horizontal line
    (y = 4) is one of the two in about one set in six.
11. Parallel lines, or one line for both equations written two ways (y = a(x + c) + d and y = ax + b; the stem says both
    graph as the one line shown) — Florida's same-line case: none or infinitely many.
12. The solution read from the graph (whole-number point of intersection, negative coordinates allowed; ½ may multiply x; a
    horizontal line about one set in six).
13. Two tables of values (x = 0…5): (a) the value missing from the first, (b) the solution — the one column where both agree.
14. (a) A story (one saves and one spends; two savers; two plants) with its graph, axes named and scaled by 5 or 10 (2 or 5 cm):
    when the two are equal and what both are, whole numbers on grid lines; (b) **its own graph**, a second system (widened 15 Nov 2026, below) whose
    point of intersection has thirds-, fifths-, sixths- or sevenths-type coordinates, in any quadrant, estimated to the nearest
    tenth: right when x and y are each **within 0.1** of the exact point (the lead's change of 14 Nov;
    audit E15), so no grid or half-grid point is ever inside the accepted range, nor the swapped pair; the half lines are drawn
    pale.

**Figures** (`fig.js`): every line is drawn from its own m and b and clipped to the window; the first solid, the second dashed
and teal, told apart without colour, with a legend; a grid square at least 14 px at 390 px; axis numbers every 1 or 2. The
`<svg>` carries its window and scale, so the checks read every line back onto its equation.

## 15 Nov 2026 — two boxes wherever a part asks for two numbers

The kit took one box a part, so question 12 (the paper: "Give its x and its y") took the ordered pair in one box. Since the kit's
several boxes in one part (`../kit/README.md`, "15 Nov 2026 — several boxes in a part"), every part whose answer is two numbers
has two boxes, and is still one point:

| part | boxes | right when |
|---|---|---|
| 12, the solution read from the graph | `x =` ▢ `y =` ▢ | both are the crossing |
| 13(b), the solution from the two tables | `x =` ▢ `y =` ▢ | both are the column where the tables agree |
| 14(a), the story | after ▢ weeks · $ ▢ each (plants: ▢ cm tall) | both are the crossing |
| 14(b), the estimate | `x ≈` ▢ `y ≈` ▢ | each within 0.1 of the crossing rounded to the tenth, inclusive (unchanged) |

- `unit.js`: `view.boxes` gives them (`twoBox`: every `pair` or `story` part); `keyText` one string per box; `view.form` only
  14(b)'s "each to the nearest tenth"; `view.key` and `choices` stay whole ("(4, −2)", "After 5 weeks; $40 each"), so the keys,
  the teacher copy and the all-multiple-choice paper print as before. The keypad lost its ( ) and , keys (no box takes a pair).
  The screen's note "Type an ordered pair like (4, −2)" is gone (no box takes one), and so is the printed note "Write an ordered
  pair as (x, y): x first, then y." (the lead, for Croix's "words on a page": a student writing by hand needs no rule for writing a
  point, and question 12 says "Give its x and its y"), so the printed directions are the teacher copy's two sentences only.
- Question 12's stem now ends with the paper's own "Give its x and its y." (the lock rewritten at contentVersion 1, below).
- `coach.js` `readBoxes` reads each box with the unit's own reader: a box may carry its own letter ("x = 4") or unit ("5 weeks",
  "$40", "12 cm tall"), never the other box's ("The x box takes the x. Put the x in the x box and the y in the y box."); two numbers
  in one box are said, not read as a pair. The named mistakes that depend on both boxes: the coordinates swapped ("The x box takes
  how far across, 4, and the y box how far up or down, −2"; for 13(b) the column and what both tables give there; 14(a) "swapped the
  two boxes"); the point where one line meets an axis; the nearest grid point. One box right and the other wrong says which ("Your
  x is right, but look again at the y. …"; 14(a) "The weeks are right. Now the amount: …" — it no longer reads the amount out).
- `help.js`: Hints 1 and 2 of the four families say which box takes what; Hint 3 ends with what to type in each box; the
  walkthrough's x and y (weeks and amount) steps say which box the number goes in.
- Checks: `u11_check.js` types every key, form and named mistake box by box, the labels, empty and mixed-up boxes (never a try),
  one box right; `verify.py` judges again every answer the dump typed box by box (2,600 a run) and each part's labels and box
  keys; `mc_check.js` holds the box keys to the whole key and the choices whole; `plant_check.py` plants ten box errors (below).

**The coach** names the unit's mistakes: the number in front distributed to the first term only (and the second only, for a
decimal); the sign of a negative multiplier lost; the like term left out or added the wrong way; the x-terms added instead of
taken from both sides; the number added undone the wrong way; stopping before dividing; dividing the fee by one price; a = a
read as no solution or as x = 0, x = 0 read as no solution; one equation true taken as enough; the coordinates swapped; the
point where one line meets the y- or x-axis; the column where two tables are only close; the nearest grid point for an estimate.
No false equation is printed as a line of work: "14 = −14 — never true" is an ending said in words. Multiplication is written
with parentheses or a dot, never × (no Hint either: the kit's arithmetic hints have × turned into ·). No "slope", no
"y-intercept": "the number multiplying x", "point of intersection".

## 15 Nov 2026 — the help, to the kit's help standard (`help.js`)

Croix, 14 Nov: students do not understand some explanations; every one gone through "with a fine comb", in the lessons'
vocabulary, with visuals where they help ("I want this helper to be absolutely phenomenal"). `help.js` (loaded before
`coach.js`, which applies it at its end, as Unit 6 does; `unit.js` asks it first through `rungs`) writes, for all 16 families
of the 14 questions, Hint 1 (two or three sentences and a picture), Hint 2 (the first move and its **Why:**), Hint 3 (one move a
line: Do, Why, the resulting line — the coach's own mathematics — ending with a check), the walkthrough (one question a step,
options shuffled, each wrong option's reason naming its misconception) and the named mistakes in the pattern "That is what you
get if you … . <the idea it broke and the fix>".
- **The lessons' words, every one tappable** (definition on a tap only, Croix 14 Nov): like terms, coefficient, constant,
  Distributive Property, variable term, the Addition / Subtraction / Division Property of Equality, no solution, infinitely
  many solutions, solution of a system, ordered pair, intersect, point of intersection, parallel lines, the same line, table
  of values, coefficient of x, approximate solution, nearest tenth. No "slope", no "y-intercept"; no substitution, no
  elimination; multiplication is parentheses or a dot.
- **Distribute first, always** (Croix, 14 Nov): every equation with parentheses (Q1, Q3, Q4, Q5, Q6) is taught distribute →
  collect → the smaller variable term from both sides → undo the constant → divide → check. The walkthrough's first move is
  "Distribute", and dividing first is a wrong option with its reason. `u11_check.js` fails a set whose Hint 2, first worked
  line or first walkthrough move is not "Distribute", or divides first.
- **The one "why" question** is the unit's key idea, the Distributive Property ("Why does the ⅔ multiply the −3 too?"),
  right after the distributing, in every family that distributes.
- **The pictures** (`fig.js`, drawn as the kit's `explain.js` draws, readable at 390 px light and dark): arrows from the number
  in front to each term inside (Hint 1, then with the products in Hint 2: the lessons' hand-drawn arrows); the kit's balance
  for the first move done to both sides (Hint 1 of Q2, Hint 2 of Q2, the first both-sides line of Hint 3); the kit's tape
  diagram for Q7's two plans; three small planes (cross once / never meet / one line) for Q10–11; the question's own graph
  redrawn with the point of intersection marked and dotted paths to the axes (Q10, Q12, Q14(a), and Q13(b) from its tables);
  the pair's point on the two lines (Q9); parallel lines with "3 apart" marked (Q11); the same table of values for both
  equations (Q11, one line); a table of values with its column boxed, beside its line (Q13); one grid square zoomed and cut
  into tenths (Q14(b)).
- `python3 ../kit/check/run.py .` now runs the kit's `check/help.js` (300 sets: terms, Why lines, pictures, Hint 1's length)
  and `check/help_page.js` (every help picture at 390 px, light and dark: width, label size, contrast).
- `node show_set.js 4821` still prints a set with all its help.

## Q14(b), widened (15 Nov 2026; ruling 49)

It had 38 different systems — under Croix's floor of 100 versions a part; the kit's variety check passed only because it counts
14(b) together with its story. The numbers multiplying x are now any of 1, 2, 3, ½, 3/2, 5/2 and their negatives (two
different), the numbers added −3 to 5 and −3 to 7, and the crossing may sit in any quadrant, at least half a unit from both
axes, inside a window that holds the origin and a unit or more on every side of the crossing. The lead's rules are unchanged:
the key is the crossing rounded to the tenth; right within 0.1 of it in each coordinate, inclusive; each rounded coordinate at
least 0.2 from every grid and half-grid line; never a rounding tie; x and y at least 0.5 apart. About 900 different systems
in 3,000 sets. `u11_check.js` and `verify.py` now count 14(b)'s systems on their own: at least 100 in a run of 1,000 sets or
more, at least 80% of the sets in a shorter run (plant_check's); a plant narrows it back and is caught. A crossing with fifths
falls exactly on a tenth (−4/5 = −0.8): its help says so instead of "close, not equal".

## 14 Nov 2026, evening — re-synced to the reviewed paper

The lead's review pass changed `a7/build/u11/l01–l08.py` and the practice paper in `unit.py` (14 questions, 18 points, 9 / 2 /
2 / 5, unchanged in kind and points). What did not match, and what changed here:
- **The words.** The paper is now in FAST's house style. Q1–4 "What value of n makes the equation true?" (was "What is the
  value of n?"); Q5 "Each equation has one solution, no solution or infinitely many solutions. Which? If it has one solution,
  find it."; Q6 "Complete the equation so that it has no solution. What number goes in the box?" with the equation on its own
  line; Q7 "After how many … will … have cost the same?" in every story; Q8 "Select all the systems that have (a, b) as a
  solution." (was "Select ALL the systems of equations …"); Q9 "Is (a, b) a solution of the system y = … and y = …?"; Q10–11
  "The graphs of the system y = … and y = … are shown."; Q12 "A system of equations is graphed: y = … and y = …."; Q13 "The
  tables are for y = … and y = …."; Q14 the story alone, then (a) "The PART (a) graph shows …" and (b) "The PART (b) graph
  shows a different system, y = … and y = …. Estimate its point of intersection to the nearest tenth.", each graph captioned
  as the paper's ("PART (a): Mia and Leo", "PART (b): a different system"; `fig.js` takes a `title`).
- **Q9's arguable key, gone.** "Yes — it makes the first equation true" was counted wrong beside a pair that IS the solution,
  though every word of it was true. Now every option states a checkable claim, and `u11_check.js` and `verify.py` each judge
  every option of every Q9 against the two equations: exactly one is true (claim and verdict), and it is the key; the four
  options are the four claims, and the two "only" options name the two equations. Planted: the old option put back; the key
  moved to the other equation's claim; a "neither" pair put on a line.
- **The sign help.** "Lost a minus sign along the way" said only "put your answer back in". When a typed answer is the
  negative of the key, the help now names the places in THAT equation's work where a sign goes missing, each with its own
  numbers and its right value: the negative distributed ("where the −⅔ multiplies the −3, (−⅔)(−3) = 2"), the like terms
  collected, the term moved across the equals sign ("where the + 22 moves across the equals sign (22 taken from both sides),
  2 − 22 = −20"), the division — at most three, in the order the work meets them. An equation whose work has no negative at
  all says so. Every value is read by the claims check; `u11_check.js` also holds that a "no negative" help is only given
  where no minus sign is printed. Planted: the division's value given the wrong sign.
- **The claims check read more.** A claim that ended its sentence ("… and 8 + 17 = 25.") was skipped: its full stop was
  read as a decimal point. A full stop followed by a space or the end is now a sentence break, so those are read too (about
  270,000 claims a run became about 360,000, every one true); an ending quoted as "What is left is 38 = −4" is judged in words.
- **Q14(b), the lead's ruling (follows the paper):** the key is the crossing rounded to the tenth; right when each coordinate is within 0.1 of that key, inclusive; each rounded coordinate is at least 0.2 from every grid and half-grid line and the crossing is never a rounding tie, so no printed grid point is in the range (`verify.py` asserts it; planted).
- **The marked constant** in `u11_check.js` ("THE PAPER'S SHAPE AND WORDS") now holds each question's words: a phrase of the
  paper (which must still be in `unit.py`, or the check stops and names it) and the pattern the page's stem must match.
- **Ruling 43** re-emitted: `shown.js` now 644 equations, 251 systems, 531 stories (was 632, 192, 523).
- **The lock** rewritten at contentVersion 1 (the page has never been published or used): `sets.lock.json` and
  `teacher/sets.lock.json` deleted and written again by the kit's `lock.js` in `run.py`. Once the page is published, a change
  to any set needs `contentVersion` bumped in `unit.js` instead.

**After a lesson or the paper changes**, from `a7/practice/u11/`:
1. `python3 shown43.py --emit` (ruling 43 from the specs);
2. compare `unit.py`'s `_ar21` … `_ar43` with `node show_set.js 4821` (and a few more sets) question by question; change
   `engine.js` / `coach.js` and the marked constant in `u11_check.js` to match (`node u11_check.js 300 50` says which words
   no longer match);
3. `cd teacher && python3 gen_test.py && cd ..` (the help: `help.js`; read two sets with `node show_set.js <set>`);
4. if the page is unpublished, `rm sets.lock.json teacher/sets.lock.json`; otherwise bump `contentVersion` in `unit.js`;
5. `python3 ../kit/check/run.py .` and `python3 ../kit/check/run.py teacher` (each must end "ALL CHECKS PASSED"; the kit's
   page-by-page browser check has timed out once — run it again); both rebuild their HTML.

## Ruling 43

The page never asks an equation, a system or a story that a lesson (warm-ups, notes, examples and Your Turns, whiteboards,
independent sets, banks), the review, the reference sheet or the practice paper shows. `shown43.py` reads them out of the specs
themselves (`a7/build/u11/l01–l08.py`, `unit.py`): 644 equations (the sizes of the printed numbers and the ending), 251
systems, 531 stories (a string with money or a rate in it). `python3 shown43.py --emit` writes `shown.js`, which the engine steers by; `u11_check.js` holds every set
to `shown.js` from the printed words, and `verify.py` reads the specs again on its own. Re-run `--emit` whenever a lesson changes.

## Variety (ruling 49)

Every part has at least 100 versions over set numbers 1–20,000; nothing is allowed under the floor. Q14(b) clears it by itself
too (about 900 systems in 3,000 sets; above). The fewest are Q11 (1,242)
and Q10 (2,013) — their lines are drawn from small multipliers to stay readable on a phone — then Q14(a) (2,242).

## The checks (`python3 ../kit/check/run.py .` runs them, then the lock, the variety floor and the browser checks)

| | |
|---|---|
| `u11_check.js` | 3,000 sets read back from their printed words with its own polynomial reader and exact arithmetic: the shape of the test (titles and the tracker's points read from `unit.py`; a marked constant holds the kinds of question and each question's words, checked against `unit.py`); every equation solved; every key typed back in several forms; every named mistake typed, wrong and named; every worked line an equation with the first one's solutions; every Hint number step's arithmetic, no Hint stating its answer, one right option per Hint choice with a reason for each wrong one; every arithmetic claim in every sentence (≈ 360,000); Q8's pair in all ten equations; every Q9 option's verdict and claim judged against both equations, exactly one true; the sign help's places; every graph's lines, window, crossing and axis numbers read back from the SVG; every table value; Q14(b)'s tolerance; no ×, "slope" or "intercept" anywhere; ruling 43 against `shown.js`. Writes `dump.json`. |
| `verify.py` | The sympy oracle over the rendered HTML of 1,500 sets: every equation, box, story, pair, system, graph line, table and estimate worked again; every worked line and Hint step; every paper choice; ruling 43 from the specs; the test's sections and points. |
| `plant_check.py` | 63 planted errors (15 Nov, the two boxes: read the other way round, one box right accepted, one estimate box within 0.1 enough, the x box taking the y's letter, the weeks box taking dollars, an empty box a try, Q14(b)'s ≈ shown as =, Q14(a)'s boxes in the other order, Q13(b) without boxes, one key string for two boxes — and "the pair reader swaps x and y" retired, as no box takes a pair; since 15 Nov: the help's Distribute line wrong, a Hint step's ×, its walkthrough dividing first, Hint 2 not distributing, a Why's arithmetic wrong, "slopes" in Hint 1, Q14(b) narrowed), and before it (Q9's old arguable option, Q9 keyed to the other equation, a "neither" pair on a line, the sign help's value wrong, the old question words, Q14(b) uncaptioned, wrong keys in every question, a printed sign, a fraction's reciprocal, a decimal off the list, Q8's key and clean rule weakened together, a tolerance of 0.2, a crossing on a half line, a line drawn a unit high, a dashed line drawn solid, the axis numbered a step off, a grid too small, the worked lines distributing to one term, a Hint stating its answer, ×, "slopes", a mistake marked right, the paper offering the key as a wrong answer …): every one must be caught. |
| `mc_check.js` | 3,000 sets: three wrong answers for every typed part, in the key's shape, never the key, never inside an estimate's tolerance, each a named mistake or (counted) a value one away. |
| `show_set.js` | not a check: `node show_set.js 4821` prints one set with all its help, for reading it as a student does. |
