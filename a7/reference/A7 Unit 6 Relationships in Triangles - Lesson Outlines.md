# A7 Unit 6 — Relationships in Triangles, and Thread B — Lesson Outlines

*Written 24 October 2026 from the benchmarks first (`Florida BEST Grade 8 - Source of Truth.md` §GR.1.1–1.5 and
GR.2.4, the B1G-M reading notes, the FAST item shapes), then read against Math Nation 6.1–6.8 and 16.1–16.2 (the unit
audit). Six teaching days, the one-period test, then Thread B's two days. Every number below was re-derived by sympy
before it was written down; the specs re-derive them again at build time. HOUSE STYLE §16 and ruling 43: the warm-up,
the notes and the worked examples are what the class has been shown, and every practice number after them is new.*

## The unit's standing decisions (each reversible)

1. **Radicands are whole numbers up to 225** (GR.1.1 and GR.1.2, Clarification 3; the Source of Truth's boundary; Part 7
   rule 12: "a radicand over 225 does [exceed a boundary]. Retune it."). Read strictly: every square root a student
   takes has a whole radicand ≤ 225 — so a hypotenuse found from its legs is at most 15 (whole answers: 5, 10, 13, 15),
   and the bigger triples (8-15-17, 7-24-25, 20-21-29, 9-40-41) appear as the converse (no root is taken) or as a
   missing *leg* (√(17² − 8²) = √225). Legs are whole numbers (a decimal leg makes a decimal radicand).
2. **An irrational answer is √n with n square-free, and a decimal to the nearest tenth when the words ask for a
   measurement.** Simplifying √50 to 5√2 is Algebra 1 (MA.912.NSO.1.4), not grade 8, so no radicand here has a
   square factor: √n is already simplest form and the brief's "simplified radical" costs nothing.
