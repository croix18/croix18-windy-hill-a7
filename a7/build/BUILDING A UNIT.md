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
cd a7/build && python3 build_all.py u3                                       # smoke test: rebuilds Unit 3, ends "checks: 0 findings"
```

`build_all.py` takes about ten minutes (LibreOffice renders every PDF). It is needed in a fresh
clone because the PDFs are git-ignored and `checks.py` wants a PDF twin for every document in
`out/<unit>/`; after that, build one lesson at a time with `build_lesson.py`. Run it in the
background and keep working if your shell has a time limit.

If the smoke test fails, fix the environment before touching content. Read
`../reference/GITHUB FROM A SESSION.md` before diagnosing any push problem.

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

Also open, for the unit: `../reference/A7 SCOPE AND SEQUENCE 2026-27.md` (which book lessons
merge, which threads are woven in, the dates), `../reference/ixl_skills_by_lesson.json` (IXL
names and codes per book lesson — never type a code from memory), the benchmark text in
`../reference/Florida BEST Grade 8 - Source of Truth.md`, and the B1G-M notes for every benchmark
in the unit in `../reference/B1G-M READING NOTES.md` (the misconceptions you will name, the tasks
and items the guide expects).

## 3. Audit first — and send it before you build anything

Work **every** problem in the package: student pages, practice, homework, additional practice,
assessment, and the keys. Use sympy, not your head, for every value. Write
`a7/unitNN/UNIT N AUDIT.md` with the same sections as `a7/unit03/UNIT 3 AUDIT.md`:

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
7. **Look at everything.** `python3 contact_sheet.py "out/<unit>/A7 N.NN  Slides.pdf"` and view
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
| `option C: no named error with a benchmark cite` | an mc distractor without `errors["C"]` containing `[…]` | name the error the student made and cite the benchmark or B1G-M |
| `scientific-notation coefficient 20.0 outside [1,10)` | a coefficient like `20 × 10⁵` in an item not tagged | if the item is ABOUT the rule, put `not_sci=True` as its first key; otherwise fix the item |
| `adding or subtracting 10^3 and 10^6 — a gap of 3` | MA.8.NSO.1.5 limits + and − to exponents within 2 | rewrite the item's numbers; `not_gap=True` only if the item is ABOUT the boundary |
| `√250 — MA.8.NSO.1.7 is perfect squares up to 225` | a radicand outside the benchmark's list | use a perfect square ≤ 225 or a perfect cube in −125..125; `not_bound=True` for a Unit 2 estimation retrieval item, with the reason in its `source` |
| `radicand '…' is not plain arithmetic on integers` | capcheck could not reduce the radicand | work it by hand; if it is sound, tag `not_bound=True` and say why |
| `line runs off the slide (14.7 in)` | a mixed text+math row too wide | split the row, shorten the words, or move the math to its own row |
| `box crosses the footer` / `math into footer` | too many rows on one slide | fewer rows, or split into two notes slides |
| `table cell wraps out of its row` | a notes table's cell is too long for its column, and a wrapped second line draws outside the border | shorten the cell, widen the column, use fewer columns, or move the words into an `items2` line under the table |
| `plan does not fit … leave whiteboards 22` | the fixed minutes are too few/many | adjust `min` on notes/examples so the remainder lands in 10–20 (aim 15–19) |
| `Unknown symbol: \le` | mathtext, not TeX | `\leq`; see the LaTeX paragraph in SPEC SCHEMA |
| `docscan: calculator line on student surface` | the word calculator on a student page | "a computer displays 3.5E9"; the TE may say calculator |
| `docscan: benchmark code on student surface` | `MA.…` on a student page | move it to the key/TE |
| `glyph: … U+207D` | a character with no glyph in the deck/doc fonts | use plain characters; superscript digits and ⁻ ᵐ ⁿ are fine |
| `offpage` / `slidefit` findings | text outside the page/slide box | shorten; view the page |
| `footer: '…' sits below the footer rule` | a notes line sized for one line wrapped to two and hangs past the rule | shorten the `items2` line, or drop a math row from that notes slide |

## 5. The unit documents, the manifest, the package

1. Copy `u3/unit.py` to `<unit>/unit.py`. Reference Sheet: every tested skill with its method,
   one worked example and the mistake that costs the most points, organized by topic; say what
   the FAST provides and what must be memorized (Source of Truth Part 3). Unit Review: unscored,
   parts by lesson, **one SSDD block** (four lettered parts on one surface, label on the key
   only). Unit Assessment: two periods, sections by benchmark, one point per lettered part,
   numbering straight through; the `total` and `tracker` you declare are asserted against the
   items. `python3 build_unit.py <unit>/unit.py`, then `checks.py`, then look at every page.
2. Copy `u3/manifest.py` to `<unit>/manifest.py`; fill the lesson table (the "line that carries
   the day" is each lesson's `te.lives` idea in ten words), the assessment days, the notes.
3. `python3 install_unit.py <unit>/manifest.py` — deletes and rebuilds the package folder and
   writes `00 - START HERE.md` with the timing table read from the decks.
4. `python3 build_all.py <unit> --install` — rebuilds everything from the specs, runs the suite
   (0 findings) and reinstalls the package — then push. This is the shipping gate.

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

## 8. Open items carried forward (20 September 2026)

- Retroactive coefficient scan of the Unit 1–2 banks (the scan was inert until 20 September;
  those banks were built under the old toolchain and have not been re-scanned).
- PM2 / PM3 dates in the scope calendar when Croix has them.
- Units 1 and 2 were built by the earlier JavaScript toolchain that was lost with its container
  (README). Their packages are shipped and final; they cannot be rebuilt from specs. Any fix to
  them is a hand edit of the shipped .docx/.pptx plus its PDF, recorded in the package's
  Reference folder — the only place hand edits are allowed.
- The Grade 7 on-level course (M7) has its own tree and its own session; rulings are shared
  through `HOUSE STYLE.md`'s exchange mechanism (its header explains).
