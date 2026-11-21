# A7 Unit 7 — rulings on the review of the built unit (21 Nov 2026)

The lead read the three readers (critic, barton, fast), the four blind solvers' doubts and the two blind-diff tables.
**No key was wrong** (269 questions solved blind; the one DIFFER that was not formatting was the solver's slip). What
follows is everything that changes. Each fixer applies ITS section exactly as written and nothing else.

Ids are `reader_copy.py`'s: `7.04/B6` is board 6, `N2` notes II, `E1`/`YT1` an Example and its Your Turn, `I3` the
Independent Set's question 3, `K7`/`A7` question 7 of the Question Bank / the Additional Question Bank, `W4` warm-up
question 4, `P/Q8a` the Practice Test, `R/Q9` the Review.

## Holds for every section

- **A changed number changes its `check`**, written from the mathematics; every wrong option stays one named error
  with its cite, and a cite must point at a line that exists.
- **Reserved for the paper — keep off the lessons and the banks:** fabric by the yard, a ladybug in seconds, robots,
  reading pages a minute, apples, a plumber, pens, the cost of gas, tickets at 8.50, Marcus, the weight of water,
  trains, a pump in liters. Tables: yards 0, 2, 4, 6 → 0, 5, 10, 15 (2.5) · minutes 4, 6, 10, 16 → 14, 21, 35, 56
  (3.5) · x −6, −2, 4, 10 → 9, 3, −6, −15 · x 2, 4, 6, 8 → 11, 22, 33, 44 (5.5) · x 1, 2, 3, 4 → 4, 6, 8, 10 ·
  gallons 2, 5, 8, 10 → 6.40, 16.00, 27.20, 32.00 · tickets 2, 3, 6, 8 → 17, 25.50, 51, 68 · gallons 2, 5, 10 →
  16.6, 41.5, 83 · hours 2, 3, 5 → 130, 195, 325. Lines through: (2, 1) and (4, 2) · (5, 3) and (10, 6) · (5, 1) and
  (10, 2) · (0, 2) and (2, 4) · (5, 2) and (10, 4) · (1, 60), (2, 120) · (4, 5) and (8, 10) · y = 3x beside
  y = 3x + 2. A new number you choose must not put two rows of one of these tables, or one of these lines, on a
  lesson page.
- **"per" for a constant with its unit** in every answer and step line ("18 gallons per minute", "\$3.30 per
  pound", "8 meters per second"). A story's own sentence keeps plain English ("Ribbon costs \$2.00 a foot",
  "\$2.40 a pound" as an option). Do not touch Notes sentences for this.
- **The one sentence, word for word, wherever it is said:** "On the same axes, the greater positive constant gives
  the steeper line." (was: "the greater constant"). Negative constants are in this unit; the old sentence was false.

---

## Section 7.01 — `u7/l01.py` (and `u7/figs7.py`, for B6 only)

1. **B4** — number the y-axis 0, 7, 14, 21, 28 (one square is 7) so that (2, 14) and the key (1, 7) sit on grid
   corners; the graph at least 2.6 in tall. If `plane` refuses a scale of 7, allow it in `figs7.py` (as for B6:
   every other call unchanged). The four options do not change. (Barton's (4, 14) is not taken:
   (4, 16) is on y = x + 12, the constant-difference line through (2, 14) — that is the additive error; (4, 14)
   would be option D's error a second time.)
2. **B5** — the answer reads "Any multiples of 6 — such as 0, 6, 12". The same pattern for **K8** ("Any multiples
   of 8 — such as 0, 8, 16") and **A8** ("Any multiples of 5 — such as 0, 5, 10").
3. **B6** — the four graphs are about 1.4 in wide on the slide and stop at 7.5 in of a 10-in column. The plan gives
   them 2.2 in. Make the row fill its column: each plot at least 2.0 in wide on the slide, lettering 18 pt or
   more. Work with `choices4`'s `gap`, the planes' `inches` and `S(…, inches=)` first; if `figs7` needs a new
   argument, add it with a default that leaves every other call exactly as it is (you are the only one editing
   `figs7.py` in this pass) and name it in your hand-back. Look at the slide before and after.
4. **B7** — a copier, not a printer, and no "pages": "A copier in room 114 makes 8 copies every minute. Its graph
   of copies against minutes passes through $(7, □)$." Steps: "8 copies for each minute" · "7 minutes: 8 · 7 = 56".
5. **K2** — is the paper's question 1 table. Make it "$y = 7.5x$. Complete the table." (the same x-values;
   0, 15, 30, 45 if they are 0, 2, 4, 6).
6. **K7** — (4, 10) is the paper's given pair. Make it "passes through $(5, 19)$. What is y when $x = 1$?" → 3.8.
7. **A2** — two rows of the paper's question 4 table. Make it "$y = 6.5x$. Complete the table." (the same
   x-values; 0, 13, 26, 39 if they are 0, 2, 4, 6).
8. **A4** — y = (2/5)x is the paper's question 11 line. Make it "Graph $y = \frac{8}{5}x$." on x 0–10, y 0–16
   numbered by 2; key: the line through (0, 0), (5, 8) and (10, 16).

## Section 7.02 — `u7/l02.py`

1. **W4** — "Write $\frac{7}{8}$ as a decimal." → 0.875. (3/8 = 0.375 is the Review's question 5 answer:
   `unit_repeats.py`'s one finding.)
2. **I2** — the fractions table is the set's hardest item, second, and nothing rehearses fraction ÷ fraction.
   Make the table x 7, 14, 35 and y 3, 6, 15. Answer: 3/7. (Why 3/7: the wrong order gives 7/3.)
3. **A2** — two rows of the paper's 7A table. Make the table x 2, 6, 10 and y 21, 63, 105 → 10.5.
4. **A3** — it is board 8's table again. Make it x −4, 2, 10 and y 18, −9, −45 → −4.5.
5. **A8** — a truck, not a train: "A truck travels 168 miles in 4 hours at a steady speed. Find the constant, in
   hours per mile." (1/42 hour per mile, unchanged.)
6. B7 keeps its snail (the paper's animal becomes a ladybug).

## Section 7.04 — `u7/l04.py`

1. **Header.** Add `benchmarks=[("MA.7.AR.4.1", <the text already in benchmark_text>), ("MA.8.AR.3.1", "Determine
   if a linear relationship is also a proportional relationship.")]` — the Lesson Plan then prints both in full;
   `benchmark` (the title slide) stays MA.7.AR.4.1. **Target:** "I can decide from a table, a graph or a
   description whether a relationship is proportional, and whether a linear relationship is also proportional."
2. **Vocabulary** — the definition is 7.01's, word for word: "two quantities are in a proportional relationship
   when one is always the same number times the other: $y = px$; its graph is a straight line through the origin".
3. **N2, second panel** — y = x + 2 from (0, 2) is the paper's question 7 graph D. Draw y = 2x + 3 instead: from
   (0, 3) through (1, 5) and (2, 7); caption "no: from (0, 3)". (It is Notes I's right-hand table and Notes III's
   equation: one relationship as a table, a graph and an equation.)
4. **N3 — the description test is taught nowhere, and the lesson uses it.** Notes III becomes
   "Nothing added at the start", four lines:
   - **A description** — a steady rate with nothing added at the start: proportional.
   - **$y = 2x$** — x = 0, 1, 2 give y = 0, 2, 4: through the origin. Linear and proportional.
   - **$y = 2x + 3$** — x = 0, 1, 2 give y = 3, 5, 7: 3 is added, so not through the origin. Linear, not proportional.
   - **Linear and proportional: $y = px$, nothing added.**
   Keep its figure if it has one. If the cap refuses four lines, join the two equation lines' endings, not the
   description line.
5. **E2** — add the reason as the last worked line, after the three ratio lines:
   "taxi: \$4 added at the start;  bus: nothing added at the start". **YT2**'s steps mirror E2's worked lines one
   for one: "gym: 1 month: 65, 2 months: 90" · "$65 \div 1 = 65$, $90 \div 2 = 45$" ·
   "texts: $0.10 \div 1 = 0.10$, $0.20 \div 2 = 0.10$" · "gym: \$40 added at the start;  texts: nothing added at
   the start".
6. **Cites.** Every "[Notes, Example 2: nothing added at the start]" and "[benchmark: nothing added at the start]"
   becomes "[Notes III: nothing added at the start]" (I4 E, B6 D, the banks).
7. **B6** — option D had two defensible keys ("holds 10 gallons" reads as the tub's size). New stem:
   "**Select all the proportional relationships.**" Options: A "x: 3, 6, 9;  y: 7, 14, 21" (key) · B "x: 1, 2, 3;
   y: 3, 5, 7" · C "the graph" (key) · D "A tub starts with 10 gallons and gains 4 each minute: the gallons and
   the minutes." · E "Parking costs \$3 for each hour: the cost and the hours." (key). Key A, C, E. In the figure
   the line is drawn to the edge of the grid, through (4, 3). If D wraps badly, "A tub starts with 10 gallons and
   gains 4 a minute: gallons and minutes." Steps: "D: 10 gallons at the start;  E: nothing added at the start".
8. **B7** — "A 50-page notebook costs \$3. **Is the cost proportional to the number of notebooks? If so, find the
   constant.**" Answer: "Yes — 3 dollars per notebook."
9. **I1** — its rows (2, 5), (6, 15) are two rows of the paper's question 1 table. Make it x 2, 6, 9 and
   y 13, 39, 58.5. Answer: "Yes — y ÷ x is 6.5 in every row."

## Section 7.05 — `u7/l05.py`

1. **E1** — (2, 35) sits between grid lines. "Maya earns \$120 for 4 hours, the same amount each hour." →
   p = 120 ÷ 4 = 30, e = 30h; table h 0, 2, 4, 6 → 0, 60, 120, 180; the graph on a dollars axis that counts by 20,
   through (2, 60) and (4, 120). Worked (2) begins with "Read the scales first: 20 dollars a square.", then the
   points, then "A straight line through the origin."
2. **YT1** — "Theo earns \$160 for 4 hours at a steady rate: e dollars in h hours. **Find the constant, the
   equation, a table and two points on the graph.**" Steps: "Constant: $160 \div 4 = 40$ dollars per hour" ·
   "Equation: $e = 40h$" · "Table: $40(2) = 80$, $40(4) = 160$, $40(6) = 240$" · "Graph: through $(0, 0)$ and
   $(2, 80)$". Answer: e = 40h. The answer slide may show the graph (a dollars axis that counts by 40 or 20, the
   points on grid corners).
3. **E2** — before the line "$s = \frac{2}{3}f$…" insert "$2 \div 3 = \frac{2}{3}$ cup of sugar per cup of flour".
   **YT2** — before "The other way round…" insert "$6 \div 150 = \frac{1}{25}$ gallon per mile". If the cap
   refuses a sixth worked line in E2, join "$10.5 = 1.5s$" and "$s = 7$" as one line.
4. **B4** — apples are the paper's. "Each carton holds 18 eggs. **What equation gives the eggs e in c cartons?**"
   Steps: "18 eggs for each 1 carton: $p = 18$" · "the equation: $e = 18c$". Answer: e = 18c. (18, not 12:
   board 8 is t = 12c.)
5. **B5** — k is the constant's other name in this deck's vocabulary. "A mile is about 1.6 kilometers. **Which
   equation gives d, the distance in kilometers, for m miles?**" Options in the same places: A $m = 1.6d$ ·
   B $d = 1.6m$ (key) · C $d = m + 1.6$ · D $d = 1.6$. Steps: "1.6 kilometers for each 1 mile: $p = 1.6$" ·
   "kilometers alone: $d = 1.6m$". Cites that exist: C "[7.04 Notes III: y = px, nothing added]",
   D "[Vocabulary: y = px]".
6. **I4** — y for yards trips the y = px habit. "There are 3 feet in 1 yard, so $f = 3n$ gives the feet f in
   n yards. Write the equation for the yards n in f feet." Answer: n = (1/3)f.
7. **I5** — "Complete the table for $y = 4.2x$." x 5, 10 → y 21, 42; backward, y 63 → x = 15. Answer:
   "y = 21 and 42; x = 15". (3.5 is the paper's question 4.)
8. **A2** — two rows of the paper's question 1 table. Make the crane's table t 2, 4, 7 and f 4.4, 8.8, 15.4 →
   f = 2.2t. (Not 4.5: that is this lesson's I6.)
9. **A7** — the same. "$y = 6.5x$": x 2, 6 → y 13, 39; backward, y 78 → x = 12. Answer: "y = 13 and 39; x = 12".
10. **A8** — ribbon by the yard is the paper's story, and y for yards. "Wire costs \$1.25 per meter. Write the
    equation for the cost c, in dollars, of m meters. How many meters does \$10.00 buy?" Answer: c = 1.25m;
    8 meters.

## Section 7.07 — `u7/l07.py`

1. **N1** — add, in bold, after the two computed lines: "**Make both say y for each 1 of x, then compare the
   constants.**" If the cap refuses a fifth line, it takes the place of "The constant of proportionality is the
   amount of y for each 1 of x."
2. **N2** — the title is the one sentence above: "On the same axes, the greater positive constant gives the
   steeper line". **B9**'s last step: "both constants are positive: the greater, 0.75, gives the steeper line".
3. **N3** — add as the last line: "Past the edge of the grid, use the equation: put in what you know, solve for
   the other." If the cap refuses it, put Ana's and Ben's products on one line.
4. **E2** — a snail does not crawl 4 meters in 6 minutes. "The graph shows how far a sloth climbs." — meters
   against minutes, the same line through (6, 4). "**At this rate, how many minutes to climb 10 meters?**"
   Worked lines: "$4 \div 6 = \frac{2}{3}$" (remark: meters per minute) · "$d = \frac{2}{3}t$" ·
   "$10 = \frac{2}{3}t$" · "$t = 10 \div \frac{2}{3} = 15$". Answer: 15 minutes.
5. **YT2** — a label printer, no "pages": "The graph shows the labels a printer prints." — labels against minutes,
   the same line through (4, 9). "**At this rate, how many minutes to print 45 labels?**" Steps:
   "Constant: $9 \div 4 = 2.25$ labels per minute" · "Equation: $n = 2.25t$" · "Solve: $45 = 2.25t$, so $t = 20$".
6. **B3** — no pronouns: A "Max — the longer line" · B "Neither — both start at (0, 0)" · C "Jo — the steeper
   line" (key) · D "Max — the lower line". Steps say "meters per second".
7. **B8** — 8 inches of rain in 3 hours is a record flood. "The graph shows how far an elevator rises. The grid
   ends at 10 feet. **At this rate, how many seconds does it take to rise 24 feet?**" — feet against seconds, the
   same line through (3, 8). Steps: "Constant: $8 \div 3 = \frac{8}{3}$ feet per second" · "Equation:
   $h = \frac{8}{3}t$" · "Solve: $24 = \frac{8}{3}t$, so $t = 9$". Answer: 9 seconds.
8. **I6** — (10, 2) is the paper's question 7 graph C; (10, 3) would have Kayla jogging at 18 km an hour. "Kayla
   walks at a steady rate; the graph shows her kilometers against minutes. At this rate, how many minutes does she
   take to walk 9 kilometers?" — the line through (10, 1), (20, 2), (30, 3). Answer: 90 minutes
   (9 = 0.1t in its working).
9. **K5** — it is the Review's question, word for word. "On the same axes, which line is steeper: $y = 0.9x$ or
   $y = \frac{7}{8}x$?" → y = 0.9x (7/8 = 0.875).
10. **"per"** in the answers and steps (E1, B1, B2, B3, B4, W4, I1, K1, A1 and any other).

## Section papers — `u7/unit.py`

Practice Test (the key letters stay where they are: Q5b B, Q8a A, Q9 C):
1. **P/Q2** — a ladybug, not a snail (a snail does not crawl half a centimeter a second). Nothing else changes.
2. **P/Q5a** — "What is the constant of proportionality?" (no "in dollars per pound": the unit gives part b away).
   Accept 0.6, 3/5, \$0.60. **P/Q5b** — no numbers (three options printed 5a's answer): "What does the constant
   of proportionality tell you?" A "the cost before any apples are weighed" · B "the cost of each pound of
   apples" (key) · C "the pounds of apples each dollar buys" · D "the cost of 5 pounds of apples". Errors as now.
3. **P/Q8a** — no option names a row: A "No — the cost ÷ the gallons is not the same in every row." (key) ·
   B "Yes — the cost goes up as the gallons go up." · C "Yes — 6.40 ÷ 2 = 3.20 and 16.00 ÷ 5 = 3.20." ·
   D "No — the table does not start at 0." **P/Q8b** — its old stem answered part a. "If the cost is not
   proportional, which row would have to change, and what would its cost have to be? If it is proportional,
   write "none"." Key: 8 gallons; \$25.60 — one point for both.
4. **P/Q9** — two options made the same claim. A "A and B — both are straight lines." · B "B only — its line
   starts on the y-axis at 2." · C "A only — its line passes through the origin." (key) · D "Neither — no point
   is marked at (0, 0)." Errors: A every line taken as proportional; B the start on the y-axis taken for the
   test; D the origin taken as missing because it is not marked. All three tagged MA.8.AR.3.1.
5. **Scoring notes on the key**, under the answer: 1a "one point: all three" · 1b "one point: a straight line
   from (0, 0) through (6, 15); plotted points are optional when the line passes through them" · 8b "one point:
   the row and the cost" · 13 "one point: all three" · 14a "one point: both". **Equal forms** beside the answer:
   4: 3.5 or 7/2 · 6: −1.5 or −3/2 · 11: y = (2/5)x or y = 0.4x · 12a: e = 20h · 12b: h = 0.05e, h = (1/20)e,
   h = e ÷ 20.
6. **The drawing grids** (P/Q1 and R/Q1, student paper and key): at least 3.5 in wide.

Review (it renumbers itself; the numbers below are today's):
7. **Two new questions after R/Q3**, in the Lesson 1 section — the paper's two picture-choice shapes, with the
   Review's own numbers:
   - "$y = 1.5x$. Each graph shows y against x. Which graph shows the relationship?" Four graphs built as P/Q2's
     are (the same window logic, the y-axis counting by 0.5 a square): the key through (1, 1.5) and (2, 3) ·
     axes swapped, through (3, 2) · 1.5 read as a start, y = x + 1.5 through (0, 1.5) and (1, 2.5) · the scale
     ignored, through (2, 1.5). Errors named as P/Q2's are.
   - "Four toy cars each roll at a steady speed. The graph shows the distance each car rolls, in meters, against
     the time, in seconds. Which line shows the car that rolls 4 meters every 3 seconds?" One grid, four lines
     through (1, 4), (3, 4), (4, 3) and (3, 3); the key is the line through (3, 4). Errors named as P/Q3's are.
   Spread the keyed letters: no letter keyed twice in a row across the Review's choice questions.
8. **R/Q7 D** — "Each bag of ice weighs 10 pounds." (7.2 is already questions 3 and 13.)
9. **R/Q8b** — "If it is not, which row would have to change, and what would its cost have to be?" (the paper's
   wording). Key unchanged.
10. **R/Q9a** becomes the paper's question 9 in choice form, with one option of its own: "Which relationship is
    also proportional?" A "A and B — in both, y goes up the same amount for each 1 of x." · B "B only — its line
    passes through the origin." (key) · C "A only — its line starts on the y-axis at 6." · D "Neither — no point
    is marked at (0, 0)." R/Q9b unchanged. **New R/Q9c:** "The relationship $y = 9x - 4$ is linear. Is it also
    proportional? Explain." Answer: "No — when x is 0, y is −4: its line does not pass through the origin."
11. **R/Q13a** — "Machine A: 7.2 tons per hour against 6.8".

Reference Sheet:
12. Opening, last sentence: "On this unit's test you will have neither the FAST reference sheet nor this one."
13. §6: "Store A: 4 pounds for \$12.20 is \$3.05 per pound. Store B: c = 3.15w is \$3.15 per pound. Store A costs
    less per pound." · the one sentence: "**On the same axes, the greater positive constant gives the steeper
    line.**" · "**Past the edge of a grid, use the equation.** A line through (5, 7) is y = 1.4x; for y = 28,
    28 = 1.4x, so x = 20, wherever the grid stops."
14. §7: "**proportional relationship** — two quantities are in a proportional relationship when one is always the
    same number times the other: y = px".

---

## Read and not taken (with the reason)

- critic 10's oranges (o reads as zero: eggs) · critic 11's negatives in the key ("any multiples" already holds them).
- barton 9's table 2, 4, 8 → 2.5, 5, 10 (its pairs are the paper's question 15) · barton 10 (above, 7.01 ruling 1).
- fast 2's two fixes (a number-free choice does more: 5b no longer leans on 5a either way) · fast 6's two codes on
  the title slide (the kit's rule is one code there; the plan now prints both) · fast 10's d for yards (n) ·
  fast 11's turtle and beetle (the paper's animal changed instead; the sloth is for realism).
- fast 7's choice forms for R/Q5b and R/Q8a: the Review's open form asks for more than the paper's choice.
- The solvers' doubts (open questions without a single answer, the order of a table's blanks, a fee's wording):
  each is the intended reading; none leaves two keys.
- Left as they are, on purpose: 7.01/I5 (cherries at 3.50 — one row in common with the paper's table, a different
  question) · 7.02/K4 and 7.05/K11 (a 2.5 line read, where the paper has it drawn) · 7.05/K2 · 7.07's rice table.

---

## After the fix pass (21 Nov 2026, the same night)

Six fixers (Claude Opus 5.5), one file each, applied the sections above. Where a slide's room forced another
wording, this is what stands:

- **7.01** — board 6's four graphs are 2 in wide: `figs7.plane` gained `aspect` (a cell's height against its width;
  default 1), used here at 0.65, and each window runs to 9 so the last number on an x-axis is 8 with a square to
  spare. A4's y-axis counts by 2.
- **7.04** — Notes III's terms are plain text (the deck takes no mathematics in a term). Example 2's reason is two
  worked lines ("taxi: \$4 added at the start", "bus: nothing added at the start"). Your Turn 2's answer slide
  holds two steps: "gym: 65 ÷ 1 = 65, 90 ÷ 2 = 45: \$40 added at the start" and "texts: 0.10 ÷ 1 = 0.10,
  0.20 ÷ 2 = 0.10: nothing added at the start". Board 6's options D and E are "A tub starts at 10 gallons, gains
  4 a minute." and "Parking costs \$3 for each hour." (an option beside a figure is at most 8.5 in wide).
- **7.05** — Example 2's working is two slides, a minute each (the second begins with the inserted line). Your
  Turn 2 joins the equation and its solving in one step. Your Turn 1 carries `repeat_ok` (160 and 40 are numbers on
  Example 1's dollars axis).
- **7.07** — Notes I: the new line took the place of "The constant of proportionality is…". Notes II's head is
  "Compare the lines on one grid"; the sentence is the slide's first line, word for word. Example 2's working is
  two slides. Board 8 reads "The graph shows an elevator rising. The grid ends at 10 feet."
- **The papers** — the Review is 17 questions on 8 pages (it was 15 on 7). Its keyed letters: 3 C · 4 D · 5 A ·
  9 B and D · 11a B. The grids of P/Q1 and R/Q1 print 3.56 in wide.

**The lead's look** at every changed slide, a bird's-eye sheet of each deck and the papers' changed pages found
seven more things, none of them mathematics, all fixed:
1. 7.04 Notes II — the four graphs stood 5.7 in wide in all, their captions at 9 pt. Cells half as tall as wide,
   y-axes numbered every second line: now 9 in wide and readable.
2. 7.04 Notes III — three lines wrapped and ran together. Each is one line now: "a steady rate with nothing added
   at the start" · "at x = 0, y = 0: through the origin. Proportional." · "at x = 0, y = 3: 3 is added. Not
   proportional."; the head is "Proportional: nothing added at the start".
3. 7.04 board 8 — with y counting by 4, y = 5x − 2 passed half a square under the origin. It counts by 2 now.
4. 7.07 Independent Set 3 — the labels (2, 30) and (3, 30) touched their points; moved clear.
5. The papers' header — the title ended against "Date" (the kit: the title's cell keeps a margin now).
6. P/Q2 and R/Q4 — the four graphs printed 1 in wide; the row fills the line now.
7. 7.05–06's title — "Equations of Proportional Relationships; Translating Representations" made a key's path in
   the package 184 characters and the install refused it. The deck is "Writing Equations; Translating
   Representations".
Four stale teacher lines were corrected (7.04's question about the tub and its "parking garage"; 7.05's "counts by
5"; a 7.07 cite to a line that did not exist).

**Proved again:** gates at 0 (282 items re-derived), `unit_repeats.py u7` at 0 with the banks read, the unit
rebuilt from a clean slate at `checks: 0 findings`, and the 82 questions that changed — both papers whole and 35
lesson questions — solved blind by two solvers who saw no key: no key differs (the six rows the script marks are
open questions and the same answer in other words).

**What the review missed and why:** no reader saw the banks as text (the copy they were given left them out), and
`unit_repeats.py` did not read them. The lead read all five banks: 7.07's bank question 5 was the Review's
question 14 word for word, and seven bank or set tables shared rows with the paper's tables (2.5, 3.5, 5.5). Both gaps are
closed in the kit: `reader_copy.py --bank` is what a reader gets, and `unit_repeats.py` reads the banks.

## 21 Nov, late morning — Lexend throughout

Croix, of the Review in Times beside the Practice Test in Lexend: "why does the font switch? It should be the lexend
font throughout every document." Every document of the unit is rebuilt in Lexend (`DOC_FONT`), at `checks: 0 findings`.
The Lexend build stopped once, on 7.07's Lesson Plan: three boards' `qtext` wrote money with a bare dollar sign, and
the words between two amounts had been drawn as mathematics all along. Fixed; the gate refuses it now. 7.02's
Independent Set gave up a little work room on questions 1–4 to stay on two pages.
