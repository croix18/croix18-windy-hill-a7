/* A7 Unit 6 practice: the help's words and pictures, to the help standard (Windmill practice/kit/HELP_STANDARD.md, 14 Nov 2026).
   coach.js calls this at its end — help(api, walkApi) — so the unit's checks read exactly what a student reads. For each family:
     notice  Hint 1: the kind of problem and its one idea, in the decks' words; each required term spelled out in the sentence the
             first time ([[id]]), tappable after that (Croix, 14 Nov 2026: "Spell it out first time then Show on tap after")
     first   Hint 2: the first move and why (else the worked solution's first line)
     sol     Hint 3: one move a line, each with its Why: (the values are the coach's own)
     walk    Step by step with me: the coach's steps, reworded; a "why" question only on the unit's key idea — the hypotenuse is
             the longest side, across from the right angle, so a leg comes from subtracting (Croix, 14 Nov 2026)
     coach   the named mistakes, reworded to name the move and the idea it broke */
(function (root) {
'use strict';
const node = typeof module !== 'undefined' && module.exports;
const E = node ? require('./engine.js') : root.Practice;
const X = node ? require('../kit/explain.js') : root.Kit.X;
const FG = node ? require('./fig.js') : root.Fig;
const { Q, qlt, qmul, numStr, sorted } = E, S = numStr, LET = 'ABCDEFGH', sq = v => v + '²';
const O = (label, ok, why) => ({ label, ok: !!ok, why: why || '' });
const c1 = h => X.c(1, h), c2 = h => X.c(2, h), c3 = h => X.c(3, h);
const kOut = k => E.kOut ? E.kOut(k) : S(k);

X.gloss({
  triIneq: { word: 'Triangle Inequality Theorem', def: 'any two sides of a triangle add to more than the third side' },
  leg: { word: 'legs', def: 'the two sides that form the right angle' },
  leg1: { word: 'leg', def: 'one of the two sides that form the right angle' },
  hyp: { word: 'hypotenuse', def: 'the side across from the right angle; the longest side' },
  pyth: { word: 'Pythagorean Theorem', def: 'in a right triangle, a² + b² = c², where c is the hypotenuse' },
  converse: { word: 'converse', def: 'the theorem turned around: if a² + b² = c², the triangle is a right triangle' },
  sqrt: { word: 'square root', def: 'the number that, times itself, makes the given number' },
  tenth: { word: 'nearest tenth', def: 'one digit after the decimal point' },
  horiz: { word: 'horizontal distance', def: 'the distance left to right, from the x-coordinates' },
  vert: { word: 'vertical distance', def: 'the distance up and down, from the y-coordinates' },
  perimeter: { word: 'perimeter', def: 'the distance all the way around a shape' },
  similar: { word: 'similar', def: 'the same shape: every side is multiplied by one number' },
  corr: { word: 'corresponding sides', def: 'sides in matching positions in the two triangles' },
  corr1: { word: 'corresponding side', def: 'the side in the matching position in the other triangle' },
  scale: { word: 'scale factor', def: 'the number every side is multiplied by, k' }
});

/* ------------------------------------------------------------------ pictures */
const bars = (sets, label) => X.tape({ label, rows: [].concat(...sets.map(([lab, s]) => { const t = sorted(s), sum = t[0] + t[1];
  return [{ lab, segs: [{ w: t[0], c: 1, t: String(t[0]) }, { w: t[1], c: 2, t: String(t[1]) }], mark: sum > t[2] ? '✓' : sum === t[2] ? 'flat' : 'short' }, { segs: [{ w: t[2], c: 3, t: String(t[2]) }], after: 16 }]; })) });
const exampleBars = () => X.fig(bars([['', [4, 5, 7]], ['', [3, 4, 7]], ['', [2, 3, 7]]], 'Three sets of sides: the two shorter sides end to end, over the longest side.'),
  'Three examples, not the choices. Top: ' + c1('4') + ' + ' + c2('5') + ' = 9, <b>more</b> than ' + c3('7') + ': the sides can rise and meet. Middle: 3 + 4 = 7 <b>exactly</b>: they lie flat. Bottom: 2 + 3 = 5 is <b>less</b>: they fall short.');
const tri = (a, b, c, la, lb, label, cap) => X.fig(X.rightTri({ a: { t: a, c: 2 }, b: { t: b, c: 2 }, c: { t: c, c: 1 }, la, lb, label }), cap);
const triCap = c1('The hypotenuse, c,') + ' is across from the right angle. ' + c2('The legs') + ' form the right angle.';
const STORY = { ladder: ['ladder', 'ground', 'wall'], ramp: ['ramp', 'ground', 'rise'], kite: ['string', 'level', 'height'] };
const big = p => { try { const w = FG.why(p); return w ? X.fig(X.big(w.html.replace(/<p class="vcap">[\s\S]*?<\/p>/, '').replace(/^<div class="vis">|<\/div>$/g, '')), w.cap) : ''; } catch (e) { return ''; } };
const simPic = p => { const x = p.prm, k = E.qk(x.k), val = { p: x.p, q: x.q, r: x.r }, known = ['p', 'q', 'r'].filter(s => s !== x.which)[0], third = ['p', 'q', 'r'].filter(s => s !== x.which && s !== known)[0];
  const B = ['p', 'q', 'r'].map(s => s === x.which ? 'x' : S(qmul(Q(val[s]), k))), col = {}; col[known] = 1; col[x.which] = 2; col[third] = 0;
  return X.fig(X.simPair({ A: { s: [x.p, x.q, x.r], lab: [x.p, x.q, x.r].map(String), nm: x.nm ? x.nm.slice(0, 3) : null }, B: { s: ['p', 'q', 'r'].map(s => E.qnum(qmul(Q(val[s]), k))), lab: B, nm: x.nm ? x.nm.slice(3) : null }, col, turn: x.turn,
    label: 'The two similar triangles, one above the other. Each pair of corresponding sides is drawn in the same color and line style.' }),
    c2('The dashed pair') + ' is x and its corresponding side. ' + c1('The solid pair') + ' is a pair you know both of.'); };
const lightPic = p => { const x = p.prm, sh = x.mode === 'shadow', h1 = +x.h1, s1 = +(sh ? x.s1 : x.d1), s2 = +(sh ? x.s2 : x.d2), k = s2 / s1, w = sh ? 'shadow' : 'distance';
  return X.fig(X.simPair({ A: { s: [h1, Math.hypot(h1, s1), s1], lab: [S(E.qv(x.h1)) + ' ft', '', S(E.qv(sh ? x.s1 : x.d1)) + ' ft'] }, B: { s: [h1 * k, Math.hypot(h1 * k, s2), s2], lab: ['?', '', S(E.qv(sh ? x.s2 : x.d2)) + ' ft'] }, col: { p: 2, r: 1 },
    label: 'Two similar right triangles: the heights drawn dashed, the ' + w + 's drawn solid.' }), c1('The ' + w + 's') + ' match each other, and ' + c2('the heights') + ' match each other.'); };

/* ------------------------------------------------------------------ rendering */
const why = s => s ? ' <span class="xwhy"><b>Why:</b> ' + s + '</span>' : '';
const line = (l, seen) => { const o = Object.assign({}, l, { say: X.teach((l.say || '') + why(l.why && X.whyOf(l.why)) + (l.pic || ''), 'def', seen) }); delete o.why; delete o.pic; return o; };
function stepOut(s, seen) {
  const o = Object.assign({}, s, { ask: X.teach(fix(s.ask), 'def', seen) });
  if (s.opts) o.opts = s.opts.map(p => Object.assign({}, p, { label: X.teach(fix(p.label), 'plain'), why: X.teach(fix(p.why), 'plain') }));
  if (s.hint) o.hint = X.teach(fix(s.hint), 'plain');
  return o;
}
const FIX = [[/^Count on from (\d+) by (\d+)\.$/, 'Add $1 and $2: the tens first, then the ones.'], [/^Across: /, 'Horizontal distance: '], [/^(Up|Down): /, 'Vertical distance: '],
  [/In the converse,/, 'To use the converse,'], [/the side you are finding: it is across from the right angle/, 'the missing side, across from the right angle'],
  [/^Three of the choices begin with ([\d.]+), the match for (\d+)\./, 'Pair shortest with shortest: $1 corresponds to $2.'], [/the order of the letters is the matching, /, 'the letters pair up in order: '], [/, so it matches ([A-Z]{2}), the /, ', so it corresponds to $1, the '], [/^Multiply the matching side by k\./, 'Multiply the corresponding side by k.'], [/^The scale factor from a pair you know:/, 'Find the scale factor from a pair you know both of:'], [/ — a near miss/, ' — close, but not equal'], [/^Subtract the smaller from the larger\.$/, 'Subtract the lower y-coordinate from the higher one.'], [/One is below zero and one above/, 'One is left of zero and one is right of it'],
  [/the copy(?!’)/g, 'the second triangle'], [/The copy(?!’)/g, 'The second triangle'], [/^Then (\d+) becomes/, 'The first triangle’s $1 becomes'], [/Match like with like: a (\w+) with a \w+, a height with a height\./, 'Match $1 with $1 and height with height.'],
  [/stands alone on one side/g, 'is by itself on one side of the equals sign'], [/is the hypotenuse of those two/, 'is the hypotenuse of a right triangle with those two sides as its legs'],
  [/Use the square-root key and keep three decimal places: round once, at the end\./, 'Use the square-root key and write it to three decimal places; round to the tenth only at the very end.'], [/^Never equal to either — that would lie flat\./, 'The third side can never equal the difference or the sum: that would lie flat.'], [/MORE/g, 'more'], [/SHORTER/g, 'shorter'], [/SQUARES/g, 'squares'], [/MULTIPLIED/g, 'multiplied']];
const fix = s => typeof s === 'string' ? FIX.reduce((t, [a, b]) => t.replace(a, b), s) : s;
const withWhy = (old, whys) => old.map((l, i) => Object.assign({}, l, { say: fix(l.say) }, whys[i] ? { why: whys[i] } : {}));

/* ------------------------------------------------------------------ the families */
const SPEC = {};
SPEC.triSet = { mc: true, terms: ['triIneq'], pic: true,
  notice: x => 'Use the [[triIneq]]: the two shorter sides must add to <b>more</b> than the longest side. Exactly equal lies flat; less falls short.' + exampleBars(),
  first: x => ({ say: 'Start with choice A. Put its sides in order, ' + sorted(x.sets[0]).join(', ') + ', and add the two shorter ones.', why: 'only the two shorter sides can fall short. The longest side plus any other is always more than the third.' }),
  sol: (x, old) => x.sets.map((s, i) => { const t = sorted(s), sum = t[0] + t[1];
      return { say: LET[i] + '. In order: ' + t.join(', ') + '. ' + t[0] + ' + ' + t[1] + ' = ' + sum + (sum > t[2] ? ', more than ' + t[2] + ': <b>a triangle</b>.' : sum === t[2] ? ', exactly ' + t[2] + ': it lies flat.' : ', less than ' + t[2] + ': it falls short.') }; })
    .concat([{ say: 'Only ' + LET[x.correct] + ' passes. The answer is ' + LET[x.correct] + '.' + X.fig(bars(x.sets.map((s, i) => [LET[i], s]), 'For each choice: its two shorter sides end to end, over its longest side.'), 'Each pair of bars: the two shorter sides on top, the longest side under them.') }]),
  walk: (x, old) => old.map((s, i) => i === 0 ? Object.assign({}, s, { ask: 'The [[triIneq]] compares the two shorter sides with the longest. For each set, which two sides do you add?' }) : s),
  mcw: (x, k) => { const t = sorted(x.sets[k]), tag = x.tags[k], sum = t[0] + t[1];
    if (tag === 'flat') return 'These lie flat: ' + t[0] + ' + ' + t[1] + ' = ' + sum + ', exactly the longest side. The two shorter sides lie along it and cannot rise to meet. The sum must be <b>more</b> than the longest side.';
    if (tag === 'firstTwo') return 'That adds the first two numbers listed. Order does not matter: add the two <b>shorter</b> sides. Here ' + t[0] + ' + ' + t[1] + ' = ' + sum + ', less than ' + t[2] + ', so they fall short.';
    return 'The two shorter sides add to ' + t[0] + ' + ' + t[1] + ' = ' + sum + ', less than the longest side, ' + t[2] + '. They fall short and cannot meet.'; } };
SPEC.rightSel = { mc: true, terms: ['converse', 'pyth'],
  notice: x => 'Use the [[converse]] of the [[pyth]]: square all three sides. If the two shorter sides’ squares add to exactly the longest side’s square, it is a right triangle.',
  sol: (x, old) => [{ say: 'For each set, the longest side is c. Square the sides and compare a² + b² with c².', why: 'the hypotenuse is always the longest side, wherever it is listed.' }].concat(old.map(l => ({ say: fix(l.say) }))),
  walk: (x, old) => old.map(s => s.opts && s.opts.some(o => /^Yes/.test(o.label)) ? Object.assign({}, s, { keep: true, opts: s.opts.slice().sort((a, b) => /^Yes/.test(a.label) ? -1 : /^Yes/.test(b.label) ? 1 : 0) }) : s) };
SPEC.range = { mc: true, terms: ['triIneq'],
  notice: x => 'By the [[triIneq]], the third side is more than the difference of the other two and less than their sum. Exactly either one would lie flat.',
  sol: (x, old) => { const { a, b } = x.prm; return [{ say: 'It must be longer than the difference: ' + b + ' − ' + a + ' = ' + (b - a) + '.', why: 'the third side plus ' + a + ' must be more than ' + b + '.' },
    { say: 'It must be shorter than the sum: ' + a + ' + ' + b + ' = ' + (a + b) + '.', why: a + ' + ' + b + ' must be more than the third side.' }, { say: fix(old[2].say), why: 'a third side exactly that long would lie flat, so the signs are &lt;, not ≤.' }]; },
  walk: (x, old) => { const { a, b } = x.prm; return old.map((s, i) => i === 0 ? Object.assign({}, s, { ask: 'The third side plus ' + a + ' must be more than ' + b + '. So the third side must be more than ' + b + ' − ' + a + '. What is ' + b + ' − ' + a + '?' })
    : i === 1 ? Object.assign({}, s, { ask: a + ' + ' + b + ' must be more than the third side. What is ' + a + ' + ' + b + '?' }) : s); } };
SPEC.eqChoice = { mc: true, terms: ['hyp', 'pyth'],
  notice: x => 'Find the right angle. The side across from it is the [[hyp]], c, and in the [[pyth]], a² + b² = c², it is by itself.',
  sol: (x, old) => { const f = x.fig, l = f && f.labs; return withWhy(old, [null, 'a² + b² = c² puts the hypotenuse by itself.']).map((s, i) => i === 1 && l ? Object.assign({}, s, { pic: tri(l[0], l[1], l[2], f.legs && f.legs[0], f.legs && f.legs[1], 'The right triangle: legs ' + l[0] + ' and ' + l[1] + ', hypotenuse ' + l[2] + '.', triCap) }) : s); },
  walk: (x, old) => old };
SPEC.simChoice = { mc: true, terms: ['similar', 'scale', 'corr'],
  notice: x => '[[similar|Similar]] triangles have one [[scale]]: every side is multiplied by the same number. Pair the [[corr]], shortest with shortest, and check that all three give the same k.',
  sol: (x, old) => withWhy(old, ['each side of the copy is k times its corresponding side.']), walk: (x, old) => old };

const hypNotice = (pre) => pre + 'You want the [[hyp]]. Use the [[pyth]]: square the two [[leg]], add, then take the [[sqrt]].';
SPEC.hypWhole = { terms: ['leg', 'hyp', 'pyth', 'sqrt'], pic: true,
  notice: p => hypNotice('') + tri('a = ' + p.prm.a, 'b = ' + p.prm.b, 'c = ?', p.prm.a, p.prm.b, 'A right triangle with legs ' + p.prm.a + ' and ' + p.prm.b + ' and an unknown hypotenuse.', triCap),
  sol: (p, old) => withWhy(old, [null, 'the [[pyth]].', 'taking the square root undoes squaring.']), walk: (p, old) => old };
SPEC.legWhole = { terms: ['hyp', 'leg1', 'pyth'], pic: true,
  notice: p => 'Here the [[hyp]], ' + p.prm.c + ', is given, and you want a [[leg1]]. Put the numbers into the [[pyth]], then subtract to get the leg’s square alone.' + tri('a = ' + p.prm.a, 'b = ?', 'c = ' + p.prm.c, p.prm.a, Math.sqrt(p.prm.c * p.prm.c - p.prm.a * p.prm.a), 'A right triangle with hypotenuse ' + p.prm.c + ', one leg ' + p.prm.a + ' and the other leg unknown.', triCap),
  sol: (p, old) => withWhy(old, ['the hypotenuse is across from the right angle.', null, 'subtracting ' + sq(p.prm.a) + ' from both sides gets b² alone.', 'taking the square root undoes squaring.']),
  walk: (p, old) => { const i = old.findIndex(s => /subtract/i.test(s.opts ? s.opts.map(o => o.label).join(' ') : ''));
    return old.slice(0, i + 1).concat([{ type: 'choice', ask: 'Why do you subtract to find a leg?', opts: [O('c² is the sum of the two legs’ squares, so taking one square away leaves the other', true),
      O('Because the numbers are big', false, 'The size of the numbers does not matter. The hypotenuse stands alone in a² + b² = c², so a leg’s square is c² − a².'), O('Subtracting is always used with triangles', false, 'Not always: to find the hypotenuse you add. You subtract only when the hypotenuse is the one you know.')] }], old.slice(i + 1)); } };
SPEC.legTenth = { terms: ['hyp', 'leg', 'pyth', 'tenth'], pic: true,
  notice: p => { const W = STORY[p.prm.ctx] || STORY.ladder; return 'The ' + W[0] + ' is the [[hyp]]: it is across from the right angle. Find the missing one of the two [[leg]] with the [[pyth]] by subtracting, then round to the [[tenth]].' +
    tri('a = ' + p.prm.a + ' (' + W[1] + ')', 'b = ?\n(' + W[2] + ')', 'c = ' + p.prm.c + '\n(' + W[0] + ')', p.prm.a, Math.sqrt(p.prm.c * p.prm.c - p.prm.a * p.prm.a), 'A right triangle: the ' + W[0] + ', ' + p.prm.c + ', is the hypotenuse; ' + p.prm.a + ' and the unknown side are the legs.', triCap); },
  sol: (p, old) => { const { c, a } = p.prm, m = c * c - a * a, r = Math.floor(Math.sqrt(m));
    return [{ say: fix(old[0].say) }, { say: 'Write the Pythagorean Theorem with the numbers: ' + sq(a) + ' + b² = ' + sq(c) + '.' },
      { say: fix(old[1].say).replace(/^Subtract to find the leg squared:/, 'Subtract ' + sq(a) + ' from both sides:'), why: 'subtracting from both sides leaves b² by itself.' },
      { say: fix(old[2].say), why: m + ' is between ' + sq(r) + ' = ' + r * r + ' and ' + sq(r + 1) + ' = ' + (r + 1) * (r + 1) + ', so b is between ' + r + ' and ' + (r + 1) + '.' },
      Object.assign({}, old[3], { say: old[3].say.replace(/the hundredths digit is (\d), so/, (s0, d) => 'the hundredths digit is ' + d + ', which is ' + (+d >= 5 ? '5 or more' : 'less than 5') + ', so') + ' Check: a leg is shorter than the hypotenuse, and ' + S(p.ans) + ' is less than ' + c + '.' })]; },
  walk: (p, old) => { const { c, a } = p.prm; return [old[0], { type: 'choice', ask: 'Which equation fits this triangle?', opts: [O(sq(a) + ' + ' + sq(c) + ' = b²', false, 'That puts the hypotenuse, ' + c + ', with the legs. The hypotenuse stands alone: a² + b² = c².'),
      O(sq(a) + ' + b² = ' + sq(c), true), O(a + ' + b = ' + c, false, 'The theorem is about the squares of the sides.')] },
    { type: 'choice', ask: 'Why do you subtract to find a leg?', opts: [O('c² is the sum of the two legs’ squares, so taking a² away leaves b²', true), O('Because the answer has to be rounded', false, 'Rounding comes at the end. You subtract because the hypotenuse stands alone in a² + b² = c².')] }].concat(old.slice(2)); } };
['hypTenth', 'diag'].forEach(fam => { SPEC[fam] = { terms: ['leg', 'hyp', 'sqrt', 'tenth'], pic: true,
  notice: p => { const a = p.prm.a || p.prm.w, b = p.prm.b || p.prm.l;
    return (fam === 'diag' ? 'A rectangle’s corners are right angles, so the path is the [[hyp]] of a right triangle. ' : 'You want the [[hyp]]. ') + 'Square the [[leg]], add, take the [[sqrt]], then round to the [[tenth]].' +
      tri('a = ' + a, 'b = ' + b, (fam === 'diag' ? 'path = ?' : 'c = ?'), a, b, 'A right triangle with legs ' + a + ' and ' + b + ' and an unknown hypotenuse.', triCap); },
  sol: (p, old) => withWhy(old, ['the [[pyth]]: c² = a² + b².', 'taking the square root undoes squaring.', 'to round to the nearest tenth, look at the hundredths digit: 5 or more rounds up.']), walk: (p, old) => old }; });
SPEC.shorter = { terms: ['hyp'],
  notice: p => '“How much shorter” means subtract: the walk along two sides minus the path straight across. The path is the [[hyp]]. Keep every digit until the end, then round once.',
  sol: (p, old) => { const m = /= ([\d.]+…)/.exec(old[1].say), tot = /= (\d+)/.exec(old[0].say), r = /= ([\d.]+…), the same/.exec(old[2].say);
    return [Object.assign({}, old[0], { say: fix(old[0].say) }), Object.assign({}, old[1], { say: fix(old[1].say).replace(/ — about [\d.]+ to the nearest tenth \(part a\)\./, ' (from the last question).') }),
      Object.assign({}, old[2], { say: m && tot && r ? 'Subtract, keeping every digit: ' + tot[1] + ' − ' + m[1] + ' = ' + r[1] + ' Then round to the nearest tenth.' : fix(old[2].say), why: 'rounding once, at the end, keeps the answer accurate.' })]; }, walk: (p, old) => old };
const gridNotice = (what) => 'Draw a right triangle with the line between the points as its slanted side. Its [[leg]] are the [[horiz]] and the [[vert]]. ' + what;
const gridSol = (p, old) => old.map(l => { const s = fix(l.say).replace(/^(Horizontal distance: .*?)the axis/, '$1the y-axis').replace(/^(Vertical distance: .*?)the axis/, '$1the x-axis'); return Object.assign({}, l, { say: s }, /across zero|crosses zero/.test(s) ? { why: 'one point is on each side of the axis, so the two distances to the axis add.' } : /\(−?\d+ − \(−\d+\)\)/.test(s) ? { why: 'subtracting a negative is the same as adding.' } : /hypotenuse/.test(s) ? { why: 'the [[pyth]].' } : {}); });
SPEC.gridWhole = { terms: ['leg', 'horiz', 'vert', 'hyp'], pic: true, notice: p => gridNotice('The distance is the [[hyp]].'), first: (p, old) => Object.assign({}, old[0], { say: fix(old[0].say) + big(p) }), sol: gridSol, walk: (p, old) => old };
SPEC.coordTenth = { terms: ['leg', 'horiz', 'vert', 'hyp', 'tenth'], pic: true, notice: p => gridNotice('The distance is the [[hyp]], rounded to the [[tenth]].'), first: (p, old) => Object.assign({}, old[0], { say: fix(old[0].say) + big(p) }), sol: gridSol, walk: (p, old) => old };
SPEC.streets = { terms: ['leg', 'horiz', 'vert'], pic: true, notice: p => 'Along the streets, you walk the two [[leg]] of a right triangle: the [[horiz]] plus the [[vert]].', first: (p, old) => Object.assign({}, old[0], { say: fix(old[0].say) + big(p) }), sol: gridSol, walk: (p, old) => old };
SPEC.straight = { terms: ['hyp', 'leg'], pic: true, notice: p => 'The straight line is the [[hyp]] of the right triangle whose [[leg]] are the trips across and up or down.', first: (p, old) => Object.assign({}, old[0], { say: fix(old[0].say) + big(p) }), sol: gridSol, walk: (p, old) => old };
SPEC.crossSide = { terms: ['horiz'], notice: p => { const nm = p.prm.names; return nm[0] + ' and ' + nm[1] + ' have the same y-coordinate, so the side between them is horizontal. Its length is the [[horiz]] between the x-coordinates.'; }, sol: gridSol, walk: (p, old) => old };
SPEC.perim = { terms: ['perimeter', 'hyp'],
  notice: p => 'The [[perimeter]] adds all three sides. The slanted side is the [[hyp]] of a right triangle. Round once, at the end.',
  sol: (p, old) => { const L = old[2], m = /^(.*?) — (round to the nearest tenth.*)$/.exec(L.say);
    return [Object.assign({}, old[0], { say: fix(old[0].say) }), Object.assign({}, old[1], { say: fix(old[1].say), why: 'the [[pyth]].' })].concat(m ? [{ say: m[1].replace(/, and round once, at the end:/, ':') }, Object.assign({}, L, { say: m[2].charAt(0).toUpperCase() + m[2].slice(1), why: 'rounding once, at the end, keeps the answer accurate.' })] : [L]); },
  walk: (p, old) => old };
SPEC.simSide = { terms: ['similar', 'scale', 'corr1'], pic: true,
  notice: p => 'The triangles are [[similar]]: each side of the second is the [[scale]] times its [[corr1]] in the first. Get k from a pair you know, then multiply.',
  first: (p, old) => ({ say: fix(old[0].say) + simPic(p) }),
  sol: (p, old) => { const x = p.prm, k = E.qk(x.k); const L = old.length;
    return [Object.assign({}, old[0], { say: fix(old[0].say) + simPic(p) })].concat(L === 4 ? [] : []).concat([
      Object.assign({}, old[L - 2], { say: fix(old[L - 2].say), why: 'k is second ÷ first, because second = k × first.' }),
      Object.assign({}, old[L - 1], { say: fix(old[L - 1].say) + ' Check: the second triangle is ' + (qlt(k, Q(1)) ? 'smaller, so x is less than ' : 'bigger, so x is more than ') + ({ p: x.p, q: x.q, r: x.r })[x.which] + '.' })]); },
  walk: (p, old) => { const k = E.qk(p.prm.k); return [Object.assign({}, old[0], { ask: old[0].ask + simPic(p) }), old[1],
    { type: 'choice', ask: 'Is k more than 1 or less than 1?', opts: [O(qlt(k, Q(1)) ? 'Less than 1: the second triangle is smaller' : 'More than 1: the second triangle is bigger', true),
      O(qlt(k, Q(1)) ? 'More than 1: similar triangles always grow' : 'Less than 1: k is always a fraction', false, 'k is more than 1 when the copy is bigger and less than 1 when it is smaller.')] }].concat(old.slice(2)); },
  coach: (p, ms) => ms.map(m => Object.assign({}, m, { say: m.say.replace(/^took the triangles to be equal\. .*$/, 'made x the same as its corresponding side. Similar triangles are the same shape, not the same size: every side is multiplied by the scale factor')
    .replace(/^divided by the scale factor\. The copy is (\w+), so multiply by k = (.*)$/, 'divided by the scale factor. The second triangle is $1, so each of its sides is the first triangle’s side times k = $2')
    .replace(/^matched the sides by where they sit on the page\. The copy is ([\w ]+): match them by size, shortest with shortest\.?$/, 'matched sides by where they sit on the page. The second triangle is $1, so the page can mislead: ' + (p.prm.nm ? 'pair the letters in order' : 'match by size, shortest with shortest'))
    .replace('Similar means multiplied, not added.', 'Similar triangles grow by multiplying, not by adding the same amount to each side.') })) };
['shadow', 'mirror'].forEach(fam => { SPEC[fam] = { terms: ['similar', 'scale'], pic: true,
  notice: p => (fam === 'shadow' ? 'The sun hits both at the same angle, so the two right triangles are [[similar]]. ' : 'Light leaves the mirror at the angle it arrives, so the two right triangles are [[similar]]. ') +
    'The [[scale]] is ' + (fam === 'shadow' ? 'shadow ÷ shadow' : 'distance ÷ distance') + ', and the height you want is k times the height you know.' + lightPic(p),
  sol: (p, old) => withWhy(old, ['each has a right angle and one more equal angle, so they are the same shape.', 'matching sides of similar triangles are in the same ratio.', null]), walk: (p, old) => old }; });

/* ------------------------------------------------------------------ apply to the coach */
function help(C, W) {
  const ORIG = {}, seed = (fam, x) => { const s = {}; X.ids(SPEC[fam].notice(x)).forEach(id => { s[id] = 1; }); return s; };
  const firstIds = (fam, x, old) => SPEC[fam].first ? X.ids((SPEC[fam].first(x, old).say || '') + (SPEC[fam].first(x, old).why || '')) : [];
  const outSol = (fam, x, old) => { const seen = seed(fam, x); firstIds(fam, x, old).forEach(id => { seen[id] = 1; }); return SPEC[fam].sol(x, old).map(l => line(l, seen)); };
  const outWalk = (fam, x, old) => { const seen = seed(fam, x); return old ? SPEC[fam].walk(x, old).map(s => stepOut(s, seen)) : old; };
  Object.keys(SPEC).forEach(fam => { const sp = SPEC[fam], f = C.F[fam]; if (!f) return; ORIG[fam] = f;
    C.F[fam] = Object.assign({}, f, { rule: p => X.teach(sp.notice(p).replace(/<figure[\s\S]*<\/figure>/g, ''), 'tap'), sol: p => outSol(fam, p, f.sol(p)), walk: p => outWalk(fam, p, f.walk(p)),
      models: sp.coach ? p => sp.coach(p, f.models(p)).map(m => Object.assign({}, m, { say: X.teach(m.say, 'tap') })) : f.models }); });
  Object.keys(SPEC).filter(f => SPEC[f].mcw).forEach(fam => { C.MCW[fam] = SPEC[fam].mcw; });
  Object.keys(C.MCW).forEach(fam => { const w0 = C.MCW[fam]; C.MCW[fam] = (x, k) => fix(String(w0(x, k))).replace(/It can be shorter than both: anything more than (\d+) reaches\./, (m0, d) => 'It can be shorter than both, or longer than both: anything more than ' + d + ' and less than ' + (x.prm ? x.prm.a + x.prm.b : 'the sum') + ' works.'); });
  Object.keys(C.SELWHY).forEach(fam => { const w0 = C.SELWHY[fam]; C.SELWHY[fam] = (x, i) => fix(String(w0(x, i))); });
  const mcSol = C.mcSolution; C.mcSolution = x => SPEC[x.fam] && SPEC[x.fam].mc ? outSol(x.fam, x, mcSol(x)) : mcSol(x);
  const stMC = W.stepsMC; W.stepsMC = x => SPEC[x.fam] && SPEC[x.fam].mc ? outWalk(x.fam, x, stMC(x)) : stMC(x);
  const ruleOf = x => SPEC[x.fam] ? X.teach(SPEC[x.fam].notice(x).replace(/<figure[\s\S]*<\/figure>/g, ''), 'tap') : '';
  const mcf = C.mcFeedback; C.mcFeedback = (x, k) => { const r = mcf(x, k); if (r && r.v === 'wrong' && SPEC[x.fam]) r.rule = ruleOf(x); return r; };
  const sf = C.selectFeedback; C.selectFeedback = (x, ks, tries) => { const r = sf(x, ks, tries); if (r && r.v === 'wrong' && SPEC[x.fam]) { r.rule = ruleOf(x); r.what = r.what.map(w => String(w).replace(/ Test each one and try again\.$/, ' For each set, check whether the two shorter sides’ squares add to exactly the longest side’s square.')); } return r; };
  const fb = C.feedback; C.feedback = (p, a, ctx) => { const r = fb(p, a, ctx); if (r && r.what) r.what = r.what.map(w => String(w).replace(/Check each step against the rule below, or tap Hint to go one step at a time\./, 'Open Hint, then tap Step by step with me.')); return r; };
  C.rungs = (x, type, ctx) => { const fam = x && x.fam, sp = SPEC[fam]; if (!sp) return null;
    const seen = {}, notice = X.teach(sp.notice(x), 'def', seen);
    if (!sp.first) return { notice };
    const old = sp.mc ? mcSol(x) : ORIG[fam].sol(x);
    return { notice, first: line(sp.first(x, old), seen) }; };
  C.help = { terms: Object.keys(SPEC).reduce((o, f) => (o[f] = SPEC[f].terms, o), {}), pics: Object.keys(SPEC).filter(f => SPEC[f].pic) };
  return C;
}
if (node) module.exports = help; else root.Help = help;
})(this);
