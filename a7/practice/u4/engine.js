/* A7 Unit 4 practice (Solving Problems with Rational Numbers): exact numbers, reading what a student types, drawing the
   numbers, and the questions. Same kinds, order and points as the Unit 4 test (a7/build/u4/unit.py), new numbers every set;
   never a question from the test. The two transfer items (Q6, Q15) are replaced by same-skill questions the unit taught
   (Croix, 16 Oct 2026: "Same-skill stand-ins"). 21 Oct 2026: no significant digits anywhere (Croix: "anything asking how many
   significant digits should be removed") — Part 2 is the test's four real-world problems, answered exactly. */
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
const qcmp = (a, b) => qlt(a, b) ? -1 : qeq(a, b) ? 0 : 1;
const qnum = a => Number(a.n) / Number(a.d);
const bitLen = x => (x < 0n ? -x : x).toString(2).length;
function qpow(a, k) {                       /* guarded: "((10^400)^400)^400" must answer "too big" at once, never freeze the tab (review 4) */
  k = Number(k); if (!Number.isInteger(k) || Math.abs(k) > 400) throw new Error('too big');
  if ((bitLen(a.n) + bitLen(a.d)) * Math.abs(k) > 20000) throw new Error('too big');
  const K = BigInt(Math.abs(k)), n = a.n ** K, d = a.d ** K;
  if (k < 0 && n === 0n) throw new Error('division by zero');
  return k < 0 ? Q(d, n) : Q(n, d);
}
const p10 = k => qpow(Q(10), k);
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
function expOf(q) {                                   /* the power of ten of the leading digit */
  const a = qabs(q); if (a.n === 0n) return 0;
  let k = a.n.toString().length - a.d.toString().length;
  if (qlt(a, p10(k))) k--; if (!qlt(a, p10(k + 1))) k++;
  return k;
}
/* {c: "5.7", k: 2}: as few digits as the value needs (n = a number of digits to show, trailing zeros kept) */
function sciOf(q, n) {
  const k = expOf(q), c = qdiv(q, p10(k));
  let s = decPlain(c);
  if (n) { const want = n - 1, have = s.indexOf('.') < 0 ? 0 : s.length - s.indexOf('.') - 1;
    if (have > want) throw new Error('more digits than ' + n + ': ' + s);
    if (want > 0) s = (s.indexOf('.') < 0 ? s + '.' : s) + '0'.repeat(want - have); }
  return { c: s, k };
}
const digitsOf = c => String(c).replace(/[^0-9]/g, '').replace(/^0+/, '').length;   /* how many digits a coefficient 1 ≤ c < 10 shows */

/* ------------------------------------------------------------------ showing math (html) */
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const minus = s => String(s).replace(/^-/, '−');
const sup = e => '<sup>' + minus(e) + '</sup>';
/* what a screen reader says for a piece of math (review 1, A2): "2 over 3", "the square root of 49", "10 to the 5" */
function speakH(h) {
  let t = String(h);
  for (let i = 0; i < 8; i++) { const t0 = t;
    t = t.replace(/<span class="fr"><span class="nu">((?:(?!<span class="fr">)[\s\S])*?)<\/span><span class="de">((?:(?!<span class="fr">)[\s\S])*?)<\/span><\/span>/, ' ($1 over $2) ');
    t = t.replace(/<span class="rad[^"]*"><sup class="ri">3<\/sup>(?:<span class="rg">)?√(?:<\/span>)?<span class="rc">((?:(?!<span class="rad)[\s\S])*?)<\/span><\/span>/, ' the cube root of ($1) ');
    t = t.replace(/<span class="rad[^"]*">(?:<span class="rg">)?√(?:<\/span>)?<span class="rc">((?:(?!<span class="rad)[\s\S])*?)<\/span><\/span>/, ' the square root of ($1) ');
    if (t === t0) break; }
  t = t.replace(/<sup[^>]*>(.*?)<\/sup>/g, ' to the $1 ').replace(/<[^>]+>/g, '').replace(/&nbsp;/g, ' ');
  return t.replace(/×|·/g, ' times ').replace(/÷/g, ' divided by ').replace(/−/g, ' minus ').replace(/\+/g, ' plus ').replace(/=/g, ' equals ').replace(/\s+/g, ' ').trim();
}
const M = h => '<span class="m" role="img" aria-label="' + esc(speakH(h)) + '">' + h + '</span>';
const fr = (n, d) => '<span class="fr"><span class="nu">' + n + '</span><span class="de">' + d + '</span></span>';
function qH(q) { if (q.d === 1n || places(q) >= 0) return numStr(q); return (q.n < 0n ? '−' : '') + fr(String(qabs(q).n), String(q.d)); }
function qF(q) { if (q.d === 1n) return numStr(q); return (q.n < 0n ? '−' : '') + fr(String(qabs(q).n), String(q.d)); }   /* a fraction, never a long decimal */
function sciH(c, k) { return '<span class="nw">' + minus(commas(String(c))) + ' × 10' + sup(k) + '</span>'; }   /* [D-1] one number never breaks across lines */          /* 5.7 × 10⁵ (html) */
function sciSay(c, k) { return minus(String(c)) + ' times 10 to the ' + minus(String(k)); }
function sciM(c, k) { return '<span class="m" role="img" aria-label="' + esc(sciSay(c, k)) + '">' + sciH(c, k) + '</span>'; }
const sqrtH = h => '<span class="rad' + (/class="fr"/.test(h) ? ' tall' : '') + '"><span class="rg">√</span><span class="rc">' + h + '</span></span>';   /* tall: a root over a fraction (review 1, A3) */
const cbrtH = h => '<span class="rad"><sup class="ri">3</sup><span class="rg">√</span><span class="rc">' + h + '</span></span>';
const par = h => '(' + h + ')';
/* the value as a typed-answer key, in the form the question wants */
function ansHtml(p) {
  if (p.kind === 'sci') return M(sciH(p.want.c, p.want.k)) + (p.unitWord ? ' ' + esc(p.unitWord) : '');
  if (p.kind === 'money') return numStr(p.ans).replace(/^(\d[\d,]*)\.(\d)$/, '$1.$20') + ' dollars';
  if (p.kind === 'expr') return M(p.keyExpr);
  return M(qF(p.ans));
}

/* ------------------------------------------------------------------ reading what a student types */
/* returns {ok, val, form: 'sci'|'notfin'|'num'|'expr'|'enote', c, k, digits, expr, text} or {ok: false, msg} */
const SUP = { '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁻': '-' };
const UNITW = ['square', 'sq\\.?', 'cubic', 'millimeters?', 'centimeters?', 'meters?', 'kilometers?', 'mm', 'cm', 'km', 'm', 'grams?', 'kilograms?', 'g', 'kg', 'mg',
  'liters?', 'milliliters?', 'l', 'ml', 'seconds?', 'secs?', 's', 'hours?', 'hrs?', 'h', 'km ?/ ?h(?:r|our)?', 'km per hour', 'kph', 'mph', 'm/s', 'feet', 'foot', 'ft', 'inches', 'in\\.?',
  'dollars?', 'usd', '\\$', 'photons', 'drops( of water)?', 'requests', 'beads'];
