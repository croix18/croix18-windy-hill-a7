# State of the work — 15 November 2026 (read this first)

## 27 November, afternoon — Unit 11 built an eighth time, on the kit of 27 Nov, and published (session_01W9n2X1V97j7Nf5Y7z1DaCq)

Croix, 27 Nov, 2:12 pm, of Unit 11: *"Rebuild, check, then publish"*. The unit is built on Windmill `5fbd8c1`, which
adds three changes made while Unit 10 was built: a printed title too long for its line breaks where its two lines are
most even and never after a joining word, and breaks at a semicolon when both lines fit (`877c70e`, `5fbd8c1`); and on
the web deck an option keeps the space before its mathematics (`70c8ea2`). **What changed against the seventh build:**
the handout titles of 11.01, 11.02, 11.03 and 11.08 ("Equations with Variables / on Both Sides" was "Equations with
Variables on Both / Sides"), in their seven printed documents each and the three combined PDFs; nothing else in any
PDF's text, and no page count. Gates 0, `unit_repeats.py` 0, `checks: 0 findings` from an emptied `out/u11`, the
package reinstalled (128 files), the master sheet regenerated and checked, `tools/check.sh` all passed.

**Published, 27 Nov.** `main` is `claude/u11-terms` here (`1093bb3`) and `claude/a7-u10` in Windmill (`5fbd8c1`, which
holds Unit 10's notes and tools but changes no course on its own). The site is `3ecc91f`: only Unit 11's files changed
(the package, the student files, the seven web decks); `SITE CHECKS PASS` (263 pages, 3183 links); Cloudflare's build
of that commit succeeded; the live unit page lists all seven lessons with their slides and sets, the practice test and
the review, and the live 11.02 Independent Set reads "Equations with Variables / on Both Sides". Before publishing, the
three decks whose options carry mathematics (11.01–11.03) were looked at on a scratch copy of the site: each option
keeps its space ("one solution, x = 0"). Unit 10 is not on `main` or the site.
## 27 November, afternoon — Unit 10 (Linear Relationships) built with the lean workflow, merged and published (session_01W9n2X1V97j7Nf5Y7z1DaCq)

Croix, 27 Nov, 7:20 am: *"Can you move on to the next unit"*; 3:02 pm, after the review copies: *"Publish 10"*.
**Published, 27 Nov:** `main` is the branch `claude/a7-u10` (`8157017`, fast-forwarded; Unit 11's publication is
merged into it); the site is `945bdaf` — the unit page `mrshaffer.org/a7/unit-10/`, the eight days' slides at
`/a7/slides/10.01/` … `/a7/slides/10.10/`, the calendar's eight days linked (Jan 15 – Jan 28), the package on the
teacher page; `SITE CHECKS PASS` (280 pages, 3403 links); Cloudflare's build succeeded; the live unit page lists the
eight lessons with their slides and sets, the Review, the Practice Test on paper and the Reference Sheet, and the live
10.02 Independent Set reads "Slope from Graphs, / Tables and Two Points". Like Unit 7, it has no practice page.
The unit was built on the branch `claude/a7-u10`, on Windmill's kit `70c8ea2`. Eight decks, Fri 15 Jan – Wed 27 Jan
2027 (10.04 and 10.10 are 43-minute days); the test Thu 28 Jan. The plan is `a7/reference/A7 Unit 10 Linear
Relationships - Lesson Outlines.md` (its "As built" says where the unit now differs from it); the review and every
ruling are in `… - Review Rulings.md`.

- **The workflow, second run** (Windmill `briefs/LEAN WORKFLOW.md`): scope from Math Nation (never in a repository),
  the plan with the test settled first, two plan readers (Barton, FAST), the figure module `u10/figs10.py`, eight lesson
  builders and a papers builder in their own copies, integration, a review wave (six blind solvers, three readers),
  rulings, nine fixers, and a fresh blind solver of everything that changed. **No key was wrong** in 413 questions.
- **What the review changed:** one way of saying each idea across the unit ("The rate is the slope, and the start is
  the y-intercept"; "Go back to x = 0 at the rate of change"; "the coefficient of x"); a question in a bold line on
  every board and Example; pictures large enough to read (every slide picture measured on the built deck); 10.04's
  board 4, 10.06's board 3, 10.10's boards 1–2 and several bank questions rewritten; six of the Review's questions
  sharpened (6b, 10, 11, 12a, 16c, 17). **The kit:** a printed title too long for its line breaks where its two
  lines are most even (`877c70e`); on the web deck an option keeps the space before its mathematics (`70c8ea2`).
- **What it taught** (Windmill `HANDOFF.md`, 27 Nov): measure pictures on the built pages, not the spec — the kit sets
  a Your Turn's bold line over its picture, so a Your Turn whose picture is a graph keeps its question in one line; the
  repeat gate needed 45 `repeat_ok` comments in a unit of small coordinates (each names its digits); the nine fixers
  were stopped once with the server and resumed from their saved transcripts.
- **Proof.** Gates 0 (429 items re-derived), `unit_repeats.py` 0, a clean `build_all.py u10` at `checks: 0 findings`,
  279 pictures drawn at every size, 91 changed questions solved blind with no key differing, the eight web decks read
  on a scratch copy of the site (273 slides, no page error; the three faults found there are fixed). The package
  is installed and the master sheet regenerated.
- **His calls, still open:** the five test-blueprint questions sent on 27 Nov (two drawn graphs on the test; the
  temperature formula printed; no line of fit on this test; standard form in 10.06 for IXL 7MZ; naming days); IXL N7D
  on 10.05. (Unit 11 was published the same afternoon, above.)

## 27 November — Unit 11 looked at as it will stand on the website; three kit fixes; still NOT merged, NOT published (session_01W9n2X1V97j7Nf5Y7z1DaCq)

Croix, 27 Nov, 7:20 am: *"Can you move on to the next unit"* — Unit 10 (above; branch `claude/a7-u10`).
Unit 11 still waits for his word; he was told so that morning. So that publishing takes minutes when he gives it, the
rebuilt unit was published into a scratch copy of the site and its seven web decks were read slide by slide (246
slides, the second renderer). Three faults, all the kit's, all fixed in Windmill (`b211635`, `d70dceb`, `72a02f6`):

- **The web deck's Vocabulary slide set its mathematics at twice the size of its words** ("3x and 5x" at 32 pt in a 16-pt
  definition). The PowerPoint has scaled an expression inside a sentence to its words since 18 Oct; the page had not.
  `htmlkit.inline_pt` is the same rule. This is on the published web decks of Units 3–7 too until each is republished.
- **A long warm-up question's second line began under its number on the web deck**, and a long answer broke inside itself
  ("Infinitely many / solutions"). The number stands in a box of its own now; an answer moves down whole.
- **11.07's Independent Set slide ended question 2 on a lone "0."** in the PowerPoint — the last piece was a picture, so
  the scan for short last lines could not see it — and the web deck broke "y = −5 + / 2x" inside the expression and showed
  the printed page's blank grids as thumbnails. `deckkit._flow_lines` does not leave a last line under ten characters;
  on the page an expression is one piece and page-lettered figures stay off the slide, as in the PowerPoint.

**Proof.** Kit tests 310 of 310 and 309 of 309, tools 53 of 53. Unit 11 built a seventh time from an emptied `out/u11`:
`checks: 0 findings`; of 66 PDFs, two differ in text from the sixth build (11.07's Slides and the unit's All Slides) and
none in page count; `changed_slides.py`: one slide changed in the unit, 11.07's Independent Set. The package is
reinstalled (128 files). The scratch site builds and ends `SITE CHECKS PASS`; no page error in any of the seven decks.

## 22 November, evening — Unit 11 rebuilt on today's kit, with "isolate" and "solve for" (branch `claude/u11-terms`; NOT merged, NOT published) (session_01W9n2X1V97j7Nf5Y7z1DaCq)

Croix, 22 Nov, 3:50 pm: *"Merge and publish. Then take a wack at 11 with these changes."* The first half is the section
below. **The reading taken of "these changes":** everything Unit 7 was given in its four passes. Unit 11 (built 14 Nov on
the old kit, taught Mon 30 Nov – Thu 10 Dec, test Fri 11 Dec) is rebuilt on the kit of 22 Nov, ruling 60's two words are
put where the unit names those ideas, the card's rules 19 and 20 are applied to the unit's own text, and ruling 57's
words are corrected. **It is on a branch**: `main` and the website still hold the build of 14 Nov, and merging and
republishing wait for his word (nothing on `main` or the site moves without it; his word of 3:50 pm named Unit 7).

- **What the kit changes at a rebuild:** no Teacher Edition (seven files gone; the package has none); every document in
  Lexend (the Lesson Plans run five pages, 11.03's six; eleven keys run a page longer; **no student paper changed its page
  count**); "Answer it." gone from under every whiteboard question; the IXL slide's and the Lesson Plan's standing lines;
  the Independent Set's opening line; the paper typesetting of the third pass.
- **Five figures were refused in Lexend lettering** (a wider face: a label ran through a line or an axis name): 11.07's
  bank label "(1, 4)", two key labels "(4, 1)" and "(4, 0)", 11.08's key label "about (1.7, −0.3)", and the Review's
  matching grid, whose "infinitely many" met a rule. Each label was moved or the grid re-proportioned; nothing else in
  those figures changed.
- **Ruling 60.** *"Solve for x"*, in each item's own letter, is the instruction: "Solve for x, then check." (the Examples
  and Your Turns of 11.01, 11.02 and 11.04), "Solve for h:  9h − 2h + 4 = 60" (25 warm-up, set and bank stems that said
  "Solve:"), "Solve 1.5(4x − 2) + x = 2(x + 6) for x.", "Solve for x both ways.", the Review's "Solve for the variable."
  and "Solve each equation for x.", the banks' "…the equation has fractions. Solve for the variable." *"Isolate"*: 11.01
  Notes I is "Collect the like terms. Then isolate x in two steps."; the Reference Sheet's fourth step is "Isolate x."
  (its worked table ends "divide both sides by 3: x is isolated") and its vocabulary has "isolate; solve for"; the
  Lesson Plans' MTR lines, ELL lines ("Isolate: get the variable alone on one side of the equals sign. Solve for x:
  isolate x.") and cause notes ("[Notes I: to isolate x, subtract 4 from both sides]", which read "undo + 4 by
  subtracting 4"). "Every system is given solved for y" was already the unit's phrase. The operation labels on the
  answer slides stay ("Take 5x from both sides:", "Add 9:", "Divide by 3:").
- **Card 19 on the student pages.** Whole questions for fragments: 11.03's question line is "How many solutions does it
  have? If it has one, find it." (it read "One solution, no solution or infinitely many? If one, find it."); "How many
  solutions are there?"; "Which estimate is best?"; 11.08's stories are sentences ("Tank A holds 30 liters and gains 5
  liters a minute.", "Plan A costs \$6 for shoes and \$3 a game.", "Gym A costs \$20 to join…"); "For y = 2x + 1, find y
  when x = 3." A paper's sentence does not open with an equation or a pair ("The solution of 3(x + □) + 2x = 46 is
  x = 8.", "The ordered pair (3, □) is a solution of the system…", "The system y = 3x − 3 and y = −x + 5 is
  graphed."). "Work backwards." heads no group now: "Find the missing number." Answer lines: "Yes, because 3(2) + 1 =
  7", "No, because 3(2) − 2 = 4, not 5.", "One solution, x = 0", "Never. There is no solution.", "No solution. The lines
  are parallel.", "Shop A (\$33 versus \$42)" (it read "against"). Students "explain" or "write", never "say" (11.08's
  target and Notes II, a bank heading, the Review's question 7, the Reference Sheet); "a horizontal line" for "a level
  line"; "the crossing's x-value" for "the x of the crossing". The Reference Sheet's prose is rewritten in whole
  sentences throughout. **The Practice Test's stems are untouched** (they are the state's item shapes, and the practice
  page words its questions the same way); one of its key lines changed ("One solution, x = 0").
