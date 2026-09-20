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
from .tekit import TE

COURSE = "Grade 7 Accelerated"


# ---------------------------------------------------------------- mathcheck
def _ev(expr):
    env = {"F": F, "sqrt": sp.sqrt, "Integer": Integer, "sp": sp, "Rational": F, "nsimplify": nsimplify,
           "pi": sp.pi, "Abs": sp.Abs, "abs": sp.Abs, "N": sp.N, "floor": sp.floor, "Float": sp.Float}
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
    for grp in ("warmup", "whiteboard", "bank", "additional"):
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
    for grp in ("whiteboard", "bank", "additional", "warmup"):
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
    return out


def capcheck_lesson(L):
    """Ruling 13 caps for this unit: integer exponents only; rational bases; sci-notation
    coefficients in [1,10). Scans every LaTeX/text in the spec."""
    out = []
    blob = json.dumps(L)
    # fractional exponent like ^{1/2} or ^{\frac
    if re.search(r"\^\{\s*\\frac", blob) or re.search(r"\^\{\s*\d+/\d+", blob):
        out.append(f"{L['code']}: fractional exponent found")
    for mcoef in re.finditer(r"(\d+(?:\.\d+)?)\s*\\times\s*10\^", blob):
        v = float(mcoef.group(1))
        if not (1 <= v < 10):
            # allowed only when the item is ABOUT the constraint
            ctx = blob[max(0, mcoef.start() - 200):mcoef.start()]
            if "not_sci" not in ctx and "notsci" not in ctx:
                out.append(f"{L['code']}: scientific-notation coefficient {v} outside [1,10) (tag the item not_sci if deliberate)")
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


def build_bank(L, items, kind, key, outdir):
    """kind: 'Question Bank' or 'Question Bank - Additional'."""
    code = L["code"]
    eyebrow = f"{COURSE}  ·  Unit {L['unit']}  ·  Lesson {L['lesson_no']}"
    sub = f"{kind} {code}"
    doc = Doc(eyebrow, L["title"], sub, key=key)
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
    footer = f"{COURSE} · Unit {L['unit']} · Lesson {L['lesson_no']} — {L['title']}"
    D = Deck(COURSE, L["unit"], f"Lesson {L['lesson_no']}", L["title"], footer)
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
    # ---- IXL
    D.ixl(L["ixl"], IXL_MIN)
    name = f"A7 {code}  Slides.pptx"
    path = os.path.join(outdir, name)
    D.save(path)
    return path


IXL_MIN = 5


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


