/* Checks the practice engine over many seeds. Writes dump.json for the independent check in verify.py. */
'use strict';
const P = require('./engine.js'); require('./coach.js');   /* generate() needs the coach's clean rule */
const fs = require('fs');
const SEEDS = +(process.argv[2] || 20000);
const fails = [];
const fail = (seed, where, what) => { if (fails.length < 60) fails.push(seed + ' ' + where + ': ' + what); else fails.length++; };

function atomish(a) { return a.t === 'n' || a.t === 'v' || a.t === 'pow' || a.t === 'par'; }
function typed(a, o) {                      // how a student would type it
  o = o || {};
  switch (a.t) {
    case 'n': return o.commas ? P.commas(a.s) : a.s;
    case 'v': return a.s;
    case 'pow': { const b = a.b.t === 'n' || a.b.t === 'v' ? typed(a.b) : '(' + typed(a.b.t === 'par' ? a.b.x : a.b) + ')';
      const e = a.e.t === 'n' ? a.e.s : a.e.t === 'neg' && a.e.x.t === 'n' ? '-' + a.e.x.s : '(' + typed(a.e) + ')';
      return b + '^' + e; }
    case 'mul': return a.xs.map(x => x.t === 'neg' || x.t === 'frac' ? '(' + typed(x) + ')' : typed(x)).join(a.op === '' ? '' : a.op === '×' ? ' x ' : '*');
    case 'frac': { const n = atomish(a.n) || (a.n.t === 'mul' && a.n.op === '') ? typed(a.n) : '(' + typed(a.n) + ')';
      const d = atomish(a.d) ? typed(a.d) : '(' + typed(a.d) + ')'; return n + '/' + d; }
    case 'neg': return '-' + (atomish(a.x) || a.x.t === 'frac' ? typed(a.x) : '(' + typed(a.x) + ')');
    case 'par': return '(' + typed(a.x) + ')';
    case 'eq': return typed(a.l) + '=' + typed(a.r);
  }
  throw new Error('typed ' + a.t);
}
const val = a => P.evalA(a, {});
const ENV = {}; 'abcdghkmnprstwxyz'.split('').forEach((l, i) => { ENV[l] = P.Q(13 * (i + 2) + 1, 13); });
const valE = a => qs(P.evalA(a, ENV));
const qs = q => q.n + '/' + q.d;

/* the real test's own questions, built with the same constructors: no practice question may be one of them */
const { N, V, P: Pw, Mul, Fr, Neg, Par, Eq, Sci } = P;
const TEST = [
  Mul('·', Pw(4, 3), Pw(4, 5)), Pw(Par(Pw(2, 3)), 4), Fr(Pw(7, 9), Pw(7, 4)), Pw(9, 0),
  Pw(Par(Fr(2, 3)), 3), Mul('·', Pw(6, 0), Pw(5, 2)), Fr(Pw(Par(Pw(10, 2)), 2), Pw(10, 3)),
  Mul('·', Pw(2, 4), Pw(2, 3)), Eq(Fr(Pw(5, V('n')), Pw(5, 2)), N(125)),
  Pw(6, -3), Fr(1, Pw(Neg(2), -5)), Mul('·', N(3), Pw(10, -4)),
  Pw(4, -2), Pw(Par(Neg(3)), -3), Pw(Par(Fr(1, 2)), -3), Mul('·', Pw(2, 5), Pw(2, -7)), Pw(5, -2),
  Mul('·', Pw(V('x'), 4), Pw(V('x'), 6)), Pw(Par(Pw(V('y'), 3)), 5), Pw(Par(Mul('', N(3), Pw(V('a'), 2))), 3), Fr(Mul('', N(15), Pw(V('m'), 7)), Mul('', N(5), Pw(V('m'), 2))),
  Pw(V('b'), -4), Mul('', N(5), Pw(V('x'), -2)), Pw(Par(Mul('', N(2), Pw(V('m'), -3), V('n'))), 2), Pw(Par(Mul('', N(4), Pw(V('x'), 3))), 2),
  N('8300000'), N('0.00047'), N('60500000000'), N('0.0000000092'), Sci('2.9', 5), Sci('7.1', -6), N('0.0036'),
  Fr(Sci('9', 9), Sci('3', 6)), Fr(Sci('4.8', -3), Sci('1.6', -7)), Sci('5.6', 8)].map(t => P.plain(canonT(t)));
