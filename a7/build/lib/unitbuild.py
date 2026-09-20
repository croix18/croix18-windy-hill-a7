"""Unit-wide documents from one spec: Reference Sheet, Unit Review (+ Key), Unit Assessment (+ Key).
Every item on the review and the assessment goes through the same mathcheck / distractorcheck /
capcheck as the lesson items; the assessment's point ledger is asserted against the declared
total and the per-benchmark Score Tracker at build time.
"""
import os
from .dockit import Doc, GRAY, RED
from .lessonbuild import mathcheck_item, _flatten, distractorcheck_lesson, capcheck_lesson, COURSE, _fmt_q

UNSCORED_NOTE = ("HOW TO USE THIS.   This review covers every learning target from the unit — more than the "
                 "assessment does. Work it in parts. If you miss two or more in a part, that part is where to "
                 "spend your study time. The reference sheet has everything you need for each part.")


# ---------------------------------------------------------------- checks
def _items(groups):
    out = []
    for g in groups:
        for it in g:
            if it.get("heading") or it.get("table_only"):
                continue
            out.append(it)
    return out


def check_unit(U):
    findings = []
    n = 0
    review_items = _items([p["items"] for p in U["review"]])
    exam_items = _items([sec["items"] for sec in U["assessment"]["sections"]])
    for label, items in (("review", review_items), ("assessment", exam_items)):
        for i, it in enumerate(items):
            for f in _flatten(it):
                n += 1
                findings += mathcheck_item(f, f"U{U['unit']} {label}[{i}]")
    pseudo = {"code": f"{U['unit']}.U", "bank": review_items, "additional": exam_items,
              "te": {"reference": U["reference"]}}
    findings += distractorcheck_lesson(pseudo)
    findings += capcheck_lesson(pseudo)
    return findings, n


# ---------------------------------------------------------------- reference sheet
def build_reference(U, outdir):
    eyebrow = f"{COURSE}  ·  Unit {U['unit']}"
    doc = Doc(eyebrow, "Reference Sheet", f"{U['title']}  —  keep this in your binder")
    doc.instruction(U["reference_intro"])
    for sec in U["reference"]:
        if sec.get("not_sci"):
            pass
        doc.section(sec["title"], sec.get("right", ""))
        for block in sec["blocks"]:
            if isinstance(block, str):
                doc.para(block, before=3, after=4)
            elif block.get("table"):
                widths, rows = block["table"]
                doc.table(widths, rows, header=block.get("header", True), size=block.get("size", 10.5),
                          align_center=True)
            elif block.get("bullets"):
                for b in block["bullets"]:
                    doc.para("•   " + b, before=1, after=2, indent=360, hanging=360)
            elif block.get("vocab"):
                for term, dfn in block["vocab"]:
                    doc.para(f"__{term}__   —   {dfn}", before=2, after=3, indent=360, hanging=360)
    name = f"A7 {U['unit']}  Reference Sheet.docx"
    path = os.path.join(outdir, name)
    doc.save(path)
    return path


# ---------------------------------------------------------------- unit review
def build_review(U, outdir, key):
    eyebrow = f"{COURSE}  ·  Unit {U['unit']}"
    doc = Doc(eyebrow, f"Unit {U['unit']} Review", U["title"], key=key)
    doc.instruction("Show your work. Circle your final answer.")
    doc.para(UNSCORED_NOTE, size=9.5, italic=True, color=GRAY, before=0, after=8)
    for part in U["review"]:
        n_q = len([i for i in part["items"] if not i.get("heading")])
        right = f"{part['lessons']}   ·   {n_q} questions"
        if key:  # benchmark codes never print on a student page
            right = f"{part['lessons']}   ·   {part['benchmark']}   ·   {n_q} questions"
        doc.section(f"PART {part['letter']}.   {part['title']}", right)
        for it in part["items"]:
            if it.get("heading"):
                doc.heading(it["heading"])
                continue
            it2 = dict(it)
            if key and it.get("key_stem"):
                it2["stem"] = it["key_stem"]
            _fmt_q(doc, it2, key=key)
    name = f"A7 {U['unit']}  Unit Review{' Key' if key else ''}.docx"
    path = os.path.join(outdir, name)
    doc.save(path)
    return path


# ---------------------------------------------------------------- unit assessment
def _points(it):
    if it.get("parts"):
        return [1] * len(it["parts"])
    return 1