def build_te(L, deck_path, outdir):
    code = L["code"]
    side_path = deck_path[:-5] + ".notes.json"
    rows, wb_min, side, blocks = tekit.plan_from_sidecar(side_path)
    eyebrow = f"{COURSE}  ·  Unit {L['unit']}  ·  Lesson {L['lesson_no']}"
    te = TE(eyebrow, L["title"])
    T = L["te"]
    te.h1("Read This First")
    for para in T["read_first"]:
        te.body(para)
    te.h1("Standard and Targets")
    te.label(L["benchmark"], L["benchmark_text"])
    for lab, txt in T.get("standard_notes", []):
        te.label(lab, txt)
    te.label("Learning target", L["target"])
    te.label("Essential question", L["essential"])
    te.label("Building on", L["building_on"])
    te.label("Working toward", L["working_toward"])
    if T.get("sits"):
        te.label("Where this sits in the course", T["sits"])
    te.h1("Lesson at a Glance")
    te.body(f"Windy Hill periods run **{tekit.PERIOD} minutes**. The whiteboard round takes the remainder after the taught blocks — **{wb_min} minutes** in this lesson — and IXL takes the last {IXL_MIN}. Slide numbers below are read from the deck when this edition is built.")
    tekit.timing_table(te, rows)
    te.label("Materials", T.get("materials", "Whiteboards and markers. Calculators are allowed on everything."))
    te.label("Where the lesson lives", T["lives"])
    te.body("**No partner or group work anywhere in this lesson.** Every Math Nation exploration this lesson draws on was written for pairs; here the same tables are worked from the front and on individual boards.")
    te.h1("Vocabulary")
    te.vocab(L["vocab"])
    te.h1("Warm-Up — spaced retrieval")
    te.body("Four questions, two minutes silent, then the reveal. No reteach longer than one sentence per question.")
    for i, q in enumerate(L["warmup"]):
        p = te.para("", before=0, after=4, indent=360, hanging=360)
        te._run(p, f"{i + 1}.  ", 10.5, bold=True); te.rich(p, q["stem"] + "    ", size=10.5)
        te.rich(p, q["answer"], size=10.5, bold=True, italic=True, color=RED)
        p = te.para("", before=0, after=6, indent=360)
        te._run(p, "retrieves: ", 9.5, italic=True, color=GRAY); te.rich(p, f"{q['band']} — {q['source']}", size=9.5, italic=True, color=GRAY)
    te.h1("Slide-by-Slide Teaching Notes")
    for b in blocks:
        for s in b["subs"]:
            mins = f"{s['min']} min" if s["kind"] != "wb" else ""
            if s["kind"] == "wb" and s is b["subs"][0]:
                mins = f"{wb_min} min for the round"
            te.h2(f"Slide {s['n']}.  {s['title']}" + (f" — {s['sub']}" if s["sub"] and s["kind"] not in ("wb",) else ""), mins)
            if s["note"]:
                for line in s["note"].split("\n"):
                    if line.startswith("OFF:"):
                        te.off_slide(line[4:].strip())
                    else:
                        te.bullets([line])
    te.h1("The Whiteboard Round — what each board tells you")
    te.body("Nine questions, one at a time, each with its reveal. Boards down until the cue, all up together, scan the back row first, question the blank boards before the wrong ones. Question 9 is written work. Every wrong option on a multiple-choice question is a named error; the benchmark it comes from is cited.")
    data = [["#", "Question", "Answer", "What a wrong board says"]]
    for i, q in enumerate(L["whiteboard"]):
        qt = q.get("qtext") or " ".join(q.get("text", [])) or ("$" + q["latex"] + "$")
        ans = q.get("answer") or ("$" + q["answer_latex"] + "$")
        errs = q.get("errors") or {}
        et = "; ".join(f"({k}) {v}" for k, v in errs.items()) if errs else q.get("wrong", "")
        data.append([str(i + 1), qt, {"text": ans, "bold": True, "italic": True, "color": RED}, et])
    te.table([400, 3300, 1900, 3760], data, header=True, size=9.5)
    te.h1("Question Bank — variation and answers")
    te.label("Variation.", T["variation"])
    te.body("The bank and its Additional sheet are posted, never assigned; they feed the quizzes. Answers below are the same values the keys print — both come from one source.")
    _answers_list(te, L["bank"], "Question Bank")
    _answers_list(te, L["additional"], "Question Bank — Additional")
    te.h1("What the audit against Math Nation found")
    te.bullets(T["audit"])
    if T.get("changes"):
        te.h2("What changed from the book")
        te.bullets(T["changes"])
    name = f"A7 {code}  Teacher Edition.docx"
    path = os.path.join(outdir, name)
    te.save(path)
    return path


def _answers_list(te, items, title):
    te.h2(title)
    n = 0
    for it in items:
        if it.get("heading") or it.get("table"):
            continue
        n += 1
        p = te.para("", before=0, after=3, indent=360, hanging=360)
        te._run(p, f"{n}.  ", 10, bold=True)
        if it.get("parts"):
            te.rich(p, "  ".join(f"({pp['label']}) " + (pp.get('answer') or '') for pp in it["parts"]), size=10, bold=True, italic=True, color=RED)
        elif it.get("choices"):
            corr = it["correct"] if isinstance(it["correct"], (list, tuple)) else [it["correct"]]
            te.rich(p, ", ".join(chr(65 + c) for c in corr) + "  " + (it.get("answer") or ""), size=10, bold=True, italic=True, color=RED)
        else:
            te.rich(p, it.get("answer") or "", size=10, bold=True, italic=True, color=RED)


def build_lesson(L, outdir):
    os.makedirs(outdir, exist_ok=True)
    findings, n = mathcheck_lesson(L)
    d = distractorcheck_lesson(L)
    c = capcheck_lesson(L)
    print(f"mathcheck {L['code']}: {n} items checked, {len(findings)} findings")
    for f in findings + d + c:
        print("  ", f)
    if findings or d or c:
        raise SystemExit(f"{L['code']}: build refused")
    out = {}
    out["bank"] = build_bank(L, L["bank"], "Question Bank", False, outdir)
    out["bank_key"] = build_bank(L, L["bank"], "Question Bank", True, outdir)
    out["add"] = build_bank(L, L["additional"], "Question Bank - Additional", False, outdir)
    out["add_key"] = build_bank(L, L["additional"], "Question Bank - Additional", True, outdir)
    out["deck"] = build_deck(L, outdir)
    out["te"] = build_te(L, out["deck"], outdir)
    return out
