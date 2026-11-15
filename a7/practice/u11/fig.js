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

/* ------------------------------------------------------------------ the help's pictures (help.js, 15 Nov 2026)
   Drawn as the kit's explain.js draws (svg.xsvg on a 280-unit canvas, labels .xt at 16.5 px, the three signal colors with their
   own line styles: x1 teal solid, x2 orange dashed, x3 violet dotted), so on a 390 px phone every label reads at 12.5 px or more
   in light and in dark (kit check/help_page.js). The axes' small numbers are .xtk (13 px), exempt from that check as ticks are,
   and still readable. Nothing here is a question's own figure: those stay plane() and tables(), which the checks read back. */
const r1 = v => Math.round(v * 10) / 10;
const TX = (x, y, s, cls, anchor, extra) => '<text x="' + r1(x) + '" y="' + r1(y) + '" class="' + (cls || 'xt') + '"' + (anchor ? ' text-anchor="' + anchor + '"' : '') + (extra || '') + '>' + E.esc(s) + '</text>';
const open = (w, h, label, big) => '<svg class="xsvg' + (big ? ' u11h' : '') + '" viewBox="0 0 ' + r1(w) + ' ' + r1(h) + '" role="img" aria-label="' + E.esc(label) + '">';
const cw = s => String(s).length * 9.6 + 14;                         /* a chip's width for its text */
const cwb = s => String(s).length * 11.4 + 16;                       /* a label's width in the larger help type (.u11h) */
/* a coordinate plane for the help: the grid, the axes and their numbers, lines clipped to the window (the first solid, the
   second dashed, as on the question's own graph), and on top what the help points at — a point (marked in color 3 with a
   dotted path to each axis and its coordinates), pairs of points joined by a dashed bracket (color 2: "always 3 apart"), dots */
