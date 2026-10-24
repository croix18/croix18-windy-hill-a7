"""A7 Unit 4 practice: planted errors.   python3 plant_check.py
Each plant is one edit a careless change could make to the sources. On a copy of this folder (never the sources themselves),
the unit's checks (u4_check.js on 300 sets, then verify.py) must fail on every plant, and pass on the copy with none.
Written 21 Oct 2026 with the significant-digit change."""
import os, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
PRACTICE = os.path.dirname(HERE)
A7 = os.path.dirname(PRACTICE)
FILES = ["engine.js", "coach.js", "unit.js", "u4_check.js", "verify.py", "test_forms.js"]
PLANTS = [
    ("the area's key ten times too big", "engine.js",
     "qmul(sciQ(L, 2), sciQ(W, 2)), { unitWord: 'square millimeters'", "qmul(sciQ(L, 2), sciQ(W, 3)), { unitWord: 'square millimeters'"),
    ("the speed's key ten times too big", "engine.js", "Q(v), { unitWord: 'km/h', op: '÷' }", "Q(v * 10), { unitWord: 'km/h', op: '÷' }"),
    ("the sum prints a power the key did not use", "engine.js",
     "' mm and ' + sciM(B, 2) + ' mm. Find their sum.'", "' mm and ' + sciM(B, 1) + ' mm. Find their sum.'"),
    ("the difference worked over the wrong power", "engine.js", "qsub(sciQ(C, -2), sciQ(Dd, -3))", "qsub(sciQ(C, -2), sciQ(Dd, -2))"),
    ("a worked line of the speed shows the wrong number", "coach.js",
     "{ say: 'Divide.', ex: X(sciH(E.decPlain(C), 2), p.ans) }", "{ say: 'Divide.', ex: X(sciH(E.decPlain(qmul(C, Q(2))), 2), p.ans) }"),
    ("a Hint step of the sum and difference expects the wrong number", "coach.js",
     "num('What is ' + S(A) + sg + S(b) + '?', C,", "num('What is ' + S(A) + sg + S(b) + '?', qadd(C, Q(1, 10)),"),
    ("the key a student types is off by a power", "unit.js", "' x 10^' + p.want.k", "' x 10^' + (p.want.k + 1)"),
    ("Form B's speed question dropped from the exclusion list", "test_forms.js",
     "rwSpeed: [['5.6', 8], ['7.2', 8], ['4.8', 6]]", "rwSpeed: [['5.6', 8], ['4.8', 6]]"),
    ("the clean rule no longer looks at the mistakes", "coach.js",
     "for (const m of F[p.fam].models(p)) { if (m.v && qeq(m.v, p.ans)) return false; }", ""),
    ("a right value in standard form marked right", "coach.js",
     "if (r.form === 'num') return { v: 'form', what: ['That is the value written out.", "if (r.form === 'num') return { v: 'right', what: ['That is the value written out."),
    ("mistakes no longer named", "coach.js",
     "function hits(p, v) { return (F[p.fam].models(p) || []).filter(m => m.v && qeq(m.v, v) && !qeq(m.v, p.ans)); }", "function hits(p, v) { return []; }"),
    ("a Hint choice with two right options", "coach.js", "O('time ÷ distance', false,", "O('time ÷ distance', true,"),
    ("Part 2 titled for significant digits again", "engine.js",
     "'Real-World Problems in Scientific Notation'", "'Real-World Problems and Significant Digits'"),
    ("Devon's sum back to a gap of 3 in the exclusion list", "test_forms.js", "['3.4', 4, '5.2', 6]", "['3.4', 3, '5.2', 6]"),
]

def copy():
    d = tempfile.mkdtemp(prefix="a7u4plant-")
    os.makedirs(os.path.join(d, "a7", "practice", "u4"))
    os.symlink(os.path.join(PRACTICE, "kit"), os.path.join(d, "a7", "practice", "kit"))
    os.symlink(os.path.join(A7, "build"), os.path.join(d, "a7", "build"))
    for f in FILES:
        shutil.copy(os.path.join(HERE, f), os.path.join(d, "a7", "practice", "u4", f))
    return d, os.path.join(d, "a7", "practice", "u4")

def checks(ud):
    r = subprocess.run(["node", "u4_check.js", "300", "120"], cwd=ud, capture_output=True, text=True)
    if r.returncode: return "u4_check: " + (r.stdout.strip().splitlines() or ["?"])[-1][:110]
    r = subprocess.run([sys.executable, "verify.py"], cwd=ud, capture_output=True, text=True)
    if r.returncode: return "verify: " + ([l for l in r.stdout.splitlines() if l.startswith("  ")] or [r.stdout.strip()[-110:]])[0].strip()[:110]
    return None

failed = 0
d, ud = copy()
try:
    base = checks(ud)
    if base:
        print("the unplanted copy fails: " + base); sys.exit(1)
    for name, f, old, new in PLANTS:
        src = open(os.path.join(HERE, f), encoding="utf-8").read()
        if src.count(old) != 1:
            print(f"PLANT NOT APPLIED ({src.count(old)} matches): {name}"); failed += 1; continue
        open(os.path.join(ud, f), "w", encoding="utf-8").write(src.replace(old, new))
        got = checks(ud)
        print(("caught  " if got else "MISSED  ") + name + ("  ←  " + got if got else ""))
        if not got: failed += 1
        shutil.copy(os.path.join(HERE, f), os.path.join(ud, f))
finally:
    shutil.rmtree(d, ignore_errors=True)
print(f"plant_check: {len(PLANTS) - failed} of {len(PLANTS)} planted errors caught" + ("" if failed else " — ALL CAUGHT"))
sys.exit(1 if failed else 0)
