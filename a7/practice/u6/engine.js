/* A7 Unit 6 practice (Relationships in Triangles): exact numbers, reading what a student types, drawing the numbers, and the
   questions. Ruling 49 (22 Oct 2026): the unit test is a random set of this page, so its fourteen questions are the practice
   test's (a7/build/u6/unit.py) — the same kinds, order and points, new numbers every set.

   The unit's bounds hold on every question (the lesson outlines, "standing decisions"): a square root a student takes is of a
   whole number up to 225 (MA.8.GR.1.1/1.2 Clarification 3), so a whole hypotenuse is 5, 10, 13 or 15 and a bigger triple
   appears only in the converse or as a missing leg; no distance formula — a slanted distance is the right triangle on the
   grid; the converse tests the longest side; similar triangles by the scale factor k. A length the question asks for "to the
   nearest tenth" may come from a radicand with a square factor (√72): the decimal is the answer and no worked line prints the
   radical, so nothing on the page is an unsimplified radical (an exact √n is printed only when n has no square factor). */
(function (root) {
'use strict';
const KIT = (typeof module !== 'undefined' && module.exports) ? require('../kit/core.js') : root.Kit;

/* ------------------------------------------------------------------ exact rationals {n, d} (BigInt) */
function gcd(a, b) { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) { const t = a % b; a = b; b = t; } return a; }
function Q(n, d) {
  n = BigInt(n); d = d === undefined ? 1n : BigInt(d);
  if (d === 0n) throw new Error('division by zero');
  if (d < 0n) { n = -n; d = -d; }
  const g = gcd(n, d) || 1n; return { n: n / g, d: d / g };
}
const qadd = (a, b) => Q(a.n * b.d + b.n * a.d, a.d * b.d);
const qsub = (a, b) => Q(a.n * b.d - b.n * a.d, a.d * b.d);
const qmul = (a, b) => Q(a.n * b.n, a.d * b.d);
const qdiv = (a, b) => { if (b.n === 0n) throw new Error('division by zero'); return Q(a.n * b.d, a.d * b.n); };
const qneg = a => Q(-a.n, a.d);
const qabs = a => a.n < 0n ? qneg(a) : a;
const qeq = (a, b) => !!a && !!b && a.n === b.n && a.d === b.d;
const qlt = (a, b) => a.n * b.d < b.n * a.d;
const qnum = a => Number(a.n) / Number(a.d);
function qpow(a, k) {
  k = Number(k); if (!Number.isInteger(k) || Math.abs(k) > 60) throw new Error('too big');
  const K = BigInt(Math.abs(k)), n = a.n ** K, d = a.d ** K;
  if (k < 0 && n === 0n) throw new Error('division by zero');
  return k < 0 ? Q(d, n) : Q(n, d);
}
function qdec(s) {                                    /* "8.3", ".25", "−4.5", "3,080" → exact */
  s = String(s).replace(/,/g, '').replace(/−/g, '-').trim();
  const m = /^(-?)(\d*)(?:\.(\d*))?$/.exec(s); if (!m || (m[2] === '' && !m[3])) throw new Error('not a decimal: ' + s);
  const fr = m[3] || '', v = Q(BigInt((m[2] || '0') + fr), 10n ** BigInt(fr.length));
  return m[1] ? qneg(v) : v;
}
function places(q) { let d = q.d, t = 0, f = 0; while (d % 2n === 0n) { d /= 2n; t++; } while (d % 5n === 0n) { d /= 5n; f++; } return d === 1n ? Math.max(t, f) : -1; }
function decPlain(q) {                               /* a terminating decimal written out, no commas, "-" for minus */
  const neg = q.n < 0n, a = qabs(q), k = places(a); if (k < 0) throw new Error('not terminating');
  let s = (a.n * (10n ** BigInt(k)) / a.d).toString();
  if (k > 0) { s = s.padStart(k + 1, '0'); s = s.slice(0, s.length - k) + '.' + s.slice(s.length - k); }
  return (neg ? '-' : '') + s;
}
function commas(s) { const p = s.split('.'); p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ','); return p.join('.'); }
/* how a number is shown: a decimal with commas (−, not -), or a fraction a/b */
function numStr(q) { try { const s = decPlain(q); return (s[0] === '-' ? '−' + commas(s.slice(1)) : commas(s)); } catch (e) { return (q.n < 0n ? '−' : '') + qabs(q).n + '/' + q.d; } }
const N = x => numStr(typeof x === 'object' ? x : qdec(String(x)));        /* a number as printed, from a JS number or a rational */
const qv = x => typeof x === 'object' ? x : qdec(String(x));

/* ---- square roots, exactly: a whole radicand's integer root, and its root rounded to tenths (no floating point) */
function isqrt(m) { if (m < 0) throw new Error('negative'); let r = Math.floor(Math.sqrt(m)); while (r * r > m) r--; while ((r + 1) * (r + 1) <= m) r++; return r; }
const isSquare = m => isqrt(m) ** 2 === m;
function squareFree(m) { for (let k = 2; k * k <= m; k++) if (m % (k * k) === 0) return false; return true; }
/* round(√m) for a whole m that is not a perfect square: no ties are possible (√m is irrational) */
function roundSqrt(m) { const r = isqrt(m); return m > r * r + r ? r + 1 : r; }
/* √n to the nearest tenth, exactly: round(√(100n)) / 10 */
const sqrtTenth = n => Q(roundSqrt(100 * n), 10);
/* √n cut off after the tenths (a student who drops the digits instead of rounding) */
const sqrtCut = n => Q(isqrt(100 * n), 10);
/* A ± √n to the nearest tenth, A whole: since √n is irrational, round(A ± √n) = A ± round(√n) to the tenth */
const plusSqrtTenth = (A, n, sign) => Q(10 * A + (sign < 0 ? -1 : 1) * roundSqrt(100 * n), 10);

