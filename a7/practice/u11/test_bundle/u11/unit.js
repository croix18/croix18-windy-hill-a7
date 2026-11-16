/* A7 Unit 11 (Solving Equations and Systems): what the practice-test kit needs from this unit (kit/README.md, "The unit interface"). */
(function (root) {
'use strict';
const node = typeof module !== 'undefined' && module.exports;
const E = node ? require('./engine.js') : root.Practice, C = node ? require('./coach.js') : root.Coach;
const F = node ? require('./fig.js') : root.Fig, W = node ? C.Walk : root.Walk;
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const typed = p => p.kind === 'num' || p.kind === 'pair' || p.kind === 'story';
/* every part whose answer is two numbers has two boxes (15 Nov 2026; Croix: "Fix everything"; the kit's several boxes in one part):
   Q12 and Q13(b) x = ▢ and y = ▢ (the paper: "Give its x and its y"), Q14(a) after ▢ weeks and $▢ each (▢ cm tall for the plants),
   Q14(b) x ≈ ▢ and y ≈ ▢. Still one point, judged together by coach.js pairFeedback, each box read by this unit's own reader;
   the key, the paper's choices and the all-multiple-choice paper stay whole ("(4, −2)", "After 5 weeks; $40 each") */
const twoBox = p => p.kind === 'pair' || p.kind === 'story';
const BOXES = p => p.kind === 'story'
  ? [{ pre: 'after', unit: 'weeks', say: 'weeks', kind: 'num' }, p.st.unit === 'dollars' ? { pre: '$', unit: 'each', say: 'dollars each', kind: 'num' } : { unit: 'cm tall', say: 'centimeters tall', kind: 'num' }]
  : ['x', 'y'].map(v => ({ pre: E.M(E.vi(v) + (p.fam === 'estimate' ? ' ≈' : ' =')), say: v, kind: 'num' }));
const Unit = {
  id: 'a7u11',
  contentVersion: 1,                 /* bump whenever any set's questions change (the lock check says so) */
  legacy: [],
  title: 'A7 Unit 11 Practice Test',
  eyebrow: 'Grade 7 Accelerated &nbsp;·&nbsp; Unit 11 &nbsp;·&nbsp; Practice',
  h1: 'Solving Equations and Systems',
  notes: [],                         /* no box takes an ordered pair since 15 Nov 2026: x and y each have their own box */
  /* no notesPrint (15 Nov 2026, the lead for Croix: no rule for writing a point — the question says "Give its x and its y"), so the
     printed directions are the teacher copy's two sentences only */
  keypad: [{ label: '−', say: 'minus', ins: () => '-' }, { label: '/', say: 'fraction bar', kinds: ['num'] }],   /* every box is one number since 15 Nov 2026: no ( ) , keys */
  generate: E.generate,
  key: p => p.key,
  view: {
    boxes: p => twoBox(p) ? BOXES(p) : null,
    /* a select-all's wrong pick is named on the first check (the kit's named distractors) by the coach's own line for it */
    why: (x, k) => x.type === 'multi' && x.correct.indexOf(k) < 0 ? C.SELWHY(x, k) : '',
    stem: it => it.stem,
    figure: it => it.fig ? F.figHtml(it.fig) : '',
    line: p => (p.stem || '') + (p.fig ? F.figHtml(p.fig) : ''),        /* Q14(b) has its own graph */
    pre: p => !typed(p) ? '' : p.fam === 'box' ? '□ =' : p.kind === 'num' && p.v && !p.unit ? E.M(E.vi(p.v) + ' =') : '',
    unit: p => typed(p) && p.unit ? p.unit : '',
    placeholder: () => '',
    form: p => !typed(p) ? null : p.fam === 'estimate' ? { label: 'each to the nearest tenth', equiv: false } : null,
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
  rungs: (x, type, ctx) => C.rungs ? C.rungs(x, type, ctx) : null,      /* Hints 1 and 2, to the help standard (help.js, 15 Nov 2026) */
  solution: (x, type) => type === 'text' ? C.solution(x) : C.mcSolution(x),
  walk: (x, type) => type === 'text' ? W.steps(x) : W.stepsMC(x),
  readNum: W.readNum,
  /* a Hint step's number: exactly — or, for an estimate read off the graph, any number within the tolerance of the key (the crossing
     rounded to the tenth; the lead's ruling, 14 Nov 2026) */
  numOk: (s, v) => s.tol ? Math.abs(E.qnum(v) - E.qnum(s.near)) <= E.qnum(s.tol) + 1e-9 : E.qeq(v, s.ans),
  /* for the checks: what a student would type for the key */
  keyText: p => p.kind === 'num' ? E.kstr(p.ans) : [E.kstr(p.ans[0]), E.kstr(p.ans[1])]          /* two boxes: one string per box */
};
if (node) module.exports = Unit; else root.Unit = Unit;
})(this);
