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

## 21 Nov, afternoon — the wording pass (ruling 58)

Croix sent two outside audits of the All Slides PDF (a slide-by-slide "revision guide", 11:06 am; ChatGPT's language
audit, 11:43 am) and, on the defaults put to him, said "Go" (11:58 am). No number, picture or key was changed.

**Rules applied to every deck, Independent Set, Question Bank, Lesson Plan and paper**

1. A graph shows y "versus" x. Never "against".
2. A rate is "per": "\$3 per mile", "the same amount per pound", "60 minutes per hour". The constant of proportionality
   is "the amount of y for every 1 unit of x"; the unit rate is "the amount of y for 1 unit of x".
3. A table drawn left to right has pairs, and its rows are its two quantities: "y ÷ x is the same for every pair",
   "check a pair", "which cost would have to change, and what should it be?".
4. The definition, in the same words wherever it is given: "two quantities are in a proportional relationship when one
   quantity is always a constant multiple of the other: y = px".
5. A stem is a whole question or command. A variable does not open a sentence ("Let e represent her earnings, in
   dollars, after h hours."). Two sentences are two sentences, not one joined by a colon.
6. A student is told to "explain", "identify", "tell" or "write", never to "say" (a person in a problem still says
   something: "Kim says the line for y = 0.6x is steeper…"). "The other way around". "Either quantity can be y" (not
   "the subject", not "alone").
7. A choice gives its reason in words: "B only, because its line passes through the origin."; "No. 15 ÷ 4 is not 4.";
   "Jo, with the steeper line". No answer line has two dashes.
8. A description in a select-all names its two quantities in parentheses: "A tutor charges \$30 per hour (cost and
   hours)."
9. "Read the scales first: the cost axis counts by 2." (not "is scaled by", "goes by", "cost by 2").
10. "Choose x-values that give whole-number y-values" (not "easy points").

**Headings and bold lines changed**: 7.01 Notes I "What makes a relationship proportional?", Notes II "The graph of a
proportional relationship"; 7.04 Notes I "The table test: check every pair", Notes II "The graph test: two conditions"
with "The graph must be a straight line, and it must pass through the origin.", Notes III "Nothing added at the start"
with "A linear relationship with nothing added is proportional: y = px."; 7.05 Notes II "From a graph or a
description", Notes III "Either quantity can be y"; 7.07 Notes I "Compare the constants" with "Find each constant in
the same units, then compare them."; the Reference Sheet's section 5, "Writing the Equation in Both Directions".

