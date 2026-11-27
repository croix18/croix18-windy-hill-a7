# A7 Unit 10 — Linear Relationships

Windy Hill Middle School · course 1205050 · eight teaching days (ten book lessons; 10.2 with 10.3 and 10.7 with 10.8 each one day; Mon 18 Jan is a holiday; Wed 20 Jan and Wed 27 Jan are 43-minute days), a review sent home Tue 26 Jan, the test as one period on Thu 28 Jan (a random set of the practice page), and a flex day Fri 29 Jan.

**By the plan** (Windmill's spine as of 2026-11-18; `tools/scope_calendar.py` is its source): lessons Fri 15 Jan – Wed 27 Jan, the assessment Thu 28 Jan, 2027. The dates move when the as-run log does (the plan follows the class), and a day is logged from the phone view of the plan.

Nothing exists until it is committed. This folder is generated from `a7/build/u10/` by `install_unit.py`; edit the specs and rebuild rather than editing these files by hand.

---

## How the files are named

**Course, number, title, then what it is** — `A7 10.05 Slope-Intercept Form and Graphing a Line - Slides.pptx`, `A7 10.05 Slope-Intercept Form and Graphing a Line - Question Bank.docx`, `A7 10.05 Slope-Intercept Form and Graphing a Line - Question Bank - Key.docx`. Unit-wide files carry the unit instead of a lesson: `A7 Unit 10 Linear Relationships - All Slides.pptx`, `A7 Unit 10 Linear Relationships - Practice Test.docx`, `A7 Unit 10 Linear Relationships - Practice Test - Key.docx`, `A7 Unit 10 Linear Relationships - Review.docx`, `A7 Unit 10 Linear Relationships - Reference Sheet.docx`. Single spaces, pieces joined by ` - `, two-digit lesson numbers so everything sorts in teaching order. The same pattern in both courses (Croix, 4 October 2026). The merged day 10.02–03 carries the files of `A7 10.02` (book lessons 10.2 and 10.3), and 10.07–08 carries those of `A7 10.07` (book lessons 10.7 and 10.8). There is no `A7 10.03` and no `A7 10.08`.

---

## Where everything lives

| Folder | What is in it |
|---|---|
| **All Slides** | `A7 Unit 10 Linear Relationships - All Slides.pptx` — the whole unit in one PowerPoint, in teaching order; each lesson keeps its own slide numbers, as in its own deck. **A deck is its Slides file** (ruling 41, 5 October 2026): there is no HTML deck and no console. **To teach from one in Deckhand**: upload the lesson's `Slides.pptx` (or this file) to Google Drive, open it — it opens as Google Slides — and paste that link into Deckhand's Slides card; the pen and the timers are Deckhand's. The slides are set in Lexend, which Google Slides has, so they arrive as built. A board is two slides: the question, then the same question with its steps and its answer. |
| **All in One** | Merged PDFs, in teaching order, one bookmark per document: *All Lesson Plans*, *All Assessments* (each form's paper, then its key, then its worked answers) and *All Keys*. The same pages as the per-document PDFs, for printing or reading the unit straight through (Croix, 17 October). |
| **Lessons** | **One folder per lesson, named by its number (`3.08`; the title is in every file's name), everything for that day in it**, each document with its PDF beside it (the PDF is what gets printed and posted). *Slides* — the lesson's own deck, a `.pptx` (upload it to Drive and it opens as Google Slides; paste that link into Deckhand's Slides card). *Lesson Plan* — the Florida-format plan (ruling 25): standards, the MTRs with their evidence, the sequence read from the deck, gradual release, higher-order questions with DOK, checks for understanding with the response to each, differentiation. *Independent Set* — the six questions written in silence (ruling 21). *Question Bank* and *Additional Question Bank* — retired worksheets are question banks (ruling 11): draw from them for practice, exit tickets or re-teaching. |
| **Lessons / … / Keys** | Inside each lesson's folder: that lesson's three answer keys and nothing else. |
| **Review** | The Unit Review and its key (unscored; it goes home as practice — ruling 27a, A7 has no review day). |
| **Assessment** | The Practice Test paper and its key (scoring lines, the Score Tracker) — the blueprint of the unit test. **The unit test itself is a random set of the practice page** (ruling 49), one period: print it from the page's teacher copy (Teacher copy bar → Print the test, 1–5 forms, each a different set with its key). No Form A/B, no transfer items, no worked-answers copy. |
| **Handouts** | The Reference Sheet. Students study from it; it may NOT be used on the assessment (ruling 13). There is no study guide (ruling 11). |
| **Reference** | Not handouts: `A7 Unit 10 Linear Relationships - Question Bank.md` (how each question bank varies and every bank answer), the unit's plan (Lesson Outlines) and the rulings on its review, the scope and sequence, the IXL due-date sheet, the Grade 8 source of truth. |

**Nothing with an answer printed on it sits beside a student page:** a lesson's keys are in its `Keys` folder, and every such file says Key in its name.

---

## Unit at a glance

| Day | Planned | Lesson | Benchmark | The line that carries the day |
|---|---|---|---|---|
| 10.01 | Fri 15 Jan | Linear and Proportional Relationships | MA.8.AR.3.1 | A linear relationship has a constant rate of change. It is also proportional when y is 0 when x is 0: its line passes through the origin. When a table has no row for x = 0, students step back to x = 0 to decide. |
| 10.02–03 | Tue 19 Jan | Slope from Graphs, Tables and Two Points | MA.8.AR.3.2 | Slope is the change in y divided by the change in x: rise over run. Students subtract in the same order, and any two points on the line give the same slope, including the points of a table whose x-values do not go up by 1. |
| 10.04 | Wed 20 Jan | Slope in Context | MA.8.AR.3.2, MA.8.AR.3.5 | The slope is a rate of change: its unit is the y-unit per x-unit. Students read the scales first, and a negative slope means the amount goes down. This is a 43-minute day: whiteboard question 4 is the first cut, then whiteboard question 8. |
| 10.05 | Thu 21 Jan | Slope-Intercept Form and Graphing a Line | MA.8.AR.3.4 | In y = mx + b, m is the slope and b is the y-intercept, the value of y when x is 0. To graph, students start at the y-intercept, then move with the slope; question 1 of the set is drawn in class. |
| 10.06 | Fri 22 Jan | Graphing from Tables and Contexts | MA.8.AR.3.4 | Students graph a line from a table or a description, where the start is the y-intercept and the rate is the slope, with scales that fit. An equation in another form is graphed from a table of values; question 1 of the set is drawn in class. |
| 10.07–08 | Mon 25 Jan | Interpreting Slope and y-Intercept | MA.8.AR.3.5 | The rate is the slope, and the start is the y-intercept: each is explained in a sentence with both units, from an equation, a graph, a table or a description. F = 1.8C + 32 is taught as linear, not proportional. |
| 10.09 | Tue 26 Jan | Writing Equations of Lines | MA.8.AR.3.3 | Students write y = mx + b from a graph, a table or two points. When no y-intercept is in sight, they substitute a point and solve for b. |
| 10.10 | Wed 27 Jan | Writing Equations for Contexts | MA.8.AR.3.3, MA.8.AR.3.5 | Students name the variables, then write the equation in the question's own letters: the rate is the slope, and the start is the y-intercept. This is a 43-minute day: whiteboard question 6 is the first cut, then whiteboard question 4. |
| — | — | Unit Review | all 7 | unscored, sent home as practice (ruling 27a); the SSDD block is named on the key only |
| — | Thu 28 Jan | Unit Assessment — one period, one paper | all five benchmarks, sections by benchmark in the order MA.8.AR.3.1 · AR.3.2 · AR.3.4 · AR.3.5 · AR.3.3; the practice test alone (ruling 49), 16 questions, one period (ruling 51) | 20 points |

Book order, with 10.2 and 10.3 merged (slope from a graph, a table and two points is one idea) and 10.7 and 10.8 merged (what the slope and the y-intercept mean). Eight decks run from Fri 15 Jan to Wed 27 Jan 2027. Mon 18 Jan is a holiday, and Wed 20 Jan and Wed 27 Jan are 43-minute days. There is no review day: the review paper goes home Tue 26 Jan with 10.09, the test is Thu 28 Jan in one period, and Fri 29 Jan is a flex day. Unit 10 is taught after Unit 11 (December) and Unit 7 (6–14 January).

---

## How a period runs (rulings 10–12)

Title and learning target (1 min) → warm-up, four spaced-retrieval questions (5) → notes (10–11) → two worked examples with a Your Turn each (10) → **nine whiteboard questions**, question 9 written (the remainder, 10–20) → the **independent set**, six questions written in silence (6, ruling 21) → IXL, the last five minutes. Every wrong option on every multiple-choice item is a named error with its benchmark cited, in the Lesson Plan's checks for understanding and on the keys (§16 rule 4).

## Timing

<!-- timing table: generated by install_unit.py from the deck side-cars. Do not edit by hand. -->

| Lesson | Teaching (title, warm-up, notes, examples) | Whiteboard round | IXL | Total |
|---|---|---|---|---|
| 10.01 | 37 min | 11 min | 5 min | 53 min |
| 10.02–03 | 37 min | 11 min | 5 min | 53 min |
| 10.04 | 34 min | 14 min | 5 min | 53 min |
| 10.05 | 38 min | 10 min | 5 min | 53 min |
| 10.06 | 38 min | 10 min | 5 min | 53 min |
| 10.07–08 | 36 min | 12 min | 5 min | 53 min |
| 10.09 | 36 min | 12 min | 5 min | 53 min |
| 10.10 | 35 min | 13 min | 5 min | 53 min |

The whiteboard round is the remainder — 10–14 minutes across the unit — and the build refuses any plan whose remainder falls outside 10–20. Every plan totals 53 exactly. There is no shortened variant; short days are absorbed by the person in the room.

<!-- end timing table -->

---

## Standing decisions baked into these files

- **No partner or group work anywhere.** Math Nation's explorations and collaborations are taught from the front; its partner-discussion tasks are written whiteboard questions.
- **Calculators: allowed on everything, and nothing about them is printed on any student page.** The one exception the house style allows is the Reference Sheet's description of what the FAST platform provides (an on-screen scientific calculator) — that is a description, not a permission line.
- **Old-school textbook styling.** No commentary panels, no grey bars, no clip art. American spellings.
- **One point per lettered part, no partial credit**, with follow-through credit (ruling 19): a later part earns its point when the right operation is applied to the student's own earlier value, where that work is on the page. The key carries a `Scoring:` line under every question and a per-benchmark Score Tracker at the end.
- **The assessment is one paper, one class period** (ruling 51, 24 October 2026 — every A7 unit test is one period; the practice test's random draw is sized for it, ruling 49). No transfer items: a random set can only ask what the practice asks (ruling 49).
- **No benchmark codes on student pages.** The deck title slide and the keys and Lesson Plans carry them.
- **Opens cleanly in Google Docs.** Every document is a fixed-width table layout with no nested tables and a spacer after every block; every document and every slide is set in Lexend (a Google font), with FreeSerif for the bubbles only.
- **Every answer is re-derived by machine at build time.** Every item carries a `check` that sympy evaluates (variable bases as symbols); every multiple-choice distractor must name its error; every scientific-notation coefficient is scanned for the [1, 10) rule; the build refuses on any finding. The post-build suite (`checks.py`) then reads the rendered PDFs for off-page text, glyph coverage, Google-Docs layout rules and the timing plan.
- **Nothing here is taken from Math Nation.** The book was read for the unit's scope and the shapes of its test's questions only; every lesson and question is built from the benchmark text and the B1G-M. The plan and the review's rulings are in `Reference/`.

---

## Before the unit starts

- **Built in the order the rulebook asks (§16):** the test was settled first, from the benchmarks (MA.8.AR.3.1–3.5), and then the lessons were built to it. Math Nation's Unit 10 was read for scope and its test's item shapes only, and nothing is taken from it. The plan was read by a Barton reader and a FAST reader before any spec was written.
- **Where the class stands:** Unit 11 graphed a line from a table of values, called the number that multiplies x "the coefficient of x", and wrote a story as (the amount per 1) · x + (the start). Unit 7 taught y = px, its three tests and the word "linear relationship". The class has not heard "slope" or "y-intercept" before this unit.
- **Three words, each named once and then used every day:** rate of change (10.01), slope (10.02–03), with both "rise over run" and "the vertical change divided by the horizontal change" said, and y-intercept (10.05). A key accepts "4" or "(0, 4)" for a y-intercept.
- **Proportional is the special case:** a linear relationship is also proportional when y is 0 when x is 0, and its line passes through the origin. Two reasons are accepted everywhere: the value of y when x is 0, and Unit 7's "y ÷ x is the same for every pair". Deciding whether a table is linear at all waits for Unit 12.
- **The slope formula is words first:** "Slope is the change in y divided by the change in x. Subtract in the same order." The formula is shown once, in 10.02–03, and on the Reference Sheet, and no question needs its notation. From 10.02–03 on, every lesson has a table whose x-values do not go up by 1.
- **Which quantity is x and which is y is said in every question:** a table names its rows, a graph its axes, and a slope carries its unit as the y-unit per x-unit. An axis scale is not always 1, so students read the scales first and find a slope from coordinates, never by counting squares. A real-world graph is drawn in Quadrant I and starts at x = 0.
- **Slope-intercept form only:** y = mx + b, also written y = b + mx and with a context's own letters. There is no point-slope form and no standard form on the test. When no y-intercept is in sight, students substitute a point and solve for b. Graphing an equation in standard form (IXL 7MZ) gets one Notes block and one whiteboard question in 10.06, and the test never asks it.
- **Whiteboards read, and the Independent Set draws.** The handouts of 10.05 and 10.06 print empty grids, and question 1 of each is drawn in class with the teacher circulating. The test has two drawn graphs (questions 8 and 9b), and each key prints the graph and says which lines earn the point.
- **MA.8.AR.3.5 is one line at a time:** no question compares two lines' slopes or y-intercepts. F = 1.8C + 32 is printed whenever it is used and is never memorized. Lines of fit get one whiteboard question in 10.10 that explains itself, and none is on this test. Calculators are allowed and never mentioned, and the Reference Sheet is not used on the test.
- **Hand-off to Unit 12 (from 1 Feb):** 12.08–09 asks "Is it linear?" of tables, graphs and equations (MA.8.F.1.2 with MA.8.AR.3.1) and defines "function". This unit gave it "constant rate of change" and the name "linear function", said once in 10.04.
- **Hand-off to Unit 13 (from 22 Feb):** 13.06–13.09 teach scatter plots, lines of fit and their equations (MA.8.DP.1.3 with MA.8.AR.3.5). This unit's one whiteboard question in 10.10 reads such a line's slope, and nothing else.
- **Hand-off to the practice page (not built in this pass):** questions 8 and 9(b) need a part where the student draws a line.

Installed: 144 files from the build, plus this page and the Reference folder.
