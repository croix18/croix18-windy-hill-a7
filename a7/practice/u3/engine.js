/* A7 Unit 3 practice test engine: question generators, exact arithmetic, a reader for typed answers,
   and the marking rules. Runs in the page and under Node (the checks in test_engine.js and verify.py). */
(function (root) {
'use strict';
const KIT = (typeof module !== 'undefined' && module.exports) ? require('../kit/core.js') : root.Kit;

/* ------------------------------------------------------------------ exact rationals */
function gcd(a, b) { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) { const t = a % b; a = b; b = t; } return a; }
function Q(n, d) {
  n = BigInt(n); d = d === undefined ? 1n : BigInt(d);
  if (d === 0n) throw new Error('division by zero');
  if (d < 0n) { n = -n; d = -d; }
  const g = gcd(n, d) || 1n;
  return { n: n / g, d: d / g };
}
const qadd = (a, b) => Q(a.n * b.d + b.n * a.d, a.d * b.d);
const qsub = (a, b) => Q(a.n * b.d - b.n * a.d, a.d * b.d);
const qmul = (a, b) => Q(a.n * b.n, a.d * b.d);
const qdiv = (a, b) => { if (b.n === 0n) throw new Error('division by zero'); return Q(a.n * b.d, a.d * b.n); };
const qeq = (a, b) => a.n === b.n && a.d === b.d;
const qlt = (a, b) => a.n * b.d < b.n * a.d;
function qpow(a, k) {                       // k: BigInt
  if (k < 0n) { if (a.n === 0n) throw new Error('0 to a negative power'); return qpow(Q(a.d, a.n), -k); }
  if (k === 0n && a.n === 0n) throw new Error('0 to the zero power');
  if (k > 400n) throw new Error('exponent too large');
  let r = Q(1); for (let i = 0n; i < k; i++) r = qmul(r, a); return r;
}
function qdec(s) {                          // "8.3", ".25", "290000" → exact
  const m = /^(\d*)(?:\.(\d*))?$/.exec(s);
  if (!m || (m[1] === '' && (m[2] === undefined || m[2] === ''))) throw new Error('not a number: ' + s);
  const f = m[2] || '';
  return Q(BigInt((m[1] || '0') + f), 10n ** BigInt(f.length));
}
function decStr(q) {                        // a terminating decimal, written out in full
  let neg = q.n < 0n, n = neg ? -q.n : q.n, d = q.d, two = 0, five = 0;
  while (d % 2n === 0n) { d /= 2n; two++; }
  while (d % 5n === 0n) { d /= 5n; five++; }
  if (d !== 1n) throw new Error('not a terminating decimal');
  const k = Math.max(two, five);                       // n/d = n·2^(k−two)·5^(k−five) / 10^k
  n *= 2n ** BigInt(k - two) * 5n ** BigInt(k - five);
  let s = n.toString();
  if (k > 0) { s = s.padStart(k + 1, '0'); s = s.slice(0, s.length - k) + '.' + s.slice(s.length - k); s = s.replace(/0+$/, '').replace(/\.$/, ''); }
  return (neg ? '-' : '') + s;
}
function commas(s) { const p = s.split('.'); p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ','); return p.join('.'); }

/* ------------------------------------------------------------------ expressions (one tree: drawn, written out, evaluated) */
const N = (x, opt) => { const s = typeof x === 'string' ? x : String(x); return Object.assign({ t: 'n', s, q: qdec(s) }, opt || {}); };
const V = s => ({ t: 'v', s });
const P = (b, e) => ({ t: 'pow', b: typeof b === 'object' ? b : N(b), e: typeof e === 'object' ? e : (e < 0 ? Neg(N(-e)) : N(e)) });
const Mul = (op, ...xs) => ({ t: 'mul', op, xs });
const Fr = (n, d) => ({ t: 'frac', n: typeof n === 'object' ? n : N(n), d: typeof d === 'object' ? d : N(d) });
const Neg = x => ({ t: 'neg', x: typeof x === 'object' ? x : N(x) });
const Par = x => ({ t: 'par', x });
const Eq = (l, r) => ({ t: 'eq', l, r });
const Sci = (c, k) => Mul('×', N(c), P(10, k));
const Ar = (a, op, b) => ({ t: 'ar', op, a: typeof a === 'object' ? a : (a < 0 ? Par(Neg(N(-a))) : N(a)), b: typeof b === 'object' ? b : (b < 0 ? Par(Neg(N(-b))) : N(b)) });   // arithmetic shown in an exponent: 4 + 5, 2 × 3, 9 − (−2)

function evalA(a, env) {
  switch (a.t) {
    case 'n': return a.q;
    case 'v': if (!env || !(a.s in env)) throw new Error('letter'); return env[a.s];
    case 'pow': {
      const e = evalA(a.e, env); if (e.d !== 1n) throw new Error('exponent not whole');
      return qpow(evalA(a.b, env), e.n);
    }
    case 'mul': return a.xs.reduce((r, x) => qmul(r, evalA(x, env)), Q(1));
    case 'frac': case 'div': return qdiv(evalA(a.t === 'frac' ? a.n : a.a, env), evalA(a.t === 'frac' ? a.d : a.b, env));
    case 'neg': return qmul(Q(-1), evalA(a.x, env));
    case 'par': return evalA(a.x, env);
    case 'add': return a.op === '+' ? qadd(evalA(a.a, env), evalA(a.b, env)) : qsub(evalA(a.a, env), evalA(a.b, env));
    case 'ar': { const x = evalA(a.a, env), y = evalA(a.b, env); return a.op === '+' ? qadd(x, y) : a.op === '−' ? qsub(x, y) : a.op === '×' ? qmul(x, y) : (() => { throw new Error('op'); })(); }
    default: throw new Error('cannot evaluate ' + a.t);
  }
}
function hasFrac(a) { if (!a || typeof a !== 'object') return false; if (a.t === 'frac') return true; return ['b', 'e', 'x', 'n', 'd', 'l', 'r', 'a'].some(k => a[k] && typeof a[k] === 'object' && hasFrac(a[k])) || (a.xs || []).some(hasFrac); }
function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }
function html(a) {
  switch (a.t) {
    case 'n': return esc(a.commas ? commas(a.s) : a.s);
    case 'v': return '<i>' + esc(a.s) + '</i>';
    case 'pow': {
      const wrap = ['neg', 'frac', 'mul', 'pow', 'add'].includes(a.b.t);
      const base = wrap ? html(Par(a.b)) : html(a.b);
      const tall = (a.b.t === 'par' || wrap) && hasFrac(a.b);
      return base + '<sup' + (tall ? ' class="tall"' : '') + '>' + html(a.e) + '</sup>';
    }
    case 'mul': return a.xs.map(x => (x.t === 'add' || x.t === 'neg' && a.op === '') ? html(Par(x)) : html(x)).join(a.op === '' ? '' : '<span class="op">' + a.op + '</span>');
    case 'frac': return '<span class="fr"><span class="nu">' + html(a.n) + '</span><span class="de">' + html(a.d) + '</span></span>';
    case 'neg': return '−' + (a.x.t === 'add' ? html(Par(a.x)) : html(a.x));
    case 'par': return hasFrac(a.x) ? '<span class="bp">(</span>' + html(a.x) + '<span class="bp">)</span>' : '(' + html(a.x) + ')';
    case 'eq': return html(a.l) + '<span class="rel">=</span>' + html(a.r);
    case 'ar': return html(a.a) + '<span class="op">' + a.op + '</span>' + html(a.b);
    default: throw new Error('cannot draw ' + a.t);
  }
}
/* what a screen reader says (Apple review R1-8) */
function speak(a) {
  switch (a.t) {
    case 'n': return String(a.commas ? commas(a.s) : a.s).replace(/,/g, '');
    case 'v': return a.s;
    case 'pow': { const e = a.e.t === 'n' ? a.e.s : null; return speak(a.b) + (e === '2' ? ' squared' : e === '3' ? ' cubed' : ' to the power ' + speak(a.e)); }
    case 'mul': return a.xs.map(speak).join(' times ');
    case 'frac': return speak(a.n) + ' over ' + speak(a.d);
    case 'neg': return 'negative ' + speak(a.x);
    case 'par': return 'open paren ' + speak(a.x) + ' close paren';
    case 'eq': return speak(a.l) + ' equals ' + speak(a.r);
    case 'ar': return speak(a.a) + ({ '+': ' plus ', '−': ' minus ', '×': ' times ' })[a.op] + speak(a.b);
    case 'add': return speak(a.a) + (a.op === '+' ? ' plus ' : ' minus ') + speak(a.b);
  }
  return '';
}
const M = a => { let sp = ''; try { sp = speak(a); } catch (e) {} return '<span class="m"' + (sp ? ' role="img" aria-label="' + esc(sp) + '"' : '') + '>' + html(a) + '</span>'; };
function plain(a) {               // for the independent check in Python (sympy syntax)
  switch (a.t) {
    case 'n': return a.s;
    case 'v': return a.s;
    case 'pow': return '(' + plain(a.b) + ')**(' + plain(a.e) + ')';
    case 'mul': return '(' + a.xs.map(plain).join(')*(') + ')';
    case 'frac': return '((' + plain(a.n) + ')/(' + plain(a.d) + '))';
    case 'neg': return '(-(' + plain(a.x) + '))';
    case 'par': return '(' + plain(a.x) + ')';
    case 'eq': return 'Eq(' + plain(a.l) + ', ' + plain(a.r) + ')';
    case 'ar': return '((' + plain(a.a) + ')' + ({ '+': '+', '−': '-', '×': '*' })[a.op] + '(' + plain(a.b) + '))';
    default: throw new Error('cannot write ' + a.t);
  }
}

