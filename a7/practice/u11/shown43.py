"""A7 Unit 11 practice: ruling 43 — what the lessons, the review and the practice paper SHOW, read out of the specs themselves
(a7/build/u11/l01–l08.py and unit.py), never from a list in the engine. Used by verify.py (every generated set is held to it)
and by `python3 verify.py --emit`, which writes shown.js for the engine to steer by.

Three kinds of thing are read from every string of every spec, block by block (a warm-up question, a note, an example and its
Your Turn, a whiteboard, an independent-set question, a bank question, the review's and the paper's items, the reference
sheet's lines):
  - an equation in one letter → the sizes of its printed numbers, sorted, and its ending (one number, 'none', 'all'), or
    'box' for an equation with a box in it;
  - a line y = mx + b (also written y = a(x + c) + d) → its m and b; every two lines of one block make a system;
  - a story with money, weeks, months, hours, visits, classes or centimeters → the numbers it prints."""
import os, re, runpy, sys
from fractions import Fraction as Fr
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor, rationalize

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "..", "..", "build")
UNIT = os.path.join(BUILD, "u11")
TR = standard_transformations + (implicit_multiplication_application, convert_xor, rationalize)


def kstr(q):
    q = Fr(q)
    d = q.denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    if d != 1: return "%d/%d" % (q.numerator, q.denominator)
    s = ("%.12f" % float(abs(q))).rstrip("0").rstrip(".") if q.denominator != 1 else str(abs(q.numerator))
    # exact decimal: build it from the fraction, not from a float
    if q.denominator != 1:
        k = 0; n = abs(q)
        while (n * 10 ** k).denominator != 1: k += 1
        v = int(n * 10 ** k); s = str(v).rjust(k + 1, "0"); s = s[:-k] + "." + s[-k:]
    return ("-" if q < 0 else "") + s


