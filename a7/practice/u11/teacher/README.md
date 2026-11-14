# A7 Unit 11 — Teacher copy (14 Nov 2026)

The student practice page plus the kit's teacher bar (`kit/teacher.js`). **Ruling 49: the Unit 11 test is a random set of the
practice page**, so there are no fixed forms: `gen_test.py` (kit `teacher_gen.py`) reads `a7/build/u11/unit.py`, finds the
practice test alone, and writes `test.js` with `random: true`. The bar pins Tests A and B, prints make-ups (and, since 14 Nov,
all-multiple-choice make-ups from `Unit.choices`), every key on its own page with its set number and check code. One period
(ruling 51): 14 questions, 18 points.

This page holds the answer keys in its source: it is its own private file, never linked for students — Google Sites gets
`../A7 Unit 11 Practice Test.html` only. Build: `python3 gen_test.py`, then `python3 ../../kit/check/run.py .`.
When `unit.py`'s practice paper changes (the lead's review of 14 Nov), run `gen_test.py` again and rebuild.
