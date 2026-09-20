"""Turn one LESSON spec into: Slides (.pptx + side-car), Question Bank, Question Bank - Additional,
both keys, and the Teacher Edition. Every item's answer is re-derived by sympy at build time
from its `check` field (mathcheck); an item with no check and no acknowledged human derivation
fails the build. Every multiple-choice wrong option must carry a named error (distractorcheck,
§16 rule 4, mandatory under ruling 10).
"""
import os, re, json
import sympy as sp
from sympy import Rational as F, sqrt, Integer, nsimplify
from .dockit import Doc, INK, VOCAB, RED, GRAY
from .deckkit import Deck, LM, CW
from . import tekit
from . import plankit
from .tekit import TE

COURSE = "Grade 7 Accelerated"


# ---------------------------------------------------------------- mathcheck
def _ev(expr):
    env = {"F": F, "sqrt": sp.sqrt, "Integer": Integer, "sp": sp, "Rational": F, "nsimplify": nsimplify,
           "pi": sp.pi, "Abs": sp.Abs, "abs": sp.Abs, "N": sp.N, "floor": sp.floor, "Float": sp.Float,
           # symbols for the Thread A (MA.8.AR.1.1) algebraic checks. Declared positive so that
           # x**0 -> 1 and x**-n and quotients simplify without a zero-base caveat; the items
           # themselves state "nonzero" where it matters.
           **{s: sp.Symbol(s, positive=True) for s in "abcdkmnpqrstwxyz"}}
    return sp.sympify(eval(expr, {"__builtins__": {}}, env))


def mathcheck_item(item, where):
    """Return list of findings (strings). Empty = verified."""
    out = []
    chk = item.get("check")
    if chk is None:
        if item.get("ack"):
            return []
        return [f"{where}: no check and no ack"]
    kind = chk[0]
    try:
        if kind == "eq":            # two expressions equal exactly
            a, b = _ev(chk[1]), _ev(chk[2])
            if sp.simplify(a - b) != 0:
                out.append(f"{where}: {chk[1]} = {a} but keyed {chk[2]} = {b}")
        elif kind == "val":         # expression equals a decimal/number to stated places
            a = _ev(chk[1]); b = _ev(chk[2])
            if sp.simplify(a - b) != 0:
                out.append(f"{where}: {chk[1]} evaluates to {a}, keyed {b}")
        elif kind == "approx":      # |a-b| <= tol
            a, b, tol = _ev(chk[1]), _ev(chk[2]), _ev(chk[3])
            if abs(float(a - b)) > float(tol):
                out.append(f"{where}: {chk[1]} ≈ {float(a)}, keyed {float(b)}, tol {tol}")
        elif kind == "true":        # a python boolean over sympy values
            if not bool(_ev(chk[1])):
                out.append(f"{where}: assertion false: {chk[1]}")
        elif kind == "many":
            for sub in chk[1:]:
                out += mathcheck_item({"check": sub}, where)
        else:
            out.append(f"{where}: unknown check kind {kind}")
    except Exception as e:
        out.append(f"{where}: UNSOLVED ({e})")
    return out


def mathcheck_lesson(L):
    findings = []
    n = 0
    for grp in ("warmup", "whiteboard", "bank", "additional", "independent"):
        for i, it in enumerate(L.get(grp, [])):
            if it.get("heading") or it.get("table"):
                continue
            for f in _flatten(it):
                n += 1
                findings += mathcheck_item(f, f"{L['code']} {grp}[{i}]")
    for ex in L.get("examples", []):
        for k in ("check", "yt_check"):
            if ex.get(k):
                n += 1
                findings += mathcheck_item({"check": ex[k]}, f"{L['code']} {ex['title']} {k}")
    return findings, n


def _flatten(item):
    if item.get("parts"):
        return [dict(p, _parent=item) for p in item["parts"]]
    return [item]