3. **No 3-D distances** (a box's space diagonal) and **no distance formula** (GR.1.2 Clar. 2): a slanted distance is
   always the right triangle drawn on the grid, legs read from the coordinates.
4. **The converse tests the longest side**, and at least one board lists the longest side first. The Triangle
   Inequality is taught as "the two shorter sides add to MORE than the longest"; the equal case lies flat and is a
   named error on every board that can carry it.
5. **Similar triangles are identified by matching angles or by all three side ratios**; a missing side is found with
   the scale factor k the class met in Unit 5 (copy ÷ original), and a proportion is the same thing written as a
   fraction. Thread B (Triangle Sum) comes after the test, so 6.07 never needs "the third angle is 180 minus".
6. **Colour** is the course's: base blue, exponent orange, read off the layout (a² + b² = c² colours itself).

## The test (Tue 17 Nov, one period) — the practice paper is its blueprint

Sections by benchmark, weighted to the days (1 : 2 : 2 : 1): 14 questions, 18 points, every answer a number, a
letter or a set of letters. **GR.1.3** (3 points) — 1. which set can form a triangle (the equal case, the first two
listed and the longest-plus-another as choices); 2. *select all* the sets that make a right triangle (FAST's
multiselect, which never says how many: one set with the longest side listed first, a near miss, a set that only
passes the inequality); 3. which inequality shows the third side, ▢ < x < ▢ (the book's own test shape; ≤ and
"between the two given sides" as choices). **GR.1.1** (6 points) — 4. (a) a hypotenuse, whole, (b) a leg, whole;
5. a hypotenuse to the nearest tenth; 6. which equation finds x; 7. a real situation, (a) a length and (b) how much
shorter the straight path is. **GR.1.2** (6 points) — 8. a slanted distance between two plotted points, whole (no
triangle drawn: the student draws it); 9. a slanted distance to the nearest tenth; 10. a triangle on the grid, (a)
its side that crosses an axis, (b) its perimeter to the nearest tenth; 11. a map, (a) along the streets, (b) the
straight line. **GR.2.4** (3 points) — 12. a missing side of a turned similar pair; 13. a shadow or a mirror;
14. which triangle is similar to a given one. Thread B is not on this test (ruling 48's move; Units 15–16
consolidate it).

---

## 6.01–02 · Fri 6 Nov · Triangle Inequality Theorem; Converse of the Pythagorean Theorem · MA.8.GR.1.3

IXL: Triangle inequality — 2N5; Converse of the Pythagorean theorem: is it a right triangle? — EQZ (due Mon 9 Nov).

**Target.** I can decide whether three lengths can make a triangle, and whether they make a right triangle.

**Warm-up.** (yesterday — the test; the band reaches to 5.10–11) a car's range from miles per gallon and gallons ·
(last week, 5.02–03) a copy's area at k = 3 · (last unit, 4.05) √169 · (prior grade — the prerequisite) 5² + 12².

**Notes.** I — *Two sides together must be longer than the third*: strips 3, 4, 9 (7 < 9, cannot meet); 4, 5, 9
(4 + 5 = 9, they lie flat — no triangle); 5, 6, 9 (11 > 9, a triangle). Add the two shorter, compare with the longest;
the FAST sheet's three lines a + b > c, a + c > b, b + c > a, of which only the shorter pair can fail.
II — *The third side lives between the difference and the sum* (Math Nation 6.2): sides 4 and 9 → more than 5, less
than 13. III — *Right triangles, and the converse*: the 3-4-5 triangle with its squares, 9 + 16 = 25 (the Pythagorean
Theorem, to memorize — 6.03 uses it); the converse: with a, b the two shorter sides and c the longest, a² + b² = c²
means right, anything else means not right. 9, 15, 12 → 81 + 144 = 225 = 15², right; 5, 6, 8 → 61 ≠ 64, not right.

**Examples.** 1 — 5 cm, 8 cm, 14 cm: 13 < 14, no triangle. *Your Turn:* 7 in, 9 in, 15 in: 16 > 15, a triangle.
2 — 20 m, 12 m, 16 m: 144 + 256 = 400 = 20², right. *Your Turn:* 8 ft, 11 ft, 14 ft: 185 ≠ 196, not right.

**Boards.**
1. 2 ft, 7 ft, 10 ft — a triangle? No (9 < 10).
2. 6 m, 6 m, 11 m — a triangle? Yes (12 > 11): two equal sides are no problem.
3. *MC* Which three lengths make a triangle? 5, 11, 8 ✓ · 3, 10, 6 (added the first two listed) · 7, 7, 14 (the
   equal case counted) · 12, 4, 6 (added the longest to another side).
4. Two sides are 7 cm and 12 cm: what can the third side be? More than 5 cm and less than 19 cm.
5. *MC* Two sides are 6 cm and 10 cm; which could be the third side? 12 ✓ · 4 (the equal case at the bottom) · 16
   (the equal case at the top) · 3 (shorter than the difference).
6. 8, 15, 17 — a right triangle? Yes (64 + 225 = 289).
7. *MC* Sides 25 cm, 7 cm, 24 cm — right, and which answer has the right reason? "Yes, because 7² + 24² = 25²" ✓ ·
   "No, because 25² + 7² ≠ 24²" (tested the last-listed side) · "No, because 7 + 24 ≠ 25" (added the sides, not the
   squares) · "Yes, because 7 + 24 > 25" (the right verdict for the wrong reason: the inequality is not the test).
8. *Extra number* A sail with sides 20 ft, 21 ft and 29 ft weighs 12 pounds — does it have a right angle? Yes.
9. *Written* Ana says 6, 7 and 9 make a right triangle because 6 + 7 > 9. Her test shows only that it IS a triangle;
   36 + 49 = 85 ≠ 81, so not right.

**Independent set (kinds).** a triangle? (no) · a triangle? (the equal case) · the third side's range · right? (yes,
a big triple) · right? (no, longest listed first) · a story: is a frame's corner square?

---

## 6.03 · Mon 9 Nov · Pythagorean Theorem · MA.8.GR.1.1

