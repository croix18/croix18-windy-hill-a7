/* A7 Unit 4 practice: the engine and the coach, checked over many sets.   node u4_check.js [sets=3000] [dumped=1500]
   Written 21 Oct 2026 with the significant-digit change; the 16–19 Oct checks were lost with the session that wrote them.
   For every set: the shape of the test (15 questions, 29 parts, Part 2 the four real-world problems); every key typed back is
   right; every modelled mistake typed is marked wrong and named; the not-finished, standard-form and calculator forms are
   "Almost"; every worked line and every Hint step carries the answer; every Hint choice has one right option and a reason for
   each wrong one; no Hint gives its own answer away; multiple choice and select-all mark their keys; the clean rule holds; no
   question is the test's. dump.json goes to verify.py, which re-derives everything from the printed text with sympy. */
'use strict';
const E = require('./engine.js'), C = require('./coach.js'), U = require('./unit.js'), W = C.Walk;
const fs = require('fs'), path = require('path');
const NSETS = +(process.argv[2] || 3000), NDUMP = Math.min(NSETS, +(process.argv[3] || 1500));
let nfail = 0; const fails = [];
const fail = (seed, where, what) => { nfail++; if (fails.length < 60) fails.push(seed + ' ' + where + ': ' + what); };
const { Q, qeq, qneg, qmul, qdiv, qlt, qabs, sciOf, decPlain, places, p10 } = E;
const sciType = q => { const s = sciOf(q); return s.c + ' x 10^' + s.k; };
const numType = q => places(q) >= 0 ? decPlain(q) : (q.n < 0n ? '-' : '') + (q.n < 0n ? -q.n : q.n) + '/' + q.d;
const plain = h => String(h).replace(/<[^>]+>/g, ' ').replace(/&nbsp;/g, ' ').replace(/\s+/g, ' ').trim();
const numsIn = t => (plain(t).replace(/−/g, '-').match(/\d[\d,]*(?:\.\d+)?/g) || []).map(s => s.replace(/,/g, ''));
/* the test's own section titles, read from its spec (Form A's three, in order) */
const SPEC = fs.readFileSync(path.join(__dirname, '..', '..', 'build', 'u4', 'unit.py'), 'utf8');
const TEST_TITLES = [...SPEC.slice(SPEC.indexOf('forms={"A"')).matchAll(/dict\(title="([^"]+)", benchmark="MA\.8\.NSO\.1\.\d"/g)].slice(0, 3).map(m => m[1]);
const WANT = { titles: TEST_TITLES.join('|'), items: '6,2,7', parts: '12,4,13' };
if (TEST_TITLES.length !== 3) { console.log('could not read the test\'s section titles from unit.py'); process.exit(1); }
const UNITW = { rwArea: ['mm²', 'square millimeters', 'mm^2'], rwSpeed: ['km/h', 'km per hour'], rwSum: ['mm'], rwDiff: ['g', 'grams'], rate: null };
const counts = { sets: 0, parts: 0, models: 0, forms: 0, rounded: 0, solLines: 0, walkSteps: 0, mc: 0, multi: 0 };
const dump = [];

function checkWalk(seed, w, steps, ans) {
  if (!steps || !steps.length) { fail(seed, w, 'no Hint steps'); return; }
  let lastThen = null;
  steps.forEach((s, i) => {
    counts.walkSteps++;
    if (s.type === 'choice') {
      const ok = s.opts.filter(o => o.ok);
      if (ok.length !== 1) fail(seed, w, 'Hint step ' + (i + 1) + ' has ' + ok.length + ' right options');
      if (new Set(s.opts.map(o => o.label)).size !== s.opts.length) fail(seed, w, 'Hint step ' + (i + 1) + ' repeats an option');
      s.opts.filter(o => !o.ok).forEach(o => { if (!o.why) fail(seed, w, 'Hint step ' + (i + 1) + ': no reason for "' + plain(o.label) + '"'); });
    } else if (s.type === 'num') {
      if (!s.ans || s.ans.d === undefined) fail(seed, w, 'Hint step ' + (i + 1) + ' has no exact answer');
      if (!s.hint) fail(seed, w, 'Hint step ' + (i + 1) + ' has no hint');
      /* the kit's division hint names what is left after ten of the divisor; when that equals the quotient (72 ÷ 6: 72 − 60 = 12) it is
         a coincidence of the numbers, not the hint stating its answer (noted for core.js in the Windmill handoff) */
      else if ((plain(s.hint).replace(/ = (\d+) is left\./, ' leaves $1.').replace(/−/g, '-').match(/=\s*-?\d[\d,]*(?:\.\d+)?(?![\d.]*\s*[×x*÷/^+-])/g) || []).some(x => { try { return qeq(E.qdec(x.replace(/^=\s*/, '')), s.ans); } catch (e) { return false; } }))
        fail(seed, w, 'Hint step ' + (i + 1) + ' gives its answer away: ' + plain(s.hint));
      const r = W.readNum(numType(s.ans)); if (!r || !qeq(r, s.ans)) fail(seed, w, 'Hint step ' + (i + 1) + ': its answer typed is not read back');
    } else fail(seed, w, 'Hint step ' + (i + 1) + ' of unknown type ' + s.type);
    if (s.then) { if (!qeq(s.then.v, ans)) fail(seed, w, 'Hint step ' + (i + 1) + ' leads to a different value'); lastThen = s.then; }
  });
  return lastThen;
}

for (let seed = 1; seed <= NSETS; seed++) {
  let G; try { G = U.generate(seed); } catch (e) { fail(seed, 'generate', e.message); continue; }
  counts.sets++;
  if (G.sections.map(s => s.title).join('|') !== WANT.titles) fail(seed, 'titles', G.sections.map(s => s.title).join('|'));
  if (G.sections.map(s => s.items.length).join() !== WANT.items) fail(seed, 'questions', G.sections.map(s => s.items.length).join());
  if (G.sections.map(s => s.items.reduce((t, it) => t + E.partsOf(it).length, 0)).join() !== WANT.parts) fail(seed, 'points', 'not 12, 4, 13');
  const D = seed <= NDUMP ? { seed, items: [] } : null;
  let qn = 0;
  G.sections.forEach((sec, si) => sec.items.forEach(it => {
    qn++; const w = 'Q' + qn;
    if (it.onTest) fail(seed, w, 'a question from the test');
    if (!C.clean(it)) fail(seed, w, 'breaks the clean rule');
    const di = D ? { q: qn, type: it.type, fam: it.fam || null, stem: it.stem, parts: [] } : null;
    if (it.type === 'mc' || it.type === 'multi') {
      if (new Set(it.opts).size !== it.opts.length) fail(seed, w, 'two options the same');
      if (it.type === 'mc') {
        counts.mc++;
        if (C.mcFeedback(it, it.correct).v !== 'right') fail(seed, w, 'the key is not marked right');
        it.opts.forEach((o, k) => { if (k === it.correct) return; const f = C.mcFeedback(it, k);
          if (f.v !== 'wrong') fail(seed, w, 'option ' + k + ' marked ' + f.v);
          else if (/^Not that one/.test(f.what[0])) fail(seed, w, 'option ' + k + ' has no named mistake'); });
        const sol = C.mcSolution(it); if (!sol || !sol.length) fail(seed, w, 'no Show me how');
        const st = W.stepsMC(it); if (st) checkWalk(seed, w, st, null);
      } else {
        counts.multi++;
        if (C.selectFeedback(it, it.correct, 1).v !== 'right') fail(seed, w, 'the key is not marked right');
        const wrong = it.opts.map((o, k) => k).filter(k => it.correct.indexOf(k) < 0);
        if (C.selectFeedback(it, wrong, 2).v !== 'wrong') fail(seed, w, 'the wrong picks are not marked wrong');
        if (it.correct.length !== 4 || wrong.length !== 2) fail(seed, w, 'not 4 right of 6');
      }
      if (di) { di.opts = it.opts; di.correct = it.correct; di.vals = Array.isArray(it.vals) ? it.vals.map(v => v && v.n !== undefined ? v.n + '/' + v.d : null) : null;
        di.target = it.target ? it.target.n + '/' + it.target.d : null; di.prm = it.prm; }
    }
    E.partsOf(it).forEach(p => {
      if (p.kind === 'mc' || it.type === 'mc' || it.type === 'multi') return;
      counts.parts++;
      const pw = w + (p.label || ''), kt = U.keyText(p);
      const r0 = C.feedback(p, kt, {}); if (r0.v !== 'right') fail(seed, pw, 'the key typed as "' + kt + '" is marked ' + r0.v + ': ' + plain((r0.what || [])[0] || ''));
      if (p.kind === 'sci') {
        const s = sciOf(p.ans); if (!(Math.abs(Number(s.c)) >= 1 && Math.abs(Number(s.c)) < 10)) fail(seed, pw, 'key coefficient ' + s.c);
        if (!qeq(p.want.v, p.ans) || p.want.c !== s.c || p.want.k !== s.k) fail(seed, pw, 'want ≠ answer');
        (UNITW[p.fam] || []).forEach(u => { const f = C.feedback(p, kt + ' ' + u, {}); if (f.v !== 'right') fail(seed, pw, 'the key with "' + u + '" is marked ' + f.v); });
        /* the forms that are the right value but not finished: "Almost" */
        const forms = [decPlain(p.ans), s.c + 'e' + s.k];
        const c = E.qdec(s.c); forms.push(decPlain(qmul(c, Q(10))) + ' x 10^' + (s.k - 1), decPlain(qdiv(c, Q(10))) + ' x 10^' + (s.k + 1));
        forms.forEach(f => { counts.forms++; const r = C.feedback(p, f, {}); if (r.v !== 'form') fail(seed, pw, '"' + f + '" (right value, not finished) is marked ' + r.v); });
        const rn = C.feedback(p, '-' + kt, {}); if (rn.v !== 'wrong') fail(seed, pw, 'the key with the wrong sign is marked ' + rn.v);
        /* the key rounded to one digit fewer is wrong, and said to be rounded (unless it is also a modelled mistake, named as that) */
        if (E.digitsOf(s.c) >= 2) {
          counts.rounded++;
          const unit = p10(E.expOf(p.ans) - E.digitsOf(s.c) + 2), x = qdiv(qabs(p.ans), unit);
          let r = x.n / x.d; if ((x.n % x.d) * 2n >= x.d) r += 1n;
          const rv = qmul(Q((p.ans.n < 0n ? -1n : 1n) * r), unit), f = C.feedback(p, sciType(rv), {});
          const named = (C.F[p.fam].models(p) || []).some(m => m.v && qeq(m.v, rv));
          if (f.v !== 'wrong' || (!named && !/rounded/.test(f.what[0]))) fail(seed, pw, 'the key rounded, ' + sciType(rv) + ', is marked ' + f.v + ': ' + plain(f.what[0] || ''));
        }
      }
      /* the clean rule, checked here and not through C.clean: no mistake the coach models is worth the answer */
      const models = C.F[p.fam].models(p) || [];
      if (models.some(m => m.v && qeq(m.v, p.ans))) fail(seed, pw, 'a modelled mistake is worth the answer');
      if (p.kind !== 'sci' && p.kind !== 'expr' && numsIn((it.stem + ' ' + E.partsOf(it).map(x => x.stem || '').join(' ')).replace(/<sup[^>]*>.*?<\/sup>/g, ' ')).some(x => qeq(E.qdec(x), qabs(p.ans))))
        fail(seed, pw, 'the answer is printed in the question');
      E.partsOf(it).forEach(o => { if (o !== p && o.ans && qeq(o.ans, p.ans) && p.fam !== 'patioExpr' && o.fam !== 'patioExpr') fail(seed, pw, 'two parts have the same answer'); });
      /* every modelled mistake, typed, is wrong and named */
      models.forEach(m => {
        if (!m.v || qeq(m.v, p.ans)) return;
        if (places(m.v) < 0 && p.kind === 'sci') return;                    /* a student types a decimal: a repeating value can't be typed exactly */
        counts.models++;
        const typed = p.kind === 'sci' ? (qeq(m.v, Q(0)) ? '0' : sciType(m.v)) : numType(m.v);
        const f = C.feedback(p, typed, {});
        if (f.v !== 'wrong') fail(seed, pw, 'the mistake "' + typed + '" (' + m.say + ') is marked ' + f.v);
        else if (plain(f.what[0]).indexOf(plain(m.say).replace(/\.$/, '').slice(0, 40)) < 0) fail(seed, pw, 'the mistake "' + typed + '" is not named: ' + plain(f.what[0]));
        if (m.step != null && !(m.step >= 0 && m.step < C.solution(p).length)) fail(seed, pw, 'a mistake points at worked line ' + m.step + ' of ' + C.solution(p).length);
      });
      /* Show me how: every line carries the answer */
      const sol = C.solution(p);
      if (!sol || !sol.length) fail(seed, pw, 'no Show me how');
      else sol.forEach((l, i) => { if (l.ex) { counts.solLines++; if (!qeq(l.ex.v, p.ans)) fail(seed, pw, 'worked line ' + (i + 1) + ' is worth something else'); } });
      /* the Hint */
      const st = W.steps(p), last = checkWalk(seed, pw, st, p.ans);
      if (p.kind === 'sci' && (!last || !qeq(last.v, p.ans))) fail(seed, pw, 'the Hint does not end on the answer');
      if (di) di.parts.push({ label: p.label || '', fam: p.fam, kind: p.kind, stem: p.stem, prm: p.prm, key: E.ansHtml(p), keyText: kt, unit: p.unitWord || null,
        sol: sol.filter(l => l.ex && !l.ex.approx).map(l => l.ex.h), keyExpr: p.keyExpr || null,
        walk: st.filter(x => x.type === 'num').map(x => ({ ask: x.ask, ans: x.ans.n + '/' + x.ans.d, then: x.then ? x.then.h : null })) });
    });
    if (di) D.items.push(di);
  }));
  if (D) dump.push(D);
}
/* the exclusion list recognises every test question it holds, in either order where order does not matter */
Object.keys(E.TEST).forEach(f => E.TEST[f].forEach(t => { if (!E.onTest(f, t)) fail(0, 'TEST', f + ' ' + JSON.stringify(t) + ' is not recognised'); }));
fs.writeFileSync(path.join(__dirname, 'dump.json'), JSON.stringify({ TEST: E.TEST, TITLES: E.TITLES, sets: dump }));
console.log(counts.sets + ' sets: ' + counts.parts + ' typed parts, ' + counts.models + ' mistakes typed, ' + counts.forms + ' unfinished forms, ' + counts.rounded + ' keys rounded, ' +
  counts.solLines + ' worked lines, ' + counts.walkSteps + ' Hint steps, ' + counts.mc + ' multiple choice, ' + counts.multi + ' select-all; ' +
  NDUMP + ' sets written to dump.json');
if (nfail) { console.log(nfail + ' PROBLEMS'); fails.forEach(f => console.log('  ' + f)); process.exit(1); }
console.log('u4_check: ALL SOUND');