def distractorcheck_lesson(L):
    out = []
    for grp in ("whiteboard", "bank", "additional", "independent", "warmup"):
        for i, it in enumerate(L.get(grp, [])):
            if it.get("choices"):
                corr = it["correct"] if isinstance(it["correct"], (list, tuple, set)) else [it["correct"]]
                for k in range(len(it["choices"])):
                    if k in corr:
                        continue
                    letter = chr(65 + k)
                    e = (it.get("errors") or {}).get(letter, "")
                    if not e or "[" not in e:
                        out.append(f"{L['code']} {grp}[{i}] option {letter}: no named error with a benchmark cite")
                vals = [str(c) for c in it["choices"]]
                if len(set(vals)) != len(vals):
                    out.append(f"{L['code']} {grp}[{i}]: two choices print the same value")
                # A whiteboard's options are drawn straight onto the slide as text; only the .docx
                # surfaces render $latex$. A dollar-delimited option on a board prints its braces.
                if grp == "whiteboard":
                    for k, c in enumerate(vals):
                        if "$" in c:
                            out.append(f"{L['code']} whiteboard[{i}] option {chr(65 + k)}: "
                                       f"$latex$ in a board's option, which the slide prints literally "
                                       f"(use plain text with unicode superscripts): {c[:40]!r}")
    return out


_SCI = re.compile(r"(\d+(?:\.\d+)?)\s*(?:\\+times|×)\s*10\s*(?:\^|[⁰¹²³⁴⁵⁶⁷⁸⁹⁻])")

# ---- the two Unit 4 boundaries that are machine-checkable (MA.8.NSO.1.5 / 1.6 / 1.7) ----
_SUP = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5",
        "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "-"}

# one scientific-notation term, with its exponent captured in whichever form it is written
_SCI_TERM = re.compile(r"(\d+(?:\.\d+)?)\s*(?:\\+times|×|\\+cdot)\s*10\s*"
                       r"(?:\^\s*\{\s*(-?\d+)\s*\}|\^\s*(-?\d+)|([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+))")
_GAP_JUNK = re.compile(r"[\s$]|\\+[,;:!]|\\+quad|\\+qquad|\\+ ")
_ADDSUB = {"+", "-", "\u2212", "\\pm", "\\\\pm"}
_SQRT_TEX = re.compile(r"\\+sqrt\s*(?:\[\s*(\d+)\s*\])?\s*(\{(?:[^{}]|\{[^{}]*\})*\})")
# A unicode root followed by a plain integer, or a plain integer in parentheses. A root written
# in unicode over anything else (√(2³ + 8)) is left to the LaTeX form, which carries its
# structure; guessing a radicand from a prefix is how a check starts lying.
_SQRT_UNI = re.compile("[\u221a\u221b]\\s*(?:\\(\\s*(-?\\d+)\\s*\\)|(-?\\d+)(?![\\d.,^\u00b9\u00b2\u00b3\u2070-\u209f]))")
_SAFE_ARITH = re.compile(r"[0-9+\-*/(). ]*")

SQ_MAX = 225          # MA.8.NSO.1.7 boundary: perfect squares up to 225
CUBE_LO, CUBE_HI = -125, 125   # and perfect cubes from -125 to 125
GAP_MAX = 2           # MA.8.NSO.1.5 clarification: exponents within 2 for + and -


def _sci_exp(m):
    if m.group(2) is not None:
        return int(m.group(2))
    if m.group(3) is not None:
        return int(m.group(3))
    return int("".join(_SUP[c] for c in m.group(4)))


def _radicand_value(tex):
    """The radicand as an exact rational, or None if it is not plain arithmetic on integers.
    A rational radicand is allowed when numerator and denominator are each in range (the book's
    1/8, 1/27, 1/125, 1/9 forms) — the audit asked for this to be told to us, not guessed."""
    t = tex.strip()
    if t.startswith("{") and t.endswith("}"):
        t = t[1:-1]
    t = re.sub(r"\\+[dt]?frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}", r"((\1)/(\2))", t)
    t = t.replace("\\cdot", "*").replace("\\times", "*").replace("^", "**")
    t = t.replace("{", "(").replace("}", ")")
    if not t.strip() or not _SAFE_ARITH.fullmatch(t):
        return None
    try:
        v = sp.nsimplify(sp.sympify(t))
    except Exception:
        return None
    return v if getattr(v, "is_Rational", False) else None


