# A7 7.04  Is It Proportional? — MA.7.AR.4.1 (with MA.8.AR.3.1). Fri 8 Jan 2027, 53 minutes; the last lesson is
# Thursday's 7.02+03 (the constant from a table, a graph and a description; negative constants), the next Monday's
# 7.05+06 (y = px; from one form to another). Built from the plan's section 7.04 (the unit's Lesson Outlines) and the
# benchmark's Source of Truth: the three tests in the unit's words — y ÷ x is the same for every pair; a straight line
# through the origin; nothing added at the start — and MA.8.AR.3.1 taught the same day: a linear relationship is also
# proportional only when its line passes through the origin (Unit 11's y = 2x + 3 against y = 2x). No cross products;
# "slope" and "y-intercept" are on no student page.
#
# Every check below is sympy: a table's ratios are y ÷ x row by row, exact (F('1.40') is 7/5); a table that is not
# proportional has more than one ratio; a description is tested at two values of its first quantity; a line through
# the origin gives 0 at x = 0. The figures are drawn by u7/figs7.py from their equations and points.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs7 as figs
S = figs.slide


def _q(v):
    return "F('" + str(v) + "')"


def ratios(xs, ys, p):
    """Every row of the table has y ÷ x = p."""
    return ("many",) + tuple(("eq", _q(y) + "/" + _q(x), p) for x, y in zip(xs, ys))


def not_prop(xs, ys):
    """The table's rows do not all have one ratio y ÷ x: the first row's ratio is not some later row's."""
    from fractions import Fraction as _F
    r = [_F(str(y)) / _F(str(x)) for x, y in zip(xs, ys)]
    k = next(i for i in range(1, len(r)) if r[i] != r[0])
    return ne(_q(ys[0]) + "/" + _q(xs[0]), _q(ys[k]) + "/" + _q(xs[k]))


def breaks(xs, ys, i, p):
    """Every row but row i has y ÷ x = p; row i does not."""
    return ("many",) + tuple(("eq" if k != i else "ne", _q(y) + "/" + _q(x), p) for k, (x, y) in enumerate(zip(xs, ys)))


def ne(a, b):
    return ("true", "sp.simplify((" + a + ") - (" + b + ")) != 0")


def fix_ne(c):
    """('ne', a, b) → a true-check that a is not b."""
    if c[0] == "ne":
        return ne(c[1], c[2])
    if c[0] == "many":
        return ("many",) + tuple(fix_ne(k) for k in c[1:])
    return c


def breaks_(xs, ys, i, p):
    return fix_ne(breaks(xs, ys, i, p))


def fee_rate(fee, rate):
    """A cost of fee + rate·n is not proportional: its ratio at n = 1 and n = 2 differ (fee > 0)."""
    return ne("(" + fee + " + " + rate + "*1)/1", "(" + fee + " + " + rate + "*2)/2")


def rate_only(rate):
    """A cost of rate·n is proportional: the ratio is rate at n = 1, 2 and 5."""
    return ("many",) + tuple(("eq", "(" + rate + "*" + str(n) + ")/" + str(n), rate) for n in (1, 2, 5))


def through0(m, b):
    """y = mx + b passes through the origin."""
    return ("eq", "(" + m + ")*0 + (" + b + ")", "0")


def misses0(m, b):
    """y = mx + b does not pass through the origin."""
    return ne("(" + m + ")*0 + (" + b + ")", "0")


# ---- figures: boards as large as the slide allows
def B(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.75)


def BA(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.95)


def T(spec, inches=7.0):
    return S(spec, inches=inches, pt=20, reserve=0.75)


def TA(spec, inches=6.0):
    return S(spec, inches=inches, pt=18, reserve=0.95)


# Notes I: two tables, one proportional and one going up by the same amount
NOTES1 = S(figs.row([figs.table([([5, 10, 15], [6, 12, 18])]), figs.table([([1, 2, 3], [5, 7, 9])])], gap=2.0),
           inches=9.6, pt=18, reserve=1.6)
# Notes II: the four pictures
# each cell half as tall as it is wide (figs7 `aspect`): with square cells the four tall planes were fitted to the
# slide's height and stood 5.7 in wide in all, their numbers and captions at 9 pt (the lead's look, 21 Nov 2026)
# the y-axes are numbered every second line (every third on the last, whose 9 rows stand as tall as the others' 8)
NOTES2 = S(figs.row([figs.plane((0, 4), (0, 8), lines=[figs.prop(2, "")], pt=18, aspect=0.5, ystep=2),
                     figs.plane((0, 4), (0, 8), lines=[(2, 3, "")], pt=18, aspect=0.5, ystep=2),
                     figs.plane((0, 4), (0, 8), curves=[figs.square(Fr(1, 2), 4)], pt=18, aspect=0.5, ystep=2),
                     figs.plane((0, 6), (0, 9), points=[(2, 3, ""), (4, 6, ""), (6, 9, "")], pt=18, aspect=Fr(4, 9), ystep=3)],
                    captions=["yes", "no: from (0, 3)", "no: a curve", "yes: extend it"], gap=2.0, pt=18),
           inches=12.0, pt=18, reserve=1.2)
# Notes III: y = 2x and y = 2x + 3 on one grid
NOTES3 = S(figs.plane((0, 3), (0, 10), lines=[figs.prop(2, None, (3, "r")), (2, 3, None, (2, "ul"))],
                      points=[(0, 0, ""), (1, 2, ""), (2, 4, ""), (0, 3, ""), (1, 5, ""), (2, 7, "")], inches=4.0, pt=18),
           inches=4.0, pt=18, reserve=0.9)

EX1 = T(figs.table([([4, 10, 12, 20], ["1.40", "3.50", "4.20", "6.00"])], head=("prints", "cost ($)"), cw=2.0), 8.0)
EX1W = S(figs.table([([4, 10, 12, 20], ["1.40", "3.50", "4.20", "6.00"])], head=("prints", "cost ($)"), cw=2.0),
         inches=5.0, pt=16, reserve=0.9)