/* ------------------------------------------------------------------ reading what a student typed */
function tidy(s, xTimes) {
  s = String(s).trim();
  const sup = { '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁻': '-' };
  s = s.replace(/[⁰¹²³⁴-⁹⁻]+/g, m => '^' + m.split('').map(c => sup[c]).join(''));
  s = s.replace(/[−–—]/g, '-').replace(/[×·⋅]/g, '*').replace(/÷/g, '/').replace(/\*\*/g, '^');
  s = s.replace(/\btimes\s*(larger|bigger|greater|as\s+large|as\s+big)?\b/gi, '').trim();
  if (xTimes) s = s.replace(/[xX*]\s*$/, '').replace(/\s*[xX]\s*/g, '*');
  s = s.replace(/(\d),(?=\d{3}\b)/g, '$1');          // 290,000 → 290000
  s = s.replace(/(\d) +(?=\d{3}(?!\d))/g, '$1');      // 290 000 → 290000
  for (let k = 0; k < 20 && /\.\d* +\d/.test(s); k++) s = s.replace(/(\.\d*) +(?=\d)/, '$1');   // 0.000 0071 → 0.0000071
  return s.trim().replace(/\.$/, '');
}
function tokenize(s) {
  const out = []; let i = 0;
  while (i < s.length) {
    const c = s[i];
    if (c === ' ') { i++; continue; }
    if (/[0-9.]/.test(c)) { let j = i; while (j < s.length && /[0-9.]/.test(s[j])) j++; out.push({ k: 'n', s: s.slice(i, j) }); i = j; continue; }
    if (/[a-zA-Z]/.test(c)) { out.push({ k: 'v', s: c.toLowerCase() === c ? c : c.toLowerCase() }); i++; continue; }
    if ('^*/()+-'.indexOf(c) >= 0) { out.push({ k: c }); i++; continue; }
    if (c === '[' || c === '{') { out.push({ k: '(' }); i++; continue; }
    if (c === ']' || c === '}') { out.push({ k: ')' }); i++; continue; }
    throw new Error('unexpected ' + c);
  }
  return out;
}
function parse(src, xTimes) {
  const toks = tokenize(tidy(src, xTimes)); let i = 0;
  if (!toks.length) throw new Error('empty');
  const peek = () => toks[i] && toks[i].k, take = k => { if (peek() !== k) throw new Error('expected ' + k); return toks[i++]; };
  function expr() { let a = term(); while (peek() === '+' || peek() === '-') { const op = toks[i++].k; a = { t: 'add', op, a, b: term() }; } return a; }
  function startsFactor() { const k = peek(); return k === 'n' || k === 'v' || k === '('; }
  function term() {
    let a = unary(), divided = false;
    for (;;) {
      if (peek() === '*') { if (divided) throw new Error('ambiguous'); i++; a = mulOf(a, unary()); }
      else if (peek() === '/') { if (divided) throw new Error('ambiguous'); i++; a = { t: 'div', a, b: unary() }; divided = true; }
      else if (startsFactor()) {                                 // 27a^6, 4n^2
        if (divided) throw new Error('ambiguous');               // 4/m^6n^2: is n^2 on the bottom? ask for parentheses
        const last = a.t === 'mul' ? a.xs[a.xs.length - 1] : a;
        if (peek() === 'n' && last.t === 'n') throw new Error('two numbers');   // "1 8/27": never read as 1 × 8/27
        a = mulOf(a, power(), true);
      }
      else return a;
    }
  }
  function mulOf(a, b, implicit) { return { t: 'mul', op: implicit ? '' : '*', xs: (a.t === 'mul' ? a.xs : [a]).concat([b]) }; }
  function unary() { if (peek() === '-') { i++; return { t: 'neg', x: unary() }; } if (peek() === '+') { i++; return unary(); } return power(); }
  function power() { const b = atom(); if (peek() === '^') { i++; return { t: 'pow', b, e: unary() }; } return b; }
  function atom() {
    const k = peek();
    if (k === 'n') { const s = toks[i++].s; return N(s.startsWith('.') ? '0' + s : s); }
    if (k === 'v') return V(toks[i++].s);
    if (k === '(') { i++; const a = expr(); take(')'); return { t: 'par', x: a }; }
    throw new Error('unexpected');
  }
  const a = expr();
  if (i !== toks.length) throw new Error('left over');
  return a;
}
const unwrap = a => { while (a && a.t === 'par') a = a.x; return a; };
function walk(a, f) { if (!a || typeof a !== 'object') return; f(a); for (const k of ['a', 'b', 'e', 'x', 'n', 'd']) if (a[k] && typeof a[k] === 'object' && a[k].t) walk(a[k], f); (a.xs || []).forEach(x => walk(x, f)); }
function anyNode(a, pred) { let hit = false; walk(a, n => { if (pred(n)) hit = true; }); return hit; }
const hasPow = a => anyNode(a, n => n.t === 'pow');
const hasVar = a => anyNode(a, n => n.t === 'v');
function hasNegExp(a) { return anyNode(a, n => { if (n.t !== 'pow') return false; try { return evalA(n.e, {}).n < 0n; } catch (e) { return true; } }); }
function vars(a) { const s = new Set(); walk(a, n => { if (n.t === 'v') s.add(n.s); }); return [...s]; }

/* single monomial, simplified: one number on top (and at most one below), each letter once, a power of a letter only */
function monoProblem(a, posOnly) {
  a = unwrap(a);
  const num = [], den = [], seen = {};
  let problem = null, divs = 0, topLetters = 0;
  const say = p => { problem = problem || p; };
  function factor(f, top) {
    f = unwrap(f);
    if (f.t === 'mul') return f.xs.forEach(x => factor(x, top));
    if (f.t === 'div') { if (++divs > 1) say('fraction'); factor(f.a, top); factor(f.b, !top); return; }
    if (f.t === 'n') { (top ? num : den).push(f); return; }
    if (f.t === 'v') { if (seen[f.s]) say('combine'); seen[f.s] = 1; if (top) topLetters++; return; }
    if (f.t === 'pow') {
      const b = unwrap(f.b);
      if (b.t === 'v') {
        if (seen[b.s]) say('combine'); seen[b.s] = 1; if (top) topLetters++;
        const e = literalInt(f.e);
        if (e === null) { say('exponent'); return; }
        if (e === 0n) { say('zero'); return; }
        if ((posOnly || !top) && e < 0n) say('negative');
        return;
      }
      if (b.t === 'n') { say('number'); return; }
      say('distribute'); return;
    }
    say('read');
  }
  factor(a, true);
  if (!problem && (num.length > 1 || den.length > 1 || (num.length && den.length) || den.some(d => qeq(d.q, Q(1))))) problem = 'number';
  if (!problem && num.length === 1 && qeq(num[0].q, Q(1)) && topLetters > 0) problem = 'one';
  return problem;
}
/* an exponent written as a plain whole number: 5, −3, (−3) → BigInt; anything else (2+3, 12/2, 1.5) → null */
function literalInt(x) {
  x = unwrap(x); let neg = false;
  if (x.t === 'neg') { neg = true; x = unwrap(x.x); }
  if (x.t !== 'n' || x.q.d !== 1n) return null;
  return neg ? -x.q.n : x.q.n;
}
function isSci(a) {
  a = unwrap(a);
  const ten = x => { x = unwrap(x); if (x.t !== 'pow' || unwrap(x.b).t !== 'n' || !qeq(unwrap(x.b).q, Q(10))) return null; return literalInt(x.e) === null ? null : true; };
  if (ten(a)) return { c: Q(1) };
  if (a.t !== 'mul' || a.xs.length !== 2) return null;
  let c = unwrap(a.xs[0]), p = a.xs[1];
  if (!ten(p)) { c = unwrap(a.xs[1]); p = a.xs[0]; }
  if (!ten(p) || c.t !== 'n') return null;
  return { c: c.q };
}

/* a finished value: a whole number, a decimal, or a fraction of whole numbers in lowest terms (a sign allowed) */
function valueProblem(a) {
  const strip = x => { x = unwrap(x); return x.t === 'neg' ? unwrap(x.x) : x; };
  const u = strip(a);
  if (u.t === 'n') return null;
  if (u.t === 'div') {
    const n = strip(u.a), d = strip(u.b);
    if (n.t !== 'n' || d.t !== 'n') return 'finish';
    if (n.q.d !== 1n || d.q.d !== 1n) return 'finish';
    if (d.q.n === 1n) return 'over1';
    if (gcd(n.q.n, d.q.n) !== 1n) return 'lowest';
    return null;
  }
  return 'finish';
}