def tex_plain(s):
    """TeX (or the kit's plain math) → plain text a reader can parse: fractions in parentheses, ½ as (1/2), − as -."""
    t = str(s)
    for _ in range(4):
        t = re.sub(r"\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
    t = t.replace("\\left", "").replace("\\right", "").replace("\\cdot", "*").replace("\\times", "*").replace("\\div", "/")
    t = re.sub(r"\\text\{[^{}]*\}", " ", t)
    t = re.sub(r"\\(qquad|quad|,|;|!| )", " ", t)
    t = t.replace("\\square", "□").replace("\\Box", "□").replace("▢", "□")
    t = t.replace("−", "-").replace("–", "-").replace("½", "(1/2)").replace("⅓", "(1/3)").replace("¼", "(1/4)").replace("⅔", "(2/3)").replace("¾", "(3/4)").replace("·", "*").replace("×", "*")
    t = t.replace("**", "")
    return t


def numbers(t):
    return [kstr(Fr(x)) for x in re.findall(r"\d+(?:\.\d+)?", t)]


SAFE = re.compile(r"^[\d\s.+\-*/()a-z□]+$")


def pieces(text):
    """the candidate equations of a string: its math runs ($…$, or the whole string when it has no $), each cut at = signs"""
    s = str(text)
    runs = re.findall(r"\$([^$]*)\$", s) if "$" in s and s.count("$") >= 2 else [s]
    out = []
    for r in runs:
        t = tex_plain(r)
        for seg in re.split(r"\s{2,}|,(?![^()]*\))|;|\band\b|\bor\b|:", t):
            seg = seg.strip()
            if seg.count("=") != 1: continue
            L, R = [x.strip() for x in seg.split("=")]
            # keep only the math at the edges: the longest tail of L and head of R made of math characters
            mL = re.search(r"[\d\s.+\-*/()a-z□]*$", L); mR = re.match(r"^[\d\s.+\-*/()a-z□]*", R)
            L, R = mL.group(0).strip(), mR.group(0).strip()
            if not L or not R: continue
            out.append((L, R))
    return out


def parse(e, letters):
    e = e.replace("□", "BOX")
    loc = {c: sp.Symbol(c) for c in letters}
    loc["BOX"] = sp.Symbol("BOX")
    return parse_expr(e, local_dict=loc, transformations=TR, evaluate=True)


def read_eq(L, R):
    """→ ('eq', key) | ('line', (m, b)) | None"""
    letters = set(re.findall(r"[a-z]", L + R))
    if not letters or len(letters) > 2: return None
    if any(len(w) > 1 for w in re.findall(r"[a-z]+", L + R)): return None
    try:
        l, r = parse(L, letters), parse(R, letters)
    except Exception:
        return None
    box = "□" in L or "□" in R
    nums = sorted(numbers(L + " " + R))
    if letters == {"y", "x"} and L.replace(" ", "") == "y":
        x = sp.Symbol("x")
        try:
            poly = sp.Poly(sp.expand(r), x)
        except Exception:
            return None
        if poly.degree() > 1 or r.free_symbols - {x}: return None
        m = poly.coeff_monomial(x); b = poly.coeff_monomial(1)
        return ("line", (Fr(str(m)), Fr(str(b))))
    if len(letters) != 1 or "y" in letters and not box: return None
    v = sp.Symbol(list(letters)[0])
    if box: return ("eq", ",".join(nums) + "|box")
    d = sp.expand(l - r)
    try:
        poly = sp.Poly(d, v)
    except Exception:
        return None
    if poly.degree() > 1: return None
    a, b = poly.coeff_monomial(v), poly.coeff_monomial(1)
    end = kstr(Fr(str(-b / a))) if a != 0 else ("all" if b == 0 else "none")
    return ("eq", ",".join(nums) + "|" + end)


def texts(x, skip=("check", "yt_check", "fig", "te", "source", "band", "mtr", "hoq", "ixl", "differentiation", "vocab", "vocab_note")):
    if isinstance(x, str): return [x]
    if isinstance(x, dict): return [t for k, v in x.items() if k not in skip for t in texts(v, skip)]
    if isinstance(x, (list, tuple)): return [t for v in x for t in texts(v, skip)]
    return []


STORYW = re.compile(r"\\?\$\d|each week|a week|per week|a month|per month|an hour|per hour|a visit|a class\b|cm (?:tall|each)", re.I)


def blocks():
    """(where, [strings]) for every block of every spec"""
    sys.path.insert(0, UNIT); sys.path.insert(0, BUILD)
    out = []
    for f in sorted(os.listdir(UNIT)):
        if not re.match(r"^l\d\d\.py$", f): continue
        L = runpy.run_path(os.path.join(UNIT, f))["L"]
        for sec in ("warmup", "notes", "examples", "whiteboard", "independent", "bank", "additional"):
            for i, b in enumerate(L.get(sec) or []):
                out.append(("%s %s %d" % (L["code"], sec, i + 1), texts(b)))
        out.append(("%s's other words" % L["code"], texts({k: v for k, v in L.items() if k not in ("warmup", "notes", "examples", "whiteboard", "independent", "bank", "additional")})))
    U = runpy.run_path(os.path.join(UNIT, "unit.py"))["U"]
    for i, sec in enumerate(U["reference"]):
        for j, b in enumerate(sec["blocks"]): out.append(("the reference sheet %d.%d" % (i + 1, j + 1), texts(b)))
    for sec in U["review"]:
        for i, it in enumerate(sec["items"]): out.append(("the review %s%d" % (sec["letter"], i + 1), texts(it)))
    for sec in U["assessment"]["forms"]["practice"]:
        for i, it in enumerate(sec["items"]): out.append(("the practice paper, %s %d" % (sec["benchmark"], i + 1), texts(it)))
    return out, U


def shown():
    """→ {'eq': {key: where}, 'sys': {key: where}, 'story': [(numbers, where)]}"""
    bl, U = blocks()
    EQ, SYS, ST = {}, {}, []
    for where, ts in bl:
        lines = []
        for t in ts:
            for L, R in pieces(t):
                r = read_eq(L, R)
                if not r: continue
                if r[0] == "eq": EQ.setdefault(r[1], where)
                elif r[1] not in lines: lines.append(r[1])
            if STORYW.search(t) and "other words" not in where:
                ns = numbers(tex_plain(t))
                if len(ns) >= 2: ST.append((ns, where))
        for i in range(len(lines)):
            for j in range(i + 1, len(lines)):
                SYS.setdefault(syskey(lines[i], lines[j]), where)
    return {"eq": EQ, "sys": SYS, "story": ST}, U


def syskey(a, b):
    return ";".join(sorted([kstr(a[0]) + "," + kstr(a[1]), kstr(b[0]) + "," + kstr(b[1])]))


def story_hit(nums, ST):
    for ns, where in ST:
        pool = list(ns); ok = True
        for x in nums:
            if x in pool: pool.remove(x)
            else: ok = False; break
        if ok: return where
    return None


def emit():
    import json
    S, _ = shown()
    js = ("/* GENERATED by `python3 shown43.py --emit` from the lesson specs (a7/build/u11/l01–l08.py) and unit.py — do not edit by hand.\n"
          "   Ruling 43: what the lessons, the review and the practice paper show — equations (sizes of the printed numbers|ending),\n"
          "   systems (m,b;m,b) and stories (their numbers). The engine steers by it; verify.py reads the specs again on its own. */\n"
          "(function (root) { const S = " + json.dumps({"eq": sorted(S["eq"]), "sys": sorted(S["sys"]), "story": [ns for ns, w in S["story"]]}, separators=(",", ":")) + ";\n"
          "if (typeof module !== 'undefined' && module.exports) module.exports = S; else root.U11Shown = S; })(this);\n")
    open(os.path.join(HERE, "shown.js"), "w", encoding="utf-8").write(js)
    print("shown.js: %d equations, %d systems, %d stories" % (len(S["eq"]), len(S["sys"]), len(S["story"])))


if __name__ == "__main__" and "--emit" in sys.argv:
    emit()
elif __name__ == "__main__":
    S, _ = shown()
    print(len(S["eq"]), "equations,", len(S["sys"]), "systems,", len(S["story"]), "stories")
    for k in list(S["eq"])[:15]: print(" ", k, S["eq"][k])
    for k in list(S["sys"])[:10]: print(" ", k, S["sys"][k])