YT1 = T(figs.table([([3, 5, 8], ["2.40", "4.00", "6.80"])], head=("feet", "cost ($)"), cw=2.0), 7.0)
YT1A = S(figs.table([([3, 5, 8], ["2.40", "4.00", "6.80"])], head=("feet", "cost ($)"), cw=2.0), inches=4.6, pt=14, reserve=0.9)

# ---- the boards
TB1 = figs.table([([2, 4, 8], [6, 12, 24])])
TB2 = figs.table([([2, 4, 8], [6, 8, 12])])
TB3 = figs.table([([1, 2, 3, 4], [4, 8, 12, 15])])
P4 = figs.plane((0, 6), (0, 10), lines=[(2, 1, "")], points=[(0, 1, ""), (2, 5, "")], inches=3.0, pt=18)
P5 = figs.plane((0, 12), (0, 16), xs=3, ys=4, points=[(3, 4, ""), (6, 8, ""), (9, 12, "")], inches=4.2, pt=18)
P5A = figs.plane((0, 12), (0, 16), xs=3, ys=4, lines=[figs.prop(Fr(4, 3), "")],
                 points=[(3, 4, ""), (6, 8, ""), (9, 12, "")], inches=4.2, pt=18)
# board 6: the graph of option C (the two tables are written in their options); tall, to stand beside the options
B6 = S(figs.plane((0, 4), (0, 6), lines=[figs.prop(Fr(3, 4), "")], points=[(4, 3, "on", "ul")], inches=2.4, pt=18),
       inches=2.4, pt=18, reserve=0.75)
B6A = S(figs.plane((0, 4), (0, 6), lines=[figs.prop(Fr(3, 4), "")], points=[(4, 3, "on", "ul")], inches=2.0, pt=18),
        inches=2.0, pt=18, reserve=1.3)
# y counts by 2, so the 2 that y = 5x − 2 is short of the origin is one whole square (by 4 it was half a square)
P8 = figs.row([figs.plane((-2, 2), (-6, 6), ys=2, lines=[(5, -2, ""), figs.prop(5, "")], pt=18)],
              titles=[[("y = 5x − 2", figs.BLUE), ("y = 5x", figs.ORANGE)]], pt=18, inches=3.4)

# ---- the Independent Set and the banks (paper size)
IS4 = figs.row([figs.table([([3, 5, 8], [12, 20, 32])]), figs.table([([2, 4, 6], [3, 6, 10])]),
                figs.plane((0, 6), (0, 9), lines=[(1, 3, "")], points=[(0, 3, "on", "dr"), (3, 6, "on", "ul")])],
               titles=["first table", "second table", "the graph"], gap=2.0, inches=6.4)
IS5 = figs.plane((0, 6), (0, 12), ys=2, lines=[(1, 4, "A", (5, "dr")), figs.prop(2, "B", (5, "ul"))], inches=3.0)

