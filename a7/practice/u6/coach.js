/* A7 Unit 6 practice: the coach. For every kind of question: the mistakes students make (each with the exact value it gives —
   or, when it ends on a square root that is not whole, the number it comes to — and the words that finish "That is what you
   get if you …"), the rule, the worked steps (Show me how), the step-by-step Hint, and the marking of a typed answer.
   Registers the clean rule with the engine: no mistake, no printed number and no other part's answer may equal an answer,
   so a wrong method is never marked right. The named mistakes are the unit's: adding the squares when a leg is asked, the
   hypotenuse taken as a leg, the forgotten square root, the wrong side tested in the converse, the wrong pair summed in the
   Triangle Inequality, subtracting across zero, counting grid lines, and matching sides that do not correspond. */
(function (root) {
'use strict';
const E = (typeof module !== 'undefined' && module.exports) ? require('./engine.js') : root.Practice;
const KIT = (typeof module !== 'undefined' && module.exports) ? require('../kit/core.js') : root.Kit;
const { Q, qadd, qsub, qmul, qdiv, qneg, qabs, qeq, qlt, qnum, qdec, numStr, N, M, sqrtH, sup, sq, X, pt, isqrt, isSquare, rootOK, sqrtTenth, sqrtCut, plusSqrtTenth, roundSqrt, sorted, qk, kIn, kOut } = E;
const S = numStr;
const HINT = KIT.hint;
/* the kit's division hint, unless its stepping stone happens to be the answer (72 ÷ 6: "72 − 60 = 12 is left"): then the
   plain question behind it */
const divHint = (a, b) => { const h = HINT.div(a, b), q = E.numStr(E.qdiv(a, b));
  return new RegExp('= ' + q.replace(/\./g, '\\.') + '(?![\\d.])').test(h) ? 'Think: ' + E.numStr(b) + ' × ? = ' + E.numStr(a) + '.' : h; };
const LET = 'ABCDEFGH';
const mod = (v, say, step) => ({ v, say, step: step == null ? null : step });                 /* a mistake worth exactly v */
const near = (f, say, step) => ({ f, say, step: step == null ? null : step });                /* a mistake that ends on √ of a non-square: about f */
const choice = (ask, opts, extra) => Object.assign({ type: 'choice', ask, opts }, extra || {});
const num = (ask, ans, hint, extra) => Object.assign({ type: 'num', ask, ans, hint }, extra || {});
const O = (label, ok, why) => ({ label, ok: !!ok, why: why || '' });
const EX = (h, v, o) => Object.assign({ h, v }, o || {});                                   /* a worked line: its html and its exact value (the answer) */

/* √n as printed in a worked line: the radical only when it is already in simplest form */
const rootH = n => rootOK(n) ? sqrtH(n) : 'the square root of ' + n;
/* the first three decimals of A + s·√n, cut off (exactly, from the integer square root), for "= 14.764…" */
function cut3(A, n, s) {
  const k = isqrt(n * 1000000), v = s < 0 ? 1000 * A - k - 1 : 1000 * A + k, w = Math.abs(v);
  return (v < 0 ? '−' : '') + E.commas(String(Math.floor(w / 1000))) + '.' + String(w % 1000).padStart(3, '0') + '…';
}
/* the hundredths digit of A + s·√n, and whether the tenth goes up */
function hundredths(A, n, s) { const k = isqrt(n * 10000), v = s < 0 ? 100 * A - k - 1 : 100 * A + k; return ((v % 10) + 10) % 10; }
function roundSay(A, n, s, ans) {
  const d = hundredths(A, n, s);
  return 'Round to the nearest tenth: the hundredths digit is ' + d + ', so the tenths digit ' + (d >= 5 ? 'goes up' : 'stays') + '.';
}
/* between which two whole numbers √n lies: the Hint's stepping stone (never the answer) */
const between = n => { const r = isqrt(n); return 'The root of ' + n + ' is between ' + r + ' and ' + (r + 1) + ', because ' + r + sup(2) + ' = ' + r * r + ' and ' + (r + 1) + sup(2) + ' = ' + (r + 1) * (r + 1) + '.'; };
const sqHint = (a, b, op) => { const v = String(a) !== '2' ? a : String(b) !== '2' ? b : null, then = 'then ' + (op === '-' ? 'subtract' : 'add') + '.';
  return v == null ? 'Square each number first, ' + then : 'Square each number first — ' + v + sup(2) + ' means ' + v + ' × ' + v + ', not ' + v + ' × 2 — ' + then; };
/* a root kept to three decimal places, exactly (rounded): the Hint's stepping stone before rounding once, at the end */
const sqrt3 = n => { const k = isqrt(n * 1000000), up = 4 * n * 1000000 >= (2 * k + 1) * (2 * k + 1); return Q(up ? k + 1 : k, 1000); };
const rootHint = m => { const r = isqrt(m); return 'Try ' + (r - 1) + ' × ' + (r - 1) + ' = ' + (r - 1) * (r - 1) + ' and go up one at a time.'; };
const tenthHint = n => between(n) + ' Use the square-root key, then keep one decimal place, rounding with the next digit.';

/* the truncated and the whole-number roundings of a tenth answer, when they differ from it */
function roundingModels(p, A, n, s, step) {
  const out = [], cut = Q(s < 0 ? 10 * A - isqrt(100 * n) - 1 : 10 * A + isqrt(100 * n), 10);
  if (!qeq(cut, p.ans)) out.push(mod(cut, 'cut the decimal off instead of rounding. The next digit is ' + hundredths(A, n, s) + ', so round up to ' + S(p.ans) + '.', step));
  const whole = Q(s < 0 ? A - roundSqrt(n) : A + roundSqrt(n));
  if (!qeq(whole, p.ans)) out.push(mod(whole, 'rounded to a whole number. The question asks for the nearest tenth: one decimal place.', step));
  return out;
}

/* ------------------------------------------------------------------ the families */
const F = {};
const legsOf = p => { const x = p.prm; return { dx: Math.abs(x.x2 - x.x1), dy: Math.abs(x.y2 - x.y1) }; };
/* across zero, a student who subtracts the two distances to the axis instead of adding them: that leg, or null */
const signSlip = (u, v) => E.crosses(u, v) && Math.abs(Math.abs(v) - Math.abs(u)) > 0 ? Math.abs(Math.abs(v) - Math.abs(u)) : null;
const across = (u, v, what) => E.crosses(u, v) ? ' (across zero: ' + Math.abs(u) + ' to the axis and ' + Math.abs(v) + ' past it, ' + Math.abs(u) + ' + ' + Math.abs(v) + ')' : ' (' + E.minus(String(Math.max(u, v))) + ' − ' + (Math.min(u, v) < 0 ? '(' + E.minus(String(Math.min(u, v))) + ')' : Math.min(u, v)) + ')';

/* a hypotenuse from two legs, whole */
F.hypWhole = {
  models: p => { const { a, b } = p.prm, out = [mod(Q(a + b), 'added the legs. The theorem adds their SQUARES, ' + sq(a) + ' + ' + sq(b) + ', then takes the square root.', 0),
    mod(Q(a * a + b * b), 'stopped at c' + sup(2) + ' = ' + (a * a + b * b) + ' and forgot the square root.', 1)];
    if (a !== b) out.push(near(Math.sqrt(Math.abs(a * a - b * b)), 'subtracted the squares. For the hypotenuse, add them: it is the longest side.', 0));
    return out; },
  rule: () => 'a' + sup(2) + ' + b' + sup(2) + ' = c' + sup(2) + ': square the two legs, add, then take the square root. The hypotenuse is the longest side.',
  sol: p => { const { a, b } = p.prm, n = a * a + b * b;
    return [{ say: 'The legs make the right angle, so ' + a + ' and ' + b + ' are a and b. The hypotenuse c is across from the right angle.' },
      { say: 'Square the legs and add: ' + M('c' + sup(2) + ' = ' + sq(a) + ' + ' + sq(b) + ' = ' + a * a + ' + ' + b * b + ' = ' + n) + '.' },
      { say: 'c is the number whose square is ' + n + '.', ex: EX(sqrtH(n) + ' = ' + S(p.ans), p.ans) }]; },
  walk: p => { const { a, b } = p.prm, n = a * a + b * b;
    return [choice('Which side is the hypotenuse, c?', [O('the side you are finding: it is across from the right angle', true),
      O('the longer of the two sides given, ' + Math.max(a, b), false, 'A leg makes the right angle. The hypotenuse is across from it, and it is longer than either leg.')]),
      num('What is ' + sq(a) + ' + ' + sq(b) + '?', Q(n), sqHint(a, b, '+')),
      num('What number times itself is ' + n + '?', p.ans, rootHint(n))]; }
};
/* a leg from the hypotenuse and the other leg, whole */
F.legWhole = {
  models: p => { const { c, a } = p.prm;
    return [near(Math.sqrt(c * c + a * a), 'added the squares. For a leg, subtract: this comes out longer than the hypotenuse, ' + S(Q(c)) + ', and a leg is shorter.', 2),
      mod(Q(c - a), 'subtracted the sides. The theorem is about their squares: ' + sq(c) + ' − ' + sq(a) + '.', 1),
      mod(Q(c * c - a * a), 'stopped at b' + sup(2) + ' = ' + S(Q(c * c - a * a)) + ' and forgot the square root.', 3)]; },
  rule: () => 'For a leg, subtract: b' + sup(2) + ' = c' + sup(2) + ' − a' + sup(2) + ', then take the square root. A leg is always shorter than the hypotenuse.',
  sol: p => { const { c, a } = p.prm, m = c * c - a * a;
    return [{ say: 'The hypotenuse is ' + S(Q(c)) + ': that is c. The ' + S(Q(a)) + ' is a leg, and b is the other.' },
      { say: 'Put the numbers in a' + sup(2) + ' + b' + sup(2) + ' = c' + sup(2) + ': ' + M(sq(a) + ' + b' + sup(2) + ' = ' + sq(c)) + '.' },
      { say: 'Subtract to find b' + sup(2) + ': ' + M('b' + sup(2) + ' = ' + S(Q(c * c)) + ' − ' + S(Q(a * a)) + ' = ' + S(Q(m))) + '.' },
      { say: 'b is the number whose square is ' + S(Q(m)) + '.', ex: EX(sqrtH(m) + ' = ' + S(p.ans), p.ans) }]; },
  walk: p => { const { c, a } = p.prm, m = c * c - a * a;
    return [choice('Which number is c, the hypotenuse?', [O(S(Q(c)), true), O(S(Q(a)), false, 'That is a leg: the hypotenuse is the longest side, ' + S(Q(c)) + '.')]),
      choice('So to find the other leg, you …', [O('subtract: ' + S(Q(c)) + sup(2) + ' − ' + S(Q(a)) + sup(2), true),
        O('add: ' + S(Q(a)) + sup(2) + ' + ' + S(Q(c)) + sup(2), false, 'Adding makes a side longer than the hypotenuse — but a leg is shorter than it.')]),
      num('What is ' + S(Q(c)) + sup(2) + ' − ' + S(Q(a)) + sup(2) + '?', Q(m), sqHint(S(Q(c)), S(Q(a)), '-')),
      num('What number times itself is ' + S(Q(m)) + '?', p.ans, rootHint(m))]; }
};
/* a leg in a story, to the nearest tenth: the ladder, the ramp or the kite string is the hypotenuse (6.04) */
const STORY = { ladder: { c: 'the ladder', a: 'the distance from the wall to its foot', along: 'out from the wall', b: 'the height up the wall', lies: 'lies along the ground' },
  ramp: { c: 'the ramp', a: 'the distance it runs along the ground', along: 'along the ground', b: 'how high it rises', lies: 'lies along the ground' },
  kite: { c: 'the string', a: 'the distance from the hand to the point below the kite', along: 'from the hand, level with it', b: 'how high the kite is above that point', lies: 'runs level from the hand' } };
F.legTenth = {
  models: p => { const { c, a, ctx } = p.prm, m = c * c - a * a, W = STORY[ctx];
    return [near(Math.sqrt(c * c + a * a), 'added the squares. ' + W.c[0].toUpperCase() + W.c.slice(1) + ' is the hypotenuse, so this leg is found by subtracting: ' + sq(c) + ' − ' + sq(a) + '.', 1),
      mod(Q(c - a), 'subtracted the lengths. The theorem is about their squares: ' + sq(c) + ' − ' + sq(a) + '.', 2),
      mod(Q(m), 'stopped at ' + m + ' and forgot the square root.', 3)].concat(roundingModels(p, 0, m, 1, 3)); },
  rule: p => STORY[p.prm.ctx].c[0].toUpperCase() + STORY[p.prm.ctx].c.slice(1) + ' is the hypotenuse, across from the right angle. For a leg, subtract: b' + sup(2) + ' = c' + sup(2) + ' − a' + sup(2) + ', take the square root, then round to one decimal place.',
  sol: p => { const { c, a, ctx } = p.prm, m = c * c - a * a, W = STORY[ctx];
    return [{ say: W.c[0].toUpperCase() + W.c.slice(1) + ', ' + c + ', is the hypotenuse: it is across from the right angle. The other two sides are the legs — ' + a + ' ' + W.along + ', and ' + W.b + ', the one you want.' },
      { say: 'Subtract to find the leg squared: ' + M('b' + sup(2) + ' = ' + sq(c) + ' − ' + sq(a) + ' = ' + c * c + ' − ' + a * a + ' = ' + m) + '.' },
      { say: 'Take the square root: b = ' + (rootOK(m) ? M(sqrtH(m)) + ' = ' : rootH(m) + ', ') + cut3(0, m, 1) },
      { say: roundSay(0, m, 1, p.ans), ex: EX(S(p.ans), p.ans, { approx: true }) }]; },
  walk: p => { const { c, a, ctx } = p.prm, m = c * c - a * a, W = STORY[ctx];
    return [choice('Which length is the hypotenuse, c?', [O(W.c + ', ' + c, true), O(W.a + ', ' + a, false, 'That one ' + W.lies + ': it makes the right angle, so it is a leg.')]),
      choice('So to find ' + W.b + ', you …', [O('subtract: ' + sq(c) + ' − ' + sq(a), true),
        O('add: ' + sq(a) + ' + ' + sq(c), false, 'Adding makes a side longer than the hypotenuse, ' + c + ' — but a leg is shorter than it.')]),
      num('What is ' + sq(c) + ' − ' + sq(a) + '?', Q(m), sqHint(c, a, '-')),
      num('What is ' + (rootOK(m) ? sqrtH(m) : 'the square root of ' + m) + ', to the nearest tenth?', p.ans, tenthHint(m))]; }
};
/* a hypotenuse to the nearest tenth (also the field's path, part a) */
function hypTenthFam(lead) {
  return {
    models: p => { const { a, b } = lead(p), n = a * a + b * b, out = [mod(Q(a + b), p.fam === 'diag' ? 'added the sides. That is the walk along two sides, not the path straight across.' : 'added the legs. The theorem adds their squares, then takes the square root.', 0),
      mod(Q(n), 'stopped at c' + sup(2) + ' = ' + n + ' and forgot the square root.', 1)].concat(roundingModels(p, 0, n, 1, 2));
      if (a !== b) out.push(near(Math.sqrt(Math.abs(a * a - b * b)), 'subtracted the squares. For the hypotenuse, add them.', 0));
      return out; },
    rule: () => 'Square the legs, add, take the square root, then round to one decimal place — the hundredths digit decides.',
    sol: p => { const { a, b, what } = lead(p), n = a * a + b * b;
      return [{ say: (what || 'The legs make the right angle; the hypotenuse c is across from it.') + ' ' + M('c' + sup(2) + ' = ' + sq(a) + ' + ' + sq(b) + ' = ' + a * a + ' + ' + b * b + ' = ' + n) + '.' },
        { say: 'Take the square root: c = ' + (rootOK(n) ? M(sqrtH(n)) + ' = ' : rootH(n) + ', ') + cut3(0, n, 1) },
        { say: roundSay(0, n, 1, p.ans), ex: EX(S(p.ans), p.ans, { approx: true }) }]; },
    walk: p => { const { a, b } = lead(p), n = a * a + b * b;
      return [num('What is ' + sq(a) + ' + ' + sq(b) + '?', Q(n), sqHint(a, b, '+')),
        num('What is ' + (rootOK(n) ? sqrtH(n) : 'the square root of ' + n) + ', to the nearest tenth?', p.ans, tenthHint(n))]; }
  };
}
F.hypTenth = hypTenthFam(p => ({ a: p.prm.a, b: p.prm.b }));
F.diag = hypTenthFam(p => ({ a: p.prm.w, b: p.prm.l, what: 'The path and two sides of the ' + p.prm.place + ' make a right triangle: the path is the hypotenuse.' }));
/* the field, part b: how much shorter the path is than two sides */
F.shorter = {
  models: p => { const { w, l } = p.prm, n = w * w + l * l, path = sqrtTenth(n);
    return [mod(path, 'gave the length of the path. The question asks how much SHORTER it is: take it away from the walk along two sides.', 2),
      mod(Q(w + l), 'gave the walk along two sides. Take the path away from it.', 2),
      mod(qadd(Q(w + l), path), 'added the two walks. How much shorter is a difference: subtract.', 2)].concat(roundingModels(p, w + l, n, -1, 2)); },
  rule: () => 'How much shorter = the walk along two sides − the path straight across. The path is the hypotenuse.',
  follow: (p, prev) => p.prm.w + p.prm.l - prev,
  sol: p => { const { w, l } = p.prm, n = w * w + l * l, path = sqrtTenth(n);
    return [{ say: 'Along two sides: ' + M(w + ' + ' + l + ' = ' + (w + l)) + '.' },
      { say: 'Straight across, the path is ' + (rootOK(n) ? M(sqrtH(n)) + ' = ' : rootH(n) + ', ') + cut3(0, n, 1) + ' — about ' + S(path) + ' to the nearest tenth (part a).' },
      { say: 'Subtract: ' + M((w + l) + ' − ' + S(path) + ' = ' + S(p.ans)) + '. (With every digit, ' + (w + l) + ' − ' + cut3(0, n, 1) + ' = ' + cut3(w + l, n, -1) + ', the same to the nearest tenth.)', ex: EX(S(p.ans), p.ans, { approx: true }) }]; },
  walk: p => { const { w, l } = p.prm, n = w * w + l * l, path = sqrtTenth(n);
    const p3 = sqrt3(n);
    return [num('How far is it along two sides of the ' + p.prm.place + '?', Q(w + l), 'Add its two sides.'),
      num('How long is the path straight across? Keep three decimal places.', p3, between(n) + ' Use the square-root key and keep three decimal places: round once, at the end.'),
      num('What is ' + (w + l) + ' − ' + S(p3) + ', to the nearest tenth?', p.ans, 'Take away the path from the walk along two sides, lining up the decimal points; then round to one decimal place.')]; }
};

/* ---------- distance on the coordinate plane */
function legSay(p) { const x = p.prm, { dx, dy } = legsOf(p);
  return [{ say: 'Across: from x = ' + E.minus(String(x.x1)) + ' to x = ' + E.minus(String(x.x2)) + ' is ' + dx + across(x.x1, x.x2) + '.' },
    { say: (x.y2 > x.y1 ? 'Up' : 'Down') + ': from y = ' + E.minus(String(x.y1)) + ' to y = ' + E.minus(String(x.y2)) + ' is ' + dy + across(x.y1, x.y2) + '.' }]; }
function legWalk(p) { const x = p.prm, { dx, dy } = legsOf(p);
  const h = (u, v, axis) => E.crosses(u, v) ? 'One point is on each side of the ' + axis + '-axis: add the two distances to the axis, ' + Math.abs(u) + ' and ' + Math.abs(v) + '.' : 'Subtract the smaller from the larger.';
  return [num('How far across is it, from x = ' + E.minus(String(x.x1)) + ' to x = ' + E.minus(String(x.x2)) + '?', Q(dx), h(x.x1, x.x2, 'y'), { pic: true }),
    num('How far ' + (x.y2 > x.y1 ? 'up' : 'down') + ' is it, from y = ' + E.minus(String(x.y1)) + ' to y = ' + E.minus(String(x.y2)) + '?', Q(dy), h(x.y1, x.y2, 'x'), { pic: true })]; }
function slipModels(p, whole, grid) {
  const x = p.prm, { dx, dy } = legsOf(p), out = [], put = (ax, ay, say) => { const m = ax * ax + ay * ay; out.push(isSquare(m) ? mod(Q(isqrt(m)), say, 0) : near(Math.sqrt(m), say, 0)); };
  const sx = signSlip(x.x1, x.x2), sy = signSlip(x.y1, x.y2);
  if (sx) put(sx, dy, 'subtracted across zero: from x = ' + E.minus(String(x.x1)) + ' to x = ' + E.minus(String(x.x2)) + ' is ' + Math.abs(x.x1) + ' + ' + Math.abs(x.x2) + ' = ' + dx + ' across, not ' + sx + '.');
  if (sy) put(dx, sy, 'subtracted across zero: from y = ' + E.minus(String(x.y1)) + ' to y = ' + E.minus(String(x.y2)) + ' is ' + Math.abs(x.y1) + ' + ' + Math.abs(x.y2) + ' = ' + dy + ', not ' + sy + '.');
  put(dx + 1, dy + 1, grid ? 'counted the grid lines, not the spaces between them: the legs are ' + dx + ' and ' + dy + '.'
    : 'counted one too many on each leg — the numbers from one coordinate to the other, not the steps between them: the legs are ' + dx + ' and ' + dy + '.');
  return out;
}
F.gridWhole = {
  models: p => { const { dx, dy } = legsOf(p);
    return [mod(Q(dx + dy), 'added the legs. That is the trip along the grid lines; the straight distance is the hypotenuse.', 2),
      mod(Q(dx * dx + dy * dy), 'stopped at ' + (dx * dx + dy * dy) + ' and forgot the square root.', 3)].concat(slipModels(p, true, true)); },
  rule: () => 'Draw the right triangle under the segment. Its legs are the across and the up-or-down distances, read from the coordinates; the distance is the hypotenuse.',
  sol: p => { const { dx, dy } = legsOf(p), n = dx * dx + dy * dy;
    return legSay(p).concat([{ say: 'The distance is the hypotenuse: ' + M('c' + sup(2) + ' = ' + sq(dx) + ' + ' + sq(dy) + ' = ' + dx * dx + ' + ' + dy * dy + ' = ' + n) + '.' },
      { say: 'c is the number whose square is ' + n + '.', ex: EX(sqrtH(n) + ' = ' + S(p.ans), p.ans) }]); },
  walk: p => { const { dx, dy } = legsOf(p), n = dx * dx + dy * dy;
    return legWalk(p).concat([num('What is ' + sq(dx) + ' + ' + sq(dy) + '?', Q(n), sqHint(dx, dy, '+')), num('What number times itself is ' + n + '?', p.ans, rootHint(n))]); }
};
F.coordTenth = {
  models: p => { const { dx, dy } = legsOf(p), n = dx * dx + dy * dy;
    return [mod(Q(dx + dy), 'added the legs. That is the trip along the grid lines; the straight distance is the hypotenuse.', 2),
      mod(Q(n), 'stopped at ' + n + ' and forgot the square root.', 3)].concat(roundingModels(p, 0, n, 1, 4), slipModels(p, false, false)); },
  rule: () => 'Picture the right triangle under the segment: the legs come from the coordinates, the distance is the hypotenuse, then round to one decimal place.',
  sol: p => { const { dx, dy } = legsOf(p), n = dx * dx + dy * dy;
    return legSay(p).concat([{ say: 'The distance is the hypotenuse: ' + M('c' + sup(2) + ' = ' + sq(dx) + ' + ' + sq(dy) + ' = ' + dx * dx + ' + ' + dy * dy + ' = ' + n) + '.' },
      { say: 'Take the square root: c = ' + (rootOK(n) ? M(sqrtH(n)) + ' = ' : rootH(n) + ', ') + cut3(0, n, 1) },
      { say: roundSay(0, n, 1, p.ans), ex: EX(S(p.ans), p.ans, { approx: true }) }]); },
  walk: p => { const { dx, dy } = legsOf(p), n = dx * dx + dy * dy;
    return legWalk(p).concat([num('What is ' + sq(dx) + ' + ' + sq(dy) + '?', Q(n), sqHint(dx, dy, '+')),
      num('What is ' + (rootOK(n) ? sqrtH(n) : 'the square root of ' + n) + ', to the nearest tenth?', p.ans, tenthHint(n))]); }
};
/* the triangle on the grid: its side that crosses an axis, and its perimeter */
function triParts(p) {
  const { J, K, L, names } = p.prm, horiz = J[1] === K[1], i = horiz ? 0 : 1;
  return { J, K, L, names, horiz, i, s: Math.abs(K[i] - J[i]), h: Math.abs(L[1 - i] - K[1 - i]), JK: names[0] + names[1], KL: names[1] + names[2], JL: names[0] + names[2] };
}
F.crossSide = {
  models: p => { const t = triParts(p), u = t.J[t.i], v = t.K[t.i], out = [];
    const sl = signSlip(u, v); if (sl) out.push(mod(Q(sl), 'subtracted across zero. From ' + E.minus(String(u)) + ' to ' + E.minus(String(v)) + ' is ' + Math.abs(u) + ' to the axis and ' + Math.abs(v) + ' past it: ' + Math.abs(u) + ' + ' + Math.abs(v) + '.', 0));
    out.push(mod(Q(t.s + 1), 'counted the grid lines, not the spaces between them.', 0));
    return out; },
  rule: () => 'On one grid line, subtract the coordinates that change — and across zero, the two distances to the axis add.',
  sol: p => { const t = triParts(p), c = t.horiz ? 'x' : 'y', u = t.J[t.i], v = t.K[t.i];
    return [{ say: t.names[0] + ' and ' + t.names[1] + ' have the same ' + (t.horiz ? 'y' : 'x') + '-coordinate, so ' + t.JK + ' lies along a grid line: only the ' + c + '-coordinates change.' },
      { say: 'From ' + c + ' = ' + E.minus(String(u)) + ' to ' + c + ' = ' + E.minus(String(v)) + ' crosses zero: ' + Math.abs(u) + ' to the axis and ' + Math.abs(v) + ' past it.', ex: EX(Math.abs(u) + ' + ' + Math.abs(v) + ' = ' + t.s, p.ans) }]; },
  walk: p => { const t = triParts(p), c = t.horiz ? 'x' : 'y', u = t.J[t.i], v = t.K[t.i];
    return [choice('Which coordinates change from ' + t.names[0] + ' to ' + t.names[1] + '?', [O('the ' + c + '-coordinates', true), O('the ' + (t.horiz ? 'y' : 'x') + '-coordinates', false, 'Look again: ' + t.names[0] + ' and ' + t.names[1] + ' have the same ' + (t.horiz ? 'y' : 'x') + '.')]),
      num('How far is it from ' + c + ' = ' + E.minus(String(u)) + ' to ' + c + ' = ' + E.minus(String(v)) + '?', p.ans, 'One is below zero and one above: add the two distances to the axis, ' + Math.abs(u) + ' and ' + Math.abs(v) + '.')]; }
};
F.perim = {
  models: p => { const t = triParts(p), n = t.s * t.s + t.h * t.h;
    return [mod(Q(t.s + t.h), 'left the slanted side out. A perimeter adds every side.', 1),
      mod(Q(2 * (t.s + t.h)), 'took the slanted side as the two legs added. It is the hypotenuse of those legs, shorter than their sum.', 1),
      mod(Q(t.s + t.h + n), 'forgot the square root on the slanted side.', 1)].concat(roundingModels(p, t.s + t.h, n, 1, 2)); },
  rule: () => 'A perimeter adds every side. A side on a grid line is a difference of coordinates; a slanted side is the hypotenuse of its own right triangle. Round once, at the end.',
  follow: (p, prev) => { const t = triParts(p); return prev + t.h + Math.sqrt(prev * prev + t.h * t.h); },
  sol: p => { const t = triParts(p), n = t.s * t.s + t.h * t.h;
    return [{ say: t.JK + ' = ' + t.s + ' (part a). ' + t.KL + ' lies along a grid line too: ' + t.h + '.' },
      { say: 'The slanted side ' + t.JL + ' is the hypotenuse of those two: ' + M(t.JL + sup(2) + ' = ' + sq(t.s) + ' + ' + sq(t.h) + ' = ' + n) + ', so ' + t.JL + ' = ' + (rootOK(n) ? M(sqrtH(n)) + ' = ' : rootH(n) + ', ') + cut3(0, n, 1) },
      { say: 'Add the three sides, and round once, at the end: ' + t.s + ' + ' + t.h + ' + ' + cut3(0, n, 1) + ' = ' + cut3(t.s + t.h, n, 1) + ' ' + roundSay(t.s + t.h, n, 1, p.ans).replace(/^Round/, '— round'), ex: EX(S(p.ans), p.ans, { approx: true }) }]; },
  walk: p => { const t = triParts(p), n = t.s * t.s + t.h * t.h, js = sqrtTenth(n);
    const j3 = sqrt3(n);
    return [num('How long is ' + t.KL + '?', Q(t.h), 'It lies along a grid line: subtract the coordinates that change.'),
      num('How long is the slanted side ' + t.JL + '? Keep three decimal places.', j3, 'It is the hypotenuse of a right triangle with legs ' + t.s + ' and ' + t.h + '. ' + between(n) + ' Keep three decimal places: round once, at the end.'),
      num('What is ' + t.s + ' + ' + t.h + ' + ' + S(j3) + ', to the nearest tenth?', p.ans, 'Add the three sides, then round to one decimal place.')]; }
};
/* the town map: along the streets, and straight */
F.streets = {
  models: p => { const { dx, dy } = legsOf(p), x = p.prm, out = [mod(Q(isqrt(dx * dx + dy * dy)), 'gave the straight line. Along the streets you go across and then up or down: add the two legs.', 0)];
    const sx = signSlip(x.x1, x.x2), sy = signSlip(x.y1, x.y2);
    if (sx) out.push(mod(Q(sx + dy), 'subtracted across zero: across is ' + Math.abs(x.x1) + ' + ' + Math.abs(x.x2) + ' = ' + dx + ', not ' + sx + '.', 0));
    if (sy) out.push(mod(Q(dx + sy), 'subtracted across zero: up or down is ' + Math.abs(x.y1) + ' + ' + Math.abs(x.y2) + ' = ' + dy + ', not ' + sy + '.', 1));
    return out; },
  rule: () => 'Along the streets, the trip follows the grid: the distance across plus the distance up or down.',
  sol: p => { const { dx, dy } = legsOf(p); return legSay(p).concat([{ say: 'Along the streets you go across and then up or down.', ex: EX(dx + ' + ' + dy + ' = ' + (dx + dy), p.ans) }]); },
  walk: p => { const { dx, dy } = legsOf(p); return legWalk(p).concat([num('What is ' + dx + ' + ' + dy + '?', p.ans, 'Add the two legs.')]); }
};
F.straight = {
  models: p => { const { dx, dy } = legsOf(p); return [mod(Q(dx + dy), 'gave the trip along the streets. The straight line is the hypotenuse.', 1),
    mod(Q(dx * dx + dy * dy), 'stopped at ' + (dx * dx + dy * dy) + ' and forgot the square root.', 1)].concat(slipModels(p, true, false)); },
  rule: () => 'The straight line is the hypotenuse of the right triangle whose legs are the trip across and the trip up or down.',
  sol: p => { const { dx, dy } = legsOf(p), n = dx * dx + dy * dy;
    return [{ say: 'The legs are ' + dx + ' across and ' + dy + (p.prm.y2 > p.prm.y1 ? ' up' : ' down') + ' (part a).' },
      { say: 'The straight line is the hypotenuse: ' + M('c' + sup(2) + ' = ' + sq(dx) + ' + ' + sq(dy) + ' = ' + n) + '.', ex: EX(sqrtH(n) + ' = ' + S(p.ans), p.ans) }]; },
  walk: p => { const { dx, dy } = legsOf(p), n = dx * dx + dy * dy;
    return [num('What is ' + sq(dx) + ' + ' + sq(dy) + '?', Q(n), sqHint(dx, dy, '+')), num('What number times itself is ' + n + '?', p.ans, rootHint(n))]; }
};

/* ---------- similar triangles */
/* "a decimal is fine" when k ends, "a fraction is fine" when it does not (4/3); times a fraction: divide, then multiply */
const kFine = k => E.places(k) >= 0 ? ' A decimal is fine.' : ' A fraction is fine.';
const mulHint = (a, k) => E.places(k) >= 0 ? HINT.mul(a, k) : 'Times ' + kOut(k) + ': divide ' + S(a) + ' by ' + k.d + ', then multiply by ' + k.n + '.';
/* adding a number to every side, or taking one away (a copy smaller than the first triangle) */
const addSay = (d, what) => qlt(d, Q(0)) ? 'took ' + S(qabs(d)) + ' off ' + what : 'added ' + S(d) + ' to ' + what;
const turnedSay = p => p.prm.turn === 'flip' ? 'flipped over' : 'turned';
function simParts(p) {
  const { p: a, q: b, r: c, which } = p.prm, k = qk(p.prm.k), side = { p: a, q: b, r: c }[which];
  const known = ['p', 'q', 'r'].filter(s => s !== which), o1 = { p: a, q: b, r: c }[known[0]], c1 = qmul(Q(o1), k);
  /* named triangles (engine CORNERS): side p runs between corners 0 and 2, q between 1 and 2, r between 0 and 1 */
  const nm = p.prm.nm, ends = { p: [0, 2], q: [1, 2], r: [0, 1] }, seg = (off, s) => nm[off + ends[s][0]] + nm[off + ends[s][1]];
  const names = nm ? { first: nm.slice(0, 3).join(''), copy: nm.slice(3).join(''), xOn: seg(3, which), xMatch: seg(0, which),
    pairs: nm[0] + ' with ' + nm[3] + ', ' + nm[1] + ' with ' + nm[4] + ' and ' + nm[2] + ' with ' + nm[5] } : null;
  return { a, b, c, k, which, side, known, o1, c1, names, size: { p: 'shortest', q: 'middle', r: 'longest' } };
}
F.simSide = {
  models: p => { const t = simParts(p), out = [mod(Q(t.side), 'took the triangles to be equal. Similar means the second is a scale copy: every side times one k.', 1),
    mod(qdiv(Q(t.side), t.k), 'divided by the scale factor. The copy is ' + (qlt(t.k, Q(1)) ? 'smaller' : 'bigger') + ', so multiply by k = ' + kOut(t.k) + '.', 2)];
    const d = qsub(t.c1, Q(t.o1)); if (d.n !== 0n) out.push(mod(qadd(Q(t.side), d), addSay(d, 'the side') + '. Similar means multiplied, not added.', 1));
    if (t.which === 'r') { const kq = qmul(Q(t.b), t.k); out.push(mod(qdiv(qmul(Q(t.c), kq), Q(t.a)), 'matched the sides by where they sit on the page. The copy is ' + turnedSay(p) + ': match them by size, shortest with shortest.', 0)); }
    return out; },
  rule: () => 'Match the sides by size — shortest with shortest, longest with longest. Find k = copy ÷ original from a pair you know, then multiply.',
  sol: p => { const t = simParts(p);
    return (t.names ? [{ say: 'The names give the matching: in "triangle ' + t.names.first + ' is similar to triangle ' + t.names.copy + '" the order of the letters is the matching, ' + t.names.pairs + '. x is on ' + t.names.xOn + ', so it matches ' + t.names.xMatch + ', the ' + t.side + '.' }] : []).concat([
      { say: 'Match by size' + (t.names ? ', and it agrees' : '') + '. The first triangle\'s sides are ' + t.a + ', ' + t.b + ' and ' + t.c + '; x is on the copy\'s ' + t.size[t.which] + ' side, so it matches the ' + t.side + '.' },
      { say: 'The scale factor from a pair you know: ' + M('k = ' + S(t.c1) + ' ÷ ' + t.o1 + ' = ' + kIn(t.k)) + '.' },
      { say: 'Multiply the matching side by k.', ex: EX(t.side + ' × ' + kIn(t.k) + ' = ' + S(p.ans), p.ans) }]); },
  walk: p => { const t = simParts(p), val = { p: t.a, q: t.b, r: t.c }, nm = p.prm.nm, ends = { p: [0, 2], q: [1, 2], r: [0, 1] };
    const segOf = s => nm[ends[s][0]] + nm[ends[s][1]], lab = s => String(val[s]) + (nm ? ' — ' + segOf(s) : '');
    const whyNot = s => nm ? 'The letters match in order: ' + t.names.xOn + ' matches ' + t.names.xMatch + ', not ' + segOf(s) + '.'
      : 'Match by size: x is on the copy\'s ' + t.size[t.which] + ' side, and ' + val[s] + ' is the first triangle\'s ' + t.size[s] + ' side.';
    return [choice(t.names ? 'x is on ' + t.names.xOn + '. In "triangle ' + t.names.first + ' is similar to triangle ' + t.names.copy + '" the order of the letters is the matching. Which side of triangle ' + t.names.first + ' does x match?'
      : 'The copy is ' + turnedSay(p) + '. Which side of the first triangle does x match?', ['p', 'q', 'r'].map(s => O(lab(s), s === t.which, s === t.which ? '' : whyNot(s)))),
      num('What is the scale factor, k = ' + S(t.c1) + ' ÷ ' + t.o1 + '?', t.k, 'The copy\'s side over its match in the first triangle: ' + S(t.c1) + ' ÷ ' + t.o1 + '.' + kFine(t.k)),
      num('What is ' + t.side + ' × ' + kOut(t.k) + '?', p.ans, mulHint(Q(t.side), t.k))]; }
};
function lightParts(p) {
  const x = p.prm, h1 = qdec(x.h1), shadow = x.mode === 'shadow', s1 = qdec(shadow ? x.s1 : x.d1), s2 = qdec(shadow ? x.s2 : x.d2);
  return { h1, s1, s2, k: qdiv(s2, s1), shadow, base: shadow ? 'shadow' : 'distance from the mirror', who: shadow ? 'the ' + x.who : x.name, what: x.what,
    small: shadow ? 'the ' + x.who + '\'s height' : 'the height of ' + x.name + '\'s eyes' };
}
function lightFam() {
  return {
    models: p => { const t = lightParts(p), out = [mod(qdiv(qmul(t.s2, t.s1), t.h1), 'matched a height with a ' + (t.shadow ? 'shadow' : 'distance') + '. Match like with like: k = ' + S(t.s2) + ' ÷ ' + S(t.s1) + '.', 1),
      mod(qmul(t.s2, t.h1), 'multiplied the ' + (t.shadow ? 'shadow' : 'distance') + ' by the height. Multiply the height by k, the ratio of the ' + (t.shadow ? 'shadows' : 'distances') + '.', 2),
      mod(t.k, 'stopped at k. The ' + t.what + ' is k times ' + t.small + ', ' + S(t.h1) + ' × k.', 2)];
      const add = qadd(t.s2, qsub(t.h1, t.s1)); if (qlt(Q(0), add)) out.push(mod(add, 'added the difference. Similar means multiplied: one k for the height and the ' + t.base + '.', 1));
      return out; },
    rule: p => (lightParts(p).shadow ? 'Same sun, same angle: ' : 'A mirror sends light back at the angle it came in: ') + 'the two right triangles are similar. k = the ratio of the ' + (lightParts(p).shadow ? 'shadows' : 'distances') + '; the height you want is k times the height you know.',
    sol: p => { const t = lightParts(p);
      return [{ say: (t.shadow ? 'The sun makes the same angle with both, so the two right triangles are similar.' : 'Light leaves the mirror at the angle it arrives, so the two right triangles are similar.') },
        { say: 'k from the ' + (t.shadow ? 'shadows' : 'distances along the ground') + ': ' + M('k = ' + S(t.s2) + ' ÷ ' + S(t.s1) + ' = ' + kIn(t.k)) + '.' },
        { say: 'The ' + t.what + ' is k times ' + t.small + '.', ex: EX(S(t.h1) + ' × ' + kIn(t.k) + ' = ' + S(p.ans), p.ans) }]; },
    walk: p => { const t = lightParts(p);
      return [choice('Which length matches the ' + t.what + '\'s ' + t.base + '?', [O(t.who + '\'s ' + t.base + ', ' + S(t.s1) + ' ft', true),
        O(t.small + ', ' + S(t.h1) + ' ft', false, 'Match like with like: a ' + t.base + ' with a ' + t.base + ', a height with a height.')]),
        num('What is the scale factor, k = ' + S(t.s2) + ' ÷ ' + S(t.s1) + '?', t.k, divHint(t.s2, t.s1) + (E.places(t.k) >= 0 ? '' : kFine(t.k))),
        num('What is ' + S(t.h1) + ' × ' + kOut(t.k) + '?', p.ans, mulHint(t.h1, t.k))]; }
  };
}
F.shadow = lightFam(); F.mirror = lightFam();

/* ------------------------------------------------------------------ marking a typed answer */
const RULE = p => F[p.fam].rule(p);
const joinSays = hs => hs.map((h, i) => (i ? ' — or if you ' : 'That is what you get if you ') + h.say.replace(/\.$/, '')).join('') + '.';
const TOL = 0.051;                                                                     /* a near mistake: its value rounded to the tenth, or kept longer */
/* a mistake worth an exact terminating value is matched exactly; one that ends on a root, or on a fraction that never ends
   (13 × 9 ÷ 7), is matched to within its rounding */
const fuzzy = m => m.f != null ? m.f : (E.places(m.v) < 0 ? qnum(m.v) : null);
function hits(p, r) {
  return (F[p.fam].models(p) || []).filter(m => { const f = fuzzy(m);
    if (f == null) return r.val && qeq(m.v, r.val) && !qeq(m.v, p.ans);
    return Math.abs(f - r.f) < TOL && Math.abs(f - qnum(p.ans)) >= TOL; });
}
function generic() { return 'Not one of the usual slips. Check each step against the rule below, or tap Hint to go one step at a time.'; }
const KEYH = p => E.ansHtml(p);
function feedback(p, typed, ctx) {
  const r = E.readAns(typed);
  if (r.blank) return { v: 'blank', what: [] };
  if (!r.ok) return { v: 'unread', what: [r.msg] };
  const rule = RULE(p), A = p.ans, a = qnum(A);
  const roundsTo = f => { const t = Math.round(f * 10 + 1e-9) / 10; return Math.abs(t - a) < 1e-9; };
  if (r.val && qeq(r.val, A)) {
    if (r.form === 'num') return { v: 'right', what: [] };
    if (r.form === 'root') return { v: 'form', what: ['That is right — and ' + M(sqrtH(r.n)) + ' = ' + S(A) + '. Finish it: write ' + S(A) + '.'], rule: '' };
    return { v: 'form', what: ['That works out to the right number. Finish the arithmetic: write it as one number, ' + KEYH(p) + '.'], rule: '' };
  }
  if (p.tenth) {
    if (Math.abs(r.f - p.exact) < 1e-7) return { v: 'form', what: ['That is the exact length. The question asks for it to the nearest tenth: round it to one decimal place.'], rule: '' };
    if (r.form !== 'root' && roundsTo(r.f) && Math.abs(r.f - p.exact) < TOL) return { v: 'form', what: ['Almost — keep one decimal place: round to the nearest tenth.'], rule: '' };
  } else if (r.form === 'root' && Math.abs(r.f - a) < 1e-9) {
    return { v: 'form', what: ['That is right — finish it: ' + M(sqrtH(r.n)) + ' = ' + S(A) + '.'], rule: '' };
  }
  if (F[p.fam].follow && ctx && ctx.prev != null && ctx.prevPart) {
    const pr = E.readAns(ctx.prev);
    if (pr.ok && !(pr.val && qeq(pr.val, ctx.prevPart.ans)) && Math.abs(F[p.fam].follow(p, pr.f) - r.f) < TOL) {
      const yours = S(pr.val || Q(Math.round(pr.f * 1000), 1000));
      /* "Like the real test": the point, as the printed test's follow-through line gives it (the second review, 25 Oct 2026) */
      if (ctx.mode === 'test') return { v: 'right', follow: true, what: ['Part (a) isn’t right, but this part does the right step with your own part (a), ' + yours + ' — so on the test it still earns its point.'], rule: '' };
      return { v: 'wrong', what: ['Your method for this part is right: it uses your part (a), ' + yours + '. But part (a) isn’t right yet, so this comes out wrong too. Fix part (a) first.'], rule: '', step: null };
    }
  }
  const h = hits(p, r);
  if (h.length) return { v: 'wrong', what: [joinSays(h)], rule, step: h[0].step };
  if (r.f < 0 && Math.abs(-r.f - a) < 1e-9) return { v: 'wrong', what: ['A length is never negative.'], rule };
  return { v: 'wrong', what: [generic()], rule };
}

/* ------------------------------------------------------------------ multiple choice and select-all */
const sumSay = s => { const t = sorted(s); return t[0] + ' + ' + t[1] + ' = ' + (t[0] + t[1]); };
const MCW = {
  triSet: (x, k) => { const s = x.sets[k], t = sorted(s), tag = x.tags[k];
    if (tag === 'flat') return 'Those lie flat: ' + sumSay(s) + ' is exactly the longest side. A triangle needs the two shorter sides to add to MORE than the longest.';
    if (tag === 'firstTwo') return 'That adds the first two listed. Add the two SHORTER sides: ' + sumSay(s) + ', less than ' + t[2] + ' — they cannot meet.';
    return 'The two shorter sides, ' + sumSay(s) + ', fall short of ' + t[2] + ': they cannot meet. A triangle needs MORE than the longest side.'; },
  range: (x, k) => { const { a, b } = x.prm, tag = x.tags[k];
    if (tag === 'between') return 'That keeps the third side between the two you were given. It can be shorter than both: anything more than ' + (b - a) + ' reaches.';
    if (tag === 'leq') return 'A third side of exactly ' + (b - a) + ' or ' + (a + b) + ' would lie flat. Use &lt;, not ≤.';
    return 'That forgets the other end: a third side of ' + (b - a) + ' or less cannot reach across the ' + b + '.'; },
  eqChoice: (x, k) => { const { a, c } = x.prm, tag = x.tags[k];
    if (tag === 'sumSides') return 'That adds the sides. The theorem adds the SQUARES of the legs.';
    if (tag === 'hypLeg') return 'That puts ' + c + ', the hypotenuse, with the legs. It is across from the right angle, so it stands alone: ' + c + sup(2) + '.';
    return 'That squares the legs but not the hypotenuse. ' + c + ' is a side too: square it, ' + c + sup(2) + '.'; },
  simChoice: (x, k) => { const tag = x.tags[k], s = x.sides[k], t = x.prm.t;
    if (tag === 'add') { const d = qsub(s[0], Q(t[0])); return 'That ' + (qlt(d, Q(0)) ? 'takes ' + S(qabs(d)) + ' from' : 'adds ' + S(d) + ' to') + ' every side. Similar means every side is MULTIPLIED by one number.'; }
    if (tag === 'twoRatios') return 'Check all three ratios: ' + M(S(s[0]) + ' ÷ ' + t[0] + ' = ' + kIn(qdiv(s[0], Q(t[0])))) + ' and ' + M(S(s[1]) + ' ÷ ' + t[1] + ' = ' + kIn(qdiv(s[1], Q(t[1])))) + ', but ' + S(s[2]) + ' ÷ ' + t[2] + ' is not ' + kOut(qdiv(s[0], Q(t[0]))) + '.';
    return 'Two sides are the same as the first triangle\'s, so k would be 1 — but then the third side would be ' + t[2] + ' too.'; }
};
const MCRULE = {
  triSet: () => 'Add the two shorter sides. A triangle needs MORE than the longest side; equal lies flat.',
  range: () => 'The third side is more than the difference of the other two and less than their sum — never equal to either.',
  eqChoice: () => 'Find the right angle: the side across from it is c, alone on one side. a' + sup(2) + ' + b' + sup(2) + ' = c' + sup(2) + '.',
  simChoice: () => 'Similar: one scale factor k on every side. Check all three ratios.',
  rightSel: () => 'Square all three sides. A right triangle\'s two shorter sides\' squares add to exactly the longest side\'s square.'
};
function mcFeedback(x, k) {
  if (k === x.correct) return { v: 'right', what: [] };
  const w = MCW[x.fam] ? MCW[x.fam](x, k) : 'Not that one. Work it through with the rule below.';
  return { v: 'wrong', what: [w], rule: MCRULE[x.fam] ? MCRULE[x.fam]() : '' };
}
const SELWHY = {
  rightSel: (x, i) => { const s = x.sets[i], t = sorted(s), sum = t[0] * t[0] + t[1] * t[1], tag = x.tags[i];
    const head = LET[i] + '. ' + sq(t[0]) + ' + ' + sq(t[1]) + ' = ' + sum;
    if (tag === 'right') return head + ' = ' + sq(t[2]) + ': a right triangle' + (s[0] === t[2] ? ' (its longest side is listed first)' : '') + '.';
    const tail = { near: ' — a near miss', consec: ' — numbers in a row are not enough', remember: ' — ' + t[0] + ' and ' + t[1] + ' belong to a right triangle, but not with ' + t[2],
      triOnly: ' — a triangle, but not a right one', flat: ', and ' + t[0] + ' + ' + t[1] + ' = ' + t[2] + ': it lies flat, not even a triangle' }[tag] || '';
    return head + ', not ' + sq(t[2]) + ' = ' + t[2] * t[2] + tail + '.'; }
};
function selectFeedback(x, ks, tries) {
  const picked = (ks || []).map(Number), right = x.correct;
  const wrongPicks = picked.filter(i => right.indexOf(i) < 0), missed = right.filter(i => picked.indexOf(i) < 0);
  if (!wrongPicks.length && !missed.length) return { v: 'right', what: [] };
  const rule = MCRULE[x.fam]();
  if ((tries || 1) <= 1) return { v: 'wrong', what: [(wrongPicks.length ? (wrongPicks.length === 1 ? 'One of your picks isn’t a right triangle' : wrongPicks.length + ' of your picks aren’t right triangles') : 'Every one you picked is a right triangle') +
    (missed.length ? (wrongPicks.length ? ', and you' : ', but you') + ' missed ' + missed.length + ' that ' + (missed.length === 1 ? 'is' : 'are') + '.' : '.') + ' Test each one and try again.'], rule };
  return { v: 'wrong', what: wrongPicks.concat(missed).sort().map(i => SELWHY[x.fam](x, i)), rule };
}
function mcSolution(x) {
  if (x.type === 'multi') return x.opts.map((o, i) => ({ say: SELWHY[x.fam](x, i) }));
  const ok = LET[x.correct];
  if (x.fam === 'triSet') return x.sets.map((s, i) => { const t = sorted(s); return { say: LET[i] + '. The two shorter sides: ' + sumSay(s) + (t[0] + t[1] > t[2] ? ', more than ' + t[2] + ': a triangle.' : t[0] + t[1] === t[2] ? ', exactly ' + t[2] + ': it lies flat.' : ', less than ' + t[2] + ': they cannot meet.') }; }).concat([{ say: 'The answer is ' + ok + '.' }]);
  if (x.fam === 'range') { const { a, b } = x.prm; return [{ say: 'Long enough to reach: more than ' + b + ' − ' + a + ' = ' + (b - a) + '.' }, { say: 'Short enough to be covered: less than ' + a + ' + ' + b + ' = ' + (a + b) + '.' }, { say: 'Never equal to either — that would lie flat. The answer is ' + ok + '.' }]; }
  if (x.fam === 'eqChoice') { const { a, c } = x.prm; return [{ say: 'The right angle is between the side ' + a + ' and the side ' + X + ': those are the legs.' }, { say: 'The side across from the right angle, ' + c + ', is the hypotenuse, so it stands alone.' }, { say: 'So ' + M(sq(a) + ' + ' + X + sup(2) + ' = ' + sq(c)) + ': the answer is ' + ok + '.' }]; }
  if (x.fam === 'simChoice') { const t = x.prm.t, s = x.sides[x.correct]; return [{ say: 'Divide each side of a choice by its match: ' + s.map((v, i) => M(S(v) + ' ÷ ' + t[i] + ' = ' + kIn(qdiv(v, Q(t[i]))))).join(', ') + '.' }, { say: 'One number for all three sides: similar. The answer is ' + ok + '.' }]; }
  return [{ say: 'The answer is ' + ok + '.' }];
}
function solution(p) { return F[p.fam].sol(p); }
function KIT_shuffle(a, key) { const T = KIT.slot('a7u6', 1, 'walk|' + key); return T.shuffle(a); }      /* option order fixed per question */
/* a choice step's options are shuffled (fixed per question), except letters and counts, which keep their order */
const mixed = (st, key) => st && st.map((x, i) => x.type === 'choice' && !x.keep ? Object.assign({}, x, { opts: KIT_shuffle(x.opts, key + '|' + i) }) : x);
function steps(p) { return mixed(F[p.fam].walk(p), p.key); }
function stepsMC(x) { return mixed(stepsMC0(x), x.key); }
function stepsMC0(x) {
  if (x.fam === 'triSet') {
    return [choice('To test three lengths, which two do you add?', [O('the two shorter ones', true), O('the first two listed', false, 'The order they are listed in does not matter: only the two shorter sides can fail to reach.'),
      O('the longest and one other', false, 'The longest plus anything is always more than the third, so that test never fails.')])]
      .concat(x.sets.map((s, i) => { const t = sorted(s); return num('Choice ' + LET[i] + ' (' + x.opts[i] + '): what do its two shorter sides add to?', Q(t[0] + t[1]), 'The two shorter are ' + t[0] + ' and ' + t[1] + '.'); }))
      .concat([choice('Which choice has a sum MORE than its longest side?', x.sets.map((s, i) => { const t = sorted(s); return O(LET[i], i === x.correct, i === x.correct ? '' : t[0] + t[1] === t[2] ? 'Equal lies flat.' : (t[0] + t[1]) + ' is less than ' + t[2] + '.'); }), { keep: true })]);
  }
  if (x.fam === 'range') { const { a, b } = x.prm;
    return [num('How long must the third side be, at least, to reach? What is ' + b + ' − ' + a + '?', Q(b - a), HINT.sub(Q(b), Q(a))),
      num('How long can it be, at most, to be covered? What is ' + a + ' + ' + b + '?', Q(a + b), HINT.add(Q(a), Q(b))),
      choice('Can the third side be exactly ' + (b - a) + ' or ' + (a + b) + '?', [O('No — it would lie flat', true), O('Yes — it would still make a triangle', false, 'At exactly ' + (b - a) + ' or ' + (a + b) + ' the sides lie flat: no triangle. So the signs are &lt;, not ≤.')])]; }
  if (x.fam === 'eqChoice') { const { a, c } = x.prm;
    return [choice('Which side is across from the right angle?', [O(String(c), true), O(String(a), false, 'That side makes the right angle: it is a leg.'), O(X, false, X + ' makes the right angle with ' + a + ': it is a leg.')]),
      choice('So the equation is …', [O(M(sq(a) + ' + ' + X + sup(2) + ' = ' + sq(c)), true), O(M(sq(a) + ' + ' + sq(c) + ' = ' + X + sup(2)), false, 'The hypotenuse stands alone on one side; ' + c + ' is the hypotenuse.')])]; }
  if (x.fam === 'simChoice') { const t = x.prm.t, k = qk(x.prm.k), ok = t.map(v => qmul(Q(v), k)), first = ok[0];
    /* three of the four choices begin with the copy of the shortest side (the right one, the added one, the one with a
       wrong third side); the fourth begins with the first triangle's own shortest side */
    const why = i => { const s = x.sides[i], tag = x.tags[i];
      if (tag === 'add') { const d = qsub(s[0], Q(t[0])); return 'Its second side is ' + S(s[1]) + ', not ' + S(ok[1]) + ': it ' + (qlt(d, Q(0)) ? 'takes ' + S(qabs(d)) + ' from' : 'adds ' + S(d) + ' to') + ' each side instead of multiplying.'; }
      if (tag === 'twoRatios') return 'Its third side is ' + S(s[2]) + ', not ' + S(ok[2]) + '.';
      return 'It begins with ' + t[0] + ', the first triangle\'s own side: then k would be 1, and every side would stay the same.'; };
    return [choice('Similar triangles: every side is …', [O('multiplied by the same number', true), O('increased by the same number', false, 'Adding the same amount to each side changes this triangle\'s shape. Similar means a scale copy: multiply.')]),
      num('Three of the choices begin with ' + S(first) + ', the match for ' + t[0] + '. What is k = ' + S(first) + ' ÷ ' + t[0] + '?', k, divHint(first, Q(t[0])) + kFine(k)),
      num('Then ' + t[1] + ' becomes ' + t[1] + ' × ' + kOut(k) + '. What is ' + t[1] + ' × ' + kOut(k) + '?', ok[1], mulHint(Q(t[1]), k)),
      num('And ' + t[2] + ' becomes ' + t[2] + ' × ' + kOut(k) + '. What is ' + t[2] + ' × ' + kOut(k) + '?', ok[2], mulHint(Q(t[2]), k)),
      choice('Which choice is ' + ok.map(S).join(', ') + '?', x.sides.map((s, i) => O(LET[i], i === x.correct, i === x.correct ? '' : why(i))), { keep: true })]; }
  if (x.fam === 'rightSel') { const i = 0, t = sorted(x.sets[i]);
    return [choice('In the converse, which side do you test as c?', [O('the longest side', true), O('the last one listed', false, 'Where a side is listed does not matter: c is the longest.'), O('the first one listed', false, 'Where a side is listed does not matter: c is the longest.')]),
      num('Choice A: what is ' + sq(t[0]) + ' + ' + sq(t[1]) + '?', Q(t[0] * t[0] + t[1] * t[1]), sqHint(t[0], t[1], '+')),
      choice('Is that equal to ' + sq(t[2]) + ' = ' + t[2] * t[2] + '?', [O(isRightSet(t) ? 'Yes — choice A is a right triangle' : 'No — choice A is not a right triangle', true),
        O(isRightSet(t) ? 'No — choice A is not a right triangle' : 'Yes — choice A is a right triangle', false, 'Compare the two numbers: ' + (t[0] * t[0] + t[1] * t[1]) + ' and ' + t[2] * t[2] + '.')]),
      ...x.sets.slice(1).map((s0, j) => { const i = j + 1, u = sorted(s0), r = isRightSet(u), L = LET[i];
        return choice('Choice ' + L + ': is ' + sq(u[0]) + ' + ' + sq(u[1]) + ' = ' + (u[0] * u[0] + u[1] * u[1]) + ' equal to ' + sq(u[2]) + ' = ' + u[2] * u[2] + '?',
          [O('Yes — choice ' + L + ' is a right triangle', r, r ? '' : (u[0] * u[0] + u[1] * u[1]) + ' and ' + u[2] * u[2] + ' are not equal.'),
           O('No — choice ' + L + ' is not a right triangle', !r, r ? 'They are equal: ' + (u[0] * u[0] + u[1] * u[1]) + ' = ' + u[2] * u[2] + '.' : '')]); })]; }
  return null;
}
const isRightSet = t => t[0] * t[0] + t[1] * t[1] === t[2] * t[2];

/* ------------------------------------------------------------------ the clean rule */
function printedNumbers(it) {
  const t = [it.stem].concat(E.partsOf(it).map(p => p.stem || '')).join(' ').replace(/<sup[^>]*>(.*?)<\/sup>/g, ' ').replace(/<[^>]+>/g, ' ');
  const f = it.fig ? JSON.stringify(it.fig.labs || it.fig.lab || it.fig.la || []) + ' ' + JSON.stringify(it.fig.lb || []) + ' ' + JSON.stringify(it.fig.pts || []) : '';
  return ((t + ' ' + f).match(/\d[\d,]*(?:\.\d+)?/g) || []).map(s => qdec(s.replace(/,/g, '')));
}
function clean(it) {
  if (!it || it.bad) return false;
  if (it.type === 'mc') {
    if (new Set(it.opts).size !== it.opts.length) return false;
    if (it.fam === 'simChoice') { const k = qk(it.prm.k), first = qmul(Q(it.prm.t[0]), k);       /* the Hint's "three of the choices begin with" */
      if (it.sides.filter(s => qeq(s[0], first)).length !== 3) return false; }
    if (it.fam === 'triSet') { const keys = it.sets.map(E.setKey); if (new Set(keys).size !== 4) return false;
      return it.sets.every((s, i) => { const t = sorted(s); return (t[0] + t[1] > t[2]) === (i === it.correct); }); }
    return true;
  }
  if (it.type === 'multi') {
    if (new Set(it.sets.map(E.setKey)).size !== it.sets.length) return false;
    return it.sets.every((s, i) => isRightSet(sorted(s)) === (it.correct.indexOf(i) >= 0)) && it.correct.length >= 1 && it.correct.length <= 3;
  }
  const parts = E.partsOf(it), ans = parts.map(p => p.ans);
  for (let i = 0; i < ans.length; i++) for (let j = i + 1; j < ans.length; j++) if (qeq(ans[i], ans[j])) return false;
  const printed = printedNumbers(it);
  for (const p of parts) {
    if (printed.some(x => qeq(x, p.ans))) return false;
    for (const m of F[p.fam].models(p)) {
      if (m.v && qeq(m.v, p.ans)) return false;
      if (fuzzy(m) != null && Math.abs(fuzzy(m) - qnum(p.ans)) < 0.1) return false;
    }
    if (p.tenth && qnum(p.ans) === Math.round(qnum(p.ans))) return false;              /* a tenth that is .0 reads as a whole number */
  }
  /* similar triangles: no number on the copy is also on a side of the first triangle it does not match (the second review: an
     original 6, 9, 12 and a copy 6, x, 8 lure "same number, same side", the state's GR.2.4 misconception, on one form and not the next) */
  if (it.fig && it.fig.kind === 'simPair') { const la = it.fig.la.map(v => Number(String(v).replace(/,/g, ''))), lb = it.fig.lb;
    for (let i = 0; i < 3; i++) if (lb[i] !== 'x') for (let j = 0; j < 3; j++) if (j !== i && Number(String(lb[i]).replace(/,/g, '')) === la[j]) return false; }
  return true;
}
E.setClean(clean);

const api = { F, feedback, mcFeedback, selectFeedback, mcSolution, solution, clean, joinSays, printedNumbers, SELWHY, MCW };
const walkApi = { steps, stepsMC, readNum: E.readNum };
if (typeof module !== 'undefined' && module.exports) module.exports = Object.assign({}, api, { Walk: walkApi }); else { root.Coach = api; root.Walk = walkApi; }
})(this);
