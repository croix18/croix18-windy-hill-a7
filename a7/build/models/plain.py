# MODEL: a lesson with no figures — A7 11.03 One Solution, No Solution, Infinitely Many Solutions (MA.8.AR.2.1), as built.
# Read with kit/BUILDER CARD.md. Copy it to uN/lNN.py and change EVERY field; it builds at 0 findings in u11/.
# Equations are checked over the REAL numbers (the kit's own letters are positive): solves / same / never below.
# A false ending ("8 = 5") is printed in a worked row with its words; in `steps` it is tagged [false], and the
# equation before it [equation], so stepcheck holds each line to what it declares.

U = "sp.Symbol('u', real=True)"


def _u(e):
    import re
    return re.sub(r"\bu\b", U, e)


def solves(left, right, value):
    """sympy solves left = right (in u) and finds exactly one solution, `value`."""
    return ("eq", "sp.solve(sp.Eq(" + _u(left) + ", " + _u(right) + "), " + U + ")[0]", value)


def same(e1, e2):
    """Two expressions in u are the same expression: as an equation, true for every number (infinitely many)."""
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


ASK = "**How many solutions does it have? If it has one, find it."

L = dict(
    code="11.03", unit=11, lesson_no=3,
    align="=",
    title="One Solution, No Solution, Infinitely Many Solutions",
    unit_title="Solving Equations and Systems",
    benchmark="MA.8.AR.2.1",
    benchmark_text="Solve multi-step linear equations in one variable, with rational number coefficients. Include equations with variables on both sides.",
    target="I can tell whether an equation has one solution, no solution or infinitely many solutions.",
    essential="When every variable term is gone, how does what is left tell us how many solutions there are?",
    building_on="Lesson 11.02 took the same variable term from both sides of an equation. Lesson 11.01 collected like terms and distributed. Lesson 1.03 (Unit 1) solved two-step equations.",
    working_toward="Lesson 11.04 meets the same three outcomes in equations with fraction and decimal coefficients. In Lessons 11.05–11.08, a system of equations also has one solution, no solution (parallel lines) or infinitely many solutions (the same line).",
    vocab=[("no solution", "the equation is never true, whatever number the variable is; it ends at a false statement, like $5 = 9$"),
           ("infinitely many solutions", "the equation is true for every number; it ends at a true statement, like $5 = 5$")],
    ixl=["Find the number of solutions — XDE", "Create equations with no solutions or infinitely many solutions — 7TY"],
    closure="Whiteboard question 9 is answered in writing and serves as the exit ticket. A complete answer says that neither student is right and gives the reason: 3(x + 4) − 12 = 3x simplifies to 3x = 3x, and 0 = 0 is true for every number, so the equation has infinitely many solutions. An answer of \"neither\" with no reason is not complete.",

    mtr=[("MTR.5.1", "Students read the number of solutions from the structure of the two sides, comparing the x-terms and then the constants, before they finish solving (Notes II and whiteboard questions 1, 2 and 6)."),
         ("MTR.4.1", "On whiteboard questions 4 and 6, a divided class has one minute to convince a neighbor and then votes again."),
         ("MTR.6.1", "Students check the solution x = 0 in both sides (whiteboard question 3) and explain what the statement 0 = 0 means (whiteboard question 9).")],
    hoq=[("Why does 5 = 9 mean no solution, even though we never tried a single number?", "DOK 2"),
         ("5x + 4 = 2x + 4 and 5x + 4 = 5x + 4 both have 4 on each side. Why does one have one solution and the other infinitely many?", "DOK 3"),
         ("Write an equation with no solution that has 7x on the left side. How do you know it has none?", "DOK 2")],
    differentiation=[
        ("ESE / 504", "Keep three lines on display all period, each with its example: \"x = a: one solution,\" \"a = a, always true: infinitely many solutions\" and \"a = b, never true: no solution.\" On every whiteboard question, students simplify each side and circle the two x-terms, then decide whether the x-terms are the same or different."),
        ("ELL", "**Infinitely many**: so many that there is no end, because every number works. **No solution**: no number works. **Always true / never true**: a statement like 5 = 5 is always true, and a statement like 5 = 9 is never true."),
        ("Enrichment", "Students who finish whiteboard question 8 early fill both boxes so that $□(x + 2) = 3x + □$ has infinitely many solutions (3 and 6). They then change one box so that the equation has no solution (3 and any number except 6).")],

    warmup=[
        dict(stem="Solve for x:  $6x - 4 = 2x + 20$", answer="x = 6",
             check=solves("6*u - 4", "2*u + 20", "6")),
        dict(stem="An exterior angle is 130°. One remote interior angle is 55°. Find the other remote interior angle.", answer="75°",
             check=("eq", "130 - 55", "75")),
        dict(stem="Find the distance from (1, 2) to (4, 6).", answer="5",
             check=("eq", "sqrt((4 - 1)**2 + (6 - 2)**2)", "5")),
        dict(stem="Is  $x = 2$  a solution of  $3x + 1 = 7$?", answer="Yes, because 3(2) + 1 = 7",
             check=("eq", "3*2 + 1", "7")),
    ],

    notes=[
        dict(numeral="I", head="Three endings", min=4,
             math=["$2x + 5 = 3x + 9 \\qquad x = -4 \\qquad \\text{one solution}$",
                   "$2x + 5 = 2x + 9 \\qquad 5 = 9 \\qquad \\text{never true: no solution}$",
                   "$2x + 5 = 2x + 5 \\qquad 5 = 5 \\qquad \\text{always true: infinitely many}$"],
             items2=["**Take 2x from both sides. Read what is left.**"],
             letters=False),
        dict(numeral="II", head="See it before the end", min=3,
             math=["$3(x + 2) = 3x + 6 \\qquad 3x + 6 = 3x + 6 \\qquad \\text{infinitely many}$",
                   "$3(x + 2) = 3x + 2 \\qquad 3x + 6 = 3x + 2 \\qquad \\text{no solution}$"],
             items2=["**Same x-terms, same constants: infinitely many.  Same x-terms, different constants: none.  Different x-terms: one.**"],
             letters=False),
        dict(numeral="III", head="Zero is a number", min=3,
             math=["$4x + 7 = 7 - 2x$", "$6x + 7 = 7$", "$6x = 0$", "$x = 0$"],
             items2=["**One solution: x = 0. Zero is a number.**", "Check:  $4(0) + 7 = 7$   and   $7 - 2(0) = 7$"],
             letters=False),
    ],

    examples=[
        dict(title="Example 1", min_q=1,
             prompt=["$4(x - 3) + 2 = 4x - 10$"], ask="How many solutions does it have?",
             worked=[dict(min=2,
                          rows=[("4(x - 3) + 2 = 4x - 10", "the equation"),
                                ("4x - 12 + 2 = 4x - 10", "4 times x, 4 times −3"),
                                ("4x - 10 = 4x - 10", "the same on both sides"),
                                ("-10 = -10 \\qquad \\text{always true}", "take 4x from both sides")],
                          answer="infinitely many solutions")],
             check=same("4*(u - 3) + 2", "4*u - 10"),
             your_turn=dict(min=2,
                            prompt=["$3(2x + 1) - 5 = 6x - 2$", "How many solutions are there? Write your last line and what it means."],
                            steps=["Distribute:  $6x + 3 - 5 = 6x - 2$",
                                   "Collect:  $6x - 2 = 6x - 2$",
                                   "Take 6x from both sides:  $-2 = -2$,  always true"],
                            answer="infinitely many solutions"),
             yt_check=same("3*(2*u + 1) - 5", "6*u - 2")),
        dict(title="Example 2", min_q=1,
             prompt=["$2(3x + 4) = 6x + 5$"], ask="How many solutions does it have?",
             worked=[dict(min=2,
                          rows=[("2(3x + 4) = 6x + 5", "the equation"),
                                ("6x + 8 = 6x + 5", "2 times 3x, 2 times 4"),
                                ("8 = 5 \\qquad \\text{never true}", "take 6x from both sides")],
                          answer="no solution")],
             check=never("2*(3*u + 4)", "6*u + 5"),
             your_turn=dict(min=2,
                            prompt=["$5(2x - 1) = 10x + 3$", "How many solutions are there? Write your last line and what it means."],
                            steps=["[equation] Distribute:  $10x - 5 = 10x + 3$",
                                   "[false] Take 10x from both sides:  $-5 = 3$,  never true: no solution"],
                            answer="no solution"),
             yt_check=never("5*(2*u - 1)", "10*u + 3")),
    ],

    # The round: the same expression on both sides (1), the same x-terms with different constants (2), one solution
    # that is 0 (3), the diagnostic on reading an identity (4), parentheses hiding an ordinary negative solution (5), which
    # of four has none (6), the two-plans story with no crossing and an extra number (7), backwards: fill a box for
    # each ending (8), and the x = 0 / no-solution misreadings of 0 = 0 in writing (9). The pattern breaks at 3: the
    # constants match and the x-terms do not, so it LOOKS like an ending of the new kind and is x = 0.
    whiteboard=[
        dict(text=["$7x + 2 = 7x + 2$", ASK],
             steps=["Both sides are  $7x + 2$",
                                                   "Take 7x from both sides:  $2 = 2$,  always true"],
             answer="infinitely many solutions",
             check=same("7*u + 2", "7*u + 2"),
             wrong="x = 2 — the constant in 2 = 2 read as the answer [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]; no solution — the x's gone, so 'nothing works' [Notes I: a true sentence means every number]"),
        dict(text=["$3x + 8 = 3x - 1$", ASK],
             steps=["The x-terms match:  $3x$  and  $3x$",
                                                          "[false] Take 3x from both sides:  $8 = -1$,  never true: no solution"],
             answer="no solution",
             check=never("3*u + 8", "3*u - 1"),
             wrong="infinitely many — the x-terms match, so 'always true' [Notes II: the constants must match too]; x = 9 or x = −9 — 8 − (−1) or −1 − 8 written as an answer [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]"),
        dict(text=["$5x + 4 = 2x + 4$", ASK],
             steps=["Take 2x from both sides:  $3x + 4 = 4$",
                                                      "Subtract 4:  $3x = 0$",
                                                      "Divide by 3:  $x = 0$",
                                                      "Check:  $5(0) + 4 = 4$  and  $2(0) + 4 = 4$"],
             answer="one solution, x = 0",
             check=solves("5*u + 4", "2*u + 4", "0"),
             wrong="no solution — 3x = 0 read as 'nothing left' [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant; Notes III: zero is a number]; infinitely many — the matching constants taken for the same sides [Notes II: the x-terms differ, so one solution]"),
        dict(kind="mc", text=["$2(4x + 3) = 8x + 6$", "**How many solutions does it have?"],
             qtext="How many solutions does 2(4x + 3) = 8x + 6 have?",
             steps=["Distribute:  $8x + 6 = 8x + 6$",
                                                      "Take 8x from both sides:  $6 = 6$,  always true"],
             choices=["one solution, $x = 0$", "infinitely many solutions", "no solution", "one solution, $x = 6$"], correct=1,
             answer="B — infinitely many solutions",
             errors={"A": "0 = 0 (taking 8x and 6) read as x = 0 [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]", "C": "the x-terms gone, so 'nothing is left' — but 6 = 6 is left, and it is true [Notes I: a true sentence means every number]", "D": "the constant in 6 = 6 taken for the answer [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]"},
             check=("many", same("2*(4*u + 3)", "8*u + 6"), not_never("2*(4*u + 3)", "8*u + 6"))),
        dict(text=["$6x - 9 = 3(x - 4)$", ASK],
             steps=["Distribute:  $3(x - 4) = 3x - 12$",
                                              "Take 3x from both sides:  $3x - 9 = -12$",
                                              "Add 9:  $3x = -3$",
                                              "Divide by 3:  $x = -1$",
                                              "Check:  $6(-1) - 9 = -15$  and  $3(-1 - 4) = -15$"],
             answer="one solution, x = −1",
             check=("many", solves("6*u - 9", "3*(u - 4)", "-1"), solves("6*u - 9", "3*u - 4", "F(5,3)"),
                    solves("6*u - 9", "3*u + 12", "7"), solves("3*u", "-12 - 9", "-7")),
             wrong="no solution — the verdict read before distributing [Notes II: simplify each side first; different x-terms: one]; x = 5/3 — 6x − 9 = 3x − 4, the 3 to one term only [Florida B1G-M, AR.2.1: distributing to only one term]; x = 7 — 6x − 9 = 3x + 12, 3(−4) taken as +12 [Florida B1G-M, AR.2.1: sign errors while distributing]; x = −7 — 3x = −12 − 9, the 9 subtracted instead of added [11.02 Notes I: to isolate x, add 9 to both sides]"),
        dict(kind="mc", text=["**Which equation has no solution?"],
             qtext="Which equation has no solution?",
             steps=["$3x + 1$  and  $3x - 1$:  the same x-terms",
                                                              "[false] Take 3x from both sides:  $1 = -1$,  never true: no solution"],
             choices=["$3x + 1 = x + 1$", "$3x + 1 = 2x$", "$3x + 1 = 1 + 3x$", "$3x + 1 = 3x - 1$"], correct=3,
             answer="D — 3x + 1 = 3x − 1: no solution",
             errors={"A": "2x = 0 read as 'no solution' — it has one, x = 0 [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]", "B": "different x-terms, so one solution, x = −1 [Notes II: different x-terms: one]", "C": "the same two terms in a different order — infinitely many [Notes II: same x-terms, same constants]"},
             check=("many", never("3*u + 1", "3*u - 1"), solves("3*u + 1", "u + 1", "0"), same("3*u + 1", "1 + 3*u"),
                    solves("3*u + 1", "2*u", "-1"), not_never("3*u + 1", "u + 1"), not_never("3*u + 1", "1 + 3*u"), not_never("3*u + 1", "2*u"))),
        dict(text=["Plan A costs \\$15 a month plus \\$3 a gigabyte.", "Plan B costs \\$20 a month plus \\$3 a gigabyte.",
                   "Each plan has an 8 GB limit.", "**For how many gigabytes do the plans cost the same?"],
             unneeded="8",
             steps=["[equation] g gigabytes at the same cost:  $15 + 3g = 20 + 3g$",
                                                    "[false] Take 3g from both sides:  $15 = 20$,  never true: no solution",
                                                    "B always costs \\$5 more"],
             answer="Never. There is no solution.",
             check=never("15 + 3*u", "20 + 3*u"),
             wrong="5 GB — 20 − 15 written as gigabytes [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]; 8 GB — each plan's limit taken as the answer [an extra number, included on purpose]; 'every amount' — the same \\$3 taken for the same cost [Notes II: the constants differ]"),
        dict(text=["Fill the box so  $4(x + 3) = 4x + □$  has infinitely many solutions.",
                   "Then fill the box so  $2(3x - 5) = □x + 1$  has no solution."],
             steps=["$4(x + 3)$  is  $4x + 12$:  the box is 12",
                                                      "$2(3x - 5)$  is  $6x - 10$:  the box is 6",
                                                      "[equation] With 6 in the box:  $6x - 10 = 6x + 1$",
                                                      "[false] Take 6x from both sides:  $-10 = 1$,  never true: no solution"],
             answer="12; then 6 (no solution)",
             check=("many", same("4*(u + 3)", "4*u + 12"), never("2*(3*u - 5)", "6*u + 1"), not_every("4*(u + 3)", "4*u + 3")),
             wrong="3 — the 4 never reached the 3 [Florida B1G-M, AR.2.1: distributing to only one term]; 3 in the second box — 2(3x) read as 3x, which leaves an x: one solution [Notes II: the x-terms must match]"),
        dict(kind="written", text=["Mia and Jo both solved  $3(x + 4) - 12 = 3x$  and ended at  $0 = 0$.",
                                   "Mia wrote “x = 0”. Jo wrote “no solution”.", "**Who is right? Explain."],
             qtext="Mia and Jo both solved 3(x + 4) − 12 = 3x and ended at 0 = 0. Mia wrote “x = 0”. Jo wrote “no solution”. Who is right? Explain.",
             steps=["Distribute:  $3x + 12 - 12 = 3x$,  so  $3x = 3x$",
                                                       "Take 3x from both sides:  $0 = 0$,  always true",
                                                       "Every number works: infinitely many solutions"],
             answer="Neither: infinitely many solutions",
             check=("many", same("3*(u + 4) - 12", "3*u"), not_never("3*(u + 4) - 12", "3*u")),
             wrong="Mia — 0 = 0 read as x = 0 [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]; Jo — the x's gone, so 'nothing works' [Notes I: a true sentence means every number]"),
    ],

    independent=[
        dict(stem="How many solutions does  $6h - 5 = 2h + 19$  have? If it has one, find it.", answer="One solution, h = 6",
             why="Different h-terms. 4h − 5 = 19; 4h = 24. Check: 31 = 31.",
             check=solves("6*u - 5", "2*u + 19", "6"), space=0.9),
        dict(stem="How many solutions does  $0.5(6n - 4) = 3n + 2$  have? If it has one, find it.", answer="No solution",
             why="The 0.5 multiplies both terms: 3n − 2 = 3n + 2; take 3n: −2 = 2, never true.",
             check=("many", never("F(1,2)*(6*u - 4)", "3*u + 2"), same("F(1,2)*(6*u - 4)", "3*u - 2")), space=0.9),
        dict(stem="How many solutions does  $5(k + 2) - 3 = 5k + 7$  have? If it has one, find it.", answer="Infinitely many solutions",
             why="5k + 10 − 3 = 5k + 7; both sides are 5k + 7; take 5k: 7 = 7, always true.",
             check=same("5*(u + 2) - 3", "5*u + 7"), space=0.9),
        dict(stem="How many solutions does  $3(2v + 5) = 15 - v$  have? If it has one, find it.", answer="One solution, v = 0",
             why="6v + 15 = 15 − v; add v: 7v + 15 = 15; 7v = 0. Check: 15 = 15. Zero is a solution, not 'none'.",
             check=solves("3*(2*u + 5)", "15 - u", "0"), space=0.9),
        dict(stem="What number goes in the box so that  $6(x - 2) + 1 = 6x - □$  has infinitely many solutions?", answer="11",
             why="6x − 12 + 1 = 6x − 11, so the right side must be 6x − 11.",
             check=("many", same("6*(u - 2) + 1", "6*u - 11"), not_every("6*(u - 2) + 1", "6*u - 12")), space=0.9),
        dict(stem="What number goes in the box so that  $3(4x + 1) = □x + 7$  has no solution?", answer="12",
             why="3(4x + 1) = 12x + 3. With 12x on the right, 12x + 3 = 12x + 7 ends 3 = 7, never true; any other number leaves an x, so one solution.",
             check=("many", never("3*(4*u + 1)", "12*u + 7"), solves("3*(4*u + 1)", "4*u + 7", "F(1,2)")), space=0.9),
    ],

    # Bank: the three endings bare (1–3: none, infinitely many, x = 0), with parentheses (4–6: infinitely many, none,
    # one), the decimal factor (7–8, the 21% skill: infinitely many, none), backwards (9), two plans that never cost the
    # same (10), the diagnostic mc (11), select-all (12). The additional bank mirrors it position by position.
    bank=[
        dict(heading="For questions 1 through 3, tell how many solutions the equation has. If it has one, find it."),
        dict(stem="$8p - 3 = 8p + 6$", answer="No solution", why="Take 8p: −3 = 6, never true.", check=never("8*u - 3", "8*u + 6"), space=0.7),
        dict(stem="$2(5m + 3) = 10m + 6$", answer="Infinitely many solutions", why="10m + 6 = 10m + 6; 6 = 6, always true.", check=same("2*(5*u + 3)", "10*u + 6"), space=0.7),
        dict(stem="$7q + 5 = 3q + 5$", answer="One solution, q = 0", why="4q + 5 = 5; 4q = 0. Check: 5 = 5.", check=solves("7*u + 5", "3*u + 5", "0"), space=0.7),
        dict(heading="For questions 4 through 6, simplify each side, then tell how many solutions the equation has. If it has one, find it."),
        dict(stem="$3(2y - 5) + 4 = 6y - 11$", answer="Infinitely many solutions", why="6y − 15 + 4 = 6y − 11; both sides are 6y − 11.", check=same("3*(2*u - 5) + 4", "6*u - 11"), space=0.8),
        dict(stem="$4(3k + 2) = 12k - 8$", answer="No solution", why="12k + 8 = 12k − 8; 8 = −8, never true.", check=never("4*(3*u + 2)", "12*u - 8"), space=0.8),
        dict(stem="$5(r - 2) = 2r + 11$", answer="One solution, r = 7", why="5r − 10 = 2r + 11; 3r = 21. Check: 25 = 25.", check=solves("5*(u - 2)", "2*u + 11", "7"), space=0.8),
        dict(heading="For questions 7 and 8, the factor is a decimal. Tell how many solutions the equation has."),
        dict(stem="$0.5(4x + 10) = 2x + 5$", answer="Infinitely many solutions", why="2x + 5 = 2x + 5; the 0.5 multiplies both terms.", check=same("F(1,2)*(4*u + 10)", "2*u + 5"), space=0.8),
        dict(stem="$0.2(10t - 15) = 2t + 3$", answer="No solution", why="2t − 3 = 2t + 3; −3 = 3, never true.", check=never("F(1,5)*(10*u - 15)", "2*u + 3"), space=0.8),
        dict(heading="Find the missing number."),
        dict(stem="What number goes in the box so that $5(x - 4) = 5x - □$ has infinitely many solutions?", answer="20", why="5(x − 4) = 5x − 20.",
             check=("many", same("5*(u - 4)", "5*u - 20"), not_every("5*(u - 4)", "5*u - 4")), space=0.7),
        dict(heading="Solve the problem."),
        dict(stem="Gym A costs \\$25 to join and \\$10 a month. Gym B costs \\$40 to join and \\$10 a month. After how many months will the two gyms have cost the same?",
             answer="Never. There is no solution.", why="25 + 10m = 40 + 10m ends 25 = 40, never true; B always costs \\$15 more.",
             check=never("25 + 10*u", "40 + 10*u"), space=0.8),
        dict(heading="Choose one."),
        dict(stem="How many solutions does $2(3x - 4) = 6x - 4$ have?",
             choices=["one solution, $x = -4$", "one solution, $x = 0$", "no solution", "infinitely many solutions"], correct=2, answer="C",
             why="6x − 8 = 6x − 4; −8 = −4, never true.",
             check=("many", never("2*(3*u - 4)", "6*u - 4"), same("6*u - 4", "6*u - 4"), not_every("2*(3*u - 4)", "6*u - 4")),
             errors={"A": "the constant −4 taken for the answer [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]", "B": "the x's gone read as x = 0 [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]", "D": "the 2 to the first term only: 6x − 4 = 6x − 4 [Florida B1G-M, AR.2.1: distributing to only one term]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the equations that have no solution.",
             choices=["$4x + 9 = 4(x + 2) + 1$", "$4x + 9 = 4x - 9$", "$2(2x + 3) = 4x + 5$", "$4x + 9 = 9 + 4x$", "$4x + 9 = 9$"], correct=[1, 2], answer="B, C",
             why="B ends 9 = −9 and C ends 6 = 5, never true. A and D are the same on both sides (infinitely many); E has one solution, x = 0.",
             check=("many", never("4*u + 9", "4*u - 9"), never("2*(2*u + 3)", "4*u + 5"),
                    not_never("4*u + 9", "9 + 4*u"), not_never("4*u + 9", "9"), not_never("4*u + 9", "4*(u + 2) + 1"),
                    solves("4*u + 9", "9", "0"), same("4*u + 9", "4*(u + 2) + 1")),
             errors={"A": "the 4 to one term only gives 4x + 3 and looks like none; distributed fully, both sides are 4x + 9 [Florida B1G-M, AR.2.1: distributing to only one term]", "D": "the same two terms in a different order: infinitely many [Notes II: same x-terms, same constants]", "E": "4x = 0 has one solution, x = 0 [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]"}),
    ],

    additional=[
        dict(heading="For questions 1 through 3, tell how many solutions the equation has. If it has one, find it."),
        dict(stem="$6d + 7 = 6d - 2$", answer="No solution", why="Take 6d: 7 = −2, never true.", check=never("6*u + 7", "6*u - 2"), space=0.7),
        dict(stem="$3(4a - 1) = 12a - 3$", answer="Infinitely many solutions", why="12a − 3 = 12a − 3; −3 = −3, always true.", check=same("3*(4*u - 1)", "12*u - 3"), space=0.7),
        dict(stem="$9c - 4 = 2c - 4$", answer="One solution, c = 0", why="7c − 4 = −4; 7c = 0. Check: −4 = −4.", check=solves("9*u - 4", "2*u - 4", "0"), space=0.7),
        dict(heading="For questions 4 through 6, simplify each side, then tell how many solutions the equation has. If it has one, find it."),
        dict(stem="$2(4z + 3) - 7 = 8z - 1$", answer="Infinitely many solutions", why="8z + 6 − 7 = 8z − 1; both sides are 8z − 1.", check=same("2*(4*u + 3) - 7", "8*u - 1"), space=0.8),
        dict(stem="$6(s + 3) = 6s - 18$", answer="No solution", why="6s + 18 = 6s − 18; 18 = −18, never true.", check=never("6*(u + 3)", "6*u - 18"), space=0.8),
        dict(stem="$4(w + 1) = w + 19$", answer="One solution, w = 5", why="4w + 4 = w + 19; 3w = 15. Check: 24 = 24.", check=solves("4*(u + 1)", "u + 19", "5"), space=0.8),
        dict(heading="For questions 7 and 8, the factor is a decimal. Tell how many solutions the equation has."),
        dict(stem="$0.5(6x - 8) = 3x - 4$", answer="Infinitely many solutions", why="3x − 4 = 3x − 4; the 0.5 multiplies both terms.", check=same("F(1,2)*(6*u - 8)", "3*u - 4"), space=0.8),
        dict(stem="$0.25(8t + 12) = 2t + 5$", answer="No solution", why="2t + 3 = 2t + 5; 3 = 5, never true.", check=never("F(1,4)*(8*u + 12)", "2*u + 5"), space=0.8),
        dict(heading="Find the missing number."),
        dict(stem="What number goes in the box so that $3(x + 6) = 3x + □$ has infinitely many solutions?", answer="18", why="3(x + 6) = 3x + 18.",
             check=("many", same("3*(u + 6)", "3*u + 18"), not_every("3*(u + 6)", "3*u + 6")), space=0.7),
        dict(heading="Solve the problem."),
        dict(stem="Movie plan A costs \\$8 a month plus \\$2 a movie. Plan B costs \\$11 a month plus \\$2 a movie. For how many movies in a month do the two plans cost the same?",
             answer="Never. There is no solution.", why="8 + 2m = 11 + 2m ends 8 = 11, never true; B always costs \\$3 more.",
             check=never("8 + 2*u", "11 + 2*u"), space=0.8),
        dict(heading="Choose one."),
        dict(stem="How many solutions does $5(x - 2) = 5x - 2$ have?",
             choices=["no solution", "one solution, $x = 0$", "one solution, $x = 2$", "infinitely many solutions"], correct=0, answer="A",
             why="5x − 10 = 5x − 2; −10 = −2, never true.",
             check=("many", never("5*(u - 2)", "5*u - 2"), not_every("5*(u - 2)", "5*u - 2")),
             errors={"B": "the x's gone read as x = 0 [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]", "C": "the constant 2 taken for the answer [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]", "D": "the 5 to the first term only: 5x − 2 = 5x − 2 [Florida B1G-M, AR.2.1: distributing to only one term]"}),
        dict(heading="Select all that apply."),
        dict(stem="Select all the equations that have infinitely many solutions.",
             choices=["$2x + 7 = 2x - 7$", "$2x + 7 = 7 + 2x$", "$2x + 7 = 7$", "$5x + 2 = 5(x + 2)$", "$3(x + 1) = 3x + 3$"], correct=[1, 4], answer="B, E",
             why="B and E are the same on both sides. A ends 7 = −7 and D ends 2 = 10, never true; C has one solution, x = 0.",
             check=("many", same("2*u + 7", "7 + 2*u"), same("3*(u + 1)", "3*u + 3"),
                    not_every("2*u + 7", "2*u - 7"), not_every("2*u + 7", "7"), not_every("5*u + 2", "5*(u + 2)"),
                    never("2*u + 7", "2*u - 7"), solves("2*u + 7", "7", "0"), never("5*u + 2", "5*(u + 2)")),
             errors={"A": "the x-terms match, but the constants do not: no solution [Notes II: the constants must match too]", "C": "2x = 0 read as 'always true' — it has one solution, x = 0 [Florida B1G-M, AR.2.1: expecting the solution to look like variable = constant]", "D": "the 5 to one term only gives 5x + 2 on both sides; distributed fully the right is 5x + 10: no solution [Florida B1G-M, AR.2.1: distributing to only one term]"}),
    ],

    te=dict(
        must="Students recognize from the simplified equation whether it has one solution (x = a), infinitely many solutions (a = a) or no solution (a = b).",
        must_not="Equations with fraction and decimal coefficients are solved at length in Lesson 11.04. Students do not decide the number of solutions by testing a table of values.",
        read_first=[
            "The 43-minute day (Wed 2 Dec). The kit's timing table must total 53, so the table below is the full lesson and this is the cut: warm-up 4 minutes (two silent, reveal, no discussion); skip board 1 (Example 1's twin) and board 7 (the story); board 9 answered aloud and two read, not written by all; Independent Set questions 1, 2 and 4 in class, questions 3, 5 and 6 go home; IXL starts outside class. That takes out 10 minutes. Never cut board 3 (x = 0, the boundary case), boards 4 and 6 (the two diagnostics), board 5 (the only ordinary one-solution board) or board 8 (the Unit 11 test's question 6).",
            "The unit's third day. Built from the benchmark and the B1G-M first (the unit's Lesson Outlines, §11.03), then read against Math Nation 11.3 (the unit audit, Part 1). The three endings are named from today on (standing decision 4).",
            "A false ending is written as the false equation with its words — '8 = 5, never true: no solution' — never as '8 ≠ 5' (the audit's decision 1). The answer slides' steps say it in words ('the left is 8, the right is 5 — never equal') because the build's step check holds every printed equation true.",
            "Every multiple-choice wrong option is a named AR.2.1 error — expecting the solution to look like variable = constant (a constant read as x, 0 = 0 read as x = 0, x = 0 read as 'none'), distributing to only one term — or a named slip (matching x-terms taken for the same sides).",
            "Not reproduced from the book: the perimeter warm-up (a preview, not retrieval), the partner tasks (§1 rule 4), the 11.3.3 exploration that offers five substitutions as proof of 'no solution' or 'all values' (audit D4 — here every ending is reached by simplifying; board 9's note says why trying numbers is not proof), and the Samir key that never says a = 0 (D5 — board 3, Notes III and set question 4 each say the solution is 0)."],
        materials="Whiteboards and markers. Hand out the Independent Set, one per student, after whiteboard question 9. On a 43-minute day, shorten the warm-up to 4 minutes: two minutes of silent work, then the answers. Skip whiteboard question 1, which is the same kind of equation as Example 1, and question 7, the two data plans. Take question 9 aloud and read two students\' boards to the class. Questions 1, 2 and 4 of the Independent Set are done in class, questions 3, 5 and 6 go home, and IXL starts outside class. Together these cuts save 10 minutes. Do not cut whiteboard question 3 (the solution x = 0), questions 4 and 6 (the two votes), question 5 (the only ordinary equation with one solution) or question 8 (the kind of question the test asks as its question 6).",
        variation="Boards 1–2 are bare: the same expression (infinitely many), then the same x-terms with different constants (none). The pattern breaks at 3: the constants match and the x-terms do not, so the answer is x = 0. 4 votes on an identity hidden by parentheses; 5 has parentheses too and an ordinary one solution, x = −1 — the one board where 'if one, find it' means a negative number; 6 picks the no-solution equation from four look-alikes; 7 is two plans that never cost the same, with the 8 GB limit as the extra number; 8 fills a box for each ending; 9 is written. The independent set walks the same path in six; question 2 is the day's decimal factor (0.5(6n − 4) = 3n + 2, no solution).",
        audit=["Every equation re-derived by sympy at build time over the real numbers (mathcheck: 0 findings): each one-solution answer solved, each 'infinitely many' shown to be the same expression on both sides, each 'no solution' shown to leave a nonzero number; every multiple-choice distractor re-derived from its named error.",
               "Math Nation 11.3 read against this lesson (A7 Unit 11 Audit, Part 1 §1, §3–§5): D4 and D5 not reproduced; the audit's §4 gaps met today — x = 0 asked for and keyed (board 3, set 4), the three solution forms named, an equation completed for a given count (board 8, set 5–6), a context with no solution (board 7)."],
        changes=["11.3.1 perimeter warm-up → four retrieval questions, the prerequisite (is 2 a solution?) in the last slot.",
                 "11.3.2 nine equations chosen and solved with a partner → Notes I's one-solution line and board 3, taught from the front.",
                 "11.3.3 exploration (a grid of tried values as evidence) → Notes I–II: each ending reached by simplifying.",
                 "11.3.4 classification grid → boards 1–6 and the Independent Set, each verdict with its ending."],
    ),
)
