# Unit 7 manifest — what install_unit.py needs to assemble the package and write 00 - START HERE.md.
M = dict(
    unit=7,                                           # the title is course.py UNITS[7]
    summary="five teaching days (seven book lessons; 7.2 with 7.3 and 7.5 with 7.6 each one day), a review sent home Tue 12 Jan, a spiral day Wed 13 Jan, the test as one period on Thu 14 Jan (a random set of the practice page)",
    # (file code, label as printed, title, benchmark, the line that carries the day) — in teaching order
    lessons=[
        ("7.01", "7.01", "Graphing Proportional Relationships", "MA.7.AR.4.3", "One quantity is always a constant multiple of the other: y = px. Its graph is a straight line through the origin; read the scales first, and choose x-values that give whole-number y-values. Question 1 of the set is drawn in class; a 43-minute first day back, board 3 the first cut, then board 5."),
        ("7.02", "7.02–03", "Constant of Proportionality: Table, Graph, Description", "MA.7.AR.4.2", "The constant of proportionality is the amount of y for every 1 unit of x: y ÷ x from a table, a grid-corner point from a graph, the rate from a description — with its unit, in the direction the question names. A constant can be negative."),
        ("7.04", "7.04", "Is It Proportional?", "MA.7.AR.4.1", "y ÷ x is the same for every pair; a straight line through the origin; nothing added at the start. A linear relationship is also proportional only when its line passes through the origin (MA.8.AR.3.1)."),
        ("7.05", "7.05–06", "Writing Equations; Translating Representations", "MA.7.AR.4.4", "Write y = px from a table, a graph or a description, and translate from one representation to another. Either quantity can be y: m = 60h and h = (1/60)m (\"some books write k\" is said here once)."),
        ("7.07", "7.07", "Comparing Proportional Relationships", "MA.7.AR.4.5", "Find each constant in the same units, compare them, then answer the question asked. On the same axes, the greater constant gives the steeper line; past the edge of a grid, use the constant."),
    ],
    assessment=("all six benchmarks, sections by benchmark in the order AR.4.3 · AR.4.2 · AR.4.1 · MA.8.AR.3.1 · AR.4.4 · AR.4.5; the practice test alone (ruling 49), 15 questions, one period (ruling 51)", 20),
    naming_note="The merged day 7.02–03 carries the files of `A7 7.02` (book lessons 7.2 and 7.3) and 7.05–06 those of `A7 7.05` (book lessons 7.5 and 7.6); there is no `A7 7.03` and no `A7 7.06`.",
    order_note="Book order, with 7.2 + 7.3 merged (the constant from a table, a graph and a description is one idea) and 7.5 + 7.6 merged (writing y = px and translating between forms). Five decks Wed 6 Jan – Tue 12 Jan 2027: 7.01 is the 43-minute first day back after the break. No review day (ruling 27a): the review paper goes home Tue 12 Jan with 7.07; Wed 13 Jan is a spiral day with no deck; the test is Thu 14 Jan, one period. Unit 7 is taught after Unit 11 (ruling 52) and before Unit 10.",
    handouts={},
    before_unit=[
        "**Built in the order the rulebook asks (§16):** the test was settled first, from the benchmarks (MA.7.AR.4.1–4.5 and MA.8.AR.3.1), then the lessons were built to it. Math Nation's Unit 7 was read for scope and its test's item shapes only; nothing is taken from it. The plan was read by a Barton reader and a FAST reader before any spec was written.",
        "**One definition, said the same way every day:** two quantities are in a proportional relationship when one quantity is always a constant multiple of the other, y = px. p is the constant of proportionality (named in 7.02–03; on 7.01 it is the unit rate). Florida writes p; \"some books write k\" is said once, in 7.05–06.",
        "**Three tests, in these words:** table — y ÷ x is the same for every pair; graph — a straight line through the origin; description — a steady rate with nothing added at the start. From 7.04, the equation: y = px with nothing added. No cross products (the state: they \"may lead to errors\").",
        "**\"Slope\" and \"y-intercept\" are on no page.** Unit 11 graphed lines from a table and named the coefficient of x; Unit 10 names slope on 19 Jan. A steeper line is \"more y for every 1 unit of x\"; a line that misses the origin has \"a number added\".",
        "**Which quantity is y is said in every item,** and a constant carries its unit as y-unit per x-unit. Either quantity may be y (m = 60h, h = (1/60)m): taught in 7.05–06 and asked once on the test (question 12b), with the direction named.",
        "**Graphs have readable points and an axis scale is not always 1:** \"read the scales first\" from 7.01, a graph scaled by 2, 4, 5, 10 or 20 in every lesson, and the test's question 2 turns on a d-axis scaled by 0.5. Where a choice question shows several graphs, they share one set of axes and scales. A context is drawn in Quadrant I; one negative constant is taught (7.02–03) and tested (question 6).",
        "**Whiteboards read; the Independent Set draws.** 7.01's handout prints empty grids, and its question 1 is drawn in class with the teacher circulating. The test has one draw-the-graph question (1b), whose key prints the graph.",
        "**MA.8.AR.3.1 lives in 7.04 and in one test question (9):** a linear relationship is also proportional only when its line passes through the origin — Unit 11's y = 2x + 3 versus y = 2x. Calculators are allowed and never mentioned.",
        "**Hand-off to Unit 10 (from 15 Jan) — write it into that unit's plan:** it names the constant of proportionality as the slope of y = px, and reopens 7.04's pair (y = 2x and y = 2x + 3) for MA.8.AR.3.1 with that word.",
        "**Hand-off to circles (MA.7.GR.1.3), when taught:** π is the constant of proportionality between a circle's circumference and its diameter.",
        "**Hand-off to the practice page (not built in this pass):** question 1(b) needs a part where the student plots points.",
    ],
)
