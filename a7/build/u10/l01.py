# A7 10.01  Linear and Proportional Relationships — MA.8.AR.3.1. Fri 15 Jan 2027, 53 minutes.
# Built from the unit's Lesson Outlines, section 10.01. Every relationship is given as linear (the benchmark's words);
# the question is only whether it is also proportional: y is 0 when x is 0, or y ÷ x is the same for every pair.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs10 as figs
S = figs.slide

X = "sp.Symbol('u', real=True)"


def _u(e):
    import re
    return re.sub(r"\bu\b", X, e)


def _q(v):
    return "F('" + str(v) + "')"


def ne(a, b):
    return ("true", "sp.simplify((" + a + ") - (" + b + ")) != 0")


def sat(rhs, x, y):
    """(x, y) makes y = rhs true (rhs in u)."""
    return ("true", "sp.simplify((" + _u(rhs) + ").subs(" + X + ", " + x + ") - (" + y + ")) == 0")


def table_of(rhs, xs, ys):
    """Each y of a printed table is rhs at its x."""
    return ("many",) + tuple(sat(rhs, str(a), str(b)) for a, b in zip(xs, ys))


def rates(xs, ys, r):
    """A constant rate of change: between each pair of neighbors, (change in y) ÷ (change in x) = r."""
    return ("many",) + tuple(("eq", "(" + _q(ys[i + 1]) + " - " + _q(ys[i]) + ")/(" + _q(xs[i + 1]) + " - " + _q(xs[i]) + ")", r)
                             for i in range(len(xs) - 1))


def at0(xs, ys, v):
    """Going back from the first pair to x = 0 at the constant rate gives y = v."""
    r = "(" + _q(ys[1]) + " - " + _q(ys[0]) + ")/(" + _q(xs[1]) + " - " + _q(xs[0]) + ")"
    return ("eq", _q(ys[0]) + " - " + _q(xs[0]) + "*" + r, v)


def ratios(xs, ys, p):
    """Every pair of the table has y ÷ x = p."""
    return ("many",) + tuple(("eq", _q(y) + "/" + _q(x), p) for x, y in zip(xs, ys))


def not_prop(xs, ys):
    """Not one ratio: the first pair's y ÷ x is not some later pair's."""
    r = [Fr(str(y)) / Fr(str(x)) for x, y in zip(xs, ys)]
    k = next(i for i in range(1, len(r)) if r[i] != r[0])
    return ne(_q(ys[0]) + "/" + _q(xs[0]), _q(ys[k]) + "/" + _q(xs[k]))


def prop_eq(rhs):
    """y = rhs (in u) is proportional: it is c·u for one number c (y is 0 at x = 0 and the expression is linear)."""
    return ("true", "sp.simplify((" + _u(rhs) + ").subs(" + X + ", 0)) == 0 and sp.degree(sp.expand(" + _u(rhs) + "), " + X + ") == 1")


def not_prop_eq(rhs):
    """y = rhs (in u) is linear and NOT proportional: y is not 0 at x = 0."""
    return ("true", "sp.simplify((" + _u(rhs) + ").subs(" + X + ", 0)) != 0 and sp.degree(sp.expand(" + _u(rhs) + "), " + X + ") == 1")


def B(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.75)


def T(spec, inches=7.0):
    return S(spec, inches=inches, pt=20, reserve=0.75)


def TA(spec, inches=6.0):
    return S(spec, inches=inches, pt=18, reserve=0.95)


# ---- the notes
# Notes I: one relationship, x counting by 1 and by 2, and its graph (Unit 11 drew it)
NOTES1 = S(figs.row([figs.table([([0, 1, 2, 3], [3, 5, 7, 9])], cw=1.6, rh=1.8),
                     figs.table([([0, 2, 4, 6], [3, 7, 11, 15])], cw=1.6, rh=1.8),
                     figs.plane((0, 6), (0, 16), ys=2, ystep=2, xstep=2, aspect=1.15, lines=[(2, 3)],
                                points=[(0, 3, ""), (2, 7, ""), (4, 11, ""), (6, 15, "")])],
                    captions=["up 2 for every 1", "up 4 for every 2", "a straight line"], gap=2.0, pt=18),
           inches=11.0, pt=18, reserve=1.45)
# Notes II: y = 2x and y = 2x + 3 on one grid; beside them, a curve through the origin
NOTES2 = S(figs.row([figs.plane((0, 4), (0, 12), ystep=2, aspect=0.5, lines=[figs.prop(2), (2, 3)],
                                points=[(0, 3, "")]),
                     figs.plane((0, 4), (0, 9), ys=3, aspect=2, curves=[figs.square(1, 3)])],
                    titles=[None, "a curve: not linear"], gap=4.5, pt=18),
           inches=9.0, pt=18, reserve=1.5)
# Notes III: two tables with no pair for x = 0
NOTES3 = S(figs.row([figs.table([([2, 4, 6], [9, 13, 17])], cw=1.6, rh=1.4),
                     figs.table([([4, 8, 12], [2, 4, 6])], cw=1.6, rh=1.4)],
                    titles=["first table", "second table"], gap=2.5, pt=18),
           inches=10.0, pt=18, reserve=2.3)

# ---- the examples
EX1_T = figs.table([([4, 8, 12], [9, 15, 21])], cw=1.8, rh=1.4)
EX1 = T(EX1_T, 6.0)
EX1W = S(EX1_T, inches=4.2, pt=18, reserve=0.9)
YT1_T = figs.table([([5, 10, 15], [6, 12, 18])], cw=1.8, rh=1.4)
YT1 = T(YT1_T, 6.0)
YT1A = S(YT1_T, inches=4.2, pt=18, reserve=0.9)