def assessment_ledger(U):
    """Ruling 27: ONE paper, numbered straight through, no day sections.
    Returns (total, per_benchmark {bm: (question numbers, points)}, per_section, transfer_qs)."""
    total = 0; n = 0
    per_bm = {}; per_sec = []; transfer = []
    for sec in U["assessment"]["sections"]:
        spts = 0
        for it in sec["items"]:
            if it.get("heading"):
                continue
            n += 1
            if it.get("transfer"):
                transfer.append(n)
            p = _points(it); v = sum(p) if isinstance(p, list) else p
            spts += v
            qs, pts = per_bm.setdefault(sec["benchmark"], ([], 0))
            qs.append(n); per_bm[sec["benchmark"]] = (qs, pts + v)
        per_sec.append((sec["title"], spts)); total += spts
    return total, per_bm, per_sec, transfer


CONTINUES = ("This assessment runs over two class periods. Stop when the period ends; "
             "you will continue from where you stopped.")
FOLLOW_THROUGH_STUDENT = ("If an earlier part is wrong, a later part still earns its point when the right "
                          "operation is applied to your own earlier answer — but only if that work is on the page.")
TRANSFER_FLAG = "TRANSFER ITEM — not on the practice test. Same benchmark, a surface nobody rehearsed."


def build_assessment(U, outdir, key):
    A = U["assessment"]
    total, per_bm, per_sec, transfer = assessment_ledger(U)
    assert total == A["total"], f"assessment ledger {total} != declared {A['total']}"
    for bm, (qs, pts) in per_bm.items():
        assert A["tracker"][bm] == pts, f"tracker {bm}: declared {A['tracker'][bm]}, ledger {pts}"
    assert sum(A["tracker"].values()) == total
    # Ruling 18: exactly two transfer items on every unit assessment.
    assert len(transfer) == 2, f"ruling 18: {len(transfer)} transfer items, need exactly 2 (questions {transfer})"
    eyebrow = f"{COURSE}  ·  Unit {U['unit']}  ·  Assessment"
    sub = f"{total} points" + ("  ·  two periods; students continue the same paper" if key else "")
    doc = Doc(eyebrow, U["title"], sub, key=key)
    doc.instruction("Show your work. Circle your final answer.")
    doc.para(CONTINUES, size=10, bold=True, before=0, after=3)
    doc.para(FOLLOW_THROUGH_STUDENT, size=9.5, italic=True, color=GRAY, before=0, after=8)
    si = 0; n = 0
    for sec in A["sections"]:
        si += 1
        doc.section(f"{si}.  {sec['title']}", f"{per_sec[si - 1][1]} points")
        for it in sec["items"]:
            if it.get("heading"):
                doc.heading(it["heading"]); continue
            n += 1
            it2 = dict(it)
            if key and it.get("key_stem"):
                it2["stem"] = it["key_stem"]
            if key and it.get("transfer"):
                it2["why"] = (it.get("why", "") + "  " if it.get("why") else "") + "**" + TRANSFER_FLAG + "**"
            _fmt_q(doc, it2, key=key, points=_points(it), number=n)
    if key:
        doc.section("Score Tracker")
        doc.para(f"{total} points, one point per lettered part.  " + "  ·  ".join(f"Section {i + 1} — {p}" for i, (t, p) in enumerate(per_sec)),
                 size=10, before=2, after=6)
        rows = [["Benchmark", "Questions", "Possible", "Earned"]]
        for bm in A["tracker_order"]:
            qs, pts = per_bm[bm]
            rows.append([bm, ",  ".join(str(q) for q in qs), str(pts), ""])
        rows.append([{"text": "Total", "bold": True}, "", {"text": str(total), "bold": True}, ""])
        doc.table([2600, 3600, 1500, 1660], rows, header=True, size=10.5)
        doc.para(A["follow_through"], size=9.5, italic=True, color=GRAY, before=6, after=4)
        doc.para(f"Transfer items (ruling 18): questions {transfer[0]} and {transfer[1]}. Neither surface appears on the "
                 f"review or in any question bank.", size=9.5, italic=True, color=GRAY, before=2, after=4)
    name = f"A7 {U['unit']}  Unit Assessment{' Key' if key else ''}.docx"
    path = os.path.join(outdir, name)
    doc.save(path)
    return path


def build_unit(U, outdir):
    findings, n = check_unit(U)
    print(f"unitcheck U{U['unit']}: {n} items checked, {len(findings)} findings")
    for f in findings:
        print("  ", f)
    if findings:
        raise SystemExit("unit documents: build refused")
    out = {}
    out["reference"] = build_reference(U, outdir)
    out["review"] = build_review(U, outdir, key=False)
    out["review_key"] = build_review(U, outdir, key=True)
    out["exam"] = build_assessment(U, outdir, key=False)
    out["exam_key"] = build_assessment(U, outdir, key=True)
    return out
