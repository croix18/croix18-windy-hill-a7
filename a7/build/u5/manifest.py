# Unit 5 manifest — what install_unit.py needs to assemble the package and write 00 - START HERE.md.
M = dict(
    unit=5,                                           # the title is course.py UNITS[5]
    summary="six teaching days (eleven book lessons, merged to six), a review sent home as practice, a two-period assessment",
    # (file code, label as printed, title, benchmark, the line that carries the day) — in teaching order
    lessons=[
        ("5.01", "5.01", "Scale Drawings", "MA.7.GR.1.5", "A scale factor is the one number every length is multiplied by. Copy divided by original."),
        ("5.02", "5.02–03", "Scale Factor: Perimeter and Area", "MA.7.GR.1.5", "Perimeter scales by k. Area scales by k squared."),
        ("5.04", "5.04", "Real-World Scale Drawings", "MA.7.GR.1.5", "A scale with two units is a rate: read it per 1 first."),
        ("5.06", "5.06–07", "Converting Length Across Systems; Currency", "MA.7.AR.3.3", "Multiply by a form of 1 so the unit you have cancels. Estimate first."),
        ("5.08", "5.08–09", "Converting Mass, Area and Volume Across Systems", "MA.7.AR.3.3", "Area converts by the square of the length ratio."),
        ("5.10", "5.10–11", "Multi-Step Proportion Problems", "MA.7.AR.4.5 · MA.7.AR.3.3", "A unit rate, used twice. Same units before you compare."),
    ],
    assessment=("all three benchmarks, sections by benchmark", 24),
    handouts={},
    before_unit=[
        "**Built in the order the rulebook asks (§16):** from the benchmarks first, then read against Math Nation 5.1–5.11 and its test — the audit is in Reference.",
        "**Every conversion ratio is the FAST reference sheet's** (1 in = 2.54 cm, 1 mi = 1.61 km, 1 lb = 0.454 kg, 1 kg = 2.204 lb, 1 gal = 3.785 L, 1 c = 0.24 L …) and is printed on the board or paper that uses it. Math Nation's lessons drift from the sheet (1.609, 2.2); its own assessment does not.",
    ],
)
