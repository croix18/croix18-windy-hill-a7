# MODEL: a lesson with figures — A7 11.07 Solving Systems by Graphing (MA.8.AR.4.3), as built; it imports u11/figs11.py.
# Read with kit/BUILDER CARD.md. Every picture comes from the unit's figure module and is sized for its slide by S();
# a crossing named in the words is given to figs.plane as solution=, which refuses one not on both lines.
# Boards READ a graph or two tables; the Independent Set prints an empty grid (fig) and keys it with fig_key.
# Checks are sympy over the REAL numbers: crosses / never_meet / one_line / sat / fails / table_of below.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs11 as figs          # the unit's figure module (u11/figs11.py)
S = figs.slide
BLUE, ORANGE = figs.BLUE, figs.ORANGE

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


def crosses(r1, r2, x, y):
    """The system y = r1, y = r2 has exactly one solution, (x, y)."""
    return ("true", "sp.solve([sp.Eq(" + Y + ", " + _u(r1) + "), sp.Eq(" + Y + ", " + _u(r2) + ")], [" + X + ", " + Y
            + "], dict=True) == [{" + X + ": " + x + ", " + Y + ": " + y + "}]")


def never_meet(r1, r2):
    """The system y = r1, y = r2 has no solution (parallel lines)."""
    return ("true", "sp.solve([sp.Eq(" + Y + ", " + _u(r1) + "), sp.Eq(" + Y + ", " + _u(r2) + ")], [" + X + ", " + Y
            + "], dict=True) == []")


def meets(r1, r2):
    """The system y = r1, y = r2 HAS a solution (one, or infinitely many) — a select-all's wrong option."""
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


H = Fr(1, 2)

# ---- the board figures: as large as the slide allows. B() for the question slide, BA() for the reveal (room for the
# red answer line), BM() for a multiple-choice board. A choice board sets its options beside its figure.


def B(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.75)


def BA(spec):
    """The reveal: the same size, with the room the red answer line needs under it."""
    return S(spec, inches=4.2, pt=18, reserve=0.95)


def BM(spec, reserve=0.75):
    return S(spec, inches=4.2, pt=14, reserve=reserve)


# ---- the notes and examples
NOTES1 = S(figs.row([figs.table([([0, 1, 2], [-1, 1, 3])], titles=["y = 2x − 1"]),
                     figs.plane((-2, 4), (-3, 6), lines=[(2, -1)],
                                points=[(0, -1, None, "r"), (1, 1, None, "r"), (2, 3, None, "r")])],
                    gap=1.8), inches=7.4, pt=17, reserve=1.05)
NOTES2 = S(figs.row([figs.table([([0, 1, 2], [1, 2, 3]), ([0, 1, 2], [7, 5, 3])], titles=["y = x + 1", "y = −2x + 7"]),
                     figs.plane((-1, 5), (-1, 8), lines=[(1, 1), (-2, 7)], solution=(2, 3),
                                points=[(2, 3, None, "r"), (0, 1, ""), (1, 2, ""), (0, 7, ""), (1, 5, "")])],
                    gap=1.8), inches=9.6, pt=16, reserve=1.0)
# An Example's question slide: the tables with their y's EMPTY and an empty grid — the teacher fills and draws them.
EX1 = S(figs.row([figs.table([([0, 1, 2], ["", "", ""]), ([0, 1, 2], ["", "", ""])], titles=["y = 2x − 3", "y = −x + 6"]),
                  figs.plane((0, 5), (-3, 6))],
                 gap=1.8), inches=7.2, pt=16, reserve=0.9)
EX2 = S(figs.row([figs.table([([0, 2, 4], ["", "", ""]), ([0, 2, 4], ["", "", ""])], titles=["y = ½x + 1", "y = −x + 4"]),
                  figs.plane((-1, 5), (-1, 5))],
                 gap=1.8), inches=9.6, pt=16, reserve=0.9)

# A worked entry's fig: the finished graph beside the rows, the crossing marked and named.
EX1W = S(figs.plane((0, 5), (-3, 7), lines=[(2, -3), (-1, 6)], solution=(3, 3),
                    points=[(0, -3, ""), (1, -1, ""), (2, 1, ""), (0, 6, ""), (1, 5, ""), (2, 4, ""), (3, 3, None, "r")]),
         inches=4.6, pt=16, reserve=0.9)
EX2W = S(figs.plane((-1, 5), (-1, 5), lines=[(H, 1), (-1, 4)], solution=(2, 2),
                    points=[(0, 1, ""), (4, 3, ""), (0, 4, ""), (4, 0, ""), (2, 2, None, "r+")]),
         inches=4.6, pt=16, reserve=0.9)
# A Your Turn: fig (tables filled, an empty grid) on the question slide, fig_a (the graph drawn) on the answer slide.
YT1_T = figs.table([([0, 1, 2], [-2, -1, 0]), ([0, 1, 2], [6, 3, 0])], titles=["y = x − 2", "y = −3x + 6"], cw=2.0, rh=1.6)
YT1 = S(figs.row([YT1_T, figs.plane((-1, 3), (-2, 7), step=2)], gap=1.8), inches=6.4, pt=15, reserve=0.9)
YT1A = S(figs.plane((-1, 3), (-2, 7), lines=[(1, -2), (-3, 6, "y = −3x + 6", (1, "ur"))], solution=(2, 0),
                    points=[(0, -2, ""), (1, -1, ""), (0, 6, ""), (1, 3, ""), (2, 0, None, "dr")]),
         inches=4.6, pt=16, reserve=0.9)
YT2_T = figs.table([([0, 2, 4], [3, 4, 5]), ([0, 2, 4], [9, 7, 5])], titles=["y = ½x + 3", "y = −x + 9"], cw=2.0, rh=1.6)
YT2 = S(figs.row([YT2_T, figs.plane((-1, 6), (0, 10), step=2)], gap=1.8), inches=6.4, pt=15, reserve=0.9)
YT2A = S(figs.plane((-1, 6), (0, 10), lines=[(H, 3), (-1, 9)], solution=(4, 5),
                    points=[(0, 3, ""), (2, 4, ""), (0, 9, ""), (2, 7, ""), (4, 5, None, "r+")]),
         inches=4.6, pt=16, reserve=0.9)

# ---- the boards
P1 = figs.plane((-1, 5), (-1, 6), lines=[(1, 2), (-1, 6)], solution=(2, 4))
P1A = figs.plane((-1, 5), (-1, 6), lines=[(1, 2), (-1, 6)], solution=(2, 4), points=[(2, 4, None, "r")])
T2 = figs.table([([0, 1, 2, 3, 4], [-5, -2, 1, 4, 7]), ([0, 1, 2, 3, 4], [1, 2, 3, 4, 5])],
                titles=["y = 3x − 5", "y = x + 1"])
