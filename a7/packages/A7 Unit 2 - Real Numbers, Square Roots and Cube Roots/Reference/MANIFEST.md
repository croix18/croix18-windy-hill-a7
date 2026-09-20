# MANIFEST — merge of the two House Style forks

**Merged 5 September 2026.** Output: `MERGED.md`.
Inputs: `MASTER-m7.md` (on-level, 1,599 lines, the declared master and the **base**) and
`FORK-a7.md` (accelerated, 1,136 lines).

This file is for someone deciding whether to trust `MERGED.md`. It lists where every section came
from, everything ported in from the fork by name, every conflict and how it was ruled, everything
dropped and why, and — at the end — the things this merge would not decide and has left for a
person.

Both files were read end to end before any merge was written. The overlap was verified by diffing
the ranges that looked identical rather than assumed; those diffs are recorded below.

---

## 1. Section-by-section provenance

| § | Where the content came from | Notes |
|---|---|---|
| Title block | **new** + master | The new opening declares the single master, the supersession and the dated merge line; the master's own preamble (two Source-of-Truth documents stay separate, Croix 2 September, on-level owns the merge) follows it unchanged. |
| 0. The rule that outranks this file | **both** | Master's two-course version is the base — it is a superset of the fork's single-course version. Fork ports listed in §2 below. The Croix quotation ("math errors are unacceptable…") is **byte-identical in both files**; kept as-is. |
| 1. The short list | **both** | Master's base; rules **3**, **6** and **8** replaced by the fork's fuller statements (see conflicts C4, C5, C6). Rules 1, 2, 4, 5, 7, 9, 10 identical in both. |
| 2. Type and color | **both, identical** | Diffed: identical except "Colouring"/"Coloring" in 2a rule 4. Master's spelling kept. |
| 2a. The variable color code | **both, identical** | As above. |
| 3. Page geometry | **both, identical** | Diff clean. |
| 4. Document anatomy | **both, identical** | Diff clean. |
| 5. Answers and answer space | **both, identical** | Diff clean. |
| 6. Answer keys | **both** | Master's base; the Scoring Sheet requirement replaced by the fork's retirement bullet (conflict C1, ruled). |
| 7. Mathematics conventions | **both, identical** | Diff clean. |
| 8. Figures | **both, identical** | Diff clean. |
| 9. What goes in a lesson | **both** | Master's base; three fork bullets ported (timing-as-remainder, plan-refuses-to-build, TE-reads-the-deck) and one clause added to the Teacher Edition row. Master's ruling-4 Study Guide / Reference Sheet rows kept over the fork's older single-document row. |
| 9b. How lessons teach | **master only** | Kept. Pointer to §16. |
| 10. Sequencing this year | **both, identical** | Diff clean. |
| 11. Naming and packaging | **both, identical** | Diff clean. |
| 12. Before a unit is built | **both, identical** | Diff clean. |
| "A finding is not a decision" | **both, identical** | Diff clean. |
| 13. Before anything ships | **both** | Items 1–6 and both leading blockquotes identical in the two files. Fork's **item 7** (deck geometry) ported whole. |
| "Two drift checks" | **both, identical** | Diff clean. |
| 13b. Rulings — Croix, 2 September | **master only** | Kept, with ruling 5 amended under the three rulings (see C1, C2, C3). |
| 13c. What a check has to be | **master only** | Kept; `figstale.py` added to the "adopted from the accelerated course" list, and a note added under the check table about its own count (open item O2). |
| 14. Where the courses deliberately differ | **both** | Master's base and ordering; all of the fork's accelerated entries ported (see §2). |
| 15. Traps that cost an hour each | **master** | Traps 1–11 are **byte-identical** in both files (diffed). Traps 12–31 are master-only and kept. The fork has no trap the master lacks. |
| 16. How lessons teach | **both** | Master's base — it is already the merged, ruled-for-both-courses version. Fork ports: the SSDD label ruling, the rule-3 checkable note, the question-9 placement detail, two table cross-references, the switched-off-check sentence, "in the changelog". |

---

## 2. Ported in from the fork, by name

