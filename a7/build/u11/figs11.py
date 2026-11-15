# -*- coding: utf-8 -*-
"""Unit 11 figures — a coordinate plane with one or two lines drawn from their equations, and a table of values
(figkit `shapes`).

Every line is drawn from its own m and b, clipped to the plane, so a crossing printed in a question is where the
drawing crosses: `plane` refuses a marked point that is not on the lines it is said to be on, and a solution the
words give is checked against the two equations before anything is drawn (ruling 38: a figure's labels are true;
ruling 44: the words and the picture agree). The first line is solid blue and the second dashed orange, so the two
can be told apart on a slide and on a black-and-white print; each carries its equation where it leaves the plane.
Unit 11 is taught before slope has a name (Unit 10), so nothing here prints "slope" or "y-intercept"."""
from fractions import Fraction as Fr

INK = "#1A1A1A"
GRID = "#C8C8C8"          # the pale unit grid: not ink to the struck-label check
BLUE = "#1E5AA8"
ORANGE = "#C05A00"


def _t(x, y, s, **k):
    return dict(t="text", xy=(x, y), s=s, **k)


def slide(spec, inches=3.4, pt=18, reserve=0.45):
    """The same figure sized for a slide: wider, with labels that read from the back row."""
    out = dict(spec)
    out["pt"] = pt
    out["reserve"] = reserve
    out["in"] = inches
    return out


def _minus(v):
    v = Fr(v).limit_denominator(1000)
    if v.denominator == 1:
        return str(v.numerator).replace("-", "−")
    return str(float(v)).replace("-", "−")


def eq(m, b, y="y", x="x"):
    """The equation as it is printed: y = 2x + 1, y = −x + 4, y = ½x − 2, y = 0.5x + 1, y = 3x, y = 4."""
    m = Fr(m).limit_denominator(1000) if not isinstance(m, str) else m
    b = Fr(b).limit_denominator(1000)
    if isinstance(m, str):                  # a multiplier written the way the item wants it ("0.5", "½")
        mx = f"{m}{x}"
    elif m == 0:
        mx = ""
    elif m == 1:
        mx = x
    elif m == -1:
        mx = f"−{x}"
    elif m.denominator == 1:
        mx = f"{_minus(m)}{x}"
    else:
        frac = {(1, 2): "½", (1, 3): "⅓", (2, 3): "⅔", (1, 4): "¼", (3, 4): "¾"}.get((abs(m.numerator), m.denominator))
        mx = (("−" if m < 0 else "") + frac + x) if frac else f"{_minus(float(m))}{x}"
    if not mx:
        return f"{y} = {_minus(b)}"
    if b == 0:
        return f"{y} = {mx}"
    return f"{y} = {mx} {'+' if b > 0 else '−'} {_minus(abs(b))}"


def _clip(m, b, x0, x1, y0, y1):
    """The two points where y = mx + b enters and leaves the plane, left to right; None if it misses it."""
    m, b = Fr(m), Fr(b)
    pts = []
    for x in (Fr(x0), Fr(x1)):
        y = m * x + b
        if y0 <= y <= y1:
            pts.append((x, y))
    if m != 0:
        for y in (Fr(y0), Fr(y1)):
            x = (y - b) / m
            if x0 < x < x1:
                pts.append((x, y))
    pts = sorted(set(pts))
    return (pts[0], pts[-1]) if len(pts) >= 2 else None


