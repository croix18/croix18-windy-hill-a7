/* A7 Unit 5 practice: the coach. For every kind of question: the mistakes students make (each with the exact value it gives
   and the words that finish "That is what you get if you …"), the rule, the worked steps (Show me how), the step-by-step
   Hint, and the marking of a typed answer. Registers the clean rule with the engine: no mistake, no printed number and no
   other part's answer may equal an answer, so a wrong method is never marked right.

   The named mistakes are the unit's own (the test's keys and the B1G-M's): the scale factor divided the wrong way (copy ÷
   original, 5.01), adding instead of multiplying, the area scaled by k instead of k² (5.02–03), the area ratio taken for k,
   the scale not read per 1 inch and the plan's area multiplied by the rate once (5.04), the ratio the wrong way round — the
   estimate catches it (5.06), the square unit converted with the ratio once (5.08), a chain stopped early, the exchange
   rate multiplied both ways, a part of a tank not counted, k not found from the yields, a mixture's part taken for its
   whole, and two speeds compared in two units (5.10).

   Marking a typed answer, in order: the key (or the same number unsimplified — "Almost"); the key rounded — "Almost: give
   every digit", since each conversion here comes out exactly; the sheet's other ratio, which earns the point on the test
   too ("Both directions are on the sheet, and both are accepted." — the unit's reference sheet), so it is right here, with a
   note; follow-through from the student's own part (a) (ruling 19: 6(b) and 16(b), as the test gives it); a named mistake;
   and otherwise a plain "not one of the usual slips". */
