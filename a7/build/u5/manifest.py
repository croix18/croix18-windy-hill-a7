# Unit 5 manifest — what install_unit.py needs to assemble the package and write 00 - START HERE.md.
M = dict(
    unit=5,                                           # the title is course.py UNITS[5]
    summary="six teaching days (eleven book lessons, merged to six), a review sent home Tue 3 Nov, the test as one period on Thu 5 Nov (a random draw of the practice test; Forms A and B as built)",
    # (file code, label as printed, title, benchmark, the line that carries the day) — in teaching order
    lessons=[
        ("5.01", "5.01", "Scale Drawings", "MA.7.GR.1.5", "A scale factor is the one number every length is multiplied by. Copy divided by original."),
        ("5.02", "5.02–03", "Scale Factor: Perimeter and Area", "MA.7.GR.1.5", "Perimeter scales by k. Area scales by k squared."),
        ("5.04", "5.04", "Real-World Scale Drawings", "MA.7.GR.1.5", "A scale with two units is a rate: read it per 1 first."),
        ("5.06", "5.06–07", "Converting Length Across Systems; Currency", "MA.7.AR.3.3", "Multiply by a form of 1 so the unit you have cancels. Estimate first."),
        ("5.08", "5.08–09", "Converting Mass, Area and Volume", "MA.7.AR.3.3", "Area converts by the square of the length ratio."),
        ("5.10", "5.10–11", "Multi-Step Proportion Problems", "MA.7.AR.4.5 · MA.7.AR.3.3", "A unit rate, used twice. Same units before you compare."),
    ],
    assessment=("all three benchmarks, sections by benchmark; Form A, Form B and a practice test, 19 questions, two transfer items (8 and 19)", 24),
    order_note="Book order, with 5.2 + 5.3, 5.6 + 5.7, 5.8 + 5.9 and 5.10 + 5.11 merged under ruling 30 — all four merges are the plan's own; Math Nation 5.5 (Mathlandia, an invented currency) is not on the plan and its idea lives in 5.06–07. Three days of MA.7.GR.1.5, two of MA.7.AR.3.3, one of MA.7.AR.4.5 with AR.3.3 inside it. No review day (ruling 27a): the review paper goes home Tue 3 Nov, the test is Thu–Fri 5–6 Nov.",
    handouts={},
    before_unit=[
        "**Built in the order the rulebook asks (§16):** from the benchmarks first, then read against Math Nation 5.1–5.11 and its test — the audit is in Reference.",
        "**Every conversion ratio is the FAST reference sheet's** (1 in = 2.54 cm, 1 mi = 1.61 km, 1 lb = 0.454 kg, 1 kg = 2.204 lb, 1 gal = 3.785 L, 1 c = 0.24 L …) and is printed on the board or paper that uses it. Math Nation's lessons drift from the sheet (1.609, 2.2); its own assessment does not.",
    ],
)