def plane(xr, yr, lines=(), points=(), xs=1, ys=1, xname="x", yname="y", step=None, fs=22, pt=9.5, inches=3.0,
          label=True, solution=None):
    """A coordinate plane from xr[0] to xr[1] and yr[0] to yr[1] (in the story's own numbers) with its pale grid, one
    grid line every `xs` across and every `ys` up, the two axes and their numbers.

    `lines` are (m, b) or (m, b, text) or (m, b, text, (x, where)): y = mx + b drawn across the whole plane — the first solid blue, the second
    dashed orange — with `text` (default: its equation) printed where the line leaves the plane on the right or the
    top; text="" prints nothing. With (x, where) the text is set instead beside the line's point at that x, in
    the corner `where` ('ur', 'dl', 'r', …) — added for 11.07's candles, two falling lines that leave the plane
    only through its bottom edge. `points` are (x, y) or (x, y, name) or (x, y, name, where): a dot, and its name or
    coordinates when given ("" for a bare dot); a `where` ending in "+" or "++" ("u+", "r++") sets the name two or three times as far
    from its dot (added 15 Nov for the keys' crossings). `solution` = (x, y) is checked against EVERY line and refused if it
    is not on all of them — give it whenever the words name a crossing. A point whose name is "on" is checked to lie
    on at least one line. `xname`, `yname` title the axes ("x" and "y" sit at the axes' ends; a longer name is set
    under and beside the plane)."""
    x0, x1 = xr
    y0, y1 = yr
    L = []
    at = []                                     # a line's own label place, (x, where), or None
    for ln in lines:
        m, b = Fr(ln[0]).limit_denominator(1000), Fr(ln[1]).limit_denominator(1000)
        text = ln[2] if len(ln) > 2 else eq(m, b)
        L.append((m, b, text))
        at.append(ln[3] if len(ln) > 3 else None)
    if solution is not None:
        sx, sy = Fr(solution[0]).limit_denominator(1000), Fr(solution[1]).limit_denominator(1000)
        for (m, b, _) in L:
            if m * sx + b != sy:
                raise ValueError(f"plane: ({solution[0]}, {solution[1]}) is not on {eq(m, b)}")
        if not (x0 <= sx <= x1 and y0 <= sy <= y1):
            raise ValueError(f"plane: the crossing ({solution[0]}, {solution[1]}) is off the plane {xr} × {yr}")
    if len(L) == 2 and solution is None and L[0][0] != L[1][0]:
        cx = (L[1][1] - L[0][1]) / (L[0][0] - L[1][0])
        cy = L[0][0] * cx + L[0][1]
        if not (x0 <= cx <= x1 and y0 <= cy <= y1):
            raise ValueError(f"plane: the two lines cross at ({float(cx)}, {float(cy)}), off the plane {xr} × {yr}")

    def X(x):
        return float(Fr(x) / xs)

    def Y(y):
        return float(Fr(y) / ys)

    sh = []
    nx0, nx1 = int(Fr(x0) / xs), int(Fr(x1) / xs)
    ny0, ny1 = int(Fr(y0) / ys), int(Fr(y1) / ys)
    if nx0 * xs != x0 or nx1 * xs != x1 or ny0 * ys != y0 or ny1 * ys != y1:
        raise ValueError("plane: the plane's edges must be whole grid lines")
    for i in range(nx0, nx1 + 1):
        sh.append(dict(t="seg", a=(i, ny0), b=(i, ny1), color=GRID))
    for j in range(ny0, ny1 + 1):
        sh.append(dict(t="seg", a=(nx0, j), b=(nx1, j), color=GRID))
    short = len(xname) <= 1 and len(yname) <= 1
    if ny0 <= 0 <= ny1:
        sh.append(dict(t="seg", a=(nx0, 0), b=(nx1, 0)))
        if short:
            sh.append(_t(nx1, 0, xname, ha="left", va="center", off=(0.35, 0)))
    if nx0 <= 0 <= nx1:
        sh.append(dict(t="seg", a=(0, ny0), b=(0, ny1)))
        if short:
            sh.append(_t(0, ny1, yname, ha="center", va="bottom", off=(0, 0.3)))
    if not short:
        sh.append(_t((nx0 + nx1) / 2, ny0, xname, ha="center", va="top", off=(0, -1.75)))
        sh.append(_t(nx0, ny1, yname, ha="left", va="bottom", off=(-1.2, 0.45)))
    if step is None:
        cell = inches * 72.0 / max(nx1 - nx0 + 1.4, 1)
        widest = max(len(_minus(i * xs)) for i in range(nx0, nx1 + 1))
        step = 1 if cell >= (0.62 * widest + 0.9) * pt else 2
    for i in range(nx0, nx1 + 1):
        if i % step == 0:
            sh.append(_t(i, ny0, _minus(i * xs), ha="center", va="top", off=(0, -0.35)))
    for j in range(ny0, ny1 + 1):
        if j % step == 0:
            sh.append(_t(nx0, j, _minus(j * ys), ha="right", va="center", off=(-0.35, 0)))
    ends = []
    for k, (m, b, text) in enumerate(L):
        c = _clip(m, b, x0, x1, y0, y1)
        if c is None:
            raise ValueError(f"plane: {eq(m, b)} does not cross the plane {xr} × {yr}")
        (ax, ay), (bx, by) = c
        colour = BLUE if k == 0 else ORANGE
        sh.append(dict(t="seg", a=(X(ax), Y(ay)), b=(X(bx), Y(by)), color=colour, dash=(k == 1)))
        if label and text and at[k] is not None:
            # a label set beside the line's own point at x = at[0], in the corner at[1] — for a line that leaves
            # the plane only through the bottom or the left edge (a falling line in a story that starts at x = 0)
            lx, where = at[k]
            lx = Fr(lx).limit_denominator(1000)
            ly = m * lx + b
            if not (x0 <= lx <= x1 and y0 <= ly <= y1):
                raise ValueError(f"plane: the label place x = {lx} of {eq(m, b)} is off the plane")
            ha = "left" if "r" in where else "right" if "l" in where else "center"
            va = "bottom" if "u" in where else "top" if "d" in where else "center"
            sh.append(_t(X(lx), Y(ly), text, ha=ha, va=va, color=colour,
                         off=(0.5 if ha == "left" else -0.5 if ha == "right" else 0,
                              0.45 if va == "bottom" else -0.45 if va == "top" else 0)))
        elif label and text:
            # the equation sits where the line leaves the plane on the right edge or the top edge — the bottom and
            # the left edge belong to the axes' numbers. Right edge: beside it. Top edge: above it.
            cands = [(px, py) for (px, py) in ((ax, ay), (bx, by)) if px == x1 or py == y1]
            if not cands:
                cands = [(bx, by)]
            px, py = max(cands, key=lambda p: (p[0] == x1, p[1]))
            ends.append(["r" if px == x1 else "t", X(px), Y(py), text, colour])
    if len(ends) == 2 and ends[0][0] == ends[1][0]:
        # two equations on one edge: on the top edge the left one ends at its line and the right one starts at
        # its line; on the right edge the upper one sits above its line's end and the lower one below
        axis = 1 if ends[0][0] == "t" else 2
        if abs(ends[0][axis] - ends[1][axis]) < 0.9:
            raise ValueError("plane: the two lines leave the plane at nearly the same place, so their equations "
                             "cannot both be read — change the window, or give one line text=\"\"")
        lo, hi = sorted(ends, key=lambda e: e[axis])
        lo.append("lo"); hi.append("hi")
    for e in ends:
        side, ex, ey, text, colour = e[:5]
        split = e[5] if len(e) > 5 else None
        if side == "r":
            va = {"lo": "top", "hi": "bottom", None: "center"}[split]
            sh.append(_t(ex, ey, text, ha="left", va=va, off=(0.4, 0), color=colour))
        else:
            ha = {"lo": "right", "hi": "left", None: "center"}[split]
            # an equation that would land on the y at the top of the y-axis is set one line higher
            up = 1.6 if (short and nx0 <= 0 <= nx1 and abs(ex) < 4.5) else 0.35
            sh.append(_t(ex, ey, text, ha=ha, va="bottom", off=(0, up), color=colour))
    for item in points:
        px, py = item[0], item[1]
        name = item[2] if len(item) > 2 else None
        where = item[3] if len(item) > 3 else _clear(px, py, L, xs, ys)
        if not (x0 <= px <= x1 and y0 <= py <= y1):
            raise ValueError(f"plane: point ({px}, {py}) is off the plane")
        sh.append(dict(t="circle", c=(X(px), Y(py)), r=0.13, fill=INK))
        if name is None:
            name = f"({_minus(px)}, {_minus(py)})"
        if name:
            ha = "left" if "r" in where else "right" if "l" in where else "center"
            va = "bottom" if "u" in where else "top" if "d" in where else "center"
            k = 1 + where.count("+")                 # "u+", "d++", …: the name set two or three times as far off (a
            #                                          key's crossing between two lines that meet at a narrow angle)
            sh.append(_t(X(px), Y(py), name, ha=ha, va=va,
                         off=(k * (0.5 if ha == "left" else -0.5 if ha == "right" else 0),
                              k * (0.45 if va == "bottom" else -0.45 if va == "top" else 0))))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def _clear(px, py, L, xs, ys):
    """The corner beside a point ('ur', 'ul', 'dl', 'dr') farthest in angle from every line through it."""
    import math
    dirs = []
    for (m, b, _) in L:
        if m * Fr(px).limit_denominator(1000) + b == Fr(py).limit_denominator(1000):
            d = math.degrees(math.atan2(float(m) * xs / ys, 1.0)) % 360
            dirs += [d, (d + 180) % 360]
    best, where = -1, "ur"
    for w, ang in (("ur", 45), ("ul", 135), ("dl", 225), ("dr", 315), ("r", 0), ("l", 180), ("u", 90), ("d", 270)):
        gap = min((min(abs(ang - d), 360 - abs(ang - d)) for d in dirs), default=180)
        if gap > best + 1e-9:
            best, where = gap, w
    return where


