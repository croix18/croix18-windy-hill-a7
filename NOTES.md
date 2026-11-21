# State of the work — 15 November 2026 (read this first)

## 20–21 November — the lean workflow; Unit 7 built with it, on a branch, held for Croix's word (session_01W9n2X1V97j7Nf5Y7z1DaCq)

Croix, 20 Nov, of how the lesson slides are built: *"It feels extremely inefficient and is burning tons of tokens."* Shown a
plan, 11:30 pm: *"You can get rid of the 4 page teacher edition. Only read math nation for scope and test item shapes. The
reviewers yeah opus then fable. Let's do it. Run the next unit to test."*

**Everything below is on the branch `claude/lean-workflow`** (this repository and Windmill). `main` is untouched, nothing is
on the website, and M7 has not been moved to the new kit.

- **The procedure** is Windmill's `briefs/LEAN WORKFLOW.md`, with the briefs it ran on in `briefs/lean/`: the test settled
  first and the plan reviewed before any spec; builders who read a 12 KB card (`BUILDER CARD.md`), not the history; one
  builder to a lesson, each in its own copy; reviewers who read the unit as text and its figures on sheets, not slides; one
  blind solve in place of three recomputations; one fix pass, then only what changed checked again. Builders, solvers,
  readers and fixers are Claude Opus 5.5; the lead plans, rules and looks.
- **No Teacher Edition** from here on: `TEACHER_EDITION = False` in `a7/build/course.py`. The Lesson Plan stays. Units 3–6
  and 11 keep the editions they were built with until they are rebuilt.
- **Every document in Lexend** (Croix, 21 Nov, 11:08 am, of the Review in Times beside the Practice Test in Lexend in one
  PDF: *"why does the font switch? It should be the lexend font throughout every document."*). Ruling 46 had set the
  assessment papers alone; `DOC_FONT = "Lexend"` in `a7/build/course.py` (the kit's new profile name) sets every document:
  the lesson's pages and keys, the Lesson Plan, the Review, the Reference Sheet, mathematics and figure lettering included.
  Unit 7 is rebuilt and installed so. Lexend is a wider face: each Lesson Plan runs five pages, not four. Units 3–6 and 11
  keep Times in those documents until they are rebuilt.
- **A bare dollar sign** — found by the Lexend build. Three boards of 7.07 wrote their money in `qtext` as `$7.00`, not
  `\$7.00`, so the Lesson Plan drew "7.00 and 4 pounds cost" as mathematics between two dollar signs; in Times the picture
  fitted its cell and nothing refused it. Fixed, and the kit's `rulingcheck` now refuses it (no other unit has one).
- **Math Nation** is read for a unit's scope and its test's item shapes, in one note that stays out of the repository. There
  is no Unit 7 audit and there will not be one.
- **The kit** (Windmill `ac81351`, vendored): the five lean tools (`reader_copy.py`, `student_view.py`, `blind_diff.py`,
  `unit_repeats.py`, `changed_slides.py`), `BUILDER CARD.md`, `RULINGS LEDGER.md`; a one-point section prints "1 point"; a
  paper's title keeps clear of the name lines.
- **Unit 7, Representing Proportional Relationships** (MA.7.AR.4.1–4.5, MA.8.AR.3.1; taught Wed 6 – Tue 12 Jan, spiral day
  13 Jan, test Thu 14 Jan): five decks (7.01, 7.02–03, 7.04, 7.05–06, 7.07), each with its Lesson Plan, Independent Set and
  two Question Banks; the Practice Test (15 questions, 20 points — the blueprint of the test), the Review (17 questions) and
  the Reference Sheet. `gates` 0 (282 items re-derived), `unit_repeats.py u7` 0, `checks: 0 findings`, installed.
  7.05–06's deck is titled "Writing Equations; Translating Representations" (the calendar's longer name made a
  key's path in the package 184 characters; the install's limit is 180).
  The plan and what was built differently: `a7/reference/A7 Unit 7 … - Lesson Outlines.md` ("As built" at its foot). Every
  review ruling in exact words: `a7/reference/A7 Unit 7 … - Review Rulings.md`.
