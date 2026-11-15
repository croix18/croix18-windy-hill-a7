# State of the work — 14 November 2026 (read this first)

## 14 November — A7 Unit 11, Solving Equations and Systems: built, reviewed, fixed; held for Croix's word before it is published

Croix, 10:50 am: *"Can you get working on the next unit in a7"*. The next unit taught is **Unit 11** (ruling 52: before
Units 7 and 10; MA.8.AR.2.1 and MA.8.AR.4.1–4.3; seven days, Mon 30 Nov – Thu 10 Dec, the one-period test Fri 11 Dec).
One session did it as the brief of 24 Oct lays out (`Windmill/briefs`, "What comes next"): the lead (Claude Fable 5.2)
wrote the outlines, the briefs and the rulings on the review; Claude Opus 5.5 built each piece; three readers who had
not seen the specs reviewed it.

- **The plan and the audit** (`a7/reference/A7 Unit 11 Solving Equations and Systems - Lesson Outlines.md`, `… - Audit.md`):
  outlined from the benchmarks first, 126 equations solved by sympy before a spec was written; then Math Nation 11.1–11.8
  and its test read from Croix's Drive (kept in `/root/mn/unit11`, never in git) — **29 student-facing defects and key
  errors** (D1–D11, E1–E18), none reproduced. The outlines' nine standing decisions are the unit's rules; the three that
  matter most: **a line is graphed from a table of values and "slope" / "y-intercept" are not on a student page** (Unit 10
  comes later); **no substitution or elimination**; **a false ending is the false equation and its words** ("8 = 5, never
  true: no solution"), never "8 ≠ 5" as a line of work.
- **Built:** `a7/build/u11/` — `l01.py` 11.01, `l02.py` 11.02, `l03.py` 11.03 (a 43-minute Wednesday), `l04.py` 11.04,
  `l05.py` 11.05–06 (merged), `l07.py` 11.07 (43 minutes), `l08.py` 11.08; `unit.py` (the Practice Test, 14 questions,
  18 points — the test's blueprint, ruling 49; the Review with its SSDD block; the Reference Sheet); `manifest.py`;
  **`figs11.py`** — `plane` (a coordinate plane with one or two lines drawn from m and b, which refuses a stated
  crossing that is not on every line), `table`, `row`, `slide`. The module is named `figs11`, not `figs`: every unit's
  gates run in one process and a second module called `figs` was read as Unit 6's (`gates.py` crashed on `figs.strips`).
  The package is `a7/packages/A7 Unit 11 - Solving Equations and Systems/`; the master sheet has its rows.
- **The practice page** (`a7/practice/u11`, README there): one generator per question of the paper; every part over
  1,000 versions; `u11_check.js` (3,000 sets read back from their printed words), `verify.py` (sympy; what the lessons
  showed is read from the lesson specs — `python3 shown43.py --emit` after any lesson changes), 49 of 49 planted errors,
  `mc_check.js` (the all-multiple-choice retake). The teacher copy prints the test as random sets
  (`teacher/gen_test.py` after the paper changes). **Not published** — nothing of Unit 11 is on the website.
- **The review** (`/home/claude/work/review_*.md` in the session; the dispositions are in the audit's last section): no
  wrong answer, key, worked line or graph. One blocker — the Practice Test's 14(b) accepted a point that is on one line
  only — and 28 majors about what a student and a teacher can do with the pages; fixed in a second pass (the audit lists
  each finding and what was done).
- **`tools/`:** `master_sheet.py` and `check_master_sheet.py` load each unit's own figure module; `tex2text.py` and the
  sheet's check read an escaped dollar ("\\$24") as money.

### Open, for Croix
1. **Two kit limits shape the graph days** (Windmill `kit/`, not changed here): a Your Turn slide cannot carry a
   figure, and a paper's key prints the same figure as its page — so a graph-day Your Turn works from two tables, and
   the Independent Set keys of 11.07 and 11.08 give each crossing in words over the empty grid. A `fig` on a Your Turn
   and a key-only figure would fix both.
2. **Three IXL skills of the plan may ask for what Unit 11 does not teach yet** — TS7 "Write a system of equations given
   a graph", 9Z8 "Solve a system of equations in slope-intercept form", AGZ "Find the number of solutions to a system of
   equations by graphing" — read from their titles; nobody here could open IXL. If they need slope, they move to Unit 10.
3. **The kit's steps check refuses a false line** ("8 = 5") on an answer slide, so a board's no-solution ending is in
   words there; the worked examples print it.
4. **The build kit's printed Practice Test still prints the follow-through line** under each section (Unit 6's too;
   Croix's ruling of 7 Nov took it off every page). The test Croix prints comes from the teacher copy, which does not.
5. **START HERE's dates for 11.02 and 11.03 are a day late** — they come from the plan vendored on 25 Oct
   (`assets/windmill`); the scope and the lessons are right. `python3 tools/vendor_windmill.py` when Windmill's plan is current.
6. **The kit's Teacher Edition prints "neighbour"**; the lessons are in American English.
7. **The practice page's 14(b) (the estimate) has 38 different systems**, under ruling 49's floor of 100 — the kit's
   variety check passes because it counts 14(b) with its story (19,984). Lines whose crossing is well clear of every
   grid and half-grid line on a small window are few; a wider window or thirds-and-fifths coefficients would add more.
8. **The page's question 12 takes the ordered pair in one box** (the kit gives a part one box); the paper asks for x and y.

# Earlier — 25 October 2026

## 30 October, late — Unit 5's printed test: the repeats of the lessons changed (Croix: "Yeah change them")

Form A question 1 is now 8 cm → 20 cm and Form B's 12 cm → 18 cm (5.01's Example 1 and Notes I); Form A 6(a) is the wall
drawn 4.5 in (18 ft; the room 4.5 in by 3.5 in, 252 ft²); Form A question 14 is a 30 ft² patio (2.79 m²; the sheet's own
20 ft² = 1.86 m² is gone); Form A 17(a) asks for 14 servings (k = 3.5, 5¼ cups). `a7/build/u5/unit.py`; the unit rebuilt and
installed; the practice page's form list and hashes follow (and "An 8 cm side"), every check passing again. **Print the new
Form A and Form B for Thu 5 Nov.**

## 30 October, late evening — Unit 5's practice page reviewed, fixed and published (test Thu 5 Nov)

Three fresh readers (Claude Fable 5.1) read the page built on 25 Oct — the 25 Oct readers had been cut off by the usage limit.
No wrong key and nothing wrong marked right; nine majors in the shape of the questions and the help, about a dozen minors,
all in **`a7/practice/u5/REVIEW.md`** with what was done about each. The large ones: **question 19 is now typed** (the
faster one's name and the mi/h speed in km/h — as a choice question the vehicle named in the right option gave it away in
nine sets of ten); the rate line of question 15 wraps on a phone; a mixture is the same question in any order of its colors;
part (b)'s Show me how keeps part (a)'s number back until (a) is right, and a fresh "Try another" on 6(b)/16(b) has a walk
of its own (both through the practice kit, Windmill `4d8e093`: the coach gets a context; Try another never repeats an
answer; a box may ask for the phone's decimal keypad); the forms' numbers kept off through every slot (`amount`, `range`,
`tripD`, `speedM`); the sheet's other ratio landing on a whole number is right, not "rounded"; ruling 43's misses added to
the engine and to `verify.py`'s own reader of the lesson specs. Every check passes for the page and the teacher copy
(u5_check on 3,000 sets, verify.py, 41 of 41 planted errors, the lock, the variety floor, the browser checks); content
version 1 (never published before). Published with `publish_web.py --site ../mrshaffer-site u5`; the embed sent to Croix.

## 25 October, evening — Unit 5's practice page built (ruling 55); reviewed and published 30 Oct (above)

Croix, 4:52 pm: *"Yes I still want the interactive practice page on all the units regardless of review day or not."* (ruling
55, HOUSE STYLE 13b(xxvii)). A7 Unit 5 is next after M7 Unit 9: its test is the printed Form A and Form B on Thu 5 Nov, so
the page (`a7/practice/u5`, README) is practice for them — the practice form's nineteen questions, 24 points, in the test's
three sections, new numbers every set, never the forms' numbers (hashes only; `test_forms.js` for the checks) and never a
lesson's (ruling 43), nor a question of the practice test or the review that go home.
- **Its checks:** `u5_check.js` (3,000 sets read back from the printed words with its own reader), `verify.py` (sympy: the
  forms, the practice test and the review read out of `unit.py`, every ratio the FAST sheet's, and **what the lessons showed
  read out of the lesson specs themselves** — not the engine's list, which the M7 Unit 9 review found circular there), 36 of
  36 planted errors caught, the lock, the variety floor (question 3, a value of k alone, allowed at 11 with its reason) and
  the browser checks. The teacher copy prints Form A and Form B.
- **Croix, 7:02 pm:** *"Finish the unit you are working on but don't move on to anew one"* — the pages under way (M7 Unit 9,
  A7 Unit 5) are finished; **M7 Unit 5's page, next in ruling 55's order, waits for his word.**
- **Held for its review:** three fresh readers go over it before it is published (Croix, 24 Oct: "I'd like for a fable chat to
  run over it before it gets pushed"). `hold.json` holds whole units and Unit 5's lessons are live, so the page is held by
  leaving out its two download files — `A7 Unit 5 Practice Test.html` and `teacher/A7 Unit 5 Teacher Copy.html`, the files
  `publish_web.py` copies to the website. When the review is done: fix, `python3 a7/practice/kit/check/run.py u5` and
  `u5/teacher` (they write both files), then publish.
- **Backed up as it stands** (Croix, 7:03 pm: *"Make sure everything is backed up to GitHub so we don't lose anything if we
  run out of usage limit."*). `practice/u5/show_set.js` prints one set's questions with all their help, for reading it.
- **For Croix, about the printed test** (found by the page's lesson check; not changed): Form A question 14's answer is on
  the unit's reference sheet (*20 ft² = 1.86 m²*); Form A question 1 (4 cm → 10 cm) is 5.01 Example 1's second pair of sides
  and Form B question 1 (6 → 9) is 5.01 Notes I's; Form A 6(a) (the 3 in wall at ¼ in : 1 ft) is 5.04 Example 1's; Form A
  question 17 works 5.10 Notes III's 2.5 × 1½ = 3¾.

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

**On the website:** A7 `8ca33dce` published to site `aa603e2` with the Tally sync (174 pages, 1728 links, SITE CHECKS
PASS; deployed, Workers Builds: success). The Google Sites embed, `a7/practice/u6/A7 Unit 6 Practice Test.html` (version
4), went to Croix again: it replaces the one sent at 3 pm.

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
