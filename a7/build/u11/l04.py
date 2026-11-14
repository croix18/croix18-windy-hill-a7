# A7 11.04  Multi-Step Equations — MA.8.AR.2.1 (MN 11.4). Fri 4 Dec 2026, a 53-minute period (Thursday 3 Dec has
# no class, so the last lesson is Wednesday's 11.03). The benchmark's words "with rational number coefficients" are
# today's content: a fraction distributed (it multiplies every term inside, like a whole number), both sides
# multiplied by a common denominator (every term, the constants too), and a decimal distributed — the lowest-scoring
# released Grade 8 FAST skill (21%), so it gets Notes III, board 3 and its own set question, with a negative decimal
# factor there (the audit's §4 gap: the state item is −3.5(10x − 2) = −176.75). One order for every equation, and a
# check in both sides. The three endings of 11.03 come back once (board 6, set question 5). Built from the benchmark
# and the B1G-M first (the unit's Lesson Outlines, §11.04), then read against Math Nation 11.4 (the unit audit, Part 1).
# Not reproduced: the game-statistics warm-up (no AR.2.1 content), Clare's "a mistake" that is two (D7), the card
# sort with no cards (D11) and its card K work line (D8), the key whose equation is not the student page's (D6), the
# key lines with wrong constants (D9, D10), and the partner work.
#
# Every equation is solved again by sympy at build time over the REAL numbers; every worked row of the examples is
# re-derived in its check (each line has the same solution as the first equation). The answer slides' steps: the
# kit's stepcheck holds an "=" between two expressions in the same letter to be an identity and an "=" between two
# numbers to be true, so a step never writes an equation with the letter on both sides (it writes each side's
# simplification as an identity instead), and the one true ending on a step (−2 = −2) is a true statement of numbers.

U = "sp.Symbol('u', real=True)"


def _u(e):
    import re
    return re.sub(r"\bu\b", U, e)


def solves(left, right, value):
    """sympy solves left = right (in u) and finds exactly `value`."""
    return ("eq", "sp.solve(sp.Eq(" + _u(left) + ", " + _u(right) + "), " + U + ")[0]", value)


def same(e1, e2):
    """Two expressions in u are the same expression: a correct line of work, or (as an equation) infinitely many."""
    return ("true", "sp.expand(" + _u(e1) + " - (" + _u(e2) + ")) == 0")


def never(left, right):
    """left = right is never true: left − right simplifies to a nonzero number (no solution)."""
    d = "sp.expand(" + _u(left) + " - (" + _u(right) + "))"
    return ("true", "(" + d + ").is_number and " + d + " != 0")


def not_never(left, right):
    """left = right is NOT a no-solution equation (it has one solution or infinitely many)."""
    d = "sp.expand(" + _u(left) + " - (" + _u(right) + "))"
    return ("true", "(" + d + ").is_number != True or " + d + " == 0")


def not_every(left, right):
    """left = right is NOT true for every number."""
    return ("true", "sp.expand(" + _u(left) + " - (" + _u(right) + ")) != 0")


