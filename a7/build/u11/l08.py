# A7 11.08  Systems in Context; Approximate Solutions — MA.8.AR.4.3 (MN 11.8). Thu 10 Dec 2026, a 53-minute
# period, the last lesson before the unit test (Fri 11 Dec). There is no review day (ruling 27a): the Unit Review
# goes home today, and the Teacher Edition says so; no slide does.
# Two things are new. (1) A story is a system: each quantity is (the amount per 1)·x + (the start); the axes carry
# the story's names and a scale, and the crossing is said in the story's words with its units. (2) A crossing that
# falls between the grid lines is APPROXIMATED (AR.4.3 Clar. 1, standing decision 7): read to the nearest half or
# tenth, written with "about", and checked by putting the estimate into both equations — the two values come out
# close, not equal. Every line is still graphed from a table (decision 1); "slope" and "y-intercept" are on no
# student surface (decision 2); no substitution or elimination (decision 3); every crossing is checked in both
# equations (decision 6); the boards READ a graph and the Independent Set is where a student draws (decision 9).
# Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §11.08), then read against Math Nation
# 11.8 (the unit audit, Part 2). Not reproduced: plans billed at 2.5 months (E7 — every monthly or per-game story
# here crosses at a whole number), a line drawn past where its story ends (E8), the half-unit read stated as exact
# (E12), a y-axis named for one line only (E14 — each y-axis here names what BOTH lines measure), and the
# approximate item keyed to an exact pair (E15 — an approximate item here keys "about" a read and its check holds
# the read within a stated tolerance of the exact crossing, which sympy also derives).
#
# Every check is sympy over the REAL numbers: a crossing is the system's one solution (crosses), parallel lines
# have no common point (never_meet), a pair is put into each equation (sat / fails), and an estimate is held
# within a tolerance of the exact crossing (near).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs11 as figs          # its own name: every unit's gates run in one process, and a second module called figs would be Unit 6's
S = figs.slide

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
    """The system y = r1, y = r2 HAS a solution — a select-all's 'never the same' option is wrong."""
    return ("true", "sp.solve([sp.Eq(" + Y + ", " + _u(r1) + "), sp.Eq(" + Y + ", " + _u(r2) + ")], [" + X + ", " + Y
            + "], dict=True) != []")


def table_of(rhs, xs, ys):
    """Each y of a printed table is rhs at its x."""
    return ("many",) + tuple(sat(rhs, str(a), str(b)) for a, b in zip(xs, ys))


def near(exact, est, tol="0.05"):
    """The keyed estimate is within tol of the exact coordinate (AR.4.3 Clar. 1; audit E15). A keyed read is a
    tenth: within 0.05 of the exact value. The key accepts a read within 0.1 of the keyed tenth (one policy for
    the unit, fast 15 / critic 1, 15 Nov)."""
    return ("approx", exact, est, tol)


def no_grid_point(kx, ky, xs="1", ys="1"):
    """The accepted box — x within 0.1 of kx, y within 0.1 of ky — holds no printed grid intersection (grid lines
    every xs across and ys up): a nearest-grid-point read, which lies on one line at most, is never accepted."""
    lo_x, hi_x = "(" + kx + " - F(1,10))", "(" + kx + " + F(1,10))"
    lo_y, hi_y = "(" + ky + " - F(1,10))", "(" + ky + " + F(1,10))"
    has_x = "(sp.floor(" + hi_x + "/(" + xs + "))*(" + xs + ") >= " + lo_x + ")"
    has_y = "(sp.floor(" + hi_y + "/(" + ys + "))*(" + ys + ") >= " + lo_y + ")"
    return ("true", "not (" + has_x + " and " + has_y + ")")


def estimate(r1, r2, x, y, ex, ey):
    """The exact crossing (x, y) of y = r1 and y = r2, the keyed read (ex, ey) within 0.05 of it, and the read
    NOT on both lines (it is an estimate: the two values in the check come out close, not equal)."""
    off = ("true", "sp.simplify((" + _u(r1) + ").subs(" + X + ", " + ex + ") - (" + ey + ")) != 0 or "
           "sp.simplify((" + _u(r2) + ").subs(" + X + ", " + ex + ") - (" + ey + ")) != 0")
    return ("many", crosses(r1, r2, x, y), near(x, ex), near(y, ey), off, no_grid_point(ex, ey))


# ---- the board figures: 11.07's sizes (the largest a board allows): one bold row over the figure, a window no
# bigger than the system needs, slide(inches=4.2, pt=18, reserve=0.75). A story board carries two or three rows of
# words, so its figure is set as 11.07's candles were (inches=5.0, pt=16). 15 Nov: the kit sets a choice board's options
# beside its figure, so board 4's estimate is multiple choice again (barton 16) at full height, and the round's
# diagnostics are board 4 and board 6 (a system from a story, no graph); board 2 is free response with its graph.
def B(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.75)


def BA(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.95)


def BM(spec, reserve=0.75):
    return S(spec, inches=4.2, pt=14, reserve=reserve)


def BA2(spec):
    """The reveal of a two-row story board: the room its red answer needs under two rows of words."""
    return S(spec, inches=4.2, pt=18, reserve=1.3)


def ST(spec):
    return S(spec, inches=5.0, pt=16, reserve=0.75)


def STA(spec):
    return S(spec, inches=5.0, pt=16, reserve=1.1)


F3 = (Fr(5, 3), Fr(7, 3))           # Notes III: y = 2x − 1 and y = −x + 4

# ---- the notes and examples
NOTES1 = S(figs.table([([0, 1, 2], [10, 12, 14]), ([0, 1, 2], [0, 4, 8])],
                      titles=["pass:  y = 2x + 10", "no pass:  y = 4x"]), inches=7.0, pt=18, reserve=1.3)
NOTES2 = S(figs.plane((0, 8), (0, 32), lines=[(2, 10, "pass: y = 2x + 10"), (4, 0, "no pass: y = 4x")], ys=4,
                      xname="rides", yname="cost (dollars)", solution=(5, 20), points=[(5, 20, None, "ul")]),
           inches=4.6, pt=16, reserve=1.0)
NOTES3 = S(figs.plane((-1, 5), (-2, 5), lines=[(2, -1), (-1, 4)], solution=F3,
                      points=[(F3[0], F3[1], "about (1.7, 2.3)", "r")]),
           inches=4.4, pt=16, reserve=1.0)
# The Examples' question slides (barton 24, 15 Nov): an empty grid with the story's axes (Example 1), and the two
# tables with an empty grid (Example 2) — the teacher draws while the class watches; the worked slide gives the
# equations, the crossing and its check. Example 2 is liters now, not pages (critic 11: half a page is strained).
EX1 = S(figs.plane((0, 14), (0, 100), xs=2, ys=10, xname="minutes", yname="water (liters)", step=2),
        inches=4.6, pt=16, reserve=0.9)
EX2 = S(figs.row([figs.table([([0, 1, 2, 3], [0, 3, 6, 9]), ([0, 1, 2, 3], [5, 6, 7, 8])], titles=["Tub A", "Tub B"], cw=1.0),
                  figs.plane((0, 4), (0, 12), ys=3, xname="minutes", yname="water (liters)")],
                 gap=1.4), inches=11.4, pt=16, reserve=0.8)

# The worked slides (15 Nov: a worked entry carries `fig`): the finished graph beside the rows, the crossing marked.
EX1W = S(figs.plane((0, 14), (0, 100), lines=[(5, 30, "A"), (2, 60, "B")], xs=2, ys=10, xname="minutes",
                    yname="water (liters)", step=2, solution=(10, 80), points=[(10, 80, None, "ul")]),
         inches=4.6, pt=16, reserve=1.3)
EX2W = S(figs.plane((0, 4), (0, 12), lines=[(3, 0, "A"), (1, 5, "B")], ys=3, xname="minutes", yname="water (liters)",
                    solution=(Fr(5, 2), Fr(15, 2)), points=[(Fr(5, 2), Fr(15, 2), "(2.5, 7.5)", "ul")]),
         inches=4.6, pt=16, reserve=1.3)
# The Your Turns (critic 3 / barton 1, 15 Nov: a Your Turn carries `fig` and `fig_a`): each question slide shows what
# its Example's does — an empty grid (1); two tables beside an empty grid (2) — and the answer slide the finished graph.
# Your Turn 1 is Example 1's kind: its question slide is the story's empty grid (a table at 0, 2, 4 and 6 weeks, or
# the two equations, is the student's own work, as Example 1 modeled it)
YT1 = S(figs.plane((0, 10), (0, 140), ys=20, step=2, xname="weeks", yname="dollars"), inches=4.6, pt=16, reserve=0.9)
YT1A = S(figs.plane((0, 10), (0, 140), lines=[(10, 40, "Mia"), (5, 70, "Noah")], ys=20, step=2, xname="weeks",
                    yname="dollars", solution=(6, 100), points=[(6, 100, None, "ul")]), inches=4.6, pt=16, reserve=0.9)