/* ------------------------------------------------------------------ marking one typed answer */
const SAMPLE = [Q(2), Q(3), Q(5), Q(7), Q(11), Q(13), Q(17), Q(19), Q(23), Q(29), Q(31), Q(37)];
function envFor(letters, k) { const e = {}; letters.forEach((v, i) => { e[v] = qadd(SAMPLE[(i * 5 + k * 3) % SAMPLE.length], Q(k, 7)); }); return e; }
function sameValue(typed, want, letters) {
  if (!letters.length) return qeq(evalA(typed, {}), evalA(want, {}));
  for (let k = 0; k < 4; k++) { const env = envFor(letters, k); if (!qeq(evalA(typed, env), evalA(want, env))) return false; }
  return true;
}
const UNREAD = 'I can’t read that. Type a power with ^ and a fraction with /, like 4^8 or 1/6^3.';
const AMBIG = 'Use parentheses to show what is on the bottom of the fraction, like 5/(3x^2) or (4n^2)/m^6.';
function readOne(src, xTimes) {
  try { return { a: parse(src, xTimes) }; }
  catch (e) { return { err: e.message === 'ambiguous' ? AMBIG : UNREAD }; }
}
function mark(part, text) {
  try { return markInner(part, text); }
  catch (e) { return { v: 'unread', msg: UNREAD }; }             // anything unexpected (a very long input, say) is "can't read", never a mark
}
function markInner(part, text) {
  const raw = String(text || '').trim();
  if (!raw) return { v: 'blank' };
  if (raw.length > 60) return { v: 'unread', msg: 'That is too long to read. Type just your answer.' };
  const xT = part.kind === 'sci' || part.kind === 'std' || part.kind === 'times' || !vars(part.ans).length;   // no letters in the answer: x can only mean times
  let segs = raw.split('=').map(x => x.trim());
  if (part.kind === 'n') segs = segs.filter(x => !/^n$/i.test(x));
  if (!segs.length || segs.some(x => !x)) return { v: 'unread', msg: UNREAD };
  const letters = vars(part.ans);
  const read = [];
  for (const sg of segs) {
    const r = readOne(!xT && letters.indexOf('x') < 0 ? sg.replace(/\s+[xX]\s+/g, ' * ') : sg, xT); if (r.err) return { v: 'unread', msg: r.err };
    if (vars(r.a).some(l => letters.indexOf(l) < 0)) return { v: 'wrong', msg: letters.length ? 'That uses a letter that isn’t in the question.' : 'This answer is a number — no letters.' };
    read.push(r.a);
  }
  const a = read[read.length - 1];
  let same;
  try { same = sameValue(a, part.ans, letters); } catch (e) { return { v: 'unread', msg: /too large/.test(e.message) ? 'That number is too big to check. Write it with smaller exponents.' : 'I can’t work that out. Check the exponents are whole numbers and nothing is 0 to the power 0 or divided by 0.' }; }
  if (same && read.length > 1) {         // work written before the answer: every step joined by "=" must really be equal
    for (const w of read.slice(0, -1)) {
      let ok; try { ok = sameValue(w, part.ans, letters); } catch (e) { ok = false; }
      if (!ok) return { v: 'wrong', msg: 'Your answer is right, but something you set equal to it with “=” is not equal. Check the steps before the last “=”.' };
    }
  }
  if (same) {
    const k = part.kind;
    if (k === 'power') {
      const u = unwrap(a), b = u.t === 'pow' ? unwrap(u.b) : null;
      if (b && b.t === 'n' && qeq(b.q, Q(part.base)) && literalInt(u.e) !== null) return { v: 'right' };
      return { v: 'form', msg: 'Right value. Now write it as a single power of ' + part.base + '.' };
    }
    if (k === 'value') {
      if (hasPow(a)) return { v: 'form', msg: 'Right so far. Now work out its value — no exponents in the answer.' };
      const vp = valueProblem(a);
      if (vp === 'lowest') return { v: 'form', msg: 'Right value. Write the fraction in lowest terms.' };
      if (vp === 'over1') return { v: 'form', msg: 'Right value. A number over 1 is just that number: leave off the /1.' };
      if (vp) return { v: 'form', msg: 'Right so far. Finish working it out to a single number or fraction.' };
      return { v: 'right' };
    }
    if (k === 'posexp') {
      if (hasNegExp(a)) return { v: 'form', msg: 'Right value. Now rewrite it so every exponent is positive.' };
      if (!hasPow(a)) return { v: 'form', msg: 'Right value, but the question says do not evaluate. Leave it as a power.' };
      const B = part.base, Bs = B < 0 ? '(−' + (-B) + ')' : String(B);
      const goodPow = x => { x = unwrap(x); if (x.t !== 'pow') return false; const b = unwrap(x.b), e = literalInt(x.e);
        const bn = b.t === 'n' ? b.q : b.t === 'neg' && unwrap(b.x).t === 'n' ? qmul(Q(-1), unwrap(b.x).q) : null;
        return bn !== null && qeq(bn, Q(B)) && e !== null && e >= 1n; };
      const u = unwrap(a), wantFrac = unwrap(part.ans).t === 'frac';
      const ok = wantFrac ? (u.t === 'div' && unwrap(u.a).t === 'n' && qeq(unwrap(u.a).q, evalA(unwrap(part.ans).n, {})) && goodPow(u.b)) : goodPow(u);
      if (ok) return { v: 'right' };
      return { v: 'form', msg: 'Right value. Write it ' + (wantFrac ? 'as a number over a power of ' + Bs : 'as a power of ' + Bs) + ', like the question. Keep the same base.' };
    }
    if (k === 'n') return unwrap(a).t === 'n' ? { v: 'right' } : { v: 'form', msg: 'Right value. Write it as a single number.' };
    if (k === 'mono') {
      const p = monoProblem(a, part.posOnly);
      if (!p) return { v: 'right' };
      const say = { combine: 'Right value. Combine the powers of each letter into one.', number: 'Right value. Simplify the numbers into a single number.', distribute: 'Right value, but simplify it: apply the exponent to each factor.',
        negative: 'Right value. Now rewrite it so every exponent is positive.', exponent: 'Right value. Work out each exponent to a single whole number.', read: 'Right value. Write it as a single monomial.',
        fraction: 'Right value. Write it as one fraction — no fraction inside a fraction.', zero: 'Right value. A letter to the zero power is 1, so leave it out.', one: 'Right value. Leave out the 1 in front.' };
      return { v: 'form', msg: say[p] };
    }
    if (k === 'sci') {
      const s = isSci(a);
      if (s && !qlt(s.c, Q(1)) && qlt(s.c, Q(10))) return { v: 'right' };
      if (s) return { v: 'form', msg: 'Right value, but the first number must be at least 1 and less than 10.' };
      return { v: 'form', msg: 'Right value. Write it in scientific notation: a number times a power of 10, with the exponent worked out.' };
    }
    if (k === 'std') {
      if (unwrap(a).t === 'n') return { v: 'right' };
      return { v: 'form', msg: 'Right value. Now write it out as an ordinary number — no power of 10.' };
    }
    if (k === 'times') {
      const s = isSci(a);
      if (unwrap(a).t === 'n' || (s && !qlt(s.c, Q(1)) && qlt(s.c, Q(10)))) return { v: 'right' };
      return { v: 'form', msg: 'Right value. Write it as one number, like 3,000, or in scientific notation, like ' + M(Sci('3', 3)) + '.' };
    }
    return { v: 'right' };
  }
  for (const m of part.miss || []) {
    try { if (sameValue(a, m.ans, letters)) return { v: 'wrong', msg: m.msg }; } catch (e) { /* not this one */ }
  }
  return { v: 'wrong', msg: 'Check each step and try again.' };
}

/* ------------------------------------------------------------------ the generators */
/* Ruling 49 (Croix, 22 Oct 2026): the unit test is a random set of this page, and "add in that variation factor" — so every
   question comes in many versions, with the numbers a student works by hand. FRIENDLY: the powers b^n (n ≥ 2) the value
   questions use — squares to 25² and of tens to 100², cubes to 10³ and 20³, 2…6 and 10 to the 4th, 2…4 to the 5th, 2⁶, 3⁶
   and 2⁷ … 2¹⁰: every value at most 10,000. SELECT_N: the select-all targets 1/bⁿ (b not itself a power; never the test's 64). */
const FRIENDLY = (() => { const L = [], add = (b, n) => L.push([b, n]);
  for (let b = 2; b <= 25; b++) add(b, 2); for (const b of [30, 40, 50, 60, 70, 80, 90, 100]) add(b, 2);
  for (let b = 2; b <= 10; b++) add(b, 3); add(20, 3);
  for (const b of [2, 3, 4, 5, 6, 10]) add(b, 4);
  for (const b of [2, 3, 4]) add(b, 5);
  add(2, 6); add(3, 6); for (let n = 7; n <= 10; n++) add(2, n);
  return L; })();
const SELECT_N = [[2, 2], [2, 3], [2, 4], [2, 5], [2, 7], [2, 8], [2, 9], [2, 10], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [5, 2], [5, 3], [5, 4],
  [6, 2], [6, 3], [7, 2], [7, 3], [10, 2], [10, 3], [10, 4]];
