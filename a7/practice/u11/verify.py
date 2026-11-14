"""A7 Unit 11 practice: the independent check.   python3 verify.py   (reads dump.json, written by u11_check.js)
Nothing of the engine's arithmetic is trusted here. Every question is read back from the HTML a student sees — its words, its
math, its choices, its graph's SVG and its tables — and worked again exactly in sympy over the real numbers: every equation
solved (its one solution, or no solution, or every number), every ordered pair put into both equations of its system, every
crossing found by solving the system, every table value recomputed, the box of question 6 solved for the ending its words ask,
the story of question 7 written as an equation and solved, Q14(b)'s exact crossing and the tolerance around it (audit E15:
x and y within 0.2 of it; the swapped pair and the nearest grid point outside). Then every worked line (each must be an
equation with the same solutions as the first — no false equation as a line of work), every Hint number step ("What is
15 − 18?"), and every all-multiple-choice wrong answer (never the key, never inside an estimate's tolerance). Ruling 43 is
held from the specs themselves (shown43.py reads l01–l08.py and unit.py): no set asks an equation, a system or a story a
lesson, the review or the practice paper showed. Finally the test itself (a7/build/u11/unit.py): the page has its sections,
in its order, with its kinds of question and its points (ruling 49: the test is a random set of this page)."""
import json, os, re, sys
from fractions import Fraction as Fr
import sympy as sp
from sympy import Rational as Q
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, rationalize

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import shown43

DUMP = json.load(open(os.path.join(HERE, "dump.json"), encoding="utf-8"))
GLY = str.maketrans({"½": "(1/2)", "⅓": "(1/3)", "⅔": "(2/3)", "¼": "(1/4)", "¾": "(3/4)", "⅕": "(1/5)", "⅖": "(2/5)", "⅗": "(3/5)", "⅘": "(4/5)"})
TR = standard_transformations + (implicit_multiplication_application, rationalize)
bad = []
def no(where, msg): bad.append("%s: %s" % (where, msg))
n = dict(eq=0, lines=0, steps=0, pairs=0, segs=0, tables=0, choices=0, shown=0)

def text(h):
    t = re.sub(r'<span class="fr"><span class="nu">([^<]*)</span><span class="de">([^<]*)</span></span>', r"((\1)/(\2))", str(h))
    t = re.sub(r"<svg[\s\S]*?</svg>", " ", t)
    t = re.sub(r"<[^>]+>", "", t).replace("&nbsp;", " ").replace(" ", " ").replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    return re.sub(r"\s+", " ", t).strip()
def maths(h):
    """the kit's math spans of a piece of html, whole, as plain text"""
    s, out, k = str(h), [], 0
    while True:
        k = s.find('<span class="m"', k)
        if k < 0: return out
        depth, j = 0, k
        for m in re.finditer(r"<span\b|</span>", s[k:]):
            if m.group(0) == "</span>":
                depth -= 1
                if depth == 0: j = k + m.end(); break
            else: depth += 1
        out.append(text(s[s.index(">", k) + 1:j - 7])); k = j
def expr(t, letters):
    t = re.sub(r"□(?=[a-z(])", "BOX*", t.replace("−", "-").replace("·", "*").replace("÷", "/").translate(GLY)).replace("□", "BOX")
    loc = {c: sp.Symbol(c, real=True) for c in letters}; loc["BOX"] = sp.Symbol("BOX", real=True)
    return parse_expr(t, local_dict=loc, transformations=TR)
def ending(t, v):
    L, R = t.split("=")
    x = sp.Symbol(v, real=True)
    d = sp.expand(expr(L, v) - expr(R, v))
    if not d.has(x): return ("all",) if d == 0 else ("none",)
    s = sp.solve(sp.Eq(expr(L, v), expr(R, v)), x)
    return ("one", s[0]) if len(s) == 1 else ("?",)
def line(t):
    m = re.match(r"^y\s*=\s*(.+)$", t.strip())
    if not m: raise ValueError("not a line: " + t)
    x = sp.Symbol("x", real=True); e = sp.expand(expr(m.group(1), "x"))
    return (sp.Rational(e.coeff(x, 1)), sp.Rational(e.coeff(x, 0)))
def num(s):
    s = s.replace("−", "-").strip()
    return sp.Rational(sp.nsimplify(parse_expr(s, transformations=TR), rational=True))
X, Y = sp.symbols("x y", real=True)
def solve_sys(l1, l2):
    return sp.solve([sp.Eq(Y, l1[0] * X + l1[1]), sp.Eq(Y, l2[0] * X + l2[1])], [X, Y], dict=True)
