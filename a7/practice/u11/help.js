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

X.gloss({
  likeTerms: { word: 'like terms', def: 'terms with the same variable part, like 3x and 5x' },
  likeTerm: { word: 'like term', def: 'a term with the same variable part, like 3x and 5x' },
  coef: { word: 'coefficient', def: 'the number that multiplies the variable: 3 in 3x' },
  constant: { word: 'constant', def: 'a term with no variable, like the 4 in 8x + 4' },
  variable: { word: 'variable', def: 'the letter that stands for the unknown number' },
  distProp: { word: 'Distributive Property', def: 'the number outside the parentheses multiplies every term inside' },
  varTerm: { word: 'variable term', def: 'a term with a variable in it, like 5x' },
  addProp: { word: 'Addition Property of Equality', def: 'add the same thing to both sides and they stay equal' },
  subProp: { word: 'Subtraction Property of Equality', def: 'subtract the same thing from both sides and they stay equal' },
  divProp: { word: 'Division Property of Equality', def: 'divide both sides by the same number and they stay equal' },
  solution: { word: 'solution', def: 'the number that makes the two sides of an equation equal' },
  noSol: { word: 'no solution', def: 'the equation is never true, whatever number the variable is' },
  infSol: { word: 'infinitely many solutions', def: 'the equation is true for every number the variable could be' },
  system: { word: 'system of equations', def: 'two equations taken together' },
  solSys: { word: 'solution of a system', def: 'an ordered pair (x, y) that makes BOTH equations true' },
  orderedPair: { word: 'ordered pair', def: 'a point written (x, y): x first, then y' },
  intersect: { word: 'intersect', def: 'cross; two lines that intersect meet at one point' },
  pointInt: { word: 'point of intersection', def: 'the point where two lines cross' },
  parallel: { word: 'parallel lines', def: 'lines that never meet: the same coefficient of x, different numbers added' },
  sameLine: { word: 'the same line', def: 'two equations, written two ways, that graph as one line' },
  table: { word: 'table of values', def: 'x-values you choose and the y each one gives' },
  coefX: { word: 'coefficient of x', def: 'the number that multiplies x: 3 in y = 3x − 1' },
  approx: { word: 'approximate solution', def: 'a crossing read between the grid lines, written with “about”' },
  tenth: { word: 'nearest tenth', def: 'one digit after the decimal point' }
});

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
  [/^swapped the coordinates: x comes first, then y — (.+?), not (.+)$/, 'swapped the coordinates. In an [[orderedPair]], x comes first, then y: $1, not $2'],
  [/^swapped the coordinates: x comes first, then y$/, 'swapped the coordinates. In an [[orderedPair]], x comes first, then y'],
  [/^gave where (the \w+ line|one line|\w+) meets the ([xy])-axis, (.+?): (?:that point is )?on one line only$/, 'gave where $1 meets the $2-axis, $3. That point is on one line only, and a [[solSys]] is on both'],
  [/^gave where the (\w+) line meets the y-axis: that point is on one line only$/, 'gave where the $1 line meets the y-axis. That point is on one line only, and a [[solSys]] is on both'],
  [/^took the column where the two y’s are closest, x = (\S+) — there (\S+) and (\S+) are near but not equal\. Near is not the same$/, 'took the column where the two y’s are closest, x = $1. There $2 and $3 are close but not equal, and a solution needs the same y in both'],
  [/^gave the first column of one table: (.+)$/, (m0, r) => 'gave the first column of one table. ' + r.charAt(0).toUpperCase() + r.slice(1)],
  [/^gave the missing value’s column: (.+)$/, (m0, r) => 'gave the missing value’s column. ' + r.charAt(0).toUpperCase() + r.slice(1)],
  [/^swapped the two numbers: the weeks are across \(x\) and the amount is up \(y\)$/, 'swapped the two numbers. The weeks are x, across the bottom, so they come first; the amount is y, up the side'],
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
      Object.assign({}, old[1], { say: old[1].say.replace(/^So the lines are parallel — always (\S+) apart up the side — and never meet: no solution\./, 'So the lines are parallel, always $1 apart up the side, and they never meet: no solution.'),
        pic: planePic({ w: x.fig.w, lines: [l1, l2], gaps: g, label: 'The two parallel lines with the distance between them marked: ' + n(d) + ' apart up the side at every x.' }, 'Up the side, the lines are always ' + c2(n(d) + ' apart') + ', so they never meet.') })]; },
  walk: (x, old) => old };
