/* A7 Unit 5 (Multi-Step Proportional Relationships): what the practice-test kit needs from this unit (kit/README.md, "The unit interface"). */
(function (root) {
'use strict';
const node = typeof module !== 'undefined' && module.exports;
const E = node ? require('./engine.js') : root.Practice, C = node ? require('./coach.js') : root.Coach;
const W = node ? C.Walk : root.Walk;
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
/* the lines a printed set opens with (paper is not a keyboard): the paper test's own (a7/build/lib/unitbuild.py; ruling 19) */
const PRINT = ['Show your work. One point for each lettered part.',
  'If an earlier part is wrong, a later part still earns its point when the right operation is applied to your own earlier answer — but only if that work is on the page.'];
const Unit = {
  id: 'a7u5',
  contentVersion: 1,                 /* bump whenever any set's questions change after students have used the page (the lock check says so) */
  legacy: [],
  title: 'A7 Unit 5 Practice Test',
  eyebrow: 'Grade 7 Accelerated &nbsp;·&nbsp; Unit 5 &nbsp;·&nbsp; Practice',
  h1: 'Multi-Step Proportional Relationships',
  /* an example that is never an answer on this page or the test (a third never ends; every answer here does) */
  notes: ['Type just the number: its unit is beside the box. A mixed number takes a space, like 1 1/3.'],
  notesPrint: PRINT,
  keypad: [{ label: '/', say: 'fraction bar', kinds: ['frac'] }],
  generate: E.generate,
  key: x => x.key,
  view: {
    stem: it => it.stem,
    figure: () => '',
    line: p => p.stem,
    pre: p => p.pre === '$' ? '$' : p.pre ? E.M(E.K + ' =') : '',
    unit: p => p.kind === 'mc' ? '' : p.unit || '',
    placeholder: () => '',
    opt: (x, k) => x.opts[k],
    key: p => E.ansHtml(p),
    start: () => '',
    ex: (x, ex) => E.M(ex.h),
    got: s => s.mixed ? E.mixedOut(s.ans) : s.money ? E.money(s.ans) : E.numStr(s.ans),
    picture: () => '',
    /* what was typed, drawn, when it has a fraction in it: 3 3/4 → 3¾ (never simplified: the picture is what was typed) */
    pretty: t => { const s = String(t == null ? '' : t).trim(); if (!/\d\s*\/\s*\d/.test(s) || s.length > 40) return '';
      return E.M(esc(s).replace(/(\d+)\s*\/\s*(\d+)/g, (m, a, b) => E.fr(a, b)).replace(/-/g, '−').replace(/\*/g, ' × ')); }
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
  keyText: p => p.cups ? E.mixedText(p.ans) : p.money ? E.money(p.ans) : E.decPlain(p.ans)
};
if (node) module.exports = Unit; else root.Unit = Unit;
})(this);
