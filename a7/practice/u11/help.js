/* A7 Unit 11 practice: the help's words and pictures, to the help standard (Windmill practice/kit/HELP_STANDARD.md, 14 Nov 2026).
   coach.js calls this at its end — help(api, walkApi) — so the unit's checks read exactly what a student reads. For each family:
     notice  Hint 1: the kind of problem and its one idea, in the decks' words (a7/build/u11/l01–l08.py: like terms, coefficient,
             constant, the distributive property, variable term, the subtraction property of equality, no solution, infinitely
             many solutions, system of equations, solution of a system, intersect, point of intersection, parallel lines, the
             same line, table of values, coefficient of x, approximate solution); every term tappable, its definition shown
             only on a tap (Croix, 14 Nov 2026: "Don't spell it out first"); two or three sentences, then a picture
     first   Hint 2: the first move and its Why:, with the picture of that move
     sol     Hint 3: one move a line — Do, Why:, the line that results — ending with a check; the mathematics of every line (ex)
             is the coach's own (coach.js steps()), so every line stays proved by the unit's checks
     walk    Step by step with me: one question a step, the right option not always first, every wrong option's reason naming
             its misconception; a "why" question only on the unit's key idea, the Distributive Property — the number in front
             multiplies EVERY term inside (Croix, 14 Nov 2026: "they are terrible at distributing. So let's do distribute") —
             placed right after the distributing it explains
     coach   the named mistakes, reworded to name the move and the idea it broke ("That is what you get if you …").
   Parentheses: distribute first, always (Croix, 14 Nov 2026); never divide first. No "slope", no "y-intercept" (the class has
   not met them); no substitution or elimination: a line comes from a table of values, a system is solved by graphing.
   Multiplication is parentheses or a dot, never ×. */
