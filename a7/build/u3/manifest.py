# Unit 3 manifest — what install_unit.py needs to assemble the package and write 00 - START HERE.md.
M = dict(
    unit=3, title="Exponents and Scientific Notation",
    folder="A7 Unit 3 - Exponents and Scientific Notation",
    audit_src="a7/unit03/UNIT 3 AUDIT.md",           # repo-relative; copied into Reference/
    summary="ten teaching days (nine book lessons, merged to eight, plus the two Thread A days), a review, a two-period assessment",
    # (file code, label as printed, title, benchmark, the line that carries the day) — in teaching order
    lessons=[
        ("3.01", "3.01", "Product Laws of Exponents", "MA.7.NSO.1.1", "Same base, add — and the base has to match."),
        ("3.02", "3.02", "Quotient Laws of Exponents", "MA.7.NSO.1.1", "Same base, subtract — and exponent 0 is not 0."),
        ("3.03", "3.03", "Exponential Expressions", "MA.7.NSO.1.1", "Two plans, one value — the order is yours."),
        ("3.04", "3.04", "Negative Exponent Law", "MA.8.NSO.1.3", "Reciprocal, not opposite."),
        ("3.05", "3.05", "Applying Exponent Laws", "MA.8.NSO.1.3", "Flip the numbers, not the sign."),
        ("3.06", "3.06–07", "Evaluating and Equivalent Expressions", "MA.8.NSO.1.3", "Rewrite the base to compare."),
        ("3.T1", "T-A1", "Exponent Laws with Variable Bases", "MA.8.AR.1.1", "Everything inside the parentheses gets the exponent — the number included."),
        ("3.T2", "T-A2", "Negative Exponents with Variable Bases", "MA.8.AR.1.1", "Only the factor wearing the negative exponent moves."),
        ("3.08", "3.08", "Writing Large Numbers in Scientific Notation", "MA.8.NSO.1.4", "One nonzero digit in front of the decimal point."),
        ("3.09", "3.09", "Writing Small Numbers in Scientific Notation", "MA.8.NSO.1.4", "The exponent counts places, not zeros."),
    ],
    assessment=("all four benchmarks, sections by benchmark", 41),
    naming_note="The two Thread A days are `A7 3.T1` and `A7 3.T2` (they are MA.8.AR.1.1, woven into this unit under ruling 14, and carry no book lesson number).",
    order_note="Book order with Thread A woven in after 3.07 (ruling 14): the laws are complete on numbers before they are restated on letters, and both are complete before scientific notation. Math Nation's 3.6 and 3.7 are one period here (3.06–07). MA.7.NSO.1.1 is grade 7 content the Grade 8 FAST assumes; the other three benchmarks report under Number Sense and Operations (8.NSO.1.3, 8.NSO.1.4) and Algebraic Reasoning (8.AR.1.1).",
    before_unit=[
        "**Seven defects in the Math Nation package are not reproduced here.** Practice L1 #7 (key 104,796 → 104,976), Additional Practice L8 #2 (10⁶ + 10⁴ keyed 101000 → 1,010,000), Additional Practice L9 #3 (malformed item, wrong key), Homework L3 #7 (4,046 → 4,096), Homework L9 #4b (3 → 1,000), Homework L9 #4c (item unsound; keyed 3,000, true ratio ≈ 527), Homework L9 #5 (two matching rows equal). `Reference/UNIT 3 AUDIT - Math Nation package.md` has the page numbers.",
        "**Three things the state guide expects that the book never asks are in every relevant bank and on the assessment:** unknown-exponent items (7ⁿ ÷ 7² = 343), the −b versus b⁻¹ contrast in writing, and calculator E notation with comparisons that cross from very large to very small.",
        "**The assessment is one paper over two periods, 41 points** (ruling 27). Students stop when the first period ends and continue from where they stopped — it is not two papers, and nothing on it says 'Day 1'. Four sections by benchmark, numbered 1–21 straight through. **Questions 10 and 21 are transfer items** (ruling 18): the same benchmarks, on surfaces that appear on no review and in no question bank. The key names them and the Score Tracker maps every question to its benchmark.",
        "**The Reference Sheet is the only handout.** Give it out at 3.04 or earlier; it is the document students study from. It does not go into the test.",
    ],
)
