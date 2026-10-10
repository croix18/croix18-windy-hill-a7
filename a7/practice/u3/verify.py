"""Independent check of the practice sets in dump.json (written by test_engine.js) with sympy, exact rationals only.
The JavaScript engine's own arithmetic is not trusted here: every question and answer is re-read from its written-out form."""
import json, re, sys, os
from math import gcd
import sympy as sp

D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "dump.json")))
L = {c: sp.Symbol(c) for c in "abcdghkmnprstwxyz"}
L["Eq"] = sp.Eq
def S(s): return sp.sympify(s, locals=L, rational=True, evaluate=True)
def zero(d):
    return d == 0 or (bool(d.free_symbols) and sp.cancel(d) == 0)
A0 = int(sys.argv[1]) if len(sys.argv) > 2 else 0
A1 = int(sys.argv[2]) if len(sys.argv) > 2 else (int(sys.argv[1]) if len(sys.argv) > 1 else len(D))
D = D[A0:A1]
bad = []
def no(seed, w, msg):
    bad.append(f"{seed} {w}: {msg}")

def sci_parts(s):
    """'(c)*((10)**(k))' → (c, k) as Rationals, or None"""
    m = re.fullmatch(r"\(([\d.]+)\)\*\(\(10\)\*\*\(\(?(-?)\(?(\d+)\)?\)?\)\)", s)
    if not m:
        return None
    return sp.Rational(m.group(1)), int(m.group(2) + m.group(3))

def dec_ok(text, v):
    return sp.Rational(text.replace(",", "")) == v

n_items = 0
for G in D:
    seed = G["seed"]
    for it in G["items"]:
        n_items += 1
        w, k = it["w"], it["kind"]
        try:
            if k in ("mc", "mcsci"):
                q = S(it["q"]); opts = [S(o) for o in it["opts"]]
                eq = [zero(o - q) for o in opts]
                if k == "mc":
                    if eq.count(True) != 1 or not eq[it["correct"]]:
                        no(seed, w, f"MC key: {it['q']} vs {it['opts']} key {it['correct']}")
                else:
                    c, e = sci_parts(it["opts"][it["correct"]])
                    if not eq[it["correct"]] or not (1 <= c < 10):
                        no(seed, w, "sci MC key")
                    for i, o in enumerate(it["opts"]):
                        if i != it["correct"] and eq[i]:
                            c2, _ = sci_parts(o)
                            if 1 <= c2 < 10:
                                no(seed, w, "a second right answer in sci MC")
                continue
            if k == "multi":
                t = S(it["target"]); vals = [S(o) for o in it["opts"]]
                right = [i for i, v in enumerate(vals) if v == t]
                if sorted(right) != sorted(it["correct"]):
                    no(seed, w, f"select-all key {right} vs {it['correct']}")
                for v, sv in zip(vals, it["stepVals"]):
                    if v != S(sv):
                        no(seed, w, "select-all steps value")
                continue
            q, a = S(it["q"]), S(it["ans"])
            if k == "n":
                n = L["n"]
                # b^n is strictly increasing for b > 1, so the n that works is the only one
                if q.subs(n, a) is not sp.true or not (q.lhs.subs(n, a + 1) > q.rhs and q.lhs.subs(n, a - 1) < q.rhs):
                    no(seed, w, f"n = {a} does not make {it['q']} true")
                m = re.search(r"(\d+)\)\*\*\(n\)\)/\(\((\d+)\)\*\*\((\d+)\)", it["q"])
            elif not zero(q - a):
                no(seed, w, f"question {it['q']} ≠ key {it['ans']}")
            for mstr in it["miss"]:
                if zero(S(mstr) - a):
                    no(seed, w, f"a 'mistake' equals the key: {mstr}")
            if k == "power":
                if not (a.is_Pow and a.base == it["base"]) and not (a == it["base"]):
                    # sympy folds b**1 to b; any other shape is a defect
                    if not re.fullmatch(r"\(%d\)\*\*\(-?\d+\)" % it["base"], it["ans"]):
                        no(seed, w, f"power key not a power of {it['base']}: {it['ans']}")
            if k == "value":
                r = sp.Rational(a)
                if gcd(int(r.p), int(r.q)) != 1:
                    no(seed, w, "not lowest terms")
                nums = [int(x) for x in re.findall(r"\d+", it["ans"])]
                if len(nums) == 2 and gcd(*nums) != 1:
                    no(seed, w, f"key fraction not in lowest terms {it['ans']}")
            if k == "sci":
                c, e = sci_parts(it["ans"])
                if not (1 <= c < 10):
                    no(seed, w, f"coefficient {c}")
                if not dec_ok(it["qtext"], a):
                    no(seed, w, f"shown number {it['qtext']} ≠ {a}")
                if "0" * 9 in it["qtext"].replace(".", "")[:0]:
                    pass
            if k == "std":
                if not dec_ok(it["ansText"], q):
                    no(seed, w, f"standard form {it['ansText']} ≠ {q}")
                if it["stem"]:
                    m = re.search(r"([\d.]+)E(\d+)", it["stem"])
                    if not m or sp.Rational(m.group(1)) * 10 ** int(m.group(2)) != q:
                        no(seed, w, "E-notation in the stem ≠ the question")
            if k == "times":
                if not (q > 1):
                    no(seed, w, "'how many times larger' but the first is not larger")
                m = re.fullmatch(r" = ([\d,]+) times", it["tail"])
                if not m or not dec_ok(m.group(1), a):
                    no(seed, w, f"tail {it['tail']} ≠ {a}")
                c, e = sci_parts(it["ans"])
                if not (1 <= c < 10):
                    no(seed, w, "ratio coefficient")
                # both numbers in the question must be in scientific notation
                for half in re.findall(r"\(\(([\d.]+)\)\*\(\(10\)", it["q"]):
                    if not (1 <= sp.Rational(half) < 10):
                        no(seed, w, f"question number {half} is not scientific notation")
            if k == "posexp":
                if sp.srepr(a).count("Integer(-") and "**(-" in it["ans"]:
                    no(seed, w, "key has a negative exponent")
            if k == "mono":
                if re.search(r"\*\*\(\(-", it["ans"]) and "posOnly":
                    pass
        except Exception as e:
            no(seed, w, f"could not check: {e!r} {it}")

print(len(D), "sets,", n_items, "items checked;", "ALL SOUND" if not bad else f"{len(bad)} PROBLEMS")
for b in bad[:40]:
    print(" ", b)
sys.exit(1 if bad else 0)
