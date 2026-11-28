/* A7 Unit 11 practice: the cards' arithmetic, proved (27 Nov 2026).   node cards_check.js [sets=20000]
   A term in the help opens its card (help.js's glossary; kit explain.js X.card). Every card is read back from its PRINTED text
   with this file's own reader — its own numbers and polynomials, nothing of the engine's:
   1. every relation of numbers alone (a = b = c, a < b, a ≈ b, a = 4.242…) is true — unless the words right after it say it is
      false or never true, and then it is false; "X rounds to Y" rounds X;
   2. every piece of math with a letter and a relation in it is one of the card's claims below, and the claim holds: same (an
      identity in its letters), solve (lines with one solution set), at (true for the given values), root (the equation's one
      solution), obj (a statement the card names and does not claim), fact (a sentence's claim, as a function), wrong (the
      wrong result a Watch out puts after "not" is wrong: another solution set, or another expression); a statement of numbers
      right after "not" is said to be false;
   3. no example is a question on the page (the card is the same wherever it opens): over sets 1–N, no stem, figure, part or
      choice holds an example's equation (any letter read as any other) or its numbers;
   4. no card writes ×, "slope" or "intercept" (the unit's standing decisions).
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
  wrong: (right, w) => ({ kind: 'wrong', texts: [w], ok: () => /[<>=≤≥]/.test(norm(w)) ? !sameSet(solSet(norm(right)), solSet(norm(w))) : !same(readPoly(norm(right)), readPoly(norm(w))) }),
  fact: (words, fn) => ({ kind: 'fact', words, texts: [], ok: fn })
};
const lin = s => { const { parts } = chain(norm(s)); const R = readPoly(parts[1]); return { m: R.get('x') || 0, b: R.get('') || 0 }; };   /* y = mx + b */
const meetOf = (a, b) => { const x = (b.b - a.b) / (a.m - b.m); return [x, a.m * x + a.b]; };
const r1 = v => Math.round(v * 10) / 10;
const CLAIMS = {
  likeTerms: [C.same('ax + bx = (a + b)x'), C.same('6n + 5 - 2n = 4n + 5'), C.same('5x - 2x = 3x'), C.wrong('5x - 2x', '7x'), C.wrong('4x + 3', '7x')],
  coef: [C.solve(['-3y = 12', 'y = -4']), C.wrong('-3y = 12', 'y = 4')],
  constant: [C.same('3x + 6 - 1 = 3x + 5'), C.fact('the constant is 7, not 3', () => readPoly('3x+7').get('') === 7 && readPoly('3x+7').get('x') === 3),
    C.fact('the constant is −9, not 9', () => readPoly('2x-9').get('') === -9)],
  variable: [C.solve(['w + 4 = 10', 'w = 6']), C.obj('x = 5'), C.at('3x = 3(5) = 15', { x: 5 })],
  distProp: [C.same('a(b + c) = ab + ac'), C.same('4(x + 3) = 4x + 12'), C.same('4(x) = 4x'), C.same('-2(y - 5) = -2y + 10'), C.wrong('4(x + 3)', '4x + 3')],
  varTerm: [C.solve(['7x + 2 = 3x + 14', '4x + 2 = 14']), C.wrong('7x + 2 = 3x + 14', '10x + 2 = 14'), C.same('7x - 3x = 4x')],
  addProp: [C.solve(['y - 6 = 2', 'y = 8']), C.wrong('y - 6 = 2', 'y = 2')],
  subProp: [C.solve(['5x + 1 = 2x + 7', '3x + 1 = 7']), C.wrong('5x + 1 = 2x + 7', '3x + 1 = 2x + 7')],
  divProp: [C.solve(['4n = 18', 'n = 4.5']), C.wrong('4n = 18', 'n = 72')],
  solution: [C.root('2x + 5 = 3x + 1', 4), C.obj('x = 4'), C.fact('the solution is x = 4, not 13', () => solSet('2x+5=3x+1').c === 4 && 2 * 4 + 5 === 13 && 3 * 4 + 1 === 13)],
  noSol: [C.solve(['3x + 4 = 3x + 1', '4 = 1']), C.fact('no solution', () => solSet('3x+4=3x+1').k === 'none'), C.root('3x = 0', 0), C.obj('x = 0'),
    C.fact('has one solution, x = 0, not no solution', () => solSet('3x=0').k === 'one')],
  infSol: [C.solve(['4(x + 1) = 4x + 4', '4x + 4 = 4x + 4', '4 = 4']), C.fact('infinitely many solutions', () => solSet('4(x+1)=4x+4').k === 'all'),
    C.root('2x + 4 = 5x + 4', 0), C.obj('x = 0'), C.fact('has one solution, x = 0, not infinitely many', () => solSet('2x+4=5x+4').k === 'one')],
  system: [C.obj('y = x + 1'), C.obj('y = -5x + 13'), C.fact('The two lines cross at (2, 3)', () => meetOf(lin('y = x + 1'), lin('y = -5x + 13')).join() === '2,3'),
    C.obj('x = 2'), C.fact('the solution is (2, 3), not just x = 2', () => meetOf(lin('y = x + 1'), lin('y = -5x + 13')).join() === '2,3')],
  solSys: [C.obj('y = 6x - 5'), C.obj('y = x + 5'), C.fact('so (2, 7) is a solution', () => meetOf(lin('y = 6x - 5'), lin('y = x + 5')).join() === '2,7'),
    C.fact('So (1, 1) is not a solution', () => 6 * 1 - 5 === 1 && 1 + 5 !== 1)],
  orderedPair: [],
  intersect: [C.obj('y = 6x - 12'), C.obj('y = x + 3'), C.fact('These lines intersect at (3, 6)', () => meetOf(lin('y = 6x - 12'), lin('y = x + 3')).join() === '3,6'),
    C.fact('cross at (3, 6), past your points', () => meetOf(lin('y = x + 3'), lin('y = 6x - 12')).join() === '3,6' && 3 > 2)],
  pointInt: [C.obj('y = x - 1'), C.obj('y = -5x + 17'), C.obj('x = 3'), C.obj('y = 2'), C.fact('The dotted paths lead from (3, 2)', () => meetOf(lin('y = x - 1'), lin('y = -5x + 17')).join() === '3,2'),
    C.fact('cross at (3, 2), not at (0, −1)', () => meetOf(lin('y = x - 1'), lin('y = -5x + 17')).join() === '3,2' && 0 - 1 === -1 && -5 * 0 + 17 !== -1)],
  parallel: [C.obj('y = 0.5x + 3'), C.obj('y = 0.5x - 1'), C.obj('y = 2x + 1'), C.obj('y = -2x + 4'),
    C.fact('always 4 apart', () => { const a = lin('y = 0.5x + 3'), b = lin('y = 0.5x - 1'); return a.m === b.m && a.b - b.b === 4; }),
    C.fact('are crossing lines, not parallel lines', () => lin('y = 2x + 1').m !== lin('y = -2x + 4').m)],
  sameLine: [C.obj('y = 6(x - 1)'), C.obj('y = 6x - 6'), C.same('6(x - 1) = 6x - 6'), C.obj('y = ½x + 9'), C.obj('y = 0.5x + 9'),
    C.fact('are the same line', () => same(readPoly('((1)/(2))x+9'), readPoly('0.5x+9'))),
    C.fact('is the same line as y = 6x - 6, not a different line', () => same(readPoly('6(x-1)'), readPoly('6x-6')))],
  table: [C.obj('y = 6x - 4'), C.obj('x = 0'), C.obj('y = -4'), C.fact('gives y = −4, not 2', () => 6 * 0 - 4 === -4 && 6 - 4 === 2)],
  coefX: [C.obj('y = -x + 13'), C.obj('y = 15'), C.obj('y = 6x + 1'), C.obj('y = 5 - 2x'), C.fact('the coefficient of x is −2, not 5', () => readPoly('5-2x').get('x') === -2)],
  approx: [C.obj('y = 6x - 9'), C.obj('y = -x + 7'), C.fact('about (2.3, 4.7)', () => { const p = meetOf(lin('y = 6x - 9'), lin('y = -x + 7')); return r1(p[0]) === 2.3 && r1(p[1]) === 4.7; }),
    C.fact('not (2, 5), the nearest grid point', () => { const p = meetOf(lin('y = 6x - 9'), lin('y = -x + 7')); return Math.round(p[0]) === 2 && Math.round(p[1]) === 5; })],
  tenth: []
};
/* each example's own problem, which no question on the page may print: an equation (a string), or a system (an array: all its
   lines in one question); any letter is read as any other */
