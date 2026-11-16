/* A7 Unit 4 practice: the coach. For every kind of question: the mistakes students make (each with the exact value it gives
   and the words that finish "That is what you get if you …"), the rule, the worked steps (Show me how), the step-by-step Hint,
   and the marking of a typed answer. Registers the clean rule with the engine: no mistake, no printed number and no other
   part's answer may equal an answer, so a wrong method is never marked right. */
(function (root) {
'use strict';
const E = (typeof module !== 'undefined' && module.exports) ? require('./engine.js') : root.Practice;
const KIT = (typeof module !== 'undefined' && module.exports) ? require('../kit/core.js') : root.Kit;
const { Q, qadd, qsub, qmul, qdiv, qneg, qabs, qeq, qlt, qpow, p10, qdec, numStr, sciOf, sciH, sciM, M, fr, qF, sqrtH, cbrtH, pw, par, sup, expOf, digitsOf, sciQ } = E;
const S = numStr;
const SX = (q, n) => { const s = sciOf(q, n); return sciM(s.c, s.k); };          /* a value in scientific notation (html) */
const SH = (q, n) => { const s = sciOf(q, n); return sciH(s.c, s.k); };
const X = (h, v, o) => Object.assign({ h, v }, o || {});                        /* a line of worked math: html and its exact value */
const mod = (v, say, step) => ({ v, say, step: step == null ? null : step });
const neg = k => (k < 0 ? '(' + S(Q(k)) + ')' : String(k));
const kS = k => S(Q(k));
const HINT = KIT.hint;
const choice = (ask, opts, extra) => Object.assign({ type: 'choice', ask, opts }, extra || {});
const num = (ask, ans, hint, extra) => Object.assign({ type: 'num', ask, ans, hint }, extra || {});
const O = (label, ok, why) => ({ label, ok: !!ok, why: why || '' });

/* ------------------------------------------------------------------ the families */
const F = {};
const sumSci = (c1, k1, c2, k2, op) => op === '-' ? qsub(sciQ(c1, k1), sciQ(c2, k2)) : qadd(sciQ(c1, k1), sciQ(c2, k2));
const cq = c => qdec(String(c));

/* adding or subtracting with the same power */
function sameFam(op) {
  return {
    models: p => { const x = p.prm, A = cq(x.c1), B = cq(x.c2), C = op === '+' ? qadd(A, B) : qsub(A, B), k = x.k1;
      return [mod(qmul(C, p10(2 * k)), 'add the exponents too. When you ' + (op === '+' ? 'add' : 'subtract') + ', the power of ten is copied down: it stays 10' + sup(k) + '.', 1),
        mod(qmul(qmul(A, B), p10(k)), 'multiply the coefficients. This is a ' + (op === '+' ? 'sum: add them' : 'difference: subtract them') + '.', 1),
        mod(qmul(op === '+' ? qsub(A, B) : qadd(A, B), p10(k)), (op === '+' ? 'subtract' : 'add') + ' the coefficients instead of ' + (op === '+' ? 'adding' : 'subtracting') + ' them.', 1),
        mod(qmul(C, p10(0)), 'subtract the exponents. The power of ten is copied down, not worked out.', 1)]; },
    rule: () => 'Same power of ten: ' + (op === '+' ? 'add' : 'subtract') + ' the coefficients and copy the power down. The exponents are never added when you add or subtract.',
    sol: p => { const x = p.prm, C = op === '+' ? qadd(cq(x.c1), cq(x.c2)) : qsub(cq(x.c1), cq(x.c2)), k = x.k1, out = [
      { say: 'The powers of ten match (both 10' + sup(k) + '), so ' + (op === '+' ? 'add' : 'subtract') + ' the coefficients and copy the power down.', ex: X('(' + x.c1 + ' ' + (op === '+' ? '+' : '−') + ' ' + x.c2 + ') × 10' + sup(k), p.ans) },
      { say: (op === '+' ? 'Add' : 'Subtract') + '.', ex: X(sciH(E.decPlain(C), k), p.ans) }];
      if (!qlt(C, Q(10))) out.push({ say: S(C) + ' is not less than 10. Move the point one place left and add 1 to the exponent.', ex: X(SH(p.ans), p.ans) });
      return out; },
    walk: p => { const x = p.prm, A = cq(x.c1), B = cq(x.c2), C = op === '+' ? qadd(A, B) : qsub(A, B), k = x.k1, st = [
      choice('Do the powers of ten match?', [O('Yes', true), O('No', false, 'Look again: both numbers are written with 10' + sup(k) + '.')]),
      choice('So you …', [O((op === '+' ? 'add' : 'subtract') + ' the coefficients and keep 10' + sup(k), true),
        O((op === '+' ? 'add' : 'subtract') + ' the coefficients and add the exponents', false, 'A power of ten is a place value, like “thousands”. 3 thousands + 2 thousands is 5 thousands, not 5 millions: the power is copied down.'),
        O('multiply the coefficients', false, 'Multiplying is for a product. This is a ' + (op === '+' ? 'sum' : 'difference') + '.')]),
      num('What is ' + S(A) + ' ' + (op === '+' ? '+' : '−') + ' ' + S(B) + '?', C, op === '+' ? HINT.add(A, B) : HINT.sub(A, B), { then: X(sciH(E.decPlain(C), k), p.ans) })];
      if (!qlt(C, Q(10))) { st.push(choice('Is ' + S(C) + ' at least 1 and less than 10?', [O('No', true), O('Yes, it is finished', false, 'Scientific notation needs a number at least 1 and less than 10. ' + S(C) + ' is 10 or more.')]));
        st.push(num(S(C) + ' × 10' + sup(k) + ' = ' + S(qdiv(C, Q(10))) + ' × 10' + sup('?') + '. What is the new exponent?', Q(k + 1), 'Making the number 10 times smaller means the power of ten must be 10 times bigger: one more than ' + k + '.', { then: X(SH(p.ans), p.ans) })); }
      return st; }
  };
}
F.addSame = sameFam('+'); F.subSame = sameFam('-'); F.addCarry = sameFam('+');
F.addCarry.models = p => { const x = p.prm, C = qadd(cq(x.c1), cq(x.c2)), k = x.k1;
  return F.addSame.models(p).concat([mod(qmul(qdiv(C, Q(10)), p10(k - 1)), 'move the point left but take 1 off the exponent. A smaller coefficient needs a BIGGER power: 10' + sup(k + 1) + '.', 2)]); };

F.addGap = {
  models: p => { const x = p.prm, A = cq(x.c1), B = cq(x.c2), k = x.k1;
    return [mod(qmul(qadd(A, B), p10(k)), 'add the coefficients before the powers match. ' + sciM(x.c2, x.k2) + ' is ' + sciM(S(qdiv(B, Q(10))), k) + ' first.', 0),
      mod(qmul(qadd(A, B), p10(k + x.k2)), 'add the coefficients and the exponents. Match the powers first, then copy the power down.', 0),
      mod(qmul(qadd(A, qmul(B, Q(10))), p10(k)), 'move the point the wrong way. Going up to 10' + sup(k) + ' makes ' + x.c2 + ' smaller: ' + S(qdiv(B, Q(10))) + '.', 0),
      mod(qmul(qadd(A, B), p10(x.k2)), 'add the coefficients and keep the smaller power. ' + sciM(x.c1, k) + ' is ' + sciM(S(qmul(A, Q(10))), x.k2) + ' over that power.', 0)]; },
  rule: () => 'To add, the powers of ten must match first. Rewrite the smaller one: one power of ten less means the coefficient is 10 times smaller (move its point one place left).',
  sol: p => { const x = p.prm, A = cq(x.c1), B = qdiv(cq(x.c2), Q(10)), k = x.k1, C = qadd(A, B);
    return [{ say: 'Match the powers first: ' + sciM(x.c2, x.k2) + ' = ' + sciM(S(B), k) + '.', ex: X(sciH(x.c1, k) + ' + ' + sciH(S(B), k), p.ans) },
      { say: 'Now add the coefficients and copy the power down.', ex: X('(' + x.c1 + ' + ' + S(B) + ') × 10' + sup(k), p.ans) },
      { say: 'Add.', ex: X(sciH(E.decPlain(C), k), p.ans) }]; },
  walk: p => { const x = p.prm, A = cq(x.c1), B = qdiv(cq(x.c2), Q(10)), k = x.k1, C = qadd(A, B);
    return [choice('Do the powers of ten match?', [O('No', true), O('Yes', false, 'One is 10' + sup(k) + ' and the other is 10' + sup(x.k2) + '. You can only add things of the same size.')]),
      choice('Rewrite ' + sciM(x.c2, x.k2) + ' as ___ × 10' + sup(k) + ':', [O(sciM(S(B), k), true), O(sciM(S(qmul(cq(x.c2), Q(10))), k), false, 'That is 100 times too big. Going up one power of ten, the coefficient must get 10 times SMALLER.'),
        O(sciM(x.c2, k), false, 'That changes the number: 10' + sup(k) + ' is ten times 10' + sup(x.k2) + ', so the coefficient must shrink.')], { then: X(sciH(x.c1, k) + ' + ' + sciH(S(B), k), p.ans) }),
      num('What is ' + S(A) + ' + ' + S(B) + '?', C, 'Line up the decimal points: ' + E.decPlain(A) + '0 + ' + E.decPlain(B) + '.', { then: X(sciH(E.decPlain(C), k), p.ans) })]; }
};

/* multiplying and dividing */
function prodFam(kind) {
  const isDiv = kind === 'div';
  const parts = x => ({ A: cq(x.c1), B: cq(x.c2), k1: x.k1, k2: x.k2 });
  return {
    models: p => { const { A, B, k1, k2 } = parts(p.prm), C = isDiv ? qdiv(A, B) : qmul(A, B), K = isDiv ? k1 - k2 : k1 + k2, out = [];
      if (isDiv) { out.push(mod(qmul(C, p10(k1 + k2)), 'add the exponents. In a quotient, subtract them: top minus bottom, ' + neg(k1) + ' − ' + neg(k2) + '.', 0));
        out.push(mod(qmul(C, p10(k2 - k1)), 'subtract the exponents the wrong way. It is top minus bottom: ' + neg(k1) + ' − ' + neg(k2) + '.', 0));
        out.push(mod(qmul(qsub(A, B), p10(K)), 'subtract the coefficients. In a quotient, divide them.', 0));
        try { const R = qdiv(B, A); if (E.places(R) >= 0) out.push(mod(qmul(R, p10(K)), 'divide the bottom by the top. It is ' + S(A) + ' ÷ ' + S(B) + '.', 0)); } catch (e) {} }
      else { out.push(mod(qmul(C, p10(k1 * k2)), 'multiply the exponents. Multiplying powers of ten ADDS the exponents: ' + neg(k1) + ' + ' + neg(k2) + '.', 0));
        out.push(mod(qmul(qadd(A, B), p10(K)), 'add the coefficients. In a product, multiply them.', 0));
        out.push(mod(qmul(C, p10(k1 - k2)), 'subtract the exponents. In a product, add them.', 0)); }
      if (!qlt(C, Q(10))) out.push(mod(qmul(qdiv(C, Q(10)), p10(K - 1)), 'move the point left but take 1 off the exponent. A smaller coefficient needs a BIGGER power: 10' + sup(K + 1) + '.', 2));
      if (qlt(C, Q(1))) out.push(mod(qmul(qmul(C, Q(10)), p10(K + 1)), 'move the point right but add 1 to the exponent. A bigger coefficient needs a SMALLER power: 10' + sup(K - 1) + '.', 2));
      if (k1 < 0 || k2 < 0) { const kd = isDiv ? Math.abs(k1) - Math.abs(k2) : Math.abs(k1) + Math.abs(k2); if (kd !== K) out.push(mod(qmul(C, p10(kd)), 'drop the minus sign on an exponent. Keep the sign: 10' + sup(k1 < 0 ? k1 : k2) + '.', 1)); }
      return out; },
    rule: () => isDiv ? 'Dividing: divide the coefficients and subtract the exponents, top minus bottom. Then make sure the coefficient is at least 1 and less than 10.'
      : 'Multiplying: multiply the coefficients and add the exponents. Then make sure the coefficient is at least 1 and less than 10.',
    sol: p => { const { A, B, k1, k2 } = parts(p.prm), C = isDiv ? qdiv(A, B) : qmul(A, B), K = isDiv ? k1 - k2 : k1 + k2;
      const out = [{ say: isDiv ? 'Divide the coefficients and subtract the exponents, top minus bottom.' : 'Multiply the coefficients and add the exponents.',
        ex: X('(' + S(A) + (isDiv ? ' ÷ ' : ' × ') + S(B) + ') × 10' + sup(neg(k1) + (isDiv ? ' − ' : ' + ') + neg(k2)), p.ans) },
        { say: isDiv ? 'Divide, and work out the exponent.' : 'Multiply, and work out the exponent.', ex: X(sciH(E.decPlain(C), K), p.ans) }];
      if (!qlt(C, Q(10))) out.push({ say: S(C) + ' is not less than 10. Move the point one place left and add 1 to the exponent.', ex: X(SH(p.ans), p.ans) });
      if (qlt(C, Q(1))) out.push({ say: S(C) + ' is less than 1. Move the point one place right and take 1 off the exponent.', ex: X(SH(p.ans), p.ans) });
      return out; },
    walk: p => { const { A, B, k1, k2 } = parts(p.prm), C = isDiv ? qdiv(A, B) : qmul(A, B), K = isDiv ? k1 - k2 : k1 + k2;
      const st = [choice(isDiv ? 'To divide in scientific notation, you …' : 'To multiply in scientific notation, you …', isDiv
        ? [O('divide the coefficients and subtract the exponents', true), O('divide the coefficients and divide the exponents', false, 'Powers of ten with the same base: dividing subtracts the exponents. 10' + sup(5) + ' ÷ 10' + sup(2) + ' = 10' + sup(3) + '.'),
          O('subtract the coefficients and subtract the exponents', false, 'The coefficients are divided, not subtracted.')]
        : [O('multiply the coefficients and add the exponents', true), O('multiply the coefficients and multiply the exponents', false, 'Powers of ten with the same base: multiplying adds the exponents. 10' + sup(2) + ' · 10' + sup(3) + ' = 10' + sup(5) + '.'),
          O('add the coefficients and add the exponents', false, 'The coefficients are multiplied, not added.')]),
        num('What is ' + S(A) + (isDiv ? ' ÷ ' : ' × ') + S(B) + '?', C, isDiv ? HINT.div(A, B) : HINT.mul(A, B)),
        num('What is ' + neg(k1) + (isDiv ? ' − ' : ' + ') + neg(k2) + '?', Q(K), isDiv ? (k2 < 0 ? 'Subtracting a negative goes up: ' + neg(k1) + ' + ' + Math.abs(k2) + '.' : 'Count down ' + k2 + ' from ' + k1 + '.') : (k2 > 0 ? 'Count up ' + k2 + ' from ' + kS(k1) + '.' : 'Count down ' + kS(-k2) + ' from ' + kS(k1) + '.'),
          { then: X(sciH(E.decPlain(C), K), p.ans) })];
      if (!qlt(C, Q(10)) || qlt(C, Q(1))) { const big = !qlt(C, Q(10));
        st.push(choice('Is ' + S(C) + ' at least 1 and less than 10?', [O('No', true), O('Yes, it is finished', false, 'Scientific notation needs a number at least 1 and less than 10. ' + S(C) + (big ? ' is 10 or more.' : ' is less than 1.'))]));
        st.push(num(sciH(E.decPlain(C), K) + ' = ' + S(big ? qdiv(C, Q(10)) : qmul(C, Q(10))) + ' × 10' + sup('?') + '. What is the new exponent?', Q(big ? K + 1 : K - 1),
          big ? 'The coefficient got 10 times smaller, so the power must be 10 times bigger: one more than ' + K + '.' : 'The coefficient got 10 times bigger, so the power must be 10 times smaller: one less than ' + K + '.', { then: X(SH(p.ans), p.ans) })); }
      return st; }
  };
}
F.mulInt = prodFam('mul'); F.mulAdj = prodFam('mul'); F.divDec = prodFam('div'); F.divAdj = prodFam('div');
/* the stand-in word problem: a rate times a time */
F.rate = Object.assign({}, prodFam('mul'));
const rateP = p => Object.assign({}, p, { prm: { c1: p.prm.c1, k1: p.prm.m, c2: p.prm.c2, k2: p.prm.n } });
['models', 'sol', 'walk'].forEach(k => { const f = F.rate[k]; F.rate[k] = p => f(rateP(p)); });
const rateModels = F.rate.models; F.rate.models = p => rateModels(p).map(m => Object.assign({}, m, { step: m.step == null ? null : m.step + 1 }));
F.rate.rule = () => 'How many in all = the amount each second × the number of seconds. Multiply the coefficients and add the exponents, then make sure the coefficient is at least 1 and less than 10.';
const rateSol = F.rate.sol;
F.rate.sol = p => [{ say: 'The total is the amount each second times the number of seconds.', ex: X(sciH(p.prm.c1, p.prm.m) + ' × ' + sciH(p.prm.c2, p.prm.n), p.ans) }].concat(rateSol(p));
const rateWalk = F.rate.walk;
F.rate.walk = p => [choice('How do you find how many in all?', [O('multiply the two numbers', true), O('add the two numbers', false, 'Each second adds the same amount again and again: that is multiplying.'),
  O('divide the first by the second', false, 'Dividing would make the total smaller than one second’s worth. The total grows with every second: multiply.')])].concat(rateWalk(p));

/* ------------------------------------------------------------------ Part 2: real-world problems. 21 Oct 2026 (Croix: "anything
   asking how many significant digits should be removed"): the area, the speed, the sum and the difference, each answered exactly */
/* the area of a plate: length × width, both sides × 10² — the product rule, with the formula in front */
F.rwArea = Object.assign({}, prodFam('mul'));
const areaP = p => Object.assign({}, p, { prm: { c1: p.prm.L, k1: 2, c2: p.prm.W, k2: 2 } });
['models', 'sol', 'walk'].forEach(k => { const f = F.rwArea[k]; F.rwArea[k] = p => f(areaP(p)); });
const areaModels = F.rwArea.models;
F.rwArea.models = p => { const A = qdec(p.prm.L), B = qdec(p.prm.W), C = qmul(A, B);
  return [mod(qmul(qmul(Q(2), qadd(A, B)), p10(2)), 'find the perimeter, the distance around. The area is the space inside: length × width.', 0),
    mod(qmul(C, p10(2)), 'copy the power of ten down, as you do to add. Multiplying ADDS the exponents: 2 + 2.', 1)]
    .concat(areaModels(p).map(m => Object.assign({}, m, { step: m.step == null ? null : m.step + 1 })))
    .filter(m => !qeq(m.v, p.ans)); };     /* 10² × 10²: multiplying the exponents happens to give 10⁴, so it is no mistake here */
F.rwArea.rule = () => 'The area of a rectangle is length × width. Multiply the coefficients and add the exponents, then make sure the coefficient is at least 1 and less than 10.';
const areaSol = F.rwArea.sol;
F.rwArea.sol = p => [{ say: 'The area of a rectangle is length × width.', ex: X(sciH(p.prm.L, 2) + ' × ' + sciH(p.prm.W, 2), p.ans) }].concat(areaSol(p));
const areaWalk = F.rwArea.walk;
F.rwArea.walk = p => [choice('How do you find the area of the plate?', [O('multiply the length by the width', true),
  O('add the length and the width', false, 'Adding the sides goes part of the way around the edge. The area is the space inside: length × width.'),
  O('add all four sides', false, 'That is the perimeter, the distance around. The area is the space inside: length × width.')],
  { then: X(sciH(p.prm.L, 2) + ' × ' + sciH(p.prm.W, 2), p.ans) })].concat(areaWalk(p));

/* the speed of a vehicle: distance ÷ time. The hours carry no power of ten, so only the coefficient is divided */
F.rwSpeed = {
  models: p => { const { D, t } = p.prm, A = qdec(D), C = qdiv(A, Q(t)), out = [
      mod(qmul(qmul(A, Q(t)), p10(2)), 'multiply. Average speed is distance DIVIDED by time: kilometers per hour.', 0),
      mod(qdiv(Q(t), qmul(A, p10(2))), 'divide the time by the distance. Speed is kilometers per hour: distance ÷ time.', 0),
      mod(C, 'drop the power of ten. Only ' + D + ' is divided by ' + t + '; the 10' + sup(2) + ' stays.', 1)];
    if (qlt(C, Q(1))) {
      out.push(mod(qmul(qmul(C, Q(10)), p10(3)), 'move the point right but add 1 to the exponent. A bigger coefficient needs a SMALLER power: 10' + sup(1) + '.', 3));
      out.push(mod(qmul(qmul(C, Q(10)), p10(2)), 'move the point but keep 10' + sup(2) + '. The coefficient got 10 times bigger, so the power must go down one: 10' + sup(1) + '.', 3)); }
    return out.filter(m => !qeq(m.v, p.ans)); },
  rule: () => 'Average speed is distance ÷ time. Divide the coefficient by the hours — the power of ten stays — then make sure the coefficient is at least 1 and less than 10.',
  sol: p => { const { D, t } = p.prm, C = qdiv(qdec(D), Q(t)), out = [
      { say: 'Average speed is distance ÷ time.', ex: X(fr(sciH(D, 2), String(t)), p.ans) },
      { say: 'Divide the coefficient by ' + t + '. The hours have no power of ten, so 10' + sup(2) + ' stays.', ex: X('(' + D + ' ÷ ' + t + ') × 10' + sup(2), p.ans) },
      { say: 'Divide.', ex: X(sciH(E.decPlain(C), 2), p.ans) }];
    if (qlt(C, Q(1))) out.push({ say: S(C) + ' is less than 1. Move the point one place right and take 1 off the exponent.', ex: X(SH(p.ans), p.ans) });
    return out; },
  walk: p => { const { D, t } = p.prm, A = qdec(D), C = qdiv(A, Q(t)), st = [
      choice('How do you find the average speed?', [O('distance ÷ time', true),
        O('distance × time', false, 'Multiplying gives more kilometers than the whole trip. Speed is kilometers PER hour: divide.'),
        O('time ÷ distance', false, 'That gives hours per kilometer. Speed is kilometers per hour: distance ÷ time.')], { then: X(fr(sciH(D, 2), String(t)), p.ans) }),
      num('What is ' + D + ' ÷ ' + t + '?', C, 'Think: ' + t + ' × ? = ' + D + '. Work out ' + S(qmul(A, Q(10))) + ' ÷ ' + t + ' first, then move the point one place left.',
        { then: X(sciH(E.decPlain(C), 2), p.ans) })];
    if (qlt(C, Q(1))) {
      st.push(choice('Is ' + S(C) + ' at least 1 and less than 10?', [O('No', true), O('Yes, it is finished', false, 'Scientific notation needs a number at least 1 and less than 10. ' + S(C) + ' is less than 1.')]));
      st.push(num(sciH(E.decPlain(C), 2) + ' = ' + S(qmul(C, Q(10))) + ' × 10' + sup('?') + '. What is the new exponent?', Q(1),
        'The coefficient got 10 times bigger, so the power must be 10 times smaller: one less than 2.', { then: X(SH(p.ans), p.ans) })); }
    return st; }
};

/* a sum or a difference of two measurements one power of ten apart, the first with the bigger power */
function gapFam(op) {
  const sub = op === '-', sg = sub ? ' − ' : ' + ', w = sub ? 'subtract' : 'add', W = sub ? 'Subtract' : 'Add';
  const comb = (a, b) => sub ? qsub(a, b) : qadd(a, b);
  const parts = x => ({ A: cq(x.c1), B: cq(x.c2), k: x.k1, k2: x.k2, b: qdiv(cq(x.c2), Q(10)) });
  const pad = (q, n) => { const s = E.decPlain(q), d = s.indexOf('.') < 0 ? 0 : s.length - s.indexOf('.') - 1; return d >= n ? s : (d ? s : s + '.') + '0'.repeat(n - d); };
  const lineUp = (a, b) => { const n = Math.max(E.places(a), E.places(b)); return pad(a, n) + sg + pad(b, n); };
  return {
    models: p => { const { A, B, k, k2, b } = parts(p.prm), out = [
        mod(qmul(comb(A, B), p10(k)), w + ' the coefficients before the powers match. ' + sciM(p.prm.c2, k2) + ' is ' + sciM(S(b), k) + ' first.', 0),
        mod(qmul(comb(A, B), p10(k + k2)), w + ' the coefficients and add the exponents. Match the powers first, then copy the power down.', 0),
        mod(qmul(comb(A, qmul(B, Q(10))), p10(k)), 'move the point the wrong way. Going up to 10' + sup(k) + ' makes ' + p.prm.c2 + ' smaller: ' + S(b) + '.', 0),
        mod(qmul(comb(A, B), p10(k2)), w + ' the coefficients and keep the smaller power. ' + sciM(p.prm.c1, k) + ' is ' + sciM(S(qmul(A, Q(10))), k2) + ' over that power.', 0)];
      if (sub) out.push(mod(qmul(qadd(A, b), p10(k)), 'add instead of subtracting.', 2));
      return out.filter(m => !qeq(m.v, p.ans)); },
    rule: () => 'To ' + w + ', the powers of ten must match first. Rewrite the one with the smaller power: one power of ten less means its coefficient is 10 times smaller (move its point one place left). Then ' + w + ' the coefficients and copy the power down.',
    sol: p => { const { A, k, k2, b } = parts(p.prm), C = comb(A, b);
      return [{ say: 'Match the powers first: ' + sciM(p.prm.c2, k2) + ' = ' + sciM(S(b), k) + '.', ex: X(sciH(p.prm.c1, k) + sg + sciH(S(b), k), p.ans) },
        { say: 'Now ' + w + ' the coefficients and copy the power down.', ex: X('(' + p.prm.c1 + sg + S(b) + ') × 10' + sup(k), p.ans) },
        { say: W + '.', ex: X(sciH(E.decPlain(C), k), p.ans) }]; },
    walk: p => { const { A, B, k, k2, b } = parts(p.prm), C = comb(A, b);
      return [choice('Do the powers of ten match?', [O('No', true), O('Yes', false, 'One is 10' + sup(k) + ' and the other is 10' + sup(k2) + '. You can only ' + w + ' things of the same size.')]),
        choice('Rewrite ' + sciM(p.prm.c2, k2) + ' as ___ × 10' + sup(k) + ':', [O(sciM(S(b), k), true),
          O(sciM(S(qmul(B, Q(10))), k), false, 'That is 100 times too big. Going up one power of ten, the coefficient must get 10 times SMALLER.'),
          O(sciM(p.prm.c2, k), false, 'That changes the number: 10' + sup(k) + ' is ten times 10' + sup(k2) + ', so the coefficient must shrink.')],
          { then: X(sciH(p.prm.c1, k) + sg + sciH(S(b), k), p.ans) }),
        num('What is ' + S(A) + sg + S(b) + '?', C, 'Line up the decimal points: ' + lineUp(A, b) + '.', { then: X(sciH(E.decPlain(C), k), p.ans) })]; }
  };
}
F.rwSum = gapFam('+'); F.rwDiff = gapFam('-');
const sumP = p => Object.assign({}, p, { prm: { c1: p.prm.A, k1: 3, c2: p.prm.B, k2: 2 } });
const diffP = p => Object.assign({}, p, { prm: { c1: p.prm.C, k1: -2, c2: p.prm.D, k2: -3 } });
['models', 'sol', 'walk'].forEach(k => { const f = F.rwSum[k], g = F.rwDiff[k]; F.rwSum[k] = p => f(sumP(p)); F.rwDiff[k] = p => g(diffP(p)); });

function KIT_shuffle(a, key) { const T = KIT.slot('a7u4', 1, 'walk|' + key); return T.shuffle(a); }   /* option order fixed per question */

/* the order of operations */
F.ooA = {
  models: p => { const { a, b, c } = p.prm; return [mod(Q((a - b) * c * c), 'subtract first, left to right. The power, then the product, then the subtraction.', 0), mod(Q(a - b * c * 2), 'read ' + c + sup(2) + ' as ' + c + ' × 2. It means ' + c + ' × ' + c + '.', 0), mod(Q(a - (b * c) ** 2), 'square ' + b + ' · ' + c + '. The exponent belongs only to ' + c + '.', 0), mod(Q(a + b * c * c), 'add instead of subtracting at the end.', 2)]; },
  rule: () => 'Order of operations: grouping, then powers, then multiplying and dividing (left to right), then adding and subtracting (left to right). An exponent belongs to its own base.',
  sol: p => { const { a, b, c } = p.prm; return [{ say: 'The power first: ' + c + sup(2) + ' = ' + c * c + '.', ex: X(a + ' − ' + b + ' · ' + c * c, p.ans) }, { say: 'Then the product.', ex: X(a + ' − ' + b * c * c, p.ans) }, { say: 'Then subtract.', ex: X(S(p.ans), p.ans) }]; },
  walk: p => { const { a, b, c } = p.prm; return [choice('What do you do first?', [O(c + sup(2), true), O(a + ' − ' + b, false, 'Subtracting comes last. Powers come first.'), O(b + ' · ' + c, false, 'The exponent belongs only to ' + c + ', and powers come before multiplying.')]),
    num('What is ' + c + sup(2) + '?', Q(c * c), HINT.sq(Q(c)), { then: X(a + ' − ' + b + ' · ' + c * c, p.ans) }), num('What is ' + b + ' · ' + c * c + '?', Q(b * c * c), HINT.mul(Q(b), Q(c * c)), { then: X(a + ' − ' + b * c * c, p.ans) }),
    num('What is ' + a + ' − ' + b * c * c + '?', p.ans, b * c * c > a ? 'You are taking away more than ' + a + ', so the answer is negative: ' + b * c * c + ' − ' + a + ', with a minus sign.' : HINT.sub(Q(a), Q(b * c * c)))]; }
};
F.ooB = {
  models: p => { const { a, b, c } = p.prm, out = [mod(qdiv(Q(a * a + b), Q(3 * c)), 'read ' + c + sup(3) + ' as ' + c + ' × 3. It means ' + c + ' × ' + c + ' × ' + c + '.', 0), mod(qdiv(Q(2 * a + b), Q(c ** 3)), 'read ' + a + sup(2) + ' as ' + a + ' × 2. It means ' + a + ' × ' + a + '.', 0), mod(qadd(Q(a * a), qdiv(Q(b), Q(c ** 3))), 'divide only ' + b + '. The fraction bar groups the whole top: finish ' + a + sup(2) + ' + ' + b + ' first.', 0)]; return out; },
  rule: () => 'A fraction bar is a grouping symbol: finish the whole top and the whole bottom, then divide.',
  sol: p => { const { a, b, c } = p.prm; return [{ say: 'The bar groups the top and the bottom. Powers first.', ex: X(fr(a * a + ' + ' + b, c ** 3), p.ans) }, { say: 'Finish the top.', ex: X(fr(a * a + b, c ** 3), p.ans) }, { say: 'Divide.', ex: X(S(p.ans), p.ans) }]; },
  walk: p => { const { a, b, c } = p.prm; return [num('What is ' + a + sup(2) + ' + ' + b + '?', Q(a * a + b), HINT.sq(Q(a)) + ' Then add ' + b + '.'), num('What is ' + c + sup(3) + '?', Q(c ** 3), c + sup(3) + ' means ' + c + ' × ' + c + ' × ' + c + ' (not ' + c + ' × 3).', { then: X(fr(a * a + b, c ** 3), p.ans) }), num('What is ' + (a * a + b) + ' ÷ ' + c ** 3 + '?', p.ans, HINT.div(Q(a * a + b), Q(c ** 3)))]; }
};
F.ooC = {
  models: p => { const { a, b, c } = p.prm; return [mod(qdiv(Q(a), Q(b * c)), 'multiply first. Multiplying and dividing are one level: go left to right, ' + a + ' ÷ ' + b + ' first.', 0)]; },
  rule: () => 'Multiplying and dividing are one level: work them left to right. Multiplying does not come first.',
  sol: p => { const { a, b, c } = p.prm; return [{ say: 'Dividing and multiplying are one level, so go left to right: ' + a + ' ÷ ' + b + ' first.', ex: X((a / b) + ' · ' + c, p.ans) }, { say: 'Then multiply.', ex: X(S(p.ans), p.ans) }]; },
  walk: p => { const { a, b, c } = p.prm; return [choice('Which comes first?', [O(a + ' ÷ ' + b + ' — left to right', true), O(b + ' · ' + c + ' — multiplying first', false, 'Multiplying and dividing are the same level. Go left to right.')]),
    num('What is ' + a + ' ÷ ' + b + '?', Q(a / b), HINT.div(Q(a), Q(b)), { then: X((a / b) + ' · ' + c, p.ans) }), num('What is ' + (a / b) + ' · ' + c + '?', p.ans, HINT.mul(Q(a / b), Q(c)))]; }
};
F.ooD = {
  models: p => { const { a, b } = p.prm; return [mod(Q(a * a + b * b), 'square −' + a + '. In −' + a + sup(2) + ' the exponent belongs to ' + a + ' only: it is −(' + a + ' · ' + a + ').', 0), mod(Q(-a * a - b * b), 'keep (−' + b + ')' + sup(2) + ' negative. The parentheses make −' + b + ' the base: (−' + b + ')(−' + b + ') is positive.', 0), mod(Q(a * a - b * b), 'flip both signs.', 0)]; },
  rule: () => 'An exponent belongs to the base right next to it. −' + 'n' + sup(2) + ' is −(n · n); (−n)' + sup(2) + ' is (−n)(−n). The parentheses decide the base.',
  sol: p => { const { a, b } = p.prm; return [{ say: '−' + a + sup(2) + ' = −(' + a + ' · ' + a + ') = −' + a * a + ', and (−' + b + ')' + sup(2) + ' = (−' + b + ')(−' + b + ') = ' + b * b + '.', ex: X('−' + a * a + ' + ' + b * b, p.ans) }, { say: 'Add.', ex: X(S(p.ans), p.ans) }]; },
  walk: p => { const { a, b } = p.prm; return [choice('What is −' + a + sup(2) + '?', [O('−' + a * a, true), O(String(a * a), false, 'The exponent belongs to ' + a + ' only. Square ' + a + ', then the minus sign: −' + a * a + '.')]),
    choice('What is (−' + b + ')' + sup(2) + '?', [O(String(b * b), true), O('−' + b * b, false, 'The parentheses make −' + b + ' the base: (−' + b + ')(−' + b + '), and negative × negative is positive.')], { then: X('−' + a * a + ' + ' + b * b, p.ans) }),
    num('What is −' + a * a + ' + ' + b * b + '?', p.ans, b * b > a * a ? 'Start at −' + a * a + ' and go up ' + b * b + '.' : 'Start at −' + a * a + ' and go up ' + b * b + ': you stay below zero.')]; }
};
/* radA and radB widened 22 Oct 2026 (ruling 49: "add in that variation factor"): radA also as √(x² − y), the test's other shape
   (b < 0); radB with either sign under the cube root (s) and plus or minus (o). The test's own shapes are s −1, o +1, b > 0. */
const pmc = v => v < 0 ? ' − ' + -v : ' + ' + v, addw = v => v < 0 ? 'subtract' : 'add';
F.radA = {
  models: p => { const { a, b } = p.prm; return [mod(Q(a * a + b), 'forget the square root. The radical is the last step.', 2), mod(Q(a + b), 'take the root of ' + a + sup(2) + ' only. The radical bar groups everything under it: ' + addw(b) + ' first.', 0)].concat(a === 2 ? [] : [mod(Q(a * 2 + b), 'read ' + a + sup(2) + ' as ' + a + ' × 2.', 0)]); },
  rule: () => 'A radical bar is a grouping symbol: finish everything under it, then take the root. The root of a sum or a difference is not the sum or difference of the roots.',
  sol: p => { const { a, b, r } = p.prm; return [{ say: 'The bar groups everything under it. Finish inside first: ' + a + sup(2) + ' = ' + a * a + '.', ex: X(sqrtH(a * a + pmc(b)), p.ans) }, { say: b < 0 ? 'Subtract.' : 'Add.', ex: X(sqrtH(String(a * a + b)), p.ans) }, { say: 'Take the root: ' + r + ' × ' + r + ' = ' + r * r + '.', ex: X(String(r), p.ans) }]; },
  walk: p => { const { a, b, r } = p.prm; return [choice('What do you do first?', [O('finish ' + a + sup(2) + pmc(b) + ' under the bar', true), O('take the root of ' + a + sup(2), false, 'The radical bar groups ' + a + sup(2) + pmc(b) + ' together. Finish inside first.')]),
    num('What is ' + a + sup(2) + pmc(b) + '?', Q(a * a + b), HINT.sq(Q(a)) + ' Then ' + addw(b) + ' ' + Math.abs(b) + '.', { then: X(sqrtH(String(a * a + b)), p.ans) }), num('What number times itself is ' + (a * a + b) + '?', Q(r), 'Try ' + (r - 1) + ' × ' + (r - 1) + ' = ' + (r - 1) ** 2 + ' and go up.')]; }
};
F.radB = {
  models: p => { const { n, k, s = -1, o = 1 } = p.prm, t = Q(o, k * k), root = Q(s * n); return [].concat(
      s < 0 ? [mod(qadd(Q(n), t), 'drop the minus sign. A cube root keeps the sign: (−' + n + ')(−' + n + ')(−' + n + ') = −' + n ** 3 + '.', 0)] : [],
      [mod(qadd(root, Q(-o * k * k)), 'read ' + k + sup(-2) + ' as −' + k + sup(2) + '. A negative exponent means one over: ' + fr(1, k + sup(2)) + '.', 0),
       mod(qsub(root, t), 'make ' + k + sup(-2) + ' negative. A negative exponent is a fraction, not a negative number: ' + fr(1, k * k) + '.', 0)],
      k === 2 ? [] : [mod(qadd(root, Q(-2 * k * o)), 'read ' + k + sup(-2) + ' as ' + k + ' × (−2).', 0)]); },
  rule: () => 'A cube root keeps the sign of what is under it. A negative exponent means one over the power: ' + 'k' + sup(-2) + ' = ' + fr(1, 'k' + sup(2)) + '.',
  sol: p => { const { n, k, s = -1, o = 1 } = p.prm, rt = (s < 0 ? '−' : '') + n, op = o > 0 ? ' + ' : ' − ';
    return [{ say: (s < 0 ? '(−' + n + ')(−' + n + ')(−' + n + ') = −' + n ** 3 + ', so the cube root is −' + n + '.' : n + ' × ' + n + ' × ' + n + ' = ' + n ** 3 + ', so the cube root is ' + n + '.') + ' And ' + k + sup(-2) + ' = ' + fr(1, k + sup(2)) + ' = ' + fr(1, k * k) + '.', ex: X(rt + op + fr(1, k * k), p.ans) },
      { say: (o > 0 ? 'Add' : 'Subtract') + ': ' + rt + ' = ' + fr((s < 0 ? '−' : '') + n * k * k, k * k) + ', and ' + (o > 0 ? 'one more ' : 'one less ') + fr(1, k * k) + ' makes ' + qF(p.ans) + '.', ex: X(qF(p.ans), p.ans) }]; },
  walk: p => { const { n, k, s = -1, o = 1 } = p.prm, rt = (s < 0 ? '−' : '') + n, op = o > 0 ? ' + ' : ' − ';
    return [num('What is ' + cbrtH((s < 0 ? '−' : '') + n ** 3) + '?', Q(s * n), s < 0 ? 'What number used three times makes −' + n ** 3 + '? It must be negative.' : 'What number used three times makes ' + n ** 3 + '?'),
      choice('What is ' + k + sup(-2) + '?', [O(fr(1, k * k), true), O('−' + k * k, false, 'A negative exponent does not make a number negative: it means one over. ' + k + sup(-2) + ' = ' + fr(1, k + sup(2)) + '.')].concat(k === 2 ? [] : [O('−' + 2 * k, false, 'An exponent is not a factor. ' + k + sup(-2) + ' = ' + fr(1, k + ' × ' + k) + '.')]), { then: X(rt + op + fr(1, k * k), p.ans) }),
      num('What is ' + rt + op + fr(1, k * k) + '? (A fraction is fine.)', p.ans, rt + ' = ' + fr((s < 0 ? '−' : '') + n * k * k, k * k) + '. ' + (o > 0 ? 'Add ' : 'Take away ') + fr(1, k * k) + ' on the top.')]; }
};
F.radC = {
  models: p => { const { p: P, q, r } = p.prm, A = Q(1, P * P), B = Q(q, r); return [mod(qadd(qneg(A), B), 'keep (−' + fr(1, P) + ')' + sup(2) + ' negative. The parentheses make −' + fr(1, P) + ' the base: negative × negative is positive.', 0), mod(qadd(A, Q(q * q, r * r)), 'forget the square root of ' + fr(q * q, r * r) + '. Take the root of the top and the bottom: ' + fr(q, r) + '.', 0), mod(qadd(Q(-2, P), B), 'read the square as × 2. (−' + fr(1, P) + ')' + sup(2) + ' = (−' + fr(1, P) + ')(−' + fr(1, P) + ').', 0)]; },
  rule: () => 'Square a fraction by squaring the top and the bottom; a negative squared is positive. A square root of a fraction is the root of the top over the root of the bottom.',
  sol: p => { const { p: P, q, r } = p.prm; return [{ say: '(−' + fr(1, P) + ')' + sup(2) + ' = ' + fr(1, P * P) + ' (a negative squared is positive), and ' + sqrtH(fr(q * q, r * r)) + ' = ' + fr(q, r) + '.', ex: X(fr(1, P * P) + ' + ' + fr(q, r), p.ans) },
    { say: 'Add with a common denominator.', ex: X(qF(p.ans), p.ans) }]; },
  walk: p => { const { p: P, q, r } = p.prm; return [num('What is (−' + fr(1, P) + ')' + sup(2) + '? (A fraction is fine.)', Q(1, P * P), 'Square the top and the bottom: ' + fr('1 × 1', P + ' × ' + P) + '. Negative × negative is positive.'),
    num('What is ' + sqrtH(fr(q * q, r * r)) + '?', Q(q, r), 'Take the root of the top and of the bottom: ' + sqrtH(q * q) + ' and ' + sqrtH(r * r) + '.', { then: X(fr(1, P * P) + ' + ' + fr(q, r), p.ans) }),
    num('What is ' + fr(1, P * P) + ' + ' + fr(q, r) + '? (A fraction is fine.)', p.ans, 'Use a common denominator, like ' + (P * P * r) + ': ' + fr(r, P * P * r) + ' + ' + fr(q * P * P, P * P * r) + '.')]; }
};
F.negSub = {
  models: p => { const { a, n } = p.prm; return [mod(Q(-a * n * n), 'square only ' + n + ' and keep the minus sign. Put −' + n + ' in parentheses: (−' + n + ')' + sup(2) + ' = ' + n * n + ', positive.', 0), mod(Q(a * a * n * n), 'square ' + a + ' too. The exponent belongs to ' + p.prm.L + ' only.', 0), mod(Q(-2 * a * n), 'read the square as × 2.', 0)]; },
  rule: () => 'Substitute a negative value in parentheses, then follow the order of operations: the power first, then the product.',
  sol: p => { const { a, n, L } = p.prm; return [{ say: 'Substitute in parentheses.', ex: X(a + '(−' + n + ')' + sup(2), p.ans) }, { say: 'The power first: (−' + n + ')' + sup(2) + ' = ' + n * n + '.', ex: X(a + ' · ' + n * n, p.ans) }, { say: 'Multiply.', ex: X(S(p.ans), p.ans) }]; },
  walk: p => { const { a, n, L } = p.prm; return [choice('Substitute ' + L + ' = −' + n + ':', [O(a + '(−' + n + ')' + sup(2), true), O(a + ' · −' + n + sup(2), false, 'Without parentheses the square would land on ' + n + ' only. Put −' + n + ' in parentheses.')]),
    num('What is (−' + n + ')' + sup(2) + '?', Q(n * n), '(−' + n + ')(−' + n + '): negative × negative is positive. ' + HINT.mul(Q(n), Q(n)), { then: X(a + ' · ' + n * n, p.ans) }), num('What is ' + a + ' · ' + n * n + '?', p.ans, HINT.mul(Q(a), Q(n * n)))]; }
};
/* the patio: an expression, then its value */
function patioModels(p) {
  const { s, r, f } = p.prm, R = qdec(r);
  return [mod(qadd(qmul(Q(s), R), Q(f)), 'use the side where the area is needed. The rate is per SQUARE foot: multiply it by the area, ' + s + sup(2) + '.', 0),
    mod(qmul(Q(s * s), qadd(R, Q(f))), 'put the flat fee inside the group. A flat fee is charged once, not on every square foot: add it at the end.', 0),
    mod(qadd(qadd(Q(s * s), R), Q(f)), 'add the rate to the area. The rate multiplies the area.', 0),
    mod(qmul(qadd(Q(s * s), Q(f)), R), 'charge the rate on the fee too. Only the area is multiplied by the rate.', 0),
    mod(qadd(qmul(Q(2 * s), R), Q(f)), 'read ' + s + sup(2) + ' as ' + s + ' × 2. The area of a square is side × side.', 0),
    mod(qmul(Q(s * s), R), 'leave out the delivery fee. It is added once, at the end: + ' + f + '.', 1)];
}
F.patioExpr = { models: patioModels,
  rule: () => 'Total cost = area × rate + flat fee. The rate multiplies the area; the flat fee is added once.',
  sol: p => { const { s, r, f } = p.prm; return [{ say: 'The patio is a square, so its area is ' + s + sup(2) + ' square feet.' }, { say: 'The rate is charged on every square foot, so it multiplies the area. The delivery fee is added once.', ex: X(pw(s, 2) + '(' + r + ') + ' + f, p.ans, { pre: '' }) }]; },
  walk: p => { const { s, r, f } = p.prm; return [choice('The area of the patio is …', [O(pw(s, 2) + ' square feet', true), O(4 * s + ' square feet', false, s + ' × 4 is the perimeter, the distance around in feet — not the space inside.'), O(2 * s + ' square feet', false, 'A square’s area is side × side, not side × 2.')]),
    choice('The rate, $' + r + ' per square foot, …', [O('multiplies the area', true), O('is added to the area', false, 'Every square foot costs ' + r + ' dollars: that is multiplying.'), O('multiplies the delivery fee too', false, 'The delivery fee is one flat charge.')]),
    choice('So the total cost is …', [O(M(pw(s, 2) + '(' + r + ') + ' + f), true), O(M(pw(s, 2) + '(' + r + ' + ' + f + ')'), false, 'That charges the delivery fee on every square foot.'), O(M(s + '(' + r + ') + ' + f), false, 'The rate goes with the AREA, ' + s + sup(2) + ', not the side.')])]; } };
F.patioCost = { models: patioModels, rule: F.patioExpr.rule,
  sol: p => { const { s, r, f } = p.prm, A = Q(s * s), C = qmul(A, qdec(r)); return [{ say: 'Area first: ' + s + sup(2) + ' = ' + s * s + '.', ex: X(s * s + '(' + r + ') + ' + f, p.ans) }, { say: 'Multiply by the rate.', ex: X(S(C) + ' + ' + f, p.ans) }, { say: 'Add the flat fee once.', ex: X(S(p.ans), p.ans, { tail: ' dollars' }) }]; },
  walk: p => { const { s, r, f } = p.prm, A = Q(s * s), C = qmul(A, qdec(r)); return [num('What is the area, ' + s + sup(2) + '?', A, HINT.sq(Q(s))), num('What is ' + s * s + ' × ' + r + '?', C, HINT.mul(A, qdec(r)), { then: X(S(C) + ' + ' + f, p.ans) }), num('What is ' + S(C) + ' + ' + f + '?', p.ans, 'Line up the decimal points, then add.')]; } };
/* follow-through (ruling 19): part (b) is right if it is the value of the student's own part (a) expression */
F.patioCost.follow = (p, prevVal) => prevVal;

/* ------------------------------------------------------------------ marking a typed answer */
const RULE = p => F[p.fam].rule(p);
const joinSays = hs => hs.map((h, i) => (i ? ' — or if you ' : 'That is what you get if you ') + h.say.replace(/\.$/, '')).join('') + '.';
function hits(p, v) { return (F[p.fam].models(p) || []).filter(m => m.v && qeq(m.v, v) && !qeq(m.v, p.ans)); }
const KEYH = p => E.ansHtml(p);
function generic(p) { return 'Not one of the usual slips. Check each step against the rule below, or tap Hint to go one step at a time.'; }

/* the answer rounded: to fewer digits, half up or cut off (21 Oct 2026: the class learned on 20 Oct to round measured answers;
   the test says "Do not round", and so does Part 2 here) */
function roundings(q) {
  const n0 = digitsOf(sciOf(q).c), out = [];
  for (let n = 1; n < n0; n++) {
    const unit = p10(expOf(q) - n + 1), x = qdiv(qabs(q), unit), s = q.n < 0n ? -1n : 1n;
    let r = x.n / x.d; const t = r; if ((x.n % x.d) * 2n >= x.d) r += 1n;
    out.push(qmul(Q(s * r), unit), qmul(Q(s * t), unit));
  }
  return out;
}
function sciFeedback(p, r) {
  const W = p.want, v = r.val, rule = RULE(p), key = M(sciH(W.c, W.k));
  if (qeq(v, W.v)) {
    if (r.form === 'sci') return { v: 'right', what: [] };
    if (r.form === 'enote') return { v: 'form', what: ['That is calculator notation. Write it with × 10 and a power: ' + key + '.'], rule: '' };
    if (r.form === 'notfin') {                                               /* a nudge, not the answer: moving the point is half the question (review 3) */
      const c = qabs(qdec(r.c)), big = !qlt(c, Q(10));
      return { v: 'form', what: ['Right value, but ' + E.minus(r.c) + (big ? ' is 10 or more' : ' is less than 1') + ', so it isn’t finished. Move the point one place ' + (big ? 'left' : 'right') + ' — then what happens to the exponent?'], rule: '' };
    }
    if (r.form === 'num') return { v: 'form', what: ['That is the value written out. The question wants scientific notation: ' + key + '.'], rule: '' };
    return { v: 'form', what: ['That works out to the right value — finish it in scientific notation.'], rule: '' };
  }
  const h = hits(p, v);
  if (h.length) return { v: 'wrong', what: [joinSays(h)], rule, step: h[0].step };
  if (qeq(qneg(v), W.v)) return { v: 'wrong', what: ['Check the sign: this answer is ' + (W.v.n > 0n ? 'positive' : 'negative') + '.'], rule };
  if (roundings(W.v).some(x => qeq(x, v)))
    return { v: 'wrong', what: ['That is the answer rounded. Do not round: write every digit of the exact value.'], rule, step: F[p.fam].sol(p).length - 1 };
  if (r.form === 'sci' || r.form === 'notfin') {
    const cOk = qeq(qdec(r.c), qdec(W.c)), kOk = r.k === W.k;
    if (cOk && !kOk) return { v: 'wrong', what: ['The coefficient, ' + E.minus(r.c) + ', is right. Check the power of ten: it should be 10' + sup(W.k) + '.'], rule, step: 1 };
    if (kOk && !cOk && r.form === 'sci') return { v: 'wrong', what: ['The power of ten is right. Check the coefficient: work out the ' + ({ '×': 'product', '÷': 'quotient', '+': 'sum', '-': 'difference', '−': 'difference' }[p.op] || 'numbers') + ' again.'], rule, step: 1 };
  }
  if (qeq(v, qmul(W.v, Q(10))) || qeq(v, qdiv(W.v, Q(10)))) return { v: 'wrong', what: ['The digits are right but the power of ten is off by one.'], rule, step: 2 };
  return { v: 'wrong', what: [generic(p)], rule };
}
function numFeedback(p, r, ctx) {
  const v = r.val, rule = RULE(p);
  if (qeq(v, p.ans)) {
    if (r.form === 'num' || r.form === 'enote' || r.form === 'sci') return { v: 'right', what: [] };
    return { v: 'form', what: ['That works out to the right number, but finish the arithmetic: write it as one number, ' + KEYH(p) + '.'], rule: '' };
  }
  if (p.kind === 'num' && E.places(p.ans) < 0 && r.form === 'num' && Math.abs(E.qnum(qsub(v, p.ans))) < 0.01) return { v: 'form', what: ['Close — that is rounded. Give the exact answer as a fraction.'], rule: '' };
  if (F[p.fam].follow && ctx && ctx.prev != null) {
    const pr = E.readAns(ctx.prev);
    if (pr.ok && ctx.prevPart && !qeq(pr.val, ctx.prevPart.ans) && pr.form === 'expr' && qeq(F[p.fam].follow(p, pr.val), v))
      return { v: 'wrong', what: ['Your method for this part is right: it is the value of your part (a) expression, ' + S(pr.val) + '. But part (a) isn’t right yet, so this comes out wrong too. Fix part (a) first.'], rule: '', step: null };
  }
  const h = hits(p, v);
  if (h.length) return { v: 'wrong', what: [joinSays(h)], rule, step: h[0].step };
  if (qeq(qneg(v), p.ans)) return { v: 'wrong', what: ['Check the sign: the answer is ' + (p.ans.n > 0n ? 'positive' : 'negative') + '.'], rule };
  if (p.kind === 'money' && qeq(v, qmul(p.ans, Q(100)))) return { v: 'wrong', what: ['Check the decimal point: that is the answer in cents.'], rule };
  return { v: 'wrong', what: [generic(p)], rule };
}
function exprFeedback(p, r) {
  const v = r.val, rule = RULE(p), f = p.prm.f;
  if (qeq(v, p.ans)) {
    if (r.form === 'expr') {
      const nums = (r.text.match(/\d+(?:\.\d+)?/g) || []).map(x => qdec(x)), has = q => nums.some(x => qeq(x, q));
      if (has(Q(f)) && has(qdec(p.prm.r)) && (has(Q(p.prm.s)) || has(Q(p.prm.s * p.prm.s)))) return { v: 'right', what: [] };
      return { v: 'form', what: ['That is the right total, but show where it comes from: the area times the rate, plus the ' + f + '-dollar fee.'], rule: '' };
    }
    return { v: 'form', what: ['That is the total cost — that is part (b). Part (a) wants the expression that gives it: the area times the rate, plus the fee.'], rule: '' };
  }
  const h = hits(p, v);
  if (h.length) return { v: 'wrong', what: [joinSays(h)], rule, step: h[0].step };
  return { v: 'wrong', what: ['That expression is worth ' + S(v) + ' dollars, not the total cost. ' + generic(p)], rule };
}
function feedback(p, typed, ctx) {
  const r = E.readAns(typed);
  if (r.blank) return { v: 'blank', what: [] };
  if (!r.ok) { const ex = { num: 'like 42 or −13/6', money: 'like 125.50', expr: 'like 12^2(2.50) + 30' }[p.kind];
    return { v: 'unread', what: [ex ? r.msg.replace(/like 7\.2 x 10\^6/, ex) : r.msg] }; }
  if (p.kind === 'sci') return sciFeedback(p, r);
  if (p.kind === 'expr') return exprFeedback(p, r);
  return numFeedback(p, r, ctx);
}

/* ------------------------------------------------------------------ multiple choice and select-all */
const MCW = {
  mcGap: { oneFew: 'That moves the point one place too few. Two powers of ten apart means the coefficient gets 100 times smaller: two places.', noMatch: 'That adds the coefficients before the powers of ten match.', wrongWay: 'That rewrites the bigger number the wrong way: over a SMALLER power, its coefficient must get bigger, not smaller.' },
  kendra: { exp: 'There is a second mistake: the coefficients were added before the powers matched.', wrongWay: 'The mistakes are named right, but the sum is not: the bigger number was rewritten the wrong way. Over a smaller power its coefficient gets BIGGER.', few: 'The mistakes are named right, but the sum is not: two powers of ten apart, the smaller coefficient moves TWO places.' },
  mcOrder: { times2: 'That reads the square as × 2.', addFirst: 'That adds first. Multiply before adding.', squareAll: 'That squares everything. The exponent belongs only to its own base.' },
  nadia: { right: 'The radical bar groups the sum: the root of a sum is not the sum of the roots.', noRoot: 'That forgets the square root.', mult: 'Roots of a sum do not multiply either. Finish under the bar, then take one root.' }
};
const MCRULE = {
  mcGap: () => F.addGap.rule(), kendra: () => F.addGap.rule(), mcOrder: () => F.ooA.rule(), nadia: () => F.radA.rule(),
  selSci: () => 'Work out each expression in scientific notation and compare it with the target, exponent and all.', selVal: () => F.ooA.rule()
};
function mcFeedback(x, k) {
  if (k === x.correct) return { v: 'right', what: [] };
  const tag = x.tags ? x.tags[k] : null, w = (MCW[x.fam] || {})[tag] || 'Not that one. Work it through with the rule below.';
  return { v: 'wrong', what: [w], rule: MCRULE[x.fam] ? MCRULE[x.fam]() : '' };
}
const LET = 'ABCDEFGH';
const SELWHY = {
  selSci: (x, i) => { const v = x.vals[i]; return LET[i] + ' is ' + SX(v) + (qeq(v, x.target) ? '.' : ', not ' + SX(x.target) + '.'); },
  selVal: (x, i) => { const t = x.tags[i], v = x.vals[i];
    const why = { negRoot: 'the minus sign sits outside the radical, so it is applied after the root', leftRight: 'one level, left to right: divide first, then multiply', divFirst: 'divide before adding: only the ' + x.prm.y2 + ' is divided' }[t];
    return LET[i] + ' is ' + qF(v) + (qeq(v, x.target) ? '.' : (why ? ' — ' + why + '.' : '.')); }
};
function selectFeedback(x, ks, tries) {
  const picked = (ks || []).map(Number), right = x.correct;
  const wrongPicks = picked.filter(i => right.indexOf(i) < 0), missed = right.filter(i => picked.indexOf(i) < 0);
  if (!wrongPicks.length && !missed.length) return { v: 'right', what: [] };
  const rule = MCRULE[x.fam](), T = x.fam === 'selSci' ? SX(x.target) : S(x.target);
  if ((tries || 1) <= 1) return { v: 'wrong', what: [(wrongPicks.length ? (wrongPicks.length === 1 ? 'One of your picks isn’t ' : wrongPicks.length + ' of your picks aren’t ') + T : 'Every one you picked is ' + T) + (missed.length ? (wrongPicks.length ? ', and you' : ', but you') + ' missed ' + missed.length + ' that ' + (missed.length === 1 ? 'is' : 'are') + '.' : '.') + ' Work each one out and try again.'], rule };
  return { v: 'wrong', what: wrongPicks.concat(missed).sort().map(i => SELWHY[x.fam](x, i)), rule };
}
function mcSolution(x) {
  if (x.type === 'multi') return x.opts.map((o, i) => ({ say: SELWHY[x.fam](x, i) }));
  const ok = x.opts[x.correct];
  if (x.fam === 'mcGap') { const { c1, k1, c2, k2 } = x.prm, B = qdiv(qdec(c1), Q(100)); return [{ say: 'Match the powers: ' + sciM(c1, k1) + ' = ' + sciM(S(B), k2) + ' (two powers apart: two places).' }, { say: 'Add the coefficients and copy the power down: ' + S(qdec(c2)) + ' + ' + S(B) + ' = ' + S(qadd(qdec(c2), B)) + '.' }, { say: 'The answer is ' + ok + '.' }]; }
  if (x.fam === 'kendra') { const { a, k1, b, k2 } = x.prm, B = qdiv(qdec(a), Q(100)); return [{ say: 'Two mistakes: the coefficients were added before the powers matched, and the exponents were added. Adding never adds the exponents.' }, { say: 'Match the powers: ' + sciM(a, k1) + ' = ' + sciM(S(B), k2) + '. Then ' + S(qdec(b)) + ' + ' + S(B) + ' = ' + S(qadd(qdec(b), B)) + '.' }, { say: 'The answer is ' + LET[x.correct] + '.' }]; }
  if (x.fam === 'mcOrder') { const { a, b, c } = x.prm; return [{ say: 'The power first: ' + c + sup(2) + ' = ' + c * c + '.' }, { say: 'Then multiply: ' + b + ' · ' + c * c + ' = ' + b * c * c + '.' }, { say: 'Then add: ' + a + ' + ' + b * c * c + ' = ' + (a + b * c * c) + '.' }]; }
  if (x.fam === 'nadia') { const { a, b, c } = x.prm; return [{ say: 'The radical bar is a grouping symbol: finish ' + a * a + ' + ' + b * b + ' = ' + (a * a + b * b) + ' first.' }, { say: sqrtH(String(a * a + b * b)) + ' = ' + c + ', because ' + c + ' × ' + c + ' = ' + c * c + '.' }, { say: 'The answer is ' + LET[x.correct] + '.' }]; }
  return [{ say: 'The answer is ' + ok + '.' }];
}
function solution(p) { return F[p.fam].sol(p); }
/* every Hint choice in a fixed shuffled order: the right one is not always on top (review 3: it was first 95% of the time) */
const mixed = (st, key) => st && st.map((x, i) => x.type === 'choice' ? Object.assign({}, x, { opts: KIT_shuffle(x.opts, key + '|' + i) }) : x);
function steps(p) { return mixed(F[p.fam].walk(p), p.key); }
function stepsMC(x) { return mixed(stepsMC0(x), x.key); }
function stepsMC0(x) {
  if (x.fam === 'mcOrder') { const { a, b, c } = x.prm; return [num('What is ' + c + sup(2) + '?', Q(c * c), HINT.sq(Q(c))), num('What is ' + b + ' · ' + c * c + '?', Q(b * c * c), HINT.mul(Q(b), Q(c * c))), num('What is ' + a + ' + ' + b * c * c + '?', Q(a + b * c * c), HINT.add(Q(a), Q(b * c * c)))]; }
  if (x.fam === 'mcGap' || x.fam === 'kendra') { const c1 = x.fam === 'mcGap' ? x.prm.c1 : x.prm.a, k1 = x.prm.k1, c2 = x.fam === 'mcGap' ? x.prm.c2 : x.prm.b, k2 = x.prm.k2, B = qdiv(qdec(c1), Q(100));
    return [choice('Do the powers of ten match?', [O('No', true), O('Yes', false, 'One is 10' + sup(k1) + ', the other 10' + sup(k2) + '.')]),
      choice('Rewrite ' + sciM(c1, k1) + ' as ___ × 10' + sup(k2) + ':', [O(sciM(S(B), k2), true), O(sciM(S(qdiv(qdec(c1), Q(10))), k2), false, 'That moves the point only one place, but the powers are two apart: two places.'), O(sciM(c1, k2), false, 'That makes it 100 times bigger.')]),
      num('What is ' + S(qdec(c2)) + ' + ' + S(B) + '?', qadd(qdec(c2), B), 'Line up the decimal points: ' + E.decPlain(qdec(c2)) + '00 + ' + E.decPlain(B) + '.')]; }
  if (x.fam === 'nadia') { const { a, b, c } = x.prm; return [choice('Under the radical bar, what comes first?', [O('add ' + a * a + ' + ' + b * b, true), O('take each root', false, 'The bar groups the whole sum. Finish inside first.')]), num('What is ' + a * a + ' + ' + b * b + '?', Q(a * a + b * b), HINT.add(Q(a * a), Q(b * b))), num('What number times itself is ' + (a * a + b * b) + '?', Q(c), 'Try ' + (c - 1) + ' × ' + (c - 1) + ' = ' + (c - 1) ** 2 + ' and go up.')]; }
  return null;
}

/* ------------------------------------------------------------------ the clean rule */
function printedNumbers(it) {
  const t = [it.stem].concat(E.partsOf(it).map(p => p.stem || '')).join(' ').replace(/<sup[^>]*>(.*?)<\/sup>/g, ' ').replace(/<[^>]+>/g, ' ');
  return (t.match(/\d[\d,]*(?:\.\d+)?/g) || []).map(s => qdec(s.replace(/,/g, '')));
}
function clean(it) {
  const parts = E.partsOf(it);
  if (it.type === 'mc') { if (new Set(it.opts).size !== it.opts.length) return false; if (Array.isArray(it.vals) && it.vals.some((v, i) => i !== it.correct && v.n !== undefined && qeq(v, it.vals[it.correct]))) return false; return true; }
  if (it.type === 'multi') { if (new Set(it.opts).size !== it.opts.length) return false; return it.correct.length === 4 && it.vals.filter(v => !qeq(v, it.target)).length === 2; }
  const ans = parts.map(p => p.ans);
  for (let i = 0; i < ans.length; i++) for (let j = i + 1; j < ans.length; j++) if (qeq(ans[i], ans[j]) && parts[i].fam !== 'patioExpr') return false;
  const printed = printedNumbers(it);
  for (const p of parts) {
    if (p.kind !== 'sci' && p.kind !== 'expr' && printed.some(x => qeq(x, qabs(p.ans)))) return false;
    for (const m of F[p.fam].models(p)) { if (m.v && qeq(m.v, p.ans)) return false; }
  }
  return true;
}
E.setClean(clean);

const api = { F, feedback, mcFeedback, selectFeedback, mcSolution, solution, clean, joinSays };
const walkApi = { steps, stepsMC, readNum: E.readNum };
if (typeof module !== 'undefined' && module.exports) module.exports = Object.assign({}, api, { Walk: walkApi }); else { root.Coach = api; root.Walk = walkApi; }
})(this);
