# Unit 3 — Exponents and Scientific Notation: audit of the Math Nation package

Read: unit Teacher Edition (108 pp., every student page with answers), Student Edition, all nine
Additional Practice + keys, all nine Homework + keys, Stepping Stones, Assessment + Key + Guide,
Worked Examples, the nine slide decks (text + equation-object count). Every problem worked; every
printed value recomputed. TE page numbers below are the printed page numbers (188–289);
SE pages are 99–151.

Source files stay outside the repo (Math Nation copyright) at `/root/mn/unit03/` in the build
container; only this audit and the working log are committed.

---

## 1. Bottom line

The mathematics of the lessons themselves is sound: every value on every student page in 3.1–3.9
checks. The defects are in the **answer keys** (three wrong numbers), in **two homework items
that are wrong as written**, and in a handful of TE-only slips. Nothing here changes the scope
and sequence; the 3.06+07 merge and the Thread A placement after 3.07 both hold up.

## 2. Defects — student-facing or key (must not propagate into our banks)

| # | Where | Printed | Correct | Note |
|---|---|---|---|---|
| D1 | Additional Practice L1 #7 key | (−3·6)⁴ = (−18)⁴ = **104,796** | **104,976** | digit transposition |
| D2 | Additional Practice L8 #2 key | 10⁶ + 10⁴ = **101000** | **1,010,000** | |
| D3 | Additional Practice L9 #3 key, row 1 | (10⁴) − 4×10²⁵ = −40,000,000,000,000,000,000,000,000 | −39,999,999,999,999,999,999,990,000 | key gives −4×10²⁵ exactly; the 10⁴ was dropped. The item itself is odd ("(10⁴)" reads like a stray coefficient) — do not reuse. |
| D4 | Homework L3 #7 key | (¾)⁶ = 729/**4,046** | 729/**4,096** | |
| D5 | Homework L9 #4b key | 10⁻⁸ is **3** times smaller than 10⁻⁵ | **1000** (10³) | |
| D6 | Homework L9 #4c key + item | 7.4×10⁻⁸ is **3000** times smaller than 0.000039 | true ratio 0.000039 ÷ 0.000000074 ≈ **527** | **Item design flaw.** The scaffold ("7.4 is ≈2 times larger", "10⁻⁸ is 1000 times smaller") pulls in opposite directions, so the multiply-the-two-comparisons routine taught in 3.9.6 gives 2000, and the key's 3000 comes from nowhere. Retire the item; a sound version keeps the coefficient comparison in the same direction as the power comparison (e.g. 1.8×10⁻⁷ vs 7.2×10⁻⁴ as in SE p.150). |
| D7 | Homework L9 #5 item | "112 ten millionths" matched to 1.12·10⁻⁷ | 112 × 10⁻⁷ = 0.0000112 = **1.12×10⁻⁵** — the same value as the "0.0000112" row | Two left-hand values collide and 1.12·10⁻⁷ has no partner. Rewrite as "112 billionths" (= 1.12×10⁻⁷). |

## 3. Defects — teacher-facing only (TE margins / guide; harmless to students, noted so we never copy them)

- TE p.226 differentiation thumbnail: (−4)³·(−4)⁻⁷ shown as −64/16384 = −1/256. **Correct is 1/256**; the student page (p.233) has it right (−64/−16384).
- TE p.275 margin: scientific notation constraint written 1 ≤ |a| **≤** 10. Correct is 1 ≤ |a| **<** 10 (the student glossary on p.274 and TE p.270/p.281 are right).
- TE p.270 and p.276 margins: "they may think 10⁵ is two times larger than 10⁵, because 5 − 3 = 2" — second 10⁵ should be 10³.
- TE p.196 component overview: "product of a power exponent law" → power of a power. TE p.198 (identity law) note says "power of a power". TE p.222 names a law "quotient of a power". Practice L3 #3/#6 blanks say "quotient of a power" while the word bank says "quotient of powers". Practice L5 header says "questions 6–10" for a table that is 7–10.
- TE p.285 intro refers to 10⁻¹¹/10⁻⁴ "in the table from the Exploration"; it is not in that table.
- SE p.148 (3.9.2 Q4) sample answer "the exponent is always one less than the total number of places in the place value" is muddled (10⁻² ↔ hundredths = 2 decimal places). Our version will say the place value's decimal position equals |exponent|.
- Sample answers use "inverse" for reciprocal (p.230). We say reciprocal.
- Practice L1 #10 key stops at 2¹⁰ though the column asks for the evaluated value (1,024).