def _in_range(n, deg):
    """One integer, against MA.8.NSO.1.7's list for roots of this degree."""
    if deg == 2:
        return 0 <= n <= SQ_MAX and bool(sp.integer_nthroot(int(n), 2)[1])
    return CUBE_LO <= n <= CUBE_HI and bool(sp.integer_nthroot(abs(int(n)), 3)[1])


def _rad_ok(v, deg):
    p, q = sp.fraction(sp.Rational(v))
    return _in_range(int(p), deg) and _in_range(int(q), deg)


# Keys whose strings are teacher-only prose: the note beside a slide, the named wrong boards, the
# distractor reasons, the retrieval source. Those sentences EXIST to quote what a student got
# wrong, so the boundary scans do not run inside them. Everything a student is asked to work —
# stem, text, latex, choices, answer, why, prompt, math, items2, rows, gloss, hint — is scanned.
TEACHER_PROSE = {"note", "note_q", "wrong", "errors", "source", "warmup_note"}


def boundcheck_str(s, where, code):
    """Ruling 13 for Unit 4: addition and subtraction in scientific notation keep the two
    exponents within 2 of each other; radicands are perfect squares up to 225 and perfect cubes
    from -125 to 125. A block that shows a wider gap or a stretch radicand on purpose carries
    not_gap=True or not_bound=True and says why in its note."""
    out = []
    terms = list(_SCI_TERM.finditer(s))
    for a, b in zip(terms, terms[1:]):
        if _GAP_JUNK.sub("", s[a.end():b.start()]) in _ADDSUB:
            e1, e2 = _sci_exp(a), _sci_exp(b)
            if abs(e1 - e2) > GAP_MAX:
                out.append(f"{code} {where}: adding or subtracting 10^{e1} and 10^{e2} — a gap of "
                           f"{abs(e1 - e2)}, and MA.8.NSO.1.5 limits it to {GAP_MAX} "
                           f"(tag the block not_gap=True if the item is about the boundary)")
    rads = [(int(m.group(1) or 2), m.group(2)) for m in _SQRT_TEX.finditer(s)]
    rads += [(2 if m.group(0)[0] == "\u221a" else 3, m.group(1) or m.group(2))
             for m in _SQRT_UNI.finditer(s)]
    for deg, tex in rads:
        if deg not in (2, 3):
            out.append(f"{code} {where}: a {deg}th root — MA.8.NSO.1.7 is square and cube roots only")
            continue
        n = _radicand_value(tex)
        if n is None:
            out.append(f"{code} {where}: radicand {tex!r} is not plain arithmetic on integers, so "
                       f"its bound could not be checked (work it by hand, then tag not_bound=True)")
        elif not _rad_ok(n, deg):
            name = "perfect squares up to %d" % SQ_MAX if deg == 2 else \
                   "perfect cubes from %d to %d" % (CUBE_LO, CUBE_HI)
            root = "\u221a" if deg == 2 else "cube root of "
            out.append(f"{code} {where}: {root}{n} — MA.8.NSO.1.7 is {name} "
                       f"(tag not_bound=True if deliberate, and say why in the note)")
    return out