(function (root) {
'use strict';
const node = typeof module !== 'undefined' && module.exports;
const E = node ? require('./engine.js') : root.Practice;
const KIT = node ? require('../kit/core.js') : root.Kit;
const { Q, qadd, qsub, qmul, qdiv, qneg, qabs, qeq, qlt, qnum, qdec, qv, qfloor, qround, isInt, places, numStr, N, M, fr, sup, K, mixedH, mixedOut, money, fixed, sqU, ratioH } = E;
const S = numStr;
const HINT = KIT.hint;
const LET = 'ABCDEFGH';
const mod = (v, say, step, o) => Object.assign({ v, say, step: step == null ? null : step }, o || {});    /* a mistake worth exactly v */
const choice = (ask, opts, extra) => Object.assign({ type: 'choice', ask, opts }, extra || {});
const num = (ask, ans, hint, extra) => Object.assign({ type: 'num', ask, ans, hint }, extra || {});
const O = (label, ok, why) => ({ label, ok: !!ok, why: why || '' });
const EX = (h, v, o) => Object.assign({ h, v }, o || {});                                   /* a worked line: its math and its exact value (the answer) */
const cap = s => s[0].toUpperCase() + s.slice(1);
/* a rate or a k in a sentence: a decimal, or a fraction drawn when it never ends */
const kIn = q => places(q) >= 0 ? numStr(q) : fr(String(q.n), String(q.d));
const kOut = q => places(q) >= 0 ? numStr(q) : M(kIn(q));
const decFine = q => places(q) >= 0 ? ' A decimal is fine.' : ' A fraction is fine.';
const plural = (n, one, many) => (qeq(qv(n), Q(1)) ? one : many);
/* the units' names, and what kind of amount each is */
const UW = { in: ['inch', 'inches'], cm: ['centimeter', 'centimeters'], lb: ['pound', 'pounds'], kg: ['kilogram', 'kilograms'], gal: ['gallon', 'gallons'], L: ['liter', 'liters'],
  mi: ['mile', 'miles'], km: ['kilometer', 'kilometers'], ft: ['foot', 'feet'], m: ['meter', 'meters'], c: ['cup', 'cups'], oz: ['ounce', 'ounces'], g: ['gram', 'grams'], yd: ['yard', 'yards'] };
const MASS = { lb: 1, kg: 1, oz: 1, g: 1 }, VOL = { gal: 1, L: 1, c: 1 };
const an = w => (/^[aeiou]/.test(w) ? 'an ' : 'a ') + w;
const bigW = (u, more) => MASS[u] ? (more ? 'heavier' : 'lighter') : VOL[u] ? (more ? 'bigger' : 'smaller') : (more ? 'longer' : 'shorter');
/* the estimate (5.06 Notes II: "Estimate: which is the bigger unit?"): f is how many "to" are in 1 "from" */
function estSay(n, from, to, f) {
  const more = qlt(Q(1), f);
  return an(UW[from][0]) + ' is ' + bigW(from, more) + ' than ' + an(UW[to][0]) + ', so ' + N(n) + ' ' + UW[from][1] + ' is ' + (more ? 'more' : 'fewer') + ' than ' + N(n) + ' ' + UW[to][1] + '.';
}

/* ------------------------------------------------------------------ the families */
const F = {};
/* ---- 1 and 2: the scale factor from one pair of sides (5.01) */
function kFam(up) {
  return {
    models: p => { const { a, b } = p.prm;
      return [mod(Q(a, b), 'divided the original by the copy. The scale factor is copy ÷ original, ' + b + ' ÷ ' + a + (up ? ': the copy is bigger, so k is more than 1.' : ': the copy is smaller, so k is less than 1.'), 1),
        mod(Q(Math.abs(b - a)), 'subtracted the sides. A scale copy multiplies every side by one number; it does not add or take away.', 1)]; },
    rule: () => 'k = copy ÷ original. A copy bigger than the original has k more than 1; a smaller copy has k less than 1.',
    sol: p => { const { a, b } = p.prm;
      return [{ say: 'The scale factor is copy ÷ original. The copy’s side is ' + b + ' and the original’s is ' + a + '.' },
        { say: 'Divide:', ex: EX(K + ' = ' + b + ' ÷ ' + a + ' = ' + S(p.ans), p.ans) },
        { say: 'Check: the copy is ' + (up ? 'bigger, and k is more than 1.' : 'smaller, and k is less than 1.') }]; },
    walk: p => { const { a, b } = p.prm;
      return [choice('The copy’s side is ' + b + ' and the original’s is ' + a + '. Before you divide: k is …', [O(up ? 'more than 1 — the copy is bigger' : 'less than 1 — the copy is smaller', true),
          O(up ? 'less than 1' : 'more than 1', false, up ? 'A copy bigger than the original multiplies every side by a number more than 1.' : 'A copy smaller than the original multiplies every side by a number less than 1.')]),
        choice('Which division finds k?', [O('copy ÷ original: ' + b + ' ÷ ' + a, true), O('original ÷ copy: ' + a + ' ÷ ' + b, false, 'That goes from the copy back to the original. k takes the original to the copy: copy ÷ original.')]),
        num('What is ' + b + ' ÷ ' + a + '?', p.ans, HINT.div(Q(b), Q(a)) + ' A decimal is fine.')]; }
  };
}
F.kUp = kFam(true); F.kDown = kFam(false);

/* ---- 4: the copy's perimeter and area (5.02–03) */
F.perim = {
  models: p => { const { w, h } = p.prm, k = qdec(p.prm.k), P0 = Q(2 * (w + h));
    return [mod(P0, 'found the original’s perimeter and stopped. The copy’s perimeter is that × k.', 1),
      mod(qmul(P0, qmul(k, k)), 'multiplied the perimeter by k². A perimeter is lengths added, so it is × k, like a length; k² is for area.', 1),
      mod(qmul(Q(w + h), k), 'added one length and one width. The perimeter goes all the way around: 2 × (' + w + ' + ' + h + ').', 0),
      mod(qmul(Q(w * h), k), 'multiplied the two sides — that begins the area. The perimeter adds all four sides.', 0)]; },
  rule: () => 'Every side is × k, so the perimeter is × k: find the original’s perimeter, then multiply by k.',
  sol: p => { const { w, h, u } = p.prm, k = qdec(p.prm.k), P0 = 2 * (w + h);
    return [{ say: 'The original’s perimeter: ' + M('2 × (' + w + ' + ' + h + ') = ' + P0) + ' ' + u + '.' },
      { say: 'Every side of the copy is × ' + S(k) + ', so its perimeter is too:', ex: EX(P0 + ' × ' + S(k) + ' = ' + S(p.ans), p.ans) }]; },
  walk: p => { const { w, h } = p.prm, k = qdec(p.prm.k), P0 = Q(2 * (w + h));
    return [num('What is the original rectangle’s perimeter, 2 × (' + w + ' + ' + h + ')?', P0, 'Add the length and the width, then double the sum.'),
      choice('The copy’s perimeter is the original’s …', [O('× ' + S(k) + ', the scale factor', true),
        O('× ' + S(qmul(k, k)) + ', the scale factor squared', false, 'k² is for area. A perimeter is lengths added, and each length is × ' + S(k) + '.'),
        O('+ ' + S(k), false, 'A scale copy multiplies; it never adds.')]),
      num('What is ' + S(P0) + ' × ' + S(k) + '?', p.ans, HINT.mul(P0, k))]; }
};
F.area = {
  models: p => { const { w, h } = p.prm, k = qdec(p.prm.k), k2 = qmul(k, k), A0 = Q(w * h);
    const out = [mod(qmul(A0, k), 'multiplied the area by k once. Area is two lengths multiplied, and each is × k: the area is × k², ' + S(k) + ' × ' + S(k) + ' = ' + S(k2) + '.', 1),
      mod(A0, 'found the original’s area and stopped. The copy’s area is that × k².', 1),
      mod(qmul(Q(2 * (w + h)), k), 'found the copy’s perimeter. The area is length × width.', 0)];
    if (!qeq(qmul(Q(2), k), k2)) out.push(mod(qmul(A0, qmul(Q(2), k)), 'multiplied by 2 × ' + S(k) + '. k² means ' + S(k) + ' × ' + S(k) + ', not 2 × ' + S(k) + '.', 1));
    return out; },
  rule: () => 'Area is two lengths multiplied, so the area is × k² (k × k): find the original’s area, then multiply by k².',
  sol: p => { const { w, h, u } = p.prm, k = qdec(p.prm.k), k2 = qmul(k, k), A0 = Q(w * h), wk = qmul(Q(w), k), hk = qmul(Q(h), k);
    return [{ say: 'The original’s area: ' + M(w + ' × ' + h + ' = ' + S(A0)) + ' ' + u + '².' },
      { say: 'Area is × k², and ' + M(K + sup(2) + ' = ' + S(k) + ' × ' + S(k) + ' = ' + S(k2)) + ':', ex: EX(S(A0) + ' × ' + S(k2) + ' = ' + S(p.ans), p.ans) },
      { say: 'Check with the copy’s sides, ' + S(wk) + ' by ' + S(hk) + ':', ex: EX(S(wk) + ' × ' + S(hk) + ' = ' + S(p.ans), p.ans) }]; },
  walk: p => { const { w, h } = p.prm, k = qdec(p.prm.k), k2 = qmul(k, k), A0 = Q(w * h);
    const opts = [O('× ' + S(k2) + ', which is ' + S(k) + ' × ' + S(k), true), O('× ' + S(k), false, 'Area is length × width, and both are × ' + S(k) + ': the area is × ' + S(k) + ' twice.')];
    if (!qeq(qmul(Q(2), k), k2)) opts.push(O('× ' + S(qmul(Q(2), k)) + ', which is 2 × ' + S(k), false, 'k² means ' + S(k) + ' × ' + S(k) + ', not 2 × ' + S(k) + '.'));
    return [num('What is the original rectangle’s area, ' + w + ' × ' + h + '?', A0, HINT.mul(Q(w), Q(h))),
      choice('The copy’s area is the original’s …', opts),
      num('What is ' + S(A0) + ' × ' + S(k2) + '?', p.ans, HINT.mul(A0, k2))]; }
};

/* ---- 5: k from two areas — a square root (5.02–03 Notes III) */
F.kArea = {
  models: p => { const { A, B } = p.prm, k2 = Q(B, A), out = [mod(k2, 'stopped at ' + N(B) + ' ÷ ' + A + ' = ' + S(k2) + '. That is the area ratio, k²: k is its square root.', 1),
      mod(Q(B - A), 'subtracted the areas. The copy’s area is the original’s multiplied by k².', 0)];
    const half = qdiv(k2, Q(2)); if (!qeq(half, p.ans)) out.push(mod(half, 'halved ' + S(k2) + '. k² = ' + S(k2) + ' means k × k: take the square root, not half.', 1));
    return out; },
  rule: () => 'The area ratio is k²: divide the copy’s area by the original’s, then take the square root.',
  sol: p => { const { A, B } = p.prm, k2 = Q(B, A);
    return [{ say: 'Area scales by k², so the area ratio is k²: ' + M(N(B) + ' ÷ ' + A + ' = ' + S(k2)) + '.' },
      { say: 'k is the number whose square is ' + S(k2) + ': ' + M(S(p.ans) + ' × ' + S(p.ans) + ' = ' + S(k2)) + '.', ex: EX(K + ' = ' + S(p.ans), p.ans) }]; },
  walk: p => { const { A, B } = p.prm, k2 = Q(B, A);
    return [choice('The copy’s area is the original’s area × …', [O('k², the scale factor squared', true), O('k, the scale factor', false, 'Area is two lengths multiplied, and each is × k: the area is × k × k.')]),
      num('What is ' + N(B) + ' ÷ ' + A + '? That is k².', k2, HINT.div(Q(B), Q(A))),
      num('k × k = ' + S(k2) + '. What is k?', p.ans, 'Which whole number times itself makes ' + S(k2) + '? Try the whole numbers in turn until one works.')]; }
};

/* ---- 6, 7 and 8: plans (5.04: "A scale with two units is a rate: read it per 1 first.") */
const scaleH = x => x.den > 1 ? fr('1', String(x.den)) + ' in : ' + x.s + ' ft' : '1 in : ' + x.r + ' ft';
const fracIn = x => M(fr('1', String(x.den))) + ' inch';
const perOneSay = x => 'Read the scale per 1 inch: ' + M(scaleH(x)) + ' gives ' + x.s + ' ft for each ' + fracIn(x) + ', and 1 inch is ' + x.den + ' of those, so the scale is ' + M('1 in : ' + x.r + ' ft') + '.';
const perOneStep = x => num('How many feet does 1 inch on the plan stand for? (' + M(scaleH(x)) + ')', Q(x.r), '1 inch is ' + x.den + ' pieces of ' + fracIn(x) + ', and each piece stands for ' + x.s + ' ft.');
const perOneChoice = x => choice('The scale ' + M('1 in : ' + x.r + ' ft') + ' means …', [O('each inch on the plan stands for ' + x.r + ' real feet', true),
  O('each real foot is ' + x.r + ' inches on the plan', false, 'The inches are on the plan and the feet are real: 1 inch of the plan is ' + x.r + ' feet of the room.')]);
F.wall = {
  models: p => { const x = p.prm, pp = qv(x.p), out = [];
    if (x.den > 1 && x.s === 1) out.push(mod(qmul(pp, Q(1, x.den)), 'multiplied by the ' + fracIn(x) + ' (that is dividing by ' + x.den + '). The scale is a rate: ' + M(scaleH(x)) + ' is 1 in : ' + x.r + ' ft, so multiply by ' + x.r + '.', 0));
    else out.push(mod(qdiv(pp, Q(x.r)), 'divided. A plan length becomes a real length by multiplying by the feet in 1 inch, ' + x.r + '.', 1));
    if (x.den > 1 && x.s > 1) { out.push(mod(qmul(pp, Q(1, x.den)), 'multiplied by the ' + fracIn(x) + '. Read the scale per 1 inch first: 1 in : ' + x.r + ' ft.', 0));
      out.push(mod(qmul(pp, Q(x.s)), 'used ' + x.s + ' ft for each inch. The scale gives ' + x.s + ' ft for each ' + fracIn(x) + ', so 1 inch is ' + x.r + ' ft.', 0)); }
    return out; },
  rule: p => 'Read the scale per 1 inch' + (p.prm.den > 1 ? ' (' + M(scaleH(p.prm)) + ' is 1 in : ' + p.prm.r + ' ft)' : '') + '; then plan length × feet per inch = real length.',
  sol: p => { const x = p.prm;
    return (x.den > 1 ? [{ say: perOneSay(x) }] : [{ say: 'The scale says each inch on the plan is ' + x.r + ' real feet.' }])
      .concat([{ say: 'Plan × rate = real:', ex: EX(N(x.p) + ' × ' + x.r + ' = ' + S(p.ans), p.ans) }]); },
  walk: p => { const x = p.prm;
    return [x.den > 1 ? perOneStep(x) : perOneChoice(x),
      choice('From the plan to the real room, you …', [O('multiply by ' + x.r, true), O('divide by ' + x.r, false, 'The real room is bigger than its plan: multiply.')]),
      num('What is ' + N(x.p) + ' × ' + x.r + '?', p.ans, HINT.mul(qv(x.p), Q(x.r)))]; }
};
function areaFam(follow) {
  return {
    models: p => { const x = p.prm, pp = qv(x.p), qq = qv(x.q), r = Q(x.r), off = x.den > 1 ? 1 : 0;
      return [mod(qmul(qmul(pp, qq), r), 'multiplied the plan’s area by the rate once. Each side of the room is × ' + x.r + ', so find the real length and width first.', off),
        mod(qmul(pp, qq), 'found the area on the plan, in square inches. The room’s area is its real length × its real width.', off),
        mod(qmul(Q(2), qadd(qmul(pp, r), qmul(qq, r))), 'found the room’s perimeter. Area is length × width.', off + 1)]; },
    follow: follow ? (p, a) => qmul(a, qmul(qv(p.prm.q), Q(p.prm.r))) : null,
    rule: () => 'Real dimensions first — each plan length × the feet per inch — then length × width.',
    sol: (p, ctx) => { const x = p.prm, A = qmul(qv(x.p), Q(x.r)), B = qmul(qv(x.q), Q(x.r));
      /* part (b) of question 6 builds on part (a): until part (a) is right, its worked lines say "your part (a)" and never
         its number (the educator of 30 Oct 2026: the lines handed over part (a), which then earned its point "on your own") */
      if (follow && ctx && ctx.prevOk === false) return (x.den > 1 ? [{ say: perOneSay(x) }] : []).concat([
        { say: 'The room for real: the wall from part (a), by ' + M(N(x.q) + ' × ' + x.r + ' = ' + S(B)) + ' ft.' },
        { say: 'Its area is length × width — your part (a) × ' + S(B) + ':', ex: EX(S(p.ans) + ' ft²', p.ans) }]);
      return (x.den > 1 ? [{ say: perOneSay(x) }] : []).concat([
        { say: 'The room for real: ' + M(N(x.p) + ' × ' + x.r + ' = ' + S(A)) + ' ft by ' + M(N(x.q) + ' × ' + x.r + ' = ' + S(B)) + ' ft.' },
        { say: 'Its area is length × width:', ex: EX(S(A) + ' × ' + S(B) + ' = ' + S(p.ans), p.ans) }]); },
    walk: (p, ctx) => { const x = p.prm, A = qmul(qv(x.p), Q(x.r)), B = qmul(qv(x.q), Q(x.r));
      /* part (b) of question 6 builds on part (a): its Hint asks for the other wall and uses "your part (a)", so it never
         hands over part (a)'s number. A fresh one ("Try another") has no part (a), so it gets the whole walk. */
      if (follow && !(ctx && ctx.extra)) return (x.den > 1 ? [perOneStep(x)] : []).concat([
        num('Part (a) found the real length of the wall drawn ' + N(x.p) + ' in long. How long is the other wall, drawn ' + N(x.q) + ' in long, for real?', B, HINT.mul(qv(x.q), Q(x.r))),
        choice('So the room’s area is …', [O('the real length from part (a) × ' + S(B), true), O(N(x.p) + ' × ' + N(x.q) + ' × ' + x.r, false, 'That uses the rate once, but each of the two sides is × ' + x.r + '.')]),
        num('What is the room’s real area?', p.ans, 'Multiply the real length from part (a) by ' + S(B) + '.')]);
      return (x.den > 1 ? [perOneStep(x)] : []).concat([
        num('How long is the wall drawn ' + N(x.p) + ' in long, for real?', A, HINT.mul(qv(x.p), Q(x.r))),
        num('And the wall drawn ' + N(x.q) + ' in long?', B, HINT.mul(qv(x.q), Q(x.r))),
        choice('So the room’s area is …', [O(S(A) + ' × ' + S(B), true), O(N(x.p) + ' × ' + N(x.q) + ' × ' + x.r, false, 'That uses the rate once, but each of the two sides is × ' + x.r + '.')]),
        num('What is ' + S(A) + ' × ' + S(B) + '?', p.ans, HINT.mul(A, B))]); }
  };
}
F.roomArea = areaFam(true); F.planArea = areaFam(false);
F.toPlan = {
  models: p => { const x = p.prm, L = Q(x.L), out = [mod(qmul(L, Q(x.r)), 'multiplied. From the real wall to the plan goes the other way: divide by the feet per inch, ' + x.r + '.', 1)];
    if (x.den > 1 && x.s > 1) { out.push(mod(qdiv(L, Q(x.s)), 'divided by ' + x.s + ', as if each inch were ' + x.s + ' ft. The scale gives ' + x.s + ' ft for each ' + fracIn(x) + ': 1 inch is ' + x.r + ' ft.', 0));
      out.push(mod(qmul(L, Q(1, x.den)), 'multiplied by the ' + fracIn(x) + ' and left out the ' + x.s + ' ft. Read the scale per 1 inch first: 1 in : ' + x.r + ' ft.', 0)); }
    return out; },
  rule: p => 'Read the scale per 1 inch' + (p.prm.den > 1 ? ' (' + M(scaleH(p.prm)) + ' is 1 in : ' + p.prm.r + ' ft)' : '') + '; then real length ÷ feet per inch = plan length.',
  sol: p => { const x = p.prm;
    return (x.den > 1 ? [{ say: perOneSay(x) }] : [{ say: 'Each inch on the plan is ' + x.r + ' real feet.' }])
      .concat([{ say: 'Real ÷ rate = plan:', ex: EX(x.L + ' ÷ ' + x.r + ' = ' + S(p.ans), p.ans) }]); },
  walk: p => { const x = p.prm;
    return [x.den > 1 ? perOneStep(x) : perOneChoice(x),
      choice('From the real wall to the plan, you …', [O('divide by ' + x.r, true), O('multiply by ' + x.r, false, 'The plan is smaller than the real wall: divide.')]),
      num('What is ' + x.L + ' ÷ ' + x.r + '?', p.ans, HINT.div(Q(x.L), Q(x.r)) + ' A decimal is fine.')]; }
};

/* ---- 9, 12 and 13: one ratio (5.06 Notes I–II, 5.08 Notes I) */
function convFam() {
  return {
    models: p => { const x = p.prm, f = qdec(x.f), o = qdec(x.o);
      return [mod(qdiv(Q(x.n), f), 'divided by ' + x.f + '. The ratio is for 1 ' + UW[x.from][0] + ', the unit you have, so multiply by it. ' + cap(estSay(x.n, x.from, x.to, f)), 1),
        mod(qmul(Q(x.n), o), 'multiplied by the sheet’s other ratio, ' + x.o + ' — the one for 1 ' + UW[x.to][0] + ', the unit you want. That ratio divides; the one printed here, for 1 ' + UW[x.from][0] + ', multiplies. ' + cap(estSay(x.n, x.from, x.to, f)), 1)]; },
    rule: p => { const x = p.prm; return 'Multiply by the ratio whose 1 is the unit you have. Estimate first: ' + estSay(x.n, x.from, x.to, qdec(x.f)); },
    sol: p => { const x = p.prm, f = qdec(x.f), more = qlt(Q(1), f);
      return [{ say: 'The ratio ' + M(ratioH(x.from, x.f, x.to)) + ' is for 1 ' + UW[x.from][0] + ', the unit you have, so multiply by it:', ex: EX(x.n + ' × ' + x.f + ' = ' + S(p.ans), p.ans) },
        { say: 'Check with the estimate: ' + estSay(x.n, x.from, x.to, f) + ' ' + S(p.ans) + ' is ' + (more ? 'more' : 'fewer') + ' than ' + x.n + '.' }]; },
    walk: p => { const x = p.prm, f = qdec(x.f), more = qlt(Q(1), f), big = more ? x.from : x.to, small = more ? x.to : x.from;
      return [choice('Which is ' + bigW(x.from, true) + ', 1 ' + x.from + ' or 1 ' + x.to + '?', [O('1 ' + big, true), O('1 ' + small, false, '1 ' + x.from + ' = ' + x.f + ' ' + x.to + ': ' + (more ? 'one ' + UW[x.from][0] + ' is more than one ' + UW[x.to][0] + '.' : 'one ' + UW[x.from][0] + ' is less than one ' + UW[x.to][0] + '.'))]),
        choice('So ' + x.n + ' ' + UW[x.from][1] + ' is …', [O((more ? 'more' : 'fewer') + ' than ' + x.n + ' ' + UW[x.to][1], true),
          O((more ? 'fewer' : 'more') + ' than ' + x.n + ' ' + UW[x.to][1], false, more ? 'Each ' + UW[x.from][0] + ' is more than one ' + UW[x.to][0] + ', so it takes more of them.' : 'Each ' + UW[x.from][0] + ' is less than one ' + UW[x.to][0] + ', so it takes fewer of them.')]),
        num('What is ' + x.n + ' × ' + x.f + '?', p.ans, HINT.mul(Q(x.n), f))]; }
  };
}
F.convIn = convFam(); F.convMass = convFam(); F.convVol = convFam();
/* ---- 11: a chain of three ratios (5.06–07; the reference sheet's "Some paths take two steps") */
F.chain = {
  models: p => { const n = qv(p.prm.n), i = qmul(n, Q(36)), r = qdec('2.54');
    return [mod(i, 'stopped at inches, ' + S(i) + ' in. The chain goes on to centimeters: × 2.54.', 2),
      mod(qmul(n, r), 'used only the last ratio. Yards go to feet first (× 3), then to inches (× 12), then to centimeters (× 2.54).', 0),
      mod(qmul(qmul(n, Q(3)), r), 'skipped the inches. Feet to inches is × 12, before the × 2.54.', 1),
      mod(qmul(qmul(n, Q(12)), r), 'skipped the feet. Yards to feet is × 3 first.', 0),
      mod(qdiv(i, r), 'divided by 2.54 at the last step. An inch is longer than a centimeter, so there are more centimeters than inches: × 2.54.', 2),
      mod(qmul(i, qdec('0.39')), 'multiplied the inches by the sheet’s other ratio, 0.39 — the one for 1 cm. That ratio divides; 1 in = 2.54 cm multiplies.', 2)]; },
  rule: () => 'One ratio at a time, each for the unit you have: yards × 3 = feet, feet × 12 = inches, inches × 2.54 = centimeters.',
  sol: p => { const n = qv(p.prm.n), f3 = qmul(n, Q(3)), i = qmul(n, Q(36));
    return [{ say: 'Yards to feet: ' + M(N(n) + ' × 3 = ' + S(f3)) + ' ft.' }, { say: 'Feet to inches: ' + M(S(f3) + ' × 12 = ' + S(i)) + ' in.' },
      { say: 'Inches to centimeters:', ex: EX(S(i) + ' × 2.54 = ' + S(p.ans), p.ans) }]; },
  walk: p => { const n = qv(p.prm.n), f3 = qmul(n, Q(3)), i = qmul(n, Q(36));
    return [num('1 yd = 3 ft. How many feet is ' + N(n) + ' yd?', f3, HINT.mul(n, Q(3))), num('1 ft = 12 in. How many inches is ' + S(f3) + ' ft?', i, HINT.mul(f3, Q(12))),
      num('1 in = 2.54 cm. How many centimeters is ' + S(i) + ' in?', p.ans, HINT.mul(i, qdec('2.54')))]; }
};
/* ---- 15: an exchange rate (5.06–07 Notes III) */
const moneyS = p => q => p.money ? money(q) : S(q);
const cS = c => isInt(qv(c)) ? N(c) : money(qv(c));                                 /* an amount of money in a sentence: 160.80 */
F.toCur = {
  models: p => { const x = p.prm, r = qdec(x.r); return [mod(qdiv(Q(x.d), r), 'divided by the rate. Dollars to ' + x.cur + ': each dollar is ' + N(r) + ' ' + x.cur + ', so multiply.', 0)]; },
  rule: p => 'Dollars × the rate = ' + p.prm.cur + '; ' + p.prm.cur + ' ÷ the rate = dollars.',
  sol: p => { const x = p.prm;
    return [{ say: 'Each US dollar is ' + N(x.r) + ' ' + x.cur + ', so $' + x.d + ' is ' + x.d + ' times as many:', ex: EX(x.d + ' × ' + N(x.r) + ' = ' + moneyS(p)(p.ans), p.ans) }]; },
  walk: p => { const x = p.prm, r = qdec(x.r);
    return [choice('Each US dollar is ' + N(r) + ' ' + x.cur + '. So $' + x.d + ' is …', [O(x.d + ' × ' + N(r) + ' ' + x.cur, true),
        O(x.d + ' ÷ ' + N(r) + ' ' + x.cur, false, 'Each of the ' + x.d + ' dollars is worth ' + N(r) + ' ' + x.cur + ': ' + x.d + ' of them is a multiplication.')]),
      num('What is ' + x.d + ' × ' + N(r) + '?', p.ans, HINT.mul(Q(x.d), r), { money: p.money })]; }
};
F.toUsd = {
  models: p => { const x = p.prm, r = qdec(x.r), c = qdec(x.c); return [mod(qmul(c, r), 'multiplied by the rate again. ' + cap(x.cur) + ' back to dollars goes the other way: divide by the rate.', 0)]; },
  rule: p => 'Dollars × the rate = ' + p.prm.cur + '; ' + p.prm.cur + ' ÷ the rate = dollars.',
  sol: p => { const x = p.prm;
    return [{ say: 'Each US dollar is ' + N(x.r) + ' ' + x.cur + ', so the dollars are how many ' + N(x.r) + 's fit in ' + cS(x.c) + ':', ex: EX(cS(x.c) + ' ÷ ' + N(x.r) + ' = ' + S(p.ans), p.ans) },
      { say: 'Check: ' + M(S(p.ans) + ' × ' + N(x.r) + ' = ' + cS(x.c)) + '.' }]; },
  walk: p => { const x = p.prm, r = qdec(x.r), c = qdec(x.c);
    return [choice('To change ' + x.cur + ' back to US dollars, you …', [O('divide by ' + N(r), true), O('multiply by ' + N(r), false, 'Multiplying by the rate changes dollars INTO ' + x.cur + '. Going back, divide.')]),
      num('What is ' + cS(x.c) + ' ÷ ' + N(r) + '?', p.ans, HINT.div(c, r))]; }
};

/* ---- 16: a unit rate used twice (5.10 Notes I) */
F.range = {
  models: p => { const x = p.prm; return [mod(Q(x.m + x.g), 'added. Each of the ' + x.g + ' gallons takes the ' + x.veh + ' ' + x.m + ' miles: multiply.', 0)]; },
  rule: () => 'Miles per gallon × gallons = miles.',
  sol: p => { const x = p.prm; return [{ say: 'Each gallon goes ' + x.m + ' miles, and a full tank is ' + x.g + ' gallons:', ex: EX(x.m + ' × ' + x.g + ' = ' + S(p.ans), p.ans) }]; },
  walk: p => { const x = p.prm;
    return [choice('Each gallon takes the ' + x.veh + ' ' + x.m + ' miles. A full tank of ' + x.g + ' gallons takes it …', [O(x.m + ' × ' + x.g + ' miles', true),
        O(x.m + ' + ' + x.g + ' miles', false, 'That adds gallons to miles. Each gallon is another ' + x.m + ' miles: multiply.')]),
      num('What is ' + x.m + ' × ' + x.g + '?', p.ans, HINT.mul(Q(x.m), Q(x.g)))]; }
};
F.tanks = {
  models: p => { const x = p.prm, R = Q(x.m * x.g), q = Q(x.D, x.m * x.g), fl = qfloor(q), gal = Q(x.D, x.m);
    return [mod(fl, 'rounded down. ' + S(fl) + ' ' + plural(fl, 'tank goes', 'tanks go') + ' only ' + N(qmul(fl, R)) + ' mi, so the trip needs part of one more — and part of a tank counts as a whole tank.', 2),
      mod(q, 'stopped at ' + N(x.D) + ' ÷ ' + N(R) + (places(q) >= 0 ? ' = ' + S(q) : ' ≈ ' + fixed(q, 2)) + '. Part of a tank counts as a whole tank: round up.', 2, { minDp: 1 }),
      mod(gal, 'found the gallons the trip uses, ' + N(x.D) + ' ÷ ' + x.m + (places(gal) >= 0 ? ' = ' + S(gal) : ' ≈ ' + fixed(gal, 1)) + '. A tank holds ' + x.g + ' of them.', 1)]; },
  follow: (p, a) => (qlt(Q(0), a) ? E.qceil(qdiv(Q(p.prm.D), a)) : null),
  rule: () => 'Miles on one tank first (part a); then the trip ÷ the miles on one tank, rounded UP — part of a tank is still a tank.',
  sol: (p, ctx) => { const x = p.prm, R = Q(x.m * x.g), q = Q(x.D, x.m * x.g);
    /* until part (a) is right, the lines say "your part (a)" and never its number (the educator of 30 Oct 2026) */
    if (ctx && ctx.prevOk === false) return [{ say: 'One full tank goes ' + x.m + ' × ' + x.g + ' miles — your part (a).' },
      { say: 'The trip in tanks is ' + N(x.D) + ' ÷ the miles on one tank. It is not a whole number.' },
      { say: 'Part of a tank counts as a whole tank, so round up:', ex: EX(S(p.ans) + ' tanks', p.ans) }];
    return [{ say: 'One full tank goes ' + M(x.m + ' × ' + x.g + ' = ' + N(R)) + ' mi' + (ctx && ctx.extra ? '' : ' (part a)') + '.' },
      { say: 'The trip in tanks: ' + M(N(x.D) + ' ÷ ' + N(R) + (places(q) >= 0 ? ' = ' + S(q) : ' ≈ ' + fixed(q, 2))) + '.' },
      { say: 'Part of a tank counts as a whole tank, so round up:', ex: EX(S(p.ans) + ' tanks', p.ans) }]; },
  walk: (p, ctx) => { const x = p.prm, fl = qfloor(Q(x.D, x.m * x.g)), f = Number(fl.n), R = Q(x.m * x.g);
    /* a fresh one ("Try another") has no part (a): its Hint finds the miles on one tank first */
    if (ctx && ctx.extra) return [num('How far does one full tank go? (' + x.m + ' miles per gallon, ' + x.g + ' gallons)', R, HINT.mul(Q(x.m), Q(x.g))),
      choice('To find the tanks for the ' + N(x.D) + '-mi trip, divide the trip by …', [O('the miles one full tank goes, ' + N(R), true),
        O('the miles per gallon, ' + x.m, false, 'The trip ÷ ' + x.m + ' is the gallons the trip uses, not the tanks.'),
        O('the gallons in a tank, ' + x.g, false, 'Miles ÷ gallons is not a number of tanks: divide the trip by the miles one tank goes.')]),
      choice(N(x.D) + ' ÷ ' + N(R) + ' is between …', [O(f + ' and ' + (f + 1), true), O((f + 1) + ' and ' + (f + 2), false, (f + 1) + ' full tanks go farther than ' + N(x.D) + ' mi.')].concat(f >= 1 ? [O((f - 1) + ' and ' + f, false, f + ' full ' + plural(fl, 'tank', 'tanks') + ' still fall short of ' + N(x.D) + ' mi.')] : [])),
      num('Part of a tank counts as a whole tank. How many tanks does the trip use?', p.ans, 'Round the division up to the next whole number of tanks.')];
    const span = (a, b) => a + ' and ' + b, opts = [O(span(f, f + 1), true), O(span(f + 1, f + 2), false, f + 1 + ' full tanks of your part (a) go farther than ' + N(x.D) + ' mi: the trip is less than that.')];
    if (f >= 1) opts.push(O(span(f - 1, f), false, f + ' full ' + plural(fl, 'tank', 'tanks') + ' of your part (a) still fall short of ' + N(x.D) + ' mi: the trip is more than that.'));
    /* part (b) builds on part (a): the Hint divides the trip by "your part (a)" and never asks for part (a)'s number */
    return [choice('To find the tanks for the ' + N(x.D) + '-mi trip, divide the trip by …', [O('the miles one full tank goes — your part (a)', true),
        O('the miles per gallon, ' + x.m, false, 'The trip ÷ ' + x.m + ' is the gallons the trip uses, not the tanks.'),
        O('the gallons in a tank, ' + x.g, false, 'Miles ÷ gallons is not a number of tanks: divide the trip by the miles one tank goes.')]),
      choice(N(x.D) + ' ÷ (the miles on one tank) is between …', opts),
      num('Part of a tank counts as a whole tank. How many tanks does the trip use?', p.ans, 'Round the division up to the next whole number of tanks.')]; }
};
/* ---- 17: a recipe scaled by k = new yield ÷ old yield (5.10 Notes III) */
const cupHint = (k, c) => isInt(c) ? HINT.mul(k, c) : 'Write ' + mixedOut(c) + ' as ' + numStr(c) + '. ' + HINT.mul(k, c);
F.scaleUp = {
  models: p => { const x = p.prm, c = qv(x.c), k = Q(x.t, x.s);
    return [mod(qmul(c, Q(x.t)), 'multiplied the cups by ' + x.t + ' servings without dividing by the ' + x.s + '. The recipe is for ' + x.s + ' servings: k = ' + x.t + ' ÷ ' + x.s + '.', 0),
      mod(qmul(c, Q(x.s, x.t)), 'divided the servings the wrong way round. k = new servings ÷ old servings, ' + x.t + ' ÷ ' + x.s + '.', 0),
      mod(k, 'found k = ' + kOut(k) + ' and stopped. k multiplies the ' + mixedOut(c) + ' cups.', 1)]; },
  rule: () => 'k = new servings ÷ old servings, and k multiplies every ingredient.',
  sol: p => { const x = p.prm, c = qv(x.c), k = Q(x.t, x.s);
    return [{ say: 'k = new servings ÷ old servings: ' + M(x.t + ' ÷ ' + x.s + ' = ' + kIn(k)) + '.' },
      { say: 'k multiplies the ' + x.food + ':', ex: EX(kIn(k) + ' × ' + mixedH(c) + ' = ' + mixedH(p.ans), p.ans) }]; },
  walk: p => { const x = p.prm, c = qv(x.c), k = Q(x.t, x.s);
    return [num('The recipe is for ' + x.s + ' servings and you want ' + x.t + '. What is k = ' + x.t + ' ÷ ' + x.s + '?', k, HINT.div(Q(x.t), Q(x.s)) + decFine(k)),
      num('What is ' + kOut(k) + ' × ' + mixedOut(c) + '? That is the cups of ' + x.food + '.', p.ans, cupHint(k, c) + ' A decimal or a mixed number is fine.', { mixed: true })]; }
};
F.servings = {
  models: p => { const x = p.prm, c = qv(x.c), h = qv(x.h), R = qdiv(h, c);
    return [mod(qmul(h, Q(x.s)), 'multiplied the cups on hand by the servings. First find how many recipes ' + mixedOut(h) + ' cups make: ' + mixedOut(h) + ' ÷ ' + mixedOut(c) + '.', 0),
      mod(R, 'found how many recipes, ' + kOut(R) + ', and stopped. Each recipe makes ' + x.s + ' servings.', 1)]; },
  rule: () => 'Cups on hand ÷ cups in one recipe = how many recipes; × the servings in one recipe = servings.',
  sol: p => { const x = p.prm, c = qv(x.c), h = qv(x.h), R = qdiv(h, c);
    return [{ say: 'How many recipes: ' + M(mixedH(h) + ' ÷ ' + mixedH(c) + ' = ' + kIn(R)) + '.' },
      { say: 'Each makes ' + x.s + ' servings:', ex: EX(kIn(R) + ' × ' + x.s + ' = ' + S(p.ans), p.ans) }]; },
  walk: p => { const x = p.prm, c = qv(x.c), h = qv(x.h), R = qdiv(h, c);
    return [num('How many recipes do ' + mixedOut(h) + ' cups make? (' + mixedOut(h) + ' ÷ ' + mixedOut(c) + ')', R, HINT.div(h, c) + decFine(R)),
      num('Each recipe makes ' + x.s + ' servings. How many servings is that?', p.ans, HINT.mul(R, Q(x.s)))]; }
};
/* ---- 18: a part-to-whole mixture (5.10 Notes III) */
const partName = (x, j) => x.names ? x.names[j] : E.ORD[j] + ' color';
F.mixWhole = {
  models: p => { const x = p.prm, part = x.parts[x.which], k = x.n / part, sum = x.parts[0] + x.parts[1] + x.parts[2], out = [];
    if (part !== 1) out.push(mod(Q(x.n * sum), 'multiplied the ' + x.n + ' ' + x.unit + ' by all ' + sum + ' parts. First find one part: ' + x.n + ' ÷ ' + part + '.', 0));
    out.push(mod(Q(k), 'found one part, ' + k + ' ' + x.unit + ', and stopped. The whole batch is all ' + sum + ' parts.', 1));
    const others = [0, 1, 2].filter(j => j !== x.which && x.parts[j] !== 1 && x.parts[j] !== part);
    others.filter((j, i) => others.findIndex(o => x.parts[o] === x.parts[j]) === i).forEach(j => { const same = others.filter(o => x.parts[o] === x.parts[j]);
      out.push(mod(Q(k * x.parts[j]), 'found the ' + same.map(o => partName(x, o)).join(' or the ') + ', ' + k * x.parts[j] + ' ' + x.unit + ', and stopped. The question asks for the whole batch: all ' + sum + ' parts.', 1)); });
    return out; },
  rule: () => 'One part first — the amount you know ÷ its number in the ratio — then the whole batch: one part × the sum of the parts.',
  sol: p => { const x = p.prm, part = x.parts[x.which], k = x.n / part, sum = x.parts[0] + x.parts[1] + x.parts[2];
    return [{ say: 'The ' + partName(x, x.which) + ' is ' + part + ' ' + plural(Q(part), 'part', 'parts') + ' of the ratio, so one part is ' + M(x.n + ' ÷ ' + part + ' = ' + k) + ' ' + x.unit + '.' },
      { say: 'The whole batch is ' + M(x.parts.join(' + ') + ' = ' + sum) + ' parts:', ex: EX(sum + ' × ' + k + ' = ' + S(p.ans), p.ans) }]; },
  walk: p => { const x = p.prm, part = x.parts[x.which], k = Q(x.n, part), sum = x.parts[0] + x.parts[1] + x.parts[2];
    return [num('The ' + partName(x, x.which) + ' is ' + part + ' ' + plural(Q(part), 'part', 'parts') + ' and ' + x.n + ' ' + x.unit + '. How much is one part?', k, part === 1 ? 'One part is the whole of the ' + partName(x, x.which) + '.' : HINT.div(Q(x.n), Q(part))),
      num('How many parts is the whole batch? ' + M(x.parts.join(' + ')), Q(sum), 'Add the three numbers of the ratio.'),
      num('What is ' + sum + ' × ' + S(k) + '?', p.ans, HINT.mul(Q(sum), k))]; }
};

/* ---- 19: two speeds in two units (5.10 Notes II: "Two rates in different units cannot be compared until they are in one
   unit.") — the answer is the faster one's name and the mi/h speed in km/h */
const spd = x => ({ K0: Q(x.kmh), conv: qmul(Q(x.mph), qdec('1.61')), slow: x.fast === x.a ? x.b : x.a, mover: x.b });
F.faster = {
  models: p => { const x = p.prm, { K0, conv } = spd(x);
    return [mod(K0, 'typed the ' + x.a + '’s ' + x.kmh + ' — that is already km/h. The ' + x.b + '’s ' + x.mph + ' mi/h is the speed to change: × 1.61.', 1),
      mod(Q(x.mph), 'typed the ' + x.b + '’s ' + x.mph + ' as it stands — that is mi/h. A mile is 1.61 km, so in km/h it is ' + x.mph + ' × 1.61.', 1),
      mod(qdiv(Q(x.mph), qdec('1.61')), 'divided by 1.61. A mile is longer than a kilometer, so ' + x.mph + ' mi/h is MORE than ' + x.mph + ' km/h: multiply.', 1),
      mod(qmul(K0, qdec('1.61')), 'multiplied the ' + x.a + '’s km/h by 1.61. The km/h needs no change; change the ' + x.b + '’s mi/h: ' + x.mph + ' × 1.61.', 1),
      mod(qmul(K0, qdec('0.62')), 'changed the ' + x.a + '’s speed to mi/h. That compares them too — but the box asks for the ' + x.b + '’s speed in km/h: ' + x.mph + ' × 1.61.', 1)]; },
  rule: p => 'Same unit first: a mile is 1.61 km, so ' + p.prm.mph + ' mi/h × 1.61 is km/h. Then compare the two km/h speeds — the bigger is faster.',
  sol: p => { const x = p.prm, { K0, conv } = spd(x), [hi, lo] = qlt(conv, K0) ? [K0, conv] : [conv, K0];
    return [{ say: 'Put both speeds in km/h. A mile is 1.61 km, so the ' + x.b + ' does ' + M(x.mph + ' × 1.61 = ' + S(conv)) + ' km/h.' },
      { say: 'Compare in one unit: ' + M(S(hi) + ' &gt; ' + S(lo)) + ', so the ' + x.fast + ' is faster.', ex: EX(x.mph + ' × 1.61 = ' + S(conv), p.ans) }]; },
  walk: p => { const x = p.prm, { K0, conv, slow } = spd(x);
    return [choice('Can you compare ' + x.kmh + ' km/h with ' + x.mph + ' mi/h as they are?', [O('No — put them in the same unit first', true),
        O('Yes — the bigger number is faster', false, 'A kilometer and a mile are different lengths, so ' + x.kmh + ' and ' + x.mph + ' count different things.')]),
      choice('A mile is 1.61 km. So ' + x.mph + ' mi/h in km/h is …', [O(M(x.mph + ' × 1.61'), true), O(M(x.mph + ' ÷ 1.61'), false, 'A mile is longer than a kilometer, so there are more kilometers than miles: multiply.')]),
      num('What is ' + M(x.mph + ' × 1.61') + '?', conv, HINT.mul(Q(x.mph), qdec('1.61'))),
      choice('So which is faster?', [O('The ' + x.fast, true), O('The ' + slow, false, 'Compare ' + x.kmh + ' km/h with ' + S(conv) + ' km/h: the bigger one is faster.')])]; }
};
/* what was typed for question 19: the names in it, and the rest */
function namesIn(p, typed) {
  const x = p.prm, t0 = ' ' + String(typed == null ? '' : typed).toLowerCase().replace(/[’']/g, '') + ' ';
  const has = w => new RegExp('(^|[^a-z])' + w + 's?([^a-z]|$)').test(t0);
  const names = [x.a, x.b].filter(has);
  const rest = t0.replace(new RegExp('(^|[^a-z])(' + x.a + '|' + x.b + ')s?(?=[^a-z]|$)', 'g'), '$1').replace(/\b(the|is|was|faster|fastest|at|does|goes|and|by|km\/?h|kmh|kph)\b/g, ' ').replace(/[:;,]/g, ' ').replace(/\s+/g, ' ').trim();
  return { names, rest };
}

/* ------------------------------------------------------------------ marking a typed answer */
const RULE = p => F[p.fam].rule(p);
const joinSays = hs => hs.map((h, i) => (i ? ' — or if you ' : 'That is what you get if you ') + h.say.replace(/\.$/, '')).join('') + '.';
/* a typed value is a mistake's value: exactly, or that value rounded to the places typed (a value that never ends, like
   1,200 ÷ 270, is typed rounded) — never by rounding to fewer places than the mistake's minDp */
function rounds(v, r, minDp) {
  if (r.form !== 'num' || r.dp == null || r.dp < (minDp || 0)) return false;
  const pv = places(v); if (pv >= 0 && r.dp >= pv) return false;
  return (v.n < 0n) === (r.val.n < 0n) && qeq(qround(qabs(v), r.dp), qabs(r.val));
}
function hits(p, r) {
  const ms = F[p.fam].models(p) || [], seen = [];
  const keep = list => list.filter(m => { if (seen.indexOf(m.say) >= 0) return false; seen.push(m.say); return true; });
  /* a typed number may be one mistake exactly and another rounded (5 ÷ 2.204 and 5 × 0.454 are both 2.27): both are named */
  return keep(ms.filter(m => (qeq(m.v, r.val) || rounds(m.v, r, m.minDp)) && !qeq(m.v, p.ans)));
}
/* "33/4" or "3-3/4" typed for 3 3/4: the whole number and the fraction with no space between them */
function didMean(typed, A) {
  if (isInt(A)) return null;
  const t = String(typed == null ? '' : typed).trim().replace(/\s*(?:cups?|c)\.?\s*$/i, '');
  let m = /^(\d+)\s*[-–−]\s*(\d+)\s*\/\s*(\d+)$/.exec(t), w, nn, d;
  if (m) { w = m[1]; nn = m[2]; d = m[3]; }
  else if ((m = /^(\d{2,})\/(\d+)$/.exec(t))) {
    for (let i = 1; i < m[1].length && !w; i++) { const a = m[1].slice(0, i), b = m[1].slice(i); if (b[0] !== '0' && +b < +m[2]) { w = a; nn = b; d = m[2]; } } }
  if (!w || +d === 0) return null;
  return qeq(qadd(Q(BigInt(w)), Q(BigInt(nn), BigInt(d))), A) ? w + ' ' + nn + '/' + d : null;
}
function generic() { return 'Not one of the usual slips. Check each step against the rule below, or tap Hint to go one step at a time.'; }
const plainKey = p => p.money ? money(p.ans) : p.cups ? mixedOut(p.ans) : S(p.ans);
/* the working a student did, as the sentence about it: "7 × 2.54" */
const workSay = p => { const x = p.prm; return p.fam === 'chain' ? N(x.n) + ' × 3 × 12 × 2.54' : x.n + ' × ' + x.f; };
function feedback(p, typed, ctx) {
  if (p.name) return nameFeedback(p, typed, ctx);
  return numFeedback(p, typed, ctx);
}
/* question 19: the name decides, the number proves it */
function nameFeedback(p, typed, ctx) {
  const x = p.prm, { names, rest } = namesIn(p, typed);
  if (names.length === 2) return { v: 'unread', what: ['Name just one: which is faster?'] };
  const r = numFeedback(p, rest, ctx), name = names[0] || null, mover = x.b;
  if (!name && r.v === 'unread' && /[a-z]{3,}/.test(String(typed).toLowerCase().replace(/km\/?h|kmh|kph|mi\/?h|mph/g, ''))) return { v: 'unread', what: ['Which is it, the ' + x.a + ' or the ' + x.b + '? Type its name, and the ' + x.b + '’s speed in km/h.'] };
  if (r.v === 'blank') {
    if (!name) return r;
    if (name === x.fast) return { v: 'form', what: ['Yes — now show it: the ' + mover + '’s speed in km/h, beside the name.'], rule: '' };
    return { v: 'wrong', what: ['The ' + x.a + '’s speed is in km/h and the ' + x.b + '’s in mi/h: compare them in one unit first. Change ' + x.mph + ' mi/h to km/h (× 1.61), then decide.'], rule: RULE(p), step: 0 };
  }
  if (r.v === 'right' || r.v === 'form') {
    if (!name) return r.v === 'right' ? { v: 'form', what: ['That is the ' + mover + '’s speed in km/h. Now say which is faster: its name goes with the speed.'], rule: '' } : r;
    if (name === x.fast) return r;
    const { K0, conv } = spd(x), [hi, lo] = qlt(conv, K0) ? [K0, conv] : [conv, K0];
    return { v: 'wrong', what: ['The conversion is right — but compare the two km/h speeds: ' + M(S(hi) + ' &gt; ' + S(lo)) + ', so the ' + x.fast + ' is faster.'], rule: RULE(p), step: null };
  }
  return r;
}
function numFeedback(p, typed, ctx) {
  const r = E.readAns(typed);
  if (r.blank) return { v: 'blank', what: [] };
  if (!r.ok) return { v: 'unread', what: [r.msg] };
  const rule = RULE(p), A = p.ans;
  /* a mixed number typed without its space, or with a hyphen, when the mixed number would be right: asked about, counted as
     nothing, and never told the number (the M7 Unit 9 re-read of 30 Oct 2026: a wrong 11/2 was told "Did you mean 1 1/2?") */
  const meant = didMean(typed, A); if (meant && !qeq(r.val, A)) return { v: 'unread', what: ['If that is a mixed number, put a space between the whole number and the fraction, like 1 1/3.'] };
  if (qeq(r.val, A)) {
    if (r.form === 'num' && r.frac !== 'unreduced') return { v: 'right', what: [] };
    if (r.form === 'num') return { v: 'form', what: [p.cups || places(A) < 0 || isInt(A) ? 'That is the right amount. Write the fraction in its simplest form: ' + plainKey(p) + '.'
      : 'That is the right amount. Write the fraction in its simplest form, ' + A.n + '/' + A.d + ' — or as the decimal, ' + plainKey(p) + '.'], rule: '' };
    return { v: 'form', what: ['That works out to the right number. Finish the arithmetic: write it as one number.'], rule: '' };
  }
  /* the sheet's other ratio (the reference sheet: both directions are accepted): exactly, when it comes out so (the critic of
     30 Oct 2026: 66 ÷ 0.264 = 250 was called "the answer rounded"), or rounded to the places typed */
  const via = p.fam === 'chain' ? N(qmul(qv(p.prm.n), Q(36))) + ' ÷ 0.39' : p.fam === 'faster' ? p.prm.mph + ' ÷ 0.62' : p.prm.n + ' ÷ ' + p.prm.o;
  if (p.alt && r.form === 'num' && qlt(Q(0), r.val) && qeq(p.alt, r.val))
    return { v: 'right', what: ['Right — by the sheet’s other ratio, ' + M(p.altRatio) + ': ' + M(via + ' = ' + numStr(r.val)) + '. With the ratio printed here the answer is ' + plainKey(p) + '.'] };
  if (r.form === 'num' && r.dp != null && qlt(Q(0), r.val)) {
    /* the key rounded: every answer here comes out exactly, so a rounded one is not finished */
    if (places(A) > 0 && r.dp < places(A) && qeq(qround(A, r.dp), r.val))
      return { v: 'form', what: [p.money ? 'Give money to the cent: two decimal places.' : 'That is the answer rounded. ' + (p.alt ? M(workSay(p)) + ' comes out exactly: give every digit.' : 'It comes out exactly: give every digit.')], rule: '' };
    /* the sheet's other ratio, rounded to the places typed */
    if (p.alt && r.dp >= 1 && qeq(qround(p.alt, r.dp), r.val))
      return { v: 'right', what: ['Right — by the sheet’s other ratio, ' + M(p.altRatio) + ': ' + M(via + ' ≈ ' + numStr(r.val)) + '. With the ratio printed here the answer is exact.'] };
    if (p.alt && r.dp === 0 && qeq(qround(p.alt, 0), r.val))
      return { v: 'form', what: ['That is the sheet’s other ratio rounded to a whole number. Keep the decimals, or use the ratio printed here: it comes out exactly.'], rule: '' };
  }
  /* follow-through (ruling 19; the test's 6(b) and 16(b)): the right step done to the student's own part (a) */
  if (F[p.fam].follow && ctx && ctx.prev != null && ctx.prevPart) {
    const pr = E.readAns(ctx.prev);
    if (pr.ok && pr.val && !qeq(pr.val, ctx.prevPart.ans) && qlt(Q(0), pr.val)) {
      const want = F[p.fam].follow(p, pr.val);
      if (want && (qeq(want, r.val) || rounds(want, r))) {
        const yours = numStr(pr.val);
        if (ctx.mode === 'test') return { v: 'right', follow: true, what: ['Part (a) isn’t right, but this part does the right step with your own part (a), ' + yours + ' — so on the test it still earns its point.'], rule: '' };
        return { v: 'wrong', what: ['Your method for this part is right: it uses your part (a), ' + yours + '. But part (a) isn’t right yet, so this comes out wrong too. Fix part (a) first.'], rule: '', step: null };
      }
    }
  }
  const h = hits(p, r);
  if (h.length) return { v: 'wrong', what: [joinSays(h)], rule, step: h[0].step };
  /* the key cut off after some places, not rounded (the readers of 30 Oct 2026: 5.7 for 5.75, 215 for 215.9) — when it is
     not a named mistake */
  if (r.form === 'num' && r.dp != null && qlt(Q(0), r.val) && places(A) > 0 && r.dp < places(A) && qeq(qfloor(qmul(A, Q(10n ** BigInt(r.dp)))), qmul(r.val, Q(10n ** BigInt(r.dp)))))
    return { v: 'form', what: ['That is the answer cut off after ' + (r.dp === 0 ? 'the whole number' : r.dp === 1 ? 'one decimal place' : r.dp + ' decimal places') + ', not rounded. It comes out exactly: give every digit.'], rule: '' };
  if (qlt(r.val, Q(0))) return { v: 'wrong', what: ['An amount here is never negative. Drop the minus sign and check the steps again.'], rule };
  return { v: 'wrong', what: [generic()], rule };
}

/* ------------------------------------------------------------------ multiple choice and select-all */
const lettersSay = ix => { const L = ix.slice().sort((a, b) => a - b).map(i => LET[i]); return L.length === 1 ? L[0] : L.slice(0, -1).join(', ') + ' and ' + L[L.length - 1]; };
const sqParts = x => { const pr = x.prm, r = qdec(pr.r); return { pr, r, r2: qmul(r, r), from: UW[pr.from], to: UW[pr.to] }; };
const MCW = {
  sqConv: (x, k) => { const { pr, r, r2, from, to } = sqParts(x), tag = x.tags[k];
    if (tag === 'once') return 'That uses the ratio once: ' + M(N(pr.A) + ' × ' + pr.r) + '. A square ' + from[0] + ' is ' + pr.r + ' ' + to[1] + ' on each side, so use the ratio twice: × ' + M(pr.r + sup(2)) + '.';
    if (tag === 'alone') return 'That is ' + M(pr.r + sup(2) + ' = ' + S(r2)) + ', the square ' + to[1] + ' in ONE square ' + from[0] + '. Multiply by the ' + M(N(pr.A) + ' ' + sqU(pr.from)) + '.';
    return 'That multiplies by 2 × ' + pr.r + '. Squaring is ' + pr.r + ' × ' + pr.r + ', not 2 × ' + pr.r + '.'; },
};
const MCRULE = {
  sqConv: () => 'A square unit uses the length ratio twice: the area × the ratio².',
  kFacts: () => 'A scale copy: every length × k, the perimeter × k, the area × k², and every angle stays the same.',
  convSel: () => 'Two ways give the answer: × the ratio whose 1 is the unit you have, or ÷ the ratio whose 1 is the unit you want.'
};
function mcFeedback(x, k) {
  if (k === x.correct) return { v: 'right', what: [] };
  const w = MCW[x.fam] ? MCW[x.fam](x, k) : 'Not that one. Work it through with the rule below.';
  return { v: 'wrong', what: [w], rule: MCRULE[x.fam] ? MCRULE[x.fam]() : '' };
}
/* the value of one of question 10's expressions, as printed: exact when it ends, else to two places */
const convVal = (n, op, v) => { const q = op === '×' ? qmul(Q(n), qdec(v)) : qdiv(Q(n), qdec(v)); return places(q) >= 0 ? { q, say: ' = ' + S(q) } : { q, say: ' ≈ ' + fixed(q, 2) }; };
const SELWHY = {
  kFacts: (x, i) => { const k = qdec(x.prm.k), k2 = qmul(k, k), tag = x.tags[i], L = LET[i] + '. ';
    return L + ({ side: 'True: a scale copy multiplies every length — every side — by k = ' + S(k) + '.',
      angle: 'Not true: an angle is not a length. The copy has the same shape, so every angle stays the same.',
      perim: 'True: the perimeter is the sides added, and each side is × ' + S(k) + ', so the perimeter is × ' + S(k) + '.',
      areaK: 'Not true: area is two lengths multiplied, so it is × ' + S(k) + ' twice — × ' + S(k2) + ', not × ' + S(k) + '.',
      areaK2: 'True: area is length × width, and both are × ' + S(k) + ': ' + M(S(k) + ' × ' + S(k) + ' = ' + S(k2)) + '.' })[tag]; },
  convSel: (x, i) => { const pr = x.prm, op = pr.ops[i][0], v = pr.ops[i].slice(1), cv = convVal(pr.n, op, v), tag = x.tags[i], have = UW[pr.from][0], want = UW[pr.to][0];
    const head = LET[i] + '. ' + M(pr.n + ' ' + op + ' ' + v + cv.say) + ': ';
    const oneOf = v === (pr.from === pr.pair.split('/')[0] ? pr.ab : pr.ba) ? have : want;      /* the unit whose 1 this ratio is for */
    if (tag === 'mulRight') return head + 'true — × the ratio whose 1 is ' + an(have) + ', the unit you have.';
    if (tag === 'divRight') return head + 'true — ÷ the ratio whose 1 is ' + an(want) + ', the unit you want.';
    if (tag === 'mulWrong') return head + 'not true — that multiplies by the ratio whose 1 is ' + an(oneOf) + ', the unit you want: the ratio the wrong way round.';
    return head + 'not true — that divides by the ratio whose 1 is ' + an(oneOf) + ', the unit you have: the ratio the wrong way round.'; }
};
function selectFeedback(x, ks, tries) {
  const picked = (ks || []).map(Number), right = x.correct;
  const wrongPicks = picked.filter(i => right.indexOf(i) < 0), missed = right.filter(i => picked.indexOf(i) < 0);
  if (!wrongPicks.length && !missed.length) return { v: 'right', what: [] };
  const rule = MCRULE[x.fam]();
  const what = x.fam === 'kFacts' ? ['isn’t true about the copy', 'aren’t true about the copy', 'is true', 'are true'] : ['doesn’t give the ' + x.prm.toW, 'don’t give the ' + x.prm.toW, 'gives them', 'give them'];
  if ((tries || 1) <= 1) return { v: 'wrong', what: [(wrongPicks.length ? (wrongPicks.length === 1 ? 'One of your picks ' + what[0] : wrongPicks.length + ' of your picks ' + what[1]) : 'Every one you picked ' + (x.fam === 'kFacts' ? 'is true' : 'gives the ' + x.prm.toW)) +
    (missed.length ? (wrongPicks.length ? ', and you' : ', but you') + ' missed ' + missed.length + ' that ' + (missed.length === 1 ? what[2] : what[3]) + '.' : '.') + ' Test each one and try again.'], rule };
  return { v: 'wrong', what: wrongPicks.concat(missed).sort().map(i => SELWHY[x.fam](x, i)), rule };
}
function mcSolution(x) {
  if (x.type === 'multi') return x.opts.map((o, i) => ({ say: SELWHY[x.fam](x, i) })).concat(x.fam === 'convSel'
    ? [{ say: 'The two right ones differ a little because the sheet’s ratios are rounded; both are the sheet’s answer.' }] : []);
  const ok = LET[x.correct];
  if (x.fam === 'sqConv') { const { pr, r2, from, to } = sqParts(x);
    return [{ say: 'One square ' + from[0] + ' is ' + pr.r + ' ' + to[1] + ' by ' + pr.r + ' ' + to[1] + ': ' + M(pr.r + ' × ' + pr.r + ' = ' + S(r2)) + ' square ' + to[1] + '.' },
      { say: 'So ' + M(N(pr.A) + ' ' + sqU(pr.from)) + ' is ' + M(N(pr.A) + ' × ' + S(r2) + ' = ' + S(x.exact)) + ' square ' + to[1] + '.' },
      { say: 'The closest choice is ' + ok + '.' }]; }
  return [{ say: 'The answer is ' + ok + '.' }];
}
function solution(p, ctx) { return F[p.fam].sol(p, ctx || null); }
function KIT_shuffle(a, key) { const T = KIT.slot('a7u5', 1, 'walk|' + key); return T.shuffle(a); }      /* option order fixed per question */
/* a choice step's options are shuffled (fixed per question), except a step that says to keep them (none now: the student of 30 Oct 2026 found Q3's and Q10's letter sets always right-first) */
const mixed = (st, key) => st && st.map((x, i) => x.type === 'choice' && !x.keep ? Object.assign({}, x, { opts: KIT_shuffle(x.opts, key + '|' + i) }) : x);
function steps(p, ctx) { return mixed(F[p.fam].walk(p, ctx || null), p.key); }
function stepsMC(x) { return mixed(stepsMC0(x), x.key); }
function stepsMC0(x) {
  if (x.fam === 'sqConv') { const { pr, r, r2, from, to } = sqParts(x);
    return [choice('A square ' + from[0] + ' is a square ' + pr.r + ' ' + to[1] + ' on each side. Its area in square ' + to[1] + ' is …', [O(M(pr.r + ' × ' + pr.r), true),
        O(M('2 × ' + pr.r), false, 'Area is side × side: ' + pr.r + ' × ' + pr.r + ', not 2 × ' + pr.r + '.'), O(M(pr.r), false, 'That is the length of one side. A square has area side × side.')]),
      num('What is ' + M(pr.r + ' × ' + pr.r) + '?', r2, HINT.mul(r, r)),
      num('What is ' + M(N(pr.A) + ' × ' + S(r2)) + '? That is the area in square ' + to[1] + '.', x.exact, HINT.mul(Q(pr.A), r2)),
      choice('Which choice is closest to ' + S(x.exact) + '?', x.vals.map((v, i) => O(LET[i], i === x.correct, i === x.correct ? '' : S(v) + ' is far from ' + S(x.exact) + '.')), { keep: true })]; }
  if (x.fam === 'kFacts') { const k = qdec(x.prm.k), k2 = qmul(k, k), at = t => x.tags.indexOf(t);
    const right = x.correct, noK2 = [at('side'), at('perim'), at('areaK')], plusAngle = right.concat([at('angle')]), sideOnly = [at('side'), at('perim')];
    return [choice('A scale copy multiplies every length by k. What happens to each angle?', [O('It stays the same — an angle is not a length', true),
        O('It is × ' + S(k), false, 'The copy has the same shape as the original, so its angles are the same.')]),
      choice('The perimeter is the sides added. It is …', [O('× ' + S(k), true), O('× ' + S(k2), false, 'Each side is × ' + S(k) + ', so their sum is × ' + S(k) + '. Squaring is for area.')]),
      num('Area is length × width, each × ' + S(k) + '. What is ' + S(k) + ' × ' + S(k) + '?', k2, HINT.mul(k, k)),
      choice('So the true statements are …', [O(lettersSay(right), true), O(lettersSay(noK2), false, 'The area is × ' + S(k2) + ', not × ' + S(k) + '.'),
        O(lettersSay(plusAngle), false, 'The angles do not change.'), O(lettersSay(sideOnly), false, 'The area changes too: × ' + S(k2) + '.')])]; }
  if (x.fam === 'convSel') { const pr = x.prm, P = E.PAIRS[pr.pair], have = UW[pr.from][0], want = UW[pr.to][0];
    const forHave = pr.from === P.a ? P.ab : P.ba, forWant = pr.from === P.a ? P.ba : P.ab;
    const at = (op, v) => pr.ops.indexOf(op + v), right = x.correct;
    return [choice('Which ratio is for 1 ' + have + ', the unit you have?', [O(M(ratioH(pr.from, forHave, pr.to)), true), O(M(ratioH(pr.to, forWant, pr.from)), false, 'That one starts with 1 ' + want + ', the unit you want.')]),
      choice('With the ratio for 1 ' + have + ', you …', [O('multiply: ' + M(pr.n + ' × ' + forHave), true), O('divide: ' + M(pr.n + ' ÷ ' + forHave), false, 'Each ' + have + ' is ' + forHave + ' ' + UW[pr.to][1] + ', so ' + pr.n + ' of them is a multiplication.')]),
      choice('With the ratio for 1 ' + want + ', you …', [O('divide: ' + M(pr.n + ' ÷ ' + forWant), true), O('multiply: ' + M(pr.n + ' × ' + forWant), false, 'Each ' + want + ' is ' + forWant + ' ' + UW[pr.from][1] + ', so count how many ' + forWant + 's fit in ' + pr.n + ': divide.')]),
      choice('So the two that give the ' + pr.toW + ' are …', [O(lettersSay(right), true), O(lettersSay([at('×', forHave), at('×', forWant)]), false, 'Only one ratio is multiplied; the other is divided.'),
        O(lettersSay([at('÷', forHave), at('×', forWant)]), false, 'Those are the two ways round the wrong way.'), O(lettersSay([at('×', forHave), at('÷', forHave)]), false, 'Those use one ratio both ways; only one of them is right.')])]; }
  return null;
}

/* ------------------------------------------------------------------ the clean rule */
function printedNumbers(it) {
  const t = [it.stem].concat(E.partsOf(it).map(p => p.stem || '')).join(' ').replace(/<sup[^>]*>(.*?)<\/sup>/g, ' ').replace(/<span class="fr"><span class="nu">(\d+)<\/span><span class="de">(\d+)<\/span><\/span>/g, ' $1/$2 ').replace(/<[^>]+>/g, ' ');
  const out = []; let m; const re = /(\d[\d,]*(?:\.\d+)?)(?:\s*\/\s*(\d+))?/g;
  while ((m = re.exec(t))) out.push(m[2] ? Q(BigInt(m[1]), BigInt(m[2])) : qdec(m[1].replace(/,/g, '')));
  return out;
}
function clean(it) {
  if (!it || it.bad) return false;
  if (it.type === 'mc' || it.type === 'multi') {
    const txt = it.opts.map(o => String(o).replace(/<[^>]+>/g, ''));
    if (new Set(txt).size !== it.opts.length) return false;
    if (it.fam === 'sqConv') {
      /* the right choice is the closest to the exact area by both of the sheet's routes (× r², or ÷ the other ratio²),
         and every other choice is at least 15% away */
      const o = qdec(it.prm.o), ex = qnum(it.exact), alt = qnum(qdiv(Q(it.prm.A), qmul(o, o)));
      const vals = it.vals.map(qnum), near = x => vals.map(v => Math.abs(v - x)), best = d => d.indexOf(Math.min(...d));
      if (best(near(ex)) !== it.correct || best(near(alt)) !== it.correct) return false;
      if (vals.some((v, i) => i !== it.correct && Math.abs(v - ex) < 0.15 * ex)) return false;
    }
    if (it.fam === 'convSel' && it.correct.length !== 2) return false;
    return true;
  }
  const parts = E.partsOf(it), ans = parts.map(p => p.ans);
  for (let i = 0; i < ans.length; i++) for (let j = i + 1; j < ans.length; j++) if (qeq(ans[i], ans[j])) return false;
  /* a part (b)'s Hint never asks for a number that is part (a)'s answer, even by chance (the M7 Unit 9 review) */
  for (let i = 1; i < parts.length; i++) if (F[parts[i].fam].walk(parts[i]).some(s => s.type === 'num' && qeq(s.ans, ans[0]))) return false;
  const printed = printedNumbers(it);
  for (const p of parts) {
    if (printed.some(x => qeq(x, p.ans))) return false;
    const pa = places(p.ans), models = F[p.fam].models(p);
    for (const m of models) {
      if (qeq(m.v, p.ans)) return false;
      /* a mistake rounded to the answer's own places is not the answer, so typing the mistake rounded is never right */
      if (pa > 0 && !((m.minDp || 0) > pa) && qeq(qround(qabs(m.v), pa), p.ans)) return false;
      /* nor is it the other ratio's answer rounded */
      if (p.alt) for (let dp = 0; dp <= 3; dp++) if (qeq(qround(qabs(m.v), dp), qround(p.alt, dp))) return false;
      /* nor is a mistake worth exactly the answer rounded (that would be marked "Almost" before it is named) */
      for (let dp = 0; dp < pa; dp++) if (qeq(m.v, qround(p.ans, dp))) return false;
    }
  }
  return true;
}
E.setClean(clean);

const api = { F, feedback, numFeedback, nameFeedback, namesIn, mcFeedback, selectFeedback, mcSolution, solution, clean, joinSays, printedNumbers, SELWHY, MCW, MCRULE, UW, estSay, lettersSay, hits, rounds };
const walkApi = { steps, stepsMC, readNum: E.readNum };
if (node) module.exports = Object.assign({}, api, { Walk: walkApi }); else { root.Coach = api; root.Walk = walkApi; }
})(this);
