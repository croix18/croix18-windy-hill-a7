/* A7 Unit 11 (Solving Equations and Systems): what the practice-test kit needs from this unit (kit/README.md, "The unit interface"). */
(function (root) {
'use strict';
const node = typeof module !== 'undefined' && module.exports;
const E = node ? require('./engine.js') : root.Practice, C = node ? require('./coach.js') : root.Coach;
const F = node ? require('./fig.js') : root.Fig, W = node ? C.Walk : root.Walk;
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const typed = p => p.kind === 'num' || p.kind === 'pair' || p.kind === 'story';
const Unit = {
  id: 'a7u11',
  contentVersion: 1,                 /* bump whenever any set's questions change (the lock check says so) */
  legacy: [],
  title: 'A7 Unit 11 Practice Test',
  eyebrow: 'Grade 7 Accelerated &nbsp;·&nbsp; Unit 11 &nbsp;·&nbsp; Practice',
  h1: 'Solving Equations and Systems',
  notes: ['Type an ordered pair like (4, −2): x first, then y.'],
  notesPrint: ['Write an ordered pair as (x, y): x first, then y.'],                  /* paper is not a keyboard */
  keypad: [{ label: '−', say: 'minus', ins: () => '-' }, { label: '/', say: 'fraction bar', kinds: ['num'] },
    { label: '(', say: 'open parenthesis', kinds: ['pair'] }, { label: ')', say: 'close parenthesis', kinds: ['pair'] }, { label: ',', say: 'comma', kinds: ['pair', 'story'] }],
  generate: E.generate,
  key: p => p.key,
  view: {
    /* a select-all's wrong pick is named on the first check (the kit's named distractors) by the coach's own line for it */
    why: (x, k) => x.type === 'multi' && x.correct.indexOf(k) < 0 ? C.SELWHY(x, k) : '',
    stem: it => it.stem,
    figure: it => it.fig ? F.figHtml(it.fig) : '',
    line: p => (p.stem || '') + (p.fig ? F.figHtml(p.fig) : ''),        /* Q14(b) has its own graph */
    pre: p => !typed(p) ? '' : p.fam === 'box' ? '□ =' : p.kind === 'num' && p.v && !p.unit ? E.M(E.vi(p.v) + ' =') : '',
    unit: p => typed(p) && p.unit ? p.unit : '',
    placeholder: () => '',
    form: p => !typed(p) ? null : p.fam === 'estimate' ? { label: 'to the nearest tenth, as (x, y)', expect: 'pair', equiv: false }
      : p.kind === 'pair' ? { label: 'as an ordered pair (x, y)', expect: 'pair' } : p.kind === 'story' ? { label: 'the weeks, then the amount', equiv: false } : null,
    opt: (x, k) => x.opts[k],
    key: p => C.keyHtml(p),
    start: (x, type) => type === 'text' && x.eq && x.fam !== 'box' && x.fam !== 'plans' ? E.M(E.eqH(x.eq)) : x.kind === 'mc' && x.eq ? E.M(E.eqH(x.eq)) : '',
    ex: (x, ex) => ex == null ? '' : E.M(typeof ex === 'string' ? ex : E.eqH(ex)),
    got: s => E.numStr(s.ans),
    picture: () => '',
    pretty: t => { const h = esc(t).replace(/-/g, '−').replace(/\*/g, '·'); return h !== esc(t) ? h : ''; }
  },
  judge: {
    text: (p, a) => C.feedback(p, a),
    mc: (x, k) => C.mcFeedback(x, k),
    multi: (x, ks, tries) => C.selectFeedback(x, ks, tries)
  },
  choices: p => typed(p) ? C.choices(p) : [],                 /* a typed part's wrong answers, for an all-multiple-choice paper (14 Nov 2026) */
  solution: (x, type) => type === 'text' ? C.solution(x) : C.mcSolution(x),
  walk: (x, type) => type === 'text' ? W.steps(x) : W.stepsMC(x),
  readNum: W.readNum,
  /* a Hint step's number: exactly — or, for an estimate read off the graph, any number within the tolerance of the exact one */
  numOk: (s, v) => s.tol ? Math.abs(E.qnum(v) - E.qnum(s.near)) <= E.qnum(s.tol) + 1e-9 : E.qeq(v, s.ans),
  /* for the checks: what a student would type for the key */
  keyText: p => p.kind === 'num' ? E.kstr(p.ans) : p.kind === 'story' ? E.kstr(p.ans[0]) + ', ' + E.kstr(p.ans[1]) : '(' + E.kstr(p.ans[0]) + ', ' + E.kstr(p.ans[1]) + ')'
};
if (node) module.exports = Unit; else root.Unit = Unit;
})(this);