def capcheck_lesson(L):
    """Ruling 13 caps for this unit: integer exponents only; rational bases; sci-notation
    coefficients in [1,10). Walks every item (and every notes/example block) of the spec;
    a block that deliberately shows a coefficient outside [1,10) — because it is ABOUT the
    constraint — carries not_sci=True."""
    out = []
    blob = json.dumps(L, ensure_ascii=False)
    if re.search(r"\^\{\s*\\frac", blob) or re.search(r"\^\{\s*\d+/\d+", blob):
        out.append(f"{L['code']}: fractional exponent found")

    def scan(obj, where, skip=()):
        if isinstance(obj, dict):
            skip = tuple(skip) + tuple(f for f in ("not_sci", "not_gap", "not_bound") if obj.get(f))
            for k, v in obj.items():
                scan(v, f"{where}.{k}", skip)
        elif isinstance(obj, (list, tuple)):
            for i, v in enumerate(obj):
                scan(v, f"{where}[{i}]", skip)
        elif isinstance(obj, str):
            if "not_sci" not in skip:
                for m in _SCI.finditer(obj):
                    v = float(m.group(1))
                    if not (1 <= v < 10):
                        out.append(f"{L['code']} {where}: scientific-notation coefficient {v} outside [1,10) (tag the block not_sci=True if deliberate)")
            key = where.rsplit(".", 1)[-1].split("[")[0]
            for f in ([] if key in TEACHER_PROSE else boundcheck_str(obj, where, L["code"])):
                if ("not_gap" in skip and "a gap of" in f) or ("not_bound" in skip and "MA.8.NSO.1.7" in f) \
                        or ("not_bound" in skip and "could not be checked" in f):
                    continue
                out.append(f)
    for grp in ("warmup", "notes", "examples", "whiteboard", "bank", "additional", "independent", "vocab"):
        scan(L.get(grp), grp)
    # The teacher's edition is prose ABOUT the textbook and about wrong boards: naming the book's
    # own "45 × 10⁶", the guide's "leaving 12 × 10⁹" or the Dotson task's √200 is the point of the
    # sentence, so no scan runs there. Every value the TE prints as an answer comes from an item
    # that was scanned in its own group.
    scan(L.get("te"), "te", skip=("not_sci", "not_gap", "not_bound"))
    return out


def docscan_text(text, surface):
    """Standing rulings on student paper: no benchmark codes, no calculator line, no 'homework',
    no partner/group work."""
    out = []
    if surface == "student":
        if re.search(r"MA\.\d+\.[A-Z]+\.\d+\.\d+", text):
            out.append("benchmark code on student paper")
        if re.search(r"\bcalculator", text, re.I):
            out.append("calculator line on student paper")
        if re.search(r"\bhomework\b", text, re.I):
            out.append("'homework' on student paper")
    if re.search(r"\bpartner|\bgroup work|\bwith your partner|\bteam", text, re.I):
        out.append("partner/group work")
    return out


# ---------------------------------------------------------------- builders
def _fmt_q(doc, it, number=None, key=False, points=None):
    parts = None
    if it.get("parts"):
        parts = [(p["label"], p["stem"], p.get("answer"), p.get("why"), p.get("space")) for p in it["parts"]]
    doc.question(it["stem"], answer=it.get("answer"), reasoning=it.get("why"), space=it.get("space", 1.0),
                 parts=parts, choices=it.get("choices"), choice_answer=it.get("correct"), number=number,
                 lines=it.get("lines"), points=points)


def _label(L):
    """'Lesson 4' for book lessons; threads carry their own label ('Thread A · Day 1')."""
    return L.get("label") or f"Lesson {L['lesson_no']}"


def build_bank(L, items, kind, key, outdir):
    """kind: 'Question Bank' or 'Question Bank - Additional'."""
    code = L["code"]
    eyebrow = f"{COURSE}  ·  Unit {L['unit']}  ·  {_label(L)}"
    sub = f"{kind} {code}"
    doc = Doc(eyebrow, L["title"], sub, key=key)
    if kind == "Independent Set":
        doc.instruction("Six questions, on your own, in silence. Show the step that does the work.")
    else:
        doc.instruction("Show your work. Circle your final answer.")
    n = 0
    for it in items:
        if it.get("heading"):
            doc.heading(it["heading"])
            continue
        if it.get("table"):
            doc.table(*it["table"])
            continue
        n += 1
        _fmt_q(doc, it, key=key)
    name = f"A7 {code}  {kind}{' Key' if key else ''}.docx"
    path = os.path.join(outdir, name)
    doc.save(path)
    return path


