# A7 11.05–06  Systems: Which Points Are Solutions; How Many Solutions — MA.8.AR.4.1 (with MA.8.AR.4.2)
# (MN 11.5 + 11.6, merged by the plan into one 53-minute period). Mon 7 Dec 2026; the last lesson is Friday's 11.04.
# The unit's first day with a line on it, and the class has never graphed y = mx + b and has no word for slope
# (Unit 11 comes before Units 10 and 7, ruling 52): Notes I builds a line from a table of values — x = 0 and two
# more, the third point the check — and calls every point of it a solution of the one equation. Then a system is
# two equations, and its solution is a pair that makes BOTH true (AR.4.1, Clarification); on the graph it is where
# the lines cross. Then the count from a graph (AR.4.2): cross once, one; parallel — "never meet" — none; the same
# line, written two ways, infinitely many, including the points nobody plotted. Every system is given solved for
# y; nothing is solved by substitution or elimination (Algebra 1). "Slope" and "y-intercept" are on no student
# surface: parallel lines are "the same number multiplying x". Built from the benchmarks and the B1G-M first (the
# unit's Lesson Outlines, §11.05–06, standing decisions 1, 2, 3, 6 and 9), then read against Math Nation 11.5–11.6
# (the unit audit, Part 2). Not reproduced: the scientific-notation warm-up, the partner exploration, the
# algebraic solves of 11.5.2 #1d and 11.5.3 (§3), Bevan's (2, 0.5) line with its −7/2 slip (E3), the false lines
# printed with "=" (E10, E11), the end labels off the grid (E13), the system definition that its own examples break
# (E17), and the slope vocabulary.
#
# Every check below is sympy over the REAL numbers: a pair is put into each equation (sat / fails), a crossing is
# the system's one solution (crosses), parallel lines have no common point (never_meet), and two ways of writing
# one line are the same expression (one_line). The figures are drawn from the equations by u11/figs.py, whose
# `plane` refuses a `solution` that is not on every line. A failed check is never printed as a false equation: it
# is written "3(2) − 2 = 4, not 5" (stepcheck holds every "=" between numbers to be true).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs11 as figs          # its own name: every unit's gates run in one process, and a second module called figs would be Unit 6's
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

# ---- the figures (u11/figs.py draws every line from its own m and b)
NOTES1 = S(figs.row([figs.table([([0, 1, 2], [2, 3, 4])], titles=["y = x + 2"]),
                     figs.plane((-3, 4), (-1, 6), lines=[(1, 2)],
                                points=[(0, 2, None, "ul"), (1, 3, None, "dr"), (2, 4, None, "dr")])],
                    gap=1.6), inches=6.6, pt=17, reserve=1.05)
# Notes II: one grid line every 2 up, so the window is square rather than tall and the plane fills the room the two
# check lines leave (14 Nov: it was 2.85 in wide); the crossing is a bare dot, its coordinates in the line under it.
# Notes II (barton 14, 15 Nov): equal scales on both axes, the crossing labelled "(2, 4)" and (0, 2) a bare dot —
# the eye goes to the solution, not to the pair that fails; (0, 2) is named in the line under the graph.
NOTES2 = S(figs.plane((-1, 4), (0, 6), lines=[(1, 2), (-2, 8, "y = −2x + 8", (3, "ur"))], solution=(2, 4),
                      points=[(2, 4, None, "r"), (0, 2, "")]), inches=5.2, pt=18, reserve=1.2)
NOTES3 = S(figs.row([figs.plane((-1, 6), (-1, 6), lines=[(1, 1, ""), (-1, 5, "")], solution=(2, 3)),
                     figs.plane((-1, 6), (-1, 6), lines=[(2, 1, ""), (2, -3, "")]),
                     figs.plane((-1, 6), (-1, 6), lines=[(H, 1, ""), (Fr(5, 10), 1, "")])],
                    gap=3.2,
                    titles=[[("y = x + 1", BLUE), ("y = −x + 5", ORANGE)],
                            [("y = 2x + 1", BLUE), ("y = 2x − 3", ORANGE)],
                            [("y = ½x + 1", BLUE), ("y = 0.5x + 1", ORANGE)]],
                    captions=["one solution", "no solution", "infinitely many"]),
           inches=11.4, pt=16, reserve=1.95)
EX2 = S(figs.plane((-2, 4), (-2, 4), lines=[(H, 2), (H, -1)]), inches=4.2, pt=18, reserve=0.9)


# ---- the board figures at 11.07's sizes (14 Nov): one bold row of words over a window no bigger than the system
# needs, slide(inches=4.2, pt=18, reserve=0.75) — about 3.3 in tall on the question slide. The story board's two
# rows of words leave less room, so its figure is set as 11.07's candles are (inches=5.0, pt=16).
def B(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.75)


def BA(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.95)

B3 = figs.plane((-4, 1), (0, 6), lines=[(1, 5), (-2, -1)], solution=(-2, 3))
B3A = figs.plane((-4, 1), (0, 6), lines=[(1, 5), (-2, -1)], solution=(-2, 3), points=[(-2, 3, "")])
B5 = figs.plane((-4, 3), (-2, 4), lines=[(1, 3), (1, -1)])
B6 = figs.plane((0, 4), (-1, 3), lines=[(1, -1, "")], points=[(1, 0, ""), (3, 2, "")])
# board 7 (fast 5, barton 3): a level line and a rising one — y = 4 is a line too, and 0 multiplies x in it
B7 = figs.plane((-1, 5), (-1, 7), lines=[(0, 4), (1, 1)], solution=(3, 4))
B7A = figs.plane((-1, 5), (-1, 7), lines=[(0, 4), (1, 1)], solution=(3, 4), points=[(3, 4, None, "dr")])

