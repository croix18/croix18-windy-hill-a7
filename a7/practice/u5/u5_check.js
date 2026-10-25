/* A7 Unit 5 practice: the engine and the coach, checked over many sets.   node u5_check.js [sets=3000] [dumped=1500]
   For every set: the shape of the test (the section titles read from build/u5/unit.py; 19 questions, 24 points, each
   question the practice form's kind); every question read back from the text a student sees with this file's own reader,
   and its key worked out again; no question is Form A's or Form B's (read here, compared with test_forms.js — never the
   page's hashes) and the page's hashes are exactly those forms; every key typed back several ways is right; the key rounded,
   unsimplified or unfinished is "Almost"; the sheet's other ratio is right with a note; follow-through from a wrong part (a)
   is recognised, and right in "Like the real test" (6(b) and 16(b), ruling 19); every modelled mistake typed is wrong and
   named; near misses and the negative are never right; the clean rule holds (checked here on its own); every worked line
   carries the answer; every Hint choice has one right option and a reason for each wrong one; no Hint gives its own answer
   away, and no part (b) Hint asks for part (a)'s number; every arithmetic claim in every sentence is true; multiple choice
   and select-all are keyed by their own math, every subset tried. dump.json goes to verify.py, which works everything out
   again from the printed text in sympy, and checks the lessons' shown numbers (ruling 43) from the lesson specs. */
'use strict';
const E = require('./engine.js'), C = require('./coach.js'), U = require('./unit.js'), W = C.Walk, TF = require('./test_forms.js'), KIT = require('../kit/core.js');
const fs = require('fs'), path = require('path');
const NSETS = +(process.argv[2] || 3000), NDUMP = Math.min(NSETS, +(process.argv[3] || 1500));
let nfail = 0; const fails = [];
const fail = (seed, where, what) => { nfail++; if (fails.length < 60) fails.push(seed + ' ' + where + ': ' + what); };
const { Q, qeq, qnum, qabs, qadd, qsub, qmul, qdiv, qlt, decPlain, places, numStr, qdec, qround, isInt } = E;
const LET = 'ABCDEFGH';

/* ---------- the page's text as a student reads it: a fraction "n/d", a mixed number "w n/d", a square "^2" */
const plain = h => String(h).replace(/ /g, ' ')
  .replace(/(\d)<span class="fr"><span class="nu">([^<]*)<\/span><span class="de">([^<]*)<\/span><\/span>/g, '$1 $2/$3')
  .replace(/<span class="fr"><span class="nu">([^<]*)<\/span><span class="de">([^<]*)<\/span><\/span>/g, '$1/$2')
  .replace(/<sup[^>]*>(.*?)<\/sup>/g, '^$1').replace(/<[^>]+>/g, '').replace(/&nbsp;/g, ' ').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim();
/* a number as printed: "1,234.5", "3/4", "2 1/2" */
function rat(s) {
  s = String(s).trim().replace(/,/g, '');
  let m = /^(\d+) (\d+)\/(\d+)$/.exec(s); if (m) return qadd(Q(BigInt(m[1])), Q(BigInt(m[2]), BigInt(m[3])));
  m = /^(\d+)\/(\d+)$/.exec(s); if (m) return Q(BigInt(m[1]), BigInt(m[2]));
  return qdec(s);
}
const NUM = '\\d[\\d,]*(?:\\.\\d+)?(?: \\d+\\/\\d+)?|\\d+\\/\\d+';
const ks = q => decPlain(q);
const typedOf = q => places(q) >= 0 ? decPlain(q) : (qround(qabs(q), 2).n < 0n ? '-' : '') + decPlain(qround(qabs(q), 2));

/* ---------- every arithmetic claim in a sentence is true: a chain "e = e = …", "e ≈ d" (d is e rounded to d's places),
   "a > b"; numbers with commas, fractions and mixed numbers read as numbers */
function prep(t) {
  return t.replace(/(\d),(?=\d{3}(?!\d))/g, '$1').replace(/(\d+) (\d+)\/(\d+)/g, '($1+$2/$3)').replace(/(?<![\d.(+])(\d+)\/(\d+)(?![\d.])/g, '($1/$2)')
    .replace(/([A-Za-z])\^\d+/g, '$1#').replace(/−/g, '-').replace(/×/g, '*').replace(/÷/g, '/').replace(/(\d)\^(\d)/g, '$1**$2');   /* k^2 is a letter's square, not a claim's 2 */
}
function evalE(s) {
  s = s.trim(); if (!s || !/\d/.test(s) || !/^[\d\s.+\-*/()]+$/.test(s.replace(/\*\*/g, '*'))) return null;
  if (/\d\s+\d/.test(s) || /\(\s*\)/.test(s)) return null;
  try { const v = Function('return (' + s + ')')(); return isFinite(v) ? v : null; } catch (e) { return null; }
}
function claims(seed, w, h) {
  const t = prep(plain(h)), runs = t.match(/[\d.+\-*/()≈=<> ]*[=≈<>][\d.+\-*/()≈=<> ]*/g) || [];
  runs.forEach(run => {
    const parts = run.split(/(=|≈|<|>)/), segs = [], ops = [];
    for (let i = 0; i < parts.length; i++) { if (i % 2) ops.push(parts[i]); else segs.push(parts[i]); }
    /* trim the empty ends ("k = 12 ÷ 4 = 3" is read from 12) */
    while (segs.length && evalE(segs[0]) == null) { segs.shift(); ops.shift(); }
    while (segs.length && evalE(segs[segs.length - 1]) == null) { segs.pop(); ops.pop(); }
    if (segs.length < 2) return;
    const vals = segs.map(evalE); if (vals.some(v => v == null)) return;
    counts.claims++;
    for (let i = 0; i < ops.length; i++) {
      const a = vals[i], b = vals[i + 1], op = ops[i];
      if (op === '=' && Math.abs(a - b) > 1e-9 * Math.max(1, Math.abs(a))) fail(seed, w, 'a claim is false: ' + run.trim());
      if (op === '≈') { const dp = ((segs[i + 1].trim().match(/\.(\d+)\)?$/) || ['', ''])[1]).length; if (Math.abs(a - b) > 0.5 * Math.pow(10, -dp) + 1e-9) fail(seed, w, 'a rounding claim is false: ' + run.trim()); }
      if (op === '>' && !(a > b)) fail(seed, w, 'a comparison is false: ' + run.trim());
      if (op === '<' && !(a < b)) fail(seed, w, 'a comparison is false: ' + run.trim());
    }
  });
}

