# A7 11.02  Equations with Variables on Both Sides — MA.8.AR.2.1 (MN 11.2). Tue 1 Dec 2026, a 53-minute period.
# Yesterday's equations had the variable on one side; today it is on both, and the one new move is to take the same
# variable term from both sides — the balance stays level only if both sides lose the same thing. Either term may
# go (Notes II solves it one way and says the other also works; board 9 does both); taking the smaller one keeps the coefficient positive. Parentheses
# are distributed first (11.01's move), and every solution is checked in BOTH sides of the first equation — today's
# habit. Every equation here has exactly one solution; the other two endings are 11.03. Built from the benchmark and
# the B1G-M first (the unit's Lesson Outlines, §11.02), then read against Math Nation 11.2 (the unit audit, Part 1).
# Not reproduced: the hanger warm-up (a preview, not retrieval, and its second hanger an unflagged identity), the
# algebra-tile exploration (discovery, and the grayscale tiles), the partner work, and the key's "eliminate" for a
# coefficient made 1 (T4).
#
# Every equation is solved again by sympy at build time: root() below solves "left = right" for a REAL unknown
# (the build's own letters are positive symbols), so no answer here leans on the sign of the variable. The answer
# slides' steps never write an equation with the letter on both sides inside one $…$ span: stepcheck holds such a
# span to be an identity, so a step starts from the first move (the question above it shows the equation).

U = "sp.Symbol('u', real=True)"


def _u(e):
    import re
    return re.sub(r"\bu\b", U, e)


def solves(left, right, value):
    """sympy solves left = right (in u) and finds exactly `value`."""
    return ("eq", "sp.solve(sp.Eq(" + _u(left) + ", " + _u(right) + "), " + U + ")[0]", value)


def same(e1, e2):
    """Two expressions in u are the same expression (a correct line of work)."""
    return ("true", "sp.expand(" + _u(e1) + " - (" + _u(e2) + ")) == 0")


def not_root(left, right, value):
    """`value` does not solve left = right (in u)."""
    return ("true", "sp.solve(sp.Eq(" + _u(left) + ", " + _u(right) + "), " + U + ") != [" + value + "]")


def one_root(left, right):
    """left = right has exactly one solution (not none, not every number)."""
    return ("true", "len(sp.solve(sp.Eq(" + _u(left) + ", " + _u(right) + "), " + U + ")) == 1")


