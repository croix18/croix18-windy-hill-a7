/* A7 Unit 6 practice: the figures (drawn to their own numbers) and the "why it works" pictures. The drawing board is M7 Unit
   4's (m7/practice/u4/fig.js), grown for this unit: a coordinate grid whose pale lines a label may sit over, while the axes and
   every side may not be crossed; labels beside a point as well as along a segment. Every figure is built as a model first —
   drawn segments, and labels that each name the segment they measure — so u6_check.js can prove, for thousands of sets, that
   every printed length is the length drawn, that each label sits nearest its own segment and crosses no line, and that no two
   labels overlap (ruling 44). */
(function (root) {
'use strict';
const E = (typeof module !== 'undefined' && module.exports) ? require('./engine.js') : root.Practice;
const { minus } = E;

/* ------------------------------------------------------------------ a drawing in geometry units (y up), mapped to pixels */
function textW(s) { const t = String(s).replace(/<[^>]+>/g, ''); let w = 0; for (const ch of t) w += /[0-9]/.test(ch) ? 8.6 : ch === ' ' ? 4 : /[.,]/.test(ch) ? 4.2 : /[()]/.test(ch) ? 5.2 : ch === '−' ? 9 : 9.6; return w + 3; }   /* bold 13px, sized for the widest common sans fonts */
function segD(p, a, b) { const dx = b[0] - a[0], dy = b[1] - a[1], L2 = dx * dx + dy * dy; let t = L2 ? ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / L2 : 0; t = Math.max(0, Math.min(1, t)); return Math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy); }
function boxesHit(a, b) { return a[0] < b[2] && b[0] < a[2] && a[1] < b[3] && b[1] < a[3]; }
function segsCross(p1, p2, p3, p4) {
  const d = (a, b, c) => (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
  const d1 = d(p3, p4, p1), d2 = d(p3, p4, p2), d3 = d(p1, p2, p3), d4 = d(p1, p2, p4);
  return ((d1 > 0) !== (d2 > 0)) && ((d3 > 0) !== (d4 > 0));
}
function boxHitsSeg(box, a, b) {
  const sh = [box[0] + 1, box[1] + 1, box[2] - 1, box[3] - 1];
  const inside = p => p[0] > sh[0] && p[0] < sh[2] && p[1] > sh[1] && p[1] < sh[3];
  if (inside(a) || inside(b)) return true;
  const c = [[sh[0], sh[1]], [sh[2], sh[1]], [sh[2], sh[3]], [sh[0], sh[3]]];
  for (let i = 0; i < 4; i++) if (segsCross(a, b, c[i], c[(i + 1) % 4])) return true;
  return false;
}
function Board(g0, g1, maxW, maxH) {
  const k = Math.min(maxW / (g1[0] - g0[0]), maxH / (g1[1] - g0[1]));
  const px = p => [(p[0] - g0[0]) * k, (g1[1] - p[1]) * k];
  const B = { k, px, els: [], segs: [], labels: [], pts: [], keep: [] };
  const fmt = v => (Math.round(v * 10) / 10).toString();
  const P = p => { const q = px(p); B.pts.push(q); return fmt(q[0]) + ',' + fmt(q[1]); };
  B.fmt = fmt;
  B.poly = (pts, cls, line) => { B.els.push('<polygon class="' + (cls || 'ln') + '" points="' + pts.map(P).join(' ') + '"/>'); if (line !== false) for (let i = 0; i < pts.length; i++) B.segs.push([px(pts[i]), px(pts[(i + 1) % pts.length]), cls]); };
  B.fill = (pts, cls) => B.els.push('<polygon class="' + cls + '" points="' + pts.map(P).join(' ') + '"/>');
  B.line = (a, b, cls, solid) => { const A = px(a), Bq = px(b); B.pts.push(A, Bq); B.els.push('<line class="' + (cls || 'ln') + '" x1="' + fmt(A[0]) + '" y1="' + fmt(A[1]) + '" x2="' + fmt(Bq[0]) + '" y2="' + fmt(Bq[1]) + '"/>'); if (solid !== false) B.segs.push([A, Bq, cls]); };
  B.ra = (p, u, v, s) => { s = s || 8; const c = px(p), lu = Math.hypot(u[0], u[1]) || 1, lv = Math.hypot(v[0], v[1]) || 1, U = [u[0] / lu * s, -u[1] / lu * s], V = [v[0] / lv * s, -v[1] / lv * s];
    B.els.push('<polyline class="ra" points="' + [[c[0] + U[0], c[1] + U[1]], [c[0] + U[0] + V[0], c[1] + U[1] + V[1]], [c[0] + V[0], c[1] + V[1]]].map(q => fmt(q[0]) + ',' + fmt(q[1])).join(' ') + '"/>'); };
  B.dot = (p, r) => { const q = px(p); B.pts.push(q); B.els.push('<circle class="dot" cx="' + fmt(q[0]) + '" cy="' + fmt(q[1]) + '" r="' + (r || 3.2) + '"/>'); B.keep.push([q[0] - 4, q[1] - 4, q[0] + 4, q[1] + 4]); };
  /* a label for the segment a–b, on the side away from `inside` (a geometry point); `v` is the length it states (or null) */
  B.lab = (a, b, s, v, inside, o) => {
    o = o || {};
    const A = px(a), Bp = px(b), I = px(inside);
    let dx = Bp[0] - A[0], dy = Bp[1] - A[1]; const L = Math.hypot(dx, dy) || 1; dx /= L; dy /= L;
    let n = [-dy, dx];
    const ts = o.ts || [0.5, 0.4, 0.6, 0.3, 0.7, 0.22, 0.78];
    const mid0 = [(A[0] + Bp[0]) / 2, (A[1] + Bp[1]) / 2];
    if ((mid0[0] - I[0]) * n[0] + (mid0[1] - I[1]) * n[1] < 0) n = [-n[0], -n[1]];
    const tw = textW(s), th = 14;
    let best = null, forced = true;
    const tries = []; ts.forEach(t => tries.push([t, 1, 0])); [6, 12].forEach(g => ts.forEach(t => tries.push([t, 1, g]))); if (o.both) ts.forEach(t => tries.push([t, -1, 0]));
    for (const [t, sg, extra] of tries) {
      const m = [A[0] + (Bp[0] - A[0]) * t, A[1] + (Bp[1] - A[1]) * t];
      const off = 5 + Math.abs(n[0]) * tw / 2 + Math.abs(n[1]) * th / 2 + (o.gap || 0) + extra;
      const c = [m[0] + sg * n[0] * off, m[1] + sg * n[1] * off];
      const box = [c[0] - tw / 2, c[1] - th / 2, c[0] + tw / 2, c[1] + th / 2];
      const dOwn = segD(c, A, Bp), clash = B.segs.some(sq => boxHitsSeg(box, sq[0], sq[1])) || B.labels.some(l => boxesHit(box, l.box) || (l.a && segD(c, l.a, l.b) < dOwn + 0.5)) || B.keep.some(kb => boxesHit(box, kb));
      if (!best) best = { c, box };
      if (!clash) { best = { c, box }; forced = false; break; }
    }
    B.labels.push({ s, v, a: A, b: Bp, ga: a, gb: b, x: best.c[0], y: best.c[1], box: best.box, tol: o.tol || 0, forced });
    B.pts.push([best.box[0], best.box[1]], [best.box[2], best.box[3]]);
  };
  /* a label beside a point (a corner's name, "A(−7, 1)"): the first of the four diagonal places, then the four sides, that
     touches no line, no other label, no other point and no number on the axes, inside the plane if it can be; `away` (a
     geometry point) is tried last. Outside the plane it can only be above it or to its right: the axes' numbers are kept
     clear below and to the left. */
  B.ptLab = (p, s, away, cls) => {
    const c0 = px(p), tw = textW(s), th = 14, g = 4;
    let dirs = [[1, -1], [-1, -1], [1, 1], [-1, 1], [0, -1], [0, 1], [1, 0], [-1, 0]];
    if (away) { const A = px(away), vx = c0[0] - A[0], vy = c0[1] - A[1]; dirs = dirs.slice().sort((d1, d2) => (d2[0] * vx + d2[1] * vy) / Math.hypot(d2[0], d2[1]) - (d1[0] * vx + d1[1] * vy) / Math.hypot(d1[0], d1[1])); }
    const cands = [];
    for (const extra of [0, 5, 10]) for (const [ux, uy] of dirs) {
      const cx = c0[0] + ux * (tw / 2 + g + extra) * (ux ? 1 : 0), cy = c0[1] + uy * (th / 2 + g + extra) * (uy ? 1 : 0);
      cands.push({ c: [cx, cy], box: [cx - tw / 2, cy - th / 2, cx + tw / 2, cy + th / 2] });
    }
    const clear = box => !(B.segs.some(sq => boxHitsSeg(box, sq[0], sq[1])) || B.labels.some(l => boxesHit(box, l.box)) || B.keep.some(kb => boxesHit(box, kb) && !(Math.abs(kb[0] + 4 - c0[0]) < 0.01 && Math.abs(kb[1] + 4 - c0[1]) < 0.01)));
    const inside = box => !B.frame || (box[0] >= B.frame[0] && box[2] <= B.frame[2] && box[1] >= B.frame[1] && box[3] <= B.frame[3]);
    const aboveRight = box => !B.frame || (box[0] >= B.frame[0] && box[3] <= B.frame[3]);
    const good = cands.find(c => clear(c.box) && inside(c.box)) || cands.find(c => clear(c.box) && aboveRight(c.box)), best = good || cands[0];
    B.labels.push({ s, v: null, pt: c0, x: best.c[0], y: best.c[1], box: best.box, cls: cls || 'lab', forced: !good });
    B.pts.push([best.box[0], best.box[1]], [best.box[2], best.box[3]]);
  };
  B.text = (p, s, cls, dy) => { const q = px(p); q[1] += dy || 0; const tw = textW(s); B.pts.push([q[0] - tw / 2, q[1] - 8], [q[0] + tw / 2, q[1] + 8]); B.els.push('<text class="' + (cls || 'tx') + '" x="' + fmt(q[0]) + '" y="' + fmt(q[1]) + '">' + s + '</text>'); B.keep.push([q[0] - tw / 2, q[1] - 7, q[0] + tw / 2, q[1] + 7]); };
  B.svg = (cls, alt) => {
    const xs = B.pts.map(p => p[0]), ys = B.pts.map(p => p[1]);
    const x0 = Math.min(...xs) - 4, y0 = Math.min(...ys) - 4, w = Math.max(...xs) + 4 - x0, h = Math.max(...ys) + 4 - y0;
    B.view = [x0, y0, w, h];
    return '<svg class="fig ' + (cls || '') + '" viewBox="' + [x0, y0, w, h].map(fmt).join(' ') + '" style="max-width:' + Math.ceil(w * 1.05) + 'px" role="img" aria-label="' + E.esc(alt) + '">' + B.els.join('') +
      B.labels.map(l => '<text class="' + (l.cls || 'lab') + '" x="' + fmt(l.x) + '" y="' + fmt(l.y) + '">' + l.s + '</text>').join('') + '</svg>';
  };
  return B;
}

/* ------------------------------------------------------------------ the coordinate grid */
/* the plane from x0…x1 and y0…y1 (each including 0): pale unit lines under everything, the two axes, their numbers outside
   the plane (below it and to its left) where nothing else is drawn, and x and y at the axes' ends */
function plane(x0, x1, y0, y1, maxW, maxH) {
  const B = Board([x0 - 1.6, y0 - 1.3], [x1 + 0.9, y1 + 0.9], maxW, maxH), k = B.k, f = B.fmt;
  const d = [];
  for (let x = x0; x <= x1; x++) { const a = B.px([x, y0]), b = B.px([x, y1]); d.push('M' + f(a[0]) + ' ' + f(a[1]) + 'V' + f(b[1])); }
  for (let y = y0; y <= y1; y++) { const a = B.px([x0, y]), b = B.px([x1, y]); d.push('M' + f(a[0]) + ' ' + f(a[1]) + 'H' + f(b[0])); }
  B.els.push('<path class="gridln" d="' + d.join('') + '"/>');
  const a0 = B.px([x0, y0]), a1 = B.px([x1, y1]); B.pts.push(a0, a1);
  B.frame = [a0[0], a1[1], a1[0], a0[1]];                                          /* point labels stay inside the plane */
  B.line([x0, 0], [x1, 0], 'axis'); B.line([0, y0], [0, y1], 'axis');
  const ox = B.px([x1, 0]), oy = B.px([0, y1]);
  B.els.push('<text class="tx mut ax" x="' + f(ox[0] + 10) + '" y="' + f(ox[1]) + '">x</text>'); B.pts.push([ox[0] + 17, ox[1]]); B.keep.push([ox[0] + 3, ox[1] - 7, ox[0] + 17, ox[1] + 7]);
  B.els.push('<text class="tx mut ax" x="' + f(oy[0]) + '" y="' + f(oy[1] - 10) + '">y</text>'); B.pts.push([oy[0], oy[1] - 18]); B.keep.push([oy[0] - 6, oy[1] - 17, oy[0] + 6, oy[1] - 3]);
  const step = k >= 19 ? 1 : 2;
  const tickW = s => { let w = 0; for (const ch of String(s)) w += ch === '−' ? 7 : 6.6; return w + 2; };          /* 10.5px numbers */
  for (let x = x0; x <= x1; x++) if (x % step === 0) { const q = B.px([x, y0]), s = minus(String(x)), w = tickW(s); B.els.push('<text class="tick" x="' + f(q[0]) + '" y="' + f(q[1] + 11) + '">' + s + '</text>'); B.pts.push([q[0], q[1] + 18]); B.keep.push([q[0] - w / 2, q[1] + 5, q[0] + w / 2, q[1] + 17]); }
  for (let y = y0; y <= y1; y++) if (y % step === 0) { const q = B.px([x0, y]), s = minus(String(y)), w = tickW(s); B.els.push('<text class="tick" x="' + f(q[0] - 12) + '" y="' + f(q[1]) + '">' + s + '</text>'); B.pts.push([q[0] - 24, q[1]]); B.keep.push([q[0] - 12 - w / 2, q[1] - 6, q[0] - 12 + w / 2, q[1] + 6]); }
  B.step = step;
  return B;
}
/* the plane around some points (and the origin), drawn by `draw`: a unit's margin below and to the left and two above and to
   the right at first, wider until every label finds a clear place (a point's name may hang over the top or right edge, never
   over the axes' numbers below and to the left) */
const MARGINS = [[1, 2, 1, 2], [2, 2, 1, 2], [1, 3, 1, 2], [2, 3, 2, 2], [2, 3, 2, 3], [3, 3, 2, 3], [3, 4, 3, 3], [4, 4, 3, 4], [5, 4, 3, 4], [6, 4, 3, 4], [7, 4, 4, 4], [8, 5, 4, 5]];
function onPlane(pts, draw) {
  const xs = pts.map(p => p[0]).concat([0]), ys = pts.map(p => p[1]).concat([0]);
  let B = null;
  for (const [l, r, b, t] of MARGINS) {
    B = plane(Math.min(...xs) - l, Math.max(...xs) + r, Math.min(...ys) - b, Math.max(...ys) + t, 300, 280);
    draw(B);
    if (!B.labels.some(x => x.forced)) return B;
  }
  return B;
}
const ptName = (x, y, n) => n + '(' + minus(String(x)) + ', ' + minus(String(y)) + ')';

/* ------------------------------------------------------------------ the question figures */
const rot = (p, deg) => { const t = deg * Math.PI / 180; return [p[0] * Math.cos(t) - p[1] * Math.sin(t), p[0] * Math.sin(t) + p[1] * Math.cos(t)]; };
function rtriPts(f) {
  const [L1, L2] = f.legs, s = f.flip ? -1 : 1;
  return [[0, 0], [s * L1, 0], [0, L2]].map(p => rot(p, f.turn || 0));
}
function rtri(f) {
  const P = rtriPts(f), xs = P.map(p => p[0]), ys = P.map(p => p[1]), span = Math.max(Math.max(...xs) - Math.min(...xs), Math.max(...ys) - Math.min(...ys));
  const B = Board([Math.min(...xs), Math.min(...ys)], [Math.max(...xs), Math.max(...ys)], 190, 150);
  const cen = [(P[0][0] + P[1][0] + P[2][0]) / 3, (P[0][1] + P[1][1] + P[2][1]) / 3];
  B.fill(P, 'sh'); B.poly(P);
  B.ra(P[0], [P[1][0] - P[0][0], P[1][1] - P[0][1]], [P[2][0] - P[0][0], P[2][1] - P[0][1]], 9);
  B.lab(P[0], P[1], f.labs[0], f.vals[0], cen, { tol: 1e-6 });
  B.lab(P[0], P[2], f.labs[1], f.vals[1], cen, { tol: 1e-6 });
  B.lab(P[1], P[2], f.labs[2], f.vals[2], cen, { tol: 1e-6 });
  B.meta = { span };
  return B;
}
function grid2(f) {
  return onPlane(f.pts, B => {
    f.pts.forEach(p => B.dot([p[0], p[1]]));
    f.pts.forEach((p, i) => B.ptLab([p[0], p[1]], ptName(p[0], p[1], p[2]), f.pts[1 - i]));
  });
}
function gridTri(f) {
  const V = f.pts.map(p => [p[0], p[1]]), cen = [(V[0][0] + V[1][0] + V[2][0]) / 3, (V[0][1] + V[1][1] + V[2][1]) / 3];
  return onPlane(V, B => {
    B.fill(V, 'sh'); B.poly(V); V.forEach(p => B.dot(p, 2.6));
    f.pts.forEach(p => B.ptLab([p[0], p[1]], p[2], cen));
  });
}
/* a triangle from its three sides: r along the bottom, p up the left, q up the right */
function triPts(p, q, r) { const x = (p * p - q * q + r * r) / (2 * r); return [[0, 0], [r, 0], [x, Math.sqrt(Math.max(p * p - x * x, 0))]]; }
function simPair(f) {
  const A = triPts(f.a[0], f.a[1], f.a[2]);
  let C = triPts(f.b[0], f.b[1], f.b[2]);
  if (f.turn === '180') C = C.map(p => [-p[0], -p[1]]); else C = C.map(p => [-p[0], p[1]]);
  const ax1 = Math.max(...A.map(p => p[0])), cx0 = Math.min(...C.map(p => p[0])), gap = Math.max(f.a[2], f.b[2]) * 0.45 + 1;
  const dy = Math.min(...A.map(p => p[1])) - Math.min(...C.map(p => p[1]));
  C = C.map(p => [p[0] - cx0 + ax1 + gap, p[1] + dy]);
  const all = A.concat(C), xs = all.map(p => p[0]), ys = all.map(p => p[1]);
  const B = Board([Math.min(...xs), Math.min(...ys)], [Math.max(...xs), Math.max(...ys)], 320, 140);
  [A, C].forEach((T, j) => {
    const cen = [(T[0][0] + T[1][0] + T[2][0]) / 3, (T[0][1] + T[1][1] + T[2][1]) / 3], labs = j ? f.lb : f.la, sides = j ? f.b : f.a;
    B.fill(T, 'sh'); B.poly(T);
    const num = (s, i) => s === 'x' ? null : sides[i];
    B.lab(T[0], T[2], labs[0], num(labs[0], 0), cen, { tol: 1e-6 });
    B.lab(T[1], T[2], labs[1], num(labs[1], 1), cen, { tol: 1e-6 });
    B.lab(T[0], T[1], labs[2], num(labs[2], 2), cen, { tol: 1e-6 });
  });
  B.meta = { A, C };
  return B;
}
function shadow(f) {
  const { h1, s1, s2, h2 } = f, X2 = s1 + Math.max(s1, s2) * 0.45 + 2, right = X2 + s2;
  const B = Board([-0.5 - s1 * 0.25, 0], [right + s2 * 0.08, h2], 300, 190);
  B.line([-s1 * 0.25 - 0.4, 0], [right + s2 * 0.08, 0], 'ln thin');
  B.fill([[0, 0], [s1, 0], [0, h1]], 'sh'); B.fill([[X2, 0], [X2 + s2, 0], [X2, h2]], 'sh');
  B.line([0, 0], [0, h1]); B.line([X2, 0], [X2, h2]);
  B.line([0, h1], [s1, 0], 'dash'); B.line([X2, h2], [X2 + s2, 0], 'dash');
  B.ra([0, 0], [1, 0], [0, 1], 6); B.ra([X2, 0], [1, 0], [0, 1], 8);
  B.lab([0, 0], [0, h1], f.lab[0], h1, [1, h1 / 2], { tol: 1e-6 });
  B.lab([0, 0], [s1, 0], f.lab[1], s1, [s1 / 2, 1], { tol: 1e-6 });
  B.lab([X2, 0], [X2 + s2, 0], f.lab[2], s2, [X2 + s2 / 2, 1], { tol: 1e-6 });
  B.lab([X2, 0], [X2, h2], f.lab[3], null, [X2 + 1, h2 / 2]);
  B.text([0, h1], f.what[0], 'tx mut', -12); B.text([X2, h2], f.what[1], 'tx mut', -12);
  return B;
}
function mirror(f) {
  const { h1, d1, d2, h2 } = f, X2 = d1 + d2;
  const B = Board([-d1 * 0.35 - 0.5, 0], [X2 + d2 * 0.12 + 0.5, h2], 300, 190);
  B.line([-d1 * 0.35 - 0.5, 0], [X2 + d2 * 0.12 + 0.5, 0], 'ln thin');
  B.fill([[0, 0], [d1, 0], [0, h1]], 'sh'); B.fill([[d1, 0], [X2, 0], [X2, h2]], 'sh');
  B.line([0, 0], [0, h1]); B.line([X2, 0], [X2, h2]);
  B.line([X2, h2], [d1, 0], 'dash'); B.line([d1, 0], [0, h1], 'dash');
  const m = B.px([d1, 0]); B.els.push('<line class="mirror" x1="' + B.fmt(m[0] - 7) + '" y1="' + B.fmt(m[1]) + '" x2="' + B.fmt(m[0] + 7) + '" y2="' + B.fmt(m[1]) + '"/>');
  B.ra([0, 0], [1, 0], [0, 1], 6); B.ra([X2, 0], [-1, 0], [0, 1], 8);
  B.lab([0, 0], [0, h1], f.lab[0], h1, [1, h1 / 2], { tol: 1e-6 });
  B.lab([0, 0], [d1, 0], f.lab[1], d1, [d1 / 2, 1], { tol: 1e-6 });
  B.lab([d1, 0], [X2, 0], f.lab[2], d2, [d1 + d2 / 2, 1], { tol: 1e-6 });
  B.lab([X2, 0], [X2, h2], f.lab[3], null, [X2 - 1, h2 / 2]);
  B.text([0, h1], f.what[0], 'tx mut', -12); B.text([X2, h2], f.what[1], 'tx mut', -12);
  B.text([d1, 0], 'mirror', 'tx mut', 30);
  return B;
}
const FIG = { rtri, grid2, gridTri, simPair, shadow, mirror };
function figModel(f) { const B = FIG[f.kind](f); B.html = B.svg('q', altOf(f)); return B; }
/* what a screen reader says for each figure: every length, and which one is unknown */
function altOf(f) {
  switch (f.kind) {
    case 'rtri': return 'A right triangle. The legs are labeled ' + f.labs[0] + ' and ' + f.labs[1] + '; the side across from the right angle is labeled ' + f.labs[2] + '.';
    case 'grid2': return 'A coordinate plane with ' + f.pts.map(p => 'point ' + ptName(p[0], p[1], p[2])).join(' and ') + '.';
    case 'gridTri': return 'A coordinate plane with triangle ' + f.pts.map(p => p[2]).join('') + ': ' + f.pts.map(p => ptName(p[0], p[1], p[2])).join(', ') + '.';
    case 'simPair': return 'Two similar triangles. The first has sides ' + f.la.join(', ') + '. The second, turned, has sides ' + f.lb.join(', ') + '.';
    case 'shadow': return 'The ' + f.what[0] + ', ' + f.lab[0] + ' tall, and a ' + f.lab[1] + ' shadow; the ' + f.what[1] + ', h tall, and a ' + f.lab[2] + ' shadow. The sun\'s rays are dashed.';
    case 'mirror': return f.what[0] + '\'s eyes, ' + f.lab[0] + ' up, ' + f.lab[1] + ' from a mirror on the ground; the ' + f.what[1] + ', h tall, ' + f.lab[2] + ' beyond the mirror. The light\'s path is dashed.';
  }
  return 'Figure';
}
function figHtml(f) { return f ? '<div class="qfig">' + figModel(f).html + '</div>' : ''; }

/* ------------------------------------------------------------------ "why it works" pictures: each returns a model and a caption */
function pic(B, cap, alt) { B.html = '<div class="vis">' + B.svg('why', alt) + '<p class="vcap">' + cap + '</p></div>'; B.cap = cap; return B; }
/* two points, the slanted segment, and the right triangle under it with its legs measured */
function legsPic(x, what) {
  const P1 = [x.x1, x.y1], P2 = [x.x2, x.y2], Cn = [x.x2, x.y1], dx = Math.abs(x.x2 - x.x1), dy = Math.abs(x.y2 - x.y1);
  const mid = [(P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2];
  const B = onPlane([P1, P2], B => {
  B.line(P1, Cn, 'dash'); B.line(Cn, P2, 'dash'); B.line(P1, P2, 'hl');
  B.ra(Cn, [P1[0] - Cn[0], 0], [0, P2[1] - Cn[1]], 7);
  B.dot(P1); B.dot(P2);
  /* a leg that crosses the other axis keeps its number off that axis (6.05 Notes III, 24 Oct: a "5" against the y-axis reads
     as the axis's own 5): its first places are the middle of the leg's longer piece */
  const offAxis = (a, b) => { const lo = Math.min(a, b), hi = Math.max(a, b); if (!(lo < 0 && 0 < hi)) return undefined;
    const m = -lo >= hi ? lo / 2 : hi / 2, t = (m - a) / (b - a); return [t, t - 0.08, t + 0.08, 0.5, 0.4, 0.6, 0.3, 0.7]; };
  B.lab(P1, Cn, String(dx), dx, mid, { tol: 1e-9, both: true, ts: offAxis(P1[0], Cn[0]) });
  B.lab(Cn, P2, String(dy), dy, mid, { tol: 1e-9, both: true, ts: offAxis(Cn[1], P2[1]) });
  });
  const n = dx * dx + dy * dy, r = E.isSquare(n) ? String(E.isqrt(n)) : (E.rootOK(n) ? '√' + n : 'the square root of ' + n) + ' ≈ ' + E.numStr(E.sqrtTenth(n));
  return pic(B, 'The legs of the right triangle are the distance across, ' + dx + ', and the distance ' + (x.y2 > x.y1 ? 'up' : 'down') + ', ' + dy + '. ' + (what || 'The distance') + ' is its hypotenuse: ' + dx + '² + ' + dy + '² = ' + n + ', so it is ' + r + '.', 'The right triangle under the segment, legs ' + dx + ' and ' + dy);
}
const WHY = {
  gridWhole: x => legsPic(x.prm), coordTenth: x => legsPic(x.prm), straight: x => legsPic(x.prm, 'The straight line'),
  streets: x => { const w = legsPic(x.prm, 'The straight line'), dx = Math.abs(x.prm.x2 - x.prm.x1), dy = Math.abs(x.prm.y2 - x.prm.y1);
    const cap = 'Along the streets you walk the two dashed legs: ' + dx + ' across and ' + dy + ' ' + (x.prm.y2 > x.prm.y1 ? 'up' : 'down') + ', ' + (dx + dy) + ' blocks. The straight line, the hypotenuse, is shorter.';
    w.html = w.html.replace(w.cap, cap); w.cap = cap; return w; }
};
function why(x) { try { const f = WHY[x.fam]; return f ? f(x) : null; } catch (e) { return null; } }

const api = { figModel, figHtml, altOf, why, WHY, textW, boxesHit, boxHitsSeg, segD, triPts, rtriPts, Board, plane };
if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.Fig = api;
})(this);
