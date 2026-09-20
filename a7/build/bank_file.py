#!/usr/bin/env python3
"""Ruling 26: the question-bank commentary lives outside the teacher's edition.
    python3 bank_file.py u3      ->  ../unit03/BANK - Unit 3.md
One file per unit: per lesson, the variation structure, what the audit found, what changed from
the book, and the bank answers. Generated from the same lesson specs the banks are built from.
"""
import os, sys, glob, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
unit = sys.argv[1].rstrip("/")
specs = sorted(glob.glob(os.path.join(HERE, unit, "l[0-9][0-9].py")))
Ls = []
for sp in specs:
    m = importlib.util.spec_from_file_location("x", sp)
    mod = importlib.util.module_from_spec(m); m.loader.exec_module(mod)
    Ls.append(mod.L)
un = Ls[0]["unit"]
out = [f"# BANK — Unit {un}", "",
       "The question-bank commentary for every lesson in the unit: how each bank varies, what the",
       "audit against Math Nation found, what changed from the book, and the answers.",
       "",
       "**This is not a handout and it is not the teacher's edition.** Under ruling 26 the teacher's",
       "edition is four pages read in twenty minutes; this is the reference behind it, read once when",
       "the unit is planned. The printed keys in `Answer Keys/` are generated from the same specs.",
       ""]
def answers(items, title):
    out.append(f"**{title}.**  ")
    n = 0; parts = []
    for it in items:
        if it.get("heading") or it.get("table"):
            continue
        n += 1
        if it.get("parts"):
            a = "  ".join(f"({p['label']}) {p.get('answer') or ''}" for p in it["parts"])
        elif it.get("choices"):
            corr = it["correct"] if isinstance(it["correct"], (list, tuple)) else [it["correct"]]
            a = ", ".join(chr(65 + c) for c in corr) + " " + (it.get("answer") or "")
        else:
            a = it.get("answer") or ""
        parts.append(f"{n}. {a}")
    out.append("  ".join(parts)); out.append("")
for L in Ls:
    T = L["te"]
    out.append(f"## {L['code']}  {L['title']}")
    out.append("")
    out.append(f"*{L['benchmark']}*")
    out.append("")
    if T.get("variation"):
        out.append(f"**Variation.**  {T['variation']}"); out.append("")
    if T.get("read_first"):
        out.append("**Read this once, when you plan the unit.**"); out.append("")
        for p in T["read_first"]:
            out.append(f"- {p}")
        out.append("")
    if T.get("audit"):
        out.append("**What the audit against Math Nation found.**"); out.append("")
        for p in T["audit"]:
            out.append(f"- {p}")
        out.append("")
    if T.get("changes"):
        out.append("**What changed from the book.**"); out.append("")
        for p in T["changes"]:
            out.append(f"- {p}")
        out.append("")
    answers(L["bank"], "Question Bank answers")
    answers(L["additional"], "Question Bank – Additional answers")
    out.append("---"); out.append("")
dest = os.path.join(HERE, "..", f"unit{un:02d}", f"BANK - Unit {un}.md")
os.makedirs(os.path.dirname(dest), exist_ok=True)
open(dest, "w").write("\n".join(out))
print(f"wrote {os.path.relpath(dest, os.path.join(HERE, '..', '..'))}  ({len(Ls)} lessons)")
