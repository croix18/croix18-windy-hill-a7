/* A7 Unit 6 practice: the cards' arithmetic, proved (27 Nov 2026).   node cards_check.js [sets=20000]
   A term in the help opens its card (help.js's glossary; kit explain.js X.card). Every card is read back from its PRINTED text
   with this file's own reader — its own numbers, squares and roots, nothing of the engine's:
   1. every relation of numbers alone (a = b = c, a < b < c, √n ≈ r to its decimals, √n = 4.690… cut there) is true — unless the
      words right after it say it is false, or it comes right after "not" (a Watch out's wrong one: "test 30² + 40² = 50², not
      30² + 50² = 40²"), and then it is false — and "X rounds to Y" rounds X;
   2. every piece of math with a letter and a relation in it is one of the card's claims below, and the claim holds: at (true for
      the given values: c = √250 in c² = 81 + 169 = 250), obj (a statement the card names, a² + b² = c²), fact (a sentence's claim,
      as a function);
   3. no example is a question on the page (the card is the same wherever it opens). By construction (help.js's glossary note):
      every hypotenuse or leg a card works has a square over 225 (the page's cap), or is a whole triangle the page never offers,
      every root is of a number that is neither a sum nor a difference of two squares (42, 22, 14: 4k + 2, with a prime factor
      4k + 3), every triangle has a longest side under 8 or fails the page's own test for a drawable triangle, every scale factor
      is off its list, and every point is outside its −10…10 or 1…6 off an axis. And checked: over sets 1–N, no stem, figure's
      labels, part or choice prints exactly an example's numbers (a problem is its numbers: legs 9 and 13, sides 3, 5 and 7), or
      its two points;
   4. no card writes ×.
   It prints each failure and exits 1 on any. */
'use strict';
global.window = global;
const U = require('./unit.js'), X = require('../kit/explain.js'), GL = X.glossary();
const N = +(process.argv[2] || 20000);
const fails = []; const fail = (id, what) => fails.push(id + ': ' + what);

/* ------------------------------------------------------------------ the card's text: math spans as plain math, prose as words */
function mathPlain(h) {                                                    /* the unit's math html → this reader's math */
  let t = String(h), k;
  for (let i = 0; i < 6; i++) t = t.replace(/<span class="fr"><span class="nu">((?:(?!<span class="fr">)[\s\S])*?)<\/span><span class="de">((?:(?!<span class="fr">)[\s\S])*?)<\/span><\/span>/, '(($1)/($2))');
  for (let i = 0; i < 6; i++) t = t.replace(/<span class="rad[^"]*">(?:<span class="rg">)?√(?:<\/span>)?<span class="rc">((?:(?!<span class="rad)[\s\S])*?)<\/span><\/span>/, 'sqrt($1)');
  t = t.replace(/<sup>([^<]*)<\/sup>/g, '^$1').replace(/<[^>]+>/g, '').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&').replace(/&nbsp;| /g, ' ');
  return t.replace(/[−–]/g, '-').replace(/·/g, '*').replace(/÷/g, '/').replace(/½/g, '((1)/(2))').replace(/⅓/g, '((1)/(3))').replace(/⅔/g, '((2)/(3))').replace(/¼/g, '((1)/(4))').replace(/¾/g, '((3)/(4))').replace(/²/g, '^2').replace(/√(\d+)/g, 'sqrt($1)').replace(/\s+/g, ' ').trim();
}
function spansOf(h) {                                                      /* every top-level math span, whole */
  const out = [], s = String(h); let k = 0;
  while ((k = s.indexOf('<span class="m"', k)) >= 0) { let d = 0, j = k; const re = /<span\b|<\/span>/g; re.lastIndex = k; let m;
    while ((m = re.exec(s))) { if (m[0] === '</span>') { d--; if (!d) { j = re.lastIndex; break; } } else d++; }
    out.push({ at: k, end: j, math: mathPlain(s.slice(s.indexOf('>', k) + 1, j - 7)) }); k = j; }
  return out;
}
const noSvg = h => String(h).replace(/<svg[\s\S]*?<\/svg>/g, ' ');
function proseOf(h) {                                                      /* the words, each math span as its plain math */
  const s = noSvg(h), sp = spansOf(s); let out = '', k = 0; sp.forEach((x, i) => { out += s.slice(k, x.at) + ' ⟦' + i + '⟧ '; k = x.end; }); out += s.slice(k);
  out = out.replace(/<[^>]+>/g, ' ').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&').replace(/&nbsp;|\u00a0/g, ' ').replace(/[−–]/g, '-');
  return out.replace(/⟦(\d+)⟧/g, (m0, i) => sp[+i].math).replace(/\s+/g, ' ').replace(/ ([,.;:?])(?=\s|$)/g, '$1').trim();   /* the math back only once the tags are gone: it may hold < */
}

