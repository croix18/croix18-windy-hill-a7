/* A7 Unit 5 practice (Multi-Step Proportional Relationships): exact numbers, reading what a student types, drawing the
   numbers, and the questions.

   Ruling 55 (Croix, 25 Oct 2026: "Yes I still want the interactive practice page on all the units regardless of review day
   or not."). Unit 5 was built before ruling 49, so its test is the printed Form A and Form B (Thu 5 Nov 2026), and this page
   is practice for them: the practice form's nineteen questions (a7/build/u5/unit.py), in its order and with its points —
   MA.7.GR.1.5 10, MA.7.AR.3.3 8, MA.7.AR.4.5 6 — and new numbers every set.
   - The transfer items stay off it (rulings 18 and 33): questions 8 and 19 are the practice form's bare versions — a plan's
     real area in square feet, and two speeds compared in one unit.
   - The test's numbers are not on the page (the kit's rule of 24 Oct 2026). The page never draws a question of Form A or
     Form B, and holds them only as hashes (FORMS_H: fnv1a of the unit, the slot and the slot's numbers); test_forms.js has
     the numbers, for the checks alone.
   - Ruling 43: never the numbers a lesson showed — 5.01–5.10's warm-ups, notes, worked examples and Your Turns, and the
     worked numbers of the unit's reference sheet (SHOWN, each with where it comes from).
   - Every conversion ratio is the FAST reference sheet's and no other (the unit's outline, decision 1), printed on the
     question that uses it; an exchange rate is printed and dated on the question (decision 2). */
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
const isInt = q => q.d === 1n;
function qdec(s) {                                    /* "8.3", ".25", "−4.5", "3,080" → exact */
  s = String(s).replace(/,/g, '').replace(/−/g, '-').trim();
  const m = /^(-?)(\d*)(?:\.(\d*))?$/.exec(s); if (!m || (m[2] === '' && !m[3])) throw new Error('not a decimal: ' + s);
  const fr = m[3] || '', v = Q(BigInt((m[2] || '0') + fr), 10n ** BigInt(fr.length));
  return m[1] ? qneg(v) : v;
}
const qv = x => typeof x === 'object' ? x : String(x).indexOf('/') > 0 ? Q(BigInt(String(x).split('/')[0]), BigInt(String(x).split('/')[1])) : qdec(String(x));
function qfloor(q) { let f = q.n / q.d; if (q.n < 0n && f * q.d !== q.n) f -= 1n; return Q(f); }
const qceil = q => { const f = qfloor(q); return qeq(f, q) ? f : Q(f.n + 1n); };
/* q ≥ 0 rounded half up to k decimal places, exactly */
const qround = (q, k) => { const s = 10n ** BigInt(k); return Q((2n * q.n * s + q.d) / (2n * q.d), s); };
function places(q) { let d = q.d, t = 0, f = 0; while (d % 2n === 0n) { d /= 2n; t++; } while (d % 5n === 0n) { d /= 5n; f++; } return d === 1n ? Math.max(t, f) : -1; }
function decPlain(q) {                               /* a terminating decimal written out, no commas, "-" for minus */
  const neg = q.n < 0n, a = qabs(q), k = places(a); if (k < 0) throw new Error('not terminating');
  let s = (a.n * (10n ** BigInt(k)) / a.d).toString();
  if (k > 0) { s = s.padStart(k + 1, '0'); s = s.slice(0, s.length - k) + '.' + s.slice(s.length - k); }
  return (neg ? '-' : '') + s;
}
function commas(s) { const p = s.split('.'); p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ','); return p.join('.'); }
/* how a number is shown: a decimal with commas (−, not -); a fraction that never ends as a/b */
function numStr(q) { try { const s = decPlain(q); return (s[0] === '-' ? '−' + commas(s.slice(1)) : commas(s)); } catch (e) { return (q.n < 0n ? '−' : '') + qabs(q).n + '/' + q.d; } }
const N = x => numStr(qv(x));
/* money to the cent: 55.20 */
function money(q) { const s = decPlain(qround(q, 2)), p = s.split('.'); return commas(p[0]) + '.' + ((p[1] || '') + '00').slice(0, 2); }
/* a value to k decimal places, shown with commas: 27.95 */
const fixed = (q, k) => { const s = decPlain(qround(q, k)), p = s.split('.'); return commas(p[0]) + (k ? '.' + ((p[1] || '') + '0'.repeat(k)).slice(0, k) : ''); };
/* three significant figures, trailing zeros dropped (the forms' choices: 64.5, 6.45, 0.093, 6.1) */
function sig3(q) {
  const f = qnum(q); if (!(f > 0)) throw new Error('sig3 of ' + f);
  const e = Math.floor(Math.log10(f)), k = Math.max(0, 2 - e);
  let r = qround(q, k); if (qnum(r) >= Math.pow(10, e + 1) && k > 0) r = qround(q, k - 1);
  return r;
}

/* ------------------------------------------------------------------ showing math (html) */
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const minus = s => String(s).replace(/^-/, '−');
const sup = e => '<sup>' + minus(e) + '</sup>';
function speakH(h) {                                                                  /* what a screen reader says for a piece of math */
  let t = String(h);
  for (let i = 0; i < 6; i++) { const t0 = t;
    t = t.replace(/<span class="fr"><span class="nu">((?:(?!<span class="fr">)[\s\S])*?)<\/span><span class="de">((?:(?!<span class="fr">)[\s\S])*?)<\/span><\/span>/, ' $1 over $2 ');
    if (t === t0) break; }
  t = t.replace(/<sup[^>]*>2<\/sup>/g, ' squared ').replace(/<sup[^>]*>(.*?)<\/sup>/g, ' to the $1 ').replace(/<[^>]+>/g, '').replace(/&nbsp;/g, ' ').replace(/&lt;/g, ' is less than ').replace(/&gt;/g, ' is greater than ');
  return t.replace(/≈/g, ' is about ').replace(/×|·/g, ' times ').replace(/÷/g, ' divided by ').replace(/−/g, ' minus ').replace(/\+/g, ' plus ').replace(/=/g, ' equals ').replace(/ : /g, ' to ').replace(/\s+/g, ' ').trim();
}
const M = h => '<span class="m" role="img" aria-label="' + esc(speakH(h)) + '">' + h + '</span>';
const fr = (n, d) => '<span class="fr"><span class="nu">' + n + '</span><span class="de">' + d + '</span></span>';
const K = '<i>k</i>';
/* a cup amount as printed: a whole number, or a mixed number with its fraction drawn (1½) — inside a math span */
function mixedH(q) {
  if (isInt(q)) return numStr(q);
  const w = q.n / q.d, r = q.n % q.d;
  return (w ? String(w) : '') + fr(String(r), String(q.d));
}
const mixedOut = q => isInt(q) ? numStr(q) : M(mixedH(q));
/* what a student types for one: "3 3/4" */
const mixedText = q => { if (isInt(q)) return String(q.n); const w = q.n / q.d, r = q.n % q.d; return (w ? w + ' ' : '') + r + '/' + q.d; };
const sqU = u => u + sup(2);                                                        /* cm² */

