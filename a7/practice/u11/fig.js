/* A7 Unit 11 practice: the figures — a coordinate plane with one or two lines drawn from their own equations, and two tables of
   values. Every line is drawn from its m and b and clipped to the window, so a crossing the key names is where the drawing
   crosses (the key's crossing is worked out from the equations, never typed). The first line is solid, the second dashed, as
   the lessons' figures are, so the two are told apart without colour; a legend under the plane says which is which. The grid
   has a line every unit (every half, pale, where an estimate is read), the axes' numbers every 1 or 2, and the plane is sized
   to read at 390 px. The <svg> carries its window and scale (data-win, data-px) so u11_check.js and verify.py can read every
   line back into the plane's own numbers. Lexend has no italics (ruling 46): the words on a figure are upright. */
(function (root) {
'use strict';
const E = (typeof module !== 'undefined' && module.exports) ? require('./engine.js') : root.Practice;
const { qnum, numStr } = E;
const f1 = v => (Math.round(v * 10) / 10).toString();
const mn = s => String(s).replace(/^-/, '−');

/* the two points where y = mx + b enters and leaves the window, left to right (exact, then as numbers); null if it misses it */
function clip(l, w) {
  const m = l.m, b = l.b, Q = E.Q, pts = [], X0 = Q(w.x0), X1 = Q(w.x1), Y0 = Q(w.y0), Y1 = Q(w.y1), inY = y => !E.qlt(y, Y0) && !E.qlt(Y1, y), inX = x => E.qlt(X0, x) && E.qlt(x, X1);
  [X0, X1].forEach(x => { const y = E.qadd(E.qmul(m, x), b); if (inY(y)) pts.push([x, y]); });
  if (m.n !== 0n) [Y0, Y1].forEach(y => { const x = E.qdiv(E.qsub(y, b), m); if (inX(x)) pts.push([x, y]); });
  const u = []; pts.forEach(p => { if (!u.some(q => E.qeq(q[0], p[0]) && E.qeq(q[1], p[1]))) u.push(p); });
  u.sort((p, q) => E.qlt(p[0], q[0]) ? -1 : 1);
  return u.length >= 2 ? [u[0], u[u.length - 1]] : null;
}
function plane(f) {
  const w = f.w, ys = w.ys || 1, nx = w.x1 - w.x0, ny = (w.y1 - w.y0) / ys, story = !!f.xname;
  const k = Math.min(300 / nx, 300 / ny), PX = x => (x - w.x0) * k, PY = y => (w.y1 - y) / ys * k;
  const el = [], d = [], d2 = [];
  for (let i = 0; i <= nx; i++) d.push('M' + f1(i * k) + ' 0V' + f1(ny * k));
  for (let j = 0; j <= ny; j++) d.push('M0 ' + f1(j * k) + 'H' + f1(nx * k));
  if (w.half) { for (let i = 0; i < nx; i++) d2.push('M' + f1((i + 0.5) * k) + ' 0V' + f1(ny * k)); for (let j = 0; j < ny; j++) d2.push('M0 ' + f1((j + 0.5) * k) + 'H' + f1(nx * k)); }
  if (d2.length) el.push('<path class="gridln2" d="' + d2.join('') + '"/>');
  el.push('<path class="gridln" d="' + d.join('') + '"/>');
  const ax = w.y0 <= 0 && 0 <= w.y1 ? PY(0) : null, ay = w.x0 <= 0 && 0 <= w.x1 ? PX(0) : null;
  if (ax != null) el.push('<line class="axis" x1="0" y1="' + f1(ax) + '" x2="' + f1(nx * k) + '" y2="' + f1(ax) + '"/>');
  if (ay != null) el.push('<line class="axis" x1="' + f1(ay) + '" y1="0" x2="' + f1(ay) + '" y2="' + f1(ny * k) + '"/>');
  /* the axes' numbers: below the plane and to its left, every 1 or every 2 grid lines */
  const step = k >= 21 ? 1 : 2, ticks = [];
  for (let i = 0; i <= nx; i++) { const x = w.x0 + i; if (x % step !== 0 || (x === 0 && !story && ay != null && ax != null && false)) continue;
    el.push('<text class="tick" x="' + f1(PX(x)) + '" y="' + f1(ny * k + 12) + '">' + mn(x) + '</text>'); ticks.push(['x', x]); }
  for (let j = 0; j <= ny; j++) { const y = w.y0 + j * ys; if ((j + Math.round(w.y0 / ys)) % step !== 0) continue;
    el.push('<text class="tick" x="-13" y="' + f1(PY(y)) + '">' + mn(y) + '</text>'); ticks.push(['y', y]); }
  /* the lines, clipped to the window: the first solid, the second dashed */
  const segs = [];
  f.lines.forEach((l, i) => { const c = clip(l, w); if (!c) return; const a = c[0].map(qnum), b = c[1].map(qnum);
    segs.push({ i, a: c[0], b: c[1] });
    el.push('<line class="' + (i ? 'ln2' : 'ln1') + '" data-line="' + i + '" x1="' + f1(PX(a[0])) + '" y1="' + f1(PY(a[1])) + '" x2="' + f1(PX(b[0])) + '" y2="' + f1(PY(b[1])) + '"/>'); });
  /* the axes' names: x and y at the axes' ends; a story's names under and beside the plane */
  let top = -10, bottom = ny * k + 22, left = -30, right = nx * k + 8;
  if (story) {
    el.push('<text class="axn" x="' + f1(nx * k / 2) + '" y="' + f1(ny * k + 30) + '">' + E.esc(f.xname) + '</text>'); bottom = ny * k + 38;
    el.push('<text class="axn" x="' + f1(-34) + '" y="' + f1(ny * k / 2) + '" transform="rotate(-90 ' + f1(-34) + ' ' + f1(ny * k / 2) + ')">' + E.esc(f.yname) + '</text>'); left = -44;
  } else {
    if (ax != null) { el.push('<text class="axn" x="' + f1(nx * k + 10) + '" y="' + f1(ax) + '">x</text>'); right = nx * k + 18; }
    if (ay != null) { el.push('<text class="axn" x="' + f1(ay) + '" y="-9">y</text>'); top = -18; }
  }
  const vb = [left, top, right - left, bottom - top];
  const alt = 'A coordinate plane from x = ' + w.x0 + ' to ' + w.x1 + ' and y = ' + w.y0 + ' to ' + w.y1 + (w.half ? ', with a pale line every half' : '') + '. ' +
    (f.both ? 'One line is drawn for both equations, ' + f.legend[0].replace(/<[^>]+>/g, '') + '.' : 'A solid line, ' + f.legend[0].replace(/<[^>]+>/g, '') + ', and a dashed line, ' + f.legend[1].replace(/<[^>]+>/g, '') + '.');
  const svg = '<svg class="fig plane" viewBox="' + vb.map(f1).join(' ') + '" style="max-width:' + Math.ceil(vb[2] * 1.12) + 'px" role="img" aria-label="' + E.esc(alt) + '" data-win="' + [w.x0, w.x1, w.y0, w.y1, ys].join(' ') + '" data-px="' + k.toFixed(4) + '">' + el.join('') + '</svg>';
  const key = (i, h) => '<span class="lk"><svg class="lks" viewBox="0 0 34 10" aria-hidden="true"><line class="' + (i ? 'ln2' : 'ln1') + '" x1="1" y1="5" x2="33" y2="5"/></svg><span class="lt">' + h + (f.story ? '' : '') + '</span></span>';
  const lg = f.both ? '<div class="lgd">' + key(0, 'both equations: ' + f.legend[0].split(' and ').map(t => E.M(t)).join(' and ')) + '</div>'
    : '<div class="lgd">' + f.legend.map((h, i) => key(i, (f.story ? E.esc(h) : E.M(h)) + (i ? ' (dashed)' : ' (solid)'))).join('') + '</div>';
  const cap = f.title ? '<div class="fcap">' + E.esc(f.title) + '</div>' : '';          /* the paper's caption: "PART (b): a different system" */
  return { html: '<div class="qfig">' + cap + svg + lg + '</div>', segs, ticks, k, w };
}
function tables(f) {
  const one = (t, ys) => '<table class="vt"><caption>' + E.M(t) + '</caption><tr><th scope="row">' + E.M('<i>x</i>') + '</th>' + f.xs.map(x => '<td>' + E.M(mn(x)) + '</td>').join('') + '</tr>' +
    '<tr><th scope="row">' + E.M('<i>y</i>') + '</th>' + ys.map(y => '<td>' + (y == null ? '<b class="gap" aria-label="missing">?</b>' : E.M(mn(y))) + '</td>').join('') + '</tr></table>';
  return { html: '<div class="qfig tabs">' + f.titles.map((t, i) => one(t, f.rows[i])).join('') + '</div>' };
}
const FIG = { plane, tables };
function figModel(f) { return FIG[f.kind](f); }
function figHtml(f) { return f ? figModel(f).html : ''; }
const api = { figModel, figHtml, clip, plane, tables };
if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.Fig = api;
})(this);
