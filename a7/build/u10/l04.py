# A7 10.04 Slope in Context (MA.8.AR.3.2, MA.8.AR.3.5) — Wed 20 Jan, a 43-minute day. Built from the unit's Lesson
# Outlines, §10.04. Every slope is the change in y over the change in x between two marked or given points; checks
# below re-derive each one from the printed data (rate / pairs), never from the keyed answer.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs10 as figs
S = figs.slide


def _n(v):
    """A printed value as an exact sympy number: 12.5 -> F(25,2)."""
    f = Fr(str(v))
    return "F(%d,%d)" % (f.numerator, f.denominator)


def slope(p, q):
    """The slope between two given points, as an expression: (y2 - y1)/(x2 - x1)."""
    return "(" + _n(q[1]) + " - " + _n(p[1]) + ")/(" + _n(q[0]) + " - " + _n(p[0]) + ")"


def rate(pts, m):
    """Every consecutive pair of the printed points gives the slope m: the relationship is linear with slope m."""
    return ("many",) + tuple(("eq", slope(pts[i], pts[i + 1]), m) for i in range(len(pts) - 1))


def start(pts, b):
    """The value at x = 0 found from the first point and the slope between the first two."""
    return ("eq", _n(pts[0][1]) + " - (" + slope(pts[0], pts[1]) + ")*" + _n(pts[0][0]), b)


def on(m, b, x, y):
    """(x, y) is on y = mx + b."""
    return ("eq", "(" + _n(m) + ")*" + _n(x) + " + " + _n(b), _n(y))


# ---- figures
def B(spec, reserve=0.75):
    return S(spec, inches=4.2, pt=18, reserve=reserve)


def _pt(p):
    """(x, y) -> a named dot that must be on the line; (x, y, where) -> the same, its name placed `where`;
    (x, y, name, where) as figs.plane takes it ("" a bare dot)."""
    return (p[0], p[1], "on") if len(p) == 2 else p if len(p) == 4 else (p[0], p[1], None, p[2])


def P(xr, yr, m, b, pts, **k):
    """A slide graph: the line y = mx + b, the marked points named."""
    return figs.plane(xr, yr, lines=[(m, b, "")], points=[_pt(p) for p in pts], inches=4.2, pt=18, **k)


def G(xr, yr, m, b, pts, inches=2.6, **k):
    """A paper graph at print size."""
    return figs.plane(xr, yr, lines=[(m, b, "")], points=[_pt(p) for p in pts], inches=inches, **k)


def T(xs, ys, head, cw=1.6):
    return figs.table([(xs, ys)], head=head, cw=cw)


CLIMB = [(1, 2300), (3, 2900), (6, 3800)]
NOTES1 = S(figs.table([([1, 3, 6], [2300, 2900, 3800])], head=("hours", "elevation (feet)"), cw=2.4, rh=1.25),
           inches=8.0, pt=22, reserve=0.3)
NOTES2 = S(figs.plane((0, 8), (0, 120), lines=[(-12, 100, "")], points=[(0, 100, None, "ur"), (5, 40, "on")], ys=20,
                      xname="hours", yname="charge (percent)", inches=4.6, pt=18), inches=4.6, pt=18, reserve=0.6)

BALLOON = dict(ys=150, xname="minutes", yname="height (feet)")
EX1 = B(P((0, 6), (0, 750), 75, 150, [(2, 300, "dr"), (4, 450, "dr")], **BALLOON), reserve=0.9)
EX1W = S(P((0, 6), (0, 750), 75, 150, [(2, 300, "dr"), (4, 450, "dr")], triangles=[figs.tri((2, 300), (4, 450), side="over")], **BALLOON),
         inches=4.2, pt=18, reserve=1.5)
SNOW = dict(ys=3, aspect=0.8, xname="hours", yname="depth (inches)")     # a little flat: the answer room under it holds its height
YT1 = B(P((0, 8), (0, 18), Fr(3, 2), 6, [(2, 9, "dr"), (6, 15, "dr")], **SNOW), reserve=1.05)
YT1A = B(P((0, 8), (0, 18), Fr(3, 2), 6, [(2, 9, "dr"), (6, 15, "dr")], triangles=[figs.tri((2, 9), (6, 15), side="over")], **SNOW), reserve=1.05)

PUPPY = [(2, 8), (4, 12.5), (6, 17)]
T1 = figs.table([([2, 4, 6], [8, 12.5, 17])], head=("weeks", "pounds"), cw=2.0, rh=1.3)
# Rows 1.2 times as tall as wide. The question slide's options stand beside the graph and hold its width, so there
# (8, 0) is a bare dot on the 8 (the slope is given; no name overhangs the right edge); the reveal, whose steps use
# it, names it above its dot.
_ELEV = dict(ys=40, aspect=1.2, xname="seconds", yname="height (feet)")
ELEV = P((0, 8), (0, 160), -15, 120, [(0, 120, "ur"), (8, 0, "", "u")], **_ELEV)
ELEVA = P((0, 8), (0, 160), -15, 120, [(0, 120, "ur"), (8, 0, "u+")], **_ELEV)
PAY = [(2, 31), (4, 57), (8, 109)]
T5 = T([2, 4, 8], [31, 57, 109], ("hours", "pay ($)"), cw=1.8)
PAGES = P((0, 10), (0, 360), -30, 300, [(0, 300, "ur"), (6, 120)], ys=60, xname="days", yname="pages left")