const UNITRE = new RegExp('(\\d|\\))\\s*(?:(?:' + UNITW.join('|') + ')(?![a-z])(?:²|³|\\^ ?2|\\^ ?3|2)?\\.?\\s*)+$', 'i');   /* (?![a-z]): "mmmm…" can't backtrack for hours (review 4) */
function tidy(text) {
  let t = String(text == null ? '' : text).trim();
  /* a unit or words after the number ("mm²", "km/h", "square millimeters", "dollars", "photons"): only these words, so a
     stray letter is never quietly dropped */
  t = t.replace(/\.\s*$/, '').trim();                                          /* a sentence's full stop: "8.3 x 10^6." */
  t = t.replace(UNITRE, '$1').trim().replace(/\.\s*$/, '');
  t = t.replace(/\$\s*(?=[\d.])/g, '').replace(/^\s*(?:[a-z][a-z ]{0,20})?\s*[=≈~]\s*/i, '');
  t = t.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+/g, m => '^(' + m.split('').map(c => SUP[c]).join('') + ')');
  t = t.replace(/[−–—]/g, '-').replace(/[×✕✖·•⋅]/g, '*').replace(/÷/g, '/').replace(/\s+/g, ' ');
  t = t.replace(/^\$\s*/, '').replace(/^(-)\s*\$\s*/, '$1');
  t = t.replace(/(\d)\s*[xX]\s*(?=[\d(.-])/g, '$1*').replace(/\)\s*[xX]\s*(?=[\d(.-])/g, ')*');   /* x as times */
  return t.trim();
}
function tokenize(t) {
  const out = []; let i = 0;
  while (i < t.length) {
    const ch = t[i];
    if (ch === ' ') { i++; continue; }
    const m = /^(\d[\d,]*(?:\.\d*)?|\.\d+)(?:[eE]([+-]?\d+))?/.exec(t.slice(i));
    if (m) {
      const raw = m[1];
      if (/,/.test(raw) && !/^\d{1,3}(,\d{3})+(\.\d*)?$/.test(raw)) return { err: 'comma' };
      out.push({ t: 'n', s: raw.replace(/,/g, ''), e: m[2] != null ? m[2] : null }); i += m[0].length; continue;
    }
    if ('+-*/^()'.indexOf(ch) >= 0) { out.push({ t: ch }); i++; continue; }
    return { err: 'char', ch };
  }
  return { toks: out };
}
function parse(text) {
  const tk = tokenize(text); if (tk.err) return tk;
  const T = tk.toks; let i = 0;
  const peek = () => T[i], eat = t => (T[i] && T[i].t === t ? T[i++] : null);
  function expr() { let a = term(); for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); if (eat('+')) a = { t: 'add', a, b: term() }; else if (eat('-')) a = { t: 'sub', a, b: term() }; else return a; } }
  function term() {
    let a = unary();
    for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers');
      if (eat('*')) a = { t: 'mul', a, b: unary() };
      else if (eat('/')) a = { t: 'div', a, b: unary() };
      else if (peek() && (peek().t === '(' || (peek().t === 'n' && (a.t === 'par' || a.t === 'pow' && a.a.t === 'par')))) a = { t: 'mul', a, b: unary(), imp: true };
      else return a;
    }
  }
  function unary() { if (eat('-')) return { t: 'neg', a: unary() }; if (eat('+')) return unary(); return power(); }
  function power() { const b = atom(); if (eat('^')) return { t: 'pow', a: b, b: unary() }; return b; }
  function atom() {
    const x = peek(); if (!x) throw new Error('end');
    if (x.t === 'n') { i++; return x.e != null ? { t: 'enote', s: x.s, e: x.e } : { t: 'n', s: x.s }; }
    if (eat('(')) { const e = expr(); if (!eat(')')) throw new Error(')'); return { t: 'par', a: e }; }
    throw new Error('token');
  }
  try { const e = expr(); if (i !== T.length) return { err: 'left' }; return { ast: e }; } catch (e) { return { err: 'syntax' }; }
}
function evalA(a) {
  switch (a.t) {
    case 'n': return qdec(a.s);
    case 'enote': return qmul(qdec(a.s), p10(Number(a.e)));
    case 'par': return evalA(a.a);
    case 'neg': return qneg(evalA(a.a));
    case 'add': return qadd(evalA(a.a), evalA(a.b));
    case 'sub': return qsub(evalA(a.a), evalA(a.b));
    case 'mul': return qmul(evalA(a.a), evalA(a.b));
    case 'div': return qdiv(evalA(a.a), evalA(a.b));
    case 'pow': { const e = evalA(a.b); if (e.d !== 1n) throw new Error('fractional exponent'); return qpow(evalA(a.a), e.n); }
  }
  throw new Error('node');
}
const strip = a => a.t === 'par' ? strip(a.a) : a;
function intLit(a) { a = strip(a); if (a.t === 'n' && /^\d+$/.test(a.s)) return Number(a.s); if (a.t === 'neg') { const v = intLit(a.a); return v == null ? null : -v; } return null; }
function numLit(a) { a = strip(a); if (a.t === 'n') return a.s; if (a.t === 'neg' && strip(a.a).t === 'n') return '-' + strip(a.a).s; return null; }
/* c × 10^k as typed: the coefficient exactly as written (so "7.0" keeps its zero) */
function sciShape(a) {
  a = strip(a);
  const tenPow = x => { x = strip(x); if (x.t === 'pow' && strip(x.a).t === 'n' && strip(x.a).s === '10') { const k = intLit(x.b); return k == null ? null : k; } return null; };
  if (a.t === 'mul' && (!a.imp || strip(a.b) !== a.b)) { const c = numLit(a.a), k = tenPow(a.b); if (c != null && k != null) return { c, k }; }   /* 8.3(10^6) too (review 1, M2) */
  if (a.t === 'neg') { const s = sciShape(a.a); if (s) return { c: '-' + s.c, k: s.k }; }
  const k = tenPow(a); if (k != null) return { c: '1', k };
  return null;
}
function isFracLit(a) {                                 /* "-19/4", "−(19/4)", "7/9": a number written as a fraction */
  a = strip(a); if (a.t === 'neg') return isFracLit(a.a);
  if (a.t !== 'div') return false;
  let n = strip(a.a); if (n.t === 'neg') n = strip(n.a);
  const d = strip(a.b); return n.t === 'n' && /^\d+$/.test(n.s) && d.t === 'n' && /^\d+$/.test(d.s);
}
function hasOp(a) { a = strip(a); return !(a.t === 'n' || (a.t === 'neg' && strip(a.a).t === 'n')); }
const UNREAD = 'I can’t read that. Type just your answer, like 7.2 x 10^6.';
function readAns(text) {
  const raw = String(text == null ? '' : text);
  if (!raw.trim()) return { ok: false, blank: true };
  if (raw.length > 80) return { ok: false, msg: 'That is too long to read. Type just your answer.' };
  const t = tidy(raw);
  if (!t) return { ok: false, msg: UNREAD };
  const mx = /^(-?)(\d+)\s+(\d+)\s*\/\s*(\d+)$/.exec(t);                          /* a mixed number, "-4 3/4" */
  if (mx && mx[4] !== '0') { const v = qadd(Q(BigInt(mx[2])), Q(BigInt(mx[3]), BigInt(mx[4]))); return { ok: true, val: mx[1] ? qneg(v) : v, form: 'num', text: t }; }
  if (/(?:\*|x)\s*10\s*[-−]\s*\d+\s*$/i.test(t) || /(?:\*)\s*10\s+\d+\s*$/.test(t)) return { ok: false, msg: 'Put ^ before the exponent, like 10^-4 or 10^6.', caret: true };
  const p = parse(t);
  if (p.err === 'comma') return { ok: false, msg: 'Use a period for a decimal point, like 4.5.' };
  if (p.err) {
    if (/\d\s+\d/.test(t) && !/[*/^+()-]/.test(t)) return { ok: false, msg: 'I see two numbers with a space between them. Type one number, or use x for times, like 7.2 x 10^6.' };
    return { ok: false, msg: UNREAD };
  }
  let val; try { val = evalA(p.ast); } catch (e) { return { ok: false, msg: 'I can’t work that out. Type just your answer.' }; }
  const a = strip(p.ast);
  if (a.t === 'enote' || (a.t === 'neg' && strip(a.a).t === 'enote')) return { ok: true, val, form: 'enote', text: t };
  const sh = sciShape(a);
  if (sh) { const c = qabs(qdec(sh.c)), fin = !qlt(c, Q(1)) && qlt(c, Q(10));
    return { ok: true, val, form: fin ? 'sci' : 'notfin', c: sh.c, k: sh.k, digits: digitsOf(sh.c), text: t }; }
  if (!hasOp(a) || isFracLit(a)) return { ok: true, val, form: 'num', lit: numLit(a), text: t };
  return { ok: true, val, form: 'expr', ast: p.ast, text: t };
}
/* a plain number or fraction (walkthrough number steps): "12", "-4.75", "-19/4" */
function readNum(text) {                     /* the Hint's number steps: the answer box's own reader, plus a decimal comma ("8,3" from a pt-BR keypad) */
  let t = String(text == null ? '' : text).trim();
  if (/^[-−]?\d+,\d{1,2}$|^[-−]?\d+,\d{4,}$/.test(t)) t = t.replace(',', '.');
  const r = readAns(t); return r.ok && r.form === 'num' ? r.val : null;
}