def table(rows, head=("x", "y"), cw=1.25, rh=1.0, fs=22, pt=9.5, inches=None, titles=None):
    """One or more tables of values side by side, each a row of x's over a row of y's. `rows` is a list of tables;
    a table is (xs, ys) with "" or "?" for a cell the student fills. `titles` (one per table) print above — an
    equation, usually. Numbers are printed as given."""
    sh = []
    left = 0.0
    for k, (xv, yv) in enumerate(rows):
        if len(xv) != len(yv):
            raise ValueError("table: a table's two rows must be the same length")
        n = len(xv) + 1
        for r in range(3):
            sh.append(dict(t="seg", a=(left, -r * rh), b=(left + n * cw, -r * rh)))
        for c in range(n + 1):
            sh.append(dict(t="seg", a=(left + c * cw, 0), b=(left + c * cw, -2 * rh)))
        for r, (h, vals) in enumerate(((head[0], xv), (head[1], yv))):
            sh.append(_t(left + cw / 2, -(r + 0.5) * rh, h))
            for c, v in enumerate(vals):
                s = v if isinstance(v, str) else _minus(v)
                if s:
                    sh.append(_t(left + (c + 1.5) * cw, -(r + 0.5) * rh, s))
        if titles and titles[k]:
            sh.append(_t(left + n * cw / 2, 0, titles[k], va="bottom", off=(0, 0.4)))
        left += n * cw + 1.2
    if inches is None:
        inches = round(min(6.0, 0.42 * (left - 1.2)), 2)
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def _extent(shapes):
    """The box (x0, x1, y0, y1) of a figure's drawn anchors: segments' ends, circles, and the points labels hang from."""
    xs, ys = [], []
    for s in shapes:
        if s["t"] == "seg":
            xs += [s["a"][0], s["b"][0]]; ys += [s["a"][1], s["b"][1]]
        elif s["t"] == "circle":
            xs += [s["c"][0] - s["r"], s["c"][0] + s["r"]]; ys += [s["c"][1] - s["r"], s["c"][1] + s["r"]]
        elif s["t"] == "text":
            xs.append(s["xy"][0]); ys.append(s["xy"][1])
    return min(xs), max(xs), min(ys), max(ys)