P3 = figs.plane((-5, 2), (-4, 4), lines=[(2, 4), (-1, -2)], solution=(-2, 0), step=2)
P3A = figs.plane((-5, 2), (-4, 4), lines=[(2, 4), (-1, -2)], solution=(-2, 0), step=2, points=[(-2, 0, "")])
P4 = figs.plane((-1, 4), (-1, 5), lines=[(-2, 5, ""), (1, -1, "")], solution=(2, 1))
P4A = figs.plane((-1, 4), (-1, 5), lines=[(-2, 5, ""), (1, -1, "")], solution=(2, 1), points=[(2, 1, "")])
P5 = figs.plane((-2, 3), (-3, 4), lines=[(2, 2), (2, -3)])
P6 = figs.plane((-1, 4), (-1, 5), lines=[(2, 1, ""), (-1, 4, "")], solution=(1, 3),
                points=[(0, 1, ""), (1, 3, ""), (0, 4, ""), (2, 2, "")])
P7 = figs.plane((0, 8), (0, 12), lines=[(-2, 12, "A: y = −2x + 12", (1, "ur")), (-1, 8, "B: y = −x + 8", (5, "ur"))],
                ys=2, xname="hours", yname="height (cm)", solution=(4, 4))
P7A = figs.plane((0, 8), (0, 12), lines=[(-2, 12, "A: y = −2x + 12", (1, "ur")), (-1, 8, "B: y = −x + 8", (5, "ur"))],
                 ys=2, xname="hours", yname="height (cm)", solution=(4, 4), points=[(4, 4, None, "dl")])


# ---- the Independent Set: an empty grid for each system a student graphs; the key (fig_key) draws on the same window.
def GRID(xr, yr):
    return figs.plane(xr, yr, inches=3.2)


def KEY(xr, yr, lines, solution=None, where=None):
    """The key's own figure (fig_key): the student's grid with both lines drawn from their equations
    and the crossing marked and named; `plane` refuses a crossing that is not on both lines. A same-line system draws
    its second equation dashed over the first, with no second label."""
    pts = ([(solution[0], solution[1], None, where)] if where else [(solution[0], solution[1])]) if solution else []
    return figs.plane(xr, yr, lines=lines, solution=solution, points=pts, inches=3.2)


