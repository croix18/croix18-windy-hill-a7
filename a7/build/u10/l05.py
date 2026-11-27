# A7 10.05 Slope-Intercept Form and Graphing a Line (MA.8.AR.3.4) — Thu 21 Jan 2027.
# Built from the Unit 10 Lesson Outlines, section 10.05, and the unit's standing decisions; figures from u10/figs10.py.
# Whiteboards read; the Independent Set draws (decision 12): Your Turn 1 IS the handout's question 1, drawn in class.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs10 as figs
S = figs.slide
BL = figs.BLANK

X = "sp.Symbol('u', real=True)"
Y = "sp.Symbol('v', real=True)"


def _u(e):
    import re
    return re.sub(r"\bu\b", X, e)


def sat(rhs, x, y):
    """(x, y) makes y = rhs true (rhs in u)."""
    return ("true", "sp.simplify((" + _u(rhs) + ").subs(" + X + ", " + x + ") - (" + y + ")) == 0")


def fails(rhs, x, y):
    """(x, y) makes y = rhs false."""
    return ("true", "sp.simplify((" + _u(rhs) + ").subs(" + X + ", " + x + ") - (" + y + ")) != 0")


def table_of(rhs, xs, ys):
    """Each y of a printed table is rhs at its x."""
    return ("many",) + tuple(sat(rhs, str(a), str(b)) for a, b in zip(xs, ys))


def mb(rhs, m, b):
    """y = rhs has the slope m (the rate of change, its derivative) and the y-intercept b (its value at x = 0)."""
    return ("many", ("eq", "sp.diff(" + _u(rhs) + ", " + X + ")", m), ("eq", "(" + _u(rhs) + ").subs(" + X + ", 0)", b))


def slope_not(rhs, v):
    return ("true", "sp.simplify(sp.diff(" + _u(rhs) + ", " + X + ") - (" + v + ")) != 0")


def one_line(r1, r2):
    """y = r1 and y = r2 are one line."""
    return ("true", "sp.expand((" + _u(r1) + ") - (" + _u(r2) + ")) == 0")


def two_lines(r1, r2):
    return ("true", "sp.expand((" + _u(r1) + ") - (" + _u(r2) + ")) != 0")


H = Fr(1, 2)

# ---- the notes
NOTES2 = S(figs.plane((-2, 6), (-3, 5), lines=[(Fr(3, 2), -2, "")],
                      points=[(0, -2, ""), (2, 1, ""), (4, 4, "")],
                      triangles=[figs.tri((0, -2), (2, 1)), figs.tri((2, 1), (4, 4))], inches=4.0, pt=17),
           inches=4.0, pt=17, reserve=1.6)
NOTES3 = S(figs.row([figs.plane((-1, 4), (-1, 6), lines=[(-2, 5, "")],
                                points=[(0, 5, ""), (1, 3, ""), (2, 1, "")],
                                triangles=[figs.tri((0, 5), (1, 3))]),
                     figs.plane((-1, 7), (-2, 4), lines=[(Fr(-1, 3), 2, "")],
                                points=[(0, 2, ""), (3, 1, ""), (6, 0, "")],
                                triangles=[figs.tri((0, 2), (3, 1))])],
                    gap=1.8, titles=["y = −2x + 5", "y = −(1/3)x + 2"]), inches=8.4, pt=16, reserve=1.2)

# ---- the examples: an empty grid on the question slide; the line drawn beside the worked rows
EXW = dict(inches=4.2, pt=18)
EX1 = S(figs.plane((-2, 6), (-4, 3), **EXW), inches=4.2, pt=18, reserve=0.9)
EX1W = S(figs.plane((-2, 6), (-4, 3), lines=[(H, -2, "")], points=[(0, -2, "on", "dr"), (2, -1, "on", "dr"), (4, 0, "on", "ul")],
                    **EXW), inches=4.2, pt=18, reserve=0.9)
# Your Turn 1 = the handout's question 1 (decision 12): the same window as the handout's grid
YT1 = S(figs.plane((-1, 7), (-4, 6), **EXW), inches=4.2, pt=18, reserve=0.9)
YT1A = S(figs.plane((-1, 7), (-4, 6), lines=[(Fr(4, 3), -3, "")],
                    points=[(0, -3, "on", "r"), (3, 1, "on", "r"), (6, 5, "on", "r")], **EXW), inches=4.2, pt=18, reserve=0.95)
EX2 = S(figs.plane((-1, 6), (-3, 6), **EXW), inches=4.2, pt=18, reserve=0.9)
EX2W = S(figs.plane((-1, 6), (-3, 6), lines=[(Fr(-3, 2), 5, "")],
                    points=[(0, 5, "on", "r"), (2, 2, "on", "r"), (4, -1, "on", "r")], **EXW), inches=3.4, pt=18, reserve=0.9)
YT2 = S(figs.plane((-1, 7), (-5, 7), ystep=2, **EXW), inches=4.2, pt=18, reserve=0.9)
YT2A = S(figs.plane((-1, 7), (-5, 7), ystep=2, lines=[(Fr(-5, 3), 6, "")],
                    points=[(0, 6, "on", "r"), (3, 1, "on", "r"), (6, -4, "on", "r")], **EXW), inches=4.2, pt=18, reserve=0.95)

# ---- board 5: four graphs on one window (−4 to 6, numbered every 2), lettered A–D in this order (keyed A)
g2 = dict(inches=2.6, pt=18, step=2)
B5_LINES = [(2, -3), (2, 3), (Fr(1, 2), -3), (-3, 2)]
C5 = S(figs.choices4([figs.plane((-4, 6), (-4, 6), lines=[(m, b, "")], **g2) for m, b in B5_LINES], gap=3.2),
       inches=14.0, pt=18, reserve=0.75)
