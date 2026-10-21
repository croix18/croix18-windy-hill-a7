/* A7 Unit 4 (Solving Problems with Rational Numbers): what the practice-test kit needs from this unit (kit/README.md). */
(function (root) {
'use strict';
const node = typeof module !== 'undefined' && module.exports;
const E = node ? require('./engine.js') : root.Practice, C = node ? require('./coach.js') : root.Coach;
const W = node ? C.Walk : root.Walk;
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const SCI = k => k === 'sci';
const UNITSHORT = { rwArea: 'mm²', rwSpeed: 'km/h', rwSum: 'mm', rwDiff: 'g', patioCost: 'dollars' };

const Unit = {
  id: 'a7u4',
  contentVersion: 3,                 /* bump whenever any set's questions change (the lock check says so). 2: Form B of the test excluded (19 Oct 2026).
                                        3: no significant digits — Part 2 is the four real-world problems, answered exactly (21 Oct 2026) */
  legacy: [],
  title: 'A7 Unit 4 Practice Test',
  eyebrow: 'Grade 7 Accelerated &nbsp;·&nbsp; Unit 4 &nbsp;·&nbsp; Practice',
  h1: 'Solving Problems with Rational Numbers',
  intro: 'Same kinds of questions as the unit test, new numbers every set.',
  /* examples that appear nowhere on the test (review 2, N5) */
  notes: ['Type 7.2 × 10⁶ as 7.2 x 10^6, or tap × 10^.', 'Fractions are fine: −13/6.'],
  notesPrint: ['Write scientific notation like 7.2 × 10⁶. Fractions are fine: −13/6.'],
  /* each kind of answer gets only the keys it uses (review 3) */
  keypad: [{ label: '× 10^', say: 'times ten to the', ins: () => ' x 10^', kinds: ['sci'] }, { label: '−', say: 'minus', ins: () => '-', kinds: ['sci', 'num'] },
    { label: '/', say: 'fraction bar', kinds: ['num'] }, { label: '^', say: 'to the power', kinds: ['expr'] }, { label: '(', say: 'open bracket', kinds: ['expr'] }, { label: ')', say: 'close bracket', kinds: ['expr'] }],
  generate: E.generate,
  key: x => x.key,
  view: {
    stem: it => it.stem,
    figure: () => '',
    line: p => p.stem,
    pre: () => '',
    unit: p => p.kind === 'mc' ? '' : p.fam === 'rate' ? p.prm.noun : UNITSHORT[p.fam] || '',
    placeholder: p => SCI(p.kind) ? 'like 7.2 x 10^6' : p.kind === 'expr' ? 'an expression' : '',
    blank: p => SCI(p.kind) ? '<span class="pblank short"></span> × 10<sup><span class="pblank short" style="min-width:2em"></span></sup>' : '',   /* on paper the shape teaches the form (review 3) */
    opt: (x, k) => x.opts[k],
    key: p => E.ansHtml(p),
    start: () => '',
    ex: (x, ex) => '<span class="m">' + (ex.pre != null ? ex.pre : ex.approx ? '≈ ' : '= ') + ex.h + (ex.tail || '') + '</span>',
    got: s => E.M(E.qF(s.ans)),
    picture: () => '',
    pretty: t => { let h = esc(t).replace(/\*/g, ' × ').replace(/(\d)\s*[xX]\s*(?=\d|\()/g, '$1 × ').replace(/-/g, '−');
      h = h.replace(/\^\(([^()]*)\)|\^(−?\d+)/g, (m0, a, b) => '<sup>' + (a != null ? a : b) + '</sup>').replace(/\s+/g, ' ');
      return h.replace(/\s/g, '') !== esc(t).replace(/\s/g, '') ? h : ''; }
  },
  judge: {
    text: (p, a, ctx) => C.feedback(p, a, ctx),
    mc: (x, k) => C.mcFeedback(x, k),
    multi: (x, ks, tries) => C.selectFeedback(x, ks, tries)
  },
  solution: (x, type) => type === 'text' ? C.solution(x) : C.mcSolution(x),
  walk: (x, type) => type === 'text' ? W.steps(x) : W.stepsMC(x),
  readNum: W.readNum,
  numOk: (s, v) => E.qeq(v, s.ans),
  /* for the checks: what a student would type for the key */
  keyText: p => SCI(p.kind) ? E.minus(p.want.c).replace('−', '-') + ' x 10^' + p.want.k
    : p.kind === 'expr' ? p.prm.s + '^2(' + p.prm.r + ') + ' + p.prm.f
    : p.kind === 'money' ? E.decPlain(p.ans)
    : p.ans.d === 1n ? String(p.ans.n) : (p.ans.n < 0n ? '-' : '') + (p.ans.n < 0n ? -p.ans.n : p.ans.n) + '/' + p.ans.d
};
if (node) module.exports = Unit; else root.Unit = Unit;
})(this);
