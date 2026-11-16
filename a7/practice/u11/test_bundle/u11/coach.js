/* A7 Unit 11 practice: the coach. For every kind of question: the mistakes students make (each with the exact value it gives
   and the words that finish "That is what you get if you …"), the rule (Hint 1), the worked solution (Hint 3, every line
   re-derived here from the equation's pieces), the step-by-step walk (Hint 2), the marking of a typed answer, the reasons for
   every wrong choice, and the three wrong answers of a typed part for the all-multiple-choice paper.
   The named mistakes are the unit's (the B1G-M's and the lesson outlines'): the number outside distributed to the first term
   only; the sign of a distributed negative lost; the like term left out; the x-terms added instead of taken away; the number
   added undone the wrong way; a = a read as no solution or as x = 0, x = 0 read as no solution; a pair that makes one equation
   true; the coordinates swapped; the point where one line meets an axis; the nearest grid point for an estimate.
   No false equation is printed as a line of work: "1 = 5 — never true" is an ending said in words. Multiplication is written
   with parentheses or a dot, never × (the unit's standing decision 8). Registers the clean rule with the engine. */
(function (root) {
'use strict';
const node = typeof module !== 'undefined' && module.exports;
const E = node ? require('./engine.js') : root.Practice;
const KIT = node ? require('../kit/core.js') : root.Kit;
const { Q, qadd, qsub, qmul, qdiv, qneg, qabs, qeq, qlt, qnum, qsign, isInt, places, qv, qdec, kstr, numStr, nHtml, M, vi, pairH, T_, G_, B_, sideH, sideT, eqH, eqT,
  lin, fill, ending, substT, sideNums, sgnOf, lineH, lineT, yAt, onLine, meet, ZERO, ONE } = E;
const n = numStr, LET = 'ABCDE';
const dot = s => String(s).replace(/\s*×\s*/g, ' · ');                 /* the kit's hints say ×; this unit writes a dot */
const ch = (label, ok, why) => ({ label, ok: !!ok, why: why || '' });
const choice = (ask, opts, then, extra) => Object.assign({ type: 'choice', ask, opts, then: then || null }, extra || {});
const numS = (ask, ans, hint, then, extra) => Object.assign({ type: 'num', ask, ans, hint, then: then || null }, extra || {});
const joinSays = ms => { const says = []; ms.forEach(m => { if (says.indexOf(m.say) < 0) says.push(m.say); }); return 'That is what you get if you ' + says.join(' — or if you ') + '.'; };
const term = (c, v) => sideH([T_(c, v)]);                               /* 5n, −3x, 7 as printed */
const termT = (c, v) => sideT([T_(c, v)]);
const par = q => qsign(q) < 0 ? '(' + n(q) + ')' : n(q);

/* ------------------------------------------------------------------ one smaller step of arithmetic, signs first (never the answer) */
function posHint(t, a, b) {
  if (t === 'add') return dot(KIT.hint.add(a, b));
  if (t === 'sub') return dot(KIT.hint.sub(a, b));
  if (t === 'mul') {
    if (qeq(a, ONE) || qeq(b, ONE)) return 'Multiplying by 1 leaves a number as it is.';
    if (a.n === 0n || b.n === 0n) return 'Any number times 0 is 0.';
    return dot(KIT.hint.mul(a, b));
  }
  if (a.n === 0n) return 'Zero divided by any other number is 0.';
  const h = places(qdiv(a, b)) < 0 ? 'Write it as a fraction: the first number on top, the second on the bottom.' : dot(KIT.hint.div(a, b));
  return /^Half of [^:]*: what number added to itself/.test(h) ? 'Think: 2 · ? = ' + n(a) + '.' : h;
}
function arith(t, x, y) {                                               /* x t y, t one of add sub mul div */
  if (t === 'add' || t === 'sub') {
    const yy = t === 'sub' ? qneg(y) : y;
    if (t === 'sub' && qsign(y) < 0) return 'Subtracting a negative is adding: ' + n(x) + ' − (' + n(y) + ') is ' + n(x) + ' + ' + n(qabs(y)) + '. ' + (qsign(x) >= 0 ? posHint('add', x, qabs(y)) : 'The signs are different: take the smaller size from the larger, and keep the sign of the larger.');
    if (t === 'sub' && qsign(x) >= 0 && qsign(y) > 0 && qlt(x, y)) return n(y) + ' is more than ' + n(x) + ', so the answer is negative: work out ' + n(y) + ' − ' + n(x) + ', then make it negative.';
    if (t === 'sub' && qsign(x) < 0 && qsign(y) > 0) return 'Taking ' + n(y) + ' away from a negative number goes further below 0: add ' + n(qabs(x)) + ' and ' + n(y) + ', and the answer is negative.';
    if (qsign(x) >= 0 && qsign(yy) >= 0) return posHint('add', x, yy);
    if (qsign(x) >= 0 && qsign(yy) < 0 && !qlt(x, qabs(yy))) return posHint('sub', x, qabs(yy));
    if (qsign(x) <= 0 && qsign(yy) <= 0) return 'Both numbers are negative: add ' + n(qabs(x)) + ' and ' + n(qabs(yy)) + ', and the answer is negative.';
    const bigq = qlt(qabs(yy), qabs(x)) ? x : yy, small = bigq === x ? yy : x;
    return 'The signs are different: take ' + n(qabs(small)) + ' away from ' + n(qabs(bigq)) + ', and keep the sign of ' + n(bigq) + '.';
  }
  const sx = qsign(x), sy = qsign(y);
  const sign = !sx || !sy ? '' : sx * sy < 0 ? 'The signs are different, so the answer is negative. ' : sx < 0 ? 'Two negatives make a positive. ' : '';
  return sign + posHint(t, qabs(x), qabs(y));
}
const OPV = { add: qadd, sub: qsub, mul: qmul, div: qdiv };
const nFrac = q => (qsign(q) < 0 ? '−' : '') + E.fr(String(qabs(q).n), String(q.d));
/* a fraction times a whole number: divide by the bottom first (never the answer itself) */
const fracHint = (f, c) => (qsign(f) * qsign(c) < 0 ? 'The signs are different, so the answer is negative. ' : qsign(f) < 0 ? 'Two negatives make a positive. ' : '') + 'Divide ' + n(qabs(c)) + ' by ' + f.d + ' first' + (qabs(f).n === 1n ? '.' : ', then multiply by ' + qabs(f).n + '.');
const OPT = { add: ' + ', sub: ' − ', mul: '', div: ' ÷ ' };
function calcText(t, x, y) { return t === 'mul' ? n(x) + '(' + n(y) + ')' : n(x) + OPT[t] + (t === 'sub' || t === 'add' ? (qsign(y) < 0 ? '(' + n(y) + ')' : n(y)) : par(y)); }
function numCalc(t, x, y, ask, then, extra) { return numS(ask || 'What is ' + M(calcText(t, x, y)) + '?', OPV[t](x, y), arith(t, x, y), then, extra); }

/* ------------------------------------------------------------------ solving an equation, step by step, from its pieces
   steps(e) → [{k, say, eq (the equation after the step, or null at an ending), walk: [steps]}]; the same order every lesson
   teaches: distribute, collect, the same variable term from both sides, undo the number added, divide, check. */
const clone = s => s.map(c => c.k === 'g' ? G_(c.f, clone(c.t), c.fr) : Object.assign({}, c));
function distribute(side) { const out = []; side.forEach(c => { if (c.k === 'g') c.t.forEach(t => out.push(T_(qmul(c.f, t.c), t.v))); else out.push(Object.assign({}, c)); }); return out; }
function collect(side) {                                                /* like terms together, in the order each kind first appears */
  const out = []; side.forEach(c => { const j = out.findIndex(o => o.k === 't' && !!o.v === !!c.v); if (j < 0) out.push(Object.assign({}, c)); else out[j] = T_(qadd(out[j].c, c.c), c.v); });
  return out.filter(c => c.c.n !== 0n);
}
const hasG = s => s.some(c => c.k === 'g');
const needsCollect = s => s.filter(c => c.v).length > 1 || s.filter(c => !c.v).length > 1;
const vterm = s => s.find(c => c.v), cterm = s => s.find(c => !c.v);
const coefOf = s => { const t = vterm(s); return t ? t.c : ZERO; }, constOf = s => { const t = cterm(s); return t ? t.c : ZERO; };
function groupSay(g, v) {
  const F0 = g.fr && !isInt(g.f) ? E.fracT(g.f) : n(g.f);
  const parts = g.t.map(t => (qsign(g.f) < 0 || qsign(t.c) < 0 ? '(' + F0 + ')(' + (t.v ? sideT([T_(t.c, t.v)]) : n(t.c)) + ')' : F0 + '(' + (t.v ? sideT([T_(t.c, t.v)]) : n(t.c)) + ')') + ' = ' + sideT([T_(qmul(g.f, t.c), t.v)]));
  return 'the ' + F0 + ' multiplies every term inside: ' + parts.join(' and ');
}
function steps(e) {
  const v = e.v, out = [];
  let L = clone(e.L), R = clone(e.R);
  const eqNow = () => ({ L: clone(L), R: clone(R), v });
  /* 1. distribute */
  if (hasG(L) || hasG(R)) {
    const gs = L.concat(R).filter(c => c.k === 'g'), say = 'Distribute: ' + gs.map(g => groupSay(g, v)).join('; ') + '.';
    const walk = [choice('What is a good first step?', [ch('Distribute: multiply every term inside the parentheses by the number in front', 1),
        ch('Multiply only the first term inside by the number in front', 0, 'The number in front multiplies EVERY term inside the parentheses — the number after the letter too.'),
        ch('Add or subtract the numbers outside the parentheses first', 0, 'A number in front of parentheses is multiplying them. Undo nothing until the parentheses are gone: distribute first.')])]
      .concat(gs.map(g => { const t = g.t.find(t => !t.v), F0 = g.fr && !isInt(g.f) ? E.fracT(g.f) : n(g.f), fh = g.fr && !isInt(g.f) ? nFrac(g.f) : n(g.f);
        return numS('The ' + F0 + ' multiplies the ' + n(t.c) + ' too. What is ' + M(fh + '(' + n(t.c) + ')') + '?', qmul(g.f, t.c), g.fr && !isInt(g.f) ? fracHint(g.f, t.c) : arith('mul', g.f, t.c)); }));
    L = distribute(L); R = distribute(R);
    out.push({ k: 'dist', say, eq: eqNow(), walk, gs });
  }
  /* 2. collect the like terms on each side */
  if (needsCollect(L) || needsCollect(R)) {
    const sayOf = s => { const vs = s.filter(c => c.v), cs = s.filter(c => !c.v), bits = [];
      if (vs.length > 1) bits.push(sideT(vs) + ' = ' + sideT([T_(vs.reduce((a, c) => qadd(a, c.c), ZERO), v)]));
      if (cs.length > 1) bits.push(sideT(cs) + ' = ' + n(cs.reduce((a, c) => qadd(a, c.c), ZERO)));
      return bits; };
    const bits = sayOf(L).concat(sayOf(R)), walk = [];
    [L, R].forEach(s => { const vs = s.filter(c => c.v), cs = s.filter(c => !c.v);
      if (vs.length > 1) walk.push(numS('Collect the ' + vi(v) + '-terms: ' + M(sideH(vs)) + ' is how many ' + vi(v) + '’s? What is ' + M(vs.map((c, i) => i ? (qsign(c.c) < 0 ? ' − ' + n(qabs(c.c)) : ' + ' + n(c.c)) : n(c.c)).join('')) + '?',
        vs.reduce((a, c) => qadd(a, c.c), ZERO), vs.length === 2 ? arith('add', vs[0].c, vs[1].c) : 'Add them one at a time.'));
      if (cs.length > 1) walk.push(numS('Collect the numbers: what is ' + M(sideH(cs)) + '?', cs.reduce((a, c) => qadd(a, c.c), ZERO), cs.length === 2 ? arith('add', cs[0].c, cs[1].c) : 'Add them one at a time.')); });
    const groups = [L, R].reduce((a, sd) => a.concat([sd.filter(c => c.v), sd.filter(c => !c.v)].filter(g => g.length > 1)), []);
    L = collect(L); R = collect(R);
    out.push({ k: 'coll', say: 'Collect the like terms: ' + bits.join('; ') + '.', eq: eqNow(), walk, groups });
  }
  /* 3. the letter on both sides: take the same variable term from both */
  const a = coefOf(L), b = coefOf(R);
  if (a.n !== 0n && b.n !== 0n) {
    const take = qeq(a, b) ? a : qlt(b, a) ? b : a, tk = T_(take, v), wd = qsign(take) < 0 ? 'Add ' + termT(qabs(take), v) + ' to both sides' : 'Take ' + termT(take, v) + ' from both sides';
    const wrongWd = qsign(take) < 0 ? 'Take ' + termT(qabs(take), v) + ' from both sides' : 'Add ' + termT(take, v) + ' to both sides';
    const walk0 = choice('The letter is on both sides. How do you get it on one side?', [ch(wd, 1),
      ch(wrongWd, 0, 'That puts more ' + vi(v) + '’s on both sides instead of fewer. ' + (qsign(take) < 0 ? 'Undo − ' + termT(qabs(take), v) + ' by adding it.' : 'Take the term away from both sides.')),
      ch(wd.replace(' both sides', ' one side only'), 0, 'Whatever you do to one side, do to the other — or it is no longer the same equation.')]);
    if (qeq(a, b)) {
      const cl = constOf(L), cr = constOf(R), all = qeq(cl, cr), rest = n(cl) + ' = ' + n(cr);
      out.push({ k: 'end', kind: all ? 'all' : 'none', left: rest,
        say: wd + ': ' + rest + (all ? ' — always true, whatever number ' + v + ' is, so every number is a solution: infinitely many solutions.' : ' — never true, whatever number ' + v + ' is, so no number works: no solution.'),
        eq: null, walk: [walk0, choice('What is left is ' + M(rest) + '. What does that tell you?', [ch(all ? 'Always true: infinitely many solutions' : 'Never true: no solution', 1),
          ch(all ? 'Never true: no solution' : 'Always true: infinitely many solutions', 0, all ? M(rest) + ' is true — and it stays true for every number, because the letter is gone.' : n(cl) + ' and ' + n(cr) + ' are different numbers, so it is never true.'),
          ch(vi(v) + ' = 0: one solution', 0, 'The letter is gone, so nothing says what ' + vi(v) + ' is. Read the sentence that is left: is it true, or false?')])] });
      return out;
    }
    L = collect(L.concat([T_(qneg(take), v)])); R = collect(R.concat([T_(qneg(take), v)]));
    const other = qeq(take, a) ? b : a;
    out.push({ k: 'var', say: wd + ': the ' + vi(v) + '-terms are now on one side.', eq: eqNow(), take, other, walk: [walk0, numCalc('sub', other, take, 'What is ' + M(calcText('sub', other, take)) + '? (That many ' + vi(v) + '’s are left.)')] });
  }
  /* which side has the letter now */
  const vs = coefOf(L).n !== 0n ? 'L' : coefOf(R).n !== 0n ? 'R' : null;
  if (!vs) { const cl = constOf(L), cr = constOf(R), all = qeq(cl, cr); out.push({ k: 'end', kind: all ? 'all' : 'none', left: n(cl) + ' = ' + n(cr), say: n(cl) + ' = ' + n(cr) + (all ? ' — always true: infinitely many solutions.' : ' — never true: no solution.'), eq: null, walk: [] }); return out; }
  const Vside = () => vs === 'L' ? L : R, Oside = () => vs === 'L' ? R : L;
  /* 4. undo the number added on the letter's side */
  const k0 = constOf(Vside());
  if (k0.n !== 0n) {
    const co = coefOf(Vside()), o0 = constOf(Oside()), res = qsub(o0, k0), plus = qsign(k0) > 0, pre = eqNow();
    const wd = plus ? 'Subtract ' + n(k0) + ' from both sides' : 'Add ' + n(qabs(k0)) + ' to both sides';
    const wrong = plus ? 'Add ' + n(k0) + ' to both sides' : 'Subtract ' + n(qabs(k0)) + ' from both sides';
    const nv = [T_(co, v)], no = [T_(res)];
    if (vs === 'L') { L = nv; R = no; } else { R = nv; L = no; }
    out.push({ k: 'const', co, o0, say: (plus ? 'Undo the + ' + n(k0) + ': subtract ' + n(k0) + ' from both sides.' : 'Undo the − ' + n(qabs(k0)) + ': add ' + n(qabs(k0)) + ' to both sides.'), eq: eqNow(), k0,
      walk: [choice('Now ' + M(eqH(pre)) + '. What next?', [ch(wd, 1),
        ch(wrong, 0, plus ? '+ ' + n(k0) + ' is undone by subtracting ' + n(k0) + '.' : '− ' + n(qabs(k0)) + ' is undone by adding ' + n(qabs(k0)) + '.'),
        ch('Divide only ' + M(term(co, v)) + ' by ' + n(co), 0, 'Dividing first works only if every term is divided — the ' + n(qabs(k0)) + ' too. Undo the number added first.')]),
        numCalc('sub', o0, k0, 'What is ' + M(calcText('sub', o0, k0)) + '?')] });
  }
  /* 5. divide by the number multiplying the letter */
  const co = coefOf(Vside()), rhs = constOf(Oside()), s = qdiv(rhs, co);
  if (!qeq(co, ONE)) {
    L = [T_(1, v)]; R = [T_(s)];
    out.push({ k: 'div', say: 'Divide both sides by ' + n(co) + (qsign(co) < 0 ? ', sign and all.' : '.'), eq: eqNow(), co, rhs,
      walk: [numCalc('div', rhs, co, 'What is ' + M(calcText('div', rhs, co)) + '?')] });
  } else if (vs === 'R') { L = [T_(1, v)]; R = [T_(s)]; out.push({ k: 'flip', say: 'So ' + v + ' = ' + n(s) + '.', eq: eqNow(), walk: [] }); }
  return out;
}
/* the check: the value put back into the first equation, both sides */
function checkSay(e, s) {
  const lv = E.evalSide(e.L, s), rv = E.evalSide(e.R, s), one = side => side.length === 1 && side[0].k === 't' && !side[0].v;
  const L = one(e.L) ? n(lv) : substT(e.L, s) + ' = ' + n(lv), R = one(e.R) ? n(rv) : substT(e.R, s) + ' = ' + n(rv);
  return { ok: qeq(lv, rv), s: 'Check in the first equation: ' + L + (one(e.R) ? ', and the right side is ' + R : ' and ' + R) + (qeq(lv, rv) ? ' — the same number on both sides.' : '.') };
}
/* the worked lines of an equation (Hint 3) */
function eqLines(e) {
  const st = steps(e), out = st.map(x => ({ say: x.say, ex: x.eq }));
  const en = ending(e);
  if (en.kind === 'one') { const c = checkSay(e, en.s); out.push({ say: c.s }); }
  return out;
}
function eqWalk(e) { return steps(e).reduce((a, x) => a.concat(x.walk || []), []); }
/* the generic mistakes of the last steps — the number added undone the wrong way, stopping before dividing, multiplying
   instead of dividing, the sign of the answer lost — read from the equation just before them */
function tailModels(e) {
  const st = steps(e), out = [], en = ending(e); if (en.kind !== 'one') return out;
  const s = en.s, c = st.find(x => x.k === 'const'), d = st.find(x => x.k === 'div'), v = e.v;
  const ci = st.indexOf(c), di = st.indexOf(d);
  if (c) out.push({ v: qdiv(qadd(c.o0, c.k0), c.co), say: qsign(c.k0) > 0 ? 'added ' + n(c.k0) + ' instead of subtracting it: + ' + n(c.k0) + ' is undone by subtracting ' + n(c.k0) : 'subtracted ' + n(qabs(c.k0)) + ' instead of adding it: − ' + n(qabs(c.k0)) + ' is undone by adding ' + n(qabs(c.k0)), step: null });
  if (d) { const K = d.co, prod = qmul(s, K);
    out.push({ v: prod, say: 'stopped one step short: that is the value of ' + M(term(K, v)) + '. Now divide by ' + n(K), step: null });
    if (!qeq(qabs(K), ONE)) out.push({ v: qmul(prod, K), say: 'multiplied by ' + n(K) + ' instead of dividing', step: null });
    if (qsign(K) < 0) out.push({ v: qneg(s), say: 'divided by ' + n(qabs(K)) + ' instead of ' + n(K) + ': the sign goes with the number', step: null });
  }
  if (s.n !== 0n && !out.some(m => qeq(m.v, qneg(s)))) { const sp = signSpots(st);
    out.push({ v: qneg(s), say: sp.length ? 'lost a minus sign along the way: ' + n(qneg(s)) + ' is the right size, with the wrong sign. ' + (sp.length > 1 ? 'The signs to watch in this equation: ' : 'The sign to watch in this equation: ') + sp.join('; ') + '. Find the step where yours went the other way'
      : 'put in a minus sign this equation never makes: every number in it and in its work is positive. Put your answer back in and the two sides do not match', step: null, sign: true }); }
  return out;
}
/* where a sign goes missing in THIS equation, in its own numbers (14 Nov 2026: "lost a minus sign" said only "check it"): a
   negative distributed, a term moved across the equals sign (taken from, or added to, both sides), the division — each with
   its right value, and only where a negative number is in it. At most three, in the order the work meets them. */
function signSpots(st) {
  const out = [], neg = (...q) => q.some(x => qsign(x) < 0), d = st.find(x => x.k === 'dist'), vr = st.find(x => x.k === 'var'), c = st.find(x => x.k === 'const'), dv = st.find(x => x.k === 'div');
  if (d) d.gs.forEach(g => { const F0 = g.fr && !isInt(g.f) ? E.fracT(g.f) : n(g.f);
    g.t.forEach(t => { if (!t.v && neg(g.f, t.c)) out.push('where the ' + F0 + ' multiplies the ' + n(t.c) + ', (' + F0 + ')(' + n(t.c) + ') = ' + n(qmul(g.f, t.c))); }); });
  const cl = st.find(x => x.k === 'coll');
  if (cl) cl.groups.forEach(g => { if (g.some(c => qsign(c.c) < 0)) { const sum = g.reduce((a, c) => qadd(a, c.c), ZERO); out.push('where the like terms are collected, ' + sideT(g) + ' = ' + sideT([T_(sum, g[0].v)])); } });
  if (vr && neg(vr.take, vr.other, qsub(vr.other, vr.take))) out.push('where the ' + termT(vr.take, vr.eq.v) + ' moves across the equals sign (' + termT(qabs(vr.take), vr.eq.v) + (qsign(vr.take) < 0 ? ' added to' : ' taken from') + ' both sides), ' + calcText('sub', vr.other, vr.take) + ' = ' + n(qsub(vr.other, vr.take)));
  if (c && neg(c.o0, c.k0, qsub(c.o0, c.k0))) out.push('where the ' + (qsign(c.k0) > 0 ? '+ ' : '− ') + n(qabs(c.k0)) + ' moves across the equals sign (' + n(qabs(c.k0)) + (qsign(c.k0) > 0 ? ' taken from' : ' added to') + ' both sides), ' + (qsign(c.k0) > 0 ? calcText('sub', c.o0, c.k0) : calcText('add', c.o0, qabs(c.k0))) + ' = ' + n(qsub(c.o0, c.k0)));
  if (dv && neg(dv.rhs, dv.co)) out.push('in the division, ' + calcText('div', dv.rhs, dv.co) + ' = ' + n(qdiv(dv.rhs, dv.co)));
  return out.slice(0, 3);
}

/* ------------------------------------------------------------------ the families of typed answers */
const F = {};
const vv = p => p.eq.v;
/* Q1 — like terms and one distribution */
F.like = {
  rule: () => 'Distribute first — the number in front of the parentheses multiplies EVERY term inside. Then collect the like terms, undo the number added, and divide. Check in the first equation.',
  models: p => { const x = p.prm, v = vv(p), sd = x.form === 'g-t' ? -x.d : x.d, K = x.K, ab = x.a * x.b, ac = x.a * x.c, out = [
    { v: Q(x.r - x.c, K), say: 'multiplied only the ' + termT(x.b, v) + ' by ' + x.a + ': the ' + x.a + ' multiplies the ' + n(Q(x.c)) + ' too, so it is ' + n(Q(ac)) + ', not ' + n(Q(x.c)), step: 0 },
    { v: Q(x.r - ac, ab), say: 'left the ' + termT(Q(sd), v) + ' out: it is a like term of ' + termT(ab, v) + ' — collect them, ' + termT(ab, v) + (sd < 0 ? ' − ' : ' + ') + termT(Math.abs(sd), v) + ' = ' + termT(K, v), step: 1 }];
    if (ab - sd !== 0) out.push({ v: Q(x.r - ac, ab - sd), say: (sd < 0 ? 'added the ' + termT(x.d, v) + ' instead of taking it away' : 'took the ' + termT(x.d, v) + ' away instead of adding it') + ': ' + termT(ab, v) + (sd < 0 ? ' − ' : ' + ') + termT(x.d, v) + ' = ' + termT(K, v), step: 1 });
    return out.concat(tailModels(p.eq)); },
  sol: p => eqLines(p.eq), walk: p => eqWalk(p.eq)
};
/* Q2 — variables on both sides */
F.both = {
  rule: () => 'Take the same variable term from both sides, so the letter is on one side only. Then undo the number added and divide. Check in both sides of the first equation.',
  models: p => { const x = p.prm, v = vv(p), out = [];
    if (x.a + x.c !== 0) out.push({ v: Q(x.d - x.b, x.a + x.c), say: 'added the ' + v + '-terms instead of taking one from both sides: ' + termT(x.a, v) + ' and ' + termT(x.c, v) + ' are on different sides, so take ' + termT(Math.min(x.a, x.c), v) + ' from both', step: 0 });
    return out.concat(tailModels(p.eq)); },
  sol: p => eqLines(p.eq), walk: p => eqWalk(p.eq)
};
/* Q3 — parentheses on both sides, a fraction multiplying one of them. Each mistake is the equation as the slip leaves it,
   solved: a group's number in front given to its first term only; the sign of a negative one lost on its second term */
const facT = g => g.fr && !isInt(g.f) ? E.fracT(g.f) : n(g.f);
function slipEq(e, fn) { const m = side => side.map(c => c.k === 'g' ? fn(c) : c); return { L: m(e.L), R: m(e.R), v: e.v }; }
function solvedOf(e) { const en = ending(e); return en.kind === 'one' ? en.s : null; }
F.parens = {
  rule: () => 'Distribute on both sides — each number in front multiplies every term inside its own parentheses, a fraction too. Then take the same variable term from both sides and solve. Check in both sides.',
  models: p => { const e = p.eq, v = vv(p), gs = e.L.concat(e.R).filter(c => c.k === 'g'), out = [];
    const first = g => [T_(qmul(g.f, g.t[0].c), g.t[0].v), T_(g.t[1].c)].map(t => Object.assign(t, { k: 't' }));
    const asG = arr => G_(1, arr);
    const one = (g, say) => { const s0 = solvedOf(slipEq(e, c => c === g ? asG(first(c)) : c)); if (s0) out.push({ v: s0, say, step: 0 }); };
    const both = solvedOf(slipEq(e, c => asG(first(c))));
    if (both) out.push({ v: both, say: 'multiplied only the first term inside each pair of parentheses: the number in front multiplies the second term too', step: 0 });
    gs.forEach(g => one(g, 'multiplied only the ' + termT(g.t[0].c, v) + ' by ' + facT(g) + ': the ' + facT(g) + ' multiplies the ' + n(g.t[1].c) + ' too, so it is ' + n(qmul(g.f, g.t[1].c))));
    gs.filter(g => qsign(g.f) < 0).forEach(g => { const s0 = solvedOf(slipEq(e, c => c === g ? asG([T_(qmul(g.f, g.t[0].c), v), T_(qneg(qmul(g.f, g.t[1].c)))]) : c));
      if (s0) out.push({ v: s0, say: 'lost the sign on the second term: (' + facT(g) + ')(' + n(g.t[1].c) + ') = ' + n(qmul(g.f, g.t[1].c)), step: 0 }); });
    const L = lin(e.L), R = lin(e.R), sum = qadd(L.a, R.a);
    if (sum.n !== 0n) out.push({ v: qdiv(qsub(R.b, L.b), sum), say: 'added the ' + v + '-terms instead of taking one from both sides', step: 1 });
    return out.concat(tailModels(e)); },
  sol: p => eqLines(p.eq), walk: p => eqWalk(p.eq)
};
/* Q4 — a decimal distributed (the state's most common miss: the decimal to the first term only) */
F.decimal = {
  rule: () => 'The decimal in front of the parentheses multiplies EVERY term inside — both of them, signs and all. Then take the same variable term from both sides and solve. Check in both sides.',
  models: p => { const x = p.prm, v = vv(p), k = qdec(x.k), ka = qv(x.ka), kb = qv(x.kb), d = qv(x.d), c = Q(x.c), out = [];
    const den1 = qsub(ka, c); out.push({ v: qdiv(qsub(d, Q(x.b)), den1), say: 'multiplied only the ' + termT(x.a, v) + ' by ' + n(k) + ' — the most common slip on this kind of equation: the ' + n(k) + ' multiplies the ' + n(Q(x.b)) + ' too, so it is ' + n(kb) + ', not ' + n(Q(x.b)), step: 0 });
    if (x.a !== x.c) out.push({ v: qdiv(qsub(d, kb), Q(x.a - x.c)), say: 'multiplied only the ' + n(Q(x.b)) + ' by ' + n(k) + ': the ' + n(k) + ' multiplies the ' + termT(x.a, v) + ' too, so it is ' + termT(ka, v), step: 0 });
    if (qsign(k) < 0) out.push({ v: qdiv(qadd(d, kb), den1), say: 'lost the sign of ' + n(k) + ' on the second term: (' + n(k) + ')(' + n(Q(x.b)) + ') = ' + n(kb), step: 0 });
    const den2 = qadd(ka, c); if (den2.n !== 0n) out.push({ v: qdiv(qsub(d, kb), den2), say: 'added the ' + v + '-terms instead of taking one from both sides', step: 1 });
    return out.concat(tailModels(p.eq)); },
  sol: p => eqLines(p.eq), walk: p => eqWalk(p.eq)
};
/* Q6 — the box */
function boxParts(p) { const x = p.prm, v = 'x', g = G_(x.a, [T_(x.b, v), T_(x.c)]), dt = T_(x.form === 'g-t' ? -x.d : x.d, v), L = x.form === 't+g' ? [dt, g] : [g, dt];
  return { x, L, simp: [T_(x.K, v), T_(x.C)], sd: x.form === 'g-t' ? -x.d : x.d }; }
F.box = {
  rule: p => 'Simplify the left side first. ' + (p.prm.goal === 'none' ? 'No solution: the same number multiplies x on both sides, and the numbers added are different — then it ends at a = b, never true.' : 'Infinitely many: both sides are the same expression — then it ends at a = a, always true.'),
  models: p => { const { x, sd } = boxParts(p), ab = x.a * x.b, out = [];
    if (x.goal === 'allc') {
      out.push({ v: Q(x.c), say: 'multiplied only the ' + termT(x.b, 'x') + ' by ' + x.a + ': the ' + x.a + ' multiplies the ' + n(Q(x.c)) + ' too, so the number added is ' + n(Q(x.C)), step: 0 });
      out.push({ v: Q(-x.C), say: 'lost the sign: ' + x.a + '(' + n(Q(x.c)) + ') = ' + n(Q(x.C)), step: 0 });
      out.push({ v: Q(x.K), say: 'gave the number multiplying x. The box here is the number added: it must match the ' + n(Q(x.C)) + ' on the left', step: 1 });
      return out; }
    out.push({ v: Q(ab), say: 'left the ' + termT(Q(sd), 'x') + ' out: collect it with the ' + termT(ab, 'x') + ', and the left side has ' + termT(x.K, 'x'), step: 0 });
    if (ab - sd !== 0) out.push({ v: Q(ab - sd), say: (sd < 0 ? 'added the ' + termT(x.d, 'x') + ' instead of taking it away' : 'took the ' + termT(x.d, 'x') + ' away instead of adding it') + ': ' + termT(ab, 'x') + (sd < 0 ? ' − ' : ' + ') + termT(x.d, 'x') + ' = ' + termT(x.K, 'x'), step: 0 });
    out.push({ v: Q(x.C), say: 'gave the number added on the left. The box multiplies x: it must match the ' + termT(x.K, 'x'), step: 1 });
    return out; },
  sol: p => { const { x, L, simp } = boxParts(p), e0 = { L, R: p.eq.R, v: 'x' }, st = steps({ L, R: [T_(0)], v: 'x' }), out = [];
    st.filter(s => s.k === 'dist' || s.k === 'coll').forEach(s => out.push({ say: s.say.replace(/^Distribute/, 'Simplify the left side. Distribute').replace(/^Collect/, 'Collect'), ex: { L: s.eq.L, R: p.eq.R, v: 'x' } }));
    const K = n(Q(x.K)), C = n(Q(x.C)), A = n(p.ans);
    if (x.goal === 'none') {
      out.push({ say: 'No solution needs the same number multiplying x on both sides and different numbers added: ' + C + ' on the left and ' + n(Q(x.e)) + ' on the right are different, so the box is ' + K + '.' });
      out.push({ say: 'With ' + K + ' in the box: take ' + termT(x.K, 'x') + ' from both sides, and ' + C + ' = ' + n(Q(x.e)) + ' is left — never true: no solution. Any other number in the box gives one solution.', ex: '□ = ' + A });
    } else if (x.goal === 'allx') {
      out.push({ say: 'The numbers added already match: ' + C + ' on both sides. Infinitely many needs the same number multiplying x too, so the box is ' + K + '.' });
      out.push({ say: 'With ' + K + ' in the box both sides are ' + sideT(simp) + ': take ' + termT(x.K, 'x') + ' from both sides, and ' + C + ' = ' + C + ' is left — always true: infinitely many solutions.', ex: '□ = ' + A });
    } else {
      out.push({ say: 'The x-terms already match: ' + termT(x.K, 'x') + ' on both sides. Infinitely many needs the same number added too, so the box is ' + C + '.' });
      out.push({ say: 'With ' + C + ' in the box both sides are ' + sideT(simp) + ': take ' + termT(x.K, 'x') + ' from both sides, and ' + C + ' = ' + C + ' is left — always true: infinitely many solutions.', ex: '□ = ' + A });
    }
    return out; },
  walk: p => { const { x, L } = boxParts(p), st = steps({ L, R: [T_(0)], v: 'x' }), w = [];
    st.filter(s => s.k === 'dist' || s.k === 'coll').forEach(s => w.push(...s.walk));
    const K = Q(x.K), C = Q(x.C);
    w.push(numS('So the left side is ' + M(sideH([T_(x.K, 'x'), T_(x.C)])) + '. What number multiplies x on the left?', K, 'It is the number in front of x once the left side is simplified.'));
    if (x.goal === 'allc') w.push(numS('Infinitely many: both sides must be the same expression. What number is added on the left?', C, 'Look at the number on its own, sign and all.'));
    else w.push(choice(x.goal === 'none' ? 'For no solution, what goes in the box?' : 'For infinitely many solutions, what goes in the box?', [ch('The number that multiplies x on the left', 1),
      ch('The number added on the left', 0, 'The box is in front of x: it multiplies x.'), ch('Any number but that one', 0, 'Any other number gives two different x-terms, and then the equation has one solution.')]));
    return w; }
};
/* Q7 — two plans that cost the same */
function planParts(p) { const x = p.prm, P = E.PLANS[x.ctx]; return { x, P, v: P.v, eq: p.eq }; }
F.plans = {
  rule: p => { const { P, v } = planParts(p); return 'Write each plan’s cost for ' + v + ' ' + P.unit + ': its fee plus its price each ' + P.one + ' times ' + v + '. Set the two costs equal and solve. Check: the two plans cost the same.'; },
  models: p => { const { x } = planParts(p), out = [];
    out.push({ v: Q(x.f - x.g, x.b), say: 'divided the fee by the second price: that leaves out the $' + x.a + ' the first one costs each time', step: 0 });
    out.push({ v: Q(x.f - x.g, x.a), say: 'divided the fee by the first price: the second one costs $' + x.b + ' each time, so the gap closes by ' + x.b + ' − ' + x.a + ' = ' + (x.b - x.a) + ' each time', step: 0 });
    out.push({ v: Q(x.f - x.g, x.a + x.b), say: 'added the two prices: the gap closes by their difference, ' + x.b + ' − ' + x.a + ' = ' + (x.b - x.a) + ', each time', step: 1 });
    out.push({ v: Q(x.f + x.a * x.n), say: 'gave the cost. The question asks how many ' + E.PLANS[x.ctx].unit + ': that is the letter', step: null });
    return out; },
  sol: p => { const { x, P, v, eq } = planParts(p), st = steps(eq), A = x.f + x.a * x.n;
    return [{ say: P.who[0][0].toUpperCase() + P.who[0].slice(1) + ' costs ' + sideT(eq.L) + ' for ' + v + ' ' + P.unit + '; ' + P.who[1] + ' costs ' + sideT(eq.R) + '. They cost the same when', ex: eq }]
      .concat(st.map(s => ({ say: s.say, ex: s.eq })))
      .concat([{ say: 'Check: ' + P.who[0] + ' costs ' + substT(eq.L, Q(x.n)) + ' = ' + A + ' and ' + P.who[1] + ' costs ' + substT(eq.R, Q(x.n)) + ' = ' + A + ' — both $' + A + ', after ' + x.n + ' ' + P.unit + '.' }]); },
  walk: p => { const { x, P, v, eq } = planParts(p);
    return [choice('Which equation says the two cost the same after ' + v + ' ' + P.unit + '?', [ch(M(eqH(eq)), 1),
      ch(M(eqH({ L: [T_(x.f), T_(x.b, v)], R: x.g ? [T_(x.g), T_(x.a, v)] : [T_(x.a, v)], v })), 0, 'Each fee goes with its own price: ' + P.who[0] + ' charges $' + x.a + ' each ' + P.one + '.'),
      ch(M(eqH({ L: [T_(x.f + x.a, v)], R: [T_(x.b, v)], v })), 0, 'The fee is paid once; only the price each ' + P.one + ' is multiplied by ' + v + '.')])].concat(eqWalk(eq)); }
};
/* Q13(a) — a value missing from a table */
F.tableGap = {
  rule: () => 'Put the column’s x into the equation: the number multiplying x, times x, plus the number added. Each step of 1 in x changes y by the same amount.',
  models: p => { const l = p.l1, l2 = p.l2, xm = Q(p.miss), out = [];
    out.push({ v: yAt(l, p.miss - 1), say: 'copied the number beside it. Each column has its own x: put x = ' + p.miss + ' into the equation', step: 0 });
    out.push({ v: yAt(l, p.miss + 1), say: 'copied the number beside it. Each column has its own x: put x = ' + p.miss + ' into the equation', step: 0 });
    if (!qeq(qabs(l.m), ONE)) out.push({ v: qadd(l.m, qadd(xm, l.b)), say: 'added the ' + n(l.m) + ' and the x instead of multiplying: ' + termT(l.m, 'x') + ' means ' + n(l.m) + ' times x', step: 0 });
    if (l.b.n !== 0n) out.push({ v: qsub(qmul(l.m, xm), l.b), say: 'took the sign of the ' + n(l.b) + ' the wrong way', step: 1 });
    out.push({ v: yAt(l2, p.miss), say: 'used the other equation, ' + lineT(l2) + '. This table is for ' + lineT(l), step: 0 });
    return out; },
  sol: p => { const l = p.l1, y = yAt(l, p.miss); return [{ say: 'The missing number is in the column x = ' + p.miss + '. Put ' + p.miss + ' into ' + lineT(l) + ': ' + (l.m.n ? substT(E.lineSide(l), Q(p.miss)) + ' = ' + n(y) : n(y)) + '.', ex: 'y = ' + nHtml(y) },
    { say: 'It fits the pattern: each step of 1 in x ' + (qsign(l.m) > 0 ? 'adds ' + n(l.m) + ' to' : 'takes ' + n(qabs(l.m)) + ' from') + ' y, so ' + n(yAt(l, p.miss - 1)) + ', ' + n(y) + ', ' + n(yAt(l, p.miss + 1)) + '.' }]; },
  walk: p => { const l = p.l1, xm = Q(p.miss);
    if (qeq(qabs(l.m), ONE)) return [numS('The column is x = ' + p.miss + '. Put it into ' + M(lineH(l)) + ': what is ' + M(substT(E.lineSide(l), xm)) + '?', yAt(l, p.miss), arith('add', qmul(l.m, xm), l.b))];
    return [numCalc('mul', l.m, xm, 'The column is x = ' + p.miss + '. What is ' + M(calcText('mul', l.m, xm)) + '?'), numCalc('add', qmul(l.m, xm), l.b, 'Now add the number added in ' + M(lineH(l)) + '. What is ' + M(calcText('add', qmul(l.m, xm), l.b)) + '?')]; }
};

/* ---------- the typed answers that are two numbers: an ordered pair, or the weeks and the amount of a story */
const pairOf = p => p.ans;
const PF = {};
/* every typed answer of two numbers has two boxes since 15 Nov 2026 (the kit's several boxes in one part): x = ▢ and y = ▢, or
   after ▢ weeks and $▢ each — so a swap is said box by box */
const swapM = p => ({ v: [p.ans[1], p.ans[0]], say: 'swapped the coordinates: the x box takes ' + (p.fam === 'tableSol' ? 'the column, ' + n(p.ans[0]) + ', and the y box what both tables give there, ' : 'how far across, ' + n(p.ans[0]) + ', and the y box how far up or down, ') + n(p.ans[1]) });
const pairT = E.pairT;
const yAxis = (l, which) => ({ v: [ZERO, l.b], say: 'gave where ' + which + ' meets the y-axis, ' + pairT(ZERO, l.b) + ': that point is on one line only' });
function bothSay(p, x, y) {                                       /* a pair put into both equations, as a student checks it */
  return [p.l1, p.l2].map(l => { const got = yAt(l, x), ok = qeq(got, y); return lineT(l) + ': ' + (l.m.n ? substT(E.lineSide(l), x) + ' = ' : '') + n(got) + (ok ? ', true' : ', not ' + n(y)); }).join('; ');
}
PF.readGraph = {
  rule: () => 'The solution is the point of intersection, where the two lines meet. Read x first — across — then y — up or down — and check the pair in both equations.',
  models: p => { const out = [swapM(p), yAxis(p.l1, 'the solid line'), yAxis(p.l2, 'the dashed line')];
    [p.l1, p.l2].forEach((l, i) => { if (l.m.n !== 0n) { const xi = qdiv(qneg(l.b), l.m); if (isInt(xi)) out.push({ v: [xi, ZERO], say: 'gave where the ' + (i ? 'dashed' : 'solid') + ' line meets the x-axis, ' + pairT(xi, ZERO) + ': on one line only' }); } });
    return out; },
  sol: p => [{ say: 'The two lines intersect at ' + pairT(p.ans[0], p.ans[1]) + ': x = ' + n(p.ans[0]) + ' across, then y = ' + n(p.ans[1]) + (qsign(p.ans[1]) < 0 ? ' down.' : ' up.') },
    { say: 'Check it in both equations — ' + bothSay(p, p.ans[0], p.ans[1]) + '.', ex: pairH(p.ans[0], p.ans[1]) }],
  walk: p => [choice('Where on the graph is the solution of the system?', [ch('At the point of intersection, where the two lines meet', 1), ch('Where the solid line meets the y-axis', 0, 'That point is on the solid line only. A solution is on both lines.'),
      ch('Where the dashed line meets the y-axis', 0, 'That point is on the dashed line only. A solution is on both lines.')]),
    numS('From the crossing, go straight ' + (qsign(p.ans[1]) < 0 ? 'up' : 'down') + ' to the x-axis. What is the x of the crossing?', p.ans[0], 'Read the number on the x-axis under (or over) the crossing.'),
    numS('From the crossing, go straight across to the y-axis. What is its y?', p.ans[1], 'Read the number on the y-axis level with the crossing, sign and all.')]
};
PF.tableSol = {
  rule: () => 'The solution is the column where both tables give the same y: that x and that y, x first.',
  models: p => { const out = [swapM(p)], xs = p.xs;
    let best = null; xs.forEach(x => { if (qeq(Q(x), p.ans[0]) || x === p.miss) return; const d = qnum(qabs(qsub(yAt(p.l1, x), yAt(p.l2, x)))); if (!best || d < best.d) best = { x, d }; });
    if (best) out.push({ v: [Q(best.x), yAt(p.l1, best.x)], say: 'took the column where the two y’s are closest, x = ' + best.x + ' — there ' + n(yAt(p.l1, best.x)) + ' and ' + n(yAt(p.l2, best.x)) + ' are near but not equal. Near is not the same' });
    out.push({ v: [ZERO, p.l1.b], say: 'gave the first column of one table: a solution is where BOTH tables give the same y' });
    out.push({ v: [Q(p.miss), yAt(p.l1, p.miss)], say: 'gave the missing value’s column: the solution is where the two tables agree' });
    return out; },
  sol: p => [{ say: 'Look along the two rows for the column where both give the same y: at x = ' + n(p.ans[0]) + ' both give ' + n(p.ans[1]) + '.' },
    { say: 'Check it in both equations — ' + bothSay(p, p.ans[0], p.ans[1]) + '. The solution is ' + pairT(p.ans[0], p.ans[1]) + '.', ex: pairH(p.ans[0], p.ans[1]) }],
  walk: p => [numS('In which column do the two tables give the same y? What is its x?', p.ans[0], 'Compare the two y’s in each column, one column at a time.'),
    numS('What y do both tables give in that column?', p.ans[1], 'Read either table in that column: they agree there.')]
};
const storyAmt = (p, v) => p.st.unit === 'dollars' ? '$' + n(v) : n(v) + ' cm';   /* the story's amt, from the part's own data: a part holds no function (16 Nov 2026: a part must survive Kit.pack, for the test the site judges) */
PF.storyMeet = {
  rule: () => 'The two amounts are equal at the point of intersection: read the weeks across, then the amount up. Say it with its units.',
  models: p => { const out = [{ v: [p.ans[1], p.ans[0]], say: 'swapped the two boxes: the weeks are across the bottom (x) and go in the weeks box, and the amount is up the side (y)' },
    { v: [ZERO, p.l2.b], say: 'gave where one line starts, at 0 weeks: that is ' + p.B + '’s start, not where the two meet' },
    { v: [ZERO, p.l1.b], say: 'gave where one line starts, at 0 weeks: that is ' + p.A + '’s start, not where the two meet' }];
    const x1 = qadd(p.ans[0], ONE); out.push({ v: [x1, yAt(p.l1, x1)], say: 'read the crossing one grid line too far: at ' + n(x1) + ' weeks the two are no longer equal' });
    return out; },
  sol: p => { const [x, y] = p.ans, l1 = p.l1, l2 = p.l2;
    return [{ say: p.A + '’s line is ' + lineT(l1) + ' and ' + p.B + '’s is ' + lineT(l2) + '. They intersect at ' + pairT(x, y) + '.' },
      { say: 'Check: ' + substT(E.lineSide(l1), x) + ' = ' + n(y) + ' and ' + substT(E.lineSide(l2), x) + ' = ' + n(y) + '.' },
      { say: 'After ' + n(x) + ' weeks they are the same: ' + storyAmt(p, y) + ' ' + p.st.each + '.', ex: 'After ' + n(x) + ' weeks; ' + storyAmt(p, y) + ' ' + p.st.each }]; },
  walk: p => [choice('Where on the graph are the two amounts the same?', [ch('At the point of intersection', 1), ch('Where ' + p.B + '’s line starts, at 0 weeks', 0, 'At 0 weeks the two lines are at different heights: their amounts are not the same yet.'),
      ch('Where a line reaches the top of the graph', 0, 'The edge of the graph is only where the drawing stops.')]),
    numS('Go straight down from the point of intersection. How many weeks?', p.ans[0], 'Read the number on the weeks axis under the crossing.'),
    numS('Go straight across from the point of intersection. How much does each have then?', p.ans[1], 'Read the number on the ' + p.st.yname + ' axis level with the crossing.')]
};
/* the lead's ruling (14 Nov 2026), the paper's: within 0.1 of the KEY (the crossing rounded to the tenth), inclusive, exactly */
const near1 = (v, k, t) => !qlt(t, qabs(qsub(qv(v), k)));
const within = (p, x, y) => near1(x, p.ans[0], p.tol) && near1(y, p.ans[1], p.tol);
const rangeOf = (k, t) => [qsub(k, t), qadd(k, t)];
const fmt1 = v => n(qdec(v.toFixed(1)));
PF.estimate = {
  rule: () => 'Between the grid lines, estimate: read each coordinate to the nearest tenth (the pale lines are halves), and say “about”. Check the estimate in both equations — the two values come out close, not equal.',
  models: p => { const c = p.exact, out = [{ v: [p.ans[1], p.ans[0]], say: 'swapped the coordinates: the x box takes the reading across and the y box the reading up or down', within: true }];
    out.push({ v: [Q(Math.round(qnum(c.x))), Q(Math.round(qnum(c.y)))], say: 'took the nearest grid point. It is on neither line: the crossing is between the grid lines, so estimate each coordinate to the tenth', exact: true });
    out.push({ v: [ZERO, p.l1.b], say: 'gave where the solid line meets the y-axis: that point is on one line only', exact: true });
    out.push({ v: [ZERO, p.l2.b], say: 'gave where the dashed line meets the y-axis: that point is on one line only', exact: true });
    return out; },
  sol: p => { const c = p.exact, [ax, ay] = p.ans, rx = rangeOf(ax, p.tol), ry = rangeOf(ay, p.tol);
    return [{ say: 'The lines intersect between the grid lines: x is between ' + n(Q(Math.floor(qnum(c.x)))) + ' and ' + n(Q(Math.ceil(qnum(c.x)))) + ', about ' + n(ax) + '; y is between ' + n(Q(Math.floor(qnum(c.y)))) + ' and ' + n(Q(Math.ceil(qnum(c.y)))) + ', about ' + n(ay) + '.' },
      { say: 'Check the estimate in both equations — ' + [p.l1, p.l2].map(l => lineT(l) + ': ' + substT(E.lineSide(l), ax) + ' = ' + n(yAt(l, ax))).join('; ') + '. Both are close to ' + n(ay) + ': a good estimate.' },
      { say: 'Exactly, the point of intersection is x = ' + M(nHtml(c.x)) + ' and y = ' + M(nHtml(c.y)) + ': about ' + pairT(ax, ay) + ' to the nearest tenth. Anything from ' + n(rx[0]) + ' to ' + n(rx[1]) + ' and ' + n(ry[0]) + ' to ' + n(ry[1]) + ' is a careful reading.', ex: 'about ' + pairH(ax, ay) }]; },
  walk: p => [numS('Find the point of intersection on the graph. About what is its x, to the nearest tenth?', p.ans[0], 'Is it nearer the grid line to its left or to its right? The pale line in between is the half.', null, { tol: p.tol, near: p.ans[0] }),
    numS('About what is its y, to the nearest tenth?', p.ans[1], 'Is it nearer the grid line below it or above it? The pale line in between is the half.', null, { tol: p.tol, near: p.ans[1] })]
};

/* ------------------------------------------------------------------ marking a typed answer */
const RULE = p => (F[p.fam] || PF[p.fam]).rule(p);
/* a typed decimal that is a never-ending number rounded, or cut off, to the places the student typed */
function roundedTo(val, typed, least) {
  if (places(val) >= 0) return false;
  const m = /\.(\d+)/.exec(String(typed)); if (!m || m[1].length < least) return false;
  const f = Math.pow(10, m[1].length), x = qnum(val) * f, y = Number(String(typed).replace(/[^\d.\-−]/g, '').replace('−', '-')) * f;
  return Math.abs(Math.round(x) - y) < 1e-6 || Math.abs(Math.trunc(x) - y) < 1e-6;
}
const keyOfPart = p => p.fam === 'box' ? '□ = ' + nHtml(p.ans) : p.unit ? nHtml(p.ans) + ' ' + p.unit : p.v ? vi(p.v) + ' = ' + nHtml(p.ans) : nHtml(p.ans);
function numFeedback(p, typed) {
  const r = E.readAns(typed, 'num'), rule = RULE(p), ans = p.ans;
  if (!r.ok) return r.blank ? { v: 'blank', what: [] } : { v: 'unread', what: [r.msg] };
  if (r.unsolved) return { v: 'wrong', what: ['Finish solving: get ' + (p.v ? vi(p.v) : 'the letter') + ' by itself, then type its value.'], rule };
  const val = r.nums[0].q;
  if (qeq(val, ans)) {
    if (r.shape === 'expr') return { v: 'form', what: ['That works out to the right number — now finish the arithmetic and type it as one number.'], rule: '' };
    if (r.letter && p.v && r.letter !== p.v) return { v: 'form', what: ['Right number — but this question’s letter is ' + vi(p.v) + ': ' + M(vi(p.v) + ' = ' + nHtml(ans)) + '.'], rule: '' };
    return { v: 'right', what: [] };
  }
  const fam = F[p.fam], mods = (fam.models(p) || []).filter(m => !qeq(m.v, ans)), hit = mods.filter(m => qeq(m.v, val) || roundedTo(m.v, typed, 2));
  if (hit.length) return { v: 'wrong', what: [joinSays(hit)], rule, step: hit[0].step == null ? null : hit[0].step };
  if (r.shape === 'expr') return { v: 'wrong', what: ['That works out to ' + n(val) + ', which isn’t the answer. Type just your final number.'], rule };
  let chk = '';
  if (p.fam === 'box') { const e = { L: p.eq.L, R: E.fill(p.eq.R, val), v: 'x' }, en = ending(e);
    chk = 'With ' + n(val) + ' in the box, ' + eqT(e) + ' has ' + (en.kind === 'one' ? 'one solution, x = ' + n(en.s) : en.kind === 'none' ? 'no solution' : 'infinitely many solutions') + '.'; }
  else if (p.fam === 'plans') { const x = p.prm, P = E.PLANS[x.ctx], a = E.evalSide(p.eq.L, val), b = E.evalSide(p.eq.R, val);
    chk = 'With ' + n(val) + ' ' + P.unit + ': ' + P.who[0] + ' costs ' + substT(p.eq.L, val) + ' = ' + n(a) + ' and ' + P.who[1] + ' costs ' + substT(p.eq.R, val) + ' = ' + n(b) + ' — not the same.'; }
  else if (p.fam === 'tableGap') chk = 'Put x = ' + p.miss + ' into ' + lineT(p.l1) + ' and work it out.';
  else if (p.eq) { const lv = E.evalSide(p.eq.L, val), rv = E.evalSide(p.eq.R, val), lone = sd => sd.length === 1 && sd[0].k === 't' && !sd[0].v;
    const sv = (sd, v0) => lone(sd) ? n(v0) : substT(sd, val) + ' = ' + n(v0);
    chk = 'Check it: with ' + p.v + ' = ' + n(val) + ', the left side is ' + sv(p.eq.L, lv) + ' and the right side is ' + sv(p.eq.R, rv) + ' — not equal.'; }
  if (qeq(val, qneg(ans))) return { v: 'wrong', what: ['The size is right, but the sign isn’t. ' + chk], rule };
  return { v: 'wrong', what: [chk + ' Tap Hint to go one step at a time.'], rule };
}
/* the two boxes (15 Nov 2026): each read by this unit's own number reader. A box may carry its own letter ("x = 4" in the x box)
   or its own unit ("5 weeks", "$40", "12 cm"), never the other box's; two numbers in one box are not read as a pair */
const BOXV = ['x', 'y'];
const boxName = (p, k) => p.kind === 'story' ? (k ? 'amount' : 'weeks') : BOXV[k];
const boxNames = p => p.kind === 'story' ? 'the weeks in the weeks box and the amount in the other' : 'the x in the x box and the y in the y box';
function readBoxes(p, typed) {
  const got = [];
  if (typed.every(t => t == null || !String(t).trim())) return { ok: false, blank: true };
  for (let k = 0; k < 2; k++) {
    const raw = typed[k] == null ? '' : String(typed[k]), t = p.kind === 'story' ? raw.replace(/\btall\b/gi, ' ') : raw, v = BOXV[k], nm = boxName(p, k);
    if (!t.trim()) return { ok: false, msg: 'Fill in every box: the ' + nm + ' box is still empty.' };
    const two = E.readAns(t, p.kind === 'story' ? 'story' : 'pair');
    if (two.ok && two.nums && two.nums.length === 2) return { ok: false, msg: 'The ' + nm + ' box has two numbers. Put ' + boxNames(p) + '.' };
    const r = E.readAns(t, 'num');
    if (!r.ok) return { ok: false, msg: 'The ' + nm + ' box: ' + r.msg };
    if (r.unsolved || !r.nums || r.nums.length !== 1 || r.shape === 'expr') return { ok: false, msg: 'The ' + nm + ' box: type just the number, like ' + (p.kind === 'story' ? (k ? '40' : '5') : '4 or −2') + '.' };
    if (r.letter && r.letter !== v) return { ok: false, msg: 'The ' + nm + ' box takes the ' + (p.kind === 'story' ? nm : v) + '. Put ' + boxNames(p) + '.' };
    const tag = r.nums[0].tag;
    if (p.kind === 'story' && tag && tag !== (k ? 'amt' : 'count')) return { ok: false, msg: 'The ' + nm + ' box takes the ' + nm + '. Put ' + boxNames(p) + '.' };
    got.push(r.nums[0]);
  }
  return { ok: true, nums: got, labels: true, shape: 'pair' };
}
function pairFeedback(p, typed) {
  const kind = p.kind === 'story' ? 'story' : 'pair', r = Array.isArray(typed) ? readBoxes(p, typed) : E.readAns(typed, kind), rule = RULE(p), fam = PF[p.fam];
  if (!r.ok) return r.blank ? { v: 'blank', what: [] } : { v: 'unread', what: [r.msg] };
  const [x, y] = r.nums.map(z => z.q), est = p.fam === 'estimate';
  if (est ? within(p, x, y) : qeq(x, p.ans[0]) && qeq(y, p.ans[1])) return { v: 'right', what: [] };
  const mods = fam.models(p).filter(m => !(qeq(m.v[0], p.ans[0]) && qeq(m.v[1], p.ans[1])));
  const hit = mods.filter(m => est && m.within ? near1(x, m.v[0], p.tol) && near1(y, m.v[1], p.tol) : qeq(x, m.v[0]) && qeq(y, m.v[1]));
  if (hit.length) return { v: 'wrong', what: [joinSays(hit)], rule };
  if (est) {
    const okx = near1(x, p.ans[0], p.tol), oky = near1(y, p.ans[1], p.tol);
    return { v: 'wrong', what: [(okx ? 'Your x is a good estimate, but look again at y: ' : oky ? 'Your y is a good estimate, but look again at x: ' : 'Look again at the crossing: ') + 'check your two numbers in both equations — ' + [p.l1, p.l2].map(l => lineT(l) + ' gives ' + n(yAt(l, x)) + ' at x = ' + n(x)).join(', ') + '. A good estimate makes both close to its y.'], rule };
  }
  if (p.fam === 'storyMeet') {
    const a = yAt(p.l1, x), b = yAt(p.l2, x);
    return { v: 'wrong', what: [qeq(x, p.ans[0]) ? 'The weeks are right. Now the amount: from the point of intersection, go straight across to the ' + p.st.yname + ' axis and read it.' : 'After ' + n(x) + ' weeks ' + p.A + ' has ' + storyAmt(p, a) + ' and ' + p.B + ' has ' + storyAmt(p, b) + ' — not the same yet.'], rule };
  }
  const okx = qeq(x, p.ans[0]), oky = qeq(y, p.ans[1]), read = p.fam === 'tableSol' ? ['Find the column where both tables give the same y.', 'Read the y that both tables give in that column.'] : ['From the point of intersection, go straight up or down to the x-axis.', 'From the point of intersection, go straight across to the y-axis.'];
  const lead = okx ? 'Your x is right, but look again at the y. ' + read[1] + ' ' : oky ? 'Your y is right, but look again at the x. ' + read[0] + ' ' : '';
  return { v: 'wrong', what: [lead + 'Check x = ' + n(x) + ' and y = ' + n(y) + ' in both equations — ' + bothSay(p, x, y) + '. A solution makes both true.'], rule };
}
function feedback(p, typed) { return p.kind === 'num' ? numFeedback(p, typed) : pairFeedback(p, typed); }

/* ------------------------------------------------------------------ the choice questions */
/* a negative number in front of parentheses: its sign goes in with it (the slip that turns one ending into another) */
const negSay = p => { const g = p.eq.L.concat(p.eq.R).find(c => c.k === 'g' && qsign(c.f) < 0); if (!g) return ''; const t = g.t.find(t => !t.v);
  return ' Check the sign: (' + n(g.f) + ')(' + n(t.c) + ') = ' + n(qmul(g.f, t.c)) + '.'; };
const ENDW = { one: 'One solution', none: 'No solution', all: 'Infinitely many solutions' };
const endIdx = k => ['one', 'none', 'all'][k];
function endStep(p) { return steps(p.eq).find(s => s.k === 'end'); }
const MC = {
  /* Q5's parts: one ending each */
  endings: {
    why: (p, k) => { const got = endIdx(k), en = p.end, es = endStep(p), v = p.eq.v;
      if (en.kind === 'one') return got === 'none' ? (qeq(en.s, ZERO) ? 'It ends at ' + v + ' = 0 — and 0 is a number. ' + v + ' = 0 is one solution, not “no solution”.' : 'It ends at ' + v + ' = ' + n(en.s) + ': one number works.') : 'The ' + v + '-terms are different on the two sides, so they do not cancel: it ends at ' + v + ' = ' + n(en.s) + ', one solution.';
      if (en.kind === 'none') return got === 'all' ? 'The ' + v + '-terms match, but what is left, ' + es.left + ', is never true: no number works.' + negSay(p) : 'Once both sides are simplified the ' + v + '-terms are the same, so they cancel and ' + es.left + ' is left — never true, whatever ' + v + ' is: no solution.';
      return got === 'none' ? 'What is left, ' + es.left + ', is true — a true sentence like that means every number works.' + negSay(p) : 'The letter cancels and ' + es.left + ' is left — always true. That does not say ' + v + ' = 0: every number works.'; },
    rule: () => 'Simplify each side, take the same variable term from both sides, and read what is left: ' + vi('x') + ' = a number is one solution; a = a, always true, is infinitely many; a = b, never true, is no solution. ' + vi('x') + ' = 0 is one solution.',
    sol: p => { const lines = eqLines(p.eq).filter(l => !/^Check/.test(l.say)), en = p.end;
      if (en.kind === 'one') lines.push({ say: (qeq(en.s, ZERO) ? 'It ends at x = 0, and 0 is a number: ' : 'It ends at x = ' + n(en.s) + ': ') + 'one solution. ' + checkSay(p.eq, en.s).s.replace(/^Check in the first equation/, 'Check') });
      lines.push({ say: 'The answer is ' + ENDW[en.kind].toLowerCase() + '.' });
      return lines; },
    walk: p => { const w = eqWalk(p.eq), en = p.end; if (en.kind === 'one') w.push(choice('It ends at ' + M(vi(p.eq.v) + ' = ' + nHtml(en.s)) + '. How many solutions?', [ch('One solution', 1), ch('No solution', 0, qeq(en.s, ZERO) ? '0 is a number: ' + vi(p.eq.v) + ' = 0 is one solution.' : 'One number works.'), ch('Infinitely many solutions', 0, 'Only that one number makes it true.')], null, { keep: true })); return w; }
  },
  isSol: {
    /* each option is a verdict and a claim about this pair; a wrong one is answered with the two checks and what they show */
    truth: x => [x.l1, x.l2].map(L => onLine(L, x.px, x.py)),
    shows: x => { const t = MC.isSol.truth(x), P = pairT(Q(x.px), Q(x.py));
      return t[0] && t[1] ? P + ' makes both equations true: it is a solution.' : t[0] || t[1] ? P + ' makes only ' + lineT(t[0] ? x.l1 : x.l2) + ' true — one equation is not enough: it is not a solution.' : P + ' makes neither equation true: it is not a solution.'; },
    at: (x, i) => { const L = i ? x.l2 : x.l1, t = onLine(L, x.px, x.py);
      return lineT(L) + ' gives ' + substT(E.lineSide(L), Q(x.px)) + ' = ' + n(yAt(L, x.px)) + (t ? ', true' : ', not ' + n(Q(x.py))); },
    /* what is false in the option picked — its own words, so no two wrong options say the same — then the two checks */
    why: (x, k) => { const id = x.ids[k], t = MC.isSol.truth(x), L = [x.l1, x.l2].map(lineT), i = id === 'only1' ? 0 : 1;
      const lead = id === 'both' ? 'Not both equations are true.' : id === 'neither' ? L[t[0] ? 0 : 1] + ' is true for this pair.'
        : t[i] ? 'Not only ' + L[i] + ': ' + L[1 - i] + ' is true too.' : L[i] + ' is not true for this pair.';
      return lead + ' ' + MC.isSol.at(x, 0) + '; ' + MC.isSol.at(x, 1) + '. So ' + MC.isSol.shows(x); },
    rule: () => 'A solution of a system makes BOTH equations true. Put the x into each equation and see whether it gives the y — one equation is not enough.',
    sol: x => { const t = MC.isSol.truth(x);
      return [0, 1].map(i => ({ say: (i ? 'Second: ' : 'First: ') + MC.isSol.at(x, i).replace(/, true$/, ' — true.').replace(/, (not [^,]*)$/, ', $1 — false.') }))
        .concat([{ say: MC.isSol.shows(x) + ' The answer is ' + LET[x.correct] + '.' }]); },
    walk: x => { const t = MC.isSol.truth(x), Qx = Q(x.px), ask = L => numS('Put x = ' + n(Qx) + ' into ' + M(lineH(L)) + '. What y does it give?', yAt(L, x.px), L.m.n ? arith('mul', L.m, Qx) + ' Then add the number added.' : 'Read the number added.');
      const isIt = (i, w) => choice('Is that the pair’s y, ' + n(Q(x.py)) + '?', [ch(t[i] ? 'Yes — the ' + w + ' is true' : 'No — the ' + w + ' is false', 1), ch(t[i] ? 'No — the ' + w + ' is false' : 'Yes — the ' + w + ' is true', 0, 'Compare ' + n(yAt(i ? x.l2 : x.l1, x.px)) + ' with ' + n(Q(x.py)) + '.')], null, { keep: true });
      return [ask(x.l1), isIt(0, 'first'), ask(x.l2), isIt(1, 'second'),
        choice('So which answer is true of ' + M(pairH(Q(x.px), Q(x.py))) + '?', x.opts.map((o, i) => ch(LET[i], i === x.correct, i === x.correct ? '' : MC.isSol.why(x, i))), null, { keep: true })]; }
  },
  countCross: {
    why: (x, k) => k === 1 ? 'The lines intersect — at ' + pairT(x.cross.x, x.cross.y) + ' — so they share that point: one solution. Parallel lines would never meet.' : 'Two different lines that cross share one point only. Infinitely many is one line drawn for both equations.',
    rule: () => 'Two lines that intersect meet once, at their point of intersection: one solution. Parallel lines never meet: no solution. One line for both equations: every point of it is a solution.',
    sol: x => [{ say: 'The two lines intersect once, at ' + pairT(x.cross.x, x.cross.y) + ': ' + lineT(x.l1) + ' gives ' + substT(E.lineSide(x.l1), x.cross.x) + ' = ' + n(x.cross.y) + ' and ' + lineT(x.l2) + ' gives ' + substT(E.lineSide(x.l2), x.cross.x) + ' = ' + n(x.cross.y) + '.' },
      { say: 'Different numbers multiply x, ' + n(x.l1.m) + ' and ' + n(x.l2.m) + ', so the lines must cross. One solution: the answer is A.' }],
    walk: x => [choice('Look at the graph. Do the two lines meet?', [ch('Yes — they intersect once', 1), ch('No — they never meet', 0, 'Follow the two lines: they cross. Lines with different numbers multiplying x always cross.'), ch('They are the same line', 0, 'There are two different lines on the graph.')]),
      choice('So how many solutions does the system have?', x.opts.map((o, i) => ch(o, i === 0, i ? MC.countCross.why(x, i) : '')), null, { keep: true })]
  },
  countPar: {
    why: (x, k) => x.same ? (k === 0 ? 'Both equations graph as the one line shown, so they share every point of it — not just one.' : 'The two equations are one line, written two ways: ' + lineT(x.l1.alt ? x.l2 : x.l1) + '. They share every point, so there is no shortage of solutions.')
      : (k === 0 ? 'Not every two lines cross: the same number, ' + n(x.l1.m) + ', multiplies x in both, so the lines are parallel — always the same distance apart.' : 'The same number multiplies x, but the numbers added, ' + n(x.l1.b) + ' and ' + n(x.l2.b) + ', are different: two parallel lines, not one.'),
    rule: () => 'The same number multiplying x and different numbers added: parallel lines, never meeting — no solution. One equation written two ways: one line — infinitely many solutions.',
    sol: x => x.same ? [{ say: 'Write both the same way: ' + lineT(x.l1.alt ? x.l1 : x.l2) + ' is ' + sideT(E.lineSide({ m: x.l1.m, b: x.l1.b })) + ' once the ' + n(x.l1.m) + ' is distributed.' },
      { say: 'Both equations are the one line shown, and every point of it is a solution: infinitely many solutions. The answer is C.' }]
      : [{ say: 'The same number, ' + n(x.l1.m) + ', multiplies x in both, and the numbers added are different: ' + n(x.l1.b) + ' and ' + n(x.l2.b) + '.' },
        { say: 'So the lines are parallel — always ' + n(qabs(qsub(x.l1.b, x.l2.b))) + ' apart up the side — and never meet: no solution. The answer is B.' }],
    walk: x => [choice('What number multiplies x in each equation' + (x.same ? ', once both are written without parentheses' : '') + '?', [ch('The same number in both', 1), ch('Different numbers', 0, 'Look again: ' + (x.same ? 'distribute first, then compare.' : 'both have ' + termT(x.l1.m, 'x') + '.'))]),
      choice(x.same ? 'And the numbers added, once the parentheses are gone?' : 'And the numbers added?', [ch(x.same ? 'The same: it is one line' : 'Different: the lines are parallel', 1), ch(x.same ? 'Different: the lines are parallel' : 'The same: it is one line', 0, x.same ? 'Distribute: they come out the same.' : n(x.l1.b) + ' and ' + n(x.l2.b) + ' are different.')]),
      choice('So how many solutions?', x.opts.map((o, i) => ch(o, i === x.correct, i === x.correct ? '' : MC.countPar.why(x, i))), null, { keep: true })]
  }
};
function mcFeedback(x, k) {
  if (k === x.correct) return { v: 'right', what: [] };
  const m = MC[x.fam]; return { v: 'wrong', what: [m.why(x, k)], rule: m.rule(x) };
}
/* Q8 — select all the systems that have the pair as a solution */
const SELWHY = (x, i) => { const [l1, l2] = x.systems[i], P = pairT(Q(x.pa), Q(x.pb)), X0 = Q(x.pa);
  const at = l => lineT(l) + ': ' + (l.m.n ? substT(E.lineSide(l), X0) + ' = ' : '') + n(yAt(l, x.pa)) + (onLine(l, x.pa, x.pb) ? ', true' : ', not ' + n(Q(x.pb)));
  const t = [onLine(l1, x.pa, x.pb), onLine(l2, x.pa, x.pb)];
  return LET[i] + '. ' + at(l1) + '; ' + at(l2) + (t[0] && t[1] ? ' — both true: ' + P + ' is a solution of this system.' : ' — one equation true is not enough: ' + P + ' is not a solution of this system.'); };
function selectFeedback(x, ks, tries) {
  const picked = (ks || []).map(Number), right = x.correct, wrongPicks = picked.filter(i => right.indexOf(i) < 0), missed = right.filter(i => picked.indexOf(i) < 0);
  if (!wrongPicks.length && !missed.length) return { v: 'right', what: [] };
  const rule = 'A pair is a solution of a system when it makes BOTH equations true. Put the x into each equation of each system and see whether it gives the y.';
  if ((tries || 1) <= 1 && !wrongPicks.length) return { v: 'wrong', what: ['Every one you picked is a solution, but you missed ' + missed.length + ' that ' + (missed.length === 1 ? 'is' : 'are') + '. Test each pair in both equations.'], rule };
  return { v: 'wrong', what: wrongPicks.concat(tries > 1 ? missed : []).sort().map(i => SELWHY(x, i)).concat(missed.length && tries <= 1 ? ['One more choice is right too.'] : []), rule };
}
function mcSolution(x) {
  if (x.type === 'multi') return x.opts.map((o, i) => ({ say: SELWHY(x, i) })).concat([{ say: 'The answers are ' + x.correct.map(i => LET[i]).join(', ').replace(/, (?=[^,]*$)/, ' and ') + '.' }]);
  return MC[x.fam].sol(x);
}
function stepsMC(x) {
  if (x.type === 'multi') return x.systems.map((sy, i) => { const r = x.correct.indexOf(i) >= 0, L = LET[i];
    return choice('System ' + L + ', ' + x.opts[i] + ': does ' + M(pairH(Q(x.pa), Q(x.pb))) + ' make both of its equations true?', [ch('Yes — choice ' + L + ' is a solution', r, r ? '' : SELWHY(x, i)), ch('No — choice ' + L + ' is not a solution', !r, r ? SELWHY(x, i) : '')], null, { keep: true }); });
  return MC[x.fam].walk(x);
}

/* ------------------------------------------------------------------ the rest of the unit interface */
const isPairFam = f => !!PF[f];
function solution(p) { return (F[p.fam] || PF[p.fam]).sol(p); }
function walk(p) { return mixed((F[p.fam] || PF[p.fam]).walk(p), p.key); }
function KIT_shuffle(a, key) { const T = KIT.slot('a7u11', 1, 'walk|' + key); return T.shuffle(a); }      /* option order fixed per question */
const mixed = (st, key) => st && st.map((x, i) => x.type === 'choice' && !x.keep ? Object.assign({}, x, { opts: KIT_shuffle(x.opts, key + '|' + i) }) : x);
function walkMC(x) { return mixed(x.kind === 'mc' && x.fam === 'endings' ? MC.endings.walk(x) : stepsMC(x), x.key); }
function solMC(x) { return x.fam === 'endings' ? MC.endings.sol(x) : mcSolution(x); }
function judgeMC(x, k) { return x.fam === 'endings' ? mcFeedback(Object.assign({}, x, { fam: 'endings' }), k) : mcFeedback(x, k); }

/* ------------------------------------------------------------------ the clean rule: no modelled mistake, printed number or other
   part's answer may equal an answer, so a wrong method is never marked right; every choice is different */
function clean(it) {
  if (!it || it.bad) return false;
  if (it.type === 'mc') { if (new Set(it.opts).size !== it.opts.length) return false;
    if (it.fam === 'isSol') { const t = [it.l1, it.l2].map(L => onLine(L, it.px, it.py)), want = { sol: [1, 1], first: [1, 0], second: [0, 1], neither: [0, 0] }[it.scen];
      if (!want || t[0] !== !!want[0] || t[1] !== !!want[1] || it.ids[it.correct] !== E.ISSOL_RIGHT[it.scen]) return false; }
    return true; }
  if (it.type === 'multi') {
    if (it.correct.length < 2 || it.correct.length > 3) return false;
    return it.systems.every(([l1, l2], i) => { const t = [onLine(l1, it.pa, it.pb), onLine(l2, it.pa, it.pb)];
      return !qeq(l1.m, l2.m) && (it.correct.indexOf(i) >= 0 ? t[0] && t[1] : t[0] !== t[1]); });
  }
  const parts = E.partsOf(it);
  if (it.type === 'parts' && parts[0].kind === 'mc') { const keys = parts.map(p => eqT(p.eq)); if (new Set(keys).size !== keys.length) return false;
    return parts.every(p => ending(p.eq).kind === ['one', 'none', 'all'][p.correct] && steps(p.eq).length >= 2); }
  const printed = it.eq ? E.printedNums({ L: it.eq.L.filter(c => c.k !== 'b'), R: it.eq.R.filter(c => c.k !== 'b'), v: it.eq.v }) : [];
  for (const p of parts) {
    if (p.kind === 'num') {
      if (!p.ans || (p.eq && p.fam !== 'box' && p.fam !== 'plans' && !qeq(ending(p.eq).s || Q(9999), p.ans))) return false;
      if (printed.some(q => qeq(q, qabs(p.ans)))) return false;
      if (F[p.fam].models(p).some(m => qeq(m.v, p.ans))) return false;
      if (p.fam === 'tableGap' && it.fig.rows.some(r => r.some(v => v != null && qeq(Q(v), p.ans)))) return false;
    } else {
      const ms = PF[p.fam].models(p);
      if (p.fam === 'estimate') { if (ms.some(m => within(p, m.v[0], m.v[1]))) return false; if (!within(p, p.ans[0], p.ans[1])) return false; }
      else if (ms.some(m => qeq(m.v[0], p.ans[0]) && qeq(m.v[1], p.ans[1]))) return false;
    }
  }
  return true;
}
E.setClean(clean);

/* ------------------------------------------------------------------ the wrong answers of a typed part, for a paper that is all
   multiple choice (the kit's ui.js mcOf; Croix, 14 Nov 2026): each what one of the part's own mistakes gives, in its order, as
   the key shows it; never the answer, never inside an estimate's tolerance, never twice. A part left with fewer than three is
   filled with whole numbers near the answer (an ordered pair: one coordinate one away). */
function keyHtml(p) {
  if (p.kind === 'num') return M(keyOfPart(p));
  if (p.fam === 'storyMeet') return 'After ' + n(p.ans[0]) + ' weeks; ' + storyAmt(p, p.ans[1]) + ' ' + p.st.each;
  if (p.fam === 'estimate') return 'about ' + M(pairH(p.ans[0], p.ans[1]));
  return M(pairH(p.ans[0], p.ans[1]));
}
function choices(p) {
  const out = [], seen = [keyHtml(p)];
  const add = v => { const q = Object.assign({}, p, { ans: v }), h = keyHtml(q); if (seen.indexOf(h) >= 0) return;
    if (p.kind === 'num') { if (qeq(v, p.ans)) return; if (places(v) < 0) return; }
    else if (p.fam === 'estimate' ? within(p, v[0], v[1]) : qeq(v[0], p.ans[0]) && qeq(v[1], p.ans[1])) return;
    seen.push(h); out.push(h); };
  if (p.kind === 'num') {
    F[p.fam].models(p).forEach(m => { if (p.fam !== 'plans' || qnum(m.v) <= 24) add(m.v); });      /* a cost is not a count of months on paper */
    [1, -1, 2, -2, 3, -3].forEach(d => { if (out.length < 3) { const v = qadd(p.ans, Q(d)); if (p.fam !== 'plans' || qsign(v) > 0) add(v); } });
  } else {
    PF[p.fam].models(p).forEach(m => add(p.fam === 'estimate' ? [E.tenthOf(m.v[0]), E.tenthOf(m.v[1])] : m.v));
    [[1, 0], [0, 1], [-1, 0], [0, -1]].forEach(([a, b]) => { if (out.length < 3) add([qadd(p.ans[0], Q(a)), qadd(p.ans[1], Q(b))]); });
  }
  return out;
}

const api = { F, PF, MC, choices, keyHtml, feedback, numFeedback, pairFeedback, readBoxes, mcFeedback: judgeMC, selectFeedback, mcSolution: solMC, solution, clean, joinSays,
  steps, eqLines, eqWalk, tailModels, checkSay, SELWHY, arith, within, isPairFam, ENDW };
const walkApi = { steps: walk, stepsMC: walkMC, readNum: E.readNum };
/* the help's words and pictures (help.js, 15 Nov 2026): Hints 1–3, the walkthrough and the coach's lines, to the help standard */
const HELP = node ? require('./help.js') : root.Help;
if (HELP) HELP(api, walkApi);
if (node) module.exports = Object.assign({}, api, { Walk: walkApi }); else { root.Coach = api; root.Walk = walkApi; }
})(this);
