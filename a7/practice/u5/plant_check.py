"""A7 Unit 5 practice: planted errors.   python3 plant_check.py
Each plant is one edit a careless change could make to the sources. On a copy of this folder (never the sources themselves),
the unit's checks (u5_check.js on 300 sets, then verify.py on the 120 it writes out) must fail on every plant, and pass on
the copy with none. Written 25 Oct 2026, with the page."""
import os, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
PRACTICE = os.path.dirname(HERE)
A7 = os.path.dirname(PRACTICE)
FILES = ["engine.js", "coach.js", "unit.js", "u5_check.js", "verify.py", "test_forms.js"]
PLANTS = [
    # keys
    ("the scale factor divided the wrong way", "engine.js", "const k = Q(b, a), prm = { a, b, u };", "const k = Q(a, b), prm = { a, b, u };"),
    ("the copy's area multiplied by k once", "engine.js", "A = qmul(Q(w * h), qmul(k, k)), prm", "A = qmul(Q(w * h), k), prm"),
    ("k from two areas one too big", "engine.js", "part: numPart('', 'kArea', prm, '', Q(k), { pre: 'k =' })", "part: numPart('', 'kArea', prm, '', Q(k + 1), { pre: 'k =' })"),
    ("the room's area with the rate used once", "engine.js", "'Find the room’s real area.', qmul(a, b), { unit: 'ft²' })", "'Find the room’s real area.', qmul(qmul(p, q), r), { unit: 'ft²' })"),
    ("a real wall drawn by multiplying", "engine.js", "part: numPart('', 'toPlan', prm, '', Q(L, sc.r), { unit: 'in' })", "part: numPart('', 'toPlan', prm, '', Q(L * sc.r), { unit: 'in' })"),
    ("a conversion by the other line of the sheet", "engine.js", "const f = toMetric ? qdec(P.ab) : qdec(P.ba), o = toMetric", "const f = toMetric ? qdec(P.ba) : qdec(P.ab), o = toMetric"),
    ("the chain skips the inches", "engine.js", "const prm = { n: N(n) }, inches = qmul(n, Q(36));", "const prm = { n: N(n) }, inches = qmul(n, Q(3));"),
    ("the square-unit choice keyed to the ratio used once", "engine.js", "exact, correct: order.indexOf(0),", "exact, correct: order.indexOf(1),"),
    ("dollars back by multiplying", "engine.js", "C0.name + '?', Q(Dl), { pre: '$' })", "C0.name + '?', qmul(c, r), { pre: '$' })"),
    ("the tanks rounded down", "engine.js", "qceil(Q(Dm, R)), { unit: 'tanks' })", "qfloor(Q(Dm, R)), { unit: 'tanks' })"),
    ("the recipe never divided by its servings", "engine.js", "const A = qdiv(qmul(c, Q(t)), Q(s)), Bs", "const A = qmul(c, Q(t)), Bs"),
    ("the mixture's whole without finding one part", "engine.js", "numPart('', 'mixWhole', prm, '', Q(k * sum), { unit: X.unit })", "numPart('', 'mixWhole', prm, '', Q(n * sum), { unit: X.unit })"),
    ("the speeds keyed to comparing the numbers as they stand", "engine.js", "correct: order.indexOf(0), key: 'speeds'", "correct: order.indexOf(1), key: 'speeds'"),
    ("the area × k statement keyed true", "engine.js", "{ h: 'The area is ' + kS + ' times as large.', tag: 'areaK', ok: false }", "{ h: 'The area is ' + kS + ' times as large.', tag: 'areaK', ok: true }"),
    ("a select-all ratio printed the wrong way", "engine.js", "' and ' + M(ratioH(P.b, P.ba, P.a)) + '. Select ALL", "' and ' + M(ratioH(P.b, P.ab, P.a)) + '. Select ALL"),
    ("a ratio that is not the sheet's", "engine.js", "stem: M(ratioH('gal', '3.785', 'L'))", "stem: M(ratioH('gal', '3.79', 'L'))"),
    ("liters asked, gallons given the wrong way", "engine.js", "'. How many liters is ' + n + ' gal?'", "'. How many gallons is ' + n + ' L?'"),
    ("Part 2 retitled", "engine.js", "'Converting Across Systems'", "'Converting Between Systems'"),
    # the test and the lessons
    ("the test's numbers no longer kept off", "engine.js", "const fresh = fk => fk.every(([s, k]) => !isForm(s, k) && !isShown(s, k));", "const fresh = fk => fk.every(([s, k]) => !isShown(s, k));"),
    ("the lessons' numbers no longer kept off (ruling 43)", "engine.js", "const fresh = fk => fk.every(([s, k]) => !isForm(s, k) && !isShown(s, k));", "const fresh = fk => fk.every(([s, k]) => !isForm(s, k));"),
    ("a form hash drifted", "engine.js", "4239484767", "4239484768"),
    ("test_forms.js drifted from the form", "test_forms.js", "sf: ['4>10', '15>6']", "sf: ['4>11', '15>6']"),
    # the coach's marking
    ("the clean rule lets a printed number be the answer", "coach.js", "    if (printed.some(x => qeq(x, p.ans))) return false;\n", ""),
    ("mistakes no longer named", "coach.js", "  const h = hits(p, r);\n", "  const h = [];\n"),
    ("the key rounded marked right", "coach.js", "      return { v: 'form', what: [p.money ? 'Almost — give money", "      return { v: 'right', what: [p.money ? 'Almost — give money"),
    ("the sheet's other ratio no longer right", "coach.js", "    if (p.alt && r.dp >= 1 && qeq(qround(p.alt, r.dp), r.val)) {", "    if (false) {"),
    ("an unsimplified fraction marked right", "coach.js", "    if (r.form === 'num' && r.frac !== 'unreduced') return { v: 'right', what: [] };", "    if (r.form === 'num') return { v: 'right', what: [] };"),
    ("a mixed number run together read as a fraction", "coach.js", "  const meant = didMean(typed, A); if (meant && !qeq(r.val, A))", "  const meant = null; if (meant && !qeq(r.val, A))"),
    ("follow-through from the wrong wall", "coach.js", "follow: follow ? (p, a) => qmul(a, qmul(qv(p.prm.q), Q(p.prm.r))) : null,", "follow: follow ? (p, a) => qmul(a, qv(p.prm.q)) : null,"),
    ("follow-through not credited in \"Like the real test\"", "coach.js", "if (ctx.mode === 'test') return { v: 'right', follow: true,", "if (ctx.mode === 'test') return { v: 'wrong', follow: true,"),
    # the coach's words and help
    ("a Hint choice with two right options", "coach.js", "O('divide by ' + x.r, false, 'The real room is bigger than its plan: multiply.')", "O('divide by ' + x.r, true, 'The real room is bigger than its plan: multiply.')"),
    ("a part (b) Hint asks for part (a)'s number", "coach.js", "How long is the other wall, drawn ' + N(x.q) + ' in long, for real?', B,", "How long is the other wall, drawn ' + N(x.q) + ' in long, for real?', A,"),
    ("a worked line one off", "coach.js", "{ say: 'Inches to centimeters:', ex: EX(S(i) + ' × 2.54 = ' + S(p.ans), p.ans) }", "{ say: 'Inches to centimeters:', ex: EX(S(i) + ' × 2.54 = ' + S(qadd(p.ans, Q(1))), p.ans) }"),
    ("a Hint gives its answer away", "coach.js", "num('What is ' + b + ' ÷ ' + a + '?', p.ans, HINT.div(Q(b), Q(a)) + ' A decimal is fine.')", "num('What is ' + b + ' ÷ ' + a + '?', p.ans, 'It is ' + b + ' ÷ ' + a + ' = ' + S(p.ans) + '.')"),
    ("an estimate that says the wrong way", "coach.js", "+ (more ? 'more' : 'fewer') + ' than ' + N(n) + ' ' + UW[to][1] + '.';", "+ (more ? 'fewer' : 'more') + ' than ' + N(n) + ' ' + UW[to][1] + '.';"),
    ("the key a student types is not the key", "unit.js", "keyText: p => p.cups ? E.mixedText(p.ans) : p.money ? E.money(p.ans) : E.decPlain(p.ans)", "keyText: p => p.cups ? E.mixedText(p.ans) : p.money ? E.money(p.ans) : E.decPlain(E.qadd(p.ans, E.Q(1, 100)))"),
]

