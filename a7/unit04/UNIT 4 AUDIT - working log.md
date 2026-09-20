# Unit 4 audit — working log

Every value re-derived with sympy. This file is the denominator: it records what was checked,
not only what was wrong. Written as the audit proceeds so nothing is lost.

## What arrived (20 September 2026)

Five PDFs, staged at `/root/mn/unit04/` (outside the repository — Math Nation is copyrighted):

| File | Pages |
|---|---|
| 7a.04 Assessment Guide.pdf | 7 |
| 7a.04 Assessment.pdf | 6 |
| 7a.04 Compiled Homework.pdf | 16 |
| 7a.04 Compiled Practice Problems.pdf | 16 |
| 7a.04 Teacher Edition.pdf | 82 |

**Not in the package** (all five were present for Unit 3): a standalone Student Edition,
the Practice answer keys, the Homework answer keys, the Additional Practice sheets and their
keys, and the Stepping Stones refreshers. The Teacher Edition carries the in-lesson student
pages with answers as embedded images; the Practice and Homework documents as uploaded are
student copies with blank answer space.

Consequence for this audit: **the Practice and Homework ITEMS can be and are worked and judged;
their KEYS cannot be checked, because they were not supplied.** Unit 3's worst defects were key
errors (D1, D2, D3, D4, D5), so this is a real gap and it is stated in the audit's bottom line.

---

## Assessment (13 questions, 100 points) — verified, 0 discrepancies

24 values re-derived. The Assessment Guide's key agrees with every one.

| Q | Benchmark | Item | Key | Verified |
|---|---|---|---|---|
| 1a | 8.NSO.1.6 | 1.058×10⁵ + 3.38×10⁶ | 3.4858×10⁶ mg | ✓ 3,485,800 |
| 1b | 8.NSO.1.6 | 1.352×10⁷ − 1.058×10⁵ | 1.34142×10⁷ mg | ✓ 13,414,200 |
| 2 | 8.NSO.1.6 | 3.09×10⁻³ − 3.472×10⁻⁵, "using significant digits" | 3.06×10⁻³ ft³ | ✓ exact 0.00305528, to 5 decimal places 0.00306 |
| 3 | 8.NSO.1.5 | (−6×10⁻⁸)(1.9×10⁻⁶), select all | −1.14×10⁻¹³ and −.000000000000114 | ✓ both; the other six are not equal |
| 4 | 8.NSO.1.5 | (5.2×10¹⁷) − (9.8637×10¹⁹), select all | −9.8117×10¹⁹ and −98,117,000,000,000,000,000 | ✓ both |
| 5 | 8.NSO.1.5 | (4.7×10⁻⁴)/(−3.76×10⁻⁶) | −1.25×10² / −125 | ✓ |
| 6 | 8.NSO.1.5 | (5×10⁻⁵) + (8×10⁻⁶) | 5.8×10⁻⁵ / 0.000058 | ✓ |
| 7 | 8.NSO.1.5 | (2.65×10¹¹) ÷ (5×10¹³) | 5.3×10⁻³ / 0.0053 | ✓ |
| 8 | 8.NSO.1.5 | (2.9×10⁵)(6×10⁷) | 1.74×10¹³ / 17,400,000,000,000 | ✓ |
| 9 | 8.NSO.1.7 | √(4³ − 39) · 5⁻³ | 1/25 | ✓ |
| 10 | 8.NSO.1.7 | (2³ − 5)/6² − √(4/9 − 1/3) | −1/4 | ✓ |
| 11 | 8.NSO.1.7 | 4(8.63 − (3.2)²) + ∛125 | −1.44 | ✓ |
| 12 | 8.NSO.1.7 | 12((1/2)³ + 3⁻²) | 51/18 | ✓ — equals 17/6; the guide keys it unsimplified on purpose (it says to accept equivalent values) |
| 13 | 8.NSO.1.7 | 2⁻¹(62.4)(4)² | 499.2 lb/ft | ✓ |

**Point ledger:** 4 + 4 + 4 + (11 × 8) = **100**, and the guide claims 100. ✓

**Boundary checks on the assessment.** Every addition/subtraction item has its two exponents
within 2 (gaps of 1, 2, 2, 2, 1) ✓. Every 8.NSO.1.7 item stays inside the book's own stated
assessment limits (integer exponents between −3 and 3; radicand a perfect square or cube) ✓.

**The book's own assessment limits for MA.8.NSO.1.7**, stated on page 1 of the guide and worth
adopting for our items: expressions must be *given* and must incorporate a negative exponent
and/or a radical; the radicand must be a perfect square or perfect cube; integer exponents
between −3 and 3 inclusive. These are tighter than the B1G-M and are the FAST-realistic shape.

---

## Notes on the assessment that are not errors

- **Q10's radicand is 4/9 − 1/3 = 1/9**, a perfect square of a rational rather than of an
  integer. The benchmark's wording ("perfect squares up to 225") is about integers. The book
  does this in several places (Practice L5 #5 and #10 use ∛(1/125) and ∛(1/27)). It is
  defensible — numerator and denominator are each perfect within range — and it is good
  mathematics, but it is a place where our capcheck has to be told the rule deliberately rather
  than left to guess.
- **Q2 asks for significant digits on a subtraction.** The sig-digit rule for addition and
  subtraction is about decimal places, not significant digits, and the guide's own key (3.06×10⁻³)
  is the decimal-places answer. Whether the book *taught* that rule is a Lesson 4 question —
  checked below.
- The guide's key for Q12 is 51/18 rather than 17/6, deliberately, with a stated policy of
  accepting equivalent values and not requiring simplification.