def build_deck(L, outdir):
    code = L["code"]
    footer = f"{COURSE} · Unit {L['unit']} · {_label(L)} — {L['title']}"
    D = Deck(COURSE, L["unit"], _label(L), L["title"], footer)
    D.title_slide(L["benchmark"], L["target"], L["yesterday"], L["today"], minutes=1,
                  note=L.get("title_note", "Post the learning target. Say the 'today' line and nothing else yet."))
    # ---- warm-up: four retrieval questions, one slide; reveal slide after
    wu = L["warmup"]
    D.section("Warm-Up", "On your own. Four minutes. No notes.", 4, L.get("warmup_note", "Spaced retrieval. Two minutes silent, then reveal. One sentence of reteach per question at most."), "warmup")
    D.cursor = 1.95
    for i, q in enumerate(wu):
        D.math_row(f"{i + 1}.   " + q["stem"], surface="slide", gap=0.22, size=23, align="left", x=LM + 1.2)
    D.section("Warm-Up", "Answers.", 1, "Reveal. Ask for the band each question came from only if time allows.", "warmup")
    D.cursor = 1.95
    for i, q in enumerate(wu):
        y0 = D.cursor
        tw, hh = D._mixed(f"{i + 1}.   " + q["stem"], LM + 1.2, y0, "slide", 23, INK)
        aw = D.measure(q["answer"], "slide", 23, bold=True)
        if LM + 1.2 + tw + 0.6 + aw <= LM + CW:
            D._mixed(q["answer"], LM + 1.2 + tw + 0.6, y0, "slide", 23, RED, True)
            D.cursor = y0 + hh + 0.22
        else:
            _, h2 = D._mixed(q["answer"], LM + 2.0, y0 + hh + 0.05, "slide", 23, RED, True)
            D.cursor = y0 + hh + 0.05 + h2 + 0.22
    # ---- notes
    for ni, note in enumerate(L["notes"]):
        D.section("Notes", note.get("sub", ""), note["min"], note["note"], "notes")
        D.head(note["head"], note.get("numeral"))
        if note.get("items"):
            D.items(note["items"], size=note.get("size", 23), panel=note.get("panel", False), letters=note.get("letters", True))
        if note.get("table"):
            D.table(*note["table"], size=note.get("tsize", 16))
        if note.get("math"):
            for mrow in note["math"]:
                D.math_row(mrow, surface="slidemid", gap=0.3)
        if note.get("text"):
            for t in note["text"]:
                D.text(t, 22)
        if note.get("items2"):
            D.items(note["items2"], size=note.get("size", 23), letters=note.get("letters", True), start=len(note.get("items", [])))
    # ---- examples: question slide, worked slide(s), your turn q + reveal
    for ex in L["examples"]:
        D.section(ex["title"], ex.get("sub", ""), ex["min_q"], ex["note_q"], "example")
        D.cursor = 2.3
        for row in ex["prompt"]:
            D.math_row(row, surface="slidemid", gap=0.35) if "$" in row else D.text(row, 24, align="center")
        if ex.get("ask"):
            D.cursor += 0.2
            D.text(ex["ask"], 24, bold=True, align="center")
        for wi, w in enumerate(ex["worked"]):
            D.section(ex["title"], w.get("sub", "Worked."), w.get("min", 2), w["note"], "example")
            D.cursor = 2.1
            for row in w["rows"]:
                if isinstance(row, tuple):
                    latex, gloss = row
                    y0 = D.cursor
                    wdt, hgt = D.math(latex, "slidemid", align="left", x=2.0)
                    gx = 2.0 + wdt + 0.5
                    D._text(gx, y0 + (hgt - 0.5) / 2, min(7.0, LM + CW - gx), 0.55, gloss, 21, italic=True, color=GRAY, anchor="middle")
                    D.cursor = y0 + hgt + 0.3
                else:
                    D.text(row, 23)
            if w.get("answer"):
                D.answer_line(w["answer"], y=max(D.cursor + 0.2, 5.0))
            if w.get("items"):
                D.items(w["items"], size=23)
        yt = ex.get("your_turn")
        if yt:
            D.section("Your Turn", "Same steps, your numbers. Boards up when done.", yt.get("min", 2), yt["note"], "yourturn")
            D.cursor = 2.4
            for row in yt["prompt"]:
                D.math_row(row, surface="slidebig", gap=0.35) if "$" in row else D.text(row, 24, align="center")
            D.section("Your Turn", "Answer.", 1, "Reveal; name what a wrong board most likely did (see the note above).", "yourturn")
            D.cursor = 2.4
            for row in yt["prompt"]:
                D.math_row(row, surface="slidebig", gap=0.35) if "$" in row else D.text(row, 24, align="center")
            if yt.get("gloss"):
                D.text(yt["gloss"], 24, color=GRAY, align="center")
            if yt.get("answer_latex"):
                D.answer_math(yt["answer_latex"], y=max(D.cursor + 0.2, 4.9))
            else:
                D.answer_line(yt["answer"], y=max(D.cursor + 0.2, 5.0))
    # ---- whiteboards: 9 questions, question + reveal each
    wb = L["whiteboard"]
    assert len(wb) == 9, f"{code}: whiteboard round must be nine questions, got {len(wb)}"
    for qi, q in enumerate(wb):
        last = qi == 8
        title = f"Whiteboards   ·   Question {qi + 1} of 9"
        subq = "Take your time. Boards up when you have written it." if last else "Boards up on three."
        D.section(title, subq, 0, q["note"], "wb")
        D.cursor = 2.4
        _wb_body(D, q, reveal=False)
        D.section(title, "Answer.", 0, q.get("note_a", "Reveal. Scan the back row first; question the blank boards before the wrong ones."), "wb")
        D.cursor = 2.3
        _wb_body(D, q, reveal=True)
    # ---- independent set (ruling 21), then IXL
    D.independent(INDEP_MIN)
    D.ixl(L["ixl"], IXL_MIN)
    name = f"A7 {code}  Slides.pptx"
    path = os.path.join(outdir, name)
    D.save(path)
    return path