/* Q12 — read the solution from the graph */
const crossPic = (w, l1, l2, P, cap, story, dots) => planePic({ w, lines: [l1, l2], dots, mark: { x: P[0], y: P[1], t: pairT(P[0], P[1]) }, guides: true, story: !!story, names: story,
  label: 'The graph with the point of intersection, ' + pairT(P[0], P[1]) + ', marked, and a dotted path from it to each axis.' }, cap);
SPEC.readGraph = { terms: ['solSys', 'pointInt'], pic: true,
  notice: p => 'The [[solSys]] is the [[pointInt]], where the two lines cross. Read its x first, across, then its y, up or down.',
  first: p => ({ say: 'Find the point of intersection. Go straight ' + (qsign(p.ans[1]) < 0 ? 'up' : 'down') + ' from it to the x-axis and read its x.', why: 'an ordered pair gives x first, then y.' }),
  sol: (p, old) => [Object.assign({}, old[0], { pic: crossPic(p.figw, p.l1, p.l2, p.ans, 'The dotted paths lead from ' + c3(pairT(p.ans[0], p.ans[1])) + ' to x = ' + n(p.ans[0]) + ' and y = ' + n(p.ans[1]) + '.') }),
    { say: old[1].say.replace(/^Check it in both equations — /, 'Check it in both equations: ') , why: 'a solution of a system must make both equations true.', ex: old[1].ex }],
  walk: (p, old) => old };
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
  notice: p => 'A [[solSys]] makes both equations true, so it is where both tables give the same y for the same x. Compare the two [[table|tables of values]] one column at a time.',
  first: p => ({ say: 'Start at x = 0: the first table gives ' + n(yAt(p.l1, 0)) + ' and the second gives ' + n(yAt(p.l2, 0)) + '. Move right, one column at a time.', why: 'a solution needs the same x and the same y in both tables.' }),
  sol: (p, old) => { const A = tableLine(p, true, 0), B = tableLine(p, true, 1), j = p.xs.indexOf(qnum(p.ans[0])), w = winAround(p.xs.map((x, i) => [Q(x), Q(A.ys[i])]).concat(p.xs.map((x, i) => [Q(x), Q(B.ys[i])])), 1);
    return [Object.assign({}, old[0], { why: 'the solution of a system is the one pair that makes both equations true.', pic: X.fig(FG.tablePic({ xs: p.xs, hi: j, rows: [{ name: lineT(p.l1), ys: A.ys.map((v, i) => i === p.miss ? null : v), hl: true }, { name: lineT(p.l2), ys: B.ys, hl: true }], label: 'Both tables of values, with the column x = ' + n(p.ans[0]) + ' boxed: both give y = ' + n(p.ans[1]) + '.' }),
      'In the ' + c3('boxed column') + ', both tables give ' + n(p.ans[1]) + '.') }),
      Object.assign({}, old[1], { say: old[1].say.replace(/^Check it in both equations — /, 'Check it in both equations: '), pic: crossPic(w, p.l1, p.l2, p.ans, 'Graphed from their tables' + ' (the dots), the two lines intersect at ' + c3(pairT(p.ans[0], p.ans[1])) + ', the same pair.', null, p.xs.map((x, i) => ({ x: Q(x), y: Q(A.ys[i]) })).filter((d, i) => i !== p.miss).concat(p.xs.map((x, i) => ({ x: Q(x), y: Q(B.ys[i]) })))) })]; },
  walk: (p, old) => { const l = p.l2, x = p.ans[0];
    return old.concat([{ type: 'num', ask: 'Check it in the second equation, ' + M(lineH(l)) + '. What is ' + M(substT(lineSide(l), x)) + '?', ans: yAt(l, x), hint: C0.arith('mul', l.m, x) + ' Then add the number added.', then: null }]); } };