const TESTSET = new Set(TEST);
/* canonical form, written here independently of engine.canon: the factors of a product in sorted order (2³·2⁴ = 2⁴·2³) */
function canonT(a) {
  if (!a || typeof a !== 'object') return a;
  const c = {}; for (const k of Object.keys(a)) c[k] = Array.isArray(a[k]) ? a[k].map(canonT) : (a[k] && typeof a[k] === 'object' ? canonT(a[k]) : a[k]);
  if (c.t === 'mul') c.xs = c.xs.slice().sort((x, y) => { const px = P.plain(x), py = P.plain(y); return px < py ? -1 : px > py ? 1 : 0; });
  return c;
}

const dump = [];
const counts = {};
for (let seed = 1; seed <= SEEDS; seed++) {
  let G;
  try { G = P.generate(seed); } catch (e) { fail(seed, 'generate', e.message); continue; }
  const pts = G.sections.map(s => s.items.reduce((t, it) => t + (it.type === 'parts' ? it.parts.length : 1), 0));
  if (pts.join() !== '9,9,8,10') fail(seed, 'points', pts.join());
  const out = { seed, items: [] };
  G.sections.forEach((sec, si) => sec.items.forEach((it, ii) => {
    const where = 'S' + (si + 1) + 'I' + (ii + 1);
    try { P.html(Mul('', N(1))); } catch (e) {}
    if (it.type === 'parts' || it.type === 'solo') {
      const parts = it.type === 'parts' ? it.parts : [it.part];
      parts.forEach(p => {
        const w = where + p.label;
        try { P.html(p.q); P.html(p.ans); (p.miss || []).forEach(m => P.html(m.ans)); } catch (e) { fail(seed, w, 'draw ' + e.message); }
        if (TESTSET.has(P.plain(canonT(p.q)))) fail(seed, w, 'same as the test: ' + P.plain(p.q));
        const forms = [typed(p.ans)];
        if (p.kind === 'std') forms.push(typed(p.ans, { commas: true }));
        if (p.kind === 'times') { forms.push(P.decStr(val(p.ans))); forms.push(P.commas(P.decStr(val(p.ans)))); }
        if (p.kind === 'n') forms.push('n=' + typed(p.ans), 'n = ' + typed(p.ans));
        forms.forEach(f => { const m = P.mark(p, f); counts[m.v] = (counts[m.v] || 0) + 1; if (m.v !== 'right') fail(seed, w, 'key typed as "' + f + '" marked ' + m.v + ' ' + (m.msg || '')); });
        (p.miss || []).forEach(mm => {
          let same; try { same = p.kind === 'mono' ? P.mark(p, typed(mm.ans)).v === 'right' : P.qeq(val(mm.ans), val(p.ans)); } catch (e) { same = false; }
          const m = P.mark(p, typed(mm.ans));
          if (m.v === 'right') fail(seed, w, 'mistake "' + typed(mm.ans) + '" marked right');
          else if (!same && m.v === 'wrong' && m.msg !== mm.msg) {
            counts.shadow = (counts.shadow || 0) + 1;      // an earlier mistake has the same value: its message shows instead
          }
        });
        if (p.kind === 'sci') { const c = val(p.ans.xs[0]); if (P.qeq(c, P.Q(10)) || !(c.n >= c.d && c.n < 10n * c.d)) fail(seed, w, 'coefficient ' + qs(c)); }
        out.items.push({ w, kind: p.kind, q: P.plain(p.q), ans: P.plain(p.ans), qtext: p.q.t === 'n' ? p.q.s : null, ansText: p.ans.t === 'n' ? p.ans.s : null,
          miss: (p.miss || []).map(m => P.plain(m.ans)), tail: p.tail || null, stem: it.type === 'solo' ? it.stem : null, base: p.base || null });
      });
    } else if (it.type === 'mc') {
      if (TESTSET.has(P.plain(canonT(it.q)))) fail(seed, where, 'same as the test');
      const vs = it.opts.map(valE);
      if (it.why.filter(x => x === null).length !== 1 || it.why[it.correct] !== null) fail(seed, where, 'key');
      if (new Set(it.opts.map(P.plain)).size !== it.opts.length) fail(seed, where, 'two choices are written the same');
      if (!it.sci && new Set(vs).size !== vs.length) fail(seed, where, 'two choices have the same value ' + vs);
      try { P.html(it.q); it.opts.forEach(P.html); } catch (e) { fail(seed, where, 'draw ' + e.message); }
      out.items.push({ w: where, kind: it.sci ? 'mcsci' : 'mc', q: P.plain(it.q), opts: it.opts.map(P.plain), correct: it.correct });
    } else if (it.type === 'multi') {
      if (!it.correct.length || it.correct.length === it.opts.length) fail(seed, where, 'select-all needs some right and some wrong');
      if (new Set(it.opts.map(P.plain)).size !== it.opts.length) fail(seed, where, 'two choices are written the same');
      it.steps.forEach((s, i) => { if (!P.qeq(val(s.e), val(s.v)) || s.ok !== it.correct.includes(i)) fail(seed, where, 'steps'); });
      out.items.push({ w: where, kind: 'multi', target: P.plain(it.target), opts: it.opts.map(P.plain), correct: it.correct, stepVals: it.steps.map(s => P.plain(s.v)) });
    }
  }));
  if (seed <= 4000) dump.push(out);
}