/* ------------------------------------------------------------------ the questions */
const UNIT_ID = 'a7u4';
const TITLES = ['Operations in Scientific Notation', 'Real-World Problems in Scientific Notation', 'The Order of Operations with Exponents and Radicals'];
const NAMES = ['Nia', 'Omar', 'Lucia', 'Ben', 'Sofia', 'Kai', 'Maya', 'Leo', 'Zoe', 'Andre', 'Isla', 'Mateo', 'Grace', 'Jalen', 'Ruby', 'Eli', 'Hana', 'Felix'];
const d1 = T => T.ri(1, 9) + '.' + T.ri(1, 9);                                 /* a one-decimal coefficient, no ".0" */
const sciQ = (c, k) => qmul(qdec(c), p10(k));
const want = (q, n) => { const s = sciOf(q, n); return { v: q, c: s.c, k: s.k, n: n || digitsOf(s.c) }; };
const pS = h => par(h);                                                            /* (5.7 × 10⁵) */
const SECT = (title, items) => ({ title, items });
function sciPart(label, fam, prm, stem, value, extra) { return Object.assign({ label, fam, prm, stem, kind: 'sci', want: want(value), ans: value, key: fam + JSON.stringify(prm) }, extra || {}); }

/* the test (a7/build/u4/unit.py, Forms A and B): the numbers of every question, per family; the practice never uses them */
const TEST = {   /* Form A, then Form B (19 Oct 2026), then the review's numbers */
  addSame: [['3.6', 5, '2.1', 5], ['4.3', 6, '2.4', 6]], subSame: [['8.4', -6, '5.9', -6], ['9.1', -5, '3.6', -5]], addCarry: [['7.5', 8, '6.8', 8], ['6.4', 7, '8.2', 7]], addGap: [['4.2', 4, '3.7', 3], ['5.3', 5, '2.6', 4]],
  mulInt: [[3, 4, 2, 6], [4, 3, 2, 5]], divDec: [['9.6', 9, '1.2', 4], ['8.4', 8, '2.1', 3]], mulAdj: [[5, -3, 4, 7], [6, -4, 5, 6]], divAdj: [['1.8', 2, 6, 5], ['1.5', 2, 5, 6]],
  mcGap: [['1.4', 3, '2.9', 5], ['2.3', 3, '4.1', 5]], selSci: [[3, 6], [4, 6]],
  kendra: [['2.3', 4, '6.1', 6], ['3.4', 4, '5.2', 6]],   /* Form B's Devon: 3.4 × 10⁴ since 21 Oct (it was 10³, a gap of 3) */
  rate: [['6.5', 14, '4', 2], ['4', 3, '2', -1], ['5', 4, '3', -2]],   /* the review's laser, and the two forms' transfer item */
  rwArea: [['2.4', '1.35'], ['3.5', '1.25'], ['3.2', '1.45']], rwSpeed: [['5.6', 8], ['7.2', 8], ['4.8', 6]],
  rwSum: [['6.25', '4.1'], ['7.35', '5.2'], ['5.4', '2.8']], rwDiff: [['9.3', '4.72'], ['8.4', '3.61'], ['7.6', '3.42']],
  ooA: [[15, 2, 3], [20, 3, 2], [24, 3, 5]], ooB: [[5, 7, 2], [4, 9, 5], [6, 9, 3]], ooC: [[36, 4, 3], [45, 9, 3], [48, 6, 2]], ooD: [[4, 4], [3, 3], [6, 6]],
  radA: [[6, 13], [8, 17], [7, -24]], radB: [[5, 2], [4, 3]], radC: [[3, 2, 3], [2, 3, 4], [2, 1, 3]],
  patio: [[14, '2.40', 85], [12, '2.60', 75], [15, '2.20', 60], [18, '3.50', 140]], mcOrder: [[2, 5, 3], [3, 4, 3], [2, 4, 5]], selVal: [6, 8],
  nadia: [[5, 12], [6, 8]], negSub: [[5, 3]]
};
const onTest = (fam, key) => (TEST[fam] || []).some(t => JSON.stringify([].concat(t).map(String)) === JSON.stringify([].concat(key).map(String)));