const SIG = { coef: ['-3y = 12'], variable: ['w + 4 = 10'], varTerm: ['7x + 2 = 3x + 14'], addProp: ['y - 6 = 2'], subProp: ['5x + 1 = 2x + 7'], divProp: ['4n = 18'],
  solution: ['2x + 5 = 3x + 1'], noSol: ['3x + 4 = 3x + 1', '3x = 0'], infSol: ['4(x + 1) = 4x + 4', '2x + 4 = 5x + 4'], system: [['y = x + 1', 'y = -5x + 13']], solSys: [['y = 6x - 5', 'y = x + 5']],
  intersect: [['y = 6x - 12', 'y = x + 3']], pointInt: [['y = x - 1', 'y = -5x + 17']], parallel: [['y = 0.5x + 3', 'y = 0.5x - 1']], sameLine: [['y = 6(x - 1)', 'y = 6x - 6']],
  table: ['y = 6x - 4'], coefX: ['y = 6x + 1'], approx: [['y = 6x - 9', 'y = -x + 7']], distProp: ['4(x + 3) = 4x + 12'], likeTerms: ['6n + 5 - 2n = 4n + 5'], constant: ['3x + 6 - 1 = 3x + 5'] };

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
  if (/×|\bslopes?\b|intercept/i.test(prose)) fail(id, 'a student reads ×, "slope" or "intercept"');
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
const eqKey = t => mathPlain(t).replace(/\s+/g, '').replace(/[a-z]/g, 'v');
/* a question's printed math: every math span whole, and each relation in it (a span may hold "y = 2x − 1 and y = x + 3"), and a
   figure's labels (a table's values, a line's name) */