/* the reader on hand-typed answers */
const baseOf = a => { const pw = a.t === 'frac' ? a.d : a; const b = pw.b.t === 'par' ? pw.b.x : pw.b; return b.t === 'neg' ? -Number(b.x.s) : Number(b.s); };
const R = (kind, ans, text, want, extra) => { const p = Object.assign({ kind, ans: typeof ans === 'string' ? P.parse(ans) : ans, miss: [] }, kind === 'posexp' ? { base: baseOf(ans) } : {}, extra || {}); const m = P.mark(p, text); if (m.v !== want) fails.push('reader: [' + kind + '] "' + text + '" → ' + m.v + ' (wanted ' + want + ') ' + (m.msg || '')); };
R('power', Pw(4, 8), '4^8', 'right', { base: 4 }); R('power', Pw(4, 8), '4⁸', 'right', { base: 4 }); R('power', Pw(4, 8), '65536', 'form', { base: 4 }); R('power', Pw(4, 8), '2^16', 'form', { base: 4 });
R('power', Pw(4, 8), '4^15', 'wrong', { base: 4 }); R('power', Pw(4, 8), '4**8', 'right', { base: 4 }); R('power', Pw(4, 8), '4^(8)', 'right', { base: 4 });
R('value', Fr(1, 16), '1/16', 'right'); R('value', Fr(1, 16), '0.0625', 'right'); R('value', Fr(1, 16), '2/32', 'form'); R('value', Fr(1, 16), '4^-2', 'form'); R('value', Fr(1, 16), '1/4^2', 'form');
R('value', Fr(1, 16), '-1/16', 'wrong'); R('value', Neg(Fr(1, 27)), '-1/27', 'right'); R('value', Neg(Fr(1, 27)), '−1/27', 'right'); R('value', Neg(Fr(1, 27)), '1/-27', 'right'); R('value', Neg(Fr(1, 27)), '-(1/27)', 'right');
R('value', N(8), '8', 'right'); R('value', N(8), '8/1', 'form'); R('value', N(8), '2*4', 'form'); R('value', N(1), '1', 'right'); R('value', N(1), '0', 'wrong'); R('value', N(1), 'x', 'unread'); R('value', N(1), 'y', 'wrong');
R('value', Fr(1, 4), '2^-2 = 1/4', 'right'); R('value', Fr(1, 4), '.25', 'right');
R('posexp', Fr(1, Pw(6, 3)), '1/6^3', 'right'); R('posexp', Fr(1, Pw(6, 3)), '1/(6^3)', 'right'); R('posexp', Fr(1, Pw(6, 3)), '1/216', 'form'); R('posexp', Fr(1, Pw(6, 3)), '6^-3', 'form'); R('posexp', Fr(1, Pw(6, 3)), '-6^3', 'wrong');
R('posexp', Pw(Par(Neg(2)), 5), '(-2)^5', 'right'); R('posexp', Pw(Par(Neg(2)), 5), '-2^5', 'form'); R('posexp', Pw(Par(Neg(2)), 4), '-2^4', 'wrong'); R('posexp', Pw(Par(Neg(2)), 4), '(-2)^4', 'right');
R('posexp', Fr(3, Pw(10, 4)), '3/10^4', 'right'); R('posexp', Fr(3, Pw(10, 4)), '0.0003', 'form');
R('n', N(5), '5', 'right'); R('n', N(5), 'n=5', 'right'); R('n', N(5), '2+3', 'form'); R('n', N(5), '3', 'wrong');
R('mono', Pw(V('x'), 10), 'x^10', 'right'); R('mono', Pw(V('x'), 10), 'X^10', 'right'); R('mono', Pw(V('x'), 10), 'x^4*x^6', 'form'); R('mono', Pw(V('x'), 10), 'x^24', 'wrong'); R('mono', Pw(V('x'), 10), 'y^10', 'wrong');
R('mono', Mul('', N(27), Pw(V('a'), 6)), '27a^6', 'right'); R('mono', Mul('', N(27), Pw(V('a'), 6)), '27*a^6', 'right'); R('mono', Mul('', N(27), Pw(V('a'), 6)), '(3a^2)^3', 'form'); R('mono', Mul('', N(27), Pw(V('a'), 6)), '3^3a^6', 'form');
R('mono', Mul('', N(27), Pw(V('a'), 6)), '9a^6', 'wrong'); R('mono', Mul('', N(27), Pw(V('a'), 6)), 'a^6*27', 'right');
R('mono', Fr(1, Pw(V('b'), 4)), '1/b^4', 'right', { posOnly: true }); R('mono', Fr(1, Pw(V('b'), 4)), 'b^-4', 'form', { posOnly: true }); R('mono', Fr(1, Pw(V('b'), 4)), '-b^4', 'wrong', { posOnly: true });
R('mono', Fr(Mul('', N(4), Pw(V('n'), 2)), Pw(V('m'), 6)), '4n^2/m^6', 'right', { posOnly: true }); R('mono', Fr(Mul('', N(4), Pw(V('n'), 2)), Pw(V('m'), 6)), '(4n^2)/(m^6)', 'right', { posOnly: true });
R('mono', Fr(Mul('', N(4), Pw(V('n'), 2)), Pw(V('m'), 6)), '4m^-6n^2', 'form', { posOnly: true }); R('mono', Fr(Mul('', N(4), Pw(V('n'), 2)), Pw(V('m'), 6)), '2n^2/m^6', 'wrong', { posOnly: true });
R('mono', Mul('', N(3), Pw(V('m'), 5)), '15m^5/5', 'form'); R('mono', Pw(V('x'), 10), 'x^10/1', 'form'); R('mono', Fr(1, Pw(V('b'), 4)), '1/(b^4)', 'right', { posOnly: true }); R('mono', Fr(5, Pw(V('x'), 2)), '5x^-2', 'form', { posOnly: true }); R('mono', Fr(5, Pw(V('x'), 2)), '1/5x^2', 'unread', { posOnly: true }); R('mono', Mul('', N(3), Pw(V('m'), 5)), 'm^5*3', 'right');
R('sci', Sci('8.3', 6), '8.3 x 10^6', 'right'); R('sci', Sci('8.3', 6), '8.3×10⁶', 'right'); R('sci', Sci('8.3', 6), '8.3*10^6', 'right'); R('sci', Sci('8.3', 6), '83 x 10^5', 'form'); R('sci', Sci('8.3', 6), '8300000', 'form');
R('sci', Sci('8.3', 6), '8.3 x 10^5', 'wrong'); R('sci', Sci('4.7', -4), '4.7 x 10^-4', 'right'); R('sci', Sci('4.7', -4), '4.7x10^(-4)', 'right'); R('sci', Sci('4.7', -4), '4.7 x 10^4', 'wrong'); R('sci', Sci('4.7', -4), '0.47 x 10^-3', 'form');
R('std', N('290000'), '290,000', 'right'); R('std', N('290000'), '290 000', 'right'); R('std', N('290000'), '290000', 'right'); R('std', N('290000'), '2.9 x 10^5', 'form'); R('std', N('290000'), '29000', 'wrong');
R('std', N('0.0000071'), '.0000071', 'right'); R('std', N('0.0000071'), '0.0000071', 'right'); R('std', N('0.0000071'), '0.000071', 'wrong');
R('times', Sci('3', 3), '3000', 'right'); R('times', Sci('3', 3), '3 x 10^3', 'right'); R('times', Sci('3', 3), '3,000 times', 'right'); R('times', Sci('3', 3), '3', 'wrong');
R('value', Fr(1, 16), '', 'blank'); R('value', Fr(1, 16), '1//16', 'unread'); R('value', Fr(1, 16), '1/0', 'unread');

