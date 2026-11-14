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
  const s = t.replace(/−/g, '-');
  const re = /[\d.()+\-*/½⅓⅔¼¾⅕⅖⅗⅘·÷\s]*\d[\d.()+\-*/½⅓⅔¼¾⅕⅖⅗⅘·÷\s=]*/g; let m;
  while ((m = re.exec(s))) {
    const run = m[0]; if (run.indexOf('=') < 0) continue;
    const before = s.slice(0, m.index).replace(/\s+$/, ''), after = s.slice(m.index + run.length);
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
/* >>> THE PAPER'S SHAPE, BY HAND — update here if unit.py's practice paper changes kind. The section titles above are read from
   unit.py (any wording; the page's must match them). Q8 is "Select ALL the systems that have (a, b) as a solution" (the lead,
   14 Nov 2026: one pair, five systems, two or three right) — still a select-all, 'multi', so nothing here names its words. <<< */
const WANT = { items: '7,2,2,3', points: TRACK.join(','), types: 'solo,solo,solo,solo,parts,solo,solo|multi,mc|mc,mc|solo,parts,parts' };

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
    wrong(kt(E.qadd(p.ans, E.Q(1))), false);
  } else {
    const [x, y] = p.ans;
    if (p.kind === 'story') { right(kt(x) + ' weeks, ' + (p.st.unit === 'dollars' ? '$' + kt(y) : kt(y) + ' cm')); right(p.st.unit === 'dollars' ? '$' + kt(y) + ' after ' + kt(x) + ' weeks' : kt(y) + ' cm after ' + kt(x) + ' weeks'); right(kt(x) + ' and ' + kt(y)); }
    else { right(kt(x) + ', ' + kt(y)); right('x = ' + kt(x) + ', y = ' + kt(y)); right('(' + kt(x) + ',' + kt(y) + ')'); }
    C.PF[p.fam].models(p).forEach(m => { if (E.qeq(m.v[0], x) && E.qeq(m.v[1], y)) return; wrong('(' + kt(m.v[0]) + ', ' + kt(m.v[1]) + ')', true); });
    if (p.fam === 'estimate') {
      const ex = p.exact, t = 0.1;
      [[0.05, 0], [-0.05, 0.05], [0, -0.05], [0.15, 0], [0, -0.15]].forEach(([a, b]) => { const X = Math.round((fl([ex.x.n, ex.x.d]) + a) * 10) / 10, Y = Math.round((fl([ex.y.n, ex.y.d]) + b) * 10) / 10;
        const inside = Math.abs(X - E.qnum(ex.x)) <= t + 1e-9 && Math.abs(Y - E.qnum(ex.y)) <= t + 1e-9; const r = U.judge.text(p, '(' + X + ', ' + Y + ')');
        if ((r.v === 'right') !== inside) fail(seed, w, '(' + X + ', ' + Y + ') is ' + r.v + ' but is ' + (inside ? 'inside' : 'outside') + ' the tolerance'); });
      const far = '(' + (Math.round((E.qnum(ex.x) + 0.2) * 10) / 10) + ', ' + (Math.round(E.qnum(ex.y) * 10) / 10) + ')';
      if (U.judge.text(p, far).v === 'right') fail(seed, w, far + ' is 0.2 off and marked right');
      if (E.qnum(p.tol) !== 0.1) fail(seed, w, 'the tolerance is not 0.1');
    } else wrong('(' + kt(y) + ', ' + kt(x) + ')', !E.qeq(x, y));
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
  /* the rule (Hint 1) and every named mistake's words: read too */
  const fam = C.F[p.fam] || C.PF[p.fam]; if (fam) words(seed, w + ' rule', fam.rule(p));
  else if (C.MC[p.fam]) words(seed, w + ' rule', C.MC[p.fam].rule(p));
  if (!st || !st.length) fail(seed, w, 'no walk');
}

