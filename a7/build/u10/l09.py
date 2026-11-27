# A7 10.09 Writing Equations of Lines (MA.8.AR.3.3). Built from the unit's Lesson Outlines, section 10.09.
# Figures from u10/figs10.py. No vocabulary slide: every word is carried over (slope, y-intercept, slope-intercept form).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs10 as figs
S = figs.slide

X = "sp.Symbol('u', real=True)"


def _u(e):
    import re
    return re.sub(r"\bu\b", X, e)


def sat(rhs, x, y):
    """(x, y) makes y = rhs true (rhs in u)."""
    return ("true", "sp.simplify((" + _u(rhs) + ").subs(" + X + ", " + x + ") - (" + y + ")) == 0")


def fails(rhs, x, y):
    """(x, y) makes y = rhs false."""
    return ("true", "sp.simplify((" + _u(rhs) + ").subs(" + X + ", " + x + ") - (" + y + ")) != 0")


def through(rhs, *pts):
    """The line y = rhs passes through every point given."""
    return ("many",) + tuple(sat(rhs, str(a), str(b)) for a, b in pts)


def slope(p, q, m):
    """The change in y divided by the change in x from p to q is m."""
    return ("eq", "sp.Rational(" + str(q[1]) + " - (" + str(p[1]) + "), " + str(q[0]) + " - (" + str(p[0]) + "))", m)


def misses(rhs, *pts):
    """The line y = rhs misses at least one of the points: it is not the line through them."""
    return ("true", " or ".join("(sp.simplify((" + _u(rhs) + ").subs(" + X + ", " + str(a) + ") - (" + str(b) + ")) != 0)"
                                for a, b in pts))


H = Fr(1, 2)


def BP(xr, yr, **kw):
    """A board's graph, drawn and sized for a question slide (4.2 in, 18 pt)."""
    return S(figs.plane(xr, yr, inches=4.2, pt=18, **kw), inches=4.2, pt=18, reserve=0.75)


def BPA(xr, yr, **kw):
    return S(figs.plane(xr, yr, inches=4.2, pt=18, **kw), inches=4.2, pt=18, reserve=0.95)


def TB(xs, ys, reserve=0.75):
    """A board's table, at slide size."""
    return S(figs.table([(xs, ys)], cw=1.6, rh=1.3), inches=6.4, pt=20, reserve=reserve)


def GP(xr, yr, lines, points):
    """A paper graph: the line drawn, unlabeled, its two points named."""
    return figs.plane(xr, yr, lines=lines, points=points, inches=2.6)


def PT(xs, ys):
    return figs.table([(xs, ys)], inches=4.0)


# ---- notes and examples
NOTES1 = S(figs.plane((-1, 7), (0, 4), lines=[(-H, 3, "")], points=[(0, 3), (4, 1), (2, 2, "")], inches=4.0, pt=18),
           inches=4.0, pt=18, reserve=1.0)
NOTES2 = S(figs.table([([0, 4, 8], [-5, -2, 1])], cw=1.6, rh=1.3), inches=5.0, pt=20, reserve=1.6)
EX1_T = figs.table([([2, 5, 8], [13, 7, 1])], cw=1.6, rh=1.3)
EX1 = S(EX1_T, inches=5.4, pt=20, reserve=0.9)
EX1W = S(EX1_T, inches=3.6, pt=16, reserve=0.9)
YT1_T = figs.table([([4, 6, 10], [16, 11, 1])], cw=1.6, rh=1.3)
YT1 = S(YT1_T, inches=5.4, pt=20, reserve=0.9)
YT1A = S(YT1_T, inches=3.6, pt=16, reserve=0.9)

# ---- the boards
P3 = dict(lines=[(2, -2, "")], points=[(0, -2), (3, 4)])
T4 = ([-2, 0, 2], [10, 4, -2])
T5 = ([1, 2, 3], [6, 11, 16])