/* the review's findings, each pinned */
const X10 = Pw(V('x'), 10), F4 = Fr(Mul('', N(4), Pw(V('n'), 2)), Pw(V('m'), 6)), F16 = Fr(1, Pw(6, 3));
R('value', N(1), '0^0', 'unread'); R('mono', X10, '0^0x^10', 'unread');
R('posexp', Pw(Par(Neg(4)), 4), '4^4', 'form'); R('posexp', Pw(Par(Neg(3)), 4), '9^2', 'form'); R('posexp', Pw(Par(Neg(3)), 4), '81^1', 'form'); R('posexp', Pw(Par(Neg(3)), 4), '(-3)^4', 'right');
R('power', Pw(4, 8), '4^15 = 4^8', 'wrong', { base: 4 }); R('value', Fr(1, 4), '1/2 = 1/4', 'wrong'); R('power', Pw(4, 8), '4^3*4^5 = 4^8', 'right', { base: 4 }); R('n', N(5), '5 = n', 'right');
R('posexp', Fr(1, Pw(8, 2)), '1/64^1', 'form'); R('posexp', Fr(1, Pw(8, 2)), '8^0/64', 'form'); R('posexp', Fr(1, Pw(8, 2)), '1/(8^1*8)', 'form'); R('posexp', Fr(1, Pw(8, 2)), '1/8^(2+0)', 'form'); R('posexp', Fr(1, Pw(8, 2)), '1/4^3', 'form');
R('posexp', F16, '1/(6^4/6)', 'form'); R('posexp', F16, '1/(2^3*3^3)', 'form'); R('posexp', F16, '-1/(-6)^3', 'form'); R('posexp', F16, '1/6^-(-3)', 'form'); R('posexp', F16, '2/6^3 - 1/6^3', 'form'); R('posexp', F16, '1/6^3+0', 'form');
R('posexp', Fr(3, Pw(10, 4)), '0.0003*10^0', 'form'); R('posexp', Fr(3, Pw(10, 4)), '0.3/10^3', 'form'); R('posexp', Fr(3, Pw(10, 4)), '3/10^4', 'right'); R('posexp', Fr(3, Pw(10, 4)), '30/10^5', 'form');
R('sci', Sci('8.3', 6), '8.3 x 10^(3+3)', 'form'); R('sci', Sci('8.3', 6), '8.3 x 10^(12/2)', 'form'); R('sci', Sci('4.7', -4), '4.7 x 10^(-2*2)', 'form'); R('sci', Sci('8.3', 6), '10^6 x 8.3', 'right');
R('mono', X10, '1/x^-10', 'form'); R('mono', F4, 'n^2/(m^6/4)', 'form', { posOnly: true }); R('mono', F4, '4/(m^6/n^2)', 'form', { posOnly: true });
R('mono', F4, '4/m^6n^2', 'unread', { posOnly: true }); R('mono', F4, '(4n^2)/m^6', 'right', { posOnly: true });
R('posexp', Fr(3, Pw(10, 4)), '1/8*10^6', 'unread');
R('times', Sci('3', 3), '3000 times larger', 'right'); R('times', Sci('3', 3), '3000x', 'right'); R('value', Fr(8, 27), '8÷27', 'right'); R('value', Fr(35, 27), '1 8/27', 'unread'); R('std', N('0.0000071'), '0.000 0071', 'right');
R('value', Fr(8, 27), '-'.repeat(6000) + '8/27', 'unread');
R('mono', X10, '1*x^10', 'form'); R('mono', X10, 'x^10*1', 'form'); R('mono', X10, '1x^10', 'form'); R('mono', X10, 'x^0*x^10', 'form'); R('mono', Fr(1, Pw(V('b'), 4)), '1/b^4', 'right', { posOnly: true });
R('times', Sci('3', 3), '2999+1', 'form'); R('times', Sci('3', 3), '6000/2', 'form'); R('times', Sci('3', 3), '30 x 10^2', 'form');