def pair(s):
    m = re.search(r"\((−?-?[\d./()]+),\s*(−?-?[\d./()]+)\)", s.replace("−", "-"))
    return (num(m.group(1)), num(m.group(2)))

SHOWN, U = shown43.shown()

def plane(where, html, lines, want_n, cross=None):
    m = re.search(r'data-win="([^"]+)" data-px="([^"]+)"', html)
    if not m: no(where, "no plane"); return
    x0, x1, y0, y1, ys = [Fr(v) for v in m.group(1).split()]; k = Fr(m.group(2))
    segs = re.findall(r'<line class="(ln[12])" data-line="(\d)" x1="([-\d.]+)" y1="([-\d.]+)" x2="([-\d.]+)" y2="([-\d.]+)"/>', html)
    if len(segs) != want_n: no(where, "%d lines drawn, not %d" % (len(segs), want_n))
    for cls, i, a, b, c, d in segs:
        n["segs"] += 1; L = lines[int(i)]
        for px, py in ((a, b), (c, d)):
            xv = x0 + Fr(px) / k; yv = y1 - Fr(py) / k * ys
            if abs(float(L[0]) * float(xv) + float(L[1]) - float(yv)) > (abs(float(L[0])) + 1) * float(ys) * 0.06 / float(k) + 1e-6:
                no(where, "a drawn line is off its equation y = %sx + %s at (%s, %s)" % (L[0], L[1], float(xv), float(yv)))
    if cross is not None:
        cx, cy = cross
        if not (x0 < cx < x1 and y0 < cy < y1): no(where, "the crossing (%s, %s) is outside the window" % cross)

def check_lines(where, sol, first, v):
    for i, l in enumerate(sol):
        n["lines"] += 1
        ex = l.get("ex") if isinstance(l, dict) else None
        if ex and "=" in text(ex) and first and v:
            t = text(ex)
            if "□" in t or t.startswith("about") or "(" in t and "," in t: continue
            got = ending(t, v)
            if got != first: no(where, "worked line %d, %s, is %s; the equation is %s" % (i + 1, t, got, first))
def check_steps(where, steps):
    for s in steps:
        n["steps"] += 1
        runs = [r for r in maths(s["ask"]) if not re.search(r"[a-z□]", r)]
        if re.search(r"What is ", text(s["ask"])) and runs:
            try: v = sp.nsimplify(expr(runs[-1], ""), rational=True)
            except Exception: continue
            if v != num(s["ans"]): no(where, "a Hint step asks %s; its answer is %s" % (runs[-1], s["ans"]))
        if s.get("tol") and abs(num(s["ans"]) - num(s["near"])) > num(s["tol"]): no(where, "a Hint estimate step's own answer is outside its tolerance")

def check_choices(where, p, keyval, est=None):
    for c in p["choices"]:
        n["choices"] += 1
        t = text(c)
        if est:
            v = pair(t)
            if abs(v[0] - est[0]) <= Q(1, 10) and abs(v[1] - est[1]) <= Q(1, 10): no(where, "a wrong choice %s is inside the tolerance" % t)
        elif p["kind"] in ("pair", "story"):
            nums = [num(x) for x in re.findall(r"−?\d+(?:\.\d+)?", t)]
            if tuple(nums[:2]) == tuple(keyval): no(where, "a wrong choice %s is the key" % t)
        else:
            m = re.findall(r"−?\d+(?:\.\d+)?", t)
            if m and num(m[-1]) == keyval: no(where, "a wrong choice %s is the key" % t)
    if len(p["choices"]) < 3: no(where, "fewer than three wrong answers for the paper")

def eq_key(t, ending_):
    nums = sorted(shown43.numbers(t.replace("−", "-").replace("½", "(1/2)")))
    e = ending_
    end = "box" if "□" in t else shown43.kstr(Fr(str(e[1]))) if e[0] == "one" else e[0]
    return ",".join(nums) + "|" + end
def held43(where, eqs=(), lines=(), story=None):
    for t, e in eqs:
        k = eq_key(t, e)
        if k in SHOWN["eq"]: n["shown"] += 1; no(where, "asks %s, which %s showed" % (t, SHOWN["eq"][k]))
    if len(lines) == 2:
        k = shown43.syskey(*[(Fr(str(a)), Fr(str(b))) for a, b in lines])
        if k in SHOWN["sys"]: n["shown"] += 1; no(where, "asks the system %s, which %s showed" % (k, SHOWN["sys"][k]))
    if story:
        w = shown43.story_hit(story, SHOWN["story"])
        if w: n["shown"] += 1; no(where, "tells a story with the numbers %s, which %s showed" % (story, w))

