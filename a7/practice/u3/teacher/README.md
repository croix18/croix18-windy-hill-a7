# A7 Unit 3 — Teacher copy (21 Oct 2026)

Make-up tests left the student pages on 21 Oct, and Unit 3 had no teacher copy to print them from. Croix sent the Unit 3 page
as it was before, its Print menu still offering them: *"This has the retake. Cant you make it off of that?"* Its questions are
`../` exactly — engine, coach, pictures, walkthroughs and unit, verbatim; only the kit around them was older — so this copy is
built from `../` like the Unit 4 teacher copies: the student page plus the kit's teacher bar (`kit/teacher.js`), which prints
**the real Unit 3 test** — its one form, as given on 15 Oct (36 points) — as the paper: Test / Test + key / Key only; and
Print → **Make-up tests** (one to five new forms of the whole unit, each with its key — what Croix calls the retake).
`gen_test.py` (kit `teacher_gen.py`) copies the test out of `a7/build/u3/unit.py`; `--check` proves test.js is current and
re-runs every item's `check` tuple under sympy.

**Published:** the private claude.ai artifact *A7 Unit 3 — Teacher copy* (https://claude.ai/artifact/P2dK5TFAbDsEBmShodx6JT).

This page holds the answer key in its source: it is its own private artifact, never linked for students — Google Sites gets
`../A7 Unit 3 Practice Test.html` only. Build: `python3 ../../kit/check/run.py .`
