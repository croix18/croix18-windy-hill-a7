# A7 11.04  Multi-Step Equations — MA.8.AR.2.1 (MN 11.4). Fri 4 Dec 2026, a 53-minute period (Thursday 3 Dec is
# a spiral day with no deck, so the last lesson is Wednesday's 11.03). The benchmark's words "with rational number coefficients" are
# today's content: a fraction distributed (it multiplies every term inside, like a whole number), both sides
# multiplied by a common denominator (every term, the constants too), and a decimal distributed — the lowest-scoring
# released Grade 8 FAST skill (21%), so it gets Notes III (the state's shape, −2.4(5x − 3) = −40.8), Example 1, boards 3
# and 4 and its own set question, with negative decimal factors (the audit's §4 gap: the state item is −3.5(10x − 2) =
# −176.75). One order for every equation, and a
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
    align="=",   # every run of rows that solve an equation set with its equals signs in one column (kit, 15 Nov 2026)
    title="Multi-Step Equations",
    unit_title="Solving Equations and Systems",
    benchmark="MA.8.AR.2.1",
    benchmark_text="Solve multi-step linear equations in one variable, with rational number coefficients. Include equations with variables on both sides.",
    target="I can solve a multi-step equation with fraction or decimal coefficients and check it.",
    yesterday="Last class: one solution, no solution or infinitely many.",
    today="Today: multi-step equations with fractions and decimals.",
    essential="Why does a fraction or a decimal in front of parentheses follow the same rule as a whole number — and why must every term be multiplied when we clear fractions?",
    building_on="Lesson 11.01 collected like terms and distributed. Lesson 11.02 solved equations with the variable on both sides. Lesson 11.03 sorted equations by their number of solutions. Unit 4 covered arithmetic with fractions and decimals.",
    working_toward="Question 4 of the Unit 11 test (Friday 11 December) distributes a decimal. In Lessons 11.05–11.08, both equations of a system give the same y at the point where their lines cross. In Algebra 1 (MA.912.AR.2.1), students write the equation from a context themselves.",
    vocab=[("common denominator", "a number that every denominator divides evenly: 6 is a common denominator of $\\frac{x}{2}$ and $\\frac{x}{3}$"),
           ("rational coefficient", "a coefficient that is a fraction or a decimal, like $\\frac{1}{3}$ in $\\frac{1}{3}x$ or $0.5$ in $0.5x$")],
    vocab_note="Two words for today's numbers. A common denominator is the number that clears every fraction at once — 6 for halves and thirds, 15 for thirds and fifths. A rational coefficient is just a fraction or a decimal in front of the variable; the moves of the last three days do not change.",
    ixl=["Solve multi-step equations — 55K", "Solve multi-step equations: complete the solution — PGH", "Solve equations: mixed review — HZZ"],
    closure="Whiteboard question 9 is answered in writing and serves as the exit ticket. A complete answer simplifies the left side, 1.5(4x − 2) + x, to 7x − 3 and the right side to 2x + 12, so 5x = 15 and x = 3. It then checks 3 in both sides of the first equation: 1.5(10) + 3 = 18 and 2(9) = 18. An answer of x = 3 with no check is only half complete.",

    mtr=[("MTR.3.1", "On whiteboard questions 1–5, students follow one order for every equation: distribute, collect like terms, take the same variable term from both sides, isolate the variable and check."),
         ("MTR.4.1", "On whiteboard questions 4 and 6, a divided class has one minute to convince a neighbor and then votes again."),
         ("MTR.6.1", "Students check each solution in both sides of the first equation (whiteboard question 9 and every answer slide).")],
    hoq=[("In x/2 + 3 = x/3 + 5, why must the 3 and the 5 be multiplied by 6 too?", "DOK 2"),
         ("The wrong options of whiteboard question 4 come from three different mistakes. Without solving, how can you show that x = 0.5 is not the solution?", "DOK 3"),
         ("For (1/3)(6x + 9) = x + 7, would you distribute the 1/3 or multiply both sides by 3 first? Do both ways give the same solution? Why?", "DOK 3")],
    differentiation=[
        ("ESE / 504", "Keep the order on display all period as five numbered steps: distribute, collect like terms, take the same variable term from both sides, isolate the variable, check. Draw arrows from the fraction or decimal to each term inside the parentheses. Students draw those arrows on every whiteboard question before they write anything else."),
        ("ELL", "**Distribute**: the number outside multiplies every term inside. **Common denominator**: one number that clears every fraction. **Isolate**: get the variable alone on one side. **Check**: put the solution back into each side. The two values must match."),
        ("Enrichment", "Students who finish whiteboard question 5 early solve x/4 − 2 = x/6 + 1 for x in two ways, multiplying every term by 12 and then by 24. They explain why both ways give x = 36 and which way is less work.")],

    warmup=[
        dict(stem="How many solutions does  $2(x + 3) = 2x + 6$  have?", answer="Infinitely many solutions", band="last lesson",
             source="11.03 — the three endings: both sides are 2x + 6",
             check=same("2*(u + 3)", "2*u + 6")),
        dict(stem="Solve for x:  $9x - 7 = 4x + 18$", answer="x = 5", band="this week",
             source="11.02 — the variable on both sides",
             check=solves("9*u - 7", "4*u + 18", "5")),
        dict(stem="A triangle has sides 5, 9 and x. Between which numbers is x?", answer="Between 4 and 14", band="last unit",
             source="6.01 — the Triangle Inequality: 9 − 5 < third side < 9 + 5",
             check=("true", "9 - 5 == 4 and 9 + 5 == 14")),
        dict(stem="Find  $\\frac{2}{3}$  of 9.", answer="6", band="the prerequisite this lesson needs",
             source="5.02 — a scale factor k multiplies every length (k = ⅔ makes 9 into 6); today's fractions multiply every term inside the parentheses",
             check=("eq", "F(2,3)*9", "6")),
    ],
    warmup_note="Q4 is today's move in miniature: two-thirds of 9 is 6, so two-thirds of 9x is 6x. Say that in one sentence after the reveal — Notes II and board 2 distribute a negative fraction the same way. Two minutes silent, then reveal, no discussion.",

    notes=[
        dict(numeral="I", head="One order for every equation", min=4, sub="Copy all six lines.",
             note="The order of the last three days, every move on its own line: distribute on both sides (6x − 12 + 5 and 2x + 12 + 1); collect each side (6x − 7 and 2x + 13); take 2x from both sides (4x − 7 = 13); add 7 (4x = 20); divide by 4. Check in both sides of the first equation: 3(6) + 5 = 23 and 2(11) + 1 = 23.\nOFF: 'Distribute, collect, take the same term from both sides, divide, check. Every equation, every time.'",
             math=["$3(2x - 4) + 5 = 2(x + 6) + 1$", "$6x - 12 + 5 = 2x + 12 + 1$", "$6x - 7 = 2x + 13$", "$4x - 7 = 13$", "$4x = 20$",
                   "$x = 5 \\qquad \\text{Check: } 3(6) + 5 = 23 \\quad 2(11) + 1 = 23$"],
             letters=False),
        dict(numeral="II", head="A fraction outside: every term, and its sign", min=3, sub="",
             note="The fraction multiplies every term inside, just as a whole number does — and a negative fraction carries its sign to each term, as 11.01's −3 did: (−½)(4x) = −2x and (−½)(−10) = +5. Then add 2x to both sides (the smaller x-term is −2x), add 1, divide by 3. Check: −½(8 − 10) = 1 and 2 − 1 = 1. A board with −2x − 10 sent the fraction to one term; one with −2x − 5 lost the sign. Fractions can also be CLEARED — multiply every term by a common denominator — and that is Example 2.\nOFF: 'A fraction outside the parentheses multiplies every term inside — sign and all.'",
             math=["$-\\frac{1}{2}(4x - 10) = x - 1$", "$-2x + 5 = x - 1$", "$5 = 3x - 1$", "$6 = 3x$", "$x = 2$"],
             letters=False),
        dict(numeral="III", head="Decimals: the decimal multiplies both terms", min=3, sub="",
             note="The state's own shape: a negative decimal outside, a decimal left over. −2.4 times 5x is −12x; −2.4 times −3 is +7.2 — not a whole number, and that is fine. Subtract 7.2 from both sides: −12x = −48. Divide by −12: x = 4. Check: −2.4(20 − 3) = −2.4(17) = −40.8. This is the skill the state scored lowest on its released Grade 8 test — almost four in five students missed it — and the miss is nearly always the decimal never reaching the second term (−12x − 3) or its sign (−12x − 7.2).\nOFF: 'The decimal is a number like any other. It multiplies every term inside, sign and all.'",
             math=["$-2.4(5x - 3) = -40.8$", "$-12x + 7.2 = -40.8$", "$-12x = -48$", "$x = 4$"],
             items2=["$-2.4(-3) = 7.2$      Check:  $-2.4(20 - 3) = -40.8$"],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", sub="A decimal outside, the variable on both sides.", min_q=1,
             note_q="Ask what 0.2 of 10x is, and what 0.2 of −15 is, before anyone writes.",
             prompt=["$0.2(10x - 15) = x + 4$"], ask="Solve for x, then check in both sides.",
             worked=[dict(sub="Worked.", min=2,
                          note="0.2 of 10x is 2x; 0.2 of −15 is −3 — both terms. Take x (the smaller) from both sides: x − 3 = 4. Add 3: x = 7. Check in both sides of the first equation: 0.2(55) = 11 and 7 + 4 = 11. A board with x = 19 wrote 2x − 15 (the decimal to one term only); one with x = 1 wrote 2x + 3 (the sign).",
                          rows=[("0.2(10x - 15) = x + 4", "the equation"),
                                ("2x - 3 = x + 4", "0.2 of 10x is 2x; 0.2 of −15 is −3"),
                                ("x - 3 = 4", "take x from both sides"),
                                ("x = 7", "add 3 to both sides"),
                                ("\\text{Check: } 0.2(70 - 15) = 11 \\quad 7 + 4 = 11", "both sides of the first equation")],
                          answer="x = 7")],
             check=("many", solves("F(1,5)*(10*u - 15)", "u + 4", "7"), same("F(1,5)*(10*u - 15)", "2*u - 3"),
                    solves("u - 3", "4", "7"), ("eq", "F(1,5)*(70 - 15)", "11"), ("eq", "7 + 4", "11"),
                    solves("2*u - 15", "u + 4", "19"), solves("2*u + 3", "u + 4", "1")),
             your_turn=dict(min=2, note="0.6 of 10x is 6x and 0.6 of −5 is −3: 6x − 3 = 4x + 5. Take 4x: 2x − 3 = 5, so 2x = 8 and x = 4. Check: 0.6(35) = 21 and 4(4) + 5 = 21. A board with x = 5 wrote 6x − 5 (the decimal to one term only); one with x = 1 wrote 6x + 3 (the sign).",
                            prompt=["$0.6(10x - 5) = 4x + 5$", "Solve for x, then check in both sides."],
                            steps=["Distribute:  $0.6(10x - 5) = 6x - 3$",
                                   "Take 4x from both sides:  $2x - 3 = 5$",
                                   "Add 3:  $2x = 8$",
                                   "Divide by 2:  $x = 4$",
                                   "Check:  $0.6(40 - 5) = 21$  and  $4(4) + 5 = 21$"],
                            gloss="distribute the decimal, take 4x", answer="x = 4"),
             yt_check=("many", solves("F(3,5)*(10*u - 5)", "4*u + 5", "4"), same("F(3,5)*(10*u - 5)", "6*u - 3"),
                       solves("6*u - 5", "4*u + 5", "5"), solves("6*u + 3", "4*u + 5", "1"))),
        dict(title="Example 2", sub="Clear the fractions with a common denominator.", min_q=1,
             note_q="Ask what number both 2 and 3 divide into, before anyone writes: 6. Then ask which terms the 6 must multiply: all four.",
             prompt=["$\\frac{x}{2} + 3 = \\frac{x}{3} + 5$"], ask="Solve for x, then check in both sides.",
             worked=[dict(sub="Worked: clear the fractions.", min=1,
                          note="Halves and thirds clear with 6. The second line is the one students skip: 6 multiplies EVERY term — the 3 and the 5 as well as the fractions. 6 times x/2 is 3x; 6 times 3 is 18. A board with 3x + 3 = 2x + 5 multiplied only the fractions (x = 2).",
                          rows=[("\\frac{x}{2} + 3 = \\frac{x}{3} + 5", "the equation"),
                                ("6\\left(\\frac{x}{2}\\right) + 6(3) = 6\\left(\\frac{x}{3}\\right) + 6(5)", "multiply every term by 6"),
                                ("3x + 18 = 2x + 30", "6 · x/2 = 3x; 6 · 3 = 18")]),
                     dict(sub="Worked: then solve.", min=2,
                          note="No fractions are left: it is 11.02's equation. Take 2x from both sides and subtract 18. Check in both sides of the first equation: 6 + 3 = 9 and 4 + 5 = 9.",
                          rows=[("3x + 18 = 2x + 30", "the fractions cleared"),
                                ("x + 18 = 30", "take 2x from both sides"),
                                ("x = 12", "subtract 18 from both sides"),
                                ("\\text{Check: } 12 \\div 2 + 3 = 9 \\quad 12 \\div 3 + 5 = 9", "both sides of the first equation")],
                          answer="x = 12")],
             check=("many", solves("u/2 + 3", "u/3 + 5", "12"), same("6*(u/2) + 6*3", "3*u + 18"), same("6*(u/3) + 6*5", "2*u + 30"),
                    solves("u + 18", "30", "12"), ("eq", "F(12,2) + 3", "9"), ("eq", "F(12,3) + 5", "9"),
                    solves("3*u + 3", "2*u + 5", "2")),
             your_turn=dict(min=2, note="Quarters and sixths clear with 12: 12 times x/4 is 3x, 12 times −1 is −12, 12 times x/6 is 2x, 12 times 1 is 12. Take 2x: x − 12 = 12, so x = 24. Check: 6 − 1 = 5 and 4 + 1 = 5. A board with 3x − 1 = 2x + 1 multiplied only the fractions (x = 2); one with 24 as the multiplier is right too, with bigger numbers.",
                            prompt=["$\\frac{x}{4} - 1 = \\frac{x}{6} + 1$", "Solve for x, then check in both sides."],
                            steps=["[equation] Every term times 12:  $3x - 12 = 2x + 12$",
                                   "Take 2x from both sides:  $x - 12 = 12$",
                                   "Add 12:  $x = 24$",
                                   "Check:  $24 \\div 4 - 1 = 5$  and  $24 \\div 6 + 1 = 5$"],
                            gloss="multiply every term by 12", answer="x = 24"),
             yt_check=("many", solves("u/4 - 1", "u/6 + 1", "24"), same("12*(u/4 - 1)", "3*u - 12"), same("12*(u/6 + 1)", "2*u + 12"),
                       solves("3*u - 1", "2*u + 1", "2"))),
    ],

    # The round: whole numbers, distribute and collect on one side (1), a negative fraction distributed (2), a decimal
    # distributed whose products are not whole (3, the 21% skill), the diagnostic on a negative decimal factor (4),
    # clearing fractions with a common denominator (5), the three endings with a fraction — an identity (6), the rental
    # story with an extra number (7), backwards (8), and a decimal solved and checked in writing (9). The pattern breaks
    # at 6: everything cancels.
    whiteboard=[
        dict(latex="5(x - 2) + 3 = 2x + 11",
             hint="Distribute, then collect.", steps=["Distribute:  $5(x - 2) + 3 = 5x - 10 + 3$",
                                                      "Collect:  $5x - 10 + 3 = 5x - 7$",
                                                      "Take 2x from both sides:  $3x - 7 = 11$",
                                                      "Add 7:  $3x = 18$",
                                                      "Divide by 3:  $x = 6$"],
             gloss="5x − 7 = 2x + 11", answer="x = 6",
             note="Notes I's order with whole numbers. A board with x = 10/3 wrote 5x − 2 (the 5 to one term only); one with x = −2/3 wrote 5x + 10 (the sign). Check: 5(4) + 3 = 23 and 2(6) + 11 = 23.",
             check=("many", solves("5*(u - 2) + 3", "2*u + 11", "6"), solves("5*u - 2 + 3", "2*u + 11", "F(10,3)"), solves("5*u + 10 + 3", "2*u + 11", "F(-2,3)")),
             wrong="x = 10/3 ≈ 3.33 — 5x − 2 + 3, the 5 to one term only [Florida B1G-M, AR.2.1: distributing to only one term]; x = −2/3 — 5x + 10 + 3, 5(−2) taken as +10 [Florida B1G-M, AR.2.1: sign errors while distributing]"),
        dict(latex="-\\frac{1}{3}(6x - 9) = x - 6",
             hint="The negative third reaches every term.", steps=["Distribute:  $-\\frac{1}{3}(6x - 9) = -2x + 3$",
                                                                  "Add 2x to both sides:  $3 = 3x - 6$",
                                                                  "Add 6:  $9 = 3x$",
                                                                  "Divide by 3:  $x = 3$"],
             gloss="−2x + 3 = x − 6", answer="x = 3",
             note="Notes II with new numbers: −⅓ of 6x is −2x and −⅓ of −9 is +3. A board with x = −1 wrote −2x − 9 (the fraction to one term only); one with x = 1 wrote −2x − 3 (the sign). Check: −⅓(18 − 9) = −3 and 3 − 6 = −3.",
             check=("many", solves("-F(1,3)*(6*u - 9)", "u - 6", "3"), solves("-2*u - 9", "u - 6", "-1"), solves("-2*u - 3", "u - 6", "1")),
             wrong="x = −1 — −2x − 9 = x − 6, the −1/3 to one term only [Florida B1G-M, AR.2.1: distributing to only one term]; x = 1 — −2x − 3 = x − 6, (−1/3)(−9) taken as −3 [Florida B1G-M, AR.2.1: sign errors while distributing]"),
        dict(latex="0.6(3x + 4) = 1.2x + 5.1",
             hint="The decimal multiplies both terms.", steps=["Distribute:  $0.6(3x + 4) = 1.8x + 2.4$",
                                                               "Take 1.2x from both sides:  $0.6x + 2.4 = 5.1$",
                                                               "Subtract 2.4:  $0.6x = 2.7$",
                                                               "Divide by 0.6:  $x = 4.5$"],
             gloss="1.8x + 2.4 = 1.2x + 5.1", answer="x = 4.5",
             note="Notes III and Example 1 with numbers that do not come out whole — the 21% skill at the state's level. 0.6 of 3x is 1.8x and 0.6 of 4 is 2.4. A board with x ≈ 1.83 wrote 1.8x + 4 (the decimal to one term only — the state's most common miss); one with x = 12.5 added the 2.4 (0.6x = 7.5). Check: 0.6(13.5 + 4) = 10.5 and 1.2(4.5) + 5.1 = 10.5.",
             check=("many", solves("F(3,5)*(3*u + 4)", "F(6,5)*u + F(51,10)", "F(9,2)"), solves("F(9,5)*u + 4", "F(6,5)*u + F(51,10)", "F(11,6)"),
                    solves("F(3,5)*u", "F(51,10) + F(12,5)", "F(25,2)"), ("eq", "F(3,5)*(F(27,2) + 4)", "F(21,2)"), ("eq", "F(6,5)*F(9,2) + F(51,10)", "F(21,2)")),
             wrong="x = 11/6 ≈ 1.83 — 1.8x + 4 = 1.2x + 5.1, the 0.6 to one term only [Florida B1G-M, AR.2.1: distributing to only one term]; x = 12.5 — 0.6x = 5.1 + 2.4, the 2.4 added instead of subtracted [Notes I: to isolate x, subtract 2.4 from both sides]"),
        dict(kind="mc", latex="-1.5(2x - 6) = x - 11",
             qtext="Solve −1.5(2x − 6) = x − 11 for x.",
             hint="The −1.5 multiplies both terms.", steps=["Distribute the −1.5:  $-1.5(2x - 6) = -3x + 9$",
                                                            "Add 3x to both sides:  $9 = 4x - 11$",
                                                            "Add 11:  $20 = 4x$",
                                                            "Divide by 4:  $x = 5$"],
             choices=["x = 5", "x = −10", "x = 1.25", "x = 0.5"], correct=0, answer="A — x = 5",
             errors={"B": "the −3x carried to the right side with its sign unchanged: 9 = x − 3x − 11, so −2x = 20 [Notes I: take the same term from both sides]", "C": "the −1.5 never reached the −6: −3x − 6 = x − 11, so 5 = 4x [Florida B1G-M, AR.2.1: distributing to only one term]", "D": "(−1.5)(−6) taken as −9: −3x − 9 = x − 11, so 2 = 4x [Florida B1G-M, AR.2.1: sign errors while distributing]"},
             note="Diagnostic, on a negative decimal factor (Notes III's kind). Option D is the sign, option C the one-term distribution, option B a term carried across the equals sign without its sign changing. On a split: sixty seconds to think again, re-vote — then check 5 in both sides: −1.5(10 − 6) = −6 and 5 − 11 = −6.",
             check=("many", solves("-F(3,2)*(2*u - 6)", "u - 11", "5"),
                    solves("-3*u - 9", "u - 11", "F(1,2)"), solves("-3*u - 6", "u - 11", "F(5,4)"), solves("9", "u - 3*u - 11", "-10"))),
        dict(latex="\\frac{x}{3} - 1 = \\frac{x}{5} + 1",
             hint="Thirds and fifths: multiply by 15.", steps=["Left times 15:  $15\\left(\\frac{x}{3} - 1\\right) = 5x - 15$",
                                                               "Right times 15:  $15\\left(\\frac{x}{5} + 1\\right) = 3x + 15$",
                                                               "Take 3x from both sides:  $2x - 15 = 15$",
                                                               "Add 15:  $2x = 30$",
                                                               "Divide by 2:  $x = 15$"],
             gloss="5x − 15 = 3x + 15", answer="x = 15",
             note="Example 2's move with new denominators: thirds and fifths clear with 15, and the 15 multiplies every term — the 1s as well. A board with x = 1 multiplied only the fractions (5x − 1 = 3x + 1); one stuck at 2x = 30 wrote the answer before dividing. Check: 15/3 − 1 = 4 and 15/5 + 1 = 4.",
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
             note="Diagnostic, and 11.03's endings with a fraction. Both sides are 3x − 2, so every number works. Option A distributed the 3 to one term and found 'no solution' — ask what 3 times −1 is. Options D and B read the true ending as an x — the same error, and the same reteach: say −2 = −2 aloud and ask for which x it is true. On a split: sixty seconds to think again, re-vote.",
             check=("many", same("F(1,2)*(6*u - 4)", "3*(u - 1) + 1"), not_never("F(1,2)*(6*u - 4)", "3*(u - 1) + 1"),
                    never("F(1,2)*(6*u - 4)", "3*u - 1 + 1"))),
        dict(text=["Shop A rents a bike for \\$12 plus \\$4.50 an hour.", "Shop B, 3 blocks away, charges \\$7.50 an hour.",
                   "**For how many hours do the two shops cost the same?"],
             unneeded="3",
             steps=["[equation] h hours at the same cost:  $12 + 4.5h = 7.5h$",
                    "Take 4.5h from both sides:  $12 = 3h$",
                    "Divide by 3:  $h = 4$",
                    "Check:  $12 + 4.5(4) = 30$  and  $7.5(4) = 30$"],
             gloss="12 + 4.5h = 7.5h", answer="4 hours (h = 4)",
             note="The extra-number board (ruling 22): Shop B's 3 blocks are not needed. Each shop's cost is an expression in h; they cost the same when the expressions are equal, 12 + 4.5h = 7.5h. Take 4.5h (the smaller) from both sides. Check: both cost \\$30 for 4 hours.",
             check=("many", solves("12 + F(9,2)*u", "F(15,2)*u", "4"), ("eq", "12 + F(9,2)*4", "30"), ("eq", "F(15,2)*4", "30"),
                    solves("12", "(F(9,2) + F(15,2))*u", "1"), solves("12", "F(15,2)*u", "F(8,5)")),
             wrong="1 hour — 12 = 12h, the two hourly rates added [Notes I: take the same term from both sides]; 1.6 hours — 12 ÷ 7.5, Shop A's \\$4.50 an hour left out [both shops' costs are equal]; 3 hours — the number of blocks taken as the answer [an extra number, included on purpose]"),
        dict(text=["The solution of  $3(x + □) = 2x + 20$  is  $x = 2$.", "**What number goes in the box?"],
             hint="Put 2 in for x.", steps=["Put 2 in for x:  $2(2) + 20 = 24$,  so  $3(2 + □) = 24$",
                                            "$24 \\div 3 = 8$,  and  $8 - 2 = 6$"],
             gloss="3(2 + 6) = 24", answer="6",
             note="Backwards: the solution is given and a number in the equation is missing. Put 2 in for x on BOTH sides — the right is 24, so 2 + □ must be 8. Check: 3(2 + 6) = 24 and 2(2) + 20 = 24.",
             check=("many", solves("3*(2 + u)", "2*2 + 20", "6"), solves("3*(u + 6)", "2*u + 20", "2"), solves("3*2 + u", "2*2 + 20", "18")),
             wrong="8 — the value of the parentheses, one step short [the box is what is added to 2]; 18 — 6 plus the box set equal to 24, the 3 to the first term only [Florida B1G-M, AR.2.1: distributing to only one term]"),
        dict(kind="written", text=["Solve  $1.5(4x - 2) + x = 2(x + 6)$  for x.", "**Then check your solution in both sides."],
             qtext="Solve 1.5(4x − 2) + x = 2(x + 6) for x. Then check your solution in both sides.",
             hint="Each side first.", steps=["Left:  $1.5(4x - 2) + x = 7x - 3$.   Right:  $2(x + 6) = 2x + 12$",
                                             "Take 2x from both sides:  $5x - 3 = 12$",
                                             "Add 3:  $5x = 15$",
                                             "Divide by 5:  $x = 3$",
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
        dict(stem="Solve for w:  $-\\frac{3}{4}(8w - 12) = 2w - 23$", answer="w = 4",
             why="The −¾ multiplies both terms: −6w + 9 = 2w − 23; add 6w: 9 = 8w − 23; 32 = 8w. Check: −¾(20) = −15 and 8 − 23 = −15.",
             check=("many", solves("-F(3,4)*(8*u - 12)", "2*u - 23", "4"), same("-F(3,4)*(8*u - 12)", "-6*u + 9"),
                    ("eq", "-F(3,4)*(8*4 - 12)", "-15"), ("eq", "2*4 - 23", "-15")), space=1.0),
        dict(stem="Solve for n:  $\\frac{2}{5}(10n - 5) = 3n + 4$", answer="n = 6",
             why="Two-fifths of 10n is 4n; two-fifths of −5 is −2. 4n − 2 = 3n + 4; n = 6. Check: 22 = 22.",
             check=("many", solves("F(2,5)*(10*u - 5)", "3*u + 4", "6"), ("eq", "F(2,5)*(10*6 - 5)", "22"), ("eq", "3*6 + 4", "22")), space=1.0),
        dict(stem="Solve for m:  $\\frac{m}{2} - 3 = \\frac{m}{5} + 3$", answer="m = 20",
             why="Multiply both sides by 10 (every term): 5m − 30 = 2m + 30; 3m = 60. Check: 7 = 7.",
             check=("many", solves("u/2 - 3", "u/5 + 3", "20"), same("10*(u/2 - 3)", "5*u - 30"), same("10*(u/5 + 3)", "2*u + 30")), space=1.0),
        dict(stem="Solve for k:  $-2.5(2k - 4) = k - 8$", answer="k = 3",
             why="The −2.5 multiplies both terms: −5k + 10 = k − 8; 18 = 6k. Check: −2.5(2) = −5 and 3 − 8 = −5.",
             check=("many", solves("-F(5,2)*(2*u - 4)", "u - 8", "3"), same("-F(5,2)*(2*u - 4)", "-5*u + 10"), ("eq", "-F(5,2)*(2*3 - 4)", "-5")), space=1.0),
        dict(stem="How many solutions does  $\\frac{1}{4}(8v + 12) = 2v - 1$  have? If it has one, find it.", answer="No solution",
             why="2v + 3 = 2v − 1; take 2v from both sides: 3 = −1, never true.",
             check=never("F(1,4)*(8*u + 12)", "2*u - 1"), space=1.0),
        dict(stem="A kayak rental costs \\$15 plus \\$6.50 an hour. A second shop charges \\$9 an hour. For how many hours do the two cost the same?",
             answer="6 hours", why="15 + 6.5h = 9h; 15 = 2.5h. Check: both cost \\$54.",
             check=("many", solves("15 + F(13,2)*u", "9*u", "6"), ("eq", "15 + F(13,2)*6", "54"), ("eq", "9*6", "54")), space=1.0),
    ],

    # Bank: whole-number multi-step (1–3: one side's parentheses, both sides', and one at the state's ugliness with a
    # fraction answer), fractions (4–6: a positive and a negative fraction distributed, fraction coefficients cleared by
    # a common denominator), decimals (7–8, the 21% skill, products not whole: a positive factor, a negative one), backwards (9), a rental story (10), the diagnostic mc on a decimal (11), select-all on the
    # endings with fraction and decimal coefficients (12). The additional bank mirrors it position by position.
    bank=[
        dict(heading="For questions 1 through 3, solve the equation."),
        dict(stem="$2(4p - 1) + 3 = 5p + 13$", answer="p = 4", why="8p + 1 = 5p + 13; 3p = 12. Check: 33 = 33.", check=solves("2*(4*u - 1) + 3", "5*u + 13", "4"), space=0.8),
        dict(stem="$6(m + 1) - 2m = 3(m + 4)$", answer="m = 6", why="4m + 6 = 3m + 12. Check: 30 = 30.", check=solves("6*(u + 1) - 2*u", "3*(u + 4)", "6"), space=0.8),
        dict(stem="$5(2q - 3) + 3q = -2(4q + 1)$", answer="q = 13/21", why="10q − 15 + 3q = −8q − 2; 13q − 15 = −8q − 2; 21q = 13. Not a whole number — the state's tests ask for these too.", check=solves("5*(2*u - 3) + 3*u", "-2*(4*u + 1)", "F(13,21)"), space=0.8),
        dict(heading="For questions 4 through 6, the equation has fractions. Solve for the variable."),
        dict(stem="$\\frac{1}{2}(6y + 10) = 2y + 9$", answer="y = 4", why="3y + 5 = 2y + 9. Check: 17 = 17.", check=solves("F(1,2)*(6*u + 10)", "2*u + 9", "4"), space=0.8),
        dict(stem="$-\\frac{2}{3}(6r - 9) = r - 15$", answer="r = 4.2", why="−4r + 6 = r − 15; 21 = 5r. Check: −(2/3)(16.2) = −10.8 and 4.2 − 15 = −10.8.", check=solves("-F(2,3)*(6*u - 9)", "u - 15", "F(21,5)"), space=0.8),
        dict(stem="$\\frac{2}{3}z + 5 = \\frac{1}{6}z - 1$", answer="z = −12", why="Multiply every term by 6: 4z + 30 = z − 6; 3z = −36. Check: −8 + 5 = −3 and −2 − 1 = −3.", check=solves("F(2,3)*u + 5", "F(1,6)*u - 1", "-12"), space=0.8),
        dict(heading="For questions 7 and 8, the factor is a decimal. Solve the equation."),
        dict(stem="$0.3(5t + 4) = t + 2.2$", answer="t = 2", why="1.5t + 1.2 = t + 2.2; 0.5t = 1. Check: 0.3(14) = 4.2 and 2 + 2.2 = 4.2.", check=solves("F(3,10)*(5*u + 4)", "u + F(11,5)", "2"), space=0.8),
        dict(stem="$-1.5(4k - 3) = 2k - 13.5$", answer="k = 2.25", why="−6k + 4.5 = 2k − 13.5; 18 = 8k. Check: −1.5(6) = −9 and 4.5 − 13.5 = −9.", check=solves("-F(3,2)*(4*u - 3)", "2*u - F(27,2)", "F(9,4)"), space=0.8),
        dict(heading="Find the missing number."),
        dict(stem="The solution of $3(x + □) = x + 26$ is $x = 4$. What number goes in the box?", answer="6", why="Put 4 in for x: 3 times the parentheses is 30. The parentheses are 10, so the box is 6.",
             check=("many", solves("3*(4 + u)", "4 + 26", "6"), solves("3*(u + 6)", "u + 26", "4")), space=0.8),
        dict(heading="Solve the problem."),
        dict(stem="Boat rental A costs \\$20 plus \\$5.50 an hour. Boat rental B costs \\$8 an hour. For how many hours do the two rentals cost the same?",
             answer="8 hours", why="20 + 5.5h = 8h; 20 = 2.5h. Both cost \\$64.", check=solves("20 + F(11,2)*u", "8*u", "8"), space=0.8),
        dict(heading="Choose one."),
        dict(stem="Solve for x:  $1.5(2x - 4) = x + 8$", choices=["$x = 3.5$", "$x = 1$", "$x = 6$", "$x = 7$"], correct=3, answer="D",
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
        dict(stem="$4(3q - 2) + q = -3(2q + 1)$", answer="q = 5/19", why="12q − 8 + q = −6q − 3; 13q − 8 = −6q − 3; 19q = 5. Not a whole number — the state's tests ask for these too.", check=solves("4*(3*u - 2) + u", "-3*(2*u + 1)", "F(5,19)"), space=0.8),
        dict(heading="For questions 4 through 6, the equation has fractions. Solve for the variable."),
        dict(stem="$\\frac{1}{2}(8y - 6) = 3y + 4$", answer="y = 7", why="4y − 3 = 3y + 4. Check: 25 = 25.", check=solves("F(1,2)*(8*u - 6)", "3*u + 4", "7"), space=0.8),
        dict(stem="$-\\frac{3}{4}(4r - 8) = r - 9$", answer="r = 3.75", why="−3r + 6 = r − 9; 15 = 4r. Check: −¾(7) = −5.25 and 3.75 − 9 = −5.25.", check=solves("-F(3,4)*(4*u - 8)", "u - 9", "F(15,4)"), space=0.8),
        dict(stem="$\\frac{1}{3}z + 8 = \\frac{5}{6}z - 2$", answer="z = 20", why="Multiply every term by 6: 2z + 48 = 5z − 12; 60 = 3z. Check: both sides are 44/3.", check=solves("F(1,3)*u + 8", "F(5,6)*u - 2", "20"), space=0.8),
        dict(heading="For questions 7 and 8, the factor is a decimal. Solve the equation."),
        dict(stem="$0.4(5t + 3) = t + 4.2$", answer="t = 3", why="2t + 1.2 = t + 4.2; t = 3. Check: 0.4(18) = 7.2 and 3 + 4.2 = 7.2.", check=solves("F(2,5)*(5*u + 3)", "u + F(21,5)", "3"), space=0.8),
        dict(stem="$-1.5(2k - 5) = k - 4.5$", answer="k = 3", why="−3k + 7.5 = k − 4.5; 12 = 4k. Check: −1.5(1) = −1.5 and 3 − 4.5 = −1.5.", check=solves("-F(3,2)*(2*u - 5)", "u - F(9,2)", "3"), space=0.8),
        dict(heading="Find the missing number."),
        dict(stem="The solution of $4(x + □) = 2x + 26$ is $x = 3$. What number goes in the box?", answer="5", why="Put 3 in for x: 4 times the parentheses is 32. The parentheses are 8, so the box is 5.",
             check=("many", solves("4*(3 + u)", "2*3 + 26", "5"), solves("4*(u + 5)", "2*u + 26", "3")), space=0.8),
        dict(heading="Solve the problem."),
        dict(stem="Scooter rental A costs \\$10 plus \\$3.50 an hour. Scooter rental B costs \\$6 an hour. For how many hours do the two rentals cost the same?",
             answer="4 hours", why="10 + 3.5h = 6h; 10 = 2.5h. Both cost \\$24.", check=solves("10 + F(7,2)*u", "6*u", "4"), space=0.8),
        dict(heading="Choose one."),
        dict(stem="Solve for x:  $2.5(2x - 4) = x + 6$", choices=["$x = \\frac{8}{3}$", "$x = 4$", "$x = 2.5$", "$x = -1$"], correct=1, answer="B",
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
        say=["Distribute, collect each side, take the same term from both sides until x is alone, divide — then check in both sides.",
             "A fraction or a decimal outside the parentheses multiplies every term inside, just as a whole number does.",
             "To clear fractions, multiply every term on both sides by a common denominator."],
        must="Students solve multi-step linear equations with rational coefficients (fractions and decimals) and the variable on both sides, and they verify each solution by substitution.",
        must_not="Students write an equation from a context only where two plans cost the same. Writing equations from other contexts belongs to Algebra 1 (MA.912.AR.2.1). Systems of equations begin in Lesson 11.05.",
        read_first=[
            "The unit's fourth day, after a spiral day with no deck (Thu 3 Dec, FAST PM2). Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §11.04), then read against Math Nation 11.4 (the unit audit, Part 1). The moves are the last three days'; the new content is the benchmark's 'rational number coefficients' — a fraction distributed, fractions cleared by a common denominator, a decimal distributed.",
            "The two example pairs go to the techniques that need a model: Example 1 is the decimal distributed with the variable on both sides, Example 2 clears fractions with a common denominator, its second line written out — 6(x/2) + 6(3) = 6(x/3) + 6(5) — because that is the step students skip. Notes I shows every move of the whole-number order on its own line. The decimal distribution is the lowest-scoring released Grade 8 FAST skill (21%): Notes III is the state's own shape (−2.4(5x − 3) = −40.8: a negative decimal factor, a decimal product, the equation of FAST's released item at our numbers), then Example 1, board 3 (products not whole: 1.8x + 2.4), board 4 (a negative decimal, −1.5, as a diagnostic), board 9 and set question 4 (−2.5). A negative fraction is on the slides too: Notes II (−½), board 2 (−⅓) and set question 1 (−¾). Bank 3 and additional 3 end at a fraction (13/21, 5/19) — the state's 'tedious' value.",
            "Every multiple-choice wrong option is one of the B1G-M's named AR.2.1 errors — distributing to only one term, a sign error while distributing, expecting variable = constant — or a named slip (a term carried across the equals sign with its sign unchanged; the x-terms added). A false ending is written as the false equation with its words, never as '≠'; on an answer slide it is said in words because the build's step check holds every printed equation true.",
            "Not reproduced from the book: the 11.4.1 game-statistics warm-up (no AR.2.1 content); Clare's error analysis, whose stem says 'a mistake' over two (D7); the 11.4.3 card sort, whose cards were never supplied (D11, T8) and whose card K work line has both signs wrong (D8); PP #10, whose student page and key are different equations (D6 — here each item's key is worked from the very equation printed); the key lines with wrong constants, '10 ≠ 3' and '0.8 ≠ 1.8' (D9, D10); the partner work."],
        standard_notes=[("Clarification", "Problem types include equations that generate one solution, infinitely many solutions or no solution (Clarification 1) — today mostly one solution with rational coefficients; board 6 and set question 5 bring back the other two endings."),
                        ("Unit boundary", "Fraction and decimal coefficients, positive and negative; parentheses on either or both sides; whole and negative solutions. Solution forms x = a, a = a, a = b (B1G-M); one-solution answers verified by substitution in both sides.")],
        sits="The unit's fourth day and the last of its equations before systems. IXL 55K, PGH and HZZ are done today and due by the Unit 11 test (Fri 11 Dec), whose questions 1–4 are today's kinds — question 4 distributes a decimal. 11.05 starts systems: a pair of values that makes two equations true.",
        lives="Notes III — the decimal multiplies both terms, sign and all — and Example 2, clearing fractions. Board 3 is the 21% skill with products that are not whole; board 4 the diagnostic on a negative decimal factor (sign, one term, a term carried across); board 6 the endings with a fraction; board 9 a decimal solved and checked in writing.",
        materials="Whiteboards and markers. Hand out the Independent Set, one per student, after whiteboard question 9.",
        variation="Board 1 is Notes I's order with whole numbers; 2 distributes a negative fraction (Notes II); 3 a decimal whose products are not whole (the 21% skill); 4 votes on a negative decimal factor. 5 clears fractions with a common denominator (Example 2). The pattern breaks at 6: a fraction distributed and everything cancels — infinitely many. 7 is the rental story with Shop B's 3 blocks as the extra number; 8 runs backwards; 9 distributes a decimal and checks in writing. The independent set walks the same path in six: a negative fraction distributed, a positive fraction distributed, a common denominator, a negative decimal distributed, an ending with a fraction (no solution) and a rental story.",
        audit=["Every equation re-derived by sympy at build time over the real numbers (mathcheck: 0 findings); every worked row of the examples checked to have the first equation's solution, and every check row computed; every multiple-choice distractor and every wrong answer named in a note solved again from its named error.",
               "Math Nation 11.4 read against this lesson (A7 Unit 11 Audit, Part 1 §1–§5): D6–D11 and T1 not reproduced — no key here is worked from a different equation than its student page (D6); every printed work line is re-derived, so none carries a wrong constant (D8–D10, and T1's halving: Example 2 multiplies every term by 6 and the build checks it); no stem miscounts its errors (D7); no activity depends on missing materials (D11). The audit's §4 gaps met today: a negative rational factor distributed (Notes II and III, boards 2 and 4, set 1 and 4, bank 5 and 8, additional 5 and 8), a fraction in a no-solution equation (set 5, bank 12), fractions cleared by multiplying (Example 2 and its Your Turn, board 5, set 3, bank 6), substitution in both sides on every item."],
        changes=["11.4.1 game-statistics warm-up → four retrieval questions, the prerequisite (two-thirds of 9) in the last slot.",
                 "11.4.2 Clare's error analysis (two errors, 'a mistake') → board 4's options, each a named error, and board 9's check.",
                 "11.4.3 card sort in pairs (no cards supplied) → Notes I–III and boards 1–6, taught from the front; the endings with fractions are board 6 and set question 5.",
                 "PP and HW pages 7–8 (solve eight, none checked) → the Independent Set, every answer checked in both sides."],
    ),
)
