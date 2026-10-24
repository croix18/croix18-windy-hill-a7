"""A7 Unit 4 practice: the independent check.   python3 verify.py   (reads dump.json, written by u4_check.js)
Written 21 Oct 2026. The engine's arithmetic is not trusted here: every question is read back from the HTML the student sees
and worked out again in exact rationals (Python's own parser and fractions, nothing of the engine's), then compared with the
key the page marks against. Every worked line of Show me how and every Hint step is read back the same way. And the test
itself (a7/build/u4/unit.py, Forms A and B) is read from its TeX: every one of its questions must be in the engine's
exclusion list, and no practice part may print the numbers of the test's part in its position."""
import ast, json, os, re, runpy, sys
from fractions import Fraction as R
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
DUMP = json.load(open(os.path.join(HERE, "dump.json"), encoding="utf-8"))
bad = []
def no(where, msg):
    bad.append(f"{where}: {msg}")

# ---------------------------------------------------------------- exact arithmetic on what is printed
def iroot(n, k):
    r = round(abs(n) ** (1 / k))
    for c in (r - 1, r, r + 1):
        if c >= 0 and c ** k == abs(n): return c if n >= 0 else -c
    raise ValueError(f"{n} has no whole {k}th root")
def ev(node):
    if isinstance(node, ast.Expression): return ev(node.body)
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        f = node.func.id
        if f == "N": return R(node.args[0].value)
        a = [ev(x) for x in node.args]
        if f == "sqrt":
            if a[0] < 0: raise ValueError("square root of a negative number")
            return R(iroot(a[0].numerator, 2), iroot(a[0].denominator, 2))
        if f == "cbrt": return R(iroot(a[0].numerator, 3), iroot(a[0].denominator, 3))
        raise ValueError("unknown function " + f)
    if isinstance(node, ast.BinOp):
        l, r = ev(node.left), ev(node.right)
        if isinstance(node.op, ast.Add): return l + r
        if isinstance(node.op, ast.Sub): return l - r
        if isinstance(node.op, ast.Mult): return l * r
        if isinstance(node.op, ast.Div): return l / r
        if isinstance(node.op, ast.Pow):
            if r.denominator != 1: raise ValueError("a fractional exponent")
            return l ** int(r)
    if isinstance(node, ast.UnaryOp):
        x = ev(node.operand)
        if isinstance(node.op, ast.USub): return -x
        if isinstance(node.op, ast.UAdd): return x
    raise ValueError("cannot read " + ast.dump(node)[:60])
def num(s):
    """the exact value of an expression in + − × ÷, powers, sqrt() and cbrt(), every numeral read exactly"""
    s = re.sub(r"\d+(?:\.\d+)?", lambda m: f"N('{m.group(0)}')", s)
    return ev(ast.parse(s, mode="eval"))

# ---------------------------------------------------------------- the page's HTML math, read back
class Node:
    def __init__(self, tag, attrs):
        self.tag, self.cls, self.kids = tag, dict(attrs).get("class", ""), []
class Tree(HTMLParser):
    def __init__(self):
        super().__init__(); self.root = Node("root", []); self.stack = [self.root]
    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs); self.stack[-1].kids.append(n); self.stack.append(n)
    def handle_endtag(self, tag):
        if len(self.stack) > 1: self.stack.pop()
    def handle_data(self, d):
        self.stack[-1].kids.append(d)
def tree(h):
    t = Tree(); t.feed(h); t.close(); return t.root
def sym(n):
    """a math node → an expression Python can read"""
    if isinstance(n, str):
        s = n.replace("\u00a0", " ").replace("×", "*").replace("·", "*").replace("÷", "/").replace("−", "-")
        return re.sub(r"(?<=\d),(?=\d{3})", "", s)
    k = n.kids
    if n.tag == "span" and n.cls == "fr":
        nu = next(x for x in k if not isinstance(x, str) and x.cls == "nu"); de = next(x for x in k if not isinstance(x, str) and x.cls == "de")
        return "((" + sym(nu) + ")/(" + sym(de) + "))"
    if n.tag == "span" and n.cls.startswith("rad"):
        rc = next(x for x in k if not isinstance(x, str) and x.cls == "rc")
        cube = any(not isinstance(x, str) and x.tag == "sup" and x.cls == "ri" for x in k)
        return ("cbrt(" if cube else "sqrt(") + sym(rc) + ")"
    if n.tag == "sup":
        return "**(" + "".join(sym(x) for x in k) + ")"
    return "".join(sym(x) for x in k)
