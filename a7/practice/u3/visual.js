/* A7 Unit 3 practice: pictures of WHY each rule works, built from the question's own numbers.
   spec(part) returns plain data (counts, values) that visual_check.js verifies; html(spec) draws it.
   Kinds: row (factors side by side), grid (copies of a power), cancel (factors over factors), ladder (powers going down,
   each one ÷ the base), signs (pairs of negatives), copies (a product raised to a power), hop (the decimal point moving). */
(function (root) {
'use strict';
const E = (typeof module !== 'undefined' && module.exports) ? require('./engine.js') : root.Practice;
const { Q, qeq, qdec, decStr, commas, N, V, P, Mul, Fr, Neg, Par, Ar, M, qmul, qdiv, qpow, esc } = E;
const qi = x => typeof x === 'object' ? x : typeof x === 'string' ? qdec(x) : Q(BigInt(x));

function spec(part) {
  const f = part.fam, x = part.prm; if (!f || !x) return null;
  const L = v => ({ letter: v });
  switch (f) {
    case 'prod': return { kind: 'row', base: x.b, groups: [x.m, x.n], total: x.m + x.n };
    case 'monoProd': return { kind: 'row', base: L(x.v), groups: [x.m, x.n], total: x.m + x.n };
    case 'powpow': return { kind: 'grid', base: x.b, rows: x.n, cols: x.m, total: x.m * x.n };
    case 'monoPow': return { kind: 'grid', base: L(x.v), rows: x.n, cols: x.m, total: x.m * x.n };
    case 'quot': return { kind: 'cancel', base: x.b, top: x.m, bottom: x.n };
    case 'zero': return { kind: 'cancel', base: x.b, top: 3, bottom: 3, zero: true };
    case 'monoQuot': return { kind: 'cancel', base: L(x.v), top: x.p, bottom: x.q, numbers: [x.k, x.j, x.t] };
    case 'mixedProd': return { kind: 'cancel', base: x.B, top: x.m, bottom: x.n, fromNeg: true };
    case 'powquot': return { kind: 'cancel', base: x.B, top: x.p * x.q, bottom: x.r, fromPow: [x.p, x.q] };
    case 'solveN': return { kind: 'cancel', base: x.b, top: x.k + x.c, bottom: x.k, solve: { k: x.k, c: x.c, V: x.V } };
    case 'negToFrac': case 'negVal': return { kind: 'ladder', base: x.b, low: -x.n };
    case 'varNeg': return { kind: 'ladder', base: L(x.v), low: -x.n };
    case 'coefVarNeg': return { kind: 'ladder', base: L(x.v), low: -x.n, coef: x.c };
    case 'coefNeg': return { kind: 'ladder', base: 10, low: -x.m, coef: x.k };
    case 'negDen': return { kind: 'ladder', base: -x.c, low: -x.m, high: Math.min(x.m, 3), mark: x.m <= 3 ? [-x.m, x.m] : [-x.m], note: 'negDen', m: x.m, c: x.c };
    case 'zeroMix': return { kind: 'ladder', base: x.a, low: 0, note: 'zero' };
    case 'fracNeg': return { kind: 'ladder', base: { frac: x.d }, low: -x.n };
    case 'negNegBase': return { kind: 'signs', c: x.c, e: x.e };
    case 'fracpow': return { kind: 'copies', copies: x.k, parts: [{ n: x.p, of: 'top' }, { n: x.q, of: 'bottom' }], frac: true };
    case 'monoCoefPow': return { kind: 'copies', copies: x.q, parts: [{ n: x.c }, { letter: x.v, e: x.p }] };
    case 'monoNegPow': return { kind: 'copies', copies: x.q, parts: [{ n: x.k }, { letter: x.v, e: -x.p }, { letter: x.w, e: 1 }] };
    case 'toSci': return hopSpec(x.c, x.k, 'toSci');
    case 'toStd': case 'eNote': return hopSpec(x.c, x.k, 'toStd');
    case 'ratio': return x.p > 0 && x.q > 0 ? { kind: 'cancel', base: 10, top: x.p, bottom: x.q, numbers: [x.A, x.B, x.t] } : null;
    default: return null;
  }
}
/* the digits in a row, and where the decimal point sits for c and for the ordinary number */
function hopSpec(c, k, dir) {
  const sd = c.replace('.', '').replace(/^0+/, '');        // 8.3 → "83", 3.07 → "307"
  let cells, cpos, spos;
  if (k >= 0) { cells = sd.length >= k + 1 ? sd : sd + '0'.repeat(k + 1 - sd.length); cpos = 1; spos = k + 1; }
  else { cells = '0'.repeat(-k) + sd; cpos = -k + 1; spos = 1; }
  return { kind: 'hop', c, k, dir, cells, cpos, spos, pad: k >= 0 ? [sd.length, cells.length] : [0, -k] };
}

/* ------------------------------------------------------------------ drawing */
const bHtml = b => b && b.letter ? '<i>' + esc(b.letter) + '</i>' : b && b.frac ? M(Fr(1, b.frac)) : String(b).replace('-', '−');
const bAst = b => b && b.letter ? V(b.letter) : b && b.frac ? Par(Fr(1, b.frac)) : (b < 0 ? Par(Neg(N(-b))) : N(b));
function tiles(n, b, cls, cap) {
  cap = cap || 12;
  const one = '<span class="tile ' + (cls || '') + '">' + bHtml(b) + '</span>';
  if (n <= cap) return Array(n).fill(one).join('');
  return Array(4).fill(one).join('') + '<span class="tdots">… ' + (n - 6) + ' more …</span>' + Array(2).fill(one).join('');
}
function html(s) {
  if (!s) return '';
  switch (s.kind) {
    case 'row': {
      const [m, n] = s.groups;
      return '<div class="vis"><div class="vrow"><span class="vgrp">' + tiles(m, s.base, 'a') + '<span class="vlab">' + m + ' factors</span></span><span class="vop">·</span><span class="vgrp">' + tiles(n, s.base, 'b') + '<span class="vlab">' + n + ' factors</span></span></div>' +
        '<p class="vcap">' + M(P(bAst(s.base), m)) + ' is ' + m + ' factors of ' + bHtml(s.base) + '; ' + M(P(bAst(s.base), n)) + ' is ' + n + ' more. Together: ' + m + ' + ' + n + ' = ' + s.total + ' factors, so ' + M(P(bAst(s.base), s.total)) + '.</p></div>';
    }
    case 'grid': {
      const rows = []; const shown = Math.min(s.rows, 6);
      for (let i = 0; i < shown; i++) rows.push('<div class="vrow"><span class="vrl">copy ' + (i + 1) + '</span>' + tiles(s.cols, s.base, i % 2 ? 'b' : 'a') + '</div>');
      if (shown < s.rows) rows.push('<div class="vrow"><span class="tdots">… ' + (s.rows - shown) + ' more copies …</span></div>');
      return '<div class="vis">' + rows.join('') + '<p class="vcap">' + M(P(Par(P(bAst(s.base), s.cols)), s.rows)) + ' is ' + s.rows + ' copies of ' + M(P(bAst(s.base), s.cols)) + ': ' + s.rows + ' rows of ' + s.cols + ' factors = ' + s.rows + ' × ' + s.cols + ' = ' + s.total + ' factors, so ' + M(P(bAst(s.base), s.total)) + '.</p></div>';
    }
    case 'cancel': {
      const c = Math.min(s.top, s.bottom), lt = s.top - c, lb = s.bottom - c, B = bAst(s.base);
      const top = tiles(c, s.base, 'x', 9) + tiles(lt, s.base, 'a', 9), bot = tiles(c, s.base, 'x', 9) + tiles(lb, s.base, 'b', 9);
      let cap;
      if (s.solve) cap = 'For the top to leave ' + M(P(B, s.solve.c)) + ' = ' + commas(String(s.solve.V)) + ' after ' + s.solve.k + ' factors cancel, it needs ' + s.solve.k + ' + ' + s.solve.c + ' = ' + (s.solve.k + s.solve.c) + ' factors. So <i>n</i> = ' + (s.solve.k + s.solve.c) + '.';
      else if (s.zero) cap = 'The same number of factors on top and bottom: they all cancel and leave 1. The exponent rule says ' + M(Fr(P(B, s.top), P(B, s.bottom))) + ' = ' + M(P(B, Ar(s.top, '−', s.bottom))) + ' = ' + M(P(B, 0)) + ', so ' + M(P(B, 0)) + ' must be 1.';
      else {
        cap = (s.fromNeg ? M(P(B, -s.bottom)) + ' means one over ' + M(P(B, s.bottom)) + ', so it goes on the bottom. ' : '') +
              (s.fromPow ? M(P(Par(P(B, s.fromPow[0])), s.fromPow[1])) + ' is ' + s.fromPow[1] + ' × ' + s.fromPow[0] + ' = ' + s.top + ' factors on top. ' : '') +
              'Each factor on the bottom cancels one on top: ' + c + (c === 1 ? ' pair cancels. ' : ' pairs cancel. ') +
              (lt > 0 ? s.top + ' − ' + s.bottom + ' = ' + lt + (lt === 1 ? ' factor is' : ' factors are') + ' left on top: ' + M(P(B, lt)) + '.' : lb > 0 ? s.bottom + ' − ' + s.top + ' = ' + lb + (lb === 1 ? ' factor is' : ' factors are') + ' left on the bottom: ' + M(Fr(1, P(B, lb))) + '.' : 'Nothing is left but 1.');
        if (s.numbers) cap = 'The numbers divide: ' + s.numbers[0] + ' ÷ ' + s.numbers[1] + ' = ' + s.numbers[2] + '. ' + cap;
      }
      return '<div class="vis vcancel"><div class="vrow">' + top + '</div><div class="vbar"></div><div class="vrow">' + bot + '</div><p class="vcap">' + cap + '</p></div>';
    }
    case 'ladder': {
      const b = s.base, bq = b && b.letter ? null : b && b.frac ? Q(1n, BigInt(b.frac)) : Q(BigInt(b)), B = bAst(b);
      const hi = s.high != null ? s.high : 3, lo = s.low, rows = [], marks = s.mark || [lo];
      for (let j = hi; j >= Math.min(lo, -1); j--) {
        const val = bq ? valueHtml(qpow(bq, BigInt(j))) : (j > 1 ? M(P(B, j)) : j === 1 ? M(B) : j === 0 ? '1' : j === -1 ? M(Fr(1, B)) : M(Fr(1, P(B, -j))));
        rows.push('<tr class="' + (marks.indexOf(j) >= 0 ? 'hl' : '') + '"><td class="lp">' + M(P(B, j)) + '</td><td class="le">=</td><td class="lv">' + val + '</td><td class="ld">' + (j > Math.min(lo, -1) ? '÷ ' + bHtml(b) : '') + '</td></tr>');
      }
      let cap = 'Each step down, the exponent goes down by 1, so you divide by ' + bHtml(b) + ' once more. ';
      if (s.note === 'zero') cap += 'One step below ' + M(P(B, 1)) + ' = ' + bHtml(b) + ' is ' + bHtml(b) + ' ÷ ' + bHtml(b) + ' = 1. That is why ' + M(P(B, 0)) + ' = 1.';
      else cap += 'Past ' + M(P(B, 0)) + ' = 1, the values become one over the powers: that is what a negative exponent means.';
      if (s.coef != null) cap += ' The ' + s.coef + ' in front just multiplies: ' + s.coef + ' · ' + M(Fr(1, P(B, -s.low))) + ' = ' + M(Fr(s.coef, P(B, -s.low))) + '.';
      if (s.note === 'negDen') cap += ' The question has ' + M(P(B, s.low)) + ' on the bottom, which is one over ' + M(P(B, -s.low)) + '; one over one over something is that something: ' + M(P(B, -s.low)) + '.';
      return '<div class="vis"><table class="ladder">' + rows.join('') + '</table><p class="vcap">' + cap + '</p></div>';
    }
    case 'signs': {
      const pairs = Math.floor(s.e / 2), left = s.e % 2;
      const t = '<span class="tile b">−' + s.c + '</span>';
      let h = ''; for (let i = 0; i < pairs; i++) h += '<span class="vpair">' + t + t + '<span class="vlab">+</span></span>';
      if (left) h += '<span class="vpair odd">' + t + '<span class="vlab">−</span></span>';
      return '<div class="vis"><div class="vrow">' + h + '</div><p class="vcap">' + M(P(Par(Neg(N(s.c))), s.e)) + ' has ' + s.e + ' negative factors. Each pair of negatives multiplies to a positive; ' + (left ? 'with an odd number, one negative is left over, so the result is negative.' : 'with an even number, none are left over, so the result is positive.') + '</p></div>';
    }
    case 'copies': {
      const q = s.copies, fac = s.frac ? Fr(s.parts[0].n, s.parts[1].n) : Mul('', ...s.parts.map(p => p.letter ? (p.e === 1 ? V(p.letter) : P(V(p.letter), p.e)) : N(p.n)));
      const row = Array(Math.min(q, 5)).fill('<span class="vcopy">' + M(Par(fac)) + '</span>').join('<span class="vop">·</span>') + (q > 5 ? '<span class="tdots">… ' + q + ' copies</span>' : '');
      const gather = s.parts.map(p => {
        if (p.letter) return '<li>' + (p.e === 1 ? 'Each copy has one <i>' + p.letter + '</i>: ' : 'Each copy has ' + M(P(V(p.letter), p.e)) + ': ') + q + ' × ' + (p.e < 0 ? '(' + String(p.e).replace('-', '−') + ')' : p.e) + ' = ' + String(p.e * q).replace('-', '−') + ', so ' + M(P(V(p.letter), p.e * q)) + '.</li>';
        const tms = Array(q).fill(p.n).join(' · ');
        return '<li>' + (p.of ? 'The ' + p.of + ': ' : 'The number: ') + tms + ' = ' + qpow(qi(p.n), BigInt(q)).n + '.</li>';
      }).join('');
      return '<div class="vis"><div class="vrow">' + row + '</div><ul class="vlist">' + gather + '</ul><p class="vcap">An exponent outside the parentheses makes copies of everything inside. Gather the matching pieces.</p></div>';
    }
    case 'hop': {
      const n = s.cells.length, W = 24, H = 74, w = n * W + 20;
      const from = s.dir === 'toSci' ? s.spos : s.cpos, to = s.dir === 'toSci' ? s.cpos : s.spos, step = to > from ? 1 : -1;
      let svg = '<svg class="hop" viewBox="0 0 ' + w + ' ' + H + '" width="' + w + '" height="' + H + '" role="img" aria-label="The decimal point moves ' + Math.abs(s.k) + ' places">';
      for (let i = 0; i < n; i++) {
        const pad = i >= s.pad[0] && i < s.pad[1];
        svg += '<rect x="' + (10 + i * W + 2) + '" y="34" width="' + (W - 4) + '" height="30" rx="5" class="' + (pad ? 'hpad' : 'hcell') + '"/><text x="' + (10 + i * W + W / 2) + '" y="55" text-anchor="middle" class="ht">' + s.cells[i] + '</text>';
      }
      let k = 0;
      for (let p = from; p !== to; p += step) { k++;
        const x1 = 10 + p * W, x2 = 10 + (p + step) * W, mx = (x1 + x2) / 2;
        svg += '<path d="M' + x1 + ' 32 Q' + mx + ' 8 ' + x2 + ' 32" class="harc"/><text x="' + mx + '" y="15" text-anchor="middle" class="hk">' + k + '</text>'; }
      svg += '<circle cx="' + (10 + from * W) + '" cy="64" r="3.6" class="hfrom"/><circle cx="' + (10 + to * W) + '" cy="64" r="4.2" class="hto"/></svg>';
      const big = s.k > 0, std = commas(decStr(qmul(qdec(s.c), qpow(Q(10), BigInt(s.k)))));
      const cap = s.dir === 'toSci'
        ? 'The decimal point moves from where it is in ' + std + ' (gray dot) to just after the first digit (blue dot): ' + Math.abs(s.k) + ' places ' + (big ? 'left' : 'right') + '. ' + (big ? 'A big number, so the exponent is +' + s.k : 'A number less than 1, so the exponent is −' + (-s.k)) + '.'
        : 'Start with the point in ' + s.c + ' (gray dot) and move it ' + Math.abs(s.k) + ' places ' + (big ? 'right' : 'left') + ' (blue dot). The shaded boxes are the zeros you fill in. That gives ' + std + '.';
      return '<div class="vis"><div class="hopwrap">' + svg + '</div><p class="vcap">' + cap + '</p></div>';
    }
  }
  return '';
}
function valueHtml(q) {
  const neg = q.n < 0n, n = neg ? -q.n : q.n;
  const a = q.d === 1n ? N(n.toString(), { commas: true }) : Fr(N(n.toString(), { commas: true }), N(q.d.toString(), { commas: true }));
  return M(neg ? Neg(a) : a);
}

const api = { spec, html, hopSpec };
if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.Visual = api;
})(this);
