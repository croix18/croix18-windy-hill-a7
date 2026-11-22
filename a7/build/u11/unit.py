# A7 Unit 11 — Solving Equations and Systems: Reference Sheet, Unit Review (home Thu 10 Dec with 11.08's independent
# set; ruling 27a — A7 has no review day) and the assessment as THE PRACTICE TEST ALONE (ruling 49, 22 October): the
# unit test is a random set of the practice page, so this paper is the test's blueprint — its fourteen questions in this
# order with these points are what the page generates with new numbers and what the master sheet maps. One period
# (ruling 51; Fri 11 Dec): 14 questions, 18 points, sections by benchmark in the order AR.2.1 · AR.4.1 · AR.4.2 · AR.4.3,
# weighted to the days (4 : ½ : ½ : 2) as the outline's "The test" sets them. No transfer items and no Form A/B.
#
# The unit's standing decisions (outline §"standing decisions") hold on every page: a line is graphed from a table of
# values and every system is given solved for y (Unit 11 is taught before Unit 10, ruling 52); no "slope" and no
# "y-intercept" on a student page — parallel is "the same number multiplying x"; no substitution and no elimination;
# the three endings x = a, a = a, a = b, and x = 0 is one solution; a decimal distributed has its own question (the 21%
# skill); every solution is checked in both sides, every system's solution in both equations; an approximate crossing
# is read to the nearest tenth with "about", and its key gives the exact value and the range it accepts (audit E15).
# Every answer on the practice paper is a number, an ordered pair, a letter, a set of letters or one of the three
# endings — a shape the practice page's generators can vary.
#
# Numbers: the practice paper, the review and the reference sheet's worked lines use their own — no equation, system or
# story of a lesson (ruling 43's spirit), checked against every string of l01–l08 before they were written. The book
# test's defects (audit E1, E6, E15, E16) are not reproduced: every key answers its own stem, no item rests on slope,
# the approximate item accepts a careful estimate, and no coefficient is a mixed number.
#
# Every check is sympy over the REAL numbers (the build's own letters are positive symbols): an equation is solved for a
# real u (solves), an ending is read from left − right (never / same), a pair is put into each equation (sat / fails), a
# crossing is the system's one solution (crosses), parallel lines share no point (never_meet), one line written two ways
# is one expression (one_line), and a table is checked value by value (table_of).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs11 as figs          # its own name: every unit's gates run in one process, and a second module called figs would be Unit 6's

BLUE, ORANGE = figs.BLUE, figs.ORANGE
X = "sp.Symbol('u', real=True)"
Y = "sp.Symbol('v', real=True)"


def _u(e):
    import re
    return re.sub(r"\bu\b", X, e)


def solves(left, right, value):
    """sympy solves left = right (in u) and finds exactly one solution, `value`."""
    return ("true", "sp.solve(sp.Eq(" + _u(left) + ", " + _u(right) + "), " + X + ") == [" + value + "]")


def same(e1, e2):
    """Two expressions in u are the same expression: as an equation, true for every number (infinitely many)."""
    return ("true", "sp.expand(" + _u(e1) + " - (" + _u(e2) + ")) == 0")


def never(left, right):
    """left = right is never true: left − right simplifies to a nonzero number (no solution)."""
    d = "sp.expand(" + _u(left) + " - (" + _u(right) + "))"
    return ("true", "(" + d + ").is_number and " + d + " != 0")


def sat(rhs, x, y):
    """(x, y) makes y = rhs true (rhs in u)."""
    return ("true", "sp.simplify((" + _u(rhs) + ").subs(" + X + ", " + x + ") - (" + y + ")) == 0")


def fails(rhs, x, y):
    """(x, y) makes y = rhs false."""
    return ("true", "sp.simplify((" + _u(rhs) + ").subs(" + X + ", " + x + ") - (" + y + ")) != 0")


def crosses(r1, r2, x, y):
    """The system y = r1, y = r2 has exactly one solution, (x, y)."""
    return ("true", "sp.solve([sp.Eq(" + Y + ", " + _u(r1) + "), sp.Eq(" + Y + ", " + _u(r2) + ")], [" + X + ", " + Y
            + "], dict=True) == [{" + X + ": " + x + ", " + Y + ": " + y + "}]")


def never_meet(r1, r2):
    """The system y = r1, y = r2 has no solution (parallel lines)."""
    return ("true", "sp.solve([sp.Eq(" + Y + ", " + _u(r1) + "), sp.Eq(" + Y + ", " + _u(r2) + ")], [" + X + ", " + Y
            + "], dict=True) == []")


def meets(r1, r2):
    """The system y = r1, y = r2 HAS a solution (one, or infinitely many) — a wrong 'no solution' option."""
    return ("true", "sp.solve([sp.Eq(" + Y + ", " + _u(r1) + "), sp.Eq(" + Y + ", " + _u(r2) + ")], [" + X + ", " + Y
            + "], dict=True) != []")


def one_line(r1, r2):
    """y = r1 and y = r2 are one line: r1 and r2 are the same expression (infinitely many solutions)."""
    return ("true", "sp.expand((" + _u(r1) + ") - (" + _u(r2) + ")) == 0")


def two_lines(r1, r2):
    """y = r1 and y = r2 are NOT one line."""
    return ("true", "sp.expand((" + _u(r1) + ") - (" + _u(r2) + ")) != 0")


def table_of(rhs, xs, ys):
    """Each y of a printed table is rhs at its x."""
    return ("many",) + tuple(sat(rhs, str(a), str(b)) for a, b in zip(xs, ys))


# ------------------------------------------------------------------ the practice paper's figures
# Papers draw `figs.plane(..., inches=)` and `figs.table` directly (figs.slide is for slides); each window is no bigger
# than its system needs, and every crossing the key names is given to `plane` as `solution=`.
Q10_FIG = figs.plane((-3, 2), (-6, 4), lines=[(3, 2), (-1, -2)], ys=2, solution=(-1, -1), inches=2.5)
Q11_FIG = figs.plane((-2, 2), (-10, 10), lines=[(4, 3), (4, -2)], ys=5, inches=2.3)
Q12_FIG = figs.plane((-1, 6), (-5, 3), lines=[(-1, 2), (Fr(1, 2), -4)], solution=(4, -2), inches=3.0)
Q13_FIG = figs.table([([0, 1, 2, 3, 4, 5], [-5, -3, "?", 1, 3, 5]), ([0, 1, 2, 3, 4, 5], [7, 6, 5, 4, 3, 2])],
                     titles=["y = 2x − 5", "y = −x + 7"], inches=6.0)
# question 14's two graphs are one picture (the kit prints one figure per item): the story's for part (a), with its
# names on its lines, and part (b)'s system, whose equations are set over it in the colours of their lines (solid,
# dashed) so that no label sits on the window a tenth is read from; its grid has a line every half, which also draws
# it at twice the story's scale. Critic 18 / barton 22 (15 Nov): each graph's caption names its part and its system,
# so part (b)'s graph cannot be read as Mia and Leo's.
Q14_FIG = figs.row([figs.plane((0, 8), (0, 60), lines=[(6, 10, "Mia"), (-4, 60, "Leo")], ys=10,
                               xname="weeks", yname="dollars", solution=(5, 40)),
                    figs.plane((0, 3), (0, 5), lines=[(1, 1, ""), (-2, 6, "")], xs=Fr(1, 2), ys=Fr(1, 2), step=2, solution=(Fr(5, 3), Fr(8, 3)))],
                   gap=4.0, titles=[["PART (a):  Mia and Leo"], ["PART (b):  a different system", ("y = x + 1   (solid)", BLUE), ("y = −2x + 6   (dashed)", ORANGE)]],
                   inches=6.3)


