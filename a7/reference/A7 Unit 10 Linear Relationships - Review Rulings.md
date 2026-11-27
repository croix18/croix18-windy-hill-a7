# A7 Unit 10 — rulings on the review of the built unit (27 Nov 2026)

The lead read the three readers (critic, barton, fast), the six blind solvers' doubts and the two blind-diff tables,
then looked at every deck, every paper and every handout, and measured every picture on the built pages.
**No key was wrong** (413 questions solved blind; every DIFFER row was wording or format). What follows is
everything that changes. Each fixer applies ITS section exactly as written, and "Holds for every section", and
nothing else.

Ids are `reader_copy.py`'s: `10.04/B6` is board 6, `N2` Notes II, `E1`/`YT1` an Example and its Your Turn, `I3` the
Independent Set's question 3, `K7`/`A7` question 7 of the Question Bank / the Additional Question Bank, `W4` warm-up
question 4, `P/Q8a` the Practice Test, `R/Q9` the Review. `s05` is slide 5 of the deck as it is built now.

## Holds for every section

**Numbers and keys**
- A changed number changes its `check` (written from the mathematics), its steps, its `why`, its named errors and
  its figure. Every wrong option stays one named error with its cite, and a cite names a line that exists.
- Use the numbers a ruling gives. Where a ruling leaves a choice to you, say in your hand-back what you chose.
- A story or a number you change may be named elsewhere in your file (a `note`, a `why`, the Lesson Plan's
  sentences, the cut for the short day, `qtext`): grep for it and change every mention.
- Keep off every lesson (reserved for the paper): a water tank that drains, a candle, pizza toppings, a tree's
  height, a van rental, Dana's savings; y = 1.5x; y = 2x + 2; y = 2.5x + 4; y = −(3/4)x + 2 as a line to draw;
  c = 1.75t + 9.50; the points (−2, 7) with (4, −5); (0, −4) with (3, 1); (5, 1) with (10, 4); (2, 110) with (5, 185).
- Do not add a `repeat_ok`, and do not remove one, unless a ruling's new numbers make the gate ask: then the comment
  says exactly which digits coincide. Do not run `shuffle_choices.py`: every keyed letter stays where it is.
- Do not edit `u10/figs10.py`. If a picture cannot be made with it, say so in your hand-back.

**One way of saying each thing** (where your file says it another way, change it to this)
- "The rate is the slope, and the start is the y-intercept." (never the start first)
- A table has pairs: "no pair for x = 0", "the first pair" (not "row", not "column").
- "Go back to x = 0 at the rate of change." (not "step back", not "back 5 units" as a heading)
- "the coefficient of x" (not "the number with x", not "the number that multiplies x")
- "An amount that goes down has a negative slope." (the one sentence for a negative slope in a context)
- Money has two decimals when it has cents: \$2.50, \$5.50, 14.50 in a worked line.

**The question is the bold line.** On every Example, Your Turn and board the givens are the prompt and the question
itself is the `ask` (bold), as on the Example's own slide. Six Your Turns have no bold line; each is named below.

**Pictures on slides** (measured on the BUILT slide; `python3 /home/claude/lean/u10/slidefigs.py
"out/u10/<your deck>.pptx"` prints every picture's lettering and every plane's size, grid edge to grid edge, and
marks what falls short)
- Lettering 18 pt (the tool reads an 18-pt label as about 17.5; it flags under 16, and under 14.5 on a reveal
  slide). A picture that only fits by being made smaller whole has too much on its slide: give it room.
- A coordinate plane a student reads: longer side at least 2.2 in, shorter side at least 1.3 in; aim for 2.6 in
  where the slide has the room, and a Your Turn's graph is no smaller than its Example's. On a Notes slide or a
  reveal slide the floor is 2.0 in. A row of four graphs: each plane at least 1.4 in wide and 1.8 in tall.
- The numbers along an axis never touch one another (number every second line where the squares are small), and a
  point's name never sits on an axis, on an axis's name, on a number or on a line.
- Nothing on a slide is within 0.15 in of the footer rule. (The tool measures pictures; a line of text at the footer
  you find by looking.)
- Room comes from the layout: fewer lines under a picture, a name keyed on its line instead of stacked over the
  plane, `aspect` for a tall or a flat window, a larger `inches`. It never comes from smaller lettering.

**Pictures on paper** (`python3 /home/claude/lean/u10/paperfigs.py u10/lNN.py` prints every printed picture's
lettering and the size of its squares)
- Lettering 8 to 11.5 pt. A plane's squares: 0.24 to 0.31 in on the Independent Set, 0.21 to 0.35 in in the banks.
  A grid's `inches` follows from its window: about 0.27 in for each column plus the room its numbers take.