/* Q14 — (a) the story's point of intersection; (b) an estimate between the grid lines */
SPEC.storyMeet = { terms: ['intersect', 'pointInt'], pic: true,
  notice: p => 'The two amounts are equal where the lines [[intersect]], at the [[pointInt]]. Read the weeks across the bottom first, then the amount up the side.',
  first: p => ({ say: 'Find the point of intersection. Go straight down from it to the weeks axis and read the weeks.', why: 'the weeks are x, across the bottom, so they come first.' }),
  sol: (p, old) => [Object.assign({}, old[0], { pic: p.figw ? crossPic(p.figw, p.l1, p.l2, p.ans, 'The dotted paths lead from the crossing to ' + c3(n(p.ans[0]) + ' weeks') + ' and ' + c3(p.st.amt(n(p.ans[1]))) + '.', ['weeks', p.st.yname]) : '' }),
      Object.assign({}, old[1], { why: 'at the point of intersection both equations give the same amount.' }), old[2]],
  walk: (p, old) => old };
SPEC.estimate = { terms: ['intersect', 'approx', 'tenth'], pic: true,
  notice: p => 'These lines [[intersect]] between the grid lines, so the answer is an [[approx]]. Find the grid lines on each side of the crossing, then read each coordinate to the [[tenth]]. The pale dashed lines are the halves.',
  first: p => { const c = p.exact, fx = Math.floor(qnum(c.x)), fy = Math.floor(qnum(c.y));
    return { say: 'Find the grid square the crossing is in: x is between ' + mn(fx) + ' and ' + mn(fx + 1) + ', and y is between ' + mn(fy) + ' and ' + mn(fy + 1) + '.', why: 'the grid lines on each side give the whole-number part of each coordinate.' }; },
  sol: (p, old) => { const c = p.exact;
    return [Object.assign({}, old[0], { pic: X.fig(FG.zoomPic({ l1: p.l1, l2: p.l2, c, ax: 'about ' + n(p.ans[0]), ay: 'about ' + n(p.ans[1]), label: 'One grid square zoomed in, cut into tenths: the lines cross at about x = ' + n(p.ans[0]) + ' and y = ' + n(p.ans[1]) + '.' }),
      'Zoomed in to one grid square, cut into tenths. The ' + c3('crossing') + ' reads about ' + n(p.ans[0]) + ' across and about ' + n(p.ans[1]) + ' up.') }),
      (() => { const same = qeq(yAt(p.l1, p.ans[0]), yAt(p.l2, p.ans[0])) && qeq(yAt(p.l1, p.ans[0]), p.ans[1]);   /* a crossing exactly on a tenth (fifths): both give the same y */
        return Object.assign({}, old[1], { say: old[1].say.replace(/^Check the estimate in both equations — /, 'Check the estimate in both equations: ').replace(/ Both are close to (\S+): a good estimate\.$/, same ? ' Both are exactly $1: this crossing falls right on a tenth.' : ' Both are close to $1: a good estimate.'),
          why: same ? 'when the crossing falls exactly on a tenth, the reading is exact; most crossings give two y’s that are close, not equal.' : 'an estimate is not exact, so the two equations give y’s that are close, not equal.' }); })(),
      old[2]]; },
  walk: (p, old) => { const c = p.exact, fx = Math.floor(qnum(c.x)), fy = Math.floor(qnum(c.y)), sq = (a, b) => 'x between ' + mn(a) + ' and ' + mn(a + 1) + ', y between ' + mn(b) + ' and ' + mn(b + 1);
    return [choice('Which grid square is the point of intersection in?', [ch(sq(fx, fy), 1), fx !== fy ? ch(sq(fy, fx), 0, 'That swaps x and y. x is read across, left to right; y is read up and down.') : ch(sq(fx, fy + 1), 0, 'Look again at y: the crossing is below the grid line y = ' + mn(fy + 1) + ', so y is between ' + mn(fy) + ' and ' + mn(fy + 1) + '.'),
      ch('Exactly on the grid point (' + mn(Math.round(qnum(c.x))) + ', ' + mn(Math.round(qnum(c.y))) + ')', 0, 'The lines cross between the grid lines, not on a grid point. That is why the answer is an estimate.')])].concat(old); } };
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