**§0**
1. **"The 4 September round, and the two lessons it added"** — ported whole as its own subsection:
   112 documents, twenty-one independent readers, **46 defects**; **"a repair is a new claim"**
   (the A7 1.06 slides, slide 18's *"…and the total came to $273. Write the equation."*, the same
   shape at 1.10 question 6, three of the round's defects introduced by the previous round's
   repairs); and the **study-guide leak class** (the false "numbers are all different" promise,
   A7 1's C3, A7 2's B3/C3/D1, the generator comment that said the opposite of what it produced,
   **`guideleak.py`**, and the `x² = 0` exception named on the front page). A cross-reference to
   §13c was added, because §13c states the repair lesson as a property a check must have.
2. **`figstale.py`** — for every figure directory, is any figure older than the generator that
   draws it. The master mentioned `piglyph` and `guideleak` but not this one. Added in §0 and
   again to §13c's list of accelerated tools not yet built on-level.
3. **`exprcheck.js`** — compares printed values against keyed values and prints how many it could
   not compare.
4. **`mathcheck.ack.json`** — can excuse an unsolved item **only** with the reason and the human
   derivation that replaces it.
5. **`mathcheck` also runs inside `finish()`**, which every packaging script goes through.
6. **`wbseq.js` takes a per-question instruction** — the tool name behind the master's "a question
   must determine its own answer".
7. **`partsum.js`** filename, and "the plan reads the total and never looked at the parts".
8. **"a row without the `from:` field is itself reported"**.
9. **"none was caught by any of the eleven checks then in place."**
10. Two defect-table examples the master lacked: *"a slide asserting 10x − x leaves a repeating
    tail when it leaves 3.5 exactly"* and *"a Study Guide table saying 30/36/34 beside banners
    saying 7/7/7"*.
11. The precise values `π³ ≈ 31.006` / `3π ≈ 9.425` (master had 31.0 / 9.4), and "Nothing in the
    tree knew what either picture said".

**§1**
12. **Rule 3 in full** — the pages that carry no codes, the title-slide and answer-key exemptions,
    the Croix quotation of 1 September, the ~twenty places the shipped set broke the old wording,
    the `docscan.py` `paper` scope, and "naming the mathematics beats naming the code".
13. **Rule 6's per-part material** — one lettered part is one point; A7 Unit 1 is 21, A7 Unit 2 is
    34; the fork's wording of the 1 September Croix quotation; the 2 September extension to
    on-level (*"same philosophy I ruled for accelerated"*); follow-through; grain as a scoring
    decision; the single `Q` map; the Practice Test's own first line and its /21.
14. **Rule 8 in full** — calculators allowed on everything, the 2 September Croix quotation, what
    counts as a "calculator line", **the obligation being on the question not the policy**, and
    the FLDOE sentence with the warning to get it from FLDOE and not from memory.

