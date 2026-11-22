# A7 Unit 7 — Representing Proportional Relationships: Reference Sheet, Unit Review (home Tue 12 Jan with 7.07; A7
# has no review day) and the assessment as THE PRACTICE TEST ALONE (ruling 49): the unit test is a random set of the
# practice page, so this paper is the test's blueprint — its fifteen questions in this order with these points are
# what the page generates with new numbers and what the master sheet maps. One period (ruling 51; Thu 14 Jan):
# 15 questions, 20 points, sections by benchmark in teaching order AR.4.3 · AR.4.2 · AR.4.1 · MA.8.AR.3.1 · AR.4.4 ·
# AR.4.5, tracker 4 · 4 · 3 · 1 · 5 · 3 — exactly the outline's "The test" (reviewed 20–21 Nov). No transfer items
# and no Form A/B.
#
# The unit's standing decisions hold on every page: one definition (one is always the same number times the other:
# y = px), p the constant of proportionality; the three tests in the unit's words (y ÷ x the same for every pair; a
# straight line through the origin; nothing added at the start) and, from 7.04, the equation's (y = px, nothing
# added); which quantity is y is said in every item; no cross products; no "slope" and no "y-intercept" on any page;
# a context is drawn in Quadrant I; where a question shows several graphs they share one set of axes and scales.
#
# Numbers: the practice paper's are the outline's own (its stories and relationships are reserved for it). The
# review and the reference sheet use their own — none of the paper's and none a lesson shows — read against every
# number of the outline's lessons before they were written. The review's constants: 3.6, 7/4, 7.2, 2.8, 3/8, −3.5,
# 5.2, 1.8, 4.6, 1.25, 4.8, 6.8 and 9.6 (with 10.5 against it); the rulings of 21 Nov add 1.5 and 4/3 (the two
# picture-choice questions in the paper's shapes, numbers the lead set), 10 (the bag of ice) and 9 (y = 9x − 4).
#
# Every check is sympy over exact rationals: a ratio y ÷ x is compared row by row (ratios), a table is the equation's
# value at every x (table_of), and a wrong option is held to be NOT the key by its own "!=" clause.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs7 as figs          # its own name: every unit's gates run in one process

BLANK = figs.BLANK


def _q(v):
    """A number as a sympy-ready exact string: F('27.20'), F(7,4), or an integer."""
    if isinstance(v, Fr):
        return f"F({v.numerator},{v.denominator})"
    return f"F('{v}')"


def ratios(xs, ys, p):
    """y ÷ x is p for every pair."""
    return ("many",) + tuple(("eq", f"{_q(y)}/{_q(x)}", _q(p)) for x, y in zip(xs, ys))


def table_of(p, xs, ys):
    """Each y of a table is p times its x (y = px)."""
    return ("many",) + tuple(("eq", f"{_q(p)}*{_q(x)}", _q(y)) for x, y in zip(xs, ys))


def stack(specs, gap=2.6, titles=None, inches=4.6, pt=9.5):
    """Figures of figs7 set one above another as ONE picture (the kit prints one figure per item), each centred
    across, `gap` grid units apart — a table over its grid (question 1), two tables over two graphs (question 7).
    `titles` (one per figure, or None) print above each."""
    sh, top = [], 0.0
    for k, s in enumerate(specs):
        x0, x1, y0, y1 = figs._extent(s["shapes"])
        if titles and titles[k]:
            sh.append(figs._t(0, top, titles[k], va="bottom", off=(0, 0.3)))
            top -= 1.6
        dx, dy = -(x0 + x1) / 2.0, top - y1
        for e in s["shapes"]:
            e = dict(e)
            if e["t"] == "seg":
                e["a"] = (e["a"][0] + dx, e["a"][1] + dy); e["b"] = (e["b"][0] + dx, e["b"][1] + dy)
            elif e["t"] == "circle":
                e["c"] = (e["c"][0] + dx, e["c"][1] + dy)
            elif e["t"] == "text":
                e["xy"] = (e["xy"][0] + dx, e["xy"][1] + dy)
            sh.append(e)
        top -= (y1 - y0) + gap
    return dict(kind="shapes", fs=22, pt=pt, **{"in": inches}, shapes=sh)


# ------------------------------------------------------------------ the practice paper's figures
# question 1: the table to complete over the grid to draw on (yards 0 to 8 by 1, cost 0 to 20 by 5); the key's copy
# fills the table and draws the points and the line from the origin through (6, 15)
Q1_GRID, Q1_DRAWN = figs.pair((0, 8), (0, 20), lines=[figs.prop(Fr(5, 2), "")],
                              points=[(2, 5, ""), (4, 10, ""), (6, 15, "")],
                              ys=5, xname="yards", yname="cost in dollars", inches=3.2)
Q1_IN = 7.2       # the grid at least 3.5 in wide on the page (ruling 6, 21 Nov): the picture is the table's width, 11.5 units, the grid 8
Q1_T = figs.table([([0, 2, 4, 6], [BLANK, BLANK, "10.00", BLANK])], head=("yards", "cost ($)"), cw=2.0)
Q1_TK = figs.table([([0, 2, 4, 6], ["0.00", "5.00", "10.00", "15.00"])], head=("yards", "cost ($)"), cw=2.0)
Q1_FIG = stack([Q1_T, Q1_GRID], inches=Q1_IN)
Q1_KEY = stack([Q1_TK, Q1_DRAWN], inches=Q1_IN)

# question 2: four graphs on the same axes, the d-axis scaled by 0.5 (decision 6): the axes swapped (d = 2t), the
# scale ignored (half a square for each second: d = 0.25t), 0.5 read as a start (d = t + 0.5), and the key
_g2 = dict(ys=Fr(1, 2), xname="t", yname="d", xstep=2, ystep=1)
Q2_FIG = figs.row([figs.plane((0, 6), (0, 3), lines=[figs.prop(2, "")], **_g2),
                   figs.plane((0, 6), (0, 3), lines=[figs.prop(Fr(1, 4), "")], **_g2),
                   figs.plane((0, 6), (0, 3), lines=[(1, Fr(1, 2), "")], **_g2),
                   figs.plane((0, 6), (0, 3), lines=[figs.prop(Fr(1, 2), "")], **_g2)],
                  gap=2.4, titles=["A", "B", "C", "D"], inches=7.2)   # at gap 3 and 6.8 in each grid printed 1 in wide; at gap 1.5 one graph's t stood against the next one's 0

# question 3: four lines through the origin on one grid, lettered
Q3_FIG = figs.plane((0, 6), (0, 6), lines=[figs.prop(3, "A"), figs.prop(Fr(3, 2), "B"), figs.prop(Fr(2, 3), "C"),
                                           figs.prop(1, "D")],
                    xname="time in seconds", yname="distance in meters", inches=3.0)

Q4_FIG = figs.table([([4, 6, 10, 16], [14, 21, 35, 56])], head=("minutes", "pages"))

# question 5: the pounds axis scaled by 5 and the cost axis by 3
Q5_FIG = figs.plane((0, 25), (0, 15), lines=[figs.prop(Fr(3, 5), "")], points=[(5, 3, ""), (10, 6, "")], xs=5, ys=3,
                    xname="pounds of apples", yname="cost in dollars", inches=3.0)

Q6_FIG = figs.table([([-6, -2, 4, 10], [9, 3, -6, -15])])

