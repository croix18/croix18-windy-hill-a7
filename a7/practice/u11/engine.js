/* A7 Unit 11 practice (Solving Equations and Systems): exact numbers, equations kept as their printed pieces, lines y = mx + b,
   reading what a student types, and the fourteen questions of the practice test (a7/build/u11/unit.py), in its order and with
   its points. Ruling 49 (22 Oct 2026): the unit test is a random set of this page, so every part comes in many versions.

   The unit's standing decisions hold on every question (the lesson outlines): every system is given solved for y and a line is
   read from a table of values or a graph — no "slope", no "y-intercept" on the page; no substitution, no elimination; the three
   endings x = a, a = a, a = b, and x = 0 is one solution; a decimal distributed has its own question; multiplication is written
   with parentheses or a dot, never ×, so x is always a variable. Each equation is generated FROM its solution and its shape,
   then solved again (coach.js re-derives every line; u11_check.js and verify.py solve it a third and a fourth way). */
(function (root) {
'use strict';
const node = typeof module !== 'undefined' && module.exports;
const KIT = node ? require('../kit/core.js') : root.Kit;

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
const qsign = a => a.n > 0n ? 1 : a.n < 0n ? -1 : 0;
const isInt = q => q.d === 1n;
const ZERO = Q(0), ONE = Q(1);
function places(q) { let d = q.d, t = 0, f = 0; while (d % 2n === 0n) { d /= 2n; t++; } while (d % 5n === 0n) { d /= 5n; f++; } return d === 1n ? Math.max(t, f) : -1; }
function decPlain(q) {                               /* a terminating decimal, ASCII "-" for minus; throws if it never ends */
  const neg = q.n < 0n, a = qabs(q), k = places(a); if (k < 0) throw new Error('not terminating');
  let s = (a.n * (10n ** BigInt(k)) / a.d).toString();
  if (k > 0) { s = s.padStart(k + 1, '0'); s = s.slice(0, s.length - k) + '.' + s.slice(s.length - k); }
  return (neg ? '-' : '') + s;
}
function qdec(s) {                                   /* "-1.5", "−2", ".5", "3/4", "-7/2" → exact */
  let t = String(s).trim().replace(/[−–]/g, '-'), neg = false;
  if (t[0] === '-') { neg = true; t = t.slice(1); }
  let m = /^(\d+)\/(\d+)$/.exec(t);
  if (m) { const q = Q(m[1], m[2]); return neg ? qneg(q) : q; }
  m = /^(\d*)(?:\.(\d*))?$/.exec(t);
  if (!m || (m[1] === '' && !m[2])) throw new Error('not a number: ' + s);
  const f = m[2] || '', q = Q(BigInt((m[1] || '0') + f), 10n ** BigInt(f.length));
  return neg ? qneg(q) : q;
}
const qv = v => typeof v === 'object' ? v : typeof v === 'string' ? qdec(v) : Number.isInteger(v) ? Q(v) : qdec(String(v));
const kstr = q => places(q) >= 0 ? decPlain(q) : q.n + '/' + q.d;          /* a number in a key or a prm: ASCII, exact */
/* a number as read: −1.5, 7, 11/2 (a fraction only when it never ends; in html it is drawn as one) */
function numStr(q) { q = qv(q); const a = qabs(q); return (q.n < 0n ? '−' : '') + (places(a) < 0 ? a.n + '/' + a.d : decPlain(a)); }
const N = numStr;
/* a number to the nearest tenth, as a key prints an estimate */
function tenthOf(q) { const t = Math.round(qnum(q) * 10 + (qsign(q) >= 0 ? 1e-9 : -1e-9)); return Q(t, 10); }

/* ------------------------------------------------------------------ html */
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const fr = (n, d) => '<span class="fr"><span class="nu">' + n + '</span><span class="de">' + d + '</span></span>';
function nHtml(q) { q = qv(q); const a = qabs(q); return (q.n < 0n ? '−' : '') + (places(a) < 0 ? fr(String(a.n), String(a.d)) : decPlain(a)); }
/* what a screen reader says for a piece of math */
function speakH(h) {
  let t = String(h);
  for (let i = 0; i < 4; i++) t = t.replace(/<span class="fr"><span class="nu">([^<]*)<\/span><span class="de">([^<]*)<\/span><\/span>/, ' $1 over $2 ');
  t = t.replace(/<[^>]+>/g, '').replace(/&nbsp;| /g, ' ');
  return t.replace(/□/g, ' box ').replace(/·/g, ' times ').replace(/÷/g, ' divided by ').replace(/−/g, ' minus ').replace(/\+/g, ' plus ').replace(/=/g, ' equals ').replace(/≈/g, ' is about ').replace(/\s+/g, ' ').trim();
}
const M = h => '<span class="m" role="img" aria-label="' + esc(speakH(h)) + '">' + h + '</span>';
const vi = v => '<i>' + v + '</i>';
const pairH = (x, y) => '(' + nHtml(x) + ', ' + nHtml(y) + ')';            /* (4, −2), held together */
const pairT = (x, y) => '(' + numStr(x) + ', ' + numStr(y) + ')';

/* ------------------------------------------------------------------ an equation in one letter, kept as its printed pieces
   A side is a list of chunks, printed in order: a term {k:'t', c, v} (v the letter, or null for a number), a group
   {k:'g', f, t: [terms]} — f times the terms inside — or the box {k:'b', v}. The first chunk carries its own sign; a later one
   is joined by + or − . So 18 − 3(x − 2) is [t 18, g −3 (t x, t −2)]. */
const T_ = (c, v) => ({ k: 't', c: qv(c), v: v || null });
const G_ = (f, terms, frc) => ({ k: 'g', f: qv(f), t: terms, fr: !!frc });
const B_ = v => ({ k: 'b', v: v || null });
const sgnOf = ch => ch.k === 't' ? qsign(ch.c) : ch.k === 'g' ? qsign(ch.f) : 1;
const absOf = ch => ch.k === 't' ? Object.assign({}, ch, { c: qabs(ch.c) }) : ch.k === 'g' ? Object.assign({}, ch, { f: qabs(ch.f) }) : ch;
const HALF = q => qabs(q).d === 2n && qabs(q).n === 1n;              /* ½ in a line is drawn as a fraction, as the lessons write it */
const GLYPH = { '1/2': '½', '1/3': '⅓', '2/3': '⅔', '1/4': '¼', '3/4': '¾', '1/5': '⅕', '2/5': '⅖', '3/5': '⅗', '4/5': '⅘' };
const fracT = q => (qsign(q) < 0 ? '−' : '') + (GLYPH[qabs(q).n + '/' + q.d] || '(' + qabs(q).n + '/' + q.d + ')');   /* a fraction in a sentence: ⅔ */
function coefH(c, v, how, frc) {                    /* 3x, x, ½x, 0.4x */
  if (!v) return how === 'text' ? numStr(c) : nHtml(c);
  if (qeq(c, ONE)) return how === 'text' ? v : vi(v);
  if (frc && !isInt(c)) return how === 'text' ? fracT(c) + v : (qsign(c) < 0 ? '−' : '') + fr(String(qabs(c).n), String(c.d)) + vi(v);
  return (how === 'text' ? numStr(c) : nHtml(c)) + (how === 'text' ? v : vi(v));
}
function body(ch, how) {
  if (ch.k === 't') return coefH(ch.c, ch.v, how, ch.fr);
  if (ch.k === 'b') return '□' + (ch.v ? (how === 'text' ? ch.v : vi(ch.v)) : '');
  const fq = ch.fr && !isInt(ch.f) ? (how === 'text' ? fracT(ch.f) : fr(String(ch.f.n), String(ch.f.d))) : how === 'text' ? numStr(ch.f) : nHtml(ch.f);
  return (qeq(ch.f, ONE) ? '' : fq) + '(' + sideOut(ch.t, how) + ')';
}
function sideOut(side, how) {
  if (!side.length) return '0';
  return side.map((ch, i) => { const neg = sgnOf(ch) < 0, b = body(absOf(ch), how);
    return i === 0 ? (neg ? '−' + b : b) : (neg ? ' − ' : ' + ') + b; }).join('');
}
const sideH = s => sideOut(s, 'html'), sideT = s => sideOut(s, 'text');
const eqH = e => sideH(e.L) + ' = ' + sideH(e.R), eqT = e => sideT(e.L) + ' = ' + sideT(e.R);
/* the linear form a·v + b of a side, exactly (a box counts as nothing: its side is read once the box is filled) */
function lin(side) {
  let a = ZERO, b = ZERO;
  for (const ch of side) {
    if (ch.k === 't') { if (ch.v) a = qadd(a, ch.c); else b = qadd(b, ch.c); }
    else if (ch.k === 'g') { const i = lin(ch.t); a = qadd(a, qmul(ch.f, i.a)); b = qadd(b, qmul(ch.f, i.b)); }
  }
  return { a, b };
}
const fill = (side, val) => side.map(ch => ch.k === 'b' ? T_(val, ch.v) : ch);
/* the ending of an equation: {kind: 'one', s} | {kind: 'none'} | {kind: 'all'} */
function ending(e) {
  const L = lin(e.L), R = lin(e.R), a = qsub(L.a, R.a), b = qsub(R.b, L.b);
  if (a.n === 0n) return { kind: b.n === 0n ? 'all' : 'none' };
  return { kind: 'one', s: qdiv(b, a) };
}
function evalSide(side, val) { const l = lin(side); return qadd(qmul(l.a, val), l.b); }
/* sympy syntax, exact */
const R_ = q => 'Rational(' + q.n + ',' + q.d + ')';
function plainSide(side, v) {
  if (!side.length) return '0';
  return side.map(ch => ch.k === 't' ? '(' + R_(ch.c) + ')' + (ch.v ? '*' + v : '') : ch.k === 'g' ? '(' + R_(ch.f) + ')*(' + plainSide(ch.t, v) + ')' : 'BOX' + (ch.v ? '*' + v : '')).join('+');
}
/* the value put in, as a student writes a check: 2(3(3) − 4) + 5(3) */
function substT(side, val) {
  const vs = q => qsign(q) < 0 ? '(' + numStr(q) + ')' : numStr(q), vn = q => qsign(q) <= 0 ? '(' + numStr(q) + ')' : numStr(q);
  const one = ch => {
    if (ch.k === 't') return ch.v ? (qeq(ch.c, ONE) ? (sgnOf0 < 0 ? vn(val) : first ? numStr(val) : vs(val)) : (ch.fr && !isInt(ch.c) ? fracT(ch.c) : numStr(ch.c)) + '(' + numStr(val) + ')') : numStr(ch.c);
    if (ch.k === 'g') return (qeq(ch.f, ONE) ? '' : ch.fr && !isInt(ch.f) ? fracT(ch.f) : numStr(ch.f)) + '(' + substT(ch.t, val) + ')';
    return '?';
  };
  if (!side.length) return '0';
  let sgnOf0 = 1, first = true;
  return side.map((ch, i) => { const neg = sgnOf(ch) < 0; sgnOf0 = neg ? -1 : 1; first = i === 0; const b = one(absOf(ch)); return i === 0 ? (neg ? '−' + b : b) : (neg ? ' − ' : ' + ') + b; }).join('');
}
/* the numbers a student sees printed in an equation, as sizes */
function sideNums(side) { const out = []; for (const ch of side) { if (ch.k === 't') out.push(qabs(ch.c)); else if (ch.k === 'g') { out.push(qabs(ch.f)); out.push(...sideNums(ch.t)); } } return out; }

/* ------------------------------------------------------------------ a line y = mx + b (the systems are given solved for y) */
const L_ = (m, b) => ({ m: qv(m), b: qv(b) });
/* y = 3x − 2, y = −x + 6, y = ½x − 4, y = 4x; `alt` is the same line written another way: y = a(x + c) + d */
function lineSide(l) {
  if (l.alt) { const a = l.alt; return [G_(a.a, [T_(1, 'x'), T_(a.c)])].concat(qsign(qv(a.d)) ? [T_(a.d)] : []); }
  const s = []; if (l.m.n !== 0n) s.push(Object.assign(T_(l.m, 'x'), { fr: true })); if (l.b.n !== 0n || !s.length) s.push(T_(l.b)); return s;
}
const lineH = l => vi('y') + ' = ' + sideH(lineSide(l));
const lineT = l => 'y = ' + sideT(lineSide(l));
const onLine = (l, x, y) => qeq(qadd(qmul(l.m, qv(x)), l.b), qv(y));
const yAt = (l, x) => qadd(qmul(l.m, qv(x)), l.b);
/* where two lines meet: {x, y}, or null when the same number multiplies x */
function meet(l1, l2) { const dm = qsub(l1.m, l2.m); if (dm.n === 0n) return null; const x = qdiv(qsub(l2.b, l1.b), dm); return { x, y: yAt(l1, x) }; }

/* ------------------------------------------------------------------ reading what a student types
   readNum(text) — one number (a Hint step): 7, −28, 5.5, 11/2, 5 1/2.
   readAns(text) → {ok, nums: [{q, tag}], letter, shape, labels} or {ok: false, msg} or {ok: false, blank: true}:
     one number "n = 3", "3 = n", "−7", "11/2", "5 1/2", "33 ÷ 11" (shape 'expr' for arithmetic left to do), "7 months";
     two numbers "(4, −2)", "4, −2", "x = 4, y = −2", "4 and −2", "5 weeks, $40" (a tag says which is which). */
const UNREAD = 'I can’t read that. Type just your answer, like 7, −3.5 or 2/3.';
function tidy(t) {
  return String(t == null ? '' : t).toLowerCase().replace(/[−–—‒]/g, '-').replace(/[·∙⋅×✕*]/g, '*').replace(/÷/g, '/').replace(/ /g, ' ')
    .replace(/\s+/g, ' ').trim().replace(/([\da-z)])\s*\.$/, '$1').trim();
}
function parseExpr(t) {                          /* numbers, + − × ÷ / and parentheses, exact; null if it is not that */
  const toks = [], re = /\s*(\d+\.?\d*|\.\d+|[+\-*/()])/y; let pos = 0;
  t = t.trim(); if (!t) return null;
  while (pos < t.length) { re.lastIndex = pos; const m = re.exec(t); if (!m) return null; toks.push(m[1]); pos = re.lastIndex; while (t[pos] === ' ') pos++; }
  if (/\d\s+\d/.test(t.replace(/\s*([+\-*/()])\s*/g, '$1'))) return { two: true };
  let i = 0; const isNum = x => /^[\d.]/.test(x);
  function atom() { const x = toks[i]; if (x === undefined) throw 0; if (isNum(x)) { i++; return qdec(x.replace(/\.$/, '')); } if (x === '(') { i++; const e = expr(); if (toks[i] !== ')') throw 0; i++; return e; } throw 0; }
  function unary() { if (toks[i] === '-') { i++; return qneg(unary()); } if (toks[i] === '+') { i++; return unary(); } return atom(); }
  function term() { let a = unary(); for (;;) { const x = toks[i]; if (x === '*') { i++; a = qmul(a, unary()); } else if (x === '/') { i++; const b = unary(); if (b.n === 0n) throw 1; a = qdiv(a, b); } else if (x === '(') a = qmul(a, atom()); else return a; } }
  function expr() { let a = term(); for (;;) { if (toks[i] === '+') { i++; a = qadd(a, term()); } else if (toks[i] === '-') { i++; a = qsub(a, term()); } else return a; } }
  try {
    const v = expr(); if (i !== toks.length) return null;
    const n = toks.length, numAt = k => isNum(toks[k]);
    const shape = (n === 1 && numAt(0)) || (n === 2 && toks[0] === '-' && numAt(1)) ? 'num'
      : (n === 3 && numAt(0) && toks[1] === '/' && numAt(2)) || (n === 4 && toks[0] === '-' && numAt(1) && toks[2] === '/' && numAt(3)) ? 'frac' : 'expr';
    return { val: v, shape };
  } catch (e) { return e === 1 ? { zero: true } : null; }
}
function parseNum(s) {                           /* a mixed number (5 1/2), or an expression of numbers */
  s = s.trim();
  const m = /^(-?)(\d+) (\d+)\/(\d+)$/.exec(s);
  if (m) { if (m[4] === '0') return { zero: true }; const v = qadd(Q(m[2]), Q(m[3], m[4])); return { val: m[1] ? qneg(v) : v, shape: 'mixed' }; }
  return parseExpr(s);
}
const UNITW = /\b(?:dollars?|bucks|weeks?|wks?|months?|mos?|visits?|hours?|hrs?|classes|class|lessons?|days?|years?|cm|centimeters?|inches|inch|feet|foot|ft|each|both|after|about|approximately|approx|around|solution|the|is|it|of|in|and so|so|only)\b/g;
function tagOf(s) { return /\$|dollar|buck|cm|centimeter|inch|feet|foot|ft\b/.test(s) ? 'amt' : /week|wk|month|hour|visit|class|lesson|day|year/.test(s) ? 'count' : null; }
function oneNum(s) {                             /* one piece: its value and the letter it was given to, if any */
  let t = s.trim(), letter = null;
  const tag = tagOf(t);
  t = t.replace(/\$/g, ' ').replace(UNITW, ' ').replace(/\s+/g, ' ').trim();
  let m = /^([a-z])\s*=\s*(.+)$/.exec(t); if (m) { letter = m[1]; t = m[2]; }
  else if ((m = /^(.+?)\s*=\s*([a-z])$/.exec(t))) { letter = m[2]; t = m[1]; }
  if (/[a-z=]/.test(t)) return null;
  const r = parseNum(t); if (!r) return null;
  return Object.assign({ letter, tag }, r);
}
function readAns(text, kind) {
  const raw = String(text == null ? '' : text);
  if (!raw.trim()) return { ok: false, blank: true };
  if (raw.length > 60) return { ok: false, msg: 'That is too long to read. Type just your answer.' };
  let t = tidy(raw);
  if (/\d,\d{3}(?!\d)/.test(t) && kind === 'num') t = t.replace(/(\d),(?=\d{3}(?!\d))/g, '$1');
  if (kind === 'num') {
    if (/[<>≤≥]/.test(t)) return { ok: false, msg: 'This is an equation: the answer is one number, with no &lt;, &gt;, ≤ or ≥.' };
    if (/\d,\d/.test(t)) return { ok: false, msg: 'Use a period for a decimal point, like 5.5.' };
    if (/no solution|none|infinite|every number|all (real )?numbers/.test(t)) return { ok: false, msg: 'This one asks for a number. Type just the number.' };
    const r = oneNum(t);
    if (!r) { if (/^-?\d*\.?\d*\s*[a-z]$/.test(t) && /\d/.test(t)) return { ok: true, unsolved: true, nums: [] }; return { ok: false, msg: UNREAD }; }
    if (r.zero) return { ok: false, msg: 'That divides by 0.' };
    if (r.two) return { ok: false, msg: 'I see two numbers with a space between them. Type one number.' };
    return { ok: true, nums: [{ q: r.val, tag: r.tag }], letter: r.letter, shape: r.shape };
  }
  /* two numbers: an ordered pair, or the weeks and the amount */
  let s = t.replace(/^\(\s*/, '').replace(/\s*\)$/, '').replace(/[()]/g, ' ').trim();
  let pieces = null, labels = null;
  const lx = /x\s*=\s*(-?[\d./]+(?: \d+\/\d+)?)/.exec(s), ly = /y\s*=\s*(-?[\d./]+(?: \d+\/\d+)?)/.exec(s);
  if (lx && ly) { pieces = [lx[1], ly[1]]; labels = true; }
  else if (lx || ly) return { ok: false, msg: 'Give both numbers: the x and the y, like (4, −2).' };
  else {
    const parts = s.split(/\s*(?:,|;|\band\b|&)\s*/).filter(p => p.trim());
    if (parts.length === 2) pieces = parts;
    else if (parts.length === 1) {
      const sp = parts[0].replace(/\$/g, ' $').trim().split(/\s+/).filter(Boolean), nums = sp.filter(w => /\d/.test(w));
      if (nums.length === 2 && sp.length <= 6) { const i = sp.findIndex(w => /\d/.test(w)), j = sp.findIndex((w, k) => k > i && /\d/.test(w)); pieces = [sp.slice(0, j).join(' '), sp.slice(j).join(' ')]; }
      else if (nums.length === 1) return { ok: false, msg: kind === 'story' ? 'Give both numbers: how many, and how much each has, like 5 weeks, $40.' : 'Give both numbers: the x and the y, like (4, −2).' };
    } else if (parts.length > 2) return { ok: false, msg: 'Type two numbers, like (4, −2).' };
  }
  if (!pieces) return { ok: false, msg: kind === 'story' ? 'Type the two numbers, like 5 weeks, $40.' : 'Type the ordered pair, like (4, −2).' };
  const got = pieces.map(oneNum);
  if (got.some(g => !g || g.zero || g.two || g.shape === 'expr')) return { ok: false, msg: kind === 'story' ? 'Type the two numbers, like 5 weeks, $40.' : 'Type the ordered pair, like (4, −2).' };
  let nums = got.map(g => ({ q: g.val, tag: g.tag }));
  if (kind === 'story' && nums[0].tag === 'amt' && nums[1].tag !== 'amt') nums = [nums[1], nums[0]];     /* "$40 after 5 weeks" */
  return { ok: true, nums, labels: !!labels, shape: 'pair' };
}
function readNum(text) {
  const t = String(text || '').trim().replace(/[−–]/g, '-').replace(/^\$\s*/, '');
  if (/^-?\d+\s+\d+\s*\/\s*\d+$/.test(t)) { const r = parseNum(t.replace(/\s*\/\s*/, '/').replace(/\s+/, ' ')); return r && r.val ? r.val : null; }
  if (!/^-?\d+(\.\d+)?$|^-?\.\d+$|^-?\d+\s*\/\s*\d+$/.test(t)) return null;
  const r = parseNum(t.replace(/\s+/g, '')); return r && r.val ? r.val : null;
}

/* ------------------------------------------------------------------ the questions */
const UNIT_ID = 'a7u11';
const TITLES = ['Solving Equations', 'Solutions of a System', 'How Many Solutions a System Has', 'Solving Systems by Graphing'];
const LETTERS = ['n', 'h', 'm', 'v', 'w', 'k', 't', 'p', 'x'];
const NAMES = ['Mia', 'Leo', 'Ava', 'Ben', 'Nia', 'Omar', 'Lucia', 'Kai', 'Maya', 'Zoe', 'Andre', 'Isla', 'Mateo', 'Grace', 'Jalen', 'Ruby', 'Eli', 'Hana', 'Felix', 'Sofia'];
const ENDINGS = ['One solution', 'No solution', 'Infinitely many solutions'];         /* a choice keeps this order */
const SECT = (title, items) => ({ title, items });
const keyOf = (fam, prm) => fam + ':' + JSON.stringify(prm);
let CLEAN = null;
function setClean(fn) { CLEAN = fn; }
function D(slot, seed, build) { return KIT.draw(UNIT_ID, seed, slot, build, it => !CLEAN || CLEAN(it)); }
const nz = (T, lo, hi) => T.until(() => T.ri(lo, hi), v => v !== 0);
const pm = (T, lo, hi) => T.ri(lo, hi) * (T.r() < 0.5 ? -1 : 1);
const big = (q, m) => qnum(qabs(qv(q))) > m;
/* ruling 43: the equations, systems and stories the lessons, the review and the practice paper show (read from the specs by
   verify.py, which also holds every generated set to them on its own) */
const SHOWN = (node ? require('./shown.js') : root.U11Shown) || { eq: [], sys: [], story: [] };
const SHOWN_EQ = new Set(SHOWN.eq), SHOWN_SYS = new Set(SHOWN.sys);
/* an equation's key: the sizes of its printed numbers, sorted, and its ending */
const printedNums = e => (eqT(e).replace(/[½⅓⅔¼¾⅕⅖⅗⅘]/g, c => '(' + Object.keys(GLYPH).find(k => GLYPH[k] === c) + ')').match(/\d+(?:\.\d+)?/g) || []).map(qdec);
function eqKey(e) {
  const nums = (eqT(e).replace(/[½⅓⅔¼¾⅕⅖⅗⅘]/g, c => '(' + Object.keys(GLYPH).find(k => GLYPH[k] === c) + ')').match(/\d+(?:\.\d+)?/g) || []).map(x => kstr(qdec(x))).sort(), en = e.L.concat(e.R).some(c => c.k === 'b') ? { kind: 'box' } : ending(e);
  return nums.join(',') + '|' + (en.kind === 'one' ? kstr(en.s) : en.kind);
}
const sysKey = (l1, l2) => [kstr(l1.m) + ',' + kstr(l1.b), kstr(l2.m) + ',' + kstr(l2.b)].sort().join(';');
const storyShown = nums => (SHOWN.story || []).some(set => { const pool = set.slice(); return nums.every(n => { const i = pool.indexOf(n); if (i < 0) return false; pool.splice(i, 1); return true; }); });
const shownEq = e => SHOWN_EQ.has(eqKey(e));
const shownSys = (l1, l2) => SHOWN_SYS.has(sysKey(l1, l2));
function numPart(o) { return Object.assign({ kind: 'num', label: '', stem: '' }, o); }
const shownLine = h => '<span class="shown">' + h + '</span>';           /* FAST's way: announce it, show it on its own line, then ask */
function eqItem(fam, slotPrm, e) {
  const v = e.v, part = numPart({ fam, prm: slotPrm, eq: e, v, ans: ending(e).s, key: keyOf(fam, slotPrm) });
  return { type: 'solo', stem: 'An equation is shown.' + shownLine(M(eqH(e))) + 'What value of ' + vi(v) + ' makes the equation true?', part, eq: e };
}

/* ---------- section 1: MA.8.AR.2.1, solving equations */
/* Q1 — like terms and one distribution: a(bn + c) ± dn = r, or dn + a(bn + c) = r */
function q1(seed) {
  return D('q1', seed, T => {
    const x = T.until(() => {
      const form = T.pick(['g+t', 'g-t', 't+g']), v = T.pick(LETTERS), a = T.ri(2, 6), b = T.ri(1, 5), c = pm(T, 1, 9), d = T.ri(1, 7), s = nz(T, -6, 10);
      const K = form === 'g-t' ? a * b - d : a * b + d;
      return { form, v, a, b, c, d, s, K, r: K * s + a * c };
    }, x => x.K >= 2 && x.r !== 0 && Math.abs(x.r) <= 90 && x.d !== x.a * x.b);
    const inner = [T_(x.b, x.v), T_(x.c)], g = G_(x.a, inner), dt = T_(x.form === 'g-t' ? -x.d : x.d, x.v);
    const e = { L: x.form === 't+g' ? [dt, g] : [g, dt], R: [T_(x.r)], v: x.v };
    if (shownEq(e)) return { bad: true };
    return eqItem('like', x, e);
  });
}
/* Q2 — variables on both sides, a negative solution: ah + b = ch + d (the larger number with the letter on either side) */
function q2(seed) {
  return D('q2', seed, T => {
    const x = T.until(() => {
      const v = T.pick(LETTERS), big1 = T.ri(3, 12), small = T.ri(1, big1 - 2), s = -T.ri(2, 12), b = pm(T, 1, 30), left = T.r() < 0.7;
      const [a, c] = left ? [big1, small] : [small, big1];
      const d = (a - c) * s + b, swapL = T.r() < 0.2, swapR = T.r() < 0.2;
      return { v, a, b, c, d, s, swapL, swapR };
    }, x => x.d !== 0 && Math.abs(x.d) <= 70 && x.b !== x.d);
    const L = [T_(x.a, x.v), T_(x.b)], R = [T_(x.c, x.v), T_(x.d)];
    const e = { L: x.swapL ? L.reverse() : L, R: x.swapR ? R.reverse() : R, v: x.v };
    if (shownEq(e)) return { bad: true };
    return eqItem('both', x, e);
  });
}
/* Q3 — parentheses on both sides, a fraction multiplying one of them (½, ⅓, ¼, ⅔, ¾ or a negative one): f(bm + q) = r(m + t).
   Every term the fraction multiplies comes out whole; the solution is whole, or a half */
const FRACS = ['1/2', '1/3', '1/4', '2/3', '3/4', '-1/2', '-1/3', '-1/4', '-2/3', '-3/4'];
function q3(seed) {
  return D('q3', seed, T => {
    const x = T.until(() => {
      const v = T.pick(LETTERS), f = T.pick(FRACS), F = qdec(f), dd = Number(F.d), b = dd * T.ri(1, 3), q = dd * pm(T, 1, 4), r = T.ri(2, 6) * (T.r() < 0.2 ? -1 : 1);
      const fb = qmul(F, Q(b)), fq = qmul(F, Q(q)), co = qsub(fb, Q(r)), s = T.r() < 0.85 ? Q(nz(T, -8, 10)) : Q(2 * T.ri(-5, 5) + 1, 2);
      const rt = qadd(fq, qmul(co, s)), t = qdiv(rt, Q(r)), side = T.r() < 0.5 ? 'L' : 'R';
      return { v, f, b, q, r, s: kstr(s), t: kstr(t), side, fb: kstr(fb), fq: kstr(fq) };
    }, x => { const t = qv(x.t), co = qsub(qv(x.fb), Q(x.r)); return co.n !== 0n && isInt(t) && t.n !== 0n && !big(t, 12) && !qeq(qv(x.fb), Q(1)); });
    const g1 = G_(x.f, [T_(x.b, x.v), T_(x.q)], true), g2 = G_(x.r, [T_(1, x.v), T_(x.t)]);
    const e = x.side === 'L' ? { L: [g1], R: [g2], v: x.v } : { L: [g2], R: [g1], v: x.v };
    if (shownEq(e)) return { bad: true };
    return eqItem('parens', x, e);
  });
}
/* Q4 — a decimal distributed (the lowest-scoring released Grade 8 FAST skill, 21%): k(av + b) = cv + d, k one of 0.2, 0.4,
   0.5, 1.5, 2.5 or a negative of one; ka and kb decimals of one place at most, most sets with one of them not whole; the
   answer whole or a half */
const DECK = ['0.2', '0.4', '0.5', '1.5', '2.5', '-0.2', '-0.4', '-0.5', '-1.5', '-2.5'];
function q4(seed) {
  return D('q4', seed, T => {
    const x = T.until(() => {
      const v = T.pick(LETTERS), k = T.pick(DECK), K = qdec(k), a = T.ri(1, 12), b = pm(T, 1, 30), c = pm(T, 1, 9);
      const ka = qmul(K, Q(a)), kb = qmul(K, Q(b)), co = qsub(ka, Q(c));
      const s = T.r() < 0.8 ? Q(nz(T, -10, 12)) : Q(2 * T.ri(-6, 6) + 1, 2);
      const d = qadd(qmul(co, s), kb);
      return { v, k, a, b, c, s: kstr(s), d: kstr(d), ka: kstr(ka), kb: kstr(kb) };
    }, x => { const ka = qv(x.ka), kb = qv(x.kb), d = qv(x.d), co = qsub(ka, Q(x.c));
      return places(ka) <= 1 && ka.n !== 0n && places(kb) <= 1 && (!isInt(ka) || !isInt(kb) || T.r() < 0.4) && co.n !== 0n && places(d) >= 0 && places(d) <= 1 && d.n !== 0n && !big(d, 60) && x.a !== 1 && !qeq(ka, ONE) && (isInt(qv(x.s)) || isInt(qmul(co, qv(x.s)))); });
    const e = { L: [G_(x.k, [T_(x.a, x.v), T_(x.b)])], R: [T_(x.c, x.v), T_(x.d)], v: x.v };
    if (shownEq(e)) return { bad: true };
    return eqItem('decimal', x, e);
  });
}
/* Q5 — how many solutions: three equations, one of each ending, in a random order; the one with one solution may be x = 0 */
function endEq(T, kind) {
  const X = 'x';
  if (kind === 'none') {
    const t = T.pick(['g+c', 't-g']);
    if (t === 'g+c') { const a = T.ri(2, 6), b = T.ri(1, 4), c = pm(T, 1, 8), d = pm(T, 1, 9), C = a * c + d; const e2 = T.until(() => pm(T, 1, 12), e => e !== C);
      return { L: [G_(a, [T_(b, X), T_(c)]), T_(d)], R: [T_(a * b, X), T_(e2)], v: X, t, prm: { a, b, c, d, e: e2 } }; }
    const p = T.ri(4, 9), a = T.ri(2, p - 1), c = pm(T, 1, 8), C = -a * c, e2 = T.until(() => T.r() < 0.5 ? a * c : pm(T, 1, 12), e => e !== C && e !== 0);
    return { L: [T_(p, X), G_(-a, [T_(1, X), T_(c)])], R: [T_(p - a, X), T_(e2)], v: X, t, prm: { p, a, c, e: e2 } };
  }
  if (kind === 'all') {
    const t = T.pick(['t-g', 'g+c', 'g=g']);
    if (t === 't-g') { const p = T.ri(4, 9), a = T.ri(2, p - 1), c = pm(T, 1, 8);
      return { L: [T_(p, X), G_(-a, [T_(1, X), T_(c)])], R: [T_(p - a, X), T_(-a * c)], v: X, t, prm: { p, a, c } }; }
    if (t === 'g+c') { const a = T.ri(2, 6), b = T.ri(1, 4), c = pm(T, 1, 8), d = pm(T, 1, 9), C = a * c + d;
      return C === 0 ? null : { L: [G_(a, [T_(b, X), T_(c)]), T_(d)], R: [T_(a * b, X), T_(C)], v: X, t, prm: { a, b, c, d } }; }
    const a = T.ri(2, 4), c = pm(T, 1, 6), m = T.pick([2, 3]);           /* m·a(x + c) = a(mx + mc): 6(x − 1) = 3(2x − 2) */
    return { L: [G_(a * m, [T_(1, X), T_(c)])], R: [G_(a, [T_(m, X), T_(m * c)])], v: X, t, prm: { a, c, m } };
  }
  const t = T.pick(['tt', 'g=tt']), s = T.r() < 0.35 ? 0 : nz(T, -6, 8);
  if (t === 'tt') { const a = T.ri(2, 9), c = T.ri(1, 7), b = pm(T, 1, 15), e2 = b + (a + c) * s;          /* ax + b = e − cx */
    return e2 === 0 ? null : { L: [T_(a, X), T_(b)], R: [T_(e2), T_(-c, X)], v: X, t, prm: { a, b, c, e: e2, s } }; }
  const a = T.ri(2, 5), b = T.ri(1, 3), c = pm(T, 1, 8), d = T.until(() => T.ri(1, 12), d => d !== a * b), e2 = (a * b - d) * s + a * c;
  return { L: [G_(a, [T_(b, X), T_(c)])], R: [T_(d, X), T_(e2)].filter(ch => ch.c.n !== 0n), v: X, t, prm: { a, b, c, d, e: e2, s } };
}
function q5(seed) {
  return D('q5', seed, T => {
    const order = T.shuffle(['one', 'none', 'all']), eqs = order.map(k => endEq(T, k));
    if (eqs.some(e => !e || shownEq(e))) return { bad: true };
    const parts = eqs.map((e, i) => { const en = ending(e), prm = Object.assign({ end: order[i], t: e.t }, e.prm);
      return { label: 'abc'[i], kind: 'mc', fam: 'endings', prm, eq: e, stem: M(eqH(e)), opts: ENDINGS.slice(), end: en, correct: ['one', 'none', 'all'].indexOf(order[i]), key: keyOf('endings', prm) }; });
    return { type: 'parts', stem: 'Each equation has one solution, no solution or infinitely many solutions. Which? If it has one solution, find it.', parts };
  });
}
/* Q6 — fill the box: no solution (the number multiplying x), or infinitely many (that number with the same constant, or the
   constant itself) */
function q6(seed) {
  return D('q6', seed, T => {
    const x = T.until(() => {
      const form = T.pick(['g-t', 'g+t', 't+g']), a = T.ri(2, 5), b = T.ri(1, 5), c = pm(T, 1, 9), d = T.ri(1, 6), goal = T.pick(['none', 'none', 'allx', 'allc']);
      const K = form === 'g-t' ? a * b - d : a * b + d, C = a * c;
      const e2 = goal === 'none' ? T.until(() => pm(T, 1, 12), e => e !== C) : C;
      return { form, a, b, c, d, goal, K, C, e: e2 };
    }, x => x.K >= 2 && x.d !== x.a * x.b && x.K !== Math.abs(x.C) && x.C !== 0);
    const X = 'x', g = G_(x.a, [T_(x.b, X), T_(x.c)]), dt = T_(x.form === 'g-t' ? -x.d : x.d, X);
    const L = x.form === 't+g' ? [dt, g] : [g, dt];
    const R = x.goal === 'allc' ? [T_(x.K, X), B_(null)] : [B_(X), T_(x.e)];
    const e = { L, R, v: X }, ans = Q(x.goal === 'allc' ? x.C : x.K);
    if (shownEq(e)) return { bad: true };
    const want = x.goal === 'none' ? 'no solution' : 'infinitely many solutions';
    return { type: 'solo', stem: 'Complete the equation so that it has ' + want + '. What number goes in the box?' + shownLine(M(eqH(e))), eq: e,
      part: numPart({ fam: 'box', prm: x, eq: e, v: null, ans, key: keyOf('box', x) }) };
  });
}
/* Q7 — two plans that cost the same: a fee and a smaller price each time, against a bigger price each time (and no fee, or a
   smaller fee). The count is whole and sensible in its story. */
const PLANS = [
  { id: 'storage', v: 'm', unit: 'months', one: 'month', n: [3, 12], a: [6, 40], fee: [20, 120],
    A: (f, a) => 'Storage company A charges ' + aDollar(f) + ' move-in fee and $' + a + ' a month.', B: (g, b) => 'Company B charges $' + b + ' a month and ' + (g ? aDollar(g) + ' move-in fee.' : 'no fee.'),
    ask: 'After how many months will the two companies have cost the same?', who: ['company A', 'company B'] },
  { id: 'gym', v: 'm', unit: 'months', one: 'month', n: [3, 12], a: [10, 45], fee: [25, 150],
    A: (f, a) => 'Gym A costs ' + aDollar(f) + ' sign-up fee and $' + a + ' a month.', B: (g, b) => 'Gym B costs $' + b + ' a month and ' + (g ? aDollar(g) + ' sign-up fee.' : 'has no sign-up fee.'),
    ask: 'After how many months will the two gyms have cost the same?', who: ['gym A', 'gym B'] },
  { id: 'pool', v: 'v', unit: 'visits', one: 'visit', n: [4, 15], a: [2, 9], fee: [12, 60],
    A: (f, a) => 'A pool pass costs $' + f + ' plus $' + a + ' a visit.', B: (g, b) => 'Without the pass, a visit costs $' + b + (g ? ' plus ' + aDollar(g) + ' one-time card fee.' : '.'),
    ask: 'After how many visits will the two ways have cost the same?', who: ['the pass', 'paying without it'] },
  { id: 'kayak', v: 'h', unit: 'hours', one: 'hour', n: [2, 8], a: [6, 25], fee: [8, 40],
    A: (f, a) => 'Shop A rents kayaks for ' + aDollar(f) + ' fee plus $' + a + ' an hour.', B: (g, b) => 'Shop B charges $' + b + ' an hour' + (g ? ' and ' + aDollar(g) + ' fee.' : ' and no fee.'),
    ask: 'After how many hours will the two shops have cost the same?', who: ['shop A', 'shop B'] },
  { id: 'art', v: 'c', unit: 'classes', one: 'class', n: [3, 12], a: [6, 20], fee: [15, 80],
    A: (f, a) => 'An art studio’s plan A costs $' + f + ' to join and $' + a + ' a class.', B: (g, b) => 'Plan B costs $' + b + ' a class' + (g ? ' and $' + g + ' to join.' : ' and nothing to join.'),
    ask: 'After how many classes will the two plans have cost the same?', who: ['plan A', 'plan B'] }
];
function aDollar(m) { return (/^(8|11|18|8\d)(\D|$)/.test(String(m)) ? 'an' : 'a') + ' $' + m; }
function q7(seed) {
  return D('q7', seed, T => {
    const x = T.until(() => {
      const ctx = T.ri(0, PLANS.length - 1), P = PLANS[ctx], n = T.ri(P.n[0], P.n[1]), a = T.ri(P.a[0], P.a[1]), gap = T.ri(1, Math.max(2, Math.round(a / 2)));
      const b = a + gap, g = T.r() < 0.3 ? T.ri(1, 4) * 5 : 0, f = g + gap * n;
      return { ctx, n, a, b, f, g };
    }, x => { const P = PLANS[x.ctx]; return x.f >= P.fee[0] && x.f <= P.fee[1] && x.f !== x.b && x.n !== x.a && x.n !== x.b && x.n !== x.f && x.n !== x.g && !Number.isInteger(x.f / x.b) && !storyShown([x.f, x.a, x.b].concat(x.g ? [x.g] : []).map(String)); });
    const P = PLANS[x.ctx], V = P.v;
    const e = { L: [T_(x.f), T_(x.a, V)], R: x.g ? [T_(x.g), T_(x.b, V)] : [T_(x.b, V)], v: V };
    return { type: 'solo', stem: P.A(x.f, x.a) + ' ' + P.B(x.g, x.b) + ' ' + P.ask, eq: e,
      part: numPart({ fam: 'plans', prm: x, eq: e, v: V, ans: Q(x.n), unit: P.unit, key: keyOf('plans', x) }) };
  });
}

/* ---------- section 2: MA.8.AR.4.1, solutions of a system */
const MS = [1, -1, 2, -2, 3, -3, 4, -4, 5];
/* a system y = m1x + b1, y = m2x + b2 with integer numbers multiplying x (1 and −1 among them, the two different), crossing at
   a whole-number point (x0, y0) inside the bounds */
function intSystem(T, o) {
  o = o || {};
  return T.until(() => {
    const m1 = T.pick(o.ms || MS), m2 = T.pick(o.ms || MS), x0 = T.ri(o.x[0], o.x[1]), y0 = T.ri(o.y[0], o.y[1]);
    return { m1, m2, x0, y0, b1: y0 - m1 * x0, b2: y0 - m2 * x0 };
  }, s => s.m1 !== s.m2 && s.b1 !== s.b2 && Math.abs(s.b1) <= (o.bmax || 12) && Math.abs(s.b2) <= (o.bmax || 12) && (!o.ok || o.ok(s)));
}
const sysLines = s => [L_(s.m1, s.b1), L_(s.m2, s.b2)];
const sysStem = (l1, l2) => M(lineH(l1)) + ' &nbsp;and&nbsp; ' + M(lineH(l2));
const sysShown = (l1, l2) => '<span class="shown">' + M(lineH(l1)) + '<br>' + M(lineH(l2)) + '</span>';
/* Q8 — select ALL the systems that have (a, b) as a solution: five systems, each solved for y; two or three have the pair as
   their solution (it is on both lines); each other system is true for the pair in exactly one of its two equations. The stem
   never says how many. */
function q8(seed) {
  return D('q8', seed, T => {
    const a = nz(T, -4, 5), b = T.until(() => T.ri(-8, 9), v => v !== a), k = T.pick([2, 3, 3]);
    const thru = m => L_(m, b - m * a);
    const sys = [];
    for (let g = 0; g < 400 && sys.length < 5; g++) {
      const right = sys.filter(z => z.ok).length < k, m1 = T.pick(MS), m2 = T.pick(MS);
      if (m1 === m2) continue;
      let l1 = thru(m1), l2 = thru(m2);
      if (!right) { const off = pm(T, 1, 5), which = T.r() < 0.5 ? 1 : 2; if (which === 1) l1 = L_(m1, b - m1 * a + off); else l2 = L_(m2, b - m2 * a + off); }
      if ([l1, l2].some(l => big(l.b, 12)) || shownSys(l1, l2)) continue;
      const key = sysKey(l1, l2); if (sys.some(z => z.key === key)) continue;
      sys.push({ l1, l2, ok: right, key });
    }
    if (sys.length !== 5) return { bad: true };
    const shown = T.shuffle(sys), prm = { a, b, sys: shown.map(z => z.key) };
    return { type: 'multi', fam: 'selSys', prm, pa: a, pb: b, systems: shown.map(z => [z.l1, z.l2]),
      stem: 'Select all the systems that have&nbsp; ' + M(pairH(Q(a), Q(b))) + ' &nbsp;as a solution.', opts: shown.map(z => sysStem(z.l1, z.l2)),
      correct: shown.map((z, i) => z.ok ? i : -1).filter(i => i >= 0), key: keyOf('selSys', prm) };
  });
}
/* Q9 — is (x, y) a solution? Four choices, each a verdict with a claim about THIS pair that can be checked: "Yes — it makes both
   equations true", "No — it makes only y = … true" (each equation), "No — it makes neither equation true". The four claims are
   the four ways a pair can sit (on both lines, on the first only, on the second only, on neither), so exactly one option is true
   for every pair; "Yes" goes only with both (14 Nov 2026: the old "Yes — it makes the first true" was true, word for word, of the
   solution itself — an arguable key). The pair is the solution, on one line only, or (about one set in seven) on neither. */
const ISSOL_RIGHT = { sol: 'both', first: 'only1', second: 'only2', neither: 'neither' };
function q9(seed) {
  return D('q9', seed, T => {
    const s = intSystem(T, { x: [-5, 6], y: [-8, 9], ok: s => s.x0 !== 0 });
    const [l1, l2] = sysLines(s);
    if (shownSys(l1, l2)) return { bad: true };
    const scen = T.pick(['first', 'first', 'second', 'second', 'sol', 'sol', 'neither']);
    let px = s.x0, py = s.y0;
    if (scen === 'first' || scen === 'second') { const l = scen === 'first' ? l1 : l2; px = T.until(() => T.ri(-5, 6), xx => xx !== s.x0 && Math.abs(qnum(yAt(l, xx))) <= 12); py = qnum(yAt(l, px)); }
    if (scen === 'neither') { px = T.until(() => T.ri(-5, 6), xx => xx !== s.x0); const y1 = qnum(yAt(l1, px)), y2 = qnum(yAt(l2, px));
      py = T.until(() => (T.r() < 0.5 ? y1 : y2) + pm(T, 1, 3), y => y !== y1 && y !== y2); if (Math.abs(py) > 12) return { bad: true }; }
    const eqOf = k => M(lineH(k === 1 ? l1 : l2));
    const O = { both: 'Yes — it makes both equations true.', only1: 'No — it makes only ' + eqOf(1) + ' true.', only2: 'No — it makes only ' + eqOf(2) + ' true.', neither: 'No — it makes neither equation true.' };
    const ids = T.shuffle(['both', 'only1', 'only2', 'neither']), right = ISSOL_RIGHT[scen];
    const prm = { m1: s.m1, b1: s.b1, m2: s.m2, b2: s.b2, px, py, scen, ids };
    return { type: 'mc', fam: 'isSol', prm, l1, l2, px, py, scen, ids,
      stem: 'Is&nbsp; ' + M(pairH(Q(px), Q(py))) + ' &nbsp;a solution of the system&nbsp; ' + sysStem(l1, l2) + '?',
      opts: ids.map(k => O[k]), correct: ids.indexOf(right), key: keyOf('isSol', prm) };
  });
}

/* ---------- section 3: MA.8.AR.4.2, how many solutions a system has (read from its graph) */
/* a window around the origin and the points that must show, every grid line one unit (or two up the side when it is tall) */
function windowFor(pts, o) {
  o = o || {};
  const xs = pts.map(p => p[0]).concat([0]), ys = pts.map(p => p[1]).concat([0]);
  const mx = o.mx == null ? 2 : o.mx, my = o.my == null ? 2 : o.my;
  return { x0: Math.min(...xs) - mx, x1: Math.max(...xs) + mx, y0: Math.min(...ys) - my, y1: Math.max(...ys) + my };
}
/* how much of a line lies in the window (its length in grid units) — every line drawn must cross a good part of it */
function inWindow(l, w) {
  const m = qnum(l.m), b = qnum(l.b), pts = [];
  for (const x of [w.x0, w.x1]) { const y = m * x + b; if (y >= w.y0 - 1e-9 && y <= w.y1 + 1e-9) pts.push([x, y]); }
  if (m !== 0) for (const y of [w.y0, w.y1]) { const x = (y - b) / m; if (x > w.x0 + 1e-9 && x < w.x1 - 1e-9) pts.push([x, y]); }
  if (pts.length < 2) return 0;
  pts.sort((p, q) => p[0] - q[0]); const a = pts[0], z = pts[pts.length - 1]; return Math.hypot(z[0] - a[0], (z[1] - a[1]) / (w.ys || 1));
}
const COUNTOPTS = ENDINGS.slice();
function q10(seed) {
  return D('q10', seed, T => {
    const s = intSystem(T, { ms: [1, -1, 2, -2, 3, -3, 0], x: [-4, 4], y: [-5, 6], bmax: 7, ok: s => !(s.x0 === 0 && s.y0 === 0) && !(s.m1 === 0 && s.b1 === 0) && !(s.m2 === 0 && s.b2 === 0) });
    if ((s.m1 === 0 || s.m2 === 0) && T.r() < 0.55) return { bad: true };       /* a horizontal line (y = 4) in about one set in six */
    const [l1, l2] = sysLines(s), w = windowFor([[s.x0, s.y0], [0, s.b1], [0, s.b2]], { mx: 2, my: 2 });
    if (w.x1 - w.x0 > 10 || w.y1 - w.y0 > 14 || inWindow(l1, w) < 4 || inWindow(l2, w) < 4 || shownSys(l1, l2)) return { bad: true };
    const prm = { m1: s.m1, b1: s.b1, m2: s.m2, b2: s.b2, w: [w.x0, w.x1, w.y0, w.y1] };
    return { type: 'mc', fam: 'countCross', prm, l1, l2, cross: { x: Q(s.x0), y: Q(s.y0) }, stem: 'The graphs of the system&nbsp; ' + sysStem(l1, l2) + ' &nbsp;are shown. How many solutions does the system have?',
      fig: { kind: 'plane', w, lines: [l1, l2], legend: [lineH(l1), lineH(l2)] }, opts: COUNTOPTS.slice(), correct: 0, key: keyOf('countCross', prm) };
  });
}
function q11(seed) {
  return D('q11', seed, T => {
    const same = T.r() < 0.45, m = T.pick([1, -1, 2, -2, 3, -3]);
    let l1, l2, prm;
    if (same) {                                       /* one line written two ways: y = a(x + c) + d and y = ax + (ac + d) */
      const c = pm(T, 1, 4), d = pm(T, 1, 6), b = m * c + d;
      if (b === 0 || Math.abs(b) > 7) return { bad: true };
      const alt = T.r() < 0.5;
      l1 = L_(m, b); l2 = Object.assign(L_(m, b), { alt: { a: m, c, d } });
      if (alt) { const t = l1; l1 = l2; l2 = t; }
      prm = { same, m, c, d, alt };
    } else {
      const b1 = pm(T, 1, 6), b2 = T.until(() => pm(T, 1, 6), z => Math.abs(z - b1) >= 2); l1 = L_(m, b1); l2 = L_(m, b2); prm = { same, m, b1, b2 };
    }
    const w = { x0: -3, x1: 3, y0: Math.min(-2, ...[l1, l2].map(l => qnum(l.b) - 3)), y1: Math.max(2, ...[l1, l2].map(l => qnum(l.b) + 3)) };
    if (w.y1 - w.y0 > 14 || inWindow(l1, w) < 4 || inWindow(l2, w) < 4 || shownSys(l1, l2)) return { bad: true };
    prm.w = [w.x0, w.x1, w.y0, w.y1];
    const stem = 'The graphs of the system&nbsp; ' + sysStem(l1, l2) + ' &nbsp;are shown. ' + (same ? 'Both equations graph as the one line shown. ' : '') + 'How many solutions does the system have?';
    return { type: 'mc', fam: 'countPar', prm, l1, l2, same, stem, fig: { kind: 'plane', w, lines: same ? [l1] : [l1, l2], legend: same ? [lineH(l1) + ' and ' + lineH(l2)] : [lineH(l1), lineH(l2)], both: same },
      opts: COUNTOPTS.slice(), correct: same ? 2 : 1, key: keyOf('countPar', prm) };
  });
}

/* ---------- section 4: MA.8.AR.4.3, solving systems by graphing */
function pairPart(o) { return Object.assign({ kind: 'pair', label: '', stem: '' }, o); }
/* Q12 — the solution read from a graph: a whole-number crossing, negative coordinates allowed; a half may multiply x */
function q12(seed) {
  return D('q12', seed, T => {
    const MQ = ['1', '-1', '2', '-2', '3', '-3', '1/2', '-1/2', '0'];
    const s = T.until(() => ({ m1: T.pick(MQ), m2: T.pick(MQ), x0: T.ri(-5, 6), y0: T.ri(-6, 6) }),
      s => s.m1 !== s.m2 && s.x0 !== s.y0 && s.x0 !== 0 && s.y0 !== 0 && (s.m1.indexOf('/') < 0 || s.x0 % 2 === 0) && (s.m2.indexOf('/') < 0 || s.x0 % 2 === 0));
    const l1 = L_(s.m1, qsub(Q(s.y0), qmul(qv(s.m1), Q(s.x0)))), l2 = L_(s.m2, qsub(Q(s.y0), qmul(qv(s.m2), Q(s.x0))));
    if (!isInt(l1.b) || !isInt(l2.b) || big(l1.b, 7) || big(l2.b, 7) || qeq(l1.b, l2.b)) return { bad: true };
    if ((l1.m.n === 0n || l2.m.n === 0n) && T.r() < 0.55) return { bad: true };
    const w = windowFor([[s.x0, s.y0], [0, qnum(l1.b)], [0, qnum(l2.b)]], { mx: 2, my: 2 });
    if (w.x1 - w.x0 > 12 || w.y1 - w.y0 > 14 || inWindow(l1, w) < 4 || inWindow(l2, w) < 4 || shownSys(l1, l2)) return { bad: true };
    const prm = { m1: kstr(l1.m), b1: kstr(l1.b), m2: kstr(l2.m), b2: kstr(l2.b), x0: s.x0, y0: s.y0, w: [w.x0, w.x1, w.y0, w.y1] };
    return { type: 'solo', stem: 'A system of equations is graphed:&nbsp; ' + sysStem(l1, l2) + '. What is the solution of the system? Give its x and its y.', l1, l2,
      fig: { kind: 'plane', w, lines: [l1, l2], legend: [lineH(l1), lineH(l2)] },
      part: pairPart({ fam: 'readGraph', prm, l1, l2, ans: [Q(s.x0), Q(s.y0)], key: keyOf('readGraph', prm), figw: w }) };
  });
}
/* Q13 — two tables of values: (a) the value missing from the first, (b) the solution, where the two tables agree */
function q13(seed) {
  return D('q13', seed, T => {
    const s = intSystem(T, { ms: [1, -1, 2, -2, 3, -3, 4], x: [1, 5], y: [-6, 9], bmax: 10 });
    const [l1, l2] = sysLines(s), xs = [0, 1, 2, 3, 4, 5];
    const miss = T.until(() => T.ri(1, 4), j => j !== s.x0);
    const y1 = xs.map(x => qnum(yAt(l1, x))), y2 = xs.map(x => qnum(yAt(l2, x)));
    if (y1.concat(y2).some(v => Math.abs(v) > 20) || shownSys(l1, l2)) return { bad: true };
    const prm = { m1: s.m1, b1: s.b1, m2: s.m2, b2: s.b2, miss };
    const fig = { kind: 'tables', xs, rows: [y1.map((v, i) => i === miss ? null : v), y2], titles: [lineH(l1), lineH(l2)] };
    return { type: 'parts', stem: 'The tables are for&nbsp; ' + sysStem(l1, l2) + '.', fig, l1, l2,
      parts: [numPart({ label: 'a', fam: 'tableGap', stem: 'What number is missing from the table for ' + M(lineH(l1)) + '?', prm, l1, l2, xs, miss, ans: Q(y1[miss]), key: keyOf('tableGap', prm) }),
        pairPart({ label: 'b', fam: 'tableSol', stem: 'What is the solution of the system?', prm, l1, l2, xs, miss, ans: [Q(s.x0), Q(s.y0)], key: keyOf('tableSol', prm) })] };
  });
}
/* Q14 — (a) a story with its graph, axes named and scaled: when the two are equal and what both equal, whole numbers on grid
   lines; (b) a second system whose point of intersection falls between the grid lines, estimated to the nearest tenth. The lead's
   ruling (14 Nov 2026), as the paper keys it: the key is the crossing rounded to the tenth in each coordinate, and a reading is
   right when each coordinate is within 0.1 of that rounded value, inclusive — (5/3, 8/3) is keyed (1.7, 2.7), and 1.6 to 1.8,
   2.6 to 2.8 are right. Each rounded coordinate is at least 0.2 from every grid and half-grid line the graph prints (it ends in
   .2, .3, .7 or .8), so no printed grid or half-grid point is ever inside the accepted range; the exact crossing is never a
   rounding tie (its hundredths never exactly 5). Each part has its own graph. */
/* a rounded coordinate at least 0.2 from every grid and half-grid line (in tenths: 2, 3, 7 or 8 past a whole), and an exact one
   that is no rounding tie (20·c an odd whole number would be one) */
function clearOfGrid(c) { const t = qmul(tenthOf(c), Q(10)), k = ((Number(t.n) % 5) + 5) % 5, tw = qmul(c, Q(20)); return isInt(t) && (k === 2 || k === 3) && !(isInt(tw) && tw.n % 2n !== 0n); }
const STORIES = [
  { id: 'saveSpend', unit: 'dollars', xname: 'weeks', yname: 'dollars', say: (A, B, s) => A + ' has $' + s.b1 + ' and saves $' + s.m1 + ' each week. ' + B + ' has $' + s.b2 + ' and spends $' + (-s.m2) + ' each week.',
    ask: (A, B) => 'After how many weeks will ' + A + ' and ' + B + ' have the same amount, and how much will each have?', amt: v => '$' + v, each: 'each', up: false },
  { id: 'saveSave', unit: 'dollars', xname: 'weeks', yname: 'dollars', say: (A, B, s) => A + ' has $' + s.b1 + ' and saves $' + s.m1 + ' each week. ' + B + ' has $' + s.b2 + ' and saves $' + s.m2 + ' each week.',
    ask: (A, B) => 'After how many weeks will ' + A + ' and ' + B + ' have the same amount, and how much will each have?', amt: v => '$' + v, each: 'each', up: true },
  { id: 'plants', unit: 'cm', xname: 'weeks', yname: 'centimeters', say: (A, B, s) => A + '’s plant is ' + s.b1 + ' cm tall and grows ' + s.m1 + ' cm each week. ' + B + '’s plant is ' + s.b2 + ' cm tall and grows ' + s.m2 + ' cm each week.',
    ask: (A, B) => 'After how many weeks will the two plants be the same height, and how tall will each be?', amt: v => v + ' cm', each: 'tall', up: true }
];
function q14(seed) {
  return D('q14', seed, T => {
    const st = T.pick(STORIES), [A, B] = T.shuffle(NAMES).slice(0, 2), ys = st.id === 'plants' ? T.pick([2, 5]) : T.pick([5, 10]);
    const x = T.until(() => {
      const x0 = T.ri(2, 9), y0 = ys * T.ri(2, 10), m1 = st.id === 'plants' ? T.ri(1, 6) : T.ri(2, 12), m2 = st.up ? T.ri(1, m1 - 1) : -T.ri(1, 12);
      return { x0, y0, m1, m2, b1: y0 - m1 * x0, b2: y0 - m2 * x0, ys };
    }, s => s.m2 !== 0 && s.m1 > s.m2 && s.b1 >= 0 && s.b2 > s.b1 && s.b1 % (st.id === 'plants' ? 1 : 5) === 0 && s.b2 % (st.id === 'plants' ? 1 : 5) === 0 &&
      s.b2 / ys <= 12 && s.y0 !== s.x0 && (st.up || s.b2 + s.m2 * (s.x0 + 2) >= 0) && (st.id !== 'plants' || s.b1 >= 2) && !storyShown([s.b1, s.m1, s.b2, Math.abs(s.m2)].map(String)));
    const l1 = L_(x.m1, x.b1), l2 = L_(x.m2, x.b2);
    const X1 = Math.min(12, Math.max(x.x0 + 2, 6)), wa = { x0: 0, x1: X1, y0: 0, y1: ys * Math.min(12, Math.max(Math.ceil(x.b2 / ys), x.y0 / ys + 2)), ys };
    if (inWindow(l1, wa) < 2 || inWindow(l2, wa) < 2) return { bad: true };
    /* part (b) (widened 15 Nov 2026 to well over Croix's floor of 100 versions on its own; ruling 49): the numbers multiplying x
       whole or halves (½, 3/2, 5/2), either sign, so the crossing's coordinates are thirds, fifths, sixths or sevenths; the
       crossing in any of the four quadrants, at least half a unit from both axes; x and y far enough apart that the swapped pair
       is never inside the tolerance. The window holds the origin and the crossing, a unit or more beyond it on every side. */
    const MB = ['1', '2', '3', '1/2', '3/2', '5/2', '-1', '-2', '-3', '-1/2', '-3/2', '-5/2'];
    const b = T.until(() => ({ m1: T.pick(MB), m2: T.pick(MB), b1: T.ri(-3, 5), b2: T.ri(-3, 7) }), b => {
      if (b.m1 === b.m2) return false;
      const p = L_(b.m1, b.b1), q = L_(b.m2, b.b2), c = meet(p, q); if (!c) return false;
      const X = qnum(c.x), Y = qnum(c.y);
      return Math.abs(X) >= 0.5 && Math.abs(X) < 4 && Math.abs(Y) >= 0.5 && Math.abs(Y) < 6 && clearOfGrid(c.x) && clearOfGrid(c.y) && [3n, 5n, 6n, 7n].includes(c.x.d) && [3n, 5n, 6n, 7n].includes(c.y.d) && Math.abs(X - Y) >= 0.5 && !shownSys(p, q); });
    const p = L_(b.m1, b.b1), q = L_(b.m2, b.b2), c = meet(p, q);
    const span = (v, least) => { let lo = Math.min(0, Math.floor(v) - 1), hi = Math.max(0, Math.ceil(v) + 1); while (hi - lo < least) { if (v >= 0) hi++; else lo--; } return [lo, hi]; };
    const [bx0, bx1] = span(qnum(c.x), 3), [by0, by1] = span(qnum(c.y), 4);
    const wb = { x0: bx0, x1: bx1, y0: by0, y1: by1, half: true };
    if (inWindow(p, wb) < 2 || inWindow(q, wb) < 2) return { bad: true };
    const prm = { st: st.id, A, B, x0: x.x0, y0: x.y0, m1: x.m1, b1: x.b1, m2: x.m2, b2: x.b2, ys, bm1: b.m1, bb1: b.b1, bm2: b.m2, bb2: b.b2 };
    const figA = { kind: 'plane', w: wa, lines: [l1, l2], legend: [A, B], xname: st.xname, yname: st.yname, story: true, title: 'PART (a): ' + A + ' and ' + B };
    const figB = { kind: 'plane', w: wb, lines: [p, q], legend: [lineH(p), lineH(q)], title: 'PART (b): a different system' };
    const pa = pairPart({ label: 'a', kind: 'story', fam: 'storyMeet', stem: 'The PART (a) graph shows ' + (st.id === 'plants' ? 'the height y, in centimeters, of each plant' : 'the dollars y each has') + ' after x weeks. ' + st.ask(A, B), prm, l1, l2, st, A, B, figw: wa, ans: [Q(x.x0), Q(x.y0)], key: keyOf('storyMeet', prm) });
    const pb = pairPart({ label: 'b', fam: 'estimate', stem: 'The PART (b) graph shows a different system,&nbsp; ' + sysStem(p, q) + '. Estimate its point of intersection to the nearest tenth.', fig: figB, prm, l1: p, l2: q, exact: c,
      ans: [tenthOf(c.x), tenthOf(c.y)], tol: Q(1, 10), key: keyOf('estimate', prm) });
    return { type: 'parts', stem: st.say(A, B, x), fig: figA, parts: [pa, pb] };
  });
}

function generate(seed) {
  if (!CLEAN) throw new Error('coach.js must be loaded before generating');
  return { seed, sections: [
    SECT(TITLES[0], [q1(seed), q2(seed), q3(seed), q4(seed), q5(seed), q6(seed), q7(seed)]),
    SECT(TITLES[1], [q8(seed), q9(seed)]),
    SECT(TITLES[2], [q10(seed), q11(seed)]),
    SECT(TITLES[3], [q12(seed), q13(seed), q14(seed)])] };
}
function partsOf(it) { return it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : [it]; }

const api = { clearOfGrid, ISSOL_RIGHT, printedNums, fracT, FRACS, sysShown, UNIT_ID, TITLES, NAMES, ENDINGS, PLANS, STORIES, Q, qadd, qsub, qmul, qdiv, qneg, qabs, qeq, qlt, qnum, qsign, isInt, places, decPlain, qdec, qv, kstr, numStr, N, nHtml, tenthOf,
  esc, fr, M, vi, speakH, pairH, pairT, T_, G_, B_, sideH, sideT, eqH, eqT, lin, fill, ending, evalSide, plainSide, substT, sideNums, sgnOf, absOf,
  L_, lineSide, lineH, lineT, onLine, yAt, meet, inWindow, readAns, readNum, parseNum, tidy, setClean, generate, partsOf, eqKey, sysKey, storyShown, ZERO, ONE };
if (node) module.exports = api; else root.Practice = api;
})(this);