## 4. Conflicts with our settled rules (not errors; just what changes in the rebuild)

- **Partner/group work.** Every Exploration/Collaboration/Station in 3.1–3.9 is "with your partner" or "in teams of three" (3.3.4 Roundtable). All of it converts to solo work; the discovery tables survive as-is because a single student can complete them.
- **Videos.** 3.1.1 (growth-mindset video) and 3.4.1 (ichthyologist career video) are video warm-ups. Our period has no video slot; these are replaced by a math warm-up (quiz slot).
- **Calculators.** The MN assessment is headed "No Calculator" and the guide repeats it. Our rule: calculators allowed, nothing printed. The values on the MN test are all hand-doable anyway (1.331, −15.625, 169/81…).
- **Partial credit / points.** MN guide: 100 points, 4 per item, 12 per select-all "4 per correct box", partial credit for "minor mathematical error" on Q1–4. Ours: one point per lettered part, no partial credit.
- **Notation.** MN assessment Q3 writes negatives with a raised minus: (⁻5)³·4⁰/(⁻1⁷). We never do; we write (−5)³·4⁰ ÷ (−1)⁷ with explicit parentheses. Also MN writes products like (−3 · −2)⁸ and 1/(−4⁻⁵); we always parenthesize a negative base: (−3 · (−2))⁸, 1/((−4)⁻⁵) — the second one is ambiguous as MN prints it (the value happens to be the same either way, −4⁵ = (−4)⁵, which is why their key survives).
- **Benchmark codes** are printed on MN student pages (slide 2 of every deck, TE headers). Ours carry none.

## 5. Capcheck (ruling 29) — Unit 3 content against the Grade 8 guide

- 8.NSO.1.3: every exponent in the unit is an integer; every base is rational. No fractional exponents anywhere. **Pass.**
- 7.NSO.1.1 (carried, 3.1–3.3): whole-number exponents, rational bases incl. negatives and decimals. **Pass.**
- 8.NSO.1.4: coefficients in [1, 10) throughout; both directions (large/small) and "how many times" by coefficient ratio × power ratio. **Pass.** One unit-wide gap vs. the guide (see §6).
- Assessment Q10 asks for "bˣ where x is a positive number" and the key gives −1/18 (which is (−1/18)¹). Acceptable but the item is weak; ours will not ask for the form when the exponent would be 1.

## 6. What the guide expects that Math Nation never does (goes into our banks)

From the B1G-M reading notes for 7.NSO.1.1 / 8.NSO.1.3 / 8.NSO.1.4:

1. **Working backwards / unknown exponent**: 7ⁿ/7² = 343 → n = 5; (5²)ⁿ = 5¹⁰ → n = 5. Not in any MN lesson, practice or test.
2. **−b versus b⁻¹** as an explicit contrast task (MN only touches it in 3.4.7's Ellen item, 5⁻² ≠ −25).
3. **Calculator "E" notation** (2.3147E27) and comparisons that cross from very large to very small (≈10³² times). MN compares only within the same sign of exponent.
4. **"Aryella says 10⁰ = 134⁰"** style zero-exponent equality items.
5. **Fluency with and without a calculator** — the guide's phrase; our whiteboards do the no-calculator work by keeping values hand-sized, not by printing a rule.
6. The guide's misconception list to name in distractors (distractorcheck): multiply/divide the *bases*; add instead of multiply in power-of-a-power (and the reverse); negative exponent makes the value negative; 4² × 4⁻⁶ sign/reciprocal slips; "10⁴ times" read as "4 times"; multiplying the exponent when scaling (3 times 3×10³ → 9×10⁹); coefficient outside [1,10).

## 7. Structure check against the scope and sequence

| Our row | MN source | Verdict |
|---|---|---|
| 3.01 Product laws | 3.1 (SE 99–105) | as planned |
| 3.02 Quotient laws | 3.2 (106–111) | as planned |
| 3.03 Exponential expressions (multiple laws) | 3.3 (112–117) | as planned |
| 3.04 Negative exponent law | 3.4 (118–123) | as planned |
| 3.05 Applying exponent laws (rational bases, negative exponents) | 3.5 (124–129) | as planned |
| 3.06+07 Evaluate / equivalent, integer exponents | 3.6 (130–134) + 3.7 (135–139) | **merge confirmed**: 3.6 is "evaluate with several laws", 3.7 is "rewrite to a common base (8⁵ = 2¹⁵) and decide equivalence"; together they are one period of practice plus the common-base idea, which is ten minutes of new content. |
| T-A1, T-A2 (8.AR.1.1, variable bases) | Unit 14 lessons 1–4 | placed after 3.07, before scientific notation — the laws are all in hand by then. |
| 3.08 Large numbers | 3.8 (140–145) | as planned |
| 3.09 Small numbers; how many times | 3.9 (146–151) | as planned |
| 3.X1–X2 Unit exam | MN assessment (20 items) | MN items restyled per §4 become bank seeds only if approved (§8). |

## 8. Judgment calls (only these)

1. **MN items as bank seed, or original items only?** The MN practice/homework/assessment items are mathematically usable once the seven defects above are excluded and the notation is fixed. Using them (restyled, renumbered, answers re-derived by script) gets the Unit 3 banks up fastest; writing only original items avoids leaning on licensed material. I can do either; the checks run the same way.
2. **The two video warm-ups (3.1.1, 3.4.1)** — replace with math warm-ups (my default) or keep a 2-minute video slot on those two days?
   **RULED, 20 September 2026 — Croix: "Get rid of the video warm ups."** No video slot anywhere in the unit. Every lesson opens with the four-question spaced-retrieval warm-up; the 3.01 and 3.04 Teacher Editions record the replacement. Standing for every unit from here on.

Everything else is settled by existing rules and needs no answer.

## 9. Inventory of what was checked

- TE pp.188–289 (all nine lessons, every answer on every student page) — every numeric value recomputed; all match except the TE-margin slips in §3.
- Practice keys L1–L9 (18 pp.) — D1, D2, D3.
- Homework keys L1–L9 (18 pp.) — D4, D5, D6, D7.
- Assessment (20 items) + key + guide — all 20 answers correct (729; −1/128; 125; −15.625; select-all 1/64, (−8)⁻², (−8)²/(−8)⁴; select-all (6/1)¹, 1⁻¹/6⁻¹, 6; (7/12)³; (11/6)²⁴; (1/13)⁶; −1/18; (1/37)¹¹; 1.331; −1/120; 8/125; 169/81; 5.03×10⁵; 3.2×10⁶; 20; 1,390,000,000,000,000,000,000; 0.000008056; 4). Points total 100 as the guide says.
- Worked Examples (handwritten sheet) — correct.
- Slides — mirror the SE with answers blanked; equation objects not separately audited because the SE they copy was.
- Stepping Stones (Accelerate Learning's 3–6 item refreshers) + keys — values correct (1296, 1/8, 8¹⁰, 2²⁰, −2, 16/9, 3/2, 1, 4⁵, 16, 128, 32m¹⁵, f⁵, 10²², 10⁻², 10⁻¹, 0.001, 0.00001), but the sheets are weak: L5 and L6 repeat three items verbatim; L5 #1 asks for an exponential expression and the key gives the value 1/9; L7 #2 asks which law "simplifies 5⁶" (nothing does; key says power of a power); L9 #1 calls an expression an equation; L9 #5's sample answer 0.04 is not a power of 10. L8 #2–3 use variable bases ((2m³)⁵, f¹⁰/f⁵) — that is 8.AR.1.1, i.e. Thread A content, which is fine for us. Not worth mining.