IXL: Pythagorean theorem: find the missing leg or hypotenuse length — MTM (due Tue 10 Nov).

**Target.** I can find a missing side of a right triangle — the hypotenuse, or a leg.

**Warm-up.** (yesterday, 6.01) is 10, 24, 26 a right triangle · (last week, 5.10–11) a rate used twice · (last unit,
4.05) √196 · (prior grade) 13² − 5², the subtraction a leg needs.

**Notes.** I — *a² + b² = c², and c is across from the right angle*: a right triangle labelled a, b, c, and the same
triangle turned so the right angle is on top — find the right angle first; the side across from it is c, the longest.
II — *The hypotenuse: add the squares, take the root*: legs 6 and 8 → 100 → 10; legs 3 and 5 → 34 → √34 ≈ 5.8 (exact
√34; 5.8 when a measurement is asked). III — *A leg: subtract*: hypotenuse 17, leg 15 → 289 − 225 = 64 → 8. A leg is
always shorter than the hypotenuse — the check that catches an added square.

**Examples.** 1 — legs 7 and 9: c² = 130, c = √130 ≈ 11.4. *Your Turn:* legs 5 and 11 → √146 ≈ 12.1.
2 — hypotenuse 26, leg 24: b² = 676 − 576 = 100, b = 10. *Your Turn:* hypotenuse 11, leg 6 → √85 ≈ 9.2 (not the book's
12-and-7 ladder, which its own TE keys wrong — audit D13).

**Boards.**
1. Legs 9 and 12: the hypotenuse? 15.
2. Legs 4 and 9: the hypotenuse? √97 ≈ 9.8.
3. Hypotenuse 25, a leg 20: the other leg? 15.
4. *MC* Hypotenuse 41, a leg 40: the other leg? 9 ✓ · 57.3 (added the squares) · 1 (subtracted the sides) · 81
   (forgot the square root).
5. A turned triangle (right angle on top), legs 5 and 7: the hypotenuse? √74 ≈ 8.6 — which side is c is the point.
6. *MC* Which equation finds x (hypotenuse 15, a leg 9, the other leg x)? 9² + x² = 15² ✓ · 9² + 15² = x² (the
   hypotenuse taken as a leg) · 9 + x = 15 (sides, not squares) · 2·9 + 2x = 2·15 (doubled instead of squared).
7. Hypotenuse 14, a leg 9: the other leg to the nearest tenth? √115 ≈ 10.7.
8. *Extra number* A flag cut as a right triangle with legs 8 in and 11 in costs $6 — its longest side? √185 ≈ 13.6 in.
9. *Written* Jo finds a leg: hypotenuse 15, leg 12, "√(144 + 225) ≈ 19.2". What went wrong, and what is the leg? A
   leg cannot be longer than the hypotenuse; subtract: 9.

**Independent set.** hypotenuse, whole · hypotenuse, √ and tenth · leg, whole (from a big hypotenuse) · leg, √ and
tenth · a turned triangle · which equation finds x.

---

## 6.04 · Tue 10 Nov · Pythagorean Theorem in Real-World Problems · MA.8.GR.1.1

IXL: Pythagorean theorem: word problems — 87U (due Thu 12 Nov).

**Target.** I can find a length in a real situation by finding the right triangle inside it.

**Warm-up.** (yesterday, 6.03) a leg from hypotenuse 13 and leg 12 · (last week, 6.01) a triangle? · (last unit, 5.04)
a plan's real length · (prior grade) a rectangle's two right angles at a corner — which side is across from one.