# question 7: tables A and B over graphs C and D (one set of axes and scales for both graphs)
Q7_TABLES = figs.table([([2, 4, 6, 8], [11, 22, 33, 44]), ([1, 2, 3, 4], [4, 6, 8, 10])], titles=["A", "B"])
Q7_GRAPHS = figs.row([figs.plane((0, 10), (0, 5), lines=[figs.prop(Fr(1, 5), "")], points=[(5, 1, ""), (10, 2, "")]),
                      figs.plane((0, 10), (0, 5), lines=[(1, 2, "")], points=[(2, 4, ""), (3, 5, "")])],
                     gap=3.0, titles=["C", "D"])
Q7_FIG = stack([Q7_TABLES, Q7_GRAPHS], gap=3.4, inches=6.4)

Q8_FIG = figs.table([([2, 5, 8, 10], ["6.40", "16.00", "27.20", "32.00"])], head=("gallons", "cost ($)"))

# question 9: two parallel lines, A through the origin with (2, 6) marked, B from (0, 2) with (2, 8) marked
Q9_FIG = figs.plane((0, 4), (0, 14), lines=[figs.prop(3, "A"), (3, 2, "B")], ys=2, points=[(2, 6, None, "dr"), (2, 8, None, "ul")],
                    inches=3.0)

Q10_FIG = figs.table([([2, 3, 6, 8], ["17.00", "25.50", "51.00", "68.00"])], head=("tickets, n", "cost, c ($)"))

# question 11: the benchmark's own example, (5, 2) and (10, 4)
Q11_FIG = figs.plane((0, 10), (0, 5), lines=[figs.prop(Fr(2, 5), "")], points=[(5, 2, "on"), (10, 4, "on")],
                     inches=3.2)

Q13_FIG = figs.table([([2, 5, BLANK], [BLANK, BLANK, 83])], head=("gallons, g", "pounds, w"))

# question 14: Train A's table beside Train B's graph (miles against hours, the miles axis scaled by 30)
Q14_FIG = figs.row([figs.table([([2, 3, 5], [130, 195, 325])], head=("hours", "miles")),
                    figs.plane((0, 4), (0, 240), lines=[figs.prop(60, "")], points=[(1, 60, ""), (2, 120, ""), (3, 180, "")],
                               ys=30, ystep=2, xname="hours", yname="miles")],
                   gap=4.0, titles=["Train A", "Train B"], inches=5.6)

# question 15: the grid runs to 12 minutes and 15 liters; 30 liters is past its edge
Q15_FIG = figs.plane((0, 12), (0, 15), lines=[figs.prop(Fr(5, 4), "")], points=[(4, 5, ""), (8, 10, "")],
                     xname="minutes", yname="liters", inches=3.2)


def _ar43():
    q1 = dict(stem="Fabric costs the same amount per yard, and 4 yards cost \\$10.00.",
              fig=Q1_FIG, fig_key=Q1_KEY,
              parts=[dict(label="a", stem="Complete the table.", answer="\\$0.00,  \\$5.00,  \\$15.00",
                          why="One point: all three. 10.00 ÷ 4 = 2.50 dollars per yard. 2.50(0) = 0.00, 2.50(2) = 5.00, 2.50(6) = 15.00.",
                          check=("many", ("eq", "F('10.00')/4", "F('2.50')"), table_of(Fr(5, 2), [0, 2, 4, 6], ["0.00", "5.00", "10.00", "15.00"])),
                          space=0.2),
                     dict(label="b", stem="Graph the relationship on the grid.",
                          answer="The points (0, 0), (2, 5), (4, 10) and (6, 15), and the line from the origin through them",
                          why="One point: a straight line from (0, 0) through (6, 15); plotted points are optional when the line passes through them. Read the scales first: the cost axis counts by 5. A line that misses the origin earns no point, and neither do points plotted as if each square were \\$1.",
                          check=table_of(Fr(5, 2), [0, 2, 4, 6], [0, 5, 10, 15]), space=0.3)])
    q2 = dict(stem="The equation  $d = 0.5t$  gives the distance d, in centimeters, that a ladybug crawls in t seconds. Which graph shows the relationship?",
              fig=Q2_FIG, choices=["Graph A", "Graph B", "Graph C", "Graph D"], correct=3, answer="D", space=0.3,
              errors={"A": "the axes swapped: its line is d = 2t, through (1, 2) [B1G-M, MA.7.AR.4.3: the ratio taken in the wrong order]",
                      "B": "the scale ignored: half a square up for each second is d = 0.25t, through (2, 0.5) and (4, 1) [B1G-M, MA.7.AR.4.3: the axis scale misread]",
                      "C": "0.5 read as a start and t as the rate: d = t + 0.5, through (0, 0.5) and (1, 1.5) [B1G-M, MA.7.AR.4.3: the constant read as a start]"},
              why="Read the scales first: each square up is 0.5 centimeters. d = 0.5t gives 0.5(2) = 1 and 0.5(4) = 2: the line through the origin, (2, 1) and (4, 2) is graph D. In grid squares graph B looks like 0.5 — half a square for each second — but its line is d = 0.25t.",
              check=("many", ("eq", "F(1,2)*2", "1"), ("eq", "F(1,2)*4", "2"),
                     ("true", "2*1 != F(1,2)*1"), ("true", "F(1,4)*4 != F(1,2)*4"), ("true", "F(1,2) != F(1,2)*0")))
    q3 = dict(stem="Four robots each move at a constant speed. The graph shows the distance each robot travels, in meters, versus the time, in seconds. Which line shows the robot that travels 3 meters every 2 seconds?",
              fig=Q3_FIG, choices=["Line A", "Line B", "Line C", "Line D"], correct=1, answer="B", space=0.3,
              errors={"A": "3 meters every 1 second: line A passes through (1, 3) [B1G-M, MA.7.AR.4.3: the rate read for 1 second]",
                      "C": "the ratio reversed: line C goes 2 meters every 3 seconds, through (3, 2) [B1G-M, MA.7.AR.4.3: the ratio taken in the wrong order]",
                      "D": "3 − 2 = 1 meter each second, subtracted: line D passes through (2, 2) [B1G-M, MA.7.AR.4.3: a difference taken for the rate]"},
              why="3 meters every 2 seconds is the point (2, 3), and line B passes through it (and through (4, 6)): 1.5 meters per second.",
              check=("many", ("eq", "F(3,2)*2", "3"), ("eq", "F(3,2)*4", "6"),
                     ("true", "3*2 != 3"), ("true", "F(2,3)*2 != 3"), ("true", "1*2 != 3")))
    return [q1, q2, q3]