function pageKeys(segs) {
  const out = new Set();
  segs.forEach(h => { h = String(h || '');
    spansOf(h.replace(/<svg[\s\S]*?<\/svg>/g, ' ')).forEach(sp => { const m = sp.math.replace(/\s+/g, '').replace(/[a-z]/g, 'v'); out.add(m); m.split(/,|and|;/).forEach(x => out.add(x)); });
    [...h.matchAll(/<text[^>]*>([^<]*)<\/text>/g)].forEach(m => out.add(eqKey(m[1].replace(/&lt;/g, '<').replace(/&gt;/g, '>'))));
    const words = proseOf(h).replace(/[−–]/g, '-');                     /* an equation printed in plain words: "y = 2x − 1" */
    words.split(/(?<=[a-z0-9)])\s*(?:,|;|\.|\band\b|\?|:)\s*(?=[A-Za-z(−\-\d])/).forEach(x => { const k = x.trim().replace(/\s+/g, '').replace(/[a-z]/g, 'v'); if (/[=<>≤≥]/.test(k)) out.add(k.replace(/^[^\dv(-]+/, '')); }); });
  return out;
}
const sigs = []; Object.keys(SIG).forEach(id => SIG[id].forEach(t => sigs.push({ id, t: [].concat(t), k: [].concat(t).map(eqKey) })));
const seenSig = {};
const V = U.view;
for (let seed = 1; seed <= N; seed++) {
  U.generate(seed).sections.forEach(sec => sec.items.forEach(it => {
    const ps = it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : [it], segs = [V.stem(it), V.figure ? V.figure(it) : ''];
    ps.forEach(p => { if (p !== it && V.line) segs.push(V.line(p)); const ox = p.opts || (p === it ? it.opts : null); if (ox) ox.forEach((o, k) => { try { segs.push(V.opt(p, k)); } catch (e) { segs.push(typeof o === 'string' ? o : ''); } }); });
    const keys = pageKeys(segs);
    sigs.forEach(g => { if (g.k.every(k => keys.has(k))) { const w = g.id + '|' + g.t.join(); if (!seenSig[w]) fail(g.id, 'its example ' + g.t.join(' and ') + ' is a question on the page (set ' + seed + ')'); seenSig[w] = 1; } });
  }));
}
/* ------------------------------------------------------------------ 5: the distribute picture (27 Nov 2026; the lead: "the two
   arrows start at one point and the teal arrow's tail sits on the orange dashed one. Start them side by side from the 4 so
   neither crosses the other"): in the card and in every picture of arrows the help draws over sets 1–M (Hints 1 and 2, Hint 3),
   each arrow starts at its own point, at least 6 units from any other, and no two arrows cross */
const M2 = Math.min(N, 2000); let nArrowPics = 0, nArrows = 0;
const quad = (a, b, c) => { const pts = []; for (let k = 0; k <= 120; k++) { const t = k / 120, u = 1 - t; pts.push([u * u * a[0] + 2 * u * t * b[0] + t * t * c[0], u * u * a[1] + 2 * u * t * b[1] + t * t * c[1]]); } return pts; };
const cross = (p, q, r, s2) => { const d = (a, b, c) => (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
  const d1 = d(r, s2, p), d2 = d(r, s2, q), d3 = d(p, q, r), d4 = d(p, q, s2); return (d1 > 0) !== (d2 > 0) && (d3 > 0) !== (d4 > 0); };
const seenArrows = {};
function arrowsIn(where, html) {
  (String(html || '').match(/<svg[\s\S]*?<\/svg>/g) || []).forEach(svg => {
    const A = [...svg.matchAll(/<path class="xarr xarr\d" d="M([\d.-]+) ([\d.-]+) Q([\d.-]+) ([\d.-]+) ([\d.-]+) ([\d.-]+)"/g)].map(m => m.slice(1).map(Number));
    if (A.length < 2) return; const key = A.map(a => a.join()).join('|'); if (seenArrows[key]) return; seenArrows[key] = 1; nArrowPics++; nArrows += A.length;
    const P = A.map(a => quad([a[0], a[1]], [a[2], a[3]], [a[4], a[5]]));
    for (let i = 0; i < A.length; i++) for (let j = i + 1; j < A.length; j++) {
      if (Math.hypot(A[i][0] - A[j][0], A[i][1] - A[j][1]) < 6) fail(where, 'two arrows start at one point (' + A[i][0] + ', ' + A[i][1] + ')');
      let hit = false; for (let a = 0; a < P[i].length - 1 && !hit; a++) for (let b = 0; b < P[j].length - 1 && !hit; b++) hit = cross(P[i][a], P[i][a + 1], P[j][b], P[j][b + 1]);
      if (hit) fail(where, 'two arrows cross: ' + svg.match(/aria-label="([^"]*)"/)[1].slice(0, 80)); } });
}
ids.forEach(id => arrowsIn('card ' + id, X.card(id)));
require('./coach.js'); const kinds = it => it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : [it];
for (let seed = 1; seed <= M2; seed++) U.generate(seed).sections.forEach(sec => sec.items.forEach(it => kinds(it).forEach(p => {
  const t = p.kind === 'nline' ? 'nline' : (p.kind === 'mc' || it.type === 'mc' && p === it) ? 'mc' : it.type === 'multi' ? 'multi' : 'text';
  let R; try { R = U.rungs(p, t, {}) || {}; } catch (e) { return; }
  [R.notice, R.first && R.first.say].concat((R.steps || []).map(l => l.say)).forEach(h => arrowsIn('set ' + seed + ' ' + (p.fam || it.fam), h)); })));
const n0 = ids.length;
fails.forEach(f => console.log('FAIL ' + f));
console.log('cards: ' + n0 + ' cards, ' + nClaims + ' claims and ' + nAuto + ' numeric statements read back and proved; ' + sigs.length + ' examples kept off ' + N + ' sets of the page; ' + nArrowPics + ' pictures of arrows (' + nArrows + ' arrows, the card and the help over sets 1–' + M2 + '), none starting together or crossing — ' + (fails.length ? fails.length + ' problems' : 'all true'));
process.exit(fails.length ? 1 : 0);
