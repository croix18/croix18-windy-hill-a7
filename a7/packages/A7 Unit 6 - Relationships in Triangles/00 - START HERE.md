# A7 Unit 6 — Relationships in Triangles

Windy Hill Middle School · course 1205050 · six teaching days (eight book lessons, merged to six) and the two Thread B days after the test, a review sent home Mon 16 Nov, the test as one period on Tue 17 Nov (a random set of the practice page).

**By the plan** (Windmill's spine as of 2026-10-24; `tools/scope_calendar.py` is its source): lessons Fri 6 Nov – Thu 19 Nov, the assessment Tue 17 Nov, 2026. The dates move when the as-run log does (the plan follows the class), and a day is logged from the phone view of the plan.

Nothing exists until it is committed. This folder is generated from `a7/build/u6/` by `install_unit.py`; edit the specs and rebuild rather than editing these files by hand.

---

## How the files are named

**Course, number, title, then what it is** — `A7 6.04 Pythagorean Theorem in Real-World Problems - Slides.pptx`, `A7 6.04 Pythagorean Theorem in Real-World Problems - Question Bank.docx`, `A7 6.04 Pythagorean Theorem in Real-World Problems - Question Bank - Key.docx`. Unit-wide files carry the unit instead of a lesson: `A7 Unit 6 Relationships in Triangles - All Slides.pptx`, `A7 Unit 6 Relationships in Triangles - Test.docx`, `A7 Unit 6 Relationships in Triangles - Test - Key.docx`, `A7 Unit 6 Relationships in Triangles - Review.docx`, `A7 Unit 6 Relationships in Triangles - Reference Sheet.docx`. Single spaces, pieces joined by ` - `, two-digit lesson numbers so everything sorts in teaching order. The same pattern in both courses (Croix, 4 October 2026). The two Thread B days are `A7 6.T1` and `A7 6.T2` (MA.8.GR.1.4 and 1.5 — Math Nation 16.1 and 16.2, taught after the Unit 6 test so the angle facts are in play for the rest of the year) and carry no book lesson number.

---

## Where everything lives

| Folder | What is in it |
|---|---|
| **All Slides** | `A7 Unit 6 Relationships in Triangles - All Slides.pptx` — the whole unit in one PowerPoint, in teaching order; each lesson keeps its own slide numbers, so the Teacher Edition lines up. **A deck is its Slides file** (ruling 41, 5 October 2026): there is no HTML deck and no console. **To teach from one in Deckhand**: upload the lesson's `Slides.pptx` (or this file) to Google Drive, open it — it opens as Google Slides — and paste that link into Deckhand's Slides card; the pen and the timers are Deckhand's. The slides are set in Lexend, which Google Slides has, so they arrive as built. A board is two slides: the question, then the same question with its steps and its answer. |
| **Lessons** | **One folder per lesson, named by its number (`3.08`; the title is in every file's name), everything for that day in it**, each document with its PDF beside it (the PDF is what gets printed and posted). *Slides* — the lesson's own deck, a `.pptx` (upload it to Drive and it opens as Google Slides; paste that link into Deckhand's Slides card). *Teacher Edition* — three or four pages, read in twenty minutes (ruling 26): page 1 is the period (benchmark with its Must and Must-not lines, the target, the MTRs, the timing table, the three sentences to say out loud), then one line per slide, each board carrying its answer, its named distractors and the split-board move, and Misconceptions to Watch at the end. *Lesson Plan* — the Florida-format plan (ruling 25): standards, the MTRs with their evidence, the sequence read from the deck, gradual release, higher-order questions with DOK, checks for understanding with the response to each, differentiation. *Independent Set* — the six questions written in silence (ruling 21). *Question Bank* and *Additional Question Bank* — retired worksheets are question banks (ruling 11): draw from them for practice, exit tickets or re-teaching. |
| **Lessons / … / Keys** | Inside each lesson's folder: that lesson's three answer keys and nothing else. |
| **Review** | The Unit Review and its key (unscored; it goes home as practice — ruling 27a, A7 has no review day). |
| **Assessment** | The unit test (one paper, one period) and its key. |
| **Handouts** | The Reference Sheet. Students study from it; it may NOT be used on the assessment (ruling 13). There is no study guide (ruling 11). |
| **Reference** | Not handouts: `A7 Unit 6 Relationships in Triangles - Question Bank.md` (how each question bank varies, what the audit found, what changed from the book, and every bank answer — ruling 26 moved this out of the teacher's edition), the Math Nation package audit, the scope and sequence, the IXL due-date sheet, the Grade 8 source of truth. |

**Nothing with an answer printed on it sits beside a student page:** a lesson's keys are in its `Keys` folder, and every such file says Key in its name.

---

## Unit at a glance

| Day | Planned | Lesson | Benchmark | The line that carries the day |
|---|---|---|---|---|
| 6.01–02 | Fri 6 Nov | Triangle Inequality Theorem; Converse of the Pythagorean Theorem | MA.8.GR.1.3 | The two shorter sides add to MORE than the longest. Right exactly when their squares add to the longest side's square. |
| 6.03 | Mon 9 Nov | Pythagorean Theorem | MA.8.GR.1.1 | a² + b² = c², and c is across from the right angle. A leg: subtract. |
| 6.04 | Tue 10 Nov | Pythagorean Theorem in Real-World Problems | MA.8.GR.1.1 | Find the right angle first; the side across from it is c. |
| — | — | Unit Review | all six | unscored, sent home as practice (ruling 27a); the SSDD block is named on the key only |
| — | Tue 17 Nov | Unit Assessment — one period, one paper | all four benchmarks, sections by benchmark in the order GR.1.3 · GR.1.1 · GR.1.2 · GR.2.4; the practice test alone (ruling 49), 14 questions, one period (ruling 51) | 18 points |

Book order, with 6.1 + 6.2 and 6.7 + 6.8 merged — both merges are the plan's own (6.2 is 6.1's practice, 6.8 is 6.7's). One day of MA.8.GR.1.3, two of MA.8.GR.1.1, two of MA.8.GR.1.2, one of MA.8.GR.2.4. No review day (ruling 27a): the review paper goes home Mon 16 Nov with 6.07's independent set, the test is Tue 17 Nov. Thread B (T-B1 Wed 18 Nov, 43 minutes; T-B2 Thu 19 Nov) is not on the Unit 6 test.

---

## How a period runs (rulings 10–12)

Title and learning target (1 min) → warm-up, four spaced-retrieval questions (5) → notes (10–11) → two worked examples with a Your Turn each (10) → **nine whiteboard questions**, question 9 written (the remainder, 10–20) → the **independent set**, six questions written in silence (6, ruling 21) → IXL, the last five minutes. Every wrong option on every multiple-choice item is a named error with its benchmark cited, in the Teacher Edition and on the keys (§16 rule 4).

## Timing

<!-- timing table: generated by install_unit.py from the deck side-cars. Do not edit by hand. -->

| Lesson | Teaching (title, warm-up, notes, examples) | Whiteboard round | IXL | Total |
|---|---|---|---|---|
| 6.01–02 | 38 min | 10 min | 5 min | 53 min |
| 6.03 | 38 min | 10 min | 5 min | 53 min |
| 6.04 | 38 min | 10 min | 5 min | 53 min |

The whiteboard round is the remainder — 10–10 minutes across the unit — and the build refuses any plan whose remainder falls outside 10–20. Every plan totals 53 exactly. There is no shortened variant; short days are absorbed by the person in the room.

<!-- end timing table -->

---

## Standing decisions baked into these files

- **No partner or group work anywhere.** Math Nation's explorations and collaborations are taught from the front; its partner-discussion tasks are written whiteboard questions.
- **Calculators: allowed on everything, and nothing about them is printed on any student page.** The one exception the house style allows is the Reference Sheet's description of what the FAST platform provides (an on-screen scientific calculator) — that is a description, not a permission line.
- **Old-school textbook styling.** No commentary panels, no grey bars, no clip art. American spellings.
- **One point per lettered part, no partial credit**, with follow-through credit (ruling 19): a later part earns its point when the right operation is applied to the student's own earlier value, where that work is on the page. The key carries a `Scoring:` line under every question and a per-benchmark Score Tracker at the end.
- **The assessment is one paper, one class period** (ruling 51, 24 October 2026 — every A7 unit test is one period; the practice test's random draw is sized for it, ruling 49). Two questions are **transfer items** (ruling 18) — same benchmark, a surface that appears on no review and in no question bank — and the key names them.
- **No benchmark codes on student pages.** The deck title slide and the keys and Teacher Editions carry them.
- **Opens cleanly in Google Docs.** Every document is a fixed-width table layout with no nested tables and a spacer after every block; fonts are Times New Roman / Georgia / Arial with FreeSerif for the bubbles only.
- **Every answer is re-derived by machine at build time.** Every item carries a `check` that sympy evaluates (variable bases as symbols); every multiple-choice distractor must name its error; every scientific-notation coefficient is scanned for the [1, 10) rule; the build refuses on any finding. The post-build suite (`checks.py`) then reads the rendered PDFs for off-page text, glyph coverage, Google-Docs layout rules and the timing plan.
- **Math Nation's copyrighted pages are not in this repository.** The audit in `Reference/` records what was checked and what was found; the items here are a mix of the book's (verified) and original ones, aligned to the benchmark text and the B1G-M first.

---

## Before the unit starts

- **Built in the order the rulebook asks (§16):** from the benchmarks first, then read against Math Nation 6.1–6.8, its test and 16.1–16.2 — the audit is in Reference.
- **Every square root has a whole radicand up to 225** (GR.1.1 and GR.1.2, Clarification 3), and none has a square factor, so √n is already in simplest form; an irrational answer is also given to the nearest tenth wherever the question asks for a measurement. Math Nation's own test breaks the 225 bound on four of its five Pythagorean items.
- **No distance formula** (GR.1.2, Clarification 2): a slanted distance is always the right triangle drawn on the grid, its legs read from the coordinates.

Installed: 54 files from the build, plus this page and the Reference folder.