IXL_MIN = 5
INDEP_MIN = 6            # ruling 21: six questions, six minutes, after the boards


def _wb_body(D, q, reveal):
    kind = q.get("kind", "free")
    if q.get("latex"):
        D.math(q["latex"], "slidebig")
    for row in q.get("text", []):
        if "$" in row:
            D.math_row(row, surface="slidemid", gap=0.3, size=26)
        else:
            D.text(row, 26 if len(row) < 60 else 23, align="center")
    if kind == "mc":
        D.cursor += 0.1
        D.choices(q["choices"], correct=(q["correct"] if reveal else None))
    if not reveal:
        y = max(D.cursor + 0.15, 4.75)
        if kind == "written":
            D._text(0.85, y, 11.6, 0.5, "Write your answer in sentences.", 26, bold=True, align="center")
            D._text(0.85, y + 0.53, 11.6, 0.4, q.get("hint", "This one is written work. Say why."), 19, italic=True, color=GRAY, align="center")
        else:
            D._text(0.85, y, 11.6, 0.5, "Answer it.", 26, bold=True, align="center")
            if q.get("hint"):
                D._text(0.85, y + 0.53, 11.6, 0.4, q["hint"], 19, italic=True, color=GRAY, align="center")
    else:
        if q.get("gloss"):
            D._text(2.0, D.cursor + 0.05, 9.3, 0.6, q["gloss"], 24, color=GRAY, align="center")
            D.cursor += 0.7
        y = max(D.cursor + 0.15, 5.1)
        if q.get("answer_latex"):
            D.answer_math(q["answer_latex"], y=y)
        else:
            D.answer_line(q["answer"], y=y)


def board_text(q):
    """The board's question as prose: its latex and its text lines, in the order they appear."""
    if q.get("qtext"):
        return q["qtext"]
    bits = []
    if q.get("latex"):
        bits.append("$" + q["latex"] + "$")
    bits += list(q.get("text", []))
    return "  ".join(bits)


