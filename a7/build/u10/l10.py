# A7 10.10 Writing Equations for Contexts (MA.8.AR.3.3 with MA.8.AR.3.5) — Wed 27 Jan, a 43-minute day.
# Built from the unit's Lesson Outlines, section 10.10. Every equation is checked over the real numbers in u:
# rule(key, start, rate) — the key is the story's start + rate·u; sat / fails — a pair on or off a line.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs10 as figs
S = figs.slide

X = "sp.Symbol('u', real=True)"


def _u(e):
    import re
    return re.sub(r"\bu\b", X, e)


def rule(key, start, rate):
    """The key (in u) is the story's equation: start + rate·u, the same expression."""
    return ("true", "sp.expand((" + _u(key) + ") - ((" + start + ") + (" + rate + ")*" + X + ")) == 0")


def not_rule(expr, start, rate):
    """A wrong option is NOT the story's equation."""
    return ("true", "sp.expand((" + _u(expr) + ") - ((" + start + ") + (" + rate + ")*" + X + ")) != 0")


def sat(rhs, x, y):
    """(x, y) makes y = rhs true (rhs in u)."""
    return ("true", "sp.simplify((" + _u(rhs) + ").subs(" + X + ", " + x + ") - (" + y + ")) == 0")


def fails(rhs, x, y):
    """(x, y) makes y = rhs false."""
    return ("true", "sp.simplify((" + _u(rhs) + ").subs(" + X + ", " + x + ") - (" + y + ")) != 0")


def table_of(rhs, xs, ys):
    """Each y of a printed table is rhs at its x."""
    return ("many",) + tuple(sat(rhs, str(a), str(b)) for a, b in zip(xs, ys))


def two_moments(rhs, p, q, slope, b):
    """The line through the two moments p and q: its slope, its b, and both moments on rhs."""
    (x1, y1), (x2, y2) = p, q
    return ("many", ("eq", "F(" + y2 + " - (" + y1 + "), " + x2 + " - (" + x1 + "))", slope),
            ("eq", "(" + y1 + ") - (" + slope + ")*(" + x1 + ")", b),
            sat(rhs, x1, y1), sat(rhs, x2, y2))


# ---- the figures
# Example 2: the fuel in a truck's tank versus the miles driven (miles by 100, gallons by 10).
EX2_P = figs.plane((0, 600), (0, 40), xs=100, ys=10, xname="distance (miles)", yname="fuel (gallons)",
                   lines=[(Fr(-1, 20), 30, "")], points=[(0, 30, None, "ur"), (200, 20, None, "ur")], inches=4.2, pt=18)
EX2 = S(EX2_P, inches=4.2, pt=18, reserve=0.75)
EX2W = S(figs.plane((0, 600), (0, 40), xs=100, ys=10, xname="distance (miles)", yname="fuel (gallons)",
                    lines=[(Fr(-1, 20), 30, "")], points=[(0, 30, None, "ur"), (200, 20, None, "ur")], inches=4.6, pt=16),
         inches=4.6, pt=16, reserve=0.9)
# Your Turn 2: the water left in a cooler versus the cups poured (cups by 10, liters by 2).
YT2_P = figs.plane((0, 80), (0, 20), xs=10, ys=2, ystep=2, aspect=0.6, xname="cups poured", yname="water (liters)",
                   lines=[(Fr(-1, 4), 18, "")], points=[(0, 18, None, "ur"), (40, 8, None, "ur")], inches=4.2, pt=18)
YT2 = S(YT2_P, inches=4.2, pt=18, reserve=0.75)
YT2A = S(YT2_P, inches=4.2, pt=18, reserve=0.95)
# Board 5: a table whose steps are 2, then 1 (decision 5).
T5 = figs.table([([1, 3, 4], [55, 125, 160])], head=("hours", "cost ($)"), cw=2.0, rh=1.5, inches=6.0, pt=18)