C5A = S(figs.row([figs.plane((-4, 6), (-4, 6), lines=[(2, -3, "")], points=[(0, -3, "on", "l"), (2, 1, "on", "r")],
                             inches=4.2, pt=18, step=2)], titles=["A"], inches=4.2, pt=18),
        inches=4.2, pt=18, reserve=1.3)


# ---- the handout: empty grids, the key's graph on the same window
def PAIR(xr, yr, m, b, pts):
    return figs.pair(xr, yr, lines=[(m, b, "")], points=[(a, c, "") for a, c in pts], inches=3.2)


IS1_G, IS1_K = PAIR((-1, 7), (-4, 6), Fr(4, 3), -3, [(0, -3), (3, 1), (6, 5)])
IS2_G, IS2_K = PAIR((-3, 4), (-4, 6), -2, 3, [(0, 3), (1, 1), (2, -1)])
IS3_G, IS3_K = PAIR((-2, 8), (-1, 6), Fr(-1, 2), 4, [(0, 4), (2, 3), (4, 2)])
IS4_G, IS4_K = PAIR((-3, 3), (-7, 7), 3, 0, [(0, 0), (1, 3), (2, 6)])

BK5_G, BK5_K = PAIR((-2, 6), (-2, 5), H, 1, [(0, 1), (2, 2), (4, 3)])
BK6_G, BK6_K = PAIR((-1, 7), (-7, 5), Fr(-5, 3), 4, [(0, 4), (3, -1), (6, -6)])
BK7_G, BK7_K = PAIR((-1, 6), (-5, 4), Fr(3, 2), -4, [(0, -4), (2, -1), (4, 2)])
AD5_G, AD5_K = PAIR((-2, 6), (-5, 2), H, -3, [(0, -3), (2, -2), (4, -1)])
AD6_G, AD6_K = PAIR((-1, 7), (-6, 6), Fr(-5, 3), 5, [(0, 5), (3, 0), (6, -5)])
AD7_G, AD7_K = PAIR((-1, 6), (-3, 6), Fr(3, 2), -1, [(0, -1), (2, 2), (4, 5)])


def TAB(xs, ys):
    return figs.table([(xs, ys)], head=("x", "y"))