L = dict(
    code="7.04", unit=7, lesson_no=4,
    title="Is It Proportional?",
    unit_title="Representing Proportional Relationships",
    benchmark="MA.7.AR.4.1",
    benchmark_text="Determine whether two quantities have a proportional relationship by examining a table, graph or written description.",
    benchmarks=[("MA.7.AR.4.1", "Determine whether two quantities have a proportional relationship by examining a table, graph or written description."),
                ("MA.8.AR.3.1", "Determine if a linear relationship is also a proportional relationship.")],
    target="I can decide from a table, a graph or a description whether a relationship is proportional, and whether a linear relationship is also proportional.",
    essential="What do a table, a graph and a description each show when one quantity is always a constant multiple of the other?",
    building_on="Lessons 7.02–03 found the constant of proportionality from a table, a graph and a description, and lesson 7.01 graphed y = px. In Unit 11, students graphed lines such as y = 2x + 3 from a table of values. In Grade 6 (MA.6.AR.3), they worked with equivalent ratios.",
    working_toward="Lessons 7.05–06 write equations y = px and translate between representations. Grade 8 (MA.8.AR.3) studies linear relationships, and Unit 10 (January) introduces slope.",
    vocab=[("linear relationship", "a relationship whose graph is a straight line, such as $y = 2x + 3$"),
           ("proportional relationship", "two quantities are in a proportional relationship when one quantity is always a constant multiple of the other: $y = px$; its graph is a straight line through the origin")],
    ixl=["Identify proportional relationships by graphing — AAN", "Identify proportional relationships in tables and graphs — VZK"],
    closure="Whiteboard question 9 is answered in writing and serves as the exit ticket. A complete answer gives a line such as y = x + 4, which is straight but gives 4 when x is 0. It passes through (0, 4), not the origin, so it is not proportional and Sam is wrong. An answer that gives a line without a reason has the example but not the proof.",

    mtr=[("MTR.4.1", "On whiteboard questions 3 and 5, students convince a neighbor and then vote again."),
         ("MTR.2.1", "Students apply one test in three forms: to a table, to a graph and to a description."),
         ("MTR.6.1", "Students test every pair in a table, not only the first three.")],
    hoq=[("Why is testing the first three pairs of a table not enough?", "DOK 2"),
         ("The points are on a line, but (0, 0) is not plotted. How can you still tell whether it is proportional?", "DOK 2"),
         ("y = 2x and y = 2x + 3 are both straight lines. Why is only one of them proportional?", "DOK 3"),
         ("A tub starts with 10 gallons. Why does that make the gallons not proportional to the minutes?", "DOK 2")],
    differentiation=[
        ("ESE / 504", "Place a printed card with the three tests on the desk. Table: y ÷ x is the same for every pair. Graph: a straight line that also passes through the origin. Description: nothing is added at the start. Students also draw a ÷ row under every table on their whiteboards."),
        ("ELL", "**Proportional**: one amount is always the same number times the other. **Origin**: the point (0, 0). **Every pair**: all of them, not some. **Fee / to start**: money added before anything is used."),
        ("Enrichment", "For students who finish whiteboard question 6 early: change one number in the second table (x = 1, 2, 3 and y = 3, 5, 7) so that it is proportional, and tell which other numbers must change too. (No single change works: y = 3, 6, 9 makes y ÷ x equal 3 for every pair, so two y-values must change.)")],

    warmup=[
        dict(stem="Find the constant of proportionality for (4, 6) and (10, 15).", answer="1.5",
             check=ratios([4, 6, 10], [6, 9, 15], "F(3,2)")),
        dict(stem="Is $(4, 12)$ on the graph of $y = 3x$?", answer="Yes",
             check=("eq", "3*4", "12")),
        dict(stem="Is $(2, 5)$ a solution of  $y = 2x + 1$  and  $y = x + 3$?", answer="Yes",
             check=("many", ("eq", "2*2 + 1", "5"), ("eq", "2 + 3", "5"))),
        dict(stem="Are $\\frac{12}{8}$ and $\\frac{15}{10}$ equal?", answer="Yes. Both equal 1.5.",
             check=("many", ("eq", "F(12,8)", "F(3,2)"), ("eq", "F(15,10)", "F(3,2)"))),
    ],

    notes=[
        dict(numeral="I", head="The table test: check every pair", min=3,
             fig=NOTES1,
             items2=["Left:   $6 \\div 5 = 1.2$,   $12 \\div 10 = 1.2$,   $18 \\div 15 = 1.2$.   Proportional.",
                     "**y ÷ x is the same for every pair.**",
                     "Right:   $5 \\div 1 = 5$,   $7 \\div 2 = 3.5$,   $9 \\div 3 = 3$.   Not proportional.",
                     "**Going up by the same amount does not make y ÷ x the same.**"],
             letters=False),
        dict(numeral="II", head="The graph test: two conditions", min=3,
             fig=NOTES2,
             items2=["**The graph must be a straight line, and it must pass through the origin.**",
                     "$(2, 3)$,  $(4, 6)$,  $(6, 9)$:  extend the line, and it reaches $(0, 0)$."],
             letters=False),
        # each line fits on one line of the slide: wrapped, the first two ran together and the third stood apart
        dict(numeral="III", head="Nothing added at the start", min=3,
             items=[("A description", "a constant rate with nothing added at the start"),
                    ("y = 2x", "at x = 0, y = 0: through the origin. Proportional."),
                    ("y = 2x + 3", "at x = 0, y = 3: 3 is added. Not proportional.")],
             items2=["**A linear relationship with nothing added is proportional: $y = px$.**"],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=1,
             prompt=["The table shows the cost of photo prints."], fig=EX1,
             ask="Is the cost proportional to the number of prints?",
             worked=[dict(min=3,
                          rows=[("1.40 \\div 4 = 0.35,\\quad 3.50 \\div 10 = 0.35", "the first two pairs"),
                                ("4.20 \\div 12 = 0.35", "the third pair"),
                                ("6.00 \\div 20 = 0.30", "the last pair breaks it"),
                                ("0.35(20) = 7.00", "what 20 prints would have to cost")],
                          fig=EX1W, answer="No. 20 prints would have to cost \\$7.00.")],
             check=("many", breaks_([4, 10, 12, 20], ["1.40", "3.50", "4.20", "6.00"], 3, "F(35,100)"),
                    ("eq", "F('6.00')/20", "F(3,10)"), ("eq", "F(35,100)*20", "7")),
             your_turn=dict(min=3,
                            prompt=["The table shows the cost of rope."], fig=YT1, fig_a=YT1A,
                            ask="Is the cost proportional to the length?",
                            steps=["$2.40 \\div 3 = 0.80$", "$4.00 \\div 5 = 0.80$",
                                   "$6.80 \\div 8 = 0.85$:  not 0.80", "$0.80(8) = 6.40$"],
                            answer="No. 8 feet would have to cost \\$6.40."),
             yt_check=("many", breaks_([3, 5, 8], ["2.40", "4.00", "6.80"], 2, "F(8,10)"),
                       ("eq", "F('6.80')/8", "F(85,100)"), ("eq", "F(8,10)*8", "F('6.40')"))),
        dict(title="Example 2", min_q=1,
             prompt=["A taxi charges \\$4 to start plus \\$3 per mile. Is the cost proportional to the number of miles?",
                     "A bus charges \\$2 per ride. Is the cost proportional to the number of rides?"],
             ask="",
             worked=[dict(min=2,
                          rows=[("\\text{taxi: }0\\text{ miles}: 4,\\quad 1\\text{ mile}: 7,\\quad 2\\text{ miles}: 10", "the taxi, in dollars"),
                                ("\\text{taxi: }7 \\div 1 = 7,\\quad 10 \\div 2 = 5", "not the same: \\$4 added at the start"),
                                ("\\text{bus: }2 \\div 1 = 2,\\quad 4 \\div 2 = 2,\\quad 6 \\div 3 = 2", "the bus: \\$2 per ride, nothing added at the start"),
                                ("\\text{taxi: \\$4 added at the start}", "the reason, the taxi"),
                                ("\\text{bus: nothing added at the start}", "the reason, the bus")],
                          answer="Taxi: no. Bus: yes.")],
             check=("many", ("eq", "4 + 3*0", "4"), ("eq", "4 + 3*1", "7"), ("eq", "4 + 3*2", "10"), fee_rate("4", "3"),
                    rate_only("2")),
             your_turn=dict(min=2,
                            prompt=["A gym charges a \\$40 joining fee plus \\$25 per month. Is the cost proportional to the number of months?",
                                    "A phone plan charges \\$0.10 per text. Is the cost proportional to the number of texts?"],
                            ask="",
                            steps=["gym:  $65 \\div 1 = 65$,  $90 \\div 2 = 45$:   \\$40 added at the start",
                                   "phone plan:  $0.10 \\div 1 = 0.10$,  $0.20 \\div 2 = 0.10$:   nothing added at the start"],
                            answer="Gym: no. Phone plan: yes."),
             yt_check=("many", ("eq", "40 + 25*1", "65"), ("eq", "40 + 25*2", "90"), fee_rate("40", "25"),
                       rate_only("F(1,10)"))),
    ],

    # The round: a table that is (1); one feature changed, the y's — not (2); a vote on a table with one row off (3);
    # a straight line that misses the origin (4); a vote on points with no point plotted at the origin, the y-axis
    # scaled by 4 (5); a select-all across the three representations (6); the notebook story, its 50 pages the extra
    # number (7); linear against proportional on one grid (8); the counterexample, written (9).
    whiteboard=[
        dict(text=["**Is y proportional to x?"], fig=T(TB1), fig_a=TA(TB1),
             qtext="The table: x 2, 4, 8; y 6, 12, 24. Is y proportional to x?",
             steps=["$6 \\div 2 = 3$,   $12 \\div 4 = 3$,   $24 \\div 8 = 3$", "the same for every pair"],
             answer="Yes. y ÷ x is 3 for every pair.",
             check=ratios([2, 4, 8], [6, 12, 24], "3"),
             wrong="no — 'the y's do not go up by the same amount' (6, then 12) [benchmark: a constant difference taken for the test]; yes — 'they go up' with no ratio [benchmark misconception: rising taken for proportional]"),
        dict(text=["**Is y proportional to x?"], fig=T(TB2), fig_a=TA(TB2),
             qtext="The table: x 2, 4, 8; y 6, 8, 12. Is y proportional to x?",
             steps=["$6 \\div 2 = 3$,   $8 \\div 4 = 2$,   $12 \\div 8 = 1.5$", "not the same for every pair"],
             answer="No. y ÷ x is 3, 2 and 1.5.",
             check=("many", not_prop([2, 4, 8], [6, 8, 12]), ("eq", "F(6,2)", "3"), ("eq", "F(8,4)", "2"), ("eq", "F(12,8)", "F(3,2)")),
             wrong="yes — the first pair's 3 taken for the table [benchmark misconception: not testing every pair]; yes — 'both go up' [benchmark misconception: rising taken for proportional]"),
        dict(kind="mc", text=["**Is y proportional to x?"], fig=S(TB3, inches=4.4, pt=18, reserve=0.75), fig_a=S(TB3, inches=4.4, pt=18, reserve=0.95),
             qtext="The table: x 1, 2, 3, 4; y 4, 8, 12, 15. Is y proportional to x?",
             steps=["$4 \\div 1 = 4$,   $8 \\div 2 = 4$,   $12 \\div 3 = 4$", "$15 \\div 4 = 3.75$:   the last pair breaks it"],
             choices=["No. It does not start at 0.", "Yes. y goes up with x.", "Yes. The first three give 4.", "No. 15 ÷ 4 is not 4."],
             correct=3, answer="D — No. 15 ÷ 4 is not 4.",
             errors={"A": "the pair (0, 0) taken as required in the table [benchmark misconception: the origin not shown]", "B": "y rising with x taken for proportional [Notes I: going up by the same amount does not make y ÷ x the same]", "C": "three pairs tested, not the fourth [benchmark misconception: not testing every pair]"},
             check=("many", breaks_([1, 2, 3, 4], [4, 8, 12, 15], 3, "4"), ("eq", "F(15,4)", "F(15,4)"))),
        dict(text=["**A line passes through $(0, 1)$ and $(2, 5)$. Is it proportional?"],
             fig=S(P4, inches=3.0, pt=18, reserve=0.75), fig_a=S(P4, inches=3.0, pt=18, reserve=1.3),
             qtext="A graph: a straight line through (0, 1) and (2, 5). Is the relationship proportional?",
             steps=["at $x = 0$, $y = 1$:   not through the origin"],
             answer="No. It does not pass through the origin.",
             check=("many", ("eq", "(5 - 1)/(2 - 0)", "2"), misses0("2", "1")),
             wrong="yes — a straight line taken for proportional [benchmark misconception: every straight line is proportional]; yes — 5 ÷ 2 read as a constant 2.5 from one point [benchmark misconception: not testing every point]"),
        dict(kind="mc", text=["The graph shows three points.", "**Is the relationship proportional?"],
             qtext="A graph whose y-axis counts by 4: the points (3, 4), (6, 8) and (9, 12), no point at the origin. Is the relationship proportional?",
             fig=B(P5), fig_a=BA(P5A),
             steps=["Read the scales first:   $(3, 4)$,  $(6, 8)$,  $(9, 12)$",
                    "$4 \\div 3$,   $8 \\div 6$,   $12 \\div 9$:   all $\\frac{4}{3}$",
                    "Their line passes through $(0, 0)$."],
             choices=["No. (0, 0) is not plotted.", "Yes. The points go up.", "Yes. The line passes through (0, 0).", "No. y is not a whole number times x."],
             correct=2, answer="C — Yes. It passes through (0, 0).",
             errors={"A": "the origin taken as missing because it is not plotted [benchmark misconception: the origin not shown]", "B": "rising taken for proportional [Notes I: going up by the same amount does not make y ÷ x the same]", "D": "the constant thought to be a whole number: 4/3 is a constant too [Notes I: y ÷ x is the same for every pair]"},
             check=("many", ratios([3, 6, 9], [4, 8, 12], "F(4,3)"), ("true", "not F(4,3).is_integer"))),
        dict(kind="mc", text=["**Select all the proportional relationships."],
             qtext="Select all the proportional relationships: the table x 3, 6, 9; y 7, 14, 21; the table x 1, 2, 3; y 3, 5, 7; the graph (a line through the origin and (4, 3)); a tub that starts with 10 gallons and gains 4 each minute: the gallons and the minutes; parking that costs $3 per hour: the cost and the hours.",
             fig=B6, fig_a=B6A,
             steps=["A:   $7 \\div 3 = 14 \\div 6 = 21 \\div 9$",
                    "B:   $3 \\div 1 = 3$,   $5 \\div 2 = 2.5$",
                    "C:  a straight line through the origin",
                    "D:  10 gallons at the start",
                    "E:  nothing added at the start"],
             choices=["x: 3, 6, 9;  y: 7, 14, 21", "x: 1, 2, 3;  y: 3, 5, 7", "the graph", "A tub starts with 10 gallons and gains 4 per minute.",
                      "Parking costs \\$3 per hour."],
             correct=[0, 2, 4], answer="A, C, E",
             errors={"B": "a constant difference (up 2 each time) taken for a constant ratio [Notes I: going up by the same amount does not make y ÷ x the same]",
                     "D": "the 10 gallons at the start ignored: a constant rate taken for proportional [Notes III: nothing added at the start]"},
             check=("many", ratios([3, 6, 9], [7, 14, 21], "F(7,3)"), through0("F(3,4)", "0"), ("eq", "F(3,4)*4", "3"),
                    rate_only("3"), not_prop([1, 2, 3], [3, 5, 7]), fee_rate("10", "4"))),
        dict(text=["A 50-page notebook costs \\$3.",
                   "**Is the cost proportional to the number of notebooks? If so, find the constant of proportionality."],
             unneeded="50",
             steps=["1 notebook:  \\$3;   2:  \\$6;   5:  \\$15", "$6 \\div 2 = 3$,  $15 \\div 5 = 3$:  nothing added at the start"],
             answer="Yes. The constant is 3 dollars per notebook.",
             check=rate_only("3"),
             wrong="0.06 — 3 ÷ 50, the pages used [an extra number, included on purpose]; 50 — the pages taken for the cost [an extra number, included on purpose]; 1/3 — notebooks per dollar, the ratio reversed [benchmark misconception: variables reversed]"),
        # repeat_ok: rule 43 matches only this grid's axis numbers (y by 2 from −6 to 6) and the answer's digits against
        # the numbers on Notes II and Example 2; the two lines y = 5x and y = 5x − 2 are on no other slide
        dict(text=["**Both relationships are linear. Which one is also proportional?"], fig=S(P8, inches=3.4, pt=18, reserve=0.75), fig_a=S(P8, inches=3.4, pt=18, reserve=1.3),
             repeat_ok=True,
             qtext="y = 5x − 2 and y = 5x are drawn on one grid. Both relationships are linear. Which one is also proportional?",
             steps=["$y = 5x$:   at $x = 0$, $5(0) = 0$:   through the origin",
                    "$y = 5x - 2$:   at $x = 0$, $5(0) - 2 = -2$"],
             answer="y = 5x. The other gives −2 when x is 0.",
             check=("many", through0("5", "0"), misses0("5", "-2"), ("eq", "5*0 - 2", "-2")),
             wrong="both — every straight line taken as proportional [benchmark misconception: every straight line is proportional]; y = 5x − 2 — the line with more numbers in it taken as the proportional one [Notes III: nothing added]"),
        dict(kind="written", text=["Sam says every straight-line graph shows a proportional relationship.",
                                   "**Give a line that proves him wrong, and explain why."],
             qtext="Sam says every straight-line graph shows a proportional relationship. Give a line that proves him wrong, and explain why.",
             steps=["$y = x + 4$:   a straight line", "at $x = 0$, $0 + 4 = 4$:   it passes through $(0, 4)$, not the origin"],
             answer="y = x + 4, for example: a straight line through (0, 4), not the origin.",
             check=("many", misses0("1", "4"), ("eq", "0 + 4", "4")),
             wrong="y = 2x — a line through the origin, which agrees with Sam [Notes III: linear and proportional]; 'a curve' — not a straight line, so it does not answer Sam [Notes II: two conditions]"),
    ],

    # The six: a table that is (1); a constant difference (2); one row off — which row, and what it would have to be
    # (3); the pattern breaks — a select-all from five, two tables, a graph and two descriptions, two of them
    # proportional (4); two lines on one grid, one through the origin (5); linear and not proportional, from an
    # equation (6).
    independent=[
        dict(stem="Is y proportional to x? Explain.",
             fig=figs.table([([2, 6, 9], [13, 39, "58.5"])], inches=3.4),
             answer="Yes. y ÷ x is 6.5 for every pair.", why="13 ÷ 2 = 6.5, 39 ÷ 6 = 6.5, 58.5 ÷ 9 = 6.5: the same for every pair.",
             check=ratios([2, 6, 9], [13, 39, "58.5"], "F(13,2)"), space=0.6),
        dict(stem="Is y proportional to x? Explain.",
             fig=figs.table([([1, 2, 3, 4], [6, 10, 14, 18])], inches=4.0),
             answer="No. 6 ÷ 1 = 6, but 10 ÷ 2 = 5.", why="y goes up by 4 each time, but y ÷ x is 6, 5, 4.67, 4.5: not the same for every pair.",
             check=("many", not_prop([1, 2, 3, 4], [6, 10, 14, 18]), ("eq", "F(6,1)", "6"), ("eq", "F(10,2)", "5")), space=0.6),
        dict(stem="The table shows the cost of lemons. One cost does not fit the pattern. Which cost is it, and what should it be?",
             fig=figs.table([([2, 3, 5, 6], ["1.80", "2.70", "4.75", "5.40"])], head=("lemons", "cost ($)"), cw=2.0, inches=5.0),
             answer="The cost of 5 lemons. It should be \\$4.50.", why="1.80 ÷ 2 = 0.90, 2.70 ÷ 3 = 0.90, 5.40 ÷ 6 = 0.90, but 4.75 ÷ 5 = 0.95. At 0.90 per lemon, 5 lemons cost 0.90(5) = \\$4.50.",
             check=("many", breaks_([2, 3, 5, 6], ["1.80", "2.70", "4.75", "5.40"], 2, "F(9,10)"), ("eq", "F(9,10)*5", "F('4.50')")),
             space=0.8),
        dict(stem="Select all the proportional relationships.",
             fig=IS4,
             choices=["the first table", "the second table", "the graph",
                      "A bakery sells muffins for \\$1.25 each (total cost and number of muffins).",
                      "A bike rental charges \\$8 plus \\$5 per hour (total cost and number of hours)."],
             correct=[0, 3], answer="A, D",
             why="A: 12 ÷ 3 = 20 ÷ 5 = 32 ÷ 8 = 4. D: \\$1.25 per muffin, nothing added at the start. B: 3 ÷ 2 = 1.5, but 10 ÷ 6 is not 1.5. The graph is straight but starts at (0, 3). E: \\$8 added at the start.",
             errors={"B": "the first two pairs tested, not the last [benchmark misconception: not testing every pair]",
                     "C": "a straight line taken for proportional [benchmark misconception: every straight line is proportional]",
                     "E": "the \\$8 at the start ignored [Notes III: nothing added at the start]"},
             check=("many", ratios([3, 5, 8], [12, 20, 32], "4"), rate_only("F(5,4)"),
                    ratios([2, 4], [3, 6], "F(3,2)"), ne("F(10,6)", "F(3,2)"), misses0("1", "3"), ("eq", "0 + 3", "3"), ("eq", "3 + 3", "6"),
                    fee_rate("8", "5"))),
        dict(stem="Lines A and B show two linear relationships. Which one is also proportional? Explain.",
             fig=IS5,
             answer="B. It passes through the origin.", why="B passes through (0, 0); A crosses the y-axis at 4, so at x = 0 it gives 4, not 0.",
             check=("many", through0("2", "0"), misses0("1", "4")), space=0.6),
        dict(stem="The relationship $y = 4x + 1$ is linear. Is it also proportional? Explain.",
             answer="No. When x is 0, y is 1, so its line does not pass through the origin.",
             why="4(0) + 1 = 1, so the line passes through (0, 1), not (0, 0); 1 is added.",
             check=("many", misses0("4", "1"), ("eq", "4*0 + 1", "1")), space=0.6),
    ],

    # Bank: two tables, yes and no (1–2); a row off (3); three graphs — through the origin, missing it, points with no
    # origin plotted (4–6); two descriptions (7–8); linear and also proportional, a choice and from an equation
    # (9–10); a select-all of descriptions (11); an error to find (12). The additional bank mirrors it.
    bank=[
        dict(heading="Is y proportional to x? Explain."),
        dict(stem="", fig=figs.table([([3, 6, 12], [4, 8, 16])], inches=3.4),
             answer="Yes. y ÷ x is 4/3 for every pair.", why="4 ÷ 3, 8 ÷ 6 and 16 ÷ 12 are all 4/3.",
             check=ratios([3, 6, 12], [4, 8, 16], "F(4,3)"), space=0.5),
        dict(stem="", fig=figs.table([([2, 3, 4], [9, 13, 17])], inches=3.4),
             answer="No. 9 ÷ 2 = 4.5, but 17 ÷ 4 = 4.25.", why="y goes up by 4 each time, but the ratios are 4.5, 4.33 and 4.25.",
             check=("many", not_prop([2, 3, 4], [9, 13, 17]), ("eq", "F(9,2)", "F(9,2)"), ("eq", "F(17,4)", "F(17,4)")), space=0.5),
        dict(heading="One value does not fit the pattern. Which value is it, and what should it be?"),
        dict(stem="The table shows the miles a cyclist rode.",
             fig=figs.table([([3, 4, 6, 9], [36, 48, 70, 108])], head=("hours", "miles"), inches=4.4),
             answer="The miles for 6 hours. It should be 72 miles.", why="36 ÷ 3 = 48 ÷ 4 = 108 ÷ 9 = 12, but 70 ÷ 6 is not 12; 12(6) = 72.",
             check=("many", breaks_([3, 4, 6, 9], [36, 48, 70, 108], 2, "12"), ("eq", "12*6", "72")), space=0.6),
        dict(heading="Is the relationship proportional? Explain."),
        dict(stem="", fig=figs.plane((0, 4), (0, 10), ys=5, lines=[figs.prop(Fr(5, 2), "")], points=[(2, 5, "on", "ul")], inches=2.6),
             answer="Yes. It is a straight line through the origin.", why="The line is straight and passes through (0, 0).",
             check=("many", through0("F(5,2)", "0"), ("eq", "F(5,2)*2", "5")), space=0.4),
        dict(stem="", fig=figs.plane((0, 8), (0, 8), lines=[(Fr(1, 2), 4, "")], points=[(0, 4, "on", "dr"), (4, 6, "on", "ul")], inches=2.6),
             answer="No. It does not pass through the origin.", why="The line is straight but crosses the y-axis at 4: at x = 0, y is 4.",
             check=("many", misses0("F(1,2)", "4"), ("eq", "F(1,2)*4 + 4", "6")), space=0.4),
        dict(stem="", fig=figs.plane((0, 10), (0, 8), ys=2, points=[(3, 2, ""), (6, 4, ""), (9, 6, "")], inches=2.6),
             answer="Yes. The points lie on a line that passes through (0, 0).", why="(3, 2), (6, 4), (9, 6): y ÷ x is 2/3 each time, and their line passes through the origin.",
             check=ratios([3, 6, 9], [2, 4, 6], "F(2,3)"), space=0.4),
        dict(heading="Is the relationship proportional? Explain."),
        dict(stem="A plant is 6 cm tall and grows 2 cm each week (height and number of weeks).",
             answer="No. It starts at 6 cm.", why="After 1 week 8 cm, after 2 weeks 10 cm: 8 ÷ 1 = 8 and 10 ÷ 2 = 5.",
             check=fee_rate("6", "2"), space=0.4),
        dict(stem="A car wash cleans 12 cars each hour (cars washed and number of hours).",
             answer="Yes. 12 cars per hour, with nothing added at the start.", why="1 hour 12 cars, 2 hours 24, 5 hours 60: y ÷ x is 12.",
             check=rate_only("12"), space=0.4),
        dict(heading="Linear, and also proportional?"),
        dict(stem="Each relationship is linear. Which one is also proportional?",
             choices=["$y = 7x + 1$", "$y = 7x$", "$y = 7$", "$y = x + 7$"], correct=1, answer="B",
             why="Only y = 7x gives 0 at x = 0; the others give 1, 7 and 7.",
             check=("many", through0("7", "0"), misses0("7", "1"), misses0("1", "7"), misses0("0", "7")),
             errors={"A": "the 1 added ignored [Notes III: nothing added]", "C": "y the same every time taken for y ÷ x the same [Notes I: y ÷ x is the same for every pair]", "D": "7 read as the constant though it is added [Notes III: nothing added]"}),
        dict(stem="The relationship $y = 3x - 6$ is linear. Is it also proportional? Explain.",
             answer="No. When x is 0, y is −6.", why="3(0) − 6 = −6: the line passes through (0, −6), not the origin.",
             check=("many", misses0("3", "-6"), ("eq", "3*0 - 6", "-6")), space=0.5),
        dict(heading="Select all that apply."),
        dict(stem="Select all the proportional relationships.",
             choices=["Each row of a garden has 8 plants (plants and rows).", "A faucet drips 0.2 liter each hour (water dripped and hours).", "A candle is 20 cm tall and burns 2 cm each hour (height and hours).", "A locksmith charges \\$35 for the visit plus \\$20 per lock (cost and locks).", "A museum charges \\$12 per visitor (total cost and visitors)."],
             correct=[0, 1, 4], answer="A, B, E",
             why="A, B and E: the same number for each one, nothing added at the start. D: \\$35 at the start. C: 20 cm at the start, and the height goes down.",
             check=("many", rate_only("12"), rate_only("F(2,10)"), rate_only("8"), fee_rate("35", "20"), fee_rate("20", "-2")),
             errors={"C": "a constant 2 cm an hour taken for proportional [Notes III: nothing added at the start]", "D": "the \\$35 visit ignored [Notes III: nothing added at the start]"}),
        dict(heading="Find the error."),
        dict(stem="Jada tested a table with x-values 1, 2 and 3 and y-values 5, 10 and 16. She wrote 5 ÷ 1 = 5 and 10 ÷ 2 = 5 and said it is proportional. Is she right? Explain.",
             answer="No. 16 ÷ 3 is not 5, and y ÷ x must be the same for every pair.", why="The third y-value would have to be 15.",
             check=("many", breaks_([1, 2, 3], [5, 10, 16], 2, "5"), ("eq", "5*3", "15")), space=0.6),
    ],

    additional=[
        dict(heading="Is y proportional to x? Explain."),
        dict(stem="", fig=figs.table([([4, 8, 10], [3, 6, "7.5"])], inches=3.4),
             answer="Yes. y ÷ x is 0.75 for every pair.", why="3 ÷ 4, 6 ÷ 8 and 7.5 ÷ 10 are all 0.75.",
             check=ratios([4, 8, 10], [3, 6, "7.5"], "F(3,4)"), space=0.5),
        dict(stem="", fig=figs.table([([3, 4, 5], [7, 9, 11])], inches=3.4),
             answer="No. 9 ÷ 4 = 2.25, but 11 ÷ 5 = 2.2.", why="y goes up by 2 each time, but the ratios are 2.33, 2.25 and 2.2.",
             check=("many", not_prop([3, 4, 5], [7, 9, 11]), ("eq", "F(9,4)", "F(225,100)"), ("eq", "F(11,5)", "F(22,10)")), space=0.5),
        dict(heading="One value does not fit the pattern. Which value is it, and what should it be?"),
        dict(stem="The table shows the minutes a swimmer took for her laps.",
             fig=figs.table([([2, 5, 7, 10], [6, 15, 22, 30])], head=("laps", "minutes"), inches=4.4),
             answer="The minutes for 7 laps. It should be 21 minutes.", why="6 ÷ 2 = 15 ÷ 5 = 30 ÷ 10 = 3, but 22 ÷ 7 is not 3; 3(7) = 21.",
             check=("many", breaks_([2, 5, 7, 10], [6, 15, 22, 30], 2, "3"), ("eq", "3*7", "21")), space=0.6),
        dict(heading="Is the relationship proportional? Explain."),
        dict(stem="", fig=figs.plane((0, 6), (0, 8), ys=2, lines=[figs.prop(Fr(4, 3), "")], points=[(3, 4, "on", "ul")], inches=2.6),
             answer="Yes. It is a straight line through the origin.", why="The line is straight and passes through (0, 0).",
             check=("many", through0("F(4,3)", "0"), ("eq", "F(4,3)*3", "4")), space=0.4),
        dict(stem="", fig=figs.plane((0, 6), (0, 12), ys=2, lines=[(1, 6, "")], points=[(0, 6, "on", "dr"), (4, 10, "on", "ul")], inches=2.6),
             answer="No. It does not pass through the origin.", why="The line is straight but crosses the y-axis at 6: at x = 0, y is 6.",
             check=("many", misses0("1", "6"), ("eq", "4 + 6", "10")), space=0.4),
        dict(stem="", fig=figs.plane((0, 14), (0, 4), xs=2, points=[(4, 1, ""), (8, 2, ""), (12, 3, "")], inches=2.6),
             answer="Yes. The points lie on a line that passes through (0, 0).", why="(4, 1), (8, 2), (12, 3): y ÷ x is 0.25 each time, and their line passes through the origin.",
             check=ratios([4, 8, 12], [1, 2, 3], "F(1,4)"), space=0.4),
        dict(heading="Is the relationship proportional? Explain."),
        dict(stem="A pool holds 300 gallons and drains 25 gallons each minute (gallons left and minutes).",
             answer="No. It starts at 300 gallons.", why="After 1 minute 275 gallons, after 2 minutes 250: 275 ÷ 1 = 275 and 250 ÷ 2 = 125.",
             check=fee_rate("300", "-25"), space=0.4),
        dict(stem="A machine fills 45 bottles each minute (bottles filled and minutes).",
             answer="Yes. 45 bottles per minute, with nothing added at the start.", why="1 minute 45 bottles, 2 minutes 90, 5 minutes 225: y ÷ x is 45.",
             check=rate_only("45"), space=0.4),
        dict(heading="Linear, and also proportional?"),
        dict(stem="Each relationship is linear. Which one is also proportional?",
             choices=["$y = 6x$", "$y = 6$", "$y = x + 6$", "$y = 6x - 2$"], correct=0, answer="A",
             why="Only y = 6x gives 0 at x = 0; the others give −2, 6 and 6.",
             check=("many", through0("6", "0"), misses0("6", "-2"), misses0("0", "6"), misses0("1", "6")),
             errors={"B": "y the same every time taken for y ÷ x the same [Notes I: y ÷ x is the same for every pair]", "C": "6 read as the constant though it is added [Notes III: nothing added]", "D": "the 2 taken away ignored [Notes III: nothing added]"}),
        dict(stem="The relationship $y = 2x + 5$ is linear. Is it also proportional? Explain.",
             answer="No. When x is 0, y is 5.", why="2(0) + 5 = 5: the line passes through (0, 5), not the origin.",
             check=("many", misses0("2", "5"), ("eq", "2*0 + 5", "5")), space=0.5),
        dict(heading="Select all that apply."),
        dict(stem="Select all the proportional relationships.",
             choices=["A recipe uses 3 cups of flour per batch (cups and batches).", "A tutor charges \\$30 per hour (cost and hours).", "A tank holds 50 liters and loses 2 liters each day (water left and days).", "Each box holds 24 crayons (crayons and boxes).", "A delivery costs \\$5 plus \\$2 per mile (cost and miles)."],
             correct=[0, 1, 3], answer="A, B, D",
             why="A, B and D: the same number for each one, nothing added at the start. E: \\$5 at the start. C: 50 liters at the start, and the water goes down.",
             check=("many", rate_only("30"), rate_only("3"), rate_only("24"), fee_rate("5", "2"), fee_rate("50", "-2")),
             errors={"C": "a constant 2 liters a day taken for proportional [Notes III: nothing added at the start]", "E": "the \\$5 at the start ignored [Notes III: nothing added at the start]"}),
        dict(heading="Find the error."),
        dict(stem="Ravi tested a table with x-values 2, 4 and 6 and y-values 9, 18 and 26. He wrote 9 ÷ 2 = 4.5 and 18 ÷ 4 = 4.5 and said it is proportional. Is he right? Explain.",
             answer="No. 26 ÷ 6 is not 4.5, and y ÷ x must be the same for every pair.", why="The third y-value would have to be 27.",
             check=("many", breaks_([2, 4, 6], [9, 18, 26], 2, "F(9,2)"), ("eq", "F(9,2)*6", "27")), space=0.6),
    ],

    te=dict(
        must="Students decide from a table, a graph or a description whether a relationship is proportional, and they give the reason: a constant ratio, or a line through the origin (MA.7.AR.4.1). They also determine whether a linear relationship is a proportional relationship (MA.8.AR.3.1).",
        must_not="Students do not write equations today; that belongs to MA.7.AR.4.2–4.4. Slope and y = mx + b are not taught. The only equations are the linear contrast from MA.8.AR.3.1 (y = 2x versus y = 2x + 3), and cross products are not used.",
        read_first=[
            "The unit's fourth day. Built from the plan's section 7.04 (the unit's Lesson Outlines) and the benchmark's Source of Truth. The title slide names MA.7.AR.4.1; MA.8.AR.3.1 is taught the same day (Notes III, board 8, Independent Set 5–6, bank 9–10).",
            "The three tests in the unit's words, said the same way all period: y ÷ x is the same for every pair; a straight line through the origin; nothing added at the start. Ratios are tested with y ÷ x, never cross products (the state: they may lead to errors). Say slope here if you like; the slides do not.",
            "The state's named misconceptions are the wrong options: the origin not shown (board 5), every straight line proportional (boards 4, 8, 9), not testing every pair (board 3), rising taken for proportional."],
        materials="Whiteboards and markers. The Independent Set, one per student.",
        variation="Boards 1–2 are tables, one feature changed (the y's): yes, then no. 3 votes on a table with only its last pair off; 4 is a straight line that misses the origin; 5 votes on points with no point at the origin, the y-axis scaled by 4. The pattern breaks at 6 — a select-all across tables, a graph and descriptions; 7 is the notebook story, its 50 pages the extra number; 8 is linear versus proportional on one grid; 9 is written. The independent set: a table that is, a constant difference, one pair off, a select-all of five, two lines, and an equation.",
        audit=["Every ratio re-derived by sympy at build time as an exact y ÷ x, pair by pair; every table that is not proportional shown to have more than one ratio; every description tested at two values; every line checked at x = 0; every graph drawn from its equation by u7/figs7.py, which refuses a point marked 'on' that is on no line."],
        changes=["Board 6: option E (parking, \\$3 per hour) added — the kit sets five options on a select-all."],
    ),
)