for S in DUMP["sets"]:
    seed = S["seed"]
    for it in S["items"]:
        q = it["q"]; w = "set %d Q%d" % (seed, q); st = text(it["stem"]); M = maths(it["stem"])
        try:
            if q <= 4:
                p = it["parts"][0]; t = M[0]; v = re.findall(r"[a-z]", t)[0]; e = ending(t, v); n["eq"] += 1
                key = num(text(p["key"]).split("=")[1])
                if e != ("one", key): no(w, "%s is %s, the key %s" % (t, e, key))
                check_lines(w, p["sol"], e, v); check_steps(w, p["steps"]); check_choices(w, p, key)
                held43(w, eqs=[(t, e)])
            elif q == 5:
                ends = []
                for p in it["parts"]:
                    t = text(p["line"]); e = ending(t, "x"); n["eq"] += 1
                    want = {"one": "One solution", "none": "No solution", "all": "Infinitely many solutions"}[e[0]]
                    if p["opts"][p["correct"]] != want: no(w + p["label"], "%s has %s; the key says %s" % (t, want, p["opts"][p["correct"]]))
                    if e[0] == "one" and not any(("x = " + str(e[1]).replace("-", "−")) in text(s) for s in p["sol"]): no(w + p["label"], "the worked solution does not find x = %s" % e[1])
                    ends.append(e[0]); held43(w + p["label"], eqs=[(t, e)])
                if sorted(ends) != ["all", "none", "one"]: no(w, "not one of each ending")
            elif q == 6:
                p = it["parts"][0]; t = M[0]; L, R = t.split("=")
                B = sp.Symbol("BOX", real=True); x = sp.Symbol("x", real=True)
                d = sp.expand(expr(L, "x") - expr(R, "x"))
                goal = "none" if "no solution" in st else "all"
                a, c = d.coeff(x, 1), d.coeff(x, 0)
                sols = sp.solve([a, c], [B], dict=True) if goal == "all" else [s for s in sp.solve(a, B, dict=True) if c.subs(s) != 0]
                key = num(text(p["key"]).split("=")[1])
                if len(sols) != 1 or sols[0][B] != key: no(w, "the box for %s in %s is %s; the key %s" % (goal, t, sols, key))
                n["eq"] += 1; check_steps(w, p["steps"]); check_choices(w, p, key)
                held43(w, eqs=[(t, ("box",))])
            elif q == 7:
                p = it["parts"][0]; sents = re.split(r"(?<=\.) ", st)[:2]; fees, prices = [], []
                for s_ in sents:
                    ns = [int(v) for v in re.findall(r"\$(\d+)", s_)]
                    pm = re.search(r"\$(\d+) (?:a|an) (?:month|visit|class|hour)\b", s_) or re.search(r"a visit costs \$(\d+)", s_)
                    pr = int(pm.group(1)); ns.remove(pr); prices.append(pr); fees.append(ns[0] if ns else 0)
                c = sp.Symbol("c", real=True); sol = sp.solve(sp.Eq(fees[0] + prices[0] * c, fees[1] + prices[1] * c), c)
                key = num(re.findall(r"\d+", text(p["key"]))[0])
                if sol != [key] or not key.is_integer or key < 2: no(w, "the plans meet at %s; the key %s" % (sol, key))
                first = ("one", key); v = re.findall(r"[a-z]", text(p["sol"][0]["ex"]))[0]
                if ending(text(p["sol"][0]["ex"]), v) != first: no(w, "the worked equation is not the story's")
                check_lines(w, p["sol"], first, v); check_steps(w, p["steps"]); check_choices(w, p, key)
                held43(w, story=[str(v_) for v_ in fees + prices if v_])
            elif q == 8:
                pr = pair(M[0]); rights = []
                for i, o in enumerate(it["opts"]):
                    ls = [line(t) for t in maths(o)]; n["pairs"] += 1
                    if len(ls) != 2 or ls[0][0] == ls[1][0]: no(w, "system %d is not two lines with different numbers multiplying x" % i)
                    k = sum(1 for l in ls if l[0] * pr[0] + l[1] == pr[1])
                    if k == 2: rights.append(i)
                    elif k != 1: no(w, "wrong system %d is true in %d of its equations, not exactly 1" % (i, k))
                    held43(w, lines=ls)
                if rights != it["correct"] or not 2 <= len(rights) <= 3: no(w, "the systems solved by %s are %s; the key %s" % (pr, rights, it["correct"]))
            elif q == 9:
                ls = [line(t) for t in M if t.startswith("y")][:2]
                if len(ls) != 2 or ls[0][0] == ls[1][0]: no(w, "not two lines with different numbers multiplying x")
                pr = pair(M[2]); t = [l[0] * pr[0] + l[1] == pr[1] for l in ls]; n["pairs"] += 1
                o = text(it["opts"][it["correct"]])
                ok = (o.startswith("Yes — it makes both") and all(t)) or (o.startswith("No") and not all(t) and ((M[0] in o and not t[0]) or (M[1] in o and not t[1])))
                if not ok: no(w, "the key '%s' is not the right verdict and reason for %s (%s)" % (o, pr, t))
                held43(w, lines=ls)
            elif q in (10, 11):
                ls = [line(t) for t in M if t.startswith("y")][:2]
                same = sp.expand((ls[0][0] - ls[1][0]) * X + ls[0][1] - ls[1][1]) == 0
                sol = [] if same else solve_sys(*ls)
                cnt = 2 if same else 0 if len(sol) == 1 else 1
                if it["correct"] != cnt: no(w, "the system has %s; the key %s" % (["one", "none", "infinitely many"][cnt], it["opts"][it["correct"]]))
                if (q == 10) != (cnt == 0): no(w, "Q10 must cross and Q11 must not")
                plane(w, it["fig"], ls[:1] if same else ls, 1 if same else 2, (sol[0][X], sol[0][Y]) if len(sol) == 1 else None)
                held43(w, lines=ls)
            elif q == 12:
                p = it["parts"][0]; ls = [line(t) for t in M if t.startswith("y")][:2]; sol = solve_sys(*ls)
                key = pair(text(p["key"]))
                if len(sol) != 1 or (sol[0][X], sol[0][Y]) != key: no(w, "the system solves to %s; the key %s" % (sol, key))
                elif not (key[0].is_integer and key[1].is_integer): no(w, "the crossing is not a grid point")
                plane(w, it["fig"], ls, 2, key); check_steps(w, p["steps"]); check_choices(w, p, key); held43(w, lines=ls)
            elif q == 13:
                ls = [line(t) for t in M if t.startswith("y")][:2]; n["tables"] += 1
                tabs = re.findall(r'<table class="vt"><caption>([\s\S]*?)</caption>([\s\S]*?)</table>', it["fig"]); gap = None; cols = None
                for ti, (cap, body) in enumerate(tabs):
                    if line(text(cap)) != ls[ti]: no(w, "table %d is titled %s" % (ti + 1, text(cap)))
                    rows = [re.findall(r"<td>([\s\S]*?)</td>", r) for r in re.findall(r"<tr>([\s\S]*?)</tr>", body)]
                    xs = [num(text(c)) for c in rows[0]]; cols = xs
                    for xv, c in zip(xs, rows[1]):
                        if 'class="gap"' in c: gap = xv; continue
                        if num(text(c)) != ls[ti][0] * xv + ls[ti][1]: no(w, "table %d at x = %s says %s" % (ti + 1, xv, text(c)))
                pa, pb = it["parts"]
                if num(text(pa["key"])) != ls[0][0] * gap + ls[0][1]: no(w + "a", "the missing value is %s; the key %s" % (ls[0][0] * gap + ls[0][1], text(pa["key"])))
                agree = [xv for xv in cols if ls[0][0] * xv + ls[0][1] == ls[1][0] * xv + ls[1][1]]
                if len(agree) != 1 or pair(text(pb["key"])) != (agree[0], ls[0][0] * agree[0] + ls[0][1]): no(w + "b", "the tables agree at %s; the key %s" % (agree, text(pb["key"])))
                for p in (pa, pb): check_steps(w + p["label"], p["steps"])
                check_choices(w + "a", pa, num(text(pa["key"]))); check_choices(w + "b", pb, pair(text(pb["key"]))); held43(w, lines=ls)
            elif q == 14:
                pa, pb = it["parts"]
                m = re.match(r"^(\w+)\D*?(\d+)\D+?(\d+) (?:cm )?each week\. (\w+)\D*?(\d+)\D+?(saves|spends|grows) \$?(\d+)", st)
                l1 = (Q(m.group(3)), Q(m.group(2))); l2 = (-Q(m.group(7)) if m.group(6) == "spends" else Q(m.group(7)), Q(m.group(5)))
                sol = solve_sys(l1, l2); nums = [int(v) for v in re.findall(r"\d+", text(pa["key"]))]
                if len(sol) != 1 or (sol[0][X], sol[0][Y]) != (Q(nums[0]), Q(nums[1])): no(w + "a", "the story meets at %s; the key %s" % (sol, text(pa["key"])))
                plane(w + "a", it["fig"], [l1, l2], 2, (sol[0][X], sol[0][Y]))
                held43(w + "a", story=[m.group(2), m.group(3), m.group(5), m.group(7)])
                ls = [line(t) for t in maths(pb["line"]) if t.startswith("y")][:2]; s2 = solve_sys(*ls)
                ex, ey = s2[0][X], s2[0][Y]; key = pair(text(pb["key"]))
                if abs(key[0] - ex) > Q(1, 20) or abs(key[1] - ey) > Q(1, 20): no(w + "b", "the key %s is not (%s, %s) to the tenth" % (key, ex, ey))
                for vv in (ex, ey):
                    if abs(2 * vv - round(2 * vv)) / 2 <= Q(1, 10): no(w + "b", "a grid or half-grid line is within 0.1 of the point of intersection (%s, %s)" % (ex, ey))
                if abs(ex - ey) <= Q(1, 5): no(w + "b", "the swapped pair would be inside the tolerance")
                if "0.1" not in json.dumps(pb["steps"]) and not any(s_.get("tol") == "0.1" for s_ in pb["steps"]): no(w + "b", "the Hint does not accept 0.1 around the exact point")
                if not any("from" in text(s["say"]) and "to" in text(s["say"]) for s in pb["sol"]): no(w + "b", "the worked solution does not state the range it accepts")
                plane(w + "b", pb["line"], ls, 2, (ex, ey))
                for p in (pa, pb): check_steps(w + p["label"], p["steps"])
                check_choices(w + "a", pa, (Q(nums[0]), Q(nums[1]))); check_choices(w + "b", pb, None, est=(ex, ey)); held43(w + "b", lines=ls)
        except Exception as e:
            no(w, "could not check: %r" % (e,))

