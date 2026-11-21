# A7 7.07 Comparing Proportional Relationships (MA.7.AR.4.5) — the last teaching day of Unit 7.
# Built from the unit's Lesson Outlines, section 7.07. Figures from u7/figs7.py.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs7 as figs
S = figs.slide

X = "sp.Symbol('u', real=True)"
Y = "sp.Symbol('v', real=True)"


def _u(e):
    import re
    return re.sub(r"\bu\b", X, e)


def crosses(r1, r2, x, y):
    """The system y = r1, y = r2 has exactly one solution, (x, y)."""
    return ("true", "sp.solve([sp.Eq(" + Y + ", " + _u(r1) + "), sp.Eq(" + Y + ", " + _u(r2) + ")], [" + X + ", " + Y
            + "], dict=True) == [{" + X + ": " + x + ", " + Y + ": " + y + "}]")


def rate(y, x, p):
    """y ÷ x is the constant p."""
    return ("eq", "(" + y + ")/(" + x + ")", p)


def BP(xr, yr, **kw):
    """A board's graph: drawn and sized for a question slide (4.2 in, 18 pt)."""
    return S(figs.plane(xr, yr, inches=4.2, pt=18, **kw), inches=4.2, pt=18, reserve=0.75)


def BPA(xr, yr, reserve=1.15, **kw):
    """The reveal: the same graph, with room for the red answer line."""
    return S(figs.plane(xr, yr, inches=4.2, pt=18, **kw), inches=4.2, pt=18, reserve=reserve)


# ---- notes and examples
NOTES1 = S(figs.table([([2, 4], ["25.00", "50.00"])], head=("hours", "dollars"), titles=["Ana"], cw=1.9),
           inches=4.6, pt=22, reserve=1.6)
NOTES2 = S(figs.plane((0, 6), (0, 6), lines=[figs.prop(3), figs.prop(1), figs.prop(Fr(1, 3))], inches=4.2, pt=18),
           inches=4.2, pt=18, reserve=1.0)

EX1_T = figs.table([([3, 5, 8], [54, 90, 144])], head=("minutes", "gallons"), titles=["Pump A"], cw=2.2, rh=1.6)
EX1_P = figs.plane((0, 10), (0, 160), lines=[figs.prop(16, "")], ys=20, xname="minutes", yname="gallons", xstep=2, ystep=2,
                   points=[(5, 80, "on"), (10, 160, None, "l")])
EX1 = S(figs.row([EX1_T, EX1_P], gap=1.8, titles=["", "Pump B"]), inches=8.6, pt=16, reserve=1.0)

YT1_T = figs.table([([2, 5, 6], [42, 105, 126])], head=("minutes", "gallons"), titles=["Pump C"], cw=2.2, rh=1.6)
# Pump D's gallons axis is scaled by 25, not the plan's 20: at 20 its ten rows leave the figure too small for the
# Your Turn slide (labels under 18 pt); 25 keeps (5, 100) and (10, 200) on grid corners in eight rows, as Pump B has.
YT1_P = figs.plane((0, 10), (0, 200), lines=[figs.prop(20, "")], ys=25, xname="minutes", yname="gallons", xstep=2, ystep=2,
                   points=[(5, 100, "on"), (10, 200, None, "l")])
YT1 = S(figs.row([YT1_T, YT1_P], gap=1.8, titles=["", "Pump D"]), inches=9.6, pt=16, reserve=0.9)
# the answer slide sets its steps beside the figure: Pump D's graph alone, the table's numbers are in the steps
YT1A = S(figs.row([YT1_P], titles=["Pump D"]), inches=4.4, pt=16, reserve=0.9)

EX2 = S(figs.plane((0, 9), (0, 6), lines=[figs.prop(Fr(2, 3), "")], xname="minutes", yname="meters",
                   points=[(6, 4, "on")], inches=4.4, pt=18), inches=4.4, pt=18, reserve=0.9)
YT2 = S(figs.plane((0, 8), (0, 18), lines=[figs.prop(Fr(9, 4), "")], ys=3, xname="minutes", yname="labels",
                   points=[(4, 9, "on")], inches=4.4, pt=18), inches=4.4, pt=18, reserve=0.9)

# ---- boards
RICE = figs.table([([2, 4], ["7.00", "14.00"])], head=("pounds", "cost ($)"), cw=1.9, titles=["Store A"])
RUN = dict(lines=[figs.prop(8, "Jo"), figs.prop(3, "Max")], ys=5, ystep=2, xname="seconds", yname="meters")
TAP = dict(lines=[figs.prop(5, "")], ys=5, xname="minutes", yname="liters", points=[(2, 10, "on")])
THREE = dict(lines=[figs.prop(5, "A"), figs.prop(2, "B"), figs.prop(Fr(1, 4), "C")],
             points=[(1, 5, ""), (1, 2, ""), (4, 1, "")])
LIFT = dict(lines=[figs.prop(Fr(8, 3), "")], ys=2, xname="seconds", yname="feet", points=[(3, 8, "on")])