L = dict(
    code="11.05", unit=11, lesson_no="5–6", label="Lessons 5–6",
    title="Systems: Which Points Are Solutions; How Many Solutions",
    unit_title="Solving Equations and Systems",
    benchmark="MA.8.AR.4.1",
    benchmark_text="Given a system of two linear equations and a specified set of possible solutions, determine which ordered pairs satisfy the system of linear equations.",
    target="I can decide whether an ordered pair is a solution of a system, and read from a graph how many solutions a system has.",
    yesterday="Last class: multi-step equations with fractions and decimals.",
    today="Today: two equations at once — which points make both true.",
    essential="How can one ordered pair be the solution of two equations at once — and how does a graph show how many such pairs there are?",
    building_on="11.02–11.04 — solving mx + b = nx + c; 11.03 — the three endings; Grade 7 (MA.7.AR.4.3) — graphing y = px from a table; Grade 6 — plotting ordered pairs.",
    working_toward="11.07 — solving a system by graphing (MA.8.AR.4.3); 11.08 — systems in context; Unit 10 (January) — the number multiplying x gets its name; Algebra 1 (MA.912.AR.9.1) — substitution and elimination.",
    vocab=[("system of equations", "two equations taken together, like $y = x + 2$ and $y = -2x + 8$"),
           ("solution of a system", "an ordered pair $(x, y)$ that makes BOTH equations true"),
           ("intersect; point of intersection", "cross; the point where two lines cross"),
           ("parallel lines", "lines that never meet: the same number multiplies x (the same coefficient of x) and the numbers added are different"),
           ("the same line", "two equations written two ways that graph as one line")],
    vocab_note="Five words, read once each. Say 'both' twice for the second: a pair that makes one equation true is not a solution of the system. 'Intersect' is the state's word for cross: the point of intersection is the crossing. Parallel is a picture word today — never meet; the coefficient of x is the number that multiplies x (3 in 3x, −1 in −x, 0 in y = 4), and Unit 10 gives it a second name.",
    ixl=["Is (x, y) a solution to the system of equations? — N46", "Find the number of solutions to a system of equations by graphing — AGZ", "Solve a system of equations in slope-intercept form — 9Z8"],
    closure="Board 9 is written work and it is the exit evidence: Leo's pair makes the first equation true (3(1) + 1 = 4) and not the second (2(1) + 3 = 5, not 4), so it is not a solution; a solution makes both true, and (2, 7) does. A board that says only 'no' has the verdict and not the reason.",

    mtr=[("MTR.2.1", "Notes I–III: a table, a line, an equation"),
         ("MTR.4.1", "boards 4 and 6: re-vote"),
         ("MTR.6.1", "every pair checked in both equations")],
    hoq=[("Why is checking a pair in one equation not enough to call it a solution of the system?", "DOK 2"),
         ("Two lines cross at one point. Why can the system not have a second solution?", "DOK 3"),
         ("One line is drawn for two equations. Why is every point of it a solution of the system — the points nobody marked too?", "DOK 2")],
    differentiation=[
        ("ESE / 504", "A two-column check table on the board all period — 'first equation' and 'second equation' — and every pair gets a mark in BOTH columns before anyone says 'solution'. The three pictures of Notes III stay up from board 3 on."),
        ("ELL", "**System**: two equations that go together. **Solution**: a pair that makes both true. **Parallel**: like train tracks — they never meet. **Intersect**: cross, meet at one point."),
        ("Enrichment", "Board 6 finishes early for some: write a second equation that makes a system with y = 3x − 2 that has (a) no solution, (b) infinitely many, (c) exactly the solution (1, 1). (Any y = 3x + b with b ≠ −2; y = 3x − 2 written another way, such as y = −2 + 3x; any line through (1, 1) with a different number multiplying x, such as y = x.)")],

    warmup=[
        dict(stem="Solve:  $\\frac{1}{2}(4x + 6) = x + 8$", answer="x = 5", band="last lesson",
             source="11.04 — a fraction distributed: 2x + 3 = x + 8",
             check=("eq", "sp.solve(sp.Eq(F(1,2)*(4*" + X + " + 6), " + X + " + 8), " + X + ")[0]", "5")),
        dict(stem="How many solutions does  $3x + 4 = 3x - 4$  have?", answer="No solution", band="last week",
             source="11.03 — the three endings: take 3x from both sides, 4 = −4, never true",
             check=("true", "sp.solve(sp.Eq(3*" + X + " + 4, 3*" + X + " - 4), " + X + ") == []")),
        dict(stem="Two angles are vertical angles. One is 72°. Find the other.", answer="72°", band="last unit",
             source="T-B1 — vertical angles are equal",
             check=("eq", "72", "72")),
        dict(stem="$y = 2x + 1$.  Find y when $x = 3$.", answer="y = 7", band="the prerequisite this lesson needs",
             source="1.03 — a value put into an expression and worked out (Unit 1); every table and every check today is this move",
             check=("eq", "2*3 + 1", "7")),
    ],
    warmup_note="Q4 is today's move: put the x in, get the y. (3, 7) is a point that makes y = 2x + 1 true — say that one sentence after the reveal; Notes I makes a whole line of such points. Two minutes silent, then reveal, no discussion.",

    notes=[
        dict(numeral="I", head="One equation in x and y: its solutions make a line", min=4, sub="Copy the table and the line.",
             note="An equation in two letters has many solutions, each an ordered pair. Make a table: x = 0 first, then two more — put each x in and get its y. Plot the three points; they line up, and the line through them holds every solution. Two points draw the line; the third is the check — if it misses, a y is wrong. (1, 3) is a solution because 3 = 1 + 2; (1.5, 3.5) is one too, a point between the grid lines, and so is (100, 102), off the grid. This is the first line this class has drawn from an equation (Unit 10 comes later).\nOFF: 'Pick an x, find its y, plot the point. Every point on the line makes the equation true.'",
             fig=NOTES1,
             items2=["$(1, 3)$ is a solution:   $1 + 2 = 3$.   So is every point on the line."],
             letters=False),
        dict(numeral="II", head="A system's solution makes both equations true", min=3, sub="",
             note="Two equations together are a system, and its solution is a pair that makes BOTH true. Put (2, 4) into each: 2 + 2 = 4 and −2(2) + 8 = 4 — a solution. (0, 2) makes the first true and the second not (−2(0) + 8 is 8, not 2) — so it is a solution of y = x + 2 only, and not of the system. On the graph the solution is the point on both lines: where they cross — where they intersect, the point of intersection. (Say nothing today about setting the two expressions equal: 11.07 Notes III shows it.)\nOFF: 'A solution of the system makes both equations true. One is not enough.'",
             fig=NOTES2,
             items2=["$(2, 4)$:   $2 + 2 = 4$   and   $-2(2) + 8 = 4$.   A solution.",
                     "$(0, 2)$:   $0 + 2 = 2$,  but  $-2(0) + 8 = 8$, not 2.   Not a solution."],
             letters=False),
        dict(numeral="III", head="How many solutions? Read the graph", min=3, sub="",
             note="Three pictures, three counts — read from the picture; the reasons from the equations are 11.07's. Cross once: one solution, the crossing (2, 3). Parallel — they never meet: no solution. The same line — the orange dashes lie on the blue: every point of it is on both graphs, the ones nobody plotted too (infinitely many). These are 11.03's three endings again: one, none, every. Then the level line: y = 3 is a line too — every x gives 3 — so a level line can cross a slanted one, or run parallel to another level line.\nOFF: 'Cross once: one. Never meet: none. The same line: infinitely many.'",
             fig=NOTES3,
             items2=["Cross once: one.   Never meet: none.   The same line: infinitely many.",
                     "$y = 3$  is a line too: every x gives 3."],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", sub="Which pair makes both true?", min_q=1,
             note_q="Ask what has to be true of a solution before anyone substitutes: it makes BOTH equations true.",
             prompt=["$y = 3x - 1$   and   $y = x + 5$", "$(3, 8) \\qquad (1, 2) \\qquad (2, 7)$"], ask="Which ordered pair is a solution of the system?",
             worked=[dict(sub="Worked.", min=2,
                          note="Each pair into each equation. (3, 8): 3(3) − 1 = 8 and 3 + 5 = 8 — both true, a solution. (1, 2) makes the first true and the second not (1 + 5 is 6). (2, 7) makes the second true and the first not (3(2) − 1 is 5). Each wrong pair passes one equation: a board that tested one equation only picked it.",
                          rows=[("(3, 8):\\quad 3(3) - 1 = 8 \\quad\\text{and}\\quad 3 + 5 = 8", "both true: a solution"),
                                ("(1, 2):\\quad 3(1) - 1 = 2 \\quad\\text{but}\\quad 1 + 5 = 6", "6, not 2: the second fails"),
                                ("(2, 7):\\quad 3(2) - 1 = 5", "5, not 7: the first fails")],
                          answer="(3, 8)")],
             check=("many", sat("3*u - 1", "3", "8"), sat("u + 5", "3", "8"), sat("3*u - 1", "1", "2"), fails("u + 5", "1", "2"),
                    fails("3*u - 1", "2", "7"), sat("u + 5", "2", "7"), crosses("3*u - 1", "u + 5", "3", "8")),
             your_turn=dict(min=2, note="(2, 7): 2(2) + 3 = 7 and −2 + 9 = 7. (0, 3) passes the first only; (4, 5) passes the second only. A board with (0, 3) or (4, 5) tested one equation.",
                            prompt=["$y = 2x + 3$   and   $y = -x + 9$", "$(2, 7) \\qquad (0, 3) \\qquad (4, 5)$"],
                            ask="Which ordered pair is a solution of the system?",
                            steps=["$(2, 7)$:   $2(2) + 3 = 7$   and   $-2 + 9 = 7$",
                                   "$(0, 3)$:   $2(0) + 3 = 3$,  but  $-(0) + 9 = 9$",
                                   "$(4, 5)$:   $2(4) + 3 = 11$,  not 5"],
                            gloss="each pair into both equations", answer="(2, 7)"),
             yt_check=("many", sat("2*u + 3", "2", "7"), sat("-u + 9", "2", "7"), sat("2*u + 3", "0", "3"), fails("-u + 9", "0", "3"),
                       fails("2*u + 3", "4", "5"), sat("-u + 9", "4", "5"))),
        dict(title="Example 2", sub="How many, from a graph.", min_q=1,
             note_q="Ask whether the two lines will ever meet if the grid went on forever, before anyone answers 'how many'.",
             prompt=["The graphs of  $y = \\frac{1}{2}x + 2$  and  $y = \\frac{1}{2}x - 1$  are shown."],
             fig=EX2, ask="How many solutions does the system have?",
             worked=[dict(sub="Worked.", min=1,
                          note="Read the two lines on the grid at three x's: at x = 0 they are at 2 and −1, at x = 2 at 3 and 0, at x = 4 at 4 and 1 — always 3 apart. Lines that stay 3 apart never meet: parallel, and no pair makes both true. (No algebra today: the reason from the equations is 11.07's.) A board with 'one' guessed the lines meet off the grid; with 'infinitely many', saw two lines going on forever.",
                          rows=[("x = 0:\\quad 2 \\quad\\text{and}\\quad -1", "3 apart"),
                                ("x = 2:\\quad 3 \\quad\\text{and}\\quad 0", "3 apart"),
                                ("x = 4:\\quad 4 \\quad\\text{and}\\quad 1", "always 3 apart: they never meet")],
                          answer="No solution")],
             check=("many", never_meet("F(1,2)*u + 2", "F(1,2)*u - 1"),
                    sat("F(1,2)*u + 2", "0", "2"), sat("F(1,2)*u - 1", "0", "-1"), sat("F(1,2)*u + 2", "2", "3"),
                    sat("F(1,2)*u - 1", "2", "0"), sat("F(1,2)*u + 2", "4", "4"), sat("F(1,2)*u - 1", "4", "1")),
             # the Your Turn carries its two tables in rows (the kit's Your Turn slide carries no figure — the lead's
             # ruling, 15 Nov): the same kind as the worked slide, a pair of lines always the same distance apart
             your_turn=dict(min=2, note="The tables, read column by column: 1 and −3, 5 and 1, 9 and 5 — the first is always 4 more, so the lines stay 4 apart and never meet: no solution. A board with 'one' expects them to meet past the table; with 'infinitely many', read two lines that go on forever.",
                            prompt=["$y = 4x + 1$   and   $y = 4x - 3$",
                                    "At  $x = 0,\\ 1,\\ 2$:   $y = 4x + 1$  gives  $1,\\ 5,\\ 9$",
                                    "and   $y = 4x - 3$  gives  $-3,\\ 1,\\ 5$"],
                            ask="How many solutions does the system have?",
                            steps=["at each x the first is 4 more:   1 and $-3$,   5 and 1,   9 and 5",
                                   "always 4 apart:  parallel, they never meet"],
                            gloss="always 4 apart", answer="No solution"),
             yt_check=("many", never_meet("4*u + 1", "4*u - 3"), table_of("4*u + 1", [0, 1, 2], [1, 5, 9]),
                       table_of("4*u - 3", [0, 1, 2], [-3, 1, 5]))),
    ],

    # The round: a pair that passes both (1) and one that fails the second (2); the crossing read from a graph (3);
    # the diagnostic on the four ways to pick a pair (4); the pattern breaks at 5 — parallel, none — and 6 votes on
    # the same line; the extra-number story read at its crossing (7); backwards (8); and the one-equation check
    # found and fixed in writing (9).
    whiteboard=[
        dict(text=["$y = x - 3$   and   $y = -x + 5$", "**Is $(4, 1)$ a solution of the system?"],
             hint="Both equations.", steps=["$4 - 3 = 1$   and   $-4 + 5 = 1$", "true in both equations"],
             gloss="4 − 3 = 1 and −4 + 5 = 1", answer="Yes: it makes both equations true",
             note="Both true: yes. A board with 'no' most likely took −4 + 5 as −9 or 9 — ask for the second check aloud.",
             check=("many", sat("u - 3", "4", "1"), sat("-u + 5", "4", "1")),
             wrong="No — −4 + 5 taken as 9 or −9 [B1G-M, AR.4.1: substitution errors]"),
        dict(text=["$y = 2x + 1$   and   $y = 3x - 2$", "**Is $(2, 5)$ a solution of the system?"],
             hint="One is not enough.", steps=["$2(2) + 1 = 5$,   but   $3(2) - 2 = 4$,  not 5"],
             gloss="the second equation fails", answer="No: 3(2) − 2 = 4, not 5",
             note="The first is true and the second is not, so (2, 5) is not a solution of the system — it is a solution of y = 2x + 1 only. A board with 'yes' stopped after the first equation: today's named misconception.",
             check=("many", sat("2*u + 1", "2", "5"), fails("3*u - 2", "2", "5")),
             wrong="Yes — checked the first equation only [B1G-M, AR.4.1: one pair, two equations]"),
        # repeat_ok: rule D matches only the grid's axis numbers (0–6, shared by every plane today) and the
        # answer's digits; this system (y = x + 5, y = −2x − 1, crossing at (−2, 3)) appears nowhere above.
        # the extra-number board (ruling 22) since the savings story went (barton 3): the grid's height, 6, is a
        # number nobody needs — it is not in the system, its crossing, or its check
        dict(repeat_ok=True, text=["**Ty drew this system on a grid 6 units tall. What is its solution?"],
             unneeded="6",
             fig=B(B3), fig_a=BA(B3A),
             hint="Where do they cross?", steps=["the lines cross once, at $(-2, 3)$", "$-2 + 5 = 3$   and   $-2(-2) - 1 = 3$"],
             gloss="read the crossing, then check it", answer="(−2, 3) — one solution",
             note="The extra-number board (ruling 22): the grid's height, 6, is not needed. Read the crossing on the grid lines: x = −2, y = 3. Then check it in both: −2 + 5 = 3 and 4 − 1 = 3. One crossing, one solution. A board with (3, −2) swapped the coordinates; one with (0, 5) or (0, −1) read where a line meets the y-axis; one with a 6 in it used the grid's height.",
             check=("many", crosses("u + 5", "-2*u - 1", "-2", "3"), sat("u + 5", "-2", "3"), sat("-2*u - 1", "-2", "3")),
             wrong="(3, −2) — x and y swapped [B1G-M, GR.1.2: x and y inverted]; (0, 5) — where one line meets the y-axis, on one line only [B1G-M, AR.4.1: a solution satisfies both]; (−2, 6) — the grid's height used [ruling 22]"),
        dict(kind="mc", text=["$y = 2x - 4$   and   $y = -x + 5$", "**Which ordered pair is a solution of the system?"],
             qtext="y = 2x − 4 and y = −x + 5. Which ordered pair is a solution of the system?",
             hint="Test each pair in both.", steps=["$(3, 2)$:   $2(3) - 4 = 2$   and   $-3 + 5 = 2$"],
             choices=["(0, 5)", "(2, 3)", "(2, 0)", "(3, 2)"], correct=3, answer="D — (3, 2)",
             errors={"A": "the second equation only: 2(0) − 4 is −4 [B1G-M, AR.4.1: a solution satisfies both]", "B": "the coordinates of (3, 2) swapped [B1G-M, GR.1.2: x and y inverted]", "C": "the first equation only: −2 + 5 is 3 [B1G-M, AR.4.1: a solution satisfies both]"},
             note="Diagnostic. Option C passes the first equation only, option A the second only, and option B is the answer with x and y swapped (it happens to pass the second: −2 + 5 = 3, but 2(2) − 4 = 0). On a split: sixty seconds, convince your neighbor, re-vote — then check (3, 2) in both aloud.",
             check=("many", sat("2*u - 4", "3", "2"), sat("-u + 5", "3", "2"),
                    sat("2*u - 4", "2", "0"), fails("-u + 5", "2", "0"),
                    fails("2*u - 4", "0", "5"), sat("-u + 5", "0", "5"),
                    fails("2*u - 4", "2", "3"))),
        dict(text=["**The system is graphed. How many solutions does it have?"],
             fig=B(B5), fig_a=BA(B5),
             hint="Will they ever meet?", steps=["$x + 3$ and $x - 1$:  1 multiplies x in both", "parallel: they never meet"],
             gloss="parallel: never meet", answer="No solution — the lines are parallel",
             note="The pattern breaks: no crossing to read. The same number (1) multiplies x in both, and the added numbers differ, so the first line is always 4 above the second and they never meet. A board with 'one' expects them to meet somewhere off the grid; with 'infinitely many', saw two lines that go on forever.",
             check=never_meet("u + 3", "u - 1"),
             wrong="one — the lines are taken to meet off the grid [B1G-M, AR.4.2]; infinitely many — 'the lines go on forever' [B1G-M, AR.4.2]"),
        # board 6 (critic 8, 15 Nov): a multiple-choice question slide leaves a graph about 1.5 in tall (its four options
        # take 1.75 in), so the one line and its two marked points are given in words and the graph, at full size, is
        # on the reveal — as 11.07's board 6 does
        dict(kind="mc", text=["$y = x - 1$  and  $y = -1 + x$  are one line,", "with  $(1, 0)$  and  $(3, 2)$  marked on it.",
                              "**How many solutions does the system have?"],
             qtext="y = x − 1 and y = −1 + x graph as one line. Two points of it are marked: (1, 0) and (3, 2). How many solutions does the system have?",
             fig_a=S(B6, inches=4.2, pt=18, reserve=1.0),
             hint="Which points are on both?", steps=["$10 - 1 = 9$  and  $-1 + 10 = 9$"],
             choices=["one", "infinitely many", "none", "two"], correct=1, answer="B — infinitely many",
             errors={"A": "one line drawn, read as one solution [B1G-M, AR.4.2: the same-line case]", "C": "no crossing point seen, so 'no solution' [B1G-M, AR.4.2: the same-line case]", "D": "only the two marked points counted [B1G-M, AR.4.3: only the plotted points]"},
             note="Diagnostic on the same-line case, the state's named misconception for AR.4.2; the graph is on the reveal. Every point of the line is on both graphs, the points nobody marked too: (10, 9) is off the grid and makes both true. Option D counts the two marked points; option C looks for a crossing and finds none; option A counts the one line. A and C are the same misreading — the same line taken for something other than every point — and get the same response: point at a third point of the line and check it in both.",
             check=("many", one_line("u - 1", "-1 + u"), sat("u - 1", "1", "0"), sat("u - 1", "3", "2"),
                    sat("u - 1", "10", "9"), sat("-1 + u", "10", "9"))),
        # board 7 (barton 3, fast 5): the savings story went (a crossing in a story is 11.08's board 2); a level
        # line takes its place — y = 4 has 0 multiplying x, and it still crosses a slanted line once
        dict(repeat_ok=True, text=["**$y = 4$  and  $y = x + 1$  are graphed. How many solutions?"],
             fig=B(B7), fig_a=BA(B7A),
             hint="A level line is a line.", steps=["the lines cross once, at $(3, 4)$", "$y = 4$  for every x,   and   $3 + 1 = 4$"],
             gloss="a level line crosses a slanted one once", answer="One solution: (3, 4)",
             note="A level line: y = 4 gives 4 for every x, so its graph is flat — 0 multiplies x. It crosses the rising line once, at (3, 4): 3 + 1 = 4, and y = 4 there. A board with 'none' thought a line with no x cannot meet anything; with (4, 3), swapped.",
             check=("many", crosses("4 + 0*u", "u + 1", "3", "4"), sat("u + 1", "3", "4")),
             wrong="no solution — 'y = 4 has no x, so it is not a line' [B1G-M, AR.4.2]; (4, 3) — x and y swapped [B1G-M, GR.1.2: x and y inverted]"),
        dict(text=["$(2, □)$ is a solution of  $y = 3x + 1$  and  $y = x + 5$.", "**What number goes in the box?"],
             hint="Put 2 in for x.", steps=["$3(2) + 1 = 7$   and   $2 + 5 = 7$"],
             gloss="the same y from both", answer="7",
             note="Backwards: x is given and y is missing. Put 2 into each equation; both give 7, so (2, 7) is the solution. Check both — a pair is a solution only if both equations give the same y.",
             check=("many", ("eq", "3*2 + 1", "7"), ("eq", "2 + 5", "7"), crosses("3*u + 1", "u + 5", "2", "7")),
             wrong="6 — 3(2) with the + 1 left off [B1G-M, AR.4.1: substitution errors]; 5 — 3 + 2, the 3 added to x instead of multiplying it [B1G-M, AR.4.1: substitution errors]"),
        dict(kind="written", text=["Leo says $(1, 4)$ is a solution of  $y = 3x + 1$  and  $y = 2x + 3$,",
                                   "because it makes the first equation true.", "**Is Leo right? Explain."],
             qtext="Leo says (1, 4) is a solution of y = 3x + 1 and y = 2x + 3, because it makes the first equation true. Is Leo right? Explain.",
             hint="Did he check the second?", steps=["first:   $3(1) + 1 = 4$", "second:   $2(1) + 3 = 5$,  not 4",
                                                    "a solution makes both true:   $(2, 7)$  does"],
             gloss="one is not enough", answer="No: 2(1) + 3 = 5, not 4.",
             te_answer="Full credit: 'no' AND the reason — (1, 4) fails the second equation, 2(1) + 3 = 5, not 4, and a solution of a system makes BOTH equations true. Naming (2, 7) is not needed (3(2) + 1 = 7 and 2(2) + 3 = 7); 'no' with no check earns none.",
             note="Written, and the exit evidence: today's named misconception — a pair that satisfies one equation called a solution of the system. Read two aloud.",
             check=("many", sat("3*u + 1", "1", "4"), fails("2*u + 3", "1", "4"), crosses("3*u + 1", "2*u + 3", "2", "7")),
             wrong="'yes, it works in the first' — one equation checked [B1G-M, AR.4.1: one pair, two equations]"),
    ],

    independent=[
        dict(stem="Is $(3, -1)$ a solution of the system  $y = 2x - 7$  and  $y = -x + 2$?", answer="Yes",
             why="2(3) − 7 = −1 and −3 + 2 = −1: both true.",
             check=("many", sat("2*u - 7", "3", "-1"), sat("-u + 2", "3", "-1")), space=0.6),
        dict(stem="$(-1, 4)$ makes one equation of the system  $y = -3x + 1$  and  $y = x + 6$  false. Which one?",
             answer="y = x + 6", why="−3(−1) + 1 = 4 is true; −1 + 6 = 5, not 4. So (−1, 4) is not a solution of the system.",
             check=("many", sat("-3*u + 1", "-1", "4"), fails("u + 6", "-1", "4")), space=0.6),
        # question 3 (critic 12 = fast 4, 15 Nov): FAST's multiselect never says how many, and here two systems pass —
        # each wrong system is true in exactly one of its equations (the named error: one is not enough)
        dict(stem="Select all the systems that have  $(2, 5)$  as a solution.",
             choices=["$y = x + 3$  and  $y = 3x - 1$", "$y = 2x + 1$  and  $y = x + 4$", "$y = -x + 7$  and  $y = 4x - 3$",
                      "$y = 3x - 2$  and  $y = -2x + 9$", "$y = 5x - 5$  and  $y = x + 2$"], correct=[0, 2], answer="A, C",
             why="A: 2 + 3 = 5 and 3(2) − 1 = 5. C: −2 + 7 = 5 and 4(2) − 3 = 5. B: 2(2) + 1 = 5, but 2 + 4 = 6. D: −2(2) + 9 = 5, but 3(2) − 2 = 4. E: 5(2) − 5 = 5, but 2 + 2 = 4. Each wrong system passes one equation only.",
             check=("many", crosses("u + 3", "3*u - 1", "2", "5"), crosses("-u + 7", "4*u - 3", "2", "5"),
                    sat("2*u + 1", "2", "5"), fails("u + 4", "2", "5"),
                    sat("-2*u + 9", "2", "5"), fails("3*u - 2", "2", "5"),
                    sat("5*u - 5", "2", "5"), fails("u + 2", "2", "5")),
             errors={"B": "true in y = 2x + 1 only: 2 + 4 = 6, not 5 [B1G-M, AR.4.1: a solution satisfies both]", "D": "true in y = −2x + 9 only: 3(2) − 2 = 4, not 5 [B1G-M, AR.4.1: a solution satisfies both]", "E": "true in y = 5x − 5 only: 2 + 2 = 4, not 5 [B1G-M, AR.4.1: a solution satisfies both]"}),
        dict(stem="The graphs of  $y = 3x + 2$  and  $y = 3x - 4$  are shown. How many solutions does the system have?",
             fig=figs.plane((-3, 3), (-8, 8), lines=[(3, 2), (3, -4)], ys=2, inches=2.4),
             answer="No solution", why="The lines are parallel: they stay 6 apart and never meet.",
             check=never_meet("3*u + 2", "3*u - 4"), space=0.5),
        dict(stem="The graphs of  $y = x - 1$  and  $y = -3x + 7$  are shown. How many solutions does the system have, and what is it?",
             fig=figs.plane((0, 4), (-2, 7), lines=[(1, -1), (-3, 7)], solution=(2, 1), inches=2.4),
             answer="One: (2, 1)", why="The lines cross once, at (2, 1): 2 − 1 = 1 and −3(2) + 7 = 1.",
             check=("many", crosses("u - 1", "-3*u + 7", "2", "1"), sat("u - 1", "2", "1"), sat("-3*u + 7", "2", "1")), space=0.5),
        dict(stem="Both equations of the system  $y = \\frac{3}{2}x - 2$  and  $y = 1.5x - 2$  graph as the line shown. How many solutions does the system have?",
             fig=figs.plane((0, 4), (-2, 4), lines=[(Fr(3, 2), -2, "")], inches=2.4),
             answer="Infinitely many solutions", why="3/2 and 1.5 are one number, so the two equations are one line, and every point of it — such as (2, 1) and (4, 4) — makes both true.",
             check=("many", one_line("F(3,2)*u - 2", "F(15,10)*u - 2"), sat("F(3,2)*u - 2", "2", "1"), sat("F(3,2)*u - 2", "4", "4")), space=0.5),
    ],

    # Bank: a pair in a system, yes or no (1–3, the third with a fraction and a fractional check), the equation a
    # pair makes false (4–5), backwards (6), three graphs — cross, parallel, the same line (7–9), a story's crossing
    # (10), the diagnostic mc (11), and a select-all on a same-line system (12). The additional bank mirrors it
    # position by position with new numbers.
    bank=[
        dict(heading="For questions 1 through 3, decide whether the ordered pair is a solution of the system."),
        dict(stem="$(3, 5)$;   $y = 2x - 1$  and  $y = x + 2$", answer="Yes", why="2(3) − 1 = 5 and 3 + 2 = 5.",
             check=("many", sat("2*u - 1", "3", "5"), sat("u + 2", "3", "5")), space=0.6),
        dict(stem="$(-2, 1)$;   $y = -x - 1$  and  $y = 2x + 3$", answer="No", why="−(−2) − 1 = 1 is true; 2(−2) + 3 = −1, not 1.",
             check=("many", sat("-u - 1", "-2", "1"), fails("2*u + 3", "-2", "1")), space=0.6),
        dict(stem="$(3, 0)$;   $y = \\frac{2}{3}x - 2$  and  $y = -x + 3$", answer="Yes", why="⅔(3) − 2 = 2 − 2 = 0 and −3 + 3 = 0.",
             check=("many", sat("F(2,3)*u - 2", "3", "0"), sat("-u + 3", "3", "0")), space=0.6),
        dict(heading="For questions 4 and 5, the ordered pair makes one equation of the system false. Which one?"),
        dict(stem="$(1, 6)$;   $y = 4x + 2$  and  $y = x + 3$", answer="y = x + 3", why="4(1) + 2 = 6 is true; 1 + 3 = 4, not 6.",
             check=("many", sat("4*u + 2", "1", "6"), fails("u + 3", "1", "6")), space=0.6),
        dict(stem="$(-2, -5)$;   $y = x - 3$  and  $y = 2x + 1$", answer="y = 2x + 1", why="−2 − 3 = −5 is true; 2(−2) + 1 = −3, not −5.",
             check=("many", sat("u - 3", "-2", "-5"), fails("2*u + 1", "-2", "-5")), space=0.6),
        dict(heading="Work backwards."),
        dict(stem="$(3, □)$ is a solution of  $y = 4x - 5$  and  $y = x + 4$. What number goes in the box?", answer="7",
             why="4(3) − 5 = 7 and 3 + 4 = 7.", check=("many", ("eq", "4*3 - 5", "7"), ("eq", "3 + 4", "7")), space=0.6),
        dict(heading="For questions 7 through 9, use the graph."),
        dict(stem="The graphs of  $y = 2x - 3$  and  $y = -x + 3$  are shown. What is the solution of the system?",
             fig=figs.plane((-1, 4), (-5, 5), lines=[(2, -3), (-1, 3)], solution=(2, 1), inches=2.4),
             answer="(2, 1)", why="The lines cross once, at (2, 1): 2(2) − 3 = 1 and −2 + 3 = 1.",
             check=crosses("2*u - 3", "-u + 3", "2", "1"), space=0.4),
        dict(stem="The graphs of  $y = -2x + 1$  and  $y = -2x + 5$  are shown. How many solutions does the system have?",
             fig=figs.plane((-2, 3), (-6, 10), lines=[(-2, 1, ""), (-2, 5, "")], ys=2, inches=2.4),
             answer="No solution", why="Parallel: −2 multiplies x in both; the lines never meet.",
             check=never_meet("-2*u + 1", "-2*u + 5"), space=0.4),
        dict(stem="Both equations of the system  $y = x - 3$  and  $y = -3 + x$  graph as the line shown. How many solutions does the system have?",
             fig=figs.plane((-2, 6), (-5, 3), lines=[(1, -3, "")], inches=2.4),
             answer="Infinitely many solutions", why="One expression written two ways: every point of the line is a solution.",
             check=one_line("u - 3", "-3 + u"), space=0.4),
        dict(heading="Solve the problem."),
        dict(stem="Gym A costs $y = 15x + 30$ dollars for x months, and Gym B costs $y = 25x$ dollars. The two graphs cross at $(3, 75)$. What does that point mean?",
             answer="After 3 months, both gyms cost \\$75 in all.", why="15(3) + 30 = 75 and 25(3) = 75.",
             check=("many", crosses("15*u + 30", "25*u", "3", "75")), space=0.6),
        dict(heading="Choose one."),
        dict(stem="Which ordered pair is a solution of the system  $y = 3x - 2$  and  $y = x + 4$?",
             choices=["$(2, 4)$", "$(3, 7)$", "$(0, 4)$", "$(7, 3)$"], correct=1, answer="B",
             why="3(3) − 2 = 7 and 3 + 4 = 7.",
             check=("many", crosses("3*u - 2", "u + 4", "3", "7"), sat("3*u - 2", "2", "4"), fails("u + 4", "2", "4"),
                    fails("3*u - 2", "0", "4"), sat("u + 4", "0", "4"), fails("3*u - 2", "7", "3"), fails("u + 4", "7", "3")),
             errors={"A": "makes the first equation true only [B1G-M, AR.4.1: a solution satisfies both]", "C": "makes the second equation true only [B1G-M, AR.4.1: a solution satisfies both]", "D": "the coordinates of (3, 7) swapped [B1G-M, GR.1.2: x and y inverted]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the ordered pairs that are solutions of the system  $y = 2x + 2$  and  $y = 2(x + 1)$.",
             choices=["$(3, 8)$", "$(2, 5)$", "$(1, 4)$", "$(0, 2)$", "$(-1, 1)$"], correct=[0, 2, 3], answer="A, C, D",
             why="2(x + 1) = 2x + 2, so the two equations are one line and every point of it is a solution: (0, 2), (1, 4) and (3, 8) are on it; (2, 5) and (−1, 1) are not (2(2) + 2 = 6; 2(−1) + 2 = 0).",
             check=("many", one_line("2*u + 2", "2*(u + 1)"), sat("2*u + 2", "0", "2"), sat("2*u + 2", "1", "4"), sat("2*u + 2", "3", "8"),
                    fails("2*u + 2", "2", "5"), fails("2*u + 2", "-1", "1")),
             errors={"B": "2(2) + 2 is 6, not 5 [B1G-M, AR.4.1: substitution errors]", "E": "2(−1) + 2 is 0, not 1 [B1G-M, AR.4.1: substitution errors]"}),
    ],

    additional=[
        dict(heading="For questions 1 through 3, decide whether the ordered pair is a solution of the system."),
        dict(stem="$(4, 7)$;   $y = 2x - 1$  and  $y = x + 3$", answer="Yes", why="2(4) − 1 = 7 and 4 + 3 = 7.",
             check=("many", sat("2*u - 1", "4", "7"), sat("u + 3", "4", "7")), space=0.6),
        dict(stem="$(-3, 2)$;   $y = -x - 1$  and  $y = x + 4$", answer="No", why="−(−3) − 1 = 2 is true; −3 + 4 = 1, not 2.",
             check=("many", sat("-u - 1", "-3", "2"), fails("u + 4", "-3", "2")), space=0.6),
        dict(stem="$(6, 1)$;   $y = \\frac{1}{2}x - 2$  and  $y = -x + 7$", answer="Yes", why="½(6) − 2 = 3 − 2 = 1 and −6 + 7 = 1.",
             check=("many", sat("F(1,2)*u - 2", "6", "1"), sat("-u + 7", "6", "1")), space=0.6),
        dict(heading="For questions 4 and 5, the ordered pair makes one equation of the system false. Which one?"),
        dict(stem="$(2, 9)$;   $y = 3x + 3$  and  $y = x + 6$", answer="y = x + 6", why="3(2) + 3 = 9 is true; 2 + 6 = 8, not 9.",
             check=("many", sat("3*u + 3", "2", "9"), fails("u + 6", "2", "9")), space=0.6),
        dict(stem="$(-1, -4)$;   $y = x - 3$  and  $y = 2x - 1$", answer="y = 2x − 1", why="−1 − 3 = −4 is true; 2(−1) − 1 = −3, not −4.",
             check=("many", sat("u - 3", "-1", "-4"), fails("2*u - 1", "-1", "-4")), space=0.6),
        dict(heading="Work backwards."),
        dict(stem="$(4, □)$ is a solution of  $y = 2x - 3$  and  $y = x + 1$. What number goes in the box?", answer="5",
             why="2(4) − 3 = 5 and 4 + 1 = 5.", check=("many", ("eq", "2*4 - 3", "5"), ("eq", "4 + 1", "5")), space=0.6),
        dict(heading="For questions 7 through 9, use the graph."),
        dict(stem="The graphs of  $y = x + 1$  and  $y = -2x + 4$  are shown. What is the solution of the system?",
             fig=figs.plane((-2, 3), (-3, 5), lines=[(1, 1), (-2, 4)], solution=(1, 2), inches=2.4),
             answer="(1, 2)", why="The lines cross once, at (1, 2): 1 + 1 = 2 and −2(1) + 4 = 2.",
             check=crosses("u + 1", "-2*u + 4", "1", "2"), space=0.4),
        dict(stem="The graphs of  $y = 3x - 1$  and  $y = 3x + 2$  are shown. How many solutions does the system have?",
             fig=figs.plane((-2, 2), (-8, 8), lines=[(3, -1), (3, 2)], ys=2, inches=2.4),
             answer="No solution", why="Parallel: 3 multiplies x in both; the lines never meet.",
             check=never_meet("3*u - 1", "3*u + 2"), space=0.4),
        dict(stem="Both equations of the system  $y = -x + 2$  and  $y = 2 - x$  graph as the line shown. How many solutions does the system have?",
             fig=figs.plane((-2, 5), (-3, 4), lines=[(-1, 2, "")], inches=2.4),
             answer="Infinitely many solutions", why="One expression written two ways: every point of the line is a solution.",
             check=one_line("-u + 2", "2 - u"), space=0.4),
        dict(heading="Solve the problem."),
        dict(stem="Pool A costs $y = 5x + 40$ dollars for x visits, and Pool B costs $y = 13x$ dollars. The two graphs cross at $(5, 65)$. What does that point mean?",
             answer="After 5 visits, both pools cost \\$65 in all.", why="5(5) + 40 = 65 and 13(5) = 65.",
             check=("many", crosses("5*u + 40", "13*u", "5", "65")), space=0.6),
        dict(heading="Choose one."),
        dict(stem="Which ordered pair is a solution of the system  $y = 2x + 1$  and  $y = -x + 7$?",
             choices=["$(1, 3)$", "$(5, 2)$", "$(2, 5)$", "$(3, 4)$"], correct=2, answer="C",
             why="2(2) + 1 = 5 and −2 + 7 = 5.",
             check=("many", crosses("2*u + 1", "-u + 7", "2", "5"), sat("2*u + 1", "1", "3"), fails("-u + 7", "1", "3"),
                    fails("2*u + 1", "3", "4"), sat("-u + 7", "3", "4"), fails("2*u + 1", "5", "2")),
             errors={"A": "makes the first equation true only [B1G-M, AR.4.1: a solution satisfies both]", "B": "the coordinates of (2, 5) swapped [B1G-M, GR.1.2: x and y inverted]", "D": "makes the second equation true only [B1G-M, AR.4.1: a solution satisfies both]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the ordered pairs that are solutions of the system  $y = 3x - 3$  and  $y = 3(x - 1)$.",
             choices=["$(-1, -4)$", "$(3, 9)$", "$(2, 3)$", "$(1, 0)$", "$(0, -3)$"], correct=[2, 3, 4], answer="C, D, E",
             why="3(x − 1) = 3x − 3, so the two equations are one line: (1, 0), (2, 3) and (0, −3) are on it; (3, 9) and (−1, −4) are not (3(3) − 3 = 6; 3(−1) − 3 = −6).",
             check=("many", one_line("3*u - 3", "3*(u - 1)"), sat("3*u - 3", "1", "0"), sat("3*u - 3", "2", "3"), sat("3*u - 3", "0", "-3"),
                    fails("3*u - 3", "3", "9"), fails("3*u - 3", "-1", "-4")),
             errors={"A": "3(−1) − 3 is −6, not −4 [B1G-M, AR.4.1: substitution errors]", "B": "3(3) − 3 is 6, not 9 [B1G-M, AR.4.1: substitution errors]"}),
    ],

    te=dict(
        say=["A solution of a system is an ordered pair that makes both equations true — one is not enough.",
             "On the graph, the solution is where the lines cross: cross once, one solution; parallel, never meet, none.",
             "Two equations that are one line written two ways have infinitely many solutions — every point of the line."],
        must="Test given ordered pairs in both equations of a system (AR.4.1); read one, none or infinitely many solutions from a graph (AR.4.2).",
        must_not="Slope or y-intercept by name (Unit 10); substitution or elimination (Algebra 1); a student drawing a line (11.07).",
        read_first=[
            "Two book lessons in one period (11.5 and 11.6). Built from the benchmarks and the B1G-M first (the unit's Lesson Outlines, §11.05–06), then read against Math Nation (the unit audit, Part 2, §3–§5). The title slide names AR.4.1; AR.4.2 is taught the same day.",
            "The class has never graphed y = mx + b: Notes I is the first line it sees, made from a table (x = 0 and two more; the third point is the check). Every system is given solved for y. Today reads pictures: parallel is 'never meet', and the reasons from the equations (the same coefficient of x; ½ and 0.5 one number; setting the two expressions equal) are 11.07's. You may say slope here, the slides do not. If the room is slow, run Example 1, its Your Turn and boards 1–2 straight after Notes II, before Notes III: the class does something with a system before the three cases arrive.",
            "A failed check is written as a true computation with its verdict — '3(2) − 2 = 4, not 5' — never as a false equation (audit E10, E11) and never with ≠ as a line of work. The Your Turn of Example 2 carries its two tables in rows (a Your Turn slide carries no figure): always 4 apart, so never meet — the same reading as Example 2's worked slide.",
            "Not reproduced: the off-unit warm-up, the partner exploration, the algebraic solves of 11.5.2–11.5.3 (§3), Bevan's −7/2 slip (E3), the end labels off the grid (E13), the definition of a system that its own examples break (E17). The audit's §4 gaps are here: a select-all that never says how many (set 3, bank 12), and a same-line point off the grid (board 6's (10, 9))."],
        standard_notes=[("Clarification", "AR.4.1: a solution satisfies both equations at once (Clarification 1). AR.4.2: one, none or infinitely many, read from two lines on one plane; its named misconception is the same-line case read as anything but infinitely many (B1G-M)."),
                        ("Unit boundary", "Slope-intercept form only (AR.4.3's boundary, kept from today), a level line y = 4 included; every graph is read, none is drawn by a student (standing decision 9); whole-number crossings on the grid lines.")],
        sits="The unit's first systems day, after four days of AR.2.1. IXL's N46, AGZ and 9Z8 are due by the Unit 11 test (Fri 11 Dec), whose questions 8–11 are today's: a select-all of the systems a pair solves, a pair with its reason, and two graphs to count.",
        lives="Notes II — both equations, one is not enough — and Notes III's three pictures. Board 4 is the pair diagnostic (one equation only, the other only, swapped); board 6 the same-line diagnostic; board 9 the one-equation check in writing.",
        materials="Whiteboards and markers. The Independent Set, one per student (its graphs are to read, not to draw on).",
        variation="Boards 1–2 test a pair, true in both and then false in one; 3 reads a crossing from a graph and checks it, with the grid's height as the extra number; 4 votes on four pairs. The pattern breaks at 5 — parallel, no crossing to read — and 6 votes on the same line (its graph on the reveal); 7 is a level line, y = 4, crossing a slanted one once; 8 runs backwards; 9 is written. The independent set: a solution, a pair that fails one equation, a select-all of the systems a pair solves (two of five, the count unsaid), then three graphs — parallel, crossing, the same line.",
        audit=["Every pair re-derived by sympy at build time in both equations of its system, over the real numbers; every crossing solved as a system; every parallel pair checked to have no common point and every same-line pair to be one expression; every graph drawn from its equations by u11/figs.py, which refuses a stated crossing that is not on both lines.",
               "Math Nation 11.5–11.6 read against this lesson (A7 Unit 11 Audit, Part 2, E3, E10, E11, E13, E17, E18, §3–§5): their sound shapes — candidate tables, three graphed systems, an error analysis — are here with our own numbers; the defects are not reproduced."],
        changes=["11.5.1 scientific-notation warm-up → four retrieval questions, the prerequisite (evaluate y for an x) last.",
                 "11.5.2 partner exploration and its algebraic solve → Notes I–II from the front: a line from a table, then a pair tested in both equations.",
                 "11.5.3 and 11.6.1 (parallel and same-line systems, matching) → Notes III's three pictures, Example 2 and boards 5–7.",
                 "11.6.2–11.6.5 (candidate tables, Bevan's error) → Example 1, boards 1, 2, 4 and the written board 9, with new numbers."],
    ),
)
