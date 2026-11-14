# Unit 11 manifest — what install_unit.py needs to assemble the package and write 00 - START HERE.md.
M = dict(
    unit=11,                                          # the title is course.py UNITS[11]
    summary="seven teaching days (eight book lessons; 11.5 and 11.6 merged), a review sent home Thu 10 Dec, the test as one period on Fri 11 Dec (a random set of the practice page)",
    # (file code, label as printed, title, benchmark, the line that carries the day) — in teaching order
    lessons=[
        ("11.01", "11.01", "Equations with Like Terms and the Distributive Property", "MA.8.AR.2.1", "Collect the like terms first. The number outside the parentheses multiplies every term inside — and a minus in front goes in with it."),
        ("11.02", "11.02", "Equations with Variables on Both Sides", "MA.8.AR.2.1", "Take the same variable term from both sides; check in both sides of the first equation."),
        ("11.03", "11.03", "One Solution, No Solution, Infinitely Many Solutions", "MA.8.AR.2.1", "x = a: one solution. A true sentence like 5 = 5: infinitely many. A false one like 5 = 9: none. x = 0 is one solution."),
        ("11.04", "11.04", "Multi-Step Equations", "MA.8.AR.2.1", "A fraction or a decimal outside the parentheses multiplies every term inside; to clear fractions, multiply every term by a common denominator."),
        ("11.05", "11.05–06", "Systems: Which Points Are Solutions; How Many Solutions", "MA.8.AR.4.1", "A solution of a system makes both equations true. Cross once: one; parallel: none; the same line: infinitely many."),
        ("11.07", "11.07", "Solving Systems by Graphing", "MA.8.AR.4.3", "Graph each line from a table; the solution is where they cross, checked in both equations."),
        ("11.08", "11.08", "Systems in Context; Approximate Solutions", "MA.8.AR.4.3", "Say the crossing in the story's words, with units. Between the grid lines, estimate with 'about' and check it in both."),
    ],
    assessment=("all four benchmarks, sections by benchmark in the order AR.2.1 · AR.4.1 · AR.4.2 · AR.4.3; the practice test alone (ruling 49), 14 questions, one period (ruling 51)", 18),
    naming_note="The merged day 11.05–06 carries the files of `A7 11.05` (book lessons 11.5 and 11.6, MA.8.AR.4.1 with MA.8.AR.4.2 taught the same day); there is no `A7 11.06`.",
    order_note="Book order, with 11.5 + 11.6 merged (11.6 is 11.5's practice, and AR.4.2 is read off the same graphs). Four days of MA.8.AR.2.1, one of MA.8.AR.4.1 with AR.4.2, two of MA.8.AR.4.3. Unit 11 is taught before Units 7 and 10 under ruling 52 — its equations are the district's Q2 essential benchmark — so lines are graphed from a table of values and slope is not named until Unit 10. No class Thu 3 Dec or Tue 8 Dec; 11.03 and 11.07 are 43-minute Wednesdays. No review day (ruling 27a): the review paper goes home Thu 10 Dec with 11.08's independent set, and the test is Fri 11 Dec.",
    handouts={},
    before_unit=[
        "**Built in the order the rulebook asks (§16):** from the benchmarks first, then read against Math Nation 11.1–11.8 and its test — the audit is in Reference. None of the book's 29 defects is reproduced; its test is not the blueprint (no multiple choice, no select-all, an approximate item keyed exact — E15).",
        "**A line is graphed from a table of values** (x = 0 and two more; the third point is the check), and every system is given solved for y. \"Slope\" and \"y-intercept\" are on no student page: parallel lines are \"the same number multiplying x\". The Teacher Editions may say slope.",
        "**No substitution and no elimination** (Algebra 1). The one bridge — at the crossing both equations give the same y, so its x solves mx + b = nx + c — is shown in 11.07 and not tested.",
        "**Three endings, named every day from 11.03:** x = a (one solution), a = a (always true: infinitely many), a = b (never true: no solution), written as the false equation and then the words. x = 0 is one solution.",
        "**Rational coefficients carry 11.04**, and a decimal distributed — the lowest-scoring released Grade 8 skill — has a question every day and its own on the test (question 4).",
        "**Every solution is checked by substitution**, in both sides of an equation and in both equations of a system. An approximate crossing is read to the nearest tenth with \"about\"; its key gives the exact value and the range it accepts.",
        "**Variables rotate** (x and y for systems; n, h, m, v, w elsewhere). Multiplication is written with parentheses or a dot, never ×.",
    ],
)
