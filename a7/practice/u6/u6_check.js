/* A7 Unit 6 practice: the engine, the coach and the figures, checked over many sets.   node u6_check.js [sets=3000] [dumped=1500]
   For every set: the shape of the test (the section titles read from build/u6/unit.py; 14 questions, 18 parts); every key typed
   back is right, with its unit too; every modelled mistake typed is marked wrong and named; a tenth answer's exact root and its
   longer decimals are "Almost", and the decimal cut off is wrong; a whole answer written as its root is "Almost"; the clean rule
   holds (checked here on its own, not through the coach's); every worked line and every Hint step carries the right number; every
   Hint choice has one right option and a reason for each wrong one; no Hint gives its own answer away; multiple choice and
   select-all mark their keys and name every wrong option; follow-through from a wrong part (a) is recognised; every arithmetic
   claim in a sentence is true; every figure and picture is drawn to its own numbers, each label nearest its own segment, crossing
   no line and touching no other label (ruling 44); no question asks numbers a lesson showed (ruling 43). dump.json goes to
   verify.py, which works everything out again from the printed text with Python's own arithmetic. */
'use strict';
const E = require('./engine.js'), C = require('./coach.js'), U = require('./unit.js'), FG = require('./fig.js'), W = C.Walk;
const fs = require('fs'), path = require('path');
const NSETS = +(process.argv[2] || 3000), NDUMP = Math.min(NSETS, +(process.argv[3] || 1500));
let nfail = 0; const fails = [];
const fail = (seed, where, what) => { nfail++; if (fails.length < 60) fails.push(seed + ' ' + where + ': ' + what); };
const { Q, qeq, qnum, qabs, decPlain, places } = E;
const plain = h => String(h).replace(/\u00a0/g, ' ').replace(/<span class="fr"><span class="nu">([^<]*)<\/span><span class="de">([^<]*)<\/span><\/span>/g, '($1÷$2)').replace(/<sup[^>]*>(.*?)<\/sup>/g, '^$1').replace(/<[^>]+>/g, ' ').replace(/&nbsp;/g, ' ').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim();
const numType = q => places(q) >= 0 ? decPlain(q) : q.n + '/' + q.d;                        /* what a student types: 14.8, or 4/3 */
/* the test's own section titles, read from its spec, and the shape of its practice paper */
const SPEC = fs.readFileSync(path.join(__dirname, '..', '..', 'build', 'u6', 'unit.py'), 'utf8');
const TEST_TITLES = [...SPEC.matchAll(/dict\(title="([^"]+)", benchmark="MA\.8\.GR\.\d\.\d", items=_gr\d\d\(\)\)/g)].map(m => m[1]);
const WANT = { titles: TEST_TITLES.join('|'), items: '3,4,4,3', parts: '3,6,6,3', types: 'mc,multi,mc|parts,solo,mc,parts|solo,solo,parts,parts|solo,solo,mc' };
if (TEST_TITLES.length !== 4) { console.log('could not read the test\'s four section titles from unit.py'); process.exit(1); }
const counts = { sets: 0, parts: 0, models: 0, forms: 0, solLines: 0, walkSteps: 0, mc: 0, multi: 0, labels: 0, pictures: 0, claims: 0, follow: 0 };
const dump = [];

/* ---------- every arithmetic claim in a sentence is true. A claim is a chain "e = e = …" of numeric expressions (+ − × ÷,
   squares, √n, parentheses); every link must be worth the same. A number ending in "…" is cut off after its last digit, so the
   chain may differ by one in that place for each such number (and the cut is checked: √218 = 14.764… means 14.764 ≤ √218 <
   14.765). "e ≈ d" means e rounds to d. "the square root of n, d…" is checked as a cut too. No fraction is ever printed. */
const TERM = '(?:√\\s*)?(?:\\(\\s*-?\\d+(?:\\.\\d+)?\\s*\\)|\\(\\s*\\d+\\s*÷\\s*\\d+\\s*\\)|\\d+(?:\\.\\d+)?)…?(?:\\^2)?';
const EXPR = TERM + '(?:\\s*[-+×÷]\\s*' + TERM + ')*';
const CHAIN = new RegExp('(?<![\\w.^√)…])' + EXPR + '(?:\\s*(?:=|≈)\\s*' + EXPR + ')+(?![\\w^(…]|\\.\\d)', 'g');
function evalE(s) {
  const js = s.replace(/…/g, '').replace(/×/g, '*').replace(/÷/g, '/').replace(/√\s*(\d+(?:\.\d+)?)/g, 'Math.sqrt($1)').replace(/(\d+(?:\.\d+)?|\))\^2/g, '$1**2');
  if (!/^(?:[\d\s.+\-*/()]|Math\.sqrt)+$/.test(js)) return null;
  try { const v = Function('return (' + js + ')')(); return isFinite(v) ? v : null; } catch (e) { return null; }
}
function claims(seed, w, h) {
  const t0 = plain(h);
  if (/\d\s*\/\s*\d/.test(t0)) fail(seed, w, 'a fraction is printed: ' + t0.slice(0, 120));
  const t = t0.replace(/−/g, '-').replace(/²/g, '^2').replace(/(\d),(?=\d{3}(?!\d))/g, '$1').replace(/the square root of (?=\d)/g, '√');
  let m;
  CHAIN.lastIndex = 0;
  while ((m = CHAIN.exec(t))) {
    const run = m[0], links = run.split(/\s*(=|≈)\s*/);
    const vals = [], ops = [];
    for (let i = 0; i < links.length; i++) { if (i % 2) ops.push(links[i]); else vals.push(evalE(links[i])); }
    if (vals.some(v => v == null)) continue;
    counts.claims++;
    const cuts = (run.match(/…/g) || []).length, tol = cuts ? 0.001 * cuts + 1e-9 : 1e-9;
    for (let i = 0; i + 1 < vals.length; i++) {
      if (ops[i] === '≈') { const right = links[2 * i + 2], dp = (right.split('.')[1] || '').replace(/…/, '').length;
        if (Math.abs(vals[i] - vals[i + 1]) > 0.5 * Math.pow(10, -dp) + 1e-9) fail(seed, w, 'a claim is false: ' + run); }
      else if (Math.abs(vals[i] - vals[i + 1]) > tol) fail(seed, w, 'a claim is false: ' + run);
    }
    /* "e = d…" where e has no cut of its own: d is e cut off */
    links.forEach((l, i) => { if (i % 2 || i === 0 || !/…$/.test(l) || /…/.test(links[i - 2])) return;
      const d = Number(l.replace(/…/, '')), dp = (l.split('.')[1] || '').replace(/…/, '').length, e = vals[(i - 2) / 2];
      if (!(e >= d - 1e-12 && e < d + Math.pow(10, -dp))) fail(seed, w, 'a cut-off decimal is wrong: ' + run); });
  }
  const sr = /√(\d+), (\d+\.\d+)…/g;
  while ((m = sr.exec(t))) { counts.claims++; const e = Math.sqrt(+m[1]), d = +m[2], dp = m[2].split('.')[1].length;
    if (!(e >= d - 1e-12 && e < d + Math.pow(10, -dp))) fail(seed, w, 'a cut-off root is wrong: ' + m[0]); }
}