def implicit(s):
    s = re.sub(r"\)\s*\(", ")*(", s)
    s = re.sub(r"(\d)\s*\(", r"\1*(", s)
    s = re.sub(r"\)\s*(\d)", r")*\1", s)
    return s
def val(h):
    return num(implicit(sym(tree(h))))
def segments(h, syms=None):
    """text with each math span replaced by §i§, and the values of those spans (None where a span is not a number, like x = −3)"""
    vals, out = [], []
    def walk(n):
        if isinstance(n, str): out.append(n.replace("\u00a0", " ")); return
        if n.tag == "span" and n.cls == "m":
            s_ = implicit(sym(n))
            if syms is not None: syms.append(s_)
            try: vals.append(num(s_))
            except Exception: vals.append(None)
            out.append(f"§{len(vals) - 1}§"); return
        for x in n.kids: walk(x)
    walk(tree(h))
    return re.sub(r"\s+", " ", "".join(out)).strip(), vals
def plain(h):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()
def first_math(h):
    found = []
    def find(n):
        if isinstance(n, str) or found: return
        if n.tag == "span" and n.cls == "m": found.append(n); return
        for x in n.kids: find(x)
    find(tree(h))
    return found[0] if found else None
def sci_key(h):
    """a key like '3.24 × 10⁴ square millimeters': (value, coefficient, exponent)"""
    span = first_math(h)
    m = span is not None and re.fullmatch(r"\s*(-?[\d.]+) \* 10\*\*\((-?\d+)\)\s*", sym(span))
    if not m: return None
    c = R(m.group(1)); return c * R(10) ** int(m.group(2)), c, int(m.group(2))
TEN = R(10)

# ---------------------------------------------------------------- each question, worked out again from what it prints
def expect(it, p):
    """the value a typed part's key must have, from the printed question alone"""
    st, v = segments(p["stem"]); fam = p["fam"]
    if fam in ("addSame", "subSame", "addCarry", "addGap", "mulInt", "mulAdj", "divDec", "divAdj",
               "ooA", "ooB", "ooC", "ooD", "radA", "radB", "radC"):
        if st != "§0§": raise ValueError("the part is not one expression: " + st)
        return v[0]
    if fam == "rate":
        st, v = segments(it["stem"])
        if not re.fullmatch(r"(A laser emits|A pump moves|A web server answers|A factory machine makes) §0§ (photons|drops of water|requests|tiny beads) each second\. How many does it (emit|move|answer|make) in §1§ seconds\? Write your answer in scientific notation\.", st):
            raise ValueError("rate question: " + st)
        return v[0] * v[1]
    if fam == "rwArea":
        if not re.fullmatch(r"A rectangular plate measures §0§ mm by §1§ mm\. Find its area\.", st): raise ValueError("area: " + st)
        return v[0] * v[1]
    if fam == "rwSpeed":
        m = re.fullmatch(r"A vehicle travels §0§ km in (\d+) hours\. Find its average speed\.", st)
        if not m: raise ValueError("speed: " + st)
        return v[0] / int(m.group(1))
    if fam == "rwSum":
        if not re.fullmatch(r"Two lengths are measured: §0§ mm and §1§ mm\. Find their sum\.", st): raise ValueError("sum: " + st)
        return v[0] + v[1]
    if fam == "rwDiff":
        if not re.fullmatch(r"Two masses are measured: §0§ g and §1§ g\. Find their difference\.", st): raise ValueError("difference: " + st)
        if not v[0] > v[1]: raise ValueError("the difference is negative")
        return v[0] - v[1]
    if fam in ("patioExpr", "patioCost"):
        m = re.fullmatch(r"A square patio has sides of (\d+) feet\. Sealing it costs \$(\d+\.\d\d) per square foot, plus a \$(\d+) delivery fee\.", plain(it["stem"]))
        if not m: raise ValueError("patio: " + plain(it["stem"]))
        s, r, f = int(m.group(1)), R(m.group(2)), int(m.group(3))
        return s * s * r + f
    if fam == "negSub":
        sm = []; st, v = segments(it["stem"], sm)
        a = re.fullmatch(r"(\d+)([a-z])\*\*\(2\)", sm[0]); b = re.fullmatch(r"([a-z]) = -(\d+)", sm[1])
        if not (st == "Evaluate §0§ when §1§." and a and b and a.group(2) == b.group(1)): raise ValueError("negSub: " + st + " " + repr(sm))
        return int(a.group(1)) * int(b.group(2)) ** 2
    raise ValueError("no oracle for " + fam)

