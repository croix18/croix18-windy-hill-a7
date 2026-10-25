"""A7 Unit 6 practice: the independent check.   python3 verify.py   (reads dump.json, written by u6_check.js)
Written 25 Oct 2026. Nothing of the engine's arithmetic is trusted here. Every question is read back from what a student sees —
its words, its choices and its figure's labels — and worked out again exactly with sympy (square roots kept exact; a length
"to the nearest tenth" is sympy's floor of ten times the exact length plus a half), then compared with the key the page marks
against. Every worked line of Show me how, every sentence of it (and of every Hint, rule and named mistake) that states some
arithmetic, and every Hint number step is read back the same way. The unit's bounds are checked from the words too: every square
root a student takes is of a whole number up to 225 (MA.8.GR.1.1/1.2 Clarification 3); a whole hypotenuse is 5, 10, 13 or 15;
every point is on the −10…10 grid, off the axes, and every slanted or crossing segment crosses an axis; the copy in a similar
pair is drawn to scale. Finally the test itself (a7/build/u6/unit.py) is read: the practice has its sections, in its order,
with its kinds of question and its points (ruling 49: the test is a random set of this page)."""
import functools, json, os, re, runpy, sys
from html.parser import HTMLParser
import sympy as sp
from sympy import Rational as R, sqrt, floor, Integer

HERE = os.path.dirname(os.path.abspath(__file__))
DUMP = json.load(open(os.path.join(HERE, "dump.json"), encoding="utf-8"))
bad = []
def no(where, msg):
    bad.append(f"{where}: {msg}")

# ---------------------------------------------------------------- what is printed, read back
class Node:
    def __init__(self, tag, attrs):
        self.tag, self.cls, self.kids = tag, dict(attrs).get("class", ""), []
class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.root = Node("root", []); self.stack = [self.root]
    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs); self.stack[-1].kids.append(n); self.stack.append(n)
    def handle_endtag(self, tag):
        if len(self.stack) > 1: self.stack.pop()
    def handle_data(self, d):
        self.stack[-1].kids.append(d)
def tree(h):
    t = Tree(); t.feed(h); t.close(); return t.root
def text(n):
    """the words a student reads: a radical as √(…), a square as ^2"""
    if isinstance(n, str): return n.replace(" ", " ")
    k = n.kids
    if n.tag == "span" and n.cls.startswith("rad"):
        rc = next(x for x in k if not isinstance(x, str) and x.cls == "rc")
        return "√(" + "".join(text(x) for x in rc.kids) + ")"
    if n.tag == "span" and n.cls == "fr":                          # a stacked fraction, 4 over 3, read as (4÷3)
        nu = next(x for x in k if not isinstance(x, str) and x.cls == "nu"); de = next(x for x in k if not isinstance(x, str) and x.cls == "de")
        return "(" + "".join(text(x) for x in nu.kids) + "÷" + "".join(text(x) for x in de.kids) + ")"
    if n.tag == "sup": return "^" + "".join(text(x) for x in k)
    return "".join(text(x) for x in k)
@functools.lru_cache(maxsize=None)
def words(h):
    return re.sub(r"\s+", " ", text(tree(h))).strip()
NUM = r"−?\d+(?:\.\d+)?"
def q(s):
    """a printed number, exactly"""
    return R(s.replace("−", "-").replace(",", ""))
@functools.lru_cache(maxsize=None)
def value(e):
    """the exact value of a printed expression: + − × ÷ ·, ^2, √(n) or √n, parentheses, every numeral exact"""
    s = e.replace("−", "-").replace("×", "*").replace("·", "*").replace("÷", "/").replace("^", "**")
    s = re.sub(r"(?<=\d),(?=\d{3})", "", s)
    s = re.sub(r"√\s*(\d+(?:\.\d+)?)", r"sqrt(\1)", s).replace("√(", "sqrt(")
    if not re.fullmatch(r"[\d\s.+\-*/()]*(?:sqrt[\d\s.+\-*/()]*)*", s): raise ValueError("not arithmetic: " + e)
    s = re.sub(r"\d+(?:\.\d+)?", lambda m: f"R('{m.group(0)}')", s)
    return sp.nsimplify(eval(s, {"R": R, "sqrt": sqrt, "__builtins__": {}}))
@functools.lru_cache(maxsize=None)
def tenth(v):
    """an exact length to the nearest tenth (no ties: every one here is irrational, or has one decimal place already)"""
    return R(int(floor(10 * v + R(1, 2))), 10)
@functools.lru_cache(maxsize=None)
def cut(v, places):
    return R(int(floor(v * 10 ** places)), 10 ** places)