def _ar42():
    q4 = dict(stem="Kai reads at a constant pace. The table shows how many pages he reads. What is the constant of proportionality, in pages per minute?",
              fig=Q4_FIG, answer="3.5 pages per minute   (3.5 or 7/2)",
              why="y ÷ x is the same for every pair: 14 ÷ 4 = 3.5, 21 ÷ 6 = 3.5, 35 ÷ 10 = 3.5, 56 ÷ 16 = 3.5. 4/14 = 2/7 divides minutes by pages (minutes per page).",
              check=ratios([4, 6, 10, 16], [14, 21, 35, 56], "3.5"), space=0.7)
    q5 = dict(stem="The graph shows the cost, in dollars, of apples versus their weight, in pounds.", fig=Q5_FIG,
              parts=[dict(label="a", stem="What is the constant of proportionality?", answer="0.6 dollars per pound   (accept 0.6, 3/5 or \\$0.60 per pound)",
                          why="Read the scales first: pounds count by 5 and dollars by 3. The line passes through (5, 3) and (10, 6): 3 ÷ 5 = 0.6 and 6 ÷ 10 = 0.6. 1 (squares counted) ignores the scales; 5/3 divides pounds by dollars.",
                          check=ratios([5, 10], [3, 6], "0.6"), space=0.5),
                     dict(label="b", stem="What does the constant of proportionality tell you?",
                          choices=["The cost before any apples are weighed", "The cost of each pound of apples",
                                   "The pounds of apples each dollar buys", "The cost of 5 pounds of apples"], correct=1,
                          answer="B",
                          errors={"A": "the constant read as a start: the line passes through the origin, so 0 pounds cost \\$0 [B1G-M, MA.7.AR.4.2: the constant read as a start]",
                                  "C": "reversed: each dollar buys 1 ÷ 0.6 = 5/3 pounds [B1G-M, MA.7.AR.4.2: the ratio taken in the wrong order]",
                                  "D": "a y-value read off as the constant: \\$3 is the cost of 5 pounds [B1G-M, MA.7.AR.4.2: a point's coordinate taken for the constant]"},
                          why="B. The constant of proportionality is the amount of y for every 1 unit of x: 0.60 dollars per pound. A reads it as a start (0 pounds cost \\$0); C reverses it (each dollar buys 5/3 pounds); D reads \\$3, the cost of 5 pounds.",
                          check=("many", ("eq", "F(3,5)*1", "F('0.60')"), ("true", "1/F(3,5) != F(3,5)"),
                                 ("true", "F(3,5)*0 != F('0.60')"), ("eq", "F(3,5)*5", "3"), ("true", "F(3,5)*5 != F(3,5)*1")))])
    q6 = dict(stem="A table is shown. y is proportional to x. What is the constant of proportionality?", fig=Q6_FIG,
              answer="−1.5   (−1.5 or −3/2)",
              why="y ÷ x for every pair: 9 ÷ (−6) = −1.5, 3 ÷ (−2) = −1.5, −6 ÷ 4 = −1.5, −15 ÷ 10 = −1.5. A constant can be negative. 1.5 loses the sign; −2/3 divides x by y.",
              check=ratios([-6, -2, 4, 10], [9, 3, -6, -15], "-1.5"), space=0.7)
    return [q4, q5, q6]


def _ar41():
    q7 = dict(stem="Select all the relationships that are proportional.", fig=Q7_FIG,
              choices=["Table A", "Table B", "Graph C", "Graph D",
                       "A plumber charges \\$40 to come to the house plus \\$55 per hour (total cost and number of hours).",
                       "A store sells pens for \\$0.85 each (total cost and number of pens)."],
              correct=[0, 2, 5], answer="A, C, F", space=0.3,
              errors={"B": "a constant difference taken for a constant ratio: y goes up 2 each time, but 4 ÷ 1 = 4 and 6 ÷ 2 = 3 [B1G-M, MA.7.AR.4.1: a constant increase taken for proportional]",
                      "D": "straight, but not through the origin: the line passes through (0, 2) [B1G-M, MA.7.AR.4.1: every straight line taken as proportional]",
                      "E": "a fee added at the start: 1 hour costs \\$95 and 2 hours \\$150, and 95 ÷ 1 is not 150 ÷ 2 [B1G-M, MA.7.AR.4.1: a start added]"},
              why="One point for exactly A, C and F. A: y ÷ x is 5.5 for every pair. C: a straight line through the origin, (5, 1) and (10, 2): 0.2 each time. F: the cost is 0.85 times the pens, nothing added at the start. B goes up by the same amount (4 ÷ 1 = 4, 6 ÷ 2 = 3); D passes through (0, 2); E adds a \\$40 fee.",
              check=("many", ratios([2, 4, 6, 8], [11, 22, 33, 44], "5.5"), ratios([5, 10], [1, 2], "0.2"),
                     ("true", "F(4,1) != F(6,2)"), ("true", "1*0 + 2 != 0"), ("true", "F(40 + 55*1, 1) != F(40 + 55*2, 2)"),
                     table_of(Fr(85, 100), [1, 2, 3], ["0.85", "1.70", "2.55"])))
    q8 = dict(stem="The table shows the cost of different amounts of gas.", fig=Q8_FIG,
              parts=[dict(label="a", stem="Is the cost proportional to the number of gallons?",
                          choices=["No. Cost ÷ gallons is not the same for every pair.", "Yes. The cost goes up as the gallons go up.",
                                   "Yes. 6.40 ÷ 2 = 3.20 and 16.00 ÷ 5 = 3.20.", "No. The table does not start at 0."], correct=0, answer="A",
                          errors={"B": "rising taken for proportional [B1G-M, MA.7.AR.4.1: a rising relationship taken for proportional]",
                                  "C": "only two pairs tested: 27.20 ÷ 8 = 3.40 is the pair that differs [B1G-M, MA.7.AR.4.1: not every pair tested]",
                                  "D": "the right answer for a wrong reason: a table does not have to show the pair (0, 0) [B1G-M, MA.7.AR.4.1: the origin taken as missing]"},
                          why="A. y ÷ x must be the same for every pair: 6.40 ÷ 2 = 3.20, 16.00 ÷ 5 = 3.20, 32.00 ÷ 10 = 3.20, but 27.20 ÷ 8 = 3.40. B takes rising for proportional; C tests two pairs; D says no, but its reason is not valid: a table does not have to show the pair (0, 0).",
                          check=("many", ratios([2, 5, 10], ["6.40", "16.00", "32.00"], "3.20"), ("true", "F('27.20')/8 != F('3.20')"))),
                     dict(label="b", stem="If the cost is not proportional, which cost would have to change, and what should it be? If it is proportional, write \"none\".",
                          answer="The cost of 8 gallons; \\$25.60",
                          why="One point: the cost that does not fit and what it should be. 27.20 ÷ 8 = 3.40 is the pair that differs. At 3.20 dollars per gallon, the other pairs' constant, 8 gallons cost 3.20(8) = 25.60.",
                          check=("many", ("true", "F('27.20')/8 != F('3.20')"), ("eq", "F('3.20')*8", "F('25.60')")), space=0.5)])
    return [q7, q8]


def _ar31():
    q9 = dict(stem="The graph shows two relationships, A and B. Both relationships are linear. Which relationship is also proportional?",
              fig=Q9_FIG,
              choices=["A and B, because both are straight lines.", "B only, because its line starts on the y-axis at 2.",
                       "A only, because its line passes through the origin.", "Neither, because no point is marked at (0, 0)."],
              correct=2, answer="C", space=0.3,
              errors={"A": "every straight line taken as proportional: B passes through (0, 2) [B1G-M, MA.8.AR.3.1: every line taken as proportional]",
                      "B": "the start on the y-axis taken for the test: B starts at 2, so its y is not 0 when x is 0 [B1G-M, MA.8.AR.3.1: the start on the y-axis taken for the test]",
                      "D": "the origin taken as missing because it is not marked: line A passes through (0, 0) [B1G-M, MA.8.AR.3.1: the origin taken as missing because it is not marked]"},
              why="A relationship that is linear is also proportional only when its line passes through the origin. A does (y = 3x: 3(2) = 6); B crosses the y-axis at 2 (y = 3x + 2: 3(2) + 2 = 8), so B is linear and not proportional.",
              check=("many", ("eq", "3*2", "6"), ("eq", "3*0", "0"), ("eq", "3*2 + 2", "8"),
                     ("true", "3*0 + 2 != 0"), ("true", "3*0 == 0")))
    return [q9]


