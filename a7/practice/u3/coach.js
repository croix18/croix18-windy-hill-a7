/* A7 Unit 3 practice: the coach. Reads a student's wrong (or nearly right) answer, works out which part of it went wrong,
   says so with the student's own numbers, gives the rule for next time, and builds the worked solution step by step.

   Soundness rules (checked by coach_check.js and verify_coach.py):
   - Every "That's what you get if you …" sentence is attached to a mistake model whose result is computed exactly; it is shown
     only when the typed answer has exactly that value (or, for letters, the same value at four test points). It is phrased as a
     fact about the answer ("that is what this mistake gives"), never as a guess about the student.
   - Every comparison sentence ("your exponent 7 is not 8 + 5") is computed from the parsed answer.
   - Every worked step's expression has the same value as the question; the last one is the answer. */
(function (root) {
'use strict';
const E = (typeof module !== 'undefined' && module.exports) ? require('./engine.js') : root.Practice;
const { Q, qeq, qdec, decStr, commas, N, V, P, Mul, Fr, Neg, Par, Eq, Sci, Ar, evalA, M, unwrap, literalInt, sameValue, vars, qmul, qdiv, qpow, qlt, esc } = E;

/* ------------------------------------------------------------------ small tools */
const qi = x => typeof x === 'object' ? x : typeof x === 'string' ? qdec(x) : Q(BigInt(x));
const ipow = (b, e) => qpow(qi(b), BigInt(e));
function numA(q, opt) {                                   // an exact number as a drawing: 5, −3, 1/8, −1/27, 0.0047
  const neg = q.n < 0n, n = neg ? -q.n : q.n; let a;
  if (q.d === 1n) a = N(n.toString(), { commas: true });
  else if (opt && opt.dec) { try { a = N(decStr(Q(n, q.d)), { commas: true }); } catch (e) { a = Fr(N(n.toString()), N(q.d.toString())); } }
  else a = Fr(N(n.toString()), N(q.d.toString()));
  return neg ? Neg(a) : a;
}
const m = a => M(a);
const mv = (q, opt) => M(numA(q, opt));
const negA = x => x < 0 ? Par(Neg(N(-x))) : N(x);       // a number that may be negative, in parentheses when it is
const sgn = x => x < 0 ? '(−' + (-x) + ')' : String(x);
function times(b, n) { const s = String(b).replace('-', '−'); if (n > 6) return s + ' multiplied by itself ' + n + ' times'; return Array(n).fill(s.indexOf('−') === 0 ? '(' + s + ')' : s).join(' · '); }
function val(a) { try { if (vars(a).length) return null; return evalA(a, {}); } catch (e) { return null; } }
function intOf(a) { const v = val(a); return v && v.d === 1n ? v.n : null; }
const big = k => BigInt(k);

/* a typed monomial taken apart: number part and the exponent of each letter. 27a^6/b^2 → {c: 27, x: {a: 6, b: −2}} */
function addX(x, y, s) { const r = Object.assign({}, x); for (const k in y) { r[k] = (r[k] || 0n) + s * y[k]; if (r[k] === 0n) delete r[k]; } return r; }
function mono(a) {
  a = unwrap(a);
  switch (a.t) {
    case 'n': return { c: a.q, x: {} };
    case 'v': return { c: Q(1), x: { [a.s]: 1n } };
    case 'neg': { const r = mono(a.x); return r && { c: qmul(Q(-1), r.c), x: r.x }; }
    case 'mul': { let r = { c: Q(1), x: {} }; for (const f of a.xs) { const s = mono(f); if (!s) return null; r = { c: qmul(r.c, s.c), x: addX(r.x, s.x, 1n) }; } return r; }
    case 'div': case 'frac': {
      const t = mono(a.t === 'div' ? a.a : a.n), b = mono(a.t === 'div' ? a.b : a.d);
      if (!t || !b || b.c.n === 0n) return null; return { c: qdiv(t.c, b.c), x: addX(t.x, b.x, -1n) };
    }
    case 'pow': {
      const e = intOf(a.e); if (e === null || e > 60n || e < -60n) return null;
      const s = mono(a.b); if (!s || (s.c.n === 0n && e <= 0n)) return null;
      const x = {}; for (const k in s.x) { x[k] = s.x[k] * e; if (x[k] === 0n) delete x[k]; }
      return { c: qpow(s.c, e), x };
    }
    default: return null;
  }
}
/* a single power with a number base: 4^8 → {b: 4, e: 8}; (−2)^5 → {b: −2, e: 5} */
function single(a) {
  a = unwrap(a); if (a.t !== 'pow') return null;
  const e = literalInt(a.e); if (e === null) return null;
  const b = val(a.b); if (!b) return null;
  return { b, e };
}
/* scientific-notation shape: 8.3 × 10^6 (either order) → {c: 8.3, k: 6, cs: '8.3'} */
function sciOf(a) {
  a = unwrap(a);
  const ten = x => { x = unwrap(x); if (x.t !== 'pow') return null; const b = unwrap(x.b); if (b.t !== 'n' || !qeq(b.q, Q(10))) return null; const k = literalInt(x.e); return k; };
  if (ten(a) !== null) return { c: Q(1), k: ten(a), cs: '1' };
  if (a.t !== 'mul' || a.xs.length !== 2) return null;
  for (const [c0, p0] of [[a.xs[0], a.xs[1]], [a.xs[1], a.xs[0]]]) {
    const c = unwrap(c0), k = ten(p0);
    if (k !== null && c.t === 'n') return { c: c.q, k, cs: c.s };
  }
  return null;
}
function digitsOf(q) {                                      // the significant digits of a positive terminating decimal: 0.00470 → "47"
  let s; try { s = decStr(q.n < 0n ? Q(-q.n, q.d) : q); } catch (e) { return null; }
  return s.replace('.', '').replace(/^0+/, '').replace(/0+$/, '') || '0';
}
function tenPow(q) {                                        // q = 10^j exactly → j, else null
  if (q.n <= 0n) return null;
  for (let j = -40; j <= 40; j++) if (qeq(q, qpow(Q(10), big(j)))) return j;
  return null;
}
function normSci(v) {                                      // positive v = d × 10^j with 1 ≤ d < 10
  let d = v, j = 0;
  while (!qlt(d, Q(10))) { d = qdiv(d, Q(10)); j++; }
  while (qlt(d, Q(1))) { d = qmul(d, Q(10)); j--; }
  return { d, j };
}
function logB(v, b) {                                       // v = b^k for a whole k → k (|k| ≤ 40), else null
  if (!v || !b) return null;
  for (let k = -40; k <= 40; k++) { try { if (qeq(qpow(b, big(k)), v)) return k; } catch (e) { } }
  return null;
}

/* ------------------------------------------------------------------ the rules, as a student would write them down */
const a_ = V('a'), m_ = V('m'), n_ = V('n'), k_ = V('k'), b_ = V('b');
const RULE = {
  prod: () => 'Multiplying powers with the same base: keep the base, <b>add</b> the exponents. ' + m(Eq(Mul('·', P(a_, m_), P(a_, n_)), P(a_, Ar(m_, '+', n_)))),
  powpow: () => 'A power of a power: keep the base, <b>multiply</b> the exponents. ' + m(Eq(P(Par(P(a_, m_)), n_), P(a_, Ar(m_, '×', n_)))),
  quot: () => 'Dividing powers with the same base: keep the base, <b>subtract</b> the exponents (top minus bottom). ' + m(Eq(Fr(P(a_, m_), P(a_, n_)), P(a_, Ar(m_, '−', n_)))),
  zero: () => 'Any number except 0 to the zero power is 1. ' + m(Eq(P(a_, 0), N(1))),
  fracpow: () => 'A fraction to a power: raise the top <b>and</b> the bottom. ' + m(Eq(P(Par(Fr(a_, b_)), n_), Fr(P(a_, n_), P(b_, n_)))),
  zeroMix: () => 'Change each zero power to 1 first, then work out the rest. ' + m(Eq(P(a_, 0), N(1))),
  powquot: () => 'Work from the inside out: power of a power first (multiply the exponents), then divide (subtract the exponents), then find the value.',
  solveN: () => 'Write both sides as powers of the same base. When the bases match, the exponents must match.',
  negToFrac: () => 'A negative exponent means <b>one over</b> the power — never a negative number. ' + m(Eq(P(a_, Neg(n_)), Fr(1, P(a_, n_)))),
  negDen: () => 'A power with a negative exponent in the denominator moves up to the numerator and its exponent turns positive. ' + m(Eq(Fr(1, P(a_, Neg(n_))), P(a_, n_))),
  coefNeg: () => 'Only the factor that has the negative exponent moves; the number in front stays on top. ' + m(Eq(Mul('·', k_, P(a_, Neg(n_))), Fr(k_, P(a_, n_)))),
  negVal: () => 'A negative exponent means one over the power. Then work out the power. ' + m(Eq(P(a_, Neg(n_)), Fr(1, P(a_, n_)))),
  negNegBase: () => 'One over the power first. Then the sign: a negative base to an <b>odd</b> power is negative; to an <b>even</b> power, positive.',
  fracNeg: () => 'A negative exponent on a fraction flips the fraction and makes the exponent positive. ' + m(Eq(P(Par(Fr(1, a_)), Neg(n_)), P(a_, n_))),
  mixedProd: () => 'Add the exponents — watch the signs. If the total is negative, the answer is one over the power.',
  monoProd: () => RULE.prod(),
  monoPow: () => RULE.powpow(),
  monoCoefPow: () => 'Everything inside the parentheses gets the exponent: the number <b>and</b> each letter. ' + m(Eq(P(Par(Mul('', k_, P(a_, m_))), n_), Mul('', P(k_, n_), P(a_, Ar(m_, '×', n_))))),
  monoQuot: () => 'Divide the numbers. For each letter, subtract the exponents (top minus bottom).',
  varNeg: () => RULE.negToFrac(),
  coefVarNeg: () => RULE.coefNeg(),
  monoNegPow: () => 'Raise every factor inside the parentheses to the outside exponent: the number, and each letter (multiply its exponent, keeping the sign). Then move any letter with a negative exponent to the bottom, where its exponent turns positive.',
  toSci: () => 'Scientific notation is <b>(a number at least 1 and less than 10) × 10<sup>k</sup></b>. k counts the places the decimal point moves. A big number gets a positive k; a number less than 1 gets a negative k.',
  toStd: () => 'Positive exponent: move the decimal point that many places <b>right</b> (the number gets bigger). Negative exponent: move it <b>left</b> (smaller). Fill empty places with zeros.',
  eNote: () => 'On a calculator, <b>E</b> means “× 10 to the power”: 5.6E8 means 5.6 × 10<sup>8</sup>. ' + RULE.toStd(),
  ratio: () => '“How many times larger” means <b>divide</b> (larger ÷ smaller). Divide the numbers, and subtract the exponents of the powers of 10.',
  select: () => 'Work out the value of each choice on its own. A negative exponent makes a reciprocal; a minus sign in front of a power makes the value negative.',
};

/* ------------------------------------------------------------------ worked solutions: steps whose expressions all equal the question */
function solution(part) {
  const f = part.fam, x = part.prm; if (!f || !x) return null;
  const S = (say, ex) => ({ say, ex: ex || null });
  switch (f) {
    case 'prod': case 'monoProd': {
      const b = f === 'prod' ? x.b : V(x.v), bs = f === 'prod' ? String(x.b) : '<i>' + x.v + '</i>';
      return [S('Why it works: ' + m(P(b, x.m)) + ' is ' + x.m + ' factors of ' + bs + ' and ' + m(P(b, x.n)) + ' is ' + x.n + ' more, so that is ' + x.m + ' + ' + x.n + ' factors of ' + bs + ' in all.'),
        S('The bases are the same and they are multiplied: keep the base, add the exponents.', P(b, Ar(x.m, '+', x.n))),
        S(x.m + ' + ' + x.n + ' = ' + (x.m + x.n) + '.', P(b, x.m + x.n))];
    }
    case 'powpow': case 'monoPow': {
      const b = f === 'powpow' ? x.b : V(x.v);
      return [S('Why it works: ' + m(P(Par(P(b, x.m)), x.n)) + ' is ' + x.n + ' copies of ' + m(P(b, x.m)) + ' multiplied, which adds ' + x.m + ' a total of ' + x.n + ' times.'),
        S('A power of a power: keep the base, multiply the exponents.', P(b, Ar(x.m, '×', x.n))),
        S(x.m + ' × ' + x.n + ' = ' + (x.m * x.n) + '.', P(b, x.m * x.n))];
    }
    case 'quot':
      return [S('Same base, dividing: keep the base and subtract the exponents, top minus bottom.', P(x.b, Ar(x.m, '−', x.n))),
        S(x.m + ' − ' + x.n + ' = ' + (x.m - x.n) + '.', P(x.b, x.m - x.n))];
    case 'zero':
      return [S('Why: a power divided by itself is 1, and the exponent rule gives ' + m(Eq(Fr(P(x.b, 2), P(x.b, 2)), P(x.b, Ar(2, '−', 2)))) + ' = ' + m(P(x.b, 0)) + '.'),
        S('So ' + m(P(x.b, 0)) + ' = 1.', N(1))];
    case 'fracpow':
      return [S('The exponent belongs to the whole fraction, so raise the top and the bottom.', Fr(P(x.p, x.k), P(x.q, x.k))),
        S(m(P(x.p, x.k)) + ' = ' + times(x.p, x.k) + ' = ' + ipow(x.p, x.k).n + ', and ' + m(P(x.q, x.k)) + ' = ' + times(x.q, x.k) + ' = ' + ipow(x.q, x.k).n + '.', Fr(N(String(ipow(x.p, x.k).n)), N(String(ipow(x.q, x.k).n))))];
    case 'zeroMix':
      return [S(m(P(x.a, 0)) + ' = 1, because any number except 0 to the zero power is 1.', Mul('·', N(1), P(x.c, 2))),
        S(m(P(x.c, 2)) + ' = ' + x.c + ' · ' + x.c + ' = ' + x.c * x.c + ', and 1 · ' + x.c * x.c + ' = ' + x.c * x.c + '.', N(x.c * x.c))];
    case 'powquot':
      return [S('Power of a power first: multiply the exponents, ' + x.p + ' × ' + x.q + ' = ' + x.p * x.q + '.', Fr(P(x.B, x.p * x.q), P(x.B, x.r))),
        S('Same base, dividing: subtract the exponents, ' + x.p * x.q + ' − ' + x.r + ' = ' + x.e + '.', P(x.B, x.e)),
        S('Find the value: ' + m(P(x.B, x.e)) + ' = ' + (x.e === 1 ? String(x.B) : times(x.B, x.e) + ' = ' + ipow(x.B, x.e).n) + '.', N(String(ipow(x.B, x.e).n)))];
    case 'solveN': {
      const n = V('n');
      return [S('Write ' + commas(String(x.V)) + ' as a power of ' + x.b + ': ' + commas(String(x.V)) + ' = ' + times(x.b, x.c) + ' = ' + m(P(x.b, x.c)) + '.', Eq(Fr(P(x.b, n), P(x.b, x.k)), P(x.b, x.c))),
        S('Dividing powers with the same base subtracts the exponents.', Eq(P(x.b, Ar(n, '−', x.k)), P(x.b, x.c))),
        S('The bases match, so the exponents must be equal.', Eq(Ar(n, '−', x.k), N(x.c))),
        S('Add ' + x.k + ' to both sides.', Eq(n, N(x.k + x.c))),
        S('Check: ' + m(Fr(P(x.b, x.k + x.c), P(x.b, x.k))) + ' = ' + m(P(x.b, x.c)) + ' = ' + commas(String(x.V)) + ' ✓')];
    }
    case 'negToFrac': case 'varNeg': {
      const b = f === 'negToFrac' ? x.b : V(x.v);
      return [S('Why: ' + m(Mul('·', P(b, x.n), P(b, -x.n))) + ' = ' + m(P(b, 0)) + ' = 1, so ' + m(P(b, -x.n)) + ' is the reciprocal of ' + m(P(b, x.n)) + '.'),
        S('Write one over the same power, with the exponent made positive.', Fr(1, P(b, x.n)))];
    }
    case 'negDen': {
      const b = Par(Neg(N(x.c)));
      return [S('The bottom is ' + m(P(b, -x.m)) + ', which is one over ' + m(P(b, x.m)) + '.', Fr(1, Fr(1, P(b, x.m)))),
        S('One over (one over something) is that something: the power moves up and its exponent is positive. The base ' + m(b) + ' keeps its parentheses.', P(b, x.m))];
    }
    case 'coefNeg':
      return [S('Only the 10 has the negative exponent: ' + m(P(10, -x.m)) + ' = one over ' + m(P(10, x.m)) + '.', Mul('·', N(x.k), Fr(1, P(10, x.m)))),
        S('Multiply. The ' + x.k + ' stays on top.', Fr(x.k, P(10, x.m)))];
    case 'coefVarNeg':
      return [S('Only <i>' + x.v + '</i> has the negative exponent: ' + m(P(V(x.v), -x.n)) + ' = one over ' + m(P(V(x.v), x.n)) + '.', Mul('·', N(x.c), Fr(1, P(V(x.v), x.n)))),
        S('Multiply. The ' + x.c + ' stays on top.', Fr(x.c, P(V(x.v), x.n)))];
    case 'negVal': {
      const v = ipow(x.b, x.n).n;
      return [S('A negative exponent means one over the power.', Fr(1, P(x.b, x.n))),
        S(m(P(x.b, x.n)) + ' = ' + times(x.b, x.n) + ' = ' + v + '.', Fr(1, N(String(v))))];
    }
    case 'negNegBase': {
      const b = Par(Neg(N(x.c))), v = ipow(x.c, x.e).n;
      return [S('A negative exponent means one over the power.', Fr(1, P(b, x.e))),
        S(m(P(b, x.e)) + ' = ' + times('-' + x.c, x.e) + '. That is ' + x.e + ' negative factors — an odd number — so it is negative: −' + v + '.', Fr(1, Neg(N(String(v))))),
        S('One over a negative number is negative. Write the sign in front.', Neg(Fr(1, N(String(v)))))];
    }
    case 'fracNeg': {
      const v = ipow(x.d, x.n).n;
      return [S('The negative exponent flips the fraction: ' + m(Fr(1, x.d)) + ' becomes ' + m(Fr(x.d, 1)) + ' = ' + x.d + ', and the exponent turns positive.', P(x.d, x.n)),
        S(m(P(x.d, x.n)) + ' = ' + times(x.d, x.n) + ' = ' + v + '.', N(String(v)))];
    }
    case 'mixedProd': {
      const s = x.m - x.n, v = ipow(x.B, -s).n;
      return [S('Same base, multiplying: add the exponents.', P(x.B, Ar(x.m, '+', -x.n))),
        S(x.m + ' + (−' + x.n + ') = ' + x.m + ' − ' + x.n + ' = −' + (-s) + '.', P(x.B, s)),
        S('A negative exponent means one over the power.', Fr(1, P(x.B, -s))),
        S(m(P(x.B, -s)) + ' = ' + (-s === 1 ? String(x.B) : times(x.B, -s) + ' = ' + v) + '.', Fr(1, N(String(v))))];
    }
    case 'monoCoefPow': {
      const v = V(x.v), cq = ipow(x.c, x.q).n;
      return [S('The exponent ' + x.q + ' applies to everything inside the parentheses: the ' + x.c + ' and the ' + m(P(v, x.p)) + '.', Mul('·', P(x.c, x.q), P(Par(P(v, x.p)), x.q))),
        S(m(P(x.c, x.q)) + ' = ' + times(x.c, x.q) + ' = ' + cq + '. Power of a power: ' + x.p + ' × ' + x.q + ' = ' + x.p * x.q + '.', Mul('', N(String(cq)), P(v, x.p * x.q)))];
    }
    case 'monoQuot': {
      const v = V(x.v);
      return [S('Split it: divide the numbers, and divide the powers of <i>' + x.v + '</i>.', Mul('·', Fr(x.k, x.j), Fr(P(v, x.p), P(v, x.q)))),
        S(x.k + ' ÷ ' + x.j + ' = ' + x.t + '. Same base, dividing: subtract the exponents.', Mul('', N(x.t), P(v, Ar(x.p, '−', x.q)))),
        S(x.p + ' − ' + x.q + ' = ' + (x.p - x.q) + '.', Mul('', N(x.t), P(v, x.p - x.q)))];
    }
    case 'monoNegPow': {
      const v = V(x.v), w = V(x.w), kq = ipow(x.k, x.q).n;
      return [S('Give the exponent ' + x.q + ' to every factor inside: ' + x.k + ', ' + m(P(v, -x.p)) + ' and <i>' + x.w + '</i>.', Mul('·', P(x.k, x.q), P(Par(P(v, -x.p)), x.q), P(w, x.q))),
        S(m(P(x.k, x.q)) + ' = ' + times(x.k, x.q) + ' = ' + kq + '. For <i>' + x.v + '</i>, multiply the exponents: (−' + x.p + ') × ' + x.q + ' = −' + x.p * x.q + ' (it stays negative).', Mul('', N(String(kq)), P(v, -x.p * x.q), P(w, x.q))),
        S('Move ' + m(P(v, -x.p * x.q)) + ' to the bottom, where its exponent turns positive.', Fr(Mul('', N(String(kq)), P(w, x.q)), P(v, x.p * x.q)))];
    }
    case 'toSci': {
      const val0 = qmul(qdec(x.c), ipow(10, x.k)), shown = commas(decStr(val0)), k = x.k;
      return [S('Put the decimal point just after the first nonzero digit. That gives ' + x.c + ', which is at least 1 and less than 10.'),
        k > 0 ? S('From ' + shown + ' to ' + x.c + ', the decimal point moves ' + k + ' places to the left. ' + shown + ' is big, so the exponent is positive: ' + k + '.', Sci(x.c, k))
              : S('From ' + shown + ' to ' + x.c + ', the decimal point moves ' + (-k) + ' places to the right. ' + shown + ' is less than 1, so the exponent is negative: −' + (-k) + '.', Sci(x.c, k)),
        S('Check: ' + m(Sci(x.c, k)) + ' means move the decimal point of ' + x.c + ' ' + Math.abs(k) + ' places ' + (k > 0 ? 'right' : 'left') + ', which gives back ' + shown + '. ✓')];
    }
    case 'toStd': case 'eNote': {
      const val0 = qmul(qdec(x.c), ipow(10, x.k)), k = x.k;
      const pre = f === 'eNote' ? [S(esc(x.c + 'E' + k) + ' means ' + m(Sci(x.c, k)) + '.', Sci(x.c, k))] : [];
      return pre.concat([S((k > 0 ? 'The exponent is +' + k + ': move the decimal point ' + k + ' places to the right' : 'The exponent is −' + (-k) + ': move the decimal point ' + (-k) + ' places to the left') + ', filling empty places with zeros.', numA(val0, { dec: true })),
        S('Check: ' + (k > 0 ? 'a positive exponent should give a big number.' : 'a negative exponent should give a number less than 1.') + ' ✓')]);
    }
    case 'ratio': {
      const R = qmul(qdec(x.t), ipow(10, x.p - x.q));
      return [S('“How many times larger” means divide the larger number by the smaller one.', Fr(Sci(x.A, x.p), Sci(x.B, x.q))),
        S('Divide the numbers and divide the powers of 10 separately.', Mul('×', Fr(x.A, x.B), Fr(P(10, x.p), P(10, x.q)))),
        S(x.A + ' ÷ ' + x.B + ' = ' + x.t + '. For the powers of 10, subtract the exponents: ' + sgn(x.p) + ' − ' + sgn(x.q) + ' = ' + (x.p - x.q) + '.', Sci(x.t, x.p - x.q)),
        S('As an ordinary number:', numA(R, { dec: true }))];
    }
    default: return null;
  }
}

/* ------------------------------------------------------------------ mistake models: exact results of exact mistakes */
/* each: { ex: the answer this mistake gives, if: 'you …' (what the mistake is, with the numbers), step: where in the solution it goes off,
           test?: a structural check that must also hold (used when two mistakes give the same value) } */
function models(part) {
  const f = part.fam, x = part.prm; if (!f || !x) return [];
  const L = [], add = (ex, iff, step, test) => L.push({ ex, if: iff, step, test });
  const negExpTyped = c => c.a && E.hasNegExp(c.a);
  const N = n => (typeof n === 'number' && n < 0) ? Neg(E.N(-n)) : E.N(n);      // a whole number that may come out negative
  switch (f) {
    case 'prod': case 'monoProd': {
      const b = f === 'prod' ? x.b : V(x.v);
      add(P(b, x.m * x.n), 'you multiply the exponents (' + x.m + ' × ' + x.n + ' = ' + x.m * x.n + '). Multiplying exponents is the rule for a power of a power, like ' + m(P(Par(P(b, x.m)), x.n)) + ' — not for ' + m(Mul('·', P(b, x.m), P(b, x.n))), 1);
      if (f === 'prod') { add(P(x.b * x.b, x.m + x.n), 'you multiply the bases (' + x.b + ' × ' + x.b + ' = ' + x.b * x.b + '). The base stays ' + x.b + '; only the exponents combine', 1);
        add(P(x.b * x.b, x.m * x.n), 'you multiply the bases (' + x.b + ' × ' + x.b + ') and also multiply the exponents (' + x.m + ' × ' + x.n + ')', 1); }
      if (f === 'monoProd') add(Mul('', N(2), P(b, x.m + x.n)), 'you add the two powers as if they were like terms. They are multiplied, not added, so there is no 2 in front', 1);
      add(P(b, x.m - x.n), 'you subtract the exponents (' + x.m + ' − ' + x.n + '). Subtracting is for dividing powers', 1);
      break;
    }
    case 'powpow': case 'monoPow': {
      const b = f === 'powpow' ? x.b : V(x.v);
      add(P(b, x.m + x.n), 'you add the exponents (' + x.m + ' + ' + x.n + ' = ' + (x.m + x.n) + '). For a power of a power, multiply them', 1);
      if (Math.pow(x.m, x.n) <= 60) add(P(b, Math.pow(x.m, x.n)), 'you raise ' + x.m + ' to the power ' + x.n + ' (' + m(P(x.m, x.n)) + ' = ' + Math.pow(x.m, x.n) + '). The exponents are multiplied, not raised', 1);
      break;
    }
    case 'quot':
      add(P(x.b, x.m + x.n), 'you add the exponents (' + x.m + ' + ' + x.n + '). For division, subtract them', 0);
      add(P(x.b, x.n - x.m), 'you subtract the wrong way (' + x.n + ' − ' + x.m + '). It is top minus bottom: ' + x.m + ' − ' + x.n, 1);
      if (x.m % x.n === 0) add(P(x.b, x.m / x.n), 'you divide the exponents (' + x.m + ' ÷ ' + x.n + '). Dividing powers subtracts the exponents', 0);
      add(N(1), 'you divide the bases (' + x.b + ' ÷ ' + x.b + ' = 1). The base stays ' + x.b, 0);
      add(P(x.b, x.m * x.n), 'you multiply the exponents. For division, subtract them', 0);
      break;
    case 'zero':
      add(N(0), 'you treat the zero exponent as “times 0”. An exponent of 0 gives 1, not 0', 1);
      add(N(x.b), 'you leave ' + x.b + ' as it is. A zero exponent gives 1', 1);
      break;
    case 'fracpow': {
      const pk = ipow(x.p, x.k).n, qk = ipow(x.q, x.k).n;
      add(Fr(x.p, N(String(qk))), 'you raise only the bottom to the power ' + x.k + '. The top gets it too: ' + m(P(x.p, x.k)), 0);
      add(Fr(N(String(pk)), x.q), 'you raise only the top to the power ' + x.k + '. The bottom gets it too: ' + m(P(x.q, x.k)), 0);
      add(Fr(x.p * x.k, x.q * x.k), 'you multiply the top and the bottom by ' + x.k + ' instead of raising them to the power ' + x.k + ' (that just gives back ' + m(Fr(x.p, x.q)) + ')', 1);
      add(Fr(x.p * x.k, N(String(qk))), 'you multiply the top by ' + x.k + ' (' + x.p + ' × ' + x.k + ') instead of raising it to the power ' + x.k, 1);
      add(Fr(N(String(pk)), x.q * x.k), 'you multiply the bottom by ' + x.k + ' (' + x.q + ' × ' + x.k + ') instead of raising it to the power ' + x.k, 1);
      break;
    }
    case 'zeroMix':
      add(N(0), 'you take ' + m(P(x.a, 0)) + ' as 0. It is 1, so the product is not 0', 0);
      add(N(x.a * x.c * x.c), 'you take ' + m(P(x.a, 0)) + ' as ' + x.a + '. It is 1', 0);
      add(N(2 * x.c), 'you work out ' + m(P(x.c, 2)) + ' as ' + x.c + ' × 2. It means ' + x.c + ' · ' + x.c, 1);
      add(N(x.c), 'you leave out the square: ' + m(P(x.c, 2)) + ' is ' + x.c + ' · ' + x.c, 1);
      add(N(1 + x.c * x.c), 'you add 1 + ' + x.c * x.c + '. The two parts are multiplied', 1);
      add(N(x.a + x.c * x.c), 'you take ' + m(P(x.a, 0)) + ' as ' + x.a + ' and add instead of multiplying', 0);
      break;
    case 'powquot': {
      const pq = x.p * x.q;
      add(P(x.B, x.p + x.q - x.r), 'you add the exponents inside (' + x.p + ' + ' + x.q + ') instead of multiplying them', 0);
      add(P(x.B, pq + x.r), 'you add the exponents when dividing (' + pq + ' + ' + x.r + '). For division, subtract', 1);
      add(P(x.B, x.r - pq), 'you subtract the wrong way (' + x.r + ' − ' + pq + '). It is top minus bottom: ' + pq + ' − ' + x.r, 1);
      add(P(x.B, pq), 'you work out the top, ' + m(P(x.B, pq)) + ', but do not divide by ' + m(P(x.B, x.r)), 1);
      add(N(x.B * x.e), 'you multiply ' + x.B + ' × ' + x.e + ' at the end. ' + m(P(x.B, x.e)) + ' means ' + (x.e === 1 ? x.B : times(x.B, x.e)), 2);
      break;
    }
    case 'solveN':
      add(N(x.c), 'you find the exponent of ' + commas(String(x.V)) + ' (' + commas(String(x.V)) + ' = ' + m(P(x.b, x.c)) + ') but forget that dividing by ' + m(P(x.b, x.k)) + ' already took ' + x.k + ' away from <i>n</i>', 2);
      add(N(x.c - x.k), 'you subtract ' + x.k + ' instead of adding it. From ' + m(Eq(Ar(V('n'), '−', x.k), N(x.c))) + ', add ' + x.k + ' to both sides', 3);
      add(N(x.c * x.k), 'you multiply ' + x.c + ' × ' + x.k + '. From ' + m(Eq(Ar(V('n'), '−', x.k), N(x.c))) + ', add ' + x.k + ' to both sides', 3);
      break;
    case 'negToFrac': case 'varNeg': {
      const b = f === 'negToFrac' ? x.b : V(x.v);
      add(Fr(1, P(b, -x.n)), 'you move the power to the bottom but keep its exponent negative. That flips it twice and gives back ' + m(P(b, x.n)) + '. Moving it is what makes the exponent positive', 1, negExpTyped);
      add(Neg(P(b, x.n)), 'you make the number negative. A negative exponent never makes a number negative; it means one over the power', 1);
      add(P(b, x.n), 'you just drop the minus sign from the exponent. ' + m(P(b, x.n)) + ' is the reciprocal of the answer: the power also has to go to the bottom', 1);
      if (f === 'negToFrac') add(Fr(1, N(x.b * x.n)), 'you multiply ' + x.b + ' × ' + x.n + '. The exponent is not a factor, and the question says do not evaluate', 1);
      add(Neg(Fr(1, P(b, x.n))), 'you write one over the power but also make it negative. A negative exponent does not make the number negative', 1);
      break;
    }
    case 'negDen': {
      const b = Par(Neg(N(x.c)));
      add(P(b, -x.m), 'you move the power up to the top but keep its exponent negative. Moving it is what makes the exponent positive', 1, negExpTyped);
      add(Fr(1, P(b, x.m)), 'you make the exponent positive but leave the power on the bottom. It moves to the top', 1);
      if (x.m % 2 === 1) add(P(x.c, x.m), 'you drop the negative sign of the base. The base is ' + m(b) + ', with its parentheses', 1);
      if (x.m % 2 === 0) add(Neg(P(x.c, x.m)), 'you leave out the parentheses. ' + m(Neg(P(x.c, x.m))) + ' means −(' + m(P(x.c, x.m)) + '), which is negative, but ' + m(P(b, x.m)) + ' is an even power of a negative, so it is positive', 1);
      break;
    }
    case 'coefNeg': case 'coefVarNeg': {
      const b = f === 'coefNeg' ? 10 : V(x.v), c = f === 'coefNeg' ? x.k : x.c, n = f === 'coefNeg' ? x.m : x.n;
      add(Fr(c, P(b, -n)), 'you move the power to the bottom but keep its exponent negative. That gives back ' + m(Mul(f === 'coefNeg' ? '·' : '', N(c), P(b, n))), 0, negExpTyped);
      add(Fr(1, Mul(f === 'coefNeg' ? '·' : '', N(c), P(b, n))), 'you move the ' + c + ' to the bottom too. Only ' + m(P(b, -n)) + ' has the negative exponent, so only it moves', 0);
      add(Mul(f === 'coefNeg' ? '·' : '', N(c), P(b, n)), 'you drop the minus sign from the exponent without moving the power. That is ' + m(P(b, n)) + ' on top, the reciprocal of what it should be', 0);
      add(Neg(Fr(c, P(b, n))), 'you make the number negative. A negative exponent means one over, not a negative number', 0);
      add(Neg(Mul(f === 'coefNeg' ? '·' : '', N(c), P(b, n))), 'you make the number negative instead of moving the power to the bottom', 0);
      break;
    }
    case 'negVal': {
      const v = ipow(x.b, x.n).n;
      add(Neg(N(String(v))), 'you make it negative: −' + v + '. A negative exponent means one over ' + m(P(x.b, x.n)) + ', not a negative number', 0);
      add(Neg(N(x.b * x.n)), 'you multiply ' + x.b + ' × ' + x.n + ' and make it negative. The exponent is not a factor, and a negative exponent does not make it negative', 0);
      add(Fr(1, N(x.b * x.n)), 'you take the reciprocal (good) but work out ' + m(P(x.b, x.n)) + ' as ' + x.b + ' × ' + x.n + '. It means ' + times(x.b, x.n), 1);
      add(N(String(v)), 'you drop the minus sign from the exponent. ' + v + ' is the reciprocal of the answer', 0);
      add(Neg(Fr(1, N(String(v)))), 'you take one over ' + v + ' (good) but also make it negative. A negative exponent does not make the value negative', 0);
      add(N(x.b * x.n), 'you multiply ' + x.b + ' × ' + x.n + ' and drop the negative exponent', 0);
      break;
    }
    case 'negNegBase': {
      const v = ipow(x.c, x.e).n;
      add(Fr(1, N(String(v))), 'you lose the sign. ' + m(P(Par(Neg(N(x.c))), x.e)) + ' has ' + x.e + ' negative factors — an odd number — so it is negative', 1);
      add(Neg(N(String(v))), 'you treat the negative exponent as making the number negative. It means one over the power', 0);
      add(N(String(v)), 'you drop the minus sign from the exponent and lose the sign of the base', 0);
      add(Neg(Fr(1, N(x.c * x.e))), 'you work out ' + m(P(x.c, x.e)) + ' as ' + x.c + ' × ' + x.e + '. It means ' + times(x.c, x.e), 1);
      add(Fr(1, N(x.c * x.e)), 'you work out the power as ' + x.c + ' × ' + x.e + ' and lose the sign', 1);
      break;
    }
    case 'fracNeg': {
      const v = ipow(x.d, x.n).n;
      add(Fr(1, N(String(v))), 'you make the exponent positive without flipping the fraction. The negative exponent is what flips it: ' + m(Fr(1, x.d)) + ' becomes ' + x.d, 0);
      add(Neg(N(String(v))), 'you flip the fraction (good) but make the answer negative. A negative exponent does not make the value negative', 0);
      add(Neg(Fr(1, N(String(v)))), 'you make the answer negative instead of flipping the fraction', 0);
      add(N(x.d * x.n), 'you flip the fraction (good) but work out ' + m(P(x.d, x.n)) + ' as ' + x.d + ' × ' + x.n + '. It means ' + times(x.d, x.n), 1);
      add(Fr(1, N(x.d * x.n)), 'you work out the power as ' + x.d + ' × ' + x.n + ' and do not flip the fraction', 0);
      break;
    }
    case 'mixedProd': {
      const s = x.n - x.m;
      add(P(x.B, s), 'you drop the minus sign from the exponent. ' + x.m + ' + (−' + x.n + ') = −' + s + ' is negative, so the answer is one over ' + m(P(x.B, s)) + ', not ' + m(P(x.B, s)) + ' itself', 1);
      add(Fr(1, P(x.B, x.m + x.n)), 'you add ' + x.m + ' + ' + x.n + '. The second exponent is −' + x.n + ': ' + x.m + ' + (−' + x.n + ') = −' + s, 1);
      add(P(x.B, x.m + x.n), 'you add ' + x.m + ' + ' + x.n + ' and drop the negative sign. The second exponent is −' + x.n, 1);
      add(Fr(1, P(x.B, x.m * x.n)), 'you multiply the exponents. Multiplying powers with the same base adds them: ' + x.m + ' + (−' + x.n + ')', 0);
      add(Neg(Fr(1, P(x.B, s))), 'you get one over the power (good) but make it negative. A negative exponent does not make the value negative', 2);
      add(Neg(P(x.B, s)), 'you treat the negative exponent as a negative number. It means one over the power', 2);
      break;
    }
    case 'monoCoefPow': {
      const v = V(x.v);
      add(Mul('', N(x.c), P(v, x.p * x.q)), 'you give the exponent only to the letter. The ' + x.c + ' is inside the parentheses too: ' + m(P(x.c, x.q)), 0);
      add(Mul('', N(x.c * x.q), P(v, x.p * x.q)), 'you work out ' + m(P(x.c, x.q)) + ' as ' + x.c + ' × ' + x.q + '. It means ' + times(x.c, x.q), 1);
      add(Mul('', N(String(ipow(x.c, x.q).n)), P(v, x.p + x.q)), 'you add the exponents ' + x.p + ' + ' + x.q + '. A power of a power multiplies them', 1);
      add(Mul('', N(x.c), P(v, x.p + x.q)), 'you add the exponents and leave the ' + x.c + ' without its exponent', 0);
      add(Mul('', N(x.c * x.q), P(v, x.p + x.q)), 'you multiply ' + x.c + ' × ' + x.q + ' and add the exponents ' + x.p + ' + ' + x.q, 1);
      break;
    }
    case 'monoQuot': {
      const v = V(x.v);
      add(Mul('', N(x.t), P(v, x.p + x.q)), 'you add the exponents ' + x.p + ' + ' + x.q + '. For division, subtract them', 1);
      if (x.k - x.j !== x.t) add(Mul('', N(x.k - x.j), P(v, x.p - x.q)), 'you subtract the numbers (' + x.k + ' − ' + x.j + '). Divide them: ' + x.k + ' ÷ ' + x.j, 1);
      add(Mul('', N(x.k), P(v, x.p - x.q)), 'you subtract the exponents (good) but leave ' + x.k + ' undivided. Divide the numbers too: ' + x.k + ' ÷ ' + x.j, 1);
      add(Mul('', N(x.t), P(v, x.q - x.p)), 'you subtract the exponents the wrong way (' + x.q + ' − ' + x.p + '). It is top minus bottom', 2);
      if (x.p % x.q === 0) add(Mul('', N(x.t), P(v, x.p / x.q)), 'you divide the exponents (' + x.p + ' ÷ ' + x.q + '). Subtract them', 1);
      add(Mul('', N(x.k * x.j), P(v, x.p + x.q)), 'you multiply the numbers and add the exponents, as if it were a product. It is a division', 1);
      break;
    }
    case 'monoNegPow': break;                                 /* handled part by part below */
    case 'toSci': {
      const want = qmul(qdec(x.c), ipow(10, x.k));
      add(E.N(x.c), 'you find the first number, ' + x.c + ', but leave off the power of 10. Multiply it by the power of 10 that gets back to ' + commas(decStr(want)), 1);
      break;
    }
    case 'toStd': case 'eNote': {
      const st = f === 'eNote' ? 1 : 0, want = qmul(qdec(x.c), ipow(10, x.k)), flip = qmul(qdec(x.c), ipow(10, -x.k));
      if (x.k < 0 && flip.d === 1n) add(Fr(1, E.N(String(flip.n))), 'you take one over ' + commas(String(flip.n)) + '. A negative exponent on 10 means move the decimal point of ' + x.c + ' to the left; the ' + x.c + ' does not go under a 1', st);
      if (x.k < 0) { add(Neg(numA(want, { dec: true })), 'you make the number negative. A negative exponent makes the number small (less than 1), not negative', st);
        add(Neg(numA(flip, { dec: true })), 'you move the decimal point right and make the number negative. A negative exponent means move it left: the number gets small, not negative', st); }
      break;
    }
    case 'ratio': {
      const t = qdec(x.t), A = qdec(x.A), Bq = qdec(x.B), big1 = qmul(A, ipow(10, x.p)), big2 = qmul(Bq, ipow(10, x.q));
      add(N(x.t), 'you divide ' + x.A + ' ÷ ' + x.B + ' = ' + x.t + ' but leave out the powers of 10. Divide those too (subtract the exponents)', 2);
      add(Sci(x.t, x.p + x.q), x.q < 0 ? 'you work out ' + sgn(x.p) + ' − ' + sgn(x.q) + ' as ' + (x.p + x.q) + '. Subtracting a negative is adding: ' + sgn(x.p) + ' + ' + (-x.q) + ' = ' + (x.p - x.q) : 'you add the exponents ' + x.p + ' + ' + x.q + '. Dividing powers of 10 subtracts them', 2);
      add(Fr(Sci(x.B, x.q), Sci(x.A, x.p)), 'you divide the wrong way (smaller ÷ larger). That answer is less than 1, but the first number is the larger one', 0);
      add(numA(E.qsub(big1, big2), { dec: true }), 'you subtract the two numbers. That tells how much larger, not how many times larger. “Times” means divide', 0);
      add(Mul('×', N(decStr(qmul(A, Bq))), P(10, x.p + x.q)), 'you multiply the two numbers. “How many times larger” means divide', 0);
      try { add(Mul('×', E.N(decStr(qdiv(Bq, A))), P(10, x.p - x.q)), 'you divide the smaller number by the larger one (' + x.B + ' ÷ ' + x.A + '). Divide the first number by the second: ' + x.A + ' ÷ ' + x.B, 2); } catch (e) { /* not a terminating decimal: no such answer can be typed exactly */ }
      break;
    }
    default: break;
  }
  /* a "mistake" whose value IS the answer is not a mistake */
  const L2 = vars(part.ans);
  return L.filter(md => { try { return !sameValue(md.ex, part.ans, L2); } catch (e) { return false; } }).map(md => Object.assign(md, { if: minus(md.if) }));
}

/* ------------------------------------------------------------------ part-by-part comparison (when no single mistake explains the answer) */
function partsFindings(part, c) {
  const f = part.fam, x = part.prm, out = []; let step = null;
  const say = (s, st) => { out.push(s); if (st !== undefined && st !== null && (step === null || st < step)) step = st; };
  if (!c.a) return null;
  /* powers of a known number base */
  const baseFam = { prod: [x.b, x.m + x.n, 'add the exponents: ' + x.m + ' + ' + x.n, 1], powpow: [x.b, x.m * x.n, 'multiply the exponents: ' + x.m + ' × ' + x.n, 1],
    quot: [x.b, x.m - x.n, 'subtract the exponents: ' + x.m + ' − ' + x.n, 1] }[f];
  if (baseFam) {
    const [b, e, how, st] = baseFam, sp = single(c.a);
    if (sp && !vars(c.a).length) {
      if (!qeq(sp.b, Q(b))) say('Your base is ' + mv(sp.b) + '. The base stays ' + b + ' — only the exponents change.', 0);
      else say('Your base ' + b + ' is right.');
      if (sp.e !== big(e)) say('Your exponent ' + sp.e + ' is not right. To get it, ' + how + '.', st);
      return { out, step };
    }
    const k = c.v ? logB(c.v, Q(b)) : null;
    if (k !== null) { say('Your answer equals ' + m(P(b, k)) + ', so the exponent ' + k + ' is off. To get it, ' + how + '.', st); return { out, step }; }
    return null;
  }
  /* monomials: the number part and each letter's exponent, one at a time */
  const monoFam = ['monoProd', 'monoPow', 'monoCoefPow', 'monoQuot', 'varNeg', 'coefVarNeg', 'monoNegPow'].indexOf(f) >= 0;
  if (monoFam) {
    const t = mono(c.a), r = mono(part.ans); if (!t || !r) return null;
    const how = monoHow(part);
    const ks = Object.keys(r.x);
    if (r.c.n === 1n && r.c.d === 1n && ks.length === 1 && Object.keys(t.x).length === 1 && t.x[ks[0]] === 1n && t.c.d === 1n && t.c.n === r.x[ks[0]]) {
      say('Did you mean ' + m(P(V(ks[0]), Number(r.x[ks[0]]))) + '? The exponent goes after ^: type ' + ks[0] + '^' + r.x[ks[0]] + '. Written in front, ' + t.c.n + ' multiplies <i>' + ks[0] + '</i>.', 1);
      return { out, step };
    }
    if (qeq(t.c, qmul(Q(-1), r.c))) say('Your number part has the wrong sign (' + mv(t.c) + ').' + (NEG_FAMS[f] ? ' A negative exponent never makes a number negative.' : ' Nothing in this question makes it negative.'), 0);
    else if (!qeq(t.c, r.c)) {
      const known = (how.coefKnown || []).find(kq => qeq(kq[0], t.c));
      say('Your number part is ' + mv(t.c) + '. ' + (known ? 'That is what you get if ' + known[1] + '.' : how.coef), how.coefStep);
    } else if (!(r.c.n === 1n && r.c.d === 1n)) say('Your number part ' + mv(t.c) + ' is right.');
    const letters = Object.keys(Object.assign({}, r.x, t.x)).sort();
    letters.forEach(l => {
      const te = t.x[l] || 0n, re = r.x[l] || 0n, li = '<i>' + l + '</i>';
      if (te === re) { say('The exponent on ' + li + ' is right.'); return; }
      const h = how.x[l] || { how: '', known: [], step: 0 };
      const known = (h.known || []).find(kn => kn[0] === te);
      const where = te === 0n ? 'Your answer has no ' + li + ' left in it.' : 'Your exponent on ' + li + ' works out to ' + String(te).replace('-', '−') + (te < 0n ? ' (it is on the bottom)' : '') + '.';
      say(where + ' ' + (known ? 'That is what you get if ' + known[1] + '.' : h.how), h.step);
    });
    return { out, step };
  }
  if (f === 'coefNeg') {
    const sp = single(c.a);
    if (sp && !qeq(sp.b, Q(10))) { say('Only the 10 has the exponent −' + x.m + '. The ' + x.k + ' is a separate factor in front: it is not raised to any power, and it stays on top.', 0); return { out, step }; }
    return null;
  }
  /* scientific notation */
  if (f === 'toSci') {
    const want = qmul(qdec(x.c), ipow(10, x.k)), s = sciOf(c.a);
    if (!s) { say('This needs to be in scientific notation: a number at least 1 and less than 10, times a power of 10.' + (c.v && !qeq(c.v, want) ? ' (Your number is also not equal to ' + commas(decStr(want)) + '.)' : ''), 0); return { out, step }; }
    const dT = digitsOf(s.c), dW = digitsOf(qdec(x.c));
    const inRange = !qlt(s.c, Q(1)) && qlt(s.c, Q(10));
    if (dT !== dW) say('Your first number ' + esc(s.cs) + ' has different digits. Scientific notation keeps the digits of ' + commas(decStr(want)) + ' in order: ' + dW.split('').join(', ') + '.', 0);
    else if (!inRange) say('Your first number ' + esc(s.cs) + ' is not at least 1 and less than 10. Put the decimal point just after the first digit.', 0);
    else say('Your first number ' + esc(s.cs) + ' is right.');
    const kS = Number(s.k), sh = inRange ? kS : null;
    if (sh !== null && kS !== x.k) {
      const zeros = x.k > 0 ? (decStr(want).match(/0+$/) || [''])[0].length : ((decStr(want).split('.')[1] || '').match(/^0*/) || [''])[0].length;
      if (kS === -x.k) say('Your exponent has the wrong sign. ' + (x.k > 0 ? 'The number is big, so the exponent is positive.' : 'The number is less than 1, so the exponent is negative.'), 1);
      else if (Math.abs(kS) === zeros && Math.sign(kS) === Math.sign(x.k) && zeros !== Math.abs(x.k)) say('Your exponent ' + String(kS).replace('-', '−') + ' counts the zeros ' + (x.k > 0 ? 'at the end of the number' : 'after the decimal point') + ' (' + zeros + '). The exponent counts the places the decimal point moves, which is not the same.', 1);
      else say('Your exponent ' + String(kS).replace('-', '−') + ' is off. Count the places the decimal point moves to land just after the first digit.', 1);
    } else if (sh !== null) say('Your exponent is right.');
    return { out, step };
  }
  if (f === 'toStd' || f === 'eNote') {
    const want = qmul(qdec(x.c), ipow(10, x.k));
    if (c.a && E.hasPow(c.a)) { say('Write it as an ordinary number, with no power of 10: start from ' + x.c + ' and move the decimal point ' + Math.abs(x.k) + ' places ' + (x.k > 0 ? 'right' : 'left') + '.', f === 'eNote' ? 1 : 0); return { out, step }; }
    if (!c.v || unwrap(c.a).t !== 'n') return null;
    const j = tenPow(qdiv(c.v, want));
    if (j !== null && j !== 0) {
      if (qeq(c.v, qmul(qdec(x.c), ipow(10, -x.k)))) say('You moved the decimal point the wrong way. ' + (x.k > 0 ? 'A positive exponent makes the number bigger: move it right.' : 'A negative exponent makes the number smaller: move it left.'), f === 'eNote' ? 1 : 0);
      else say('Your digits are right, but the decimal point is ' + Math.abs(j) + ' place' + (Math.abs(j) === 1 ? '' : 's') + ' too far to the ' + (j > 0 ? 'right' : 'left') + '. Move it exactly ' + Math.abs(x.k) + ' places from where it is in ' + x.c + '.', f === 'eNote' ? 1 : 0);
      return { out, step };
    }
    const dT = digitsOf(c.v), dW = digitsOf(want);
    if (dT !== dW) { say('Your digits changed. The answer uses the digits ' + dW.split('').join(', ') + ' (from ' + x.c + '), with zeros only to fill places.', f === 'eNote' ? 1 : 0); return { out, step }; }
    return null;
  }
  if (f === 'ratio') {
    if (!c.v || c.v.n <= 0n) return null;
    const t = qdec(x.t), nt = normSci(c.v);
    if (qeq(nt.d, t)) { say('Your ' + x.t + ' is right, but the power of 10 is off (yours works out to ' + m(P(10, nt.j)) + '). Subtract the exponents: ' + sgn(x.p) + ' − ' + sgn(x.q) + '.', 2); return { out, step }; }
    if (nt.j === x.p - x.q) { say('Your power of 10 is right, but the number part is off. Divide ' + x.A + ' ÷ ' + x.B + '.', 2); return { out, step }; }
    return null;
  }
  return null;
}
/* how each piece of a monomial answer is made, and the wrong values each piece commonly gets */
function monoHow(part) {
  const f = part.fam, x = part.prm, B = big;
  const L = s => '<i>' + s + '</i>';
  switch (f) {
    case 'monoProd': return { coef: '', x: { [x.v]: { how: 'Multiplying the same base: add the exponents, ' + x.m + ' + ' + x.n + '.', step: 1, known: [[B(x.m * x.n), 'you multiply the exponents']] } } };
    case 'monoPow': return { coef: '', x: { [x.v]: { how: 'Power of a power: multiply the exponents, ' + x.m + ' × ' + x.n + '.', step: 1, known: [[B(x.m + x.n), 'you add the exponents']] } } };
    case 'monoCoefPow': return { coef: 'The ' + x.c + ' gets the exponent too: work out ' + m(P(x.c, x.q)) + ' = ' + times(x.c, x.q) + '.', coefStep: 1,
      coefKnown: [[Q(B(x.c)), 'you leave the ' + x.c + ' without its exponent ' + x.q], [Q(B(x.c * x.q)), 'you multiply ' + x.c + ' × ' + x.q + ' instead of ' + times(x.c, x.q)]],
      x: { [x.v]: { how: 'Power of a power: multiply the exponents, ' + x.p + ' × ' + x.q + '.', step: 1, known: [[B(x.p + x.q), 'you add ' + x.p + ' + ' + x.q + ' instead of multiplying']] } } };
    case 'monoQuot': return { coef: 'Divide the numbers: ' + x.k + ' ÷ ' + x.j + '.', coefStep: 1,
      coefKnown: [[Q(B(x.k - x.j)), 'you subtract ' + x.k + ' − ' + x.j], [Q(B(x.k)), 'you leave ' + x.k + ' undivided'], [Q(B(x.k * x.j)), 'you multiply ' + x.k + ' × ' + x.j]],
      x: { [x.v]: { how: 'Dividing the same base: subtract the exponents, ' + x.p + ' − ' + x.q + '.', step: 2, known: [[B(x.p + x.q), 'you add the exponents'], [B(x.q - x.p), 'you subtract bottom minus top']] } } };
    case 'varNeg': return { coef: 'A negative exponent does not make the answer negative or change the number in front.', coefStep: 1,
      x: { [x.v]: { how: L(x.v) + ' should end up on the bottom with a positive exponent ' + x.n + '.', step: 1, known: [[B(x.n), 'you drop the minus sign but leave ' + L(x.v) + ' on top']] } } };
    case 'coefVarNeg': return { coef: 'Only ' + L(x.v) + ' has the negative exponent, so the ' + x.c + ' stays on top unchanged.', coefStep: 0,
      coefKnown: [[Q(1n, B(x.c)), 'you move the ' + x.c + ' to the bottom too'], [Q(B(-x.c)), 'you make the number negative']],
      x: { [x.v]: { how: L(x.v) + ' should end up on the bottom with a positive exponent ' + x.n + '.', step: 0, known: [[B(x.n), 'you drop the minus sign but leave ' + L(x.v) + ' on top']] } } };
    case 'monoNegPow': return { coef: 'The ' + x.k + ' gets the exponent too: ' + m(P(x.k, x.q)) + ' = ' + times(x.k, x.q) + '.', coefStep: 1,
      coefKnown: [[Q(B(x.k)), 'you leave the ' + x.k + ' without the exponent ' + x.q], [Q(B(x.k * x.q)), 'you multiply ' + x.k + ' × ' + x.q + ' instead of ' + times(x.k, x.q)]],
      x: { [x.v]: { how: 'Multiply the exponents (−' + x.p + ') × ' + x.q + ' — the result stays negative, so ' + L(x.v) + ' ends up on the bottom.', step: 1,
              known: [[B(-x.p + x.q), 'you add (−' + x.p + ') + ' + x.q + ' instead of multiplying'], [B(x.p * x.q), 'you lose the minus sign: (−' + x.p + ') × ' + x.q + ' is negative'], [B(-x.p), 'you do not give ' + L(x.v) + ' the outside exponent ' + x.q]] },
           [x.w]: { how: L(x.w) + ' is inside the parentheses, so it gets the exponent ' + x.q + ' too.', step: 1, known: [[1n, 'you do not give ' + L(x.w) + ' the outside exponent ' + x.q]] } } };
    default: return { coef: '', x: {} };
  }
}

/* ------------------------------------------------------------------ "right value, wrong form": say exactly how to fix the form */
function formFix(part, c, msg) {
  const f = part.fam, x = part.prm;
  if (part.kind === 'sci' && c.a) {
    const s = sciOf(c.a);
    if (s) {
      if (!qlt(s.c, Q(10))) { let j = 0, cc = s.c; while (!qlt(cc, Q(10))) { cc = qdiv(cc, Q(10)); j++; }
        return 'You wrote ' + m(Mul('×', E.N(s.cs), P(10, Number(s.k)))) + '. ' + esc(s.cs) + ' is not less than 10. Move its decimal point ' + j + ' place' + (j > 1 ? 's' : '') + ' left (' + decStr(cc) + ') and add ' + j + ' to the exponent (' + m(P(10, Number(s.k) + j)) + '). The value stays the same.'; }
      if (qlt(s.c, Q(1))) { let j = 0, cc = s.c; while (qlt(cc, Q(1))) { cc = qmul(cc, Q(10)); j++; }
        return 'You wrote ' + m(Mul('×', E.N(s.cs), P(10, Number(s.k)))) + '. ' + esc(s.cs) + ' is less than 1. Move its decimal point ' + j + ' place' + (j > 1 ? 's' : '') + ' right (' + decStr(cc) + ') and subtract ' + j + ' from the exponent (' + m(P(10, Number(s.k) - j)) + '). The value stays the same.'; }
    }
    if (c.v && unwrap(c.a).t === 'n') return 'That is the same number written out. Scientific notation needs a number at least 1 and less than 10, times a power of 10.';
  }
  if (part.kind === 'power' && c.v) {
    const sp = single(c.a);
    const u = unwrap(c.a), bu = u.t === 'pow' ? unwrap(u.b) : null;
    if (bu && bu.t === 'pow') return 'Right value, but there is still a power inside a power. Multiply the exponents to make one power of ' + part.base + ', with one exponent.';
    if (u.t === 'pow' && literalInt(u.e) === null && bu && bu.t === 'n' && qeq(bu.q, Q(part.base))) return 'Right value. Now work out the exponent to a single number.';
    if (sp && !qeq(sp.b, Q(part.base))) return 'Your answer has the right value, but it is a power of ' + mv(sp.b) + '. The question wants a single power of ' + part.base + ': keep the base ' + part.base + ' and combine the exponents.';
    if (E.hasPow(c.a)) return 'Right value, but it is not one power yet. Combine it into a single power of ' + part.base + ': one base, one exponent.';
    if (!sp) return 'Your answer has the right value, but the question wants it as a single power of ' + part.base + ' (like ' + m(P(part.base, V('k'))) + '), not worked out.';
  }
  if (part.kind === 'value' && c.a) {
    const u = unwrap(c.a);
    if (u.t === 'div' && unwrap(u.a).t === 'n' && unwrap(u.b).t === 'n' && c.v) {
      const a = unwrap(u.a).q, b = unwrap(u.b).q;
      if (a.d === 1n && b.d === 1n && b.n !== 0n) { const g = E.gcd(a.n, b.n); if (g > 1n) return 'Right value. ' + a.n + ' and ' + b.n + ' are both divisible by ' + g + ': divide the top and the bottom by ' + g + '.'; }
    }
  }
  return msg;
}

/* ------------------------------------------------------------------ the feedback for one typed answer */
function ctxOf(part, text) {
  const xT = part.kind === 'sci' || part.kind === 'std' || part.kind === 'times' || !vars(part.ans).length;
  const segs = String(text || '').split('=').map(s => s.trim()).filter(s => !(part.kind === 'n' && /^n$/i.test(s)));
  let a = null; try { a = E.parse(segs[segs.length - 1] || '', xT); } catch (e) { a = null; }
  return { a, v: a ? val(a) : null, letters: vars(part.ans) };
}
/* a whole number or a fraction of whole numbers, as written (signs gathered in front): 2/8 → {n: 2, d: 8}; 1/−8 → {n: −1, d: 8} */
function simpleFrac(a) {
  a = unwrap(a); let s = 1n;
  while (a.t === 'neg') { s = -s; a = unwrap(a.x); }
  const int = x => { x = unwrap(x); let t = 1n; while (x.t === 'neg') { t = -t; x = unwrap(x.x); } return x.t === 'n' && x.q.d === 1n ? t * x.q.n : null; };
  if (a.t === 'n') return a.q.d === 1n ? { n: s * a.q.n, d: 1n } : null;
  if (a.t === 'div' || a.t === 'frac') { const n = int(a.t === 'div' ? a.a : a.n), d = int(a.t === 'div' ? a.b : a.d); if (n === null || d === null || d === 0n) return null;
    return d < 0n ? { n: -s * n, d: -d } : { n: s * n, d }; }
  return null;
}
/* a mistake explains an answer only if the answer has that mistake's SHAPE as well as its value:
   1/b^-n is not "dropped the sign", 8^16 is not "multiplied the bases", 2/8 is not "raised only the top" */
function shapeOK(md, c, loose) {
  if (!loose && E.hasNegExp(c.a) !== E.hasNegExp(md.ex)) return false;   /* in worked lines (loose) a negative exponent may still be on its way out */
  const st = single(c.a), sx = single(md.ex);
  if (st && sx) return qeq(st.b, sx.b) && st.e === sx.e;
  if (st && !sx && !vars(md.ex).length) return false;
  const ft = simpleFrac(c.a), fx = simpleFrac(md.ex);
  if (ft && fx) return ft.n === fx.n && ft.d === fx.d;
  return true;
}
function matches(md, c, loose) {
  if (!c.a) return false;
  try { if (!sameValue(c.a, md.ex, c.letters)) return false; } catch (e) { return false; }
  if (!shapeOK(md, c, loose)) return false;
  return md.test ? !!md.test(c) : true;
}
/* where the negative exponents sit in an answer: on top, or on the bottom of a fraction */
function negPlaces(a) {
  const r = { top: false, bottom: false };
  (function go(x, top) {
    x = unwrap(x);
    if (x.t === 'div' || x.t === 'frac') { go(x.t === 'div' ? x.a : x.n, top); go(x.t === 'div' ? x.b : x.d, !top); return; }
    if (x.t === 'mul') { x.xs.forEach(y => go(y, top)); return; }
    if (x.t === 'neg') { go(x.x, top); return; }
    if (x.t === 'pow') { const e = literalInt(x.e); if (e !== null && e < 0n) { if (top) r.top = true; else r.bottom = true; } go(x.b, top); }
  })(a, true);
  return r;
}
/* typing slips that are not math mistakes: not counted as a try */
function notation(part, raw) {
  const kindSci = part.kind === 'sci' || part.kind === 'std' || part.kind === 'times';
  if (/\^\s*-?\s*\d+(?:\.\d+)?\s*\^/.test(raw)) return 'Two ^ in a row is hard to read. For a power of a power, multiply the exponents and write one ^: ' + m(Eq(P(Par(P(a_, 4)), 7), P(a_, 28))) + '.';
  if (vars(part.ans).length) { const mm = /([a-zA-Z])(\d+)/.exec(raw); if (mm && !/\^/.test(raw.slice(mm.index - 1, mm.index))) return 'It looks like the ^ is missing in “' + esc(mm[0]) + '”. Type ' + esc(mm[1]) + '^' + mm[2] + ' for ' + m(P(V(mm[1].toLowerCase()), +mm[2])) + '.'; }
  if (/(?:[x×*]\s*)10(\d+)\s*$/i.test(raw) && !/10\s*\^/.test(raw)) { const mm = /10(\d+)\s*$/.exec(raw); return 'Put ^ before the exponent: type 10^' + mm[1] + ', not 10' + mm[1] + '.'; }
  if (/\d\s*[eE]\s*[-+−]?\s*\d/.test(raw) && !vars(part.ans).length) return 'E is calculator shorthand. Write it with × 10 and ^, like 5.6 x 10^8.';
  if (part.kind === 'n' && /n/i.test(raw) && raw.split('=').map(s => s.trim()).filter(s => !/^n$/i.test(s)).some(s => /n/i.test(s))) return 'Good setup. Now solve it: get <i>n</i> by itself, then type just the number.';
  return null;
}
const POWER_FAMS = { prod: 1, powpow: 1, quot: 1 };
const NEG_FAMS = { negToFrac: 1, negDen: 1, coefNeg: 1, varNeg: 1, coefVarNeg: 1, monoNegPow: 1 };
function hasNegIn(a) { return E.plain(a).indexOf('-') >= 0; }
function feedback(part, text, opts) {
  const loose = !!(opts && opts.loose) && !NEG_FAMS[part.fam];   /* where negative exponents are the point, their presence always matters */
  const raw = String(text || '').trim();
  const base = { what: [], rule: RULE[part.fam] ? RULE[part.fam]() : '', step: null };
  /* a. typing slips: not a math mistake, not counted */
  if (raw && part.fam) { const n = notation(part, raw); if (n) return Object.assign(base, { v: 'unread', msg: n, what: [n] }); }
  const r = E.mark(part, text);
  const out = Object.assign(base, { v: r.v, msg: r.msg || '' });
  if (r.v === 'right' || r.v === 'blank' || r.v === 'unread' || !part.fam) { if (r.msg) out.what = [r.msg]; return out; }
  const c = ctxOf(part, text), x = part.prm, f = part.fam;
  if (r.v === 'form') { out.what = [formFix(part, c, r.msg)]; return out; }
  if (/something you set equal/.test(r.msg) || /letter/.test(r.msg)) { out.what = [r.msg]; return out; }
  const say = (v, what, step) => Object.assign(out, { v, what: [].concat(what), step: step == null ? null : step });
  /* b. the n-question: the power written out instead of n */
  if (f === 'solveN' && c.a) {
    const sp = single(c.a), nAns = x.k + x.c;
    if ((sp && qeq(sp.b, Q(x.b)) && sp.e === big(nAns)) || (c.v && qeq(c.v, ipow(x.b, nAns)) && nAns > 1))
      return say('form', 'That is ' + m(P(x.b, V('n'))) + ' with your <i>n</i> put in. The question asks for <i>n</i> itself — just the exponent.', 3);
    if (sp) return say('wrong', '<i>n</i> is a number — the exponent — not a power. Type just the number.', 2);
  }
  /* c. power questions: just the exponent, or a sum that needs parentheses */
  if (POWER_FAMS[f] && c.a) {
    const e = { prod: x.m + x.n, powpow: x.m * x.n, quot: x.m - x.n }[f];
    if (c.v && c.v.d === 1n && c.v.n === big(e) && unwrap(c.a).t === 'n') return say('form', 'That is the exponent. Write the whole power, keeping the base: ' + x.b + '^' + e + '.', 1);
    const mm = /^\s*(\d+)\s*\^\s*(\d+)\s*([+\-−*×·])\s*(\d+)\s*$/.exec(raw);
    if (mm) return say('wrong', 'If the exponent is meant to be ' + mm[2] + ' ' + mm[3].replace('-', '−').replace('*', '×') + ' ' + mm[4] + ', it needs parentheses: ' + mm[1] + '^(' + mm[2] + mm[3] + mm[4] + '). As typed, it means ' + m(P(+mm[1], +mm[2])) + ' and then ' + { '+': 'plus', '-': 'minus', '−': 'minus', '*': 'times', '×': 'times', '·': 'times' }[mm[3]] + ' ' + mm[4] + '.', 1);
  }
  /* d. both the top and the bottom negative */
  if (c.a && c.v) {
    const u = unwrap(c.a);
    if (u.t === 'div' || u.t === 'frac') {
      const tv = val(u.t === 'div' ? u.a : u.n), bv = val(u.t === 'div' ? u.b : u.d);
      if (tv && bv && tv.n < 0n && bv.n < 0n) {
        let want = null; try { want = evalA(part.ans, {}); } catch (e) { }
        return say('wrong', 'The top and the bottom of your fraction are both negative, so the two signs cancel and the value is positive.' + (want && want.n < 0n ? ' The answer is negative: only one minus sign belongs, in front.' : ' Leave both minus signs out.'), null);
      }
    }
  }
  /* e. exact mistakes, matched by value AND shape */
  let hit = models(part).filter(md => matches(md, c, loose));
  if (hit.some(h => h.test)) hit = hit.filter(h => h.test);
  if (hit.length) {
    const uniq = []; hit.forEach(h => { if (!uniq.some(u => u.if === h.if)) uniq.push(h); });
    return say('wrong', 'That is what you get if ' + uniq.map(h => h.if).join('. Or, if ') + '.', Math.min.apply(null, uniq.map(h => h.step)));
  }
  /* f. negative exponents left in an answer that must have only positive ones */
  if (c.a && (NEG_FAMS[f] || part.kind === 'posexp') && E.hasNegExp(c.a)) {
    const np = negPlaces(c.a), w = [];
    if (np.bottom) w.push('A power with a negative exponent is on the bottom of your fraction. Moving a power across the fraction bar is what turns its exponent positive, so once it is on the bottom its exponent should be positive.');
    if (np.top && !(opts && opts.loose)) w.push('Your answer still has a negative exponent on top. A negative exponent means one over the power: move that power to the bottom and make its exponent positive.');
    if (unwrap(c.a).t === 'neg') w.push((w.length ? 'Also, the' : 'The') + ' minus sign in front makes the value negative. A negative exponent never does that.');
    if (w.length) return say('wrong', w, NEG_FAMS[f] ? 0 : null);
  }
  /* g. piece by piece */
  const pf = partsFindings(part, c);
  if (pf && pf.out.length && pf.out.some(s0 => !/ is right\.$/.test(s0))) return say('wrong', pf.out, pf.step);
  /* h. facts about the answer as a whole */
  const want = (() => { try { return c.letters.length ? null : evalA(part.ans, {}); } catch (e) { return null; } })();
  if (c.v && want) {
    const qNeg = hasNegIn(part.q);
    if (qeq(c.v, qmul(Q(-1), want))) return say('wrong', 'Your answer is the right size but has the wrong sign. ' + (qNeg ? 'Check each step where a negative sign appears: a negative exponent never makes a number negative, and an odd power of a negative number is negative.' : 'Nothing in this question is negative, so the answer cannot be.'), null);
    if (want.n !== 0n && qeq(c.v, qdiv(Q(1), want))) return say('wrong', 'Your answer is upside down: it is the reciprocal of the right answer. Check which part belongs on the top and which on the bottom.', null);
    if (want.n !== 0n && qeq(c.v, qdiv(Q(-1), want))) return say('wrong', 'Your answer is upside down and has the wrong sign.', null);
  }
  if (f === 'solveN' && c.v && c.v.d === 1n && c.v.n >= -30n && c.v.n <= 40n) {
    const n0 = Number(c.v.n), got = ipow(x.b, n0 - x.k);
    return say('wrong', 'Check it: if <i>n</i> = ' + String(n0).replace('-', '−') + ', then ' + m(Fr(P(x.b, n0), P(x.b, x.k))) + ' = ' + m(P(x.b, n0 - x.k)) + ' = ' + mv(got) + ', not ' + commas(String(x.V)) + '.', 2);
  }
  if (c.a && E.hasPow(c.a) && part.kind === 'value') return say('wrong', 'Your answer still has a power in it, and it is not equal to the question. Work it out step by step — tap Hint for the first step.', null);
  return say('wrong', 'That is not it, and it does not match a common slip. Tap Hint to see the first step.', null);
}

/* ------------------------------------------------------------------ multiple choice and select-all */
function mcFeedback(item, k) {
  const right = k === item.correct;
  const out = { v: right ? 'right' : 'wrong', what: [], rule: RULE[item.fam] ? RULE[item.fam]() : '', step: null };
  if (right) return out;
  const fake = { fam: item.fam, prm: item.prm, ans: item.opts[item.correct], kind: 'mc' };
  const hit = item.fam ? models(fake).filter(md => { try { return sameValue(item.opts[k], md.ex, vars(fake.ans)); } catch (e) { return false; } }) : [];
  out.what = [item.why[k] || 'Not this one.'];
  if (hit.length && item.fam !== 'toSci') out.step = Math.min.apply(null, hit.map(h => h.step));
  return out;
}
function describeOption(o) {                    /* what a select-all choice equals, and why, in one line */
  const v = evalA(o, {}), u = unwrap(o);
  let why = '';
  if (u.t === 'neg') why = ' A minus sign in front of a power makes the value negative.';
  else if (u.t === 'pow' && literalInt(u.e) !== null && literalInt(u.e) < 0n) why = ' A negative exponent means one over ' + m(P(unwrap(u.b).t === 'n' ? unwrap(u.b) : u.b, -literalInt(u.e))) + '.';
  else if (u.t === 'pow') why = ' A fraction to a power: raise the top and the bottom.';
  return m(o) + ' = ' + mv(v) + '.' + why;
}
function selectFeedback(item, picked, tries) {
  const want = item.correct, got = picked.map(Number);
  const extra = got.filter(k => want.indexOf(k) < 0), missing = want.filter(k => got.indexOf(k) < 0);
  const out = { v: (!extra.length && !missing.length) ? 'right' : 'wrong', what: [], rule: RULE.select(), step: null };
  if (out.v === 'right') return out;
  const LET = 'ABCDE';
  if (tries < 2) {
    if (extra.length) out.what.push(extra.length === 1 ? 'One of your picks is not equal to ' + m(item.target) + '.' : extra.length + ' of your picks are not equal to ' + m(item.target) + '.');
    if (missing.length) out.what.push(missing.length === 1 ? 'One more choice is equal to it.' : missing.length + ' more choices are equal to it.');
    out.what.push('Work out the value of each choice on its own, then compare.');
  } else {
    extra.forEach(k => out.what.push('<b>' + LET[k] + '</b> is not equal: ' + describeOption(item.opts[k])));
    if (missing.length) out.what.push(missing.length === 1 ? 'You are still missing one: check the choices you did not pick.' : 'You are still missing ' + missing.length + ': check the choices you did not pick.');
  }
  return out;
}
function selectSolution(item) {
  const LET = 'ABCDE';
  return item.opts.map((o, k) => ({ say: '<b>' + LET[k] + '.</b> ' + describeOption(o) + (item.correct.indexOf(k) >= 0 ? ' <span class="ok">✓ equal</span>' : ' <span class="no">✗ not equal</span>'), ex: null }));
}
function mcSolution(item) {
  if (item.fam === 'select') return selectSolution(item);
  if (!item.fam) return null;
  const fake = { fam: item.fam, prm: item.prm, kind: 'mc' };
  const s = solution(fake);
  return s;
}

/* every shown sentence: a hyphen before a number is a minus sign */
const minus = s => typeof s === 'string' ? s.replace(/(^|[\s(>=])-(\d)/g, '$1−$2') : s;
function tidyOut(f) { if (f && f.what) f.what = f.what.map(minus); return f; }
function tidySol(sol) { if (sol) sol.forEach(s => { s.say = minus(s.say); }); return sol; }
/* ------------------------------------------------------------------ "Help me solve this": checking a student's own work, line by line */
function atomish(a) { return a.t === 'n' || a.t === 'v' || a.t === 'pow' || a.t === 'par'; }
function typedOf(a) {                                       /* an expression as a student would type it */
  switch (a.t) {
    case 'n': return a.s;
    case 'v': return a.s;
    case 'pow': { const b = a.b.t === 'n' || a.b.t === 'v' ? typedOf(a.b) : '(' + typedOf(a.b.t === 'par' ? a.b.x : a.b) + ')';
      const e = a.e.t === 'n' ? a.e.s : a.e.t === 'neg' && a.e.x.t === 'n' ? '-' + a.e.x.s : '(' + typedOf(a.e) + ')'; return b + '^' + e; }
    case 'mul': return a.xs.map(x => x.t === 'neg' || x.t === 'frac' || x.t === 'ar' ? '(' + typedOf(x) + ')' : typedOf(x)).join(a.op === '' ? '' : a.op === '×' ? ' x ' : '*');
    case 'frac': case 'div': { const nn = a.t === 'frac' ? a.n : a.a, dd = a.t === 'frac' ? a.d : a.b;
      return (atomish(nn) ? typedOf(nn) : '(' + typedOf(nn) + ')') + '/' + (atomish(dd) ? typedOf(dd) : '(' + typedOf(dd) + ')'); }
    case 'neg': return '-' + (atomish(a.x) ? typedOf(a.x) : '(' + typedOf(a.x) + ')');
    case 'par': return '(' + typedOf(a.x) + ')';
    case 'ar': return typedOf(a.a) + ({ '+': '+', '−': '-', '×': '*' })[a.op] + (a.b.t === 'par' ? typedOf(a.b) : typedOf(a.b));
    case 'eq': return typedOf(a.l) + ' = ' + typedOf(a.r);
  }
  return '';
}
/* a canonical spelling of a parsed expression, for "which worked step is this line?" */
function canon(a) {
  a = unwrap(a);
  switch (a.t) {
    case 'n': return decStr(a.q);
    case 'v': return a.s;
    case 'pow': return '(' + canon(a.b) + ')^(' + canon(a.e) + ')';
    case 'mul': return a.xs.map(canon).join('*');
    case 'div': return '(' + canon(a.a) + ')/(' + canon(a.b) + ')';
    case 'frac': return '(' + canon(a.n) + ')/(' + canon(a.d) + ')';
    case 'neg': return '-(' + canon(a.x) + ')';
    case 'add': return '(' + canon(a.a) + a.op + canon(a.b) + ')';
    case 'ar': return '(' + canon(a.a) + ({ '+': '+', '−': '-', '×': '*' })[a.op] + canon(a.b) + ')';
    default: return '?';
  }
}
function keyOf(a) { try { return canon(a); } catch (e) { return null; } }
/* plain facts comparing a wrong line with the line before it — always true, never a guess about why */
function relFacts(prev, line, letters, part) {
  const out = [];
  if (!letters.length) {
    const pv = val(prev), lv = val(line); if (!pv || !lv) return out;
    if (qeq(lv, qmul(Q(-1), pv))) { out.push('This line has the opposite sign of the line before it.'); return out; }
    if (pv.n !== 0n && qeq(lv, qdiv(Q(1), pv))) { out.push('This line is upside down compared with the line before it: it is the reciprocal.'); return out; }
    const B = part.prm && (part.prm.b || part.prm.B);
    const sp = single(line);
    if (B && sp && qeq(sp.b, Q(B))) { const j = logB(pv, Q(B)); if (j !== null) { out.push('This line is ' + m(P(B, Number(sp.e))) + ', but the line before it equals ' + m(P(B, j)) + '.'); return out; } }
    const small = q => (q.n < 0n ? -q.n : q.n) < 10n ** 12n && q.d < 10n ** 12n;
    if (small(lv) && small(pv)) out.push('This line equals ' + mv(lv, { dec: true }) + ', but the line before it equals ' + mv(pv, { dec: true }) + '.');
    return out;
  }
  const a = mono(prev), b = mono(line); if (!a || !b) return out;
  if (!qeq(a.c, b.c)) out.push('The number part: this line has ' + mv(b.c) + ', the line before it has ' + mv(a.c) + '.');
  Object.keys(Object.assign({}, a.x, b.x)).sort().forEach(l => {
    const ea = a.x[l] || 0n, eb = b.x[l] || 0n;
    if (ea !== eb) out.push('The exponent on <i>' + l + '</i>: this line has ' + String(eb).replace('-', '−') + ', the line before it has ' + String(ea).replace('-', '−') + ' (a letter on the bottom counts as a negative exponent).');
  });
  return out;
}
function prepLine(raw, part) {
  let s = raw.replace(/\.\s*$/, '');
  if (!vars(part.ans).length) s = s.replace(/(\d(?:\.\d+)?)\s*[eE]\s*([+-]?\d+)/g, '$1 x 10^$2');     /* 1.88E6 is the question's own way of writing it */
  else if (vars(part.ans).indexOf('x') < 0) s = s.replace(/\s+[xX]\s+/g, ' * ');                      /* "k^4 x k^7": x as times when x is not a letter here */
  return s;
}
function checkWork(part, text) {
  const out = { lines: [], next: null, done: false, finalMsg: null };
  if (!part.fam) return out;
  const xT = part.kind === 'sci' || part.kind === 'std' || part.kind === 'times' || !vars(part.ans).length;
  const letters = vars(part.ans), eqFam = part.fam === 'solveN';
  const nAns = eqFam ? evalA(part.ans, {}) : null;
  const sol = solution(part) || [];
  const solKeys = sol.map(st => { if (!st.ex) return null;
    try { return eqFam ? keyOf(E.parse(typedOf(st.ex.l), true)) + '=' + keyOf(E.parse(typedOf(st.ex.r), true)) : keyOf(E.parse(typedOf(st.ex), xT)); } catch (e) { return null; } });
  const raws = String(text || '').split(/\n/).map(x => x.trim()).filter(Boolean).slice(0, 12);
  let stop = false, reached = -1, lastGood = null, lastGoodText = '', lastEq = null;
  const nextSay = () => { const nx = sol.findIndex((st, i) => i > reached && st.ex); return nx >= 0 ? sol[nx].say : null; };
  for (const raw0 of raws) {
    if (stop) { out.lines.push({ raw: raw0, ok: null, msg: 'Fix the line above first.' }); continue; }
    const raw = prepLine(raw0, part);
    const row = { raw: raw0, ok: true, msg: '' };
    if (eqFam) {
      const sides = raw.split('=').map(x => x.trim());
      if (sides.length !== 2 || !sides[0] || !sides[1]) { row.ok = null; row.msg = 'Write each line as one equation, like n − 3 = 4.'; }
      else {
        let L, R; try { L = E.parse(sides[0], true); R = E.parse(sides[1], true); } catch (e) { L = null; }
        if (!L) { row.ok = null; row.msg = 'I can’t read that line. Use ^ for powers.'; }
        else if (vars(L).concat(vars(R)).some(l => l !== 'n')) { row.ok = null; row.msg = 'The only letter here is <i>n</i>.'; }
        else if (vars(L).concat(vars(R)).indexOf('n') < 0) { row.ok = null; row.msg = 'Keep <i>n</i> in each line until you find it.'; }
        else {
          const holds = v => { try { return qeq(evalA(L, { n: v }), evalA(R, { n: v })); } catch (e) { return false; } };
          if (!holds(nAns)) { row.ok = false; row.msg = 'This equation is not true for the right value of <i>n</i>, so this step changed the equation. ' + (lastEq ? '' : RULE.solveN()); }
          else {
            const others = [qmul(nAns, Q(-1)), E.qadd(nAns, Q(1)), E.qsub(nAns, Q(1)), E.qadd(nAns, Q(2)), Q(0)].filter(v => !qeq(v, nAns));
            const also = others.find(holds);
            if (also) { row.ok = null; row.msg = 'This is true for the right <i>n</i>, but also for <i>n</i> = ' + mv(also) + ', so it no longer pins <i>n</i> down. Keep each line equivalent to the one before.'; }
            else { lastEq = [L, R]; const k = keyOf(L) + '=' + keyOf(R), j = solKeys.indexOf(k); if (j > reached) reached = j; }
          }
        }
      }
      if (row.ok !== true) stop = true;
      out.lines.push(row); continue;
    }
    const pieces = raw.split('=').map(x => x.trim()).filter(Boolean);
    for (let pi = 0; pi < pieces.length; pi++) {
      const pc = pieces[pi];
      if (pc.length > 60) { row.ok = null; row.msg = 'That line is too long to read.'; break; }
      let a; try { a = E.parse(pc, xT); } catch (e) { row.ok = null; row.msg = e.message === 'ambiguous' ? 'Use parentheses to show what is on the bottom of a fraction.' : 'I can’t read “' + esc(pc) + '”. Use ^ for powers and / for fractions.'; break; }
      if (vars(a).some(l => letters.indexOf(l) < 0)) { row.ok = null; row.msg = letters.length ? 'That uses a letter that is not in the question.' : 'There are no letters in this question.'; break; }
      let same; try { same = sameValue(a, part.q, letters); } catch (e) { row.ok = null; row.msg = /exponent not whole/.test(e.message) ? 'Exponents in this unit are whole numbers.' : 'I can’t work that out — check for 0 to the power 0, or dividing by 0.'; break; }
      if (!same) {
        row.ok = false;
        const before = pi > 0 || lastGood ? 'what comes before it' : 'the question';
        let why = [];
        if (!lastGood && pi === 0) {                       /* the first step from the question: the mistake list applies */
          const fb = feedback(part, pc, { loose: true });
          why = (fb.what || []).filter(w => /^That is what you get if/.test(w)).map(w => w.replace(/^That is what you get if/, 'This line equals what you get if'));
          row.step = fb.step == null ? null : fb.step;
        }
        if (!why.length) why = relFacts(lastGood || part.q, a, letters, part);
        const nx = nextSay();
        row.msg = 'This is not equal to ' + before + '.' + (why.length ? ' ' + why.join(' ') : '') + (nx ? ' <span class="wstep">The step to take here: ' + nx + '</span>' : '');
        break;
      }
      const j = solKeys.indexOf(keyOf(a)); if (j > reached) reached = j;
      lastGood = a; lastGoodText = pc;
    }
    if (row.ok !== true) stop = true;
    out.lines.push(row);
  }
  if (!stop && out.lines.length) {
    if (eqFam) {
      const [L, R] = lastEq || [];
      const num = x => unwrap(x).t === 'n' || (unwrap(x).t === 'neg' && unwrap(unwrap(x).x).t === 'n');
      if (L && ((unwrap(L).t === 'v' && num(R)) || (unwrap(R).t === 'v' && num(L)))) { out.done = true; out.finalMsg = 'Solved: <i>n</i> = ' + mv(evalA(unwrap(L).t === 'v' ? R : L, {})) + '. Type that number in the answer box.'; }
    } else if (lastGood) {
      const r = E.mark(part, lastGoodText);
      if (r.v === 'right') { out.done = true; out.finalMsg = 'Every line is equal to the question, and the last one is finished. Put it in the answer box.'; }
      else out.finalMsg = 'Every line so far is equal to the question. ' + (r.v === 'form' ? formFix(part, ctxOf(part, lastGoodText), r.msg).replace(/^Right (value|so far)\.\s*/, 'Not finished yet. ') : '');
    }
    if (!out.done) { const nx = sol.findIndex((st, i) => i > reached && st.ex); if (nx >= 0) out.next = { i: nx, say: minus(sol[nx].say) }; }
  }
  out.lines.forEach(l => { l.msg = minus(l.msg); });
  if (out.finalMsg) out.finalMsg = minus(out.finalMsg);
  return out;
}

function safeFeedback(p, t) {
  try { return feedback(p, t); }
  catch (e) { return { v: E.mark(p, t).v, what: ['Check each step and try again.'], rule: RULE[p.fam] ? RULE[p.fam]() : '', step: null }; }
}
const api = { checkWork: (p, t) => { try { return checkWork(p, t); } catch (e) { return { lines: [], next: null, done: false, finalMsg: 'I could not check that work.' }; } }, typedOf,
  feedback: (p, t) => tidyOut(safeFeedback(p, t)), solution: p => tidySol(solution(p)), models,
  mcFeedback: (i, k) => tidyOut(mcFeedback(i, k)), selectFeedback: (i, p, t) => tidyOut(selectFeedback(i, p, t)), mcSolution: i => tidySol(mcSolution(i)), RULE, mono, single, sciOf, partsFindings };
if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.Coach = api;
})(this);
