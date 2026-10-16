/* Checks the coach over many seeds. Writes coach_dump.json for verify_coach.py.
   A. every worked step equals the question (same value; for n-equations, true at the answer); the last is the answer
   B. every mistake model, typed back as a student would, gets exactly its own explanation, and is never marked right
   C. fuzz: thousands of near-miss answers per set never crash, and every sentence shown is checked for arithmetic
   D. multiple choice / select-all feedback */
'use strict';
const P = require('./engine.js'), C = require('./coach.js'), Vz = require('./visual.js'), Wk = require('./walk.js'), fs = require('fs');
const SEEDS = +(process.argv[2] || 3000);
const fails = []; const fail = (s, w, m) => { if (fails.length < 80) fails.push(s + ' ' + w + ': ' + m); else fails.length++; };
const { N, V, P: Pw, Mul, Fr, Neg, Par, Sci } = P;

function atomish(a) { return a.t === 'n' || a.t === 'v' || a.t === 'pow' || a.t === 'par'; }
function typed(a) {
  switch (a.t) {
    case 'n': return a.s;
    case 'v': return a.s;
    case 'pow': { const b = a.b.t === 'n' || a.b.t === 'v' ? typed(a.b) : '(' + typed(a.b.t === 'par' ? a.b.x : a.b) + ')';
      const e = a.e.t === 'n' ? a.e.s : a.e.t === 'neg' && a.e.x.t === 'n' ? '-' + a.e.x.s : '(' + typed(a.e) + ')'; return b + '^' + e; }
    case 'mul': return a.xs.map(x => x.t === 'neg' || x.t === 'frac' ? '(' + typed(x) + ')' : typed(x)).join(a.op === '' ? '' : a.op === '×' ? ' x ' : '*');
    case 'frac': { const n = atomish(a.n) ? typed(a.n) : '(' + typed(a.n) + ')'; const d = atomish(a.d) ? typed(a.d) : '(' + typed(a.d) + ')'; return n + '/' + d; }
    case 'neg': return '-' + (atomish(a.x) ? typed(a.x) : '(' + typed(a.x) + ')');
    case 'par': return '(' + typed(a.x) + ')';
  }
  throw new Error('typed ' + a.t);
}
const strip = h => String(h).replace(/<[^>]+>/g, '');