const igcd = (a, b) => { while (b) [a, b] = [b, a % b]; return a; };
function rng(seed) { let a = seed >>> 0; return () => { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
function tools(r) {
  const ri = (lo, hi) => lo + Math.floor(r() * (hi - lo + 1));
  const pick = a => a[Math.floor(r() * a.length)];
  const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const until = (f, bad) => { for (let k = 0; k < 500; k++) { const x = f(); if (!bad(x)) return x; } throw new Error('generator could not avoid the test'); };
  return { ri, pick, shuffle, until };
}
const LET = ['a', 'b', 'c', 'd', 'g', 'h', 'k', 'm', 'n', 'p', 'r', 's', 't', 'w', 'x', 'y', 'z'];
const pw = (b, e) => b ** e;
const same = (x, y) => JSON.stringify(x) === JSON.stringify(y);
function part(label, q, ans, kind, extra) { return Object.assign({ label, q, ans, kind, miss: [], steps: [] }, extra || {}); }
function miss(ans, msg) { return { ans, msg }; }
function mc(stem, opts, correct, why) { return { type: 'mc', stem, opts, correct, why }; }

/* every question on the real test, written out: a practice set may not contain any of them, anywhere */
let TESTSET = null;
function testList() {
  const n = V('n');
  return [
    Mul('·', P(4, 3), P(4, 5)), P(Par(P(2, 3)), 4), Fr(P(7, 9), P(7, 4)), P(9, 0),
    P(Par(Fr(2, 3)), 3), Mul('·', P(6, 0), P(5, 2)), Fr(P(Par(P(10, 2)), 2), P(10, 3)),
    Mul('·', P(2, 4), P(2, 3)), Eq(Fr(P(5, n), P(5, 2)), N(125)),
    P(6, -3), Fr(1, P(Neg(2), -5)), Mul('·', N(3), P(10, -4)),
    P(4, -2), P(Par(Neg(3)), -3), P(Par(Fr(1, 2)), -3), Mul('·', P(2, 5), P(2, -7)), P(5, -2),
    Mul('·', P(V('x'), 4), P(V('x'), 6)), P(Par(P(V('y'), 3)), 5), P(Par(Mul('', N(3), P(V('a'), 2))), 3), Fr(Mul('', N(15), P(V('m'), 7)), Mul('', N(5), P(V('m'), 2))),
    P(V('b'), -4), Mul('', N(5), P(V('x'), -2)), P(Par(Mul('', N(2), P(V('m'), -3), V('n'))), 2), P(Par(Mul('', N(4), P(V('x'), 3))), 2),
    N('8300000'), N('0.00047'), N('60500000000'), N('0.0000000092'), Sci('2.9', 5), Sci('7.1', -6), N('0.0036'),
    Fr(Sci('9', 9), Sci('3', 6)), Fr(Sci('4.8', -3), Sci('1.6', -7)), Sci('5.6', 8)];
}
function testSet() { if (!TESTSET) TESTSET = new Set(testList().map(plain)); return TESTSET; }
/* each question slot draws from its own stream (kit/core.js), and is drawn again until it is not on the real test (compared
   in a canonical form: 2³ · 2⁴ is the test's 2⁴ · 2³) and no modelled mistake gives its answer (coach.js registers that
   check: the clean rule, Apple review W-1). Set 4821's Q6 depends only on (a7u3, 4821, q6) and Q6's code. */
const UNIT_ID = 'a7u3';
let CLEAN = null;
function setClean(fn) { CLEAN = fn; }
function canon(a) {                         // products in a fixed order, so the order of the factors never hides a test question
  if (!a || typeof a !== 'object') return a;
  const c = Array.isArray(a) ? a.map(canon) : Object.fromEntries(Object.entries(a).map(([k, v]) => [k, typeof v === 'object' ? canon(v) : v]));
  if (c.t === 'mul') c.xs = c.xs.slice().sort((x, y) => plain(x) < plain(y) ? -1 : plain(x) > plain(y) ? 1 : 0);
  return c;
}
let TESTCANON = null;
function onTest(q) { if (!TESTCANON) TESTCANON = new Set(testList().map(x => plain(canon(x)))); try { return TESTCANON.has(plain(canon(q))); } catch (e) { return false; } }
function itemQuestions(it) { return it.type === 'parts' ? it.parts.map(p => p.q) : it.type === 'solo' ? [it.part.q] : it.q ? [it.q] : []; }
function generate(seed) {
  if (!CLEAN) throw new Error('coach.js must be loaded before generating');
  const ok = it => !itemQuestions(it).some(onTest) && CLEAN(it);
  const tag = (x, fam, prm) => Object.assign(x, { fam, prm });
  const A7 = T => ({ ri: T.ri, pick: T.pick, shuffle: T.shuffle, until: (f, bad) => T.until(f, x => !bad(x)) });
  const sciPart = (label, c, k, opt) => {
    const value = qmul(qdec(c), qpow(Q(10), BigInt(k)));
    const shown = decStr(value);
    return part(label, N(shown, { commas: k > 0 }), Sci(c, k), 'sci', Object.assign({
      steps: [k > 0 ? 'Move the decimal point ' + k + ' places to the left to get ' + c + ', a number at least 1 and less than 10. So the exponent is ' + k + '.' : 'Move the decimal point ' + (-k) + ' places to the right to get ' + c + '. A number less than 1 has a negative exponent: −' + (-k) + '.'],
      miss: [miss(Sci(c, -k), k > 0 ? 'A large number has a positive exponent.' : 'A number less than 1 has a negative exponent.'),
             miss(Sci(c, k > 0 ? k - 1 : k + 1), 'Count the places the decimal point moves, not the zeros.'), miss(Sci(c, k > 0 ? k + 1 : k - 1), 'That is one place too many. Count the places the decimal point moves.')] }, opt || {}));
  };
  const stdPart = (label, c, k) => {
    const value = qmul(qdec(c), qpow(Q(10), BigInt(k)));
    return part(label, Sci(c, k), N(decStr(value), { commas: true }), 'std', {
      steps: [k > 0 ? 'Move the decimal point ' + k + ' places to the right.' : 'Move the decimal point ' + (-k) + ' places to the left.'],
      miss: [miss(N(decStr(qmul(qdec(c), qpow(Q(10), BigInt(k > 0 ? k - 1 : k + 1))))), 'Count the places carefully: the exponent says how many places the decimal point moves.'),
             miss(N(decStr(qmul(qdec(c), qpow(Q(10), BigInt(k > 0 ? k + 1 : k - 1))))), 'One place too many: the exponent says how many places the decimal point moves.'),
             miss(N(decStr(qmul(qdec(c), qpow(Q(10), BigInt(-k))))), k > 0 ? 'A positive exponent makes the number large.' : 'A negative exponent makes the number small.')] });
  };
  const Q1 = KIT.draw(UNIT_ID, seed, 'q1', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const q1a = until(() => ({ b: pick([2, 3, 5, 6, 7, 8, 9, 10]), m: ri(2, 9), n: ri(2, 9) }), x => same(x, { b: 4, m: 3, n: 5 }) || x.m === x.n || x.m * x.n === 2 * (x.m + x.n));   // {3,6}: b^(mn) = (b²)^(m+n), two mistakes would look alike
    const q1b = until(() => ({ b: pick([2, 3, 5, 6, 7, 10]), m: ri(2, 6), n: ri(2, 6) }), x => same(x, { b: 2, m: 3, n: 4 }) || x.m + x.n === x.m * x.n);
    const q1c = until(() => { const n = ri(2, 6); return { b: pick([2, 3, 5, 6, 8, 9, 10, 11]), m: n + ri(2, 7), n }; }, x => same(x, { b: 7, m: 9, n: 4 }));
    const q1d = until(() => ({ b: ri(2, 120) }), x => x.b === 9);
    const Q1 = { type: 'parts', stem: 'Write each expression as a single power.', parts: [
      part('a', Mul('·', P(q1a.b, q1a.m), P(q1a.b, q1a.n)), P(q1a.b, q1a.m + q1a.n), 'power', { base: q1a.b,
        steps: ['Same base, so add the exponents: ' + q1a.m + ' + ' + q1a.n + ' = ' + (q1a.m + q1a.n) + '.'],
        miss: [miss(P(q1a.b, q1a.m * q1a.n), 'For a product of powers with the same base, add the exponents. Multiplying them is the rule for a power of a power.'),
               miss(P(q1a.b * q1a.b, q1a.m + q1a.n), 'Keep the base the same. Only the exponents combine.')] }),
      part('b', P(Par(P(q1b.b, q1b.m)), q1b.n), P(q1b.b, q1b.m * q1b.n), 'power', { base: q1b.b,
        steps: ['A power of a power: multiply the exponents: ' + q1b.m + ' × ' + q1b.n + ' = ' + (q1b.m * q1b.n) + '.'],
        miss: [miss(P(q1b.b, q1b.m + q1b.n), 'For a power of a power, multiply the exponents.')] }),
      part('c', Fr(P(q1c.b, q1c.m), P(q1c.b, q1c.n)), P(q1c.b, q1c.m - q1c.n), 'power', { base: q1c.b,
        steps: ['Same base, dividing: subtract the exponents: ' + q1c.m + ' − ' + q1c.n + ' = ' + (q1c.m - q1c.n) + '.'],
        miss: [miss(P(q1c.b, q1c.m + q1c.n), 'When you divide powers with the same base, subtract the exponents.')] }),
      part('d', P(q1d.b, 0), N(1), 'value', { after: ' (give its value)',
        steps: ['Any number except 0 raised to the zero power is 1.'],
        miss: [miss(N(0), 'A zero exponent does not make the value 0. Any number except 0 to the zero power is 1.'), miss(N(q1d.b), 'A zero exponent gives 1, not the base.')] }),
    ] };
    tag(Q1.parts[0], 'prod', q1a); tag(Q1.parts[1], 'powpow', q1b); tag(Q1.parts[2], 'quot', q1c); tag(Q1.parts[3], 'zero', q1d);
    return Q1;
  }, ok);
  const Q2 = KIT.draw(UNIT_ID, seed, 'q2', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const q2a = until(() => { const k = pick([2, 2, 2, 2, 3, 3, 3, 4, 5]), q = ri(3, { 2: 20, 3: 10, 4: 5, 5: 4 }[k]); return { p: ri(2, q - 1), q, k }; },
      x => same(x, { p: 2, q: 3, k: 3 }) || igcd(x.p, x.q) !== 1);   /* p = 1 never: the clean rule (raising only the bottom is right there) */
    const q2b = until(() => ({ a: ri(2, 20), c: ri(3, 15) }), x => same(x, { a: 6, c: 5 }) || x.a === x.c);
    const q2c = until(() => { const B = pick([2, 3, 4, 5, 6, 7, 10]), p = ri(2, 5), q = ri(2, 5), e = pick([2, 3]); return { B, p, q, e, r: p * q - e }; }, x => same(x, { B: 10, p: 2, q: 2, e: 1, r: 3 }) || x.B ** x.e > 1000 || x.r < 1);
    /* e = 1 is the test's shape but never clean (B × 1 = B¹), nor is p = q = 2 (adding the exponents gives the same) */
    const Q2 = { type: 'parts', stem: 'Find the value of each expression.', parts: [
      part('a', P(Par(Fr(q2a.p, q2a.q)), q2a.k), Fr(pw(q2a.p, q2a.k), pw(q2a.q, q2a.k)), 'value', {
        steps: ['Raise the top and the bottom to the power ' + q2a.k + ': ' + q2a.p + '<sup>' + q2a.k + '</sup> = ' + pw(q2a.p, q2a.k) + ' and ' + q2a.q + '<sup>' + q2a.k + '</sup> = ' + pw(q2a.q, q2a.k) + '.'],
        miss: [miss(Fr(q2a.p, pw(q2a.q, q2a.k)), 'The exponent applies to the numerator too.'), miss(Fr(pw(q2a.p, q2a.k), q2a.q), 'The exponent applies to the denominator too.')] }),
      part('b', Mul('·', P(q2b.a, 0), P(q2b.c, 2)), N(q2b.c * q2b.c), 'value', {
        steps: [q2b.a + '<sup>0</sup> = 1, and ' + q2b.c + '<sup>2</sup> = ' + (q2b.c * q2b.c) + ', so the value is 1 · ' + (q2b.c * q2b.c) + ' = ' + (q2b.c * q2b.c) + '.'],
        miss: [miss(N(0), q2b.a + '<sup>0</sup> is 1, not 0.'), miss(N(q2b.a * q2b.c * q2b.c), q2b.a + '<sup>0</sup> is 1, not ' + q2b.a + '.')] }),
      part('c', Fr(P(Par(P(q2c.B, q2c.p)), q2c.q), P(q2c.B, q2c.r)), N(pw(q2c.B, q2c.e)), 'value', {
        steps: ['Power of a power: ' + q2c.p + ' × ' + q2c.q + ' = ' + (q2c.p * q2c.q) + '. Divide: ' + (q2c.p * q2c.q) + ' − ' + q2c.r + ' = ' + q2c.e + '. So the value is ' + q2c.B + '<sup>' + q2c.e + '</sup> = ' + pw(q2c.B, q2c.e) + '.'],
        miss: [miss(P(q2c.B, q2c.p + q2c.q - q2c.r), 'A power of a power: multiply the exponents first, then subtract.')] }),
    ] };
    tag(Q2.parts[0], 'fracpow', q2a); tag(Q2.parts[1], 'zeroMix', q2b); tag(Q2.parts[2], 'powquot', q2c);
    return Q2;
  }, ok);
  const Q3 = KIT.draw(UNIT_ID, seed, 'q3', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const q3 = until(() => ({ b: ri(2, 10), m: ri(2, 9), n: ri(2, 9) }), x => same(x, { b: 2, m: 4, n: 3 }) || x.m === x.n ||
      new Set([2 * (x.m + x.n), x.m * x.n, 2 * x.m * x.n, x.m + x.n]).size < 4);
    const o3 = shuffle([[P(q3.b * q3.b, q3.m + q3.n), 'The bases were multiplied too. Keep the base; add the exponents.'], [P(q3.b, q3.m * q3.n), 'The exponents were multiplied. For a product of powers, add them.'],
      [P(q3.b * q3.b, q3.m * q3.n), 'Both mistakes: the bases were multiplied and so were the exponents.'], [P(q3.b, q3.m + q3.n), null]]);
    const Q3 = mc('Which expression is equivalent to ' + M(Mul('·', P(q3.b, q3.m), P(q3.b, q3.n))) + '?', o3.map(o => o[0]), o3.findIndex(o => o[1] === null), o3.map(o => o[1]));
    Q3.q = Mul('·', P(q3.b, q3.m), P(q3.b, q3.n)); Q3.steps = ['Same base, so add the exponents: ' + q3.m + ' + ' + q3.n + ' = ' + (q3.m + q3.n) + '.'];
    tag(Q3, 'prod', q3);
    return Q3;
  }, ok);
  const Q4 = KIT.draw(UNIT_ID, seed, 'q4', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const q4 = until(() => { const b = pick([2, 3, 4, 5, 6, 7, 10]), k = ri(1, 8), c = ri(2, 5); return { b, k, c, V: b ** c }; }, x => (x.b === 5 && x.c === 3) || (x.V > 1296 && x.b !== 10) || x.V > 10000);     // the test's 125 = 5^3 is never used; V a power a student finds by hand (to 1,296, or 10,000)
    const Q4 = { type: 'solo', stem: 'Find the value of ' + M(V('n')) + ' that makes the statement true:  ' + M(Eq(Fr(P(q4.b, V('n')), P(q4.b, q4.k)), N(q4.V, { commas: true }))),
      part: part('', Eq(Fr(P(q4.b, V('n')), P(q4.b, q4.k)), N(q4.V)), N(q4.k + q4.c), 'n', {
        steps: [commas(String(q4.V)) + ' = ' + q4.b + '<sup>' + q4.c + '</sup>.', 'Dividing subtracts the exponents, so <i>n</i> − ' + q4.k + ' = ' + q4.c + '.', '<i>n</i> = ' + (q4.k + q4.c)],
        miss: [miss(N(q4.c), 'That is the exponent of ' + commas(String(q4.V)) + '. The division already took away ' + q4.k + ', so <i>n</i> is ' + q4.k + ' more.')] }) };
    tag(Q4.part, 'solveN', q4);
    return Q4;
  }, ok);
  const Q5 = KIT.draw(UNIT_ID, seed, 'q5', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const q5a = until(() => ({ b: ri(2, 20), n: ri(2, 7) }), x => same(x, { b: 6, n: 3 }));
    const q5b = until(() => ({ c: ri(2, 20), m: ri(2, 7) }), x => same(x, { c: 2, m: 5 }));
    const q5c = until(() => ({ k: ri(2, 19), m: ri(2, 9) }), x => same(x, { k: 3, m: 4 }) || x.k === 10);
    const Q5 = { type: 'parts', stem: 'Rewrite each expression with positive exponents. Do not evaluate.', parts: [
      part('a', P(q5a.b, -q5a.n), Fr(1, P(q5a.b, q5a.n)), 'posexp', { base: q5a.b, steps: ['A negative exponent means the reciprocal: 1 over ' + q5a.b + '<sup>' + q5a.n + '</sup>.'],
        miss: [miss(Neg(P(q5a.b, q5a.n)), 'A negative exponent means the reciprocal, not a negative number.')] }),
      part('b', Fr(1, P(Neg(q5b.c), -q5b.m)), P(Par(Neg(q5b.c)), q5b.m), 'posexp', { base: -q5b.c, steps: ['Dividing by a power with a negative exponent moves it to the top with a positive exponent. The base keeps its sign and its parentheses.'],
        miss: [miss(Fr(1, P(Neg(q5b.c), q5b.m)), 'The power moves to the numerator. It doesn’t stay in the denominator.'),
               miss(Neg(P(q5b.c, q5b.m)), 'Keep the parentheses: the base is −' + q5b.c + ', so write (−' + q5b.c + ')<sup>' + q5b.m + '</sup>.')] }),
      part('c', Mul('·', N(q5c.k), P(10, -q5c.m)), Fr(q5c.k, P(10, q5c.m)), 'posexp', { base: 10, steps: ['Only the 10 has the negative exponent. It moves down; the ' + q5c.k + ' stays on top.'],
        miss: [miss(Fr(1, Mul('·', N(q5c.k), P(10, q5c.m))), 'Only the 10 has the negative exponent. The ' + q5c.k + ' stays in the numerator.')] }),
    ] };
    tag(Q5.parts[0], 'negToFrac', q5a); tag(Q5.parts[1], 'negDen', q5b); tag(Q5.parts[2], 'coefNeg', q5c);
    return Q5;
  }, ok);
  const Q6 = KIT.draw(UNIT_ID, seed, 'q6', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const q6a = until(() => { const [b, n] = pick(FRIENDLY); return { b, n }; }, x => same(x, { b: 4, n: 2 }));
    const q6b = until(() => { const odd = pick([true, true, true, false, false]), [c, e] = pick(FRIENDLY.filter(y => y[1] % 2 === (odd ? 1 : 0))); return { c, e }; }, x => same(x, { c: 3, e: 3 }));   /* an even power too: the sign is the question */
    const q6c = until(() => { const [d, n] = pick(FRIENDLY); return { d, n }; }, x => same(x, { d: 2, n: 3 }));
    const q6d = until(() => { const B = pick([2, 3, 4, 5, 6, 7, 10]), m = ri(2, 9); return { B, m, n: m + ri(1, 3) }; }, x => same(x, { B: 2, m: 5, n: 7 }) || x.B ** (x.n - x.m) > 1000);
    const Q6 = { type: 'parts', stem: 'Find the value of each expression.', parts: [
      part('a', P(q6a.b, -q6a.n), Fr(1, pw(q6a.b, q6a.n)), 'value', { steps: ['Reciprocal of ' + q6a.b + '<sup>' + q6a.n + '</sup>: 1 over ' + pw(q6a.b, q6a.n) + '.'],
        miss: [miss(Neg(N(pw(q6a.b, q6a.n))), 'A negative exponent means the reciprocal, not a negative number.'), miss(Neg(N(q6a.b * q6a.n)), 'The exponent is not a factor. Raise ' + q6a.b + ' to the power ' + q6a.n + ', then take the reciprocal.')] }),
      q6b.e % 2 ? part('b', P(Par(Neg(q6b.c)), -q6b.e), Neg(Fr(1, pw(q6b.c, q6b.e))), 'value', { steps: ['Reciprocal: 1 over (−' + q6b.c + ')<sup>' + q6b.e + '</sup>. An odd power of a negative number is negative: (−' + q6b.c + ')<sup>' + q6b.e + '</sup> = −' + pw(q6b.c, q6b.e) + '.'],
        miss: [miss(Fr(1, pw(q6b.c, q6b.e)), 'Check the sign: an odd power of a negative number is negative.'), miss(Neg(N(pw(q6b.c, q6b.e))), 'Take the reciprocal: the negative exponent means 1 over the power.')] })
      : part('b', P(Par(Neg(q6b.c)), -q6b.e), Fr(1, pw(q6b.c, q6b.e)), 'value', { steps: ['Reciprocal: 1 over (−' + q6b.c + ')<sup>' + q6b.e + '</sup>. An even power of a negative number is positive: (−' + q6b.c + ')<sup>' + q6b.e + '</sup> = ' + pw(q6b.c, q6b.e) + '.'],
        miss: [miss(Neg(Fr(1, pw(q6b.c, q6b.e))), 'Check the sign: an even power of a negative number is positive.'), miss(N(pw(q6b.c, q6b.e)), 'Take the reciprocal: the negative exponent means 1 over the power.')] }),
      part('c', P(Par(Fr(1, q6c.d)), -q6c.n), N(pw(q6c.d, q6c.n)), 'value', { steps: ['The negative exponent flips the fraction: 1/' + q6c.d + ' becomes ' + q6c.d + '. Then ' + q6c.d + '<sup>' + q6c.n + '</sup> = ' + pw(q6c.d, q6c.n) + '.'],
        miss: [miss(Fr(1, pw(q6c.d, q6c.n)), 'The negative exponent flips the fraction, so the answer is a whole number.')] }),
      part('d', Mul('·', P(q6d.B, q6d.m), P(q6d.B, -q6d.n)), Fr(1, pw(q6d.B, q6d.n - q6d.m)), 'value', { steps: ['Same base: add the exponents: ' + q6d.m + ' + (−' + q6d.n + ') = −' + (q6d.n - q6d.m) + '.', q6d.B + '<sup>−' + (q6d.n - q6d.m) + '</sup> = 1 over ' + pw(q6d.B, q6d.n - q6d.m) + '.'],
        miss: [miss(N(pw(q6d.B, q6d.n - q6d.m)), 'The exponent comes out negative, so the value is a reciprocal.')] }),
    ] };
    tag(Q6.parts[0], 'negVal', q6a); tag(Q6.parts[1], 'negNegBase', q6b); tag(Q6.parts[2], 'fracNeg', q6c); tag(Q6.parts[3], 'mixedProd', q6d);
    return Q6;
  }, ok);
  const Q7 = KIT.draw(UNIT_ID, seed, 'q7', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const q7 = until(() => { const [b, n] = pick(FRIENDLY.filter(y => y[1] <= 4)); return { b, n }; }, x => (x.b === 5 && x.n === 2) || (x.b === 2 && x.n === 2));   /* 2^2 = 2 · 2: two choices alike */
    const v7 = pw(q7.b, q7.n), t7 = q7.n * q7.b;
    const o7 = shuffle([[Fr(1, t7), 'The reciprocal is right, but ' + q7.b + '<sup>' + q7.n + '</sup> is ' + v7 + ', not ' + q7.n + ' × ' + q7.b + ' = ' + t7 + '.'], [Neg(N(v7)), 'A negative exponent means the reciprocal, not a negative number.'],
      [Fr(1, v7), null], [Neg(N(t7)), 'The exponent isn’t a factor, and a negative exponent doesn’t make the value negative.']]);
    const Q7 = mc('Which is the value of ' + M(P(q7.b, -q7.n)) + '?', o7.map(o => o[0]), o7.findIndex(o => o[1] === null), o7.map(o => o[1]));
    Q7.q = P(q7.b, -q7.n); Q7.steps = [q7.b + '<sup>−' + q7.n + '</sup> = 1 over ' + q7.b + '<sup>' + q7.n + '</sup> = 1 over ' + v7 + '.'];
    tag(Q7, 'negVal', { b: q7.b, n: q7.n });
    return Q7;
  }, ok);
  const Q8 = KIT.draw(UNIT_ID, seed, 'q8', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  /* 1/N for N = bⁿ: three choices equal to it — bⁿ's negative power, (1/b)ⁿ, N⁻¹, and the same for any other way to write N
       as a power (16 = 4²) — and two that are not: a minus sign in front of the power, an exponent one off, (b²)⁻ⁿ, (1/b)⁻ⁿ.
       Five hand-made sets before 22 Oct 2026 (ruling 49). */
    const [b8, n8] = pick(SELECT_N), N8 = pw(b8, n8), reps = [];
    for (let j = 1; j < n8; j++) if (n8 % j === 0) reps.push([pw(b8, j), n8 / j]);
    const R8 = [P(b8, -n8), P(Par(Fr(1, b8)), n8), P(N8, -1)];
    reps.forEach(([c, k]) => { if (c !== b8) R8.push(P(c, -k), P(Par(Fr(1, c)), k)); });
    const W8 = reps.map(([c, k]) => Neg(P(c, k))).concat([P(b8, -(n8 + 1)), P(b8, -(n8 - 1)), P(b8 * b8, -n8), P(Par(Fr(1, b8)), -n8)]);
    const T8 = { N: N8 }, o8 = shuffle(shuffle(R8).slice(0, 3).concat(shuffle(W8).slice(0, 2)));
    const want8 = Q(1, T8.N);
    const Q8 = { type: 'multi', stem: 'Select ALL of the expressions whose value is ' + M(Fr(1, T8.N)) + '.', opts: o8, correct: o8.map((o, i) => qeq(evalA(o, {}), want8) ? i : -1).filter(i => i >= 0), target: Fr(1, T8.N),
      steps: o8.map(o => { const v = evalA(o, {}); return { e: o, v: v.d === 1n ? (v.n < 0n ? Neg(N(Number(-v.n))) : N(Number(v.n))) : (v.n < 0n ? Neg(Fr(Number(-v.n), Number(v.d))) : Fr(Number(v.n), Number(v.d))), ok: qeq(v, want8) }; }) };
    tag(Q8, 'select', { N: T8.N });
    return Q8;
  }, ok);
  const Q9 = KIT.draw(UNIT_ID, seed, 'q9', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const v9a = until(() => ({ v: pick(LET), m: ri(2, 15), n: ri(2, 15) }), x => same(x, { v: 'x', m: 4, n: 6 }) || x.m === x.n);
    const v9b = until(() => ({ v: pick(LET), m: ri(2, 12), n: ri(2, 12) }), x => same(x, { v: 'y', m: 3, n: 5 }) || x.m + x.n === x.m * x.n || x.m * x.n > 100);
    const v9c = until(() => { const q = pick([2, 2, 3, 3, 4]); return { c: ri(2, { 2: 12, 3: 6, 4: 3 }[q]), v: pick(LET), p: ri(2, 9), q }; }, x => same(x, { c: 3, v: 'a', p: 2, q: 3 }) || x.c * x.q === x.c ** x.q);
    const v9d = until(() => { const j = ri(2, 6), t = ri(2, 6), q = ri(2, 4); return { j, t, k: j * t, v: pick(LET), q, p: q + ri(2, 5) }; }, x => same(x, { j: 5, t: 3, k: 15, v: 'm', q: 2, p: 7 }));
    const Q9 = { type: 'parts', stem: 'Write each expression as a single monomial.', parts: [
      part('a', Mul('·', P(V(v9a.v), v9a.m), P(V(v9a.v), v9a.n)), P(V(v9a.v), v9a.m + v9a.n), 'mono', { steps: ['Same base, so add the exponents: ' + v9a.m + ' + ' + v9a.n + ' = ' + (v9a.m + v9a.n) + '.'],
        miss: [miss(P(V(v9a.v), v9a.m * v9a.n), 'For a product of powers, add the exponents.')] }),
      part('b', P(Par(P(V(v9b.v), v9b.m)), v9b.n), P(V(v9b.v), v9b.m * v9b.n), 'mono', { steps: ['A power of a power: multiply the exponents: ' + v9b.m + ' × ' + v9b.n + ' = ' + (v9b.m * v9b.n) + '.'],
        miss: [miss(P(V(v9b.v), v9b.m + v9b.n), 'For a power of a power, multiply the exponents.')] }),
      part('c', P(Par(Mul('', N(v9c.c), P(V(v9c.v), v9c.p))), v9c.q), Mul('', N(pw(v9c.c, v9c.q)), P(V(v9c.v), v9c.p * v9c.q)), 'mono', {
        steps: ['Everything inside the parentheses gets the exponent: ' + v9c.c + '<sup>' + v9c.q + '</sup> = ' + pw(v9c.c, v9c.q) + ', and ' + v9c.p + ' × ' + v9c.q + ' = ' + (v9c.p * v9c.q) + '.'],
        miss: [miss(Mul('', N(v9c.c), P(V(v9c.v), v9c.p * v9c.q)), 'Raise the ' + v9c.c + ' to the power too: ' + v9c.c + '<sup>' + v9c.q + '</sup> = ' + pw(v9c.c, v9c.q) + '.'),
               miss(Mul('', N(v9c.c * v9c.q), P(V(v9c.v), v9c.p * v9c.q)), v9c.c + '<sup>' + v9c.q + '</sup> means ' + v9c.c + ' multiplied by itself ' + v9c.q + ' times, not ' + v9c.c + ' × ' + v9c.q + '.')] }),
      part('d', Fr(Mul('', N(v9d.k), P(V(v9d.v), v9d.p)), Mul('', N(v9d.j), P(V(v9d.v), v9d.q))), Mul('', N(v9d.t), P(V(v9d.v), v9d.p - v9d.q)), 'mono', {
        steps: ['Divide the numbers: ' + v9d.k + ' ÷ ' + v9d.j + ' = ' + v9d.t + '. Subtract the exponents: ' + v9d.p + ' − ' + v9d.q + ' = ' + (v9d.p - v9d.q) + '.'],
        miss: [miss(Mul('', N(v9d.t), P(V(v9d.v), v9d.p + v9d.q)), 'When dividing, subtract the exponents.')] }),
    ] };
    tag(Q9.parts[0], 'monoProd', v9a); tag(Q9.parts[1], 'monoPow', v9b); tag(Q9.parts[2], 'monoCoefPow', v9c); tag(Q9.parts[3], 'monoQuot', v9d);
    return Q9;
  }, ok);
  const Q10 = KIT.draw(UNIT_ID, seed, 'q10', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const v10a = until(() => ({ v: pick(LET), n: ri(2, 9) }), x => same(x, { v: 'b', n: 4 }));
    const v10b = until(() => ({ c: ri(2, 20), v: pick(LET), n: ri(2, 9) }), x => same(x, { c: 5, v: 'x', n: 2 }));
    const v10c = until(() => { const v = pick(LET), w = pick(LET), q = pick([2, 2, 3, 3, 4]); return { k: ri(2, { 2: 12, 3: 5, 4: 3 }[q]), v, p: ri(2, 8), w, q }; }, x => x.v === x.w || same(x, { k: 2, v: 'm', p: 3, w: 'n', q: 2 }));
    const Q10 = { type: 'parts', stem: 'Rewrite each expression using only positive exponents.', parts: [
      part('a', P(V(v10a.v), -v10a.n), Fr(1, P(V(v10a.v), v10a.n)), 'mono', { posOnly: true, steps: ['A negative exponent means the reciprocal: 1 over ' + v10a.v + '<sup>' + v10a.n + '</sup>.'],
        miss: [miss(Neg(P(V(v10a.v), v10a.n)), 'A negative exponent means the reciprocal, not a negative.')] }),
      part('b', Mul('', N(v10b.c), P(V(v10b.v), -v10b.n)), Fr(v10b.c, P(V(v10b.v), v10b.n)), 'mono', { posOnly: true, steps: ['Only the <i>' + v10b.v + '</i> has the negative exponent, so only it moves down. The ' + v10b.c + ' stays on top.'],
        miss: [miss(Fr(1, Mul('', N(v10b.c), P(V(v10b.v), v10b.n))), 'Only the <i>' + v10b.v + '</i> has the negative exponent, so the ' + v10b.c + ' stays in the numerator.')] }),
      part('c', P(Par(Mul('', N(v10c.k), P(V(v10c.v), -v10c.p), V(v10c.w))), v10c.q), Fr(Mul('', N(pw(v10c.k, v10c.q)), P(V(v10c.w), v10c.q)), P(V(v10c.v), v10c.p * v10c.q)), 'mono', { posOnly: true,
        steps: ['Apply the exponent ' + v10c.q + ' to every factor: ' + v10c.k + '<sup>' + v10c.q + '</sup> = ' + pw(v10c.k, v10c.q) + ', <i>' + v10c.v + '</i><sup>−' + (v10c.p * v10c.q) + '</sup>, <i>' + v10c.w + '</i><sup>' + v10c.q + '</sup>.', 'Then move <i>' + v10c.v + '</i><sup>−' + (v10c.p * v10c.q) + '</sup> to the denominator.'],
        miss: [miss(Fr(Mul('', N(v10c.k), P(V(v10c.w), v10c.q)), P(V(v10c.v), v10c.p * v10c.q)), 'The ' + v10c.k + ' gets the exponent too: ' + v10c.k + '<sup>' + v10c.q + '</sup> = ' + pw(v10c.k, v10c.q) + '.')] }),
    ] };
    tag(Q10.parts[0], 'varNeg', v10a); tag(Q10.parts[1], 'coefVarNeg', v10b); tag(Q10.parts[2], 'monoNegPow', v10c);
    return Q10;
  }, ok);
  const Q11 = KIT.draw(UNIT_ID, seed, 'q11', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const v11 = until(() => { const q = pick([2, 2, 3, 3, 4]); return { c: ri(2, { 2: 12, 3: 6, 4: 3 }[q]), v: pick(LET), p: ri(2, 9), q }; }, x => same(x, { c: 4, v: 'x', p: 3, q: 2 }) || x.c ** x.q === x.c * x.q || x.p + x.q === x.p * x.q);
    const o11 = shuffle([[Mul('', N(pw(v11.c, v11.q)), P(V(v11.v), v11.p + v11.q)), 'The exponents were added. For a power of a power, multiply them.'], [Mul('', N(v11.c * v11.q), P(V(v11.v), v11.p * v11.q)), v11.c + '<sup>' + v11.q + '</sup> means ' + Array(v11.q).fill(v11.c).join(' · ') + ', not ' + v11.c + ' × ' + v11.q + '.'],
      [Mul('', N(v11.c), P(V(v11.v), v11.p * v11.q)), 'The number inside the parentheses gets the exponent too.'], [Mul('', N(pw(v11.c, v11.q)), P(V(v11.v), v11.p * v11.q)), null]]);
    const Q11 = mc('Which expression is equivalent to ' + M(P(Par(Mul('', N(v11.c), P(V(v11.v), v11.p))), v11.q)) + '?', o11.map(o => o[0]), o11.findIndex(o => o[1] === null), o11.map(o => o[1]));
    Q11.q = P(Par(Mul('', N(v11.c), P(V(v11.v), v11.p))), v11.q); Q11.steps = ['Everything inside the parentheses gets the exponent: ' + v11.c + '<sup>' + v11.q + '</sup> = ' + pw(v11.c, v11.q) + ', and ' + v11.p + ' × ' + v11.q + ' = ' + (v11.p * v11.q) + '.'];
    tag(Q11, 'monoCoefPow', v11);
    return Q11;
  }, ok);
  const Q12 = KIT.draw(UNIT_ID, seed, 'q12', T0 => { const { ri, pick, shuffle, until } = A7(T0);
    const d2 = () => ri(1, 9) + '.' + ri(1, 9);
  const s12 = until(() => ({ a: [d2(), ri(5, 9)], b: [d2(), -ri(3, 6)], c: [ri(1, 9) + '.0' + ri(1, 9), ri(8, 11)], d: [d2(), -ri(7, 10)] }),
      x => same(x.a, ['8.3', 6]) || same(x.b, ['4.7', -4]) || same(x.c, ['6.05', 10]) || same(x.d, ['9.2', -9]));
    const Q12 = { type: 'parts', stem: 'Write each number in scientific notation.', parts: [sciPart('a', ...s12.a), sciPart('b', ...s12.b), sciPart('c', ...s12.c), sciPart('d', ...s12.d)] };
    const stdPart = (label, c, k) => {
      const value = qmul(qdec(c), qpow(Q(10), BigInt(k)));
      return part(label, Sci(c, k), N(decStr(value), { commas: true }), 'std', {
        steps: [k > 0 ? 'Move the decimal point ' + k + ' places to the right.' : 'Move the decimal point ' + (-k) + ' places to the left.'],
        miss: [miss(N(decStr(qmul(qdec(c), qpow(Q(10), BigInt(k > 0 ? k - 1 : k + 1))))), 'Count the places carefully: the exponent says how many places the decimal point moves.'),
               miss(N(decStr(qmul(qdec(c), qpow(Q(10), BigInt(k > 0 ? k + 1 : k - 1))))), 'One place too many: the exponent says how many places the decimal point moves.'),
               miss(N(decStr(qmul(qdec(c), qpow(Q(10), BigInt(-k))))), k > 0 ? 'A positive exponent makes the number large.' : 'A negative exponent makes the number small.')] });
    };
    [s12.a, s12.b, s12.c, s12.d].forEach((x, i) => tag(Q12.parts[i], 'toSci', { c: x[0], k: x[1] }));
    return Q12;
  }, ok);
  const Q13 = KIT.draw(UNIT_ID, seed, 'q13', T0 => { const { ri, pick, shuffle, until } = A7(T0);
    const d2 = () => ri(1, 9) + '.' + ri(1, 9);
  const s13 = until(() => ({ a: [d2(), ri(4, 7)], b: [d2(), -ri(4, 7)] }), x => same(x.a, ['2.9', 5]) || same(x.b, ['7.1', -6]));
    const Q13 = { type: 'parts', stem: 'Write each number in standard form.', parts: [stdPart('a', ...s13.a), stdPart('b', ...s13.b)] };
    [s13.a, s13.b].forEach((x, i) => tag(Q13.parts[i], 'toStd', { c: x[0], k: x[1] }));
    return Q13;
  }, ok);
  const Q14 = KIT.draw(UNIT_ID, seed, 'q14', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const s14 = until(() => ({ d1: ri(1, 9), d2: ri(1, 9), k: ri(3, 5) }), x => same(x, { d1: 3, d2: 6, k: 3 }));
    const c14 = s14.d1 + '.' + s14.d2, n14 = decStr(qmul(qdec(c14), qpow(Q(10), BigInt(-s14.k))));
    const o14 = shuffle([[Sci(c14, s14.k), 'The sign was dropped: that number is ' + commas(decStr(qmul(qdec(c14), qpow(Q(10), BigInt(s14.k))))) + '.'], [Sci(c14, -s14.k), null],
      [Sci(c14, -(s14.k - 1)), 'That counts the zeros. The exponent counts the places the decimal point moves.'], [Sci(String(s14.d1 * 10 + s14.d2), -(s14.k + 1)), 'Equal in value, but ' + (s14.d1 * 10 + s14.d2) + ' is not less than 10, so it is not scientific notation.']]);
    const Q14 = mc('Which is ' + M(N(n14)) + ' written in scientific notation?', o14.map(o => o[0]), o14.findIndex(o => o[1] === null), o14.map(o => o[1]));
    Q14.q = N(n14); Q14.sci = true; Q14.steps = ['Move the decimal point ' + s14.k + ' places to the right to get ' + c14 + '. A number less than 1 has a negative exponent.'];
    tag(Q14, 'toSci', { c: c14, k: -s14.k });
    return Q14;
  }, ok);
  const Q15 = KIT.draw(UNIT_ID, seed, 'q15', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const s15 = until(() => { const B = ri(2, 4), t = ri(2, 4), q = ri(2, 9); const B2 = ri(11, 49) / 10, t2 = ri(2, 5), p2 = ri(2, 5);
      return { A: B * t, B, t, p: q + ri(1, 6), q, A2: Math.round(B2 * t2 * 10) / 10, B2, t2, p2, q2: p2 + ri(2, 5) }; },
      x => x.A > 9 || x.A2 >= 10 || x.A2 < 1 || same([x.A, x.B, x.p, x.q], [9, 3, 9, 6]) || same([x.A2, x.B2, x.p2, x.q2], [4.8, 1.6, 3, 7]) || String(x.B2).length !== 3);
    const A2s = String(s15.A2), B2s = String(s15.B2);
    const Q15 = { type: 'parts', stem: 'Answer each question.', parts: [
      part('a', Fr(Sci(String(s15.A), s15.p), Sci(String(s15.B), s15.q)), Sci(String(s15.t), s15.p - s15.q), 'times', { text: ['How many times larger is ', Sci(String(s15.A), s15.p), ' than ', Sci(String(s15.B), s15.q), '?'],
        shownAns: Sci(String(s15.t), s15.p - s15.q), tail: ' = ' + commas(decStr(Q(s15.t * 10 ** (s15.p - s15.q)))) + ' times',
        steps: ['Divide the numbers: ' + s15.A + ' ÷ ' + s15.B + ' = ' + s15.t + '. Divide the powers of 10: subtract the exponents, ' + s15.p + ' − ' + s15.q + ' = ' + (s15.p - s15.q) + '.'],
        miss: [miss(N(s15.t), 'Divide the powers of 10 as well: subtract the exponents.'), miss(Sci(String(s15.t), s15.p + s15.q), 'To divide powers of 10, subtract the exponents.')] }),
      part('b', Fr(Sci(A2s, -s15.p2), Sci(B2s, -s15.q2)), Sci(String(s15.t2), s15.q2 - s15.p2), 'times', { text: ['How many times larger is ', Sci(A2s, -s15.p2), ' than ', Sci(B2s, -s15.q2), '?'],
        shownAns: Sci(String(s15.t2), s15.q2 - s15.p2), tail: ' = ' + commas(decStr(Q(s15.t2 * 10 ** (s15.q2 - s15.p2)))) + ' times',
        steps: ['Divide the numbers: ' + A2s + ' ÷ ' + B2s + ' = ' + s15.t2 + '. Subtract the exponents: −' + s15.p2 + ' − (−' + s15.q2 + ') = ' + (s15.q2 - s15.p2) + '.'],
        miss: [miss(N(s15.t2), 'Divide the powers of 10 as well: subtract the exponents.'), miss(Sci(String(s15.t2), -(s15.p2 + s15.q2)), 'Subtract the exponents: −' + s15.p2 + ' − (−' + s15.q2 + ') = ' + (s15.q2 - s15.p2) + '.')] }),
    ] };
    tag(Q15.parts[0], 'ratio', { A: String(s15.A), B: String(s15.B), t: String(s15.t), p: s15.p, q: s15.q });
    tag(Q15.parts[1], 'ratio', { A: A2s, B: B2s, t: String(s15.t2), p: -s15.p2, q: -s15.q2 });
    return Q15;
  }, ok);
  const Q16 = KIT.draw(UNIT_ID, seed, 'q16', T0 => { const { ri, pick, shuffle, until } = A7(T0);
  const s16 = until(() => ({ c: ri(1, 9) + '.' + (r16 => r16)(pick([String(ri(1, 9)), String(ri(1, 9)) + String(ri(1, 9))])), k: ri(5, 9) }), x => same(x, { c: '5.6', k: 8 }) || /0$/.test(x.c));
    const v16 = qmul(qdec(s16.c), qpow(Q(10), BigInt(s16.k)));
    const Q16 = { type: 'solo', stem: 'A computer displays a number as  ' + esc(s16.c + 'E' + s16.k) + '.  Write the number in standard form.',
      part: part('', Sci(s16.c, s16.k), N(decStr(v16), { commas: true }), 'std', { steps: ['E' + s16.k + ' means × 10<sup>' + s16.k + '</sup>: move the decimal point ' + s16.k + ' places to the right.'],
        miss: [miss(N(decStr(qmul(qdec(s16.c), qpow(Q(10), BigInt(s16.k - 1))))), 'Count again: E' + s16.k + ' moves the decimal point ' + s16.k + ' places.'), miss(N(decStr(qmul(qdec(s16.c), qpow(Q(10), BigInt(s16.k + 1))))), 'Count again: E' + s16.k + ' moves the decimal point ' + s16.k + ' places.')] }) };
    tag(Q16.part, 'eNote', { c: s16.c, k: s16.k });
    return Q16;
  }, ok);
  /* the engine's own short mistake list (part.miss) may hold a "mistake" equal to the key — (−c)^m written −c^m when m is
     odd, say. Those are dropped here, as before the kit: a right value never gets a mistake's words. */
  [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16].forEach(it => (it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : []).forEach(p => {
    const L = vars(p.ans); p.miss = (p.miss || []).filter(m => { try { return !sameValue(m.ans, p.ans, L); } catch (e) { return false; } }); }));
  return { seed, sections: [
    { title: 'Laws of Exponents', items: [Q1, Q2, Q3, Q4] },
    { title: 'Integer Exponents', items: [Q5, Q6, Q7, Q8] },
    { title: 'Variable Bases', items: [Q9, Q10, Q11] },
    { title: 'Scientific Notation', items: [Q12, Q13, Q14, Q15, Q16] }] };
}

const api = { speak, UNIT_ID, setClean, canon, onTest, testList, testSet, Q, qeq, qdec, decStr, commas, N, V, P, Mul, Fr, Neg, Par, Eq, Sci, Ar, evalA, html, M, plain, parse, tidy, mark, generate, monoProblem, isSci, hasPow, hasNegExp,
  qadd, qsub, qmul, qdiv, qpow, qlt, gcd, unwrap, literalInt, sameValue, vars, valueProblem, esc };
if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.Practice = api;
})(this);