def _ar21():
    # FAST's house style on the paper (fast 9, 15 Nov): "An equation is shown." / the equation / "What value of n makes
    # the equation true?" — the kind, order and points of every question unchanged (the practice page is built from them)
    def shown(eq, v):
        return "An equation is shown.     " + eq + "     What value of " + v + " makes the equation true?"
    q1 = dict(stem=shown("$2(3n - 4) + 5n = 25$", "n"), answer="n = 3",
              why="Distribute: 6n − 8 + 5n = 25. Collect: 11n − 8 = 25. Add 8: 11n = 33. Divide by 11: n = 3. Check: 2(9 − 4) + 15 = 10 + 15 = 25. 6n − 4 + 5n (the 2 to one term only) gives 29/11; 6n − 8 = 25 (the 5n not collected) gives 5.5.",
              check=("many", solves("2*(3*u - 4) + 5*u", "25", "3"), same("2*(3*u - 4) + 5*u", "11*u - 8")), space=0.9)
    q2 = dict(stem=shown("$9h + 4 = 5h - 24$", "h"), answer="h = −7",
              why="Take 5h from both sides: 4h + 4 = −24. Subtract 4: 4h = −28. Divide by 4: h = −7. Check: 9(−7) + 4 = −59 and 5(−7) − 24 = −59. h = 7 lost the sign of −28; h = −5 added 4 instead of subtracting it (4h = −20).",
              check=solves("9*u + 4", "5*u - 24", "-7"), space=0.9)
    # question 3 (barton 10, fast 2): parentheses on both sides, one multiplier a negative fraction
    q3 = dict(stem=shown("$-\\frac{1}{2}(4m - 6) = 3(m - 4)$", "m"), answer="m = 3",
              why="The −½ multiplies both terms: −2m + 3. The 3 multiplies both: 3m − 12. So −2m + 3 = 3m − 12. Add 2m to both sides: 3 = 5m − 12. Add 12: 15 = 5m. Divide by 5: m = 3. Check: −½(12 − 6) = −3 and 3(3 − 4) = −3. −2m − 3 (the sign of (−½)(−6) lost) gives m = 1.8; −2m − 6 (the −½ to the 4m only) gives m = 1.2.",
              check=("many", solves("-F(1,2)*(4*u - 6)", "3*(u - 4)", "3"), same("-F(1,2)*(4*u - 6)", "-2*u + 3"), same("3*(u - 4)", "3*u - 12"),
                     solves("-2*u - 3", "3*u - 12", "F(9,5)"), solves("-2*u - 6", "3*u - 12", "F(6,5)")), space=0.9)
    # question 4 — the decimal distributed, the state's lowest-scoring released Grade 8 skill (standing decision 5); the
    # factor is negative now (fast 3 / barton 10), the state's own item shape
    q4 = dict(stem=shown("$-1.5(4v - 2) = v - 11$", "v"), answer="v = 2",
              why="The −1.5 multiplies both terms: −6v + 3 = v − 11. Take v from both sides: −7v + 3 = −11. Subtract 3: −7v = −14. Divide by −7: v = 2. Check: −1.5(8 − 2) = −9 and 2 − 11 = −9. −6v − 3 (the sign of (−1.5)(−2) lost) gives v = 8/7; −6v − 2 (the −1.5 to the 4v only — the state's most common miss) gives v = 9/7.",
              check=("many", solves("-F(3,2)*(4*u - 2)", "u - 11", "2"), same("-F(3,2)*(4*u - 2)", "-6*u + 3"),
                     solves("-6*u - 3", "u - 11", "F(8,7)"), solves("-6*u - 2", "u - 11", "F(9,7)")), space=0.9)
    # question 5 — one of each ending; (b) is x = 0, one solution (the guide's named misconception)
    q5 = dict(stem="Each equation has one solution, no solution or infinitely many solutions. Which? If it has one solution, find it.",
              parts=[dict(label="a", stem="$3(2x - 1) + 4 = 6x + 5$", answer="No solution",
                          why="6x − 3 + 4 = 6x + 5, so 6x + 1 = 6x + 5. Take 6x from both sides: 1 = 5 — never true: no solution.",
                          check=never("3*(2*u - 1) + 4", "6*u + 5"), space=0.7),
                     dict(label="b", stem="$6x + 5 = 5 - 3x$", answer="One solution, x = 0",
                          why="Add 3x to both sides: 9x + 5 = 5. Subtract 5: 9x = 0, so x = 0 — one solution. Check: 0 + 5 = 5 and 5 − 0 = 5. 'No solution' read x = 0 as nothing.",
                          check=solves("6*u + 5", "5 - 3*u", "0"), space=0.7),
                     dict(label="c", stem="$5x - 2(x + 3) = 3x - 6$", answer="Infinitely many solutions",
                          why="5x − 2x − 6 = 3x − 6, so 3x − 6 = 3x − 6. Take 3x from both sides: −6 = −6 — always true: infinitely many. 5x − 2x + 6 (the sign of (−2)(+3) lost) gives 6 = −6 and 'no solution'.",
                          check=("many", same("5*u - 2*(u + 3)", "3*u - 6"), never("5*u - 2*u + 6", "3*u - 6")), space=0.7)])
    q6 = dict(stem="Complete the equation so that it has no solution. What number goes in the box?     $2(4x + 3) - x = □x + 1$", answer="7",
              why="The left side is 8x + 6 − x = 7x + 6. With 7 in the box, 7x + 6 = 7x + 1 ends at 6 = 1 — never true. Any other number gives one solution (8 gives 7x + 6 = 8x + 1, so x = 5). 8 forgot the − x.",
              check=("many", same("2*(4*u + 3) - u", "7*u + 6"), never("2*(4*u + 3) - u", "7*u + 1"),
                     solves("2*(4*u + 3) - u", "8*u + 1", "5")), space=0.7)
    q7 = dict(stem="Storage company A charges a \\$35 move-in fee and \\$9 a month. Company B charges \\$14 a month and no fee. After how many months will the two companies have cost the same?",
              answer="7 months",
              why="35 + 9m = 14m. Take 9m from both sides: 35 = 5m. Divide by 5: m = 7. Check: 35 + 9(7) = 98 and 14(7) = 98 — both \\$98. 35 ÷ 14 = 2.5 ignores A's monthly price; 35 ÷ 9 ≈ 3.9 ignores B's.",
              check=("many", solves("35 + 9*u", "14*u", "7"), ("eq", "35 + 9*7", "98"), ("eq", "14*7", "98")), space=0.9)
    return [q1, q2, q3, q4, q5, q6, q7]


