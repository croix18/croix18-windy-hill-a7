# A7 10.07+08 Interpreting Slope and y-Intercept (MA.8.AR.3.5) — two book lessons, one day (Mon 25 Jan).
# Built from the unit's Lesson Outlines, section "10.07+08". Figures from u10/figs10.py.
# Checks: every slope is the change in y over the change in x, every y-intercept the value at x = 0, computed by
# sympy from the printed numbers (decimals as exact Rationals); every table is checked point by point on its line.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs10 as figs
S = figs.slide

U = "sp.Symbol('u', real=True)"


def R(v):
    return "sp.Rational('" + str(v) + "')"


def slope2(x1, y1, x2, y2, m):
    """The change in y divided by the change in x between two printed points is m."""
    return ("eq", "(" + R(y2) + " - " + R(y1) + ") / (" + R(x2) + " - " + R(x1) + ")", m)


def on_line(xs, ys, m, b):
    """Every printed pair (x, y) makes y = mx + b true."""
    return ("many",) + tuple(("eq", "(" + m + ") * " + R(x) + " + (" + b + ")", R(y)) for x, y in zip(xs, ys))


def b_from(x, y, m, b):
    """Substitute the point (x, y) and solve y = m*x + b for b: the solution is the keyed b."""
    return ("eq", "sp.solve(sp.Eq(" + R(y) + ", (" + m + ") * " + R(x) + " + " + U + "), " + U + ")[0]", b)


def rate_start(expr, m, b):
    """The equation's right side, in u: its rate (the change for every 1 unit of u) is m, and its value at u = 0 is b."""
    import re
    e = re.sub(r"\bu\b", U, expr)
    return ("many", ("eq", "sp.diff(" + e + ", " + U + ")", m), ("eq", "(" + e + ").subs(" + U + ", 0)", b))


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


def GRAPH(xr, yr, m, b, pts, **k):
    """A printed graph for the set and the banks: the line y = mx + b, its readable points named."""
    return figs.plane(xr, yr, lines=[(m, b, "")], inches=3.0, **k,
                      points=[(t[0], t[1], "on") if len(t) == 2 else (t[0], t[1], None, t[2]) for t in pts])


def TAB(xs, ys, head):
    return figs.table([(xs, ys)], head=head, cw=1.7, inches=4.0)


# ---- notes and examples
NOTES2 = S(figs.table([([3, 5, 9], [41, 35, 23])], head=("weeks", "pounds left"), cw=2.2), inches=7.0, pt=20, reserve=1.6)

EX1_P = PL((0, 6), (0, 42), lines=[(Fr(9, 2), 12, "")], ys=6, xname="hours of rain", yname="gallons",
           points=[(0, 12, "on"), (4, 30, "on")])
YT1_P = PL((0, 5), (0, 30), lines=[(5, 5, "")], ys=5, xname="seconds", yname="meters",
           points=[(0, 5, ""), (4, 25, None, "dr")])

# ---- the boards
T4 = figs.table([([2, 4, 7], ["9,000", "7,800", "6,000"])], head=("minutes", "feet"), cw=2.0, hw=3.0, fs=18)


