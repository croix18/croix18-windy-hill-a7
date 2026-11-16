# State of the work — 15 November 2026 (read this first)

## 16 November, morning — scratch paper, the calculators hardened, the docked panels: every practice page and teacher copy re-run (session_01W9n2WyAa6qRsqsdQj871ge)

Croix, 15 Nov, 7:12 pm: *"add a scratch notes to the practice and fast practice as well as a scratch grid."* 7:36 pm: *"Also
get rid of open in new tab for the calculators inside of the practice tests and tests. Harden the calculators to work."*
- **The practice kit is at Windmill `2ff88d0`** (`a7/practice/kit/KIT_VERSION`): scratch paper (`scratch.js`, `scratch.css`:
  one bar button, Notes and Grid for the question on the screen, kept on the device), the calculators hardened (`calc.js`:
  no way out to a new tab, the FAST calculator always in its own layout, focus into it on opening) and the page making
  room for a docked panel (`window.KitDock`). Each has a dated section in the kit's README. No question, key, set lock
  or `contentVersion` moved (Unit 11 stays at 1).
- **Re-run, each ALL CHECKS PASSED, page and teacher copy:** Units 3, 4, 5, 6 and 11; Units 3 to 6 on top of last night's
  Cadence 29.28 banks.
- **On the site:** all five (the site's commit of 16 Nov names this one).
- **For the test that is being built** (Windmill `practice/exam/DESIGN.md`): Unit 11's 14(a) carries three functions
  inside the part (`st.say`, `st.ask`, `st.amt`), so it cannot be kept as text and judged on the site
  (`kit/check/pack.js` will say so). It needs those moved out of the part before Unit 11 can have a test page. Nothing
  about its practice page is wrong.


## 15 November, evening — every practice page and teacher copy re-run on the kit's words pass (the site session)

Croix, 15 Nov, 7:16 pm, to the site session (session_01W9n2WyPU16kWQaNQXN3FUe), after Windmill's practice kit lost the
notes he had been circling on the website (Windmill `HANDOFF.md`, "Words on a page"; `practice/kit/README.md`, "15 Nov
2026 — the words pass"): *"Go through and rebuild and republish everything that needs it."*
- **The practice kit is at Windmill `9f3dc9b`** (`a7/practice/kit/KIT_VERSION`): `cgraph` (a circle graph the student
  builds; nothing of A7's uses it — one more inlined script) and the words pass. What a page says now: nothing in the bar
  before the first check, no "Whole practice test" chip, the end panel headed by its set number with "points" and "time",
  no note about Hint and Try a similar one, no heading over the list after Finish, one short line where the page asks
  before a change. Words only: no question, key, set lock or `contentVersion` moved (Unit 11 stays at 1).
- **Re-run on it, each ending ALL CHECKS PASSED:** Units 3, 4, 5, 6 and 11 — the page and the teacher copy.
- **On the website** in the site commit that follows this one: the ten practice pages and teacher copies only. The
  slides and the units' documents are as they were published at site `e919cfe`; nothing else in this repository changed.
- The site's `tools/test_site.mjs` now fails a practice page or teacher copy built on a kit from before the words pass,
  so a page is re-run on the vendored kit before it is put up.

## 15 November — the kits fixed in Windmill; Unit 11 uses the new pieces; Units 3–6 rebuilt on them; all of it published that evening

Croix, 8:40 am, of the kit limits and open items Unit 11's report listed: *"Fix windmill. Fix the other kits. Fix
everything"*; at 10:16 am he sent the cause of Windmill's failing GitHub check (matplotlib 3.11's glyph tuples). What
was done in Windmill is in its `HANDOFF.md` (the first sections) and in `kit/README.md` and `practice/kit/README.md`
(the 15 Nov sections). In this repository:

- **Published** (Croix, 15 Nov, 6:55 pm: *"Publish it"*): site `e919cfe` (`mrshaffer-site`) — **Unit 11 is on the
  website** (its seven days of slides, the practice page, the teacher copy and the unit's documents; `/a7/unit-11/`),
  and Units 3–6 are there as rebuilt. `publish_web.py`, then the site's `schedule.py`, `build.mjs` and `test_site.mjs`:
  SITE CHECKS PASS (218 pages, 2619 links); Cloudflare's build of that commit succeeded. Unit 11's practice page is
  live at `contentVersion` 1, so from here its sets are fixed like every published page's: a change that moves a set
  is a new content version.
- **The build kit is at Windmill `095d912`** (`a7/build/KIT_VERSION`). New in a spec (`a7/build/SPEC SCHEMA.md`): `fig`
  on a Your Turn (`fig_a` for its answer slide), on a worked slide, a warm-up question and a set question; `fig_key` on
  a paper question (the key's own figure); a step that opens `[equation]` or `[false]`; `align="="` at a lesson's top
  level (rows that solve an equation are set with their equals signs in one column). Changed without asking: every
  figure is trimmed to its ink; a choice board's options stand beside its figure when that makes the figure taller;
  each unit's own `figs.py` is loaded for that unit (`lib/unitload.py`; `tools/master_sheet.py` and
  `check_master_sheet.py` use it); the Teacher Edition says "neighbor"; no student paper prints the follow-through
  line; **a build stops on any matplotlib but 3.10** (`lib/mathimg.MATPLOTLIB` — 3.11 draws stacked fractions a
  quarter taller and several decks no longer fit; moving to it is its own job).
- **Unit 11 uses the new pieces** (rebuilt and installed, `checks: 0 findings`):
  - the graph days' Your Turns (11.05, 11.07, 11.08) show their tables and grid, and their answer slides the graph;
    every graph Example's worked slide carries the finished graph;
  - the key of every "graph both lines" question draws both lines and marks the crossing (`fig_key`: the sets, banks
    and additional banks of 11.07 and 11.08, and the Review);
  - the multiple-choice graph boards are back, the graph beside the options at 2.65–3.16 in (11.05 board 6; 11.07
    boards 4 and 6; 11.08 board 4); 11.07 board 2 and 11.08 board 2 are free response;
  - a no-solution ending is the false equation and its words on answer slides too (`[false]`), and worded lines that
    hid an equation are `[equation]` lines the build solves (11.02 boards 6–7; 11.03 Example 2's Your Turn and boards
    2, 6, 7, 8; 11.04 Example 2's Your Turn and board 7). The kit holds a `[false]` line to be false and its equation
    to have no solution; that it follows from the line before was checked by hand;
  - `align="="` in all seven lessons (48 runs of rows lined up). An answer slide's labelled steps ("Add 9: 3x = 24")
    are not lined up: the kit aligns rows that are one relation each;
  - START HERE's dates are right (11.02 Tue 1 Dec, 11.03 Wed 2 Dec);
  - 11.07 board 6 says "Four points on the lines are marked." (the crossing is one of them, so "each line passes
    through two marked points" was not what the picture showed); 11.08 board 4's stem ends "Best estimate?" because
    the full sentence does not fit on one line and a second line drops the graph under the options.
- **Unit 11's practice page** (`a7/practice/u11`) has the kit's several boxes: questions 12 and
  13(b) take `x =` and `y =`; 14(a) "after ▢ weeks" and the amount; 14(b) `x ≈` and `y ≈`, each within 0.1. A part is
  still one point, and the key and the all-multiple-choice paper show the whole pair. 63 of 63 planted errors. Today's
  lesson changes moved three sets (9, 154, 174) under ruling 43 and the sets were locked again — allowed only because
  the page had not yet been published (`contentVersion` 1). The printed test's directions are the two sentences of every
  teacher copy; the unit's own note about writing a point is gone. Page and teacher copy: ALL CHECKS PASSED on the
  practice kit at Windmill `bf7af44`, the lock unchanged across the last runs. Three lines on the page that explain the
  screen were left for Croix's word (Windmill `HANDOFF.md`, "Words on a page"): "Each to the nearest tenth" over
  14(b)'s boxes; Hint 3's "Type 3 in the x box and 2 in the y box." and the walkthrough's "That goes in the x box.";
  the coach's "Open Hint, then tap Step by step with me."
- **The practice kit is at Windmill `bf7af44`** (`a7/practice/kit/KIT_VERSION`): a part may have several labelled boxes
  (`view.boxes`), a walkthrough's options are shuffled by the question, the kit writes a dot and never × (Units 3–6
  keep the × their checks hold: `LEGACY_TIMES`), and on a phone a box with a unit takes its own row. Units 3–6's pages
  were run on the kit one commit earlier, which differs only in the boxes' phone layout (they have no boxes), so their
  `CHECKED` stamps are one kit behind: `run.py` before the next build of one, as after any vendoring.
- **Units 3, 4, 5 and 6 are rebuilt and installed on this kit**, each at `checks: 0 findings`; no question, answer or
  number changed. Page counts that moved: Unit 6 — 6.07's set key 2→1; Unit 5 — the Practice Test 6→5; Unit 4 — Forms A
  and B 8→7 each. **Unit 3 changed most.** It was last built on the morning of 25 Oct, before the kit printed a
  Vocabulary slide and before its present type sizes: each deck gains a Vocabulary slide (All Slides 344→355), nine
  Teacher Editions run 3→4 pages, an All in One folder is new, and the mathematics on 59 slides is set at the size
  every later unit has had (two thirds to nine tenths of its old height — 3.06 built on the kit this repository carried
  from 25 Oct to this morning comes out the same as today's, so it is not today's change). Two plans no longer fit
  with the Vocabulary minute and gave it one of their own: 3.01 Notes I 3→2 min, 3.06 Notes III 4→3 min.
- **Units 3–6's practice pages and teacher copies** were run again on the practice kit as fixed this morning: every
  one ends ALL CHECKS PASSED and no set lock moved.
- The master sheet is regenerated (0 problems) and `tools/check.sh` passes.

### Open, for Croix
1. *(closed: everything above was published on 15 Nov.)*
2. **Three IXL skills of the plan may ask for what Unit 11 does not teach yet** — TS7 "Write a system of equations given
   a graph", 9Z8 "Solve a system of equations in slope-intercept form", AGZ "Find the number of solutions to a system of
   equations by graphing" — read from their titles; nobody here could open IXL. If they need slope, they move to Unit 10.
3. **`drive/WindyHill.gs` in Windmill is version 3.1** (an unfinished pull is finished on the next run): paste it over
   version 3 in the Drive script editor.
4. **Not done, on purpose:** a 43-minute Lesson Plan (HOUSE STYLE has no Wednesday plan; the lessons' materials line
   says what to cut); the move to matplotlib 3.11.

## 14 November — A7 Unit 11, Solving Equations and Systems: built, reviewed, fixed; held for Croix's word (published 15 Nov, above)

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

### Open, for Croix (14 Nov)
All eight items of this list were closed on 15 Nov except the IXL question, which is item 2 of the list above.

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
