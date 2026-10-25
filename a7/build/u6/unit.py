# A7 Unit 6 — Relationships in Triangles: Reference Sheet, Unit Review (home Mon 16 Nov with 6.07's
# independent set; ruling 27a — A7 has no review day) and the assessment as THE PRACTICE TEST ALONE
# (ruling 49, 22 October): the unit test is a random set of the practice page, so this paper is the
# test's blueprint — its fourteen questions in this order with these points are what the page generates
# with new numbers and what the master sheet maps. One period (ruling 51): 14 questions, 18 points,
# sections by benchmark in the order GR.1.3 · GR.1.1 · GR.1.2 · GR.2.4, weighted 1 : 2 : 2 : 1 to the
# teaching days. No transfer items and no Form A/B (both retired for new units by ruling 49).
#
# The unit's standing decisions (outline §"standing decisions") hold on every page: every square root a
# student takes has a whole radicand up to 225 with no square factor (GR.1.1/1.2 Clarification 3, read
# strictly), so a whole hypotenuse is 5, 10, 13 or 15 and the bigger triples appear only as the converse
# or as a missing leg; an irrational length is given exactly and to the nearest tenth when the words ask
# for a measurement; no distance formula (a slanted distance is always the right triangle on the grid);
# the converse tests the longest side; similar triangles by the scale factor k from Unit 5. Every answer
# on the practice paper is a number, a letter or a set of letters (7 Oct: "I don't want to read
# explanations"). Thread B (T-B1, T-B2) is taught after the test and is not on it; its angle facts are
# on the reference sheet because the sheet goes home with the unit.
#
# not_bound=True marks every item whose root is not one of MA.8.NSO.1.7's perfect squares: its radicand is within
# GR.1.1/1.2's whole numbers up to 225 (Clarification 3) and square-free — the unit's own bound, which the course's
# capcheck (NSO.1.7) cannot see, so a scratch check holds it (every √n whole, at most 225, square-free; every
# "√n ≈ d" rounded right), as it held the lessons.
#
# Numbers: the reference sheet's examples are the lessons' own notes (what the class was shown); the
# review and the practice paper use their own, and none of their questions repeats a shown example.
from figs import right_triangle, grid, grid_poly, similar_pair, shadow


def _gr13():
    # question 1 — the three named ways to test the wrong thing: the equal case, the first two listed,
    # and the longest with another; only the two shorter sides can fail
    q1 = dict(stem="Which set of side lengths can form a triangle?",
              choices=["4 cm, 7 cm, 11 cm", "12 cm, 5 cm, 6 cm", "6 cm, 8 cm, 13 cm", "3 cm, 10 cm, 15 cm"], correct=2, answer="C", space=0.5,
              errors={"A": "4 + 7 = 11 counted — equal lies flat [6.01 Notes I]",
                      "B": "added the first two listed, 12 + 5 > 6 — but 5 + 6 = 11 is less than 12 [MA.8.GR.1.3: test the two shorter]",
                      "D": "added the longest with another, 15 + 3 > 10 — but 3 + 10 = 13 is less than 15 [MA.8.GR.1.3: test the two shorter]"},
              why="The two shorter sides against the longest: 6 + 8 = 14, more than 13. A lies flat; B and D pass only when the wrong pair is added.",
              check=("many", ("true", "6 + 8 > 13"), ("true", "4 + 7 == 11"), ("true", "5 + 6 < 12"), ("true", "3 + 10 < 15")))
    # question 2 — FAST's multiselect, which never says how many: one right set with its longest side
    # listed first, one the class has not met, a near miss, and two that pass only the Triangle Inequality
    q2 = dict(stem="Select ALL of the sets of side lengths that make a right triangle.",
              choices=["17, 8, 15", "5, 6, 7", "20, 21, 29", "7, 24, 26", "4, 6, 8"], correct=[0, 2], answer="A and C", space=0.8,
              errors={"B": "consecutive numbers, like 3, 4, 5 — but 25 + 36 = 61, not 49 [6.01 Notes III: test the squares]",
                      "D": "a near miss: 49 + 576 = 625 = 25², not 26² [6.01 Notes III: test the squares]",
                      "E": "a triangle, but not a right one: 16 + 36 = 52, not 64 [MA.8.GR.1.3: two tests — the Triangle Inequality shows only a triangle]"},
              why="Square all three and test the longest as c: 64 + 225 = 289 = 17² (the longest listed first) and 400 + 441 = 841 = 29². Both and nothing else for the point.",
              check=("many", ("eq", "8**2 + 15**2", "17**2"), ("eq", "20**2 + 21**2", "29**2"),
                     ("true", "5**2 + 6**2 != 7**2"), ("true", "7**2 + 24**2 != 26**2"), ("true", "4**2 + 6**2 != 8**2")))
    # question 3 — the book's own test shape: the third side between the difference and the sum
    q3 = dict(stem="Two sides of a triangle are 7 in and 12 in long. Which inequality shows every possible length x, in inches, of the third side?",
              choices=["$7 < x < 12$", "$5 < x < 19$", "$5 \\leq x \\leq 19$", "$0 < x < 19$"], correct=1, answer="B", space=0.4,
              errors={"A": "between the two given sides [6.01 Notes II: between the difference and the sum]",
                      "C": "≤ counts the flat cases: a side of exactly 5 or 19 lies flat [6.01 Notes I: equal is not a triangle]",
                      "D": "only the sum: a side of 5 in or less cannot reach across [6.01 Notes II: long enough to reach]"},
              why="12 − 7 = 5 and 12 + 7 = 19, never equal to either.",
              check=("many", ("eq", "12 - 7", "5"), ("eq", "12 + 7", "19")))
    return [q1, q2, q3]


