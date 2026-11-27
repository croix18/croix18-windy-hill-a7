# Question Bank — Unit 10: Linear Relationships

The question-bank commentary for every lesson in the unit: how each bank varies, what the
audit against Math Nation found, what changed from the book, and the answers.

**This is not a handout.** It is the reference behind the lesson plans, read once when the unit is planned.
The printed keys in each lesson's `Keys` folder are generated from the same specs.

## 10.01  Linear and Proportional Relationships

*MA.8.AR.3.1*

**Variation.**  Whiteboard questions 1 and 2 use one table, and only the question changes. Question 3 takes away the pair for x = 0, question 4 is an equation and question 5 is four graphs. The pattern breaks at question 6, where y = 5(x + 2) has no number added at the end and still is not proportional. Question 7 is a story with an extra number, question 8 finds the value of y at x = 0 from two pairs, and question 9 is written. The Independent Set moves from a table with x = 0 to one without, then a graph, equations, a description and two tables.

**Read this once, when you plan the unit.**

- Every relationship in this lesson is given as linear, so the only question is whether it is also proportional. Two reasons are accepted everywhere: y is 0 when x is 0, and y ÷ x is the same for every pair.
- Notes III is the heart of the lesson: a table with no pair for x = 0 is still decided by going back to x = 0 at the rate of change.

**What the audit against Math Nation found.**

- Every table is checked by sympy at build time to have a constant rate of change, and every value of y at x = 0 is computed from the first pair and the rate. Every proportional table is checked pair by pair for one ratio, and every one that is not proportional is checked to have two different ratios.
- Every equation called proportional is checked to be linear with y equal to 0 at x = 0, and every one called not proportional to be linear with y not 0 at x = 0.

**What changed from the book.**

- Nothing was taken from Math Nation; the lesson follows the unit's Lesson Outlines, section 10.01.

**Question Bank answers.**  
1. Yes, y is 0 when x is 0.  2. No, y is 6 when x is 0.  3. 6; no  4. 0; yes  5. No, its line passes through (0, 2).  6. C, D, E C, D, E  7. c = 2h + 5; no  8. c = 1.20w; yes  9. 5; no  10. C C  11. D D  12. No, y is 1 when x is 0.

**Question Bank – Additional answers.**  
1. Yes, y is 0 when x is 0.  2. No, y is 3 when x is 0.  3. 3; no  4. 0; yes  5. Yes, its line passes through the origin.  6. A, B, D A, B, D  7. c = 3g + 4; no  8. c = 0.50w; yes  9. 3; no  10. A A  11. C C  12. No, y is 4 when x is 0.

---

## 10.02  Slope from Graphs, Tables and Two Points

*MA.8.AR.3.2*

**Variation.**  Boards 1–2 find a slope from two points, and only the second y-value changes, so the slope turns negative. Board 3 votes on a table whose x-values go up by 2, board 4 reads a falling line off a graph, and board 5 votes on a graph. The pattern breaks at 6, where the slope triangle's rise is found past the edge of the grid. Board 7 is a ramp with its width as the extra number, 8 runs backwards, and 9 judges Jo's subtraction, written. The set: two points with negative coordinates, a rising and a falling graph, a table with unequal steps, a missing run, and a horizontal line with slope 0.

**Read this once, when you plan the unit.**

- Two book lessons taught as one day. Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §10.02+03, standing decisions 2, 4, 5, 6, 7 and 8), with Math Nation read for scope only.
- Today names slope: the rate of change of a line, the change in y divided by the change in x between any two points on it, rise over run. The formula m = (y₂ − y₁)/(x₂ − x₁) is shown once, in Notes III, and no question needs its notation; the words are 'Subtract in the same order.' Every table whose slope is asked has x-values that do not go up by 1, and Example 2, its Your Turn and Independent Set question 4 have unequal steps.
- Whiteboard question 6 is the similar-triangles connection: the larger triangle runs past the edge of the grid, so its rise has to be found from the slope, not counted.

**What the audit against Math Nation found.**

- Every slope re-derived by sympy at build time as the change in y divided by the change in x, from the printed points; every table's second slope checked against its first; every marked point checked on the line drawn by u10/figs10.py.
- Every wrong option is one named error: run over rise, the change in y alone, subtraction in different orders, or a falling line read as rising.