def whole_root(n, where, what):
    """√n for a whole n a student takes the root of: n ≤ 225 (the unit's bound)"""
    if not (n == int(n) and 0 < n <= 225): no(where, f"{what}: the square root of {n}, beyond the unit's bound of 225")
    return sqrt(n)
UNITS = {"cm": "centimeter", "in": "inch", "m": "meter", "ft": "foot", "yd": "yard"}
PLURAL = {"cm": "centimeters", "in": "inches", "m": "meters", "ft": "feet", "yd": "yards"}
ABBR = {v: k for k, v in PLURAL.items()}          # the words write a length out ("9 inches"); the answer box and key abbreviate it
ROUND = "Round your answer to the nearest tenth."
def unit_of(word, where):
    if word not in ABBR: raise ValueError(f"a length in the words is not written out: {word}")
    return ABBR[word]
def article(w): return "an" if w[0] in "aeiou" else "a"

# ---------------------------------------------------------------- arithmetic in a sentence (written again here, not shared)
TERM = r"(?:√\s*)?(?:\(\s*-?\d+(?:\.\d+)?\s*\)|\(\s*\d+\s*÷\s*\d+\s*\)|\d+(?:\.\d+)?)…?(?:\^2)?"
EXPR = TERM + r"(?:\s*[-+×÷·]\s*" + TERM + r")*"
CHAIN = re.compile(r"(?<![\w.^√)…])" + EXPR + r"(?:\s*(?:=|≈)\s*" + EXPR + r")+(?![\w^(…]|\.\d)")
n_claims = 0
def claims(where, h):
    global n_claims
    t = words(h) if "<" in h else h
    if re.search(r"\d\s*/\s*\d", t): no(where, "a fraction is printed: " + t[:100])
    t = t.replace("−", "-").replace("√(", "√").replace("the square root of ", "√")
    t = re.sub(r"√(\d+)\)", r"√\1", t)
    t = re.sub(r"(?<=\d),(?=\d{3}(?!\d))", "", t)
    for m in CHAIN.finditer(t):
        run = m.group(0); links = re.split(r"\s*(=|≈)\s*", run)
        try: vals = [value(links[i].replace("…", "")) for i in range(0, len(links), 2)]
        except Exception: continue
        n_claims += 1
        cuts = run.count("…")
        for i in range(len(vals) - 1):
            op, right = links[2 * i + 1], links[2 * i + 2]
            if op == "≈":
                dp = len(right.replace("…", "").split(".")[1]) if "." in right else 0
                if abs(vals[i] - vals[i + 1]) > R(1, 2) * R(10) ** -dp: no(where, "false: " + run)
            elif cuts:
                if abs(vals[i] - vals[i + 1]) > R(cuts, 1000): no(where, "false: " + run)
            elif sp.simplify(vals[i] - vals[i + 1]) != 0: no(where, "false: " + run)
        for i in range(2, len(links), 2):            # "e = d…" with no cut in e: d is e cut off after its last digit
            if links[i].endswith("…") and "…" not in links[i - 2]:
                d = links[i][:-1]; dp = len(d.split(".")[1]) if "." in d else 0
                if cut(vals[i // 2 - 1], dp) != R(d): no(where, f"{links[i - 2]} cut off is not {links[i]}")
    for m in re.finditer(r"√(\d+), (\d+\.\d+)…", t):
        n_claims += 1
        if cut(sqrt(int(m.group(1))), len(m.group(2).split(".")[1])) != R(m.group(2)): no(where, f"√{m.group(1)} cut off is not {m.group(2)}")

# ---------------------------------------------------------------- each question, worked out again from what it prints
def corners(st):
    m = re.fullmatch(r"Triangle ([A-Z])([A-Z])([A-Z]) has corners \1\((" + NUM + r"), (" + NUM + r")\), \2\((" + NUM + r"), (" + NUM + r")\) and \3\((" + NUM + r"), (" + NUM + r")\)\.", st)
    if not m: raise ValueError("the triangle: " + st)
    g = m.groups(); return {g[0]: (q(g[3]), q(g[4])), g[1]: (q(g[5]), q(g[6])), g[2]: (q(g[7]), q(g[8]))}, g[:3]
def on_grid(where, pts):
    for (x, y) in pts:
        if not (-10 <= x <= 10 and -10 <= y <= 10): no(where, f"({x}, {y}) is off the −10…10 grid")
        if x == 0 or y == 0: no(where, f"({x}, {y}) is on an axis")
def crosses(a, b): return (a < 0 < b) or (b < 0 < a)
def two_points(st):
    m = re.search(r"\((" + NUM + r"), (" + NUM + r")\) and (?:the [a-z ]+ is at )?\((" + NUM + r"), (" + NUM + r")\)", st)
    if not m: raise ValueError("two points: " + st)
    return (q(m.group(1)), q(m.group(2))), (q(m.group(3)), q(m.group(4)))
def fig_points(it):
    """the points as the figure prints them, "A(−7, 1)", and as it draws them"""
    pts = {}
    for l in it["figLabels"]:
        m = re.fullmatch(r"([A-Z])\((" + NUM + r"), (" + NUM + r")\)", l["s"])
        if m: pts[m.group(1)] = (q(m.group(2)), q(m.group(3)))
    drawn = {p[2]: (R(p[0]), R(p[1])) for p in it["fig"]["pts"]}
    if pts != drawn: raise ValueError(f"the figure prints {pts} but draws {drawn}")
    return pts

def expect(where, it, p):
    """the exact answer of a typed part, and whether it is asked to the nearest tenth, from the printed question alone"""
    st, ps, fam = words(it["stem"]), words(p["stem"]), p["fam"]
    if fam == "hypWhole":
        m = re.fullmatch(r"Its legs are (\d+) (\w+) and (\d+) \2\. How long is the hypotenuse\?", ps)
        if not m: raise ValueError("hypWhole: " + ps)
        a, u, b = int(m.group(1)), unit_of(m.group(2), where), int(m.group(3)); c = whole_root(a * a + b * b, where, "the hypotenuse")
        if c not in (5, 10, 13, 15): no(where, f"a whole hypotenuse of {c}")
        return c, u, False
    if fam == "legWhole":
        m = re.fullmatch(r"Its hypotenuse is (\d+) (\w+) and one leg is (\d+) \2\. How long is the other leg\?", ps)
        if not m: raise ValueError("legWhole: " + ps)
        c, u, a = int(m.group(1)), unit_of(m.group(2), where), int(m.group(3)); b = whole_root(c * c - a * a, where, "the other leg")
        if not b.is_integer: no(where, f"the other leg is {b}, not whole")
        return b, u, False
    if fam == "hypTenth":
        m = re.fullmatch(r"A right triangle has legs of (\d+) (\w+) and (\d+) \2\. How long is the hypotenuse, in \2\? " + re.escape(ROUND), st)
        if not m: raise ValueError("hypTenth: " + st)
        a, u, b = int(m.group(1)), unit_of(m.group(2), where), int(m.group(3))
        c = whole_root(a * a + b * b, where, "the hypotenuse")
        if c.is_integer: no(where, "a tenth question with a whole answer")
        return c, u, True
    if fam in ("diag", "shorter"):
        m = re.fullmatch(r"A rectangular (lawn|garden|playground|courtyard|patio) measures (\d+) (\w+) by (\d+) \3\. A path runs straight across it from one corner to the opposite corner\.", st)
        if not m: raise ValueError("place: " + st)
        place, u = m.group(1), unit_of(m.group(3), where)
        w, l = sorted((int(m.group(2)), int(m.group(4))))
        if u == "ft" and place not in ("garden", "patio"): no(where, f"a {place} {w} ft by {l} ft")
        # a real place at a real size: the width the shorter side, no more than three times as long, and no smaller than such a place is
        least = {("garden", "m"): 2, ("garden", "ft"): 5, ("garden", "yd"): 3, ("lawn", "m"): 4, ("lawn", "yd"): 4, ("patio", "ft"): 8, ("patio", "m"): 3,
                 ("playground", "m"): 6, ("playground", "yd"): 6, ("courtyard", "m"): 5, ("courtyard", "yd"): 5}.get((place, u))
        if least is None: no(where, f"a {place} measured in {u}")
        elif w < least: no(where, f"a {place} only {w} {u} wide")
        if not w < l <= 5 * w: no(where, f"a {place} {w} by {l}")
        path = whole_root(w * w + l * l, where, "the path")
        if fam == "diag":
            m2 = re.fullmatch(r"How long is the path, in (\w+)\? " + re.escape(ROUND), ps)
            if not m2 or m2.group(1) != PLURAL[u]: raise ValueError("diag: " + ps)
            return path, u, True
        if ps != f"How much shorter is the path than walking along two sides of the {place}? {ROUND}": raise ValueError("shorter: " + ps)
        return w + l - path, u, True
    if fam == "gridWhole":
        m = re.fullmatch(r"Find the distance between points ([A-Z]) and ([A-Z])\.", st)
        if not m: raise ValueError("gridWhole: " + st)
        P = fig_points(it); A, B = P[m.group(1)], P[m.group(2)]
        on_grid(where, [A, B])
        if not (crosses(A[0], B[0]) or crosses(A[1], B[1])): no(where, "the segment crosses no axis")
        d = whole_root((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2, where, "the distance")
        if not d.is_integer: no(where, f"a whole-number distance question with the answer {d}")
        return d, "units", False
    if fam == "coordTenth":
        m = re.fullmatch(r"Find the distance between \((" + NUM + r"), (" + NUM + r")\) and \((" + NUM + r"), (" + NUM + r")\)\. " + re.escape(ROUND), st)
        if not m: raise ValueError("coordTenth: " + st)
        A, B = (q(m.group(1)), q(m.group(2))), (q(m.group(3)), q(m.group(4)))
        on_grid(where, [A, B])
        if not (crosses(A[0], B[0]) or crosses(A[1], B[1])): no(where, "the segment crosses no axis")
        d = whole_root((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2, where, "the distance")
        if d.is_integer: no(where, "a tenth question with a whole answer")
        return d, "units", True
    if fam in ("crossSide", "perim"):
        P, names = corners(st)
        on_grid(where, P.values())
        J, K, L = (P[n] for n in names)
        if (J[0] - K[0]) * (L[0] - K[0]) + (J[1] - K[1]) * (L[1] - K[1]) != 0: no(where, "the right angle is not at the second corner")
        if fam == "crossSide":
            m = re.fullmatch(r"Find the length of side ([A-Z])([A-Z])\.", ps)
            if not m or (m.group(1), m.group(2)) != names[:2]: raise ValueError("crossSide: " + ps)
            if J[0] != K[0] and J[1] != K[1]: no(where, "side " + "".join(names[:2]) + " is not along a grid line")
            i = 0 if J[1] == K[1] else 1
            if not crosses(J[i], K[i]): no(where, "the side does not cross an axis")
            return abs(K[i] - J[i]), "units", False
        if ps != f"Find the perimeter of triangle {''.join(names)}. {ROUND}": raise ValueError("perim: " + ps)
        side = lambda A, B: whole_root((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2, where, "a side")
        per = side(J, K) + side(K, L) + side(J, L)
        if per.is_rational: no(where, "a tenth perimeter that is whole")
        return per, "units", True
    if fam in ("streets", "straight"):
        m = re.fullmatch(r"On a town map, each unit is one block\. The ([a-z ]+) is at \((" + NUM + r"), (" + NUM + r")\) and the ([a-z ]+) is at \((" + NUM + r"), (" + NUM + r")\)\.", st)
        if not m: raise ValueError("town: " + st)
        A, B = (q(m.group(2)), q(m.group(3))), (q(m.group(5)), q(m.group(6)))
        on_grid(where, [A, B])
        if not (crosses(A[0], B[0]) or crosses(A[1], B[1])): no(where, "the trip crosses no axis")
        dx, dy = abs(B[0] - A[0]), abs(B[1] - A[1])
        if fam == "streets":
            if ps != f"How far is it from the {m.group(1)} to the {m.group(4)} along the streets?": raise ValueError("streets: " + ps)
            return dx + dy, "blocks", False
        if ps != "How far is it in a straight line?": raise ValueError("straight: " + ps)
        d = whole_root(dx * dx + dy * dy, where, "the straight line")
        if not d.is_integer: no(where, "the straight line is not whole")
        return d, "blocks", False
    if fam == "simSide":
        named = re.fullmatch(r"Triangle ([A-Z])([A-Z])([A-Z]) is similar to triangle ([A-Z])([A-Z])([A-Z])\. Find x\.", st)
        if not named and st != "The two triangles are similar. Find x.": raise ValueError("simSide: " + st)
        f = it["fig"]; la = [q(s) for s in f["la"]]; lb = [None if s == "x" else q(s) for s in f["lb"]]
        if [R(v) for v in f["a"]] != la: no(where, "the first triangle is not drawn to its labels")
        if any(v is not None and abs(R(str(d)) - v) > R(1, 10 ** 9) for v, d in zip(lb, f["b"])): no(where, "the copy is not drawn to its labels")
        if lb.count(None) != 1: raise ValueError("simSide: not one x")
        ra, rb = sorted(la), sorted(range(3), key=lambda i: f["b"][i])     # the copy's sides by the lengths drawn
        if ra[1] ** 2 == ra[0] * ra[2]: no(where, f"sides {ra}: b² = ac, so two of the copy's sides can be matched two ways")
        known = [(lb[i], ra[r]) for r, i in enumerate(rb) if lb[i] is not None]
        ks = {c / o for c, o in known}
        if len(ks) != 1: no(where, f"the copy's known sides give two scale factors {ks}"); return None
        k = ks.pop(); ix = lb.index(None); x = ra[rb.index(ix)] * k
        if abs(R(str(f["b"][ix])) - x) > R(1, 10 ** 6): no(where, f"x is drawn {f['b'][ix]} long, not {x}")
        if k == 1: no(where, "a scale factor of 1")
        if named:
            # the statement's matching, read off the letters the figure prints at each corner (side i runs between the corners
            # ENDS[i]), must give the same x as matching by size
            n1, n2 = list(named.group(1, 2, 3)), list(named.group(4, 5, 6))
            if f.get("na") is None or f.get("nb") is None: no(where, "the words name the triangles and the figure does not"); return x, None, False
            at1, at2 = {c: i for i, c in enumerate(f["na"])}, {c: i for i, c in enumerate(f["nb"])}
            if set(at1) != set(n1) or set(at2) != set(n2): no(where, f"the words name {n1} and {n2}, the figure {f['na']} and {f['nb']}"); return x, None, False
            ENDS = [(0, 2), (1, 2), (0, 1)]
            def side(at, corners):                      # the side between two lettered corners
                c = {at[corners[0]], at[corners[1]]}
                return next(i for i, e in enumerate(ENDS) if set(e) == c)
            match = {}
            for i, e in enumerate(ENDS):                # the copy's side i, between two letters, matches the original's side between theirs
                u, v = f["nb"][e[0]], f["nb"][e[1]]
                match[i] = side(at1, (n1[n2.index(u)], n1[n2.index(v)]))
            kn = {lb[i] / la[match[i]] for i in range(3) if lb[i] is not None}
            if len(kn) != 1: no(where, f"by the names the known sides give two scale factors {kn}"); return x, None, False
            xn = la[match[ix]] * kn.pop()
            if xn != x: no(where, f"by the names x is {xn}, by size {x}")
        return x, None, False
    if fam == "shadow":
        m = re.fullmatch(r"A ([a-z ]+) (" + NUM + r") ft tall casts a shadow (" + NUM + r") ft long\. At the same moment, a ([a-z ]+) casts a shadow (" + NUM + r") ft long\. How tall is the \4\?", st)
        if not m: raise ValueError("shadow: " + st)
        h1, s1, s2 = q(m.group(2)), q(m.group(3)), q(m.group(5))
        if [l["s"] for l in it["figLabels"]][:3] != [m.group(2) + " ft", m.group(3) + " ft", m.group(5) + " ft"]: no(where, "the figure's lengths are not the words'")
        if m.group(1) in ("man", "woman") and h1 < 5: no(where, f"a {m.group(1)} {h1} ft tall")
        return h1 * s2 / s1, "ft", False
    if fam == "mirror":
        m = re.fullmatch(r"([A-Z][a-z]+)’s eyes are (" + NUM + r") ft above the ground\. Standing (" + NUM + r") ft from a mirror on the ground, \1 sees in it the top of a ([a-z ]+) that stands (" + NUM + r") ft beyond the mirror\. The two right triangles are similar\. How tall is the \4\?", st)
        if not m: raise ValueError("mirror: " + st)
        h1, d1, d2 = q(m.group(2)), q(m.group(3)), q(m.group(5))
        if [l["s"] for l in it["figLabels"]][:3] != [m.group(2) + " ft", m.group(3) + " ft", m.group(5) + " ft"]: no(where, "the figure's lengths are not the words'")
        return h1 * d2 / d1, "ft", False
    raise ValueError("no oracle for " + fam)

def check_part(where, it, p):
    got = expect(where, it, p)
    if got is None: return None
    exact, unit, tenth_q = got
    want = tenth(exact) if tenth_q else exact
    if not want.is_rational: no(where, f"the answer {want} is not a number a student can write"); return None
    if p["tenth"] != tenth_q: no(where, "asked to the nearest tenth, but not marked so" if tenth_q else "marked to the tenth, but not asked so")
    kw = words(p["key"])
    m = re.fullmatch(r"(" + NUM + r")(?: (\w+))?", kw)
    if not m: no(where, "the key cannot be read: " + kw); return want
    if q(m.group(1)) != want: no(where, f"the key {kw} ≠ {want}")
    if (m.group(2) or None) != unit: no(where, f"the key's unit {m.group(2)} ≠ {unit}")
    if p["unit"] != unit: no(where, f"the answer box's unit {p['unit']} ≠ {unit}")
    if q(p["keyText"]) != want: no(where, f"what a student types for the key, {p['keyText']}, ≠ {want}")
    if tenth_q and len(m.group(1).split(".")[-1]) != 1: no(where, f"a tenth key without one decimal place: {kw}")
    return want, exact

def check_sol(where, p, want, exact):
    lines = p["sol"]; n = 0
    for i, l in enumerate(lines):
        claims(f"{where} Show me how {i + 1}", l["say"] + (" " + l["h"] if l["h"] else ""))
        m = re.search(r"the hundredths digit is (\d), so the tenths digit (goes up|stays)", words(l["say"]))
        if m:
            d = int(floor(exact * 100)) % 10
            if int(m.group(1)) != d: no(where, f"Show me how says the hundredths digit is {m.group(1)}; it is {d}")
            if (m.group(2) == "goes up") != (d >= 5): no(where, "Show me how rounds the wrong way")
            if (m.group(2) == "goes up") != (tenth(exact) > cut(exact, 1)): no(where, "Show me how's rounding is not the key's")
        if not l["h"]: continue
        n += 1
        ws = words(l["h"])
        try: v = value(re.split(r"\s*=\s*", ws)[-1])
        except Exception as e: no(where, f"worked line {i + 1} cannot be read: {ws}"); continue
        if v != want: no(where, f"worked line {i + 1}, {ws}, ends on {v}, not {want}")
        if l["approx"] != p["tenth"]: no(where, f"worked line {i + 1}: '≈' {'missing' if p['tenth'] else 'on a whole answer'}")
        links = re.split(r"\s*=\s*", ws)
        for a, b in zip(links, links[1:]):
            if sp.simplify(value(a) - value(b)) != 0: no(where, f"worked line {i + 1}: {a} ≠ {b}")
    if not n: no(where, "Show me how never reaches the answer")
    return n

def hint_value(where, it, p, ask):
    """what a Hint number step asks for, from its own words and the question's"""
    a = words(ask); st = words(it["stem"])
    m = re.fullmatch(r"What number times itself is (\d+)\?", a)
    if m:
        r = whole_root(int(m.group(1)), where, "a Hint step")
        if not r.is_integer: raise ValueError("a Hint asks for a whole root of a non-square")
        return r
    m = re.fullmatch(r"What is (?:√\((\d+)\)|the square root of (\d+)), to the nearest tenth\?", a)
    if m: return tenth(whole_root(int(m.group(1) or m.group(2)), where, "a Hint step"))
    m = re.fullmatch(r"How far (across|up|down) is it, from ([xy]) = (" + NUM + r") to \2 = (" + NUM + r")\?", a)
    if m:
        u, v = q(m.group(3)), q(m.group(4))
        if m.group(1) == "up" and not v > u or m.group(1) == "down" and not v < u: no(where, f"Hint: '{a}' goes the wrong way")
        return abs(v - u)
    m = re.fullmatch(r"How far is it from ([xy]) = (" + NUM + r") to \1 = (" + NUM + r")\?", a)
    if m: return abs(q(m.group(3)) - q(m.group(2)))
    m = re.fullmatch(r"How long is ([A-Z])([A-Z])\?", a)
    if m:
        P, _ = corners(st); A, B = P[m.group(1)], P[m.group(2)]
        if A[0] != B[0] and A[1] != B[1]: no(where, f"Hint: {m.group(1)}{m.group(2)} is not along a grid line")
        return abs(A[0] - B[0]) + abs(A[1] - B[1])
    m = re.fullmatch(r"How long is the slanted side ([A-Z])([A-Z]), to the nearest tenth\?", a)
    if m:
        P, _ = corners(st); A, B = P[m.group(1)], P[m.group(2)]
        return tenth(whole_root((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2, where, "a Hint step"))
    fm = re.fullmatch(r"A rectangular [a-z ]+ measures (\d+) \w+ by (\d+) \w+\..*", st)
    if a.startswith("How far is it along two sides of the"):
        return int(fm.group(1)) + int(fm.group(2))
    if a == "How long is the path straight across, to the nearest tenth?":
        return tenth(whole_root(int(fm.group(1)) ** 2 + int(fm.group(2)) ** 2, where, "a Hint step"))
    m = re.fullmatch(r"What is the scale factor, k = (" + NUM + r") ÷ (" + NUM + r")\?", a)
    if m: return q(m.group(1)) / q(m.group(2))
    m = re.fullmatch(r"Choice ([A-E]) \(([^)]*)\): what do its two shorter sides add to\?", a)
    if m:
        k = "ABCDE".index(m.group(1)); opt = words(it["opts"][k])
        if opt != m.group(2): no(where, f"Hint: choice {m.group(1)} is quoted as {m.group(2)}, but it is {opt}")
        s = sorted(q(x) for x in re.findall(NUM, opt)); return s[0] + s[1]
    m = re.fullmatch(r"Choice ([A-E]): what is (\d+)\^2 \+ (\d+)\^2\?", a)
    if m:
        s = sorted(q(x) for x in re.findall(NUM, words(it["opts"]["ABCDE".index(m.group(1))])))
        if [s[0], s[1]] != [q(m.group(2)), q(m.group(3))]: no(where, f"Hint: {m.group(2)} and {m.group(3)} are not choice {m.group(1)}'s two shorter sides")
        return q(m.group(2)) ** 2 + q(m.group(3)) ** 2
    m = re.fullmatch(r"Three of the choices begin with (" + NUM + r"), the match for (\d+)\. What is k = \1 ÷ \2\?", a)
    if m:
        firsts = [re.findall(NUM, words(o))[0] for o in it["opts"]]
        if firsts.count(m.group(1)) != 3: no(where, f"Hint: {firsts.count(m.group(1))} of the choices begin with {m.group(1)}, not three")
        t = sorted(q(x) for x in re.findall(r"\d+", re.search(r"sides (.*)\?", st).group(1)))
        if q(m.group(2)) != t[0]: no(where, f"Hint: {m.group(2)} is not the first triangle's shortest side")
        return q(m.group(1)) / q(m.group(2))
    m = re.fullmatch(r"(?:Then|And) (\d+) becomes \1 × (" + NUM + r"|\(\d+÷\d+\))\. What is \1 × \2\?", a)
    if m: return q(m.group(1)) * value(m.group(2))
    m = re.fullmatch(r"(?:How long must the third side be, at least, to reach\? |How long can it be, at most, to be covered\? )?What is (.+)\?", a)
    if m: return value(m.group(1))
    raise ValueError("a Hint question this check cannot read: " + a)

def check_walk(where, it, p, steps, want):
    n = 0
    for i, s in enumerate(steps):
        n += 1
        ans = R(*[int(x) for x in s["ans"].split("/")])
        try: v = hint_value(where, it, p, s["ask"])
        except Exception as e: no(where, f"Hint step {i + 1}: {e}"); continue
        if v != ans: no(where, f"Hint step '{words(s['ask'])}' is {v}, not {ans}")
    if p is not None and steps and R(*[int(x) for x in steps[-1]["ans"].split("/")]) != want: no(where, "the Hint does not end on the answer")
    return n

def opts_nums(it): return [[q(x) for x in re.findall(NUM, words(o))] for o in it["opts"]]
def check_mc(where, it):
    st, fam, corr = words(it["stem"]), it["fam"], it["correct"]
    if len(set(it["opts"])) != len(it["opts"]): no(where, "two options the same")
    if fam == "triSet":
        if st != "Which set of side lengths can form a triangle?": raise ValueError("triSet: " + st)
        units = {re.sub(r"[\d.\s,]", "", words(o)) for o in it["opts"]}
        if len(units) != 1: no(where, f"the choices' units differ: {units}")
        ok = [i for i, s in enumerate(opts_nums(it)) if sorted(s)[0] + sorted(s)[1] > sorted(s)[2]]
        if ok != [corr]: no(where, f"the sets that make a triangle are {ok}, the key {corr}")
        if not any(sorted(s)[0] + sorted(s)[1] == sorted(s)[2] for s in opts_nums(it)): no(where, "no set lies flat")
    elif fam == "range":
        m = re.fullmatch(r"Two sides of a triangle are (\d+) (\w+) and (\d+) \2 long\. Which inequality shows every possible length x, in (\w+), of the third side\?", st)
        if not m or m.group(2) not in ABBR or m.group(4) != m.group(2): raise ValueError("range: " + st)
        a, b = int(m.group(1)), int(m.group(3)); good = []
        for i, o in enumerate(it["opts"]):
            mo = re.fullmatch(r"(\d+) (<|≤) x (<|≤) (\d+)", words(o))
            if not mo: raise ValueError("range option: " + words(o))
            if int(mo.group(1)) == abs(b - a) and int(mo.group(4)) == a + b and mo.group(2) == mo.group(3) == "<": good.append(i)
        if good != [corr]: no(where, f"the right inequality is option {good}, the key {corr}")
    elif fam == "eqChoice":
        if st != "Which equation can be used to find x?": raise ValueError("eqChoice: " + st)
        f = it["fig"]; legs = [s for s in f["labs"][:2]]; hyp = q(f["labs"][2])
        if legs.count("x") != 1: raise ValueError("eqChoice: the legs are not a number and x")
        a = q([s for s in legs if s != "x"][0]); x = sp.Symbol("x", positive=True)
        xdrawn = R(str(f["legs"][legs.index("x")]))
        if abs(sqrt(hyp ** 2 - a ** 2) - xdrawn) > R(1, 10 ** 9): no(where, "x is not drawn to the length the theorem gives")
        good = []
        for i, o in enumerate(it["opts"]):
            L, Rr = words(o).split("=")
            sol = sp.solve(sp.Eq(eval_x(L), eval_x(Rr)), x)
            if sol == [sqrt(hyp ** 2 - a ** 2)] and re.fullmatch(r"\s*(\d+)\^2 \+ x\^2 = (\d+)\^2\s*", words(o)): good.append(i)
        if good != [corr]: no(where, f"the equation that finds x is option {good}, the key {corr}")
    elif fam == "simChoice":
        m = re.fullmatch(r"Which triangle is similar to a triangle with sides (\d+), (\d+) and (\d+)\?", st)
        if not m: raise ValueError("simChoice: " + st)
        t = sorted(int(g) for g in m.groups()); good = []
        for i, s in enumerate(opts_nums(it)):
            if s != sorted(s): no(where, f"choice {'ABCD'[i]} lists its sides out of order: {s}")
            r = {v / o for v, o in zip(sorted(s), t)}
            if len(r) == 1 and r != {1}: good.append(i)
        if good != [corr]: no(where, f"the similar choice is {good}, the key {corr}")
    else:
        raise ValueError("no oracle for " + fam)
def eval_x(e):
    """an equation side with x in it, as sympy"""
    x = sp.Symbol("x", positive=True)
    s = e.strip().replace("−", "-").replace("·", "*").replace("×", "*").replace("^", "**")
    s = re.sub(r"(\d)\s*x", r"\1*x", s)
    s = re.sub(r"\d+(?:\.\d+)?", lambda m: f"R('{m.group(0)}')", s)
    return eval(s, {"R": R, "x": x, "__builtins__": {}})

def check_multi(where, it):
    if words(it["stem"]) != "Select ALL of the sets of side lengths that make a right triangle.": raise ValueError("rightSel: " + words(it["stem"]))
    S = opts_nums(it)
    right = [i for i, s in enumerate(S) if sorted(s)[0] ** 2 + sorted(s)[1] ** 2 == sorted(s)[2] ** 2]
    if right != sorted(it["correct"]): no(where, f"the right triangles are {right}, the key {sorted(it['correct'])}")
    if not 1 <= len(right) <= 3: no(where, f"{len(right)} right triangles of five")
    if not any(S[i][0] == max(S[i]) for i in right): no(where, "no right set lists its longest side first")

# ---------------------------------------------------------------- run
n_parts = n_lines = n_mc = n_steps = 0
for G in DUMP["sets"]:
    seed = G["seed"]
    for it in G["items"]:
        where = f"{seed} Q{it['q']}"
        try:
            claims(where + " stem", it["stem"])
            if it["type"] in ("mc", "multi"):
                (check_mc if it["type"] == "mc" else check_multi)(where, it); n_mc += 1
                for i, l in enumerate(it.get("sol") or []): claims(f"{where} Show me how {i + 1}", l)
                n_steps += check_walk(where, it, None, it.get("walk") or [], None)
                continue
            for p in it["parts"]:
                w = where + p["label"]
                got = check_part(w, it, p)
                if not got: continue
                want, exact = got; n_parts += 1
                n_lines += check_sol(w, p, want, exact)
                n_steps += check_walk(w, it, p, p["walk"], want)
                claims(w + " rule", p["rule"])
                for m in p["models"]:
                    claims(w + " mistake", m["say"])
                    mv = R(*[int(x) for x in m["v"].split("/")]) if m["v"] else None
                    if mv is not None and mv == want: no(w, "a modelled mistake is worth the answer: " + words(m["say"]))
                    if m["f"] is not None and abs(m["f"] - float(want)) < 0.1: no(w, "a modelled mistake comes to the answer: " + words(m["say"]))
        except Exception as e:
            no(where, f"could not check: {e!r}")

# ---------------------------------------------------------------- the test itself: the practice is its blueprint (ruling 49)
SPEC = os.path.join(HERE, "..", "..", "build", "u6", "unit.py")
sys.path.insert(0, os.path.dirname(SPEC))
U = runpy.run_path(SPEC)["U"]
paper = U["assessment"]["forms"]["practice"]
if [s["title"] for s in paper] != DUMP["TITLES"]: no("the test", f"its sections {[s['title'] for s in paper]} are not the practice's {DUMP['TITLES']}")
kind = lambda it: "multi" if isinstance(it.get("correct"), list) else "mc" if "choices" in it else "parts" if "parts" in it else "solo"
test_shape = [(kind(it), len(it.get("parts", [])) or 1) for s in paper for it in s["items"]]
pts = sum(n for _, n in test_shape)
if pts != U["assessment"]["total"]: no("the test", f"its points add to {pts}, not its total {U['assessment']['total']}")
for G in DUMP["sets"][:50]:
    mine = [(it["type"], len(it["parts"]) if it["type"] == "parts" else 1) for it in G["items"]]
    if mine != test_shape: no(f"{G['seed']}", f"the set's questions {mine} are not the test's {test_shape}")

print(f"{len(DUMP['sets'])} sets: {n_parts} typed parts worked out again, {n_lines} worked lines and {n_steps} Hint steps read back, "
      f"{n_mc} choice questions re-marked, {n_claims} arithmetic claims re-derived; the test's {len(test_shape)} questions and {pts} points matched: "
      + ("ALL SOUND" if not bad else f"{len(bad)} PROBLEMS"))
for b in bad[:40]:
    print("  " + b)
sys.exit(1 if bad else 0)