L = dict(
    code="10.07", unit=10, lesson_no="7–8", label="Lessons 7–8",
    title="Interpreting Slope and y-Intercept",
    unit_title="Linear Relationships",
    benchmark="MA.8.AR.3.5",
    benchmark_text="Given a real-world context, determine and interpret the slope and y-intercept of a two-variable linear equation from a written description, a table, a graph or an equation in slope-intercept form.",
    target="I can find the slope and the y-intercept of a real-world linear relationship from an equation, a graph, a table or a description, and explain what each one means.",
    essential="In a real-world linear relationship, what does the slope tell us, and what does the y-intercept tell us?",
    building_on="In lessons 10.05 and 10.06, students named the y-intercept as the value of y when x is 0 and graphed lines from y = mx + b, from tables and from contexts. In lessons 10.02–03 and 10.04, they found slope as the change in y divided by the change in x and gave it a unit.",
    working_toward="Lesson 10.09 writes the equation of a line from a graph, a table or two points, and lesson 10.10 writes equations for contexts. In Algebra 1 (MA.912.AR.2.5), students interpret the slope and intercepts of linear functions.",
    vocab=[],
    vocab_slide=False,
    ixl=["Interpret the slope and y-intercept of a linear function — H5B", "Interpret points on the graph of a linear function — 9E8"],
    closure="Whiteboard question 9 is answered in writing and serves as the exit ticket. A complete answer says that with 0 cups sold the profit is −\\$30, because the stand spent \\$30 before it sold a cup, and that the profit is negative because the spending is not yet earned back. An answer that names −30 as the y-intercept without saying what it means in the story is not complete.",

    mtr=[("MTR.2.1", "Students find the slope and the y-intercept from an equation, a table, a graph and a description of a real-world relationship."),
         ("MTR.4.1", "On whiteboard questions 3 and 5, a divided class convinces a neighbor and then votes again."),
         ("MTR.7.1", "Students explain every slope and y-intercept in a sentence that uses the story's quantities and units.")],
    hoq=[("Why is the y-intercept of the repair equation the charge for coming, and not the cost of an hour?", "DOK 2"),
         ("When a table has no row for x = 0, how can you still find the y-intercept?", "DOK 2"),
         ("Why is F = 1.8C + 32 linear but not proportional?", "DOK 3"),
         ("Why must the slope of the plane's altitude be negative before you compute it?", "DOK 2")],
    differentiation=[
        ("ESE / 504", "Provide a printed card that reads “The rate is the slope, and the start is the y-intercept.” beside a blank sentence frame: “Every ___, the ___ changes by ___.” Keep Notes II on display from whiteboard question 4 onward."),
        ("ELL", "**Rate**: how much one thing changes for every 1 unit of the other. **Start**: the amount when x is 0. **Per**: for each one (gallons per hour: gallons for each hour)."),
        ("Enrichment", "For students who finish whiteboard question 8 early: write a story whose equation is y = −3x + 45 and explain both numbers in it. (For example, a pitcher holds 45 ounces of juice and 3 ounces are poured out every minute.)")],

    warmup=[
        dict(stem="A tub holds 30 gallons and gains 6 gallons every minute. What are the y-intercept and the slope of its graph?",
             answer="30 and 6",
             check=rate_start("6*u + 30", "6", "30")),
        dict(stem="Find the slope of the line through $(2, 11)$ and $(6, 3)$.", answer="−2",
             check=slope2(2, 11, 6, 3, "-2")),
        dict(stem="Five pounds of rice cost \\$8. Write the equation for the cost c, in dollars, of w pounds.",
             answer="c = 1.6w",
             check=("eq", "F(8, 5)", R("1.6"))),
        dict(stem="Evaluate $1.8(15) + 32$.", answer="59",
             check=("eq", R("1.8") + " * 15 + 32", "59")),
    ],

    notes=[
        dict(numeral="I", head="From an equation", min=4,
             items=[("c = 45h + 60", "the cost c, in dollars, of a repair that takes h hours"),
                    ("The slope, 45", "every hour adds \\$45"),
                    ("The y-intercept, 60", "a repair of 0 hours costs \\$60, the charge for coming")],
             size=21,
             items2=["**The rate is the slope, and the start is the y-intercept.**"],
             letters=False),
        dict(numeral="II", head="From a table with no row for x = 0", min=4,
             fig=NOTES2,
             items2=["The slope:   $\\frac{35 - 41}{5 - 3} = -3$   pounds per week",
                     "Substitute a point and solve for b:   $41 = -3(3) + b$,  so  $b = 50$.",
                     "Check with $(9, 23)$:   $-3(9) + 50 = 23$.   The bag held 50 pounds at the start."],
             letters=False),
        dict(numeral="III", head="Temperature: linear, not proportional", min=3, size=21,
             math=["$F = 1.8C + 32$"],
             items=[("The slope, 1.8", "a rise of 1 degree Celsius is a rise of 1.8 degrees Fahrenheit"),
                    ("The y-intercept, 32", "0 degrees Celsius is 32 degrees Fahrenheit")],
             items2=["10 °C is 50 °F and 20 °C is 68 °F: double the Celsius is not double the Fahrenheit."],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=1,
             prompt=["The graph shows the water in a rain barrel during a storm."], fig=B(EX1_P),
             ask="Find the slope and the y-intercept, and explain what each means.",
             worked=[dict(min=2,
                          rows=[("\\text{slope} = \\frac{30 - 12}{4 - 0} = \\frac{18}{4} = 4.5", "read the scales first: gallons count by 6"),
                                ("4.5 \\text{ gallons per hour}", "the barrel gains 4.5 gallons every hour"),
                                ("\\text{y-intercept} = 12", "the barrel held 12 gallons when the rain began")],
                          fig=BA(EX1_P), answer="Slope 4.5;  y-intercept 12")],
             check=("many", slope2(0, 12, 4, 30, R("4.5")), on_line([0, 4], [12, 30], R("4.5"), "12")),
             your_turn=dict(min=2,
                            prompt=["The graph shows a skater's distance from the wall."],
                            fig=B(YT1_P), fig_a=BA(YT1_P),
                            ask="Find the slope and the y-intercept, and explain what each means.",
                            steps=["Slope:  $\\frac{25 - 5}{4 - 0} = 5$", "y-intercept:  5"],
                            answer="Slope 5;  y-intercept 5"),
             yt_check=("many", slope2(0, 5, 4, 25, "5"), on_line([0, 4], [5, 25], "5", "5"))),
        dict(title="Example 2", min_q=1,
             prompt=["A pool is filled at a constant rate. After 2 hours it holds 1,100 gallons,",
                     "and after 5 hours it holds 1,850 gallons."],
             ask="Find the slope and the y-intercept, and explain what each means.",
             worked=[dict(min=2,
                          rows=[("\\text{slope} = \\frac{1850 - 1100}{5 - 2} = \\frac{750}{3} = 250", "250 gallons per hour"),
                                ("1100 = 250(2) + b", "substitute a point and solve for b"),
                                ("b = 600", "the pool held 600 gallons when the filling began")],
                          answer="Slope 250;  y-intercept 600")],
             check=("many", slope2(2, 1100, 5, 1850, "250"), b_from(2, 1100, "250", "600"), on_line([2, 5], [1100, 1850], "250", "600")),
             your_turn=dict(min=3,
                            prompt=["A taxi charges a starting amount and the same amount for every mile.",
                                    "A 3-mile ride costs \\$14.50, and a 7-mile ride costs \\$26.50."],
                            ask="Find the slope and the y-intercept, and explain what each means.",
                            steps=["The slope:  $\\frac{26.50 - 14.50}{7 - 3} = \\frac{12}{4} = 3$ dollars per mile",
                                   "Solve for b:  $14.5 = 3(3) + b$,  so  $b = 5.5$",
                                   "The ride costs \\$5.50 before the first mile"],
                            answer="Slope 3;  y-intercept 5.5"),
             yt_check=("many", slope2(3, "14.50", 7, "26.50", "3"), b_from(3, "14.50", "3", R("5.5")),
                       on_line([3, 7], ["14.50", "26.50"], "3", R("5.5")))),
    ],

    # The round: the slope of an equation explained (1), the same equation's y-intercept (2: one thing changes, the
    # number asked about), the diagnostic on what a y-intercept means (3), a table with unequal steps and a negative
    # slope (4), the diagnostic on its y-intercept (5), the temperature formula (6), a description with an extra number (7),
    # backwards (8), and the pattern breaks at 9 — a negative y-intercept, written.
    whiteboard=[
        dict(text=["$p = 9h + 15$ gives Maya's pay p, in dollars, for a shift of h hours.", "**What does the 9 mean?"],
             qtext="p = 9h + 15 gives Maya's pay p, in dollars, for a shift of h hours. What does the 9 mean?",
             steps=["9 multiplies h:  the slope", "The unit:  dollars per hour"],
             answer="She earns \\$9 for every hour.",
             check=rate_start("9*u + 15", "9", "15"),
             wrong="'she is paid \\$9 to start' — the slope read as the y-intercept [B1G-M, AR.3.5: identifying and interpreting m and b]; 'she works 9 hours' — read as a value of h [B1G-M, AR.3.5: context confusion]"),
        # repeat_ok: the same equation as whiteboard question 1 on purpose — one thing changes, the number asked about.
        dict(repeat_ok=True, text=["Use the same equation,  $p = 9h + 15$.", "**What does the 15 mean?"],
             qtext="Use the same equation, p = 9h + 15, Maya's pay p, in dollars, for a shift of h hours. What does the 15 mean?",
             steps=["At $h = 0$:  $p = 9(0) + 15 = 15$", "The y-intercept:  15 dollars"],
             answer="She is paid \\$15 for a shift of 0 hours: an amount added to every shift.",
             check=rate_start("9*u + 15", "9", "15"),
             wrong="'she earns \\$15 every hour' — the y-intercept read as the slope [B1G-M, AR.3.5: identifying and interpreting m and b]"),
        dict(kind="mc", text=["$c = 0.35n + 2.5$ gives the cost c, in dollars, of printing n photos.", "**What does 2.5 mean?"],
             qtext="c = 0.35n + 2.5 gives the cost c, in dollars, of printing n photos. What does 2.5 mean?",
             steps=["At $n = 0$:  $c = 0.35(0) + 2.5 = 2.5$", "The y-intercept:  a charge of \\$2.50 before any photo"],
             choices=["The whole order costs \\$2.50.", "The order has 2.5 photos.", "Each photo costs \\$2.50.", "There is a \\$2.50 charge before any photo is printed."], correct=3,
             answer="D — There is a \\$2.50 charge before any photo is printed.",
             errors={"A": "the y-intercept read as the total cost [B1G-M, AR.3.5: context confusion]", "B": "2.5 read as a value of n [B1G-M, AR.3.5: context confusion]", "C": "the slope and the y-intercept exchanged [B1G-M, AR.3.5: identifying and interpreting m and b]"},
             check=("many", rate_start(R("0.35") + "*u + " + R("2.5"), R("0.35"), R("2.5")),
                    ("true", R("0.35") + " != " + R("2.5")),
                    ("true", "not " + R("2.5") + ".is_integer"),
                    ("true", R("0.35") + " * 1 + " + R("2.5") + " != " + R("2.5")))),
        dict(text=["A plane descends at a constant rate.", "The table shows its altitude, in feet, minutes into the descent.",
                   "**Find the slope and explain what it means."],
             qtext="A plane descends at a constant rate. The table gives its altitude 2, 4 and 7 minutes after the descent began: 9,000, 7,800 and 6,000 feet. Find the slope and explain what it means.",
             fig=TB(T4), fig_a=TBA(T4),
             steps=["$\\frac{7800 - 9000}{4 - 2} = -600$", "Check:  $\\frac{6000 - 7800}{7 - 4} = -600$"],
             answer="−600 feet per minute: the plane goes down 600 feet every minute.",
             check=("many", slope2(2, 9000, 4, 7800, "-600"), slope2(4, 7800, 7, 6000, "-600"),
                    on_line([2, 4, 7], [9000, 7800, 6000], "-600", "10200")),
             wrong="600 — the sign dropped [Notes II: a negative slope]; −1,200 — the change in y alone, the steps of 2 and 3 minutes ignored [B1G-M, AR.3.2: slope from a table with unequal steps]"),
        dict(kind="mc", text=["Use the same table.", "**What is the y-intercept, and what does it mean?"],
             qtext="Use the same table: the altitude 2, 4 and 7 minutes after the descent began is 9,000, 7,800 and 6,000 feet. What is the y-intercept, and what does it mean?",
             fig=TB(T4), fig_a=TBA(T4),
             steps=["Solve for b:  $9000 = -600(2) + b$", "$b = 10200$"],
             choices=["9,000 feet, when the descent began", "9,600 feet, when the descent began", "10,200 feet, when the descent began", "−600 feet, the drop every minute"], correct=2,
             answer="C — 10,200 feet, the altitude when the descent began",
             errors={"A": "the first row read as the start [B1G-M, AR.3.5: x = 0 not in the table]", "B": "one minute stepped back from the first row, not two [B1G-M, AR.3.5: x = 0 not in the table]", "D": "the slope given for the y-intercept [B1G-M, AR.3.5: identifying and interpreting m and b]"},
             check=("many", b_from(2, 9000, "-600", "10200"), on_line([2, 4, 7], [9000, 7800, 6000], "-600", "10200"),
                    ("true", "9000 != 10200"), ("true", "-600 != 10200"), ("eq", "9000 + 600", "9600"), ("true", "9600 != 10200"))),
        # repeat_ok: F = 1.8C + 32 is the state's own formula, printed wherever it is used (decision 14); this asks a rise
        # of 5 degrees, a value Notes III does not show.
        dict(repeat_ok=True, text=["Use  $F = 1.8C + 32$.  The temperature rises 5 degrees Celsius.",
                   "**By how many degrees Fahrenheit does it rise?"],
             qtext="Use F = 1.8C + 32. The temperature rises 5 degrees Celsius. By how many degrees Fahrenheit does it rise?",
             steps=["The slope:  1.8 degrees Fahrenheit for every 1 degree Celsius", "$1.8(5) = 9$"],
             answer="9 degrees Fahrenheit",
             check=("many", ("eq", R("1.8") + " * 5", "9"),
                    ("eq", "(" + R("1.8") + " * 25 + 32) - (" + R("1.8") + " * 20 + 32)", "9")),
             wrong="41 — 1.8(5) + 32, the temperature at 5 °C, not the rise [Notes III: the y-intercept, 32]; 37 — 5 + 32 [Notes III: the slope, 1.8]"),
        # repeat_ok: 4.5 is also Example 1's slope — the plan's numbers (a coincidence of values, a new story asked a new way).
        dict(repeat_ok=True,
             text=["A climbing gym that is open 12 hours a day charges \\$6 for shoes", "and \\$4.50 for every hour of climbing.",
                   "**What are the slope and the y-intercept of the cost versus hours?"],
             qtext="A climbing gym that is open 12 hours a day charges \\$6 for shoes and \\$4.50 for every hour of climbing. What are the slope and the y-intercept of the graph of cost versus hours?",
             unneeded="12",
             steps=["The rate:  \\$4.50 for every hour:  the slope, 4.5", "The start:  \\$6 for shoes:  the y-intercept, 6"],
             answer="Slope 4.5;  y-intercept 6",
             check=rate_start(R("4.5") + "*u + 6", R("4.5"), "6"),
             wrong="12 — the hours the gym is open [an extra number, included on purpose]; 6 and 4.5 — the slope and the y-intercept exchanged [B1G-M, AR.3.5: identifying and interpreting m and b]"),
        dict(text=["A job's cost has a slope of 40 dollars per hour.", "A 3-hour job costs \\$155.",
                   "**What is the y-intercept?"],
             qtext="A job's cost has a slope of 40 dollars per hour, and a 3-hour job costs \\$155. What is the y-intercept?",
             steps=["Substitute a point and solve for b:  $155 = 40(3) + b$", "$155 = 120 + b$", "$b = 35$"],
             answer="35",
             check=("many", b_from(3, 155, "40", "35"), ("eq", "155 - 40*3", "35")),
             wrong="155 — the cost of the 3-hour job given as the start [B1G-M, AR.3.5: x = 0 not in the table]; 115 — 155 − 40, one hour taken off, not three [B1G-M, AR.3.5: x = 0 not in the table]"),
        dict(kind="written", text=["$p = 1.5n - 30$ gives a lemonade stand's profit p, in dollars,", "after it sells n cups.",
                                   "**What does −30 mean? Why is it negative?"],
             qtext="p = 1.5n − 30 gives a lemonade stand's profit p, in dollars, after it sells n cups. What does −30 mean? Why is it negative?",
             steps=["At $n = 0$:  $p = 1.5(0) - 30 = -30$", "With 0 cups sold, the stand has spent \\$30 and earned nothing"],
             answer="With 0 cups sold the profit is −\\$30: the stand spent \\$30 before it sold a cup.",
             check=rate_start(R("1.5") + "*u - 30", R("1.5"), "-30"),
             wrong="'the stand loses \\$30 for every cup' — the y-intercept read as the slope [B1G-M, AR.3.5: identifying and interpreting m and b]; 'it is negative because cups are subtracted' — the sign read as a decrease [B1G-M, AR.3.5: context confusion]"),
    ],

    # The six: an equation, both numbers explained (1); a graph with a scale (2); a table that shows x = 0 (3); a table
    # with no row for x = 0 (4); a description with two moments (5); and the pattern breaks at 6 — the temperature
    # formula, a value and its 32.
    independent=[
        dict(stem="The equation $c = 5g + 9$ gives the cost c, in dollars, of g games at a bowling alley. What are the slope and the y-intercept, and what does each mean?",
             answer="Slope 5: each game adds \\$5. y-intercept 9: the cost is \\$9 before any game is played.",
             why="5 multiplies g, so the cost rises \\$5 for every game. At g = 0, c = 5(0) + 9 = 9.",
             check=rate_start("5*u + 9", "5", "9"), space=0.6),
        dict(stem="The graph shows a hot-air balloon's height, in feet, versus time, in minutes. Find the slope and the y-intercept, and explain what each means.",
             fig=GRAPH((0, 5), (0, 270), 45, 30, [(0, 30), (2, 120)], ys=30, ystep=2, aspect=0.6, xname="minutes", yname="height (ft)"),
             answer="Slope 45: the balloon rises 45 feet every minute. y-intercept 30: it was 30 feet up when the timing began.",
             why="Read the scales first: feet count by 30. (120 − 30) ÷ (2 − 0) = 90 ÷ 2 = 45 feet per minute; the line meets the y-axis at 30.",
             check=("many", slope2(0, 30, 2, 120, "45"), on_line([0, 2], [30, 120], "45", "30")), space=0.5),
        dict(stem="The table shows the charge left in a phone's battery. Find the slope and the y-intercept, and explain what each means.",
             fig=TAB([0, 2, 5, 6], [90, 84, 75, 72], ("hours", "percent left")),
             answer="Slope −3: the battery loses 3 percent every hour. y-intercept 90: it was at 90 percent at the start.",
             why="(84 − 90) ÷ (2 − 0) = −3; check (72 − 75) ÷ (6 − 5) = −3. The table shows x = 0: y = 90.",
             check=("many", slope2(0, 90, 2, 84, "-3"), on_line([0, 2, 5, 6], [90, 84, 75, 72], "-3", "90")), space=0.5),
        dict(stem="A bike-share ride costs a starting amount plus the same amount for every minute. Find the slope and the y-intercept, and explain what each means.",
             fig=TAB([4, 10, 16], ["3.40", "5.50", "7.60"], ("minutes", "cost ($)")),
             answer="Slope 0.35: each minute adds \\$0.35. y-intercept 2: the ride costs \\$2.00 before the first minute.",
             why="(5.50 − 3.40) ÷ (10 − 4) = 2.10 ÷ 6 = 0.35. Substitute a point and solve for b: 3.40 = 0.35(4) + b, so b = 2.",
             check=("many", slope2(4, "3.40", 10, "5.50", R("0.35")), b_from(4, "3.40", R("0.35"), "2"),
                    on_line([4, 10, 16], ["3.40", "5.50", "7.60"], R("0.35"), "2")), space=0.6),
        dict(stem="A kayak rental charges a fee plus the same amount for every hour. A 2-hour rental costs \\$30, and a 5-hour rental costs \\$57. Find the slope and the y-intercept, and explain what each means.",
             answer="Slope 9: each hour adds \\$9. y-intercept 12: the rental costs \\$12 before the first hour.",
             why="(57 − 30) ÷ (5 − 2) = 27 ÷ 3 = 9. Substitute a point and solve for b: 30 = 9(2) + b, so b = 12.",
             check=("many", slope2(2, 30, 5, 57, "9"), b_from(2, 30, "9", "12"), on_line([2, 5], [30, 57], "9", "12")), space=0.8),
        # repeat_ok: F = 1.8C + 32 is the state's own formula (decision 14); 35 °C is a value shown nowhere above.
        dict(repeat_ok=True, stem="Use $F = 1.8C + 32$ to change 35 °C to degrees Fahrenheit. Then explain what the 32 means.",
             answer="95 °F. The 32 means 0 °C is 32 °F.",
             why="1.8(35) + 32 = 63 + 32 = 95. At C = 0, F = 1.8(0) + 32 = 32: the y-intercept.",
             check=("many", ("eq", R("1.8") + " * 35 + 32", "95"), rate_start(R("1.8") + "*u + 32", R("1.8"), "32")), space=0.6),
    ],

    # Bank: two equations (a slope, a y-intercept), a diagnostic on a slope's meaning, two tables (no row for x = 0; one
    # with it and falling), two graphs (rising; a diagnostic on a falling line's y-intercept), two descriptions (rising;
    # falling), the temperature formula twice, backwards, and a negative y-intercept explained. The additional bank
    # mirrors it position by position with new numbers.
    bank=[
        dict(heading="Explain what the number means."),
        dict(stem="The equation $c = 5n + 12$ gives the cost c, in dollars, of a craft class that uses n kits. What does the 5 mean?",
             answer="Each kit adds \\$5 to the cost.", why="5 multiplies n: the slope, 5 dollars per kit.",
             check=rate_start("5*u + 12", "5", "12"), space=0.5),
        dict(stem="The equation $h = -3t + 45$ gives the depth h, in centimeters, of the water in a vase t days after it is filled. What does the 45 mean?",
             answer="The water was 45 centimeters deep when the vase was filled.", why="At t = 0, h = −3(0) + 45 = 45: the y-intercept.",
             check=rate_start("-3*u + 45", "-3", "45"), space=0.5),
        dict(heading="Choose one."),
        dict(stem="The equation $c = 9n + 40$ gives the cost c, in dollars, of a phone plan for n months, with a one-time fee to start. What does 9 mean?",
             choices=["The fee to start is \\$9.", "Each month adds \\$9 to the cost.", "The plan lasts 9 months.", "The whole plan costs \\$9."],
             correct=1, answer="B",
             why="9 multiplies n: the slope, 9 dollars per month. The fee to start is 40, the y-intercept.",
             errors={"A": "the slope and the y-intercept exchanged [B1G-M, AR.3.5: identifying and interpreting m and b]", "C": "9 read as a value of n [B1G-M, AR.3.5: context confusion]", "D": "the slope read as the total cost [B1G-M, AR.3.5: context confusion]"},
             check=("many", rate_start("9*u + 40", "9", "40"), ("true", "9 != 40"), ("eq", "9*1 + 40", "49"), ("true", "49 != 9")), space=0.3),
        dict(heading="Use the table."),
        dict(stem="A bamboo shoot grows at a constant rate. Find the slope and the y-intercept. What does the y-intercept mean?",
             fig=TAB([2, 3, 6], [14, 17, 26], ("days", "height (cm)")),
             answer="Slope 3, y-intercept 8: the shoot was 8 centimeters tall when the measuring began.",
             why="(17 − 14) ÷ (3 − 2) = 3. Substitute a point and solve for b: 14 = 3(2) + b, so b = 8. Check: 3(6) + 8 = 26.",
             check=("many", slope2(2, 14, 3, 17, "3"), b_from(2, 14, "3", "8"), on_line([2, 3, 6], [14, 17, 26], "3", "8")), space=0.6),
        dict(stem="A cooler's ice melts at a constant rate. What is the slope, and what does it mean?",
             fig=TAB([0, 2, 3, 7], [40, 34, 31, 19], ("hours", "pounds of ice")),
             answer="−3 pounds per hour: the cooler loses 3 pounds of ice every hour.",
             why="(34 − 40) ÷ (2 − 0) = −3; check (19 − 31) ÷ (7 − 3) = −12 ÷ 4 = −3.",
             check=("many", slope2(0, 40, 2, 34, "-3"), on_line([0, 2, 3, 7], [40, 34, 31, 19], "-3", "40")), space=0.5),
        dict(heading="Use the graph."),
        dict(stem="The graph shows a bus's distance from the station, in miles, versus time, in hours. Find the slope and the y-intercept, and explain what each means.",
             fig=GRAPH((0, 5), (0, 200), 40, 20, [(0, 20), (2, 100)], ys=20, ystep=2, aspect=0.6, xname="hours", yname="miles"),
             answer="Slope 40: the bus moves 40 miles farther from the station every hour. y-intercept 20: it was 20 miles from the station at the start.",
             why="Read the scales first: miles count by 20. (100 − 20) ÷ (2 − 0) = 40; the line meets the y-axis at 20.",
             check=("many", slope2(0, 20, 2, 100, "40"), on_line([0, 2], [20, 100], "40", "20")), space=0.5),
        dict(stem="The graph shows the fuel in a generator, in liters, versus the hours it runs. What does the y-intercept mean?",
             fig=GRAPH((0, 7), (0, 21), -3, 18, [(0, 18), (2, 12)], ys=3, xname="hours", yname="liters"),
             choices=["The generator held 18 liters at the start.", "The generator uses 3 liters every hour.", "The generator runs for 18 hours.", "The generator uses 18 liters every hour."], correct=0, answer="A",
             why="The line meets the y-axis at (0, 18): 18 liters at 0 hours.",
             errors={"B": "the slope's meaning given for the y-intercept [B1G-M, AR.3.5: identifying and interpreting m and b]", "C": "18 read as a value of x, the hours [B1G-M, AR.3.5: context confusion]", "D": "the y-intercept read as the slope [B1G-M, AR.3.5: identifying and interpreting m and b]"},
             check=("many", on_line([0, 2], [18, 12], "-3", "18"), slope2(0, 18, 2, 12, "-3"), ("true", "-3 != 18"),
                    ("eq", "sp.solve(-3*" + U + " + 18, " + U + ")[0]", "6"), ("true", "6 != 18")), space=0.3),
        dict(heading="Use the description."),
        dict(stem="A boat rental charges a fee plus the same amount for every hour. A 2-hour rental costs \\$130, and a 5-hour rental costs \\$265. What is the y-intercept, and what does it mean?",
             answer="40: the rental costs \\$40 before the first hour.",
             why="(265 − 130) ÷ (5 − 2) = 135 ÷ 3 = 45. Substitute a point and solve for b: 130 = 45(2) + b, so b = 40.",
             check=("many", slope2(2, 130, 5, 265, "45"), b_from(2, 130, "45", "40")), space=0.7),
        dict(stem="A gift card loses the same amount with every coffee. It has \\$41 left after 2 coffees and \\$23 left after 6 coffees. How much money was on the card at the start?",
             answer="\\$50", why="(23 − 41) ÷ (6 − 2) = −18 ÷ 4 = −4.5. Substitute a point and solve for b: 41 = −4.5(2) + b, so b = 50.",
             check=("many", slope2(2, 41, 6, 23, R("-4.5")), b_from(2, 41, R("-4.5"), "50")), space=0.7),
        dict(heading="For questions 10 and 11, use F = 1.8C + 32."),
        dict(stem="What is 25 °C in degrees Fahrenheit?", answer="77 °F", why="1.8(25) + 32 = 45 + 32 = 77.",
             check=("eq", R("1.8") + " * 25 + 32", "77"), space=0.4),
        dict(stem="The temperature rises 20 degrees Celsius. By how many degrees Fahrenheit does it rise?", answer="36 degrees Fahrenheit",
             why="The slope is 1.8 degrees Fahrenheit for every 1 degree Celsius: 1.8(20) = 36.",
             check=("eq", R("1.8") + " * 20", "36"), space=0.4),
        dict(heading="Find the missing number."),
        dict(stem="A job's cost has a slope of 9 dollars per hour, and a 4-hour job costs \\$50. What is the y-intercept?", answer="14",
             why="Substitute a point and solve for b: 50 = 9(4) + b = 36 + b, so b = 14.",
             check=b_from(4, 50, "9", "14"), space=0.5),
        dict(heading="Explain."),
        dict(stem="The equation $p = 3n - 45$ gives a bake sale's profit p, in dollars, after it sells n boxes of cookies. What does −45 mean? Why is it negative?",
             answer="With 0 boxes sold the profit is −\\$45: the sale spent \\$45 before it sold a box.",
             why="At n = 0, p = 3(0) − 45 = −45. The money spent is not yet earned back.",
             check=rate_start("3*u - 45", "3", "-45"), space=0.7),
    ],

    additional=[
        dict(heading="Explain what the number means."),
        dict(stem="The equation $c = 3n + 8$ gives the cost c, in dollars, of a day at a fair with n rides. What does the 3 mean?",
             answer="Each ride adds \\$3 to the cost.", why="3 multiplies n: the slope, 3 dollars per ride.",
             check=rate_start("3*u + 8", "3", "8"), space=0.5),
        dict(stem="The equation $g = -5t + 60$ gives the gas g, in gallons, in a tour bus's tank t hours into a trip. What does the 60 mean?",
             answer="The tank held 60 gallons when the trip began.", why="At t = 0, g = −5(0) + 60 = 60: the y-intercept.",
             check=rate_start("-5*u + 60", "-5", "60"), space=0.5),
        dict(heading="Choose one."),
        dict(stem="The equation $c = 45n + 30$ gives the cost c, in dollars, of n music lessons, with a one-time fee to sign up. What does 45 mean?",
             choices=["The whole cost is \\$45.", "The fee to sign up is \\$45.", "Each lesson adds \\$45 to the cost.", "There are 45 lessons."],
             correct=2, answer="C",
             why="45 multiplies n: the slope, 45 dollars per lesson. The fee to sign up is 30, the y-intercept.",
             errors={"A": "the slope read as the total cost [B1G-M, AR.3.5: context confusion]", "B": "the slope and the y-intercept exchanged [B1G-M, AR.3.5: identifying and interpreting m and b]", "D": "45 read as a value of n [B1G-M, AR.3.5: context confusion]"},
             check=("many", rate_start("45*u + 30", "45", "30"), ("true", "45 != 30"), ("eq", "45*1 + 30", "75"), ("true", "75 != 45")), space=0.3),
        dict(heading="Use the table."),
        dict(stem="A vine grows at a constant rate. Find the slope and the y-intercept. What does the y-intercept mean?",
             fig=TAB([2, 4, 9], [19, 29, 54], ("days", "length (cm)")),
             answer="Slope 5, y-intercept 9: the vine was 9 centimeters long when the measuring began.",
             why="(29 − 19) ÷ (4 − 2) = 5. Substitute a point and solve for b: 19 = 5(2) + b, so b = 9. Check: 5(9) + 9 = 54.",
             check=("many", slope2(2, 19, 4, 29, "5"), b_from(2, 19, "5", "9"), on_line([2, 4, 9], [19, 29, 54], "5", "9")), space=0.6),
        dict(stem="A bowl of soup cools at a constant rate. What is the slope, and what does it mean?",
             fig=TAB([0, 2, 5, 6], [180, 170, 155, 150], ("minutes", "temperature (°F)")),
             answer="−5 degrees per minute: the soup cools 5 degrees every minute.",
             why="(170 − 180) ÷ (2 − 0) = −5; check (150 − 155) ÷ (6 − 5) = −5.",
             check=("many", slope2(0, 180, 2, 170, "-5"), on_line([0, 2, 5, 6], [180, 170, 155, 150], "-5", "180")), space=0.5),
        dict(heading="Use the graph."),
        dict(stem="The graph shows the bottles a machine has filled versus time, in minutes. Find the slope and the y-intercept, and explain what each means.",
             fig=GRAPH((0, 6), (0, 2000), 250, 250, [(0, 250, "r"), (2, 750, "dr")], ys=250, ystep=2, xname="minutes", yname="bottles"),
             answer="Slope 250: the machine fills 250 bottles every minute. y-intercept 250: it had filled 250 bottles when the timing began.",
             why="Read the scales first: bottles count by 250. (750 − 250) ÷ (2 − 0) = 250; the line meets the y-axis at 250.",
             check=("many", slope2(0, 250, 2, 750, "250"), on_line([0, 2], [250, 750], "250", "250")), space=0.5),
        dict(stem="The graph shows the fuel in a boat, in gallons, versus the hours it runs. What does the y-intercept mean?",
             fig=GRAPH((0, 6), (0, 30), -5, 25, [(0, 25), (2, 15)], ys=5, ystep=2, xname="hours", yname="gallons"),
             choices=["The boat uses 5 gallons every hour.", "The boat held 25 gallons at the start.", "The boat runs for 25 hours.", "The boat uses 25 gallons every hour."], correct=1, answer="B",
             why="The line meets the y-axis at (0, 25): 25 gallons at 0 hours.",
             errors={"A": "the slope's meaning given for the y-intercept [B1G-M, AR.3.5: identifying and interpreting m and b]", "C": "25 read as a value of x, the hours [B1G-M, AR.3.5: context confusion]", "D": "the y-intercept read as the slope [B1G-M, AR.3.5: identifying and interpreting m and b]"},
             check=("many", on_line([0, 2], [25, 15], "-5", "25"), slope2(0, 25, 2, 15, "-5"), ("true", "-5 != 25"),
                    ("eq", "sp.solve(-5*" + U + " + 25, " + U + ")[0]", "5"), ("true", "5 != 25")), space=0.3),
        dict(heading="Use the description."),
        dict(stem="A bounce-house rental charges a fee plus the same amount for every hour. A 3-hour rental costs \\$150, and a 6-hour rental costs \\$270. What is the y-intercept, and what does it mean?",
             answer="30: the rental costs \\$30 before the first hour.",
             why="(270 − 150) ÷ (6 − 3) = 120 ÷ 3 = 40. Substitute a point and solve for b: 150 = 40(3) + b, so b = 30.",
             check=("many", slope2(3, 150, 6, 270, "40"), b_from(3, 150, "40", "30")), space=0.7),
        dict(stem="A transit card loses the same amount with every ride. It has \\$28 left after 4 rides and \\$16 left after 8 rides. How much money was on the card at the start?",
             answer="\\$40", why="(16 − 28) ÷ (8 − 4) = −12 ÷ 4 = −3. Substitute a point and solve for b: 28 = −3(4) + b, so b = 40.",
             check=("many", slope2(4, 28, 8, 16, "-3"), b_from(4, 28, "-3", "40")), space=0.7),
        dict(heading="For questions 10 and 11, use F = 1.8C + 32."),
        dict(stem="What is 30 °C in degrees Fahrenheit?", answer="86 °F", why="1.8(30) + 32 = 54 + 32 = 86.",
             check=("eq", R("1.8") + " * 30 + 32", "86"), space=0.4),
        dict(stem="The temperature rises 15 degrees Celsius. By how many degrees Fahrenheit does it rise?", answer="27 degrees Fahrenheit",
             why="The slope is 1.8 degrees Fahrenheit for every 1 degree Celsius: 1.8(15) = 27.",
             check=("eq", R("1.8") + " * 15", "27"), space=0.4),
        dict(heading="Find the missing number."),
        dict(stem="A job's cost has a slope of 5 dollars per hour, and a 6-hour job costs \\$41. What is the y-intercept?", answer="11",
             why="Substitute a point and solve for b: 41 = 5(6) + b = 30 + b, so b = 11.",
             check=b_from(6, 41, "5", "11"), space=0.5),
        dict(heading="Explain."),
        dict(stem="The equation $p = 5n - 40$ gives a car wash's profit p, in dollars, after it washes n cars. What does −40 mean? Why is it negative?",
             answer="With 0 cars washed the profit is −\\$40: the car wash spent \\$40 before it washed a car.",
             why="At n = 0, p = 5(0) − 40 = −40. The money spent is not yet earned back.",
             check=rate_start("5*u - 40", "5", "-40"), space=0.7),
    ],

    te=dict(
        must="Students find the slope and the y-intercept of a real-world linear relationship from an equation, a table, a graph and a written description, and they explain each one in a sentence with the story's units. Temperature conversions are included, with the formula always given.",
        must_not="Students do not compare the slopes or the y-intercepts of two linear equations. Students do not memorize the formula that changes Celsius to Fahrenheit.",
        read_first=[
            "Two book lessons (10.7 and 10.8) taught as one day. Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §10.07+08, standing decisions 2, 5, 9, 13 and 14), with Math Nation read for scope only.",
            "No new word today: the rate is the slope, and the start is the y-intercept. Every slope is said with its unit and every y-intercept as the amount when x is 0. When no row has x = 0, substitute a point and solve for b. The temperature formula is printed wherever it is used; the class is asked about its 32 and its values."],
        materials="Whiteboards and markers. The Independent Set, one per student.",
        variation="Boards 1–2 read one equation's two numbers (only the number asked about changes); 3 votes on what a y-intercept means; 4 finds a negative slope from a table with unequal steps and 5 votes on its y-intercept; 6 uses the temperature formula; 7 is a description with an extra number (the hours the gym is open); 8 runs backwards. The pattern breaks at 9 — a negative y-intercept, written. The set: an equation, a graph with a scale, a table that shows x = 0, a table with no row for x = 0, a description with two moments, then the temperature formula.",
        audit=["Every slope re-derived by sympy at build time from two printed points, every table and graph point checked on its line, and every y-intercept found by solving y = mx + b for b; decimals read as exact numbers.",
               "Every wrong option is one named error: the slope and the y-intercept exchanged, a number read as a value of x, the y-intercept read as a total, or the first row read as the start."],
        changes=["10.7 and 10.8 (interpreting slope and y-intercept; temperature) → one day: Notes I–III, one Example from a graph and one from a description.",
                 "Practice and Homework → the Independent Set: six questions, one representation at a time."],
    ),
)