/* ------------------------------------------------------------------ reading what a student types */
const UNI = { '½': '1/2', '⅓': '1/3', '⅔': '2/3', '¼': '1/4', '¾': '3/4', '⅕': '1/5', '⅖': '2/5', '⅗': '3/5', '⅘': '4/5', '⅙': '1/6', '⅚': '5/6', '⅛': '1/8', '⅜': '3/8', '⅝': '5/8', '⅞': '7/8' };
function tidy(text) {
  let t = String(text == null ? '' : text).trim();
  t = t.replace(/[½⅓⅔¼¾⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞]/g, (c, i, s) => (i > 0 && /\d/.test(s[i - 1]) ? ' ' : '') + UNI[c]);
  t = t.replace(/\.\s*$/, '').trim();                                                  /* a sentence's full stop */
  t = t.replace(/^\s*(?:about|approximately|approx\.?|around|it is|it's|the answer is|so)\s+/i, '');
  t = t.replace(/^\s*(?:[a-z]{1,2}|scale factor|the scale factor)\s*[=≈~]\s*/i, '');   /* "k = 2.5", "k ≈ 3" */
  t = t.replace(/^\s*[≈~]\s*/, '');
  t = t.replace(/^\s*(?:US\s*)?\$\s*/i, '');                                          /* $50 */
  t = t.replace(/[−–—]/g, '-').replace(/[×✕✖·•⋅]/g, '*').replace(/÷/g, '/').replace(/\s+/g, ' ').trim();
  /* the unit typed after the number — "150 ft²", "6 cups of rice", "5 tanks", "118.80 Canadian dollars" */
  t = t.replace(/(\d|\))\s*[a-z][a-z .']*(?:\s*(?:\^\s*[23]|[²³]|[23]))?\s*$/i, '$1').trim();
  t = t.replace(/\s*(?:\^\s*[23]|[²³])\s*$/, '').trim();
  return t.replace(/\.\s*$/, '').trim();
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
    if ('+-*/()'.indexOf(ch) >= 0) { out.push({ t: ch }); i++; continue; }
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
      else if (peek() && peek().t === '(' && a.t !== 'neg') a = { t: 'mul', a, b: unary(), imp: true };
      else return a; }
    throw new Error('long'); }
  function unary() { if (eat('-')) return { t: 'neg', a: unary() }; if (eat('+')) return unary(); return atom(); }
  function atom() {
    const x = peek(); if (!x) throw new Error('end');
    if (x.t === 'n') { i++; return { t: 'n', s: x.s }; }
    if (eat('(')) { const e = expr(); if (!eat(')')) throw new Error(')'); return { t: 'par', a: e }; }
    throw new Error('token');
  }
  try { const e = expr(); if (i !== T.length) return { err: 'left' }; return { ast: e }; } catch (e) { return { err: 'syntax' }; }
}
function evalA(a) {
  switch (a.t) {
    case 'n': return qdec(a.s);
    case 'par': return evalA(a.a);
    case 'neg': return qneg(evalA(a.a));
    case 'add': return qadd(evalA(a.a), evalA(a.b));
    case 'sub': return qsub(evalA(a.a), evalA(a.b));
    case 'mul': return qmul(evalA(a.a), evalA(a.b));
    case 'div': return qdiv(evalA(a.a), evalA(a.b));
  }
  throw new Error('node');
}
const strip = a => a.t === 'par' ? strip(a.a) : a;
const UNREAD = 'I can’t read that. Type just your answer: one number.';                 /* no example number: a fixed example can be a test answer (the M7 Unit 9 review) */
/* returns {ok, val (exact), f, form: 'num' | 'expr', dp (a decimal's typed places), frac: 'reduced' | 'unreduced' (a typed
   fraction or mixed number), text}, or {ok: false, msg}, or {ok: false, blank: true} */
function readAns(text) {
  const raw = String(text == null ? '' : text);
  if (!raw.trim()) return { ok: false, blank: true };
  if (raw.length > 60) return { ok: false, msg: 'That is too long to read. Type just your answer.' };
  const t = tidy(raw);
  if (!t) return { ok: false, msg: UNREAD };
  const mx = /^(-?)(\d+)\s+(\d+)\s*\/\s*(\d+)$/.exec(t);                          /* a mixed number, "3 3/4" */
  if (mx && mx[4] !== '0') {
    const n = BigInt(mx[3]), d = BigInt(mx[4]), v = qadd(Q(BigInt(mx[2])), Q(n, d)), val = mx[1] ? qneg(v) : v;
    return { ok: true, val, f: qnum(val), form: 'num', frac: n < d && gcd(n, d) === 1n ? 'reduced' : 'unreduced', text: t };
  }
  const p = parse(t);
  if (p.err === 'comma') return { ok: false, msg: 'Use a period for a decimal point, and a comma only between thousands (1,200).' };
  if (p.err) {
    if (/\d\s+\d/.test(t) && !/[*/+()-]/.test(t)) return { ok: false, msg: 'I see two numbers with a space between them. Type one number.' };
    return { ok: false, msg: UNREAD };
  }
  let v; try { v = evalA(p.ast); } catch (e) { return { ok: false, msg: 'I can’t work that out. Type just your answer.' }; }
  const a = strip(p.ast), neg = a.t === 'neg', b = neg ? strip(a.a) : a;
  if (b.t === 'n') { const dp = (b.s.split('.')[1] || '').length; return { ok: true, val: v, f: qnum(v), form: 'num', dp, text: t }; }
  if (b.t === 'div' && strip(b.a).t === 'n' && strip(b.b).t === 'n' && /^\d+$/.test(strip(b.a).s) && /^\d+$/.test(strip(b.b).s)) {
    const n = BigInt(strip(b.a).s), d = BigInt(strip(b.b).s);
    if (d === 0n) return { ok: false, msg: 'I can’t work that out. Type just your answer.' };
    return { ok: true, val: v, f: qnum(v), form: 'num', frac: gcd(n, d) === 1n && d !== 1n ? 'reduced' : 'unreduced', text: t };
  }
  return { ok: true, val: v, f: qnum(v), form: 'expr', text: t };
}
/* a plain number (the Hint's number steps): "218", "14.8", "45/2", "3 3/4" */
function readNum(text) {
  let t = String(text == null ? '' : text).trim();
  if (/^[-−]?\d+,\d{1,2}$/.test(t)) t = t.replace(',', '.');
  const r = readAns(t); return r.ok && r.form === 'num' ? r.val : null;
}

/* ------------------------------------------------------------------ the test's numbers and the lessons' */
const UNIT_ID = 'a7u5';
const TITLES = ['Scale Drawings and Scale Factors', 'Converting Across Systems', 'Multi-Step Proportion Problems'];
/* Form A's and Form B's questions, as hashes of their keys (test_forms.js holds the keys, for the checks alone) */
const FORMS_H = new Set([4239484767, 2837177830, 139044301, 2184204111, 1302914821, 290696692, 2152079203, 739448613, 1688744384, 2570190403, 3966846063,
  2792902225, 3375333261, 688616626, 3368556427, 1113695078, 1664065641, 3556870265, 1121612771, 2168955169, 715148050, 3962122403,
  3648731241, 3720681723, 1210306353, 1817762460, 362610366, 2248392557, 3278486234, 1968082080, 1349065794, 1044563842, 2204907025,
  1010241049, 1380089430, 638670231, 4268681763, 21600968, 3150095142, 3744964789, 1639281084, 2849559658, 965266746, 1594133106,
  287992934, 73586690, 2591276607, 3330629757, 755727102, 3351778808, 3772581963, 1441647554, 3134299049, 3853315571, 4008987314,
  3554712862, 1222423396, 1296383387, 2379650209, 2642502206, 1090810885, 1197494877, 4244678955, 2052955913, 2305900126, 3832741786,
  3058466502, 2137796549, 2677546399, 1212558215]);
const formHash = (slot, key) => KIT.fnv1a(UNIT_ID + '|' + slot + '|' + key);
/* Ruling 43: what the class has been shown — a lesson's warm-up (its answers revealed), its notes, its worked examples and
   their Your Turns, and the worked numbers on the unit's reference sheet. The keys are the slots' (test_forms.js says how a
   key is written). */
const SHOWN_SRC = {
  sf: ['4>6', '6>9',              /* 5.01 Notes I (and its essential question): 6 by 4 copied at 9 by 6 */
       '6>15', '4>10', '8>12', '10>15',   /* 5.01 Example 1 (6 by 4 at 15 by 10) and its Your Turn (8 by 10 at 12 by 15) */
       '2>5', '2>3',              /* their k written as fractions, 5/2 and 3/2 (the check tuples) */
       '10>4',                    /* 5.01 Notes II */
       '20>8', '5>2', '5>3', '14>7', '2>1',   /* the 5.02, 5.04 and 5.06 warm-ups, and their k (2/5, ½) */
       '5>10', '3>6',             /* 5.02 Notes I: 5 by 3 at 10 by 6 */
       '12>30',                   /* 5.10 Notes III: k = 30/12 */
       '3>12', '2>10', '6>24', '2>6',   /* 5.02 Example 2 (k = 4: 3 × 4 = 12), its Your Turn (k = 5: 2 × 5 = 10), Example 1's sides at k = 4 and its Your Turn's at k = 3 */
       '12>3', '10>2', '24>6', '6>2'],   /* the same pairs run backwards, a reduction (the critic of 30 Oct 2026: question 2 drew 12 → 3) */
  sel3: ['1.5',                   /* 5.01 Notes I and the Your Turn of Example 1: k = 1.5, every angle still 90° */
         '2.5',                   /* 5.01 Example 1 */
         '2', '3', '4', '5',      /* 5.02 Notes I–III and Examples 2: k = 2, 3, 4 and 5 with the perimeter and the area */
         '0.4'],                  /* the reference sheet: a 10 cm side that becomes 4 cm has k = 0.4; angles do not change */
  rect: ['2,4|3', '3,6|4', '3,5|2',   /* 5.02 Example 1, its Your Turn, Notes I (5 by 3 at k = 2) */
         '4,6|1.5', '4,6|2.5', '8,10|1.5'],   /* 5.01 Notes I, Example 1 and its Your Turn: the copies' sides are on the board */
  rectWH: ['3,5',                 /* the 5.02 warm-up: the perimeter and the area of a 3 cm by 5 cm rectangle */
           '2,4', '3,6'],         /* 5.02 Example 1 and its Your Turn work the original's perimeter and area first */
  areaK: ['20>180', '15>240', '12>300',   /* 5.02 Notes III (and the reference sheet), Example 2, its Your Turn */
          '15>60',                /* 5.02 Notes II: A: 15 → 60 */
          '9>36', '7>63',         /* the 5.04 and 5.08 warm-ups: 9 cm² at k = 2, 7 cm² at k = 3 */
          '18>288',               /* 5.02 Example 1's Your Turn: 3 by 6 at k = 4 is 18 cm² → 288 cm² */
          '25>100'],              /* 5.02's higher-order question: areas 25 and 100 */
  room: ['4|2,2.5', '4|2.5,3', '4|1.5,4',   /* 5.04 Notes II, Example 1, its Your Turn (¼ in : 1 ft is 1 in : 4 ft) */
         '6|1.5,2'],              /* the reference sheet: 1.5 in by 2 in at 1 in : 6 ft */
  wall: ['4|2', '4|2.5', '4|3', '4|1.5', '4|4', '6|1.5', '6|2',   /* the same rooms' walls */
         '4|3.5'],                /* 5.04 Notes III: 14 ft is 3.5 in at ¼ in : 1 ft, run backwards */
  plan: ['4|14',                  /* 5.04 Notes III: 14 ÷ 4 = 3.5 in */
         '4|10'],                 /* the 5.06 warm-up: a 10-ft wall at ¼ in : 1 ft */
  conv: ['in>cm|10', 'in>cm|15', 'in>cm|25',   /* 5.06 Notes I, Example 1, its Your Turn */
         'in>cm|12',              /* the 5.08 warm-up */
         'cm>in|50',              /* 5.06 Notes II (and the reference sheet) */
         'lb>kg|50', 'lb>kg|70', 'lb>kg|90',   /* 5.08 Notes I, Example 1, its Your Turn */
         'gal>L|2',               /* 5.08 Notes I */
         'kg>lb|4',               /* the 5.10 warm-up */
         'km>mi|100',             /* 5.10 Notes II (and the reference sheet): 100 km/h × 0.62 */
         'mi>km|5', 'mi>km|4'],   /* 5.10 Example 1 and its Your Turn: 5 mi and 4 mi × 1.61 */
  chain: [],
  sqconv: ['ft2>m2|1',            /* 5.08 Notes II: 1 ft² ≈ 0.093 m² */
           'ft2>m2|20'],          /* the reference sheet: 20 ft² = 1.86 m² */
  curA: ['0.92|150', '0.92|80', '1.35|120',   /* 5.06 Notes III, Example 2, its Your Turn */
         '0.92|100', '0.92|50', '1.35|60'],   /* the same lines run backwards (92 euros ÷ 0.92 = $100; 46 euros = $50; 81 CAD = $60) */
  curB: ['0.92|92', '0.92|46', '1.35|81',
         '0.92|138', '0.92|73.6', '1.35|162'],   /* $150, $80 and $120 changed into the currency, run backwards */
  tank: ['23|17.5'], trip: ['23|17.5|1207'],   /* 5.10 Notes I (and the reference sheet) */
  recA: ['12|3/2|30', '8|5/2|20', '6|3/2|12'],   /* 5.10 Notes III, Example 2, its Your Turn */
  recB: ['8|5/2|5', '6|3/2|9/2'],
  recK: ['2.5|3/2', '2.5|5/2', '2|3/2'],   /* the same three: k × the cups (2.5 × 1½, 2.5 × 2½, 2 × 1½) */
  mix: ['1:2:3|1|4',              /* 5.10 Notes III: 1 : 2 : 3 with 4 gal of the first (the key: sorted parts | the known part's share | the amount) */
        '2:4:5|2|8'],             /* the reference sheet: 2 : 4 : 5 with 8 gal of white */
  speed: ['100|65']               /* 5.10 Notes II (and the reference sheet) */
};
/* the two papers that go home — the practice test, and the review (Tue 3 Nov, key Wed): a set never repeats one of their
   questions either, so every question on the page is new */
const HOME_SRC = {
  sf: ['4>12', '12>6', '5>8', '16>4', '6>9'], sel3: ['2'], rect: ['3,5|2', '4,6|0.5'], rectWH: ['3,5'], areaK: ['6>150', '10>160'],
  room: ['5|2,3', '6|1.5,2.5', '4|3,4'], wall: ['5|2', '4|3', '2|7.5'], plan: ['3|15', '6|21'],
  conv: ['in>cm|7', 'cm>in|110', 'kg>lb|35', 'gal>L|3', 'in>cm|14', 'cm>in|120', 'cm>in|40', 'km>mi|30', 'lb>kg|80', 'L>gal|40'],
  chain: ['yd>cm|1.5', 'yd>cm|6'], sqconv: ['in2>cm2|10', 'ft2>m2|8', 'm2>ft2|1.5'], curA: ['1.32|90', '0.92|150'], curB: ['1.32|66', '0.92|69'],
  tank: ['27|10', '29|12'], trip: ['27|10|1200', '29|12|800'], range: ['270', '348'], tripD: ['1200', '800'],
  amount: ['in/cm|7', 'in/cm|110', 'in/cm|14', 'in/cm|120', 'in/cm|40', 'in/cm|54', 'in/cm|216', 'lb/kg|35', 'lb/kg|80', 'gal/L|3', 'gal/L|40', 'mi/km|30', 'in2|10', 'ft2|8', 'm2|1.5'], speedM: ['45'], recA: ['5|2|15', '3|5/4|12'], recB: ['5|2|10', '3|5/4|10'], recK: ['3|2', '4|5/4'],
  mix: ['1:2:3|1|4', '1:2:5|5|10'], speed: ['80|45', '110|65']
};
const SHOWN = new Set([].concat(...[SHOWN_SRC, HOME_SRC].map(src => [].concat(...Object.keys(src).map(s => src[s].map(k => s + '|' + k))))));
const isForm = (slot, key) => FORMS_H.has(formHash(slot, key));
const isShown = (slot, key) => SHOWN.has(slot + '|' + key);
const fresh = fk => fk.every(([s, k]) => !isForm(s, k) && !isShown(s, k));

/* ------------------------------------------------------------------ building the questions */
const SECT = (title, items) => ({ title, items });
function numPart(label, fam, prm, stem, ans, extra) { return Object.assign({ label, fam, prm, stem, kind: 'num', ans, key: fam + JSON.stringify(prm), imode: extra && (extra.kind === 'frac' || extra.name) ? undefined : 'decimal' }, extra || {}); }
let CLEAN = null, FILL = null;
function setClean(fn, fill) { CLEAN = fn; FILL = fill || null; }
function D(slot, seed, build) {
  return KIT.draw(UNIT_ID, seed, slot, T => { const it = build(T); if (it && !it.bad && FILL) FILL(it); return it; }, it => !!it && !it.bad && fresh(it.fk || []) && (!CLEAN || CLEAN(it)));
}
const UNITS = { cm: ['cm', 'centimeter', 'centimeters'], in: ['in', 'inch', 'inches'], m: ['m', 'meter', 'meters'], ft: ['ft', 'foot', 'feet'] };
const rk = (a, b) => qlt(qv(b), qv(a)) ? N(b).replace(/,/g, '') + ',' + N(a).replace(/,/g, '') : N(a).replace(/,/g, '') + ',' + N(b).replace(/,/g, '');   /* two sides, smaller first */
const ks = q => decPlain(q);                                                           /* a number in a key */
const halves = (lo, hi) => { const out = []; for (let x = 2 * lo; x <= 2 * hi; x++) out.push(Q(x, 2)); return out; };

/* ---------- section 1: scale drawings and scale factors (MA.7.GR.1.5) */
/* the scale factor from one pair of sides, copy ÷ original: question 1 enlarges, question 2 shrinks */
function sfItem(T, slot, big) {
  const u = T.pick(['cm', 'cm', 'cm', 'm', 'ft']);
  /* k in quarters or fifths, as the forms' 2.5, 1.5, 0.4, 0.25 (a reduction in tenths too, for its versions): an enlargement
     from 1.2 to 6, a reduction from 0.2 to 0.8 */
  const nice = k => isInt(qmul(k, Q(4))) || isInt(qmul(k, Q(5))) || (!big && isInt(qmul(k, Q(10))));
  const [a, b] = big
    ? T.until(() => [T.ri(2, 20), T.ri(3, 60)], ([a, b]) => { const k = Q(b, a); return nice(k) && 5 * b >= 6 * a && b <= 6 * a; })
    : T.until(() => [T.ri(4, 60), T.ri(1, 59)], ([a, b]) => { const k = Q(b, a); return nice(k) && 5 * b <= 4 * a && 5 * b >= a; });
  const k = Q(b, a), prm = { a, b, u };
  return { type: 'solo', fk: [['sf', a + '>' + b]], stem: 'A ' + a + ' ' + u + ' side of a figure is ' + b + ' ' + u + ' in its scale copy. Find the scale factor.',
    part: numPart('', big ? 'kUp' : 'kDown', prm, '', k, { pre: 'k =' }) };
}
function q1(seed) { return D('q1', seed, T => sfItem(T, 'q1', true)); }
function q2(seed) { return D('q2', seed, T => sfItem(T, 'q2', false)); }
/* question 3 — FAST's multiselect: the statements are about k alone, as on the test, so its versions are its values of k */
const K3 = ['6', '7', '8', '9', '10', '3.5', '4.5', '0.5', '0.8', '1.2', '1.6'];
function q3(seed) {
  return D('q3', seed, T => {
    const k = qdec(T.pick(K3)), k2 = qmul(k, k), kS = N(k), k2S = N(k2);
    const all = [{ h: 'Each side is ' + kS + ' times as long.', tag: 'side', ok: true }, { h: 'Each angle is ' + kS + ' times as large.', tag: 'angle', ok: false },
      { h: 'The perimeter is ' + kS + ' times as long.', tag: 'perim', ok: true }, { h: 'The area is ' + kS + ' times as large.', tag: 'areaK', ok: false },
      { h: 'The area is ' + k2S + ' times as large.', tag: 'areaK2', ok: true }];
    const order = T.shuffle([0, 1, 2, 3, 4]), shown = order.map(i => all[i]);
    return { type: 'multi', fam: 'kFacts', prm: { k: kS }, fk: [['sel3', ks(k)]], stem: 'A figure is scaled by a scale factor of ' + kS + '. Select ALL of the statements that are true about the copy.',
      opts: shown.map(x => x.h), tags: shown.map(x => x.tag), correct: shown.map((x, i) => x.ok ? i : -1).filter(i => i >= 0), key: 'kFacts' + kS + '|' + order.join('') };
  });
}
const K4 = ['2', '3', '4', '5', '6', '1.5', '2.5'];
function q4(seed) {
  return D('q4', seed, T => {
    const u = T.pick(['cm', 'cm', 'in', 'ft', 'm']), k = qdec(T.pick(K4));
    const [w, h] = T.until(() => [T.ri(2, 12), T.ri(2, 12)], ([w, h]) => w !== h && qnum(qmul(Q(w * h), qmul(k, k))) <= 500);
    const P = qmul(Q(2 * (w + h)), k), A = qmul(Q(w * h), qmul(k, k)), prm = { w, h, k: N(k), u };
    return { type: 'parts', fk: [['rect', rk(w, h) + '|' + ks(k)], ['rectWH', rk(w, h)]],
      stem: 'A ' + w + ' ' + u + ' by ' + h + ' ' + u + ' rectangle is scaled by ' + M(K + ' = ' + N(k)) + '.',
      parts: [numPart('a', 'perim', prm, 'Find the copy’s perimeter.', P, { unit: u }), numPart('b', 'area', prm, 'Find the copy’s area.', A, { unit: u + '²' })] };
  });
}
function q5(seed) {
  return D('q5', seed, T => {
    const u = T.pick(['cm', 'cm', 'in', 'ft', 'm']);
    const [A, k] = T.until(() => [T.ri(2, 40), T.ri(2, 8)], ([A, k]) => A * k * k <= 1000);
    const B = A * k * k, prm = { A, B, u };
    return { type: 'solo', fk: [['areaK', A + '>' + B]],
      stem: 'A figure has area ' + M(A + ' ' + sqU(u)) + '. Its scale copy has area ' + M(N(Q(B)) + ' ' + sqU(u)) + '. What is the scale factor?',
      part: numPart('', 'kArea', prm, '', Q(k), { pre: 'k =' }) };
  });
}
/* a plan's scale: per 1 inch (1 in : 5 ft) or a fraction of an inch for some feet (¼ in : 1 ft, ½ in : 3 ft) — the
   rate r is the feet in 1 inch. 5.04: "A scale with two units is a rate: read it per 1 first." */
const PER1 = [2, 3, 4, 5, 6, 8, 10];
const PART = [[2, 1], [4, 1]];                                                        /* [the inch's denominator, the feet]: ½ in : 1 ft and ¼ in : 1 ft, the lessons' and the forms' (the educator of 30 Oct 2026: ½ in : 3 ft is on no paper) */
function scaleOf(T, fracShare) {
  if (T.r() < fracShare) { const [den, s] = T.pick(PART); return { den, s, r: den * s, h: fr('1', String(den)) + ' in : ' + s + ' ft' }; }
  const r = T.pick(PER1); return { den: 1, s: r, r, h: '1 in : ' + r + ' ft' };
}
function q6(seed) {
  return D('q6', seed, T => {
    const sc = scaleOf(T, 0.5), r = Q(sc.r), H = halves(1.5, 6);                        /* never a 1 in wall: its real length would be the rate itself */
    const [p, q] = T.until(() => [T.pick(H), T.pick(H)], ([p, q]) => { const a = qmul(p, r), b = qmul(q, r);
      return !qeq(p, q) && qnum(a) >= 4 && qnum(b) >= 4 && qnum(a) <= 40 && qnum(b) <= 40 && qnum(qmul(a, b)) <= 1200; });
    const a = qmul(p, r), b = qmul(q, r), prm = { den: sc.den, s: sc.s, r: sc.r, p: N(p), q: N(q) };
    return { type: 'parts', fk: [['room', sc.r + '|' + rk(p, q)], ['wall', sc.r + '|' + ks(p)]],
      stem: 'A floor plan is drawn at ' + M(sc.h) + '. A room is ' + N(p) + ' in by ' + N(q) + ' in on the plan.',
      parts: [numPart('a', 'wall', prm, 'Find the real length of the wall drawn ' + N(p) + ' in long.', a, { unit: 'ft' }),
        numPart('b', 'roomArea', prm, 'Find the room’s real area.', qmul(a, b), { unit: 'ft²' })] };
  });
}
function q7(seed) {
  return D('q7', seed, T => {
    const sc = scaleOf(T, 0.5);
    const L = T.until(() => T.ri(4, 60), L => { const d = Q(L, sc.r); return isInt(qmul(d, Q(4))) && qnum(d) > 1 && qnum(d) <= 12; });                    /* never 1 in: the wall would be the rate itself */
    const prm = { den: sc.den, s: sc.s, r: sc.r, L };
    return { type: 'solo', fk: [['plan', sc.r + '|' + L]], stem: 'A plan is drawn at ' + M(sc.h) + '. A real wall is ' + L + ' ft long. How long is it on the plan?',
      part: numPart('', 'toPlan', prm, '', Q(L, sc.r), { unit: 'in' }) };
  });
}
/* question 8 — the practice form's bare version of transfer item 1: a plan's real area, in square feet */
function q8(seed) {
  return D('q8', seed, T => {
    const r = T.ri(2, 12), H = halves(1.5, 6), R = Q(r);                                 /* no 1 in side: the kit's hint for 1 × r states its product */
    const [p, q] = T.until(() => [T.pick(H), T.pick(H)], ([p, q]) => { const a = qmul(p, R), b = qmul(q, R);
      return !qeq(p, q) && qnum(a) >= 4 && qnum(b) >= 4 && qnum(a) <= 45 && qnum(b) <= 45 && qnum(qmul(a, b)) <= 1500 && (!isInt(p) || !isInt(q)); });
    const prm = { den: 1, s: r, r, p: N(p), q: N(q) };
    return { type: 'solo', fk: [['room', r + '|' + rk(p, q)]],
      stem: 'A plan is drawn at ' + M('1 in : ' + r + ' ft') + '. A room is ' + N(p) + ' in by ' + N(q) + ' in on the plan. Find the room’s real area.',
      part: numPart('', 'planArea', prm, '', qmul(qmul(p, R), qmul(q, R)), { unit: 'ft²' }) };
  });
}

/* ---------- section 2: converting across systems (MA.7.AR.3.3) */
/* the FAST reference sheet's pairs: [customary, metric, metric in 1 customary, customary in 1 metric, the words] */
const PAIRS = {
  'in/cm': { a: 'in', b: 'cm', ab: '2.54', ba: '0.39', A: 'inches', B: 'centimeters' },
  'mi/km': { a: 'mi', b: 'km', ab: '1.61', ba: '0.62', A: 'miles', B: 'kilometers' },
  'lb/kg': { a: 'lb', b: 'kg', ab: '0.454', ba: '2.204', A: 'pounds', B: 'kilograms' },
  'gal/L': { a: 'gal', b: 'L', ab: '3.785', ba: '0.264', A: 'gallons', B: 'liters' },
  'ft/m': { a: 'ft', b: 'm', ab: '0.305', ba: '3.28', A: 'feet', B: 'meters' },
  'c/L': { a: 'c', b: 'L', ab: '0.24', ba: '4.23', A: 'cups', B: 'liters' },
  'oz/g': { a: 'oz', b: 'g', ab: '28.35', ba: '0.0352', A: 'ounces', B: 'grams' }
};
const ratioH = (u1, v, u2) => '1 ' + u1 + ' = ' + v + ' ' + u2;
/* a one-step conversion with the ratio printed (questions 9, 12 and 13). alt: the sheet's other ratio's answer, which earns
   the point too ("Both directions are on the sheet, and both are accepted." — the unit's reference sheet) */
function convPart(n, P, toMetric, fam) {
  const f = toMetric ? qdec(P.ab) : qdec(P.ba), o = toMetric ? qdec(P.ba) : qdec(P.ab);
  const from = toMetric ? P.a : P.b, to = toMetric ? P.b : P.a;
  return numPart('', fam, { n, pair: P.a + '/' + P.b, from, to, f: decPlain(f), o: decPlain(o) }, '', qmul(Q(n), f), { unit: to, alt: qdiv(Q(n), o), altRatio: ratioH(to, decPlain(o), from) });
}
function q9(seed) {
  return D('q9', seed, T => {
    const n = T.ri(2, 150), P = PAIRS['in/cm'];
    return { type: 'solo', fk: [['conv', 'in>cm|' + n], ['amount', 'in/cm|' + n]], stem: M(ratioH('in', '2.54', 'cm')) + '. How many centimeters is ' + n + ' in?', part: convPart(n, P, true, 'convIn') };
  });
}
function q10(seed) {
  return D('q10', seed, T => {
    const pk = T.pick(Object.keys(PAIRS)), P = PAIRS[pk], toCust = T.r() < 0.6;          /* the test asks the customary unit in a metric amount */
    const n = pk === 'oz/g' && toCust ? 10 * T.ri(5, 60) : T.ri(10, 200);
    const from = toCust ? P.b : P.a, to = toCust ? P.a : P.b, toW = toCust ? P.A : P.B;
    /* the four ways to use the two ratios; two are right: × the ratio whose 1 is the unit you have, ÷ the one whose 1 is the
       unit you want */
    const ways = [{ op: '×', v: P.ab, tag: toCust ? 'mulWrong' : 'mulRight' }, { op: '×', v: P.ba, tag: toCust ? 'mulRight' : 'mulWrong' },
      { op: '÷', v: P.ab, tag: toCust ? 'divRight' : 'divWrong' }, { op: '÷', v: P.ba, tag: toCust ? 'divWrong' : 'divRight' }];
    const order = T.shuffle([0, 1, 2, 3]), shown = order.map(i => ways[i]);
    const prm = { n, pair: pk, from, to, toW, ab: P.ab, ba: P.ba, ops: shown.map(w => w.op + w.v) };
    return { type: 'multi', fam: 'convSel', prm, fk: [['conv', from + '>' + to + '|' + n], ['amount', pk + '|' + n]],
      stem: M(ratioH(P.a, P.ab, P.b)) + ' and ' + M(ratioH(P.b, P.ba, P.a)) + '. Select ALL of the expressions that give the number of ' + toW + ' in ' + n + ' ' + from + '.',
      opts: shown.map(w => M(n + ' ' + w.op + ' ' + w.v)), tags: shown.map(w => w.tag), correct: shown.map((w, i) => /Right/.test(w.tag) ? i : -1).filter(i => i >= 0),
      key: 'convSel' + JSON.stringify([pk, toCust, n]) + '|' + order.join('') };
  });
}
/* question 11 — a chain of three ratios, yards to centimeters (the reference sheet: "Yards to centimeters goes through feet
   and inches") */
function q11(seed) {
  return D('q11', seed, T => {
    const u = T.r(), n = u < 0.5 ? Q(T.ri(2, 80)) : u < 0.8 ? Q(2 * T.ri(1, 30) + 1, 2) : Q(4 * T.ri(1, 10) + T.pick([1, 3]), 4);   /* never 1 yd or ½ yd: the chain's first step would be the ratio itself */
    const prm = { n: N(n) }, inches = qmul(n, Q(36));
    return { type: 'solo', fk: [['chain', 'yd>cm|' + ks(n)], ['amount', 'in/cm|' + ks(inches)]],
      stem: M(ratioH('yd', '3', 'ft')) + ', ' + M(ratioH('ft', '12', 'in')) + ', ' + M(ratioH('in', '2.54', 'cm')) + '. How many centimeters is ' + N(n) + ' yd?',
      part: numPart('', 'chain', prm, '', qmul(inches, qdec('2.54')), { unit: 'cm', alt: qdiv(inches, qdec('0.39')), altRatio: ratioH('cm', '0.39', 'in') }) };
  });
}
function q12(seed) {
  return D('q12', seed, T => {
    const n = T.ri(2, 150), P = PAIRS['lb/kg'], toKg = T.r() < 0.4;                    /* Form A asks pounds, Form B kilograms */
    const part = convPart(n, P, toKg, 'convMass');
    return { type: 'solo', fk: [['conv', (toKg ? 'lb>kg|' : 'kg>lb|') + n], ['amount', 'lb/kg|' + n]],
      stem: (toKg ? M(ratioH('lb', '0.454', 'kg')) + '. How many kilograms is ' + n + ' lb?' : M(ratioH('kg', '2.204', 'lb')) + '. How many pounds is ' + n + ' kg?'), part };
  });
}
function q13(seed) {
  return D('q13', seed, T => {
    const n = T.ri(2, 150), P = PAIRS['gal/L'];
    return { type: 'solo', fk: [['conv', 'gal>L|' + n], ['amount', 'gal/L|' + n]], stem: M(ratioH('gal', '3.785', 'L')) + '. How many liters is ' + n + ' gal?', part: convPart(n, P, true, 'convVol') };
  });
}
/* question 14 — a square unit across systems: the length ratio used twice */
const SQ = [
  { from: 'in', to: 'cm', r: '2.54', o: '0.39', words: 'square centimeters', things: ['tile', 'photo', 'sticker', 'card'] },
  { from: 'ft', to: 'm', r: '0.305', o: '3.28', words: 'square meters', things: ['patio', 'rug', 'deck', 'garden bed'] },
  { from: 'm', to: 'ft', r: '3.28', o: '0.305', words: 'square feet', things: ['floor', 'stage', 'garden', 'wall'] },
  { from: 'cm', to: 'in', r: '0.39', o: '2.54', words: 'square inches', things: ['poster', 'map', 'drawing', 'window'] },
  { from: 'mi', to: 'km', r: '1.61', o: '0.62', words: 'square kilometers', things: ['lake', 'park', 'forest', 'town'] },
  { from: 'km', to: 'mi', r: '0.62', o: '1.61', words: 'square miles', things: ['lake', 'park', 'forest', 'town'] }
];
function q14(seed) {
  return D('q14', seed, T => {
    const S0 = T.pick(SQ), A = S0.from === 'cm' ? 10 * T.ri(10, 300) : T.ri(2, 60), thing = T.pick(S0.things), r = qdec(S0.r);
    const exact = qmul(Q(A), qmul(r, r));
    const all = [{ v: sig3(exact), tag: 'ok' }, { v: sig3(qmul(Q(A), r)), tag: 'once' }, { v: sig3(qmul(r, r)), tag: 'alone' }, { v: sig3(qmul(Q(2 * A), r)), tag: 'double' }];
    const order = T.shuffle([0, 1, 2, 3]), shown = order.map(i => all[i]);
    const prm = { from: S0.from, to: S0.to, r: S0.r, o: S0.o, A, thing, vals: shown.map(x => decPlain(x.v)) };
    const art = /^[aeiou]/.test(thing) ? 'An ' : 'A ';
    return { type: 'mc', fam: 'sqConv', prm, fk: [['sqconv', S0.from + '2>' + S0.to + '2|' + A], ['amount', S0.from + '2|' + A]],
      stem: M(ratioH(S0.from, S0.r, S0.to)) + '. ' + art + thing + ' is ' + M(N(Q(A)) + ' ' + sqU(S0.from)) + ' in area. Which is closest to its area in ' + S0.words + '?',
      opts: shown.map(x => M(numStr(x.v) + ' ' + sqU(S0.to))), tags: shown.map(x => x.tag), vals: shown.map(x => x.v), exact, correct: order.indexOf(0),
      key: 'sqConv' + JSON.stringify([S0.from, A]) + '|' + order.join('') };
  });
}
/* question 15 — an exchange rate, printed and dated on the question (decision 2: never a real rate) */
const CUR = [
  { name: 'euros', lo: 85, hi: 95, scale: 100 }, { name: 'Canadian dollars', lo: 125, hi: 140, scale: 100 }, { name: 'British pounds', lo: 74, hi: 82, scale: 100 },
  { name: 'Australian dollars', lo: 145, hi: 160, scale: 100 }, { name: 'Mexican pesos', lo: 68, hi: 80, scale: 4 }, { name: 'Japanese yen', lo: 140, hi: 155, scale: 1 }
];
function q15(seed) {
  return D('q15', seed, T => {
    const C0 = T.pick(CUR), r = Q(T.ri(C0.lo, C0.hi), C0.scale);
    const d = 5 * T.ri(2, 40);
    const Dl = T.until(() => T.ri(10, 150), Dl => places(qmul(r, Q(Dl))) <= 1);
    const c = qmul(r, Q(Dl)), prm = { cur: C0.name, r: decPlain(r), d, c: decPlain(c) };
    return { type: 'parts', fk: [['curA', decPlain(r) + '|' + d], ['curB', decPlain(r) + '|' + decPlain(c)]],
      stem: 'Rate on Nov 5: ' + M('1 US dollar = ' + N(r)) + ' ' + C0.name + '.',   /* the name outside the math, so the line wraps on a phone (the reviews of 30 Oct 2026) */
      parts: [numPart('a', 'toCur', prm, 'How many ' + C0.name + ' is $' + d + '?', qmul(Q(d), r), { unit: C0.name, money: places(r) > 0 }),
        numPart('b', 'toUsd', prm, 'How many US dollars is ' + (isInt(c) ? N(c) : money(c)) + ' ' + C0.name + '?', Q(Dl), { pre: '$' })] };
  });
}

/* ---------- section 3: multi-step proportion problems (MA.7.AR.4.5) */
function q16(seed) {
  return D('q16', seed, T => {
    const veh = m => m <= 22 ? T.pick(['truck', 'pickup', 'van']) : m <= 32 ? T.pick(['car', 'van', 'minivan']) : T.pick(['car', 'hybrid', 'compact car']);
    const m = T.ri(15, 40), g = m <= 22 ? T.ri(18, 26) : m <= 32 ? T.ri(13, 20) : T.ri(10, 14), R = m * g;   /* a big tank with low mileage, a small one with high (the educator of 30 Oct 2026) */
    const Dm = T.until(() => 50 * T.ri(6, 60), Dm => { const x = Dm / R, f = x - Math.floor(x); return x >= 1.15 && x <= 6.85 && f >= 0.15 && f <= 0.85; });
    const prm = { veh: veh(m), m, g, D: Dm };
    return { type: 'parts', fk: [['tank', m + '|' + g], ['trip', m + '|' + g + '|' + Dm], ['range', String(R)], ['tripD', String(Dm)]],   /* never a form's range or trip either (the critic of 30 Oct 2026) */
      stem: 'A ' + prm.veh + ' gets ' + m + ' miles per gallon and its tank holds ' + g + ' gal.',
      parts: [numPart('a', 'range', prm, 'How far does it go on a full tank?', Q(R), { unit: 'mi' }),
        numPart('b', 'tanks', prm, 'It makes a ' + N(Q(Dm)) + '-mi trip. How many tanks of gas does the trip use? (Part of a tank counts as a whole tank.)', qceil(Q(Dm, R)), { unit: 'tanks' })] };
  });
}
const CUPS = ['5/4', '3/2', '7/4', '2', '9/4', '5/2', '3', '7/2'];
function q17(seed) {
  return D('q17', seed, T => {
    const food = T.pick(['rice', 'flour', 'oatmeal', 'milk', 'broth', 'pasta']);
    const s = T.ri(2, 12), c = qv(T.pick(CUPS));
    /* k = t ÷ s a decimal that ends, as the forms' 2.5, 1.5 and 3 */
    const t = T.until(() => T.ri(2, 40), t => { const a = qdiv(qmul(c, Q(t)), Q(s)); return t !== s && places(Q(t, s)) >= 0 && places(Q(t, s)) <= 2 && isInt(qmul(a, Q(4))) && qnum(a) <= 20 && qnum(a) >= 1; });
    const h = T.until(() => Q(T.ri(4, 40), 2), h => { const sv = qmul(qdiv(h, c), Q(s)), rc = qdiv(h, c); return isInt(sv) && qnum(sv) >= 2 && qnum(sv) <= 60 && !qeq(sv, Q(s)) && qnum(h) > qnum(c) && places(rc) >= 0 && places(rc) <= 2; });
    const A = qdiv(qmul(c, Q(t)), Q(s)), Bs = qmul(qdiv(h, c), Q(s));
    const prm = { food, s, c: c.n + '/' + c.d, t, h: h.n + '/' + h.d };
    /* recK: part (a)'s computation, k × the cups — 5.10 Notes III's 2.5 × 1½ is the same problem at any yields */
    return { type: 'parts', fk: [['recA', s + '|' + (isInt(c) ? c.n : c.n + '/' + c.d) + '|' + t], ['recB', s + '|' + (isInt(c) ? c.n : c.n + '/' + c.d) + '|' + (isInt(h) ? h.n : h.n + '/' + h.d)],
      ['recK', decPlain(Q(t, s)) + '|' + (isInt(c) ? c.n : c.n + '/' + c.d)]],
      stem: 'A recipe for ' + s + ' servings uses ' + mixedOut(c) + ' cups of ' + food + '.',
      parts: [numPart('a', 'scaleUp', prm, 'How much ' + food + ' for ' + t + ' servings?', A, { unit: 'cups', cups: true, kind: 'frac' }),
        numPart('b', 'servings', prm, 'With ' + mixedOut(h) + ' cups on hand, how many servings can be made?', Bs, { unit: 'servings' })] };
  });
}
const MIX = [
  { what: 'Paint', names: null, unit: 'gal', words: 'gallons' },
  { what: 'Juice', names: ['orange', 'mango', 'water'], unit: 'cups', words: 'cups' },
  { what: 'Punch', names: ['lemonade', 'cranberry juice', 'ginger ale'], unit: 'cups', words: 'cups' },
  { what: 'Concrete', names: ['cement', 'sand', 'gravel'], unit: 'buckets', words: 'buckets' }
];
const ORD = ['first', 'second', 'third'];
/* a mixture's key: its parts sorted, the share of the part that is known, and the amount — so the same mixture with its
   colors in another order is the same question (the educator review of 30 Oct 2026: Form A's 3 : 2 : 4 with 9 cups of the
   3-part came up as 3 : 4 : 2 with 9 buckets of cement) */
const mixKey = (parts, which, n) => parts.slice().sort((a, b) => a - b).join(':') + '|' + parts[which] + '|' + n;
function q18(seed) {
  return D('q18', seed, T => {
    const X = T.pick(MIX);
    const parts = T.until(() => [T.ri(1, 6), T.ri(1, 6), T.ri(1, 6)], p => !(p[0] === p[1] && p[1] === p[2]) && p[0] + p[1] + p[2] >= 5 && p[0] + p[1] + p[2] <= 15 && gcd(gcd(BigInt(p[0]), BigInt(p[1])), BigInt(p[2])) === 1n);
    const which = T.ri(0, 2), k = T.ri(2, 8), n = parts[which] * k, sum = parts[0] + parts[1] + parts[2];
    const prm = { what: X.what, names: X.names, unit: X.unit, parts, which, n };
    const rat = M(parts.join(' : '));
    const stem = X.names
      ? X.what + ' is mixed ' + X.names.join(' : ') + ' = ' + rat + '. A batch uses ' + n + ' ' + X.unit + ' of ' + X.names[which] + '. How many ' + X.words + ' is the whole batch?'
      : X.what + ' is mixed ' + rat + '. A batch uses ' + n + ' ' + X.unit + ' of the ' + ORD[which] + ' color. How many ' + X.words + ' is the whole batch?';
    return { type: 'solo', fk: [['mix', mixKey(parts, which, n)]], stem, part: numPart('', 'mixWhole', prm, '', Q(k * sum), { unit: X.unit }) };
  });
}
/* question 19 — the practice form's bare version of transfer item 2: two speeds, one in km/h and one in mi/h, compared in one
   unit. On paper it is written; here the student types the faster one's name and the mi/h speed changed to km/h — the
   decision and the conversion that proves it (the educator of 30 Oct 2026: as a choice question, the vehicle named in the
   right option gave it away in nine sets of ten). The mi/h speed is never a form's (speedM). */
const MOVERS = [{ a: 'train', b: 'bus', ka: [60, 130], mb: [35, 75] }, { a: 'car', b: 'truck', ka: [50, 120], mb: [30, 75] }, { a: 'cyclist', b: 'scooter', ka: [15, 35], mb: [10, 22] }];
function q19(seed) {
  return D('q19', seed, T => {
    const V = T.pick(MOVERS), trap = T.r() < 0.5;                                     /* half the sets: the bigger number is the slower one */
    const [kmh, mph] = T.until(() => [T.ri(V.ka[0], V.ka[1]), T.ri(V.mb[0], V.mb[1])], ([k, m]) => { const c = m * 1.61;
      return Math.abs(k - c) >= 2 && k !== m && ((k > m) !== (k > c)) === trap; });
    const conv = qmul(Q(mph), qdec('1.61')), fast = qlt(conv, Q(kmh)) ? V.a : V.b;
    const prm = { a: V.a, b: V.b, kmh, mph, trap, fast };
    return { type: 'solo', fk: [['speed', kmh + '|' + mph], ['speedM', String(mph)]],
      stem: M(ratioH('mi', '1.61', 'km')) + '. A ' + V.a + ' does ' + kmh + ' km/h; a ' + V.b + ' does ' + mph + ' mi/h. Which is faster? Type its name, and the ' + V.b + '’s speed in km/h.',
      part: numPart('', 'faster', prm, '', conv, { unit: 'km/h', name: true, alt: qdiv(Q(mph), qdec('0.62')), altRatio: ratioH('km', '0.62', 'mi') }) };
  });
}

function generate(seed) {
  if (!CLEAN) throw new Error('coach.js must be loaded before generating');
  return { seed, sections: [
    SECT(TITLES[0], [q1(seed), q2(seed), q3(seed), q4(seed), q5(seed), q6(seed), q7(seed), q8(seed)]),
    SECT(TITLES[1], [q9(seed), q10(seed), q11(seed), q12(seed), q13(seed), q14(seed), q15(seed)]),
    SECT(TITLES[2], [q16(seed), q17(seed), q18(seed), q19(seed)])] };
}
function partsOf(it) { return it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : [it]; }
/* the key as printed beside a typed part: the number (money to the cent, cups as a mixed number) and its unit */
function ansStr(p) { return p.money ? money(p.ans) : p.cups ? null : numStr(p.ans); }
function ansHtml(p) {
  const v = p.cups ? M(mixedH(p.ans)) : M(ansStr(p));
  return (p.name ? 'the ' + esc(p.prm.fast) + ', ' : '') + (p.pre === '$' ? '$' : p.pre ? M(K + ' =') + ' ' : '') + v + (p.unit ? ' ' + esc(p.unit) : '');
}

const api = { UNIT_ID, TITLES, Q, qadd, qsub, qmul, qdiv, qneg, qabs, qeq, qlt, qnum, qdec, qv, qfloor, qceil, qround, isInt, places, decPlain, numStr, N, commas, money, fixed, sig3,
  esc, M, speakH, fr, sup, minus, K, mixedH, mixedOut, mixedText, sqU, tidy, parse, evalA, readAns, readNum, setClean, generate, partsOf, ansStr, ansHtml,
  PAIRS, SQ, CUR, MIX, ORD, MOVERS, PER1, PART, K3, K4, CUPS, mixKey, SHOWN_SRC, HOME_SRC, SHOWN, FORMS_H, formHash, isForm, isShown, fresh, ratioH };
if (node) module.exports = api; else root.Practice = api;
})(this);