**Notes.** I — *Find the right angle, then c*: a ladder against a wall (wall and ground meet square; the ladder is c),
a screen and its diagonal, a ramp (rise, run, ramp), a path across a lawn. II — *c in a story*: a 5 m by 12 m garden,
its diagonal path 13 m. III — *a leg in a story*: a 10 ft ladder with its foot 3 ft from the wall reaches √91 ≈ 9.5 ft
(the state guide's own item, so it lives here and not on a board).

**Examples.** 1 — a ramp rises 2 ft over a run of 13 ft: √173 ≈ 13.2 ft. *Your Turn:* a screen 7 in by 10 in:
√149 ≈ 12.2 in. 2 — a 12 ft ladder, foot 5 ft out: √119 ≈ 10.9 ft up. *Your Turn:* a 13 ft ladder, foot 6 ft out:
√133 ≈ 11.5 ft.

**Boards.**
1. A monitor 9 in by 12 in: its diagonal? 15 in.
2. A 15 ft ladder, foot 9 ft out: how high? 12 ft.
3. A ramp, rise 1 ft, run 12 ft: its length? √145 ≈ 12.0 ft.
4. *MC* A 13 ft ladder reaches 12 ft up: how far out is its foot? 5 ✓ · 17.7 (added the squares) · 1 (subtracted the
   lengths) · 25 (forgot the root).
5. A 6 m by 8 m lawn: how much shorter is the walk across than the walk around two sides? 14 − 10 = 4 m.
6. *MC* A kite on 15 m of string flies above a point 9 m away: which length is the hypotenuse? the string ✓ · the
   height · the 9 m · "none — it is not a right triangle" (the right angle is at the ground, under the kite).
7. A 13 in umbrella in a flat box 5 in by 12 in: does it lie flat across the diagonal? Yes, exactly 13.
8. *Extra number* A 10 ft ladder that weighs 25 pounds stands 7 ft from a wall: how high does it reach? √51 ≈ 7.1 ft.
9. *Written* Why can a 9 ft ladder never reach a window 10 ft up, wherever its foot is? The ladder is the hypotenuse,
   the longest side; the height is a leg.

**Independent set.** a screen's diagonal · a ladder's height · a ramp's length (tenth) · around vs across · will it
fit · a kite's height.

---

## 6.05 · Thu 12 Nov · Distance on the Coordinate Plane · MA.8.GR.1.2

IXL: Find the distance between two points on a horizontal or vertical line — L9V; Find the distance between two
points — ZBP (due Fri 13 Nov).

**Target.** I can find the distance between two points: count or subtract on a line, and draw the right triangle when
the segment is slanted.

**Warm-up.** (yesterday, 6.04) a ladder's foot · (last week, 6.01) right triangle? · (last unit, 4.03) |−7| + |4| ·
(prior grade, MA.6.GR.1.2) the distance from (2, 5) to (2, −3).

**Notes.** I — *Same y: the x's; same x: the y's — and across zero, add*: (−4, 3) to (5, 3) is 4 + 5 = 9, never 1
(the state's named misconception). II — *Slanted: draw the right triangle*: (1, 2) to (4, 6), across 3, up 4 → 5.
III — *The legs come from the coordinates*: (−3, 4) to (2, −2): across 5, down 6 → √61 ≈ 7.8. No formula: the
dashed legs are the method.

**Examples.** 1 — (−6, −2) to (−6, 7): 9. *Your Turn:* (−3, 5) to (8, 5): 11. 2 — (−2, 1) to (4, 9): legs 6 and 8,
distance 10. *Your Turn:* (−5, −3) to (2, 1): legs 7 and 4, √65 ≈ 8.1.

**Boards.** From board 4 on, the grid shows the two points and nothing else — the student draws the legs (the
book's test plots the points and draws no triangle, and its 6.5 names "no triangle drawn" as where students stall).
1. (−7, −4) to (−7, 6): 10.
2. (−9, 2) to (3, 2): 12.
3. *MC* (−5, 1) to (3, 1): 8 ✓ · 2 (subtracted 5 − 3 across zero) · −8 (a distance is never negative) · 9 (counted the
   gridlines, not the spaces — the book's named error).
4. (−4, −3) to (5, 9): legs 9 and 12, 15.
5. (−2, −5) to (3, 3): legs 5 and 8, √89 ≈ 9.4.
6. *MC* Which gives the distance from (2, 7) to (−3, 1)? √(5² + 6²) ✓ · 5 + 6 (added the legs) · √(1² + 6²) (2 − 3
   across zero) · √(2² + 7²) (one point's coordinates as the legs).
7. The origin to (5, −12): 13.
8. *Extra number* A map in miles: school (−3, 2), library (4, 2), town hall (0, 5) — school to library? 7 mi.
9. *Written* Ty says (−4, 0) and (6, 0) are 2 units apart. What did he do? Subtracted 6 − 4; across zero it is
   4 + 6 = 10.

**Independent set.** horizontal across zero · vertical · slanted, whole · slanted, tenth · from the origin · a map.

---

## 6.06 · Fri 13 Nov · Real-World Coordinate-Plane Problems; Perimeter · MA.8.GR.1.2

IXL: Pythagorean theorem: find the perimeter — VGE (due Mon 16 Nov).

**Target.** I can find the perimeter of a figure on the coordinate plane, and a straight-line distance on a map.

**Warm-up.** (yesterday, 6.05) a slanted distance · (last week, 6.03) a hypotenuse · (last unit, 5.04) a map scale ·
(prior grade, MA.6.GR.1.3) the perimeter of a rectangle on the coordinate plane.

**Notes.** I — *Perimeter: every side, slanted ones by their triangles*: (1, 1), (4, 1), (4, 5): 3 + 4 + 5 = 12.
II — *Straight vs along the streets*: (−4, −3) to (2, 5): streets 6 + 8 = 14 blocks, straight 10. III — *Round at the
end*: keep √'s exact until the last step, then round the total once.

**Examples.** 1 — triangle (−3, −2), (3, −2), (3, 6): 6 + 8 + 10 = 24. *Your Turn:* (−5, −6), (4, −6), (4, 6): 36.
2 — a map: (−1, −4) to (4, 8): straight 13, streets 17. *Your Turn:* a second map pair, irrational, to the tenth.

**Boards.**
1. Perimeter of (0, −3), (5, −3), (5, 9): 5 + 12 + 13 = 30.
2. Perimeter of (−3, −4), (2, −4), (2, 3) to the tenth: 5 + 7 + √74 ≈ 20.6.
3. Perimeter of the triangle (−3, −1), (3, −1), (0, 3), which has no right angle: split it by its height (the book's
   move) — two slanted sides of 5 on a base of 6, so 16.
4. *MC* Perimeter of (−4, −2), (4, −2), (4, 4): 24 ✓ · 14 (left out the slanted side) · 28 (took the slanted side as
   the sum of the legs) · 114 (forgot the square root).
5. From (−6, −3) to (6, 2): how much shorter is the straight line than the streets? 17 − 13 = 4 blocks.
6. A rectangle (−3, −2), (5, −2), (5, 4), (−3, 4): its diagonal? 10.
7. A park map in meters, the fountain (−5, 2) and the gate (4, −3): straight across? √106 ≈ 10.3 m.
8. *Extra number* A map with a third point marked; the distance between the other two.
9. *Written* Why does counting the grid squares a slanted side crosses not give its length? (A unit square's
   diagonal is about 1.4, not 1.)

**Independent set.** perimeter, whole · perimeter, tenth · a quadrilateral · straight vs streets · a map, tenth · a
missing vertex.

---

## 6.07–08 · Mon 16 Nov · Similar Triangles; Indirect Measurement · MA.8.GR.2.4

IXL: Side lengths of similar triangles — QSK; Similar triangles and indirect measurement — 88W; Identify similar
triangles — 6PD (due Tue 17 Nov). The Unit Review goes home today with the independent set; the test is tomorrow.

**Target.** I can find a missing side of similar triangles with the scale factor, and use similar triangles to
measure what I cannot reach.

**Warm-up.** (yesterday, 6.06) a perimeter · (last week, 6.04) a ladder · (last unit, 5.01) a scale factor from two
sides · (prior grade) a unit rate from a ratio.

**Notes.** I — *Similar: matching angles equal, matching sides in one ratio*: 10, 6, 8 and 15, 9, 12 — every ratio
1.5 (the state guide's item, here in the notes); match shortest to shortest, longest to longest, or angle to angle —
in a turned picture by the angles, never by position. II — *A missing side: k, then multiply*: 4, 6, 7 and a copy
whose 4-side is 10 → k = 2.5 → 15 and 17.5. III — *Shadows*: a 6 ft person, a 4 ft shadow; a tree's shadow 20 ft at
the same time → the tree is 30 ft (the guide's own task). Same sun, same angle, similar triangles.

**Examples.** 1 — a turned pair, sides 5, 7, 9 and a copy whose 5-side is 15: k = 3, so 21 and 27. *Your Turn:*
3, 5, 6 with the 3-side 12: k = 4, so 20 and 24. 2 — a 5 ft girl's shadow is 3 ft; a flagpole's is 15 ft: 25 ft.
*Your Turn:* a 2 m post, a 1.5 m shadow; a building's shadow 12 m: 16 m.

**Boards.**
1. 8, 12, 14 and 12, 18, 21 — similar? Yes, every ratio 1.5.
2. A missing side, k whole (a copy at k = 3).
3. A missing side, k under 1: 20, 16, 12 and a copy whose 20-side is 5 → k = ¼, so 4 and 3.
4. *MC* A turned pair: which side matches the 9? (named error: matched by position on the page, not by the angles).
5. *MC* Which triangle is similar to 6-8-10? 9-12-15 ✓ · 8-10-12 (added 2 to every side) · 12-16-18 (checked two
   ratios, not three) · 6-8-12 (kept two sides equal — "similar means the same").
6. A 4 ft post casts a 2.5 ft shadow; a tree's shadow is 15 ft: 24 ft.
7. *Nested* A ramp is 0.6 m high 2 m from its start: how high 8 m from its start (the whole distance, measured from
   the shared corner)? 2.4 m.
8. *Extra number, the mirror* (the book's test shape, similarity stated in the words): a person whose eyes are 6 ft up
   stands 4 ft from a mirror on the ground and sees the top of a tree 20 ft beyond it; the tree's age (45 years) is the
   extra number. 30 ft.
9. *Written* Kim says 3-4-5 and 5-6-7 are similar because each side grew by 2. Similar means multiplied by one k:
   5/3, 6/4 and 7/5 are three different numbers.

**Independent set.** similar? · missing side · k < 1 · shadow · nested, with the gap given instead of the whole
distance (the book's "add the gap" move — its named overlapping-triangles error) · which is similar.

---

## T-B1 · Wed 18 Nov (43 minutes) · Angle Pairs: Supplementary, Complementary, Vertical, Adjacent · MA.8.GR.1.4

IXL: Identify complementary, supplementary, vertical, adjacent, and congruent angles — HGV; Find measures of
complementary, supplementary, vertical, and adjacent angles — R2B; Write and solve equations using angle relationships
— DBV (due Thu 19 Nov).

**Target.** I can name an angle pair and use it to find a missing angle, with an equation when the angles are
expressions.

**Notes.** I — *adjacent* (a shared vertex and side, no overlap) and *vertical* (across the crossing, equal).
II — *complementary* (90°) and *supplementary* (180°); a linear pair is supplementary; a right-angle mark is a 90
nobody printed. III — *Equations*: name the pair, then write "= 90", "= 180" or "equal" — a linear pair
(2x + 10)° and 50° → 2x + 60 = 180, x = 60; vertical angles 3x − 5 and 70 → x = 25. Then put x back: the question
is usually the angle (the book names "reported x as the angle" three times).

**Examples.** 1 — a right angle split by a ray into (2x + 6)° and (3x − 1)°: 5x + 5 = 90, x = 17, so 40° and 50°.
*Your Turn:* (4x)° and (x + 10)° → x = 16, so 64° and 26°. 2 — vertical angles (5x − 12)° and (2x + 18)°: 3x = 30,
x = 10, each angle 38° (variables on both sides, the book's own shape; the class solved these in Unit 1). *Your
Turn:* (4x + 3)° and (x + 39)° → x = 12, each 51°.

**Boards.**
1. The complement of 34°: 56°.
2. The supplement of 112°: 68°.
3. Two lines cross and one angle is 47°: its vertical angle 47°, its neighbour 133°.
4. *MC* ∠A and ∠B are complementary and ∠A = 28°: ∠B = 62° ✓ · 152° (used 180 — complementary and supplementary
   swapped, the state's named misconception) · 28° (took them as equal) · 118° (added 90 instead of subtracting).
5. A linear pair (3x + 15)° and 105°: x = 20.
6. Vertical angles (6x − 20)° and (2x + 28)°: each angle is 52° (x = 12 — a board that says 12 reported x).
7. *MC* Which pair is adjacent? (named errors: vertical called adjacent; two angles that overlap; two angles that
   share only a vertex).
8. *Extra number* A diagram with one more angle labelled than the question needs.
9. *Written* Can two vertical angles be complementary? Sometimes — only when each is 45° (the guide's
   always/sometimes/never item, decided here rather than inherited).

**The 43-minute cut:** boards 3 and 7 and two minutes of the IXL block; never board 9.

**Independent set.** complement · supplement · vertical · linear pair with x · vertical with x · name the pair.

---

## T-B2 · Thu 19 Nov · Interior and Exterior Angles of a Triangle · MA.8.GR.1.5

IXL: Find missing angles in triangles — JFJ; Exterior Angle Theorem — FMP; Triangle Angle-Sum Theorem — 6Q6
(due Fri 20 Nov).

**Target.** I can find a missing angle of a triangle, inside or outside, with the Triangle Sum and the Exterior Angle
Theorem.

**Notes.** I — *Triangle Sum*: the three corners torn off fill a straight line, 180° (on the FAST sheet). II — *The
Exterior Angle Theorem*, by name (the book's practice uses the name and its lesson never gives it; IXL FMP is called
that): an exterior angle (one side extended) and its adjacent interior angle make 180, so the exterior angle equals
the two REMOTE interior angles: L = 50°, M = 70° → the exterior angle at N is 120° (the guide's own item). Each corner
has two exterior angles, vertical to each other and equal — never the reflex angle around the outside (both are the
state's named misconceptions). III — *Algebra*: x, 2x, x + 20 → 4x + 20 = 180, x = 40 → 40°, 80°, 60°.

**Examples.** 1 — two angles of 58° and 71°: the third is 51°. *Your Turn:* 39° and 84° → 57°. 2 — remote interior
angles 64° and 49°: the exterior angle is 113°. *Your Turn:* 72° and 35° → 107°.

**Boards.**
1. Two angles 47° and 68°: the third is 65°.
2. An isosceles triangle with base angles of 52°: the third is 76°.
3. Remote interior angles 38° and 77°: the exterior angle is 115°.
4. *MC* Interior angles 45°, 60°, 75°; the exterior angle beside the 75°: 105° ✓ · 75° (the adjacent interior angle —
   the named error) · 255° (the reflex angle) · 180° (added all three interior angles).
5. An exterior angle of 130° with one remote angle of 55°: the other remote angle is 75°.
6. Angles x, 3x and 2x + 12: x = 28, so 28°, 84°, 68°.
7. *MC* Which equation fits the diagram (exterior (5x + 4)°, remote 52° and 3x°)? 5x + 4 = 52 + 3x ✓ (x = 24) ·
   5x + 4 + 3x = 180 (the exterior angle used as an interior one) · 5x + 4 = 3x (one remote angle only) ·
   5x + 4 + 52 + 3x = 180 (all four summed to 180) — the book's "which relationship justifies this equation" shape.
8. *Extra number* A triangle with an extra labelled angle outside it.
9. *Written* Why is an exterior angle always bigger than either remote interior angle?

**Independent set.** missing interior · isosceles · exterior · a remote angle · expressions · an equation from a
diagram.