- **How it was proved:** the plan read by two readers before any spec (41 findings, 3 blockers — a line each to fix); the
  built unit solved blind, 269 questions, no wrong key; read by three readers (1 blocker, 13 majors, 21 minors); the lead
  ruled, six fixers applied it; the 82 questions that changed solved blind again, no key differs; the lead looked at every
  changed slide and a sheet of each whole deck.

### Open, for Croix (21 Nov)

- **His revision guide** (21 Nov, 11:06 am — a slide-by-slide list of wording changes for Unit 7). Checked against the built
  unit and answered the same morning. Right, and to apply on his go: "in every row" where the tables' pairs are columns
  (7.02, 7.04, 7.05, Practice Test question 8, the Reference Sheet) — "for every pair", "column"; "the other way round" —
  "around"; "can be the subject" — "can be isolated"; "against" — "versus" (Units 3–6 and 11 say "against" too); sentences
  that begin with a lowercase letter; fragments ("When equal?"); "say" — "explain"; two dashes in an answer line. Wrong, and
  not to apply: its y = kx (Florida writes y = px), its "math error" on slide 73 (the slide reads y = 3x), its k = 0.625d,
  its × sign. His to decide: "versus" or another word, and the kit-wide lines ("Answer it.", "Write your answer in
  sentences.", the two IXL lines, the cover line). The pass must cover the papers, the sets and the banks, not the slides
  alone.
- **ChatGPT's language audit** of the All Slides PDF (21 Nov, 11:43 am — "Here's what chat said."). Answered at midday. It
  lands where the guide and the lead did on "versus", "1 unit of x", "explain" for "say", whole questions for fragments,
  "Let e represent…", the definition, "Answer it." (it says delete; the guide allows delete) and the IXL lines. To take
  from it as well: answer captions as short whole sentences where the cap allows; headings as plain questions ("I. What
  makes a relationship proportional?"); two sentences where a stem joins two with a colon. Not to take: it keeps "every
  row" (the pairs are columns); it removes the snail's age, the 180 passengers, the 40 seats and the 50 pages (ruling 22,
  one board a lesson carries a number the question does not need — and it says itself "unless intentionally testing");
  "Independent Set" renamed "Independent Practice" (the name is in every file name, the site, the master sheet and six
  taught units — the lead would keep it; his call); serial commas in a target that quotes its benchmark; "at each labeled
  mark" (wrong where labels skip gridlines); "initial value of 0" ("the starting amount is 0"); any rewrite longer than
  its slide's cap (the fix is taken in fewer words).
- **The pass, as the lead would run it on his go** — defaults given to him at midday, his to change: "Answer it." deleted;
  "Write your answer in complete sentences."; the IXL slide "Open IXL and work on the skills listed below." / "Show your
  work on paper. IXL's answer box does not record it." / "Complete every listed skill to a SmartScore of at least N" and
  the due line / "Required IXL skills"; the cover line "select a lesson on the next slide to jump to it"; "versus", the
  y-quantity first; "for every 1 unit of x", and the story's own units in a story ("costs the same amount per pound");
  the definition "one quantity is always a constant multiple of the other: y = px" (7.01, 7.04 word for word, the
  Reference Sheet twice); "Independent Set" and the ruling-22 numbers kept. The four kit-wide lines change every unit of
  both courses at its next rebuild. Cheapest sound way: the lead writes each old-to-new string, a script applies them and
  refuses a string that is not found exactly once, the gates catch a line over its cap, one Opus solver re-solves the
  reworded questions blind, and the lead looks at every changed slide and page.
- **Found reading the Lexend pages, for the same pass:** the Review's section line "Lesson 7.04 · 1 questions" (kit,
  `unitbuild.py`: "1 question"); the Reference Sheet's sections 1 and 3, where the note beside the title is too long for
  the line in Lexend and wraps ("… times the / other", "… for each / 1 of x"); 7.07's Lesson Plan prints "Vocabulary."
  with nothing after it (kit, `plankit.py`: say "No new terms.").

- **Merge and publish:** say the word and the branch goes to `main` and Unit 7 onto the site. The site has not yet shown a
  unit with no Teacher Edition: `publish_web.py` publishes what a package holds, and that wants one look on the site.
