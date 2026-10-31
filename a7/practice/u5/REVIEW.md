# A7 Unit 5 practice page — the review (30 Oct 2026)

Ruling 55 (Croix, 25 Oct, 4:52 pm) and the review rule (24 Oct: *"I'd like for a fable chat to run over it before it gets
pushed for extra redundancy"*). The page was built and checked on 25 Oct and held, unpublished, for its review; the three
readers launched that evening were cut off by the usage limit. Three fresh readers (Claude Fable 5.1) read it on 30 Oct, each
alone: the critic (keys, typing, claims, fuzzing), the educator (the forms, the lessons, the Hints, the phone) and the student
(the built page in Chromium, as a 12-year-old types). **No wrong key; nothing wrong marked right.** Their findings, and what
was done about each, follow; their scripts are in the session's scratch (`review-a7u5/<role>/`).

**State, 30 Oct, late evening — published.** Every item below is fixed or marked not taken, the checks pass
(`python3 ../kit/check/run.py u5` and `u5/teacher`: u5_check on 3,000 sets, verify.py in sympy with the lessons read from
their own specs, 36 planted errors, the lock, the variety floor, the browser checks), content version 1.

## Major
1. **Q19's choice format gave the decision away** (educator): in the 51% of sets where the bigger number is the slower one,
   the right option was the only one naming its vehicle; in most of the rest all four named the same vehicle; a real 2–2
   split in 8% of sets — and the arithmetic forces it (every wrong method favours the km/h mover there). **Fixed: Q19 is
   typed.** "Which is faster? Type its name, and the bus's speed in km/h." The name decides and the conversion proves it:
   the slower one's name with the right conversion is wrong ("compare the two km/h speeds"), the number alone or the name
   alone is Almost, two names are not read, the five wrong routes (the km/h as it stands, the mi/h as it stands, ÷ 1.61,
   the km/h × 1.61, the km/h × 0.62) are named, the sheet's other ratio (÷ 0.62) earns the point with the note. The check
   reads the stem, recomputes the faster one and the conversion, and types the key fourteen ways with and without the name.
2. **Q15's rate line was cut off on phones** (educator, student): at 360 px 32 of 40 sets overflowed (Canadian, Australian,
   British); the currency's name sat inside the math span, which cannot wrap. **Fixed:** the number in math, the name
   outside; the check fails on a word inside the rate's span.
3. **Q18 drew the forms' mixtures with the colors reordered** (educator): set 503 was Form A Q18 (3 : 2 : 4 with 9 of the
   3-part) as 3 : 4 : 2 with 9 buckets of cement. **Fixed:** a mixture's key is its sorted parts, the known part's share and
   the amount (`mixKey`), in the engine, in `test_forms.js`, in the lessons' and the papers' lists, in both checks.
4. **Show me how on part (b) handed over part (a)'s answer** (educator): 16(b)'s lines said "One full tank goes 15 × 14 =
   210 mi (part a)" and 6(b)'s "The room for real: 5.5 × 2 = 11 ft by …"; (a) then earned its point "on your own". **Fixed:**
   the kit now passes the coach a context (whether part (a) is right yet, whether this is a fresh one); until (a) is right,
   6(b)'s and 16(b)'s worked lines say "your part (a)" and never its number (checked over every set).
5. **Ruling 43 gaps** (educator, critic): 5.02 Example 2's 3 → 12 (k = 4) and its Your Turn's 2 → 10 on Q1 (and reversed on
   Q2), 5.02's 18 cm² → 288 cm² and its "areas 25 and 100" on Q5, 5.04 Notes III's 3.5-in wall at ¼ in : 1 ft on Q6, and the
   5.06 money lines run backwards ($100 → 92 euros; 73.60 euros → $80; 162 CAD → $120) on Q15. **Fixed** in the engine's
   list — and in `verify.py`'s own reader of the lesson specs, which now reads "k = √16 = 4, 3 × 4 = 12", "A = 18 × 4² =
   288", "14 ÷ 4 = 3.5 in" and a money line worked either way, so the check stays independent of the engine's list.
6. **The sheet's other ratio, landing on a whole number, was called "rounded"** (critic; 13% of sets): 66 gal → 66 ÷ 0.264 =
   250 exactly was "Almost — that is the answer rounded"; 19.5 yd → 1800 "rounded to a whole number". **Fixed:** the other
   ratio's exact answer is checked first and marked right ("66 ÷ 0.264 = 250"); the check no longer treats a rounded key
   that is exactly the other ratio's answer as unfinished.