**What changed from the book.**

- Two book lessons (slope from a graph and a table; slope from two points) → one day: Notes I–III, one Example from a graph and one from a table with unequal steps.
- Practice and Homework → the Independent Set: six questions, one feature changed at a time.

**Question Bank answers.**  
1. 4  2. −3  3. 1/2  4. 0  5. 3/4  6. −3/2  7. −4/3  8. 4  9. 12  10. −4  11. 3/4  12. B B  13. D D

**Question Bank – Additional answers.**  
1. 4  2. −3  3. 1/2  4. 0  5. 3/4  6. −3/2  7. −4/3  8. 4  9. 8  10. −7  11. 1/2  12. A A  13. B B

---

## 10.04  Slope in Context

*MA.8.AR.3.2*

**Variation.**  Boards 1 and 2 use one table, and only the question changes, from the slope to its meaning; 3 votes on a meaning; 4 is a description with two moments; 5 votes on a slope from a table with unequal steps; 6 is a falling graph; 7 carries the truck's boxes as the extra number; 8 finds a missing cost; 9 is written. The set breaks the pattern at question 6, a table that is not proportional.

**Read this once, when you plan the unit.**

- Wednesday 20 January, a 43-minute day. The kit's timing table must total 53, so the table is the full lesson; the cut is under Materials. Built from the benchmarks and the B1G-M first (the unit's Lesson Outlines, §10.04, and its standing decisions 2, 5, 6, 7, 13 and 15).
- Every slope is the change in y divided by the change in x, with its unit, the y-unit per x-unit, and every meaning is a sentence with both units. Notes I says once that IXL calls a linear relationship a linear function; the pages keep 'linear relationship'. Read the scales first: the graphs count by 20, 150, 3 and 60.
- Board 9 and the set's last question turn on Unit 7's habit of dividing one pair: it gives the rate only when the line passes through the origin.

**What the audit against Math Nation found.**

- Every slope re-derived by sympy at build time from the printed points, each consecutive pair of every table; every graph drawn from its equation by u10/figs10.py, which refuses a marked point that is not on its line; every wrong option checked from its error.

**What changed from the book.**

- Built from the benchmarks and the unit plan; no Math Nation item is reproduced.

**Question Bank answers.**  
1. 28 dollars per month  2. −45 gallons per hour  3. 30 kilometers per hour  4. −10 meters per second  5. 65 miles per hour  6. −500 feet per minute  7. The bag loses 0.5 pounds of dog food every day.  8. A A  9. D D  10. \$380  11. No. The rate of change is 6 dollars per hour. The rental costs \$10 at 0 hours, so dividing one pair does not give the rate.  12. After 6 hours

**Question Bank – Additional answers.**  
1. 55 dollars per hour  2. −16 miles per hour  3. 22.5 centimeters per week  4. −50 grams per minute  5. 54 miles per hour  6. −14 copies per day  7. The feeder loses 0.75 ounces of seed every hour.  8. C C  9. B B  10. \$585  11. No. The rate of change is 6 dollars per shirt. The order costs \$9 for 0 shirts, so dividing one pair does not give the rate.  12. After 7 hours

---

## 10.05  Slope-Intercept Form and Graphing a Line

*MA.8.AR.3.4*

**Variation.**  Whiteboard questions 1 and 2 name the slope and the y-intercept, the second with b written first; 3 votes on a statement about y = 6 + (1/2)x; 4 moves twice with a negative slope from a y-intercept; 5 votes on four graphs of y = 2x − 3. The pattern breaks at 6: the class writes the equation from m and b instead of reading it. 7 carries Kai's room number as the extra number; 8 runs backwards; 9 is written. The set: question 1 drawn in class, then a negative whole-number slope, b first with a negative fraction, b = 0, and the break — no grid, a table and the two numbers — then an equation to write.

**Read this once, when you plan the unit.**

