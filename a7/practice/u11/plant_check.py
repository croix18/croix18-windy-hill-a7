"""A7 Unit 11 practice: planted errors.   python3 plant_check.py
Each plant is one edit a careless change could make to the sources. On a copy of this folder (never the sources themselves),
the unit's checks (u11_check.js on 300 sets; then, if it passes, verify.py on the 100 it writes out; then mc_check.js on 300)
must fail on every plant, and pass on the copy with none."""
import os, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
PRACTICE = os.path.dirname(HERE)
A7 = os.path.dirname(PRACTICE)
FILES = ["shown.js", "shown43.py", "engine.js", "coach.js", "fig.js", "unit.js", "u11_check.js", "verify.py", "mc_check.js"]
PLANTS = [
    # keys
    ("Q1's key one too big", "engine.js", "const v = e.v, part = numPart({ fam, prm: slotPrm, eq: e, v, ans: ending(e).s,", "const v = e.v, part = numPart({ fam, prm: slotPrm, eq: e, v, ans: fam === 'like' ? qadd(ending(e).s, ONE) : ending(e).s,"),
    ("Q2's key with its sign lost", "engine.js", "const v = e.v, part = numPart({ fam, prm: slotPrm, eq: e, v, ans: ending(e).s,", "const v = e.v, part = numPart({ fam, prm: slotPrm, eq: e, v, ans: fam === 'both' ? qneg(ending(e).s) : ending(e).s,"),
    ("every equation printed with a group's sign turned", "engine.js", "return i === 0 ? (neg ? '−' + b : b) : (neg ? ' − ' : ' + ') + b; }).join('');\n}\nconst sideH", "return i === 0 ? (neg ? '−' + b : b) : (neg !== (ch.k === 'g') ? ' − ' : ' + ') + b; }).join('');\n}\nconst sideH"),
    ("Q3's fraction printed as its reciprocal", "engine.js", "fr(String(ch.f.n), String(ch.f.d))) : how === 'text'", "fr(String(ch.f.d), String(ch.f.n))) : how === 'text'"),
    ("Q4 distributes 0.3, not on the list", "engine.js", "const DECK = ['0.2', '0.4',", "const DECK = ['0.3', '0.4',"),
    ("Q5's no-solution and infinitely-many keys swapped", "engine.js", "correct: ['one', 'none', 'all'].indexOf(order[i])", "correct: ['one', 'all', 'none'].indexOf(order[i])"),
    ("Q6's box adds the x it should take away", "engine.js", "const K = form === 'g-t' ? a * b - d : a * b + d, C = a * c;", "const K = form === 'g-t' ? a * b + d : a * b + d, C = a * c;"),
    ("Q7's fee one dollar off the count", "engine.js", "const b = a + gap, g = T.r() < 0.3 ? T.ri(1, 4) * 5 : 0, f = g + gap * n;", "const b = a + gap, g = T.r() < 0.3 ? T.ri(1, 4) * 5 : 0, f = g + gap * n + 1;"),
    ("Q8 keys a wrong system too (and the clean rule lets it)", [("engine.js", "correct: shown.map((z, i) => z.ok ? i : -1).filter(i => i >= 0), key: keyOf('selSys', prm)", "correct: shown.map((z, i) => z.ok || i === 0 ? i : -1).filter(i => i >= 0), key: keyOf('selSys', prm)"),
      ("coach.js", "return !qeq(l1.m, l2.m) && (it.correct.indexOf(i) >= 0 ? t[0] && t[1] : t[0] !== t[1]); });", "return true; });")]),
    ("Q8's wrong system true in neither equation", "engine.js", "if (which === 1) l1 = L_(m1, b - m1 * a + off); else l2 = L_(m2, b - m2 * a + off);", "l1 = L_(m1, b - m1 * a + off); l2 = L_(m2, b - m2 * a + off);"),
    ("Q8 may have one right system (and the clean rule lets it)", [("engine.js", "k = T.pick([2, 3, 3]);", "k = T.pick([1, 2, 3]);"), ("coach.js", "    if (it.correct.length < 2 || it.correct.length > 3) return false;\n", "")]),
    ("Q9 keyed to the wrong equation's reason", "engine.js", "right = scen === 'sol' ? 'both' : scen === 'first' ? 'noSecond' : 'noFirst';", "right = scen === 'sol' ? 'both' : scen === 'first' ? 'noFirst' : 'noSecond';"),
    ("Q10 keyed to no solution", "engine.js", "opts: COUNTOPTS.slice(), correct: 0, key: keyOf('countCross', prm)", "opts: COUNTOPTS.slice(), correct: 1, key: keyOf('countCross', prm)"),
    ("Q11's one line keyed as parallel", "engine.js", "opts: COUNTOPTS.slice(), correct: same ? 2 : 1,", "opts: COUNTOPTS.slice(), correct: 1,"),
    ("Q11's one line written two ways is not one line", "engine.js", "const c = pm(T, 1, 4), d = pm(T, 1, 6), b = m * c + d;", "const c = pm(T, 1, 4), d = pm(T, 1, 6), b = m * c + d + 1;"),
    ("Q12's key swapped", "engine.js", "part: pairPart({ fam: 'readGraph', prm, l1, l2, ans: [Q(s.x0), Q(s.y0)]", "part: pairPart({ fam: 'readGraph', prm, l1, l2, ans: [Q(s.y0), Q(s.x0)]"),
    ("Q12's window cut to the crossing", "engine.js", "const w = windowFor([[s.x0, s.y0], [0, qnum(l1.b)], [0, qnum(l2.b)]], { mx: 2, my: 2 });", "const w = windowFor([[s.x0, s.y0], [0, qnum(l1.b)], [0, qnum(l2.b)]], { mx: 0, my: 0 });"),
    ("Q13(a)'s key one too big", "engine.js", "ans: Q(y1[miss]), key: keyOf('tableGap', prm)", "ans: Q(y1[miss] + 1), key: keyOf('tableGap', prm)"),
    ("Q13's second table one off in its first column", "engine.js", "const fig = { kind: 'tables', xs, rows: [y1.map((v, i) => i === miss ? null : v), y2]", "const fig = { kind: 'tables', xs, rows: [y1.map((v, i) => i === miss ? null : v), y2.map((v, i) => i ? v : v + 1)]"),
    ("Q13(b)'s key one column over", "engine.js", "fam: 'tableSol', stem: 'What is the solution of the system?', prm, l1, l2, xs, miss, ans: [Q(s.x0), Q(s.y0)]", "fam: 'tableSol', stem: 'What is the solution of the system?', prm, l1, l2, xs, miss, ans: [Q(s.x0 + 1), Q(s.y0 + s.m1)]"),
    ("Q14(a)'s amount a grid line too high", "engine.js", "ans: [Q(x.x0), Q(x.y0)], key: keyOf('storyMeet', prm)", "ans: [Q(x.x0), Q(x.y0 + ys)], key: keyOf('storyMeet', prm)"),
    ("Q14(b)'s estimate keyed swapped", "engine.js", "ans: [tenthOf(c.x), tenthOf(c.y)], tol:", "ans: [tenthOf(c.y), tenthOf(c.x)], tol:"),
    ("Q14(b)'s tolerance back to 0.2", "engine.js", "tol: Q(1, 10), key", "tol: Q(1, 5), key"),
    ("Q14(b)'s crossing allowed near a half-grid line", "engine.js", "half(qnum(c.x)) >= 0.15 && half(qnum(c.y)) >= 0.15 && [3n, 5n, 6n, 7n].includes(c.x.d) && [3n, 5n, 6n, 7n].includes(c.y.d)", "true"),
    ("Q14(b)'s estimate cut off, not rounded", "engine.js", "function tenthOf(q) { const t = Math.round(", "function tenthOf(q) { const t = Math.floor("),
    ("ruling 43: the engine stops steering by what the lessons showed", "engine.js", "const SHOWN_EQ = new Set(SHOWN.eq), SHOWN_SYS = new Set(SHOWN.sys);", "const SHOWN_EQ = new Set(), SHOWN_SYS = new Set();"),
    # figures
    ("a line drawn one unit too high", "fig.js", "f.lines.forEach((l, i) => { const c = clip(l, w);", "f.lines.forEach((l, i) => { const c = clip({ m: l.m, b: E.qadd(l.b, E.ONE) }, w);"),
    ("the second line drawn solid", "fig.js", "el.push('<line class=\"' + (i ? 'ln2' : 'ln1') + '\" data-line=\"'", "el.push('<line class=\"' + 'ln1' + '\" data-line=\"'"),
    ("the y-axis numbered one step off", "fig.js", "el.push('<text class=\"tick\" x=\"-13\" y=\"' + f1(PY(y)) + '\">' + mn(y) + '</text>');", "el.push('<text class=\"tick\" x=\"-13\" y=\"' + f1(PY(y)) + '\">' + mn(y + ys) + '</text>');"),
    ("the grid too small for a phone", "fig.js", "const k = Math.min(300 / nx, 300 / ny)", "const k = Math.min(130 / nx, 130 / ny)"),
    # the coach
    ("distributing gives the first term only, in the worked lines", "coach.js", "function distribute(side) { const out = []; side.forEach(c => { if (c.k === 'g') c.t.forEach(t => out.push(T_(qmul(c.f, t.c), t.v)));", "function distribute(side) { const out = []; side.forEach(c => { if (c.k === 'g') c.t.forEach(t => out.push(T_(t.v ? qmul(c.f, t.c) : t.c, t.v)));"),
    ("the check line's right side one off", "coach.js", "R = one(e.R) ? n(rv) : substT(e.R, s) + ' = ' + n(rv);", "R = one(e.R) ? n(rv) : substT(e.R, s) + ' = ' + n(qadd(rv, ONE));"),
    ("a Hint step divides by multiplying", "coach.js", "const OPV = { add: qadd, sub: qsub, mul: qmul, div: qdiv };", "const OPV = { add: qadd, sub: qsub, mul: qmul, div: qmul };"),
    ("a Hint states its own answer", "coach.js", "  return sign + posHint(t, qabs(x), qabs(y));\n}", "  return sign + posHint(t, qabs(x), qabs(y)) + ' It comes to = ' + n(OPV[t](x, y)) + '.';\n}"),
    ("a named mistake is marked right", "coach.js", "if (hit.length) return { v: 'wrong', what: [joinSays(hit)], rule, step: hit[0].step == null ? null : hit[0].step };", "if (hit.length) return { v: 'right', what: [joinSays(hit)], rule, step: null };"),
    ("Q5's wrong endings not named", "coach.js", "    why: (p, k) => { const got = endIdx(k), en = p.end, es = endStep(p), v = p.eq.v;", "    why: (p, k) => { return ''; const got = endIdx(k), en = p.end, es = endStep(p), v = p.eq.v;"),
    ("a Hint multiplies with ×", "coach.js", "function calcText(t, x, y) { return t === 'mul' ? n(x) + '(' + n(y) + ')' :", "function calcText(t, x, y) { return t === 'mul' ? n(x) + ' × ' + par(y) :"),
    ("the word slope in the rule", "coach.js", "'Two lines that intersect meet once, at their point of intersection: one solution.", "'Two lines with different slopes intersect once, at their point of intersection: one solution."),
    ("the paper's wrong answers include the key", "coach.js", "  const out = [], seen = [keyHtml(p)];", "  const out = [keyHtml(p)], seen = [];"),
    ("the estimate's paper choices may sit inside the tolerance", [("coach.js", "PF[p.fam].models(p).forEach(m => add(p.fam === 'estimate' ? [E.tenthOf(m.v[0]), E.tenthOf(m.v[1])] : m.v));", "(p.fam === 'estimate' ? [{ v: [qadd(p.ans[0], Q(1, 10)), p.ans[1]] }] : []).concat(PF[p.fam].models(p)).forEach(m => add(p.fam === 'estimate' ? [E.tenthOf(m.v[0]), E.tenthOf(m.v[1])] : m.v));"),
      ("coach.js", "else if (p.fam === 'estimate' ? within(p, v[0], v[1]) :", "else if (p.fam === 'estimate' ? false :")]),
    ("the pair reader swaps x and y", "engine.js", "  let nums = got.map(g => ({ q: g.val, tag: g.tag }));", "  let nums = got.map(g => ({ q: g.val, tag: g.tag })).reverse();"),
    ("the estimate's Hint accepts anything within 0.5", "unit.js", "numOk: (s, v) => s.tol ? Math.abs(E.qnum(v) - E.qnum(s.near)) <= E.qnum(s.tol) + 1e-9", "numOk: (s, v) => s.tol ? Math.abs(E.qnum(v) - E.qnum(s.near)) <= 0.5"),
    ("the key a student types is not the key", "unit.js", "keyText: p => p.kind === 'num' ? E.kstr(p.ans)", "keyText: p => p.kind === 'num' ? E.kstr(E.qadd(p.ans, E.Q(1, 10)))"),
]