(function (root) {
'use strict';
const node = typeof module !== 'undefined' && module.exports;
const E = node ? require('./engine.js') : root.Practice;
const X = node ? require('../kit/explain.js') : root.Kit.X;
const FG = node ? require('./fig.js') : root.Fig;
const { Q, qadd, qsub, qmul, qdiv, qneg, qabs, qeq, qlt, qnum, qsign, isInt, numStr, nHtml, M, vi, T_, sideH, sideT, eqH, lineH, lineT, lineSide, yAt, onLine, substT, pairT, pairH, ZERO, ONE } = E;
const n = numStr, LET = 'ABCDE';
const c1 = h => X.c(1, h), c2 = h => X.c(2, h), c3 = h => X.c(3, h);
const tT = (c, v) => sideT([T_(c, v || null)]);                         /* a term as text: 16v, −7v, v, −16 */
const tH = (c, v) => sideH([T_(c, v || null)]);
const sgn = q => (qsign(q) < 0 ? '− ' : '+ ') + n(qabs(q));            /* + 10, − 16: a constant with its sign */
const signed = (c, v) => (qsign(c) < 0 ? '' : '+') + tT(c, v);          /* a chip just put on a pan: +16, −3v */
const ch = (label, ok, why) => ({ label, ok: !!ok, why: why || '' });
const choice = (ask, opts, extra) => Object.assign({ type: 'choice', ask, opts, then: null }, extra || {});
let C0 = null;

/* the glossary: its words and their cards are below the pictures they draw ("the glossary and its cards") */

/* ------------------------------------------------------------------ rendering */
const why = s => s ? ' <span class="xwhy"><b>Why:</b> ' + s + '</span>' : '';
const line = l => { const o = Object.assign({}, l, { say: X.teach(fix(l.say || '') + why(l.why) + (l.pic || ''), 'def') }); delete o.why; delete o.pic; return o; };
function stepOut(s) {
  const o = Object.assign({}, s, { ask: X.teach(fix(s.ask), 'def') });
  if (s.opts) o.opts = s.opts.map(p => Object.assign({}, p, { label: X.teach(fix(p.label), 'plain'), why: X.teach(fix(p.why), 'plain') }));
  if (s.hint) o.hint = X.teach(fix(s.hint), 'plain');
  return o;
}
const noFig = h => String(h).replace(/<figure[\s\S]*?<\/figure>/g, '');
/* the coach's own words, brought to the lessons' vocabulary (a choice's reason, a Hint step's question) */
const FIX = [[/\bthe letter\b/g, 'the variable'], [/\bThe letter\b/g, 'The variable'], [/\bletter\b/g, 'variable'], [/ sentence\b/g, ' statement'],
  [/numbers multiplying x/g, 'coefficients of x'], [/[Tt]he same number multiplies x/g, m => (m[0] === 'T' ? 'T' : 't') + 'he same coefficient of x is in both'], [/ — or it is no longer the same equation\./, '. Otherwise it is no longer the same equation.'],
  [/^(Yes|No) — the (first|second) is (true|false)$/, '$1: the $2 equation is $3'], [/^Compare (\S+) with (\S+)\.$/, 'The equation gives $1, and the pair’s y is $2.'],
  [/^(Yes|No) — they /, '$1: they '], [/^What number multiplies x in each equation/, 'What is the coefficient of x in each equation'], [/^The same number in both$/, 'The same coefficient in both'], [/^Different numbers$/, 'Different coefficients'],
  [/^The same number, (\S+), multiplies x in both, and/, 'The coefficient of x is $1 in both equations, and'], [/the same number, (\S+), multiplies x in both/g, 'the coefficient of x is $1 in both']];
const fix = s => typeof s === 'string' ? FIX.reduce((t, [a, b]) => t.replace(a, b), s) : s;

/* ------------------------------------------------------------------ pictures */
const chips = (side, v) => side.filter(c => c.k === 't').map(c => ({ t: tT(c.c, c.v), c: c.v ? 1 : 0 }));
/* an equation as a balance (11.02 Notes I: "a balance stays level only if both pans lose the same thing") */
function balanceOf(e, cap) {
  const lab = 'A balance: ' + sideT(e.L) + ' on the left pan has the same value as ' + sideT(e.R) + ' on the right pan.';
  return X.fig(X.balance({ left: chips(e.L), right: chips(e.R), label: lab, tag: 'equal' }), cap || 'An equation is a balance: both sides have the same value. ' + c1('The variable terms') + ' are drawn in color.');
}
/* the move done to both sides: the same chip put on each pan (dashed), and the pair that makes 0 struck out */
function balanceMove(pre, add, av) {
  const pan = side => { const cs = chips(side); let hit = -1;
    side.filter(c => c.k === 't').forEach((c, i) => { if (hit < 0 && !!c.v === !!av && qeq(c.c, qneg(add))) hit = i; });
    if (hit >= 0) cs[hit] = Object.assign({}, cs[hit], { c: 2, gone: true });
    return { cs: cs.concat([{ t: signed(add, av), c: 2, add: true, gone: hit >= 0 }]), hit: hit >= 0 }; };
  const L = pan(pre.L), R = pan(pre.R), was = tT(qneg(add), av), side = L.hit ? 'left' : 'right';
  const lab = 'The same ' + signed(add, av) + ' goes on both pans of the balance. On the ' + side + ', ' + was + ' and ' + signed(add, av) + ' make 0, so both sides stay equal.';
  return X.fig(X.balance({ left: L.cs, right: R.cs, label: lab, tag: 'still equal' }),
    qsign(add) < 0 ? 'Take ' + c2(tT(qabs(add), av)) + ' off both pans, so they stay equal. On the ' + side + ', the ' + c2(was) + ' is gone, struck out.'
      : 'Put ' + c2(signed(add, av)) + ' on both pans, so they stay equal. On the ' + side + ', ' + c2(was) + ' and ' + c2(signed(add, av)) + ' make 0.');
}
const facT = g => g.fr && !isInt(g.f) ? E.fracT(g.f) : n(g.f);            /* ⅔, −0.5, 4 */
const prodT = (g, t) => { const F0 = facT(g); return (qsign(g.f) < 0 ? '(' + F0 + ')' : F0) + '(' + tT(t.c, t.v) + ') = ' + tT(qmul(g.f, t.c), t.v); };
/* the Distributive Property: an arrow from the number in front to each term inside, and (Hint 2) each product */
function arrows(gs, withProd) {
  const pics = gs.map(g => ({ f: facT(g), t: g.t.map(t => tT(t.c, t.v)), p: withProd ? g.t.map(t => tT(qmul(g.f, t.c), t.v)) : null }));
  const g0 = gs[0], lab = gs.map(g => 'An arrow from the ' + facT(g) + ' to each term inside its parentheses, ' + g.t.map(t => tT(t.c, t.v)).join(' and ') + (withProd ? ', and each product under its term: ' + g.t.map(t => tT(qmul(g.f, t.c), t.v)).join(' and ') : '') + '.').join(' ');
  const cap = withProd ? gs.map(g => c1(prodT(g, g.t[0])) + ' and ' + c2(prodT(g, g.t[1]))).join('; ') + '.'
    : 'Each arrow is one multiplication: ' + (gs.length > 1 ? 'every number in front reaches ' + c1('the first term') + ' and ' + c2('the second term') + ' inside.' : 'the ' + facT(g0) + ' reaches ' + c1(tT(g0.t[0].c, g0.t[0].v)) + ' and ' + c2(tT(g0.t[1].c, g0.t[1].v)) + '.');
  return X.fig(FG.arrowsPic(pics, lab), cap);
}
const groupsOf = e => e.L.concat(e.R).filter(c => c.k === 'g');
/* the question's own graph, redrawn for the help with what it points at */
function planePic(o, cap) { return X.fig(FG.helpPlane(o), cap); }
const three = () => X.fig(FG.threePic(), 'Left to right: lines that cross once, ' + c1('one solution') + '; ' + c2('parallel lines') + ', no solution; ' + c3('the same line') + ', infinitely many solutions.');
function winAround(pts, pad) {                                          /* a window around the points and the origin; a grid line every 1 across, every 1, 2 or 5 up */
  const xs = pts.map(p => qnum(p[0])).concat([0]), ys = pts.map(p => qnum(p[1])).concat([0]);
  const lo = Math.min(...ys), hi = Math.max(...ys), sp = hi - lo + 2 * pad, st = sp > 28 ? 5 : sp > 14 ? 2 : 1;
  return { x0: Math.floor(Math.min(...xs)) - pad, x1: Math.ceil(Math.max(...xs)) + pad, y0: st * Math.floor((lo - pad) / st), y1: st * Math.ceil((hi + pad) / st), ys: st };
}

/* ------------------------------------------------------------------ the glossary and its cards (27 Nov 2026)
   A term in the help opens its card (kit explain.js X.card; Croix, 27 Nov 2026: "I would like a card to pop up that's the
   definition and everything else in depth about the word"): def is the lead line (the help's own since 14 Nov), more says what
   it means, sym the rule in symbols, ex one worked example, watch the common mistake, see the related words. Every card says
   what the decks say (a7/build/u11/l01–l08.py, their vocabulary and notes; unit.py's Reference Sheet), with small numbers of its
   own: no lesson's, the paper's or the test's, and none of a question on the page (the card is the same wherever it opens).
   cards_check.js proves every example's arithmetic and scans the page's sets for its numbers. No × anywhere, no "slope". */
const kx = s => String(s).replace(/\{([^{}]+)\/([^{}]+)\}|([a-z])|-|\*/g, (m0, a, b, v) => a !== undefined ? E.fr(kx(a), kx(b)) : v ? vi(v) : m0 === '-' ? '−' : '·');
const km = s => M(kx(s));                                               /* a piece of math, as the help writes it: 2x − 3 */
const kl = s => '<span class="xcl">' + km(s) + '</span>';                /* a line of math on its own */
const kp = s => '<p>' + s + '</p>';
const kw = (a, b) => b ? '<ul><li>' + a + '</li><li>' + b + '</li></ul>' : a;   /* a Watch out: one item, or two as a list (HELP_STANDARD §3, 27 Nov 2026) */
const Ln = (m, b) => ({ m: E.qv(m), b: E.qv(b) });
const kPlane = (lines, mk, win, label, cap, more) => planePic(Object.assign({ w: win, lines, mark: mk && { x: Q(mk[0]), y: Q(mk[1]), t: pairT(Q(mk[0]), Q(mk[1])) }, label }, more || {}), cap);
X.gloss({
  likeTerms: { word: 'like terms', def: 'terms with the same variable part, like 3x and 5x',
    more: 'Like terms have the same letter to the same power. Collect them by adding their coefficients: three x’s and five more x’s are eight x’s. A constant is like another constant, but never like a variable term.',
    sym: km('ax + bx = (a + b)x'),
    ex: kl('6n + 5 - 2n = 4n + 5') + kp(km('6n') + ' and ' + km('-2n') + ' are like terms: ' + km('6 - 2 = 4') + '. The 5 is a constant, so it stays as it is.'),
    watch: kw('Use the sign in front of each term when you combine like terms. ' + km('5x - 2x = 3x') + ', not ' + km('7x') + ', because ' + km('5 - 2 = 3') + '.',
      'Combine only like terms. ' + km('4x + 3') + ' stays ' + km('4x + 3') + ', not ' + km('7x') + ', because 3 has no ' + vi('x') + '.'),
    see: ['coef', 'constant', 'varTerm'] },
  likeTerm: { word: 'like term', def: 'a term with the same variable part, like 3x and 5x', card: 'likeTerms' },
  coef: { word: 'coefficient', def: 'the number that multiplies the variable: 3 in 3x', say: 'koh-uh-FISH-uhnt',
    more: 'In a term like ' + km('3x') + ', the 3 is the coefficient: ' + km('3x') + ' means 3 times ' + vi('x') + '. A minus sign belongs to it, so the coefficient of ' + km('-4y') + ' is −4. A variable on its own, like ' + vi('x') + ', has a coefficient of 1.',
    ex: kl('-3y = 12') + kl('y = -4') + kp('The coefficient of ' + vi('y') + ' is −3, so divide both sides by −3, sign and all: ' + km('12 ÷ (-3) = -4') + '.'),
    watch: 'Divide both sides by the whole coefficient, including its minus sign. ' + km('-3y = 12') + ' gives ' + km('y = -4') + ', not ' + km('y = 4') + ', because ' + km('12 ÷ (-3) = -4') + '.',
    see: ['variable', 'constant', 'coefX'] },
  constant: { word: 'constant', def: 'a term with no variable, like the 4 in 8x + 4',
    more: 'A constant is a number on its own. Its value never changes, whatever number the variable is. Constants are like terms of each other, so they can be added.',
    ex: kl('3x + 6 - 1 = 3x + 5') + kp('The 6 and the −1 are constants, so they combine: ' + km('6 - 1 = 5') + '. The ' + km('3x') + ' has a variable, so it is not a constant.'),
    watch: kw('Find the term that has no variable. In ' + km('3x + 7') + ', the constant is 7, not 3.',
      'Write a constant with its sign. In ' + km('2x - 9') + ', the constant is ' + km('-9') + ', not 9.'),
    see: ['coef', 'likeTerms', 'varTerm'] },
  variable: { word: 'variable', def: 'the letter that stands for the unknown number',
    more: 'A variable holds the place of a number you do not know yet. Any letter can be one: ' + vi('x') + ', ' + vi('n') + ', ' + vi('w') + ' or ' + vi('k') + '. To solve an equation is to find the number the variable stands for.',
    ex: kl('w + 4 = 10') + kl('w = 6') + kp(vi('w') + ' is the variable. It stands for 6, because ' + km('6 + 4 = 10') + '.'),
    watch: 'Multiply when a number is written next to a variable. If ' + km('x = 5') + ', then ' + km('3x = 3(5) = 15') + ', not 35.',
    see: ['coef', 'solution', 'varTerm'] },
  distProp: { word: 'Distributive Property', def: 'the number outside the parentheses multiplies every term inside', say: 'dih-STRIB-yuh-tiv',
    more: 'Distribute means hand out to everyone. The number in front of the parentheses multiplies each term inside, sign and all. Then the parentheses are gone, and you can collect like terms and solve.',
    sym: km('a(b + c) = ab + ac'),
    ex: kl('4(x + 3) = 4x + 12') + X.fig(FG.arrowsPic([{ f: '4', t: ['x', '3'], p: ['4x', '12'] }], 'An arrow from the 4 to each term inside the parentheses, x and 3, and each product under its term: 4x and 12.'),
      'Each arrow is one multiplication: ' + c1(km('4(x) = 4x')) + ' and ' + c2(km('4(3) = 12')) + '.'),
    watch: kw('Multiply every term inside, not just the first one. ' + km('4(x + 3) = 4x + 12') + ', not ' + km('4x + 3') + '.',                       /* the lead's words, 27 Nov 2026 */
      'If the number in front is negative, multiply each term by that negative number. ' + km('-2(y - 5) = -2y + 10') + ', because ' + km('-2 * (-5) = +10') + '.'),
    see: ['likeTerms', 'coef', 'constant'] },
  varTerm: { word: 'variable term', def: 'a term with a variable in it, like 5x',
    more: 'A variable term is a coefficient times a variable, like ' + km('5x') + ' or ' + km('-3x') + '. When an equation has a variable term on each side, take the same variable term from both sides. Then the variable is on one side only.',
    ex: kl('7x + 2 = 3x + 14') + kl('4x + 2 = 14') + kp(km('7x') + ' and ' + km('3x') + ' are the variable terms. Subtract ' + km('3x') + ', the smaller one, from both sides.'),
    watch: 'Subtract the smaller variable term from both sides. ' + km('7x + 2 = 3x + 14') + ' becomes ' + km('4x + 2 = 14') + ', not ' + km('10x + 2 = 14') + ', because ' + km('7x - 3x = 4x') + '.',
    see: ['likeTerms', 'subProp', 'coef'] },
  addProp: { word: 'Addition Property of Equality', def: 'add the same thing to both sides and they stay equal',
    more: 'An equation is like a balance: both sides have the same value. Add the same number, or the same term, to both sides, and they stay equal. Use it to undo a subtraction.',
    ex: kl('y - 6 = 2') + kl('y = 8') + balanceMove({ L: [T_(1, 'y'), T_(-6)], R: [T_(2)], v: 'y' }, Q(6), null) + kp('Add 6 to both sides. The −6 and +6 make 0, and ' + km('2 + 6 = 8') + '.'),
    watch: 'Add the same number to both sides. ' + km('y - 6 = 2') + ' becomes ' + km('y = 8') + ', not ' + km('y = 2') + ', because ' + km('2 + 6 = 8') + '.',
    see: ['subProp', 'divProp', 'solution'] },
  subProp: { word: 'Subtraction Property of Equality', def: 'subtract the same thing from both sides and they stay equal',
    more: 'Subtract the same number, or the same term, from both sides, and they stay equal. Use it to undo an addition, or to take the same variable term from both sides.',
    ex: kl('5x + 1 = 2x + 7') + kl('3x + 1 = 7') + balanceMove({ L: [T_(5, 'x'), T_(1)], R: [T_(2, 'x'), T_(7)], v: 'x' }, Q(-2), 'x') + kp('Subtract ' + km('2x') + ' from both sides. Now the variable is on one side only.'),
    watch: 'Subtract the same term from both sides. ' + km('5x + 1 = 2x + 7') + ' becomes ' + km('3x + 1 = 7') + ', not ' + km('3x + 1 = 2x + 7') + '.',
    see: ['addProp', 'varTerm', 'divProp'] },
  divProp: { word: 'Division Property of Equality', def: 'divide both sides by the same number and they stay equal',
    more: 'Divide both sides by the same number, and they stay equal. It is often the last move: divide by the coefficient, and the variable is alone. You can divide by any number but 0.',
    ex: kl('4n = 18') + kl('n = 4.5') + kp('Divide both sides by 4, the coefficient of ' + vi('n') + ': ' + km('18 ÷ 4 = 4.5') + '.'),
    watch: 'Divide both sides by the coefficient. ' + km('4n = 18') + ' gives ' + km('n = 4.5') + ', not ' + km('n = 72') + ', because ' + km('18 ÷ 4 = 4.5') + '.',
    see: ['coef', 'subProp', 'addProp'] },
  solution: { word: 'solution', def: 'the number that makes the two sides of an equation equal',
    more: 'A solution is not just the last line of your work. It is the number that makes both sides of the first equation come out the same. To check it, put it into both sides and get the same number twice.',
    ex: kl('2x + 5 = 3x + 1') + kp('Try ' + km('x = 4') + ': ' + km('2(4) + 5 = 13') + ' and ' + km('3(4) + 1 = 13') + '. The same number twice, so 4 is the solution.'),
    watch: 'Give the value of the variable, not the value of each side. For ' + km('2x + 5 = 3x + 1') + ', the solution is ' + km('x = 4') + ', not 13.',
    see: ['variable', 'noSol', 'infSol'] },
  noSol: { word: 'no solution', def: 'the equation is never true, whatever number the variable is',
    more: 'Sometimes the variable terms cancel and what is left is false, like ' + km('5 = 9') + ', which is never true. The variable is gone, so no number can make it true. The equation has no solution.',
    ex: kl('3x + 4 = 3x + 1') + kl('4 = 1') + kp('Subtract ' + km('3x') + ' from both sides. What is left, ' + km('4 = 1') + ', is never true: no solution.'),
    watch: 'Say no solution only when the variable is gone and what is left is false. ' + km('3x = 0') + ' has one solution, ' + km('x = 0') + ', not no solution.',
    see: ['infSol', 'solution', 'parallel'] },
  infSol: { word: 'infinitely many solutions', def: 'the equation is true for every number the variable could be', say: 'IN-fuh-nit-lee',
    more: 'Sometimes the variable terms cancel and what is left is true, like ' + km('5 = 5') + '. Then every number works, because the two sides are the same expression. The equation has infinitely many solutions.',
    ex: kl('4(x + 1) = 4x + 4') + kl('4x + 4 = 4x + 4') + kl('4 = 4') + kp('Distribute, then subtract ' + km('4x') + ' from both sides. What is left, ' + km('4 = 4') + ', is always true.'),
    watch: 'Say infinitely many solutions only when the variable is gone and what’s left is true, like ' + km('4 = 4') + '. ' + km('2x + 4 = 5x + 4') + ' has one solution, ' + km('x = 0') + ', not infinitely many.',
    see: ['noSol', 'solution', 'sameLine'] },
  system: { word: 'system of equations', def: 'two equations taken together',
    more: 'A system is two equations about the same ' + vi('x') + ' and ' + vi('y') + '. Each equation graphs as a line. A solution of the system has to make both equations true at once.',
    ex: kl('y = x + 1') + kl('y = -5x + 13') + kPlane([Ln(1, 1), Ln(-5, 13)], [2, 3], { x0: -1, x1: 4, y0: -1, y1: 6, ys: 1 }, 'The lines y = x + 1, solid, and y = −5x + 13, dashed, crossing at the point (2, 3).', 'The two lines cross at ' + c3('(2, 3)') + '.') +
      kp('The point (2, 3) makes both equations true: ' + km('2 + 1 = 3') + ' and ' + km('-5(2) + 13 = 3') + '.'),
    watch: 'Give the solution of a system as an ordered pair. For ' + km('y = x + 1') + ' and ' + km('y = -5x + 13') + ', the solution is (2, 3), not just ' + km('x = 2') + '.',
    see: ['solSys', 'pointInt', 'orderedPair'] },
  solSys: { word: 'solution of a system', def: 'an ordered pair (x, y) that makes BOTH equations true',
    more: 'To test a pair, put its ' + vi('x') + ' into each equation and see whether you get its ' + vi('y') + '. If both equations give its ' + vi('y') + ', the pair is a solution of the system. On a graph, it is the point on both lines.',
    ex: kl('y = 6x - 5') + kl('y = x + 5') + kp('(2, 7): ' + km('6(2) - 5 = 7') + ' and ' + km('2 + 5 = 7') + '. Both are true, so (2, 7) is a solution.') +
      kp('(1, 1): ' + km('6(1) - 5 = 1') + ', but ' + km('1 + 5 = 6') + ', not 1. So (1, 1) is not a solution.'),
    watch: 'Test the pair in both equations, not just one. (1, 1) fits ' + km('y = 6x - 5') + ' but fails ' + km('y = x + 5') + ', because ' + km('1 + 5 = 6') + ', not 1.',
    see: ['system', 'orderedPair', 'pointInt'] },
  orderedPair: { word: 'ordered pair', def: 'a point written (x, y): x first, then y',
    more: 'The first number is ' + vi('x') + ': how far across, left or right. The second is ' + vi('y') + ': how far up or down. The order matters, so (2, 5) and (5, 2) are different points.',
    ex: kp('(3, −1): start at 0, go 3 to the right, then 1 down.') + kPlane([], [3, -1], { x0: -1, x1: 4, y0: -3, y1: 2, ys: 1 }, 'The point (3, −1) marked, 3 to the right of 0 and 1 down, with a dotted path to each axis.', 'From 0, go ' + c3('3 right') + ', then ' + c3('1 down') + '.', { guides: true }),
    watch: kw('Write ' + vi('x') + ' first, then ' + vi('y') + '. 3 right and 1 down is (3, −1), not (−1, 3).',
      'Put the first number in the ' + vi('x') + ' box. For (3, −1), the ' + vi('x') + ' box gets 3, not −1.'),
    see: ['solSys', 'pointInt'] },
  intersect: { word: 'intersect', def: 'cross; two lines that intersect meet at one point', say: 'in-ter-SEKT',
    more: 'Two lines intersect where they cross. Lines with different coefficients of ' + vi('x') + ' always intersect, at exactly one point. That point is on both lines.',
    ex: kl('y = 6x - 12') + kl('y = x + 3') + kPlane([Ln(6, -12), Ln(1, 3)], [3, 6], { x0: -1, x1: 5, y0: -1, y1: 8, ys: 1 }, 'The lines y = 6x − 12, solid, and y = x + 3, dashed, intersecting at the point (3, 6).', 'The lines intersect at ' + c3('(3, 6)') + '.') +
      kp('These lines intersect at (3, 6): ' + km('6(3) - 12 = 6') + ' and ' + km('3 + 3 = 6') + '.'),
    watch: 'Draw each line on to the edge of the grid, not only between your points. ' + km('y = x + 3') + ' and ' + km('y = 6x - 12') + ' cross at (3, 6), past your points.',
    see: ['pointInt', 'parallel', 'solSys'] },
  pointInt: { word: 'point of intersection', def: 'the point where two lines cross',
    more: 'The point of intersection is on both lines, so its ' + vi('x') + ' and ' + vi('y') + ' make both equations true. That is why it is the solution of the system. Read its ' + vi('x') + ' across, then its ' + vi('y') + ' up or down.',
    ex: kl('y = x - 1') + kl('y = -5x + 17') + kPlane([Ln(1, -1), Ln(-5, 17)], [3, 2], { x0: -1, x1: 5, y0: -2, y1: 6, ys: 1 }, 'The lines y = x − 1, solid, and y = −5x + 17, dashed, crossing at (3, 2), with a dotted path from the crossing to each axis.', 'The dotted paths lead from ' + c3('(3, 2)') + ' to ' + km('x = 3') + ' and ' + km('y = 2') + '.', { guides: true }) +
      kp('Check it in both equations: ' + km('3 - 1 = 2') + ' and ' + km('-5(3) + 17 = 2') + '.'),
    watch: 'Use the point where the two lines cross, not where one line meets an axis. ' + km('y = x - 1') + ' and ' + km('y = -5x + 17') + ' cross at (3, 2), not at (0, −1).',
    see: ['intersect', 'solSys', 'approx'] },
  parallel: { word: 'parallel lines', def: 'lines that never meet: the same coefficient of x, different numbers added',
    more: 'Parallel lines slant the same way at the same steepness, so they stay the same distance apart. Their equations have the same coefficient of ' + vi('x') + ' and different numbers added. A system of parallel lines has no solution.',
    ex: kl('y = 0.5x + 3') + kl('y = 0.5x - 1') + kPlane([Ln(Q(1, 2), 3), Ln(Q(1, 2), -1)], null, { x0: -4, x1: 5, y0: -3, y1: 6, ys: 1 }, 'The parallel lines y = 0.5x + 3, solid, and y = 0.5x − 1, dashed, with the distance between them marked: 4 apart, measured straight up and down, at every x.', 'Measured straight up and down, the lines are always ' + c2('4 apart') + ', so they never meet.', { gaps: [{ x: Q(2), y1: Q(4), y2: Q(0), t: '4 apart' }] }) +
      kp('The coefficient of ' + vi('x') + ' is 0.5 in both, and 3 and −1 are different. The lines never meet: no solution.'),
    watch: 'Compare the coefficients of ' + vi('x') + ' with their signs. ' + km('y = 2x + 1') + ' and ' + km('y = -2x + 4') + ' are crossing lines, not parallel lines, because 2 and −2 are different.',
    see: ['coefX', 'noSol', 'sameLine'] },
  sameLine: { word: 'the same line', def: 'two equations, written two ways, that graph as one line',
    more: 'Two equations can look different and still say the same thing. Simplify them, and they match: the same coefficient of ' + vi('x') + ' and the same number added. Every point of the line works in both, so the system has infinitely many solutions.',
    ex: kl('y = 6(x - 1)') + kl('y = 6x - 6') + X.fig(FG.tablePic({ xs: [0, 1, 2], rows: [{ name: 'y = 6(x − 1)', ys: [-6, 0, 6] }, { name: 'y = 6x − 6', ys: [-6, 0, 6] }], label: 'Tables of values for y = 6(x − 1) and y = 6x − 6 at x = 0, 1 and 2: both give −6, 0 and 6.' }), 'Both equations make the same table of values, so their graphs are one line.') +
      kp('Distribute: ' + km('6(x - 1) = 6x - 6') + '. The two equations are one line.'),
    watch: kw('Compare values, not how the numbers look. ' + km('y = ½x + 9') + ' and ' + km('y = 0.5x + 9') + ' are the same line, not parallel lines, because ' + km('½ = 0.5') + '.',
      'Distribute before you compare. ' + km('y = 6(x - 1)') + ' is the same line as ' + km('y = 6x - 6') + ', not a different line.'),
    see: ['parallel', 'infSol', 'distProp'] },
  table: { word: 'table of values', def: 'x-values you choose and the y each one gives',
    more: 'Choose ' + km('x = 0') + ' first, then two more values of ' + vi('x') + '. Put each ' + vi('x') + ' into the equation to get its ' + vi('y') + '. Plot the three points: two of them draw the line, and the third is a check.',
    ex: kl('y = 6x - 4') + X.fig(FG.tablePic({ xs: [0, 1, 2], rows: [{ name: 'y = 6x − 4', ys: [-4, 2, 8] }], label: 'The table of values for y = 6x − 4: x = 0, 1 and 2 give y = −4, 2 and 8.' }), 'Each ' + vi('x') + ' gives its own ' + vi('y') + '.') +
      kp(km('6(0) - 4 = -4') + ', ' + km('6(1) - 4 = 2') + ' and ' + km('6(2) - 4 = 8') + '.'),
    watch: 'Multiply the coefficient by the ' + vi('x') + '-value. For ' + km('y = 6x - 4') + ', ' + km('x = 0') + ' gives ' + km('y = -4') + ', not 2, because ' + km('6(0) = 0') + '.',
    see: ['coefX', 'orderedPair', 'pointInt'] },
  coefX: { word: 'coefficient of x', def: 'the number that multiplies x: 3 in y = 3x − 1', say: 'koh-uh-FISH-uhnt',
    more: 'Each step of 1 in ' + vi('x') + ' adds the coefficient of ' + vi('x') + ' to ' + vi('y') + '. In ' + km('y = -x + 13') + ' it is −1, and in ' + km('y = 15') + ' it is 0. Lines with the same coefficient of ' + vi('x') + ' are equally steep in the same direction.',
    ex: kl('y = 6x + 1') + kp(km('6(0) + 1 = 1') + ', ' + km('6(1) + 1 = 7') + ' and ' + km('6(2) + 1 = 13') + '. Each step of 1 in ' + vi('x') + ' adds 6, the coefficient of ' + vi('x') + ', to ' + vi('y') + '.'),
    watch: 'Find the number that multiplies ' + vi('x') + ', even when the ' + vi('x') + '-term is last. In ' + km('y = 5 - 2x') + ', the coefficient of ' + vi('x') + ' is −2, not 5.',
    see: ['coef', 'parallel', 'table'] },
  approx: { word: 'approximate solution', def: 'a crossing read between the grid lines, written with “about”', say: 'uh-PROK-suh-mit',
    more: 'When two lines cross between the grid lines, the point cannot be read exactly. Find the grid lines on each side, then read each coordinate to the nearest tenth. Write about in front of it.',
    ex: kl('y = 6x - 9') + kl('y = -x + 7') + X.fig(FG.zoomPic({ l1: Ln(6, -9), l2: Ln(-1, 7), c: E.meet(Ln(6, -9), Ln(-1, 7)), ax: 'about 2.3', ay: 'about 4.7', label: 'One grid square zoomed in, cut into tenths: the lines y = 6x − 9 and y = −x + 7 cross at about x = 2.3 and y = 4.7.' }),
      'Zoomed in to one grid square, cut into tenths. The ' + c3('crossing') + ' reads about 2.3 across and about 4.7 up.') +
      kp('They cross at about (2.3, 4.7). Check: ' + km('6(2.3) - 9 = 4.8') + ' and ' + km('-2.3 + 7 = 4.7') + '. Close, not equal: a good estimate.'),
    watch: 'Read each coordinate between the grid lines, to the tenth. The crossing is about (2.3, 4.7), not (2, 5), the nearest grid point.',
    see: ['pointInt', 'tenth', 'intersect'] },
  tenth: { word: 'nearest tenth', def: 'one digit after the decimal point',
    more: 'To round to the nearest tenth, keep one digit after the decimal point. Then look at the next digit: 5 or more rounds up, and 4 or less leaves it. On a graph, a tenth is one of ten equal steps between two grid lines.',
    ex: kp('3.46 rounds to 3.5, because the next digit, 6, is 5 or more.') + kp('1.82 rounds to 1.8, because the next digit, 2, is 4 or less.'),
    watch: 'Round up when the next digit is 5 or more. 3.46 rounds to 3.5, not 3.4.',
    see: ['approx'] }
});

/* ------------------------------------------------------------------ an equation, solved one move a line (the lessons' order:
   distribute, collect, the same variable term from both sides, undo the constant, divide, check) */
const vterm = s => s.find(c => c.k === 't' && c.v), cterm = s => s.find(c => c.k === 't' && !c.v);
function distLine(s, v) {
  const gs = s.gs, one = gs.length === 1, F0 = facT(gs[0]);
  return { say: (one ? 'Distribute the ' + F0 + ': ' : 'Distribute on both sides: ') + gs.map(g => g.t.map(t => prodT(g, t)).join(' and ')).join('; ') + '.',
    why: 'the [[distProp]] says ' + (one ? 'the ' + F0 + ' multiplies' : 'each number in front multiplies') + ' every term inside ' + (one ? 'the' : 'its own') + ' parentheses, sign and all.', ex: s.eq };
}
function collLine(s) {
  const bits = [], ar = [];
  s.groups.forEach(g => { const sum = g.reduce((a, c) => qadd(a, c.c), ZERO);
    bits.push(sideT(g) + ' = ' + tT(sum, g[0].v));
    if (g[0].v) ar.push(g.map((c, i) => i ? (qsign(c.c) < 0 ? ' − ' : ' + ') + n(qabs(c.c)) : n(c.c)).join('') + ' = ' + n(sum)); });
  return { say: 'Collect the like terms: ' + bits.join(' and ') + '.', why: ar.length ? '[[likeTerms]] have the same variable part, so you combine their coefficients: ' + ar.join(' and ') + '.' : 'the constants are [[likeTerms]], so you add them.', ex: s.eq };
}
function moveTerm(take, v) {                                           /* the smaller variable term, taken from (or added to) both sides */
  const t = tT(qabs(take), v);
  return qsign(take) < 0 ? { say: 'Add ' + t + ' to both sides.', why: 'the [[addProp]] keeps the two sides equal, and adding ' + t + ' makes the ' + tT(take, v) + ' zero.' }
    : { say: 'Subtract ' + t + ' from both sides, the smaller variable term.', why: 'the [[subProp]] keeps the two sides equal, and taking the smaller term leaves a positive coefficient.' };
}
function checkLine(e, s) {
  /* the coach's own check (coach.js checkSay), in sentences: its numbers stay the coach's */
  const t = C0.checkSay(e, s).s, m = /^Check in the first equation: (.*?)(, and the right side is | and )(.*?)( — the same number on both sides\.|\.)$/.exec(t);
  const head = 'Check: put ' + e.v + ' = ' + n(s) + ' into the first equation.';
  return m ? { say: head + ' The left side is ' + m[1] + ', and the right side is ' + m[3] + '. Both sides are the same number, so the answer is right.' } : { say: t };
}
function solveLines(e, o) {
  o = o || {}; const st = C0.steps(e), out = [], v = e.v; let pic = !!o.pic;
  st.forEach((s, i) => { const pre = i ? st[i - 1].eq : e;
    if (s.k === 'dist') out.push(distLine(s, v));
    else if (s.k === 'coll') out.push(collLine(s));
    else if (s.k === 'var') { const mv = moveTerm(s.take, v); out.push(Object.assign(mv, { ex: s.eq }, pic ? { pic: balanceMove(pre, qneg(s.take), v) } : {})); pic = false; }
    else if (s.k === 'end') { const a = vterm(pre.L).c, mv = moveTerm(a, v);
      out.push({ say: mv.say.replace(', the smaller variable term', ''), why: (qsign(a) < 0 ? 'the [[addProp]]' : 'the [[subProp]]') + ' keeps both sides equal, and the variable terms are the same, so both become 0.' });
      out.push({ say: 'What is left, ' + s.left + ', is ' + (s.kind === 'none' ? 'never true, whatever number ' + v + ' is. So the equation has [[noSol]].' : 'always true, whatever number ' + v + ' is. So the equation has [[infSol]].') }); }
    else if (s.k === 'const') { const k0 = s.k0, a = n(qabs(k0)), plus = qsign(k0) > 0;
      out.push(Object.assign({ say: 'Undo the constant ' + sgn(k0) + ': ' + (plus ? 'subtract ' + a + ' from' : 'add ' + a + ' to') + ' both sides.',
        why: 'the ' + (plus ? '[[subProp]]' : '[[addProp]]') + ' keeps both sides equal, and ' + (plus ? 'subtracting ' : 'adding ') + a + ' makes the ' + sgn(k0) + ' zero, so the variable term is alone.', ex: s.eq }, pic ? { pic: balanceMove(pre, qneg(k0), null) } : {})); pic = false; }
    else if (s.k === 'div') out.push({ say: 'Divide both sides by ' + n(s.co) + ', the [[coef]] of ' + v + '.', why: 'the [[divProp]] keeps both sides equal, and dividing ' + tT(s.co, v) + ' by ' + n(s.co) + ' leaves ' + v + ' alone' + (qsign(s.co) < 0 ? '; the negative sign belongs to the coefficient.' : '.'), ex: s.eq });
    else if (s.k === 'flip') out.push({ say: 'Write it with the variable first: ' + v + ' = ' + n(s.eq.R[0].c) + '.', why: 'an equation says the same thing read from either side.', ex: s.eq });
  });
  return out;
}
/* the walkthrough of an equation: the coach's arithmetic steps, with the moves asked in the lessons' words */
function eqWalk(e, o) {
  o = o || {}; const st = C0.steps(e), out = [], v = e.v;
  st.forEach((s, i) => { const pre = i ? st[i - 1].eq : e; if (o.only && o.only.indexOf(s.k) < 0) return;
    if (s.k === 'dist') { const gs = s.gs, F0 = facT(gs[0]), one = gs.length === 1, inside = gs[0].t;
      out.push(choice('The ' + c1(F0) + ' is in front of the parentheses' + (one ? '' : ', and so is the ' + facT(gs[1])) + '. What is a good first step?', [
        ch('Distribute: multiply every term inside by the number in front', 1),
        ch('Multiply only the first term inside by the number in front', 0, 'That is the most common slip. The [[distProp]] says the number in front multiplies every term inside, the ' + n(inside[1].c) + ' too.'),
        ch('Divide both sides by the ' + F0 + ' to clear the parentheses', 0, 'Dividing would have to divide every term on both sides, not just the parentheses. Distribute first: it is one clear step.')]));
      s.walk.slice(1).forEach((w, j) => out.push(gs.length > 1 && !(gs[j].fr && !isInt(gs[j].f)) ? Object.assign({}, w, { opt: 1 }) : w));
      const g = gs.find(gg => gg.fr && !isInt(gg.f)) || gs[0], t2 = g.t[1];
      out.push(choice('Why does the ' + facT(g) + ' multiply the ' + n(t2.c) + ' too, not only the ' + tH(g.t[0].c, g.t[0].v) + '?', [
        ch('The number in front multiplies the whole group in the parentheses, so it multiplies every term', 1),
        ch('Because ' + n(t2.c) + ' is a constant', 0, 'Being a constant does not matter. The number in front multiplies every term inside, with a variable or without one.'),
        ch('It does not: it multiplies only the term with the variable', 0, 'That is the slip the state tests most. Try it with numbers: 2(3 + 1) = 2(4) = 8, and 2(3) + 2(1) = 8 too.')]));
    } else if (s.k === 'coll') s.walk.forEach(w => out.push(Object.assign({}, w, { ask: String(w.ask).replace(/^Collect the (?:<i>)?\w(?:<\/i>)?-terms: /, 'Collect the like terms: ').replace(/^Collect the numbers: what is /, 'The constants are like terms too. What is ') , opt: 1 })));
    else if (s.k === 'var' || s.k === 'end') { const a = vterm(pre.L).c, b = vterm(pre.R).c, take = s.k === 'var' ? s.take : a, t = tT(qabs(take), v), neg = qsign(take) < 0;
      const right = neg ? 'Add ' + t + ' to both sides' : 'Subtract ' + t + ' from both sides', wrong = neg ? 'Subtract ' + t + ' from both sides' : 'Add ' + t + ' to both sides';
      const where = qeq(a, take) && !qeq(b, take) ? 'on the left' : qeq(b, take) && !qeq(a, take) ? 'on the right' : 'on both sides';
      out.push(choice('Now ' + M(eqH(pre)) + '. ' + (s.k === 'end' ? 'The variable terms are the same on both sides, ' : 'Variable terms are on both sides, ') + M(tH(a, v)) + ' and ' + M(tH(b, v)) + '. ' + (s.k === 'end' ? 'What do you do?' : 'How do you get the variable on one side?'), [ch(right, 1),
        ch(wrong, 0, 'That gives more ' + vi(v) + '’s on both sides, not fewer. ' + (neg ? 'Adding ' + t + ' makes the ' + tT(take, v) + ' ' + where + ' zero.' : 'Subtracting ' + t + ' makes the ' + t + ' ' + where + ' zero.')),
        ch(right.replace(' both sides', ' one side only'), 0, 'Changing one side only breaks the balance. Whatever you do to one side, do to the other.')]));
      if (s.k === 'end') { const L0 = cterm(pre.L), R0 = cterm(pre.R), cl = L0 ? L0.c : ZERO, cr = R0 ? R0.c : ZERO, all = s.kind === 'all', rest = s.left;
        out.push(choice('What is left is ' + M(rest) + '. What does that tell you?', [ch(all ? 'Always true: infinitely many solutions' : 'Never true: no solution', 1),
          ch(all ? 'Never true: no solution' : 'Always true: infinitely many solutions', 0, all ? M(rest) + ' is true, and it stays true for every number, because the variable is gone.' : n(cl) + ' and ' + n(cr) + ' are different numbers. What is left, ' + rest + ', is never true.'),
          ch(vi(v) + ' = 0: one solution', 0, 'The variable is gone, so nothing says what ' + vi(v) + ' is. Read the statement that is left: is it true or false?')])); } }
    else if (s.k === 'const') { const k0 = s.k0, a = n(qabs(k0)), plus = qsign(k0) > 0, co = s.co;
      out.push(choice('Now ' + M(eqH(pre)) + '. The constant ' + c2(sgn(k0)) + ' is on the side with the variable. How do you undo it?', [
        ch(plus ? 'Subtract ' + a + ' from both sides' : 'Add ' + a + ' to both sides', 1),
        ch(plus ? 'Add ' + a + ' to both sides' : 'Subtract ' + a + ' from both sides', 0, plus ? 'That doubles the + ' + a + ' instead of undoing it. The inverse of adding ' + a + ' is subtracting ' + a + '.' : 'That doubles the − ' + a + ' instead of undoing it. The inverse of subtracting ' + a + ' is adding ' + a + '.'),
        ch('Divide only ' + M(tH(co, v)) + ' by ' + n(co), 0, 'Dividing only one term breaks the balance: the ' + a + ' would have to be divided too. Undo the constant first.')]));
      s.walk.slice(1).forEach(w => out.push(Object.assign({}, w, { opt: 2 }))); }
    else if (s.k === 'div') s.walk.forEach(w => out.push(Object.assign({}, w, { ask: 'Now ' + M(eqH(pre)) + '. Divide both sides by the coefficient, ' + n(s.co) + '. ' + w.ask }, o.optDiv ? { opt: 3 } : {})));
  });
  /* 3–6 steps where the work allows (the standard, §5.6): an arithmetic step marked optional goes first */
  const max = o.max || 6; let res = out.slice(); for (const k of [3, 2, 1]) while (res.length > max && res.some(x => x.opt === k)) res.splice(res.findIndex(x => x.opt === k), 1);
  return res.map(x => { const y = Object.assign({}, x); delete y.opt; return y; });
}

/* ------------------------------------------------------------------ the coach's named mistakes, in the standard's pattern */
const COACH = [
  [/^added (\S+) instead of subtracting it: \+ \S+ is undone by subtracting \S+$/, 'added $1 to both sides instead of subtracting it. The inverse of adding $1 is subtracting $1, so subtract it from both sides'],
  [/^subtracted (\S+) instead of adding it: − \S+ is undone by adding \S+$/, 'subtracted $1 from both sides instead of adding it. The inverse of subtracting $1 is adding $1, so add it to both sides'],
  [/^stopped one step short: that is the value of (.+)\. Now divide by (\S+)$/, 'stopped one step early: that is the value of $1, not of the variable alone. Divide both sides by $2, the [[coef]]'],
  [/^multiplied by (\S+) instead of dividing$/, 'multiplied by $1 instead of dividing. The inverse of multiplying by the [[coef]] $1 is dividing both sides by $1'],
  [/^divided by (\S+) instead of (\S+): the sign goes with the number$/, 'divided by $1 instead of $2. The negative sign is part of the [[coef]], so divide both sides by $2'],
  [/^lost a minus sign along the way: (\S+) is the right size, with the wrong sign\. The (signs? to watch in this equation): (.*)\. Find the step where yours went the other way$/, 'lost a minus sign: $1 is the right size with the wrong sign. Look again at the $2: $3'],
  [/^put in a minus sign this equation never makes: every number in it and in its work is positive\. .*$/, 'put in a minus sign that this equation never makes. Every number in it and in its work is positive, so its solution is positive too'],
  [/^multiplied only the (.+?) by (.+?)(?: — the most common slip on this kind of equation)?: the (.+?) multiplies the (.+?) too, so (?:it is|the number added is) (.+?)(?:, not .+)?$/, 'multiplied only the $1 by $2. The [[distProp]] says the $3 multiplies every term inside, so the $4 becomes $5'],
  [/^multiplied only the first term inside each pair of parentheses: the number in front multiplies the second term too$/, 'multiplied only the first term inside each pair of parentheses. The [[distProp]] says each number in front multiplies every term inside, the second term too'],
  [/^lost the sign (?:of \S+ )?on the second term: (.+)$/, 'lost the sign on the second term. A negative number in front carries its sign to every term inside: $1'],
  [/^lost the sign: (.+)$/, 'lost the sign of the constant. Distribute with the signs: $1'],
  [/^left the (.+?) out: it is a like term of (.+?) — collect them, (.+)$/, 'left out the $1. It is a [[likeTerm]] of $2, so collect them: $3'],
  [/^left the (.+?) out: collect it with the (.+?), and the left side has (.+)$/, 'left out the $1. It is a [[likeTerm]] of the $2, so the left side has $3'],
  [/^(added the .+? instead of taking it away|took the .+? away instead of adding it): (.+)$/, '$1. Collect [[likeTerms]] with their own signs: $2'],
  [/^added the (\w)-terms instead of taking one from both sides: (.+?) and (.+?) are on different sides, so take (.+?) from both$/, 'added the $1-terms from the two sides. $2 and $3 are on different sides of the equals sign, so subtract $4 from both sides'],
  [/^added the (\w)-terms instead of taking one from both sides$/, 'added the $1-terms from the two sides. A [[varTerm]] on each side is not a pair of like terms to add: subtract the smaller one from both sides'],
  [/^gave the number multiplying x\. The box here is the number added: it must match the (.+?) on the left$/, 'gave the [[coefX]]. The box here stands alone, so it is a [[constant]]: it must match the $1 on the left'],
  [/^gave the number added on the left\. The box multiplies x: it must match the (.+)$/, 'gave the [[constant]] on the left. The box is in front of x, so it is the [[coefX]]: it must match the $1'],
  [/^divided the fee by the (first|second) price: (.+)$/, (m0, w, r) => 'divided the fee by the ' + w + ' price. ' + r.charAt(0).toUpperCase() + r.slice(1)],
  [/^added the two prices: (.+)$/, (m0, r) => 'added the two prices. ' + r.charAt(0).toUpperCase() + r.slice(1)],
  [/^gave the cost\. The question asks how many (\w+): that is the letter$/, 'gave the cost. The question asks how many $1, which is the value of the [[variable]]'],
  [/^added the (.+?) and the x instead of multiplying: (.+)$/, 'added the $1 and the x instead of multiplying. $2'],
  [/^took the sign of the (.+?) the wrong way$/, 'took the sign of the $1 the wrong way. The number added keeps its own sign: y is the coefficient of x times x, then add $1'],
  /* the two boxes (15 Nov 2026): x = ▢ and y = ▢, or after ▢ weeks and $▢ each */
  [/^swapped the coordinates: the x box takes (.+)$/, 'swapped the coordinates. The x box takes $1'],
  [/^gave where (the \w+ line|one line|\w+) meets the ([xy])-axis, (.+?): (?:that point is )?on one line only$/, 'gave where $1 meets the $2-axis, $3. That point is on one line only, and a [[solSys]] is on both'],
  [/^gave where the (\w+) line meets the y-axis: that point is on one line only$/, 'gave where the $1 line meets the y-axis. That point is on one line only, and a [[solSys]] is on both'],
  [/^took the column where the two y’s are closest, x = (\S+) — there (\S+) and (\S+) are near but not equal\. Near is not the same$/, 'took the column where the two y’s are closest, x = $1. There $2 and $3 are close but not equal, and a solution needs the same y in both'],
  [/^gave the first column of one table: (.+)$/, (m0, r) => 'gave the first column of one table. ' + r.charAt(0).toUpperCase() + r.slice(1)],
  [/^gave the missing value’s column: (.+)$/, (m0, r) => 'gave the missing value’s column. ' + r.charAt(0).toUpperCase() + r.slice(1)],
  [/^swapped the two boxes: the weeks are across the bottom \(x\) and go in the weeks box, and the amount is up the side \(y\)$/, 'swapped the two boxes. The weeks are x, read across the bottom, so they go in the weeks box. The amount is y, read up the side'],
  [/^gave where one line starts, at 0 weeks: that is (.+?), not where the two meet$/, 'gave where one line starts, at 0 weeks. That is $1, not the [[pointInt]]'],
  [/^read the crossing one grid line too far: (.+)$/, (m0, r) => 'read the crossing one grid line too far. ' + r.charAt(0).toUpperCase() + r.slice(1)],
  [/^took the nearest grid point\. It is on neither line: the crossing is between the grid lines, so estimate each coordinate to the tenth$/, 'took the nearest grid point. That point is on neither line, so read each coordinate between the grid lines to the [[tenth]]']];
const coachFix = s => COACH.reduce((t, [a, b]) => t.replace(a, b), String(s));
/* a wrong choice's reason (the coach's MC lines), in sentences and the lessons' words */
const WHYFIX = [[/^It ends at (\w) = 0 — and 0 is a number\. \w = 0 is one solution, not “no solution”\.$/, 'It ends at $1 = 0, and 0 is a number. So $1 = 0 is one solution, not no solution.'],
  [/ is true — a true statement like that means every number works\./, ' is true, and a true statement like that means every number works.'], [/ — a true sentence like that means every number works\./, ', and a true statement like that means every number works.'],
  [/^The letter cancels and (.+?) is left — always true\. /, 'The variable cancels and $1 is left, which is always true. '],
  [/^The lines intersect — at (.+?) — so they share that point: one solution\. Parallel lines would never meet\.$/, 'The lines intersect at $1, so they share that one point: one solution. [[parallel|Parallel lines]] would never meet.'],
  [/, so the lines are parallel — always the same distance apart\./, ', so the lines are [[parallel|parallel]], always the same distance apart.'], [/ — one equation is not enough: /, '. One equation is not enough: '],
  [/ — both true: /, '. Both are true, so '], [/ — one equation true is not enough: /, '. Only one is true, so '],
  [/so they cancel and (.+?) is left — never true, whatever (\w) is: no solution\./, 'so they cancel, and what is left, $1, is never true, whatever $2 is: no solution.'],
  [/the same number, (\S+), multiplies x in both/g, 'the coefficient of x is $1 in both']];
const whyFix = s => fix(WHYFIX.reduce((t, [a, b]) => t.replace(a, b), String(s == null ? '' : s)));

/* ------------------------------------------------------------------ the families */
const SPEC = {};
const SOLVED = { tail: e => [checkLine(e, E.ending(e).s)] };
/* the move that gets the variable on one side, said for THIS equation: take the smaller variable term from both sides (adding it
   when it is negative) */
const moveWord = e => { const s = C0.steps(e).find(x => x.k === 'var' || x.k === 'end'), t = s && s.k === 'var' ? s.take : null;
  return t && qsign(t) < 0 ? 'add the same [[varTerm]] to both sides, so the variable is on one side only' : 'subtract the same [[varTerm]] from both sides, so the variable is on one side only'; };
/* Q1 — like terms and one distribution: a(bn + c) ± dn = r */
SPEC.like = { terms: ['distProp', 'likeTerms'], pic: true,
  notice: p => { const g = groupsOf(p.eq)[0];
    return 'This equation has parentheses and [[likeTerms]]. Distribute first: the [[distProp]] says the ' + c1(facT(g)) + ' multiplies every term inside, ' + M(tH(g.t[0].c, g.t[0].v)) + ' and ' + M(tH(g.t[1].c)) + '. Then collect the like terms and solve.' + arrows([g], false); },
  first: p => { const s = C0.steps(p.eq)[0]; return Object.assign(distLine(s, p.eq.v), { pic: arrows(s.gs, true) }); },
  sol: p => solveLines(p.eq, { pic: true }).concat(SOLVED.tail(p.eq)),
  walk: p => eqWalk(p.eq) };
/* Q2 — variables on both sides */
SPEC.both = { terms: ['varTerm', 'subProp'], pic: true,
  notice: p => { const e = p.eq, a = vterm(e.L).c, b = vterm(e.R).c, v = e.v;
    return 'Here a [[varTerm]] is on each side: ' + c1(tT(a, v)) + ' and ' + c1(tT(b, v)) + '. Subtract the smaller one from both sides, so the variable is on one side only. The [[subProp]] keeps the two sides equal.' + balanceOf(e); },
  first: p => { const s = C0.steps(p.eq)[0]; return Object.assign(moveTerm(s.take, p.eq.v), { ex: s.eq, pic: balanceMove(p.eq, qneg(s.take), p.eq.v) }); },
  sol: p => solveLines(p.eq).concat(SOLVED.tail(p.eq)),
  walk: p => eqWalk(p.eq) };
/* Q3 — parentheses on both sides, a fraction in front of one */
SPEC.parens = { terms: ['distProp', 'varTerm'], pic: true,
  notice: p => { const gs = groupsOf(p.eq), g = gs.find(x => x.fr && !isInt(x.f)) || gs[0];
    return 'There are parentheses on both sides, and a fraction in front of one. Distribute first: the [[distProp]] says each number in front multiplies every term inside, so the ' + c1(facT(g)) + ' reaches ' + M(tH(g.t[0].c, g.t[0].v)) + ' and ' + M(tH(g.t[1].c)) + '. Then ' + moveWord(p.eq) + '.' + arrows(gs, false); },
  first: p => { const s = C0.steps(p.eq)[0]; return Object.assign(distLine(s, p.eq.v), { pic: arrows(s.gs, true) }); },
  sol: p => solveLines(p.eq, { pic: true }).concat(SOLVED.tail(p.eq)),
  walk: p => eqWalk(p.eq) };
/* Q4 — a decimal distributed */
SPEC.decimal = { terms: ['distProp', 'varTerm'], pic: true,
  notice: p => { const g = groupsOf(p.eq)[0];
    return 'A decimal is in front of the parentheses. Distribute first: the [[distProp]] says the ' + c1(facT(g)) + ' multiplies every term inside, ' + M(tH(g.t[0].c, g.t[0].v)) + ' and ' + M(tH(g.t[1].c)) + ', sign and all. Then ' + moveWord(p.eq) + '.' + arrows([g], false); },
  first: p => { const s = C0.steps(p.eq)[0]; return Object.assign(distLine(s, p.eq.v), { pic: arrows(s.gs, true) }); },
  sol: p => solveLines(p.eq, { pic: true }).concat(SOLVED.tail(p.eq)),
  walk: p => eqWalk(p.eq) };
/* Q5 — one solution, no solution or infinitely many (a choice for each equation) */
SPEC.endings = { mc: true, terms: ['likeTerms', 'varTerm', 'noSol', 'infSol'],
  notice: p => 'Simplify each side first: distribute, then collect the [[likeTerms]]. Then subtract the same [[varTerm]] from both sides and read what is left. If x is left, there is one solution; if not, a false statement means [[noSol]] and a true one [[infSol]].',
  first: p => { const s = C0.steps(p.eq)[0]; return s.k === 'dist' ? distLine(s, 'x') : s.k === 'coll' ? collLine(s) : solveLines(p.eq)[0]; },
  sol: (p, old) => { const en = p.end, lines = solveLines(p.eq);
    if (en.kind === 'one') lines.push({ say: 'It ends at x = ' + n(en.s) + (qeq(en.s, ZERO) ? ', and 0 is a number' : '') + ': one solution.', why: 'a variable is still there, so exactly one number makes the equation true.' }, checkLine(p.eq, en.s));
    lines.push({ say: 'The answer is ' + C0.ENDW[en.kind].toLowerCase() + '.' });
    return lines; },
  walk: (p, old) => { const en = p.end, w = eqWalk(p.eq, en.kind === 'one' ? { max: 5, optDiv: true } : {});
    if (en.kind === 'one') { const s = n(en.s), z = qeq(en.s, ZERO), st = C0.steps(p.eq), d = st.find(x => x.k === 'div');
      const pd = d ? (st[st.indexOf(d) - 1] || {}).eq : null;
      w.push(choice((pd ? 'Dividing both sides of ' + M(eqH(pd)) + ' by ' + n(d.co) + ' gives ' : 'It ends at ') + M(vi('x') + ' = ' + nHtml(en.s)) + '. How many solutions does the equation have?', [ch('One solution', 1),
        ch('No solution', 0, z ? '0 is a number, and x = 0 makes the equation true. So there is one solution.' : 'x = ' + s + ' makes the equation true, so there is a solution.'),
        ch('Infinitely many solutions', 0, 'Only x = ' + s + ' makes the equation true, not every number. So there is exactly one solution.')], { keep: true })); }
    return w; } };
/* Q6 — fill the box */
SPEC.box = { terms: ['coefX', 'constant'], pic: false,
  notice: p => { const g = p.prm.goal;
    return (g === 'none' ? 'For [[noSol]], the two sides need the same [[coefX]] and different [[constant|constants]].' : 'For [[infSol]], both sides must be the same expression: the same [[coefX]] and the same [[constant]].') +
      ' Simplify the left side first: distribute, then collect the like terms. ' + (g === 'allc' ? 'The box stands alone, so it is the constant on the right.' : 'The box is in front of x, so it is the coefficient of x on the right.'); },
  first: p => { const x = p.prm, g = groupsOf({ L: p.eq.L, R: [] })[0], s = C0.steps({ L: p.eq.L, R: [T_(0)], v: 'x' })[0];
    return { say: 'Simplify the left side. Distribute the ' + facT(g) + ': ' + g.t.map(t => prodT(g, t)).join(' and ') + '.', why: 'the [[distProp]] says the ' + facT(g) + ' multiplies every term inside the parentheses, sign and all.', ex: { L: s.eq.L, R: p.eq.R, v: 'x' } }; },
  sol: (p, old) => { const x = p.prm, K = n(Q(x.K)), C = n(Q(x.C)), out = [];
    const st = C0.steps({ L: p.eq.L, R: [T_(0)], v: 'x' }).filter(s => s.k === 'dist' || s.k === 'coll');
    st.forEach((s, i) => { const l = s.k === 'dist' ? SPEC.box.first(p) : Object.assign(collLine(s), { ex: { L: s.eq.L, R: p.eq.R, v: 'x' } }); out.push(l); });
    const left = sideT([T_(x.K, 'x'), T_(x.C)]);
    if (x.goal === 'none') {
      out.push({ say: 'The left side is ' + left + '. Its constant, ' + C + ', and the ' + n(Q(x.e)) + ' on the right are already different. So the box must be ' + K + ', to match the ' + tT(x.K, 'x') + '.',
        why: 'with the same coefficient of x on both sides, subtracting ' + tT(x.K, 'x') + ' leaves only the constants, and what is left, ' + C + ' = ' + n(Q(x.e)) + ', is never true.' });
      out.push({ say: 'Check: with ' + K + ' in the box, subtracting ' + tT(x.K, 'x') + ' from both sides leaves ' + C + ' = ' + n(Q(x.e)) + ', never true: no solution. Any other number in the box gives one solution.', ex: '□ = ' + nHtml(p.ans) });
    } else if (x.goal === 'allx') {
      out.push({ say: 'The left side is ' + left + '. The constants already match, ' + C + ' on both sides. So the box must be ' + K + ', to match the ' + tT(x.K, 'x') + '.', why: 'when both sides are the same expression, every number makes them equal.' });
      out.push({ say: 'Check: with ' + K + ' in the box, both sides are ' + left + '. Subtracting ' + tT(x.K, 'x') + ' leaves ' + C + ' = ' + C + ', always true: infinitely many solutions.', ex: '□ = ' + nHtml(p.ans) });
    } else {
      out.push({ say: 'The left side is ' + left + '. The x-terms already match, ' + tT(x.K, 'x') + ' on both sides. So the box must be ' + C + ', to match the constant.', why: 'when both sides are the same expression, every number makes them equal.' });
      out.push({ say: 'Check: with ' + C + ' in the box, both sides are ' + left + '. Subtracting ' + tT(x.K, 'x') + ' leaves ' + C + ' = ' + C + ', always true: infinitely many solutions.', ex: '□ = ' + nHtml(p.ans) });
    }
    return out; },
  walk: (p, old) => eqWalk({ L: p.eq.L, R: [T_(0)], v: 'x' }, { only: ['dist', 'coll'] }).concat(old.slice(-2).map(s => s.type === 'choice' && /what goes in the box\?$/.test(s.ask) ? Object.assign({}, s, { opts: s.opts.map(o => Object.assign({}, o, { label: o.label.replace('The number that multiplies x on the left', 'The coefficient of x on the left').replace('The number added on the left', 'The constant on the left'),
      why: o.why.replace('The box is in front of x: it multiplies x.', 'The box is in front of x, so it is a coefficient, not a constant.').replace('Any other number gives two different x-terms, and then the equation has one solution.', 'Any other number gives two different coefficients of x, and then the equation has one solution.') })) })
    : Object.assign({}, s, { ask: String(s.ask).replace('What number multiplies x on the left?', 'What is the coefficient of x on the left?').replace('What number is added on the left?', 'What is the constant on the left?'), hint: s.hint && String(s.hint).replace('It is the number in front of x once the left side is simplified.', 'It is the number in front of x once the left side is simplified, sign and all.') }))) };
/* Q7 — two plans that cost the same */
function planTape(p) {
  const x = p.prm, P = E.PLANS[x.ctx], v = P.v, cells = (a, k) => Array.from({ length: k }, (z, i) => i === k - 2 ? '…' : '$' + a);
  const rowA = { lab: 'A', segs: [{ w: 3, c: 2, t: '$' + x.f, brace: 'once' }, { w: 7, c: 1, cells: cells(x.a, 4), brace: v + ' ' + P.unit }] };
  const rowB = x.g ? { lab: 'B', segs: [{ w: 3, c: 2, t: '$' + x.g, brace: 'once' }, { w: 7, c: 1, cells: cells(x.b, 4), brace: v + ' ' + P.unit }] } : { lab: 'B', segs: [{ w: 10, c: 1, cells: cells(x.b, 5), brace: v + ' ' + P.unit }] };
  const lab = 'Two tape diagrams. A: ' + P.who[0] + ', $' + x.f + ' once, then $' + x.a + ' for each of ' + v + ' ' + P.unit + '. B: ' + P.who[1] + ', ' + (x.g ? '$' + x.g + ' once, then ' : '') + '$' + x.b + ' for each of ' + v + ' ' + P.unit + '.';
  return X.fig(X.tape({ rows: [rowA, rowB], label: lab }), 'A is ' + P.who[0] + ' and B is ' + P.who[1] + '. ' + c1('The price each ' + P.one) + ' repeats ' + v + ' times; ' + c2('a fee') + ' is paid once.');
}
SPEC.plans = { terms: ['coef', 'constant'], pic: true,
  notice: p => { const P = E.PLANS[p.prm.ctx], v = P.v;
    return 'Each plan costs its fee once, plus its price each ' + P.one + ' times ' + vi(v) + '. The price each ' + P.one + ' is the [[coef]] of ' + vi(v) + ', and a fee is a [[constant]]. Write the two costs as expressions, set them equal and solve.' + planTape(p); },
  first: p => { const x = p.prm, P = E.PLANS[x.ctx], eq = p.eq;
    return { say: P.who[0].charAt(0).toUpperCase() + P.who[0].slice(1) + ' costs ' + sideT(eq.L) + ' for ' + eq.v + ' ' + P.unit + ', and ' + P.who[1] + ' costs ' + sideT(eq.R) + '. Set the two costs equal.', why: 'each price is paid once for every ' + P.one + ', so it multiplies ' + eq.v + '; a fee is paid once, so it is added.', ex: eq }; },
  sol: (p, old) => { const x = p.prm, P = E.PLANS[x.ctx], A = x.f + x.a * x.n, eq = p.eq;
    return [SPEC.plans.first(p)].concat(solveLines(eq, { pic: true }))
      .concat([{ say: old[old.length - 1].say.replace(/ — both \$(\d+), after (\d+) (\w+)\.$/, '. Both cost $$$1 after $2 $3, so the answer makes sense.') }]); },
  walk: (p, old) => { const x = p.prm, P = E.PLANS[x.ctx];
    return [Object.assign({}, old[0], { ask: 'Each plan is its fee plus its price each ' + P.one + ' times ' + vi(P.v) + '. ' + old[0].ask,
      opts: old[0].opts.map(o => Object.assign({}, o, { why: o.why.replace(/^Each fee goes with its own price: (.)/, (m0, c) => 'Each fee goes with its own price. ' + c.toUpperCase()).replace(/^The fee is paid once; only the price each (\w+) is multiplied by (\w)\.$/, 'The fee is paid once, so it is a constant. Only the price each $1 is multiplied by $2.') })) })].concat(eqWalk(p.eq)); } };
/* Q8 — select all the systems with (a, b) as a solution */
SPEC.selSys = { mc: true, terms: ['solSys'],
  notice: x => 'A [[solSys]] makes BOTH of its equations true. For each system, put x = ' + n(Q(x.pa)) + ' into both equations and see whether each gives y = ' + n(Q(x.pb)) + '. One true equation is not enough.',
  first: x => ({ say: 'Start with system A. ' + whyFix(C0.SELWHY(x, 0)).replace(/^A\. /, ''), why: 'a solution of a system must make both of its equations true.' }),
  sol: (x, old) => [{ say: 'For each system, put x = ' + n(Q(x.pa)) + ' into both equations and compare with y = ' + n(Q(x.pb)) + '.', why: 'a [[solSys]] must make both equations true, so one true equation is not enough.' }]
    .concat(old.map(l => ({ say: whyFix(l.say) }))),
  walk: (x, old) => old.map((s, i) => { const [l1, l2] = x.systems[i], r = x.correct.indexOf(i) >= 0, P = M(pairH(Q(x.pa), Q(x.pb)));
    return Object.assign({}, s, { ask: 'System ' + LET[i] + ' is ' + M(lineH(l1)) + ' and ' + M(lineH(l2)) + '. Does ' + P + ' make both of its equations true?',
      opts: [ch('Yes: ' + P + ' is a solution of system ' + LET[i], r, r ? '' : whyFix(C0.SELWHY(x, i))), ch('No: ' + P + ' is not a solution of system ' + LET[i], !r, r ? whyFix(C0.SELWHY(x, i)) : '')] }); }) };
/* Q9 — is (x, y) a solution of the system? */
function pairPic(x) {
  const P = [[Q(x.px), Q(x.py)]], c = E.meet(x.l1, x.l2); if (c) P.push([c.x, c.y]);
  const w = winAround(P, 1), t = C0.MC.isSol.truth(x), where = t[0] && t[1] ? 'on both lines' : t[0] ? 'on the solid line only' : t[1] ? 'on the dashed line only' : 'on neither line';
  return planePic({ w, lines: [x.l1, x.l2], mark: { x: Q(x.px), y: Q(x.py), t: pairT(Q(x.px), Q(x.py)) }, label: 'The two lines, y = ' + sideT(lineSide(x.l1)) + ' solid and y = ' + sideT(lineSide(x.l2)) + ' dashed, with the point ' + pairT(Q(x.px), Q(x.py)) + ' marked ' + where + '.' },
    'The point ' + c3(pairT(Q(x.px), Q(x.py))) + ' is ' + where + '. A solution of the system is on both lines.');
}
SPEC.isSol = { mc: true, terms: ['solSys'], pic: true,
  notice: x => 'A [[solSys]] makes BOTH equations true. Put x = ' + n(Q(x.px)) + ' into each equation and see whether it gives y = ' + n(Q(x.py)) + '. One true equation is not enough.',
  first: x => ({ say: 'Put x = ' + n(Q(x.px)) + ' into the first equation. ' + C0.MC.isSol.at(x, 0).replace(/, true$/, ', which is the pair’s y.').replace(/, not (\S+)$/, ', not $1.'), why: 'the pair is a solution only if each equation gives its y when you put in its x.' }),
  sol: (x, old) => old.slice(0, -1).map((l, i) => i === 0 ? Object.assign({}, l, { why: 'a [[solSys]] must make both equations true.' }) : l).concat([Object.assign({}, old[old.length - 1], { say: whyFix(old[old.length - 1].say), pic: pairPic(x) })]),
  walk: (x, old) => old.map((s, i) => (i === 1 || i === 3) && s.type === 'choice' ? Object.assign({}, s, { opts: s.opts.map(o => { if (o.ok) return o; const L = i === 1 ? x.l1 : x.l2, g = n(yAt(L, x.px)), y = n(Q(x.py)), t = onLine(L, x.px, x.py);
      return Object.assign({}, o, { why: t ? 'The equation gives ' + g + ', the same as the pair’s y. So this equation is true.' : 'The equation gives ' + g + ', but the pair’s y is ' + y + '. So this equation is false.' }); }) })
    : i === old.length - 1 ? Object.assign({}, s, { opts: s.opts.map((o, k) => Object.assign({}, o, { label: LET[k] + ': ' + x.opts[k].replace(/^(Yes|No) — /, '$1, ') })) }) : s) };
/* Q10 — two lines that cross: how many solutions? */
SPEC.countCross = { mc: true, terms: ['solSys', 'intersect', 'pointInt'], pic: true,
  notice: x => 'Each [[solSys]] is a point on both lines, so count the points the two lines share. Lines that [[intersect]] once share one point, the [[pointInt]].' + three(),
  first: x => ({ say: 'Compare the coefficients of x: ' + n(x.l1.m) + ' in the first equation and ' + n(x.l2.m) + ' in the second.', why: 'different coefficients of x mean the lines are not parallel, so they must cross once.' }),
  sol: (x, old) => [Object.assign({}, old[0], { why: 'the point of intersection is on both lines, so it makes both equations true.', pic: planePic({ w: x.fig.w, lines: [x.l1, x.l2], mark: { x: x.cross.x, y: x.cross.y, t: pairT(x.cross.x, x.cross.y) }, label: 'The graph with the point of intersection, ' + pairT(x.cross.x, x.cross.y) + ', marked.' }, 'The lines intersect once, at ' + c3(pairT(x.cross.x, x.cross.y)) + '.') }),
    Object.assign({}, old[1], { say: old[1].say.replace(/^Different numbers multiply x, (.+?) and (.+?), so the lines must cross\./, 'The coefficients of x are different, $1 and $2, so the lines must cross.') })],
  walk: (x, old) => [choice('What is the coefficient of x in each equation, ' + M(lineH(x.l1)) + ' and ' + M(lineH(x.l2)) + '?', [ch('Different: ' + n(x.l1.m) + ' and ' + n(x.l2.m), 1),
    ch('The same in both', 0, 'Look again: the first has ' + n(x.l1.m) + ' and the second has ' + n(x.l2.m) + '. Different coefficients of x mean the lines cross.')])].concat(old) };
/* Q11 — parallel lines, or one line written two ways */
SPEC.countPar = { mc: true, terms: ['coefX', 'parallel', 'sameLine'], pic: true,
  notice: x => (x.same ? 'One equation has parentheses: distribute first, so both are written the same way. ' : '') + 'Compare the [[coefX]] in the two equations, then the numbers added. The same coefficient with different numbers added makes [[parallel]]; with the same number added, it is [[sameLine]].' + three(),
  first: x => { if (!x.same) return { say: 'Compare the coefficients of x: both equations have ' + n(x.l1.m) + '.', why: 'the same coefficient of x means the lines are equally steep in the same direction.' };
    const alt = (x.l1.alt ? x.l1 : x.l2).alt;
    return { say: 'Distribute the ' + n(Q(alt.a)) + ': ' + lineT(x.l1.alt ? x.l1 : x.l2) + ' becomes y = ' + sideT([T_(alt.a, 'x'), T_(qmul(Q(alt.a), Q(alt.c))), T_(alt.d)]) + ', which is y = ' + sideT(lineSide({ m: x.l1.m, b: x.l1.b })) + '.', why: 'the [[distProp]] says the ' + n(Q(alt.a)) + ' multiplies both the x and the ' + n(Q(alt.c)) + '.' }; },
  sol: (x, old) => { const l1 = x.l1, l2 = x.l2;
    if (x.same) { const xs = [0, 1, 2], lin = { m: l1.m, b: l1.b };
      return [Object.assign({}, old[0], { why: 'the [[distProp]] lets you write it without parentheses, and then the two equations match.' }),
        Object.assign({}, old[1], { pic: X.fig(FG.tablePic({ xs, rows: [{ name: lineT(l1), ys: xs.map(v => qnum(yAt(lin, v))) }, { name: lineT(l2), ys: xs.map(v => qnum(yAt(lin, v))) }], label: 'Tables of values for the two equations at x = 0, 1 and 2: both give the same y every time.' }),
          'Both equations make the same table of values, so their graphs are one line.') })]; }
    const d = qabs(qsub(l1.b, l2.b)), g = [-2, 2].filter(v => v >= x.fig.w.x0 + 0.5 && v <= x.fig.w.x1 - 0.5).map(v => ({ x: Q(v), y1: yAt(l1, v), y2: yAt(l2, v), t: n(d) + ' apart' })).filter(z => [z.y1, z.y2].every(y => qnum(y) >= x.fig.w.y0 && qnum(y) <= x.fig.w.y1));
    return [Object.assign({}, old[0], { why: 'the coefficient of x is the same, so for every x the two y’s stay the same distance apart.' }),
      Object.assign({}, old[1], { say: old[1].say.replace(/^So the lines are parallel — always (\S+) apart up the side — and never meet: no solution\./, 'So the lines are parallel, always $1 apart measured straight up and down, and they never meet: no solution.'),
        pic: planePic({ w: x.fig.w, lines: [l1, l2], gaps: g, label: 'The two parallel lines with the distance between them marked: ' + n(d) + ' apart, measured straight up and down, at every x.' }, 'Measured straight up and down, the lines are always ' + c2(n(d) + ' apart') + ', so they never meet.') })]; },
  walk: (x, old) => old };
/* Q12 — read the solution from the graph */
const crossPic = (w, l1, l2, P, cap, story, dots) => planePic({ w, lines: [l1, l2], dots, mark: { x: P[0], y: P[1], t: pairT(P[0], P[1]) }, guides: true, story: !!story, names: story,
  label: 'The graph with the point of intersection, ' + pairT(P[0], P[1]) + ', marked, and a dotted path from it to each axis.' }, cap);
SPEC.readGraph = { terms: ['solSys', 'pointInt'], pic: true,
  notice: p => 'The [[solSys]] is the [[pointInt]], where the two lines cross. Read its x across for the x box, then its y, up or down, for the y box.',
  first: p => ({ say: 'Find the point of intersection. Go straight ' + (qsign(p.ans[1]) < 0 ? 'up' : 'down') + ' from it to the x-axis and read its x.', why: 'x is how far across, and it goes in the x box.' }),
  sol: (p, old) => [Object.assign({}, old[0], { pic: crossPic(p.figw, p.l1, p.l2, p.ans, 'The dotted paths lead from ' + c3(pairT(p.ans[0], p.ans[1])) + ' to x = ' + n(p.ans[0]) + ' and y = ' + n(p.ans[1]) + '.') }),
    { say: old[1].say.replace(/^Check it in both equations — /, 'Check it in both equations: ') , why: 'a solution of a system must make both equations true.' },
    { say: 'Type ' + n(p.ans[0]) + ' in the x box and ' + n(p.ans[1]) + ' in the y box.', ex: old[1].ex }],
  walk: (p, old) => boxAsk(old) };
/* Q13 — two tables of values */
function tableLine(p, filled, which) {
  const l = which ? p.l2 : p.l1, xs = p.xs, ys = xs.map(x => qnum(yAt(l, x))), w = winAround(xs.map((x, i) => [Q(x), Q(ys[i])]), 1);
  return { xs, ys, w, l };
}
SPEC.tableGap = { terms: ['table', 'coefX'], pic: true,
  notice: p => 'A [[table]] gives the y for each x of one equation. Put the missing column’s x, ' + p.miss + ', into ' + M(lineH(p.l1)) + ': the [[coefX]] times x, plus the number added.' +
    X.fig(FG.tablePic({ xs: p.xs, hi: p.miss, rows: [{ name: lineT(p.l1), ys: p.xs.map((x, i) => i === p.miss ? null : qnum(yAt(p.l1, x))) }], label: 'The table of values for ' + lineT(p.l1) + ', with the missing column, x = ' + p.miss + ', boxed.' }),
      'The ' + c3('boxed column') + ' is x = ' + p.miss + '. Its y is the missing number.'),
  first: p => ({ say: 'Put x = ' + p.miss + ' into ' + lineT(p.l1) + '. Start with the coefficient of x times x: ' + n(p.l1.m) + '(' + p.miss + ').', why: 'the coefficient of x, ' + n(p.l1.m) + ', multiplies x, so you multiply first and then add the number added.' }),
  sol: (p, old) => { const T0 = tableLine(p, true, 0), y = yAt(p.l1, p.miss);
    return [Object.assign({}, old[0], { why: 'a table of values puts each x into the equation to get its y.' }),
      Object.assign({}, old[1], { pic: X.fig(FG.tablePic({ xs: p.xs, hi: p.miss, rows: [{ name: lineT(p.l1), ys: T0.ys, hl: true }], label: 'The table of values for ' + lineT(p.l1) + ', filled in: x = ' + p.miss + ' gives y = ' + n(y) + '.' }), 'The ' + c3('missing value') + ' fits the table.') +
        planePic({ w: T0.w, lines: [p.l1], dots: p.xs.map((x, i) => ({ x: Q(x), y: Q(T0.ys[i]) })), mark: { x: Q(p.miss), y, t: pairT(Q(p.miss), y) }, label: 'The table’s points plotted and the line through them; the point (' + p.miss + ', ' + n(y) + ') is on the line too.' }, 'The table’s points line up, and ' + c3(pairT(Q(p.miss), y)) + ' is on the same line.') })]; },
  walk: (p, old) => { const l = p.l1, m = l.m, xm = Q(p.miss), mx = qmul(m, xm), y = yAt(l, p.miss), b = l.b, prev = yAt(l, p.miss - 1), next = yAt(l, p.miss + 1);
    const add = b.n === 0n ? [] : [{ type: 'num', ask: 'Now add the number added, ' + sgn(b) + '. What is ' + M(n(mx) + (qsign(b) < 0 ? ' − ' + n(qabs(b)) : ' + ' + n(b))) + '?', ans: y, hint: C0.arith('add', mx, b), then: null }];
    return [{ type: 'num', ask: 'The missing value is in the column x = ' + p.miss + '. First the coefficient of x times x: what is ' + M(n(m) + '(' + p.miss + ')') + '?', ans: mx, hint: C0.arith('mul', m, xm), then: null }].concat(add,
      [choice('Does ' + n(y) + ' fit the table, between ' + n(prev) + ' and ' + n(next) + '?', [ch('Yes: each step of 1 in x ' + (qsign(m) > 0 ? 'adds ' + n(m) + ' to' : 'takes ' + n(qabs(m)) + ' from') + ' y, so ' + n(prev) + ', ' + n(y) + ', ' + n(next), 1),
        ch('No: it should be the same as the number beside it', 0, 'Each column has its own x, so each y is different. The y’s change by the same amount at every step.')])]); } };
SPEC.tableSol = { terms: ['solSys', 'table'], pic: true,
  notice: p => 'A [[solSys]] makes both equations true, so both tables give the same y for the same x. Compare the two [[table|tables of values]] one column at a time. That column’s x goes in the x box, and its y in the y box.',
  first: p => ({ say: 'Start at x = 0: the first table gives ' + n(yAt(p.l1, 0)) + ' and the second gives ' + n(yAt(p.l2, 0)) + '. Move right, one column at a time.', why: 'a solution needs the same x and the same y in both tables.' }),
  sol: (p, old) => { const A = tableLine(p, true, 0), B = tableLine(p, true, 1), j = p.xs.indexOf(qnum(p.ans[0])), w = winAround(p.xs.map((x, i) => [Q(x), Q(A.ys[i])]).concat(p.xs.map((x, i) => [Q(x), Q(B.ys[i])])), 1);
    return [Object.assign({}, old[0], { why: 'the solution of a system is the one pair that makes both equations true.', pic: X.fig(FG.tablePic({ xs: p.xs, hi: j, rows: [{ name: lineT(p.l1), ys: A.ys.map((v, i) => i === p.miss ? null : v), hl: true }, { name: lineT(p.l2), ys: B.ys, hl: true }], label: 'Both tables of values, with the column x = ' + n(p.ans[0]) + ' boxed: both give y = ' + n(p.ans[1]) + '.' }),
      'In the ' + c3('boxed column') + ', both tables give ' + n(p.ans[1]) + '.') }),
      Object.assign({}, old[1], { say: old[1].say.replace(/^Check it in both equations — /, 'Check it in both equations: ').replace(/ The solution is (\(.+?\))\.$/, ' The solution is $1: type ' + n(p.ans[0]) + ' in the x box and ' + n(p.ans[1]) + ' in the y box.'), pic: crossPic(w, p.l1, p.l2, p.ans, 'Graphed from their tables' + ' (the dots), the two lines intersect at ' + c3(pairT(p.ans[0], p.ans[1])) + ', the same pair.', null, p.xs.map((x, i) => ({ x: Q(x), y: Q(A.ys[i]) })).filter((d, i) => i !== p.miss).concat(p.xs.map((x, i) => ({ x: Q(x), y: Q(B.ys[i]) })))) })]; },
  walk: (p, old) => { const l = p.l2, x = p.ans[0];
    return boxAsk(old).concat([{ type: 'num', ask: 'Check it in the second equation, ' + M(lineH(l)) + '. What is ' + M(substT(lineSide(l), x)) + '?', ans: yAt(l, x), hint: C0.arith('mul', l.m, x) + ' Then add the number added.', then: null }]); } };
/* Q14 — (a) the story's point of intersection; (b) an estimate between the grid lines */
SPEC.storyMeet = { terms: ['intersect', 'pointInt'], pic: true,
  notice: p => 'The two amounts are equal where the lines [[intersect]], at the [[pointInt]]. Read the weeks across the bottom for the weeks box, then the amount up the side for the other box.',
  first: p => ({ say: 'Find the point of intersection. Go straight down from it to the weeks axis and read the weeks.', why: 'the weeks are x, across the bottom, and they go in the weeks box.' }),
  sol: (p, old) => [Object.assign({}, old[0], { pic: p.figw ? crossPic(p.figw, p.l1, p.l2, p.ans, 'The dotted paths lead from the crossing to ' + c3(n(p.ans[0]) + ' weeks') + ' and ' + c3(p.st.unit === 'dollars' ? '$' + n(p.ans[1]) : n(p.ans[1]) + ' cm') + '.', ['weeks', p.st.yname]) : '' }),
      Object.assign({}, old[1], { why: 'at the point of intersection both equations give the same amount.' }),
      Object.assign({}, old[2], { say: old[2].say + ' Type ' + n(p.ans[0]) + ' in the weeks box and ' + n(p.ans[1]) + ' in the ' + (p.st.unit === 'dollars' ? 'dollars' : 'centimeters') + ' box.' })],
  walk: (p, old) => old.map(s => s.type !== 'num' ? s : Object.assign({}, s, { ask: s.ask + (qeq(s.ans, p.ans[0]) && /weeks\?$/.test(s.ask) ? ' That goes in the weeks box.' : ' That goes in the ' + (p.st.unit === 'dollars' ? 'dollars' : 'centimeters') + ' box.') })) };
SPEC.estimate = { terms: ['intersect', 'approx', 'tenth'], pic: true,
  notice: p => 'These lines [[intersect]] between the grid lines, so the answer is an [[approx]]. Find the grid lines on each side of the crossing, then read x and y, each to the [[tenth]], for their boxes. The pale dashed lines are the halves.',
  first: p => { const c = p.exact, fx = Math.floor(qnum(c.x)), fy = Math.floor(qnum(c.y));
    return { say: 'Find the grid square the crossing is in: x is between ' + mn(fx) + ' and ' + mn(fx + 1) + ', and y is between ' + mn(fy) + ' and ' + mn(fy + 1) + '.', why: 'the grid lines on each side give the whole-number part of each coordinate.' }; },
  sol: (p, old) => { const c = p.exact;
    return [Object.assign({}, old[0], { pic: X.fig(FG.zoomPic({ l1: p.l1, l2: p.l2, c, ax: 'about ' + n(p.ans[0]), ay: 'about ' + n(p.ans[1]), label: 'One grid square zoomed in, cut into tenths: the lines cross at about x = ' + n(p.ans[0]) + ' and y = ' + n(p.ans[1]) + '.' }),
      'Zoomed in to one grid square, cut into tenths. The ' + c3('crossing') + ' reads about ' + n(p.ans[0]) + ' across and about ' + n(p.ans[1]) + ' up.') }),
      (() => { const same = qeq(yAt(p.l1, p.ans[0]), yAt(p.l2, p.ans[0])) && qeq(yAt(p.l1, p.ans[0]), p.ans[1]);   /* a crossing exactly on a tenth (fifths): both give the same y */
        return Object.assign({}, old[1], { say: old[1].say.replace(/^Check the estimate in both equations — /, 'Check the estimate in both equations: ').replace(/ Both are close to (\S+): a good estimate\.$/, same ? ' Both are exactly $1: this crossing falls right on a tenth.' : ' Both are close to $1: a good estimate.'),
          why: same ? 'when the crossing falls exactly on a tenth, the reading is exact; most crossings give two y’s that are close, not equal.' : 'an estimate is not exact, so the two equations give y’s that are close, not equal.' }); })(),
      Object.assign({}, old[2], { say: old[2].say + ' Type ' + n(p.ans[0]) + ' in the x box and ' + n(p.ans[1]) + ' in the y box.' })]; },
  walk: (p, old) => { const c = p.exact, fx = Math.floor(qnum(c.x)), fy = Math.floor(qnum(c.y)), sq = (a, b) => 'x between ' + mn(a) + ' and ' + mn(a + 1) + ', y between ' + mn(b) + ' and ' + mn(b + 1);
    return [choice('Which grid square is the point of intersection in?', [ch(sq(fx, fy), 1), fx !== fy ? ch(sq(fy, fx), 0, 'That swaps x and y. x is read across, left to right; y is read up and down.') : ch(sq(fx, fy + 1), 0, 'Look again at y: the crossing is below the grid line y = ' + mn(fy + 1) + ', so y is between ' + mn(fy) + ' and ' + mn(fy + 1) + '.'),
      ch('Exactly on the grid point (' + mn(Math.round(qnum(c.x))) + ', ' + mn(Math.round(qnum(c.y))) + ')', 0, 'The lines cross between the grid lines, not on a grid point. That is why the answer is an estimate.')])].concat(boxAsk(old)); } };
/* the walkthrough's x and y steps say which box each number goes in (the two boxes, 15 Nov 2026) */
function boxAsk(old) { let k = 0; return old.map(s => { if (s.type !== 'num' || k > 1) return s; const v = 'xy'[k++]; return Object.assign({}, s, { ask: s.ask + ' That goes in the ' + v + ' box.' }); }); }
const mn = v => String(v).replace(/^-/, '−');

/* ------------------------------------------------------------------ apply to the coach */
function help(C, W) {
  C0 = C;
  const ORIG = {};
  ['like', 'both', 'parens', 'decimal', 'box', 'plans', 'tableGap'].forEach(fam => { const f = C.F[fam], sp = SPEC[fam]; ORIG[fam] = f;
    C.F[fam] = Object.assign({}, f, { rule: p => X.teach(noFig(sp.notice(p)), 'tap'), sol: p => sp.sol(p, f.sol(p)).map(line), walk: p => sp.walk(p, f.walk(p)).map(stepOut),
      models: p => f.models(p).map(m => Object.assign({}, m, { say: X.teach(coachFix(m.say), 'tap') })) }); });
  ['readGraph', 'tableSol', 'storyMeet', 'estimate'].forEach(fam => { const f = C.PF[fam], sp = SPEC[fam]; ORIG[fam] = f;
    C.PF[fam] = Object.assign({}, f, { rule: p => X.teach(noFig(sp.notice(p)), 'tap'), sol: p => sp.sol(p, f.sol(p)).map(line), walk: p => sp.walk(p, f.walk(p)).map(stepOut),
      models: p => f.models(p).filter((m, i, a) => a.findIndex(z => qeq(z.v[0], m.v[0]) && qeq(z.v[1], m.v[1])) === i).map(m => Object.assign({}, m, { say: X.teach(coachFix(m.say), 'tap') })) }); });
  ['endings', 'isSol', 'countCross', 'countPar'].forEach(fam => { const f = C.MC[fam], sp = SPEC[fam]; ORIG[fam] = f;
    C.MC[fam] = Object.assign({}, f, { rule: x => X.teach(noFig(sp.notice(x)), 'tap'), sol: x => sp.sol(x, f.sol(x)).map(line), walk: x => sp.walk(x, f.walk(x)).map(stepOut),
      why: (x, k) => { const w = f.why(x, k); return w ? X.teach(whyFix(w), 'tap') : w; } }); });
  /* Q8, the select-all: its worked lines, walk and reasons */
  const mcSol = C.mcSolution, stMC = W.stepsMC, sel = C.SELWHY, sf = C.selectFeedback;
  C.mcSolution = x => x.type === 'multi' ? SPEC.selSys.sol(x, mcSol(x)).map(line) : mcSol(x);
  W.stepsMC = x => x.type === 'multi' ? SPEC.selSys.walk(x, stMC(x)).map(stepOut) : stMC(x);
  C.SELWHY = (x, i) => whyFix(sel(x, i));
  C.selectFeedback = (x, ks, tries) => { const r = sf(x, ks, tries); if (r && r.v === 'wrong') { r.rule = X.teach(SPEC.selSys.notice(x), 'tap'); r.what = r.what.map(w => whyFix(w).replace(/ Test each pair in both equations\.$/, ' Put the x into both equations of each system.')); } return r; };
  const fb = C.feedback; C.feedback = (p, a) => { const r = fb(p, a); if (r && r.what) r.what = r.what.map(w => String(w).replace(/ Tap Hint to go one step at a time\.$/, ' Open Hint, then tap Step by step with me.').replace(/ — not equal\.$/, '. The two sides are not equal.').replace(/ — not the same\.$/, '. They are not the same.')); return r; };
  /* Hints 1 and 2 */
  C.rungs = (x, type, ctx) => { const fam = x && x.fam, sp = SPEC[fam]; if (!sp) return null;
    const notice = X.teach(sp.notice(x), 'def'), first = sp.first ? line(sp.first(x)) : null;
    return first ? { notice, first } : { notice }; };
  C.help = { terms: Object.keys(SPEC).reduce((o, f) => (o[f] = SPEC[f].terms, o), {}), pics: Object.keys(SPEC).filter(f => SPEC[f].pic) };
  return C;
}
if (node) module.exports = help; else root.Help = help;
})(this);
