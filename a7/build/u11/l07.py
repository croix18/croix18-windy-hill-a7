# A7 11.07  Solving Systems by Graphing — MA.8.AR.4.3 (MN 11.7). Wed 9 Dec 2026, a 43-minute Wednesday: the deck is
# written to the kit's standard plan, as 11.03's was (HOUSE STYLE §9 — no Wednesday plan; the cut is the teacher's,
# and the title slide's note says so). Tuesday 8 Dec has no class, so the last lesson is Monday's 11.05–06.
# The class has never graphed y = mx + b and has no word for slope (Unit 11 comes before Units 10 and 7, ruling 52):
# a line is graphed FROM A TABLE OF VALUES — x = 0 and two more, the third point the check (standing decision 1).
# Parallel lines are "the same steepness: the same number multiplying x" (decision 2); "slope" and "y-intercept"
# are on no student surface. No substitution and no elimination (decision 3): the one algebra bridge — where the
# lines cross, both give the same y, so x + 1 = −2x + 7 and x = 2 — is shown in Notes III and not practised.
# Every crossing is checked in both equations (decision 6). The boards READ a graph or two tables; the
# Independent Set is where a student draws: its graphing questions print an empty grid (decision 9).
# Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §11.07), then read against Math Nation
# 11.7 (the unit audit, Part 2). Not reproduced: the answer graphs that are not the lines of their equations (E4,
# E5 — every line here is drawn from its own m and b by u11/figs.py, and every crossing named in the words is given
# to `plane` as `solution=`, which refuses one that is not on both lines), the end labels past the last grid line
# (E13 — a figs.plane grid ends on its last numbered line, and a key's grid is the student's grid), the half-unit
# key read stated as exact (E12 — every crossing today is a lattice point), the x = 3.5 item (audit decision 2:
# a vertical line is outside AR.4.3's slope-intercept boundary), the partner work, and the slope vocabulary.
#
# Every check is sympy over the REAL numbers: a crossing is the system's one solution (crosses), parallel lines
# have no common point (never_meet), two ways of writing one line are one expression (one_line), and a pair is put
# into each equation (sat / fails). A failed check is written as a true computation with its verdict, never as a
# false equation.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs
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

# ---- the board figures: the largest the question and reveal slides allow (11.07, 14 Nov). One bold row of words
# over the figure, a square window no bigger than the system needs, and slide(inches=4.2, pt=18, reserve=0.75):
# the slide's height is what binds (FOOT_Y − the row's foot − the ask's room), so a board's plane comes out about
# 3.3 in tall on the question slide and 3.2 in on the reveal, its labels at 18 pt. 11.05's were 2.6 in at 16 pt.
# A multiple-choice board gives 1.75 in more to its four options, so a graph there would be at most about 1.5 in
# tall on the question slide — too small to read from the back of the room (Croix, 14 Nov). So no question slide of
# a multiple-choice board carries a graph: board 2's vote is on two tables (wide, not tall), board 6 gives its four
# points in words and shows the graph only on its reveal, and board 4 — read a crossing — is free response at full
# size.


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
NOTES3 = S(figs.row([figs.plane((-2, 3), (-5, 6), lines=[(2, 3, ""), (2, -2, "")], step=2),
                     figs.plane((-1, 3), (-5, 6), lines=[(3, -1, "")], step=2)],
                    gap=4.0,
                    titles=[[("y = 2x + 3", BLUE), ("y = 2x − 2", ORANGE)],
                            [("y = 3x − 1", BLUE), ("y = −1 + 3x", BLUE)]],
                    captions=["no solution", "infinitely many"]),
           inches=6.4, pt=16, reserve=1.35)
EX1 = S(figs.row([figs.table([([0, 1, 2], [-3, -1, 1]), ([0, 1, 2], [6, 5, 4])], titles=["y = 2x − 3", "y = −x + 6"]),
                  figs.plane((0, 5), (-3, 6), lines=[(2, -3), (-1, 6)], solution=(3, 3),
                             points=[(3, 3)])],
                 gap=1.8), inches=7.2, pt=16, reserve=0.9)
EX2 = S(figs.row([figs.table([([0, 2, 4], [1, 2, 3]), ([0, 2, 4], [4, 2, 0])], titles=["y = ½x + 1", "y = −x + 4"]),
                  figs.plane((-1, 5), (-1, 5), lines=[(H, 1), (-1, 4)], solution=(2, 2),
                             points=[(2, 2, "")])],
                 gap=1.8), inches=9.6, pt=16, reserve=0.9)

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


# ---- the Independent Set: an empty grid for each system a student graphs (decision 9). A grid is the window its
# key's graph is drawn on — the same lines, the same numbers (audit E13).
def GRID(xr, yr):
    return figs.plane(xr, yr, inches=3.2)


