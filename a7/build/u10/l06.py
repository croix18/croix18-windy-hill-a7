# A7 10.06 Graphing from Tables and Contexts (MA.8.AR.3.4), from the unit's Lesson Outlines §10.06.
# Whiteboards read; the Independent Set draws (standing decision 12): the handout prints empty grids with the drawn
# line on the key (figs.pair), and Your Turn 1 IS the handout's question 1, drawn in class.
# Checks are sympy over the REAL numbers: sat / table_of / std_table / other_line below.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs10 as figs          # the unit's figure module (u10/figs10.py)
S = figs.slide
BL = figs.BLANK
H = Fr(1, 2)

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
    """Each y of a table is rhs at its x."""
    return ("many",) + tuple(sat(rhs, str(a), str(b)) for a, b in zip(xs, ys))


def std_table(a, c, xs, ys):
    """Each y is the y that makes a·x + y = c true at its x (the equation solved for y by sympy)."""
    return ("many",) + tuple(("true", "sp.solve(sp.Eq(" + str(a) + "*" + X + " + " + Y + ", " + str(c) + "), " + Y
                              + ")[0].subs(" + X + ", " + str(p) + ") == " + str(q)) for p, q in zip(xs, ys))


def other_line(r1, r2):
    """y = r1 and y = r2 are NOT one line (a wrong option's line is not the key's)."""
    return ("true", "sp.expand((" + _u(r1) + ") - (" + _u(r2) + ")) != 0")


def slope(p, q):
    return "((" + q[1] + ") - (" + p[1] + "))/sp.Integer((" + q[0] + ") - (" + p[0] + "))"


# ---- the notes
T1 = figs.table([([-3, 0, 3, 6], [4, 2, 0, -2])], head=("x", "y"), cw=2.0, rh=1.5)
NOTES1 = S(figs.row([T1, figs.plane((-4, 7), (-4, 6), lines=[(Fr(-2, 3), 2, "")],
                                    points=[(-3, 4, ""), (0, 2, ""), (3, 0, ""), (6, -2, "")])],
                    gap=2.5), inches=8.4, pt=18, reserve=1.1)
POOL = dict(xname="minutes", yname="gallons", ys=100)
NOTES2 = S(figs.plane((0, 6), (0, 500), lines=[(50, 200, "")], **POOL,
                      points=[(0, 200, "on", "dr"), (2, 300, "on", "dr"), (4, 400, "on", "dr")], inches=4.4, pt=18),
           inches=4.4, pt=18, reserve=1.3)
T3 = figs.table([([0, 2, 4], [8, 4, 0])], head=("x", "y"), cw=1.8, rh=1.5, titles=["2x + y = 8"])
NOTES3 = S(figs.row([T3, figs.plane((-1, 5), (-1, 9), lines=[(-2, 8, "")],
                                    points=[(0, 8, ""), (2, 4, ""), (4, 0, "")])],
                    gap=2.5), inches=7.6, pt=18, reserve=1.3)

# ---- Example 1: y = (1/2)x + 3; Your Turn 1 = the handout's question 1, y = 2x − 5
EX1 = S(figs.row([figs.table([([-2, 0, 2, 4], [BL, BL, BL, BL])], cw=1.8, rh=1.5),
                  figs.plane((-3, 5), (-1, 6))], gap=2.5), inches=8.4, pt=18, reserve=0.9)
EX1W = S(figs.plane((-3, 5), (-1, 6), lines=[(H, 3, "")],
                    points=[(-2, 2, ""), (0, 3, "on", "ul"), (2, 4, ""), (4, 5, "on", "dr")],
                    inches=4.0, pt=18), inches=4.0, pt=18, reserve=0.9)
YT1 = S(figs.row([figs.table([([0, 1, 2, 4], [BL, BL, BL, BL])], cw=1.8, rh=1.5),
                  figs.plane((-1, 5), (-6, 4))], gap=2.5), inches=8.0, pt=18, reserve=0.9)
YT1A = S(figs.plane((-1, 5), (-6, 4), lines=[(2, -5, "")],
                    points=[(0, -5, "on", "r"), (1, -3, "on", "r"), (2, -1, "on", "r"), (4, 3, "on", "r")],
                    inches=4.2, pt=18), inches=4.2, pt=18, reserve=0.95)

# ---- Example 2: the cyclist, 60 miles out, 12 miles every hour; Your Turn 2: the bucket, 40 liters, 8 every minute
BIKE = dict(xname="hours", yname="miles from home", ys=12)
EX2 = S(figs.row([figs.table([([0, 1, 2, 5], [BL, BL, BL, BL])], head=("hours", "miles"), cw=1.6, rh=1.5),
                  figs.plane((0, 5), (0, 60), **BIKE)], gap=2.5), inches=8.4, pt=18, reserve=0.9)
EX2W = S(figs.plane((0, 5), (0, 60), lines=[(-12, 60, "", None, (0, 5))], **BIKE,
                    points=[(0, 60, "on", "r"), (1, 48, "on", "ur"), (2, 36, "on", "ur"), (5, 0, "on", "ur")],
                    inches=4.0, pt=18), inches=4.0, pt=18, reserve=0.9)
PAIL = dict(xname="minutes", yname="liters", ys=8)
YT2 = S(figs.row([figs.table([([0, 1, 2, 5], [BL, BL, BL, BL])], head=("minutes", "liters"), cw=1.6, rh=1.5),
                  figs.plane((0, 5), (0, 40), **PAIL)], gap=2.5), inches=8.4, pt=18, reserve=0.9)
YT2A = S(figs.plane((0, 5), (0, 40), lines=[(-8, 40, "", None, (0, 5))], **PAIL,
                    points=[(0, 40, "on", "r"), (1, 32, "on", "ur"), (2, 24, "on", "ur"), (5, 0, "on", "ur")],
                    inches=4.2, pt=18), inches=4.2, pt=18, reserve=0.95)