L = dict(
    code="10.09", unit=10, lesson_no=9,
    align="=",
    title="Writing Equations of Lines",
    unit_title="Linear Relationships",
    benchmark="MA.8.AR.3.3",
    benchmark_text="Given a table, graph or written description of a linear relationship, write an equation in slope-intercept form.",
    target="I can write the equation of a line in slope-intercept form from its graph, from a table or from two points.",
    essential="When the y-intercept is not shown, how can one point and the slope tell you what it is?",
    building_on="Lesson 10.07+08 read the slope and the y-intercept of a line as a rate and a start. Lessons 10.02+03 found a slope from a graph, a table or two points, and 10.05 graphed y = mx + b from its slope and y-intercept. Lesson 11.01 solved two-step equations like 11 = 3(2) + b.",
    working_toward="Lesson 10.10 writes the equation of a line from a story, in the story's own letters. The unit test on Thursday asks for four equations in slope-intercept form, and Algebra 1 (MA.912.AR.2.2) writes equations of lines from the same information.",
    vocab=[],
    vocab_slide=False,
    ixl=["Write a linear equation from a graph — WHM", "Write a linear function from a table — UYY",
         "Write a linear equation from a slope and a point — VKP", "Write a linear equation from two points — 2R9"],
    closure="Whiteboard question 9 is written work, and it is the exit evidence. A full answer says that Sam exchanged the slope and the y-intercept: the slope is (17 − 7) ÷ (2 − 0) = 5 and the y-intercept is 7, so the equation is y = 5x + 7.",

    mtr=[("MTR.2.1", "Students write one equation from a graph, from a table and from two points, and see that the same two numbers, m and b, come out of each."),
         ("MTR.4.1", "On whiteboard questions 3 and 5, students convince a neighbor and then vote again."),
         ("MTR.6.1", "Every equation is checked with a point that was not used to write it.")],
    hoq=[("Why does any point on the line give the same b when you substitute it?", "DOK 2"),
         ("Whiteboard questions 1 and 2 have the same slope. Why does only the second need a step to find b?", "DOK 2"),
         ("A table has no x = 0. How could you find y at x = 0 without substituting?", "DOK 3")],
    differentiation=[
        ("ESE / 504", "Students keep a printed card with the three steps: find m, substitute a point and solve for b, then check with another point."),
        ("ELL", "The words slope, y-intercept and substitute stay on the board all period, each beside its symbol: m, b and an arrow from a point into the equation."),
        ("Enrichment", "Students who finish whiteboard question 8 early write the equation of a line that passes through (2, −1) and has the same y-intercept as y = 4x − 6, and check it with the point.")],

    warmup=[
        dict(stem="c = 3n + 8 gives the cost c, in dollars, of bowling n games. What does the 8 mean?",
             answer="The cost is \\$8 before the first game.",
             check=("eq", "3*0 + 8", "8")),
        dict(stem="What are the slope and the y-intercept of  $y = 9 - 3x$?", answer="−3 and 9",
             check=("many", ("eq", "sp.diff(9 - 3*" + X + ", " + X + ")", "-3"), ("eq", "9 - 3*0", "9"))),
        dict(stem="Pump A fills 45 gallons in 3 minutes. Pump B fills 64 gallons in 4 minutes. Which pump is faster?",
             answer="Pump B (16 gallons per minute versus 15)",
             check=("many", ("eq", "F(64, 4)", "16"), ("eq", "F(45, 3)", "15"), ("true", "F(64, 4) > F(45, 3)"))),
        dict(stem="Solve for b:  $11 = 3(2) + b$", answer="b = 5",
             check=("eq", "sp.solve(sp.Eq(11, 3*2 + sp.Symbol('bb', real=True)), sp.Symbol('bb', real=True))[0]", "5")),
    ],

    notes=[
        dict(numeral="I", head="From a graph: read b, then find m", min=3,
             fig=NOTES1,
             math=["$b = 3 \\qquad m = \\frac{1 - 3}{4 - 0} = -\\frac{1}{2} \\qquad y = -\\frac{1}{2}x + 3$"],
             items2=["Check with $(2, 2)$:   $-1 + 3 = 2$"],
             letters=False),
        dict(numeral="II", head="From a table that shows x = 0", min=3,
             fig=NOTES2,
             math=["$b = -5 \\qquad m = \\frac{-2 - (-5)}{4 - 0} = \\frac{3}{4} \\qquad y = \\frac{3}{4}x - 5$"],
             items2=["The y-intercept is the value of y when x is 0."],
             letters=False),
        dict(numeral="III", head="No y-intercept in sight", min=3,
             items=["**Substitute a point and solve for b.**", "The line passes through $(2, 3)$ and $(6, 11)$."],
             math=["$m = \\frac{11 - 3}{6 - 2} = \\frac{8}{4} = 2$", "$3 = 2(2) + b$", "$b = -1$"],
             items2=["$y = 2x - 1$.   Check with $(6, 11)$:   $12 - 1 = 11$"],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=1,
             prompt=["The table shows a linear relationship. It has no x = 0."], fig=EX1,
             ask="Write its equation in slope-intercept form.",
             worked=[dict(min=3,
                          rows=[("m = \\frac{7 - 13}{5 - 2} = \\frac{-6}{3} = -2", "change in y over change in x"),
                                ("13 = -2(2) + b", "substitute (2, 13)"),
                                ("13 = -4 + b", ""),
                                ("b = 17", "add 4 to both sides"),
                                ("y = -2x + 17", "check (8, 1):  −16 + 17 = 1")],
                          fig=EX1W, answer="y = −2x + 17")],
             check=("many", slope((2, 13), (5, 7), "-2"), through("-2*u + 17", (2, 13), (5, 7), (8, 1))),
             your_turn=dict(min=3,
                            prompt=["The table shows a linear relationship.", "Write its equation in slope-intercept form."],
                            fig=YT1, fig_a=YT1A, ask="",
                            steps=["Slope:  $\\frac{11 - 16}{6 - 4} = -\\frac{5}{2}$",
                                   "Substitute $(4, 16)$:  $16 = -\\frac{5}{2}(4) + b$",
                                   "Solve for b:  $16 = -10 + b$,  so  $b = 26$",
                                   "Check $(10, 1)$:  $-25 + 26 = 1$",
                                   "The equation:  $y = -\\frac{5}{2}x + 26$"],
                            answer="y = −(5/2)x + 26"),
             yt_check=("many", slope((4, 16), (6, 11), "F(-5, 2)"),
                       through("-F(5,2)*u + 26", (4, 16), (6, 11), (10, 1)))),
        dict(title="Example 2", min_q=1,
             prompt=["A line passes through (−3, 7) and (3, 3)."], ask="Write its equation in slope-intercept form.",
             worked=[dict(min=2,
                          rows=[("m = \\frac{3 - 7}{3 - (-3)} = \\frac{-4}{6} = -\\frac{2}{3}", "change in y over change in x"),
                                ("3 = -\\frac{2}{3}(3) + b", "substitute (3, 3):  3 = −2 + b"),
                                ("b = 5", "add 2 to both sides"),
                                ("y = -\\frac{2}{3}x + 5", "check (−3, 7):  2 + 5 = 7")],
                          answer="y = −(2/3)x + 5")],
             check=("many", slope((-3, 7), (3, 3), "F(-2, 3)"), through("-F(2,3)*u + 5", (-3, 7), (3, 3))),
             # repeat_ok: rule D matches only small digits (2, 4, 7) shared with Example 1; this line appears nowhere above.
             your_turn=dict(repeat_ok=True, min=3,
                            prompt=["A line passes through (−4, 7) and (2, −2).", "Write its equation in slope-intercept form."],
                            ask="",
                            steps=["Slope:  $\\frac{-2 - 7}{2 - (-4)} = \\frac{-9}{6} = -\\frac{3}{2}$",
                                   "Substitute $(2, -2)$:  $-2 = -\\frac{3}{2}(2) + b$",
                                   "Solve for b:  $-2 = -3 + b$,  so  $b = 1$",
                                   "Check $(-4, 7)$:  $6 + 1 = 7$",
                                   "The equation:  $y = -\\frac{3}{2}x + 1$"],
                            answer="y = −(3/2)x + 1"),
             yt_check=("many", slope((-4, 7), (2, -2), "F(-3, 2)"), through("-F(3,2)*u + 1", (-4, 7), (2, -2)))),
    ],

    # The round: a slope and the y-intercept (1); the same slope and a point off the y-axis (2, one thing changes);
    # the graph diagnostic (3); a table through x = 0 with a negative slope (4); the table diagnostic with no x = 0 (5);
    # two points (6); the extra number, a grid's width (7); backwards, the slope missing (8); Sam's exchange, written (9).
    whiteboard=[
        # repeat_ok: rule D matches only small digits shared by coordinates and answers; this line appears nowhere above.
        dict(repeat_ok=True, text=["A line has the slope 4 and passes through (0, −6).", "**Write its equation."],
             steps=["$(0, -6)$ is on the y-axis:  $b = -6$",
                    "The equation:  $y = 4x - 6$"],
             answer="y = 4x − 6",
             check=("many", sat("4*u - 6", "0", "-6"), ("eq", "sp.diff(4*" + X + " - 6, " + X + ")", "4")),
             wrong="y = −6x + 4 — the slope and the y-intercept exchanged [Florida B1G-M, AR.3.3: swapping m and b]"),
        dict(text=["A line has the slope 4 and passes through (2, −6).", "**Write its equation."],
             steps=["Substitute $(2, -6)$:  $-6 = 4(2) + b$",
                    "Solve for b:  $-6 = 8 + b$,  so  $b = -14$",
                    "The equation:  $y = 4x - 14$"],
             answer="y = 4x − 14",
             check=("many", sat("4*u - 14", "2", "-6"), ("eq", "sp.diff(4*" + X + " - 14, " + X + ")", "4"),
                    fails("4*u - 6", "2", "-6"), fails("4*u + 2", "2", "-6")),
             wrong="y = 4x − 6 — the point's y taken as b, though the point is not on the y-axis [Notes III: substitute a point and solve for b]; y = 4x + 2 — 8 added to −6 instead of subtracted [Notes III: substitute a point and solve for b]"),
        # repeat_ok: rule D matches only small digits shared by coordinates and answers; this line appears nowhere above.
        dict(repeat_ok=True, kind="mc", text=["**The line is graphed. Which equation is the line's?"],
             qtext="A line passes through (0, −2) and (3, 4), as graphed. Which equation is the line's?",
             fig=BP((-1, 4), (-3, 5), **P3), fig_a=BPA((-1, 4), (-3, 5), **P3),
             steps=["$b = -2$;   slope:  $\\frac{4 - (-2)}{3 - 0} = \\frac{6}{3} = 2$",
                    "Check $(3, 4)$:  $2(3) - 2 = 4$"],
             choices=["$y = 2x + 4$", "$y = -2x + 2$", "$y = 2x - 2$", "$y = \\frac{1}{2}x - 2$"], correct=2,
             answer="C — y = 2x − 2",
             errors={"A": "the other point's y-value, 4, taken as b [Notes I: b is where the line crosses the y-axis]", "B": "the slope and the y-intercept exchanged [Florida B1G-M, AR.3.3: swapping m and b]", "D": "the slope turned over: the change in x over the change in y [Florida B1G-M, AR.3.3: inverted slope]"},
             check=("many", through("2*u - 2", (0, -2), (3, 4)), slope((0, -2), (3, 4), "2"),
                    misses("-2*u + 2", (0, -2), (3, 4)), misses("F(1,2)*u - 2", (0, -2), (3, 4)), misses("2*u + 4", (0, -2), (3, 4)))),
        dict(text=["**The table shows a linear relationship. Write its equation."],
             qtext="A table of a linear relationship: x −2, 0, 2; y 10, 4, −2. Write the equation of its line.",
             fig=TB(*T4), fig_a=TB(*T4, reserve=0.95),
             steps=["At $x = 0$, $y = 4$:  $b = 4$",
                    "Slope:  $\\frac{-2 - 4}{2 - 0} = \\frac{-6}{2} = -3$",
                    "The equation:  $y = -3x + 4$"],
             answer="y = −3x + 4",
             check=("many", slope((0, 4), (2, -2), "-3"), through("-3*u + 4", (-2, 10), (0, 4), (2, -2))),
             wrong="y = 3x + 4 — the sign of the slope lost: y falls as x rises [Florida B1G-M, AR.3.3: positive and negative slopes]; y = −3x + 10 — the first y-value taken as b [Notes II: the y-intercept is the value of y when x is 0]"),
        dict(kind="mc", text=["**The table shows a linear relationship. Which is its equation?"],
             qtext="A table of a linear relationship: x 1, 2, 3; y 6, 11, 16. Which equation is its line's?",
             fig=TB(*T5), fig_a=TB(*T5, reserve=0.95),
             steps=["Slope:  $\\frac{11 - 6}{2 - 1} = 5$",
                    "Substitute $(1, 6)$:  $6 = 5(1) + b$,  so  $b = 1$",
                    "Check $(3, 16)$:  $5(3) + 1 = 16$"],
             choices=["$y = 5x + 1$", "$y = x + 5$", "$y = \\frac{1}{5}x + 1$", "$y = 5x + 6$"], correct=0,
             answer="A — y = 5x + 1",
             errors={"B": "the slope and the y-intercept exchanged [Florida B1G-M, AR.3.3: swapping m and b]", "C": "the change in x over the change in y [Florida B1G-M, AR.3.3: inverted slope]", "D": "the first y-value, 6, taken as b, though the table has no x = 0 [Notes III: substitute a point and solve for b]"},
             check=("many", slope((1, 6), (2, 11), "5"), through("5*u + 1", (1, 6), (2, 11), (3, 16)),
                    misses("5*u + 6", (1, 6), (2, 11), (3, 16)), misses("F(1,5)*u + 1", (1, 6), (2, 11), (3, 16)),
                    misses("u + 5", (1, 6), (2, 11), (3, 16)))),
        dict(text=["**Write the equation of the line through (1, 2) and (3, 10)."],
             steps=["Slope:  $\\frac{10 - 2}{3 - 1} = \\frac{8}{2} = 4$",
                    "Substitute $(1, 2)$:  $2 = 4(1) + b$,  so  $b = -2$",
                    "Check $(3, 10)$:  $4(3) - 2 = 10$",
                    "The equation:  $y = 4x - 2$"],
             answer="y = 4x − 2",
             check=("many", slope((1, 2), (3, 10), "4"), through("4*u - 2", (1, 2), (3, 10))),
             wrong="y = 4x + 2 — the first point's y taken as b [Notes III: substitute a point and solve for b]; y = (1/4)x + 7/4 — the change in x over the change in y [Florida B1G-M, AR.3.3: inverted slope]"),
        # repeat_ok: rule D matches only small digits shared by coordinates and answers; this line appears nowhere above.
        dict(repeat_ok=True, text=["On a grid 20 squares wide, a line crosses the y-axis at 6", "and the x-axis at 4.",
                   "**Write the line's equation."],
             unneeded="20",
             steps=["The line passes through $(0, 6)$ and $(4, 0)$:  $b = 6$",
                    "Slope:  $\\frac{0 - 6}{4 - 0} = -\\frac{6}{4} = -\\frac{3}{2}$",
                    "The equation:  $y = -\\frac{3}{2}x + 6$"],
             answer="y = −(3/2)x + 6",
             check=("many", slope((0, 6), (4, 0), "F(-3, 2)"), through("-F(3,2)*u + 6", (0, 6), (4, 0))),
             wrong="y = −(3/10)x + 6 — the grid's width, 20, used as the x-axis crossing [an extra number, included on purpose]; y = −(2/3)x + 6 — the slope turned over [Florida B1G-M, AR.3.3: inverted slope]; y = 4x + 6 — the x-axis crossing taken as the slope [Notes I: slope is the change in y divided by the change in x]"),
        dict(text=["The line $y = □x + 5$ passes through (2, −1).", "**Find the missing number."],
             steps=["Substitute $(2, -1)$:  $-1 = □(2) + 5$",
                    "Subtract 5:  $-6 = □(2)$",
                    "Divide by 2:  $□ = -3$"],
             answer="−3",
             check=("many", ("eq", "F(-1 - 5, 2)", "-3"), sat("-3*u + 5", "2", "-1")),
             wrong="3 — the sign lost in −1 − 5 [Notes III: substitute a point and solve]; 2 — (−1 + 5) ÷ 2, the 5 added instead of subtracted [Notes III: substitute a point and solve]"),
        # repeat_ok: rule D matches only small digits shared by coordinates and answers; this line appears nowhere above.
        dict(repeat_ok=True, kind="written", text=["For the line through (0, 7) and (2, 17), Sam writes y = 7x + 5.",
                                   "**What is Sam's mistake? Write the correct equation."],
             qtext="For the line through (0, 7) and (2, 17), Sam writes y = 7x + 5. What is Sam's mistake? Write the correct equation.",
             steps=["$(0, 7)$ is on the y-axis:  $b = 7$",
                    "Slope:  $\\frac{17 - 7}{2 - 0} = \\frac{10}{2} = 5$",
                    "Sam exchanged them:  $y = 5x + 7$"],
             answer="Sam exchanged m and b: y = 5x + 7.",
             check=("many", slope((0, 7), (2, 17), "5"), through("5*u + 7", (0, 7), (2, 17)), misses("7*u + 5", (0, 7), (2, 17))),
             wrong="'Sam is right' — 7 and 5 both appear, so the equation looks right [Florida B1G-M, AR.3.3: swapping m and b]; y = 10x + 7 — the change in y alone taken as the slope [Notes I: slope is the change in y divided by the change in x]"),
    ],

    # The six: from a graph that shows the y-intercept (1), from a graph with a negative fraction slope (2), from a table
    # that shows x = 0 (3, its steps unequal), from a table with no x = 0 (4, unequal steps), from a slope and a point (5),
    # from two points (6).
    independent=[
        # repeat_ok: rule D matches only small digits shared by coordinates and answers; this line appears nowhere above.
        dict(repeat_ok=True, stem="The graphed line passes through $(0, 5)$ and $(2, -1)$. Write its equation in slope-intercept form.",
             fig=GP((-1, 4), (-2, 6), [(-3, 5, "")], [(0, 5), (2, -1)]),
             answer="y = −3x + 5", why="b = 5. Slope: (−1 − 5) ÷ (2 − 0) = −6 ÷ 2 = −3. So y = −3x + 5.",
             check=("many", slope((0, 5), (2, -1), "-3"), through("-3*u + 5", (0, 5), (2, -1))), space=0.6),
        # repeat_ok: rule D matches only small digits shared by coordinates and answers; this line appears nowhere above.
        dict(repeat_ok=True, stem="The graphed line passes through $(0, -1)$ and $(3, -3)$. Write its equation in slope-intercept form.",
             fig=GP((-4, 5), (-5, 3), [(Fr(-2, 3), -1, "")], [(0, -1), (3, -3)]),
             answer="y = −(2/3)x − 1", why="b = −1. Slope: (−3 − (−1)) ÷ (3 − 0) = −2/3. So y = −(2/3)x − 1.",
             check=("many", slope((0, -1), (3, -3), "F(-2, 3)"), through("-F(2,3)*u - 1", (0, -1), (3, -3))), space=0.6),
        # repeat_ok: rule D matches only small digits shared by coordinates and answers; this line appears nowhere above.
        dict(repeat_ok=True, stem="In a linear relationship, y is 5, 2, −1 and −7 when x is −2, 0, 2 and 6. Write its equation in slope-intercept form.",
             fig=PT([-2, 0, 2, 6], [5, 2, -1, -7]),
             answer="y = −(3/2)x + 2", why="At x = 0, y = 2, so b = 2. Slope: (−1 − 2) ÷ (2 − 0) = −3/2. Check (6, −7): −9 + 2 = −7.",
             check=("many", slope((0, 2), (2, -1), "F(-3, 2)"), through("-F(3,2)*u + 2", (-2, 5), (0, 2), (2, -1), (6, -7))), space=0.6),
        dict(stem="In a linear relationship, y is 2, 12, 17 and 32 when x is 1, 3, 4 and 7. Write its equation in slope-intercept form.",
             fig=PT([1, 3, 4, 7], [2, 12, 17, 32]),
             answer="y = 5x − 3", why="Slope: (12 − 2) ÷ (3 − 1) = 5. Substitute (1, 2): 2 = 5(1) + b, so b = −3. Check (7, 32): 35 − 3 = 32.",
             check=("many", slope((1, 2), (3, 12), "5"), through("5*u - 3", (1, 2), (3, 12), (4, 17), (7, 32))), space=0.6),
        # repeat_ok: rule D matches only small digits shared by coordinates and answers; this line appears nowhere above.
        dict(repeat_ok=True, stem="A line has the slope $-\\frac{1}{2}$ and passes through $(6, 1)$. Write its equation in slope-intercept form.",
             answer="y = −(1/2)x + 4", why="Substitute (6, 1): 1 = −(1/2)(6) + b = −3 + b, so b = 4.",
             check=("many", sat("-F(1,2)*u + 4", "6", "1"), ("eq", "sp.diff(-F(1,2)*" + X + " + 4, " + X + ")", "F(-1, 2)")), space=0.6),
        # repeat_ok: rule D matches only small digits shared by coordinates and answers; this line appears nowhere above.
        dict(repeat_ok=True, stem="Write the equation of the line through $(-4, -1)$ and $(4, 5)$ in slope-intercept form.",
             answer="y = (3/4)x + 2", why="Slope: (5 − (−1)) ÷ (4 − (−4)) = 6/8 = 3/4. Substitute (4, 5): 5 = 3 + b, so b = 2. Check (−4, −1): −3 + 2 = −1.",
             check=("many", slope((-4, -1), (4, 5), "F(3, 4)"), through("F(3,4)*u + 2", (-4, -1), (4, 5))), space=0.6),
    ],

    # Bank: two graphs that show b (1–2), two tables, with and without x = 0 (3–4), a slope and a point (5–6), two
    # points, the first a proportional line (7–8), backwards (9), the graph and table diagnostics (10–11), and a
    # select-all of the equations of one line, b written first in one (12). The additional bank mirrors it.
    bank=[
        dict(heading="For questions 1 and 2, write the equation of the graphed line in slope-intercept form."),
        dict(stem="The line passes through the two marked points.",
             fig=GP((-1, 5), (-3, 3), [(Fr(3, 4), -2, "")], [(0, -2), (4, 1)]),
             answer="y = (3/4)x − 2", why="b = −2. Slope: (1 − (−2)) ÷ (4 − 0) = 3/4.",
             check=("many", slope((0, -2), (4, 1), "F(3, 4)"), through("F(3,4)*u - 2", (0, -2), (4, 1))), space=0.5),
        dict(stem="The line passes through the two marked points.",
             fig=GP((-1, 5), (-4, 2), [(-H, -1, "")], [(0, -1), (4, -3)]),
             answer="y = −(1/2)x − 1", why="b = −1. Slope: (−3 − (−1)) ÷ (4 − 0) = −2/4 = −1/2.",
             check=("many", slope((0, -1), (4, -3), "F(-1, 2)"), through("-F(1,2)*u - 1", (0, -1), (4, -3))), space=0.5),
        dict(heading="For questions 3 and 4, the table shows a linear relationship. Write its equation in slope-intercept form."),
        dict(stem="The table has a column for x = 0.", fig=PT([0, 2, 6], [7, 1, -11]),
             answer="y = −3x + 7", why="At x = 0, y = 7, so b = 7. Slope: (1 − 7) ÷ (2 − 0) = −3. Check (6, −11): −18 + 7 = −11.",
             check=("many", slope((0, 7), (2, 1), "-3"), through("-3*u + 7", (0, 7), (2, 1), (6, -11))), space=0.5),
        dict(stem="The table has no column for x = 0.", fig=PT([2, 3, 6], [5, 9, 21]),
             answer="y = 4x − 3", why="Slope: (9 − 5) ÷ (3 − 2) = 4. Substitute (2, 5): 5 = 8 + b, so b = −3. Check (6, 21): 24 − 3 = 21.",
             check=("many", slope((2, 5), (3, 9), "4"), through("4*u - 3", (2, 5), (3, 9), (6, 21))), space=0.5),
        dict(heading="For questions 5 and 6, write the equation of the line in slope-intercept form."),
        dict(stem="A line has the slope $-\\frac{2}{3}$ and passes through $(6, -1)$.",
             answer="y = −(2/3)x + 3", why="Substitute (6, −1): −1 = −(2/3)(6) + b = −4 + b, so b = 3.",
             check=("many", sat("-F(2,3)*u + 3", "6", "-1"), ("eq", "sp.diff(-F(2,3)*" + X + " + 3, " + X + ")", "F(-2, 3)")), space=0.5),
        dict(stem="A line has the slope 5 and passes through $(-2, 1)$.",
             answer="y = 5x + 11", why="Substitute (−2, 1): 1 = 5(−2) + b = −10 + b, so b = 11.",
             check=("many", sat("5*u + 11", "-2", "1"), ("eq", "sp.diff(5*" + X + " + 11, " + X + ")", "5")), space=0.5),
        dict(heading="For questions 7 and 8, write the equation of the line through the two points in slope-intercept form."),
        dict(stem="$(-4, 6)$ and $(4, -6)$",
             answer="y = −(3/2)x", why="Slope: (−6 − 6) ÷ (4 − (−4)) = −12/8 = −3/2. Substitute (4, −6): −6 = −6 + b, so b = 0.",
             check=("many", slope((-4, 6), (4, -6), "F(-3, 2)"), through("-F(3,2)*u", (-4, 6), (4, -6))), space=0.5),
        dict(stem="$(1, 7)$ and $(4, 13)$",
             answer="y = 2x + 5", why="Slope: (13 − 7) ÷ (4 − 1) = 6/3 = 2. Substitute (1, 7): 7 = 2 + b, so b = 5.",
             check=("many", slope((1, 7), (4, 13), "2"), through("2*u + 5", (1, 7), (4, 13))), space=0.5),
        dict(heading="Find the missing number."),
        dict(stem="The line $y = □x - 4$ passes through $(3, -13)$. Find the missing number.",
             answer="−3", why="3 times the missing number, minus 4, is −13. So 3 times it is −9, and the missing number is −3.",
             check=("many", ("eq", "F(-13 + 4, 3)", "-3"), sat("-3*u - 4", "3", "-13")), space=0.5),
        dict(heading="Choose one."),
        dict(stem="Which equation is the graphed line's?",
             fig=GP((-2, 3), (-3, 5), [(4, -1, "")], [(0, -1), (1, 3)]),
             choices=["$y = -x + 4$", "$y = 4x + 3$", "$y = \\frac{1}{4}x - 1$", "$y = 4x - 1$"], correct=3, answer="D",
             why="b = −1. Slope: (3 − (−1)) ÷ (1 − 0) = 4.",
             check=("many", through("4*u - 1", (0, -1), (1, 3)), misses("-u + 4", (0, -1), (1, 3)),
                    misses("F(1,4)*u - 1", (0, -1), (1, 3)), misses("4*u + 3", (0, -1), (1, 3))),
             errors={"A": "the slope and the y-intercept exchanged [Florida B1G-M, AR.3.3: swapping m and b]", "B": "the other point's y-value, 3, taken as b [Notes I: b is where the line crosses the y-axis]", "C": "the slope turned over [Florida B1G-M, AR.3.3: inverted slope]"}),
        dict(stem="The table shows a linear relationship. Which is its equation?",
             fig=PT([1, 2, 3], [-1, 1, 3]),
             choices=["$y = \\frac{1}{2}x - 3$", "$y = 2x - 3$", "$y = 2x - 1$", "$y = -3x + 2$"], correct=1, answer="B",
             why="Slope: (1 − (−1)) ÷ (2 − 1) = 2. Substitute (1, −1): −1 = 2 + b, so b = −3.",
             check=("many", through("2*u - 3", (1, -1), (2, 1), (3, 3)), misses("2*u - 1", (1, -1), (2, 1), (3, 3)),
                    misses("-3*u + 2", (1, -1), (2, 1), (3, 3)), misses("F(1,2)*u - 3", (1, -1), (2, 1), (3, 3))),
             errors={"A": "the change in x over the change in y [Florida B1G-M, AR.3.3: inverted slope]", "C": "the first y-value taken as b, though the table has no x = 0 [Notes III: substitute a point and solve for b]", "D": "the slope and the y-intercept exchanged [Florida B1G-M, AR.3.3: swapping m and b]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the equations of the line through $(-2, 7)$ and $(2, 1)$.",
             choices=["$y = -\\frac{3}{2}x + 7$", "$y = 4x - \\frac{3}{2}$", "$y = 4 - \\frac{3}{2}x$", "$y = \\frac{3}{2}x + 4$", "$y = -\\frac{3}{2}x + 4$"],
             correct=[2, 4], answer="C, E",
             why="Slope: (1 − 7) ÷ (2 − (−2)) = −6/4 = −3/2. Substitute (2, 1): 1 = −3 + b, so b = 4. C and E are the same equation, with b written first in C.",
             check=("many", through("-F(3,2)*u + 4", (-2, 7), (2, 1)), through("4 - F(3,2)*u", (-2, 7), (2, 1)),
                    misses("4*u - F(3,2)", (-2, 7), (2, 1)), misses("-F(3,2)*u + 7", (-2, 7), (2, 1)),
                    misses("F(3,2)*u + 4", (-2, 7), (2, 1))),
             errors={"A": "the first point's y-value taken as b [Notes III: substitute a point and solve for b]", "B": "the slope and the y-intercept exchanged [Florida B1G-M, AR.3.3: swapping m and b]", "D": "the sign of the slope lost: the line falls from (−2, 7) to (2, 1) [Florida B1G-M, AR.3.3: positive and negative slopes]"}),
    ],

    additional=[
        dict(heading="For questions 1 and 2, write the equation of the graphed line in slope-intercept form."),
        dict(stem="The line passes through the two marked points.",
             fig=GP((-1, 5), (-1, 5), [(Fr(3, 4), 1, "")], [(0, 1), (4, 4)]),
             answer="y = (3/4)x + 1", why="b = 1. Slope: (4 − 1) ÷ (4 − 0) = 3/4.",
             check=("many", slope((0, 1), (4, 4), "F(3, 4)"), through("F(3,4)*u + 1", (0, 1), (4, 4))), space=0.5),
        dict(stem="The line passes through the two marked points.",
             fig=GP((-1, 5), (-5, 1), [(Fr(-1, 2), -2, "")], [(0, -2), (4, -4)]),
             answer="y = −(1/2)x − 2", why="b = −2. Slope: (−4 − (−2)) ÷ (4 − 0) = −2/4 = −1/2.",
             check=("many", slope((0, -2), (4, -4), "F(-1, 2)"), through("-F(1,2)*u - 2", (0, -2), (4, -4))), space=0.5),
        dict(heading="For questions 3 and 4, the table shows a linear relationship. Write its equation in slope-intercept form."),
        dict(stem="The table has a column for x = 0.", fig=PT([0, 2, 3], [1, -5, -8]),
             answer="y = −3x + 1", why="At x = 0, y = 1, so b = 1. Slope: (−5 − 1) ÷ (2 − 0) = −3. Check (3, −8): −9 + 1 = −8.",
             check=("many", slope((0, 1), (2, -5), "-3"), through("-3*u + 1", (0, 1), (2, -5), (3, -8))), space=0.5),
        dict(stem="The table has no column for x = 0.", fig=PT([2, 4, 8], [4, -1, -11]),
             answer="y = −(5/2)x + 9", why="Slope: (−1 − 4) ÷ (4 − 2) = −5/2. Substitute (2, 4): 4 = −5 + b, so b = 9. Check (8, −11): −20 + 9 = −11.",
             check=("many", slope((2, 4), (4, -1), "F(-5, 2)"), through("-F(5,2)*u + 9", (2, 4), (4, -1), (8, -11))), space=0.5),
        dict(heading="For questions 5 and 6, write the equation of the line in slope-intercept form."),
        dict(stem="A line has the slope $\\frac{3}{4}$ and passes through $(4, -1)$.",
             answer="y = (3/4)x − 4", why="Substitute (4, −1): −1 = (3/4)(4) + b = 3 + b, so b = −4.",
             check=("many", sat("F(3,4)*u - 4", "4", "-1"), ("eq", "sp.diff(F(3,4)*" + X + " - 4, " + X + ")", "F(3, 4)")), space=0.5),
        dict(stem="A line has the slope 4 and passes through $(-1, 2)$.",
             answer="y = 4x + 6", why="Substitute (−1, 2): 2 = 4(−1) + b = −4 + b, so b = 6.",
             check=("many", sat("4*u + 6", "-1", "2"), ("eq", "sp.diff(4*" + X + " + 6, " + X + ")", "4")), space=0.5),
        dict(heading="For questions 7 and 8, write the equation of the line through the two points in slope-intercept form."),
        dict(stem="$(-2, 3)$ and $(2, -3)$",
             answer="y = −(3/2)x", why="Slope: (−3 − 3) ÷ (2 − (−2)) = −6/4 = −3/2. Substitute (2, −3): −3 = −3 + b, so b = 0.",
             check=("many", slope((-2, 3), (2, -3), "F(-3, 2)"), through("-F(3,2)*u", (-2, 3), (2, -3))), space=0.5),
        dict(stem="$(1, -3)$ and $(4, 3)$",
             answer="y = 2x − 5", why="Slope: (3 − (−3)) ÷ (4 − 1) = 6/3 = 2. Substitute (1, −3): −3 = 2 + b, so b = −5.",
             check=("many", slope((1, -3), (4, 3), "2"), through("2*u - 5", (1, -3), (4, 3))), space=0.5),
        dict(heading="Find the missing number."),
        dict(stem="The line $y = □x + 3$ passes through $(4, -9)$. Find the missing number.",
             answer="−3", why="4 times the missing number, plus 3, is −9. So 4 times it is −12, and the missing number is −3.",
             check=("many", ("eq", "F(-9 - 3, 4)", "-3"), sat("-3*u + 3", "4", "-9")), space=0.5),
        dict(heading="Choose one."),
        dict(stem="Which equation is the graphed line's?",
             fig=GP((-2, 3), (-5, 3), [(5, -4, "")], [(0, -4), (1, 1)]),
             choices=["$y = \\frac{1}{5}x - 4$", "$y = -4x + 5$", "$y = 5x + 1$", "$y = 5x - 4$"], correct=3, answer="D",
             why="b = −4. Slope: (1 − (−4)) ÷ (1 − 0) = 5.",
             check=("many", through("5*u - 4", (0, -4), (1, 1)), misses("-4*u + 5", (0, -4), (1, 1)),
                    misses("5*u + 1", (0, -4), (1, 1)), misses("F(1,5)*u - 4", (0, -4), (1, 1))),
             errors={"A": "the slope turned over [Florida B1G-M, AR.3.3: inverted slope]", "B": "the slope and the y-intercept exchanged [Florida B1G-M, AR.3.3: swapping m and b]", "C": "the other point's y-value, 1, taken as b [Notes I: b is where the line crosses the y-axis]"}),
        dict(stem="The table shows a linear relationship. Which is its equation?",
             fig=PT([1, 2, 3], [5, 2, -1]),
             choices=["$y = -3x + 8$", "$y = -3x + 5$", "$y = 8x - 3$", "$y = -\\frac{1}{3}x + 8$"], correct=0, answer="A",
             why="Slope: (2 − 5) ÷ (2 − 1) = −3. Substitute (1, 5): 5 = −3 + b, so b = 8.",
             check=("many", through("-3*u + 8", (1, 5), (2, 2), (3, -1)), misses("-3*u + 5", (1, 5), (2, 2), (3, -1)),
                    misses("8*u - 3", (1, 5), (2, 2), (3, -1)), misses("-F(1,3)*u + 8", (1, 5), (2, 2), (3, -1))),
             errors={"B": "the first y-value taken as b, though the table has no x = 0 [Notes III: substitute a point and solve for b]", "C": "the slope and the y-intercept exchanged [Florida B1G-M, AR.3.3: swapping m and b]", "D": "the change in x over the change in y [Florida B1G-M, AR.3.3: inverted slope]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the equations of the line through $(-3, 6)$ and $(3, 2)$.",
             choices=["$y = 4 - \\frac{2}{3}x$", "$y = 4x - \\frac{2}{3}$", "$y = \\frac{2}{3}x + 4$", "$y = -\\frac{2}{3}x + 6$", "$y = -\\frac{2}{3}x + 4$"],
             correct=[0, 4], answer="A, E",
             why="Slope: (2 − 6) ÷ (3 − (−3)) = −4/6 = −2/3. Substitute (3, 2): 2 = −2 + b, so b = 4. A and E are the same equation, with b written first in A.",
             check=("many", through("-F(2,3)*u + 4", (-3, 6), (3, 2)), through("4 - F(2,3)*u", (-3, 6), (3, 2)),
                    misses("-F(2,3)*u + 6", (-3, 6), (3, 2)), misses("F(2,3)*u + 4", (-3, 6), (3, 2)),
                    misses("4*u - F(2,3)", (-3, 6), (3, 2))),
             errors={"B": "the slope and the y-intercept exchanged [Florida B1G-M, AR.3.3: swapping m and b]", "C": "the sign of the slope lost: the line falls from (−3, 6) to (3, 2) [Florida B1G-M, AR.3.3: positive and negative slopes]", "D": "the first point's y-value taken as b [Notes III: substitute a point and solve for b]"}),
    ],

    te=dict(
        must="Students write the equation of a line in slope-intercept form from a graph, from a table or from two points. When the y-intercept is not shown, they substitute a point and solve for b.",
        must_not="Point-slope form and standard form are not taught or accepted as a final answer. Stories, with their own letters, wait for lesson 10.10.",
        materials="Whiteboards and markers, and the Independent Set, one copy per student.",
        variation="Whiteboard questions 1 and 2 change one thing: the point leaves the y-axis, so b has to be found. Question 3 reads a graph and question 4 a table through x = 0 with a negative slope; question 5 is a table with no x = 0, where the first y-value is the trap. Question 6 gives two points, question 7 two axis crossings with the grid's width as an extra number, question 8 runs backwards to the slope, and question 9 is written. The pattern breaks at question 7, where the line's two points are its crossings and neither is marked as a point. In the Independent Set the pattern breaks at question 3, whose table shows x = 0 between negative and positive x-values.",
        audit=["Every equation is checked by sympy at build time to pass through every point and every table value it was written from, every slope is recomputed from two points as an exact fraction, and every wrong option is checked to miss at least one of the points.",
               "Math Nation was read for scope and item shapes only; nothing in this lesson is taken from it."],
        changes=["The lesson is new for this unit and is built from the unit's Lesson Outlines, section 10.09."],
        read_first=["Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, section 10.09). Three ways in, one method: find m from two points, then read b at x = 0 or substitute a point and solve for b, then check with another point.",
                    "Whiteboard questions 3 and 5 are the diagnostics: each wrong option is one named error — the slope and the y-intercept exchanged, the slope turned over, or a y-value that is not at x = 0 taken as b."],
    ),
)
