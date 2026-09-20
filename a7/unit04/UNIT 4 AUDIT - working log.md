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

---

## Practice Problems and Homework — every item worked

Two compiled documents, 8 lessons each, 10 items per lesson (L7/L8 have sub-parts).
**Every value re-derived.** The items below are the ones that do not survive; everything not
listed was worked and is sound.

### Values verified and sound (a sample of the denominator)

Practice L2 matching (all five products against the five-item answer bank: 3.212×10⁹, 1.8×10⁻¹⁵,
4.539×10⁷, 5.76×10⁻⁵, 3.6×10¹⁵ — one each, no collisions) ✓. Practice L3 #7–10 (1.8×10⁸,
7.2×10⁻⁶, 7.8×10⁴, 1.4×10⁻⁶) ✓. Practice L5 #1–10 (0.11, 15, 5, 7, 0.1, −14/9, −9, 19, 0.85,
13/3) ✓. Practice L6 #6–10 (48, 7/4, 2, −24, −239/16) ✓. Practice L7 #1–10 (BMI 26.3, cone
106.31 cm², TV 35.03 in, 3,928.5 J, 101,120 in³, 11/8, 53.25, 900, 2, 31/20) ✓. Homework L5
#1–10 (0.2625, 37, 12, 8, 1/6, −3, −22.5, 9, 0.7, 9.5) ✓. Homework L6 #6–10 (1, 13/4, 125/4,
−53, −89/9) ✓. Homework L7 #1–10 (BMI 25.1, cone 147.96 cm², TV 34.48 in, 2,205 J, 72,625 in³,
4/3, 65.75, 256, 22/25, 7/16) ✓. Homework L8 (generator $498.34 and $2,800; Janet $20,300;
Dominic $664.08) ✓. Practice L8 (generator $1,041.40 and $2,761.25; Janet $28,450; Dominic
$959.34) ✓.

### Defects — student-facing

| # | Where | What it says | What is true |
|---|---|---|---|
| **D1** | Practice L1, table + Q1 | Table holds 4,500,000,000 · 45×10⁶ · 45×10⁷ · 45×10⁵ and asks "which numbers are represented by the same standard scientific form?" | The four forms are 4.5×10⁹, 4.5×10⁷, 4.5×10⁸, 4.5×10⁶ — **all different. The question has no answer.** The parallel Homework item works (38,000,000,000 and 38×10⁹ are both 3.8×10¹⁰), so a row was mistyped: 45×10⁸ was meant. |
| **D2** | Homework L1 Q4 | Stem: "Cell D has a diameter of 4.2 × 10⁻⁴." Scaffold line 2: "(__ × 10⁻⁴) − (**6.8** × 10⁻⁴)" | The 6.8 is left over from Practice L1 Q6. A student who follows the scaffold solves a different problem. True answer 9.97×10⁻³ − 4.2×10⁻⁴ = **9.55×10⁻³**; the scaffold gives 9.29×10⁻³. |
| **D3** | Homework L2 Q1 | Tyree's "correct" standard-notation column: 2,800 × 9,700 → 27.16 × 1,000,000 → **2,716,000** | 27.16 × 1,000,000 = **27,160,000**. The column the student is told to check against is wrong by a factor of 10, and it is the column that is supposed to expose Tyree's error. |
| **D4** | Homework L3 Q4 | Stem: "160,000,000,000 meters" and "3.5 × 10² meters per second". Both students' work starts from **(1.6 × 10¹²)** and **(3.5 × 10³)** | 160,000,000,000 = 1.6 × 10**¹¹**, and the stem's speed is 3.5 × 10**²**. Neither worked column matches the problem it claims to solve. True answer from the stem: 4.571×10⁸ s. |
| **D5** | Homework L4 Q3 | "the amount of profit of companies who manufactured **three** popular gaming systems"; the table lists **two** rows, Apple iPhones and Samsung Phones; part (a) reads "all two companies" | Two rows, neither a gaming system. Separately the figures are not of this world: Samsung at 2.37×10¹⁴ dollars is $237 trillion, more than global GDP. |
| **D6** | Practice L4 Q3 | "If the people living in San Francisco were to pay off **the national debt**, how much would each person pay?" | The national debt is never given. Q2 gave the **student loan** debt ($1.58 trillion). Using that: 1.58×10¹² ÷ 8.73×10⁶ ≈ $180,985. |
| **D7** | Practice + Homework L8, Dominic | Table puts **Underlay** under *Bathroom*; the expression puts its price inside the **bedroom's** area group. **Grout** is priced per square foot in the table but added as a flat amount in the expression | Both readings cannot be right. Q6, Q9 and Q10 ("carpeting the bedroom", "bedroom only", "bathroom only") have no unambiguous answer. The same defect appears in both documents with different numbers. |
| **D8** | Homework L2 Q6 | One answer in the matching column is typeset "**2.× 10⁸**" | Dangling decimal point; should be 2.0 × 10⁸. |