# ---- the boards
B1T = figs.table([([-1, 0, 2, 5], [BL, BL, BL, BL])], cw=1.8, rh=1.5)
B1A = figs.table([([-1, 0, 2, 5], [-7, -4, 2, 11])], cw=1.8, rh=1.5)
B2T = figs.table([([0, 2, 4], [6, 5, 4])], cw=1.8, rh=1.5)
B5T = figs.table([([1, 2, 3], [5, 8, 11])], cw=1.8, rh=1.5)
# Board 3: four graphs, each on its own axes, the same scales on all four (gallons by 5, minutes by 1)
TUB = dict(ys=5, ystep=2, inches=2.6, pt=18)
G_OK = figs.plane((0, 4), (0, 30), lines=[(5, 10, "")], points=[(0, 10, ""), (2, 20, "")], **TUB)
G_SWAP = figs.plane((0, 4), (0, 30), lines=[(10, 5, "")], points=[(0, 5, ""), (2, 25, "")], **TUB)
G_ZERO = figs.plane((0, 4), (0, 30), lines=[(5, 0, "")], points=[(2, 10, "")], **TUB)
G_FALL = figs.plane((0, 4), (0, 30), lines=[(-5, 10, "", None, (0, 2))], points=[(0, 10, ""), (1, 5, "")], **TUB)
C3 = S(figs.choices4([G_SWAP, G_ZERO, G_FALL, G_OK], gap=2.2), inches=14.0, pt=18, reserve=0.75)
C3A = S(figs.row([figs.plane((0, 4), (0, 30), lines=[(5, 10, "")], xname="minutes", yname="gallons", ys=5, ystep=2,
                             points=[(0, 10, "on", "ul"), (2, 20, "on", "ul")])], titles=["D"], inches=4.2, pt=18),
        inches=4.2, pt=18, reserve=1.0)


def BT(t):
    return S(t, inches=6.4, pt=20, reserve=0.75)


def BTA(t):
    return S(t, inches=5.6, pt=18, reserve=0.95)


# ---- the handout: empty grids, and the key's line drawn on the same window (figs.pair). In Quadrant I a key marks
# only the points off the axes: a dot on a numbered axis tick is read by the kit as a line through that number.
def TAB(xs, ys, head=("x", "y"), title=None):
    return figs.table([(xs, ys)], head=head, titles=[title] if title else None)


IS1_G, IS1_K = figs.pair((-1, 5), (-6, 4), lines=[(2, -5, "")],
                         points=[(0, -5, ""), (1, -3, ""), (2, -1, ""), (4, 3, "")], inches=3.2)
IS2_G, IS2_K = figs.pair((-7, 7), (-6, 4), lines=[(Fr(-2, 3), -1, "")],
                         points=[(-6, 3, ""), (-3, 1, ""), (0, -1, ""), (3, -3, ""), (6, -5, "")], inches=3.2)
IS3_G, IS3_K = figs.pair((0, 6), (0, 400), lines=[(50, 100, "")],
                         points=[(2, 200, ""), (4, 300, ""), (6, 400, "")],
                         xname="hours", yname="miles from the station", ys=50, ystep=1, aspect=0.6, inches=3.2)
IS4_G, IS4_K = figs.pair((0, 7), (0, 35), lines=[(-5, 30, "", None, (0, 6))],
                         points=[(2, 20, ""), (4, 10, "")],
                         xname="minutes", yname="tons of gravel", ys=5, inches=3.2)
IS5_G, IS5_K = figs.pair((-1, 5), (-2, 7), lines=[(-2, 6, "")], points=[(0, 6, ""), (1, 4, ""), (3, 0, "")], inches=3.2)
IS6 = figs.plane((0, 8), (0, 10), lines=[(H, 6, "")], points=[(4, 8, "on", "dr")],
                 xname="hours", yname="inches of snow", inches=3.2)

# ---- the banks' grids
QB4_G, QB4_K = figs.pair((-5, 5), (-5, 3), lines=[(H, -2, "")], points=[(-4, -4, ""), (0, -2, ""), (4, 0, "")], inches=3.0)
QB5_G, QB5_K = figs.pair((-2, 3), (-9, 8), lines=[(5, -3, "")], points=[(-1, -8, ""), (0, -3, ""), (1, 2, ""), (2, 7, "")],
                         ystep=2, inches=3.0)
QB6_G, QB6_K = figs.pair((0, 6), (0, 450), lines=[(50, 150, "")], points=[(2, 250, ""), (4, 350, "")],
                         xname="minutes", yname="meters above the ground", ys=50, ystep=1, aspect=0.6, inches=3.0)
QB7_G, QB7_K = figs.pair((0, 3), (0, 16), lines=[(-8, 16, "", None, (0, 2))], points=[(1, 8, "")],
                         xname="hours", yname="miles from home", ys=2, inches=3.0)
QB8_G, QB8_K = figs.pair((-1, 4), (-1, 10), lines=[(-3, 9, "")], points=[(0, 9, ""), (1, 6, ""), (3, 0, "")], inches=3.0)
QB9 = figs.plane((0, 6), (0, 24), lines=[(3, 4, "")], points=[(0, 4, "on", "ul"), (2, 10, "on", "ul")],
                 xname="weeks", yname="height (cm)", ys=2, ystep=2, inches=3.0)

QA4_G, QA4_K = figs.pair((-5, 5), (-3, 5), lines=[(Fr(1, 4), 2, "")], points=[(-4, 1, ""), (0, 2, ""), (4, 3, "")], inches=3.0)
QA5_G, QA5_K = figs.pair((-3, 4), (-8, 4), lines=[(2, -3, "")], points=[(-2, -7, ""), (0, -3, ""), (1, -1, ""), (3, 3, "")],
                         ystep=2, inches=3.0)
QA6_G, QA6_K = figs.pair((0, 6), (0, 400), lines=[(50, 100, "")], points=[(2, 200, ""), (4, 300, "")],
                         xname="minutes", yname="feet above the ground", ys=50, ystep=1, aspect=0.6, inches=3.0)
QA7_G, QA7_K = figs.pair((0, 5), (0, 48), lines=[(-12, 48, "", None, (0, 4))], points=[(2, 24, "")],
                         xname="minutes", yname="pounds left", ys=6, ystep=2, inches=3.0)
QA8_G, QA8_K = figs.pair((-1, 6), (-1, 11), lines=[(-2, 10, "")], points=[(0, 10, ""), (2, 6, ""), (5, 0, "")], inches=3.0)
QA9 = figs.plane((0, 6), (0, 40), lines=[(5, 10, "")], points=[(0, 10, "on", "ul"), (2, 20, "on", "ul")],
                 xname="hours", yname="length (cm)", ys=5, ystep=2, inches=3.0)