/* ------------------------------------------------------------------ one set */
const dump = [];
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
        const L1 = q === 9 ? lineOf(eqRun[0]) : null, L2 = q === 9 ? lineOf(eqRun[1]) : null;
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
        } else {
          const m = /\((-?[\d.]+),\s*(-?[\d.]+)\)/.exec(eqRun[2].replace(/−/g, '-')), pr = [numR(m[1]), numR(m[2])], t = [on(L1, ...pr), on(L2, ...pr)];
          const pick = it.opts.map(o => { const s = plainOf(o); const which = s.indexOf(plainOf(E.lineH(it.l1))) >= 0 && !/both/.test(s) ? 1 : s.indexOf(plainOf(E.lineH(it.l2))) >= 0 ? 2 : 0;
            if (/^Yes — it makes both/.test(s)) return t[0] && t[1];
            if (/^Yes/.test(s)) return false;                                  /* one equation is never the reason */
            return !(t[0] && t[1]) && !t[which - 1] && (which === 1 || which === 2); });
          const rights = pick.map((v, i) => v ? i : -1).filter(i => i >= 0);
          if (rights.length !== 1 || rights[0] !== it.correct) fail(seed, w, 'the right reason is ' + rights + ', the key ' + it.correct);
          if (!t[0] && !t[1]) fail(seed, w, 'the pair is on neither line');
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
        if (half(fx) < 0.15 || half(fy) < 0.15) fail(seed, w + 'b', 'the crossing (' + fx + ', ' + fy + ') is not well between the grid and half-grid lines');
        /* no grid or half-grid point inside the accepted range (it would be marked right, and it is on at most one line) */
        for (let gx = Math.floor((fx - 0.1) * 2); gx <= Math.ceil((fx + 0.1) * 2); gx++) for (let gy = Math.floor((fy - 0.1) * 2); gy <= Math.ceil((fy + 0.1) * 2); gy++)
          if (Math.abs(gx / 2 - fx) <= 0.1 + 1e-9 && Math.abs(gy / 2 - fy) <= 0.1 + 1e-9) fail(seed, w + 'b', 'the grid point (' + gx / 2 + ', ' + gy / 2 + ') is inside the tolerance');
        if (Math.abs(fl([pb.ans[0].n, pb.ans[0].d]) - fx) > 0.05 + 1e-9 || Math.abs(fl([pb.ans[1].n, pb.ans[1].d]) - fy) > 0.05 + 1e-9) fail(seed, w + 'b', 'the key is not the crossing to the tenth');
        if (Math.abs(fx - fy) <= 0.2) fail(seed, w + 'b', 'the swapped pair is inside the tolerance');
        readPlane(seed, w + 'b', lineH, [B1, B2], { n: 2, cross: [bx, by] }); held43(seed, w + 'b', { lines: [B1, B2] });
        { const mm = /^(\w+)\D*?(\d+)\D+?(\d+) (?:cm )?each week\. (\w+)\D*?(\d+)\D+?(saves|spends|grows) \$?(\d+)/.exec(tx); held43(seed, w + 'a', { story: [mm[2], mm[3], mm[5], mm[7]] }); }
        if (!/gridln2/.test(lineH)) fail(seed, w + 'b', 'no half lines to read between');
        [pa, pb].forEach(p => { words(seed, w + p.label, p.stem); typeBack(seed, w + p.label, p); checkHelp(seed, w + p.label, it, p, 'text', null, null); });
      }
    } catch (e) { fail(seed, w, 'could not read it back: ' + e.message); }
    if (DI) { if (q !== 5) E.partsOf(it).forEach(p => { if (it.type === 'mc' || it.type === 'multi') return;
        DI.parts.push({ label: p.label, kind: p.kind, fam: p.fam, line: U.view.line(p), key: U.view.key(p), keyText: U.keyText(p), choices: U.choices(p),
          sol: U.solution(p, 'text').map(l => ({ say: l.say, ex: l.ex == null ? null : typeof l.ex === 'string' ? l.ex : E.eqH(l.ex) })),
          steps: U.walk(p, 'text').filter(s => s.type === 'num').map(s => ({ ask: s.ask, ans: E.kstr(s.ans), tol: s.tol ? E.kstr(s.tol) : null, near: s.near ? E.kstr(s.near) : null })) }); });
      if (it.type === 'mc' || it.type === 'multi') DI.sol = U.solution(it, 'mc').map(l => l.say);
      D.items.push(DI); }
  }));
  if (D) dump.push(D);
}
fs.writeFileSync(path.join(__dirname, 'dump.json'), JSON.stringify({ TITLES: E.TITLES, sets: dump }));
console.log(counts.sets + ' sets: ' + counts.eqs + ' equations solved again from their words, ' + counts.keys + ' keys typed back, ' + counts.models + ' mistakes typed, ' + counts.lines + ' worked lines and ' +
  counts.steps + ' Hint steps, ' + counts.claims + ' arithmetic claims, ' + counts.pairs + ' ordered pairs in both equations, ' + counts.figs + ' graphs (' + counts.segs + ' lines read back), ' + counts.tables + ' table pairs, ' + counts.mc + ' wrong choices named, ruling 43 held on ' + counts.r43 + ' questions; ' + NDUMP + ' sets written to dump.json');
if (nfail) { console.log(nfail + ' PROBLEMS'); fails.forEach(f => console.log('  ' + f)); process.exit(1); }
console.log('u11_check: ALL CHECKS PASS');