/* ---------- figures: every label is the length drawn, on its own segment, clear of lines and other labels */
function checkBoard(seed, w, B) {
  B.labels.forEach((l, i) => {
    counts.labels++;
    if (l.a) {
      if (l.v != null) { const g = Math.hypot(l.gb[0] - l.ga[0], l.gb[1] - l.ga[1]); if (Math.abs(g - l.v) > (l.tol || 1e-9) + 1e-9) fail(seed, w, 'label ' + l.s + ' says ' + l.v + ' but the segment is ' + g.toFixed(4));
        const said = Number(plain(l.s).replace(/ ft$/, '').replace(/,/g, '').replace(/−/g, '-')); if (!(Math.abs(said - l.v) < 1e-9)) fail(seed, w, 'label "' + plain(l.s) + '" is on a segment of ' + l.v); }
      const own = FG.segD([l.x, l.y], l.a, l.b);
      if (own > 40) fail(seed, w, 'label ' + plain(l.s) + ' is ' + own.toFixed(0) + 'px from its segment');
      B.labels.forEach((o, j) => { if (j !== i && o.a && FG.segD([l.x, l.y], o.a, o.b) + 0.5 < own) fail(seed, w, 'label ' + plain(l.s) + ' sits nearer to the segment labelled ' + plain(o.s)); });
    } else if (l.pt) {
      const d = Math.hypot(l.x - l.pt[0], l.y - l.pt[1]); if (d > 60) fail(seed, w, 'the label ' + plain(l.s) + ' is ' + d.toFixed(0) + 'px from its point');
      if (B.frame && (l.box[0] < B.frame[0] - 0.5 || l.box[3] > B.frame[3] + 0.5)) fail(seed, w, 'the label ' + plain(l.s) + ' hangs below or left of the plane, where its numbers are');
    }
    B.segs.forEach(sg => { if (FG.boxHitsSeg(l.box, sg[0], sg[1])) fail(seed, w, 'label ' + plain(l.s) + ' crosses a drawn line'); });
    B.labels.forEach((o, j) => { if (j > i && FG.boxesHit(l.box, o.box)) fail(seed, w, 'labels ' + plain(l.s) + ' and ' + plain(o.s) + ' overlap'); });
    (B.keep || []).forEach(kb => { if (FG.boxesHit(l.box, kb) && !(l.pt && Math.abs(kb[0] + 4 - l.pt[0]) < 0.01 && Math.abs(kb[1] + 4 - l.pt[1]) < 0.01)) fail(seed, w, 'label ' + plain(l.s) + ' covers a point or a word'); });
  });
}
function checkFig(seed, w, it) {
  const f = it.fig, B = FG.figModel(f);
  checkBoard(seed, w + ' figure', B);
  const labs = B.labels.map(l => plain(l.s));
  /* ruling 44: a number the words give with a unit is on the figure; a number on the figure is in the words or is the figure's own */
  if (f.kind === 'rtri') { if (B.labels.filter(l => l.v != null).length !== 2 || labs.filter(s => s === 'x').length !== 1) fail(seed, w, 'the right triangle does not show two lengths and x'); }
  if (f.kind === 'simPair') { if (labs.filter(s => s === 'x').length !== 1 || B.labels.filter(l => l.v != null).length !== 5) fail(seed, w, 'the similar pair does not show five lengths and x');
    const ra = E.sorted(f.a), rb = E.sorted(f.b), k = rb[0] / ra[0]; if (rb.some((v, i) => Math.abs(v - ra[i] * k) > 1e-9)) fail(seed, w, 'the two triangles drawn are not similar');
    /* named (25 Oct 2026): the words name the corners the figure letters, in its order, and each letter stands at its own corner */
    const m = /^Triangle ([A-Z]{3}) is similar to triangle ([A-Z]{3})\./.exec(plain(it.stem));
    if (!!m !== !!f.na) fail(seed, w, m ? 'the words name the triangles and the figure does not' : 'the figure letters corners the words do not name');
    if (m && f.na) {
      if (m[1] !== f.na.join('') || m[2] !== f.nb.join('')) fail(seed, w, 'the words name ' + m[1] + ' and ' + m[2] + ', the figure ' + f.na.join('') + ' and ' + f.nb.join(''));
      if (new Set(f.na.concat(f.nb)).size !== 6) fail(seed, w, 'a letter names two corners');
      [[f.na, B.meta.A], [f.nb, B.meta.C]].forEach(([nm, T]) => nm.forEach((c, i) => {
        const l = B.labels.find(x => x.pt && plain(x.s) === c), at = B.px(T[i]);
        if (!l) fail(seed, w, 'corner ' + c + ' is not lettered');
        else if (Math.hypot(l.pt[0] - at[0], l.pt[1] - at[1]) > 0.01) fail(seed, w, 'the letter ' + c + ' is not at its corner');
        else if (T.some((P, j) => j !== i && Math.hypot(l.x - B.px(P)[0], l.y - B.px(P)[1]) < Math.hypot(l.x - at[0], l.y - at[1]))) fail(seed, w, 'the letter ' + c + ' stands nearer another corner');
      }));
    } }
  if (f.kind === 'shadow' || f.kind === 'mirror') {
    const words = plain(it.stem); f.lab.slice(0, 3).forEach(s => { if (words.indexOf(s.replace(' ft', '')) < 0) fail(seed, w, 'the figure\'s ' + s + ' is not in the words'); });
    const r1 = f.h1 / (f.s1 || f.d1), r2 = f.h2 / (f.s2 || f.d2); if (Math.abs(r1 - r2) > 1e-9) fail(seed, w, 'the two triangles are not similar');
  }
  if (f.kind === 'grid2' || f.kind === 'gridTri') {
    f.pts.forEach(p => { if (Math.abs(p[0]) > 10 || Math.abs(p[1]) > 10 || p[0] === 0 || p[1] === 0) fail(seed, w, 'a point off the −10…10 grid or on an axis'); });
    if (f.kind === 'gridTri') { const st = plain(it.stem); f.pts.forEach(p => { const s = p[2] + '(' + E.minus(String(p[0])) + ', ' + E.minus(String(p[1])) + ')'; if (st.indexOf(s) < 0) fail(seed, w, 'corner ' + s + ' is drawn but not in the words'); }); }
  }
  return B;
}