YT2_T = figs.table([([0, 1, 2], [0, 4, 8]), ([0, 1, 2], [3, 5, 7])], titles=["y = 4x", "y = 2x + 3"], cw=2.0, rh=1.6)
YT2 = S(figs.row([YT2_T, figs.plane((0, 3), (0, 9))], gap=1.8), inches=6.4, pt=15, reserve=0.9)
YT2A = S(figs.plane((0, 3), (0, 9), lines=[(4, 0), (2, 3)], solution=(Fr(3, 2), 6),
                    points=[(Fr(3, 2), 6, "(1.5, 6)", "dr+")]), inches=4.6, pt=16, reserve=0.9)

# ---- the boards
P1 = figs.plane((0, 6), (0, 30), lines=[(3, 6, "A"), (5, 0, "B")], ys=5,
                xname="games", yname="cost (dollars)", solution=(3, 15))
P1A = figs.plane((0, 6), (0, 30), lines=[(3, 6, "A"), (5, 0, "B")], ys=5,
                 xname="games", yname="cost (dollars)", solution=(3, 15), points=[(3, 15, "")])
P2 = figs.plane((0, 8), (0, 60), lines=[(6, 6, "A"), (3, 18, "B")], ys=10,
                xname="miles", yname="cost (dollars)", solution=(4, 30))
P2A = figs.plane((0, 8), (0, 60), lines=[(6, 6, "A"), (3, 18, "B")], ys=10,
                 xname="miles", yname="cost (dollars)", solution=(4, 30), points=[(4, 30, "")])
P3 = figs.plane((0, 3), (0, 5), lines=[(1, 0, ""), (-2, 5, "")], solution=(Fr(5, 3), Fr(5, 3)))
# board 3 at one row of words: its equations are the lines' labels (14 Nov), so the plane takes the room a second row had
P3L = figs.plane((0, 3), (0, 5), lines=[(1, 0), (-2, 5)], solution=(Fr(5, 3), Fr(5, 3)))
P4 = figs.plane((0, 3), (0, 5), lines=[(2, 1, ""), (-1, 5, "")], solution=(Fr(4, 3), Fr(11, 3)))
# the reveal keeps the question's window and marks the crossing (critic 16)
P4A = figs.plane((0, 3), (0, 5), lines=[(2, 1, ""), (-1, 5, "")], solution=(Fr(4, 3), Fr(11, 3)),
                 points=[(Fr(4, 3), Fr(11, 3), "")])
P5 = figs.plane((0, 8), (0, 48), lines=[(3, 12, "A"), (6, 0, "B")], ys=6,
                xname="hours", yname="cost (dollars)", solution=(4, 24), step=2)
P5A = figs.plane((0, 8), (0, 48), lines=[(3, 12, "A"), (6, 0, "B")], ys=6,
                 xname="hours", yname="cost (dollars)", solution=(4, 24), step=2,
                 points=[(7, 33, ""), (7, 42, "")])
P7 = figs.plane((0, 16), (0, 80), lines=[(4, 10, "sunflower"), (2, 30, "bean")], xs=2, ys=10,
                xname="weeks", yname="height (cm)", solution=(10, 50), step=2)
P7A = figs.plane((0, 16), (0, 80), lines=[(4, 10, "sunflower"), (2, 30, "bean")], xs=2, ys=10,
                 xname="weeks", yname="height (cm)", solution=(10, 50), step=2, points=[(10, 50, "")])
# board 9 (barton 20): the written exit board is an estimate and its check — the skill the test's 14(b) asks
P9 = figs.plane((0, 3), (0, 6), lines=[(1, 3, ""), (-2, 5, "")], solution=(Fr(2, 3), Fr(11, 3)))
P9A = figs.plane((0, 3), (0, 6), lines=[(1, 3, ""), (-2, 5, "")], solution=(Fr(2, 3), Fr(11, 3)),
                 points=[(Fr(2, 3), Fr(11, 3), "")])


# ---- the Independent Set and the banks: an empty grid for each system a student graphs (decision 9). A grid is
# the window its key's graph is drawn on (audit E13).
def GRID(xr, yr, **k):
    return figs.plane(xr, yr, inches=3.2, **k)


def KEY(xr, yr, lines, solution=None, name=None, where=None, **k):
    """The key's own figure (fig_key, 15 Nov — critic 2): the student's grid with both lines drawn from their equations
    and the crossing marked and named (an estimate: the exact lines, the point, "about (…)"); `plane` refuses a
    crossing that is not on both lines."""
    pts = [(solution[0], solution[1], name) + ((where,) if where else ())] if solution else []
    return figs.plane(xr, yr, lines=lines, solution=solution, points=pts, inches=3.2, **k)


