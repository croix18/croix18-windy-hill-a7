# A7 7.02+03 Constant of Proportionality: Table, Graph, Description (MA.7.AR.4.2) — two book lessons, one day.
# Built from the unit's Lesson Outlines, section "7.02+03". Figures from u7/figs7.py.
# Checks: every constant is y ÷ x, computed by sympy from the printed numbers (decimals as exact Rationals).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs7 as figs
S = figs.slide

U = "sp.Symbol('u', real=True)"


def _u(e):
    import re
    return re.sub(r"\bu\b", U, e)


def solves(left, right, value):
    """sympy solves left = right (in u) and finds exactly one solution, `value`."""
    return ("eq", "sp.solve(sp.Eq(" + _u(left) + ", " + _u(right) + "), " + U + ")[0]", value)


def never(left, right):
    """left = right is never true: left − right simplifies to a nonzero number (no solution)."""
    d = "sp.expand(" + _u(left) + " - (" + _u(right) + "))"
    return ("true", "(" + d + ").is_number and " + d + " != 0")


def R(v):
    return "sp.Rational('" + str(v) + "')"


def ratios(xs, ys, p):
    """y ÷ x is p in every printed pair (a table, or the points read off a graph)."""
    return ("many",) + tuple(("eq", R(y) + " / " + R(x), p) for x, y in zip(xs, ys))


def B(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.75)


def BA(spec):
    return S(spec, inches=4.2, pt=18, reserve=0.95)


def TB(spec):
    """A table on a board's question slide."""
    return S(spec, inches=8.0, pt=18, reserve=0.75)


def TBA(spec):
    """The same table on the reveal, with room for the answer."""
    return S(spec, inches=7.0, pt=16, reserve=0.95)


def PL(xr, yr, **k):
    """A slide plane: 4.2 in, 18 pt."""
    return figs.plane(xr, yr, inches=4.2, pt=18, **k)


# ---- notes and examples
NOTES1 = S(figs.table([([2, 3, 5], [24, 36, 60])], head=("hours", "pay ($)")), inches=6.0, pt=22, reserve=1.2)
NOTES2 = S(figs.plane((0, 10), (0, 15), lines=[figs.prop(Fr(3, 2), "")], xs=2, ys=3,
                      points=[(4, 6, "on"), (8, 12, "on")], inches=4.0, pt=17), inches=4.0, pt=17, reserve=1.1)

EX1_T = figs.table([([2, 5, 8], ["13.00", "32.50", "52.00"])], head=("pounds", "cost ($)"), cw=1.7)
YT1_T = figs.table([([2, 4, 6], ["6.50", "13.00", "19.50"])], head=("pounds", "cost ($)"), cw=1.7)

EX2_P = figs.plane((-3, 7), (-10, 6), lines=[figs.prop(Fr(-4, 3), "")], ys=2,
                   points=[(3, -4, "on"), (6, -8, "on")], inches=4.2, pt=18)
YT2_P = figs.plane((-3, 7), (-10, 6), lines=[figs.prop(Fr(-5, 3), "")], ys=2,
                   points=[(3, -5, "on"), (6, -10, "on")], inches=4.2, pt=18)

# ---- the boards
T_COOK = figs.table([([2, 4, 7], [30, 60, 105])], head=("cups of flour", "cookies"))
T3 = figs.table([([3, 6, 12], [2, 4, 8])])
P4 = PL((0, 7), (0, 70), lines=[figs.prop(15, "")], ys=10, xname="hours", yname="miles",
        points=[(2, 30, "on"), (4, 60, "on")])
P5 = PL((0, 6), (0, 24), lines=[figs.prop(4, "")], ys=4, points=[(3, 12, "on")])
T8 = figs.table([([-4, 2, 6], [10, -5, -15])])
T9 = figs.table([([2, 4, 8], [10, 20, 40])])


def GRAPH(xr, yr, p, pts, **k):
    """A printed graph for the set and the banks: the line y = px through the origin, its readable points named."""
    return figs.plane(xr, yr, lines=[figs.prop(p, "")], points=[(a, b, "on") for a, b in pts], inches=3.0, **k)


