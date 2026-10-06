# BUILDING A UNIT — the procedure, start to finish

*Written 20 September 2026 for whoever builds the next unit. It is explicit on purpose: follow
it in order, do not skip a gate, and when something here and your own judgment disagree, do what
this says and tell Croix why you wanted to differ.*

Read these first, in this order: this file; `SPEC SCHEMA.md` (the fields); `../reference/HOUSE
STYLE.md` §0, §1, §6, §9, §13, §13b (rulings 1–15) and §16; `../packages/A7 Unit 3 - Exponents
and Scientific Notation/00 - START HERE.md` (what a finished unit looks like); then open
`u3/l04.py` and `u3/unit.py` side by side with their PDFs in `out/u3/` and read them
together — that is the standard you are matching.

## 0. Rule 0, and what "done" means

> "math errors are unacceptable… the stuff that touches students needs to be completely
> mathematically sound. everything else is secondary… the second I get associated with bad
> math is the second I utterly fail." — Croix

Every number on every student page is re-derived by sympy from a `check` you write, and the
build refuses to run without one. That is the floor, not the ceiling: a check proves the keyed
value; it does not prove the item asks what you think it asks, that a distractor is the named
error, or that the wording is unambiguous. **You read every item as a student would, and you look
at every rendered slide and page.** "The checks passed" is never the whole answer.

**Nothing exists until it is committed.** `bash tools/push.sh "message"` after every lesson. A
build that is not pushed did not happen (README).

## 1. Session start (every session, ~5 minutes)

```sh
git clone https://github.com/croix18/croix18-windy-hill-a7.git windy-hill   # or pull
cd windy-hill && bash tools/setup_env.sh                                     # apt + pip + fonts, verifies
printf '%s' '<token from Croix>' > .github-token && chmod 600 .github-token  # git-ignored; never elsewhere
bash tools/check.sh                                                          # gates over every unit, kit manifest, due-date sheet, packages
cd a7/build && python3 build_all.py u3                                       # smoke test: rebuilds Unit 3, ends "checks: 0 findings"
```

`build_all.py` takes about ten minutes (LibreOffice renders every PDF). It is needed in a fresh
clone because the PDFs are git-ignored and `checks.py` wants a PDF twin for every document in
`out/<unit>/`; after that, build one lesson at a time with `build_lesson.py`. Run it in the
background and keep working if your shell has a time limit.

If the smoke test fails, fix the environment before touching content. Read
`../reference/GITHUB FROM A SESSION.md` before diagnosing any push problem.

## 1a. The kit, and changing it (4 October 2026)

`lib/`, `checks.py`, `gates.py`, the `build_*.py` drivers, `slotaudit.py`, `shuffle_choices.py`,
`contact_sheet.py`, `assets/` and `SPEC SCHEMA.md` are **the build kit — one code base for this
course and the on-level one**, published from `croix18/Windmill` (`kit/`), vendored here by
`tools/vendor_windmill.py` and listed in `KIT.sha256`. **They are never edited here**: `kitcheck`
(in `checks.py` and `gates.py`) refuses a copy that differs. To change the kit: edit `kit/` in a
Windmill checkout, run its `tools/check.sh` (the kit's tests, under a profile shaped like each
course), vendor into both course repositories, and rebuild a unit of each — a change is finished
when **both** courses rebuild at `checks: 0 findings` and nothing moved that the change did not
mean to move. What this course settles for itself is `course.py` (the profile: `python3 -m
lib.profile` prints it and marks what A7 sets); ours too are the unit folders, `install_unit.py`,
and this file. `python3 gates.py [uN]` runs every build gate over the specs in seconds, with no
rendering — `tools/check.sh` runs it before every push, and CI on every push.

## 1b. File names and folders (ruling 34, 4 October 2026)