# ---- the boards
TB1 = figs.table([([0, 1, 2, 3], [4, 7, 10, 13])], cw=1.6, rh=1.4)
TB3 = figs.table([([4, 8, 12, 16], [3, 6, 9, 12])], cw=1.6, rh=1.4)
# Board 5: four graphs on one window, the same scales on all four. Lettered in their final order (keyed A):
# A the points (1, 3), (2, 6), (3, 9); B a curve through (0, 0), (1, 1) and (2, 4); C a line through (0, 3) and (3, 6);
# D the points (2, 5), (4, 6), (6, 7).
g5 = dict(inches=2.6, pt=18, ystep=2, xstep=2)
G5_LINE = figs.plane((0, 7), (0, 10), lines=[(1, 3, "")], points=[(0, 3, ""), (3, 6, "")], **g5)
G5_RATE = figs.plane((0, 7), (0, 10), points=[(2, 5, ""), (4, 6, ""), (6, 7, "")], **g5)
G5_OK = figs.plane((0, 7), (0, 10), points=[(1, 3, ""), (2, 6, ""), (3, 9, "")], **g5)
G5_CURVE = figs.plane((0, 7), (0, 10), curves=[figs.square(1, 3)], points=[(1, 1, ""), (2, 4, "")], **g5)
C5 = S(figs.choices4([G5_OK, G5_CURVE, G5_LINE, G5_RATE], gap=3.6), inches=14.0, pt=18, reserve=0.75)
C5A = S(figs.row([figs.plane((0, 7), (0, 10), lines=[figs.prop(3, "")], points=[(1, 3, "on", "r"), (2, 6, "on", "r"), (3, 9, "on", "r")],
                             inches=4.2, pt=18, ystep=2, xstep=2)], titles=["A"], inches=4.2, pt=18),
        inches=4.2, pt=18, reserve=0.95)


# ---- paper figures
def PTS(xr, yr, pts, inches=2.6, **k):
    return figs.plane(xr, yr, points=[(a, b, "") for a, b in pts], inches=inches, **k)


IS3K = figs.plane((0, 8), (0, 6), points=[(0, 2, "on"), (2, 3, "on"), (4, 4, "on"), (6, 5, "on")], lines=[(Fr(1, 2), 2, "")], inches=3.0)
IS6 = figs.row([figs.table([([2, 3, 5], [8, 12, 20])]), figs.table([([1, 3, 5], [6, 10, 14])])],
               titles=["first table", "second table"], gap=2.0, inches=5.0)

gb = dict(inches=2.0, ystep=2, xstep=2)
BK11 = figs.choices4([figs.plane((0, 4), (0, 10), points=[(1, 5, ""), (2, 6, ""), (3, 7, "")], **gb),
                      figs.plane((0, 4), (0, 10), lines=[(Fr(1, 2), 3, "")], points=[(0, 3, ""), (4, 5, "")], **gb),
                      figs.plane((0, 4), (0, 10), curves=[figs.square(Fr(1, 4), 4)], points=[(2, 1, ""), (4, 4, "")], **gb),
                      figs.plane((0, 4), (0, 10), points=[(1, 2, ""), (2, 4, ""), (3, 6, "")], **gb)],
                     gap=1.6, inches=6.6, pt=9.5)
ga = dict(inches=2.0, ystep=2, xstep=2)
AD11 = figs.choices4([figs.plane((0, 4), (0, 14), points=[(1, 7, ""), (2, 8, ""), (3, 9, "")], **ga),
                      figs.plane((0, 4), (0, 14), lines=[(2, 4, "")], points=[(0, 4, ""), (4, 12, "")], **ga),
                      figs.plane((0, 4), (0, 14), points=[(2, 6, ""), (3, 9, ""), (4, 12, "")], **ga),
                      figs.plane((0, 4), (0, 14), curves=[figs.square(2, Fr(5, 2))], points=[(1, 2, ""), (2, 8, "")], **ga)],
                     gap=1.6, inches=6.6, pt=9.5)