def _ar44():
    q10 = dict(stem="The table shows the cost c, in dollars, of n tickets. What equation gives c in terms of n?", fig=Q10_FIG,
               answer="c = 8.5n",
               why="c ÷ n is 8.5 for every pair: 17.00 ÷ 2, 25.50 ÷ 3, 51.00 ÷ 6, 68.00 ÷ 8. So c = 8.5n; check a pair: 8.5(6) = 51. n = 8.5c swaps c and n.",
               check=("many", ratios([2, 3, 6, 8], ["17.00", "25.50", "51.00", "68.00"], "8.5"), table_of(Fr(17, 2), [2, 3, 6, 8], [17, "25.5", 51, 68])),
               space=0.7)
    q11 = dict(stem="A graph of a proportional relationship is shown. What is the equation of the relationship?", fig=Q11_FIG,
               answer="$y = \\frac{2}{5}x$  or  $y = 0.4x$",
               why="y ÷ x at (5, 2) is 2/5, and at (10, 4) is 4/10 = 2/5. Both y = (2/5)x and y = 0.4x are right. y = (5/2)x divides x by y.",
               check=("many", ratios([5, 10], [2, 4], Fr(2, 5)), ("eq", "F(2,5)", "F('0.4')")), space=0.7)
    q12 = dict(stem="Marcus is paid the same amount for each hour he works. He earns \\$240 for 12 hours.",
               parts=[dict(label="a", stem="Write an equation for his earnings e, in dollars, after h hours.", answer="e = 20h",
                           why="240 ÷ 12 = 20 dollars per hour. Check: 20(12) = 240.",
                           check=("many", ("eq", "F(240,12)", "20"), ("eq", "20*12", "240")), space=0.6),
                      dict(label="b", stem="Solve your equation for h, the hours it takes him to earn e dollars.",
                           answer="h = e ÷ 20,   h = (1/20)e   or   h = 0.05e",
                           why="Divide both sides of e = 20h by 20: h = e ÷ 20, which is (1/20)e or 0.05e, 0.05 hours per dollar. Check: 0.05(240) = 12.",
                           check=("many", ("eq", "F(12,240)", "F('0.05')"), ("eq", "F('0.05')*240", "12")), space=0.6)])
    q13 = dict(stem="The equation  $w = 8.3g$  gives the weight w, in pounds, of g gallons of water. Complete the table.",
               fig=Q13_FIG, answer="w = 16.6 and 41.5;   g = 10",
               why="One point: all three. 8.3(2) = 16.6 and 8.3(5) = 41.5. Solve 83 = 8.3g for g: g = 83 ÷ 8.3 = 10.",
               check=("many", table_of(Fr(83, 10), [2, 5, 10], ["16.6", "41.5", 83]), ("eq", "F(83)/F('8.3')", "10")), space=0.6)
    return [q10, q11, q12, q13]


def _ar45():
    q14 = dict(stem="Two trains travel at constant speeds. The table shows Train A's distances. The graph shows Train B's.", fig=Q14_FIG,
               parts=[dict(label="a", stem="What is each train's constant of proportionality, in miles per hour?",
                           answer="Train A: 65 miles per hour;  Train B: 60 miles per hour",
                           why="One point: both. A: 130 ÷ 2 = 195 ÷ 3 = 325 ÷ 5 = 65. B: read the scales first — the line passes through (1, 60), (2, 120) and (3, 180): 60.",
                           check=("many", ratios([2, 3, 5], [130, 195, 325], 65), ratios([1, 2, 3], [60, 120, 180], 60)), space=0.5),
                      dict(label="b", stem="After 4 hours, how many more miles has the faster train traveled?", answer="20 miles",
                           why="Train A is faster (65 > 60). 65(4) = 260 and 60(4) = 240: 260 − 240 = 20. 5 is the difference for one hour.",
                           check=("many", ("eq", "65*4 - 60*4", "20"), ("true", "65 > 60")), space=0.6)])
    q15 = dict(stem="A pump fills a tank at a constant rate. The graph shows the liters of water it pumps versus the minutes it runs. At this rate, how many minutes will it take to pump 30 liters?",
               fig=Q15_FIG, answer="24 minutes",
               why="The line passes through (4, 5) and (8, 10): 5 ÷ 4 = 1.25 liters per minute. Solve 30 = 1.25m for m: m = 30 ÷ 1.25 = 24 — beyond the grid. 37.5 multiplies 30 by 1.25.",
               check=("many", ratios([4, 8], [5, 10], Fr(5, 4)), ("eq", "30/F(5,4)", "24")), space=0.8)
    return [q14, q15]


def _sections(form="practice"):
    """The practice test, the only form (ruling 49): the blueprint of the unit test."""
    assert form == "practice", "ruling 49: Unit 7's assessment is the practice test alone"
    return [dict(title="Graphing Proportional Relationships", benchmark="MA.7.AR.4.3", items=_ar43()),
            dict(title="The Constant of Proportionality", benchmark="MA.7.AR.4.2", items=_ar42()),
            dict(title="Is It Proportional?", benchmark="MA.7.AR.4.1", items=_ar41()),
            dict(title="Linear, and Also Proportional?", benchmark="MA.8.AR.3.1", items=_ar31()),
            dict(title="Equations of Proportional Relationships", benchmark="MA.7.AR.4.4", items=_ar44()),
            dict(title="Comparing Proportional Relationships", benchmark="MA.7.AR.4.5", items=_ar45())]


# ------------------------------------------------------------------ the review's figures
R1_GRID, R1_DRAWN = figs.pair((0, 10), (0, 36), lines=[figs.prop(Fr(18, 5), "")],
                              points=[(5, 18, ""), (10, 36, "")],
                              ys=6, xname="pounds of birdseed", yname="cost in dollars", inches=3.2)
R1_IN = 5.8       # the grid at least 3.5 in wide on the page (ruling 6, 21 Nov): the table 11.5 units, the grid 10
R1_T = figs.table([([0, 1, 5, 10], [BLANK, BLANK, "18.00", BLANK])], head=("pounds", "cost ($)"), cw=2.0)
R1_TK = figs.table([([0, 1, 5, 10], ["0.00", "3.60", "18.00", "36.00"])], head=("pounds", "cost ($)"), cw=2.0)
R1_FIG = stack([R1_T, R1_GRID], inches=R1_IN)
R1_KEY = stack([R1_TK, R1_DRAWN], inches=R1_IN)
# the review's two picture-choice questions in the paper's shapes (ruling 7, 21 Nov), after the point on y = 7.2x:
# four graphs of y = 1.5x built as the paper's question 2 is (the y-axis by 0.5 a square): the axes swapped
# (y = (2/3)x, through (3, 2)), the scale ignored (y = 0.75x, through (2, 1.5)), 1.5 read as a start (y = x + 1.5),
# and the key, through (1, 1.5) and (2, 3)
_gR = dict(ys=Fr(1, 2), xstep=2, ystep=1)
RG_FIG = figs.row([figs.plane((0, 6), (0, 3), lines=[figs.prop(Fr(2, 3), "")], **_gR),
                   figs.plane((0, 6), (0, 3), lines=[figs.prop(Fr(3, 4), "")], **_gR),
                   figs.plane((0, 6), (0, 3), lines=[(1, Fr(3, 2), "")], **_gR),
                   figs.plane((0, 6), (0, 3), lines=[figs.prop(Fr(3, 2), "")], **_gR)],
                  gap=2.4, titles=["A", "B", "C", "D"], inches=7.2)   # at gap 3 and 6.8 in each grid printed 1 in wide; at gap 1.5 one graph's t stood against the next one's 0
