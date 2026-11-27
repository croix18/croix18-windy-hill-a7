# A7 Unit 10 — Linear Relationships: Reference Sheet, Unit Review (home Tue 26 Jan with 10.09; A7 has no review day)
# and the assessment as THE PRACTICE TEST ALONE (ruling 49): the unit test is a random set of the practice page, so
# this paper is the test's blueprint — its sixteen questions in this order with these points are what the page
# generates with new numbers and what the master sheet maps. One period (ruling 51; Thu 28 Jan): 16 questions,
# 20 points, sections by benchmark in teaching order AR.3.1 · AR.3.2 · AR.3.4 · AR.3.5 · AR.3.3, tracker
# 3 · 5 · 3 · 5 · 4 — exactly the outline's "The test" (reviewed 27 Nov). No transfer items and no Form A/B.
#
# The unit's standing decisions hold on every page: rate of change, slope and y-intercept named once and used every
# day; proportional is the special case (y is 0 when x is 0); the slope formula in words first ("Subtract in the same
# order."); which quantity is x and which is y is said in every question; read the scales first; slope-intercept form
# only; F = 1.8C + 32 always printed; no line of fit and no comparison of two lines' slopes.
#
# Numbers: the practice paper's are the outline's own (its stories and relationships are reserved for it). The
# review uses its own — none of the paper's and none a lesson shows. The review's slopes: 6, 1.6, −7, 7/4, 18, 0.4,
# 1/3 (the four graphs), −0.75, −45, −5/2, 2.75 (as a wrong option only); its y-intercepts and starts: 11, 9, −8,
# 150, 2, 1, 75, 2.50, 32 (F = 1.8C + 32, the state's). The reference sheet works the lessons' own Notes examples (what the class saw).
#
# Every check is sympy over exact rationals: a slope is a difference quotient between consecutive pairs (slopes), a
# table is the equation's value at every x (line_of), and a wrong option is held to be NOT the key by its own "!="
# clause.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs10 as figs         # its own name: every unit's gates run in one process

BLANK = figs.BLANK


def _q(v):
    """A number as a sympy-ready exact string: F('27.20'), F(7,4), or an integer."""
    if isinstance(v, Fr):
        return f"F({v.numerator},{v.denominator})"
    return f"F('{v}')"


def slopes(xs, ys, m):
    """The change in y divided by the change in x is m between every two consecutive pairs."""
    return ("many",) + tuple(("eq", f"({_q(y1)} - {_q(y0)})/({_q(x1)} - {_q(x0)})", _q(m))
                             for x0, y0, x1, y1 in zip(xs, ys, xs[1:], ys[1:]))


def line_of(m, b, xs, ys):
    """Each y of a table is m times its x plus b (y = mx + b)."""
    return ("many",) + tuple(("eq", f"{_q(m)}*{_q(x)} + {_q(b)}", _q(y)) for x, y in zip(xs, ys))


def stack(specs, gap=2.6, titles=None, inches=4.6, pt=9.5):
    """Figures of figs10 set one above another as ONE picture (the kit prints one figure per item), each centred
    across, `gap` grid units apart — a table over its grid (question 9). `titles` (one per figure, or None) print
    above each. (Unit 7's helper, kept as it was.)"""
    sh, top = [], 0.0
    for k, s in enumerate(specs):
        x0, x1, y0, y1 = figs._extent(s["shapes"])
        if titles and titles[k]:
            sh.append(figs._t(0, top, titles[k], va="bottom", off=(0, 0.3)))
            top -= 1.6
        dx, dy = -(x0 + x1) / 2.0, top - y1
        for e in s["shapes"]:
            e = dict(e)
            if e["t"] == "seg":
                e["a"] = (e["a"][0] + dx, e["a"][1] + dy); e["b"] = (e["b"][0] + dx, e["b"][1] + dy)
            elif e["t"] == "circle":
                e["c"] = (e["c"][0] + dx, e["c"][1] + dy)
            elif e["t"] == "text":
                e["xy"] = (e["xy"][0] + dx, e["xy"][1] + dy)
            sh.append(e)
        top -= (y1 - y0) + gap
    return dict(kind="shapes", fs=22, pt=pt, **{"in": inches}, shapes=sh)


def match(rows, cols, rw=3.0, cw=5.4, rh=1.3, hh=5.2, fs=22, pt=9.5, inches=6.4):
    """FAST's matching grid with a meaning in each column head: one row per number (its words at the left), one
    column per meaning (its letter and words on top, on as many lines as it is given — a list of lines), an empty
    box in every cell for a student's mark. figs10's match_grid sets one line of words over a column; a meaning is
    three or four lines, so the head row here is `hh` tall."""
    sh = []
    n, m = len(rows), len(cols)
    W = rw + m * cw
    ys = [0.0, -hh] + [-hh - r * rh for r in range(1, n + 1)]
    for y in ys:
        sh.append(dict(t="seg", a=(0, y), b=(W, y)))
    bottom = ys[-1]
    for c in range(m + 1):
        x = 0 if c == 0 else rw + (c - 1) * cw
        sh.append(dict(t="seg", a=(x, 0), b=(x, bottom)))
    sh.append(dict(t="seg", a=(W, 0), b=(W, bottom)))
    for c, lines in enumerate(cols):
        sh.append(figs._t(rw + (c + 0.5) * cw, -hh / 2.0, "\n".join(lines)))
    for r, name in enumerate(rows):
        yc = -hh - (r + 0.5) * rh
        sh.append(figs._t(rw / 2.0, yc, name))
        for c in range(m):
            xc = rw + (c + 0.5) * cw
            q = 0.28
            for (a, b) in (((xc - q, yc - q), (xc + q, yc - q)), ((xc + q, yc - q), (xc + q, yc + q)),
                           ((xc + q, yc + q), (xc - q, yc + q)), ((xc - q, yc + q), (xc - q, yc - q))):
                sh.append(dict(t="seg", a=a, b=b))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


# ------------------------------------------------------------------ the practice paper's figures
Q1_FIG = figs.table([([2, 4, 6, 8], [7, 13, 19, 25])])

# question 3: four graphs, each on its own axes, the same scales on all four: dots on y = 1.5x (the key), the line
# y = x + 2, the curve y = x²/2 through (0, 0), (2, 2) and (4, 8), and dots on y = 2x + 2 (a constant rate, no ratio)
_g3 = dict(xstep=2, ystep=2)
Q3_FIG = figs.row([figs.plane((0, 6), (0, 10), points=[(2, 3, ""), (4, 6, ""), (6, 9, "")], **_g3),
                   figs.plane((0, 6), (0, 10), lines=[(1, 2, "")], **_g3),
                   figs.plane((0, 6), (0, 10), curves=[figs.square(Fr(1, 2), 4)], **_g3),
                   figs.plane((0, 6), (0, 10), points=[(1, 4, ""), (2, 6, ""), (3, 8, "")], **_g3)],
                  gap=3.6, titles=["A", "B", "C", "D"], inches=7.0)

Q5_FIG = figs.table([([-6, -2, 2, 10], [-7, -2, 3, 13])])

# question 6: the gallons axis counts by 40; the line from (0, 240) through (2, 160) and (5, 40), the two marked
# (a dot at (0, 240) is struck by the axis number 240, which reads the start)
Q6_FIG = figs.plane((0, 6), (0, 280), lines=[(-40, 240, "")], points=[(2, 160, "on"), (5, 40, "on")],
                    ys=40, xname="time in minutes", yname="water in gallons", inches=3.2)