function helpPlane(o) {
  const w = o.w, ys = w.ys || 1, nx = w.x1 - w.x0, ny = (w.y1 - w.y0) / ys, story = !!o.story;
  const L = story ? 42 : 30, Rm = 16, top = 16, W = 280, k0 = (W - L - Rm) / nx, k = Math.min(k0, 300 / ny), pw = nx * k, ph = ny * k, ox = L + (W - L - Rm - pw) / 2;
  const PX = x => ox + (x - w.x0) * k, PY = y => top + (w.y1 - y) / ys * k;
  let out = '', d = '';
  for (let i = 0; i <= nx; i++) d += 'M' + r1(PX(w.x0 + i)) + ' ' + top + 'V' + r1(top + ph);
  for (let j = 0; j <= ny; j++) d += 'M' + r1(ox) + ' ' + r1(top + j * k) + 'H' + r1(ox + pw);
  out += '<path class="xgrid" d="' + d + '"/>';
  if (w.y0 <= 0 && 0 <= w.y1) out += '<line class="xaxis" x1="' + r1(ox) + '" y1="' + r1(PY(0)) + '" x2="' + r1(ox + pw) + '" y2="' + r1(PY(0)) + '"/>';
  if (w.x0 <= 0 && 0 <= w.x1) out += '<line class="xaxis" x1="' + r1(PX(0)) + '" y1="' + top + '" x2="' + r1(PX(0)) + '" y2="' + r1(top + ph) + '"/>';
  const sx = k >= 24 ? 1 : 2, sy = k >= 18 ? 1 : 2;
  for (let i = 0; i <= nx; i++) { const x = w.x0 + i; if (x % sx === 0) out += TX(PX(x), top + ph + 13, mn(x), 'xtk tick', 'middle'); }
  for (let j = 0; j <= ny; j++) { const y = w.y0 + j * ys; if (Math.round(y / ys) % sy === 0) out += TX(ox - 6, PY(y), mn(y), 'xtk tick', 'end'); }
  (o.lines || []).forEach((l, i) => { const c = clip(l, w); if (!c) return; const a = c[0].map(qnum), b = c[1].map(qnum);
    out += '<line class="' + (i ? 'ln2' : 'ln1') + '" x1="' + r1(PX(a[0])) + '" y1="' + r1(PY(a[1])) + '" x2="' + r1(PX(b[0])) + '" y2="' + r1(PY(b[1])) + '"/>'; });
  (o.gaps || []).forEach(g => { const x = PX(qnum(g.x)), y1 = PY(qnum(g.y1)), y2 = PY(qnum(g.y2));
    out += '<line class="xgap" x1="' + r1(x) + '" y1="' + r1(y1) + '" x2="' + r1(x) + '" y2="' + r1(y2) + '"/>' + '<path class="xgaph" d="M' + r1(x - 5) + ' ' + r1(y1) + 'H' + r1(x + 5) + 'M' + r1(x - 5) + ' ' + r1(y2) + 'H' + r1(x + 5) + '"/>' +
      (g.t ? TX(x + 9, (y1 + y2) / 2, g.t, 'xt xf2', 'start') : ''); });
  (o.dots || []).forEach(p => { out += '<circle class="xpt" cx="' + r1(PX(qnum(p.x))) + '" cy="' + r1(PY(qnum(p.y))) + '" r="4.5"/>'; });
  if (o.mark) { const mx = PX(qnum(o.mark.x)), my = PY(qnum(o.mark.y)), x0 = PX(Math.max(w.x0, Math.min(w.x1, 0))), y0 = PY(Math.max(w.y0, Math.min(w.y1, 0)));
    if (o.guides) out += '<path class="xguide" d="M' + r1(mx) + ' ' + r1(my) + 'V' + r1(y0) + 'M' + r1(mx) + ' ' + r1(my) + 'H' + r1(x0) + '"/>';
    out += '<circle class="xmark" cx="' + r1(mx) + '" cy="' + r1(my) + '" r="6"/>';
    if (o.mark.t) { const right = mx < ox + pw * 0.6, up = my > top + 26;
      out += '<rect class="xlabbg" x="' + r1(right ? mx + 9 : mx - 9 - cwb(o.mark.t) + 6) + '" y="' + r1((up ? my - 22 : my + 22) - 13) + '" width="' + r1(cwb(o.mark.t) - 6) + '" height="26" rx="5"/>' +
        TX(right ? mx + 12 : mx - 12, up ? my - 22 : my + 22, o.mark.t, 'xt xf3', right ? 'start' : 'end'); } }
  if (!story && w.y0 <= 0 && 0 <= w.y1) out += TX(ox + pw + 4, PY(0) - 10, 'x', 'xt xsm', 'start');
  if (!story && w.x0 <= 0 && 0 <= w.x1) out += TX(PX(0) + 7, top + 2, 'y', 'xt xsm', 'start');
  let h = top + ph + 26;
  if (story && o.names) { out += TX(ox + pw / 2, h + 6, o.names[0], 'xt xsm', 'middle'); h += 22; }
  return open(W, h, o.label, true) + out + '</svg>';
}
/* the crossing, zoomed: one grid square cut into tenths, its half lines dashed, the two lines through it, the crossing marked and
   read to the nearest tenth on each edge */