L = dict(
    code="11.08", unit=11, lesson_no=8,
    align="=",   # every run of rows that solve an equation set with its equals signs in one column (kit, 15 Nov 2026)
    title="Systems in Context; Approximate Solutions",
    unit_title="Solving Equations and Systems",
    benchmark="MA.8.AR.4.3",
    benchmark_text="Given a mathematical or real-world context, solve systems of two linear equations by graphing.",
    target="I can solve a real-world system by graphing, explain what the crossing point means, and estimate a crossing that falls between the grid lines.",
    yesterday="Last class: we graphed both lines from tables and read where they cross.",
    today="Today: the lines come from stories, and some crossings fall between the grid lines.",
    essential="What does the point where two lines cross tell you about the two things in a story?",
    building_on="Lesson 11.07 solved a system by graphing each line from a table of values. Lessons 11.05–06 showed that a solution of a system makes both equations true. Lesson 11.02 solved equations of the form mx + b = nx + c for two plans that cost the same.",
    working_toward="Question 14 of the Unit 11 test (Friday 11 December) has a story with its graph and a point of intersection between the grid lines. In Unit 10 (January), the amount per 1 is named the slope and the starting amount the y-intercept. In Algebra 1 (MA.912.AR.9.1), students find exact solutions by substitution and elimination.",
    vocab=[("approximate solution", "a crossing read between the grid lines, written with \"about\": about $(1.7, 2.3)$")],
    vocab_note="One phrase. An estimate is a careful read, not a guess: nearest half or tenth, the word 'about', and a check in both equations that comes out close.",
    ixl=["Solve a system of equations by graphing: word problems — W9J"],
    title_note="The last lesson before Friday's test, and there is no review day: hand out the Unit Review at the IXL slide; it goes home tonight. Say so out loud — no slide does.",
    closure="Whiteboard question 9 is answered in writing and serves as the exit ticket. A complete answer gives an estimate of about (0.7, 3.7) for y = x + 3 and y = −2x + 5 and writes both checks, 0.7 + 3 = 3.7 and −2(0.7) + 5 = 3.6, which are close. An answer of (1, 4) is the nearest grid point, which is on one line only. An estimate with no check is only half complete.",

    mtr=[("MTR.5.1", "Students write each story as an equation with the same structure: the amount per 1, times x, plus the starting amount."),
         ("MTR.6.1", "Students check every estimate in both equations and expect the two values to be close, not equal."),
         ("MTR.7.1", "On whiteboard questions 1, 2, 5 and 7, students explain what the point of intersection means in the story, with its units.")],
    hoq=[("Your estimate gives 2.4 in one equation and 2.3 in the other. Why does that not mean your estimate is wrong?", "DOK 2"),
         ("Before the crossing one plan is cheaper; after it, the other. How does the graph show which is which?", "DOK 2"),
         ("Two savers add the same amount each week but start with different amounts. Why will they never be equal?", "DOK 3")],
    differentiation=[
        ("ESE / 504", "Provide a desk card that reads \"amount per 1 · x + start.\" For an estimate, provide a printed strip that divides the space between two grid lines into tenths, to lay along the point of intersection."),
        ("ELL", "**Per**: for every one. **Start**: the amount at x = 0. **About**: close, but not exact. **Costs less**: is cheaper."),
        ("Enrichment", "Students who finish whiteboard question 5 early change Shop A's starting charge so that the two shops cost the same at 7 hours. They solve 3(7) + s = 6(7) for s, so s = \\$21.")],

    warmup=[
        dict(stem="Use tables to solve the system  $y = x + 3$  and  $y = 2x$.", answer="(3, 6)", band="last lesson",
             source="11.07 — a crossing read from two tables: at x = 3 both give 6",
             check=("many", crosses("u + 3", "2*u", "3", "6"))),
        dict(stem="How many solutions does  $5x + 4 = 2x + 4$  have?", answer="One solution, x = 0", band="last week",
             source="11.03 — x = 0 is one solution: 3x = 0",
             check=("eq", "sp.solve(sp.Eq(5*" + X + " + 4, 2*" + X + " + 4), " + X + ")[0]", "0")),
        dict(stem="A 6-ft post casts a 4-ft shadow. A tree casts a 10-ft shadow. How tall is the tree?", answer="15 ft", band="last unit",
             source="6.07 — similar triangles: 6/4 = h/10",
             check=("eq", "F(6,4)*10", "15")),
        dict(stem="A gym costs \\$15 to join and \\$4 a visit. What do 5 visits cost?", answer="\\$35", band="the prerequisite this lesson needs",
             source="1.06–1.07 — a start plus an amount per one, from a story (Unit 1); every line today is one",
             check=("eq", "15 + 4*5", "35")),
    ],
    warmup_note="Q1 is yesterday in one line; Q4 is today's move — a start plus an amount for each one: 15 + 4(5). Every line today is (the amount per 1)·x + (the start). Two minutes silent, then reveal.",

    notes=[
        dict(numeral="I", head="A story is a system", min=4, sub="Copy both equations.",
             note="Each quantity is (the amount per 1)·x + (the start). The pass is \\$10 at the start and \\$2 for each ride: y = 2x + 10. With no pass there is no start: y = 4x. The tables come from the story too — at 0 rides the pass has already cost \\$10. You may say 'slope' here; the room says 'amount per 1'.\nOFF: 'What do you pay for each one? What do you pay before the first one? That is the equation.'",
             items=["Pass:  \\$10, then \\$2 a ride.     $y = 2x + 10$",
                    "No pass:  \\$4 a ride.     $y = 4x$"],
             fig=NOTES1,
             items2=["Each one:   (the amount per 1) · x  +  (the start)"],
             letters=False),
        dict(numeral="II", head="Explain what the point means, with units", min=3, sub="",
             note="The axes carry the story's names and a scale: rides across, cost in dollars up, one line every 4 dollars. The crossing (5, 20) is x = 5 rides and y = 20 dollars: at 5 rides both cost \\$20. Check: 2(5) + 10 = 20 and 4(5) = 20. Then read the picture on either side: left of the crossing the no-pass line is lower (fewer rides — pay per ride); right of it the pass line is lower (more rides — buy the pass).\nOFF: 'An answer is x and y in the story's words: 5 rides, 20 dollars.'",
             fig=NOTES2,
             items2=["At 5 rides, both cost \\$20.   Fewer rides: pay per ride.   More: buy the pass."],
             letters=False),
        dict(numeral="III", head="Between the grid lines: estimate", min=3, sub="",
             note="These lines cross between x = 1 and x = 2, a little past the middle, and a little above y = 2: about (1.7, 2.3). Read each coordinate to the nearest tenth and write 'about'. Check the estimate in both equations: 2(1.7) − 1 = 2.4 and −1.7 + 4 = 2.3 — close, not equal, which is what an estimate gives. The exact crossing is 5/3 and 7/3; nobody is asked for it (Algebra 1). A read within 0.1 of each — (1.6, 2.3), (1.7, 2.4) — is a good estimate; a grid point such as (2, 2) is on one line only, and is not.\nOFF: 'Between which grid lines? Nearer which one? Then about, and check: close is right.'",
             fig=NOTES3,
             items2=["Check:   $2(1.7) - 1 = 2.4$   and   $-1.7 + 4 = 2.3$.   Close: a good estimate."],
             letters=False),
    ],

    examples=[
        # barton 9: writing a system from a story is modeled here (Notes I, then this worked slide, a line each)
        # before board 6 asks for it
        dict(title="Example 1", sub="A story to a system; the crossing in words.", min_q=2,
             note_q="The grid is empty on purpose. Ask for each tank's start and amount per minute before anyone writes an equation; write the two equations, a line each. Read the axes' names and scale aloud: minutes across, every 2; liters up, every 10. Then plot each tank at 0 and 6 minutes and draw the two lines on the projected grid; ask the room where they cross.",
             prompt=["Tank A holds 30 liters and gains 5 liters a minute.", "Tank B holds 60 liters and gains 2 liters a minute."],
             fig=EX1, ask="When do the tanks hold the same amount, and how much is that?",
             worked=[dict(sub="Worked.", min=1,
                          note="Tank A: start 30, 5 per minute, y = 5x + 30. Tank B: y = 2x + 60. The lines cross at (10, 80): x = 10 minutes, y = 80 liters. Check: 5(10) + 30 = 80 and 2(10) + 60 = 80. Say it in the story's words. A board with 'after 80 minutes' swapped the coordinates.",
                          rows=[("\\mathrm{A}:\\ y = 5x + 30", "start 30, 5 per minute"),
                                ("\\mathrm{B}:\\ y = 2x + 60", "start 60, 2 per minute"),
                                ("5(10) + 30 = 80", "A at 10 minutes"),
                                ("2(10) + 60 = 80", "B at 10 minutes: the crossing (10, 80)")],
                          fig=EX1W, answer="After 10 minutes, both hold 80 liters.")],
             check=("many", crosses("5*u + 30", "2*u + 60", "10", "80"), sat("5*u + 30", "10", "80"), sat("2*u + 60", "10", "80")),
             # the Your Turn shows the story's empty grid, as Example 1's question slide does, and its answer slide the
             # graph (15 Nov: a Your Turn carries a figure); the crossing is at 6 weeks (critic 3d: the old one needed 12)
             your_turn=dict(min=2, note="The tables: Mia has 40, 60, 80, 100 and Noah 70, 80, 90, 100 at 0, 2, 4, 6 weeks — both 100 at 6 weeks. As a system, Mia y = 10x + 40 and Noah y = 5x + 70: 10(6) + 40 = 100 and 5(6) + 70 = 100. A board with 'after 100 weeks' swapped; one with 'after 4 weeks' took the column where Mia is closest before she catches up (80 against 90).",
                            prompt=["Mia has \\$40 and saves \\$10 a week. Noah has \\$70 and saves \\$5 a week."],
                            fig=YT1, fig_a=YT1A,
                            ask="When will they have the same amount, and how much is that?",
                            steps=["Mia:  $10(6) + 40 = 100$     Noah:  $5(6) + 70 = 100$"],
                            gloss="the crossing, in weeks and dollars", answer="After 6 weeks, both have \\$100."),
             yt_check=("many", crosses("10*u + 40", "5*u + 70", "6", "100"), table_of("10*u + 40", [0, 2, 4, 6], [40, 60, 80, 100]),
                       table_of("5*u + 70", [0, 2, 4, 6], [70, 80, 90, 100]))),
        dict(title="Example 2", sub="A crossing halfway between grid lines.", min_q=2,
             note_q="Read the two tables first: at 2 minutes Tub A is behind (6 against 7), at 3 minutes ahead (9 against 8) — so they are equal somewhere between. Draw both lines on the projected grid from the tables, then ask where they cross: between which two x's? Between which two y's? Halfway, both ways.",
             prompt=["Tub A is empty and gains 3 liters a minute.", "Tub B holds 5 liters and gains 1 liter a minute."],
             fig=EX2, ask="When do the tubs hold the same amount?",
             worked=[dict(sub="Worked.", min=1,
                          note="A: y = 3x. B: y = x + 5. The lines cross halfway between x = 2 and x = 3 and halfway between the grid lines y = 6 and y = 9 (one line every 3 liters): (2.5, 7.5). This read lands exactly: 3(2.5) = 7.5 and 2.5 + 5 = 7.5. In the story: after 2.5 minutes both tubs hold 7.5 liters. A board with (2, 6) or (3, 9) took a nearby grid point; check it — (2, 6) is on A only: 2 + 5 = 7, not 6.",
                          rows=[("\\mathrm{A}:\\ y = 3x", "no start, 3 per minute"),
                                ("\\mathrm{B}:\\ y = x + 5", "start 5, 1 per minute"),
                                ("3(2.5) = 7.5", "A, halfway between 2 and 3"),
                                ("2.5 + 5 = 7.5", "B: the same, so (2.5, 7.5)")],
                          fig=EX2W, answer="After 2.5 minutes, both hold 7.5 liters.")],
             check=("many", crosses("3*u", "u + 5", "F(5,2)", "F(15,2)"), sat("3*u", "F(5,2)", "F(15,2)"), sat("u + 5", "F(5,2)", "F(15,2)"),
                    table_of("3*u", [0, 1, 2, 3], [0, 3, 6, 9]), table_of("u + 5", [0, 1, 2, 3], [5, 6, 7, 8])),
             your_turn=dict(min=2, note="Tables at x = 0, 1, 2: 4x gives 0, 4, 8 and 2x + 3 gives 3, 5, 7. At x = 1 the first is lower, at x = 2 higher: they change places between, and halfway works — (1.5, 6). Check: 4(1.5) = 6 and 2(1.5) + 3 = 6. A board with (6, 1.5) swapped; one with (2, 8) took the grid point on one line only.",
                            prompt=["Solve the system  $y = 4x$  and  $y = 2x + 3$."], fig=YT2, fig_a=YT2A, ask="",
                            steps=["halfway from 1 to 2:   $4(1.5) = 6$   and   $2(1.5) + 3 = 6$"],
                            gloss="a half, checked in both", answer="(1.5, 6)"),
             yt_check=("many", crosses("4*u", "2*u + 3", "F(3,2)", "6"), table_of("4*u", [0, 1, 2], [0, 4, 8]),
                       table_of("2*u + 3", [0, 1, 2], [3, 5, 7]))),
    ],

    # The round: a story's crossing read with its units (1) and a crossing's meaning (2); then the estimates —
    # which two whole numbers (3) and the diagnostic on the four reads a graph offers (4); the pattern changes at
    # 5 — not the crossing but the cheaper side of it; 6 votes on the system a story makes; 7 is the plants with
    # their price as the extra number; 8 runs backwards from the crossing; 9 is written: which plan, and why.
    whiteboard=[
        dict(text=["Plan A costs \\$6 for shoes and \\$3 a game. Plan B costs \\$5 a game.",
                   "**After how many games do the plans cost the same?"],
             fig=B(P1), fig_a=BA2(P1A),
             steps=["the lines cross at $(3, 15)$", "A:  $3(3) + 6 = 15$     B:  $5(3) = 15$"],
             gloss="x = 3 games, y = 15 dollars", answer="After 3 games, both cost \\$15.",
             note="Read the crossing on the grid: x = 3 games, y = \\$15 (one line every \\$5). Check: 3(3) + 6 = 15 and 5(3) = 15. A board with '15 games' swapped the coordinates; one with '6 games' took the \\$6 for shoes as the answer.",
             check=("many", crosses("3*u + 6", "5*u", "3", "15"), sat("3*u + 6", "3", "15"), sat("5*u", "3", "15")),
             wrong="15 games — x and y swapped [B1G-M, GR.1.2: x and y inverted]; 6 games — the \\$6 for shoes taken as the answer [B1G-M, AR.3.5: misinterpreting in context]"),
        # repeat_ok: rule D matches only the digits 30 and 4 (Example 1's tank starts at 30 liters, and a 4 is in its
        # working); this point, (4, 30), and its taxi system appear nowhere above. Flagged once its graph moved to
        # the reveal (14 Nov), when the question slide stopped carrying a figure.
        # free response (15 Nov): the round's vote is board 4's again, with its graph beside its options (barton 16);
        # this board's graph is on its question slide, and the three misreadings are its wrong list
        dict(repeat_ok=True, text=["Taxis A and B cost y dollars for x miles. Their lines cross at $(4, 30)$.",
                                   "**What does that point mean?"],
             qtext="Taxis A and B cost y dollars for a ride of x miles. Their graphs cross at (4, 30). What does that point mean?",
             fig=B(P2), fig_a=BA2(P2A),
             steps=["x is miles:  4", "y is dollars:  30,  on both lines"],
             gloss="x = 4 miles, y = 30 dollars", answer="For a 4-mile ride, both taxis cost \\$30.",
             wrong="'for a 30-mile ride, both cost \\$4' — x and y swapped [B1G-M, GR.1.2: x and y inverted]; 'Taxi A costs \\$30' — the point read on one line only [B1G-M, AR.4.1: a solution satisfies both]; 'they always cost the same' — one crossing read as the same line [B1G-M, AR.4.2: the same-line case]",
             note="The meaning of a crossing. A point's meaning is its x and its y in the story's words: x = 4 miles, y = \\$30 — for a 4-mile ride both taxis cost \\$30. (Taxi A is y = 6x + 6 and Taxi B is y = 3x + 18: 6(4) + 6 = 30 and 3(4) + 18 = 30.) A board with 'for a 30-mile ride' swapped; one that names Taxi A only gives the point to one taxi; one with 'always the same' reads one crossing as the same line — at 1 mile Taxi A costs \\$12 and Taxi B \\$21.",
             check=("many", crosses("6*u + 6", "3*u + 18", "4", "30"), sat("6*u + 6", "4", "30"), sat("3*u + 18", "4", "30"),
                    fails("6*u + 6", "30", "4"), fails("3*u + 18", "30", "4"),
                    ("true", "sp.expand((" + _u("6*u + 6") + ") - (" + _u("3*u + 18") + ")) != 0"),
                    sat("6*u + 6", "1", "12"), sat("3*u + 18", "1", "21"))),
        # repeat_ok: with its equations moved onto the lines (14 Nov), rule D matches only the grid's axis numbers
        # (0 to 5) and the answer's digits; this system (y = x, y = −2x + 5) appears nowhere above.
        dict(repeat_ok=True, text=["**Between which two whole numbers is the crossing's x-value?"],
             fig=B(P3L), fig_a=BA(P3L),
             steps=["$x = 1$:   $1$ and $-2(1) + 5 = 3$", "$x = 2$:   $2$ and $-2(2) + 5 = 1$"],
             gloss="the lines change places between 1 and 2", answer="1 and 2",
             note="The crossing is between the grid lines, so the question is only where: between x = 1 and x = 2. The tables say so without a graph — at x = 1 the second line is higher, at x = 2 the first is: they changed places in between. A board with 'between 1 and 2 for y' answered for y (y is also between 1 and 2 here — read the x); one with '2' took the nearest grid line.",
             check=("many", crosses("u", "-2*u + 5", "F(5,3)", "F(5,3)"), ("true", "1 < F(5,3) < 2"),
                    sat("-2*u + 5", "1", "3"), sat("-2*u + 5", "2", "1")),
             wrong="'2' — the nearest grid line taken as the crossing [B1G-M, AR.4.3: plotting and graphing errors]; '0 and 5' — where each line meets the y-axis [B1G-M, AR.4.1: a solution satisfies both]"),
        # board 4 (barton 16, 15 Nov): multiple choice again, as the outline had it — the kit sets a choice board's
        # options beside its figure, so the estimate is read at full height and each wrong option is a named error
        dict(kind="mc", text=["**$y = 2x + 1$  and  $y = -x + 5$  are graphed. Which estimate is best?"],
             qtext="y = 2x + 1 and y = −x + 5 are graphed. Which is the best estimate of the solution?",
             fig=B(P4), fig_a=BA(P4A),
             steps=["between $x = 1$ and $x = 2$, nearer 1:  about $(1.3, 3.7)$",
                    "$2(1.3) + 1 = 3.6$   and   $-1.3 + 5 = 3.7$:  close"],
             choices=["$(1, 3)$", "$(3.7, 1.3)$", "$(0, 5)$", "$(1.3, 3.7)$"], correct=3, answer="D — about (1.3, 3.7)",
             errors={"A": "the nearest grid point, on y = 2x + 1 only: −1 + 5 = 4, not 3 [B1G-M, AR.4.3: plotting and graphing errors]", "B": "the coordinates of the estimate swapped [B1G-M, GR.1.2: x and y inverted]", "C": "where y = −x + 5 starts, on one line only [B1G-M, AR.4.1: a solution satisfies both]"},
             note="Diagnostic on the estimate, read at full size. The keyed read is about (1.3, 3.7); the exact crossing is (4/3, 11/3), and a read within 0.1 of each — (1.3, 3.6), (1.4, 3.7) — is a good estimate. Check (1.3, 3.7) in both aloud: 3.6 and 3.7, close. A vote for (3.7, 1.3) swapped it; one for (1, 3) took the nearest grid point, which is on one line only; one for (0, 5) read where a line starts. On a split: sixty seconds, convince your neighbor, re-vote.",
             check=("many", estimate("2*u + 1", "-u + 5", "F(4,3)", "F(11,3)", "1.3", "3.7"),
                    fails("2*u + 1", "3.7", "1.3"), fails("-u + 5", "3.7", "1.3"),
                    sat("2*u + 1", "1", "3"), fails("-u + 5", "1", "3"),
                    sat("-u + 5", "0", "5"), fails("2*u + 1", "0", "5"))),
        dict(text=["Shop A charges \\$12 plus \\$3 an hour. Shop B charges \\$6 an hour.",
                   "**Which bike shop costs less for 7 hours?"],
             fig=S(P5, inches=4.2, pt=18, reserve=0.95), fig_a=BA2(P5A),
             steps=["they cross at $(4, 24)$", "A:  $3(7) + 12 = 33$", "B:  $6(7) = 42$"],
             gloss="past the crossing, the other side wins", answer="Shop A (\\$33 versus \\$42)",
             note="The pattern changes: the crossing is not the answer, it is the dividing line. Before 4 hours Shop B is cheaper; after 4 hours Shop A is. At 7 hours: 3(7) + 12 = 33 and 6(7) = 42. A board with Shop B decided by the smaller start, or by the \\$6 being less than \\$12.",
             check=("many", crosses("3*u + 12", "6*u", "4", "24"), sat("3*u + 12", "7", "33"), sat("6*u", "7", "42"), ("true", "33 < 42")),
             wrong="Shop B — 'it has no start fee', true only before 4 hours [B1G-M, AR.3.5: misinterpreting in context]; 4 hours — the crossing given instead of the shop [B1G-M, AR.3.5: misinterpreting in context]"),
        dict(kind="mc", text=["Gym A costs \\$20 to join and \\$10 a month.", "Gym B costs \\$15 a month.",
                              "**Which system gives each gym's cost y for x months?"],
             qtext="Gym A costs \\$20 to join and \\$10 a month. Gym B costs \\$15 a month. Which system gives each gym's cost y for x months?",
             steps=["A:  \\$10 a month, \\$20 once:   $y = 10x + 20$", "B:  \\$15 a month, nothing to join:   $y = 15x$"],
             choices=["y = 10x + 20 and y = x + 15", "y = 30x and y = 15x", "y = 20x + 10 and y = 15x", "y = 10x + 20 and y = 15x"],
             correct=3, answer="D — y = 10x + 20 and y = 15x",
             errors={"A": "Gym B's \\$15 a month taken as a start [B1G-M, AR.3.5: misinterpreting in context]", "B": "the join fee added to the monthly amount [B1G-M, AR.3.5: misinterpreting in context]", "C": "the join fee and the monthly amount swapped [B1G-M, AR.3.3: which value is which]"},
             note="Diagnostic on writing the system: the amount per month multiplies x, and the one-time fee is the start. Test each option at 2 months — Gym A has cost \\$40 and Gym B \\$30: option C gives 50, option A gives 17 for Gym B, option B gives 60.",
             check=("many", sat("10*u + 20", "2", "40"), sat("15*u", "2", "30"),
                    fails("20*u + 10", "2", "40"), fails("u + 15", "2", "30"), fails("30*u", "2", "40"))),
        dict(text=["Two plants cost \\$8 in all. The graph shows their heights.",
                   "**When are the two plants the same height?"],
             unneeded="8",
             fig=B(P7), fig_a=BA2(P7A),
             steps=["the lines cross at $(10, 50)$", "x is weeks:  10;   y is height:  50 cm"],
             gloss="x = 10 weeks, y = 50 cm", answer="After 10 weeks, both are 50 cm tall.",
             note="The extra-number board (ruling 22): the \\$8 is not needed. The crossing is (10, 50): after 10 weeks both plants are 50 cm tall. (The sunflower is y = 4x + 10 and the bean y = 2x + 30: 4(10) + 10 = 50 and 2(10) + 30 = 50.) A board with 'after 8 weeks' used the price; one with 'after 50 weeks' swapped.",
             check=("many", crosses("4*u + 10", "2*u + 30", "10", "50"), sat("4*u + 10", "10", "50"), sat("2*u + 30", "10", "50")),
             wrong="'after 8 weeks' — the plants' price taken as the time [an extra number, included on purpose]; 'after 50 weeks' — x and y swapped [B1G-M, GR.1.2: x and y inverted]"),
        dict(text=["Two plans cost the same for 6 months:", "$y = 8x + 30$   and   $y = □x$", "**What number goes in the box?"],
             steps=["$8(6) + 30 = 78$", "$78 \\div 6 = 13$"],
             gloss="both cost 78 at x = 6", answer="13",
             note="Backwards: the crossing's x is given, and the second plan's amount per month is missing. The first plan costs 8(6) + 30 = 78 at 6 months, so □ · 6 = 78 and □ = 13. Check: 13(6) = 78. A board with 8 copied the first plan's amount; one with 5 did 30 ÷ 6.",
             check=("many", ("eq", "(8*6 + 30)/6", "13"), crosses("8*u + 30", "13*u", "6", "78")),
             wrong="8 — the first plan's amount copied [B1G-M, AR.4.1: substitution errors]; 5 — 30 ÷ 6, the start shared over the months [B1G-M, AR.4.1: substitution errors]"),
        # board 9 (barton 20, 15 Nov): the written exit board is an estimate and its check written out — the skill of
        # the test's 14(b), taught the day before it; the cheaper side of a crossing stays on board 5
        dict(kind="written", text=["$y = x + 3$  and  $y = -2x + 5$  are graphed.",
                                   "**Estimate the solution. Show that it is close in both equations."],
             qtext="y = x + 3 and y = −2x + 5 are graphed. Estimate the solution. Show that your estimate is close in both equations.",
             fig=B(P9), fig_a=BA2(P9A),
             steps=["between $x = 0$ and $x = 1$, nearer 1:  about $(0.7, 3.7)$",
                    "$-2(0.7) + 5 = 3.6$   and   $0.7 + 3 = 3.7$:  close"],
             gloss="an estimate, checked in both", answer="about (0.7, 3.7)",
             te_answer="Full credit: an estimate within 0.1 of (0.7, 3.7) — x from 0.6 to 0.8, y from 3.6 to 3.8 — AND both checks written, with the two values close: 0.7 + 3 = 3.7 and −2(0.7) + 5 = 3.6. (Exactly 2/3 and 11/3.) (1, 4), the nearest grid point, is on y = x + 3 only (−2 + 5 = 3) and earns none; an estimate with no check earns half.",
             note="Written, and the exit evidence: tomorrow's question 14(b). The lines cross between x = 0 and x = 1, nearer 1, a little below y = 4. Read two aloud — one whose two checks come out close, one that took (1, 4) and whose check shows it: 4 and 3, not close.",
             check=("many", estimate("u + 3", "-2*u + 5", "F(2,3)", "F(11,3)", "0.7", "3.7"),
                    sat("u + 3", "1", "4"), fails("-2*u + 5", "1", "4"),
                    ("eq", "0.7 + 3", "3.7"), ("eq", "-2*0.7 + 5", "3.6")),
             wrong="(1, 4) — the nearest grid point, on y = x + 3 only [B1G-M, AR.4.3: plotting and graphing errors]; (3.7, 0.7) — the coordinates swapped [B1G-M, GR.1.2: x and y inverted]"),
    ],

    # The six: a story's graph read (1), what a crossing means (2), an estimate on an empty grid (3), the system a
    # story makes (4), the cheaper side of a crossing on an empty grid (5), and two savers who add the same amount
    # each week — never equal (6).
    independent=[
        dict(stem="Pot A of water is 20°C and warms 6°C a minute. Pot B is 45°C and warms 1°C a minute. When are they the same temperature, and what is it?",
             fig=figs.plane((0, 8), (0, 70), lines=[(6, 20, "A: y = 6x + 20"), (1, 45, "B: y = x + 45")], ys=10,
                            xname="minutes", yname="temperature (°C)", solution=(5, 50), inches=3.2),
             answer="After 5 minutes, both are 50°C.",
             why="The lines cross at (5, 50): 6(5) + 20 = 50 and 5 + 45 = 50.",
             check=("many", crosses("6*u + 20", "u + 45", "5", "50")), space=0.3),
        dict(stem="Music lessons cost $y = 9x + 24$ dollars for x lessons with plan A and $y = 15x$ dollars with plan B. The graphs cross at $(4, 60)$. What does that point mean?",
             answer="For 4 lessons, both plans cost \\$60.",
             why="x = 4 lessons and y = \\$60: 9(4) + 24 = 60 and 15(4) = 60.",
             check=("many", crosses("9*u + 24", "15*u", "4", "60")), space=0.5),
        dict(stem="Graph both lines and estimate the solution:   $y = 2x - 2$   and   $y = -x + 2$",
             fig=GRID((-1, 4), (-3, 4)), fig_key=KEY((-1, 4), (-3, 4), [(2, -2), (-1, 2)], (Fr(4, 3), Fr(2, 3)), "about (1.3, 0.7)", "r"),
             answer="about (1.3, 0.7)",
             why="Tables at x = 0, 1, 2: y = −2, 0, 2 and y = 2, 1, 0. The lines cross between x = 1 and x = 2, nearer 1, a little above y = 0.5: about (1.3, 0.7). Check: 2(1.3) − 2 = 0.6 and −1.3 + 2 = 0.7 — close. Accept a read within 0.1 of each: x from 1.2 to 1.4, y from 0.6 to 0.8, such as (1.4, 0.6). (1, 1) and (2, 0) are grid points on one line only.",
             check=("many", estimate("2*u - 2", "-u + 2", "F(4,3)", "F(2,3)", "1.3", "0.7"),
                    near("F(4,3)", "1.4", "0.1"), near("F(2,3)", "0.6", "0.1"),
                    sat("-u + 2", "1", "1"), fails("2*u - 2", "1", "1"), sat("-u + 2", "2", "0"), fails("2*u - 2", "2", "0"),
                    table_of("2*u - 2", [0, 1, 2], [-2, 0, 2]), table_of("-u + 2", [0, 1, 2], [2, 1, 0])),
             space=0.3),
        dict(stem="Shop A sells shirts for \\$7 each plus \\$15 to ship. Shop B sells them for \\$12 each with free shipping. Write a system for the cost y of x shirts.",
             answer="y = 7x + 15  and  y = 12x",
             why="Shop A: \\$7 per shirt and a start of \\$15. Shop B: \\$12 per shirt and no start. (They cost the same at 3 shirts, \\$36.)",
             check=("many", sat("7*u + 15", "1", "22"), sat("12*u", "1", "12"), crosses("7*u + 15", "12*u", "3", "36")), space=0.5),
        dict(stem="Club A costs \\$12 to join and \\$2 a week. Club B costs \\$5 a week. Graph both. Which club costs less for 6 weeks?",
             fig=GRID((0, 8), (0, 40), ys=4, xname="weeks", yname="cost (dollars)"), fig_key=KEY((0, 8), (0, 40), [(2, 12, "Club A"), (5, 0, "Club B")], (4, 20), ys=4, xname="weeks", yname="cost (dollars)"),
             answer="Club A (\\$24 versus \\$30)",
             why="y = 2x + 12 and y = 5x cross at (4, 20). After 4 weeks Club A's line is lower: 2(6) + 12 = 24 and 5(6) = 30.",
             check=("many", crosses("2*u + 12", "5*u", "4", "20"), sat("2*u + 12", "6", "24"), sat("5*u", "6", "30")),
             space=0.3),
        dict(stem="Lia has \\$25 and saves \\$4 a week. Omar has \\$40 and saves \\$4 a week. Graph both. Will they ever have the same amount? Explain.",
             fig=GRID((0, 8), (0, 80), ys=5, xname="weeks", yname="savings (dollars)"), fig_key=KEY((0, 8), (0, 80), [(4, 25, "Lia"), (4, 40, "Omar")], ys=5, xname="weeks", yname="savings (dollars)"),
             answer="No. The lines are parallel, so there is no solution.",
             why="y = 4x + 25 and y = 4x + 40: both add \\$4 a week, so Omar always has \\$15 more. The lines are parallel and never meet.",
             check=("many", never_meet("4*u + 25", "4*u + 40"), ("eq", "(4*8 + 40) - (4*8 + 25)", "15")), space=0.3),
    ],

    # Bank: a story's graph read (1), a crossing's meaning (2), an estimate and a whole-number bracket off a graph
    # (3–4), the system a story makes (5), the cheaper side and an estimate on empty grids (6–7), backwards (8),
    # the estimate diagnostic and the write-a-system diagnostic (9–10), a select-all on a crossing's meaning (11),
    # and two savers at the same rate (12). The additional bank mirrors it position by position with new numbers.
    bank=[
        dict(heading="Use the graph."),
        dict(stem="Phone A has 100% charge and uses 10% an hour. Phone B has 80% and uses 5% an hour. When do the phones have the same charge, and what is it?",
             fig=figs.plane((0, 10), (0, 100), lines=[(-10, 100, "A", (2, "ur")), (-5, 80, "B", (8, "ur"))], ys=10,
                            xname="hours", yname="charge (%)", solution=(4, 60), inches=2.6),
             answer="After 4 hours, both have 60%.", why="The lines cross at (4, 60): −10(4) + 100 = 60 and −5(4) + 80 = 60.",
             check=("many", crosses("-10*u + 100", "-5*u + 80", "4", "60")), space=0.4),
        dict(heading="Explain what the point means."),
        dict(stem="Van A costs $c = 2m + 40$ dollars for m miles, and Van B costs $c = 3m + 25$ dollars. The graphs cross at $(15, 70)$. What does that point mean?",
             answer="For 15 miles, both vans cost \\$70.", why="2(15) + 40 = 70 and 3(15) + 25 = 70.",
             check=("many", crosses("2*u + 40", "3*u + 25", "15", "70")), space=0.4),
        dict(heading="For questions 3 and 4, use the graph."),
        dict(stem="The system  $y = 2x$  and  $y = -x + 4$  is graphed. Estimate its solution to the nearest tenth.",
             fig=figs.plane((0, 3), (0, 5), lines=[(2, 0), (-1, 4)], solution=(Fr(4, 3), Fr(8, 3)), inches=3.0),
             answer="about (1.3, 2.7)", why="Between x = 1 and x = 2, nearer 1: about (1.3, 2.7). Check: 2(1.3) = 2.6 and −1.3 + 4 = 2.7 — close. Accept a read within 0.1 of each: x from 1.2 to 1.4, y from 2.6 to 2.8.",
             check=estimate("2*u", "-u + 4", "F(4,3)", "F(8,3)", "1.3", "2.7"), space=0.4),
        dict(stem="The system  $y = 3x - 1$  and  $y = -x + 6$  is graphed. Between which two whole numbers is the crossing's x-value?",
             fig=figs.plane((-1, 4), (-4, 7), lines=[(3, -1), (-1, 6)], solution=(Fr(7, 4), Fr(17, 4)), inches=2.4),
             answer="1 and 2", why="At x = 1 the second line is higher (2 and 5); at x = 2 the first is (5 and 4). They cross between, at about 1.8.",
             check=("many", crosses("3*u - 1", "-u + 6", "F(7,4)", "F(17,4)"), ("true", "1 < F(7,4) < 2")), space=0.4),
        dict(heading="Write the system."),
        dict(stem="Lawn service A charges \\$25 to start and \\$15 a visit. Service B charges \\$20 a visit. Write a system for the cost y of x visits.",
             answer="y = 15x + 25  and  y = 20x", why="The amount per visit multiplies x; the \\$25 is A's start. (They cost the same at 5 visits, \\$100.)",
             check=("many", sat("15*u + 25", "1", "40"), sat("20*u", "1", "20"), crosses("15*u + 25", "20*u", "5", "100")), space=0.5),
        dict(heading="For questions 6 and 7, graph both lines on the grid and answer."),
        dict(stem="Rink A charges \\$9 plus \\$4 an hour. Rink B charges \\$7 an hour. Which rink costs less for 5 hours?",
             fig=GRID((0, 6), (0, 42), ys=3, xname="hours", yname="cost (dollars)"), fig_key=KEY((0, 6), (0, 42), [(4, 9, "Rink A"), (7, 0, "Rink B")], (3, 21), ys=3, xname="hours", yname="cost (dollars)"),
             answer="Rink A (\\$29 versus \\$35)", why="y = 4x + 9 and y = 7x cross at (3, 21). After 3 hours Rink A is lower: 4(5) + 9 = 29 and 7(5) = 35.",
             check=("many", crosses("4*u + 9", "7*u", "3", "21"), sat("4*u + 9", "5", "29"), sat("7*u", "5", "35")), space=0.6),
        dict(stem="Estimate the solution:   $y = x + 4$   and   $y = -2x + 6$",
             fig=GRID((-1, 4), (-1, 7)), fig_key=KEY((-1, 4), (-1, 7), [(1, 4), (-2, 6)], (Fr(2, 3), Fr(14, 3)), "about (0.7, 4.7)", "r"),
             answer="about (0.7, 4.7)", why="Tables at x = 0, 1: 4, 5 and 6, 4. The lines cross between x = 0 and x = 1, nearer 1: about (0.7, 4.7). Check: 0.7 + 4 = 4.7 and −2(0.7) + 6 = 4.6 — close. Accept a read within 0.1 of each: x from 0.6 to 0.8, y from 4.6 to 4.8.",
             check=estimate("u + 4", "-2*u + 6", "F(2,3)", "F(14,3)", "0.7", "4.7"), space=0.6),
        dict(heading="Find the missing number."),
        dict(stem="Two plans cost the same for 4 months:  $y = 6x + 20$  and  $y = □x$. What number goes in the box?", answer="11",
             why="6(4) + 20 = 44, and 44 ÷ 4 = 11. Check: 11(4) = 44.",
             check=("many", ("eq", "(6*4 + 20)/4", "11"), crosses("6*u + 20", "11*u", "4", "44")), space=0.6),
        dict(heading="Choose one."),
        dict(stem="The system $y = x + 2$ and $y = -2x + 6$ is graphed. Which ordered pair is closest to its solution?",
             fig=figs.plane((0, 3), (0, 6), lines=[(1, 2), (-2, 6, "y = −2x + 6", (Fr(1, 2), "r"))], solution=(Fr(4, 3), Fr(10, 3)), inches=3.0),
             choices=["$(1.3, 3.3)$", "$(1, 3)$", "$(0, 6)$", "$(3.3, 1.3)$"], correct=0, answer="A",
             why="Between x = 1 and x = 2, nearer 1: about (1.3, 3.3). Check: 1.3 + 2 = 3.3 and −2(1.3) + 6 = 3.4 — close.",
             check=("many", estimate("u + 2", "-2*u + 6", "F(4,3)", "F(10,3)", "1.3", "3.3"),
                    sat("u + 2", "1", "3"), fails("-2*u + 6", "1", "3"), sat("-2*u + 6", "0", "6"), fails("u + 2", "0", "6"),
                    fails("u + 2", "3.3", "1.3")),
             errors={"B": "the nearest grid point, on y = x + 2 only [B1G-M, AR.4.3: plotting and graphing errors]", "C": "where y = −2x + 6 starts, on one line only [B1G-M, AR.4.1: a solution satisfies both]", "D": "the coordinates swapped [B1G-M, GR.1.2: x and y inverted]"}),
        dict(stem="A movie club costs \\$15 to join and \\$6 a movie. Without the club, a movie is \\$9. Which system gives the cost y of x movies?",
             choices=["$y = 6x + 15$ and $y = x + 9$", "$y = 6x + 15$ and $y = 9x$", "$y = 15x + 6$ and $y = 9x$", "$y = 21x$ and $y = 9x$"],
             correct=1, answer="B", why="\\$6 a movie multiplies x and the \\$15 is the start; without the club, \\$9 a movie and no start.",
             check=("many", sat("6*u + 15", "2", "27"), sat("9*u", "2", "18"), fails("15*u + 6", "2", "27"), fails("u + 9", "2", "18"), fails("21*u", "2", "27")),
             errors={"A": "the \\$9 a movie taken as a start [B1G-M, AR.3.5: misinterpreting in context]", "C": "the join fee and the amount per movie swapped [B1G-M, AR.3.3: which value is which]", "D": "the join fee added to the amount per movie [B1G-M, AR.3.5: misinterpreting in context]"}),
        dict(heading="Select all that apply."),
        dict(stem="The cost of x tickets is $y = 4x + 10$ dollars online and $y = 6x$ dollars at the door. The graphs cross at $(5, 30)$. Select all the true statements.",
             choices=["For 5 tickets, both cost \\$30.", "For 30 tickets, both cost \\$5.", "For 2 tickets, online costs less.", "The two never cost the same.", "For 8 tickets, online costs less."],
             correct=[0, 4], answer="A, E",
             why="A: 4(5) + 10 = 30 = 6(5). E: online 42, door 48. B swaps the point; C: online 18, door 12; D: they cross at (5, 30).",
             check=("many", crosses("4*u + 10", "6*u", "5", "30"), ("true", "4*8 + 10 < 6*8"),
                    fails("4*u + 10", "30", "5"), ("true", "sp.Min(4*2 + 10, 6*2) != 4*2 + 10"), meets("4*u + 10", "6*u")),
             errors={"B": "x and y swapped [B1G-M, GR.1.2: x and y inverted]", "C": "the side before the crossing read as the side after [B1G-M, AR.3.5: misinterpreting in context]", "D": "a system with one crossing read as never equal [B1G-M, AR.4.1: how one pair solves two equations]"}),
        dict(heading="Explain."),
        dict(stem="Jo has \\$20 and saves \\$6 a week. Kai has \\$35 and saves \\$6 a week. Will they ever have the same amount? Explain.",
             answer="No. Kai always has \\$15 more, so the lines are parallel and there is no solution.", why="y = 6x + 20 and y = 6x + 35: the same amount per week, different starts.",
             check=never_meet("6*u + 20", "6*u + 35"), lines=2),
    ],

    additional=[
        dict(heading="Use the graph."),
        dict(stem="Tablet A has 90% charge and uses 15% an hour. Tablet B has 60% and uses 5% an hour. When do the tablets have the same charge, and what is it?",
             fig=figs.plane((0, 6), (0, 90), lines=[(-15, 90, "A", (1, "ur")), (-5, 60, "B", (5, "ur"))], ys=15,
                            xname="hours", yname="charge (%)", solution=(3, 45), inches=2.6),
             answer="After 3 hours, both have 45%.", why="The lines cross at (3, 45): −15(3) + 90 = 45 and −5(3) + 60 = 45.",
             check=("many", crosses("-15*u + 90", "-5*u + 60", "3", "45")), space=0.4),
        dict(heading="Explain what the point means."),
        dict(stem="Truck A costs $y = 3x + 30$ dollars for x miles, and Truck B costs $y = 5x + 10$ dollars. The graphs cross at $(10, 60)$. What does that point mean?",
             answer="For 10 miles, both trucks cost \\$60.", why="3(10) + 30 = 60 and 5(10) + 10 = 60.",
             check=("many", crosses("3*u + 30", "5*u + 10", "10", "60")), space=0.4),
        dict(heading="For questions 3 and 4, use the graph."),
        dict(stem="The system  $y = 2x - 1$  and  $y = -x + 3$  is graphed. Estimate its solution to the nearest tenth.",
             fig=figs.plane((0, 4), (-1, 4), lines=[(2, -1), (-1, 3)], solution=(Fr(4, 3), Fr(5, 3)), inches=3.0),
             answer="about (1.3, 1.7)", why="Between x = 1 and x = 2, nearer 1: about (1.3, 1.7). Check: 2(1.3) − 1 = 1.6 and −1.3 + 3 = 1.7 — close. Accept a read within 0.1 of each: x from 1.2 to 1.4, y from 1.6 to 1.8.",
             check=estimate("2*u - 1", "-u + 3", "F(4,3)", "F(5,3)", "1.3", "1.7"), space=0.4),
        dict(stem="The system  $y = 2x - 3$  and  $y = -x + 4$  is graphed. Between which two whole numbers is the crossing's x-value?",
             fig=figs.plane((-1, 5), (-4, 5), lines=[(2, -3), (-1, 4)], solution=(Fr(7, 3), Fr(5, 3)), inches=2.4),
             answer="2 and 3", why="At x = 2 the second line is higher (1 and 2); at x = 3 the first is (3 and 1). They cross between, at about 2.3.",
             check=("many", crosses("2*u - 3", "-u + 4", "F(7,3)", "F(5,3)"), ("true", "2 < F(7,3) < 3")), space=0.4),
        dict(heading="Write the system."),
        dict(stem="Dog walker A charges \\$20 to start and \\$12 a walk. Walker B charges \\$16 a walk. Write a system for the cost y of x walks.",
             answer="y = 12x + 20  and  y = 16x", why="The amount per walk multiplies x; the \\$20 is A's start. (They cost the same at 5 walks, \\$80.)",
             check=("many", sat("12*u + 20", "1", "32"), sat("16*u", "1", "16"), crosses("12*u + 20", "16*u", "5", "80")), space=0.5),
        dict(heading="For questions 6 and 7, graph both lines on the grid and answer."),
        dict(stem="Arcade A charges \\$10 to enter and \\$3 a game. Arcade B charges \\$5 a game. Which arcade costs less for 7 games?",
             fig=GRID((0, 8), (0, 40), ys=5, xname="games", yname="cost (dollars)"), fig_key=KEY((0, 8), (0, 40), [(3, 10, "Arcade A"), (5, 0, "Arcade B")], (5, 25), ys=5, xname="games", yname="cost (dollars)"),
             answer="Arcade A (\\$31 versus \\$35)", why="y = 3x + 10 and y = 5x cross at (5, 25). After 5 games Arcade A is lower: 3(7) + 10 = 31 and 5(7) = 35.",
             check=("many", crosses("3*u + 10", "5*u", "5", "25"), sat("3*u + 10", "7", "31"), sat("5*u", "7", "35")), space=0.6),
        dict(stem="Estimate the solution:   $y = x - 2$   and   $y = -2x + 3$",
             fig=GRID((-1, 4), (-4, 4)), fig_key=KEY((-1, 4), (-4, 4), [(1, -2), (-2, 3)], (Fr(5, 3), Fr(-1, 3)), "about (1.7, −0.3)", "dr+"),
             answer="about (1.7, −0.3)", why="Tables at x = 0, 1, 2: −2, −1, 0 and 3, 1, −1. The lines cross between x = 1 and x = 2, nearer 2: about (1.7, −0.3). Check: 1.7 − 2 = −0.3 and −2(1.7) + 3 = −0.4 — close. Accept a read within 0.1 of each: x from 1.6 to 1.8, y from −0.4 to −0.2.",
             check=estimate("u - 2", "-2*u + 3", "F(5,3)", "F(-1,3)", "1.7", "-0.3"), space=0.6),
        dict(heading="Find the missing number."),
        dict(stem="Two plans cost the same for 6 months:  $y = 7x + 18$  and  $y = □x$. What number goes in the box?", answer="10",
             why="7(6) + 18 = 60, and 60 ÷ 6 = 10. Check: 10(6) = 60.",
             check=("many", ("eq", "(7*6 + 18)/6", "10"), crosses("7*u + 18", "10*u", "6", "60")), space=0.6),
        dict(heading="Choose one."),
        dict(stem="The system $y = x + 1$ and $y = -2x + 5$ is graphed. Which ordered pair is closest to its solution?",
             fig=figs.plane((0, 3), (0, 5), lines=[(1, 1), (-2, 5)], solution=(Fr(4, 3), Fr(7, 3)), inches=3.0),
             choices=["$(1.3, 2.3)$", "$(2.3, 1.3)$", "$(1, 2)$", "$(0, 5)$"], correct=0, answer="A",
             why="Between x = 1 and x = 2, nearer 1: about (1.3, 2.3). Check: 1.3 + 1 = 2.3 and −2(1.3) + 5 = 2.4 — close.",
             check=("many", estimate("u + 1", "-2*u + 5", "F(4,3)", "F(7,3)", "1.3", "2.3"),
                    sat("u + 1", "1", "2"), fails("-2*u + 5", "1", "2"), sat("-2*u + 5", "0", "5"), fails("u + 1", "0", "5"),
                    fails("u + 1", "2.3", "1.3")),
             errors={"B": "the coordinates swapped [B1G-M, GR.1.2: x and y inverted]", "C": "the nearest grid point, on y = x + 1 only [B1G-M, AR.4.3: plotting and graphing errors]", "D": "where y = −2x + 5 starts, on one line only [B1G-M, AR.4.1: a solution satisfies both]"}),
        dict(stem="A skating rink costs \\$12 to join and \\$4 a visit. Without joining, a visit is \\$7. Which system gives the cost y of x visits?",
             choices=["$y = 12x + 4$ and $y = 7x$", "$y = 4x + 12$ and $y = 7x$", "$y = 16x$ and $y = 7x$", "$y = 4x + 12$ and $y = x + 7$"],
             correct=1, answer="B", why="\\$4 a visit multiplies x and the \\$12 is the start; without joining, \\$7 a visit and no start.",
             check=("many", sat("4*u + 12", "2", "20"), sat("7*u", "2", "14"), fails("12*u + 4", "2", "20"), fails("u + 7", "2", "14"), fails("16*u", "2", "20")),
             errors={"A": "the join fee and the amount per visit swapped [B1G-M, AR.3.3: which value is which]", "C": "the join fee added to the amount per visit [B1G-M, AR.3.5: misinterpreting in context]", "D": "the \\$7 a visit taken as a start [B1G-M, AR.3.5: misinterpreting in context]"}),
        dict(heading="Select all that apply."),
        dict(stem="The cost of x games is $y = 3x + 12$ dollars with a pass and $y = 5x$ dollars without one. The graphs cross at $(6, 30)$. Select all the true statements.",
             choices=["For 6 games, both cost \\$30.", "For 30 games, both cost \\$6.", "The two never cost the same.", "For 9 games, the pass costs less.", "For 3 games, the pass costs less."],
             correct=[0, 3], answer="A, D",
             why="A: 3(6) + 12 = 30 = 5(6). D: with the pass 39, without 45. B swaps the point; E: with the pass 21, without 15; C: they cross at (6, 30).",
             check=("many", crosses("3*u + 12", "5*u", "6", "30"), ("true", "3*9 + 12 < 5*9"),
                    fails("3*u + 12", "30", "6"), ("true", "sp.Min(3*3 + 12, 5*3) != 3*3 + 12"), meets("3*u + 12", "5*u")),
             errors={"B": "x and y swapped [B1G-M, GR.1.2: x and y inverted]", "C": "a system with one crossing read as never equal [B1G-M, AR.4.1: how one pair solves two equations]", "E": "the side before the crossing read as the side after [B1G-M, AR.3.5: misinterpreting in context]"}),
        dict(heading="Explain."),
        dict(stem="Ray has \\$50 and saves \\$8 a week. Tess has \\$35 and saves \\$8 a week. Will they ever have the same amount? Explain.",
             answer="No. Ray always has \\$15 more, so the lines are parallel and there is no solution.", why="y = 8x + 50 and y = 8x + 35: the same amount per week, different starts.",
             check=never_meet("8*u + 50", "8*u + 35"), lines=2),
    ],

    te=dict(
        say=["In a story, each line is the amount per 1 times x, plus the start.",
             "The crossing is said in the story's words, with units: 'at 5 rides, both cost \\$20.'",
             "Between the grid lines, estimate with 'about' and check it in both equations — close is right."],
        must="Students solve systems of two linear equations by graphing in real-world contexts and explain what the solution means. They approximate solutions that are not integers (MA.8.AR.4.3, Clarification 1).",
        must_not="The words \"slope\" and \"y-intercept\" are not used until Unit 10. Substitution and elimination belong to Algebra 1. Where a question asks for an estimate, the key accepts a close estimate and does not require the exact pair.",
        read_first=[
            "Thu 10 Dec, 53 minutes, the last lesson before the one-period Unit 11 test on Fri 11 Dec. No review day (ruling 27a): the Unit Review goes home today — hand it out at the IXL slide. Built from the benchmark and the B1G-M first (Lesson Outlines §11.08, standing decisions 1, 2, 3, 6, 7, 9), then read against Math Nation 11.8 (audit Part 2: E7, E8, E12, E14, E15, §3–§5).",
            "Every story crosses at a whole number of games, months, weeks or miles, inside its window and on a grid line; each y-axis names what both lines measure (E7, E14). The one half-unit story (Example 2's tubs) crosses at 2.5 minutes and 7.5 liters. The Examples' question slides show an empty grid (and Example 2 its two tables): draw on the projected slide; the worked slide gives the equations, a line each, and the check. Your Turn 1 shows the story's empty grid, as Example 1 does; Your Turn 2 its two tables beside an empty grid, as Example 2 does; each answer slide shows the graph with the crossing marked, and both cross inside a short table.",
            "One policy for every estimate in the unit: keyed as 'about' a read to the nearest tenth (within 0.05 of the exact crossing), and the key accepts a read within 0.1 of each keyed coordinate — a range that holds no printed grid point, so the nearest-grid-point read, on one line only, never earns credit (E15; the build checks both). The exact crossing is never asked for.",
            "Boards 7 and 9 are designed here (the outline left them open): the plants with an \\$8 price nobody needs, crossing at (10, 50); and board 9, an estimate with its check written out — tomorrow's question 14(b). The Independent Set prints empty grids for 3, 5 and 6, each numbered so the lines' points land on grid lines; its key draws both lines on each grid, from their equations, and marks the crossing (an estimate: the point and 'about')."],
        standard_notes=[("Clarification", "AR.4.3 Clar. 1: approximate non-integer solutions — to the nearest half or tenth, with 'about'."),
                        ("Unit boundary", "Every system is given solved for y, or written from a story as (amount per 1)·x + (start); one story is in c and m, not x and y (bank 2).")],
        sits="The unit's last teaching day. IXL W9J is due by the Unit 11 test (Fri 11 Dec), whose question 14 is today's: a story with its graph, (a) when the two are equal and what both equal, (b) a crossing between the grid lines, approximated.",
        lives="Notes II — the crossing in the story's words — and Notes III's estimate and its close-not-equal check. Board 2 reads the meaning of a crossing (swapped, one taxi only, the same line), board 4 is the estimate diagnostic, its graph beside its options, board 5 the cheaper side of a crossing, board 6 the write-a-system diagnostic, board 9 an estimate checked in both, in writing.",
        materials="Whiteboards, markers and rulers. Hand out the Independent Set, one per student, after whiteboard question 9. Hand out the Unit Review, one per student, to take home today.",
        variation="Boards 1–2 read a story's crossing and say it with units; 3–4 estimate a crossing between the grid lines (where, then about what — 4 a vote). The pattern changes at 5 — the cheaper side of the crossing — and 6 votes on the system a story makes; 7 is the plants with their price as the extra number; 8 runs backwards from a crossing; 9 is a written estimate with its check. The independent set: a story's graph read, a crossing's meaning, an estimate drawn, a system written, the cheaper side drawn, and two savers who never meet.",
        audit=["Every crossing re-derived by sympy at build time as the system's one solution and checked in both equations; every estimate held within 0.05 of the exact crossing and shown not to be on either line exactly; every graph drawn from its equations by u11/figs.py, which refuses a stated crossing that is not on both lines.",
               "Math Nation 11.8 read against this lesson (A7 Unit 11 Audit, Part 2, E7, E8, E12, E14, E15, §3–§5): its sound shapes — a story graphed, the meaning of the crossing, an estimate — are here with our own numbers; its defects are not reproduced."],
        changes=["11.8.1 video warm-up → four retrieval questions (no video).",
                 "11.8.2 internet plans at 2.5 months (E7) → whole-number crossings; board 9 decides a plan by its crossing.",
                 "11.8.3 hikers (E8) → not used; estimates are read on slope-intercept lines (Notes III, boards 3–4, set 3).",
                 "11.8.4 tanks → Example 1's tanks, with our own numbers and a labeled, scaled grid.",
                 "Practice and Homework L8 → the Independent Set; the y-axis names what both lines measure (E14)."],
    ),
)