# four toy cars on one grid, as the paper's question 3: lines through (3, 4) (the key), (1, 4), (4, 3) and (3, 3)
RC_FIG = figs.plane((0, 6), (0, 6), lines=[figs.prop(Fr(4, 3), "A"), figs.prop(4, "B"), figs.prop(Fr(3, 4), "C"),
                                           figs.prop(1, "D")],
                    xname="time in seconds", yname="distance in meters", inches=3.0)
R4_FIG = figs.table([([3, 5, 8], ["8.4", "14", "22.4"])], head=("hours", "miles"))
# a plant grows 3/8 inch a day: the days axis scaled by 4
R5_FIG = figs.plane((0, 24), (0, 9), lines=[figs.prop(Fr(3, 8), "")], points=[(8, 3, ""), (16, 6, "")], xs=4,
                    xname="days", yname="inches of growth", inches=3.0)
R6_FIG = figs.table([([-8, -2, 2, 6], [28, 7, -7, -21])])
R7_GRAPH = figs.plane((0, 8), (0, 8), lines=[(Fr(1, 2), 3, "")], points=[(2, 4, ""), (4, 5, "")], inches=2.4)
R7_FIG = figs.row([figs.table([([1, 2, 3, 4], [6, 9, 12, 15])]), figs.table([([4, 8, 12, 16], [7, 14, 21, 28])]), R7_GRAPH],
                  gap=2.0, titles=["A", "B", "C"], inches=6.4)
R8_FIG = figs.table([([2, 3, 5, 6], ["10.40", "16.60", "26.00", "31.20"])], head=("pounds", "cost ($)"))
# two lines on one grid: A from (0, 6), B through the origin
R9_FIG = figs.plane((0, 10), (0, 24), lines=[(Fr(9, 5), 6, "A"), figs.prop(Fr(9, 5), "B")], ys=3,
                    points=[(5, 15, "on"), (5, 9, "on")], inches=3.0)
R10_FIG = figs.table([([3, 5, 8], ["13.8", "23", "36.8"])], head=("bricks, n", "pounds, w"))
R12_FIG = figs.table([([5, 15, BLANK], [BLANK, BLANK, 96])], head=("seconds, t", "feet, h"))
R13_FIG = figs.table([([2, 3, 5], ["14.4", "21.6", "36"])], head=("hours", "tons"))
# the SSDD graph: kayak rental, dollars against hours, the dollars axis scaled by 8
R_SSDD = figs.plane((0, 10), (0, 96), lines=[figs.prop(Fr(48, 5), "")], points=[(5, 48, ""), (10, 96, "")], ys=8, ystep=2,
                    xname="hours", yname="cost in dollars", inches=3.0)
R_SSDD_T = figs.table([([2, 3, 5], ["21.00", "31.50", "52.50"])], head=("hours", "cost ($)"), cw=2.0)
R_SSDD_FIG = figs.row([R_SSDD, R_SSDD_T], gap=4.0, titles=["Shop A", "Shop B"], inches=6.0)