# question 7: y = (2/3)x + 1 on a grid that runs to 10, one slope triangle 3 across and 2 up; a triangle 15 across
# would end at x = 18, past the grid
Q7_FIG = figs.plane((0, 10), (0, 10), lines=[(Fr(2, 3), 1, "")], points=[(0, 1, "")],
                    triangles=[figs.tri((3, 3), (6, 5))], inches=3.2)

# question 8: the grid, and the key's copy with y = −(3/4)x + 2 through (−4, 5), (0, 2) and (4, −1)
Q8_GRID, Q8_KEY = figs.pair((-6, 6), (-6, 6), lines=[(Fr(-3, 4), 2, "")],
                            points=[(-4, 5, ""), (0, 2, ""), (4, -1, "")], inches=3.4)

# question 9: the table to complete over the grid (hours 0 to 8, inches 0 to 12, both by 1); the key fills the table
# and draws the line from (0, 12) down to (8, 0), where the candle is gone
Q9_GRID, Q9_DRAWN = figs.pair((0, 8), (0, 12), lines=[(Fr(-3, 2), 12, "")],
                              points=[(2, 9, ""), (4, 6, ""), (6, 3, "")],
                              xname="time in hours", yname="height in inches", inches=3.2)
Q9_IN = 5.0
Q9_T = figs.table([([0, 2, 4, 6], [BLANK, BLANK, BLANK, BLANK])], head=("hours", "inches"), cw=1.6)
Q9_TK = figs.table([([0, 2, 4, 6], [12, 9, 6, 3])], head=("hours", "inches"), cw=1.6)
Q9_FIG = stack([Q9_T, Q9_GRID], inches=Q9_IN)
Q9_KEY = stack([Q9_TK, Q9_DRAWN], inches=Q9_IN)

Q10_FIG = match(["1.75", "9.50"],
                [["A", "the cost of", "a pizza with", "no toppings"], ["B", "the amount", "each topping", "adds to", "the cost"],
                 ["C", "the number", "of toppings", "on the pizza"], ["D", "the cost of", "a pizza with", "one topping"]])

Q11_FIG = figs.table([([2, 4, 7], [9, 14, "21.5"])], head=("years", "feet"))

Q13_FIG = figs.plane((-6, 6), (-6, 6), lines=[(Fr(5, 3), -4, "")], points=[(0, -4, "on"), (3, 1, "on")], inches=3.2)

Q14_FIG = figs.table([([2, 3, 5, 8], [6, 2, -6, -18])])


def _ar31():
    q1 = dict(stem="A table of a linear relationship is shown. What is y when x is 0? Is the relationship also proportional?",
              fig=Q1_FIG, answer="y is 1 when x is 0. No, the relationship is not proportional.",
              why="One point: both answers. The rate of change is 6 for every 2 units of x, which is 3 for every 1 unit. Go back 2 units from x = 2:  $7 - 2(3) = 1$.  y is 1, not 0, when x is 0, so the line does not pass through the origin.",
              check=("many", slopes([2, 4, 6, 8], [7, 13, 19, 25], 3), ("eq", "7 - 2*3", "1"), ("true", "7 - 2*3 != 0"),
                     line_of(3, 1, [2, 4, 6, 8], [7, 13, 19, 25])),
              space=0.8)
    q2 = dict(stem="Each equation or description shows a linear relationship between x and y. Select all that are also proportional.",
              choices=["$y = 3.5x$", "$y = x$", "$y = 6 + 2x$", "$y = -\\frac{1}{2}x$",
                       "The cost y, in dollars, of renting a van for x miles is \\$40 plus \\$0.30 for every mile."],
              correct=[0, 1, 3], answer="A, B, D", space=0.3,
              errors={"C": "the number added is written first: y is 6 when x is 0 [B1G-M, MA.8.AR.3.1: a number added taken for proportional]",
                      "E": "a start amount: 0 miles cost \\$40, so y is 40 when x is 0 [B1G-M, MA.8.AR.3.1: a start amount taken for proportional]"},
              why="One point for exactly A, B and D. A linear relationship is also proportional when y is 0 when x is 0. A: 3.5(0) = 0. B: the constant is 1. D: a constant can be negative, and −(1/2)(0) = 0. C adds 6 (6 + 2(0) = 6), and E starts at \\$40.",
              check=("many", ("eq", "F('3.5')*0", "0"), ("eq", "1*0", "0"), ("eq", "-F(1,2)*0", "0"),
                     ("true", "6 + 2*0 != 0"), ("true", "40 + F('0.30')*0 != 0")))
    q3 = dict(stem="Which graph shows a proportional relationship?", fig=Q3_FIG,
              choices=["Graph A", "Graph B", "Graph C", "Graph D"], correct=0, answer="A", space=0.3,
              errors={"B": "straight, but not through the origin: the line passes through (0, 2) [B1G-M, MA.8.AR.3.1: every straight line taken as proportional]",
                      "C": "through the origin, but not straight: the curve passes through (0, 0), (2, 2) and (4, 8) [B1G-M, MA.8.AR.3.1: through the origin taken as enough]",
                      "D": "a constant rate of change taken for a constant ratio: y goes up 2 each time, but 4 ÷ 1 = 4 and 6 ÷ 2 = 3 [B1G-M, MA.8.AR.3.1: a constant increase taken for proportional]"},
              why="A. Its points (2, 3), (4, 6) and (6, 9) lie on a straight line that reaches (0, 0): y ÷ x is 1.5 for every pair. B passes through (0, 2). C passes through the origin but is not straight. D goes up 2 for every 1 unit of x, but 4 ÷ 1 = 4 and 6 ÷ 2 = 3: its line would pass through (0, 2).",
              check=("many", ("eq", "F(3,2)*2", "3"), ("eq", "F(3,2)*4", "6"), ("eq", "F(3,2)*6", "9"), ("eq", "F(3,2)*0", "0"),
                     ("true", "1*0 + 2 != 0"),
                     ("eq", "F(1,2)*2**2", "2"), ("eq", "F(1,2)*4**2", "8"), ("true", "F(2 - 0, 2 - 0) != F(8 - 2, 4 - 2)"),
                     ("true", "F(4,1) != F(6,2)"), ("eq", "4 - 2*1", "2")))
    return [q1, q2, q3]