L = dict(
    code="7.07", unit=7, lesson_no=7,
    title="Comparing Proportional Relationships",
    unit_title="Representing Proportional Relationships",
    benchmark="MA.7.AR.4.5",
    benchmark_text="Solve real-world problems involving proportional relationships.",
    target="I can compare two proportional relationships shown in different ways, and solve problems with them.",
    essential="When two relationships are shown in different ways, what one number lets us compare them?",
    building_on="7.05+06 — the equation y = px from a table, a graph and a description, either quantity as the subject; 7.02+03 — the constant of proportionality as y for each 1 of x; Grade 6 (MA.6.AR.3.5) — unit rates and the better buy.",
    working_toward="The Unit 7 test (Thu 14 Jan), questions 14 and 15; Unit 10 (19 Jan) — the steepness of a line gets its name; Grade 8 (MA.8.AR.3.4, 3.5) — comparing linear relationships.",
    vocab=[],
    vocab_slide=False,
    ixl=["Compare proportional relationships represented in different ways — 5A9"],
    closure="Board 9 is written work and it is the exit evidence: Kim is wrong — 0.6 is less than 3/4 = 0.75, so y = (3/4)x has the greater constant and, on the same axes, the steeper line. A board that says only 'no' has the verdict and not the comparison of the two constants.",

    mtr=[("MTR.4.1", "boards 3 and 6: a split room re-votes; Example 1 compares a table and a graph by their constants"),
         ("MTR.2.1", "a table, a graph, an equation and a description, each brought to y for each 1 of x"),
         ("MTR.7.1", "pumps, taps, buses, plans and an elevator: each comparison ends in the question the story asked")],
    hoq=[("Ana's table and Ben's equation look nothing alike. What one number do we find for each, and why does it settle who earns more?", "DOK 2"),
         ("On board 3 the slower runner's line is the longer one. Why does the length of a line say nothing about speed?", "DOK 3"),
         ("The elevator graph ends at 10 feet. How can we answer for 24 feet without a bigger grid?", "DOK 2")],
    differentiation=[
        ("ESE / 504", "One line stays on the board all period: \"the constant of proportionality is the amount of y for each 1 of x\" — and every comparison starts by writing each relationship's constant with its unit, side by side."),
        ("ELL", "**Compare**: say which is more or less. **Faster**: more distance in each minute or hour. **Cheaper per pound**: less money for each 1 pound. **Steeper**: climbs more for each 1 across."),
        ("Enrichment", "Board 6 finishes early for some: for how many songs do Plans P and Q cost the same? (Only 0 songs: P is \\$0.10 more for every song, so Q is cheaper for any number of songs.)")],

    warmup=[
        dict(stem="A proportional table: x is 4 and 10; y is 26 and 65. Its equation?", answer="y = 6.5x",
             check=("many", rate("26", "4", "F(13,2)"), rate("65", "10", "F(13,2)"))),
        dict(stem="A taxi charges a \\$5 fee and \\$2 a mile. Is the cost proportional?",
             answer="No — the \\$5 fee is added at the start",
             check=("true", "F(5 + 2*1, 1) != F(5 + 2*2, 2)")),
        dict(stem="Where do  $y = x + 1$  and  $y = 3x - 5$  cross?", answer="(3, 4)",
             check=crosses("u + 1", "3*u - 5", "3", "4")),
        dict(stem="Better buy: 3 pounds for \\$7.20 or 5 pounds for \\$11.50?",
             answer="5 pounds: \\$2.30 per pound against \\$2.40",
             check=("many", ("eq", "F(720,100)/3", "F(240,100)"), ("eq", "F(1150,100)/5", "F(230,100)"),
                    ("true", "F(230,100) < F(240,100)"))),
    ],

    notes=[
        dict(numeral="I", head="Compare with the constant", min=3,
             fig=NOTES1,
             math=["$\\text{Ana:}\\quad 25 \\div 2 = 12.5$", "$\\text{Ben:}\\quad e = 11h$"],
             items2=["**Make both say y for each 1 of x, then compare the constants.**",
                     "Ana earns \\$12.50 each hour; Ben earns \\$11.00. Ana earns more each hour."],
             letters=False),
        # the head is the ruling's sentence less "On the same axes,": whole, it is wider than the slide and runs over the
        # head's rule; the sentence, word for word, is the bold line under the graph.
        dict(numeral="II", head="Compare the lines on one grid", min=3,   # the sentence itself is the slide's first line
             fig=NOTES2,
             items2=["**On the same axes, the greater positive constant gives the steeper line.**",
                     "$3 > 1 > \\frac{1}{3}$:   $y = 3x$ is the steepest,   $y = \\frac{1}{3}x$ the least steep."],
             letters=False),
        dict(numeral="III", head="Then answer the question asked", min=3,
             items=["In 8 hours, how much more does Ana earn than Ben?"],
             math=["$\\text{Ana:}\\quad 12.5(8) = 100 \\qquad \\text{Ben:}\\quad 11(8) = 88$", "$100 - 88 = 12$"],
             items2=["In 8 hours Ana earns \\$12.00 more.",
                     "Past the edge of the grid, use the equation: put in what you know, solve for the other."],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=2,
             prompt=["Pump A's table and Pump B's graph show the gallons each pumps."], fig=EX1,
             ask="Which pump is faster? How many more gallons in 15 minutes?",
             worked=[dict(min=2,
                          rows=[("A:\\quad 54 \\div 3 = 18", "gallons per minute; 90 ÷ 5 and 144 ÷ 8 are 18 too"),
                                ("B:\\quad 80 \\div 5 = 16", "read the scales first: by 20 up"),
                                ("18 > 16", "Pump A is faster")],
                          answer="Pump A: 18 gallons per minute against 16"),
                     dict(min=1,
                          rows=[("A:\\quad 18(15) = 270", "gallons in 15 minutes"),
                                ("B:\\quad 16(15) = 240", "gallons in 15 minutes"),
                                ("270 - 240 = 30", "the question asked")],
                          answer="Pump A, 30 gallons more")],
             check=("many", rate("54", "3", "18"), rate("90", "5", "18"), rate("144", "8", "18"),
                    rate("80", "5", "16"), rate("160", "10", "16"), ("eq", "18*15 - 16*15", "30")),
             your_turn=dict(min=3,
                            prompt=[], fig=YT1, fig_a=YT1A,
                            ask="Which pump is faster? How many more gallons in 10 minutes?",
                            steps=["Pump C:  $42 \\div 2 = 21$",
                                   "Pump D:  $100 \\div 5 = 20$",
                                   "In 10 minutes:  $21(10) = 210$  and  $20(10) = 200$",
                                   "Difference:  $210 - 200 = 10$"],
                            answer="Pump C, 10 gallons more"),
             yt_check=("many", rate("42", "2", "21"), rate("105", "5", "21"), rate("126", "6", "21"),
                       rate("100", "5", "20"), rate("200", "10", "20"), ("eq", "21*10 - 20*10", "10"))),
        # figwords_ok: 10 meters is past the grid's edge on purpose — the example goes past the picture.
        dict(title="Example 2", min_q=1, figwords_ok=True,
             prompt=["The graph shows how far a sloth climbs."], fig=EX2,
             ask="At this rate, how many minutes to climb 10 meters?",
             worked=[dict(min=1,
                          rows=[("4 \\div 6 = \\frac{2}{3}", "meters per minute, from (6, 4)"),
                                ("d = \\frac{2}{3}t", "the equation")]),
                     dict(min=1,
                          rows=[("10 = \\frac{2}{3}t", "10 meters is past the grid's edge"),
                                ("t = 10 \\div \\frac{2}{3} = 15", "solve for t")],
                          answer="15 minutes")],
             check=("many", rate("4", "6", "F(2,3)"), ("eq", "10 / F(2,3)", "15"),
                    ("true", "sp.solve(sp.Eq(10, F(2,3)*" + X + "), " + X + ") == [15]")),
             your_turn=dict(min=3,
                            prompt=["The graph shows the labels a printer prints."], fig=YT2,
                            ask="At this rate, how many minutes to print 45 labels?",
                            steps=["Constant:  $9 \\div 4 = 2.25$  labels per minute",
                                   "Equation:  $n = 2.25t$",
                                   "Solve:  $45 = 2.25t$,  so  $t = 20$"],
                            answer="20 minutes"),
             yt_check=("many", rate("9", "4", "F(9,4)"), ("eq", "45 / F(9,4)", "20"),
                       ("true", "sp.solve(sp.Eq(45, F(9,4)*" + X + "), " + X + ") == [20]"))),
    ],

    # The round: a table against an equation (1), and again with only the equation changed (2); a vote on two lines
    # (3); a description against a graph (4); three constants read off one grid and put in order (5); a vote on which
    # plan is cheaper and by how much (6); two descriptions with the seats as the extra number (7); a graph read and
    # gone past (8, backwards); Kim's claim about digits, written (9).
    whiteboard=[
        dict(text=["Store A's rice prices are in the table.", "Store B:  $c = 3.3w$  (c dollars for w pounds).",
                   "**Which store's rice costs less per pound?"],
             qtext="Store A's rice prices are in the table: 2 pounds cost \\$7.00 and 4 pounds cost \\$14.00. Store B: c = 3.3w (c dollars for w pounds). Which store's rice costs less per pound?",
             fig=S(RICE, inches=4.6, pt=22, reserve=0.75), fig_a=S(RICE, inches=4.0, pt=20, reserve=0.95),
             steps=["Store A:  $7.00 \\div 2 = 3.50$", "Store B:  \\$3.30 per pound",
                    "Compare:  $3.30 < 3.50$"],
             answer="Store B: \\$3.30 per pound against \\$3.50",
             check=("many", rate("F(700,100)", "2", "F(7,2)"), rate("F(1400,100)", "4", "F(7,2)"),
                    ("true", "F(33,10) < F(7,2)")),
             wrong="Store A — 7.00 and 14.00 compared with 3.3 as if they were per pound [Notes I: make both say y for each 1 of x]; Store A — 2 ÷ 7.00, pounds per dollar, the ratio in the wrong order [Florida B1G-M, AR.4.2: the ratio in the wrong order]"),
        # repeat_ok: the same table as board 1 on purpose — one thing changes, Store B's equation (the plan's board 2).
        dict(repeat_ok=True, text=["The same table for Store A. Store B is now $c = 3.75w$.",
                                   "**Which store's rice costs less per pound?"],
             qtext="Store A's rice prices are in the table: 2 pounds cost \\$7.00 and 4 pounds cost \\$14.00. Store B is now c = 3.75w. Which store's rice costs less per pound?",
             fig=S(RICE, inches=4.6, pt=22, reserve=0.75), fig_a=S(RICE, inches=4.0, pt=20, reserve=0.95),
             steps=["Store A:  $14.00 \\div 4 = 3.50$", "Store B:  \\$3.75 per pound",
                    "Compare:  $3.50 < 3.75$"],
             answer="Store A: \\$3.50 per pound against \\$3.75",
             check=("many", rate("F(1400,100)", "4", "F(7,2)"), ("true", "F(7,2) < F(375,100)")),
             wrong="Store B — the answer to board 1 carried over without a new comparison [Notes I: make both say y for each 1 of x]; Store B — 2 ÷ 7.00 = 0.29 pound per dollar against 3.75, the ratio in the wrong order [Florida B1G-M, AR.4.2: the ratio in the wrong order]"),
        dict(kind="mc", text=["Two runners' distances are graphed on one grid.", "**Who is faster?"],
             qtext="The graph shows two runners' distances, in meters, against time, in seconds, on one grid. Jo's line is the steeper. Who is faster?",
             fig=BP((0, 10), (0, 40), **RUN), fig_a=BPA((0, 10), (0, 40), reserve=1.15, **RUN),
             steps=["Jo:  $40 \\div 5 = 8$  meters per second", "Max:  $30 \\div 10 = 3$  meters per second"],
             choices=["Max — the longer line", "Neither — both start at (0, 0)", "Jo — the steeper line", "Max — the lower line"],
             correct=2, answer="C — Jo — the steeper line",
             errors={"A": "the length of the drawn line read as speed [Notes II: the greater positive constant gives the steeper line]", "B": "passing through the origin taken to mean the same rate [Notes I: make both say y for each 1 of x]", "D": "the lower line read as the faster [Notes II: the greater positive constant gives the steeper line]"},
             check=("many", rate("40", "5", "8"), rate("30", "10", "3"), ("true", "8 > 3"),
                    ("true", "sqrt(10**2 + 6**2) > sqrt(5**2 + 8**2) and not (3 > 8)"),
                    ("true", "3*1 < 8*1 and not (3 > 8)"), ("true", "8 != 3"))),
        dict(text=["Tap A fills 18 liters in 4 minutes. The graph shows Tap B.", "**Which tap is faster?"],
             qtext="Tap A fills 18 liters in 4 minutes. Tap B's graph, liters against minutes, passes through (2, 10). Which tap is faster?",
             fig=BP((0, 6), (0, 30), **TAP), fig_a=BPA((0, 6), (0, 30), **TAP),
             steps=["Tap A:  $18 \\div 4 = 4.5$", "Tap B:  $10 \\div 2 = 5$", "Compare:  $5 > 4.5$"],
             answer="Tap B: 5 liters per minute against 4.5",
             check=("many", rate("18", "4", "F(9,2)"), rate("10", "2", "5"), ("true", "5 > F(9,2)")),
             wrong="Tap A — 18 liters against 10, the totals compared [Notes I: make both say y for each 1 of x]; Tap A — 4 ÷ 18 against 2 ÷ 10, minutes per liter, the ratio in the wrong order [Florida B1G-M, AR.4.2: the ratio in the wrong order]"),
        # repeat_ok: rule 43 matches only the grid's axis numbers (0 to 6, as Notes II) and the answer's digits; these three
        # lines (y = 5x, 2x, x/4) appear nowhere above.
        dict(repeat_ok=True, text=["**Order the three constants of proportionality, least to greatest."],
             qtext="Three lines through the origin are on one grid: A through (1, 5), B through (1, 2) and C through (4, 1). What are their constants of proportionality, from least to greatest?",
             fig=BP((0, 6), (0, 6), **THREE), fig_a=BPA((0, 6), (0, 6), reserve=0.95, **THREE),
             steps=["A:  $5 \\div 1 = 5$", "B:  $2 \\div 1 = 2$", "C:  $1 \\div 4 = \\frac{1}{4}$"],
             answer="1/4 (C), 2 (B), 5 (A)",
             check=("many", rate("5", "1", "5"), rate("2", "1", "2"), rate("1", "4", "F(1,4)"),
                    ("true", "F(1,4) < 2 < 5")),
             wrong="C = 4 — x ÷ y, the ratio in the wrong order [Florida B1G-M, AR.4.2: the ratio in the wrong order]; 5, 2, 1/4 — greatest first [Notes II: the greater positive constant gives the steeper line]"),
        dict(kind="mc", text=["Plan P: \\$0.90 a song. Plan Q: 12 songs for \\$9.60.",
                              "**Which is cheaper for 30 songs, and by how much?"],
             qtext="Plan P charges \\$0.90 a song. Plan Q charges \\$9.60 for 12 songs. Which plan is cheaper for 30 songs, and by how much?",
             steps=["Plan Q:  $9.60 \\div 12 = 0.80$",
                    "30 songs:  $0.90(30) = 27.00$  and  $0.80(30) = 24.00$", "Difference:  $27.00 - 24.00 = 3.00$"],
             choices=["Q, by \\$3.00", "Q, by \\$0.10", "Q, by \\$17.40", "P, by \\$3.00"],
             correct=0, answer="A — Q, by \\$3.00",
             errors={"B": "the difference for one song, 0.90 − 0.80 [Notes III: then answer the question asked]", "C": "30 songs on Plan P against the price of 12 on Plan Q: 27.00 − 9.60 [Notes I: make both say y for each 1 of x]", "D": "the plans compared backwards: the higher cost taken as cheaper [Notes III: then answer the question asked]"},
             check=("many", rate("F(960,100)", "12", "F(4,5)"), ("eq", "30*F(9,10) - 30*F(4,5)", "3"),
                    ("true", "30*F(9,10) > 30*F(4,5)"),
                    ("true", "F(9,10) - F(4,5) == F(1,10) and F(1,10) != 3"),
                    ("true", "30*F(9,10) - F(96,10) == F(174,10) and F(174,10) != 3"))),
        dict(text=["Bus A, with 40 seats, goes 135 miles in 3 hours.", "Bus B goes 240 miles in 5 hours.",
                   "**Which bus is faster?"],
             unneeded="40",
             steps=["Bus A:  $135 \\div 3 = 45$", "Bus B:  $240 \\div 5 = 48$", "Compare:  $48 > 45$"],
             answer="Bus B: 48 miles per hour against 45",
             check=("many", rate("135", "3", "45"), rate("240", "5", "48"), ("true", "48 > 45")),
             wrong="Bus B — 240 miles against 135, the totals compared [Notes I: make both say y for each 1 of x]; 135 ÷ 40 — the seats used [ruling 22: the extra number]"),
        # figwords_ok: 24 feet is past the grid's edge on purpose (the plan's board 8).
        dict(figwords_ok=True, text=["The graph shows an elevator rising. The grid ends at 10 feet.",
                   "**At this rate, how many seconds does it take to rise 24 feet?"],
             qtext="The graph shows how far an elevator rises, feet against seconds, through (3, 8); the grid ends at 10 feet. At this rate, how many seconds does it take to rise 24 feet?",
             fig=BP((0, 6), (0, 10), **LIFT), fig_a=BPA((0, 6), (0, 10), **LIFT),
             steps=["Constant:  $8 \\div 3 = \\frac{8}{3}$  feet per second", "Equation:  $h = \\frac{8}{3}t$",
                    "Solve:  $24 = \\frac{8}{3}t$,  so  $t = 9$"],
             answer="9 seconds",
             check=("many", rate("8", "3", "F(8,3)"), ("eq", "24 / F(8,3)", "9"),
                    ("true", "sp.solve(sp.Eq(24, F(8,3)*" + X + "), " + X + ") == [9]")),
             wrong="64 — 24 times 8/3, multiplied instead of divided [Florida B1G-M, AR.4.2: the ratio in the wrong order]; 'cannot tell' — the grid's edge taken as the end of the line [Example 2: past the grid's edge]"),
        dict(kind="written", text=["Kim says the line for  $y = 0.6x$  is steeper than the line for  $y = \\frac{3}{4}x$,",
                                   "because 6 is greater than 3.", "**Is Kim right? Explain."],
             qtext="Kim says the line for y = 0.6x is steeper than the line for y = (3/4)x, because 6 is greater than 3. Is Kim right? Explain.",
             steps=["Write both as decimals:  $\\frac{3}{4} = 0.75$", "Compare:  $0.6 < 0.75$",
                    "both constants are positive: the greater, 0.75, gives the steeper line"],
             answer="No: 0.6 < 0.75, so y = (3/4)x is steeper.",
             check=("many", ("eq", "F(3,4)", "F(75,100)"), ("true", "F(6,10) < F(3,4)")),
             wrong="'yes' — the digits 6 and 3 compared, not the numbers 0.6 and 0.75 [Notes II: the greater positive constant gives the steeper line]"),
    ],

    # The six: a table against an equation (1); an equation against a description, then how much farther (2); two
    # lines on one grid (3); three constants in order (4); which is cheaper and by how much (5); a graph read, then a
    # value past its edge found backward (6). The pattern breaks at 4: no question to answer after the constants,
    # only their order.
    independent=[
        dict(stem="Store A's rope prices are in the table. Store B: $c = 0.8f$ (c dollars for f feet). Which store costs less per foot?",
             fig=figs.table([([4, 10], ["3.00", "7.50"])], head=("feet", "cost ($)"), cw=1.9, titles=["Store A"], inches=2.6),
             answer="Store A: \\$0.75 per foot against \\$0.80",
             why="Store A: 3.00 ÷ 4 = 0.75 and 7.50 ÷ 10 = 0.75, \\$0.75 per foot. Store B: \\$0.80 per foot. 0.75 < 0.80.",
             check=("many", rate("3", "4", "F(3,4)"), rate("F(750,100)", "10", "F(3,4)"), ("true", "F(3,4) < F(4,5)")),
             space=0.5),
        dict(stem="Car A goes $d = 62t$ miles in t hours. Car B goes 174 miles in 3 hours. After 6 hours, how much farther has the faster car gone?",
             answer="24 miles (Car A)",
             why="Car B: 174 ÷ 3 = 58 miles per hour; Car A: 62. In 6 hours: 62(6) = 372 and 58(6) = 348; 372 − 348 = 24.",
             check=("many", rate("174", "3", "58"), ("eq", "62*6 - 58*6", "24")), space=0.6),
        dict(stem="Lines A and B show two cyclists' miles against hours. Which cyclist is faster, and by how many miles per hour?",
             fig=figs.plane((0, 6), (0, 60), lines=[figs.prop(15, "A"), figs.prop(10, "B")], ys=10,
                            xname="hours", yname="miles", points=[(2, 30, None, "ul"), (3, 30, None, "dr")], inches=3.2),
             answer="A, by 5 miles per hour",
             why="A: 30 ÷ 2 = 15 miles per hour. B: 30 ÷ 3 = 10 miles per hour. 15 − 10 = 5.",
             check=("many", rate("30", "2", "15"), rate("30", "3", "10"), ("eq", "15 - 10", "5")), space=0.5),
        dict(stem="Put the constants of proportionality in order, least to greatest. A: $y = 1.2x$. B: y is 4 when x is 5. C: y is 9 when x is 6.",
             answer="B (0.8), A (1.2), C (1.5)",
             why="A: 1.2. B: 4 ÷ 5 = 0.8. C: 9 ÷ 6 = 1.5. 0.8 < 1.2 < 1.5.",
             check=("many", rate("4", "5", "F(4,5)"), rate("9", "6", "F(3,2)"), ("true", "F(4,5) < F(6,5) < F(3,2)")),
             space=0.5),
        dict(stem="Shop F sells 8 markers for \\$6.00. Shop G sells markers for \\$0.80 each. Which shop is cheaper for 25 markers, and by how much?",
             answer="Shop F, by \\$1.25",
             why="Shop F: 6.00 ÷ 8 = 0.75, \\$0.75 per marker. 25 markers: 0.75(25) = 18.75 and 0.80(25) = 20.00; 20.00 − 18.75 = 1.25.",
             check=("many", rate("6", "8", "F(3,4)"), ("eq", "F(4,5)*25 - F(3,4)*25", "F(5,4)")), space=0.6),
        # figwords_ok: 9 kilometers is past the grid's edge on purpose.
        dict(figwords_ok=True, stem="Kayla walks at a steady rate; the graph shows her kilometers against minutes. At this rate, how many minutes does she take to walk 9 kilometers?",
             fig=figs.plane((0, 40), (0, 4), lines=[figs.prop(Fr(1, 10), "")], xs=5, xname="minutes", yname="kilometers",
                            points=[(10, 1, "on"), (20, 2, "on"), (30, 3, "on")], inches=3.2),
             answer="90 minutes",
             why="1 ÷ 10 = 0.1 kilometer per minute, so d = 0.1t; 9 = 0.1t, so t = 9 ÷ 0.1 = 90.",
             check=("many", rate("1", "10", "F(1,10)"), rate("2", "20", "F(1,10)"), rate("3", "30", "F(1,10)"),
                    ("eq", "9 / F(1,10)", "90"), ("true", "sp.solve(sp.Eq(9, F(1,10)*" + X + "), " + X + ") == [90]")), space=0.5),
    ],

    bank=[
        dict(heading="Compare the constants."),
        dict(stem="Store A's prices are in the table. Store B charges $c = 1.5w$ dollars for w pounds. Which store costs less per pound?",
             fig=figs.table([([3, 6], ["4.20", "8.40"])], head=("pounds", "cost ($)"), cw=1.9, titles=["Store A"], inches=2.6),
             answer="Store A: \\$1.40 per pound against \\$1.50",
             why="Store A: 4.20 ÷ 3 = 1.40 and 8.40 ÷ 6 = 1.40. Store B: 1.50. 1.40 < 1.50.",
             check=("many", rate("F(420,100)", "3", "F(7,5)"), rate("F(840,100)", "6", "F(7,5)"), ("true", "F(7,5) < F(3,2)")),
             space=0.5),
        # figwords_ok: 9 miles in 4 hours is Walker B, who is not on the graph: the comparison is the point.
        dict(figwords_ok=True, stem="Walker A's graph shows miles against hours. Walker B walks 9 miles in 4 hours. Who walks faster?",
             fig=figs.plane((0, 6), (0, 16), lines=[figs.prop(Fr(5, 2), "")], ys=2, xname="hours", yname="miles",
                            points=[(4, 10, "on")], inches=2.6),
             answer="Walker A: 2.5 miles per hour against 2.25",
             why="Walker A: 10 ÷ 4 = 2.5. Walker B: 9 ÷ 4 = 2.25. 2.5 > 2.25.",
             check=("many", rate("10", "4", "F(5,2)"), rate("9", "4", "F(9,4)"), ("true", "F(5,2) > F(9,4)")), space=0.5),
        dict(stem="Lines A and B show what two workers earn, dollars against hours. Who earns more each hour, and how much more?",
             fig=figs.plane((0, 6), (0, 60), lines=[figs.prop(12, "A"), figs.prop(10, "B")], ys=10, xname="hours",
                            yname="dollars", points=[(5, 60, None, "l"), (5, 50, None, "r")], inches=2.6),
             answer="A, \\$2.00 more each hour",
             why="A: 60 ÷ 5 = 12. B: 50 ÷ 5 = 10. 12 − 10 = 2.",
             check=("many", rate("60", "5", "12"), rate("50", "5", "10"), ("eq", "12 - 10", "2")), space=0.5),
        dict(heading="Put them in order."),
        dict(stem="Order the constants of proportionality from least to greatest:  $y = 0.7x$,  $y = \\frac{2}{3}x$,  $y = 0.65x$.",
             answer="0.65, 2/3, 0.7",
             why="2/3 = 0.666…, between 0.65 and 0.7.",
             check=("true", "F(65,100) < F(2,3) < F(7,10)"), space=0.4),
        dict(stem="On the same axes, which line is steeper: $y = 0.9x$ or $y = \\frac{7}{8}x$?",
             answer="y = 0.9x",
             why="7/8 = 0.875, and 0.9 > 0.875. On the same axes, the greater positive constant gives the steeper line.",
             check=("many", ("eq", "F(7,8)", "F(875,1000)"), ("true", "F(9,10) > F(7,8)")), space=0.4),
        dict(heading="Solve the problem."),
        dict(stem="Store F sells 6 notebooks for \\$10.50. Store G sells notebooks for \\$1.95 each. Which store is cheaper for 20 notebooks, and by how much?",
             answer="Store F, by \\$4.00",
             why="Store F: 10.50 ÷ 6 = 1.75, \\$1.75 per notebook. 20 notebooks: 1.75(20) = 35.00 and 1.95(20) = 39.00; 39.00 − 35.00 = 4.00.",
             check=("many", rate("F(1050,100)", "6", "F(7,4)"), ("eq", "F(195,100)*20 - F(7,4)*20", "4")), space=0.6),
        dict(stem="Boat A goes $d = 14t$ miles in t hours. Boat B goes 33 miles in 3 hours. After 5 hours, how much farther has the faster boat gone?",
             answer="15 miles (Boat A)",
             why="Boat B: 33 ÷ 3 = 11. In 5 hours: 14(5) = 70 and 11(5) = 55; 70 − 55 = 15.",
             check=("many", rate("33", "3", "11"), ("eq", "14*5 - 11*5", "15")), space=0.6),
        dict(stem="A hose fills a tank at a steady rate; the graph shows gallons against minutes. At this rate, how many minutes to fill 60 gallons?",
             fig=figs.plane((0, 5), (0, 20), lines=[figs.prop(4, "")], ys=4, xname="minutes", yname="gallons",
                            points=[(3, 12, "on")], inches=2.6),
             answer="15 minutes",
             why="12 ÷ 3 = 4 gallons per minute; 60 ÷ 4 = 15.",
             check=("many", rate("12", "3", "4"), ("eq", "60 / 4", "15")), space=0.5),
        dict(stem="A baker uses 5 cups of flour for every 2 loaves. How many cups for 7 loaves?",
             answer="17.5 cups",
             why="5 ÷ 2 = 2.5 cups per loaf; 2.5(7) = 17.5.",
             check=("many", rate("5", "2", "F(5,2)"), ("eq", "F(5,2)*7", "F(35,2)")), space=0.5),
        dict(heading="Choose one."),
        dict(stem="Four stores sell coffee beans. Which price is the least per pound?",
             choices=["\\$1.00 buys 0.4 pound", "6 pounds for \\$15.30", "2 pounds for \\$5.20", "\\$2.40 a pound"],
             correct=3, answer="D",
             why="Per pound: A 1.00 ÷ 0.4 = 2.50; B 15.30 ÷ 6 = 2.55; C 5.20 ÷ 2 = 2.60; D 2.40. The least is D.",
             check=("many", ("true", "F(240,100) < 1/F(4,10)"), ("true", "F(240,100) < F(520,100)/2"),
                    ("true", "F(240,100) < F(1530,100)/6"), ("eq", "1/F(4,10)", "F(5,2)")),
             errors={"A": "0.4 pound per dollar read as dollars per pound: the ratio in the wrong order [Florida B1G-M, AR.4.2: the ratio in the wrong order]", "B": "the biggest bag taken as the cheapest per pound [Notes I: make both say y for each 1 of x]", "C": "the least total price taken as the least per pound [Notes I: make both say y for each 1 of x]"}),
        dict(stem="Plan R: \\$1.20 a ride. Plan S: 10 rides for \\$10.00. Which is cheaper for 25 rides, and by how much?",
             choices=["R, by \\$5.00", "S, by \\$5.00", "S, by \\$20.00", "S, by \\$0.20"],
             correct=1, answer="B",
             why="Plan S: 10.00 ÷ 10 = 1.00, \\$1.00 per ride. 25 rides: 1.20(25) = 30.00 and 1.00(25) = 25.00; S, by 5.00.",
             check=("many", ("eq", "F(6,5)*25 - 1*25", "5"), ("true", "F(6,5)*25 > 25"),
                    ("true", "F(6,5) - 1 == F(1,5) and F(1,5) != 5"),
                    ("true", "F(6,5)*25 - 10 == 20 and 20 != 5")),
             errors={"A": "the plans compared backwards: the higher cost taken as cheaper [Notes III: then answer the question asked]", "C": "25 rides on Plan R against the price of 10 on Plan S: 30.00 − 10.00 [Notes I: make both say y for each 1 of x]", "D": "the difference for one ride, 1.20 − 1.00 [Notes III: then answer the question asked]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the relationships whose constant of proportionality is greater than 4.",
             choices=["y is 20 when x is 5", "$y = \\frac{15}{4}x$", "$y = 4.5x$", "y is 2 when x is 10", "y is 27 when x is 6"],
             correct=[2, 4], answer="C, E",
             why="A: 20 ÷ 5 = 4, not greater than 4. B: 15/4 = 3.75. C: 4.5. D: 2 ÷ 10 = 0.2. E: 27 ÷ 6 = 4.5. Greater than 4: C and E.",
             check=("many", ("true", "F(9,2) > 4"), ("true", "F(27,6) > 4"), ("true", "(F(15,4) > 4) != True"),
                    ("true", "(F(20,5) > 4) != True"), ("true", "(F(2,10) > 4) != True")),
             errors={"A": "4 counted as greater than 4 [MA.7.AR.4.5: the comparison asked]", "B": "the 15 of 15/4 read as the constant [Notes I: make both say y for each 1 of x]", "D": "10 ÷ 2 = 5, x ÷ y: the ratio in the wrong order [Florida B1G-M, AR.4.2: the ratio in the wrong order]"}),
    ],

    additional=[
        dict(heading="Compare the constants."),
        dict(stem="Store A's prices are in the table. Store B charges $c = 1.7w$ dollars for w pounds. Which store costs less per pound?",
             fig=figs.table([([2, 5], ["3.60", "9.00"])], head=("pounds", "cost ($)"), cw=1.9, titles=["Store A"], inches=2.6),
             answer="Store B: \\$1.70 per pound against \\$1.80",
             why="Store A: 3.60 ÷ 2 = 1.80 and 9.00 ÷ 5 = 1.80. Store B: 1.70. 1.70 < 1.80.",
             check=("many", rate("F(360,100)", "2", "F(9,5)"), rate("9", "5", "F(9,5)"), ("true", "F(17,10) < F(9,5)")),
             space=0.5),
        # figwords_ok: 13 miles in 4 hours is Walker B, who is not on the graph: the comparison is the point.
        dict(figwords_ok=True, stem="Walker A's graph shows miles against hours. Walker B walks 13 miles in 4 hours. Who walks faster?",
             fig=figs.plane((0, 6), (0, 20), lines=[figs.prop(Fr(7, 2), "")], ys=2, xname="hours", yname="miles",
                            points=[(4, 14, "on")], inches=2.6),
             answer="Walker A: 3.5 miles per hour against 3.25",
             why="Walker A: 14 ÷ 4 = 3.5. Walker B: 13 ÷ 4 = 3.25. 3.5 > 3.25.",
             check=("many", rate("14", "4", "F(7,2)"), rate("13", "4", "F(13,4)"), ("true", "F(7,2) > F(13,4)")), space=0.5),
        dict(stem="Lines A and B show what two workers earn, dollars against hours. Who earns more each hour, and how much more?",
             fig=figs.plane((0, 6), (0, 50), lines=[figs.prop(8, "A"), figs.prop(9, "B")], ys=5, xname="hours",
                            yname="dollars", points=[(5, 40, None, "r"), (5, 45, None, "l")], inches=2.6),
             answer="B, \\$1.00 more each hour",
             why="A: 40 ÷ 5 = 8. B: 45 ÷ 5 = 9. 9 − 8 = 1.",
             check=("many", rate("40", "5", "8"), rate("45", "5", "9"), ("eq", "9 - 8", "1")), space=0.5),
        dict(heading="Put them in order."),
        dict(stem="Order the constants of proportionality from least to greatest:  $y = 0.8x$,  $y = \\frac{3}{4}x$,  $y = 0.78x$.",
             answer="3/4, 0.78, 0.8",
             why="3/4 = 0.75, less than 0.78, which is less than 0.8.",
             check=("true", "F(3,4) < F(78,100) < F(8,10)"), space=0.4),
        dict(stem="On the same axes, which line is steeper:  $y = 2.4x$  or  $y = \\frac{5}{2}x$?",
             answer="y = (5/2)x",
             why="5/2 = 2.5, and 2.5 > 2.4. On the same axes, the greater positive constant gives the steeper line.",
             check=("many", ("eq", "F(5,2)", "F(25,10)"), ("true", "F(5,2) > F(24,10)")), space=0.4),
        dict(heading="Solve the problem."),
        dict(stem="Store F sells 4 folders for \\$3.40. Store G sells folders for \\$0.90 each. Which store is cheaper for 30 folders, and by how much?",
             answer="Store F, by \\$1.50",
             why="Store F: 3.40 ÷ 4 = 0.85, \\$0.85 per folder. 30 folders: 0.85(30) = 25.50 and 0.90(30) = 27.00; 27.00 − 25.50 = 1.50.",
             check=("many", rate("F(340,100)", "4", "F(17,20)"), ("eq", "F(9,10)*30 - F(17,20)*30", "F(3,2)")), space=0.6),
        dict(stem="Boat A goes $d = 16t$ miles in t hours. Boat B goes 39 miles in 3 hours. After 4 hours, how much farther has the faster boat gone?",
             answer="12 miles (Boat A)",
             why="Boat B: 39 ÷ 3 = 13. In 4 hours: 16(4) = 64 and 13(4) = 52; 64 − 52 = 12.",
             check=("many", rate("39", "3", "13"), ("eq", "16*4 - 13*4", "12")), space=0.6),
        dict(stem="A hose fills a tank at a steady rate; the graph shows gallons against minutes. At this rate, how many minutes to fill 80 gallons?",
             fig=figs.plane((0, 5), (0, 25), lines=[figs.prop(5, "")], ys=5, xname="minutes", yname="gallons",
                            points=[(2, 10, "on")], inches=2.6),
             answer="16 minutes",
             why="10 ÷ 2 = 5 gallons per minute; 80 ÷ 5 = 16.",
             check=("many", rate("10", "2", "5"), ("eq", "80 / 5", "16")), space=0.5),
        dict(stem="A baker uses 4 cups of flour for every 3 loaves. How many cups for 9 loaves?",
             answer="12 cups",
             why="4 ÷ 3 = 4/3 cups per loaf; (4/3)(9) = 12.",
             check=("many", rate("4", "3", "F(4,3)"), ("eq", "F(4,3)*9", "12")), space=0.5),
        dict(heading="Choose one."),
        dict(stem="Four stores sell coffee beans. Which price is the least per pound?",
             choices=["2 pounds for \\$6.40", "\\$1.00 buys 0.3 pound", "8 pounds for \\$25.20", "\\$3.10 a pound"],
             correct=3, answer="D",
             why="Per pound: A 6.40 ÷ 2 = 3.20; B 1.00 ÷ 0.3 = 3.33…; C 25.20 ÷ 8 = 3.15; D 3.10. The least is D.",
             check=("many", ("true", "F(310,100) < 1/F(3,10)"), ("true", "F(310,100) < F(640,100)/2"),
                    ("true", "F(310,100) < F(2520,100)/8"), ("eq", "F(2520,100)/8", "F(315,100)")),
             errors={"A": "the least total price taken as the least per pound [Notes I: make both say y for each 1 of x]", "B": "0.3 pound per dollar read as dollars per pound: the ratio in the wrong order [Florida B1G-M, AR.4.2: the ratio in the wrong order]", "C": "the biggest bag taken as the cheapest per pound [Notes I: make both say y for each 1 of x]"}),
        dict(stem="Plan R: \\$1.50 a ride. Plan S: 8 rides for \\$10.00. Which is cheaper for 24 rides, and by how much?",
             choices=["S, by \\$6.00", "S, by \\$0.25", "R, by \\$6.00", "S, by \\$26.00"],
             correct=0, answer="A",
             why="Plan S: 10.00 ÷ 8 = 1.25, \\$1.25 per ride. 24 rides: 1.50(24) = 36.00 and 1.25(24) = 30.00; S, by 6.00.",
             check=("many", ("eq", "F(3,2)*24 - F(5,4)*24", "6"), ("true", "F(3,2)*24 > F(5,4)*24"),
                    ("true", "F(3,2) - F(5,4) == F(1,4) and F(1,4) != 6"),
                    ("true", "F(3,2)*24 - 10 == 26 and 26 != 6")),
             errors={"B": "the difference for one ride, 1.50 − 1.25 [Notes III: then answer the question asked]", "C": "the plans compared backwards: the higher cost taken as cheaper [Notes III: then answer the question asked]", "D": "24 rides on Plan R against the price of 8 on Plan S: 36.00 − 10.00 [Notes I: make both say y for each 1 of x]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the relationships whose constant of proportionality is greater than 3.",
             choices=["y is 12 when x is 4", "y is 26 when x is 8", "y is 2 when x is 8", "$y = 3.5x$", "$y = \\frac{10}{4}x$"],
             correct=[1, 3], answer="B, D",
             why="A: 12 ÷ 4 = 3, not greater than 3. B: 26 ÷ 8 = 3.25. C: 2 ÷ 8 = 0.25. D: 3.5. E: 10/4 = 2.5. Greater than 3: B and D.",
             check=("many", ("true", "F(26,8) > 3"), ("true", "F(7,2) > 3"), ("true", "(F(10,4) > 3) != True"),
                    ("true", "(F(12,4) > 3) != True"), ("true", "(F(2,8) > 3) != True")),
             errors={"A": "3 counted as greater than 3 [MA.7.AR.4.5: the comparison asked]", "C": "8 ÷ 2 = 4, x ÷ y: the ratio in the wrong order [Florida B1G-M, AR.4.2: the ratio in the wrong order]", "E": "the 10 of 10/4 read as the constant [Notes I: make both say y for each 1 of x]"}),
    ],

    te=dict(
        must="Any real-world proportional problem, including a comparison of two relationships and a graph-and-read item (AR.4.5, May ask).",
        must_not="Non-proportional (fee + rate) situations as if proportional — those are NSO.2.3 / AR.2.2 items (AR.4.5, Must not ask).",
        read_first=[
            "The last teaching day of Unit 7 (Tue 12 Jan, 53 minutes). Built from the benchmark first (the unit's Lesson Outlines, §7.07, standing decisions 1–4 and 6): every comparison brings both relationships to y for each 1 of x, then answers the question the story asked. No new term: no vocabulary slide.",
            "Example 2 and board 8 go past the grid's edge: the constant is read from one marked point and the answer found by dividing. 'Slope' is on no slide; a steeper line is 'more y for each 1 of x'.",
            "The test's AR.4.5 items (14 and 15: trains, a pump in liters) are not used; Example 1's pumps are in gallons."],
        materials="Whiteboards and markers. The Independent Set, one per student. The Unit Review goes home today; tomorrow, Wed 13 Jan, is a spiral day (no deck), and the unit test is Thu 14 Jan, one period.",
        variation="Boards 1–2 are a table against an equation, and only the equation changes, so the verdict flips. 3 votes on two lines on one grid (the slower line drawn longer and lower). 4 is a description against a graph; 5 reads three constants off one grid and orders them. 6 votes on cheaper-and-by-how-much; 7 is two descriptions with the seats as the extra number; 8 reads a graph and goes past its edge; 9 is Kim's digits claim, written. The independent set: a table against an equation, an equation against a description and how much farther, two lines on one grid, three constants in order (the pattern breaks: no question after the order), which is cheaper and by how much, and a graph read past its edge.",
        audit=["Every constant re-derived by sympy at build time as y ÷ x from the printed values, every row of every table checked, every comparison and every 'how much more' recomputed; every multiple-choice distractor re-derived from its named error; every graph drawn from y = px by u7/figs7.py, which refuses a marked point that is not on its line."],
        changes=["Independent Set question 2: Car A is given as the equation d = 62t, not a graph — 62 miles an hour cannot sit on a grid corner at the unit's scales (2, 4, 5, 10, 20)."],
    ),
)