def _first_sentence(t):
    t = (t or "").split("\n")[0].strip()
    for stop in (". ", "? ", "! "):
        if stop in t:
            return t[:t.index(stop) + 1].strip()
    return t


def _slide_line(s):
    """Ruling 26: one line per slide, in the voice of someone standing beside the teacher.
    An OFF: line IS the line (the phrase 'OFF THE SLIDE, YOURS TO SAY' retires)."""
    note = s.get("note") or ""
    for line in note.split("\n"):
        if line.startswith("OFF:"):
            return line[4:].strip().strip("'\u2018\u2019")
    return _first_sentence(note)


SPLIT_MOVE = ("Split (no option near two-thirds)? Sixty seconds, convince your neighbour, "
              "re-vote, then reveal.")


def _locator(ev):
    """An MTR's evidence reads '<where> — <what happens there>'. Page 1 of the Teacher Edition
    carries only the <where>; the whole sentence is section 3 of the Lesson Plan (ruling 25)."""
    return ev.split(" — ")[0].strip() if " — " in ev else _first_sentence(ev)


def build_te(L, deck_path, outdir):
    """Ruling 26: four pages or fewer, read in twenty minutes. Page 1 is the period; then one
    line per slide; then Misconceptions to Watch. No keys, no bank commentary, no paragraphs."""
    code = L["code"]
    side_path = deck_path[:-5] + ".notes.json"
    rows, wb_min, side, blocks = tekit.plan_from_sidecar(side_path)
    eyebrow = f"{COURSE}  ·  Unit {L['unit']}  ·  {_label(L)}"
    te = TE(eyebrow, L["title"])
    T = L["te"]

    # ---------------- page 1: the period, and nothing else
    te.h1("The Period")
    te.label(L["benchmark"], L["benchmark_text"])
    notes = dict(T.get("standard_notes", []))
    must = T.get("must") or notes.get("Clarification") or notes.get("Benchmark") or ""
    must_not = T.get("must_not") or notes.get("Boundary") or ""
    if must:
        te.label("Must", must)
    if must_not:
        te.label("Must not", must_not)
    te.label("Target", L["target"])
    mtr = L.get("mtr") or []
    if mtr:
        te.label("MTR", "   ·   ".join(f"**{m}** — {_locator(ev)}" for m, ev in mtr))
    tekit.timing_table(te, rows)
    te.h2("Say these three things out loud today")
    say = T.get("say") or [x for x in (T.get("lives"), *(T.get("read_first") or [])) if x][:3]
    for i, line in enumerate(say[:3]):
        p = te.para("", before=1, after=4, indent=360, hanging=360)
        te._run(p, f"{i + 1}.  ", 10.5, bold=True)
        te.rich(p, line, size=10.5)
    te.d.add_page_break()

    # ---------------- one line per slide, in slide order
    te.h1("Slide by Slide")
    wb_seen = 0
    i = 0
    while i < len(side):
        s = side[i]
        if s["kind"] == "wb":
            # a board is two slides (question, reveal); one line covers both
            q = L["whiteboard"][wb_seen]
            rev = side[i + 1] if i + 1 < len(side) and side[i + 1]["kind"] == "wb" else s
            qt = board_text(q)
            ans = q.get("answer") or ("$" + q.get("answer_latex", "") + "$")
            errs = q.get("errors") or {}
            wrong = "; ".join(f"({k}) {v}" for k, v in errs.items()) if errs else q.get("wrong", "")
            p = te.para("", before=1, after=3, indent=470, hanging=470)
            te._run(p, f"{s['n']}\u2013{rev['n']}.  ", 10.5, bold=True)
            te._run(p, f"Board {wb_seen + 1}.  ", 10.5, bold=True)
            te.rich(p, qt + "  \u2192  ", size=10.5)
            te.rich(p, ans, size=10.5, bold=True, italic=True, color=RED)
            if q.get("unneeded"):
                te.rich(p, f"   The {q['unneeded']} is not needed.", size=10, italic=True, color=GRAY)
            if wrong:
                te.rich(p, "   " + wrong, size=9.5, italic=True, color=GRAY)
            if q.get("kind") == "mc":
                te.rich(p, "   " + SPLIT_MOVE, size=9.5, italic=True, color=GRAY)
            wb_seen += 1
            i += 2
            continue
        line = _slide_line(s)
        if s["kind"] == "warmup" and "Answers" in (s.get("sub") or ""):
            line = "Reveal.  " + "   ".join(f"{k + 1}. {w['answer']}" for k, w in enumerate(L["warmup"]))
        p = te.para("", before=1, after=3, indent=470, hanging=470)
        te._run(p, f"{s['n']}.  ", 10.5, bold=True)
        head = s["title"] + (f" \u2014 {s['sub']}" if s.get("sub") else "")
        te._run(p, head + ".  ", 10.5, bold=True)
        te.rich(p, line, size=10.5)
        i += 1

    # ---------------- misconceptions, tied to the board that surfaces each
    te.h1("Misconceptions to Watch")
    for i, q in enumerate(L["whiteboard"]):
        errs = q.get("errors") or {}
        src = "; ".join(v for v in errs.values()) if errs else q.get("wrong", "")
        if not src:
            continue
        first = src.split(";")[0].strip()
        p = te.para("", before=0, after=2, indent=360, hanging=360)
        te._run(p, f"Board {i + 1}.  ", 10, bold=True)
        te.rich(p, first, size=10)
    if T.get("materials"):
        te.label("Materials", T["materials"], after=2)
    name = f"A7 {code}  Teacher Edition.docx"
    path = os.path.join(outdir, name)
    te.save(path)
    return path