L = dict(
    code="11.07", unit=11, lesson_no=7,
    align="=",
    title="Solving Systems by Graphing",
    unit_title="Solving Equations and Systems",
    benchmark="MA.8.AR.4.3",
    benchmark_text="Given a mathematical or real-world context, solve systems of two linear equations by graphing.",
    target="I can solve a system of two equations by graphing both lines and reading where they cross.",
    essential="Why is the point where two lines cross the one pair that makes both equations true?",
    building_on="Lessons 11.05–06 showed that a solution of a system makes both equations true, and read from a graph whether a system has one solution, no solution or infinitely many solutions. Lesson 11.02 solved equations of the form mx + b = nx + c.",
    working_toward="Lesson 11.08 solves systems in context and estimates a point of intersection that falls between the grid lines. In Unit 10 (January), the coefficient of x is named the slope. In Algebra 1 (MA.912.AR.9.1), students solve systems by substitution and elimination.",
    vocab=[("table of values", "x-values you choose and the y each one gives: $x = 0$ first, then two more"),
           ("solve by graphing", "graph both equations on one grid; the point of intersection — where the lines intersect — is the solution"),
           ("coefficient of x", "the number that multiplies x: 3 in $y = 3x - 1$, −1 in $y = -x + 4$, 0 in $y = 4$"),
           ("parallel lines", "the same coefficient of x and different numbers added: the same steepness in the same direction, never meeting")],
    ixl=["Solve a system of equations by graphing — C8X", "Write a system of equations given a graph — TS7"],
    closure="Whiteboard question 9 is answered in writing and serves as the exit ticket. A complete answer says that Tia is not right and gives the reason: the coefficient of x is 3 in both equations, so for every x the second line is 3 units above the first. The lines are parallel and never meet, on the grid or off it, so the system has no solution. An answer of \"no\" with no reason is not complete.",

    mtr=[("MTR.2.1", "Students find one point of intersection from a table, from a graph and from an equation."),
         ("MTR.4.1", "On whiteboard questions 4 and 6, a divided class has one minute to convince a neighbor and then votes again."),
         ("MTR.6.1", "Students check every point of intersection in both equations.")],
    hoq=[("Why does a third point in each table matter before you draw the line?", "DOK 2"),
         ("Why must two lines with different coefficients of x cross somewhere, even off the grid?", "DOK 3"),
         ("Whiteboard question 2 needs no graph. Where in the two tables do you see the solution?", "DOK 2"),
         ("y = ½x + 1 and y = 0.5x + 1 look different. How can you show they are one line without drawing either?", "DOK 2")],
    differentiation=[
        ("ESE / 504", "Provide a printed blank table, with x = 0, 1 and 2 already written, beside each grid. Students draw each line in pencil before ink. Keep Notes II on display from whiteboard question 1 on."),
        ("ELL", "**Table of values**: the x-values you choose and the y-value each one gives. **Intersect**: cross, or meet at one point. **Check**: put the point into both equations. **Parallel**: like train tracks, which never meet."),
        ("Enrichment", "Students who finish whiteboard question 6 early write a second equation that makes a system with y = 2x − 1 whose solution is (3, 5), and then one that makes a system with no solution. Possible answers are any line through (3, 5) with a different coefficient of x, such as y = −x + 8, and y = 2x plus any number other than −1, such as y = 2x + 3.")],

    warmup=[
        dict(stem="Is $(1, 5)$ a solution of  $y = 2x + 3$  and  $y = x + 4$?", answer="Yes",
             check=("many", sat("2*u + 3", "1", "5"), sat("u + 4", "1", "5"))),
        dict(stem="Solve for x:  $0.5(6x + 4) = x + 8$", answer="x = 3",
             check=("eq", "sp.solve(sp.Eq(F(1,2)*(6*" + X + " + 4), " + X + " + 8), " + X + ")[0]", "3")),
        dict(stem="A right triangle has legs 9 and 12. Find the hypotenuse.", answer="15",
             check=("eq", "sqrt(9**2 + 12**2)", "15")),
        dict(stem="For  $y = 2x - 1$,  find y when x is 0, 1 and 2.", answer="−1, 1, 3",
             check=("many", ("eq", "2*0 - 1", "-1"), ("eq", "2*1 - 1", "1"), ("eq", "2*2 - 1", "3"))),
    ],

    notes=[
        dict(numeral="I", head="A line from a table", min=3,
             fig=NOTES1,
             items2=["Three points in a row: the third is the check.   Draw the line past them."],
             letters=False),
        dict(numeral="II", head="Solve by graphing", min=3,
             fig=NOTES2,
             items2=["$(2, 3)$:   $2 + 1 = 3$   and   $-2(2) + 7 = 3$.   The solution."],
             letters=False),
        # Notes III: no picture; reasons from the equations, and the one algebra bridge, shown not practiced.
        dict(numeral="III", head="Not one crossing; and the check without a graph", min=3,
             items=[("Parallel, none", "same coefficient of x, different numbers added"),
                    ("One line, infinitely many", "one equation written two ways")],
             math=["$x + 1 = -2x + 7$", "$3x + 1 = 7$", "$3x = 6$", "$x = 2$"],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=2,
             prompt=["$y = 2x - 3$   and   $y = -x + 6$"], fig=EX1, ask="Solve the system by graphing.",
             worked=[dict(min=1,
                          rows=[("y = 2x - 3:\\quad -3,\\ -1,\\ 1", "at x = 0, 1, 2"),
                                ("y = -x + 6:\\quad 6,\\ 5,\\ 4", "at x = 0, 1, 2"),
                                ("(3, 3):\\quad 2(3) - 3 = 3", "on the first line"),
                                ("-3 + 6 = 3", "on the second: the crossing, checked")],
                          fig=EX1W, answer="(3, 3)")],
             check=("many", crosses("2*u - 3", "-u + 6", "3", "3"), table_of("2*u - 3", [0, 1, 2], [-3, -1, 1]),
                    table_of("-u + 6", [0, 1, 2], [6, 5, 4])),
             # its crossing is inside the tables, where the two rows agree; then everyone draws Independent Set question 1
             your_turn=dict(min=5,
                            prompt=["Where do  $y = x - 2$  and  $y = -3x + 6$  cross?"], fig=YT1, fig_a=YT1A, ask="",
                            steps=["at $x = 2$:   $2 - 2 = 0$   and   $-3(2) + 6 = 0$",
                                   "the lines cross at $(2, 0)$"],
                            answer="(2, 0)"),
             yt_check=("many", crosses("u - 2", "-3*u + 6", "2", "0"), table_of("u - 2", [0, 1, 2], [-2, -1, 0]),
                       table_of("-3*u + 6", [0, 1, 2], [6, 3, 0]))),
        dict(title="Example 2", min_q=1,
             prompt=["$y = \\frac{1}{2}x + 1$   and   $y = -x + 4$"], fig=EX2, ask="Solve the system by graphing.",
             worked=[dict(min=2,
                          rows=[("y = \\frac{1}{2}x + 1:\\quad 1,\\ 2,\\ 3", "at x = 0, 2, 4"),
                                ("y = -x + 4:\\quad 4,\\ 2,\\ 0", "at x = 0, 2, 4"),
                                ("(2, 2):\\quad \\frac{1}{2}(2) + 1 = 2", "on the first line"),
                                ("-2 + 4 = 2", "on the second: the crossing, checked")],
                          fig=EX2W, answer="(2, 2)")],
             check=("many", crosses("F(1,2)*u + 1", "-u + 4", "2", "2"), table_of("F(1,2)*u + 1", [0, 2, 4], [1, 2, 3]),
                    table_of("-u + 4", [0, 2, 4], [4, 2, 0])),
             # the Your Turn crosses inside the table the example models (x = 0, 2, 4)
             your_turn=dict(min=2,
                            prompt=["Where do  $y = \\frac{1}{2}x + 3$  and  $y = -x + 9$  cross?"], fig=YT2, fig_a=YT2A, ask="",
                            steps=["at $x = 4$:   $\\frac{1}{2}(4) + 3 = 5$   and   $-4 + 9 = 5$"],
                            answer="(4, 5)"),
             yt_check=("many", crosses("F(1,2)*u + 3", "-u + 9", "4", "5"), table_of("F(1,2)*u + 3", [0, 2, 4], [3, 4, 5]),
                       table_of("-u + 9", [0, 2, 4], [9, 7, 5]))),
    ],

    # The round: a crossing read off a graph (1) and off two tables (2); a crossing on an axis (3); a vote on the four
    # points a graph offers (4); the pattern breaks at 5 — parallel, none; 6 votes on the system through four marked points;
    # the candle story, its price the extra number (7); backwards (8); the "they must cross off the grid" claim, written (9).
    whiteboard=[
        # repeat_ok: rule D matches only the grid's axis numbers (−1 to 6, shared by the planes today) and the
        # answer's digits; this system (y = x + 2, y = −x + 6) appears nowhere above.
        dict(repeat_ok=True, text=["**The system is graphed. What is its solution?"],
             fig=B(P1), fig_a=BA(P1A),
             steps=["the lines cross at $(2, 4)$", "$2 + 2 = 4$   and   $-2 + 6 = 4$"],
             answer="(2, 4)",
             check=("many", crosses("u + 2", "-u + 6", "2", "4"), sat("u + 2", "2", "4"), sat("-u + 6", "2", "4")),
             wrong="(4, 2) — x and y swapped [B1G-M, GR.1.2: x and y inverted]; (0, 6) — where one line meets the y-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]"),
        # repeat_ok: rule D matches only the table's x row (0 to 4) and the answer's digits; this system appears
        # nowhere above.
        dict(repeat_ok=True, text=["**The tables are for one system. What is its solution?"],
             qtext="The two tables are for one system: y = 3x − 5 and y = x + 1. What is the solution of the system?",
             fig=S(T2, inches=8.0, pt=18, reserve=0.75), fig_a=S(T2, inches=6.6, pt=15, reserve=0.95),
             steps=["at $x = 3$:   $3(3) - 5 = 4$   and   $3 + 1 = 4$"],
             answer="(3, 4)",
             wrong="(4, 3) — the coordinates of (3, 4) swapped [B1G-M, GR.1.2: x and y inverted]; (2, 1) — the column where the tables are closest but not equal, read from y = 3x − 5 only: x + 1 gives 3 there [B1G-M, AR.4.1: a solution satisfies both]; (4, 4) — the shared y, 4, written for x too [B1G-M, GR.1.2: x and y inverted]",
             check=("many", crosses("3*u - 5", "u + 1", "3", "4"), table_of("3*u - 5", [0, 1, 2, 3, 4], [-5, -2, 1, 4, 7]),
                    table_of("u + 1", [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]),
                    fails("3*u - 5", "4", "3"), fails("u + 1", "4", "3"),
                    sat("3*u - 5", "2", "1"), fails("u + 1", "2", "1"),
                    fails("3*u - 5", "4", "4"), fails("u + 1", "4", "4"))),
        # repeat_ok: rule D matches only the grid's axis numbers and the answer's digits; the system is new.
        dict(repeat_ok=True, text=["**The system is graphed. What is its solution?"],
             fig=B(P3), fig_a=BA(P3A),
             steps=["the lines cross at $(-2, 0)$", "$2(-2) + 4 = 0$   and   $-(-2) - 2 = 0$"],
             answer="(−2, 0)",
             check=("many", crosses("2*u + 4", "-u - 2", "-2", "0"), sat("2*u + 4", "-2", "0"), sat("-u - 2", "-2", "0")),
             wrong="(0, −2) — x and y swapped, and where one line meets the y-axis [B1G-M, GR.1.2: x and y inverted]; (0, 4) — where one line meets the y-axis [B1G-M, AR.4.1: a solution satisfies both]"),
        # repeat_ok: rule D matches only the grid's axis numbers and the options' digits; the system is new.
        dict(repeat_ok=True, kind="mc", text=["**$y = -2x + 5$  and  $y = x - 1$  are graphed. Which is the solution?"],
             qtext="y = −2x + 5 and y = x − 1 are graphed. Which ordered pair is the solution of the system?",
             fig=B(P4), fig_a=BA(P4A),
             steps=["the lines cross at $(2, 1)$", "$-2(2) + 5 = 1$   and   $2 - 1 = 1$"],
             choices=["(0, 5)", "(1, 2)", "(2, 1)", "(1, 0)"], correct=2, answer="C — (2, 1)",
             errors={"A": "where y = −2x + 5 meets the y-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]", "B": "the coordinates of the crossing swapped [B1G-M, GR.1.2: x and y inverted]", "D": "where y = x − 1 meets the x-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]"},
             check=("many", crosses("-2*u + 5", "u - 1", "2", "1"), sat("-2*u + 5", "2", "1"), sat("u - 1", "2", "1"),
                    fails("-2*u + 5", "1", "2"), fails("u - 1", "1", "2"),
                    sat("-2*u + 5", "0", "5"), fails("u - 1", "0", "5"),
                    sat("u - 1", "1", "0"), fails("-2*u + 5", "1", "0"))),
        # repeat_ok: rule D matches only the grid's axis numbers; the system is new.
        dict(repeat_ok=True, text=["**The system is graphed. Solve the system."],
             fig=B(P5), fig_a=BA(P5),
             steps=["$2x + 2$ and $2x - 3$:  2 multiplies x in both", "parallel:  they never meet"],
             answer="No solution. The lines are parallel.",
             check=never_meet("2*u + 2", "2*u - 3"),
             wrong="a point such as (0, 2) — a point of one line read as the answer [B1G-M, AR.4.3: plotting and graphing errors]; infinitely many — 'the lines go on forever' [B1G-M, AR.4.2: the same-line case]"),
        # repeat_ok: rule D matches the grid's axis numbers and the four marked points; the system is new.
        dict(repeat_ok=True, kind="mc", text=["Four points on the lines are marked.",
                                              "**Which system is graphed?"],
             qtext="The graph shows two lines with four of their points marked. Which system is graphed?",
             fig=B(P6), fig_a=BA(P6),
             steps=["first line:   $2(0) + 1 = 1$   and   $2(1) + 1 = 3$",
                                                  "second line:   $-(0) + 4 = 4$   and   $-2 + 4 = 2$"],
             choices=["y = 2x + 1 and y = −x + 4", "y = x + 2 and y = 4x − 1", "y = x + 2 and y = −x + 4", "y = 2x + 1 and y = x + 4"],
             correct=0, answer="A — y = 2x + 1 and y = −x + 4",
             errors={"B": "the two numbers of each equation swapped [B1G-M, AR.3.3: which value is which]", "C": "a first line tested at (1, 3) only: x + 2 is 2 at x = 0, not 1 [B1G-M, AR.4.3: plotting and graphing errors]", "D": "the falling line written rising: x + 4 grows as x grows [B1G-M, AR.4.3: plotting and graphing errors]"},
             check=("many", sat("2*u + 1", "0", "1"), sat("2*u + 1", "1", "3"), sat("-u + 4", "0", "4"), sat("-u + 4", "2", "2"),
                    crosses("2*u + 1", "-u + 4", "1", "3"),
                    sat("u + 2", "1", "3"), fails("u + 2", "0", "1"),
                    fails("u + 4", "2", "2"), fails("u + 4", "1", "3"),
                    fails("4*u - 1", "2", "2"))),
        dict(text=["Candle A cost \\$3. The graph shows both candles' heights.",
                   "**When are the two candles the same height?"],
             unneeded="3",
             fig=S(P7, inches=5.0, pt=16, reserve=0.75), fig_a=S(P7A, inches=5.0, pt=16, reserve=1.1),
             steps=["A:   $-2(4) + 12 = 4$", "B:   $-4 + 8 = 4$"],
             answer="After 4 hours, both are 4 cm tall.",
             check=("many", crosses("-2*u + 12", "-u + 8", "4", "4"), sat("-2*u + 12", "4", "4"), sat("-u + 8", "4", "4")),
             wrong="'after 3 hours' — candle A's price taken as the time [an extra number, included on purpose]; 'at 8 cm' — where candle B starts, on one line only [B1G-M, AR.4.1: a solution satisfies both]"),
        dict(text=["$(2, 5)$ is the solution of  $y = 2x + 1$  and  $y = -x + □$.", "**What number goes in the box?"],
             steps=["$2(2) + 1 = 5$", "$-2 + 7 = 5$"],
             answer="7",
             check=("many", ("eq", "5 + 2", "7"), crosses("2*u + 1", "-u + 7", "2", "5")),
             wrong="3 — 5 − 2, the −x taken the wrong way [B1G-M, AR.4.1: substitution errors]; 5 — the y copied into the box [B1G-M, AR.4.1: substitution errors]"),
        dict(kind="written", text=["Tia graphed  $y = 3x - 2$  and  $y = 3x + 1$.  She says the lines must",
                                   "cross somewhere off her grid.", "**Is Tia right? Explain."],
             qtext="Tia graphed y = 3x − 2 and y = 3x + 1. She says the lines must cross somewhere off her grid. Is Tia right? Explain.",
             steps=["3 multiplies x in both:  each line climbs 3 for every 1 across",
                                                             "at $x = 0$:   $-2$ and $1$;   at $x = 10$:   $28$ and $31$",
                                                             "always 3 apart:  parallel, no solution"],
             answer="No. Parallel lines never meet.",
             check=("many", never_meet("3*u - 2", "3*u + 1"), one_line("(3*u + 1) - (3*u - 2)", "3"),
                    ("eq", "3*10 - 2", "28"), ("eq", "3*10 + 1", "31")),
             wrong="'yes, they meet off the grid' — two lines taken to always meet [B1G-M, AR.4.3: plotting and graphing errors]"),
    ],

    # The six: graph and solve with a whole crossing (1), with negative coordinates (2), with a ½ multiplying x (3);
    # the pattern breaks — parallel, no solution (4) and one line twice, infinitely many (5); and two tables read to
    # the solution (6). Each of 1–5 prints an empty grid and room for two tables beside it (decision 9).
    independent=[
        dict(stem="Solve by graphing:   $y = x + 3$   and   $y = -2x + 6$",
             fig=GRID((-2, 5), (-1, 7)), fig_key=KEY((-2, 5), (-1, 7), [(1, 3), (-2, 6)], (1, 4)),
             answer="(1, 4)", why="Tables at x = 0, 1, 2: y = 3, 4, 5 and y = 6, 4, 2. The lines cross at (1, 4): 1 + 3 = 4 and −2(1) + 6 = 4.",
             check=("many", crosses("u + 3", "-2*u + 6", "1", "4"), table_of("u + 3", [0, 1, 2], [3, 4, 5]), table_of("-2*u + 6", [0, 1, 2], [6, 4, 2])),
             space=0.3),
        dict(stem="Solve by graphing:   $y = x - 1$   and   $y = -2x - 4$.   Use $x = -2$, $-1$ and $0$.",
             fig=GRID((-4, 3), (-5, 4)), fig_key=KEY((-4, 3), (-5, 4), [(1, -1), (-2, -4)], (-1, -2), "l+"),
             answer="(−1, −2)", why="Tables at x = −2, −1, 0: y = −3, −2, −1 and y = 0, −2, −4. The lines cross at (−1, −2): −1 − 1 = −2 and −2(−1) − 4 = −2.",
             check=("many", crosses("u - 1", "-2*u - 4", "-1", "-2"), table_of("u - 1", [-2, -1, 0], [-3, -2, -1]), table_of("-2*u - 4", [-2, -1, 0], [0, -2, -4])),
             space=0.3),
        dict(stem="Solve by graphing:   $y = \\frac{1}{2}x - 1$   and   $y = -x + 5$",
             fig=GRID((-1, 6), (-2, 6)), fig_key=KEY((-1, 6), (-2, 6), [(H, -1), (-1, 5)], (4, 1), "u++"),
             answer="(4, 1)", why="Even x for the ½: at x = 0, 2, 4, y = −1, 0, 1 and y = 5, 3, 1. The lines cross at (4, 1): ½(4) − 1 = 1 and −4 + 5 = 1.",
             check=("many", crosses("F(1,2)*u - 1", "-u + 5", "4", "1"), table_of("F(1,2)*u - 1", [0, 2, 4], [-1, 0, 1]), table_of("-u + 5", [0, 2, 4], [5, 3, 1])),
             space=0.3),
        dict(stem="Solve by graphing:   $y = -x + 4$   and   $y = -x - 1$",
             fig=GRID((-3, 5), (-4, 6)), fig_key=KEY((-3, 5), (-4, 6), [(-1, 4), (-1, -1, "y = −x − 1", (0, "ur"))]),
             answer="No solution", why="−1 multiplies x in both: the lines are parallel, always 5 apart, and never meet.",
             check=never_meet("-u + 4", "-u - 1"), space=0.3),
        dict(stem="Solve by graphing:   $y = 2x - 5$   and   $y = -5 + 2x$",
             fig=GRID((0, 5), (-5, 5)), fig_key=KEY((0, 5), (-5, 5), [(2, -5), (2, -5, "")]),
             answer="Infinitely many solutions", why="−5 + 2x is 2x − 5: the two tables are the same (−5, −3, −1 at x = 0, 1, 2), so the graphs are one line, and every point of it is a solution.",
             check=("many", one_line("2*u - 5", "-5 + 2*u"), table_of("2*u - 5", [0, 1, 2], [-5, -3, -1])), space=0.3),
        dict(stem="The tables are for $y = 4x - 6$ and $y = x + 3$. What is the solution of the system?",
             fig=figs.table([([0, 1, 2, 3, 4], [-6, -2, 2, 6, 10]), ([0, 1, 2, 3, 4], [3, 4, 5, 6, 7])],
                            titles=["y = 4x − 6", "y = x + 3"], inches=5.2),
             answer="(3, 6)", why="At x = 3 both tables give 6: 4(3) − 6 = 6 and 3 + 6 = 6.",
             check=("many", crosses("4*u - 6", "u + 3", "3", "6"), table_of("4*u - 6", [0, 1, 2, 3, 4], [-6, -2, 2, 6, 10]),
                    table_of("u + 3", [0, 1, 2, 3, 4], [3, 4, 5, 6, 7])), space=0.5),
    ],

    # Bank: two crossings read off a graph (1–2), two tables (3), a parallel pair and one line twice (4–5), two
    # systems to graph on an empty grid (6–7, the second with a ½), backwards (8), a story's crossing (9), the
    # diagnostic on a graph's four points (10), the system a graph shows (11), and a select-all of the systems
    # with no solution (12). The additional bank mirrors it position by position with new numbers.
    bank=[
        dict(heading="For questions 1 and 2, the system is graphed. What is its solution?"),
        dict(stem="$y = x + 4$   and   $y = -x + 2$",
             fig=figs.plane((-4, 3), (-1, 6), lines=[(1, 4), (-1, 2)], solution=(-1, 3), inches=2.6),
             answer="(−1, 3)", why="The lines cross at (−1, 3): −1 + 4 = 3 and −(−1) + 2 = 3.",
             check=crosses("u + 4", "-u + 2", "-1", "3"), space=0.4),
        dict(stem="$y = 3x - 2$   and   $y = -x + 6$",
             fig=figs.plane((-1, 4), (-2, 7), lines=[(3, -2), (-1, 6)], solution=(2, 4), inches=2.6),
             answer="(2, 4)", why="The lines cross at (2, 4): 3(2) − 2 = 4 and −2 + 6 = 4.",
             check=crosses("3*u - 2", "-u + 6", "2", "4"), space=0.4),
        dict(heading="Use the tables."),
        dict(stem="The tables are for $y = 2x + 5$ and $y = 4x + 1$. What is the solution of the system?",
             fig=figs.table([([0, 1, 2, 3, 4], [5, 7, 9, 11, 13]), ([0, 1, 2, 3, 4], [1, 5, 9, 13, 17])],
                            titles=["y = 2x + 5", "y = 4x + 1"], inches=5.2),
             answer="(2, 9)", why="At x = 2 both tables give 9: 2(2) + 5 = 9 and 4(2) + 1 = 9.",
             check=("many", crosses("2*u + 5", "4*u + 1", "2", "9"), table_of("2*u + 5", [0, 1, 2, 3, 4], [5, 7, 9, 11, 13]),
                    table_of("4*u + 1", [0, 1, 2, 3, 4], [1, 5, 9, 13, 17])), space=0.4),
        dict(heading="For questions 4 and 5, the system is graphed. How many solutions does it have?"),
        dict(stem="$y = -2x + 3$   and   $y = -2x - 1$",
             fig=figs.plane((-2, 3), (-8, 8), lines=[(-2, 3), (-2, -1)], ys=2, inches=2.2),
             answer="No solution", why="Parallel: −2 multiplies x in both, so the lines never meet.",
             check=never_meet("-2*u + 3", "-2*u - 1"), space=0.4),
        dict(stem="$y = -x + 3$   and   $y = 3 - x$   (both graph as the line shown)",
             fig=figs.plane((-2, 5), (-2, 5), lines=[(-1, 3, "")], inches=2.0),
             answer="Infinitely many solutions", why="3 − x is −x + 3: one line, and every point of it makes both true.",
             check=one_line("-u + 3", "3 - u"), space=0.4),
        dict(heading="For questions 6 and 7, graph both lines on the grid and solve the system."),
        dict(stem="$y = x - 3$   and   $y = -2x + 3$",
             fig=GRID((-2, 5), (-4, 4)), fig_key=KEY((-2, 5), (-4, 4), [(1, -3), (-2, 3)], (2, -1)),
             answer="(2, −1)", why="Tables at x = 0, 1, 2: y = −3, −2, −1 and y = 3, 1, −1. Both give −1 at x = 2: 2 − 3 = −1 and −2(2) + 3 = −1.",
             check=("many", crosses("u - 3", "-2*u + 3", "2", "-1"), table_of("u - 3", [0, 1, 2], [-3, -2, -1]), table_of("-2*u + 3", [0, 1, 2], [3, 1, -1])),
             space=0.9),
        dict(stem="$y = \\frac{1}{2}x + 2$   and   $y = -x + 5$",
             fig=GRID((-1, 6), (-1, 6)), fig_key=KEY((-1, 6), (-1, 6), [(H, 2), (-1, 5)], (2, 3), "r+"),
             answer="(2, 3)", why="Even x: at x = 0, 2, 4, y = 2, 3, 4 and y = 5, 3, 1. Both give 3 at x = 2: ½(2) + 2 = 3 and −2 + 5 = 3.",
             check=("many", crosses("F(1,2)*u + 2", "-u + 5", "2", "3"), table_of("F(1,2)*u + 2", [0, 2, 4], [2, 3, 4]), table_of("-u + 5", [0, 2, 4], [5, 3, 1])),
             space=0.9),
        dict(heading="Find the missing number."),
        dict(stem="The solution of the system  $y = x - 1$  and  $y = -2x + □$  is $(3, 2)$. What number goes in the box?", answer="8",
             why="Put (3, 2) into the second equation: 2 is −6 plus the box, so the box is 8. Check the first equation: 3 − 1 = 2.",
             check=("many", ("eq", "2 + 6", "8"), crosses("u - 1", "-2*u + 8", "3", "2")), space=0.6),
        dict(heading="Solve the problem."),
        dict(stem="Tank A holds $y = -2x + 10$ gallons after x minutes, and Tank B holds $y = x + 1$ gallons. When do the tanks hold the same amount, and how much is in each?",
             fig=figs.plane((0, 6), (0, 10), lines=[(-2, 10, "A", (1, "ur")), (1, 1, "B")], ys=2, xname="minutes", yname="gallons",
                            solution=(3, 4), inches=2.6),
             answer="After 3 minutes, 4 gallons each.", why="The lines cross at (3, 4): −2(3) + 10 = 4 and 3 + 1 = 4.",
             check=("many", crosses("-2*u + 10", "u + 1", "3", "4")), space=0.5),
        dict(heading="Choose one."),
        dict(stem="The system $y = 3x - 3$ and $y = -x + 5$ is graphed. What is its solution?",
             fig=figs.plane((-1, 4), (-4, 6), lines=[(3, -3), (-1, 5)], solution=(2, 3), inches=2.2),
             choices=["$(3, 2)$", "$(2, 3)$", "$(0, 5)$", "$(1, 0)$"], correct=1, answer="B",
             why="The lines cross at (2, 3): 3(2) − 3 = 3 and −2 + 5 = 3.",
             check=("many", crosses("3*u - 3", "-u + 5", "2", "3"), fails("3*u - 3", "3", "2"), sat("-u + 5", "0", "5"), fails("3*u - 3", "0", "5"),
                    sat("3*u - 3", "1", "0"), fails("-u + 5", "1", "0")),
             errors={"A": "the coordinates of the crossing swapped [B1G-M, GR.1.2: x and y inverted]", "C": "where y = −x + 5 meets the y-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]", "D": "where y = 3x − 3 meets the x-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]"}),
        dict(stem="One line passes through $(0, 1)$ and $(1, 4)$; the other passes through $(0, 5)$ and $(2, 3)$. Which system is graphed?",
             fig=figs.plane((-1, 4), (-1, 6), lines=[(3, 1, ""), (-1, 5, "")], solution=(1, 4),
                            points=[(0, 1, None, "r"), (1, 4, None, "r"), (0, 5, None, "ur"), (2, 3, None, "dl")], inches=2.4),
             choices=["$y = 3x + 1$ and $y = x + 5$", "$y = x + 3$ and $y = 5x - 1$", "$y = x + 3$ and $y = -x + 5$", "$y = 3x + 1$ and $y = -x + 5$"],
             correct=3, answer="D",
             why="3(0) + 1 = 1 and 3(1) + 1 = 4; −0 + 5 = 5 and −2 + 5 = 3.",
             check=("many", sat("3*u + 1", "0", "1"), sat("3*u + 1", "1", "4"), sat("-u + 5", "0", "5"), sat("-u + 5", "2", "3"),
                    fails("u + 3", "0", "1"), fails("u + 5", "2", "3"), fails("5*u - 1", "0", "5")),
             errors={"A": "the falling line written rising [B1G-M, AR.4.3: plotting and graphing errors]", "B": "the two numbers of each equation swapped [B1G-M, AR.3.3: which value is which]", "C": "a first line through the crossing (1, 4) only: x + 3 is 3 at x = 0, not 1 [B1G-M, AR.4.3: plotting and graphing errors]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the systems that have no solution.",
             choices=["$y = 4x + 1$ and $y = 4x - 3$", "$y = 2x + 5$ and $y = -2x + 5$", "$y = -3x + 2$ and $y = -3x - 4$", "$y = 5x$ and $y = x + 5$", "$y = x - 6$ and $y = -6 + x$"], correct=[0, 2], answer="A, C",
             why="A and C: the same number multiplies x in both and the added numbers differ — parallel. B crosses at (0, 5); D crosses at (1.25, 6.25); E is one line written two ways (infinitely many).",
             check=("many", never_meet("4*u + 1", "4*u - 3"), never_meet("-3*u + 2", "-3*u - 4"),
                    meets("2*u + 5", "-2*u + 5"), meets("u - 6", "-6 + u"), meets("5*u", "u + 5")),
             errors={"B": "2 and −2 taken as the same number multiplying x [B1G-M, AR.4.3: plotting and graphing errors]", "D": "the same digit, 5, in both read as parallel [B1G-M, AR.4.3: plotting and graphing errors]", "E": "one line read as no solution [B1G-M, AR.4.2: the same-line case]"}),
    ],

    additional=[
        dict(heading="For questions 1 and 2, the system is graphed. What is its solution?"),
        dict(stem="$y = x + 5$   and   $y = -x + 1$",
             fig=figs.plane((-5, 2), (-1, 6), lines=[(1, 5), (-1, 1)], solution=(-2, 3), inches=2.6),
             answer="(−2, 3)", why="The lines cross at (−2, 3): −2 + 5 = 3 and −(−2) + 1 = 3.",
             check=crosses("u + 5", "-u + 1", "-2", "3"), space=0.4),
        dict(stem="$y = 4x - 3$   and   $y = -x + 7$",
             fig=figs.plane((0, 4), (-3, 7), lines=[(4, -3), (-1, 7)], solution=(2, 5), inches=2.2),
             answer="(2, 5)", why="The lines cross at (2, 5): 4(2) − 3 = 5 and −2 + 7 = 5.",
             check=crosses("4*u - 3", "-u + 7", "2", "5"), space=0.4),
        dict(heading="Use the tables."),
        dict(stem="The tables are for $y = 3x + 2$ and $y = 5x - 2$. What is the solution of the system?",
             fig=figs.table([([0, 1, 2, 3, 4], [2, 5, 8, 11, 14]), ([0, 1, 2, 3, 4], [-2, 3, 8, 13, 18])],
                            titles=["y = 3x + 2", "y = 5x − 2"], inches=5.2),
             answer="(2, 8)", why="At x = 2 both tables give 8: 3(2) + 2 = 8 and 5(2) − 2 = 8.",
             check=("many", crosses("3*u + 2", "5*u - 2", "2", "8"), table_of("3*u + 2", [0, 1, 2, 3, 4], [2, 5, 8, 11, 14]),
                    table_of("5*u - 2", [0, 1, 2, 3, 4], [-2, 3, 8, 13, 18])), space=0.4),
        dict(heading="For questions 4 and 5, the system is graphed. How many solutions does it have?"),
        dict(stem="$y = -3x + 4$   and   $y = -3x - 1$",
             fig=figs.plane((-2, 2), (-8, 8), lines=[(-3, 4), (-3, -1)], ys=2, inches=2.0),
             answer="No solution", why="Parallel: −3 multiplies x in both, so the lines never meet.",
             check=never_meet("-3*u + 4", "-3*u - 1"), space=0.4),
        dict(stem="$y = x + 4$   and   $y = 4 + x$   (both graph as the line shown)",
             fig=figs.plane((-5, 2), (-2, 5), lines=[(1, 4, "")], inches=2.0),
             answer="Infinitely many solutions", why="4 + x is x + 4: one line, and every point of it makes both true.",
             check=one_line("u + 4", "4 + u"), space=0.4),
        dict(heading="For questions 6 and 7, graph both lines on the grid and solve the system."),
        dict(stem="$y = x - 4$   and   $y = -2x + 5$",
             fig=GRID((-1, 5), (-5, 5)), fig_key=KEY((-1, 5), (-5, 5), [(1, -4), (-2, 5)], (3, -1)),
             answer="(3, −1)", why="Tables at x = 0, 1, 2, 3: y = −4, −3, −2, −1 and y = 5, 3, 1, −1. Both give −1 at x = 3: 3 − 4 = −1 and −2(3) + 5 = −1.",
             check=("many", crosses("u - 4", "-2*u + 5", "3", "-1"), table_of("u - 4", [0, 1, 2, 3], [-4, -3, -2, -1]), table_of("-2*u + 5", [0, 1, 2, 3], [5, 3, 1, -1])),
             space=0.9),
        dict(stem="$y = \\frac{1}{2}x - 2$   and   $y = -x + 4$",
             fig=GRID((-1, 6), (-3, 5)), fig_key=KEY((-1, 6), (-3, 5), [(H, -2), (-1, 4)], (4, 0), "u++"),
             answer="(4, 0)", why="Even x: at x = 0, 2, 4, y = −2, −1, 0 and y = 4, 2, 0. Both give 0 at x = 4: ½(4) − 2 = 0 and −4 + 4 = 0.",
             check=("many", crosses("F(1,2)*u - 2", "-u + 4", "4", "0"), table_of("F(1,2)*u - 2", [0, 2, 4], [-2, -1, 0]), table_of("-u + 4", [0, 2, 4], [4, 2, 0])),
             space=0.9),
        dict(heading="Find the missing number."),
        dict(stem="The solution of the system  $y = x - 3$  and  $y = -2x + □$  is $(4, 1)$. What number goes in the box?", answer="9",
             why="Put (4, 1) into the second equation: 1 is −8 plus the box, so the box is 9. Check the first equation: 4 − 3 = 1.",
             check=("many", ("eq", "1 + 8", "9"), crosses("u - 3", "-2*u + 9", "4", "1")), space=0.6),
        dict(heading="Solve the problem."),
        dict(stem="Tank A holds $y = -3x + 12$ gallons after x minutes, and Tank B holds $y = x + 4$ gallons. When do the tanks hold the same amount, and how much is in each?",
             fig=figs.plane((0, 5), (0, 12), lines=[(-3, 12, "A", (1, "ur")), (1, 4, "B")], ys=2, xname="minutes", yname="gallons",
                            solution=(2, 6), inches=2.3),
             answer="After 2 minutes, 6 gallons each.", why="The lines cross at (2, 6): −3(2) + 12 = 6 and 2 + 4 = 6.",
             check=("many", crosses("-3*u + 12", "u + 4", "2", "6")), space=0.5),
        dict(heading="Choose one."),
        dict(stem="The system $y = 2x - 5$ and $y = -x + 4$ is graphed. What is its solution?",
             fig=figs.plane((-1, 5), (-5, 5), lines=[(2, -5), (-1, 4)], solution=(3, 1), inches=2.2),
             choices=["$(0, -5)$", "$(4, 0)$", "$(3, 1)$", "$(1, 3)$"], correct=2, answer="C",
             why="The lines cross at (3, 1): 2(3) − 5 = 1 and −3 + 4 = 1.",
             check=("many", crosses("2*u - 5", "-u + 4", "3", "1"), fails("2*u - 5", "1", "3"), sat("2*u - 5", "0", "-5"), fails("-u + 4", "0", "-5"),
                    sat("-u + 4", "4", "0"), fails("2*u - 5", "4", "0")),
             errors={"A": "where y = 2x − 5 meets the y-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]", "B": "where y = −x + 4 meets the x-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]", "D": "the coordinates of the crossing swapped [B1G-M, GR.1.2: x and y inverted]"}),
        dict(stem="One line passes through $(0, -2)$ and $(1, 2)$; the other passes through $(2, 1)$ and $(3, 0)$. Which system is graphed?",
             fig=figs.plane((-1, 4), (-3, 5), lines=[(4, -2, ""), (-1, 3, "")], solution=(1, 2),
                            points=[(0, -2, None, "r"), (1, 2, None, "r"), (2, 1, None, "ur"), (3, 0, None, "ur")], inches=2.2),
             choices=["$y = 4x - 2$ and $y = -x + 3$", "$y = 4x - 2$ and $y = x + 3$", "$y = x + 1$ and $y = -x + 3$", "$y = -2x + 4$ and $y = 3x - 1$"],
             correct=0, answer="A",
             why="4(0) − 2 = −2 and 4(1) − 2 = 2; −2 + 3 = 1 and −3 + 3 = 0.",
             check=("many", sat("4*u - 2", "0", "-2"), sat("4*u - 2", "1", "2"), sat("-u + 3", "2", "1"), sat("-u + 3", "3", "0"),
                    fails("u + 1", "0", "-2"), fails("-2*u + 4", "0", "-2"), fails("u + 3", "3", "0")),
             errors={"B": "the falling line written rising [B1G-M, AR.4.3: plotting and graphing errors]", "C": "a first line through the crossing (1, 2) only: x + 1 is 1 at x = 0, not −2 [B1G-M, AR.4.3: plotting and graphing errors]", "D": "the two numbers of each equation swapped [B1G-M, AR.3.3: which value is which]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the systems that have no solution.",
             choices=["$y = 3x + 4$ and $y = -3x + 4$", "$y = 2x - 7$ and $y = -7 + 2x$", "$y = \\frac{1}{2}x + 3$ and $y = 0.5x - 1$", "$y = -x + 6$ and $y = -x - 2$", "$y = 6x$ and $y = x + 6$"], correct=[2, 3], answer="C, D",
             why="C and D: the same number multiplies x in both (½ and 0.5 are one number) and the added numbers differ — parallel. A crosses at (0, 4); B is one line written two ways (infinitely many); E crosses at (1.2, 7.2).",
             check=("many", never_meet("-u + 6", "-u - 2"), never_meet("F(1,2)*u + 3", "F(5,10)*u - 1"),
                    meets("3*u + 4", "-3*u + 4"), meets("6*u", "u + 6"), meets("2*u - 7", "-7 + 2*u")),
             errors={"A": "3 and −3 taken as the same number multiplying x [B1G-M, AR.4.3: plotting and graphing errors]", "B": "one line read as no solution [B1G-M, AR.4.2: the same-line case]", "E": "the same digit, 6, in both read as parallel [B1G-M, AR.4.3: plotting and graphing errors]"}),
    ],

    te=dict(
        must="Students solve systems of two linear equations by graphing, in mathematical and real-world contexts. They recognize that parallel lines, which have the same coefficient of x, never meet (MA.8.AR.4.3, Clarification 3).",
        must_not="The words \"slope\" and \"y-intercept\" are not used until Unit 10. Substitution and elimination belong to Algebra 1. Every system is given solved for y, so no system has an equation such as x = 3.5.",
        read_first=[
            "The 43-minute day (Wed 9 Dec; Tuesday 8 Dec is a spiral day with no deck, so the last lesson is Monday's 11.05–06). The kit's timing table must total 53, so the table below is the full lesson; the cut is under Materials in the Lesson Plan. Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §11.07, standing decisions 1, 2, 3, 6 and 9), then read against Math Nation 11.7 (the unit audit, Part 2, E4, E5, E12, E13, §3–§5).",
            "Every line is graphed from a table (x = 0 and two more; the third point is the check). Today's words: the coefficient of x (Monday's 'number multiplying x'), and intersect — the point of intersection is the crossing. You may say slope here, the slides do not. The reasons from the equations that Monday only pictured are taught here (Notes III): the same coefficient of x and different numbers added — parallel, two level lines included; one equation written two ways — one line. The bridge x + 1 = −2x + 7 is printed once, a move a line, and practiced nowhere.",
            "The Examples' question slides show empty tables and an empty grid: fill and draw them on the projected slide while the class watches; the worked slide gives the tables and the check beside the finished graph. Each Your Turn shows its two tables filled beside an empty grid, and its answer slide the graph with the crossing marked; both cross inside their tables. Right after Example 1's Your Turn, hand out the Independent Set: every student draws question 1 on its grid while you circulate (three of that Your Turn's five minutes) — the first lines are drawn where you can see them. The boards read a graph or two tables; nobody draws two lines on a whiteboard. The key draws both lines on each student grid, from their equations, with the crossing marked and named.",
            "Changed from the outline: board 5 is y = 2x + 2 and y = 2x − 3 (the outline's y = 2x + 1 and y = 2x − 3 is 11.05's Notes III system). Not reproduced: the off-grid key graphs (E4, E5), end labels past the grid (E13), x = 3.5 (audit decision 2), the partner tasks."],
        materials="Whiteboards, markers and rulers. Hand out the Independent Set, one per student, at Example 1's Your Turn. Students draw question 1 of the set then, in class, while the teacher circulates. On a 43-minute day, shorten the warm-up to 4 minutes: two minutes of silent work, then the answers. Skip whiteboard question 7 (the two candles) and question 8 (the missing number). Take question 9 aloud and read two students' boards to the class. Question 6 of the Independent Set is done in class, questions 2–5 go home, and IXL starts outside class. Together these cuts save about 13 minutes. Keep the vocabulary slide. Do not cut whiteboard questions 4 and 6 (the two votes), question 2 (the two tables), question 5 (parallel lines) or question 9.",
        variation="Boards 1–4 read a crossing — a graph, two tables, a crossing on an axis, then a vote on the four points a graph offers. The pattern breaks at 5 — parallel, under a stem that says 'solve' (the trap is deliberate: 'no solution' is a solution of the question) — and 6 votes on the system through four marked points; 7 is the candle story with its price as the extra number; 8 runs backwards; 9 is written. The independent set: question 1 drawn in class after Example 1, then two more systems to graph (negative x's, named in the stem; a ½), a parallel pair and one line twice to graph, then two tables.",
        audit=["Every crossing re-derived by sympy at build time as the system's one solution, and checked in both equations; every printed table checked value by value; every parallel pair checked to have no common point and every same-line pair to be one expression; every graph drawn from its equations by u11/figs.py, which refuses a stated crossing that is not on both lines.",
               "Math Nation 11.7 read against this lesson (A7 Unit 11 Audit, Part 2, E4, E5, E12, E13, §3–§5): its sound shapes — read and verify, graph and read, a parallel pair — are here with our own numbers; its defects are not reproduced."],
        changes=["11.7.1 Which One Doesn't Belong → four retrieval questions, the table of Notes I last.",
                 "11.7.2 read-and-verify and graph-and-read → Notes II, Example 1 and boards 1–4, with new numbers and a table route.",
                 "11.7.3 approximating (x = 3.5) → not used (audit decision 2); estimates are 11.08.",
                 "11.7.4–11.7.5 parallel lines by slope → Notes III, board 5 and the written board 9, said as the same number multiplying x.",
                 "Practice and Homework L7 → the Independent Set: empty grids whose window is the key's."],
    ),
)