function checkWalk(seed, w, steps, ans) {
  if (!steps || !steps.length) { fail(seed, w, 'no Hint steps'); return; }
  steps.forEach((s, i) => {
    counts.walkSteps++;
    claims(seed, w + ' Hint', s.ask + ' ' + (s.hint || '') + ' ' + (s.opts || []).map(o => o.label + ' ' + o.why).join(' '));
    if (s.type === 'choice') {
      const ok = s.opts.filter(o => o.ok);
      if (ok.length !== 1) fail(seed, w, 'Hint step ' + (i + 1) + ' has ' + ok.length + ' right options');
      if (new Set(s.opts.map(o => plain(o.label))).size !== s.opts.length) fail(seed, w, 'Hint step ' + (i + 1) + ' repeats an option');
      s.opts.filter(o => !o.ok).forEach(o => { if (!o.why) fail(seed, w, 'Hint step ' + (i + 1) + ': no reason for "' + plain(o.label) + '"'); });
    } else if (s.type === 'num') {
      if (!s.ans || s.ans.d === undefined) fail(seed, w, 'Hint step ' + (i + 1) + ' has no exact answer');
      else if (places(s.ans) < 0) {                                    /* a fraction that never ends: typed as a fraction, or rounded */
        if (!/A fraction is fine\./.test(s.hint || '')) fail(seed, w, 'Hint step ' + (i + 1) + ' asks for ' + E.numStr(s.ans) + ' without saying a fraction is fine');
        const r2 = W.readNum((qnum(s.ans)).toFixed(2)), r1 = W.readNum((qnum(s.ans)).toFixed(1));
        if (!r2 || !U.numOk(s, r2)) fail(seed, w, 'Hint step ' + (i + 1) + ': ' + qnum(s.ans).toFixed(2) + ' for ' + E.numStr(s.ans) + ' is not accepted');
        if (r1 && U.numOk(s, r1)) fail(seed, w, 'Hint step ' + (i + 1) + ': ' + qnum(s.ans).toFixed(1) + ' for ' + E.numStr(s.ans) + ' is accepted');
      }
      if (!s.hint) fail(seed, w, 'Hint step ' + (i + 1) + ' has no hint');
      else if ((plain(s.hint).replace(/−/g, '-').match(/=\s*-?\d[\d,]*(?:\.\d+)?(?![\d.]*\s*[×x*÷/^+-])/g) || []).some(x => { try { return qeq(E.qdec(x.replace(/^=\s*/, '')), s.ans); } catch (e) { return false; } }))
        fail(seed, w, 'Hint step ' + (i + 1) + ' gives its answer away: ' + plain(s.hint));
      const r = W.readNum(numType(s.ans)); if (!r || !qeq(r, s.ans) || !U.numOk(s, r)) fail(seed, w, 'Hint step ' + (i + 1) + ': its answer typed is not read back');
    } else fail(seed, w, 'Hint step ' + (i + 1) + ' of unknown type ' + s.type);
    if (s.then && ans && !qeq(s.then.v, ans)) fail(seed, w, 'Hint step ' + (i + 1) + ' leads to a different value');
  });
}
const tenthOf = x => Math.round(x * 10 + 1e-9) / 10;
const FOLLOW = {
  shorter: (p, a) => p.prm.w + p.prm.l - a,                                                   /* the two sides, less your path */
  perim: (p, a) => { const { J, K, L } = p.prm, h = J[1] === K[1] ? Math.abs(L[1] - K[1]) : Math.abs(L[0] - K[0]);
    return a + h + Math.sqrt(a * a + h * h); }                                                 /* your side, the other leg, and the slant from them */
};