function zoomPic(o) {
  const c = o.c, X0 = Math.floor(qnum(c.x)), Y0 = Math.floor(qnum(c.y)), S = 200, L = 54, top = 14, W = 280, k = S;
  const PX = x => L + (x - X0) * k, PY = y => top + (Y0 + 1 - y) * k, w = { x0: X0, x1: X0 + 1, y0: Y0, y1: Y0 + 1 };
  let out = '', d = '', d2 = '';
  for (let i = 1; i < 10; i++) { if (i === 5) continue; d += 'M' + r1(L + i * k / 10) + ' ' + top + 'V' + (top + S) + 'M' + L + ' ' + r1(top + i * k / 10) + 'H' + (L + S); }
  d2 = 'M' + (L + S / 2) + ' ' + top + 'V' + (top + S) + 'M' + L + ' ' + (top + S / 2) + 'H' + (L + S);
  out += '<path class="xtenth" d="' + d + '"/><path class="xhalf" d="' + d2 + '"/><rect class="xsq" x="' + L + '" y="' + top + '" width="' + S + '" height="' + S + '"/>';
  [o.l1, o.l2].forEach((l, i) => { const cl = clip(l, w); if (!cl) return; const a = cl[0].map(qnum), b = cl[1].map(qnum);
    out += '<line class="' + (i ? 'ln2' : 'ln1') + '" x1="' + r1(PX(a[0])) + '" y1="' + r1(PY(a[1])) + '" x2="' + r1(PX(b[0])) + '" y2="' + r1(PY(b[1])) + '"/>'; });
  const mx = PX(qnum(c.x)), my = PY(qnum(c.y));
  out += '<path class="xguide" d="M' + r1(mx) + ' ' + r1(my) + 'V' + (top + S) + 'M' + r1(mx) + ' ' + r1(my) + 'H' + L + '"/><circle class="xmark" cx="' + r1(mx) + '" cy="' + r1(my) + '" r="6"/>';
  [X0, X0 + 0.5, X0 + 1].forEach(v => { out += TX(PX(v), top + S + 14, mn(v), 'xtk tick', 'middle'); });
  [Y0, Y0 + 0.5, Y0 + 1].forEach(v => { out += TX(L - 6, PY(v), mn(v), 'xtk tick', 'end'); });
  const yw = cwb(o.ay) - 6, yy = my < top + 30 ? my + 20 : my - 20;      /* the y reading inside the square, just above (or below) its dotted path */
  out += TX(mx, top + S + 34, o.ax, 'xt xf3', 'middle') + '<rect class="xlabbg" x="' + (L + 3) + '" y="' + r1(yy - 12) + '" width="' + r1(yw) + '" height="24" rx="5"/>' + TX(L + 6, yy, o.ay, 'xt xf3', 'start');
  return open(W, top + S + 50, o.label, true) + out + '</svg>';
}
/* tables of values as the lessons draw them: an x row and a y row per equation, the equation above its table; one column may be
   boxed (color 3, dotted) and a missing value shown as "?" */
function tablePic(o) {
  const W = 280, head = 40, n = o.xs.length, cwid = (W - head - 2) / n, rh = 30;
  let out = '', y = 4;
  o.rows.forEach(r => {
    out += TX(2, y + 11, r.name, 'xt xsm', 'start'); y += 24;
    const y0 = y;
    if (o.hi != null && o.hi >= 0) out += '<rect class="xhi" x="' + r1(head + o.hi * cwid + 1) + '" y="' + r1(y0 - 2) + '" width="' + r1(cwid - 2) + '" height="' + r1(2 * rh + 4) + '" rx="4"/>';
    [['x', o.xs], ['y', r.ys]].forEach(([lab, vals], j) => { const yy = y0 + j * rh;
      out += '<rect class="xcell xhead" x="1" y="' + yy + '" width="' + (head - 1) + '" height="' + rh + '"/>' + TX(head / 2, yy + rh / 2, lab, 'xt', 'middle');
      vals.forEach((v, i) => { const xx = head + i * cwid;
        out += '<rect class="xcell" x="' + r1(xx) + '" y="' + yy + '" width="' + r1(cwid) + '" height="' + rh + '"/>' + TX(xx + cwid / 2, yy + rh / 2, v == null ? '?' : mn(v), 'xt' + (j && r.hl && i === o.hi ? ' xf3' : ''), 'middle'); }); });
    y = y0 + 2 * rh + 12; });
  return open(W, y, o.label, true) + out + '</svg>';
}
/* the Distributive Property as the lessons draw it by hand: an arrow from the number in front to EACH term inside (11.01 Notes
   III: "Draw two arrows by hand from the −3, one to the x and one to the −2"), and, when given, each product under its term */