- Thursday 21 January. Built from the benchmark and the B1G-M first (the Unit 10 Lesson Outlines, §10.05, standing decisions 2, 9, 11 and 12); Math Nation was read for scope only.
- Today names the y-intercept and the form y = mx + b, and graphs a line by starting at the y-intercept and moving with the slope; Unit 11's table of values stays the method for anything else (10.06). A negative slope goes down as you move right: −2/3 is down 2, right 3. Every line gets a third point as the check.
- The Examples' question slides show an empty grid: draw the line on the projected slide while the class watches. Right after Example 1, hand out the Independent Set: Your Turn 1 is its question 1, and every student draws it on the handout's grid while you circulate. The boards read; nobody draws a line on a whiteboard. The key draws each line on the student's own grid.
- Changed from the outline: none of its numbers.

**What the audit against Math Nation found.**

- Every slope and y-intercept re-derived by sympy at build time (the derivative and the value at x = 0); every point checked on its line; every choice's key and each wrong option checked from its error; every graph drawn from its equation by u10/figs10.py, which refuses a labeled point that is not on its line.

**What changed from the book.**

- Built from the benchmark, its B1G-M notes and the unit plan; no Math Nation item is reproduced.

**Question Bank answers.**  
1. The slope is 3/2 and the y-intercept is 4.  2. The slope is −5 and the y-intercept is 1.  3. $y = \frac{4}{3}x - 2$  4. y = −2x + 7  5. The line through (0, 1), (2, 2) and (4, 3)  6. The line through (0, 4), (3, −1) and (6, −6)  7. The line through (0, −4), (2, −1) and (4, 2)  8. (3, 3) and (6, 7)  9. 7  10. D D  11. C C  12. B, D, E B, D, E

**Question Bank – Additional answers.**  
1. The slope is −1/3 and the y-intercept is 6.  2. The slope is −2 and the y-intercept is 8.  3. $y = \frac{1}{2}x - 6$  4. y = −5x + 3  5. The line through (0, −3), (2, −2) and (4, −1)  6. The line through (0, 5), (3, 0) and (6, −5)  7. The line through (0, −1), (2, 2) and (4, 5)  8. (3, 2) and (6, 1)  9. 5  10. B B  11. D D  12. A, B, E A, B, E

---

## 10.06  Graphing from Tables and Contexts

*MA.8.AR.3.4*

**Variation.**  Whiteboard questions 1 and 2 work from an equation and a table; 3 votes on four graphs of one story; 4 writes a description's points; 5 votes on a table's y-intercept when the table has no x = 0. The pattern breaks at 6, an equation in another form. 7 carries the boat's seats as the extra number; 8 finds a missing number on a line; 9 is written. The set: question 1 drawn in class, then a table, a rising story, a falling story, an equation in another form, and a graph read for its start and rate.

**Read this once, when you plan the unit.**

- Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §10.06). Math Nation was read for scope only, and nothing is taken from it.
- Every line is graphed one of two ways: from a description, the rate is the slope, and the start is the y-intercept; from a table or another form, plot the pairs and draw the line through them. A real-world graph starts at x = 0 and stops where the story ends.
- Right after Example 1, hand out the Independent Set: Your Turn 1 is its question 1 (y = 2x − 5), and every student completes the table and draws the line on the handout's grid while you circulate. The boards read a table, a description or a graph; nobody draws a graph on a whiteboard. The key draws each line on the student's own grid.
- Changed from the outline: the boat on whiteboard question 7 has 4 seats, not 6, because 6 is also the answer's number of hours; board 4's kitten gains 0.5 pounds, plural with a decimal.

**What the audit against Math Nation found.**

- Every table value, slope and y-intercept is re-derived by sympy at build time from its equation or its two points; every graph is drawn from its equation by u10/figs10.py, which refuses a point marked on a line it is not on.

**What changed from the book.**

- Math Nation 10.6 was read for scope only; the lesson is built from the benchmark and the unit's plan.

**Question Bank answers.**  
1. −7, −2, 3, 13  2. 6, 4, 2, 0  3. Slope 3; y-intercept 1.  4. The line through (−4, −4), (0, −2) and (4, 0)  5. The y-intercept is −3.  6. The line from (0, 150) through (2, 250) to (6, 450)  7. The line from (0, 16) to (2, 0)  8. 9, 6, 0; the line through (0, 9) and (3, 0)  9. 4 centimeters at the start; it grows 3 centimeters per week.  10. C C  11. A A  12. 17