def row(specs, gap=3.0, titles=None, captions=None, fs=22, pt=9.5, inches=6.0):
    """Two or more figures of this file (each a `plane` or a `table`, already drawn and checked by its own helper —
    a `plane` still refuses a solution that is not on its lines) set side by side as ONE picture, left to right,
    `gap` grid units apart, centred on one another top to bottom. `titles` (one per figure, or None) print above
    each: a string, or a list of lines, each a string or (text, colour) — the equations of a plane whose own line
    labels were turned off (text=""), set in the colour of the line they name. `captions` (one per figure, or
    None; a string or a list of lines) print under each, below its numbers. Added for 11.05 Notes I (a table beside its line) and Notes III
    (three systems side by side: cross once, parallel, the same line)."""
    boxes = [_extent(s["shapes"]) for s in specs]
    hmax = max(b[3] - b[2] for b in boxes)
    sh, left = [], 0.0
    for k, (spec, (x0, x1, y0, y1)) in enumerate(zip(specs, boxes)):
        dx = left - x0
        dy = -(y0 + y1) / 2.0                 # every figure centred on y = 0
        for s in spec["shapes"]:
            s = dict(s)
            if s["t"] == "seg":
                s["a"] = (s["a"][0] + dx, s["a"][1] + dy); s["b"] = (s["b"][0] + dx, s["b"][1] + dy)
            elif s["t"] == "circle":
                s["c"] = (s["c"][0] + dx, s["c"][1] + dy)
            elif s["t"] == "text":
                s["xy"] = (s["xy"][0] + dx, s["xy"][1] + dy)
            sh.append(s)
        mid = left + (x1 - x0) / 2.0
        top, bottom = (y1 - y0) / 2.0, -(y1 - y0) / 2.0
        if titles and titles[k]:
            lines = [titles[k]] if isinstance(titles[k], (str, tuple)) else list(titles[k])
            for j, ln in enumerate(reversed(lines)):          # the last line sits lowest, just over the figure
                text, colour = (ln, INK) if isinstance(ln, str) else ln
                sh.append(_t(mid, top, text, va="bottom", off=(0, 1.7 + 1.25 * j), color=colour))
        if captions and captions[k]:
            lines = [captions[k]] if isinstance(captions[k], str) else list(captions[k])
            for j, text in enumerate(lines):
                sh.append(_t(mid, bottom, text, va="top", off=(0, -1.9 - 1.25 * j)))
        left += (x1 - x0) + gap
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def match_grid(rows, cols, rw=7.5, cw=3.6, rh=1.15, fs=22, pt=9.5, inches=6.0):
    """A matching grid in FAST's shape: one row per item (its words at the left), one column per choice (its name
    on top), an empty box in every cell for a student's mark. Added for the Unit Review (fast 9)."""
    sh = []
    n, m = len(rows), len(cols)
    W = rw + m * cw
    for r in range(n + 2):
        sh.append(dict(t="seg", a=(0, -r * rh), b=(W, -r * rh)))
    for c in range(m + 2):
        x = 0 if c == 0 else rw + (c - 1) * cw
        sh.append(dict(t="seg", a=(x, 0), b=(x, -(n + 1) * rh)))
    for c, name in enumerate(cols):
        sh.append(_t(rw + (c + 0.5) * cw, -0.5 * rh, name))
    for r, name in enumerate(rows):
        yc = -(r + 1.5) * rh
        sh.append(_t(0.4, yc, name, ha="left"))
        for c in range(m):
            xc = rw + (c + 0.5) * cw
            q = 0.28
            for (a, b) in (((xc - q, yc - q), (xc + q, yc - q)), ((xc + q, yc - q), (xc + q, yc + q)),
                           ((xc + q, yc + q), (xc - q, yc + q)), ((xc - q, yc + q), (xc - q, yc - q))):
                sh.append(dict(t="seg", a=a, b=b))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)