def _ar41():
    # question 8 (critic 12 = fast 4, 15 Nov): FAST's multiselect, which never says how many — five systems, two of
    # them right; each wrong system is true in exactly one of its equations (the named error: one is not enough)
    q8 = dict(stem="Select all the systems that have  $(3, -2)$  as a solution.",
              choices=["$y = x - 5$  and  $y = -2x + 4$", "$y = 2x - 8$  and  $y = x - 4$", "$y = -x + 1$  and  $y = 3x - 11$",
                       "$y = 4x - 14$  and  $y = -x + 2$", "$y = -2x + 3$  and  $y = x - 5$"], correct=[0, 2], answer="A, C", space=0.4,
              errors={"B": "true in y = 2x − 8 only: 3 − 4 = −1, not −2 [B1G-M, AR.4.1: a solution satisfies both]",
                      "D": "true in y = 4x − 14 only: −3 + 2 = −1, not −2 [B1G-M, AR.4.1: a solution satisfies both]",
                      "E": "true in y = x − 5 only: −2(3) + 3 = −3, not −2 [B1G-M, AR.4.1: a solution satisfies both]"},
              why="A: 3 − 5 = −2 and −2(3) + 4 = −2. C: −3 + 1 = −2 and 3(3) − 11 = −2. B, D and E each make one equation true and the other false — one is not enough.",
              check=("many", crosses("u - 5", "-2*u + 4", "3", "-2"), crosses("-u + 1", "3*u - 11", "3", "-2"),
                     sat("2*u - 8", "3", "-2"), fails("u - 4", "3", "-2"),
                     sat("4*u - 14", "3", "-2"), fails("-u + 2", "3", "-2"),
                     sat("u - 5", "3", "-2"), fails("-2*u + 3", "3", "-2")))
    q9 = dict(stem="Is $(4, -1)$ a solution of the system   $y = -x + 3$   and   $y = 2x - 7$?",
              choices=["Yes — it makes $y = -x + 3$ true.", "No — it makes $y = -x + 3$ false.",
                       "Yes — it makes both equations true.", "No — it makes $y = 2x - 7$ false."], correct=3, answer="D", space=0.4,
              errors={"A": "one equation checked, and one is not enough [B1G-M, AR.4.1: a solution satisfies both]",
                      "B": "−x with x = 4 taken as +4: 4 + 3 = 7 [B1G-M, AR.4.1: substitution errors]",
                      "C": "2(4) − 7 = 1, not −1 — the second equation checked carelessly [B1G-M, AR.4.1: substitution errors]"},
              why="−4 + 3 = −1 is true, but 2(4) − 7 = 1, not −1: the pair makes the second equation false, so it is not a solution. A stops at one equation; B loses the sign of −x; C misreads 1 as −1.",
              check=("many", sat("-u + 3", "4", "-1"), fails("2*u - 7", "4", "-1")))
    return [q8, q9]


def _ar42():
    q10 = dict(stem="The graphs of the system   $y = 3x + 2$   and   $y = -x - 2$   are shown. How many solutions does the system have?",
               fig=Q10_FIG, answer="One solution",
               why="The lines intersect once (at (−1, −1): 3(−1) + 2 = −1 and −(−1) − 2 = −1), so there is exactly one solution. The coefficients of x, 3 and −1, are different, so they must cross.",
               check=("many", crosses("3*u + 2", "-u - 2", "-1", "-1"), two_lines("3*u + 2", "-u - 2")), space=0.4)
    q11 = dict(stem="The graphs of the system   $y = 4x + 3$   and   $y = 4x - 2$   are shown. How many solutions does the system have?",
               fig=Q11_FIG, answer="No solution",
               why="The coefficient of x is 4 in both and the numbers added differ: the lines are parallel, always 5 apart, and never intersect. 'One' guessed that two lines must cross; 'infinitely many' read the shared 4x as one line.",
               check=("many", never_meet("4*u + 3", "4*u - 2"), two_lines("4*u + 3", "4*u - 2")), space=0.4)
    return [q10, q11]


def _ar43():
    q12 = dict(stem="A system of equations is graphed:   $y = -x + 2$   and   $y = \\frac{1}{2}x - 4$.   What is the solution of the system? Give its x and its y.",
               fig=Q12_FIG, answer="x = 4,  y = −2   — the point (4, −2)",
               why="The lines intersect at (4, −2): −4 + 2 = −2 and ½(4) − 4 = −2. (−2, 4) swaps the coordinates — it is on y = −x + 2 only; (0, 2) and (0, −4) are where one line meets the y-axis, on that line only.",
               check=("many", crosses("-u + 2", "F(1,2)*u - 4", "4", "-2"), sat("-u + 2", "-2", "4"), fails("F(1,2)*u - 4", "-2", "4"), fails("F(1,2)*u - 4", "0", "2")), space=0.4)
    q13 = dict(stem="The tables are for   $y = 2x - 5$   and   $y = -x + 7$.",
               fig=Q13_FIG,
               parts=[dict(label="a", stem="What number is missing from the table for $y = 2x - 5$?", answer="−1",
                           why="At x = 2: 2(2) − 5 = −1 (it sits between −3 and 1: each step of 1 in x adds 2 to y).",
                           check=sat("2*u - 5", "2", "-1"), space=0.4),
                      dict(label="b", stem="What is the solution of the system?", answer="(4, 3)",
                           why="At x = 4 both tables give 3: 2(4) − 5 = 3 and −4 + 7 = 3. (3, 4) swaps it. At x = 3 the two y's, 1 and 4, are close but not equal — near is not the same.",
                           check=("many", crosses("2*u - 5", "-u + 7", "4", "3"),
                                  table_of("2*u - 5", [0, 1, 3, 4, 5], [-5, -3, 1, 3, 5]),
                                  table_of("-u + 7", [0, 1, 2, 3, 4, 5], [7, 6, 5, 4, 3, 2])), space=0.4)])
    # question 14 — (a) a story's crossing said in its words; (b) a crossing between the grid lines, estimated (AR.4.3
    # Clar. 1). The key gives the exact crossing and the range it accepts (audit E15: the book keyed an exact pair and
    # took points off a correct estimate). Critic 1 = fast 1 (15 Nov): part (b)'s grid has a line every half, so the
    # range is within 0.1 of the keyed (1.7, 2.7) — x from 1.6 to 1.8, y from 2.6 to 2.8 — and holds no printed grid
    # point: (1.5, 2.5) and (2, 3), each on y = x + 1 only, are outside it. Stem in two sentences (fast 16).
    q14 = dict(stem="Mia has \\$10 and saves \\$6 each week. Leo has \\$60 and spends \\$4 each week.",
               fig=Q14_FIG,
               parts=[dict(label="a", stem="The PART (a) graph shows the dollars y each has after x weeks. After how many weeks will Mia and Leo have the same amount, and how much will each have?",
                           answer="After 5 weeks;  \\$40 each",
                           why="Mia's line y = 6x + 10 and Leo's y = −4x + 60 intersect at (5, 40): 6(5) + 10 = 40 and −4(5) + 60 = 40. (40, 5) swaps the coordinates.",
                           check=crosses("6*u + 10", "-4*u + 60", "5", "40"), space=0.5),
                      dict(label="b", stem="The PART (b) graph shows a different system,   $y = x + 1$   and   $y = -2x + 6$.   Estimate its point of intersection to the nearest tenth.",
                           answer="about (1.7, 2.7)",
                           why="Exactly (5/3, 8/3) = (1.666…, 2.666…). Accept a read within 0.1 of (1.7, 2.7): x from 1.6 to 1.8 and y from 2.6 to 2.8, such as (1.6, 2.7) or (1.7, 2.6). Check (1.7, 2.7): 1.7 + 1 = 2.7 and −2(1.7) + 6 = 2.6 — close. (1.5, 2.5) and (2, 3) are grid points on y = x + 1 only; (2.7, 1.7) swaps the coordinates.",
                           check=("many", crosses("u + 1", "-2*u + 6", "F(5,3)", "F(8,3)"),
                                  ("approx", "F(5,3)", "F(17,10)", "F(1,20)"), ("approx", "F(8,3)", "F(27,10)", "F(1,20)"),
                                  ("true", "F(8,5) <= F(5,3) <= F(9,5) and F(13,5) <= F(8,3) <= F(14,5)"),
                                  # no grid point (every half) inside the accepted box: the halves nearest are 1.5 and 2,
                                  # 2.5 and 3, all outside it
                                  ("true", "F(3,2) < F(8,5) and F(9,5) < 2 and F(5,2) < F(13,5) and F(14,5) < 3"),
                                  sat("u + 1", "F(3,2)", "F(5,2)"), fails("-2*u + 6", "F(3,2)", "F(5,2)"),
                                  sat("u + 1", "2", "3"), fails("-2*u + 6", "2", "3")), space=0.5)])
    return [q12, q13, q14]


