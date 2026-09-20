# UNIT 4 PRE-AUDIT — the standards side

**Written 20 September 2026, before the Math Nation package arrived.** Everything here is
derived from documents already in this repository — the benchmark texts, the B1G-M reading
notes, the scope and sequence, the IXL plan. Nothing here describes Math Nation's Unit 4,
because I have not seen it. When the package lands this becomes sections 5, 6 and 7 of
`UNIT 4 AUDIT.md`; sections 1–4, 8 and 9 (bottom line, defects, teacher-facing slips, conflicts
with the settled rules, judgment calls, inventory) can only be written from the book.

Every numerical value below was re-derived with sympy in this session — **26 values from the
B1G-M, 0 discrepancies.** They are the guide's own worked examples and items, so they are the
seed for our banks and they had to be checked before they could be trusted.

---

## What the unit is

Math Nation calls it **Unit 4, Solving Problems with Rational Numbers**. Three benchmarks, eight
book lessons, six teaching days under the scope and sequence, then a two-period exam and a flex
day.

| Day | Book | Title (book's) | Benchmark | IXL |
|---|---|---|---|---|
| 4.01 | 4.1 | Adding and Subtracting Numbers Expressed in Scientific Notation | MA.8.NSO.1.5 | Add and subtract numbers written in scientific notation — HUR |
| 4.02+03 | 4.2, 4.3 | Multiplying / Dividing Numbers Expressed in Scientific Notation | MA.8.NSO.1.5 | Multiply … — YZU; Divide … — SGT |
| 4.04 | 4.4 | Solving Real-World Problems Involving Numbers Expressed in Scientific Notation | MA.8.NSO.1.6 | Add, subtract, multiply, and divide … word problems — D5S |
| 4.05 | 4.5 | Evaluating Expressions with Radicals | MA.8.NSO.1.7 | Evaluate radical expressions — D8J |
| 4.06 | 4.6 | Evaluating Expressions Using the Order of Operations | MA.8.NSO.1.7 | Evaluate radical expressions — D8J |
| 4.07+08 | 4.7, 4.8 | Evaluating Real-World Problems Using the Order of Operations, Parts 1–2 | MA.8.NSO.1.7 | Evaluate variable expressions: word problems — DPG |
| 4.X1, 4.X2 | — | Unit 4 exam, two periods | all three | — |
| flex | — | Reteach from exam evidence, or absorb a lost day | — | — |

Two merges (4.2+4.3 and 4.7+4.8) are already in the scope and sequence under ruling 14. Note
that 4.05 and 4.06 are **not** merged, and that IXL gives both days the same skill (D8J) — the
due-date sheet will therefore repeat it; that is the plan's doing, not an error.

**What this unit rests on.** Scientific notation itself was built in 3.08–3.09 (MA.8.NSO.1.4) —
the coefficient rule, reading notation back, and "how many times larger". Square roots and cube
roots were built in Unit 2 (2.01–2.06): the principal square root, that a radical names one
number, and the perfect-square and perfect-cube lists. Unit 4 is where those two strands are
operated on. The warm-up retrieval bands write themselves: *last unit* is exponents and
scientific notation, *last week* is whichever Unit 4 lesson preceded, *prior grade / earlier
unit* is the Unit 2 root lists, which 4.05 needs cold.

---

## 5. Capcheck — the boundaries this unit must not cross

These are the benchmark boundaries from `Florida BEST Grade 8 - Source of Truth.md`, checked
against the B1G-M clarifications. **Every one of them is a place a textbook routinely overshoots,
so each is a thing to look for in the book and a thing to enforce in our own items.**

1. **Addition and subtraction: the two exponents must be within 2 of each other.** (MA.8.NSO.1.5
   boundary; MA.8.NSO.1.6 carries the same limit.) `2.31×10¹⁵ + 9.1×10¹³` is legal — a gap of 2.
   `1.3×10³ + 3.4×10⁵` is a gap of 2 and legal. A gap of 3 or more is out of bounds for us even
   if the book prints one. **Multiplication and division carry no such limit.**
2. **Order of operations: six steps or fewer.** (MA.8.NSO.1.7 boundary.) Count the operations,
   not the characters.
3. **Radicals are limited to what can be simplified by factoring: square roots of perfect
   squares up to 225, cube roots of perfect cubes from −125 to 125.** (MA.8.NSO.1.7 boundary.)
   So √196 yes, √250 no; ∛(−125) yes, ∛216 no — even though 216 is a perfect cube, it is outside
   the stated range, and Unit 2's reference sheet already marks 216/343/512 as stretch-only.
   A radicand that is *not* a perfect square or cube (√52) belongs to MA.8.NSO.1.1 estimation,
   which is Unit 2's benchmark, not this one; inside an order-of-operations expression the
   radical should come out exact.
4. **Scientific-notation answers keep a coefficient in [1, 10).** Carried forward from Unit 3.
   The guide names `12×10⁹ instead of 1.2×10¹⁰` as a misconception, so `12×10⁹` may appear as a
   distractor or inside an item that is *about* the rule — those items get `not_sci=True` — but
   it may never be a keyed final answer.
5. **No fractional exponents.** Unchanged from Unit 3; rational exponents are MA.912.NSO.1.2.
6. **Significant digits are in scope for MA.8.NSO.1.6 only**, and only "when physical
   measurements are involved" (Clarification 1). A count is not a measurement. Do not impose
   sig-digit rounding on 1.5's pure-number arithmetic.

**Toolchain consequence.** `lessonbuild.capcheck_lesson` currently enforces only items 4 and 5 —
its docstring says "Ruling 13 caps for **this unit**", meaning Unit 3. Items 1 and 3 are
machine-checkable and I intend to add them before building 4.01: a scan that flags any
`a×10^m ± b×10^n` with |m − n| > 2, and any `\sqrt{…}` or `\sqrt[3]{…}` whose radicand is
outside the allowed lists. Item 2 (step count) is a judgment call and will be stated per item in
the Teacher Edition instead of automated. This is a change to the shared build library, so it
gets its own commit with its own reason, per the procedure.

---

## 6. What the state guide requires — every value re-derived

The B1G-M's tasks, worked examples and items for these three benchmarks. **All 26 values below
were re-derived with sympy in this session and agree with the guide.** They are candidate seed
items for our banks; whether Math Nation also has them is what the book-side audit will say.

### MA.8.NSO.1.5 — add, subtract, multiply, divide in scientific notation

- **Clarification 1:** for addition and subtraction, exponents within 2 of each other.
- **Guide's worked example:** 2.31×10¹⁵ + 9.1×10¹³ = **2.401×10¹⁵**. ✓
- **The guide asks for colour-coding coefficients against powers.** We do not colour student
  pages (house style), so this becomes a notes line that names the two parts and handles them
  separately.
- **Fluency with and without a calculator** is the guide's phrase. Our whiteboards do the
  no-calculator work by keeping the numbers hand-sized; nothing about calculators is printed.
- **Three named misconceptions — each one is a distractor we owe:**
  - `(1.3×10³) + (3.4×10⁵) = 4.7×10⁸` — coefficients added *and* exponents added. True value
    **3.413×10⁵**. ✓ (and 4.7×10⁸ is indeed not equal to it ✓)
  - `(2×10⁴)(3×10⁵) = 6×10²⁰` — exponents multiplied instead of added. True value **6×10⁹**. ✓
  - leaving **12×10⁹** instead of renormalizing to **1.2×10¹⁰**. ✓
- **Guide's task — meteorites** 1.1×10², 6.8×10², 8.4×10⁻² grams:
  - heaviest − lightest = 680 − 0.084 = **679.916 g** ✓
  - Part C: 680 ÷ 0.084 = 170000/21 ≈ **8,095 times** ✓
  - Part D: total = 110 + 680 + 0.084 = **790.084 g**, which is **≤ 850** ✓
- **Guide's items:** 7×10⁻⁸ + 6×10⁻⁸ = **1.3×10⁻⁷** ✓ ;
  (8×10²)(7.5×10⁴) ÷ (5×10²) = **1.2×10⁵** ✓ (the intermediate 12×10⁴ is exactly the
  renormalization misconception, so this item teaches and tests it at once — a good Example 2).

### MA.8.NSO.1.6 — real-world problems, and significant digits

- **Clarification 1 — the significant-digit rules the guide states:** leading zeros are never
  significant; trailing zeros are significant only when there is a decimal point; middle zeros
  are always significant; **a product or quotient keeps the least number of significant digits
  of its operands.**
- **Guide's task — Puerto Rico:** 3.98×10⁶ people (3 significant digits) ÷ 1000 people per
  square mile = **3.98×10³ = 3,980 mi²** ✓. The guide expects a discussion of whether the sig
  digits changed; strictly, "1000" as written is one significant digit, which would force one.
  **This is the subtle item of the unit** and it is where a student learns that the rule is about
  the measurement, not the arithmetic.
- **Guide's item — Amazon:** 5.5×10⁷ gal/s × 3.2×10⁹ s/yr = 17.6×10¹⁶ = **1.76×10¹⁷** exactly ✓,
  then to 2 significant digits (both operands have 2) **1.8×10¹⁷ gal** ✓.
- **Newer guide items:** 4.66×10⁸ calculations/s × 60 = **2.796×10¹⁰ per minute** ✓; 5 processors
  × 20 minutes = **2.796×10¹² calculations**, 3 significant digits ✓.
- **And one to watch:** 7.79×10⁸ m ÷ 3×10⁸ m/s = 779/300 ≈ **2.5967 s**, which the guide gives as
  ≈ 2.6 s (2 significant digits) ✓ — but strictly 3×10⁸ carries one significant digit, which
  would give 3 s. The reading notes already flag this. **We should not put an item in a bank
  whose sig-digit answer depends on reading an exact constant as a measurement.** If we use this
  context, the divisor gets written 3.00×10⁸.

### MA.8.NSO.1.7 — order of operations with exponents and radicals

- **Clarification 1:** six steps or fewer. **Clarification 2:** simplify radicals by factoring,
  within the ranges in §5.
- **The guide explicitly says to avoid the PEMDAS mnemonic.** It wants the structure taught —
  grouping symbols including the radical bar, then powers and roots, then multiplication and
  division left to right, then addition and subtraction left to right. Our notes must teach it
  that way and the word PEMDAS should not appear on any page.
- **Guide's worked example:** (−½)² + √(2³ + 8) = ¼ + √16 = ¼ + 4 = **17/4** ✓
- **Guide's tiered example:** (−⅓)² − ∛(2² + 4) = 1/9 − 2 = **−17/9** ✓
- **Guide's item:** ∛27 − 1.4(√(3² − 5)) = 3 − 1.4(2) = **0.2** ✓
- **Named misconceptions — our distractors:** confusing square roots with cube roots; performing
  operations in the order they are written (left-to-right regardless); recency bias (doing the
  operation most recently taught first); keyword hunting in word problems.
- **Guide's task — the Dotson backyard.** 600 ft² of yard as three equal squares, each 200 ft²,
  side √200 = 10√2 ≈ **14.142 ft** ✓. Arranged in an L with the house along the bottom edge two
  squares wide, the fence runs 8 sides − 2 = 6 sides = 60√2 ≈ **84.85 ft** ✓. Panels: 3½ × 6 ft
  at \$60.05 → **\$10.0083 per foot** ✓; 3½ × 8 ft at \$88.66 → **\$11.0825 per foot** ✓; the
  6-ft panels are the better value ✓.
  **Note for us:** √200 is not a perfect square, so this task sits at the edge of Clarification
  2. It is a legitimate guide task and the estimation is Unit 2 work the students have, but if we
  use it the radical must be left exact until the last step (Unit 2's "round last, not first"
  rule) and the item must say what precision it wants.

---

## 7. Structure check against the scope and sequence

- Six teaching days for eight book lessons, with 4.2+4.3 and 4.7+4.8 merged. That matches the
  pattern of Unit 3's 3.6+3.7 merge and needs no new ruling.
- **No thread day falls inside Unit 4.** Thread A was Unit 3; Thread B is Unit 6; Thread C is
  Unit 13. Unit 4 is six straight days plus the exam.
- Unit 4 is the **second unit of the three under MA.8.NSO**, and the Grade 8 FAST reports all
  three benchmarks under Number Sense and Operations — the same reporting category as 3.04–3.09.
  The unit review's parts will therefore split by benchmark, not by reporting category.
- The exam is **two periods** (ruling 14), so it takes the same shape as Unit 3's: one continuous
  question map, sections by benchmark, one point per lettered part, Score Tracker on the key.
- The flex day after the exam is in the calendar and is not a document we build.

---

## What is still needed, and why I stopped here

The Math Nation Unit 4 package did not arrive with the message that asked for this unit. Sections
1–4, 8 and 9 of the audit are statements *about the book* — which of its keys are wrong, which of
its items are unsound, what it does that our settled rules forbid, what was checked — and there is
no honest way to write any of them without the pages in front of me. Guessing them would be the
one failure Rule 0 names.

**To start the book-side audit I need the Unit 4 package** — the same shape as Unit 3's: student
edition, teacher edition, practice, additional practice, homework, stepping stones, the unit
assessment and all the keys. Split zip parts are fine.

Everything above is done and committed, so the moment the package lands the remaining work is
the book-side audit and then the build.
