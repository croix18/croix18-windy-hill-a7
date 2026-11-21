# -*- coding: utf-8 -*-
"""Unit 7 figures — proportional relationships (figkit `shapes`), built from Unit 11's figs11 and drawn its way.

A first-quadrant plane with named axes and its own scale on each (`plane`, `xs=`, `ys=`), holding lines through
the origin given by their constant (`prop(p)`), plotted points with or without a line, a line that is NOT
proportional (`(m, b)` with b != 0, the contrast), a curve (`curves=`, `square(...)`), and two to four lines on one
grid, each lettered or named; the four-quadrant plane for y = px with a negative constant is the same `plane` with
negative ranges. `table` is a ratio table with named rows and a ▢ where a value is asked; `row` sets figures side
by side (the three notes pictures); `choices4` is the row of four lettered graphs for a choice board; `pair` is
the empty grid a student draws on and the same grid with the answer drawn, for `fig` and `fig_key`.

Every line is drawn from its own m and b, clipped to the plane, so a point printed in a question is where the
drawing is: `plane` refuses a point named "on" that is on no line, and a `solution` that is not on every line
(ruling 38: a figure's labels are true; ruling 44: the words and the picture agree). Lines are, in order, solid
blue, dashed orange, solid green, dashed purple. "Slope" and "y-intercept" are on no label (decision 1)."""
from fractions import Fraction as Fr

INK = "#1A1A1A"
GRID = "#C8C8C8"          # the pale unit grid: not ink to the struck-label check
BLUE = "#1E5AA8"
ORANGE = "#C05A00"
GREEN = "#2E7D32"
PURPLE = "#6A3D9A"
STYLES = ((BLUE, False), (ORANGE, True), (GREEN, False), (PURPLE, True))   # line k: (colour, dashed)
BLANK = "▢"               # a table cell or a point's coordinate the student fills: drawn as an empty box


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
    d = v.denominator
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    if d == 1:                               # a terminating decimal: 2.5, 0.4, 1.75
        return str(float(v)).replace("-", "−")
    return f"{v.numerator}/{v.denominator}".replace("-", "−")     # never a rounded decimal: 1/3, not 0.333


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
        if frac:
            mx = ("−" if m < 0 else "") + frac + x
        elif "/" in _minus(m):              # y = (2/7)x — a fraction that is not a terminating decimal
            mx = ("−" if m < 0 else "") + f"({_minus(abs(m))}){x}"
        else:
            mx = f"{_minus(m)}{x}"
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


def prop(p, text=None, at=None):
    """A line through the origin, y = px, given by its constant: (p, 0), (p, 0, text) or (p, 0, text, at) for
    `plane(lines=...)`. text=None prints its equation; "A" or "Pump A" names it; "" prints nothing."""
    out = (p, 0)
    if text is not None or at is not None:
        out += (text if text is not None else eq(p, 0),)
    if at is not None:
        out += (at,)
    return out


def square(a, x1, x0=0, n=24):
    """The points of the curve y = a·x² from x0 to x1, for `plane(curves=[...])` — the notes' curve through the
    origin (7.04 Notes II), straight in no stretch of it."""
    return [(x0 + (x1 - x0) * Fr(i, n), a * (x0 + (x1 - x0) * Fr(i, n)) ** 2) for i in range(n + 1)]


