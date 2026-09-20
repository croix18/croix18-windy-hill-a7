# SPEC SCHEMA — every field a lesson spec, unit spec and manifest can carry

A lesson is one Python file, `a7/build/<unit>/lNN.py`, holding one dict named `L`. The unit
documents are `<unit>/unit.py` holding `U`; the package is described by `<unit>/manifest.py`
holding `M`. **The canonical worked examples are `u3/l04.py` (a numerical lesson), `u3/l08.py`
(a lesson with word-form items and tagged coefficients), `u3/unit.py` and `u3/manifest.py`.**
Copy one and change every field; do not start from a blank file.

Markup that works in every string rendered on paper (`dockit.rich`): `$latex$` becomes an image;
`**bold**`; `__vocab term__` (blue bold). **A `**…**` span may not contain `$`** — write
`"**Reciprocal pairs.**  $x^{3}$ and …"`, never `"**$x^{3}$ is …**"`. On slides, `$…$` inside a
row makes the row a "mixed" row (text + images) that is laid out on one line and **must fit the
slide width** — the build raises "line runs off the slide" if it does not; split the row.

LaTeX goes through matplotlib mathtext, not TeX: `\frac`, `\cdot`, `\times`, `\left(`, `\right)`,
`\sqrt`, `\leq`, `\neq`, `\div` work; `\le`, `\text{}`, `\dfrac`, `\hbox` do **not**. Thousands
separators inside math are `1{,}000`. Unicode superscripts (`⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ᵐⁿ`) may be used in plain
text and are converted to real superscript runs; `⁽ ⁾ ✗` and other exotic characters have no glyph
in the fonts and fail the glyph check. Dollar signs in prose are impossible (they open math) —
write "30,100,000,000 dollars". The word "calculator" and any `MA.x.xx.x.x` code may not appear
on a student surface (docscan fails the build); write "a computer displays 3.5E9". The Reference
Sheet alone may describe the FAST calculator.

## `L` — a lesson

| field | type | meaning |
|---|---|---|
| `code` | str | file code: `"3.04"`, or `"3.T1"` for a thread day. Two digits after the point. |
| `unit` | int | unit number |
| `lesson_no` | int or str | prints as "Lesson 4"; `"6–7"` for a merged pair |
| `label` | str, optional | overrides "Lesson N" everywhere: `"Thread A · Day 1"` |
| `title` | str | lesson title, as on the title slide and every header |
| `benchmark` | str | the ONE benchmark on the title slide, e.g. `"MA.8.NSO.1.3"` |
| `benchmark_text` | str | the benchmark's exact wording (from the Source of Truth) |
| `target` | str | "I can …" — ≤ ~170 characters or the title slide wraps to three lines |
| `yesterday`, `today` | str | the two lines in the title-slide box; keep `today` ≤ ~60 characters |
| `essential` | str | essential question (TE only) |
| `building_on`, `working_toward` | str | vertical alignment lines (TE) |
| `vocab` | list of (term, definition) | definition may carry `$…$` |
| `ixl` | list of str | `"Skill name — CODE"`; codes from `a7/reference/ixl_skills_by_lesson.json`; prefix `"Also consider: "` for the plan's optional skill |
| `warmup` | list of 4 dicts | see below — bands: yesterday / last week (or "this week") / last unit / prior grade |
| `warmup_note` | str | TE note for the warm-up slide |
| `title_note` | str, optional | TE note for the title slide |
| `notes` | list of dicts | Notes slides, see below (usually three: I, II, III; 3–4 min each) |
| `examples` | list of 2 dicts | see below |
| `whiteboard` | list of exactly 9 dicts | see below; #9 is `kind="written"` |
| `bank`, `additional` | list of item dicts | the two question banks; `additional` mirrors `bank` position by position with new numbers |
| `te` | dict | Teacher Edition prose, see below |

### warm-up question
`dict(stem, answer, band, source, check)` — `stem` may hold `$…$` and must fit one slide line at
23 pt beside its number (≈ 70 characters of text, less with images); `answer` is printed red
beside the stem and wraps to a second line if too wide; `band` is the retrieval band; `source`
names the lesson/unit it retrieves ("3.02 — quotient of powers"); `check` as for items.