7. **The forms' numbers reached the page through other slots** (critic): Q19 printed Form B's transfer conversion
   "55 mi/h = 88.55 km/h" (set 1), Q14 Form B Q8's 48 ft², Q9 Form A Q11's 144 in, Q10 Form A Q10's four expressions at
   70, Q16 the forms' 390- and 440-mile ranges and Form A's 1,000-mi trip. **Fixed:** new slots `amount` (an amount with
   its pair of units, either direction), `range`, `tripD` and `speedM` (the transfer item's mi/h speed), listed in
   `test_forms.js` from the forms, derived by `verify.py` from `unit.py`, hashed in the page.
8. **A fresh one ("Try another") on 6(b)/16(b) referred to a part (a) it did not have** (student). **Fixed:** the kit marks a
   fresh one; its Hint and Show me how are the whole walk (the miles on one tank first; both walls first). Checked.
9. **A Hint step wanting a repeating fraction refused the decimal** (student): Q17(b) "10 ÷ 1½" wanted 20/3 and called 6.67
   wrong after sending the student to 100 ÷ 15. **Fixed:** Q17(b)'s recipe count always ends; the check fails on any Hint
   number that does not.

## Minor
- Q3's and Q10's last Hint step had the right letter set first in 100% of sets (`keep`) (student). **Fixed:** shuffled.
- Q5's last hint "Try a few: 2 × 2, then 3 × 3" named the answer when k = 2 or 3 (all three). **Fixed:** "Try the whole
  numbers in turn until one works."
- A fresh one could share the revealed answer (Q5 19%, Q16b 18% of pairs) (student). **Fixed in the kit:** Try another
  rejects a question with the same answer as well as the same numbers.
- The inverted ratio (n × the other ratio, 5.08 Example 1's named board) was not named on Q9/Q11/Q12/Q13 (educator). **Fixed:**
  named ("multiplied by the sheet's other ratio, 0.39 — the one for 1 cm, the unit you want: that ratio divides"); a number
  that is one mistake exactly and another rounded names both.
- "Almost Almost — that is the answer rounded" (the tag and the sentence) (student). **Fixed:** the sentences no longer begin
  "Almost".
- Truncation ("5.7" for 5.75, "215" for 215.9) got the generic message (critic, student). **Fixed:** "That is the answer cut
  off after one decimal place, not rounded" (Almost), when it is not a named mistake.
- An unsimplified fraction typed for a decimal key: "simplest form: 0.4 (or the decimal)" (critic). **Fixed:** "in its
  simplest form, 2/5 — or as the decimal, 0.4."
- Q6/Q7 drew scales no paper uses (½ in : 3 ft, ½ in : 5 ft, ⅛ in : 1 ft, ~30%) (educator). **Fixed:** ¼ in : 1 ft, ½ in :
  1 ft and 1 in : r ft, the lessons' and the forms'.
- Q16's mpg and tank drawn independently ("a pickup gets 40 mpg", "a car gets 15 mpg with a 25-gal tank") (educator,
  student). **Fixed:** the tank fits the mileage, and the vehicle fits both.
- No answer box set a phone keyboard (student). **Fixed in the kit:** a part may ask for the decimal keypad; every box here
  does but 17(a)'s, which needs a space for its mixed number.
- "31/2" → "Did you mean 3 1/2?" named the right number to a student who may have meant 15.5 (the M7 Unit 9 re-read's
  point). **Fixed:** the nudge no longer states a number.
- Not taken: units are never checked ("90 in^2" for a perimeter is right — the page says "type just the number");
  Q14's Hint wants 0.093025 exactly where the sheet shows 0.093 (the Hint's own multiplication; a kit tolerance would be
  the change); Check-as-I-go's Finish leaves a blank card unlabelled, and 6(b)'s "fix part (a) first" stays after (a) is
  fixed until (b) is re-checked (kit behaviour, noted for Windmill); `5 x 2` read as 5 (the reader takes "x 2" for a
  squared unit); the Q19 "same answer on a fresh one" case is covered by the kit change above.

## Outside the page — the printed test (for Croix; not changed)
- Form A question 14's answer is on the unit's reference sheet (20 ft² = 1.86 m²); Form A question 1 (4 cm → 10 cm) is 5.01
  Example 1's second pair of sides and Form B question 1 (6 → 9) is 5.01 Notes I's; Form A 6(a) (the 3-in wall at ¼ in :
  1 ft) is 5.04 Example 1's; Form A question 17 works 5.10 Notes III's 2.5 × 1½ = 3¾.

## Checked and sound (the readers)
Every key recomputed from the printed words by two independent readers (3,000 and 20,000 sets); every MC and select-all key;
every printed ratio the FAST sheet's; Q14's "closest" unambiguous by both sheet routes; right answers typed 20+ ways all
right; every modelled mistake named by its own words and never right; near misses never right except the sheet's other
ratio; no false arithmetic claim in any stem, option, feedback, rule, worked line or Hint; follow-through 6(b)/16(b) in both
modes; 20,000 random strings read without a crash; "Like the real test", Check-as-I-go, the menus, sets, print preview, dark
mode and the phone layout (but Q15) all as designed.