for (let seed = 1; seed <= NSETS; seed++) {
  let G; try { G = U.generate(seed); } catch (e) { fail(seed, 'generate', e.message); continue; }
  counts.sets++;
  if (G.sections.map(s => s.title).join('|') !== WANT.titles) fail(seed, 'titles', G.sections.map(s => s.title).join('|'));
  if (G.sections.map(s => s.items.length).join() !== WANT.items) fail(seed, 'questions', G.sections.map(s => s.items.length).join());
  if (G.sections.map(s => s.items.reduce((t, it) => t + E.partsOf(it).length, 0)).join() !== WANT.parts) fail(seed, 'points', 'not 3, 6, 6, 3');
  if (G.sections.map(s => s.items.map(it => it.type).join()).join('|') !== WANT.types) fail(seed, 'types', G.sections.map(s => s.items.map(it => it.type).join()).join('|'));
  /* ruling 43 on the test (the second review, 25 Oct 2026): no question asks numbers a lesson showed — question 2 offers no
     right triangle a lesson showed whole as a right set, 4(a) is 5-12-13 or 9-12-15, and 4(b), 5 and 7 use no legs and no
     hypotenuse-and-leg pair a warm-up, the notes, an example or a Your Turn worked */
  { const [s1, s2] = [G.sections[0].items, G.sections[1].items];
    s1[1].sets.forEach((s, i) => { if (s1[1].correct.indexOf(i) >= 0 && E.SHOWN_CONV.has(E.setKey(s))) fail(seed, 'Q2', 'a right set a lesson showed: ' + s.join(', ')); });
    const [pa, pb] = s2[0].parts;
    if (!E.TRIPLE_TEST.some(t => E.legKey(t[0], t[1]) === E.legKey(pa.prm.a, pa.prm.b))) fail(seed, 'Q4a', 'legs ' + pa.prm.a + ' and ' + pa.prm.b + ' are not a test triangle');
    if (E.shownLeg(pb.prm.c, pb.prm.a)) fail(seed, 'Q4b', 'a hypotenuse and leg a lesson showed: ' + pb.prm.c + ', ' + pb.prm.a);
    const p5 = s2[1].part;
    if (p5.prm.ctx ? E.shownLeg(p5.prm.c, p5.prm.a) : E.SHOWN_LEGS.has(E.legKey(p5.prm.a, p5.prm.b))) fail(seed, 'Q5', 'numbers a lesson showed: ' + JSON.stringify(p5.prm));
    const p7 = s2[3].parts[0];
    if (E.SHOWN_LEGS.has(E.legKey(p7.prm.w, p7.prm.l))) fail(seed, 'Q7', 'legs a lesson showed: ' + p7.prm.w + ', ' + p7.prm.l);
    counts.ruling43 = (counts.ruling43 || 0) + 1; }
  const D = seed <= NDUMP ? { seed, items: [] } : null;
  let qn = 0;
  G.sections.forEach((sec, si) => sec.items.forEach(it => {
    qn++; const w = 'Q' + qn;
    if (!C.clean(it)) fail(seed, w, 'breaks the clean rule');
    claims(seed, w, it.stem);
    const di = D ? { q: qn, type: it.type, fam: it.fam || null, stem: it.stem, fig: it.fig || null, parts: [] } : null;
    if (it.fig) { const B = checkFig(seed, w, it); if (di) di.figLabels = B.labels.map(l => ({ s: plain(l.s), v: l.v })); }
    if (it.type === 'mc' || it.type === 'multi') {
      if (new Set(it.opts).size !== it.opts.length) fail(seed, w, 'two options the same');
      const sol = C.mcSolution(it); if (!sol || !sol.length) fail(seed, w, 'no Show me how'); else sol.forEach(l => claims(seed, w + ' Show me how', l.say));
      const st = W.stepsMC(it); if (st) checkWalk(seed, w, st, null); else fail(seed, w, 'no Hint');
      if (it.type === 'mc') {
        counts.mc++;
        if (C.mcFeedback(it, it.correct).v !== 'right') fail(seed, w, 'the key is not marked right');
        it.opts.forEach((o, k) => { if (k === it.correct) return; const f = C.mcFeedback(it, k);
          if (f.v !== 'wrong') fail(seed, w, 'option ' + k + ' marked ' + f.v);
          else if (/^Not that one/.test(f.what[0])) fail(seed, w, 'option ' + k + ' has no named mistake'); else claims(seed, w + ' option ' + k, f.what[0]); });
      } else {
        counts.multi++;
        if (C.selectFeedback(it, it.correct, 1).v !== 'right') fail(seed, w, 'the key is not marked right');
        const wrong = it.opts.map((o, k) => k).filter(k => it.correct.indexOf(k) < 0);
        if (C.selectFeedback(it, wrong, 2).v !== 'wrong') fail(seed, w, 'the wrong picks are not marked wrong');
        if (!wrong.length || it.correct.length < 1 || it.correct.length > 3) fail(seed, w, it.correct.length + ' right of ' + it.opts.length);
        it.sets.forEach((s, i) => { const t = E.sorted(s); if ((t[0] * t[0] + t[1] * t[1] === t[2] * t[2]) !== (it.correct.indexOf(i) >= 0)) fail(seed, w, 'option ' + i + ' keyed wrongly'); });
        if (!it.sets.some((s, i) => it.correct.indexOf(i) >= 0 && s[0] === Math.max(...s))) fail(seed, w, 'no right set lists its longest side first');
        C.mcSolution(it).forEach(l => claims(seed, w + ' why', l.say));
      }
      if (di) { di.opts = it.opts; di.correct = it.correct; di.prm = it.prm; di.sol = sol.map(l => l.say);
        di.walk = (st || []).filter(x => x.type === 'num').map(x => ({ ask: x.ask, ans: x.ans.n + '/' + x.ans.d })); }
    }
    E.partsOf(it).forEach((p, pi) => {
      if (it.type === 'mc' || it.type === 'multi') return;
      counts.parts++;
      const pw = w + (p.label || ''), kt = U.keyText(p), a = qnum(p.ans);
      if (!p.unit && p.fam !== 'simSide') fail(seed, pw, 'no unit beside the answer box');
      [kt, kt + ' ' + (p.unit || ''), 'about ' + kt].forEach(t => { const r0 = C.feedback(p, t, {}); if (r0.v !== 'right') fail(seed, pw, 'the key typed as "' + t + '" is marked ' + r0.v + ': ' + plain((r0.what || [])[0] || '')); });
      if (p.tenth) {
        if (Math.abs(a - tenthOf(p.exact)) > 1e-9) fail(seed, pw, 'the key ' + kt + ' is not ' + p.exact + ' to the nearest tenth');
        if (places(p.ans) !== 1) fail(seed, pw, 'a tenth answer that is not one decimal place: ' + kt);
        const forms = [p.exact.toFixed(2), p.exact.toFixed(3)].filter(t => Math.abs(Number(t) - a) > 1e-9 && tenthOf(Number(t)) === a);
        if (p.rad) forms.push('√' + p.rad, 'sqrt(' + p.rad + ')');
        forms.forEach(t => { counts.forms++; const r = C.feedback(p, t, {}); if (r.v !== 'form') fail(seed, pw, '"' + t + '" (right, not rounded to the tenth) is marked ' + r.v); });
        const cut = Math.floor(p.exact * 10 + 1e-9) / 10; if (Math.abs(cut - a) > 1e-9) { const r = C.feedback(p, String(cut), {}); if (r.v !== 'wrong') fail(seed, pw, 'the decimal cut off, ' + cut + ', is marked ' + r.v); }
      } else {
        if (!Number.isInteger(a * 2) && places(p.ans) > 1) fail(seed, pw, 'a whole-number question with the answer ' + kt);
        if (Number.isInteger(a) && a <= 120) { counts.forms++; const r = C.feedback(p, '√' + a * a, {}); if (r.v !== 'form') fail(seed, pw, '√' + a * a + ' is marked ' + r.v); }
      }
      const rn = C.feedback(p, '-' + kt, {}); if (rn.v !== 'wrong') fail(seed, pw, 'the key with a minus sign is marked ' + rn.v);
      /* the clean rule, here and not through C.clean: no mistake is worth the answer, no printed number is the answer */
      const models = C.F[p.fam].models(p) || [];
      const fz = m => m.f != null ? m.f : places(m.v) < 0 ? qnum(m.v) : null;
      if (models.some(m => (m.v && qeq(m.v, p.ans)) || (fz(m) != null && Math.abs(fz(m) - a) < 0.1))) fail(seed, pw, 'a modelled mistake is worth the answer');
      if (C.printedNumbers(it).some(x => qeq(x, qabs(p.ans)))) fail(seed, pw, 'the answer is printed in the question');
      E.partsOf(it).forEach(o => { if (o !== p && qeq(o.ans, p.ans)) fail(seed, pw, 'two parts have the same answer'); });
      /* every modelled mistake, typed, is wrong and named */
      models.forEach(m => {
        counts.models++;
        const typed = m.v && places(m.v) >= 0 ? numType(m.v) : String(tenthOf(fz(m)));
        const f = C.feedback(p, typed, {});
        if (f.v !== 'wrong') fail(seed, pw, 'the mistake "' + typed + '" (' + plain(m.say) + ') is marked ' + f.v);
        else if (plain(f.what[0]).indexOf(plain(m.say).replace(/\.$/, '').slice(0, 40)) < 0) fail(seed, pw, 'the mistake "' + typed + '" is not named: ' + plain(f.what[0]));
        if (fz(m) != null) { const f2 = C.feedback(p, fz(m).toFixed(2), {}); if (f2.v !== 'wrong') fail(seed, pw, 'the mistake ' + fz(m).toFixed(2) + ' is marked ' + f2.v); }
        if (m.step != null && !(m.step >= 0 && m.step < C.solution(p).length)) fail(seed, pw, 'a mistake points at worked line ' + m.step + ' of ' + C.solution(p).length);
        claims(seed, pw + ' mistake', m.say);
      });
      /* follow-through (ruling 19; the test's follow_through: 7(b) from 7(a), 10(b) from 10(a)): a wrong part (a), worked on
         correctly, is recognised. What "worked on correctly" gives is worked out here, not taken from the coach */
      if (!!C.F[p.fam].follow !== (p.fam in FOLLOW)) fail(seed, pw, 'follow-through ' + (C.F[p.fam].follow ? 'offered where the test has none' : 'missing'));
      if (FOLLOW[p.fam] && pi > 0) {
        const pa = E.partsOf(it)[0], wrongA = qnum(pa.ans) + 1, want = FOLLOW[p.fam](p, wrongA);
        counts.follow++;
        const f = C.feedback(p, String(tenthOf(want)), { prev: String(wrongA), prevPart: pa });
        if (Math.abs(tenthOf(want) - a) > 0.05 && !/Your method for this part is right/.test(plain((f.what || [])[0] || ''))) fail(seed, pw, 'follow-through from part (a) = ' + wrongA + ' is not recognised: ' + plain((f.what || [])[0] || ''));
      }
      /* Show me how: every worked line with a value carries the answer */
      const sol = C.solution(p);
      if (!sol || !sol.length) fail(seed, pw, 'no Show me how');
      else sol.forEach((l, i) => { claims(seed, pw + ' Show me how', l.say + (l.ex ? ' ' + l.ex.h : '')); if (l.ex) { counts.solLines++; if (!qeq(l.ex.v, p.ans)) fail(seed, pw, 'worked line ' + (i + 1) + ' is worth something else'); } });
      if (!sol.some(l => l.ex)) fail(seed, pw, 'Show me how never reaches the answer');
      claims(seed, pw + ' rule', C.F[p.fam].rule(p));
      /* the Hint */
      const st = W.steps(p); checkWalk(seed, pw, st, p.ans);
      const lastNum = st.filter(x => x.type === 'num').pop(); if (!lastNum || !qeq(lastNum.ans, p.ans)) fail(seed, pw, 'the Hint does not end on the answer');
      /* the picture */
      const pic = U.view.picture(p); if (pic) { counts.pictures++; const B = FG.why(p); checkBoard(seed, pw + ' picture', B); claims(seed, pw + ' picture', B.cap); }
      if (di) di.parts.push({ label: p.label || '', fam: p.fam, stem: p.stem, prm: p.prm, unit: p.unit || null, tenth: !!p.tenth, key: E.ansHtml(p), keyText: kt,
        sol: sol.map(l => ({ say: l.say, h: l.ex ? l.ex.h : null, approx: !!(l.ex && l.ex.approx) })), walk: st.filter(x => x.type === 'num').map(x => ({ ask: x.ask, ans: x.ans.n + '/' + x.ans.d })),
        rule: C.F[p.fam].rule(p), models: models.map(m => ({ say: m.say, v: m.v ? m.v.n + '/' + m.v.d : null, f: m.f != null ? m.f : null })) });
    });
    if (di) D.items.push(di);
  }));
  if (D) dump.push(D);
}
fs.writeFileSync(path.join(__dirname, 'dump.json'), JSON.stringify({ TITLES: E.TITLES, sets: dump }));
console.log(counts.sets + ' sets: ' + counts.parts + ' typed parts, ' + counts.models + ' mistakes typed, ' + counts.forms + ' "Almost" forms, ' + counts.follow + ' follow-throughs, ' +
  counts.solLines + ' worked lines, ' + counts.walkSteps + ' Hint steps, ' + counts.mc + ' multiple choice, ' + counts.multi + ' select-all, ' + counts.labels + ' figure labels, ' +
  counts.pictures + ' pictures, ' + counts.claims + ' arithmetic claims; ruling 43 held in ' + (counts.ruling43 || 0) + ' sets; ' + NDUMP + ' sets written to dump.json');
if (nfail) { console.log(nfail + ' PROBLEMS'); fails.forEach(f => console.log('  ' + f)); process.exit(1); }
console.log('u6_check: ALL SOUND');