def _gr11():
    q4 = dict(stem="Find the missing side of each right triangle.",
              parts=[dict(label="a", stem="Its legs are 9 in and 12 in. How long is the hypotenuse?", answer="15 in",
                          why="c² = 81 + 144 = 225", check=("eq", "sqrt(9**2 + 12**2)", "15"), space=0.5),
                     dict(label="b", stem="Its hypotenuse is 50 m and one leg is 48 m. How long is the other leg?", answer="14 m",
                          why="a leg: subtract — 2,500 − 2,304 = 196. Adding the squares gives a 'leg' longer than the hypotenuse.",
                          check=("eq", "sqrt(50**2 - 48**2)", "14"), space=0.6)])
    q5 = dict(not_bound=True, stem="A right triangle has legs of 7 cm and 13 cm. Find the length of the hypotenuse to the nearest tenth of a centimeter.",
              answer="14.8 cm  (exactly √218 cm)", why="c² = 49 + 169 = 218; √218 = 14.76…",
              check=("many", ("eq", "7**2 + 13**2", "218"), ("approx", "sqrt(218)", "14.8", "0.05")), space=0.7)
    # question 6 — the hypotenuse is the side across from the square corner, whatever way the triangle is turned
    q6 = dict(stem="Which equation can be used to find x?",
              fig=right_triangle(4, 65 ** 0.5, la="4", lb="x", lc="9", turn=200, inches=1.7),
              choices=["$4 + x = 9$", "$4^{2} + 9^{2} = x^{2}$", "$2 \\cdot 4 + 2x = 2 \\cdot 9$", "$4^{2} + x^{2} = 9^{2}$"], correct=3, answer="D", space=0.4,
              errors={"A": "the sides added, not their squares [MA.8.GR.1.1: the theorem is about squares]",
                      "B": "the hypotenuse put with the legs [Source of Truth, GR.1.1: misidentifying the hypotenuse]",
                      "C": "doubled instead of squared [B1G-M, GR.1.1: doubling versus squaring]"},
              why="The 9 is across from the right angle, so it is c and stands alone: x² = 81 − 16 = 65.",
              check=("many", ("eq", "sqrt(9**2 - 4**2)", "sqrt(65)"), ("true", "sqrt(4**2 + 9**2) != sqrt(65)"),
                     ("true", "9 - 4 != sqrt(65)"), ("true", "(2*9 - 2*4)/2 != sqrt(65)")))
    q7 = dict(not_bound=True, stem="A rectangular field is 9 m wide and 10 m long. A path runs straight across it from one corner to the opposite corner.",
              parts=[dict(label="a", stem="How long is the path, to the nearest tenth of a meter?", answer="13.5 m  (exactly √181 m)",
                          why="the path is the hypotenuse: 81 + 100 = 181", check=("many", ("eq", "9**2 + 10**2", "181"), ("approx", "sqrt(181)", "13.5", "0.05")), space=0.6),
                     dict(label="b", stem="How much shorter is the path than walking along two sides of the field?", answer="5.5 m",
                          why="9 + 10 = 19 m along two sides; 19 − 13.5. Follow-through on part (a).",
                          check=("approx", "9 + 10 - sqrt(181)", "5.5", "0.05"), space=0.5)])
    return [q4, q5, q6, q7]


def _gr12():
    # question 8 — the grid shows the two points and nothing else: the student draws the legs
    q8 = dict(stem="Find the distance between points A and B.",
              fig=grid((-8, 6), (-5, 3), points=[(-7, 1, "A"), (5, -4, "B")], step=2, inches=3.3),
              answer="13 units", why="Across 5 − (−7) = 12, down 1 − (−4) = 5: c² = 144 + 25 = 169.",
              check=("eq", "sqrt((5 - (-7))**2 + (1 - (-4))**2)", "13"), space=0.7)
    q9 = dict(not_bound=True, stem="Find the distance between (−1, 3) and (4, 1) to the nearest tenth.",
              answer="5.4 units  (exactly √29)", why="Across 5, down 2: c² = 25 + 4 = 29.",
              check=("many", ("eq", "(4 - (-1))**2 + (3 - 1)**2", "29"), ("approx", "sqrt(29)", "5.4", "0.05")), space=0.7)
    q10 = dict(not_bound=True, stem="Triangle JKL has corners J(−6, 1), K(8, 1) and L(8, 6).",
               fig=grid_poly((-7, 9), (-1, 7), [(-6, 1), (8, 1), (8, 6)], names="JKL", step=2, inches=3.5),
               parts=[dict(label="a", stem="Find the length of side JK.", answer="14 units", why="Across zero: 6 + 8 — never 8 − 6.",
                           check=("eq", "8 - (-6)", "14"), space=0.4),
                      dict(label="b", stem="Find the perimeter of triangle JKL to the nearest tenth.", answer="33.9 units",
                           why="KL = 5; JL = √(196 + 25) = √221 ≈ 14.866; 14 + 5 + 14.866 = 33.866 — round once, at the end. Follow-through on part (a).",
                           check=("many", ("eq", "6 - 1", "5"), ("approx", "14 + 5 + sqrt(14**2 + 5**2)", "33.9", "0.05")), space=0.7)])
    q11 = dict(stem="On a town map, each unit is one block. The library is at (−1, −5) and the pool is at (8, 7).",
               parts=[dict(label="a", stem="How far is it from the library to the pool along the streets?", answer="21 blocks",
                           why="The streets follow the grid: 9 across and 12 up.", check=("eq", "(8 - (-1)) + (7 - (-5))", "21"), space=0.5),
                      dict(label="b", stem="How far is it in a straight line?", answer="15 blocks", why="The hypotenuse of legs 9 and 12: 81 + 144 = 225.",
                           check=("eq", "sqrt(9**2 + 12**2)", "15"), space=0.5)])
    return [q8, q9, q10, q11]