**§6**
15. **The retirement of the printed Scoring Sheet** — Croix's quotation, the split between the two
    A7 keys, both keys now carrying the Score Tracker and no sheet (Unit 1's opening with it,
    Unit 2's closing with it, either end fine), and the **item ledger kept in the generator** and
    asserted against the paper's total at build time.

**§9**
16. **The worksheet share is the remainder, computed, not chosen** — `deckread.js`,
    `planFromDeck`, the explicit replacement of "45–50 with 3–8", and A7's measured 40–48 / 5–13.
17. **"A plan that does not fit refuses to build"** — `planFromDeck` throws, `decktime.js` checks.
18. **"The teacher's edition reads the deck. It does not keep a second copy of it."** —
    `telib.deckPlan`, `nm("Notes III")`, the sixteen hand-typed tables, and the throw.
19. The Teacher Edition row's clause that the timing table and slide numbers are read from the deck.

**§13**
20. **Item 7, deck geometry** — `slideoverlap.py` (0.78 / 0.48 / 0.62 threshold), `shapeoverlap.py`
    (picture-vs-text-frame, ink-shrink, `shapeoverlap.ack.json` with a reason), `decktime.js`, and
    the **"a placer that does not record where it ended"** blockquote.

**§14**
21. **A7 — the pop quiz is scored per part** (Croix, 4 September): Quiz 1's surviving `/ 10`,
    question 7's four points, *"an answer with no work is half credit"*, now **out of 8**.
22. **A7 — Unit 2 question 6 stays one all-or-nothing point** (Croix, 4 September), with the
    reason and the /38 correction.
23. **The fade's correction from "next unit" to "next QUARTER"**, with the fork's note on why the
    old wording was false and how the source line was left unrepaired behind the four documents.
24. **SETTLED, 4 September: A7 is on the two-document model now, not at Q2** — Reference Sheet
    unchanged, Study Guide now blank, **Study Guide COMPLETED** in `Answer Keys/`.
25. **One generator, `FILLED = process.argv[2] === "filled"`**, the required `ask` per skill, the
    throw, and the unchanged `guideleak.py` token set.
26. **"The fade is unaffected and its words now mean one thing."**
27. **"Judged and kept, 5 September"** — the §7 cube entry, and "every number here differs"
    being true item for item and false digit for digit.
28. **"Judged and kept"** — B5/B2 and C5/C4 as the chain working.

**§16**
29. **The SSDD label ruling** — *the name goes on the KEY, never on the student paper* (on-level
    worker, 4 September; A7 matched the same day), including "any line to the same effect on the
    paper goes the same way" and "noticing that the parts differ **is the task**".
30. **The rule-3 checkable note** — including *a check coupled to a name stops you fixing the name
    even when the name is the defect*.
31. **The corrected question numbers with their placement** — both blocks at question 9, A7 Unit 1
    at the opening of Part B, A7 Unit 2 at the end of Part A. (Both files already said 9; the fork
    supplied the placement.)
32. **"a switched-off check is worse than no check, because the next person believes the green."**
33. Two cross-reference precisions in the rule-6 table: "§5, **and the 1.04 grid**" and
    "§1 **rule 4**"; and "coverage is recorded per unit, **in the changelog**".

---

## 3. Conflicts, and how each was resolved

### The three that were already ruled

**C1 — Scoring sheets. RULED: retired.** *Under the 4 September ruling; Croix: "no need for a
scoring sheet, a detailed key is good."*
The master's §6 required a Scoring Sheet on every assessment key. That requirement is **retired**
and replaced by the fork's §6 bullet: a detailed key is enough, both A7 keys carry the Score
Tracker and no sheet, Unit 1's opens with it and Unit 2's closes with it, and either end is fine.
Consequential edits made under the same ruling, all recorded here so none of them is silent:
- The retired requirement's own text (including the unique-label discipline `4a dec`, `4a pct`,
  `8 r1` … `8 r4`) is **quoted inside the retirement bullet** rather than deleted, so a reader can
  see what was retired.
- §13b ruling 5 item 2 said the header, banners, printed values "and the scoring sheet" all come
  from one map. Changed to "the item ledger", with a parenthesis recording the retirement.
- §13b ruling 5's "No scoring sheet" bullet now cross-references §6.
- §1 rule 6's ported sentence about M7's conversion still says "with their scoring sheets …
  regenerated to match". **Left standing**, with a flagged note beside it, because it is a record
  of what was done on 2 September; the note says the sheets no longer exist.

**C2 — A7 Unit 2 question 6. RULED: not adopted for the accelerated course.** *Croix, 4 September.*
The master's §13b ruling 5 recorded a 3 September ruling splitting an ordered list one point per
number and stated "**Q6 is split**, and now matches Q9's six". Applied:
- **On-level keeps the 3 September ruling** — M7 Unit 2 Q7 is four points, one per number placed.
- **A7 Unit 2 Q6 stays one all-or-nothing point**, and that paper stays **out of 34**. Reason
  recorded in §14 in Croix's terms: *ordering a list is one judgment, not five, and a student who
  has three of five in the right places has not ordered the list.*
- **Factual error in the master corrected.** The master's "Q6 becomes six" is wrong twice: the item
  has **five** numbers, not six, so a split would have made that paper **/38, not /39**. The
  correction is stated in both §13b and §14 rather than silently applied.
- The forward reference earlier in ruling 5 ("This is what settles the open A7 question below: Q6
  is split") was amended to say it settled it *for on-level only*.

**C3 — The pop quiz. RULED: rescored per part, as an extension of the ruling.** *Croix,
4 September.* Both files stated that the per-part ruling did not touch the pop quiz. Both
statements were updated:
- §1 rule 6's scope now reads: unit assessments, any parallel form of one, and A7's pop quiz.
- §13b ruling 5's scope bullet now carries the same, with the Quiz 1 evidence (`/ 10`, question 7
  at four points, *"an answer with no work is half credit"*) and **out of 8**.