def _ar32():
    # repeat_ok: unit_repeats (rule D) matches only the digits 2, 4, 5, 7 against several lessons' Notes; no lesson shows these
    # two points or asks this slope.
    q4 = dict(repeat_ok=True, stem="A line passes through (−2, 7) and (4, −5). Find its slope.", answer="−2",
              why="Slope is the change in y divided by the change in x. Subtract in the same order:  $\\frac{-5 - 7}{4 - (-2)} = \\frac{-12}{6} = -2$.  The line falls from left to right, so its slope is negative.",
              check=("eq", "F(-5 - 7, 4 - (-2))", "-2"), space=0.8)
    q5 = dict(stem="A table of a linear relationship is shown. Find the slope.", fig=Q5_FIG,
              answer="5/4   (5/4 or 1.25)",
              why="The steps in x are not all the same, so divide each change in y by its change in x:  $\\frac{-2 - (-7)}{-2 - (-6)} = \\frac{5}{4}$,  $\\frac{3 - (-2)}{2 - (-2)} = \\frac{5}{4}$,  $\\frac{13 - 3}{10 - 2} = \\frac{10}{8} = \\frac{5}{4}$.  10 is the change in y alone.",
              check=("many", slopes([-6, -2, 2, 10], [-7, -2, 3, 13], Fr(5, 4)), ("eq", "F(5,4)", "F('1.25')")), space=0.8)
    q6 = dict(stem="Water drains from a tank at a constant rate. The graph shows the water in the tank, in gallons, versus the time, in minutes.",
              fig=Q6_FIG,
              parts=[dict(label="a", stem="Find the slope of the line.", answer="−40",
                          why="Read the scales first: the gallons axis counts by 40. From (2, 160) to (5, 40):  $\\frac{40 - 160}{5 - 2} = \\frac{-120}{3} = -40$.  (0, 240) and (2, 160) give the same slope. −1 counts squares; 40 drops the sign.",
                          check=("many", slopes([0, 2, 5], [240, 160, 40], -40)), space=0.6),
                     dict(label="b", stem="What does the slope tell you?",
                          choices=["How many gallons are added to the tank every minute", "How many gallons the tank loses every minute",
                                   "How many gallons the tank held at the start", "How many minutes the tank takes to lose 1 gallon"],
                          correct=1, answer="B",
                          errors={"A": "the sign ignored: the slope is negative, so the tank loses water [B1G-M, MA.8.AR.3.5: the sign of the slope ignored]",
                                  "C": "the slope read as the y-intercept: the tank held 240 gallons at the start [B1G-M, MA.8.AR.3.5: the slope and the y-intercept exchanged]",
                                  "D": "the ratio turned over: minutes per gallon is the change in x over the change in y [B1G-M, MA.8.AR.3.2: the change in x over the change in y]"},
                          why="B. The slope is a rate of change: its unit is the y-unit per x-unit, gallons per minute. −40 gallons per minute means the tank loses 40 gallons every minute.",
                          check=("many", ("eq", "-40*1", "-40"), ("true", "-40 < 0"), ("true", "-40 != 240"), ("true", "F(1,40) != 40")))])
    q7 = dict(stem="The graph shows a line with one slope triangle drawn on it. A larger slope triangle on the same line has a horizontal side of 15. How long is its vertical side?",
              fig=Q7_FIG, answer="10",
              why="Any two points on the line give the same slope:  $\\frac{2}{3} = \\frac{?}{15}$.  15 is 3 times 5, so the vertical side is 2(5) = 10. The larger triangle is past the edge of the grid.",
              check=("many", ("eq", "F(5 - 3, 6 - 3)", "F(2,3)"), ("eq", "F(2,3)*15", "10")), space=0.8)
    return [q4, q5, q6, q7]


def _ar34():
    q8 = dict(stem="Graph  $y = -\\frac{3}{4}x + 2$  on the grid.", fig=Q8_GRID, fig_key=Q8_KEY,
              answer="The line through (0, 2), (4, −1) and (−4, 5)",
              why="One point: a straight line through (0, 2) and (4, −1) that runs on past both points; arrows are not required. Start at the y-intercept, (0, 2), then move with the slope. A negative slope goes down as you move right: down 3 and right 4 to (4, −1). Check:  $-\\frac{3}{4}(-4) + 2 = 5$.",
              check=line_of(Fr(-3, 4), 2, [-4, 0, 4], [5, 2, -1]), space=0.2)
    # figwords_ok: 1.5 is the rate the student uses to fill the table; it is a rate, not a length on the grid
    q9 = dict(stem="A candle is 12 inches tall. It burns down 1.5 inches every hour.", fig=Q9_FIG, fig_key=Q9_KEY, figwords_ok=True,
              parts=[dict(label="a", stem="Complete the table.", answer="12, 9, 6, 3",
                          why="One point: all four. The start is 12 inches, and the height goes down 1.5 inches every hour: 12 − 1.5(2) = 9, 12 − 1.5(4) = 6, 12 − 1.5(6) = 3.",
                          check=line_of(Fr(-3, 2), 12, [0, 2, 4, 6], [12, 9, 6, 3]), space=0.2),
                     dict(label="b", stem="Graph the candle's height, in inches, versus the time, in hours, on the grid.",
                          answer="The line from (0, 12) through (2, 9), (4, 6) and (6, 3)",
                          why="One point: a straight line that starts at (0, 12) and passes through (2, 9), (4, 6) and (6, 3); it may end anywhere from (6, 3) to (8, 0). Points with no line through them do not earn the point, because time does not stop between the hours.",
                          check=("many", line_of(Fr(-3, 2), 12, [0, 2, 4, 6, 8], [12, 9, 6, 3, 0])), space=0.2)])
    return [q8, q9]


def _ar35():
    q10 = dict(stem="The equation  $c = 1.75t + 9.50$  gives the cost c, in dollars, of a pizza with t toppings. Match each number in the equation with its meaning. Mark one box in each row.",
               fig=Q10_FIG,
               parts=[dict(label="a", stem="1.75", answer="B, the amount each topping adds to the cost",
                           why="1.75 is the slope: the cost goes up \\$1.75 for every 1 topping.",
                           check=("eq", "(F('1.75')*2 + F('9.50')) - (F('1.75')*1 + F('9.50'))", "F('1.75')"), space=0.1),
                      dict(label="b", stem="9.50", answer="A, the cost of a pizza with no toppings",
                           why="9.50 is the y-intercept: the value of c when t is 0. D, \\$11.25 for one topping, is neither number.",
                           check=("many", ("eq", "F('1.75')*0 + F('9.50')", "F('9.50')"), ("eq", "F('1.75')*1 + F('9.50')", "F('11.25')"),
                                  ("true", "F('11.25') != F('9.50')"), ("true", "F('11.25') != F('1.75')")), space=0.1)])
    q11 = dict(stem="A tree grows at a constant rate. The table shows its height, in feet, in the years after it was planted.",
               fig=Q11_FIG,
               parts=[dict(label="a", stem="Find the slope, in feet per year.", answer="2.5",
                           why="$\\frac{14 - 9}{4 - 2} = \\frac{5}{2} = 2.5$  and  $\\frac{21.5 - 14}{7 - 4} = \\frac{7.5}{3} = 2.5$.  The steps in x are not the same, so divide by each change in x.",
                           check=slopes([2, 4, 7], [9, 14, "21.5"], "2.5"), space=0.6),
                      dict(label="b", stem="How tall was the tree when it was planted?", answer="4 feet",
                           why="The y-intercept is the value of y when x is 0. Go back 2 years from (2, 9):  $9 - 2(2.5) = 4$.  Or substitute a point and solve for b:  $9 = 2.5(2) + b$,  so  $b = 4$.",
                           check=("many", ("eq", "9 - 2*F('2.5')", "4"), line_of("2.5", 4, [2, 4, 7], [9, 14, "21.5"])), space=0.6)])
    # repeat_ok: F = 1.8C + 32 is the state's own formula (MA.8.AR.3.5, clarification 1), taught in 10.07+08, which asks about its 32
    # and its values; the paper alone asks what 1.8 means (the plan, "Reserved for the paper").
    q12 = dict(repeat_ok=True, stem="The equation  $F = 1.8C + 32$  gives the temperature F, in degrees Fahrenheit, for a temperature of C degrees Celsius. What does the slope, 1.8, mean?",
               choices=["The Fahrenheit temperature is 1.8 times the Celsius temperature.",
                        "A temperature of 0 degrees Celsius is 1.8 degrees Fahrenheit.",
                        "For every increase of 1 degree Celsius, the Fahrenheit temperature increases 1.8 degrees.",
                        "For every increase of 1 degree Fahrenheit, the Celsius temperature increases 1.8 degrees."],
               correct=2, answer="C", space=0.3,
               errors={"A": "read as proportional: 1.8(10) = 18, but 10 degrees Celsius is 50 degrees Fahrenheit [B1G-M, MA.8.AR.3.5: a linear relationship read as proportional]",
                       "B": "the slope read as the y-intercept: 0 degrees Celsius is 32 degrees Fahrenheit [B1G-M, MA.8.AR.3.5: the slope and the y-intercept exchanged]",
                       "D": "turned over: the slope is the change in F for every 1 unit of C [B1G-M, MA.8.AR.3.5: the rate read in the wrong order]"},
               why="C. The slope is the change in F for every 1 unit that C increases: 1.8(1) + 32 = 33.8, and 33.8 − 32 = 1.8. A reads it as proportional (10 °C is 50 °F, not 18 °F); B reads it as the y-intercept (0 °C is 32 °F); D turns it over.",
               check=("many", ("eq", "(F('1.8')*1 + 32) - (F('1.8')*0 + 32)", "F('1.8')"), ("true", "F('1.8')*10 + 32 != F('1.8')*10"),
                      ("eq", "F('1.8')*0 + 32", "32"), ("true", "F('1.8')*0 + 32 != F('1.8')"), ("true", "F(5,9) != F('1.8')")))
    return [q10, q11, q12]


