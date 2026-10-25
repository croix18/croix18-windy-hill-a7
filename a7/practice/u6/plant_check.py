"""A7 Unit 6 practice: planted errors.   python3 plant_check.py
Each plant is one edit a careless change could make to the sources. On a copy of this folder (never the sources themselves),
the unit's checks (u6_check.js on 300 sets, then verify.py on the 120 it writes out) must fail on every plant, and pass on the
copy with none. Written 25 Oct 2026, with the page."""
import os, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
PRACTICE = os.path.dirname(HERE)
A7 = os.path.dirname(PRACTICE)
FILES = ["engine.js", "coach.js", "fig.js", "unit.js", "u6_check.js", "verify.py"]
PLANTS = [
    # keys
    ("the hypotenuse's key one too big", "engine.js",
     "Q(t[2]), { unit: ua, exact: t[2] }", "Q(t[2] + 1), { unit: ua, exact: t[2] }"),
    ("a tenth cut off instead of rounded", "engine.js",
     "const sqrtTenth = n => Q(roundSqrt(100 * n), 10);", "const sqrtTenth = n => Q(isqrt(100 * n), 10);"),
    ("how much shorter: the path added, not taken away", "engine.js",
     "Q(10 * A + (sign < 0 ? -1 : 1) * roundSqrt(100 * n), 10)", "Q(10 * A + roundSqrt(100 * n), 10)"),
    ("the perimeter leaves out a side", "engine.js",
     "plusSqrtTenth(s + h, n, 1), { unit: 'units', tenth: true", "plusSqrtTenth(s, n, 1), { unit: 'units', tenth: true"),
    ("the mirror's height off by one scale", "engine.js",
     "const D2 = qmul(qdec(d1), Q(k)), H2 = qmul(qdec(h1), Q(k));", "const D2 = qmul(qdec(d1), Q(k)), H2 = qmul(qdec(h1), Q(k + 1));"),
    ("the range's lower end one short", "engine.js",
     "const lo = b - a, hi = a + b, le = '&lt;'", "const lo = b - a - 1, hi = a + b, le = '&lt;'"),
    ("the equation choice keyed to the hypotenuse added in", "engine.js",
     "correct: order.indexOf(3), key: 'eqChoice'", "correct: order.indexOf(1), key: 'eqChoice'"),
    ("the similar choice keyed to the one with a side added", "engine.js",
     "sides: shown.map(x => x.s), correct: order.indexOf(0),", "sides: shown.map(x => x.s), correct: order.indexOf(1),"),
    ("the triangle choice keyed to the flat set", "engine.js",
     "tags: shown.map(x => x.tag), correct: order.indexOf(0),\n      key: 'triSet'", "tags: shown.map(x => x.tag), correct: order.indexOf(1),\n      key: 'triSet'"),
    ("Part 3 retitled", "engine.js", "'Distance on the Coordinate Plane'", "'Distance in the Coordinate Plane'"),
    # figures
    ("a grid point's label prints the wrong y", "fig.js",
     "B.ptLab([p[0], p[1]], ptName(p[0], p[1], p[2]), f.pts[1 - i])", "B.ptLab([p[0], p[1]], ptName(p[0], p[1] + 1, p[2]), f.pts[1 - i])"),
    ("a right triangle's leg label on the other leg", "fig.js",
     "B.lab(P[0], P[1], f.labs[0], f.vals[0], cen, { tol: 1e-6 });", "B.lab(P[0], P[2], f.labs[0], f.vals[0], cen, { tol: 1e-6 });"),
    ("the similar copy drawn too long", "engine.js",
     "b: [qnum(cp), qnum(cq), qnum(cr)]", "b: [qnum(cp), qnum(cq), qnum(cr) + 1]"),
    ("the copy's corners lettered in another order", "fig.js",
     "T.forEach((p, i) => B.ptLab(p, nm[i], cen)); });", "T.forEach((p, i) => B.ptLab(p, nm[(i + j) % 3], cen)); });"),
    ("the words name the copy's corners in another order", "engine.js",
     "' is similar to triangle ' + nm.slice(3).join('') + '.'", "' is similar to triangle ' + [nm[4], nm[3], nm[5]].join('') + '.'"),
    # the words: a real place, a grown-up's height, and the mirror's similar triangles said
    ("a garden 1 m wide", "engine.js", "garden: [['m', 2], ['ft', 5], ['yd', 3]]", "garden: [['m', 1], ['ft', 1], ['yd', 1]]"),
    ("a man 4 ft tall", "engine.js", "man: ['5.5', '6'], woman: ['5', '5.5', '6']", "man: ['4', '4.5'], woman: ['4', '4.5']"),
    ("the mirror's words stop saying the triangles are similar", "engine.js",
     "' ft beyond the mirror. The two right triangles are similar. How tall is the '", "' ft beyond the mirror. How tall is the '"),
    ("the shadow figure labels the girl's shadow with her height", "engine.js",
     "lab: [N(h1) + ' ft', N(s1) + ' ft', numStr(S2) + ' ft', 'h']", "lab: [N(h1) + ' ft', N(h1) + ' ft', numStr(S2) + ' ft', 'h']"),
    # the coach's words and numbers
    ("Show me how reads the hundredths digit one off", "coach.js",
     "return ((v % 10) + 10) % 10; }", "return ((v % 10) + 11) % 10; }"),
    ("a cut-off decimal one too big in its last place", "coach.js",
     "const k = isqrt(n * 1000000), v = s < 0", "const k = isqrt(n * 1000000) + 1, v = s < 0"),
    ("a worked line takes the root of the wrong number", "coach.js",
     "{ say: 'c is the number whose square is ' + n + '.', ex: EX(sqrtH(n) + ' = ' + S(p.ans), p.ans) }]; },\n  walk: p => { const { a, b } = p.prm, n = a * a + b * b;\n    return [choice('Which side is the hypotenuse, c?'",
     "{ say: 'c is the number whose square is ' + n + '.', ex: EX(sqrtH(n + 1) + ' = ' + S(p.ans), p.ans) }]; },\n  walk: p => { const { a, b } = p.prm, n = a * a + b * b;\n    return [choice('Which side is the hypotenuse, c?'"),
    ("a Hint step across zero one off", "coach.js",
     "'?', Q(dx), h(x.x1, x.x2, 'y'), { pic: true })", "'?', Q(dx + 1), h(x.x1, x.x2, 'y'), { pic: true })"),
    ("a fraction printed in a reason", "coach.js",
     "' ÷ ' + t[2] + ' is not ' + kOut(qdiv(s[0], Q(t[0]))) + '.';", "' ÷ ' + t[2] + ' is ' + S(qdiv(s[2], Q(t[2]))) + '.';"),
    ("a fraction scale factor on sides it does not divide", "engine.js",
     "const k = qk(ks), m = ks.indexOf('/') > 0 ? Number(k.d) : 1;", "const k = qk(ks), m = 1;"),
    ("a Hint step takes 1.3 for 4/3", "unit.js", "E.places(s.ans) < 0 && E.places(v) >= 2", "E.places(s.ans) < 0 && E.places(v) >= 1"),
    # marking
    ("a modelled mistake worth the answer (the clean rule must refuse every such question)", "coach.js",
     "mod(Q(a * a + b * b), 'stopped at c' + sup(2) + ' = ' + (a * a + b * b) + ' and forgot the square root.', 1)];",
     "mod(p.ans, 'stopped at c' + sup(2) + ' = ' + (a * a + b * b) + ' and forgot the square root.', 1)];"),
    ("the clean rule lets a printed number be the answer", "coach.js",
     "    if (printed.some(x => qeq(x, p.ans))) return false;\n", ""),
    ("the root of a whole answer marked right", "coach.js",
     "if (r.form === 'root') return { v: 'form', what: ['That is right — and '", "if (r.form === 'root') return { v: 'right', what: ['That is right — and '"),
    ("mistakes no longer named", "coach.js", "  const h = hits(p, r);\n", "  const h = [];\n"),
    ("a Hint choice with two right options", "coach.js",
     "O('the longer leg, ' + Math.max(a, b), false,", "O('the longer leg, ' + Math.max(a, b), true,"),
    ("follow-through from part (a) adds instead of subtracting", "coach.js",
     "follow: (p, prev) => p.prm.w + p.prm.l - prev,", "follow: (p, prev) => p.prm.w + p.prm.l + prev,"),
    ("the key a student types is not the key", "unit.js", "keyText: p => E.decPlain(p.ans)", "keyText: p => E.decPlain(E.qadd(p.ans, E.Q(1, 10)))"),
]

def copy():
    d = tempfile.mkdtemp(prefix="a7u6plant-")
    os.makedirs(os.path.join(d, "a7", "practice", "u6"))
    os.symlink(os.path.join(PRACTICE, "kit"), os.path.join(d, "a7", "practice", "kit"))
    os.symlink(os.path.join(A7, "build"), os.path.join(d, "a7", "build"))
    for f in FILES:
        shutil.copy(os.path.join(HERE, f), os.path.join(d, "a7", "practice", "u6", f))
    return d, os.path.join(d, "a7", "practice", "u6")

def checks(ud):
    r = subprocess.run(["node", "u6_check.js", "300", "120"], cwd=ud, capture_output=True, text=True)
    if r.returncode: return "u6_check: " + ([l for l in r.stdout.splitlines() if l.startswith("  ")] or (r.stdout + r.stderr).strip().splitlines()[-1:] or ["?"])[0].strip()[:110]
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