- §14 carries the full entry.
Croix's blessing is recorded as **an extension of the ruling rather than an exception to it**, in
those terms, in all three places.

### The conflicts the two files raised on their own

**C4 — §1 rule 3, benchmark codes. Resolved: the fork's wording.**
Master: *"No benchmark codes on anything a student sees."* Fork: *"No benchmark codes on a page a
student works from,"* with the title-slide and answer-key exemptions. These genuinely conflict —
but the master's own §13b ruling 6 and §15 trap 23 both record that "anything a student sees" is
the **retired** form and that Croix exempted title slides on 1 September. The master was
disagreeing with itself, which is the failure its own §13 blockquote warns about. The fork's
wording is the one consistent with the ruling, so it wins. No new rule was invented.

**C5 — §1 rule 8, calculators. Resolved: the fork's wording.**
Master rule 8 still said on-level prints a calculator line on unit assessments. The master's own
§13b **ruling 2** (Croix, 2 September) says nothing about calculators is printed on any test page
in either course. Same shape as C4: the master contradicted its own recorded ruling, and the
fork's rule 8 — which carries Croix's 2 September quotation — is the consistent one. Ported whole.

**C6 — §9 timing. Resolved: the fork's computed remainder.**
Master: *"Both courses run 45–50 minutes of instruction with 3–8 of worksheet."* Fork: that range
was typed by hand and was wrong for fifteen of the sixteen rebuilt A7 lessons; the share is now
computed from the deck. The master's own §14 already records the 45–50 / 3–8 figure as corrected
on 1 September, so the §9 sentence was a retired rule still asserted elsewhere. The fork's bullet
replaces it and quotes the retired sentence inside its own replacement note.

**C7 — §9 document types, Study Guide and Reference Sheet. Resolved: the master.**
The fork's table still describes one document doing both jobs ("Study Guide | A reference, not a
practice set…"). §13b ruling 4 splits them. The master's two rows are kept; the fork's row is
dropped (see D7).

**C8 — the fade's horizon. RULED: "next QUARTER".** Master §14 said the Study Guide's last page
tells students that *next unit* this is all they get. The fork records that as false — Units 1 and
2 are both inside Q1 — and corrected to **next QUARTER**. Applied, with the fork's note about the
four shipped documents having been repaired while the line they are built from was not.

**C9 — §16 SSDD rollout question numbers. No real conflict.** Both files say question 9 and both
record that the accelerated copy's "41 and 31" were wrong. The fork's placement detail (Unit 1 at
the opening of Part B, Unit 2 at the end of Part A) was added to the master's line.

**C10 — the per-part scope and the unit reviews. NOT RESOLVED — see §5, open item O1.**

**C11 — the 1 September Croix quotation is recorded differently in the two files.
Both kept; not smoothed over.**
- Master §13b ruling 5: *"instead of being out of 100, I'm going to just count each touch point
  from a student as 1 point. **then** add them up and that's what the test is out of."*
- Fork §1 rule 6: *"instead of being out of 100, I'm going to just count each touch point from a
  student as 1 point**,** then add them up and that's what the test is out of."*
The difference is a full stop against a comma. Both records are kept where each fork had them, and
`MERGED.md` states in §1 rule 6 that the two records differ and that the difference is not the
file's to resolve. **A difference in what he is recorded as saying is not ours to smooth over.**

**C12 — the §0 lead-in. Resolved: the master.** Master: "after wrong answers reached student pages
in both courses in one week". Fork: "after two wrong answers reached student pages in one week".
The master's is the two-course statement and the merged file covers both courses. The fork's
"eleven checks then in place" sentence was ported into the same section (port 9), so nothing in
the fork's framing was lost.

---

## 4. Dropped, with the reason

Nothing was dropped because it was inconvenient. Each of these is a passage that exists in one
file and not in `MERGED.md`.