def _sections(form="practice"):
    """The practice test, the only form (ruling 49): the blueprint of the unit test."""
    assert form == "practice", "ruling 49: Unit 11's assessment is the practice test alone"
    return [dict(title="Solving Equations", benchmark="MA.8.AR.2.1", items=_ar21()),
            dict(title="Solutions of a System", benchmark="MA.8.AR.4.1", items=_ar41()),
            dict(title="How Many Solutions a System Has", benchmark="MA.8.AR.4.2", items=_ar42()),
            dict(title="Solving Systems by Graphing", benchmark="MA.8.AR.4.3", items=_ar43())]


# ------------------------------------------------------------------ the review's figures
# the three pictures (cross once, parallel, the same line — the reference sheet's section 5, which the kit prints in words
# only), each a 4-by-7 window so that the three read as one set
R_THREE = figs.row([figs.plane((-3, 1), (-6, 8), lines=[(2, 4, ""), (2, -1, "")], ys=2),
                    figs.plane((-1, 3), (-1, 6), lines=[(1, 2, ""), (-3, 6, "")], solution=(1, 3)),
                    figs.plane((-1, 3), (-5, 2), lines=[(2, -3, "")])],
                   gap=3.4, titles=["a", "b", "c"], inches=6.2)
R_READ = figs.plane((-4, 1), (-2, 5), lines=[(1, 4), (-2, -2)], solution=(-2, 2), inches=2.6)
R_TABLES = figs.table([([0, 1, 2, 3, 4, 5], [-6, -3, 0, 3, 6, 9]), ([0, 1, 2, 3, 4, 5], [2, 3, 4, 5, 6, 7])],
                      titles=["y = 3x − 6", "y = x + 2"], inches=6.0)
R_GRID = figs.plane((-4, 2), (-5, 4), inches=3.0)
# its key's own figure (fig_key, 15 Nov — critic 2): both lines drawn on the same window, the crossing marked and named
R_GRID_KEY = figs.plane((-4, 2), (-5, 4), lines=[(1, 1), (-1, -3)], solution=(-2, -1), points=[(-2, -1, None, "r++")],
                        inches=3.0)
R_STORY = figs.plane((0, 10), (0, 50), lines=[(3, 20, "Ava"), (6, 5, "Ben")], ys=5, xname="weeks", yname="dollars",
                     solution=(5, 35), inches=3.0)
# the estimate cropped to its crossing and printed at 3 in (critic 6)
R_EST = figs.plane((0, 4), (-2, 3), lines=[(2, -2), (-1, 3)], solution=(Fr(5, 3), Fr(4, 3)), inches=3.0)
# fast 5: level lines — two of them (parallel, none) and one with a slanted line (one solution)
R_LEVEL = figs.row([figs.plane((-1, 4), (-3, 6), lines=[(0, 4, ""), (0, -1, "")]),
                    figs.plane((-4, 1), (-1, 6), lines=[(0, 3, ""), (-1, 1, "")], solution=(-2, 3))],
                   gap=3.4, titles=[[("y = 4", BLUE), ("y = −1", ORANGE), "a"], [("y = 3", BLUE), ("y = −x + 1", ORANGE), "b"]], inches=5.4)
# fast 9: FAST's matching grid, on the Review (the paper keeps its kinds)
R_MATCH = figs.match_grid(["a.   4(x + 3) = 4x + 12", "b.   6x − 1 = 6x + 4", "c.   8x + 5 = 3x + 5"],
                          ["one solution", "no solution", "infinitely many"], rw=7.8, cw=5.8, rh=1.4, pt=10, inches=6.6)