def _ar33():
    q13 = dict(stem="The graph of a line is shown. Write the equation of the line in slope-intercept form.", fig=Q13_FIG,
               answer="$y = \\frac{5}{3}x - 4$",
               why="The y-intercept is −4: the line passes through (0, −4). The slope from (0, −4) to (3, 1):  $\\frac{1 - (-4)}{3 - 0} = \\frac{5}{3}$.  A rounded slope, 1.67, does not earn the point. Check:  $\\frac{5}{3}(3) - 4 = 1$.",
               check=("many", ("eq", "F(1 - (-4), 3 - 0)", "F(5,3)"), line_of(Fr(5, 3), -4, [0, 3], [-4, 1])), space=0.8)
    q14 = dict(stem="A table of a linear relationship is shown. Write its equation in slope-intercept form.", fig=Q14_FIG,
               answer="$y = -4x + 14$",
               why="The slope:  $\\frac{2 - 6}{3 - 2} = -4$,  and  $\\frac{-6 - 2}{5 - 3} = -4$.  Substitute a point and solve for b:  $6 = -4(2) + b$,  so  $b = 14$.  Check with (8, −18):  $-4(8) + 14 = -18$.",
               check=("many", slopes([2, 3, 5, 8], [6, 2, -6, -18], -4), line_of(-4, 14, [2, 3, 5, 8], [6, 2, -6, -18])), space=0.9)
    q15 = dict(stem="A line passes through the points (5, 1) and (10, 4). Write the equation of the line in slope-intercept form.",
               answer="$y = \\frac{3}{5}x - 2$   (y = 0.6x − 2 is the same answer)",
               why="The slope:  $\\frac{4 - 1}{10 - 5} = \\frac{3}{5}$.  Neither point is on the y-axis, so substitute a point and solve for b:  $1 = \\frac{3}{5}(5) + b$,  so  $b = -2$.  Check with (10, 4):  $\\frac{3}{5}(10) - 2 = 4$.",
               check=("many", ("eq", "F(4 - 1, 10 - 5)", "F(3,5)"), line_of(Fr(3, 5), -2, [5, 10], [1, 4]), ("eq", "F(3,5)", "F('0.6')")),
               space=0.9)
    q16 = dict(stem="Dana saves the same amount every week. She has \\$110 after 2 weeks and \\$185 after 5 weeks. Write an equation for the amount a, in dollars, that Dana has after w weeks.",
               answer="a = 25w + 60   (a = 60 + 25w is the same answer)",
               why="The rate is the slope:  $\\frac{185 - 110}{5 - 2} = \\frac{75}{3} = 25$  dollars per week. Substitute a point and solve for b:  $110 = 25(2) + b$,  so  $b = 60$.  The equation uses the question's letters, a and w. Check:  $25(5) + 60 = 185$.",
               check=("many", ("eq", "F(185 - 110, 5 - 2)", "25"), line_of(25, 60, [2, 5], [110, 185])), space=0.9)
    return [q13, q14, q15, q16]


def _sections(form="practice"):
    """The practice test, the only form (ruling 49): the blueprint of the unit test."""
    assert form == "practice", "ruling 49: Unit 10's assessment is the practice test alone"
    return [dict(title="Linear, and Also Proportional?", benchmark="MA.8.AR.3.1", items=_ar31()),
            dict(title="Slope", benchmark="MA.8.AR.3.2", items=_ar32()),
            dict(title="Graphing a Line", benchmark="MA.8.AR.3.4", items=_ar34()),
            dict(title="Slope and y-Intercept in Context", benchmark="MA.8.AR.3.5", items=_ar35()),
            dict(title="Writing the Equation of a Line", benchmark="MA.8.AR.3.3", items=_ar33())]


# ------------------------------------------------------------------ the review's figures
R1_FIG = figs.table([([3, 6, 9, 12], [29, 47, 65, 83])])

# four graphs, each on its own axes, the same scales: a falling line y = −0.75x + 9 (straight, not through the
# origin), the curve y = x²/9 through (0, 0), (3, 1), (6, 4) and (9, 9), dots on y = x/3 + 1 (a constant rate of
# change, no constant ratio), and dots on y = x/3, the key
_gR = dict(xstep=2, ystep=2)
R3_FIG = figs.row([figs.plane((0, 10), (0, 10), lines=[(Fr(-3, 4), 9, "")], **_gR),
                   figs.plane((0, 10), (0, 10), curves=[figs.square(Fr(1, 9), 9)], **_gR),
                   figs.plane((0, 10), (0, 10), points=[(3, 2, ""), (6, 3, ""), (9, 4, "")], **_gR),
                   figs.plane((0, 10), (0, 10), points=[(3, 1, ""), (6, 2, ""), (9, 3, "")], **_gR)],
                  gap=3.6, titles=["A", "B", "C", "D"], inches=7.0)

R5_FIG = figs.table([([-8, -4, 4, 16], [-22, -15, -1, 20])])

# a gift card: the dollars axis counts by 15; the line from (0, 150) (read on the axis) through (2, 60), down to the x-axis
R6_FIG = figs.plane((0, 4), (0, 165), lines=[(-45, 150, "")], points=[(2, 60, "on")], ys=15, ystep=2, aspect=0.4,
                    xname="time in weeks", yname="amount left in dollars", inches=3.0)

# y = 0.4x + 2, one slope triangle 5 across and 2 up; a triangle 18 up would be 45 across
R7_FIG = figs.plane((0, 12), (0, 8), lines=[(Fr(2, 5), 2, "")], points=[(0, 2, "")],
                    triangles=[figs.tri((5, 4), (10, 6))], inches=3.2)

