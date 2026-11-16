/* A7 Unit 3 practice: the guided walkthrough ("Walk me through it").
   A question becomes a few small questions, one at a time:
     choice — tap one; a wrong tap says why and lets the student tap again;
     num    — type one number; it is checked exactly (its value comes from the `of` expression, which walk_check re-evaluates).
   After each step the work so far is shown (`then`): every `then` expression equals the original question.
   Soundness is checked by coach_check.js: one right option per choice, every num answer = its `of`, every `then` = the question,
   the last `then` = the answer, every arithmetic sentence true. */
(function (root) {
'use strict';
const E = (typeof module !== 'undefined' && module.exports) ? require('./engine.js') : root.Practice;
const { Q, qeq, qdec, decStr, commas, N, V, P, Mul, Fr, Neg, Par, Eq, Sci, Ar, M, qmul, qdiv, qpow, evalA, esc } = E;
const qi = x => typeof x === 'object' ? x : typeof x === 'string' ? qdec(x) : Q(BigInt(x));
const ip = (b, e) => qpow(qi(b), BigInt(e));
const Z = n => n < 0 ? Neg(N(-n)) : N(n);
const m = a => M(a);
const sg = x => x < 0 ? '(−' + (-x) + ')' : String(x);
const times = (b, n) => n > 6 ? b + ' multiplied by itself ' + n + ' times' : Array(n).fill(String(b).replace('-', '−')).join(' · ');
const ch = (ask, opts, then, extra) => Object.assign({ type: 'choice', ask, opts: opts.map(o => ({ label: o[0], ok: !!o[1], why: o[2] || '' })), then: then || null }, extra || {});
/* a hint that only names the operation gets one smaller step for the arithmetic too (Apple review R1-3) */
const KIT = (typeof module !== 'undefined' && module.exports) ? require('../kit/core.js') : root.Kit;
function autoArith(of) {
  try {
    if (of.t === 'ar') { const a = evalA(of.a, {}), b = evalA(of.b, {}); if (a.n < 0n || b.n < 0n || a.d !== 1n || b.d !== 1n) return '';
      if (of.op === '+') return KIT.hint.add(a, b); if (of.op === '×') return KIT.hint.mul(a, b); if (of.op === '−' && a.n >= b.n) return KIT.hint.sub(a, b); }
    if (of.t === 'frac' && of.n.t === 'n' && of.d.t === 'n') return KIT.hint.div(of.n.q, of.d.q);
  } catch (e) { /* none */ }
  return '';
}
const ECHO = /^(Add the two exponents|Multiply the exponents|Subtract|Subtract the bottom exponent from the top one|Divide [\d.]+ by [\d.]+|A power of a power multiplies the exponents)\.$/;
const num = (ask, of, hint, then) => { const au = ECHO.test(hint || '') ? autoArith(of) : ''; return { type: 'num', ask, of, ans: evalA(of, {}), hint: (hint || '') + (au ? ' ' + au : ''), then: then || null }; };

function steps(part) {
  const f = part.fam, x = part.prm; if (!f || !x) return null;
  const letter = v => V(v);
  switch (f) {
    case 'prod': case 'monoProd': {
      const b = f === 'prod' ? x.b : letter(x.v), bs = f === 'prod' ? String(x.b) : '<i>' + x.v + '</i>';
      return [ch('Both powers have the base ' + bs + ', and they are multiplied. What happens to the exponents?',
          [['Add them', 1], ['Multiply them', 0, 'Multiplying exponents is for a power of a power, like ' + m(P(Par(P(b, x.m)), x.n)) + '. Here the powers are just multiplied.'], ['Subtract them', 0, 'Subtracting exponents is for dividing powers.']],
          P(b, Ar(x.m, '+', x.n))),
        num('What is ' + x.m + ' + ' + x.n + '?', Ar(x.m, '+', x.n), 'Add the two exponents.', P(b, x.m + x.n))];
    }
    case 'powpow': case 'monoPow': {
      const b = f === 'powpow' ? x.b : letter(x.v);
      return [ch('A power is raised to another power. What happens to the exponents ' + x.m + ' and ' + x.n + '?',
          [['Multiply them', 1], ['Add them', 0, 'Adding is for multiplying two powers, like ' + m(Mul('·', P(b, x.m), P(b, x.n))) + '. Here ' + m(P(b, x.m)) + ' is used ' + x.n + ' times, so ' + x.m + ' is added ' + x.n + ' times: that is multiplying.'],
           ['Raise ' + x.m + ' to the power ' + x.n, 0, 'Each copy of ' + m(P(b, x.m)) + ' adds ' + x.m + ' more factors, and there are ' + x.n + ' copies: ' + x.m + ' × ' + x.n + ', not ' + m(P(x.m, x.n)) + '.']],
          P(b, Ar(x.m, '×', x.n))),
        num('What is ' + x.m + ' × ' + x.n + '?', Ar(x.m, '×', x.n), 'Multiply the exponents.', P(b, x.m * x.n))];
    }
    case 'quot':
      return [ch('Same base, and one power is divided by the other. What happens to the exponents?',
          [['Subtract: top minus bottom', 1], ['Subtract: bottom minus top', 0, 'It is the top exponent minus the bottom one. The top has more factors, so the answer stays on top.'], ['Add them', 0, 'Adding is for multiplying powers. Dividing takes factors away.']].concat(x.m % x.n === 0 && x.m / x.n === x.m - x.n ? [] : [['Divide them', 0, 'Dividing powers subtracts the exponents: each factor on the bottom cancels one on top.']]),
          P(x.b, Ar(x.m, '−', x.n))),
        num('What is ' + x.m + ' − ' + x.n + '?', Ar(x.m, '−', x.n), 'Subtract the bottom exponent from the top one.', P(x.b, x.m - x.n))];
    case 'zero':
      return [ch('What is any number (except 0) raised to the power 0?',
          [['1', 1], ['0', 0, 'A zero exponent does not mean “times 0”. ' + m(Fr(P(x.b, 2), P(x.b, 2))) + ' = ' + m(P(x.b, 0)) + ', and anything divided by itself is 1.'], [String(x.b), 0, 'A zero exponent does not leave the base as it is. ' + m(Fr(P(x.b, 2), P(x.b, 2))) + ' = ' + m(P(x.b, 0)) + ', and anything divided by itself is 1.']],
          N(1))];
    case 'fracpow':
      return [ch('The exponent ' + x.k + ' is outside the parentheses. What does it apply to?',
          [['The top and the bottom', 1], ['Only the top', 0, 'The exponent belongs to the whole fraction, so the bottom gets it too.']].concat(x.p === 1 ? [] : [['Only the bottom', 0, 'The exponent belongs to the whole fraction, so the top gets it too.']]),
          Fr(P(x.p, x.k), P(x.q, x.k))),
        num('What is ' + m(P(x.p, x.k)) + '?', P(x.p, x.k), m(P(x.p, x.k)) + ' means ' + times(x.p, x.k) + '.'),
        num('What is ' + m(P(x.q, x.k)) + '?', P(x.q, x.k), m(P(x.q, x.k)) + ' means ' + times(x.q, x.k) + '.', Fr(N(String(ip(x.p, x.k).n)), N(String(ip(x.q, x.k).n))))];
    case 'zeroMix':
      return [ch('What is ' + m(P(x.a, 0)) + '?',
          [['1', 1], ['0', 0, 'A zero exponent gives 1, not 0.'], [String(x.a), 0, 'A zero exponent gives 1, not the base.']], Mul('·', N(1), P(x.c, 2))),
        num('What is ' + m(P(x.c, 2)) + '?', P(x.c, 2), m(P(x.c, 2)) + ' means ' + x.c + ' · ' + x.c + '.'),
        num('What is 1 · ' + (x.c * x.c) + '?', Mul('·', N(1), N(x.c * x.c)), 'Multiplying by 1 changes nothing.', N(x.c * x.c))];
    case 'powquot': {
      const pq = x.p * x.q;
      return [ch('Start with the top: ' + m(P(Par(P(x.B, x.p)), x.q)) + '. What do you do with ' + x.p + ' and ' + x.q + '?',
          [['Multiply them', 1]].concat(x.p + x.q === x.p * x.q ? [['Subtract them', 0, 'It is a power raised to a power, so multiply the exponents.']] : [['Add them', 0, 'It is a power raised to a power, so multiply the exponents.']]), Fr(P(x.B, Ar(x.p, '×', x.q)), P(x.B, x.r))),
        num('What is ' + x.p + ' × ' + x.q + '?', Ar(x.p, '×', x.q), 'Multiply the exponents.', Fr(P(x.B, pq), P(x.B, x.r))),
        ch('Now ' + m(Fr(P(x.B, pq), P(x.B, x.r))) + '. What happens to the exponents?',
          [['Subtract: top minus bottom', 1], ['Add them', 0, 'Dividing powers subtracts the exponents.']].concat(pq % x.r === 0 && pq / x.r === pq - x.r ? [] : [['Divide them', 0, 'Dividing powers subtracts the exponents.']]), P(x.B, Ar(pq, '−', x.r))),
        num('What is ' + pq + ' − ' + x.r + '?', Ar(pq, '−', x.r), 'Subtract.', P(x.B, x.e)),
        num('What is ' + m(P(x.B, x.e)) + '?', P(x.B, x.e), x.e === 1 ? 'A number to the power 1 is itself.' : m(P(x.B, x.e)) + ' means ' + times(x.B, x.e) + '.', N(String(ip(x.B, x.e).n)))];
    }
    case 'solveN': {
      const n = V('n');
      return [num('Write ' + commas(String(x.V)) + ' as a power of ' + x.b + '. ' + commas(String(x.V)) + ' = ' + x.b + ' to what power?', N(x.c), 'Multiply ' + x.b + ' by itself until you reach ' + commas(String(x.V)) + ', and count the factors.', Eq(Fr(P(x.b, n), P(x.b, x.k)), P(x.b, x.c))),
        ch(m(Fr(P(x.b, n), P(x.b, x.k))) + ' is ' + x.b + ' to what power?',
          [['<i>n</i> − ' + x.k, 1], ['<i>n</i> + ' + x.k, 0, 'Dividing powers subtracts the exponents.'], ['<i>n</i> × ' + x.k, 0, 'Dividing powers subtracts the exponents.']], Eq(Ar(n, '−', x.k), N(x.c))),
        num('So <i>n</i> − ' + x.k + ' = ' + x.c + '. What is <i>n</i>?', Ar(x.c, '+', x.k), 'Add ' + x.k + ' to both sides.', Eq(n, N(x.k + x.c)))];
    }
    case 'negToFrac': case 'varNeg': case 'negVal': {
      const b = f === 'varNeg' ? letter(x.v) : x.b;
      const s = [ch('What does a negative exponent mean?',
          [['One over the power, with the exponent made positive', 1], ['The answer is a negative number', 0, 'A negative exponent never makes a number negative. ' + m(Mul('·', P(b, x.n), P(b, -x.n))) + ' = ' + m(P(b, 0)) + ' = 1, so ' + m(P(b, -x.n)) + ' is one over ' + m(P(b, x.n)) + '.'],
           ['Just drop the minus sign', 0, 'Then you get ' + m(P(b, x.n)) + ', which is the reciprocal of the answer. The power has to go to the bottom.']],
          Fr(1, P(b, x.n)))];
      if (f === 'negVal') s.push(num('What is ' + m(P(x.b, x.n)) + '?', P(x.b, x.n), m(P(x.b, x.n)) + ' means ' + times(x.b, x.n) + '.', Fr(1, N(String(ip(x.b, x.n).n)))));
      return s;
    }
    case 'negDen': {
      const b = Par(Neg(N(x.c)));
      return [ch('The bottom is ' + m(P(b, -x.m)) + '. What is one over a power with a negative exponent?',
          [['The same power with a positive exponent, on top', 1], ['The power with a positive exponent, still on the bottom', 0, m(P(b, -x.m)) + ' already means one over ' + m(P(b, x.m)) + '. One over that is ' + m(P(b, x.m)) + ' itself, so it comes up to the top.'], ['The power moves to the top but its exponent stays negative', 0, 'Moving the power from the bottom to the top is what makes its exponent positive.']],
          P(b, x.m)),
        ch('Does the base keep its parentheses: ' + m(P(b, x.m)) + '?',
          [['Yes — the base is ' + m(b), 1], ['No, write ' + m(Neg(P(x.c, x.m))), 0, m(Neg(P(x.c, x.m))) + ' means −(' + m(P(x.c, x.m)) + '): only ' + x.c + ' is raised to the power. The base here is ' + m(b) + '.']],
          P(b, x.m))];
    }
    case 'coefNeg': case 'coefVarNeg': {
      const b = f === 'coefNeg' ? 10 : letter(x.v), c = f === 'coefNeg' ? x.k : x.c, n = f === 'coefNeg' ? x.m : x.n, bs = f === 'coefNeg' ? 'the 10' : 'the letter <i>' + x.v + '</i>';
      return [ch('Which part has the negative exponent?',
          [['Only ' + bs, 1], ['Both ' + c + ' and ' + bs, 0, 'The exponent sits on ' + bs + ' only. The ' + c + ' is a separate factor.'], ['Only the ' + c, 0, 'The exponent sits on ' + bs + '.']], Mul(f === 'coefNeg' ? '·' : '·', N(c), Fr(1, P(b, n)))),
        ch('So ' + m(P(b, -n)) + ' becomes one over ' + m(P(b, n)) + '. Where does the ' + c + ' go?',
          [['It stays on top', 1], ['It moves to the bottom too', 0, 'Only the factor with the negative exponent moves. The ' + c + ' stays on top.']], Fr(c, P(b, n)))];
    }
    case 'negNegBase': {
      const b = Par(Neg(N(x.c))), v = ip(x.c, x.e).n;
      const odd = x.e % 2 === 1;
      return [ch('What does the negative exponent mean?',
          [['One over the power', 1], ['It makes the answer negative', 0, 'A negative exponent means one over the power; it never makes a number negative by itself.' + (odd ? ' (This answer does turn out negative — but that comes from the negative base, as you will see.)' : '')]], Fr(1, P(b, x.e))),
        num('First, what is ' + m(P(x.c, x.e)) + '?', P(x.c, x.e), m(P(x.c, x.e)) + ' means ' + times(x.c, x.e) + '.'),
        ch('So is ' + m(P(b, x.e)) + ' equal to ' + v + ' or −' + v + '?',
          [['−' + v, x.e % 2 === 1], [String(v), x.e % 2 === 0]].map(o => o[1] ? [o[0], 1] : [o[0], 0, x.e % 2 === 1 ? 'There are ' + x.e + ' negative factors, an odd number. Pairs of negatives make positives, and one negative is left over, so it is negative.' : 'There are ' + x.e + ' negative factors, an even number, so they pair up into positives.']),
          odd ? Neg(Fr(1, N(String(v)))) : Fr(1, N(String(v))))];
    }
    case 'fracNeg':
      return [ch('What does a negative exponent do to a fraction?',
          [['Flips it, and the exponent becomes positive', 1], ['Makes the answer negative', 0, 'A negative exponent never makes a number negative.'], ['Nothing — just drop the minus sign', 0, 'Then the fraction would not flip, and you would get one over the answer.']], P(x.d, x.n)),
        num('What is ' + m(P(x.d, x.n)) + '?', P(x.d, x.n), m(P(x.d, x.n)) + ' means ' + times(x.d, x.n) + '.', N(String(ip(x.d, x.n).n)))];
    case 'mixedProd': {
      const s = x.m - x.n;
      return [ch('Same base, multiplied. What do you do with the exponents ' + x.m + ' and −' + x.n + '?',
          [['Add them', 1], ['Multiply them', 0, 'Multiplying powers with the same base adds the exponents.']], P(x.B, Ar(x.m, '+', -x.n))),
        num('What is ' + x.m + ' + (−' + x.n + ')?', Ar(x.m, '+', -x.n), 'Adding a negative is subtracting: ' + x.m + ' − ' + x.n + '.', P(x.B, s)),
        ch('The exponent is ' + String(s).replace('-', '−') + '. What does that mean?',
          [['One over ' + (-s === 1 ? String(x.B) : m(P(x.B, -s))), 1], ['The answer is negative', 0, 'A negative exponent never makes a number negative.']], -s === 1 ? Fr(1, x.B) : Fr(1, P(x.B, -s)))].concat(-s === 1 ? [] : [
        num('What is ' + m(P(x.B, -s)) + '?', P(x.B, -s), m(P(x.B, -s)) + ' means ' + times(x.B, -s) + '.', Fr(1, N(String(ip(x.B, -s).n))))]);
    }
    case 'monoCoefPow': {
      const v = letter(x.v);
      return [ch('The exponent ' + x.q + ' is outside the parentheses. What gets it?',
          [['Both the ' + x.c + ' and ' + m(P(v, x.p)), 1], ['Only ' + m(P(v, x.p)), 0, 'Everything inside the parentheses gets the exponent, the number too.'], ['Only the ' + x.c, 0, 'Everything inside the parentheses gets the exponent.']], Mul('·', P(x.c, x.q), P(Par(P(v, x.p)), x.q))),
        num('What is ' + m(P(x.c, x.q)) + '?', P(x.c, x.q), m(P(x.c, x.q)) + ' means ' + times(x.c, x.q) + '.'),
        num('For ' + m(P(Par(P(v, x.p)), x.q)) + ', multiply the exponents. What is ' + x.p + ' × ' + x.q + '?', Ar(x.p, '×', x.q), 'A power of a power multiplies the exponents.', Mul('', N(String(ip(x.c, x.q).n)), P(v, x.p * x.q)))];
    }
    case 'monoQuot': {
      const v = letter(x.v);
      return [num('Divide the numbers. What is ' + x.k + ' ÷ ' + x.j + '?', Fr(x.k, x.j), 'Divide ' + x.k + ' by ' + x.j + '.', Mul('·', N(x.t), Fr(P(v, x.p), P(v, x.q)))),
        ch('Now ' + m(Fr(P(v, x.p), P(v, x.q))) + '. What happens to the exponents?',
          [['Subtract: top minus bottom', 1], ['Add them', 0, 'Dividing powers subtracts the exponents.']].concat(x.p % x.q === 0 && x.p / x.q === x.p - x.q ? [] : [['Divide them', 0, 'The numbers in front are divided, but for powers of the same letter you subtract the exponents: each <i>' + x.v + '</i> on the bottom cancels one on top.']]), Mul('', N(x.t), P(v, Ar(x.p, '−', x.q)))),
        num('What is ' + x.p + ' − ' + x.q + '?', Ar(x.p, '−', x.q), 'Subtract the bottom exponent from the top one.', Mul('', N(x.t), P(v, x.p - x.q)))];
    }
    case 'monoNegPow': {
      const v = letter(x.v), w = letter(x.w), kq = ip(x.k, x.q).n;
      return [ch('The exponent ' + x.q + ' is outside the parentheses. What gets it?',
          [['Every factor: ' + x.k + ', ' + m(P(v, -x.p)) + ' and <i>' + x.w + '</i>', 1], ['Only the letters', 0, 'The number inside gets the exponent too.'], ['Only ' + m(P(v, -x.p)), 0, 'Everything inside the parentheses gets the exponent.']],
          Mul('·', P(x.k, x.q), P(Par(P(v, -x.p)), x.q), P(w, x.q))),
        num('What is ' + m(P(x.k, x.q)) + '?', P(x.k, x.q), m(P(x.k, x.q)) + ' means ' + times(x.k, x.q) + '.'),
        num('For <i>' + x.v + '</i>, multiply the exponents. What is (−' + x.p + ') × ' + x.q + '?', Ar(-x.p, '×', x.q), 'A negative times a positive is negative.', Mul('', N(String(kq)), P(v, -x.p * x.q), P(w, x.q))),
        ch(m(P(v, -x.p * x.q)) + ' has a negative exponent. Where does it go?',
          [['To the bottom, with exponent ' + x.p * x.q, 1], ['It stays on top', 0, 'The answer must have only positive exponents, and a negative exponent means one over.'], ['It makes the answer negative', 0, 'A negative exponent never makes a number negative.']],
          Fr(Mul('', N(String(kq)), P(w, x.q)), P(v, x.p * x.q)))];
    }
    case 'toSci': {
      const val = qmul(qdec(x.c), ip(10, x.k)), shown = commas(decStr(val)), big = x.k > 0;
      const c10 = decStr(qmul(qdec(x.c), Q(10))), c01 = decStr(qdiv(qdec(x.c), Q(10)));
      return [ch('Where does the decimal point go? (The first number must be at least 1 and less than 10.)',
          [[x.c, 1], [c10, 0, c10 + ' is not less than 10.'], [c01, 0, c01 + ' is less than 1.']], null),
        Object.assign(num('From ' + shown + ' to ' + x.c + ', how many places does the decimal point move?' + (big ? ' (In a whole number, the point is at the end.)' : ''), N(Math.abs(x.k)), 'Count the jumps from where the point is now to just after the first digit.'), { places: true }),
        ch('Is the exponent positive or negative?',
          [['Positive', big], ['Negative', !big]].map(o => o[1] ? [o[0], 1] : [o[0], 0, big ? shown + ' is big (more than 10), so the exponent is positive.' : shown + ' is less than 1, so the exponent is negative.']), Sci(x.c, x.k))];
    }
    case 'toStd': case 'eNote': {
      const val = qmul(qdec(x.c), ip(10, x.k)), big = x.k > 0, std = N(decStr(val), { commas: true });
      const s = [];
      if (f === 'eNote') s.push(ch('What does <b>E' + x.k + '</b> mean?', [['× ' + m(P(10, x.k)), 1], ['× ' + x.k, 0, 'E is short for “times 10 to the power”.'], ['+ ' + x.k + ' zeros at the end', 0, 'E' + x.k + ' means × ' + m(P(10, x.k)) + ': move the decimal point ' + x.k + ' places, which is not the same as adding ' + x.k + ' zeros after all the digits.']], Sci(x.c, x.k)));
      s.push(ch('Which way does the decimal point move?',
          [['Right — the number gets bigger', big], ['Left — the number gets smaller', !big]].map(o => o[1] ? [o[0], 1] : [o[0], 0, big ? 'A positive exponent makes the number bigger: move right.' : 'A negative exponent makes the number smaller: move left.'])));
      s.push(Object.assign(num('How many places?', N(Math.abs(x.k)), 'The number of places is the size of the exponent, without its sign.', std), { places: true }));
      return s;
    }
    case 'ratio': {
      const t = qdec(x.t);
      return [ch('“How many times larger” means:',
          [['Divide the larger number by the smaller one', 1], ['Subtract them', 0, 'Subtracting tells how much larger, not how many times larger.'], ['Multiply them', 0, '“Times larger” is a division: larger ÷ smaller.']], Fr(Sci(x.A, x.p), Sci(x.B, x.q))),
        num('Divide the numbers. What is ' + x.A + ' ÷ ' + x.B + '?', Fr(N(x.A), N(x.B)), 'Divide ' + x.A + ' by ' + x.B + '.'),
        num('Divide the powers of 10: subtract the exponents. What is ' + sg(x.p) + ' − ' + sg(x.q) + '?', Ar(x.p, '−', x.q), x.q < 0 ? 'Subtracting a negative is adding.' : 'Subtract.', Sci(x.t, x.p - x.q))];
    }
    default: return null;
  }
}
/* multiple choice and select-all */
function stepsMC(item) {
  if (item.fam === 'select') {
    return item.opts.map((o, k) => {
      const v = evalA(o, {}), eq = qeq(v, evalA(item.target, {}));
      return ch('Choice ' + 'ABCDE'[k] + ': is ' + m(o) + ' equal to ' + m(item.target) + '?',
        [['Yes', eq], ['No', !eq]].map(x => x[1] ? [x[0], 1] : [x[0], 0, m(o) + ' = ' + m(v.d === 1n ? (v.n < 0n ? Neg(N(String(-v.n))) : N(String(v.n))) : v.n < 0n ? Neg(Fr(N(String(-v.n)), N(String(v.d)))) : Fr(N(String(v.n)), N(String(v.d)))) + (eq ? ', which is equal.' : ', which is not equal.')]));
    });
  }
  if (!item.fam || !item.prm) return null;
  const s = steps({ fam: item.fam, prm: item.prm });
  if (!s) return null;
  return s;
}
function readNum(text) {
  /* a plain number only — a fraction or a decimal, maybe negative — so typing the question back ("4^2", "9-5") does not count */
  let t = String(text || '').trim().replace(/^n\s*=\s*/i, '').replace(/\s*(places?|times)\s*$/i, '').replace(/[−–]/g, '-').replace(/^\(\s*(.*?)\s*\)$/, '$1');
  if (!/^-?\s*[\d][\d,\s]*(\.\d+)?(\s*\/\s*[\d][\d,\s]*)?$|^-?\s*\.\d+$/.test(t)) return null;
  let a; try { a = E.parse(t, true); } catch (e) { return null; }
  try { if (E.vars(a).length) return null; return evalA(a, {}); } catch (e) { return null; }
}
function finalHtml(part) {
  return part.kind === 'n' ? m(Eq(V('n'), part.ans)) : M(part.shownAns || part.ans) + (part.tail ? esc(part.tail) : '');
}
const minus = s => typeof s === 'string' ? s.replace(/(^|[\s(>=])-(\d)/g, '$1−$2') : s;
function tidy(st) { if (st) st.forEach(x => { x.ask = minus(x.ask); if (x.hint) x.hint = minus(x.hint); if (x.opts) x.opts.forEach(o => { o.label = minus(o.label); o.why = minus(o.why); }); }); return st; }
/* the step whose idea the picture (visual.js) shows: when a student gets that step wrong, the picture comes up with the reason */
const PIC = { prod: 0, monoProd: 0, powpow: 0, monoPow: 0, quot: 0, zero: 0, fracpow: 0, zeroMix: 0, powquot: 2, solveN: 1, negToFrac: 0, varNeg: 0, negVal: 0,
  negDen: 0, coefNeg: 0, coefVarNeg: 0, negNegBase: 2, fracNeg: 0, mixedProd: 2, monoCoefPow: 0, monoQuot: 1, monoNegPow: 0, toSci: 1, toStd: 'places', eNote: 'places', ratio: 2 };
function markPic(st, fam) {
  if (!st || PIC[fam] == null) return st;
  const i = PIC[fam] === 'places' ? st.findIndex(x => x.places) : PIC[fam];
  if (st[i]) st[i].pic = true;
  return st;
}
const api = { steps: p => markPic(tidy(steps(p)), p.fam), stepsMC: i => markPic(tidy(stepsMC(i)), i.fam), readNum, finalHtml };
if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.Walk = api;
})(this);