### notes slide
`dict(numeral, head, min, sub, note, …)` plus any of: `items` (lettered rows: plain strings,
`"**bold row**"`, or `(term, rest)` vocab tuples), `letters=False` to drop the letters,
`table=(widths_in_inches_list, rows)` with `tsize` (pt, default 16), `math=[…]` (one `$…$` row
per entry, centered), `text=[…]` (plain sentences), `items2` (rows after the math), `size`,
`panel=True` (a boxed first block). `note` is the TE's slide note; a line beginning `OFF:` inside
it is printed in the TE as *OFF THE SLIDE, YOURS TO SAY* — the sentence the teacher says that
is not on the slide. A `not_sci=True` key on a notes dict exempts it from the coefficient scan.

### example
`dict(title, sub, min_q, note_q, prompt=[rows], ask, worked=[…], check, your_turn={…}, yt_check)`.
`prompt` rows: a `$…$` row is centered math; a plain row is centered text (wraps). `ask` is the
bold instruction line ("" to omit). Each `worked` entry: `dict(sub, min, note, rows, answer)` where
`rows` are `(latex, gloss)` tuples — the latex is set at the left, the gray gloss beside it (keep
the gloss ≤ ~45 characters) — or plain strings. `your_turn`: `dict(min, note, prompt=[rows],
gloss, answer | answer_latex)`. `check` and `yt_check` are re-derived by sympy like any item.

### whiteboard question
`dict(kind="free"|"mc"|"written", latex | text=[rows], hint, gloss, answer | answer_latex, note,
check, wrong, …)`. `latex` is set large and centered; `text` rows are centered (a row with `$`
is a mixed row and must fit one line). `hint` prints under "Answer it." on the question slide.
`gloss` is the gray line on the reveal. `note` is the TE note; `note_a` optionally the reveal's.
`wrong` is the TE's named-wrong-answers line for free/written questions: `"value — error name
[benchmark cite]; …"`. **`kind="mc"`** adds `choices` (4 strings, unicode superscripts allowed),
`correct` (index), `answer` ("A — 25m⁶") and **`errors`** — a dict from every wrong letter to
`"what the student did [benchmark or B1G-M cite]"`; the build refuses an mc item with a wrong
option that has no cited error. **`kind="written"`** adds `qtext` (the plain-text question for
the TE) and the answer states the full-credit sentence.

### bank / additional item
`dict(stem, answer, why, check, space)` for a one-part question (`space` = inches of work room);
`dict(stem, parts=[dict(label, stem, answer, why, check, space), …])` for lettered parts;
`dict(stem, choices=[…], correct=i, answer="A", errors={…}, why, check)` for multiple choice;
`correct=[i, j, …]` makes it select-all (square boxes). `dict(heading="…")` prints a bold
instruction line between groups. `lines=n` prints n ruled lines instead of `space`.
`not_sci=True` (first key) marks an item that is ABOUT the coefficient rule. `key_stem` (unit
documents only) is a stem printed on the key in place of `stem` — the SSDD label lives there.

**The two Unit 4 boundary escapes.** `capcheck` also refuses (a) an addition or subtraction whose
two powers of ten are more than 2 apart, the MA.8.NSO.1.5 clarification, and (b) a radicand that
is not a perfect square up to 225 or a perfect cube from −125 to 125. A rational radicand passes
when its numerator and its denominator are each in range, so `∛(1/8)` and `√(1/9)` are fine. An
item that shows a wider gap on purpose — because it is ABOUT the boundary — carries
`not_gap=True`; one that uses a stretch radicand on purpose (a Unit 2 estimation retrieval item,
or the Dotson √200 task) carries `not_bound=True` and says why in its `note` or `source`. Both
flags work like `not_sci`: put them on the item dict and they cover everything inside it.

### `check` — the mathcheck field (mandatory on every item, part, warm-up and example)
A tuple sympy evaluates at build time with `F = Rational`, `sqrt`, `pi`, `abs`, `floor`,
`Float`, `sp` (sympy itself), and the letters `a b c d k m n p q r s t w x y z` as **positive
symbols** (so `x**0` is 1 and quotients cancel; use only these letters as variable bases):
- `("eq", "expr", "keyed")` — exact symbolic equality. Use `F(2)**-3`, `F(3,4)**2`; never
  Python floats where a rational exists. Variable bases: `("eq", "(3*m**2*n)**3/(9*m**4*n)",
  "3*m**2*n**2")`.
