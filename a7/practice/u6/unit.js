/* A7 Unit 6 (Relationships in Triangles): what the practice-test kit needs from this unit (kit/README.md, "The unit interface"). */
(function (root) {
'use strict';
const node = typeof module !== 'undefined' && module.exports;
const E = node ? require('./engine.js') : root.Practice, C = node ? require('./coach.js') : root.Coach;
const F = node ? require('./fig.js') : root.Fig, W = node ? C.Walk : root.Walk;
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

const Unit = {
  id: 'a7u6',
  contentVersion: 1,                 /* bump whenever any set's questions change (the lock check says so) */
  legacy: [],
  title: 'A7 Unit 6 Practice Test',
  eyebrow: 'Grade 7 Accelerated &nbsp;·&nbsp; Unit 6 &nbsp;·&nbsp; Practice',
  h1: 'Relationships in Triangles',
  notes: ['Give a length to the nearest tenth when the question asks, like 6.4.'],
  keypad: [],
  generate: E.generate,
  key: x => x.key,
  view: {
    stem: it => it.stem,
    figure: it => it.fig ? F.figHtml(it.fig) : '',
    line: p => p.stem,
    pre: p => p.fam === 'simSide' ? E.X + ' =' : '',
    unit: p => p.kind === 'mc' ? '' : p.unit || '',
    placeholder: p => p.tenth ? 'nearest tenth' : '',                /* short enough for a phone's answer box */
    opt: (x, k) => x.opts[k],
    key: p => E.ansHtml(p),
    start: () => '',
    ex: (x, ex) => '<span class="m">' + (ex.approx ? '≈ ' : '= ') + ex.h + '</span>',
    got: s => E.kOut(s.ans),                                       /* a Hint step's answer: 1.5, or 4/3 as a fraction */
    picture: x => { const w = F.why(x); return w ? w.html : ''; },
    pretty: t => { const h = esc(t).replace(/sqrt/gi, '√').replace(/\*/g, ' × ').replace(/\^2/g, '²').replace(/-/g, '−');
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
  /* a Hint step's number: exactly, or — when the answer is a fraction that never ends (k = 4/3) — that fraction rounded to two
     or more decimal places (1.33), as a calculator gives it */
  numOk: (s, v) => E.qeq(v, s.ans) || (E.places(s.ans) < 0 && E.places(v) >= 2 && Math.abs(E.qnum(v) - E.qnum(s.ans)) <= 0.5 * Math.pow(10, -E.places(v)) + 1e-12),
  /* for the checks: what a student would type for the key */
  keyText: p => E.decPlain(p.ans)
};
if (node) module.exports = Unit; else root.Unit = Unit;
})(this);