# ---------------------------------------------------------------- the test itself: the practice is its blueprint (ruling 49)
paper = U["assessment"]["forms"]["practice"]
if [s["title"] for s in paper] != DUMP["TITLES"]: no("the test", "its sections %s are not the practice's %s" % ([s["title"] for s in paper], DUMP["TITLES"]))
kind = lambda it: "multi" if isinstance(it.get("correct"), list) else "mc" if "choices" in it or it.get("answer", "").endswith("solution") or "solution" in it.get("answer", "") and "fig" in it and "parts" not in it else "parts" if "parts" in it else "solo"
pts = sum(len(it.get("parts", [])) or 1 for s in paper for it in s["items"])
if pts != U["assessment"]["total"]: no("the test", "its points add to %d, not %d" % (pts, U["assessment"]["total"]))
want_pts = [sum(len(it.get("parts", [])) or 1 for it in s["items"]) for s in paper]
if want_pts != [U["assessment"]["tracker"][b] for b in U["assessment"]["tracker_order"]]: no("the test", "its sections' points are not its tracker's")
for G in DUMP["sets"][:200]:
    mine = [len(it["parts"]) if it["type"] == "parts" else 1 for it in G["items"]]
    theirs = [len(it.get("parts", [])) or 1 for s in paper for it in s["items"]]
    if mine != theirs: no("set %d" % G["seed"], "its parts %s are not the test's %s" % (mine, theirs))

print("%d sets: %d equations solved, %d worked lines and %d Hint steps read back, %d ordered pairs put in both equations, %d drawn lines on their equations, %d table pairs, %d paper choices; ruling 43 from the specs: %d equations, %d systems, %d stories shown, %d hits; the test's %d questions and %d points matched: %s"
      % (len(DUMP["sets"]), n["eq"], n["lines"], n["steps"], n["pairs"], n["segs"], n["tables"], n["choices"], len(SHOWN["eq"]), len(SHOWN["sys"]), len(SHOWN["story"]), n["shown"],
         sum(len(s["items"]) for s in paper), pts, "ALL SOUND" if not bad else "%d PROBLEMS" % len(bad)))
for b in bad[:40]: print("  " + b)
sys.exit(1 if bad else 0)