R8_GRID, R8_KEY = figs.pair((-6, 6), (-6, 6), lines=[(Fr(-5, 2), 1, "")],
                            points=[(-2, 6, ""), (0, 1, ""), (2, -4, "")], inches=3.4)

# a drone 9 meters up that climbs 6 meters every second: seconds 0 to 6, meters 0 to 45 by 3
R9_GRID, R9_DRAWN = figs.pair((0, 6), (0, 45), lines=[(6, 9, "")],
                              points=[(1, 15, ""), (3, 27, ""), (5, 39, "")],
                              ys=3, ystep=3, aspect=0.6, xname="time in seconds", yname="height in meters", inches=3.2)
R9_IN = 5.6
R9_T = figs.table([([0, 1, 3, 5], [BLANK, BLANK, BLANK, BLANK])], head=("seconds", "meters"), cw=2.0)
R9_TK = figs.table([([0, 1, 3, 5], [9, 15, 27, 39])], head=("seconds", "meters"), cw=2.0)
R9_FIG = stack([R9_T, R9_GRID], inches=R9_IN)
R9_KEY = stack([R9_TK, R9_DRAWN], inches=R9_IN)

R10_FIG = match(["0.40", "2.50"],
                [["A", "the number", "of minutes", "of the ride"], ["B", "the cost", "before the", "first minute"],
                 ["C", "the cost of", "a 1-minute", "ride"], ["D", "the amount", "each minute", "adds to", "the cost"]])

R11_FIG = figs.table([([4, 6, 10], [122, 108, 80])], head=("minutes", "meters"))

R13_FIG = figs.plane((-2, 7), (-7, 10), lines=[(Fr(-5, 2), 9, "")], points=[(0, 9, "on"), (2, 4, "on")], inches=3.2)

R14_FIG = figs.table([([-5, 5, 10, 20], [3, 19, 27, 43])])

R_SSDD_FIG = figs.table([([4, 8, 12, 20], [8, 5, 2, -4])])


