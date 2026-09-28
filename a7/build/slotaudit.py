"""Every expression a unit's decks paint in slot colours (HOUSE STYLE §2a), as the renderer reads
it: [base] in brackets, ^{exponent} marked, one line each. Rule 0 — a wrong base is a wrong
statement about the mathematics — so this list is READ, line by line, after any change to a spec's
notes, worked examples or boards, and after any change to mathimg._slot_colors.
    python3 slotaudit.py u3          → prints the list; the last line counts refusals
"""
import sys, os, re, glob, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
UNIT = sys.argv[1] if len(sys.argv) > 1 else "u3"
from lib import mathimg
from matplotlib.font_manager import FontProperties

def pieces(row):
    return [p[1:-1] for p in re.split(r"(\$[^$]+\$)", row) if p.startswith("$")]

def show(latex, pt):
    latex = re.sub(r"\\frac(?![A-Za-z])", r"\\dfrac", latex)
    r = mathimg._PARSER.parse(f"${latex}$", dpi=72, prop=FontProperties(size=pt))
    col = mathimg._slot_colors(r.glyphs, pt)
    out, prev = [], None
    for g, c in zip(r.glyphs, col):
        tag = {mathimg.CB1: "B", mathimg.CB2: "E"}.get(c, "")
        if tag != prev:
            if prev == "B": out.append("]")
            if prev == "E": out.append("}")
            if tag == "B": out.append("[")
            if tag == "E": out.append("^{")
        out.append(chr(g[2])); prev = tag
    if prev == "B": out.append("]")
    if prev == "E": out.append("}")
    return "".join(out)

rows = []
for f in sorted(glob.glob(os.path.join(HERE, UNIT, "l[0-9]*.py"))):
    sp = importlib.util.spec_from_file_location("l", f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    L = m.L; code = L["code"]
    for n in L["notes"]:
        for r in n.get("math", []): rows += [(code, "notes", x, 32) for x in pieces(r)]
        for it in n.get("items", []) + n.get("items2", []):
            t = it if isinstance(it, str) else " ".join(it)
            rows += [(code, "notes", x, 32) for x in pieces(t)]
    for ex in L["examples"]:
        for w in ex["worked"]:
            for r in w["rows"]:
                if isinstance(r, tuple): rows.append((code, "worked", r[0], 32))
            for it in w.get("items", []): rows += [(code, "worked", x, 32) for x in pieces(it)]
        yt = ex.get("your_turn")
        if yt:
            for r in yt["prompt"]: rows += [(code, "yt-reveal", x, 40) for x in pieces(r)]
    for q in L["whiteboard"]:
        if q.get("latex"): rows.append((code, "wb-reveal", q["latex"], 40))
        for r in q.get("text", []): rows += [(code, "wb-reveal", x, 32) for x in pieces(r)]

bad = 0
for code, where, latex, pt in rows:
    try:
        print(f"{code:5} {where:9} {show(latex, pt)}")
    except Exception as e:
        bad += 1
        print(f"{code:5} {where:9} REFUSED  {latex}   <- {e}")
print(f"\n{len(rows)} expressions, {bad} refused")
