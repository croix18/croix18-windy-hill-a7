/* A7 Unit 11 practice: every generated question read back from its PRINTED WORDS and worked again here, with this file's own
   reader and its own exact arithmetic (nothing of the engine's solver is used).   node u11_check.js [sets=3000] [dumped=1500]
   For every set: the shape of the test (section titles and points read from build/u11/unit.py: 14 questions, 18 points); every
   equation solved again from its printed text (polynomials in the letter and the box, exactly); every key typed back, in several
   forms, is right; every modelled mistake typed is wrong and named; every worked line is an equation with the same solutions
   as the first (no false equation printed as a line of work — a false ending is said in words, "1 = 5 — never true"); every
   Hint number step's answer is the arithmetic it asks, no Hint states its own answer, every Hint choice has one right option
   and a reason for each wrong one; every arithmetic claim in every sentence is true ("2(4(−1) + 9) − 5(−1) = 15"); every ordered
   pair of Q8 and Q9 put into both equations; every line of every graph read back from its SVG onto its own equation, inside the
   window, the crossing inside it; every table value; Q14(b)'s tolerance (the exact crossing between the grid lines, the key's
   estimate within it, the swapped pair and the nearest grid point outside it); no × and no "slope" or "intercept" anywhere a
   student reads; every wrong choice named. dump.json goes to verify.py, the sympy oracle. */
'use strict';
const E = require('./engine.js'), C = require('./coach.js'), U = require('./unit.js'), FG = require('./fig.js'), W = C.Walk;
const fs = require('fs'), path = require('path');
const NSETS = +(process.argv[2] || 3000), NDUMP = Math.min(NSETS, +(process.argv[3] || 1500));
let nfail = 0; const fails = [];
const fail = (seed, where, what) => { nfail++; if (fails.length < 60) fails.push(seed + ' ' + where + ': ' + what); };
const counts = { sets: 0, eqs: 0, keys: 0, models: 0, lines: 0, steps: 0, claims: 0, pairs: 0, figs: 0, segs: 0, tables: 0, mc: 0 };