U = dict(
    unit=11, title="Solving Equations and Systems",
    review_note="HOW TO USE THIS.   This review covers every learning target of Lessons 1–8 — more than the test does. Work it in parts. If you miss two or more in a part, that part is where to spend your study time. The reference sheet has everything you need for each part.",
    reference_intro="Nothing in this unit is on the Grade 8 FAST reference sheet: the order of work for an equation, the three endings, what a solution of a system is and how to read one from a graph are all tested from memory. You may not use this sheet or the FAST reference sheet on the Unit 11 test.",

    reference=[
        dict(title="1.   Solving an Equation", right="Lessons 1–4 · distribute, collect, one side, isolate, check",
             blocks=[dict(bullets=[
                         "**Distribute.**  The number outside the parentheses multiplies EVERY term inside, and a minus sign in front is multiplied too: $15 - 2(x - 4) = 15 - 2x + 8$.",
                         "**Collect the like terms on each side.**  Like terms have the same letter to the same power: $6x$ and $-x$ are like terms, but $6x$ and $2$ are not.",
                         "**Take the same variable term from both sides.**  Either term can be taken. Taking the smaller one keeps the coefficient of x positive.",
                         "**Isolate x.**  What is left is a two-step equation: undo the number added, then divide both sides by the coefficient of x.",
                         "**Check in the FIRST equation.**  Substitute the solution into both sides. The two sides must give the same number."]),
                     dict(table=([4300, 5060], [
                         ["Each line", "What was done"],
                         ["$2(3x + 1) - x = 2x + 17$", "the equation"],
                         ["$6x + 2 - x = 2x + 17$", "distribute: 2 times 3x, 2 times 1"],
                         ["$5x + 2 = 2x + 17$", "collect: 6x − x = 5x"],
                         ["$3x + 2 = 17$", "take 2x from both sides"],
                         ["$3x = 15$", "subtract 2 from both sides"],
                         ["$x = 5$", "divide both sides by 3: x is isolated"],
                         ["$2(16) - 5 = 27$  and  $2(5) + 17 = 27$", "the check: 27 on both sides"]])),
                     "**A fraction or a decimal outside the parentheses multiplies every term too.**  The equation $0.4(5x + 15) = x + 12$ becomes $2x + 6 = x + 12$, so $x = 6$. The left side is not $2x + 15$, which multiplies only one term by the decimal.",
                     "**To clear fractions, multiply EVERY term on both sides by a common denominator.**  Multiply every term of $\\frac{x}{3} + 2 = \\frac{x}{2} - 1$ by 6 to get $2x + 12 = 3x - 6$. Take 2x from both sides, so $12 = x - 6$, and add 6 to both sides, so $x = 18$. Check: $6 + 2 = 8$ and $9 - 1 = 8$."]),
        dict(title="2.   One Solution, No Solution, Infinitely Many", right="Lessons 3–4 · read what is left",
             blocks=["**Simplify each side, take the same variable term from both sides, and read what is left.**",
                     dict(table=([2600, 2600, 4160], [
                         ["What is left", "The equation has", "Example"],
                         ["x = a number", "one solution", "$7x - 3 = 4x - 3$:  $3x = 0$, so $x = 0$"],
                         ["a = a, always true", "infinitely many solutions (every number works)", "$5(x - 1) = 5x - 5$:  $-5 = -5$"],
                         ["a = b, never true", "no solution (no number works)", "$5(x - 1) = 5x + 2$:  $-5 = 2$"]])),
                     "**A solution of 0 is one solution.**  Zero is a number, so $7x - 3 = 4x - 3$ has exactly one solution, x = 0. It does not have \"no solution.\"",
                     "**Read what is left. Do not test numbers.**  Five numbers that work do not show that every number works. Simplify both sides and read what is left.",
                     "**Compare the x-terms on the two sides.**  With different x-terms, the equation has one solution. With the same x-terms and the same constant, it has infinitely many solutions. With the same x-terms and different constants, it has no solution. The equation $4(x + 2) = 4x + □$ has infinitely many solutions with 8 in the box and no solution with any other number."]),
        dict(title="3.   Solutions of a System", right="Lessons 5–6 · both equations true",
             blocks=["**A system is two equations taken together. Its solution is an ordered pair (x, y) that makes BOTH equations true.**  For $y = x - 2$ and $y = -x + 8$, the pair $(5, 3)$ is a solution because $5 - 2 = 3$ and $-5 + 8 = 3$. The pair $(2, 0)$ is not a solution: $2 - 2 = 0$ is true, but $-2 + 8 = 6$, not 0. Making one equation true is not enough.",
                     "**An ordered pair gives x first, then y.**  The point $(3, 5)$ is different from the point $(5, 3)$.",
                     "**Test every pair, or every system, in both equations.**  If the two lines cross, exactly one pair makes both equations true. If the two equations graph as the same line, every pair on that line does. Do not stop at the first one that works."]),
        dict(title="4.   A Line from a Table of Values", right="Lessons 5–7 · x = 0 and two more",
             blocks=["**Make a table of values: x = 0 and two more values of x. Substitute each x to get its y.**  Plot the three points. Two points draw the line, and the third is a check: if it is off the line, a y-value is wrong. Every point on the line is a solution of the equation.",
                     dict(table=([3360, 2000, 2000, 2000], [
                         ["x", "0", "1", "2"],
                         ["$y = 3x - 4$", "−4", "−1", "2"]]), header=False),
                     "**When the coefficient of x is a half, choose even values of x. For thirds, choose multiples of 3.**  Then every y is a whole number, which is easy to plot.",
                     dict(table=([3360, 2000, 2000, 2000], [
                         ["x", "0", "2", "4"],
                         ["$y = \\frac{1}{2}x - 1$", "−1", "0", "1"]]), header=False)]),
        dict(title="5.   How Many Solutions a System Has", right="Lessons 5–6 · cross, parallel, the same line",
             blocks=[dict(table=([2000, 3300, 2000, 2060], [
                         ["The two lines", "The equations", "Solutions", "Example"],
                         ["intersect once", "different coefficients of x", "one: the point of intersection", "$y = x - 2$, $y = -x + 8$"],
                         ["parallel: never meet", "the same coefficient of x, different numbers added", "none", "$y = 3x + 1$, $y = 3x - 4$"],
                         ["the same line", "one equation written two ways", "infinitely many: every point of the line", "$y = 4(x - 1)$, $y = 4x - 4$"]])),
                     "**Parallel lines have the same steepness in the same direction, so they have the same coefficient of x.**  The coefficients ½ and 0.5 are the same number. The coefficients 2 and −2 are not, so $y = 2x + 1$ and $y = -2x + 1$ cross, at (0, 1). A horizontal line is a line too. The lines $y = 2$ and $y = -3$ both have 0 as the coefficient of x, so they are parallel, and $y = 2$ crosses $y = -x + 6$ once, at (4, 2).",
                     "**Two equations for the same line have infinitely many solutions, not one and not none.**  Write both equations the same way first: $4(x - 1)$ is $4x - 4$."]),
        dict(title="6.   Solving a System by Graphing", right="Lessons 7–8 · read the crossing, check it in both",
             blocks=["**Graph both lines. The solution is the point where they cross.**  Read x, then y, and check the pair in both equations. Two tables show the solution too: it is the column where both tables give the same y. The equations $y = x - 2$ and $y = -x + 8$ both give 3 at $x = 5$, so the solution is $(5, 3)$.",
                     "**In a story, explain what the point of intersection means, with its units.**  Club A costs $y = 8x + 15$ dollars and Club B costs $y = 11x$ dollars for x months. The lines cross at $(5, 55)$, so at 5 months both clubs cost \\$55. Each equation is the amount per 1, times x, plus the starting amount.",
                     "**Between the grid lines, estimate, and write \"about.\"**  Read each coordinate to the nearest tenth. Then check the estimate in both equations: the two values come out close, not equal. A good estimate is within 0.1 of each coordinate. The lines $y = x + 2$ and $y = -2x + 4$ cross at about $(0.7, 2.7)$, because $0.7 + 2 = 2.7$ and $-2(0.7) + 4 = 2.6$, which are close. (The exact solution is $x = \\frac{2}{3}$ and $y = \\frac{8}{3}$.) The nearest grid point, (1, 3), is on $y = x + 2$ only, so it is not a solution."]),
        dict(title="7.   Vocabulary",
             blocks=[dict(vocab=[
                 ("like terms", "terms with the same variable to the same power: $6x$ and $-x$"),
                 ("coefficient; constant", "the number that multiplies the variable (6 in $6x$; the coefficient of x in $y = -x + 4$ is −1); a term with no variable"),
                 ("distributive property", "$a(b + c) = ab + ac$ — the number outside multiplies every term inside"),
                 ("solution of an equation", "a number that makes the equation true"),
                 ("isolate; solve for", "to isolate a variable is to get it alone on one side of the equals sign; an equation solved for x has x isolated"),
                 ("no solution; infinitely many solutions", "never true, whatever the number (it ends at a = b); true for every number (it ends at a = a)"),
                 ("system of equations", "two equations about the same two variables, taken together"),
                 ("solution of a system", "an ordered pair (x, y) that makes both equations true; on a graph, where the lines cross"),
                 ("ordered pair", "(x, y): the x first, then the y"),
                 ("intersect; point of intersection", "cross; the point where two lines cross — on a graph, the solution of the system"),
                 ("parallel lines", "lines that never meet: the same coefficient of x and different numbers added"),
                 ("estimate", "a careful read between the grid lines, written with \"about\" and checked in both equations")])]),
    ],

    # ------------------------------------------------------------------ unit review (unscored; home Thu 10 Dec)
    review=[
        dict(letter="A", title="Solving Equations", lessons="Lessons 1–4", benchmark="MA.8.AR.2.1", items=[
            dict(stem="Solve for the variable. Check your solution in the first equation.", parts=[
                dict(label="a", stem="$6x - 2x + 7 = 31$", answer="x = 6", why="Collect: 4x + 7 = 31, so 4x = 24. Check: 36 − 12 + 7 = 31.",
                     check=solves("6*u - 2*u + 7", "31", "6"), space=0.5),
                dict(label="b", stem="$4(2n + 1) - 3n = 29$", answer="n = 5", why="8n + 4 − 3n = 29, so 5n + 4 = 29 and 5n = 25. Check: 4(11) − 15 = 29.",
                     check=solves("4*(2*u + 1) - 3*u", "29", "5"), space=0.5),
                dict(label="c", stem="$20 - 4(w - 3) = 8$", answer="w = 6", why="The −4 multiplies both terms: 20 − 4w + 12 = 8, so 32 − 4w = 8, −4w = −24. Check: 20 − 4(3) = 8.",
                     check=solves("20 - 4*(u - 3)", "8", "6"), space=0.5)]),
            dict(stem="Solve for the variable. Check your solution in both sides.", parts=[
                dict(label="a", stem="$8m - 5 = 3m + 20$", answer="m = 5", why="Take 3m from both sides: 5m − 5 = 20, so 5m = 25. Check: 35 and 35.",
                     check=solves("8*u - 5", "3*u + 20", "5"), space=0.5),
                dict(label="b", stem="$2h + 15 = 7h + 40$", answer="h = −5", why="Take 2h from both sides: 15 = 5h + 40, so 5h = −25. Check: 5 and 5.",
                     check=solves("2*u + 15", "7*u + 40", "-5"), space=0.5),
                dict(label="c", stem="$6(v - 1) = 2(v + 9)$", answer="v = 6", why="6v − 6 = 2v + 18, so 4v = 24. Check: 6(5) = 30 and 2(15) = 30.",
                     check=solves("6*(u - 1)", "2*(u + 9)", "6"), space=0.5)]),
            dict(stem="Solve for x.", parts=[
                dict(label="a", stem="$0.3(10x - 20) = x + 8$", answer="x = 7", why="The 0.3 multiplies both terms: 3x − 6 = x + 8, so 2x = 14. Check: 0.3(50) = 15 and 7 + 8 = 15.",
                     check=("many", solves("F(3,10)*(10*u - 20)", "u + 8", "7"), same("F(3,10)*(10*u - 20)", "3*u - 6")), space=0.5),
                dict(label="b", stem="$\\frac{1}{4}(8x + 12) = x + 9$", answer="x = 6", why="A quarter of 8x is 2x and a quarter of 12 is 3: 2x + 3 = x + 9. Check: ¼(60) = 15 and 6 + 9 = 15.",
                     check=solves("F(1,4)*(8*u + 12)", "u + 9", "6"), space=0.5),
                dict(label="c", stem="$\\frac{x}{4} + 3 = \\frac{x}{2} - 2$", answer="x = 20", why="Times 4, every term: x + 12 = 2x − 8, so x = 20. Check: 5 + 3 = 8 and 10 − 2 = 8.",
                     check=("many", solves("u/4 + 3", "u/2 - 2", "20"), same("4*(u/4 + 3)", "u + 12"), same("4*(u/2 - 2)", "2*u - 8")), space=0.5),
                dict(label="d", stem="$-0.4(5x - 10) = x + 2.5$", answer="x = 0.5", why="The −0.4 multiplies both terms: −2x + 4 = x + 2.5. Add 2x: 4 = 3x + 2.5. Subtract 2.5: 1.5 = 3x, so x = 0.5. Check: −0.4(2.5 − 10) = 3 and 0.5 + 2.5 = 3.",
                     check=("many", solves("-F(2,5)*(5*u - 10)", "u + F(5,2)", "F(1,2)"), same("-F(2,5)*(5*u - 10)", "-2*u + 4")), space=0.5),
                dict(label="e", stem="$-\\frac{3}{4}(4x - 8) = x + 1$", answer="x = 1.25", why="The −¾ multiplies both terms: −3x + 6 = x + 1. Add 3x: 6 = 4x + 1. Subtract 1: 5 = 4x, so x = 1.25. Check: −¾(5 − 8) = 2.25 and 1.25 + 1 = 2.25.",
                     check=("many", solves("-F(3,4)*(4*u - 8)", "u + 1", "F(5,4)"), same("-F(3,4)*(4*u - 8)", "-3*u + 6")), space=0.5)]),
            dict(stem="What number goes in the box so that   $5(x + 2) - x = 4x + □$   has infinitely many solutions?", answer="10",
                 why="The left side is 5x + 10 − x = 4x + 10, so the box is 10: 4x + 10 = 4x + 10 is true for every number. Any other number gives no solution.",
                 check=("many", same("5*(u + 2) - u", "4*u + 10"), never("5*(u + 2) - u", "4*u + 2")), space=0.5),
            dict(stem="A pottery studio has two plans. Plan A costs \\$45 to join and \\$8 a class. Plan B costs \\$13 a class. For how many classes do the two plans cost the same?",
                 answer="9 classes (both \\$117)", why="45 + 8c = 13c, so 45 = 5c and c = 9. Check: 45 + 72 = 117 and 13(9) = 117.",
                 check=("many", solves("45 + 8*u", "13*u", "9"), ("eq", "45 + 8*9", "117"), ("eq", "13*9", "117")), space=0.6),
            # FAST's matching grid (fast 9): the three endings, one box a row
            dict(stem="Each equation has one solution, no solution or infinitely many solutions. Mark one box in each row.", fig=R_MATCH,
                 parts=[dict(label="a", stem="$4(x + 3) = 4x + 12$", answer="Infinitely many solutions", why="4x + 12 = 4x + 12: take 4x from both sides, 12 = 12 — always true.",
                             check=same("4*(u + 3)", "4*u + 12"), space=0.2),
                        dict(label="b", stem="$6x - 1 = 6x + 4$", answer="No solution", why="Take 6x from both sides: −1 = 4 — never true.",
                             check=never("6*u - 1", "6*u + 4"), space=0.2),
                        dict(label="c", stem="$8x + 5 = 3x + 5$", answer="One solution (x = 0)", why="Take 3x from both sides: 5x + 5 = 5. Subtract 5: 5x = 0, so x = 0 — one solution.",
                             check=solves("8*u + 5", "3*u + 5", "0"), space=0.2)]),
            dict(stem="Solve each equation for x. If it has no solution or infinitely many solutions, write which.",
                 parts=[
                     dict(label="a", stem="$4(x - 2) = x + 7$", answer="x = 5", why="4x − 8 = x + 7, so 3x = 15. Check: 4(3) = 12 and 5 + 7 = 12.",
                          check=solves("4*(u - 2)", "u + 7", "5"), space=0.4),
                     dict(label="b", stem="$4(x - 2) = 6x + 2$", answer="x = −5", why="4x − 8 = 6x + 2, so −10 = 2x. Check: 4(−7) = −28 and −30 + 2 = −28.",
                          check=solves("4*(u - 2)", "6*u + 2", "-5"), space=0.4),
                     dict(label="c", stem="$4(x - 2) = 4x + 8$", answer="No solution", why="4x − 8 = 4x + 8; take 4x from both sides: −8 = 8 — never true.",
                          check=never("4*(u - 2)", "4*u + 8"), space=0.4),
                     dict(label="d", stem="$4(x - 2) = 4x - 8$", answer="Infinitely many solutions", why="4x − 8 = 4x − 8; take 4x from both sides: −8 = −8 — always true.",
                          check=same("4*(u - 2)", "4*u - 8"), space=0.4)]),
            # the SSDD block (HOUSE STYLE §16 rule 3: the end of Part A) — barton 8, 15 Nov: ONE context, FOUR different
            # structures (an equation, two expressions set equal, a pair tested in a system, a system with no solution),
            # so that a student must decide what kind of problem each part is. The name prints on the key only.
            dict(stem="Gym A costs \\$36 to join and \\$4 a visit. Gym B costs \\$10 a visit. Answer each part.",
                 key_stem="**SSDD.**   Gym A costs \\$36 to join and \\$4 a visit; Gym B costs \\$10 a visit. One story, four different structures: (a) one equation (11.01), (b) two plans set equal (11.02), (c) a pair tested in a system (11.05), (d) a system that never meets (11.03, 11.05) — the student decides which kind each part is.",
                 parts=[
                     dict(label="a", stem="Dana has paid Gym A \\$64 in all. How many visits has she made?", answer="7 visits",
                          why="36 + 4v = 64. Subtract 36: 4v = 28. Divide by 4: v = 7. Check: 36 + 28 = 64.",
                          check=solves("36 + 4*u", "64", "7"), space=0.5),
                     dict(label="b", stem="After how many visits have the two gyms cost the same?", answer="6 visits (both \\$60)",
                          why="36 + 4v = 10v. Take 4v from both sides: 36 = 6v, so v = 6. Check: 36 + 24 = 60 and 10(6) = 60.",
                          check=("many", solves("36 + 4*u", "10*u", "6"), ("eq", "36 + 4*6", "60")), space=0.5),
                     dict(label="c", stem="Is $(5, 56)$ a solution of the system  $y = 4x + 36$  and  $y = 10x$?", answer="No",
                          why="4(5) + 36 = 56 is true, but 10(5) = 50, not 56: one equation is not enough.",
                          check=("many", sat("4*u + 36", "5", "56"), fails("10*u", "5", "56")), space=0.5),
                     dict(label="d", stem="Gym C costs \\$50 to join and \\$4 a visit. Will Gym A and Gym C ever have cost the same? Explain.", answer="Never. Gym C always costs \\$14 more.",
                          why="36 + 4v = 50 + 4v; take 4v from both sides: 36 = 50 — never true. Both add \\$4 a visit, so the difference stays \\$14: parallel lines, no solution.",
                          check=("many", never("36 + 4*u", "50 + 4*u"), never_meet("4*u + 36", "4*u + 50")), space=0.5)]),
        ]),
        dict(letter="B", title="Solutions of a System", lessons="Lessons 5–6", benchmark="MA.8.AR.4.1", items=[
            dict(stem="Is the ordered pair a solution of the system? Show both checks.", parts=[
                dict(label="a", stem="$(3, 10)$;   $y = 3x + 1$  and  $y = x + 7$", answer="Yes", why="3(3) + 1 = 10 and 3 + 7 = 10: both true.",
                     check=("many", sat("3*u + 1", "3", "10"), sat("u + 7", "3", "10")), space=0.4),
                dict(label="b", stem="$(-2, 5)$;   $y = -2x + 1$  and  $y = x + 6$", answer="No", why="−2(−2) + 1 = 5 is true, but −2 + 6 = 4, not 5: one equation is not enough.",
                     check=("many", sat("-2*u + 1", "-2", "5"), fails("u + 6", "-2", "5")), space=0.4),
                dict(label="c", stem="$(8, 3)$;   $y = \\frac{1}{2}x - 1$  and  $y = -x + 11$", answer="Yes", why="½(8) − 1 = 3 and −8 + 11 = 3: both true.",
                     check=("many", sat("F(1,2)*u - 1", "8", "3"), sat("-u + 11", "8", "3")), space=0.4)]),
            # critic 12 = fast 4: the systems a pair solves, the count unsaid — three of five here
            dict(stem="Select all the systems that have  $(-1, 3)$  as a solution.",
                 choices=["$y = x + 4$  and  $y = -2x + 1$", "$y = -x + 2$  and  $y = 3x + 6$", "$y = 2x + 5$  and  $y = x + 3$",
                          "$y = -3x$  and  $y = x + 4$", "$y = 4x + 7$  and  $y = -x + 1$"], correct=[0, 1, 3], answer="A, B, D", space=0.4,
                 errors={"C": "true in y = 2x + 5 only: −1 + 3 = 2, not 3 [B1G-M, AR.4.1: a solution satisfies both]",
                         "E": "true in y = 4x + 7 only: −(−1) + 1 = 2, not 3 [B1G-M, AR.4.1: a solution satisfies both]"},
                 why="A: −1 + 4 = 3 and −2(−1) + 1 = 3. B: 1 + 2 = 3 and 3(−1) + 6 = 3. D: −3(−1) = 3 and −1 + 4 = 3. C and E each make one equation true only.",
                 check=("many", crosses("u + 4", "-2*u + 1", "-1", "3"), crosses("-u + 2", "3*u + 6", "-1", "3"), crosses("-3*u", "u + 4", "-1", "3"),
                        sat("2*u + 5", "-1", "3"), fails("u + 3", "-1", "3"), sat("4*u + 7", "-1", "3"), fails("-u + 1", "-1", "3"))),
            dict(stem="The ordered pair $(□, 9)$ is a solution of the system   $y = 2x + 3$   and   $y = 4x - 3$. What number goes in the box?", answer="3",
                 why="2x + 3 = 9 gives x = 3, and 4(3) − 3 = 9 as well: (3, 9) makes both true.",
                 check=("many", crosses("2*u + 3", "4*u - 3", "3", "9")), space=0.5),
        ]),
        dict(letter="C", title="How Many Solutions a System Has", lessons="Lessons 5–6", benchmark="MA.8.AR.4.2", items=[
            dict(stem="Each picture shows a system. How many solutions does each system have?",
                 fig=R_THREE, parts=[
                     dict(label="a", stem="$y = 2x + 4$ and $y = 2x - 1$", answer="No solution", why="Parallel: 2 multiplies x in both, so the lines never meet.",
                          check=never_meet("2*u + 4", "2*u - 1"), space=0.3),
                     dict(label="b", stem="$y = x + 2$ and $y = -3x + 6$", answer="One solution", why="The lines cross once, at (1, 3): 1 + 2 = 3 and −3 + 6 = 3.",
                          check=crosses("u + 2", "-3*u + 6", "1", "3"), space=0.3),
                     dict(label="c", stem="$y = 2(x - 2) + 1$ and $y = 2x - 3$ (both graph as the one line shown)", answer="Infinitely many solutions", why="2(x − 2) + 1 = 2x − 4 + 1 = 2x − 3: one line, and every point of it is a solution.",
                          check=one_line("2*(u - 2) + 1", "2*u - 3"), space=0.3)]),
            dict(stem="Which system has infinitely many solutions?",
                 choices=["$y = 3x + 6$  and  $y = 3x - 6$", "$y = 3x + 6$  and  $y = -3x + 6$", "$y = 3x + 6$  and  $y = 3(x + 2)$", "$y = 3x + 6$  and  $y = 6x + 3$"], correct=2, answer="C", space=0.3,
                 errors={"A": "the same number multiplying x read as the same line — the numbers added differ, so the lines are parallel: none [B1G-M, AR.4.2: the same-line case]",
                         "B": "3 and −3 taken as the same number multiplying x — the lines cross once, at (0, 6) [B1G-M, AR.4.3: plotting and graphing errors]",
                         "D": "the same two digits read as the same line — the lines cross once, at (1, 9) [B1G-M, AR.4.2: the same-line case]"},
                 why="3(x + 2) = 3x + 6: one equation written two ways, so every point of the line is a solution.",
                 check=("many", one_line("3*u + 6", "3*(u + 2)"), never_meet("3*u + 6", "3*u - 6"), crosses("3*u + 6", "-3*u + 6", "0", "6"), crosses("3*u + 6", "6*u + 3", "1", "9"))),
            dict(stem="Each picture shows a system with a horizontal line. How many solutions does each system have?", fig=R_LEVEL, parts=[
                     dict(label="a", stem="$y = 4$ and $y = -1$", answer="No solution", why="Two horizontal lines: 0 multiplies x in both and the numbers differ — parallel, they never meet.",
                          check=never_meet("4 + 0*u", "-1 + 0*u"), space=0.3),
                     dict(label="b", stem="$y = 3$ and $y = -x + 1$", answer="One solution, (−2, 3)", why="The lines intersect once, at (−2, 3): y = 3 there, and −(−2) + 1 = 3.",
                          check=crosses("3 + 0*u", "-u + 1", "-2", "3"), space=0.3)]),
            # FAST's dropdown sentence (fast 9), on the Review: choose one from each bracket
            dict(stem="Complete the sentence about the system  $y = -3x + 2$  and  $y = -3x - 4$.   The lines  [ intersect once  /  are parallel  /  are the same line ],  so the system has  [ one solution  /  no solution  /  infinitely many solutions ].",
                 answer="are parallel;  no solution", why="The coefficient of x is −3 in both and the numbers added differ: parallel lines never meet.",
                 check=never_meet("-3*u + 2", "-3*u - 4"), space=0.4),
            dict(stem="Without graphing, tell how many solutions the system   $y = 5x - 2$   and   $y = 5x + 1$   has. Explain how you know.", answer="No solution. The coefficient of x is 5 in both equations and the numbers added differ, so the lines are parallel.",
                 why="parallel lines never meet", check=never_meet("5*u - 2", "5*u + 1"), space=0.5),
        ]),
        dict(letter="D", title="Solving Systems by Graphing", lessons="Lessons 7–8", benchmark="MA.8.AR.4.3", items=[
            dict(stem="The system   $y = x + 4$   and   $y = -2x - 2$   is graphed. What is its solution?", fig=R_READ, answer="(−2, 2)",
                 why="The lines cross at (−2, 2): −2 + 4 = 2 and −2(−2) − 2 = 2.", check=crosses("u + 4", "-2*u - 2", "-2", "2"), space=0.4),
            dict(stem="The tables are for   $y = 3x - 6$   and   $y = x + 2$. What is the solution of the system?", fig=R_TABLES, answer="(4, 6)",
                 why="At x = 4 both tables give 6: 3(4) − 6 = 6 and 4 + 2 = 6.",
                 check=("many", crosses("3*u - 6", "u + 2", "4", "6"), table_of("3*u - 6", [0, 1, 2, 3, 4, 5], [-6, -3, 0, 3, 6, 9]),
                        table_of("u + 2", [0, 1, 2, 3, 4, 5], [2, 3, 4, 5, 6, 7])), space=0.4),
            dict(stem="Graph both lines on the grid and solve the system:   $y = x + 1$   and   $y = -x - 3$", fig=R_GRID, fig_key=R_GRID_KEY, answer="(−2, −1)",
                 why="Tables at x = 0, −1, −2: y = 1, 0, −1 and y = −3, −2, −1. Both give −1 at x = −2: −2 + 1 = −1 and 2 − 3 = −1.",
                 check=("many", crosses("u + 1", "-u - 3", "-2", "-1"), table_of("u + 1", [0, -1, -2], [1, 0, -1]), table_of("-u - 3", [0, -1, -2], [-3, -2, -1])), space=0.8),
            dict(stem="Ava has \\$20 and saves \\$3 a week. Ben has \\$5 and saves \\$6 a week. The graph shows the dollars y each has after x weeks. When will they have the same amount, and how much will each have?",
                 fig=R_STORY, answer="After 5 weeks, \\$35 each.", why="y = 3x + 20 and y = 6x + 5 cross at (5, 35): 3(5) + 20 = 35 and 6(5) + 5 = 35.",
                 check=crosses("3*u + 20", "6*u + 5", "5", "35"), space=0.5),
            dict(stem="The system   $y = 2x - 2$   and   $y = -x + 3$   is graphed. Estimate its point of intersection to the nearest tenth.", fig=R_EST, answer="about (1.7, 1.3)",
                 why="Exactly (5/3, 4/3). Accept a read within 0.1 of each: x from 1.6 to 1.8, y from 1.2 to 1.4. Check (1.7, 1.3): 2(1.7) − 2 = 1.4 and −1.7 + 3 = 1.3 — close. (2, 1) is a grid point on y = −x + 3 only.",
                 check=("many", crosses("2*u - 2", "-u + 3", "F(5,3)", "F(4,3)"), ("approx", "F(5,3)", "F(17,10)", "F(1,20)"), ("approx", "F(4,3)", "F(13,10)", "F(1,20)"),
                        ("true", "1 < F(8,5) and F(9,5) < 2 and 1 < F(6,5) and F(7,5) < 2"),
                        sat("-u + 3", "2", "1"), fails("2*u - 2", "2", "1")), space=0.4),
            dict(stem="Two plans cost the same for 5 months:   $y = 7x + 25$   and   $y = □x$. What number goes in the box?", answer="12",
                 why="7(5) + 25 = 60 at 5 months, so 5 times the box is 60 and the box is 12.", check=("many", ("eq", "F(7*5 + 25, 5)", "12"), crosses("7*u + 25", "12*u", "5", "60")), space=0.5),
        ]),
    ],

    # ------------------------------------------------------------------ the assessment: the practice test alone (ruling 49)
    assessment=dict(
        total=18,
        tracker_order=["MA.8.AR.2.1", "MA.8.AR.4.1", "MA.8.AR.4.2", "MA.8.AR.4.3"],
        tracker={"MA.8.AR.2.1": 9, "MA.8.AR.4.1": 2, "MA.8.AR.4.2": 2, "MA.8.AR.4.3": 5},
        follow_through="Follow-through (ruling 19).  No part of this paper is built on an earlier part's answer: 5(a)–(c), 13(a)–(b) and 14(a)–(b) are each scored on their own.",
        forms={"practice": _sections("practice")},
    ),
)