def _gr24():
    # question 12 — the copy is turned, so its sides are matched by size, not by place on the page
    q12 = dict(stem="The two triangles are similar. Find x.",
               fig=similar_pair((8, 10, 14), (12, 15, 21), l1=("8", "10", "14"), l2=("12", "15", "x"), turn2=180, gap=0.9, inches=4.2),
               answer="x = 21", why="Match by size: 12 with 8 and 15 with 10, so k = 1.5 and x = 14 × 1.5. 26.25 matched by place on the page (15 with the 8); 14 took similar as equal; 18 added the difference 12 − 8.",
               check=("many", ("eq", "F(12,8)", "F(3,2)"), ("eq", "F(15,10)", "F(3,2)"), ("eq", "14*F(3,2)", "21")), space=0.6)
    q13 = dict(stem="A boy 4 ft tall casts a shadow 5 ft long. At the same moment, a tree casts a shadow 30 ft long. How tall is the tree?",
               fig=shadow(4, 5, 24, 30, l=("4", "5", "h", "30"), unit="ft", what=("boy", "tree"), inches=3.2),
               answer="24 ft", why="k = 30 ÷ 5 = 6 from the shadows; 4 × 6. 37.5 matched height and shadow crosswise; 120 multiplied by the boy's height, not by k.",
               check=("eq", "4*F(30,5)", "24"), space=0.6)
    q14 = dict(stem="Which triangle is similar to a triangle with sides 6, 9 and 12?",
               choices=["8, 12, 16", "9, 12, 15", "12, 18, 20", "6, 9, 14"], correct=0, answer="A", space=0.5,
               errors={"B": "added 3 to every side [Source of Truth, GR.2.4: similar means multiplied, not added]",
                       "C": "checked two ratios, not three: 20 ÷ 12 is not 2 [6.07 Notes I: all three ratios]",
                       "D": "kept two sides the same [Source of Truth, GR.2.4: similar triangles assumed to have equal sides]"},
               why="Every side × 4/3: 8/6 = 12/9 = 16/12.",
               check=("many", ("eq", "F(8,6)", "F(4,3)"), ("eq", "F(12,9)", "F(4,3)"), ("eq", "F(16,12)", "F(4,3)"),
                      ("true", "F(9,6) != F(12,9)"), ("true", "F(20,12) != 2"), ("true", "F(14,12) != 1")))
    return [q12, q13, q14]


def _sections(form="practice"):
    """The practice test, the only form (ruling 49): the blueprint of the unit test."""
    assert form == "practice", "ruling 49: Unit 6's assessment is the practice test alone"
    return [dict(title="Triangle Inequality and the Converse", benchmark="MA.8.GR.1.3", items=_gr13()),
            dict(title="The Pythagorean Theorem", benchmark="MA.8.GR.1.1", items=_gr11()),
            dict(title="Distance on the Coordinate Plane", benchmark="MA.8.GR.1.2", items=_gr12()),
            dict(title="Similar Triangles", benchmark="MA.8.GR.2.4", items=_gr24())]