U = dict(
    unit=7, title="Representing Proportional Relationships",
    reference_intro="Nothing in this unit is on the Grade 8 FAST reference sheet: the definition, the tests, the constant of proportionality and y = px are all tested from memory. You may not use this sheet or the FAST reference sheet on the Unit 7 test.",

    reference=[
        dict(title="1.   What Proportional Means", right="Lessons 1–4 · a constant multiple",
             blocks=["**Two quantities are in a proportional relationship when one quantity is always a constant multiple of the other:  y = px.**  The number p is the constant of proportionality. Its unit is a y-unit per x-unit, such as dollars per pound or miles per hour.",
                     "**Identify which quantity is y.**  A table labels its rows, a graph labels its axes, and a description names its two quantities. The question tells you which one is y.",
                     "**When x is 0, y is 0.**  In 0 hours you earn \\$0, so the graph of a proportional relationship passes through the origin, (0, 0)."]),
        dict(title="2.   Is It Proportional? The Tests", right="Lesson 4 · every pair, both conditions",
             blocks=[dict(table=([1900, 3700, 3760], [
                         ["Shown as", "Proportional when", "Not proportional, for example"],
                         ["a table", "y ÷ x is the same for every pair", "x: 1, 2, 3 and y: 3, 7, 11, because 3 ÷ 1 = 3 but 7 ÷ 2 = 3.5"],
                         ["a graph", "a straight line through the origin", "a straight line that starts at (0, 3); a curve"],
                         ["a description", "a constant rate, nothing added at the start", "a \\$15 fee plus \\$2 per mile"],
                         ["an equation", "y = px, nothing added", "y = 4x + 1"]])),
                     "**Test every pair.**  Two pairs that agree are not enough. If even one pair gives a different value of y ÷ x, the relationship is not proportional.",
                     "**Going up by the same amount does not make y ÷ x the same.**  When x is 1, 2, 3 and y is 3, 7, 11, y goes up 4 each time, but 3 ÷ 1 = 3 and 7 ÷ 2 = 3.5.",
                     "**A table does not have to show the pair (0, 0), and a graph does not have to mark it.**  If a table does show (0, 0), skip that pair when you divide, because you cannot divide by 0. On a graph, extend the line. If it passes through the origin, the graph passes the test.",
                     "**Linear, and also proportional?**  A linear relationship has a straight-line graph. It is also proportional only when its line passes through the origin: $y = 1.4x$ is proportional; $y = 1.4x + 2$ is linear but not proportional, because y is 2 when x is 0."]),
        dict(title="3.   Finding the Constant of Proportionality", right="Lessons 2–3 · y ÷ x",
             blocks=[dict(table=([2600, 6760], [
                         ["From", "How"],
                         ["a table", "y ÷ x is the same for every pair. For x: 3, 5, 10 and y: 4.2, 7, 14, it is 4.2 ÷ 3 = 7 ÷ 5 = 14 ÷ 10 = 1.4."],
                         ["a graph", "Read the scales first. Choose a point on the line where two grid lines cross, and divide its y by its x: (5, 7) gives 7 ÷ 5 = 1.4."],
                         ["a description", "Divide the y-quantity by the x-quantity. Sam types 250 words in 5 minutes: 250 ÷ 5 = 50 words per minute."]])),
                     "**The constant of proportionality is the amount of y for every 1 unit of x.**  Divide y by x to find it, in any representation.",
                     "**The constant depends on which quantity is y.**  Typing 250 words in 5 minutes is $250 \\div 5 = 50$ words per minute. With minutes as y, it is $5 \\div 250 = 1/50$ minute per word. The question tells you which one to find.",
                     "**A constant can be negative.**  For x: −2, 1, 4 and y: 6, −3, −12, y ÷ x = −3 for every pair, and the line goes down from left to right through the origin.",
                     "**Explain what it means, with its units.**  A constant of 0.25 dollars per minute means that each minute costs \\$0.25. It is not a starting amount, and it is not the number of minutes per dollar."]),
        dict(title="4.   Graphing a Proportional Relationship", right="Lesson 1 · a line through the origin",
             blocks=["**Make a table, plot its points, and draw a straight line through the origin.**  Use the third point as a check: all three points must lie on one straight line.",
                     "**Choose x-values that give whole-number y-values.**  For $y = \\frac{5}{3}x$, the x-values 0, 3 and 6 give the y-values 0, 5 and 10.",
                     "**Read the scales first.**  Before you read or plot a point, find what one square stands for on each axis. If the grid lines are numbered 0, 10, 20, one square stands for 10. The two axes may have different scales.",
                     "**The point (1, p) is on the line.**  It shows the constant: the amount of y for 1 unit of x."]),
        dict(title="5.   Writing and Solving the Equation", right="Lessons 5–6 · y = px",
             blocks=["**Find p, then write y = px using the problem's letters.**  Sam types w words in m minutes, so $w = 50m$. Check it with a pair: $50(5) = 250$.",
                     "**Either variable can be isolated.**  The equation $w = 50m$ is solved for w, and it gives the words typed in m minutes. To solve it for m, divide both sides by 50. The equation $m = (1/50)w$, or $m = 0.02w$, gives the minutes for w words. One relationship has two constants, 50 and 1/50.",
                     "**Translate from one representation to another.**  An equation gives a table (substitute x to get y), the table gives the graph, and any one of them gives p.",
                     "**Solve for x when you know y.**  If $y = 1.4x$ and y is 21, substitute 21 for y:  $21 = 1.4x$. Isolate x by dividing both sides by 1.4:  $x = 21 \\div 1.4 = 15$."]),
        dict(title="6.   Comparing Proportional Relationships", right="Lesson 7 · compare the constants",
             blocks=["**Find each constant in the same units, then compare them.**  Store A: 4 pounds for \\$12.20 is \\$3.05 per pound. Store B: $c = 3.15w$ is \\$3.15 per pound. Store A costs less per pound.",
                     "**On the same axes, the greater positive constant gives the steeper line.**  The line $y = 2x$ is steeper than the line $y = 1.4x$.",
                     "**Then answer the question asked.**  For 10 pounds, Store A costs $3.05(10) = 30.50$ and Store B costs $3.15(10) = 31.50$, so Store A costs \\$1.00 less.",
                     "**For values beyond the grid, use the equation.**  The line through the origin and (5, 7) is $y = 1.4x$. If the grid ends before y reaches 28, solve $28 = 1.4x$ for x:  $x = 20$."]),
        dict(title="7.   Vocabulary",
             blocks=[dict(vocab=[
                 ("proportional relationship", "two quantities are in a proportional relationship when one quantity is always a constant multiple of the other: y = px"),
                 ("constant of proportionality", "the number p in y = px. It equals y ÷ x for every pair where x is not 0: the amount of y for every 1 unit of x (some books write k)"),
                 ("unit rate", "the amount of y for 1 unit of x; in a proportional relationship, it is the constant of proportionality with its unit"),
                 ("origin", "the point (0, 0)"),
                 ("linear relationship", "a relationship whose graph is a straight line"),
                 ("equation of a proportional relationship", "y = px, with nothing added")])]),
    ],

    # ------------------------------------------------------------------ unit review (unscored; home Tue 12 Jan)
    review=[
        dict(title="Graphing Proportional Relationships", lessons="Lesson 1", benchmark="MA.7.AR.4.3", items=[
            dict(stem="Birdseed costs the same amount per pound, and 5 pounds cost \\$18.00.", fig=R1_FIG, fig_key=R1_KEY,
                 parts=[dict(label="a", stem="Complete the table.", answer="\\$0.00,  \\$3.60,  \\$36.00",
                             why="18.00 ÷ 5 = 3.60 dollars per pound: 3.60(0) = 0.00, 3.60(1) = 3.60, 3.60(10) = 36.00.",
                             check=("many", ("eq", "F('18.00')/5", "F('3.60')"), table_of(Fr(18, 5), [0, 1, 5, 10], ["0.00", "3.60", "18.00", "36.00"])), space=0.2),
                        dict(label="b", stem="Graph the relationship on the grid.",
                             answer="The points (0, 0), (5, 18) and (10, 36), and the line from the origin through them",
                             why="Read the scales first: the cost axis counts by 6. (1, 3.60) is on the line too, between grid lines.",
                             check=table_of(Fr(18, 5), [0, 5, 10], [0, 18, 36]), space=0.3)]),
            dict(stem="Choose three x-values that give whole-number y-values for  $y = \\frac{7}{4}x$,  and find each y.",
                 answer="x = 0, 4, 8 gives y = 0, 7, 14  (any multiples of 4)",
                 why="Choose multiples of 4 for x. (7/4)(4) = 7 and (7/4)(8) = 14.",
                 check=table_of(Fr(7, 4), [0, 4, 8], [0, 7, 14]), space=0.6),
            dict(stem="Which point is on the graph of  $y = 7.2x$?",
                 choices=["(36, 5)", "(1, 8.2)", "(5, 36)", "(0, 7.2)"], correct=2, answer="C", space=0.3,
                 errors={"A": "the coordinates reversed: y written first [B1G-M, MA.7.AR.4.3: the ratio taken in the wrong order]",
                         "B": "7.2 added to 1, not multiplied [B1G-M, MA.7.AR.4.3: added, not multiplied]",
                         "D": "7.2 read as a start: when x is 0, y is 0 [B1G-M, MA.7.AR.4.3: the constant read as a start]"},
                 why="7.2(5) = 36, so (5, 36) is on the line. 7.2(36) = 259.2, 7.2(1) = 7.2 and 7.2(0) = 0 rule out the others.",
                 check=("many", ("eq", "F('7.2')*5", "36"), ("true", "F('7.2')*36 != 5"), ("true", "F('7.2')*1 != F('8.2')"),
                        ("true", "F('7.2')*0 != F('7.2')"))),
            dict(stem="Which graph shows the relationship  $y = 1.5x$?",
                 fig=RG_FIG, choices=["Graph A", "Graph B", "Graph C", "Graph D"], correct=3, answer="D", space=0.3,
                 errors={"A": "the axes swapped: its line is y = (2/3)x, through (3, 2) [B1G-M, MA.7.AR.4.3: the ratio taken in the wrong order]",
                         "B": "the scale ignored: one and a half squares up for every 1 unit of x is y = 0.75x, through (2, 1.5) [B1G-M, MA.7.AR.4.3: the axis scale misread]",
                         "C": "1.5 read as a start and x as the rate: y = x + 1.5, through (0, 1.5) and (1, 2.5) [B1G-M, MA.7.AR.4.3: the constant read as a start]"},
                 why="Read the scales first: each square up is 0.5. y = 1.5x gives 1.5(1) = 1.5 and 1.5(2) = 3: the line through the origin, (1, 1.5) and (2, 3) is graph D. In grid squares graph B looks like 1.5 — one and a half squares up for every 1 unit of x — but its line is y = 0.75x.",
                 check=("many", ("eq", "F(3,2)*1", "F(3,2)"), ("eq", "F(3,2)*2", "3"),
                        ("eq", "F(2,3)*3", "2"), ("true", "F(2,3)*3 != F(3,2)*3"),
                        ("eq", "F(3,4)*2", "F(3,2)"), ("true", "F(3,4)*2 != F(3,2)*2"),
                        ("eq", "0 + F(3,2)", "F(3,2)"), ("eq", "1 + F(3,2)", "F(5,2)"), ("true", "0 + F(3,2) != F(3,2)*0"))),
            dict(stem="Four toy cars each roll at a constant speed. The graph shows the distance each car rolls, in meters, versus the time, in seconds. Which line shows the car that rolls 4 meters every 3 seconds?",
                 fig=RC_FIG, choices=["Line A", "Line B", "Line C", "Line D"], correct=0, answer="A", space=0.3,
                 errors={"B": "4 meters every 1 second: line B passes through (1, 4) [B1G-M, MA.7.AR.4.3: the rate read for 1 second]",
                         "C": "the ratio reversed: line C goes 3 meters every 4 seconds, through (4, 3) [B1G-M, MA.7.AR.4.3: the ratio taken in the wrong order]",
                         "D": "4 − 3 = 1 meter each second, subtracted: line D passes through (3, 3) [B1G-M, MA.7.AR.4.3: a difference taken for the rate]"},
                 why="4 meters every 3 seconds is the point (3, 4), and line A passes through it: 4/3 meters per second.",
                 check=("many", ("eq", "F(4,3)*3", "4"),
                        ("true", "4*3 != 4"), ("true", "F(3,4)*3 != 4"), ("true", "1*3 != 4"))),
        ]),
        dict(title="The Constant of Proportionality", lessons="Lessons 2–3", benchmark="MA.7.AR.4.2", items=[
            dict(stem="A kayaker paddles at a constant speed. The table shows how far she paddles. What is the constant of proportionality, in miles per hour?",
                 fig=R4_FIG, answer="2.8 miles per hour",
                 why="y ÷ x for every pair: 8.4 ÷ 3 = 2.8, 14 ÷ 5 = 2.8, 22.4 ÷ 8 = 2.8.",
                 check=ratios([3, 5, 8], ["8.4", 14, "22.4"], "2.8"), space=0.5),
            dict(stem="The graph shows how much a plant grows, in inches, versus the number of days.", fig=R5_FIG,
                 parts=[dict(label="a", stem="What is the constant of proportionality, in inches per day?", answer="3/8 inch per day  (0.375)",
                             why="Read the scales first: the days axis counts by 4. The line passes through (8, 3) and (16, 6): 3 ÷ 8 = 6 ÷ 16 = 3/8.",
                             check=("many", ratios([8, 16], [3, 6], Fr(3, 8)), ("eq", "F(3,8)", "F('0.375')")), space=0.4),
                        dict(label="b", stem="What does the constant of proportionality mean in this situation?",
                             answer="Each day, the plant grows 3/8 inch.",
                             why="The amount of y for every 1 unit of x: inches per day. Not 8/3 inches per day (x ÷ y), and not a starting height.",
                             check=("eq", "F(3,8)*1", "F(3,8)"), space=0.4)]),
            dict(stem="A table is shown. y is proportional to x. What is the constant of proportionality?", fig=R6_FIG,
                 answer="−3.5", why="28 ÷ (−8) = −3.5, 7 ÷ (−2) = −3.5, −7 ÷ 2 = −3.5, −21 ÷ 6 = −3.5.",
                 check=ratios([-8, -2, 2, 6], [28, 7, -7, -21], "-3.5"), space=0.5),
        ]),
        dict(title="Is It Proportional?", lessons="Lesson 4", benchmark="MA.7.AR.4.1", items=[
            dict(stem="Select all the relationships that are proportional.", fig=R7_FIG,
                 choices=["Table A", "Table B", "Graph C",
                          "Each bag of ice weighs 10 pounds (total weight and number of bags).",
                          "A bowling alley charges \\$3.00 for shoes plus \\$4.80 per game (total cost and number of games)."],
                 correct=[1, 3], answer="B, D", space=0.3,
                 errors={"A": "a constant difference: y goes up 3 each time, but 6 ÷ 1 = 6 and 9 ÷ 2 = 4.5 [B1G-M, MA.7.AR.4.1: a constant increase taken for proportional]",
                         "C": "straight, but from (0, 3), not the origin [B1G-M, MA.7.AR.4.1: every straight line taken as proportional]",
                         "E": "a \\$3.00 start added: 1 game costs \\$7.80 and 2 games \\$12.60, and 7.80 ÷ 1 is not 12.60 ÷ 2 [B1G-M, MA.7.AR.4.1: a start added]"},
                 why="B: 7 ÷ 4 = 14 ÷ 8 = 21 ÷ 12 = 28 ÷ 16 = 1.75. D: the weight is 10 times the bags, nothing added at the start. A goes up by the same amount; C starts at (0, 3); E adds \\$3.00 for shoes.",
                 check=("many", ratios([4, 8, 12, 16], [7, 14, 21, 28], Fr(7, 4)), table_of(10, [1, 2, 3], [10, 20, 30]),
                        ("true", "F(6,1) != F(9,2)"), ("true", "F(1,2)*0 + 3 != 0"), ("true", "F('7.80')/1 != F('12.60')/2"))),
            dict(stem="The table shows the cost of different weights of cherries.", fig=R8_FIG,
                 parts=[dict(label="a", stem="Is the cost proportional to the weight? Explain.",
                             answer="No, because 16.60 ÷ 3 is not 5.20, and every other pair gives 5.20.",
                             why="10.40 ÷ 2 = 26.00 ÷ 5 = 31.20 ÷ 6 = 5.20, but 16.60 ÷ 3 ≈ 5.53: one pair with a different value means the relationship is not proportional.",
                             check=("many", ratios([2, 5, 6], ["10.40", "26.00", "31.20"], "5.20"), ("true", "F('16.60')/3 != F('5.20')")), space=0.4),
                        dict(label="b", stem="If it is not, which cost would have to change, and what should it be?", answer="The cost of 3 pounds; \\$15.60",
                             why="5.20(3) = 15.60.", check=("eq", "F('5.20')*3", "F('15.60')"), space=0.4)]),
        ]),
        dict(title="Linear, and Also Proportional?", lessons="Lesson 4", benchmark="MA.8.AR.3.1", items=[
            dict(stem="The graph shows two relationships, A and B. Both relationships are linear.", fig=R9_FIG,
                 parts=[dict(label="a", stem="Which relationship is also proportional?",
                             choices=["A and B, because in both, y goes up the same amount for every 1 unit of x.", "B only, because its line passes through the origin.",
                                      "A only, because its line starts on the y-axis at 6.", "Neither, because no point is marked at (0, 0)."],
                             correct=1, answer="B",
                             errors={"A": "a constant increase taken for proportional: A goes up 1.8 for every 1 unit of x too, but starts at 6 [B1G-M, MA.8.AR.3.1: a constant increase taken for proportional]",
                                     "C": "the start on the y-axis taken for the test: A starts at 6, so its y is not 0 when x is 0 [B1G-M, MA.8.AR.3.1: the start on the y-axis taken for the test]",
                                     "D": "the origin taken as missing because it is not marked: line B passes through (0, 0) [B1G-M, MA.8.AR.3.1: the origin taken as missing because it is not marked]"},
                             why="B. Both lines go up 1.8 for every 1 unit of x, but only B passes through (0, 0). A linear relationship is also proportional only when its line passes through the origin; A is 6 when x is 0.",
                             check=("many", ("eq", "F(9,5)*5", "9"), ("eq", "F(9,5)*0", "0"), ("eq", "F(9,5)*5 + 6", "15"),
                                    ("true", "F(9,5)*0 + 6 != 0"), ("true", "F(9,5)*0 == 0"))),
                        dict(label="b", stem="Write the equation of the proportional relationship.", answer="y = 1.8x",
                             why="(5, 9) is on B: 9 ÷ 5 = 1.8.", check=ratios([5], [9], "1.8"), space=0.4),
                        dict(label="c", stem="The relationship  $y = 9x - 4$  is linear. Is it also proportional? Explain.",
                             answer="No. When x is 0, y is −4, so its line does not pass through the origin.",
                             why="9(0) − 4 = −4, not 0. A linear relationship is also proportional only when its line passes through the origin.",
                             check=("many", ("eq", "9*0 - 4", "-4"), ("true", "9*0 - 4 != 0")), space=0.4)]),
        ]),
        dict(title="Equations of Proportional Relationships", lessons="Lessons 5–6", benchmark="MA.7.AR.4.4", items=[
            dict(stem="The table shows the weight w, in pounds, of n bricks. What equation gives w in terms of n?", fig=R10_FIG,
                 answer="w = 4.6n", why="w ÷ n is 4.6 for every pair: 13.8 ÷ 3, 23 ÷ 5, 36.8 ÷ 8. Check: 4.6(8) = 36.8.",
                 check=ratios([3, 5, 8], ["13.8", 23, "36.8"], "4.6"), space=0.5),
            dict(stem="Kiwis cost the same amount per pound, and 4 pounds cost \\$5.00.",
                 parts=[dict(label="a", stem="Write an equation for the cost c, in dollars, of w pounds.", answer="c = 1.25w",
                             why="5.00 ÷ 4 = 1.25 dollars per pound. Check: 1.25(4) = 5.", check=("eq", "F('5.00')/4", "F('1.25')"), space=0.4),
                        dict(label="b", stem="Solve your equation for w, the pounds that c dollars buy.", answer="w = c ÷ 1.25,   w = 0.8c   or   w = (4/5)c",
                             why="Divide both sides of c = 1.25w by 1.25: w = c ÷ 1.25, which is 0.8c, 0.8 pounds per dollar. Check: 0.8(5) = 4.", check=("many", ("eq", "4/F('5.00')", "F('0.8')"), ("eq", "F('0.8')*5", "4")), space=0.4)]),
            dict(stem="The equation  $h = 4.8t$  gives how many feet h a weather balloon has risen t seconds after it is released. Complete the table.",
                 fig=R12_FIG, answer="h = 24 and 72;   t = 20",
                 why="4.8(5) = 24 and 4.8(15) = 72. Solve 96 = 4.8t for t: t = 96 ÷ 4.8 = 20.",
                 check=("many", table_of(Fr(24, 5), [5, 15, 20], [24, 72, 96]), ("eq", "96/F('4.8')", "20")), space=0.5),
        ]),
        dict(title="Comparing Proportional Relationships", lessons="Lesson 7", benchmark="MA.7.AR.4.5", items=[
            dict(stem="Two machines make snow at constant rates. The table shows how many tons of snow Machine A makes. Machine B makes s tons in h hours, where  $s = 6.8h$.",
                 fig=R13_FIG,
                 parts=[dict(label="a", stem="Which machine makes more snow each hour?", answer="Machine A (7.2 tons per hour versus 6.8)",
                             why="A: 14.4 ÷ 2 = 21.6 ÷ 3 = 36 ÷ 5 = 7.2.",
                             check=("many", ratios([2, 3, 5], ["14.4", "21.6", 36], "7.2"), ("true", "F('7.2') > F('6.8')")), space=0.4),
                        dict(label="b", stem="How many more tons does it make in 10 hours?", answer="4 tons",
                             why="7.2(10) = 72 and 6.8(10) = 68: 72 − 68 = 4.", check=("eq", "F('7.2')*10 - F('6.8')*10", "4"), space=0.4)]),
            dict(stem="On the same axes, which line is steeper:  $y = 1.8x$  or  $y = \\frac{7}{4}x$?  Explain.",
                 answer="y = 1.8x, because 1.8 is greater than 7/4 = 1.75",
                 why="On the same axes, the greater positive constant gives the steeper line: 1.8 > 1.75.",
                 check=("true", "F('1.8') > F(7,4)"), space=0.5),
            # the SSDD block (§16 rule 3): ONE graph asked four ways — the constant, the equation, a value past the grid,
            # and the same relationship against a second one given as a table. The name prints on the key only.
            dict(stem="The graph shows the cost of renting a kayak from Shop A. The table shows Shop B's costs. Answer each part.",
                 key_stem="The graph shows the cost of renting a kayak from Shop A. The table shows Shop B's costs.   **SSDD:**  one graph asked four ways — (a) the constant (7.02–03), (b) the equation (7.05–06), (c) a value beyond the grid (7.07), (d) the same relationship compared with a second one given as a table (7.07). The student decides which kind each part is.",
                 fig=R_SSDD_FIG,
                 parts=[dict(label="a", stem="What is Shop A's constant of proportionality, in dollars per hour?", answer="9.6 dollars per hour  (\\$9.60)",
                             why="Read the scales first: the cost axis counts by 8. (5, 48): 48 ÷ 5 = 9.6, and (10, 96): 96 ÷ 10 = 9.6.",
                             check=ratios([5, 10], [48, 96], "9.6"), space=0.4),
                        dict(label="b", stem="Write an equation for Shop A's cost c, in dollars, for h hours.", answer="c = 9.6h",
                             why="c = ph with p = 9.6. Check: 9.6(5) = 48.", check=("eq", "F('9.6')*5", "48"), space=0.4),
                        dict(label="c", stem="For how many hours can you rent a kayak from Shop A for \\$144?", answer="15 hours",
                             why="Solve 144 = 9.6h for h: h = 144 ÷ 9.6 = 15 — beyond the grid.", check=("eq", "144/F('9.6')", "15"), space=0.4),
                        dict(label="d", stem="Which shop charges less per hour, and how much less does it cost for 6 hours?",
                             answer="Shop A; \\$5.40 less",
                             why="Shop B: 21.00 ÷ 2 = 31.50 ÷ 3 = 52.50 ÷ 5 = 10.50 dollars per hour, more than 9.60. For 6 hours: 10.50(6) − 9.60(6) = 63.00 − 57.60 = 5.40.",
                             check=("many", ratios([2, 3, 5], ["21.00", "31.50", "52.50"], "10.5"), ("eq", "F('10.5')*6 - F('9.6')*6", "F('5.40')")), space=0.5)]),
        ]),
    ],

    # ------------------------------------------------------------------ the assessment: the practice test alone (ruling 49)
    assessment=dict(
        total=20,
        tracker_order=["MA.7.AR.4.3", "MA.7.AR.4.2", "MA.7.AR.4.1", "MA.8.AR.3.1", "MA.7.AR.4.4", "MA.7.AR.4.5"],
        tracker={"MA.7.AR.4.3": 4, "MA.7.AR.4.2": 4, "MA.7.AR.4.1": 3, "MA.8.AR.3.1": 1, "MA.7.AR.4.4": 5, "MA.7.AR.4.5": 3},
        forms={"practice": _sections("practice")},
    ),
)
