# A7 7.05–06 Writing Equations; Translating Representations (MA.7.AR.4.4) — one deck,
# two book lessons (7.5 and 7.6) taught as one day, Mon 11 Jan 2027. Built from the unit's Lesson Outlines, §7.05+06.
# Checks are sympy over exact rationals: a printed decimal is read as sp.Rational('22.50'), never a float.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs7 as figs
S = figs.slide
BLANK = figs.BLANK

U = "sp.Symbol('u', real=True)"


def _u(e):
    import re
    return re.sub(r"\bu\b", U, e)


def R(s):
    """A printed number as an exact rational."""
    return "sp.Rational('" + str(s) + "')"


def solves(left, right, value):
    """sympy solves left = right (in u) and finds exactly one solution, `value`."""
    return ("eq", "sp.solve(sp.Eq(" + _u(left) + ", " + _u(right) + "), " + U + ")[0]", value)


def ratios(xs, ys, p):
    """y ÷ x is p for every pair of a printed table."""
    return ("many",) + tuple(("eq", R(y) + "/" + R(x), p) for x, y in zip(xs, ys))


def on(p, xs, ys):
    """Every (x, y) given makes y = p·x true."""
    return ("many",) + tuple(("eq", "(" + p + ")*" + R(x), R(y)) for x, y in zip(xs, ys))


def off(p, x, y):
    """(x, y) does NOT make y = p·x true."""
    return ("true", "(" + p + ")*" + R(x) + " != " + R(y))


def offb(m, b, x, y):
    """(x, y) does NOT make y = m·x + b true."""
    return ("true", "(" + m + ")*" + R(x) + " + (" + b + ") != " + R(y))


TH = dict(inches=8.0, pt=22, reserve=0.75)     # a board's table, question slide
THA = dict(inches=5.2, pt=18, reserve=0.95)    # a board's table, reveal


def ST(rows, head, inches, pt, reserve, cw=1.25):
    """A slide table: lettered for the size it is drawn at."""
    return S(figs.table(rows, head=head, cw=cw, inches=inches, pt=pt), inches=inches, pt=pt, reserve=reserve)


def BT(rows, head, a=False, cw=1.25):
    return ST(rows, head, cw=cw, **(THA if a else TH))


def BP(spec, a=False):
    return S(spec, inches=4.2, pt=18, reserve=0.95 if a else 0.75)


def PL(*a, **k):
    """A slide plane: lettered for the 4.2-in size it is drawn at."""
    return figs.plane(*a, inches=4.2, pt=18, **k)


# ---- notes
NOTES1 = ST([([3, 4, 6], ["22.50", "30.00", "45.00"])], ("tickets n", "cost c ($)"), 6.0, 22, 1.6, cw=2.3)
NOTES2 = S(figs.plane((0, 10), (0, 8), lines=[figs.prop(Fr(4, 5), "")], points=[(5, 4, "on")], inches=4.2, pt=18),
           inches=4.2, pt=18, reserve=0.6)

# ---- Example 1 (Maya, $120 for 4 hours) and its Your Turn (Theo, $160 for 4 hours)
EX1T = ST([([0, 2, 4, 6], [0, 60, 120, 180])], ("hours h", "dollars e"), 5.4, 20, 0.9, cw=1.6)
EX1G = S(figs.plane((0, 6), (0, 180), lines=[figs.prop(30, "")], ys=20, xname="hours", yname="dollars",
                    points=[(2, 60, "on"), (4, 120, "on")], inches=2.6, pt=16), inches=2.6, pt=16, reserve=1.15)
YT1 = ST([([0, 2, 4, 6], [BLANK, BLANK, BLANK, BLANK])], ("hours h", "dollars e"), 5.4, 20, 0.9, cw=1.6)
# The answer slide shows the filled table (the ruling allows, but does not need, the graph).
YT1A = ST([([0, 2, 4, 6], [0, 80, 160, 240])], ("hours h", "dollars e"), 4.6, 16, 0.9, cw=1.6)

# ---- the boards
B1 = ([2, 3, 7], [16, 24, 56])
B2 = ([2, 4, 5], ["19.00", "38.00", "47.50"])
P3 = PL((0, 8), (0, 6), lines=[figs.prop(Fr(1, 3), "")], points=[(6, 2, "on")])
B9 = ([8, 12, 20], [2, 3, 5])


# ---- the papers
def TP(rows, head, inches=4.2, cw=1.6):
    return figs.table(rows, head=head, inches=inches, cw=cw)