def typed_value(t):
    m = re.fullmatch(r"(-?[\d.]+) x 10\^(-?\d+)", t)
    return R(m.group(1)) * TEN ** int(m.group(2)) if m else None
def check_key(where, p, want):
    k = p["kind"]
    if k == "sci":
        got = sci_key(p["key"])
        if not got: no(where, "the key is not c × 10^k: " + plain(p["key"])); return
        v, c, e = got
        if v != want: no(where, f"key {plain(p['key'])} ≠ {want}")
        if not (1 <= abs(c) < 10): no(where, f"key coefficient {c} is not at least 1 and less than 10")
        if typed_value(p["keyText"]) != want: no(where, f"what a student types for the key, {p['keyText']}, ≠ {want}")
    elif k == "money":
        m = re.fullmatch(r"([\d,]+(?:\.\d\d)?) dollars", plain(p["key"]))      # whole dollars, or dollars and cents
        if not m or R(m.group(1).replace(",", "")) != want: no(where, f"money key {plain(p['key'])} ≠ {want}")
    elif k == "expr":
        if val(p["key"]) != want: no(where, f"expression key {plain(p['key'])} is worth {val(p['key'])}, not {want}")
        if not re.fullmatch(r"\s*(\d+)\*\*\(2\)\*\((\d+\.\d\d)\) \+ (\d+)\s*", implicit(sym(tree(p["key"])))): no(where, "the expression key is not side²(rate) + fee")
    else:
        if val(p["key"]) != want: no(where, f"key {plain(p['key'])} ≠ {want}")

def check_mc(where, it):
    st, v = segments(it["stem"]); fam = it["fam"]; opts = it["opts"]; corr = it["correct"]
    if fam == "mcGap":
        if not re.fullmatch(r"Which is the value of §0§ ?\?", st): raise ValueError("mcGap: " + st)
        right = [i for i, o in enumerate(opts) if val(o) == v[0]]
        if right != [corr]: no(where, f"options worth the value {right}, key {corr}")
        for o in opts:
            g = sci_key(o)
            if not g or not (1 <= abs(g[1]) < 10): no(where, "an option is not in scientific notation: " + plain(o))
    elif fam == "mcOrder":
        if not re.fullmatch(r"Which is the value of §0§ ?\?", st): raise ValueError("mcOrder: " + st)
        right = [i for i, o in enumerate(opts) if R(plain(o)) == v[0]]
        if right != [corr]: no(where, f"options worth the value {right}, key {corr}")
    elif fam == "kendra":
        if not re.fullmatch(r"(\w+) writes §0§ = §1§\. Which gives the correct sum and names the mistakes\?", st): raise ValueError("kendra: " + st)
        good = []
        for i, o in enumerate(opts):
            os_, ov = segments(o)
            if ov and ov[0] == v[0] and os_ == "§0§: the powers weren’t matched before adding, and the exponents were added.": good.append(i)
        if good != [corr]: no(where, f"options with the right sum and both mistakes {good}, key {corr}")
        two = re.findall(r"\(([\d.]+) \* 10\*\*\((-?\d+)\)\)", implicit(sym(first_math(it["stem"]))))
        if len(two) != 2: raise ValueError("kendra: the sum is not two numbers")
        (a, ka), (b, kb) = two
        if v[1] != (R(a) + R(b)) * TEN ** (int(ka) + int(kb)): no(where, "the claimed sum is not the two named mistakes")
        if abs(int(ka) - int(kb)) > 2: no(where, "a sum with exponents more than 2 apart")
    elif fam == "nadia":
        m = re.fullmatch(r"(\w+) writes §0§ = §1§ = (\d+)\. Which explains the mistake and gives the correct value\?", st)
        if not m: raise ValueError("nadia: " + st)
        good = [i for i, o in enumerate(opts) if plain(o).startswith("Add under the bar first:") and R(re.findall(r"= (\d+)\.$", plain(o))[0]) == v[0]]
        if good != [corr]: no(where, f"the option that adds first and gets {v[0]}: {good}, key {corr}")
        if v[1] != int(m.group(2)) or v[0] == v[1]: no(where, "the student's line is not what is claimed")
    else:
        raise ValueError("no oracle for " + fam)

