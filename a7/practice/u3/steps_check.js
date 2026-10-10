/* Every arithmetic claim written in the steps and messages ("4 + 5 = 9", "3<sup>2</sup> = 9", "6.6 ÷ 3.3 = 2") is recomputed exactly. */
const P = require('./engine.js');
const n = s => P.qdec(s.replace(/,/g, ''));
const num = s => { s = s.replace(/−/g, '-'); const neg = s.startsWith('-') || s.startsWith('(-'); const t = s.replace(/[()\-]/g, ''); const q = n(t); return neg ? P.Q(-q.n, q.d) : q; };
let claims = 0; const bad = [];
const NUM = '\\(?−?[\\d.,]+\\)?';
function scan(seed, where, text) {
  const t = String(text).replace(/<\/?i>|<span[^>]*>|<\/span>/g, '').replace(/1 over (\d+)<sup>(\d+)<\/sup>/g, '[1/$1^$2]').replace(/1 over ([\d,]+)/g, '[1/$1]');
  const re2 = new RegExp('(' + NUM + ') ([+−×÷]) (' + NUM + ') = (' + NUM + ')', 'g');
  let m;
  while ((m = re2.exec(t))) {
    claims++;
    const a = num(m[1]), b = num(m[3]), c = num(m[4]);
    const r = m[2] === '+' ? P.Q(a.n * b.d + b.n * a.d, a.d * b.d) : m[2] === '−' ? P.Q(a.n * b.d - b.n * a.d, a.d * b.d) : m[2] === '×' ? P.Q(a.n * b.n, a.d * b.d) : P.Q(a.n * b.d, a.d * b.n);
    if (!P.qeq(r, c)) bad.push(seed + ' ' + where + ': ' + m[0]);
  }
  const re3 = /(?<![×\d.]\s?)(\(?−?\d+\)?)<sup>(−?\d+)<\/sup> = (−?[\d,]+(?!<sup>|\d)|\[1\/\d+(?:\^\d+)?\])/g;
  const rhs = s => { const f = /^\[1\/(\d+)(?:\^(\d+))?\]$/.exec(s); if (!f) return num(s); return P.Q(1n, BigInt(f[1]) ** BigInt(f[2] || 1)); };
  while ((m = re3.exec(t))) {
    claims++;
    const base = num(m[1]), e = BigInt(m[2].replace('−', '-'));
    let r = P.Q(1); const k = e < 0n ? -e : e; for (let i = 0n; i < k; i++) r = P.Q(r.n * base.n, r.d * base.d);
    if (e < 0n) r = P.Q(r.d, r.n);
    if (!P.qeq(r, rhs(m[3]))) bad.push(seed + ' ' + where + ': ' + m[0]);
  }
  const re4 = /(−?[\d,]+) = (\d+)<sup>(\d+)<\/sup>/g;
  while ((m = re4.exec(t))) { claims++; if (!P.qeq(num(m[1]), P.Q(BigInt(m[2]) ** BigInt(m[3])))) bad.push(seed + ' ' + where + ': ' + m[0]); }
}
for (let seed = 1; seed <= 20000; seed++) {
  const G = P.generate(seed);
  G.sections.forEach((s, si) => s.items.forEach((it, ii) => {
    const w = 'S' + (si + 1) + 'I' + (ii + 1);
    const parts = it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : [];
    parts.forEach(p => { p.steps.forEach(x => scan(seed, w + p.label, x)); p.miss.forEach(x => scan(seed, w + p.label + ' miss', x.msg)); if (p.tail) scan(seed, w + p.label, P.html(p.shownAns) + p.tail); });
    if (it.type === 'mc') { it.steps.forEach(x => scan(seed, w, x)); it.why.forEach(x => x && scan(seed, w + ' why', x)); }
    if (it.stem) scan(seed, w + ' stem', it.stem);
  }));
}
console.log(claims, 'arithmetic claims checked;', bad.length ? bad.length + ' WRONG\n' + bad.slice(0, 30).join('\n') : 'all true');
/* the checker itself must catch a planted error */
bad.length = 0; claims = 0;
scan(0, 'plant', '4 + 5 = 10'); scan(0, 'plant', '3<sup>2</sup> = 6'); scan(0, 'plant', '5<sup>−2</sup> = 1 over 10'); scan(0, 'plant', '125 = 5<sup>4</sup>'); scan(0, 'plant', '6.6 ÷ 3.3 = 3');
console.log('planted errors caught:', bad.length, 'of 5');
bad.length = 0; scan(0, 'plant', P.html(P.Sci('2', 4)) + ' = 30,000 times'); scan(0, 'ok', P.html(P.Sci('2', 4)) + ' = 20,000 times');
console.log('tail check: planted wrong caught', bad.length === 0 ? 'NO (tails are checked in verify.py instead)' : 'yes');