### Outside the benchmark boundary (capcheck, §5 of the pre-audit)

MA.8.NSO.1.5 and 1.6 limit addition and subtraction to exponents **within 2 of each other.**

| Where | Item | Gap |
|---|---|---|
| **Homework L1 Q2** | (8.7 × 10⁶) + (4.8 × 10³) | **3** |
| **Homework L4 Q3a** | 1.898 × 10¹¹ + 2.37 × 10¹⁴ | **3** |
| **Homework L4 Q3c** | 2.37 × 10¹⁴ − 1.898 × 10¹¹ | **3** |

Every other addition or subtraction in both documents and on the assessment is within 2. All
radicands in Lessons 5–8 are perfect squares up to 225 or perfect cubes within −125 to 125 (or
the rational versions 1/8, 1/27, 1/125), so Clarification 2 is respected throughout.

### Weak items — not wrong, but not reusable as written

- **Practice L1 Q6** asks for "the difference in diameters of Cell A and Cell B" and sets up
  A − B, which is negative (−6.398 × 10⁻⁵). A difference of two sizes should be posed so the
  answer is positive, or the question should name the order.
- **Practice L1 Q3 and Q5** are the same question asked twice (Jacksonville minus Gainesville),
  with Q4 converting to scientific notation in between.
- **Practice L4 Q5–7** give "the approximate distance between Neptune and the sun is 4.5 × 10⁹"
  with **no unit**. (Kilometres, from the figures.) A measurement without a unit is not a
  measurement, and this is the significant-digits lesson.
- **Practice L4 Q10** has the "average mass of 105 cows" at 4.305 × 10⁴ and 6.25 × 10⁵ — a cow is
  about 6 × 10² kg, and an average does not depend on the herd size.
- **Homework L1 Q3c** asks "how many times larger is the population of Florida than Alabama?
  Write your answer using scientific notation" — the answer is ≈ 4.27, which is already
  4.27 × 10⁰. Asking for scientific notation on a single-digit ratio teaches nothing.
- **Homework L4 Q3b** likewise: 2.37×10¹⁴ ÷ 1.898×10¹¹ = 1,248.68…, an ugly ratio in a context
  whose numbers are fictional anyway.
- **The Marcus / Sara error-analysis pair** (Practice L3 Q6, Homework L3 Q4) is well designed
  underneath: Marcus **subtracts** the coefficients instead of dividing (1.5 − 3.4 = −1.9;
  1.6 − 3.5 = −1.9, which is where the −1.9 in both versions comes from) and Sara gets the
  **exponent operation** wrong (adds in the Practice version, multiplies in the Homework one)
  and leaves a coefficient below 1. Both are nameable errors and worth keeping. Sara also carries
  an unexplained negative sign in both versions, which no named error accounts for.
- **The context of both versions** asks how long sound takes to travel from Earth to the Sun.
  Sound does not travel through a vacuum. The arithmetic is fine; the physics is not, and this is
  the kind of thing a student notices out loud.

---

## Teacher Edition — Lessons 1 to 4

The TE reproduces each in-lesson student page with its answers printed in red. 70 values
re-derived across Lessons 1–4.