U = dict(
    unit=6, title="Relationships in Triangles",
    review_note="HOW TO USE THIS.   This review covers every learning target of Lessons 1–8 — more than the test does. Work it in parts. If you miss two or more in a part, that part is where to spend your study time. The reference sheet has everything you need for each part. Thread B's two angle days come after the test and are not on it.",
    reference_intro="Two things on this page are printed on the Grade 8 FAST reference sheet: the Triangle Inequality Theorem (section 1) and the Triangle Sum Theorem (section 5). Everything else is tested from memory — the Pythagorean Theorem and its converse are not on the state's sheet, and neither is distance on the grid, similar triangles or the angle pairs. On this unit's test you will not have either sheet. Section 5 is taught on the Thread B days, after the test; it is here because this sheet goes home with the unit.",

    reference=[
        dict(title="1.   The Triangle Inequality and the Converse", right="Lessons 1–2 · the two shorter sides; the longest as c",
             blocks=["**The Triangle Inequality: the two shorter sides must add to MORE than the longest.**  The FAST sheet prints it as $a + b > c$, $a + c > b$, $b + c > a$. Adding the two shorter sides checks all three at once, because that is the only pair that can fail. It is true of every triangle, not only right ones.",
                     dict(table=([1900, 2500, 2300, 2660], [
                         ["Sides", "The two shorter, added", "Against the longest", "A triangle?"],
                         ["3, 4, 9", "3 + 4 = 7", "7 < 9", "No — too short to meet"],
                         ["4, 5, 9", "4 + 5 = 9", "9 = 9", "No — equal lies flat"],
                         ["5, 6, 9", "5 + 6 = 11", "11 > 9", "Yes"],
                         ["10, 4, 7", "4 + 7 = 11", "11 > 10", "Yes — the longest is listed first"]])),
                     "**The third side is between the difference and the sum of the other two.**  Sides 4 and 9: the third side is more than 9 − 4 = 5 and less than 9 + 4 = 13, so $5 < x < 13$. Never $\\leq$: a third side of exactly 5 or 13 lies flat.",
                     "**The converse of the Pythagorean Theorem: square all three and test the LONGEST side as c.**  If the two shorter sides' squares add to the longest side's square, the triangle is right; if not, it is not — and passing the Triangle Inequality only shows there is a triangle. 9, 15, 12: $9^{2} + 12^{2} = 81 + 144 = 225 = 15^{2}$ — right, though the longest side is listed in the middle. 5, 6, 8: $25 + 36 = 61$, not 64 — a triangle, but not a right one.",
                     "**Right triangles worth knowing by sight** (and any whole-number multiple of one): 3-4-5, 5-12-13, 8-15-17 and 7-24-25 — so 6-8-10 and 9-12-15 as well. Anything else, square and check."]),
        dict(title="2.   The Pythagorean Theorem", right="Lessons 3–4 · c is across from the right angle",
             blocks=["**The Pythagorean Theorem.**  $a^{2} + b^{2} = c^{2}$: the legs a and b make the right angle, and the hypotenuse c is across from it — always the longest side. It is not on the FAST sheet: know it cold.",
                     dict(table=([2300, 3400, 3660], [
                         ["To find", "Do this", "Example"],
                         ["the hypotenuse", "square the legs, add, take the root", "legs 6 and 8: 36 + 64 = 100, c = 10"],
                         ["a leg", "square, subtract from c², take the root", "c = 17 and a leg 15: 289 − 225 = 64, the leg is 8"],
                         ["a length that is not whole", "the same, then the root to the nearest tenth", "legs 3 and 5: 9 + 25 = 34, c = √34 ≈ 5.8"]])),
                     "**Exact, or to the nearest tenth.**  $\\sqrt{34}$ is the exact length; 5.8 is that length to the nearest tenth, the one to give when a question asks for a measurement. Every root in this unit is of a whole number up to 225 with no square factor, so $\\sqrt{34}$ is already as simple as it gets.",
                     "**Check the size.**  A leg is shorter than the hypotenuse. A leg that comes out longer than c was found by adding the squares — a leg is found by subtracting.",
                     "**In a story: find the right angle first; the side across from it is c.**  A ladder against a wall (the wall meets the ground square, so the ladder is c), the diagonal of a rectangle, a ramp over its run, the size of a screen (its diagonal). A 10-ft ladder with its foot 3 ft from the wall reaches $\\sqrt{100 - 9} = \\sqrt{91} \\approx 9.5$ ft up the wall. Round once, at the end."]),
        dict(title="3.   Distance on the Coordinate Plane", right="Lessons 5–6 · a slanted distance is a hypotenuse",
             blocks=["**On one line: subtract the coordinates that change — and across zero, add.**  From (−4, 3) to (5, 3) the y's match, so take the x's: $5 - (-4) = 9$ — 4 to the axis and 5 past it, never 1. Count the spaces, not the grid lines. A distance is never negative.",
                     "**A slanted distance is the hypotenuse of a right triangle drawn on the grid.**  Draw the across leg and the up-or-down leg, read their lengths from the coordinates, then use $a^{2} + b^{2} = c^{2}$. From (−3, 4) to (2, −2): across 5, down 6, so $c = \\sqrt{25 + 36} = \\sqrt{61} \\approx 7.8$. That is the whole method; there is no distance formula to learn.",
                     "**A perimeter adds every side, and a slanted side is found by its own triangle.**  (1, 1), (4, 1), (4, 5): 3 + 4 + 5 = 12. When a side is a root, keep three decimal places and round only the total: 6 + 5.831 + 5.831 = 17.662 ≈ 17.7, where 6 + 5.8 + 5.8 = 17.6 comes up short.",
                     "**Along the streets, or straight.**  On a map in blocks the streets follow the grid, so the trip along them adds the legs: 6 + 8 = 14 blocks. The straight line is the hypotenuse, 10 blocks — always the shorter way, unless the two places are on one street."]),
        dict(title="4.   Similar Triangles", right="Lessons 7–8 · one scale factor on every side",
             blocks=["**Similar triangles: matching angles are equal, and matching sides are in one ratio, the scale factor k.**  6, 8, 10 and 9, 12, 15: $\\frac{9}{6} = \\frac{12}{8} = \\frac{15}{10} = 1.5$. Check all three ratios — two equal ratios are not enough — and adding the same amount to every side never makes a similar triangle.",
                     "**Match the sides by size, not by where they sit on the page.**  Sort each triangle's sides: shortest with shortest, longest with longest. A turned or flipped copy is matched the same way, or by its equal angles.",
                     "**A missing side: k = copy ÷ original, then multiply.**  A triangle 4, 6, 7 and a similar copy whose 4-side is 10: $k = \\frac{10}{4} = 2.5$, so its other sides are $6 \\times 2.5 = 15$ and $7 \\times 2.5 = 17.5$. A smaller copy has k less than 1.",
                     "**Indirect measurement: the same sun makes the same angle.**  A 6-ft person casts a 4-ft shadow as a tree casts a 20-ft shadow: $k = \\frac{20}{4} = 5$, so the tree is $6 \\times 5 = 30$ ft. A mirror on the ground works the same way — light leaves it at the angle it arrived — so the two triangles are similar, and the heights and the distances from the mirror are in one ratio."]),
        dict(title="5.   Angle Facts", right="Thread B · after the unit test, and all year",
             blocks=[dict(table=([2300, 4200, 2860], [
                         ["Two angles that are", "mean", "Example"],
                         ["complementary", "they add to 90°", "64° and 26°"],
                         ["supplementary", "they add to 180°", "60° and 120°"],
                         ["vertical", "across from each other where two lines cross — always equal", "51° and 51°"],
                         ["adjacent", "they share a vertex and a side, and do not overlap", "a right angle split into 40° and 50°"],
                         ["a linear pair", "adjacent and supplementary: together a straight line", "130° and 50°"]])),
                     "**The Triangle Sum Theorem: the three angles of a triangle add to 180°.**  It is on the FAST reference sheet. Angles of 65° and 40°: the third angle is 180° − 105° = 75°.",
                     "**The Exterior Angle Theorem: an exterior angle equals the two remote interior angles added.**  Remote interior angles of 50° and 70° make an exterior angle of 120° — not the interior angle beside it, which is 60° (the two make a straight line, 180°).",
                     "**With x: name the fact, write its equation, solve, then put x back.**  A triangle's angles are x, x and 2x + 20: $x + x + (2x + 20) = 180$, so $4x = 160$ and $x = 40$ — the angles are 40°, 40° and 100°."]),
        dict(title="6.   Vocabulary",
             blocks=[dict(vocab=[
                 ("Triangle Inequality Theorem", "the two shorter sides of a triangle add to more than the longest side"),
                 ("right triangle, legs, hypotenuse", "a triangle with a right angle; the two sides that make the right angle; the side across from it, always the longest"),
                 ("Pythagorean Theorem", "in a right triangle, $a^{2} + b^{2} = c^{2}$"),
                 ("converse of the Pythagorean Theorem", "if the two shorter sides' squares add to the longest side's square, the triangle is a right triangle"),
                 ("Pythagorean triple", "three whole numbers that are the sides of a right triangle, such as 5, 12, 13"),
                 ("distance", "the length of the segment between two points; never negative"),
                 ("perimeter", "the distance around a figure: every side added"),
                 ("similar triangles", "triangles whose matching angles are equal and whose matching sides are in one ratio"),
                 ("corresponding sides", "a side of one triangle and the side of a similar triangle that matches it"),
                 ("scale factor (k)", "copy ÷ original: every side of the copy is k times the side it matches"),
                 ("indirect measurement", "finding a length you cannot reach from similar triangles you can measure"),
                 ("complementary, supplementary", "two angles that add to 90°; two angles that add to 180°"),
                 ("vertical angles", "the angles across from each other where two lines cross; always equal"),
                 ("adjacent angles", "two angles that share a vertex and a side and do not overlap"),
                 ("exterior angle, remote interior angles", "the angle between one side of a triangle and the next side extended; the two inside angles that are not beside it")])]),
    ],

    # ------------------------------------------------------------------ unit review (unscored; home Mon 16 Nov)
    review=[
        dict(letter="A", title="The Triangle Inequality and the Converse", lessons="Lessons 1–2", benchmark="MA.8.GR.1.3", items=[
            dict(stem="Can the three lengths be the sides of a triangle? Show the test.", parts=[
                dict(label="a", stem="5 cm, 9 cm and 15 cm", answer="No — 5 + 9 = 14 is less than 15.", why="the two shorter sides against the longest",
                     check=("true", "5 + 9 < 15"), space=0.3),
                dict(label="b", stem="6 in, 10 in and 16 in", answer="No — 6 + 10 = 16 is equal to the longest side, so the sides lie flat.", why="equal is not more",
                     check=("true", "6 + 10 == 16"), space=0.3),
                dict(label="c", stem="11 m, 4 m and 8 m", answer="Yes — 4 + 8 = 12 is more than 11.", why="the longest is listed first; 11 + 4 tests the wrong pair",
                     check=("true", "4 + 8 > 11"), space=0.3)]),
            dict(stem="Two sides of a triangle are 6 ft and 14 ft. Write an inequality for every possible length x of the third side.", answer="8 < x < 20",
                 why="between the difference, 14 − 6, and the sum, 14 + 6 — never equal to either", check=("many", ("eq", "14 - 6", "8"), ("eq", "14 + 6", "20")), space=0.5),
            dict(stem="Is a triangle with these sides a right triangle? Show the test.", parts=[
                dict(label="a", stem="25, 24 and 7", answer="Yes — 7² + 24² = 49 + 576 = 625 = 25².", why="the longest, 25, is c, though it is listed first",
                     check=("eq", "7**2 + 24**2", "25**2"), space=0.4),
                dict(label="b", stem="7, 8 and 11", answer="No — 49 + 64 = 113, and 11² = 121.", why="a triangle (7 + 8 > 11), but not a right one",
                     check=("true", "7**2 + 8**2 != 11**2"), space=0.4)]),
            dict(stem="Which set of side lengths makes a right triangle?",
                 choices=["6, 7, 8", "10, 24, 26", "3, 4, 7", "8, 9, 12"], correct=1, answer="B", space=0.5,
                 errors={"A": "consecutive numbers, like 3, 4, 5 — but 36 + 49 = 85, not 64 [6.01 Notes III: test the squares]",
                         "C": "3 and 4 from 3-4-5, and 3 + 4 = 7: these lie flat, not even a triangle [MA.8.GR.1.3]",
                         "D": "a near miss: 64 + 81 = 145, not 144 [6.01 Notes III: test the squares]"},
                 why="100 + 576 = 676 = 26².",
                 check=("many", ("eq", "10**2 + 24**2", "26**2"), ("true", "6**2 + 7**2 != 8**2"), ("true", "3 + 4 == 7"), ("true", "8**2 + 9**2 != 12**2"))),
        ]),
        dict(letter="B", title="The Pythagorean Theorem", lessons="Lesson 3", benchmark="MA.8.GR.1.1", items=[
            dict(stem="A right triangle has legs of 12 ft and 5 ft. How long is the hypotenuse?", answer="13 ft", why="144 + 25 = 169",
                 check=("eq", "sqrt(12**2 + 5**2)", "13"), space=0.5),
            dict(not_bound=True, stem="A right triangle has legs of 3 in and 13 in. How long is the hypotenuse, exactly and to the nearest tenth?", answer="√178 in ≈ 13.3 in", why="9 + 169 = 178",
                 check=("many", ("eq", "3**2 + 13**2", "178"), ("approx", "sqrt(178)", "13.3", "0.05")), space=0.5),
            dict(stem="A right triangle has a hypotenuse of 41 cm and one leg of 40 cm. How long is the other leg?", answer="9 cm", why="1,681 − 1,600 = 81",
                 check=("eq", "sqrt(41**2 - 40**2)", "9"), space=0.5),
            dict(not_bound=True, stem="A right triangle has a hypotenuse of 11 ft and one leg of 8 ft. How long is the other leg, exactly and to the nearest tenth?", answer="√57 ft ≈ 7.5 ft", why="121 − 64 = 57",
                 check=("many", ("eq", "11**2 - 8**2", "57"), ("approx", "sqrt(57)", "7.5", "0.05")), space=0.5),
            dict(stem="A right triangle has a hypotenuse of 15 cm and one leg of 9 cm. How long is the other leg?",
                 choices=["12 cm", "6 cm", "17.5 cm", "144 cm"], correct=0, answer="A", space=0.5,
                 errors={"B": "subtracted the sides, 15 − 9 [MA.8.GR.1.1: the theorem is about squares]",
                         "C": "added the squares instead of subtracting: longer than the hypotenuse [6.03 Notes III: for a leg, subtract]",
                         "D": "stopped at b² = 144 and forgot the square root [Math Nation names skipping the final root]"},
                 why="225 − 81 = 144 = 12².",
                 check=("many", ("eq", "sqrt(15**2 - 9**2)", "12"), ("eq", "15 - 9", "6"), ("approx", "sqrt(15**2 + 9**2)", "17.5", "0.05"), ("eq", "15**2 - 9**2", "144"))),
            dict(stem="Ana finds the missing leg of a right triangle whose hypotenuse is 5 cm and whose other leg is 3 cm. She writes $3^{2} + 5^{2} = 34$, so the leg is about 5.8 cm. What did she do wrong? Find the leg.",
                 answer="She added the squares, and a leg cannot be longer than the 5-cm hypotenuse. Subtract: 25 − 9 = 16, so the leg is 4 cm.",
                 why="the error named and the leg found", check=("eq", "sqrt(5**2 - 3**2)", "4"), space=0.9),
        ]),
        dict(letter="C", title="The Pythagorean Theorem in Real-World Problems", lessons="Lesson 4", benchmark="MA.8.GR.1.1", items=[
            dict(stem="A 13-ft ladder leans against a wall with its foot 5 ft from the wall. How high up the wall does it reach?", answer="12 ft", why="the ladder is c: 169 − 25 = 144",
                 check=("eq", "sqrt(13**2 - 5**2)", "12"), space=0.5),
            dict(not_bound=True, stem="A rectangular garden is 10 m long and 11 m wide. How long is a path straight across it from corner to corner, to the nearest tenth of a meter?", answer="About 14.9 m (√221 m)", why="the diagonal is c: 100 + 121 = 221",
                 check=("many", ("eq", "10**2 + 11**2", "221"), ("approx", "sqrt(221)", "14.9", "0.05")), space=0.5),
            dict(not_bound=True, stem="A ramp rises 1 ft over a run of 9 ft along the ground. How long is the ramp, to the nearest tenth of a foot?", answer="About 9.1 ft (√82 ft)", why="the ramp is c: 1 + 81 = 82",
                 check=("many", ("eq", "1**2 + 9**2", "82"), ("approx", "sqrt(82)", "9.1", "0.05")), space=0.5),
            dict(not_bound=True, stem="A park is a rectangle 9 m by 11 m. How much shorter is it to walk straight across the park from corner to corner than to walk along two of its sides? Give the answer to the nearest tenth.",
                 answer="About 5.8 m", why="along two sides 20 m; across √202 ≈ 14.2 m",
                 check=("many", ("eq", "9**2 + 11**2", "202"), ("approx", "9 + 11 - sqrt(202)", "5.8", "0.05")), space=0.7),
            dict(not_bound=True, stem="A 9-ft ladder stands with its foot 2 ft from a wall. Will it reach a window ledge 8.5 ft up the wall?",
                 answer="Yes — it reaches √77 ≈ 8.8 ft up the wall, above 8.5 ft.", why="the height is a leg: 81 − 4 = 77",
                 check=("many", ("eq", "9**2 - 2**2", "77"), ("true", "sqrt(77) > F(17,2)")), space=0.7),
        ]),
        dict(letter="D", title="Distance on the Coordinate Plane", lessons="Lesson 5", benchmark="MA.8.GR.1.2", items=[
            dict(stem="Find the distance between the two points.", parts=[
                dict(label="a", stem="(−6, 2) and (5, 2)", answer="11 units", why="across zero: 6 + 5", check=("eq", "5 - (-6)", "11"), space=0.4),
                dict(label="b", stem="(3, −7) and (3, 2)", answer="9 units", why="across zero: 7 + 2", check=("eq", "2 - (-7)", "9"), space=0.4)]),
            dict(stem="Find the distance between points P and Q.",
                 fig=grid((-6, 4), (-3, 5), points=[(-5, -2, "P"), (3, 4, "Q")], inches=2.5),
                 answer="10 units", why="across 8, up 6: 64 + 36 = 100", check=("eq", "sqrt((3 - (-5))**2 + (4 - (-2))**2)", "10"), space=0.7),
            dict(not_bound=True, stem="Find the distance between (−6, −1) and (1, 5), to the nearest tenth.", answer="About 9.2 units (√85)", why="across 7, up 6: 49 + 36 = 85",
                 check=("many", ("eq", "(1 - (-6))**2 + (5 - (-1))**2", "85"), ("approx", "sqrt(85)", "9.2", "0.05")), space=0.5),
            dict(not_bound=True, stem="How far is the point (−9, 4) from the origin, to the nearest tenth?", answer="About 9.8 units (√97)", why="legs 9 and 4: 81 + 16 = 97",
                 check=("many", ("eq", "9**2 + 4**2", "97"), ("approx", "sqrt(97)", "9.8", "0.05")), space=0.5),
            dict(stem="What is the distance between (−3, 4) and (5, 4)?",
                 choices=["2 units", "8 units", "9 units", "−8 units"], correct=1, answer="B", space=0.3,
                 errors={"A": "5 − 3: subtracted across zero [Source of Truth, GR.1.2: (−2, 0) to (3, 0) is not 1]",
                         "C": "counted the grid lines, not the spaces [Math Nation names counting gridlines]",
                         "D": "a distance is never negative [6.05 Notes I]"},
                 why="5 − (−3) = 8: 3 to the axis and 5 past it.",
                 check=("many", ("eq", "5 - (-3)", "8"), ("true", "5 - 3 != 8"), ("true", "9 != 8"), ("true", "-8 != 8"))),
        ]),
        dict(letter="E", title="Coordinate-Plane Problems and Perimeter", lessons="Lesson 6", benchmark="MA.8.GR.1.2", items=[
            dict(stem="Every part below is about triangle PQR on the grid, with corners P(−4, −4), Q(8, −4) and R(8, 5).",
                 key_stem="**SSDD.**   Every part below is about one triangle on the grid: P(−4, −4), Q(8, −4), R(8, 5).  Same surface, six different questions: two distances on a line (both across zero), the slanted side as a hypotenuse, a perimeter, around against across, and a similar copy — the unit's moves on one triangle, so that a student learns to read the question and not the picture.",
                 fig=grid_poly((-6, 10), (-6, 6), [(-4, -4), (8, -4), (8, 5)], names="PQR", step=2, inches=2.7),
                 parts=[
                     dict(label="a", stem="Find the length of PQ.", answer="12 units", why="across zero: 4 + 8", check=("eq", "8 - (-4)", "12"), space=0.3),
                     dict(label="b", stem="Find the length of QR.", answer="9 units", why="across zero: 4 + 5", check=("eq", "5 - (-4)", "9"), space=0.3),
                     dict(label="c", stem="Find the length of PR.", answer="15 units", why="the hypotenuse of legs 12 and 9: 144 + 81 = 225", check=("eq", "sqrt(12**2 + 9**2)", "15"), space=0.4),
                     dict(label="d", stem="Find the perimeter of triangle PQR.", answer="36 units", why="12 + 9 + 15", check=("eq", "12 + 9 + 15", "36"), space=0.3),
                     dict(label="e", stem="How much shorter is the trip straight from P to R than the trip from P to Q to R?", answer="6 units", why="21 − 15",
                          check=("eq", "(12 + 9) - 15", "6"), space=0.3),
                     dict(label="f", stem="A triangle similar to PQR has a shortest side of 3. How long is its longest side?", answer="5", why="k = 3 ÷ 9 = 1/3, and 15 × 1/3 — a copy smaller than the original",
                          check=("eq", "15*F(3,9)", "5"), space=0.4)]),
            dict(not_bound=True, stem="Find the perimeter of the triangle with corners (−4, 2), (6, 2) and (6, −1), to the nearest tenth.", answer="About 23.4 units",
                 why="10 + 3 + √109; √109 ≈ 10.440 — round once, at the end",
                 check=("many", ("eq", "6 - (-4)", "10"), ("eq", "2 - (-1)", "3"), ("approx", "13 + sqrt(109)", "23.4", "0.05")), space=0.8),
            dict(stem="On a town map in blocks, the school is at (−3, −4) and the park is at (9, 1).", parts=[
                dict(label="a", stem="How far is it from the school to the park along the streets?", answer="17 blocks", why="12 across + 5 up",
                     check=("eq", "(9 - (-3)) + (1 - (-4))", "17"), space=0.5),
                dict(label="b", stem="How far is it in a straight line?", answer="13 blocks", why="144 + 25 = 169",
                     check=("eq", "sqrt(12**2 + 5**2)", "13"), space=0.5)]),
            dict(stem="A rectangle has corners (−3, −2), (5, −2), (5, 4) and (−3, 4).", parts=[
                dict(label="a", stem="Find its perimeter.", answer="28 units", why="8 + 6 + 8 + 6", check=("eq", "2*((5 - (-3)) + (4 - (-2)))", "28"), space=0.5),
                dict(label="b", stem="Find the length of one of its diagonals.", answer="10 units", why="64 + 36 = 100", check=("eq", "sqrt(8**2 + 6**2)", "10"), space=0.5)]),
        ]),
        dict(letter="F", title="Similar Triangles and Indirect Measurement", lessons="Lessons 7–8", benchmark="MA.8.GR.2.4", items=[
            dict(stem="Are the two triangles similar? Show the three ratios.", parts=[
                dict(label="a", stem="Sides 5, 7, 8 and sides 15, 21, 24", answer="Yes — 15/5 = 21/7 = 24/8 = 3.", why="one k for every side",
                     check=("many", ("eq", "F(15,5)", "3"), ("eq", "F(21,7)", "3"), ("eq", "F(24,8)", "3")), space=0.4),
                dict(label="b", stem="Sides 5, 8, 10 and sides 10, 16, 18", answer="No — 10/5 = 16/8 = 2, but 18/10 = 1.8.", why="two equal ratios are not enough",
                     check=("many", ("eq", "F(10,5)", "2"), ("eq", "F(16,8)", "2"), ("true", "F(18,10) != 2")), space=0.4)]),
            dict(stem="A triangle has sides 6, 10 and 12. A similar triangle's shortest side is 9. Find its other two sides.", answer="15 and 18", why="k = 9 ÷ 6 = 1.5",
                 check=("many", ("eq", "F(9,6)", "F(3,2)"), ("eq", "10*F(3,2)", "15"), ("eq", "12*F(3,2)", "18")), space=0.5),
            dict(stem="A triangle has sides 15, 20 and 30. A similar triangle's middle side is 8. Find its other two sides.", answer="6 and 12", why="k = 8 ÷ 20 = 0.4 — the copy is smaller",
                 check=("many", ("eq", "F(8,20)", "F(2,5)"), ("eq", "15*F(2,5)", "6"), ("eq", "30*F(2,5)", "12")), space=0.5),
            dict(stem="A 4-ft fence post casts a 3-ft shadow. At the same moment, a tree casts a 21-ft shadow. How tall is the tree?",
                 fig=shadow(4, 3, 28, 21, l=("4", "3", "h", "21"), unit="ft", what=("post", "tree"), inches=2.6),
                 answer="28 ft", why="k = 21 ÷ 3 = 7 from the shadows; 4 × 7", check=("eq", "4*F(21,3)", "28"), space=0.5),
            dict(stem="Kai's eyes are 5 ft above the ground. He stands 3 ft from a mirror on the ground and sees in it the top of a pole that stands 12 ft beyond the mirror. How tall is the pole?",
                 answer="20 ft", why="k = 12 ÷ 3 = 4; 5 × 4", check=("eq", "5*F(12,3)", "20"), space=0.5),
            dict(stem="Which triangle is similar to one with sides 6, 8 and 9?",
                 choices=["8, 10, 11", "12, 16, 20", "9, 12, 13.5", "6, 8, 12"], correct=2, answer="C", space=0.5,
                 errors={"A": "added 2 to every side [Source of Truth, GR.2.4: similar means multiplied, not added]",
                         "B": "checked two ratios, not three: 20 ÷ 9 is not 2 [6.07 Notes I: all three ratios]",
                         "D": "kept two sides the same [Source of Truth, GR.2.4: similar triangles assumed to have equal sides]"},
                 why="Every side × 1.5.",
                 check=("many", ("eq", "F(9,6)", "F(3,2)"), ("eq", "F(12,8)", "F(3,2)"), ("eq", "F(27,2)/9", "F(3,2)"),
                        ("true", "F(10,8) != F(8,6)"), ("true", "F(20,9) != 2"), ("true", "F(12,9) != 1"))),
        ]),
    ],

    # ------------------------------------------------------------------ the assessment: the practice test alone (ruling 49)
    assessment=dict(
        total=18,
        tracker_order=["MA.8.GR.1.3", "MA.8.GR.1.1", "MA.8.GR.1.2", "MA.8.GR.2.4"],
        tracker={"MA.8.GR.1.3": 3, "MA.8.GR.1.1": 6, "MA.8.GR.1.2": 6, "MA.8.GR.2.4": 3},
        follow_through="Follow-through (ruling 19).  A later part is correct when the right operation is applied to the student's own earlier value: question 7(b) from their own 7(a), question 10(b) from their own 10(a). Look at what they wrote for the earlier part, do this part's operation to it, and tick if that is what they wrote.",
        forms={"practice": _sections("practice")},
    ),
)