fs.writeFileSync(__dirname + '/dump.json', JSON.stringify(dump));
console.log('seeds', SEEDS, 'marks', JSON.stringify(counts));
/* planted errors (Apple review W-9): the checks above must catch each of these */
{ const C = require('./coach.js'); let planted = 0, caught = 0;
  const plant = (name, isCaught) => { planted++; if (isCaught) caught++; else fails.push('PLANT NOT CAUGHT: ' + name); };
  plant('a reordered test question', TESTSET.has(P.plain(canonT(Mul('·', Pw(2, 3), Pw(2, 4))))));
  plant('a test question with its factors swapped, in the engine', P.onTest(Mul('·', Pw(4, 5), Pw(4, 3))));
  const pq = P.generate(1).sections[0].items[1].parts[2]; const bad = Object.assign({}, pq, { prm: { B: 2, p: 2, q: 2, e: 1, r: 3 }, q: Fr(Pw(Par(Pw(2, 2)), 2), Pw(2, 3)), ans: N(2) });
  plant('a mistake that gives the answer ((2²)² ÷ 2³)', !C.clean({ type: 'solo', part: bad }));
  const key = P.generate(1).sections[0].items[0].parts[0]; plant('a wrong key', P.mark(key, '99^99').v !== 'right');
  console.log('planted errors caught:', caught + '/' + planted); }
console.log(fails.length ? fails.length + ' FAILURES\n' + fails.slice(0, 60).join('\n') : 'all checks pass');
process.exit(fails.length ? 1 : 0);