let CLEAN = null;
function setClean(fn) { CLEAN = fn; }
function D(slot, seed, build) { return KIT.draw(UNIT_ID, seed, slot, build, it => !it.onTest && (!CLEAN || CLEAN(it))); }

/* ---------- section 1: operations in scientific notation */
function q1(seed) {
  return D('q1', seed, T => {
    const a = (() => { for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); const c1 = d1(T), c2 = d1(T), k = T.ri(3, 9), s = qadd(qdec(c1), qdec(c2));
      if (c1 !== c2 && qlt(s, Q(10)) && s.d === 10n) return { c1, k1: k, c2, k2: k }; } })();
    const b = (() => { for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); const c1 = d1(T), c2 = d1(T), k = -T.ri(2, 9), s = qsub(qdec(c1), qdec(c2));
      if (!qlt(s, Q(1)) && s.d === 10n) return { c1, k1: k, c2, k2: k }; } })();
    const c = (() => { for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); const c1 = d1(T), c2 = d1(T), k = T.ri(4, 9), s = qadd(qdec(c1), qdec(c2));
      if (!qlt(s, Q(10)) && s.d === 10n && c1 !== c2) return { c1, k1: k, c2, k2: k }; } })();
    const d = (() => { for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); const c1 = d1(T), c2 = d1(T), k = T.ri(3, 8), s = qadd(qdec(c1), qdiv(qdec(c2), Q(10)));
      if (qlt(s, Q(10))) return { c1, k1: k, c2, k2: k - 1 }; } })();
    const mk = (label, fam, x, op) => sciPart(label, fam, x, M(pS(sciH(x.c1, x.k1)) + ' ' + (op === '+' ? '+' : '−') + ' ' + pS(sciH(x.c2, x.k2))),
      op === '+' ? qadd(sciQ(x.c1, x.k1), sciQ(x.c2, x.k2)) : qsub(sciQ(x.c1, x.k1), sciQ(x.c2, x.k2)), { op });
    const parts = [mk('a', 'addSame', a, '+'), mk('b', 'subSame', b, '-'), mk('c', 'addCarry', c, '+'), mk('d', 'addGap', d, '+')];
    const tk = (fam, x) => onTest(fam, [x.c1, x.k1, x.c2, x.k2]) || onTest(fam, [x.c2, x.k2, x.c1, x.k1]);
    return { type: 'parts', stem: 'Add or subtract. Write each answer in scientific notation.', parts, onTest: tk('addSame', a) || tk('subSame', b) || tk('addCarry', c) || tk('addGap', d) };
  });
}
function q2(seed) {
  return D('q2', seed, T => {
    const PAIRS = [[2, 2], [2, 3], [3, 2], [2, 4], [4, 2], [3, 3]];
    const a = (() => { const [x, y] = T.pick(PAIRS); return { c1: x, k1: T.ri(2, 9), c2: y, k2: T.ri(2, 9) }; })();
    const b = (() => { for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); const c2 = d1(T), q = T.ri(2, 8), c1 = qmul(qdec(c2), Q(q)); if (qlt(c1, Q(10)) && places(c1) <= 1 && qdec(c2).n % 10n !== 0n) return { c1: decPlain(c1), k1: T.ri(6, 12), c2, k2: T.ri(2, 5) }; } })();
    const c = (() => { for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); const x = T.ri(2, 9), y = T.ri(2, 9); if (x * y >= 10) return { c1: x, k1: -T.ri(2, 6), c2: y, k2: T.ri(5, 9) }; } })();
    const d = (() => { for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); const t = T.pick(['0.2', '0.25', '0.3', '0.4', '0.5', '0.6', '0.75', '0.8']), c2 = T.pick([2, 3, 4, 5, 6, 8, '1.2', '1.5', '2.4', '3.2']);
      const c1 = qmul(qdec(t), qdec(String(c2))); if (!qlt(c1, Q(1)) && places(c1) <= 1) { const k1 = T.ri(2, 6); return { c1: decPlain(c1), k1, c2: String(c2), k2: k1 + T.ri(1, 6) }; } } })();
    const mul = x => qmul(sciQ(String(x.c1), x.k1), sciQ(String(x.c2), x.k2)), div = x => qdiv(sciQ(String(x.c1), x.k1), sciQ(String(x.c2), x.k2));
    const line = (x, op) => op === '×' ? M(pS(sciH(x.c1, x.k1)) + pS(sciH(x.c2, x.k2))) : M(fr(sciH(x.c1, x.k1), sciH(x.c2, x.k2)));
    const parts = [sciPart('a', 'mulInt', a, line(a, '×'), mul(a), { op: '×' }), sciPart('b', 'divDec', b, line(b, '÷'), div(b), { op: '÷' }),
      sciPart('c', 'mulAdj', c, line(c, '×'), mul(c), { op: '×' }), sciPart('d', 'divAdj', d, line(d, '÷'), div(d), { op: '÷' })];
    const tk = (fam, x) => onTest(fam, [x.c1, x.k1, x.c2, x.k2]) || (/mul/.test(fam) && onTest(fam, [x.c2, x.k2, x.c1, x.k1]));
    return { type: 'parts', stem: 'Multiply or divide. Write each answer in scientific notation.', parts,
      onTest: tk('mulInt', a) || tk('divDec', b) || tk('mulAdj', c) || tk('divAdj', d) };
  });
}
function q3(seed) {
  return D('q3', seed, T => {
    let c1, c2, k; for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); c1 = d1(T); c2 = d1(T); k = T.ri(5, 9); if (qlt(qadd(qdec(c1), qdec(c2)), Q(10)) && c1 !== c2) break; }
    const k1 = k - 2, v = qadd(sciQ(c1, k1), sciQ(c2, k));
    const opts = [                                                         /* every wrong choice is a real slip with as many digits as the key (review 3) */
      { v, tag: 'ok' },
      { v: qadd(sciQ(c2, k), qmul(qdec(c1), p10(k - 1))), tag: 'oneFew' },
      { v: qmul(qadd(qdec(c1), qdec(c2)), p10(k)), tag: 'noMatch' },
      { v: qmul(qadd(qdec(c1), qdiv(qdec(c2), Q(100))), p10(k1)), tag: 'wrongWay' }];
    const order = T.shuffle([0, 1, 2, 3]), shown = order.map(i => opts[i]);
    return { type: 'mc', fam: 'mcGap', prm: { c1, k1, c2, k2: k }, stem: 'Which is the value of ' + M(pS(sciH(c1, k1)) + ' + ' + pS(sciH(c2, k))) + '?',
      opts: shown.map(o => { const s = sciOf(o.v); return M(sciH(s.c, s.k)); }), vals: shown.map(o => o.v), tags: shown.map(o => o.tag), correct: order.indexOf(0),
      key: 'mcGap' + [c1, k1, c2, k].join(',') + '|' + order.join(''), onTest: onTest('mcGap', [c1, k1, c2, k]) };
  });
}
function q4(seed) {                     /* 4 right of 6, drawn from five true forms and three false ones, so the shape never gives the answer (review 4) */
  return D('q4', seed, T => {
    const t = T.ri(3, 9), n = T.ri(4, 8), V = qmul(Q(t), p10(n));          /* t ≥ 3: two one-decimal coefficients over 1 can add to it */
    const off = T.pick(['0.2', '0.4', '0.5']), sub = { a: [decPlain(qadd(Q(t), qdec(off))), n], b: [decPlain(qmul(qdec(off), Q(10))), n - 1], op: '−' };
    const bs = ['2', '3', '4', '1.2', '1.5', '1.1'].filter(b => qlt(qmul(Q(t), qdec(b)), Q(10)) && !qeq(qdec(b), Q(1)));
    const b = T.pick(bs), qd = T.ri(2, 4), divR = { a: [decPlain(qmul(Q(t), qdec(b))), n + qd], b: [b, qd], op: '÷' };
    const F = ['1.5', '2', '2.5', '3', '3.5', '4', '5', '6', '7', '8', '9'], pairs = [], pairs10 = [];
    F.forEach(x => F.forEach(y => { const p = qmul(qdec(x), qdec(y)); if (x <= y && qeq(p, Q(t))) pairs.push([x, y]); if (x <= y && qeq(p, Q(10 * t))) pairs10.push([x, y]); }));
    const mp = pairs10.length && T.r() < 0.6 ? T.pick(pairs10).concat([1]) : T.pick(pairs.length ? pairs : pairs10).concat([pairs.length ? 0 : 1]);
    const p1 = T.ri(1, n - 1 - mp[2]), mulR = { a: [mp[0], p1], b: [mp[1], n - mp[2] - p1], op: '×' };
    let u, w; for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); u = T.ri(11, 10 * t - 11); w = 10 * t - u; if (u % 10 && w % 10) break; }
    const addR = { a: [decPlain(Q(u, 10)), n], b: [decPlain(Q(w, 10)), n], op: '+' };
    const dd = T.pick(['0.2', '0.4', '0.6', '0.8']), addGapR = { a: [decPlain(qsub(Q(t), qdec(dd))), n], b: [decPlain(qmul(qdec(dd), Q(10))), n - 1], op: '+' };
    const divW = { a: divR.a, b: [b, qd + 1], op: '÷' };
    let u2, w2; for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); u2 = T.ri(11, 10 * t - 11); w2 = 10 * t - u2; if (u2 % 10 && w2 % 10 && u2 !== u) break; }
    const addW = { a: [decPlain(Q(u2, 10)), n], b: [decPlain(Q(w2, 10)), n - 1], op: '+' };
    const mulW = pairs10.length ? (([x, y]) => { const q1 = T.ri(1, n - 1); return { a: [x, q1], b: [y, n - q1], op: '×' }; })(T.pick(pairs10)) : { a: divR.a, b: [b, qd - 1], op: '÷' };
    const trues = T.shuffle([sub, divR, mulR, addR, addGapR]).slice(0, 4), falses = T.shuffle([divW, addW, mulW]).slice(0, 2);
    const all = trues.concat(falses), val = e => { const A = sciQ(e.a[0], e.a[1]), B = sciQ(e.b[0], e.b[1]); return e.op === '+' ? qadd(A, B) : e.op === '−' ? qsub(A, B) : e.op === '×' ? qmul(A, B) : qdiv(A, B); };
    const order = T.shuffle([0, 1, 2, 3, 4, 5]), shown = order.map(i => all[i]);
    const h = e => e.op === '÷' ? M(fr(sciH(e.a[0], e.a[1]), sciH(e.b[0], e.b[1]))) : e.op === '×' ? M(pS(sciH(e.a[0], e.a[1])) + pS(sciH(e.b[0], e.b[1]))) : M(pS(sciH(e.a[0], e.a[1])) + ' ' + e.op + ' ' + pS(sciH(e.b[0], e.b[1])));
    return { type: 'multi', fam: 'selSci', prm: { t, n, exprs: shown }, stem: 'Select ALL of the expressions whose value is ' + sciM(t, n) + '.',
      opts: shown.map(h), vals: shown.map(val), target: V, correct: shown.map((e, i) => qeq(val(e), V) ? i : -1).filter(i => i >= 0), key: 'selSci' + JSON.stringify(shown), onTest: onTest('selSci', [t, n]) };
  });
}
function q5(seed) {
  return D('q5', seed, T => {
    let a, b, k1; for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); a = d1(T); b = d1(T); k1 = T.ri(3, 5); if (qlt(qadd(qdec(a), qdec(b)), Q(10)) && qlt(qadd(qdec(a), qdiv(qdec(b), Q(100))), Q(10))) break; }
    const k2 = k1 + 2, who = T.pick(NAMES), claimed = { c: decPlain(qadd(qdec(a), qdec(b))), k: k1 + k2 };
    const R = sciOf(qadd(sciQ(a, k1), sciQ(b, k2))), wrongSum = sciOf(qadd(sciQ(b, k2), qmul(qdec(a), p10(k2 - 1)))), noMatch = { c: claimed.c, k: k2 }, wrongWay = sciOf(qmul(qadd(qdec(a), qdiv(qdec(b), Q(100))), p10(k1)));
    const two = ': the powers weren’t matched before adding, and the exponents were added.';
    const opts = [                                                         /* the sum first, then the reason; three share a reason, so the sum decides (review 3) */
      { tag: 'ok', h: sciM(R.c, R.k) + two }, { tag: 'few', h: sciM(wrongSum.c, wrongSum.k) + two }, { tag: 'wrongWay', h: sciM(wrongWay.c, wrongWay.k) + two },
      { tag: 'exp', h: sciM(noMatch.c, noMatch.k) + ': the exponents were added, but the coefficients were added correctly.' }];
    const order = T.shuffle([0, 1, 2, 3]);
    return { type: 'mc', fam: 'kendra', prm: { a, k1, b, k2, who }, stem: who + ' writes ' + M(pS(sciH(a, k1)) + ' + ' + pS(sciH(b, k2))) + ' = ' + M(sciH(claimed.c, claimed.k)) + '. Which gives the correct sum and names the mistakes?',
      opts: order.map(i => opts[i].h), tags: order.map(i => opts[i].tag), correct: order.indexOf(0), sums: { R, wrongSum, noMatch, wrongWay, claimed }, key: 'kendra' + [a, k1, b, k2].join(',') + '|' + order.join(''), onTest: onTest('kendra', [a, k1, b, k2]) };
  });
}
const RATES = [['A laser emits', 'photons each second', 'photons', 'emit'], ['A pump moves', 'drops of water each second', 'drops', 'move'],
  ['A web server answers', 'requests each second', 'requests', 'answer'], ['A factory machine makes', 'tiny beads each second', 'beads', 'make']];
