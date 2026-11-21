# A7 7.01 Graphing Proportional Relationships (MA.7.AR.4.3) — Wed 6 Jan 2027, a 43-minute day, the first day back.
# Built from the Unit 7 Lesson Outlines, section 7.01, and the unit's standing decisions; figures from u7/figs7.py.
# Whiteboards read; the Independent Set draws (decision 7): Your Turn 1 IS the handout's question 1, drawn in class.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs7 as figs
S = figs.slide
BL = figs.BLANK

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


def table_of(rhs, xs, ys):
    """Each y of a printed table is rhs at its x."""
    return ("many",) + tuple(sat(rhs, str(a), str(b)) for a, b in zip(xs, ys))


def whole_at(p, xs):
    """y = p·x is a whole number at each x."""
    return ("many",) + tuple(("true", "((" + p + ")*(" + str(a) + ")).is_integer") for a in xs)


# ---- slide sizes
def B(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.75)


def BA(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.95)


def SP(xr, yr, **k):
    """A plane drawn for a slide: plane's own size the slide's."""
    return figs.plane(xr, yr, inches=4.2, pt=18, **k)


# ---- notes
RIB = dict(xname="feet of ribbon", yname="cost in dollars")
NOTES1 = S(figs.table([([0, 1, 2, 3, 4], ["0.00", "2.00", "4.00", "6.00", "8.00"])], head=("feet", "cost ($)"), cw=1.6),
           inches=7.0, pt=24, reserve=1.6)
NOTES2 = S(SP((0, 5), (0, 10), lines=[figs.prop(2, "")], ys=2, **RIB,
              points=[(0, 0, "on", "ul"), (1, 2, "on", "dr"), (2, 4, "on", "dr"), (3, 6, "on", "dr")]),
           inches=4.2, pt=18, reserve=1.5)

# ---- Example 1: the hose (3 gallons a minute)
HOSE = dict(xname="minutes", yname="gallons", ys=2)
EX1 = S(figs.row([figs.table([([0, 1, 2, 4], [BL, BL, BL, BL])], head=("minutes", "gallons")),
                  figs.plane((0, 5), (0, 14), **HOSE)], gap=1.8), inches=8.6, pt=18, reserve=0.9)
EX1W = S(SP((0, 5), (0, 14), lines=[figs.prop(3, "")], **HOSE,
            points=[(0, 0, "on", "ul"), (1, 3, "on", "dr"), (2, 6, "on", "dr"), (4, 12, "on", "dr")]),
         inches=4.2, pt=18, reserve=1.4)
# Your Turn 1 = the handout's question 1 (decision 7): the machine, 5 boxes a minute.
BOX = dict(xname="minutes", yname="boxes filled", ys=5)
YT1 = S(figs.row([figs.table([([0, 1, 2, 3], [BL, BL, BL, BL])], head=("minutes", "boxes")),
                  figs.plane((0, 4), (0, 20), **BOX)], gap=1.8), inches=8.6, pt=18, reserve=0.9)
YT1A = S(SP((0, 4), (0, 20), lines=[figs.prop(5, "")], **BOX,
            points=[(1, 5, "on", "dr"), (2, 10, "on", "dr"), (3, 15, "on", "dr")]),
         inches=4.2, pt=18, reserve=0.95)

# ---- Example 2: y = (3/4)x
EX2 = S(figs.row([figs.table([([0, 4, 8], [BL, BL, BL])]), figs.plane((0, 8), (0, 6))], gap=1.8),
        inches=8.6, pt=18, reserve=0.9)
EX2W = S(SP((0, 8), (0, 6), lines=[figs.prop(Fr(3, 4), "")],
            points=[(4, 3, "on", "dr"), (8, 6, "on", "dr")]),
         inches=4.2, pt=18, reserve=1.4)
YT2 = S(figs.row([figs.table([([0, 3, 6], [BL, BL, BL])]), figs.plane((0, 6), (0, 8))], gap=1.8),
        inches=8.6, pt=18, reserve=0.9)
YT2A = S(SP((0, 6), (0, 8), lines=[figs.prop(Fr(4, 3), "")],
            points=[(3, 4, "on", "dr"), (6, 8, "on", "dr")]),
         inches=4.2, pt=18, reserve=0.95)

# ---- boards
GRAPES = figs.table([([0, 1, 2, 6], [BL, BL, "9.00", BL])], head=("pounds", "cost ($)"), cw=2.4)
GRAPES_A = figs.table([([0, 1, 2, 6], ["0.00", "4.50", "9.00", "27.00"])], head=("pounds", "cost ($)"), cw=2.2)
# Board 4: one square is 7 up (ruling 7.01/1), so (2, 14) and the key (1, 7) sit on grid corners; drawn 5.6 in wide so
# the 7-by-4 grid stands at least 2.6 in tall.
P4 = figs.plane((0, 7), (0, 28), lines=[figs.prop(7, "")], ys=7, points=[(2, 14, "on", "dr")], inches=5.6, pt=18)
P4A = figs.plane((0, 7), (0, 28), lines=[figs.prop(7, "")], ys=7, points=[(2, 14, "on", "dr"), (1, 7, "on", "dr")], inches=5.6, pt=18)
# Board 6: four graphs on one window, cost scaled by 2; lettered A–D in this order (keyed D: through (1, 4) and (2, 8)).
# the row fills the column beside the options (ruling 7.01/3): each grid 2 in wide or more, its cells 0.65 as tall as
# wide (figs7 `aspect`, added for this board), the graphs 1.6 grid cells apart; the window runs to 9 so that the last
# number on each x-axis is 8 with a square to spare — at (0, 8) one graph's 8 stood beside the next graph's 0
TK = dict(xname="tickets", yname="cost ($)", ys=2, ystep=4, xstep=2, inches=2.6, pt=18, aspect=0.65)
G_OK = figs.plane((0, 9), (0, 16), lines=[figs.prop(4, "")], points=[(1, 4, ""), (2, 8, "")], **TK)
G_SWAP = figs.plane((0, 9), (0, 16), lines=[figs.prop(Fr(1, 4), "")], points=[(4, 1, ""), (8, 2, "")], **TK)
G_START = figs.plane((0, 9), (0, 16), lines=[(1, 4, "")], points=[(0, 4, ""), (2, 6, "")], **TK)
G_SCALE = figs.plane((0, 9), (0, 16), lines=[figs.prop(8, "")], points=[(1, 8, ""), (2, 16, "")], **TK)
# the reveal: graph D alone, its two points named (the steps stand beside it)
C6A = S(figs.row([SP((0, 8), (0, 16), lines=[figs.prop(4, "")], ys=2, ystep=2, xstep=2, xname="tickets", yname="cost ($)",
                     points=[(1, 4, "on", "dr"), (2, 8, "on", "dr")])], titles=["D"], inches=4.2, pt=18),
        inches=4.2, pt=18, reserve=1.5)
