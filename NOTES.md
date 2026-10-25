# State of the work — 25 October 2026 (read this first)

## 25 October, 4 pm — Unit 6 checked again after its fixes (content version 4); the website brought up to date

Croix, 3:11 pm: *"Is everything else pushed to the site and updated?"* Both courses' published units and every app were
current on the site except **Tally** (the site's copy was older than Tally `7e135ab`; Tally's own tests passed, 46 suites,
1461 checks, and it is synced). A fourth reader, who had seen none of the work, then read only what the second review's
fixes changed in Unit 6: every new number right, **eight findings, all taken** (audit §8, "The check after the fixes"):
- **6.07's warm-up** is a 17-ft ladder 8 ft out (15 ft up): the 10/6 ladder was the Review's Q11 word for word.
- **The Reference Sheet's converse example** is 24, 40, 32, as 6.01's Notes III (the old 9, 15, 12 was the test's 9-12-15).
- **T-B1 board 7** asks its question beside a larger figure; the edition says what the slide says.
- **6.04 Example 2** is an 8-ft ladder 3 ft out (√55 ≈ 7.4): the old 12/5 was board 1's pool.
- **The kite** (the page's question 5 and 6.04's independent question 6): "Straight below the kite, level with the hand
  that holds the string, is a point 12 meters from the hand." The Hint no longer says that leg lies along the ground, and
  the page never draws 6.04's own kite (19 m, 12 m) — `engine.js` `ASKED`, enforced by `u6_check.js`.
- **Repeats inside the lessons:** 6.06's bank question 4 (now (−6, −3), (6, −3), (0, 5): 32), 6.04's bank courtyard (now
  5 m by 13 m: about 4.1 m shorter), 6.05's independent question 6 (now the park at (8, 8): √221 ≈ 14.9 km).
- Two words: "The the mirror's size" in 6.07's edition; 6.01's note to the teacher named the old warm-up.

The page is **content version 4** (version 3 was up about an hour, on a Sunday), 35 of 35 plants caught; the page and the
teacher copy checked and built; Unit 6 rebuilt and installed at 0 findings; master sheet regenerated.

## 25 October, afternoon — Unit 6's second review done; Unit 6 and Thread B go back on the website

Croix, 11:14 am: *"Take them down until a review chat goes over them. Then put them back up."* The second review of Unit 6
(three readers, each alone — Croix asked for Fable; the Fable readers were refused for rate, so the same three ran on Claude
Opus 5.5) found no wrong key and no blocker. Its 9 major and about 50 minor findings are fixed or judged in the audit, §8,
"The second review" (`a7/reference/A7 Unit 6 Relationships in Triangles - Audit.md`). The headlines:
- **Ruling 43 on the test.** The lessons now show only the 3-4-5 and 6-8-10 triangles (6.01's warm-up and Notes III, 6.04
  Notes II and 6.07's warm-up changed); the page draws 4(a) from 5-12-13 and 9-12-15 and keeps 4(b), 5, 7 and question 2
  off every number a warm-up, notes slide, example or Your Turn showed — `u6_check.js` fails a set that does not. **When a
  Unit 6 lesson's shown numbers change, change `engine.js`'s SHOWN lists with them** (the page's README says how).
- **The page:** half of question 5 is a leg in a story (a ladder, a ramp, a kite) to the tenth; no option order gives a key
  away; no Hint states its own answer; "Like the real test" credits follow-through; content version 3; 35 of 35 planted
  errors caught. The page and the teacher copy are checked and built.
- **The lessons:** 6.01, 6.03, 6.04 (boards 1, 4, 6, 7 and independent question 6), 6.05 (independent question 6), 6.06
  (board 3's reveal draws the height; independent question 1), 6.07 (Your Turn 1's reveal, board 8), and Thread B's slide
  text; the deciding step is labelled on three worked slides.
- **Kit:** Windmill `d4d2048` (a coordinate's minus sign; the page's mode to the coach), `95c6fb0` (a printed question never
  split across a page), `74dbaab` and `ee0544b` (the plans' warm-up and IXL rows), `71f5138` (the Score Tracker kept whole;
  a single paper's sections named) — vendored. Unit 6 rebuilt and installed at 0 findings; the master sheet regenerated.
- **Back on the website:** A7 `5200cc3b` published to site `782f69d` (deployed, Workers Builds: success) — Unit 6, its
  practice page and teacher copy, and the T-B1 and T-B2 slides; `hold.json` no longer holds A7 Unit 6 (M7 Unit 8 is
  still held). The Google Sites embed, `a7/practice/u6/A7 Unit 6 Practice Test.html`, went to Croix.
- **Not done, judged** (audit §8): new worked slides the readers asked for — Your Turns that change only the numbers, a
  6.01 Notes II example, a 6.07 nested pair, the T-B2 reverse steps, two Thread B boards. For the next build of these lessons.

## 25 October, 1 pm — ruling 54 (one title and numbering hierarchy); Units 3–5 rebuilt; Unit 6 in its second review

Croix, 11:28 am, of a printed Unit 6 test whose section "1. Triangle Inequality and the Converse" sat over question "1.":
*"Look at this numbering. It's confusing. 1.1. can you get a logical common sense title and numbering heirarchy across both
courses so we can avoid this."* **Ruling 54** (HOUSE STYLE 13b(xxvi)): a section is named, never numbered, on any page that
numbers its questions; questions run 1, 2, 3 … through the page; parts a, b, c; choices A–D; a lesson is called by its code
("Lessons 6.01–6.02", never "Lessons 1–2"). Windmill `9aac4a9`, `ee0544b`, `74dbaab`, `95c6fb0` vendored: the test forms,
practice test, keys, review and reference sheet by section name and lesson code; the page's sections, "only" choices and
results by name; the printed test headed as the paper with Name, Date and Period and never a question split across a page;
the Lesson Plan's IXL row "Start the skills; due by the Unit N test." (ruling 53), its warm-up and notes rows in the
Teacher's Edition's words. Rebuilt at 0 findings and installed: **Units 4 and 5**; the pages and teacher copies of **Units 3
and 4**. **Unit 4's Forms A and B (Mon 26 Oct) were sent to Croix again** with the new headings. Unit 3's package is not
rebuilt (re-timing taught lessons, as before).

**Unit 6 and Thread B are off the website** until the review chat's second review is done (Croix, 11:14 am: *"Take them
down until a review chat goes over them. Then put them back up."*; the site's `hold.json`). The review chat is fixing what
its three readers found; do not publish Unit 6 from here.

## 25 October, late morning — the kit's open items closed; Units 4–6 reinstalled; the website up to date

Croix, 9:15 am: *"Fix the kit, fix units 4 and 5 … Don't move on yet to unit 11."* Then 9:36: *"Yes please see to each
one of those issues. I give you permission to edit and to make fixes on the website."*
- **The kit (Windmill):** `7611a99` — a test paper says how long its test is: the plan's test days for the unit, else
  `EXAM_PERIODS` (1 in `a7/build/course.py`, ruling 51); the teacher copy's printed test the same, with no "Answer:"
  lines; the Lesson Plan's Notes row without the exponents unit's "Expand once per law". `02de689` — figures on a Lexend
  paper lettered in Lexend (ruling 46); the division Hint never states its answer (for 45 ÷ 3 it said "45 − 30 = 15 is
  left"; `check/hints.js` now reads 400,000 of them); the teacher bar's wording. Both sit on the head engineer's ruling 53
  (`fbac773`, IXL due by the unit test), which every unit below is built on.
- **Units 4 and 5 rebuilt and installed at 0 findings:** every form reads "one class period" (Unit 4's test is Mon
  26 Oct; its two forms were also sent to Croix); Unit 5's Reference Sheet prints "scale factor (k)" (its "($k$)" showed
  its dollar signs).
- **Unit 6 — triangles named by their corners** (the FAST reader's note): 6.07's Notes II teaches "triangle ABC is
  similar to triangle DEF" — the order of the letters is the matching; board 2 is a named turned pair (now 6-8-9 and
  18-24-27, so the small triangle's letters clear its lengths); independent question 2 gives names and lengths only. The
  practice paper's question 12, the Review's Part F question and the Reference Sheet name their triangles; half the
  practice page's question-12 sets do, the corners lettered, Show me how and the Hint using the letters; the oracle works
  x out by the letters and by size and they must agree; 33 of 33 planted errors caught; content version 2 (audit §8).
  Rebuilt and installed at 0 findings.
- **Practice pages rebuilt on the new kit:** Units 3, 4 and 6 and their teacher copies (every check passed).
- **Unit 3's package is not rebuilt:** today's kit counts a vocabulary minute, and 3.01's whiteboard round would drop to
  9 minutes (the floor is 10), so a rebuild means re-timing lessons already taught. Its test (15 Oct) is over; print a
  Unit 3 make-up from the teacher copy, which is fixed. Its package papers still say "two class periods".
- **The stale kit copy at the top of `a7/` is removed** (52 files, 24 Oct; nothing read it).
- **The website** (mrshaffer-site `08741ba`, deployed — Workers Builds: success; Croix's permission at 9:36): A7
  published from `a7302000` — every unit's package, the practice pages and teacher copies, the web slides; the A7 course
  page regenerated. **Unit 6 and Thread B were then taken down** (site `26d4820`, the head engineer's session — Croix,
  11:14 am: *"Take them down until a review chat goes over them. Then put them back up."*) and the site's `hold.json`
  keeps them off until a review chat publishes them (site `1da4c03`).
- **Windmill:** `7611a99`, `02de689`; HANDOFF `76e7cf2` (M7 should vendor `02de689`).
- **11:12 am — Croix: *"Can you get rid of one class period. I don't need that text at all."*** Windmill `ca12f9b`: a
  one-period test says nothing about its length (the papers and the teacher copy's printed test); M7's two-period papers
  keep theirs. Units 4 and 5 rebuilt and installed at 0 findings (each form's head is now "Form A · 29 points"); the
  teacher copies of Units 3, 4 and 6 rebuilt; site `300fd5b` (deployed): Units 4 and 5 and the teacher copies of Units
  3 and 4 republished, Unit 6 still held for its review.

## 25 October — A7 Unit 6 and Thread B are built, reviewed and installed

The kickoff ("KICKOFF — A7 Unit 6 and Thread B", followed step by step) made this the build chat for **Unit 6,
Relationships in Triangles** (taught Fri 6 – Mon 16 Nov, the test Tue 17 Nov) and **Thread B** (Wed 18 – Thu 19 Nov,
after the test and not on it). Ruling 52 moved the year mid-build (Unit 11 in December; slope is Unit 10).

- **Built (`a7/build/u6/`, 0 gate findings):** 6.01 (book 6.01–02 merged, MA.8.GR.1.3), 6.03 and 6.04 (GR.1.1), 6.05 and
  6.06 (GR.1.2), 6.07 (book 6.07–08 merged, GR.2.4), Thread B 6.T1 (T-B1, GR.1.4, the 43-minute Wednesday) and 6.T2
  (T-B2, GR.1.5); `u6/unit.py` — the Reference Sheet (the state's two theorems as the FAST sheet prints them), the Review
  (home Mon 16 Nov; A7 has no review day) and the **Practice Test alone, as the test's blueprint** (ruling 49: the unit
  test is a random set of the practice page; 14 questions, 18 points, 3 / 6 / 6 / 3, one period, ruling 51).
- **Installed** (`a7/packages/A7 Unit 6 - Relationships in Triangles/`): `build_all.py u6 --install` at 0 gate and 0 check
  findings on Windmill `c9c3e8a`, and again later that day on `02de689` (above); the master sheet regenerated, 0
  problems.
- **The practice page (`a7/practice/u6/`), built:** `A7 Unit 6 Practice Test.html` and the teacher copy
  (`teacher/A7 Unit 6 Teacher Copy.html`), each with its CHECKED. Its checks — `u6_check.js` (3,000 sets), `verify.py` (a
  sympy oracle that reads every question back from what a student sees), 31 planted errors — the stability lock, the
  variety floor and the kit's browser check pass. The teacher copy prints the test as 1–5 random sets with the paper's
  shape (no set number on a student's sheet; points; the key with its set number and the score tracker). Held off the
  website until a review chat goes over the unit (Croix, 25 Oct, 11:14 am; the site's `hold.json`).
- **The unit's standing decisions** (audit §6): every square root a student takes has a whole radicand up to 225
  (Clarification 3, read literally), so a whole hypotenuse is 5, 10, 13 or 15; no radicand on the papers has a square
  factor; no distance formula (a slanted distance is its right triangle on the grid); every mirror and nested item says
  its triangles are similar.
- **Reviewed before shipping** (kickoff step 7): an explicit-instruction reviewer, an adversarial critic and a Florida FAST
  item-writing educator, each alone — 8 blockers (5 different), 41 fixes, 31 notes, with the fixes, in the audit's §8
  (`a7/reference/A7 Unit 6 Relationships in Triangles - Audit.md`).
- **The kit, fixed with Croix's permission** ("Fix it. I give you permission", 25 Oct) in Windmill `c9c3e8a`: `deckkit`
  gives a wrapping IXL skill name the rows it needs (T-B1's two long names overprinted the next row, so the unit could
  not install); the practice kit's printed test has the paper's shape and no set number on the student's sheet; its
  browser check reads "&lt;" as "<". Vendored here (`tools/vendor_windmill.py`; `practice_kit.py --vendor`).
- **Commits:** `943d42c7` audit and outlines · `5543d4a5` 6.01 · `f26614d3` 6.03 · `4f76e0b6` 6.04 · `a5222251` 6.05 ·
  `64677830` 6.06 · `1b8682be` 6.07 · `a1d0d7b7` T-B1 · `9f55139e` T-B2 · `b8ff3013` unit documents · `292d4c00` the
  practice page · `b5638493` the review pass · `28e8a92c` the notes before the install · then the install and the built
  page, on Windmill `c9c3e8a`.
- **Open:** nothing from the kit list (all fixed, above). Unit 3's package papers still say "two class periods" (above).
  The Windmill HANDOFF's own open items (publish_web.py and unreviewed units) are not A7's.
- **Next:** Unit 11, Solving Equations and Systems (MA.8.AR.2.1, AR.4.1–4.3) — taught Mon 30 Nov – Thu 10 Dec, the test
  Fri 11 Dec; due 23 Nov, the same procedure in `u11/`.