- **Card 20 in the seven Lesson Plans.** "Required by the benchmark", "Not part of this lesson", the three MTR lines,
  Building on, Working toward, Differentiation, Closure and Materials are whole sentences that say "whiteboard question
  9", not "board 9"; no ruling number, audit code or word about the build is printed ("(audit D4)", "(audit E15)",
  "[ruling 22]", "THE 43-MINUTE CUT (… the build cannot print a 43-minute one)" are gone: the two Wednesdays' cuts are
  sentences under Materials, as 7.01's is); the wrong answer that uses the unneeded number is cited "[an extra number,
  included on purpose]". "Grade 7 (MA.7.AR.4.3) — graphing y = px from a table" is out of 11.05's and 11.07's Building
  on: Unit 7 is taught after Unit 11.
- **Ruling 57's words:** `u11/l04.py`, `u11/l07.py` and the manifest said Thu 3 Dec and Tue 8 Dec have no class; they
  are spiral days with no deck. No date moved.
- **A wrong premise, found while rewording:** 11.01's first higher-order question asked why the 4 in 3(2x − 5) + 4 = 25
  cannot be subtracted from the 25 before the 3 is distributed. It can. It reads: "…the 4 can be subtracted from both
  sides before the 3 is distributed. Why can the 4 not be added to the −5 first?"