| # | Dropped | From | Reason |
|---|---|---|---|
| D1 | The fork's three-line preamble ("This file is the source of truth…") | fork | Superseded by the new opening plus the master's fuller preamble, which says everything it said and more (the two Source-of-Truth documents, `speccheck`, the 2 September ruling). |
| D2 | The fork's §0 "What went wrong, **precisely**" narrative (its numbered items 1 and 2) | fork | The master's "in both courses" version carries the same two A7 defects plus the three M7 ones. Its distinct details were ported individually (ports 9, 11). Its cross-reference "§13 already says a wrong answer beside correct-looking reasoning reads as already checked" is redundant — that blockquote is in §13 of the merged file. |
| D3 | The fork's "Then the harness was measured against a reading, and lost" (forty-five defects, single course) | fork | The master's "— twice" version states the same forty-five *and* the M7 forty-nine, totalling ninety-four. The fork's number survives inside it. Its two extra table examples were ported (port 10). |
| D4 | The fork's "So the reading is now the gate, not the harness" bullets | fork | The master's equivalent section is a superset (it adds `pdftwin.py` and `pagecheck.py`). The fork's extras were ported (ports 5, 6, 7). |
| D5 | The fork's closing "Two things stay on the person" paragraph | fork | The master's version of the same two things is longer and includes "check the shipped PDF, not the source" plus "a generator that has been throwing for days looks exactly like one that is fine until you run it alone". Kept the clearer one. |
| D6 | "Colouring" (2a rule 4) | fork | Spelling variant of the master's "Coloring". Only textual difference in all of §2/§2a. |
| D7 | The fork's Study Guide row ("A **reference**, not a practice set…") and its bare Reference Sheet row | fork | Superseded by §13b ruling 4, which the fork did not carry. The master's two rows say both things correctly. |
| D8 | The fork's Teacher Edition row phrase "and what changed from Math Nation" | fork | The master's row explicitly rejects that phrasing ("not 'what changed from Math Nation', which describes a lesson that started from the book"). The fork's deck-reading clause from the same row **was** ported. |
| D9 | The fork's §14 Practice Test sentence "the study guide is the reference" | fork | Under ruling 4 the *Reference Sheet* is the reference. The master's wording of the same entry is used. |
| D10 | The fork's §16 rule 5 four-row slot table | fork | The master states the same four bands in prose ("yesterday · last week · earlier this unit or last unit · anything from the year so far"). Kept the master's, because §9 and §13 of this file both warn that a number in a table outranks a principle in prose. |
| D11 | The fork's §16 rule 5 "Open, and it needs Croix or a stated default" blockquote | fork | The master resolves the same open question: the prior-grade default is **adopted for both courses**, marked as adopted rather than ruled so Croix can overturn it, and refined so the prior-grade question must be the prerequisite that lesson needs. The master's is the later state of the same item. |
| D12 | The fork's "a check that fails on **sixteen** lessons the ruling explicitly exempts" | fork | The master makes the same argument with its own measured figure (twenty-seven findings on the first run). Two different numbers for two different corpora; keeping both in one paragraph would assert a fact neither file states. The fork's distinct half — the switched-off check — **was** ported (port 32). |
| D13 | The fork's per-rule "`designcheck.py`, rule N" pointers | fork | The master carries the same information as a marker table that also says what each check reads and what it cannot see. Kept the more informative one. |
| D14 | "and the scoring sheet" in §13b ruling 5 item 2's list of things derived from the map | master | Retired under C1. Replaced by "the item ledger", with the retirement noted in place. |
| D15 | The master's §6 Scoring Sheet requirement as a live rule | master | Retired under C1. Its text is quoted inside the retirement bullet, so it is not gone from the file. |
| D16 | The master's §1 rule 3 and rule 8 as live rules | master | Superseded under C4 and C5, by the master's own recorded rulings. The old rule-3 wording is quoted inside the new rule 3 ("The rule previously read 'on anything a student sees'"). The old rule-8 wording is not quoted; it asserted a printed calculator line on M7 unit assessments, which §13b ruling 2 forbids outright. |
| D17 | The fork's §16 heading wording ("Math Nation's role changed on the same date", "Rollout — and why the checks report rather than fail") | fork | Heading variants; the master's headings carry the same sections. No content dropped with them. |

**Editorial corrections made, listed so they are not mistaken for source text:**
- The §9 document-types table's cross-references "the Variation note (§9b rule 2)" and "Under §9b
  it does not" now point at **§16**. §9b of the master is a pointer stub with no rules in it; §16
  is where rule 2 lives, and §9b itself says §16 is the number both courses cite.