function arrowsPic(groups, label) {
  const W = 280; let out = '', y = 0;
  groups.forEach(g => {
    const fw = String(g.f).length * 9.6 + 6, ws = g.t.map(cw), total = fw + 10 + ws[0] + 8 + ws[1] + 10;
    let x = (W - total) / 2; const top = y + 44, fx = x + fw / 2;
    out += TX(x + fw / 2, top + 17, g.f, 'xt xbig2', 'middle'); x += fw;
    out += TX(x + 5, top + 17, '(', 'xt xbig2', 'middle'); x += 10;
    const cx = [];
    g.t.forEach((t, i) => { out += '<rect x="' + r1(x) + '" y="' + top + '" width="' + r1(ws[i]) + '" height="34" rx="7" class="xchip xs' + (i + 1) + (i ? ' xadd' : '') + '"/>' + TX(x + ws[i] / 2, top + 17, t, 'xt', 'middle'); cx.push(x + ws[i] / 2); x += ws[i] + 8; });
    out += TX(x + 1, top + 17, ')', 'xt xbig2', 'middle');
    cx.forEach((c, i) => { const h = 18 + i * 12, y1 = top - 4, y0 = top - 2;
      out += '<path class="xarr xarr' + (i + 1) + '" d="M' + r1(fx) + ' ' + y0 + ' Q' + r1((fx + c) / 2) + ' ' + (y1 - h * 2) + ' ' + r1(c) + ' ' + (y1 - 2) + '"/>' +
        '<path class="xhead' + (i + 1) + '" d="M' + r1(c - 5) + ' ' + (y1 - 9) + ' L' + r1(c) + ' ' + (y1 - 1) + ' L' + r1(c + 5) + ' ' + (y1 - 9) + ' Z"/>'; });
    y = top + 34;
    if (g.p) { g.p.forEach((p, i) => { out += TX(cx[i], y + 18, p, 'xt xf' + (i + 1), 'middle'); }); y += 30; }
    y += 8; });
  return open(W, y, label) + out + '</svg>';
}
/* the three ways two lines can sit (11.05 Notes III, "three pictures, three counts"): cross once, parallel, the same line */
function threePic() {
  const W = 280, pw = 84, gap = (W - 3 * pw) / 2, H = 84; let out = '';
  const panel = (i, segs, words) => { const x0 = i * (pw + gap);
    out += '<rect class="xsq" x="' + r1(x0) + '" y="2" width="' + pw + '" height="' + H + '" rx="6"/>';
    segs.forEach(([a, b, c, d, cls]) => { out += '<line class="' + cls + '" x1="' + r1(x0 + a) + '" y1="' + b + '" x2="' + r1(x0 + c) + '" y2="' + d + '"/>'; });
    words.forEach((t, j) => { out += TX(x0 + pw / 2, H + 20 + j * 19, t, 'xt xsm', 'middle'); }); };
  panel(0, [[8, 76, 76, 12, 'ln1'], [8, 18, 76, 70, 'ln2']], ['cross', 'once']);
  out += '<circle class="xmark" cx="' + r1(42) + '" cy="44" r="5"/>';
  panel(1, [[8, 60, 76, 20, 'ln1'], [8, 80, 76, 40, 'ln2']], ['never', 'meet']);
  panel(2, [[8, 74, 76, 16, 'ln1'], [8, 74, 76, 16, 'ln2']], ['one', 'line']);
  return open(W, H + 46, 'Three ways two lines can sit: crossing once, parallel and never meeting, or one line drawn for both equations.') + out + '</svg>';
}
const api = { figModel, figHtml, clip, plane, tables, helpPlane, zoomPic, tablePic, arrowsPic, threePic };
if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.Fig = api;
})(this);