def plane(xr, yr, lines=(), points=(), xs=1, ys=1, xname="x", yname="y", step=None, fs=22, pt=9.5, inches=3.0,
          label=True, solution=None, curves=(), letters=None, xstep=None, ystep=None, aspect=1):
    """A coordinate plane from xr[0] to xr[1] and yr[0] to yr[1] (in the story's own numbers) with its pale grid, one
    grid line every `xs` across and every `ys` up (1, 2, 4, 5, 10, 20 … — each axis its own), the two axes and their
    numbers. xr = (0, …), yr = (0, …) is the first quadrant; negative ranges give the four-quadrant plane.

    `lines` (at most four) are (m, b) or (m, b, text) or (m, b, text, (x, where)) — `prop(p, text)` writes the first
    for y = px: y = mx + b drawn across the whole plane, in order solid blue, dashed orange, solid green, dashed
    purple, with `text` (default: its equation, in `letters` = (x-letter, y-letter) when given, e.g. ("p", "c") for
    c = 2.5p) printed where the line leaves the plane on the right or the top; text="" prints nothing. With
    (x, where) the text is set instead beside the line's point at that x, in the corner `where` ('ur', 'dl', 'r', …)
    — for a falling line, or labels that would crowd one edge. `points` are (x, y) or (x, y, name) or
    (x, y, name, where): a dot, and its name or its coordinates when name is None ("" for a bare dot); a `where`
    ending in "+" or "++" sets the name two or three times as far from its dot. A point whose name is "on" (printed as
    its coordinates) must lie on at least one line. `solution` = (x, y) is checked against EVERY line. `curves` are
    lists of (x, y) in the story's numbers (`square(a, x1)`), drawn after the lines in the next style, every point on
    the plane. `xname`, `yname` title the axes ("x" and "y" sit at the axes' ends; a longer name — "pounds", "cost
    in dollars" — is set under the plane and over its top-left corner). `xstep`/`ystep` (default `step`, default
    by room) number every k-th grid line. `aspect` is a grid cell's height against its width (default 1, square
    cells, as every call before 21 Nov 2026 drew them); below 1 the cells are wider than tall — added for 7.01
    board 6, four graphs on one row that must each be 2 in wide in a row 2.8 in tall."""
    x0, x1 = xr
    y0, y1 = yr
    L = []
    at = []                                     # a line's own label place, (x, where), or None
    if len(lines) > len(STYLES):
        raise ValueError(f"plane: at most {len(STYLES)} lines on one grid")
    lx_, ly_ = letters if letters else ("x", "y")
    for ln in lines:
        m, b = Fr(ln[0]).limit_denominator(1000), Fr(ln[1]).limit_denominator(1000)
        text = ln[2] if len(ln) > 2 else eq(m, b, y=ly_, x=lx_)
        L.append((m, b, text))
        at.append(ln[3] if len(ln) > 3 else None)
    if solution is not None:
        sx, sy = Fr(solution[0]).limit_denominator(1000), Fr(solution[1]).limit_denominator(1000)
        for (m, b, _) in L:
            if m * sx + b != sy:
                raise ValueError(f"plane: ({solution[0]}, {solution[1]}) is not on {eq(m, b)}")
        if not (x0 <= sx <= x1 and y0 <= sy <= y1):
            raise ValueError(f"plane: the point ({solution[0]}, {solution[1]}) is off the plane {xr} × {yr}")

    def X(x):
        return float(Fr(x).limit_denominator(100000) / Fr(xs))

    def Y(y):
        return float(Fr(y).limit_denominator(100000) / Fr(ys))

    sh = []
    nx0, nx1 = int(Fr(x0) / Fr(xs)), int(Fr(x1) / Fr(xs))
    ny0, ny1 = int(Fr(y0) / Fr(ys)), int(Fr(y1) / Fr(ys))
    if nx0 * Fr(xs) != x0 or nx1 * Fr(xs) != x1 or ny0 * Fr(ys) != y0 or ny1 * Fr(ys) != y1:
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
    yname_at = len(sh) if not short else None
    if not short:
        sh.append(_t((nx0 + nx1) / 2, ny0, xname, ha="center", va="top", off=(0, -1.75)))
        sh.append(_t(nx0, ny1, yname, ha="left", va="bottom", off=(-1.2, 0.45)))
    # how many grid lines to a number: the cell's width (or height) against the widest number at `pt`, the plane
    # being drawn `inches` wide (the numbers' column and the names' room take about 1.4 cells)
    cell = inches * 72.0 / max(nx1 - nx0 + 1.4, 1)
    if xstep is None:
        widest = max(len(_minus(i * xs)) for i in range(nx0, nx1 + 1))
        xstep = step or (1 if cell >= (0.62 * widest + 0.9) * pt else 2 if 2 * cell >= (0.62 * widest + 0.9) * pt else 5)
    if ystep is None:
        ystep = step or (1 if cell >= 1.35 * pt else 2 if 2 * cell >= 1.35 * pt else 5)
    for i in range(nx0, nx1 + 1):
        if i % xstep == 0:
            sh.append(_t(i, ny0, _minus(i * xs), ha="center", va="top", off=(0, -0.35)))
    for j in range(ny0, ny1 + 1):
        if j % ystep == 0:
            sh.append(_t(nx0, j, _minus(j * ys), ha="right", va="center", off=(-0.35, 0)))
    ends = []
    for k, (m, b, text) in enumerate(L):
        c = _clip(m, b, x0, x1, y0, y1)
        if c is None:
            raise ValueError(f"plane: {eq(m, b)} does not cross the plane {xr} × {yr}")
        (ax, ay), (bx, by) = c
        colour, dash = STYLES[k]
        sh.append(dict(t="seg", a=(X(ax), Y(ay)), b=(X(bx), Y(by)), color=colour, dash=dash))
        if label and text and at[k] is not None:
            # a label set beside the line's own point at x = at[0], in the corner at[1]
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
            # the label sits where the line leaves the plane on the right edge or the top edge — the bottom and
            # the left edge belong to the axes' numbers. Right edge: beside it. Top edge: above it.
            cands = [(px, py) for (px, py) in ((ax, ay), (bx, by)) if px == x1 or py == y1]
            if not cands:
                cands = [(bx, by)]
            px, py = max(cands, key=lambda p: (p[0] == x1, p[1]))
            ends.append(["r" if px == x1 else "t", X(px), Y(py), text, colour])
    for side in ("r", "t"):
        mine = sorted((e for e in ends if e[0] == side), key=lambda e: e[2] if side == "r" else e[1])
        axis = 2 if side == "r" else 1
        for lo, hi in zip(mine, mine[1:]):
            if abs(hi[axis] - lo[axis]) < 0.9:
                raise ValueError("plane: two lines leave the plane at nearly the same place, so their labels cannot "
                                 "both be read — change the window, or set one label beside its line with (x, where)")
        if len(mine) == 2:
            # two on one edge: on the top edge the left one ends at its line and the right one starts at it; on the
            # right edge the upper one sits above its line's end and the lower one below
            mine[0].append("lo"); mine[1].append("hi")
    if yname_at is not None and any(e[0] == "t" for e in ends):
        # a line's label on the top edge would read on with the y-axis's name ("meters A"): the name goes up a row
        sh[yname_at + 1] = _t(nx0, ny1, yname, ha="left", va="bottom", off=(-1.2, 1.7))
    for e in ends:
        side, ex, ey, text, colour = e[:5]
        split = e[5] if len(e) > 5 else None
        if side == "r":
            va = {"lo": "top", "hi": "bottom", None: "center"}[split]
            sh.append(_t(ex, ey, text, ha="left", va=va, off=(0.4, 0), color=colour))
        else:
            ha = {"lo": "right", "hi": "left", None: "center"}[split]
            # a label that would land on the y at the top of the y-axis is set one line higher
            up = 1.6 if (short and nx0 <= 0 <= nx1 and abs(ex) < 4.5) else 0.35
            sh.append(_t(ex, ey, text, ha=ha, va="bottom", off=(0, up), color=colour))
    for k, pts in enumerate(curves):
        colour, dash = STYLES[(len(L) + k) % len(STYLES)]
        for (px, py) in pts:
            if not (x0 <= px <= x1 and y0 <= py <= y1):
                raise ValueError(f"plane: the curve's point ({float(px)}, {float(py)}) is off the plane")
        for (pa, pb) in zip(pts, pts[1:]):
            sh.append(dict(t="seg", a=(X(pa[0]), Y(pa[1])), b=(X(pb[0]), Y(pb[1])), color=colour, dash=dash))
    for item in points:
        px, py = item[0], item[1]
        name = item[2] if len(item) > 2 else None
        where = item[3] if len(item) > 3 else _clear(px, py, L, xs, ys, (x0, x1, y0, y1))
        if not (x0 <= px <= x1 and y0 <= py <= y1):
            raise ValueError(f"plane: point ({px}, {py}) is off the plane")
        if name == "on":
            fx, fy = Fr(px).limit_denominator(1000), Fr(py).limit_denominator(1000)
            if not any(m * fx + b == fy for (m, b, _) in L):
                raise ValueError(f"plane: the point ({px}, {py}) is said to be on a line and is on none")
            name = None
        sh.append(dict(t="circle", c=(X(px), Y(py)), r=0.13, fill=INK))
        # the kit draws a circle under every segment, so the pale grid ran across the dot (a white cross in it):
        # chords of ink, drawn after the grid, fill it again
        for i in range(-6, 7):
            h = 0.13 * i / 6.5
            w = (0.13 ** 2 - h * h) ** 0.5
            sh.append(dict(t="seg", a=(X(px) - w, Y(py) + h), b=(X(px) + w, Y(py) + h), color=INK))
            if aspect != 1:
                sh[-1]["_dot"] = Y(py)          # a dot's chord moves with its centre and keeps its round shape
        if name is None:
            name = f"({_minus(px)}, {_minus(py)})"
        if name:
            ha = "left" if "r" in where else "right" if "l" in where else "center"
            va = "bottom" if "u" in where else "top" if "d" in where else "center"
            k = 1 + where.count("+")
            sh.append(_t(X(px), Y(py), name, ha=ha, va=va,
                         off=(k * (0.5 if ha == "left" else -0.5 if ha == "right" else 0),
                              k * (0.45 if va == "bottom" else -0.45 if va == "top" else 0))))
    if aspect != 1:
        # every height in the plane drawn `aspect` times as tall; a dot stays round (its circle and its chords
        # move with its centre), and the labels' offsets are in ems, so they do not change
        k = float(aspect)
        for s in sh:
            if s["t"] == "seg" and "_dot" in s:
                d = s.pop("_dot") * (k - 1)
                s["a"] = (s["a"][0], s["a"][1] + d); s["b"] = (s["b"][0], s["b"][1] + d)
            elif s["t"] == "seg":
                s["a"] = (s["a"][0], s["a"][1] * k); s["b"] = (s["b"][0], s["b"][1] * k)
            elif s["t"] == "circle":
                s["c"] = (s["c"][0], s["c"][1] * k)
            elif s["t"] == "text":
                s["xy"] = (s["xy"][0], s["xy"][1] * k)
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def pair(xr, yr, lines=(), points=(), **kw):
    """The empty grid a student draws on (`fig`) and the same grid with the answer drawn (`fig_key` / `fig_a`): one
    window, one scale, one set of names, so the key is the student's grid. Returns (empty, drawn)."""
    empty = plane(xr, yr, **{k: v for k, v in kw.items() if k != "solution"})
    return empty, plane(xr, yr, lines=lines, points=points, **kw)


