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


---

# The review pass (14 November 2026) — three readers who had not seen the specs

After the seven lessons, the unit papers and the package were built at 0 findings, three independent readers went over
the built unit: an adversarial critic, a Barton audit against HOUSE STYLE §16, and a Florida educator reading it
against the benchmarks and FAST's item shapes. **None found a wrong answer, key, worked line, classification or
graph.** Counts: critic 1 blocker, 9 major, 10 minor; Barton 0 / 11 / 13; FAST 1 / 8 / 7 — the two blockers are one
item (the Practice Test's 14(b) accepted a half-grid point that is on one line only; it now accepts 1.6–1.8 and
2.6–2.8, and the build checks that no printed grid point falls inside any accepted range). The lead's rulings on each
finding follow, as given to the builders; the three reports are below them, whole. The fixes were made in a second
pass and the unit rebuilt and reinstalled at 0 findings.

## The rulings — what is taken, what is not

**Taken as the reviewer proposes (or better):**
- critic 1 = fast 1: Practice Test 14(b) accepts x from 1.6 to 1.8 and y from 2.6 to 2.8 (the range must exclude every
  point that is on one line only). Check every other approximate item in the unit the same way (fast 15: state every
  tolerance one way — "within 0.1 of").
- critic 4, 5, 6, 8, 13, 14, 16, 17, 19, 20; critic 11 (11.08 Example 2 becomes liters, not pages); critic 7 (the
  vocabulary slide's "parallel lines": lines that never meet — the same number multiplies x and the numbers added are
  different; then "the same line" has its own line).
- critic 12 = fast 4: the select-all with exactly one right answer goes. Practice Test question 8, the Review's
  matching question and 11.05's independent question 3 become: **"Select all the systems that have (a, b) as a
  solution"** — five systems, each solved for y, two or three of them right, each wrong one true in exactly one of its
  equations; the stem never says how many. Remove "at most one can pass" from the Reference Sheet.
- barton 3 (11.05–06 is overloaded): do what the reviewer lists — move what it says to 11.07, drop what it says.
- barton 4, as far as Croix's ruling 37 allows: one move per line in every worked row and notes row (never two or three
  moves on a line; 11.04 Notes I shows every move); equals signs aligned wherever the kit's layout permits. The move's
  name stays in the spec's gloss and the Teacher Edition — ruling 37 took the grey glosses off the slides and that
  stands, so do NOT add words beside worked rows on slides.
- barton 5 (11.04's two example pairs go to the techniques that need them), barton 9 (writing an equation from a story
  is modeled before it is practiced — one notes row or an example in 11.01 or 11.02 and again for systems in 11.08),
  barton 11, barton 8 (the Review's SSDD block is replaced by the reviewer's one-context, four-structures block).
- barton 7: each Wednesday spec (11.03, 11.07) names its 43-minute cut in the Teacher Edition — which boards go, which
  independent questions go home — and the Lesson Plan's minutes add to 43 if the kit lets a spec say so (see how a
  43-minute lesson in a7/build/u6 or u5 does it; if the kit has no way, say so in the TE's first slide note).
- barton 2 and critic 3 / barton 1, within the kit: a Your Turn slide cannot carry a figure and a paper's key prints
  the same figure as its page — both are KIT limits the lead is taking to Croix; do not hack around them. Do this
  instead: (i) every graph-day Your Turn is answerable from what its slide shows — its two tables of values set out in
  rows (typeset text/math), the crossing found where the tables agree — and its system crosses INSIDE the table the
  example models (11.07 Your Turn 2 must not cross at x = −4 when the taught table is x = 0, 2, 4); no reveal states
  a crossing nobody could have found; (ii) in 11.07 the FIRST question of the Independent Set is drawn during the
  lesson, right after Example 1, with the teacher circulating (say so in the Teacher Edition and the Lesson Plan, and
  give it minutes), so somebody graphs under the teacher's eye before the silent set; (iii) barton 24 / critic 10: an
  Example's question slide shows the EMPTY grid (or the two tables), not the solved graph; the solved graph appears
  only on a reveal or a following notes-style slide.
- fast 2, 3 and barton 10 — rational coefficients at the state's level: a negative fraction coefficient and a negative
  decimal factor on SLIDES (11.04 notes or example, and boards), in the Review and on the Practice Test; decimal
  factors whose products are not all whole; one state-shaped equation in 11.04 (the reviewer's −2.4(5x − 3) = −40.8
  or better). The Practice Test gets a fraction-coefficient equation: question 3 (parentheses on both sides) carries a
  fraction multiplier on one side. Keep the paper at 14 questions, 18 points, the same four sections and tracker.
- fast 5: one horizontal line (y = 4 with a slanted line) on a 11.05 or 11.07 board and in the Review; the notes' rule
  for parallel is worded so a horizontal pair fits it.
- fast 8: the words **intersect / point of intersection** and **coefficient of x** are taught (vocabulary slides of
  11.05 and 11.07; used in the Practice Test's stems where natural). "Slope" and "y-intercept" stay off student pages.
  Add to `manifest.py`'s notes the hand-off the reviewer writes: Unit 10 names the coefficient of x as the slope and
  re-reads this unit's parallel lines with that word; the spring review asks one AR.4.3 item that says "slope".
- fast 9: reword the Practice Test's stems to FAST's house style per the reviewer's table (short stems, "An equation is
  shown.", "x =" answers, the direction leading on the multiselect) wherever the question's KIND, ORDER and POINTS do
  not change. Where the table would change a kind (a matching grid, a dropdown sentence), make that change in the
  Review or a lesson's independent set instead, not on the paper — the practice web page is being built from the
  paper's 14 kinds right now.
- fast 13, 14, 16; barton 12–22 (the minors) wherever the fix is a wording or number change in a spec.

**Not taken (do not act on these):**
- critic 9 = fast 7 (IXL skills 9Z8, TS7, AGZ may need slope): the plan's skills are Croix's; the build refuses any
  other. The lead reports it to him. Do not change `ixl`.
- critic 2 (keys with drawn graphs), critic 15, barton 6's line weight, barton 23 ("neighbour"): kit; reported.
- fast 6's second half (question 13(a), a table value, stays — graphing from a table IS this unit's method), fast 10
  (the weighting stays 9 / 2 / 2 / 5), fast 12.
- The Practice Test keeps its story question 7 (fast 3's second half): two plans that cost the same is 11.02's own
  board and the district's item shape.


**Left as the reviewers found them, and why:** 11.07's board 4 stays free response (as multiple choice its graph is
1.5 in tall); 11.05 keeps critic 7's definition of parallel lines over barton 3's shorter one; equals signs are not
aligned (the kit centers notes rows); three board reveals still carry two moves on a line (the slide has no room for
more rows).


---

# Report · The adversarial critic

## A7 Unit 11 — adversarial critic's findings

**Bottom line.** I found no wrong answer, no wrong worked line, no mis-classified equation, no wrong distractor and no graph whose lines, labels or marked crossing disagree with its equations — every one of those I recomputed or looked at holds.
The defects are on the graph days and are about what a student or teacher can actually do with the page: one arguable accepted range on the Practice Test, keys with empty grids, Your Turns that ask for a graph with no grid, grids whose scale the given line misses, and estimate graphs too small for "nearest tenth".
Counts: 1 BLOCKER (arguable key, narrow), 9 MAJOR, 10 MINOR.

How I worked: read all seven specs (every stem, step, choice, named error, `wrong` line, key and `why`) and re-derived each by hand; read `unit.py` (Practice Test, Review, Reference Sheet); rendered and looked at every slide of 11.05, 11.07 and 11.08, the notes/examples/boards of 11.03 and 11.04, the Independent Sets and keys and both banks of 11.05, 11.07, 11.08, the Practice Test and the Review; checked every `figs.plane` window against its lines and crossing; ran a script for repeated equations inside each lesson. Not viewed as images: the 11.01 and 11.02 decks (text and spec only), the bank keys other than 11.07's, the Reference Sheet PDF (spec only), Teacher Editions and Lesson Plans (grep only).

---

### Findings

#### 1. BLOCKER (arguable key) — Practice Test 14(b): the accepted range takes in the error the key itself names
- **Where:** Practice Test and Key, question 14(b) (y = x + 1 and y = −2x + 6, "estimate to the nearest tenth").
- **What it says:** exact (5/3, 8/3); "Accept x from 1.5 to 1.9 and y from 2.5 to 2.9"; "(2, 3) is the nearest grid point, on y = x + 1 only" is marked wrong.
- **What is wrong:** this graph is printed with half-unit grid lines. (1.5, 2.5) is therefore a grid point, it is on y = x + 1 only (−2(1.5) + 6 = 3), and it is exactly the "nearest grid point" misreading — yet it sits inside the accepted range. The crossing is visibly off that grid point. One student is refused for (2, 3) and another credited for (1.5, 2.5), the same mistake one grid step finer.
- **Fix:** accept x from 1.6 to 1.8 and y from 2.6 to 2.8 (±0.1 of 1.7, 2.7), and add "(1.5, 2.5) is a grid point on y = x + 1 only." If the wider band is wanted, drop the half-unit grid lines from this figure so that 1.5 is an honest estimate.