L = dict(
    code="10.10", unit=10, lesson_no=10,
    align="=",
    title="Writing Equations for Contexts",
    unit_title="Linear Relationships",
    benchmark="MA.8.AR.3.3",
    benchmark_text="Given a table, graph or written description of a linear relationship, write an equation in slope-intercept form.",
    benchmarks=[("MA.8.AR.3.3", "Given a table, graph or written description of a linear relationship, write an equation in slope-intercept form."),
                ("MA.8.AR.3.5", "Given a real-world context, determine and interpret the slope and y-intercept of a two-variable linear equation from a written description, a table, a graph or an equation in slope-intercept form.")],
    target="I can write an equation in slope-intercept form for a real-world linear relationship and tell what each variable stands for.",
    essential="In a story, which number is the slope and which is the y-intercept, and how do you find them when the story does not give them?",
    building_on="Lesson 10.09 wrote the equation of a line from a graph, a table or two points. Lessons 10.07 and 10.08 read the slope and the y-intercept of a story as the rate and the start.",
    working_toward="The Unit 10 test on Thursday asks for an equation from a story, a graph and a table. Unit 13 writes the equation of a line of fit for a scatter plot.",
    vocab=[],
    vocab_slide=False,
    ixl=["Write linear functions: word problems — YK6"],
    closure="Whiteboard question 9 is written work and it is the exit evidence. A full answer says that Dev exchanged the rate and the start, writes c = 10n + 25, and says that n is the number of classes.",

    mtr=[("MTR.4.1", "On whiteboard questions 3 and 5, students convince a neighbor and then vote again when the room is split."),
         ("MTR.7.1", "Students write an equation for a gym, a caterer, a moving company, a truck's fuel and a cooler, and say what each letter stands for."),
         ("MTR.6.1", "Students check each equation by substituting a moment from the story, as whiteboard question 5 does with all three pairs of its table.")],
    hoq=[("Why is the cost of 0 guests the y-intercept, even though nobody throws a party for 0 guests?", "DOK 2"),
         ("The table starts at 1 hour, not 0. How can you still find the start?", "DOK 2"),
         ("A bus pass's equation can be written a = 40 − 2.5n or a = −2.5n + 40. Why are they the same equation?", "DOK 2"),
         ("On whiteboard question 6, why does the answer say 'about 5 points'?", "DOK 3")],
    differentiation=[
        ("ESE / 504", "Students keep a two-row card on the desk, 'rate: the slope' and 'start: the y-intercept', and circle each number in a story before writing the equation."),
        ("ELL", "The words rate (how much for every 1), start (the amount at 0), fee (a charge paid once) and left (what remains) are posted with a picture of each."),
        ("Enrichment", "Students who finish whiteboard question 4 early find the plant's height after 12 weeks and the week it reaches 50 centimeters (41 centimeters; week 15).")],

    warmup=[
        dict(stem="Write the equation of the line through (0, −1) and (2, 5).", answer="y = 3x − 1",
             check=("many", ("eq", "F(5 - (-1), 2 - 0)", "3"), sat("3*u - 1", "0", "-1"), sat("3*u - 1", "2", "5"))),
        dict(stem="A pond holds 90 gallons after 2 hours of filling and 180 gallons after 5 hours. Find the rate of change.",
             answer="30 gallons per hour",
             check=("eq", "F(180 - 90, 5 - 2)", "30")),
        dict(stem="A ride costs a \\$5 fee plus \\$2 for every mile. Is the cost proportional to the miles?",
             answer="No, a ride of 0 miles costs \\$5.",
             check=("true", "5 + 2*0 != 0")),
        dict(stem="Solve for b:  $86 = 12(3) + b$", answer="b = 50",
             check=("eq", "86 - 12*3", "50")),
    ],

    notes=[
        dict(numeral="I", head="Name the variables", min=4,
             items=["A gym charges a \\$35 sign-up fee and \\$20 every month.",
                    "Let n be the number of months and c the total cost in dollars."],
             math=["$c = 20n + 35$"],
             items2=["**The rate is the slope, and the start is the y-intercept.**"],
             letters=False),
        dict(numeral="II", head="An amount that goes down", min=4,
             items=["A bus pass holds \\$40, and every ride costs \\$2.50.",
                    "Let n be the number of rides and a the amount left, in dollars."],
             math=["$a = 40 - 2.5n$", "$a = -2.5n + 40$"],
             items2=["**An amount that goes down has a negative slope.**"],
             letters=False, align=False),
    ],

    examples=[
        dict(title="Example 1", min_q=1,
             prompt=["A caterer charges a setup fee and the same amount for every guest.",
                     "A party of 40 guests costs \\$700, and a party of 100 guests costs \\$1,300."],
             ask="Write an equation for the cost c, in dollars, of a party of g guests.",
             worked=[dict(min=3,
                          rows=[("m = \\frac{1300 - 700}{100 - 40} = \\frac{600}{60} = 10", "the slope, dollars per guest"),
                                ("700 = 10(40) + b", "substitute a point"),
                                ("700 = 400 + b", "multiply"),
                                ("b = 300", "solve for b")],
                          answer="c = 10g + 300")],
             check=("many", two_moments("10*u + 300", ("40", "700"), ("100", "1300"), "10", "300"),
                    rule("10*u + 300", "300", "10")),
             your_turn=dict(min=3,
                            prompt=["A moving company charges a truck fee and the same amount per hour.",
                                    "A 2-hour job costs \\$410, and a 5-hour job costs \\$650.",
                                    "Write an equation for the cost c, in dollars, of a job of h hours."],
                            ask="",
                            steps=["The slope:  $\\frac{650 - 410}{5 - 2} = \\frac{240}{3} = 80$",
                                   "Substitute a point:  $410 = 80(2) + b$",
                                   "Solve for b:  $b = 250$"],
                            answer="c = 80h + 250"),
             yt_check=("many", two_moments("80*u + 250", ("2", "410"), ("5", "650"), "80", "250"),
                       rule("80*u + 250", "250", "80"))),
        dict(title="Example 2", min_q=1,
             prompt=["The graph shows the fuel in a truck's tank, in gallons, versus the distance driven, in miles."],
             fig=EX2,
             ask="Write an equation for the fuel g, in gallons, after d miles.",
             worked=[dict(min=2, lead="Read the scales first.",
                          rows=[("b = 30", "the y-intercept: 30 gallons at the start"),
                                ("m = \\frac{20 - 30}{200 - 0} = \\frac{-10}{200} = -0.05", "gallons per mile")],
                          fig=EX2W, answer="g = −0.05d + 30")],
             check=("many", two_moments("-F(1,20)*u + 30", ("0", "30"), ("200", "20"), "-F(1,20)", "30"),
                    rule("-F(5,100)*u + 30", "30", "-F(1,20)")),
             your_turn=dict(min=3,
                            prompt=["The graph shows the water left in a cooler, in liters, versus the cups poured."],
                            fig=YT2, fig_a=YT2A, ask="Write an equation for the water w, in liters, after c cups.",
                            steps=["The y-intercept:  $b = 18$",
                                   "The slope:  $\\frac{8 - 18}{40} = -0.25$"],
                            answer="w = −0.25c + 18"),
             yt_check=("many", two_moments("-F(1,4)*u + 18", ("0", "18"), ("40", "8"), "-F(1,4)", "18"),
                       rule("-F(25,100)*u + 18", "18", "-F(1,4)"))),
    ],

    # The round: a rate and a start (1); one thing changes, the amount goes down (2); the diagnostic on which number is
    # which (3); two moments (4, the second cut); a table whose steps are 2 then 1, voted (5); the one look ahead to
    # Unit 13, a line of fit's slope read (6, the first cut); the tank's size as the extra number (7); backwards, the
    # missing start (8); Dev's exchanged rate and start, written (9).
    whiteboard=[
        dict(text=["A kayak rental costs \\$15 plus \\$10 for every hour.",
                   "**Write an equation for the cost c, in dollars,", "**of renting for h hours."],
             steps=["The rate is the slope:  $m = 10$", "The start is the y-intercept:  $b = 15$"],
             answer="c = 10h + 15",
             check=rule("10*u + 15", "15", "10"),
             wrong="c = 15h + 10 — the rate and the start exchanged [B1G-M, AR.3.3: swapping m and b]; c = 25h — the two numbers added into one rate [Notes I: the rate is the slope, and the start is the y-intercept]"),
        # repeat_ok: board 2 is board 1 with one thing changed (the amount goes down), as the plan sets it; the 10 is
        # the point of the pair.
        dict(repeat_ok=True,
             text=["A kayak pass is loaded with \\$150, and every hour of rental costs \\$10.",
                   "**Write an equation for the amount a, in dollars,", "**left on the pass after h hours."],
             steps=["The start is the y-intercept:  $b = 150$", "The amount goes down:  $m = -10$"],
             answer="a = 150 − 10h",
             check=rule("150 - 10*u", "150", "-10"),
             wrong="a = 10h + 150 — the amount made to go up [Notes II: an amount that goes down has a negative slope]; a = 150h − 10 — the rate and the start exchanged [B1G-M, AR.3.3: swapping m and b]"),
        dict(kind="mc",
             text=["A phone plan costs \\$30 a month plus \\$0.25 for every text.",
                   "**Which equation gives the monthly cost c, in dollars, for t texts?"],
             qtext="A phone plan costs \\$30 a month plus \\$0.25 for every text. Which equation gives the monthly cost c, in dollars, for t texts?",
             steps=["The rate is the slope:  $m = 0.25$", "The start is the y-intercept:  $b = 30$"],
             choices=["$c = 0.25(t + 30)$", "$c = 0.25t + 30$", "$c = 30.25t$", "$c = 30t + 0.25$"], correct=1,
             answer="B — c = 0.25t + 30",
             errors={"A": "the start put inside the parentheses, so the 0.25 multiplies it too [B1G-M, AR.3.5: identifying m and b]", "C": "the two numbers added into one rate [Notes I: the rate is the slope, and the start is the y-intercept]", "D": "the rate and the start exchanged [B1G-M, AR.3.3: swapping m and b]"},
             check=("many", rule("F(1,4)*u + 30", "30", "F(1,4)"),
                    not_rule("30*u + F(1,4)", "30", "F(1,4)"), not_rule("F(121,4)*u", "30", "F(1,4)"),
                    not_rule("F(1,4)*(u + 30)", "30", "F(1,4)"))),
        dict(text=["A plant grows at a constant rate. It is 11 centimeters tall after",
                   "2 weeks and 20 centimeters tall after 5 weeks.",
                   "**Write an equation for its height h, in centimeters, after w weeks."],
             steps=["The slope:  $\\frac{20 - 11}{5 - 2} = \\frac{9}{3} = 3$",
                    "Substitute a point:  $11 = 3(2) + b$",
                    "Solve for b:  $b = 5$"],
             answer="h = 3w + 5",
             check=("many", two_moments("3*u + 5", ("2", "11"), ("5", "20"), "3", "5"), rule("3*u + 5", "5", "3")),
             wrong="h = 3w — the slope with no start [B1G-M, AR.3.5: substitute a point and the slope to find b]; h = 3w + 11 — the height after 2 weeks taken as the start [Notes I: the start is the y-intercept]; h = 5w + 3 — the slope and b exchanged [B1G-M, AR.3.3: swapping m and b]"),
        dict(kind="mc",
             text=["The table shows the cost, in dollars, of a rental for h hours.",
                   "**Which equation gives the cost c for h hours?"],
             qtext="The table shows the cost, in dollars, of a rental: 1 hour costs \\$55, 3 hours cost \\$125 and 4 hours cost \\$160. Which equation gives the cost c for h hours?",
             fig=S(T5, inches=6.0, pt=18, reserve=0.75), fig_a=S(T5, inches=6.0, pt=18, reserve=0.95),
             steps=["The slope:  $\\frac{125 - 55}{3 - 1} = 35$",
                    "Substitute a point:  $55 = 35(1) + b$",
                    "Solve for b:  $b = 20$"],
             choices=["$c = 35h + 20$", "$c = 20h + 35$", "$c = 35h + 55$", "$c = 55h$"], correct=0,
             answer="A — c = 35h + 20",
             errors={"B": "the rate and the start exchanged [B1G-M, AR.3.3: swapping m and b]", "C": "the first cost taken as the start, but \\$55 is the cost for 1 hour, not 0 [Notes I: the start is the y-intercept]", "D": "the first pair taken as a proportional rate, \\$55 for 1 hour [B1G-M, AR.3.2: a slope is not a constant of proportionality unless the line passes through the origin]"},
             check=("many", table_of("35*u + 20", [1, 3, 4], [55, 125, 160]),
                    fails("55*u", "3", "125"), fails("35*u + 55", "1", "55"), fails("20*u + 35", "3", "125"))),
        dict(text=["A class graphs each student's test score s versus the hours h",
                   "that the student studied.",
                   "A line through the middle of the points is s = 5h + 62.",
                   "**What does the 5 mean?"],
             steps=["The slope is the rate:  5 points for every 1 hour",
                    "One more hour:  $5(3) + 62 - (5(2) + 62) = 5$"],
             answer="A student scores about 5 points more for every extra hour of study.",
             check=("eq", "(5*3 + 62) - (5*2 + 62)", "5"),
             wrong="'a score of 5 with no study' — the slope read as the y-intercept [B1G-M, AR.3.5: identifying and interpreting m and b]; '5 hours of study' — the slope read as an amount of x [B1G-M, AR.3.5: context confusion]"),
        dict(text=["A 60-gallon aquarium holds 14 gallons, and a pump adds",
                   "4 gallons every minute.",
                   "**Write an equation for the gallons g after t minutes."],
             unneeded="60",
             steps=["The rate is the slope:  $m = 4$", "The start is the y-intercept:  $b = 14$"],
             answer="g = 4t + 14",
             check=rule("4*u + 14", "14", "4"),
             wrong="g = 4t + 60 — the aquarium's size taken as the start [an extra number, included on purpose]; g = 14t + 4 — the rate and the start exchanged [B1G-M, AR.3.3: swapping m and b]"),
        dict(text=["A ride of d miles costs  $c = 1.5d + □$  dollars, and a 6-mile",
                   "ride costs \\$13.50.",
                   "**Find the missing number."],
             steps=["Substitute the ride:  $13.50 = 1.5(6) + 4.50$",
                    "Subtract 9 from 13.50:  $13.50 - 9 = 4.50$"],
             answer="4.50",
             check=("eq", "F(1350, 100) - F(3, 2)*6", "F(9, 2)"),
             wrong="9 — 1.5(6) taken for the missing number [B1G-M, AR.3.5: identifying m and b]; 22.50 — 9 added to 13.50 instead of subtracted [Notes I: the start is the y-intercept]; 2.25 — 13.50 divided by 6, the whole cost taken as the rate [B1G-M, AR.3.2: a slope is not a constant of proportionality unless the line passes through the origin]"),
        dict(kind="written",
             text=["A studio charges a \\$25 sign-up fee and \\$10 for every class.",
                   "Dev writes c = 25n + 10.",
                   "**What is Dev's mistake? Write the correct equation,",
                   "**and tell what n stands for."],
             qtext="A studio charges a \\$25 sign-up fee and \\$10 for every class. Dev writes c = 25n + 10. What is Dev's mistake? Write the correct equation and tell what n stands for.",
             steps=["The rate is the slope, and the start is the y-intercept:  $c = 10n + 25$",
                    "n is the number of classes"],
             answer="Dev exchanged the rate and the start. It is c = 10n + 25 for n classes.",
             check=("many", rule("10*u + 25", "25", "10"), not_rule("25*u + 10", "25", "10")),
             wrong="'c = 10n + 25' with no reason — the equation without the mistake named [B1G-M, AR.3.3: swapping m and b]; 'n is the cost' — the letters of the story mixed up [B1G-M, AR.3.5: context confusion]"),
    ],

    # The six: a rate and a start (1); an amount that goes down (2); two moments (3); a table whose steps are 3 then
    # 4 (4); a graph with scales (5); two moments again, with the slope and the y-intercept each explained (6).
    independent=[
        dict(stem="Mini golf costs \\$9 for a club plus \\$4 a round. Write an equation for the cost c, in dollars, of r rounds.",
             answer="c = 4r + 9", why="The rate, \\$4 per round, is the slope; the start, \\$9 for a club, is the y-intercept.",
             check=rule("4*u + 9", "9", "4"), space=0.5),
        dict(stem="A gift card holds \\$80, and every smoothie costs \\$4. Write an equation for the amount a, in dollars, left on the card after s smoothies.",
             answer="a = 80 − 4s", why="The card starts at \\$80 and goes down \\$4 for every smoothie, so the slope is −4: a = −4s + 80.",
             check=rule("80 - 4*u", "80", "-4"), space=0.5),
        dict(stem="An electrician charges a fee plus the same amount for every hour. Two hours cost \\$145, and six hours cost \\$285. Write an equation for the cost c of h hours.",
             answer="c = 35h + 75", why="The slope is (285 − 145) ÷ (6 − 2) = 140 ÷ 4 = 35. Substitute a point: 145 = 35(2) + b, so b = 75.",
             check=("many", two_moments("35*u + 75", ("2", "145"), ("6", "285"), "35", "75"), rule("35*u + 75", "75", "35")),
             space=0.9),
        dict(stem="A pool fills at a constant rate. The table shows its water g, in gallons, after t minutes. Write an equation for g.",
             fig=figs.table([([3, 6, 10], [70, 100, 140])], head=("minutes", "gallons"), inches=3.6),
             answer="g = 10t + 40", why="The slope is (100 − 70) ÷ (6 − 3) = 30 ÷ 3 = 10, and (140 − 100) ÷ (10 − 6) = 10 too. Substitute a point: 70 = 10(3) + b, so b = 40.",
             check=("many", table_of("10*u + 40", [3, 6, 10], [70, 100, 140]), rule("10*u + 40", "40", "10")),
             space=0.9),
        dict(stem="The graph shows a train's distance d, in miles, after t hours. Write an equation for d.",
             fig=figs.plane((0, 8), (0, 450), ys=50, aspect=0.6, xname="time (hours)", yname="distance (miles)",
                            lines=[(80, 50, "")], points=[(0, 50, None, "r"), (3, 290, None, "dr")], inches=3.2),
             answer="d = 80t + 50", why="The line starts at (0, 50), so b = 50. The slope is (290 − 50) ÷ (3 − 0) = 240 ÷ 3 = 80.",
             check=("many", two_moments("80*u + 50", ("0", "50"), ("3", "290"), "80", "50"), rule("80*u + 50", "50", "80")),
             space=0.7),
        dict(stem="A tutor charges a fee plus a rate per session. Four sessions cost \\$110, and ten cost \\$230. Write an equation for the cost c of s sessions, and explain its slope and y-intercept.",
             answer="c = 20s + 30. The slope, 20, means every session costs \\$20. The y-intercept, 30, is the fee, \\$30.",
             why="The slope is (230 − 110) ÷ (10 − 4) = 120 ÷ 6 = 20. Substitute a point: 110 = 20(4) + b, so b = 30.",
             check=("many", two_moments("20*u + 30", ("4", "110"), ("10", "230"), "20", "30"), rule("20*u + 30", "30", "20")),
             space=1.0),
    ],

    # Bank: a rate and a start (1); an amount that goes down (2); two moments, rising and falling (3–4); a table (5);
    # a graph (6); the diagnostic on which number is which (7) and on a table's first pair (8); the missing start (9);
    # the slope and the y-intercept explained (10); a mistake found (11); a select-all of one equation written two
    # ways (12). The additional bank mirrors it position by position with new numbers.
    bank=[
        dict(heading="Write an equation for the situation."),
        dict(stem="A music app charges a \\$10 sign-up fee and \\$4 every month. Write an equation for the total cost c, in dollars, after n months.",
             answer="c = 4n + 10", why="The rate, \\$4 per month, is the slope; the fee, \\$10, is the y-intercept.",
             check=rule("4*u + 10", "10", "4"), space=0.5),
        dict(stem="An arcade card holds \\$35, and every game costs \\$0.25. Write an equation for the amount a, in dollars, left on the card after n games.",
             answer="a = 35 − 0.25n", why="The amount goes down \\$0.25 for every game, so the slope is −0.25: a = −0.25n + 35.",
             check=rule("35 - F(1,4)*u", "35", "-F(1,4)"), space=0.5),
        dict(heading="Use the two moments."),
        dict(stem="A plumber charges a trip fee and the same amount for every hour. A 1-hour job costs \\$125, and a 3-hour job costs \\$285. Write an equation for the cost c, in dollars, of a job of h hours.",
             answer="c = 80h + 45", why="The slope is (285 − 125) ÷ (3 − 1) = 160 ÷ 2 = 80. Substitute a point: 125 = 80(1) + b, so b = 45.",
             check=("many", two_moments("80*u + 45", ("1", "125"), ("3", "285"), "80", "45"), rule("80*u + 45", "45", "80")),
             space=0.9),
        dict(stem="A car uses fuel at a constant rate. It has 18 gallons in its tank after 100 miles and 8 gallons after 300 miles. Write an equation for the fuel g, in gallons, after d miles.",
             answer="g = −0.05d + 23", why="The slope is (8 − 18) ÷ (300 − 100) = −10 ÷ 200 = −0.05. Substitute a point: 18 = −0.05(100) + b, so b = 23.",
             check=("many", two_moments("-F(1,20)*u + 23", ("100", "18"), ("300", "8"), "-F(1,20)", "23"), rule("-F(1,20)*u + 23", "23", "-F(1,20)")),
             space=0.9),
        dict(heading="Use the table."),
        dict(stem="The table shows the cost, in dollars, of renting a bounce house for h hours. Write an equation for the cost c, in dollars, of h hours.",
             fig=figs.table([([2, 5, 6], [45, 75, 85])], head=("hours", "cost ($)"), inches=3.6),
             answer="c = 10h + 25", why="The slope is (75 − 45) ÷ (5 − 2) = 30 ÷ 3 = 10. Substitute a point: 45 = 10(2) + b, so b = 25.",
             check=("many", table_of("10*u + 25", [2, 5, 6], [45, 75, 85]), rule("10*u + 25", "25", "10")), space=0.8),
        dict(heading="Use the graph."),
        dict(stem="The graph shows the money in a savings account, in dollars, versus the time, in weeks. Write an equation for the amount a, in dollars, after w weeks.",
             fig=figs.plane((0, 8), (0, 160), ys=20, xname="time (weeks)", yname="savings ($)",
                            lines=[(20, 40, "")], points=[(0, 40, None, "r"), (4, 120, None, "dr")], inches=3.0),
             answer="a = 20w + 40", why="The line starts at (0, 40), so b = 40. The slope is (120 − 40) ÷ (4 − 0) = 80 ÷ 4 = 20.",
             check=("many", two_moments("20*u + 40", ("0", "40"), ("4", "120"), "20", "40"), rule("20*u + 40", "40", "20")),
             space=0.7),
        dict(heading="Choose one."),
        dict(stem="A parking garage charges \\$3 to enter plus \\$4 for every hour. Which equation gives the cost c, in dollars, of parking for h hours?",
             choices=["$c = 7h$", "$c = 4(h + 3)$", "$c = 4h + 3$", "$c = 3h + 4$"], correct=2, answer="C",
             why="The rate, \\$4 per hour, is the slope; the \\$3 to enter is the y-intercept.",
             errors={"A": "the two numbers added into one rate [Notes I: the rate is the slope, and the start is the y-intercept]", "B": "the start put inside the parentheses, so the 4 multiplies it too [B1G-M, AR.3.5: identifying m and b]", "D": "the rate and the start exchanged [B1G-M, AR.3.3: swapping m and b]"},
             check=("many", rule("4*u + 3", "3", "4"), not_rule("3*u + 4", "3", "4"), not_rule("7*u", "3", "4"),
                    not_rule("4*(u + 3)", "3", "4"))),
        dict(stem="The table shows the cost, in dollars, of renting a boat: 1 hour costs \\$50, 2 hours cost \\$85 and 5 hours cost \\$190. Which equation gives the cost c for h hours?",
             choices=["$c = 50h$", "$c = 15h + 35$", "$c = 35h + 50$", "$c = 35h + 15$"], correct=3, answer="D",
             why="The slope is (85 − 50) ÷ (2 − 1) = 35. Substitute a point: 50 = 35(1) + b, so b = 15.",
             errors={"A": "the first pair taken as a proportional rate, \\$50 for 1 hour [B1G-M, AR.3.2: a slope is not a constant of proportionality unless the line passes through the origin]", "B": "the rate and the start exchanged [B1G-M, AR.3.3: swapping m and b]", "C": "the first cost taken as the start, but \\$50 is the cost for 1 hour, not 0 [Notes I: the start is the y-intercept]"},
             check=("many", table_of("35*u + 15", [1, 2, 5], [50, 85, 190]),
                    fails("50*u", "2", "85"), fails("35*u + 50", "1", "50"), fails("15*u + 35", "2", "85"))),
        dict(heading="Find the missing number."),
        dict(stem="A ride of d miles costs $c = 3d + □$ dollars, and a 4-mile ride costs \\$17.50. What number goes in the box?",
             answer="5.50", why="A 4-mile ride: 3(4) = 12, so the box is 17.50 − 12 = 5.50.",
             check=("eq", "F(1750, 100) - 3*4", "F(11, 2)"), space=0.6),
        dict(heading="Explain the numbers."),
        dict(stem="The equation w = 80t + 300 gives the water w, in gallons, in a pool t hours after a hose is turned on.",
             parts=[dict(label="a", stem="What does 80 mean?", answer="The pool gains 80 gallons every hour.",
                         why="80 is the slope, the rate: gallons per hour.",
                         check=("eq", "(80*2 + 300) - (80*1 + 300)", "80"), space=0.4),
                    dict(label="b", stem="What does 300 mean?", answer="The pool held 300 gallons when the hose was turned on.",
                         why="300 is the y-intercept, the water when t is 0.",
                         check=("eq", "80*0 + 300", "300"), space=0.4)]),
        dict(heading="Find the mistake."),
        dict(stem="A gym charges a \\$40 sign-up fee and \\$20 every month. Sam writes c = 40n + 20. What is Sam's mistake? Write the correct equation.",
             answer="Sam exchanged the rate and the start. The equation is c = 20n + 40.",
             why="The rate, \\$20 per month, is the slope, and the fee, \\$40, is the y-intercept.",
             check=("many", rule("20*u + 40", "40", "20"), not_rule("40*u + 20", "40", "20")), space=0.7),
        dict(heading="Select all that apply."),
        dict(stem="A tablet's battery is at 80 percent and loses 10 percent every hour. Select all the equations that give the charge p, in percent, after h hours.",
             choices=["$p = 10h + 80$", "$p = -10h + 80$", "$p = 80 - 10h$", "$p = 80h - 10$", "$p = 70h$"], correct=[1, 2],
             answer="B, C",
             why="The charge starts at 80 and goes down 10 every hour: p = −10h + 80, which is also written p = 80 − 10h.",
             errors={"A": "the charge made to go up [Notes II: an amount that goes down has a negative slope]", "D": "the rate and the start exchanged [B1G-M, AR.3.3: swapping m and b]", "E": "the two numbers combined into one rate [Notes I: the rate is the slope, and the start is the y-intercept]"},
             check=("many", rule("80 - 10*u", "80", "-10"), rule("-10*u + 80", "80", "-10"),
                    not_rule("10*u + 80", "80", "-10"), not_rule("80*u - 10", "80", "-10"), not_rule("70*u", "80", "-10"))),
    ],

    additional=[
        dict(heading="Write an equation for the situation."),
        dict(stem="A streaming service charges a \\$20 sign-up fee and \\$3 every month. Write an equation for the total cost c, in dollars, after n months.",
             answer="c = 3n + 20", why="The rate, \\$3 per month, is the slope; the fee, \\$20, is the y-intercept.",
             check=rule("3*u + 20", "20", "3"), space=0.5),
        dict(stem="A copy card holds \\$10, and every copy costs \\$0.05. Write an equation for the amount a, in dollars, left on the card after n copies.",
             answer="a = 10 − 0.05n", why="The amount goes down \\$0.05 for every copy, so the slope is −0.05: a = −0.05n + 10.",
             check=rule("10 - F(1,20)*u", "10", "-F(1,20)"), space=0.5),
        dict(heading="Use the two moments."),
        dict(stem="A florist charges a delivery fee and the same amount for every flower. An order of 12 flowers costs \\$150, and an order of 30 flowers costs \\$330. Write an equation for the cost c, in dollars, of f flowers.",
             answer="c = 10f + 30", why="The slope is (330 − 150) ÷ (30 − 12) = 180 ÷ 18 = 10. Substitute a point: 150 = 10(12) + b, so b = 30.",
             check=("many", two_moments("10*u + 30", ("12", "150"), ("30", "330"), "10", "30"), rule("10*u + 30", "30", "10")),
             space=0.9),
        dict(stem="A mower uses fuel at a constant rate. It has 10 liters in its tank after 8 minutes and 7 liters after 20 minutes. Write an equation for the fuel f, in liters, after t minutes.",
             answer="f = −0.25t + 12", why="The slope is (7 − 10) ÷ (20 − 8) = −3 ÷ 12 = −0.25. Substitute a point: 10 = −0.25(8) + b, so b = 12.",
             check=("many", two_moments("-F(1,4)*u + 12", ("8", "10"), ("20", "7"), "-F(1,4)", "12"), rule("-F(1,4)*u + 12", "12", "-F(1,4)")),
             space=0.9),
        dict(heading="Use the table."),
        dict(stem="The table shows the cost, in dollars, of renting a canoe for h hours. Write an equation for the cost c, in dollars, of h hours.",
             fig=figs.table([([1, 4, 5], [35, 95, 115])], head=("hours", "cost ($)"), inches=3.6),
             answer="c = 20h + 15", why="The slope is (95 − 35) ÷ (4 − 1) = 60 ÷ 3 = 20. Substitute a point: 35 = 20(1) + b, so b = 15.",
             check=("many", table_of("20*u + 15", [1, 4, 5], [35, 95, 115]), rule("20*u + 15", "15", "20")), space=0.8),
        dict(heading="Use the graph."),
        dict(stem="The graph shows the money in a savings account, in dollars, versus the time, in weeks. Write an equation for the amount a, in dollars, after w weeks.",
             fig=figs.plane((0, 8), (0, 350), ys=50, xname="time (weeks)", yname="savings ($)",
                            lines=[(35, 50, "")], points=[(0, 50, None, "dr"), (4, 190, None, "dr")], inches=3.0),
             answer="a = 35w + 50", why="The line starts at (0, 50), so b = 50. The slope is (190 − 50) ÷ (4 − 0) = 140 ÷ 4 = 35.",
             check=("many", two_moments("35*u + 50", ("0", "50"), ("4", "190"), "35", "50"), rule("35*u + 50", "50", "35")),
             space=0.7),
        dict(heading="Choose one."),
        dict(stem="A bike rental charges \\$5 to start plus \\$3 for every hour. Which equation gives the cost c, in dollars, of renting for h hours?",
             choices=["$c = 5h + 3$", "$c = 3h + 5$", "$c = 8h$", "$c = 3(h + 5)$"], correct=1, answer="B",
             why="The rate, \\$3 per hour, is the slope; the \\$5 to start is the y-intercept.",
             errors={"A": "the rate and the start exchanged [B1G-M, AR.3.3: swapping m and b]", "C": "the two numbers added into one rate [Notes I: the rate is the slope, and the start is the y-intercept]", "D": "the start put inside the parentheses, so the 3 multiplies it too [B1G-M, AR.3.5: identifying m and b]"},
             check=("many", rule("3*u + 5", "5", "3"), not_rule("8*u", "5", "3"), not_rule("3*(u + 5)", "5", "3"),
                    not_rule("5*u + 3", "5", "3"))),
        dict(stem="The table shows the cost, in dollars, of a lawn service: 1 hour costs \\$110, 2 hours cost \\$190 and 4 hours cost \\$350. Which equation gives the cost c for h hours?",
             choices=["$c = 110h$", "$c = 30h + 80$", "$c = 80h + 30$", "$c = 80h + 110$"], correct=2, answer="C",
             why="The slope is (190 − 110) ÷ (2 − 1) = 80. Substitute a point: 110 = 80(1) + b, so b = 30.",
             errors={"A": "the first pair taken as a proportional rate, \\$110 for 1 hour [B1G-M, AR.3.2: a slope is not a constant of proportionality unless the line passes through the origin]", "B": "the rate and the start exchanged [B1G-M, AR.3.3: swapping m and b]", "D": "the first cost taken as the start, but \\$110 is the cost for 1 hour, not 0 [Notes I: the start is the y-intercept]"},
             check=("many", table_of("80*u + 30", [1, 2, 4], [110, 190, 350]),
                    fails("110*u", "2", "190"), fails("80*u + 110", "1", "110"), fails("30*u + 80", "2", "190"))),
        dict(heading="Find the missing number."),
        dict(stem="A ride of d miles costs $c = 4d + □$ dollars, and a 3-mile ride costs \\$15.25. What number goes in the box?",
             answer="3.25", why="A 3-mile ride: 4(3) = 12, so the box is 15.25 − 12 = 3.25.",
             check=("eq", "F(1525, 100) - 4*3", "F(13, 4)"), space=0.6),
        dict(heading="Explain the numbers."),
        dict(stem="The equation h = 3t + 20 gives the height h, in centimeters, of a sunflower t days after a gardener first measures it.",
             parts=[dict(label="a", stem="What does 3 mean?", answer="The sunflower grows 3 centimeters every day.",
                         why="3 is the slope, the rate: centimeters per day.",
                         check=("eq", "(3*2 + 20) - (3*1 + 20)", "3"), space=0.4),
                    dict(label="b", stem="What does 20 mean?", answer="The sunflower was 20 centimeters tall when it was first measured.",
                         why="20 is the y-intercept, the height when t is 0.",
                         check=("eq", "3*0 + 20", "20"), space=0.4)]),
        dict(heading="Find the mistake."),
        dict(stem="A climbing gym charges a \\$20 entry fee and \\$3 for every hour of gear rental. Leo writes c = 20h + 3. What is Leo's mistake? Write the correct equation.",
             answer="Leo exchanged the rate and the start. The equation is c = 3h + 20.",
             why="The rate, \\$3 per hour, is the slope, and the fee, \\$20, is the y-intercept.",
             check=("many", rule("3*u + 20", "20", "3"), not_rule("20*u + 3", "20", "3")), space=0.7),
        dict(heading="Select all that apply."),
        dict(stem="A gift card holds \\$35, and every snack costs \\$3. Select all the equations that give the amount a, in dollars, left on the card after s snacks.",
             choices=["$a = 3s + 35$", "$a = 32s$", "$a = 35 - 3s$", "$a = 35s - 3$", "$a = -3s + 35$"], correct=[2, 4],
             answer="C, E",
             why="The card starts at \\$35 and goes down \\$3 for every snack: a = −3s + 35, which is also written a = 35 − 3s.",
             errors={"A": "the amount made to go up [Notes II: an amount that goes down has a negative slope]", "B": "the two numbers combined into one rate [Notes I: the rate is the slope, and the start is the y-intercept]", "D": "the rate and the start exchanged [B1G-M, AR.3.3: swapping m and b]"},
             check=("many", rule("35 - 3*u", "35", "-3"), rule("-3*u + 35", "35", "-3"),
                    not_rule("3*u + 35", "35", "-3"), not_rule("32*u", "35", "-3"), not_rule("35*u - 3", "35", "-3"))),
    ],

    te=dict(
        must="Students write an equation in slope-intercept form from a written description, a table or a graph of a real-world linear relationship. They determine and interpret the slope and the y-intercept in the story's own units.",
        must_not="Point-slope form and standard form are not expected at this grade. Students do not compare the slopes or y-intercepts of two linear equations, and lines of fit are previewed once, on whiteboard question 6, and taught in Unit 13.",
        read_first=[
            "Wednesday 27 January is a 43-minute day, the day before the unit test. The timing table is the full 53-minute lesson, and the cut is under Materials.",
            "The lesson has two Notes slides and no vocabulary slide: every word it uses was named earlier in the unit. Notes I names the variables and reads the rate as the slope and the start as the y-intercept; Notes II shows an amount that goes down, written both ways.",
            "When a story gives two moments and no start, students find the slope, then substitute a point and solve for b, as Example 1 and whiteboard question 4 do. Example 2 and its Your Turn read the scales first and find the slope from the marked points.",
            "Whiteboard question 6 is the unit's one look ahead to Unit 13. It reads the slope of a line drawn through a class's scores and says 'about', because the line is drawn through the middle of the points."],
        materials="Whiteboards and markers, and the Independent Set, one per student. On this 43-minute day the first cut is whiteboard question 6 and the second is whiteboard question 4. The warm-up takes 4 minutes, and the Independent Set questions 4 to 6 go home. Whiteboard questions 3 and 5 are never cut, because they are the round's two diagnostic questions.",
        variation="Whiteboard questions 1 and 2 give a rate and a start, and only one thing changes between them: the amount goes down. Question 3 votes on which number is which, and question 4 gives two moments with no start. The pattern breaks at question 5: the table starts at 1 hour, so its first cost is not the start. Question 6 reads a line of fit, question 7 carries the aquarium's size as an extra number, question 8 runs backwards to the start, and question 9 is written.",
        audit=["Every equation is checked at build time against its story: the rate and the start, both moments of a two-moment story, and every pair of every printed table; every wrong option is checked to differ from the story's equation.",
               "The graphs are drawn from their equations by the unit's figure module, which refuses a marked point that is not on its line."],
        changes=["The warm-up's third answer is written as a whole sentence: 'No, a ride of 0 miles costs $5.'",
                 "Whiteboard question 8's answer is written 4.50, because money has two decimals."],
    ),
)