- `("val", …)` — same as eq (kept for readability of decimal answers).
- `("approx", "expr", "keyed", "tol")` — |difference| ≤ tol, for rounded answers.
- `("true", "python boolean over sympy values")` — e.g. `"9**2 < 95 < 10**2"`,
  `"sp.simplify(x**4*x**3 - x**12) != 0"` for "these are NOT equal".
- `("many", check, check, …)` — several of the above; use it for select-all (every correct
  option `eq`, every wrong option `true …!= …`) and for multi-value answers.
An item may carry `ack="reason"` instead of a check **only** for a purely verbal item; do not
use it to skip work.

### `te`
Under **ruling 26** the teacher's edition is **four printed pages or fewer** and `checks.py`
fails a longer one. Only these fields reach it:

- `must` / `must_not` — the benchmark's two lines, quoted from the Source of Truth or the B1G-M
  notes. (If absent, they fall back to `standard_notes`' "Clarification" and "Boundary".)
- **`say=[three strings]`** — the three sentences to say out loud today. They are the last thing
  on page 1 and nothing else goes there.
- `materials` — one line, printed at the end.

Everything else in `te` — `read_first`, `variation`, `audit`, `changes`, `sits`, `lives` — no
longer prints in the teacher's edition. It is written to **`a7/unitNN/BANK - Unit N.md`** by
`bank_file.py`, together with every bank answer, and installs into the package's `Reference/`
folder. Keep writing those fields: that file is where the unit's reasoning lives.

### `mtr` and `hoq` — ruling 25
- **`mtr=[("MTR.4.1", "evidence line"), …]`** — the two or three MA.K12.MTR.x.1 the lesson
  actually exercises, each with one line of evidence from the period ("the re-vote on board 5").
  Not all seven. **The build refuses a lesson with no `mtr`.**
- `hoq=[(question, "DOK n"), …]` — the higher-order questions the plan prints with their DOK.
- `differentiation=dict(ese, ell, enrichment)` — one concrete line each.

## `U` — the unit documents (`unit.py`)

`dict(unit, title, reference_intro, reference=[sections], review=[parts],
assessment=dict(total, tracker_order, tracker, follow_through, days=[…]))`.

- `reference` sections: `dict(title, right, blocks=[…], not_sci=…)`; a block is a prose string
  (bold lead + sentence), `dict(table=(widths_twips, rows), header=True/False)`,
  `dict(bullets=[…])` or `dict(vocab=[(term, dfn), …])`. Column widths are twips and sum to 9360.
- `review` parts: `dict(letter, title, lessons, benchmark, items=[…])` — items as in banks. One
  item per review carries the **SSDD block**: a stem with four lettered parts on the same
  surface asking four different things, with `key_stem="**SSDD.**   …"` so the label prints on
  the key only. The review is unscored: no points anywhere.
- `assessment.sections`: `[dict(title, benchmark, items=[…])]` — **one paper, numbered straight
  through, with no Day 1 / Day 2 division anywhere** (ruling 27). The paper's front line says it
  runs over two periods and that students continue from where they stopped; the student line for
  follow-through credit (ruling 19) sits under it. Every lettered part is one point; every
  single-part item is one point. `total` and `tracker` (benchmark → points) are asserted against
  the items at build time; `tracker_order` fixes the Score Tracker's row order.
- **Exactly two items carry `transfer=True`** (ruling 18) and the build refuses any other count.
  A transfer item is the same benchmark and the same one-operation demand on a surface that
  appears on no review and in no question bank — not harder, not longer, not a chain. The key
  prints *TRANSFER ITEM — not on the practice test. Same benchmark, a surface nobody rehearsed.*

## `M` — the manifest (`manifest.py`)

`dict(unit, title, folder, audit_src, summary, lessons=[(code, label, title, benchmark,
carry_line)], assessment=(benchmarks, points), naming_note, order_note,
before_unit=[bullets])`. `lessons` is in teaching order and drives the START HERE tables and the
timing table (read from the deck side-cars, never typed).