def _ruling_checks(L):
    out = []
    if not L.get("mtr"):
        out.append(f"{L['code']}: ruling 25 — no `mtr`; name the two or three MTRs this lesson exercises, each with its evidence")
    ind = L.get("independent") or []
    n_ind = len([i for i in ind if not i.get("heading")])
    if n_ind != 6:
        out.append(f"{L['code']}: ruling 21 — the independent set has {n_ind} questions, needs exactly 6")
    unneeded = [i for i, q in enumerate(L["whiteboard"]) if q.get("unneeded")]
    if len(unneeded) != 1:
        out.append(f"{L['code']}: ruling 22 — {len(unneeded)} boards carry a figure the question does not need, needs exactly 1"
                   + (f" (boards {[u + 1 for u in unneeded]})" if unneeded else ""))
    if not (L["te"].get("say") and len(L["te"]["say"]) == 3):
        out.append(f"{L['code']}: ruling 26 — te.say must be the three sentences to say out loud today")
    return out


def build_lesson(L, outdir):
    os.makedirs(outdir, exist_ok=True)
    findings, n = mathcheck_lesson(L)
    d = distractorcheck_lesson(L)
    c = capcheck_lesson(L)
    r = _ruling_checks(L)
    print(f"mathcheck {L['code']}: {n} items checked, {len(findings)} findings")
    for f in findings + d + c + r:
        print("  ", f)
    if findings or d or c or r:
        raise SystemExit(f"{L['code']}: build refused")
    out = {}
    out["bank"] = build_bank(L, L["bank"], "Question Bank", False, outdir)
    out["bank_key"] = build_bank(L, L["bank"], "Question Bank", True, outdir)
    out["add"] = build_bank(L, L["additional"], "Question Bank - Additional", False, outdir)
    out["add_key"] = build_bank(L, L["additional"], "Question Bank - Additional", True, outdir)
    out["indep"] = build_bank(L, L["independent"], "Independent Set", False, outdir)
    out["indep_key"] = build_bank(L, L["independent"], "Independent Set", True, outdir)
    out["deck"] = build_deck(L, outdir)
    out["te"] = build_te(L, out["deck"], outdir)
    out["plan"] = plankit.build_plan(L, out["deck"], outdir, COURSE, _label(L))
    return out