def _clear(px, py, L, xs, ys, box=None):
    """The corner beside a point ('ur', 'ul', 'dl', 'dr', …) farthest in angle from every line through it; of the
    corners as far as each other, one that does not reach toward an edge of the plane close by (the y-axis one cell to
    the left of (1, 4) ran through a name set to its left — added for Unit 7)."""
    import math
    dirs = []
    for (m, b, _) in L:
        if m * Fr(px).limit_denominator(1000) + b == Fr(py).limit_denominator(1000):
            d = math.degrees(math.atan2(float(m) * xs / ys, 1.0)) % 360
            dirs += [d, (d + 180) % 360]
    near = ""
    if box:
        x0, x1, y0, y1 = box
        near += "l" if (px - x0) / xs < 2.5 else ""
        near += "d" if (py - y0) / ys < 0.8 else ""     # (the left and bottom edges carry the numbers; the right
        #                                                   and top edges are pale grid, and a name may pass them)
        if x0 < 0 < x1:                         # the y-axis inside a four-quadrant plane is a line too
            near += "l" if 0 < px / xs < 2.5 else "r" if 0 < -px / xs < 2.5 else ""
        if y0 < 0 < y1:
            near += "d" if 0 < py / ys < 0.8 else "u" if 0 < -py / ys < 0.8 else ""
    best, where = -1e9, "ur"
    for w, ang in (("ur", 45), ("ul", 135), ("dl", 225), ("dr", 315), ("r", 0), ("l", 180), ("u", 90), ("d", 270)):
        gap = min((min(abs(ang - d), 360 - abs(ang - d)) for d in dirs), default=180)
        score = gap - 60 * sum(c in near for c in w) - (30 if len(w) == 1 else 0)   # a name set straight above
        #                                                   or beside its dot is wide: a corner, where one is clear
        if score > best + 1e-9:
            best, where = score, w
    return where