def check_multi(where, it):
    st, v = segments(it["stem"])
    if it["fam"] == "selSci":
        if not re.fullmatch(r"Select ALL of the expressions whose value is §0§\.", st): raise ValueError("selSci: " + st)
        target = v[0]
    else:
        m = re.fullmatch(r"Select ALL of the expressions whose value is (\d+)\.", st)
        if not m: raise ValueError("selVal: " + st)
        target = int(m.group(1))
    right = sorted(i for i, o in enumerate(it["opts"]) if val(o) == target)
    if right != sorted(it["correct"]): no(where, f"options worth {target}: {right}, key {sorted(it['correct'])}")
    if len(right) != 4: no(where, f"{len(right)} right options, not 4")

def check_walk(w, p, want):
    n = 0
    for i, st in enumerate(p.get("walk") or []):
        n += 1
        ans = R(*[int(x) for x in st["ans"].split("/")]); ask = st["ask"]
        m3 = re.fullmatch(r"(.+) = ([\d.,−]+) × 10<sup>\?</sup>\. What is the new exponent\?", ask, re.S)
        m2 = re.fullmatch(r"What number times itself is (\d+)\?", ask)
        m = re.fullmatch(r"What is (?:the area, )?(.+)\?(?: \(A fraction is fine\.\))?", ask, re.S)
        if m3:
            if R(m3.group(2).replace(",", "").replace("−", "-")) * TEN ** int(ans) != val(m3.group(1)): no(w, f"Hint: {plain(ask)} is not {ans}")
        elif m2:
            if ans < 0 or ans * ans != int(m2.group(1)): no(w, f"Hint: {plain(ask)} is not {ans}")
        elif m:
            got = val(m.group(1))
            if got != ans: no(w, f"Hint: {plain(ask)} is {got}, not {ans}")
        else:
            no(w, "a Hint question this check cannot read: " + plain(ask))
        if st.get("then") and val(st["then"]) != want: no(w, f"Hint step {i + 1} leads to {plain(st['then'])}, not the answer")
    return n

n_parts = n_lines = n_mc = n_steps = 0
for G in DUMP["sets"]:
    seed = G["seed"]
    for it in G["items"]:
        where = f"{seed} Q{it['q']}"
        try:
            if it["type"] == "mc": check_mc(where, it); n_mc += 1; continue
            if it["type"] == "multi": check_multi(where, it); n_mc += 1; continue
            for p in it["parts"]:
                w = where + p["label"]; want = expect(it, p); n_parts += 1
                check_key(w, p, want)
                for i, h in enumerate(p["sol"]):
                    n_lines += 1
                    if val(h) != want: no(w, f"worked line {i + 1}, {plain(h)}, is worth {val(h)}, not {want}")
                n_steps += check_walk(w, p, want)
        except Exception as e:
            no(where, f"could not check: {e!r}")

# ---------------------------------------------------------------- the test forms, from their TeX
U = runpy.run_path(os.path.join(HERE, "..", "..", "build", "u4", "unit.py"))["U"]
SCI = re.compile(r"(\d+(?:\.\d+)?) \\times 10\^\{(-?\d+)\}")
def flat(sections):
    return [it for s in sections for it in s["items"] if not it.get("heading")]