U = dict(
    unit=10, title="Linear Relationships",
    reference_intro="One thing on this page is printed on the Grade 8 FAST reference sheet: the slope formula (section 2). Everything else is tested from memory: linear and proportional, slope as a rate, y = mx + b, graphing a line, what the slope and the y-intercept mean, and writing the equation. F = 1.8C + 32 is printed whenever a question uses it. You may not use this sheet or the FAST reference sheet on the Unit 10 test.",

    reference=[
        dict(title="1.   Linear and Proportional", right="Lesson 1 · a constant rate of change",
             blocks=["**A linear relationship has a constant rate of change.**  The rate of change is the amount y changes for every 1 unit that x increases. When x is 0, 1, 2, 3 and y is 3, 5, 7, 9, y increases 2 for every 1 unit of x. The graph of a linear relationship is a straight line.",
                     "**It is also proportional when y is 0 when x is 0: its line passes through the origin.**  The lines $y = 2x$ and $y = 2x + 3$ both have the rate of change 2. The line $y = 2x$ passes through the origin, so it is proportional. The line $y = 2x + 3$ passes through (0, 3), so it is linear but not proportional.",
                     "**Two reasons are both right.**  Show that y is 0 when x is 0, or use Unit 7's test: y ÷ x is the same for every pair.",
                     "**When the table has no row for x = 0, step back to x = 0.**  For x: 2, 4, 6 and y: 9, 13, 17, the rate of change is 4 for every 2 units, which is 2 for every 1 unit. Go back 2 units from x = 2:  $9 - 2 - 2 = 5$.  y is 5 when x is 0, so the relationship is not proportional.",
                     "**A curve through the origin is not proportional.**  A proportional relationship is linear first: its graph is a straight line through the origin."]),
        dict(title="2.   Slope", right="Lessons 2–3 · rise over run",
             blocks=["**Slope is the change in y divided by the change in x: rise over run.**  The slope is the rate of change of a line. The rise is the vertical change and the run is the horizontal change. The letter for slope is m.",
                     "**Subtract in the same order.**  For the line through (1, 7) and (4, 1), the slope is  $\\frac{1 - 7}{4 - 1} = \\frac{-6}{3} = -2$.  Both differences start from the same point.",
                     "**The slope formula.**  For two points $(x_1, y_1)$ and $(x_2, y_2)$ on a line, the slope is  $m = \\frac{y_2 - y_1}{x_2 - x_1}$.  It says the same thing as the words: the change in y divided by the change in x.",
                     "**Any two points on the line give the same slope.**  On the line through (0, 1), (2, 2) and (6, 4), one slope triangle has a rise of 1 and a run of 2, and a larger one has a rise of 2 and a run of 4. The triangles are similar, so  $\\frac{1}{2} = \\frac{2}{4}$.",
                     dict(table=([2900, 2200, 4260], [
                         ["A line that", "has a slope that is", "for example"],
                         ["rises from left to right", "positive", "through (0, 1) and (2, 5): slope 2"],
                         ["falls from left to right", "negative", "through (1, 7) and (4, 1): slope −2"],
                         ["is horizontal", "0", "through (−3, 4) and (5, 4): slope 0"]])),
                     "**A table whose x-values do not go up by 1.**  For x: −3, 1, 9 and y: 2, 5, 11, divide each change in y by its own change in x:  $\\frac{5 - 2}{1 - (-3)} = \\frac{3}{4}$  and  $\\frac{11 - 5}{9 - 1} = \\frac{6}{8} = \\frac{3}{4}$.  The slope is 3/4. The change in y alone, 3 or 6, is not the slope."]),
        dict(title="3.   Slope as a Rate", right="Lesson 4 · units",
             blocks=["**The slope is a rate of change: its unit is the y-unit per x-unit.**  A climber is at 2,300 feet after 1 hour and at 2,900 feet after 3 hours:  $\\frac{2{,}900 - 2{,}300}{3 - 1} = 300$  feet per hour. The climber gains 300 feet every hour.",
                     "**Read the scales first.**  On a graph, find what one square stands for on each axis, then find the slope from the coordinates of two points, never by counting squares.",
                     "**A negative slope means the amount goes down.**  A phone's charge falls from 100 percent to 40 percent in 5 hours:  $\\frac{40 - 100}{5 - 0} = -12$  percent per hour. The phone loses 12 percent of its charge every hour.",
                     "**The slope is not always y ÷ x.**  Dividing one pair gives the rate only when the relationship is proportional. For the climber, 2,300 ÷ 1 is not the rate, because the climb did not start at 0 feet."]),
        dict(title="4.   Slope-Intercept Form", right="Lesson 5 · y = mx + b",
             blocks=["**In y = mx + b, m is the slope and b is the y-intercept.**  The y-intercept is the value of y when x is 0. It is where the line crosses the y-axis, so the line passes through (0, b). For $y = 2x + 3$, the slope is 2 and the y-intercept is 3.",
                     dict(table=([3120, 3120, 3120], [
                         ["The equation", "The slope, m", "The y-intercept, b"],
                         ["y = 3 + 2x", "2", "3: the same line as y = 2x + 3"],
                         ["y = 2x − 3", "2", "−3"],
                         ["y = −x + 4", "−1", "4"],
                         ["y = 5x", "5", "0: proportional"],
                         ["y = 4", "0", "4: a horizontal line"],
                         ["c = 20n + 35", "20", "35: a context's own letters"]])),
                     "**The y-intercept can be written first.**  In $y = 6 + \\frac{1}{2}x$, the slope is still the number that multiplies x, 1/2, and the y-intercept is 6."]),
        dict(title="5.   Graphing a Line", right="Lessons 5–6 · two methods",
             blocks=["**From y = mx + b: start at the y-intercept, then move with the slope.**  For $y = \\frac{3}{2}x - 2$, plot (0, −2). Move up 3 and right 2 to (2, 1), then again to (4, 4). The third point is the check: all three must lie on one straight line.",
                     "**A negative slope goes down as you move right.**  For $y = -\\frac{1}{3}x + 2$, start at (0, 2) and move down 1 and right 3 to (3, 1), then to (6, 0).",
                     "**From a table: plot the pairs, then draw the line through them.**  For x: −3, 0, 3, 6 and y: 4, 2, 0, −2, the line crosses the y-axis at 2 and goes down 2 for every 3 units to the right.",
                     "**From a description: the start is the y-intercept and the rate is the slope.**  A pool holds 200 gallons, and a hose adds 50 gallons every minute: plot (0, 200), (2, 300) and (4, 400). Choose scales that fit the numbers. A real-world graph starts at x = 0, and a quantity like time or distance is drawn as a line, not as a row of dots.",
                     "**An equation in another form: make a table of values.**  For $2x + y = 8$, y is 8 when x is 0, 4 when x is 2, and 0 when x is 4. Plot the three points and draw the line."]),
        dict(title="6.   Slope and y-Intercept in Context", right="Lessons 7–8 · one line at a time",
             blocks=["**The rate is the slope, and the start is the y-intercept.**  The equation $c = 45h + 60$ gives the cost c, in dollars, of a repair that takes h hours. The slope, 45, means that every hour adds \\$45. The y-intercept, 60, means that a repair of 0 hours costs \\$60, the charge for coming.",
                     "**Explain each one in a sentence with both units.**  \"The barrel gains 4.5 gallons every hour.\" \"The barrel held 12 gallons when the rain began.\"",
                     "**When no row shows x = 0, substitute a point and solve for b.**  Dog food left: 41 pounds after 3 weeks and 35 pounds after 5 weeks, so the slope is −3 pounds per week. Then  $41 = -3(3) + b$,  so  $b = 50$:  the bag held 50 pounds at the start.",
                     "**Temperature is linear, not proportional.**  The equation $F = 1.8C + 32$ is given whenever it is used. The slope, 1.8, means a rise of 1 degree Celsius is a rise of 1.8 degrees Fahrenheit. The y-intercept, 32, means 0 degrees Celsius is 32 degrees Fahrenheit. Since 10 °C is 50 °F and 20 °C is 68 °F, double the Celsius is not double the Fahrenheit."]),
        dict(title="7.   Writing the Equation", right="Lessons 9–10 · find m, then b",
             blocks=["**When b is shown, read it, then find m.**  A line passes through (0, 3) and (4, 1). The y-intercept is 3, and the slope is  $\\frac{1 - 3}{4 - 0} = -\\frac{1}{2}$,  so  $y = -\\frac{1}{2}x + 3$.  A table that shows x = 0 gives b the same way.",
                     "**When no y-intercept is in sight, substitute a point and solve for b.**  Through (2, 3) and (6, 11), the slope is  $\\frac{8}{4} = 2$,  so  $y = 2x + b$.  Then  $3 = 2(2) + b$,  so  $b = -1$  and  $y = 2x - 1$.  Check with the other point:  $2(6) - 1 = 11$.",
                     "**For a context, name the variables first.**  A gym charges a \\$35 sign-up fee and \\$20 every month. Let n be the number of months and c the total cost in dollars:  $c = 20n + 35$.  Use the question's own letters.",
                     "**An amount that goes down has a negative slope.**  A bus pass holds \\$40, and every ride costs \\$2.50. The amount a left after n rides is  $a = 40 - 2.5n$,  which is  $a = -2.5n + 40$  in slope-intercept form."]),
        dict(title="8.   Vocabulary",
             blocks=[dict(vocab=[
                 ("rate of change", "the amount y changes for every 1 unit that x increases; in a linear relationship it is constant"),
                 ("linear relationship", "a relationship with a constant rate of change; its graph is a straight line (IXL calls it a linear function)"),
                 ("proportional relationship", "a linear relationship in which y is 0 when x is 0: y = px, a line through the origin"),
                 ("slope", "the rate of change of a line: the change in y divided by the change in x between any two points on the line (rise over run); its letter is m"),
                 ("y-intercept", "the value of y where a line crosses the y-axis, which is the value of y when x is 0; the line passes through (0, b)"),
                 ("slope-intercept form", "y = mx + b, where m is the slope and b is the y-intercept")])]),
    ],

    # ------------------------------------------------------------------ unit review (unscored; home Tue 26 Jan)
    review=[
        dict(title="Linear, and Also Proportional?", lessons="Lesson 1", benchmark="MA.8.AR.3.1", items=[
            dict(stem="A table of a linear relationship is shown.", fig=R1_FIG,
                 parts=[dict(label="a", stem="What is y when x is 0?", answer="11",
                             why="The rate of change is 18 for every 3 units of x, which is 6 for every 1 unit. Go back 3 units from x = 3:  $29 - 3(6) = 11$.",
                             check=("many", slopes([3, 6, 9, 12], [29, 47, 65, 83], 6), ("eq", "29 - 3*6", "11")), space=0.5),
                        dict(label="b", stem="Is the relationship also proportional? Explain.",
                             answer="No, because y is 11 when x is 0.",
                             why="A linear relationship is also proportional only when y is 0 when x is 0. Or: 29 ÷ 3 is not 47 ÷ 6.",
                             check=("many", ("true", "29 - 3*6 != 0"), ("true", "F(29,3) != F(47,6)")), space=0.4)]),
            dict(stem="Each equation or description shows a linear relationship between x and y. Select all that are also proportional.",
                 choices=["$y = 9 + 1.6x$", "$y = -7x$", "$y = 2.75x - 8$", "$y = \\frac{7}{4}x$",
                          "The weight y, in pounds, of x boxes of tiles is 18 pounds for every box."],
                 correct=[1, 3, 4], answer="B, D, E", space=0.3,
                 errors={"A": "a number added, written first: y is 9 when x is 0 [B1G-M, MA.8.AR.3.1: a number added taken for proportional]",
                         "C": "a number subtracted: y is −8 when x is 0 [B1G-M, MA.8.AR.3.1: a number added taken for proportional]"},
                 why="B: −7(0) = 0; a constant can be negative. D: (7/4)(0) = 0. E: the weight is 18 times the boxes, with nothing added at the start. A is 9 when x is 0, and C is −8.",
                 check=("many", ("eq", "-7*0", "0"), ("eq", "F(7,4)*0", "0"), ("eq", "18*0", "0"),
                        ("true", "9 + F('1.6')*0 != 0"), ("true", "F('2.75')*0 - 8 != 0"))),
            dict(stem="Which graph shows a proportional relationship?", fig=R3_FIG,
                 choices=["Graph A", "Graph B", "Graph C", "Graph D"], correct=3, answer="D", space=0.3,
                 errors={"A": "straight, but not through the origin: the line passes through (0, 9) [B1G-M, MA.8.AR.3.1: every straight line taken as proportional]",
                         "B": "through the origin, but not straight: the curve passes through (3, 1), (6, 4) and (9, 9) [B1G-M, MA.8.AR.3.1: through the origin taken as enough]",
                         "C": "a constant rate of change taken for a constant ratio: y goes up 1 for every 3 units of x, but 2 ÷ 3 is not 3 ÷ 6 [B1G-M, MA.8.AR.3.1: a constant increase taken for proportional]"},
                 why="D. Its points (3, 1), (6, 2) and (9, 3) lie on a straight line that reaches (0, 0): y ÷ x is 1/3 for every pair. A passes through (0, 9); B is not straight; C's line would pass through (0, 1).",
                 check=("many", ("eq", "F(1,3)*3", "1"), ("eq", "F(1,3)*6", "2"), ("eq", "F(1,3)*9", "3"),
                        ("true", "-F(3,4)*0 + 9 != 0"), ("eq", "F(1,9)*6**2", "4"), ("true", "F(1 - 0, 3 - 0) != F(4 - 1, 6 - 3)"),
                        ("true", "F(2,3) != F(3,6)"), ("eq", "2 - F(1,3)*3", "1"))),
        ]),
        dict(title="Slope", lessons="Lessons 2–4", benchmark="MA.8.AR.3.2", items=[
            dict(stem="A line passes through (−3, −2) and (2, 6). Find its slope.", answer="8/5   (8/5 or 1.6)",
                 why="Subtract in the same order:  $\\frac{6 - (-2)}{2 - (-3)} = \\frac{8}{5}$.",
                 check=("many", ("eq", "F(6 - (-2), 2 - (-3))", "F(8,5)"), ("eq", "F(8,5)", "F('1.6')")), space=0.6),
            dict(stem="A table of a linear relationship is shown. Find the slope.", fig=R5_FIG, answer="7/4   (7/4 or 1.75)",
                 why="The steps in x are 4, 8 and 12:  $\\frac{-15 - (-22)}{-4 - (-8)} = \\frac{7}{4}$,  $\\frac{-1 - (-15)}{4 - (-4)} = \\frac{14}{8}$,  $\\frac{20 - (-1)}{16 - 4} = \\frac{21}{12}$,  and each is 7/4.",
                 check=("many", slopes([-8, -4, 4, 16], [-22, -15, -1, 20], Fr(7, 4)), ("eq", "F(7,4)", "F('1.75')")), space=0.6),
            dict(stem="Ana spends the same amount from a gift card every week. The graph shows the amount left on the card, in dollars, versus the time, in weeks.",
                 fig=R6_FIG,
                 parts=[dict(label="a", stem="Find the slope of the line, in dollars per week.", answer="−45",
                             why="Read the scales first: the dollars axis counts by 15. From (0, 150) to (2, 60):  $\\frac{60 - 150}{2 - 0} = -45$.",
                             check=slopes([0, 2], [150, 60], -45), space=0.5),
                        dict(label="b", stem="What does the slope tell you about the gift card?",
                             answer="Ana spends \\$45 from the card every week.",
                             why="The slope is a rate of change: −45 dollars per week. It is negative because the amount on the card goes down.",
                             check=("eq", "-45*1 + 150", "105"), space=0.4)]),
            dict(stem="The graph shows a line with one slope triangle drawn on it. A larger slope triangle on the same line has a vertical side of 18. How long is its horizontal side?",
                 fig=R7_FIG, answer="45",
                 why="Any two points on the line give the same slope:  $\\frac{2}{5} = \\frac{18}{?}$.  18 is 2 times 9, so the horizontal side is 5(9) = 45.",
                 check=("many", ("eq", "F(6 - 4, 10 - 5)", "F(2,5)"), ("eq", "18/F(2,5)", "45")), space=0.6),
        ]),
        dict(title="Graphing a Line", lessons="Lessons 5–6", benchmark="MA.8.AR.3.4", items=[
            dict(stem="Graph  $y = -\\frac{5}{2}x + 1$  on the grid.", fig=R8_GRID, fig_key=R8_KEY,
                 answer="The line through (0, 1), (2, −4) and (−2, 6)",
                 why="Start at the y-intercept, (0, 1), then move with the slope. A negative slope goes down as you move right: down 5 and right 2 to (2, −4). Check:  $-\\frac{5}{2}(-2) + 1 = 6$.",
                 check=line_of(Fr(-5, 2), 1, [-2, 0, 2], [6, 1, -4]), space=0.2),
            dict(stem="A drone is 9 meters above the ground. It climbs 6 meters every second.", fig=R9_FIG, fig_key=R9_KEY,
                 parts=[dict(label="a", stem="Complete the table.", answer="9, 15, 27, 39",
                             why="The start is 9 meters, and the rate is 6 meters per second: 9 + 6(1) = 15, 9 + 6(3) = 27, 9 + 6(5) = 39.",
                             check=line_of(6, 9, [0, 1, 3, 5], [9, 15, 27, 39]), space=0.2),
                        dict(label="b", stem="Graph the drone's height, in meters, versus the time, in seconds, on the grid.",
                             answer="The line from (0, 9) through (1, 15), (3, 27) and (5, 39)",
                             why="Read the scales first: the meters axis counts by 3. The start is the y-intercept and the rate is the slope. Time does not stop between the seconds, so draw a line, not a row of dots.",
                             check=line_of(6, 9, [0, 1, 3, 5, 6], [9, 15, 27, 39, 45]), space=0.2)]),
        ]),
        dict(title="Slope and y-Intercept in Context", lessons="Lessons 7–8", benchmark="MA.8.AR.3.5", items=[
            dict(stem="The equation  $c = 0.40m + 2.50$  gives the cost c, in dollars, of a scooter ride of m minutes. Match each number in the equation with its meaning. Mark one box in each row.",
                 fig=R10_FIG,
                 parts=[dict(label="a", stem="0.40", answer="D, the amount each minute adds to the cost",
                             why="0.40 is the slope: the cost goes up \\$0.40 for every 1 minute.",
                             check=("eq", "(F('0.40')*2 + F('2.50')) - (F('0.40')*1 + F('2.50'))", "F('0.40')"), space=0.1),
                        dict(label="b", stem="2.50", answer="B, the cost before the first minute",
                             why="2.50 is the y-intercept: the value of c when m is 0. C, \\$2.90 for a 1-minute ride, is neither number.",
                             check=("many", ("eq", "F('0.40')*0 + F('2.50')", "F('2.50')"), ("eq", "F('0.40')*1 + F('2.50')", "F('2.90')")), space=0.1)]),
            dict(stem="A submarine rises toward the surface at a constant rate. The table shows its depth below the surface, in meters, after different numbers of minutes.",
                 fig=R11_FIG,
                 parts=[dict(label="a", stem="Find the slope, in meters per minute.", answer="−7",
                             why="$\\frac{108 - 122}{6 - 4} = -7$  and  $\\frac{80 - 108}{10 - 6} = -7$.  The depth goes down 7 meters every minute.",
                             check=slopes([4, 6, 10], [122, 108, 80], -7), space=0.5),
                        dict(label="b", stem="How deep was the submarine when it began to rise?", answer="150 meters",
                             why="Substitute a point and solve for b:  $122 = -7(4) + b$,  so  $b = 150$.  Check with (10, 80):  $-7(10) + 150 = 80$.",
                             check=line_of(-7, 150, [4, 6, 10], [122, 108, 80]), space=0.5)]),
            # repeat_ok: the state's formula again, with a value (25) and a question (the 32) of the Review's own.
            dict(repeat_ok=True, stem="The equation  $F = 1.8C + 32$  gives the temperature F, in degrees Fahrenheit, for a temperature of C degrees Celsius.",
                 parts=[dict(label="a", stem="What is 25 degrees Celsius in degrees Fahrenheit?", answer="77 degrees Fahrenheit",
                             why="Substitute 25 for C:  $1.8(25) + 32 = 45 + 32 = 77$.",
                             check=("eq", "F('1.8')*25 + 32", "77"), space=0.5),
                        dict(label="b", stem="What does the 32 mean?", answer="A temperature of 0 degrees Celsius is 32 degrees Fahrenheit.",
                             why="32 is the y-intercept: the value of F when C is 0. That is why temperature is linear but not proportional.",
                             check=("eq", "F('1.8')*0 + 32", "32"), space=0.4)]),
        ]),
        dict(title="Writing Equations of Lines", lessons="Lesson 9", benchmark="MA.8.AR.3.3", items=[
            dict(stem="The graph of a line is shown. Write the equation of the line in slope-intercept form.", fig=R13_FIG,
                 answer="$y = -\\frac{5}{2}x + 9$   (or y = −2.5x + 9)",
                 why="The y-intercept is 9. The slope from (0, 9) to (2, 4):  $\\frac{4 - 9}{2 - 0} = -\\frac{5}{2}$.",
                 check=("many", ("eq", "F(4 - 9, 2 - 0)", "F(-5,2)"), line_of(Fr(-5, 2), 9, [0, 2], [9, 4])), space=0.6),
            dict(stem="A table of a linear relationship is shown. Write its equation in slope-intercept form.", fig=R14_FIG,
                 answer="y = 1.6x + 11   (or y = (8/5)x + 11)",
                 why="The slope:  $\\frac{19 - 3}{5 - (-5)} = \\frac{16}{10} = 1.6$.  Substitute a point and solve for b:  $19 = 1.6(5) + b$,  so  $b = 11$.  Check with (20, 43):  $1.6(20) + 11 = 43$.",
                 check=("many", slopes([-5, 5, 10, 20], [3, 19, 27, 43], "1.6"), line_of("1.6", 11, [-5, 5, 10, 20], [3, 19, 27, 43])), space=0.7),
            dict(stem="A line passes through (5, 40) and (10, 5). Write its equation in slope-intercept form.", answer="y = −7x + 75",
                 why="The slope:  $\\frac{5 - 40}{10 - 5} = -7$.  Substitute a point and solve for b:  $40 = -7(5) + b$,  so  $b = 75$.  Check:  $-7(10) + 75 = 5$.",
                 check=("many", ("eq", "F(5 - 40, 10 - 5)", "-7"), line_of(-7, 75, [5, 10], [40, 5])), space=0.7),
            # the SSDD block (§16 rule 3): ONE table asked four ways — the slope, y when x is 0, whether it is
            # proportional, and the equation. The name prints on the key only.
            dict(stem="A table of a linear relationship is shown. Answer each part.",
                 key_stem="**SSDD.**   A table of a linear relationship is shown. One table asked four ways: (a) the slope (10.02–10.03), (b) y when x is 0 (10.01), (c) whether it is proportional (10.01), (d) the equation (10.09). The student decides which kind each part is.",
                 fig=R_SSDD_FIG,
                 parts=[dict(label="a", stem="Find the slope.", answer="−0.75   (−0.75 or −3/4)",
                             why="$\\frac{5 - 8}{8 - 4} = -\\frac{3}{4}$,  $\\frac{2 - 5}{12 - 8} = -\\frac{3}{4}$  and  $\\frac{-4 - 2}{20 - 12} = -\\frac{6}{8} = -\\frac{3}{4}$.",
                             check=("many", slopes([4, 8, 12, 20], [8, 5, 2, -4], Fr(-3, 4)), ("eq", "F(-3,4)", "F('-0.75')")), space=0.5),
                        dict(label="b", stem="What is y when x is 0?", answer="11",
                             why="Go back 4 units from x = 4: y goes up 3, so  $8 + 3 = 11$.",
                             check=("eq", "8 - 4*F(-3,4)", "11"), space=0.4),
                        dict(label="c", stem="Is the relationship proportional? Explain.", answer="No, because y is 11 when x is 0.",
                             why="A linear relationship is also proportional only when y is 0 when x is 0. Or: 8 ÷ 4 = 2, but 5 ÷ 8 is not 2.",
                             check=("many", ("true", "8 - 4*F(-3,4) != 0"), ("true", "F(8,4) != F(5,8)")), space=0.4),
                        dict(label="d", stem="Write the equation of the line in slope-intercept form.", answer="y = −0.75x + 11   (or y = −(3/4)x + 11)",
                             why="The slope is −0.75 and the y-intercept is 11. Check with (20, −4):  $-0.75(20) + 11 = -4$.",
                             check=line_of(Fr(-3, 4), 11, [4, 8, 12, 20], [8, 5, 2, -4]), space=0.4)]),
        ]),
        dict(title="Writing Equations for Contexts", lessons="Lesson 10", benchmark="MA.8.AR.3.3", items=[
            dict(heading="This section is taught on Wednesday, 27 January, the day after this review goes home. Try it, and finish it after that lesson."),
            dict(stem="A tutoring center charges a sign-up fee and the same amount for every session. The cost of 4 sessions is \\$147, and the cost of 10 sessions is \\$255. Write an equation for the cost c, in dollars, of s sessions.",
                 answer="c = 18s + 75",
                 why="The rate is the slope:  $\\frac{255 - 147}{10 - 4} = \\frac{108}{6} = 18$  dollars per session. Substitute a point and solve for b:  $147 = 18(4) + b$,  so  $b = 75$:  the sign-up fee is \\$75. Check:  $18(10) + 75 = 255$.",
                 check=("many", ("eq", "F(255 - 147, 10 - 4)", "18"), line_of(18, 75, [4, 10], [147, 255])), space=0.8),
            dict(stem="A ferry leaves port with 75 gallons of fuel and uses 6 gallons every hour. Write an equation for the fuel f, in gallons, left after h hours.",
                 answer="f = −6h + 75   (f = 75 − 6h is the same answer)",
                 why="The start is the y-intercept, 75. An amount that goes down has a negative slope, −6. Check: after 2 hours,  $-6(2) + 75 = 63$  gallons are left.",
                 check=("eq", "-6*2 + 75", "63"), space=0.7),
        ]),
    ],

    # ------------------------------------------------------------------ the assessment: the practice test alone (ruling 49)
    assessment=dict(
        total=20,
        tracker_order=["MA.8.AR.3.1", "MA.8.AR.3.2", "MA.8.AR.3.4", "MA.8.AR.3.5", "MA.8.AR.3.3"],
        tracker={"MA.8.AR.3.1": 3, "MA.8.AR.3.2": 5, "MA.8.AR.3.4": 3, "MA.8.AR.3.5": 5, "MA.8.AR.3.3": 4},
        forms={"practice": _sections("practice")},
    ),
)