def table(rows, head=("x", "y"), cw=1.25, rh=1.0, fs=22, pt=9.5, inches=None, titles=None, hw=None):
    """One or more ratio tables side by side, each a row of x's over a row of y's, the rows named by `head`
    ("x", "y" or "hours", "pay ($)"). `rows` is a list of tables; a table is (xs, ys) with "▢" (BLANK) for a value
    the question asks — drawn as an empty box — and "" for a cell left empty. `titles` (one per table) print above.
    `hw` is the width of the names' column (default: room for the longer name). Numbers are printed as given:
    a number is printed by `_minus` (6.4 stays 6.4); money with two decimals is given as a string ("6.40")."""
    sh = []
    left = 0.0
    if hw is None:
        hw = max(cw, 0.36 * max(len(h) for h in head) + 0.6)
    for k, (xv, yv) in enumerate(rows):
        if len(xv) != len(yv):
            raise ValueError("table: a table's two rows must be the same length")
        n = len(xv)
        W = hw + n * cw
        for r in range(3):
            sh.append(dict(t="seg", a=(left, -r * rh), b=(left + W, -r * rh)))
        for c in range(n + 1):
            x = left + (0 if c == 0 else hw + (c - 1) * cw)
            sh.append(dict(t="seg", a=(x, 0), b=(x, -2 * rh)))
        sh.append(dict(t="seg", a=(left + W, 0), b=(left + W, -2 * rh)))
        for r, (h, vals) in enumerate(((head[0], xv), (head[1], yv))):
            yc = -(r + 0.5) * rh
            sh.append(_t(left + hw / 2, yc, h))
            for c, v in enumerate(vals):
                xc = left + hw + (c + 0.5) * cw
                s = v if isinstance(v, str) else _minus(v)
                if s == BLANK:
                    q = 0.24 * min(cw, rh)
                    for (a, b) in (((xc - q, yc - q), (xc + q, yc - q)), ((xc + q, yc - q), (xc + q, yc + q)),
                                   ((xc + q, yc + q), (xc - q, yc + q)), ((xc - q, yc + q), (xc - q, yc - q))):
                        sh.append(dict(t="seg", a=a, b=b))
                elif s:
                    sh.append(_t(xc, yc, s))
        if titles and titles[k]:
            sh.append(_t(left + W / 2, 0, titles[k], va="bottom", off=(0, 0.4)))
        left += W + 1.2
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


def choices4(specs, letters="ABCD", gap=2.2, fs=22, pt=18, inches=14.0):
    """Four small graphs (each a `plane`, drawn small: a short window, `step=` thinned) in a row, lettered A–D over
    each, for a choice board ("Which graph shows it?"). Its options are then the letters. At `inches` = 11 and
    pt = 18 a plane of 6 by 6 cells stands about 2.4 in tall — see FIGS7.md for what fits."""
    if len(specs) != len(letters):
        raise ValueError("choices4: one graph for each letter")
    return row(specs, gap=gap, titles=list(letters), fs=fs, pt=pt, inches=inches)


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