function q6(seed) {                     /* stand-in for the transfer item: the review's product word problem, the exact product two digits
                                           (like the review's 6.5 × 4 = 26). 21 Oct: the second number lost its ".0" (it was there for
                                           significant digits) */
  return D('q6', seed, T => {
    const C1 = [], C2 = ['2', '4', '5', '6', '8'];
    for (let d = 1; d <= 9; d++) ['2', '4', '5', '6', '8'].forEach(e => C1.push(d + '.' + e));
    const pairs = []; C1.forEach(x => C2.forEach(y => { const p = qmul(qdec(x), qdec(y)); if (!qlt(p, Q(10)) && p.d === 1n && p.n % 10n !== 0n && p.n < 100n) pairs.push([x, y]); }));
    const [x, y] = T.pick(pairs), sw = T.r() < 0.5, c1 = sw ? y : x, c2 = sw ? x : y, m = T.ri(5, 15), n = T.ri(1, 4);
    const [subj, per, noun, verb] = T.pick(RATES), v = qmul(sciQ(c1, m), sciQ(c2, n));
    const part = sciPart('', 'rate', { c1, m, c2, n, noun, verb }, '', v, { unitWord: noun, op: '×' });
    return { type: 'solo', stem: subj + ' ' + sciM(c1, m) + ' ' + per + '. How many does it ' + verb + ' in ' + sciM(c2, n) + ' seconds? Write your answer in scientific notation.',
      part, onTest: onTest('rate', [c1, m, c2, n]) || onTest('rate', [c2, n, c1, m]) };
  });
}

