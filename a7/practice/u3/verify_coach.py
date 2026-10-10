"""Independent sympy check of the coach's worked solutions (coach_dump.json from coach_check.js).
Every step must equal the question exactly; for the n-equation, every step must be true at the answer and the last must be n = answer."""
import json, os, sys
import sympy as sp

D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "coach_dump.json")))
A0 = int(sys.argv[1]) if len(sys.argv) > 2 else 0
A1 = int(sys.argv[2]) if len(sys.argv) > 2 else len(D)
D = D[A0:A1]
L = {c: sp.Symbol(c) for c in "abcdghkmnprstwxyz"}
def S(s): return sp.sympify(s, locals=L, rational=True)
def zero(d): return d == 0 or (bool(d.free_symbols) and sp.cancel(d) == 0)
bad, n = [], 0
for G in D:
    for s in G["sols"]:
        n += 1
        try:
            q, a = S(s["q"]), S(s["ans"])
            if s["eq"]:
                nv = a
                for l, r in s["steps"]:
                    if S(l).subs(L["n"], nv) != S(r).subs(L["n"], nv):
                        bad.append(f'{G["seed"]} {s["w"]}: equation step false at n = {nv}')
                l, r = s["steps"][-1]
                if S(l) != L["n"] or S(r) != nv:
                    bad.append(f'{G["seed"]} {s["w"]}: last step is not n = {nv}')
                continue
            for k, st in enumerate(s["steps"]):
                if not zero(S(st) - q):
                    bad.append(f'{G["seed"]} {s["w"]} step {k}: {st} ≠ {s["q"]}')
            if s["steps"] and not zero(S(s["steps"][-1]) - a):
                bad.append(f'{G["seed"]} {s["w"]}: last step ≠ answer')
        except Exception as e:
            bad.append(f'{G["seed"]} {s["w"]}: could not check {e!r}')
print(len(D), "sets,", n, "worked solutions checked;", "ALL SOUND" if not bad else f"{len(bad)} PROBLEMS")
for b in bad[:30]: print(" ", b)
sys.exit(1 if bad else 0)