**Question Bank – Additional answers.**  
1. −11, −5, −2, 7  2. 5, 3, 2, 0  3. Slope −2/3; y-intercept 8.  4. The line through (−4, 1), (0, 2) and (4, 3)  5. The y-intercept is −3.  6. The line from (0, 50) through (2, 150) to (6, 350)  7. The line from (0, 48) to (4, 0)  8. 10, 6, 0; the line through (0, 10) and (5, 0)  9. 10 centimeters at the start; it grows 5 centimeters per hour.  10. B B  11. A A  12. 11

---

## 10.07  Interpreting Slope and y-Intercept

*MA.8.AR.3.5*

**Variation.**  Boards 1–2 read one equation's two numbers (only the number asked about changes); 3 votes on what a y-intercept means; 4 finds a negative slope from a table with unequal steps and 5 votes on its y-intercept; 6 uses the temperature formula; 7 is a description with an extra number (the hours the gym is open); 8 runs backwards. The pattern breaks at 9 — a negative y-intercept, written. The set: an equation, a graph with a scale, a table that shows x = 0, a table with no pair for x = 0, a description with two moments, then the temperature formula.

**Read this once, when you plan the unit.**

- Two book lessons (10.7 and 10.8) taught as one day. Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §10.07+08, standing decisions 2, 5, 9, 13 and 14), with Math Nation read for scope only.
- No new word today: the rate is the slope, and the start is the y-intercept. Every slope is said with its unit and every y-intercept as the amount when x is 0. When a table has no pair for x = 0, substitute a point and solve for b. The temperature formula is printed wherever it is used; the class is asked about its 32 and its values.

**What the audit against Math Nation found.**

- Every slope re-derived by sympy at build time from two printed points, every table and graph point checked on its line, and every y-intercept found by solving y = mx + b for b; decimals read as exact numbers.
- Every wrong option is one named error: the slope and the y-intercept exchanged, a number read as a value of x, the y-intercept read as a total, or the first pair read as the start.

**What changed from the book.**

- 10.7 and 10.8 (interpreting slope and y-intercept; temperature) → one day: Notes I–III, one Example from a graph and one from a description.
- Practice and Homework → the Independent Set: six questions, one representation at a time.

**Question Bank answers.**  
1. Each kit adds \$5 to the cost.  2. The water was 45 centimeters deep when the vase was filled.  3. B B  4. Slope 3, y-intercept 8: the shoot was 8 centimeters tall when the measuring began.  5. −3 pounds per hour: the cooler loses 3 pounds of ice every hour.  6. Slope 40: the bus moves 40 miles farther from the station every hour. y-intercept 20: it was 20 miles from the station at the start.  7. A A  8. 40: the rental costs \$40 before the first hour.  9. \$50  10. 77 °F  11. 36 degrees Fahrenheit  12. 14  13. With 0 boxes sold the profit is −\$45: the sale spent \$45 before it sold a box.

**Question Bank – Additional answers.**  
1. Each ride adds \$3 to the cost.  2. The tank held 60 gallons when the trip began.  3. C C  4. Slope 5, y-intercept 13: the vine was 13 centimeters long when the measuring began.  5. −5 degrees Fahrenheit per minute: the soup cools 5 degrees Fahrenheit every minute.  6. Slope 250: the machine fills 250 bottles every minute. y-intercept 500: it had filled 500 bottles when the timing began.  7. B B  8. 30: the rental costs \$30 before the first hour.  9. \$40  10. 86 °F  11. 27 degrees Fahrenheit  12. 11  13. With 0 cars washed the profit is −\$40: the car wash spent \$40 before it washed a car.

---

## 10.09  Writing Equations of Lines

*MA.8.AR.3.3*

**Variation.**  Whiteboard questions 1 and 2 change one thing: the point leaves the y-axis, so b has to be found. Question 3 reads a graph and question 4 a table through x = 0 with a negative slope; question 5 is a table with no pair for x = 0, where the first y-value is the trap. Question 6 gives two points, question 7 two axis crossings with the grid's width as an extra number, question 8 runs backwards to the slope, and question 9 is written. The pattern breaks at question 7, where the line's two points are its crossings and neither is marked as a point. In the Independent Set the pattern breaks at question 3, whose table shows x = 0 between negative and positive x-values.

**Read this once, when you plan the unit.**

- Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, section 10.09). Three ways in, one method: find m from two points, then read b at x = 0 or substitute a point and solve for b, then check with another point.
- Whiteboard questions 3 and 5 are the diagnostics: each wrong option is one named error — the slope and the y-intercept exchanged, the slope turned over, or a y-value that is not at x = 0 taken as b.

**What the audit against Math Nation found.**

- Every equation is checked by sympy at build time to pass through every point and every table value it was written from, every slope is recomputed from two points as an exact fraction, and every wrong option is checked to miss at least one of the points.
- Math Nation was read for scope and item shapes only; nothing in this lesson is taken from it.

**What changed from the book.**

- The lesson is new for this unit and is built from the unit's Lesson Outlines, section 10.09.

**Question Bank answers.**  
1. y = (3/4)x − 2  2. y = −(1/2)x − 1  3. y = −3x + 7  4. y = 4x − 3  5. y = −(2/3)x + 3  6. y = 5x + 11  7. y = −(3/2)x  8. y = 2x + 5  9. −3  10. D D  11. B B  12. C, E C, E

**Question Bank – Additional answers.**  
1. y = (3/4)x + 1  2. y = −(1/2)x − 2  3. y = −3x + 1  4. y = −(5/2)x + 9  5. y = (3/4)x − 4  6. y = 4x + 6  7. y = −(1/2)x  8. y = 2x − 5  9. −3  10. D D  11. A A  12. A, E A, E

---

## 10.10  Writing Equations for Contexts

*MA.8.AR.3.3*

**Variation.**  Whiteboard questions 1 and 2 give a rate and a start, and only one thing changes between them: the amount goes down. Question 3 votes on which number is which, and question 4 gives two moments with no start. The pattern breaks at question 5: the table starts at 1 hour, so its first cost is not the start. Question 6 reads a line of fit, question 7 carries the aquarium's size as an extra number, question 8 runs backwards to the start, and question 9 is written.

**Read this once, when you plan the unit.**

- Wednesday 27 January is a 43-minute day, the day before the unit test. The timing table is the full 53-minute lesson, and the cut is under Materials.
- The lesson has two Notes slides and no vocabulary slide: every word it uses was named earlier in the unit. Notes I names the variables and reads the rate as the slope and the start as the y-intercept; Notes II shows an amount that goes down, written both ways.
- When a story gives two moments and no start, students find the slope, then substitute a point and solve for b, as Example 1 and whiteboard question 4 do. Example 2 and its Your Turn read the scales first and find the slope from the marked points.
- Whiteboard question 6 is the unit's one look ahead to Unit 13. It reads the slope of a line drawn through a class's scores and says 'about', because the line is drawn through the middle of the points.

**What the audit against Math Nation found.**

- Every equation is checked at build time against its story: the rate and the start, both moments of a two-moment story, and every pair of every printed table; every wrong option is checked to differ from the story's equation.
- The graphs are drawn from their equations by the unit's figure module, which refuses a marked point that is not on its line.

**What changed from the book.**

- The warm-up's third answer is written as a whole sentence: 'No, a ride of 0 miles costs $5.'
- Whiteboard question 8's answer is written 4.50, because money has two decimals.

**Question Bank answers.**  
1. c = 4n + 10  2. a = 35 − 0.25n  (a = −0.25n + 35 is the same answer)  3. c = 80h + 45  4. g = −0.05d + 23  5. c = 10h + 35  6. a = 20w + 40  7. C C  8. D D  9. 5.50  10. (a) The pool gains 80 gallons every hour.  (b) The pool held 300 gallons when the hose was turned on.  11. Sam exchanged the rate and the start. The equation is c = 20n + 45.  12. B, C B, C

**Question Bank – Additional answers.**  
1. c = 3n + 20  2. a = 10 − 0.05n  (a = −0.05n + 10 is the same answer)  3. c = 10f + 30  4. f = −0.25t + 12  5. c = 20h + 15  6. a = 35w + 50  7. B B  8. C C  9. 3.25  10. (a) The sunflower grows 2 centimeters every day.  (b) The sunflower was 30 centimeters tall when it was first measured.  11. Leo exchanged the rate and the start. The equation is c = 3h + 15.  12. C, E C, E

---