- §14's removed-calculator note now cites "§1 rule 8 and §13b ruling 2" rather than §13b alone,
  because after C5 rule 8 also states it.
- One pronoun fixed: `FORK-a7.md` line 187, "**She** extended it to on-level on 2 September" →
  "**He** extended it". That is the only wrong-gender pronoun referring to Croix in either file
  (both files were grepped). The "her" in the §0 defect table refers to a **student** in a worked
  example and was deliberately left alone.

---

## 5. Left open for a person — not guessed at

**O1 — Are the on-level unit reviews inside the per-part scoring scope?** The two files disagree
and this merge did not pick a side.
- `MASTER-m7.md` §13b ruling 5: *"**Unit reviews are NOT scored** — Croix, 3 September: 'I don't
  want to score reviews.'"* — a direct, dated quotation.
- `FORK-a7.md` §1 rule 6: *"M7's assessments **and unit reviews** convert from weighted /100 to
  per-part…"* and *"This applies to the unit assessments, to the on-level unit reviews, and to the
  Practice Test."*
- `FORK-a7.md` §14, dated 4 September — later than the quotation — restates the scope as
  *"unit assessments, the practice test, **the on-level unit reviews**, and the pop quiz"* while
  in the next sentence saying *"unit reviews still carry no point values at all."* The fork
  contradicts itself here as well.
Both statements are carried in `MERGED.md`: the ruling stands as written in §13b, and the fork's
sentence stands in §1 rule 6 inside a blockquote that says plainly that the two disagree and that
it is Croix's call. **Nothing was blended and nothing was quietly dropped.** A one-line answer from
Croix settles it, and then one of the two passages should be deleted.

**O2 — §13c says "Twenty" checks and the table names nineteen.** Counted twice: `mathcheck`,
`xmlcheck`, `glyphaudit`, `imagedrift`, `indexdrift`, `figglyph`, `barwidth`, `plancheck`,
`speccheck`, `specdiff`, `docscan`, `boxcheck`, `pagecheck`, `buildref`, `figscale`, `pdftwin`,
`designcheck`, `guideleak`, `piglyph` — nineteen. Neither fork names a twentieth, and the fork's
tools that would make it twenty (`rederive`, `offpage`, `partsum`, `figstale`) are listed in the
same section as **not yet built on-level**, so adding one to the table would assert something
neither file says. A note saying exactly this was added under the table in `MERGED.md` rather than
a number being quietly changed.

*Update, 6 September.* Two more checks were written since — `gdoccheck` (will Google Docs import
this .docx faithfully) and `tedeck` (is any teacher's edition older than the deck it quotes) —
and both are in the table now. That makes twenty-one, which closes the arithmetic without
answering the question: neither was the missing twentieth, because neither existed when the count
was recorded. **O2 stays open.** Two REPAIRS also joined `finish()` and are listed under the table
rather than in it, because they change documents rather than report on them: `keepwith` and
`pagebind`. And `buildpdf` runs at the head of every pack script, which is a rebuild step, not a
check at all.

**O3 — The 1 September quotation differs between the two records** (C11). Both are kept. Someone
with the original message should decide which is the transcript; until then the merged file says
they differ.

---

## 6. What was checked before this was called finished

- Both files read in full — 1,599 and 1,136 lines — before any edit was written.
- Sections believed identical were **diffed**, not assumed: §2/§2a (one word differs), §3–§5, §7–§8,
  §10–§12, "A finding is not a decision", §13 items 1–6, "Two drift checks", §15 traps 1–11. All
  clean apart from the one noted spelling.
- Every edit to the master was applied as an exact-string replacement that **asserted a unique
  match** before it was made; a failed match aborted the run. 40 edits, every one matched
  exactly once.
- A normalized line-level sweep of `FORK-a7.md` against `MERGED.md` was run to find fork content
  that had not landed; every one of the 158 flagged lines was reviewed by hand and is accounted
  for above as either ported, identical-in-substance, or a listed drop.
- Grepped the result for: remaining Scoring Sheet requirements, wrong-gender pronouns, "next unit"
  in the fade, the /34 and /38 figures, and dangling §9b references.
