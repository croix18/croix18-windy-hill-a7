"""Ruling 25: a Florida-format lesson plan per lesson, with the MTRs named and the evidence for
each. Ten sections, in this order, one page-set per lesson, 53 minutes. Everything that can be
read from the deck's side-car is read, never typed.
"""
import os
from .dockit import Doc, INK, GRAY, RED, VOCAB
from . import tekit

# The seven Mathematical Thinking and Reasoning standards, for the plan's standards block.
MTR_TEXT = {
    "MTR.1.1": "Actively participate in effortful learning both individually and collectively.",
    "MTR.2.1": "Demonstrate understanding by representing problems in multiple ways.",
    "MTR.3.1": "Complete tasks with mathematical fluency.",
    "MTR.4.1": "Engage in discussions that reflect on the mathematical thinking of self and others.",
    "MTR.5.1": "Use patterns and structure to help understand and connect mathematical concepts.",
    "MTR.6.1": "Assess the reasonableness of solutions.",
    "MTR.7.1": "Apply mathematics to real-world contexts.",
}

SPLIT_MOVE = ("When a board splits — no option holding about two-thirds of the room — sixty "
              "seconds of “convince the person next to you”, then re-vote, then reveal. "
              "The minute comes out of the whiteboard remainder.")


def build_plan(L, deck_path, outdir, course, label):
    rows, wb_min, side, blocks = tekit.plan_from_sidecar(deck_path[:-5] + ".notes.json")
    code = L["code"]
    doc = Doc(f"{course}  ·  Unit {L['unit']}  ·  {label}", L["title"], "Lesson Plan", name_block=False)

    # 1 -------------------------------------------------- info
    doc.section("1.  Lesson Information")
    doc.table([2200, 2400, 2200, 2560], [
        ["Course", "Grade 7 Accelerated (1205050)", "Unit",
         f"{L['unit']} — {L['unit_title']}" if L.get("unit_title") else str(L["unit"])],
        ["Lesson", f"{label} — {L['title']}", "Date", "____________________"],
        ["Length", f"{tekit.PERIOD} minutes (one period)", "Benchmark(s)", L["benchmark"]],
    ], header=False, size=10)

    # 2 -------------------------------------------------- standards
    doc.section("2.  Standards")
    doc.para(f"**{L['benchmark']}**  {L['benchmark_text']}", size=10.5, before=2, after=4)
    T = L["te"]
    notes = dict(T.get("standard_notes", []))
    must = T.get("must") or notes.get("Clarification") or notes.get("Benchmark")
    if must:
        doc.para("**Must.**  " + must, size=10.5, before=0, after=3)
    if T.get("must_not") or notes.get("Boundary"):
        doc.para("**Must not.**  " + (T.get("must_not") or notes.get("Boundary")), size=10.5, before=0, after=4)

    # 3 -------------------------------------------------- MTRs, with evidence
    doc.section("3.  Mathematical Thinking and Reasoning Standards", "the evidence for each, from this period")
    rows_mtr = [["MTR", "What it asks", "The evidence in this lesson"]]
    for mtr, ev in L["mtr"]:
        rows_mtr.append([f"MA.K12.{mtr}", MTR_TEXT.get(mtr, ""), ev])
    doc.table([1500, 3400, 4460], rows_mtr, header=True, size=10)

    # 4 -------------------------------------------------- target and essential question
    doc.section("4.  Learning Target and Essential Question")
    doc.para("**Learning target.**  " + L["target"], size=10.5, before=2, after=3)
    doc.para("**Essential question.**  " + L["essential"], size=10.5, before=0, after=3)
    doc.para("**Building on.**  " + L["building_on"], size=10, before=0, after=2)
    doc.para("**Working toward.**  " + L["working_toward"], size=10, before=0, after=4)

    # 5 -------------------------------------------------- sequence, read from the deck
    doc.section("5.  Sequence", "read from the deck; never typed")
    seq = [["Segment", "Min", "What the teacher does", "What students do"]]
    for b in blocks:
        first = b["subs"][0]
        seg = b["seg"]
        mins = wb_min if b["kind"] == "wb" else b["min"]
        if b["kind"] == "title":
            t, s_ = "Post the target; say the 'today' line and nothing else yet.", "Copy the target."
        elif b["kind"] == "warmup":
            t, s_ = "Two minutes silent, then reveal. One sentence of reteach per question at most.", "Four retrieval questions, alone, no notes."
        elif b["kind"] == "notes":
            t, s_ = "Teach from the front. Expand once per law; say the OFF line out loud.", "Copy the notes; answer the checks aloud."
        elif b["kind"] == "example":
            t, s_ = "Work the example; name the wrong boards before they appear.", "Watch, then work the Your Turn alone."
        elif b["kind"] == "yourturn":
            t, s_ = "Circulate; reveal and name what a wrong board most likely did.", "Work it alone; boards up on the cue."
        elif b["kind"] == "wb":
            t, s_ = "One question at a time. Boards down until the cue, all up together; scan the back row first.", "Answer on a board; hold it up on three."
        elif b["kind"] == "independent":
            t, s_ = "Silent. Circulate and mark what you see; do not teach.", "Six questions, written, alone."
        else:
            t, s_ = "Assign the day's IXL skills.", "Start the skills; finish tonight."
        seq.append([seg, f"{mins}", t, s_])
    seq.append([{"text": "Total", "bold": True}, {"text": str(tekit.PERIOD), "bold": True}, "", ""])
    doc.table([2300, 620, 3300, 3140], seq, header=True, size=9.5)

    # 6 -------------------------------------------------- gradual release
    doc.section("6.  Gradual Release")
    doc.para("**I do.**  The Notes slides and the worked half of each Example: the teacher writes, the class copies, and the OFF line is said out loud rather than printed.", size=10.5, before=2, after=3)
    doc.para("**We do.**  Each Example's Your Turn: the same steps on the student's own numbers, revealed and named a minute later.", size=10.5, before=0, after=3)
    doc.para(f"**You do.**  The nine-question whiteboard round ({wb_min} minutes) and then the six-question independent set, silent and written.", size=10.5, before=0, after=4)

    # 7 -------------------------------------------------- higher-order questions with DOK
    doc.section("7.  Higher-Order Questions")
    hq = [["Question", "DOK"]]
    for q, dok in L.get("hoq", []):
        hq.append([q, dok])
    doc.table([7860, 1500], hq, header=True, size=10)

    # 8 -------------------------------------------------- checks for understanding, with the response
    doc.section("8.  Checks for Understanding", "each board, and what to do about it")
    chk = [["#", "What the board asks", "Answer", "If the board is wrong"]]
    for i, q in enumerate(L["whiteboard"]):
        from .lessonbuild import board_text
        qt = board_text(q)
        ans = q.get("answer") or ("$" + q.get("answer_latex", "") + "$")
        errs = q.get("errors") or {}
        wrong = "; ".join(f"({k}) {v}" for k, v in errs.items()) if errs else q.get("wrong", "")
        chk.append([str(i + 1), qt, {"text": ans, "bold": True, "italic": True, "color": RED}, wrong])
    doc.table([400, 3100, 1900, 3960], chk, header=True, size=9)
    doc.para("**MTR.4.1 — the one peer move.**  " + SPLIT_MOVE, size=10, before=4, after=4)

    # 9 -------------------------------------------------- differentiation
    doc.section("9.  Differentiation")
    d = L.get("differentiation", {})
    doc.para("**ESE / IEP.**  " + d.get("ese", ""), size=10.5, before=2, after=3)
    doc.para("**ELL.**  " + d.get("ell", ""), size=10.5, before=0, after=3)
    doc.para("**Enrichment.**  " + d.get("enrichment", ""), size=10.5, before=0, after=4)

    # 10 ------------------------------------------------- closure, vocabulary, materials, homework
    doc.section("10.  Closure, Vocabulary, Materials, Practice")
    doc.para("**Closure.**  " + L.get("closure", "The last board is written work; it is the exit evidence. Read the boards, not the papers."), size=10.5, before=2, after=3)
    doc.para("**Vocabulary.**  " + "; ".join(f"__{t}__" for t, _ in L["vocab"]), size=10.5, before=0, after=3)
    doc.para("**Materials.**  " + T.get("materials", "Whiteboards and markers."), size=10.5, before=0, after=3)
    doc.para("**Practice.**  The six-question independent set is worked silently in class; whatever is not finished goes home. "
             + "IXL, all skills required to a SmartScore of 67, due at the start of the next class: "
             + "; ".join(L["ixl"]) + ".", size=10.5, before=0, after=4)

    name = f"A7 {code}  Lesson Plan.docx"
    path = os.path.join(outdir, name)
    doc.save(path)
    return path
