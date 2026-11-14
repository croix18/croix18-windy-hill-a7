# A7 Unit 11 — Solving Equations and Systems — Audit

*14 November 2026. Math Nation Grade 7 Accelerated, Unit 11 (lessons 11.1–11.8, the practice problems, the homework,
their keys, the unit assessment, its key and guide, the worked examples), read from Croix's Drive as an audit target
after the lessons were outlined from the benchmarks (HOUSE STYLE §16; `A7 Unit 11 Solving Equations and Systems -
Lesson Outlines.md`). Every problem was worked in sympy by two readers who did not write the outlines: Part 1 is
lessons 11.1–11.4 (MA.8.AR.2.1), Part 2 is lessons 11.5–11.8 and the assessment (MA.8.AR.4.1–4.3). No Math Nation
page is in this repository.*

## Bottom line

- **29 student-facing defects and key errors** (D1–D11 in Part 1, E1–E18 in Part 2), from 211 pages and 282 logged
  checks. One printed final answer is wrong (E2, a worked example that drops a sign: the solution is (−4, 7)); one
  practice item's student page and key are different equations (D6); one test item's key answers a different stem
  (E1); four answer graphs are not the lines of their equations (E4, E5). None is reproduced in Unit 11.
- **The book assumes slope and y-intercept in every systems lesson and on its test**, and solves systems
  algebraically in 11.5. This course teaches Unit 11 before Unit 10 (ruling 52), so every line is graphed from a
  table of values, and nothing is solved by substitution or elimination (the outlines' standing decisions 1–3).
- **The book's test is not the blueprint.** It has no multiple choice, no select-all and no AR.2.1 item with no
  solution; its approximate-solution item keys an exact pair and its guide takes points off a correct estimate (E15).
  The practice paper follows the benchmarks and the FAST item shapes instead (the outlines, "The test").

## Decisions taken on the readers' judgment calls (each reversible)

1. **A false ending is written as the false equation, then the words**: "8 = 5 — never true: no solution" (the
   state's a = b form), never "8 ≠ 5" as a line of work.
2. **The book's x = 3.5 item is not used** (a vertical line is outside MA.8.AR.4.3's slope-intercept boundary);
   approximation is taught on two slope-intercept lines whose crossing falls between the grid lines.
3. **A story's crossing has to make sense in the story**: whole months, a hiker who stops at the lake. The internet
   plans (E7) and the hikers (E8) are not reused.
4. **No table of five substitutions is offered as proof of "no solution" or "every number"** (D4): the endings are
   reached by simplifying both sides.

---

# Part 1 · A7 Unit 11 — Solving Equations and Systems of Equations — Audit, Part 1 (Lessons 11.1–11.4)

Math Nation Grade 7 Accelerated, Unit 11, lessons 11.01–11.04, read as an audit target against MA.8.AR.2.1 (Source of
Truth Part 1, Parts 4–7; B1G-M reading notes, "MA.8.AR.2.1"). Files read: the four Teacher Editions (11.01–11.04 TE,
37 pages, printed pp. 949–985), the Student Edition pp. 93–110 (file pp. 3–20), and pages 1–8 of Practice Problems,
Practice Problems Keys, Homework and Homework Keys (two pages per lesson). Every page that carries a key, a table, a
tile model or a hanger was viewed as an image; the hanger figure, the tile tables and the card-sort keys were viewed
again at 200–250 dpi. Every equation, every printed key value, every substitution line and every printed work line was
checked in sympy (`/tmp/mn_check/check_u11_part1.py`, outside the repository); §7 is its log. No Math Nation page is
reproduced here: items are described in our words, with the book's equations only where a check needs them.

Page conventions: SE and TE pages are the book's printed numbers. "PP p. n", "PPK p. n", "HW p. n", "HWK p. n" are file
pages of Practice Problems, its Keys, Homework and its Keys (pp. 1–2 = 11.1, 3–4 = 11.2, 5–6 = 11.3, 7–8 = 11.4).

**14 November 2026.** 87 pages read; 173 sympy checks, covering 171 printed work lines and 39 table cells.

| Files | Pages | Checks | Agree |
|---|---|---|---|
| 11.01 TE + SE pp. 93–97 | 11 + 5 | 23 | 22 (the TE's halving note is wrong, T1; Kenneth's wrong move lands on the right answer, D1) |
| 11.02 TE + SE pp. 98–103 | 10 + 6 | 14 | 14 |
| 11.03 TE + SE pp. 104–107 | 9 + 4 | 22 | 22 |
| 11.04 TE + SE pp. 108–110 | 7 + 3 | 23 | 22 (card K's work line, D8); the stem undercounts Clare's errors (D7); no cards supplied (D11) |
| Practice + Keys, 11.1–11.4 | 16 | 47 | 43 (PP 11.4 #10's stem and key solve different equations, D6; two key typos, D9–D10) |
| Homework + Keys, 11.1–11.4 | 16 | 44 | 43 (HW 11.1 #7 asks for coins, defines and keys dimes, D3) |

Every printed final answer that matches its own stem is right, including every "one / none / infinitely many"
verdict. The defects are in stems that do not match their keys or work, in printed work lines, and in item design.

## 1. Student-facing defects and key errors

Numbered; what the page says and what is true. None is to be reproduced.

**11.01**

| # | Where | Says | True |
|---|---|---|---|
| D1 | SE p. 94, 11.1.3 #2 (TE p. 953) | Kenneth combines 3c, 6 and 6c into 15c, giving 15 = 15c, and the item has students call that wrong | The wrong move gives c = 1, which is the **correct** solution of 15 = 3c + 6 + 6c (3 + 6 + 6 = 15). A student who checks Kenneth by substitution finds him right. The error is real, but these numbers cannot expose it. Any constant other than 6 (say 15 = 3c + 4 + 6c, giving 11/9 against 15/13) separates the two |
| D2 | SE p. 96, 11.1.5 (key TE p. 957) | Elena's first step is described as "add 2 to both sides". The key says she erred "when she added 2 to both sides" and that "adding negative 2 in parentheses … is not the same as adding 2" | Adding 2 to both sides is a legal first step. Her error is writing the +2 **inside** the parentheses, which adds only 1/2 to the left side and leads to her c = 80. The key names a legal move as the error. Its second sentence misdescribes what she added (+2, not −2); one possible reading is "adding 2 to the −2 inside the parentheses", but the printed wording is unclear |
| D3 | HW p. 2 #7 (HWK p. 2) | c is "the number of coins Marcela has", and the question asks for "the number of coins she has". The key switches the letter to d and answers "9 dimes (and 9 nickels)" | 0.10c + 0.05c + 0.12 = 1.47 gives c = 9, which is the number of **dimes** (and of nickels). She has 9 + 9 + 12 = **30 coins**. The stem's definition of c is wrong, and the key answers a different question from the one asked |

**11.03**

| # | Where | Says | True |
|---|---|---|---|
| D4 | SE pp. 105–106, 11.3.3 #1b and #2; PP p. 5 #2 and #4; HW p. 5 #2 and #4 | After five or six substitutions, students are told an equation was "true for all values" or "false for all values", or are asked to explain how many solutions there are "based on your work in question 1" | Finitely many checks cannot show **no solution**. The equation j = 7 is also false at all six of HW #1's values. For a linear equation, two true checks do force an identity, but no page says so. The keyed verdicts (none, infinitely many) are true, but the evidence the page points to does not establish them. The reason is the simplification: 3n + 2 = 3n + 1 gives 2 = 1 |
| D5 | PPK p. 5 #5 (Samir) | The key says only "No … the right side … simplified to 5a + 1, therefore both sides are not the same" | 4a + 1 = 5a + 1 has exactly **one** solution, a = 0. The key never says so, and this is the case behind the TE's own named misconception (p. 971: a solution of 0 read as "no solution") |

**11.04**

| # | Where | Says | True |
|---|---|---|---|
| D6 | PP p. 8 #10 (student page) vs PPK p. 8 #10 | The student page's stem is 3(2g − 11) = 5g + g − 11. Soledad's printed work, and the key's own stem, start from 3(2g − 15) = 5g + g − 45. The key: "I do not agree … infinite number of solutions" | For the equation the student is given, 6g − 33 = 6g − 11 has **no solution**, so Soledad's claim is **true** and the key marks the correct answer wrong. The key's verdict holds only for the key's equation (6g − 45 = 6g − 45). Her work also does not start from the stem it is meant to solve |
| D7 | SE p. 108, 11.4.2 (TE p. 982) | "She knows she made a mistake", and students "circle where she made the mistake" | Clare's work has **two** independent errors. Line 2 writes −(5 − 9y) as −5 − 9y. Line 4 writes −5 − 60 as −55. Each other line is equivalent to the line before it (checked). The TE circles both, so the stem's singular contradicts its own key. Correct solution: y = −65/11, with both sides −900/11 (checked) |
| D8 | TE p. 984, card K | The second line, −0.8s − 3 = 7 − 0.8s, is printed as the simplified first line | The right side of 0.80s − 3 = 7 + s − 0.20s simplifies to 0.8s + 7. The printed line gives **both** variable terms the wrong sign, so it is not the simplification. The verdict, no solution (−3 = 7), is right |
| D9 | PPK p. 7 #3 | 4 + 6 = −3, then "10 ≠ 3" | The right side is −3. The line should read 10 = −3 (false), so no solution. The verdict is right |
| D10 | PPK p. 8 #8 | 1.7k + 0.6 = 1.7k + 1.8, then "0.8 ≠ 1.8" | The left constant is 0.6: 0.6 = 1.8 (false). The verdict is right |
| D11 | SE p. 109, 11.4.3; TE p. 979 Materials | "You and your partner will receive 12 cards." The materials list "Equation Cards for 11.4.3 Activity" | The cards are not in any file supplied. The SE recording sheet carries only the letters A–L. The twelve equations exist only in the TE's red key (pp. 983–984), so the activity cannot run from the student page. Every card's key is right apart from card K's work line (D8): one solution B, F, G, J; no solution A, C, K, L; infinitely many D, E, H, I |

Wording, notation and typos on these pages, not counted above (none changes a value):
- **Negative signs.** The SE p. 99 tile tables print negatives with a raised minus (¯2x, ¯1), and so does the TE p. 968 key (¯4, ¯20). Every other page uses "−".
- **Key notation.** The keys multiply a whole equation written in parentheses ("(… = …) × 4": PPK p. 7 #5, p. 8 #7). PPK p. 4 #10 prints "3 · −8" without parentheses.
- **Typos in keys.** HWK p. 4 #4 prints "3(0.6 − 0.4)— 0.3 + 0.9" (the "=" is missing). HWK p. 2 has "CBanker's Method". The TE p. 982 key spells the student "Claire" (the SE has "Clare").
- **SE p. 99, 11.2.2 #1a:** says "each equation" when there is one.
- **SE p. 110, 11.4.4:** has a reflection row on real-world contexts, but 11.4 has none.
- **Algebra tiles on PP p. 3 and HW p. 3.** The pages print in grayscale, so the 1, −1 and −x tiles are the same dark gray. Only small labels tell them apart.

## 2. Teacher-facing slips

- **T1 — a math error (TE p. 955).** The note on 13 = g + 2(g − 4) says that dividing every term by 2 gives
  "7.5 = g/2 + g − 4". The true halving is **6.5** = g/2 + g − 4 (13/2). The printed equation has solution g = 23/3,
  not 7. This is the one place in these lessons where the book models a step and gets the arithmetic wrong, and it is
  the step it tells the teacher to show the class.
- **T2 (TE p. 956).** "Why does Joel rewrite the fraction this way after distributing the 4?" Joel distributes 1/4.
  Nichele is the one who multiplies by 4.
- **T3 (TE p. 961, misconceptions).** "try to combine terms that **can** be combined" should be "cannot".
- **T4 (TE p. 966, 11.2.2 #3b).** The sample answer says the x-term has "a coefficient of −1 that must be eliminated".
  The coefficient is made 1, not eliminated. The TE's own note on the facing page (p. 965) says "eliminate" means
  making 0, and asks for "a coefficient of 1". The item is also keyed "Answers will vary", but Marcus's
  recommendation is simply correct.
- **T5 (TE p. 975).** "The purpose of this task is to consider equations with one or many solutions." The task's
  three equations have infinitely many, none and infinitely many solutions; none of them has exactly one.
- **T6 (TE p. 976, 11.3.3 #4).** The sample answer says "any equation with the same variable term but different
  constant terms" has no solution. That holds only after each side is simplified: 2n + 5 − 1 = 2n + 4 has the same
  variable term, and its constants look different as written, but it is true for every n.
- **T7 (TE p. 953, 11.1.3 #3).** The sample answer gives a rule ("they are on different sides of the equal sign") as
  the reason. The reason is that an operation is applied to both sides: subtracting 6 gives 9 = 9c, not 21 = 9c.
  The facing teacher note states it correctly.
- **T8 (TE p. 979 and p. 983).** The cards are listed as "1 set per group" on p. 979 but given to pairs on p. 983,
  and the cards themselves are not supplied (D11).
- **Typos.** "students' make selections" (p. 973); "or drawing paper" for "on" (p. 974); "false for values" for
  "false for all values" (p. 976).

## 3. Conflicts with the course's settled rules

- **Partner and group work (§1 rule 4; ruling 20).**
  - In the SE: 11.1.3 #3 ("Discuss with your partner"); 11.1.4 #1b and #2b; all of 11.1.5 ("Work with your partner");
    11.2.2 ("Work with your partner", and #4 "Discuss with your partner"); 11.3.2 (choose and solve "with your
    partner"); 11.3.3 (the whole exploration, including #2b, #3 and #4); 11.4.2a; and 11.4.3, whose card sort is a
    pair activity ("Record your partner's name").
  - In the TEs: Think-Pair-Share (pp. 980, 984); tiles "for students to use in pairs" (p. 960); "releasing them to
    student pairs" (pp. 967, 977); small groups (pp. 955, 978, 980); "pairing students to discuss their reflections"
    (p. 985).
- **Video (ruling 31).** The 11.1.1 warm-up is built around the "Problem Solving" video (4:01, TE p. 951).
- **Warm-ups (§16 rule 5).** No warm-up in these lessons is spaced retrieval.
  - 11.1.1 is a discussion of collaboration at work.
  - 11.4.1 is an argument from game statistics (no MA.8.AR.2.1 content).
  - 11.2.1 (hangers) and 11.3.1 (perimeter) preview the day's content.
- **Discovery in first teaching (§16 rule 6).** 11.2.2 Exploration (tiles, "primarily student-directed", TE p. 963)
  and 11.3.3 Exploration both teach by discovery.
- **The word "homework".** Every Homework page's header ("Lesson 1 Homework" … "Lesson 4 Homework"); TE p. 951 ("as
  a homework or extra credit opportunity").
- **Calculator statements (Part 8: nothing about calculators on any page).** HW p. 1 #1 opens with "Use a calculator
  to complete the following." On the teacher side, TE pp. 971, 975 and 982 suggest "allowing" a calculator, which
  frames a standing permission as a per-task one.
- **Benchmark codes on student pages (§1 rule 3).** SE pp. 92–93, 98, 103 and 107 print MA.8.AR.2.1 with its
  statement.
- **Multi-paragraph stems (Part 4 pattern 2; Part 7 rules 5–7).**
  - 11.1.5: three paragraphs plus three bullets before part a.
  - PP p. 1 #1–3 and HW p. 2 #2–4: two paragraphs each.
  - 11.4.2 (Clare): two paragraphs plus a table.
  - 11.1.6 #2 and 11.1.7: the context and the equation in one long sentence.
- **Compound questions to split into (a)/(b) (rule 5).**
  - 11.1.4 #1b: an if/else with two different tasks.
  - 11.1.5b: "Identify … and explain".
  - 11.3.3 #2b: solve, then either show the solution or explain why there is none.
  - 11.4.2a: find, then circle.
  - HW p. 1 #1b: two questions in one.
  - 11.3.4 #1, PP p. 6 and HW p. 6 directions: simplify, then classify.
  - 11.3.2 #2: choose, circle, solve.
- **Mnemonics.** None. The TE explicitly avoids "cancel" (p. 965), which fits Part 5's spirit.
- **Variables (Part 5 prohibition 4).** Compliant. Twenty-two letters are used and none is o, i or l.
- **Names (Part 4 pattern 11).** About twenty-five named people across four lessons. FAST uses three in 36 items.

## 4. What MA.8.AR.2.1 and the state guide expect that these lessons never ask

| Expected (benchmark, B1G-M, FAST) | The book (11.1–11.4) |
|---|---|
| A **negative rational** factor distributed. The state item is −3.5(10x − 2) = −176.75 → x = 5.25 | Negative integers throughout: −2(n − 3), −3(j − 2), −4(2c − 1), −15(1 − g), −(5 − 9y). There is no negative decimal factor anywhere. The only negative fraction, −½(t + 3), is one of nine in 11.3.2, where students choose three |
| Fractional coefficients in **no-solution** equations (the guide's ⅓x − 6 = ⅓(x − 3) − 1) and a decimal no-solution case (0.8x + 1.4 = 0.8x) | Decimal no-solution cases are present (PP p. 8 #8, HW p. 8 #8, cards K and I). Fractional coefficients appear in identities (PP p. 7 #6, HW p. 7 #6, card D). Card L (½ distributed) is the only fractional no-solution equation. No item clears a fraction by multiplying and then lands on a = b |
| **x = 0 as a solution**, distinguished from "no solution": the guide's 2x + 7 = −2x + 7, and the TE's own named misconception (p. 971) | The only items with a solution of 0 are optional (11.3.2: c = 0), worked for the student (HW p. 1 example: a = 0), or left unstated by the key (PP p. 5 #5, D5). No required item asks for x = 0 and keys it |
| The three **solution forms** named: x = a, a = a, a = b | Never named. The keys write the false case as "8 ≠ 5" or "10 ≠ 3" (see §6) |
| **Verify by substitution** | Present in 11.1.4 #1d, 11.2.4, PP/HW pp. 3–4 and 11.4.2c, and as the value grids of 11.3 (PP/HW p. 5 #1 and #3). Absent from all twenty items on the 11.4 practice and homework pages, where eight equations each are solved and none is checked. No-solution and identity verdicts are never confirmed by substitution beyond those grids (and see D4 on them) |
| **Create** an equation with a given number of solutions, or complete one (4x + 3 = 4x + ▢) | Only 11.3.3 #3–4: write one "true for all values" and one "false for all values", as partner work. Nothing asks for a one-solution equation, a missing constant or a missing coefficient |
| **Ugly exact answers** (the state's 15(2x − 10) + 4x = −3(15x + 4) → x = 138/79) | Clare's y = −65/11 is the only required one. 9/4, 13/2 and 1/2 occur. 7/8 and 13/3 appear only as rows to classify, never to solve. Every other answer is an integer or a terminating decimal |
| FAST item shapes: multiselect ("Select all the equations that have no solution"), an "x =" box, a matching grid, a two-dropdown sentence, multiple choice whose distractors are error products (partial distribution, sign) | The 11.3.4 / PP p. 6 / HW p. 6 grids work as a matching grid. 11.1.3 is a two-dropdown sentence. There is no multiselect and no multiple choice. The error-analysis items (Clare, Soledad, Marilu, Elena) carry the right errors and could be recast as distractors |
| Interpreting a solution in context, including a context with no or infinitely many solutions | 11.1.5–11.1.7, PP pp. 1–2 and HW p. 2 give the equation and ask for the value, sometimes with a sentence frame. 11.2–11.4 have no context at all. No context ever has no solution or infinitely many |
| Named misconceptions: distributing to one term only; sign errors in distributing; expecting x = constant always | Partial distribution: Soledad (PP p. 8 #10, as printed in the key). Sign errors: Clare (line 2) and Marilu. The third (expecting x = constant always) is addressed by 11.3 as a whole |

Writing an equation from a context is MA.912.AR.2.1, not MA.8.AR.2.1, so its absence here is not a gap.

## 5. Per lesson

**11.1 Solving Equations (TE pp. 949–959; SE pp. 93–97; PP pp. 1–2; HW pp. 1–2).**
- **Order.** Warm-up on collaboration (video). Like terms: the definitions of term, constant term and like terms, then
  a four-pair matching (SE p. 94). Error analysis of combining terms across the equal sign (two dropdown sentences
  and a discussion). Solving with a choice of first step: 12 = 4(1 + q − 2), with explain, compare, solve, verify;
  then three equations solved two ways. One equation, ¼(c − 2) = 18, solved by three named students' first steps
  (distribute ¼ / a planted error / multiply by 4), then find the error and interpret the answer (74). Two
  given-equation contexts with decimals (tickets; overtime pay). Exit ticket 6(c − 1.50) = 46.50.
- **Vocabulary:** term, constant term, like terms.
- **Shapes:** match lines; dropdown sentence; "solve two ways" tables (PP p. 1 #1–3 and HW p. 2 #2–4: divide first /
  distribute / combine first); a context given with its equation; sentence-frame interpretation.
- **Variables:** on one side only. Coefficients include ¼ and decimals.
- **Sound to reuse:** SE p. 94 #1 (matching); SE p. 95 11.1.4 #1 and all three of #2; SE p. 96 the cookie equation
  (with Elena's column re-described, D2); SE p. 97 11.1.6 #1–2 and 11.1.7; PP pp. 1–2 #1–3, #5–10; HW p. 1 #1
  (without its calculator line); HW p. 2 #2–6.
- **Not as printed:** 11.1.3 (D1: change a number); HW p. 2 #7 (D3).

**11.2 Solving Equations with Variables on Both Sides (TE pp. 960–969; SE pp. 98–103; PP pp. 3–4; HW pp. 3–4).**
- **Order.** Warm-up hangers: A gives 21 + s = 5s + 6, so s = 3.75; B gives 12 + 2p = 2p + 12, an unflagged identity
  that previews 11.3. Algebra-tile tables, each row a picture, a description ("Add ___ to both sides to create zero
  pairs" / "Divide into ___ groups") and an algebraic line: 4x = 2x + 12; 8x + 15 = 4x − 1; and
  6 − 3x = 8 + (−4x) + 2, which ends at −4 = −x with "Marcus" on multiplying by −1. Guided tables, "eliminate the
  constant / the variable term / isolate": 3y − 4 = 6 − 2y, 4(m + 7.2) = −2m − 8.1 (m = −6.15), and
  −12p + 3p − 11 = 14 − 3p − 7. Your Turn: two equations, with substitution. Self-rating scale.
- **Vocabulary:** zero pairs, eliminate, isolate the variable. "Cancel" is avoided on purpose.
- **Shapes:** step tables with the description given; fill-in blanks for the move; solve and verify.
- **Sound to reuse:** both hangers (SE p. 98); 11.2.2 #1–3; 11.2.3 #1–3; 11.2.4 #1–2; PP pp. 3–4 #1–10; HW pp. 3–4
  #1–10 (keys right; fix the HWK p. 4 typo).
- **Note:** the tile pictures in the PP and HW are hard to read in grayscale.

**11.3 Solutions to Linear Equations (TE pp. 970–978; SE pp. 104–107; PP pp. 5–6; HW pp. 5–6).**
- **Order.** Warm-up: triangle (2x, 2x, x − 8) and square (x + 2) with equal perimeters, so x = 16 and both
  perimeters are 72. Nine equations rated "least / most difficult" and three solved with a partner. All nine have
  exactly one solution: −10, −14, −3.5, −¼, 3/2, −2, 3, 3 and 0, with fractions, decimals, a negative fraction factor
  and nested negatives. Evaluation grid: n = n, 3n + 2 = 3n + 1 and 3(n − 2) = 3n − 6 at five values (D4). Solve the
  false one to 2 = 1. Create an always-true and an always-false equation. Definition box. Classification grid,
  simplify then mark one / none / infinitely many: b = 12; identity; none; identity; none. Written cool-down.
- **Vocabulary:** infinitely many solutions, no solution; "structure" (MTR.5.1).
- **Shapes:** "is this value a solution?" yes/no grids (PP and HW #1 and #3); a three-column classification grid;
  claim critique (Samir, Crystal); create an equation.
- **Sound to reuse:** 11.3.1; all nine 11.3.2 equations, as solving items; the 11.3.3 #1 grid as evaluation, not as
  proof; 11.3.4 all five rows; PP p. 5 #1, #3, #5 (key completed, D5); PP p. 6 #6–10; HW p. 5 #1, #3, #5; HW p. 6
  #6–10.
- **Rephrase:** PP/HW #2 and #4 ("based on your work …", D4).

**11.4 Solving Multi-Step Equations (TE pp. 979–985; SE pp. 108–110; PP pp. 7–8; HW pp. 7–8).**
- **Order.** Off-benchmark warm-up arguing from game statistics. Error analysis: Clare's
  12(5 + 2y) = 4y − (5 − 9y), with two errors (D7), corrected to −65/11 and checked. A 12-card sort solved in pairs
  and sorted 4 / 4 / 4 by number of solutions. The cards cover fractions (¼, ½, ¾), decimals (0.60, 1.20, 0.80,
  3.5), a fraction bar and nested negatives. Self-rating table.
- **Vocabulary:** none new.
- **Shapes:** find and circle the error, then correct; solve-then-sort; the PP and HW "solve eight, then place each
  in the one / none / infinite table"; critique of a claimed verdict (Soledad: partial distribution; Marilu: sign
  errors on both sides).
- **Sound to reuse:** Clare (with "two mistakes", D7); cards A–L (with K's line fixed, D8; we supply the cards);
  PP pp. 7–8 #1–9 (keys #3 and #8 fixed, D9–D10); HW pp. 7–8 #1–10.
- **Not as printed:** PP p. 8 #10 (D6).

## 6. Judgment calls

1. **How the keys write the false case.** The keys print "8 ≠ 5", "10 ≠ 3", "−3 ≠ 7" and "2 ≠ 1" as the last line.
   The derived line is the equation 8 = 5, which is false, and that a = b form is what the state guide names.
   Writing ≠ changes the derived equation into a true statement about numbers. Ours should print the false equation
   and then say "false for every value, so no solution". This is not counted as a defect, because the convention is
   common and every verdict is right.
2. **PP p. 8 #10, which equation to keep.** The stem's equation (no solution, Soledad right) and the key's equation
   (an identity, Soledad wrong because she distributed to one term only) are both coherent items. The key's equation
   is the one whose purpose is the named misconception (partial distribution), so if the item is reused it should be
   the key's version, with the student page corrected.
3. **D4 as a defect rather than a style point.** The answers are true. The defect is that the page asks students to
   conclude "no solution" from evidence that cannot show it, and that is exactly the habit the state's third
   misconception feeds. A teacher may prefer to keep the evaluation grids as a warm-up to the idea and draw the
   conclusion only from the simplified form; that is the reading recommended here.

## 7. Inventory and log

| File | Pages read | sympy checks | Flags (all real) |
|---|---|---|---|
| 11.01 TE + SE pp. 93–97 | 16 | 23 | T1 |
| 11.02 TE + SE pp. 98–103 | 16 | 14 | — |
| 11.03 TE + SE pp. 104–107 | 13 | 22 | — |
| 11.04 TE + SE pp. 108–110 | 10 | 23 | D8 |
| Practice Problems + Keys pp. 1–8 (11.1: 10, 11.2: 13, 11.3: 10, 11.4: 14) | 16 | 47 | D6 (two rows), D9, D10 |
| Homework + Keys pp. 1–8 (11.1: 10, 11.2: 13, 11.3: 10, 11.4: 11) | 16 | 44 | D3 |
| **Total** | **87** | **173** (171 work lines, 39 grid cells inside them) | 7 rows flagged |

D1, D2, D4, D5, D7 and D11 are defects of design or wording and were found by reading. Their computations (Kenneth's
c = 1; Clare's two non-equivalent lines; Samir's a = 0) are rows 7, 62–66 and 110 below, where the check agrees with the
printed value and the defect is in what the page says about it.

Items read but not computable: these are open responses, and each "answers will vary" key was read for soundness.
- 11.1.1 #1–2
- 11.1.3 #3
- 11.1.4 #1a–b and #2b
- 11.1.5b
- 11.2.2 #3b and #4
- 11.2.5
- 11.3.2 #1
- 11.3.3 #1b, #2a, #3 and #4
- 11.3.5
- 11.4.1 #1–2 (the table facts are checked in row 60)
- 11.4.4
- PP p. 1 #4
- HW p. 1 #1b and p. 2 #5
- the explanation keys of PP p. 5 #5, HW p. 5 #5, PP p. 8 #10 and HW p. 8 #10

Log (generated by `/tmp/mn_check/check_u11_part1.py`). "Work lines" are the printed key or student lines, each
tested for having the same solution set as the item's equation. Rows flagged by the script carry a verdict other
than "match".

| # | Lesson | Source | Page | Item | Equation / expression as read | sympy | Key / printed | Verdict | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 11.1 | SE p.94 / TE p.952 | 952 | 11.1.2 #1 | 10p like -3p | True | True | match | TE lines A-III, B-II, C-IV, D-I |
| 2 | 11.1 | SE p.94 / TE p.952 | 952 | 11.1.2 #1 | 12m^3 like 13m^3 | True | True | match | TE lines A-III, B-II, C-IV, D-I |
| 3 | 11.1 | SE p.94 / TE p.952 | 952 | 11.1.2 #1 | f like 7f | True | True | match | TE lines A-III, B-II, C-IV, D-I |
| 4 | 11.1 | SE p.94 / TE p.952 | 952 | 11.1.2 #1 | -64 like -1 | True | True | match | TE lines A-III, B-II, C-IV, D-I |
| 5 | 11.1 | SE p.94 / TE p.953 | 953 | 11.1.3 (stem) | 15 = 3c + 6 + 6c | 1 | 1 | match |  |
| 6 | 11.1 | TE p.953 | 953 | 11.1.3 #1 Jayla | 15 = 9c + 6 | 1 | 1 | match | equivalent to stem: Jayla "is correct" |
| 7 | 11.1 | TE p.953 | 953 | 11.1.3 #2 Kenneth | 15 = 15c | 1 | 1 | match | Kenneth's WRONG combination also gives c = 1 (see D1) |
| 8 | 11.1 | TE p.953 | 953 | 11.1.3 #3 "add 15 and 6" | 21 = 9c | 7/3 | 7/3 | match | not equivalent to stem (c = 1): key "No" is right |
| 9 | 11.1 | SE p.95 / TE p.954 | 954 | 11.1.4 #1c | 12 = 4(1 + q - 2) | 4 | 4 | match |  |
| 10 | 11.1 | TE p.954 | 954 | 11.1.4 #1d substitution | 4*(1+4-2) | 12 | 12 | match |  |
| 11 | 11.1 | SE p.95 / TE p.955 | 955 | 11.1.4 #2 (1st) | 12 = 12(-2 - z + 5) | 2 | 2 | match | 3 work lines: all equivalent |
| 12 | 11.1 | TE p.955 | 955 | 11.1.4 #2 (2nd) | 2w + 9 - 5w = -3 | 4 | 4 | match | 2 work lines: all equivalent |
| 13 | 11.1 | TE p.955 | 955 | 11.1.4 #2 (3rd) | 13 = g + 2(g - 4) | 7 | 7 | match | 3 work lines: all equivalent |
| 14 | 11.1 | TE p.955 teacher note | 955 | 11.1.4 note "divide all terms by 2" | 7.5 = g/2 + g - 4 | 23/3 | 7 | ANSWER WRONG | TE says this is the original divided by 2; true halving is 6.5 = g/2 + g - 4 (see T1) |
| 15 | 11.1 | check | 955 | 11.1.4 note, corrected | 6.5 = g/2 + g - 4 | 7 | 7 | match |  |
| 16 | 11.1 | SE p.96 / TE p.956 | 956 | 11.1.5 equation | 1/4(c - 2) = 18 | 74 | 74 | match | 4 work lines: all equivalent Joel and Nichele columns |
| 17 | 11.1 | TE p.956 | 956 | 11.1.5 Elena (intended error) | 1/4(c - 2 + 2) = 18 + 2 | 80 | 80 | match | 1 work lines: all equivalent not equivalent to the stem: the planted error |
| 18 | 11.1 | context | 956 | 11.1.5 context | 4*18 + 2 | 74 | 74 | match | four plates of a dozen and a half, plus 2 |
| 19 | 11.1 | TE p.956 | 956 | 11.1.5 Joel 18 2/4 = 74/4 | 18 + 2/4 | 37/2 | 74/4 | match |  |
| 20 | 11.1 | SE p.97 / TE p.958 | 958 | 11.1.6 #1 | 54.45 = 9.50t + 25.95 | 3 | 3 | match | 1 work lines: all equivalent |
| 21 | 11.1 | TE p.958 | 958 | 11.1.6 #2 | p(40 + 7.5) = 1306.25 | 55/2 | 27.50 | match | 1 work lines: all equivalent |
| 22 | 11.1 | context | 958 | 11.1.6 #2 model | 40p + 5(1.5p) = 1306.25 | 55/2 | 27.50 | match | 45 h = 40 regular + 5 at 1.5x: the given equation models the story |
| 23 | 11.1 | SE p.97 / TE p.959 | 959 | 11.1.7 | 6(c - 1.50) = 46.50 | 37/4 | 9.25 | match | 1 work lines: all equivalent |
| 24 | 11.2 | SE p.98 / TE p.962 | 962 | 11.2.1 Hanger A (read from figure) | 3 + 6 + 6 + s + 6 = s + s + s + s + 6 + s | 15/4 | 3.75 | match | 2 work lines: all equivalent |
| 25 | 11.2 | SE p.98 / TE p.962 | 962 | 11.2.1 Hanger B (read from figure) | 6 + 6 + p + p = p + p + 3 + 3 + 6 | infinitely many | infinitely many | match | 1 work lines: all equivalent |
| 26 | 11.2 | SE p.99 / TE p.963 | 963 | 11.2.2 #1 | 4x = 2x + 12 | 6 | 6 | match | 1 work lines: all equivalent blanks: -2x, 2 |
| 27 | 11.2 | SE p.99 / TE p.964 | 964 | 11.2.2 #2 | 8x + 15 = 4x - 1 | -4 | -4 | match | 2 work lines: all equivalent blanks: -4x, -15, 4; tile counts 15 and 16 checked on the image |
| 28 | 11.2 | SE p.100 / TE p.965-966 | 965 | 11.2.2 #3 | 6 - 3x = 8 + (-4x) + 2 | 4 | 4 | match | 3 work lines: all equivalent |
| 29 | 11.2 | SE p.101 / TE p.967 | 967 | 11.2.3 #1 | 3y - 4 = 6 - 2y | 2 | 2 | match | 2 work lines: all equivalent |
| 30 | 11.2 | TE p.967 | 967 | 11.2.3 #2 | 4(m + 7.2) = -2m - 8.1 | -123/20 | -6.15 | match | 3 work lines: all equivalent |
| 31 | 11.2 | SE p.102 / TE p.967 | 967 | 11.2.3 #3 | -12p + 3p - 11 = 14 - 3p - 7 | -3 | -3 | match |  |
| 32 | 11.2 | SE p.102 / TE p.968 | 968 | 11.2.4 #1 | 6 - x = 5x + 30 | -4 | -4 | match |  |
| 33 | 11.2 | TE p.968 | 968 | 11.2.4 #1 substitution (both sides) | 6-(-4) | 10 | 10 | match |  |
| 34 | 11.2 | TE p.968 | 968 | 11.2.4 #1 substitution RHS | 5*(-4)+30 | 10 | 10 | match |  |
| 35 | 11.2 | SE p.102 / TE p.968 | 968 | 11.2.4 #2 | 9(p - 4) = 3(2p + 6) | 18 | 18 | match |  |
| 36 | 11.2 | TE p.968 | 968 | 11.2.4 #2 substitution | 9*(18-4) | 126 | 126 | match |  |
| 37 | 11.2 | TE p.968 | 968 | 11.2.4 #2 substitution RHS | 3*(2*18+6) | 126 | 126 | match |  |
| 38 | 11.3 | SE p.104 / TE p.972 | 972 | 11.3.1 b | 4(x + 2) = 2x + 2x + x - 8 | 16 | 16 | match | 1 work lines: all equivalent |
| 39 | 11.3 | TE p.972 | 972 | 11.3.1 c triangle | 2*16+2*16+16-8 | 72 | 72 | match |  |
| 40 | 11.3 | TE p.972 | 972 | 11.3.1 c square | 4*(16+2) | 72 | 72 | match |  |
| 41 | 11.3 | check | 972 | 11.3.1 triangle 32-32-8 exists | triangle inequality 32+8>32, 32+32>8 | True | True | match |  |
| 42 | 11.3 | SE p.104 / TE p.974 | 974 | 11.3.2 eq 1 | -1/2(t + 3) - 10 = -6.5 | -10 | -10 | match |  |
| 43 | 11.3 | SE p.104 / TE p.974 | 974 | 11.3.2 eq 2 | (10 - v)/4 = 2(v + 17) | -14 | -14 | match |  |
| 44 | 11.3 | SE p.104 / TE p.974 | 974 | 11.3.2 eq 3 | n/7 - 12 = 5n + 5 | -7/2 | -3.5 | match |  |
| 45 | 11.3 | SE p.104 / TE p.974 | 974 | 11.3.2 eq 4 | (4m - 3)/4 = -(9 + 4m)/8 | -1/4 | -1/4 | match |  |
| 46 | 11.3 | SE p.104 / TE p.974 | 974 | 11.3.2 eq 5 | 2r + 49 = -8(-r - 5) | 3/2 | 3/2 | match |  |
| 47 | 11.3 | SE p.104 / TE p.974 | 974 | 11.3.2 eq 6 | p - 5(p + 4) = p - (8 - p) | -2 | -2 | match |  |
| 48 | 11.3 | SE p.104 / TE p.974 | 974 | 11.3.2 eq 7 | 2(2q + 1.5) = 18 - q | 3 | 3 | match |  |
| 49 | 11.3 | SE p.104 / TE p.974 | 974 | 11.3.2 eq 8 | 2(4k + 3) - 13 = 2(18 - k) - 13 | 3 | 3 | match |  |
| 50 | 11.3 | SE p.104 / TE p.974 | 974 | 11.3.2 eq 9 | 3(c - 1) + 2(3c + 1) = -(3c + 1) | 0 | 0 | match |  |
| 51 | 11.3 | SE p.105 / TE p.975 | 975 | 11.3.3 #1a row 1 | n = n at -10, -5, 0, 5, 10 | T, T, T, T, T | T, T, T, T, T | match |  |
| 52 | 11.3 | SE p.105 / TE p.975 | 975 | 11.3.3 #1a row 2 | 3n + 2 = 3n + 1 at -10, -5, 0, 5, 10 | F, F, F, F, F | F, F, F, F, F | match |  |
| 53 | 11.3 | SE p.105 / TE p.975 | 975 | 11.3.3 #1a row 3 | 3(n - 2) = 3n - 6 at -10, -5, 0, 5, 10 | T, T, T, T, T | T, T, T, T, T | match |  |
| 54 | 11.3 | SE p.106 / TE p.976 | 976 | 11.3.3 #2b | 3n + 2 = 3n + 1 | no solution | no solution | match | key derives 2 = 1, prints "2 ≠ 1" |
| 55 | 11.3 | SE p.106 / TE p.977 | 977 | 11.3.4 #1 row 1 | 5(b + 3) = -9 + 7b | 12 | 12 | match | 1 work lines: all equivalent TE marks only the category; "one" keyed, value computed here |
| 56 | 11.3 | SE p.106 / TE p.977 | 977 | 11.3.4 #1 row 2 | 2(3c + 3) = 3(2c + 2) | infinitely many | infinitely many | match | 1 work lines: all equivalent |
| 57 | 11.3 | SE p.106 / TE p.977 | 977 | 11.3.4 #1 row 3 | 8(13 + r) = 48 + 8r | no solution | no solution | match | 1 work lines: all equivalent |
| 58 | 11.3 | SE p.106 / TE p.977 | 977 | 11.3.4 #1 row 4 | 3a - 5 = 9 + 3a - 14 | infinitely many | infinitely many | match | 1 work lines: all equivalent |
| 59 | 11.3 | SE p.106 / TE p.977 | 977 | 11.3.4 #1 row 5 | -12s + 14 = -2(6s + 7) | no solution | no solution | match | 1 work lines: all equivalent |
| 60 | 11.4 | SE p.108 / TE p.981 | 981 | 11.4.1 | Michelle's average 5,817 > Dave's 5,126; Dave's high 8,931 > 6,751 and latest 7,915 > 5,284 | True | True | match |  |
| 61 | 11.4 | SE p.108 / TE p.982 | 982 | 11.4.2 b (corrected) | 12(5 + 2y) = 4y - (5 - 9y) | -65/11 | -65/11 | match | 4 work lines: all equivalent |
| 62 | 11.4 | SE p.108 / TE p.982 | 982 | 11.4.2 Clare line 2 vs line 1 | 60 + 24y = 4y - 5 - 9y | NOT equivalent | TE circles | match | Clare's planted errors are exactly lines 2 and 4: TWO errors (see D7) |
| 63 | 11.4 | SE p.108 / TE p.982 | 982 | 11.4.2 Clare line 3 vs line 2 | 60 + 24y = -5y - 5 | equivalent | not circled | match |  |
| 64 | 11.4 | SE p.108 / TE p.982 | 982 | 11.4.2 Clare line 4 vs line 3 | 24y = -5y - 55 | NOT equivalent | TE circles | match | Clare's planted errors are exactly lines 2 and 4: TWO errors (see D7) |
| 65 | 11.4 | SE p.108 / TE p.982 | 982 | 11.4.2 Clare line 5 vs line 4 | 29y = -55 | equivalent | not circled | match |  |
| 66 | 11.4 | SE p.108 / TE p.982 | 982 | 11.4.2 Clare line 6 vs line 5 | y = -55/29 | equivalent | not circled | match |  |
| 67 | 11.4 | TE p.982 | 982 | 11.4.2 c substitution LHS | 12*(5+2*(-65/11)) | -900/11 | -900/11 | match |  |
| 68 | 11.4 | TE p.982 | 982 | 11.4.2 c substitution RHS | 4*(-65/11)-(5-9*(-65/11)) | -900/11 | -900/11 | match |  |
| 69 | 11.4 | TE p.983-984 (cards only in TE key) | 983 | 11.4.3 card A | 15g + 1 = -15(1 - g) | no solution | no solution | match | 1 work lines: all equivalent |
| 70 | 11.4 | TE p.983-984 (cards only in TE key) | 983 | 11.4.3 card B | 5 + 8x + x = 4x + 30 | 5 | 5 | match | 3 work lines: all equivalent |
| 71 | 11.4 | TE p.983-984 (cards only in TE key) | 983 | 11.4.3 card C | y - 3(2 - 3y) = 2(5y + 1) | no solution | no solution | match | 2 work lines: all equivalent |
| 72 | 11.4 | TE p.983-984 (cards only in TE key) | 983 | 11.4.3 card D | 1/4(12 - 4d) = 3 - d | infinitely many | infinitely many | match | 1 work lines: all equivalent |
| 73 | 11.4 | TE p.983-984 (cards only in TE key) | 983 | 11.4.3 card E | (15t - 10)/5 = 3t - 2 | infinitely many | infinitely many | match | 1 work lines: all equivalent |
| 74 | 11.4 | TE p.983-984 (cards only in TE key) | 983 | 11.4.3 card F | 4(2c - 2) - 4 = 4(c - 2) | 1 | 1 | match | 4 work lines: all equivalent |
| 75 | 11.4 | TE p.983-984 (cards only in TE key) | 983 | 11.4.3 card G | 8 + 2n = -3.5n + 19 | 2 | 2 | match | 2 work lines: all equivalent |
| 76 | 11.4 | TE p.983-984 (cards only in TE key) | 983 | 11.4.3 card H | 3(3j + 2) - 2j = 7j + 6 | infinitely many | infinitely many | match | 2 work lines: all equivalent |
| 77 | 11.4 | TE p.983-984 (cards only in TE key) | 983 | 11.4.3 card I | -12 + 0.60*(2*e - 5) = 1.20*e - 15 | infinitely many | infinitely many | match | 2 work lines: all equivalent |
| 78 | 11.4 | TE p.983-984 (cards only in TE key) | 983 | 11.4.3 card J | 1/2 b - 3 = 2 - 3/4 b | 4 | 4 | match | 2 work lines: all equivalent |
| 79 | 11.4 | TE p.983-984 (cards only in TE key) | 983 | 11.4.3 card K | 0.80s - 3 = 7 + s - 0.20s | no solution | no solution | match | 1 work lines: all equivalent |
| 80 | 11.4 | TE p.983-984 (cards only in TE key) | 983 | 11.4.3 card L | 4(m - 1) = 1/2(8m - 2) | no solution | no solution | match | 1 work lines: all equivalent |
| 81 | 11.4 | TE p.984 | 984 | 11.4.3 card K line 2 is the simplified line 1 | line 1 sides: 0.8s - 3 / 0.8s + 7;  printed: -0.8s - 3 / 7 - 0.8s | False | True | CLAIM FALSE | both variable terms carry the wrong sign; verdict "no solution" still right (see D8) |
| 82 | 11.4 | TE p.984 | 984 | 11.4.3 #4 sort | One: BFGJ  None: ACKL  Infinite: DEHI | True | True | match |  |
| 83 | 11.1 | Practice + Key p.1 | PP 1 | #1 Landry | 6(p + p + 11) = 162 | 8 | 8 | match | 3 work lines: all equivalent |
| 84 | 11.1 | Practice + Key p.1 | PP 1 | #2 Chiara | 6(p + p + 11) = 162 | 8 | 8 | match | 3 work lines: all equivalent |
| 85 | 11.1 | Practice + Key p.1 | PP 1 | #3 Roy | 6(p + p + 11) = 162 | 8 | 8 | match | 3 work lines: all equivalent |
| 86 | 11.1 | Practice + Key p.1 | PP 1 | #5 notebooks | 8+11 | 19 | 19 | match |  |
| 87 | 11.1 | Practice + Key p.1 | PP 1 | #6 | 0.25q + 0.10q + 3(0.05) = 1.90 | 5 | 5 | match | 2 work lines: all equivalent |
| 88 | 11.1 | context | PP 1 | #6 coins | 5*0.25+5*0.10+3*0.05 | 19/10 | 1.90 | match |  |
| 89 | 11.1 | Practice + Key p.2 | PP 2 | #7 | 2(4) + 3p + 1(7) = 30 | 5 | 5 | match | 3 work lines: all equivalent |
| 90 | 11.1 | Practice + Key p.2 | PP 2 | #8 | 4(t - 1.75) + 18.89 = 52.09 | 201/20 | 10.05 | match | 3 work lines: all equivalent |
| 91 | 11.1 | Practice + Key p.2 | PP 2 | #9 | 140 + 21.40h = 214.90 | 7/2 | 3.5 | match | 1 work lines: all equivalent |
| 92 | 11.1 | Practice + Key p.2 | PP 2 | #10 | 6(a + 9.75 + 3.80) = 153.30 | 12 | 12 | match | 3 work lines: all equivalent |
| 93 | 11.2 | Practice + Key p.3 | PP 3 | #1-2 tiles | 4x - 3 = x + 9 | 4 | 4 | match | 2 work lines: all equivalent blanks -x, 3, 3; tile counts (3 and 9; 12) checked on image |
| 94 | 11.2 | Practice + Key p.4 | PP 4 | #3 | 5(1.2m - 0.3) = -2m + 1.7 | 2/5 | 0.4 | match | 3 work lines: all equivalent |
| 95 | 11.2 | Practice + Key p.4 | PP 4 | #4 substitution LHS | 5*(1.2*0.4-0.3) | 9/10 | 0.9 | match |  |
| 96 | 11.2 | Practice + Key p.4 | PP 4 | #4 substitution RHS | -2*0.4+1.7 | 9/10 | 0.9 | match |  |
| 97 | 11.2 | Practice + Key p.4 | PP 4 | #5 | 8 - k = 3k + 20 | -3 | -3 | match | 2 work lines: all equivalent |
| 98 | 11.2 | Practice + Key p.4 | PP 4 | #6 substitution | 8-(-3) | 11 | 11 | match |  |
| 99 | 11.2 | Practice + Key p.4 | PP 4 | #6 substitution RHS | 3*(-3)+20 | 11 | 11 | match |  |
| 100 | 11.2 | Practice + Key p.4 | PP 4 | #7 | 4(s - 5) = 9s + 25 | -9 | -9 | match | 3 work lines: all equivalent |
| 101 | 11.2 | Practice + Key p.4 | PP 4 | #8 substitution | 4*(-9-5) | -56 | -56 | match |  |
| 102 | 11.2 | Practice + Key p.4 | PP 4 | #8 substitution RHS | 9*(-9)+25 | -56 | -56 | match |  |
| 103 | 11.2 | Practice + Key p.4 | PP 4 | #9 | 3(1 - 3p) = 6(p - 7) | 3 | 3 | match | 3 work lines: all equivalent |
| 104 | 11.2 | Practice + Key p.4 | PP 4 | #10 substitution | 3*(1-3*3) | -24 | -24 | match |  |
| 105 | 11.2 | Practice + Key p.4 | PP 4 | #10 substitution RHS | 6*(3-7) | -24 | -24 | match |  |
| 106 | 11.3 | Practice + Key p.5 | PP 5 | #1 | 2k + 1 = k + k + 1 at 0, 0.5, 1, -1, 8, -3 | T, T, T, T, T, T | T, T, T, T, T, T | match |  |
| 107 | 11.3 | Practice + Key p.5 | PP 5 | #2 | 2k + 1 = k + k + 1 | infinitely many | infinitely many | match |  |
| 108 | 11.3 | Practice + Key p.5 | PP 5 | #3 | 8m + 1 = 2(4m + 1) at 0, 8, -1, 4, -0.5, -4 | F, F, F, F, F, F | F, F, F, F, F, F | match |  |
| 109 | 11.3 | Practice + Key p.5 | PP 5 | #4 | 8m + 1 = 2(4m + 1) | no solution | no solution | match |  |
| 110 | 11.3 | Practice + Key p.5 | PP 5 | #5 Samir | 4a + 1 = 4a + 1 + a | 0 | (no key) | match | key: "No ... 5a + 1": right, but never states the one solution a = 0 |
| 111 | 11.3 | Practice + Key p.6 | PP 6 | #6 | 3f + 14 = 9 + 3f + 5 | infinitely many | infinitely many | match | 1 work lines: all equivalent |
| 112 | 11.3 | Practice + Key p.6 | PP 6 | #7 | 5(2h + 3) = 10h + 3 | no solution | no solution | match | 1 work lines: all equivalent |
| 113 | 11.3 | Practice + Key p.6 | PP 6 | #8 | 3b + b - 9 = 2b + 2b + 9 | no solution | no solution | match | 1 work lines: all equivalent |
| 114 | 11.3 | Practice + Key p.6 | PP 6 | #9 | 3(-4j + 1) = 5(-4j + 2) | 7/8 | 7/8 | match | 1 work lines: all equivalent keyed "one solution"; value computed here |
| 115 | 11.3 | Practice + Key p.6 | PP 6 | #10 | 3y + 12 + y = 4(y + 3) | infinitely many | infinitely many | match | 1 work lines: all equivalent |
| 116 | 11.4 | Practice + Key p.7 | PP 7 | #1 | -2(n - 3) = -2n + 6 | infinitely many | infinitely many | match | 1 work lines: all equivalent |
| 117 | 11.4 | Practice + Key p.7 | PP 7 | #2 | 5y + 8 - 2y = 4y - y + 5 | no solution | no solution | match | 1 work lines: all equivalent |
| 118 | 11.4 | Practice + Key p.7 | PP 7 | #3 | 4 - 3(j - 2) = 3(-j - 1) | no solution | no solution | match | 1 work lines: all equivalent |
| 119 | 11.4 | Practice + Key p.7 | PP 7 | #3 key line "4 + 6 = -3" then "10 ≠ 3": right side | 3*(-1) | -3 | 3 | VALUE WRONG | the right side is -3, so the printed "10 ≠ 3" should read 10 = -3 (false) (see D9) |
| 120 | 11.4 | Practice + Key p.7 | PP 7 | #4 | 3.5(2m + 8) = 9 + 3m - 1 | -5 | -5 | match | 3 work lines: all equivalent |
| 121 | 11.4 | Practice + Key p.7 | PP 7 | #5 | (6h + 1)/4 = 2h - 3 | 13/2 | 13/2 | match | 2 work lines: all equivalent |
| 122 | 11.4 | Practice + Key p.7 | PP 7 | #6 | 2/3(12a + 9) = 2(4a + 3) | infinitely many | infinitely many | match | 1 work lines: all equivalent |
| 123 | 11.4 | Practice + Key p.8 | PP 8 | #7 | 1/2 w + 3 = 3/4 w - 4 | 28 | 28 | match | 2 work lines: all equivalent |
| 124 | 11.4 | Practice + Key p.8 | PP 8 | #8 | 0.6(3k + 1) - 0.1k = k + 1.8 + 0.7k | no solution | no solution | match | 2 work lines: all equivalent |
| 125 | 11.4 | Practice + Key p.8 | PP 8 | #8 key "0.8 ≠ 1.8": left constant after -1.7k | 0.6 | 3/5 | 0.8 | VALUE WRONG | left constant is 0.6, not 0.8 (see D10) |
| 126 | 11.4 | Practice + Key p.8 | PP 8 | #9 sort | One: 4,5,7  None: 2,3,8  Infinite: 1,6 | True | True | match | from rows above |
| 127 | 11.4 | Practice p.8 (student page) | PP 8 | #10 equation AS PRINTED ON STUDENT PAGE | 3(2g - 11) = 5g + g - 11 | no solution | infinitely many | ANSWER WRONG | key says "I do not agree ... infinite"; the student page's equation has NO solution, so Soledad's claim is TRUE (see D6) |
| 128 | 11.4 | Practice Key p.8 | PP 8 | #10 equation as printed in KEY and in Soledad's work | 3(2g - 15) = 5g + g - 45 | infinitely many | infinitely many | match | 1 work lines: all equivalent |
| 129 | 11.4 | Practice p.8 | PP 8 | #10 student stem equals Soledad's first line | 3(2g-11)=6g-11  vs  3(2g-15)=6g-45 | False | True | CLAIM FALSE | the stem and the work are different equations |
| 130 | 11.1 | Homework + Key p.1 | HW 1 | #1 example row | 20 = 10(a + 2) | 0 | 0 | match | 3 work lines: all equivalent |
| 131 | 11.1 | Homework + Key p.1 | HW 1 | #1a row 2 | -2 = -8(x - 2) | 9/4 | 9/4 | match | 3 work lines: all equivalent |
| 132 | 11.1 | Homework + Key p.1 | HW 1 | #1a row 3 | 1500(x - 1) = -6000 | -3 | -3 | match | 3 work lines: all equivalent |
| 133 | 11.1 | Homework + Key p.2 | HW 2 | #2 Demarcus | 3(d + d + 7) = 111 | 15 | 15 | match | 3 work lines: all equivalent |
| 134 | 11.1 | Homework + Key p.2 | HW 2 | #3 Brother | 3(d + d + 7) = 111 | 15 | 15 | match | 3 work lines: all equivalent |
| 135 | 11.1 | Homework + Key p.2 | HW 2 | #4 Banker | 3(d + d + 7) = 111 | 15 | 15 | match | 3 work lines: all equivalent |
| 136 | 11.1 | Homework + Key p.2 | HW 2 | #6 brother | 15+7 | 22 | 22 | match |  |
| 137 | 11.1 | Homework + Key p.2 | HW 2 | #7 | 0.10c + 0.05c + 0.12 = 1.47 | 9 | 9 | match | 2 work lines: all equivalent key writes d for c |
| 138 | 11.1 | context | HW 2 | #7 "number of coins she has" (the question asked) | 9+9+12 | 30 | 9 | VALUE WRONG | she has 30 coins; c = 9 is the number of dimes (see D3) |
| 139 | 11.1 | context | HW 2 | #7 coin value check | 9*0.10+9*0.05+12*0.01 | 147/100 | 1.47 | match |  |
| 140 | 11.2 | Homework + Key p.3 | HW 3 | #1-2 tiles | 6x - 5 = 2x + 11 | 4 | 4 | match | 2 work lines: all equivalent blanks -2x, 5, 4; tile counts (5, 11; 16) checked on image |
| 141 | 11.2 | Homework + Key p.4 | HW 4 | #3 | 3(2m - 0.4) = -m + 0.9 | 3/10 | 0.3 | match | 3 work lines: all equivalent |
| 142 | 11.2 | Homework + Key p.4 | HW 4 | #4 substitution LHS | 3*(2*0.3-0.4) | 3/5 | 0.6 | match |  |
| 143 | 11.2 | Homework + Key p.4 | HW 4 | #4 substitution RHS | -(0.3)+0.9 | 3/5 | 0.6 | match |  |
| 144 | 11.2 | Homework + Key p.4 | HW 4 | #5 | 9 - h = 2h + 3 | 2 | 2 | match | 1 work lines: all equivalent |
| 145 | 11.2 | Homework + Key p.4 | HW 4 | #6 substitution | 9-2 | 7 | 7 | match |  |
| 146 | 11.2 | Homework + Key p.4 | HW 4 | #6 substitution RHS | 2*2+3 | 7 | 7 | match |  |
| 147 | 11.2 | Homework + Key p.4 | HW 4 | #7 | 5(j - 3) = 8j + 9 | -8 | -8 | match | 2 work lines: all equivalent |
| 148 | 11.2 | Homework + Key p.4 | HW 4 | #8 substitution | 5*(-8-3) | -55 | -55 | match |  |
| 149 | 11.2 | Homework + Key p.4 | HW 4 | #8 substitution RHS | 8*(-8)+9 | -55 | -55 | match |  |
| 150 | 11.2 | Homework + Key p.4 | HW 4 | #9 | -2(y + 1) = 3(y - 14) | 8 | 8 | match | 2 work lines: all equivalent |
| 151 | 11.2 | Homework + Key p.4 | HW 4 | #10 substitution | -2*(8+1) | -18 | -18 | match |  |
| 152 | 11.2 | Homework + Key p.4 | HW 4 | #10 substitution RHS | 3*(8-14) | -18 | -18 | match |  |
| 153 | 11.3 | Homework + Key p.5 | HW 5 | #1 | 2j + 1 = 2j - 1 at 0, 0.5, 1, -1, 12, -2 | F, F, F, F, F, F | F, F, F, F, F, F | match |  |
| 154 | 11.3 | Homework + Key p.5 | HW 5 | #2 | 2j + 1 = 2j - 1 | no solution | no solution | match |  |
| 155 | 11.3 | Homework + Key p.5 | HW 5 | #3 | 4h + 10 = 2(2h + 5) at 0, 8.5, -1, 4, -0.5, -3 | T, T, T, T, T, T | T, T, T, T, T, T | match |  |
| 156 | 11.3 | Homework + Key p.5 | HW 5 | #4 | 4h + 10 = 2(2h + 5) | infinitely many | infinitely many | match |  |
| 157 | 11.3 | Homework + Key p.5 | HW 5 | #5 Crystal | 6x + 2 = 2(3x + 1) | infinitely many | infinitely many | match |  |
| 158 | 11.3 | Homework + Key p.6 | HW 6 | #6 | 5h + 3 = 3 + 5h - 4 | no solution | no solution | match | 1 work lines: all equivalent |
| 159 | 11.3 | Homework + Key p.6 | HW 6 | #7 | 2(4y + 3) = 8y + 6 | infinitely many | infinitely many | match | 1 work lines: all equivalent |
| 160 | 11.3 | Homework + Key p.6 | HW 6 | #8 | 3a + 2a - 9 = a + a + 4 | 13/3 | 13/3 | match | 1 work lines: all equivalent keyed "one solution"; value computed here |
| 161 | 11.3 | Homework + Key p.6 | HW 6 | #9 | 3(8 - 4j) = 6(-2j + 4) | infinitely many | infinitely many | match | 1 work lines: all equivalent |
| 162 | 11.3 | Homework + Key p.6 | HW 6 | #10 | 7z + 5 - z = 6(z + 5) | no solution | no solution | match | 1 work lines: all equivalent |
| 163 | 11.4 | Homework + Key p.7 | HW 7 | #1 | -3(1 - j) = 3j + 1 | no solution | no solution | match | 1 work lines: all equivalent |
| 164 | 11.4 | Homework + Key p.7 | HW 7 | #2 | 6a + 1 - 2a + 4 = a - 10 | -5 | -5 | match | 3 work lines: all equivalent |
| 165 | 11.4 | Homework + Key p.7 | HW 7 | #3 | 7 - 2(z - 1) = 2(-z + 4) | no solution | no solution | match | 2 work lines: all equivalent |
| 166 | 11.4 | Homework + Key p.7 | HW 7 | #4 | 0.5(4m + 10) = m + m - 2 | no solution | no solution | match | 1 work lines: all equivalent |
| 167 | 11.4 | Homework + Key p.7 | HW 7 | #5 | (4y + 9)/3 = 5y - 8 | 3 | 3 | match | 4 work lines: all equivalent |
| 168 | 11.4 | Homework + Key p.7 | HW 7 | #6 | 3/4(8k + 12) = 2(3k + 4) + 1 | infinitely many | infinitely many | match | 2 work lines: all equivalent |
| 169 | 11.4 | Homework + Key p.8 | HW 8 | #7 | 5 + 1/2 b = 3/8 b + 1 | -32 | -32 | match | 2 work lines: all equivalent |
| 170 | 11.4 | Homework + Key p.8 | HW 8 | #8 | 0.3(4h + 9) + 0.4h = h + 2.4 + 0.6h | no solution | no solution | match | 2 work lines: all equivalent |
| 171 | 11.4 | Homework + Key p.8 | HW 8 | #9 sort | One: 2,5,7  None: 1,3,4,8  Infinite: 6 | True | True | match | from rows above |
| 172 | 11.4 | Homework + Key p.8 | HW 8 | #10 Marilu (corrected) | 3 - 4(2c - 1) = 10c - 2c - 1 | 1/2 | 1/2 | match | 4 work lines: all equivalent |
| 173 | 11.4 | Homework + Key p.8 | HW 8 | #10 Marilu's printed line 2 is equivalent to the stem | 3 - 8c - 4 = -10c + 2c - 1 | False | False | match | planted errors (both sides), as the key says |


---

# Part 2 · A7 Unit 11 — Systems of Equations (11.05–11.08 and the unit test) — Audit, part 2

Scope: Math Nation Grade 7 Accelerated Unit 11, lessons 11.05–11.08 (Teacher Editions, Student Edition pp. 110–131,
Practice and Homework with keys, 2 pages each per lesson) and the whole unit test (Assessment, Key, Guide) plus the
one-page Worked Examples. 124 pages were rendered and viewed. Every system was solved exactly in sympy. Every candidate
ordered pair was substituted into both equations. Every printed graph was checked against its equations: most were read
at 300–900 dpi off two lattice points; the key and test graphs were also fitted by pixel calibration (axis and gridline
detection, then a least-squares fit of the drawn line's pixels). Benchmarks were read in `Florida BEST Grade 8 - Source
of Truth.md` (MA.8.AR.4.1–4.3, Parts 2, 4–8) and `A7 B1G-M Reading Notes.md` (AR.2.1, AR.4.1–4.3). No Math Nation
page is in the repository; items are described in our words, quoting only a few words. Page numbers are the SE/TE
printed numbers, or "L5 p1" (lesson, page within the lesson's two pages) for the practice and homework files.

**14 November 2026.** 109 logged checks (§7) across 124 pages. Every final answer the book keys is right except one
(Worked Examples #4). The defects are in the worked lines, the key graphs, one test-key stem, the guide's notes, the
grids and the contexts.

Course context that drives §3: in this course Unit 11 comes **before** Unit 10 (slope, y = mx + b) and before Unit 7
(graphing proportional relationships). Students will graph every line from a table of values. The book assumes
slope and y-intercept throughout, and its TE says so outright ("Students graphed equations in Unit 10", TE p. 1014).

## 1. Student-facing defects and key errors

Numbered E1–E18. None is to be reproduced in our materials.

| # | Where | Says | True | Evidence |
|---|---|---|---|---|
| E1 | Assessment **Key** p. 6, Q12 stem | The key's stem gives Tank 1 as y = 10 − 2x and Tank 2 as 6x + 3y = 30. The same page's part a, and the student test, use y = 10 − 2.5x and y = −(5/2)x + 10. | The key stem is from another version of the item. Its own system is y = 10 − 2x twice (6x + 3y = 30 ⇔ y = 10 − 2x), so it is not the system graphed beside it. It is also in **standard form**, which is out of scope. The keyed answers (same slope; infinitely many) are right for the test as printed. | text and render of key p. 6 against test p. 8 |
| E2 | Worked Examples #4 | Solves y = −½x + 5 and y = −¼x + 6. Step 1 gets x = −4 (right). Step 2 writes y = ½(−4) + 5 = 3, dropping the sign. | **(−4, 7)**: −½(−4) + 5 = 7 and −¼(−4) + 6 = 7. The typed stem shows a hand-added minus on ½. If the stem were read as +½, the answer would be (4/3, 17/3). (−4, 3) fails under either reading. | sympy; high-zoom render of the stem |
| E3 | SE p. 121 (TE p. 1008), 11.6.5 Bevan's table | Row (2, 0.5), second equation: ¼(2) − 3 = ½ − 3, then "0.5 ≠ −7/2". | ½ − 3 = **−5/2**. The verdict (≠) still holds. The slip is printed on the student page as if it were model work. The TE key's note to Bevan never mentions it. | sympy |
| E4 | TE p. 1020, 11.7.6 #1c answer graph | Keys the solution (3, 5) and draws both lines. | The line drawn for y = 2x − 1 has slope **≈ 2.17** (fitted: y = 2.165x − 1.01; the y = x + 2 line fits 1.007x + 2.03). The drawn lines cross at ≈ **(2.6, 4.7)**, visibly off the (3, 5) lattice point that the key states. | pixel fit, 900 dpi |
| E5 | TE p. 1017, 11.7.4 #1 answer graph ("parallel lines"); TE p. 1016, 11.7.3 #2 | 11.7.4 draws y = −⅓x ± 4 as the model of parallel lines. | The lower line fits −0.323x − 3.97. The upper line fits **−0.293x + 4.17**, which meets the x-axis near 13.5, not 12. The two drawn lines spread apart from left to right. Minor, same kind: in 11.7.3 #2 the line for y = 3x − 4 is drawn at slope ≈ 3.2 (it still crosses near the keyed (2.1, 2.4)). | pixel fit |
| E6 | Assessment **Guide** p. 2, Q1 "Additional Notes" | Without a calculator students may give −26/22 or −13/12; with one, −1.1̅8̅. | Q1's answer is **y = 2** (keyed correctly above the note). The note belongs to another item. It is also wrong in itself: −26/22 = −13/11, not −13/12. | sympy |
| E7 | SE p. 129 (TE p. 1025), 11.8.2 #2 (Sofia's internet plans) | Keys "both plans cost $260 after 2.5 months". The graph draws both lines into negative months and negative cost, on an x-axis from −5 to 15. | Monthly plans bill whole months. No one is billed $260. At month 2 the costs are $225 and $230; at month 3 they are $295 and $290. The honest reading is that the first plan is cheaper through month 2 and the second is cheaper from month 3 on. The intersection is a valid point of the model, but the stated meaning is not a real bill. | sympy |
| E8 | TE p. 1026, 11.8.3 answer graph (Anais and Chauncey) | Draws Anais's line on to about t = 1.4 h, where d ≈ 6.2 mi. The student grid runs to d = 7. | The lake is 5 mi from the parking lot (Chauncey starts there: d = 5 at t = 0). Anais reaches it at t = 16/15 h and turns back. The key graph puts her past the lake. | sampled heights: 4.67 at t = 1.0, 5.6 at 1.25, 6.15 at 1.4 |
| E9 | Practice L5 key p. 2 #5 | (2/3)x = (2/3)x − 5 → "0 ≠ 5". | Subtracting (2/3)x gives 0 = −5 (false). The line should read 0 ≠ −5. The verdict "no solution" is right. | — |
| E10 | Practice L6 key p. 1 #1; Assessment Key p. 2–3 and Guide pp. 7–8, Q7a and Q7c | False statements are printed as equations: "6 = −4.125", "−5.5 = 17", "5 = −16", "11 = −31". The practice key marks them with ✗; the test key and guide do not mark them at all. | These should read ≠. The homework keys and SE p. 117 do use ≠. All Yes/No verdicts are right. | — |
| E11 | Homework L6 key p. 2 #6 and #10 | #6: "3 = −4 + 1". #10: "4 = 4 − 1". | −3 = −4 + 1, and 3 = 4 − 1. Both verdicts are right. | — |
| E12 | Homework L8 p. 2 (Andre and Elena); Practice L6 p. 2 #5 | Andre/Elena grid: gridlines every 2 weeks and every $20. The key states the solution as exactly (2, 50). Practice #5 keys (1, −2.5) on a 1-unit grid. | On the Andre/Elena grid, (2, 50) lies halfway between the $40 and $60 lines. Elena's line y = 10 + 20x passes through **no** gridline crossing at all: at even x, y is an odd multiple of 10. Students cannot plot her line from lattice points. In practice #5, y = −2.5 is a half-unit read; this is minor, but the key states the value as exact. | sympy; grid detection |
| E13 | SE p. 116 Warm-Up graph A (TE p. 998); SE p. 123 11.7.2 #3 (TE p. 1014); student grids of Practice L7 and Homework L7 (all four) | Axis labels "±6", "±8" and "±10" are printed at the arrow tips. | The last gridline is ±5, ±7 and ±9 respectively, so the end labels sit about half a unit beyond it. On the L7 pages the **keys are drawn on a different grid** (gridlines −10 to 10), so a student's (−10, 7) or (10, −5) on y = −⅗x + 1 does not land where the key's line does. | gridline detection: 19 lines on each L7 student grid, 21 on the key grid |
| E14 | Practice L8 p. 1 (cookies) and p. 2 key (cab services) | Cookies: "x is the number of cookies and y is cost", but one of the two lines is revenue. Both lines are drawn into negative cookies. Cab key: the y-axis is titled "Fee ($)" and the answer reads "charge the same fee of $16", although the stem uses "fee" for Andy's $6 base charge. | y is the cost for one line and the revenue for the other. The y-axis is the total cost of the trip. | — |
| E15 | Assessment Q11 (p. 7), Key p. 5, Guide p. 9 | Asks for the "approximate solution". Keys **(9, 147.15)**. The guide deducts 2 points from a student who "correctly estimate[s]" y between 140 and 150. | The solution is exactly (9, 147.15). y = 147.15 cannot be read on a $10 grid. The rubric penalizes the graph estimate the stem asks for, and it rewards substituting x into an equation, which is not solving by graphing (AR.4.3). | sympy; grid by 1 h × $10 |
| E16 | Assessment Q5 (p. 3) | "4⅓x", a mixed number used as a coefficient. | The term can be read as (13/3)x, which gives the keyed **x = 11/5**, or as 4·⅓x, which gives **x = 11/2**. The answer depends on a notation that FAST does not use. | sympy, both readings |
| E17 | SE p. 111 (TE p. 989) definition box, against SE pp. 123–124 | Defines a system: "Each equation contains two or more variables." | 11.7.2 #2 (y = 4) and 11.7.3 #1 (x = 3.5) are systems containing one-variable equations. The definition is false for the book's own examples. | — |
| E18 | Wording on student pages | Practice and Homework L7 #7: "show that the solution you identified both equations" (the verb "satisfies" is missing). SE p. 126, 11.7.5 #2: "the same slope and the different y-intercepts". Assessment Q8: the system is printed without its brace. SE p. 112, 11.5.2 #1e: "The solution only gives the x-value" (this means the solution of the one-variable equation in part d, just after "solution" was defined for the system). Practice/Homework L8 #9: "Explain the meaning of the solution in the context?" (a question mark on an instruction). | — | — |

Not counted: Practice L7 key label "y = −⅗ + 1" lacks the x (key-only, §2).

## 2. Teacher-facing slips

- **TE p. 1012, 11.7.2 #1c.** The first verification line is printed "2 = +2"; the (1/3)(0) term is missing.
- **TE p. 1008, 11.6.5.** The sample note to Bevan says "all of the points do not satisfy both equations" (it means not all of them do). It never says that (−4, −4) is the system's one solution, or that her (2, 0.5) line contains the −7/2 slip (E3).
- **TE p. 1015–1016, 11.7.3 #1.** 1b keys "(3.5, 4.5)" as the approximation and 1d computes y = 13/3 ≈ 4.33. The TE never compares the two. 4.5 is the nearest half; 4.3 is the better read on a 1-unit minor grid. The facilitation note (p. 1016) says the exact solution waits for "Algebra 1", although 1d has just found it exactly, and 11.5 solved systems exactly by setting the expressions equal.
- **TE p. 1011, 11.7.1 key.** "System C … the only one with two lines that have negative slopes that intersect." On the printed ±6 window, C's lines (read as y ≈ −⅚x − 1 and y ≈ −¾x − 2; the slopes are uncertain to about ±0.03) do **not** meet: they converge to (12, −11), off the grid. A student who calls C "no solution" from the picture is reading the graph correctly. This is a useful AR.4.2 discussion point. It is not a key error, because the warm-up answers "will vary".
- **TE p. 998.** The TE copy of the 11.6.1 middle graph has a dark vertical rule at x = 1 that is not in the SE copy. It looks like a second axis on a projected key.
- **TE p. 1023, 11.8.1.** The sample answer ("Jones at the 18 yard line … Eisen at the 12") is not readable from the printed screenshot. The sample graph starts both runners at 12–17 yd at time 0, in a 40-yard dash from a standing start.
- **Assessment Key p. 4, Q10.** The sample "approximation" (−3.5, 5.75) gives y to hundredths, which is the exact value, not a graph read. The x value is the only approximated coordinate.
- **Guide p. 1.** The test is called "calculator neutral", which conflicts with Q11's guide (a calculator is used to get 147.15). The guide also suggests a calculator-free administration, which this classroom never uses (Part 8 ruling).
- **11.6.3 #1b (TE p. 1004)** concludes "infinitely many" from three tested points. That is mathematically sound, because two shared points fix the line, but the book never says why. The TE's own probing question asks the same thing, and 11.6.5's key then says infinitely many happens "only when every ordered pair on both lines is the same". The reason (two points determine a line) should be stated once.
- **Practice L7 key p. 1** labels a line "y = −⅗ + 1".
- **TE p. 986 lesson narrative** admits "students are not expected to solve systems of equations algebraically in this course", and then 11.5.2 #1d, 11.5.3 #1a and #2a do exactly that (see §3).

## 3. Conflicts with the course's settled rules and the benchmark boundaries

**Slope, y-intercept and slope-intercept graphing assumed known** (Unit 10 comes after this unit here):
- **11.05:** SE p. 112 #2 offers "slope" and "y-intercept" as choices. The TE (pp. 987, 989) leans on "linear relationships learned in the previous unit" and "their work in Unit 10". The TE p. 989 key for 1a says "positive slop[e]".
- **11.06:** SE p. 118 #3b: "Parallel lines have the same slope". TE p. 998 matches by "learning from Unit 10". TE p. 1001 uses "slope and y-intercept" vocabulary.
- **11.07:** SE p. 125 #1f (same slopes, different y-intercepts) and SE p. 126 11.7.5 #2 (a three-row slope/intercept table). The TE p. 1020 key reasons by slope. TE p. 1014: "Students graphed equations in Unit 10 … should not need a refresher."
- **11.08:** TE p. 1022 misconceptions are about slope and y-intercept in context. The TE p. 1024 probe asks students to "explain … using the slope and y-intercept".
- **Practice/Homework L6 #8 keys:** "same slope".
- **Test:** Q6 ("Any line … with a slope of −4") needs slope; there is no table route to it. Q12b asks "same slope / different slopes".
- **Every "graph the equation/system" item can be done from a table**, but several need chosen inputs: −⅗, ⅔, ⅕ and ¾ slopes (L7); t in quarter-hours (11.8.3); x in hundreds (11.8.4).

**Standard form:** Assessment Key Q12 stem, 6x + 3y = 30 (E1). That is the only instance.

**Outside "slope-intercept form only"** (AR.4.3 boundary): 11.7.3 #1 uses **x = 3.5**, a vertical line that has no slope-intercept form. y = 4 (11.7.2 #2) is allowed (m = 0).

**Substitution or elimination** (Algebra 1):
- 11.5.2 #1d and 11.5.3 #1a, #2a set the two expressions equal and solve for x, then substitute back (11.5.2 #1e).
- Practice/Homework L5 #2 and #5 do the same.
- Worked Examples #4 is a full substitution solve.
- The test guide's Q11 rubric expects substitution for the exact y.
- TE p. 1005 says "challenge students to verify their solutions algebraically".

"Use substitution to verify" (substituting a point into an equation, used across 11.6–11.7 and L5–L7) is AR.4.1 and is allowed, but the name collides with the Algebra 1 method. Our pages should say "substitute the point".

**Partner and group work** (none allowed):
- SE 11.5.2 (Partner A / Partner B); 11.5.3 #1b, #2b, and #2c (a classmate initials your summary).
- 11.7.2 "Collaboration"; 11.7.3 #1c; 11.7.4 #1b–e; 11.8.4 "Collaboration" a, b and e.
- TE: Think-Pair-Share (pp. 992, 1000), a jigsaw (p. 1004), "Partner work" (p. 1006), Take Turns (p. 1013), floor-grid walking in pairs (pp. 997, 1002), pairing to discuss reflections (p. 995).

**Videos:** 11.8.1 is built on a 36-second video (TE pp. 1021, 1023). The 11.6.5 TE offers students "the option to make a video".

**"Homework" on student pages:** every Homework page header reads "Lesson N Homework".

**Calculator statements:** TE materials list "(Optional) Scientific calculator" (11.05–11.07) or a "Graphing utility" (11.08; TE pp. 1004, 1027). The 11.6 TE says "Allowing students to use calculators". Guide pp. 1–2 contain calculator text. No student page names a calculator.

**Multi-paragraph stems:** 11.5.1 (diamond); 11.8.1; 11.8.3 (three paragraphs); 11.8.4 (two); Practice L8 cookies; Homework L8; test Q11 (four sentences of story, then the system) and Q12.

**Compound questions:**
- "Determine whether one/none/infinitely many … If one, give the solution" (11.6.3 #2; Practice/Homework L6 #5, #7, #9).
- 11.5.3 #2b ("Discuss … Predict … Make a sketch").
- 11.7.6 #1c ("Graph … Then write the solution").
- 11.8.4 #1a ("Discuss … Then complete").
- Practice L8 #10 (two questions).
- Practice/Homework L8 #6–7 (label and title in one).

**Other:**
- "Perpendicular" (SE p. 125 #1d and #1f) is not grade 8 content.
- Discovery openers: 11.5.2 and 11.7.4 are Explorations; Notice and Wonder in 11.5 and 11.8.
- The 11.5.1 warm-up is off-unit (scientific notation, NSO.1.4) and includes a confidence rating.

## 4. What AR.4.1, 4.2, 4.3 (and the test's AR.2.1) expect that the book never asks

| Benchmark | The state expects | The book |
|---|---|---|
| AR.4.1 | A specified set of candidates, tested in **both** equations. The misconception "how can one pair be a single solution to two equations". Integer substitution errors. The FAST multiselect, which never says how many to pick. | Strong here: tables of 2–3 candidates in 11.6.2–11.6.4, L6 and test Q7, including a pair that passes one equation and fails the other (L6 #1, Q7c). **Never** a select-all list, never a candidate list with **no** solution, and never the state task's fraction coefficients with a fractional check (y = ⅗x − 9/5 style). |
| AR.4.2 | One, none or infinitely many, read from a graph. The coincident case stated as infinitely many, **including points not plotted** (named misconception). The state items: two horizontal lines (none), a slanted and a horizontal line (one), and two lines through the origin (Ashley: "no y-intercept, so no intersection" is wrong). | The coincident case is called infinitely many (SE p. 118; L5 #8–10; L6 #9–10), but the only points tested on it, (−4, 1) and (5, 3), are on the drawn window. The book **never** asks about a point off the graph, such as (100, 79) on y = 0.8x − 1. It never has two horizontal lines and never two lines through the origin. It never shows lines that meet off-window: 11.7.1 C does, but unannounced (§2). |
| AR.4.3 | Solve by graphing, in mathematical and real-world contexts. **Approximate non-integer solutions** (the guide's −28/13 ≈ −2.15). **Slope-intercept form only.** **Parallel lines have the same slope.** Plotting errors and coincident misreads as misconceptions. | Approximation appears in 11.7.3, 11.8.3 and test Q10–11, but **no precision is ever stated** (tenths? nearest half?). The keys mix 13/3, 4.5, 0.7, 2.1, 5.75 and 147.15, and Q11's rubric rewards the exact value (E15). Parallel = same slope is stated as a rule before slope is taught here. x = 3.5 breaks the form boundary. No real-world item asks for the coincident or parallel case in context except test Q12 (identical tanks). No item asks whether the solution is **reasonable in context** (E7, E8). |
| AR.2.1 (test Q1–5) | One, none and infinitely many solutions. The distributive property. Variables on both sides. The misconception "a solution must look like x = constant". | Q4 is the infinitely-many case. **No item has no solution**, although the state task has one (⅓x − 6 = ⅓(x − 3) − 1). Q5's mixed-number coefficient is ambiguous (E16). |

## 5. Per lesson, and the test

**11.05 Introduction to systems** (AR.4.1, 4.2; SE pp. 110–115, TE pp. 986–995). Order: a scientific-notation warm-up; a partner exploration of a graphed system (y = −x + 5, y = ½x + 2; grid −2..7 × −3..6) with the definition; setting the expressions equal to get x = 2, then y by substitution; plotting (2, 3); "the solution is the point of intersection". Guided instruction then covers a parallel pair (0.8x and 0.8x − 3.2; ±6 grid) by solving to a false statement, and a coincident pair (−0.5x + 6 and 6 − ½x; grid −2..14 × −2..9). Vocabulary: system of equations, solution, point of intersection (slope and y-intercept as distractors). Item shapes: notice/explain, solve, predict and sketch, graph a second line. Practice/Homework L5 (±6 grids): read an intersection, solve the equation, relate the two, verify; a parallel pair; a coincident pair. **Sound to reuse (as graphs to read and points to test, not as equations to solve):** SE p. 111 graph (y = −x + 5, y = ½x + 2); SE p. 113 #1 graph; SE p. 114 #2d–g (the coincident pair); Practice L5 #1, #4, #6, #8–10; Homework L5 #1, #4, #6, #8–10. Not #2 or #5 of either (they solve algebraically; E9).

**11.06 Solutions to systems** (AR.4.1, 4.2; SE pp. 115–121, TE pp. 996–1008). Order: match three systems to graphs (one, none, coincident); test (2, 7.5) in both equations, then a table of three candidates, then the solution (4, 7), then graph the second line (−20..20 × −10..12); a three-case summary table; parallel lines have the same slope; guided practice on a coincident pair tested at three points and two systems read from graphs; Your Turn (three candidates, then the graph, −14..18 × −8..8); error analysis (Bevan). Vocabulary: one solution / no solution / infinitely many solutions, satisfy, parallel. Item shapes: Yes/No candidate tables with work, two-dropdown sentence completion, matching. Practice/Homework L6: candidate tables (3 pairs, then 2 on a coincident pair) and three graphed systems on ±6 grids. **Sound:**
- SE p. 116 #1 (tables only; E3 does not touch them)
- p. 117 #1c–d
- p. 119 #1 and #2 (both graphs)
- p. 120 #1
- p. 121 Bevan, with E3 corrected (the checkmarks are right, and the error is a good AR.4.1 item)
- Practice L6 #1–7, #9–10 (fix the "=" lines, E10)
- Homework L6 #1–5, #7, #9 (fix E11)

**11.07 Solving by graphing** (AR.4.3; SE pp. 121–126, TE pp. 1009–1020). Order: Which One Doesn't Belong (four graphed systems, no equations); read and verify (y = ⅓x + 2 and 2x + 2 → (0, 2); y = 4 and ½x − 1 → (10, 4)); graph and read (3x − 3 and ½x + 2 → (2, 3)); approximating (x = 3.5 with ⅔x + 2; −¾x + 4 and 3x − 4 → (32/15, 12/5)); parallel lines (−⅓x ± 4); a summary table; an exit ticket (pick the no-solution system; graph x + 2 and 2x − 1 → (3, 5)). Grids: ±6, ±7, ±8, ±10 by 2, ±12 × ±10. Vocabulary adds approximate, parallel, perpendicular, slope, y-intercept. Practice/Homework L7: graph two lines on ±10 grids (gridlines only to ±9, E13); every intersection is a lattice point ((5, −2), (−4, −7), (3, −3), (5, 1)); one parallel pair each. **Sound:** SE p. 122 #1 and p. 123 #2 (read and verify); p. 123 #3; p. 124 #2 (the approximation; key art E5 aside); p. 126 #1 (as a graphing task, without "slope" as the reason); all of Practice and Homework L7, provided our grid has gridlines to ±10. Not 11.7.3 #1 (x = 3.5) unless Croix accepts the boundary breach.

**11.08 Real-world systems** (AR.4.3; SE pp. 127–131, TE pp. 1021–1030). Order: video warm-up (40-yard dash); bamboo (¼x + 6, ½x + 3 → (12, 9); grid 0..14 × 0..22); internet plans read off a graph with labeled points ((2.5, 260); E7); hikers (3.75t + 1, −2.25t + 5 → (⅔, 3.5), an approximation; grid in 0.25 h × 1 mi); tanks (−2x + 1500, 6x + 300 → (150, 1200); 0..900 × 0..1500); cool-down. Vocabulary: label axes with titles and units; meaning of the solution in context. Practice L8: cookies (break-even at (18, 40.5), labeled graph); cab services ((20, 16), 1-unit grid to 28 × 25, plus "which is cheaper when"). Homework L8: kayaks ((5, 37.5), labeled graph); savings ((2, 50); E12). **Sound:** bamboo (SE p. 128); tanks (SE pp. 130–131); hikers with a "reasonable in context" part added and the line stopped at the lake; Practice L8 cabs #5–10 (a model item; fix E14's "fee"); Homework L8 kayaks; cookies with E14 fixed. The savings item needs a finer grid.

**The unit test** (12 items, 100 points; recomputed: every keyed answer right; the defects are E1, E6, E10, E15, E16).

| Q | Benchmark (guide) | Type | Gives → asks | Answer | Pts |
|---|---|---|---|---|---|
| 1 | AR.2.1 | open response, work | distributive on both terms, one solution | y = 2 | 8 |
| 2 | AR.2.1 | open response | decimal coefficients, variable both sides | h = 2.5 | 8 |
| 3 | AR.2.1 | open response | fraction coefficients, both sides | k = 1.6 | 8 |
| 4 | AR.2.1 | open response | identity | infinitely many | 8 |
| 5 | AR.2.1 | open response | mixed-number coefficient (E16) | x = 11/5 | 8 |
| 6 | AR.4.2 | graphing (draw a line) | y = −4x + 6 drawn → draw a no-solution partner | any y = −4x + b, b ≠ 6 | 4 |
| 7a–c | AR.4.1 | Yes/No with work, ×3 | three candidates for −9/4x + 2 and 3x − 19 | No / Yes / No | 6 each = 18 |
| 8 | AR.4.1 | two-dropdown completion | graph of −x + 5 and x + 1 → "(2, 3) is a solution of both" | — | 6 |
| 9 | AR.4.3 | open response, read graph | lattice intersection | (−2, −6) | 6 |
| 10 | AR.4.3 | open response, approximate | non-lattice intersection | ≈ (−3.4, 5.75) | 8 |
| 11 | AR.4.3 | open response, context | wages; "approximate" (E15) | (9, 147.15) | 8 |
| 12a | AR.4.3 | graphing | draw the second (identical) line | the same line | 4 |
| 12b | AR.4.3 | two-dropdown completion | same slope; infinitely many | — | 6 |

Weights: AR.2.1 40 · AR.4.1 24 · AR.4.3 32 · AR.4.2 4. There is no single-answer four-option multiple choice and no select-all. The grids in Q6, Q9 and Q10 are not square (x unit about 1.12 × the y unit). Q8, Q9 and Q12 sit on lattice-friendly grids. Q11's grid is 1 h × $10.

## 6. Judgment calls

1. **E10 (false statements printed with "=")** is counted as a defect, as Unit 6's audit counted false equalities (D28). The verdicts are all right. If Croix prefers to treat this as notation only, drop it.
2. **The test's benchmark tags.** Q6 is tagged AR.4.2, but it is a construction resting on AR.4.3 Clarification 3 (parallel lines have the same slope). Q12 is tagged AR.4.3, but its graded part (12b) is AR.4.2 (decide the number of solutions of a graphed system). On the book's own tags the test has a single 4-point AR.4.2 item. Re-tagged, AR.4.2 has 10 points.
3. **11.7.3 #1 (x = 3.5).** The AR.4.3 boundary says slope-intercept form only, and this item breaks it. It is also the book's clearest approximation lesson (the answer is 13/3). Keep it with a slope-intercept partner, or replace it (for example y = −0.5x + 2 and y = 4.5x − 5 → (1.4, 1.3), the state's own item). This is Croix's call.
4. **E7 (the internet plans) and E8 (the hikers)** are context-sense defects, not math errors. The models are correct as equations. They are reported because the TE keys a "meaning in context" that is not true of the context.
5. **The 11.7.1 System C reading** (§2) is not counted as a defect. The equations are my reading (slopes about ±0.03), and the warm-up's answers "vary".

## 7. Inventory and log

| File | Pages viewed | Logged checks | Agree with sympy / the drawing |
|---|---|---|---|
| 11.05 TE + SE pp. 110–115 | 10 + 6 | 4 | 4 (definition box: E17) |
| 11.06 TE + SE pp. 115–121 | 13 + 7 | 22 | 22 values; one printed work line wrong (E3) |
| 11.07 TE + SE pp. 121–126 | 12 + 6 | 12 | 12 values; two key graphs off (E4, E5) |
| 11.08 TE + SE pp. 127–131 | 10 + 5 | 7 | 7 values; context (E7, E8) |
| Practice + key, L5–L8 | 8 + 8 | 19 | 19 verdicts; work lines E9, E10 |
| Homework + key, L5–L8 | 8 + 8 | 21 | 21 verdicts; work lines E11; grid E12 |
| Assessment, Key, Guide | 8 + 6 + 10 | 16 | 16 keyed answers; key stem E1, guide E6, rubric E15, notation E16 |
| Worked Examples | 1 | 8 | 7; #4 wrong (E2) |
| **Total** | **124** | **109** (several rows span two to four sub-items) | **one wrong final answer (WE #4)** |

Graph checks: 37 printed graphs were compared with their equations. 25 were fitted by pixel calibration: the practice and homework graphs; the test graphs Q6, Q8–Q12; and the TE key graphs 11.7.3 #2, 11.7.4, 11.7.6, the bamboo and the hikers. The rest were read off lattice points. Only E4 and E5 disagree, plus the end-label issue E13.

Log columns: lesson · source · page · item · the system or check as read · sympy · lattice? · grid · the book's key · verdict.


| Lesson | Source | Page | Item | System / check as read | sympy | Lattice? | Grid | Book key | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 11.5 | SE/TE | 111 / TE 988 | 11.5.1 #1 | "10 billion-trillion-trillion" = 10·10^9·10^12·10^12 | 10^34 |  |  | 1×10^34 | match |
| 11.5 | SE/TE | 111–112 / TE 989–991 | 11.5.2 #1–2 | y = 5 - x ; y = x/2 + 2 | (2, 3) | lattice | −2..7 × −3..6, 1-unit | (2, 3) | match; graph checked |
| 11.5 | SE/TE | 113 / TE 992 | 11.5.3 #1 | y = 4·x/5 ; y = 4·x/5 - 16/5 | no solution (parallel) | — | ±6, 1-unit | no solution | match; graph checked |
| 11.5 | SE/TE | 113–114 / TE 992–994 | 11.5.3 #2 | y = 6 - x/2 ; y = 6 - x/2 | infinitely many (same line) | — | −2..14 × −2..9 | infinitely many | match; graph checked |
| 11.5 | PP | L5 p1 | #1–2 | y = 3 - x/4 ; y = x - 2 | (4, 2) | lattice | ±6, 1-unit | (4, 2); x = 4 | match; graph fitted |
| 11.5 | PP | L5 p2 | #5–6 | y = 2·x/3 + 1 ; y = 2·x/3 - 4 | no solution (parallel) | — | ±6 | no solution; work line "0 ≠ 5" | verdict match; work line wrong (E9) |
| 11.5 | PP | L5 p2 | #8–10 | y = 2 - x/4 ; y = 2 - x/4 | infinitely many (same line) | — | ±6 | infinitely many | match |
| 11.5 | HW | L5 p1 | #1–2 | y = 5 - 2·x ; y = x/3 - 2 | (3, -1) | lattice | ±6 | (3, −1); x = 3 | match; graph fitted |
| 11.5 | HW | L5 p2 | #5–6 | y = 3 - x/2 ; y = -x/2 - 2 | no solution (parallel) | — | ±6 | no solution | match; graph fitted |
| 11.5 | HW | L5 p2 | #8–10 | y = 3·x/4 + 1 ; y = 3·x/4 + 1 | infinitely many (same line) | — | ±6 | infinitely many | match |
| 11.6 | SE/TE | 116 / TE 998 | 11.6.1 System A | y = x/4 + 5/4 ; y = x/4 + 5/4 | infinitely many (same line) | — | ±6 (end labels off-grid, E13) | graph 3; infinitely many (TE 1002) | match |
| 11.6 | SE/TE | 116 / TE 998 | 11.6.1 System B | y = 2·x/3 + 5 ; y = x/3 + 3 | (-6, 1) | lattice | −8..3 × −5..6 | graph 1; one solution | match; graph checked |
| 11.6 | SE/TE | 116 / TE 998 | 11.6.1 System C | y = 1 - x/6 ; y = -x/6 - 1 | no solution (parallel) | — | ±6 | graph 2; no solution | match |
| 11.6 | SE/TE | 116–117 / TE 999–1000 | 11.6.2 #1a | (2, 15/2) in y = x/2 + 5 ; y = 8 - x/4 | 2nd only → not a solution |  |  | not a solution (1st no, 2nd yes) | match |
| 11.6 | SE/TE | 116–117 / TE 999–1000 | 11.6.2 #1c | (-2, 4) in y = x/2 + 5 ; y = 8 - x/4 | 1st only → not a solution |  |  | No | match |
| 11.6 | SE/TE | 116–117 / TE 999–1000 | 11.6.2 #1c | (1, 8) in y = x/2 + 5 ; y = 8 - x/4 | neither → not a solution |  |  | No | match |
| 11.6 | SE/TE | 116–117 / TE 999–1000 | 11.6.2 #1c | (4, 7) in y = x/2 + 5 ; y = 8 - x/4 | both → solution |  |  | Yes | match |
| 11.6 | SE/TE | 117 / TE 1001 | 11.6.2 #1d, #2 | y = x/2 + 5 ; y = 8 - x/4 | (4, 7) | lattice | −20..20 × −10..12, labels by 2 | (4, 7); one | match; graph checked |
| 11.6 | SE/TE | 119 / TE 1004 | 11.6.3 #1a | (-3/2, 3/5) in y = 2·x/5 + 6/5 ; y = 2·x/5 + 6/5 | both → solution |  |  | Yes | match |
| 11.6 | SE/TE | 119 / TE 1004 | 11.6.3 #1a | (0, 6/5) in y = 2·x/5 + 6/5 ; y = 2·x/5 + 6/5 | both → solution |  |  | Yes | match |
| 11.6 | SE/TE | 119 / TE 1004 | 11.6.3 #1a | (2, 2) in y = 2·x/5 + 6/5 ; y = 2·x/5 + 6/5 | both → solution |  |  | Yes | match |
| 11.6 | SE/TE | 119 / TE 1004 | 11.6.3 #1b | y = 2·x/5 + 6/5 ; y = 2·x/5 + 6/5 | infinitely many (same line) | — | — | infinitely many | match |
| 11.6 | SE/TE | 119 / TE 1005 | 11.6.3 #2 row 1 | y = 3·x/4 + 11 ; y = 5·x/2 - 3 | (8, 17) | lattice | −16..18 × −4..18, 1-unit | (8, 17) | match; graph checked |
| 11.6 | SE/TE | 119 / TE 1005 | 11.6.3 #2 row 2 | y = 5·x/3 - 8 ; y = 5·x/3 + 2 | no solution (parallel) | — | ±18 × ±10, 2-unit | no solution | match; graph checked |
| 11.6 | SE/TE | 120 / TE 1006 | 11.6.4 #1a | (4, 4) in y = 5·x/6 - 2 ; y = 6 - x/2 | 2nd only → not a solution |  |  | No | match |
| 11.6 | SE/TE | 120 / TE 1006 | 11.6.4 #1a | (6, 3) in y = 5·x/6 - 2 ; y = 6 - x/2 | both → solution |  |  | Yes | match |
| 11.6 | SE/TE | 120 / TE 1006 | 11.6.4 #1a | (12, 0) in y = 5·x/6 - 2 ; y = 6 - x/2 | 2nd only → not a solution |  |  | No | match |
| 11.6 | SE/TE | 120 / TE 1006–1007 | 11.6.4 #1b–c | y = 5·x/6 - 2 ; y = 6 - x/2 | (6, 3) | lattice | −14..18 × −8..8 | one solution, (6, 3) | match; graph checked |
| 11.6 | SE/TE | 121 / TE 1008 | 11.6.5 Bevan table | (2, 1/2) in y = 3·x/4 - 1 ; y = x/4 - 3 | 1st only → not a solution |  |  | ✓ 1st only (printed 1/2 − 3 = −7/2) | checkmarks right; (2, 0.5) work line wrong: 1/2 − 3 = −5/2 (E3) |
| 11.6 | SE/TE | 121 / TE 1008 | 11.6.5 Bevan table | (0, -3) in y = 3·x/4 - 1 ; y = x/4 - 3 | 2nd only → not a solution |  |  | ✓ 2nd only | checkmarks right; (2, 0.5) work line wrong: 1/2 − 3 = −5/2 (E3) |
| 11.6 | SE/TE | 121 / TE 1008 | 11.6.5 Bevan table | (-4, -4) in y = 3·x/4 - 1 ; y = x/4 - 3 | both → solution |  |  | ✓ both | checkmarks right; (2, 0.5) work line wrong: 1/2 − 3 = −5/2 (E3) |
| 11.6 | SE/TE | 121 / TE 1008 | 11.6.5 (true solution) | y = 3·x/4 - 1 ; y = x/4 - 3 | (-4, -4) | lattice | — | not stated by key | key never states (−4, −4) (§2) |
| 11.6 | PP | L6 p1 | #1 | (-1/2, 6) in y = 5 - 2·x ; y = x/4 - 4 | 1st only → not a solution |  |  | No | match; false lines printed with "=" and ✗ (E10) |
| 11.6 | PP | L6 p1 | #1 | (-6, -11/2) in y = 5 - 2·x ; y = x/4 - 4 | 2nd only → not a solution |  |  | No | match; false lines printed with "=" and ✗ (E10) |
| 11.6 | PP | L6 p1 | #1 | (4, -3) in y = 5 - 2·x ; y = x/4 - 4 | both → solution |  |  | Yes | match; false lines printed with "=" and ✗ (E10) |
| 11.6 | PP | L6 p1 | #2 | y = 5 - 2·x ; y = x/4 - 4 | (4, -3) | lattice | — | one solution (4, −3) | match |
| 11.6 | PP | L6 p1 | #3 | (-4, -3) in y = x/4 - 2 ; y = x/4 - 2 | both → solution |  |  | Yes | match |
| 11.6 | PP | L6 p1 | #3 | (12, 1) in y = x/4 - 2 ; y = x/4 - 2 | both → solution |  |  | Yes | match |
| 11.6 | PP | L6 p2 | #5–6 | y = -5·x/2 ; y = x/2 - 3 | (1, -5/2) ≈ (1.000, -2.500) | not lattice | ±6, 1-unit | (1, −2.5) | match; y = −2.5 is a half-unit read (E12); graph fitted |
| 11.6 | PP | L6 p2 | #7 | y = 2·x + 1 ; y = 2·x - 5 | no solution (parallel) | — | ±6 | no solutions | match; graph fitted |
| 11.6 | PP | L6 p2 | #9 | y = 3·x/4 + 4 ; y = 3·x/4 + 4 | infinitely many (same line) | — | ±6 | infinitely many | match; graph fitted |
| 11.6 | PP | L6 p2 | #10 | (-4, 1) in y = 3·x/4 + 4 ; y = 3·x/4 + 4 | both → solution |  |  | Yes | match |
| 11.6 | HW | L6 p1 | #1 | (-5/2, 4) in y = 3 - 2·x/5 ; y = x/5 - 3 | 1st only → not a solution |  |  | No | match |
| 11.6 | HW | L6 p1 | #1 | (10, -1) in y = 3 - 2·x/5 ; y = x/5 - 3 | both → solution |  |  | Yes | match |
| 11.6 | HW | L6 p1 | #1 | (0, -3) in y = 3 - 2·x/5 ; y = x/5 - 3 | 2nd only → not a solution |  |  | No | match |
| 11.6 | HW | L6 p1 | #2 | y = 3 - 2·x/5 ; y = x/5 - 3 | (10, -1) | lattice | — | one solution (10, −1) | match |
| 11.6 | HW | L6 p1 | #3 | (-2, 2) in y = 3·x/2 + 5 ; y = 3·x/2 + 5 | both → solution |  |  | Yes | match |
| 11.6 | HW | L6 p1 | #3 | (4, 11) in y = 3·x/2 + 5 ; y = 3·x/2 + 5 | both → solution |  |  | Yes | match |
| 11.6 | HW | L6 p2 | #5–6 | y = 1 - 4·x ; y = x - 4 | (1, -3) | lattice | ±6 | (1, −3); work line "3 = −4 + 1" | verdict match; work line wrong (E11); graph fitted |
| 11.6 | HW | L6 p2 | #7 | y = 3 - x ; y = -x - 2 | no solution (parallel) | — | ±6 | no solutions | match; graph fitted |
| 11.6 | HW | L6 p2 | #9 | y = 4·x/5 - 1 ; y = 4·x/5 - 1 | infinitely many (same line) | — | ±6 | infinitely many | match; graph fitted |
| 11.6 | HW | L6 p2 | #10 | (5, 3) in y = 4·x/5 - 1 ; y = 4·x/5 - 1 | both → solution |  |  | Yes; work line "4 = 4 − 1" | verdict match; work line wrong (E11) |
| 11.7 | SE/TE | 122 / TE 1011 | 11.7.1 System A (read off graph) | y = 3 - 3·x/4 ; y = 2·x/5 + 4 | (-20/23, 84/23) ≈ (-0.870, 3.652) | not lattice | ±6 | "only solution in Quadrant II" | match; green slope read ≈ 0.4 (uncertain) |
| 11.7 | SE/TE | 122 / TE 1011 | 11.7.1 System B (read) | y = -3·x/4 - 2 ; y = 3·x - 4 | (8/15, -12/5) ≈ (0.533, -2.400) | not lattice | ±6 | — | Quadrant IV, non-lattice |
| 11.7 | SE/TE | 122 / TE 1011 | 11.7.1 System C (read) | y = -5·x/6 - 1 ; y = -3·x/4 - 2 | (12, -11) | lattice | ±6 | "negative slopes that intersect" | meet off-window (§2); orange slope read ≈ −0.84 (uncertain) |
| 11.7 | SE/TE | 122 / TE 1011 | 11.7.1 System D (read) | y = 3 - 3·x/4 ; y = -3·x/4 - 2 | no solution (parallel) | — | ±6 | "parallel" | match |
| 11.7 | SE/TE | 122 / TE 1012 | 11.7.2 #1 | y = x/3 + 2 ; y = 2·x + 2 | (0, 2) | lattice | −7..7 × −5..6 | (0, 2) | match; work line "2 = +2" (§2) |
| 11.7 | SE/TE | 123 / TE 1013 | 11.7.2 #2 | y = 4 ; y = x/2 − 1 | (10, 4) | lattice | ±10, 2-unit | (10, 4) | match; graph checked |
| 11.7 | SE/TE | 123 / TE 1014 | 11.7.2 #3 | y = 3·x - 3 ; y = x/2 + 2 | (2, 3) | lattice | ±8 (end labels off-grid, E13) | (2, 3) | match; graph checked |
| 11.7 | SE/TE | 124 / TE 1015–1016 | 11.7.3 #1 | x = 3.5 ; y = 2x/3 + 2 | (7/2, 13/3) ≈ (3.5, 4.333) | not lattice | ±12 × ±10, labels by 2 | b: (3.5, 4.5) approx; d: 13/3 | 4.5 is the nearest half; key never reconciles 4.5 with 13/3 (§2); x = 3.5 is not slope-intercept form (§3) |
| 11.7 | SE/TE | 124 / TE 1016 | 11.7.3 #2 | y = 4 - 3·x/4 ; y = 3·x - 4 | (32/15, 12/5) ≈ (2.133, 2.400) | not lattice | ±12 × ±10 | (2.1, 2.4) approx | match; steep key line drawn slope ≈ 3.2 (E5, minor) |
| 11.7 | SE/TE | 125 / TE 1017–1018 | 11.7.4 #1 | y = 4 - x/3 ; y = -x/3 - 4 | no solution (parallel) | — | ±12 × ±10 | no solution; parallel | verdict match; key upper line drawn slope ≈ −0.29 (E5) |
| 11.7 | SE/TE | 126 / TE 1020 | 11.7.6 #1 (circled) | y = 3 - x ; y = -x - 1 | no solution (parallel) | — | — | no solutions | match |
| 11.7 | SE/TE | 126 / TE 1020 | 11.7.6 #1c | y = x + 2 ; y = 2·x - 1 | (3, 5) | lattice | ±12 × ±10 | (3, 5) | value match; key graph crosses ≈ (2.6, 4.7) (E4) |
| 11.7 | PP | L7 p1 | #1–4 | y = 1 - 3·x/5 ; y = x - 7 | (5, -2) | lattice | gridlines ±9, labels ±10 (E13) | (5, −2) | match; graph fitted; key label "y = −3/5 + 1" lacks x |
| 11.7 | PP | L7 p2 | #5–7 | y = 3·x/4 - 4 ; y = 3·x + 5 | (-4, -7) | lattice | same | (−4, −7) | match; graph fitted |
| 11.7 | PP | L7 p2 | #8–10 | y = 3 - 2·x ; y = 7 - 2·x | no solution (parallel) | — | same | parallel; no solutions | match; graph fitted |
| 11.7 | HW | L7 p1 | #1–4 | y = 2·x/3 - 5 ; y = 3 - 2·x | (3, -3) | lattice | same | (3, −3) | match |
| 11.7 | HW | L7 p2 | #5–7 | y = x/5 ; y = 2 - x/5 | (5, 1) | lattice | same | (5, 1) | match |
| 11.7 | HW | L7 p2 | #8–10 | y = x - 5 ; y = x + 1 | no solution (parallel) | — | same | parallel; no solution | match |
| 11.8 | SE/TE | 128 / TE 1024–1025 | 11.8.2 #1 bamboo | y = x/4 + 6 ; y = x/2 + 3 | (12, 9) | lattice | 0..14 × 0..22, 1-unit | (12, 9) | match; graph fitted |
| 11.8 | SE/TE | 129 / TE 1025 | 11.8.2 #2 Sofia | y = 70·x + 85 ; y = 60·x + 110 | (5/2, 260) ≈ (2.500, 260.000) | not lattice | x by 5, y by 125 (labeled points) | (2.5, 260) | value match; context (E7) |
| 11.8 | SE | 129 | 11.8.2 #2 labeled point | (0, 85) in y = 70·x + 85 ; y = 60·x + 110 | 1st only → not a solution |  |  | on 1st | consistent with drawing |
| 11.8 | SE | 129 | 11.8.2 #2 labeled point | (1, 170) in y = 70·x + 85 ; y = 60·x + 110 | 2nd only → not a solution |  |  | on 2nd | consistent with drawing |
| 11.8 | SE | 129 | 11.8.2 #2 labeled point | (5, 410) in y = 70·x + 85 ; y = 60·x + 110 | 2nd only → not a solution |  |  | on 2nd | consistent with drawing |
| 11.8 | SE/TE | 129–130 / TE 1026–1027 | 11.8.3 Anais/Chauncey (t for x, d for y) | y = 15·x/4 + 1 ; y = 5 - 9·x/4 | (2/3, 7/2) ≈ (0.667, 3.500) | not lattice | t by 0.25, d by 1 | (0.7, 3.5) approx | match; key graph runs Anais past the lake (E8) |
| 11.8 | SE/TE | 130–131 / TE 1028–1029 | 11.8.4 Victor | y = 1500 - 2·x ; y = 6·x + 300 | (150, 1200) | lattice | 0..900 × 0..1500, gridline 50 × 100 | (150, 1200); at 100 min: 1300 L, 900 L | match (1300, 900 verified) |
| 11.8 | PP | L8 p1 | #3 cookies | y = 9·x/4 ; y = x/4 + 36 | (18, 81/2) ≈ (18.000, 40.500) | not lattice | by 20 (labeled points) | (18, 40.5) | match; "y is cost" for revenue (E14) |
| 11.8 | PP | L8 p1 | labeled (10, 22.5) | (10, 45/2) in y = 9·x/4 ; y = x/4 + 36 | 1st only → not a solution |  |  | on revenue line | consistent |
| 11.8 | PP | L8 p2 | #8 cabs | y = x/2 + 6 ; y = 4·x/5 | (20, 16) | lattice | 0..28 × −5..25, 1-unit | (20, 16); Andy > 20 mi, Randy < 20 mi | match |
| 11.8 | HW | L8 p1 | #3 kayaks | y = 9·x/2 + 15 ; y = 5·x + 25/2 | (5, 75/2) ≈ (5.000, 37.500) | not lattice | by 2 h × $10 (labeled points) | (5, 37.5) | match |
| 11.8 | HW | L8 p1 | labeled point | (0, 25/2) in y = 9·x/2 + 15 ; y = 5·x + 25/2 | 2nd only → not a solution |  |  | on B | consistent |
| 11.8 | HW | L8 p1 | labeled point | (2, 24) in y = 9·x/2 + 15 ; y = 5·x + 25/2 | 1st only → not a solution |  |  | on A | consistent |
| 11.8 | HW | L8 p1 | labeled point | (7, 93/2) in y = 9·x/2 + 15 ; y = 5·x + 25/2 | 1st only → not a solution |  |  | on A | consistent |
| 11.8 | HW | L8 p2 | #8 savings | y = 5·x + 40 ; y = 20·x + 10 | (2, 50) | lattice | by 2 wk × $20 | (2, 50) | value match; grid (E12) |
| Test | Key/Guide | p1 | Q1 | 22·y - 32 = 12 | 2 |  |  | y = 2 | match; guide note quotes −26/22, −13/12 (E6) |
| Test | Key/Guide | p1 | Q2 | 427/5 - 183·h/10 = 297/5 - 79·h/10 | 5/2 |  |  | h = 2.5 | match |
| Test | Key/Guide | p2 | Q3 | 56·k/5 - 14/5 = 6·k/5 + 66/5 | 8/5 |  |  | k = 1.6 | match |
| Test | Key/Guide | p2 | Q4 | 24·r + 18 = 24·r + 18 | all values (identity) |  |  | infinite solutions | match |
| Test | Key/Guide | p3 | Q5 (4⅓ read as 13/3) | 5·x - 18 = -7 | 11/5 |  |  | x = 11/5 | match under this reading; ambiguous (E16) |
| Test | — | p3 | Q5 (4⅓x read as 4·⅓x) | 2·x - 18 = -7 | 11/2 |  |  | — | second reading gives 11/2 |
| Test | Key/Guide | p3 | Q6 | y = −4x + 6 drawn; add a parallel line | any y = −4x + b, b ≠ 6 |  | x −8..8 × y −10..9 (non-square) | same | match; drawn line fitted −3.97x + 5.87 |
| Test | Key/Guide | p4 | Q7 | (8, 5) in y = 2 - 9·x/4 ; y = 3·x - 19 | 2nd only → not a solution |  |  | No | match; false lines printed with "=" (E10) |
| Test | Key/Guide | p4 | Q7 | (4, -7) in y = 2 - 9·x/4 ; y = 3·x - 19 | both → solution |  |  | Yes | match; false lines printed with "=" (E10) |
| Test | Key/Guide | p4 | Q7 | (-4, 11) in y = 2 - 9·x/4 ; y = 3·x - 19 | 1st only → not a solution |  |  | No | match; false lines printed with "=" (E10) |
| Test | Key/Guide | p5 | Q8 | y = 5 - x ; y = x + 1 | (2, 3) | lattice | −2..6 × −2..6 | (2, 3) is a solution of both | match; graph fitted |
| Test | Key/Guide | p6 | Q9 | y = 3·x/2 - 3 ; y = 4·x + 2 | (-2, -6) | lattice | −8..10 × −10..8, non-square | (−2, −6) | match; graph fitted |
| Test | Key/Guide | p6 | Q10 | y = -2·x - 1 ; y = 2·x/3 + 8 | (-27/8, 23/4) ≈ (-3.375, 5.750) | not lattice | −8..8 × −8..10, non-square | approx (−3.5, 5.75); exact (−3.375, 5.75) | match; graph fitted |
| Test | Key/Guide | p7 | Q11 | y = 197·x/20 + 117/2 ; y = 327·x/20 | (9, 2943/20) ≈ (9.000, 147.150) | not lattice | 1 h × $10 | "approximate" (9, 147.15) | exact value keyed as approximate; rubric (E15) |
| Test | Key/Guide | p8 | Q12 | y = 10 - 5·x/2 ; y = 10 - 5·x/2 | infinitely many (same line) | — | −9..10 × −2..10 | same slope; infinite | match; key stem differs (E1) |
| Test | Key | p6 | Q12 key stem as printed | y = 10 - 2·x ; y = 10 - 2·x | infinitely many (same line) | — | — | — | key stem system is not the test system (E1) |
| WE | WE | p1 | #1 | 1069/20 = 17·t/2 + 559/20 | 3 |  |  | t = 3 | match |
| WE | WE | p1 | #2a | 4·y - 16 = 12·y + 24 | -5 |  |  | y = −5 | match |
| WE | WE | p1 | #2b | -18·p - 11 = 7 - 5·p | -18/13 |  |  | p = −18/13 | match |
| WE | WE | p1 | #3a | 2·b + 6 = 6·b + 5 | 1/4 |  |  | one solution | match (b = 1/4) |
| WE | WE | p1 | #3b | 6·b + 6 = 6·b + 18 | no solution |  |  | no solutions | match |
| WE | WE | p1 | #3c | 3·b + 3 = 6·b + 18 | -5 |  |  | one solution | match (b = −5) |
| WE | WE | p1 | #4 (as worked, −½) | y = 5 - x/2 ; y = 6 - x/4 | (-4, 7) | lattice | — | x = −4, y = 3 | WRONG: y = 7 (E2) |
| WE | WE | p1 | #4 (if typed +½) | y = x/2 + 5 ; y = 6 - x/4 | (4/3, 17/3) ≈ (1.333, 5.667) | not lattice | — | — | (−4, 3) fails this reading too |