/* ------------------------------------------------------------------ showing math (html) */
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const minus = s => String(s).replace(/^-/, '−');
const sup = e => '<sup>' + minus(e) + '</sup>';
const sq = x => N(x) + sup(2);                                                       /* 7² */
function speakH(h) {                                                                  /* what a screen reader says for a piece of math */
  let t = String(h);
  for (let i = 0; i < 6; i++) { const t0 = t;
    t = t.replace(/<span class="rad[^"]*">(?:<span class="rg">)?√(?:<\/span>)?<span class="rc">((?:(?!<span class="rad)[\s\S])*?)<\/span><\/span>/, ' the square root of ($1) ');
    t = t.replace(/<span class="fr"><span class="nu">((?:(?!<span class="fr">)[\s\S])*?)<\/span><span class="de">((?:(?!<span class="fr">)[\s\S])*?)<\/span><\/span>/, ' ($1 over $2) ');
    if (t === t0) break; }
  t = t.replace(/<sup[^>]*>2<\/sup>/g, ' squared ').replace(/<sup[^>]*>(.*?)<\/sup>/g, ' to the $1 ').replace(/<[^>]+>/g, '').replace(/&nbsp;/g, ' ').replace(/&lt;/g, ' is less than ').replace(/&gt;/g, ' is greater than ');
  return t.replace(/≤/g, ' is less than or equal to ').replace(/≈/g, ' is about ').replace(/×|·/g, ' times ').replace(/÷/g, ' divided by ').replace(/−/g, ' minus ').replace(/\+/g, ' plus ').replace(/=/g, ' equals ').replace(/\s+/g, ' ').trim();
}
const M = h => '<span class="m" role="img" aria-label="' + esc(speakH(h)) + '">' + h + '</span>';
const fr = (n, d) => '<span class="fr"><span class="nu">' + n + '</span><span class="de">' + d + '</span></span>';
const sqrtH = h => '<span class="rad"><span class="rg">√</span><span class="rc">' + h + '</span></span>';
const X = '<i>x</i>';
const pt = (x, y) => '(' + minus(String(x)) + ', ' + minus(String(y)) + ')';         /* a point: (−6, 1) */
/* the exact length √n as printed: the radical when n has no square factor; otherwise no radical is printed at all */
const rootOK = n => squareFree(n) && !isSquare(n);
/* a scale factor, written "1.5" or "4/3", exactly; and as printed: a decimal when it ends, else a fraction — inside a math
   span (kIn) or in running text (kOut) */
const qk = s => { s = String(s); const m = /^(\d+)\/(\d+)$/.exec(s); return m ? Q(BigInt(m[1]), BigInt(m[2])) : qdec(s); };
const kIn = k => places(k) >= 0 ? numStr(k) : fr(String(k.n), String(k.d));
const kOut = k => places(k) >= 0 ? numStr(k) : M(fr(String(k.n), String(k.d)));

/* ------------------------------------------------------------------ reading what a student types */
/* returns {ok, val (exact, or null), f (its value as a number), form: 'num' | 'root' | 'expr', n (a lone root's radicand), text}
   or {ok: false, msg} or {ok: false, blank: true} */
const UNITW = ['square units?', 'units?', 'blocks?', 'centimeters?', 'cm', 'millimeters?', 'mm', 'meters?', 'm', 'kilometers?', 'km', 'inch(?:es)?', 'in\\.?',
  'feet', 'foot', 'ft\\.?', 'yards?', 'yd\\.?', 'miles?', 'mi', 'long', 'tall', 'high', 'shorter', 'away'];