No spec and no script types a file name. `lib/names.py` makes every one —
`A7 3.08 Writing Large Numbers in Scientific Notation - Slides.pptx`,
`A7 Unit 3 Exponents and Scientific Notation - Test - Key.docx` — from the spec's `code` and `title`
and from `course.py` UNITS, and `lib/packkit.py` lays the package out **by lesson** (`All Slides/`,
`Lessons/<N.NN>/` with that lesson's keys in `Keys/`, `Review/`, `Assessment/`, `Handouts/`,
`Reference/`). A lesson's folder is its **number only** (`Lessons/4.06/`) and a unit's zips carry no title: with the title in the folder too, paths ran past 255 characters as links and past Windows' 260 once a zip was extracted; Croix was asked and chose number-only (4 October). The installer refuses a path over 180 characters inside `packages/`. So: a lesson's `title` is its name everywhere; `code` keeps two digits; a thread day
carries `plan_code` (the plan's name for it, `T-A1`); **add a new unit's title to `course.py` UNITS
before building it**; and a new kind of document is a new word in `names.py`, not a string in a
builder. HOUSE STYLE §11 is the convention; `SPEC SCHEMA.md` "File names" is the detail. Units 1
and 2 (not buildable) were renamed and re-foldered the same day; every old name is in
`../reference/A7 Rename List 2026-10-04.csv`.

## 2. Intake — the Math Nation package

Croix uploads the unit as a zip, often split (`pkg.z01 … pkg.z06 + pkg.zip`). Put the parts in one
folder with matching names and join them: `zip -s 0 pkg.zip --out single.zip && unzip single.zip`.
Extract to **`/root/mn/unitNN/`** — outside the repository. Math Nation's pages are copyrighted
and never enter git; the `.gitignore` does not protect you, the location does.

Then make the text you will work from:

```sh
mkdir -p /root/mn/unitNN/st
for f in /root/mn/unitNN/**/*.pdf; do pdftotext -layout "$f" "/root/mn/unitNN/st/$(basename "${f%.pdf}").txt"; done
python3 tools/pdf_supertext.py "<pdf>" > out.txt      # keeps exponents as ^{…}; use for any page with powers
```

Read a page as an image (`pdftoppm -r 80 -f N -l N`) whenever the text is scrambled — two-column
layouts interleave, and the TE's boxed answers often come out as images only.

Also open, for the unit: `../reference/A7 Scope and Sequence 2026-27.md` (which book lessons
merge, which threads are woven in, the dates), `../reference/ixl_skills_by_lesson.json` (IXL
names and codes per book lesson — never type a code from memory), the benchmark text in
`../reference/Florida BEST Grade 8 - Source of Truth.md`, and the B1G-M notes for every benchmark
in the unit in `../reference/A7 B1G-M Reading Notes.md` (the misconceptions you will name, the tasks
and items the guide expects).

## 3. Audit first — and send it before you build anything

Work **every** problem in the package: student pages, practice, homework, additional practice,
assessment, and the keys. Use sympy, not your head, for every value. Write
`a7/reference/A7 Unit N <Title> - Audit.md` with the same sections as `A7 Unit 3 Exponents and Scientific Notation - Audit.md`:

1. Bottom line. 2. Defects that are student-facing or in a key (numbered D1, D2 … with page,
what it says, what is true). 3. Teacher-facing slips. 4. Conflicts with the settled rules (partner
work, videos, homework wording — not errors, just what changes). 5. Capcheck — anything beyond
the benchmark boundary (fractional exponents, a topic the guide excludes). 6. What the B1G-M
expects that the book never asks (these go into your banks). 7. Structure check against the
scope and sequence. 8. Judgment calls — **only genuine ones**. 9. Inventory of what was checked.

Keep a working log beside it (`UNIT N AUDIT - working log.md`) with every value you verified, so
the next reader can see the denominator. Commit both, **send the audit to Croix, and ask the
judgment calls in one message**. If he is not around, state your default for each call in the
audit and proceed on it — he ruled on Unit 3 this way ("mix of Math Nation's problems and original
ones; alignment with the standards first and foremost", and "no video warm-ups") and those two
defaults stand for every unit. Do not ask about anything the rulings already settle.

## 4. Build one lesson at a time

For each row of the scope and sequence (a book lesson, a merged pair, or a thread day):

1. **Copy the nearest existing spec** (`u3/l04.py` for a skills lesson, `u3/l08.py` for one with
   real-world quantities, `u3/l07.py` for a thread day) to `<unit>/lNN.py` and change every
   field. Fields are documented in `SPEC SCHEMA.md`. Do not leave a field from the old lesson in
   place because it "still fits".
2. **Decide the items before the prose.** Warm-up: four questions, one per retrieval band
   (yesterday / last week / last unit / prior-grade prerequisite — the last one is the
   prerequisite *this* lesson needs). Notes: three slides that teach the idea from the front,
   each with an `OFF:` line — the sentence the teacher says. Two examples, each with a Your Turn.
   Nine whiteboard questions: 4 free, 2 multiple-choice diagnostics (every wrong option a named
   error with a cite), 2 more free including one working-backwards / unknown-exponent shape, and
   #9 written. Bank: 12–13 questions with a **variation structure you can state** (one move each,
   then two laws, then backwards, then a setting, then the diagnostic mc, then a select-all) —
   the `te.variation` field is where you state it. Additional: the same structure, new numbers,
   position for position.
3. **Mix the book's items with original ones.** A book item is reused only if the audit verified
   it; a defective item is never reused, and the TE says so by page. Original items exist to
   cover what the guide expects and the book lacks (§6 of the audit). Every distractor is one of
   the B1G-M's named misconceptions or a named procedural slip, with the cite in brackets.
4. **Write the `check` for every item as you write the item**, from the mathematics, not from
   the answer you typed. If the check disagrees with your answer, the check is usually right.
5. `python3 build_lesson.py <unit>/lNN.py` — it runs mathcheck, distractorcheck and capcheck and
   refuses on any finding; then it writes the six documents and their PDFs to `out/<unit>/`.
6. `python3 checks.py out/<unit>` — must end `checks: 0 findings`. Every finding is a defect;
   never argue with one, fix the content (or, if the check is wrong, fix the check in a separate
   commit that says why).
7. **Look at everything.** `python3 contact_sheet.py "out/<unit>/A7 N.NN <Title> - Slides.pdf"` and view
   `/tmp/sheets/…png`; then the bank key, the additional key and the TE at 45 dpi in a grid; then
   any slide that looked crowded at 60–80 dpi on its own. You are looking for: a title-slide box
   that wrapped, a gloss that ran into the margin or the math, a table cell that wrapped, a notes
   heading on two lines over the first math row, an answer that took three lines, a question
   split across pages, anything ugly. The checks do not see ugliness. Fix the spec, rebuild, look
   again.
8. Read the TE's whiteboard table and the bank key **as Croix's substitute would**: does every
   wrong answer have its reason, does every `why` say something a student would need, does the
   `read_first` tell the truth about what was kept and dropped?
9. `bash tools/push.sh "A7 Unit N: lesson N.NN (benchmark) — one line on what is notable"`.

Do not batch lessons before the first push. One lesson, checked, viewed, pushed; then the next.

### Common build failures and what they mean

| message | cause | fix |
|---|---|---|
| `mathcheck … = A but keyed B` | your answer is wrong, or the check expression is | re-derive by hand; fix whichever is wrong; never "fix" the check to match the answer |
| `UNSOLVED (name 'e' is not defined)` | a variable letter that is not a symbol | use only `a b c d k m n p q r s t w x y z` as bases |
| `$latex$ in a board's option` | a whiteboard multiple-choice option written with `$…$` | a slide draws its options as plain text; use unicode (12²(1.25) + 38). The .docx surfaces do render `$…$` |
| `select-all has N wrong options but only M clauses asserting an option is NOT the target` | a select-all whose wrong options are not checked against the target value | give each wrong option its own `("true", "<option> != <target>")` clause. This is the check that catches an option that is secretly correct — a student selecting it would be marked wrong for being right |
| `option B equals the keyed answer … a student who picks it is right` | two choices are the same number, and one of them is keyed wrong | change the option, or the question: if the item is about FORM, the question must say so ("written in scientific notation", "to the correct number of significant digits") and the item gets `form_only="B"`. "Which expression is equivalent?" with an equal option is a wrong key, not a trick |
| `wrong options C and D are the same number` | on a one-answer item, two distractors with one value — a student who computes it rules out both | replace one with a distractor from a different named error. On a select-all this is allowed (each option is judged alone) |
| `form_only=B but the question never names the form` | a form exemption on a question that asks for a value | reword the question to name the form, or drop `form_only` and fix the option |
| `sig() needs a plain numeral written out` | `sig()` was given an expression rather than a numeral string | `sig('0.00470')`, in quotes: significant digits depend on how a number is WRITTEN, so the argument is a string and not a value |
| `option C: no named error with a benchmark cite` | an mc distractor without `errors["C"]` containing `[…]` | name the error the student made and cite the benchmark or B1G-M |
| `scientific-notation coefficient 20.0 outside [1,10)` | a coefficient like `20 × 10⁵` in an item not tagged | if the item is ABOUT the rule, put `not_sci=True` as its first key; otherwise fix the item |
| `adding or subtracting 10^3 and 10^6 — a gap of 3` | MA.8.NSO.1.5 limits + and − to exponents within 2 | rewrite the item's numbers; `not_gap=True` only if the item is ABOUT the boundary |
| `√250 — MA.8.NSO.1.7 is perfect squares up to 225` | a radicand outside the benchmark's list | use a perfect square ≤ 225 or a perfect cube in −125..125; `not_bound=True` for a Unit 2 estimation retrieval item, with the reason in its `source` |
| `radicand '…' is not plain arithmetic on integers` | capcheck could not reduce the radicand | work it by hand; if it is sound, tag `not_bound=True` and say why |
| `line runs off the slide (14.7 in)` | a mixed text+math row too wide | split the row, shorten the words, or move the math to its own row |
| `every single-answer item is keyed A — the key is guessable` / `select-alls key the first options` | the specs were written answer-first (correct=0) and printed in that order; students noticed on 3 Oct 2026 | write new items answer-first if you like, then run `python3 shuffle_choices.py <unit>` ONCE before the first build: it permutes each item's options in the source, re-keys `errors`, re-letters `answer`/`form_only`, remaps letters in the item's own teacher prose, and prints HAND-CHECK lines for letter references elsewhere (a Teacher Edition saying "a board full of B on Q5") — fix those by hand. Never run it twice on the same file; the gate `balancecheck` keeps the spread from then on |
| `slot colour: an exponent sits on '…', which is not a base` / `…with nothing to its left` | a coloured surface (notes, worked row, reveal) whose layout the base/exponent reader cannot place — HOUSE STYLE §2a | rewrite the expression so each exponent sits on a letter, a numeral or a bracketed group; never teach the reader a guess |
| `slot colour: a radical set small` | a root index (`\sqrt[3]{…}`) on a coloured surface — an index is not an exponent | move the root to an uncoloured surface, or write it without the index |
| `pdftwin: … - All Slides.pptx differs from A7 3.04 … - Slides.pptx at its slide 16` | a lesson was rebuilt on its own and the whole-unit deck was not | `python3 build_unit.py u3/unit.py` (it rebuilds the unit deck from the specs) |
| `text box runs into the footer … Answer it.` on a multiple-choice board | a tall display-size fraction above four options (slide fractions are set with `\dfrac` since 27 Sep 2026, so a `\frac` board is ~0.4 in taller than it was) | the placer clamps the prompt/answer line above the footer; if the options themselves collide, put the question on one `text` row or shorten the latex |
| `box crosses the footer` / `math into footer` | too many rows on one slide | fewer rows, or split into two notes slides |
| `table cell wraps out of its row` | a notes table's cell is too long for its column, and a wrapped second line draws outside the border | shorten the cell, widen the column, use fewer columns, or move the words into an `items2` line under the table |
| `plan does not fit … leave whiteboards 22` | the fixed minutes are too few/many | adjust `min` on notes/examples so the remainder lands in 10–20 (aim 15–19) |
| `title-slide line does not fit its box` | `yesterday` or `today` wider than the box, measured with the font | shorten the line (seven shipped lines sat on the box's edge until 4 October) |
| `ruling 28 — IXL code X is not in this course's IXL plan` / `the plan lists … and the slide does not` | an `ixl` entry that is not the plan's skill, code or lesson | the skills and codes are `../reference/ixl_skills_by_lesson.json`'s, via the spine; never type a code from memory |
| `Unknown symbol: \le` | mathtext, not TeX | `\leq`; see the LaTeX paragraph in SPEC SCHEMA |
| `docscan: calculator line on student surface` | the word calculator on a student page | "a computer displays 3.5E9"; the TE may say calculator |
| `docscan: benchmark code on student surface` | `MA.…` on a student page | move it to the key/TE |
| `glyph: … U+207D` | a character with no glyph in the deck/doc fonts | use plain characters; superscript digits and ⁻ ᵐ ⁿ are fine |
| `offpage` / `slidefit` findings | text outside the page/slide box | shorten; view the page |
| `overlap: text on text` / `figure on text` | two slide elements drawn on each other, found in the rendered PDF | move one; a placer that sets its own `y` must leave room for what came before |
| `imagedrift: … not in the figure library` | a document embeds an image that is not a current `figs/` file — an older rendering or an orphan | rebuild the document; never edit the index by hand |
| `suitecheck: …` | HOUSE STYLE's `suite:a7` tables disagree with what runs | edit the table in HOUSE STYLE (its A7 block is maintained from this side) and tell Croix, who relays it to M7 |
| `ruling 28 — an IXL skill is marked optional` | an `ixl` entry carrying "Optional" or "Also consider" | every listed skill is required; drop the words. A run of the same skill across two lessons uses `ixl_due` (SPEC SCHEMA) |
| `footer: '…' sits below the footer rule` | a notes line sized for one line wrapped to two and hangs past the rule | shorten the `items2` line, or drop a math row from that notes slide |

## 5. The unit documents, the manifest, the package

> **Ruling 41 (5 October 2026, evening): there is no console and no HTML deck any more.** Croix:
> *"I like running my files in deckhand because I can use deckhands tools like the pen and timers
> and stuff. So stop building the html. Keep it as slides files."* A deck is its `Slides.pptx`: he
> uploads it to Drive, it opens as Google Slides, and he pastes the link into Deckhand's Slides
> card. `course.py` says `HTML = False`; `htmlcheck` refuses an `.html` deck left in `out/`; the kit
> keeps the HTML code and `HTML = True` brings it back. A slide names only fonts Google Slides has
> (Lexend; Arial for the arrow; Times New Roman bold for a π in words). **Nothing in the build can
> open Google Slides** — the layout is checked in LibreOffice's PDF of the same file, so a
> screenshot from him of a line wrapping in Slides is evidence the build cannot see. Gone with
> the console: Today, period bookmarks, the stepped reveal, the whiteboard tally, the as-run log
> from the panel (a day is logged from the phone view of the plan). Where this file says
> "console" or `.html` below, read it as history. Send him the `.pptx`.

**The whole-unit deck.** `build_unit.py` also writes `A7 Unit <u> <Title> - All Slides.pptx` (+ PDF): a cover,
a contents slide whose rows jump to each lesson, then every lesson's slides in the manifest's
teaching order, each lesson numbered from 1 exactly as its own deck and its Teacher Edition number
it. It has no side-car (the minutes live beside each lesson's deck). `checks.py` compares it to the
lesson decks slide for slide, so **after rebuilding any one lesson, run `build_unit.py` again**.
**After any change to a coloured expression, run `slotaudit.py <unit>` and read it** (HOUSE STYLE §2a).

**The console (the unit's `.html`, 3 Oct 2026).** `A7 Unit <u> <Title> - All Slides.html` is not a deck with a
contents page; it is the day wrapped around the slides (`lib/consolekit.py`, Room Coordination Plan
phase 3). It opens on TODAY: the period read from the bell schedule (Deckhand's, via Windmill's
spine), the plan's lesson for the date, this period's bookmark, the room's word from Tally if any;
Resume / Start / Choose. A RAIL lists the lesson's segments with the Teacher Edition's minutes (the
same grouping as `tekit.plan_from_sidecar`; the whiteboard block takes the remainder); the bar shows
the segment, how far ahead or behind the plan the clock says, the period and the minutes to the
bell. On a board the rail becomes the ROUND: a timer (30/45/60/90 s), the answer slide veiled until
Space or R, and tally tiles — the letters for a multiple-choice board with the keyed one marked and
the spec's error key under each, right / partly / not yet otherwise; hold a tile to take one back.
Everything it records is the room's `panel` part (bookmark per period, tallies with benchmark and
misconception keys) in the browser's store, the shape Deckhand will publish. Keys: Space/→ advance
(first press on an answer slide lifts the veil), ← back, 1–9 jump to that board, L rail, T timer,
R reveal, Esc Today, P print. `#period=3` in the URL (Deckhand's hand-off) sets the period; `#L=3.06`
opens a lesson; `#s=17` a slide; the URL is never rewritten, so a reload returns to Today and Resume.
Nothing teacher-only is drawn on the slide surface (ruling 12). The per-lesson `.html` decks stay
plain decks. `tools/vendor_windmill.py` brings `room-reader.js`, `spine.js` and `benchmarks.json`
from the Windmill checkout into `assets/windmill/` — rerun it after Windmill changes; `VERSION`
there says which commit the decks carry.

**The HTML decks.** Every deck is written twice from the same spec and the same `_fill_deck`:
`.pptx` (deckkit) and `.html` (htmlkit) — one self-contained file per deck, the math typeset in
the browser by KaTeX from the spec's own LaTeX, Schola from the inlined fonts, arrow keys or a
click to advance, `#17` in the address bar to open at slide 17, one slide per page when printed.
There is no PDF twin of an `.html`; `install_unit.py` puts it in Slides beside the `.pptx`. The
slot colours are painted by the page's own script from KaTeX's DOM (`.msupsub` is the exponent,
what it sits on is the base) and `checks.py` `htmlcheck` opens every deck in a real browser and
reads the colours back against `slotaudit.show()`'s reading of the LaTeX, so the two renderers
cannot disagree about which slot is which without failing the suite. The vendored KaTeX and font
files live in `assets/` with the script that regenerates them (`assets/make_assets.py`).

1. Copy `u3/unit.py` to `<unit>/unit.py`. Reference Sheet: every tested skill with its method,
   one worked example and the mistake that costs the most points, organized by topic; say what
   the FAST provides and what must be memorized (Source of Truth Part 3). Unit Review: unscored,
   parts by lesson, **one SSDD block** (four lettered parts on one surface, label on the key
   only). Unit Assessment: two periods, sections by benchmark, one point per lettered part,
   numbering straight through; the `total` and `tracker` you declare are asserted against the
   items. `python3 build_unit.py <unit>/unit.py`, then `checks.py`, then look at every page.
2. Add the unit's title to `course.py` UNITS (the package folder and every unit-wide file are named
   from it). Copy `u3/manifest.py` to `<unit>/manifest.py`; fill the lesson table (the "line that carries
   the day" is each lesson's `te.lives` idea in ten words), the assessment days, the notes.
3. `python3 install_unit.py <unit>` — deletes and rebuilds the package folder and
   writes `00 - START HERE.md` with the timing table read from the decks.
4. `python3 build_all.py <unit> --install` — rebuilds everything from the specs, runs the suite
   (0 findings) and reinstalls the package — then push. This is the shipping gate.
5. Regenerate Croix's master sheet so the new unit's days get their links and details:
   `python3 ../../tools/master_sheet.py`, then the xlsx skill's `recalc.py` on
   `../reference/A7 Master Sheet 2026-27.xlsx` (0 errors), then
   `python3 ../../tools/check_master_sheet.py` (0 problems). Push, and send Croix the new file.
   **Its links open Google Drive and are live (4 Oct 2026 — GitHub is blocked at school, and
   Croix asked not to depend on a rebuild):** a link cell looks its document's Drive address up in
   the workbook's hidden Drive tab, which a script in HIS Google account refills every hour; the
   fallback is a Drive search for the file's exact title. The same script copies everything this
   repository publishes into his Drive and makes the live Google Sheet. So: **push, and it reaches
   him; there is nothing to upload or send.** Windmill `drive/README.md` is the whole arrangement;
   `windy-hill-m7` `NOTES.md` (top section) says what it means for the generator and the check,
   which are the same here. `python3 ../../tools/test_live_links.py` exercises the looked-up half.
   Since version 3 of that script (4 Oct, late) a new edition of the master sheet goes into the
   SAME Google Sheet — its address stays — and his IXL ticks and notes are written back by lesson
   (keyed by the tracker's "Lesson(s)" text and which occurrence it is: keep that column stable).
   The About tab says so, and `check_master_sheet.py` requires it to. Only the yellow cells are
   carried. The script fetches the consoles and master sheets first, then the rest.

**Ruling 37 (4 October 2026, night) — no comments on a slide.** Croix: *"on all slides remove
the comments in the boxes and in parenthesis. If a problem is in parenthesis, it should be pulled
out into the main text … Remove it everywhere."* The title slide has no yesterday/today box; no
slide has the small grey italic line under its rules; an Example's whole problem — story, givens,
question — is in `prompt`. A spec's `sub` is the slide's label in the Teacher's Edition only; a
question a worked slide asks the room is its `lead`. HOUSE STYLE §13b(xvii); the kit's
`SPEC SCHEMA.md`. Units 3 and 4 were rebuilt that night with no spec changed (every `sub` here
was already a label). The same night the console's slide placement was fixed (it was wrong at
every window size but one) and `htmlcheck` began measuring it.

**Ruling 37, widened the same night.** *"But also those comments"* … **"Remove both."** No hint
under "Answer it.", no remark beside a worked step, no line above a reveal's answer: `hint`,
`gloss` and a worked row's remark stay in the spec and are on no slide. An Example's `ask` is
the problem's own question ("Find the value.") or absent — never a direction to the room.
A7's specs needed no change; Units 3 and 4 were rebuilt.

**Ruling 21, amended the same night — the independent set is on the board.** *"The individual
review portion of the slides needs to put the problems on the board."* The Independent Set slide
now shows the six questions (typeset, the type stepping down until they fit); the printed page and
its key are unchanged. Write stems that fit: six on one slide at 16 pt or larger, or the build
refuses.

**Rulings 39 and 40 (4–5 October) — steps on every answer slide; slides in Lexend.** Every
board and every Your Turn carries `steps=[…]` (one to five rows, words with `$latex$`), drawn on
its answer slide and worked by the build. Slides are set in Lexend (the kit installs it);
printed documents are unchanged. **State on the morning of 5 October: steps are written for every lesson of
Units 3 and 4** (16 lessons, 176 answer slides) and `course.py` says `STEPS = "required"`. The
pattern for Unit 5: each row is one line of the working with the law visible in it
(`$x^{5} \\cdot x^{8} = x^{5+8} = x^{13}$`), a short label where it names a part ("The a's:",
"Divide the powers:"); the build checks every equality, numeric or in letters. Under a tall
problem two tall rows are the limit — "cannot hold its steps" means write fewer. Since kit `9b1f030` (5 October; `62cc4d5` fits one slide at a time as it comes on screen — the first way made the Unit 3 console take 5.7 s to open; `40db72a` puts an answer slide's working under the console's veil with its answer — for a day the steps showed as the slide came on) a line of working is one size (label and numbers alike), the HTML decks and the console set a too-tall slide smaller so nothing meets the footer (14 answer slides in Units 3–4, at 79–98%, each with its question slide; `htmlcheck` refuses under 75% — write fewer steps), and a slide's mathematics and figure labels are Lexend too (π stays the textbook's; `\cdot` is Lexend's raised dot; a variable l is the script ℓ — the kit swaps them, specs do not change). `steps` may pass through a form that is not yet scientific notation (matching the powers); an answer may not. Before a rebuild, rehearse it: `python3 /root/windmill/tools/dry_run.py /root/windy-hill/a7/build u3 u4` runs every gate of `build_lesson`, lays out both decks and runs the real `htmlcheck` in two minutes, without LibreOffice and without writing here — the HTML check otherwise runs last in a 15-minute build. HOUSE STYLE (rulings 39, 40);
`SPEC SCHEMA.md`.

**Ruling 38 (4 October 2026, later that night) — a figure's labels can be read, and are true.**
The kit refuses a figure in which a line runs through a label, and a spec in which a figure and
its own words use different units (`kit/SPEC SCHEMA.md` § Figures; HOUSE STYLE §13b(xviii)). Place
a label beside a line with `off=(dx, dy)` in ems, never by a step in the figure's units; print a
length that follows from the others only as what it truly is. Found in M7 Unit 4 (13 struck
labels, three impossible slanted sides, one wrong unit); A7's Units 3 and 4 were surveyed and are
clean. This is the rule to write Unit 5's figures by.

## 5a. Geopardy (the review game, formerly Boards Up) — planned, not built (3 Oct 2026)

Croix's review game Geopardy! lives in a separate repository, `croix18/Geopardy` (engine in `engine/`, one
JSON file per unit in `units/`, `tools/build.py` makes a single-file game, `tools/check.sh`
playtests it headless; read its `docs/HANDOFF.md` first). Its unit format is `categories[] →
questions[] {q, a, work}` with `$…$` math, five tiers per category, easiest first, plus a Final.
Every A7 bank item already carries a `check`, so a generator here can write a unit file from the
specs — categories from the manifest's lessons, tiers from the bank's ordering — and only
mathcheck-passing items reach the game. Agreed with Croix 3 Oct: possible, wanted later, not now.
His other tools: **Cadence** (the item engine, `croix18/Cadence`), **Deckhand** (the panel's classroom
OS, `croix18/Deckhand`) and **Tally** (`croix18/Tally`, his command hub for grades: IXL Score Grids and
Focus gradebooks → one grade per unit). Tally is the ecosystem's source of "where are we": it keeps the
unit each course is working in at `localStorage["tally.v1"].settings.currentUnit` as `{acc: N, on: N}`
(set by the "Working in" selector on the class bar; sections are keyed `period-N` with `prep` acc|on).
Tally's store holds real grades, so no other tool reads `tally.v1`; the agreed design (3 Oct) is that
Tally publishes a small name-free handoff key on save — current unit per course and, later, class-level
counts per benchmark — and the lesson deck, Cadence, Geopardy and Deckhand read only that, falling back
to the master sheet's plan when Tally has not been opened on that device. All of this is planned, not
built.

## 6. The final report to Croix

One message, in this shape (see the end of the Unit 3 session for the model):

- What was built, by lesson code, with the book/original mix and the guide shapes added.
- The book defects not reproduced (by number, page) and any new defect found while building.
- Anything you changed in the toolchain and why (a check that was inert, a new field).
- **Judgment calls you made — each one reversible, each stated in one line** — and nothing
  that a ruling already settles.
- What is still open.

Send the START HERE, the Reference Sheet PDF and the assessment key PDF with it.

## 7. Never

- Never put a Math Nation page, PDF, docx or pptx in the repository.
- Never write an answer without a `check`, and never use `ack` to skip one.
- Never print a benchmark code, the word calculator, "homework", or partner/group work on a
  student page; never a grey bar, a commentary panel, a speaker note, a video slot, a study
  guide, partial credit, or a point value that is not 1 per lettered part.
- Never edit a file in `a7/packages/` by hand; edit the spec, rebuild, reinstall.
- Never edit `HOUSE STYLE.md` except to record a ruling Croix actually gave, quoted, dated.
- Never put the GitHub token anywhere but `.github-token`; never trust `git push`'s message —
  `push.sh` compares the remote head and says `pushed:` or `PUSH FAILED`.
- Never leave a lesson unpushed while starting the next one.
- Never rescale a plan by trimming the whiteboard round below 10 minutes or IXL below 5.

## 8. State of the work — 4 October 2026 (read this before anything else)

**First, 5 October evening:** ruling 41 — no HTML, no console; the deck is the PowerPoint, run as
Google Slides in Deckhand (the boxed note at the top of §5). Rulings 39 and 40 are complete for
Units 3 and 4 (steps on every answer slide; Lexend for words, mathematics and figure labels).

**4 Oct, later — one kit for both courses; everything below is pushed.** Croix asked for M7 to be
adapted "to a7 and the family", and chose all four parts. What that changed HERE:

- **The build library is no longer this repository's.** `lib/`, `checks.py`, `gates.py`, the
  drivers, `slotaudit.py`, `shuffle_choices.py`, `contact_sheet.py`, `assets/` and `SPEC SCHEMA.md`
  are the shared kit, published from `croix18/Windmill` (`kit/`) and vendored here (§1a). Ours:
  `course.py`, the unit folders, `install_unit.py`, this file. The earlier note below that "this
  repository's copies are the masters" is superseded: **Windmill's `kit/` is the master.**
- **A7's output moved only where it was meant to.** Against the pre-kit build: Unit 3 — 100
  documents identical in structure, 7 differ (3.03's title line; three two-line answer boxes now
  sized for two lines); Unit 4 — 53 identical, 14 differ, all of them the six title-slide lines
  below and the unit deck that repeats them. Both units rebuilt at `checks: 0 findings` (eighteen
  checks) and reinstalled.
- **Seven title-slide `today` lines were too long for their box** and sat on its edge in the
  shipped decks (3.03, 4.01, 4.02, 4.04, 4.05, 4.06, 4.07). Shortened; the builder now measures
  the line with the font and refuses one that does not fit.
- **New for both courses:** the IXL plan as a gate (every skill and code on a slide is
  `ixl_skills_by_lesson.json`'s, via the spine — Units 3 and 4 passed as they stood; M7's Unit 5
  did not); options compared as numbers with their units; the letters an item's words name held to
  its key; the keyed letters balanced across a unit; a figure's height refused if it ends outside
  the figure; `tools/check.sh` before every push and in CI (`.github/workflows/check.yml`).
- **Word boards:** a board's `hint` now always shows when it has one. A7's sixteen word-board
  hints were removed from the specs so those slides stay exactly as Croix approved them.
- `install_unit.py` takes the unit (`u3`) as well as the manifest path; `build_all.py uN --install`
  calls it that way.
- **Family:** the M7 repository now has this one's layout (`m7/build`, `m7/reference`,
  `m7/packages`); Geopardy gained two M7 games; Windmill's handoff has the kit's takeover notes.
- **4 Oct, later still — one way to name a file (ruling 34; §1b above, HOUSE STYLE §11).** Every
  file now carries its lesson's title (`A7 3.08 Writing Large Numbers in Scientific Notation -
  Slides.pptx`), unit-wide files carry the unit's (`A7 Unit 3 Exponents and Scientific Notation -
  Test - Key.docx`), the whole-unit deck is `All Slides` (it was `Unit Slides`), and **packages are
  laid out by lesson** — `Lessons/<N.NN>/` (the number only: paths with the title twice broke the
  master sheet's links and Windows' path limit; Croix chose number-only) with that lesson's keys in
  `Keys/` — instead of by
  type with a `PDFs` mirror. Units 3 and 4 were rebuilt under the new names at `checks: 0
  findings`; against the build before the renaming, Unit 3's 107 documents are identical in
  structure except the console's index (it gained each lesson's plan code). Units 1 and 2 were
  renamed and re-foldered, nothing inside changed. `a7/unit03/` and `a7/unit04/` are gone: their
  audits and bank files are in `a7/reference/` under unit names. The master sheet's links follow
  the new layout, and **no link in it may be longer than 255 characters** (Excel's HYPERLINK takes no
  more and LibreOffice cuts a cell's link there on save — it did, silently): `tools/master_sheet.py`
  links a document whose own address is longer to its lesson's folder and the cell reads "in
  folder" (19 links, all in Units 1–2); `tools/check_master_sheet.py` holds every tab to this, reads
  what the next commit will hold (not HEAD), and now runs in `tools/check.sh` and in CI. Units 1–2
  are zipped by `tools/zip_package.py`. Every old name is in `../reference/A7 Rename List 2026-10-04.csv`.
- **4 Oct, night — the plan follows the class (ruling 35; HOUSE STYLE §13b(xvi)).** Croix: "I need
  the plan to be fluid and adjust on the fly." **The dates of this course are not typed anywhere any
  more**: `tools/scope_calendar.py` builds the year's sequence (PLAN) and the kit's engine
  (`lib/flow.py`) lays it on the school days that `../reference/A7 As Run 2026-27.csv` leaves. His
  rule when the class is behind: push everything back — flex and spiral days absorb the loss first,
  then tests move to the next Monday or Thursday.
  **When he says a day went to something else**: add a line to the as-run CSV (`review`, `off`, or
  the code of the lesson the class began that day; his words in a `#` line above it) → `python3
  tools/scope_calendar.py` (it writes the scope and sequence and the IXL due-date sheet) → read him
  the scope document's last section → in Windmill `python3 spine/spine.py --a7 … --m7 …`, check,
  push → here `python3 tools/vendor_windmill.py`, `python3 tools/master_sheet.py` with its
  recalculation and check, rebuild the units being taught (`build_all.py uN --install`), push, send
  him the consoles. Windmill's `HANDOFF.md` has the whole story and what is not done.
  **The log today**: Friday 2 October was an extra review day; Monday 5 October is T-A1 (the deck's
  3.T1) — two days behind, so Thursday 1 October stands as "a day off the plan" the log does not
  explain; state tests on Thursday 8 October, Thursday 14 January and Monday 1 March take every
  period. **What that moved**: Unit 3's test 8–9 → **15–16 October (now in Q2)**, Unit 4's 22–23 →
  29–30 October, and so on until Unit 10; **five of the seven flex days are absorbed, two are left;
  content still ends 30 April.** He has been told.
  The console offers each period its next lesson, takes a day marked review or no class and says
  when the unit's test now falls; the master sheet reads the same layout (two new day codes, `extra`
  and `off`).
- **Open for Croix:** the teacher's edition and lesson plan differ in format between the courses
  (profile `TE_STYLE`, `PLAN_STYLE`) — converging them is his call. Everything in "Pending" below
  still stands.

Where things stood at the end of the 3 Oct session:

**Shipped today, all pushed (HEAD e9db9ff).** Units 3 and 4 rebuilt: every multiple-choice answer was
A (students noticed) — spread by `shuffle_choices.py`, keyed letters now vary (gate `balancecheck`);
the ruling-22 word boards rewritten so the ask names a thing in the story (§4 and HOUSE STYLE);
the colour renderer's fraction bars fixed (check `slotgeometry`); every deck also as `.html` with
KaTeX (check `htmlcheck`); the unit `.html` is now the **console** (§5 above: Today from the bell,
rail with minutes, pacing, the whiteboard round with timer, veil and tally, per-period resume, the
room code). Windmill vendored into `assets/windmill/` (`tools/vendor_windmill.py`).

**The ecosystem.** Croix's tools — Deckhand (the panel), Cadence (items), Tally (grades, the source
of the current unit), Geopardy (review game, renamed from Boards Up today) and the two Windy Hill
builds — coordinate through **Windmill** (`croix18/Windmill`: the spine = the year's plan as JSON,
the room contract, the reader, the room codes, the conformance test). The whole design, the per-tool
changes, the spiral rule and the build order are in the *Room Coordination Plan*, a Claude doc:
https://claude.ai/code/artifact/9db84d04-9444-48c4-adad-9c68905eefd8 (read it with the docs tool).
Croix's standing instruction for it: "Keep it over engineered. I want everything." Data tiers:
open (counts, codes, times) rides every road; roster (first names, seating) rides the Drive file or
encrypted; standing (grades, scores, FAST) never leaves Tally.

**Pending, in order.** (1) Monday 5 Oct: Croix runs the four panel tests (`Windmill/tests/room-test/`,
"READ ME FIRST.txt"); the results choose the default road. (2) Tally's Publish button (writes
`room.js` to the Drive folder; both codes; the Apps Script post). (3) Deckhand: room code field, Drive
folder pick, Geopardy card beside the Cadence card, settle-in hands off to the console with
`#period=N`, the `panel` writer. (4) Console phase 2: "another one" from build-time verified variants,
the teacher-note overlay (held key), pacing actuals per segment. (5) Cadence: Today (the spiral rule),
class sets from the room, Export a Geopardy board. (6) The loop: exit tickets → room → Tally's heat
map; phone remote; room history; pacing truth; simulator; digest. Also still open: Unit 5 build (needs
Math Nation Unit 5), IXL/Focus import for the master sheet, rulings 16/17/23/24 from M7.

**Assumptions that need Croix's word** (also in Windmill's HANDOFF): periods 1 and 3 accelerated,
2/4/5 on-level, 6 planning; the holidays in both calendars are unverified against the district PDF.

**4 Oct, early.** M7 got the HTML decks and the console (its own fork of `htmlkit.py`/`consolekit.py`;
this repository's copies are the masters — change here first, then port). Two fixes came back from
that port: `rich()` treats `\$` as a literal dollar sign, and `choices()` gives long options the full
width with the type stepping down. M7's `htmlcheck` also found a PowerPoint defect its suite could not
see (an option wrapping over the one below); A7's `overlap` check guards that here. If the session
ends: everything is pushed; the builds are regenerable with `build_all.py u3 --install` / `u4`.

**Tokens.** Four PATs were pasted into the 3 Oct chat; all are to be rotated. `.github-token` here
holds the A7 token; Windmill's checkout holds the Windmill token (it reaches every repo).

## 8a. Open items carried forward (20 September 2026)

- Retroactive coefficient scan of the Unit 1–2 banks (the scan was inert until 20 September;
  those banks were built under the old toolchain and have not been re-scanned).
- PM2 / PM3 dates in the scope calendar when Croix has them.
- Units 1 and 2 were built by the earlier JavaScript toolchain that was lost with its container
  (README). Their packages are shipped and final; they cannot be rebuilt from specs. Any fix to
  them is a hand edit of the shipped .docx/.pptx plus its PDF, recorded in the package's
  Reference folder — the only place hand edits are allowed.
- The Grade 7 on-level course (M7) has its own tree and its own session; rulings are shared
  through `HOUSE STYLE.md`'s exchange mechanism (its header explains).