/* ---------- section 2: real-world problems in scientific notation. 21 Oct 2026 (Croix: "Remove the questions pertaining to
   significant digits. Add, subtract, multiply and dividing scientific notation is fine"): the counting question, the two
   explain-the-rule questions and the significant-digit choice are gone; the area, the speed, the sum and the difference stay,
   and every answer is the exact value in scientific notation, as on the test. "Do not round" is printed, as on the test: the
   class learned on 20 Oct (4.04) to round measured answers. */
function q7(seed) {
  return D('q7', seed, T => {
    /* the area: a one-decimal side times a two-decimal side, both × 10², as on the test (2.4 × 1.35); one set in four has a
       product of 10 or more, so the coefficient must be fixed (Part 1 practised it); never more than 4 digits to type */
    const big = T.r() < 0.25;
    let L, W, C; for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers');
      L = d1(T); W = T.ri(1, 9) + '.' + T.ri(0, 9) + T.ri(1, 9); C = qmul(qdec(L), qdec(W));
      if (!qlt(C, Q(10)) === big && digitsOf(sciOf(C).c) <= 4) break; }
    /* the speed: a whole number of km/h over a whole number of hours, the distance a one-decimal coefficient × 10²
       (as on the test: 5.6 × 10² km in 8 hours); a car or a train, 40 to 250 km/h */
    let Dk, t, v; for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers');
      t = T.ri(2, 9); v = T.ri(40, 250); const d = v * t; if (d >= 110 && d <= 990 && d % 10 === 0 && d % 100 !== 0) { Dk = decPlain(Q(d, 100)); break; } }
    const a = sciPart('a', 'rwArea', { L, W }, 'A rectangular plate measures ' + sciM(L, 2) + ' mm by ' + sciM(W, 2) + ' mm. Find its area.',
      qmul(sciQ(L, 2), sciQ(W, 2)), { unitWord: 'square millimeters', op: '×' });
    const b = sciPart('b', 'rwSpeed', { D: Dk, t }, 'A vehicle travels ' + sciM(Dk, 2) + ' km in ' + t + ' hours. Find its average speed.',
      Q(v), { unitWord: 'km/h', op: '÷' });
    return { type: 'parts', stem: 'Solve. Write each answer in scientific notation. Do not round.', parts: [a, b],
      onTest: onTest('rwArea', [L, W]) || onTest('rwArea', [W, L]) || onTest('rwSpeed', [Dk, t]) };
  });
}
function q8(seed) {
  return D('q8', seed, T => {
    /* the sum: a two-decimal coefficient × 10³ and a one-decimal coefficient × 10², one power apart (6.25 × 10³ + 4.1 × 10²) */
    let A, B; for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers');
      A = T.ri(1, 9) + '.' + T.ri(0, 9) + T.ri(1, 9); B = d1(T); if (qlt(qadd(qdec(A), qdiv(qdec(B), Q(10))), Q(10))) break; }
    /* the difference: a one-decimal coefficient × 10⁻² less a two-decimal coefficient × 10⁻³ (9.3 × 10⁻² − 4.72 × 10⁻³) */
    let C, Dd; for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers');
      C = d1(T); Dd = T.ri(1, 9) + '.' + T.ri(0, 9) + T.ri(1, 9); if (!qlt(qsub(qdec(C), qdiv(qdec(Dd), Q(10))), Q(1))) break; }
    const a = sciPart('a', 'rwSum', { A, B }, 'Two lengths are measured: ' + sciM(A, 3) + ' mm and ' + sciM(B, 2) + ' mm. Find their sum.',
      qadd(sciQ(A, 3), sciQ(B, 2)), { unitWord: 'mm', op: '+' });
    const b = sciPart('b', 'rwDiff', { C, D: Dd }, 'Two masses are measured: ' + sciM(C, -2) + ' g and ' + sciM(Dd, -3) + ' g. Find their difference.',
      qsub(sciQ(C, -2), sciQ(Dd, -3)), { unitWord: 'g', op: '−' });
    return { type: 'parts', stem: 'Solve. Write each answer in scientific notation. Do not round.', parts: [a, b], onTest: onTest('rwSum', [A, B]) || onTest('rwDiff', [C, Dd]) };
  });
}