L = dict(
    code="10.05", unit=10, lesson_no=5,
    title="Slope-Intercept Form and Graphing a Line",
    unit_title="Linear Relationships",
    benchmark="MA.8.AR.3.4",
    benchmark_text="Given a mathematical or real-world context, graph a two-variable linear equation from a written description, a table or an equation in slope-intercept form.",
    target="I can name the slope and the y-intercept of y = mx + b and use them to graph the line.",
    essential="How do the two numbers in y = mx + b tell you where a line starts and which way it goes?",
    building_on="In lessons 10.02+03 and 10.04, students found the slope of a line from a graph, a table and two points, and in context. In Unit 11, they graphed a line from a table of values and called the number that multiplies x the coefficient of x.",
    working_toward="Lesson 10.06 graphs a line from a table and from a context, and lessons 10.07+08 interpret the slope and the y-intercept. In lesson 10.09, students write the equation of a line in slope-intercept form.",
    vocab=[("y-intercept", "the value of y where a line crosses the y-axis: the value of y when x is 0"),
           ("slope-intercept form", "y = mx + b, where m is the slope and b is the y-intercept")],
    ixl=["Slope-intercept form: find the slope and y-intercept — U55", "Graph a line using slope — FSV",
         "Graph a line from an equation in slope-intercept form — W5E", "Write a linear equation from a slope and y-intercept — WHP",
         "Compare linear functions: tables, graphs, and equations — N7D"],
    closure="Whiteboard question 9 is answered in writing and serves as the exit ticket. A complete answer says that Ava exchanged the rise and the run: a slope of 2/5 is up 2 and right 5, so from (0, 1) she should reach (5, 3). An answer that gives only the point has the result without naming the mistake.",

    mtr=[("MTR.2.1", "Every line today is seen as an equation, a starting point with a slope, and a graph."),
         ("MTR.4.1", "On whiteboard questions 3 and 5, students convince a neighbor and then vote again."),
         ("MTR.6.1", "Students plot a third point on every line as a check that the three points lie on one straight line.")],
    hoq=[("Why is the y-intercept always the point (0, b)?", "DOK 1"),
         ("In y = 5 − (3/2)x, which number is the slope, and how do you know?", "DOK 2"),
         ("Why does a third point catch a mistake that two points cannot?", "DOK 2"),
         ("Ava moved up 5 and right 2 for a slope of 2/5. How could she have caught her mistake from the equation alone?", "DOK 3")],
    differentiation=[
        ("ESE / 504", "Provide a card that reads \"b: start on the y-axis. m: rise over run, up for a positive rise and down for a negative one.\" Keep Notes II on display from whiteboard question 1 onward, and give each student a ruler."),
        ("ELL", "**Slope**: how steep, rise over run. **y-intercept**: where the line crosses the y-axis. **Rise**: up or down. **Run**: right. **Check**: a third point on the same line."),
        ("Enrichment", "After whiteboard question 8, ask for the equation of a line with slope −1/3 that passes through (6, 1). (Substitute the point and solve for b: 1 = −2 + b, so b = 3 and y = −(1/3)x + 3.)")],

    warmup=[
        dict(stem="A pool holds 200 gallons after 4 minutes and 320 gallons after 10 minutes. Find the rate of change in gallons per minute.",
             answer="20 gallons per minute",
             check=("eq", "sp.Rational(320 - 200, 10 - 4)", "20")),
        dict(stem="A linear table has the x-values 3, 6, 9 and the y-values 14, 26, 38. What is y when x is 0?",
             answer="2",
             check=("many", ("eq", "sp.Rational(26 - 14, 6 - 3)", "4"), ("eq", "sp.Rational(38 - 26, 9 - 6)", "4"),
                    ("eq", "14 - 4*3", "2"))),
        dict(stem="For $y = \\frac{3}{4}x$, find y when x is 0, 4 and 8.", answer="0, 3, 6",
             check=table_of("F(3,4)*u", [0, 4, 8], [0, 3, 6])),
        dict(stem="For $y = -2x + 5$, find y when x is 0, 1 and 2.", answer="5, 3, 1",
             check=table_of("-2*u + 5", [0, 1, 2], [5, 3, 1])),
    ],

    notes=[
        dict(numeral="I", head="y = mx + b: m is the slope and b is the y-intercept", min=3,
             items2=["$y = 2x + 3$:  x = 0, 1, 2 give y = 3, 5, 7.", "It crosses the y-axis at 3 and goes up 2 for every 1 unit of x.",
                     "$y = 3 + 2x$:  the same line     $y = 2x - 3$:  b is −3     $y = -x + 4$:  m is −1",
                     "$y = 5x$:  b is 0, proportional     $y = 4$:  m is 0"],
             letters=False),
        dict(numeral="II", head="To graph: start at the y-intercept, then move with the slope", min=3,
             fig=NOTES2,
             items2=["$y = \\frac{3}{2}x - 2$:  plot (0, −2), then up 3 and right 2 to (2, 1).",
                     "Again to (4, 4):  the third point is the check."],
             letters=False),
        dict(numeral="III", head="A negative slope goes down as you move right", min=3,
             fig=NOTES3,
             items2=["$y = -2x + 5$:  from (0, 5), down 2 and right 1 to (1, 3), then (2, 1).",
                     "$y = -\\frac{1}{3}x + 2$:  from (0, 2), down 1 and right 3 to (3, 1), then (6, 0)."],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=2,
             prompt=["$y = \\frac{1}{2}x - 2$"], fig=EX1, ask="Graph the line.",
             worked=[dict(min=2,
                          rows=[("b = -2:\\quad (0, -2)", "start at the y-intercept"),
                                ("m = \\frac{1}{2}:\\quad (2, -1)", "up 1 and right 2"),
                                ("(4, 0)", "again: the third point is the check")],
                          fig=EX1W, answer="Through (0, −2), (2, −1) and (4, 0)")],
             check=("many", mb("F(1,2)*u - 2", "F(1,2)", "-2"), table_of("F(1,2)*u - 2", [0, 2, 4], [-2, -1, 0])),
             # decision 12: this Your Turn IS the Independent Set's question 1 — hand the set out now; every student
             # draws question 1 on its grid while the teacher circulates.
             your_turn=dict(min=5,
                            prompt=["Handout, question 1:  Graph  $y = \\frac{4}{3}x - 3$."], fig=YT1, fig_a=YT1A, ask="",
                            steps=["Start:   $b = -3$,  the point $(0, -3)$",
                                   "Move:   up 4 and right 3 to $(3, 1)$",
                                   "Check:   again to $(6, 5)$"],
                            answer="Through (0, −3), (3, 1) and (6, 5)"),
             yt_check=("many", mb("F(4,3)*u - 3", "F(4,3)", "-3"), table_of("F(4,3)*u - 3", [0, 3, 6], [-3, 1, 5]))),
        dict(title="Example 2", min_q=1,
             prompt=["$y = 5 - \\frac{3}{2}x$"], fig=EX2, ask="Graph the line.",
             worked=[dict(min=2,
                          rows=[("b = 5:\\quad (0, 5)", "the y-intercept, written first"),
                                ("m = -\\frac{3}{2}:\\quad (2, 2)", "down 3 and right 2"),
                                ("(4, -1)", "again: the third point is the check")],
                          fig=EX2W, answer="Through (0, 5), (2, 2) and (4, −1)")],
             check=("many", mb("5 - F(3,2)*u", "-F(3,2)", "5"), table_of("5 - F(3,2)*u", [0, 2, 4], [5, 2, -1])),
             your_turn=dict(min=2,
                            prompt=["Graph  $y = 6 - \\frac{5}{3}x$."], fig=YT2, fig_a=YT2A, ask="",
                            steps=["Start:   $b = 6$,  the point $(0, 6)$",
                                   "Move:   down 5 and right 3 to $(3, 1)$",
                                   "Check:   again to $(6, -4)$"],
                            answer="Through (0, 6), (3, 1) and (6, −4)"),
             yt_check=("many", mb("6 - F(5,3)*u", "-F(5,3)", "6"), table_of("6 - F(5,3)*u", [0, 3, 6], [6, 1, -4]))),
    ],

    # The round: name m and b (1), the same with b first (2); a vote on a statement about y = 6 + (1/2)x (3); move with
    # the slope from a y-intercept, a negative slope (4); a vote on four graphs (5); the pattern breaks — write the
    # equation from m and b (6); Kai, his room number the extra number (7); backwards (8); Ava's exchanged rise and run,
    # written (9).
    whiteboard=[
        # repeat_ok: rule D matches only small digits that the notes' and examples' lines also carry (a coincidence
        # of values); this equation, its givens and its answer appear nowhere above.
        dict(repeat_ok=True, text=["**What are the slope and the y-intercept of y = 4x − 7?"],
             steps=["Slope:   the coefficient of x,  $m = 4$", "y-intercept:   at $x = 0$,  $4(0) - 7 = -7$"],
             answer="The slope is 4 and the y-intercept is −7.",
             check=mb("4*u - 7", "4", "-7"),
             wrong="slope 4, y-intercept 7 — the sign of b dropped [B1G-M, AR.3.4: swapping m and b]; slope −7, y-intercept 4 — the two numbers exchanged [B1G-M, AR.3.4: swapping m and b]"),
        # repeat_ok: the one change from question 1 is the order (y = −7 + 4x is 4x − 7 written with b first) — the
        # point of the board, as the plan sets it.
        dict(repeat_ok=True, text=["**What are the slope and the y-intercept of y = −7 + 4x?"],
             steps=["Slope:   the number with x,  $m = 4$", "y-intercept:   at $x = 0$,  $-7 + 4(0) = -7$"],
             answer="The slope is 4 and the y-intercept is −7.",
             check=("many", mb("-7 + 4*u", "4", "-7"), one_line("-7 + 4*u", "4*u - 7")),
             wrong="slope −7, y-intercept 4 — the first number taken as the slope [B1G-M, AR.3.4: swapping m and b]"),
        dict(kind="mc", text=["**Which statement describes the line $y = 6 + \\frac{1}{2}x$?"],
             qtext="Which statement describes the line y = 6 + (1/2)x?",
             steps=["Slope:   $\\frac{1}{2}$", "At $x = 0$:   $y = 6$"],
             choices=["Slope 6, y-intercept $(0, \\frac{1}{2})$", "Slope $\\frac{1}{2}$, y-intercept (0, 6)", "Slope 2, y-intercept (0, 6)", "Slope $\\frac{1}{2}$, y-intercept (6, 0)"],
             correct=1, answer="B — Slope 1/2, y-intercept (0, 6)",
             errors={"A": "the first number taken as the slope [B1G-M, AR.3.4: swapping m and b]", "C": "the fraction turned over [B1G-M, AR.3.4: inverting rise and run]", "D": "the intercept put on the x-axis [B1G-M, GR.1.2: x and y inverted]"},
             check=("many", mb("6 + F(1,2)*u", "F(1,2)", "6"), sat("6 + F(1,2)*u", "0", "6"),
                    slope_not("6 + F(1,2)*u", "6"), fails("6 + F(1,2)*u", "0", "F(1,2)"),
                    slope_not("6 + F(1,2)*u", "2"), fails("6 + F(1,2)*u", "6", "0"))),
        # repeat_ok: rule D matches only small digits that the notes' and examples' lines also carry (a coincidence
        # of values); this equation, its givens and its answer appear nowhere above.
        dict(repeat_ok=True, text=["A line has the y-intercept 2 and the slope −3.",
                   "**Start at the y-intercept and move with the slope twice. Which two points do you reach?"],
             steps=["Start:   $(0, 2)$", "Once:   down 3 and right 1 to $(1, -1)$", "Twice:   down 3 and right 1 to $(2, -4)$"],
             answer="(1, −1) and (2, −4)",
             check=("many", sat("-3*u + 2", "1", "-1"), sat("-3*u + 2", "2", "-4")),
             wrong="(1, 5) and (2, 8) — up 3, the sign of the slope dropped [Notes III: a negative slope goes down as you move right]; (3, 1) and (6, 0) — right 3 and down 1, rise and run exchanged [B1G-M, AR.3.4: inverting rise and run]"),
        # repeat_ok: rule D matches only the grid's axis numbers (−4 to 6, numbered every 2); this line appears
        # nowhere above.
        dict(repeat_ok=True, kind="mc", text=["**Which graph shows y = 2x − 3?"],
             qtext="Four graphs, each on its own grid from −4 to 6 on both axes, numbered every 2. Which graph shows y = 2x − 3?",
             fig=C5, fig_a=C5A,
             steps=["Start:   $b = -3$,  the point $(0, -3)$", "Move:   up 2 and right 1, twice, to $(2, 1)$"],
             choices=["A", "B", "C", "D"], correct=0, answer="A",
             errors={"B": "the sign of b dropped: through (0, 3) and (1, 5) [B1G-M, AR.3.4: swapping m and b]", "C": "rise and run exchanged, slope 1/2: through (0, −3) and (2, −2) [B1G-M, AR.3.4: inverting rise and run]", "D": "the slope and the y-intercept exchanged, y = −3x + 2: through (0, 2) and (1, −1) [B1G-M, AR.3.4: swapping m and b]"},
             check=("many", sat("2*u - 3", "0", "-3"), sat("2*u - 3", "2", "1"),
                    sat("2*u + 3", "0", "3"), sat("2*u + 3", "1", "5"), fails("2*u - 3", "0", "3"),
                    sat("F(1,2)*u - 3", "2", "-2"), fails("2*u - 3", "2", "-2"),
                    sat("-3*u + 2", "0", "2"), sat("-3*u + 2", "1", "-1"), fails("2*u - 3", "0", "2"))),
        # repeat_ok: rule D matches only small digits that the notes' and examples' lines also carry (a coincidence
        # of values); this equation, its givens and its answer appear nowhere above.
        dict(repeat_ok=True, text=["A line has the slope −5 and the y-intercept 2.", "**Write its equation."],
             steps=["Slope-intercept form:   $y = mx + b$", "Substitute:   $m = -5$  and  $b = 2$"],
             answer="y = −5x + 2",
             check=mb("-5*u + 2", "-5", "2"),
             wrong="y = 2x − 5 — the slope and the y-intercept exchanged [B1G-M, AR.3.4: swapping m and b]; y = 5x + 2 — the sign of the slope dropped [Notes III: a negative slope goes down as you move right]"),
        # repeat_ok: rule D matches only small digits that the notes' and examples' lines also carry (a coincidence
        # of values); this equation, its givens and its answer appear nowhere above.
        dict(repeat_ok=True, text=["Kai, in room 204, graphs y = 3x − 2. He plots the y-intercept, then moves up 3 and right 1.",
                   "**Which point does he reach?"],
             unneeded="204",
             steps=["Start:   $(0, -2)$", "Move:   up 3 to $-2 + 3 = 1$,  right 1 to $x = 1$"],
             answer="(1, 1)",
             check=("many", sat("3*u - 2", "0", "-2"), sat("3*u - 2", "1", "1"), ("eq", "-2 + 3", "1")),
             wrong="(1, 5) — up 3 from 2, the sign of b dropped [B1G-M, AR.3.4: swapping m and b]; (3, −1) — right 3 and up 1, rise and run exchanged [B1G-M, AR.3.4: inverting rise and run]; (1, 206) — the room number used as the start [an extra number, included on purpose]"),
        dict(text=["The line $y = 2x + □$ passes through (3, 10).", "**Find the missing number."],
             steps=["Substitute (3, 10):   $10 = 2(3) + b$", "Simplify:   $10 = 6 + b$", "Solve for b:   $b = 4$"],
             answer="4",
             check=("many", ("eq", "10 - 2*3", "4"), sat("2*u + 4", "3", "10")),
             wrong="7 — 10 − 3, the x-value subtracted [B1G-M, AR.4.1: substitution errors]; 16 — 10 + 6, the 6 added, not subtracted [B1G-M, AR.4.1: substitution errors]"),
        dict(kind="written", text=["Ava graphs $y = \\frac{2}{5}x + 1$. She plots (0, 1), then moves up 5 and right 2.",
                                   "**What is Ava's mistake? Which point should she reach?"],
             qtext="Ava graphs y = (2/5)x + 1. She plots (0, 1), then moves up 5 and right 2. What is Ava's mistake? Which point should she reach?",
             steps=["Slope:   $\\frac{2}{5}$ is rise 2 over run 5", "Ava:   up 5 and right 2,  slope $\\frac{5}{2}$",
                    "From (0, 1):   up 2 and right 5 to $(5, 3)$"],
             answer="She swapped rise and run: (5, 3).",
             check=("many", sat("F(2,5)*u + 1", "5", "3"), fails("F(2,5)*u + 1", "2", "6"), mb("F(2,5)*u + 1", "F(2,5)", "1")),
             wrong="'she should start at (1, 0)' — the y-intercept put on the x-axis [B1G-M, GR.1.2: x and y inverted]; (2, 6) — Ava's own point kept [B1G-M, AR.3.4: inverting rise and run]"),
    ],

    # The six (decision 12: the handout prints empty grids, the key draws the line): question 1 is Your Turn 1, drawn in
    # class; a negative whole-number slope (2); b first with a negative fraction (3); b = 0 (4); the pattern breaks — no
    # grid: name m and b and complete a table (5); write the equation from m and b (6).
    independent=[
        # repeat_ok: decision 12 — this question IS Your Turn 1, drawn in class with the teacher circulating.
        dict(repeat_ok=True, stem="Graph  $y = \\frac{4}{3}x - 3$.",
             fig=IS1_G, fig_key=IS1_K,
             answer="The line through (0, −3), (3, 1) and (6, 5)",
             why="Start at the y-intercept, (0, −3). Up 4 and right 3 to (3, 1), then again to (6, 5): the third point is the check.",
             check=("many", mb("F(4,3)*u - 3", "F(4,3)", "-3"), table_of("F(4,3)*u - 3", [0, 3, 6], [-3, 1, 5])), space=0.3),
        dict(stem="Graph  $y = -2x + 3$.",
             fig=IS2_G, fig_key=IS2_K,
             answer="The line through (0, 3), (1, 1) and (2, −1)",
             why="Start at (0, 3). A slope of −2 is down 2 and right 1: (1, 1), then (2, −1).",
             check=("many", mb("-2*u + 3", "-2", "3"), table_of("-2*u + 3", [0, 1, 2], [3, 1, -1])), space=0.3),
        dict(stem="Graph  $y = 4 - \\frac{1}{2}x$.",
             fig=IS3_G, fig_key=IS3_K,
             answer="The line through (0, 4), (2, 3) and (4, 2)",
             why="The y-intercept is written first: start at (0, 4). A slope of −1/2 is down 1 and right 2: (2, 3), then (4, 2).",
             check=("many", mb("4 - F(1,2)*u", "-F(1,2)", "4"), table_of("4 - F(1,2)*u", [0, 2, 4], [4, 3, 2])), space=0.3),
        # repeat_ok: rule D matches only small digits that the notes' and examples' lines also carry (a coincidence
        # of values); this equation, its givens and its answer appear nowhere above.
        dict(repeat_ok=True, stem="Graph  $y = 3x$.",
             fig=IS4_G, fig_key=IS4_K,
             answer="The line through (0, 0), (1, 3) and (2, 6)",
             why="b is 0: start at the origin. Up 3 and right 1: (1, 3), then (2, 6).",
             check=("many", mb("3*u", "3", "0"), table_of("3*u", [0, 1, 2], [0, 3, 6])), space=0.3),
        dict(stem="Name the slope and the y-intercept of $y = -x - 6$. Then complete its table.",
             fig=TAB([-2, 0, 3], [BL, BL, BL]), fig_key=TAB([-2, 0, 3], [-4, -6, -9]),
             answer="The slope is −1 and the y-intercept is −6; y = −4, −6, −9.",
             why="−x is −1 times x, so m = −1, and b = −6. At x = −2: −(−2) − 6 = −4; at x = 0: −6; at x = 3: −3 − 6 = −9.",
             check=("many", mb("-u - 6", "-1", "-6"), table_of("-u - 6", [-2, 0, 3], [-4, -6, -9])), space=0.4),
        # repeat_ok: rule D matches only small digits that the notes' and examples' lines also carry (a coincidence
        # of values); this equation, its givens and its answer appear nowhere above.
        dict(repeat_ok=True, stem="Write the equation of the line with slope $-\\frac{1}{3}$ and y-intercept −5.",
             answer="$y = -\\frac{1}{3}x - 5$",
             why="y = mx + b with m = −1/3 and b = −5.",
             check=mb("-F(1,3)*u - 5", "-F(1,3)", "-5"), space=0.5),
    ],

    # Bank: name m and b (1–2, the second with b first); write the equation (3–4); graph on an empty grid (5–7: a
    # fraction, a negative fraction, b first); move with the slope (8); backwards (9); a statement vote (10); the
    # equation a graph shows (11); a select-all of the lines through a given y-intercept (12). The additional bank
    # mirrors it position by position with new numbers.
    bank=[
        dict(heading="For questions 1 and 2, name the slope and the y-intercept."),
        dict(stem="$y = \\frac{3}{2}x + 4$",
             answer="The slope is 3/2 and the y-intercept is 4.", why="m is the coefficient of x, 3/2; b is the number added, 4.",
             check=mb("F(3,2)*u + 4", "F(3,2)", "4"), space=0.4),
        dict(stem="$y = 1 - 5x$",
             answer="The slope is −5 and the y-intercept is 1.", why="The y-intercept is written first: b = 1, and the number with x is −5.",
             check=mb("1 - 5*u", "-5", "1"), space=0.4),
        dict(heading="For questions 3 and 4, write the equation of the line in slope-intercept form."),
        dict(stem="A line has the slope $\\frac{4}{3}$ and the y-intercept −2.",
             answer="$y = \\frac{4}{3}x - 2$", why="y = mx + b with m = 4/3 and b = −2.",
             check=mb("F(4,3)*u - 2", "F(4,3)", "-2"), space=0.4),
        dict(stem="A line has the slope −2 and the y-intercept 7.",
             answer="y = −2x + 7", why="y = mx + b with m = −2 and b = 7.",
             check=mb("-2*u + 7", "-2", "7"), space=0.4),
        dict(heading="For questions 5 to 7, graph the line on the grid."),
        dict(stem="$y = \\frac{1}{2}x + 1$", fig=BK5_G, fig_key=BK5_K,
             answer="The line through (0, 1), (2, 2) and (4, 3)", why="Start at (0, 1); up 1 and right 2 to (2, 2), then (4, 3).",
             check=table_of("F(1,2)*u + 1", [0, 2, 4], [1, 2, 3]), space=0.3),
        dict(stem="$y = -\\frac{5}{3}x + 4$", fig=BK6_G, fig_key=BK6_K,
             answer="The line through (0, 4), (3, −1) and (6, −6)", why="Start at (0, 4); down 5 and right 3 to (3, −1), then (6, −6).",
             check=table_of("-F(5,3)*u + 4", [0, 3, 6], [4, -1, -6]), space=0.3),
        dict(stem="$y = -4 + \\frac{3}{2}x$", fig=BK7_G, fig_key=BK7_K,
             answer="The line through (0, −4), (2, −1) and (4, 2)", why="The y-intercept is written first: start at (0, −4); up 3 and right 2 to (2, −1), then (4, 2).",
             check=table_of("-4 + F(3,2)*u", [0, 2, 4], [-4, -1, 2]), space=0.3),
        dict(heading="Move with the slope."),
        dict(stem="A line has the y-intercept −1 and the slope $\\frac{4}{3}$. Start at the y-intercept and move with the slope twice. Which two points do you reach?",
             answer="(3, 3) and (6, 7)", why="From (0, −1): up 4 and right 3 to (3, 3), then again to (6, 7).",
             check=table_of("F(4,3)*u - 1", [3, 6], [3, 7]), space=0.5),
        dict(heading="Find the missing number."),
        dict(stem="The line $y = -5x + □$ passes through (2, −3). Find the missing number.",
             answer="7", why="−3 = −5(2) + b = −10 + b, so b = 7.",
             check=("many", ("eq", "-3 + 10", "7"), sat("-5*u + 7", "2", "-3")), space=0.6),
        dict(heading="Choose one."),
        dict(stem="Which statement describes the line $y = 2 - \\frac{1}{3}x$?",
             choices=["Its slope is 2 and it crosses the y-axis at $(0, -\\frac{1}{3})$.", "Its slope is −3 and it crosses the y-axis at (0, 2).", "Its slope is $-\\frac{1}{3}$ and it crosses the y-axis at (2, 0).", "Its slope is $-\\frac{1}{3}$ and it crosses the y-axis at (0, 2)."],
             correct=3, answer="D", why="The number with x is −1/3, the slope; at x = 0, y = 2, so the line crosses the y-axis at (0, 2).",
             check=("many", mb("2 - F(1,3)*u", "-F(1,3)", "2"), slope_not("2 - F(1,3)*u", "2"), fails("2 - F(1,3)*u", "0", "-F(1,3)"),
                    slope_not("2 - F(1,3)*u", "-3"), fails("2 - F(1,3)*u", "2", "0")),
             errors={"A": "the first number taken as the slope [B1G-M, AR.3.4: swapping m and b]", "B": "the fraction turned over [B1G-M, AR.3.4: inverting rise and run]", "C": "the intercept put on the x-axis [B1G-M, GR.1.2: x and y inverted]"}),
        dict(stem="The graph shows a line through $(0, 1)$ and $(1, -1)$. Which equation does it show?",
             fig=figs.plane((-3, 3), (-4, 4), lines=[(-2, 1, "")], points=[(0, 1, "on", "r"), (1, -1, "on", "r")], inches=2.4),
             choices=["$y = 2x + 1$", "$y = x - 2$", "$y = -2x + 1$", "$y = -\\frac{1}{2}x + 1$"],
             correct=2, answer="C", why="It crosses the y-axis at (0, 1), so b = 1; from (0, 1) to (1, −1) is down 2 and right 1, so m = −2.",
             check=("many", sat("-2*u + 1", "0", "1"), sat("-2*u + 1", "1", "-1"), fails("u - 2", "0", "1"),
                    fails("-F(1,2)*u + 1", "1", "-1"), fails("2*u + 1", "1", "-1")),
             errors={"A": "the falling line read as rising [Notes III: a negative slope goes down as you move right]", "B": "the slope and the y-intercept exchanged [B1G-M, AR.3.4: swapping m and b]", "D": "rise and run exchanged [B1G-M, AR.3.4: inverting rise and run]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the equations whose graphs cross the y-axis at (0, 3).",
             choices=["$y = \\frac{4}{3}x - 3$", "$y = \\frac{1}{2}x + 3$", "$y = 3x + 1$", "$y = 3 - \\frac{5}{3}x$", "$y = 3$"],
             correct=[1, 3, 4], answer="B, D, E",
             why="At x = 0 each of B, D and E gives 3. A crosses at (0, −3); C crosses at (0, 1).",
             check=("many", sat("F(1,2)*u + 3", "0", "3"), sat("3 - F(5,3)*u", "0", "3"), sat("0*u + 3", "0", "3"),
                    fails("3*u + 1", "0", "3"), fails("F(4,3)*u - 3", "0", "3")),
             errors={"A": "the sign of b dropped [B1G-M, AR.3.4: swapping m and b]", "C": "the slope 3 taken as the y-intercept [B1G-M, AR.3.4: swapping m and b]"}),
    ],

    additional=[
        dict(heading="For questions 1 and 2, name the slope and the y-intercept."),
        dict(stem="$y = -\\frac{1}{3}x + 6$",
             answer="The slope is −1/3 and the y-intercept is 6.", why="m is the coefficient of x, −1/3; b is the number added, 6.",
             check=mb("-F(1,3)*u + 6", "-F(1,3)", "6"), space=0.4),
        dict(stem="$y = 8 - 2x$",
             answer="The slope is −2 and the y-intercept is 8.", why="The y-intercept is written first: b = 8, and the number with x is −2.",
             check=mb("8 - 2*u", "-2", "8"), space=0.4),
        dict(heading="For questions 3 and 4, write the equation of the line in slope-intercept form."),
        dict(stem="A line has the slope $\\frac{1}{2}$ and the y-intercept −6.",
             answer="$y = \\frac{1}{2}x - 6$", why="y = mx + b with m = 1/2 and b = −6.",
             check=mb("F(1,2)*u - 6", "F(1,2)", "-6"), space=0.4),
        dict(stem="A line has the slope −5 and the y-intercept 3.",
             answer="y = −5x + 3", why="y = mx + b with m = −5 and b = 3.",
             check=mb("-5*u + 3", "-5", "3"), space=0.4),
        dict(heading="For questions 5 to 7, graph the line on the grid."),
        dict(stem="$y = \\frac{1}{2}x - 3$", fig=AD5_G, fig_key=AD5_K,
             answer="The line through (0, −3), (2, −2) and (4, −1)", why="Start at (0, −3); up 1 and right 2 to (2, −2), then (4, −1).",
             check=table_of("F(1,2)*u - 3", [0, 2, 4], [-3, -2, -1]), space=0.3),
        dict(stem="$y = -\\frac{5}{3}x + 5$", fig=AD6_G, fig_key=AD6_K,
             answer="The line through (0, 5), (3, 0) and (6, −5)", why="Start at (0, 5); down 5 and right 3 to (3, 0), then (6, −5).",
             check=table_of("-F(5,3)*u + 5", [0, 3, 6], [5, 0, -5]), space=0.3),
        dict(stem="$y = -1 + \\frac{3}{2}x$", fig=AD7_G, fig_key=AD7_K,
             answer="The line through (0, −1), (2, 2) and (4, 5)", why="The y-intercept is written first: start at (0, −1); up 3 and right 2 to (2, 2), then (4, 5).",
             check=table_of("-1 + F(3,2)*u", [0, 2, 4], [-1, 2, 5]), space=0.3),
        dict(heading="Move with the slope."),
        dict(stem="A line has the y-intercept 3 and the slope $-\\frac{1}{3}$. Start at the y-intercept and move with the slope twice. Which two points do you reach?",
             answer="(3, 2) and (6, 1)", why="From (0, 3): down 1 and right 3 to (3, 2), then again to (6, 1).",
             check=table_of("-F(1,3)*u + 3", [3, 6], [2, 1]), space=0.5),
        dict(heading="Find the missing number."),
        dict(stem="The line $y = -2x + □$ passes through (4, −3). Find the missing number.",
             answer="5", why="−3 = −2(4) + b = −8 + b, so b = 5.",
             check=("many", ("eq", "-3 + 8", "5"), sat("-2*u + 5", "4", "-3")), space=0.6),
        dict(heading="Choose one."),
        dict(stem="Which statement describes the line $y = 5 + \\frac{4}{3}x$?",
             choices=["Its slope is 5 and it crosses the y-axis at $(0, \\frac{4}{3})$.", "Its slope is $\\frac{4}{3}$ and it crosses the y-axis at (0, 5).", "Its slope is $\\frac{3}{4}$ and it crosses the y-axis at (0, 5).", "Its slope is $\\frac{4}{3}$ and it crosses the y-axis at (5, 0)."],
             correct=1, answer="B", why="The number with x is 4/3, the slope; at x = 0, y = 5, so the line crosses the y-axis at (0, 5).",
             check=("many", mb("5 + F(4,3)*u", "F(4,3)", "5"), slope_not("5 + F(4,3)*u", "5"), fails("5 + F(4,3)*u", "0", "F(4,3)"),
                    slope_not("5 + F(4,3)*u", "F(3,4)"), fails("5 + F(4,3)*u", "5", "0")),
             errors={"A": "the first number taken as the slope [B1G-M, AR.3.4: swapping m and b]", "C": "the fraction turned over [B1G-M, AR.3.4: inverting rise and run]", "D": "the intercept put on the x-axis [B1G-M, GR.1.2: x and y inverted]"}),
        dict(stem="The graph shows a line through $(0, -1)$ and $(2, 0)$. Which equation does it show?",
             fig=figs.plane((-3, 4), (-4, 3), lines=[(H, -1, "")], points=[(0, -1, "on", "dr"), (2, 0, "on", "dr")], inches=2.4),
             choices=["$y = -x + \\frac{1}{2}$", "$y = 2x - 1$", "$y = -\\frac{1}{2}x - 1$", "$y = \\frac{1}{2}x - 1$"],
             correct=3, answer="D", why="It crosses the y-axis at (0, −1), so b = −1; from (0, −1) to (2, 0) is up 1 and right 2, so m = 1/2.",
             check=("many", sat("F(1,2)*u - 1", "0", "-1"), sat("F(1,2)*u - 1", "2", "0"), fails("-u + F(1,2)", "0", "-1"),
                    fails("2*u - 1", "2", "0"), fails("-F(1,2)*u - 1", "2", "0")),
             errors={"A": "the slope and the y-intercept exchanged [B1G-M, AR.3.4: swapping m and b]", "B": "rise and run exchanged [B1G-M, AR.3.4: inverting rise and run]", "C": "the rising line read as falling [Notes III: a negative slope goes down as you move right]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the equations whose graphs cross the y-axis at (0, −4).",
             choices=["$y = -4$", "$y = -4 - 2x$", "$y = \\frac{1}{2}x + 4$", "$y = -4x + 1$", "$y = -\\frac{1}{3}x - 4$"],
             correct=[0, 1, 4], answer="A, B, E",
             why="At x = 0 each of A, B and E gives −4. C crosses at (0, 4); D crosses at (0, 1).",
             check=("many", sat("-F(1,3)*u - 4", "0", "-4"), sat("-4 - 2*u", "0", "-4"), sat("0*u - 4", "0", "-4"),
                    fails("-4*u + 1", "0", "-4"), fails("F(1,2)*u + 4", "0", "-4")),
             errors={"C": "the sign of b dropped [B1G-M, AR.3.4: swapping m and b]", "D": "the slope −4 taken as the y-intercept [B1G-M, AR.3.4: swapping m and b]"}),
    ],

    te=dict(
        must="Students graph a two-variable linear equation given in slope-intercept form, starting at the y-intercept and moving with the slope. They name the slope and the y-intercept of y = mx + b, including when it is written y = b + mx.",
        must_not="Point-slope form and standard form are not expectations at this grade level. No line in this lesson is vertical, and no question compares the slopes of two lines.",
        materials="Whiteboards, markers and rulers. Hand out the Independent Set, one per student, at Example 1's Your Turn. Question 1 of the set is that Your Turn, and students draw it in class while the teacher circulates.",
        variation="Whiteboard questions 1 and 2 name the slope and the y-intercept, the second with b written first; 3 votes on a statement about y = 6 + (1/2)x; 4 moves twice with a negative slope from a y-intercept; 5 votes on four graphs of y = 2x − 3. The pattern breaks at 6: the class writes the equation from m and b instead of reading it. 7 carries Kai's room number as the extra number; 8 runs backwards; 9 is written. The set: question 1 drawn in class, then a negative whole-number slope, b first with a negative fraction, b = 0, and the break — no grid, a table and the two numbers — then an equation to write.",
        audit=["Every slope and y-intercept re-derived by sympy at build time (the derivative and the value at x = 0); every point checked on its line; every choice's key and each wrong option checked from its error; every graph drawn from its equation by u10/figs10.py, which refuses a labeled point that is not on its line."],
        changes=["Built from the benchmark, its B1G-M notes and the unit plan; no Math Nation item is reproduced."],
        read_first=[
            "Thursday 21 January. Built from the benchmark and the B1G-M first (the Unit 10 Lesson Outlines, §10.05, standing decisions 2, 9, 11 and 12); Math Nation was read for scope only.",
            "Today names the y-intercept and the form y = mx + b, and graphs a line by starting at the y-intercept and moving with the slope; Unit 11's table of values stays the method for anything else (10.06). A negative slope goes down as you move right: −2/3 is down 2, right 3. Every line gets a third point as the check.",
            "The Examples' question slides show an empty grid: draw the line on the projected slide while the class watches. Right after Example 1, hand out the Independent Set: Your Turn 1 is its question 1, and every student draws it on the handout's grid while you circulate. The boards read; nobody draws a line on a whiteboard. The key draws each line on the student's own grid.",
            "Changed from the outline: none of its numbers."],
    ),
)