L = dict(
    code="11.07", unit=11, lesson_no=7,
    title="Solving Systems by Graphing",
    unit_title="Solving Equations and Systems",
    benchmark="MA.8.AR.4.3",
    benchmark_text="Given a mathematical or real-world context, solve systems of two linear equations by graphing.",
    target="I can solve a system of two equations by graphing both lines and reading where they cross.",
    yesterday="Last class: which pairs solve a system, and how many solutions a graph shows.",
    today="Today: we draw both lines ourselves and read where they cross.",
    essential="Why is the point where two lines cross the one pair that makes both equations true?",
    building_on="11.05–06 — a solution of a system makes both equations true; one, none or infinitely many from a graph; 11.02 — solving mx + b = nx + c; Grade 7 (MA.7.AR.4.3) — graphing from a table.",
    working_toward="11.08 — systems in context and estimates between the grid lines; Unit 10 (January) — the number multiplying x gets its name; Algebra 1 (MA.912.AR.9.1) — substitution and elimination.",
    vocab=[("table of values", "x-values you choose and the y each one gives: $x = 0$ first, then two more"),
           ("solve by graphing", "graph both equations on one grid; the point where the lines cross is the solution")],
    vocab_note="Two phrases, read once each. The table is the tool all period: x = 0 first, then two more, and the third point is the check. 'Solve by graphing' ends with a check in both equations, every time.",
    ixl=["Solve a system of equations by graphing — C8X", "Write a system of equations given a graph — TS7"],
    title_note="A 43-minute Wednesday on the standard plan, as 11.03 was: the cut is yours — boards 7 and 8 first, then the vocabulary slide.",
    closure="Board 9 is written work and it is the exit evidence: Tia's lines are parallel — 3 multiplies x in both, so for every x the second is 3 above the first — and they never meet, on the grid or off it: no solution. A board that says only 'no' has the verdict and not the reason.",

    mtr=[("MTR.2.1", "a table, a graph and an equation for one crossing"),
         ("MTR.4.1", "boards 2 and 6: re-vote"),
         ("MTR.6.1", "every crossing checked in both equations")],
    hoq=[("Why does a third point in each table matter before you draw the line?", "DOK 2"),
         ("Two lines with different numbers multiplying x: why must they cross somewhere, even off the grid?", "DOK 3"),
         ("Board 2 needs no graph. Where in two tables do you see the solution?", "DOK 2")],
    differentiation=[
        ("ESE / 504", "A printed blank table (x = 0, 1, 2 already written) beside each grid, and a pencil for each line before ink. Notes II stays up from board 1 on."),
        ("ELL", "**Table**: the x's you pick and the y's they give. **Cross**: meet at one point. **Check**: put the point into both equations. **Parallel**: like train tracks — never meet."),
        ("Enrichment", "Board 6 finishes early for some: write a second equation that makes a system with y = 2x − 1 whose solution is (3, 5), and one that makes a system with no solution. (Any line through (3, 5) with another number multiplying x, such as y = −x + 8; any y = 2x + b with b ≠ −1.)")],

    warmup=[
        dict(stem="Is $(1, 5)$ a solution of  $y = 2x + 3$  and  $y = x + 4$?", answer="Yes", band="last lesson",
             source="11.05–06 — a pair tested in both equations: 2(1) + 3 = 5 and 1 + 4 = 5",
             check=("many", sat("2*u + 3", "1", "5"), sat("u + 4", "1", "5"))),
        dict(stem="Solve:  $0.5(6x + 4) = x + 8$", answer="x = 3", band="last week",
             source="11.04 — a decimal distributed: 3x + 2 = x + 8",
             check=("eq", "sp.solve(sp.Eq(F(1,2)*(6*" + X + " + 4), " + X + " + 8), " + X + ")[0]", "3")),
        dict(stem="A right triangle has legs 9 and 12. Find the hypotenuse.", answer="15", band="last unit",
             source="6.03 — the Pythagorean Theorem: 81 + 144 = 225",
             check=("eq", "sqrt(9**2 + 12**2)", "15")),
        dict(stem="$y = 2x - 1$.  Find y when $x = 0$, $1$ and $2$.", answer="−1, 1, 3", band="the prerequisite this lesson needs",
             source="7th grade — evaluate an expression; it is the table of Notes I",
             check=("many", ("eq", "2*0 - 1", "-1"), ("eq", "2*1 - 1", "1"), ("eq", "2*2 - 1", "3"))),
    ],
    warmup_note="Q4 is Notes I's table: three x's, three y's, three points. Say that after the reveal. Two minutes silent, then reveal, no discussion — 43 minutes today.",

    notes=[
        dict(numeral="I", head="A line from a table", min=4, sub="Copy the table and the line.",
             note="The class has never drawn y = mx + b, so the line comes from a table. x = 0 first, then two more; put each x in and get its y. Plot the three points. Two points draw a line; the third is the check — three points in a row, or a y is wrong. Then draw the line through them and PAST them, to the edge of the grid: the crossing may be beyond the points you plotted.\nOFF: 'Pick three x's. Find each y. Three points in a row, then a ruler through them, edge to edge.'",
             fig=NOTES1,
             items2=["Three points in a row: the third is the check.   Draw the line past them."],
             letters=False),
        dict(numeral="II", head="Solve by graphing", min=4, sub="",
             note="A table for each equation, both lines on one grid. They cross at (2, 3), and that is the solution — the one point on both lines. Then the check, every time: 2 + 1 = 3 and −2(2) + 7 = 3. Point out that the tables already agree at x = 2 (both give 3): the crossing shows in the tables too.\nOFF: 'Graph both. Read the crossing. Check it in both equations.'",
             fig=NOTES2,
             items2=["$(2, 3)$:   $2 + 1 = 3$   and   $-2(2) + 7 = 3$.   The solution."],
             letters=False),
        dict(numeral="III", head="Not one crossing; and the check without a graph", min=3, sub="",
             note="Left: 2 multiplies x in both, so the lines climb at the same steepness and stay 5 apart — parallel, no solution. Right: y = 3x − 1 and y = −1 + 3x make the same table (−1, 2, 5), so their graphs are one line: infinitely many solutions. Then the bridge, said and not practised: where the lines of Notes II cross, both give the same y, so x + 1 = −2x + 7 — 11.02's equation — and x = 2. It is how a graphed answer is checked; nobody is asked to do it today.\nOFF: 'Same number multiplying x, different numbers added: parallel. Same table: one line.'",
             fig=NOTES3,
             items2=["Where Notes II's lines cross:   $x + 1 = -2x + 7$,   so   $3x = 6$   and   $x = 2$."],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", sub="Tables, graph, crossing, check.", min_q=1,
             note_q="This is the model: read the tables row by row (x = 0 first), point to each plotted point, then ask the room where the lines cross before anyone says it.",
             prompt=["$y = 2x - 3$   and   $y = -x + 6$"], fig=EX1, ask="Solve the system by graphing.",
             worked=[dict(sub="Worked.", min=2,
                          note="The tables: 2x − 3 gives −3, −1, 1 and −x + 6 gives 6, 5, 4 at x = 0, 1, 2. The lines cross beyond the tables, at (3, 3) — which is why each line is drawn past its points. Check in both: 2(3) − 3 = 3 and −3 + 6 = 3. A board with (3, 0) or (0, 3) read a line where it meets an axis.",
                          rows=[("y = 2x - 3:\\quad -3,\\ -1,\\ 1", "at x = 0, 1, 2"),
                                ("y = -x + 6:\\quad 6,\\ 5,\\ 4", "at x = 0, 1, 2"),
                                ("(3, 3):\\quad 2(3) - 3 = 3 \\quad\\text{and}\\quad -3 + 6 = 3", "the crossing, checked in both")],
                          answer="(3, 3)")],
             check=("many", crosses("2*u - 3", "-u + 6", "3", "3"), table_of("2*u - 3", [0, 1, 2], [-3, -1, 1]),
                    table_of("-u + 6", [0, 1, 2], [6, 5, 4])),
             your_turn=dict(min=2, note="Tables at x = 0, 1, 2: x − 2 gives −2, −1, 0 and −3x + 6 gives 6, 3, 0. Both give 0 at x = 2: the lines cross at (2, 0), on the x-axis. A board with (0, 2) swapped the coordinates; with 'no solution', saw a crossing on an axis and did not count it.",
                            prompt=["$y = x - 2$   and   $y = -3x + 6$"],
                            ask="Solve the system by graphing.",
                            steps=["at $x = 2$:   $2 - 2 = 0$   and   $-3(2) + 6 = 0$",
                                   "the lines cross at $(2, 0)$"],
                            gloss="both tables give 0 at x = 2", answer="(2, 0)"),
             yt_check=("many", crosses("u - 2", "-3*u + 6", "2", "0"), sat("u - 2", "2", "0"), sat("-3*u + 6", "2", "0"))),
        dict(title="Example 2", sub="A ½ multiplying x: choose even x.", min_q=1,
             note_q="Ask what x's make ½x easy before anyone fills a table: the even ones, so x = 0, 2, 4.",
             prompt=["$y = \\frac{1}{2}x + 1$   and   $y = -x + 4$"], fig=EX2, ask="Solve the system by graphing.",
             worked=[dict(sub="Worked.", min=2,
                          note="Even x for the ½: at x = 0, 2, 4, ½x + 1 gives 1, 2, 3 and −x + 4 gives 4, 2, 0. Both tables give 2 at x = 2, so the lines cross at (2, 2). Check: ½(2) + 1 = 2 and −2 + 4 = 2. An odd x works too (x = 1 gives 1.5) — it is only harder to plot.",
                          rows=[("y = \\frac{1}{2}x + 1:\\quad 1,\\ 2,\\ 3", "at x = 0, 2, 4"),
                                ("y = -x + 4:\\quad 4,\\ 2,\\ 0", "at x = 0, 2, 4"),
                                ("(2, 2):\\quad \\frac{1}{2}(2) + 1 = 2 \\quad\\text{and}\\quad -2 + 4 = 2", "the crossing, checked in both")],
                          answer="(2, 2)")],
             check=("many", crosses("F(1,2)*u + 1", "-u + 4", "2", "2"), table_of("F(1,2)*u + 1", [0, 2, 4], [1, 2, 3]),
                    table_of("-u + 4", [0, 2, 4], [4, 2, 0])),
             your_turn=dict(min=2, note="Even x, and this crossing is to the left: at x = −4, ½(−4) + 3 = 1 and −(−4) − 3 = 1, so (−4, 1). A table at x = 0, 2, 4 alone (3, 4, 5 and −3, −5, −7) never meets; the lines have to be drawn left. A board with (1, −4) swapped the coordinates.",
                            prompt=["$y = \\frac{1}{2}x + 3$   and   $y = -x - 3$"],
                            ask="Solve the system by graphing.",
                            steps=["at $x = -4$:   $\\frac{1}{2}(-4) + 3 = 1$   and   $-(-4) - 3 = 1$",
                                   "the lines cross at $(-4, 1)$"],
                            gloss="even x, to the left", answer="(−4, 1)"),
             yt_check=("many", crosses("F(1,2)*u + 3", "-u - 3", "-4", "1"), sat("F(1,2)*u + 3", "-4", "1"), sat("-u - 3", "-4", "1"))),
    ],

    # The round: a crossing read off a graph (1) and off two tables, the first diagnostic (2); a crossing with a
    # negative x on an axis (3); a graph that offers four points, read at full size (4); the pattern breaks at 5 —
    # parallel, none; 6 votes on the system through four points given in words (TS7); the candle story read at its crossing, with the price as the extra number (7);
    # backwards (8); and the "they must cross off the grid" claim refuted in writing (9). Every graph is read; none
    # is drawn on a whiteboard (decision 9).
    whiteboard=[
        # repeat_ok: rule D matches only the grid's axis numbers (−1 to 6, shared by the planes today) and the
        # answer's digits; this system (y = x + 2, y = −x + 6) appears nowhere above.
        dict(repeat_ok=True, text=["**The system is graphed. What is its solution?"],
             fig=B(P1), fig_a=BA(P1A),
             hint="Where do they cross?", steps=["the lines cross at $(2, 4)$", "$2 + 2 = 4$   and   $-2 + 6 = 4$"],
             gloss="read the crossing, then check it", answer="(2, 4)",
             note="Read the crossing on the grid lines: x = 2, y = 4. Check it in both: 2 + 2 = 4 and −2 + 6 = 4. A board with (4, 2) swapped the coordinates; one with (0, 6) or (0, 2) read where a line meets the y-axis.",
             check=("many", crosses("u + 2", "-u + 6", "2", "4"), sat("u + 2", "2", "4"), sat("-u + 6", "2", "4")),
             wrong="(4, 2) — x and y swapped [B1G-M, GR.1.2: x and y inverted]; (0, 6) — where one line meets the y-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]"),
        # repeat_ok: rule D matches only the table's x row (0 to 4) and the answer's digits; this system appears
        # nowhere above.
        dict(repeat_ok=True, kind="mc", text=["**The tables are for one system. What is its solution?"],
             qtext="The two tables are for one system: y = 3x − 5 and y = x + 1. What is the solution of the system?",
             fig=S(T2, inches=8.0, pt=18, reserve=0.75), fig_a=S(T2, inches=5.2, pt=14, reserve=0.95),
             hint="Same x, same y.", steps=["at $x = 3$:   $3(3) - 5 = 4$   and   $3 + 1 = 4$"],
             choices=["(4, 3)", "(2, 1)", "(3, 4)", "(4, 4)"], correct=2, answer="C — (3, 4)",
             errors={"A": "the coordinates of (3, 4) swapped [B1G-M, GR.1.2: x and y inverted]", "B": "the column where the tables are closest but not equal, read from y = 3x − 5 only: x + 1 gives 3 there [B1G-M, AR.4.1: a solution satisfies both]", "D": "the shared y, 4, written for x too [B1G-M, GR.1.2: x and y inverted]"},
             note="Diagnostic. No graph needed: the solution is the column where both tables give the same y. At x = 3 both give 4, so C, (3, 4). Option A swaps it; option D writes the shared y for x as well; option B is the column x = 2, where the two y's (1 and 3) are closest before they meet — near is not equal. On a split: sixty seconds, convince your neighbor, re-vote — then check (3, 4) in both aloud.",
             check=("many", crosses("3*u - 5", "u + 1", "3", "4"), table_of("3*u - 5", [0, 1, 2, 3, 4], [-5, -2, 1, 4, 7]),
                    table_of("u + 1", [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]),
                    fails("3*u - 5", "4", "3"), fails("u + 1", "4", "3"),
                    sat("3*u - 5", "2", "1"), fails("u + 1", "2", "1"),
                    fails("3*u - 5", "4", "4"), fails("u + 1", "4", "4"))),
        # repeat_ok: rule D matches only the grid's axis numbers and the answer's digits; the system is new.
        dict(repeat_ok=True, text=["**The system is graphed. What is its solution?"],
             fig=B(P3), fig_a=BA(P3A),
             hint="Where do they cross?", steps=["the lines cross at $(-2, 0)$", "$2(-2) + 4 = 0$   and   $-(-2) - 2 = 0$"],
             gloss="a crossing on the x-axis", answer="(−2, 0)",
             note="The crossing sits on the x-axis, at x = −2: (−2, 0). Check: 2(−2) + 4 = 0 and 2 − 2 = 0. A board with (0, −2) swapped the coordinates — (0, −2) is where the second line meets the y-axis, so it is a doubly tempting slip.",
             check=("many", crosses("2*u + 4", "-u - 2", "-2", "0"), sat("2*u + 4", "-2", "0"), sat("-u - 2", "-2", "0")),
             wrong="(0, −2) — x and y swapped, and where one line meets the y-axis [B1G-M, GR.1.2: x and y inverted]; (0, 4) — where one line meets the y-axis [B1G-M, AR.4.1: a solution satisfies both]"),
        # repeat_ok: rule D matches only the grid's axis numbers and the options' digits; the system is new.
        dict(repeat_ok=True, text=["**$y = -2x + 5$  and  $y = x - 1$  are graphed. What is the solution?"],
             fig=B(P4), fig_a=BA(P4A),
             hint="Cross, then check.", steps=["the lines cross at $(2, 1)$", "$-2(2) + 5 = 1$   and   $2 - 1 = 1$"],
             gloss="read the crossing, then check it", answer="(2, 1)",
             wrong="(1, 2) — the coordinates of the crossing swapped [B1G-M, GR.1.2: x and y inverted]; (1, 0) — where y = x − 1 meets the x-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]; (0, 5) — where y = −2x + 5 meets the y-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]",
             note="The four points a graph offers: the crossing (2, 1), the crossing swapped, and two places where a line meets an axis. Read the crossing on the grid lines, then check it in both: −2(2) + 5 = 1 and 2 − 1 = 1. A board with (1, 2) swapped it; one with (1, 0) or (0, 5) read a point that lies on one line only.",
             check=("many", crosses("-2*u + 5", "u - 1", "2", "1"), sat("-2*u + 5", "2", "1"), sat("u - 1", "2", "1"),
                    fails("-2*u + 5", "1", "2"), fails("u - 1", "1", "2"),
                    sat("-2*u + 5", "0", "5"), fails("u - 1", "0", "5"),
                    sat("u - 1", "1", "0"), fails("-2*u + 5", "1", "0"))),
        # repeat_ok: rule D matches only the grid's axis numbers; the system is new (11.05 used y = 2x + 1 and
        # y = 2x − 3; one number is changed from the outline for that reason).
        dict(repeat_ok=True, text=["**The system is graphed. What is its solution?"],
             fig=B(P5), fig_a=BA(P5),
             hint="Will they ever meet?", steps=["$2x + 2$ and $2x - 3$:  2 multiplies x in both", "parallel:  they never meet"],
             gloss="the same steepness", answer="No solution — the lines are parallel.",
             note="The pattern breaks: no crossing to read. The same number, 2, multiplies x in both, so the lines climb at the same steepness and the first is always 5 above the second. A board with a point read a spot where the lines look close; one with 'infinitely many' saw two lines that go on forever.",
             check=never_meet("2*u + 2", "2*u - 3"),
             wrong="a point such as (0, 2) — a point of one line read as the answer [B1G-M, AR.4.3: plotting and graphing errors]; infinitely many — 'the lines go on forever' [B1G-M, AR.4.2: the same-line case]"),
        # repeat_ok: rule D matches the grid's axis numbers and the four marked points; the system is new.
        dict(repeat_ok=True, kind="mc", text=["Line 1 passes through $(0, 1)$ and $(1, 3)$.", "Line 2 passes through $(0, 4)$ and $(2, 2)$.",
                                              "**Which system has these two lines?"],
             qtext="Line 1 passes through (0, 1) and (1, 3). Line 2 passes through (0, 4) and (2, 2). Which system has these two lines?",
             fig_a=S(P6, inches=4.2, pt=18, reserve=0.85),
             hint="Test the marked points.", steps=["first line:   $2(0) + 1 = 1$   and   $2(1) + 1 = 3$",
                                                  "second line:   $-(0) + 4 = 4$   and   $-2 + 4 = 2$"],
             choices=["y = 2x + 1 and y = −x + 4", "y = x + 2 and y = 4x − 1", "y = x + 2 and y = −x + 4", "y = 2x + 1 and y = x + 4"],
             correct=0, answer="A — y = 2x + 1 and y = −x + 4",
             errors={"B": "the two numbers of each equation swapped [B1G-M, AR.3.3: which value is which]", "C": "a first line tested at (1, 3) only: x + 2 is 2 at x = 0, not 1 [B1G-M, AR.4.3: plotting and graphing errors]", "D": "the falling line written rising: x + 4 grows as x grows [B1G-M, AR.4.3: plotting and graphing errors]"},
             note="Diagnostic, and today's second IXL skill (write a system from a graph): the four points are given in words, and the reveal shows the two lines through them. Each equation must pass through both points of its line. Option C fits (1, 3), where the lines cross, and not (0, 1); option D makes the falling line rise; option B swaps the multiplier and the added number in both. The TE may say slope and y-intercept for B; the room says 'the number multiplying x'.",
             check=("many", sat("2*u + 1", "0", "1"), sat("2*u + 1", "1", "3"), sat("-u + 4", "0", "4"), sat("-u + 4", "2", "2"),
                    crosses("2*u + 1", "-u + 4", "1", "3"),
                    sat("u + 2", "1", "3"), fails("u + 2", "0", "1"),
                    fails("u + 4", "2", "2"), fails("u + 4", "1", "3"),
                    fails("4*u - 1", "2", "2"))),
        dict(text=["Candle A cost \\$3. The graph shows both candles' heights.",
                   "**When are the two candles the same height?"],
             unneeded="3",
             fig=S(P7, inches=5.0, pt=16, reserve=0.75), fig_a=S(P7A, inches=5.0, pt=16, reserve=1.1),
             hint="x is hours; y is height.", steps=["A:   $-2(4) + 12 = 4$", "B:   $-4 + 8 = 4$"],
             gloss="x = 4 hours, y = 4 cm", answer="After 4 hours, both are 4 cm tall.",
             note="The extra-number board (ruling 22): the \\$3 is not needed. The crossing is (4, 4): x = 4 hours and y = 4 cm, so after 4 hours both candles are 4 cm tall. Check: −2(4) + 12 = 4 and −4 + 8 = 4. A board with 'after 3 hours' used the price.",
             check=("many", crosses("-2*u + 12", "-u + 8", "4", "4"), sat("-2*u + 12", "4", "4"), sat("-u + 8", "4", "4")),
             wrong="'after 3 hours' — the price used [ruling 22]; 'at 8 cm' — where candle B starts, on one line only [B1G-M, AR.4.1: a solution satisfies both]"),
        dict(text=["$(2, 5)$ is the solution of  $y = 2x + 1$  and  $y = -x + □$.", "**What number goes in the box?"],
             hint="Put the point in the second equation.", steps=["$2(2) + 1 = 5$", "$-2 + 7 = 5$"],
             gloss="the box makes the second equation give 5", answer="7",
             note="Backwards: the point is given and a number of the second equation is missing. Put x = 2 and y = 5 into it: 5 = −2 + □, so the box is 7. Check the first too: 2(2) + 1 = 5. A board with 3 took 5 − 2 instead of 5 + 2.",
             check=("many", ("eq", "5 + 2", "7"), crosses("2*u + 1", "-u + 7", "2", "5")),
             wrong="3 — 5 − 2, the −x taken the wrong way [B1G-M, AR.4.1: substitution errors]; 5 — the y copied into the box [B1G-M, AR.4.1: substitution errors]"),
        dict(kind="written", text=["Tia graphed  $y = 3x - 2$  and  $y = 3x + 1$.  She says the lines must",
                                   "cross somewhere off her grid.", "**Is Tia right? Explain."],
             qtext="Tia graphed y = 3x − 2 and y = 3x + 1. She says the lines must cross somewhere off her grid. Is Tia right? Explain.",
             hint="Look at the number multiplying x.", steps=["3 multiplies x in both:  each line climbs 3 for every 1 across",
                                                             "at $x = 0$:   $-2$ and $1$;   at $x = 10$:   $28$ and $31$",
                                                             "always 3 apart:  parallel, no solution"],
             gloss="the same steepness", answer="No: the lines are parallel — no solution.",
             te_answer="Full credit: 'no' AND the reason — 3 multiplies x in both, so the lines climb at the same steepness and stay 3 apart everywhere, on the grid and off it; they never meet, and the system has no solution. 'No' with no reason earns none.",
             note="Written, and the exit evidence: the claim that two lines must meet somewhere. Read two aloud. The TE may say 'the same slope'; the room says 'the same number multiplying x'.",
             check=("many", never_meet("3*u - 2", "3*u + 1"), one_line("(3*u + 1) - (3*u - 2)", "3"),
                    ("eq", "3*10 - 2", "28"), ("eq", "3*10 + 1", "31")),
             wrong="'yes, they meet off the grid' — two lines taken to always meet [B1G-M, AR.4.3: plotting and graphing errors]"),
    ],

    # The six: graph and solve with a whole crossing (1), with negative coordinates (2), with a ½ multiplying x (3);
    # the pattern breaks — parallel, no solution (4) and one line twice, infinitely many (5); and two tables read to
    # the solution (6). Each of 1–5 prints an empty grid and room for two tables beside it (decision 9).
    independent=[
        dict(stem="Solve by graphing:   $y = x + 3$   and   $y = -2x + 6$",
             fig=GRID((-2, 5), (-1, 7)),
             answer="(1, 4)", why="Tables at x = 0, 1, 2: y = 3, 4, 5 and y = 6, 4, 2. The lines cross at (1, 4): 1 + 3 = 4 and −2(1) + 6 = 4.",
             check=("many", crosses("u + 3", "-2*u + 6", "1", "4"), table_of("u + 3", [0, 1, 2], [3, 4, 5]), table_of("-2*u + 6", [0, 1, 2], [6, 4, 2])),
             space=0.3),
        dict(stem="Solve by graphing:   $y = x - 1$   and   $y = -2x - 4$",
             fig=GRID((-4, 3), (-5, 4)),
             answer="(−1, −2)", why="Tables at x = −2, −1, 0: y = −3, −2, −1 and y = 0, −2, −4. The lines cross at (−1, −2): −1 − 1 = −2 and −2(−1) − 4 = −2.",
             check=("many", crosses("u - 1", "-2*u - 4", "-1", "-2"), table_of("u - 1", [-2, -1, 0], [-3, -2, -1]), table_of("-2*u - 4", [-2, -1, 0], [0, -2, -4])),
             space=0.3),
        dict(stem="Solve by graphing:   $y = \\frac{1}{2}x - 1$   and   $y = -x + 5$",
             fig=GRID((-1, 6), (-2, 6)),
             answer="(4, 1)", why="Even x for the ½: at x = 0, 2, 4, y = −1, 0, 1 and y = 5, 3, 1. The lines cross at (4, 1): ½(4) − 1 = 1 and −4 + 5 = 1.",
             check=("many", crosses("F(1,2)*u - 1", "-u + 5", "4", "1"), table_of("F(1,2)*u - 1", [0, 2, 4], [-1, 0, 1]), table_of("-u + 5", [0, 2, 4], [5, 3, 1])),
             space=0.3),
        dict(stem="Solve by graphing:   $y = -x + 4$   and   $y = -x - 1$",
             fig=GRID((-3, 5), (-4, 6)),
             answer="No solution", why="−1 multiplies x in both: the lines are parallel, always 5 apart, and never meet.",
             check=never_meet("-u + 4", "-u - 1"), space=0.3),
        dict(stem="Solve by graphing:   $y = 2x - 5$   and   $y = -5 + 2x$",
             fig=GRID((0, 5), (-5, 5)),
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
             answer="None", why="Parallel: −2 multiplies x in both, so the lines never meet.",
             check=never_meet("-2*u + 3", "-2*u - 1"), space=0.4),
        dict(stem="$y = -x + 3$   and   $y = 3 - x$   (both graph as the line shown)",
             fig=figs.plane((-2, 5), (-2, 5), lines=[(-1, 3, "")], inches=2.0),
             answer="Infinitely many", why="3 − x is −x + 3: one line, and every point of it makes both true.",
             check=one_line("-u + 3", "3 - u"), space=0.4),
        dict(heading="For questions 6 and 7, graph both lines on the grid and solve the system."),
        dict(stem="$y = x - 3$   and   $y = -2x + 3$",
             fig=GRID((-2, 5), (-4, 4)),
             answer="(2, −1)", why="Tables at x = 0, 1, 2: y = −3, −2, −1 and y = 3, 1, −1. Both give −1 at x = 2: 2 − 3 = −1 and −2(2) + 3 = −1.",
             check=("many", crosses("u - 3", "-2*u + 3", "2", "-1"), table_of("u - 3", [0, 1, 2], [-3, -2, -1]), table_of("-2*u + 3", [0, 1, 2], [3, 1, -1])),
             space=0.9),
        dict(stem="$y = \\frac{1}{2}x + 2$   and   $y = -x + 5$",
             fig=GRID((-1, 6), (-1, 6)),
             answer="(2, 3)", why="Even x: at x = 0, 2, 4, y = 2, 3, 4 and y = 5, 3, 1. Both give 3 at x = 2: ½(2) + 2 = 3 and −2 + 5 = 3.",
             check=("many", crosses("F(1,2)*u + 2", "-u + 5", "2", "3"), table_of("F(1,2)*u + 2", [0, 2, 4], [2, 3, 4]), table_of("-u + 5", [0, 2, 4], [5, 3, 1])),
             space=0.9),
        dict(heading="Work backwards."),
        dict(stem="$(3, 2)$ is the solution of  $y = x - 1$  and  $y = -2x + □$. What number goes in the box?", answer="8",
             why="2 = −2(3) + □ = −6 + □, so □ = 8. Check the first: 3 − 1 = 2.",
             check=("many", ("eq", "2 + 6", "8"), crosses("u - 1", "-2*u + 8", "3", "2")), space=0.6),
        dict(heading="Solve the problem."),
        dict(stem="Tank A holds $y = -2x + 10$ gallons after x minutes, and Tank B holds $y = x + 1$ gallons. When do the tanks hold the same amount, and how much is in each?",
             fig=figs.plane((0, 6), (0, 10), lines=[(-2, 10, "A", (1, "ur")), (1, 1, "B")], ys=2, xname="minutes", yname="gallons",
                            solution=(3, 4), inches=2.6),
             answer="After 3 minutes, 4 gallons each.", why="The lines cross at (3, 4): −2(3) + 10 = 4 and 3 + 1 = 4.",
             check=("many", crosses("-2*u + 10", "u + 1", "3", "4")), space=0.5),
        dict(heading="Choose one."),
        dict(stem="$y = 3x - 3$ and $y = -x + 5$ are graphed. What is the solution of the system?",
             fig=figs.plane((-1, 4), (-4, 6), lines=[(3, -3), (-1, 5)], solution=(2, 3), inches=2.2),
             choices=["$(3, 2)$", "$(2, 3)$", "$(0, 5)$", "$(1, 0)$"], correct=1, answer="B",
             why="The lines cross at (2, 3): 3(2) − 3 = 3 and −2 + 5 = 3.",
             check=("many", crosses("3*u - 3", "-u + 5", "2", "3"), fails("3*u - 3", "3", "2"), sat("-u + 5", "0", "5"), fails("3*u - 3", "0", "5"),
                    sat("3*u - 3", "1", "0"), fails("-u + 5", "1", "0")),
             errors={"A": "the coordinates of the crossing swapped [B1G-M, GR.1.2: x and y inverted]", "C": "where y = −x + 5 meets the y-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]", "D": "where y = 3x − 3 meets the x-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]"}),
        dict(stem="One line passes through $(0, 1)$ and $(1, 4)$; the other passes through $(0, 5)$ and $(2, 3)$. Which system is graphed?",
             fig=figs.plane((-1, 4), (-1, 6), lines=[(3, 1, ""), (-1, 5, "")], solution=(1, 4),
                            points=[(0, 1, None, "r"), (1, 4, None, "r"), (0, 5, None, "ur"), (2, 3, None, "r")], inches=2.2),
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
             fig=figs.plane((0, 4), (-3, 7), lines=[(4, -3), (-1, 7)], solution=(2, 5), inches=2.4),
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
             answer="None", why="Parallel: −3 multiplies x in both, so the lines never meet.",
             check=never_meet("-3*u + 4", "-3*u - 1"), space=0.4),
        dict(stem="$y = x + 4$   and   $y = 4 + x$   (both graph as the line shown)",
             fig=figs.plane((-5, 2), (-2, 5), lines=[(1, 4, "")], inches=2.0),
             answer="Infinitely many", why="4 + x is x + 4: one line, and every point of it makes both true.",
             check=one_line("u + 4", "4 + u"), space=0.4),
        dict(heading="For questions 6 and 7, graph both lines on the grid and solve the system."),
        dict(stem="$y = x - 4$   and   $y = -2x + 5$",
             fig=GRID((-1, 5), (-5, 5)),
             answer="(3, −1)", why="Tables at x = 0, 1, 2, 3: y = −4, −3, −2, −1 and y = 5, 3, 1, −1. Both give −1 at x = 3: 3 − 4 = −1 and −2(3) + 5 = −1.",
             check=("many", crosses("u - 4", "-2*u + 5", "3", "-1"), table_of("u - 4", [0, 1, 2, 3], [-4, -3, -2, -1]), table_of("-2*u + 5", [0, 1, 2, 3], [5, 3, 1, -1])),
             space=0.9),
        dict(stem="$y = \\frac{1}{2}x - 2$   and   $y = -x + 4$",
             fig=GRID((-1, 6), (-3, 5)),
             answer="(4, 0)", why="Even x: at x = 0, 2, 4, y = −2, −1, 0 and y = 4, 2, 0. Both give 0 at x = 4: ½(4) − 2 = 0 and −4 + 4 = 0.",
             check=("many", crosses("F(1,2)*u - 2", "-u + 4", "4", "0"), table_of("F(1,2)*u - 2", [0, 2, 4], [-2, -1, 0]), table_of("-u + 4", [0, 2, 4], [4, 2, 0])),
             space=0.9),
        dict(heading="Work backwards."),
        dict(stem="$(4, 1)$ is the solution of  $y = x - 3$  and  $y = -2x + □$. What number goes in the box?", answer="9",
             why="1 = −2(4) + □ = −8 + □, so □ = 9. Check the first: 4 − 3 = 1.",
             check=("many", ("eq", "1 + 8", "9"), crosses("u - 3", "-2*u + 9", "4", "1")), space=0.6),
        dict(heading="Solve the problem."),
        dict(stem="Tank A holds $y = -3x + 12$ gallons after x minutes, and Tank B holds $y = x + 4$ gallons. When do the tanks hold the same amount, and how much is in each?",
             fig=figs.plane((0, 5), (0, 12), lines=[(-3, 12, "A", (1, "ur")), (1, 4, "B")], ys=2, xname="minutes", yname="gallons",
                            solution=(2, 6), inches=2.6),
             answer="After 2 minutes, 6 gallons each.", why="The lines cross at (2, 6): −3(2) + 12 = 6 and 2 + 4 = 6.",
             check=("many", crosses("-3*u + 12", "u + 4", "2", "6")), space=0.5),
        dict(heading="Choose one."),
        dict(stem="$y = 2x - 5$ and $y = -x + 4$ are graphed. What is the solution of the system?",
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
        say=["To graph a line, make a table: x = 0 and two more — the third point is the check.",
             "The solution of a system is where the two lines cross, and you check it in both equations.",
             "The same number multiplying x and different numbers added: parallel lines, no solution."],
        must="Solve systems of two linear equations by graphing, in mathematical and real-world contexts; recognize that parallel lines (the same number multiplying x) never meet (AR.4.3, Clar. 3).",
        must_not="Slope or y-intercept by name (Unit 10); substitution or elimination (Algebra 1); a system not in slope-intercept form (x = 3.5).",
        read_first=[
            "A 43-minute Wednesday (Tuesday 8 Dec has no class, so the last lesson is Monday's 11.05–06). The deck is the standard plan, as 11.03's was; the cut is the teacher's. Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §11.07, standing decisions 1, 2, 3, 6 and 9), then read against Math Nation 11.7 (the unit audit, Part 2, E4, E5, E12, E13, §3–§5).",
            "Every line is graphed from a table (x = 0 and two more; the third point is the check). Parallel is 'the same number multiplying x'; you may say slope here, the slides do not. The bridge x + 1 = −2x + 7 is shown once in Notes III and practised nowhere.",
            "The boards read a graph or two tables; nobody draws two lines on a whiteboard. The Independent Set is where students draw: questions 1–5 print an empty grid, and the key's grid is the same window (E13). The key gives the tables and the crossing in words: the kit prints one figure per item, so the key shows the same empty grid.",
            "Changed from the outline: board 5 is y = 2x + 2 and y = 2x − 3 (the outline's y = 2x + 1 and y = 2x − 3 is 11.05's Notes III system). Not reproduced: the off-grid key graphs (E4, E5), end labels past the grid (E13), x = 3.5 (audit decision 2), the partner tasks."],
        standard_notes=[("Clarification", "AR.4.3: approximate non-integer solutions (11.08); slope-intercept form only; parallel lines have the same slope (Clar. 3), said here as the same number multiplying x."),
                        ("Unit boundary", "Every system is given solved for y; every crossing today is a lattice point (estimates are 11.08).")],
        sits="The unit's second systems day, before 11.08's stories and estimates. IXL C8X and TS7 are due by the Unit 11 test (Fri 11 Dec), whose questions 12–13 are today's: a solution read from a graph and a system's two tables.",
        lives="Notes I — the table and its third point — and Notes II's graph, read and checked. Board 2 is the two-tables diagnostic (swapped, the closest column, the shared y as x), board 6 the write-a-system diagnostic, board 9 the 'they must meet' claim refuted in writing.",
        materials="Whiteboards and markers; rulers. The Independent Set, one per student — its grids are for drawing.",
        variation="Boards 1–4 read a crossing — a graph, two tables (a vote), a crossing on an axis, then a graph that offers four points. The pattern breaks at 5 — parallel — and 6 votes on the system through four given points; 7 is the candle story with its price as the extra number; 8 runs backwards; 9 is written. The independent set: three systems to graph and solve (whole, negative, ½), a parallel pair and one line twice to graph, then two tables.",
        audit=["Every crossing re-derived by sympy at build time as the system's one solution, and checked in both equations; every printed table checked value by value; every parallel pair checked to have no common point and every same-line pair to be one expression; every graph drawn from its equations by u11/figs.py, which refuses a stated crossing that is not on both lines.",
               "Math Nation 11.7 read against this lesson (A7 Unit 11 Audit, Part 2, E4, E5, E12, E13, §3–§5): its sound shapes — read and verify, graph and read, a parallel pair — are here with our own numbers; its defects are not reproduced."],
        changes=["11.7.1 Which One Doesn't Belong → four retrieval questions, the table of Notes I last.",
                 "11.7.2 read-and-verify and graph-and-read → Notes II, Example 1 and boards 1–4, with new numbers and a table route.",
                 "11.7.3 approximating (x = 3.5) → not used (audit decision 2); estimates are 11.08.",
                 "11.7.4–11.7.5 parallel lines by slope → Notes III, board 5 and the written board 9, said as the same number multiplying x.",
                 "Practice and Homework L7 → the Independent Set: empty grids whose window is the key's."],
    ),
)