**Sound throughout:** 4.1.2 Exploration (Neptune + Saturn = 1.67×10⁵ km, wider than Jupiter's
1.43×10⁵ ✓); 4.1.3 Guided Instruction (the four-row equivalence table, 2.185×10⁶, 1.125×10⁶,
7.17×10⁻³, 1.252×10⁻²); 4.1.4 Q1–Q2; 4.1.5 Try It all five; every value in Lesson 2 including
**all eighteen "Give Me Five!" game cards**; every value in Lesson 3 (toilet paper, the five
conjecture tables, Gizmo Gadgets, the four quotients); 4.4.1 Warm-Up's four rows; 4.4.2's
significant-digit table and the Apollo/smartphone arithmetic; 4.4.4 parts a, c, d and Q2.

### Defects — Teacher Edition

| # | Where | What it says | What is true |
|---|---|---|---|
| **D9** | 4.4.3 Guided Instruction Q1b | National debt $26.9 trillion ÷ North Bay's 197,974 people → key **1.36 × 10⁹** | 2.69×10¹³ ÷ 1.97974×10⁵ = **1.3588 × 10⁸**. The key's exponent is one too high — this is the worked answer the teacher reads out. |
| **D10** | 4.4.4 Your Turn Q1b | "4(1.2 × 10⁷) + 3.0 × 10⁸ **−** 3.48 × 10⁹ ≈ 3 × 10⁸" | 4.8×10⁷ + 3.0×10⁸ = **3.48 × 10⁸**. Exponent one too high, **and** the key prints a minus sign where the equals sign belongs, so the line as printed is not even an equation. |
| **D11** | 4.3.3 Guided Instruction Q2 | "The speed of light is (3 × 10⁹) meters per second." | The speed of light is **3 × 10⁸ m/s**. Worse, with the true value the answer is 500 s — which is exactly **Mara's answer, the one the book circles as the error**. A student who knows that light takes about eight minutes to reach Earth is told the right number is wrong. |
| **D12** | 4.4.2 Guided Instruction Q3 | Smartphone processing speed **2.7 MHz** | A modern smartphone runs at about 2.7 **GHz**. As printed, a 2020 phone is 2.6 times faster than a 1966 guidance computer, which is the opposite of the point the item is making. (Using GHz would put the subtraction's exponents 3 apart, outside the benchmark — which may be why it was changed, but a false fact is not the fix.) |
| **D13** | 4.4.2 Guided Instruction, the sig-digit rule | "If two numbers are written with different precision, then the precision is the least **number of significant digits**." The book then applies this to **subtraction** (Q1d, and the assessment's Q2) | That is the rule for **products and quotients**. For sums and differences precision is governed by **decimal places**. The two rules agree on every example the book uses, so nothing in the book is wrong *numerically* — but the rule as stated is wrong, and a student who applies it to 1.234×10³ + 5.6 gets 1.2×10³ where 1.240×10³ is right. |

### Outside the boundary — Teacher Edition

- **4.1.4 Guided Practice Q3**: 2.37 × 10³² + 14.29 × 10³⁴. Written properly that is 2.37×10³² +
  1.429×10³⁵, an **exponent gap of 3**. The margin note on the facing page quotes Clarification 1
  ("within two of each other") and says the lesson has built understanding to within one — so the
  book knows the rule and breaks it two questions later.

### Conflicts with our settled rules (not errors)

- **Partner work is everywhere**: 4.1.2 Exploration, 4.3.2 Exploration (which also has students
  collect initials from two other pairs), 4.2.4 "Give Me Five!" (a two-player game with cards and
  a gameboard), 4.4.2 partner discussions, 4.6.3 Collaboration, 4.7.2 Collaboration, and the whole
  of 4.8 (three stations). All taught from the front or rewritten as written work.
- **"Students should not be allowed to use a calculator"** (4.2.1 Warm-Up) and **"The questions on
  the unit assessment are no calculator"** (Assessment Guide p. 2). Croix's ruling is the
  opposite and nothing about calculators is printed on any of our pages.
- The TE tells teachers students "will not have a calculator on the **FSA**" (4.5.4 margin). The
  test is the **FAST**, and Florida provides an on-screen scientific calculator at grades 7–8.