/* ---------- the test, read from its spec */
const SPEC = fs.readFileSync(path.join(__dirname, '..', '..', 'build', 'u5', 'unit.py'), 'utf8');
const TEST_TITLES = [...SPEC.matchAll(/dict\(title="([^"]+)", benchmark="MA\.7\.[A-Z]+\.\d\.\d", items=_\w+\(f\)\)/g)].map(m => m[1]);
if (TEST_TITLES.length !== 3) { console.log('could not read the test\'s three section titles from unit.py'); process.exit(1); }
const WANT = { titles: TEST_TITLES.join('|'), items: '8,7,4', parts: '10,8,6',
  types: 'solo,solo,multi,parts,solo,parts,solo,solo|solo,multi,solo,solo,solo,mc,parts|parts,parts,solo,mc' };
const shape = { mixKnownOne: 0, mixSets: 0 };
const counts = { sets: 0, parts: 0, typedRight: 0, forms: 0, models: 0, near: 0, alt: 0, follow: 0, didMean: 0, solLines: 0, walkSteps: 0, mc: 0, multi: 0, subsets: 0, claims: 0, keysRead: 0, cleanChecked: 0 };
const dump = [];

/* ---------- this file's own reader: each question's numbers, its keys (as test_forms.js writes them) and its answer */
const UNIT_OF = { inches: 'in', centimeters: 'cm', pounds: 'lb', kilograms: 'kg', gallons: 'gal', liters: 'L', miles: 'mi', kilometers: 'km', feet: 'ft', meters: 'm', cups: 'c', ounces: 'oz', grams: 'g' };
function scale(s) {                                  /* "1 in : 5 ft" or "1/4 in : 1 ft" → feet per inch */
  let m = /^1 in : (\d+) ft$/.exec(s); if (m) return Q(+m[1]);
  m = /^1\/(\d+) in : (\d+) ft$/.exec(s); if (m) return Q(+m[1] * +m[2]);
  return null;
}
function read(qn, it) {
  const st = plain(it.stem), P = E.partsOf(it).map(p => plain(p.stem || '')), out = { keys: [], ans: [] };
  const need = (m, what) => { if (!m) throw new Error('cannot read ' + what + ': ' + st + ' | ' + P.join(' | ')); return m; };
  let m;
  switch (qn) {
    case 1: case 2: {
      m = need(/^A (\d+) (cm|m|ft) side of a figure is (\d+) \2 in its scale copy\. Find the scale factor\.$/.exec(st), 'the sides');
      const a = +m[1], b = +m[3]; out.keys.push(['sf', a + '>' + b]); out.ans.push(Q(b, a));
      if (qn === 1 ? !(b > a) : !(b < a)) throw new Error('question ' + qn + ' ' + (qn === 1 ? 'does not enlarge' : 'does not shrink'));
      break; }
    case 3: {
      m = need(/^A figure is scaled by a scale factor of ([\d.]+)\. Select ALL of the statements that are true about the copy\.$/.exec(st), 'k');
      const k = qdec(m[1]); out.keys.push(['sel3', ks(k)]);
      out.correct = it.opts.map(plain).map((o, i) => { let x;
        if ((x = /^Each side is ([\d.]+) times as long\.$/.exec(o))) return qeq(qdec(x[1]), k) ? i : -1;
        if ((x = /^The perimeter is ([\d.]+) times as long\.$/.exec(o))) return qeq(qdec(x[1]), k) ? i : -1;
        if ((x = /^The area is ([\d.]+) times as large\.$/.exec(o))) return qeq(qdec(x[1]), qmul(k, k)) ? i : -1;
        if (/^Each angle is ([\d.]+) times as large\.$/.test(o)) return -1;
        throw new Error('a statement I cannot read: ' + o); }).filter(i => i >= 0);
      break; }
    case 4: {
      m = need(/^A (\d+) (cm|in|ft|m) by (\d+) \2 rectangle is scaled by k = ([\d.]+)\.$/.exec(st), 'the rectangle');
      const w = +m[1], h = +m[3], k = qdec(m[4]), lo = Math.min(w, h), hi = Math.max(w, h);
      out.keys.push(['rect', lo + ',' + hi + '|' + ks(k)], ['rectWH', lo + ',' + hi]);
      need(P[0] === 'Find the copy’s perimeter.' && P[1] === 'Find the copy’s area.', 'the parts');
      out.ans.push(qmul(Q(2 * (w + h)), k), qmul(Q(w * h), qmul(k, k))); break; }
    case 5: {
      m = need(/^A figure has area ([\d,]+) (cm|in|ft|m)\^2\. Its scale copy has area ([\d,]+) \2\^2\. What is the scale factor\?$/.exec(st), 'the areas');
      const A = +m[1].replace(/,/g, ''), B = +m[3].replace(/,/g, ''), k = Math.round(Math.sqrt(B / A));
      need(k * k * A === B, 'a whole k'); out.keys.push(['areaK', A + '>' + B]); out.ans.push(Q(k)); break; }
    case 6: {
      m = need(/^A floor plan is drawn at (.+?)\. A room is ([\d.]+) in by ([\d.]+) in on the plan\.$/.exec(st), 'the plan');
      const r = need(scale(m[1]), 'the scale'), p = qdec(m[2]), q = qdec(m[3]);
      const pa = need(/^Find the real length of the wall drawn ([\d.]+) in long\.$/.exec(P[0]), 'part a');
      need(qeq(qdec(pa[1]), p) && P[1] === 'Find the room’s real area.', 'the parts');
      const lo = qlt(q, p) ? q : p, hi = qlt(q, p) ? p : q;
      out.keys.push(['room', ks(r) + '|' + ks(lo) + ',' + ks(hi)], ['wall', ks(r) + '|' + ks(p)]);
      out.ans.push(qmul(p, r), qmul(qmul(p, r), qmul(q, r))); out.follow = a => qmul(a, qmul(q, r)); break; }
    case 7: {
      m = need(/^A plan is drawn at (.+?)\. A real wall is (\d+) ft long\. How long is it on the plan\?$/.exec(st), 'the wall');
      const r = need(scale(m[1]), 'the scale'), L = +m[2]; out.keys.push(['plan', ks(r) + '|' + L]); out.ans.push(qdiv(Q(L), r)); break; }
    case 8: {
      m = need(/^A plan is drawn at 1 in : (\d+) ft\. A room is ([\d.]+) in by ([\d.]+) in on the plan\. Find the room’s real area\.$/.exec(st), 'the room');
      const r = Q(+m[1]), p = qdec(m[2]), q = qdec(m[3]), lo = qlt(q, p) ? q : p, hi = qlt(q, p) ? p : q;
      out.keys.push(['room', ks(r) + '|' + ks(lo) + ',' + ks(hi)]); out.ans.push(qmul(qmul(p, r), qmul(q, r))); break; }
    case 9: {
      m = need(/^1 in = 2\.54 cm\. How many centimeters is (\d+) in\?$/.exec(st), 'the inches');
      out.keys.push(['conv', 'in>cm|' + m[1]]); out.ans.push(qmul(Q(+m[1]), qdec('2.54'))); out.alt = qdiv(Q(+m[1]), qdec('0.39')); break; }
    case 10: {
      m = need(/^1 (\w+) = ([\d.]+) (\w+) and 1 \3 = ([\d.]+) \1\. Select ALL of the expressions that give the number of (\w+) in (\d+) (\w+)\.$/.exec(st), 'the ratios');
      const one = { [m[1]]: m[2], [m[3]]: m[4] }, to = need(UNIT_OF[m[5]], 'the unit wanted'), n = +m[6], from = m[7];
      need((from === m[1] && to === m[3]) || (from === m[3] && to === m[1]), 'the two units');
      out.keys.push(['conv', from + '>' + to + '|' + n]);
      out.correct = it.opts.map(plain).map((o, i) => { const x = need(/^(\d+) (×|÷) ([\d.]+)$/.exec(o), 'an expression'); need(+x[1] === n, 'the amount in a choice');
        const unitOne = Object.keys(one).find(u => one[u] === x[3]); need(unitOne, 'a ratio in a choice');
        return (x[2] === '×' && unitOne === from) || (x[2] === '÷' && unitOne === to) ? i : -1; }).filter(i => i >= 0);
      break; }
    case 11: {
      m = need(/^1 yd = 3 ft, 1 ft = 12 in, 1 in = 2\.54 cm\. How many centimeters is ([\d.]+) yd\?$/.exec(st), 'the yards');
      const n = qdec(m[1]); out.keys.push(['chain', 'yd>cm|' + ks(n)]); out.ans.push(qmul(qmul(n, Q(36)), qdec('2.54'))); out.alt = qdiv(qmul(n, Q(36)), qdec('0.39')); break; }
    case 12: {
      if ((m = /^1 kg = 2\.204 lb\. How many pounds is (\d+) kg\?$/.exec(st))) { out.keys.push(['conv', 'kg>lb|' + m[1]]); out.ans.push(qmul(Q(+m[1]), qdec('2.204'))); out.alt = qdiv(Q(+m[1]), qdec('0.454')); }
      else { m = need(/^1 lb = 0\.454 kg\. How many kilograms is (\d+) lb\?$/.exec(st), 'the mass'); out.keys.push(['conv', 'lb>kg|' + m[1]]); out.ans.push(qmul(Q(+m[1]), qdec('0.454'))); out.alt = qdiv(Q(+m[1]), qdec('2.204')); }
      break; }
    case 13: {
      m = need(/^1 gal = 3\.785 L\. How many liters is (\d+) gal\?$/.exec(st), 'the gallons');
      out.keys.push(['conv', 'gal>L|' + m[1]]); out.ans.push(qmul(Q(+m[1]), qdec('3.785'))); out.alt = qdiv(Q(+m[1]), qdec('0.264')); break; }
    case 14: {
      m = need(/^1 (in|ft|m|cm|mi|km) = ([\d.]+) (in|ft|m|cm|mi|km)\. An? ([a-z ]+) is ([\d,]+) \1\^2 in area\. Which is closest to its area in square (\w+)\?$/.exec(st), 'the area');
      const r = qdec(m[2]), A = +m[5].replace(/,/g, ''); need(UNIT_OF[m[6]] === m[3], 'the square unit wanted');
      out.keys.push(['sqconv', m[1] + '2>' + m[3] + '2|' + A]);
      const exact = qmul(Q(A), qmul(r, r)), OTHER = { in: '0.39', cm: '2.54', ft: '3.28', m: '0.305', mi: '0.62', km: '1.61' };
      const o = qdec(OTHER[m[1]]), alt = qdiv(Q(A), qmul(o, o));
      const vals = it.opts.map(plain).map(s => { const x = need(new RegExp('^([\\d,.]+) ' + m[3] + '\\^2$').exec(s), 'a choice'); return qdec(x[1].replace(/,/g, '')); });
      const best = x => { const d = vals.map(v => Math.abs(qnum(v) - qnum(x))); return d.indexOf(Math.min(...d)); };
      out.correct = best(exact); if (best(alt) !== out.correct) throw new Error('the sheet\'s two routes pick different choices');
      break; }
    case 15: {
      m = need(/^Rate on Nov 5: 1 US dollar = ([\d.,]+) ([A-Za-z ]+)\.$/.exec(st), 'the rate');
      const r = qdec(m[1].replace(/,/g, '')), cur = m[2];
      const a = need(new RegExp('^How many ' + cur + ' is \\$(\\d+)\\?$').exec(P[0]), 'part a'), b = need(new RegExp('^How many US dollars is ([\\d.,]+) ' + cur + '\\?$').exec(P[1]), 'part b');
      const d = +a[1], c = qdec(b[1].replace(/,/g, ''));
      out.keys.push(['curA', ks(r) + '|' + d], ['curB', ks(r) + '|' + ks(c)]); out.ans.push(qmul(Q(d), r), qdiv(c, r));
      if (!isInt(qdiv(c, r))) throw new Error('part (b) is not a whole number of dollars');
      break; }
    case 16: {
      m = need(/^A (car|truck|van|pickup) gets (\d+) miles per gallon and its tank holds (\d+) gal\.$/.exec(st), 'the car');
      const mm = +m[2], g = +m[3], b = need(/^It makes a ([\d,]+)-mi trip\. How many tanks of gas does the trip use\? \(Part of a tank counts as a whole tank\.\)$/.exec(P[1]), 'part b');
      need(P[0] === 'How far does it go on a full tank?', 'part a');
      const D = +b[1].replace(/,/g, ''); out.keys.push(['tank', mm + '|' + g], ['trip', mm + '|' + g + '|' + D]);
      out.ans.push(Q(mm * g), E.qceil(Q(D, mm * g))); out.follow = a => E.qceil(qdiv(Q(D), a)); break; }
    case 17: {
      m = need(new RegExp('^A recipe for (\\d+) servings uses (' + NUM + ') cups of (\\w+)\\.$').exec(st), 'the recipe');
      const s = +m[1], c = rat(m[2]), food = m[3];
      const a = need(new RegExp('^How much ' + food + ' for (\\d+) servings\\?$').exec(P[0]), 'part a'), b = need(new RegExp('^With (' + NUM + ') cups on hand, how many servings can be made\\?$').exec(P[1]), 'part b');
      const t = +a[1], h = rat(b[1]), cK = isInt(c) ? String(c.n) : c.n + '/' + c.d, hK = isInt(h) ? String(h.n) : h.n + '/' + h.d;
      out.keys.push(['recA', s + '|' + cK + '|' + t], ['recB', s + '|' + cK + '|' + hK], ['recK', decPlain(Q(t, s)) + '|' + cK]);
      out.ans.push(qdiv(qmul(c, Q(t)), Q(s)), qmul(qdiv(h, c), Q(s))); break; }
    case 18: {
      let parts, which, n, u;
      if ((m = /^Paint is mixed (\d+) : (\d+) : (\d+)\. A batch uses (\d+) gal of the (first|second|third) color\. How many gallons is the whole batch\?$/.exec(st))) {
        parts = [+m[1], +m[2], +m[3]]; which = ['first', 'second', 'third'].indexOf(m[5]); n = +m[4]; }
      else { m = need(/^(\w+) is mixed ([a-z ]+) : ([a-z ]+) : ([a-z ]+) = (\d+) : (\d+) : (\d+)\. A batch uses (\d+) (\w+) of ([a-z ]+)\. How many \9 is the whole batch\?$/.exec(st), 'the mixture');
        parts = [+m[5], +m[6], +m[7]]; which = [m[2], m[3], m[4]].indexOf(m[10]); n = +m[8]; need(which >= 0, 'the part named'); }
      need(n % parts[which] === 0, 'a whole part');
      out.keys.push(['mix', parts.join(':') + '|' + which + '|' + n]); out.ans.push(Q(n / parts[which] * (parts[0] + parts[1] + parts[2]))); break; }
    case 19: {
      m = need(/^1 mi = 1\.61 km\. A (\w+) does (\d+) km\/h; a (\w+) does (\d+) mi\/h\. Which is faster\? Choose the answer that shows both speeds in one unit\.$/.exec(st), 'the speeds');
      const A = m[1], kmh = +m[2], B = m[3], mph = +m[4], conv = qmul(Q(mph), qdec('1.61')), fast = qlt(conv, Q(kmh)) ? A : B;
      out.keys.push(['speed', kmh + '|' + mph]);
      out.correct = it.opts.map(plain).map((o, i) => { let x;
        if ((x = /^The (\w+): (\d+) mi\/h = ([\d.]+) km\/h, and ([\d.]+) > ([\d.]+)\.$/.exec(o))) {
          const said = qdec(x[3]), hi = qdec(x[4]), lo = qdec(x[5]);
          const set = [Q(kmh), said]; const okConv = +x[2] === mph && qeq(said, conv);
          const okCmp = qlt(lo, hi) && set.some(v => qeq(v, hi)) && set.some(v => qeq(v, lo));
          return okConv && okCmp && x[1] === fast ? i : -1; }
        return -1; }).filter(i => i >= 0);
      if (out.correct.length !== 1) throw new Error('question 19 has ' + out.correct.length + ' right choices');
      out.correct = out.correct[0];
      break; }
  }
  return out;
}

/* ---------- Hints */
function checkWalk(seed, w, steps, ans, aAns) {
  if (!steps || !steps.length) { fail(seed, w, 'no Hint steps'); return; }
  steps.forEach((s, i) => {
    counts.walkSteps++;
    claims(seed, w + ' Hint', s.ask + ' ' + (s.hint || '') + ' ' + (s.opts || []).map(o => o.label + ' ' + o.why).join(' '));
    if (s.type === 'choice') {
      const ok = s.opts.filter(o => o.ok);
      if (ok.length !== 1) fail(seed, w, 'Hint step ' + (i + 1) + ' has ' + ok.length + ' right options');
      if (s.opts.length < 2) fail(seed, w, 'Hint step ' + (i + 1) + ' has one option');
      if (new Set(s.opts.map(o => plain(o.label))).size !== s.opts.length) fail(seed, w, 'Hint step ' + (i + 1) + ' repeats an option');
      s.opts.filter(o => !o.ok).forEach(o => { if (!o.why) fail(seed, w, 'Hint step ' + (i + 1) + ': no reason for "' + plain(o.label) + '"'); });
    } else if (s.type === 'num') {
      if (!s.ans || s.ans.d === undefined) { fail(seed, w, 'Hint step ' + (i + 1) + ' has no exact answer'); return; }
      if (places(s.ans) < 0 && !/A fraction is fine\./.test(s.hint || '')) fail(seed, w, 'Hint step ' + (i + 1) + ' asks for ' + numStr(s.ans) + ' without saying a fraction is fine');
      if (!s.hint) fail(seed, w, 'Hint step ' + (i + 1) + ' has no hint');
      else { const hs = prep(plain(s.hint)); (hs.match(/=\s*\(?\d[\d.]*(?:\+\d+\/\d+)?\)?(?![\d.]*\s*[-+*/])/g) || []).forEach(x => { const v = evalE(x.replace(/^=\s*/, '')); if (v != null && Math.abs(v - qnum(s.ans)) < 1e-9) fail(seed, w, 'Hint step ' + (i + 1) + ' gives its answer away: ' + plain(s.hint)); }); }
      [places(s.ans) >= 0 ? decPlain(s.ans) : s.ans.n + '/' + s.ans.d].concat(isInt(s.ans) || places(s.ans) < 0 ? [] : [E.mixedText(s.ans)]).forEach(t => {
        const r = W.readNum(t); if (!r || !qeq(r, s.ans) || !U.numOk(s, r)) fail(seed, w, 'Hint step ' + (i + 1) + ': its answer typed as ' + t + ' is not read back'); });
      if (aAns && qeq(s.ans, aAns)) fail(seed, w, 'part (b)\'s Hint step ' + (i + 1) + ' asks for part (a)\'s answer');
    } else fail(seed, w, 'Hint step ' + (i + 1) + ' of unknown type ' + s.type);
  });
}

/* ---------- the forms: the page's hashes are exactly test_forms.js's keys */
{ const want = new Set(); ['A', 'B'].forEach(f => Object.keys(TF[f]).forEach(s => TF[f][s].forEach(k => want.add(KIT.fnv1a('a7u5|' + s + '|' + k)))));
  if (want.size !== E.FORMS_H.size || [...want].some(h => !E.FORMS_H.has(h))) fail(0, 'FORMS_H', 'the page\'s form hashes are not test_forms.js\'s keys'); }
const formKey = (slot, key) => ['A', 'B'].filter(f => (TF[f][slot] || []).indexOf(key) >= 0);

/* ---------- the page's fixed text: no number in it is a test answer (verify.py checks the forms' answers) */
const FIXED = U.notes.concat(U.notesPrint, ['', '1,2', '2 3', '((3', 'x', 'abc'].map(t => (E.readAns(t).msg || '')).filter(Boolean));

for (let seed = 1; seed <= NSETS; seed++) {
  let G; try { G = U.generate(seed); } catch (e) { fail(seed, 'generate', e.message); continue; }
  counts.sets++;
  if (G.sections.map(s => s.title).join('|') !== WANT.titles) fail(seed, 'titles', G.sections.map(s => s.title).join('|'));
  if (G.sections.map(s => s.items.length).join() !== WANT.items) fail(seed, 'questions', G.sections.map(s => s.items.length).join());
  if (G.sections.map(s => s.items.reduce((t, it) => t + E.partsOf(it).length, 0)).join() !== WANT.parts) fail(seed, 'points', 'not 10, 8, 6');
  if (G.sections.map(s => s.items.map(it => it.type).join()).join('|') !== WANT.types) fail(seed, 'types', G.sections.map(s => s.items.map(it => it.type).join()).join('|'));
  const Dm = seed <= NDUMP ? { seed, items: [] } : null;
  let qn = 0;
  G.sections.forEach(sec => sec.items.forEach(it => {
    qn++; const w = 'Q' + qn;
    let R; try { R = read(qn, it); counts.keysRead++; } catch (e) { fail(seed, w, e.message); return; }
    R.keys.forEach(([s, k]) => { const f = formKey(s, k); if (f.length) fail(seed, w, 'Form ' + f.join(' and ') + '\'s numbers: ' + s + ' ' + k); });
    if (qn === 18) { shape.mixSets++; const [pp, wh] = R.keys[0][1].split('|'); if (+pp.split(':')[+wh] === 1) shape.mixKnownOne++; }
    /* the estimate (5.06 Notes II) says the right way: more of the smaller unit, fewer of the bigger */
    if (qn === 9 || qn === 12 || qn === 13) { const p0 = it.part, f = qdec(p0.prm.f), more = qlt(Q(1), f), say = plain(C.F[p0.fam].rule(p0)) + ' ' + C.solution(p0).map(l => plain(l.say)).join(' ');
      if (/is more than/.test(say) !== more || /is fewer than/.test(say) === more) fail(seed, w, 'the estimate says the wrong way: ' + say.slice(0, 160));
      const ck = /(\d[\d,]*(?:\.\d+)?) is (more|fewer) than (\d+)\.$/.exec(say); if (!ck || (ck[2] === 'more') !== (+ck[1].replace(/,/g, '') > +ck[3])) fail(seed, w, 'the estimate\'s check is false: ' + (ck ? ck[0] : say.slice(-80))); }
    if (!C.clean(it)) fail(seed, w, 'breaks the clean rule');
    claims(seed, w, it.stem);
    const di = Dm ? { q: qn, type: it.type, fam: it.fam || null, stem: plain(it.stem), keys: R.keys, parts: [] } : null;
    if (it.type === 'mc' || it.type === 'multi') {
      if (new Set(it.opts.map(plain)).size !== it.opts.length) fail(seed, w, 'two options the same');
      it.opts.forEach((o, k) => claims(seed, w + ' option ' + LET[k], o));
      const sol = C.mcSolution(it); if (!sol || !sol.length) fail(seed, w, 'no Show me how'); else sol.forEach(l => claims(seed, w + ' Show me how', l.say));
      const st = W.stepsMC(it); if (st) checkWalk(seed, w, st, null); else fail(seed, w, 'no Hint');
      const last = st && st[st.length - 1];
      if (it.type === 'mc') {
        counts.mc++;
        if (R.correct !== it.correct) fail(seed, w, 'keyed ' + LET[it.correct] + ', the math says ' + LET[R.correct]);
        if (C.mcFeedback(it, it.correct).v !== 'right') fail(seed, w, 'the key is not marked right');
        it.opts.forEach((o, k) => { if (k === it.correct) return; const f = C.mcFeedback(it, k);
          if (f.v !== 'wrong') fail(seed, w, 'option ' + LET[k] + ' marked ' + f.v);
          else if (/^Not that one/.test(f.what[0])) fail(seed, w, 'option ' + LET[k] + ' has no named mistake'); else claims(seed, w + ' option ' + LET[k] + ' why', f.what[0]); });
        if (!last || last.type !== 'choice' || last.opts.filter(o => o.ok)[0].label !== LET[it.correct]) fail(seed, w, 'the Hint does not end on the right letter');
      } else {
        counts.multi++;
        const want = R.correct.slice().sort().join();
        if (it.correct.slice().sort().join() !== want) fail(seed, w, 'keyed ' + it.correct.join() + ', the math says ' + want);
        for (let mask = 0; mask < (1 << it.opts.length); mask++) { counts.subsets++;
          const pick = it.opts.map((o, i) => i).filter(i => mask & (1 << i)), v = C.selectFeedback(it, pick, 2).v;
          if ((v === 'right') !== (pick.join() === want)) fail(seed, w, 'the picks ' + (pick.join() || 'none') + ' are marked ' + v); }
        it.opts.forEach((o, i) => claims(seed, w + ' why', C.SELWHY[it.fam](it, i)));
        if (!last || last.type !== 'choice' || last.opts.filter(o => o.ok)[0].label !== C.lettersSay(it.correct)) fail(seed, w, 'the Hint does not end on the right letters');
      }
      if (di) { di.opts = it.opts.map(plain); di.correct = it.correct; di.sol = (sol || []).map(l => plain(l.say)); di.walk = (st || []).filter(x => x.type === 'num').map(x => ({ ask: plain(x.ask), ans: x.ans.n + '/' + x.ans.d })); }
    }
    const parts = E.partsOf(it);
    parts.forEach((p, pi) => {
      if (it.type === 'mc' || it.type === 'multi') return;
      counts.parts++;
      const pw = w + (p.label || ''), kt = U.keyText(p), a = p.ans;
      if (!qeq(a, R.ans[pi])) fail(seed, pw, 'the key ' + numStr(a) + ' is not what the question says: ' + numStr(R.ans[pi]));
      if (!p.unit && !p.pre) fail(seed, pw, 'nothing says what the answer counts');
      /* the key, typed several ways */
      const ways = [kt, ' ' + kt + '. ', kt + ' ' + (p.unit || ''), 'about ' + kt];
      if (p.pre === '$') ways.push('$' + kt);
      if (p.pre && p.pre !== '$') ways.push('k = ' + kt, 'k=' + kt);
      if (p.unit && /²$/.test(p.unit)) ways.push(kt + ' ' + p.unit.replace('²', '^2'), kt + ' sq ' + p.unit.replace('²', ''), kt + ' square feet');
      if (!isInt(a) && places(a) >= 0) ways.push(decPlain(a), a.n + '/' + a.d, E.mixedText(a));
      if (places(a) >= 0 && qnum(a) >= 1000) ways.push(numStr(a));
      if (p.money && places(a) < 2) ways.push(E.money(a));
      if (p.cups && !isInt(a)) ways.push(E.mixedText(a).replace(/ (\d+)\/(\d+)$/, (m0, n, d) => ({ '1/2': '½', '1/4': '¼', '3/4': '¾' })[n + '/' + d] || m0));
      ways.forEach(t => { counts.typedRight++; const r0 = C.feedback(p, t, {}); if (r0.v !== 'right') fail(seed, pw, 'the key typed as "' + t + '" is marked ' + r0.v + ': ' + plain((r0.what || [])[0] || '')); });
      /* not finished: the key rounded, a fraction not in simplest form, the arithmetic left undone */
      const forms = [];
      for (let dp = 0; dp < places(a); dp++) { const t = qround(a, dp); if (!qeq(t, a) && qnum(t) > 0) forms.push(decPlain(t)); }
      forms.push((2n * a.n) + '/' + (2n * a.d), (places(a) >= 0 ? decPlain(a) : a.n + '/' + a.d) + ' + 0');
      forms.forEach(t => { counts.forms++; const r = C.feedback(p, t, {}); if (r.v !== 'form') fail(seed, pw, '"' + t + '" (right, not finished) is marked ' + r.v + ': ' + plain((r.what || [])[0] || '')); });
      /* a mixed number with no space between its whole number and its fraction */
      if (p.cups && !isInt(a)) { counts.didMean++; const w0 = a.n / a.d, n0 = a.n % a.d, t = w0 + '' + n0 + '/' + a.d, r = C.feedback(p, t, {});
        if (r.v !== 'unread' || !/Did you mean/.test((r.what || [])[0] || '')) fail(seed, pw, '"' + t + '" is marked ' + r.v); }
      /* the sheet's other ratio, rounded to one, two or three places: right, with a note */
      if (p.alt) { if (!R.alt || !qeq(R.alt, p.alt)) fail(seed, pw, 'the other ratio\'s answer is not the question\'s');
        for (let dp = 1; dp <= 3; dp++) { const t = qround(p.alt, dp); let shadow = qeq(t, a); for (let d2 = 0; d2 < places(a); d2++) if (qeq(t, qround(a, d2))) shadow = true;
          if (shadow) continue; counts.alt++; const ty = E.fixed(p.alt, dp), r = C.feedback(p, ty, {});
          if (r.v !== 'right' || !/other ratio/.test(plain((r.what || [])[0] || ''))) fail(seed, pw, 'the other ratio\'s ' + ty + ' is marked ' + r.v); } }
      /* near misses and the minus sign */
      [qadd(a, Q(1)), qsub(a, Q(1)), qadd(a, Q(1, 10)), qsub(a, Q(1, 10)), qadd(a, Q(1, 100))].filter(t => qnum(t) > 0).forEach(t => {
        if (p.alt && [1, 2, 3].some(dp => qeq(t, qround(p.alt, dp)))) return;
        counts.near++; const r = C.feedback(p, typedOf(t), {}); if (r.v === 'right') fail(seed, pw, 'a near miss ' + typedOf(t) + ' is marked right'); });
      { const r = C.feedback(p, '-' + kt, {}); if (r.v !== 'wrong') fail(seed, pw, 'the key with a minus sign is marked ' + r.v); }
      /* the clean rule, here and not through C.clean: no mistake is worth the answer, no printed number is the answer */
      counts.cleanChecked++;
      const models = C.F[p.fam].models(p) || [];
      if (models.some(m => qeq(m.v, a))) fail(seed, pw, 'a modelled mistake is worth the answer');
      if (C.printedNumbers(it).some(x => qeq(x, a))) fail(seed, pw, 'the answer is printed in the question');
      parts.forEach(o => { if (o !== p && qeq(o.ans, a)) fail(seed, pw, 'two parts have the same answer'); });
      /* every modelled mistake, typed, is wrong and named */
      models.forEach(m => {
        counts.models++;
        const typed = typedOf(m.v), f = C.feedback(p, typed, {});
        if (f.v !== 'wrong') fail(seed, pw, 'the mistake "' + typed + '" (' + plain(m.say) + ') is marked ' + f.v + ': ' + plain((f.what || [])[0] || ''));
        else if (plain(f.what[0]).indexOf(plain(m.say).replace(/\.$/, '').slice(0, 40)) < 0) fail(seed, pw, 'the mistake "' + typed + '" is not named: ' + plain(f.what[0]));
        if (m.step != null && !(m.step >= 0 && m.step < C.solution(p).length)) fail(seed, pw, 'a mistake points at worked line ' + m.step + ' of ' + C.solution(p).length);
        claims(seed, pw + ' mistake', m.say);
      });
      /* follow-through (ruling 19; the test's 6(b) from 6(a) and 16(b) from 16(a)), worked out here from the question's words */
      if (!!C.F[p.fam].follow !== !!(pi > 0 && R.follow)) fail(seed, pw, 'follow-through ' + (C.F[p.fam].follow ? 'offered where the test has none' : 'missing'));
      if (pi > 0 && R.follow) {
        const pa = parts[0];
        [qadd(pa.ans, Q(10)), qmul(pa.ans, Q(2)), qadd(pa.ans, Q(1, 2))].forEach(wrongA => {
          const want = R.follow(wrongA); if (qeq(want, a)) return;
          counts.follow++;
          const f = C.feedback(p, typedOf(want), { prev: decPlain(wrongA), prevPart: pa, mode: 'check' });
          if (!/Your method for this part is right/.test(plain((f.what || [])[0] || ''))) fail(seed, pw, 'follow-through from part (a) = ' + decPlain(wrongA) + ' is not recognised: ' + plain((f.what || [])[0] || ''));
          const ft = C.feedback(p, typedOf(want), { prev: decPlain(wrongA), prevPart: pa, mode: 'test' });
          if (ft.v !== 'right' || !ft.follow) fail(seed, pw, 'follow-through in "Like the real test" is marked ' + ft.v);
        });
      }
      /* Show me how: every worked line carries the answer */
      const sol = C.solution(p);
      if (!sol || !sol.length) fail(seed, pw, 'no Show me how');
      else sol.forEach((l, i) => { claims(seed, pw + ' Show me how', l.say + (l.ex ? ' ' + l.ex.h : '')); if (l.ex) { counts.solLines++; if (!qeq(l.ex.v, a)) fail(seed, pw, 'worked line ' + (i + 1) + ' is worth something else'); } });
      if (!sol.some(l => l.ex)) fail(seed, pw, 'Show me how never reaches the answer');
      claims(seed, pw + ' rule', C.F[p.fam].rule(p));
      /* the Hint; a part (b) never asks for part (a)'s number */
      const st = W.steps(p); checkWalk(seed, pw, st, a, pi > 0 ? parts[0].ans : null);
      const lastNum = st.filter(x => x.type === 'num').pop(); if (!lastNum || !qeq(lastNum.ans, a)) fail(seed, pw, 'the Hint does not end on the answer');
      if (di) di.parts.push({ label: p.label || '', fam: p.fam, stem: plain(p.stem), unit: p.unit || null, pre: p.pre || null, key: plain(E.ansHtml(p)), keyText: kt, ans: a.n + '/' + a.d,
        alt: p.alt ? p.alt.n + '/' + p.alt.d : null, sol: sol.map(l => ({ say: plain(l.say), h: l.ex ? plain(l.ex.h) : null })),
        walk: st.filter(x => x.type === 'num').map(x => ({ ask: plain(x.ask), ans: x.ans.n + '/' + x.ans.d })), rule: plain(C.F[p.fam].rule(p)),
        models: models.map(m => ({ say: plain(m.say), v: m.v.n + '/' + m.v.d })) });
    });
    if (di) Dm.items.push(di);
  }));
  if (Dm) dump.push(Dm);
}
if (shape.mixSets && shape.mixKnownOne > 0.6 * shape.mixSets) fail(0, 'Q18', 'the known part is 1 in ' + shape.mixKnownOne + ' of ' + shape.mixSets + ' sets: the clean rule is hiding a key that is right only then');
fs.writeFileSync(path.join(__dirname, 'dump.json'), JSON.stringify({ TITLES: E.TITLES, fixed: FIXED.map(plain), sets: dump }));
console.log(counts.sets + ' sets: ' + counts.keysRead + ' questions read back, ' + counts.parts + ' typed parts, ' + counts.typedRight + ' keys typed, ' + counts.forms + ' "Almost" forms, ' + counts.didMean + ' mixed numbers run together, ' +
  counts.alt + ' other-ratio answers, ' + counts.models + ' mistakes typed, ' + counts.near + ' near misses, ' + counts.follow + ' follow-throughs, ' + counts.solLines + ' worked lines, ' + counts.walkSteps + ' Hint steps, ' +
  counts.mc + ' multiple choice, ' + counts.multi + ' select-all (' + counts.subsets + ' subsets), ' + counts.claims + ' arithmetic claims; ' + NDUMP + ' sets written to dump.json');
if (nfail) { console.log(nfail + ' PROBLEMS'); fails.forEach(f => console.log('  ' + f)); process.exit(1); }
console.log('u5_check: ALL SOUND');