**Kit-wide (ruling 58 in the kit's ledger)**: a board prints no "Answer it."; a written board says "Write your answer
in complete sentences."; the IXL slide's three lines and "Required IXL skills"; the cover's "the next slide links to
each one"; a Review section of one question says "1 question"; a Lesson Plan with no new word says "No new terms.".

**Not taken**: y = kx (Florida writes y = px); the guide's "math error" on 7.04's warm-up (the slide reads y = 3x), its
k = 0.625d and its × sign; "every row" kept by ChatGPT's audit; the removal of the ruling-22 numbers (the snail's age,
the 180 passengers, the 40 seats, the 50 pages); "Independent Practice" for "Independent Set"; serial commas where a
target quotes its benchmark; "initial value of 0" (the unit's words are "nothing added at the start"); "steady" left
as it is (both audits write "constant" — Croix's to say); every rewrite too long for its slide.

**What the slide would not hold** (found by the test build and the lead's look, and shortened): a warm-up stem is one
line, so 7.01's "Plan A costs 12 + 4w. Plan B costs 6w. When are they equal?", 7.04's "Find the constant of
proportionality for (4, 6) and (10, 15).", 7.05's "For (3, 5), (6, 10) and (9, 16), is y proportional to x?" and "Find
the constant, in dollars per pencil.", 7.07's "y is proportional to x. When x is 4, y is 26. Write the equation." and
"Which costs less per pound: 3 pounds for \$7.20 or 5 for \$11.50?"; 7.02 board 5 keeps one line of words ("Find the
constant of proportionality of the line."), and 7.04 board 4 one line ("A line passes through (0, 1) and (2, 5). Is it
proportional?"), so their graphs keep their size; 7.04's Example 2 and Your Turn ask a whole question of each situation ("A taxi
charges \$4 to start plus \$3 per mile. Is the cost proportional to the number of miles?"), which the slide wraps
onto a second line, and answer in one line ("Taxi: no. Bus: yes.", "Gym: no. Phone plan: yes."); 7.05's Your Turn
is "Theo earns \$160 for 4 hours at a steady rate." with "Find the constant, the equation for e, the table and two
graph points."

**Proof**: gates 0 (282 items re-derived); `unit_repeats.py u7` 0; `checks: 0 findings`; 151 reworded questions solved
blind by two solvers, no key differs; two of their doubts were real and are fixed (7.05's Your Turn did not name the
letter e; 7.07's first warm-up read "the equation y = px" as given); every changed slide looked at (152 in the
first pass, 14 after the fixes, 3 after Example 2's whole questions went back in) and the papers on contact sheets;
every PDF searched for the old lines ("Answer it.", "against", "the other way round", "easy points": none left);
every character of text is Lexend (the only other glyphs are the answer bubbles, the check boxes and the back arrow,
which Lexend does not have).

## 21 Nov, later — the second wording pass (ruling 59)

ChatGPT's third audit ("Deep Second-Pass Editorial and Consistency Audit"), of the rebuilt All Slides and All Documents
PDFs, sent by Croix at 3:08 pm. His three answers: "steady" — "Switch to "constant""; the Independent Set's opening line
— "Just get rid of it completely"; who reads the Lesson Plans — "John or admin: write it out".

**Taken**

1. Nothing printed carries a ruling number or a word about the build. 7.01's Materials said "the build cannot print a
   43-minute one"; six wrong answers were cited "[ruling 22]" (now "[an extra number, included on purpose]"); the
   Practice Test key's note said "(ruling 19)".
2. The constant of proportionality "equals y ÷ x for every pair where x is not 0" — at its definition (7.02–03's
   vocabulary slide, the Reference Sheet) and nowhere else: a table whose x-values are 2, 4 and 8 is still tested
   "for every pair". 7.02–03's plan gains the question "Every proportional relationship includes the pair (0, 0). Why can
   that pair not be used to find the constant?" (DOK 2).
3. 7.04 Notes I and the Reference Sheet: "Going up by the same amount does not make y ÷ x the same." A proportional
   table goes up by the same amount too, so "is not the same ratio" was loose.
4. 7.04 board 5 and its two bank twins: a line "passes through (0, 0)", the unit's phrase, not "reaches". ("Extend the
   line, and it reaches (0, 0)" stays in Notes II and on the Reference Sheet: there the line is being extended.)
5. "Explain." for "Give the reason." (nine places in 7.04), so a set asks one way.
6. The Review's directions are the Practice Test's first sentence: "Show your work for problems that require
   calculations." (kit).
7. "Constant" for "steady": a constant rate, speed, pace or increase, in 28 places.
8. The Lesson Plans in whole sentences (kit template and each lesson's own fields), and "whiteboard question 3" for
   "board 3" in a plan's prose. The checks table keeps its compact form (wrong answer — cause [source]) under the
   heading "Likely wrong answers and their causes".
9. An Independent Set prints no instruction line (kit).

**Wrong on the facts**: Theo's e and h are named by his table's rows ("hours h", "dollars e"); both pumps are named, on
the table and on the graph; the Reference Sheet exists (Handouts) and was not in the two PDFs; "two constants" is the
standard statement (one for each direction); "11.07–08" is right, because A7 teaches Unit 11 before Unit 7; the packet's
Independent Sets and banks are its keys by design (All Documents is the teacher's packet; the student copies are in
Lessons).

**Not taken**: "x ≠ 0" on every line that says "every pair"; "two reciprocal unit rates, depending on which quantity we
treat as the output"; every longer board question (a board is read at a glance); "× " in a worked line; dropping the
comma before a unit ("…, in dollars per pound" is how the state's items write it); "The price per pound is constant" for
"cost the same amount per pound"; removing the B1G-M tags (the state's guide, cited for each wrong answer); "Independent
Practice"; "Higher-Order Questions" renamed; the ruling-22 numbers removed; "inverse conversion equation" for "the other
way around"; a second sentence on every answer slide.

**What the slide would not hold**: 7.04 board 5's answer line is "C — Yes. It passes through (0, 0)." ("Their line
passes through" and "The line passes through" each ran to two lines; the step above it names the line); the definition
is in words, "where x is not 0" ("$(0, 0)$" broke across the line at its space and printed a dollar sign — `markup`
refused it — and without the space left a gap before the colon); 7.02–03 board 7 is "A 3-year-old snail crawls 34
centimeters every 8 minutes." ("…in 8 minutes at a constant speed." left "speed." alone on a second line; "every" is
how the unit gives a rate: "8 copies every minute"); the pump question keeps "by how many gallons in 15 minutes?"
("How many more gallons does it move in 15 minutes?" needs a second line).

**Proof**: gates 0 (282 items re-derived); `unit_repeats.py u7` 0; a full rebuild, `checks: 0 findings`; the student
view before and after differs in 23 questions (19 "steady" to "constant", 3 "Give the reason." to "Explain.", the
snail) and 3 answers, in no key and no check, so no solver was run; the 12 changed slides, the five plans and a page of
each changed paper looked at; every PDF searched for the old lines; page counts unchanged (plans 5 pages each).

## 21 Nov, night — the third wording pass (the pages looked at)

Gemini's "Comprehensive Proofreading & Edit Checklist", the fourth outside audit, sent by Croix at 8:50 pm with "Drop the
line. Also here is what Gemini found. I want the student facing slides and handouts specifically to be perfect." "The
line" is the follow-through note on a key.

**Taken from Gemini**

1. No key prints a follow-through note (kit). Ruling 19's scoring is unchanged.
2. A line "passes through" a point, everywhere: the Reference Sheet and 7.04 Notes II no longer say "reaches".
3. A graph "shows how far a cyclist rides", "how far she walks", "how much two workers earn", "how many tons of snow
   Machine A makes"; the compressed "two cyclists' miles versus hours" is gone. "Versus" stays where it names both
   quantities in full ("the distance each car rolls, in meters, versus the time, in seconds") and where a student is
   told what to graph ("graph cost versus pounds").
4. A decimal takes a plural unit: "0.8 pounds per dollar", "0.75 gallons per room", "0.2 liters", "0.6 dollars per
   pound". A fraction keeps the singular ("1/24 gallon per mile").
5. Where the letters are not x and y, the equation is "for" a letter: 7.05–06 Notes III is "An equation for either
   quantity"; Example 2 and its Your Turn ask "Write the equation for f" and "for m"; board 5's step is "kilometers =
   1.6 · miles".
6. 7.02–03 Notes III names the unit before each division ("miles per gallon: 120 ÷ 5 = 24"), so no dash stands before a
   number.
7. 7.04: the captions "no: starts at (0, 3)" and "yes: extends to (0, 0)"; board 3's step "the last pair does not give
   4"; board 4 "Is y proportional to x?".
8. 7.07: "For values beyond the grid, use the equation."; a comparison's answer is "Store B (\$3.30 per pound versus
   \$3.50)", with no second colon after "Answer:"; "Bus A has 40 seats and travels 135 miles in 3 hours."
9. The Reference Sheet: "You may not use this sheet or the FAST reference sheet on the Unit 7 test."; "In 0 hours you
   earn \$0"; "If even one pair gives a different value of y ÷ x, the relationship is not proportional."; "A table does
   not have to show the pair (0, 0)…"; "The constant depends on which quantity is y."; "goes down from left to right
   through the origin"; "A constant of 0.25 dollars per minute means that each minute costs \$0.25."; "Use the third
   point as a check"; "find what one square stands for on each axis"; "using the problem's letters"; "You can write an
   equation for either quantity."
10. The papers: the Review's "How to use this review" (kit); "Which graph shows the relationship y = 1.5x?" without
    "Each graph shows y versus x."; "after it is released"; "For how many hours can you rent a kayak from Shop A for
    \$144?"; "how many more miles has the faster train traveled?"; the bank headings "Find the unit rate." and "Write the
    equation the other way around."; "the gallons g of water in a tank after t minutes"; the hose question; "Which
    store has the lowest price per pound?"; and "different numbers of" gone ("how many marbles are in 2, 5 and 7 bags",
    "how far she paddles", "how many pages he reads").
11. The keys: the Review key's question 17 prints its question above the SSDD note; "Working backward:"; "D says no, but
    its reason is not valid"; "one pair with a different value means the relationship is not proportional"; "beyond the
    grid".
12. The plans: "are not introduced until lesson 7.04"; "explain what it means in context"; "Which one is the constant,
    and what tells you?"; 7.04's ESE row "a row for y ÷ x"; 7.07's sentences on one form and on the word "slope".

**From the reading and the look, beyond the list**

13. A sentence does not open with a numeral: "Five notebooks cost \$9.00.", "Twelve pencils cost \$3.", "In 0 hours you
    earn \$0", "Typing 250 words in 5 minutes is…", "One relationship, 60 minutes in 1 hour, has two constants.";
    7.02–03 board 6 is two rows, "Rice costs the same amount per pound, and 5 pounds cost \$8.00." and "The constant of
    proportionality is 1.6. What does 1.6 mean?".
14. "No." is not followed by a numeral, where it reads as "number": "No, 20 prints would have to cost \$7.00."; "No,
    because 6 ÷ 1 = 6 but 10 ÷ 2 = 5."; 7.04 board 3's choice D is "No. The last pair gives 3.75."
15. 7.07 board 3's choices are facts about the two lines ("Max. Max's line is longer.", "Jo. Jo's line is steeper."),
    not "The steeper line is faster": a line has no speed, and the student decides which fact answers the question.
16. 7.02–03 board 9's answer is "Ben. y ÷ x = 5, and Ana divided x by y."; 7.04 board 9's is "y = x + 4, for example.
    It is a straight line through (0, 4), not the origin."
17. On the Reference Sheet a sentence does not open with an equation ("The equation w = 50m gives…", "The line y = 2x
    is steeper than the line y = 1.4x."), and the comparison is two short equations ("Store A costs 3.05(10) = 30.50
    and Store B costs 3.15(10) = 31.50").
18. A word alone on a slide's second line: 7.02–03 board 2 asks "in cups per cookie" (board 1 says "cookies per cup");
    7.01's set, question 6, is "The point (1, 3.5) is on the graph from question 5. What does it mean?".
19. The gap before an equation on a slide (the deck's 6% margin on a run of words): sixteen lines write a simple
    expression in words, among them the four Vocabulary slides, 7.01 board 8, 7.02–03's second example and Your Turn,
    7.04 Notes II and III, 7.05–06 Notes I and II, 7.07 boards 1 and 2; two put the picture early (7.01 board 7, "The
    point (7, □) is on the graph of copies versus minutes."; 7.02–03 board 9, "Ana says 1/5 is the constant of
    proportionality.").
20. On paper (kit): an equation in a sentence does not break across a line; a stacked fraction stands on the line
    with its comma beside it; a paragraph's last line is never one short word.

**Wrong on the facts**: the Reference Sheet prints "x: −2, 1, 4" (the audit read 2 and asked for the mathematics to be
checked); the 3 in slide 73's equation is a 3; the Practice Test key prints "83 = 8.3g".

**Not taken**: "Write an equation for f in terms of s" on a slide (the unit says "the equation for f"; "in terms of"
is on the Review and the Practice Test, as the state writes it); "which variable to isolate", "Solve for the other
variable", "Either variable can be isolated" (the unit's words are "which quantity" and "the other way around", ruling
58); "SSDD" taken out as a British term (it is Croix's own word for the routine); the dates taken out of 7.07's plan
(the plan is for his calendar); "[distractor information used]" for "[an extra number, included on purpose]"; "a \$40
service fee" for "\$40 to come to the house"; "Does it represent a proportional relationship?"; "the last pair breaks
the proportional pattern"; "\$0.25 per minute means each minute costs \$0.25" (it says one thing twice); "Plot a third
point to check that your line is straight" (three points are plotted and the third is the check); "Award 0 points
if…" (the key gives the reason in a sentence); a new stem for "A table is shown. y is proportional to x." (the
state's form); "Max, because his line is longer" (the choices became facts instead, item 15).

**What the slide would not hold**: 7.01's first warm-up does not say what w is ("After w weeks, Plan A costs 12 + 4w
and Plan B costs 6w." measures 12.9 in and a warm-up line is 10.45 in; "Plans cost 12 + 4w and 6w for w weeks." and
"Costs for w weeks: 12 + 4w and 6w." fit and are worse sentences); 7.05–06's first Your Turn keeps "Find the
constant, the equation for e, the table and two graph points." (the table's rows are "hours h" and "dollars e"; the
fuller sentence is two lines, and the answer slide then cannot hold its four steps); the pump example keeps "Which pump
is faster, and by how many gallons in 15 minutes?" (the fuller question ran into the footer); 7.01 board 5 keeps "y =
(5/6)x. Choose three x-values…" ("For y = (5/6)x, choose…" took a second line from the answer's steps); 7.04 board 6's
tub "gains 4 per minute"; 7.07's Independent Set slide holds its six questions only with their equations as pictures,
and 7.02–03's keeps one so that the five set slides look alike.

**Proof**: gates 0 (282 items re-derived); `unit_repeats.py u7` 0; a clean rebuild and `checks: 0 findings`; the student
view before and after differs in 58 questions, 28 answers and 5 lists of choices, in no keyed letter and no check, so
no solver was run; all 62 changed slides looked at in their last form; the Reference Sheet, the Review, the Practice
Test and the five Independent Sets looked at page by page, with pages of the banks, a plan and a key; no line of any
paper breaks inside an equation (25 did) and no paragraph of a student paper ends on a line under ten characters; every
PDF searched for the old lines; every PDF has the page count it had.