L = dict(
    code="10.06", unit=10, lesson_no=6,
    title="Graphing from Tables and Contexts",
    unit_title="Linear Relationships",
    benchmark="MA.8.AR.3.4",
    benchmark_text="Given a mathematical or real-world context, graph a two-variable linear equation from a written description, a table or an equation in slope-intercept form.",
    target="I can graph a linear relationship from a table or a description, with scales that fit.",
    essential="How do the start and the rate of a situation tell you where its line begins and which way it goes?",
    building_on="Lesson 10.05 taught the y-intercept and graphing from y = mx + b. Lessons 10.02–03 found the slope from a graph, a table and two points. Lesson 11.07 graphed a line from a table of values.",
    working_toward="Lessons 10.07–08 interpret the slope and the y-intercept of a situation. Lessons 10.09 and 10.10 write the equation of a line from a graph, a table and a description.",
    vocab=[],
    vocab_slide=False,
    ixl=["Complete a table and graph a linear function — DC2", "Complete a table and make a graph: word problems — T7R",
         "Complete a table for a linear function — D9B", "Graph a line from an equation in standard form — 7MZ"],
    closure="Whiteboard question 9 is written work and it is the exit evidence. A full answer says that Lee exchanged the start and the rate: the pool starts at 50 gallons and gains 20 gallons every minute, so two correct points are (0, 50) and (2, 90).",

    mtr=[("MTR.2.1", "Students show one relationship as a description, a table and a graph, and move from each to the others."),
         ("MTR.4.1", "On whiteboard questions 3 and 5, students convince a neighbor and then vote again."),
         ("MTR.6.1", "Students check that a third point lies on the line they drew before they call the graph finished.")],
    hoq=[("Why does a real-world graph start at x = 0?", "DOK 1"),
         ("How do you choose a scale for the y-axis when the values reach 400?", "DOK 2"),
         ("2x + y = 8 is not in slope-intercept form. How can you still graph it?", "DOK 2"),
         ("Lee plotted (0, 20) for a pool that starts at 50 gallons. What did Lee mix up, and how would the graph show it?", "DOK 3")],
    differentiation=[
        ("ESE / 504", "Students receive a printed table with the x-values already written beside each grid, and a ruler. Notes II stays on display from whiteboard question 3 onward."),
        ("ELL", "The words start, rate, scale and y-intercept are posted with a picture of each on a graph, and the teacher points to them while reading each story aloud."),
        ("Enrichment", "Students write a story whose graph passes through (0, 30) and (5, 0), and they explain what the slope means in their story.")],

    warmup=[
        dict(stem="What are the slope and the y-intercept of  $y = 5 - 2x$?", answer="−2 and 5",
             check=("many", ("eq", "sp.diff(5 - 2*" + X + ", " + X + ")", "-2"), ("eq", "(5 - 2*" + X + ").subs(" + X + ", 0)", "5"))),
        dict(stem="Find the slope of the line through $(-2, 3)$ and $(2, 11)$.", answer="2",
             check=("eq", slope(("-2", "3"), ("2", "11")), "2")),
        dict(stem="A proportional relationship passes through $(5, 7)$. Find y when x is 10.", answer="14",
             check=("eq", "sp.Rational(7, 5)*10", "14")),
        dict(stem="For  $y = 15 + 10x$,  find y when x is 0, 2 and 4.", answer="15, 35, 55",
             check=table_of("15 + 10*u", [0, 2, 4], [15, 35, 55])),
    ],

    notes=[
        dict(numeral="I", head="From a table: plot the pairs, then draw the line through them", min=3,
             fig=NOTES1,
             items2=["The line crosses the y-axis at 2", "and goes down 2 for every 3 units to the right.",
                     "Slope $-\\frac{2}{3}$:   $y = -\\frac{2}{3}x + 2$"],
             letters=False),
        dict(numeral="II", head="From a description", min=4,
             text=["The start is the y-intercept and the rate is the slope.",
                   "A pool holds 200 gallons, and a hose adds 50 gallons every minute."],
             fig=NOTES2,
             items2=["Choose scales that fit: minutes 0 to 6, gallons 0 to 500 counting by 100.",
                     "A real-world graph starts at x = 0."],
             letters=False),
        dict(numeral="III", head="An equation in another form: make a table of values", min=3,
             fig=NOTES3,
             items2=["$2x + y = 8$:   when x is 0, y is 8;  when x is 2, y is 4;  when x is 4, y is 0.",
                     "Plot the three points and draw the line.",
                     "Solving the equation for y gives  $y = -2x + 8$,  the same line."],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=2,
             prompt=["$y = \\frac{1}{2}x + 3$"], fig=EX1,
             ask="Complete the table for x = −2, 0, 2 and 4, then graph the line.",
             worked=[dict(min=2,
                          rows=[("x = -2:\\ \\ -1 + 3 = 2", "half of −2, plus 3"),
                                ("x = 0:\\ \\ 0 + 3 = 3", "the y-intercept"),
                                ("x = 2:\\ \\ 1 + 3 = 4", "half of 2, plus 3"),
                                ("x = 4:\\ \\ 2 + 3 = 5", "the check")],
                          fig=EX1W, answer="The line through (0, 3) and (4, 5)")],
             check=table_of("F(1,2)*u + 3", [-2, 0, 2, 4], [2, 3, 4, 5]),
             # standing decision 12: this Your Turn IS the Independent Set's question 1 — hand the set out now; every
             # student draws question 1 on its grid while the teacher circulates.
             your_turn=dict(min=5,
                            prompt=["Handout, question 1:  $y = 2x - 5$"], fig=YT1, fig_a=YT1A,
                            ask="Complete the table for x = 0, 1, 2 and 4, then graph the line.",
                            steps=["at $x = 0$ and $1$:   $2(0) - 5 = -5$   and   $2(1) - 5 = -3$",
                                   "at $x = 2$:   $2(2) - 5 = -1$",
                                   "at $x = 4$:   $2(4) - 5 = 3$"],
                            answer="The line through (0, −5) and (4, 3)"),
             yt_check=table_of("2*u - 5", [0, 1, 2, 4], [-5, -3, -1, 3])),
        dict(title="Example 2", min_q=1,
             prompt=["A cyclist is 60 miles from home and rides toward home at 12 miles every hour."], fig=EX2,
             ask="Graph her distance from home versus time.",
             worked=[dict(min=2,
                          rows=[("(0, 60)", "the start is the y-intercept"),
                                ("60 - 12 = 48,\\ \\ 48 - 12 = 36", "after 1 hour and 2 hours"),
                                ("60 - 12(5) = 0", "home after 5 hours: (5, 0)"),
                                ("\\text{slope } -12", "a negative slope goes down as you move right")],
                          fig=EX2W, answer="The line from (0, 60) to (5, 0)")],
             check=table_of("-12*u + 60", [0, 1, 2, 5], [60, 48, 36, 0]),
             your_turn=dict(min=2,
                            prompt=["A bucket holds 40 liters and leaks 8 liters every minute."], fig=YT2, fig_a=YT2A,
                            ask="Graph the liters in the bucket versus time.",
                            steps=["start:   $(0, 40)$", "$40 - 8 = 32$   and   $32 - 8 = 24$",
                                   "$40 - 8(5) = 0$:   the point $(5, 0)$"],
                            answer="The line from (0, 40) to (5, 0)"),
             yt_check=table_of("-8*u + 40", [0, 1, 2, 5], [40, 32, 24, 0])),
    ],

    # The round: a table from an equation (1); slope and y-intercept from a table (2); a vote on four graphs of one
    # story (3); points from a description (4); a vote on where a table's line crosses the y-axis (5); an equation in
    # another form (6); the boat, its seats the extra number (7); a missing number on a line (8); Lee's mistake (9).
    whiteboard=[
        dict(text=["**Complete the table for $y = 3x - 4$", "**using the x-values −1, 0, 2 and 5."],
             qtext="Complete the table for y = 3x − 4 using the x-values −1, 0, 2 and 5.",
             fig=BT(B1T), fig_a=BTA(B1A),
             steps=["$3(-1) - 4 = -7$", "$3(0) - 4 = -4$", "$3(2) - 4 = 2$", "$3(5) - 4 = 11$"],
             answer="−7, −4, 2, 11",
             check=table_of("3*u - 4", [-1, 0, 2, 5], [-7, -4, 2, 11]),
             wrong="−1 at x = −1 — 3(−1) read as 3 [Example 1: substitute each x, signs and all]; −1, −4, 6, 15 — 3x + 4, the subtraction taken as addition after x = 0 [Example 1: substitute each x]"),
        # repeat_ok: the outline's own board; rule D matches only small numbers (0 to 6) that Notes I–III and
        # Example 1 print as axis numbers and table entries. No table of 6, 5, 4 and no slope −1/2 is shown above.
        dict(repeat_ok=True, text=["A table has the x-values 0, 2, 4 and the y-values 6, 5, 4.",
                   "**What are the slope and the y-intercept of its line?"],
             qtext="A table has the x-values 0, 2, 4 and the y-values 6, 5, 4. What are the slope and the y-intercept of its line?",
             fig=BT(B2T), fig_a=BTA(B2T),
             steps=["slope:   $\\frac{5 - 6}{2 - 0} = -\\frac{1}{2}$", "y-intercept:   y is 6 when x is 0"],
             answer="Slope −1/2; y-intercept 6.",
             check=("many", ("eq", slope(("0", "6"), ("2", "5")), "-1/2"), ("eq", slope(("2", "5"), ("4", "4")), "-1/2"),
                    table_of("-F(1,2)*u + 6", [0, 2, 4], [6, 5, 4]), ("eq", "(-F(1,2)*" + X + " + 6).subs(" + X + ", 0)", "6")),
             wrong="slope −2 — the change in x over the change in y [B1G-M, AR.3.2: inverting x and y in the slope]; slope −1 — the change in y alone [standing decision 5: x-steps that are not 1]; y-intercept 4 — the last y read [Notes II: the y-intercept is the value of y when x is 0]"),
        dict(kind="mc", text=["**A tub has 10 gallons and gains 5 per minute. Which is its graph?"],
             qtext="A tub has 10 gallons and gains 5 gallons per minute. Four graphs, each with minutes across and gallons up, the gallons axis counting by 5. Which graph shows the gallons in the tub versus the minutes?",
             fig=C3, fig_a=C3A,
             steps=["start:   $(0, 10)$", "after 2 minutes:   $10 + 5(2) = 20$"],
             choices=["A", "B", "C", "D"], correct=3, answer="D — through (0, 10) and (2, 20)",
             errors={"A": "the line from (0, 5) through (2, 25): the start and the rate exchanged [B1G-M, AR.3.4: swapping m and b]", "B": "the line from (0, 0) through (2, 10): the start left out [Notes II: the start is the y-intercept]", "C": "the line from (0, 10) through (2, 0): falling, not rising — the 5 gallons taken away [B1G-M, AR.3.4: inverting the direction of the rise]"},
             check=("many", table_of("5*u + 10", [0, 2], [10, 20]),
                    table_of("10*u + 5", [0, 2], [5, 25]), other_line("10*u + 5", "5*u + 10"),
                    table_of("5*u", [0, 2], [0, 10]), other_line("5*u", "5*u + 10"),
                    table_of("-5*u + 10", [0, 2], [10, 0]), other_line("-5*u + 10", "5*u + 10"))),
        dict(text=["A kitten weighs 2 pounds and gains 0.5 pounds every week.",
                   "**Write the points for weeks 0, 2 and 4."],
             qtext="A kitten weighs 2 pounds and gains 0.5 pounds every week. Write the points for weeks 0, 2 and 4.",
             steps=["week 0:   the start, $(0, 2)$", "week 2:   $2 + 0.5(2) = 3$", "week 4:   $2 + 0.5(4) = 4$"],
             answer="(0, 2), (2, 3) and (4, 4)",
             check=table_of("F(1,2)*u + 2", [0, 2, 4], [2, 3, 4]),
             wrong="(0, 0.5), (2, 4.5), (4, 8.5) — the start and the rate exchanged [B1G-M, AR.3.4: swapping m and b]; (2, 2.5) and (4, 3) — 0.5 added once for each point, not for each week [Notes II: the rate is the slope]"),
        dict(kind="mc", text=["A table of a linear relationship has the x-values 1, 2, 3 and the y-values 5, 8, 11.",
                              "**Where does its line cross the y-axis?"],
             qtext="A table of a linear relationship has the x-values 1, 2, 3 and the y-values 5, 8, 11. Where does its line cross the y-axis?",
             fig=BT(B5T), fig_a=BTA(B5T),
             steps=["slope:   $\\frac{8 - 5}{2 - 1} = 3$", "one step back to $x = 0$:   $5 - 3 = 2$"],
             choices=["At 3", "At 2", "At 5", "At 0"], correct=1, answer="B — at 2",
             errors={"A": "the slope read as the y-intercept [B1G-M, AR.3.4: swapping m and b]", "C": "the first y-value read as the y-intercept, at x = 1 and not x = 0 [Notes II: the y-intercept is the value of y when x is 0]", "D": "every line taken to start at the origin [standing decision 3: a linear relationship is proportional only through the origin]"},
             check=("many", table_of("3*u + 2", [1, 2, 3], [5, 8, 11]), ("eq", "(3*" + X + " + 2).subs(" + X + ", 0)", "2"),
                    fails("3*u + 2", "0", "5"), fails("3*u + 2", "0", "3"), fails("3*u + 2", "0", "0"))),
        dict(text=["**For $3x + y = 12$, find y when x is 0, 2 and 4."],
             qtext="For 3x + y = 12, find y when x is 0, 2 and 4.",
             steps=["$x = 0$:   $3(0) + y = 12$,  so  $y = 12$", "$x = 2$:   $6 + y = 12$,  so  $y = 6$",
                    "$x = 4$:   $12 + y = 12$,  so  $y = 0$"],
             answer="12, 6, 0",
             check=std_table(3, 12, [0, 2, 4], [12, 6, 0]),
             wrong="12, 18, 24 — 3x added to 12, not subtracted [Notes III: solving the equation for y]; 4, 2, 0 — 12 divided by 3 first [Notes III: make a table of values]"),
        # the seats were 6 in the outline, the same number as the answer's 6 hours; 4 seats keeps the extra number
        # apart from the answer (and 48 ÷ 4 = 12 is its own wrong answer)
        dict(text=["A boat with 4 seats is 48 miles from port and sails toward port at 8 miles every hour.",
                   "**At which point does the graph of its distance from port versus time reach the x-axis?"],
             qtext="A boat with 4 seats is 48 miles from port and sails toward port at 8 miles every hour. At which point does the graph of its distance from port versus time reach the x-axis?",
             unneeded="4",
             steps=["distance:   $48 - 8t$", "$48 - 8(6) = 0$:   in port after 6 hours"],
             answer="(6, 0)",
             check=("many", ("eq", "sp.solve(48 - 8*" + X + ", " + X + ")[0]", "6"), sat("48 - 8*u", "6", "0")),
             wrong="(12, 0) — 48 ÷ 4, the seats used [an extra number, included on purpose]; (0, 48) — where the graph starts, on the y-axis [Notes II: the start is the y-intercept]"),
        dict(text=["The points (0, 7), (2, 13) and $(5, □)$ are on one line.", "**Find the missing number."],
             qtext="The points (0, 7) and (2, 13) are on one line, and so is a point whose x-coordinate is 5. Find the missing y-coordinate of that point.",
             steps=["slope:   $\\frac{13 - 7}{2 - 0} = 3$", "$7 + 3(5) = 22$"],
             answer="22",
             check=("many", ("eq", slope(("0", "7"), ("2", "13")), "3"), ("eq", "7 + 3*5", "22"),
                    ("eq", slope(("2", "13"), ("5", "22")), "3")),
             wrong="16 — 13 + 3, one slope step for 3 units of x [B1G-M, AR.3.2: the change in x read as 1]; 35 — 7 · 5, the y-intercept multiplied by x [B1G-M, AR.3.4: swapping m and b]"),
        dict(kind="written", text=["A pool holds 50 gallons and gains 20 gallons every minute.",
                                   "Lee plots (0, 20) and (2, 120).",
                                   "**What is Lee's mistake? Write two correct points."],
             qtext="A pool holds 50 gallons and gains 20 gallons every minute. Lee plots (0, 20) and (2, 120). What is Lee's mistake? Write two correct points.",
             steps=["Lee's points:   $20 + 50(2) = 120$:  start 20, rate 50", "start 50, rate 20:   $(0, 50)$",
                    "$50 + 20(2) = 90$:   the point $(2, 90)$"],
             answer="Lee exchanged the start and rate: (0, 50) and (2, 90).",
             check=("many", table_of("50*u + 20", [0, 2], [20, 120]), other_line("50*u + 20", "20*u + 50"),
                    table_of("20*u + 50", [0, 2], [50, 90])),
             wrong="'Lee used the wrong x-values' — the points read for their x's, not their y's [B1G-M, AR.3.4: swapping m and b]; (0, 50) and (2, 70) — the rate added once, not for each minute [Notes II: the rate is the slope]"),
    ],

    # The six: question 1 IS Your Turn 1, drawn in class (decision 12); a table to graph, then its y-intercept, which
    # is not in the table (2); a description that rises, its axes given (3); one that falls and stops at the x-axis
    # (4); the break — an equation in another form, 2x + y = 6, through a table (5); a real-world graph read (6).
    independent=[
        # repeat_ok: standing decision 12 — this question IS Your Turn 1, drawn in class with the teacher circulating.
        dict(repeat_ok=True, stem="Complete the table for $y = 2x - 5$, then graph the line.",
             fig=figs.row([TAB([0, 1, 2, 4], [BL, BL, BL, BL]), IS1_G], gap=1.8),
             fig_key=figs.row([TAB([0, 1, 2, 4], [-5, -3, -1, 3]), IS1_K], gap=1.8),
             answer="−5, −3, −1, 3; the line through (0, −5) and (4, 3)",
             why="2(0) − 5 = −5, 2(1) − 5 = −3, 2(2) − 5 = −1 and 2(4) − 5 = 3. The four points lie on one line.",
             check=table_of("2*u - 5", [0, 1, 2, 4], [-5, -3, -1, 3]), space=0.3),
        # repeat_ok: rule D matches only the axis numbers 0 to 6 and the answer's 1; the table (−6, 3), (−3, 1),
        # (3, −3), (6, −5) and its y-intercept −1 appear nowhere above.
        dict(repeat_ok=True, stem="Graph the line through the points in the table. What is its y-intercept?",
             fig=figs.row([TAB([-6, -3, 3, 6], [3, 1, -3, -5]), IS2_G], gap=1.8),
             fig_key=figs.row([TAB([-6, -3, 3, 6], [3, 1, -3, -5]), IS2_K], gap=1.8),
             answer="The y-intercept is −1.",
             why="Each step of 3 to the right goes down 2: slope −2/3. From (−3, 1), one step of 3 to the right reaches (0, −1).",
             check=("many", table_of("-F(2,3)*u - 1", [-6, -3, 3, 6], [3, 1, -3, -5]),
                    ("eq", "1 - (" + slope(("-3", "1"), ("3", "-3")) + ")*(-3)", "-1")), space=0.3),
        # repeat_ok: rule D matches the grid's axis numbers (0 to 400 by 50, as Notes II's pool counts by 100); the
        # train starts at 100, not 200, and its line is y = 50x + 100, which nothing above draws.
        dict(repeat_ok=True, stem="A train is 100 miles from the station and travels away from it at 50 miles every hour. Graph its distance from the station versus time.",
             fig=IS3_G, fig_key=IS3_K,
             answer="The line from (0, 100) through (2, 200) to (6, 400)",
             why="The start, 100 miles, is the y-intercept; the rate, 50 miles per hour, is the slope: 100 + 50(2) = 200 and 100 + 50(6) = 400.",
             check=table_of("50*u + 100", [0, 2, 4, 6], [100, 200, 300, 400]), space=0.3),
        dict(stem="A dump truck holds 30 tons of gravel and unloads 5 tons every minute. Graph the tons of gravel in the truck versus time.",
             fig=IS4_G, fig_key=IS4_K,
             answer="The line from (0, 30) to (6, 0)",
             why="The start, 30 tons, is the y-intercept; the slope is −5: 30 − 5(2) = 20 and 30 − 5(6) = 0, empty after 6 minutes.",
             check=("many", table_of("-5*u + 30", [0, 2, 6], [30, 20, 0]), ("eq", "sp.solve(30 - 5*" + X + ", " + X + ")[0]", "6")),
             space=0.3),
        # repeat_ok: the outline's own question; it shares only the form 2x + y with Notes III (2x + y = 8). The
        # equation 2x + y = 6, its x-values 0, 1, 3 and its table 6, 4, 0 are new.
        dict(repeat_ok=True, stem="Complete the table for $2x + y = 6$, then graph the line.",
             fig=figs.row([TAB([0, 1, 3], [BL, BL, BL]), IS5_G], gap=1.8),
             fig_key=figs.row([TAB([0, 1, 3], [6, 4, 0]), IS5_K], gap=1.8),
             answer="6, 4, 0; the line through (0, 6) and (3, 0)",
             why="2(0) + y = 6, so y = 6; 2(1) + y = 6, so y = 4; 2(3) + y = 6, so y = 0. Solved for y: y = −2x + 6.",
             check=std_table(2, 6, [0, 1, 3], [6, 4, 0]), space=0.3),
        dict(stem="The graph shows the snow on the ground, in inches, versus the time, in hours, during a storm. How deep was the snow at the start, and how fast did it rise?",
             fig=IS6,
             answer="6 inches at the start; it rose 1/2 inch per hour.",
             why="The line meets the y-axis at 6: the start, (0, 6). From (0, 6) to (4, 8) it rises 2 inches in 4 hours: 2 ÷ 4 = 1/2 inch per hour.",
             check=("many", ("eq", slope(("0", "6"), ("4", "8")), "1/2"), sat("F(1,2)*u + 6", "0", "6")), space=0.5),
    ],

    # Bank: two tables from equations (1–2); slope and y-intercept from a table (3); a line to graph from an equation
    # and from a table (4–5); a rising and a falling story to graph (6–7); an equation in another form (8); a graph
    # read for its start and rate (9); two diagnostics (10–11); a missing number (12). The additional bank mirrors it.
    bank=[
        dict(heading="For questions 1 and 2, complete the table for the equation."),
        dict(stem="$y = 5x - 2$",
             fig=TAB([-1, 0, 1, 3], [BL, BL, BL, BL]), fig_key=TAB([-1, 0, 1, 3], [-7, -2, 3, 13]),
             answer="−7, −2, 3, 13", why="5(−1) − 2 = −7, 5(0) − 2 = −2, 5(1) − 2 = 3 and 5(3) − 2 = 13.",
             check=table_of("5*u - 2", [-1, 0, 1, 3], [-7, -2, 3, 13]), space=0.4),
        dict(stem="$y = -\\frac{2}{3}x + 4$",
             fig=TAB([-3, 0, 3, 6], [BL, BL, BL, BL]), fig_key=TAB([-3, 0, 3, 6], [6, 4, 2, 0]),
             answer="6, 4, 2, 0", why="−(2/3)(−3) + 4 = 6, then 4, −(2/3)(3) + 4 = 2 and −(2/3)(6) + 4 = 0.",
             check=table_of("-F(2,3)*u + 4", [-3, 0, 3, 6], [6, 4, 2, 0]), space=0.4),
        dict(heading="Use the table."),
        dict(stem="What are the slope and the y-intercept of the line through the points in the table?",
             fig=TAB([0, 2, 4], [1, 7, 13]),
             answer="Slope 3; y-intercept 1.", why="(7 − 1) ÷ (2 − 0) = 3, and y is 1 when x is 0.",
             check=("many", ("eq", slope(("0", "1"), ("2", "7")), "3"), table_of("3*u + 1", [0, 2, 4], [1, 7, 13])), space=0.4),
        dict(heading="For questions 4 and 5, graph the line on the grid."),
        dict(stem="Make a table for $y = \\frac{1}{2}x - 2$, then graph the line.",
             fig=QB4_G, fig_key=QB4_K,
             answer="The line through (−4, −4), (0, −2) and (4, 0)", why="Even x's: ½(−4) − 2 = −4, ½(0) − 2 = −2, ½(4) − 2 = 0.",
             check=table_of("F(1,2)*u - 2", [-4, 0, 4], [-4, -2, 0]), space=0.9),
        dict(stem="Graph the line through the points in the table. What is its y-intercept?",
             fig=figs.row([TAB([-1, 1, 2], [-8, 2, 7]), QB5_G], gap=1.8), fig_key=figs.row([TAB([-1, 1, 2], [-8, 2, 7]), QB5_K], gap=1.8),
             answer="The y-intercept is −3.", why="From (1, 2) to (2, 7) is up 5 for 1 to the right: slope 5. One step back from (1, 2) gives (0, −3).",
             check=("many", table_of("5*u - 3", [-1, 1, 2], [-8, 2, 7]), ("eq", "2 - (" + slope(("1", "2"), ("2", "7")) + ")", "-3")), space=0.9),
        dict(heading="For questions 6 and 7, graph the situation on the grid."),
        dict(stem="A balloon is 150 meters above the ground and rises 50 meters every minute. Graph its height versus time.",
             fig=QB6_G, fig_key=QB6_K,
             answer="The line from (0, 150) through (2, 250) to (6, 450)", why="The start, 150, is the y-intercept; the slope is 50: 150 + 50(2) = 250 and 150 + 50(6) = 450.",
             check=table_of("50*u + 150", [0, 2, 6], [150, 250, 450]), space=0.9),
        dict(stem="A jogger is 16 miles from home and runs toward home at 8 miles every hour. Graph her distance from home versus time.",
             fig=QB7_G, fig_key=QB7_K,
             answer="The line from (0, 16) to (2, 0)", why="The start, 16, is the y-intercept; the slope is −8: 16 − 8(1) = 8 and 16 − 8(2) = 0.",
             check=table_of("-8*u + 16", [0, 1, 2], [16, 8, 0]), space=0.9),
        dict(heading="An equation in another form."),
        dict(stem="Complete a table for $3x + y = 9$ at $x = 0$, $1$ and $3$, then graph the line.",
             fig=QB8_G, fig_key=QB8_K,
             answer="9, 6, 0; the line through (0, 9) and (3, 0)", why="3(0) + y = 9, so y = 9; 3 + y = 9, so y = 6; 9 + y = 9, so y = 0.",
             check=std_table(3, 9, [0, 1, 3], [9, 6, 0]), space=0.9),
        dict(heading="Read the graph."),
        dict(stem="The graph shows a plant's height, in centimeters, versus the time, in weeks. How tall was the plant at the start, and how fast does it grow?",
             fig=QB9,
             answer="4 centimeters at the start; it grows 3 centimeters per week.", why="The line starts at (0, 4); from (0, 4) to (2, 10) it rises 6 in 2 weeks: 6 ÷ 2 = 3.",
             check=("many", ("eq", slope(("0", "4"), ("2", "10")), "3"), sat("3*u + 4", "0", "4")), space=0.5),
        dict(heading="Choose one."),
        dict(stem="A table of a linear relationship has the x-values 2, 3, 4 and the y-values 1, 4, 7. Where does its line cross the y-axis?",
             choices=["At 3", "At 0", "At −5", "At 1"], correct=2, answer="C",
             why="The slope is 3. Two steps back from (2, 1) to x = 0: 1 − 3(2) = −5.",
             check=("many", table_of("3*u - 5", [2, 3, 4], [1, 4, 7]), ("eq", "(3*" + X + " - 5).subs(" + X + ", 0)", "-5"),
                    fails("3*u - 5", "0", "1"), fails("3*u - 5", "0", "3"), fails("3*u - 5", "0", "0")),
             errors={"A": "the slope read as the y-intercept [B1G-M, AR.3.4: swapping m and b]", "B": "every line taken to start at the origin [standing decision 3: a linear relationship is proportional only through the origin]", "D": "the first y-value read as the y-intercept, at x = 2 and not x = 0 [Notes II: the y-intercept is the value of y when x is 0]"}),
        dict(stem="A tub holds 5 gallons, and a hose adds 3 gallons every minute. Which two points are on the graph of the gallons in the tub versus the minutes?",
             choices=["$(0, 5)$ and $(2, 11)$", "$(0, 5)$ and $(2, -1)$", "$(0, 0)$ and $(2, 6)$", "$(0, 3)$ and $(2, 13)$"],
             correct=0, answer="A",
             why="The start, 5, is the y-intercept: (0, 5). After 2 minutes, 5 + 3(2) = 11.",
             check=("many", table_of("3*u + 5", [0, 2], [5, 11]), fails("3*u + 5", "0", "3"), fails("3*u + 5", "0", "0"),
                    fails("3*u + 5", "2", "-1"), table_of("5*u + 3", [0, 2], [3, 13]), table_of("-3*u + 5", [0, 2], [5, -1])),
             errors={"B": "the 3 gallons taken away, not added [B1G-M, AR.3.4: inverting the direction of the rise]", "C": "the start left out [Notes II: the start is the y-intercept]", "D": "the start and the rate exchanged [B1G-M, AR.3.4: swapping m and b]"}),
        dict(heading="Find the missing number."),
        dict(stem="The points $(0, -1)$, $(2, 5)$ and $(6, □)$ are on one line. Find the missing number.", answer="17",
             why="The slope is (5 − (−1)) ÷ 2 = 3, so y = 3x − 1, and 3(6) − 1 = 17.",
             check=("many", ("eq", slope(("0", "-1"), ("2", "5")), "3"), ("eq", "3*6 - 1", "17")), space=0.6),
    ],

    additional=[
        dict(heading="For questions 1 and 2, complete the table for the equation."),
        dict(stem="$y = 3x - 5$",
             fig=TAB([-2, 0, 1, 4], [BL, BL, BL, BL]), fig_key=TAB([-2, 0, 1, 4], [-11, -5, -2, 7]),
             answer="−11, −5, −2, 7", why="3(−2) − 5 = −11, 3(0) − 5 = −5, 3(1) − 5 = −2 and 3(4) − 5 = 7.",
             check=table_of("3*u - 5", [-2, 0, 1, 4], [-11, -5, -2, 7]), space=0.4),
        dict(stem="$y = -\\frac{1}{2}x + 3$",
             fig=TAB([-4, 0, 2, 6], [BL, BL, BL, BL]), fig_key=TAB([-4, 0, 2, 6], [5, 3, 2, 0]),
             answer="5, 3, 2, 0", why="−½(−4) + 3 = 5, then 3, −½(2) + 3 = 2 and −½(6) + 3 = 0.",
             check=table_of("-F(1,2)*u + 3", [-4, 0, 2, 6], [5, 3, 2, 0]), space=0.4),
        dict(heading="Use the table."),
        dict(stem="What are the slope and the y-intercept of the line through the points in the table?",
             fig=TAB([0, 3, 6], [8, 6, 4]),
             answer="Slope −2/3; y-intercept 8.", why="(6 − 8) ÷ (3 − 0) = −2/3, and y is 8 when x is 0.",
             check=("many", ("eq", slope(("0", "8"), ("3", "6")), "-2/3"), table_of("-F(2,3)*u + 8", [0, 3, 6], [8, 6, 4])), space=0.4),
        dict(heading="For questions 4 and 5, graph the line on the grid."),
        dict(stem="Make a table for $y = \\frac{1}{4}x + 2$, then graph the line.",
             fig=QA4_G, fig_key=QA4_K,
             answer="The line through (−4, 1), (0, 2) and (4, 3)", why="Use x-values that 4 divides: (1/4)(−4) + 2 = 1, (1/4)(0) + 2 = 2, (1/4)(4) + 2 = 3.",
             check=table_of("F(1,4)*u + 2", [-4, 0, 4], [1, 2, 3]), space=0.9),
        dict(stem="Graph the line through the points in the table. What is its y-intercept?",
             fig=figs.row([TAB([-2, 1, 3], [-7, -1, 3]), QA5_G], gap=1.8), fig_key=figs.row([TAB([-2, 1, 3], [-7, -1, 3]), QA5_K], gap=1.8),
             answer="The y-intercept is −3.", why="From (1, −1) to (3, 3) is up 4 for 2 to the right: slope 2. One step back from (1, −1) gives (0, −3).",
             check=("many", table_of("2*u - 3", [-2, 1, 3], [-7, -1, 3]), ("eq", "-1 - (" + slope(("1", "-1"), ("3", "3")) + ")", "-3")), space=0.9),
        dict(heading="For questions 6 and 7, graph the situation on the grid."),
        dict(stem="A drone is 100 feet above the ground and rises 50 feet every minute. Graph its height versus time.",
             fig=QA6_G, fig_key=QA6_K,
             answer="The line from (0, 100) through (2, 200) to (6, 400)", why="The start, 100, is the y-intercept; the slope is 50: 100 + 50(2) = 200 and 100 + 50(6) = 400.",
             check=table_of("50*u + 100", [0, 2, 6], [100, 200, 400]), space=0.9),
        dict(stem="A bag holds 48 pounds of mulch, and a gardener spreads 12 pounds every minute. Graph the pounds left in the bag versus time.",
             fig=QA7_G, fig_key=QA7_K,
             answer="The line from (0, 48) to (4, 0)", why="The start, 48, is the y-intercept; the slope is −12: 48 − 12(2) = 24 and 48 − 12(4) = 0.",
             check=table_of("-12*u + 48", [0, 2, 4], [48, 24, 0]), space=0.9),
        dict(heading="An equation in another form."),
        dict(stem="Complete a table for $2x + y = 10$ at $x = 0$, $2$ and $5$, then graph the line.",
             fig=QA8_G, fig_key=QA8_K,
             answer="10, 6, 0; the line through (0, 10) and (5, 0)", why="2(0) + y = 10, so y = 10; 4 + y = 10, so y = 6; 10 + y = 10, so y = 0.",
             check=std_table(2, 10, [0, 2, 5], [10, 6, 0]), space=0.9),
        dict(heading="Read the graph."),
        dict(stem="The graph shows the length of an icicle, in centimeters, versus the time, in hours. How long was the icicle at the start, and how fast does it grow?",
             fig=QA9,
             answer="10 centimeters at the start; it grows 5 centimeters per hour.", why="The line starts at (0, 10); from (0, 10) to (2, 20) it rises 10 in 2 hours: 10 ÷ 2 = 5.",
             check=("many", ("eq", slope(("0", "10"), ("2", "20")), "5"), sat("5*u + 10", "0", "10")), space=0.5),
        dict(heading="Choose one."),
        dict(stem="A table of a linear relationship has the x-values 2, 4, 6 and the y-values 4, 5, 6. Where does its line cross the y-axis?",
             choices=["At 0", "At 3", "At 0.5", "At 4"], correct=1, answer="B",
             why="The slope is 1/2. One step of 2 back from (2, 4) to x = 0: 4 − 1 = 3.",
             check=("many", table_of("F(1,2)*u + 3", [2, 4, 6], [4, 5, 6]), ("eq", "(F(1,2)*" + X + " + 3).subs(" + X + ", 0)", "3"),
                    fails("F(1,2)*u + 3", "0", "4"), fails("F(1,2)*u + 3", "0", "F(1,2)"), fails("F(1,2)*u + 3", "0", "0")),
             errors={"A": "every line taken to start at the origin [standing decision 3: a linear relationship is proportional only through the origin]", "C": "the slope read as the y-intercept [B1G-M, AR.3.4: swapping m and b]", "D": "the first y-value read as the y-intercept, at x = 2 and not x = 0 [Notes II: the y-intercept is the value of y when x is 0]"}),
        dict(stem="A bucket holds 4 liters, and a faucet adds 5 liters every minute. Which two points are on the graph of the liters in the bucket versus the minutes?",
             choices=["$(0, 4)$ and $(2, 14)$", "$(0, 4)$ and $(2, -6)$", "$(0, 5)$ and $(2, 13)$", "$(0, 0)$ and $(2, 10)$"],
             correct=0, answer="A",
             why="The start, 4, is the y-intercept: (0, 4). After 2 minutes, 4 + 5(2) = 14.",
             check=("many", table_of("5*u + 4", [0, 2], [4, 14]), fails("5*u + 4", "0", "5"), fails("5*u + 4", "0", "0"),
                    fails("5*u + 4", "2", "-6"), table_of("4*u + 5", [0, 2], [5, 13]), table_of("-5*u + 4", [0, 2], [4, -6])),
             errors={"B": "the 5 liters taken away, not added [B1G-M, AR.3.4: inverting the direction of the rise]", "C": "the start and the rate exchanged [B1G-M, AR.3.4: swapping m and b]", "D": "the start left out [Notes II: the start is the y-intercept]"}),
        dict(heading="Find the missing number."),
        dict(stem="The points $(0, 1)$, $(3, 7)$ and $(5, □)$ are on one line. Find the missing number.", answer="11",
             why="The slope is (7 − 1) ÷ 3 = 2, so y = 2x + 1, and 2(5) + 1 = 11.",
             check=("many", ("eq", slope(("0", "1"), ("3", "7")), "2"), ("eq", "2*5 + 1", "11")), space=0.6),
    ],

    te=dict(
        must="Students graph a two-variable linear equation from a written description, a table or an equation in slope-intercept form, in mathematical and real-world contexts.",
        must_not="Point-slope form and standard form are not expectations of the benchmark, so the one equation in another form today is graphed from a table of values and is never on the test.",
        read_first=[
            "Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §10.06). Math Nation was read for scope only, and nothing is taken from it.",
            "Every line is graphed one of two ways: from a description, the start is the y-intercept and the rate is the slope; from a table or another form, plot the pairs and draw the line through them. A real-world graph starts at x = 0 and stops where the story ends.",
            "Right after Example 1, hand out the Independent Set: Your Turn 1 is its question 1 (y = 2x − 5), and every student completes the table and draws the line on the handout's grid while you circulate. The boards read a table, a description or a graph; nobody draws a graph on a whiteboard. The key draws each line on the student's own grid.",
            "Changed from the outline: the boat on whiteboard question 7 has 4 seats, not 6, because 6 is also the answer's number of hours; board 4's kitten gains 0.5 pounds, plural with a decimal."],
        materials="Whiteboards and markers, rulers, and the Independent Set, one per student, handed out at Example 1's Your Turn so that question 1 is drawn in class.",
        variation="Whiteboard questions 1 and 2 work from an equation and a table; 3 votes on four graphs of one story; 4 writes a description's points; 5 votes on a table's y-intercept when the table has no x = 0. The pattern breaks at 6, an equation in another form. 7 carries the boat's seats as the extra number; 8 finds a missing number on a line; 9 is written. The set: question 1 drawn in class, then a table, a rising story, a falling story, an equation in another form, and a graph read for its start and rate.",
        audit=["Every table value, slope and y-intercept is re-derived by sympy at build time from its equation or its two points; every graph is drawn from its equation by u10/figs10.py, which refuses a point marked on a line it is not on."],
        changes=["Math Nation 10.6 was read for scope only; the lesson is built from the benchmark and the unit's plan."],
    ),
)