- **The practice page** for Unit 7 is not built (the test is a random set of it). Question 1(b) needs a part where a student
  plots points, and 8(b) takes a row and a cost, or "none".
- **M7** builds its next unit (11, from 11 Feb) the same way once it vendors this kit.
- Unit 11's notes on 11.04 and 11.07 still call Thu 3 and Tue 8 Dec no-class days (ruling 57, below): unchanged here.

## 18 November, night — ruling 57: the PM2 days are class days; A7 keeps every date (session_01W9n2X1DGdhkjT92EJfNN3K)

Croix (re-laying M7 around Thanksgiving): *"There's still class on pm days just condensed."* For A7 he chose **"Spiral days,
nothing moves"**: Thu 3 Dec (ELA PM2) and Tue 8 Dec (math PM2) are `review` lines in the as-run log now ("FAST PM2 … — short
periods; spiral review"), not `off`. Unit 11 (11.01 Mon 30 Nov … 11.08 Thu 10 Dec, test Fri 11 Dec), the semester review
(14–16 Dec) and the catch-up days (17–18 Dec) are unchanged, and so is the Unit 11 build. `tools/master_sheet.py` finds the PM2
row from either kind of day. Ruling 57 in HOUSE STYLE (M7's half — Unit 10 tested 1–2 Dec, Unit 13 15–16 Dec — in M7's).
**For the Unit 11 build:** `u11/l04.py` and `u11/l07.py` still say Thu 3 and Tue 8 Dec have no class (the TE notes on
11.04 and 11.07). The days are spiral days now, so the warm-ups stand (the lesson before 11.04 is still 11.03, and the one
before 11.07 is still 11.05–06); only those words need changing, and they were left to the build chat so its work in progress
is not touched.

## 16 November, night — lesson tests: every teacher copy re-run, each unit's test rebuilt; no practice page changed (session_01W9n2WyAa6qRsqsdQj871ge)

Croix, 16 Nov, 8:12 pm: *"Once that's completely done, I want you to apply that across all of the practice tests, so I can
test on a specific unit or lesson to test on."* Asked how large a lesson's test should be: *"8, like a practice set."*
- **The practice kit is at Windmill `f322aa1`** (`a7/practice/kit/KIT_VERSION`; kit version `3f3540b015d8`). New, in a teacher
  copy and the test page only: a **lesson test** is the same locked test (the site's Test card, the start code, the one test
  page, judged and sealed by the site, the code, Tally, See the test) on one lesson's 8 bank questions: 6 regular and 2 high
  rigor (8 regular where a lesson has none), a pure function of the unit, the lesson and a 128-bit seed. `exam_lesson.js`
  (teacher copies only) draws them for the cockpit; the test page shows them from the site's answer and holds nothing of the
  bank; the unit's bundle judges them (`UL`, bank.js's judging as a module, no bank data) and lists the unit's lessons for the
  card. A unit test is untouched (Windmill `practice/exam/DESIGN.md`, "6. Lesson tests").
- **Not secret:** a lesson's bank is about 60 fixed questions students also practice on. A lesson test is a check on a lesson,
  not a sealed test with new numbers as the unit's is.
- **No practice page changed.** Every unit's page was rebuilt with plain `build.py` (its `CHECKED` stamp taken) to the same
  bytes. No question, key, set lock or `contentVersion` moved.
- **Re-run, each ALL CHECKS PASSED:** the teacher copies of Units 3, 4, 5, 6 and 11.
- **Each unit's test rebuilt and checked** (each TEST BUILT AND CHECKED; for a unit with a bank that is every lesson choice:
  three tests drawn, proved in the page and by the bundle under Node, the test page's cards held to the teacher copy's, a whole
  lesson test through the stand-in site, See the test for a lesson): Units 3, 4, 5 and 6 have lessons (12, 7, 14 and 12
  choices); Unit 11 has no bank and keeps the unit test only.
