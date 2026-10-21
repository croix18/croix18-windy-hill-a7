/* A7 Unit 3 (Exponents and Scientific Notation): what the practice-test kit needs from this unit (kit/README.md). */
(function (root) {
'use strict';
const node = typeof module !== 'undefined' && module.exports;
const E = node ? require('./engine.js') : root.Practice, C = node ? require('./coach.js') : root.Coach;
const VZ = node ? require('./visual.js') : root.Visual, WK = node ? require('./walk.js') : root.Walk;
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const sciish = k => k === 'sci' || k === 'std' || k === 'times';
function numAst(q) { const neg = q.n < 0n, n = neg ? -q.n : q.n; let a; if (q.d === 1n) a = E.N(n.toString(), { commas: true }); else { try { a = E.N(E.decStr(E.Q(n, q.d)), { commas: true }); } catch (e) { a = E.Fr(E.N(n.toString()), E.N(q.d.toString())); } } return neg ? E.Neg(a) : a; }

const Unit = {
  id: 'a7u3',
  contentVersion: 4,                 /* bump whenever any set's questions change (the lock check says so); v3 was the page before the kit */
  legacy: ['a7u3prac.v3.', 'a7u3prac.v2.', 'a7u3prac.v1.'],
  title: 'A7 Unit 3 Practice Test',
  eyebrow: 'Grade 7 Accelerated &nbsp;·&nbsp; Unit 3 &nbsp;·&nbsp; Practice',
  h1: 'Exponents and Scientific Notation',
  notes: [],
  keypad: [{ label: '^', say: 'power' }, { label: '/', say: 'divided by' }, { label: '×', say: 'times', ins: k => sciish(k) ? ' x ' : '*' },
    { label: '−', say: 'minus', ins: () => '-' }, { label: '(', say: 'open bracket' }, { label: ')', say: 'close bracket' }],
  generate: E.generate,
  key: x => { try { if (x.type === 'mc') return E.plain(x.q) + '|' + x.opts.map(E.plain).join(','); if (x.type === 'multi') return E.plain(x.target) + '|' + x.opts.map(E.plain).sort().join(','); return E.plain(x.q); } catch (e) { return JSON.stringify([x.fam, x.prm]); } },
  view: {
    stem: it => it.type === 'parts' ? esc(it.stem) : it.stem,
    figure: () => '',
    line: p => p.text ? p.text.map(x => typeof x === 'string' ? esc(x) : E.M(x)).join('') : E.M(p.q) + (p.after ? esc(p.after) : ''),
    pre: p => p.kind === 'n' ? '<span class="m"><i>n</i> =</span>' : '',
    unit: () => '',
    placeholder: () => '',
    opt: (x, k) => E.M(x.opts[k]),
    key: p => (p.kind === 'n' ? '<span class="m"><i>n</i> = </span>' : '') + E.M(p.shownAns || p.ans) + (p.tail ? esc(p.tail) : ''),
    start: (x, type) => { const q = type === 'multi' ? null : x.q; return q ? E.M(q) : ''; },
    ex: (x, ex, type) => (type === 'text' && x.fam === 'solveN' ? '' : '<span class="m">= </span>') + E.M(ex),
    got: s => E.M(numAst(s.ans)),
    picture: (x, type) => { const sp = type === 'text' ? VZ.spec(x) : x.fam && x.fam !== 'select' ? VZ.spec({ fam: x.fam, prm: x.prm }) : null; return sp ? VZ.html(sp) : ''; },
    /* the typing preview: ^ then a number, a letter, or a bracket — never the letters after it (Apple review R1-6) */
    pretty: (t, kind) => {
      let h = esc(t).replace(/\*\*/g, '^').replace(/-/g, '−');
      h = h.replace(/\^\(([^()]*)\)|\^(−?\d+|[a-z])/gi, (m0, a, b) => '<sup>' + (a != null ? a : b) + '</sup>');
      if (sciish(kind)) h = h.replace(/([0-9])\s*[x*]\s*(?=10)/gi, '$1 × ');
      h = h.replace(/\*/g, '·');
      return h !== esc(t) ? h : '';
    }
  },
  judge: {
    text: (p, a) => C.feedback(p, a),
    mc: (x, k) => C.mcFeedback(x, k),
    multi: (x, ks, tries) => C.selectFeedback(x, ks, tries)
  },
  solution: (x, type) => type === 'text' ? C.solution(x) : C.mcSolution(x),
  walk: (x, type) => type === 'text' ? WK.steps(x) : WK.stepsMC(x),
  readNum: WK.readNum,
  numOk: (s, v) => E.qeq(v, s.ans) || (s.places && E.qeq(v, E.qmul(s.ans, E.Q(-1)))),
  keyText: p => C.typedOf(p.ans)
};
if (node) module.exports = Unit; else root.Unit = Unit;
})(this);
