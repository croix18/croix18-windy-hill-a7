# A7 Unit 6 — Teacher copy (25 Oct 2026)

The student practice page plus the kit's teacher bar (`kit/teacher.js`). **Ruling 49: the Unit 6 test is a random set of the
practice page**, so there are no fixed forms: `gen_test.py` (kit `teacher_gen.py`) reads `a7/build/u6/unit.py`, finds the
practice test alone (`assessment.forms = {"practice": …}`), and writes `test.js` with `random: true`. The bar then prints the
test as 1–5 forms, each a different set of the page headed as the Unit 6 test, every form's answer key on its own page (the
kit's make-up printout). The test is one period (ruling 51): 14 questions, 18 points.

This page holds the answer keys in its source: it is its own private file, never linked for students — Google Sites gets
`../A7 Unit 6 Practice Test.html` only. Build: `python3 ../../kit/check/run.py .` (runs `gen_test.py --check` and the kit's
`teacher_check.js`, then the lock and the browser checks).