/* ---------- section 3: the order of operations with exponents and radicals. Each keeps its 16 Oct slot name (q12 … q18), so a
   set keeps its Part 3 questions through the 21 Oct change; the questions are numbered 9 to 15 now. */
const pw = (b, e) => b + sup(e);
const pm = v => v < 0 ? ' − ' + -v : ' + ' + v;   /* a signed term after a first one */
function numPart(label, fam, prm, stem, ans, extra) { return Object.assign({ label, fam, prm, stem, kind: 'num', ans, key: fam + JSON.stringify(prm) }, extra || {}); }
function q9(seed) {
  return D('q12', seed, T => {
    const a = (() => { for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); const x = T.ri(10, 30), y = T.ri(2, 5), z = T.ri(2, 4); if (x - y * z * z !== 0) return { a: x, b: y, c: z }; } })();
    const b = (() => { for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); const c = T.pick([2, 3, 4]), x = T.ri(3, 12), y = T.ri(1, 99), s = x * x + y; if (s % (c ** 3) === 0 && s / c ** 3 >= 2) return { a: x, b: y, c }; } })();
    const c = (() => { const y = T.ri(2, 9), z = T.ri(2, 9), m = T.ri(2, 12); return { a: y * m, b: y, c: z }; })();
    const d = (() => { for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); const x = T.ri(2, 15), y = T.ri(2, 15); if (x !== y) return { a: x, b: y }; } })();
    const parts = [
      numPart('a', 'ooA', a, M(a.a + ' − ' + a.b + ' · ' + pw(a.c, 2)), Q(a.a - a.b * a.c * a.c)),
      numPart('b', 'ooB', b, M(fr(pw(b.a, 2) + ' + ' + b.b, pw(b.c, 3))), Q((b.a * b.a + b.b) / b.c ** 3)),
      numPart('c', 'ooC', c, M(c.a + ' ÷ ' + c.b + ' · ' + c.c), Q(c.a / c.b * c.c)),
      numPart('d', 'ooD', d, M('−' + pw(d.a, 2) + ' + ' + pw('(−' + d.b + ')', 2)), Q(d.b * d.b - d.a * d.a))];
    return { type: 'parts', stem: 'Evaluate each expression.', parts, onTest: onTest('ooA', [a.a, a.b, a.c]) || onTest('ooB', [b.a, b.b, b.c]) || onTest('ooC', [c.a, c.b, c.c]) || onTest('ooD', [d.a, d.b]) };
  });
}
function q10(seed) {
  return D('q13', seed, T => {
    const a = (() => { for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); const isSq = v => Math.round(Math.sqrt(v)) ** 2 === v;
      if (T.r() < 0.5) { const r = T.ri(5, 15), x = T.ri(2, r - 1), y = r * r - x * x; if (!isSq(y)) return { a: x, b: y, r }; }   /* √(x² + y) */
      else { const r = T.ri(2, 14), x = T.ri(r + 1, 15), y = x * x - r * r; if (!isSq(y)) return { a: x, b: -y, r }; } } })();   /* √(x² − y): b < 0 */
    const b = { n: T.ri(2, 5), k: T.ri(2, 10), s: T.r() < 2 / 3 ? -1 : 1, o: T.r() < 2 / 3 ? 1 : -1 };   /* s: the sign under the root; o: plus or minus (the test's shape is s −1, o +1) */
    const c = (() => { for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); const p = T.ri(2, 8), r = T.ri(2, 10), q = T.ri(1, r - 1); if (Number(gcd(BigInt(q), BigInt(r))) === 1 && p * p * r / Number(gcd(BigInt(p * p), BigInt(r))) <= 300) return { p, q, r }; } })();
    const parts = [
      numPart('a', 'radA', a, M(sqrtH(pw(a.a, 2) + pm(a.b))), Q(a.r)),
      numPart('b', 'radB', b, M(cbrtH((b.s < 0 ? '−' : '') + b.n ** 3) + (b.o > 0 ? ' + ' : ' − ') + pw(b.k, -2)), qadd(Q(b.s * b.n), Q(b.o, b.k * b.k))),
      numPart('c', 'radC', c, M(pw('(−' + fr(1, c.p) + ')', 2) + ' + ' + sqrtH(fr(c.q * c.q, c.r * c.r))), qadd(Q(1, c.p * c.p), Q(c.q, c.r)))];
    return { type: 'parts', stem: 'Evaluate each expression.', parts, onTest: onTest('radA', [a.a, a.b]) || (b.s < 0 && b.o > 0 && onTest('radB', [b.n, b.k])) || onTest('radC', [c.p, c.q, c.r]) };
  });
}
function q11(seed) {
  return D('q14', seed, T => {
    const s = T.ri(10, 25), cents = T.ri(30, 96) * 5, rr = Math.floor(cents / 100) + '.' + String(cents % 100).padStart(2, '0'), f = T.ri(8, 30) * 5;
    const total = qadd(qmul(Q(s * s), qdec(rr)), Q(f));
    const prm = { s, r: rr, f };
    const a = { label: 'a', fam: 'patioExpr', prm, stem: 'Write an expression for the total cost.', kind: 'expr', ans: total, keyExpr: pw(s, 2) + '(' + rr + ') + ' + f, key: 'patioExpr' + JSON.stringify(prm) };
    const b = { label: 'b', fam: 'patioCost', prm, stem: 'Find the total cost.', kind: 'money', ans: total, key: 'patioCost' + JSON.stringify(prm) };
    return { type: 'parts', stem: 'A square patio has sides of ' + s + ' feet. Sealing it costs $' + rr + ' per square foot, plus a $' + f + ' delivery fee.', parts: [a, b], onTest: onTest('patio', [s, rr, f]) };
  });
}
function q12(seed) {
  return D('q15', seed, T => {
    let a, b, c, vs; for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); a = T.ri(2, 9); b = T.ri(2, 9); c = T.ri(2, 5); vs = [a + b * c * c, a + b * c * 2, (a + b) * c * c, (a + b * c) ** 2]; if (new Set(vs).size === 4) break; }
    const tags = ['ok', 'times2', 'addFirst', 'squareAll'], order = T.shuffle([0, 1, 2, 3]);
    return { type: 'mc', fam: 'mcOrder', prm: { a, b, c }, stem: 'Which is the value of ' + M(a + ' + ' + b + ' · ' + pw(c, 2)) + '?', opts: order.map(i => String(vs[i])), vals: order.map(i => Q(vs[i])), tags: order.map(i => tags[i]),
      correct: order.indexOf(0), key: 'mcOrder' + [a, b, c] + '|' + order.join(''), onTest: onTest('mcOrder', [a, b, c]) };
  });
}
function q13(seed) {                    /* 4 right of 6, drawn from six true forms and three false ones (review 4) */
  return D('q16', seed, T => {
    const v = T.pick([4, 5, 7, 8, 9, 10, 11, 12]);
    let x, y; for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); x = T.ri(2, v - 1); y = v * v - x * x; if (y > 0) break; }
    let z, x2, y2; for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); z = T.ri(2, 5); x2 = T.ri(2, 6); y2 = v * z - x2 * x2; if (y2 > 0 && y2 % z !== 0) break; }
    const b = T.ri(2, 4), c = T.ri(2, 4), A = v * b * c;
    let b2, c2, A2; for (let _g = 0; ; _g++) { if (_g > 20000) throw new Error('generator could not find numbers'); b2 = T.ri(2, 6); c2 = T.ri(2, 6); A2 = v * b2 / c2; if (Number.isInteger(A2) && b2 !== c2 && A2 > 0) break; }
    const trues = [{ h: M(sqrtH(v * v)), v: Q(v), tag: 'root' }, { h: M(pw(par(fr(1, v)), -1)), v: Q(v), tag: 'recip' }, { h: M(sqrtH(pw(x, 2) + ' + ' + y)), v: Q(v), tag: 'rootSum' },
      { h: M(fr(pw(x2, 2) + ' + ' + y2, z)), v: Q(v), tag: 'bar' }, { h: M(sqrtH(pw('(−' + v + ')', 2))), v: Q(v), tag: 'negSq' }, { h: M(A2 + ' ÷ ' + b2 + ' · ' + c2), v: Q(v), tag: 'lrTrue' }];
    const falses = [{ h: M('−' + sqrtH(v * v)), v: Q(-v), tag: 'negRoot' }, { h: M(A + ' ÷ ' + b + ' · ' + c), v: Q(A / b * c), tag: 'leftRight' },
      { h: M(pw(x2, 2) + ' + ' + y2 + ' ÷ ' + z), v: qadd(Q(x2 * x2), Q(y2, z)), tag: 'divFirst' }];
    const pickT = T.shuffle([0, 1, 2, 3, 4, 5]).slice(0, 4), pickF = T.shuffle([0, 1, 2]).slice(0, 2), ex = pickT.map(i => trues[i]).concat(pickF.map(i => falses[i]));
    const order = T.shuffle([0, 1, 2, 3, 4, 5]), shown = order.map(i => ex[i]);
    return { type: 'multi', fam: 'selVal', prm: { v, x, y, z, x2, y2, A, b, c, A2, b2, c2, pickT, pickF, order }, stem: 'Select ALL of the expressions whose value is ' + v + '.', opts: shown.map(e => e.h), vals: shown.map(e => e.v), tags: shown.map(e => e.tag),
      target: Q(v), correct: shown.map((e, i) => qeq(e.v, Q(v)) ? i : -1).filter(i => i >= 0), key: 'selVal' + JSON.stringify([v, x, z, x2, A, b, c, A2, b2, c2, pickT, pickF, order]), onTest: onTest('selVal', [v]) };
  });
}
const TRIPLES = [[3, 4, 5], [6, 8, 10], [8, 15, 17], [7, 24, 25], [9, 12, 15], [12, 16, 20], [15, 20, 25]];   /* roots the unit teaches (to 25); never the test's 5, 12, 13 */
function q14(seed) {
  return D('q17', seed, T => {
    const tr = T.pick(TRIPLES), sw = T.r() < 0.5, a = sw ? tr[1] : tr[0], b = sw ? tr[0] : tr[1], c = tr[2], A = a * a, B = b * b, who = T.pick(NAMES);
    const opts = [                                                         /* every choice the same shape: a reason, then the value (review 3) */
      { tag: 'ok', h: 'Add under the bar first: ' + M(sqrtH(A + B)) + ' = ' + c + '.' },
      { tag: 'right', h: who + ' is right: ' + M(sqrtH(A) + ' + ' + sqrtH(B)) + ' = ' + (a + b) + '.' },
      { tag: 'mult', h: 'Multiply the roots: ' + M(sqrtH(A) + ' · ' + sqrtH(B)) + ' = ' + (a * b) + '.' },
      { tag: 'noRoot', h: 'Add and drop the root: ' + A + ' + ' + B + ' = ' + (A + B) + '.' }];
    const order = T.shuffle([0, 1, 2, 3]);
    return { type: 'mc', fam: 'nadia', prm: { a, b, c, who }, stem: who + ' writes ' + M(sqrtH(A + ' + ' + B)) + ' = ' + M(sqrtH(A) + ' + ' + sqrtH(B)) + ' = ' + (a + b) + '. Which explains the mistake and gives the correct value?',
      opts: order.map(i => opts[i].h), tags: order.map(i => opts[i].tag), correct: order.indexOf(0), key: 'nadia' + [a, b] + '|' + order.join(''), onTest: onTest('nadia', [a, b]) || onTest('nadia', [b, a]) };   /* both orders: √(64 + 36) is Form B's question written backwards (21 Oct) */
  });
}
function q15(seed) {                                                            /* stand-in for the transfer item: evaluate with a negative value (Lesson 7) */
  return D('q18', seed, T => {
    const a = T.ri(2, 12), n = T.ri(2, 12), L = T.pick(['x', 'n', 't', 'w']);          /* to 12 × 12²: 120 versions (ruling 49, 22 Oct 2026) */
    const part = numPart('', 'negSub', { a, n, L }, '', Q(a * n * n));
    return { type: 'solo', stem: 'Evaluate ' + M(a + '<i>' + L + '</i>' + sup(2)) + ' when ' + M('<i>' + L + '</i> = −' + n) + '.', part, onTest: onTest('negSub', [a, n]) };
  });
}

function generate(seed) {
  if (!CLEAN) throw new Error('coach.js must be loaded before generating');
  return { seed, sections: [
    SECT(TITLES[0], [q1(seed), q2(seed), q3(seed), q4(seed), q5(seed), q6(seed)]),
    SECT(TITLES[1], [q7(seed), q8(seed)]),
    SECT(TITLES[2], [q9(seed), q10(seed), q11(seed), q12(seed), q13(seed), q14(seed), q15(seed)])] };
}
function partsOf(it) { return it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : [it]; }

const api = { UNIT_ID, TITLES, NAMES, TEST, Q, qadd, qsub, qmul, qdiv, qneg, qabs, qeq, qlt, qcmp, qnum, qpow, p10, qdec, places, decPlain, numStr, commas,
  expOf, sciOf, digitsOf, esc, M, speakH, fr, qH, qF, sciH, sciM, sciSay, sqrtH, cbrtH, pw, par, sup, minus, ansHtml,
  tidy, parse, evalA, readAns, readNum, sciShape, setClean, onTest, generate, partsOf, sciQ };
if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.Practice = api;
})(this);
