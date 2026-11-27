# A7 10.02+03 Slope from Graphs, Tables and Two Points (MA.8.AR.3.2): two book lessons taught as one day.
# Built from the unit's Lesson Outlines, section 10.02+03, and its standing decisions 2, 4, 5, 6, 7 and 8.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs10 as figs
S = figs.slide

X = "sp.Symbol('u', real=True)"


def slope(p, q):
    """The change in y divided by the change in x, from p to q, as sympy reads it (an exact rational)."""
    return "((%s) - (%s))/((%s) - (%s))" % (q[1], p[1], q[0], p[0])


def on(m, b, x, y):
    """(x, y) is on the line y = mx + b (m given as a sympy string)."""
    return ("true", "sp.simplify((%s)*(%s) + (%s) - (%s)) == 0" % (m, x, b, y))


def table_on(m, b, xs, ys):
    return ("many",) + tuple(on(m, b, str(a), str(c)) for a, c in zip(xs, ys))


def solves(lhs, rhs, val):
    return ("eq", "sp.solve(sp.Eq(" + lhs.replace("u", X) + ", " + rhs.replace("u", X) + "), " + X + ")[0]", val)


def B(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.75)


def BA(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.95)


def P(xr, yr, **k):
    """A slide plane at the size it is shown."""
    return figs.plane(xr, yr, inches=4.2, pt=18, **k)


def PP(xr, yr, inches=2.6, **k):
    """A printed plane (set and banks)."""
    return figs.plane(xr, yr, inches=inches, **k)


def TT(xs, ys, inches=3.2):
    return figs.table([(xs, ys)], head=("x", "y"), inches=inches)


def run_off_axis(fig, run, x):
    """A slope triangle whose run is centred on the y-axis has its run's number struck by the axis: set the number
    over the run's right half, at x (the triangle's own colour; figs10.tri has no place for it)."""
    for sh in fig["shapes"]:
        if sh["t"] == "text" and sh["s"] == run and sh.get("color") == figs.TRIS[0]:
            sh["xy"] = (x, sh["xy"][1])
            return fig
    raise ValueError(f"run_off_axis: no run number {run}")


# ---- notes
NOTES1 = S(figs.plane((0, 5), (0, 6), lines=[(2, 1, "")], points=[(0, 1, ""), (2, 5, "")],
                      triangles=[figs.tri((0, 1), (2, 5), "run 2", "rise 4")], inches=4.2, pt=18),
           inches=4.2, pt=18, reserve=2.05)
NOTES2 = S(figs.plane((0, 7), (0, 4), lines=[(Fr(1, 2), 1, "")], points=[(0, 1, ""), (2, 2, ""), (6, 4, "")],
                      triangles=[figs.tri((0, 1), (2, 2)), figs.tri((2, 2), (6, 4))], inches=4.2, pt=18),
           inches=3.6, pt=18, reserve=1.6)
NOTES3 = S(figs.table([([-3, 1, 9], [2, 5, 11])], head=("x", "y"), cw=2.0, rh=1.5), inches=4.0, pt=18, reserve=1.2)

# ---- examples
EX1 = B(P((-5, 4), (-3, 6), lines=[(Fr(-3, 2), 2, "")], points=[(-2, 5, None, "dl"), (2, -1, None, "r")]))
EX1W = run_off_axis(S(figs.plane((-5, 4), (-3, 6), lines=[(Fr(-3, 2), 2, "")], points=[(-2, 5, ""), (2, -1, "")],
                    triangles=[figs.tri((-2, 5), (2, -1), side="over")], inches=4.2, pt=18), inches=4.2, pt=18, reserve=1.4), "4", 1)
YT1 = S(P((-7, 5), (-3, 7), lines=[(Fr(-4, 3), 2, "")], points=[(-3, 6, None, "dl"), (3, -2, None, "r")], ystep=2),
        inches=4.2, pt=18, reserve=0.5)
YT1A = run_off_axis(BA(P((-7, 5), (-3, 7), lines=[(Fr(-4, 3), 2, "")], points=[(-3, 6, ""), (3, -2, "")], ystep=2,
            triangles=[figs.tri((-3, 6), (3, -2), side="over")])), "6", 1.5)
EX2 = S(figs.table([([-4, -1, 5], [13, 4, -14])], head=("x", "y"), cw=2.0, rh=1.5), inches=5.0, pt=18, reserve=0.9)
EX2W = S(figs.table([([-4, -1, 5], [13, 4, -14])], head=("x", "y"), cw=2.0, rh=1.5), inches=4.0, pt=16, reserve=0.9)
YT2 = S(figs.table([([-6, -2, 6], [1, -1, -5])], head=("x", "y"), cw=2.0, rh=1.5), inches=5.0, pt=18, reserve=0.9)
YT2A = S(figs.table([([-6, -2, 6], [1, -1, -5])], head=("x", "y"), cw=2.0, rh=1.5), inches=4.4, pt=18, reserve=1.1)