def copy():
    d = tempfile.mkdtemp(prefix="a7u11plant-")
    os.makedirs(os.path.join(d, "a7", "practice", "u11"))
    os.symlink(os.path.join(PRACTICE, "kit"), os.path.join(d, "a7", "practice", "kit"))
    os.symlink(os.path.join(A7, "build"), os.path.join(d, "a7", "build"))
    for f in FILES:
        shutil.copy(os.path.join(HERE, f), os.path.join(d, "a7", "practice", "u11", f))
    return d, os.path.join(d, "a7", "practice", "u11")

def first(out):
    return ([l for l in out.splitlines() if l.startswith("  ")] or out.strip().splitlines()[-1:] or ["?"])[0].strip()[:110]

def checks(ud):
    r = subprocess.run(["node", "u11_check.js", "300", "100"], cwd=ud, capture_output=True, text=True)
    if r.returncode: return "u11_check: " + first(r.stdout + r.stderr)
    r = subprocess.run([sys.executable, "verify.py"], cwd=ud, capture_output=True, text=True)
    if r.returncode: return "verify: " + first(r.stdout + r.stderr)
    r = subprocess.run(["node", "mc_check.js", "300"], cwd=ud, capture_output=True, text=True)
    if r.returncode: return "mc_check: " + first(r.stdout + r.stderr)
    return None