/* ------------------------------------------------------------------ this file's own exact arithmetic */
const g = (a, b) => { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) [a, b] = [b, a % b]; return a; };
const R = (n, d = 1n) => { n = BigInt(n); d = BigInt(d); if (d === 0n) throw new Error('/0'); if (d < 0n) { n = -n; d = -d; } const k = g(n, d) || 1n; return [n / k, d / k]; };
const ad = (a, b) => R(a[0] * b[1] + b[0] * a[1], a[1] * b[1]), mu = (a, b) => R(a[0] * b[0], a[1] * b[1]), ng = a => R(-a[0], a[1]);
const dv = (a, b) => R(a[0] * b[1], a[1] * b[0]), eqr = (a, b) => a[0] === b[0] && a[1] === b[1], fl = a => Number(a[0]) / Number(a[1]);
const dec = s => { const m = /^(\d*)(?:\.(\d+))?$/.exec(s); const f = m[2] || ''; return R(BigInt((m[1] || '0') + f), 10n ** BigInt(f.length)); };
/* polynomials: monomial (sorted letters, '' for a number) → rational */
const P = (m, c) => new Map([[m, c]]);
const padd = (A, B) => { const o = new Map(A); B.forEach((c, m) => { const v = o.has(m) ? ad(o.get(m), c) : c; if (v[0] === 0n) o.delete(m); else o.set(m, v); }); return o; };
const pmul = (A, B) => { let o = new Map(); A.forEach((a, ma) => B.forEach((b, mb) => { o = padd(o, P((ma + mb).split('').sort().join(''), mu(a, b))); })); return o; };
const pneg = A => { const o = new Map(); A.forEach((c, m) => o.set(m, ng(c))); return o; };
/* a printed expression → polynomial: numbers, one-letter variables, the box (B), + −, ·, /, implicit products, parentheses */
function plainOf(h) {
  return String(h).replace(/<span class="fr"><span class="nu">([^<]*)<\/span><span class="de">([^<]*)<\/span><\/span>/g, '(($1)/($2))').replace(/<svg[\s\S]*?<\/svg>/g, ' ')
    .replace(/<[^>]+>/g, '').replace(/&nbsp;| /g, ' ').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim();
}
function readPoly(s) {
  const t = s.replace(/−/g, '-').replace(/[½⅓⅔¼¾⅕⅖⅗⅘]/g, c => ({'½':'(1/2)','⅓':'(1/3)','⅔':'(2/3)','¼':'(1/4)','¾':'(3/4)','⅕':'(1/5)','⅖':'(2/5)','⅗':'(3/5)','⅘':'(4/5)'})[c]).replace(/·/g, '*').replace(/÷/g, '/').replace(/□/g, 'B').replace(/\s+/g, '');
  let i = 0;
  const peek = () => t[i];
  function expr() { let a = term(); for (;;) { if (peek() === '+') { i++; a = padd(a, term()); } else if (peek() === '-') { i++; a = padd(a, pneg(term())); } else return a; } }
  function term() { let a = unary(); for (;;) { const c = peek(); if (c === '*') { i++; a = pmul(a, unary()); } else if (c === '/') { i++; const b = unary(); if (b.size !== 1 || !b.has('')) throw new Error('/'); a = pmul(a, P('', dv(R(1), b.get('')))); } else if (c && /[\d.(a-zB]/.test(c)) a = pmul(a, atom()); else return a; } }
  function unary() { if (peek() === '-') { i++; return pneg(unary()); } if (peek() === '+') { i++; return unary(); } return atom(); }
  function atom() { const c = peek(); if (c === undefined) throw new Error('end');
    if (/[\d.]/.test(c)) { const m = /^\d*\.?\d+|^\d+/.exec(t.slice(i)); i += m[0].length; return P('', dec(m[0])); }
    if (c === '(') { i++; const e = expr(); if (peek() !== ')') throw new Error(')'); i++; return e; }
    if (/[a-zB]/.test(c)) { i++; return P(c, R(1)); }
    throw new Error('char ' + c); }
  const e = expr(); if (i !== t.length) throw new Error('left: ' + t.slice(i)); return e;
}
const coef = (A, m) => A.get(m) || R(0);
/* an equation "L = R" in one letter → {kind: one|none|all, s} */
function solveText(txt, v) {
  const [L, Rr] = txt.split('='), d = padd(readPoly(L), pneg(readPoly(Rr)));
  [...d.keys()].forEach(m => { if (m !== '' && m !== v) throw new Error('monomial ' + m); });
  const a = coef(d, v), b = coef(d, '');
  if (a[0] === 0n) return { kind: b[0] === 0n ? 'all' : 'none' };
  return { kind: 'one', s: dv(ng(b), a) };
}
/* a line "y = …" → [m, b] */
function lineOf(txt) { const m = /^y\s*=\s*(.+)$/.exec(txt.trim()); if (!m) throw new Error('not a line: ' + txt); const p = readPoly(m[1]); [...p.keys()].forEach(k => { if (k !== '' && k !== 'x') throw new Error('line ' + txt); }); return [coef(p, 'x'), coef(p, '')]; }
const at = (l, x) => ad(mu(l[0], x), l[1]);
const on = (l, x, y) => eqr(at(l, x), y);
const sameR = (a, q) => a[0] === q.n && a[1] === q.d;
const numR = s => { s = s.replace(/−/g, '-').trim(); const neg = s[0] === '-'; if (neg) s = s.slice(1); const m = /^\(\((\d+)\)\/\((\d+)\)\)$/.exec(s); const v = m ? R(m[1], m[2]) : /\//.test(s) ? R(s.split('/')[0], s.split('/')[1]) : dec(s); return neg ? ng(v) : v; };
/* the math runs of a printed stem, in order */
const mathRuns = h => [...String(h).matchAll(/<span class="m"[^>]*>([\s\S]*?)<\/span>(?=[^<]*(?:<|$))/g)].map(m => plainOf(m[1]));
function mathSpans(h) {                                                     /* the kit's math spans, whole (they may hold a fraction) */
  const out = [], s = String(h); let k = 0;
  while ((k = s.indexOf('<span class="m"', k)) >= 0) { let depth = 0, j = k; const re = /<span\b|<\/span>/g; re.lastIndex = k;
    let m; while ((m = re.exec(s))) { if (m[0] === '</span>') { depth--; if (!depth) { j = re.lastIndex; break; } } else depth++; }
    out.push(plainOf(s.slice(s.indexOf('>', k) + 1, j - 7))); k = j; }
  return out;
}

/* ------------------------------------------------------------------ sentences: every arithmetic claim true; no ×, no slope */
/* ruling 43, read from the words: an equation's printed numbers and its ending; a system's two lines; a story's numbers —
   against shown.js (written from the specs by shown43.py; verify.py reads the specs again itself) */
const SH = require('./shown.js'), SH_EQ = new Set(SH.eq), SH_SYS = new Set(SH.sys);
const kq = r => { const q = E.Q(r[0], r[1]); return E.kstr(q); };
function eqKey43(t, v, box) { const nums = (t.replace(/½/g, '(1/2)').match(/\d+(?:\.\d+)?/g) || []).map(x => E.kstr(E.qdec(x))).sort(); if (box) return nums.join(',') + '|box'; const e = solveText(t, v); return nums.join(',') + '|' + (e.kind === 'one' ? kq(e.s) : e.kind); }
const sysKey43 = (a, b) => [kq(a[0]) + ',' + kq(a[1]), kq(b[0]) + ',' + kq(b[1])].sort().join(';');
const story43 = nums => SH.story.some(set => { const pool = set.slice(); return nums.every(x => { const i = pool.indexOf(x); if (i < 0) return false; pool.splice(i, 1); return true; }); });
function held43(seed, w, o) { counts.r43 = (counts.r43 || 0) + 1;
  (o.eqs || []).forEach(([t, v, box]) => { if (SH_EQ.has(eqKey43(t, v, box))) fail(seed, w, 'ruling 43: a lesson, the review or the paper showed ' + t); });
  if (o.lines && SH_SYS.has(sysKey43(o.lines[0], o.lines[1]))) fail(seed, w, 'ruling 43: a lesson, the review or the paper showed this system');
  if (o.story && story43(o.story.map(String))) fail(seed, w, 'ruling 43: a lesson, the review or the paper told this story: ' + o.story); }
const BANNED = /×|\bslopes?\b|intercept/i;
function words(seed, w, h) {
  const t = plainOf(h);
  if (BANNED.test(t)) fail(seed, w, 'a student reads "×", "slope" or "intercept": ' + t.slice(0, 140));
  /* a chain of numeric expressions joined by =, with no letter touching it */
  /* a full stop ends a sentence, never a decimal point (always a digit after it): made a ';' so that a claim which ends its
     sentence is read, not skipped, and two sentences are never one claim (14 Nov 2026) */
  const s = t.replace(/−/g, '-').replace(/\.(?=\s|$)/g, ';');
  const re = /[\d.()+\-*/½⅓⅔¼¾⅕⅖⅗⅘·÷\s]*\d[\d.()+\-*/½⅓⅔¼¾⅕⅖⅗⅘·÷\s=]*/g; let m;
  while ((m = re.exec(s))) {
    const run = m[0]; if (run.indexOf('=') < 0) continue;
    const before = s.slice(0, m.index).replace(/\s+$/, ''), after = s.slice(m.index + run.length);
    if (/\bleft is$/.test(before)) continue;                          /* "What is left is 38 = −4": the ending quoted, then judged in words */
    if (/(^|[^A-Za-z])[A-Za-z]$|[□’']$/.test(before) || /^[A-Za-z□](?![A-Za-z])/.test(after.replace(/^\s+/, ''))) continue;      /* a letter touching it: part of an equation, not arithmetic */
    const segs = run.split('=').map(x => x.trim().replace(/^[(]+(?=[^)]*$)/, '').replace(/(?<=^[^(]*)[)]+$/, ''));
    if (segs.some(x => !x)) continue;
    let vals; try { vals = segs.map(x => { const p = readPoly(x); if (p.size > 1 || (p.size === 1 && !p.has(''))) throw 0; return coef(p, ''); }); } catch (e) { continue; }
    counts.claims++;
    const sentence = (s.slice(m.index + run.length).split(/[.;]/)[0] || '');
    const neverSaid = /^[\s,]*(?:is left\s*)?(?:—\s*|is\s+)?never true/.test(after);
    const allEq = vals.every(v => eqr(v, vals[0]));
    if (neverSaid ? allEq : !allEq) fail(seed, w, 'a claim is ' + (neverSaid ? 'said to be never true but is true' : 'false') + ': ' + run.trim() + '  «' + t.slice(0, 140) + '»');
  }
}

/* ------------------------------------------------------------------ the test's shape, from its spec */
const SPEC = fs.readFileSync(path.join(__dirname, '..', '..', 'build', 'u11', 'unit.py'), 'utf8');
const TEST_TITLES = [...SPEC.matchAll(/dict\(title="([^"]+)", benchmark="MA\.8\.AR\.\d\.\d", items=_ar\d\d\(\)\)/g)].map(m => m[1]);
if (TEST_TITLES.length !== 4) { console.log('could not read the test\'s four section titles from unit.py'); process.exit(1); }
const TRACK = /tracker=\{"MA\.8\.AR\.2\.1": (\d+), "MA\.8\.AR\.4\.1": (\d+), "MA\.8\.AR\.4\.2": (\d+), "MA\.8\.AR\.4\.3": (\d+)\}/.exec(SPEC).slice(1).map(Number);
/* >>> THE PAPER'S SHAPE AND WORDS, BY HAND — update here when unit.py's practice paper changes. The section titles above are
   read from unit.py (any wording; the page's must match them). Since the review pass of 14 Nov 2026 the paper is in FAST's
   house style, and each question's own words are held here: `paper` is a phrase of unit.py's question (it must still be in
   unit.py — if the paper is reworded this check fails and says which, so this table is brought up to date), `page` is what
   the page's stem must say for that question (a pattern; the page's numbers are its own). Q8 is "Select all the systems that
   have (a, b) as a solution" (five systems, two or three right); Q9's four options are a verdict with a claim about the pair
   (both / only the first / only the second / neither), exactly one of them true; Q14's two graphs are captioned "PART (a)" and
   "PART (b): a different system". <<< */
const WANT = { items: '7,2,2,3', points: TRACK.join(','), types: 'solo,solo,solo,solo,parts,solo,solo|multi,mc|mc,mc|solo,parts,parts',
  words: [
    [1, 'An equation is shown.', /^An equation is shown\.\s*.+?\s*What value of [a-z] makes the equation true\?$/],
    [2, 'What value of " + v + " makes the equation true?', /^An equation is shown\.\s*.+?\s*What value of [a-z] makes the equation true\?$/],
    [3, 'An equation is shown.', /^An equation is shown\.\s*.+?\s*What value of [a-z] makes the equation true\?$/],
    [4, 'An equation is shown.', /^An equation is shown\.\s*.+?\s*What value of [a-z] makes the equation true\?$/],
    [5, 'Each equation has one solution, no solution or infinitely many solutions. Which? If it has one solution, find it.', /^Each equation has one solution, no solution or infinitely many solutions\. Which\? If it has one solution, find it\.$/],
    [6, 'Complete the equation so that it has no solution. What number goes in the box?', /^Complete the equation so that it has (?:no solution|infinitely many solutions)\. What number goes in the box\?\s*.+$/],
    [7, 'After how many months will the two companies have cost the same?', /\. After how many (?:months|visits|hours|classes) will the two (?:companies|gyms|ways|shops|plans) have cost the same\?$/],
    [8, 'Select all the systems that have', /^Select all the systems that have \(.+\) as a solution\.$/],
    [9, 'a solution of the system', /^Is \(.+\) a solution of the system y = .+ and y = .+\?$/],
    [10, 'The graphs of the system', /^The graphs of the system y = .+ and y = .+ are shown\. How many solutions does the system have\?$/],
    [11, 'are shown. How many solutions does the system have?', /^The graphs of the system y = .+ and y = .+ are shown\. (?:Both equations graph as the one line shown\. )?How many solutions does the system have\?$/],
    [12, 'What is the solution of the system? Give its x and its y.', /^A system of equations is graphed: y = .+ and y = .+\. What is the solution of the system\? Give its x and its y\.$/],   /* the paper's last sentence too since 15 Nov 2026 (two boxes) */
    [13, 'The tables are for', /^The tables are for y = .+ and y = .+\.$/],
    [14, 'The PART (a) graph shows', /^\w+(?: has|’s plant is) .+ each week\. \w+(?: has|’s plant is) .+ each week\.$/]],
  parts: [[13, 'a', 'What number is missing from the table for', /^What number is missing from the table for y = .+\?$/], [13, 'b', 'What is the solution of the system?', /^What is the solution of the system\?$/],
    [14, 'a', 'After how many weeks will', /^The PART \(a\) graph shows (?:the dollars y each has|the height y, in centimeters, of each plant) after x weeks\. After how many weeks will .+\?$/],
    [14, 'b', 'a different system', /^The PART \(b\) graph shows a different system, y = .+ and y = .+\. Estimate its point of intersection to the nearest tenth\.$/]],
  captions: [['PART (a):  Mia and Leo', /^PART \(a\): \w+ and \w+$/], ['PART (b):  a different system', /^PART \(b\): a different system$/]],
  q9claims: ['Yes — it makes both equations true.', 'No — it makes only E true.', 'No — it makes only E true.', 'No — it makes neither equation true.'] };
{ const gone = WANT.words.map(w => w[1]).concat(WANT.parts.map(w => w[2]), WANT.captions.map(w => w[0])).filter(ph => SPEC.indexOf(ph) < 0);
  if (gone.length) { console.log('unit.py\'s practice paper no longer says: ' + gone.map(g => '"' + g + '"').join(', ') + ' — update THE PAPER\'S SHAPE AND WORDS in u11_check.js'); process.exit(1); } }
const wordsOk = (seed, w, h, re) => { const t = plainOf(h); if (!re.test(t)) fail(seed, w, 'not the paper\'s words (' + re + '): ' + t.slice(0, 160)); };
/* Q9: an option read as a verdict and a claim about the pair, and judged true or false against the two equations */
function q9Claim(o, lines, t) {
  const m = /^(Yes|No) — it makes (.+?)\.$/.exec(o); if (!m) throw new Error('an option is not a verdict with its claim: ' + o);
  const yes = m[1] === 'Yes', c = m[2], idx = e => lines.findIndex(L => L === e);
  let claim;
  if (c === 'both equations true') claim = t[0] && t[1];
  else if (c === 'neither equation true') claim = !t[0] && !t[1];
  else { const mm = /^(only )?(y = .+) (true|false)$/.exec(c); if (!mm) throw new Error('an option\'s claim is not read: ' + o);
    const i = idx(mm[2]); if (i < 0) throw new Error('an option names an equation not in the system: ' + mm[2]);
    claim = mm[3] === 'true' ? t[i] && (!mm[1] || !t[1 - i]) : !t[i] && !mm[1]; }
  return { yes, claim, whole: claim && yes === (t[0] && t[1]) };     /* an option is true when its claim is, and its verdict is too */
}

/* ------------------------------------------------------------------ the figures, read back from their SVG */
function readPlane(seed, w, html, lines, want) {
  const sv = /<svg class="fig plane"[^>]*data-win="([^"]+)" data-px="([^"]+)"/.exec(html);
  if (!sv) { fail(seed, w, 'no plane'); return; }
  counts.figs++;
  const [x0, x1, y0, y1, ys] = sv[1].split(' ').map(Number), k = Number(sv[2]);
  const toX = px => x0 + px / k, toY = py => y1 - py / k * ys;
  const segs = [...html.matchAll(/<line class="(ln[12])" data-line="(\d)" x1="([-\d.]+)" y1="([-\d.]+)" x2="([-\d.]+)" y2="([-\d.]+)"\/>/g)];
  if (segs.length !== want.n) fail(seed, w, segs.length + ' lines drawn, not ' + want.n);
  segs.forEach(sg => { counts.segs++;
    const i = +sg[2], l = lines[i], cls = sg[1]; if (cls !== (i ? 'ln2' : 'ln1')) fail(seed, w, 'line ' + i + ' is not ' + (i ? 'dashed' : 'solid'));
    const ends = [[+sg[3], +sg[4]], [+sg[5], +sg[6]]].map(([a, b]) => [toX(a), toY(b)]);
    const tolx = 0.06 / k * 1.0 + 0.002, toly = 0.06 / k * ys + 0.002 * ys;
    ends.forEach(([X, Y]) => {
      const yl = fl(l[0]) * X + fl(l[1]);
      if (Math.abs(yl - Y) > (Math.abs(fl(l[0])) + 1) * 0.06 / k * Math.max(1, ys) + 1e-6) fail(seed, w, 'line ' + i + ' is not drawn on its equation: (' + X.toFixed(3) + ', ' + Y.toFixed(3) + ')');
      if (X < x0 - 0.01 || X > x1 + 0.01 || Y < y0 - 0.01 * ys || Y > y1 + 0.01 * ys) fail(seed, w, 'line ' + i + ' leaves the window');
      const edge = Math.abs(X - x0) < 0.02 || Math.abs(X - x1) < 0.02 || Math.abs(Y - y0) < 0.02 * ys || Math.abs(Y - y1) < 0.02 * ys;
      if (!edge) fail(seed, w, 'line ' + i + ' stops inside the window');
    });
    if (Math.hypot(ends[1][0] - ends[0][0], (ends[1][1] - ends[0][1]) / ys) < 1.9) fail(seed, w, 'line ' + i + ' shows too little of itself');
  });
  if (want.cross) { const [cx, cy] = want.cross.map(fl); if (cx < x0 + 0.5 || cx > x1 - 0.5 || cy < y0 + 0.5 * ys || cy > y1 - 0.5 * ys) fail(seed, w, 'the crossing is not well inside the window'); }
  if (!(x0 <= 0 && 0 <= x1 && y0 <= 0 && 0 <= y1)) fail(seed, w, 'the window leaves out the origin');
  /* the axes' numbers: every 1 or 2 */
  const ticks = [...html.matchAll(/<text class="tick" x="([-\d.]+)" y="([-\d.]+)">([^<]+)<\/text>/g)];
  if (ticks.length < 4) fail(seed, w, 'too few axis numbers');
  ticks.forEach(t => { const px = +t[1], py = +t[2], v = Number(t[3].replace('−', '-'));
    const isX = Math.abs(py - ((y1 - y0) / ys * k + 12)) < 0.2, val = isX ? toX(px) : toY(py);
    if (Math.abs(val - v) > 0.06 / k * ys + 1e-9) fail(seed, w, 'an axis number ' + t[3] + ' sits at ' + val.toFixed(3)); });
  const xs = ticks.filter(t => Math.abs(+t[2] - ((y1 - y0) / ys * k + 12)) < 0.2).map(t => Number(t[3].replace('−', '-'))).sort((a, b) => a - b);
  if (xs.some((v, i) => i && v - xs[i - 1] > 2)) fail(seed, w, 'the x-axis numbers skip more than 2');
  if (k < 14) fail(seed, w, 'a grid square is ' + k.toFixed(1) + ' px: too small to read on a phone');
  if (!/<div class="lgd">/.test(html)) fail(seed, w, 'no legend');
}
function readTables(seed, w, html) {
  const tabs = [...html.matchAll(/<table class="vt"><caption>([\s\S]*?)<\/caption>([\s\S]*?)<\/table>/g)];
  return tabs.map(t => { const rows = [...t[2].matchAll(/<tr>([\s\S]*?)<\/tr>/g)].map(r => [...r[1].matchAll(/<td>([\s\S]*?)<\/td>/g)].map(c => /class="gap"/.test(c[1]) ? null : numR(plainOf(c[1]))));
    return { title: plainOf(t[1]), xs: rows[0], ys: rows[1] }; });
}

/* ------------------------------------------------------------------ a typed part's key typed back; its mistakes typed */
const kt = q => q.d === 1n ? String(q.n) : E.places(q) >= 0 ? E.decPlain(q) : q.n + '/' + q.d;
function typeBack(seed, w, p) {
  const right = t => { const r = U.judge.text(p, t); counts.keys++; if (r.v !== 'right') fail(seed, w, 'the key typed "' + t + '" is ' + r.v + ': ' + (r.what || []).join(' ')); };
  const wrong = (t, named) => { const r = U.judge.text(p, t); counts.models++; (r.what || []).forEach(x => words(seed, w + ' "' + t + '"', x)); if (r.v === 'right') fail(seed, w, 'a mistake typed "' + t + '" is marked right'); else if (named && !/That is what you get if you/.test((r.what || []).join(' '))) fail(seed, w, 'the mistake "' + t + '" is not named: ' + (r.what || []).join(' ')); };
  right(U.keyText(p));
  if (p.kind === 'num') {
    if (p.v) { right(p.v + ' = ' + kt(p.ans)); right(kt(p.ans) + ' = ' + p.v); }
    if (p.unit) right(kt(p.ans) + ' ' + p.unit);
    const f = C.F[p.fam].models(p).filter(m => !E.qeq(m.v, p.ans));
    f.forEach(m => wrong(E.places(m.v) >= 0 ? kt(m.v) : (Math.round(E.qnum(m.v) * 100) / 100).toFixed(2), true));
    if (p.ans.n !== 0n) wrong(kt(E.qneg(p.ans)), false);
    /* the sign help (14 Nov 2026): it names the places in THIS equation's work where a negative is — each with its value, read
       by words() — or, if it says the work never makes one, no minus sign is printed in the equation or any worked line */
    f.filter(m => m.sign).forEach(m => { const said = plainOf(m.say), work = [p.eq ? E.eqT(p.eq) : ''].concat(U.solution(p, 'text').map(l => plainOf(l.say) + ' ' + (l.ex && typeof l.ex === 'object' ? plainOf(E.eqH(l.ex)) : ''))).join(' ');
      if (/never makes/.test(said)) { if (/−/.test(work)) fail(seed, w, 'the sign help says the work makes no negative, but it does: ' + work.slice(0, 160)); }
      else if (!/signs? to watch in this equation: where|signs? to watch in this equation: in the division/.test(said)) fail(seed, w, 'the sign help names no place: ' + said);
      counts.signs = (counts.signs || 0) + 1; });
    wrong(kt(E.qadd(p.ans, E.Q(1))), false);
  } else {
    /* two boxes since 15 Nov 2026 (the kit's several boxes in one part): x = ▢ and y = ▢ (Q12, Q13(b)), x ≈ ▢ and y ≈ ▢ (Q14(b)),
       after ▢ weeks and $▢ each / ▢ cm tall (Q14(a)) — one point, judged together; every answer typed as one string per box */
    const [x, y] = p.ans, B = U.view.boxes(p), story = p.kind === 'story', dol = story && p.st.unit === 'dollars';
    if (!B || B.length !== 2) { fail(seed, w, 'a part of two numbers without its two boxes'); return; }
    const labs = B.map(b => plainOf((b.pre || '') + ' ▢ ' + (b.unit || '')).replace(/\s+/g, ' ').trim());
    const wantLabs = story ? ['after ▢ weeks', dol ? '$ ▢ each' : '▢ cm tall'] : p.fam === 'estimate' ? ['x ≈ ▢', 'y ≈ ▢'] : ['x = ▢', 'y = ▢'];
    if (JSON.stringify(labs) !== JSON.stringify(wantLabs)) fail(seed, w, 'the boxes are labeled ' + JSON.stringify(labs) + ', not ' + JSON.stringify(wantLabs));
    if (B.some(b => !b.say)) fail(seed, w, 'a box has no name for a screen reader');
    if (JSON.stringify(U.keyText(p)) !== JSON.stringify([kt(x), kt(y)])) fail(seed, w, 'the two boxes\' keys are ' + JSON.stringify(U.keyText(p)));
    const neg = t => t.replace(/^-/, '−');
    right([kt(x), ' ' + kt(y) + ' ']); right([neg(kt(x)), neg(kt(y))]);
    if (story) { right([kt(x) + ' weeks', dol ? '$' + kt(y) : kt(y) + ' cm']); if (!dol) right([kt(x), kt(y) + ' cm tall']); }
    else right(['x = ' + kt(x), 'y = ' + kt(y)]);
    /* never right: a box holding the other's letter or unit, both numbers in one box, a box left empty */
    const bad = story ? [['$' + kt(x), kt(y)], [kt(x) + ', ' + kt(y), kt(y)], [kt(x), ''], ['', kt(y)]] : [['y = ' + kt(x), kt(y)], [kt(x), 'x = ' + kt(y)], [kt(x) + ', ' + kt(y), kt(y)], ['(' + kt(x) + ', ' + kt(y) + ')', ''], [kt(x), ''], ['', kt(y)]];
    bad.forEach(t => { const r = U.judge.text(p, t); counts.models++; if (r.v === 'right' || r.v === 'wrong') fail(seed, w, 'the boxes ' + JSON.stringify(t) + ' are ' + r.v + ' (they must be unread, not a try)'); (r.what || []).forEach(z => words(seed, w + ' ' + JSON.stringify(t), z)); });
    if (U.judge.text(p, ['', '']).v !== 'blank') fail(seed, w, 'two empty boxes are not blank');
    C.PF[p.fam].models(p).forEach(m => { if (E.qeq(m.v[0], x) && E.qeq(m.v[1], y)) return; wrong([kt(m.v[0]), kt(m.v[1])], true); });
    if (p.fam === 'estimate') {
      /* the lead's ruling (14 Nov 2026), the paper's: right when each coordinate is within 0.1 of the KEY (the crossing rounded to
         the tenth), inclusive — every tenth from key − 0.2 to key + 0.2 in each coordinate typed, box by box, and judged as that rule says */
      const K = p.ans.map(q => Math.round(E.qnum(q) * 10));
      for (let a = -2; a <= 2; a++) for (let b2 = -2; b2 <= 2; b2++) { const X = (K[0] + a) / 10, Y = (K[1] + b2) / 10, inside = Math.abs(a) <= 1 && Math.abs(b2) <= 1;
        const r = U.judge.text(p, [String(X), String(Y)]); if ((r.v === 'right') !== inside) fail(seed, w, 'x ≈ ' + X + ', y ≈ ' + Y + ' is ' + r.v + ' but is ' + (inside ? 'inside' : 'outside') + ' the range'); }
      [[0.05, 0.05], [-0.1, 0.1], [0.11, 0], [0, -0.11]].forEach(([a, b2]) => { const X = +(K[0] / 10 + a).toFixed(2), Y = +(K[1] / 10 + b2).toFixed(2), inside = Math.abs(a) <= 0.1 && Math.abs(b2) <= 0.1;
        const r = U.judge.text(p, [String(X), String(Y)]); if ((r.v === 'right') !== inside) fail(seed, w, 'x ≈ ' + X + ', y ≈ ' + Y + ' is ' + r.v + ' but is ' + (inside ? 'inside' : 'outside') + ' the range'); });
      if (E.qnum(p.tol) !== 0.1) fail(seed, w, 'the tolerance is not 0.1');
      /* one box right and the other wrong is wrong, and says which */
      const offx = String((K[0] + 5) / 10), offy = String((K[1] + 5) / 10);
      [[[String(K[0] / 10), offy], /Your x is a good estimate/], [[offx, String(K[1] / 10)], /Your y is a good estimate/]].forEach(([t, re]) => { const r = U.judge.text(p, t); counts.models++;
        if (r.v !== 'wrong') fail(seed, w, JSON.stringify(t) + ' (one box right) is ' + r.v); else if (!re.test((r.what || []).join(' ')) && !/That is what you get if you/.test((r.what || []).join(' '))) fail(seed, w, JSON.stringify(t) + ' does not say which box is right: ' + (r.what || []).join(' ')); });
    } else {
      wrong([kt(y), kt(x)], !E.qeq(x, y));
      /* one box right and the other wrong: wrong, and (unless it is a named mistake) it says which box is right */
      const ox = E.qadd(x, E.Q(7)), oy = E.qadd(y, E.Q(7));
      [[[kt(x), kt(oy)], story ? /The weeks are right/ : /Your x is right/], [[kt(ox), kt(y)], story ? /not the same yet/ : /Your y is right/]].forEach(([t, re]) => { const r = U.judge.text(p, t); counts.models++; (r.what || []).forEach(z => words(seed, w + ' ' + JSON.stringify(t), z));
        if (r.v !== 'wrong') fail(seed, w, JSON.stringify(t) + ' (one box right) is ' + r.v); else if (!re.test((r.what || []).join(' ')) && !/That is what you get if you/.test((r.what || []).join(' '))) fail(seed, w, JSON.stringify(t) + ' does not say which box is right: ' + (r.what || []).join(' ')); });
    }
  }
}

/* ------------------------------------------------------------------ the help: worked lines, Hint steps */
function checkHelp(seed, w, it, p, kind, eqText, v) {
  const sol = kind === 'text' ? U.solution(p, 'text') : U.solution(p, 'mc'), st = U.walk(p, kind === 'text' ? 'text' : 'mc');
  const first = eqText ? solveText(eqText, v) : null;
  (sol || []).forEach((l, i) => { counts.lines++; words(seed, w + ' line ' + (i + 1), l.say);
    if (l.ex && typeof l.ex === 'object' && first) { const t = plainOf(E.eqH(l.ex)), got = solveText(t, v);
      if (got.kind !== first.kind || (got.kind === 'one' && !eqr(got.s, first.s))) fail(seed, w, 'worked line ' + (i + 1) + ', ' + t + ', is not the same equation as ' + eqText);
      if (got.kind !== 'one' && /^[-\d.\s]+=[-\d.\s]+$/.test(t.replace(/−/g, '-'))) fail(seed, w, 'a false equation printed as a line of work: ' + t); }
    if (l.ex && typeof l.ex === 'string') words(seed, w + ' line ' + (i + 1) + ' ex', l.ex); });
  if (!sol || !sol.length) fail(seed, w, 'no worked solution');
  (st || []).forEach((s, i) => { counts.steps++; const sw = w + ' step ' + (i + 1); words(seed, sw, s.ask);
    if (s.type === 'choice') { const ok = s.opts.filter(o => o.ok); if (ok.length !== 1) fail(seed, sw, ok.length + ' right options');
      s.opts.forEach(o => { words(seed, sw, o.label); if (!o.ok && !o.why) fail(seed, sw, 'a wrong option without a reason: ' + plainOf(o.label)); if (o.why) words(seed, sw, o.why); });
      if (new Set(s.opts.map(o => plainOf(o.label))).size !== s.opts.length) fail(seed, sw, 'two options say the same'); }
    else { words(seed, sw, s.hint);
      /* "What is 15 − 18?": the step's answer is that arithmetic, worked here */
      const asked = mathSpans(s.ask).filter(x => !/[a-zB□]/.test(x.replace(/−/g, '-')) && /[\d)]\s*[-+/(]|^\s*-?\d/.test(x)).pop();
      if (/^What is /.test(plainOf(s.ask).replace(/^.*?(What is )/, '$1')) && asked) { try { const val = coef(readPoly(asked), ''); if (!eqr(val, [s.ans.n, s.ans.d])) fail(seed, sw, 'asks ' + asked + ' but its answer is ' + E.numStr(s.ans)); } catch (e) { } }
      const said = plainOf(s.hint).replace(/−/g, '-'), a = E.numStr(s.ans).replace(/−/g, '-');
      if (new RegExp('=\\s*' + a.replace(/[.()]/g, '\\$&') + '(?!\\d|\\.\\d|\\s*[-+·*/(])').test(said)) fail(seed, sw, 'the Hint states its own answer: ' + said);
      if (!U.numOk(s, s.ans)) fail(seed, sw, 'its own answer is not accepted');
      if (s.tol) [0.2, -0.2].forEach(d => { const v = E.qadd(s.near, E.Q(Math.round(d * 10), 10)); if (U.numOk(s, v)) fail(seed, sw, 'the estimate step accepts ' + E.numStr(v) + ', 0.2 off'); }); } });
  /* Hints 1 and 2 (help.js, 15 Nov 2026): every claim and word read; an equation with parentheses is taught DISTRIBUTE FIRST
     (Croix, 14 Nov 2026: "they are terrible at distributing. So let's do distribute") — Hint 2, the first worked line and the
     walkthrough's first move all distribute, and nothing divides first */
  const RG = U.rungs ? U.rungs(p, kind === 'text' ? 'text' : 'mc', {}) : null;
  if (!RG || !RG.notice) fail(seed, w, 'no Hint 1');
  else { words(seed, w + ' Hint 1', RG.notice); if (RG.first) words(seed, w + ' Hint 2', RG.first.say); }
  if (eqText && /\(/.test(eqText) && !(p.fam === 'plans')) { counts.dist = (counts.dist || 0) + 1;
    const t0 = plainOf((RG && RG.first || {}).say || ''), l0 = plainOf((sol[0] || {}).say || ''), m0 = (st || []).find(s => s.type === 'choice'), r0 = m0 ? plainOf((m0.opts.find(o => o.ok) || {}).label || '') : '';
    if (!/^Distribute/.test(t0) || !/^Distribute/.test(l0) || !/^Distribute/.test(r0)) fail(seed, w, 'parentheses not distributed first: Hint 2 "' + t0.slice(0, 40) + '", line 1 "' + l0.slice(0, 40) + '", walk "' + r0.slice(0, 40) + '"');
    if (/^Divide/.test(t0 + l0) || /^Divide/.test(r0)) fail(seed, w, 'the help divides first'); }
  /* the rule (Hint 1) and every named mistake's words: read too */
  const fam = C.F[p.fam] || C.PF[p.fam]; if (fam) words(seed, w + ' rule', fam.rule(p));
  else if (C.MC[p.fam]) words(seed, w + ' rule', C.MC[p.fam].rule(p));
  if (!st || !st.length) fail(seed, w, 'no walk');
}

/* ------------------------------------------------------------------ one set */
const dump = [];
const V14B = new Set();               /* Q14(b)'s versions counted on their own (ruling 49's floor, 100; 15 Nov 2026) */
for (let seed = 1; seed <= NSETS; seed++) {
  counts.sets++;
  const G = U.generate(seed), D = seed <= NDUMP ? { seed, items: [] } : null;
  const secs = G.sections;
  if (secs.map(s => s.title).join('|') !== TEST_TITLES.join('|')) fail(seed, 'shape', 'the sections are not the test\'s');
  if (secs.map(s => s.items.length).join(',') !== WANT.items) fail(seed, 'shape', 'the questions per section are not the test\'s');
  if (secs.map(s => s.items.reduce((a, it) => a + E.partsOf(it).length, 0)).join(',') !== WANT.points) fail(seed, 'shape', 'the points per section are not the tracker\'s');
  if (secs.map(s => s.items.map(it => it.type).join(',')).join('|') !== WANT.types) fail(seed, 'shape', 'the kinds of question are not the test\'s');
  let q = 0;
  secs.forEach(sec => sec.items.forEach(it => { q++; const w = 'Q' + q, stem = U.view.stem(it), figH = U.view.figure(it);
    words(seed, w + ' stem', stem);
    WANT.words.filter(x => x[0] === q).forEach(x => wordsOk(seed, w + ' stem', stem, x[2]));
    WANT.parts.filter(x => x[0] === q).forEach(x => { const p = it.parts.find(pp => pp.label === x[1]); if (!p) fail(seed, w, 'no part ' + x[1]); else wordsOk(seed, w + x[1], p.stem, x[3]); });
    if (q === 14) { const caps = [figH, U.view.line(it.parts[1])].map(h => (/<div class="fcap">([^<]*)<\/div>/.exec(h) || [])[1] || '');
      caps.forEach((c, i) => { if (!WANT.captions[i][1].test(c)) fail(seed, w, 'graph ' + (i + 1) + ' is not captioned as the paper: "' + c + '"'); }); }
    const DI = D ? { q, type: it.type, stem, fig: figH, parts: [], opts: it.opts || null, correct: it.correct == null ? null : it.correct } : null;
    const eqRun = mathSpans(stem);
    try {
      if (q <= 4) {                                                        /* Solve: … */
        const p = it.part, t = eqRun[0], v = p.v, s = solveText(t, v); counts.eqs++;
        if (s.kind !== 'one' || !sameR(s.s, p.ans)) fail(seed, w, t + ' solves to ' + (s.s ? fl(s.s) : s.kind) + ', the key is ' + E.numStr(p.ans));
        if (q === 2 && !(fl(s.s) < 0)) fail(seed, w, 'the solution is not negative');
        if (q === 4 && !/^-?(?:0\.2|0\.4|0\.5|1\.5|2\.5)\(/.test(t.replace(/−/g, '-'))) fail(seed, w, 'not a decimal 0.2, 0.4, 0.5, 1.5 or 2.5 (or its negative) distributed: ' + t);
        if (q === 1 && !(/\(/.test(t) && (t.match(/[a-z]/g) || []).length === 2 && !/=.*[a-z]/.test(t))) fail(seed, w, 'not like terms and one distribution on one side: ' + t);
        if (q === 3 && ((t.match(/\(\(/g) || []).length !== 1 || t.split('=').some(sd => !/\(/.test(sd)))) fail(seed, w, 'not parentheses on both sides with a fraction in front of one: ' + t);
        /* the clean rule, read from the words: the answer is not one of the printed numbers */
        (t.match(/\d+(?:\.\d+)?/g) || []).forEach(x => { if (eqr(dec(x), [E.qabs(p.ans).n, E.qabs(p.ans).d])) fail(seed, w, 'the answer ' + x + ' is printed in the question'); });
        held43(seed, w, { eqs: [[t, v]] });
        typeBack(seed, w, p); checkHelp(seed, w, it, p, 'text', t, v);
      } else if (q === 5) {
        const ends = it.parts.map(p => { const s = solveText(plainOf(p.stem), 'x'); counts.eqs++;
          const want = ['One solution', 'No solution', 'Infinitely many solutions'][s.kind === 'one' ? 0 : s.kind === 'none' ? 1 : 2];
          if (p.opts[p.correct] !== want) fail(seed, w + p.label, plainOf(p.stem) + ' has ' + want.toLowerCase() + ', the key says ' + p.opts[p.correct]);
          [0, 1, 2].forEach(k => { if (k === p.correct) return; const r = U.judge.mc(p, k); counts.mc++; if (r.v !== 'wrong' || !r.what[0]) fail(seed, w + p.label, 'choice ' + k + ' not named'); words(seed, w + p.label, r.what[0]); });
          held43(seed, w + p.label, { eqs: [[plainOf(p.stem), 'x']] });
          if (U.judge.mc(p, p.correct).v !== 'right') fail(seed, w + p.label, 'the key is not right');
          checkHelp(seed, w + p.label, it, p, 'mc', plainOf(p.stem), 'x');
          if (s.kind === 'one') { const sol = U.solution(p, 'mc').map(l => plainOf(l.say)).join(' '); if (sol.indexOf('x = ' + E.numStr(E.Q(s.s[0], s.s[1]))) < 0) fail(seed, w + p.label, 'the worked solution does not find x = ' + fl(s.s)); }
          return s.kind; });
        if (ends.slice().sort().join() !== 'all,none,one') fail(seed, w, 'not one of each ending: ' + ends);
        it.parts.forEach(p => DI && DI.parts.push({ label: p.label, kind: 'mc', line: p.stem, opts: p.opts, correct: p.correct, sol: U.solution(p, 'mc').map(l => l.say) }));
      } else if (q === 6) {
        const p = it.part, t = eqRun[0], [Ls, Rs] = t.split('='), want = /no solution/.test(plainOf(stem)) ? 'none' : 'all';
        const d = padd(readPoly(Ls), pneg(readPoly(Rs)));               /* (a − B)x + … or a·x + (c − B) */
        const B = p.ans, put = padd(d, new Map());
        const filled = new Map(); d.forEach((c, m) => { const mm = m.replace('B', ''); const add = m.indexOf('B') >= 0 ? mu(c, [B.n, B.d]) : c; filled.set(mm, filled.has(mm) ? ad(filled.get(mm), add) : add); });
        const a = filled.get('x') || R(0), b = filled.get('') || R(0), kind = a[0] !== 0n ? 'one' : b[0] === 0n ? 'all' : 'none';
        if (kind !== want) fail(seed, w, 'with ' + E.numStr(B) + ' in the box, ' + t + ' has ' + kind + ', not ' + want);
        /* the box's number is the only one: the box's coefficient is not zero, so exactly one value does it */
        const bc = [...d.entries()].filter(([m]) => m.indexOf('B') >= 0); if (bc.length !== 1) fail(seed, w, 'the box appears ' + bc.length + ' times');
        held43(seed, w, { eqs: [[t, 'x', true]] });
        typeBack(seed, w, p); checkHelp(seed, w, it, p, 'text', null, 'x'); counts.eqs++;
      } else if (q === 7) {
        const p = it.part, tx = plainOf(stem), $ = [...tx.matchAll(/\$(\d+)/g)].map(m => +m[1]);
        const sents = tx.split(/(?<=\.) /).slice(0, 2).map(snt => { const ns = [...snt.matchAll(/\$(\d+)/g)].map(m => +m[1]);
          const pm = /\$(\d+) (?:a|an) (?:month|visit|class|hour)\b/.exec(snt) || /a visit costs \$(\d+)/.exec(snt); if (!pm) throw new Error('no price each time: ' + snt);
          const price = +pm[1], rest = ns.slice(); rest.splice(rest.indexOf(price), 1); return { price, fee: rest.length ? rest[0] : 0 }; });
        const fA = sents[0].fee, pA = sents[0].price, fB = sents[1].fee, pB = sents[1].price;
        const nn = dv(R(fA - fB), R(pB - pA));
        if (!sameR(nn, p.ans)) fail(seed, w, 'the story gives ' + fl(nn) + ', the key is ' + E.numStr(p.ans) + ': ' + tx);
        if (nn[1] !== 1n || fl(nn) < 2) fail(seed, w, 'the count is not a whole number of 2 or more');
        if (!(pB > pA && fA > fB)) fail(seed, w, 'the story is not two plans that meet');
        held43(seed, w, { story: [fA, pA, pB].concat(fB ? [fB] : []) });
        const e0 = U.solution(p, 'text')[0].ex, t0 = plainOf(E.eqH(e0)), s0 = solveText(t0, p.v);
        if (s0.kind !== 'one' || !eqr(s0.s, nn)) fail(seed, w, 'the worked equation ' + t0 + ' is not the story\'s');
        typeBack(seed, w, p); checkHelp(seed, w, it, p, 'text', t0, p.v);
      } else if (q === 8 || q === 9) {
        const L1 = q === 9 ? lineOf(eqRun[1]) : null, L2 = q === 9 ? lineOf(eqRun[2]) : null;
        if (q === 9) { if (eqr(L1[0], L2[0])) fail(seed, w, 'the same number multiplies x'); held43(seed, w, { lines: [L1, L2] }); [L1, L2].forEach(l => { if (l[0][1] !== 1n) fail(seed, w, 'not an integer multiplier'); }); }
        if (q === 8) {
          const pr = (() => { const m = /\((-?[\d.]+),\s*(-?[\d.]+)\)/.exec(eqRun[0].replace(/−/g, '-')); return [numR(m[1]), numR(m[2])]; })();
          const sysL = it.opts.map(o => mathSpans(o).map(lineOf));
          const rights = sysL.map((ls, i) => on(ls[0], ...pr) && on(ls[1], ...pr) ? i : -1).filter(i => i >= 0);
          if (rights.join() !== it.correct.join() || rights.length < 2 || rights.length > 3) fail(seed, w, 'the systems with the pair as a solution are ' + rights + ', the key ' + it.correct);
          sysL.forEach((ls, i) => { counts.pairs++; if (eqr(ls[0][0], ls[1][0])) fail(seed, w, 'system ' + i + ': the same number multiplies x');
            ls.forEach(l => { if (l[0][1] !== 1n) fail(seed, w, 'not an integer multiplier'); });
            const k = (on(ls[0], ...pr) ? 1 : 0) + (on(ls[1], ...pr) ? 1 : 0); if (rights.indexOf(i) < 0 && k !== 1) fail(seed, w, 'wrong system ' + i + ' is true in ' + k + ' of its equations, not 1');
            held43(seed, w, { lines: ls });
            if (rights.indexOf(i) < 0) { const why = U.view.why(it, i); if (!why) fail(seed, w, 'system ' + i + ' has no reason'); words(seed, w, why); } });
          if (new Set(sysL.map(ls => ls.map(l => l.join()).sort().join(';'))).size !== 5) fail(seed, w, 'two systems the same');
          if (/\b(two|three|2|3) (of|systems)\b/i.test(plainOf(stem))) fail(seed, w, 'the stem says how many');
          if (it.opts.length !== 5) fail(seed, w, it.opts.length + ' systems, not five');
        } else {
          /* every option is a verdict with a claim about THIS pair; exactly one option is true, and it is the key — so no
             option is arguable (14 Nov 2026: "Yes — it makes the first equation true" was true of the solution itself) */
          const m = /\((-?[\d.]+),\s*(-?[\d.]+)\)/.exec(eqRun[0].replace(/−/g, '-')), pr = [numR(m[1]), numR(m[2])], t = [on(L1, ...pr), on(L2, ...pr)];
          const names = [eqRun[1], eqRun[2]], judged = it.opts.map(o => q9Claim(plainOf(o), names, t)); counts.pairs++;
          const trueOnes = judged.map((j, i) => j.whole ? i : -1).filter(i => i >= 0);
          if (trueOnes.length !== 1 || trueOnes[0] !== it.correct) fail(seed, w, 'the options true of ' + plainOf(eqRun[0]) + ' are ' + trueOnes + ', the key ' + it.correct + ' (' + it.opts.map(plainOf).join(' | ') + ')');
          judged.forEach((j, i) => { if (j.claim !== j.whole) fail(seed, w, 'option ' + i + "'s claim is true but its verdict is not: " + plainOf(it.opts[i])); });
          const shapes = it.opts.map(o => plainOf(o).replace(/y = .+? (?=true)/, 'E ')).sort().join('|');
          if (shapes !== WANT.q9claims.slice().sort().join('|')) fail(seed, w, 'the options are not the four claims (both, only each one, neither): ' + it.opts.map(plainOf).join(' | '));
          if (it.opts.map(plainOf).filter(o => /only/.test(o)).map(o => /only (y = .+) true/.exec(o)[1]).sort().join('|') !== names.slice().sort().join('|')) fail(seed, w, 'the two "only" options do not name the two equations');
          { const ws = it.opts.map((o, k) => k === it.correct ? null : (U.judge.mc(it, k).what || [])[0]).filter(x => x != null); if (new Set(ws).size !== ws.length) fail(seed, w, 'two wrong options get the same reason'); }
          counts.q9 = (counts.q9 || 0) + 1; counts.q9t = counts.q9t || {}; const pat = (t[0] ? 'A' : '-') + (t[1] ? 'B' : '-'); counts.q9t[pat] = (counts.q9t[pat] || 0) + 1;
        }
        (it.opts || []).forEach((o, k) => { words(seed, w, o); if (it.type === 'mc' && k !== it.correct) { const r = U.judge.mc(it, k); counts.mc++; if (r.v !== 'wrong' || !r.what[0]) fail(seed, w, 'choice ' + k + ' not named'); words(seed, w, r.what[0]); } });
        if (it.type === 'mc' && U.judge.mc(it, it.correct).v !== 'right') fail(seed, w, 'the key is not right');
        if (it.type === 'multi' && U.judge.multi(it, it.correct, 1).v !== 'right') fail(seed, w, 'the key is not right');
        checkHelp(seed, w, it, it, 'mc', null, null);
      } else if (q === 10 || q === 11) {
        const L1 = lineOf(eqRun[0]), L2 = lineOf(eqRun[1]), same = eqr(L1[0], L2[0]) && eqr(L1[1], L2[1]), par = eqr(L1[0], L2[0]) && !same;
        const want = same ? 2 : par ? 1 : 0; held43(seed, w, { lines: [L1, L2] });
        if (it.correct !== want) fail(seed, w, 'the count is ' + it.opts[want] + ', the key ' + it.opts[it.correct]);
        if (q === 10 && want !== 0) fail(seed, w, 'Q10 lines do not cross');
        if (q === 11 && want === 0) fail(seed, w, 'Q11 lines cross');
        if (q === 11 && same !== /Both equations graph as the one line shown/.test(plainOf(stem))) fail(seed, w, 'the one-line words and the equations disagree');
        let cross = null; if (want === 0) { const x = dv(ad(L2[1], ng(L1[1])), ad(L1[0], ng(L2[0]))); cross = [x, at(L1, x)]; if (x[1] !== 1n || cross[1][1] !== 1n) fail(seed, w, 'the crossing is not a grid point'); }
        readPlane(seed, w, figH, same ? [L1] : [L1, L2], { n: same ? 1 : 2, cross });
        it.opts.forEach((o, k) => { if (k !== it.correct) { const r = U.judge.mc(it, k); counts.mc++; if (r.v !== 'wrong' || !r.what[0]) fail(seed, w, 'choice ' + k + ' not named'); words(seed, w, r.what[0]); } });
        checkHelp(seed, w, it, it, 'mc', null, null);
      } else if (q === 12) {
        const p = it.part, L1 = lineOf(eqRun[0]), L2 = lineOf(eqRun[1]), x = dv(ad(L2[1], ng(L1[1])), ad(L1[0], ng(L2[0]))), y = at(L1, x);
        if (!sameR(x, p.ans[0]) || !sameR(y, p.ans[1])) fail(seed, w, 'the crossing is (' + fl(x) + ', ' + fl(y) + '), the key ' + p.ans.map(E.numStr));
        if (x[1] !== 1n || y[1] !== 1n) fail(seed, w, 'the crossing is not a grid point');
        readPlane(seed, w, figH, [L1, L2], { n: 2, cross: [x, y] }); held43(seed, w, { lines: [L1, L2] });
        typeBack(seed, w, p); checkHelp(seed, w, it, p, 'text', null, null);
      } else if (q === 13) {
        const L1 = lineOf(eqRun[0]), L2 = lineOf(eqRun[1]), T = readTables(seed, w, figH); counts.tables++; held43(seed, w, { lines: [L1, L2] });
        if (T.length !== 2 || T[0].title !== eqRun[0] || T[1].title !== eqRun[1]) fail(seed, w, 'the tables are not titled by the equations');
        let gap = -1;
        T.forEach((t, ti) => t.xs.forEach((x, i) => { const y = t.ys[i], l = ti ? L2 : L1; if (y == null) { if (ti) fail(seed, w, 'a gap in the second table'); gap = i; return; } if (!on(l, x, y)) fail(seed, w, 'table ' + (ti + 1) + ' at x = ' + fl(x) + ' says ' + fl(y)); }));
        const pa = it.parts[0], pb = it.parts[1], miss = at(L1, T[0].xs[gap]);
        if (!sameR(miss, pa.ans)) fail(seed, w + 'a', 'the missing value is ' + fl(miss) + ', the key ' + E.numStr(pa.ans));
        const agree = T[0].xs.map((x, i) => eqr(at(L1, x), at(L2, x)) ? i : -1).filter(i => i >= 0);
        if (agree.length !== 1) fail(seed, w + 'b', 'the tables agree in ' + agree.length + ' columns');
        else { const x = T[0].xs[agree[0]]; if (!sameR(x, pb.ans[0]) || !sameR(at(L1, x), pb.ans[1])) fail(seed, w + 'b', 'the tables agree at x = ' + fl(x) + ', the key ' + pb.ans.map(E.numStr)); if (agree[0] === gap) fail(seed, w + 'b', 'the solution is in the gap'); }
        [pa, pb].forEach(p => { words(seed, w + p.label, p.stem); typeBack(seed, w + p.label, p); checkHelp(seed, w + p.label, it, p, 'text', null, null); });
      } else if (q === 14) {
        const pa = it.parts[0], pb = it.parts[1], tx = plainOf(stem);
        let L1, L2;
        { const mm = /^(\w+)\D*?(\d+)\D+?(\d+) (?:cm )?each week\. (\w+)\D*?(\d+)\D+?(saves|spends|grows) \$?(\d+)/.exec(tx);
          if (!mm) throw new Error('the story is not read: ' + tx);
          L1 = [R(+mm[3]), R(+mm[2])]; L2 = [R(mm[6] === 'spends' ? -mm[7] : +mm[7]), R(+mm[5])]; }
        const x = dv(ad(L2[1], ng(L1[1])), ad(L1[0], ng(L2[0]))), y = at(L1, x);
        if (!sameR(x, pa.ans[0]) || !sameR(y, pa.ans[1])) fail(seed, w + 'a', 'the story meets at (' + fl(x) + ', ' + fl(y) + '), the key ' + pa.ans.map(E.numStr));
        if (x[1] !== 1n || y[1] !== 1n || fl(x) < 1) fail(seed, w + 'a', 'not whole weeks and a whole amount');
        const ys = +/data-win="[^"]* ([\d.]+)"/.exec(figH)[1]; if (fl(y) % ys !== 0) fail(seed, w + 'a', 'the amount is not on a grid line');
        if (!/weeks/.test(figH) || !/(dollars|centimeters)/.test(figH)) fail(seed, w + 'a', 'the axes are not named');
        readPlane(seed, w + 'a', figH, [L1, L2], { n: 2, cross: [x, y] });
        const lineH = U.view.line(pb), runs = mathSpans(pb.stem), B1 = lineOf(runs[0]), B2 = lineOf(runs[1]);
        const bx = dv(ad(B2[1], ng(B1[1])), ad(B1[0], ng(B2[0]))), by = at(B1, bx), fx = fl(bx), fy = fl(by);
        const frac = v => v - Math.floor(v);
        const half = v => Math.abs(v * 2 - Math.round(v * 2)) / 2;
        /* the key: the crossing rounded to the tenth, never from a tie; each rounded coordinate at least 0.2 from every grid and
           half-grid line, so no printed grid or half-grid point is inside the accepted box (key ± 0.1, inclusive) */
        const KX = Math.round(fx * 10), KY = Math.round(fy * 10), tie = v => { const t = mu(v, R(20)); return t[1] === 1n && t[0] % 2n !== 0n; };
        if (!sameR(R(KX, 10), pb.ans[0]) || !sameR(R(KY, 10), pb.ans[1])) fail(seed, w + 'b', 'the key is not the crossing rounded to the tenth');
        if (tie(bx) || tie(by)) fail(seed, w + 'b', 'the crossing is a rounding tie');
        [KX, KY].forEach(k => { const d = Math.min(...[0, 5].map(o => { const r = ((k - o) % 5 + 5) % 5; return Math.min(r, 5 - r); })); if (d < 2) fail(seed, w + 'b', 'the key ' + k / 10 + ' is ' + d / 10 + ' from a grid or half-grid line'); });
        const ws = /data-win="([^"]+)"/.exec(lineH)[1].split(' ').map(Number);
        for (let gx = ws[0] * 2; gx <= ws[1] * 2; gx++) for (let gy = ws[2] * 2; gy <= ws[3] * 2; gy++)
          if (Math.abs(gx * 5 - KX) <= 1 && Math.abs(gy * 5 - KY) <= 1) fail(seed, w + 'b', 'the grid point (' + gx / 2 + ', ' + gy / 2 + ') is inside the accepted range');
        if (Math.abs(KX - KY) <= 1) fail(seed, w + 'b', 'the swapped pair is inside the accepted range');
        readPlane(seed, w + 'b', lineH, [B1, B2], { n: 2, cross: [bx, by] }); held43(seed, w + 'b', { lines: [B1, B2] });
        V14B.add(runs.slice(0, 2).join(' ; '));                       /* 14(b)'s own version: its two printed equations, in order */
        { const mm = /^(\w+)\D*?(\d+)\D+?(\d+) (?:cm )?each week\. (\w+)\D*?(\d+)\D+?(saves|spends|grows) \$?(\d+)/.exec(tx); held43(seed, w + 'a', { story: [mm[2], mm[3], mm[5], mm[7]] }); }
        if (!/gridln2/.test(lineH)) fail(seed, w + 'b', 'no half lines to read between');
        [pa, pb].forEach(p => { words(seed, w + p.label, p.stem); typeBack(seed, w + p.label, p); checkHelp(seed, w + p.label, it, p, 'text', null, null); });
      }
    } catch (e) { fail(seed, w, 'could not read it back: ' + e.message); }
    if (DI) { if (q !== 5) E.partsOf(it).forEach(p => { if (it.type === 'mc' || it.type === 'multi') return;
        const B = U.view.boxes(p);                   /* the two boxes (15 Nov 2026): their labels, and answers typed box by box with the page's verdict, for verify.py to judge again */
        const tries = !B ? null : (() => { const k = p.ans.map(q => E.qnum(q)), f = v => String(+v.toFixed(2)), out = [[k[0], k[1]], [k[1], k[0]], [k[0], k[1] + 3], [k[0] + 3, k[1]], [k[0] + 1, k[1] + 1]];
          if (p.fam === 'estimate') [[0.1, 0.1], [-0.1, -0.1], [0.1, -0.2], [0.2, 0], [0, 0.2], [-0.2, 0.1]].forEach(([a, b2]) => out.push([k[0] + a, k[1] + b2]));
          return out.map(([a, b2]) => { const t = [f(a), f(b2)]; return { typed: t, v: U.judge.text(p, t).v }; }); })();
        DI.parts.push({ label: p.label, kind: p.kind, fam: p.fam, line: U.view.line(p), key: U.view.key(p), keyText: U.keyText(p), choices: U.choices(p),
          boxes: B ? B.map(b => plainOf((b.pre || '') + ' ▢ ' + (b.unit || '')).replace(/\s+/g, ' ').trim()) : null, tries,
          sol: U.solution(p, 'text').map(l => ({ say: l.say, ex: l.ex == null ? null : typeof l.ex === 'string' ? l.ex : E.eqH(l.ex) })),
          steps: U.walk(p, 'text').filter(s => s.type === 'num').map(s => ({ ask: s.ask, ans: E.kstr(s.ans), tol: s.tol ? E.kstr(s.tol) : null, near: s.near ? E.kstr(s.near) : null })) }); });
      if (it.type === 'mc' || it.type === 'multi') DI.sol = U.solution(it, 'mc').map(l => l.say);
      D.items.push(DI); }
  }));
  if (D) dump.push(D);
}
/* the floor of 100 versions holds for Q14(b) by itself, not only with its story (the kit's variety check counts the two together):
   a run of 1,000 sets or more must show 100 different systems; a shorter run (plant_check's 300) at least 80% of its sets */
{ const need = NSETS >= 1000 ? 100 : Math.ceil(0.8 * NSETS); counts.v14b = V14B.size;
  if (V14B.size < need) fail('all', 'Q14b', 'only ' + V14B.size + ' different systems in ' + NSETS + ' sets (the floor: ' + need + ')'); }
fs.writeFileSync(path.join(__dirname, 'dump.json'), JSON.stringify({ TITLES: E.TITLES, sets: dump }));
console.log(counts.sets + ' sets: ' + counts.eqs + ' equations solved again from their words, ' + counts.keys + ' keys typed back, ' + counts.models + ' mistakes typed, ' + counts.lines + ' worked lines and ' +
  counts.steps + ' Hint steps, ' + counts.claims + ' arithmetic claims, ' + counts.pairs + ' ordered pairs in both equations, ' + counts.figs + ' graphs (' + counts.segs + ' lines read back), ' + counts.tables + ' table pairs, ' + counts.mc + ' wrong choices named, Q9 (pairs on both lines, A only, B only, neither) '  + JSON.stringify(counts.q9t || {}) + ' with exactly one option true, ruling 43 held on ' + counts.r43 + ' questions, ' + counts.dist + ' equations with parentheses distributed first in the help, Q14(b) in ' + counts.v14b + ' versions of its own; ' + NDUMP + ' sets written to dump.json');
if (nfail) { console.log(nfail + ' PROBLEMS'); fails.forEach(f => console.log('  ' + f)); process.exit(1); }
console.log('u11_check: ALL CHECKS PASS');