L = dict(
    code="11.04", unit=11, lesson_no=4,
    title="Multi-Step Equations",
    unit_title="Solving Equations and Systems",
    benchmark="MA.8.AR.2.1",
    benchmark_text="Solve multi-step linear equations in one variable, with rational number coefficients. Include equations with variables on both sides.",
    target="I can solve a multi-step equation with fraction or decimal coefficients and check it.",
    yesterday="Last class: one solution, no solution or infinitely many.",
    today="Today: multi-step equations with fractions and decimals.",
    essential="Why does a fraction or a decimal in front of parentheses follow the same rule as a whole number — and why must every term be multiplied when we clear fractions?",
    building_on="11.01 — like terms and the distributive property; 11.02 — the variable on both sides; 11.03 — the three endings; Unit 4 — fraction and decimal arithmetic.",
    working_toward="The Unit 11 test (Fri 11 Dec), whose question 4 distributes a decimal; 11.05–11.08 — at a system's crossing both equations give the same y; Algebra 1 (MA.912.AR.2.1) — writing the equation from a context.",
    vocab=[("common denominator", "a number that every denominator divides evenly: 6 is a common denominator of $\\frac{x}{2}$ and $\\frac{x}{3}$"),
           ("rational coefficient", "a coefficient that is a fraction or a decimal, like $\\frac{1}{3}$ in $\\frac{1}{3}x$ or $0.5$ in $0.5x$")],
    vocab_note="Two words for today's numbers. A common denominator is the number that clears every fraction at once — 6 for halves and thirds, 15 for thirds and fifths. A rational coefficient is just a fraction or a decimal in front of the variable; the moves of the last three days do not change.",
    ixl=["Solve multi-step equations — 55K", "Solve multi-step equations: complete the solution — PGH", "Solve equations: mixed review — HZZ"],
    closure="Board 9 is written work and it is the exit evidence: 1.5(4x − 2) + x is 6x − 3 + x = 7x − 3, the right side is 2x + 12, so 5x = 15 and x = 3; the check puts 3 into both sides of the first equation, 1.5(10) + 3 = 18 and 2(9) = 18. A board with x = 3 and no check has half of it.",

    mtr=[("MTR.3.1", "boards 1–5: one order for every equation — distribute, collect, move, divide, check"),
         ("MTR.4.1", "boards 4 and 6: a split room re-votes"),
         ("MTR.6.1", "board 9 and every answer slide: the solution checked in both sides of the first equation")],
    hoq=[("In x/2 + 3 = x/3 + 5, why must the 3 and the 5 be multiplied by 6 too?", "DOK 2"),
         ("Board 4's wrong options came from three different mistakes. Without solving, how can you show that x = 2 is not the solution?", "DOK 3"),
         ("For ⅓(6x + 9) = x + 7, would you distribute the ⅓ or multiply both sides by 3 first? Do both routes give the same solution? Why?", "DOK 3")],
    differentiation=[
        ("ESE / 504", "The order stays on the board all period as five numbered words — distribute, collect, move, divide, check — with arrows from the fraction or decimal to each term inside. Every board starts by drawing those arrows before anything is written."),
        ("ELL", "**Distribute**: the number outside multiplies every term inside. **Common denominator**: one number that clears every fraction. **Check**: put the number back in each side; the two numbers must match."),
        ("Enrichment", "Board 5 finishes early for some: solve x/4 − 2 = x/6 + 1 two ways — multiply by 12, then by 24. Why do both give x = 36? Which is less work?")],

    warmup=[
        dict(stem="How many solutions does  $2(x + 3) = 2x + 6$  have?", answer="Infinitely many", band="last lesson",
             source="11.03 — the three endings: both sides are 2x + 6",
             check=same("2*(u + 3)", "2*u + 6")),
        dict(stem="Solve:  $9x - 7 = 4x + 18$", answer="x = 5", band="this week",
             source="11.02 — the variable on both sides",
             check=solves("9*u - 7", "4*u + 18", "5")),
        dict(stem="A triangle has sides 5, 9 and x. Between which numbers is x?", answer="Between 4 and 14", band="last unit",
             source="6.01 — the Triangle Inequality: 9 − 5 < third side < 9 + 5",
             check=("true", "9 - 5 == 4 and 9 + 5 == 14")),
        dict(stem="Find  $\\frac{2}{3}$  of 9.", answer="6", band="the prerequisite this lesson needs",
             source="7th grade — a fraction of a number; today's fractions multiply every term inside the parentheses",
             check=("eq", "F(2,3)*9", "6")),
    ],
    warmup_note="Q4 is today's move in miniature: two-thirds of 9 is 6, so two-thirds of 9x is 6x. Say that in one sentence after the reveal — Example 2's Your Turn distributes a two-thirds. Two minutes silent, then reveal, no discussion.",

    notes=[
        dict(numeral="I", head="One order for every equation", min=4, sub="Copy all four lines.",
             note="The order of the last three days, said once as a list: distribute; collect like terms on each side; move the x-terms to one side and the constants to the other; divide; check. Here the left is 6x − 12 + 5 = 6x − 7 and the right is 2x + 12 + 1 = 2x + 13. Take 2x from both sides and add 7: 4x = 20, so x = 5. Check in both sides of the first equation: 3(6) + 5 = 23 and 2(11) + 1 = 23.\nOFF: 'Distribute, collect, move, divide, check. Every equation, every time.'",
             math=["$3(2x - 4) + 5 = 2(x + 6) + 1$", "$6x - 7 = 2x + 13$", "$4x = 20 \\qquad x = 5$"],
             items2=["**Distribute. Collect each side. Move. Divide. Check.**",
                     "Check:  $3(6) + 5 = 23$   and   $2(11) + 1 = 23$"],
             letters=False),
        dict(numeral="II", head="Fractions: distribute, or clear them", min=4, sub="",
             note="Two ways with a fraction. First: distribute it — one-third of 6x is 2x and one-third of 9 is 3, every term inside, just as a whole number would. Then 2x + 3 = x + 7 and x = 4. Second: multiply BOTH sides by a common denominator. Halves and thirds clear with 6, and the 6 multiplies EVERY term — the 3 and the 5 as well as the fractions: 3x + 18 = 2x + 30, so x = 12. Check: 6 + 3 = 9 and 4 + 5 = 9. A board that writes 3x + 3 = 2x + 5 multiplied only the fractions.\nOFF: 'A fraction outside the parentheses multiplies every term inside. A common denominator multiplies every term on both sides.'",
             math=["$\\frac{1}{3}(6x + 9) = x + 7 \\qquad 2x + 3 = x + 7 \\qquad x = 4$",
                   "$\\frac{x}{2} + 3 = \\frac{x}{3} + 5 \\qquad 3x + 18 = 2x + 30 \\qquad x = 12$"],
             items2=["**Multiply both sides by 6: every term, the 3 and the 5 too.**"],
             letters=False),
        dict(numeral="III", head="Decimals: the decimal multiplies both terms", min=3, sub="",
             note="The 0.5 multiplies the 8x AND the −6: 4x − 3. Then the x-terms: take 1.5x from both sides, 2.5x on the left; add 3: 2.5x = 5, so x = 2. Check: 0.5(16 − 6) = 5 and 1.5(2) + 2 = 5. This is the skill the state scored lowest on its released Grade 8 test — almost four in five students missed it — and the miss is nearly always 4x − 6: the decimal never reached the second term.\nOFF: 'The decimal is a number like any other. It multiplies every term inside.'",
             math=["$0.5(8x - 6) = 1.5x + 2$", "$4x - 3 = 1.5x + 2$", "$2.5x = 5 \\qquad x = 2$"],
             items2=["The 0.5 multiplies both terms:  $0.5(8x) = 4x$  and  $0.5(-6) = -3$."],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", sub="Parentheses on both sides.", min_q=1,
             note_q="Ask what each side is once it is distributed and collected, before anyone moves a term.",
             prompt=["$2(3x + 1) - 4x = 3(x - 2) + 1$"], ask="Solve it, then check in both sides.",
             worked=[dict(sub="Worked.", min=2,
                          note="Each side first: the left is 6x + 2 − 4x = 2x + 2, the right 3x − 6 + 1 = 3x − 5. Take 2x (the smaller) from both sides: 2 = x − 5, so x = 7. Check in both sides of the first equation: 2(22) − 28 = 16 and 3(5) + 1 = 16. A board with x = 3 wrote 3x − 2 on the right (the 3 to one term only); one with x = −5 wrote 3x + 6 (the sign).",
                          rows=[("2(3x + 1) - 4x = 3(x - 2) + 1", "the equation"),
                                ("6x + 2 - 4x = 3x - 6 + 1", "distribute on both sides"),
                                ("2x + 2 = 3x - 5", "collect like terms on each side"),
                                ("2 = x - 5 \\qquad x = 7", "take 2x from both sides; add 5"),
                                ("\\text{Check: } 2(22) - 4(7) = 16 \\quad 3(5) + 1 = 16", "both sides of the first equation")],
                          answer="x = 7")],
             check=("many", solves("2*(3*u + 1) - 4*u", "3*(u - 2) + 1", "7"),
                    solves("6*u + 2 - 4*u", "3*u - 6 + 1", "7"), solves("2*u + 2", "3*u - 5", "7"), solves("2", "u - 5", "7"),
                    ("eq", "2*(3*7 + 1) - 4*7", "16"), ("eq", "3*(7 - 2) + 1", "16"),
                    solves("2*(3*u + 1) - 4*u", "3*u - 2 + 1", "3"), solves("2*(3*u + 1) - 4*u", "3*u + 6 + 1", "-5")),
             your_turn=dict(min=2, note="The left is 4x + 8 − x = 3x + 8, the right 2x − 6 + 20 = 2x + 14. Take 2x: x + 8 = 14, so x = 6. Check: 4(8) − 6 = 26 and 2(3) + 20 = 26. This catches a student who collects across the equals sign, and the one-term distribution: 4x + 2 − x on the left gives x = 12.",
                            prompt=["$4(x + 2) - x = 2(x - 3) + 20$", "Solve it, then check in both sides."],
                            steps=["Left:  $4(x + 2) - x = 3x + 8$.   Right:  $2(x - 3) + 20 = 2x + 14$",
                                   "Take 2x from both sides:  $x + 8 = 14$,  so  $x = 6$",
                                   "Check:  $4(6 + 2) - 6 = 26$  and  $2(6 - 3) + 20 = 26$"],
                            gloss="each side first, then take 2x", answer="x = 6"),
             yt_check=("many", solves("4*(u + 2) - u", "2*(u - 3) + 20", "6"), same("4*(u + 2) - u", "3*u + 8"), same("2*(u - 3) + 20", "2*u + 14"),
                       solves("4*u + 2 - u", "2*(u - 3) + 20", "12"))),
        dict(title="Example 2", sub="A fraction in front of the parentheses.", min_q=1,
             note_q="Ask what three-fourths of 8x is, and what three-fourths of −4 is, before anyone writes.",
             prompt=["$\\frac{3}{4}(8x - 4) = 2x + 9$"], ask="Solve it, then check in both sides.",
             worked=[dict(sub="Worked.", min=2,
                          note="Three-fourths of 8x is 6x; three-fourths of −4 is −3 — every term inside, as with a whole number. Then take 2x from both sides: 4x − 3 = 9, so 4x = 12 and x = 3. Check: three-fourths of 20 is 15, and 2(3) + 9 = 15. A board with x = 3.25 wrote 6x − 4 (the fraction to one term only); one with x = 1.5 wrote 6x + 3 (the sign).",
                          rows=[("\\frac{3}{4}(8x - 4) = 2x + 9", "the equation"),
                                ("6x - 3 = 2x + 9", "3/4 of 8x is 6x; 3/4 of −4 is −3"),
                                ("4x - 3 = 9", "take 2x from both sides"),
                                ("4x = 12 \\qquad x = 3", "add 3; divide by 4"),
                                ("\\text{Check: } \\frac{3}{4}(20) = 15 \\quad 2(3) + 9 = 15", "both sides of the first equation")],
                          answer="x = 3")],
             check=("many", solves("F(3,4)*(8*u - 4)", "2*u + 9", "3"), same("F(3,4)*(8*u - 4)", "6*u - 3"),
                    solves("4*u - 3", "9", "3"), solves("4*u", "12", "3"), ("eq", "F(3,4)*(8*3 - 4)", "15"), ("eq", "2*3 + 9", "15"),
                    solves("6*u - 4", "2*u + 9", "F(13,4)"), solves("6*u + 3", "2*u + 9", "F(3,2)")),
             your_turn=dict(min=2, note="Two-thirds of 9x is 6x and two-thirds of −6 is −4: 6x − 4 = 2x + 12. Take 2x: 4x − 4 = 12, so 4x = 16 and x = 4. Check: two-thirds of 30 is 20, and 2(4) + 12 = 20. A board with x = 4.5 wrote 6x − 6 (the two-thirds never reached the 6).",
                            prompt=["$\\frac{2}{3}(9x - 6) = 2x + 12$", "Solve it, then check in both sides."],
                            steps=["Distribute:  $\\frac{2}{3}(9x - 6) = 6x - 4$",
                                   "Take 2x from both sides:  $4x - 4 = 12$,  so  $4x = 16$,  $x = 4$",
                                   "Check:  $\\frac{2}{3}(30) = 20$  and  $2(4) + 12 = 20$"],
                            gloss="distribute the fraction, take 2x", answer="x = 4"),
             yt_check=("many", solves("F(2,3)*(9*u - 6)", "2*u + 12", "4"), same("F(2,3)*(9*u - 6)", "6*u - 4"),
                       solves("6*u - 6", "2*u + 12", "F(9,2)"))),
    ],

    # The round: whole numbers, distribute and collect on one side (1), a fraction distributed (2), a decimal
    # distributed (3, the 21% skill), the diagnostic on a negative factor (4), clearing fractions with a common
    # denominator (5), the three endings with a fraction — an identity (6), the rental story with an extra number (7),
    # backwards (8), and a decimal solved and checked in writing (9). The pattern breaks at 6: everything cancels.
    whiteboard=[
        dict(latex="5(x - 2) + 3 = 2x + 11",
             hint="Distribute, then collect.", steps=["Distribute and collect:  $5(x - 2) + 3 = 5x - 7$",
                                                      "Take 2x from both sides:  $3x - 7 = 11$",
                                                      "Add 7, then divide by 3:  $3x = 18$,  $x = 6$"],
             gloss="5x − 7 = 2x + 11", answer="x = 6",
             note="Notes I's order with whole numbers. A board with x = 10/3 wrote 5x − 2 (the 5 to one term only); one with x = −2/3 wrote 5x + 10 (the sign). Check: 5(4) + 3 = 23 and 2(6) + 11 = 23.",
             check=("many", solves("5*(u - 2) + 3", "2*u + 11", "6"), solves("5*u - 2 + 3", "2*u + 11", "F(10,3)"), solves("5*u + 10 + 3", "2*u + 11", "F(-2,3)")),
             wrong="x = 10/3 ≈ 3.33 — 5x − 2 + 3, the 5 to one term only [Florida B1G-M, AR.2.1: distributing to only one term]; x = −2/3 — 5x + 10 + 3, 5(−2) taken as +10 [Florida B1G-M, AR.2.1: sign errors while distributing]"),
        dict(latex="\\frac{1}{2}(10x + 8) = 3x + 14",
             hint="Half of every term.", steps=["Distribute:  $\\frac{1}{2}(10x + 8) = 5x + 4$",
                                                "Take 3x from both sides:  $2x + 4 = 14$",
                                                "Subtract 4, then divide by 2:  $2x = 10$,  $x = 5$"],
             gloss="5x + 4 = 3x + 14", answer="x = 5",
             note="Notes II's first way: half of 10x is 5x and half of 8 is 4. A board with x = 3 wrote 5x + 8 (the half to one term only); one with x = 9 took the 4 the wrong way (2x = 18). Check: half of 58 is 29, and 3(5) + 14 = 29.",
             check=("many", solves("F(1,2)*(10*u + 8)", "3*u + 14", "5"), solves("5*u + 8", "3*u + 14", "3"), solves("2*u", "14 + 4", "9")),
             wrong="x = 3 — 5x + 8 = 3x + 14, the half to one term only [Florida B1G-M, AR.2.1: distributing to only one term]; x = 9 — 2x = 14 + 4, the 4 added instead of subtracted [Notes I: undo + 4 by subtracting 4]"),
        dict(latex="0.4(5x - 10) = x + 3",
             hint="The decimal multiplies both terms.", steps=["Distribute:  $0.4(5x - 10) = 2x - 4$",
                                                               "Take x from both sides:  $x - 4 = 3$",
                                                               "Add 4:  $x = 7$"],
             gloss="2x − 4 = x + 3", answer="x = 7",
             note="Notes III with new numbers — the 21% skill. 0.4 of 5x is 2x and 0.4 of −10 is −4. A board with x = 13 wrote 2x − 10 (the decimal to one term only — the state's most common miss); one with x = −1 wrote 2x + 4 (the sign). Check: 0.4(25) = 10 and 7 + 3 = 10.",
             check=("many", solves("F(2,5)*(5*u - 10)", "u + 3", "7"), solves("2*u - 10", "u + 3", "13"), solves("2*u + 4", "u + 3", "-1")),
             wrong="x = 13 — 2x − 10 = x + 3, the 0.4 to one term only [Florida B1G-M, AR.2.1: distributing to only one term]; x = −1 — 2x + 4 = x + 3, 0.4(−10) taken as +4 [Florida B1G-M, AR.2.1: sign errors while distributing]"),
        dict(kind="mc", latex="-2(3x - 5) = 4x - 30",
             qtext="Solve −2(3x − 5) = 4x − 30.",
             hint="The −2 multiplies both terms.", steps=["Distribute the −2:  $-2(3x - 5) = -6x + 10$",
                                                          "Add 6x to both sides:  $10 = 10x - 30$",
                                                          "Add 30, then divide by 10:  $40 = 10x$,  $x = 4$"],
             choices=["x = 4", "x = −20", "x = 2.5", "x = 2"], correct=0, answer="A — x = 4",
             errors={"B": "the −6x carried to the right side with its sign unchanged: 10 = 4x − 6x − 30, so −2x = 40 [Notes I: move a term by doing the same to both sides]", "C": "the −2 never reached the −5: −6x − 5 = 4x − 30, so −10x = −25 [Florida B1G-M, AR.2.1: distributing to only one term]", "D": "(−2)(−5) taken as −10: −6x − 10 = 4x − 30, so −10x = −20 [Florida B1G-M, AR.2.1: sign errors while distributing]"},
             note="Diagnostic. Option D is the sign, option C the one-term distribution, option B a term carried across the equals sign without its sign changing. On a split: sixty seconds to think again, re-vote — then check 4 in both sides: −2(12 − 5) = −14 and 16 − 30 = −14.",
             check=("many", solves("-2*(3*u - 5)", "4*u - 30", "4"),
                    solves("-6*u - 10", "4*u - 30", "2"), solves("-6*u - 5", "4*u - 30", "F(5,2)"), solves("10", "4*u - 6*u - 30", "-20"))),
        dict(latex="\\frac{x}{3} - 1 = \\frac{x}{5} + 1",
             hint="Thirds and fifths: multiply by 15.", steps=["Multiply both sides by 15:  $15\\left(\\frac{x}{3} - 1\\right) = 5x - 15$  and  $15\\left(\\frac{x}{5} + 1\\right) = 3x + 15$",
                                                               "Take 3x from both sides:  $2x - 15 = 15$",
                                                               "Add 15, then divide by 2:  $2x = 30$,  $x = 15$"],
             gloss="5x − 15 = 3x + 15", answer="x = 15",
             note="Notes II's second way: thirds and fifths clear with 15, and the 15 multiplies every term — the 1s as well. A board with x = 1 multiplied only the fractions (5x − 1 = 3x + 1); one stuck at 2x = 30 wrote the answer before dividing. Check: 15/3 − 1 = 4 and 15/5 + 1 = 4.",
             check=("many", solves("u/3 - 1", "u/5 + 1", "15"), same("15*(u/3 - 1)", "5*u - 15"), same("15*(u/5 + 1)", "3*u + 15"),
                    solves("5*u - 1", "3*u + 1", "1")),
             wrong="x = 1 — 5x − 1 = 3x + 1, the 15 to the fractions only [Florida B1G-M, AR.2.1: distributing to only one term]"),
        dict(kind="mc", text=["$\\frac{1}{2}(6x - 4) = 3(x - 1) + 1$", "**How many solutions does it have?"],
             qtext="How many solutions does ½(6x − 4) = 3(x − 1) + 1 have?",
             hint="Simplify each side, then compare.", steps=["Left:  $\\frac{1}{2}(6x - 4) = 3x - 2$.   Right:  $3(x - 1) + 1 = 3x - 2$",
                                                              "Take 3x from both sides:  $-2 = -2$,  always true"],
             choices=["no solution", "one solution, x = −2", "infinitely many solutions", "one solution, x = 0"], correct=2,
             answer="C — infinitely many solutions",
             errors={"A": "the 3 to the first term only: 3x − 1 + 1 = 3x, so 3x − 2 = 3x ends −2 = 0 [Florida B1G-M, AR.2.1: distributing to only one term]", "B": "the constant in −2 = −2 taken for the answer [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]", "D": "0 = 0 (taking 3x − 2 from both sides) read as x = 0 [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]"},
             note="Diagnostic, and 11.03's endings with a fraction. Both sides are 3x − 2, so every number works. Option A distributed the 3 to one term and found 'no solution' — ask what 3 times −1 is. Options D and B read the true ending as an x. On a split: sixty seconds to think again, re-vote.",
             check=("many", same("F(1,2)*(6*u - 4)", "3*(u - 1) + 1"), not_never("F(1,2)*(6*u - 4)", "3*(u - 1) + 1"),
                    never("F(1,2)*(6*u - 4)", "3*u - 1 + 1"))),
        dict(text=["Shop A rents a bike for \\$12 plus \\$4.50 an hour.", "Shop B, 3 blocks away, charges \\$7.50 an hour.",
                   "**For how many hours do the two shops cost the same?"],
             unneeded="3",
             steps=["Shop A costs  $12 + 4.5h$.   Shop B costs  $7.5h$.",
                    "Take 4.5h from both:  $12 = 3h$,  so  $h = 4$",
                    "Check:  $12 + 4.5(4) = 30$  and  $7.5(4) = 30$"],
             gloss="12 + 4.5h = 7.5h", answer="4 hours",
             note="The extra-number board (ruling 22): Shop B's 3 blocks are not needed. Each shop's cost is an expression in h; they cost the same when the expressions are equal, 12 + 4.5h = 7.5h. Take 4.5h (the smaller) from both sides. Check: both cost \\$30 for 4 hours.",
             check=("many", solves("12 + F(9,2)*u", "F(15,2)*u", "4"), ("eq", "12 + F(9,2)*4", "30"), ("eq", "F(15,2)*4", "30"),
                    solves("12", "(F(9,2) + F(15,2))*u", "1"), solves("12", "F(15,2)*u", "F(8,5)")),
             wrong="1 hour — 12 = 12h, the two hourly rates added [Notes I: take the same term from both sides]; 1.6 hours — 12 ÷ 7.5, Shop A's \\$4.50 an hour left out [both shops' costs are equal]; '3' — the extra number used"),
        dict(text=["$x = 2$ is the solution of  $3(x + □) = 2x + 20$.", "**What number goes in the box?"],
             hint="Put 2 in for x.", steps=["Put 2 in for x:  $2(2) + 20 = 24$,  so  $3(2 + □) = 24$",
                                            "$24 \\div 3 = 8$,  and  $8 - 2 = 6$"],
             gloss="3(2 + 6) = 24", answer="6",
             note="Backwards: the solution is given and a number in the equation is missing. Put 2 in for x on BOTH sides — the right is 24, so 2 + □ must be 8. Check: 3(2 + 6) = 24 and 2(2) + 20 = 24.",
             check=("many", solves("3*(2 + u)", "2*2 + 20", "6"), solves("3*(u + 6)", "2*u + 20", "2"), solves("3*2 + u", "2*2 + 20", "18")),
             wrong="8 — the value of 2 + □, one step short [the box is what is added to 2]; 18 — 6 + □ = 24, the 3 to the first term only [Florida B1G-M, AR.2.1: distributing to only one term]"),
        dict(kind="written", text=["Solve  $1.5(4x - 2) + x = 2(x + 6)$.", "**Then check your solution in both sides."],
             qtext="Solve 1.5(4x − 2) + x = 2(x + 6). Then check your solution in both sides.",
             hint="Each side first.", steps=["Left:  $1.5(4x - 2) + x = 7x - 3$",
                                             "Right:  $2(x + 6) = 2x + 12$",
                                             "Take 2x, then add 3:  $5x = 15$,  $x = 3$",
                                             "Check:  $1.5(4 \\cdot 3 - 2) + 3 = 18$  and  $2(3 + 6) = 18$"],
             gloss="7x − 3 = 2x + 12", answer="x = 3; both sides are 18",
             te_answer="Full credit: x = 3 from a correct line (7x − 3 = 2x + 12, so 5x = 15) AND the check in both sides of the first equation — 1.5(10) + 3 = 18 and 2(9) = 18. x = 3 with no check, or a check in a later line, does not earn it. A board with 6x − 2 + x has distributed the 1.5 to one term (x = 2.8, and its check fails: 16.6 against 17.6).",
             note="Written, and the exit evidence. Read two aloud: one that distributes the 1.5 to both terms and checks in the first equation, and one whose check caught its own slip. The decimal is the 21% skill; the check is what proves the answer.",
             check=("many", solves("F(3,2)*(4*u - 2) + u", "2*(u + 6)", "3"), same("F(3,2)*(4*u - 2) + u", "7*u - 3"), same("2*(u + 6)", "2*u + 12"),
                    ("eq", "F(3,2)*(4*3 - 2) + 3", "18"), ("eq", "2*(3 + 6)", "18"),
                    solves("6*u - 2 + u", "2*u + 12", "F(14,5)"), ("eq", "F(3,2)*(4*F(14,5) - 2) + F(14,5)", "F(83,5)"), ("eq", "2*(F(14,5) + 6)", "F(88,5)")),
             wrong="x = 2.8 — 6x − 2 + x, the 1.5 to one term only [Florida B1G-M, AR.2.1: distributing to only one term]; x = 3 with the check in 7x − 3 = 2x + 12 — a later line, not the first equation [Notes I: check in both sides of the first equation]"),
    ],

    independent=[
        dict(stem="Solve:  $4(2w - 3) - 2w = 3(w + 1) + 9$", answer="w = 8",
             why="Left: 8w − 12 − 2w = 6w − 12. Right: 3w + 3 + 9 = 3w + 12. Take 3w: 3w − 12 = 12; 3w = 24. Check: 36 = 36.",
             check=("many", solves("4*(2*u - 3) - 2*u", "3*(u + 1) + 9", "8"), ("eq", "4*(2*8 - 3) - 2*8", "36"), ("eq", "3*(8 + 1) + 9", "36")), space=1.0),
        dict(stem="Solve:  $\\frac{2}{5}(10n - 5) = 3n + 4$", answer="n = 6",
             why="Two-fifths of 10n is 4n; two-fifths of −5 is −2. 4n − 2 = 3n + 4; n = 6. Check: 22 = 22.",
             check=("many", solves("F(2,5)*(10*u - 5)", "3*u + 4", "6"), ("eq", "F(2,5)*(10*6 - 5)", "22"), ("eq", "3*6 + 4", "22")), space=1.0),
        dict(stem="Solve:  $\\frac{m}{2} - 3 = \\frac{m}{5} + 3$", answer="m = 20",
             why="Multiply both sides by 10 (every term): 5m − 30 = 2m + 30; 3m = 60. Check: 7 = 7.",
             check=("many", solves("u/2 - 3", "u/5 + 3", "20"), same("10*(u/2 - 3)", "5*u - 30"), same("10*(u/5 + 3)", "2*u + 30")), space=1.0),
        dict(stem="Solve:  $-2.5(2k - 4) = k - 8$", answer="k = 3",
             why="The −2.5 multiplies both terms: −5k + 10 = k − 8; 18 = 6k. Check: −2.5(2) = −5 and 3 − 8 = −5.",
             check=("many", solves("-F(5,2)*(2*u - 4)", "u - 8", "3"), same("-F(5,2)*(2*u - 4)", "-5*u + 10"), ("eq", "-F(5,2)*(2*3 - 4)", "-5")), space=1.0),
        dict(stem="How many solutions does  $\\frac{1}{4}(8v + 12) = 2v - 1$  have? If one, find it.", answer="No solution",
             why="2v + 3 = 2v − 1; take 2v from both sides: 3 = −1, never true.",
             check=never("F(1,4)*(8*u + 12)", "2*u - 1"), space=1.0),
        dict(stem="A kayak rental costs \\$15 plus \\$6.50 an hour. A second shop charges \\$9 an hour. For how many hours do the two cost the same?",
             answer="6 hours", why="15 + 6.5h = 9h; 15 = 2.5h. Check: both cost \\$54.",
             check=("many", solves("15 + F(13,2)*u", "9*u", "6"), ("eq", "15 + F(13,2)*6", "54"), ("eq", "9*6", "54")), space=1.0),
    ],

    # Bank: whole-number multi-step (1–3: one side's parentheses, both sides', a subtracted group), fractions (4–6:
    # two distributed, one cleared by a common denominator), decimals (7–8, the 21% skill: a positive factor, a
    # negative one), backwards (9), a rental story (10), the diagnostic mc on a decimal (11), select-all on the
    # endings with fraction and decimal coefficients (12). The additional bank mirrors it position by position.
    bank=[
        dict(heading="For questions 1 through 3, solve the equation."),
        dict(stem="$2(4p - 1) + 3 = 5p + 13$", answer="p = 4", why="8p + 1 = 5p + 13; 3p = 12. Check: 33 = 33.", check=solves("2*(4*u - 1) + 3", "5*u + 13", "4"), space=0.8),
        dict(stem="$6(m + 1) - 2m = 3(m + 4)$", answer="m = 6", why="4m + 6 = 3m + 12. Check: 30 = 30.", check=solves("6*(u + 1) - 2*u", "3*(u + 4)", "6"), space=0.8),
        dict(stem="$5q - 2(q + 3) = 4(q - 4)$", answer="q = 10", why="5q − 2q − 6 = 3q − 6; 3q − 6 = 4q − 16; 10 = q. Check: 24 = 24.", check=solves("5*u - 2*(u + 3)", "4*(u - 4)", "10"), space=0.8),
        dict(heading="For questions 4 through 6, the equation has fractions. Solve it."),
        dict(stem="$\\frac{1}{2}(6y + 10) = 2y + 9$", answer="y = 4", why="3y + 5 = 2y + 9. Check: 17 = 17.", check=solves("F(1,2)*(6*u + 10)", "2*u + 9", "4"), space=0.8),
        dict(stem="$\\frac{2}{3}(6r - 9) = 3r + 2$", answer="r = 8", why="4r − 6 = 3r + 2. Check: 26 = 26.", check=solves("F(2,3)*(6*u - 9)", "3*u + 2", "8"), space=0.8),
        dict(stem="$\\frac{z}{3} + 4 = \\frac{z}{4} + 6$", answer="z = 24", why="Multiply both sides by 12: 4z + 48 = 3z + 72. Check: 12 = 12.", check=solves("u/3 + 4", "u/4 + 6", "24"), space=0.8),
        dict(heading="For questions 7 and 8, the factor is a decimal. Solve the equation."),
        dict(stem="$0.2(15t + 10) = t + 12$", answer="t = 5", why="3t + 2 = t + 12; 2t = 10. Check: 17 = 17.", check=solves("F(1,5)*(15*u + 10)", "u + 12", "5"), space=0.8),
        dict(stem="$-0.5(4k + 6) = k - 12$", answer="k = 3", why="−2k − 3 = k − 12; 9 = 3k. Check: −9 = −9.", check=solves("-F(1,2)*(4*u + 6)", "u - 12", "3"), space=0.8),
        dict(heading="Work backwards."),
        dict(stem="$x = 4$ is the solution of $3(x + □) = x + 26$. What number goes in the box?", answer="6", why="3(4 + □) = 30; 4 + □ = 10.",
             check=("many", solves("3*(4 + u)", "4 + 26", "6"), solves("3*(u + 6)", "u + 26", "4")), space=0.8),
        dict(heading="Solve the problem."),
        dict(stem="Boat rental A costs \\$20 plus \\$5.50 an hour. Boat rental B costs \\$8 an hour. For how many hours do the two rentals cost the same?",
             answer="8 hours", why="20 + 5.5h = 8h; 20 = 2.5h. Both cost \\$64.", check=solves("20 + F(11,2)*u", "8*u", "8"), space=0.8),
        dict(heading="Choose one."),
        dict(stem="Solve:  $1.5(2x - 4) = x + 8$", choices=["$x = 3.5$", "$x = 1$", "$x = 6$", "$x = 7$"], correct=3, answer="D",
             why="3x − 6 = x + 8; 2x = 14.",
             check=("many", solves("F(3,2)*(2*u - 4)", "u + 8", "7"), solves("3*u - 4", "u + 8", "6"),
                    solves("3*u + 6", "u + 8", "1"), solves("3*u + u - 6", "8", "F(7,2)")),
             errors={"A": "the x-terms added: 4x − 6 = 8 [Notes I: take the same term from both sides]", "B": "1.5(−4) taken as +6: 3x + 6 = x + 8 [Florida B1G-M, AR.2.1: sign errors while distributing]", "C": "the 1.5 to the first term only: 3x − 4 = x + 8 [Florida B1G-M, AR.2.1: distributing to only one term]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the equations that have no solution.",
             choices=["$0.5(2x + 4) = x$", "$\\frac{1}{3}(3x - 9) = 2x - 3$", "$\\frac{1}{2}(4x + 6) = 2x + 6$", "$\\frac{1}{2}(4x + 6) = 2x + 3$", "$\\frac{1}{3}(3x - 9) = x + 3$"],
             correct=[0, 2, 4], answer="A, C, E",
             why="A ends 2 = 0, C ends 3 = 6 and E ends −3 = 3, never true. D is the same on both sides (infinitely many); B has one solution, x = 0.",
             check=("many", never("F(1,2)*(4*u + 6)", "2*u + 6"), never("F(1,3)*(3*u - 9)", "u + 3"), never("F(1,2)*(2*u + 4)", "u"),
                    not_never("F(1,2)*(4*u + 6)", "2*u + 3"), not_never("F(1,3)*(3*u - 9)", "2*u - 3"),
                    same("F(1,2)*(4*u + 6)", "2*u + 3"), solves("F(1,3)*(3*u - 9)", "2*u - 3", "0")),
             errors={"B": "x − 3 = 2x − 3 has one solution, x = 0 [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]", "D": "both sides are 2x + 3: infinitely many [Notes II: the fraction multiplies every term]"}),
    ],

    additional=[
        dict(heading="For questions 1 through 3, solve the equation."),
        dict(stem="$3(2p + 1) - 4 = 4p + 9$", answer="p = 5", why="6p − 1 = 4p + 9; 2p = 10. Check: 29 = 29.", check=solves("3*(2*u + 1) - 4", "4*u + 9", "5"), space=0.8),
        dict(stem="$5(m - 1) + m = 4(m + 2) + 1$", answer="m = 7", why="6m − 5 = 4m + 9; 2m = 14. Check: 37 = 37.", check=solves("5*(u - 1) + u", "4*(u + 2) + 1", "7"), space=0.8),
        dict(stem="$7q - 3(q - 2) = 5(q - 1)$", answer="q = 11", why="7q − 3q + 6 = 4q + 6; 4q + 6 = 5q − 5; 11 = q. Check: 50 = 50.", check=solves("7*u - 3*(u - 2)", "5*(u - 1)", "11"), space=0.8),
        dict(heading="For questions 4 through 6, the equation has fractions. Solve it."),
        dict(stem="$\\frac{1}{2}(8y - 6) = 3y + 4$", answer="y = 7", why="4y − 3 = 3y + 4. Check: 25 = 25.", check=solves("F(1,2)*(8*u - 6)", "3*u + 4", "7"), space=0.8),
        dict(stem="$\\frac{3}{4}(4r + 8) = 2r + 10$", answer="r = 4", why="3r + 6 = 2r + 10. Check: 18 = 18.", check=solves("F(3,4)*(4*u + 8)", "2*u + 10", "4"), space=0.8),
        dict(stem="$\\frac{z}{2} + 1 = \\frac{z}{3} + 4$", answer="z = 18", why="Multiply both sides by 6: 3z + 6 = 2z + 24. Check: 10 = 10.", check=solves("u/2 + 1", "u/3 + 4", "18"), space=0.8),
        dict(heading="For questions 7 and 8, the factor is a decimal. Solve the equation."),
        dict(stem="$0.4(10t - 5) = t + 7$", answer="t = 3", why="4t − 2 = t + 7; 3t = 9. Check: 10 = 10.", check=solves("F(2,5)*(10*u - 5)", "u + 7", "3"), space=0.8),
        dict(stem="$-0.5(6k - 4) = 2k - 18$", answer="k = 4", why="−3k + 2 = 2k − 18; 20 = 5k. Check: −10 = −10.", check=solves("-F(1,2)*(6*u - 4)", "2*u - 18", "4"), space=0.8),
        dict(heading="Work backwards."),
        dict(stem="$x = 3$ is the solution of $4(x + □) = 2x + 26$. What number goes in the box?", answer="5", why="4(3 + □) = 32; 3 + □ = 8.",
             check=("many", solves("4*(3 + u)", "2*3 + 26", "5"), solves("4*(u + 5)", "2*u + 26", "3")), space=0.8),
        dict(heading="Solve the problem."),
        dict(stem="Scooter rental A costs \\$10 plus \\$3.50 an hour. Scooter rental B costs \\$6 an hour. For how many hours do the two rentals cost the same?",
             answer="4 hours", why="10 + 3.5h = 6h; 10 = 2.5h. Both cost \\$24.", check=solves("10 + F(7,2)*u", "6*u", "4"), space=0.8),
        dict(heading="Choose one."),
        dict(stem="Solve:  $2.5(2x - 4) = x + 6$", choices=["$x = \\frac{8}{3}$", "$x = 4$", "$x = 2.5$", "$x = -1$"], correct=1, answer="B",
             why="5x − 10 = x + 6; 4x = 16.",
             check=("many", solves("F(5,2)*(2*u - 4)", "u + 6", "4"), solves("5*u - 4", "u + 6", "F(5,2)"),
                    solves("5*u + 10", "u + 6", "-1"), solves("5*u + u - 10", "6", "F(8,3)")),
             errors={"A": "the x-terms added: 6x − 10 = 6 [Notes I: take the same term from both sides]", "C": "the 2.5 to the first term only: 5x − 4 = x + 6 [Florida B1G-M, AR.2.1: distributing to only one term]", "D": "2.5(−4) taken as +10: 5x + 10 = x + 6 [Florida B1G-M, AR.2.1: sign errors while distributing]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the equations that have infinitely many solutions.",
             choices=["$\\frac{1}{2}(6x - 2) = 3x - 1$", "$\\frac{1}{2}(6x - 2) = 3x - 2$", "$\\frac{1}{4}(8x + 4) = x + 1$", "$\\frac{1}{4}(8x + 4) = 2x + 1$", "$0.5(4x - 2) = 2x - 1$"],
             correct=[0, 3, 4], answer="A, D, E",
             why="A, D and E are the same on both sides. B ends −1 = −2, never true; C has one solution, x = 0.",
             check=("many", same("F(1,2)*(6*u - 2)", "3*u - 1"), same("F(1,4)*(8*u + 4)", "2*u + 1"), same("F(1,2)*(4*u - 2)", "2*u - 1"),
                    not_every("F(1,2)*(6*u - 2)", "3*u - 2"), not_every("F(1,4)*(8*u + 4)", "u + 1"),
                    never("F(1,2)*(6*u - 2)", "3*u - 2"), solves("F(1,4)*(8*u + 4)", "u + 1", "0")),
             errors={"B": "the x-terms match, but the constants do not: −1 = −2, no solution [11.03 Notes II: the constants must match too]", "C": "2x + 1 = x + 1 has one solution, x = 0 [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]"}),
    ],

    te=dict(
        say=["Distribute, collect each side, move the x-terms one way and the constants the other, divide — then check in both sides.",
             "A fraction or a decimal outside the parentheses multiplies every term inside, just as a whole number does.",
             "To clear fractions, multiply every term on both sides by a common denominator."],
        must="Solve multi-step linear equations with rational (fraction and decimal) coefficients and variables on both sides; verify by substitution (B1G-M).",
        must_not="Writing the equation from a context (MA.912.AR.2.1); systems (11.05).",
        read_first=[
            "The unit's fourth day, after a day with no class (Thu 3 Dec). Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §11.04), then read against Math Nation 11.4 (the unit audit, Part 1). The moves are the last three days'; the new content is the benchmark's 'rational number coefficients' — a fraction distributed, fractions cleared by a common denominator, a decimal distributed.",
            "The decimal distribution is the lowest-scoring released Grade 8 FAST skill (21%): it has Notes III, board 3, board 9 and set question 4, which distributes a negative decimal (−2.5) — the audit's §4 gap; the state's item distributes −3.5.",
            "Every multiple-choice wrong option is one of the B1G-M's named AR.2.1 errors — distributing to only one term, a sign error while distributing, expecting variable = constant — or a named slip (a term carried across the equals sign with its sign unchanged; the x-terms added). A false ending is written as the false equation with its words, never as '≠'; on an answer slide it is said in words because the build's step check holds every printed equation true.",
            "Not reproduced from the book: the 11.4.1 game-statistics warm-up (no AR.2.1 content); Clare's error analysis, whose stem says 'a mistake' over two (D7); the 11.4.3 card sort, whose cards were never supplied (D11, T8) and whose card K work line has both signs wrong (D8); PP #10, whose student page and key are different equations (D6 — here each item's key is worked from the very equation printed); the key lines with wrong constants, '10 ≠ 3' and '0.8 ≠ 1.8' (D9, D10); the partner work."],
        standard_notes=[("Clarification", "Problem types include equations that generate one solution, infinitely many solutions or no solution (Clarification 1) — today mostly one solution with rational coefficients; board 6 and set question 5 bring back the other two endings."),
                        ("Unit boundary", "Fraction and decimal coefficients, positive and negative; parentheses on either or both sides; whole and negative solutions. Solution forms x = a, a = a, a = b (B1G-M); one-solution answers verified by substitution in both sides.")],
        sits="The unit's fourth day and the last of its equations before systems. IXL 55K, PGH and HZZ are done today and due by the Unit 11 test (Fri 11 Dec), whose questions 1–4 are today's kinds — question 4 distributes a decimal. 11.05 starts systems: a pair of values that makes two equations true.",
        lives="Notes II — distribute the fraction, or clear it — and Notes III — the decimal multiplies both terms. Board 3 is the 21% skill; board 4 the diagnostic on a negative factor (sign, one term, a term carried across); board 6 the endings with a fraction; board 9 a decimal solved and checked in writing.",
        materials="Whiteboards and markers. The Independent Set, one per student.",
        variation="Board 1 is Notes I's order with whole numbers; 2 distributes a fraction; 3 a decimal (the 21% skill); 4 votes on a negative factor. 5 clears fractions with a common denominator. The pattern breaks at 6: a fraction distributed and everything cancels — infinitely many. 7 is the rental story with Shop B's 3 blocks as the extra number; 8 runs backwards; 9 distributes a decimal and checks in writing. The independent set walks the same path in six: whole numbers on both sides, a fraction distributed, a common denominator, a negative decimal distributed, an ending with a fraction (no solution) and a rental story.",
        audit=["Every equation re-derived by sympy at build time over the real numbers (mathcheck: 0 findings); every worked row of the examples checked to have the first equation's solution, and every check row computed; every multiple-choice distractor and every wrong answer named in a note solved again from its named error.",
               "Math Nation 11.4 read against this lesson (A7 Unit 11 Audit, Part 1 §1–§5): D6–D11 and T1 not reproduced — no key here is worked from a different equation than its student page (D6); every printed work line is re-derived, so none carries a wrong constant (D8–D10, and T1's halving: Notes II multiplies every term by 6 and the build checks it); no stem miscounts its errors (D7); no activity depends on missing materials (D11). The audit's §4 gaps met today: a negative rational factor distributed (set 4, bank 8, additional 8), a fraction in a no-solution equation (set 5, bank 12), fractions cleared by multiplying (Notes II, board 5, set 3), substitution in both sides on every item."],
        changes=["11.4.1 game-statistics warm-up → four retrieval questions, the prerequisite (two-thirds of 9) in the last slot.",
                 "11.4.2 Clare's error analysis (two errors, 'a mistake') → board 4's options, each a named error, and board 9's check.",
                 "11.4.3 card sort in pairs (no cards supplied) → Notes I–III and boards 1–6, taught from the front; the endings with fractions are board 6 and set question 5.",
                 "PP and HW pages 7–8 (solve eight, none checked) → the Independent Set, every answer checked in both sides."],
    ),
)
