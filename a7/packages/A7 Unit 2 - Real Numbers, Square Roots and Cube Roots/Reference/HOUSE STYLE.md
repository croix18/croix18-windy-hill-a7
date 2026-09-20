# Windy Hill Math — House Style

**This file is the single master for both courses — on-level (M7) and accelerated (A7) — and it
supersedes every earlier copy of it:** every style note, every package copy, every staging and
handoff copy, `3 - HOUSE STYLE SPEC.md` in the accelerated handoff folder, and both of the two
forks this file was made from. There is one rulebook from here on, and a second copy of it is not
a variant — it is a defect.

<!-- exchange:base m7-20sep-rulings-18-28 sha1 (M7 to confirm) -->
<!-- merged 20 September 2026 (late) by A7 under ruling 3: M7's numbering stands.
     A7's former rulings 13, 14, 15 are now 29, 30, 31; M7's 16-28 are carried below.
     A ruling names the course it binds when it is not both. -->

**How the two forks exchange this file, ruled 7 September 2026 after a replace nearly deleted a
week of the other fork's work.** *Replace only works when the replacing file is a superset, and
neither worker can know whether theirs is* — each asked the other for a straight replace within
two days and each was wrong the same way. So: **exchange against the base, never against each
other**, and state at the top of the file which base you merged from. The line above is that
statement. It was introduced on the accelerated side, which built its 7 September file by taking
the on-level fork's 2,494-line file — itself a three-way merge against the 1,884-line 5 September
common base — and applying its own work onto it. The accelerated side does **not** hold the
1,884-line base (its spec archive stops at the pre-merge fork), which is exactly why naming the
base in the file matters: the fork that lacks it can still say precisely what it merged onto.

*Verified on both sides the first two times it was used.* The on-level fork checked the
accelerated base line with one command before touching anything (2,494 lines, `4b449025c042`,
exact) and could therefore skip a second three-way merge. The accelerated fork checked theirs the
same way: `a7-8sep-2583 sha1 8a206d87a485` is byte-identical to the copy in its own Unit 1 zip.
**A hash turned "my file is a superset of yours, trust me" into a fact checkable in one command**,
and it is one line. Take the hash of the file as committed, not as sent.

**And the naming pays for itself the first time it is used.** *8 September.* The line said
`m7-7sep-2494 sha1 4b449025c042`, and the on-level fork ran `git show HEAD:"HOUSE STYLE.md" |
sha1sum` before doing anything else: **2,494 lines, `4b449025c042`, exact.** That turned "your file
is a superset of mine, trust me" into a fact checkable in one command, and it meant this version
could be built by applying on-level's 8 September work directly onto the accelerated file rather
than by a second three-way merge. *A hash is worth more than a paragraph of provenance, and it is
one line.* State the base as `fork-date-lines sha1 xxxxxxxxxxxx`, and take the hash of the file as
committed, not as sent.

*Merged 5 September 2026 from the two forks that had evolved apart.* **`MASTER-m7.md`, the
on-level master, is the base:** its structure, its section numbering, its wording wherever the two
said the same thing, and §9b, §13b and §13c, which the accelerated copy did not carry.
**`FORK-a7.md`, the accelerated copy, supplied:** §0's 4 September reader round (the 46 defects,
"a repair is a new claim", the study-guide leak class), `figstale.py`, §6's retirement of the
printed Scoring Sheet, §1's full statements of rules 3, 6 and 8, §9's computed worksheet remainder
and deck-read teacher's edition, §13's deck-geometry checks, §14's accelerated entries (the pop
quiz scored per part, Unit 2 question 6, the two-document settlement, the fade correction) and
§16's SSDD label ruling. Three conflicts were ruled rather than blended and are marked in place.
Every port, every conflict, every drop and everything left open is listed in `MANIFEST.md`.

**This file is the master, for BOTH courses.** The two Source-of-Truth documents are NOT
merged and stay separate — *Croix, 3 September: "keep the grade 8 source of truth separate"*.
`FL-Grade7-Math-Source-of-Truth.md` serves M7 and `Florida BEST Grade 8 - Source of Truth.md`
serves A7, because they are different standards lists for courses that teach different
benchmarks, not two versions of one document. What IS shared across both — the FAST house
style, Florida's wording rules, the calculator policy and the standing preferences — lives in
this file or is stated identically in both, and `speccheck` polices each against its own master.
 Croix ruled on 2 September that the on-level
HOUSE STYLE and Source of Truth are the master set and that on-level owns the merge. It
supersedes every earlier style note, including `3 - HOUSE STYLE SPEC.md` in the accelerated
handoff folder and the accelerated packages' own copies. Where anything disagrees with this file,
this file wins. Where the two courses deliberately differ it is recorded in §14 and nowhere else.
Where this file is silent, copy the on-level Unit 2 materials exactly.

Reference implementation: `M7 2  Unit Assessment`, `M7 2  Unit Assessment Key`,
`M7 2  Study Guide`, and any Unit 2–4 worksheet. When in doubt, open one and match it.

---

## 0. The rule that outranks this file

**Everything on a page a student sees must be mathematically correct. Nothing else in this
document is allowed to compete with that.**

Croix, 2 September 2026, after wrong answers reached student pages in both courses in one week:

> math errors are unacceptable. the fact that you shipped with math errors is a failure. that is
> the most important rule — the stuff that touches students needs to be completely mathematically
> sound. everything else is secondary. I can put out a lot of B's and make it work. the second I
> get associated with bad math is the second I utterly fail.

Read that as a ranking, not a sentiment. A page that is ugly, late, inconsistently formatted or
missing a point value can be fixed next week. A page with a wrong answer has already done its
damage by the time anyone notices, and the damage is to his name in front of parents and a
department. **When correctness competes with anything else in this file — a deadline, a layout,
a rule above, a consistency check that would be nicer to keep green — it wins, and it is not
close.**

### What went wrong, in both courses, so it is not repeated by accident

*Each of these was shipped by the same habit, and none of them was caught by any of the eleven
checks then in place.*

**A7.** (1) A row was copied out of a retired generator into a live deck and never worked:
`−2(−5) = −2( ½x ) − 3` keyed `x = 4`, true only if the coefficient is *negative* one half. It had
working attached, which is what stops the eye. It was wrong in the retired deck too — restoring
content is not verifying it, and inheriting a mistake is still shipping one. (2) An expression
image was chosen by name from a list of 576 and never looked at: `u2_pi3` is π³ ≈ 31.006,
`u2_3pi` is 3π ≈ 9.425. Nothing in the tree knew what either picture said, so the question printed
a value its own key contradicted and its own number line could not reach.

**M7.** (3) A worksheet gave a clock face a diameter of `9⁵⁄₅` inches — ten — while its key said
`9⁵⁄₅ = 9.6`. The numerator should have been a 3. (4) A simulation table projected on four
consecutive slides had a six-spin column reading 0 / 16.7 / 16.7 / 33.3 / 0 / 16.7: 83.4%, and as
counts, five spins. Its six-thousand-spin column summed to 100.4%. Neither column could have come
from any simulation that ever ran. (5) A slide told students to halve a diameter only *after*
dividing by π, "never before", repeated five times in the teacher's edition — the two operations
commute, and the deck contradicted its own answer key.

**The common cause is the important part, and both courses found it independently.** Every check
in either `checkall.py` verified that documents AGREE WITH EACH OTHER — the PDF matches the
.docx, the index matches the images, the tracker matches the question values, the plan totals 53
minutes. **Not one of them could see a wrong answer, because a wrong answer is perfectly
consistent with itself.** A consistency harness cannot catch this class no matter how many checks
are added. Something has to independently re-derive.

### What now stands in the way

- **`mathcheck.py` runs first in `checkall.py`,** ahead of even `xmlcheck`, and packaging refuses
  to proceed on a disagreement — and it runs again inside `finish()`, which every packaging script
  goes through. A7's parses the PROBLEM out of the generator and solves it with
  sympy knowing nothing about the printed answer, reading picture coefficients from the LaTeX in
  `bars.py` and `exprval.js`. M7's evaluates every equality chain, arithmetic statement,
  count-against-probability phrase and printed point total in the shipped document itself. The two
  approaches are complementary and both are kept: the generator-side one catches a keyed answer
  that was never true, the document-side one catches anything that reached the page by any route.
- **An item a checker cannot solve is a finding, not a silence.** Unsolved items fail, and the
  summary line counts them. **The denominator is the finding** — report what was not checked, not
  only what passed. `mathcheck.ack.json` can excuse one **only** with the reason and the human
  derivation that replaces it.
- **A checker that reports correct work as wrong is worse than no checker.** A7's `mathcheck`
  first run read only the text half of an item whose coefficient was an image and called a correct
  key an error; acting on it would have *introduced* a mistake. M7's first run reported 760
  findings, none real, and every round of triage found a bug in the checker rather than the corpus
  — several of which could equally have HIDDEN an error: a regex that ate a leading digit, a
  fraction bar and a division sign collapsed into one character, superscripts flattened so `7²`
  read as `72`, and an old copy of a function shadowing the new one so the fix was not running at
  all. Therefore: an item that cannot be fully read is reported UNSOLVED, never wrong; and
  **M7's `mathcheck` self-tests on every invocation** against 47 cases — 16 planted errors and 31
  correct statements, every one a real line from the corpus — and refuses to report anything if
  the self-test fails.
- **A check that reports a finding and exits 0 is worse than no check,** because the next step
  believes it. Two had that hole; both were fixed and each fix was verified by feeding the check
  an input that genuinely breaks its rule.
- **A filter that silences a check is worse than a missing check,** because the silence looks like
  a pass. M7's `mathcheck` skipped any line matching `\d{1,2}\.\d{2}` so lesson numbers would be
  ignored — which silently excluded every line in the corpus containing a two-decimal value, and
  the one real arithmetic error sat on such a line.
