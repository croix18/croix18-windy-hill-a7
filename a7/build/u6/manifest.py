# Unit 6 manifest — what install_unit.py needs to assemble the package and write 00 - START HERE.md.
M = dict(
    unit=6,                                           # the title is course.py UNITS[6]
    summary="six teaching days (eight book lessons, merged to six) and the two Thread B days after the test, a review sent home Mon 16 Nov, the test as one period on Tue 17 Nov (a random set of the practice page)",
    # (file code, label as printed, title, benchmark, the line that carries the day) — in teaching order
    lessons=[
        ("6.01", "6.01–02", "Triangle Inequality Theorem; Converse of the Pythagorean Theorem", "MA.8.GR.1.3", "The two shorter sides add to MORE than the longest. Right exactly when their squares add to the longest side's square."),
        ("6.03", "6.03", "Pythagorean Theorem", "MA.8.GR.1.1", "a² + b² = c², and c is across from the right angle. A leg: subtract."),
        ("6.04", "6.04", "Pythagorean Theorem in Real-World Problems", "MA.8.GR.1.1", "Find the right angle first; the side across from it is c."),
        ("6.05", "6.05", "Distance on the Coordinate Plane", "MA.8.GR.1.2", "A slanted distance is a hypotenuse, and the legs come from the coordinates."),
        ("6.06", "6.06", "Real-World Coordinate-Plane Problems; Perimeter", "MA.8.GR.1.2", "A perimeter adds every side; a slanted side is found by its own triangle."),
        ("6.07", "6.07–08", "Similar Triangles; Indirect Measurement", "MA.8.GR.2.4", "Similar: one scale factor on every side. Same sun, same angle."),
        ("6.T1", "T-B1", "Angle Pairs: Supplementary, Complementary, Vertical, Adjacent", "MA.8.GR.1.4", "Complementary makes 90, supplementary 180; vertical angles are equal."),
        ("6.T2", "T-B2", "Interior and Exterior Angles of a Triangle", "MA.8.GR.1.5", "The three angles make 180. An exterior angle equals the two remote interior angles."),
    ],
    assessment=("all four benchmarks, sections by benchmark in the order GR.1.3 · GR.1.1 · GR.1.2 · GR.2.4; the practice test alone (ruling 49), 14 questions, one period (ruling 51)", 18),
    naming_note="The two Thread B days are `A7 6.T1` and `A7 6.T2` (MA.8.GR.1.4 and 1.5 — Math Nation 16.1 and 16.2, taught after the Unit 6 test so the angle facts are in play for the rest of the year) and carry no book lesson number.",
    order_note="Book order, with 6.1 + 6.2 and 6.7 + 6.8 merged — both merges are the plan's own (6.2 is 6.1's practice, 6.8 is 6.7's). One day of MA.8.GR.1.3, two of MA.8.GR.1.1, two of MA.8.GR.1.2, one of MA.8.GR.2.4. No review day (ruling 27a): the review paper goes home Mon 16 Nov with 6.07's independent set, the test is Tue 17 Nov. Thread B (T-B1 Wed 18 Nov, 43 minutes; T-B2 Thu 19 Nov) is not on the Unit 6 test.",
    handouts={},
    before_unit=[
        "**Built in the order the rulebook asks (§16):** from the benchmarks first, then read against Math Nation 6.1–6.8, its test and 16.1–16.2 — the audit is in Reference.",
        "**Every square root has a whole radicand up to 225** (GR.1.1 and GR.1.2, Clarification 3), and none has a square factor, so √n is already in simplest form; an irrational answer is also given to the nearest tenth wherever the question asks for a measurement. Math Nation's own test breaks the 225 bound on four of its five Pythagorean items.",
        "**No distance formula** (GR.1.2, Clarification 2): a slanted distance is always the right triangle drawn on the grid, its legs read from the coordinates.",
    ],
)
