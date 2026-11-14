/* A7 Unit 6 practice: the help, rewritten to the help standard (14 Nov 2026 proofs; Windmill practice/kit/explain.js).
   Three families so far — Q1 triSet (the Triangle Inequality Theorem), Q6 legTenth (a leg of a right triangle, to the
   tenth) and Q15 simSide (a missing side of similar triangles). Hint 1 names the theorem or idea with the decks' words and
   shows it; Hint 2 is the first move and why; Hint 3 is one move per line with its reason; the walkthrough asks one thing
   per step, with the picture in the step it explains, and ends on a self-explanation prompt; the coach names the mistake and
   the idea it broke. The worked lines' values (ex, ans) are the coach's own. Loaded after unit.js. */
(function (root) {
'use strict';
if (typeof module !== 'undefined' && module.exports) return;
const E = root.Practice, C = root.Coach, U = root.Unit, X = root.Kit && root.Kit.X, FG = root.Fig;
if (!E || !C || !U || !X) return;
const { Q, qdiv, qlt, numStr, M, sorted } = E, S = numStr, LET = 'ABCDEFGH', sup2 = '²';
const O = (label, ok, why) => ({ label, ok: !!ok, why: why || '' });
const why = s => '<span class="xwhy"><b>Why:</b> ' + s + '</span>';
const c1 = h => X.c(1, h), c2 = h => X.c(2, h), c3 = h => X.c(3, h);
X.gloss({
  triIneq: { word: 'Triangle Inequality Theorem', def: 'any two sides of a triangle add to more than the third side' },
  leg: { word: 'legs', def: 'the two sides that form the right angle' },
  hyp: { word: 'hypotenuse', def: 'the side across from the right angle; always the longest side' },
  pyth: { word: 'Pythagorean Theorem', def: 'in a right triangle, a² + b² = c²: the legs’ squares add to the hypotenuse’s square' },
  sqrt: { word: 'square root', def: 'the number that, times itself, makes the given number: √81 = 9 because 9 × 9 = 81' },
  similar: { word: 'similar', def: 'the same shape: one triangle is a scale copy of the other, with equal angles' },
  corr: { word: 'corresponding sides', def: 'sides in the same position in the two triangles, the ones that match' },
  scale: { word: 'scale factor', def: 'the number every side is multiplied by to get the copy, k' }
});
const T = X.term;

/* ------------------------------------------------------------------ Q1 triSet */
const triRows = sets => X.tape({ label: 'For each set: the two shorter sides end to end, and the longest side under them.', rows: [].concat(...sets.map(([lab, s]) => { const t = sorted(s);
  const verdict = t[0] + t[1] > t[2] ? '✓' : t[0] + t[1] === t[2] ? '= flat' : '✗';
  return [{ lab, segs: [{ w: t[0], c: 1, t: String(t[0]) }, { w: t[1], c: 2, t: String(t[1]) }], mark: verdict }, { segs: [{ w: t[2], c: 3, t: String(t[2]) }], after: 14 }]; })) });
const exampleRows = () => X.fig(triRows([['', [4, 5, 7]], ['', [3, 4, 7]], ['', [2, 3, 7]]]),
  'Top: ' + c1('4') + ' + ' + c2('5') + ' = 9 is <b>more</b> than ' + c3('7') + ', so the two sides can lift up and meet: a triangle. Middle: 3 + 4 = 7 <b>exactly</b>, so they lie flat on the 7. Bottom: 2 + 3 = 5 is <b>less</b> than 7, so they fall short and cannot meet.');
const MCRULE_tri = () => 'Use the ' + T('triIneq') + ': the two shorter sides must add to <b>more</b> than the longest side. Exactly equal lies flat; less falls short.';
const MCW0 = C.MCW.triSet;
C.MCW.triSet = (x, k) => { const s = x.sets[k], t = sorted(s), tag = x.tags[k], sum = t[0] + t[1];
  if (tag === 'flat') return 'These lie flat: ' + t[0] + ' + ' + t[1] + ' = ' + sum + ', exactly the longest side, ' + t[2] + '. The two shorter sides lie along the longest one and cannot lift up to meet. The sum must be <b>more</b> than the longest side.';
  if (tag === 'firstTwo') return 'That checks the first two numbers listed. The order does not matter: sort the sides and add the two <b>shorter</b> ones. Here ' + t[0] + ' + ' + t[1] + ' = ' + sum + ', less than ' + t[2] + ', so they fall short.';
  return 'The two shorter sides add to ' + t[0] + ' + ' + t[1] + ' = ' + sum + ', less than the longest side, ' + t[2] + '. They fall short and cannot meet, so these lengths make no triangle.'; };
const sol0 = C.mcSolution, steps0 = root.Walk.stepsMC;
const triSol = x => x.sets.map((s, i) => { const t = sorted(s), sum = t[0] + t[1];
    return { say: LET[i] + '. In order: ' + t.join(', ') + '. ' + t[0] + ' + ' + t[1] + ' = ' + sum + (sum > t[2] ? ' &gt; ' + t[2] + ': <b>a triangle</b>.' : sum === t[2] ? ' = ' + t[2] + ': lies flat, no triangle.' : ' &lt; ' + t[2] + ': falls short, no triangle.') }; })
  .concat([{ say: 'Only ' + LET[x.correct] + ' passes, so the answer is ' + LET[x.correct] + '.' + X.fig(triRows(x.sets.map((s, i) => [LET[i], s])), 'Each pair of bars: the two shorter sides on top, the longest side under them.') }]);
const triSteps = x => [
  { type: 'choice', keep: true, ask: 'The ' + T('triIneq') + ' says the two shorter sides must add to more than the longest. For each set, which two sides do you add?' + exampleRows(),
    opts: [O('the longest and one other', false, 'The longest plus anything is always more than the third side, so that test can never fail. It tells you nothing.'),
      O('the two shorter ones', true), O('the first two listed', false, 'The order in the list does not matter. Sort the sides first; only the two shorter ones can fall short.')] }]
  .concat(x.sets.map((s, i) => { const t = sorted(s); return { type: 'num', ask: 'Choice ' + LET[i] + ' (' + x.opts[i] + '). Sorted: ' + t.join(', ') + '. What is ' + t[0] + ' + ' + t[1] + '?', ans: Q(t[0] + t[1]), hint: 'Add the two smallest numbers, ' + t[0] + ' and ' + t[1] + '.' }; }))
  .concat([{ type: 'choice', keep: true, ask: 'Which choice has a sum <b>more than</b> its longest side?', opts: x.sets.map((s, i) => { const t = sorted(s), sum = t[0] + t[1];
      return O(LET[i] + ': ' + sum + (sum > t[2] ? ' &gt; ' : sum === t[2] ? ' = ' : ' &lt; ') + t[2], i === x.correct, i === x.correct ? '' : sum === t[2] ? 'Equal is not enough: ' + sum + ' = ' + t[2] + ' lies flat.' : sum + ' is less than ' + t[2] + ': it falls short.'); }) },
    { type: 'choice', ask: 'Why is a sum <em>equal</em> to the longest side not enough?', opts: [O('The two sides would lie flat along the longest one, with no room to rise to a corner', true),
      O('Because equal numbers are not allowed in a triangle', false, 'Equal sides are fine (a triangle can have two equal sides). The problem is that the two shorter sides would lie flat.'),
      O('It is enough: equal works', false, 'Try it with sticks: 3 + 4 laid on a 7 lies flat. There is no corner at the top, so no triangle.')] }]);

/* ------------------------------------------------------------------ Q6 legTenth */
const STORY = { ladder: { c: 'the ladder', a: 'the ground to the wall', b: 'height up the wall', cS: 'ladder', aS: 'ground', bS: 'wall' },
  ramp: { c: 'the ramp', a: 'along the ground', b: 'how high it rises', cS: 'ramp', aS: 'ground', bS: 'rise' },
  kite: { c: 'the string', a: 'level from the hand', b: 'height of the kite', cS: 'string', aS: 'level', bS: 'height' } };
const leg0 = C.F.legTenth;
const legPic = (p, showB) => { const { c, a, ctx } = p.prm, W = STORY[ctx] || STORY.ladder;
  return X.rightTri({ a: { t: 'leg a = ' + a + ' (' + W.aS + ')', c: 2 }, b: { t: (showB ? 'leg b = ?' : 'leg b') + ' (' + W.bS + ')', c: 2 }, c: { t: 'hypotenuse c = ' + c + ' (' + W.cS + ')', c: 1 }, la: a, lb: Math.sqrt(c * c - a * a),
    label: 'A right triangle: the ' + W.cS + ', ' + c + ', is the hypotenuse across from the right angle; ' + a + ' and the unknown side are the legs.' }); };
const legFig = (p, cap) => X.fig(legPic(p, true), cap);
C.F.legTenth = Object.assign({}, leg0, {
  rule: p => { const W = STORY[p.prm.ctx] || STORY.ladder; return 'Name the sides first. The ' + T('hyp') + ' is across from the right angle, so it is ' + W.c + '. The other two sides are the ' + T('leg') + '. You want a leg, so put the numbers into the ' + T('pyth') + ' and subtract.'; },
  models: p => { const { c, a } = p.prm, old = leg0.models(p), sq = v => v + sup2;
    const say = ['added the squares: ' + sq(a) + ' + ' + sq(c) + '. That finds a side longer than the hypotenuse, ' + c + ' — but you want a leg, which is shorter. Subtract: ' + sq(c) + ' − ' + sq(a),
      'subtracted the lengths, ' + c + ' − ' + a + '. The Pythagorean Theorem is about the squares of the sides: ' + sq(c) + ' − ' + sq(a),
      'stopped at ' + (c * c - a * a) + '. That is b' + sup2 + ', the leg squared. Take its square root to get b'];
    const cut = s0 => { const d = /next digit is (\d), so round up to ([\d.]+)/.exec(s0); return d ? 'cut off the extra digits instead of rounding. To round to the nearest tenth, look at the hundredths digit: it is ' + d[1] + ', which is 5 or more, so the tenths digit goes up, to ' + d[2] : s0; };
    return old.map((m, i) => Object.assign({}, m, { say: say[i] || (/^cut the decimal off/.test(m.say) ? cut(m.say) : m.say) })); },
  sol: p => { const { c, a } = p.prm, m = c * c - a * a, old = leg0.sol(p), W = STORY[p.prm.ctx] || STORY.ladder;
    return [
      { say: 'Name the sides. ' + c1('Hypotenuse c = ' + c) + ' (' + W.c + ', across from the right angle). ' + c2('Leg a = ' + a) + '. ' + c2('Leg b') + ' is the ' + W.b + ', the one you want.' + X.fig(legPic(p, true), '') },
      { say: 'Write the ' + T('pyth') + ' with the numbers: ' + M(a + sup2 + ' + b' + sup2 + ' = ' + c + sup2) + '.' },
      { say: 'Get b' + sup2 + ' alone: subtract ' + a + sup2 + ' from both sides. ' + M('b' + sup2 + ' = ' + (c * c) + ' − ' + (a * a) + ' = ' + m) + '.' },
      { say: 'Take the ' + T('sqrt') + ': b = √' + m + ' = ' + old[2].say.split(/[,=] /).pop() + ' ' + why(m + ' is between ' + Math.floor(Math.sqrt(m)) + sup2 + ' = ' + Math.floor(Math.sqrt(m)) ** 2 + ' and ' + (Math.floor(Math.sqrt(m)) + 1) + sup2 + ' = ' + (Math.floor(Math.sqrt(m)) + 1) ** 2 + ', so b is between ' + Math.floor(Math.sqrt(m)) + ' and ' + (Math.floor(Math.sqrt(m)) + 1) + '.') },
      Object.assign({}, old[3], { say: old[3].say.replace(/the hundredths digit is (\d), so/, (s0, d) => 'look at the hundredths digit, ' + d + '. It is ' + (+d >= 5 ? '5 or more' : 'less than 5') + ', so') + ' The leg is shorter than the hypotenuse, as it must be.' })]; },
  walk: p => { const { c, a } = p.prm, m = c * c - a * a, old = leg0.walk(p), W = STORY[p.prm.ctx] || STORY.ladder;
    return [
      { type: 'choice', ask: 'The right angle is where the ' + W.aS + ' meets the ' + W.bS + '. Which length is the ' + T('hyp') + ', across from it?' + X.fig(legPic(p, true), ''),
        opts: [O(W.c + ', ' + c, true), O(W.a + ', ' + a, false, 'That side touches the right angle, so it is a leg. The hypotenuse is the side that does not touch the right angle.')] },
      { type: 'choice', ask: 'Which equation fits this triangle?', opts: [O(M(a + sup2 + ' + ' + c + sup2 + ' = b' + sup2), false, 'That puts the hypotenuse, ' + c + ', with the legs. The hypotenuse stands alone: a' + sup2 + ' + b' + sup2 + ' = c' + sup2 + '.'),
        O(M(a + sup2 + ' + b' + sup2 + ' = ' + c + sup2), true), O(M(a + ' + b = ' + c), false, 'The theorem is about the squares of the sides, not the sides themselves.')] },
      Object.assign({}, old[2], { ask: 'Get b' + sup2 + ' alone by subtracting. What is ' + c + sup2 + ' − ' + a + sup2 + '?' }),
      Object.assign({}, old[3], { ask: 'b' + sup2 + ' = ' + m + '. What is √' + m + ', rounded to the nearest tenth?' }),
      { type: 'choice', ask: 'Does your answer make sense?', opts: [O('Yes: the leg is shorter than the hypotenuse, ' + c, true),
        O('No: a leg should be longer than the hypotenuse', false, 'The hypotenuse is always the longest side, so a leg is always shorter than it.')] }]; }
});

/* ------------------------------------------------------------------ Q15 simSide */
const sim0 = C.F.simSide;
const simOf = p => { const { p: a, q: b, r: c, which } = p.prm, k = E.qk(p.prm.k), val = { p: a, q: b, r: c }, known = ['p', 'q', 'r'].filter(s => s !== which), o1 = val[known[0]];
  return { a, b, c, which, k, val, known, o1, c1: E.qmul(Q(o1), k), side: val[which], nm: p.prm.nm }; };
const segName = (nm, off, s) => { const e = { p: [0, 2], q: [1, 2], r: [0, 1] }[s]; return nm ? nm[off + e[0]] + nm[off + e[1]] : ''; };
const simPic = (p, cap) => { const f = p._fig; if (!f || !FG || !FG.figModel) return '';
  const B = FG.figModel(f), A = B.meta.A, Cc = B.meta.C, t = simOf(p), e = { p: [0, 2], q: [1, 2], r: [0, 1] };
  const third = ['p', 'q', 'r'].filter(s => s !== t.which && s !== t.known[0])[0];
  [[t.known[0], 'xs1'], [t.which, 'xs2'], [third, 'xs3']].forEach(([s, cls]) => { B.line(A[e[s][0]], A[e[s][1]], cls); B.line(Cc[e[s][0]], Cc[e[s][1]], cls); });
  return X.fig(B.svg('why', 'The two triangles with each pair of corresponding sides drawn in the same color and line style.'), cap); };
const kStr = k => E.kOut ? E.kOut(k) : S(k);
C.F.simSide = Object.assign({}, sim0, {
  rule: p => 'The triangles are ' + T('similar') + ': every side of the second is the same number, the ' + T('scale') + ', times its ' + T('corr') + ' in the first. Find which sides correspond, get k from a pair you know, then multiply.',
  models: p => { const t = simOf(p), old = sim0.models(p);
    const say = ['made x the same as its corresponding side, ' + t.side + '. Similar triangles are the same shape, not the same size: every side is multiplied by the scale factor',
      'divided by the scale factor. The second triangle is ' + (qlt(t.k, Q(1)) ? 'smaller' : 'bigger') + ', so each of its sides is the first triangle’s side <b>times</b> k = ' + kStr(t.k)];
    const pos = 'matched sides by where they sit on the page. The second triangle is ' + (p.prm.turn === 'flip' ? 'flipped over' : 'turned') + ', so the page can mislead: ' + (t.nm ? 'pair the letters in order' : 'match by size, shortest with shortest') + ' to find corresponding sides';
    return old.map((m, i) => Object.assign({}, m, { say: say[i] || (/^matched the sides by where/.test(m.say) ? pos : m.say.replace('Similar means multiplied, not added.', 'Similar triangles grow by multiplying, not by adding the same amount to each side.')) })); },
  sol: p => { const t = simOf(p), old = sim0.sol(p), n = t.nm, xOn = segName(n, 3, t.which), xM = segName(n, 0, t.which), kOn = segName(n, 0, t.known[0]), kOnC = segName(n, 3, t.known[0]);
    const match = n ? 'Find the ' + T('corr') + '. The letters pair up in order: ' + n[0] + '↔' + n[3] + ', ' + n[1] + '↔' + n[4] + ', ' + n[2] + '↔' + n[5] + '. So x, on ' + c2(xOn) + ', corresponds to ' + c2(xM + ' = ' + t.side) + '.'
      : 'Find the ' + T('corr') + ' by size: x is on the second triangle’s ' + { p: 'shortest', q: 'middle', r: 'longest' }[t.which] + ' side, so it corresponds to the first triangle’s ' + { p: 'shortest', q: 'middle', r: 'longest' }[t.which] + ' side, ' + c2(String(t.side)) + '.';
    return [{ say: match + simPic(p, '') },
      { say: 'Find the ' + T('scale') + ' from a pair you know both of: ' + c1(S(t.c1)) + ' corresponds to ' + c1(String(t.o1)) + (n ? ' (' + kOnC + ' and ' + kOn + ')' : '') + ', so ' + M('k = ' + S(t.c1) + ' ÷ ' + t.o1 + ' = ' + kStr(t.k)) + '. ' + why('k is second ÷ first, because second = k × first.') },
      Object.assign({}, old[old.length - 1], { say: 'Multiply the corresponding side by k: x = ' + t.side + ' × ' + kStr(t.k) + '. ' + why('the second triangle is ' + (qlt(t.k, Q(1)) ? 'smaller, so x is less than ' : 'bigger, so x is more than ') + t.side + '.') })]; },
  walk: p => { const t = simOf(p), old = sim0.walk(p), n = t.nm, xOn = segName(n, 3, t.which);
    return [Object.assign({}, old[0], { ask: (n ? 'x is on ' + xOn + '. In “' + n.slice(0, 3).join('') + ' is similar to ' + n.slice(3).join('') + '” the letters pair up in order. Which side of the first triangle is the ' + T('corr', 'corresponding side') + ' to x?'
        : 'Which side of the first triangle is the ' + T('corr', 'corresponding side') + ' to x? Match by size: shortest with shortest, longest with longest.') + simPic(p, c2('The dashed pair') + ' is x and its corresponding side. ' + c1('The solid pair') + ' you know both of.') }),
      Object.assign({}, old[1], { ask: 'Use the pair you know both of. What is the scale factor, k = ' + S(t.c1) + ' ÷ ' + t.o1 + '?' }),
      { type: 'choice', ask: 'Is k more than 1 or less than 1, and why?', opts: [O(qlt(t.k, Q(1)) ? 'Less than 1: the second triangle is smaller' : 'More than 1: the second triangle is bigger', true),
        O(qlt(t.k, Q(1)) ? 'More than 1: similar triangles always grow' : 'Less than 1: k is always a fraction', false, 'k can be more or less than 1. It is more than 1 when the copy is bigger and less than 1 when it is smaller.')] },
      Object.assign({}, old[2], { ask: 'x corresponds to ' + t.side + '. What is ' + t.side + ' × ' + kStr(t.k) + '?' })]; }
});

/* ------------------------------------------------------------------ the page's hooks */
const gen0 = U.generate;
U.generate = seed => { const g = gen0(seed); g.sections.forEach(s => s.items.forEach(it => { if (it.type === 'solo' && it.part && it.part.fam === 'simSide' && it.fig) it.part._fig = it.fig; })); return g; };
const FIRST = {
  triSet: x => ({ say: 'Start with choice A. Sort its sides: ' + sorted(x.sets[0]).join(', ') + '. Add the two shorter ones and compare the sum with the longest. ' + why('only the two shorter sides can fall short.') }),
  legTenth: p => { const { c, a } = p.prm; return { say: 'Write the ' + T('pyth') + ' with the numbers: the hypotenuse, ' + c + ', stands alone, so ' + M(a + sup2 + ' + b' + sup2 + ' = ' + c + sup2) + '.' }; },
  simSide: p => C.F.simSide.sol(p)[0]
};
const NOTICE = { triSet: x => MCRULE_tri() + exampleRows(), legTenth: p => C.F.legTenth.rule(p) + legFig(p, c1('The hypotenuse') + ' is across from the right angle. ' + c2('The legs') + ' form the right angle.'),
  simSide: p => C.F.simSide.rule(p) };
const rungs0 = U.rungs;
U.rungs = (x, type, ctx) => { const f = x && x.fam; if (FIRST[f]) return { notice: NOTICE[f](x), first: FIRST[f](x), steps: f === 'triSet' ? triSol(x) : undefined }; return rungs0 ? rungs0(x, type, ctx) : null; };
const walk0 = U.walk;
U.walk = (x, type, ctx) => x && x.fam === 'triSet' ? triSteps(x) : walk0(x, type, ctx);
const sol1 = U.solution;
U.solution = (x, type, ctx) => x && x.fam === 'triSet' ? triSol(x) : sol1(x, type, ctx);
const mc0 = U.judge.mc;
U.judge.mc = (x, k) => { const r = mc0(x, k); if (r && x.fam === 'triSet' && r.v === 'wrong') r.rule = MCRULE_tri(); return r; };
const text0 = U.judge.text;
U.judge.text = (p, a, ctx) => { const r = text0(p, a, ctx);
  if (r && FIRST[p.fam] && r.what) r.what = r.what.map(w => String(w).replace(/Check each step against the rule below, or tap Hint to go one step at a time\./, 'Open Hint, then tap Step by step with me.'));
  return r; };
})(this);