def tuples(q, it):
    """the test question at position q, as the engine's exclusion list writes it: [(family, tuple)]"""
    st = it["stem"]; P = it.get("parts", [])
    sc = lambda s: [(c, int(k)) for c, k in SCI.findall(s)]
    two = lambda s: (lambda x: [x[0][0], x[0][1], x[1][0], x[1][1]])(sc(s))
    if q == 1: return [(f, two(p["stem"])) for f, p in zip(("addSame", "subSame", "addCarry", "addGap"), P)]
    if q == 2: return [(f, two(p["stem"])) for f, p in zip(("mulInt", "divDec", "mulAdj", "divAdj"), P)]
    if q == 3: return [("mcGap", two(st))]
    if q == 4: return [("selSci", [sc(st)[0][0], sc(st)[0][1]])]
    if q == 5: return [("kendra", two(st.split("=")[0]))]
    if q == 6: return [("rate", two(st))]
    if q == 7:
        a = sc(P[0]["stem"]); b = re.search(r"\$(\d+(?:\.\d+)?) \\times 10\^\{2\}\$ km in (\d+) hours", P[1]["stem"])
        return [("rwArea", [a[0][0], a[1][0]]), ("rwSpeed", [b.group(1), int(b.group(2))])]
    if q == 8: return [("rwSum", [x[0] for x in sc(P[0]["stem"])]), ("rwDiff", [x[0] for x in sc(P[1]["stem"])])]
    if q == 9:
        a = re.fullmatch(r"\$(\d+) - (\d+) \\cdot (\d+)\^\{2\}\$", P[0]["stem"])
        b = re.fullmatch(r"\$\\frac\{(\d+)\^\{2\} \+ (\d+)\}\{(\d+)(?:\^\{3\})?\}\$", P[1]["stem"])
        c = re.fullmatch(r"\$(\d+) \\div (\d+) \\cdot (\d+)\$", P[2]["stem"])
        d = re.fullmatch(r"\$-(\d+)\^\{2\} [+-] \(-(\d+)\)\^\{2\}\$", P[3]["stem"])
        return [(f, [int(x) for x in m.groups()]) for f, m in zip(("ooA", "ooB", "ooC", "ooD"), (a, b, c, d))]
    if q == 10:
        a = re.fullmatch(r"\$\\sqrt\{(\d+)\^\{2\} \+ (\d+)\}\$", P[0]["stem"])
        b = re.fullmatch(r"\$\\sqrt\[3\]\{-(\d+)\} \+ (\d+)\^\{-2\}\$", P[1]["stem"])
        c = re.fullmatch(r"\$\\left\(-\\frac\{1\}\{(\d+)\}\\right\)\^\{2\} \+ \\sqrt\{\\frac\{(\d+)\}\{(\d+)\}\}\$", P[2]["stem"])
        return [("radA", [int(a.group(1)), int(a.group(2))]), ("radB", [iroot(int(b.group(1)), 3), int(b.group(2))]),
                ("radC", [int(c.group(1)), iroot(int(c.group(2)), 2), iroot(int(c.group(3)), 2)])]
    if q == 11:
        m = re.search(r"side (\d+) feet is sealed at (\d+\.\d\d) dollars a square foot, with a flat (\d+) dollars", st)
        return [("patio", [int(m.group(1)), m.group(2), int(m.group(3))])]
    if q == 12:
        m = re.search(r"\$(\d+) \+ (\d+) \\cdot (\d+)\^\{2\}\$", st); return [("mcOrder", [int(x) for x in m.groups()])]
    if q == 13: return [("selVal", [int(re.search(r"value is\s+(\d+)\.", st).group(1))])]
    if q == 14:
        m = re.search(r"\\sqrt\{(\d+) \+ (\d+)\}", st); return [("nadia", [iroot(int(m.group(1)), 2), iroot(int(m.group(2)), 2)])]
    return []                       # 15: the transfer item, which the practice replaces with its own stand-in