- **Found by building and by looking, and mended:** (1) **□, ⅓ and ⅔ are not Lexend glyphs**: 16 `glyph` findings in
  plans and keys. A third is written "(1/3)". A box in a key's worked line or a plan's cause note is in words ("Put 4
  in for x: 5 times the parentheses, minus 8, is 37. The parentheses are 9, so the box is 5."): written as mathematics
  it is a picture, and it stood half again as tall as the small words beside it (the fourth build; the fifth has the
  words). In a sentence of the body's size it stays mathematics (the Lesson Plans' Enrichment lines). (2) **The IXL slide's third line** left "test." alone on a second line on all seven IXL slides,
  because "Unit 11" is a character longer than "Unit 7": a kit line, mended in the kit (Windmill `1b560a0`: the due
  sentence wraps whole). (3) **A second row of words over a graph is paid for out of the graph**: 11.08's whiteboard
  question 4 came out with a graph a quarter of an inch tall, and 11.05's second Your Turn and question 7 a quarter
  smaller; each is one line again. (4) A line the kit measured as two (its 6% margin) left a blank line and a smaller
  figure (11.08's first Your Turn and question 5): shortened. (5) One-word last lines on four slides: reworded. (6)
  11.07's Additional Question Bank ran 8 pages for 6: two of its figures are 0.2 and 0.3 in smaller.
- **Croix, 6:24 pm, reading the review copy:** *"Similar triangles. Find x. What the heck does that mean"*. It is
  11.01's second warm-up question, "Similar triangles: 6/9 = x/12. Find x." **The pass had not read the unit's 28
  warm-up questions against rule 19**; it rewrote the boards, sets, banks and papers. Five were a label and its data.
  **Why they were written so:** the kit made a warm-up question fit one line at 23 pt, about 65 characters, and a whole
  sentence about remote interior angles is longer. The kit sets a long warm-up question on two lines now (Windmill
  `3192c1c`, `deckkit.stem_rows`: broken after a sentence; a question that fits one line is drawn as it was, and Unit 7
  test-builds unchanged). Rewritten: 11.01 questions 2 and 3 ("The sides of two similar triangles give 6/9 = x/12.
  Solve for x."; "A map's scale is 1 cm : 20 km. What distance does 3 cm on the map represent?"), 11.02 questions 2
  and 3 ("The two remote interior angles of a triangle are 50° and 65°. Find the exterior angle."; "A right triangle
  has a hypotenuse of 13 and a leg of 5. Find the other leg."), 11.03 question 2 ("An exterior angle is 130°. One
  remote interior angle is 55°. Find the other remote interior angle."), 11.08 questions 1 and 3 ("Use tables to solve
  the system y = x + 3 and y = 2x."; "A 6-ft post casts a 4-ft shadow. A tree casts a 10-ft shadow. How tall is the
  tree?") and question 2's answer ("One solution, x = 0"). Unit 7's twenty warm-up questions were read the same
  evening: each is a whole question. **The Notes slides keep their short lines** ("Cross once: one. Never meet: none."):
  students copy them while the teacher talks. His to say if those should be sentences too.
- **Seen, not changed:** a box or fraction equation in a Lesson Plan's question cell is a picture at the body's size,
  larger than the 9-pt words of its cell, as it was on 14 Nov: the kit sets a picture at one size (`dockit.img`).
- **Left on purpose:** a whiteboard question that is a bare equation shows the equation alone (ruling 58 took "Answer
  it." away; whether "Solve for x." should stand there is asked of Croix); the step labels; the notes' short lines; the
  banks' data lines under a heading ("(3, 5);  y = 2x − 1 and y = x + 2"); "Florida B1G-M" in the plans' cause notes;
  the Review key's SSDD note; `te.say`, `note` and the other fields that print nowhere now.
- **Proof.** 341 exact strings by `reword.py` (lists and their generators in the session's `lean/u11/edits`; the
  generator is Windmill's `briefs/lean/edit_list.py` now). Gates 0 (390 items re-derived); `unit_repeats.py u11` 0; six
  full builds, the fourth from an emptied `out/u11` and the committed figure cache and the fifth and sixth from an
  emptied `out/u11` on that cache, each `checks: 0 findings`. `student_view.py u11 --bank` before and after: 376 ids, **105 questions
  and 35 answer lines reworded, no check, keyed letter, list of choices or kind moved, and no digit differs in any
  question or answer**. 146 of 248 slides differ from the build of 14 Nov: all looked at, and the 20 that the look sent
  back looked at again; the fourth and fifth builds' decks differ from the third's in the two slides meant to
  change and no other, the fifth build changed the words of three plans and nine keys and of nothing else, and the
  sixth changed eight warm-up slides and nothing else. Every PDF scanned: no
  equation broken across a line, no last line under ten characters, no line beginning with a lone variable, none of the
  old lines. Package reinstalled (128 files, no Teacher Edition); master sheet regenerated; `tools/check.sh` passes.
- **Not done:** not merged and not published; the site's Unit 11 pages and web decks are the build of 14 Nov (and still
  have the graph-over-question fault). **Before publishing, look at Unit 11's web decks** (Windmill's `briefs/REVIEW AND
  PUBLISH`): the web deck is a second renderer that no gate looks at. The practice page is untouched, and needs no
  change for this pass. M7 is not on this kit.
- **Open, for Croix:** merge and republish Unit 11 before 30 Nov; and whether a bare-equation whiteboard question should
  say "Solve for x." under its equation.


## 20–22 November — the lean workflow; Unit 7 built with it, merged and published on 22 Nov (session_01W9n2X1V97j7Nf5Y7z1DaCq)

Croix, 20 Nov, of how the lesson slides are built: *"It feels extremely inefficient and is burning tons of tokens."* Shown a
plan, 11:30 pm: *"You can get rid of the 4 page teacher edition. Only read math nation for scope and test item shapes. The
reviewers yeah opus then fable. Let's do it. Run the next unit to test."*

**Merged and published, 22 Nov** (Croix, 3:50 pm: *"Merge and publish."*). The branch `claude/lean-workflow` is `main` in
this repository and in Windmill, and Unit 7 is on the website: `mrshaffer.org/a7/unit-7/`, the five days' slides at
`/a7/slides/7.01/` … `/a7/slides/7.07/`, the calendar's five days linked, the teacher page behind the password (site
`efe8178`, from this repository's `05fd1f3`; Cloudflare's build of that commit succeeded and the live pages were read).
M7 has not been moved to the new kit.

- **What publishing found.** (1) **The web deck let a graph run over its question and its answer line**: on 7.01's web
  pages the picture beside a Your Turn's steps covered "Complete the table…" above it and "Answer:" below. The
  PowerPoint never had it; the web deck is a second renderer (`lib/htmlkit`) that no gate looks at. One rule of its
  stylesheet was wrong (Windmill `557f670`, vendored here in `05fd1f3`). All 177 slides of Unit 7's five web decks were
  looked at after the fix. **The web decks of Units 3–6 and 11 on the site still have the fault** (11.07's Example 1 and
  both Your Turns, for one): each is mended when its unit is next published, and not before, because a deck made today
  would carry this kit's lines beside a PowerPoint that does not. (2) The site's own check that an unnamed unit shows as
  "Unit N" alone named Unit 7, and failed the moment Unit 7 had a name; it reads the unnamed units from the plan now.
  (3) Unit 7 is the first unit on the site with no Teacher Edition and no practice page: the teacher page lists Lesson
  Plans, banks and keys, "All in one" has four files, and the unit page has no online practice test. Both pages were
  looked at. (4) On the unit page a lesson's name is its file's name, so "Is It Proportional?" reads "Is It
  Proportional" and 7.02–03 has no colon: every unit's page does this.


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
- **The kit** (Windmill `d144647`, vendored): `reword.py` (a wording pass as exact strings) and the five lean tools (`reader_copy.py`, `student_view.py`, `blind_diff.py`,
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

- **The wording pass (ruling 58).** Croix sent two outside audits of the All Slides PDF on 21 Nov (11:06 am, a
  slide-by-slide "revision guide"; 11:43 am, ChatGPT's language audit: *"Here's what chat said."*) and, on the defaults
  put to him at midday, 11:58 am: *"Go"*. Done that afternoon in every deck, Independent Set, Question Bank and Lesson
  Plan, the Review, the Practice Test, the Reference Sheet and 00 - START HERE:
  - a graph shows y "versus" x, never "against"; a rate is "per" ("\$3 per mile", "the same amount per pound"), and the
    constant of proportionality is "the amount of y for every 1 unit of x";
  - a table drawn left to right has pairs, not rows: "y ÷ x is the same for every pair", "which cost would have to
    change, and what should it be?";
  - the definition, in the same words in 7.01, 7.04 and the Reference Sheet: "two quantities are in a proportional
    relationship when one quantity is always a constant multiple of the other: y = px";
  - whole questions for fragments ("When equal?", "Its equation?", "The same table."); "Let e represent…" where a
    sentence began with a letter; two sentences where a colon joined two; "explain" and "identify" for "say"; "the
    other way around"; "either quantity can be y" for "the subject" and "alone"; options as "B only, because its line
    passes through the origin." and "No. 15 ÷ 4 is not 4." in place of the two-dash lines;
  - headings: 7.01 "What makes a relationship proportional?" and "The graph of a proportional relationship"; 7.04 "The
    table test: check every pair", "The graph test: two conditions", "Nothing added at the start"; 7.05 "From a graph
    or a description", "Either quantity can be y"; 7.07 "Compare the constants", with "Find each constant in the same
    units, then compare them.";
  - kit-wide, so in every unit of both courses at its next rebuild: no "Answer it." under a board; "Write your answer
    in complete sentences."; the IXL slide ("Open IXL and work on the skills listed below." / "Show your work on
    paper. IXL's answer box does not record it." / "Complete every listed skill to a SmartScore of at least 67." and
    the due line, under "Required IXL skills"); the unit cover's "the next slide links to each one"; "1 question";
    "No new terms." in a Lesson Plan with no new word.

  Not taken, with the reason: the guide's y = kx (Florida writes y = px), its "math error" on 7.04's warm-up (the
  slide reads y = 3x), its k = 0.625d and its × sign; chat's "every row" (the pairs are columns), its removal of the
  ruling-22 numbers, serial commas where a target quotes its benchmark, "initial value of 0" (the unit's words are
  "nothing added at the start"), and every rewrite too long for its slide — a warm-up stem is one line of about 60
  characters, so "Find the constant, in dollars per pencil." (7.05) and "or 5 for \$11.50" (7.07) stay short.

  How it was run and proved (Windmill `briefs/LEAN WORKFLOW.md`, "A wording pass"): about 470 strings written by the
  lead and applied by `reword.py`; gates 0, `unit_repeats.py u7` 0, a clean build, `checks: 0 findings`; the 151
  questions whose words changed solved blind by two Opus solvers (216,000 tokens, the pass's only agent runs) — no key
  differs; of their 27 doubts two were real and are fixed (7.05's Your Turn never named the letter e; 7.07's warm-up
  read "the equation y = px" as given), the rest were the solver file's misplaced bank headings or ruling-22 numbers;
  the lead looked at all 152 changed slides and at the papers, and shortened nine lines that left one word on a
  second line, wrapped an answer or squeezed a graph (14 slides, looked at again). 7.04's Example 2 and Your Turn
  then got their whole questions back ("Is the cost proportional to the number of miles?"), which the slide wraps
  onto a second line: 3 slides, looked at. Every PDF was searched for the old lines (none left) and for a font other
  than Lexend (none but the answer bubbles, check boxes and back arrow, which Lexend does not have). Page counts are
  unchanged but for two bank keys (one page each way).

- **The second wording pass (ruling 59).** At 3:08 pm on 21 Nov Croix sent ChatGPT's third audit, of the rebuilt slides and
  the All Documents packet (*"Here's what chat found"*). Seven of its findings were real. Four of its "top ten" were wrong on
  the facts: Theo's e and h are named by the table's rows; both pumps are named, on the table and on the graph; the
  Reference Sheet is its own handout, which was not in the two PDFs; "two constants" is the standard statement. His three
  answers, asked one at a time: "steady" — *"Switch to "constant""*; the Independent Set's opening line — *"Just get rid of
  it completely"*; who reads the Lesson Plans — *"John or admin: write it out"*.
  - **Kit** (ruling 59, card 20): the Lesson Plan template prints whole sentences in both plan styles — "Required by the
    benchmark." and "Not part of this lesson." for "Must." and "Must not."; the sequence rows, the gradual release, "Peer
    discussion (MTR.4.1)", the practice line; the checks table headed "Likely wrong answers and their causes"; the build's
    notes beside three headings gone. An Independent Set prints no instruction line. The Review's directions are the
    Practice Test's ("Show your work for problems that require calculations."). No ruling number prints: the key's
    follow-through note and the transfer note say it in words.
  - **Unit 7's specs** (`reword.py`, 91 edits): "constant" for "steady" in 28 places; every plan field of the five lessons
    as sentences (`te.must`, `te.must_not`, the MTR evidence, Building on, Working toward, three higher-order questions,
    the ESE / 504 and Enrichment rows, the closure, the materials — 7.01's 43-minute day no longer mentions the build);
    "[an extra number, included on purpose]" for "[ruling 22]"; the constant of proportionality "equals y ÷ x for every
    pair where x is not 0", once, at its definition (7.02–03's vocabulary slide and the Reference Sheet), and a fourth
    higher-order question in 7.02–03's plan ("Why can that pair not be used to find the constant?"); 7.04's note "Going
    up by the same amount does not make y ÷ x the same."; 7.04 board 5 "passes through (0, 0)"; "Explain." for "Give the
    reason.".
  - **What the slide would not hold:** 7.04 board 5's answer line is "It passes through (0, 0)." ("Their line passes
    through" ran to two lines); the definition says "where x is not 0" in words ("(0, 0)" set as mathematics broke across
    the line and printed a dollar sign, which `markup` refused; without the space it left a gap before its colon); the
    snail of 7.02–03 board 7 "crawls 34 centimeters every 8 minutes" ("at a constant speed." left one word on a second
    line); the pump question's fuller form needs two lines and stays as it was.
  - **Not taken** (each with its reason in the Review Rulings): "x ≠ 0" on every line; "two reciprocal unit rates"; the
    longer board questions; dropping the comma before a unit; "The price per pound is constant"; removing the B1G-M tags;
    "Independent Practice".
  - **Proof:** gates 0 (282 items re-derived), `unit_repeats.py u7` 0, `checks: 0 findings` after a full rebuild;
    `student_view.py` before and after differs in 23 questions (20 that said "steady", the snail among them, and 3
    that said "Give the reason.") and 3 answers, and in no key and no check — so no solver was run, because nothing that is asked changed; all 12 changed
    slides, the five plans and one page of each changed paper looked at; every PDF searched for the old lines. Page
    counts are unchanged.

- **The third wording pass: the follow-through line dropped, and the pages looked at.** At 8:50 pm on 21 Nov Croix sent
  Gemini's checklist, the fourth outside audit (*"Drop the line. Also here is what Gemini found. I want the student facing
  slides and handouts specifically to be perfect."*). "The line" is the follow-through note on a key, asked of him after
  the second pass. Gemini's list was checked item by item against the pages; then every student-facing question, every
  slide line and the Reference Sheet were read again; then the built pages were looked at, which found what no reading of
  the words had.
  - **Kit** (Windmill `f8634ee`, `254e1b0`, `5b374da`, `33a26e0`; card 19). No key prints a follow-through note (ruling
    19's scoring stands). The Review's "How to use this review" is three plain sentences. A bank says "Show your work for
    problems that require calculations." and no longer "Circle your final answer". **Three things about how a paper is
    set, for every unit at its next rebuild:** an equation written in a sentence does not break across a line
    (`dockit.glue`: 25 lines of this unit's papers ended on a sign or began with one, "She wrote 5 / ÷ 1 = 5" in 7.04's
    Question Bank among them; none does now); a stacked fraction stands on the line with its comma beside it
    (`dockit.img`: it rode a third of a line high with a gap on each side, "Graph    y = ¼x   .  Choose"); a paragraph's
    last line is never one short word (`dockit.bind_tail`: "…in miles per / hour?", "…and find each / y.").
  - **Unit 7's specs** (`reword.py`, about 180 lines in the five lessons and `unit.py`). From Gemini: a line "passes
    through" a point; a graph "shows how far a cyclist rides", not "miles versus hours"; a decimal takes a plural unit
    ("0.8 pounds per dollar"); "Write the equation for f" where the letters are not x and y; "For values beyond the grid,
    use the equation."; a comparison's answer is "Store B (\$3.30 per pound versus \$3.50)", not a second colon after
    "Answer:"; the Reference Sheet, sentence by sentence; the Review key's question 17 prints its question; the plans'
    last loose sentences. From the reading: a sentence does not open with a numeral ("Five notebooks cost \$9.00.";
    7.02–03 board 6 is "Rice costs the same amount per pound, and 5 pounds cost \$8.00." over "The constant of
    proportionality is 1.6. What does 1.6 mean?"); "No." is not followed by a numeral, where it reads as "number" ("No, 20
    prints would have to cost \$7.00."; "No, because 6 ÷ 1 = 6 but 10 ÷ 2 = 5."); 7.07 board 3's choices are facts about
    the lines ("Jo. Jo's line is steeper."), not "The steeper line is faster."; "how many marbles are in 2, 5 and 7 bags"
    and "how far she paddles" for "different numbers of".
  - **From the look at the pages:** a word alone on a slide's second line (7.02–03 board 2 is now "in cups per cookie";
    7.01's set, question 6, "The point (1, 3.5) is on the graph from question 5. What does it mean?"); a semicolon adrift
    after an equation on 7.04's Vocabulary slide; and **the gap before an equation on a slide**. The deck keeps a 6%
    margin on the measured width of a run of words, so a picture of an equation after a long run stands about half an inch
    off. Sixteen lines of this unit now write a simple expression in the sentence's own words ("…passes through (5, 13).",
    "…of the other: y = px", "Store B's equation is now c = 3.75w."), and two put the picture early ("The point (7, □) is
    on the graph of copies versus minutes."; "Ana says 1/5 is the constant of proportionality."). Short runs keep their
    pictures, and so do the five Independent Set slides (7.07's does not hold its six questions otherwise).
  - **Wrong on the facts** (Gemini): the Reference Sheet prints "x: −2, 1, 4" (the audit read 2); the 3 of slide 73 is a 3.
  - **What the slide would not hold:** 7.01's first warm-up still does not say what w is ("After w weeks, Plan A costs…"
    is 12.9 in on a line of 10.45 in; the three wordings that fit are worse sentences); 7.05–06's first Your Turn keeps
    "Find the constant, the equation for e, the table and two graph points." (its table names e and h; the fuller
    sentence takes the room the four steps need); the pump question keeps "by how many gallons in 15 minutes?"; 7.01
    board 5 keeps "y = (5/6)x. Choose three x-values…"; 7.04 board 6's tub "gains 4 per minute".
  - **Not taken** (each with its reason in the Review Rulings): "in terms of" and "isolate" on a slide; "SSDD" removed
    (his word); the dates taken out of 7.07's plan (it is his calendar); "[distractor information used]"; "a \$40 service
    fee"; "Does it represent a proportional relationship?"; "\$0.25 per minute means each minute costs \$0.25".
  - **Proof:** gates 0 (282 items re-derived); `unit_repeats.py u7` 0; a clean rebuild, `checks: 0 findings`;
    `student_view.py` before and after: 58 questions, 28 answers and 5 lists of choices reworded, no keyed letter and no
    check moved, so no solver was run; all 62 changed slides looked at in their last form, with the Reference Sheet, the
    Review, the Practice Test, the five Independent Sets and pages of the banks, a plan and a key; every PDF searched
    for the old lines and for a line break inside an equation; fonts Lexend but for the bubbles, the check boxes and the
    back arrow; every PDF has the page count it had.
- **The fourth wording pass (ruling 60): "isolate" and "solve for".** The third pass had refused those two words where
  Gemini asked for them, on the ground that Unit 7 does not teach them. Croix, 21 Nov, 11:40 pm: *"What do you have now
  instead of isolate?"* Shown the six places, 22 Nov, 1:54 pm: *"Isolate and solve for are correct terminology. That's
  what should be used across the whole unit."* (A7's Unit 1, Equations and Inequalities, taught both: "Describe the
  operation that isolates n on the left side.", "Solve for x, then simplify." The third pass had not looked.) **Ruling
  60** is on the kit's card (19) and in its ledger: a variable alone on one side is *isolated*, and the equation is
  *solved for* it; "the other way around", "work backward", "an equation for either quantity" and "which quantity the
  equation is for" are retired for that idea. 74 exact strings by `reword.py`.
  - **On the slides** (8 of 179 changed): 7.05–06 Notes III is "Either variable can be isolated" ("Solved for m",
    "Solved for h", "The question tells you which variable to solve for."); its second Your Turn ("solve for g: 350 =
    25g, so g = 14"; "Solved for g: g = (1/25)m…"); whiteboard questions 5 ("Solved for d, the kilometers: d = 1.6m")
    and 6 ("solve for x: 36 = 2.4x, so x = 15"); the Independent Set's question 4; 7.07 Notes III ("…then solve for the
    other variable."), its second Your Turn and whiteboard question 8 ("Solve for t: …").
  - **On the papers:** 7.05–06's set, question 4, "Solve the equation for n, the yards in f feet." (key: "n = (1/3)f, or
    n = f ÷ 3"; the state's own second form is h = m/60); both banks' heading "Solve for the other variable." and its
    question; the Reference Sheet's section 5, now "Writing and Solving the Equation" ("Either variable can be
    isolated…", "Solve for x when you know y… Isolate x by dividing both sides by 1.4"), with a line each in sections 3
    and 6; the keys ("Solve 63 = 4.2x for x: x = 15." for "working backward"); the Lesson Plans (7.02–03's third
    question, in Gemini's words; 7.05–06's "Required by the benchmark", ELL and enrichment lines and two causes in its
    checks table; 7.07's "Building on").
  - **Two questions now ask something a little different: the Review's 13(b) and the Practice Test's 12(b)**, "Solve
    your equation for w, the pounds that c dollars buy." and "Solve your equation for h, the hours it takes him to earn
    e dollars." Before, each asked for a second equation, which a student could write from 12 ÷ 240 without part (a);
    now part (b) starts from the student's own equation, so a wrong (a) carries into (b) and ruling 19 scores it. Each
    key gives three forms (h = e ÷ 20, h = (1/20)e or h = 0.05e). His to turn back.
  - **Left as it was, on purpose:** "which quantity is y" where the page names no letters and the question is the
    constant (7.02–03 Notes III, "With gallons as y"; its boards and keys; the Reference Sheet's sections 1 and 3):
    nothing is isolated there, and Gemini's own list keeps "The constant depends on which quantity is y." "Write the
    equation for f" and the Review's "Write an equation for…" stay: the question names the variable the equation is
    solved for. The example slides stay mathematics only (ruling 37); their notes in the spec use the terms.
  - **What the pages showed.** The Practice Test's 12(b) ran into its "1 pt" (shortened). On 7.05–06's set the paper
    broke "Solve the equation for / n, the yards in f feet." **Kit, Windmill `d144647`:** on a paper a one-letter
    variable now stays with the word before it (`dockit.tie_letters`), and the rule that keeps a paragraph's closing
    words together reaches across its pieces. That second fix mends a line the third pass's proof had missed: 7.01's
    Question Bank, question 7, ended "What is y when / x = 1?", six characters alone on a line, where the proof said no
    student paper had a last line under ten (the scan counted "x = 1?" as three words). It reads "What is y / when x =
    1?" now. Two Reference Sheet paragraphs that ended on "constants." and "that point." were reworded.
  - **Proof:** gates 0 (282 items re-derived); `unit_repeats.py u7` 0; three full builds, the last one clean, `checks: 0
    findings`; `student_view.py` before and after: 5 questions and their answers reworded and 2 headings, no keyed letter
    and no check moved, each of the five worked by hand (f = 3n gives n = f ÷ 3), so no solver was run; all 8 changed
    slides looked at in their last form; the 9 changed pages of the student papers looked at, with the Reference Sheet
    whole, a plan page and two key pages; 33 paper pages differ in all, in 19 papers; every PDF searched for the retired
    lines (none), for an equation broken across a line (none) and, by a scan written from the rule this time, for a last
    line under ten characters (none); all 50 PDFs keep their page counts; kit tests 301 of 301, 300 of 300 and 53 of 53.

### Open, for Croix (22 Nov)

- **Wording left as it is, his to say:** the name "Independent Set" (the audits want "Independent Practice": it is in
  every file name, the site, the master sheet and six taught units); the ruling-22 numbers (the snail's age, the 180
  passengers, the 40 seats, the 50 pages, room 114).
- **The gap before an equation on a slide is the kit's, and in every unit.** Unit 7's long lines were rewritten in
  words (above). The kit could set a simple expression inside a sentence as words on every slide, as it does on paper:
  a change to the look of every deck, to be seen in Google Slides before it is made. His to say.
- **Units 3–6 and 11 keep the old wording** until they are rebuilt: "against" in every one of them, "the other way
  round" in Units 4 and 5, "Answer it." under every board, the old IXL lines; and, since ruling 59, the Lesson Plans'
  shorthand, the Independent Set's opening line and "Circle your final answer" on the Review; and, since the third pass,
  a key's follow-through note and the way a paper is set (an equation may break across a line, a fraction rides high, a
  last line may be one word, a line may begin with a lone variable). **Ruling 60 is not in them either:** Units 4 and 5
  say "the other way round" where Unit 7 now says "solve for", and **Unit 11, Solving Equations and Systems (taught from
  30 Nov), has neither "isolate" nor "solve for" on any page** (its 74 PDFs searched): its notes say "undo + 25 by
  subtracting". Unit 1's pages did use both ("Describe the operation that isolates n on the left side.", "Solve for x,
  then simplify."), which is why the two words are his class's own. ("Work backwards." heads a group in Unit 11's banks
  and in Units 3 and 4: a kind of question, not this idea.) His to say whether Unit 11 gets the two words before it is
  taught. The kit's lines change at a
  rebuild; a unit's own plan sentences (`te.must`, the MTR evidence, the closure) need the rewrite Unit 7 had. Unit 11
  is taught from 30 Nov.
- **Merged and published on 22 Nov** (above). Windmill's `main` carries the Drive test's fix (`41a5a7c`), the kits of
  ruling 59 (`7344e7e`), the third pass (`33a26e0`) and ruling 60 (`d144647`), and the web deck's fix (`557f670`). The
  Drive script in his Google account is unchanged (Windmill HANDOFF, 21 Nov); its mirror picks up Unit 7's package by
  itself.
- **The web decks of Units 3–6 and 11 on the site** have the graph-over-its-question fault until each unit is published
  again. Unit 11 is taught from 30 Nov.
- **The practice page** for Unit 7 is not built (the test is a random set of it). Question 1(b) needs a part where a student
  plots points, and 8(b) takes a cost and what it should be, or "none".
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