/* arithmetic claims in a sentence ("4 + 5 = 9", "3 × 4 = 12", "2 · 2 · 2 = 8", "10 ÷ 2 = 5") are recomputed */
const NUM = '\\(?−?[\\d.,]+\\)?';
function numQ(s) { s = s.replace(/−/g, '-').replace(/,/g, ''); const neg = /^\(?-/.test(s); const q = P.qdec(s.replace(/[()\-]/g, '')); return neg ? P.Q(-q.n, q.d) : q; }
let claims = 0;
function claimCheck(seed, w, html) {
  if (/(^|[\s(>=])-\d/.test(String(html).replace(/<[^>]*>/g, ' '))) fail(seed, w, 'hyphen used as a minus sign: ' + strip(html).slice(0, 100));
  /* every chain like "2 + (−5) = 2 − 5 = −3" or "3 · 3 · 3 = 27": each side is worked out exactly (× · ÷ before + −) and all sides must agree */
  const t = String(html).replace(/<sup>([^<]*)<\/sup>/g, '^$1').replace(/<[^>]+>/g, '');
  const NUMR = '\\(?−?\\d[\\d,]*(?:\\.\\d+)?\\)?';
  const EXPR = NUMR + '(?: [+−×÷·] ' + NUMR + ')*';
  const re = new RegExp('(?<![\\d.^,])' + EXPR + '(?: = ' + EXPR + ')+(?![\\d^]|\\.\\d)', 'g'); let m;
  while ((m = re.exec(t))) {
    const sides = m[0].split(' = ');
    if (sides.every(sd => !/ [+−×÷·] /.test(sd))) continue;           /* "x = y" with no arithmetic: nothing to check */
    claims++;
    const vals = sides.map(evalSide);
    if (vals.some(v => v === null)) continue;
    if (!vals.every(v => P.qeq(v, vals[0]))) fail(seed, w, 'false claim "' + m[0] + '" in: ' + t.slice(0, 160));
  }
}
function evalSide(sd) {
  const tok = sd.split(' ');
  const nums = [], ops = [];
  for (let i = 0; i < tok.length; i++) { if (i % 2 === 0) { try { nums.push(numQ(tok[i])); } catch (e) { return null; } } else ops.push(tok[i]); }
  const mul = (a, b) => P.Q(a.n * b.n, a.d * b.d), div = (a, b) => P.Q(a.n * b.d, a.d * b.n), add = (a, b) => P.Q(a.n * b.d + b.n * a.d, a.d * b.d);
  const terms = [nums[0]], tops = [];
  for (let i = 0; i < ops.length; i++) {
    if (ops[i] === '×' || ops[i] === '·') terms[terms.length - 1] = mul(terms[terms.length - 1], nums[i + 1]);
    else if (ops[i] === '÷') terms[terms.length - 1] = div(terms[terms.length - 1], nums[i + 1]);
    else { tops.push(ops[i]); terms.push(nums[i + 1]); }
  }
  let r = terms[0]; tops.forEach((o, i) => { r = o === '+' ? add(r, terms[i + 1]) : add(r, P.Q(-terms[i + 1].n, terms[i + 1].d)); });
  return r;
}
/* the checker must catch planted errors */
(function () { const before = fails.length; claimCheck(0, 'plant', '4 + 5 = 10'); claimCheck(0, 'plant', '2 + (−5) = 2 − 5 = −2'); claimCheck(0, 'plant', '3 · 3 · 3 = 26'); claimCheck(0, 'plant', '6.6 ÷ 3.3 = 3');
  claimCheck(0, 'ok', '2 + (−5) = 2 − 5 = −3'); claimCheck(0, 'ok', '(−4) · (−4) · (−4) = −64');
  const caught = fails.length - before; fails.length = before; if (caught !== 4) { console.log('CHECKER BROKEN: caught', caught, 'of 4 planted'); process.exit(2); } })();

/* ---- pictures: every count and value in a picture is re-derived here ---- */
const VQ = (n, d) => P.Q(BigInt(n), BigInt(d === undefined ? 1 : d));
function ansExp(p) { const m = C.mono(p.ans); if (!m) return null; const ks = Object.keys(m.x); if (ks.length === 1) return Number(m.x[ks[0]]);
  const sp = C.single(p.ans); if (sp) return Number(sp.e); return null; }
function checkVis(seed, w, p, s) {
  const x = p.prm, bad = m => fail(seed, w, 'picture: ' + m);
  if (s.kind === 'row') { if (s.groups[0] + s.groups[1] !== s.total) bad('row sum'); const e = ansExp(p); if (e !== null && e !== s.total) bad('row total ' + s.total + ' ≠ answer exponent ' + e); }
  if (s.kind === 'grid') { if (s.rows * s.cols !== s.total) bad('grid'); const e = ansExp(p); if (e !== null && e !== s.total) bad('grid total ≠ answer exponent'); }
  if (s.kind === 'cancel') {
    if (s.zero) { if (s.top !== s.bottom) bad('zero picture'); return; }
    if (s.solve) { if (s.top !== s.solve.k + s.solve.c || s.top - s.bottom !== s.solve.c || !P.qeq(P.evalA(p.ans, {}), VQ(s.top))) bad('solve picture'); if (!P.qeq(P.qpow(VQ(x.b), BigInt(s.solve.c)), VQ(s.solve.V))) bad('solve V'); return; }
    let want;
    if (p.fam === 'ratio') { want = x.p - x.q; if (!P.qeq(P.qdiv(P.qdec(x.A), P.qdec(x.B)), P.qdec(x.t))) bad('ratio numbers'); }
    else if (p.fam === 'monoQuot') { want = x.p - x.q; if (x.k / x.j !== x.t) bad('monoQuot numbers'); }
    else if (p.fam === 'powquot') want = x.e; else if (p.fam === 'mixedProd') want = x.m - x.n; else want = ansExp(p);
    if (s.top - s.bottom !== want) bad('cancel leaves ' + (s.top - s.bottom) + ', answer exponent ' + want);
    if (p.fam === 'powquot' && s.top !== s.fromPow[0] * s.fromPow[1]) bad('powquot top');
  }
  if (s.kind === 'ladder') {
    const b = s.base;
    const wantBase = { negToFrac: x.b, negVal: x.b, coefNeg: 10, negDen: -x.c, zeroMix: x.a, varNeg: { letter: x.v }, coefVarNeg: { letter: x.v }, fracNeg: { frac: x.d } }[p.fam];
    if (JSON.stringify(wantBase) !== JSON.stringify(b)) bad('ladder base ' + JSON.stringify(b) + ' ≠ ' + JSON.stringify(wantBase));
    const wantLow = { negToFrac: -x.n, negVal: -x.n, coefNeg: -x.m, negDen: -x.m, zeroMix: 0, varNeg: -x.n, coefVarNeg: -x.n, fracNeg: -x.n }[p.fam];
    if (s.low !== wantLow) bad('ladder does not reach the question exponent');
    if (b && b.letter) return;
    const bq = b && b.frac ? VQ(1, b.frac) : VQ(b);
    /* walk up from b^0 = 1 multiplying, down dividing: an independent derivation of every row */
    let up = VQ(1), dn = VQ(1);
    for (let j = 1; j <= (s.high != null ? s.high : 3); j++) up = P.qmul(up, bq);
    for (let j = 1; j <= -Math.min(s.low, -1); j++) dn = P.qdiv(dn, bq);
    if (!P.qeq(up, P.qpow(bq, BigInt(s.high != null ? s.high : 3))) || !P.qeq(dn, P.qpow(bq, BigInt(Math.min(s.low, -1))))) bad('ladder values');
    const h = Vz.html(s); const rows = (h.match(/<tr/g) || []).length; if (rows !== (s.high != null ? s.high : 3) - Math.min(s.low, -1) + 1) bad('ladder rows');
  }
  if (s.kind === 'signs') { if (s.c !== x.c || s.e !== x.e) bad('signs'); const neg = s.e % 2 === 1; if (neg !== (P.evalA(p.ans, {}).n < 0n)) bad('signs result'); }
  if (s.kind === 'copies') {
    const m = C.mono(p.ans);
    if (s.frac) { const v = P.evalA(p.ans, {}); if (!P.qeq(v, P.qdiv(P.qpow(VQ(s.parts[0].n), BigInt(s.copies)), P.qpow(VQ(s.parts[1].n), BigInt(s.copies))))) bad('fracpow copies'); }
    else { s.parts.forEach(pt => { if (pt.letter) { if ((m.x[pt.letter] || 0n) !== BigInt(pt.e * s.copies)) bad('copies exponent ' + pt.letter); } else if (!P.qeq(m.c, P.qpow(VQ(pt.n), BigInt(s.copies)))) bad('copies number'); }); }
  }
  if (s.kind === 'hop') {
    const val = pos => { const ds = s.cells; const intPart = ds.slice(0, pos) || '0', fr = ds.slice(pos); return P.qdec((intPart.replace(/^0+(?=\d)/, '') || '0') + (fr ? '.' + fr : '')); };
    if (!P.qeq(val(s.cpos), P.qdec(x.c))) bad('hop: digits at c position are not ' + x.c);
    if (!P.qeq(val(s.spos), P.qmul(P.qdec(x.c), P.qpow(VQ(10), BigInt(x.k))))) bad('hop: digits at standard position are not the number');
    if (Math.abs(s.spos - s.cpos) !== Math.abs(x.k)) bad('hop count');
    if ((s.spos > s.cpos) !== (x.k > 0)) bad('hop direction');
  }
}

/* the picture checker must catch planted errors */
(function () { const G = P.generate(1), before = fails.length; let planted = 0, caughtN = 0;   /* counted per plant (Apple review W-9) */
  G.sections.forEach(sec => sec.items.forEach(it => (it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : []).forEach(p => {
    const s = Vz.spec(p); if (!s) return; const t = JSON.parse(JSON.stringify(s));
    if (t.kind === 'row' || t.kind === 'grid') t.total += 1; else if (t.kind === 'cancel') t.top += 1; else if (t.kind === 'ladder') { if (t.base && t.base.letter) return; t.base = (typeof t.base === 'number' ? t.base + 1 : t.base); if (typeof s.base !== 'number') return; }
    else if (t.kind === 'signs') t.e += 1; else if (t.kind === 'copies') t.copies += 1; else if (t.kind === 'hop') t.cpos += 1; else return;
    planted++; const b0 = fails.length; checkVis(0, 'plant', p, t); if (fails.length === b0) console.log('PLANT NOT CAUGHT', p.fam, t.kind); else caughtN++;
  })));
  fails.length = before; console.log('picture checker caught', caughtN, 'of', planted, 'planted errors'); if (caughtN !== planted) { console.log('CHECKER BROKEN'); process.exit(2); } })();

/* ---- the walkthrough: one right option per tap, every typed number re-derived from its own question text, every "then" = the question ---- */
const supTxt = h => String(h).replace(/<sup>([^<]*)<\/sup>/g, '^$1').replace(/<[^>]+>/g, '');
function checkWalk(seed, w, st, ctx) {
  if (!st || !st.length) { fail(seed, w, 'no walkthrough'); return; }
  stat.walks = (stat.walks || 0) + 1;
  let lastThen = null;
  st.forEach((s, k) => {
    const wk = w + ' walk' + k;
    claimCheck(seed, wk, s.ask);
    if (s.type === 'choice') {
      if (s.opts.filter(o => o.ok).length !== 1) fail(seed, wk, 'choice has ' + s.opts.filter(o => o.ok).length + ' right options');
      if (new Set(s.opts.map(o => strip(o.label))).size !== s.opts.length) fail(seed, wk, 'two options read the same');
      s.opts.forEach(o => { if (!o.ok && !o.why) fail(seed, wk, 'wrong option without a reason'); claimCheck(seed, wk, o.why); claimCheck(seed, wk, o.label); });
    } else {
      if (!P.qeq(P.evalA(s.of, {}), s.ans)) fail(seed, wk, 'num answer ≠ its expression');
      claimCheck(seed, wk, s.hint);
      const t = supTxt(s.ask), mm = /[Ww]hat is (.+)\?$/.exec(t), sn = /n − (\d+) = (\d+)\. What is n\?$/.exec(t);
      if (sn) { if (!P.qeq(s.ans, P.Q(BigInt(+sn[1] + +sn[2])))) fail(seed, wk, 'n step'); stat.walkNums = (stat.walkNums || 0) + 1; }
      else if (mm) { let v = null; try { v = P.evalA(P.parse(mm[1].replace(/[×·]/g, '*').replace(/÷/g, '/').replace(/−/g, '-'), true), {}); } catch (e) { }
        if (!v || !P.qeq(v, s.ans)) fail(seed, wk, 'the question "' + t + '" does not have the answer ' + P.decStr(s.ans)); stat.walkNums = (stat.walkNums || 0) + 1; }
      else if (/to what power\?$/.test(t) && ctx.fam === 'solveN') { if (!P.qeq(P.qpow(P.Q(BigInt(ctx.prm.b)), s.ans.n), P.Q(BigInt(ctx.prm.V)))) fail(seed, wk, 'power of b'); }
      else if (/how many places/i.test(t)) { if (!P.qeq(s.ans, P.Q(BigInt(Math.abs(ctx.prm.k))))) fail(seed, wk, 'places'); }
      else fail(seed, wk, 'a typed step whose question is not checked: ' + t);
    }
    if (s.then) {
      if (ctx.fam === 'solveN') { const env = { n: P.evalA(ctx.ans, {}) }; let ok; try { ok = s.then.t === 'eq' && P.qeq(P.evalA(s.then.l, env), P.evalA(s.then.r, env)); } catch (e) { ok = false; } if (!ok) fail(seed, wk, 'equation false at the answer'); }
      else if (ctx.q) { let ok; try { ok = P.sameValue(s.then, ctx.q, P.vars(ctx.q)); } catch (e) { ok = false; } if (!ok) fail(seed, wk, 'then ' + P.plain(s.then) + ' ≠ question'); }
      lastThen = s.then;
    }
  });
  if (st.filter(x => x.pic).length > 1) fail(seed, w, 'more than one picture step');
  if (ctx.select) return;
  if (!lastThen) { fail(seed, w, 'walkthrough never reaches the answer'); return; }
  if (ctx.fam === 'solveN') { if (!P.qeq(P.evalA(lastThen.r, {}), P.evalA(ctx.ans, {})) || lastThen.l.t !== 'v') fail(seed, w, 'walk does not end at n = answer'); }
  else { let ok; try { ok = P.sameValue(lastThen, ctx.ans, P.vars(ctx.ans)); } catch (e) { ok = false; } if (!ok) fail(seed, w, 'walk ends at ' + P.plain(lastThen) + ', not the answer');
    if (ctx.part && ctx.part.kind !== 'times' && ctx.part.kind !== 'std') { const r = P.mark(ctx.part, C.typedOf(lastThen)); if (r.v !== 'right') fail(seed, w, 'walk ends at an unfinished answer: ' + C.typedOf(lastThen) + ' ' + r.v); } }
}



const dump = []; const stat = { models: 0, modelHits: 0, collide: 0, fuzz: 0, fuzzSaid: {}, steps: 0 };
const FUZZ = ['0', '1', '-1', '2', '10', 'x', '1/2', '-1/2'];
/* the walkthrough checker must catch planted errors */
(function () { const G = P.generate(2), before = fails.length; let planted = 0, caught = 0;
  G.sections.forEach(sec => sec.items.forEach(it => (it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : []).forEach(p => {
    const ctx = { fam: p.fam, prm: p.prm, q: p.q, ans: p.ans, part: p };
    for (const mut of ['ans', 'twoOk', 'then']) {
      const st = Wk.steps(p); const i = mut === 'ans' ? st.findIndex(x => x.type === 'num') : mut === 'twoOk' ? st.findIndex(x => x.type === 'choice' && x.opts.length > 1) : st.findIndex(x => x.then);
      if (i < 0) continue;
      if (mut === 'ans') st[i].ans = P.qadd(st[i].ans, P.Q(1n)); else if (mut === 'twoOk') st[i].opts.forEach(o => { o.ok = true; }); else st[i].then = P.N(999983);
      planted++; const b0 = fails.length; checkWalk(0, 'plant', st, ctx); if (fails.length > b0) caught++; else console.log('WALK PLANT NOT CAUGHT', p.fam, mut);
    }
  })));
  fails.length = before; console.log('walk checker caught', caught, 'of', planted, 'planted errors'); })();
for (let seed = 1; seed <= SEEDS; seed++) {
  const G = P.generate(seed); const D = { seed, sols: [] };
  G.sections.forEach((sec, si) => sec.items.forEach((it, ii) => {
    const w0 = 'S' + (si + 1) + 'I' + (ii + 1);
    const parts = it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : [];
    parts.forEach(p => {
      const w = w0 + p.label, L = P.vars(p.ans);
      /* A. the worked solution */
      const sol = C.solution(p);
      if (!sol || !sol.length) { fail(seed, w, 'no solution for ' + p.fam); return; }
      const exs = sol.filter(s => s.ex);
      if (!exs.length) fail(seed, w, 'solution has no expressions');
      sol.forEach((s, k) => {
        claimCheck(seed, w + ' step' + k, s.say); stat.steps++;
        try { P.html(s.ex || N(1)); } catch (e) { fail(seed, w, 'draw step ' + k + ' ' + e.message); }
        if (!s.ex) return;
        if (p.fam === 'solveN') {
          const env = { n: P.evalA(p.ans, {}) };
          if (!P.qeq(P.evalA(s.ex.l, env), P.evalA(s.ex.r, env))) fail(seed, w, 'equation step ' + k + ' false at the answer');
        } else {
          let ok; try { ok = P.sameValue(s.ex, p.q, L); } catch (e) { ok = false; }
          if (!ok) fail(seed, w, 'step ' + k + ' ' + P.plain(s.ex) + ' ≠ question ' + P.plain(p.q));
        }
      });
      const last = exs[exs.length - 1].ex;
      if (p.fam === 'solveN') { if (!P.qeq(P.evalA(last.r, {}), P.evalA(p.ans, {}))) fail(seed, w, 'last step is not n = answer'); }
      else { const r = P.mark(p, typed(last)); if (r.v !== 'right' && p.kind !== 'times') fail(seed, w, 'last step "' + typed(last) + '" is not marked right: ' + r.v); }
      D.sols.push({ w, fam: p.fam, q: P.plain(p.q), ans: P.plain(p.ans), eq: p.fam === 'solveN', steps: exs.map(s => p.fam === 'solveN' ? [P.plain(s.ex.l), P.plain(s.ex.r)] : P.plain(s.ex)) });
      { const vs = Vz.spec(p); if (vs) { stat.pics = (stat.pics || 0) + 1; try { checkVis(seed, w, p, vs); claimCheck(seed, w + ' picture', Vz.html(vs)); } catch (e) { fail(seed, w, 'picture crashed: ' + e.message); } } }
      try { checkWalk(seed, w, Wk.steps(p), { fam: p.fam, prm: p.prm, q: p.q, ans: p.ans, part: p }); } catch (e) { fail(seed, w, 'walk crashed: ' + e.message); }
      /* B. every mistake model */
      const ms = C.models(p);
      ms.forEach(md => {
        stat.models++;
        claimCheck(seed, w + ' model', md.if);
        const txt = typed(md.ex);
        const f = C.feedback(p, txt);
        if (f.v === 'right') { fail(seed, w, 'mistake "' + txt + '" marked RIGHT'); return; }
        if (f.v === 'form') return;                         /* the right value in another form: the form message wins (e.g. 1/b^-n read as unfinished) */
        const said = f.what.join(' ');
        if (said.indexOf(md.if) < 0) {
          if (md.test && !md.test({ a: P.parse(txt, ['sci', 'std', 'times'].includes(p.kind)) })) return;
          fail(seed, w, 'model "' + strip(md.if).slice(0, 60) + '" typed as "' + txt + '" got: ' + strip(said).slice(0, 120));
        } else stat.modelHits++;
        if (/\. Or, if /.test(said)) stat.collide++;
        if (f.step === null || f.step === undefined || !sol[f.step]) fail(seed, w, 'model step ' + f.step + ' does not point at a solution step');
      });
      /* C. fuzz */
      const near = [];
      const sp = C.single(p.ans), mo = C.mono(p.ans), sc = C.sciOf(p.ans);
      if (sp) for (const db of [-1, 0, 1]) for (const de of [-2, -1, 0, 1, 2]) near.push(typed(Pw(Number(sp.b.n) + db < 0 ? Par(Neg(N(-(Number(sp.b.n) + db)))) : N(Number(sp.b.n) + db), Number(sp.e) + de)));
      if (mo && L.length) { const ks = Object.keys(mo.x); for (const d of [-1, 1, 2]) { ks.forEach(k => { const x = Object.assign({}, mo.x); x[k] = x[k] + BigInt(d);
        const top = [], bot = []; Object.keys(x).forEach(l => { if (x[l] > 0n) top.push(Pw(V(l), Number(x[l]))); else if (x[l] < 0n) bot.push(Pw(V(l), -Number(x[l]))); });
        const c = mo.c; const tp = Mul('', N(String(c.n < 0n ? -c.n : c.n)), ...top); const e = bot.length ? Fr(tp, bot.length === 1 ? bot[0] : Mul('', ...bot)) : tp; near.push(typed(e)); }); } }
      if (sc) for (const dk of [-2, -1, 1, 2]) near.push(sc.cs + ' x 10^' + (Number(sc.k) + dk));
      try { const v = P.evalA(p.ans, {}); const s = P.decStr(v); near.push(s, '-' + s, s + '0', s.replace(/0(?=[^0]*$)/, '')); } catch (e) { }
      near.concat(FUZZ).forEach(txt => {
        let f; try { f = C.feedback(p, txt); } catch (e) { fail(seed, w, 'feedback crashed on "' + txt + '": ' + e.message); return; }
        stat.fuzz++; f.what.forEach(s => claimCheck(seed, w + ' fuzz "' + txt + '"', s));
        const key = p.fam + ':' + (f.what[0] || '').replace(/<[^>]+>/g, '').replace(/[\d.,−-]+/g, '#').slice(0, 40); stat.fuzzSaid[key] = (stat.fuzzSaid[key] || 0) + 1;
        if (f.v === 'wrong' && f.step !== null && f.step !== undefined && !sol[f.step]) fail(seed, w, 'fuzz step out of range');
      });
    });
    /* D. multiple choice */
    if (it.type === 'mc') {
      it.opts.forEach((o, k) => { const f = C.mcFeedback(it, k); if ((k === it.correct) !== (f.v === 'right')) fail(seed, w0, 'mc feedback key'); f.what.forEach(s => claimCheck(seed, w0, s)); });
      { const vs = Vz.spec({ fam: it.fam, prm: it.prm, ans: it.opts[it.correct] }); if (vs) { try { checkVis(seed, w0, { fam: it.fam, prm: it.prm, ans: it.opts[it.correct] }, vs); claimCheck(seed, w0 + ' picture', Vz.html(vs)); } catch (e) { fail(seed, w0, 'MC picture crashed: ' + e.message); } } }
      try { checkWalk(seed, w0, Wk.stepsMC(it), { fam: it.fam, prm: it.prm, q: it.q, ans: it.opts[it.correct] }); } catch (e) { fail(seed, w0, 'MC walk crashed: ' + e.message); }
      const sol = C.mcSolution(it); if (!sol) fail(seed, w0, 'no MC solution');
      else sol.forEach(s => { claimCheck(seed, w0, s.say); if (s.ex) { let ok; try { ok = P.sameValue(s.ex, it.q, P.vars(it.q)); } catch (e) { ok = false; } if (!ok) fail(seed, w0, 'MC step ≠ question'); } });
      if (sol) D.sols.push({ w: w0, fam: it.fam, q: P.plain(it.q), ans: P.plain(it.opts[it.correct]), eq: false, steps: sol.filter(s => s.ex).map(s => P.plain(s.ex)) });
    }
    if (it.type === 'multi') {
      const all = it.opts.map((o, k) => k);
      [[it.correct], [all], [it.correct.slice(1)], [all.filter(k => it.correct.indexOf(k) < 0)]].forEach(([pick]) => [1, 2].forEach(tr => {
        const f = C.selectFeedback(it, pick, tr); const ok = pick.length === it.correct.length && pick.every(k => it.correct.indexOf(k) >= 0);
        if ((f.v === 'right') !== ok) fail(seed, w0, 'select feedback'); }));
      try { const ws = Wk.stepsMC(it); checkWalk(seed, w0, ws, { select: true }); ws.forEach((s, k) => { const yes = s.opts.findIndex(o => o.ok) === 0; if (yes !== it.correct.includes(k)) fail(seed, w0, 'select walk: choice ' + k + ' yes/no is wrong'); }); } catch (e) { fail(seed, w0, 'select walk crashed: ' + e.message); }
      C.mcSolution(it).forEach((s, k) => { const v = P.evalA(it.opts[k], {}); const txt = strip(s.say);
        if ((it.correct.indexOf(k) >= 0) !== /✓/.test(txt)) fail(seed, w0, 'select solution marks'); });
    }
  }));
  if (seed <= 1500) dump.push(D);
}

/* ---- pinned: every defect from the 10 Oct coach review stays fixed ---- */
(function () {
  const parts = function* () { for (let sd = 1; sd < 4000; sd++) { const G = P.generate(sd); for (const sec of G.sections) for (const it of sec.items) { for (const p of (it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : [])) yield [p, it]; if (it.type === 'mc') yield [null, it]; } } };
  const find = (fam, pred) => { for (const [p] of parts()) if (p && p.fam === fam && (!pred || pred(p.prm))) return p; throw new Error('no ' + fam); };
  const PIN = (name, p, text, v, must, mustNot, step) => {
    const f = C.feedback(p, text), said = strip(f.what.join(' '));
    if (v && f.v !== v) fails.push('pin ' + name + ': "' + text + '" → ' + f.v + ' (wanted ' + v + ') ' + said.slice(0, 100));
    if (must && !must.test(said)) fails.push('pin ' + name + ': "' + text + '" missing ' + must + ' — said: ' + said.slice(0, 140));
    if (mustNot && mustNot.test(said)) fails.push('pin ' + name + ': "' + text + '" must not say ' + mustNot + ' — said: ' + said.slice(0, 140));
    if (step !== undefined && f.step !== step) fails.push('pin ' + name + ': step ' + f.step + ' (wanted ' + step + ')');
  };
  const pw = (b, e) => Math.pow(b, e);
  let n11 = 0; for (const [p, it] of parts()) { if (p || it.fam !== 'monoCoefPow' || it.prm.q !== 3) continue; const x = it.prm;
    const k = it.opts.findIndex(o => P.plain(o).startsWith('(' + x.c * x.q + ')*((' + x.v + ')**(' + x.p * x.q + '))')); const f = C.mcFeedback(it, k);
    if (!/·.*·/.test(strip(f.what.join(' '))) || /times itself/.test(f.what.join(' '))) fails.push('pin Q11: ' + strip(f.what.join(' '))); if (++n11 > 30) break; }
  let x, q;
  q = find('monoNegPow'); x = q.prm; PIN('double flip', q, pw(x.k, x.q) + x.w + '^' + x.q + '/' + x.v + '^-' + x.p * x.q, 'wrong', /bottom of your fraction/, /lose the minus/);
  q = find('negToFrac'); x = q.prm; PIN('neg-neg', q, '-' + x.b + '^-' + x.n, 'wrong', /still has a negative exponent/, /one over the power but also/);
  q = find('varNeg'); x = q.prm; PIN('neg-neg var', q, '-' + x.v + '^-' + x.n, 'wrong', /still has a negative exponent/, /one over the power but also/);
  q = find('prod'); x = q.prm; PIN('8^16', q, x.b + '^' + 2 * (x.m + x.n), 'wrong', null, /multiply the bases/);
  q = find('monoQuot'); x = q.prm; PIN('no caret', q, x.t + x.v + (x.p - x.q), 'unread', /\^ is missing/);
  /* p = 1 in (p/q)^k no longer occurs: raising only the bottom gives the right answer there, so the clean rule (15 Oct)
     draws other numbers. The pin stays as a check that it never comes back. */
  { let found = null; try { found = find('fracpow', y => y.p === 1); } catch (e) { found = null; } if (found) fails.push('clean rule: (1/q)^k is back in a set'); }
  q = find('mixedProd'); x = q.prm; PIN('right size', q, String(pw(x.B, x.n - x.m)), 'wrong', /one over/, /right size/);
  q = find('monoCoefPow'); x = q.prm; PIN('mono sign', q, '-' + pw(x.c, x.q) + x.v + '^' + x.p * x.q, 'wrong', /wrong sign/);
  q = find('toSci', y => y.k > 0); x = q.prm; PIN('sci plain', q, P.decStr(P.qdec(x.c)).replace('.', '') + '0'.repeat(x.k + 1), 'wrong', /needs to be in scientific notation/, /zeros|one place/);
  q = find('negNegBase'); x = q.prm; PIN('-1/-8', q, '-1/-' + pw(x.c, x.e), 'wrong', /both negative/, /lose the sign/);
  q = find('monoPow'); x = q.prm; PIN('stacked', q, x.v + '^' + x.m + '^' + x.n, 'unread', /Two \^/);
  q = find('coefNeg'); x = q.prm; PIN('x as times', q, x.k + ' x 10^-' + x.m, 'form', null, /letter/); PIN('coef struct step', q, x.k + '/10^-' + x.m, 'wrong', /keep its exponent negative/, null, 0);
  PIN('coef base', q, x.k + '^-' + x.m, 'wrong', /still has a negative exponent|Only the 10/);
  q = find('zeroMix'); x = q.prm; PIN('sign no neg', q, '-' + x.c * x.c, 'wrong', /Nothing in this question is negative/);
  q = find('fracNeg'); x = q.prm; PIN('over 1', q, pw(x.d, x.n) + '/1', 'form', /over 1/, /lowest/);
  q = find('prod'); x = q.prm; PIN('needs parens', q, x.b + '^' + x.m + '+' + x.n, 'wrong', /parentheses/);
  PIN('just the exponent', q, String(x.m + x.n), 'form', /That is the exponent/);
  q = find('solveN'); x = q.prm; PIN('b^n', q, x.b + '^' + (x.k + x.c), 'form', /just the exponent/); PIN('setup', q, 'n-' + x.k + '=' + x.c, 'unread', /Good setup/);
  q = find('toStd', y => y.k < 0 && P.qmul(P.qdec(y.c), P.qpow(P.Q(10), BigInt(-y.k))).d === 1n); x = q.prm;
  const flip = P.qmul(P.qdec(x.c), P.qpow(P.Q(10), BigInt(-x.k))).n, want = P.decStr(P.qmul(P.qdec(x.c), P.qpow(P.Q(10), BigInt(x.k))));
  PIN('1/N', q, '1/' + flip, 'wrong', /one over/); PIN('neg small', q, '-' + want, 'wrong', /small/);
  q = find('toSci'); x = q.prm; PIN('E', q, x.c + 'E' + x.k, 'unread', /calculator/); PIN('10k', q, x.c + ' x 10' + Math.abs(x.k), 'unread', /Put \^/);
  q = find('monoProd'); x = q.prm; PIN('11k', q, (x.m + x.n) + x.v, 'wrong', /Did you mean/);
})();

/* (review 3's pins tested "Help me solve this", which Croix took out on 11 Oct; its code was deleted on 15 Oct.) */

/* ---- pinned: review 4 (walkthrough) ---- */
(function () {
  const find = (fam, pred) => { for (let sd = 1; sd < 4000; sd++) { const G = P.generate(sd); for (const sec of G.sections) for (const it of sec.items) for (const p of (it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : [])) if (p.fam === fam && (!pred || pred(p.prm))) return p; } return null; };
  const labels = st => st.map(x => x.opts ? x.opts.map(o => strip(o.label)).join('|') : '').join(' / ');
  let q = find('negDen', y => y.m % 2 === 1); if (q && /A negative number/.test(labels(Wk.steps(q)))) fails.push('walk pin: negDen offers "A negative number" when the answer is negative');
  q = find('powquot', y => y.p === 2 && y.q === 2); if (q && /Add them/.test(labels(Wk.steps(q)).split(' / ')[0])) fails.push('walk pin: powquot 2,2 offers Add (same result)');
  q = find('fracpow', y => y.p === 1); if (q && /Only the bottom/.test(labels(Wk.steps(q)))) fails.push('walk pin: fracpow p=1 offers Only the bottom');
  q = find('quot', y => y.m % y.n === 0 && y.m / y.n === y.m - y.n); if (q && /Divide them/.test(labels(Wk.steps(q)))) fails.push('walk pin: quot offers Divide when it gives the same number');
  for (const [t, ok] of [['4^2', false], ['9-5', false], ['6x3', false], ['17', true], ['n = 6', true], ['(−3)', true], ['1/16', true], ['-2', true]]) if ((Wk.readNum(t) !== null) !== ok) fails.push('walk pin: readNum("' + t + '")');
  q = find('toStd', y => y.k < 0); const st = Wk.steps(q).find(x => x.places); if (!st) fails.push('walk pin: places step not marked');
})();

fs.writeFileSync(__dirname + '/coach_dump.json', JSON.stringify(dump));
console.log('seeds', SEEDS, '| solution steps', stat.steps, '| models', stat.models, 'explained by their own words', stat.modelHits, '| two explanations shown together', stat.collide, '| fuzz answers', stat.fuzz, '| arithmetic claims', claims, '| pictures', stat.pics, '| walkthroughs', stat.walks, '(typed steps re-derived:', stat.walkNums + ')');
const top = Object.entries(stat.fuzzSaid).sort((a, b) => b[1] - a[1]);
console.log('distinct fuzz messages', top.length);
console.log(fails.length ? fails.length + ' FAILURES\n' + fails.slice(0, 80).join('\n') : 'all coach checks pass');
process.exit(fails.length ? 1 : 0);