/* ------------------------------------------------------------------ this file's own reader: polynomials over the letters */
const P = (m, c) => new Map([[m, c]]), EPS = 1e-9;
const padd = (A, B) => { const o = new Map(A); B.forEach((c, m) => { const v = (o.get(m) || 0) + c; if (Math.abs(v) < EPS) o.delete(m); else o.set(m, v); }); return o; };
const pmul = (A, B) => { let o = new Map(); A.forEach((a, ma) => B.forEach((b, mb) => { o = padd(o, P((ma + mb).split('').sort().join(''), a * b)); })); return o; };
const pneg = A => { const o = new Map(); A.forEach((c, m) => o.set(m, -c)); return o; };
const num = A => { if (A.size > 1 || (A.size === 1 && !A.has(''))) throw new Error('not a number'); return A.get('') || 0; };
function readPoly(s0) {
  const t = String(s0).replace(/\s+/g, ''); let i = 0;
  const peek = () => t[i];
  function expr() { let a = term(); for (;;) { if (peek() === '+') { i++; a = padd(a, term()); } else if (peek() === '-') { i++; a = padd(a, pneg(term())); } else return a; } }
  function term() { let a = power(); for (;;) { const c = peek(); if (c === '*') { i++; a = pmul(a, power()); } else if (c === '/') { i++; a = pmul(a, P('', 1 / num(power()))); }
      else if (c && /[\d.(a-zA-Z]/.test(c)) a = pmul(a, power()); else return a; } }
  function power() { let a = unary(); if (peek() === '^') { i++; const e = num(unary()); let r = P('', 1); for (let k = 0; k < e; k++) r = pmul(r, a); return r; } return a; }
  function unary() { if (peek() === '-') { i++; return pneg(unary()); } if (peek() === '+') { i++; return unary(); } return atom(); }
  function atom() { const c = peek(); if (c === undefined) throw new Error('end');
    if (t.startsWith('sqrt(', i)) { i += 5; const e = expr(); if (peek() !== ')') throw new Error(')'); i++; return P('', Math.sqrt(num(e))); }
    if (/[\d.]/.test(c)) { const m = /^\d{1,3}(?:,\d{3})+(?:\.\d+)?|^\d*\.?\d+/.exec(t.slice(i)); i += m[0].length; return P('', parseFloat(m[0].replace(/,/g, ''))); }
    if (c === '(') { i++; const e = expr(); if (peek() !== ')') throw new Error(')'); i++; return e; }
    if (/[a-zA-Z]/.test(c)) { i++; return P(c, 1); }
    throw new Error('char ' + c); }
  const e = expr(); if (i !== t.length) throw new Error('left: ' + t.slice(i)); return e;
}
const REL = /\s*(<=|>=|≤|≥|≈|=|<|>)\s*/;
const chain = s => { const bits = String(s).split(REL); const parts = [], rels = []; bits.forEach((b, i) => { if (i % 2) rels.push(b.replace('<=', '≤').replace('>=', '≥')); else parts.push(b.trim()); }); return { parts, rels }; };
const same = (A, B) => { const D = padd(A, pneg(B)); return [...D.values()].every(v => Math.abs(v) < 1e-7); };
const subst = (A, vals) => { let v = 0; A.forEach((c, m) => { let t = c; for (const ch of m) { if (!(ch in vals)) throw new Error('no value for ' + ch); t *= vals[ch]; } v += t; }); return v; };
/* a decimal written with … is the value cut off there; a value after ≈ is the left side rounded to its decimals */
const decs = s => { const m = /\.(\d+)/.exec(s); return m ? m[1].length : 0; };
function relHolds(a, rel, b, bText, aText) {
  if (/…$/.test(bText || '')) { const d = decs(bText), cut = Math.trunc(a * 10 ** d + (a >= 0 ? 1e-9 : -1e-9)) / 10 ** d; return Math.abs(cut - b) < 1e-9; }
  if (rel === '=') return Math.abs(a - b) < 1e-7 * Math.max(1, Math.abs(a));
  if (rel === '≈') { const d = decs(bText); return Math.abs(a - b) <= 0.5 * 10 ** -d + 1e-9 && Math.abs(a - b) > 1e-12; }
  return rel === '<' ? a < b - EPS : rel === '>' ? a > b + EPS : rel === '≤' ? a <= b + EPS : a >= b - EPS;
}
/* a relation in one letter → its solution set: {k: 'one'|'all'|'none'|'ray', rel, c} */
function solSet(s) {
  const { parts, rels } = chain(s); if (parts.length !== 2) throw new Error('not one relation: ' + s);
  const D = padd(readPoly(parts[0]), pneg(readPoly(parts[1]))), vs = [...D.keys()].filter(m => m);
  if (vs.some(m => m.length > 1) || new Set(vs).size > 1) throw new Error('not linear in one letter: ' + s);
  const a = vs.length ? D.get(vs[0]) : 0, b = D.get('') || 0, r = rels[0];
  if (Math.abs(a) < EPS) return { k: relHolds(b, r, 0) ? 'all' : 'none' };
  const c = -b / a; if (r === '=') return { k: 'one', c };
  const flip = { '<': '>', '>': '<', '≤': '≥', '≥': '≤' }; return { k: 'ray', rel: a > 0 ? r : flip[r], c };
}
const sameSet = (A, B) => A.k === B.k && (A.k === 'all' || A.k === 'none' || (Math.abs(A.c - B.c) < 1e-9 && A.rel === B.rel));

/* ------------------------------------------------------------------ the claims each card makes, by hand */
const norm = s => mathPlain(s).replace(/\s+/g, '');
const C = {
  same: t => ({ kind: 'same', texts: [t], ok: () => { const { parts } = chain(norm(t)); const ps = parts.map(readPoly); return ps.every(p => same(p, ps[0])); } }),
  solve: ts => ({ kind: 'solve', texts: ts, ok: () => { const s0 = solSet(norm(ts[0])); return ts.every(t => sameSet(solSet(norm(t)), s0)); } }),
  at: (t, vals) => ({ kind: 'at', texts: [t], ok: () => { const { parts, rels } = chain(norm(t)); const v = parts.map(p => subst(readPoly(p), vals)); return rels.every((r, i) => relHolds(v[i], r, v[i + 1], parts[i + 1], parts[i])); } }),
  root: (t, c) => ({ kind: 'root', texts: [t], ok: () => { const s = solSet(norm(t)); return s.k === 'one' && Math.abs(s.c - c) < 1e-9; } }),
  obj: t => ({ kind: 'obj', texts: [t], ok: () => true }),
  fact: (words, fn) => ({ kind: 'fact', words, texts: [], ok: fn })
};
const R = Math.sqrt;
const CLAIMS = {
  triIneq: [C.fact('Sides 3, 5 and 7 make a triangle', () => 3 + 5 > 7), C.fact('Sides 2, 5 and 7 do not', () => !(2 + 5 > 7)),
    C.fact('Sides 2, 5 and 7 make no triangle, because 2 + 5 = 7, not more', () => 2 + 5 === 7 && !(2 + 5 > 7))],
  leg: [C.fact('The legs, 21 and 28, form the right angle', () => 21 * 21 + 28 * 28 === 35 * 35),
    C.fact('the other leg is 21, not about 44.8, which comes from adding the squares', () => 35 * 35 - 28 * 28 === 21 * 21 && Math.round(R(35 * 35 + 28 * 28) * 10) / 10 === 44.8)],
  hyp: [C.obj('a^2 + b^2 = c^2'), C.at('c^2 = 2.5^2 + 6^2 = 6.25 + 36 = 42.25', { c: 6.5 }), C.at('c = sqrt(42.25) = 6.5', { c: 6.5 }), C.fact('The hypotenuse, 6.5, is longer than either leg', () => 6.5 > 6 && 6.5 > 2.5),
    C.fact('the hypotenuse is 6.5, not 6, the bottom side', () => R(2.5 * 2.5 + 6 * 6) === 6.5)],
  pyth: [C.obj('a^2 + b^2 = c^2'), C.at('a^2 + 5^2 = 16^2', { a: R(231) }), C.at('a^2 = 256 - 25 = 231', { a: R(231) }), C.at('a = sqrt(231) ≈ 15.2', { a: R(231) }), C.fact('Check: 15.2 is shorter than 16', () => 15.2 < 16), C.at('a^2 = 16^2 - 5^2', { a: R(231) })],
  converse: [C.fact('The squares match, so it is a right triangle', () => 30 * 30 + 40 * 40 === 50 * 50), C.fact('It is not a right triangle', () => 30 * 30 + 40 * 40 !== 51 * 51)],
  sqrt: [C.fact('is between 5 and 6', () => 5 < R(30) && R(30) < 6), C.fact('To the nearest tenth, it is 6.5', () => Math.round(R(42) * 10) / 10 === 6.5),
    C.fact('not 18, because', () => R(36) === 6 && 36 / 2 === 18)],
  tenth: [C.fact('rounds to 4.7, not 4.6', () => Math.round(R(22) * 10) / 10 === 4.7 && Math.trunc(R(22) * 10) / 10 === 4.6),
    C.fact('not 4.4 from 2.2 + 2.2', () => Math.round(2 * R(5) * 10) / 10 === 4.5 && Math.round(R(5) * 10) / 10 === 2.2 && Math.round((2.2 + 2.2) * 10) / 10 === 4.4)],
  horiz: [C.fact('From −3 to 5 is 8 units, not 2', () => 5 - (-3) === 8 && 5 + (-3) === 2)],
  vert: [C.fact('the distance is 7, not 0 from 8 - 8', () => 1 - (-6) === 7 && 8 - 8 === 0)],
  perimeter: [C.at('P = 10 + 12 + sqrt(244) ≈ 37.6', { P: 22 + R(244) }), C.fact('is about 15.6, not 22 along the grid lines', () => Math.round(R(10 * 10 + 12 * 12) * 10) / 10 === 15.6 && 10 + 12 === 22)],
  similar: [C.fact('Every ratio is 4, so the triangles are similar', () => 6 / 1.5 === 4 && 10 / 2.5 === 4 && 12 / 3 === 4),
    C.fact('Sides 2, 3, 4 and 4, 6, 9 are not similar', () => 4 / 2 === 2 && 6 / 3 === 2 && 9 / 4 === 2.25)],
  corr: [C.fact('1.5 matches 4.5, not 6', () => 4.5 / 1.5 === 3 && 6 / 2 === 3 && 9 / 3 === 3)],
  scale: [C.at('k = 7 ÷ 2 = 3.5', { k: 3.5 }), C.at('x = 5(3.5) = 17.5', { x: 17.5 }), C.fact('which would shrink the copy', () => 2 / 7 < 1 && 7 > 2)]
};
/* each example's own problem, which no question of its kind on the page may print: f, the page's kinds of question it could be
   (its families); sets, each printed exactly (these numbers and no others) in one stem, figure's labels, part or choice of one
   question; pts, points printed in one place. Two triangles are one problem only when both are in one question. */
const RT = /^(hypWhole|hypTenth|legTenth|eqChoice|diag|shorter|rightSel)$/, GRID = /^(gridWhole|coordTenth|crossSide|perim|streets|straight)$/, SIM = /^(simSide|simChoice|shadow|mirror)$/;
const SIG = { triIneq: [{ f: /^(triSet|range)$/, sets: [[3, 5, 7]] }, { f: /^(triSet|range)$/, sets: [[2, 5, 7]] }],
  leg: [{ f: RT, sets: [[21, 28, 35]] }, { f: RT, sets: [[21, 28]] }], hyp: [{ f: RT, sets: [[2.5, 6]] }], pyth: [{ f: RT, sets: [[16, 5]] }],
  converse: [{ f: RT, sets: [[30, 40, 50]] }, { f: RT, sets: [[30, 40, 51]] }],
  horiz: [{ f: GRID, pts: ['(-3,8)', '(5,8)'] }], vert: [{ f: GRID, pts: ['(8,-6)', '(8,1)'] }], perimeter: [{ f: GRID, pts: ['(10,0)', '(10,12)'] }],
  similar: [{ f: SIM, sets: [[1.5, 2.5, 3], [6, 10, 12]] }, { f: SIM, sets: [[2, 3, 4], [4, 6, 9]] }], corr: [{ f: SIM, sets: [[1.5, 2, 3], [4.5, 6, 9]] }], scale: [{ f: SIM, sets: [[2, 5, 7]] }] };

/* ------------------------------------------------------------------ 1, 2, 4: every card */
let nClaims = 0, nAuto = 0;
/* a statement of numbers is said to be false when the words right after it say so */
const FALSE_AFTER = /^[\s,]*(?:which\s+)?(?:is\s+)?(?:never true|false|not true)\b/;
const NUM = '-?\\d{1,3}(?:,\\d{3})+(?:\\.\\d+)?…?|-?\\d+(?:\\.\\d+)?…?';
const EXPR = '(?:\\(\\s*)?(?:' + NUM + ')(?:\\s*\\)?\\s*[-+*/]\\s*\\(?\\s*(?:' + NUM + ')\\s*\\)?)*(?:\\s*\\))?';
const STMT = new RegExp('(?<![\\w.,⟧(])' + EXPR + '(?:\\s*(?:<=|>=|≤|≥|≈|=|<|>)\\s*' + EXPR + ')+(?![\\w⟦(]|\\.\\d)', 'g');
function checkStmt(id, run, after, before) {
  run = run.trim(); while ((run.match(/\)/g) || []).length > (run.match(/\(/g) || []).length && /\)$/.test(run)) run = run.slice(0, -1).trim();
  while ((run.match(/\(/g) || []).length > (run.match(/\)/g) || []).length && /^\(/.test(run)) run = run.slice(1).trim();
  const { parts, rels } = chain(run); if (parts.length < 2 || parts.some(p => !p.replace(/…/g, ''))) return;
  let v; try { v = parts.map(p => num(readPoly(p.replace(/…/g, '')))); } catch (e) { fail(id, 'a statement could not be read: ' + run); return; }
  nAuto++; if (process.env.SHOW) console.log('  [' + id + '] ' + run);
  const claimedFalse = FALSE_AFTER.test(after) || /\bnot\s*$/.test(before || ''), holds = rels.every((r, i) => relHolds(v[i], r, v[i + 1], parts[i + 1], parts[i]));
  if (claimedFalse ? holds : !holds) fail(id, 'a numeric statement is ' + (claimedFalse ? 'said to be false but is true' : 'false') + ': ' + run);
}
function autoNumeric(id, html, covered) {                                  /* every statement of numbers alone: in the math and in the words */
  const s = noSvg(html), items = spansOf(s); let out = '', k = 0;
  items.forEach((sp, i) => { out += s.slice(k, sp.at) + ' ⟦' + i + '⟧ '; k = sp.end; }); out += s.slice(k);
  const prose = out.replace(/<[^>]+>/g, ' ').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&').replace(/&nbsp;| /g, ' ').replace(/[−–]/g, '-').replace(/\s+/g, ' ');
  items.forEach((sp, i) => { const t = sp.math, at = prose.indexOf('⟦' + i + '⟧');
    if (/[a-zA-Z]/.test(t.replace(/sqrt/g, '')) || !REL.test(t) || covered.has(t.replace(/\s+/g, ''))) return;
    checkStmt(id, t, prose.slice(at + String(i).length + 2), prose.slice(0, at)); });
  let m; STMT.lastIndex = 0;
  while ((m = STMT.exec(prose))) checkStmt(id, m[0], prose.slice(m.index + m[0].length), prose.slice(0, m.index));
  /* "3.46 rounds to 3.5" */
  prose.replace(/(-?\d+\.\d+)…?,?\s+(?:which\s+)?rounds to (-?\d+(?:\.\d+)?)/g, (m0, x, y) => { nAuto++; if (Math.abs(Math.round(parseFloat(x) * 10 ** decs(y)) / 10 ** decs(y) - parseFloat(y)) > 1e-9) fail(id, 'a rounding is wrong: ' + m0); });
}
const ids = Object.keys(GL).filter(id => !GL[id].card);
ids.forEach(id => {
  const html = X.card(id), prose = proseOf(html), claims = CLAIMS[id];
  if (!claims) { fail(id, 'no claims listed in cards_check.js'); return; }
  if (/×/.test(prose)) fail(id, 'a student reads ×');
  claims.forEach(c => { nClaims++;
    let ok = false; try { ok = c.ok(); } catch (e) { fail(id, c.kind + ' could not be read: ' + (c.texts[0] || c.words) + ' (' + e.message + ')'); return; }
    if (!ok) fail(id, 'a ' + c.kind + ' claim is false: ' + (c.texts.join(' | ') || c.words));
    if (c.kind === 'fact' && prose.toLowerCase().indexOf(c.words.replace(/[−–]/g, '-').toLowerCase()) < 0) fail(id, 'the card does not say: "' + c.words + '"'); });
  const covered = new Set([].concat(...claims.map(c => c.texts.map(norm))));
  const spans = spansOf(noSvg(html));
  spans.forEach(sp => { const t = sp.math.replace(/\s+/g, '');
    if (/[a-zA-Z]/.test(t.replace(/sqrt/g, '')) && REL.test(t) && !covered.has(t)) fail(id, 'its math "' + sp.math + '" has a letter and a relation but is no claim listed here'); });
  claims.forEach(c => c.texts.forEach(t => { if (!spans.some(sp => sp.math.replace(/\s+/g, '') === norm(t))) fail(id, 'the claim "' + t + '" is not printed on the card'); }));
  autoNumeric(id, html, covered);
});

/* ------------------------------------------------------------------ 3: no example is a question on the page */
const segText = h => { h = String(h || ''); const lab = [...h.matchAll(/<text([^>]*)>([^<]*)<\/text>/g)].filter(m => !/\btick\b|\bax\b/.test(m[1])).map(m => m[2]).join(' ');   /* a figure's labels, not its axes' numbers */
  return (proseOf(h) + ' ' + lab).replace(/[−–]/g, '-').replace(/\u00a0/g, ' ').replace(/\^\d+/g, ''); };          /* an exponent is not one of the problem's numbers */
const tokens = t => { const nums = new Set((t.replace(/(\d),(\d{3})/g, '$1$2').match(/-?\d+(?:\.\d+)?/g) || []).map(Number)), pts = new Set((t.replace(/\s+/g, '').match(/\(-?\d+,-?\d+\)/g) || [])); return { nums, pts }; };
const sigs = []; Object.keys(SIG).forEach(id => SIG[id].forEach(g => sigs.push(Object.assign({ id }, g))));
const sameNums = (tk, set) => tk.nums.size === new Set(set).size && set.every(v => tk.nums.has(v));
const seenSig = {};
const V = U.view;
for (let seed = 1; seed <= N; seed++) {
  U.generate(seed).sections.forEach(sec => sec.items.forEach(it => {
    const ps = it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : [it], fams = [it.fam].concat(ps.map(p => p.fam)).filter(Boolean), segs = [V.stem(it), V.figure ? V.figure(it) : ''];
    ps.forEach(p => { if (p !== it && V.line) segs.push(V.line(p)); const ox = p.opts || (p === it ? it.opts : null); if (ox) ox.forEach((o, k) => { try { segs.push(V.opt(p, k)); } catch (e) { segs.push(typeof o === 'string' ? o : ''); } }); });
    const tks = segs.map(segText).map(tokens);
    sigs.forEach(g => { if (!fams.some(f => g.f.test(f))) return;
      const hit = (g.sets || []).every(set => tks.some(tk => sameNums(tk, set))) && (g.pts || []).every(pt => tks.some(tk => tk.pts.has(pt)));
      if (hit) { const w = g.id + '|' + JSON.stringify(g.sets || g.pts); if (!seenSig[w]) fail(g.id, 'its example ' + JSON.stringify(g.sets || g.pts) + ' is a question on the page (set ' + seed + ', ' + fams.join('/') + ')'); seenSig[w] = 1; } });
  }));
}
const n0 = ids.length;
fails.forEach(f => console.log('FAIL ' + f));
console.log('cards: ' + n0 + ' cards, ' + nClaims + ' claims and ' + nAuto + ' numeric statements read back and proved; ' + sigs.length + ' examples kept off ' + N + ' sets of the page — ' + (fails.length ? fails.length + ' problems' : 'all true'));
process.exit(fails.length ? 1 : 0);