C6 = S(figs.choices4([G_START, G_SCALE, G_SWAP, G_OK], gap=1.6), inches=14.0, pt=18, reserve=0.75)


# ---- the handout: empty grids, the key's graph on the same window
def GRID(xr, yr, **k):
    return figs.plane(xr, yr, inches=3.2, **k)


def KEY(xr, yr, p, pts, **k):
    return figs.plane(xr, yr, lines=[figs.prop(p, "")], points=[(a, b, "") for a, b in pts if (a, b) != (0, 0)], inches=3.2, **k)


def TAB(xs, ys, head=("x", "y")):
    money = any(isinstance(v, str) and "." in v for v in ys)
    return figs.table([(xs, ys)], head=head, cw=1.9 if money else 1.25)


IS1_G, IS1_K = figs.pair((0, 4), (0, 20), lines=[figs.prop(5, "")], points=[(1, 5, ""), (2, 10, ""), (3, 15, "")],
                         ys=5, xname="minutes", yname="boxes filled", inches=3.2)
CH = dict(xname="pounds", yname="cost in dollars", ys=2)

L = dict(
    code="7.01", unit=7, lesson_no=1,
    title="Graphing Proportional Relationships",
    unit_title="Representing Proportional Relationships",
    benchmark="MA.7.AR.4.3",
    benchmark_text="Given a mathematical or real-world context, graph proportional relationships from a table, equation or a written description.",
    target="I can graph a proportional relationship from a description, a table or an equation y = px.",
    essential="Why does the graph of a proportional relationship always pass through the origin?",
    building_on="11.07–08 — a line graphed from a table of values, x = 0 and two more, the third point the check; Grade 6 — unit rates and ratio tables.",
    working_toward="7.02+03 — the constant of proportionality from a table, a graph and a description; 7.05+06 — the equation y = px; Unit 10 (January) — the constant as the line's steepness.",
    vocab=[("proportional relationship", "two quantities are in a proportional relationship when one is always the same number times the other: $y = px$"),
           ("origin", "the point $(0, 0)$, where the axes meet"),
           ("unit rate", "the amount of y for 1 of x: \\$2.00 for 1 foot")],
    ixl=["Graph a proportional relationship: word problems — FJW"],
    closure="Board 9 is written work and it is the exit evidence: in a proportional relationship y is always the same number times x, so when x is 0, y is 0 — the line has to pass through the origin, and Dev's line, which meets the y-axis at 3, cannot be right. A board that says only 'it should start at 0' has the fact and not the reason.",

    mtr=[("MTR.2.1", "a description, a table and a graph of one relationship, every example"),
         ("MTR.4.1", "boards 2, 4 and 6: convince your neighbor, re-vote"),
         ("MTR.6.1", "the third point of every table is the check that the line is straight")],
    hoq=[("Why is (0, 0) in every table today?", "DOK 2"),
         ("Where on the graph do you see the unit rate?", "DOK 1"),
         ("For y = (3/4)x, why are 0, 4 and 8 better x-values than 0, 1 and 2?", "DOK 2"),
         ("Board 6: two graphs pass through the point marked 8 on the cost axis. How does reading the scale first decide which one is right?", "DOK 3")],
    differentiation=[
        ("ESE / 504", "A printed table with x = 0, 1, 2 already written beside each grid, and a ruler; Notes II stays up from board 1 on."),
        ("ELL", "**Proportional**: always the same number times. **Origin**: the corner (0, 0). **Unit rate**: how much for one. **Scale**: what one square stands for."),
        ("Enrichment", "After board 5: for y = (7/12)x, which x-values give whole-number y-values, and why does the 12 decide? (Any multiple of 12.)")],

    warmup=[
        dict(stem="Plan A costs $12 + 4w$, Plan B $6w$, after w weeks. When equal?",
             answer="w = 6",
             check=("eq", "sp.solve(sp.Eq(12 + 4*" + X + ", 6*" + X + "), " + X + ")[0]", "6")),
        dict(stem="$y = 3x - 2$.  Find y when $x = 0$, $1$ and $2$.", answer="−2, 1, 4",
             check=("many", ("eq", "3*0 - 2", "-2"), ("eq", "3*1 - 2", "1"), ("eq", "3*2 - 2", "4"))),
        dict(stem="Solve:  $5x - 4 = 3x + 10$", answer="x = 7",
             check=("eq", "sp.solve(sp.Eq(5*" + X + " - 4, 3*" + X + " + 10), " + X + ")[0]", "7")),
        dict(stem="5 notebooks cost \\$9.00. What does one notebook cost?", answer="\\$1.80",
             check=("eq", "sp.Rational(9, 5)", "F(18, 10)")),
    ],

    notes=[
        dict(numeral="I", head="One is always the same number times the other", min=3,
             text=["Ribbon costs \\$2.00 a foot."],
             fig=NOTES1,
             items2=["$c = 2f$:   the cost is always 2 times the feet.   0 feet cost \\$0.00."],
             letters=False),
        dict(numeral="II", head="Its graph", min=3,
             fig=NOTES2,
             items2=["Read the scales first:  the cost axis is scaled by 2.",
                     "A straight line through the origin;  $(1, 2)$ shows the unit rate."],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=2,
             prompt=["A hose fills a pool with 3 gallons of water every minute."],
             fig=EX1, ask="Make the table, then graph the gallons against the minutes.",
             worked=[dict(min=2,
                          rows=[("\\text{gallons} = 3 \\cdot \\text{minutes}", "3 times the minutes"),
                                ("0,\\ 3,\\ 6,\\ 12", "at 0, 1, 2, 4 minutes"),
                                ("(1, 3):\\ \\text{the unit rate}", "3 gallons for 1 minute")],
                          fig=EX1W, answer="The line through (0, 0) and (4, 12)")],
             check=table_of("3*u", [0, 1, 2, 4], [0, 3, 6, 12]),
             # decision 7: this Your Turn IS the Independent Set's question 1 — hand the set out now; every student
             # draws question 1 on its grid while the teacher circulates.
             your_turn=dict(min=5,
                            prompt=["Handout, question 1:  a machine fills 5 boxes every minute."],
                            fig=YT1, fig_a=YT1A, ask="Make the table, then graph the boxes against the minutes.",
                            steps=["boxes:   0,  5,  10,  15", "$5 \\cdot 3 = 15$:   the point $(3, 15)$",
                                   "a straight line through the origin"],
                            answer="The line through (0, 0) and (3, 15)"),
             yt_check=table_of("5*u", [0, 1, 2, 3], [0, 5, 10, 15])),
        dict(title="Example 2", min_q=1,
             prompt=["$y = \\frac{3}{4}x$"], fig=EX2, ask="Choose x-values that give easy points, then graph.",
             worked=[dict(min=2,
                          rows=[("x = 0,\\ 4,\\ 8", "easy points: 4 divides them"),
                                ("\\frac{3}{4}(4) = 3", "y at x = 4"),
                                ("\\frac{3}{4}(8) = 6", "the third point is the check")],
                          fig=EX2W, answer="The line through (0, 0) and (8, 6)")],
             check=table_of("F(3,4)*u", [0, 4, 8], [0, 3, 6]),
             your_turn=dict(min=2,
                            prompt=["Graph  $y = \\frac{4}{3}x$:  choose x-values that give easy points."],
                            fig=YT2, fig_a=YT2A, ask="",
                            steps=["easy points:   x = 0, 3, 6", "$\\frac{4}{3}(3) = 4$   and   $\\frac{4}{3}(6) = 8$",
                                   "a straight line through the origin"],
                            answer="The line through (0, 0) and (6, 8)"),
             yt_check=table_of("F(4,3)*u", [0, 3, 6], [0, 4, 8])),
    ],

    # The round: a table from a description (1); a vote on a point of the same story (2); y = px at three x's (3);
    # a vote on a second point of a graphed line (4); the easy x's of a fraction (5); a vote on four graphs, the cost
    # axis scaled by 2 (6); the copier, its room number the extra number (7); backwards from (5, 13) (8);
    # the line that misses the origin, written (9).
    whiteboard=[
        dict(text=["Grapes cost the same for each pound: 2 pounds cost \\$9.00.",
                   "**Complete the table of cost against pounds."],
             qtext="Grapes cost the same for each pound: 2 pounds cost \\$9.00. Complete the table: pounds 0, 1, 2, 6; cost in dollars ?, ?, 9.00, ?.",
             fig=S(GRAPES, inches=8.0, pt=24, reserve=0.75), fig_a=S(GRAPES_A, inches=5.2, pt=18, reserve=0.95),
             steps=["1 pound:   $9 \\div 2 = 4.50$", "0 pounds:   $4.50 \\cdot 0 = 0$", "6 pounds:   $4.50 \\cdot 6 = 27.00$"],
             answer="\\$0.00, \\$4.50, \\$27.00",
             check=("many", ("eq", "sp.Rational(9, 2)*0", "0"), ("eq", "sp.Rational(9, 2)", "F(450, 100)"),
                    ("eq", "sp.Rational(9, 2)*6", "27")),
             wrong="\\$18.00 for 1 pound — 9 · 2, not 9 ÷ 2 [B1G-M, AR.4.3: dependent and independent confused]; \\$13.00 for 6 pounds — the 4 more pounds added as \\$4 [B1G-M, AR.4.1: a constant difference taken for the rate]"),
        dict(kind="mc", text=["Grapes cost the same for each pound: 2 pounds cost \\$9.00.",
                              "**Which point is on the graph of cost against pounds?"],
             steps=["1 pound:   $9 \\div 2 = 4.50$", "4 pounds:   $4.50 \\cdot 4 = 18$:   the point $(4, 18)$"],
             choices=["(4, 8.5)", "(18, 4)", "(4, 18)", "(0, 4.5)"], correct=2, answer="C — (4, 18)",
             errors={"A": "4.50 added to 4, not multiplied [B1G-M, AR.4.1: a constant difference taken for the rate]", "B": "the cost written first: x and y swapped [B1G-M, AR.4.3: axes swapped]", "D": "the unit rate 4.50 read as the cost of 0 pounds [Notes I: 0 feet cost \\$0.00]"},
             check=("many", sat("F(9,2)*u", "4", "18"), fails("F(9,2)*u", "18", "4"), ("eq", "4 + F(9,2)", "F(17,2)"),
                    fails("F(9,2)*u", "4", "F(17,2)"), fails("F(9,2)*u", "0", "F(9,2)"))),
        dict(text=["**$y = 2.2x$.  Find y when $x = 0$, $5$ and $10$."],
             steps=["$2.2 \\cdot 0 = 0$", "$2.2 \\cdot 5 = 11$", "$2.2 \\cdot 10 = 22$"],
             answer="0, 11, 22",
             check=table_of("F(22,10)*u", [0, 5, 10], [0, 11, 22]),
             wrong="2.2, 7.2, 12.2 — 2.2 added to x, not multiplied [B1G-M, AR.4.1: a constant difference taken for the rate]; 2.2 at x = 0 — 2.2 read as a start [Notes II: a straight line through the origin]"),
        dict(kind="mc", text=["A proportional relationship is graphed.", "**Which other point is on the line?"],
             qtext="A proportional relationship is graphed: a straight line through the origin and (2, 14). Which other point is on the line?",
             fig=S(P4, inches=5.6, pt=18, reserve=0.75), fig_a=S(P4A, inches=5.6, pt=18, reserve=0.95),
             steps=["$(2, 14)$:   $14 \\div 2 = 7$,  7 for each 1 of x", "1 of x:   $7 \\cdot 1 = 7$:   the point $(1, 7)$"],
             choices=["(7, 1)", "(1, 7)", "(4, 16)", "(1, 14)"], correct=1, answer="B — (1, 7)",
             errors={"A": "the coordinates of (1, 7) reversed [B1G-M, AR.4.3: axes swapped]", "C": "2 added to each coordinate of (2, 14) [B1G-M, AR.4.1: a constant difference taken for the rate]", "D": "the y-value 14 taken as the amount for 1 of x [Notes II: (1, 2) shows the unit rate]"},
             check=("many", sat("7*u", "2", "14"), sat("7*u", "1", "7"), fails("7*u", "7", "1"), fails("7*u", "4", "16"),
                    fails("7*u", "1", "14"))),
        dict(text=["**$y = \\frac{5}{6}x$.  Choose three x-values that give whole-number y-values."],
             steps=["the 6 must divide x:   $x = 0$, $6$, $12$", "$\\frac{5}{6}(6) = 5$   and   $\\frac{5}{6}(12) = 10$"],
             answer="Any multiples of 6 — such as 0, 6, 12",
             check=("many", whole_at("sp.Rational(5, 6)", [0, 6, 12]), ("eq", "sp.Rational(5, 6)*12", "10"),
                    ("true", "not (sp.Rational(5, 6)*5).is_integer")),
             wrong="0, 5, 10 — the 5 of the numerator chosen: 5/6 · 5 is not whole [B1G-M, AR.4.3: a scale of 1 used where a fraction needs another]; 0, 1, 2 — the first x's of every table [Example 2: choose x-values that give easy points]"),
        dict(kind="mc", text=["**Tickets cost \\$4.00 each. Which graph shows cost against tickets?"],
             qtext="Tickets cost \\$4.00 each. Four graphs, each with tickets across and cost in dollars up, the cost axis scaled by 2. Which graph shows the cost against the number of tickets?",
             fig=C6, fig_a=C6A,
             steps=["read the scales first:  cost by 2", "1 ticket, \\$4:   $(1, 4)$;   2 tickets, \\$8:   $(2, 8)$"],
             choices=["A", "B", "C", "D"], correct=3, answer="D",
             errors={"A": "the \\$4.00 read as a start: through (0, 4) and (2, 6) [Notes II: a straight line through the origin]", "B": "the scale ignored: 4 squares up read as \\$4, so through (1, 8) [B1G-M, AR.4.3: the scale read as 1]", "C": "the axes swapped: through (8, 2), 8 tickets for \\$2 [B1G-M, AR.4.3: axes swapped]"},
             check=("many", table_of("4*u", [1, 2], [4, 8]), table_of("F(1,4)*u", [8], [2]), fails("4*u", "8", "2"),
                    table_of("8*u", [1], [8]), fails("4*u", "1", "8"),
                    table_of("u + 4", [0, 2], [4, 6]), fails("4*u", "0", "4"))),
        dict(text=["A copier in room 114 makes 8 copies every minute.",
                   "Its graph of copies against minutes passes through $(7, □)$.", "**What number goes in the box?"],
             unneeded="114",
             steps=["8 copies for each minute", "7 minutes:   $8 \\cdot 7 = 56$"],
             answer="56",
             check=sat("8*u", "7", "56"),
             wrong="15 — 8 + 7, added not multiplied [B1G-M, AR.4.1: a constant difference taken for the rate]; 798 — the room number used, 114 · 7 [ruling 22]"),
        dict(text=["The graph of a proportional relationship passes through $(5, 13)$.",
                   "**What is y when $x = 1$?"],
             steps=["y for each 1 of x:   $13 \\div 5 = 2.6$"],
             answer="2.6",
             check=("many", ("eq", "sp.Rational(13, 5)", "F(26, 10)"), sat("F(13,5)*u", "5", "13")),
             wrong="65 — 13 · 5, multiplied not divided [B1G-M, AR.4.3: dependent and independent confused]; 0.38 — 5 ÷ 13, the ratio reversed [B1G-M, AR.4.3: dependent and independent confused]; 9 — 13 − 4, the 4 steps back taken as 1 each [B1G-M, AR.4.1: a constant difference taken for the rate]"),
        # repeat_ok: rule D matches only 0 (the origin, the point of the board) and the 3 where Dev's line meets the
        # y-axis — a coincidence of small numbers; nothing above asks this.
        dict(repeat_ok=True, kind="written", text=["Dev graphs a proportional relationship. His line crosses the y-axis at 3.",
                                   "**How do you know something is wrong? Explain."],
             qtext="Dev graphs a proportional relationship. His line crosses the y-axis at 3. How do you know something is wrong? Explain.",
             steps=["proportional:  y is always the same number times x", "at $x = 0$:   $y = p \\cdot 0 = 0$",
                    "the line must pass through $(0, 0)$, not $(0, 3)$"],
             answer="When x is 0, y is 0: the line has to pass through the origin.",
             check=("many", ("eq", "p*0", "0"), ("true", "0 != 3")),
             wrong="'the line is too steep' — the steepness blamed, not the start [B1G-M, AR.4.3: plotting and graphing errors]; 'it should start at 3 on the x-axis' — the axes swapped [B1G-M, AR.4.3: axes swapped]"),
    ],

    # The six (decision 7: the handout prints empty grids, the key draws the graph): question 1 is Your Turn 1,
    # drawn in class; a table (2); y = 3x (3); y = (1/4)x, the easy x's (4); the pattern breaks — a rate that is not a
    # unit rate, $7.00 for 2 pounds, its table first (5); what the point (1, 3.5) of that graph means (6).
    independent=[
        # repeat_ok: decision 7 — this question IS Your Turn 1, drawn in class with the teacher circulating.
        dict(repeat_ok=True,
             stem="A machine fills 5 boxes every minute. Complete the table, then graph the boxes filled against the minutes.",
             fig=figs.row([TAB([0, 1, 2, 3], [BL, BL, BL, BL], ("minutes", "boxes")), IS1_G], gap=1.8),
             fig_key=figs.row([TAB([0, 1, 2, 3], [0, 5, 10, 15], ("minutes", "boxes")), IS1_K], gap=1.8),
             answer="0, 5, 10, 15; the line through the origin and (3, 15)",
             why="5 times the minutes: 0, 5, 10, 15 at 0, 1, 2, 3 minutes. The points lie on a straight line through the origin.",
             check=table_of("5*u", [0, 1, 2, 3], [0, 5, 10, 15]), space=0.3),
        dict(stem="The table shows a proportional relationship. Graph it.",
             fig=figs.row([TAB([2, 4, 6], [3, 6, 9]), GRID((0, 8), (0, 12))], gap=1.8),
             fig_key=figs.row([TAB([2, 4, 6], [3, 6, 9]), KEY((0, 8), (0, 12), Fr(3, 2), [(0, 0), (2, 3), (4, 6), (6, 9)])], gap=1.8),
             answer="The line through (0, 0), (2, 3), (4, 6) and (6, 9)",
             why="y ÷ x is 1.5 in every row: 3 ÷ 2 = 6 ÷ 4 = 9 ÷ 6 = 1.5. Plot the three points and the origin: a straight line through the origin.",
             check=table_of("F(3,2)*u", [0, 2, 4, 6], [0, 3, 6, 9]), space=0.3),
        dict(stem="Graph  $y = 6x$.",
             fig=GRID((0, 4), (0, 24), ys=4),
             fig_key=KEY((0, 4), (0, 24), 6, [(0, 0), (2, 12), (4, 24)], ys=4),
             answer="The line through (0, 0), (2, 12) and (4, 24)",
             why="Read the scales first: y by 4. At x = 0, 2, 4, y = 0, 12, 24; the third point is the check.",
             check=table_of("6*u", [0, 2, 4], [0, 12, 24]), space=0.3),
        dict(stem="Graph  $y = \\frac{1}{4}x$.  Choose x-values that give easy points.",
             fig=GRID((0, 12), (0, 4), xs=2),
             fig_key=KEY((0, 12), (0, 4), Fr(1, 4), [(0, 0), (4, 1), (8, 2), (12, 3)], xs=2),
             answer="The line through (0, 0), (4, 1), (8, 2) and (12, 3)",
             why="Multiples of 4 for x: at x = 0, 4, 8, 12, y = 0, 1, 2, 3. Read the scales first: x by 2.",
             check=table_of("F(1,4)*u", [0, 4, 8, 12], [0, 1, 2, 3]), space=0.3),
        dict(stem="Cherries cost the same for each pound: 2 pounds cost \\$7.00. Complete the table, then graph the cost against the pounds.",
             fig=figs.row([TAB([0, 2, 4, 8], [BL, "7.00", BL, BL], ("pounds", "cost ($)")), GRID((0, 8), (0, 28), **CH)], gap=1.8),
             fig_key=figs.row([TAB([0, 2, 4, 8], ["0.00", "7.00", "14.00", "28.00"], ("pounds", "cost ($)")),
                               KEY((0, 8), (0, 28), Fr(7, 2), [(0, 0), (2, 7), (4, 14), (8, 28)], **CH)], gap=1.8),
             answer="\\$0.00, \\$14.00, \\$28.00; the line through the origin and (8, 28)",
             why="7.00 ÷ 2 = 3.50 for each pound: 3.50 · 4 = 14.00 and 3.50 · 8 = 28.00. Read the scales first: cost by 2.",
             check=table_of("F(7,2)*u", [0, 2, 4, 8], [0, 7, 14, 28]), space=0.3),
        dict(stem="The graph of question 5 passes through $(1, 3.5)$. What does that point mean?",
             answer="1 pound of cherries costs \\$3.50: the unit rate.",
             why="x is pounds and y is cost in dollars: (1, 3.5) is \\$3.50 for 1 pound, 7.00 ÷ 2.",
             check=("many", sat("F(7,2)*u", "1", "F(7,2)"), ("eq", "7/sp.Integer(2)", "F(35, 10)")), space=0.6),
    ],

    # Bank: tables from a description and an equation (1–2); three graphs on empty grids — a description, a fraction,
    # a table (3–5); the unit rate read off a graph (6); backwards (7); easy x's (8); a point of a story's graph and a
    # second point of a graphed line, each a vote (9–10); the line that misses the origin, explained (11); a select-all
    # of the points on y = 4x (12). The additional bank mirrors it position by position with new numbers.
    bank=[
        dict(heading="Complete the table."),
        dict(stem="A car wash cleans 6 cars every hour. Complete the table of cars against hours.",
             fig=TAB([0, 1, 3, 5], [BL, BL, BL, BL], ("hours", "cars")),
             answer="0, 6, 18, 30", why="6 times the hours: 6 · 0, 6 · 1, 6 · 3, 6 · 5.",
             check=table_of("6*u", [0, 1, 3, 5], [0, 6, 18, 30]), space=0.4),
        dict(stem="$y = 7.5x$. Complete the table.",
             fig=TAB([0, 2, 4, 6], [BL, BL, BL, BL]),
             answer="0, 15, 30, 45", why="7.5 · 0 = 0, 7.5 · 2 = 15, 7.5 · 4 = 30, 7.5 · 6 = 45.",
             check=table_of("F(15,2)*u", [0, 2, 4, 6], [0, 15, 30, 45]), space=0.4),
        dict(heading="Graph the relationship on the grid."),
        dict(stem="A baker uses 3 cups of flour for every batch of muffins. Graph the cups of flour against the batches.",
             fig=GRID((0, 6), (0, 18), ys=2, xname="batches", yname="cups of flour"),
             fig_key=KEY((0, 6), (0, 18), 3, [(0, 0), (2, 6), (4, 12), (6, 18)], ys=2, xname="batches", yname="cups of flour"),
             answer="The line through (0, 0), (2, 6), (4, 12) and (6, 18)",
             why="3 cups for each batch: 0, 6, 12, 18 cups at 0, 2, 4, 6 batches. Read the scales first: cups by 2.",
             check=table_of("3*u", [0, 2, 4, 6], [0, 6, 12, 18]), space=0.3),
        dict(stem="Graph  $y = \\frac{2}{3}x$.",
             fig=GRID((0, 9), (0, 6)),
             fig_key=KEY((0, 9), (0, 6), Fr(2, 3), [(0, 0), (3, 2), (6, 4), (9, 6)]),
             answer="The line through (0, 0), (3, 2), (6, 4) and (9, 6)",
             why="Multiples of 3 for x: at x = 0, 3, 6, 9, y = 0, 2, 4, 6.",
             check=table_of("F(2,3)*u", [0, 3, 6, 9], [0, 2, 4, 6]), space=0.3),
        dict(stem="The table shows a proportional relationship. Graph it.",
             fig=figs.row([TAB([1, 3, 5], [2, 6, 10]), GRID((0, 6), (0, 12), ys=2)], gap=1.8),
             fig_key=figs.row([TAB([1, 3, 5], [2, 6, 10]), KEY((0, 6), (0, 12), 2, [(0, 0), (1, 2), (3, 6), (5, 10)], ys=2)], gap=1.8),
             answer="The line through (0, 0), (1, 2), (3, 6) and (5, 10)",
             why="y ÷ x is 2 in every row. Plot the points and the origin: a straight line through the origin.",
             check=table_of("2*u", [0, 1, 3, 5], [0, 2, 6, 10]), space=0.3),
        dict(heading="Use the graph."),
        dict(stem="The graph shows the cost of bags of popcorn. How much does 1 bag cost?",
             fig=figs.plane((0, 5), (0, 20), lines=[figs.prop(4, "")], ys=4, xname="bags", yname="cost in dollars",
                            points=[(3, 12, "on", "dr")], inches=2.6),
             answer="\\$4.00", why="3 bags cost \\$12.00: 12 ÷ 3 = 4.00 for each bag.",
             check=("many", sat("4*u", "3", "12"), ("eq", "12/sp.Integer(3)", "4")), space=0.4),
        dict(heading="Work backwards."),
        dict(stem="The graph of a proportional relationship passes through $(5, 19)$. What is y when $x = 1$?",
             answer="3.8", why="19 ÷ 5 = 3.8: the amount of y for each 1 of x.",
             check=("eq", "sp.Rational(19, 5)", "F(38, 10)"), space=0.5),
        dict(heading="Choose x-values."),
        dict(stem="$y = \\frac{3}{8}x$. Choose three x-values that give whole-number y-values.",
             answer="Any multiples of 8 — such as 0, 8, 16", why="The 8 must divide x: 3/8 · 8 = 3 and 3/8 · 16 = 6.",
             check=whole_at("sp.Rational(3, 8)", [0, 8, 16]), space=0.5),
        dict(heading="Choose one."),
        dict(stem="Kiwis cost \\$0.75 each. Which point is on the graph of cost against kiwis?",
             choices=["$(4, 3)$", "$(4, 4.75)$", "$(0, 0.75)$", "$(3, 4)$"], correct=0, answer="A",
             why="4 kiwis cost 0.75 · 4 = \\$3.00: the point (4, 3).",
             check=("many", sat("F(3,4)*u", "4", "3"), fails("F(3,4)*u", "3", "4"), fails("F(3,4)*u", "4", "F(19,4)"),
                    fails("F(3,4)*u", "0", "F(3,4)")),
             errors={"B": "0.75 added to 4, not multiplied [B1G-M, AR.4.1: a constant difference taken for the rate]", "C": "the price of one read as the cost of none [Notes I: 0 feet cost \\$0.00]", "D": "the cost written first: x and y swapped [B1G-M, AR.4.3: axes swapped]"}),
        dict(stem="A proportional relationship is graphed. Which other point is on the line?",
             fig=figs.plane((0, 5), (0, 10), lines=[figs.prop(2, "")], ys=2, points=[(3, 6, "on", "dr")], inches=2.4),
             choices=["$(2, 1)$", "$(1, 6)$", "$(5, 8)$", "$(1, 2)$"], correct=3, answer="D",
             why="6 ÷ 3 = 2 for each 1 of x: the point (1, 2).",
             check=("many", sat("2*u", "3", "6"), sat("2*u", "1", "2"), fails("2*u", "2", "1"), fails("2*u", "5", "8"),
                    fails("2*u", "1", "6")),
             errors={"A": "the coordinates of (1, 2) reversed [B1G-M, AR.4.3: axes swapped]", "B": "the y-value 6 taken as the amount for 1 of x [Notes II: (1, 2) shows the unit rate]", "C": "2 added to each coordinate of (3, 6) [B1G-M, AR.4.1: a constant difference taken for the rate]"}),
        dict(heading="Explain."),
        dict(stem="Ana graphs a proportional relationship and her line starts at $(0, 2)$. What is wrong?",
             answer="When x is 0, y is 0: the line has to pass through the origin, not (0, 2).",
             why="y is always the same number times x, and any number times 0 is 0.",
             check=("many", ("eq", "p*0", "0"), ("true", "0 != 2")), space=0.6),
        dict(heading="Select all that apply."),
        dict(stem="Select all the points on the graph of $y = 4x$.",
             choices=["$(1, 5)$", "$(3, 12)$", "$(8, 2)$", "$(2, 8)$", "$(0, 0)$"], correct=[1, 3, 4], answer="B, D, E",
             why="4 · 0 = 0, 4 · 2 = 8 and 4 · 3 = 12. (8, 2) has its coordinates reversed; (1, 5) is 1 + 4.",
             check=("many", sat("4*u", "0", "0"), sat("4*u", "2", "8"), sat("4*u", "3", "12"),
                    fails("4*u", "8", "2"), fails("4*u", "1", "5")),
             errors={"A": "4 added to x, not multiplied [B1G-M, AR.4.1: a constant difference taken for the rate]", "C": "the coordinates of (2, 8) reversed [B1G-M, AR.4.3: axes swapped]"}),
    ],

    additional=[
        dict(heading="Complete the table."),
        dict(stem="A worker packs 7 crates every hour. Complete the table of crates against hours.",
             fig=TAB([0, 1, 3, 5], [BL, BL, BL, BL], ("hours", "crates")),
             answer="0, 7, 21, 35", why="7 times the hours: 7 · 0, 7 · 1, 7 · 3, 7 · 5.",
             check=table_of("7*u", [0, 1, 3, 5], [0, 7, 21, 35]), space=0.4),
        dict(stem="$y = 6.5x$. Complete the table.",
             fig=TAB([0, 2, 4, 6], [BL, BL, BL, BL]),
             answer="0, 13, 26, 39", why="6.5 · 0 = 0, 6.5 · 2 = 13, 6.5 · 4 = 26, 6.5 · 6 = 39.",
             check=table_of("F(13,2)*u", [0, 2, 4, 6], [0, 13, 26, 39]), space=0.4),
        dict(heading="Graph the relationship on the grid."),
        dict(stem="A coach packs 4 water bottles in every cooler. Graph the bottles against the coolers.",
             fig=GRID((0, 6), (0, 24), ys=4, xname="coolers", yname="bottles"),
             fig_key=KEY((0, 6), (0, 24), 4, [(0, 0), (1, 4), (3, 12), (6, 24)], ys=4, xname="coolers", yname="bottles"),
             answer="The line through (0, 0), (1, 4), (3, 12) and (6, 24)",
             why="4 bottles for each cooler. Read the scales first: bottles by 4.",
             check=table_of("4*u", [0, 1, 3, 6], [0, 4, 12, 24]), space=0.3),
        dict(stem="Graph  $y = \\frac{8}{5}x$.",
             fig=GRID((0, 10), (0, 16), ys=2),
             fig_key=KEY((0, 10), (0, 16), Fr(8, 5), [(0, 0), (5, 8), (10, 16)], ys=2),
             answer="The line through (0, 0), (5, 8) and (10, 16)",
             why="Multiples of 5 for x: at x = 0, 5, 10, y = 0, 8, 16. Read the scales first: y by 2.",
             check=table_of("F(8,5)*u", [0, 5, 10], [0, 8, 16]), space=0.3),
        dict(stem="The table shows a proportional relationship. Graph it.",
             fig=figs.row([TAB([2, 3, 5], [8, 12, 20]), GRID((0, 6), (0, 24), ys=4)], gap=1.8),
             fig_key=figs.row([TAB([2, 3, 5], [8, 12, 20]), KEY((0, 6), (0, 24), 4, [(0, 0), (2, 8), (3, 12), (5, 20)], ys=4)], gap=1.8),
             answer="The line through (0, 0), (2, 8), (3, 12) and (5, 20)",
             why="y ÷ x is 4 in every row. Plot the points and the origin: a straight line through the origin.",
             check=table_of("4*u", [0, 2, 3, 5], [0, 8, 12, 20]), space=0.3),
        dict(heading="Use the graph."),
        dict(stem="The graph shows the cost of packs of stickers. How much does 1 pack cost?",
             fig=figs.plane((0, 8), (0, 12), lines=[figs.prop(Fr(3, 2), "")], ys=2, xname="packs", yname="cost in dollars",
                            points=[(4, 6, "on", "dr")], inches=2.6),
             answer="\\$1.50", why="4 packs cost \\$6.00: 6 ÷ 4 = 1.50 for each pack.",
             check=("many", sat("F(3,2)*u", "4", "6"), ("eq", "6/sp.Integer(4)", "F(15, 10)")), space=0.4),
        dict(heading="Work backwards."),
        dict(stem="The graph of a proportional relationship passes through $(5, 8)$. What is y when $x = 1$?",
             answer="1.6", why="8 ÷ 5 = 1.6: the amount of y for each 1 of x.",
             check=("eq", "sp.Rational(8, 5)", "F(16, 10)"), space=0.5),
        dict(heading="Choose x-values."),
        dict(stem="$y = \\frac{4}{5}x$. Choose three x-values that give whole-number y-values.",
             answer="Any multiples of 5 — such as 0, 5, 10", why="The 5 must divide x: 4/5 · 5 = 4 and 4/5 · 10 = 8.",
             check=whole_at("sp.Rational(4, 5)", [0, 5, 10]), space=0.5),
        dict(heading="Choose one."),
        dict(stem="Pears cost \\$1.25 each. Which point is on the graph of cost against pears?",
             choices=["$(0, 1.25)$", "$(4, 5.25)$", "$(4, 5)$", "$(5, 4)$"], correct=2, answer="C",
             why="4 pears cost 1.25 · 4 = \\$5.00: the point (4, 5).",
             check=("many", sat("F(5,4)*u", "4", "5"), fails("F(5,4)*u", "5", "4"), fails("F(5,4)*u", "4", "F(21,4)"),
                    fails("F(5,4)*u", "0", "F(5,4)")),
             errors={"A": "the price of one read as the cost of none [Notes I: 0 feet cost \\$0.00]", "B": "1.25 added to 4, not multiplied [B1G-M, AR.4.1: a constant difference taken for the rate]", "D": "the cost written first: x and y swapped [B1G-M, AR.4.3: axes swapped]"}),
        dict(stem="A proportional relationship is graphed. Which other point is on the line?",
             fig=figs.plane((0, 5), (0, 15), lines=[figs.prop(3, "")], ys=3, points=[(4, 12, "on", "dr")], inches=2.4),
             choices=["$(6, 14)$", "$(1, 3)$", "$(1, 12)$", "$(3, 1)$"], correct=1, answer="B",
             why="12 ÷ 4 = 3 for each 1 of x: the point (1, 3).",
             check=("many", sat("3*u", "4", "12"), sat("3*u", "1", "3"), fails("3*u", "3", "1"), fails("3*u", "6", "14"),
                    fails("3*u", "1", "12")),
             errors={"A": "2 added to each coordinate of (4, 12) [B1G-M, AR.4.1: a constant difference taken for the rate]", "C": "the y-value 12 taken as the amount for 1 of x [Notes II: (1, 2) shows the unit rate]", "D": "the coordinates of (1, 3) reversed [B1G-M, AR.4.3: axes swapped]"}),
        dict(heading="Explain."),
        dict(stem="Leo graphs a proportional relationship and his line starts at $(0, 5)$. What is wrong?",
             answer="When x is 0, y is 0: the line has to pass through the origin, not (0, 5).",
             why="y is always the same number times x, and any number times 0 is 0.",
             check=("many", ("eq", "p*0", "0"), ("true", "0 != 5")), space=0.6),
        dict(heading="Select all that apply."),
        dict(stem="Select all the points on the graph of $y = 9x$.",
             choices=["$(1, 10)$", "$(2, 18)$", "$(3, 27)$", "$(0, 0)$", "$(18, 2)$"], correct=[1, 2, 3], answer="B, C, D",
             why="9 · 0 = 0, 9 · 2 = 18 and 9 · 3 = 27. (18, 2) has its coordinates reversed; (1, 10) is 1 + 9.",
             check=("many", sat("9*u", "0", "0"), sat("9*u", "2", "18"), sat("9*u", "3", "27"),
                    fails("9*u", "18", "2"), fails("9*u", "1", "10")),
             errors={"A": "9 added to x, not multiplied [B1G-M, AR.4.1: a constant difference taken for the rate]", "E": "the coordinates of (2, 18) reversed [B1G-M, AR.4.3: axes swapped]"}),
    ],

    te=dict(
        must="Plot a proportional relationship from any of the three sources; identify the constant on the graph.",
        must_not="Non-proportional lines; intercepts other than the origin.",
        read_first=[
            "Wednesday 6 January, the first day back from winter break and a 43-minute day. The kit's timing table must total 53, so the table is the full lesson; the cut is under Materials. Built from the benchmark and its clarification first (the Unit 7 Lesson Outlines, §7.01, and the unit's standing decisions 1–7); Math Nation was read for scope only.",
            "The class last graphed lines from a table in Unit 11 (x = 0 and two more, the third point the check); today every table starts at the origin. The definition is said the same way every day: one quantity is always the same number times the other, y = px. The number is the unit rate today; it is named the constant of proportionality tomorrow (7.02+03). 'Slope' and 'y-intercept' are on no student page. Read the scales first: Notes II's cost axis is scaled by 2, and board 6 turns on it.",
            "The Examples' question slides show an empty table beside an empty grid: fill and draw them on the projected slide. Right after Example 1, hand out the Independent Set: Your Turn 1 is its question 1 (the machine, 5 boxes a minute), and every student draws it on the handout's grid while you circulate. The boards read a table, a point or a graph; nobody draws a graph on a whiteboard. The key draws each graph on the student's own grid.",
            "Changed from the outline: none of its numbers. Its Notes III was dropped at the plan review (Barton 5); the deck has two Notes slides."],
        materials="Whiteboards and markers; rulers. The Independent Set, one per student, handed out at Example 1's Your Turn — its question 1 is that Your Turn, drawn then, in class, under your eye. THE 43-MINUTE CUT (the timing table is the full 53 — the build cannot print a 43-minute one): skip board 3 first (y = 2.2x), then board 5 (the easy x's of y = (5/6)x); warm-up 4 min (two silent, reveal); of the Independent Set, question 1 is already drawn and questions 2–6 go home; IXL starts outside class — about 12 minutes out. Never cut boards 2, 4 and 6 (the three votes) or board 9.",
        variation="Board 1 builds a table from a description and 2 votes on a point of the same story; 3 is an equation at three x's; 4 votes on a second point of a graphed line; 5 is a fraction whose x's must be chosen; 6 votes on four graphs with the cost axis scaled by 2 — the pattern breaks here: two graphs pass through the same grid square, and only the scale tells them apart. 7 carries the room number as the extra number; 8 runs backwards; 9 is written. The set: question 1 drawn in class, then a table, y = 6x (y by 4), y = (1/4)x (x by 2), and the break — a rate that is not a unit rate, \\$7.00 for 2 pounds, then what (1, 3.5) on that graph means.",
        audit=["Every table checked value by value against y = px by sympy at build time; every choice's key and each wrong option checked from its error; every graph drawn from its equation by u7/figs7.py, which refuses a labeled point that is not on its line.",
               "Math Nation read for scope only (Croix, 20 Nov); nothing here is taken from it."],
        changes=["Built from the benchmark and the unit plan; no Math Nation item is reproduced."],
    ),
)