- **On the site:** all five (the site's commit of this night names this one).


## 16 November, evening — See the test: every teacher copy re-run, each unit's test rebuilt; no practice page changed (session_01W9n2WyAa6qRsqsdQj871ge)

Croix, 16 Nov, 6:34 pm, after his first dummy run of a test on the site (this course's Unit 6, on his tablet, opened in
Tally): *"That's really excellent! I did a dummy run. It seems to work really well. Is there any way to have it be able to
show me the exact questions as well?"*
- **The practice kit is at Windmill `41c736e`** (`a7/practice/kit/KIT_VERSION`; kit version `2e2c5655dbf6`). One thing is new,
  in a teacher copy only: `exam_show.js` with `exam_show.css`. Opened at `…/practice/#test=<payload>` (Tally's "See the
  test" link), the teacher copy redraws that student's test from the record's seed, proves it is the same test (the same
  parts in the same order, every key equal) and shows each question as the page drew it, with what the student answered,
  the verdict and the key. A unit changed since the test shows one line and no question. The payload holds no name and is
  never sent to the site (Windmill `practice/exam/DESIGN.md`, "See the test").
- **This course found the kit's one slip.** Unit 6's figures carry the class `q` (`svg.fig.q`), and the first build of the
  view gave them a question card's padding and rule line; its own check failed on Unit 6's teacher run ("19 of 14"). Fixed
  in `41c736e` (the sheet's rules are for `.q[data-q]` only, and the check fails if anything else inside a card takes the
  card's rule); the check then passed on every teacher copy of both courses before the full runs.
- **No practice page changed.** The new files are built into, and hashed for, a teacher copy only; every unit's page was
  rebuilt with plain `build.py` (its `CHECKED` stamp taken) to the same bytes. No question, key, set lock or
  `contentVersion` moved.
- **Re-run, each ALL CHECKS PASSED (the new check, `check/exam_show_page.js`, among them):** the teacher copies of Units
  3, 4, 5, 6 and 11.
- **Each unit's test rebuilt and checked** (each TEST BUILT AND CHECKED), so a unit's teacher copy, test page and site
  bundle carry one kit version: Units 3, 4, 5, 6 and 11.
- **On the site:** all five (the site's commit of this evening names this one).


## 16 November, afternoon — the kit with the test: every page and teacher copy re-run, each unit's test built; Unit 11's story part made storable (session_01W9n2WyAa6qRsqsdQj871ge)

Croix, 15 Nov, 7:52 pm, of a test taken on the website and judged there: *"I'm fully on board with a bigger build. Make it
airtight."* The design, the reviews and what was changed after them are in Windmill (`practice/exam/DESIGN.md`,
`practice/exam/review-16nov/`).
- **The practice kit is at Windmill `86dfa38`** (`a7/practice/kit/KIT_VERSION`). For a practice page two things changed:
  the page judges through `judge.js` (the judging moved, unchanged, into one module the site also calls — 16,800 parts
  judged before and after, no verdict different), and `exam_link.js` shows a third choice, **Test**, on the start screen
  while the site says the unit's test is open (on mrshaffer.org only). A teacher copy also carries `exam_pool.js`: asked
  by the cockpit at `#exam-pool`, it draws the tests the site hands out. No question, key, set lock or `contentVersion`
  moved.
- **Unit 11's story question (14a) holds data only now.** Its part carried three functions (`st.say`, `st.ask`, `st.amt`),
  so it could not be kept as text and judged on the site. `engine.js` gives the part the story's data (`id`, `unit`,
  `xname`, `yname`, `each`, `up`) and `coach.js` and `help.js` say an amount from the part's own `unit`. Compared before
  and after on 300 sets (600 parts: the stem, the key, the solution, the walkthrough, three judgments): identical.
  `kit/check/pack.js` passes: 1,080 parts over 60 sets, every part judged the same after `unpack(pack())`.
- **Re-run, each ALL CHECKS PASSED, page and teacher copy:** Units 3, 4, 5, 6 and 11. The pages were run on the kit at
  `4f19284` and rebuilt byte for byte on `86dfa38` (nothing a page is built from changed between them; `build.py` takes
  the stamp); the teacher copies were run on `86dfa38`.
- **Each unit's test built and checked** (`kit/exam/build_exam.py`, each TEST BUILT AND CHECKED): `A7 Unit N Test.html`
  (the test page: no engine, no key) and `test_bundle/` (what the site judges with), for Units 3, 4, 5, 6 and 11. A unit's
  teacher copy and its bundle carry the same kit version; they are published together.
- **On the site:** the site's commit of this day names this one.


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