failed = 0
d, ud = copy()
try:
    base = checks(ud)
    if base:
        print("the unplanted copy fails: " + base); sys.exit(1)
    for plant in PLANTS:
        name, edits = plant[0], plant[1] if isinstance(plant[1], list) else [tuple(plant[1:])]
        srcs, ok = {}, True
        for f, old, new in edits:
            src = srcs.get(f) or open(os.path.join(HERE, f), encoding="utf-8").read()
            if src.count(old) != 1: print(f"PLANT NOT APPLIED ({src.count(old)} matches): {name}"); ok = False; break
            srcs[f] = src.replace(old, new)
        if not ok: failed += 1; continue
        for f, src in srcs.items(): open(os.path.join(ud, f), "w", encoding="utf-8").write(src)
        got = checks(ud)
        print(("caught  " if got else "MISSED  ") + name + ("  ←  " + got if got else ""), flush=True)
        if not got: failed += 1
        for f in srcs: shutil.copy(os.path.join(HERE, f), os.path.join(ud, f))
finally:
    shutil.rmtree(d, ignore_errors=True)
print(f"plant_check: {len(PLANTS) - failed} of {len(PLANTS)} planted errors caught" + ("" if failed else " — ALL CAUGHT"))
sys.exit(1 if failed else 0)