def copy():
    d = tempfile.mkdtemp(prefix="a7u5plant-")
    os.makedirs(os.path.join(d, "a7", "practice", "u5"))
    os.symlink(os.path.join(PRACTICE, "kit"), os.path.join(d, "a7", "practice", "kit"))
    os.symlink(os.path.join(A7, "build"), os.path.join(d, "a7", "build"))
    for f in FILES:
        shutil.copy(os.path.join(HERE, f), os.path.join(d, "a7", "practice", "u5", f))
    return d, os.path.join(d, "a7", "practice", "u5")

def checks(ud):
    try:
        r = subprocess.run(["node", "u5_check.js", "300", "120"], cwd=ud, capture_output=True, text=True, timeout=600)
    except subprocess.TimeoutExpired:
        return "u5_check: timed out"
    if r.returncode: return "u5_check: " + ([l for l in r.stdout.splitlines() if l.startswith("  ")] or (r.stdout + r.stderr).strip().splitlines()[-1:] or ["?"])[0].strip()[:110]
    r = subprocess.run([sys.executable, "verify.py"], cwd=ud, capture_output=True, text=True)
    if r.returncode: return "verify: " + ([l for l in r.stdout.splitlines() if l.startswith("  ")] or [(r.stdout + r.stderr).strip()[-110:]])[0].strip()[:110]
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