const UNITRE = new RegExp('(\\d|\\))\\s*(?:(?:' + UNITW.join('|') + ')(?![a-z])\\s*)+$', 'i');
function tidy(text) {
  let t = String(text == null ? '' : text).trim();
  t = t.replace(/\.\s*$/, '').trim();                                              /* a sentence's full stop */
  t = t.replace(UNITRE, '$1').trim().replace(/\.\s*$/, '');
  t = t.replace(/^\s*(?:about|approximately|approx\.?|around|it is|it's|the answer is)\s+/i, '');
  t = t.replace(/^\s*(?:[a-z]{1,2}\s*)?[=≈~]\s*/i, '');                          /* "x = 21", "h ≈ 14.8", "≈ 9.2" */
  t = t.replace(/[−–—]/g, '-').replace(/[×✕✖·•⋅]/g, '*').replace(/÷/g, '/').replace(/\s+/g, ' ');
  t = t.replace(/²/g, '^2').replace(/sqrt/gi, '√').replace(/\bsq\.?\s*rt\b/gi, '√').replace(/\broot\b/gi, '√');
  return t.trim();
}
function tokenize(t) {
  const out = []; let i = 0;
  while (i < t.length) {
    const ch = t[i];
    if (ch === ' ') { i++; continue; }
    const m = /^(\d[\d,]*(?:\.\d*)?|\.\d+)/.exec(t.slice(i));
    if (m) {
      const raw = m[1];
      if (/,/.test(raw) && !/^\d{1,3}(,\d{3})+(\.\d*)?$/.test(raw)) return { err: 'comma' };
      out.push({ t: 'n', s: raw.replace(/,/g, '') }); i += m[0].length; continue;
    }
    if ('+-*/^()√'.indexOf(ch) >= 0) { out.push({ t: ch }); i++; continue; }
    return { err: 'char', ch };
  }
  return { toks: out };
}
function parse(text) {
  const tk = tokenize(text); if (tk.err) return tk;
  const T = tk.toks; let i = 0;
  const peek = () => T[i], eat = t => (T[i] && T[i].t === t ? T[i++] : null);
  function expr() { let a = term(); for (let g = 0; g < 200; g++) { if (eat('+')) a = { t: 'add', a, b: term() }; else if (eat('-')) a = { t: 'sub', a, b: term() }; else return a; } throw new Error('long'); }
  function term() { let a = unary();
    for (let g = 0; g < 200; g++) {
      if (eat('*')) a = { t: 'mul', a, b: unary() };
      else if (eat('/')) a = { t: 'div', a, b: unary() };
      else if (peek() && (peek().t === '(' || peek().t === '√') && a.t !== 'neg') a = { t: 'mul', a, b: unary(), imp: true };
      else return a; }
    throw new Error('long'); }
  function unary() { if (eat('-')) return { t: 'neg', a: unary() }; if (eat('+')) return unary(); return power(); }
  function power() { const b = atom(); if (eat('^')) return { t: 'pow', a: b, b: unary() }; return b; }
  function atom() {
    const x = peek(); if (!x) throw new Error('end');
    if (x.t === 'n') { i++; return { t: 'n', s: x.s }; }
    if (eat('√')) return { t: 'root', a: atom() };
    if (eat('(')) { const e = expr(); if (!eat(')')) throw new Error(')'); return { t: 'par', a: e }; }
    throw new Error('token');
  }
  try { const e = expr(); if (i !== T.length) return { err: 'left' }; return { ast: e }; } catch (e) { return { err: 'syntax' }; }
}
/* the value of a typed expression: exact where it can be ({q, f}), a number where a root is not whole (q null) */
function evalA(a) {
  const both = q => ({ q, f: qnum(q) });
  switch (a.t) {
    case 'n': return both(qdec(a.s));
    case 'par': return evalA(a.a);
    case 'neg': { const x = evalA(a.a); return { q: x.q && qneg(x.q), f: -x.f }; }
    case 'add': case 'sub': case 'mul': case 'div': {
      const x = evalA(a.a), y = evalA(a.b);
      const op = { add: [qadd, (u, v) => u + v], sub: [qsub, (u, v) => u - v], mul: [qmul, (u, v) => u * v], div: [qdiv, (u, v) => u / v] }[a.t];
      if (a.t === 'div' && y.f === 0) throw new Error('division by zero');
      return { q: x.q && y.q ? op[0](x.q, y.q) : null, f: op[1](x.f, y.f) }; }
    case 'pow': { const x = evalA(a.a), e = evalA(a.b);
      if (!e.q || e.q.d !== 1n || Math.abs(Number(e.q.n)) > 12) throw new Error('exponent');
      return { q: x.q ? qpow(x.q, e.q.n) : null, f: Math.pow(x.f, Number(e.q.n)) }; }
    case 'root': { const x = evalA(a.a); if (x.f < 0) throw new Error('negative');
      if (x.q && x.q.d === 1n && x.q.n <= 10n ** 12n && isSquare(Number(x.q.n))) return both(Q(isqrt(Number(x.q.n))));
      return { q: null, f: Math.sqrt(x.f) }; }
  }
  throw new Error('node');
}
const strip = a => a.t === 'par' ? strip(a.a) : a;
function isNumLit(a) { a = strip(a); if (a.t === 'n') return true; if (a.t === 'neg') return isNumLit(a.a); return a.t === 'div' && strip(a.a).t === 'n' && strip(a.b).t === 'n'; }
const UNREAD = 'I can’t read that. Type just your answer, like 12 or 7.5.';
function readAns(text) {
  const raw = String(text == null ? '' : text);
  if (!raw.trim()) return { ok: false, blank: true };
  if (raw.length > 60) return { ok: false, msg: 'That is too long to read. Type just your answer.' };
  const t = tidy(raw);
  if (!t) return { ok: false, msg: UNREAD };
  const mx = /^(-?)(\d+)\s+(\d+)\s*\/\s*(\d+)$/.exec(t);                          /* a mixed number, "22 1/2" */
  if (mx && mx[4] !== '0') { const v = qadd(Q(BigInt(mx[2])), Q(BigInt(mx[3]), BigInt(mx[4]))), val = mx[1] ? qneg(v) : v; return { ok: true, val, f: qnum(val), form: 'num', text: t }; }
  const p = parse(t);
  if (p.err === 'comma') return { ok: false, msg: 'Use a period for a decimal point, like 14.8.' };
  if (p.err) {
    if (/\d\s+\d/.test(t) && !/[*/^+()√-]/.test(t)) return { ok: false, msg: 'I see two numbers with a space between them. Type one number.' };
    return { ok: false, msg: UNREAD };
  }
  let v; try { v = evalA(p.ast); } catch (e) { return { ok: false, msg: 'I can’t work that out. Type just your answer.' }; }
  if (!isFinite(v.f)) return { ok: false, msg: UNREAD };
  const a = strip(p.ast);
  if (a.t === 'root' && strip(a.a).t === 'n' && /^\d+$/.test(strip(a.a).s)) return { ok: true, val: v.q, f: v.f, form: 'root', n: Number(strip(a.a).s), text: t };
  if (isNumLit(a)) return { ok: true, val: v.q, f: v.f, form: 'num', text: t };
  return { ok: true, val: v.q, f: v.f, form: 'expr', text: t };
}
/* a plain number (the Hint's number steps): "218", "14.8", "45/2" */
function readNum(text) {
  let t = String(text == null ? '' : text).trim();
  if (/^[-−]?\d+,\d{1,2}$/.test(t)) t = t.replace(',', '.');
  const r = readAns(t); return r.ok && r.form === 'num' && r.val ? r.val : null;
}

/* ------------------------------------------------------------------ the questions */
const UNIT_ID = 'a7u6';
const TITLES = ['Triangle Inequality and the Converse', 'The Pythagorean Theorem', 'Distance on the Coordinate Plane', 'Similar Triangles'];
const NAMES = ['Nia', 'Omar', 'Lucia', 'Ben', 'Sofia', 'Kai', 'Maya', 'Leo', 'Zoe', 'Andre', 'Isla', 'Mateo', 'Grace', 'Jalen', 'Ruby', 'Eli', 'Hana', 'Felix'];
/* [abbreviation, singular, plural] */
const UNITS = { cm: ['cm', 'centimeter', 'centimeters'], in: ['in', 'inch', 'inches'], m: ['m', 'meter', 'meters'], ft: ['ft', 'foot', 'feet'], yd: ['yd', 'yard', 'yards'] };
const SECT = (title, items) => ({ title, items });
const aUnit = u => (u === 'in' ? 'an ' : 'a ') + UNITS[u][1];                          /* "a meter", "an inch" */
const PL = u => UNITS[u][2];                                                          /* a length in the words: "9 inches", never "9 in" */
const ROUND = 'Round your answer to the nearest tenth.';                              /* the state's own sentence */
function numPart(label, fam, prm, stem, ans, extra) { return Object.assign({ label, fam, prm, stem, kind: 'num', ans, key: fam + JSON.stringify(prm) }, extra || {}); }

let CLEAN = null;
function setClean(fn) { CLEAN = fn; }
function D(slot, seed, build) { return KIT.draw(UNIT_ID, seed, slot, build, it => !CLEAN || CLEAN(it)); }

/* the right triangles a student meets in this unit */
const TRIPLE15 = [[3, 4, 5], [6, 8, 10], [5, 12, 13], [9, 12, 15]];                 /* the only whole hypotenuses with a radicand to 225 */
/* [hypotenuse, the leg given]: every right triangle whose missing leg is whole with a radicand to 225 (21 of them) */
const LEGWHOLE = [[5, 3], [5, 4], [10, 6], [10, 8], [13, 5], [13, 12], [15, 9], [15, 12], [17, 8], [17, 15], [20, 16], [25, 20], [25, 24], [26, 24],
  [37, 35], [39, 36], [41, 40], [50, 48], [61, 60], [85, 84], [113, 112]];
/* the converse tests a set by squaring it, so any right triangle will do: these, and each of 3-4-5 and 5-12-13 scaled */
const CONVERSE = [[3, 4, 5], [6, 8, 10], [9, 12, 15], [12, 16, 20], [15, 20, 25], [18, 24, 30], [5, 12, 13], [10, 24, 26], [15, 36, 39], [8, 15, 17], [16, 30, 34],
  [7, 24, 25], [14, 48, 50], [20, 21, 29], [12, 35, 37], [9, 40, 41], [28, 45, 53], [11, 60, 61], [33, 56, 65], [16, 63, 65]];
/* legs of a slanted segment on the grid with a whole length (the four triples to 15, either way round) */
const LEGS = [[3, 4], [4, 3], [6, 8], [8, 6], [5, 12], [12, 5], [9, 12], [12, 9]];
const isRight = s => { const t = s.slice().sort((a, b) => a - b); return t[0] * t[0] + t[1] * t[1] === t[2] * t[2]; };
const isTri = s => { const t = s.slice().sort((a, b) => a - b); return t[0] + t[1] > t[2]; };
const sorted = s => s.slice().sort((a, b) => a - b);
const setKey = s => sorted(s).join(',');

/* ---------- section 1: the Triangle Inequality and the converse */
function q1(seed) {
  return D('q1', seed, T => {
    const u = T.pick(['cm', 'in', 'm', 'ft']);
    const ok = T.until(() => { const c = T.ri(8, 20), a = T.ri(3, c - 2), b = c + T.ri(1, 3) - a; return [a, b, c]; }, s => s[0] < s[1] && s[1] < s[2]);
    const flat = T.until(() => { const c = T.ri(8, 20), a = T.ri(2, c - 2); return [a, c - a, c]; }, s => s[0] < s[1]);
    const first = T.until(() => { const L = T.ri(9, 20), s1 = T.ri(2, L - 4), s2 = T.ri(s1 + 1, L - 1); return [L, s1, s2]; }, s => s[1] + s[2] < s[0]);
    const lng = T.until(() => { const L = T.ri(9, 20), s1 = T.ri(2, L - 4), s2 = T.ri(s1 + 1, L - 1); return [s1, s2, L]; }, s => s[0] + s[1] < s[2]);
    const okOrder = T.pick([[0, 1, 2], [2, 0, 1], [0, 2, 1], [1, 2, 0], [2, 1, 0]]), shownOk = okOrder.map(i => ok[i]);
    const flatShown = T.r() < 0.5 ? flat : [flat[1], flat[0], flat[2]];
    const firstShown = T.r() < 0.5 ? first : [first[0], first[2], first[1]];
    const sets = [{ s: shownOk, tag: 'ok' }, { s: flatShown, tag: 'flat' }, { s: firstShown, tag: 'firstTwo' }, { s: lng, tag: 'longPlus' }];
    const order = T.shuffle([0, 1, 2, 3]), shown = order.map(i => sets[i]);
    return { type: 'mc', fam: 'triSet', prm: { u, sets: shown.map(x => x.s), tags: shown.map(x => x.tag) }, stem: 'Which set of side lengths can form a triangle?',
      opts: shown.map(x => x.s.map(v => v + ' ' + u).join(', ')), sets: shown.map(x => x.s), tags: shown.map(x => x.tag), correct: order.indexOf(0),
      key: 'triSet' + JSON.stringify(shown.map(x => x.s)) };
  });
}
function q2(seed) {
  return D('q2', seed, T => {
    const R = T.pick([1, 2, 2, 2, 3]);
    const trips = T.shuffle(CONVERSE.slice()).slice(0, R);
    /* one right set always lists its longest side first: the set a student who tests the last number misses */
    const rights = trips.map((t, i) => ({ s: i === 0 ? [t[2], ...T.shuffle([t[0], t[1]])] : T.shuffle(t.slice()), tag: 'right' }));
    const kinds = T.shuffle(['near', 'consec', 'remember', 'triOnly', 'flat']).slice(0, 5 - R);
    const pool = CONVERSE.filter(t => !trips.includes(t));
    const make = {
      near: () => { const t = T.pick(pool); return T.shuffle([t[0], t[1], t[2] + 1]); },
      consec: () => { const n = T.ri(4, 12); return [n, n + 1, n + 2]; },
      remember: () => { const t = T.pick(pool); const d = t[2] + T.ri(2, 4); return [t[0], t[1], d]; },
      triOnly: () => T.until(() => { const c = T.ri(6, 20), a = T.ri(3, c - 1), b = T.ri(a + 1, c); return T.shuffle([a, b, c]); }, s => new Set(s).size === 3 && isTri(s) && !isRight(s)),
      flat: () => { const a = T.ri(3, 12), b = T.ri(a + 1, 16); return [a, b, a + b]; }
    };
    const wrongs = kinds.map(k => ({ s: T.until(make[k], s => !isRight(s) && (k === 'flat' || isTri(s))), tag: k }));
    const all = rights.concat(wrongs), order = T.shuffle([0, 1, 2, 3, 4]), shown = order.map(i => all[i]);
    return { type: 'multi', fam: 'rightSel', prm: { sets: shown.map(x => x.s), tags: shown.map(x => x.tag) }, stem: 'Select ALL of the sets of side lengths that make a right triangle.',
      opts: shown.map(x => x.s.join(', ')), sets: shown.map(x => x.s), tags: shown.map(x => x.tag),
      correct: shown.map((x, i) => x.tag === 'right' ? i : -1).filter(i => i >= 0), key: 'rightSel' + JSON.stringify(shown.map(x => x.s)) };
  });
}
function q3(seed) {
  return D('q3', seed, T => {
    const a = T.ri(3, 14), b = T.ri(a + 2, 22), u = T.pick(['in', 'cm', 'ft', 'm']);
    const lo = b - a, hi = a + b, le = '&lt;', L = (x, r1, r2, y) => N(x) + ' ' + r1 + ' ' + X + ' ' + r2 + ' ' + N(y);
    const opts = [{ h: L(lo, le, le, hi), tag: 'ok' }, { h: L(a, le, le, b), tag: 'between' }, { h: L(lo, '≤', '≤', hi), tag: 'leq' }, { h: L(0, le, le, hi), tag: 'sumOnly' }];
    const order = T.shuffle([0, 1, 2, 3]);
    return { type: 'mc', fam: 'range', prm: { a, b, u }, stem: 'Two sides of a triangle are ' + a + ' ' + PL(u) + ' and ' + b + ' ' + PL(u) + ' long. Which inequality shows every possible length ' + X + ', in ' + UNITS[u][2] + ', of the third side?',
      opts: order.map(i => M(opts[i].h)), tags: order.map(i => opts[i].tag), correct: order.indexOf(0), key: 'range' + [a, b].join(',') + '|' + order.join('') };
  });
}

/* ---------- section 2: the Pythagorean Theorem */
function q4(seed) {
  return D('q4', seed, T => {
    const t = T.pick(TRIPLE15), sw = T.r() < 0.5, a = sw ? t[1] : t[0], b = sw ? t[0] : t[1], ua = T.pick(['in', 'cm', 'm', 'ft']);
    const [c2, g] = T.pick(LEGWHOLE), ub = T.pick(['m', 'ft', 'cm', 'in']), bb = isqrt(c2 * c2 - g * g);
    const pa = numPart('a', 'hypWhole', { a, b, u: ua }, 'Its legs are ' + a + ' ' + PL(ua) + ' and ' + b + ' ' + PL(ua) + '. How long is the hypotenuse?', Q(t[2]), { unit: ua, exact: t[2] });
    const pb = numPart('b', 'legWhole', { c: c2, a: g, u: ub }, 'Its hypotenuse is ' + N(c2) + ' ' + PL(ub) + ' and one leg is ' + N(g) + ' ' + PL(ub) + '. How long is the other leg?', Q(bb), { unit: ub, exact: bb });
    return { type: 'parts', stem: 'Find the missing side of each right triangle.', parts: [pa, pb] };
  });
}
function q5(seed) {
  return D('q5', seed, T => {
    const u = T.pick(['cm', 'in', 'm', 'ft']);
    const [a, b] = T.until(() => [T.ri(2, 14), T.ri(2, 14)], ([a, b]) => a * a + b * b <= 225 && !isSquare(a * a + b * b));
    const n = a * a + b * b;
    const part = numPart('', 'hypTenth', { a, b, u }, '', sqrtTenth(n), { unit: u, tenth: true, exact: Math.sqrt(n), rad: n });
    return { type: 'solo', stem: 'A right triangle has legs of ' + a + ' ' + PL(u) + ' and ' + b + ' ' + PL(u) + '. How long is the hypotenuse, in ' + PL(u) + '? ' + ROUND, part };
  });
}
function q6(seed) {
  return D('q6', seed, T => {
    /* legs not a sliver (the shorter at least 0.3 of the longer), and a known leg of 3 or more */
    const [a, c] = T.until(() => { const c = T.ri(5, 20); return [T.ri(3, c - 1), c]; }, ([a, c]) => { const x = Math.sqrt(c * c - a * a); return c * c - a * a <= 225 && Math.min(a, x) >= 0.3 * Math.max(a, x); });
    const x = Math.sqrt(c * c - a * a), xFirst = T.r() < 0.5, turn = T.pick([0, 90, 180, 270]), flip = T.r() < 0.5;
    const opts = [{ h: a + ' + ' + X + ' = ' + c, tag: 'sumSides' }, { h: sq(a) + ' + ' + sq(c) + ' = ' + X + sup(2), tag: 'hypLeg' },
      { h: sq(a) + ' + ' + X + sup(2) + ' = 2 · ' + c, tag: 'doubled' }, { h: sq(a) + ' + ' + X + sup(2) + ' = ' + sq(c), tag: 'ok' }];
    const order = T.shuffle([0, 1, 2, 3]);
    const fig = { kind: 'rtri', legs: xFirst ? [x, a] : [a, x], labs: xFirst ? ['x', String(a), String(c)] : [String(a), 'x', String(c)], vals: xFirst ? [null, a, c] : [a, null, c], turn, flip };
    return { type: 'mc', fam: 'eqChoice', prm: { a, c, xFirst, turn, flip }, stem: 'Which equation can be used to find ' + X + '?', fig,
      opts: order.map(i => M(opts[i].h)), tags: order.map(i => opts[i].tag), correct: order.indexOf(3), key: 'eqChoice' + [a, c, xFirst, turn, flip].join(',') + '|' + order.join('') };
  });
}
/* places a path can cross at the sizes a radicand to 225 allows (a side of 14 at most), each in a unit it is measured in and no
   smaller than such a place is: [unit, its shorter side at least]. A field or a parking lot is far bigger than 14 m, so neither
   is here; a garden can be a 2 m strip along a fence. */
const PLACES = { garden: [['m', 2], ['ft', 5], ['yd', 3]], lawn: [['m', 4], ['yd', 4]], patio: [['ft', 8], ['m', 3]], playground: [['m', 6], ['yd', 6]], courtyard: [['m', 5], ['yd', 5]] };
function q7(seed) {
  return D('q7', seed, T => {
    const place = T.pick(Object.keys(PLACES)), [u, lo] = T.pick(PLACES[place]);
    /* w the shorter side, the longer no more than five times it; the words give the two sides in either order ("9 by 13") */
    const [w, l] = T.until(() => [T.ri(lo, 13), T.ri(lo + 1, 14)], ([w, l]) => w < l && l <= 5 * w && w * w + l * l <= 225 && !isSquare(w * w + l * l));
    const n = w * w + l * l, prm = { w, l, u, place }, [s1, s2] = T.r() < 0.5 ? [w, l] : [l, w];
    const pa = numPart('a', 'diag', prm, 'How long is the path, in ' + PL(u) + '? ' + ROUND, sqrtTenth(n), { unit: u, tenth: true, exact: Math.sqrt(n), rad: n });
    const pb = numPart('b', 'shorter', prm, 'How much shorter is the path than walking along two sides of the ' + place + '? ' + ROUND, plusSqrtTenth(w + l, n, -1), { unit: u, tenth: true, exact: w + l - Math.sqrt(n) });
    return { type: 'parts', stem: 'A rectangular ' + place + ' measures ' + s1 + ' ' + PL(u) + ' by ' + s2 + ' ' + PL(u) + '. A path runs straight across it from one corner to the opposite corner.', parts: [pa, pb] };
  });
}

/* ---------- section 3: distance on the coordinate plane */
const PAIRS = [['A', 'B'], ['P', 'Q'], ['M', 'N'], ['R', 'S'], ['C', 'D'], ['E', 'F']];
const crosses = (u, v) => (u < 0 && v > 0) || (u > 0 && v < 0);
/* two points whose legs are dx and dy, inside −10…10, the segment crossing at least one axis */
function twoPoints(T, dx, dy, lim) {
  lim = lim || 10;
  return T.until(() => { const x1 = T.ri(-lim, lim - dx), y1 = T.ri(-lim, lim), sy = T.r() < 0.5 ? 1 : -1; return [x1, y1, x1 + dx, y1 + sy * dy]; },
    ([x1, y1, x2, y2]) => Math.abs(y2) <= lim && (crosses(x1, x2) || crosses(y1, y2)) && x1 !== 0 && y1 !== 0 && x2 !== 0 && y2 !== 0);
}
function q8(seed) {
  return D('q8', seed, T => {
    const [dx, dy] = T.pick(LEGS), [x1, y1, x2, y2] = twoPoints(T, dx, dy, 9), sw = T.r() < 0.5, nm = T.pick(PAIRS);
    const P = sw ? [x2, y2, x1, y1] : [x1, y1, x2, y2];
    const prm = { x1: P[0], y1: P[1], x2: P[2], y2: P[3], names: nm };
    const part = numPart('', 'gridWhole', prm, '', Q(isqrt(dx * dx + dy * dy)), { unit: 'units', exact: isqrt(dx * dx + dy * dy) });
    return { type: 'solo', stem: 'Find the distance between points ' + nm[0] + ' and ' + nm[1] + '.', part,
      fig: { kind: 'grid2', pts: [[P[0], P[1], nm[0]], [P[2], P[3], nm[1]]] } };
  });
}
function q9(seed) {
  return D('q9', seed, T => {
    const [dx, dy] = T.until(() => [T.ri(1, 14), T.ri(1, 14)], ([a, b]) => a * a + b * b <= 225 && !isSquare(a * a + b * b) && a + b >= 4);
    const [x1, y1, x2, y2] = twoPoints(T, dx, dy, 10), sw = T.r() < 0.5;
    const P = sw ? [x2, y2, x1, y1] : [x1, y1, x2, y2], n = dx * dx + dy * dy;
    const prm = { x1: P[0], y1: P[1], x2: P[2], y2: P[3] };
    const part = numPart('', 'coordTenth', prm, '', sqrtTenth(n), { unit: 'units', tenth: true, exact: Math.sqrt(n), rad: n });
    return { type: 'solo', stem: 'Find the distance between ' + pt(P[0], P[1]) + ' and ' + pt(P[2], P[3]) + '. ' + ROUND, part };
  });
}
const TRINAMES = [['J', 'K', 'L'], ['A', 'B', 'C'], ['P', 'Q', 'R'], ['D', 'E', 'F'], ['R', 'S', 'T'], ['X', 'Y', 'Z']];
function q10(seed) {
  return D('q10', seed, T => {
    /* the first two corners make the side that crosses an axis; the right angle is at the second; the third is off it */
    const horiz = T.r() < 0.6, nm = T.pick(TRINAMES);
    const [s, h] = T.until(() => [T.ri(4, 14), T.ri(2, 9)], ([s, h]) => s * s + h * h <= 225 && !isSquare(s * s + h * h) && s !== h);
    /* the crossing side from a < 0 to b = a + s > 0; the other side from base to far, both on one side of the other axis */
    const g = T.until(() => { const a = -T.ri(1, s - 1), off = T.r() < 0.5 ? 1 : -1, base = off * T.ri(1, Math.min(6, 10 - h)), far = base + off * h; return { a, b: a + s, base, far }; },
      g => Math.abs(g.far) <= 10 && g.b <= 10 && g.a >= -10);
    const flipEnd = T.r() < 0.5;   /* the right angle at the crossing side's other end: then the first corner is the far one */
    let J, K, L;
    if (horiz) { J = [flipEnd ? g.b : g.a, g.base]; K = [flipEnd ? g.a : g.b, g.base]; L = [K[0], g.far]; }
    else { J = [g.base, flipEnd ? g.b : g.a]; K = [g.base, flipEnd ? g.a : g.b]; L = [g.far, K[1]]; }
    const n = s * s + h * h, prm = { J, K, L, names: nm };
    const pa = numPart('a', 'crossSide', prm, 'Find the length of side ' + nm[0] + nm[1] + '.', Q(s), { unit: 'units', exact: s });
    const pb = numPart('b', 'perim', prm, 'Find the perimeter of triangle ' + nm.join('') + '. ' + ROUND, plusSqrtTenth(s + h, n, 1), { unit: 'units', tenth: true, exact: s + h + Math.sqrt(n) });
    return { type: 'parts', stem: 'Triangle ' + nm.join('') + ' has corners ' + nm[0] + pt(J[0], J[1]) + ', ' + nm[1] + pt(K[0], K[1]) + ' and ' + nm[2] + pt(L[0], L[1]) + '.',
      parts: [pa, pb], fig: { kind: 'gridTri', pts: [[J[0], J[1], nm[0]], [K[0], K[1], nm[1]], [L[0], L[1], nm[2]]] } };
  });
}
const SPOTS = [['library', 'pool'], ['school', 'park'], ['museum', 'zoo'], ['bakery', 'bank'], ['station', 'stadium'], ['library', 'skate park'], ['school', 'store']];
function q11(seed) {
  return D('q11', seed, T => {
    const [dx, dy] = T.pick(LEGS), [x1, y1, x2, y2] = twoPoints(T, dx, dy, 10), sw = T.r() < 0.5, sp = T.pick(SPOTS);
    const P = sw ? [x2, y2, x1, y1] : [x1, y1, x2, y2], prm = { x1: P[0], y1: P[1], x2: P[2], y2: P[3], spots: sp };
    const pa = numPart('a', 'streets', prm, 'How far is it from the ' + sp[0] + ' to the ' + sp[1] + ' along the streets?', Q(dx + dy), { unit: 'blocks', exact: dx + dy });
    const pb = numPart('b', 'straight', prm, 'How far is it in a straight line?', Q(isqrt(dx * dx + dy * dy)), { unit: 'blocks', exact: isqrt(dx * dx + dy * dy) });
    return { type: 'parts', stem: 'On a town map, each unit is one block. The ' + sp[0] + ' is at ' + pt(P[0], P[1]) + ' and the ' + sp[1] + ' is at ' + pt(P[2], P[3]) + '.', parts: [pa, pb] };
  });
}

/* ---------- section 4: similar triangles */
/* scale factors: decimals (the test's 1.5), and fractions (the test's 4/3), whose triangles have sides that are multiples of the
   denominator, so every side of the copy is whole */
const KS = ['1.5', '2', '2.5', '3', '0.5', '4', '1.5', '2', '4/3', '2/3', '5/3', '3/4', '5/4'];
const okTri = s => { const t = sorted(s); return t[0] + t[1] >= t[2] + 2 && new Set(t).size === 3; };
/* a triangle to draw: not too flat — its height over the longest side at least 0.3 of that side (8-10-14 is 0.40; 6-15-18, 0.26, is refused) */
const roundTri = s => { const [a, b, c] = sorted(s), p = (a + b + c) / 2, area = Math.sqrt(p * (p - a) * (p - b) * (p - c)); return okTri(s) && 2 * area / c >= 0.3 * c; };
function sidesFor(T, ks, plain, ok) {
  const k = qk(ks), m = ks.indexOf('/') > 0 ? Number(k.d) : 1;
  return m === 1 ? T.until(plain, ok) : T.until(() => [m * T.ri(1, 6), m * T.ri(1, 6), m * T.ri(1, 6)], s => ok(s) && Math.max(...s) <= 20);
}
/* sides a, b, c with b/a = c/b: two of a copy's sides could then be matched two ways, each with its own k */
const oneRatio = s => { const [a, b, c] = sorted(s); return b * b === a * c; };
function q12(seed) {
  return D('q12', seed, T => {
    const ks = T.pick(KS), k = qk(ks), tri = sidesFor(T, ks, () => [T.ri(3, 10), T.ri(4, 13), T.ri(5, 16)], s => roundTri(s) && !oneRatio(s)), [p, q, r] = sorted(tri);
    const cp = qmul(Q(p), k), cq = qmul(Q(q), k), cr = qmul(Q(r), k);
    const which = T.pick(['r', 'r', 'p', 'q']), turn = T.pick(['180', 'flip']);
    const copy = { p: cp, q: cq, r: cr }, ans = copy[which];
    const prm = { p, q, r, k: ks, which, turn };
    const part = numPart('', 'simSide', prm, '', ans, { exact: qnum(ans) });
    /* the original: p up the left, q up the right, r along the bottom; the copy turned so that no side sits where its match does */
    const fig = { kind: 'simPair', a: [p, q, r], b: [qnum(cp), qnum(cq), qnum(cr)], la: [String(p), String(q), String(r)],
      lb: ['p', 'q', 'r'].map(s => s === which ? 'x' : N(copy[s])), turn };
    return { type: 'solo', stem: 'The two triangles are similar. Find ' + X + '.', part, fig };
  });
}
const SUNLIT = [['girl', 'tree'], ['boy', 'flagpole'], ['man', 'building'], ['woman', 'light pole'], ['student', 'tree'], ['girl', 'statue']];
/* a grown-up 5 to 6 ft tall; a girl, a boy or a student 4 to 5.5 ft */
const HEIGHTS = { man: ['5.5', '6'], woman: ['5', '5.5', '6'], girl: ['4', '4.5', '5', '5.5'], boy: ['4', '4.5', '5', '5.5'], student: ['4.5', '5', '5.5'] };
function q13(seed) {
  return D('q13', seed, T => {
    if (T.r() < 0.6) {
      const [who, what] = T.pick(SUNLIT), h1 = T.pick(HEIGHTS[who]), s1 = T.pick(['2', '2.5', '3', '4', '5', '6', '8']), k = T.ri(3, 12);
      const S2 = qmul(qdec(s1), Q(k)), H2 = qmul(qdec(h1), Q(k));
      const prm = { mode: 'shadow', who, what, h1, s1, s2: decPlain(S2) };
      return { type: 'solo', stem: 'A ' + who + ' ' + N(h1) + ' ft tall casts a shadow ' + N(s1) + ' ft long. At the same moment, a ' + what + ' casts a shadow ' + numStr(S2) + ' ft long. How tall is the ' + what + '?',
        part: numPart('', 'shadow', prm, '', H2, { unit: 'ft', exact: qnum(H2) }), fig: { kind: 'shadow', h1: +h1, s1: +s1, s2: qnum(S2), h2: qnum(H2), lab: [N(h1) + ' ft', N(s1) + ' ft', numStr(S2) + ' ft', 'h'], what: [who, what] } };
    }
    const name = T.pick(NAMES), what = T.pick(['tree', 'flagpole', 'pole', 'building']), h1 = T.pick(['4', '4.5', '5', '5.5', '6']), d1 = T.pick(['2', '2.5', '3', '4', '5']), k = T.ri(3, 10);
    const D2 = qmul(qdec(d1), Q(k)), H2 = qmul(qdec(h1), Q(k));
    const prm = { mode: 'mirror', name, what, h1, d1, d2: decPlain(D2) };
    return { type: 'solo', stem: name + '’s eyes are ' + N(h1) + ' ft above the ground. Standing ' + N(d1) + ' ft from a mirror on the ground, ' + name + ' sees in it the top of a ' + what + ' that stands ' + numStr(D2) + ' ft beyond the mirror. The two right triangles are similar. How tall is the ' + what + '?',
      part: numPart('', 'mirror', prm, '', H2, { unit: 'ft', exact: qnum(H2) }), fig: { kind: 'mirror', h1: +h1, d1: +d1, d2: qnum(D2), h2: qnum(H2), lab: [N(h1) + ' ft', N(d1) + ' ft', numStr(D2) + ' ft', 'h'], what: [name, what] } };
  });
}
function q14(seed) {
  return D('q14', seed, T => {
    const ks = T.pick(['2', '3', '1.5', '2.5', '0.5', '4/3', '2/3', '5/3', '3/4', '2', '1.5']), k = qk(ks), K = qnum(k);
    const t = sorted(sidesFor(T, ks, () => [T.ri(3, 9), T.ri(4, 11), T.ri(5, 12)], okTri));
    const sc = s => s.map(v => qmul(Q(v), k)), okS = sc(t);
    const d = qsub(okS[0], Q(t[0]));                                                   /* adding d makes the first side match the right choice */
    const add = t.map(v => qadd(Q(v), d));
    const e = T.pick([1, 2, -1]), two = [okS[0], okS[1], qadd(okS[2], Q(e))];
    const f = T.pick([1, 2, 3, -1]), kept = [Q(t[0]), Q(t[1]), Q(t[2] + f)];
    const sim = s => { const r = qdiv(s[0], Q(t[0])); return qeq(qdiv(s[1], Q(t[1])), r) && qeq(qdiv(s[2], Q(t[2])), r); };
    const sets = [{ s: okS, tag: 'ok' }, { s: add, tag: 'add' }, { s: two, tag: 'twoRatios' }, { s: kept, tag: 'keptTwo' }];
    if (sets.some(x => x.s.some(v => !qlt(Q(0), v)) || !isTri(x.s.map(qnum)))) return { bad: true };
    if (sets.filter(x => sim(x.s)).length !== 1 || K === 1) return { bad: true };
    if (sets.some(x => !(qlt(x.s[0], x.s[1]) && qlt(x.s[1], x.s[2])))) return { bad: true };       /* "3, 4.5, 4": out of order */
    const order = T.shuffle([0, 1, 2, 3]), shown = order.map(i => sets[i]);
    return { type: 'mc', fam: 'simChoice', prm: { t, k: ks, e, f }, stem: 'Which triangle is similar to a triangle with sides ' + t[0] + ', ' + t[1] + ' and ' + t[2] + '?',
      opts: shown.map(x => x.s.map(numStr).join(', ')), tags: shown.map(x => x.tag), sides: shown.map(x => x.s), correct: order.indexOf(0),
      key: 'simChoice' + JSON.stringify([t, ks, e, f]) + '|' + order.join('') };
  });
}

function generate(seed) {
  if (!CLEAN) throw new Error('coach.js must be loaded before generating');
  return { seed, sections: [
    SECT(TITLES[0], [q1(seed), q2(seed), q3(seed)]),
    SECT(TITLES[1], [q4(seed), q5(seed), q6(seed), q7(seed)]),
    SECT(TITLES[2], [q8(seed), q9(seed), q10(seed), q11(seed)]),
    SECT(TITLES[3], [q12(seed), q13(seed), q14(seed)])] };
}
function partsOf(it) { return it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : [it]; }
/* the key as shown beside a typed part: the number and its unit */
function ansHtml(p) { return M(numStr(p.ans)) + (p.unit ? ' ' + esc(p.unit) : ''); }

const api = { UNIT_ID, TITLES, NAMES, UNITS, Q, qadd, qsub, qmul, qdiv, qneg, qabs, qeq, qlt, qnum, qpow, qdec, qv, places, decPlain, numStr, N, commas,
  isqrt, isSquare, squareFree, roundSqrt, sqrtTenth, sqrtCut, plusSqrtTenth, rootOK, qk, kIn, kOut, esc, M, speakH, fr, sqrtH, sup, sq, minus, pt, X,
  tidy, parse, evalA, readAns, readNum, setClean, generate, partsOf, ansHtml, isRight, isTri, sorted, setKey, crosses, TRIPLE15, LEGWHOLE, CONVERSE, LEGS };
if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.Practice = api;
})(this);
