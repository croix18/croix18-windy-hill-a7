# A7 Unit 5 — Teacher copy (25 Oct 2026)

The student practice page plus the kit's teacher bar (`kit/teacher.js`) that prints **the real Unit 5 test** — Form A or
Form B (ruling 33) — as the paper: Test / Test + key / Key only. `gen_test.py` (kit `teacher_gen.py`) copies both forms out of
`a7/build/u5/unit.py`; `--check` proves test.js is current and re-runs every item's `check` tuple under sympy on both forms.
The key carries the key notes, the transfer flags (questions 8 and 19) and the score tracker (MA.7.GR.1.5 10, MA.7.AR.3.3 8,
MA.7.AR.4.5 6).

This page holds the answer keys in its source: it sits behind the teacher password on mrshaffer.org and is never linked for
students — Google Sites gets `../A7 Unit 5 Practice Test.html` only. Build: `python3 ../../kit/check/run.py .`