T = DUMP["TEST"]
canon = lambda t: json.dumps([str(x) for x in t])
n_test = 0
for form in ("A", "B"):
    items = flat(U["assessment"]["forms"][form])
    if len(items) != 15: no(f"Form {form}", f"{len(items)} questions; the practice has 15")
    for q, it in enumerate(items, 1):
        try:
            for fam, t in tuples(q, it):
                n_test += 1
                have = {canon(x if isinstance(x, list) else [x]) for x in T.get(fam, [])}
                swapped = (t[2:] + t[:2]) if len(t) == 4 else t[::-1]
                if canon(t) not in have and not (fam in ("rwArea", "mulInt", "mulAdj") and canon(swapped) in have):
                    no(f"Form {form} Q{q}", f"{fam} {t} is not in the engine's exclusion list")
        except Exception as e:
            no(f"Form {form} Q{q}", f"could not read the test question: {e!r}")
# no practice part prints the numbers of the test's part in its position: the numbers in the order they are printed (a number in
# scientific notation counts as one number, every other numeral, exponents too, as itself; signs aside), and in any order where
# the question is a sum or a product, which reads the same backwards
TEXNUM = re.compile(r"(\d+(?:\.\d+)?) \\times 10\^\{(-?\d+)\}|(\d+(?:\.\d+)?)")
PAGENUM = re.compile(r"(\d+(?:\.\d+)?) \* 10\*\*\((-?\d+)\)|(\d+(?:\.\d+)?)")
def seq(t, rx):
    return [R(m.group(1)) * TEN ** int(m.group(2)) if m.group(1) else R(m.group(3)) for m in rx.finditer(t)]
def per_part(stem_nums, parts_nums):
    return [stem_nums + pn for pn in (parts_nums or [[]])]
COMMUTE = {(1, 0), (1, 2), (1, 3), (2, 0), (2, 2), (3, 0), (5, 0), (6, 0), (7, 0), (8, 0), (14, 0)}
tests = {f: [per_part(seq(it["stem"], TEXNUM), [seq(p["stem"], TEXNUM) for p in it.get("parts", [])]) for it in flat(U["assessment"]["forms"][f])] for f in ("A", "B")}
n_cmp = 0; hits = []
for G in DUMP["sets"]:
    for it in G["items"]:
        try:
            pg = lambda h: seq(sym(tree(h)), PAGENUM)
            mine = per_part(pg(it["stem"]), [pg(p["stem"]) for p in it["parts"]] if it["type"] == "parts" else None)
            for f in ("A", "B"):
                theirs = tests[f][it["q"] - 1]
                for j, m in enumerate(mine):
                    if not m or j >= len(theirs): continue
                    n_cmp += 1
                    a_, b_ = [abs(x) for x in m], [abs(x) for x in theirs[j]]
                    if a_ == b_ or ((it["q"], j) in COMMUTE and sorted(a_) == sorted(b_)):
                        hits.append(f"{G['seed']} Q{it['q']} part {j + 1} = Form {f}")   # the page excludes nothing (24 Oct 2026): counted, and capped below
        except Exception as e:
            no(f"{G['seed']} Q{it['q']}", f"could not read its numbers: {e!r}")

# a part whose printed numbers are a test part's: rare by the variety floor (ruling 49), never zero now that the page carries
# no exclusion list (P0, 24 Oct 2026). The cap is per part compared, as the floor is: above 2 % a part's numbers are too few.
# (24 Oct, this unit: 240 of 34,800 parts, 0.7 %; a third of sets hold one such part of their 29 — Part 3's small spaces.)
hit_sets = {h.split(" ")[0] for h in hits}
if n_cmp and len(hits) > 0.02 * n_cmp: no("test questions", f"{len(hits)} of {n_cmp} parts compared print a test part's numbers: " + "; ".join(hits[:8]))
print(f"{len(hits)} of {n_cmp} parts compared print a test part's numbers ({len(hit_sets)} of {len(DUMP['sets'])} sets hold one)")
print(f"{len(DUMP['sets'])} sets: {n_parts} typed parts re-derived, {n_lines} worked lines and {n_steps} Hint steps read back, "
      f"{n_mc} choice questions re-marked; {n_test} test questions found in the exclusion list, {n_cmp} parts compared with the test: "
      + ("ALL SOUND" if not bad else f"{len(bad)} PROBLEMS"))
for b in bad[:40]:
    print("  " + b)
sys.exit(1 if bad else 0)