L = dict(
    code="7.05", unit=7, lesson_no="5–6", label="Lessons 5–6",
    align="=",
    title="Writing Equations; Translating Representations",
    unit_title="Representing Proportional Relationships",
    benchmark="MA.7.AR.4.4",
    benchmark_text="Given any representation of a proportional relationship, translate the representation to a written description, table or equation.",
    target="I can write the equation y = px from a table, a graph or a description, and translate from one representation to another.",
    essential="How does one number, the constant of proportionality, let us write the same relationship as a table, a graph, an equation and a sentence?",
    building_on="Lesson 7.04 tested whether a relationship is proportional from a table, a graph and a description, including linear relationships that are also proportional. Lessons 7.02–03 found the constant from a table, a graph and a description. In Grade 6, students solved one-step equations.",
    working_toward="Lesson 7.07 compares proportional relationships by finding each one's constant and then answering the question asked. In Unit 10 (January), the constant is named as the slope of y = px.",
    vocab=[("equation of a proportional relationship", "y = px, where p is the constant of proportionality (some books write k)")],
    ixl=["Write equations for proportional relationships from tables — 6GU",
         "Write equations for proportional relationships from graphs — JKH",
         "Write and solve equations for proportional relationships — VKK"],
    closure="Whiteboard question 9 is answered in writing and serves as the exit ticket. A complete answer says that Lee divided x by y. Because y ÷ x is the same for every pair and 2 ÷ 8 = 1/4, the equation is y = (1/4)x, and the check (1/4)(20) = 5 holds. An answer with the right equation but no check, or with no explanation of the mistake, is only half complete.",

    mtr=[("MTR.2.1", "Students show one relationship as a table, a graph, an equation and a sentence (Example 1 and whiteboard questions 6 and 8)."),
         ("MTR.4.1", "On whiteboard questions 3 and 5, a divided class has sixty seconds to convince a neighbor and then votes again."),
         ("MTR.6.1", "Students check every equation by substituting a pair of values (Notes I and whiteboard question 9).")],
    hoq=[("Why is one pair from a table enough to find p, but not enough to know the table is proportional?", "DOK 2"),
         ("m = 60h and h = (1/60)m: how can one relationship have two constants?", "DOK 3"),
         ("On whiteboard question 3, the line passes through (6, 2). Why is y = 6x wrong, and how could you see it without dividing?", "DOK 2"),
         ("How can you tell from an equation alone that its graph goes through the origin?", "DOK 2")],
    differentiation=[
        ("ESE / 504", "Provide a card that shows the three forms side by side (a table, y ÷ x and y = px) with the line “y ÷ x is the same for every pair” printed on it. Keep Notes I on display for whiteboard questions 1 and 2."),
        ("ELL", "**Equation**: a sentence with an equals sign, c = 7.5n. **Constant**: the number that stays the same, the amount of y for every 1 unit of x. **y**: the quantity the equation gives, alone on one side."),
        ("Enrichment", "After whiteboard question 8, students write question 7's equation the other way around, giving the minutes t for d miles (t = (1/9)d), and explain what 1/9 means: one ninth of a minute per mile.")],

    warmup=[
        dict(stem="For (3, 5), (6, 10) and (9, 16), is y proportional to x?", answer="No",
             check=("many", ("eq", "F(5,3)", "F(10,6)"), ("true", "F(16,9) != F(5,3)"))),
        dict(stem="Twelve pencils cost \\$3. Find the constant, in dollars per pencil.", answer="0.25",
             check=("eq", "F(3,12)", R("0.25"))),
        dict(stem="Solve:  $3(x + 4) + 2x = 37$", answer="x = 5",
             check=solves("3*(u + 4) + 2*u", "37", "5")),
        dict(stem="Solve:  $8x = 52$", answer="x = 6.5",
             check=solves("8*u", "52", R("6.5"))),
    ],

    notes=[
        dict(numeral="I", head="From a table", min=3,
             fig=NOTES1,
             math=["$p = 22.50 \\div 3 = 7.5$", "$c = 7.5n$"],
             items2=["y ÷ x is the same for every pair:  30.00 ÷ 4 = 7.5.   Check:  7.5(6) = 45."],
             letters=False),
        dict(numeral="II", head="From a graph or a description", min=3,
             fig=NOTES2,
             items=[("Graph", "the point $(5, 4)$:  $p = 4 \\div 5 = \\frac{4}{5}$,  so  $y = \\frac{4}{5}x$"),
                    ("Description", "a printer prints 22 sheets per minute:  s = 22m")],
             items2=["The constant of proportionality is the amount of y for every 1 unit of x."],
             letters=False),
        dict(numeral="III", head="An equation for either quantity", min=3,
             items=[("Minutes from hours", "$m = 60h$:  60 minutes per hour"),
                    ("Hours from minutes", "$h = \\frac{1}{60}m$:  $\\frac{1}{60}$ hour per minute")],
             items2=["One relationship, 60 minutes in 1 hour, has two constants. The question tells you which quantity the equation is for."],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=1,
             prompt=["Maya earns \\$120 for 4 hours of work, the same amount each hour.",
                     "Let e represent her earnings, in dollars, after h hours."],
             ask="Find the constant and the equation. Then make a table and a graph.",
             worked=[dict(min=1,
                          rows=[("p = 120 \\div 4 = 30", "dollars per hour"),
                                ("e = 30h", "the equation"),
                                ("30(2) = 60,\\quad 30(6) = 180", "the table, at hours 0, 2, 4, 6")],
                          fig=EX1T, answer="e = 30h"),
                     dict(min=1,
                          rows=["Read the scales first: the dollars axis counts by 20.",
                                ("(0, 0),\\ (2, 60),\\ (4, 120)", "points from the table"),
                                "Draw the straight line through the origin."],
                          fig=EX1G, answer="The line through (0, 0) and (2, 60)")],
             check=("many", ("eq", "F(120,4)", "30"), on("30", [0, 2, 4, 6], [0, 60, 120, 180])),
             # repeat_ok: rule 43 matches 160 and 40 only on Example 1's dollars axis (0 to 180 by 20) and the hours
             # 0, 2, 4, 6 that every table in this structure shares (rule 5: same structure, new numbers).
             your_turn=dict(repeat_ok=True, min=4,
                            prompt=["Theo earns \\$160 for 4 hours at a constant rate."],
                            ask="Find the constant, the equation for e, the table and two graph points.",
                            fig=YT1, fig_a=YT1A,
                            steps=["Constant:  $160 \\div 4 = 40$ dollars per hour",
                                   "Equation:  $e = 40h$",
                                   "Table:  $40(2) = 80$,  $40(4) = 160$,  $40(6) = 240$",
                                   "Graph:  through $(0, 0)$ and $(2, 80)$"],
                            answer="e = 40h"),
             yt_check=("many", ("eq", "F(160,4)", "40"), on("40", [0, 2, 4, 6], [0, 80, 160, 240]))),
        dict(title="Example 2", min_q=1,
             prompt=["A recipe uses 3 cups of flour for every 2 cups of sugar.",
                     "Let f represent the cups of flour and s the cups of sugar."],
             ask="Write the equation for f. How much sugar goes with 10.5 cups of flour?",
             # Two worked slides: with the ruled line "2 ÷ 3 = 2/3" the five rows ran the answer into the footer, even
             # with 10.5 = 1.5s and s = 7 joined (ruling 7.05/3's fallback) — so the other way around is its own slide.
             worked=[dict(min=1,
                          rows=[("p = 3 \\div 2 = 1.5", "cups of flour per cup of sugar"),
                                ("f = 1.5s", "the equation"),
                                ("10.5 = 1.5s", "10.5 cups of flour"),
                                ("s = 7", "divide both sides by 1.5")],
                          answer="7 cups of sugar"),
                     dict(min=1,
                          rows=[("2 \\div 3 = \\frac{2}{3}", "cup of sugar per cup of flour"),
                                ("s = \\frac{2}{3}f:\\quad \\frac{2}{3}(10.5) = 7", "the other way around: 7 again")],
                          answer="7 cups of sugar")],
             check=("many", ("eq", "F(3,2)", R("1.5")), solves(R("1.5") + "*u", R("10.5"), "7"),
                    ("eq", "F(2,3)*" + R("10.5"), "7"), ("eq", "1/" + R("1.5"), "F(2,3)"), ("eq", "sp.Integer(2)/3", "F(2,3)")),
             your_turn=dict(min=2,
                            prompt=["A car goes 150 miles on 6 gallons of gas.",
                                    "Let m represent the miles it goes on g gallons."],
                            ask="Write the equation for m. How much gas does it use in 350 miles?",
                            steps=["Constant:  $150 \\div 6 = 25$ miles per gallon",
                                   "Equation:  $m = 25g$;  solve  $350 = 25g$,  so  $g = 14$",
                                   "$6 \\div 150 = \\frac{1}{25}$ gallon per mile",
                                   "The other way around:  $g = \\frac{1}{25}m$,  $\\frac{1}{25}(350) = 14$"],
                            answer="m = 25g; 14 gallons"),
             yt_check=("many", ("eq", "F(150,6)", "25"), solves("25*u", "350", "14"), ("eq", "F(6,150)", "F(1,25)"), ("eq", "F(1,25)*350", "14"))),
    ],

    # The round: the equation from a table (1) and from a table with money and named letters (2); the vote on a
    # graph's equation (3); from a description (4); the vote on which letter is alone (5); the pattern breaks at 6 —
    # a table FROM an equation, its last x found backward; the plane story with its passengers as the extra number
    # (7); an equation said as a sentence (8); Lee's x ÷ y, written (9).
    whiteboard=[
        dict(text=["**Write the equation for the table."],
             fig=BT([B1], ("x", "y")), fig_a=BT([B1], ("x", "y"), a=True),
             steps=["y ÷ x:  $16 \\div 2 = 8$", "$24 \\div 3 = 8$", "$56 \\div 7 = 8$",
                    "the equation:  $y = 8x$"],
             answer="y = 8x",
             check=ratios(*B1, "8"),
             wrong="y = (1/8)x — x ÷ y [B1G-M, AR.4.2: the ratio taken in the wrong order]; y = x + 14 — the first pair's difference taken as the rule [B1G-M, AR.4.1: a constant difference taken for a constant ratio]"),
        dict(text=["**Write the equation for d, the dollars earned, after h hours."],
             fig=BT([B2], ("hours h", "dollars d"), cw=2.3), fig_a=BT([B2], ("hours h", "dollars d"), a=True, cw=2.3),
             steps=["d ÷ h:  $19.00 \\div 2 = 9.5$", "$38.00 \\div 4 = 9.5$", "$47.50 \\div 5 = 9.5$",
                    "the equation:  $d = 9.5h$"],
             answer="d = 9.5h",
             check=ratios(*B2, R("9.5")),
             wrong="h = 9.5d — the letters swapped [B1G-M, AR.4.2: the ratio taken in the wrong order]; d = 19h — the first dollars value taken as the constant [Notes I: y ÷ x, not y]"),
        # repeat_ok: rule D matches only the grid's axis numbers (0 to 8, shared with Notes II's grid) and the answer's
        # digits; the line y = (1/3)x appears nowhere above.
        dict(repeat_ok=True, kind="mc", text=["**What is the equation of the line?"],
             fig=BP(P3), fig_a=BP(P3, a=True),
             steps=["y ÷ x:  $2 \\div 6 = \\frac{1}{3}$", "check:  $\\frac{1}{3}(6) = 2$"],
             choices=["$y = 6x$", "$y = x - 4$", "$y = \\frac{1}{3}x$", "$y = 3x$"], correct=2,
             answer="C — y = (1/3)x",
             errors={"A": "the x-coordinate taken as the constant [B1G-M, AR.4.2: a coordinate read off as the constant]", "B": "the difference 6 − 2 subtracted: it passes through (6, 2) but not the origin [Notes II: the constant is the amount of y for every 1 unit of x]", "D": "x ÷ y, 6 ÷ 2 [B1G-M, AR.4.2: the ratio taken in the wrong order]"},
             check=("many", on("F(1,3)", [0, 6], [0, 2]), ("eq", "F(2,6)", "F(1,3)"),
                    off("3", 6, 2), off("6", 6, 2), offb("1", "-4", 0, 0), ("eq", "6 - 4", "2"))),
        dict(text=["Each carton holds 18 eggs.", "**Write the equation for the number of eggs e in c cartons."],
             steps=["18 eggs per carton:  $p = 18$", "the equation:  $e = 18c$"],
             answer="e = 18c",
             check=("many", ("eq", "18*c/c", "18"), ("eq", "18*1", "18")),
             wrong="c = 18e — the quantities swapped [B1G-M, AR.4.2: the ratio taken in the wrong order]; e = c + 18 — the 18 added [Notes II: nothing added at the start]"),
        dict(kind="mc", text=["A mile is about 1.6 kilometers.", "**Which equation gives d, the distance in kilometers, for m miles?"],
             steps=["1.6 kilometers per mile:  $p = 1.6$", "kilometers = 1.6 · miles:  $d = 1.6m$"],
             choices=["$m = 1.6d$", "$d = 1.6m$", "$d = m + 1.6$", "$d = 1.6$"], correct=1,
             answer="B — d = 1.6m",
             errors={"A": "x and y reversed: miles as y [B1G-M, AR.4.2: the ratio taken in the wrong order]", "C": "the constant added, not multiplied [7.04 Notes III: y = px, nothing added]", "D": "the constant written as the equation, with no m [Vocabulary: y = px]"},
             check=("many", on(R("1.6"), [1, 5], ["1.6", 8]), ("true", "1/" + R("1.6") + " != " + R("1.6")),
                    offb("1", R("1.6"), 5, 8), ("true", R("1.6") + " != 8"))),
        dict(text=["**Complete the table for $y = 2.4x$."],
             fig=BT([([5, 10, BLANK], [BLANK, BLANK, 36])], ("x", "y")),
             fig_a=BT([([5, 10, 15], [12, 24, 36])], ("x", "y"), a=True),
             steps=["$2.4(5) = 12$", "$2.4(10) = 24$", "work backward:  $36 = 2.4x$,  so  $x = 15$"],
             answer="y = 12 and 24; x = 15",
             check=("many", on(R("2.4"), [5, 10], [12, 24]), solves(R("2.4") + "*u", "36", "15")),
             wrong="86.4 for the last x — 2.4 · 36, multiplied going backward [B1G-M, AR.4.4: the equation used the wrong way around]; 33.6 — 36 − 2.4, subtracted [Notes I: y = px]"),
        dict(text=["A plane carrying 180 passengers flies 9 miles every minute.",
                   "**Write the equation for d, its distance in miles, after t minutes.",
                   "**How far does it fly in 40 minutes?"],
             unneeded="180",
             steps=["9 miles per minute:  $d = 9t$", "$d = 9(40) = 360$"],
             answer="d = 9t; 360 miles",
             check=("many", ("eq", "9*40", "360")),
             wrong="d = 180t — the passengers taken as the rate [an extra number, included on purpose]; 49 — 9 + 40, added [Notes II: y = px]"),
        # repeat_ok: rule 43 matches only the 12 (and 1) shared with warm-up 2's 12 pencils — a coincidence of values.
        dict(repeat_ok=True, text=["The equation $t = 12c$ gives the minutes t it takes to wash c cars.",
                   "**What does the 12 tell you? Answer in a complete sentence."],
             steps=["12 minutes per car:  $12(1) = 12$"],
             answer="Each car takes 12 minutes to wash.",
             check=("eq", "12*1", "12"),
             wrong="'12 cars are washed each minute' — the quantities reversed [B1G-M, AR.4.2: the ratio taken in the wrong order]; 'it takes 12 minutes in all' — the constant read as a total [Notes II: the amount of y for every 1 unit of x]"),
        dict(kind="written", text=["Lee writes $y = 4x$ for this table.", "**What mistake did Lee make? What is the correct equation?"],
             qtext="For the table x 8, 12, 20 and y 2, 3, 5, Lee writes y = 4x. What mistake did Lee make, and what is the correct equation?",
             fig=BT([B9], ("x", "y")), fig_a=BT([B9], ("x", "y"), a=True),
             steps=["Lee divided x by y:  $8 \\div 2 = 4$",
                    "y ÷ x:  $2 \\div 8 = \\frac{1}{4}$,  $5 \\div 20 = \\frac{1}{4}$",
                    "the equation:  $y = \\frac{1}{4}x$",
                    "check:  $\\frac{1}{4}(20) = 5$"],
             answer="Lee divided x by y; y = (1/4)x.",
             check=("many", ratios(*B9, "F(1,4)"), ("eq", "F(8,2)", "4"), off("4", 8, 2), ("eq", "F(1,4)*20", "5")),
             wrong="'y = 4x is right' — x ÷ y taken as the constant [B1G-M, AR.4.2: the ratio taken in the wrong order]"),
    ],

    # The six: the equation from a table (1), from a graph whose y-axis is scaled by 2 (2), from a description and
    # then solved (3); the pattern breaks at 4 — the same relationship the other way around; a table from an equation,
    # one entry found backward (5); a description from a table (6, the plan's laps).
    independent=[
        dict(stem="The table shows the cost c, in dollars, of w pounds of rice. Write the equation.",
             fig=TP([([2, 5, 9], ["3.60", "9.00", "16.20"])], ("pounds w", "cost c ($)"), cw=2.3),
             answer="c = 1.8w", why="c ÷ w is 1.8 for every pair: 3.60 ÷ 2 = 9.00 ÷ 5 = 16.20 ÷ 9 = 1.8.",
             check=ratios([2, 5, 9], ["3.60", "9.00", "16.20"], R("1.8")), space=0.4),
        # repeat_ok: rule D matches only the grid's axis numbers and the answer's digits; y = (4/3)x appears nowhere above.
        dict(repeat_ok=True, stem="Write the equation of the line.",
             fig=figs.plane((0, 6), (0, 8), lines=[figs.prop(Fr(4, 3), "")], ys=2, points=[(3, 4, "")], inches=3.2),
             answer="y = (4/3)x", why="Read the scales first: the y-axis counts by 2. The line passes through the origin and (3, 4): 4 ÷ 3 = 4/3.",
             check=("many", on("F(4,3)", [0, 3, 6], [0, 4, 8]), ("eq", "F(4,3)*3", "4")), space=0.4),
        dict(stem="A bakery uses 2.5 cups of milk per batch of muffins. Write the equation for the cups of milk m in b batches. How many batches use 20 cups of milk?",
             answer="m = 2.5b; 8 batches", why="2.5 cups per batch: m = 2.5b. 20 = 2.5b, so b = 8.",
             check=("many", solves(R("2.5") + "*u", "20", "8")), space=0.6),
        # repeat_ok: rule 43 matches only the 1 and 3 of "3 feet in 1 yard"; the relationship appears nowhere above.
        dict(repeat_ok=True, stem="There are 3 feet in 1 yard, so $f = 3n$ gives the feet f in n yards. Write the equation for the yards n in f feet.",
             answer="n = (1/3)f", why="1/3 yard per foot: n = (1/3)f. Check: 6 feet is (1/3)(6) = 2 yards, and 3(2) = 6.",
             check=("many", ("eq", "F(1,3)*6", "2"), ("eq", "3*2", "6")), space=0.4),
        dict(stem="Complete the table for $y = 4.2x$.",
             fig=TP([([5, 10, BLANK], [BLANK, BLANK, 63])], ("x", "y")),
             fig_key=TP([([5, 10, 15], [21, 42, 63])], ("x", "y")),
             answer="y = 21 and 42; x = 15", why="4.2(5) = 21 and 4.2(10) = 42; working backward, 63 = 4.2x, so x = 15.",
             check=("many", on(R("4.2"), [5, 10], [21, 42]), solves(R("4.2") + "*u", "63", "15")), space=0.4),
        dict(stem="The table shows the minutes m a runner takes to run n laps. Write the equation, and explain in a sentence what its constant means.",
             fig=TP([([2, 5, 8], [9, "22.5", 36])], ("laps n", "minutes m")),
             answer="m = 4.5n. Each lap takes 4.5 minutes.", why="m ÷ n is 4.5 for every pair: 9 ÷ 2 = 22.5 ÷ 5 = 36 ÷ 8 = 4.5.",
             check=ratios([2, 5, 8], [9, "22.5", 36], R("4.5")), space=0.5),
    ],

    # Bank: the equation from two tables (1–2), two graphs (3–4, the second scaled by 10) and a description (5); one
    # relationship the other way around (6); a table from an equation (7); write and solve (8); an equation said as a
    # sentence (9); the diagnostics on a table and a graph (10–11); a select-all of the equations for one story (12).
    # The additional bank mirrors it position by position with new numbers.
    bank=[
        dict(heading="Write the equation."),
        dict(stem="", fig=TP([([3, 5, 8], [21, 35, 56])], ("x", "y")),
             answer="y = 7x", why="y ÷ x is 7 for every pair: 21 ÷ 3 = 35 ÷ 5 = 56 ÷ 8 = 7.",
             check=ratios([3, 5, 8], [21, 35, 56], "7"), space=0.4),
        dict(stem="The table shows the gallons g of water in a tank after t minutes.",
             fig=TP([([2, 5, 6], [7, "17.5", 21])], ("minutes t", "gallons g")),
             answer="g = 3.5t", why="g ÷ t is 3.5 for every pair: 7 ÷ 2 = 17.5 ÷ 5 = 21 ÷ 6 = 3.5.",
             check=ratios([2, 5, 6], [7, "17.5", 21], R("3.5")), space=0.4),
        dict(stem="",
             fig=figs.plane((0, 6), (0, 4), lines=[figs.prop(Fr(2, 3), "")], points=[(3, 2, "on")], inches=2.6),
             answer="y = (2/3)x", why="The line passes through the origin and (3, 2): 2 ÷ 3 = 2/3.",
             # repeat_ok: unit_repeats pairs this with 7.02's bank question 6 on their axis numbers and the digits 2
             # and 3 — that line falls (−2/3) and asks for the constant; this one rises and asks for the equation
             check=("many", on("F(2,3)", [0, 3, 6], [0, 2, 4])), space=0.4, repeat_ok=True),
        dict(stem="The graph shows the miles m a cyclist rides in h hours.",
             fig=figs.plane((0, 4), (0, 60), lines=[figs.prop(15, "")], ys=10, xname="hours", yname="miles",
                            points=[(2, 30, ""), (4, 60, "")], inches=2.6),
             answer="m = 15h", why="Read the scales first: the miles axis counts by 10. The line passes through (2, 30): 30 ÷ 2 = 15.",
             check=on("15", [0, 2, 4], [0, 30, 60]), space=0.4),
        dict(stem="A hose sprays 6 gallons of water each minute. Write the equation for the gallons g in t minutes.",
             answer="g = 6t", why="6 gallons per minute, nothing added at the start.",
             check=("eq", "6*1", "6"), space=0.3),
        dict(heading="Write the equation the other way around."),
        dict(stem="There are 4 quarts in 1 gallon, so $q = 4g$ gives the quarts q in g gallons. Write the equation for the gallons g in q quarts.",
             answer="g = (1/4)q", why="1/4 gallon per quart. Check: (1/4)(8) = 2 and 4(2) = 8.",
             check=("many", ("eq", "F(1,4)*8", "2"), ("eq", "4*2", "8")), space=0.4),
        dict(heading="Complete the table."),
        dict(stem="$y = 1.5x$", fig=TP([([4, 8, BLANK], [BLANK, BLANK, 18])], ("x", "y")),
             answer="y = 6 and 12; x = 12", why="1.5(4) = 6 and 1.5(8) = 12; working backward, 18 = 1.5x, so x = 12.",
             check=("many", on(R("1.5"), [4, 8], [6, 12]), solves(R("1.5") + "*u", "18", "12")), space=0.4),
        dict(heading="Write the equation, then solve."),
        dict(stem="Rope costs \\$0.75 per foot. Write the equation for the cost c, in dollars, of f feet. How many feet does \\$9.00 buy?",
             answer="c = 0.75f; 12 feet", why="c = 0.75f. 9.00 = 0.75f, so f = 12.",
             check=solves(R("0.75") + "*u", R("9.00"), "12"), space=0.5),
        dict(heading="Explain in a sentence."),
        dict(stem="The equation $b = 24c$ gives the bottles b in c cases. What does the 24 tell you?",
             answer="Each case holds 24 bottles.", why="24 bottles per case: 24(1) = 24.",
             check=("eq", "24*1", "24"), space=0.3),
        dict(heading="Choose one."),
        dict(stem="Which equation fits the table?", fig=TP([([4, 6, 10], [6, 9, 15])], ("x", "y")),
             choices=["$y = x + 2$", "$y = 6x$", "$y = \\frac{2}{3}x$", "$y = 1.5x$"], correct=3, answer="D",
             why="y ÷ x is 1.5 for every pair: 6 ÷ 4 = 9 ÷ 6 = 15 ÷ 10 = 1.5.",
             check=("many", ratios([4, 6, 10], [6, 9, 15], R("1.5")), off("F(2,3)", 4, 6), offb("1", "2", 6, 9), off("6", 4, 6)),
             errors={"A": "the first pair's difference taken as the rule [B1G-M, AR.4.1: a constant difference taken for a constant ratio]", "B": "the first y taken as the constant [Notes I: y ÷ x, not y]", "C": "x ÷ y [B1G-M, AR.4.2: the ratio taken in the wrong order]"}),
        dict(stem="Which equation is graphed?",
             fig=figs.plane((0, 4), (0, 10), lines=[figs.prop(Fr(5, 2), "")], points=[(2, 5, "on")], inches=2.2),
             choices=["$y = 2.5x$", "$y = 0.4x$", "$y = 5x$", "$y = x + 3$"], correct=0, answer="A",
             why="The line passes through the origin and (2, 5): 5 ÷ 2 = 2.5.",
             check=("many", on(R("2.5"), [0, 2], [0, 5]), off("5", 2, 5), off(R("0.4"), 2, 5), offb("1", "3", 0, 0)),
             errors={"B": "x ÷ y [B1G-M, AR.4.2: the ratio taken in the wrong order]", "C": "the y-coordinate taken as the constant [B1G-M, AR.4.2: a coordinate read off as the constant]", "D": "the difference 5 − 2 added: through (2, 5) but not the origin [Notes II: nothing added at the start]"}),
        dict(heading="Select all that apply."),
        dict(stem="Sam types 40 words each minute. Select all the equations that are true for w words in m minutes.",
             choices=["$w = 40$", "$m = 40w$", "$w = 40m$", "$m = \\frac{1}{40}w$", "$w = m + 40$"], correct=[2, 3],
             answer="C, D", why="40 words per minute: w = 40m; the other way around, m = (1/40)w. Check: 2 minutes, 80 words.",
             check=("many", ("eq", "40*2", "80"), ("eq", "F(1,40)*80", "2"), ("true", "40*80 != 2"),
                    ("true", "2 + 40 != 80"), ("true", "40 != 80")),
             errors={"A": "the constant written as the equation, with no m [Notes I: y = px names both quantities]", "B": "x and y reversed [B1G-M, AR.4.2: the ratio taken in the wrong order]", "E": "the rate added [Notes II: nothing added at the start]"}),
    ],

    additional=[
        dict(heading="Write the equation."),
        dict(stem="", fig=TP([([4, 6, 9], [36, 54, 81])], ("x", "y")),
             answer="y = 9x", why="y ÷ x is 9 for every pair: 36 ÷ 4 = 54 ÷ 6 = 81 ÷ 9 = 9.",
             check=ratios([4, 6, 9], [36, 54, 81], "9"), space=0.4),
        dict(stem="The table shows the feet f a crane lifts a load in t minutes.",
             fig=TP([([2, 4, 7], ["4.4", "8.8", "15.4"])], ("minutes t", "feet f")),
             answer="f = 2.2t", why="f ÷ t is 2.2 for every pair: 4.4 ÷ 2 = 8.8 ÷ 4 = 15.4 ÷ 7 = 2.2.",
             check=ratios([2, 4, 7], ["4.4", "8.8", "15.4"], R("2.2")), space=0.4),
        dict(stem="",
             fig=figs.plane((0, 8), (0, 4), lines=[figs.prop(Fr(1, 4), "")], points=[(4, 1, "on")], inches=2.6),
             answer="y = (1/4)x", why="The line passes through the origin and (4, 1): 1 ÷ 4 = 1/4.",
             check=("many", on("F(1,4)", [0, 4, 8], [0, 1, 2])), space=0.4),
        dict(stem="The graph shows the dollars d a sitter earns in h hours.",
             fig=figs.plane((0, 4), (0, 50), lines=[figs.prop(Fr(25, 2), "")], ys=5, xname="hours", yname="dollars",
                            points=[(2, 25, ""), (4, 50, "")], inches=2.6),
             answer="d = 12.5h", why="Read the scales first: the dollars axis counts by 5. The line passes through (2, 25): 25 ÷ 2 = 12.5.",
             check=on(R("12.5"), [0, 2, 4], [0, 25, 50]), space=0.4),
        dict(stem="A machine stamps 14 cans each minute. Write the equation for the cans c in t minutes.",
             answer="c = 14t", why="14 cans per minute, nothing added at the start.",
             check=("eq", "14*1", "14"), space=0.3),
        dict(heading="Write the equation the other way around."),
        dict(stem="There are 100 centimeters in 1 meter, so $c = 100m$ gives the centimeters c in m meters. Write the equation for the meters m in c centimeters.",
             answer="m = (1/100)c, or m = 0.01c", why="1/100 meter per centimeter. Check: (1/100)(300) = 3 and 100(3) = 300.",
             check=("many", ("eq", "F(1,100)*300", "3"), ("eq", "100*3", "300"), ("eq", "F(1,100)", R("0.01"))), space=0.4),
        dict(heading="Complete the table."),
        dict(stem="$y = 6.5x$", fig=TP([([2, 6, BLANK], [BLANK, BLANK, 78])], ("x", "y")),
             answer="y = 13 and 39; x = 12", why="6.5(2) = 13 and 6.5(6) = 39; working backward, 78 = 6.5x, so x = 12.",
             check=("many", on(R("6.5"), [2, 6], [13, 39]), solves(R("6.5") + "*u", "78", "12")), space=0.4),
        dict(heading="Write the equation, then solve."),
        dict(stem="Wire costs \\$1.25 per meter. Write the equation for the cost c, in dollars, of m meters. How many meters does \\$10.00 buy?",
             answer="c = 1.25m; 8 meters", why="c = 1.25m. 10.00 = 1.25m, so m = 8.",
             check=solves(R("1.25") + "*u", R("10.00"), "8"), space=0.5),
        dict(heading="Explain in a sentence."),
        dict(stem="The equation $n = 8b$ gives the crayons n in b boxes. What does the 8 tell you?",
             answer="Each box holds 8 crayons.", why="8 crayons per box: 8(1) = 8.",
             check=("eq", "8*1", "8"), space=0.3),
        dict(heading="Choose one."),
        dict(stem="Which equation fits the table?", fig=TP([([2, 5, 8], [7, "17.5", 28])], ("x", "y")),
             choices=["$y = \\frac{2}{7}x$", "$y = 7x$", "$y = 3.5x$", "$y = x + 5$"], correct=2, answer="C",
             why="y ÷ x is 3.5 for every pair: 7 ÷ 2 = 17.5 ÷ 5 = 28 ÷ 8 = 3.5.",
             check=("many", ratios([2, 5, 8], [7, "17.5", 28], R("3.5")), off("7", 2, 7), off("F(2,7)", 2, 7), offb("1", "5", 5, "17.5")),
             errors={"A": "x ÷ y [B1G-M, AR.4.2: the ratio taken in the wrong order]", "B": "the first y taken as the constant [Notes I: y ÷ x, not y]", "D": "the first pair's difference taken as the rule [B1G-M, AR.4.1: a constant difference taken for a constant ratio]"}),
        dict(stem="Which equation is graphed?",
             fig=figs.plane((0, 4), (0, 6), lines=[figs.prop(Fr(3, 2), "")], points=[(2, 3, "on")], inches=2.2),
             choices=["$y = \\frac{2}{3}x$", "$y = 1.5x$", "$y = x + 1$", "$y = 3x$"], correct=1, answer="B",
             why="The line passes through the origin and (2, 3): 3 ÷ 2 = 1.5.",
             check=("many", on(R("1.5"), [0, 2], [0, 3]), off("F(2,3)", 2, 3), off("3", 2, 3), offb("1", "1", 0, 0)),
             errors={"A": "x ÷ y [B1G-M, AR.4.2: the ratio taken in the wrong order]", "C": "the difference 3 − 2 added: through (2, 3) but not the origin [Notes II: nothing added at the start]", "D": "the y-coordinate taken as the constant [B1G-M, AR.4.2: a coordinate read off as the constant]"}),
        dict(heading="Select all that apply."),
        dict(stem="A cyclist rides 12 miles each hour. Select all the equations that are true for m miles in h hours.",
             choices=["$m = 12h$", "$m = 12$", "$h = \\frac{1}{12}m$", "$m = h + 12$", "$h = 12m$"], correct=[0, 2],
             answer="A, C", why="12 miles per hour: m = 12h; the other way around, h = (1/12)m. Check: 3 hours, 36 miles.",
             check=("many", ("eq", "12*3", "36"), ("eq", "F(1,12)*36", "3"), ("true", "12*36 != 3"),
                    ("true", "3 + 12 != 36"), ("true", "12 != 36")),
             errors={"B": "the constant written as the equation, with no h [Notes I: y = px names both quantities]", "D": "the rate added [Notes II: nothing added at the start]", "E": "x and y reversed [B1G-M, AR.4.2: the ratio taken in the wrong order]"}),
    ],

    te=dict(
        must="Students write an equation from a table, a graph or a description, make a table from an equation and write a description from a graph. Either variable can be y.",
        must_not="Every relationship in this lesson passes through the origin. Lines that do not are not used.",
        read_first=[
            "Two book lessons, 7.5 and 7.6, taught as one day: writing y = px from a table, a graph and a description, then going from any one form to the others. Built from the benchmark and its clarifications first (the unit's Lesson Outlines, §7.05+06, standing decisions 2, 4, 6 and 10).",
            "Florida writes p; say once, at the vocabulary slide, that some books write k. Notes III is the benchmark's own example: m = 60h and h = (1/60)m are one relationship, two constants — the question tells which quantity is y, and the test asks it once (question 12b).",
            "Example 1 goes from a description to the other three forms; its graph's dollars axis counts by 20: say \"read the scales first\" before a point is plotted. Example 2 writes and then solves, and solves again the other way around to show the same answer."],
        materials="Whiteboards and markers. Hand out the Independent Set, one per student, after whiteboard question 9.",
        variation="Boards 1–2 write the equation from a table (whole numbers, then money with named letters); 3 votes on a graph's equation; 4 from a description; 5 votes on which quantity is y. The pattern breaks at 6 — a table FROM an equation, its last x found backward; 7 is the plane story with its passengers as the extra number; 8 says an equation in a sentence; 9 is Lee's x ÷ y, written. The set breaks at 4: the same relationship the other way around.",
        audit=["Every constant re-derived by sympy at build time as y ÷ x for every printed pair, over exact rationals; every table from an equation checked entry by entry, the backward entry solved; every graph drawn from y = px by u7/figs7.py, which refuses a marked point not on its line.",
               "Every wrong option of a choice item checked to fail at the item's own point or at the origin."],
        changes=["7.5 equations from tables, graphs and descriptions → Notes I–II, boards 1–4 and the set's questions 1–3.",
                 "7.6 translating between representations → Notes III, Examples 1–2, boards 5–8 and the set's questions 4–6."],
    ),
)