**Every picture draws at every size.** After your last change run `python3 figure_sheets.py u10 --out
$HOME/figsheets` and read `items.txt`: no item of your file may say `COULD NOT DRAW`. (Two do now: a dot on a
numbered tick of the y-axis is struck by the tick's number when the picture is drawn small.)

**Look at every slide of your deck that carries a picture — not only the ones you changed** — at reading size:
`python3 /home/claude/lean/u10/mosaic.py $HOME/look.png 2 "out/u10/<deck>.pdf:5,6,7,8,9,10"` (six slides to a
picture, each 800 pixels wide), and at every page of the Independent Set and of each bank that carries a picture
(`python3 contact_sheet.py "<pdf>" 70 3`). You are looking for what no gate sees: a name printed across an axis,
numbers run together, a tiny plane on an empty slide, a line of text on the footer rule, a table whose numbers are
smaller than its neighbour's. Fix what you find, say what you fixed, and look again at that slide.

---

## Section 10.01 — `u10/l01.py`

1. **N1 (s05)** — the graph is 1.2 in tall (`aspect=0.25` flattened it). Make its plane at least 2.0 in tall, the y-axis
   still numbered by 4; the two tables and the three captions stay as they are.
2. **N2 (s06)** — the two-lines graph is the lesson's picture and its plane is 1.0 by 1.5 in. Take the three stacked
   title lines off the top of it: key each equation on its own line in the line's colour (y = 2x; y = 2x + 3) and
   keep the dot at (0, 3). The plane at least 2.2 in tall. The curve keeps its title "a curve: not linear" and is at
   least 1.4 in tall. The two sentences under the picture stay, and they stay clear of the footer rule.
3. **B5 (s24)** — the four planes are 1.1 in wide. Draw them with square cells (drop `aspect=1.4`) so each is at
   least 1.4 in wide and 1.8 in tall; the same change for the reveal's graph if it is drawn from the same dict.
4. **K9** — it is the Practice Test's question 1 relationship asked the same way. Make the pairs (3, 14) and
   (7, 26): "5; no" ((26 − 14) ÷ (7 − 3) = 3 and 14 − 3(3) = 5).
5. **K9 and A9's heading** — "Find the missing number." stands over a question with no missing number. Make both
   headings "Use the two pairs."
6. Not taken: B5, K11 and A11 keep two wrong graphs that are linear and not proportional (a drawn line through
   (0, 3), and dots with a constant rate): the two errors are named apart, and the paper's question 3 is built the
   same way.

## Section 10.02+03 — `u10/l02.py`

1. **E1 (s08, s09)** — the name "(−2, 5)" is printed across the y-axis and under its "y". Place it clear (below
   left of its point is free). Look at "(2, −1)" too.
2. **E1 worked (s09) and YT1 reveal (s11)** — the slope triangle numbers its rise and not its run. Number both
   sides: 6 and 4 on E1's, 8 and 6 on YT1's (Notes I's triangle names both).
3. **YT1** — no bold line. Prompt: "The line passes through (−3, 6) and (3, −2)." Ask: "Find the slope of the
   line." (Example 1's own two lines.)
4. **N1 (s05)** — its last line sits on the footer rule. Give it 0.15 in: a slightly shorter plane is enough (the
   plane stays at least 2.0 in tall).
5. **N2** — one line added under the line that is there, so that a missing side is taught before board 6 and
   Independent Set 5 ask for one: "On this line a run of 6 has a rise of 3, and a rise of 5 has a run of 10: the
   slope stays $\frac{1}{2}$."
6. **B4 (s22, s23)** — the picture's lettering reads 15 pt: it was made smaller whole. Give it its 18 pt.
7. **K9** — it is Independent Set 5's triangle (rise 2, run 4). Make it "A slope triangle on a line has a rise of 3
   and a run of 4. A larger slope triangle on the same line has a run of 16. What is its rise?" → 12.
8. Not taken: boards 8 of this lesson, of 10.05 and of 10.09 ask a number backwards before a slide shows how. Board 8
   is each lesson's backwards question and its reveal is where the step is shown, as in Units 7 and 11.

## Section 10.04 — `u10/l04.py`

1. **N1** — one line added after "300 feet per hour: the climber gains 300 feet every hour.", so that the bank's
   "start from a point we know" has a model that is not on a board the short day cuts:
   "From 3 hours to 5 hours: 2 · 300 = 600 more feet, so 3,500 feet at 5 hours."
   It must be one line and the slide must keep 0.15 in over the footer rule; if it cannot, say so and leave N1.
2. **N2 (s05)** — the head becomes "An amount that goes down has a negative slope". The third line, "A negative
   slope goes down as you move right.", comes off (it is 10.05's sentence, and it put the text on the footer rule).
   With the room, the plane at least 2.2 in tall.
3. **YT1 (s08, s09)** — the plane is 1.9 by 1.4 in on a slide that is half empty, smaller than Example 1's. Make it
   at least 2.4 in on its longer side on both slides.
4. **B3 (s18, s19)** — the elevator's plane is 2.1 by 1.1 in. At least 2.6 in wide and 1.5 in tall on the question
   slide (`aspect` makes its four rows taller), and no smaller than 2.2 by 1.3 in on the reveal.
5. **B4** — "15 cups after 4 batches and 33 after 10" has 3 cups used before any batch. A stack of cups has a start
   that is real: "A stack of 4 cups is 15 centimeters tall, and a stack of 10 cups is 33 centimeters tall." Ask:
   "Find the rate of change, with its unit." Steps: "Change in height: $33 - 15 = 18$" · "Change in cups:
   $10 - 4 = 6$" · "Rate: $18 \div 6 = 3$". Answer: "3 centimeters per cup". (The critic's 12 and 30 are not taken:
   a student who divides one pair would then be right, which is the error Notes I warns against.)
6. **B5 option D, K9 option A, A9 option D** — a turned-over rate carries the turned-over unit:
   "$\frac{1}{13}$ hour per dollar", "$\frac{1}{7}$ ticket per dollar", "$\frac{1}{6}$ pound per dollar".
7. **K12** — its two facts contradict each other (18 feet per hour, yet 24 feet after 2 hours). "A crew paints a
   fence at a constant rate of 18 feet per hour. They have painted 36 feet after 2 hours. After how many hours will
   they have painted 108 feet?" → "After 6 hours". Why: (108 − 36) ÷ 18 = 4 more hours; 108 ÷ 18 = 6 agrees.
   **A12** the same way: "…14 square feet per hour. They have laid 28 square feet after 2 hours. After how many hours
   will they have laid 98 square feet?" → "After 7 hours".
8. **A4** — the hourglass graph cannot be drawn small (its dot sits on the tick "200") and its printed lettering
   reads 15 pt. Number the sand axis by 50 from 0 to 250, mark (1, 150) and (3, 50) and no point on the axis. The
   answer stays −50 grams per minute; why: (50 − 150) ÷ (3 − 1) = −100 ÷ 2 = −50. Lettering and squares as "Pictures
   on paper" says.
9. Not taken: the header already carries both benchmarks (`benchmarks=`); the title slide names the first.

## Section 10.05 — `u10/l05.py`

1. **N3 (s07)** — its lettering reads 16 pt (the picture was made smaller whole) and its last line is on the footer
   rule. Both planes at least 2.0 in tall with 18-pt lettering, each equation still named over its own plane, and
   the two sentences 0.15 in clear of the footer rule. Windows no taller than their lines need.
2. **YT1 and YT2** — no bold line. YT1: prompt "Handout, question 1:  $y = \frac{4}{3}x - 3$", ask "Graph the
   line." YT2: prompt "$y = 6 - \frac{5}{3}x$", ask "Graph the line." (Example 1's and Example 2's own shape.)
3. **B2** — "Slope: the coefficient of x, $m = 4$".
4. **B3** — the unit's y-intercept is a number; an option that calls a point "y-intercept (6, 0)" teaches the other.
   Options: A "Slope 6; passes through $(0, \frac{1}{2})$" · B "Slope $\frac{1}{2}$; passes through (0, 6)" (key) ·
   C "Slope 2; passes through (0, 6)" · D "Slope $\frac{1}{2}$; passes through (6, 0)". Answer: "B — Slope 1/2;
   passes through (0, 6)". Error D: "the y-intercept put on the x-axis".
5. **B4, K8, A8** — "move with the slope twice" does not say which way. "Start at the y-intercept and move with the
   slope twice, to the right. Which two points do you reach?"
6. **B5 Error B, K12 Error A, A12 Error C** (the sign of b dropped) carry the tag of the real exchange beside them.
   Their cite becomes "[Notes I: y = 2x − 3: b is −3]".
7. **B8** — the steps solve for a letter the question shows as a box. "Substitute (3, 10): $10 = 2(3) + □$" ·
   "Simplify: $10 = 6 + □$" · "Subtract 6 from both sides: $□ = 4$".
8. **K10** — it is Notes III's line again. Make it $y = 4 - \frac{1}{3}x$, and word K10 and A10's options as board
   3's are: K10 — A "Its slope is 4 and it passes through $(0, -\frac{1}{3})$." · B "Its slope is −3 and it passes
   through (0, 4)." · C "Its slope is $-\frac{1}{3}$ and it passes through (4, 0)." · D "Its slope is
   $-\frac{1}{3}$ and it passes through (0, 4)." (key). A10 keeps its line and its letters, with "passes through" for
   "crosses the y-axis at" in all four options.
9. **The handout (Independent Set).** Its four grids have squares from 0.22 to 0.34 in. Draw all four with squares
   of 0.24 to 0.31 in (question 4's window is the tall one). If the set then fits two pages, good; do not go under
   0.24 in to force it.
10. Not taken: the IXL list keeps N7D ("Compare linear functions"); the list is Croix's, and the lead has put the
    question to him.

## Section 10.06 — `u10/l06.py`

This deck's pictures are the unit's weakest: every Notes slide, both Your Turns and board 3 fall short.

1. **N1 (s04)** — lettering 12 pt, plane 1.9 by 1.8 in, last line on the footer rule. The three lines become two:
   "The line crosses the y-axis at 2 and goes down 2 for every 3 units to the right." and
   "Slope $-\frac{2}{3}$:   $y = -\frac{2}{3}x + 2$". The table's numbers 18 pt, the plane at least 2.2 in tall.
2. **N2 (s05)** — plane 1.2 by 1.0 in, lettering 15 pt, and its four lines stand at two different indents. One list,
   three lines: "A pool holds 200 gallons, and a hose adds 50 gallons every minute." · "The rate is the slope, and
   the start is the y-intercept." · "Choose scales that fit. A real-world graph starts at x = 0." The plane at least
   2.2 in tall, its three points named clear of the axis numbers.
3. **N3 (s06)** — plane 0.9 in wide with its axis numbers run together. At least 1.6 in wide and 2.2 in tall
   (`aspect` under 1 for the tall window), numbers that do not touch, the table's numbers 18 pt. The three lines
   stay.
4. **YT1 (s09, s10), the handout's question 1** — the y-axis numbers are printed on one another and "−1" runs into
   "0" on the x-axis. Question slide: the table's numbers 18 pt and the plane at least 3.0 in tall (the slide has
   the room), every square numbered as on the handout if the numbers then clear one another, every second square
   if not. Reveal: the plane at least 2.4 in tall, numbers clear, each point's name clear of the axis and of the
   other names.
5. **E2 (s11)** — the grid's plane is 1.8 in: at least 2.4 in. **YT2 (s13, s14)** — the grid at least 2.4 in on the
   question slide; on the reveal the lettering back to 18 pt (it reads 14), and "(0, 40)" clear of the number 40 and
   of the axis's name.
6. **B3 (s19, s20)** — the four graphs do not draw small, they name their axes x and y, and the stem leaves out a
   unit. Prompt: "A tub holds 10 gallons, and a faucet adds 5 gallons every minute." Ask: "Which graph shows the
   gallons in the tub versus the minutes?" (`qtext` to match.) Each of the four graphs names its axes "minutes" and
   "gallons". No dot on the gallons axis: each graph marks one point off the axes — A (2, 25), B (2, 10), C (1, 5),
   D (2, 20) — and the start is read where the line meets the axis. Each plane at least 1.4 in wide and 1.8 in
   tall. The reveal's graph at least 2.2 in tall with its lettering clear of the axis numbers; steps and answer
   stay. The options' errors stay as they are worded.
7. **B5 (s23)** — the question slide carries a table 0.7 in wide. The stem gives the pairs in words, so the
   question slide has no picture; the reveal keeps its table. Steps: "slope: $\frac{8 - 5}{2 - 1} = 3$" · "Go back to
   x = 0 at the rate of change: $5 - 3 = 2$". Error C, **K10** Error D and **A10** Error D cite Notes II, which is
   about descriptions: their cite becomes "[10.05 vocabulary: the y-intercept is the value of y when x is 0]".
8. **B9** — answer: "Lee exchanged the start and the rate: (0, 50) and (2, 90)."
9. **A6** — it is Independent Set 3's line and key picture. "A drone is 50 feet above the ground and rises 50 feet
   every minute. Graph its height versus time." → "The line from (0, 50) through (2, 150) to (6, 350)", on the grid
   it has.
10. **The handout and both banks: the printed grids.** Their squares run from 0.20 to 0.59 in and two are lettered
    at 13 and 15 pt (K7, K9; A9 at 12). Bring every one inside "Pictures on paper": I2, I3, I5; K4, K5, K7, K8, K9;
    A4, A7, A9 are outside it now. I2's table has cells half the size of I1's: give it I1's cells.
11. Not taken: I5, K8 and A8 keep 2x + y = 6, 3x + y = 9 and 2x + y = 10. Croix's IXL list puts "Graph a line from
    an equation in standard form" on this lesson, so the handout rehearses it once and each bank once; the Review
    and the test never ask it. The lead amends standing decision 10 to say so, and has put the question to Croix.

## Section 10.07+08 — `u10/l07.py`

1. **E1, YT1, E2, YT2 answer lines** — all four ask "explain what each means" and answer with two bare numbers. The
   answer line is the two sentences (standing decision 13); the worked lines carry the numbers with their units.
   - E1: rows "slope $= \frac{30 - 12}{4 - 0} = \frac{18}{4} = 4.5$" · "4.5 gallons per hour" · "y-intercept = 12
     gallons". Answer: "The barrel gains 4.5 gallons every hour. It held 12 gallons when the rain began."
   - YT1 (see 2): Answer: "The skater moves 5 meters farther from the wall every second and started 10 meters away."
   - E2: Answer: "The pool gains 250 gallons every hour. It held 600 gallons when the filling began."
   - YT2: steps "The slope: $\frac{26.50 - 14.50}{7 - 3} = \frac{12}{4} = 3$ dollars per mile" · "Solve for b:
     $14.50 = 3(3) + b$,  so  $b = 5.50$". Answer: "Each mile adds \$3. The ride costs \$5.50 before the first mile."
   An answer may take two lines; where the kit refuses three, shorten the sentence, not the meaning, and give the
   graph beside it the room that is left (a reveal's plane is at least 2.0 in).
2. **YT1 (s09, s10)** — slope and y-intercept are both 5, so a student who exchanges them is marked right; and the
   plane is 1.4 by 1.7 in. The line passes through (0, 10) and (4, 30), the meters axis counting by 5 to 35.
   Steps: "Slope: $\frac{30 - 10}{4 - 0} = 5$ meters per second" · "y-intercept: 10 meters". The plane at least
   2.4 in tall on both slides (no smaller than Example 1's on the question slide).
3. **N2** — head: "From a table with no pair for x = 0".
4. **B3** — money: "$c = 0.35n + 2.50$ … What does 2.50 mean?" (steps and errors to match).
5. **B5** — Errors A and B say "the first row": "the first pair".
6. **K7 and A7 option D** — B and D are one confusion seen from both sides. K7 D: "The generator runs out after 6
   hours." A7 D: "The boat runs out after 5 hours." Error: "the point where the line meets the x-axis read as the
   start".
7. **A1** — it is K4's line and 10.09's warm-up. "$c = 3n + 7$". **A3** — it is Independent Set 2's line.
   "$c = 45n + 25$" (the options keep 45). **A4** — it is Independent Set 1's line. Table: days 2, 4, 9; length 23,
   33, 58. Answer: "Slope 5, y-intercept 13: the vine was 13 centimeters long when the measuring began."
8. **A5** — the unit: "−5 degrees Fahrenheit per minute: the soup cools 5 degrees Fahrenheit every minute."
9. **A6** — slope and y-intercept are both 250. The line passes through (0, 500) and (2, 1,000). Answer: "Slope
   250: the machine fills 250 bottles every minute. y-intercept 500: it had filled 500 bottles when the timing
   began."

## Section 10.09 — `u10/l09.py`

1. **N1 (s04)** — the plane is 1.4 in tall: at least 2.0 in, the row of three results and the check under it clear
   of the footer rule.
2. **N3 (s06)** — its last line is on the footer rule. The sentence "Substitute a point and solve for b." moves
   into the head — "No y-intercept in sight: substitute a point and solve for b" — and the slide begins at "The line
   passes through (2, 3) and (6, 11)."
3. **E1** — prompt: "The table shows a linear relationship. It has no pair for x = 0." **K3, A3**: "The table has a
   pair for x = 0." **K4, A4**: "The table has no pair for x = 0."
4. **E2 worked** — a line between "$3 = -\frac{2}{3}(3) + b$" and "$b = 5$": "$3 = -2 + b$" (Your Turn 2 shows that
   step).
5. **YT1 and YT2** — no bold line. YT1: prompt "The table shows a linear relationship.", ask "Write its equation in
   slope-intercept form." YT2: prompt "A line passes through (−4, 7) and (2, −2).", ask "Write its equation in
   slope-intercept form."
6. **B8** — it is Independent Set 1's line through the same point. "The line $y = □x + 2$ passes through
   (3, −10)." Ask: "Find the missing number." Steps: "Substitute (3, −10): $-10 = □(3) + 2$" · "Subtract 2 from
   both sides: $-12 = □(3)$" · "Divide both sides by 3: $□ = -4$". Answer: −4.
7. **A7** — it is K7's line. "(−4, 2) and (4, −2)" → y = −(1/2)x.
8. **The handout.** Questions 1 and 2 are drawn at two scales (squares 0.34 and 0.20 in). Both between 0.24 and
   0.31 in.

## Section 10.10 — `u10/l10.py`

1. **YT1** — no bold line. Prompt, two lines as now; ask: "Write an equation for the cost c, in dollars, of a job of
   h hours."
2. **YT2 (s12, s13)** — lettering 12 pt, plane 2.0 by 1.5 in on a half-empty slide, and a blank line between the
   stem and the question. The plane at least 2.4 in on its longer side with 18-pt lettering, the blank line
   closed. The cups are n, not c (c is a cost on every other slide of this lesson): "Write an equation for the
   water w, in liters, after n cups." Steps: "The y-intercept: $b = 18$" · "The slope: $\frac{8 - 18}{40 - 0} =
   \frac{-10}{40} = -0.25$". Answer: "w = −0.25n + 18".
3. **B1** — boards 1 and 2 change two things at once (15 to 150, and the direction). B1: "A kayak club charges a
   \$150 membership plus \$10 for every hour." Ask: "Write an equation for the cost c, in dollars, of h hours."
   Steps: "The rate is the slope: $m = 10$" · "The start is the y-intercept: $b = 150$". Answer: "c = 10h + 150".
   B2 stays, and its answer gives both forms: "a = −10h + 150, or a = 150 − 10h".
4. **B3** — \$30 is the fee, not a rate: "A phone plan has a monthly fee of \$30 plus \$0.25 for every text."
5. **B8** — its first step writes the answer before finding it. "Substitute the ride: $13.50 = 1.5(6) + □$" ·
   "Multiply: $13.50 = 9 + □$" · "Subtract 9 from both sides: $□ = 4.50$".
6. **I1** — "Mini golf costs \$9 for a club plus \$4 for every round. Write an equation for the cost c, in dollars,
   of r rounds." **I3** and **I6**: "the cost c, in dollars, of h hours" / "the cost c, in dollars, of s sessions".
7. **I2, K2, A2** — the key gives both forms, as the paper does: "a = 80 − 4s  (a = −4s + 80 is the same answer)";
   "a = 35 − 0.25n  (a = −0.25n + 35 is the same answer)"; "a = 10 − 0.05n  (a = −0.05n + 10 is the same answer)".
8. **K5** — it is board 9's line. Table costs 55, 85, 95 (hours 2, 5, 6) → "c = 10h + 35".
9. **K8 and A8** say "The table shows" and have no table. K8: "A boat rental costs \$50 for 1 hour, \$85 for 2 hours
   and \$190 for 5 hours. Which equation gives the cost c, in dollars, for h hours?" A8: "A lawn service costs \$110
   for 1 hour, \$190 for 2 hours and \$350 for 4 hours. Which equation gives the cost c, in dollars, for h hours?"
10. **K11** — it is K6's line and nearly Notes I's gym. "A karate school charges a \$45 sign-up fee and \$20 every
    month. Sam writes c = 45n + 20. What is Sam's mistake? Write the correct equation." → "Sam exchanged the rate
    and the start. The equation is c = 20n + 45."
11. **A10 and A11** — A1, A10 and A11 are one line (3 and 20). A10: "The equation h = 2t + 30 gives the height h, in
    centimeters, of a sunflower t days after a gardener first measures it." (a) "What does 2 mean?" → "The sunflower
    grows 2 centimeters every day." (b) "What does 30 mean?" → "The sunflower was 30 centimeters tall when it was
    first measured." A11: "A climbing gym charges a \$15 entry fee and \$3 for every hour of gear rental. Leo writes
    c = 15h + 3." → "Leo exchanged the rate and the start. The equation is c = 3h + 15."
12. Not taken: the header already carries both benchmarks.

## Section papers — `u10/unit.py` (the Review, the Practice Test, the Reference Sheet)

The Practice Test does not change.

1. **R/Q2** — Error C ("a number subtracted") carries Error A's tag. Give it its own: "a number subtracted taken
   for proportional", with the cite it already has.
2. **R/Q6b** — the paper asks for a meaning as a four-option choice twice, and the Review never does. 6b becomes a
   choice with no number in it. Stem: "What does the slope tell you about the gift card?" A "How many dollars are
   added to the card every week" · B "How many dollars Ana spends from the card every week" (key) · C "How many
   dollars were on the card at the start" · D "How many weeks it takes Ana to spend \$1". Errors: A the sign
   ignored; C the slope read as the y-intercept; D the rate turned over. Part (a) keeps −45.
3. **R/Q10** — a quantity is never named m (standing decision 16). "The equation $c = 0.40t + 2.50$ gives the cost
   c, in dollars, of a scooter ride of t minutes." Nothing else changes.
4. **R/Q11** — the stem does not say that minute 0 is when the rise began: "…The table shows its depth below the
   surface, in meters, and the minutes since it began to rise."
5. **R/Q12a** — it is 10.07/K10 word for word. "What is 40 degrees Celsius in degrees Fahrenheit?" → "104 degrees
   Fahrenheit" (1.8(40) + 32 = 72 + 32).
6. **R/Q16** — parts b and c are one question ("y when x is 0" and "is that 0?"). Part c becomes "For which value
   of x is y equal to −1?" → 16. Why: from (12, 2), y goes down 3 more for 4 more in x; or −1 = −0.75x + 11, so
   0.75x = 12. The key's first line names the four parts: "(a) the slope (10.02–10.03), (b) y when x is 0 (10.01),
   (c) x for a given y (10.04), (d) the equation (10.09)".
7. **R/Q17** — it is 10.10/I6's story, x-values and letters. "A swim school charges a sign-up fee and the same
   amount for every lesson. The cost of 3 lessons is \$129, and the cost of 8 lessons is \$219. Write an equation
   for the cost c, in dollars, of n lessons." → "c = 18n + 75" (90 ÷ 5 = 18; 129 − 54 = 75).
8. **Reference Sheet** — five lines to the unit's one way of saying each: §1 "When the table has no pair for
   x = 0, go back to x = 0 at the rate of change."; §3 "An amount that goes down has a negative slope."; §4 "the
   coefficient of x"; §5 "From a description: the rate is the slope, and the start is the y-intercept."; §6 "When the
   table has no pair for x = 0, substitute a point and solve for b."
9. Not taken: a rule for follow-through credit on P/Q11(b) — how a point is marked is Croix's; the key says what
   earns it.

## After the fix pass (27 Nov 2026, the same day)

Nine fixers (Claude Opus 5.5), one file each, applied the sections above. Where a slide's room or the kit forced
another way, this is what stands:

- **A Your Turn whose picture is a graph keeps its question in its one line** (10.05 YT1 and YT2, 10.06 YT1,
  10.07 YT1). The kit sets a Your Turn's bold line over its picture, and under a prompt and a bold line those graphs
  fell to 1.0 to 1.3 in wide. 10.05: "Handout, question 1:  Graph y = (4/3)x − 3." and "Graph y = 6 − (5/3)x.",
  the planes as they were. 10.06 YT1: "Handout, question 1:  complete the table and graph y = 2x − 5." 10.07 YT1:
  "A skater's distance from a wall:  explain the slope and the y-intercept.", its line through (0, 15) and (4, 35)
  on axes named seconds and meters, the meters axis counting by 5 and numbered by 10, so neither dot sits on a
  number.
- **10.01** — Notes III's arithmetic is plain text ("First:  2 for every 1 unit.   9 − 2 − 2 = 5:  not
  proportional."): a text line takes no mathematics.
- **10.02** — Your Turn 1 keeps its bold line; its plane is 2.5 by 2.1 in, above the floor.
- **10.04** — board 3's answer keeps its period: "B — Down 15 feet every second."
- **10.05** — Notes III's two planes start at y = −1, so the x-axis lies inside each grid; with the left plane
  starting at 0, its "x" sat after its last number and read "3x". Boards 1 and 7 (the sign of b dropped) cite
  [Notes I: y = 2x − 3: b is −3], as ruling 6 did for B5, K12 and A12.
- **10.06** — Notes I's sentence is set at 21 pt (at 23 pt "right." stood alone on a second line). Notes II's three
  lines are one list. Notes III's plane has cells half as tall as wide (2.1 by 1.8 in). Your Turn 2's cells are 0.7
  as tall as wide (minutes and liters have their own scales), so both its graphs are 2.3 to 2.4 in wide. Board 3:
  each window runs 0 to 35 with cells half as tall as wide; the answer slide shows graph D in the same window. Its
  four graphs are 1.4 by 1.2 in, under the 1.4 by 1.8 floor: two lines, the options column and each graph's axis
  names (ruled) leave 2.7 in. They read at 16.5 pt and are kept. Board 5 has no question picture. Bank K9 and A9
  mark only (2, 10) and (2, 20): a dot on the y-axis struck its number when drawn small. K7's columns are half
  hours. Example 2: "rides home at 12 miles every hour".
- **10.07** — Examples 1 and 2 end in one sentence ("…every hour and held 12 gallons when the rain began."), so no
  "It" stands at the end of a line.
- **10.10** — Notes II prints both forms, a = 40 − 2.50n and a = −2.50n + 40. Board 2's steps are "The amount goes
  down:  m = −10" and "The start is the y-intercept:  b = 150". Board 8 is the ride: c = 1.50d + □, a 6-mile ride
  costs \$13.50, the box is 4.50.
- **The papers** — the Reference Sheet's section 6 leads with "When no pair has x = 0, substitute a point and solve
  for b." and section 7's equation is a = 40 − 2.50n. Money keeps two decimals in an equation as the page prints it
  (2.50n, 1.50d, 1.20w, 0.50w, 1.60w).
- **The kit** (Windmill 877c70e) — a handout title too long for its line breaks by length, not at its last word:
  "Slope from Graphs, / Tables and Two Points", "Slope-Intercept Form / and Graphing a Line". Unit 11's handouts
  take the same change when it is rebuilt.

**The lead's look** at every changed slide (a sheet of each deck's changed pages against the build before the fixes),
every picture measured on the built slides and pages, every handout, the Review, the Practice Test and the Reference
Sheet found six more things, none of them mathematics, all fixed:
1. 10.01 Your Turn 1 — "Rate of change: 6 ÷ 5 = 1.2" also reads as y ÷ x (6 and 5 are the table's first pair). It
   is "(12 − 6) ÷ (10 − 5) = 1.2", as board 8 writes it.
2. 10.05 Notes III and 10.06 Notes I — the line with fractions under the picture touched the footer rule (0.02 and
   0.04 in). Each picture gives it room: 0.14 and 0.15 in now.
3. 10.06 board 9 — the answer broke "(0," from "50)" across its two lines. Each pair is kept whole.
4. 10.06 board 5 — "A table of a linear relationship has…" left "5, 8, 11." alone on a second line; it is "A linear
   relationship has the x-values 1, 2, 3 and the y-values 5, 8, 11."
5. 10.07 warm-up 1 asked for "the y-intercept and the slope" (the start first); it asks for the slope first, "6 and 30".
6. 10.07 Your Turn 2 — "A taxi charges a starting amount…" was given a blank line's room under it; it is "a starting
   fee".

**Proved again:** gates at 0 (429 items re-derived), `unit_repeats.py u10` at 0 (8 lessons, 47 paper questions, the
banks read), the unit rebuilt from a clean slate at `checks: 0 findings`, `figure_sheets.py` drew all 279 pictures at
every size, and the 91 questions whose words, key or picture changed (49 on the decks and the papers, 42 in the
banks) were solved blind by a fresh solver who saw no key: no key differs. The script marks 11 rows where the solver
named the same line by more points and 15 where it gave the same answer in other words. Items 4 to 6 above changed
words only after that solve; the gates re-derive them. Every picture on the slides was measured: three stand below
a floor and are kept, each named above (10.05 Notes III's left plane at 1.4 by 2.0 in, the floor itself; 10.06
board 3; 10.07 Your Turn 1 at 2.2 by 1.9 in, the floor itself). Every printed picture is inside its ranges.

**Read and not taken, after the fix pass:** nine slides have a plain line or an answer 0.06 to 0.12 in over the footer
rule. The kit lets a line end 0.02 in past it (published Unit 7 has 18 such slides). Only the two lines with
fractions, which touched it, were moved; the rest stand as the kit sets them. A kit margin for the footer would
change every course's slides, so it waits for its own decision.

**What the review missed and why:** the readers read words, and a Your Turn's picture is only as large as its slide
leaves it. The kit sets a Your Turn's bold line over its picture, so ruling the question into a bold line shrank four
Your Turn graphs. This was found by measuring the built slides, not by reading them. The measuring tools (slidefigs,
paperfigs, footgap) now run before a unit is offered.