# ---- boards
T3 = S(figs.table([([1, 3, 5], [10, 4, -2])], head=("x", "y"), cw=2.0, rh=1.5), inches=4.6, pt=18, reserve=0.75)
P4 = P((-5, 4), (-3, 5), lines=[(-2, 2, "")], points=[(-1, 4, None, "l"), (2, -2, None, "r")])
P5 = P((-1, 7), (-1, 5), lines=[(Fr(-2, 3), 4, "")], points=[(0, 4), (6, 0)])
P6 = P((0, 9), (0, 9), lines=[(Fr(3, 4), 2, "")], points=[(0, 2, ""), (4, 5, ""), (8, 8, "")],
       triangles=[figs.tri((0, 2), (4, 5))], step=2)


L = dict(
    code="10.02", unit=10, lesson_no="2–3", label="Lessons 2–3",
    title="Slope from Graphs, Tables and Two Points",
    unit_title="Linear Relationships",
    benchmark="MA.8.AR.3.2",
    benchmark_text="Given a table, graph or written description of a linear relationship, determine the slope.",
    target="I can find the slope of a line from its graph, from a table and from two points.",
    essential="Why do any two points on a line give the same slope, and what does that number tell us about the line?",
    building_on="In lesson 10.01, students learned that a linear relationship has a constant rate of change and is also proportional when its line passes through the origin. In Unit 6 (lessons 6.07–08), they used similar triangles, and in Unit 7 they found the constant of proportionality as the amount of y for every 1 unit of x.",
    working_toward="Lesson 10.04 finds slope in context, where the slope is a rate of change with a unit. Lesson 10.05 names the y-intercept and graphs a line from y = mx + b.",
    vocab=[("slope", "the rate of change of a line: the change in y divided by the change in x between any two points on the line (rise over run); its letter is m")],
    ixl=["Find the slope from two points — ZAC", "Find the slope from a table — GSB", "Find the slope from a graph — Q94"],
    closure="Whiteboard question 9 is answered in writing and serves as the exit ticket. A complete answer says that Jo subtracted in different orders, 9 − 1 on top but 6 − 2 below, and that the slope is (1 − 9) ÷ (6 − 2) = −8 ÷ 4 = −2, which is negative because the line falls. An answer that gives only −2 has the slope without the mistake.",

    mtr=[("MTR.2.1", "Students find one idea, slope, from a graph, from a table and from two points."),
         ("MTR.4.1", "On whiteboard questions 3 and 5, a divided class convinces a neighbor for sixty seconds and then votes again."),
         ("MTR.6.1", "Students check a slope from a table with a second pair of points and check its sign against the direction of the line.")],
    hoq=[("Why does it not matter which two points of a line you use to find its slope?", "DOK 2"),
         ("Board 5's line falls. How does the picture tell you the sign of the slope before you compute it?", "DOK 2"),
         ("In a table whose x-values do not go up by 1, why is the change in y alone not the slope?", "DOK 2"),
         ("A larger slope triangle on the same line is past the edge of the grid. How can you find its rise without drawing it?", "DOK 3")],
    differentiation=[
        ("ESE / 504", "Provide a printed card that reads “slope = change in y ÷ change in x, in the same order”, with two empty boxes for the subtractions. Keep Notes III on display from whiteboard question 1 onward."),
        ("ELL", "**Rise**: how far up or down. **Run**: how far to the right. **Slope**: rise over run. **Falls**: goes down from left to right."),
        ("Enrichment", "For students who finish whiteboard question 8 early: find two points with no coordinate equal to 0 on a line whose slope is −3/2, and show that a third point of your own gives the same slope. (Any points such as (2, 1), (4, −2) and (6, −5) work.)")],

    warmup=[
        dict(stem="A table of a linear relationship has the x-values 0, 2, 4 and the y-values 3, 8, 13. Is the relationship also proportional?",
             answer="No, because y is 3 when x is 0.",
             check=("many", ("true", "3 != 0"), ("eq", slope((0, 3), (2, 8)), slope((2, 8), (4, 13))))),
        dict(stem="A proportional relationship passes through (5, 6). Write its equation.", answer="y = 1.2x",
             check=("eq", "F(6, 5)", "F(12, 10)")),
        dict(stem="Solve for x:  $7x - 5 = 3x + 19$", answer="x = 6",
             check=solves("7*u - 5", "3*u + 19", "6")),
        dict(stem="Find  $-3 - 5$  and  $4 - (-2)$.", answer="−8 and 6",
             check=("many", ("eq", "-3 - 5", "-8"), ("eq", "4 - (-2)", "6"))),
    ],

    notes=[
        dict(numeral="I", head="Slope: rise over run", min=3,
             fig=NOTES1,
             items2=["Slope is the change in y divided by the change in x: rise over run.",
                     "$\\frac{4}{2} = 2$:   the rate of change of  $y = 2x + 1$,  up 2 for every 1 unit to the right."],
             letters=False),
        dict(numeral="II", head="Any two points on the line give the same slope", min=3,
             fig=NOTES2,
             items2=["Rise 1, run 2  and  rise 2, run 4.   The triangles are similar (6.07–08):   $\\frac{1}{2} = \\frac{2}{4}$",
                     "On this line a run of 6 has a rise of 3, and a rise of 5 has a run of 10:",
                     "the slope stays $\\frac{1}{2}$."],
             letters=False),
        dict(numeral="III", head="Without a graph: subtract in the same order", min=4,
             items=["$m = \\frac{y_2 - y_1}{x_2 - x_1}$    Through (1, 7) and (4, 1):   $\\frac{1 - 7}{4 - 1} = \\frac{-6}{3} = -2$.   The line falls."],
             math=["$\\frac{5 - 2}{1 - (-3)} = \\frac{3}{4}$     and     $\\frac{11 - 5}{9 - 1} = \\frac{6}{8} = \\frac{3}{4}$"],
             table=([1.0, 1.0, 1.0, 1.0], [["x", "−3", "1", "9"], ["y", "2", "5", "11"]]), tsize=18,
             items2=["Rises: positive.   Falls: negative.   Horizontal: slope 0."],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=1,
             prompt=["The line passes through (−2, 5) and (2, −1)."], fig=EX1, ask="Find the slope of the line.",
             worked=[dict(min=2,
                          rows=[("\\frac{-1 - 5}{2 - (-2)}", "subtract in the same order"),
                                ("= \\frac{-6}{4} = -\\frac{3}{2}", "the line falls: negative")],
                          fig=EX1W, answer="The slope is −3/2.")],
             check=("many", ("eq", slope((-2, 5), (2, -1)), "F(-3, 2)"), on("F(-3,2)", "2", "-2", "5"), on("F(-3,2)", "2", "2", "-1")),
             your_turn=dict(min=3, repeat_ok=True,  # repeat_ok: rule D matches only small digits (axis numbers); these points appear nowhere above
                            prompt=["The line passes through (−3, 6) and (3, −2)."], fig=YT1, fig_a=YT1A,
                            ask="Find the slope of the line.",
                            steps=["Subtract in the same order:  $\\frac{-2 - 6}{3 - (-3)} = \\frac{-8}{6} = -\\frac{4}{3}$"],
                            answer="The slope is −4/3."),
             yt_check=("many", ("eq", slope((-3, 6), (3, -2)), "F(-4, 3)"), on("F(-4,3)", "2", "-3", "6"), on("F(-4,3)", "2", "3", "-2"))),
        dict(title="Example 2", min_q=1,
             prompt=["The table shows a linear relationship."], fig=EX2, ask="Find the slope.",
             worked=[dict(min=2,
                          rows=[("\\frac{4 - 13}{-1 - (-4)} = \\frac{-9}{3} = -3", "the first two pairs"),
                                ("\\frac{-14 - 4}{5 - (-1)} = \\frac{-18}{6} = -3", "the check: the last two")],
                          fig=EX2W, answer="The slope is −3.")],
             check=("many", ("eq", slope((-4, 13), (-1, 4)), "-3"), ("eq", slope((-1, 4), (5, -14)), "-3"),
                    table_on("-3", "1", [-4, -1, 5], [13, 4, -14])),
             your_turn=dict(min=3, repeat_ok=True,  # repeat_ok: rule D matches only small digits; this table appears nowhere above
                            prompt=["The table shows a linear relationship."], fig=YT2, fig_a=YT2A, ask="Find the slope.",
                            steps=["First two pairs:  $\\frac{-1 - 1}{-2 - (-6)} = \\frac{-2}{4} = -\\frac{1}{2}$",
                                   "Check:  $\\frac{-5 - (-1)}{6 - (-2)} = \\frac{-4}{8} = -\\frac{1}{2}$"],
                            answer="The slope is −1/2."),
             yt_check=("many", ("eq", slope((-6, 1), (-2, -1)), "F(-1, 2)"), ("eq", slope((-2, -1), (6, -5)), "F(-1, 2)"),
                       table_on("F(-1,2)", "-2", [-6, -2, 6], [1, -1, -5]))),
    ],

    # The round: two points (1), one thing changed, the second y (2); a table vote with x-steps of 2 (3); a falling line
    # read off a graph (4); a graph vote (5); the pattern breaks at 6, similar triangles past the grid's edge; a ramp,
    # its width the extra number (7); backwards (8); Jo's mistake, written (9).
    whiteboard=[
        dict(text=["**Find the slope of the line through (2, 3) and (5, 15)."],
             steps=["Change in y:  $15 - 3 = 12$", "Change in x:  $5 - 2 = 3$", "Divide:  $\\frac{12}{3} = 4$"],
             answer="4",
             check=("eq", slope((2, 3), (5, 15)), "4"),
             wrong="1/4 — the change in x over the change in y [B1G-M, AR.3.2: run over rise]; 12 — the change in y alone [Notes I: rise over run]"),
                # repeat_ok: rule D matches only small digits (axis numbers 0 to 7, the notes' table and points); this problem appears nowhere above.
        dict(repeat_ok=True, text=["**Find the slope of the line through (2, 3) and (5, −6)."],
             steps=["Change in y:  $-6 - 3 = -9$", "Change in x:  $5 - 2 = 3$", "Divide:  $\\frac{-9}{3} = -3$"],
             answer="−3",
             check=("eq", slope((2, 3), (5, -6)), "-3"),
             wrong="3 — subtracted in different orders, 3 − (−6) over 5 − 2 [Notes III: subtract in the same order]; −1/3 — run over rise [B1G-M, AR.3.2: run over rise]"),
        # repeat_ok: rule D matches small digits only; Notes II's added line (run 6, rise 3, rise 5, run 10) shares 3, 5 and 10 with this table (x 1, 3, 5; y 10, 4, −2); the problem appears nowhere above.
        dict(repeat_ok=True, kind="mc", text=["The table shows a linear relationship.", "**What is its slope?"],
             qtext="The table shows a linear relationship: x 1, 3, 5; y 10, 4, −2. What is its slope?",
             fig=T3,
             steps=["Change in y:  $4 - 10 = -6$", "Change in x:  $3 - 1 = 2$", "Divide:  $\\frac{-6}{2} = -3$"],
             choices=["$-3$", "$-\\frac{1}{3}$", "$-6$", "$3$"], correct=0, answer="A — −3",
             errors={"B": "the change in x over the change in y [B1G-M, AR.3.2: run over rise]", "C": "the change in y alone, not divided by the change in x [standing decision 5: a table's x-steps are not 1]", "D": "subtracted in different orders, 10 − 4 over 3 − 1 [Notes III: subtract in the same order]"},
             check=("many", ("eq", slope((1, 10), (3, 4)), "-3"), ("eq", slope((3, 4), (5, -2)), "-3"),
                    ("eq", "4 - 10", "-6"), ("eq", "(3 - 1)/(4 - 10)", "-F(1,3)"), ("eq", "(10 - 4)/(3 - 1)", "3"))),
                # repeat_ok: rule D matches only small digits (axis numbers 0 to 7, the notes' table and points); this problem appears nowhere above.
        dict(repeat_ok=True, text=["**The graph shows a line. What is the slope of the line?"],
             fig=B(P4), fig_a=BA(P4),
             steps=["Subtract in the same order:  $\\frac{-2 - 4}{2 - (-1)} = \\frac{-6}{3}$", "Divide:  $\\frac{-6}{3} = -2$"],
             answer="−2",
             check=("many", ("eq", slope((-1, 4), (2, -2)), "-2"), on("-2", "2", "-1", "4"), on("-2", "2", "2", "-2")),
             wrong="2 — a falling line read as rising [Notes III: a line that falls has a negative slope]; −1/2 — run over rise [B1G-M, AR.3.2: run over rise]"),
                # repeat_ok: rule D matches only small digits (axis numbers 0 to 7, the notes' table and points); this problem appears nowhere above.
        dict(repeat_ok=True, kind="mc", text=["**The graph shows a line. What is its slope?"],
             qtext="The graph shows a line through (0, 4) and (6, 0). What is its slope?",
             fig=B(P5), fig_a=BA(P5),
             steps=["Subtract in the same order:  $\\frac{0 - 4}{6 - 0} = \\frac{-4}{6}$", "Simplify:  $\\frac{-4}{6} = -\\frac{2}{3}$"],
             choices=["$-4$", "$\\frac{2}{3}$", "$-\\frac{2}{3}$", "$-\\frac{3}{2}$"], correct=2, answer="C — −2/3",
             errors={"A": "the change in y alone, not divided by the change in x [Notes I: rise over run]", "B": "a falling line read as rising [Notes III: a line that falls has a negative slope]", "D": "the change in x over the change in y [B1G-M, AR.3.2: run over rise]"},
             check=("many", ("eq", slope((0, 4), (6, 0)), "F(-2, 3)"), on("F(-2,3)", "4", "0", "4"), on("F(-2,3)", "4", "6", "0"),
                    ("eq", "(6 - 0)/(0 - 4)", "F(-3, 2)"), ("eq", "0 - 4", "-4"))),
        dict(text=["**A larger slope triangle on this line has a run of 20. What is its rise?"],
             qtext="A line passes through (0, 2), (4, 5) and (8, 8), with a slope triangle drawn: a rise of 3 and a run of 4. A larger slope triangle on the same line has a run of 20. What is its rise?",
             fig=B(P6), fig_a=BA(P6),
             steps=["Slope:  $\\frac{3}{4}$", "Same slope:  $\\frac{3}{4} = \\frac{?}{20}$", "Rise:  $\\frac{3}{4}(20) = 15$"],
             answer="The rise is 15.",
             check=("many", ("eq", "F(3, 4)*20", "15"), ("eq", slope((0, 2), (4, 5)), "F(3, 4)"), ("eq", slope((4, 5), (8, 8)), "F(3, 4)")),
             wrong="19 — the run grew by 16, so the rise was taken to grow by 16 too [B1G-M, AR.3.2: similar triangles]; 26 2/3 — run over rise used, (4/3)(20) [B1G-M, AR.3.2: run over rise]"),
        dict(text=["A ramp is 36 inches wide.", "It rises 2 feet over a horizontal distance of 16 feet.",
                   "**What is the slope of the ramp?"],
             unneeded="36",
             steps=["Rise over run:  $\\frac{2}{16}$", "Simplify:  $\\frac{2}{16} = \\frac{1}{8}$"],
             answer="The slope of the ramp is 1/8.",
             check=("eq", "F(2, 16)", "F(1, 8)"),
             wrong="36/16 = 9/4 — the width used as the rise [an extra number, included on purpose]; 8 — run over rise [B1G-M, AR.3.2: run over rise]"),
        dict(text=["The line through $(5, □)$ and (1, 4) has a slope of 3.", "**Find the missing number."],
             steps=["Change in x:  $5 - 1 = 4$", "Change in y:  $3(4) = 12$", "Missing number:  $4 + 12 = 16$"],
             answer="16",
             check=("many", ("eq", "4 + 3*(5 - 1)", "16"), ("eq", slope((1, 4), (5, 16)), "3")),
             wrong="7 — the slope added to 4, as if x went up by 1 [standing decision 5: a table's x-steps are not 1]; 12 — the change in y, not the y-value [Notes III: subtract in the same order]"),
        dict(kind="written", text=["Jo finds the slope of the line through (2, 9) and (6, 1) this way:",
                                   "$(9 - 1) \\div (6 - 2) = 2$",
                                   "**What is Jo's mistake? What is the slope?"],
             qtext="Jo finds the slope of the line through (2, 9) and (6, 1) this way: (9 − 1) ÷ (6 − 2) = 2. What is Jo's mistake? What is the slope?",
             steps=["Jo:  9 − 1 on top, but 6 − 2 below:  different orders",
                    "Same order:  $(1 - 9) \\div (6 - 2) = -8 \\div 4$",
                    "Slope:  $-8 \\div 4 = -2$"],
             answer="Jo used two orders. The slope is −2.",
             check=("many", ("eq", slope((2, 9), (6, 1)), "-2"), ("eq", "(9 - 1)/(6 - 2)", "2")),
             wrong="'Jo is right' — the order of subtraction not checked [Notes III: subtract in the same order]"),
    ],

    # The six: two points with negative coordinates (1); a rising line, a fraction (2); a falling line (3); a table with
    # unequal steps and a negative slope (4); two slope triangles, the run missing (5); the pattern breaks at 6, a
    # horizontal line, slope 0.
    independent=[
                # repeat_ok: rule D matches only small digits (axis numbers 0 to 7, the notes' table and points); this problem appears nowhere above.
        dict(repeat_ok=True, stem="Find the slope of the line through (−3, −9) and (−1, −1).",
             answer="4", why="(−1 − (−9)) ÷ (−1 − (−3)) = 8 ÷ 2 = 4.",
             check=("eq", slope((-3, -9), (-1, -1)), "4"), space=0.6),
        # repeat_ok: rule D matches only small digits (axis numbers 0 to 7, the notes' table and points); this problem appears nowhere above.
        dict(repeat_ok=True, stem="Find the slope of the line.",
             fig=PP((-5, 5), (-5, 3), inches=3.8, lines=[(Fr(1, 2), -2, "")], points=[(-2, -3), (4, 0)]),
             answer="1/2", why="(0 − (−3)) ÷ (4 − (−2)) = 3 ÷ 6 = 1/2. The line rises: positive.",
             check=("many", ("eq", slope((-2, -3), (4, 0)), "F(1, 2)"), on("F(1,2)", "-2", "-2", "-3"), on("F(1,2)", "-2", "4", "0")),
             space=0.4),
        # repeat_ok: rule D matches only small digits (axis numbers 0 to 7, the notes' table and points); this problem appears nowhere above.
        dict(repeat_ok=True, stem="Find the slope of the line.",
             fig=PP((-4, 4), (-4, 6), inches=3.0, lines=[(Fr(-4, 3), 1, "")], points=[(-3, 5), (3, -3)]),
             answer="−4/3", why="(−3 − 5) ÷ (3 − (−3)) = −8 ÷ 6 = −4/3. The line falls: negative.",
             check=("many", ("eq", slope((-3, 5), (3, -3)), "F(-4, 3)"), on("F(-4,3)", "1", "-3", "5"), on("F(-4,3)", "1", "3", "-3")),
             space=0.4),
                # repeat_ok: rule D matches only small digits (axis numbers 0 to 7, the notes' table and points); this problem appears nowhere above.
        dict(repeat_ok=True, stem="The table shows a linear relationship. Find the slope.",
             fig=TT([-4, -2, 4], [7, 4, -5]),
             answer="−3/2", why="(4 − 7) ÷ (−2 − (−4)) = −3 ÷ 2 = −3/2. Check: (−5 − 4) ÷ (4 − (−2)) = −9 ÷ 6 = −3/2.",
             check=("many", ("eq", slope((-4, 7), (-2, 4)), "F(-3, 2)"), ("eq", slope((-2, 4), (4, -5)), "F(-3, 2)")),
             space=0.6),
        dict(stem="A slope triangle on the line has a rise of 2 and a run of 4. A larger slope triangle on the same line has a rise of 9. What is its run?",
             fig=PP((0, 10), (0, 8), inches=3.8, lines=[(Fr(1, 2), 2, "")], points=[(0, 2, ""), (4, 4, "")],
                    triangles=[figs.tri((0, 2), (4, 4))]),
             answer="18", why="The slope is 2/4 = 1/2, so the run is twice the rise: 2(9) = 18.",
             check=("many", ("eq", "9 / F(2, 4)", "18"), ("eq", slope((0, 2), (4, 4)), "F(1, 2)")), space=0.5),
                # repeat_ok: rule D matches only small digits (axis numbers 0 to 7, the notes' table and points); this problem appears nowhere above.
        dict(repeat_ok=True, stem="Find the slope of the line through (−3, 4) and (5, 4).",
             answer="0", why="(4 − 4) ÷ (5 − (−3)) = 0 ÷ 8 = 0. The line is horizontal.",
             check=("eq", slope((-3, 4), (5, 4)), "0"), space=0.5),
    ],

    # Bank: two points (1–4, the fourth a horizontal line); two graphs, rising and falling (5–6); two tables, steps of 3
    # and unequal steps (7–8); similar triangles in words (9); backwards (10); a roof (11); two votes, a table and a graph
    # (12–13). The additional bank mirrors it position by position with new numbers.
    bank=[
        dict(heading="For questions 1 to 4, find the slope of the line through the two points."),
        dict(stem="$(1, 2)$ and $(3, 10)$", answer="4", why="(10 − 2) ÷ (3 − 1) = 8 ÷ 2 = 4.",
             check=("eq", slope((1, 2), (3, 10)), "4"), space=0.4),
        dict(stem="$(-2, 1)$ and $(2, -11)$", answer="−3", why="(−11 − 1) ÷ (2 − (−2)) = −12 ÷ 4 = −3.",
             check=("eq", slope((-2, 1), (2, -11)), "-3"), space=0.4),
        dict(stem="$(-5, 3)$ and $(3, 7)$", answer="1/2", why="(7 − 3) ÷ (3 − (−5)) = 4 ÷ 8 = 1/2.",
             check=("eq", slope((-5, 3), (3, 7)), "F(1, 2)"), space=0.4),
        dict(stem="$(-4, 6)$ and $(2, 6)$", answer="0", why="(6 − 6) ÷ (2 − (−4)) = 0 ÷ 6 = 0: a horizontal line.",
             check=("eq", slope((-4, 6), (2, 6)), "0"), space=0.4),
        dict(heading="For questions 5 and 6, find the slope of the line."),
        dict(stem="The graph shows a line.",
             fig=PP((-2, 6), (-4, 3), lines=[(Fr(3, 4), -2, "")], points=[(0, -2), (4, 1)]),
             answer="3/4", why="(1 − (−2)) ÷ (4 − 0) = 3 ÷ 4 = 3/4.",
             check=("many", ("eq", slope((0, -2), (4, 1)), "F(3, 4)"), on("F(3,4)", "-2", "0", "-2"), on("F(3,4)", "-2", "4", "1")),
             space=0.4),
        dict(stem="The graph shows a line.",
             fig=PP((-2, 4), (-2, 5), lines=[(Fr(-3, 2), 3, "")], points=[(0, 3), (2, 0)]),
             answer="−3/2", why="(0 − 3) ÷ (2 − 0) = −3 ÷ 2 = −3/2.",
             check=("many", ("eq", slope((0, 3), (2, 0)), "F(-3, 2)"), on("F(-3,2)", "3", "0", "3"), on("F(-3,2)", "3", "2", "0")),
             space=0.4),
        dict(heading="For questions 7 and 8, find the slope."),
        dict(stem="The table shows a linear relationship.", fig=figs.table([([0, 3, 6, 9], [5, 1, -3, -7])], head=("x", "y"), inches=3.6),
             answer="−4/3", why="(1 − 5) ÷ (3 − 0) = −4 ÷ 3 = −4/3.",
             check=("many", ("eq", slope((0, 5), (3, 1)), "F(-4, 3)"), table_on("F(-4,3)", "5", [0, 3, 6, 9], [5, 1, -3, -7])),
             space=0.4),
        dict(stem="The table shows a linear relationship.", fig=TT([-3, -1, 4], [-10, -2, 18]),
             answer="4", why="(−2 − (−10)) ÷ (−1 − (−3)) = 8 ÷ 2 = 4. Check: (18 − (−2)) ÷ (4 − (−1)) = 20 ÷ 5 = 4.",
             check=("many", ("eq", slope((-3, -10), (-1, -2)), "4"), ("eq", slope((-1, -2), (4, 18)), "4")),
             space=0.4),
        dict(heading="Use similar triangles."),
        dict(stem="A slope triangle on a line has a rise of 3 and a run of 4. A larger slope triangle on the same line has a run of 16. What is its rise?",
             answer="12", why="The slope is 3/4, so the rise is (3/4)(16) = 12.",
             check=("eq", "F(3, 4)*16", "12"), space=0.5),
        dict(heading="Find the missing number."),
        dict(stem="The slope of the line through $(-1, 5)$ and $(2, □)$ is −3. Find the missing number.",
             answer="−4", why="The change in x is 2 − (−1) = 3, so the change in y is −3(3) = −9, and 5 − 9 = −4.",
             check=("many", ("eq", "5 + (-3)*(2 - (-1))", "-4"), ("eq", slope((-1, 5), (2, -4)), "-3")), space=0.5),
        dict(heading="Solve the problem."),
        dict(stem="A roof rises 9 feet over a horizontal distance of 12 feet. What is the slope of the roof?",
             answer="3/4", why="Rise over run: 9/12 = 3/4.",
             check=("eq", "F(9, 12)", "F(3, 4)"), space=0.5),
        dict(heading="Choose one."),
        dict(stem="The table shows a linear relationship. What is its slope?",
             fig=TT([0, 2, 6], [3, 4, 6]),
             choices=["$2$", "$\\frac{1}{2}$", "$-\\frac{1}{2}$", "$1$"], correct=1, answer="B",
             why="(4 − 3) ÷ (2 − 0) = 1/2. Check: (6 − 4) ÷ (6 − 2) = 2/4 = 1/2.",
             check=("many", ("eq", slope((0, 3), (2, 4)), "F(1, 2)"), ("eq", slope((2, 4), (6, 6)), "F(1, 2)"),
                    ("eq", "4 - 3", "1"), ("eq", "(2 - 0)/(4 - 3)", "2"), ("eq", "(3 - 4)/(2 - 0)", "-F(1, 2)")),
             errors={"A": "the change in x over the change in y [B1G-M, AR.3.2: run over rise]", "C": "subtracted in different orders, 3 − 4 over 2 − 0 [Notes III: subtract in the same order]", "D": "the change in y alone, not divided by the change in x [standing decision 5: a table's x-steps are not 1]"}),
        dict(stem="The graph shows a line. What is its slope?",
             fig=PP((-3, 3), (-3, 8), inches=2.6, pt=8.5, lines=[(-4, 3, "")], points=[(-1, 7), (1, -1)]),
             choices=["$-\\frac{1}{4}$", "$4$", "$-8$", "$-4$"], correct=3, answer="D",
             why="(−1 − 7) ÷ (1 − (−1)) = −8 ÷ 2 = −4. The line falls: negative.",
             check=("many", ("eq", slope((-1, 7), (1, -1)), "-4"), on("-4", "3", "-1", "7"), on("-4", "3", "1", "-1"),
                    ("eq", "(1 - (-1))/(-1 - 7)", "-F(1, 4)"), ("eq", "-1 - 7", "-8")),
             errors={"A": "the change in x over the change in y [B1G-M, AR.3.2: run over rise]", "B": "a falling line read as rising [Notes III: a line that falls has a negative slope]", "C": "the change in y alone, not divided by the change in x [Notes I: rise over run]"}),
    ],

    additional=[
        dict(heading="For questions 1 to 4, find the slope of the line through the two points."),
        dict(stem="$(2, -1)$ and $(4, 7)$", answer="4", why="(7 − (−1)) ÷ (4 − 2) = 8 ÷ 2 = 4.",
             check=("eq", slope((2, -1), (4, 7)), "4"), space=0.4),
        dict(stem="$(-3, 2)$ and $(1, -10)$", answer="−3", why="(−10 − 2) ÷ (1 − (−3)) = −12 ÷ 4 = −3.",
             check=("eq", slope((-3, 2), (1, -10)), "-3"), space=0.4),
        dict(stem="$(-6, -2)$ and $(2, 2)$", answer="1/2", why="(2 − (−2)) ÷ (2 − (−6)) = 4 ÷ 8 = 1/2.",
             check=("eq", slope((-6, -2), (2, 2)), "F(1, 2)"), space=0.4),
        dict(stem="$(-5, -3)$ and $(3, -3)$", answer="0", why="(−3 − (−3)) ÷ (3 − (−5)) = 0 ÷ 8 = 0: a horizontal line.",
             check=("eq", slope((-5, -3), (3, -3)), "0"), space=0.4),
        dict(heading="For questions 5 and 6, find the slope of the line."),
        dict(stem="The graph shows a line.",
             fig=PP((-2, 6), (-2, 5), lines=[(Fr(3, 4), 1, "")], points=[(0, 1), (4, 4)]),
             answer="3/4", why="(4 − 1) ÷ (4 − 0) = 3 ÷ 4 = 3/4.",
             check=("many", ("eq", slope((0, 1), (4, 4)), "F(3, 4)"), on("F(3,4)", "1", "0", "1"), on("F(3,4)", "1", "4", "4")),
             space=0.4),
        dict(stem="The graph shows a line.",
             fig=PP((-4, 2), (-3, 4), lines=[(Fr(-3, 2), -1, "")], points=[(-2, 2), (0, -1)]),
             answer="−3/2", why="(−1 − 2) ÷ (0 − (−2)) = −3 ÷ 2 = −3/2.",
             check=("many", ("eq", slope((-2, 2), (0, -1)), "F(-3, 2)"), on("F(-3,2)", "-1", "-2", "2"), on("F(-3,2)", "-1", "0", "-1")),
             space=0.4),
        dict(heading="For questions 7 and 8, find the slope."),
        dict(stem="The table shows a linear relationship.", fig=figs.table([([-3, 0, 3, 6], [6, 2, -2, -6])], head=("x", "y"), inches=3.6),
             answer="−4/3", why="(2 − 6) ÷ (0 − (−3)) = −4 ÷ 3 = −4/3.",
             check=("many", ("eq", slope((-3, 6), (0, 2)), "F(-4, 3)"), table_on("F(-4,3)", "2", [-3, 0, 3, 6], [6, 2, -2, -6])),
             space=0.4),
        dict(stem="The table shows a linear relationship.", fig=TT([-2, 1, 3], [-7, 5, 13]),
             answer="4", why="(5 − (−7)) ÷ (1 − (−2)) = 12 ÷ 3 = 4. Check: (13 − 5) ÷ (3 − 1) = 8 ÷ 2 = 4.",
             check=("many", ("eq", slope((-2, -7), (1, 5)), "4"), ("eq", slope((1, 5), (3, 13)), "4")),
             space=0.4),
        dict(heading="Use similar triangles."),
        dict(stem="A slope triangle on a line has a rise of 3 and a run of 6. A larger slope triangle on the same line has a run of 16. What is its rise?",
             answer="8", why="The slope is 3/6 = 1/2, so the rise is (1/2)(16) = 8.",
             check=("eq", "F(3, 6)*16", "8"), space=0.5),
        dict(heading="Find the missing number."),
        dict(stem="The slope of the line through $(1, 2)$ and $(4, □)$ is −3. Find the missing number.",
             answer="−7", why="The change in x is 4 − 1 = 3, so the change in y is −3(3) = −9, and 2 − 9 = −7.",
             check=("many", ("eq", "2 + (-3)*(4 - 1)", "-7"), ("eq", slope((1, 2), (4, -7)), "-3")), space=0.5),
        dict(heading="Solve the problem."),
        dict(stem="A path rises 15 meters over a horizontal distance of 30 meters. What is the slope of the path?",
             answer="1/2", why="Rise over run: 15/30 = 1/2.",
             check=("eq", "F(15, 30)", "F(1, 2)"), space=0.5),
        dict(heading="Choose one."),
        dict(stem="The table shows a linear relationship. What is its slope?",
             fig=TT([0, 6, 8], [1, 4, 5]),
             choices=["$\\frac{1}{2}$", "$-\\frac{1}{2}$", "$2$", "$3$"], correct=0, answer="A",
             why="(4 − 1) ÷ (6 − 0) = 3/6 = 1/2. Check: (5 − 4) ÷ (8 − 6) = 1/2.",
             check=("many", ("eq", slope((0, 1), (6, 4)), "F(1, 2)"), ("eq", slope((6, 4), (8, 5)), "F(1, 2)"),
                    ("eq", "4 - 1", "3"), ("eq", "(6 - 0)/(4 - 1)", "2"), ("eq", "(1 - 4)/(6 - 0)", "-F(1, 2)")),
             errors={"B": "subtracted in different orders, 1 − 4 over 6 − 0 [Notes III: subtract in the same order]", "C": "the change in x over the change in y [B1G-M, AR.3.2: run over rise]", "D": "the change in y alone, not divided by the change in x [standing decision 5: a table's x-steps are not 1]"}),
        dict(stem="The graph shows a line. What is its slope?",
             fig=PP((-3, 3), (-4, 6), lines=[(-4, 1, "")], points=[(-1, 5), (1, -3)]),
             choices=["$-\\frac{1}{4}$", "$-4$", "$4$", "$-8$"], correct=1, answer="B",
             why="(−3 − 5) ÷ (1 − (−1)) = −8 ÷ 2 = −4. The line falls: negative.",
             check=("many", ("eq", slope((-1, 5), (1, -3)), "-4"), on("-4", "1", "-1", "5"), on("-4", "1", "1", "-3"),
                    ("eq", "(1 - (-1))/(-3 - 5)", "-F(1, 4)"), ("eq", "-3 - 5", "-8")),
             errors={"A": "the change in x over the change in y [B1G-M, AR.3.2: run over rise]", "C": "a falling line read as rising [Notes III: a line that falls has a negative slope]", "D": "the change in y alone, not divided by the change in x [Notes I: rise over run]"}),
    ],

    te=dict(
        must="Students find the slope of a line from a graph with readable points, from a table whose x-values do not go up by 1 and from two points, and they connect slope to similar triangles on the coordinate plane. A slope is positive, negative or 0.",
        must_not="Students do not write an equation of a line or name the y-intercept, which are later lessons of this unit. No vertical line appears, because its slope is an Algebra 1 idea, and no question needs the formula's notation.",
        read_first=[
            "Two book lessons taught as one day. Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §10.02+03, standing decisions 2, 4, 5, 6, 7 and 8), with Math Nation read for scope only.",
            "Today names slope: the rate of change of a line, the change in y divided by the change in x between any two points on it, rise over run. The formula m = (y₂ − y₁)/(x₂ − x₁) is shown once, in Notes III, and no question needs its notation; the words are 'Subtract in the same order.' Every table whose slope is asked has x-values that do not go up by 1, and Example 2, its Your Turn and Independent Set question 4 have unequal steps.",
            "Whiteboard question 6 is the similar-triangles connection: the larger triangle runs past the edge of the grid, so its rise has to be found from the slope, not counted."],
        materials="Whiteboards and markers. The Independent Set, one per student.",
        variation="Boards 1–2 find a slope from two points, and only the second y-value changes, so the slope turns negative. Board 3 votes on a table whose x-values go up by 2, board 4 reads a falling line off a graph, and board 5 votes on a graph. The pattern breaks at 6, where the slope triangle's rise is found past the edge of the grid. Board 7 is a ramp with its width as the extra number, 8 runs backwards, and 9 judges Jo's subtraction, written. The set: two points with negative coordinates, a rising and a falling graph, a table with unequal steps, a missing run, and a horizontal line with slope 0.",
        audit=["Every slope re-derived by sympy at build time as the change in y divided by the change in x, from the printed points; every table's second slope checked against its first; every marked point checked on the line drawn by u10/figs10.py.",
               "Every wrong option is one named error: run over rise, the change in y alone, subtraction in different orders, or a falling line read as rising."],
        changes=["Two book lessons (slope from a graph and a table; slope from two points) → one day: Notes I–III, one Example from a graph and one from a table with unequal steps.",
                 "Practice and Homework → the Independent Set: six questions, one feature changed at a time."],
    ),
)
