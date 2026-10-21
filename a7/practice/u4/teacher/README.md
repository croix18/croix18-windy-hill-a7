# A7 Unit 4 — Teacher copy (19 Oct 2026; rebuilt 21 Oct)

The student practice page plus the kit's teacher bar (`kit/teacher.js`) that prints **the real Unit 4 test** — Form A or
Form B (ruling 33) — as the paper: Test / Test + key / Key only. `gen_test.py` (kit `teacher_gen.py`) copies both forms out of
`a7/build/u4/unit.py`; `--check` proves test.js is current and re-runs every item's `check` tuple under sympy on both forms.
The key carries the key notes, the transfer flags and the score tracker.

21 Oct 2026: rebuilt from the test without significant digits (29 points; Part 2 is the area, the speed, the sum and the
difference, answered exactly), after the folder was lost with the session that first wrote it.

This page holds the answer keys in its source: it is its own private artifact, never linked for students — Google Sites gets
`../A7 Unit 4 Practice Test.html` only. Build: `python3 ../../kit/check/run.py .`