L = dict(
    code="7.02", unit=7, lesson_no="2–3", label="Lessons 2–3",
    title="Constant of Proportionality: Table, Graph, Description",
    unit_title="Representing Proportional Relationships",
    benchmark="MA.7.AR.4.2",
    benchmark_text="Determine the constant of proportionality within a mathematical or real-world context given a table, graph or written description of a proportional relationship.",
    target="I can find the constant of proportionality from a table, a graph or a description, and explain what it means.",
    essential="Why is y ÷ x the same number for every pair of a proportional relationship, and what does that number tell us?",
    building_on="7.01 — a proportional relationship graphed from a description, a table or y = px: a straight line through the origin; the unit rate; read the scales first. Grade 6 (MA.6.AR.3.2) — unit rates.",
    working_toward="7.04 — is it proportional? (y ÷ x the same for every pair; a straight line through the origin; nothing added at the start); 7.05+06 — the equation y = px from the constant.",
    vocab=[("constant of proportionality", "the number $p$ in $y = px$. It equals $y \\div x$ for every pair: the amount of y for every 1 unit of x")],
    ixl=["Interpret graphs of proportional relationships — RMH", "Find the constant of proportionality from a table — LKZ",
         "Find the constant of proportionality from a graph — ZUT"],
    closure="Board 9 is written work and it is the exit evidence: Ben is right — y ÷ x is 10 ÷ 2 = 20 ÷ 4 = 40 ÷ 8 = 5, 5 units of y for every 1 unit of x; Ana divided x by y (2 ÷ 10 = 1/5), the ratio in the wrong order. A board that says only 'Ben' has the verdict and not the reason.",

    mtr=[("MTR.2.1", "one constant read three ways: a table, a graph, a description"),
         ("MTR.4.1", "boards 3, 5 and 6: a split room re-votes"),
         ("MTR.7.1", "every constant said with its unit, as what it means in the story")],
    hoq=[("Why must y ÷ x give the same number for every pair, not just the first?", "DOK 2"),
         ("On a graph scaled by 4, why does counting squares give the wrong constant?", "DOK 2"),
         ("120 miles on 5 gallons gives 24 and 1/24. Which is the constant, and who decides?", "DOK 3")],
    differentiation=[
        ("ESE / 504", "A printed card: \"constant = y ÷ x — y on top\", with the board's two quantities written as y and x before dividing. Notes I stays up from board 1 on."),
        ("ELL", "**Constant**: always the same. **Per**: for each one (dollars per pound: dollars for each pound). **Origin**: the point (0, 0)."),
        ("Enrichment", "Board 8 finishes early for some: make a table of three pairs with constant −2.5 in which no x is a whole number. (Any x with y = −2.5x, such as x 0.4, 1.2, 2.5 and y −1, −3, −6.25.)")],

    warmup=[
        dict(stem="$y = 4x$.  Find y when $x = 0$, $2$ and $5$.", answer="0, 8, 20",
             check=("many", ("eq", "4*0", "0"), ("eq", "4*2", "8"), ("eq", "4*5", "20"))),
        dict(stem="How many solutions does  $4(x - 1) = 4x + 3$  have?", answer="None",
             check=never("4*(u - 1)", "4*u + 3")),
        dict(stem="Solve:  $0.5(4x + 6) = 13$", answer="x = 5",
             check=solves("F(1,2)*(4*u + 6)", "13", "5")),
        dict(stem="Write $\\frac{7}{8}$ as a decimal.", answer="0.875",
             check=("eq", "F(7,8)", R("0.875"))),
    ],

    notes=[
        dict(numeral="I", head="From a table", min=4,
             fig=NOTES1,
             items2=["$24 \\div 2 = 12 \\qquad 36 \\div 3 = 12 \\qquad 60 \\div 5 = 12$:   12 dollars per hour.",
                     "**y ÷ x is the same for every pair.**"],
             letters=False),
        dict(numeral="II", head="From a graph", min=4,
             fig=NOTES2,
             items2=["**Read the scales first: the x-axis counts by 2.**",
                     "$(4, 6)$:   $6 \\div 4 = 1.5$.   Check $(8, 12)$:   $12 \\div 8 = 1.5$."],
             letters=False),
        dict(numeral="III", head="From a description — which quantity is y?", min=4,
             items=[("A car goes 120 miles on 5 gallons", "$120 \\div 5 = 24$ miles per gallon"),
                    ("With gallons as y", "$5 \\div 120 = \\frac{1}{24}$ gallon per mile")],
             items2=["There are two constants, each with its own unit. The question tells you which one to find.",
                     "**The constant is the amount of y for every 1 unit of x.**"],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=1,
             prompt=["Almonds cost the same amount per pound."], fig=S(EX1_T, inches=6.6, pt=20, reserve=1.0),
             ask="Find the constant of proportionality, in dollars per pound.",
             worked=[dict(min=2,
                          rows=[("13.00 \\div 2 = 6.50", "2 pounds"),
                                ("32.50 \\div 5 = 6.50", "5 pounds"),
                                ("52.00 \\div 8 = 6.50", "8 pounds: the same for every pair")],
                          fig=S(EX1_T, inches=5.4, pt=18, reserve=0.9), answer="$6.50 per pound")],
             check=ratios([2, 5, 8], ["13.00", "32.50", "52.00"], "F(13,2)"),
             your_turn=dict(min=2,
                            prompt=["Walnuts cost the same amount per pound."],
                            fig=S(YT1_T, inches=6.6, pt=20, reserve=1.0),
                            ask="Find the constant of proportionality, in dollars per pound.",
                            steps=["2 pounds:  $6.50 \\div 2 = 3.25$",
                                   "4 pounds:  $13.00 \\div 4 = 3.25$",
                                   "6 pounds:  $19.50 \\div 6 = 3.25$"],
                            answer="$3.25 per pound"),
             yt_check=ratios([2, 4, 6], ["6.50", "13.00", "19.50"], "F(13,4)")),
        dict(title="Example 2", min_q=1,
             prompt=["The line passes through the origin and the points $(3, -4)$ and $(6, -8)$."], fig=B(EX2_P),
             ask="Find the constant of proportionality.",
             worked=[dict(min=2,
                          rows=[("-4 \\div 3 = -\\frac{4}{3}", "the point (3, −4)"),
                                ("-8 \\div 6 = -\\frac{4}{3}", "check with (6, −8)"),
                                ("p = -\\frac{4}{3}", "a constant can be negative")],
                          fig=S(EX2_P, inches=4.2, pt=18, reserve=0.9), answer="p = −4/3")],
             check=ratios([3, 6], [-4, -8], "F(-4,3)"),
             your_turn=dict(min=2,
                            prompt=["The line passes through the origin and the points $(3, -5)$ and $(6, -10)$."], fig=B(YT2_P),
                            fig_a=BA(YT2_P), ask="Find the constant of proportionality.",
                            steps=["$(3, -5)$:  $-5 \\div 3 = -\\frac{5}{3}$",
                                   "Check $(6, -10)$:  $-10 \\div 6 = -\\frac{5}{3}$"],
                            answer="p = −5/3"),
             yt_check=ratios([3, 6], [-5, -10], "F(-5,3)")),
    ],

    # The round: a table in a context (1), the same table the other way (2: only which quantity is y changes), the
    # diagnostic on a bare table (3), a graph scaled by 10 (4), the diagnostic on a graph scaled by 4 (5), the
    # diagnostic on what a constant means (6), a description with an extra number (7), the pattern breaks at 8 — a
    # negative constant from a table — and the written verdict on a reversed ratio (9).
    whiteboard=[
        dict(text=["**What is the constant of proportionality, in cookies per cup?"],
             qtext="The table shows cups of flour and cookies: 2, 4, 7 cups make 30, 60, 105 cookies. What is the constant of proportionality, in cookies per cup?",
             fig=TB(T_COOK), fig_a=TBA(T_COOK),
             steps=["2 cups:  $30 \\div 2 = 15$", "4 cups:  $60 \\div 4 = 15$", "7 cups:  $105 \\div 7 = 15$"],
             answer="15 cookies per cup",
             check=ratios([2, 4, 7], [30, 60, 105], "15"),
             wrong="1/15 — cups ÷ cookies, the ratio in the wrong order [B1G-M, AR.4.2: ratio taken in the wrong order]; 28 — 30 − 2, subtracted [Notes I: y ÷ x is the same for every pair]"),
        # repeat_ok: the same table as board 1 on purpose — one thing changes, which quantity is y (the plan's board 2).
        dict(repeat_ok=True, text=["Use the same table.", "**What is the constant of proportionality, in cups of flour per cookie?"],
             qtext="Use the same table: 2, 4, 7 cups of flour make 30, 60, 105 cookies. What is the constant of proportionality, in cups of flour per cookie?",
             fig=TB(T_COOK), fig_a=TBA(T_COOK),
             steps=["Cups are y now:  $2 \\div 30 = \\frac{1}{15}$", "Check:  $4 \\div 60 = \\frac{1}{15}$  and  $7 \\div 105 = \\frac{1}{15}$"],
             answer="1/15 cup of flour per cookie",
             check=ratios([30, 60, 105], [2, 4, 7], "F(1,15)"),
             wrong="15 — board 1's constant, cookies per cup, kept [B1G-M, AR.4.2: ratio taken in the wrong order]"),
        # repeat_ok: rule D matches only the axis numbers of the Notes II and Example 2 grids (2, 4, 6, 8, 3, 12 as
        # tick labels) and the answer's digits; this table (x 3, 6, 12; y 2, 4, 8) appears nowhere above.
        dict(repeat_ok=True, kind="mc", text=["**What is the constant of proportionality?"],
             qtext="A table: x 3, 6, 12; y 2, 4, 8. What is the constant of proportionality?",
             fig=TB(T3), fig_a=TBA(T3),
             steps=["$2 \\div 3 = \\frac{2}{3}$", "Check:  $4 \\div 6 = \\frac{2}{3}$  and  $8 \\div 12 = \\frac{2}{3}$"],
             choices=["$1$", "$\\frac{2}{3}$", "$\\frac{3}{2}$", "$2$"], correct=1, answer="B — 2/3",
             errors={"A": "3 − 2, x and y subtracted [Notes I: y ÷ x is the same for every pair]", "C": "x ÷ y [B1G-M, AR.4.2: ratio taken in the wrong order]", "D": "the first y-value read as the constant [Notes III: the amount of y for every 1 unit of x]"},
             check=("many", ratios([3, 6, 12], [2, 4, 8], "F(2,3)"),
                    ("true", "F(3,2) != F(2,3)"), ("eq", "3 - 2", "1"), ("true", "1 != F(2,3)"), ("true", "2 != F(2,3)"))),
        dict(text=["The graph shows how far a cyclist rides.", "**What is the constant of proportionality, in miles per hour?"],
             qtext="A cyclist's graph of miles versus hours, a line through the origin, (2, 30) and (4, 60). What is the constant of proportionality, in miles per hour?",
             fig=B(P4), fig_a=S(P4, inches=4.2, pt=18, reserve=1.2),
             steps=["Read the scales first:  miles count by 10", "$(2, 30)$:  $30 \\div 2 = 15$", "Check $(4, 60)$:  $60 \\div 4 = 15$"],
             answer="15 miles per hour",
             check=ratios([2, 4], [30, 60], "15"),
             wrong="1.5 — three squares up for two across, the scale ignored [B1G-M, AR.4.2: axis scale ignored on a graph]; 30 — a y-value read off [Notes III: the amount of y for every 1 unit of x]"),
        dict(kind="mc", text=["**Find the constant of proportionality of the line."],
             qtext="A graph whose y-axis counts by 4: a line through the origin and (3, 12). What is the constant of proportionality?",
             fig=B(P5), fig_a=BA(P5),
             steps=["Read the scales first:  the y-axis counts by 4", "$(3, 12)$:  $12 \\div 3 = 4$"],
             choices=["$4$", "$\\frac{1}{4}$", "$12$", "$1$"], correct=0, answer="A — 4",
             errors={"B": "x ÷ y [B1G-M, AR.4.2: ratio taken in the wrong order]", "C": "a y-value read off as the constant [Notes III: the amount of y for every 1 unit of x]", "D": "3 squares up for 3 across, the scale ignored [B1G-M, AR.4.2: axis scale ignored on a graph]"},
             check=("many", ratios([3], [12], "4"), ("eq", "F(12, 4)/3", "1"), ("true", "1 != 4"),
                    ("eq", "F(3, 12)", "F(1,4)"), ("true", "F(1,4) != 4"), ("true", "12 != 4"))),
        dict(kind="mc", text=["5 pounds of rice cost \\$8.00. The constant of proportionality is 1.6.", "**What does 1.6 mean?"],
             qtext="5 pounds of rice cost $8.00; the constant of proportionality is 1.6. What does it mean?",
             steps=["$8.00 \\div 5 = 1.60$:  dollars ÷ pounds", "\\$1.60 per pound"],
             choices=["Each pound costs \\$8.00.", "Each dollar buys 1.6 pounds.", "The rice costs \\$1.60 before any is weighed.", "Each pound costs \\$1.60."], correct=3, answer="D — each pound costs $1.60",
             errors={"A": "a given number, the total cost, read off as the constant [Notes III: the amount of y for every 1 unit of x]", "B": "the constant read in the wrong order: each dollar buys 5 ÷ 8 = 0.625 pound [B1G-M, AR.4.2: ratio taken in the wrong order]", "C": "the constant read as a start: 0 pounds cost $0 [7.01: a straight line through the origin]"},
             check=("many", ("eq", R("8.00") + " / 5", R("1.6")), ("true", "F(5, 8) != " + R("1.6")),
                    ("true", R("8.00") + " != " + R("1.6")), ("eq", R("1.6") + " * 0", "0"))),
        dict(text=["A 3-year-old snail crawls 34 centimeters in 8 minutes at a steady speed.",
                   "**What is the constant of proportionality, in centimeters per minute?"],
             unneeded="3",
             steps=["Centimeters are y:  $34 \\div 8 = 4.25$"],
             answer="4.25 centimeters per minute",
             check=("eq", "F(34, 8)", R("4.25")),
             wrong="0.235… — 8 ÷ 34, minutes per centimeter [B1G-M, AR.4.2: ratio taken in the wrong order]; 34 ÷ 3 — the snail's age used [ruling 22]"),
        dict(text=["**What is the constant of proportionality?"],
             qtext="A table: x −4, 2, 6; y 10, −5, −15. What is the constant of proportionality?",
             fig=TB(T8), fig_a=TBA(T8),
             steps=["$10 \\div (-4) = -2.5$", "$-5 \\div 2 = -2.5$", "$-15 \\div 6 = -2.5$"],
             answer="−2.5",
             check=ratios([-4, 2, 6], [10, -5, -15], R("-2.5")),
             wrong="2.5 — the signs dropped [Example 2: a constant can be negative]; −0.4 — x ÷ y [B1G-M, AR.4.2: ratio taken in the wrong order]"),
        dict(kind="written", text=["Ana says the constant of proportionality is $\\frac{1}{5}$. Ben says it is 5.",
                                   "**Who is right? What mistake did the other student make?"],
             qtext="For x 2, 4, 8 and y 10, 20, 40, Ana says the constant of proportionality is 1/5 and Ben says it is 5. Who is right? What mistake did the other student make?",
             fig=TB(T9), fig_a=TBA(T9),
             steps=["y ÷ x:  $10 \\div 2 = 5$", "Check:  $20 \\div 4 = 5$  and  $40 \\div 8 = 5$", "Ana's:  $2 \\div 10 = \\frac{1}{5}$,  x ÷ y"],
             answer="Ben is right: y ÷ x = 5. Ana divided x by y.",
             check=("many", ratios([2, 4, 8], [10, 20, 40], "5"), ("eq", "F(2, 10)", "F(1,5)")),
             wrong="'Ana' — x ÷ y taken as the constant [B1G-M, AR.4.2: ratio taken in the wrong order]; 'both, they are the same' — a number and its reciprocal taken as one constant [Notes III: the question tells you which one to find]"),
    ],

    # The six: a table in a context with a decimal constant (1), a table with a fraction constant (2), a graph scaled by 1 (3),
    # a graph scaled by 5 and what its constant means (4), a description with the direction named (5), and the
    # pattern breaks at 6 — a negative constant from a table.
    # work room trimmed on questions 1–4 (21 Nov): in Lexend the set ran to a third page that Times did not need
    independent=[
        dict(stem="Bananas cost the same amount per pound. Find the constant of proportionality, in dollars per pound.",
             fig=figs.table([([2, 3, 6], ["1.18", "1.77", "3.54"])], head=("pounds", "cost ($)"), cw=1.7, inches=4.0),
             answer="$0.59 per pound", why="1.18 ÷ 2 = 0.59, 1.77 ÷ 3 = 0.59 and 3.54 ÷ 6 = 0.59: the same for every pair.",
             check=ratios([2, 3, 6], ["1.18", "1.77", "3.54"], R("0.59")), space=0.4),
        dict(stem="Find the constant of proportionality.",
             fig=figs.table([([7, 14, 35], [3, 6, 15])], inches=4.0),
             answer="3/7", why="3 ÷ 7 = 3/7, 6 ÷ 14 = 3/7 and 15 ÷ 35 = 3/7: y ÷ x, not x ÷ y (7/3).",
             check=("many", ratios([7, 14, 35], [3, 6, 15], "F(3,7)"), ("true", "F(7,3) != F(3,7)")), space=0.4),
        dict(stem="The line passes through the origin and the points $(4, 3)$ and $(8, 6)$. Find the constant of proportionality.",
             fig=GRAPH((0, 8), (0, 6), Fr(3, 4), [(4, 3), (8, 6)]),
             answer="3/4", why="3 ÷ 4 = 3/4; check: 6 ÷ 8 = 3/4.",
             check=ratios([4, 8], [3, 6], "F(3,4)"), space=0.35),
        dict(stem="The graph shows the money a car wash raises. Find the constant of proportionality, in dollars per car, and explain what it means.",
             fig=GRAPH((0, 6), (0, 45), Fr(15, 2), [(2, 15), (4, 30)], ys=5, xname="cars washed", yname="dollars raised"),
             answer="7.5. The car wash raises $7.50 per car.", why="Read the scales first: dollars count by 5. 15 ÷ 2 = 7.5 and 30 ÷ 4 = 7.5.",
             check=ratios([2, 4], [15, 30], R("7.5")), space=0.5),
        dict(stem="Lena runs 3 miles in 27 minutes at a steady pace. Find the constant of proportionality, in minutes per mile.",
             answer="9 minutes per mile", why="Minutes are y: 27 ÷ 3 = 9.",
             check=("eq", "F(27, 3)", "9"), space=0.6),
        dict(stem="Find the constant of proportionality.",
             fig=figs.table([([-8, 4, 12], [6, -3, -9])], inches=4.0),
             answer="−3/4 (−0.75)", why="6 ÷ (−8) = −3/4, −3 ÷ 4 = −3/4 and −9 ÷ 12 = −3/4: a negative constant.",
             check=ratios([-8, 4, 12], [6, -3, -9], "F(-3,4)"), space=0.6),
    ],

    # Bank: three tables (a context, bare, a negative), three graphs (scaled by 1, by 10, a negative), two
    # descriptions (each direction named), three diagnostics (a table, what a constant means, a scaled graph) and
    # one reversed ratio to judge. The additional bank mirrors it position by position with new numbers.
    bank=[
        dict(heading="Find the constant of proportionality from the table."),
        dict(stem="The table shows the number of marbles in different numbers of bags. Find the constant of proportionality, in marbles per bag.",
             fig=figs.table([([2, 5, 7], [18, 45, 63])], head=("bags", "marbles"), inches=3.6),
             answer="9 marbles per bag", why="18 ÷ 2 = 9, 45 ÷ 5 = 9, 63 ÷ 7 = 9.",
             check=ratios([2, 5, 7], [18, 45, 63], "9"), space=0.5),
        dict(stem="Find the constant of proportionality.",
             fig=figs.table([([4, 6, 10], [18, 27, 45])], inches=3.6),
             answer="4.5", why="18 ÷ 4 = 4.5, 27 ÷ 6 = 4.5, 45 ÷ 10 = 4.5.",
             check=ratios([4, 6, 10], [18, 27, 45], R("4.5")), space=0.5),
        dict(stem="Find the constant of proportionality.",
             fig=figs.table([([-2, 3, 8], [7, "−10.5", -28])], inches=3.6),
             answer="−3.5", why="7 ÷ (−2) = −3.5, −10.5 ÷ 3 = −3.5, −28 ÷ 8 = −3.5.",
             check=ratios([-2, 3, 8], [7, "-10.5", -28], R("-3.5")), space=0.5),
        dict(heading="Find the constant of proportionality from the graph."),
        dict(stem="The line passes through the origin and the points $(2, 5)$ and $(4, 10)$.",
             fig=GRAPH((0, 6), (0, 12), Fr(5, 2), [(2, 5), (4, 10)]),
             answer="2.5", why="5 ÷ 2 = 2.5; check: 10 ÷ 4 = 2.5.",
             check=ratios([2, 4], [5, 10], R("2.5")), space=0.4),
        dict(stem="The graph shows words typed at a steady speed. Find the constant of proportionality, in words per minute.",
             fig=GRAPH((0, 5), (0, 200), 40, [(1, 40), (3, 120)], ys=20, xname="minutes", yname="words"),
             answer="40 words per minute", why="Read the scales first: words count by 20. 40 ÷ 1 = 40; 120 ÷ 3 = 40.",
             check=ratios([1, 3], [40, 120], "40"), space=0.4),
        dict(stem="The line passes through the origin and the points $(3, -2)$ and $(6, -4)$.",
             fig=GRAPH((-3, 7), (-5, 3), Fr(-2, 3), [(3, -2), (6, -4)]),
             answer="−2/3", why="−2 ÷ 3 = −2/3; check: −4 ÷ 6 = −2/3.",
             check=ratios([3, 6], [-2, -4], "F(-2,3)"), space=0.4),
        dict(heading="Find the constant of proportionality from the description."),
        dict(stem="A recipe uses 6 cups of flour for 4 loaves of bread. Find the constant of proportionality, in cups per loaf.",
             answer="1.5 cups per loaf", why="Cups are y: 6 ÷ 4 = 1.5.", check=("eq", "F(6, 4)", R("1.5")), space=0.4),
        dict(stem="A bus travels 135 miles in 3 hours at a steady speed. Find the constant of proportionality, in hours per mile.",
             answer="1/45 hour per mile", why="Hours are y: 3 ÷ 135 = 1/45.", check=("eq", "F(3, 135)", "F(1,45)"), space=0.4),
        dict(heading="Choose one."),
        dict(stem="A table shows x-values 4, 8 and 10 with y-values 10, 20 and 25. What is the constant of proportionality?",
             choices=["$\\frac{2}{5}$", "$6$", "$\\frac{5}{2}$", "$10$"], correct=2, answer="C",
             why="10 ÷ 4 = 20 ÷ 8 = 25 ÷ 10 = 5/2.",
             check=("many", ratios([4, 8, 10], [10, 20, 25], "F(5,2)"), ("true", "F(2,5) != F(5,2)"),
                    ("eq", "10 - 4", "6"), ("true", "6 != F(5,2)"), ("true", "10 != F(5,2)")),
             errors={"A": "x ÷ y [B1G-M, AR.4.2: ratio taken in the wrong order]", "B": "10 − 4, subtracted [Notes I: y ÷ x is the same for every pair]", "D": "the first y-value read as the constant [Notes III: the amount of y for every 1 unit of x]"}),
        dict(stem="A plant grows 6 inches in 4 weeks at a steady rate. The constant of proportionality is 1.5. What does 1.5 mean?",
             choices=["The plant grows 6 inches each week.", "The plant was 1.5 inches tall at the start.", "Each inch takes 1.5 weeks.", "The plant grows 1.5 inches each week."], correct=3, answer="D",
             why="6 ÷ 4 = 1.5: inches ÷ weeks, 1.5 inches per week.",
             check=("many", ("eq", "F(6, 4)", R("1.5")), ("true", "F(4, 6) != " + R("1.5")), ("true", "6 != " + R("1.5")),
                    ("eq", R("1.5") + " * 0", "0")),
             errors={"A": "a given number read off as the constant [Notes III: the amount of y for every 1 unit of x]", "B": "the constant read as a start [7.01: a straight line through the origin]", "C": "the constant read in the wrong order: each inch takes 4 ÷ 6 = 2/3 week [B1G-M, AR.4.2: ratio taken in the wrong order]"}),
        dict(stem="The line passes through the origin and $(2, 15)$. What is the constant of proportionality?",
             fig=GRAPH((0, 5), (0, 30), Fr(15, 2), [(2, 15)], ys=5),
             choices=["$\\frac{15}{2}$", "$\\frac{2}{15}$", "$15$", "$\\frac{3}{2}$"], correct=0, answer="A",
             why="Read the scales first: y counts by 5. 15 ÷ 2 = 7.5.",
             check=("many", ratios([2], [15], "F(15,2)"), ("eq", "F(15, 5)/2", "F(3,2)"), ("true", "F(3,2) != F(15,2)"),
                    ("true", "F(2,15) != F(15,2)"), ("true", "15 != F(15,2)")),
             errors={"B": "x ÷ y [B1G-M, AR.4.2: ratio taken in the wrong order]", "C": "a y-value read off as the constant [Notes III: the amount of y for every 1 unit of x]", "D": "3 squares up for 2 across, the scale ignored [B1G-M, AR.4.2: axis scale ignored on a graph]"}),
        dict(heading="Explain."),
        dict(stem="A table has x-values 3, 6 and 9 and y-values 1, 2 and 3. Sam says the constant of proportionality is 3. Is Sam right? Explain.",
             answer="No. y ÷ x = 1/3; Sam divided x by y.", why="1 ÷ 3 = 2 ÷ 6 = 3 ÷ 9 = 1/3. Sam's 3 is 3 ÷ 1, x ÷ y.",
             check=("many", ratios([3, 6, 9], [1, 2, 3], "F(1,3)"), ("true", "3 != F(1,3)")), space=0.6),
    ],

    additional=[
        dict(heading="Find the constant of proportionality from the table."),
        dict(stem="The table shows the number of crayons in different numbers of boxes. Find the constant of proportionality, in crayons per box.",
             fig=figs.table([([3, 4, 6], [24, 32, 48])], head=("boxes", "crayons"), inches=3.6),
             answer="8 crayons per box", why="24 ÷ 3 = 8, 32 ÷ 4 = 8, 48 ÷ 6 = 8.",
             check=ratios([3, 4, 6], [24, 32, 48], "8"), space=0.5),
        dict(stem="Find the constant of proportionality.",
             fig=figs.table([([2, 6, 10], [21, 63, 105])], inches=3.6),
             answer="10.5", why="21 ÷ 2 = 10.5, 63 ÷ 6 = 10.5, 105 ÷ 10 = 10.5.",
             check=ratios([2, 6, 10], [21, 63, 105], R("10.5")), space=0.5),
        dict(stem="Find the constant of proportionality.",
             fig=figs.table([([-4, 2, 10], [18, -9, -45])], inches=3.6),
             answer="−4.5", why="18 ÷ (−4) = −4.5, −9 ÷ 2 = −4.5, −45 ÷ 10 = −4.5.",
             check=ratios([-4, 2, 10], [18, -9, -45], R("-4.5")), space=0.5),
        dict(heading="Find the constant of proportionality from the graph."),
        dict(stem="The line passes through the origin and the points $(3, 4)$ and $(6, 8)$.",
             fig=GRAPH((0, 7), (0, 10), Fr(4, 3), [(3, 4), (6, 8)]),
             answer="4/3", why="4 ÷ 3 = 4/3; check: 8 ÷ 6 = 4/3.",
             check=ratios([3, 6], [4, 8], "F(4,3)"), space=0.4),
        dict(stem="The graph shows water running from a faucet at a steady rate. Find the constant of proportionality, in gallons per minute.",
             fig=GRAPH((0, 5), (0, 50), 10, [(2, 20), (4, 40)], ys=10, xname="minutes", yname="gallons"),
             answer="10 gallons per minute", why="Read the scales first: gallons count by 10. 20 ÷ 2 = 10; 40 ÷ 4 = 10.",
             check=ratios([2, 4], [20, 40], "10"), space=0.4),
        dict(stem="The line passes through the origin and the points $(2, -5)$ and $(4, -10)$.",
             fig=GRAPH((-2, 5), (-12, 6), Fr(-5, 2), [(2, -5), (4, -10)], ys=2),
             answer="−5/2", why="−5 ÷ 2 = −5/2; check: −10 ÷ 4 = −5/2.",
             check=ratios([2, 4], [-5, -10], "F(-5,2)"), space=0.4),
        dict(heading="Find the constant of proportionality from the description."),
        dict(stem="A painter uses 3 gallons of paint for 4 rooms. Find the constant of proportionality, in gallons per room.",
             answer="0.75 gallon per room", why="Gallons are y: 3 ÷ 4 = 0.75.", check=("eq", "F(3, 4)", R("0.75")), space=0.4),
        dict(stem="A truck travels 168 miles in 4 hours at a steady speed. Find the constant of proportionality, in hours per mile.",
             answer="1/42 hour per mile", why="Hours are y: 4 ÷ 168 = 1/42.", check=("eq", "F(4, 168)", "F(1,42)"), space=0.4),
        dict(heading="Choose one."),
        dict(stem="A table shows x-values 6, 9 and 12 with y-values 8, 12 and 16. What is the constant of proportionality?",
             choices=["$8$", "$\\frac{4}{3}$", "$2$", "$\\frac{3}{4}$"], correct=1, answer="B",
             why="8 ÷ 6 = 12 ÷ 9 = 16 ÷ 12 = 4/3.",
             check=("many", ratios([6, 9, 12], [8, 12, 16], "F(4,3)"), ("eq", "8 - 6", "2"), ("true", "2 != F(4,3)"),
                    ("true", "8 != F(4,3)"), ("true", "F(3,4) != F(4,3)")),
             errors={"A": "the first y-value read as the constant [Notes III: the amount of y for every 1 unit of x]", "C": "8 − 6, subtracted [Notes I: y ÷ x is the same for every pair]", "D": "x ÷ y [B1G-M, AR.4.2: ratio taken in the wrong order]"}),
        dict(stem="Printer ink costs the same amount per cartridge, and 4 cartridges cost \\$30.00. The constant of proportionality is 7.5. What does 7.5 mean?",
             choices=["Each cartridge costs \\$30.00.", "The ink costs \\$7.50 before any is bought.", "Each cartridge costs \\$7.50.", "Each dollar buys 7.5 cartridges."], correct=2, answer="C",
             why="30.00 ÷ 4 = 7.50: dollars ÷ cartridges, $7.50 per cartridge.",
             check=("many", ("eq", R("30.00") + " / 4", R("7.5")), ("true", "F(4, 30) != " + R("7.5")),
                    ("eq", R("7.5") + " * 0", "0"), ("true", R("30.00") + " != " + R("7.5"))),
             errors={"A": "a given number read off as the constant [Notes III: the amount of y for every 1 unit of x]", "B": "the constant read as a start [7.01: a straight line through the origin]", "D": "the constant read in the wrong order: each dollar buys 4 ÷ 30 cartridge [B1G-M, AR.4.2: ratio taken in the wrong order]"}),
        dict(stem="The line passes through the origin and $(3, 8)$. What is the constant of proportionality?",
             fig=GRAPH((0, 5), (0, 12), Fr(8, 3), [(3, 8)], ys=2),
             choices=["$8$", "$\\frac{4}{3}$", "$\\frac{3}{8}$", "$\\frac{8}{3}$"], correct=3, answer="D",
             why="Read the scales first: y counts by 2. 8 ÷ 3 = 8/3.",
             check=("many", ratios([3], [8], "F(8,3)"), ("eq", "F(8, 2)/3", "F(4,3)"), ("true", "F(4,3) != F(8,3)"),
                    ("true", "F(3,8) != F(8,3)"), ("true", "8 != F(8,3)")),
             errors={"A": "a y-value read off as the constant [Notes III: the amount of y for every 1 unit of x]", "B": "4 squares up for 3 across, the scale ignored [B1G-M, AR.4.2: axis scale ignored on a graph]", "C": "x ÷ y [B1G-M, AR.4.2: ratio taken in the wrong order]"}),
        dict(heading="Explain."),
        dict(stem="A table has x-values 4, 8 and 12 and y-values 1, 2 and 3. Mia says the constant of proportionality is 4. Is Mia right? Explain.",
             answer="No. y ÷ x = 1/4; Mia divided x by y.", why="1 ÷ 4 = 2 ÷ 8 = 3 ÷ 12 = 1/4. Mia's 4 is 4 ÷ 1, x ÷ y.",
             check=("many", ratios([4, 8, 12], [1, 2, 3], "F(1,4)"), ("true", "4 != F(1,4)")), space=0.6),
    ],

    te=dict(
        must="The constant from a table, graph (readable points) or description, and its meaning in context; negative constants.",
        must_not="\"Slope\"; constants that must be estimated from a graph with no readable point (state: begin with identifiable points).",
        read_first=[
            "Two book lessons (7.2 and 7.3) taught as one day. Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §7.02+03, standing decisions 2–6), with Math Nation read for scope only.",
            "Today names the constant of proportionality: yesterday's unit rate, the p in y = px, y ÷ x for every pair. Every constant is said with its unit (dollars per pound), and which quantity is y is said in every item: board 2 asks board 1's table the other way around. Negative constants are taught in a bare context only (Example 2, board 8). No 'slope' on any page."],
        materials="Whiteboards and markers. The Independent Set, one per student.",
        variation="Boards 1–2 read one table both ways (only which quantity is y changes); 3 votes on a bare table; 4 reads a graph scaled by 10, 5 votes on one scaled by 4, 6 votes on what a constant means; 7 is a description with an extra number (the snail's age). The pattern breaks at 8 — a negative constant from a table — and 9 judges a reversed ratio, written. The set: a table with a decimal, a table with a fraction constant, a graph by 1, a graph by 5 with its meaning, a description with the direction named, then a negative constant.",
        audit=["Every constant re-derived by sympy at build time as y ÷ x for every printed pair, decimals read as exact numbers; every graph drawn from y = px by u7/figs7.py, which refuses a marked point not on its line.",
               "Every wrong option is one named error: the ratio reversed, the scale ignored, a given number read off, a subtraction, or the constant read as a start."],
        changes=["7.2 and 7.3 (table; graph and description) → one day: Notes I–III, one Example each for a table and a graph, the description in Notes III and boards 6–7.",
                 "Practice and Homework → the Independent Set: six questions, one feature changed at a time."],
    ),
)