#### 2. MAJOR — Every key for a "graph both lines" question prints an empty grid
- **Where:** 11.07 Independent Set Key q1–q5; 11.07 Question Bank Key q6–q7 and Additional q6–q7; 11.08 Independent Set Key q3, q5, q6; 11.08 bank keys q6–q7; Review Key q15.
- **What it says:** the answer in words ("(1, 4)", "No solution", "Club A: $24 against $30") under the student's blank grid.
- **What is wrong:** the question is "solve by graphing"; the thing to be marked is the drawing, and the key does not show it. A teacher (or a substitute, or a student self-checking the Review at home) has no picture to compare against — worst for the parallel, same-line and estimate items, where the drawing is the whole answer.
- **Fix:** on key pages draw both lines and mark the crossing (the figures already exist for the read-a-graph items: pass `lines=` and `solution=` to the key's grid).

#### 3. MAJOR — Your Turns on the graph days carry no graph or grid, so they are not the same kind as their examples
- **Where:** 11.05 Your Turn 2 (slides 14–15); 11.07 Your Turns 1 and 2 (slides 10–11, 14–15); 11.08 Your Turns 1 and 2 (slides 10–11, 14–15).
- **What it says:** 11.05: Example 2 reads a graph of parallel lines; the Your Turn prints only "y = −x + 4 and y = 2x − 5. How many solutions?" and the reveal says "they cross at (3, 1)". 11.07: "Solve the system by graphing" on a blank slide, twice. 11.08: Example 1 reads a story graph; Your Turn 1 (Mia and Noah, equal at 12 weeks) has no graph; Example 2 is a story graph, Your Turn 2 is a bare "y = 4x and y = 2x + 3 — solve by graphing", crossing at (1.5, 6).
- **What is wrong:** (a) not the same kind as the example (read a graph vs. no graph). (b) 11.07 and 11.08 ask the class to draw two lines on a blank whiteboard in two minutes — the unit's own standing decision 9 says a blank whiteboard is no place for two lines. (c) 11.07 Your Turn 2 crosses at (−4, 1): the taught table (x = 0, 2, 4) gives 3, 4, 5 and −3, −5, −7, lines that move apart; the spec's own note admits it. (d) 11.08 Your Turn 1 needs a table out to x = 12 or the 10x + 40 = 5x + 100 bridge, which is "taught and not tested". (e) no reveal shows a graph or a table, so a wrong board cannot see what right looks like. (f) 11.05's reveal states a crossing nobody could have found.
- **Fix:** put the figure on the slide. 11.05: the graph of the two lines. 11.07: an empty grid on the question slide and the drawn lines on the reveal; replace Your Turn 2 with y = ½x + 3 and y = −x + 9 (tables at 0, 2, 4: 3, 4, 5 and 9, 7, 5; solution (4, 5)) so it matches Example 2. 11.08: give each Your Turn its graph (Mia/Noah on 0–16 weeks, 0–200 dollars; y = 4x and y = 2x + 3 on 0–3, 0–9). If the kit's Your Turn slide truly cannot hold a figure, make these boards instead and say so in the plan.

#### 4. MAJOR — "Graph both" story grids are scaled so the given line misses the grid lines
- **Where:** 11.08 Independent Set q5 and q6; 11.08 Question Bank q6.
- **What it says:** q5: y = 2x + 12 on a grid numbered by 5s. q6: y = 4x + 25 and y = 4x + 40 on a grid numbered by 10s. Bank q6: y = 4x + 9 on a grid numbered by 7s.
- **What is wrong:** the first point every student plots is x = 0. That is 12 on a 5-grid, 25 on a 10-grid (then 29, 33, 37), 9 on a 7-grid. In bank q6 the only point of y = 4x + 9 on a grid line is the crossing itself. A class that has drawn lines for three days cannot draw these accurately, and q6's "parallel" depends on an accurate drawing.
- **Fix:** q5: `ys=4` (12, 16, 20 and 0, 20, 40 all land on lines). q6: `ys=5` (25, 45 and 40, 60 land at x = 0 and 5). Bank q6: `ys=3` (9, 21, 33 and 0, 21, 42 land).

#### 5. MAJOR — 11.07 Independent Set q2: the taught table falls off the printed grid
- **Where:** 11.07 Independent Set q2, y = x − 1 and y = −2x − 4, grid x −4 to 3, y −5 to 4.
- **What is wrong:** the vocabulary slide defines a table as "x = 0 first, then two more" and every model uses 0, 1, 2. For y = −2x − 4 that gives −4, −6, −8: two of three points are below the grid. Only negative x works, and nothing says so (the key quietly uses x = −2, −1, 0).
- **Fix:** grid `(-4, 3), (-8, 4)`, or add to the stem "Use x = −2, −1 and 0."

#### 6. MAJOR — Estimate "to the nearest tenth" from graphs about 1.3 inches wide
- **Where:** 11.08 Question Bank q3 and q9, Additional q3 and q9, Review q17 (figures set at `inches=2.2`–`2.8` including labels).
- **What is wrong:** the plotted area of bank q3 is about 1.3 in for 6 units — 0.22 in per unit, so a tenth is half a millimetre. The stem asks for more than the picture can give; the key then has to accept ±0.2, which takes in (1.5, 2.5).
- **Fix:** crop each estimate window to the crossing (0–3 by 0–5, as board 4 does) and print it at 3 in or more; or ask "to the nearest half". Keep one policy across the lessons and the test (see finding 1).

#### 7. MAJOR — 11.05 vocabulary: "parallel lines … the same number multiplies x in both equations" is also true of one line written twice
- **Where:** 11.05 slide 4 (Vocabulary); Notes III's only rule line is "Different numbers multiply x: the lines cross once."
- **What is wrong:** Notes III's third picture (y = ½x + 1 and y = 0.5x + 1) has the same number multiplying x and infinitely many solutions. A student who learns the slide's wording answers "parallel, none" for board 6, Independent q6 and bank q9. The Reference Sheet has it right ("the same number multiplies x and different numbers are added").
- **Fix:** slide 4: "lines that never meet: the same number multiplies x, and different numbers are added". Notes III line: "Different numbers multiply x: cross once. Same number, different number added: parallel. Same equation: one line."

#### 8. MAJOR — 11.05 board 6: the figure on the question slide is about an inch wide
- **Where:** 11.05 slide 26 (set at `pt=14`); the answer slide's copy is larger.
- **What is wrong:** the question depends on seeing one line with two marked points (option D, "two", is those two points). On a 13-inch slide the plane is roughly 1.2 in wide; the dots are specks from the back row.
- **Fix:** size it as boards 3 and 5 are, and shorten the stem to make room. Also smaller than they should be on reveal slides: 11.07 board 2's tables and board 6's figure.

#### 9. MAJOR (unverified — needs Croix's eyes on IXL) — two IXL skills may need what the unit does not teach
- **Where:** 11.05 slide 35, "Solve a system of equations in slope-intercept form — 9Z8"; 11.07 slide 35, "Write a system of equations given a graph — TS7".
- **What is wrong:** (a) 9Z8 is assigned on 11.05, when the class cannot yet solve a system by any method (graphing is 11.07); if IXL expects an algebraic solve it is substitution, which this unit never teaches. (b) TS7 asks for equations written from a graph, which normally means slope and y-intercept; the unit only ever tests given options against points (board 6). (c) "slope-intercept" is printed on a student slide, against standing decision 2. I could not open IXL from here, so (a) and (b) are risks, not confirmed defects.
- **Fix:** try five questions of each as a student. If they need algebra or slope, drop them or move them to Unit 10; if 9Z8 stays, move it to 11.07.

#### 10. MAJOR — 11.07 Example 1's question slide already shows the solved graph
- **Where:** 11.07 slide 8 (and Example 2, slide 12, with the crossing dotted).
- **What it says:** "Solve the system by graphing" above both tables, both lines and the label "(3, 3)".
- **What is wrong:** the lesson's one skill is building the graph; the slide gives the class nothing to build and the answer to read. Paired with finding 3, no student draws a line in 11.07 until the Independent Set.
- **Fix:** question slide: the two equations and an empty grid; worked slide: tables, lines, crossing.

#### MINOR

11. **11.08 Example 2** — "After 2.5 minutes, both have printed 7.5 pages." Half a page is a strained answer for a counted thing. Fix: make it liters (Hose A fills 3 L a minute; Bucket B has 5 L and gains 1 L a minute) — same numbers, same graph.
12. **Select-all with exactly one answer** — Practice Test q8, Review q8, 11.05 Independent q3. Mathematically forced (two crossing lines), and the key says so, but FAST multiselects normally have two or more; a careful student will hunt for a second and doubt a right answer. Fix: keep one of the three and make the test's version the same-line kind used in the 11.05 banks (three correct), or say "Select all that apply; there may be only one."
13. **11.07 Question Bank q11** — the point labels "(1, 4)" and "(2, 3)" are struck through by the dashed line. Move them to the left of their points.
14. **Reference Sheet §4** — "A fraction multiplying x: use even x." True for halves only (⅔x appears in 11.05 bank q3). Fix: "A half multiplying x: use even x (for thirds, multiples of 3)."
15. **Independent Set slide (slide 34) of 11.05, 11.07, 11.08** — says "the graphs … are shown" and "the tables are for" with no figure, and 11.05 q3 shows no options. Harmless if every student holds the handout; add "on your handout".
16. **11.08 board 4** — the reveal redraws the system in a different window (−1 to 4, −1 to 6) from the question (0 to 3, 0 to 5), smaller. Use the question's window with the crossing marked.
17. **Handout figure sizes** — graphs on one page differ in size and weight (11.05 Independent q4/q5/q6; 11.07 Independent q5's grid is heavier than q1–q4; 11.05 Additional q8 is about 0.6 in wide). Set one size per document.
18. **Practice Test q14** — two unrelated systems share one stem and sit side by side; the part (b) graph is beside Mia and Leo's story. The "for part (b)" caption saves it; a separate question 15, or the (b) graph placed under part (b), would be cleaner.
19. **11.01 Lesson Plan, Enrichment** — "which box makes the solution x = 0? (3□ = 46 …)" follows a sentence about the equation with 52; it is not clear which equation is meant. Say "in the board's equation (… = 46)".
20. **11.01 Independent q4 and banks q7–q8** — a decimal factor (0.5(4x + 6) + x = 18) on a day whose notes and boards show none. Deliberate (standing decision 5), and answerable, but untaught at that point; one line under Notes II ("a decimal outside multiplies both terms too: 0.5(4x + 6) = 2x + 3") would cover it.

---

### Checked and found sound (the denominator)

- **Keys and worked lines, re-derived by hand:** all 7 warm-ups (28 items), 21 notes panels, 14 examples and 14 Your Turns, 63 boards with every `steps` line, 42 Independent Set questions, 14 banks (about 170 questions), Practice Test (14 questions, 18 parts), Review (18 questions, 31 parts), every worked line and example on the Reference Sheet. No error.
- **Distractors recomputed from their named errors:** every multiple-choice option on boards and banks of 11.01–11.04 (e.g. 11.04 board 4: −20, 2.5, 2), every `wrong` value quoted for open boards, the Practice Test's quoted wrong answers. All produce the stated value.
- **Classification (one / none / infinitely many):** every equation in 11.03, 11.04, Practice Test q5–q6, Review q4 and q6, simplified by hand. All correct, including the x = 0 cases.
- **Fill-the-box items:** each has exactly one valid answer (11.01–11.05, 11.07, 11.08 boards and banks; PT q6; Review q4, q9, q18).
- **Ordered-pair items:** every pair tested in both equations; each "one equation only" distractor satisfies exactly the equation named (where a "swapped" option happens to satisfy one equation, it is still not a solution). Same-line select-alls (11.05 banks) have exactly the keyed three.
- **Select-all items in 11.01–11.04, 11.07, 11.08:** no secretly correct option; no two options with the same value.
- **Graphs:** every crossing solved and found where the picture marks it; every line passes through the points its equation gives; every window contains its crossing; tables of values have no wrong entry (11.07 board 2, Independent q6, banks q3; PT q13; Review q14). Story graphs: axis names fit both lines, no negative time, crossings inside what the story allows (candles stop at 0 cm; tanks and phones stop at 0).
- **Sequence:** no fraction coefficient before 11.04 (decimals only, by decision 5); no "slope" or "y-intercept" on a student page except the IXL skill name (finding 9); no substitution or elimination; no ×, "homework", "calculator" or partner work on a student page.
- **Repeats (ruling 43):** no practice equation or system repeats one from the same lesson's warm-up, notes or examples (script over all seven specs, plus the figure-only boards by eye).
- **Practice Test against the lessons:** every question type is taught and practiced (q13(a)'s missing table value is 11.07 warm-up 4; q14's falling line is 11.07 board 7 and the tank and phone banks); each key answers what its question asks.
- **Keys against student pages:** 11.05, 11.07, 11.08 Independent Set keys, 11.07 bank key and the Review key print the same questions as the student pages.


---

# Report · The Barton audit

## A7 Unit 11 — Barton audit (HOUSE STYLE §16, cognitive load, sequence, pacing, test mirror)

**Bottom line.** The four equation days (11.01–11.04) are sound explicit instruction: real example/Your Turn pairs, declared variation with a true boundary case each day, diagnostic boards whose wrong options are the state's named errors. I found no wrong mathematics and no wrong key (0 BLOCKER).
The three systems days are where the method breaks: every graph-based example is followed by a Your Turn with no graph, nobody draws a line while the teacher can see it, the graphs are too small to read from the back, and 11.05–06 carries more than one period holds.
Across all seven decks the worked equations are not laid out for a student to follow (equals signs not aligned, two or three moves on one line, the move itself never written), and the Unit Review's "SSDD" block is one procedure four times, not four different structures.

Counts: **BLOCKER 0 · MAJOR 11 · MINOR 13.** Every replacement number below was solved with sympy before it was written here.

---

### MAJOR

#### 1. The systems Your Turns are not the same kind as their examples (Rule 1 is met in shape only)
**WHERE.** 11.05 slides 12–15 (Example 2 / Your Turn); 11.07 slides 8–15 (both pairs); 11.08 slides 8–15 (both pairs).
**WHAT IT SAYS.** Each example shows a graph (11.07 and 11.08 also show the tables). Each Your Turn slide shows two equations or a story and nothing else. The 11.05 Teacher Edition says why: "the kit's Your Turn slide carries none."
**WHAT IS WRONG.** The example cannot be used as a model, because the thing the example read (a picture) is absent.
- 11.05 Your Turn 2: the example reads *parallel lines from a graph* (no solution). The Your Turn asks "how many solutions" for y = −x + 4 and y = 2x − 5 from the equations alone — a different case and a different method — and the reveal announces "One solution, (3, 1)", a point no student could have produced. A student will either write "none" (copying the example's verdict) or sit still.
- 11.07 Your Turn 1 and 2 say "Solve the system by graphing" to a class holding blank whiteboards (standing decision 9 says a whiteboard is no place for two lines). The reveal solves by tables. Your Turn 2 is a trap rather than a copy: Example 2 crosses inside its table (x = 2); the Your Turn crosses at (−4, 1), and the TE itself notes that a table at x = 0, 2, 4 "never meets". A student who follows the model exactly fails.
- 11.08 Your Turn 1 (Mia and Noah) has no graph; the only route is 10x + 40 = 5x + 100, the bridge the unit says is "taught and not tested". Your Turn 2 asks for (1.5, 6) "by graphing" with no grid.
**FIX.** Let a Your Turn slide carry a figure (boards already do). Then:
- 11.05 Your Turn 2: a graph of **y = 4x + 1 and y = 4x − 3**, "How many solutions does the system have?" → none (parallel; always 4 apart). Drop the named crossing.
- 11.07 Your Turn 1: keep y = x − 2 and y = −3x + 6, print two empty three-column tables and an empty grid on the slide and on a half-sheet (or the grid inserts in dry-erase sleeves the Source of Truth lists for AR.4.1–4.3); reveal shows the filled tables and graph.
- 11.07 Your Turn 2: **y = ½x + 3 and y = −x + 9**, tables at x = 0, 2, 4 give 3, 4, 5 and 9, 7, 5 → **(4, 5)**, inside the table like the example. Move (−4, 1) to a board as the declared boundary case ("the crossing is left of your table").
- 11.08 Your Turn 1 and 2: show the graph, as the examples do.
If the kit cannot be changed before 30 November, turn each of these Your Turns into Board 1 (boards carry figures) and say so in the TE.

#### 2. In 11.07 nobody graphs while the teacher is watching
**WHERE.** 11.07 whole lesson; Independent Set 11.07 (4 pages); Lesson Plan sequence.
**WHAT IT SAYS.** Target: "solve a system by graphing both lines." Boards 1–9 read a finished graph or table. The first time a student plots a table and rules a line is the Independent Set: five systems to graph (ten lines, thirty table values) plus one table question, in 6 silent minutes — "circulate; do not teach" — at the end of a 43-minute Wednesday. The handout prints grids but no empty tables.
**WHAT IS WRONG.** The one new motor procedure of the unit gets no guided practice and no feedback; it will be done at home, where a wrong table produces a wrong line and nobody sees it. The state's named AR.4.3 misconception is "plotting and graphing errors producing wrong solutions" — and no board in the lesson can show the teacher a plotting error, because no board plots. Also, the Example slides (8 and 12) and Notes II show the finished product at once — both tables filled, both lines drawn, the crossing labeled — so the order of the moves (table, three points, ruler, second line, crossing, check) is never seen as a sequence.
**FIX.** (a) Your Turn 1 is drawn on a printed grid (finding 1). (b) Stage Example 1 as three reveals: table and line 1; table and line 2; crossing and check. (c) Print two empty tables beside every grid on the Independent Set. (d) Cut the set to what 6 minutes holds: in class Q1 (whole crossing) and Q6 (two tables — the test's Q13); Q3 (the ½) and Q4 (parallel) go home; drop Q2 and Q5 to the Question Bank. (e) Add to "Misconceptions to Watch": a third point off the line means a y is wrong; a line stopped at its last plotted point misses the crossing.
Note for the decision: the Practice Test never asks a student to draw (Q12–14 all supply the graph). If drawing is deliberately untested, say so in the TE and spend Wednesday's minutes on reading; if it matters, Review Q15 is its only assessed appearance.

#### 3. 11.05–06 is overloaded for one 53-minute period — what should move or go
**WHERE.** 11.05 slides 4–15; Lesson Plan (Notes 10 min).
**WHAT IT SAYS.** In 10 minutes of notes, before any practice: three vocabulary terms; the first graph of a line this class has ever seen, from a table (Notes I); a system, its solution tested by substitution, and the crossing as that solution (Notes II); three cases from three graphs with the reason "the same number multiplies x" (Notes III). Then one example on substitution and one (2 minutes) on parallel lines whose worked line is (½x + 2) − (½x − 1) = 3.
**WHAT IS WRONG.** Four new ideas and two new representations arrive before the student does anything. The reasoning-from-equations strand (same multiplier ⇒ parallel; ½ and 0.5 are one number ⇒ one line) is a second lesson stacked on top of "read the picture" — and 11.07 Notes III teaches it again two days later. The worked line of Example 2 subtracts a bracketed fraction expression, a move heavier than anything in 11.01–11.04, to justify something the graph already shows.
**FIX — keep AR.4.1 and picture-reading; move the reasoning to 11.07; drop the story.**
1. Vocabulary: "parallel lines — lines that never meet." Remove "the same number multiplies x in both equations" from the definition (it is a property, and it is 11.07's).
2. Notes III: three pictures, three counts, nothing else. Replace the caption "Different numbers multiply x: the lines cross once" (which explains only one of the three) with "Cross once: one. Never meet: none. The same line: infinitely many."
3. Example 2 worked slide: replace the subtraction line with a three-column table read off the graph — x = 0: 2 and −1; x = 2: 3 and 0; x = 4: 4 and 1 — "always 3 apart: they never meet."
4. The bridge (x + 2 = −2x + 8) is in the Notes II speaker note: do not say it Monday; 11.07 Notes III prints it.
5. Board 7 (the savings story) goes: reading a crossing in context is 11.08 board 2. Put the extra number (ruling 22) on another board — e.g. board 3, "The system is graphed on a grid 5 units wide. What is its solution?" — and use the freed board for a second same-line or parallel picture, the AR.4.2 case the state names.
6. Order the practice by dependency: boards 1, 2, 4, 8, 9 need only substitution. Consider running Example 1, its Your Turn and boards 1–2 straight after Notes II, before Notes III, so the class has done something with a system before the three cases arrive (the TE can say this without a rebuild).

#### 4. Worked equations are not laid out for a student to follow
**WHERE.** Every Notes slide and worked Example in 11.01–11.04; every board reveal. Clearest cases: 11.01 slides 6, 7, 13; 11.02 slides 5, 6, 13; 11.04 slides 5, 6, 7, 9.
**WHAT IT SAYS / WHAT IS WRONG.**
- **Equals signs do not line up.** Notes lines are centered (3x + 5x − 4 = 28 above x = 4), example lines are flush left. Neither gives a column of "=" to track down the board.
- **Two or three moves share a line.** "6x = 36   x = 6" (11.01 II), "−3x = −15   x = 5" (11.01 III), "7x = 56   x = 8", "2x = 11   x = 5.5", "4x = 20   x = 5". 11.02 Notes II runs each whole route across one line. 11.04 Notes II puts each fraction method on one line in three states.
- **11.04 Notes I skips four moves at once:** 3(2x − 4) + 5 = 2(x + 6) + 1 goes straight to 6x − 7 = 2x + 13 (two distributions and two collections), then "4x = 20   x = 5" (two more). The slide titled "One order for every equation" does not show the order.
- **The move is never written.** In 11.02 Notes I — the one new idea of the day — 5x + 2 = 3x + 10 is followed by 2x + 2 = 10 with nothing between. "Take 3x from both sides" exists only in the heading; "− 3x" under each side is not shown, and the reason (the balance) is in the teacher's voice only. The spec's per-line reasons ("take 4x from both sides", "add 5 to both sides") reach neither the slide nor the speaker notes (the decks have no notes pages and no animations), so a student's copied notes are four bare lines.
- **Clearing fractions has no intermediate line:** x/2 + 3 = x/3 + 5 jumps to 3x + 18 = 2x + 30. The step students get wrong — 6 · x/2 = 3x and 6 · 3 = 18 — is invisible.
- Board reveals are written as prose chains ("Collect: 7x − 8 = 34, so 7x = 42, x = 6"), and error-analysis items print the student's work as one run-on line (11.01 board 9, set Q6), so "which line has the mistake" has no lines.
**A student will:** copy lines they cannot reconstruct; in 11.02 move a term to one side only; in 11.04 multiply only the fractions by the common denominator (the TE's own predicted error, x = 1 on board 5).
**FIX.** One move per line, aligned on "=", in every notes block and worked example; the operation written under both sides in the accent color on the line where it happens (− 3x   − 3x); the short reason from the spec's rows printed small at the right of each line. For 11.04 Notes II add the line 6(x/2) + 6(3) = 6(x/3) + 6(5). For 11.04 Notes I show five lines: distribute, collect, take 2x, add 7, divide. Print error-analysis work line under line.

#### 5. 11.04 spends its two pairs on the wrong things
**WHERE.** 11.04 slides 5–15; Independent Set Q3, Q4.
**WHAT IT SAYS.** Three new techniques in 11 minutes of notes: a fraction distributed, fractions cleared by a common denominator, a decimal distributed. Example 1 and its Your Turn are whole-number multi-step equations (11.02 with one more collection — review). Example 2 and its Your Turn distribute a fraction.
**WHAT IS WRONG.** The two hardest and most important techniques have no pair: clearing fractions (one compressed line of notes, then board 5), and the decimal distribution — the 21% skill and Practice Test Q4 — (Notes III, then board 3). Independent Q4, −2.5(2k − 4) = k − 8, then changes three things at once from anything modeled (negative, decimal, variable on both sides).
**FIX.** Example 1 becomes the decimal: **0.2(10x − 15) = x + 4** → 2x − 3 = x + 4 → x = 7 (check: 11 and 11). Your Turn: **0.6(10x − 5) = 4x + 5** → 6x − 3 = 4x + 5 → x = 4 (check: 21 and 21). Keep Example 2 (fraction distributed) or, better, make it the common-denominator pair and leave the distributed fraction to Notes II and board 2. Board 1 already carries the whole-number case. Set Q4 changes one thing, not three: give it a positive decimal like the test's, and move −2.5(2k − 4) = k − 8 to the Question Bank (or model a negative decimal on a board first).

#### 6. The graphs are too small and too faint to carry the lesson from the back of the room
**WHERE.** 11.05 slides 12, 20, 24, 26; 11.07 slides 16, 19, 20, 22, 24, 27, 28; 11.08 slides 8, 12, 16, 20, 22, 24, 28, 32.
**WHAT IT SAYS.** On a 13.33 × 7.5 in slide the grid itself is typically about 2 in square with most of the slide empty; 11.05 board 6 is 1.5 in including its labels; 11.07 board 2's reveal shrinks both tables to a strip; 11.07 board 6's reveal graph is 1.6 in. Board graphs use hairlines while 11.05 Notes III uses bold lines. 11.08 board 4 — "Estimate the solution", described in the TE as "the estimate at full size" — has grid cells of about 0.4 in.
**WHAT IS WRONG.** These boards ask the class to read a crossing, and one asks for tenths of a cell. From the back the answer is a guess, so a show of boards measures eyesight. The diagnostic value of the wrong answers (swapped, nearest grid point) is lost.
**FIX.** On any slide whose question is the graph, the grid fills the available height (about 4.5 in), lines at the Notes III weight, tick labels at body-text size. On answer slides keep the graph at question size and put the two lines of working beneath it rather than beside a shrunken copy.

#### 7. Pacing: the two 43-minute Wednesdays, nine boards in 13 minutes, six questions in 6
**WHERE.** Lesson Plans and TE "The Period" tables, all lessons; 11.03 and 11.07 in particular.
**WHAT IT SAYS.** Every plan totals 53 (house rule: one plan, the teacher absorbs short days). 11.03 names no cut. 11.07 names one: "boards 7 and 8 first, then the vocabulary slide." Boards get 12–14 minutes for nine questions including two votes with a 60-second re-vote and a written board 9 read aloud. The Independent Set gets 6 minutes for six written questions.
**WHAT IS WRONG.** Ten minutes must come out of the two hardest days and the plan leaves it to the moment. 11.07's suggested cut removes the vocabulary slide — the opposite of Rule 6 (words before the notes use them). Ninety seconds a board is not possible for 11.04 board 5 (clear fractions) or any board 9. Six minutes is one or two questions of an Independent Set, so most independent practice happens at home with no feedback.
**FIX.** Keep the 53-minute plan; add a "43-minute day" line to the TE of 11.03 and 11.07 that names the cut:
- **11.03:** skip boards 5 and 7 (5 is a third copy of Example 2; 7 is the story); board 9 answered aloud, not written; IXL starts outside class. Keep board 8 — it is Practice Test Q6.
- **11.07:** skip boards 6 and 7 (6, "which system has these lines", is a skill nothing in the lesson teaches and the test does not ask) and board 8; keep the vocabulary slide; IXL outside class.
In every TE mark the boards that must happen — the two diagnostics, the boundary case and board 9 — and say that 7 and 8 are first to go. In every Independent Set mark the three questions to do in class.

#### 8. The Unit Review's SSDD block has one deep structure, not four
**WHERE.** Review Q6 a–d; Review Key Q6.
**WHAT IT SAYS.** 4(x − 2) = x + 7; 4(x − 2) = 6x + 2; 4(x − 2) = 4x + 8; 4(x − 2) = 4x − 8. Stem: "Solve each equation. If it has no solution or infinitely many solutions, say so." The key: "the moves are the same every time."
**WHAT IS WRONG.** That sentence is the finding. SSDD exists to break "match a procedure to a surface"; here one procedure answers all four parts, (a) and (b) differ only in the sign of the answer, and the stem announces the other two endings. It is a good minimally-different set (it belongs in 11.03) but it does not make a student choose what kind of problem they are in — which is the unit's real risk: an equation, a pair to test, a system to count and a story all look alike.
**FIX.** One context, four structures (numbers checked; none repeats a lesson item):
"Gym A costs \$36 to join and \$4 a visit. Gym B costs \$10 a visit."
a. Dana has paid Gym A \$64 in all. How many visits? → 36 + 4v = 64, **7 visits** (11.01).
b. After how many visits have the two gyms cost the same? → 36 + 4v = 10v, **6 visits, \$60** (11.02).
c. Is (5, 56) a solution of the system y = 4x + 36 and y = 10x? → **No**: 4(5) + 36 = 56, but 10(5) = 50 (AR.4.1).
d. Gym C costs \$50 to join and \$4 a visit. Will Gym A and Gym C ever have cost the same? → **Never**: 36 = 50 is never true; C is always \$14 more (11.03 / AR.4.2).
Stem: "Answer each part." Keep the name on the key only. Move the present Q6 into the equations section as an ordinary question.

#### 9. Writing an equation from a story is practiced and tested but never taught
**WHERE.** 11.02 board 7 and set Q6; 11.03 board 7; 11.04 board 7 and set Q6; Practice Test Q7; 11.04 TE "Must not".
**WHAT IT SAYS.** "After how many visits do the plans cost the same?" The reveal writes "Plan 1 costs 30 + 5v. Plan 2 costs 8v" and sets them equal. No notes slide or example in 11.01–11.04 models turning two plans into two expressions and an equation; the first model is 11.08 Notes I, six days later. The 11.04 TE lists "Writing the equation from a context (MA.912.AR.2.1)" under **Must not** while its own board 7 and set Q6 require it.
**WHAT IS WRONG.** The first attempt is cold, on a board, and the predicted wrong answers (13v = 30; 30 ÷ 5) are what an untaught student does. Practice Test Q7 then depends on it.
**FIX.** In 11.02, teach it once: use the "two plans" story as the second line of Notes III or run board 7 as a worked example (the teacher writes "cost of plan 1 = cost of plan 2" and the two expressions, the class solves), so set Q6 is its Your Turn. Remove the contradicting clause from 11.04's Must not, or reword it: "writing equations from contexts beyond 'two plans cost the same'".

#### 10. The Practice Test is a fair mirror with one hole: no fraction coefficient
**WHERE.** Practice Test Q1–Q7 against 11.04.
**WHAT IT SAYS.** Q1–Q4 are like terms, both sides with a negative solution, parentheses on both sides, a decimal distributed. No question has a fraction coefficient or a common denominator.
**WHAT IS WRONG.** 11.04's target is "fraction or decimal coefficients", half its notes and its only new-content pair are fractions, and the benchmark says rational coefficients. A student who rehearses the practice paper until it is easy never rehearses a fraction; either the test under-samples what was taught or Friday's fraction time is unassessed.
**FIX.** Make Q3 carry it and keep "parentheses on both sides": **½(8m + 6) = 3(m + 2)** → 4m + 3 = 3m + 6 → **m = 3** (check: 15 and 15). If fractions are meant to stay off the test, say so in 11.04's TE and trim Notes II to the distributed fraction.
**The rest of the mirror, for the record.** Taught and practiced but not on the paper: drawing a graph; "which plan costs less after the crossing" (11.08 boards 5 and 9, set Q5); writing a system from a story (11.08 board 6, set Q4); a system from four points (11.07 board 6). On the paper with a twist the lessons did not practice: Q6's extra "− x" before the box (11.03's box items have no collecting step); Q14's Leo "spends \$4 each week" — no 11.08 story decreases (harmless here, since the graph is given). Everything else on the paper has a same-kind board or set question.

#### 11. 11.01: the hardest idea has no pair, and its first practice reverses the model
**WHERE.** 11.01 slide 7 (Notes III), boards 5 and 6.
**WHAT IT SAYS.** Notes III: 18 − 3(x − 2) = 9, with (−3)(−2) = +6. There is no example or Your Turn for a subtracted group; Examples 1 and 2 are collecting and a plus-distribution. The first attempt is board 5, 15 − 2(w + 1) = 5, where (−2)(+1) = −2.
**WHAT IS WRONG.** The only model the student has shows the inside number turning positive. On board 5 they reproduce that: 15 − 2w + 2, w = 6 — the first wrong answer the TE lists. The declared "pattern break" lands before the pattern exists. Nothing on slide 7 points at the −3 (the arrows are in the ESE note only).
**FIX.** Swap boards 5 and 6: board 6 (12 − 3(x − 4) = 6, "which is a correct next step?") has the same shape as Notes III and works as its Your Turn; 15 − 2(w + 1) = 5 then follows as the variation, and the TE's Variation note says so. On slide 7 draw the two arrows from −3 and color the −3 and the +6.

---

### MINOR

#### 12. 11.03 boards never show an ordinary single solution
**WHERE.** 11.03 boards 1–9. **WHAT.** Infinitely many, none, x = 0, infinitely many, none, "which has none", none, fill the box, infinitely many. The only one-solution board is the x = 0 case. **WRONG.** "If one, find it" is exercised once, and only with zero; the three-way discrimination the test's Q5 needs is practiced as a two-way one. Board 5 is also a third copy of Example 2. **FIX.** Board 5 → **6x − 9 = 3(x − 4)**: 6x − 9 = 3x − 12, 3x = −3, **x = −1** — it looks like the no-solution kind until distributed.

#### 13. The decimal factor is set before it is taught
**WHERE.** 11.01 set Q4, 0.5(4x + 6) + x = 18; 11.02 set Q5. **WRONG.** Standing decision 5 puts the 21% skill in front of the class daily, but its first two appearances are in silent independent work with no model; Notes III of 11.04 is the first teaching. A student will write 2x + 6. **FIX.** 11.01 board 3 (a near-copy of Example 2 and its Your Turn) → **0.5(6n + 4) + 2n = 22**: 3n + 2 + 2n = 22, **n = 4**. Add to Notes II: "A decimal outside works the same way."

#### 14. 11.05 notes graphs point at the wrong thing
**WHERE.** 11.05 slides 6, 7. **WHAT.** Notes II labels (0, 2) — the pair that is *not* a solution — with a large dot, and leaves the crossing (2, 4) unlabeled; its y-axis counts by 2 while x counts by 1, on the first system graph the class sees. In Notes III the "same line" picture is a single blue line. **WRONG.** Attention goes to the non-solution; and one line on a grid does not look like two equations. **FIX.** Label the crossing "(2, 4)" in bold and mark (0, 2) lightly; use equal scales; draw the second equation as orange dashes on top of the blue in the third picture.

#### 15. Several diagnostic boards spend two options on one misconception
**WHERE.** 11.02 board 6 (A and B both one-term distribution); 11.03 board 4 (A and D both "variable = constant"); 11.04 board 6 (B and D the same); 11.05 board 6 (A and C both cited to the same-line case). **WRONG.** Two options, one reteach; a named error goes untested. **FIX.** 11.02 board 6: option B → **x = 1** (4(−2) taken as +8: 4x + 8 = 2x + 10) — the state's "sign errors while distributing", absent from that board. The others are tolerable as built; note in the TE that A and D get the same response.

#### 16. 11.07 board 4 lost its vote; board 6 tests what was not taught
**WHERE.** 11.07 boards 4, 6. **WHAT.** The outline has board 4 as multiple choice (the crossing, the swap, two axis points); it was built free-response with those three errors listed. Board 6 asks which system passes through four points. **WRONG.** Board 4's errors are exactly a diagnostic set and a show of boards would sort them. Board 6 has no notes or example behind it and is not on the test. **FIX.** Restore board 4 as multiple choice: (2, 1) ✓ · (1, 2) · (0, 5) · (1, 0). Then board 6 can be skipped on the short day without dropping below two diagnostics.

#### 17. Warm-up bands and sources
**WHERE.** TE warm-up lines, 11.02, 11.03, 11.05, 11.07, 11.08. **WHAT / WRONG.**
- Four fourth questions cite "7th grade" as the source. This class is in 7th grade; the lesson number is what the rule asks for. 11.02 Q4 (2x − 5x) is yesterday's like terms, so questions 1 and 4 retrieve the same lesson.
- 11.03 Q1 and Q2 are 11.02 and 11.01 — one and two days old; no question reaches last week.
- 11.08 Q4, "halfway between 2 and 3", is not what the day leans on. The day leans on turning "a start and an amount per one" into numbers.
**FIX.** Name the lesson each fourth question retrieves, as the other three lines do (11.02 Q4 is 11.01; for the others, the Unit 1 lesson where a solution was checked or an expression evaluated). 11.03 Q2 → a T-B2 angle question. 11.08 Q4 → "A gym costs \$15 to join and \$4 a visit. What do 5 visits cost?" (\$35).
All four questions in every lesson are retrieval; none previews new content.

#### 18. 11.03 Your Turns give away their verdict
**WHERE.** 11.03 slides 10, 14. **WRONG.** Example 1 is "infinitely many" and so is its Your Turn; Example 2 and its Your Turn are both "no solution". A board can be right without simplifying anything. **FIX.** Ask for the last line as well: "Write the line you end on, and what it means." The TE checks for −2 = −2, not the words.

#### 19. 11.02 Notes II teaches two routes on the day the first is new
**WHERE.** 11.02 slide 6. **WRONG.** Two solutions of one equation side by side, each on one line, the day the move is introduced; board 9 does the same job later, in writing. **FIX.** Notes II shows one route (take the smaller term) laid out line under line, with the sentence "Taking 6x instead also works; board 9." Leave the comparison to board 9.

#### 20. 11.08's exit evidence is the untested skill
**WHERE.** 11.08 boards 5 and 9, set Q5; Notes II. **WRONG.** "Which costs less after the crossing" gets one sentence of notes, two boards, and the written exit board — and is not on the test. The estimate (test Q14b, taught the day before the test) gets boards 3–4 only. **FIX.** Make board 9 an estimate with its check written out ("Estimate the crossing of … and show that your estimate is close in both equations"), and keep board 5 as the one "cheaper side" question.

#### 21. 11.07 board 5's stem presumes a solution
**WHERE.** 11.07 slide 24: "The system is graphed. What is its solution?" over parallel lines. **WRONG.** A fair boundary case, but 11.05 board 5 asked "How many solutions?" for the same picture; here the stem tells the class there is one. **FIX.** Keep the trap but say so in the TE's Variation note, or use "Solve the system."

#### 22. Practice Test Q14 prints two unrelated graphs side by side
**WHERE.** Practice Test page 6. **WRONG.** Part (b)'s graph (y = x + 1, y = −2x + 6) sits beside Mia and Leo's and has nothing to do with them; a student reads the wrong picture. "To the nearest tenth" from a graph about 1.3 in wide is finer than the picture supports (the key sensibly accepts 1.5–1.9 and 2.5–2.9). **FIX.** Make (b) its own question 15 with its own stem and a larger grid; word it "Estimate the solution" and let the key's range stand.

#### 23. "neighbour" in the Teacher Editions
**WHERE.** TE 11.01, 11.02, 11.03, 11.05, 11.08 (ten instances): "convince your neighbour". **WRONG.** House style is American English; the specs say "neighbor", so the string comes from the shared kit. 11.04's spec says "sixty seconds to think again" instead — inconsistent with the other six. The specs for 11.07 also contain "practised" (in read-first text; I did not find it in a printed PDF). **FIX.** "neighbor" in the kit string; "practiced" in l07.py.

#### 24. Example slides in 11.07 and 11.08 show the answer before the example is worked
**WHERE.** 11.07 slides 8, 12; 11.08 slides 8, 12. **WRONG.** The prompt slide already carries the filled tables, both lines and (11.07) the labeled crossing; the "worked" slide then drops the graph and lists numbers. There is nothing left to work. **FIX.** Prompt slide: the equations and an empty grid. Worked slide(s): the tables, then the graph with the crossing (see finding 2b).

---

### Checked and found sound

- **Rule 1, equations.** All eight pairs in 11.01–11.04 are true pairs: same structure, new numbers, one small change (e.g. 5x + 9 − 2x = 30 → 7x − 3 − 4x = 24). 11.05 Example 1 and its Your Turn are a true pair. Every Your Turn note in the TE says what it catches.
- **Rule 2.** Every TE carries a Variation paragraph that can be checked against the boards, and each equation day has a real boundary case in the right place: a negative solution with the larger term on the right (11.02 board 3), x = 0 (11.03 board 3, set Q4, Notes III), an identity hidden by a fraction (11.04 board 6), parallel lines (11.05 board 5, 11.07 board 5). 11.03 Notes I — three equations differing by one number — is the best slide in the unit. The independent sets follow the boards' path.
- **Rule 4.** Every multiple-choice board has every wrong option named in the TE, and each named error is one the state lists for AR.2.1, AR.4.1, AR.4.2 or AR.4.3 or a plain slip a student makes (x-terms added, a constant moved the wrong way, coordinates swapped, one equation checked). I re-derived the distractors of 11.01 boards 4 and 6, 11.02 boards 4 and 6, 11.04 board 4 and 11.05 board 4: each follows from its stated error. The same-line board (11.05 board 6) and "only the two marked points" hit the state's AR.4.2 and AR.4.3 wording directly.
- **Rule 5.** Four questions in every warm-up, all retrieval, none previewing; the fourth is the day's prerequisite in 11.01, 11.04, 11.05 and 11.07.
- **Rule 6.** Every new term is on the vocabulary slide before the notes use it (checked all seven). The reasons exist and are right — why the same term comes off both sides, why 5 = 9 means no number works, why the crossing is the solution — but they sit in the speaker text; findings 3 and 4 are about getting them onto the slide.
- **Sequence 11.01 → 11.04.** Each day's prerequisite is the day before; 11.03's endings are carried into 11.04 (board 6, set Q5) and into systems.
- **No slope, no y-intercept, no ×, no benchmark code** on any student slide I viewed; systems are always given solved for y.
- **Practice Test.** Q1–Q14 each match a board or set-question kind from the lessons apart from the points in finding 10; the 9 : 2 : 2 : 5 weighting matches the days.

**Not audited:** the Question Banks and Additional Question Banks, the keys' arithmetic (machine-checked by the build), the Reference Sheet, and the IXL skill lists.


---

# Report · The FAST item review

## A7 Unit 11 — review against the state (FAST Grade 8 / B.E.S.T. / B1G-M)

**Bottom line.** The unit stays inside all four benchmarks (no standard form, no substitution or elimination demanded, no vertical line, no inequality, no third equation), teaches the three endings and the same-line case the way the B1G-M asks, and its "before slope" wording is mathematically honest. One key is arguable (Practice Test 14b accepts a printed grid point that lies on one line only).
The real gap is level and coverage, not correctness: "rational coefficients" is taught with friendly numbers only (no negative fraction anywhere, a negative decimal in three bank/set items and never on a slide, the test or the review, never a decimal constant), and the Practice Test has no fraction-coefficient equation at all.
The test is benchmark-shaped but not FAST-shaped: no "An equation is shown.", no "x =" response, no matching grid, no dropdown sentence, and its one multiselect always has exactly one key. Counts: 1 BLOCKER, 8 MAJOR, 7 MINOR.

---

### Findings

#### 1. BLOCKER — Practice Test 14(b): the key's accepted range includes a grid point that is on one line only
- **WHERE.** Assessment / Practice Test, question 14(b), and its key (`unit.py` q14, the `why` and the two range checks).
- **WHAT IT SAYS.** "Estimate the solution of that system to the nearest tenth." Key: about (1.7, 2.7); "Accept a careful read with x from 1.5 to 1.9 and y from 2.5 to 2.9 … (2, 3) is the nearest grid point, on y = x + 1 only."
- **WHAT IS WRONG.** The part-(b) graph is drawn with a grid line every half (I viewed it at 170 dpi). (1.5, 2.5) is a printed grid intersection, it lies exactly on y = x + 1 (1.5 + 1 = 2.5) and not on y = −2x + 6 (−3 + 6 = 3). It is the same error the key rejects for (2, 3) — snapping to the nearest grid point — yet the stated range earns it the point. The spec comment says the range is "strictly between the grid lines"; that is true of the whole-number lines only (the check tests 1 < 1.5 and 1.9 < 2), not of this figure. Two teachers will score (1.5, 2.5) differently.
- **FIX.** Key: "Accept x from 1.6 to 1.8 and y from 2.6 to 2.8. (1.5, 2.5) and (2, 3) are grid points on y = x + 1 only; (2.7, 1.7) swaps the coordinates." (5/3 and 8/3 are inside; both rejected points are outside.) Change the range check to 8/5 ≤ 5/3 ≤ 9/5 and 13/5 ≤ 8/3 ≤ 14/5, and add `fails("-2*u + 6", "F(3,2)", "F(5,2)")`. The same rule should govern the practice page's generator: the tolerance must exclude every printed grid intersection.

#### 2. MAJOR — "Rational number coefficients" is taught and practiced below the state's level
- **WHERE.** Whole unit; sharpest in 11.04 (slides, set, both banks), the Practice Test Q4 and Review A3.
- **WHAT IT SAYS.** Every decimal factor in the unit is chosen so the products are whole (0.5(4x + 6), 0.4(5t + 10), 0.2(10t − 5), 0.6(5v + 10), 1.5(2t + 4), 2.5(2x − 4)); every fraction factor is positive and clears to whole numbers (½, ⅓, ¼, ⅔, ¾, ⅖); no equation has a decimal constant; nearly every solution is a whole number.
- **WHAT IS WRONG (searched the seven specs and `unit.py`).**
  - **Negative fraction coefficient or factor: zero items in the unit.** The benchmark says rational coefficients; the B1G-M's named misconception is sign errors while distributing.
  - **Negative decimal factor: three items only** — 11.04 set Q4 (−2.5(2k − 4) = k − 8), bank Q8 (−0.5(4k + 6) = k − 12), additional Q8 (−0.5(6k − 4) = 2k − 18). None on a slide or whiteboard, none in the Review, none on the Practice Test. The state's own item is −3.5(10x − 2) = −176.75 (x = 5.25): negative decimal factor, decimal constant, decimal answer.
  - **Decimal constant or decimal x-coefficient left after distributing: one worked line** (Notes III of 11.04, 1.5x on the right). No practice item.
  - **A solution that is not "nice": none.** The state's second item, 15(2x − 10) + 4x = −3(15x + 4), ends x = 138/79. Source of Truth Part 7 rule 12 says the accelerated class should meet a value that is merely tedious.
  - The decimal-distributed skill (21% statewide) is promised "a question every day from 11.01". 11.03 has it in neither a board nor the Independent Set (bank Q7–8 only).
- **FIX (each solved in sympy before writing).**
  - 11.04 Notes III, add a second line or replace board 3: **−2.4(5x − 3) = −40.8** → −12x + 7.2 = −40.8 → x = 4. This is the state item's exact shape.
  - 11.04 board 3 (now 0.4(5x − 10) = x + 3): **0.6(3x + 4) = 1.2x + 5.1** → 1.8x + 2.4 = 1.2x + 5.1 → 0.6x = 2.7 → x = 4.5.
  - 11.04 Independent Set, swap Q1 (whole-number multi-step, already drilled for three days) for **−¾(8x − 12) = 2x − 23** → −6x + 9 = 2x − 23 → x = 4.
  - 11.04 bank, add or swap: **⅔x + 5 = ⅙x − 1** → x = −12 (fraction coefficients on the variable itself, negative solution); **−1.5(4x − 3) = 2x − 13.5** → x = 2.25; **−⅔(6x − 9) = x − 15** → −4x + 6 = x − 15 → x = 21/5 = 4.2.
  - 11.03 Independent Set, make one of Q2/Q3 a decimal ending, e.g. **0.4(5x − 10) = 2x − 4** is already in 11.04; use **0.5(6n − 4) = 3n + 2** (−2 = 2, no solution).
  - One enrichment item in the 11.04 bank at the state's ugliness: **5(2x − 3) + 3x = −2(4x + 1)** → 13x − 15 = −8x − 2 → x = 13/21.
  - Review A3: add **(d) −0.4(5x − 10) = x + 2.5** → −2x + 4 = x + 2.5 → x = 0.5.

#### 3. MAJOR — The Practice Test (the test's blueprint) has no fraction-coefficient equation, and Q7 measures something AR.2.1 does not state
- **WHERE.** Practice Test Q1–Q7 (`unit.py` `_ar21`).
- **WHAT IT SAYS.** Q1 like terms + distribution; Q2 both sides; Q3 parentheses both sides; Q4 0.6(5v + 10) = 2v + 13; Q5 three endings; Q6 fill the box; Q7 storage companies (write 35 + 9m = 14m from a story).
- **WHAT IS WRONG.** 11.04's target is "fraction or decimal coefficients"; the Review practices a fraction distributed and a common denominator (A3 b, c); the test never asks either. Half of 11.04 is untested. Meanwhile Q7's difficulty is writing the equation from a context, which MA.8.AR.2.1 does not state (11.04's own `working_toward` assigns it to MA.912.AR.2.1); a FAST AR.2.1 item is a bare equation. Q4 is the gentlest possible form of the 21% skill (positive factor, whole products, whole answer).
- **FIX.** Q7 → a fraction distributed, with numbers no lesson uses: **⅔(6w + 9) = w − 3** → 4w + 6 = w − 3 → w = −3 (check: ⅔(−9) = −6 and −3 − 3 = −6). Q4 → **−1.5(4v − 6) = 2v − 15** → −6v + 9 = 2v − 15 → v = 3 (check: −1.5(6) = −9 and 6 − 15 = −9), with the key's named misses −6v − 9 (sign) and −6v − 6 (one term). Keep the two-plans story where it belongs, in 11.08 and Q14.

#### 4. MAJOR — The only multiselect on the test always has exactly one correct answer
- **WHERE.** Practice Test Q8; Review B (second item); 11.05 Independent Set Q3; Reference Sheet section 3, third bullet.
- **WHAT IT SAYS.** "Select ALL the solutions of the system y = 3x − 2 and y = x + 6." Key: C only. The Reference Sheet: "when you test several pairs, at most one can pass."
- **WHAT IS WRONG.** FAST's multiselect is hard because the count is unknown (Source of Truth Part 4, pattern 4: released keys of 3, 2 and 2). Here a student who notices different coefficients knows the count is one before testing anything, and the Reference Sheet teaches exactly that. The item is multiple choice wearing a multiselect's clothes, and it trains "select all = pick one". The unit already owns the right version: 11.05 bank Q12 (y = 2x + 2 and y = 2(x + 1), key A, C, D).
- **FIX.** Practice Test Q8 → "Select all the ordered pairs that are solutions of the system **y = 2x − 6 and y = 2(x − 3)**." Options (5, 4) ✓, (3, 1) ✗, (0, −6) ✓, (−1, −8) ✓, (2, −1) ✗; key A, C, D. Have the practice page draw the crossing form and the same-line form at random so the count cannot be predicted. Reword the Reference Sheet bullet: "If the two lines cross, exactly one pair can pass. If the two equations are the same line, every pair on that line passes — so test every option." Also lowercase "ALL" to FAST's "Select all the…".

#### 5. MAJOR — No horizontal line anywhere, and "the same number multiplying x" cannot describe one
- **WHERE.** All of 11.05–11.08, the Review, the Practice Test (searched every `lines=[…]` and every equation: no line with 0 multiplying x).
- **WHAT THE STATE EXPECTS.** The B1G-M's AR.4.2 item (reading notes): System B is two horizontal lines (no solution); System C is a slanted line and a horizontal line (one solution). Its AR.4.2 task is y = −½x and y = ⅓x, both through the origin ("no y-intercept, so no intersection" is the error). y = 3 is slope-intercept form, so it is inside AR.4.3's boundary as well.
- **WHAT IS WRONG.** The unit's rule for parallel lines needs a number multiplying x; y = 2 and y = 5 show none. A student meets this for the first time on the state test. Likewise no system has both lines through the origin.
- **FIX.** Add to 11.05 (a board or bank Q8–9) and to Review C: a graph of **y = 4 and y = −1** — no solution ("no x at all: 0 multiplies x in both, so each line stays level; parallel"); a graph of **y = 3 and y = x + 1** — one solution, (2, 3); and **y = 2x and y = −x** — one solution, (0, 0). One sentence in 11.05 Notes III: "y = 3 is a line too: every x gives 3."

#### 6. MAJOR — The blueprint paper never shows the same-line case in a system, and spends an AR.4.3 point on evaluating an expression
- **WHERE.** Practice Test Q10–Q13.
- **WHAT IT SAYS.** Q10 crossing; Q11 parallel; Q12 read a crossing; Q13(a) "What number is missing from the table for y = 2x − 5?"; Q13(b) the solution from the tables.
- **WHAT IS WRONG.** The B1G-M names exactly one misconception for AR.4.2 (the same-line case read as something other than infinitely many) and one for AR.4.3 beyond plotting (only the plotted points are solutions). The lessons teach both well; the blueprint paper tests neither (the outline says Q11 is "parallel or one line", so a given test form may never ask it). Q13(a) is substitution into one equation — not AR.4.3.
- **FIX.** Q11 becomes two parts, 1 point each: (a) the parallel graph as printed; (b) "y = ½x − 2 and y = 0.5x − 2 both graph as the line shown, with two points marked. Which is true? A. one solution B. two solutions C. no solution D. infinitely many solutions" (key D). Replace Q13(a) with an AR.4.3 part (wording in finding 10, which also keeps the total at 18).

#### 7. MAJOR — Three required IXL skills ask for what the unit deliberately withholds (verify in IXL; I could not open it)
- **WHERE.** 11.05 IXL slide (slide 35) and 11.07 IXL slide.
- **WHAT IT SAYS.** 11.05: "Solve a system of equations in slope-intercept form — 9Z8" and "Find the number of solutions to a system of equations by graphing — AGZ". 11.07: "Write a system of equations given a graph — TS7". All required to SmartScore 67.
- **WHAT IS WRONG.** (a) 9Z8's printed title puts "slope-intercept" on a student slide — the one place the unit breaks its own rule (text search of every student PDF: "slope" and "intercept" occur once each, here). (b) TS7 by its title asks the student to write y = mx + b from a graph, which is MA.8.AR.3.3 (Unit 10); 11.07 does this once, as multiple choice (board 6). (c) AGZ is assigned on 11.05, two days before any student has graphed a line (11.07). (d) If 9Z8 is solved algebraically it is the "bridge taught, not tested" being required at 67.
- **FIX.** Open each skill before Monday. Move AGZ to 11.07. Move TS7 to Unit 10, or make it optional. If 9Z8 expects algebra, drop it; if it stays, the slide can list it by code with a neutral label.

#### 8. MAJOR — Teaching this before slope: the decision holds, but two Florida words are missing now and a hand-off must be written down
- **VERDICT.** The wording is sound mathematics and prepares the concept: "3 multiplies x in both, so each line climbs 3 for every 1 across and they stay 3 apart" (11.07 board 9) is slope in everything but name. A spring FAST item on AR.4.3 that says "slope" will be read by students who have had Unit 10 since January. I would not put "slope" on a December student page. PM2 falls on Tue 8 Dec, mid-unit and before Unit 10, so its AR.3 and AR.4.3 results are not evidence about this unit.
- **WHAT MUST BE ADDED NOW.**
  1. **"Intersect" never appears in the unit** (0 occurrences; "cross/crossing" 387). Florida's items and guide say the lines intersect and name the point of intersection. Add to 11.05 vocabulary: "intersect — to cross; the point of intersection is where two lines cross", and use "intersect" in the Practice Test and Review stems ("The lines intersect at…").
  2. **Say "coefficient of x"** beside "the number multiplying x" in 11.05–11.08. "Coefficient" is a Florida glossary word the class already owns from 11.01 (it is in the Reference Sheet vocabulary) and it is the word Unit 10 will rename: "the coefficient of x is the slope". It also survives y = x + 3 (coefficient 1), y = −x + 4 (−1) and y = 5 + 2x, where "the number in front" fails.
  3. "The same steepness" is true only with direction: y = 2x and y = −2x are equally steep. The Reference Sheet covers it; say "the same steepness in the same direction" in 11.05 and 11.07.
- **WHAT TO LEAVE TO UNIT 10 AND THE SPRING REVIEW — but write it into the plan now.** Unit 10's slope lesson reopens a Unit 11 pair (y = 3x − 2 and y = 3x + 1) and states Clarification 3 in the state's words: the same slope and different y-intercepts — parallel, no solution; the same slope and the same y-intercept — one line, infinitely many. PM3-R2 (20 Apr) carries at least three AR.4.2/4.3 items worded with "slope" and "y-intercept". Nothing in the Scope and Sequence records this yet.

#### 9. MAJOR — Item shapes: the Practice Test is benchmark-shaped, not FAST-shaped
Searched the specs: "An equation is shown." 0; "What is the value of" 0; a response prefixed "x =" 0; matching grid 0; dropdown sentence 0. "…are shown." is used only on AR.4.2 graph stems.

| Q | Now | Verdict | Reword to |
|---|---|---|---|
| 1–4 | "Solve: 2(3n − 4) + 5n = 25" | Not FAST | "An equation is shown." / the equation on its own line / "What value of n makes the equation true?" / **n = ▢** |
| 5 | three equations, name the ending, "if it has one, find it" | Right content, wrong shape | A **matching grid**: rows the three equations; columns No Solution · One Solution · Infinitely Many Solutions; one box per row. Keep "find it" as a separate line for (b). |
| 6 | "What number in the box makes … have no solution?" | Close to FAST's inline blank | "Complete the equation so that it has no solution." 2(4x + 3) − x = ▢x + 1 |
| 7 | story | Not an AR.2.1 shape | Replace (finding 3) |
| 8 | multiselect, one key | Shape right, key count wrong | Finding 4 |
| 9 | yes/no with reason, four options | FAST-shaped | Keep |
| 10–11 | "The graphs of … are shown. How many solutions does the system have?" open | Stem right; response open | Add the three options, or use the dropdown below |
| 12 | "What is its solution? Give its x and its y." | Nearly | "A system of equations is graphed. What is the solution of the system?" **x = ▢ y = ▢** (the outline already says so; the paper prints no boxes) |
| 13 | two tables | Not a FAST stimulus for AR.4.3, but sound | Keep (b) |
| 14(a) | story graph | FAST-shaped once shortened | Keep; two sentences |
| 14(b) | estimate "to the nearest tenth", open | Not FAST | Multiple choice: "Which ordered pair is closest to the solution?" (1.7, 2.7) ✓ · (2.7, 1.7) · (2, 3) · (1.5, 2.5) — the unit's own 11.08 board 4 shape. Also, 14(b) has nothing to do with 14's stem; make it question 15 or give it its own stem. |

**Missing from the test altogether:** a matching grid (the natural shape for one/none/infinitely many, equations or graphs); a dropdown sentence ("Complete the sentence about the system. The lines [intersect once / are parallel / are the same line], so the system has [one solution / no solution / infinitely many solutions]."); a choose-among-four-graphs item ("Which graph shows a system with no solution?" — Part 4 pattern 7: every graph is a stimulus). Each should appear at least once on a whiteboard in 11.03 and 11.05 before it appears on the test.

#### 10. MINOR — Point weighting (9 / 2 / 2 / 5)
Defensible by days taught (4 : 1 : 2) and by the district's Q2 essential benchmark; not by FAST, where each of the four benchmarks is one blueprint row. The weak point is practical: two one-point items cannot tell you anything about AR.4.1 or AR.4.2 on the Score Tracker. Recommended, keeping 18 points: delete Q1 (its skill is inside Q3 and Q5c); give Q11 its second part (finding 6); replace Q13(a) with an AR.4.3 part rather than dropping it — "The tables for y = 2x − 5 and y = 2x + 1 never show the same y for the same x. How many solutions does that system have?" (no solution). Result: **AR.2.1 8 · AR.4.1 2 · AR.4.2 3 · AR.4.3 5**.

#### 11. MINOR — Systems are easier than the state's examples
The B1G-M's AR.4.3 items: y = −¾x + 5 and y = −4x − 2 (about (−2.15, 6.62)); y = −0.5x + 2 and y = 4.5x − 5 ((1.4, 1.3)); y = 2x + 6 and y = 2x − 4.2 (parallel, decimal constant); AR.4.1 task with y = ⅗x − 9⁄5. The unit's systems use coefficients ±1, ±2, ±3, ½ (⅔ and 3⁄2 once each), whole constants, and every estimate sits in the first quadrant on thirds. Add to the 11.08 bank: "y = −0.5x + 2 and y = 4.5x − 5 are graphed. Which is closest to the solution? (1.4, 1.3) ✓ · (1.3, 1.4) · (1, 1.5) · (0, 2)"; to 11.07 "Select all the systems that have no solution" an option "y = 2x + 6 and y = 2x − 4.2"; to the 11.05 bank one check with a fractional constant, "(3, 0); y = ⅗x − 9⁄5 and y = −⅘x + 12⁄5" (yes: 9⁄5 − 9⁄5 = 0 and −12⁄5 + 12⁄5 = 0 — the state's own task).

#### 12. MINOR — Items that belong to MA.8.AR.3.3, not to these four benchmarks
11.07 board 6, bank Q11 and additional Q11 ("which system is graphed", from four points); 11.08 board 6, set Q4, bank Q5/Q10, additional Q5/Q10 ("write a system for the cost y of x …"). All are answerable without slope and are reasonable setup for a real-world AR.4.3 item, so keep them — but they are Unit 10's benchmark taught early, they should not be counted as AR.4.3 evidence, and none should reach the test.

#### 13. MINOR — Florida's wording
- **Answers written "None" / "Infinitely many"** (seven keyed answers in 11.05 and 11.07, the 11.04 and 11.05 warm-ups) where the benchmark's phrases are "no solution" and "infinitely many solutions". Use the full phrases every time; students copy the answer slide.
- **Properties are not named.** The B1G-M asks students to verbalize the property used (Appendix D); "take 3x from both sides" is never called the subtraction property of equality (0 occurrences). One line in 11.02 Notes I is enough.
- **Variables.** Equation lessons rotate letters well and avoid o, i, l. Every system and every story uses x and y only; the guide models contextual letters (h = 0.21m + 4.9). One 11.08 story in c and m would do.
- No mnemonic or trick found (searched PEMDAS, FOIL and similar: 0). "Distribute, collect, move, divide, check" is an order of work, not a trick, but "move" is the word the guide's sign-error misconception grows from; "take the same term from both sides" (used elsewhere in the unit) is better.

#### 14. MINOR — The decimal skill's daily promise is not met on 11.03
Standing decision 5 promises a decimal-distributed question every day from 11.01 "(a board, or a question of the Independent Set)". 11.03 has none on a board or in the set (bank Q7–8 only). Fix in finding 2.

#### 15. MINOR — Estimate tolerances are stated three ways
Practice Test: a range (finding 1). Review D5 and 11.08 bank: "within about 0.2". 11.08 set Q3: "within about 0.2 of each, such as (1.5, 0.5)" — (1.5, 0.5) is on y = −x + 2 only. One rule everywhere: within 0.1 of the exact value rounded to the tenth, and never a printed grid intersection.

#### 16. MINOR — Q14's stem
Three sentences plus a second, unrelated system. FAST context stems are at most two sentences (Part 4 pattern 2). "Mia has $10 and saves $6 each week. Leo has $60 and spends $4 each week." then the graph, then the question.

---

### Checked and found sound
- **Boundaries.** Every equation and system string in `l01–l08.py` and `unit.py`: one variable, linear, no inequality, no quadratic; every system is two equations, both solved for y; no standard form; no vertical line (the book's x = 3.5 item is correctly dropped); no item demands substitution or elimination (the mx + b = nx + c bridge is shown and never asked). Same-line pairs written y = b + mx or y = a(x + c) are within the state's own practice (its AR.4.2 item is 3y = 6x − 9).
- **Three endings (AR.2.1 Clar. 1).** Taught as x = a, a = a, a = b with Florida's three phrases; x = 0 as one solution is taught, boarded, set, reviewed and tested (Q5b) — the guide's named misconception.
- **Same-line case and unplotted points (AR.4.2, AR.4.3 misconceptions).** 11.05 Notes I ((100, 102), off the grid), Notes III ("the ones nobody plotted too"), board 6 (distractor "two — the marked points"), set Q6, both banks' select-all on a same-line system: taught properly. The gap is only on the test (finding 6).
- **"A solution satisfies both" (AR.4.1).** Every wrong pair in every AR.4.1 item satisfies exactly one equation or is a swapped pair; keys name which.
- **Approximation (AR.4.3 Clar. 1).** Taught in 11.08 (Notes III, boards 3–4, set, banks) with "about" and a check in both equations.
- **Parallel lines (Clar. 3).** Recognized from equations and from graphs, including coefficient 1 and −1 pairs (11.05 board 5; 11.07 set Q4) and the ½ versus 0.5 trap.
- **Practice Test keys 1–13 and 14(a).** Read against their stems; Q4, Q6, Q8, Q9 and Q12 distractor claims spot-checked by hand. All proposed replacement equations above were solved in sympy.
- **Pictures viewed as images:** Practice Test pages 2–6 (every graph and table), Q14(b) at 170 dpi, and nine 11.08 slides (Notes III, boards 2, 3, 4, 6). I did not view every slide of 11.05 and 11.07 or the Review's figures as images; my reading of those rests on the specs.
- **Not checked:** the practice page and its generators (`a7/practice/`, out of bounds), and IXL skill content (finding 7 is from the skill titles).