# ---- the Independent Set (print size)
IS1 = T([1, 3, 7], [52, 88, 160], ("hours", "loaves baked"))
IS3 = G((0, 6), (0, 490), 70, 70, [(1, 140), (4, 350)], inches=2.4, ys=70, xname="hours", yname="distance (miles)")
IS4 = G((0, 6), (0, 24), -4, 24, [(2, 16), (5, 4)], inches=2.4, ys=4, xname="hours", yname="ice (pounds)")
IS6 = T([2, 5, 8], ["9.00", "16.50", "24.00"], ("miles", "cost ($)"), cw=1.9)

L = dict(
    code="10.04", unit=10, lesson_no=4,
    title="Slope in Context",
    unit_title="Linear Relationships",
    benchmark="MA.8.AR.3.2",
    benchmark_text="Given a table, graph or written description of a linear relationship, determine the slope.",
    benchmarks=[("MA.8.AR.3.2", "Given a table, graph or written description of a linear relationship, determine the slope."),
                ("MA.8.AR.3.5", "Given a real-world context, determine and interpret the slope and y-intercept of a two-variable linear equation from a written description, a table, a graph or an equation in slope-intercept form.")],
    target="I can find the slope of a real-world linear relationship and explain what it means, with its units.",
    essential="Why does the slope of a real-world line carry a unit, and what does its sign tell you?",
    building_on="In lesson 10.02+03, students found the slope of a line from a graph, a table and two points. In lesson 10.01, they learned that a linear relationship has a constant rate of change. In Unit 7, they found the constant of proportionality as a unit rate.",
    working_toward="In lesson 10.05, the y-intercept is named and lines are graphed from y = mx + b. In lessons 10.07+08, students interpret both the slope and the y-intercept of a real-world equation.",
    vocab=[],
    vocab_slide=False,
    ixl=["Rate of change of a linear function: graphs — ZPF", "Rate of change of a linear function: tables — 8FE"],
    closure="Whiteboard question 9 is written work, and it is the exit evidence. A full answer says that Tom is not correct, finds the rate of change as (110 − 60) ÷ (10 − 5) = 10 gallons per minute, and explains that dividing one pair gives the rate only when the relationship is proportional, which this one is not, because the pool held 10 gallons at 0 minutes.",

    mtr=[("MTR.4.1", "On whiteboard questions 3 and 5, students convince a neighbor and then vote again."),
         ("MTR.5.1", "Students find the same slope as a rate of change in a table, a graph and a written description, and they explain it in a sentence with both units."),
         ("MTR.6.1", "Students check each slope by its sign: an amount that goes down has a negative slope.")],
    hoq=[("Why is 2,300 ÷ 1 not the climber's rate of change?", "DOK 2"),
         ("What does a negative slope tell you about the amount on the y-axis?", "DOK 1"),
         ("How can you tell from the units which number goes on top of the slope?", "DOK 2"),
         ("When does dividing one pair give the rate of change, and how can you tell from a table?", "DOK 3")],
    differentiation=[
        ("ESE / 504", "Students keep a printed card with the two lines \"change in y over change in x\" and \"y-unit per x-unit\", and they write the units beside every subtraction."),
        ("ELL", "Before the Notes, the teacher points to the words rate, per, gains and loses on the slide, and students write a sentence frame: \"The ___ gains (loses) ___ every ___.\""),
        ("Enrichment", "After whiteboard question 8, students find the fee in the ticket order (\\$7.00) and explain why it is the cost of an order of 0 tickets.")],

    warmup=[
        dict(stem="Find the slope of the line through $(-1, 8)$ and $(3, 0)$.", answer="−2",
             check=("eq", slope((-1, 8), (3, 0)), "-2")),
        dict(stem="Is $y = 4x + 6$ a proportional relationship? How do you know?",
             answer="No, because y is 6 when x is 0.",
             check=("many", ("eq", "4*0 + 6", "6"), ("true", "4*0 + 6 != 0"))),
        dict(stem="A car travels 150 miles on 6 gallons of gas. Find the constant of proportionality in miles per gallon.",
             answer="25", check=("eq", "F(150, 6)", "25")),
        dict(stem="Find $120 \\div 8$ and $-120 \\div 8$.", answer="15 and −15",
             check=("many", ("eq", "F(120, 8)", "15"), ("eq", "F(-120, 8)", "-15"))),
    ],

    notes=[
        dict(numeral="I", head="The slope is a rate of change: its unit is the y-unit per x-unit.", min=4,
             fig=NOTES1,
             text=["(2,900 − 2,300) ÷ (3 − 1) = 300   and   (3,800 − 2,900) ÷ (6 − 3) = 300",
                     "300 feet per hour: the climber gains 300 feet every hour.",
                     "From 3 hours to 5 hours: 2 · 300 = 600 more feet, so 3,500 feet at 5 hours.",
                     "The slope is not y ÷ x here: 2,300 ÷ 1 is not the rate, because the climb did not start at 0 feet.",
                     "IXL calls a linear relationship a linear function."],
             letters=False),
        dict(numeral="II", head="An amount that goes down has a negative slope", min=4,
             fig=NOTES2,
             text=["Read the scales first.   (40 − 100) ÷ (5 − 0) = −12",
                     "−12 percent per hour: the phone loses 12 percent of its charge every hour."],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=1,
             prompt=["The graph shows a hot-air balloon's height, in feet, versus time, in minutes."], fig=EX1,
             ask="Find the slope, with its unit, and explain what it means.",
             # figwords_ok: 75 is the slope the rows compute; the figure gives its run 2 and rise 150, and its other
             # numbers are the axis's tick numbers.
             worked=[dict(min=2, figwords_ok=True,
                          rows=[("\\frac{450 - 300}{4 - 2} = \\frac{150}{2}", "change in feet over change in minutes"),
                                ("= 75", "feet per minute")],
                          fig=EX1W, answer="The balloon rises 75 feet every minute.")],
             check=("many", ("eq", slope((2, 300), (4, 450)), "75"), on(75, 150, 2, 300), on(75, 150, 4, 450)),
             your_turn=dict(min=3,
                            prompt=["The graph shows the depth of snow, in inches, versus time, in hours."],
                            ask="Find the slope, with its unit, and explain what it means.",
                            fig=YT1, fig_a=YT1A,
                            steps=["Slope:   $(15 - 9) \\div (6 - 2) = 6 \\div 4 = 1.5$"],
                            answer="The snow gains 1.5 inches every hour."),
             yt_check=("many", ("eq", slope((2, 9), (6, 15)), "F(3,2)"), on(Fr(3, 2), 6, 2, 9), on(Fr(3, 2), 6, 6, 15))),
        dict(title="Example 2", min_q=1,
             prompt=["A hiker walks down a mountain at a constant rate. After 2 hours her elevation is 5,400 feet, and after 5 hours it is 3,300 feet."],
             ask="Find the slope, with its unit, and explain what it means.",
             worked=[dict(min=2,
                          rows=[("\\frac{3{,}300 - 5{,}400}{5 - 2} = \\frac{-2{,}100}{3}", "change in feet over change in hours"),
                                ("= -700", "feet per hour")],
                          answer="−700 feet per hour: she goes down 700 feet every hour.")],
             check=("eq", slope((2, 5400), (5, 3300)), "-700"),
             your_turn=dict(min=3,
                            prompt=["A printer works at a constant rate. After 4 minutes, 420 sheets are left in its tray, and after 10 minutes, 300 sheets are left."],
                            ask="Find the slope, with its unit, and explain what it means.",
                            steps=["Change in sheets:   $300 - 420 = -120$", "Change in time:   $10 - 4 = 6$",
                                   "Slope:   $-120 \\div 6 = -20$"],
                            answer="−20 sheets per minute: the tray loses 20 sheets every minute."),
             yt_check=("eq", slope((4, 420), (10, 300)), "-20")),
    ],

    # The round: a slope from a table (1) and what it means (2, the same table: one thing changes, the question); a
    # vote on a slope's meaning (3); a description with two moments (4); a vote on a slope from a table with unequal
    # steps (5); a falling graph with a scale (6); the truck, its 18 boxes the extra number (7); a missing number (8);
    # Tom's y ÷ x, written (9).
    whiteboard=[
        dict(text=["The table shows a puppy's weight.", "**Find the slope, with its unit."],
             qtext="The table shows a puppy's weight: weeks 2, 4, 6; weight in pounds 8, 12.5, 17. Find the slope, with its unit.",
             fig=S(T1, inches=6.4, pt=22, reserve=0.75), fig_a=S(T1, inches=5.4, pt=18, reserve=0.95),
             steps=["Slope:   $(12.5 - 8) \\div (4 - 2) = 4.5 \\div 2 = 2.25$", "Check:   $(17 - 12.5) \\div (6 - 4) = 2.25$"],
             answer="2.25 pounds per week",
             check=rate(PUPPY, "F(9,4)"),
             wrong="0.44 weeks per pound — the change in weeks over the change in pounds [B1G-M, AR.3.2: inverting the x- and y-values]; 4 pounds per week — 8 ÷ 2, one pair divided [B1G-M, AR.3.2: slope is not the constant of proportionality]"),
        # repeat_ok: the plan's own design — the same table as board 1, and only the question changes (meaning, not number).
        dict(repeat_ok=True, text=["The table shows a puppy's weight.", "**What does the slope mean?"],
             qtext="The table shows a puppy's weight: weeks 2, 4, 6; weight in pounds 8, 12.5, 17. What does the slope mean?",
             fig=S(T1, inches=6.4, pt=22, reserve=0.75), fig_a=S(T1, inches=5.4, pt=18, reserve=0.95),
             steps=["Slope:   $4.5 \\div 2 = 2.25$ pounds per week", "Positive:   the weight goes up"],
             answer="The puppy gains 2.25 pounds every week.",
             check=("many", rate(PUPPY, "F(9,4)"), ("true", "(" + slope(PUPPY[0], PUPPY[1]) + ") > 0")),
             wrong="'the puppy weighed 2.25 pounds' — the slope read as a weight [B1G-M, AR.3.5: misinterpreting the slope in context]; 'the puppy takes 2.25 weeks to gain 1 pound' — the rate turned over [B1G-M, AR.3.2: inverting the x- and y-values]"),
        dict(kind="mc", text=["The graph shows an elevator's height. The slope is −15.", "**What does the slope mean?"],
             qtext="The graph shows an elevator's height, in feet, versus time, in seconds, a line from (0, 120) to (8, 0). The slope of the line is −15. What does the slope mean?",
             fig=B(ELEV), fig_a=B(ELEVA, reserve=1.15),
             steps=["Slope:   $\\frac{0 - 120}{8 - 0} = -15$ feet per second", "Negative:   the height goes down"],
             choices=["The elevator goes up 15 feet every second.", "The elevator goes down 15 feet every second.", "The elevator takes 15 seconds to go down 1 foot.", "The elevator starts 15 feet above the ground."],
             correct=1, answer="B — Down 15 feet every second.",
             errors={"A": "the sign ignored: a negative slope read as rising [B1G-M, AR.3.5: misinterpreting the slope in context]", "C": "the rate turned over: seconds per foot [B1G-M, AR.3.2: inverting the x- and y-values]", "D": "the slope read as a start [B1G-M, AR.3.5: misidentifying slope and y-intercept]"},
             check=("many", ("eq", slope((0, 120), (8, 0)), "-15"), ("true", "(" + slope((0, 120), (8, 0)) + ") < 0"),
                    ("true", "120 != 15"), ("true", "(" + slope((120, 0), (0, 8)) + ") != -15"))),
        dict(text=["A stack of 4 cups is 15 centimeters tall, and", "a stack of 10 cups is 33 centimeters tall.",
                   "**Find the rate of change, with its unit."],
             steps=["Change in height:   $33 - 15 = 18$", "Change in cups:   $10 - 4 = 6$", "Rate:   $18 \\div 6 = 3$"],
             answer="3 centimeters per cup",
             check=("eq", slope((4, 15), (10, 33)), "3"),
             wrong="3.75 centimeters per cup — 15 ÷ 4, one pair divided [B1G-M, AR.3.2: slope is not the constant of proportionality]; 1/3 cup per centimeter — the rate turned over [B1G-M, AR.3.2: inverting the x- and y-values]"),
        dict(kind="mc", text=["The table shows a worker's pay.", "**What is the slope?"],
             qtext="The table shows a worker's pay: hours 2, 4, 8; pay in dollars 31, 57, 109. What is the slope?",
             fig=S(T5, inches=5.4, pt=18, reserve=0.75), fig_a=S(T5, inches=5.4, pt=18, reserve=0.95),
             steps=["Change in pay:   $57 - 31 = 26$", "Change in hours:   $4 - 2 = 2$", "Slope:   $26 \\div 2 = 13$",
                    "Check:   $(109 - 57) \\div (8 - 4) = 52 \\div 4 = 13$"],
             choices=["26 dollars per hour", "15.5 dollars per hour", "13 dollars per hour", "$\\frac{1}{13}$ hour per dollar"],
             correct=2, answer="C — 13 dollars per hour",
             errors={"A": "the change in pay alone, not divided by the change in hours [B1G-M, AR.3.2: slope is the change in y over the change in x]", "B": "31 ÷ 2: one pair divided, as if proportional [B1G-M, AR.3.2: slope is not the constant of proportionality]", "D": "the change in hours over the change in pay: turned over [B1G-M, AR.3.2: inverting the x- and y-values]"},
             check=("many", rate(PAY, "13"), ("true", "57 - 31 != 13"), ("true", "F(31, 2) != 13"),
                    ("true", "(" + slope((31, 2), (57, 4)) + ") != 13"), ("eq", slope((31, 2), (57, 4)), "F(1,13)"))),
        dict(text=["The graph shows the pages left to read in a book.", "**Find the slope, with its unit."],
             qtext="The graph shows the pages left to read in a book versus time, in days; a line through (0, 300) and (6, 120). Find the slope, with its unit.",
             fig=B(PAGES), fig_a=B(PAGES, reserve=0.95),
             steps=["Change in pages:   $120 - 300 = -180$", "Change in days:   $6 - 0 = 6$", "Slope:   $-180 \\div 6 = -30$"],
             answer="−30 pages per day",
             check=("many", ("eq", slope((0, 300), (6, 120)), "-30"), on(-30, 300, 6, 120)),
             wrong="30 pages per day — the sign dropped for a line that falls [B1G-M, AR.3.5: misinterpreting the slope in context]; −180 pages per day — the change in pages alone [B1G-M, AR.3.2: slope is the change in y over the change in x]"),
        dict(text=["A truck carrying 18 boxes is 250 miles from home after",
                   "2 hours and 130 miles from home after 4 hours.",
                   "**Find the slope, in miles per hour."],
             unneeded="18",
             steps=["Change in miles:   $130 - 250 = -120$", "Change in hours:   $4 - 2 = 2$", "Slope:   $-120 \\div 2 = -60$"],
             answer="−60 miles per hour",
             check=("eq", slope((2, 250), (4, 130)), "-60"),
             wrong="60 — the sign dropped: the truck is getting closer to home [B1G-M, AR.3.5: misinterpreting the slope in context]; −6.67 — the 18 boxes used: −120 ÷ 18 [an extra number, included on purpose]"),
        dict(text=["An order of tickets has one fee,", "and every ticket costs the same amount.",
                   "The slope is 4 dollars per ticket, and 3 tickets cost \\$19.",
                   "**How much do 7 tickets cost?"],
             steps=["More tickets:   $7 - 3 = 4$", "More cost:   $4 \\cdot 4 = 16$", "Cost:   $19 + 16 = 35$"],
             answer="7 tickets cost \\$35.",
             check=("many", ("eq", "19 + 4*(7 - 3)", "35"), ("eq", "(35 - 19)/(7 - 3)", "4")),
             wrong="\\$28 — 4 · 7, the fee left out [B1G-M, AR.3.1: believing all linear relationships are proportional]; \\$44.33 — 19 ÷ 3 · 7, one pair scaled as if proportional [B1G-M, AR.3.2: slope is not the constant of proportionality]"),
        dict(kind="written",
             text=["A pool holds 60 gallons after 5 minutes, 110 gallons",
                   "after 10 minutes and 160 gallons after 15 minutes.",
                   "Tom says the rate of change is 12 gallons per minute,",
                   "because 60 ÷ 5 = 12.", "**Is Tom correct? Explain."],
             qtext="A pool holds 60 gallons after 5 minutes, 110 gallons after 10 minutes and 160 gallons after 15 minutes. Tom says the rate of change is 12 gallons per minute, because 60 ÷ 5 = 12. Is Tom correct? Explain.",
             steps=["Rate:   $(110 - 60) \\div (10 - 5) = 10$;   at 0 minutes,   $60 - 10 \\cdot 5 = 10$"],
             answer="No. The rate is 10 gallons per minute, and the pool held 10 gallons at 0 minutes.",
             check=("many", rate([(5, 60), (10, 110), (15, 160)], "10"), start([(5, 60), (10, 110)], "10"),
                    ("true", "F(60, 5) != 10")),
             wrong="'yes, 60 ÷ 5 = 12' — one pair divided, as if proportional [B1G-M, AR.3.1: believing all linear relationships are proportional]"),
    ],

    # The six: a slope from a table in context (1); a slope's meaning in a sentence (2); a rising graph with a scale (3);
    # a falling graph and its meaning (4); a description with two moments (5); the break — a table that is not
    # proportional, where y ÷ x does not give the rate (6).
    independent=[
        dict(stem="The table shows the loaves a bakery has baked. Find the slope, with its unit.", fig=IS1,
             answer="18 loaves per hour", why="(88 − 52) ÷ (3 − 1) = 36 ÷ 2 = 18, and (160 − 88) ÷ (7 − 3) = 72 ÷ 4 = 18.",
             check=rate([(1, 52), (3, 88), (7, 160)], "18"), space=0.6),
        dict(stem="A graph of a cyclist's distance, in miles, versus time, in hours, has a slope of 14. What does the slope mean?",
             answer="The cyclist rides 14 miles every hour.", why="The slope is a rate of change: 14 miles per hour.",
             ack="a sentence that reads a given slope with its units", space=0.6),
        dict(stem="The graph shows a train's distance from the station. Find the slope, with its unit.", fig=IS3,
             answer="70 miles per hour", why="(350 − 140) ÷ (4 − 1) = 210 ÷ 3 = 70.",
             check=("many", ("eq", slope((1, 140), (4, 350)), "70"), on(70, 70, 1, 140), on(70, 70, 4, 350)), space=0.6),
        dict(stem="The graph shows the ice left in a cooler. Find the slope, with its unit, and explain what it means.", fig=IS4,
             answer="−4 pounds per hour: the cooler loses 4 pounds of ice every hour.",
             why="(4 − 16) ÷ (5 − 2) = −12 ÷ 3 = −4. The slope is negative, so the ice goes down.",
             check=("many", ("eq", slope((2, 16), (5, 4)), "-4"), on(-4, 24, 2, 16), on(-4, 24, 5, 4)), space=0.6),
        dict(stem="A gift card's balance goes down at a constant rate. It is \\$86.00 after 2 weeks and \\$58.00 after 6 weeks. Find the slope, with its unit.",
             answer="−7 dollars per week", why="(58 − 86) ÷ (6 − 2) = −28 ÷ 4 = −7.",
             check=("eq", slope((2, 86), (6, 58)), "-7"), space=0.6),
        dict(stem="The table shows the cost of a taxi ride. Find the rate of change, with its unit. Explain why $9.00 \\div 2$ does not give it.",
             fig=IS6,
             answer="2.50 dollars per mile. The ride costs \\$4.00 at 0 miles, so the relationship is not proportional.",
             why="(16.50 − 9.00) ÷ (5 − 2) = 7.50 ÷ 3 = 2.50. 9.00 ÷ 2 = 4.50 is not the rate, because 9.00 − 2(2.50) = 4.00: the ride costs \\$4.00 for 0 miles.",
             check=("many", rate([(2, 9), (5, 16.5), (8, 24)], "F(5,2)"), start([(2, 9), (5, 16.5)], "4"),
                    ("true", "F(9, 2) != F(5, 2)")), space=0.7),
    ],

    # Bank: two tables (1–2, the second falling with unequal steps), two graphs with a scale (3–4), two descriptions
    # (5–6), a slope's meaning in a sentence (7), two diagnostics (8–9), a missing number (10), the y ÷ x claim (11),
    # backwards (12). The additional bank mirrors it position by position with new numbers.
    bank=[
        dict(heading="Find the slope, with its unit."),
        dict(stem="The table shows the total paid for a gym membership.",
             fig=T([2, 3, 6], [64, 92, 176], ("months", "total paid ($)")),
             answer="28 dollars per month", why="(92 − 64) ÷ (3 − 2) = 28, and (176 − 92) ÷ (6 − 3) = 84 ÷ 3 = 28.",
             check=rate([(2, 64), (3, 92), (6, 176)], "28"), space=0.5),
        dict(stem="The table shows the fuel left in a ferry.",
             fig=T([1, 3, 4], [450, 360, 315], ("hours", "fuel left (gallons)")),
             answer="−45 gallons per hour", why="(360 − 450) ÷ (3 − 1) = −90 ÷ 2 = −45, and (315 − 360) ÷ (4 − 3) = −45.",
             check=rate([(1, 450), (3, 360), (4, 315)], "-45"), space=0.5),
        dict(stem="The graph shows a ship's distance from the dock.",
             fig=G((0, 7), (0, 240), 30, 30, [(2, 90), (6, 210)], ys=30, xname="hours", yname="distance (km)"),
             answer="30 kilometers per hour", why="(210 − 90) ÷ (6 − 2) = 120 ÷ 4 = 30.",
             check=("many", ("eq", slope((2, 90), (6, 210)), "30"), on(30, 30, 2, 90), on(30, 30, 6, 210)), space=0.5),
        dict(stem="The graph shows a drone's height as it comes down.",
             fig=G((0, 8), (0, 90), -10, 80, [(0, 80, "ur"), (5, 30)], ys=10, xname="seconds", yname="height (meters)"),
             answer="−10 meters per second", why="(30 − 80) ÷ (5 − 0) = −50 ÷ 5 = −10.",
             check=("many", ("eq", slope((0, 80), (5, 30)), "-10"), on(-10, 80, 5, 30)), space=0.5),
        dict(stem="A car's odometer reads 1,250 miles after 2 hours and 1,445 miles after 5 hours of driving at a constant speed.",
             answer="65 miles per hour", why="(1,445 − 1,250) ÷ (5 − 2) = 195 ÷ 3 = 65.",
             check=("eq", slope((2, 1250), (5, 1445)), "65"), space=0.5),
        dict(stem="An airplane comes down at a constant rate. It is at 9,000 feet after 3 minutes and at 6,500 feet after 8 minutes.",
             answer="−500 feet per minute", why="(6,500 − 9,000) ÷ (8 − 3) = −2,500 ÷ 5 = −500.",
             check=("eq", slope((3, 9000), (8, 6500)), "-500"), space=0.5),
        dict(heading="Explain what the slope means."),
        dict(stem="A graph shows the dog food in a bag, in pounds, versus time, in days. The slope is −0.5.",
             answer="The bag loses 0.5 pounds of dog food every day.", why="A negative slope: the food goes down 0.5 pounds for every 1 day.",
             ack="a sentence that reads a given slope with its units", space=0.5),
        dict(heading="Choose one."),
        dict(stem="A graph shows the money on a lunch account, in dollars, versus time, in school days. The slope is −3.50. What does the slope mean?",
             choices=["The account goes down \\$3.50 every school day.", "The account goes up \\$3.50 every school day.", "The account started with \\$3.50.", "The account takes 3.50 school days to go down \\$1."],
             correct=0, answer="A", why="The slope is −3.50 dollars per school day: negative, so the money goes down 3.50 dollars every day.",
             check=("many", ("true", "-F(7,2) < 0"), ("true", "F(1, -F(7,2)) != -F(7,2)")),
             errors={"B": "the sign ignored [B1G-M, AR.3.5: misinterpreting the slope in context]", "C": "the slope read as a start [B1G-M, AR.3.5: misidentifying slope and y-intercept]", "D": "the rate turned over [B1G-M, AR.3.2: inverting the x- and y-values]"}),
        dict(stem="The table shows the cost of tickets. What is the slope?",
             fig=T([2, 5, 6], [19, 40, 47], ("tickets", "cost ($)")),
             choices=["$\\frac{1}{7}$ ticket per dollar", "21 dollars per ticket", "9.50 dollars per ticket", "7 dollars per ticket"],
             correct=3, answer="D", why="(40 − 19) ÷ (5 − 2) = 21 ÷ 3 = 7, and (47 − 40) ÷ (6 − 5) = 7.",
             check=("many", rate([(2, 19), (5, 40), (6, 47)], "7"), ("true", "40 - 19 != 7"), ("true", "F(19, 2) != 7"),
                    ("eq", slope((19, 2), (40, 5)), "F(1,7)")),
             errors={"A": "the change in tickets over the change in cost: turned over [B1G-M, AR.3.2: inverting the x- and y-values]", "B": "the change in cost alone [B1G-M, AR.3.2: slope is the change in y over the change in x]", "C": "19 ÷ 2: one pair divided, as if proportional [B1G-M, AR.3.2: slope is not the constant of proportionality]"}),
        dict(heading="Solve the problem."),
        dict(stem="A plumber charges one fee for a visit and the same amount for every hour. The slope is 65 dollars per hour, and a 2-hour job costs \\$185. How much does a 5-hour job cost?",
             answer="\\$380", why="3 more hours cost 3 · 65 = 195, and 185 + 195 = 380.",
             check=("eq", "185 + 65*(5 - 2)", "380"), space=0.5),
        dict(stem="A bike rental costs \\$22 for 2 hours, \\$34 for 4 hours and \\$46 for 6 hours. Ana says the rate of change is 11 dollars per hour, because 22 ÷ 2 = 11. Is Ana correct? Explain.",
             answer="No. The rate of change is 6 dollars per hour. The rental costs \\$10 at 0 hours, so dividing one pair does not give the rate.",
             why="(34 − 22) ÷ (4 − 2) = 6, and 22 − 2(6) = 10: not proportional.",
             check=("many", rate([(2, 22), (4, 34), (6, 46)], "6"), start([(2, 22), (4, 34)], "10"), ("true", "F(22, 2) != 6")),
             space=0.7),
        dict(stem="A crew paints a fence at a constant rate of 18 feet per hour. They have painted 36 feet after 2 hours. After how many hours will they have painted 108 feet?",
             answer="After 6 hours", why="(108 − 36) ÷ 18 = 72 ÷ 18 = 4 more hours, so 2 + 4 = 6; 108 ÷ 18 = 6 agrees.",
             check=("many", ("eq", "2 + F(108 - 36, 18)", "6"), ("eq", slope((2, 36), (6, 108)), "18"),
                    ("eq", "F(108, 18)", "6"), ("eq", "F(36, 2)", "18")), space=0.5),
    ],

    additional=[
        dict(heading="Find the slope, with its unit."),
        dict(stem="The table shows what a photographer has earned.",
             fig=T([1, 3, 4], [95, 205, 260], ("hours", "earned ($)")),
             answer="55 dollars per hour", why="(205 − 95) ÷ (3 − 1) = 110 ÷ 2 = 55, and (260 − 205) ÷ (4 − 3) = 55.",
             check=rate([(1, 95), (3, 205), (4, 260)], "55"), space=0.5),
        dict(stem="The table shows the miles of road a snowplow has left to clear.",
             fig=T([2, 3, 6], [90, 74, 26], ("hours", "miles left")),
             answer="−16 miles per hour", why="(74 − 90) ÷ (3 − 2) = −16, and (26 − 74) ÷ (6 − 3) = −48 ÷ 3 = −16.",
             check=rate([(2, 90), (3, 74), (6, 26)], "-16"), space=0.5),
        dict(stem="The graph shows a sunflower's height.",
             fig=G((0, 7), (0, 180), Fr(45, 2), 15, [(2, 60), (6, 150)], ys=15, xname="weeks", yname="height (cm)"),
             answer="22.5 centimeters per week", why="(150 − 60) ÷ (6 − 2) = 90 ÷ 4 = 22.5.",
             check=("many", ("eq", slope((2, 60), (6, 150)), "F(45,2)"), on(Fr(45, 2), 15, 2, 60), on(Fr(45, 2), 15, 6, 150)), space=0.5),
        dict(stem="The graph shows the sand left in the top of an hourglass.",
             fig=G((0, 4), (0, 250), -50, 200, [(1, 150), (3, 50)], inches=1.8, ys=50, xname="minutes", yname="sand left (grams)"),
             answer="−50 grams per minute", why="(50 − 150) ÷ (3 − 1) = −100 ÷ 2 = −50.",
             check=("many", ("eq", slope((1, 150), (3, 50)), "-50"), on(-50, 200, 1, 150), on(-50, 200, 3, 50)), space=0.5),
        dict(stem="A train travels at a constant speed. It has gone 135 miles after 3 hours and 351 miles after 7 hours.",
             answer="54 miles per hour", why="(351 − 135) ÷ (7 − 3) = 216 ÷ 4 = 54.",
             check=("eq", slope((3, 135), (7, 351)), "54"), space=0.5),
        dict(stem="A store sells a game at a constant rate. It has 180 copies left after 2 days and 124 copies left after 6 days.",
             answer="−14 copies per day", why="(124 − 180) ÷ (6 − 2) = −56 ÷ 4 = −14.",
             check=("eq", slope((2, 180), (6, 124)), "-14"), space=0.5),
        dict(heading="Explain what the slope means."),
        dict(stem="A graph shows the seed in a bird feeder, in ounces, versus time, in hours. The slope is −0.75.",
             answer="The feeder loses 0.75 ounces of seed every hour.", why="A negative slope: the seed goes down 0.75 ounces for every 1 hour.",
             ack="a sentence that reads a given slope with its units", space=0.5),
        dict(heading="Choose one."),
        dict(stem="A graph shows the money on a bus pass, in dollars, versus the number of rides. The slope is −1.25. What does the slope mean?",
             choices=["The pass takes 1.25 rides to go down \\$1.", "The pass started with \\$1.25.", "The pass goes down \\$1.25 every ride.", "The pass goes up \\$1.25 every ride."],
             correct=2, answer="C", why="The slope is −1.25 dollars per ride: negative, so the money goes down 1.25 dollars every ride.",
             check=("many", ("true", "-F(5,4) < 0"), ("true", "F(1, -F(5,4)) != -F(5,4)")),
             errors={"A": "the rate turned over [B1G-M, AR.3.2: inverting the x- and y-values]", "B": "the slope read as a start [B1G-M, AR.3.5: misidentifying slope and y-intercept]", "D": "the sign ignored [B1G-M, AR.3.5: misinterpreting the slope in context]"}),
        dict(stem="The table shows the cost of rice. What is the slope?",
             fig=T([2, 6, 7], [17, 41, 47], ("pounds", "cost ($)")),
             choices=["24 dollars per pound", "6 dollars per pound", "8.50 dollars per pound", "$\\frac{1}{6}$ pound per dollar"],
             correct=1, answer="B", why="(41 − 17) ÷ (6 − 2) = 24 ÷ 4 = 6, and (47 − 41) ÷ (7 − 6) = 6.",
             check=("many", rate([(2, 17), (6, 41), (7, 47)], "6"), ("true", "41 - 17 != 6"), ("true", "F(17, 2) != 6"),
                    ("eq", slope((17, 2), (41, 6)), "F(1,6)")),
             errors={"A": "the change in cost alone [B1G-M, AR.3.2: slope is the change in y over the change in x]", "C": "17 ÷ 2: one pair divided, as if proportional [B1G-M, AR.3.2: slope is not the constant of proportionality]", "D": "the change in pounds over the change in cost: turned over [B1G-M, AR.3.2: inverting the x- and y-values]"}),
        dict(heading="Solve the problem."),
        dict(stem="A moving company charges one fee and the same amount for every hour. The slope is 85 dollars per hour, and a 3-hour move costs \\$330. How much does a 6-hour move cost?",
             answer="\\$585", why="3 more hours cost 3 · 85 = 255, and 330 + 255 = 585.",
             check=("eq", "330 + 85*(6 - 3)", "585"), space=0.5),
        dict(stem="An online order costs \\$27 for 3 shirts, \\$45 for 6 shirts and \\$63 for 9 shirts. Ben says the rate of change is 9 dollars per shirt, because 27 ÷ 3 = 9. Is Ben correct? Explain.",
             answer="No. The rate of change is 6 dollars per shirt. The order costs \\$9 for 0 shirts, so dividing one pair does not give the rate.",
             why="(45 − 27) ÷ (6 − 3) = 6, and 27 − 3(6) = 9: not proportional.",
             check=("many", rate([(3, 27), (6, 45), (9, 63)], "6"), start([(3, 27), (6, 45)], "9"), ("true", "F(27, 3) != 6")),
             space=0.7),
        dict(stem="A crew lays tile at a constant rate of 14 square feet per hour. They have laid 28 square feet after 2 hours. After how many hours will they have laid 98 square feet?",
             answer="After 7 hours", why="(98 − 28) ÷ 14 = 70 ÷ 14 = 5 more hours, so 2 + 5 = 7; 98 ÷ 14 = 7 agrees.",
             check=("many", ("eq", "2 + F(98 - 28, 14)", "7"), ("eq", slope((2, 28), (7, 98)), "14"),
                    ("eq", "F(98, 14)", "7"), ("eq", "F(28, 2)", "14")), space=0.5),
    ],

    te=dict(
        must="Students find the slope of a linear relationship from a table, a graph and a written description of a real-world context, and they give it with its unit. They explain what the slope means in a sentence that uses both units, and a negative slope as an amount that goes down.",
        must_not="This lesson does not name the y-intercept, which comes in lesson 10.05, and it never compares the slopes of two lines. No question asks for the equation of a line.",
        read_first=[
            "Wednesday 20 January, a 43-minute day. The kit's timing table must total 53, so the table is the full lesson; the cut is under Materials. Built from the benchmarks and the B1G-M first (the unit's Lesson Outlines, §10.04, and its standing decisions 2, 5, 6, 7, 13 and 15).",
            "Every slope is the change in y divided by the change in x, with its unit, the y-unit per x-unit, and every meaning is a sentence with both units. Notes I says once that IXL calls a linear relationship a linear function; the pages keep 'linear relationship'. Read the scales first: the graphs count by 20, 150, 3 and 60.",
            "Board 9 and the set's last question turn on Unit 7's habit of dividing one pair: it gives the rate only when the line passes through the origin."],
        materials="Whiteboards and markers. On this 43-minute day, skip whiteboard question 4 first (the stack of cups) and then whiteboard question 8 (the tickets). Shorten the warm-up to 4 minutes, and the Independent Set goes home. Do not cut whiteboard questions 3 and 5 (the two votes) or question 9.",
        variation="Boards 1 and 2 use one table, and only the question changes, from the slope to its meaning; 3 votes on a meaning; 4 is a description with two moments; 5 votes on a slope from a table with unequal steps; 6 is a falling graph; 7 carries the truck's boxes as the extra number; 8 finds a missing cost; 9 is written. The set breaks the pattern at question 6, a table that is not proportional.",
        audit=["Every slope re-derived by sympy at build time from the printed points, each consecutive pair of every table; every graph drawn from its equation by u10/figs10.py, which refuses a marked point that is not on its line; every wrong option checked from its error."],
        changes=["Built from the benchmarks and the unit plan; no Math Nation item is reproduced."],
    ),
)