- **An error-analysis row must declare the equation it came from** (`from:` — see ERRORCHECK in
  A7's `slides04b.js`). "The step as written" is by definition not the problem, so without that
  field nothing can solve the row. Its absence is what let A7 error 1 ship, and a row without the
  field is itself reported.
- **`exprcheck.js`** compares the values a question prints against the values its key states, and
  prints how many items it could not compare rather than quietly skipping them.

### Then the harness was measured against a reading, and lost — twice

A7's `mathcheck` ran clean while an independent reading of the same materials found **forty-five**
more defects, nine in Unit 2 and thirty-six in Unit 1. The harness caught none of them. M7's
`mathcheck` ran clean over 256 documents while an independent re-derivation of the answer keys,
then of the slides and teacher's editions, found **forty-nine** more — one wrong answer on a
student worksheet, four pieces of false mathematics projected at students, and the rest false
statements in teaching notes. Two courses, two harnesses, two readings, the same result.

Not one of the ninety-four was an equation with a wrong answer. They were:

| what it was | example |
|---|---|
| a FIGURE disagreeing with its question | a number line plotting B at 5.8 when B = π + 2 = 5.1 |
| a FALSE PROSE CLAIM | "−0.09 repeating is exactly −0.1" (it is −1/11); "9 and 43 are neither perfect cubes nor perfect squares" (9 = 3²); "dividing by a fraction makes things bigger" (20 ÷ 5/2 = 8) |
| a UNIVERSAL CLAIM with a counterexample nearby | "the only fair game of the four" when two are; an "or" event "always larger than either part" when it can be equal, with the counterexample in the same table; "never the other way round" about two operations that commute. Twenty of M7's forty-nine, and almost always in a sentence written to be memorable — **quotable and true pull in opposite directions** |
| a WORKED EXAMPLE contradicting its own reasoning | a student says "closer to 3" and the page plots her answer at 3.5, the midpoint; a slide asserting 10x − x leaves a repeating tail when it leaves 3.5 exactly |
| a TABLE that cannot exist | six percentages summing to 83.4%, implying five trials out of six |
| a MISSING ANSWER | `body.pop()` silently deleting the last paragraph of a key, which in a key is an answer |
| a COUNT that does not match the page | "All six in order" over five numbers; a Practice Test summing to 47 on a paper out of 21; a Study Guide table saying 30/36/34 beside banners saying 7/7/7 |
| a METHOD that contradicts the lesson | a key using 100x − 10x on 0.21666…, which has two digits before the repeat, in a lesson built on not doing that |
| TEXT DRAWN OFF THE PAGE | sixteen whiteboard slides centered to a negative x; three lost the words the question needed — "A **budget** allows 15.75 students" is the whole reason that item rounds down |

**Neither a consistency harness nor a sympy oracle can see any of these, because they are not in
its category.** What found all ninety-four was a reader with no access to the key, working every
question from the rendered page and only then comparing.

### So the reading is the gate and the harness is the floor

- **`rederive.py` is a LEDGER.** A document's fingerprint is its extracted text *plus the hash of
  every embedded image*, because A7 defect 2 changed nothing but a PNG. A record says a named
  reader re-derived that exact fingerprint and what they found. Change the document — change one
  picture — and the record is void. Packaging prints coverage every run and **refuses to package a
  document carrying a recorded, unfixed defect.**
- Mechanical checks added because a reading found what they now catch: **`offpage.py`** (every
  word is on the page it is drawn on, read from the rendered PDF because wrapping and font
  substitution move text after the geometry is written), **`partsum`** (`partsum.js`; the per-slide minutes
  inside a block add up to the block's own stated total — the plan reads the total and never
  looked at the parts), **`pdftwin.py`** (every PDF says what
  its document says — the PDF is the file that gets printed, and one had been a week stale while
  every .docx audit passed), and **`pagecheck.py`** (no shipped page is blank).
- **A question must determine its own answer.** A shared instruction made A7 1.01's questions 1
  and 2 pixel-identical while keying them to 0.375 and 37.5%. **`wbseq.js` takes a per-question
  instruction** for exactly this reason: a question that does not determine its own answer is not
  a question.

### The 4 September round, and the two lessons it added

*Ported from the accelerated copy, which is where this round was recorded.* The whole shipped
tree — 112 documents — was re-derived at its then-current content by twenty-one independent
readers on 3–4 September. They found **46 defects**, none of which any check in this directory
could see. The two worth writing down:

- **A repair can be worse than the defect.** Two A7 1.06 whiteboard slides had text running off
  the page edge. The repair shortened the stem — so hard that the question lost the numbers its
  own reveal used, and for a fortnight slide 18 read, literally, *"…and the total came to $273.
  Write the equation."* `offpage.py` passed it, because nothing was off the page any more. The
  same shape appeared at 1.10 question 6. **Whatever a repair is, it is a new claim, and it gets
  read like one.** Three of the defects in this round were introduced by the repairs of the round
  before it, and every one was caught by the next reader rather than by any check. (§13c states
  the same lesson as a property a check has to have.)
- **A study guide the student may carry into the test can hand over the answers.** Both guides
  promise on their front page that "the numbers are all different from the ones on the test."
  That promise was false four times: A7 1's C3 worked `x ≤ −7` with the assessment's own graphing
  note; A7 2's B3, C3 and D1 reproduced questions 5c, 2d and 4b. Three of the four came out of a
  generator whose own comment, in the same file, read *"deliberately not the assessment's
  numbers."* The intent was written down and the values drifted away from it — which is precisely
  what a comment cannot catch. **`guideleak.py`** now lists every mathematical token a guide and
  its assessment share, with the phrase each came from, and an acknowledgement file that makes
  each exclusion carry a reason. It reports rather than fails, because deciding whether an
  overlap matters is a person's job: `x² = 0` is the only equation with exactly one square root,
  so that case cannot be illustrated with different numbers, and the answer there was to name the
  exception on the front page rather than to pretend it did not exist.

**`figstale.py`** joined the same round: for every figure directory, is any figure older than the
generator that draws it? Nothing else asks whether an artifact is what its generator would draw
today, and a corrected generator whose output was never regenerated is how a capital Π reached a
student's answer key.

### Two things stay on the person, and no script will take them

1. **Work every answer independently.** The publisher's key is not evidence, and neither is ours.
2. **A fix written to a generator is not a fix.** Five A7 repairs were written, the rebuild chain
   aborted on an unrelated error partway through a `&&` chain, and every one was reported STILL
   WRONG by the next reader. **Rebuild each file with its own command, and check the shipped PDF,
   not the source.** A generator that has been throwing for days looks exactly like one that is
   fine until you run it alone.

### What this does not promise

It does not promise there are no errors. It promises that a whole class of them fails the build,
that anything unverified is *visibly* unverified, and — the part that actually did the work —
that **someone reads every page with the key covered, and that the reading is recorded against
the exact bytes it read, so it cannot be quietly inherited by a later version.**

---

## 1. The short list

Ten rules, under rule 0. Everything else in this file is detail.

1. **Old-school textbook.** Serif type, black ink, gray table headers, ruled headings. No emoji,
   no rounded corners, no gradients, no color panels, no clip art, no decorative anything.
2. **No answer boxes and no answer lines.** Leave work space. Students circle their final answer.
3. **No benchmark codes on a page a student works from.** Worksheets, additional practice, unit
   reviews, the practice test, the pop quiz, unit assessments and student reference sheets carry
   none. **A deck's title slide may name its benchmark**, and answer keys and teacher's editions
   keep theirs — a key is a page only the teacher holds, and its codes are what the score tracker
   reads. *Croix ruled this on 1 September 2026, in these words: "Codes on title slides are fine.
   Keep them off student stuff like worksheets and tests."* The rule previously read "on anything
   a student sees," which the shipped set broke in about twenty places — every title slide, and
   the right margin of every question on the assessment and the practice test. It is enforced now
   rather than restated: `docscan.py` carries it as a standing ruling scoped to `paper`, a surface
   that deliberately excludes slide bodies and answer keys. **Naming the mathematics beats naming
   the code anyway** — a student revising can look for "rational numbers in three forms" on the
   page, and cannot look for MA.7.NSO.1.2. See §13b ruling 6 and §15 trap 23.
4. **No partner or group work, anywhere, ever.** Rebuild it as front-taught notes, worked
   examples and individual whiteboard rounds.
5. **A student practice page is a "worksheet."** Never "homework" on the page itself. Only the
   teacher's edition mentions finishing at home.
6. **Every point value is printed and every total adds up.** Section totals and question values
   must both sum to the number in the header.
   **On a unit assessment in either course, one lettered part is worth one point** and the paper
   is out of however many parts it has — A7 Unit 1 is 21, A7 Unit 2 is 34. *Croix ruled this for
   A7 on 1 September 2026: "instead of being out of 100, I'm going to just count each touch point
   from a student as 1 point, then add them up and that's what the test is out of." He extended
   it to on-level on 2 September — "same philosophy I ruled for accelerated" — so it is the house
   rule, not an accelerated quirk, and M7's assessments and unit reviews convert from weighted
   /100 to per-part with their scoring sheets, benchmark trackers and study-guide point tables
   regenerated to match.* A part is right or it is not, so
   marking is a tick per part and a count, with no partial credit to weigh and no arithmetic.

   > **Two later rulings cut across that last clause, and it is left standing rather than quietly
   > edited.** The printed Scoring Sheet was **retired** on 4 September (§6), so the sheets it
   > says were regenerated no longer exist — the item ledger behind them is what was kept. And
   > §13b ruling 5 records *Croix, 3 September: "I don't want to score reviews."*
   >
   > **SETTLED 5 September, by looking at the papers rather than at the prose.** The merge left
   > this open because the two forks disagreed about whether the on-level **unit reviews** were
   > inside the per-part scope. They are not, and the documents say so on both sides: **no unit
   > review in either course prints a point value anywhere** — checked on all three shipped M7
   > reviews (Units 2, 3 and 4) and both A7 reviews. The shipped papers agree with Croix's
   > quotation; it was only the accelerated fork's prose that claimed the reviews had converted,
   > and that claim was false when it was written. **Unit reviews are unscored, in both courses.**
   > *A disagreement between two descriptions of a document is settled by opening the document.*
   >
   > The 1 September ruling is also quoted with different punctuation in §13b ruling 5 ("…as
   > 1 point. then add them up…"). Both records are kept as each fork recorded them; the
   > difference is not this file's to smooth over.

   Two consequences to hold on to. **A wrong setup is not charged twice** — a student who solves
   their own wrong equation correctly still earns the next part, and both keys say so in print.
   And **an item's grain is now a scoring decision**: splitting a question into a and b doubles
   what it is worth, so the split has to be about the mathematics rather than about the layout.
   The counts live in one `Q` map per generator; the header, the section banners and every printed
   value are derived from it, and the build throws if they stop agreeing. The study guides quote
   these numbers, so they move with the test.
   *Scope, as it stands after 4 September: the unit assessments, any parallel form of one — the
   Practice Test — and A7's pop quiz.* Asked which papers moved, Croix said the assessments; the
   Practice Test followed a day later, because its own first line promises *"same twelve
   questions, same order, same point values, only the numbers are different"* — a parallel form
   that rehearses a different denominator is not one. It is out of 21, question for question with
   the Unit 1 assessment, and its key prints the same two marking rules. **The pop quiz is no
   longer outside the scope:** it was rescored on 4 September to one point per lettered part, out
   of 8, and Croix blessed that as an extension of the ruling rather than an exception to it —
   see §14. **Every worksheet is unchanged**, and carries no point values at all.
   §13b ruling 5 carries the full ruling — its grain, its row-not-cell convention and its
   follow-through rule. This is the short form.
7. **Fractions are centered on the line**, never sitting on the denominator. Render them as
   images; Word cannot do it.
8. **No calculator line on any page, in either course. Calculators are allowed on everything.**
   *Croix ruled this on 2 September 2026, superseding a 1 September ruling that had put
   per-question bans on the A7 Unit 2 assessment: "Calculators: allowed on every assessment.
   Print nothing about calculators on any test page. I announce the policy in class; the paper
   stays clean."* A *calculator line* is any instruction telling a student whether they may use
   one **on this page** — a permission and a prohibition are equally a line, and both are out, on
   assessments, quizzes, reviews, practice tests, worksheets and slides alike.
   **The obligation this creates is on the QUESTION, not on the policy:** if an item stops
   measuring anything once a calculator is on the desk, rewrite it so the reasoning is what is
   graded. A7 Unit 2 question 2 asks for the comparison the bracket came from rather than only
   the bracket; the estimating worksheets ask for the perfect squares by name before the root.
   Reaching for a ban instead is the move that is now closed. Describing the tools the state test
   provides is a different thing and belongs on the reference sheet: *"the Grade 8 FAST gives you
   an on-screen scientific calculator for the whole test."* **Get that sentence from FLDOE, not
   from memory** — ours said "you may use a calculator on every item" and "bring the one you have
   practiced with," and the state's own policy says grades 7–8 get an online scientific calculator
   inside the testing platform and that *"not every test item will require the use of a
   calculator."* See §13b ruling 2.
9. **Every answer is worked independently.** The publisher's key is not evidence.
10. **Every document ships as .docx and .pdf.** The PDF is what gets printed and posted.

---


> **An automated extraction proposes; the source disposes.** Any finding produced by a script
> reading a document — a benchmark count, a glyph audit, a width measurement, a page count — is a
> **candidate** until it has been checked against the document itself. The script narrows what you
> have to look at. It never replaces looking.
>
> This is written once, here, because it kept being rediscovered: §8 says it about measuring versus
> rendering, §13 says it about the cmap check, and it has now cost a near-miss in each course a week
> apart. A width measurement that ignored kerning nearly shortened a title that fits. An extraction
> that returned 36 of 40 benchmark codes nearly reported four missing benchmarks that were never
> missing. Both were caught by opening the document.

## 2. Type and color

```
INK    1A1A1A   body text, rules, borders
VOCAB  0B5394   the one blue accent — vocabulary terms only
RED    9E1B32   answer keys, "Watch out" labels
GRAY   6B6B6B   captions, reasoning lines, point values, footers
LT     D9D9D9   table header shading
FILL   F2F2F0   example panels and callout boxes
```

| | Font | Body size |
|---|---|---|
| Student documents | **Century Schoolbook** | 10–11 pt (`size: 20`–`22` half-points) |
| Teacher's editions | **Cambria** | 10.5 pt (`size: 21`) |
| Slides | **Century Schoolbook** | — |
| Spreadsheets | **Arial** | 10 pt |

> **The π trap.** `fc-match Cambria` resolves to Caladea, whose π glyph renders with a bar across
> the top. Split runs so the π character alone uses Century Schoolbook. See `rs()` in `te0406.js`.

> **The figure-generator trap.** Every matplotlib generator must set
> `mathtext.fontset` explicitly. **`stix`** — never `dejavuserif` (its π is a capital Π) and never
> the default, which is `dejavusans` and puts sans-serif fractions inside a serif document.
> `figs.py` did exactly that on the likelihood scale: `0` and `1` in serif, `¼ ½ ¾` in DejaVu Sans,
> on the same tick row. Eight generators, twenty mathtext strings; all now on `stix`.
>
> **`bars.py` is the exception and stays on `dejavuserif`.** Converting it re-renders 830 of 986
> images ~20% narrower, and 156 index entries come from generators whose expression source is
> lost — 57 of them unrecoverable — so the set cannot be made uniform. Consistency across the
> shipped fraction set beats matching the other generators. Revisit only if those 57 are
> transcribed back from the PNGs.

> **No generator rebuilds an index. Ever.** Load what is on disk, update it, write it back. An
> index is shared even when it looks like it is not — `geo/index.json` has **eight** writers,
> `bars/index.json` has three — and a generator that starts from `{}` silently deletes every entry
> the others added. Sole ownership is a fact about today, not a property of the code: the bug
> arrives the first time anyone adds a second writer, and it arrives without an error.
>
> This has already fired once, destroying 156 bars entries of which 57 had no recoverable source.
> It came within a run order of firing far worse: five of the eight `geo` writers rebuilt, the
> worst leaving 2 entries of 89, and the STIX pass survived only because they happened to be run
> in ascending numeric order with the three mergers last. All eleven generators now merge.
>
> **And the order is load-bearing.** When a generator's font or metrics change:
> **1.** fix the merge · **2.** regenerate · **3.** re-run the sizing conversion against the new
> metrics. Doing 2 before 1 is what destroyed the 156. "The set is regenerable" is only true after
> step 1 — before it, regenerating is the thing that does the damage.

### 2a. The variable color code — slides only

One color per **slot in a formula**. Wherever a letter and the number that fills it appear
together, they carry the same color, so the match is seen before it is explained.

```
CB1  1E5AA8   blue     the first slot   — b₁, b, d₁
CB2  C05A00   orange   the second slot  — b₂, d₂
CH   398080   teal     the height       — h
```

**Three, not four.** No formula in this course puts more than three slots on one slide. A pair of
symmetric slots — two diagonals, two bases, two legs, two points — takes the safe pair, blue and
orange, and needs no color of its own.

`4D3D57` **slate** is the reserve fourth, verified, for a course whose formula families genuinely
carry four slots. It is not used here.

Six rules. Four, five and six are the ones that carry the teaching.

1. **The letter is always printed too.** Color is redundant, never the sole carrier of meaning —
   a colourblind student who reads only the letters loses nothing. This also means a
   black-and-white photocopy still works.
2. **Color names slots, not shapes.** The same number changes color when the shape changes.
   On whiteboard Q2 that is the question, not a bug in the palette.
3. **A number with no slot gets no color.** The 5 m slant on a trapezoid stays black. Having no
   color is the cleanest available way to say "this is spare" — which is why black counts as a
   value in the check below.
4. **Color is withheld wherever the student is the one who has to decide.** Question slides are
   black; answer slides are colored. Notes II shows a plain figure because its whole ask is
   *which number is the height*. Coloring it would answer the question the slide is asking.
5. **One axis per slide.** Color names slots, or it names objects — which equation, pre-image
   versus image, point 1 versus point 2 — never both on the same slide. When the axis is objects,
   use blue and orange, because two objects is the common case. The letters carry the slot
   information, as they always do.
6. **A mixed-benchmark slide has no axis, so it gets no color.** Spaced retrieval, review, a
   walkthrough of a returned test — there is no single formula family on the slide, so blue means
   four different things in four questions. Bellwork and review run in black.

**Checking a color before you add one.** `RED 9E1B32` is a value in this system, not decoration —
it is the answer color and it sits on the same slide as coded work.

> Any new color must clear **every existing value** — the other slots, INK and RED — at
> CIEDE2000 **≥ 15** under normal vision, protanopia and deuteranopia. The standing exception is
> **INK/RED at 12.9**, which predates the code and is grandfathered. That is the tightest pair in
> the system and nothing new may join it.

So the true worst pair in the system is **12.9**, not the 17.4 that the coded slots reach on their
own. Stating it the other way made the spec fail its own entry test.

Two things that fail, and why they are not the same kind of failure. **A brown fails against RED** —
6.8, and no brown will do better, because brown is a dark orange-red. **A mid-lightness violet
fails against blue** — under deuteranopia the red–green axis is gone, so a violet has nothing but
hue to separate it from blue, and hue is what is missing. But a *dark* violet separates on
lightness instead: the violet that failed is L\* 42, and the reserve slate is L\* 28. The rule is
therefore narrower than "no violet": **a violet in a code with blue must be substantially darker
than the blue.** Run the numbers; do not pick by eye.

**With a symmetric pair, decide which number carries the change.** For d₁/d₂, two bases, two legs
or two points, which one is "first" is a free choice — and it silently decides which number changes
color when the shape changes. On whiteboard Q2 of `M7 4.02`, assigning 9 → d₁ keeps *first slot is
blue* and puts the change on the 4; assigning 4 → d₁ would have put it on the 9. Both are
defensible. **Choose the one that puts the color change on the number you want them looking at,
and say which in the teacher's edition.** It is a decision made at every symmetric-pair question,
so make it on purpose.

**Figures come in two variants:** `name.png` plain and `name_c.png` colored, from the *same*
generator behind a `CO` flag. Never hand-edit one to match the other.

**The teacher's edition states the assignment in words, per colored figure** — *b₁ blue, b₂
orange, h teal* — because the TE is printed in black and the teacher is standing next to the
screen. One line per figure, and the black-and-white TE stays self-sufficient.

**Slides only.** Worksheets, assessments and teacher's editions stay on INK / VOCAB / RED / GRAY.
Color printing is not reliable and a photocopy loses it, so anything a student holds works in
black. The scaffold lives on the board and is gone from the page, which is the same shape as a
study guide narrowing to a note card.

---

## 3. Page geometry

```js
page:   { width: 12240, height: 15840 }              // US Letter, twips
margin: { top: 900, bottom: 900, left: 1440, right: 1440 }   // default
CW = 9360
```

Dense documents — assessments, study guides — may go to `left/right: 1080` with `CW = 10080`.
**Never tighter than 1080 (0.75").** Bottom margin never below 600 twips; several classroom
printers clip below that.

---

## 4. Document anatomy

**Header.** A borderless two-column table. Left: eyebrow line
(`GRADE 7 · UNIT 2 · ASSESSMENT`, 8.5pt gray, spaced), title (14pt bold), then either the
worksheet code or the point total (9.5pt gray italic). Right: `Name` / `Date` / `Period` rules,
blank on the key. Followed by `rule(14)` then `rule(4)` — thick, then thin.

**Instruction line.** One line of 9.5pt gray italic under the double rule. This is where
"Show your work. Circle your final answer." goes, and where an open-note test says so.

**Section banners.** Used on assessments, study guides and reviews. A numbered title (12pt bold)
on the left, the section's point total (9.5pt gray italic) on the right, then a size-8 rule.
Banner, rule and the section's first block travel together — a banner alone at the foot of a
page is a defect.

**Question stems.** Three-column borderless table: number (bold) | stem | `N pts` right-aligned
9.5pt gray italic. The stem keeps with whatever introduces it.

**Parts** are `a.` `b.` `c.` bold, indented 900 twips with a 380 hanging indent.

---

## 5. Answers and answer space

**There are no answer boxes and no trailing answer rules.** Not `Percent ______`, not a shaded
label butted against an empty cell. Give the student open space to work in, and let the
instruction line tell them to circle the answer.

What is banned is a **receptacle appended to a question that already has work space** — a
`Percent ______` line or a shaded `Fraction ▭` box sitting under a problem the student has
already solved. Four things are not receptacles and are allowed, because in each the blank *is*
the question:

- **A cloze blank inside a sentence or a formula** being completed:
  `Area = ½ ( ____ ) ( ____ + ____ )`, or *the base of triangle A is ____ units.* The blank
  carries the scaffold; removing it removes the question.
- **A response table** whose cells are the thing being completed — a fraction/decimal/percent
  grid, an event/probability table, a simulation X-grid.
- **Multiple choice**, which uses open bubbles `○` at 1300 twips indent.
- **An ordered list of slots** where the order is the answer, e.g. least to greatest.

The test: could you delete the blank and still have the same question? If yes it is decoration —
cut it. If no it is the response format — keep it.

Work space is sized to the work, not to the page: about 0.6" for a one-step conversion, 1.5" for
a multi-step problem, and 1.3" for an explanation.

---

## 6. Answer keys

- Answers in **red bold italic**. Reasoning under them in **9.5pt gray italic**.
- **Every creditable item carries its point value** in small gray parentheses beside it — `(4)`.
- **Every question closes with a subtotal line**: `Scoring: a 4 · b 4 · c 4 = 12 points.`
  Every question, including the one-part ones. Consistency is the point.
- **RETIRED 4 September 2026: the printed Scoring Sheet.** Croix: *"no need for a scoring sheet,
  a detailed key is good."* The A7 keys had split — Unit 1's page was gone and Unit 2's was still
  there — which is how the review found this. **Both keys now carry the Score Tracker and no
  sheet.** Unit 1's opens with it and Unit 2's closes with it, and either end is a fine place for
  a page a teacher fills in while marking. What was not fine was a scoring sheet on one key and
  not the other, which is what this settled. The item ledger that fed the sheet is KEPT in the
  generator and asserted against the paper's total at build time: dropping a page is not the same
  as dropping the guard, and that ledger is what caught the /100-era point values. A key still
  CARRIES the per-benchmark Score Tracker and the follow-through rule, wherever it puts them.
  *This retires the requirement this file previously carried — "every assessment key ends with a
  Scoring Sheet: one page, one row per creditable item, in test order, columns `Item | What earns
  the credit | Points | Score`, and a Total row." The unique-label discipline it carried (`4a
  dec`, `4a pct`, `8 r1` … `8 r4`, so no row can be posted twice) lives on in the item ledger.*
- Student version and key come from **one script** branching on `KEY = process.argv[2] === "key"`.
  They can then never drift apart.

---

## 7. Mathematics conventions

- **π:** 3.14 by default. 22/7 only where the measurement's denominator cancels the 7, and the
  question says so. "In terms of π" is asked for explicitly. 355/113 is a curiosity, never an
  answer.
- **Rounding:** one convention per document, stated on the page. Decimals to the hundredth,
  percents to the tenth, unless the document says otherwise. Round **last** — take the percent
  from the full decimal, never from a rounded one.
- **Repeating decimals** keep the bar. Never round a repeating decimal away.
- **Simplifying** is accepted but not required unless asked; the key says so.
- **≈ means approximately.** Never write `=` for a rounded value.
- Every figure is **drawn to scale, geometrically possible, and solvable from the labels given**.

---

## 8. Figures

- `figs.py` builds spinners, jars, number lines, geometry. 300 dpi, `transparent=True`.
- **`mathtext.fontset = "stix"`, never `dejavuserif`.** DejaVu Serif's mathtext sets lowercase π
  with straight legs and a flat bar; at 12 point it reads as a capital Π. On a unit about circles
  or irrational numbers that is not a small thing. STIX sets a proper π.
- **Size mathematics in ems, not by eye.** Record each image's height in ems in the figure index
  and set it at one fixed point size at render time — larger than the prose on purpose, so a
  radical over two digits stays legible across a desk. Heights picked at the call site drift: a
  one-line barred decimal set to stacked-fraction height towers over the text beside it, and
  stacked fractions set by hand come out half the size of the numbers they sit next to. Both
  happened here before the rule existed.
- **Grayscale plus hatch patterns**, never color alone — everything gets photocopied.
- Section labels get a white rounded bbox or the hatching runs through the letters.
- **Exact-size printing.** A figure students measure must be rendered without
  `bbox_inches="tight"`, at `figsize = span_cm / 2.54`, with `subplots_adjust(0,0,1,1)`. The
  document must carry a printed scale bar and a "print at 100 percent" warning.
- **Sizing is computed, not quoted, and the numbers belong to a corpus.** A one-line expression
  and a two-line one must not carry the same height, and neither height is chosen by hand. *How*
  it is computed differs by fork, and so do the numbers, so §14's rule applies to this bullet:
  a figure quoted in this file is a snapshot of what one tree's code computes, never an
  instruction to the code, and the moment the code starts computing it the number here is a
  liability.
  - *Accelerated:* `m()` renders every figure with a recorded em height at `hem x 17/72` inches
    and ignores whatever the call site passed — a single-line barred decimal at **0.23"**, a
    stacked fraction at **0.42"** as that corpus stands. Those two were written here as 0.17" and
    0.40" and the 0.17" was wrong by a third from the day the em rule replaced it, measured on the
    shipped Practice Test Key whose barred cells are 0.229-0.240" tall. Only a figure with no
    `hem` falls back to a call-site height, and in Unit 1 those are the ten slide images alone.
  - *On-level:* there is no `hem` and no single pair of numbers to quote. Every figure is drawn at
    its own natural size from the index and printed at `e.w x s` by `e.h x s`, so height follows
    the expression's own aspect. Measured across the 1,132 images in the full M7 package on
    7 September: barred decimals sit at **0.167-0.229"**, stacked fractions at **0.302-0.458"**,
    and the 24 tallest are figures rather than expressions. The rule is satisfied — one line and
    two lines never share a height — and it is satisfied by construction rather than by a
    constant, which is why no number here needs maintaining.
- **Set larger than the prose on purpose, and check the neighbours.** 17 point against 11 point
  makes a barred digit about 1.7x the height of a typed one. That is right for display
  mathematics and wrong inside a table whose other cells hold the same kind of value as plain
  text: *(accelerated)* Question 1 of the Practice Test sets `0.5-bar` and `55.5-bar%` as images
  beside a typed `0.65` and `48%`, and the row is visibly taller for it. It is not a mathematical
  defect and it ships, but a column that mixes image and text values is a place to look before
  printing.
- **One digit size per document, and the rule has to be implemented in every helper that sizes
  a figure — plural.** *Both courses, 7 September.* §8 has forbidden mismatched digit sizes since
  the file existed and, in both forks, nothing measured it. `exprsize` measures it now, and it can
  be exact rather than a judgement: every stored figure is drawn at one font size and cropped to
  its own ink, so the printed digit size is exactly `printed height / natural height`, and two
  figures at the same ratio have the same digits whatever their boxes.
  - *On-level* was shipping a one-line barred decimal and a two-line fraction in the same 0.375"
    box on the 2.04 Worksheet Key — three lines apart, the decimal's digits nearly twice the
    fraction's — across four documents and their keys.
  - *Accelerated* predicted itself immune, because `m()` sizes from `hem` and `hem` is 2.400 x the
    ink height for all 2,134 `bars` and all 310 `figs4` entries, so the ratio is arithmetically
    constant. The prediction was right about `m()` and wrong about the corpus: there were **five**
    sizing helpers across the two accelerated trees and the rule was implemented in one.
    `em()` multiplied `disp` figures by **1.45** on a comment that had been true under the
    box-height sizing it replaced and false ever since; `a()`, both `telib.js` copies,
    `teachers_edition.js` and `worksheet_AND_key.js` each carried their own 0.19", 0.24" or 0.38"
    default. The Unit 2 **graded assessment** printed 27/4 at 1.48x the digits of the 2-pi three
    lines above it, and the Unit 2 Review reached 2.03x. All five now size from `hem`; worst ratio
    in the corpus went from 2.03x to 1.048x, and the residual is 96-dpi integer rounding.

  **The rule this earns is about arguments, not about figures: a derivation that proves a property
  of one function proves nothing about a corpus that reaches that function by four other routes.**
  The argument was correct and it was standing in for the measurement. It tells you where to look.

- **A library is part of a generator's timestamp.** *Accelerated, 7 September.* `docstale` compares
  each document with the generator that names it, and correctly classifies `lib.js` and `telib.js`
  as libraries because they write nothing — so an edit to the sizing of every expression image in
  the corpus left **115 of 115 documents reported clean**. It now takes the newest of a generator
  and every local module it `require`s, transitively, and the same edit reported 47 stale
  immediately. *A check whose denominator excludes the thing that changed is the failure this
  suite keeps re-learning, and it is worth asking of every check in it: what could I change that
  this would not notice?*

- **Measuring finds candidates; rendering settles them.** A width check that sums advance widths
  ignores kerning, and at a tenth of an inch that is the whole margin of error. Never shorten a
  title or a label on a measurement alone — render it and look. Setting a one-line expression to fraction height makes it tower over the body text.

**Figures beside tables break in Google Docs.** A picture placed in a table cell next to another
table renders clipped there, though Word and the PDF are fine. Post the PDF. If a document has to
be editable in Google Docs, stack the figure above its table instead.

---

## 9. What goes in a lesson

- **A deck is measured in teaching blocks, not slides.** Eight to ten blocks: warm-up, notes,
  worked examples, a whiteboard sequence, the worksheet hand-off, ticket out the door. A
  whiteboard sequence is **one block** however many slides it takes — a question-and-reveal pair
  is forty-five seconds, not a teaching block. Do not pad or trim a deck to hit a slide count.
  **No slide count appears anywhere in this file.** One did — "12–13 slides", in the document-types
  table forty lines below this line — and it stood for a week against the rule directly above it
  while both courses shipped 26-slide decks. A number in a table outranks a principle in prose for
  anyone skim-reading, which is exactly who reads a table.
- **Timing.** The plan totals the period **exactly** — 53 minutes — and the teacher's edition
  states how much of that is worksheet. **The worksheet share is the remainder, computed, not
  chosen:** the instruction blocks are read from the deck's own speaker notes and the worksheet
  absorbs whatever is left (`deckread.js`, `planFromDeck`). *This replaces "Both courses run 45–50
  minutes of instruction with 3–8 of worksheet," which was a range typed by hand and was wrong for
  fifteen of the sixteen rebuilt A7 lessons the day it was written.* Across A7 as built today the
  instruction runs **40–48 minutes** and the worksheet **5–13**; a range in this file is a
  description of what is built and never a target to hit. What is not negotiable is that the
  numbers add up and the worksheet share is stated, because the worksheet share is the flex and a
  reader has to be able to see it.
- **A plan that does not fit refuses to build.** `planFromDeck` throws when the instruction blocks
  leave the worksheet less than a minute, and `decktime.js` fails when the worksheet slide's own
  note states a different number from the one the plan leaves it. Two places said the same thing
  and drifted; now one is computed and the other is checked against it.
- **Worksheet time is the flex.** Nothing instructional is ever cut to protect it.
- **The teacher's edition reads the deck. It does not keep a second copy of it.** The timing
  table, the slide-by-slide walk and every slide number in the surrounding prose come from the
  `.pptx` at build time (`telib.deckPlan`, on `deckread.js`); the edition owns the *wording* — a
  gloss per segment, and `nm("Notes III")` prints "Notes III (slide 5)" with the bracket derived.
  *This rule exists because the first sixteen editions carried hand-typed tables: the decks were
  rebuilt from thirteen slides to as many as thirty-two and every table went on describing the
  deck that used to exist, pointing a teacher at "slides 9–11" for a sequence that now runs 19 to
  30.* A gloss or a reference naming a segment the deck does not have **throws**; a segment that
  quietly disappears is exactly the failure this is for.
- **One plan per lesson. Build the full lesson every time.** There is no shortened variant, no
  second timing table, and no Wednesday plan — not in the deck, not in the teacher's edition, not
  in the pacing guide. Short days, assemblies, fire drills and everything else are the teacher's
  to absorb, and the teacher is the only person in the building who knows on the day which block
  can go. A printed cut is a guess made weeks earlier by someone who is not in the room; it takes
  the decision away from the person best placed to make it and it makes the deck look like it
  needs an apology. **Build the whole lesson and let it be cut.**
- **No commentary on slides.** No "say this," no "write this exactly." Teaching notes live in the
  teacher's edition.
- **Whiteboard sequences show one question at a time**, each followed by the same slide with the
  answer revealed. Never several problems on one slide — students then work at their own pace and
  the round stops being simultaneous. Six questions beats ten. Sequence them so exactly one
  feature changes between consecutive questions, so a wrong answer names the missing idea. Each
  question must be answerable in under ten seconds and impossible to get right while still
  holding the misconception. Every distractor must be a genuinely different value — two choices
  that are the same number is a defect. The routine — boards down until the cue, all up together,
  scan the back row first, question the blank boards before the wrong ones — lives in the
  teacher's edition, not on the slide.
- **Teacher's editions** carry: standards and targets, learning target, essential question,
  building on / working toward, materials, both timing plans, vocabulary, slide-by-slide notes,
  the full answer key, and a *Changes from the Math Nation Lesson* section listing exactly what
  was wrong in the original and what it is now.

**Warm-ups.** Four minutes. Name the type in the teacher's
edition and rotate through five:

| | Type | What it is for |
|---|---|---|
| 1 | **Spaced retrieval** — four questions: last lesson, last week, last unit, prior-grade prerequisite | Keeps earlier units alive without spending days on review |
| 2 | **Diagnostic question** — one multiple-choice item on whiteboards | Every distractor is a named misconception from the teacher's edition |
| 3 | **SSDD** — same context or picture, different deep structure | Kills autopilot. Short to read |
| 4 | **Same and different** | Builds the discrimination that ordering and classifying questions need |
| 5 | **Reflect, expect, check, explain** — predict the next answer before computing | Turns practice into thinking |

A warm-up with no mathematics in it is not a warm-up. Notice-and-wonder prompts, career videos
and advertisements have all been cut for this reason.

**Document types.**

| Type | What it is |
|---|---|
| Worksheet | The student practice page. One per lesson. |
| Worksheet Key | Same page with answers. |
| Slides | Slide deck with speaker notes. Length follows the teaching blocks — see §9. |
| Teacher Edition | The lesson plan: standards, the timing table, vocabulary, slide-by-slide notes, the answer key, misconceptions, the Variation note (§16 rule 2), and **what the audit against Math Nation found** — not "what changed from Math Nation", which describes a lesson that started from the book. Under §16 it does not. **The timing table, the slide walk and every slide number in the prose are read from the deck** — see §9. |
| Handout | A lesson-specific in-class page. |
| Record Sheet | A page for recording trials or measurements. |
| Vocabulary Reference | Every term in the unit, alphabetical, with the lesson it appears in. |
| **Study Guide** | Ruling 4: the document the student **makes**. The Reference Sheet's material with the answers taken out — cloze blanks, formula frames, space for their own examples. **May be used on the unit assessment**, in whatever state they filled it in. Rendered from the same content file as the Reference Sheet. Files under Handouts. |
| Unit Review | The practice set. |
| Additional Practice | A second practice sheet on the same lesson. Posted, never assigned. Has its own key. Files under Worksheets. |
| Practice Test | A parallel form of the unit assessment — same questions, same order, same point values, different numbers. Files under Assessments. |
| Quiz 1, Quiz 2 … | A short in-unit quiz, numbered so a unit can hold several and still sort. Files under Assessments. |
| **Reference Sheet** | Ruling 4: the document the student **studies from**. Every tested skill with its method, one worked example and the mistake that costs the most points, **complete and filled in**, with the skill's point value beside it. Numbers differ from the test's. **May NOT be used on the assessment.** Wider than a Vocabulary Reference — it carries procedures and number lists as well as terms. Files under Handouts. |
| Unit Assessment | The test. |

The Study Guide and Reference Sheet rows above were written before ruling 4 and described one
document doing both jobs. They are corrected here rather than only in §13b, because this file
records what happens when a table disagrees with a principle in prose: **the table wins with
anyone skim-reading, which is exactly who reads a table.**

---

## 9b. How lessons teach

Moved to **§16**, which is where the accelerated course wrote the same ruling. One rulebook
means one section number, and §16 is the number both courses' checkers and handovers cite.
The pointer stays here because §9 says what goes in a lesson and §16 says how it teaches,
and a reader arriving at the first will want the second.

---

## 10. Sequencing this year

Both courses run the **book's own order** for 2026–2027, the final Math Nation year. On-level
skips Math Nation Unit 1 and runs sequentially from Unit 2; accelerated runs its own book from
Unit 1.

The county's 2026–2027 scope and sequence sheets are transcribed in
`Reference/SCOPE AND SEQUENCE 2026-2027.md`, but they were built around the textbook adopted next
year. Following them against Math Nation would jump between units all year and, from Q3, between
two books students carry at once. Use those sheets for what the county considers essential, not
for pacing.

---

## 11. Naming and packaging

```
M7 2.03  Worksheet.docx
 │  │  │      └── what it is
 │  │  └───────── lesson 3, always two digits
 │  └──────────── unit 2
 └─────────────── course code
```

**Lesson numbers are always two digits.** Drive and Classroom sort filenames as text, so a
one-digit scheme puts `2.10` between `2.1` and `2.2` the first time a unit reaches ten lessons.
Two digits everywhere is one rule instead of two.

Two spaces before the type. Unit-wide documents drop the lesson number: `M7 2  Unit Review.docx`.
Course codes: **M7** on-level, **A7** accelerated.

Type names are exactly the list in section 9 — plus `Worksheet Key`, `Handout Key`,
`Unit Review Key`, `Unit Assessment Key`. Nothing else is invented on the spot.

**Folders**, in every package:

```
Worksheets/         Slides/          Handouts/        Assessments/
Answer Keys/        Teacher Editions/
PDFs/               a mirror of all six, same filenames
Reference/          benchmark text, this file
00 - START HERE.md
```

Every key lives in `Answer Keys` — including unit review and assessment keys. That is deliberate:
there is exactly one folder you never upload to Classroom by accident.

---

## 12. Before a unit is built

Math Nation borrows tools from later in the book, teaches past the benchmark, and misstates its
own coherence. Audit the source **before building**, and send the findings to Croix as a note —
not into a teacher's edition he opens the morning he teaches it.

1. **Technique, not just content.** For each worked example, list the *moves* a student must
   already own — solving for a variable, cross-multiplying — and locate each move in the book.
   Anything located later is a finding. Recording only the topic is what let the Unit 2
   repeating-decimal defect through.
2. **Scope.** Pull the benchmark's clarifications and examples from the state course description.
   Beyond them is optional; optional content costing a day is a candidate to cut.
3. **Grade level.** Anything needing a grade 8 benchmark is a finding.
4. **Their coherence claims are unreliable** — "N/A" twice in Unit 4 where a real prerequisite
   exists. Derive them.
5. **Their answer key has been wrong outright.** Work every answer independently.
6. **Split benchmarks** — note any whose lessons live in two units.

Standing findings are in `Reference/UNIT AUDIT.md`.

---


### A finding is not a decision

§12 routes findings to Croix because the person who has to act on one is the person who should
hear it first. **The same applies to the decisions those findings raise.** When a conflict turns
up between two rules — as the rebuilt deck did against the length of a Wednesday period — the
question of which rule gives way is his, and it is not to be settled between the two courses.

The failure mode of a good collaboration is that it starts absorbing decisions that belong outside
it. Answering each other's findings quickly and well is why the glyph work and the index work went
as they did; it is also exactly what made solving that one between us feel like more of the same.
Both courses spent a day building an answer to a question neither had asked whose it was.

**Ask whose problem it is before solving it.**

## 13. Before anything ships


> **Read the spec end to end, and the check is a person.** The four drift checks — `indexdrift`,
> `imagedrift`, `speccheck`, `specdiff` — all take the current spec as ground truth, so the one
> failure none of them can see is **the spec disagreeing with itself**. A rule retired in prose and
> still asserted in a table is not retired; it is asserted twice, differently, and `specdiff` reads
> the surviving half as live.
>
> Three were found on one reading: a `12–13 slides` row against *"do not pad or trim a deck to hit
> a slide count"* forty lines above it, a divergence entry claiming A7 decks run longer when both
> courses now ship 26, and a `Teacher Edition | As above` row pointing at the slide count. All
> three had stood for a week while the tools reported clean, because a tool cannot notice that its
> ground truth is inconsistent.
>
> Read it whole after any change that touches more than one section. Numbers in tables are the
> place to look first: a number in a table outranks a principle in prose for anyone skim-reading,
> which is exactly who reads a table.

> **Re-derive, never re-read.** Working every answer independently is item 1 because *reading* an
> answer cannot catch the failure that matters most: a wrong answer sitting beside correct
> reasoning. A wrong answer with wrong reasoning looks wrong. A wrong answer with right reasoning
> reads as already checked — the correct clause is exactly what stops the eye and moves it on.
> Both wrong answers that reached a classroom in this project were of that kind. "The working is
> shown" is not evidence; it may be the opposite.
1. **Work every answer independently.** Do not copy the publisher's key; it has been wrong
   repeatedly, including a printed circumference that was simply incorrect.
2. **Check every figure is solvable** from the labels actually printed on it.
3. **Render to PDF, rasterize, and look at every page.** Measure the ink bbox against the
   printable area. A page returning `None` is blank; a bottom near the margin is about to
   overflow.
4. **Check the totals two ways** — by section and by question.
5. **Audit the glyphs in every document, not just teacher's editions.** `glyphaudit.py` resolves
   each run's declared font through `fc-match`, opens the file that will actually be used, and
   checks the cmap. Anything the document asks for that the font does not contain is a finding —
   it is being drawn by a fallback nobody chose.

   Century Schoolbook resolves to TeX Gyre Schola and Cambria to Caladea, and **between them they
   lack ○ ● □ ■ ✓ ✗ ∛, every subscript and superscript, every vulgar fraction, and (Caladea) π.**
   An audit of this set found **195 such characters across 24 documents**, all being supplied by
   DejaVu Sans — a sans-serif — inside serif documents.

   **Neither script carries a list of risky characters.** A hand-written list is only as good as
   the last person's imagination, and the characters that get missed are the ones nobody thought
   to type. Everything above U+007F is checked; ASCII is safe in the fonts we use and nothing else
   is assumed to be.

   **Audit every part the reader sees**, not just `word/document.xml`: headers, footers,
   footnotes, endnotes, `word/numbering.xml` — where a list bullet is defined, usually with no
   font named at all — and for a deck both `slides` and `notesSlides`. The document default comes
   from `docDefaults` in `styles.xml` or the slide master, so runs declaring no font are still
   resolved against the font they will really use.

   `fixglyphs.py` re-fonts only what the declared font cannot draw — **π → Century Schoolbook,
   everything else → FreeSerif** — and refuses to run if a target font turns out to lack the
   character. It runs after every build, so nothing depends on whoever writes the next document
   remembering. Doing this at call sites does not hold: the call-site π fix leaked eight
   characters in one file.

   **A cmap check is necessary, not sufficient.** It catches a character the font cannot draw. It
   cannot catch a character the font draws *wrongly* — Caladea has no π so the check finds it, but
   DejaVu Serif's mathtext π is present and shaped like a capital Π, and only looking at the PDF
   ever found that. The audit narrows what you have to look at. It does not replace looking.

   The PDF embeds a subset, so once built correctly it prints identically anywhere. The exposure
   is the **.docx**, which carries only the font name and gets re-resolved on whatever machine
   opens it.
6. **Confirm every .docx has a .pdf twin** with the same name.
7. **Check the geometry of every deck, not only its words.** Item 3 rasterizes and looks at each
   page, which finds a blank page and ink over the margin; it does not find a collision in the
   middle of a slide, because a page with a picture drawn across a paragraph has ink exactly where
   ink belongs. Three checks cover what the eye and the bbox both miss, and `checkall.py` runs all
   three over every deck:

   - `slideoverlap.py` renders the deck and compares **text against text** — two lines whose
     vertical centers sit closer than a line height are a collision. Measured, not guessed: a
     wrapped continuation line sits at 0.78 of a line height every time and the real collision
     found on A7 2.02 sat at 0.48, so the threshold is the midpoint, 0.62.
   - `shapeoverlap.py` reads the `.pptx` and compares **pictures against text frames**, which the
     rendered check cannot do because a picture puts no words in the text layer. It shrinks each
     picture to its ink first — these figures are saved with a label row reserved above and below,
     so a frame can be twice the drawing — and an overlap confirmed harmless by rendering the
     slide goes in `shapeoverlap.ack.json` **with the reason**, never by loosening the threshold.
   - `decktime.js` checks that the worksheet slide's own note states the minutes the plan leaves
     it. See §9.

   > **A placer that does not record where it ended is the whole family of bugs.** `outline()`
   > advanced a cursor; `figure()`, `img()`, `line()` and `nline()` did not, and the cursor was
   > not reset between slides. So a callout placed from `Math.max(endOf(), floor)` after a picture
   > took its position from whatever ran **before** the picture — on one slide, from the previous
   > slide entirely. That drew a number line through three lines of notes, a parabola through its
   > own callout, and a labeled radical across the words of item C. Every placer records its
   > bottom now and `slide()` clears the cursor, which turns three silent layout bugs into one
   > build-time failure of the guard that was already there.

```bash
node doc.js && node doc.js key
soffice --headless --convert-to pdf doc.docx
pdftoppm -jpeg -r 100 doc.pdf page
python3 -c "
from PIL import Image; import glob
for f in sorted(glob.glob('page-*.jpg')):
    im=Image.open(f).convert('L')
    b=im.point(lambda v:255 if v<235 else 0).getbbox()
    print(f, b[1] if b else None, b[3] if b else None)"
```

---

### Two drift checks, both before shipping

A generated artifact and the thing that generated it drift apart silently. Two checks, neither
expensive, both run before anything goes out:

```
python3 indexdrift.py                  # does each index match what its source declares now?
find "out/<pkg>" \( -name '*.docx' -o -name '*.pptx' \) -print0 \
  | xargs -0 python3 imagedrift.py lib # does every embedded figure still match the library?
```

`indexdrift.py --record` after any deliberate regeneration. It catches the
**declared-but-unrealised** state — a generator that says `stix` while its images are still
DejaVu Serif — which nothing else can see, because reading the source and reading the index each
give a consistent answer and only the pair disagrees.

`imagedrift.py` catches the document side: **a document embeds a copy of each figure at build
time, and regenerating the figure does not update it.** A corrected figure only reaches students
if every document built from it is rebuilt, and nothing in the document says which those are.

> **Quote the paths.** The first run of `imagedrift.py` here reported *clean* over **zero
> documents** — shell word-splitting broke every filename containing a space, every `ZipFile`
> raised, and the exception was swallowed. A check that examined nothing must never be able to
> print a clean result. Both tools now print the denominator — documents opened, images examined —
> and exit non-zero if it is zero. If a check reports clean, look at what it counted.

> **Name the corpus, not just the count.** A denominator only defends you if you also say what
> population it was drawn from. *"110 PDFs scanned"* is true, reassuring, and conceals never having
> opened a `.md` file — which is where the reference documents live. Both of this project's worst
> finds were markdown: a `START HERE` page no script touches, and a source-of-truth document that
> stated a retired rule as a **build requirement**, so anyone building the next unit from it would
> have correctly reproduced the thing we had just spent a day removing. Print `107 PDFs · 24
> markdown · 2 workbooks`, and ask what file type is missing from that line.

> **Fixing the shipped copy is not fixing it.** A spec lives in one place and is copied into every
> package, staging directory and handoff folder. Eleven staging copies here still carried a rule
> that had been removed from the shipped set, and the intermediate a repack reads from was among
> them — so the shipped file would have been correct exactly until the next rebuild. Two handoff
> documents were 11,000 bytes behind, including the one whose entire purpose is to be pasted into
> a new chat. `speccheck.py` compares every copy against its master and scans every markdown file
> in the tree for retired rules; run it with the other two drift checks.

> **Orphans.** `imagedrift` finds a third thing neither index nor glyph audit does: an embedded
> figure with **no counterpart in the library at all** — 5 of the 15 distinct stale images here.
> Those documents cannot be rebuilt faithfully, because whatever drew the figure is gone or has
> changed. Same family as an index entry whose expression source is lost, one layer out.


## 13b. Rulings — Croix, 2 September

Recorded verbatim in substance. These are his, not inferences from them, and they outrank
anything earlier in this file that disagrees.

**Ruling 1 — Lesson 2.04 is taught by the pattern, not by algebra.** Keep the direction
(repeating decimal → fraction) and teach it as the pattern: the repeating part over 9s
(0.4̄ = 4/9, 0.4̄5̄ = 45/99), extended to the prefix cases as *subtract the non-repeating part,
put it over 90 or 900* — a fill-in recipe with a why-it-works demonstration. **No "let x",
no pairs of equations, and nowhere does a student solve for anything.** This governs the whole
coordinated set: the 2.04 deck, teacher's edition, worksheet, additional practice, section 3
of the study guide, and the Unit 2 assessment. An assessment item survives if the pattern as
taught covers it — 19.1̄% works as (191 − 19)/900 — and is retuned if it needs the equations.
This is the answer to the UNIT AUDIT's finding 1 "hard block": *keep the pattern and drop the
algebra*, chosen by Croix, 2 September.

**Ruling 2 — Calculators are allowed on every test, and nothing about calculators is printed
on any test page.** Croix announces the policy in class. No `NO CALCULATOR`, no `CALCULATOR`,
no per-question ban, no explanatory header, on any assessment or unit review in either course.
The Part 1 / Part 2 layout of the Unit 3 and Unit 4 assessments may stay; only the labels go.
Part 8 of the Source of Truth says this once and says nothing else about it.

**Ruling 3 — One rulebook, and M7 owns the master.** This file and the Source of Truth are the
master set for both courses. The accelerated copies' recorded rulings merge in; where the
courses deliberately differ it is recorded in §14 and nowhere else. Identical copies ship in
every package, `speccheck` polices every copy including the accelerated ones, and there is
exactly one master from here on.

**Ruling 4 — Every unit gets two documents, and they are different documents.**

| | Reference Sheet | Study Guide |
|---|---|---|
| Content | the compilation of all the unit's notes and important topics, **complete and filled in** | built so the student does the work: blanks, worked-example frames, space for their own examples |
| Purpose | the thing they study *from* | the thing they *make*, and the act of making it is the studying |
| On the test | **may NOT be used** | **MAY be used**, in the state the student filled it in |

Both are built for every unit. The assessment's "you may use your study guide" line means the
Study Guide and only the Study Guide.

**Built, 3 September — and how.** Units 2, 3 and 4 each ship both documents. The pair is rendered
from ONE content file per unit (`u2guide.js`, `u3guide.js`, `u4guide.js`) over a shared
`sgkit.js`: `bl("13.026")` prints the value on the Reference Sheet and a rule of the same width
on the Study Guide, and `frame()` appears on the guide only. The alternative — write the sheet,
copy it, delete the answers — produces two documents that agree on the day they are written and
never again, which is this file's oldest failure shape wearing a new coat.

Three things that came out of building it:

- **Unit 2 could not wait for "whenever you next touch that unit".** Its one study document was
  complete and filled in, which under this ruling makes it a Reference Sheet — and the Unit 2
  assessment printed *"You may use your study guide."* The paper was pointing a student at the
  one document the ruling does not let them bring. A contradiction that is already printed is
  not a scheduling question.
- **The arithmetic is set as TEXT, not as images.** `mathcheck` reads text; an equality chain
  drawn as a PNG is invisible to it, and these sheets are nothing but equality chains. Setting
  them in stacked fractions would have put the entire pair outside the reach of the one check
  that exists to stop a wrong answer reaching a student. Barred decimals stay images because the
  bar is the notation, and the equality that uses them is written in text alongside.
- **Rule 2 and this ruling collide, and the collision is resolved by SURFACE, not by exclusion.**
  A Study Guide is made of blanks; rule 2 forbids them. The later, more specific ruling wins on
  that one document type — so `docscan` classifies a Study Guide as its own surface rather than
  excluding it, and the surface it leaves behind carries a new rule of its own: **a Reference
  Sheet has no blanks.** That is the failure this pair can actually have — one render mode not
  set, every answer on the complete document silently becoming a line, the build succeeding, and
  a student revising from a sheet with the answers missing. Verified in both directions by
  installing the guide under the sheet's name.

The Unit 2 section totals now come from `u2map.js`, which the assessment builds from too. The
sheet used to say "Section 3 alone is worth 11 of the 35 points" as typed numbers — a second copy
of the point map in a second file, and a second copy is how a paper and a study document come to
disagree about what a section is worth.

**Ruling 5 — One point per lettered part, in both courses.** Croix, 1 September, extended to
on-level on 2 September:

> instead of being out of 100, I'm going to just count each touch point from a student as
> 1 point. then add them up and that's what the test is out of.

The goal he gave for it is **grading maximally easy**: marking is a tick per part and a count,
with no partial credit to weigh and no arithmetic. Three follow-up decisions he made when asked,
which matter as much as the headline:

- **Grain — one point per part that requires its OWN calculation or processing.** *Refined by
  Croix, 3 September:* "Do per part. but only when each part requires its own calculation or
  processing. so like a number from least to greatest is 1 point." Not per blank and not per
  lettered part automatically — the test is whether the student had to do separate work for it.
  A matrix question — several contexts down the side, several tools across the top — is scored
  **by the row, not by the cell** (*Croix, 3 September: "row not cell"*). Working out that 70% is
  7 of 10 is the calculation; the boxes across that row are one decision about one context. This
  is also the "both cells right = the point" convention carried over from the accelerated keys.

  Two consequences that cut in opposite directions:
  - A lettered part that needs no separate work is not its own point. Restating an answer in a
    second form, or a bubble that only records a conclusion already reached, rides with the part
    that earned it.
  - A sub-item INSIDE one part that does need its own work IS its own point. **Ordering a list is
    one point per number**, because each value has to be evaluated before it can be placed —
    √50, π + 2 and −0.09 repeating are three separate pieces of work. This is what settled the
    open A7 question below — **for on-level.** It was **not adopted for the accelerated course**:
    *Croix, 4 September*, A7 Unit 2 Q6 stays one all-or-nothing point. See §14.
- **Scope — unit assessments only, in both courses, plus any parallel form of one.** A7's
  Practice Test followed a day later because its own first line promises the same point values.
  **Unit reviews are NOT scored** — *Croix, 3 September: "I don't want to score reviews."* A
  review is practice, not a graded instrument, and a point value on one invites a student to
  treat it as a rehearsal for a mark rather than for the mathematics. Any weighting language
  already on a review comes off. Every worksheet is likewise untouched.
  **The pop quiz is no longer untouched.** *Updated 4 September 2026:* A7's Quiz 1 was still
  printing `/ 10` with question 7 weighted at four points and *"an answer with no work is half
  credit"* — the retired scheme surviving in the one paper the scope had left alone. It is now
  **out of 8**: one point per lettered part, question 7's a and b one point each, no partial
  credit. **Croix blessed that as an extension of this ruling rather than an exception to it**, so
  the scope now reads: **unit assessments in both courses, any parallel form of one, and the pop
  quiz.** See §14.
- **No scoring sheet.** *Croix, 3 September: "no need for a scoring sheet, a detailed key is
  good."* The marking instrument is the answer key: each part carries its `(1)` and each
  question a one-line scoring note saying what earns it. Nothing separate is built or maintained,
  which also removes a document that could disagree with the paper. §6 records the retirement of
  the printed sheet and what a key carries in its place.
- **Follow-through — yes.** Mark b against their own a. A wrong setup is not charged twice: a
  student who solves their own wrong equation correctly still earns the next part, and both keys
  say so in print. "Both cells right = the point" carries over unchanged.

Two consequences worth carrying into any conversion:

1. **An item's grain is now a scoring decision.** Splitting a question into a and b doubles what
   it is worth, so a split has to be about the mathematics rather than about the layout. Two
   further limits learned building M7 Unit 3:
   - **A split must reveal the student's reasoning, never dictate it.** Unit 3 Q4a asks how much
     higher a share was on one date than another, from a table of departures from the year's
     average. The good method subtracts the two departures and never computes either price,
     because the average cancels. Lettering it "find each price, then subtract" would buy a
     point by taking the better method away, so it stays one part.
   - **One instruction can be worth several points without being lettered several times.**
     "Determine the cost of each of the four items" is one applied decision — knowing that four
     price-times-quantity products are wanted — and four calculations. Lettering it a, b, c, d
     prints the number of multiplications on the page, which is the part being assessed. So it
     is one part carrying four points, and the key lists the four answers on four lines.
   *Settled, Croix, 3 September:* **split Q6.** A7 Unit 2 Q6 ordered a list for one
   all-or-nothing point while Q9 sorted six numbers for six.
   **Two corrections to that ruling as it was recorded here.** *First, a count:* the Q6 item has
   **five** numbers, not six. The six-count was corrected in an earlier round and this ruling's
   text never caught up, so "Q6 becomes six" was wrong twice over — a split would have made that
   paper **/38, not /39**. *Second, and it is a ruling, not a correction:* **the split was not
   adopted for the accelerated course.** *Croix, 4 September* — ordering a list is one judgment,
   not five — so A7 Unit 2 Q6 stays one all-or-nothing point and that paper stays **out of 34**.
   Recorded as a deliberate course difference in §14.
   The same shape existed on-level — M7 Unit 2 Q7 ordered four numbers for three all-or-nothing
   points — and **on-level takes the 3 September answer**: four points, one per number placed.
2. **Derive every printed number from one map.** The counts live in a single per-paper map; the
   header, the section banners, every printed value and the item ledger all come from it, and
   the build throws if they stop agreeing. *(The printed Scoring Sheet that ledger used to feed
   was retired on 4 September — §6. The ledger itself is kept and asserted against the paper's
   total at build time.)* This is not tidiness — A7's Practice Test shipped with
   stem values reading 3, 4, 9, 1, 1, 1, 9, 5, 1, 1, 1, 11 on a paper whose header said / 21, and
   a hand-typed table is how that happened.

**A consequence nobody chose: the conversion re-weighted the papers.** A procedural item is one
response by nature; an application is several steps that used to collapse into one. Converting
M7 Unit 3 to per-part scoring therefore turned a blueprint weighted 40 procedural / 60 applied
into a paper reading 10 procedural against 6 applied — an inversion produced by the scoring
grain, with nobody having decided anything about weighting. *Croix, 3 September, choosing the
repair over leaving it:* **"I like the split idea."** Part 2 was split along the steps the
mathematics already has and now reads 10 against 14, 58% applied. **Check the weighting after
any per-part conversion.** It is not visible in the total, which adds up correctly either way.

**Ruling 6 — Benchmark codes.** Croix, 1 September, choosing between options:

> Codes on title slides are fine. Keep them off student stuff like worksheets and tests.

So the `docscan` rule for this is scoped to **paper** — worksheets, assessments, handouts, keys —
and NOT to *student*, which would also catch every deck title slide and get itself switched off.
A teacher's copy of a key keeps its codes; it is a teacher surface by name. This closes the two
scope questions on-level had been carrying open.

## 13b(iii). Rulings — Croix, 13 and 14 September: the model changed

**Ruling 10 — the worksheet is gone, and so is the Ticket Out the Door.** *Croix, 13 September:*
"I'm over the worksheets. I've decided, I'm going to do the slides, whiteboards, ixl, and frequent
quizzes." And: "We'll cut exit tickets too." The period is now **slides → whiteboards → IXL**, with
his own quizzes on his own system. The whiteboard round goes from six questions to nine, and the
last one asks for written work — *"I'm gunna say yes to written work, but I'm probably not going
to grade super strictly about written work."*

- **The round takes the REMAINDER, and it is computed rather than fixed.** Croix: "I don't think
  20 minutes of board work is necessarily the best. Let's do 10-20 minutes. Leave a smidgen of
  time at the end for ixl." The on-level fork fixed it at 16 first and printed tables summing to
  51, 52 and 54, because each lesson had spent a different amount on the worksheet. Measured on
  the accelerated corpus, worksheet slots ran **5 to 13 minutes**, so a constant would have
  produced totals from 49 to 57. `planFromDeck` computes it and throws outside 10–20; all 16
  lessons land at **12 to 20** and every table totals 53 exactly. **A timing table that does not
  total 53 is a lie on a page a teacher is holding at 7:40 in the morning.**
- **§16 rule 4 is now MANDATORY, not opportunistic.** The round is the only formative instrument
  left in the period — no worksheet to mark, no ticket to read, and IXL takes an answer without
  ever seeing the work. When a board full of one wrong answer is the only signal a teacher gets,
  that wrong answer has to say what to reteach, so every distractor is a named error.
- **The retired worksheets become question banks, not deletions.** Every value in them was derived
  twice and read cold before it shipped, which makes them the one bank in the building that does
  not need re-checking — and Croix writes his own frequent quizzes now. They are refiled from
  `Worksheets/` to `Question Banks/`, which changes who they are FOR without throwing away the
  work. All 48 new whiteboard questions came out of them.

**Ruling 11 — no grey bars, and no study guides.** *Croix:* "No I meant the gray bars and the
stuff inside them..they often contain snarky or redundant information. Get rid of the whole
thing." And: "reference sheets are great. The study guides meh."

- **Do not key the deletion on the colour.** *This is the near-miss worth the whole entry.* The
  on-level rule was "delete a filled shape whose contents are prose and which sits low on the
  slide," with a 4.2in floor read off their corpus. Measured here before adopting it: this
  corpus's commentary panels start at **2.70in**, and the OTHER filled colour is **vocabulary
  definition boxes and table header rows**, one of which sits at 4.33in. That rule would have
  spared a hundred real panels and deleted vocabulary. Printing the contents of every candidate
  before deleting anything also caught the last one standing: the **learning target box** on every
  title slide. Keying on the `panel()` CALL is exact and needs no threshold — available only
  because these generators survived. **Print what you are about to delete, on your own corpus,
  every time.**
- **The sentence is not thrown away.** 151 panel sentences moved into the teacher's edition as
  `OFF THE SLIDE, YOURS TO SAY`. Some deserved to go; some were the point of the lesson. Off the
  slide either way, deleted only from the page and not from the teacher.
- **The Reference Sheet stays and the exam changes shape.** Croix: "Into the unit exam, probably
  still their notes. I'll still give them the reference sheet, but they can't use it on the test."
  So what a student carries in is their own notes, which makes the **Notes slides the only durable
  record of the unit a student owns**. That raises the bar on them; it does not lower it.

**Ruling 12 — no speaker notes on any slide.** *Croix:* "stop writing them in the slides. Only
write them on the te/lesson plan because I can't see them on the slides."

- **Measure the overlap before stripping anything.** The on-level fork measured first and found
  **64%** of their deck notes appeared nowhere in the edition; a straight `clear()` would have
  destroyed two thirds of their teaching commentary, and their generators were gone. Measured
  here the answer was **5%**, and for a structural reason that inverts the whole job: **the
  accelerated teacher's edition READS the deck's notes at build time** (§9, `deckread` →
  `telib.slideNotes`). Clearing the deck and rebuilding would have left every edition holding a
  timing table and silence, silently, on the next build.
- **So the fix is ownership, not surgery.** `addNotes` now records to a side-car JSON beside the
  deck and writes nothing into the `.pptx`; `deckread` reads the side-car. The note stays written
  beside the slide it belongs to, which is what has kept it correct — one source, one copy, and
  none of it on the slide. `readDeck` throws if a deck has both notes and a side-car, or neither.
- **The same instruction, in two trees, needed two different implementations.** Theirs was a
  text-merge with a fuzzy dedupe because they had orphaned artifacts; ours was six lines in a
  library because the pipeline was live. *An instruction is not a procedure. Measure your own
  tree before you copy one.*

## 13b(vii). Rulings 16, 17, 23, 24 — not yet carried

M7 holds rulings 16–28. The 20 September handoff sent A7 the texts of **18, 19, 20, 21, 22, 25,
26, 27 and 28**, which are below. **Rulings 16, 17, 23 and 24 are not in this file yet** — ask M7
for their texts at the next exchange and paste them here. Nothing in the A7 toolchain claims to
implement them.

## 13b(viii). Rulings — Croix, 20 September: the assessment and the practice model [both courses]

**Ruling 18 — two transfer items on every unit assessment, flagged in the key, never on the
practice test.** Two items on the real assessment are transfer items — the same benchmark, the
same DOK, a surface nobody has rehearsed — and they are on neither the practice test nor the
review deck. The key flags each one: *TRANSFER ITEM — not on the practice test. Same benchmark, a
surface nobody rehearsed.* A transfer item is not harder, not longer, not a chain. It is the same
one-operation question wearing different clothes. If it needs a step the unit did not teach, it
is a new question, not a transfer item, and it goes back.

**Ruling 19 — follow-through credit, mechanically.** One point per part, no partial credit,
stays. A later part is correct when the right operation is applied to the student's own earlier
value. The marker looks at the student's number for part a, does part b's operation to it, and
ticks if that is what the student wrote. It only applies where the work is on the page. The
student is told: *"If an earlier part is wrong, a later part still earns its point when the
right operation is applied to your own earlier answer — but only if that work is on the page."*

**Ruling 20 — one peer move, on a split board only.** *"No partner or group work, anywhere,
ever"* stays as the default. One move is allowed, and only one: when a hold-up-a-letter board
splits — no option holding about two-thirds of the room — sixty seconds of *convince the person
next to you*, then re-vote, then reveal. It is timed, it is scripted, it is triggered by the
board and not by the clock, and it is not group work. It costs a minute; the plan names where
the minute comes from.

**Ruling 21 — independent written practice is back, in a small dose.** The worksheet stays
gone. But whiteboards are teacher-paced and vanish when erased, and five minutes of IXL is not
deliberate practice. So: every lesson carries a short independent set — six questions, varied on
§16 rule 2's discipline, done silently after the boards, before IXL. Six, not twenty; the point
is pace and a written record, not volume. The teacher's edition carries the two-line variation
note. Where a lesson's minutes will not stretch, the set is the homework, and the teacher's
edition says so.

**Ruling 22 — one board per round carries a number that is not needed.** Ruling 15 stands for
the assessment: cut the reading, keep the math. It was slightly wrong for practice, because FAST
items do carry a figure a student has to read past. So on the whiteboard round, one board per
round carries a number the question does not need, and the teacher's edition names it. Not a
trick and not a chain — the same one-operation question with one extra figure in it. The
assessment is not touched.

*(The "ruling 15" that ruling 22 refers to is M7's ruling 15, on cutting the reading in
assessment items — not A7's former ruling 15, which is now ruling 31.)*

## 13b(ix). Rulings — Croix, 20 September: the plan and the teacher's edition [both courses]

**Ruling 25 — every lesson ships with a Florida-format lesson plan, and the MTRs are named in
it.** Info table, standards, MTRs with the evidence for each, learning target and essential
question, sequence table, gradual release, higher-order questions with DOK, checks for
understanding with the response to each, differentiation (ESE / ELL / enrichment), closure,
vocabulary, materials, homework. One page-set per lesson, 53 minutes. Applies to every lesson
built from here on.

**Ruling 26 — the teacher's edition is lean, and it is read in twenty minutes.** Croix:
*"Teacher's editions can be leaner and easier for me to read and follow along with. I should be
able to print out the teacher's editions, read them 20 minutes before class starts, and know
exactly what I'll be teaching."* Page 1 is the period: standards and target (quoting the
benchmark's Must / Must-not lines), the MTR, the timing table, and the three sentences to say out
loud today — nothing else on page 1. Then one line per slide, in slide order, in the voice of
someone standing beside you: what to say, what to watch for, the answer; a board's line carries
its answer, its named distractors, and the one thing to say when the room splits; no paragraphs.
Keys are not in the TE — they live in `Answer Keys`; the question bank commentary moves to
`Reference/BANK - Unit N.md`. Misconceptions to Watch stays, as a short list at the end, each
tied to the board that surfaces it. Four pages or fewer, printed; a TE that runs longer is cut,
not shrunk. Every "OFF THE SLIDE, YOURS TO SAY" line becomes the slide's one line; the phrase
retires.

## 13b(x). Rulings — Croix, 20 September: the test runs two days, and IXL is required [both courses]

**Ruling 27 — every unit test runs over two days.** Croix: *"I need two days for
assessments."* Day 2 is the same paper continued — students stop where the period ends and pick
up where they left off; it is not two papers. The reteach day is folded into the review day
(what the review boards expose gets fixed on the spot; the practice test is the homework), and
the test takes the next two school days. Neither test day is a Wednesday (43 minutes), so day 1
is a Monday or a Thursday; the two days never straddle a weekend or a break; the review day is
always the school day right before day 1, and any slack between the last lesson and the review
is a spiral day. Croix is fine with review days on Wednesdays, and allowed Unit 3's test to run
Tuesday–Wednesday (22–23 September) this once.

**Ruling 28 — IXL: every listed skill is required, to a SmartScore of 60 on-level and 67
accelerated, due next class.** Croix: *"Include the also consider. Students are expected to get
at least up to 60 SmartScore."* and, 20 September (late), *"Accelerated has smartscore of 67 and
on level is 60."* All skills IXL lists for the lesson are assigned — the numbered ones and the
"also consider" ones alike; nothing on the list is optional. Done means the SmartScore on each
skill: **M7 60, A7 67.** Assigned the day of the lesson, due at the start of the next class; the
five-minute block at the end of the period is the start, not the whole. When the next lesson
keeps the same skills, it is one assignment covering the run, due after its last lesson. A
lesson IXL lists nothing for assigns nothing new.

## 13b(xi). Rulings — Croix, 20 September: the state guides are the backbone [A7 first, both courses]

**Ruling 29 — Grade 8 B1G-M is the spine; Grade 7 B1G-M is the prerequisite map.** *Croix:*
"Grade 8 is the spine. Yes to all four." Every lesson serves a named MA.8 benchmark; the 17
carried MA.7 benchmarks are taught where the spine needs them; a lesson serving neither is
enrichment and is flagged, not silently built. The full map, the caps, the reference-sheet split
and the distractor catalogue are in `Reference/B1G-M BACKBONE.md`; the per-benchmark reading
record is `Reference/B1G-M READING NOTES.md`.

- **The guide's numeric caps are hard checks** (`capcheck`, a §13c check that fails the build:
  radicands ≤ 225, cubes in [−125, 125], sci-notation ± within 2 exponents, slope-intercept only,
  rotations about the origin, ≤ 20 points, two repetitions except coins, and the rest of the
  table). It runs on the Unit 1–2 question banks retroactively before Unit 3 starts.
- **The Reference Sheet follows the memorize/provide split literally.** Pythagorean Theorem and
  converse OFF (the state says memorize); circle, quadrilateral, cylinder, simple interest and
  F↔C formulas ON (the state says do not memorize); slope, the two triangle theorems and the
  conversion tables mirror the FAST sheet line for line.
- **Every distractor is recorded in the TE by its guide-named error**, with the benchmark cited.
  "Arithmetic slip" is not an error name; `distractorcheck` fails a whiteboard or assessment
  whose wrong option has no named-error line.

## 13b(xii). Ruling — Croix, 20 September: book order, three woven threads [A7]

**Ruling 30 — the year runs in Math Nation's unit order (3 → 17), with the Q4 Grade 8 content
woven in early.** *Croix:* "my dad and I decided to follow book order this year … Any way I can
weave it in a way where we are mostly teaching the same material but I get in some of those
things intermittently." So: no unit moves; three two-period threads sit inside the unit that
already teaches the same idea numerically — 8.AR.1.1 inside Unit 3, 8.GR.1.4–1.5 inside Unit 6,
8.DP.2.1–2.2 inside Unit 13 — and Units 14, 16, 17 open with a retrieval day from the thread's
bank. Paired book lessons run as one period; Grade-7-only units run short but are taught.
Unit exams are two periods; quizzes take the warm-up. The plan and its day table are
`Reference/A7 SCOPE AND SEQUENCE 2026-27.md`, generated by `tools/scope_calendar.py` — edit the
PLAN, never the table.

## 13b(xiii). Ruling — Croix, 20 September: no video warm-ups [both courses]

**Ruling 31 — there is no video slot in a period.** *Croix:* "Get rid of the video warm ups."
Math Nation's video openers (3.1.1 growth-mindset, 3.4.1 career profile, and any like them in
later units) are dropped, not shortened. Every lesson opens with the four-question spaced-retrieval
warm-up (yesterday / last week / last unit / prior-grade prerequisite). The Teacher Edition's
"What changed" list records each replacement so the book's numbering still maps.

## 13b(ii). Rulings — Croix, 6 September

**Ruling 8 — a question is never split across a page, and the paper is the price.**

> "add the extra page if it's needed."

Asked to choose between 22 questions that ran over a page break with every part still beside its
own answer space, and a printed sheet per student per copy to make them whole, he chose the
sheets. It is a standing ruling for the corpus, not a per-document call, so `pagebind.py` now
REPAIRS what it used to report and `PAGE BREAKS - for Croix.md` records the answer instead of
asking the question.

Two things this ruling does not do:

* It does not license shoving a question that cannot fit on one page however it is placed. That
  case is rendered, detected, the break taken back out, and the question listed.
* It does not license paying for a defect in the block detection. A break can push what follows
  it down by at most one page, so N breaks may cost at most N pages; growth beyond that means the
  blocks are wrong, and the document is left alone and reported.

**What it actually cost, measured after the fact: one page.** The Unit 1 unit assessment went from
seven to eight; every other document absorbed its repairs without growing. 924 printed pages
before, 925 after. The first attempt reported +7, and six of those seven were the block detection
swallowing the stimulus that introduces the NEXT question — question 4 of the 1.02 worksheets
owned the trail-mix recipe that sets up questions 5 to 8. **A ruling that costs paper is worth
measuring twice before you spend it**: the cheap version of "is this repair right?" is "what did
it cost, and does that number look like the thing I asked for?"

---

## 13c. What a check has to be, before it counts as one

Merged from both courses on 2 September. Each of these was learned by shipping something.

1. **A check that reports a finding and exits 0 is worse than no check,** because the next step
   believes it. Two had that hole. Both were fixed and each fix was verified by feeding the check
   an input that genuinely breaks its rule.
2. **A checker that reports correct work as wrong is worse than no checker.** Acting on a false
   finding *introduces* a mistake. An item a check cannot fully read is reported UNSOLVED, never
   wrong.
3. **The denominator is the finding.** Report what was NOT checked, not only what passed. A
   coverage line that says "483 of 546 expressions re-measured" is worth more than a green tick.
4. **A filter that silences a check is worse than a missing check,** because the silence looks
   like a pass. Any exclusion has to be justified by what it excludes, not by what it lets
   through.
5. **Verify in both directions before adopting.** Run it against the corpus, then against an
   input that genuinely breaks its rule, and record both. A check nobody has seen fail is a check
   nobody should believe. `mathcheck` does this on every invocation against 47 cases and refuses
   to speak if it fails.
6. **A check whose scope depends on a filename must accept every filename the corpus uses.**
   `docscan` classified by installed package name and misread every loose build name, reporting
   59 findings, none real.
7. **A threshold is a proxy. Ask the question the threshold stands in for.** *Accelerated
   course, 5 September.* `gdoccheck` allowed a document up to sixty runs in the fallback font
   and called anything above that a document set in the wrong face. It reported three Unit 2
   teacher's editions as documents Google Docs cannot import. Each carried about thirty cube-root
   radicals and nothing else — item 2 of this list, in the field. Two faults stacked: the counter
   was counting `w:ascii`, `w:hAnsi` and `w:cs` separately, so thirty runs read as ninety; and
   the cap was never the question anyway. The question is WHICH CHARACTERS are in that font, and
   a document set in the wrong face is a defect at one run while a page of cube roots is fine at
   three hundred. Replacing the cap with a list of the thirteen characters the corpus happened to
   contain was the same mistake one step later — a population taken from a snapshot instead of
   from the rule. The check now resolves the document's own face through `fc-match` and asks
   whether that face has the glyph: a character it cannot draw HAD to move, one it can draw never
   should have. `fixglyphs.py` had already written the principle in its own docstring — *"A hand
   written list is only ever as good as the last person's imagination; this asks the font"* — and
   the checker guarding its output was not following it.
8. **A probe that asks about the wrong population answers a question nobody had.** The first
   Google Docs glyph probe was written by hand and asked Croix about eight characters. The corpus
   carries thirteen, and the one it omitted — the cube-root radical, at 170 uses against the
   tick's 133 — was the most common of the set. `probe.py` now derives the characters from the
   shipped tree the same way `gdoccheck` does, and prints the population it found so a silent
   narrowing is visible. A question put to a person is a check like any other, and item 3 applies
   to it: the denominator is the finding.
9. **Ask of every check: what could I change that this would not notice?** *Both courses,
   8 September.* `docstale` attributes to each document the sources its build script RUNS. It
   never followed `require`, so a shared module — the file whose edit reaches the most documents —
   was named by no build script and belonged to no document. On-level: `wp4.js` is required by
   thirteen builders, `wp.js` by seven, `sgkit.js` by three, and an edit to any of them left every
   document in the corpus reported clean. Accelerated hit the identical hole the same week: an
   edit to the sizing of every expression image in that tree left **115 of 115 documents reported
   current**, because `lib.js` and `telib.js` write nothing and so were correctly classified as
   libraries and wrongly classified as irrelevant. Both now take the transitive closure of local
   `require`s; the on-level fix was verified in both directions by appending one comment to
   `wp.js`, which moved **68 documents** from clean to stale and back. *The `cat a.js b.js > c.js`
   form had been followed for weeks. `require` had not, for no reason except that nobody had yet
   edited a module.* **A check whose denominator excludes the thing that changed answers a smaller
   question while printing the same sentence**, and the way to find that before it costs you
   something is to name what it cannot see, out loud, in its own docstring.
10. **A mechanism written out twice is a mechanism that will be half-fixed.** *On-level,
   8 September, found within the hour of writing item 9.* The structural pass — separate touching
   tables, register namespaces, pin every layout, serialise — existed as six lines in
   `docxfix.fix()` and as the same six lines copied into `fixglyphs.py`. The prefix registration
   above was corrected in `docxfix`, the document was rebuilt, and the prefixes came out renamed
   anyway: **every build script runs the copy in `fixglyphs`, and the copy had not been told.**
   The two are one function now (`docxfix.repair`). This is §13's own subject arriving from
   inside the tooling rather than the documents, and it does not stop being the same defect
   because both copies were written by the same author on the same day.

   *Asked of the accelerated tree the same day, and the answer is a partial yes worth writing
   down.* All four pack scripts go through `finish()`, so the eleven-step sequence has one caller
   — but `repack2.py` carries a **subset** of it, `fixglyphs` + `glyphaudit`, run over the SHIPPED
   tree rather than the sources, and its own comment says why: the shipped set was once clean
   while the intermediate and both repack sources carried 4,188 characters with no glyph, waiting
   for the next rebuild. Measured on 8 September that pass changes **0 of 98** documents, so it is
   a verification that the source-side pass held, not a second repair.
   **The risk it leaves is the mirror of the on-level one:** a step added to `finish.py` would not
   appear there, and nothing would say so. So the subset is now asserted rather than assumed —
   `repack2` refuses to package if it names a tool `finish.py` does not run. *A deliberate partial
   copy is defensible; an undeclared one is the thing that half-gets-fixed.*

11. **A guard that reads the artifact but not the prose beside it has the blind spot of no
   guard.** *Both courses, 8 September.* §14's sentence stating how many checks each fork runs was
   wrong three times in one day — first against a table four hundred lines above it, then again
   when `exprsize` and `xmlshape` landed, and the *intersection* moved too, which is the number
   neither fork would have thought to re-check. The accelerated fork found the first error, wrote
   the correction in a covering note, and **shipped the file with the sentence unchanged** at
   `sha1 8a206d87a485`, where the on-level fork pulled it back out of the zip. Both forks' guards
   passed that file, because both read the table and not the paragraph. *A repair reported is not
   a repair applied*, and **anywhere a fact is stated twice, something has to compare the two —
   prose counts as a copy.** Both counts and the intersection are derived now, by `tablecheck` on
   one side and `speccheck` on the other, and both also fail on an `exchange:base` line left at a
   placeholder.

   *One implementation note, because it nearly made the guard theatre:* the first version matched
   one fork's exact phrasing and failed on the other's — bolded number words, and "accelerated
   twenty-six" where the other writes "accelerated runs twenty-six". A guard that fails on
   `**twenty-four**` and passes on `twenty-four` is checking punctuation, not arithmetic. Strip
   the emphasis, collapse the whitespace, match the SHAPE of the sentence, and accept digits or
   words.

   *Done on the on-level side too, and verified across three phrasings rather than one:* the
   guard now passes `on-level runs 24, accelerated runs 26, and 15 names appear in both`, passes
   the same sentence in unbolded number words, and fails when a single value is wrong in either
   form. **A guard tested only against the sentence it was written for has been tested against
   nothing.**

12. **A block boundary that depends on the order of the blocks is not a boundary.** *On-level,
   8 September, on the accelerated fork's question — "have you tested what happens if the two
   markers ever appear in the other order?"* No, and the answer was that it broke. The on-level
   slicer ran from its own marker to the OTHER fork's marker, which is correct only while `m7`
   happens to come first; reordered, each guard ran from its marker to the end of the file. Shown
   rather than argued: on a reordered copy of this file the old accelerated-block slicer read
   **50 rows into a 26-row table**, having swallowed the on-level one whole.

   Both forks' slicers now start at the first occurrence of their own marker and end at the next
   `<!-- suite:` marker of EITHER fork or the next `##` heading, whichever comes first — and then
   take **only the first table inside that**, because the accelerated block is followed, inside
   the same section, by a second table listing the repairs that fork runs in `finish.py`. Ending
   at the heading swept those two rows in and made the block report 28 where its own sentence said
   26: **a guard inventing a disagreement, which is worse than one that misses it**, because the
   next person spends the morning looking for a defect that is not there.

   The general form, and it is the one worth carrying: **a scoping rule that happens to work is
   indistinguishable from one that is right, until somebody moves something.** The cheap test is
   to move it on purpose.

   *And writing item 11 broke the guard item 11 describes, within the minute.* The worked example
   above — `on-level runs 24, accelerated runs 26, and 15 names appear in both` — is a sentence
   ABOUT §14's sentence, and an unscoped search found the example first and reported the real one
   as wrong. That is the third time this week a guard has matched the documentation of itself: the
   suite markers quoted in §14's prose, the block boundary that swallowed a neighbouring table,
   and now this. **A guard that matches on text alone will eventually match a description of
   itself.** Scope it to the section it is about — `speccheck` reads §14 alone — and expect the
   file's own examples to be the adversary, because a file that explains its guards is a file
   full of near-misses of them.

*Confirmed in the accelerated tree, 8 September, by reproducing it rather than reasoning about
it.* Of the two failures the on-level fork found by moving things on purpose, **one was live here
and one was not.** Swapping the two `suite:` blocks changed nothing — that slicer already ended at
the next marker of either fork. But adding a single worked EXAMPLE of §14's sentence, above the
real one, flipped the accelerated prose guard to reporting `on-level 99` and calling the true
sentence wrong. Unscoped text matching, exactly as reported. It reads only §14 now.

The confirmation arrived by itself an hour later: the on-level master that carried this finding
also carries **two worked examples of that sentence**, above the real one, because a file that
documents a guard is where near-misses of it accumulate. Adopting that file with the old unscoped
matcher would have failed on the documentation of the fix. **Scope first, then match** — and the
cheap way to find out whether your scope is right rather than merely lucky is to move something
on purpose.

### The suite, and what each check asks

*Two checks were RETIRED on 14 September, not loosened.* Ruling 10 removed the worksheet slide
and `decktime` asked whether that slide stated the minutes the plan left it — two records of one
fact, compared. There is no second record now: the whiteboard round absorbs the remainder and is
computed rather than stated, which is the stronger version of what the check was buying, and
`planFromDeck` throws if the remainder falls outside Croix's 10–20. Ruling 11 removed the study
guide and `guideleak` compared one against the paper it was allowed on; nothing we author now goes
into the unit exam with a student. **A check whose subject no longer exists either fails forever or
gets weakened until it passes, and the second is worse — it keeps a name in the suite and stops
meaning anything.**

*And the retirement found a hole in `tablecheck` itself.* Both calls were commented out with their
reasons above them, and `tablecheck` went on reporting 26 checks and calling the table clean,
because it matched `run("name"` as TEXT across the whole source and a comment is text. **A guard
that reads source rather than executed calls will believe a comment.** It strips comments now.



**This section is the one part of this file that cannot be merged, and that is a finding, not an
inconvenience.** Everything else here is a shared ruling: it is true in both courses or it is
wrong in both. A list of the checks that run is not a ruling — it is a *measurement of one tree*,
and the two trees have never had the same checkers. Merging it produced exactly the failure a
derived list is supposed to prevent: on 6 September the accelerated fork ran `tablecheck.py`
against its own `checkall.py`, found eight rows naming nothing it runs, and recorded them as
**"checks that do not exist anywhere in either tree."** All eight exist in the on-level tree, are
run by its `checkall.py` on every build, and report clean. The grep was sound; the tree it was run
against was one of two.

So the tables below are labelled by fork, and each fork's own guard reads only its own. The rule
this earns is in §14, where the courses' deliberate differences live: **a derived list belongs to
the tree it was derived from. Put a fork's name on it or do not put it in a shared file.**

<!-- suite:m7 — read by speccheck.py against the on-level checkall.py. Do not merge rows in. -->

**On-level (M7) — twenty-six, in the order `checkall.py` runs them,** and this table is checked
rather than maintained: `speccheck.py` reads `checkall.py`'s own run list and fails on a check
with no row, a row naming a check nothing runs, and a stated count that disagrees with the rows.
`mathcheck` is first because it is the only one that would matter if the rest were deleted.

| check | asks |
|---|---|
| `mathcheck` | is every arithmetic claim a student is told TRUE? |
| `xmlcheck` | does every XML part of every shipped document parse? |
| `glyphaudit` | does every character have a glyph in the font that will be used? |
| `imagedrift` | does every embedded figure match the library? |
| `indexdrift` | does each index match its source and its images? |
| `figglyph` | does any figure draw a non-ASCII character outside mathtext? |
| `barwidth` | is every stored expression image wide enough for its expression? |
| `plancheck` | do the deck and its printed plan both total 53 minutes? |
| `partsum` | does every block's stated minutes equal the minutes its own slides declare? |
| `speccheck` | does every spec copy match its master, does any of them still state a retired rule, does any of them still use the wrong pronoun for Croix, and does the M7 table above name every check that runs and only those? |
| `specdiff` | is any retired assertion still live anywhere in the tree? |
| `docscan` | does any shipped document break one of the standing rulings, on the surface that ruling applies to? |
| `boxcheck` | does any student page carry an answer box? |
| `pagecheck` | is any shipped page blank — and, reported beside it, is any page on a document with no work space suspiciously thin? |
| `buildref` | is every builder that writes a shipped document run by a build script? |
| `figscale` | do the geometry labels print at a legible size? |
| `exprsize` | does every expression in a document print at one digit size? |
| `pdftwin` | does every shipped PDF say what its document says? |
| `designcheck` | does every §16 claim in `designrules.json` hold — and how many lessons out of how many have claimed anything at all? |
| `guideleak` | does a study guide hand a student an answer to the paper it is allowed to go into? |
| `piglyph` | does any figure DRAW a capital Π where a lowercase π belongs? |
| `figstale` | has the source a figure is drawn from changed since the figure was drawn? |
| `docstale` | was every shipped document built from the sources it is recorded against? |
| `gdoccheck` | will every .docx open in Google Docs looking like the file we shipped? |
| `xmlshape` | did any post-build tool change XML it was not asked to change, diffed against the generator's own output? |
| `pagebind` | is any question split across a page? |

<!-- suite:a7 — the accelerated fork's list. Maintained from the A7 side, where `tablecheck.py`
     reads THIS BLOCK against that fork's checkall.py and fails on a check with no row, a row
     naming a check nothing runs, and a count that disagrees. Read from the on-level side but not
     verified there: neither tree can read the other.
     ROWS ARE BACKTICKED AGAIN, 8 September. They were stripped so that an on-level pattern
     scanning the whole file could not read them as claims about the on-level tree — a defence
     against a guard that had no boundary. Both guards now slice on these markers before they
     match anything, so the boundary does the work the punctuation was standing in for, and the
     table can be written the way every other table in this file is written. The marker is the
     contract; the formatting is not. -->

**Accelerated (A7) — twenty-four, in the order `checkall.py` runs them,** checked from that side by
`tablecheck.py`. Recorded here so each course can see what the other covers; from the on-level side
this is read, not verified.

| check (A7) | asks |
|---|---|
| `mathcheck` | is every arithmetic claim a student is told TRUE? |
| `glyphaudit` | does every character have a glyph in the font that will be used? |
| `imagedrift` | does every embedded figure match the library? |
| `docscan` | does any LIVE shipped document break one of the standing rulings, on the surface that ruling applies to? |
| `pdftwin` | does every shipped PDF say what its document says? |
| `shapeoverlap` | does any picture sit on top of any words? |
| `partsum` | do the per-slide minutes inside a block add up to the block? |
| `slideoverlap` | do any two lines of text collide, by rendering? |
| `offpage` | is every word on the page it is drawn on, read from the rendered PDF? |
| `exprcheck` | does the question print the values its key states? |
| `sheretime` | does every START HERE timing table agree with its decks? |
| `designcheck` | does every §16 claim in `designrules.json` hold? |
| `figstale` | is every figure newer than the generator that draws it? |
| `tedeck` | is every teacher's edition newer than the deck whose speaker notes it prints? |
| `docstale` | is every built document newer than the generator that writes it? |
| `piglyph` | does any figure DRAW a capital Π where a lowercase π belongs? |
| `gdoccheck` | will Google Docs — the editor Croix actually opens these in — import this .docx faithfully? |
| `emptypage` | is any shipped page BLANK — and, as a report beside it, how many are nearly empty? |
| `indexdrift` | does each index match its source and its images? |
| `speccheck` | does every spec copy match its master, does any of them still state a retired rule, and does any of them still use the wrong pronoun for Croix? |
| `tablecheck` | does the A7 table name every check that runs, and only those? |
| `xmlshape` | did any post-build tool change XML it was not asked to change — and were the namespace prefixes rewritten, reported once rather than once per tag? |
| `exprsize` | does every expression in a document print at one digit size? |
| `specdiff` | is any retired assertion still live anywhere in the tree? |

Two more run inside the accelerated fork's `finish.py` rather than in its `checkall.py`, because
they are REPAIRS and a repair belongs at the choke point every packaging script already passes
through. The on-level fork reaches the same two ends differently — `pagebind.py` is a CHECK here,
run in `checkall.py`, and the on-level builders bind a stem to its box at construction rather
than by writing `w:keepNext` afterwards:

| repair (A7) | does what |
|---|---|
| keepwith | writes `w:keepNext` so a stem stays with the box under it, THROUGH the writing room between them, and `w:tblHeader` so a real header row repeats across a page break |
| pagebind | renders the document, LOOKS at which page each answer box and number line came out on, and puts a page break in front of the question when the box did not come with it — then reports every question that still runs over a page break |

*What this table used to say, and what finding that cost.* Until 6 September the sentence above
said TWENTY, the table named nineteen, and the file recorded the gap as an open question **for a
person** — twice, in two forks, neither of which ever identified the twentieth. It was worse than
a miscount. Handing the question to a script found, in the accelerated tree, that **nine checks
ran with no row at all** — `shapeoverlap`, `decktime`, `partsum`, `slideoverlap`, `offpage`,
`exprcheck`, `sheretime`, `figstale` and `docstale`, which is coverage nobody reading this file
knew existed.

**And it found the merge defect too, without recognising it as one.** The eight rows it could not
account for — `xmlcheck`, `figglyph`, `barwidth`, `plancheck`, `boxcheck`, `pagecheck`, `buildref`,
`figscale` — were not phantom coverage. They were the on-level fork's coverage, correctly
recorded, read in a tree that does not contain it. The conclusion drawn was "not moved, not
renamed, not present"; the true statement was "not present **here**." Two of the three questions
`tablecheck` asks are tree-local and the third — *does this row name something real?* — is the one
that cannot be answered from inside a single tree at all. The file's own §13c item 3 applies to
the finding as much as to the check: **the denominator is the finding**, and the denominator here
was one tree out of two.

The evidence, so this is settled by measurement rather than by two people asserting at each other:
every one of the eight is a file in the on-level tree, is invoked by name from `checkall.py`, and
printed a clean result in the run of 7 September — `xmlcheck` 86 lines, `figglyph` 75, `barwidth`
103, `plancheck` 62, `boxcheck` 88, `pagecheck` 91, `buildref` 117, `figscale` 111. The accelerated
file makes the point against itself one paragraph later, in a sentence written before the grep:
*"`plancheck` sums the whole deck and has never looked inside a block."* A tool that has never
looked inside a block is a tool that runs.

**The half of the finding that survives intact, and it is the important half.** One row was doing
active damage in the accelerated tree: `emptypage.py` declined to fail on a blank page and said so
in its own docstring, on the grounds that "`pagecheck` already asks whether a page is BLANK."
`pagecheck` does — in the on-level tree, where it was written after two blank pages shipped, and
where it still fails on one. It does not exist in the accelerated tree, so over there the sentence
was true of nothing and for weeks nothing asked whether a shipped page was empty. **A tool that
declines a job by naming another tool has just made a claim about the world, and it is the kind of
claim nobody checks, because it reads as delegation rather than as an assertion.** Note what the
claim actually was: not false, but *true somewhere else*. A borrowed docstring carries its
tree with it.

*Checked here on 7 September:* no on-level checker declines a job by naming another checker.
Nothing in the tree matches "already asks", "already does", "handled by", "covered by", "left to"
or "delegat*" in that sense. The rule is recorded ahead of the defect rather than after it, which
is the only time that is cheap.

The general rule this earns: **a list of what a system does is a claim about that system, and a
claim in a table outranks a principle in prose for anyone skim-reading — which is exactly who
reads a table.** §9 already records this once, about a slide count that stood for a week against
the rule directly above it. It is the same failure. Any list in this file that a script could
derive should be derived, and both of these now are — each against its own tree.


*Open item O2 from the 5 September merge — "the line says twenty and the table names nineteen,
and neither fork identifies the twentieth" — is **closed, 5 September**. The twentieth is
`figstale`, adopted from the accelerated course in the same round and built on-level that day; the
merge could not have known, because it was listed under §0 and under "adopted and not yet built"
in the same file, and it was in flight while the merge was written.*

*The number is no longer typed. `speccheck` now reads `checkall.py`'s own run list and reports
a check that runs with no row, a row for a check that does not run, and a count that disagrees
with its table. Two files asserting the same fact with nothing comparing them is the shape this
whole section exists to stop, and this table had been one of them for two days — the count was
edited by hand each time a check was added, and it was wrong within a week.*

**What the canary set came back with, 5 September — and it was not what I expected.** Croix
opened five files in Google Docs. The worksheet was fine. The KEY was wrecked: every repeating
decimal showed as a bare `0.`, `0.45` broke as `0.4 / 5`, and a one-line note wrapped a word per
line — *"caref / ul — / read / it"*.

One cause for all of it, and it was not the nesting I had flagged as the risk. **Google Docs welds
two tables with nothing between them into one table and imposes a single grid on the result.** On a
key each question emits a stem table of `[700, 8660]` followed immediately by an answer table of
`[700, 500, 2000, 500, 2000]`; the merged table takes the narrow grid and the stem's wide cell
becomes 500 twips. **On the student worksheet the two tables happen to have identical widths, so
the same weld is invisible** — which is exactly why the worksheet looked right, the key did not,
and nothing here could tell them apart. 528 occurrences across 66 documents. LibreOffice and Word
keep the tables separate, so every PDF was correct and no check had anything to compare.

`fixglyphs.py` now puts a 1pt paragraph between adjacent tables at build time — it is the only
step every build script already runs on every document, so the fix reached all 106 without editing
thirty build scripts — and `gdoccheck` guards it.

**And "a couple of breaks" was about the page breaks, not the file.** Two forced breaks had spread
nine short questions and a small table across three pages, each a quarter used. Both removed; the
same content and the same working room now sit on two full pages. `pagecheck` reports thin pages
from that day, **scoped to documents with no work space** — a student page is allowed to be mostly
white, because that white is where they work, and a check that objected to it would be objecting
to rule 2. Seventy are reported on keys and teacher's editions, to be closed as each unit is next
opened.

**The lesson is the one this file keeps relearning from a new direction.** I guessed nested tables
and shipped a canary to test the guess; the canary found something else entirely, in the half of
the pair I had least reason to suspect. **Ask the renderer. Do not model it.**

**RULED, Croix, 6 September: "Add the extra page if it's needed."** A question is not split
across a page. If making it whole means starting it on a fresh sheet, the sheet is the price. He
answered once, for the corpus, so it is a standing ruling and not a per-document call. `pagebind`
reads the printed page and reports a stem separated from its own parts or receptacle; it found two
on its first run, both in Unit 2, and **the ruling cost this corpus nothing — 1,137 printed pages
before and 1,137 after**, because the questions that were splitting were short enough to move
whole.

**The nesting in these documents is load-bearing, and that is now measured rather than assumed.**
Every question here is built inside a one-cell `cantSplit` table — precisely the nesting the Google
Docs pass was tempted to flatten. The accelerated course flattened theirs and lost page cohesion
with it: `w:keepNext` is the documented remedy and **does nothing for a table**, which every
question stem in both corpora is, and on a data table the same property is read as a row
instruction and splits the table it was meant to hold. They needed a four-hundred-line repair tool
to put back what the wrapper had been doing for free. So the argument for removing the nesting is
a rumour about an importer, and the argument for keeping it is a ruling and a measurement.

*The rumour is now settled, and it settles in favour of nesting.* The on-level canary was five
files, two of which nest **three deep** — their Unit 3 assessment and its key. The README named the
nesting question and asked Croix to look at those two specifically, and he passed them. Nested
tables import into Google Docs correctly; 63 of 106 on-level documents nest and stay nested.
**The accelerated `gdoccheck` nonetheless keeps its nested-table rule fatal, and the reason is now
a preference rather than a fear:** nothing in either accelerated package nests, `pagebind` does the
keep-whole job by measuring, and a rule that costs nothing and must be argued with before removal
is cheap insurance. What matters is that the rule no longer *claims* an importer limitation — its
printed message says which it is, because a checker's message is read far more often than its
docstring.

*And how the accelerated side got this wrong in the safe direction.* Its record said the question
was "not known", and listed what would retire it: a nested .docx imported by Croix and looked at.
That had already been done, in the other tree, and the sentence was written without asking.
**Careful reasoning about the limits of your own evidence is still reasoning about one tree.**
The scope rule in §14 cuts both ways: it stops you asserting what you cannot see, and it should
also stop you concluding "unknown" when the fork that can see it already looked.

**Every table's layout is pinned, and this is the more important of the two Google Docs fixes.**
Absent `w:tblLayout` means AUTO, and auto lets the renderer recompute every column from its
contents. **1,906 of 1,906 tables in this corpus were in that state** — every table. The
accelerated course found it when Croix opened their Unit 1 assessment and question 1's stem came
out one or two characters per line down a thirty-pixel column, while question 2 three inches below
was perfect, because its stem was long enough to force the column open.

The general form is worth more than the fix: **every check in this repository asks whether two
artifacts AGREE, and none asks whether a document is fully SPECIFIED.** An unstated property is not
a property with a safe default; it is a decision handed to whoever opens the file, and a correct
PDF means only that one renderer guessed the way the author meant. Where a grid does not sum to its
declared width the grid is scaled UP, not the width down — an auto renderer stretches those columns
and pinning without scaling would visibly shrink the document. Verified by rendering: layout text
and page count identical, document by document.

**And the repair broke a check, which is the rule working.** Rewriting `document.xml` through
ElementTree closes empty elements as `<w:tag />` where the docx library writes `<w:tag/>`, and
`mathcheck` reported 48 correct superscripts as wrong arithmetic — `3.14 × 4²` read as
`3.14 × 42`. Both halves were fixed: the pattern now tolerates the space, *and* the serialiser
writes the shape the rest of the toolchain expects. Either alone would have left the next tool
exposed.

**And it broke a second thing that nobody looked for until the accelerated fork named the class.**
*7 September.* The same round trip also RENAMES the XML namespace prefixes: `<wp:inline>` comes
back as `<ns2:inline>`, `a:` as `ns3:`, `pic:` as `ns4:`. Measured across the shipped set, **61 of
106 documents carry renamed prefixes and none carries the original `wp:`**. Prefixes are arbitrary
in XML — the namespace URI is what binds — so Word, LibreOffice and Google Docs all read these
files correctly, and Croix opened them on 6 September and passed them. It is not a defect in the
documents.

It is a defect in what the tooling can assume. `exprsize.py`, written the next day, needed the
printed size of every embedded figure; the obvious pattern `<wp:extent cx=...>` matches **zero
images in the shipped corpus** and would have printed a confident clean over 844 figures it never
saw. A pattern that finds nothing looks exactly like a corpus with nothing wrong in it.

Two rules out of one measurement. **A post-build tool changes more than it was asked to, and the
extra changes are invisible until something downstream depends on the part it changed** — which is
what the accelerated fork's `xmlshape` exists to find, and which applies here more than there,
because `docxfix` is the only tool in either tree that parses rather than pattern-matches.
**And: never write a reader that hard-codes a namespace prefix.** `(?:\w+:)?` costs six characters
and removes the whole class. *Swept on the accelerated side the same day, after the on-level fork
asked:* three readers there named a literal prefix — `gdoccheck`'s anchored-drawing scan, and
`<w:drawing>` as a literal substring in both `keepwith` and `pagebind`. Nothing in that tree
renames prefixes today, which is precisely why it was worth closing: the class costs nothing to
remove and everything to discover.

**And on the on-level side the fix went one level further down, to the tool that caused it.**
Patching readers closes instances; the rename itself was the defect. `docxfix` registered exactly
one prefix — `w` — so ElementTree invented names for every namespace it had not been told about.
It now registers **every prefix the document itself declares**, read off the file rather than
listed in the code, and from the WHOLE file rather than the document element: the docx library
declares `wp:` on the root but declares `a:` and `pic:` inline on each `<a:graphic>`, so a
root-only scan restores two thirds of the prefixes and silently invents the rest — which is worse
than not trying, because it looks finished. Verified on a freshly built key: 23 `wp:inline`
elements and zero invented prefixes, where the same file had carried 23 invented ones an hour
earlier. The whole corpus was rebuilt for it. **The reader patches stay** — a prefix-agnostic
pattern costs six characters and is right whatever the writer does — but they are now
belt-and-braces rather than the repair.

**A check that reports a rename tag-by-tag has not reported it.** *Accelerated, 7 September, on
the on-level fork's question:* asked whether `xmlshape` would catch a prefix rename or drown in
noise, the honest answer was the second — renaming the prefixes in three documents made it print
**"3,966 tags changed"** under twenty near-identical lines, with no sentence naming the cause. It
now compares the prefix-to-URI map FIRST, reports a wholesale rename as one finding that names the
prefixes and what breaks, normalises by URI, and diffs what is left: the same experiment now
prints one line, and a rename hiding a real reshape prints one line plus the three real changes.
*This is the `emptypage` shape one level up — a check that reports so much it stops being read is
a check that has stopped running.* **Asking another reader "would this drown?" is worth more than
asking yourself "is this correct?", and it was their question, not mine.**

**The renderer that matters is the one the reader uses.** *Croix, 5 September:* "When I try to
open the doc files in Google Docs, the formatting is usually way off. I have to use the PDFs in
order to print something useful, but I don't have the ability to edit PDFs for when I want to do
that." The .docx set exists so he can adapt materials; the only faithful copies were the ones he
cannot edit, which makes the editable half dead weight in every package.

**Why nothing here could see it.** `fc-match` resolves Century Schoolbook to TeX Gyre Schola, a
metrically compatible clone, so every PDF this tree has ever rendered was correct — the fonts were
never wrong *here*. Google Docs has neither face and substitutes silently, and a substituted metric
moves every line wrap, table row and page break with it. **A document can be correct in every
renderer you own and wrong in the one your reader uses**, and no check that reads the file alone
will ever say so. The body face is now **Tinos**, which is native to Google Docs, is metrically
identical to Times New Roman so even a substitution lands in the same place, and — unlike Georgia —
can be installed here, so the PDF this tree renders is set in the same font the teacher sees. The
whole corpus came out 23 pages shorter and nothing else moved.

`gdoccheck` reads the XML as the importer will: fonts outside the Docs-native set, table nesting,
anchored drawings, floating text boxes, exact-height rows, welded tables and unpinned layouts.

**Nesting was reported rather than failed, and on 6 September it was settled by the reader.** Croix
opened the third canary — five documents, nested tables among them, each beside its PDF — and
passed them. **Nested tables are fine in Google Docs.** The count is still printed, because it is a
real structural fact and the next importer may disagree, but it is no longer a suspicion.

That is the whole argument for the canary, stated as a cost. The accelerated course flattened their
wrappers during the same compatibility pass, lost page cohesion with them, and needed four hundred
lines to put back what a one-cell `cantSplit` table had been doing for free — for a defect that,
measured, was not there. **Four files and one teacher's morning were cheaper than the rebuild, and
cheaper again than the rebuild's own repairs.**

**The same defect twice in a fortnight: a source corrected, and the output never rebuilt.**
`analyse` was fixed in `te0307b.js` on 4 September and shipped in the teacher's edition through
three separate spelling passes. The accelerated course lost a capital Π to the identical shape a
day later. Both are the same sentence: **every check in this file reads the shipped file and asks
whether it is correct, and a document built from last week's builder is correct.** It is just not
the one the repository says it is. `figstale` asks the question of figures and `docstale` of
documents, and between them the answer is now a fingerprint rather than a memory.

Two things `docstale` got wrong first, both worth keeping because both are the same mistake:
`os.path.splitext("M7 2.04  Teacher Edition")` returns `("M7 2", ".04  Teacher Edition")`, because
every document in this tree has a dot in its stem — so every teacher's edition, worksheet and key
collapsed to one key and the check reported 42 documents covered and 91 blind. Then
`build_guides.sh`'s six documents, carried as one pipe-joined shell string, matched as a single
130-character filename. **A check that invents a blind spot is as misleading as one that hides
it**, and both times the number it printed was confident and wrong.

**A repair is a new claim, and gets read like one.** *Accelerated course, 4 September.* Two
whiteboard slides had text running off the page; the repair shortened the stem so hard that the
question lost the numbers its own reveal used. The off-page checker passed it — nothing was off
the page any more. Three of that round's 46 findings were introduced by the repairs of the round
before, and every one was caught by the next reader rather than by any check. **A check confirms
that the thing you broke is no longer broken. It has no opinion about what you broke instead.**
So a fix is re-read at its settled content, the same way the original was, and "the check passes
now" is the weakest possible evidence that a repair worked.

**A rule about a setting is weaker than a measurement of the output.** The two courses chose
OPPOSITE mathtext fontsets to keep π lowercase — stix over there, dejavuserif here — and both were
right, and neither rule prevented anything: accelerated shipped four capital Π glyphs on a page a
student holds, in figures that had no generator for a staleness check to compare against and were
not on the re-render script's hand-typed list. `piglyph` opens the image and asks what character is
drawn. That is why it can be adopted by both courses without either changing its fontset.

**Adopted from the accelerated course and not yet built here** — recorded so the gap is visible
rather than forgotten: `rederive.py` (the reading ledger — has a human read THIS exact version,
fingerprinted by text plus the hash of every embedded image), `offpage.py` (is every word on the
page it is drawn on, read from the rendered PDF), and a START HERE timing check. `pdftwin` was
the first of the set adopted; `guideleak`, `piglyph` and `figstale` followed on 4 and 5 September,
`exprsize` on the 7th and **`partsum` on the 8th**, and all now run in `checkall.py`.

**`partsum` is §13c item 9 used the way it is meant to be used — before the defect, not after.**
The question is *what could I change that this check would not notice?*, and put to `plancheck` —
which compares one number, 53 minutes, on the deck and on the printed plan — the answer is: move
two minutes from one block to another. Both totals still say 53 and the lesson a teacher runs from
has changed. So `partsum` reads the two artifacts row by row: every slide's speaker notes open
with `(N min)`, the teacher's edition prints `slides · minutes · what happens`, and each row's
stated minutes must equal the sum its own slides declare. **27 lessons, 298 rows, none
disagreeing.** A check whose first run is clean is not wasted — it is the difference between
believing two artifacts agree and knowing it, and `plancheck`'s totals had been believed for three
weeks. Verified in the other direction by editing one cell of a shipped teacher's edition from
4 min to 6, which it named.

**`xmlshape` is adopted, and this tree can pair its whole corpus.** *8 September.* It asks the
one question nothing else here asks: not *is the shipped file correct*, but *did the tools that
edited it after its generator change anything they were not asked to change?* `docxfix` has
reshaped this corpus twice and both times a downstream tool found it by breaking — `<w:tag />`
with a space, which made `mathcheck` read `3.14 × 4²` as `3.14 × 42`, and the prefix rename that
would have let a new check print a confident clean over 844 figures it never saw.

The accelerated fork can pair 50 of its 98 documents, because several of its generators write
into the pack tree and are edited in place; the rest are honestly outside its population, and it
says so. Here **106 of 106 pair**, because every document passes through `fixglyphs.fix()` exactly
once and that function stashes `word/document.xml` into `xmlbase/` at its first line — before its
own glyph pass, which is one of the tools being audited. *Coverage by construction beats coverage
by remembering, and the place to get it is the one function everything already goes through.*

Four benign transformations had to be separated from real ones before the check could say anything,
and each was a lesson in what "changed" means:

* **Prefix renames** are one finding, not four thousand — normalise by URI first. *(The
  accelerated fork measured the alternative: 3,966 tag-level findings and no sentence naming the
  cause.)*
* **`&apos;` and `&quot;` written out.** ElementTree prefers the literal character. This cost the
  pairing before it cost the diff: two apostrophes made a shipped key ten characters shorter than
  its baseline, and **70 of 106 documents reported UNPAIRED** — a check quietly halving its own
  denominator and printing the smaller number as though it were the corpus.
* **Empty elements collapsed** — `<w:t xml:space="preserve"></w:t>` to `<w:t
  xml:space="preserve"/>`. The same shape class as the `<w:tag />` that cost 48 false findings,
  from the other direction. Normalising is safe here in a way that *allowing changes to `<w:t>`*
  would not be: the check pairs documents on their visible text, so a tool that altered a
  character would report UNPAIRED, not clean. **The pairing key guards the text; the
  normalisation only forgives how an empty one is spelled.**
* **Declarations hoisted to the root, and unused ones dropped.** The docx library declares `a:`
  and `pic:` inline on each `<a:graphic>`; the round trip declares them once at the top. *Where* a
  namespace is declared is presentation; *whether* it is in scope is meaning — so the line diff
  ignores declarations and the URI SET is compared separately. Thirty unused extension namespaces
  are genuinely dropped, each checked before it was listed, and they live in `xmlack.json` with
  their reason. **Acknowledged, not reported-and-passed:** a check that prints a finding and exits
  0 is worse than no check, and anything dropped that is not in that file fails the run.

Verified in the other direction by deleting three `<w:jc>` elements from a shipped key, which it
named.

**`tedeck` was offered and does not apply here, and the reason is worse than the defect it
guards.** It asks whether a teacher's edition is older than the deck whose speaker notes it
prints. Measured before answering: **0 of 30** of the 2.04 deck's note openings appear anywhere in
its teacher's edition. The on-level editions do not read the deck and do not reprint its notes —
they print a plan table and their own commentary. So there is no stale-read to guard, and the open
item recorded here for two weeks (*"the teacher's edition carries an unguarded second copy of the
deck notes"*) **was itself wrong, and was believed because nobody had opened both files side by
side.** What the editions actually restate is the deck's slide ranges and minutes, which is what
`partsum` now compares. *An open item is a claim like any other and goes stale like any other.*

**`figstale` was built on 5 September and its first design was wrong in an instructive way.** The
obvious implementation asks whether a PNG is older than the `.py` that writes it. Run once, that
reported **952 of 1,522 figures stale — 828 of them from `bars.py` alone**, which is append-only
by design and says so in its own header, because rebuilding it once destroyed 156 entries.
Appending a new bar does not stale the eight hundred already written. A check that reports correct
work as wrong is worse than no checker, so the question is asked properly instead: a bar declared
as an expression is fingerprinted by **its expression**, so appending leaves every existing
fingerprint untouched and editing one character stales exactly one figure; a figure a generator
plots is fingerprinted by **its generator file**. Both were verified by mutating one of each and
confirming the finding was that figure and no other.

---

## 14. Where the courses deliberately differ

Recorded here so a difference between the two sets reads as intentional rather than as drift.
Everything not listed is shared. Merged from both courses' copies on 2 September; the accelerated
worker's entries are carried over in their own words except where the two-document model of
§13b ruling 4 required them to be restated in its vocabulary.

**The eight were verified from the accelerated side on 7 September**, against the on-level
package rather than by taking the correction on trust: all eight files are present in
`Reference/`, their line counts match the figures reported (86, 75, 103, 62, 88, 91, 117, 111
for `xmlcheck`, `figglyph`, `barwidth`, `plancheck`, `boxcheck`, `pagecheck`, `buildref`,
`figscale`), and each is invoked by name from that fork's `checkall.py`. *A retraction is a claim
too, and the fork that got it wrong is the one that should check it.*

**A derived list belongs to the tree it was derived from, and a shared file must say so.** *Both
courses, 7 September 2026 — recorded here because it is the first difference that was not
intentional and got merged anyway.* The two forks have never run the same set of checkers: on-level
runs **twenty-six**, accelerated **twenty-four**, and **sixteen** names appear in both. For four days
one table in §13c tried to describe both. What that produced was a script in one tree reading a row
written from the other, finding nothing behind it, and recording the honest conclusion its evidence
supported — *"eight checks that do not exist anywhere in either tree"* — about eight checks that
exist, run and pass in the tree it could not see. Nothing was done carelessly. A correct tool ran a
correct query against the wrong denominator, and a shared file is what supplied the wrong
denominator.

*And then this paragraph did it again, twice, in one day.* It was written saying "twenty-three,
twenty-five, fourteen" while the table four hundred lines above it already said twenty-four. The
accelerated fork read the file, **spotted the disagreement, said so in its message — and shipped
the file back with the sentence unchanged**, because the correction lived in the covering note and
the artifact was never edited. By then both numbers were wrong: on-level had added `exprsize` and
accelerated had added `exprsize` and `xmlshape`, so the true figures were twenty-four, twenty-six
and fifteen.

Three failures, one shape. **A prose sentence restating a number that a table already carries is a
second copy, and §13c's guard read the table and not the prose.** The count in the table has been
derived since 6 September and has never been wrong since; the count in the sentence beside it was
wrong within a day, three times. So the guard now reads this sentence too — both counts and the
size of the intersection, all three against the two blocks in §13c — and `speccheck` fails on any
of them. **The rule is not "check the table". It is: anywhere a fact is stated twice, something
has to compare the two, and prose counts as a copy.**

*A repair reported is not a repair applied.* The accelerated fork's message named this defect
precisely and its file still carried it; a fix that exists only in the covering note is a fix
nobody has.

Three things follow, and they apply to anything else in this file a script could generate:

* **A list a script derives is a measurement, not a ruling.** Rulings merge, because they are true
  in both courses or wrong in both. Measurements do not, because they are true of one tree at one
  time. When both are in one file, the merge treats them alike and the measurement is the one that
  ends up lying.
* **Label it with the fork it measures, and let each fork's guard read only its own.** §13c's two
  tables carry `<!-- suite:m7 -->` and `<!-- suite:a7 -->` for exactly this: `speccheck` reads the
  M7 rows against the on-level `checkall.py` and does not look at the other table, and the A7 rows
  are written without backticks so no on-level pattern can mistake them for a claim about this
  tree.
* **The other fork's list is recorded, not verified, and it must say which.** Neither worker can
  read the other's tree. A row copied across is worth having — it is how each course learns what
  the other covers, and it is where `pdftwin`, `guideleak`, `piglyph` and `figstale` came from —
  but it is hearsay until that fork's own guard reports on it, and a file that does not mark the
  difference invites a grep that treats it as fact.

**The general form: a claim's scope is part of the claim.** "This check does not exist" and "this
check does not exist *here*" are different sentences, and the shorter one is the one a reader acts
on. §13c item 3 already says the denominator is the finding; this is that rule applied to a
sentence rather than to a corpus.

**A7 — the pop quiz is scored per part too.** *(Croix, 4 September 2026.)* §1 rule 6 and §13b
ruling 5 both said the pop quiz was untouched by the per-part ruling, and that was true when it
was written. On 4 September a reader found A7's Quiz 1 still printing `/ 10` with question 7
weighted at four points and *"an answer with no work is half credit"* — the retired scheme
surviving in the one paper the scope had left alone. It is now **out of 8**: one point per
lettered part, question 7's a and b one point each, no partial credit. **Croix blessed this as an
extension of the ruling rather than an exception to it**, so the scope in §1 rule 6 and §13b
ruling 5 now reads: unit assessments, any parallel form of one, and the pop quiz. Worksheets carry
no point values at all.

**A7 — Unit 2 question 6 stays a single all-or-nothing point.** §13b records a 3 September ruling
splitting an ordered list one point per number. **Not adopted for the accelerated course**
*(Croix, 4 September)*: ordering a list is one judgment, not five, and a student who has three of
five in the right places has not ordered the list. The A7 Unit 2 assessment stays **out of 34**.
*This also fixes a count in §13b's own text: the item has **five** numbers, not the six that
ruling recorded — the count was corrected in an earlier round and the ruling text never caught
up — so a split would have made that paper **/38, not /39**.* On-level is unchanged: M7 Unit 2 Q7
is split four ways under the 3 September ruling. This is the one place the two courses score the
same shape differently, and it is deliberate.

**A7 — what a student may carry into the assessment fades across the year.** Q1: notes and the
completed Study Guide. Q2: the completed Study Guide only, and students may annotate it. Q3: one
sheet of notebook paper. Q4: one note card. **The condensing is the instruction** — by Q4 the
student has to decide what actually matters.

*Restated 2 September in the two-document vocabulary, because A7's entry and the new model used
the words differently and one rulebook cannot hold two definitions of "study guide".* Under §13b
ruling 4 both courses build a **Reference Sheet** (complete, filled in, studied from, **not**
carried in) and a **Study Guide** (blanks and frames the student fills in, **carried in**). The
fade is entirely about the carried-in document, so it is a schedule applied to the Study Guide and
the model is untouched by it. Two consequences: the Reference Sheet is never part of the fade,
because it was never carried in; and the A7 **Study Guide carries no page cap**, because it has to
survive being condensed twice. Its last page carries a line telling students that the support is
withdrawn on a schedule — **next QUARTER** the guide is all they get, then a sheet of notebook
paper, then a note card — and from Q2 a blank note-card-sized box beside it.
*This line said "next unit" until 4 September, which is false: Units 1 and 2 are both inside Q1
and notes are allowed on both. The four shipped documents were repaired first and this line — the
line they are built from — was not, which is §13's own failure arriving from inside §14.*

**SETTLED, 4 September 2026: A7 is on the two-document model now, not at Q2.** Croix ruled it
the same day the review raised it. What changed:

- **Reference Sheet** — unchanged. Complete and filled in, organized by topic. The student studies
  FROM it and does **not** carry it into the test.
- **Study Guide** — now **blank**: per tested skill, the name, the point value, numbered ruled
  lines for the method in the student's own words, the example's task printed with ruled space to
  work it, and a ruled line for the mistake that catches them. **Filling it in is the studying.**
  The copy in the student's own handwriting is what they carry in.
- **Study Guide COMPLETED** — new, in `Answer Keys/`. The teacher's copy: projected, or handed out
  at the end of the filling-in session so a student can check their own. **Not** a student
  document and deliberately not in `Handouts/`, where one would be picked up by mistake.

Both forms come from **one generator** branching on `FILLED = process.argv[2] === "filled"`, so
the blank and the completed copy cannot drift apart. Each blank skill carries an explicit `ask` —
the instruction for the example the completed copy works — and the generator **throws** if a skill
has none, so no skill can ship with an empty panel. The asks reuse the completed copy's numbers,
so no new mathematics entered the corpus and `guideleak.py`'s token set is unchanged.

**The fade is unaffected and its words now mean one thing.** Q1: notes and the (student-filled)
Study Guide. Q2: the Study Guide only, annotated. Q3: one sheet of notebook paper. Q4: one note
card. The fade was always about what a student may CARRY IN, and what they carry in is now
unambiguously the document they filled in themselves.

**Judged and kept, 5 September:** the Reference Sheet's §7 cube entry says the cubes past ±125
"still appear on the worksheets" while §1's note says "on the worksheets and in the study
guide" — §7 is less complete but not false, so it stands. And the A7 1 completed copy says
"every number here differs from the ones on the Unit 1 assessment", which is true item for
item and false digit for digit (0, 4 and 7 appear on both). Both were raised by a reader,
checked, and left alone; recorded so the next reader does not re-raise them.

**Judged and kept:** B5 checks the equation B2 solved, and C5 answers the situation C4 set up.
A reader flagged that as handing the student an earlier answer. It is the chain working: you
check the thing you just solved, and you interpret the situation you just modeled. Breaking the
pair to avoid the repeat would cost the link and teach less.

**A7 — a separate Practice Test.** With the shared model the unit review is the practice and the
Reference Sheet is the reference. A parallel form of the test is a third thing, and it earns its
place in a course where the support is being withdrawn on a schedule. It is also the one document
whose point values must track the assessment's exactly — its own first line promises "same twelve
questions, same order, same point values, only the numbers are different", and a parallel form
that rehearses a different denominator is not one.

**A7 — longer worksheets, and more of one goes home.** *This entry replaces "A7 — more worksheet
time," removed 30 August; its "45–50 with 3–8" was corrected on 1 September, when the decks were
first measured rather than estimated.* A7 as built runs **40–48 minutes of instruction and 5–13 of
worksheet**, lesson by lesson, and the split is the remainder rule in §9 rather than a target: the
old 38–42 / 11–15 no longer holds because A7 adopted the rebuilt deck shape whole and Croix chose
to protect instruction rather than the in-class start. A7 worksheets are **not** getting shorter,
so the smaller in-class start means **more unfinished work leaves the room.** That is the cost, it
was chosen deliberately, and it is recorded here rather than discovered in November. The tightest
lesson is **1.08 at five minutes**, which is where that cost is largest — it carries four worked
examples because the Talia and Jen item was restored to it, and the in-class start pays for them.

*Removed 2 September: "A7 — no calculator line anywhere."* No longer a course difference — Croix
ruled the same for on-level the same day. §1 rule 8 and §13b ruling 2 state it once for both
courses.

*Removed 31 August: "A7 — longer decks."* It was never a course difference and it is now not even
a difference: `M7 4.02` and `A7 2.05` are both **26 slides**, because both run the same
architecture — one idea per notes slide, one slide per example step, one whiteboard question per
slide with its own reveal. A deck is measured in teaching blocks; both carry nine.

---

## 15. Traps that cost an hour each

1. **A `PageBreak` after content that already fills the page makes a blank page.** Prefer
   `pageBreakBefore: true` on the next paragraph, gated on `!KEY`.
2. **Table rows split across pages.** `cantSplit: true` on every `TableRow`. Always.
3. **A heading orphaned from its content.** `keepNext: true` does not bind a paragraph to a
   following *table*. Wrap heading + rule + first block in one single-cell `cantSplit` table.
4. **A bubble list split across a page** lets a student answer without seeing every choice. Wrap
   the stem and all options together.
5. **An image wider than its table cell is drawn under the neighboring table**, silently. It does
   not overflow or scale — it disappears. Check `height × aspect` against the cell width.
6. **`]);` instead of `]});`** closing `new Table({ ... rows: [...] })`. Symptom:
   `SyntaxError: Unexpected token ')'`.
7. **A missing image key** throws `Cannot read properties of undefined (reading 'w')`. Add it to
   `bars.py` and re-run.
8. **A patch script that asserts mid-way** leaves the file unwritten while the next command still
   reports success. Warn and continue instead of asserting.
9. **Conditional formatting that sets a font can clear the fill** underneath it. Scope the rule to
   the columns that need it.
10. **A glyph that renders correctly in the .docx can still be wrong in the PDF**, because the
    substitution happens at conversion. Always check the PDF, never the .docx.
11. **Two answer choices that are the same number** — `A. 5` and `C. √25` — is a defect that only
    becomes visible when you look at one question at a time. Another reason whiteboard sequences
    show one question per slide.
12. **Never guess where a dimension label goes.** A hand-picked offset that clears the arrowhead
    on a tall figure runs into it on a short one, because the text's width depends on the string,
    the point size, the figure size and whether it is bold. Draw the text, ask matplotlib for its
    extent through `ax.transData.inverted()`, and shift it until it clears. This cost four
    re-renders across three generators before it was written down.
13. **`ax.transData` is wrong until the axis limits are final.** A figure that measures its own
    labels must call `set_xlim` and `set_ylim` *before* it draws any dimension, not after. The
    measurement silently uses the autoscaled transform otherwise, and the labels land in the wrong
    place while looking as though the measuring code ran.
14. **`Object.assign` copies an explicit `undefined` over a real value.** Passing
    `{color: cond ? GRAY : undefined}` as the last argument strips the color a run set for
    itself. Build the object conditionally instead: `const ex={}; if(cond) ex.color=GRAY;`.
    Symptom: a red answer renders black and nothing in the source looks wrong.
15. **A .docx or .pptx whose XML does not parse still opens, and still ships.** Four slides
    of a finished, packaged, zipped lesson carried an empty grey panel where a bold line of
    text should have been. The text was in the file; its run had lost `</a:rPr>`, so `<a:t>`
    sat inside an unclosed `<a:solidFill>` and the renderer dropped the whole paragraph.
    None of the other checks could see it — a regex is happy with broken nesting, an image
    check never reads text, and a prose check cannot object to a paragraph that extraction
    silently dropped. `xmlcheck.py` hands every part to a real parser and runs first.
16. **Never place a slide element at a fixed y underneath an outline.** An outline's height
    depends on how its text wraps, which depends on the text. Anchor to `endOf()`, and clamp the
    result so the element cannot run past the footer rule:
    `Math.min(Math.max(endOf(), floor), ceiling)`.

17. **A staged figure must not carry the reveal's caption on the question slide.** `w4_q3` was
    built with "box 13 × 8, take away 4 × 3" written under it, and that caption was in the mono
    file as well as the color one — so whiteboard question 3 printed its own answer on the slide
    that asked it. Any text a builder adds for the reveal must be inside `if CO:`, and the mono
    and color files must be looked at side by side, not one after the other.

18. **A figure where two unknowns are the same number cannot tell a student they are wrong.**
    The first draft of Lesson 4's L-shape was 14 across the bottom and 11 across the top, 7 down
    one side and 4 down the other, so both missing lengths came out at 3 m. A student who
    subtracted the wrong pair got the right answer and no feedback. Choose dimensions so every
    quantity a student has to derive is distinct from every other one.

19. **A label wider than the region it names has no correct position.** "42 m²" does not fit
    inside a triangle 14 wide and 6 high at any height or any readable font size; four attempts
    at moving it were four attempts at the wrong problem. When a label will not fit, put a letter
    in the region and the quantity somewhere else — in the slide text, or a caption — rather than
    shrinking the type until it technically clears the edge.

20. **A font's cmap can report a glyph as present while matplotlib still draws it
    wrongly.** DejaVu Serif's cmap contains U+03C0, so a coverage check passes — and a
    literal `π` in a plain matplotlib string is still drawn from `font.family` and comes
    out as a squared-off capital Π, because `mathtext.fontset` governs only `$…$`. The
    fix is `$\pi$`. The lesson is wider than π: **coverage is not rendering, and the only
    way to know a character looks right is to draw it and look at it.**
    `figglyph.py` now enforces this over every `geo*.py`, and it is the eighth check in
    `checkall.py` because text drawn into a figure was the one surface none of the other
    seven could see — glyphaudit reads runs inside shipped documents, and an image's
    label is not a run.

21. **A "did it fit?" guard that reads the bounding box gives a false negative when the
    overflow lands in a gap.** `bars.py` and `sgbars.py` size a canvas by trial: render
    at 4 inches, widen 1.7× if the alpha bbox touches an edge, four tries. When an
    over-wide expression is clipped between glyphs, the first surviving glyph starts a
    few pixels inside the canvas, the bbox touches neither edge, and the loop concludes
    it fitted — then writes the middle of the expression out as the whole thing.
    `5 - (-9)  and  (-9) - 5` shipped as `(-9)  and  (-9)`; `l6_ex1d` shipped in the
    3.06 slides reading `× 11/14 × 7/9 = 1836`, an equals sign followed by a number
    that is not the answer to anything. **Measure, do not infer:** `t.get_window_extent()`
    after `fig.canvas.draw()` gives the width the text actually needs, and the canvas is
    sized from that. `barwidth.py` re-measures every declared expression against its
    stored image and is the ninth check in `checkall.py`.

    Note what could not see this. `imagedrift` confirms the embedded bytes match the
    library — they did; the library copy was truncated too. `glyphaudit` reads document
    runs, and this text lives inside a picture. `figglyph` reads figure source, and the
    source was correct LaTeX. **When the generator is wrong, every check that compares
    an output against that generator's own output agrees with it.**

22. **A build script cloned with `sed` will silently keep the previous lesson's body.**
    `build0302.sh` was made from `build0301.sh` with `s/0301/0302/g`. Every filename
    changed — except `cat _head.js _b301.js`, because `_b301.js` contains `b301`, not
    `0301`. So 3.02 and 3.03 were both being assembled from **lesson 1's body**, and
    nothing failed: the deck body names its own output file, so it wrote `M7 3.01
    Slides.pptx`, and the install step then copied the correct `M7 3.02 Slides.pptx`
    that an earlier manual build had left on disk. Right output, wrong reason, and no
    error anywhere.
    Every build script now asserts the link before it builds:
    `grep -q 'fileName:"M7 3.02  Slides.pptx"' _b302.js || exit 1`.
    **A generated script needs a check that its inputs and its outputs still refer to the
    same thing** — cloning by substitution changes the names you thought of, not the
    names you forgot.

23. **A rule with no check quietly stops being followed.** House rule 3 — no benchmark
    codes on anything a student sees — is as old as this spec and had no check for it.
    The Unit 3 assessment shipped with **19 benchmark codes on the student paper** and
    the Unit 4 assessment with **31**, because one `rail()` helper printed them on both
    its student build and its key build. Unit 2's assessment never did, which is the
    only reason it was recognizable as a regression rather than a decision.
    `docscan.py` now carries rule 3 as its fifth ruling.
    Two scope decisions came with it, and both are judgements rather than deductions:
    an **answer key is a teacher document** and may carry codes (keys are otherwise
    classed as student surfaces on purpose, because a key reproduces the student page);
    and a **deck's title slide** carries the benchmark under the rule by standing
    convention in every deck in the corpus, so the ruling exempts it. If either reading
    is wrong, the fix is one line in `docscan.py` — but they should be Croix's calls.
    **A new ruling must be tested in both directions**: this one was verified to stay
    quiet on the title-slide convention AND to still fire on a benchmark code injected
    into a worksheet body. A ruling only ever verified to pass is not a check.

24. **A plan table that was typed to add up will add up.** Every teacher's edition
    prints a segment-by-segment plan totalling 53 minutes, and every deck's speaker
    notes open with that slide's own allocation. Those are two independent records of
    the same thing, and they drifted apart on **four of seventeen decks** — 4.04, 4.05,
    4.06 and 3.07 — always by a minute or two moved from one slide to another *after*
    the table was written. Every table still read 53, because each had been typed to.
    Checking the table against itself proves nothing; `plancheck.py` sums the DECK and
    the TABLE separately and requires both to be 53. It is the tenth check.
    The general shape: **two records of one fact are only worth having if something
    compares them.** Until then the tidier one is believed, and it is the one nobody
    teaches from.


25. **A check whose scope depends on a filename must accept every filename the corpus
    uses.** `docscan.py` decides whether a document is a student surface or a teacher
    surface by looking at its name, and it tested for the literal string
    `"Teacher Edition"` — the *installed package* name. The working directory holds the
    same documents under their *build* names (`7.02.09_..._TEACHER_EDITION.docx`), and
    against those the test failed on every one: every teacher's edition in Unit 2 was
    classified as a student document, and its own compliance notes — "No partner work.",
    "Working toward MA.8.DP.2.2" — were reported as violations of the rules they were
    recording. **59 findings, not one of them real.** The same silent miss applied to
    `is_key`, which tested `"Key"` and never matched `..._WORKSHEET_KEY.docx`.
    Both tests now normalize the basename (underscores to spaces, lowercased) before
    matching. Verified in both directions, per trap 23: the loose corpus went from 59
    findings to clean, the installed corpus stayed clean and unchanged, and a benchmark
    code plus the word "homework" injected into a worksheet body still fires both rules.

    The check was never wrong about the documents. It was wrong about **which document
    it was holding** — and a check that misidentifies its input produces findings that
    look exactly like real ones, which is the fastest way to teach someone to skim past
    the output.

26. **A rule with two halves gets followed on the half that is checked.** Rule 2 forbids
    answer boxes *and* answer lines. Rule 3's check (trap 23) was written for benchmark
    codes and nothing was ever written for rule 2 — so when the corpus was finally read
    for it, **39 of 74 student documents carried an underscore rule**, and a hand count
    found true receptacles on five Unit 4 worksheets, both unit assessments, both unit
    reviews, a handout and a Unit 3 worksheet. Thirty-one of them were written during
    this rebuild, by me, against a rule I was working from. Plus five answer boxes on the
    7.02.02 worksheet: a shaded `Sample Space` label over a tall empty cell, five times.

    Three separate lessons came out of fixing it.

    **(a) The spec already contained the test; nobody had run it.** "Could you delete the
    blank and still have the same question? If yes it is decoration — cut it. If no it is
    the response format — keep it." That is mechanical enough to check, and the four
    allowances it lists each leave a signature in the line: a cloze blank has the sentence
    continuing past it, a formula being completed ends in `=`, an ordered list of slots has
    rules separated by commas, multiple choice has bubbles and no rules. `docscan.py`'s
    sixth ruling is that test, written out. Eighteen surviving cases were then judged one
    at a time and acknowledged with reasons, because the line between a receptacle and a
    response format is a judgement and belongs in writing, not in a regex.

    **(b) Removing the rule is only half the fix — the rule WAS the writing line.** The
    first pass deleted the label and the rule and left the spacing alone, and questions 6
    to 9 of the 4.05 worksheet ended up half an inch apart, because the space above the
    rule had been room to work in and the rule itself was where the answer went. Removing
    a receptacle means giving back the line it occupied, at the spec's size — 0.6" for a
    one-step, 1.3" to explain — and adding the instruction line that now carries what the
    label used to say. **A prohibition with no replacement is a regression.**

    **(c) LibreOffice drops a paragraph's space-before when a TABLE immediately precedes
    it** — and in these worksheets the question itself is a borderless table, so the
    spacer that replaced each rule contributed nothing but its own line height. Measured
    rather than guessed: paragraph-then-spacer keeps the space (107pt for 1300 twips),
    table-then-spacer loses it (31pt), table-then-empty-paragraph-then-spacer keeps it
    (119pt). `W.workspace()` emits that empty anchor paragraph, and the anchor is
    load-bearing. Two other measuring lessons came with it: an empty paragraph still
    costs its own line whatever its `after` is, and a cell whose last child is a table
    gets an implicit empty paragraph anyway — so trimming `after` on a trailing pad saves
    nothing at all.

    `boxcheck.py` is the eleventh check and covers the half of rule 2 that has no text in
    it: a one-column table with a shaded short label over rows that are all empty. Run
    across 101 student documents it fired on the five known boxes and nothing else.

27. **Nothing was reading the printed page.** Eleven checks read documents' sources — XML,
    runs, embedded images, indexes, generators, speaker notes, prose. None of them looked
    at what comes out of the printer. A page can parse cleanly, break no ruling, carry no
    drifted figure, and still be **blank**.

    Two were. Adding the instruction line to the 2.07 worksheet and the 2.06 answer key
    pushed their content to fill a page exactly, and a **standalone `PageBreak` paragraph**
    — which costs a paragraph of its own — then landed alone at the top of the next page.
    Both shipped a blank sheet in the middle of a document and both passed everything.

    Two lessons, and the second is the general one.

    **(a) A page break should be an attribute of the content that moves, not an object of
    its own.** `pageBreakBefore: true` on the following paragraph moves the same content
    without adding anything to move. A standalone `new Paragraph({children:[new
    PageBreak()]})` is a paragraph, and when the page above it is exactly full it becomes
    the only thing on the next one. Fifteen builders still used the standalone form when
    this was written; all of them have since been converted or retired, and no builder in
    the tree uses it now.

    **(b) Every check here compares a document to a description of itself.** Glyph coverage,
    figure hashes, index entries, spec assertions, plan totals — all of them ask whether the
    document matches what it was supposed to be. None asked the simpler question: is there
    anything on the page? `pagecheck.py` is the twelfth check and it asks only that, of all
    2,206 printed pages in the corpus. It counts a page blank when it has no text AND no
    image, because a record sheet's grid page is a picture with nothing to extract and is
    not a defect.

    Verified in both directions per trap 23: it reports the corpus clean, and run against
    the 2.06 key rebuilt with its standalone break restored it names the page and exits 1.

28. **A dead builder that writes a live filename is invisible to every check that reads
    output.** The nine pre-rebuild teacher's editions — `te.js`, `te1.js`, `te3.js` through
    `te9.js` — sat in the working directory beside the nine that replaced them, writing to
    exactly the same nine filenames. No build script had referenced them since the rebuild
    began, so they never ran, and all twelve checks stayed clean for weeks. But `node te5.js`
    was one keystroke from replacing a shipped 2.05 teacher's edition with thirteen-slide
    content, and nothing in the suite would have objected: the document it produces parses,
    breaks no ruling, drifts no figure, prints no blank page and is internally consistent.
    It is simply the wrong document, and the only evidence of that lives in which script the
    build runs.

    Three lessons.

    **(a) Twelve checks read output; none read source.** Every check written before this one
    asks whether a shipped document is correct. `buildref.py` is the thirteenth and asks
    whether the file that produced it is the file that will produce it next time. That is a
    different question, and a corpus can be perfect on the first while being one command away
    from disaster on the second.

    **(b) Superseding a file is not the same as retiring it.** Writing `te0205b.js` did not
    make `te5.js` harmless; it made it dangerous, because now two files claimed one output
    and only one of them was right. `superseded/` already existed in this tree and twenty
    files had been moved there correctly — the convention was sound and had simply stopped
    being applied. Retiring is now the documented answer to a `SHADOW` finding.

    **(c) The same check found four shipped documents with no build script at all.** The
    Unit 2 assessment, review, study guide and vocabulary reference were being rebuilt by
    hand from memory — the identical gap that `build0407.sh` and `build_u3assess.sh` were
    written to close, still open in a third place. `build_u2assess.sh` closes it. A check
    written for one failure found a second, unrelated one on its first run, which is the
    third time that has happened in this tree.

    Verified in both directions per trap 23: it reports the tree clean, and run with
    `te5.js` restored to the working directory it names the shadow and exits 1.

29. **A figure is not shown at the size it was drawn, so a point size in a figure script is
    not a point size on the page.** matplotlib draws labels in points onto a canvas measured
    in inches; the builder then places that canvas at whatever width the slide has room for.
    What the student sees is

        on-page points  =  the point size in the geo script  ×  (placed width ÷ generated width)

    and that second factor was never controlled. Measured across the corpus it ran from 1.04
    to 2.26, so the same `lab(..., fs=13)` call printed at 14pt on deck 4.01 and 29pt on deck
    4.02 — too small to read from the back of the room at one end, louder than the sentence
    beside it at the other. Twenty of thirty-five placements were outside any band worth
    stating. Every figure was individually fine and no two agreed.

    Three lessons.

    **(a) The type is the invariant, not the picture.** The fix is not to hand-tune thirty
    point sizes. `figscale.json` carries a per-figure factor that `save()` applies to the
    FIGURE — fonts and line widths stay in points, so scaling the canvas is precisely what
    changes their size relative to the drawing. Placement width does not move, so nothing
    reflows and no page count changes. Sizing in ems rather than inches, which is what the
    backlog had been calling this for weeks without saying why it mattered.

    **(b) A normalization factor must be cumulative or it oscillates.** A figure is measured
    AFTER its factor was applied, so the new factor is the old one times how far it still is
    from target. One pass took the spread from 1.04–2.26 to 1.28–1.63.

    **(c) Mentioning an index is not writing it.** `indexdrift` decided `figscale.py` was a
    new, undeclared generator of all 276 geometry figures because it reads `geo/index.json`
    to do the measuring. Its writer test now looks for an actual write of that path, which
    also revealed that `barwidth.py` had been mis-recorded as a writer of `bars/index.json`
    since the day it was written. A check that cannot tell a reader from a writer raises a
    false alarm every time something new looks at the data.

    Verified in both directions per trap 23: run against the un-normalized corpus it named
    twenty placements and exited 1; run now it reports the corpus clean.

30. **Fifteen checks and not one of them ever evaluated a sum.** Math errors shipped. Every
    check written before `mathcheck.py` asked whether a document was the document it was
    supposed to be — whether it parsed, whether its figures matched, whether its pages were
    blank, whether it broke a ruling, whether its plan totalled 53 minutes. None asked whether
    what it says is true. A key could have read 4/6 = 0.75 and the corpus would have been
    declared clean fifteen times over.

    **Correctness is rule zero, and it outranks everything else in this file.** A style slip
    costs a reputation slowly. A wrong answer on a key costs it in one lesson, in front of
    thirty students, and it is the teacher who wears it. `mathcheck` runs FIRST, ahead of
    xmlcheck, and a single finding fails the build.

    Four lessons, and the last is the important one.

    **(a) A filter that silences a check is worse than a missing check.** The first version
    skipped any line matching `\d{1,2}\.\d{2}` so that lesson numbers like 2.08 would be
    ignored — which silently excluded every line containing a two-decimal value: every price,
    every measurement, every rounded answer in the corpus. The one real arithmetic error in
    256 documents sat on a line that was skipped whole. Silence looked exactly like a pass.

    **(b) Precision belongs to the number, not to its neighbors.** Tolerance was read from
    the most decimal places appearing anywhere on the line, so `5.2 × 3.14 = 16.3 cm` — a
    correct answer rounded to the nearest tenth — was reported as wrong because 3.14 prints
    two places. A result is exactly as precise as it is written.

    **(c) A parser that can drop a digit can hide an error as easily as invent one.** Writing
    this check produced 760 findings on its first run, none of them real, and every round of
    triage found a bug in the checker rather than the corpus: run boundaries inserting a space
    inside `4/9`; table cells not broken, so three unrelated correct answers became one wrong
    equation; a lazy regex eating the leading digit of `10 + 5 = 15`; the fraction bar and the
    division sign collapsed into one character, so `6 ÷ 2/3` evaluated as `(6/2)/3`;
    superscripts flattened, so `7²` became `72`; an em-dash read as a minus sign; and an old
    copy of `arithmetic()` shadowing the new one entirely, so the fix was not running at all.
    Each of those could equally have masked a true error.

    **(d) So the check self-tests on every invocation, and refuses to speak if it fails.**
    Forty-seven cases — sixteen planted errors and thirty-one correct statements, every one a
    real line from this corpus, including all fifteen the checker got wrong at first. If the
    self-test fails, `mathcheck` reports nothing and exits non-zero, because a check nobody
    has proved can fail is a check nobody should believe. This is trap 23 made permanent:
    verification in both directions, run every time rather than once.

    **What it does not do.** It verifies arithmetic that is written down. It cannot catch an
    answer that adds up correctly and is still the wrong answer to the question. That gap is
    covered by independent re-derivation — solving every question from the question text
    alone, without reading the key first — and that pass is what found `9⁵⁄₅ = 9.6` on a
    student worksheet, where the numerator should have been a 3. Both layers are needed:
    the check runs on every build, the re-derivation runs before a release.

31. **Arithmetic that is wrong on purpose is recorded, not excluded.** This corpus teaches
    error analysis, so wrong sums appear deliberately — Ashlyn's `10.90 + 1.375 = 11.275` is
    a whiteboard question whose whole point is that students find the slip. `mathack.json`
    carries these, keyed on the exact statement text and never on a path, because a path
    exclusion hides the next real one. Every entry must state the correct value, so the file
    is a record of what is true rather than a way of not being told.

32. **A side-by-side layout does not need a table inside a table — it needs more columns.**
    *Accelerated course, 5 September.* Google Docs flattens or misrenders a nested table, and
    the Practice Test nested two: a borderless 2×2 grid holding four lettered parts, each cell
    carrying its own two-cell answer box, and a borderless 1×3 grid doing the same for questions
    4 to 6. The instinct is to delete the outer wrapper and stack everything full width, which
    changes the look of a test question. The actual fix is to keep one table and give it the
    columns both jobs need: `label · answer · gutter · label · answer`. The stem and the writing
    room span two columns with `gridSpan`, which Docs handles; only the box cells carry borders.
    The layout is identical, nothing nests, and the three Solution boxes come out level with one
    another, which they never were when each was the last thing inside a cell of its own height.

    Three things this taught, each found only by rendering and looking:

    **(a) A borderless gutter column is not decoration.** Without it the two answer boxes butt
    together and read as one four-cell strip rather than two boxes.

    **(b) Rows are where a table breaks, so `keepNext` has to run through them.** Splitting one
    cell into three rows — stem, writing room, box — hands the page-breaker three new places to
    break, and the first render put a part's answer box on the page after the question it
    belongs to. `keepNext` on every paragraph in the rows above the box closes it. This is the
    same instrument `keepwith.py` applies corpus-wide, applied by hand where the structure needs
    it.

    **(c) A table that splits across a page gets a rule drawn across the continuation, whatever
    its borders say.** LibreOffice drew a hairline above "c." at the top of page 2 — 70pt to
    310.5pt, exactly the width of the left stem cell — on a table whose every border is `none`.
    No border setting removes it, because it is not a border. **One table per pair** removes it
    instead: two tables cannot split between them, so the break falls in the paragraph between,
    where a break belongs. Consecutive tables MERGE in Word and LibreOffice, so that separating
    paragraph is load-bearing rather than spacing — the same lesson the ruled answer lines taught
    in the study guide, arriving from the other direction.

    And the cost was real and had to be paid back: the repair pushed the answer key from four
    pages to five, stranding the marking notes alone on the last one. Trimming the doubled cell
    margins the flattening had introduced — a stem cell's bottom margin and a box cell's top
    margin now meet where one cell's margin used to sit — brought it back to four. **A layout
    repair that adds a page has not finished.**

33. **`w:keepNext` does not move a table, and this corpus's question stems are tables.**
    *Accelerated course, 5 September.* Every answer box separated from its own question on the
    Unit 1 assessment traced back to this. Word and LibreOffice both take "keep this table with
    what follows" from `keepNext` on the paragraphs in the table's last row — that is the
    documented mechanism, it works in a two-paragraph test file, and against the real assessment
    it changes **nothing**: rendered with the property and rendered without it, the stem stays at
    the foot of page 5 and its Solution box and number line go to page 6 by themselves, on a page
    a student turns to and finds an unlabelled box above an unlabelled axis.

    **Re-measured 6 September, this time with a denominator**, because "it changes nothing" was
    an observation on one document and the on-level fork was about to act on it. Twelve Unit 1
    worksheets and answer keys carrying **650 `w:keepNext` elements between them**, each rendered
    three ways — as shipped, with every `keepNext` stripped, and with `keepNext` added to every
    table's own `tblPr`:

    - stripping every `keepNext` changed the rendered text of **4 of the 12**, so the property is
      genuinely load-bearing on paragraphs and `keepwith` is doing real work;
    - adding it to every table changed the rendered text of **0 of the 12**.

    That is the shape of the finding: not "keepNext does nothing", which would be false and would
    have led someone to delete a working repair, but "keepNext does nothing **to a table**".

    Three things came out of chasing it, and the third is the one that matters:

    **(a) The paragraph nearest the box is not the stem.** It is the empty paragraph that makes
    the writing room. Binding *that* to the box binds nothing anyone cares about. `keepwith` now
    walks back through the blank paragraphs to the thing that owns them, bounded at eight so a
    runaway walk cannot bind a whole page into one unbreakable block.

    **(b) The same property on a DATA table is read as a row instruction, and splits it.** The
    first repair wrote `keepNext` on every table's last row and question 2's flavour table
    promptly sent its last two rows to the next page, away from their own headings. §13c item 2
    again, four days after the last time. The table binding was retired the day it was written,
    with its reason recorded rather than the code silently deleted.

    **(c) So `pagebind.py` measures instead.** It renders the document, reads which page every
    answer box and every number line actually landed on — words matched by rarest-word ordinal
    against `pdftotext`, figures by page from `pdfimages -list`, both checked by count before
    they are trusted — and where a box came out on a different page from its question it writes
    a page break in front of the question and renders again. **One break per pass**, because
    every break changes the answer for every break after it: applying them all at once moved
    question 12 on the strength of a layout that question 11's break had already replaced, and
    left a page two-thirds empty. And the break goes in a paragraph BEFORE the table, never in
    the first paragraph inside it — `pageBreakBefore` in a cell breaks the TABLE at that row and
    the renderer draws the continuation's top edge, which is trap 32(c) arriving from the other
    direction.

    **What it will not do, on purpose.** A question that runs over a page break with each part
    still beside its own answer space is worse reading and is NOT repaired. Making it whole means
    starting it on a fresh page, and on the Unit 1 assessment that turned seven pages into eight
    and left page one holding question 1 and nothing else. Whether a class is better served by an
    extra sheet or by turning back a page mid-test is a teacher's decision about their own
    classroom. Those go to `pagebind-report.txt` — eighty of them across the corpus — and Croix
    can say. A build that prints eighty "for a person to decide" lines every time teaches the
    person to stop reading the build log.

34. **A document that READS another document has a build order, and build order is a habit.**
    *Accelerated course, 5 September.* A teacher's edition does not own its slide notes:
    `telib.deckPlan()` opens the `.pptx` and prints what is in it, which is the right design —
    one source, no second copy to drift. Four slide notes were repaired that day, the decks were
    rebuilt, and the teacher's editions were rebuilt in the same command **three lines earlier**.
    Every one of them read the deck as it stood before the repair and printed the sentence the
    repair had removed.

    That is worse than a stale file. The 1.09 teacher's edition ended up printing, on page 3, the
    false diagnosis the repair existed to delete — *"if BOTH came out true… the answer is too
    wide, and the symbol is probably reversed"* — one sheet before its own misconceptions page
    stated the corrected version. A single document contradicting itself is what a teacher reads
    aloud in front of a class.

    `tedeck.py` asks the one question: is any teacher's edition older than the deck beside it? It
    is an mtime heuristic exactly like `figstale`, wrong in the cheap direction — rebuilding costs
    a second — and it runs inside `finish()` as a refusal, not only in `checkall.py`, because a
    check you have to remember to run is the same habit that caused the defect. It found five,
    one more than the reader did.

    **The general rule: wherever one shipped document reads another, the reader is rebuilt after
    the read, and something other than memory enforces it.**

35. **When you cannot render what the reader sees, one round trip beats a correct measurement.**
    *Accelerated course, 6 September.* Croix opened the glyph probe in Google Docs: twelve of the
    thirteen fallback characters came out right, and the cube-root radical came out "slightly too
    large".

    The diagnosis was measured, not argued, and as far as it went it was true. FreeSerif draws
    U+221B from 0.781 em above the baseline down to −0.165 em below it, so in the printed PDF the
    radical HANGS BELOW the line and barely rises above it — on the Reference Sheet a word
    containing it measures 13.22pt against 12.18pt for its neighbours, and 0.95pt of that is
    underhang. Docs has no FreeSerif and substitutes a DejaVu-class face whose radical runs from
    0.938 em down to only −0.020: the same total height, hung the other way up, standing over the
    line instead of dropping below it. No font is both native to Docs and in possession of the
    glyph, so the only available lever is the point size of that one run.

    A tenth was taken off. It was checked in print — rendered at 200 dpi before and after and
    looked at, because arithmetic cannot tell you whether a radical still reads as a radical — and
    it cost nothing there. Everything about that was sound.

    **And it was the wrong fix.** Shown the same four sentences at 100%, 90% and 80% on one page,
    Croix picked **100%**: the original. Seen beside two smaller versions, the thing he had called
    too large was the thing that reads correctly. The change was unwound the same hour.

    What this is really about:

    **(a) A correct measurement can answer a question nobody asked.** Every step of the diagnosis
    held up. What none of it could establish is the one quantity that mattered — how much — because
    the substitute cannot be rendered on this machine at all. A number you cannot measure is not
    improved by deriving it from numbers you can.

    **(b) The probe cost one round trip and saved a change to 170 runs across 61 documents**, plus
    the later reversal of that change, plus whatever the reversal would have broken. `radprobe.py`
    is nine lines of content and one page of output. That is the price of asking, and it is almost
    always lower than the price of being wrong quietly.

    **(c) The obvious fix was rightly not taken either.** The offer on the table was to draw the
    radical as a picture, the way every other radical in this corpus is drawn, which no font can
    break. All 170 of these sit in the MIDDLE OF SENTENCES, and a picture mid-sentence brings its
    own line-spacing trouble — a trade worth making for a defect and not for a blemish. Knowing
    which of the two is in front of you is the whole judgement, and in this case the answer was
    neither: there was nothing wrong with the file.

    **(d) The retired entry stays in the source with its reason,** the same as `keepwith`'s
    `_last_row_bound`. A deleted mistake teaches nobody; a recorded one stops the next person
    reaching for the same lever.

36. **Two tables that touch are one table, and a correct diagnosis is not the same as the
    cause.** *Accelerated course, 6 September — the worst defect of the Google Docs work, found by
    a teacher on a graded test, and MISDIAGNOSED once before it was found.*

    Croix opened the Unit 1 assessment in Google Docs. Question 1's stem came out **one and two
    characters per line**, running down a column about thirty pixels wide. Question 2's stem,
    built by the same helper from the same widths, was perfect.

    **The first answer was wrong.** Every table declared no `w:tblLayout`, which means AUTO, which
    means the renderer may recompute the columns; LibreOffice honoured the stated widths and Docs
    did not. That was all true, it was worth fixing — `tablefix.py` pins all 953 — and it did not
    fix this. He opened it again and found it identical. A measurement that explains a mechanism
    is not evidence that the mechanism is the one operating.

    **The cause is older and this file already knew it.** Trap 32 records that consecutive tables
    MERGE, which is why a spacer paragraph sits between the study guide's ruled answer lines. A
    question stem is a two-cell table and it is followed IMMEDIATELY by the question's content
    table, nothing in between. Two tables that touch are one table, and one table has one grid.
    Question 1's neighbour begins with the narrow "a. b. c." label column — 760 twips — so the
    merged grid begins narrow and the stem lands in it; less the stem's own 480 twips of hanging
    indent, that is about 3% of the page to write in. Question 2's neighbour begins at 5400
    twips, so its stem got a wide column and survived. **Same construction, same bug, different
    neighbour** — which is exactly why it looked like the two questions differed when they are
    byte-identical.

    There is no "do not merge" property in OOXML. A paragraph between them is the only mechanism.
    `tablesplit.py` inserts a 1pt one; 76 pairs across 18 documents.

    Four things worth keeping:

    **(a) The merge was damaging the PRINT too, and nobody had noticed.** Separating the tables
    moved column positions on the PDFs and made four documents SHORTER — the completed Unit 1
    study guide went from eight pages to five, because its worked-example boxes had been squeezed
    into a column narrower than they were built for. Every one is full width now. A defect can sit
    in plain sight for weeks while every check passes and the pages still look plausible.

    **(b) That PDF change is what made the second diagnosis believable.** The first fix was a
    property I hoped Docs would read differently; the second removes a merge that I could watch
    happening in the renderer I have. **When you cannot test in the reader's program, prefer the
    repair whose effect you can observe over the one you can only argue for.**

    **(c) `atom()`'s refusal to wrap a group containing a table silently disabled a second
    mechanism.** The study guide's section banner was held back and prepended into the first
    skill's unbreakable group so the two could not part — but the banner was a TABLE, so the
    wrapper never applied, and the comment describing the mechanism had been wrong since the day
    it was written. The banner is now a paragraph with a right tab stop and it binds. **A guard
    added for one reason can turn off a mechanism added for another, and neither comment will
    mention the other.**

    **(d) The canary is the only step that tests what the pass is for.** Four files and two of
    Croix's mornings found what 98 documents of static checking could not, twice. `gdoccheck` now
    counts unstated layouts and touching pairs, so both can be seen; neither could have been
    seen before he looked.

---
## 16. How lessons teach — the instructional design rules

**Ruled by Croix, 3 September 2026, for both courses.** §9 says what goes in a lesson. This says
how the lesson teaches, and it is a ruling rather than a preference:

> The build method these rules describe is explicit instruction in the Craig Barton /
> cognitive-load tradition — worked examples, immediate checks, retrieval, deliberate practice
> design. This is not a style preference; it is the approach with the strongest evidence for the
> students in these rooms, and the on-level sections are the exact population that evidence is
> strongest for.

Much of the corpus already works this way. What this section changes is that it now happens **on
purpose rather than by instinct**, which is the difference between a habit and a rule: a habit
survives until the week somebody is in a hurry.

### The build order, and what Math Nation is now

**Benchmark, CPALMS clarifications and FAST item specifications first. Math Nation second.** A
lesson starts from what the benchmark requires and how FAST asks it. The Math Nation original is
then read *against* the built lesson, using the standing UNIT AUDIT checks, for three things: scope
it covers that we missed, prerequisite traps, and items worth stealing.

**"Adapting the lesson" is retired as a description of this work.** It describes a lesson that
started from the book and was changed, and that is no longer what happens. The book is an audit
target and an occasional item mine. It is not a template.

**This reverses the direction the corpus was built in**, and it is the change most likely to be
undone by habit, because a PDF arriving looks like a task. It is not. It is a second opinion, and
it arrives *after* the build, not before it.

One line worth keeping in front of whoever reads this next, because the opposite reading is the
natural one: **Croix keeps sending the source PDFs for exactly this purpose, and their arrival is
not an instruction to follow them.** A file landing in the folder feels like a brief. It is a
comparison set.

### Rule 1 — Every worked example is a pair: the example, then a Your Turn

After each staged worked example, the very next thing is **one near-identical problem the student
does alone, before anything varies**. Same structure, same difficulty, different numbers — close
enough that the example is still usable as a map while it sits in their notes.

- **Deck shape.** The example's reveal slides, then one Your Turn slide with its own reveal. It
  joins the whiteboard rhythm already there. It is not a second example.
- **The teacher's edition names what the Your Turn checks** — "this catches a student who watched
  the halving step without doing it."
- **The whiteboard rounds stay.** They are the *varied* practice. The Your Turn is the un-varied
  step in between, which is the step the current decks skip. 4.09's Mikel pizza example would be
  followed by "a 10-inch pizza, 8 slices, Amara ate 3" before the round asks anything harder.

*Checkable:* every deck section titled **Example N** is followed by a **Your Turn** slide before
the next section begins.

### Rule 2 — Worksheets are built on intelligent variation, and the variation is declared

A practice sequence is **designed, not assembled**. Consecutive questions change one feature at a
time, chosen so that the change teaches: the number gains a decimal, the given switches from
radius to diameter, the orientation rotates, the wording flips from "find the area" to "find the
base". A student working the sequence should be able to feel what each change did. That is the
point of it.

Somewhere the sequence must also **break the pattern on purpose** — Barton's boundary move. After
four questions where the given is a diameter, one where halving would be wrong. The 4.10 Q5/Q6
fence-and-window pair is exactly this and is the house model.

- Every worksheet's teacher's edition carries a **two-line Variation note**: what varies across the
  sequence, and where the pattern deliberately breaks.
- **If that note cannot be written, the worksheet is a pile of questions and goes back.** That is
  the whole force of the rule — the note is not documentation of the design, it is the test of
  whether there was one.
- Additional Practice mirrors the worksheet's variation structure with different numbers, the same
  discipline the practice-test rule already imposes.

### Rule 3 — Every unit review carries an SSDD block

**Same Surface, Different Deep.** Four problems that look identical — same context, same picture,
same numbers where they can be — where the mathematics differs. One circular garden, asked for its
circumference, its area, its radius from the circumference, and the cost of a fraction of it.

**The unit's whole failure mode on FAST is students matching a procedure to a surface.** This block
is where that habit gets broken, and it is where a review earns its keep in a calculator era.

- **Placement:** end of Part A or opening of Part B on every unit review, as its own numbered
  question with lettered parts — which under per-part scoring also prices it correctly.
- **The name goes on the KEY, never on the student paper.** *(On-level worker, 4 September; A7
  matched the same day.)* "SSDD" is teacher jargon, and printed on a student page it tells the
  student the four parts are secretly different — **which is the answer to the only thing the
  block asks.** Any line to the same effect on the paper (*"they are not the same question"*) goes
  the same way. Noticing that the parts differ **is the task**.
- 4.10 ("Circumference or Area?") is the SSDD *lesson*; the review block is its rehearsal.
- **Units without a natural geometric pair still have one.** Probability: the same spinner asked
  for a theoretical probability, an experimental one, its sample space, and whether it is fair.
  Rational numbers: the same account table asked for a balance, a change, an average change, and
  when it crosses zero.
- *Checkable:* the review KEY names the block, the review PAPER carries a stem with four lettered
  parts, and the paper does **not** print the name. *The first version of that check looked for
  the label on the paper, which would have made the label impossible to remove — a check coupled
  to a name stops you fixing the name even when the name is the defect. It now checks for what the
  block **is** rather than what it is called.*

### Rule 4 — Whiteboard rounds diagnose. One misconception per wrong option

Where a whiteboard question is multiple choice, **every distractor is a named error and the
teacher's edition names it**: "(b) is squaring the diameter; (c) is 2πr with the diameter; (d) is
the circumference."

A board full of (b)s changes the next five minutes. A board full of wrong-but-scattered answers
tells you nothing, and a distractor nobody would pick is dead weight taking up a line.

- **At least two questions per whiteboard round** run as diagnostic multiple choice with this
  discipline. The rest stay free response — the reveal-per-question structure already there is
  right.
- The misconception names come from the audits and the B1G-M lists already collected: truncating
  repeating decimals, using *m* where *a* belongs, halving after multiplying by π.
- Each diagnostic distractor **cites its misconception in the teacher's edition**, which is also
  what makes the item checkable: *a distractor without a named error is a finding.*

### Rule 5 — Warm-ups are spaced retrieval, on a schedule, and never new content

The old rule — a warm-up reaches back one lesson — becomes the **floor, not the design**.

A warm-up is **four short questions on a fixed spacing pattern**: yesterday · last week · earlier
this unit or last unit · anything from the year so far. Retrieval from memory: no notes, and no
calculator unless the retrieved skill is itself a calculator skill. Two minutes of silent work, a
quick reveal, and **no reteach longer than one sentence per question** — a warm-up that grows into
a lesson steals the lesson's time.

- The teacher's edition lists, per question, **the lesson it retrieves from**.
- *Checkable:* four questions, four distinct recency bands, sources named.
- The "same and different" warm-ups built this week satisfy the *yesterday* slot and stay. They
  gain the three reach-back questions beside them.
- This **replaces any warm-up inherited from Math Nation that previews the day's content** instead
  of retrieving old content. Previewing is the opposite job.

**The opening-lesson problem, and the default both courses now run.** Lesson 1 of a unit has no
*yesterday* and no *earlier this unit*; the first unit of a course has no *last unit* either. The
rule cannot be met as written for the first few lessons, and quietly writing a three-question
warm-up there would be the rule decaying by exception.

*Raised by the accelerated worker, 4 September, with a default already built into A7 1.01.
Adopted here for both courses, and marked as adopted rather than ruled so Croix can overturn it:*
**an opening lesson fills the empty bands from the prior grade** — grade 7 for A7, grade 6 for M7.
That is still retrieval, it is still on the FAST, and it is the prerequisite check those lessons
want anyway.

One refinement on top of their version, because a default this loose can be filled with anything:
**the prior-grade question must be the prerequisite THIS lesson needs**, and the teacher's edition
names it as that. "Grade 6 content" is a band; "the fraction-to-decimal division 2.04 is about to
run backwards" is a warm-up. Without the refinement the rule says only *reach further back*, which
is the part a hurried builder can satisfy with anything.

> **Check the calendar before you write the bands.** *(5 September 2026, after a review found a
> rebuilt Unit 2 lesson whose warm-up "retrieved" the circumference of a circle and signed
> rational addition — both of them units that come LATER in the year.)* "Last unit" and "earlier
> this year" are **forward references** in the opening units, and a student cannot retrieve what
> has not been taught. In an early unit the bands collapse to: yesterday · last week · earlier
> this unit · **anything from the year so far, which includes the prior grade**. The prior grade
> is what fills an empty band, and it is where the prerequisite lives anyway. **Every warm-up
> whose TE names a source lesson must have that lesson's number checked against the pacing
> guide** — a warm-up that points down the calendar the wrong way is a silent-teacher task a
> student cannot start.

### Rule 6 — The moves already in this file are confirmed as rules, with their names attached

So that nobody improves them away later:

| The move | Its name | Where it already lives |
|---|---|---|
| one idea per slide, with its own reveal | atomisation | §9 |
| the worked example narrated while students only watch, then copied | silent teacher / example first | §9 |
| error-analysis tables where the student names the step that broke | diagnosing, not redoing | §5, and the 1.04 grid |
| no discovery tasks and no partner scaffolds in first teaching | fully guided instruction | §1 rule 4 |
| reasons before procedures — Notes I before Notes II | why before how | as 2.04 now does |

These stay. And anything in rules 1–5 that collides with a deadline **loses to rule 0 exactly as
everything else in this file does: correct first, then this.**

### Rollout, and why it is not a mass rebuild

New builds follow all six rules immediately. Existing units are **not** mass-rebuilt; rules 1–5 are
applied opportunistically, whenever a lesson is already open for another reason. Two exceptions are
done now because they are cheap and high-yield:

1. **The SSDD block** goes into the three M7 unit reviews and both A7 reviews the next time each is
   regenerated. *Done: M7 units 2, 3 and 4 on 3 September; A7 units 1 and 2 on 3 September, both
   at **question 9** — A7 Unit 1 at the opening of Part B, A7 Unit 2 at the end of Part A.* The accelerated course's own copy of this section said "Unit 1 review
   question 41, Unit 2 review question 31"; the shipped reviews carry the block at question 9 in
   both, and their covering note says 9 as well. Corrected here rather than pasted through,
   because a status line naming the wrong question is the same failure as a status line naming a
   rebuild that did not happen, and this file has already been caught by one of those this week.
2. **Warm-ups convert to the four-question spaced pattern** unit by unit, going forward.

**Coverage is recorded per unit, in the changelog, not assumed.** `designrules.json` declares
which of rules 1–5 each unit or lesson claims, and `designcheck.py` enforces every claim and prints the rest as coverage.
`designcheck.py --rules` prints what each rule looks for **and its blind spot**.

*Merged 4 September, ruling 3.* Both courses built this check independently and both made the same
central decision for the same reason — report coverage, fail only where the ruling is in force —
which is worth recording as a convergence rather than a coincidence. On-level contributed the
per-**lesson** claim, which is the grain the rollout actually arrives in; accelerated contributed
the **denominator** (`1 of 27 lessons`, not `1 claim`) and `--rules`. The blind-spot text is the
sentence the file most needs to keep saying: **every one of these is a shape check, and a lesson
can satisfy all five and still teach badly.**

**What each rule looks like on the page**, because a rule whose convention lives only inside a
checker is a rule nobody can build to:

| rule | the marker `designcheck` reads |
|---|---|
| 1 | a slide whose first line is **Your Turn**, immediately after the last slide of each `Example N` run |
| 2 | a paragraph in the teacher's edition beginning **Variation.**, saying what varies and where the pattern deliberately breaks |
| 3 | the unit review **key** names the block — *Same Surface, Different Deep* — and the review itself carries **one numbered question with four lettered parts**. The naming stays on the key: a student told the four parts are secretly different has been handed the answer to the only thing the block asks. |
| 4 | a speaker note that names its **distractors** and accounts for **every** wrong option by letter — (b), (c) and (d) — on at least two questions per deck. Counting a heading would certify the wrong thing: a note that names one of three leaves the other two as the dead weight the rule exists to stop. |
| 5 | four **retrieves** lines in the teacher's edition's warm-up, between them naming all four recency bands |

Rule 6 has no marker and is not faked into one. Its five moves are visible to a reader and not to
a regular expression, and a check that pretended otherwise would measure the word rather than the
move.

That shape is deliberate and it is the only shape that works here. A check that simply demanded
rule 1 of every deck would have reported twenty-seven findings on its first run — every one of them
a lesson built correctly under the rules of the week before — and a check that cries wolf
twenty-seven times is one nobody reads on the day it is right. A check that fails on lessons the
ruling explicitly exempts is a check somebody switches off within a day, **and a switched-off
check is worse than no check, because the next person believes the green.** A check that was quietly scoped to
"new lessons only" would have no denominator at all and would go stale the moment somebody forgot
to widen it. Declaring the claim makes both halves visible at once: what is enforced, and what is
not yet claimed.