L = dict(
    code="10.01", unit=10, lesson_no=1,
    title="Linear and Proportional Relationships",
    unit_title="Linear Relationships",
    benchmark="MA.8.AR.3.1",
    benchmark_text="Determine if a linear relationship is also a proportional relationship.",
    target="I can decide whether a linear relationship shown in a table, a graph, an equation or a description is also proportional, and explain how I know.",
    essential="Every proportional relationship is linear. What does a linear relationship need before it is also proportional?",
    building_on="Lesson 7.04 tested a relationship for proportionality with a table, a graph and a description, and Lesson 7.07 compared rates. Lesson 11.07 graphed lines such as y = 2x + 3 from a table of values.",
    working_toward="Lessons 10.02 and 10.03 name the rate of change of a line its slope. Lesson 10.05 names the value of y when x is 0 the y-intercept.",
    vocab=[("rate of change", "the amount y changes for every 1 unit that x increases"),
           ("linear relationship", "a relationship with a constant rate of change; its graph is a straight line"),
           ("proportional relationship", "a linear relationship in which y is 0 when x is 0:  $y = px$")],
    ixl=["Find the constant of proportionality from a table — ZCK", "Identify proportional relationships by graphing — RXD",
         "Identify proportional relationships — Z64", "Write equations for proportional relationships from tables and graphs — VXM",
         "Interpret graphs of proportional relationships — Q96"],
    closure="Whiteboard question 9 is written work, and it is the exit evidence. A full answer says that Mia is not correct: a constant increase makes the relationship linear, but y is 4 when x is 0 (or y ÷ x is 6 and then 4), so it is not proportional. An answer that says only \"no\" gives the verdict without the reason.",

    mtr=[("MTR.2.1", "Students decide the same question from a table, a graph, an equation and a description, and they see that each one shows the same two facts: the rate of change and the value of y when x is 0."),
         ("MTR.4.1", "On whiteboard questions 3 and 5, a split class convinces a neighbor for sixty seconds and then votes again."),
         ("MTR.6.1", "Students check each decision two ways, by the value of y when x is 0 and by y ÷ x for every pair.")],
    hoq=[("Why is every proportional relationship linear, but not every linear relationship proportional?", "DOK 2"),
         ("The table has no pair for x = 0. How can you still find y when x is 0?", "DOK 2"),
         ("y = 5(x + 2) has no number added at the end. Is it proportional? How do you know?", "DOK 2"),
         ("A curve passes through the origin. Why is it not a proportional relationship?", "DOK 3")],
    differentiation=[
        ("ESE / 504", "Students have a printed card with the two tests, \"Is y 0 when x is 0?\" and \"Is y ÷ x the same for every pair?\", and Notes III stays on the board from whiteboard question 1 on."),
        ("ELL", "The words are taught with a picture: a rate of change is how much y goes up for every 1 unit of x, linear means a straight line, and proportional means a straight line through the origin."),
        ("Enrichment", "Students who finish early write a table with no pair for x = 0 for a proportional relationship and another for a relationship that is not proportional, and they trade them with a neighbor.")],

    warmup=[
        dict(stem="Car A travels 150 miles in 3 hours. Car B travels 110 miles in 2 hours. Which car is faster?",
             answer="Car B (55 miles per hour versus 50)",
             check=("many", ("eq", "F(110, 2)", "55"), ("eq", "F(150, 3)", "50"), ("true", "F(110, 2) > F(150, 3)"))),
        dict(stem="A table has the x-values 2, 4, 6 and the y-values 5, 10, 15. Is y proportional to x?",
             answer="Yes, y ÷ x is 2.5 for every pair.",
             check=ratios([2, 4, 6], [5, 10, 15], "F(5,2)")),
        dict(stem="For $y = 2x + 3$, find y when x is 0, 1 and 2.", answer="3, 5, 7",
             check=table_of("2*u + 3", [0, 1, 2], [3, 5, 7])),
        dict(stem="Find  $15 \\div 6$  and  $7 - 2(2.5)$.", answer="2.5 and 2",
             check=("many", ("eq", "F(15, 6)", "F(5, 2)"), ("eq", "7 - 2*F(5, 2)", "2"))),
    ],

    notes=[
        dict(numeral="I", head="Linear: a constant rate of change", min=3,
             fig=NOTES1,
             text=["A linear relationship has a constant rate of change.",
                   "Up 4 for every 2 units of x is 2 for every 1 unit."],
             letters=False),
        dict(numeral="II", head="Also proportional? Look at x = 0.", min=4,
             fig=NOTES2,
             text=["It is also proportional when y is 0 when x is 0:", "its line passes through the origin."],
             letters=False),
        # figwords_ok: the words' 1 is "for every 1 unit", a rate, not a value of the tables; the tables' other values
        # (12, 13, 17, 6, 8) are read off the picture as a table is, and the words work only from the first pairs.
        dict(figwords_ok=True, numeral="III", head="When the table has no pair for x = 0", min=3,
             fig=NOTES3,
             text=["Go back to x = 0 at the rate of change.",
                   "First:  2 for every 1 unit.   9 − 2 − 2 = 5:  not proportional.",
                   "Second:  0.5 for every 1 unit.   2 − 4(0.5) = 0:  proportional.",
                   "Check the second:  y ÷ x is 0.5 for every pair."],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=1,
             prompt=["The table shows a linear relationship."], fig=EX1, ask="Is it also proportional?",
             worked=[dict(min=2,
                          rows=[("15 - 9 = 6", "for every 4 units of x"),
                                ("6 \\div 4 = 1.5", "for every 1 unit of x"),
                                ("9 - 4(1.5) = 3", "back 4 units from x = 4")],
                          fig=EX1W, answer="Not proportional: y is 3 when x is 0.")],
             check=("many", rates([4, 8, 12], [9, 15, 21], "F(3,2)"), at0([4, 8, 12], [9, 15, 21], "3"),
                    ("eq", "9 - 4*F(3,2)", "3"), not_prop([4, 8, 12], [9, 15, 21])),
             # the Your Turn's answer differs from the Example's on purpose
             your_turn=dict(min=3,
                            prompt=["The table shows a linear relationship."], fig=YT1, fig_a=YT1A,
                            ask="Is it also proportional?",
                            steps=["Rate of change:   $(12 - 6) \\div (10 - 5) = 1.2$",
                                   "Go back to x = 0:   $6 - 5(1.2) = 0$"],
                            answer="Proportional: y is 0 when x is 0."),
             yt_check=("many", rates([5, 10, 15], [6, 12, 18], "F(6,5)"), at0([5, 10, 15], [6, 12, 18], "0"),
                       ("eq", "6 - 5*F(6,5)", "0"), ratios([5, 10, 15], [6, 12, 18], "F(6,5)"))),
        dict(title="Example 2", min_q=1,
             prompt=["A boat rental costs \\$12 for every hour plus a \\$20 deposit.",
                     "A bike rental costs \\$9 for every hour."],
             ask="Write an equation for each cost c, in dollars, after h hours. Which relationship is also proportional?",
             worked=[dict(min=2,
                          rows=[("c = 12h + 20", "the boat"),
                                ("c = 9h", "the bike"),
                                ("h = 0:\\quad 12(0) + 20 = 20", "the boat costs \\$20 at 0 hours"),
                                ("9(0) = 0", "the bike costs \\$0 at 0 hours")],
                          answer="The bike rental's cost is proportional.")],
             check=("many", not_prop_eq("12*u + 20"), prop_eq("9*u"), ("eq", "12*0 + 20", "20"), ("eq", "9*0", "0")),
             your_turn=dict(min=3,
                            prompt=["One plant is 6 centimeters tall and grows 1.5 centimeters every week.",
                                    "A second plant sprouts today and grows 2 centimeters every week."],
                            ask="Write an equation for each height h, in centimeters, after w weeks. Which is also proportional?",
                            steps=["Equations:   $h = 1.5w + 6$   and   $h = 2w$",
                                   "At $w = 0$:   $1.5(0) + 6 = 6$   and   $2(0) = 0$"],
                            answer="The second plant's height is proportional."),
             yt_check=("many", not_prop_eq("F(3,2)*u + 6"), prop_eq("2*u"), ("eq", "F(3,2)*0 + 6", "6"), ("eq", "2*0", "0"))),
    ],

    # The round: the rate of change from a table with x = 0 (1); the same table, also proportional? (2 — one thing
    # changes, the question); the diagnostic on a table with no pair for x = 0 (3); an equation (4); the diagnostic on
    # four graphs (5); a select-all of equations, the pattern broken by 5(x + 2) (6); the taxi, its seats the extra
    # number (7); backwards to the start from two pairs (8); Mia's claim, written (9).
    whiteboard=[
        dict(text=["The table shows a linear relationship.", "**What is its rate of change?"],
             fig=T(TB1), fig_a=TA(TB1),
             steps=["$7 - 4 = 3$,   $10 - 7 = 3$,   $13 - 10 = 3$",
                    "y increases 3 for every 1 unit of x"],
             answer="3",
             check=("many", rates([0, 1, 2, 3], [4, 7, 10, 13], "3"), table_of("3*u + 4", [0, 1, 2, 3], [4, 7, 10, 13])),
             wrong="4 — the value of y at x = 0 read as the rate [Notes I: the rate of change is the change in y for every 1 unit of x]; 13 — the last y read as the rate [Notes I: a constant rate of change]"),
        # repeat_ok: the same table as whiteboard question 1 on purpose — one thing changes, the question (the plan).
        dict(repeat_ok=True, text=["The table shows a linear relationship.", "**Is it also proportional? How do you know?"],
             fig=T(TB1), fig_a=TA(TB1),
             steps=["At $x = 0$:   $y = 4$", "4 is not 0:  not proportional"],
             answer="No, because y is 4 when x is 0.",
             check=("many", table_of("3*u + 4", [0], [4]), ne("4", "0"), not_prop([1, 2, 3], [7, 10, 13])),
             wrong="yes, the rate of change is constant — linear taken for proportional [Florida B1G-M, AR.3.1: every linear relationship taken as proportional]"),
        dict(kind="mc", text=["The table shows a linear relationship.", "**Is it also proportional?"],
             qtext="The table shows a linear relationship: x 4, 8, 12, 16; y 3, 6, 9, 12. Is it also proportional?",
             fig=B(TB3), fig_a=TA(TB3, 4.2),
             steps=["$3 \\div 4 = 0.75$,   $6 \\div 8 = 0.75$", "$9 \\div 12 = 0.75$,   $12 \\div 16 = 0.75$"],
             choices=["No, y is 3 when x is 0.", "Yes, y ÷ x is 0.75 for every pair.", "No, y is not a whole-number multiple of x.", "No, the table has no pair for x = 0."],
             correct=1, answer="B — Yes, y ÷ x is 0.75 for every pair.",
             errors={"A": "the first pair's y read as the value at x = 0 [Notes III: go back to x = 0 at the rate of change]", "C": "the constant thought to be a whole number [Notes III: 0.5 for every 1 unit is a constant too]", "D": "a table with no pair for x = 0 taken as not proportional [benchmark misconception: the origin must be shown]"},
             check=("many", ratios([4, 8, 12, 16], [3, 6, 9, 12], "F(3,4)"), at0([4, 8, 12, 16], [3, 6, 9, 12], "0"),
                    ne(at0([4, 8, 12, 16], [3, 6, 9, 12], "0")[1], "3"), ("true", "not F(3,4).is_integer"))),
        dict(text=["$y = 6x - 1$  is a linear relationship.", "**Is it also proportional? How do you know?"],
             steps=["At $x = 0$:   $6(0) - 1 = -1$", "−1 is not 0:  not proportional"],
             answer="No, because y is −1 when x is 0.",
             check=("many", sat("6*u - 1", "0", "-1"), not_prop_eq("6*u - 1")),
             wrong="yes, 6 is the coefficient of x — the number subtracted ignored [Notes II: look at x = 0]"),
        dict(kind="mc", text=["**Which graph shows a proportional relationship?"],
             qtext="Four graphs, each on its own axes with the same scales: A the points (1, 3), (2, 6) and (3, 9); B a curve through (0, 0), (1, 1) and (2, 4); C a line through (0, 3) and (3, 6); D the points (2, 5), (4, 6) and (6, 7). Which graph shows a proportional relationship?",
             fig=C5, fig_a=C5A,
             steps=["$3 \\div 1 = 3$,   $6 \\div 2 = 3$,   $9 \\div 3 = 3$",
                    "their line passes through the origin"],
             choices=["A", "B", "C", "D"], correct=0, answer="A",
             errors={"B": "a graph through the origin taken as proportional, though it is a curve [Notes II: a proportional relationship is linear first]", "C": "a straight line taken as proportional, though it passes through (0, 3) [Notes II: look at x = 0]", "D": "a constant rate of change taken for a constant ratio: y ÷ x is 2.5, then 1.5 [Florida B1G-M, AR.3.1: every linear relationship taken as proportional]"},
             check=("many", ratios([1, 2, 3], [3, 6, 9], "3"), sat("3*u", "0", "0"),
                    table_of("u + 3", [0, 3], [3, 6]), not_prop_eq("u + 3"),
                    rates([2, 4, 6], [5, 6, 7], "F(1,2)"), not_prop([2, 4, 6], [5, 6, 7]),
                    table_of("u**2", [0, 1, 2], [0, 1, 4]), ne("F(1,1)/1", "F(4,1)/2"))),
        dict(kind="mc", text=["**Select all the equations that show a proportional relationship."],
             qtext="Select all the equations that show a proportional relationship: A y = x/5; B y = (2/5)x; C y = 5(x + 2); D y = −5x; E y = 2 + 5x.",
             steps=["A:   $\\frac{x}{5}$ is $\\frac{1}{5}x$:   y is 0 when x is 0", "B:   $\\frac{2}{5}(0) = 0$",
                    "C:   $5(x + 2) = 5x + 10$,  so y is 10 when x is 0", "D:   $-5(0) = 0$", "E:   y is 2 when x is 0"],
             choices=["$y = \\frac{x}{5}$", "$y = \\frac{2}{5}x$", "$y = 5(x + 2)$", "$y = -5x$", "$y = 2 + 5x$"],
             correct=[0, 1, 3], answer="A, B, D",
             errors={"C": "no number seen added, but 5(x + 2) is 5x + 10 [Florida B1G-M, AR.3.1: the equation not simplified first]", "E": "the number added missed because it is written first [Notes II: look at x = 0]"},
             check=("many", prop_eq("F(2,5)*u"), prop_eq("-5*u"), prop_eq("u/5"),
                    not_prop_eq("2 + 5*u"), not_prop_eq("5*(u + 2)"))),
        dict(text=["A taxi with 4 seats charges \\$3.50 to start and \\$2.25 for every mile.",
                   "**Is the cost proportional to the number of miles? Explain."],
             unneeded="4",
             steps=["0 miles:   $2.25(0) + 3.50 = 3.50$", "\\$3.50 is not \\$0:  not proportional"],
             answer="No, a ride of 0 miles costs \\$3.50.",
             check=("many", ("eq", "F(9,4)*0 + F(7,2)", "F(7,2)"), not_prop_eq("F(9,4)*u + F(7,2)")),
             wrong="yes, \\$2.25 for every mile — the start charge ignored [Notes II: look at x = 0]; 4 seats used as the rate [an extra number, included on purpose]"),
        dict(text=["A linear relationship includes the pairs (2, 11) and (5, 23).", "**What is y when x is 0?"],
             steps=["Rate of change:   $(23 - 11) \\div (5 - 2) = 4$", "Go back to x = 0:   $11 - 2(4) = 3$"],
             answer="3",
             check=("many", rates([2, 5], [11, 23], "4"), at0([2, 5], [11, 23], "3")),
             wrong="11 — the y of the first pair read as the start [Notes III: go back to x = 0 at the rate of change]; 7 — 11 − 4, back one unit only [Notes III: go back to x = 0 at the rate of change]"),
        # repeat_ok: rule D matches only Notes II's axis numbers (0 to 10) against the plan's table 1, 2, 3 / 6, 8, 10;
        # the relationship y = 2x + 4 appears nowhere above.
        dict(repeat_ok=True, kind="written", text=["Mia says the table with the x-values 1, 2, 3 and the y-values 6, 8, 10",
                                   "shows a proportional relationship, because y increases",
                                   "by the same amount every time.",
                                   "**Is Mia correct? Explain."],
             qtext="Mia says the table with the x-values 1, 2, 3 and the y-values 6, 8, 10 shows a proportional relationship, because y increases by the same amount every time. Is Mia correct? Explain.",
             steps=["Rate of change:   $8 - 6 = 2$   and   $10 - 8 = 2$:   linear",
                    "Go back to x = 0:   $6 - 2 = 4$"],
             answer="No, it is linear, but y is 4 when x is 0.",
             check=("many", rates([1, 2, 3], [6, 8, 10], "2"), at0([1, 2, 3], [6, 8, 10], "4"), not_prop([1, 2, 3], [6, 8, 10])),
             wrong="yes, it goes up by 2 every time — a constant rate of change taken for proportional [Florida B1G-M, AR.3.1: every linear relationship taken as proportional]"),
    ],

    # The six: a table with x = 0 (1); no pair for x = 0, x counting by 3 (2); a graph of three points (3); a select-all
    # (4); a description to write and decide (5); two tables, which is proportional (6).
    independent=[
        # repeat_ok: rule D matches only Notes I's axis numbers (0 to 16 by 2) against this table; the relationship
        # y = 0.75x + 1 appears nowhere above.
        dict(repeat_ok=True, stem="The table shows a linear relationship. Is it also proportional? Explain how you know.",
             fig=figs.table([([0, 4, 8, 12], [1, 4, 7, 10])], inches=3.6),
             answer="No, y is 1 when x is 0.", why="The pair (0, 1) is in the table: y is 1, not 0, when x is 0. The rate of change is 3 for every 4 units, 0.75 for every 1 unit.",
             check=("many", rates([0, 4, 8, 12], [1, 4, 7, 10], "F(3,4)"), ne("1", "0")), space=0.5),
        dict(stem="The table shows a linear relationship. What is y when x is 0? Is the relationship also proportional?",
             fig=figs.table([([3, 6, 9], [11, 20, 29])], inches=3.0),
             answer="2; no", why="The rate of change is 9 for every 3 units, 3 for every 1 unit. Go back to x = 0 at the rate of change: 11 − 3(3) = 2, so y is 2 when x is 0, and the relationship is not proportional.",
             check=("many", rates([3, 6, 9], [11, 20, 29], "3"), at0([3, 6, 9], [11, 20, 29], "2"), not_prop([3, 6, 9], [11, 20, 29])), space=0.6),
        # repeat_ok: rule D matches only the grid's axis numbers (0 to 8, as on Notes I's graph) and the answer's
        # 0 and 2; the points (2, 3), (4, 4), (6, 5) and the relationship y = 0.5x + 2 appear nowhere above.
        dict(repeat_ok=True, stem="The points of a linear relationship are graphed. Is the relationship also proportional? Explain.",
             fig=PTS((0, 8), (0, 6), [(2, 3), (4, 4), (6, 5)], inches=3.0), fig_key=IS3K,
             answer="No, its line passes through (0, 2).", why="The points go up 1 for every 2 units of x. Back 2 units from (2, 3) is (0, 2): y is 2 when x is 0, so the line does not pass through the origin.",
             check=("many", rates([2, 4, 6], [3, 4, 5], "F(1,2)"), at0([2, 4, 6], [3, 4, 5], "2"), not_prop([2, 4, 6], [3, 4, 5])), space=0.5),
        dict(stem="Select all the equations that show a proportional relationship.",
             choices=["$y = 4x$", "$y = 4 + x$", "$y = -2x$", "$y = 3(x - 1)$", "$y = 0.75x$"],
             correct=[0, 2, 4], answer="A, C, E",
             why="A, C and E: y is 0 when x is 0. B is 4 when x is 0; D is 3x − 3, which is −3 when x is 0.",
             errors={"B": "the number added missed because it is written first [Notes II: look at x = 0]", "D": "no number seen added, but 3(x − 1) is 3x − 3 [Florida B1G-M, AR.3.1: the equation not simplified first]"},
             check=("many", prop_eq("4*u"), prop_eq("F(3,4)*u"), prop_eq("-2*u"), not_prop_eq("4 + u"), not_prop_eq("3*(u - 1)"))),
        dict(stem="A gym charges a \\$30 sign-up fee and \\$4 for every visit. Write an equation for the cost c, in dollars, of v visits. Is the cost proportional to the number of visits?",
             answer="c = 4v + 30; no", why="0 visits cost 4(0) + 30 = 30 dollars, not 0, so the cost is not proportional.",
             check=("many", ("eq", "4*0 + 30", "30"), not_prop_eq("4*u + 30")), space=0.6),
        dict(stem="Both tables show linear relationships. Which relationship is also proportional?",
             fig=IS6,
             answer="The first table's", why="First table: 8 ÷ 2 = 12 ÷ 3 = 20 ÷ 5 = 4, so y ÷ x is 4 for every pair. Second table: the rate of change is 2, and 6 − 2 = 4 is y when x is 0.",
             check=("many", ratios([2, 3, 5], [8, 12, 20], "4"), rates([1, 3, 5], [6, 10, 14], "2"), at0([1, 3, 5], [6, 10, 14], "4")), space=0.5),
    ],

    bank=[
        dict(heading="For questions 1 and 2, the table shows a linear relationship. Is it also proportional? Explain how you know."),
        dict(stem="", fig=figs.table([([0, 1, 2, 3], [0, -2, -4, -6])], inches=3.4),
             answer="Yes, y is 0 when x is 0.", why="The pair (0, 0) is in the table, and y ÷ x is −2 for every other pair.",
             check=("many", rates([0, 1, 2, 3], [0, -2, -4, -6], "-2"), ratios([1, 2, 3], [-2, -4, -6], "-2")), space=0.4),
        dict(stem="", fig=figs.table([([0, 4, 8, 12], [6, 9, 12, 15])], inches=3.4),
             answer="No, y is 6 when x is 0.", why="The pair (0, 6) is in the table: y is 6, not 0, when x is 0.",
             check=("many", rates([0, 4, 8, 12], [6, 9, 12, 15], "F(3,4)"), ne("6", "0")), space=0.4),
        dict(heading="For questions 3 and 4, the table shows a linear relationship. What is y when x is 0? Is the relationship also proportional?"),
        dict(stem="", fig=figs.table([([2, 4, 6], [7, 8, 9])], inches=3.0),
             answer="6; no", why="The rate of change is 1 for every 2 units, 0.5 for every 1 unit. Go back to x = 0 at the rate of change: 7 − 2(0.5) = 6.",
             check=("many", rates([2, 4, 6], [7, 8, 9], "F(1,2)"), at0([2, 4, 6], [7, 8, 9], "6"), not_prop([2, 4, 6], [7, 8, 9])), space=0.5),
        dict(stem="", fig=figs.table([([4, 8, 12], [12, 24, 36])], inches=3.0),
             answer="0; yes", why="The rate of change is 12 for every 4 units, 3 for every 1 unit. Go back to x = 0 at the rate of change: 12 − 4(3) = 0.",
             check=("many", rates([4, 8, 12], [12, 24, 36], "3"), at0([4, 8, 12], [12, 24, 36], "0"), ratios([4, 8, 12], [12, 24, 36], "3")), space=0.5),
        dict(heading="Use the graph."),
        dict(stem="The points of a linear relationship are graphed. Is the relationship also proportional? Explain.",
             fig=PTS((0, 14), (0, 12), [(4, 5), (8, 8), (12, 11)], xs=2, ystep=2),
             answer="No, its line passes through (0, 2).", why="The points go up 3 for every 4 units of x. Back 4 units from (4, 5) is (0, 2): the line does not pass through the origin.",
             check=("many", rates([4, 8, 12], [5, 8, 11], "F(3,4)"), at0([4, 8, 12], [5, 8, 11], "2"), not_prop([4, 8, 12], [5, 8, 11])), space=0.5),
        dict(heading="Select all that apply."),
        dict(stem="Select all the equations that show a proportional relationship.",
             choices=["$y = x - 3$", "$y = 2(x + 4)$", "$y = \\frac{x}{3}$", "$y = -4x$", "$y = 0.5x$"],
             correct=[2, 3, 4], answer="C, D, E",
             why="C, D and E: y is 0 when x is 0. A is −3 when x is 0; B is 2x + 8, which is 8 when x is 0.",
             errors={"A": "the number subtracted ignored [Notes II: look at x = 0]", "B": "no number seen added, but 2(x + 4) is 2x + 8 [Florida B1G-M, AR.3.1: the equation not simplified first]"},
             check=("many", prop_eq("F(1,2)*u"), prop_eq("u/3"), prop_eq("-4*u"), not_prop_eq("u - 3"), not_prop_eq("2*(u + 4)"))),
        dict(heading="For questions 7 and 8, write an equation, then decide."),
        dict(stem="A pool charges a \\$5 entry fee plus \\$2 for every hour. Write an equation for the cost c, in dollars, of h hours. Is the cost proportional to the number of hours?",
             answer="c = 2h + 5; no", why="0 hours cost 2(0) + 5 = 5 dollars, not 0.",
             check=("many", ("eq", "2*0 + 5", "5"), not_prop_eq("2*u + 5")), space=0.5),
        dict(stem="Apples cost \\$1.20 for every pound. Write an equation for the cost c, in dollars, of w pounds. Is the cost proportional to the number of pounds?",
             answer="c = 1.20w; yes", why="0 pounds cost 1.20(0) = 0 dollars, and c ÷ w is 1.20 for every pair.",
             check=("many", ("eq", "F(6,5)*0", "0"), prop_eq("F(6,5)*u")), space=0.5),
        dict(heading="Use the two pairs."),
        dict(stem="A linear relationship includes the pairs (3, 14) and (7, 26). What is y when x is 0? Is the relationship also proportional?",
             answer="5; no", why="The rate of change is (26 − 14) ÷ (7 − 3) = 3. Go back to x = 0 at the rate of change: 14 − 3(3) = 5.",
             check=("many", rates([3, 7], [14, 26], "3"), at0([3, 7], [14, 26], "5"), not_prop([3, 7], [14, 26])), space=0.6),
        dict(heading="Choose one."),
        dict(stem="The table shows a linear relationship with the x-values 10, 20, 30 and the y-values 5, 10, 15. Is it also proportional?",
             choices=["No, the table has no pair for x = 0.", "No, y is 5 when x is 0.", "Yes, y ÷ x is 0.5 for every pair.", "No, y is not a whole-number multiple of x."],
             correct=2, answer="C",
             why="5 ÷ 10 = 10 ÷ 20 = 15 ÷ 30 = 0.5.",
             errors={"A": "a table with no pair for x = 0 taken as not proportional [benchmark misconception: the origin must be shown]", "B": "the first pair's y read as the value at x = 0 [Notes III: go back to x = 0 at the rate of change]", "D": "the constant thought to be a whole number [Notes III: 0.5 for every 1 unit is a constant too]"},
             check=("many", ratios([10, 20, 30], [5, 10, 15], "F(1,2)"), at0([10, 20, 30], [5, 10, 15], "0"), ("true", "not F(1,2).is_integer"))),
        dict(stem="Which graph shows a proportional relationship?",
             fig=BK11,
             choices=["A", "B", "C", "D"], correct=3, answer="D",
             why="Graph D: 2 ÷ 1 = 4 ÷ 2 = 6 ÷ 3 = 2, so its points lie on a line through the origin.",
             errors={"A": "a constant rate of change taken for a constant ratio: y ÷ x is 5, then 3 [Florida B1G-M, AR.3.1: every linear relationship taken as proportional]", "B": "a straight line taken as proportional, though it passes through (0, 3) [Notes II: look at x = 0]", "C": "a graph through the origin taken as proportional, though it is a curve [Notes II: a proportional relationship is linear first]"},
             check=("many", ratios([1, 2, 3], [2, 4, 6], "2"), table_of("F(1,2)*u + 3", [0, 4], [3, 5]), not_prop_eq("F(1,2)*u + 3"),
                    rates([1, 2, 3], [5, 6, 7], "1"), not_prop([1, 2, 3], [5, 6, 7]),
                    table_of("u**2/4", [0, 2, 4], [0, 1, 4]), ne("F(1,2)", "F(4,4)"))),
        dict(heading="Explain."),
        dict(stem="Leo says the table with the x-values 2, 4, 6 and the y-values 5, 9, 13 shows a proportional relationship, because y increases by 4 every time. Is Leo correct? Explain.",
             answer="No, y is 1 when x is 0.", why="A constant increase makes the relationship linear. The rate of change is 2 for every 1 unit; back 2 units from x = 2 gives 5 − 2(2) = 1, so y is 1 when x is 0 (and y ÷ x is 2.5, then 2.25). It is not proportional.",
             check=("many", rates([2, 4, 6], [5, 9, 13], "2"), at0([2, 4, 6], [5, 9, 13], "1"), not_prop([2, 4, 6], [5, 9, 13])), lines=3),
    ],

    additional=[
        dict(heading="For questions 1 and 2, the table shows a linear relationship. Is it also proportional? Explain how you know."),
        dict(stem="", fig=figs.table([([0, 1, 2, 3], [0, -3, -6, -9])], inches=3.4),
             answer="Yes, y is 0 when x is 0.", why="The pair (0, 0) is in the table, and y ÷ x is −3 for every other pair.",
             check=("many", rates([0, 1, 2, 3], [0, -3, -6, -9], "-3"), ratios([1, 2, 3], [-3, -6, -9], "-3")), space=0.4),
        dict(stem="", fig=figs.table([([0, 5, 10, 15], [3, 9, 15, 21])], inches=3.4),
             answer="No, y is 3 when x is 0.", why="The pair (0, 3) is in the table: y is 3, not 0, when x is 0.",
             check=("many", rates([0, 5, 10, 15], [3, 9, 15, 21], "F(6,5)"), ne("3", "0")), space=0.4),
        dict(heading="For questions 3 and 4, the table shows a linear relationship. What is y when x is 0? Is the relationship also proportional?"),
        dict(stem="", fig=figs.table([([2, 4, 6], [4, 5, 6])], inches=3.0),
             answer="3; no", why="The rate of change is 1 for every 2 units, 0.5 for every 1 unit. Go back to x = 0 at the rate of change: 4 − 2(0.5) = 3.",
             check=("many", rates([2, 4, 6], [4, 5, 6], "F(1,2)"), at0([2, 4, 6], [4, 5, 6], "3"), not_prop([2, 4, 6], [4, 5, 6])), space=0.5),
        dict(stem="", fig=figs.table([([6, 12, 18], [12, 24, 36])], inches=3.0),
             answer="0; yes", why="The rate of change is 12 for every 6 units, 2 for every 1 unit. Go back to x = 0 at the rate of change: 12 − 6(2) = 0.",
             check=("many", rates([6, 12, 18], [12, 24, 36], "2"), at0([6, 12, 18], [12, 24, 36], "0"), ratios([6, 12, 18], [12, 24, 36], "2")), space=0.5),
        dict(heading="Use the graph."),
        dict(stem="The points of a linear relationship are graphed. Is the relationship also proportional? Explain.",
             fig=PTS((0, 6), (0, 14), [(1, 4), (2, 8), (3, 12)], ys=2),
             answer="Yes, its line passes through the origin.", why="y ÷ x is 4 for every point: 4 ÷ 1 = 8 ÷ 2 = 12 ÷ 3 = 4. Back 1 unit from (1, 4) is (0, 0).",
             check=("many", ratios([1, 2, 3], [4, 8, 12], "4"), at0([1, 2, 3], [4, 8, 12], "0")), space=0.5),
        dict(heading="Select all that apply."),
        dict(stem="Select all the equations that show a proportional relationship.",
             choices=["$y = 1.2x$", "$y = -3x$", "$y = 4(x - 1)$", "$y = \\frac{x}{4}$", "$y = x + 2$"],
             correct=[0, 1, 3], answer="A, B, D",
             why="A, B and D: y is 0 when x is 0. E is 2 when x is 0; C is 4x − 4, which is −4 when x is 0.",
             errors={"C": "no number seen added, but 4(x − 1) is 4x − 4 [Florida B1G-M, AR.3.1: the equation not simplified first]", "E": "the number added ignored [Notes II: look at x = 0]"},
             check=("many", prop_eq("F(6,5)*u"), prop_eq("u/4"), prop_eq("-3*u"), not_prop_eq("u + 2"), not_prop_eq("4*(u - 1)"))),
        dict(heading="For questions 7 and 8, write an equation, then decide."),
        dict(stem="A bowling alley charges \\$4 for shoes plus \\$3 for every game. Write an equation for the cost c, in dollars, of g games. Is the cost proportional to the number of games?",
             answer="c = 3g + 4; no", why="0 games cost 3(0) + 4 = 4 dollars, not 0.",
             check=("many", ("eq", "3*0 + 4", "4"), not_prop_eq("3*u + 4")), space=0.5),
        dict(stem="Bananas cost \\$0.50 for every pound. Write an equation for the cost c, in dollars, of w pounds. Is the cost proportional to the number of pounds?",
             answer="c = 0.50w; yes", why="0 pounds cost 0.50(0) = 0 dollars, and c ÷ w is 0.50 for every pair.",
             check=("many", ("eq", "F(1,2)*0", "0"), prop_eq("F(1,2)*u")), space=0.5),
        dict(heading="Use the two pairs."),
        dict(stem="A linear relationship includes the pairs (2, 9) and (6, 21). What is y when x is 0? Is the relationship also proportional?",
             answer="3; no", why="The rate of change is (21 − 9) ÷ (6 − 2) = 3. Go back to x = 0 at the rate of change: 9 − 2(3) = 3.",
             check=("many", rates([2, 6], [9, 21], "3"), at0([2, 6], [9, 21], "3")), space=0.6),
        dict(heading="Choose one."),
        dict(stem="The table shows a linear relationship with the x-values 2, 4, 6, 8 and the y-values 1, 2, 3, 4. Is it also proportional?",
             choices=["Yes, y ÷ x is 0.5 for every pair.", "No, y is 1 when x is 0.", "No, the table has no pair for x = 0.", "No, y is not a whole-number multiple of x."],
             correct=0, answer="A",
             why="1 ÷ 2 = 2 ÷ 4 = 3 ÷ 6 = 4 ÷ 8 = 0.5.",
             errors={"B": "the first pair's y read as the value at x = 0 [Notes III: go back to x = 0 at the rate of change]", "C": "a table with no pair for x = 0 taken as not proportional [benchmark misconception: the origin must be shown]", "D": "the constant thought to be a whole number [Notes III: 0.5 for every 1 unit is a constant too]"},
             check=("many", ratios([2, 4, 6, 8], [1, 2, 3, 4], "F(1,2)"), at0([2, 4, 6, 8], [1, 2, 3, 4], "0"), ("true", "not F(1,2).is_integer"))),
        dict(stem="Which graph shows a proportional relationship?",
             fig=AD11,
             choices=["A", "B", "C", "D"], correct=2, answer="C",
             why="Graph C: 6 ÷ 2 = 9 ÷ 3 = 12 ÷ 4 = 3, so its points lie on a line through the origin.",
             errors={"A": "a constant rate of change taken for a constant ratio: y ÷ x is 7, then 4 [Florida B1G-M, AR.3.1: every linear relationship taken as proportional]", "B": "a straight line taken as proportional, though it passes through (0, 4) [Notes II: look at x = 0]", "D": "a graph through the origin taken as proportional, though it is a curve [Notes II: a proportional relationship is linear first]"},
             check=("many", ratios([2, 3, 4], [6, 9, 12], "3"), rates([1, 2, 3], [7, 8, 9], "1"), not_prop([1, 2, 3], [7, 8, 9]),
                    table_of("2*u**2", [0, 1, 2], [0, 2, 8]), ne("F(2,1)", "F(8,2)"),
                    table_of("2*u + 4", [0, 4], [4, 12]), not_prop_eq("2*u + 4"))),
        dict(heading="Explain."),
        dict(stem="Ava says the table with the x-values 4, 8, 12 and the y-values 7, 10, 13 shows a proportional relationship, because y increases by 3 every time. Is Ava correct? Explain.",
             answer="No, y is 4 when x is 0.", why="A constant increase makes the relationship linear. The rate of change is 3 for every 4 units, 0.75 for every 1 unit; back 4 units from x = 4 gives 7 − 4(0.75) = 4, so y is 4 when x is 0 (and y ÷ x is 1.75, then 1.25). It is not proportional.",
             check=("many", rates([4, 8, 12], [7, 10, 13], "F(3,4)"), at0([4, 8, 12], [7, 10, 13], "4"), not_prop([4, 8, 12], [7, 10, 13])), lines=3),
    ],

    te=dict(
        must="Students determine whether a linear relationship, given as a table, a graph, an equation or a description, is also a proportional relationship. They give the reason: y is 0 when x is 0, so the line passes through the origin, or y ÷ x is the same for every pair.",
        must_not="Students do not decide whether a table is linear at all; every relationship today is given as linear, and that question belongs to Unit 12. The words slope and y-intercept are not used yet; they arrive in Lessons 10.02 and 10.05.",
        materials="Students need whiteboards and markers, and each student needs one copy of the Independent Set.",
        variation="Whiteboard questions 1 and 2 use one table, and only the question changes. Question 3 takes away the pair for x = 0, question 4 is an equation and question 5 is four graphs. The pattern breaks at question 6, where y = 5(x + 2) has no number added at the end and still is not proportional. Question 7 is a story with an extra number, question 8 finds the value of y at x = 0 from two pairs, and question 9 is written. The Independent Set moves from a table with x = 0 to one without, then a graph, equations, a description and two tables.",
        audit=["Every table is checked by sympy at build time to have a constant rate of change, and every value of y at x = 0 is computed from the first pair and the rate. Every proportional table is checked pair by pair for one ratio, and every one that is not proportional is checked to have two different ratios.",
               "Every equation called proportional is checked to be linear with y equal to 0 at x = 0, and every one called not proportional to be linear with y not 0 at x = 0."],
        changes=["Nothing was taken from Math Nation; the lesson follows the unit's Lesson Outlines, section 10.01."],
        read_first=["Every relationship in this lesson is given as linear, so the only question is whether it is also proportional. Two reasons are accepted everywhere: y is 0 when x is 0, and y ÷ x is the same for every pair.",
                    "Notes III is the heart of the lesson: a table with no pair for x = 0 is still decided by going back to x = 0 at the rate of change."],
    ),
)