L = dict(
    code="11.02", unit=11, lesson_no=2,
    align="=",   # every run of rows that solve an equation set with its equals signs in one column (kit, 15 Nov 2026)
    title="Equations with Variables on Both Sides",
    unit_title="Solving Equations and Systems",
    benchmark="MA.8.AR.2.1",
    benchmark_text="Solve multi-step linear equations in one variable, with rational number coefficients. Include equations with variables on both sides.",
    target="I can solve an equation that has the variable on both sides, and check the solution in both sides.",
    yesterday="Last class: equations with like terms and parentheses.",
    today="Today: equations with the variable on both sides.",
    essential="Why may we take the same variable term from both sides of an equation — and why does it not matter which one we take?",
    building_on="Lesson 11.01 solved equations by collecting like terms and distributing. Lesson 1.03 (Unit 1) solved two-step equations. Unit 4 covered arithmetic with signed rational numbers.",
    working_toward="Lesson 11.03 sorts equations by whether they have one solution, no solution or infinitely many solutions. Lesson 11.04 adds fraction and decimal coefficients. In Lessons 11.05–11.08, the x-value where two lines cross is the solution of an equation with the variable on both sides.",
    vocab=[("variable term", "a term with a variable in it, like $5x$ or $-3x$"),
           ("solution", "the number that makes the two sides of an equation equal")],
    vocab_note="Two words, and the second is today's habit. A solution is not just the last line: it is the number that makes the two sides equal, so it is proved by putting it into BOTH sides of the first equation and getting the same number twice.",
    ixl=["Solve equations with variables on both sides — ZYL"],
    closure="Whiteboard question 9 is answered in writing and serves as the exit ticket. A complete answer shows both ways: Kai takes 2x from both sides and reaches 15 = 4x − 9, Lena takes 6x from both sides and reaches −4x + 15 = −9, and both end at x = 6. It also gives the reason: the same step done to both sides keeps the equation true, whichever term is taken. A check of 6 in both sides, 27 = 27, also earns full credit.",

    mtr=[("MTR.3.1", "On whiteboard questions 1–5, students take the same variable term from both sides, isolate the variable and check the solution in both sides."),
         ("MTR.4.1", "On whiteboard questions 4 and 6, a divided class has one minute to convince a neighbor and then votes again."),
         ("MTR.5.1", "Students see that either variable term can be taken from both sides and that the solution is the same either way (Notes II and whiteboard question 9).")],
    hoq=[("In 2x + 9 = 6x − 11, why do taking 2x and taking 6x give the same solution?", "DOK 2"),
         ("The solution of whiteboard question 3 is negative. Before solving, how could you tell that it would be?", "DOK 3"),
         ("Why must a check go into both sides of the first equation, not into a later line?", "DOK 2")],
    differentiation=[
        ("ESE / 504", "Keep one line on display all period, with a drawing of a balance beside it: \"Take the same variable term from BOTH sides.\" On every whiteboard question, students circle the two variable terms and the smaller coefficient before they write anything else."),
        ("ELL", "**Variable term**: a term with a letter in it, such as 5x. **Both sides**: the left of the equals sign and the right of it. **Isolate**: get the variable alone on one side. **Check**: put the solution back into each side. The two values must match."),
        ("Enrichment", "Students who finish whiteboard question 8 early find the number that goes in the box so that $5x + □ = 2x + 16$ has the solution x = 0 (the answer is 16), and then the number that makes the solution x = −2 (the answer is 22).")],

    warmup=[
        dict(stem="Solve for x:  $3(x + 2) + x = 26$", answer="x = 5", band="last lesson",
             source="11.01 — distribute, then collect like terms",
             check=solves("3*(u + 2) + u", "26", "5")),
        dict(stem="Remote interior angles: 50° and 65°. Find the exterior angle.", answer="115°", band="last week",
             source="T-B2 — an exterior angle equals the sum of the two remote interior angles",
             check=("eq", "50 + 65", "115")),
        dict(stem="A right triangle: hypotenuse 13, one leg 5. Find the other leg.", answer="12", band="last unit",
             source="6.03 — the Pythagorean Theorem, a missing leg",
             check=("eq", "sqrt(13**2 - 5**2)", "12")),
        dict(stem="Simplify:  $2x - 5x$", answer="−3x", band="the prerequisite this lesson needs",
             source="11.01 — collecting like terms (Notes I), here with a negative result: 2 − 5 = −3; every board today takes one x-term from another",
             check=("eq", "2*x - 5*x", "-3*x")),
    ],
    warmup_note="Q4 is today's move in miniature: taking 5x from 2x leaves −3x, and taking 2x from 5x leaves 3x. Say that in one sentence after the reveal — it is why Notes II takes the smaller x-term. Two minutes silent, then reveal, no discussion.",

    notes=[
        dict(numeral="I", head="Subtraction property of equality: same term from both sides", min=4, sub="Copy all four lines.",
             note="The equation has x on both sides, so the first move is new: take 3x from BOTH sides — the second line writes the move out, − 3x under each side, and is the only line today that does; after this, the move is made in the head and the next line is written. Its name is in the heading: the subtraction property of equality (Florida asks students to name the property they used). A balance stays level only if both pans lose the same thing — 3x from one side alone would tip it. What is left, 2x + 2 = 10, is Unit 1's two-step equation. Then the check, in both sides of the first equation: 5(4) + 2 = 22 and 3(4) + 10 = 22. The same number twice is the proof.\nOFF: 'Whatever you do to one side, you do to the other — and that includes taking away x's.'",
             math=["$5x + 2 = 3x + 10$", "$5x + 2 - 3x = 3x + 10 - 3x$", "$2x + 2 = 10$", "$2x = 8$", "$x = 4$"],
             items2=["Check:  $5(4) + 2 = 22$   and   $3(4) + 10 = 22$"],
             letters=False),
        dict(numeral="II", head="Either side works", min=3, sub="",
             note="One route on the slide, line under line: take 2x from both sides, 9 = 4x − 11; add 11, 20 = 4x; divide by 4. Say the other route aloud and do not write it: taking 6x gives −4x + 9 = −11 and also ends at 5, because each step is done to both sides — board 9 has the class do both. Taking the smaller x-term leaves a positive coefficient, so no division by a negative. Check: 2(5) + 9 = 19 and 6(5) − 11 = 19. The last line writes two plans as one equation before board 7 asks for it: each plan's cost is an expression — 12 + 3v and 5v — and 'the same cost' is the equals sign. Do not solve it on the slide (v = 6); say which term is smaller.\nOFF: 'Take the smaller x-term and the coefficient stays positive.'",
             math=["$2x + 9 = 6x - 11$", "$9 = 4x - 11$", "$20 = 4x$", "$x = 5$"],
             items2=["**Take the smaller x-term: it stays positive. Taking 6x also works.**",
                     "Plan 1: \\$12 plus \\$3 a visit.  Plan 2: \\$5 a visit.  The same cost:   $12 + 3v = 5v$"],
             letters=False),
        dict(numeral="III", head="Simplify each side first", min=3, sub="",
             note="Parentheses are distributed before any term moves — yesterday's move first, today's second. The 3 multiplies the x AND the 4: 3x + 12. Then take 3x (the smaller) from both sides: 12 = 2x − 2. Then two steps. Check: 3(7 + 4) = 33 and 5(7) − 2 = 33.\nOFF: 'Clear the parentheses, then move one variable term.'",
             math=["$3(x + 4) = 5x - 2$", "$3x + 12 = 5x - 2$", "$12 = 2x - 2$", "$14 = 2x$", "$x = 7$"],
             items2=["Check:  $3(7 + 4) = 33$   and   $5(7) - 2 = 33$"],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", sub="The variable on both sides.", min_q=1,
             note_q="Ask which variable term is smaller before anyone writes: 4x. Take it from both sides.",
             prompt=["$7x - 5 = 4x + 13$"], ask="Solve for x, then check in both sides.",
             worked=[dict(sub="Worked.", min=2,
                          note="Take 4x from both sides: 3x − 5 = 13. Then two steps: add 5, divide by 3. Check in both sides of the first equation: 7(6) − 5 = 37 and 4(6) + 13 = 37. A board with x = 18/11 added the x-terms (11x = 18); one with x = 8/3 took the 5 the wrong way.",
                          rows=[("7x - 5 = 4x + 13", "the equation"),
                                ("3x - 5 = 13", "take 4x from both sides"),
                                ("3x = 18", "add 5 to both sides"),
                                ("x = 6", "divide both sides by 3"),
                                ("\\text{Check: } 7(6) - 5 = 37 \\quad 4(6) + 13 = 37", "both sides of the first equation")],
                          answer="x = 6")],
             check=solves("7*u - 5", "4*u + 13", "6"),
             your_turn=dict(min=2, note="Take 5x from both sides: 3x − 9 = 15, so 3x = 24 and x = 8. This catches a student who watched the move without doing it — a board with 13x = 24 added the x-terms; one with x = 2 subtracted the 9 (3x = 6).",
                            prompt=["$8x - 9 = 5x + 15$", "Solve for x, then check in both sides."],
                            steps=["Take 5x from both sides:  $3x - 9 = 15$",
                                   "Add 9:  $3x = 24$",
                                   "Divide by 3:  $x = 8$",
                                   "Check:  $8(8) - 9 = 55$  and  $5(8) + 15 = 55$"],
                            gloss="take 5x, then two steps", answer="x = 8"),
             yt_check=solves("8*u - 9", "5*u + 15", "8")),
        dict(title="Example 2", sub="Parentheses first; a solution that is not whole.", min_q=1,
             note_q="Ask what the 2 multiplies before anyone writes: the 3x AND the −1.",
             prompt=["$2(3x - 1) = 4x + 9$"], ask="Solve for x, then check in both sides.",
             worked=[dict(sub="Worked.", min=2,
                          note="Distribute: 6x − 2. Take 4x from both sides: 2x − 2 = 9, so 2x = 11 and x = 5.5. A solution need not be a whole number — 5.5 is checked like any other: 2(16.5 − 1) = 31 and 4(5.5) + 9 = 31. A board with 2x = 10 distributed to one term (6x − 1).",
                          rows=[("2(3x - 1) = 4x + 9", "the equation"),
                                ("6x - 2 = 4x + 9", "2 times 3x, 2 times −1"),
                                ("2x - 2 = 9", "take 4x from both sides"),
                                ("2x = 11", "add 2 to both sides"),
                                ("x = 5.5", "divide both sides by 2"),
                                ("\\text{Check: } 2(15.5) = 31 \\quad 4(5.5) + 9 = 31", "both sides of the first equation")],
                          answer="x = 5.5")],
             check=solves("2*(3*u - 1)", "4*u + 9", "F(11,2)"),
             your_turn=dict(min=2, note="8x − 12 = 6x + 1, so 2x − 12 = 1, 2x = 13 and x = 6.5. This catches the one-term distribution: a board with 8x − 3 = 6x + 1 gets x = 2. Check: 4(13 − 3) = 40 and 6(6.5) + 1 = 40.",
                            prompt=["$4(2x - 3) = 6x + 1$", "Solve for x, then check in both sides."],
                            steps=["Distribute:  $4(2x - 3) = 8x - 12$",
                                   "Take 6x from both sides:  $2x - 12 = 1$",
                                   "Add 12:  $2x = 13$",
                                   "Divide by 2:  $x = 6.5$",
                                   "Check:  $4(13 - 3) = 40$  and  $6(6.5) + 1 = 40$"],
                            gloss="distribute, take 6x, two steps", answer="x = 6.5"),
             yt_check=solves("4*(2*u - 3)", "6*u + 1", "F(13,2)")),
    ],

    # The round: one variable term on each side with no constant on the left (1), with a constant on each side (2),
    # the larger coefficient on the right so the solution is negative (3), the diagnostic on the move (4), parentheses
    # on one side (5) and on both, its diagnostic (6), the two-plans story with an extra number (7), backwards (8),
    # and one equation solved both ways in writing (9). The pattern breaks at 3: the smaller x-term is on the LEFT,
    # so the constants end on the left and the solution is negative.
    whiteboard=[
        dict(latex="6x = 2x + 28",
             hint="Take 2x from both sides.", steps=["Take 2x from both sides:  $4x = 28$", "Divide by 4:  $x = 7$",
                                                     "Check:  $6(7) = 42$  and  $2(7) + 28 = 42$"],
             gloss="4x = 28", answer="x = 7",
             note="One move, then one step. A board with x = 3.5 added the x-terms (8x = 28); one with x ≈ 4.67 dropped the 2x (6x = 28). Check in both sides: 42 = 42.",
             check=solves("6*u", "2*u + 28", "7"),
             wrong="x = 3.5 — 8x = 28, the x-terms added [Notes I: take the same term from both sides]; x = 14/3 ≈ 4.67 — 6x = 28, the 2x dropped [Notes I: a variable term is a term too]"),
        dict(latex="9x + 4 = 5x + 40",
             hint="Which x-term is smaller?", steps=["Take 5x from both sides:  $4x + 4 = 40$", "Subtract 4:  $4x = 36$", "Divide by 4:  $x = 9$",
                                                     "Check:  $9(9) + 4 = 85$  and  $5(9) + 40 = 85$"],
             gloss="4x + 4 = 40", answer="x = 9",
             note="Notes I with bigger numbers. A board with x = 11 added the 4 (4x = 44); one with x ≈ 2.57 added the x-terms (14x = 36).",
             check=solves("9*u + 4", "5*u + 40", "9"),
             wrong="x = 11 — 4x = 44, the 4 added instead of subtracted [Notes I: to isolate x, subtract 4 from both sides]; x = 18/7 ≈ 2.57 — 14x + 4 = 40, the x-terms added [Notes I: take the same term from both sides]"),
        dict(latex="3n - 8 = 7n + 12",
             hint="Take the smaller n-term.", steps=["Take 3n from both sides:  $-8 = 4n + 12$", "Subtract 12:  $-20 = 4n$", "Divide by 4:  $n = -5$",
                                                     "Check:  $3(-5) - 8 = -23$  and  $7(-5) + 12 = -23$"],
             gloss="−8 = 4n + 12", answer="n = −5",
             note="The pattern breaks: the larger n-term is on the right, so the constants end on the left and the solution is negative. A board with n = 5 lost the sign of −20; one with n = 1 added 12 to −8 (4 = 4n). Check: −23 = −23.",
             check=solves("3*u - 8", "7*u + 12", "-5"),
             wrong="n = 5 — 20 = 4n, the sign of −20 lost [Notes I: −8 − 12 = −20]; n = 1 — 4 = 4n, 12 added to −8 instead of subtracted [Notes I: to isolate n, subtract 12 from both sides]; n = 2 — 10n − 8 = 12, the n-terms added [Notes I: take the same term from both sides]"),
        dict(kind="mc", latex="5x + 8 = x - 16",
             qtext="Solve 5x + 8 = x − 16 for x.",
             hint="Take x from both sides.", steps=["Take x from both sides:  $4x + 8 = -16$", "Subtract 8:  $4x = -24$", "Divide by 4:  $x = -6$",
                                                    "Check:  $5(-6) + 8 = -22$  and  $-6 - 16 = -22$"],
             choices=["$x = 6$", "$x = -6$", "$x = -2$", "$x = -4$"], correct=1, answer="B — x = −6",
             errors={"A": "the sign lost at the last step: 4x = 24 [Notes I: −16 − 8 = −24]", "C": "8 added instead of taken away: 4x = −16 + 8 = −8 [Notes I: to isolate x, subtract 8 from both sides]", "D": "the x-terms added: 6x + 8 = −16, so 6x = −24 [Notes I: take the same term from both sides]"},
             note="Diagnostic. Option D adds the x-terms, option C moves the 8 the wrong way, option A drops the sign. On a split: sixty seconds, convince your neighbor, re-vote — then check −6 in both sides: −22 and −22.",
             check=("many", solves("5*u + 8", "u - 16", "-6"),
                    solves("6*u + 8", "-16", "-4"), solves("4*u", "-16 + 8", "-2"), solves("4*u", "24", "6"))),
        dict(latex="2(x + 7) = 5x - 4",
             hint="Distribute first.", steps=["Distribute:  $2(x + 7) = 2x + 14$", "Take 2x from both sides:  $14 = 3x - 4$",
                                              "Add 4:  $18 = 3x$", "Divide by 3:  $x = 6$"],
             gloss="14 = 3x − 4", answer="x = 6",
             note="Notes III's order: parentheses first, then a variable term. A board with x ≈ 3.67 wrote 2x + 7 (one term); one with x ≈ 3.33 took the 4 the wrong way (10 = 3x). Check: 2(6 + 7) = 26 and 5(6) − 4 = 26.",
             check=solves("2*(u + 7)", "5*u - 4", "6"),
             wrong="x = 11/3 ≈ 3.67 — 2x + 7 = 5x − 4, the 2 to one term only [Florida B1G-M, AR.2.1: distributing to only one term]; x = 10/3 ≈ 3.33 — 14 − 4 = 3x, the 4 subtracted instead of added [Notes I: to isolate x, add 4 to both sides]"),
        dict(kind="mc", latex="4(x - 2) = 2(x + 5)",
             qtext="Solve 4(x − 2) = 2(x + 5) for x.",
             hint="Distribute on both sides.", steps=["[equation] Distribute:  $4x - 8 = 2x + 10$",
                                                      "Take 2x from both sides:  $2x - 8 = 10$",
                                                      "Add 8:  $2x = 18$",
                                                      "Divide by 2:  $x = 9$",
                                                      "Check:  $4(9 - 2) = 28$  and  $2(9 + 5) = 28$"],
             choices=["$x = 3.5$", "$x = 1$", "$x = 9$", "$x = 3$"], correct=2, answer="C — x = 9",
             errors={"A": "each multiplier to its first term only: 4x − 2 = 2x + 5, so 2x = 7 [Florida B1G-M, AR.2.1: distributing to only one term]", "B": "4(−2) taken as +8: 4x + 8 = 2x + 10, so 2x = 2 [Florida B1G-M, AR.2.1: sign errors while distributing]", "D": "the x-terms added: 6x − 8 = 10, so 6x = 18 [Notes I: take the same term from both sides]"},
             note="Diagnostic: three different named errors — option A distributes each multiplier to its first term only, option B loses the sign of 4(−2), option D adds the x-terms. Ask a room that chose C to check 9 in both sides: 28 and 28.",
             check=("many", solves("4*(u - 2)", "2*(u + 5)", "9"),
                    solves("4*u - 2", "2*u + 5", "F(7,2)"), solves("4*u + 8", "2*u + 10", "1"), solves("4*u - 8 + 2*u", "10", "3"))),
        dict(text=["A gym is open 7 days a week. It has two plans:", "\\$30 a month plus \\$5 a visit, or \\$8 a visit.", "**After how many visits in a month do the plans cost the same?"],
             unneeded="7",
             hint="Write each plan's cost.", steps=["[equation] v visits at the same cost:  $30 + 5v = 8v$",
                                                    "Take 5v from both sides:  $30 = 3v$",
                                                    "Divide by 3:  $v = 10$",
                                                    "Check:  $30 + 5(10) = 80$  and  $8(10) = 80$"],
             gloss="30 + 5v = 8v", answer="10 visits",
             note="The extra-number board (ruling 22): the gym's 7 days a week is not needed. Notes II's last line modeled the writing. Each plan's cost is an expression in v; the two plans cost the same when the expressions are equal, 30 + 5v = 8v. Take 5v (the smaller) from both sides. Check: both plans cost \\$80 at 10 visits.",
             check=solves("30 + 5*u", "8*u", "10"),
             wrong="about 2.3 visits — 13v = 30, the 5v and 8v added [Notes I: take the same term from both sides]; 6 visits — 30 ÷ 5, the \\$8 plan left out [both plans' costs are equal]; 7 visits — the days in a week taken as the answer [an extra number, included on purpose]"),
        dict(text=["The solution of  $5x + □ = 2x + 16$  is  $x = 3$.", "**What number goes in the box?"],
             hint="Put 3 in for x.", steps=["Put 3 in for x:  $5(3) = 15$  and  $2(3) + 16 = 22$",
                                            "$15 + □ = 22$,  so the box is  $22 - 15 = 7$"],
             gloss="15 + 7 = 22", answer="7",
             note="Backwards: the solution is given and a number in the equation is missing. Put 3 in for x on BOTH sides — the right side is 22, the left is 15 + □. Check: 5(3) + 7 = 22 and 2(3) + 16 = 22.",
             check=("many", solves("5*3 + u", "2*3 + 16", "7"), solves("5*u + 7", "2*u + 16", "3")),
             wrong="22 — the value of the right side, one step short [the box is what is added to 15]; 1 — 15 plus the box set equal to 16, the 2x left out of the right side [put 3 in on both sides]"),
        dict(kind="written", text=["$2x + 15 = 6x - 9$", "Kai starts by taking 2x from both sides.", "Lena starts by taking 6x from both sides.", "**Solve for x both ways. Do they get the same solution?"],
             qtext="2x + 15 = 6x − 9. Kai starts by taking 2x from both sides; Lena starts by taking 6x from both sides. Solve for x both ways. Do they get the same solution?",
             hint="Each step is done to both sides.", steps=["Kai:  $15 = 4x - 9$,  $24 = 4x$,  $x = 6$",
                                                             "Lena:  $-4x + 15 = -9$,  $-4x = -24$,  $x = 6$",
                                                             "Check:  $2(6) + 15 = 27$  and  $6(6) - 9 = 27$"],
             gloss="x = 6 both ways", answer="Yes, x = 6 both ways.",
             te_answer="Full credit: both routes carried to x = 6 (Kai: 15 = 4x − 9, 4x = 24; Lena: −4x + 15 = −9, −4x = −24) AND the reason — each step is done to both sides, so the equation stays true whichever variable term is taken; a check, 27 = 27, earns it too. 'x = 6' with one route only does not.",
             note="Written, and the exit evidence. Read two aloud: one that names the reason (the same step done to both sides), one that checks 6 in both sides. Lena divides by −4 — the room that forgets the sign gets −6, and the check exposes it: 2(−6) + 15 = 3, 6(−6) − 9 = −45.",
             check=("many", solves("2*u + 15", "6*u - 9", "6"), solves("15", "4*u - 9", "6"), solves("-4*u + 15", "-9", "6"),
                    same("(2*u + 15) - 2*u", "15"), same("(6*u - 9) - 6*u", "-9")),
             wrong="Lena x = −6 — −4x = −24 divided to −6, the sign lost [Notes II: a negative divided by a negative]; 'Lena is wrong to take 6x' — a legal move, the same on both sides [Notes II: either side works]"),
    ],

    independent=[
        dict(stem="Solve for w:  $11w - 7 = 4w + 35$", answer="w = 6", why="Take 4w: 7w − 7 = 35; 7w = 42. Check: 59 = 59.",
             check=solves("11*u - 7", "4*u + 35", "6"), space=0.9),
        dict(stem="Solve for h:  $3h + 10 = 8h + 45$", answer="h = −7", why="Take 3h: 10 = 5h + 45; −35 = 5h. Check: −11 = −11.",
             check=solves("3*u + 10", "8*u + 45", "-7"), space=0.9),
        dict(stem="Solve for p:  $5(p - 3) = 2p + 12$", answer="p = 9", why="5p − 15 = 2p + 12; 3p − 15 = 12; 3p = 27. Check: 30 = 30.",
             check=solves("5*(u - 3)", "2*u + 12", "9"), space=0.9),
        dict(stem="Solve for k:  $3(k + 6) = 5(k - 2)$", answer="k = 14", why="3k + 18 = 5k − 10; 18 = 2k − 10; 28 = 2k. Check: 60 = 60.",
             check=solves("3*(u + 6)", "5*(u - 2)", "14"), space=0.9),
        dict(stem="Solve for t:  $0.5(6t + 4) = t + 9$", answer="t = 3.5", why="3t + 2 = t + 9; 2t + 2 = 9; 2t = 7. The 0.5 multiplies both terms. Check: 12.5 = 12.5.",
             check=solves("F(1,2)*(6*u + 4)", "u + 9", "F(7,2)"), space=0.9),
        dict(stem="A skating rink charges \\$9 a visit, or \\$24 a month plus \\$5 a visit. After how many visits in a month do the two plans cost the same?",
             answer="6 visits", why="9v = 24 + 5v; 4v = 24. Check: both cost \\$54.",
             check=solves("9*u", "24 + 5*u", "6"), space=0.9),
    ],

    # Bank: both sides, no parentheses (1–3: a whole solution, a larger constant, a negative solution), parentheses
    # (4–6: on one side, on both, on both with a decimal solution), the decimal factor (7–8, the 21% skill),
    # backwards (9), two plans (10), the diagnostic mc (11), select-all (12). The additional bank mirrors it
    # position by position with new numbers.
    bank=[
        dict(heading="For questions 1 through 3, solve the equation."),
        dict(stem="$7p + 3 = 4p + 27$", answer="p = 8", why="3p + 3 = 27; 3p = 24.", check=solves("7*u + 3", "4*u + 27", "8"), space=0.7),
        dict(stem="$10m - 6 = 3m + 22$", answer="m = 4", why="7m − 6 = 22; 7m = 28.", check=solves("10*u - 6", "3*u + 22", "4"), space=0.7),
        dict(stem="$2q + 5 = 7q + 25$", answer="q = −4", why="5 = 5q + 25; −20 = 5q. The larger q-term is on the right, so the solution is negative.", check=solves("2*u + 5", "7*u + 25", "-4"), space=0.7),
        dict(heading="For questions 4 through 6, distribute, then solve."),
        dict(stem="$4(y + 3) = 7y - 9$", answer="y = 7", why="4y + 12 = 7y − 9; 12 = 3y − 9; 21 = 3y.", check=solves("4*(u + 3)", "7*u - 9", "7"), space=0.8),
        dict(stem="$5(k - 1) = 3(k + 5)$", answer="k = 10", why="5k − 5 = 3k + 15; 2k − 5 = 15; 2k = 20.", check=solves("5*(u - 1)", "3*(u + 5)", "10"), space=0.8),
        dict(stem="$3(2w - 1) = 2(w + 5)$", answer="w = 3.25", why="6w − 3 = 2w + 10; 4w − 3 = 10; 4w = 13.", check=solves("3*(2*u - 1)", "2*(u + 5)", "F(13,4)"), space=0.8),
        dict(heading="For questions 7 and 8, the factor is a decimal. Solve the equation."),
        dict(stem="$0.5(8x + 6) = x + 12$", answer="x = 3", why="4x + 3 = x + 12; 3x + 3 = 12; 3x = 9.", check=solves("F(1,2)*(8*u + 6)", "u + 12", "3"), space=0.8),
        dict(stem="$0.2(10t - 5) = t + 4$", answer="t = 5", why="2t − 1 = t + 4; t − 1 = 4.", check=solves("F(1,5)*(10*u - 5)", "u + 4", "5"), space=0.8),
        dict(heading="Find the missing number."),
        dict(stem="The solution of $6x - □ = 2x + 9$ is $x = 4$. What number goes in the box?", answer="7", why="Put 4 in for x: 24 minus the box is 8 + 9 = 17, so the box is 7.",
             check=("many", solves("6*4 - u", "2*4 + 9", "7"), solves("6*u - 7", "2*u + 9", "4")), space=0.8),
        dict(heading="Solve the problem."),
        dict(stem="A swim club charges \\$6 a visit, or \\$20 a month plus \\$2 a visit. After how many visits in a month do the two plans cost the same?", answer="5 visits", why="6v = 20 + 2v; 4v = 20. Both cost \\$30.",
             check=solves("6*u", "20 + 2*u", "5"), space=0.7),
        dict(heading="Choose one."),
        dict(stem="Solve for x:  $3(x - 4) = x + 6$", choices=["$x = 9$", "$x = 4.5$", "$x = 5$", "$x = -3$"], correct=0, answer="A",
             why="3x − 12 = x + 6; 2x − 12 = 6; 2x = 18.",
             check=("many", solves("3*(u - 4)", "u + 6", "9"), solves("3*u - 4", "u + 6", "5"),
                    solves("3*u + 12", "u + 6", "-3"), solves("3*u - 12 + u", "6", "F(9,2)")),
             errors={"B": "the x-terms added: 4x − 12 = 6 [Notes I: take the same term from both sides]", "C": "the 3 to the first term only: 3x − 4 = x + 6 [Florida B1G-M, AR.2.1: distributing to only one term]", "D": "3(−4) taken as +12: 3x + 12 = x + 6 [Florida B1G-M, AR.2.1: sign errors while distributing]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the equations that have the same solution as $5x - 3 = 2x + 12$.",
             choices=["$3x = 15$", "$5x = 2x + 15$", "$7x - 3 = 12$", "$3x = 9$", "$3x - 3 = 12$"], correct=[0, 1, 4], answer="A, B, E",
             why="5x − 3 = 2x + 12 has x = 5, and so do A, B and E; C adds the x-terms (x = 15/7) and D takes the 3 the wrong way (x = 3).",
             check=("many", solves("5*u - 3", "2*u + 12", "5"), solves("3*u - 3", "12", "5"), solves("3*u", "15", "5"),
                    solves("5*u", "2*u + 15", "5"), not_root("7*u - 3", "12", "5"), not_root("3*u", "9", "5")),
             errors={"C": "the x-terms added: 5x + 2x [Notes I: take the same term from both sides]", "D": "the 3 subtracted instead of added: 3x = 12 − 3 [Notes I: to isolate x, add 3 to both sides]"}),
    ],

    additional=[
        dict(heading="For questions 1 through 3, solve the equation."),
        dict(stem="$8q + 5 = 3q + 40$", answer="q = 7", why="5q + 5 = 40; 5q = 35.", check=solves("8*u + 5", "3*u + 40", "7"), space=0.7),
        dict(stem="$9d - 8 = 4d + 17$", answer="d = 5", why="5d − 8 = 17; 5d = 25.", check=solves("9*u - 8", "4*u + 17", "5"), space=0.7),
        dict(stem="$3c + 4 = 8c + 34$", answer="c = −6", why="4 = 5c + 34; −30 = 5c. The larger c-term is on the right, so the solution is negative.", check=solves("3*u + 4", "8*u + 34", "-6"), space=0.7),
        dict(heading="For questions 4 through 6, distribute, then solve."),
        dict(stem="$3(a + 5) = 6a - 3$", answer="a = 6", why="3a + 15 = 6a − 3; 15 = 3a − 3; 18 = 3a.", check=solves("3*(u + 5)", "6*u - 3", "6"), space=0.8),
        dict(stem="$6(z - 2) = 4(z + 1)$", answer="z = 8", why="6z − 12 = 4z + 4; 2z − 12 = 4; 2z = 16.", check=solves("6*(u - 2)", "4*(u + 1)", "8"), space=0.8),
        dict(stem="$2(4s - 1) = 3(s + 2)$", answer="s = 1.6", why="8s − 2 = 3s + 6; 5s − 2 = 6; 5s = 8.", check=solves("2*(4*u - 1)", "3*(u + 2)", "F(8,5)"), space=0.8),
        dict(heading="For questions 7 and 8, the factor is a decimal. Solve the equation."),
        dict(stem="$0.5(6x + 8) = x + 14$", answer="x = 5", why="3x + 4 = x + 14; 2x + 4 = 14; 2x = 10.", check=solves("F(1,2)*(6*u + 8)", "u + 14", "5"), space=0.8),
        dict(stem="$0.2(15t - 10) = t + 6$", answer="t = 4", why="3t − 2 = t + 6; 2t − 2 = 6; 2t = 8.", check=solves("F(1,5)*(15*u - 10)", "u + 6", "4"), space=0.8),
        dict(heading="Find the missing number."),
        dict(stem="The solution of $4x + □ = x + 23$ is $x = 5$. What number goes in the box?", answer="8", why="Put 5 in for x: 20 plus the box is 5 + 23 = 28, so the box is 8.",
             check=("many", solves("4*5 + u", "5 + 23", "8"), solves("4*u + 8", "u + 23", "5")), space=0.8),
        dict(heading="Solve the problem."),
        dict(stem="A bike shop rents bikes for \\$7 an hour, or \\$18 plus \\$4 an hour. After how many hours do the two plans cost the same?", answer="6 hours", why="7h = 18 + 4h; 3h = 18. Both cost \\$42.",
             check=solves("7*u", "18 + 4*u", "6"), space=0.7),
        dict(heading="Choose one."),
        dict(stem="Solve for x:  $5(x - 2) = x + 26$", choices=["$x = 6$", "$x = 7$", "$x = 4$", "$x = 9$"], correct=3, answer="D",
             why="5x − 10 = x + 26; 4x − 10 = 26; 4x = 36.",
             check=("many", solves("5*(u - 2)", "u + 26", "9"), solves("5*u - 2", "u + 26", "7"),
                    solves("5*u + 10", "u + 26", "4"), solves("5*u - 10 + u", "26", "6")),
             errors={"A": "the x-terms added: 6x − 10 = 26 [Notes I: take the same term from both sides]", "B": "the 5 to the first term only: 5x − 2 = x + 26 [Florida B1G-M, AR.2.1: distributing to only one term]", "C": "5(−2) taken as +10: 5x + 10 = x + 26 [Florida B1G-M, AR.2.1: sign errors while distributing]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the equations that have the same solution as $6x + 4 = 2x + 28$.",
             choices=["$6x = 2x + 24$", "$4x = 24$", "$4x = 32$", "$4x + 4 = 28$", "$8x + 4 = 28$"], correct=[0, 1, 3], answer="A, B, D",
             why="6x + 4 = 2x + 28 has x = 6, and so do A, B and D; E adds the x-terms (x = 3) and C adds the 4 instead of subtracting it (x = 8).",
             check=("many", solves("6*u + 4", "2*u + 28", "6"), solves("4*u + 4", "28", "6"), solves("4*u", "24", "6"),
                    solves("6*u", "2*u + 24", "6"), not_root("8*u + 4", "28", "6"), not_root("4*u", "32", "6")),
             errors={"C": "the 4 added instead of subtracted: 4x = 28 + 4 [Notes I: to isolate x, subtract 4 from both sides]", "E": "the x-terms added: 6x + 2x [Notes I: take the same term from both sides]"}),
    ],

    te=dict(
        say=["Take the same variable term from both sides — the balance stays level only if both sides lose the same thing.",
             "Either term may go; taking the smaller one keeps the coefficient positive.",
             "Check the solution in both sides of the first equation: the same number twice."],
        must="Students solve multi-step equations with the variable on both sides, using the distributive property and combining like terms, and they verify each solution by substituting it into both sides.",
        must_not="Equations with no solution or infinitely many solutions are taught in Lesson 11.03. Clearing fractions and negative decimal factors are taught in Lesson 11.04.",
        read_first=[
            "The unit's second day. Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §11.02), then read against Math Nation 11.2 (the unit audit, Part 1). The new move is one: take the same variable term from both sides — written out once (Notes I's second line, − 3x on each side) and named, the subtraction property of equality. Everything after it is 11.01 and Unit 1. Notes II shows one route only (the smaller term); the second route is said aloud and done in writing on board 9. Notes II's last line writes two plans as one equation (12 + 3v = 5v) so that board 7 and set question 6 are practice, not a first attempt.",
            "Every multiple-choice wrong option is one of the B1G-M's named AR.2.1 errors — distributing to only one term, a sign error while distributing — or a named slip (the x-terms added instead of one taken from both sides; a constant moved the wrong way; a sign lost at the last step).",
            "Not reproduced from the book: the 11.2.1 hanger warm-up (a preview, not spaced retrieval, §16 rule 5 — and its second hanger, 12 + 2p = 2p + 12, is an identity nobody flags, which belongs to 11.03); the 11.2.2 algebra-tile exploration (discovery in first teaching, §16 rule 6; and its tiles are unreadable in grayscale); the partner work in 11.2.2 (§1 rule 4); the benchmark codes on the student pages; and the key's 'a coefficient of −1 that must be eliminated' (audit T4 — a coefficient is made 1, not eliminated; Notes II divides by −4 and says so).",
            "Standing decision 5 asks for a decimal coefficient every day: here it is set question 5, 0.5(6t + 4) = t + 9, which is also the set's decimal solution (t = 3.5), and bank questions 7–8 (additional 7–8). Standing decision 6, the check by substitution, is today's habit: every worked row, every answer slide and every set answer checks in both sides."],
        standard_notes=[("Clarification", "Problem types include equations that generate one solution, infinitely many solutions or no solution (Clarification 1) — today every equation has exactly one, and the other two endings are 11.03."),
                        ("Unit boundary", "Integer and decimal coefficients; the variable on both sides; whole, negative and decimal solutions. Solution form x = a (B1G-M); verify by substitution.")],
        sits="The unit's second day, after 11.01's like terms and distribution. IXL ZYL is done today and due by the Unit 11 test (Fri 11 Dec). 11.03 runs the same move into equations whose variable terms cancel — a = a and a = b — and 11.07 checks a graphed crossing with an equation of today's kind.",
        lives="Notes I — the same variable term from both sides — and Notes II — either side works. Board 4 is the diagnostic on the move (x-terms added, a constant moved the wrong way, a sign lost); board 6 the diagnostic on distributing two sides; board 9 the two routes in writing.",
        materials="Whiteboards and markers. Hand out the Independent Set, one per student, after whiteboard question 9.",
        variation="Boards 1–2 take one variable term (the first with no constant beside the larger term, the second with a constant on each side). The pattern breaks at 3: the larger coefficient is on the right, so the solution is negative. 4 votes on the move; 5 distributes one side; 6 distributes both and votes on it; 7 is the two-plans story with the gym's 7 days as the extra number; 8 runs backwards; 9 solves one equation both ways in writing. The independent set walks the same path in six: a whole solution, a negative one, parentheses on one side, on both, a decimal factor with a decimal solution, and two plans that cost the same.",
        audit=["Every equation re-derived by sympy at build time over the real numbers (mathcheck: 0 findings); every multiple-choice distractor solved again from its named error; every answer slide's check row computed in both sides.",
               "Math Nation 11.2 read against this lesson (A7 Unit 11 Audit, Part 1 §1, §3–§5): no 11.2 student-facing defect was logged (14 of 14 checks agree); its shapes worth keeping — a step and its reason, solve and verify, a decimal solution (m = −6.15) — are here with our own numbers. The audit's §4 gaps met today: substitution in both sides on every item, a context (two plans), multiple choice with error-product distractors."],
        changes=["11.2.1 hanger warm-up → four retrieval questions, the prerequisite (2x − 5x) in the last slot; the balance idea moves into Notes I, said from the front.",
                 "11.2.2 algebra-tile exploration (pairs) → Notes I–II, taught from the front: take the same variable term from both sides, and either side works.",
                 "11.2.3 guided step tables (constant / variable term / isolate) → Notes III, the examples' worked rows (each step with its reason) and boards 1–6.",
                 "11.2.4 Your Turn with substitution → the check in both sides on every answer slide and the Independent Set."],
    ),
)
