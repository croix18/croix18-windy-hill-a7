# -*- coding: utf-8 -*-
"""Unit 6 figures — triangles, grids, shadows and angles, each drawn from its own numbers (figkit `shapes`).

Every helper takes the lengths, coordinates or angles the student reads and returns a spec; the drawing is to scale,
so a hypotenuse really is the longest side and a 3-4-5 triangle really has a square corner. A length that follows from
the others is computed, never typed: a right triangle refuses a printed hypotenuse that is not √(a² + b²), a triangle
from three sides refuses three lengths that cannot close, and a grid refuses a point off its own axes (ruling 38;
M7 `u4/figs.py` is the model). A label sits over the middle of the side it measures, stepped off it in ems (`off`),
never in a corner (ruling 44's look-through)."""
import math
import re

INK = "#1A1A1A"
GRID = "#C8C8C8"          # the pale unit grid: not ink to the struck-label check
SHADE = "#E4E9F1"         # a light fill that marks a piece (a shadow, an angle)


def _t(x, y, s, **k):
    return dict(t="text", xy=(x, y), s=s, **k)


def slide(spec, inches=3.4, pt=18, reserve=0.45, max_h=None):
    """The same figure sized for a slide: wider, with labels that read from the back row. `reserve` is the room left
    under the figure for the line that follows it; `max_h` narrows a tall figure (a ladder against a wall) so that the
    whole picture, labels included, is no taller than that many inches and no wider than `inches`. The labels keep
    their size in points while the drawing shrinks, so the width is found by drawing it (the kit's own renderer,
    a few passes) rather than guessed from the drawing's proportions."""
    out = dict(spec)
    out["pt"] = pt
    out["reserve"] = reserve
    out["in"] = inches
    if not max_h:
        return out
    from lib import figkit

    def height(w):
        out["in"] = round(w, 2)
        return figkit.draw(figkit.slide(out), out["in"])[2]

    # height grows with width, nearly in a straight line once the labels' fixed size is counted: two draws give the
    # line, and a secant step or two lands on max_h
    w0, h0 = inches, height(inches)
    if h0 <= max_h:
        return out
    w1 = w0 * max_h / h0
    h1 = height(w1)
    for _ in range(3):
        if abs(h1 - max_h) <= max_h * 0.02 or h1 == h0:
            break
        w2 = max(0.4, min(inches, w1 + (max_h - h1) * (w0 - w1) / (h0 - h1)))
        w0, h0, w1, h1 = w1, h1, w2, height(w2)
    if h1 > max_h * 1.02:                    # still too tall: step down until it fits
        while h1 > max_h * 1.02 and w1 > 0.5:
            w1 *= 0.95
            h1 = height(w1)
    out["in"] = round(w1, 2)
    return out


def fit_width(spec, w, h):
    """The width to draw `spec` at so that its drawing (the shapes, not counting their labels' overhang) is no taller
    than h inches, and no wider than w."""
    xs, ys = [], []
    for s in spec.get("shapes", []):
        if s["t"] == "poly":
            xs += [p[0] for p in s["pts"]]; ys += [p[1] for p in s["pts"]]
        elif s["t"] == "seg":
            xs += [s["a"][0], s["b"][0]]; ys += [s["a"][1], s["b"][1]]
        elif s["t"] == "circle":
            xs += [s["c"][0] - s["r"], s["c"][0] + s["r"]]; ys += [s["c"][1] - s["r"], s["c"][1] + s["r"]]
    if not xs:
        return w
    bw, bh = (max(xs) - min(xs)) or 1.0, (max(ys) - min(ys)) or 1.0
    return round(min(w, h * bw / bh * 1.08), 2)


def _num(label):
    """The number a label prints, or None for a letter, '?' or a root ('√74')."""
    if label is None or "√" in str(label):
        return None
    m = re.match(r"\s*(\d+(?:\.\d+)?)", str(label).replace(",", ""))
    return float(m.group(1)) if m else None


def _lab(text, unit):
    """'8' + 'cm' -> '8 cm'; a letter or '?' carries no unit."""
    if text is None or text == "":
        return None
    t = str(text)
    if unit and _num(t) is not None and not t.endswith(unit):
        return f"{t} {unit}"
    if unit and "√" in t and not t.endswith(unit):
        return f"{t} {unit}"
    return t


def _rot(p, deg, about=(0.0, 0.0)):
    a = math.radians(deg)
    x, y = p[0] - about[0], p[1] - about[1]
    return (about[0] + x * math.cos(a) - y * math.sin(a), about[1] + x * math.sin(a) + y * math.cos(a))


def _side_label(p, q, centre, text, gap=0.35):
    """A label over the middle of side pq, on the side away from `centre`, stepped off by `gap` ems."""
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = q[0] - p[0], q[1] - p[1]
    n = (-dy, dx)
    if (n[0] * (mx - centre[0]) + n[1] * (my - centre[1])) < 0:
        n = (dy, -dx)
    L = math.hypot(*n) or 1.0
    nx, ny = n[0] / L, n[1] / L
    half_w = 0.30 * len(str(text))          # half the label's width, in ems (a Lexend digit is about 0.6 em)
    if abs(nx) > 1.6 * abs(ny):                                     # a side that runs up and down
        # the side leans by |dx/dy| over the label's half-height (0.5 em): step out by that much more
        lean = abs(dx / dy) if dy else 0.0
        return _t(mx, my, text, ha="left" if nx > 0 else "right", va="center",
                  off=((gap + 0.1 + 0.5 * lean) * (1 if nx > 0 else -1), 0))
    if abs(ny) > 1.6 * abs(nx):                                     # a side that runs across
        # the side rises by |dy/dx| over the label's half-width: step off by that much more
        lean = abs(dy / dx) if dx else 0.0
        return _t(mx, my, text, ha="center", va="bottom" if ny > 0 else "top",
                  off=(0, (gap + half_w * lean) * (1 if ny > 0 else -1)))
    return _t(mx, my, text, ha="left" if nx > 0 else "right", va="bottom" if ny > 0 else "top",
              off=(gap * 0.8 * (1 if nx > 0 else -1), gap * 0.8 * (1 if ny > 0 else -1)))


def _centre(pts):
    return (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))


def right_triangle(a, b, la=None, lb=None, lc=None, unit="", turn=0, flip=False, fs=22, pt=9.5, inches=2.2,
                   names=None):
    """A right triangle with legs a (along the bottom) and b (up the side), drawn to scale with its right-angle mark.
    la, lb, lc are what the legs and the hypotenuse print (a number, a letter, '?' or None for nothing); a numeric lc
    must be √(a² + b²) to its own decimal places. `turn` rotates the whole picture (degrees, counterclockwise) so the
    right angle can sit anywhere; `flip` puts the right angle at the bottom right instead of the bottom left.
    `names` = three vertex letters (right-angle vertex first)."""
    c = math.hypot(a, b)
    if lc is not None and _num(lc) is not None:
        v = _num(lc)
        places = len(str(lc).split()[0].split(".")[1]) if "." in str(lc).split()[0] else 0
        if abs(v - round(c, places)) > 1e-9:
            raise ValueError(f"right_triangle({a}, {b}): the hypotenuse is {c:.4f}, not {lc}")
    for leg, lab in ((a, la), (b, lb)):
        if lab is not None and _num(lab) is not None and abs(_num(lab) - leg) > 1e-9:
            raise ValueError(f"right_triangle({a}, {b}): a leg is {leg}, not {lab}")
    if flip:
        R, P, Q = (a, 0.0), (0.0, 0.0), (a, b)          # right angle at the bottom right
    else:
        R, P, Q = (0.0, 0.0), (a, 0.0), (0.0, b)        # right angle at the bottom left
    pts = [_rot(R, turn), _rot(P, turn), _rot(Q, turn)]
    R2, P2, Q2 = pts
    cen = _centre(pts)
    s = min(a, b) * 0.13
    u = (P2[0] - R2[0], P2[1] - R2[1])
    v = (Q2[0] - R2[0], Q2[1] - R2[1])
    sh = [dict(t="poly", pts=pts), dict(t="ra", xy=R2, u=u, v=v, s=s)]
    for (p, q, lab) in ((R2, P2, la), (R2, Q2, lb), (P2, Q2, lc)):
        L = _lab(lab, unit)
        if L:
            sh.append(_side_label(p, q, cen, L))
    if names:
        for p, nm in zip(pts, names):
            dx, dy = p[0] - cen[0], p[1] - cen[1]
            d = math.hypot(dx, dy) or 1.0
            sh.append(_t(p[0], p[1], nm, ha="left" if dx > 0.05 * d else ("right" if dx < -0.05 * d else "center"),
                         va="bottom" if dy > 0.05 * d else ("top" if dy < -0.05 * d else "center"),
                         off=(0.35 * dx / d, 0.35 * dy / d)))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def triangle3(p, q, r, lp=None, lq=None, lr=None, unit="", turn=0, fs=22, pt=9.5, inches=2.2, right_mark=None):
    """A triangle from its three sides, drawn to scale: r along the bottom, p up the left, q up the right.
    Refuses three lengths that cannot close (the Triangle Inequality is the picture's own check). `right_mark`
    puts the square mark at the vertex opposite r when the three sides are a Pythagorean set (and refuses it when
    they are not)."""
    if not (p + q > r and p + r > q and q + r > p):
        raise ValueError(f"triangle3({p}, {q}, {r}): these three lengths do not make a triangle")
    x = (p * p - q * q + r * r) / (2 * r)
    y = math.sqrt(max(p * p - x * x, 0.0))
    A, B, C = (0.0, 0.0), (float(r), 0.0), (x, y)
    pts = [_rot(A, turn), _rot(B, turn), _rot(C, turn)]
    A2, B2, C2 = pts
    cen = _centre(pts)
    sh = [dict(t="poly", pts=pts)]
    if right_mark:
        if abs(p * p + q * q - r * r) > 1e-9:
            raise ValueError(f"triangle3({p}, {q}, {r}): no right angle opposite {r}")
        sh.append(dict(t="ra", xy=C2, u=(A2[0] - C2[0], A2[1] - C2[1]), v=(B2[0] - C2[0], B2[1] - C2[1]),
                       s=min(p, q) * 0.13))
    for (a_, b_, lab) in ((A2, C2, lp), (B2, C2, lq), (A2, B2, lr)):
        L = _lab(lab, unit)
        if L:
            sh.append(_side_label(a_, b_, cen, L))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def squares_on_sides(a, b, fs=22, pt=9.5, inches=2.6, sides=True):
    """A right triangle with legs a and b and a square drawn outward on each side, each square naming its area
    (a², b², and a² + b² on the hypotenuse — which is c² only because the triangle is right). Legs and the
    hypotenuse are named inside their squares ("3² = 9") when `sides` is True, so no length crowds the triangle."""
    c2 = a * a + b * b
    c = math.sqrt(c2)
    R, P, Q = (0.0, 0.0), (float(a), 0.0), (0.0, float(b))
    sh = [dict(t="poly", pts=[(0, 0), (a, 0), (a, -a), (0, -a)], fill=SHADE),
          dict(t="poly", pts=[(0, 0), (0, b), (-b, b), (-b, 0)], fill=SHADE),
          dict(t="poly", pts=[P, Q, (b, a + b), (a + b, a)], fill=SHADE),
          dict(t="poly", pts=[R, P, Q]),
          dict(t="ra", xy=R, u=(1, 0), v=(0, 1), s=min(a, b) * 0.14)]
    hyp = str(int(round(c))) if abs(c - round(c)) < 1e-9 else None
    if sides:                         # each square names its side and its area: "3² = 9"
        sh.append(_t(a / 2, -a / 2, f"{a}² = {a * a}"))
        sh.append(_t(-b / 2, b / 2, f"{b}² = {b * b}"))
        sh.append(_t((a + b) / 2, (a + b) / 2, f"{hyp}² = {c2}" if hyp else str(c2)))
    else:
        sh.append(_t(a / 2, -a / 2, str(a * a)))
        sh.append(_t(-b / 2, b / 2, str(b * b)))
        sh.append(_t((a + b) / 2, (a + b) / 2, str(c2)))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def strips(sets, unit="", fs=22, pt=9.5, inches=4.2):
    """Notes I of 6.01: three sets of sticks. Each set is (a, b, c) with c the longest: c lies along the bottom, a
    and b stand on its ends, tipped in until they meet (a triangle), lie flat on c (a + b = c), or fall short."""
    sh = []
    x0 = 0.0
    gap = max(s[2] for s in sets) * 0.5
    for (a, b, c) in sets:
        sh.append(dict(t="seg", a=(x0, 0), b=(x0 + c, 0)))
        if a + b > c:
            xm = (a * a - b * b + c * c) / (2 * c)
            ym = math.sqrt(max(a * a - xm * xm, 0.0))
            sh += [dict(t="seg", a=(x0, 0), b=(x0 + xm, ym)), dict(t="seg", a=(x0 + c, 0), b=(x0 + xm, ym))]
            note = "a triangle"
        elif a + b == c:
            lift = c * 0.04
            sh += [dict(t="seg", a=(x0, lift), b=(x0 + a, lift)), dict(t="seg", a=(x0 + a, lift), b=(x0 + c, lift))]
            note = "flat"
        else:
            ang = math.radians(50)
            sh += [dict(t="seg", a=(x0, 0), b=(x0 + a * math.cos(ang), a * math.sin(ang))),
                   dict(t="seg", a=(x0 + c, 0), b=(x0 + c - b * math.cos(ang), b * math.sin(ang)))]
            note = "a gap"
        sh.append(_t(x0 + c / 2, 0, f"{a}, {b}, {c}", va="top", off=(0, -0.35)))
        sh.append(_t(x0 + c / 2, 0, note, va="top", off=(0, -1.6)))
        x0 += c + gap
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def ladder(wall, foot, l_ladder=None, l_wall=None, l_foot=None, unit="ft", fs=22, pt=9.5, inches=2.0):
    """A ladder leaning on a wall: the wall stands up from the ground, the ladder from its foot on the ground to the
    wall. `wall` is how high the ladder's top is, `foot` how far its foot is from the wall; the ladder's own length
    follows from them and a numeric l_ladder must agree."""
    c = math.hypot(wall, foot)
    if l_ladder is not None and _num(l_ladder) is not None:
        v = _num(l_ladder)
        places = len(str(l_ladder).split()[0].split(".")[1]) if "." in str(l_ladder).split()[0] else 0
        if abs(v - round(c, places)) > 1e-9:
            raise ValueError(f"ladder({wall}, {foot}): the ladder is {c:.4f}, not {l_ladder}")
    W = foot * 0.12 + 0.2                      # the wall's thickness, drawn to the left of x = 0
    top = wall * 1.18
    cen = (foot * 0.33, wall * 0.33)
    sh = [dict(t="poly", pts=[(-W, 0), (0, 0), (0, top), (-W, top)], fill="#D9D4CC"),
          dict(t="seg", a=(-W - foot * 0.15, 0), b=(foot * 1.25, 0)),
          dict(t="seg", a=(foot, 0), b=(0, wall)),
          dict(t="ra", xy=(0, 0), u=(1, 0), v=(0, 1), s=min(foot, wall) * 0.12)]
    for (p, q, lab) in (((0, 0), (0, wall), l_wall), ((0, 0), (foot, 0), l_foot), ((foot, 0), (0, wall), l_ladder)):
        L = _lab(lab, unit)
        if L:
            if p == (0, 0) and q == (0, wall):          # the height goes inside, beside the wall, clear of the ladder
                sh.append(_t(0, wall * 0.42, L, ha="left", va="center", off=(0.45, 0)))
            else:
                sh.append(_side_label(p, q, cen, L))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def rect_diagonal(w, h, lw=None, lh=None, ld=None, unit="", fs=22, pt=9.5, inches=2.2):
    """A w-by-h rectangle with one diagonal drawn; a numeric ld must be the diagonal's true length."""
    d = math.hypot(w, h)
    if ld is not None and _num(ld) is not None:
        v = _num(ld)
        places = len(str(ld).split()[0].split(".")[1]) if "." in str(ld).split()[0] else 0
        if abs(v - round(d, places)) > 1e-9:
            raise ValueError(f"rect_diagonal({w}, {h}): the diagonal is {d:.4f}, not {ld}")
    pts = [(0, 0), (w, 0), (w, h), (0, h)]
    sh = [dict(t="poly", pts=pts), dict(t="seg", a=(0, 0), b=(w, h)),
          dict(t="ra", xy=(w, 0), u=(-1, 0), v=(0, 1), s=min(w, h) * 0.1)]
    if _lab(lw, unit):
        sh.append(_t(w / 2, 0, _lab(lw, unit), va="top", off=(0, -0.35)))
    if _lab(lh, unit):
        sh.append(_t(w, h / 2, _lab(lh, unit), ha="left", off=(0.45, 0)))
    if _lab(ld, unit):
        # above the diagonal's middle, on the upper-left triangle's side of it
        sh.append(_t(w / 2, h / 2, _lab(ld, unit), ha="right", va="bottom", off=(-0.2, 0.25)))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def ramp(run, rise, l_run=None, l_rise=None, l_ramp=None, unit="ft", fs=22, pt=9.5, inches=2.6):
    """A ramp: the run along the ground, the rise at the high end, the ramp the slanted side. The rise is drawn
    to scale, so a gentle ramp looks gentle."""
    return right_triangle(run, rise, la=l_run, lb=l_rise, lc=l_ramp, unit=unit, flip=True, fs=fs, pt=pt,
                          inches=inches)


def grid(xr, yr, points=(), segs=(), legs=None, step=None, fs=22, pt=9.5, inches=3.0, labels=True, polys=()):
    """A coordinate plane from xr[0] to xr[1] and yr[0] to yr[1] with the pale unit grid, the two axes and their
    numbers. `points` are (x, y, name) — a name prints beside the point with its coordinates when `labels` is True
    ("A(−3, 2)"); `segs` are ((x, y), (x, y), dashed); `legs` = ((x1, y1), (x2, y2)) draws the dashed horizontal and
    vertical legs of the right triangle under a slanted segment, with their lengths. A point off the plane is
    refused."""
    x0, x1 = xr
    y0, y1 = yr
    for (px, py, *_rest) in points:
        if not (x0 <= px <= x1 and y0 <= py <= y1):
            raise ValueError(f"grid: point ({px}, {py}) is off the plane {xr} × {yr}")
    sh = []
    for x in range(x0, x1 + 1):
        sh.append(dict(t="seg", a=(x, y0), b=(x, y1), color=GRID))
    for y in range(y0, y1 + 1):
        sh.append(dict(t="seg", a=(x0, y), b=(x1, y), color=GRID))
    if y0 <= 0 <= y1:                       # the axes end at the plane's edge, so they cross none of its numbers
        sh.append(dict(t="seg", a=(x0, 0), b=(x1, 0)))
        sh.append(_t(x1, 0, "x", ha="left", va="center", off=(0.35, 0)))
    if x0 <= 0 <= x1:
        sh.append(dict(t="seg", a=(0, y0), b=(0, y1)))
        sh.append(_t(0, y1, "y", ha="center", va="bottom", off=(0, 0.3)))
    if step is None:
        # a number every unit when a cell is wide enough for "−6" at this type size, else every other one
        cell = inches * 72.0 / max(x1 - x0 + 1.4, 1)
        step = 1 if cell >= 1.45 * pt else 2
    # the axes' numbers sit OUTSIDE the plane (below its bottom edge, left of its left edge), where no segment, leg
    # or point label can cross them; the grid lines lead the eye from a number to its axis
    for x in range(x0, x1 + 1):
        if x % step == 0:
            sh.append(_t(x, y0, _minus(x), ha="center", va="top", off=(0, -0.35)))
    for y in range(y0, y1 + 1):
        if y % step == 0:
            sh.append(_t(x0, y, _minus(y), ha="right", va="center", off=(-0.35, 0)))
    for poly in polys:
        sh.append(dict(t="poly", pts=[tuple(p) for p in poly], fill=SHADE))
    lines = []                                   # every segment, for placing the point labels clear of them
    for (p, q, dashed) in segs:
        sh.append(dict(t="seg", a=p, b=q, dash=bool(dashed)))
        lines.append((p, q))
    for poly in polys:
        for i in range(len(poly)):
            lines.append((tuple(poly[i]), tuple(poly[(i + 1) % len(poly)])))
    if legs:
        (ax, ay), (bx, by) = legs
        corner = (bx, ay)
        sh += [dict(t="seg", a=(ax, ay), b=corner, dash=True), dict(t="seg", a=corner, b=(bx, by), dash=True)]
        lines += [((ax, ay), corner), (corner, (bx, by))]
        dx, dy = abs(bx - ax), abs(by - ay)
        # each leg's length beside its middle, on the side away from the slanted segment — unless an axis runs
        # within a unit and a half on that side, when it goes inside the triangle instead (the slanted side is
        # farther away there than the axis is outside)
        below = by > ay
        if (below and 0 < ay - 0 <= 1.5) or (not below and 0 < 0 - ay <= 1.5):
            below = not below
        sh.append(_t((ax + bx) / 2, ay, str(dx), ha="center", va="top" if below else "bottom",
                     off=(0, -0.4 if below else 0.4)))
        right = bx > ax
        if (right and 0 < 0 - bx <= 1.5) or (not right and 0 < bx - 0 <= 1.5):
            right = not right
        sh.append(_t(bx, (ay + by) / 2, str(dy), ha="left" if right else "right", va="center",
                     off=(0.45 if right else -0.45, 0)))
    for item in points:
        px, py, name = item[0], item[1], item[2]
        where = item[3] if len(item) > 3 else _clear_corner((px, py), lines, (x0, x1, y0, y1))
        sh.append(dict(t="circle", c=(px, py), r=0.14, fill=INK))
        if name or labels:
            txt = (f"{name}({_minus(px)}, {_minus(py)})" if labels else name) if name else f"({_minus(px)}, {_minus(py)})"
            ha = "left" if "r" in where else "right"
            va = "bottom" if "u" in where else "top"
            sh.append(_t(px, py, txt, ha=ha, va=va, off=(0.35 if ha == "left" else -0.35, 0.3 if va == "bottom" else -0.3)))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def _clear_corner(pt, lines, box=None):
    """Which diagonal ('ur', 'ul', 'dl', 'dr') beside a point is farthest, in angle, from every line leaving it —
    never toward an edge of the plane within three units (the axes' numbers live outside those edges, and a label
    there runs off the grid)."""
    dirs = []
    for (p, q) in lines:
        for (a, b) in ((p, q), (q, p)):
            if abs(a[0] - pt[0]) < 1e-9 and abs(a[1] - pt[1]) < 1e-9:
                dirs.append(math.degrees(math.atan2(b[1] - a[1], b[0] - a[0])) % 360)
            elif _on_seg(pt, a, b):
                d = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0])) % 360
                dirs += [d, (d + 180) % 360]
    best, where = -1, "ur"
    for w, ang in (("ur", 45), ("ul", 135), ("dl", 225), ("dr", 315)):
        if box:
            x0, x1, y0, y1 = box
            if ("l" in w and pt[0] - x0 < 3) or ("r" in w and x1 - pt[0] < 3) \
                    or ("d" in w and pt[1] - y0 < 1.5) or ("u" in w and y1 - pt[1] < 1.5):
                continue
        gap = min((min(abs(ang - d), 360 - abs(ang - d)) for d in dirs), default=180)
        if gap > best + 1e-9:
            best, where = gap, w
    return where


def _on_seg(p, a, b):
    cross = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
    return abs(cross) < 1e-9 and min(a[0], b[0]) - 1e-9 <= p[0] <= max(a[0], b[0]) + 1e-9 \
        and min(a[1], b[1]) - 1e-9 <= p[1] <= max(a[1], b[1]) + 1e-9


def _minus(v):
    v = int(v) if float(v).is_integer() else v
    return str(v).replace("-", "−")


def similar_pair(t1, t2, l1=(None, None, None), l2=(None, None, None), unit="", turn2=0, flip2=False, fs=22, pt=9.5,
                 inches=4.0, names=None, angles=None, gap=0.8):
    """Two triangles side by side, each from its three sides (p, q, r as `triangle3` reads them). The second may be
    turned (`turn2`, degrees) or mirrored (`flip2`) so its matching sides are not where the first one's are. Every
    numeric label must be its side's true length (the picture is to scale)."""
    def tri(t, turn, flip):
        p, q, r = t
        if not (p + q > r and p + r > q and q + r > p):
            raise ValueError(f"similar_pair: {t} does not make a triangle")
        x = (p * p - q * q + r * r) / (2 * r)
        y = math.sqrt(max(p * p - x * x, 0.0))
        pts = [(0.0, 0.0), (float(r), 0.0), (x, y)]
        if flip:
            pts = [(r - X, Y) for (X, Y) in pts]
        return [_rot(P, turn) for P in pts]
    A = tri(t1, 0, False)
    B = tri(t2, turn2, flip2)
    # `gap` is in widths of the first triangle: the two facing sides' labels both stand in it, so a slide (larger
    # labels on a smaller picture) passes a wider one
    room = max(max(X for X, _ in A) - min(X for X, _ in A), 1.0) * gap
    shift = max(X for X, _ in A) + room - min(X for X, _ in B)
    ylift = min(Y for _, Y in A) - min(Y for _, Y in B)
    B = [(X + shift, Y + ylift) for (X, Y) in B]
    sh = [dict(t="poly", pts=A), dict(t="poly", pts=B)]
    for pts, t, labs in ((A, t1, l1), (B, t2, l2)):
        cen = _centre(pts)
        P0, P1, P2 = pts
        for (p_, q_, lab, true) in ((P0, P2, labs[0], t[0]), (P1, P2, labs[1], t[1]), (P0, P1, labs[2], t[2])):
            if lab is not None and _num(lab) is not None and abs(_num(lab) - true) > 1e-9:
                raise ValueError(f"similar_pair: a side of {t} is {true}, not {lab}")
            L = _lab(lab, unit)
            if L:
                sh.append(_side_label(p_, q_, cen, L))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def shadow(h1, s1, h2, s2, l=(None, None, None, None), unit="ft", what=("person", "tree"), fs=22, pt=9.5,
           inches=4.0):
    """Two right triangles in the same sun: an upright thing of height h and its shadow s along the ground, the sun's
    ray the slanted side (dashed). Similar by construction only when h1/s1 = h2/s2 — refused otherwise."""
    if abs(h1 * s2 - h2 * s1) > 1e-9:
        raise ValueError(f"shadow: {h1}/{s1} and {h2}/{s2} are not the same sun")
    gap = max(s1, s2) * 0.6
    X2 = s1 + gap
    sh = [dict(t="seg", a=(-s1 * 0.15, 0), b=(X2 + s2 * 1.15, 0)),
          dict(t="poly", pts=[(0, 0), (s1, 0), (0, h1)], fill=SHADE),
          dict(t="poly", pts=[(X2, 0), (X2 + s2, 0), (X2, h2)], fill=SHADE),
          dict(t="seg", a=(0, 0), b=(0, h1)), dict(t="seg", a=(X2, 0), b=(X2, h2)),
          dict(t="ra", xy=(0, 0), u=(1, 0), v=(0, 1), s=min(s1, h1) * 0.14),
          dict(t="ra", xy=(X2, 0), u=(1, 0), v=(0, 1), s=min(s2, h2) * 0.14)]
    labs = [_lab(x, unit) for x in l]
    if labs[0]:
        sh.append(_t(0, h1 / 2, labs[0], ha="right", va="center", off=(-0.4, 0)))
    if labs[1]:
        sh.append(_t(s1 / 2, 0, labs[1], ha="center", va="top", off=(0, -0.35)))
    if labs[2]:
        sh.append(_t(X2, h2 / 2, labs[2], ha="right", va="center", off=(-0.4, 0)))
    if labs[3]:
        sh.append(_t(X2 + s2 / 2, 0, labs[3], ha="center", va="top", off=(0, -0.35)))
    if what:
        sh.append(_t(0, h1, what[0], ha="center", va="bottom", off=(0, 0.3)))
        sh.append(_t(X2, h2, what[1], ha="center", va="bottom", off=(0, 0.3)))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def nested(b1, h1, b2, l=(None, None, None, None), unit="m", fs=22, pt=9.5, inches=4.0):
    """Two right triangles sharing the corner A at the left: a slope from A rises h1 over the first b1 along the
    ground and h2 = h1 · b2 / b1 over the whole b2 (similar by construction — the second height is computed, never
    typed). l = (h1, b1, b2, h2) as printed; b2 is measured from A, on a dimension line under the ground."""
    if not (0 < b1 < b2):
        raise ValueError(f"nested: the near upright ({b1}) must stand between A and the far one ({b2})")
    h2 = h1 * b2 / b1
    for lab, true in ((l[0], h1), (l[1], b1), (l[2], b2), (l[3], h2)):
        if lab is not None and _num(lab) is not None and abs(_num(lab) - true) > 1e-9:
            raise ValueError(f"nested: a length is {true}, not {lab}")
    dy = -max(h2, b2 * 0.25) * 0.55           # the dimension line for the whole distance, under the ground and clear of b1's label
    tick = abs(dy) * 0.18
    sh = [dict(t="poly", pts=[(0, 0), (b2, 0), (b2, h2)], fill=SHADE),
          dict(t="seg", a=(b1, 0), b=(b1, h1)),
          dict(t="ra", xy=(b1, 0), u=(-1, 0), v=(0, 1), s=min(b1, h1) * 0.16),
          dict(t="ra", xy=(b2, 0), u=(-1, 0), v=(0, 1), s=min(b2 - b1, h2) * 0.12),
          dict(t="seg", a=(0, dy), b=(b2, dy)),
          dict(t="seg", a=(0, dy - tick), b=(0, dy + tick)), dict(t="seg", a=(b2, dy - tick), b=(b2, dy + tick))]
    labs = [_lab(x, unit) for x in l]
    if labs[0]:
        sh.append(_t(b1, h1 / 2, labs[0], ha="left", va="center", off=(0.35, 0)))
    if labs[1]:
        sh.append(_t(b1 / 2, 0, labs[1], ha="center", va="top", off=(0, -0.3)))
    if labs[2]:
        sh.append(_t(b2 / 2, dy, labs[2], ha="center", va="top", off=(0, -0.3)))
    if labs[3]:
        sh.append(_t(b2, h2 / 2, labs[3], ha="left", va="center", off=(0.4, 0)))
    sh.append(_t(0, 0, "A", ha="right", va="bottom", off=(-0.3, 0.1)))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def mirror(h1, d1, h2, d2, l=(None, None, None, None), unit="ft", what=("person", "tree"), fs=22, pt=9.5,
           inches=4.2):
    """The mirror on the ground: a person whose eyes are h1 above the ground stands d1 from a mirror and sees the top
    of something h2 tall standing d2 beyond it. The light (dashed) comes down to the mirror and up to the eyes at
    equal angles, so the two right triangles are similar — refused unless h1/d1 = h2/d2. l = (h1, d1, d2, h2)."""
    if abs(h1 * d2 - h2 * d1) > 1e-9:
        raise ValueError(f"mirror: {h1}/{d1} and {h2}/{d2} are not equal angles at the mirror")
    for lab, true in ((l[0], h1), (l[1], d1), (l[2], d2), (l[3], h2)):
        if lab is not None and _num(lab) is not None and abs(_num(lab) - true) > 1e-9:
            raise ValueError(f"mirror: a length is {true}, not {lab}")
    M, X2 = (d1, 0.0), d1 + d2
    w = (d1 + d2) * 0.035
    sh = [dict(t="seg", a=(-d1 * 0.2, 0), b=(X2 + d2 * 0.12, 0)),
          dict(t="poly", pts=[(0, 0), M, (0, h1)], fill=SHADE),
          dict(t="poly", pts=[M, (X2, 0), (X2, h2)], fill=SHADE),
          dict(t="seg", a=(0, 0), b=(0, h1)), dict(t="seg", a=(X2, 0), b=(X2, h2)),
          dict(t="seg", a=(d1 - w, 0), b=(d1 + w, 0), lw=4.0),
          dict(t="ra", xy=(0, 0), u=(1, 0), v=(0, 1), s=min(d1, h1) * 0.14),
          dict(t="ra", xy=(X2, 0), u=(-1, 0), v=(0, 1), s=min(d2, h2) * 0.1)]
    labs = [_lab(x, unit) for x in l]
    if labs[0]:
        sh.append(_t(0, h1 / 2, labs[0], ha="right", va="center", off=(-0.4, 0)))
    if labs[1]:
        sh.append(_t(d1 / 2, 0, labs[1], ha="center", va="top", off=(0, -0.35)))
    if labs[2]:
        sh.append(_t(d1 + d2 / 2, 0, labs[2], ha="center", va="top", off=(0, -0.35)))
    if labs[3]:
        sh.append(_t(X2, h2 / 2, labs[3], ha="left", va="center", off=(0.4, 0)))
    sh.append(_t(d1, 0, "mirror", ha="center", va="top", off=(0, -1.5)))
    if what:
        sh.append(_t(0, h1, what[0], ha="center", va="bottom", off=(0, 0.3)))
        sh.append(_t(X2, h2, what[1], ha="center", va="bottom", off=(0, 0.3)))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


# ---- angles (Thread B) -------------------------------------------------------------------------------------------
def _ray(deg, r):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


def _arc_label(deg0, deg1, r, text, centre=(0.0, 0.0), push=0.55):
    """A label for the angle from deg0 to deg1 (counterclockwise), on its bisector just outside the arc."""
    mid = math.radians((deg0 + deg1) / 2)
    x, y = centre[0] + r * math.cos(mid), centre[1] + r * math.sin(mid)
    c, s = math.cos(mid), math.sin(mid)
    ha = "left" if c > 0.35 else ("right" if c < -0.35 else "center")
    va = "bottom" if s > 0.35 else ("top" if s < -0.35 else "center")
    return _t(x, y, text, ha=ha, va=va, off=(push * c, push * s))


def crossing(a_deg, labels, R=3.0, fs=22, pt=9.5, inches=2.6, names=None):
    """Two lines crossing at the origin: one along 0°–180°, the other at `a_deg` (0 < a < 180). The four angles,
    counterclockwise from the right: a, 180 − a, a, 180 − a. `labels` names what each prints (a measure, a letter,
    an expression, or None); a numeric label must be that angle's measure. An arc marks only an angle that prints
    something; `names` puts a letter (1, 2, 3, 4 or A, B …) inside the angle instead of a measure."""
    meas = [a_deg, 180 - a_deg, a_deg, 180 - a_deg]
    starts = [0, a_deg, 180, 180 + a_deg]
    for lab, m in zip(labels, meas):
        if lab is not None and _num(lab) is not None and "x" not in str(lab) and abs(_num(lab) - m) > 1e-9:
            raise ValueError(f"crossing({a_deg}): an angle is {m}°, not {lab}")
    sh = [dict(t="seg", a=_ray(180, R), b=_ray(0, R)), dict(t="seg", a=_ray(180 + a_deg, R), b=_ray(a_deg, R))]
    r = R * 0.16
    for i, lab in enumerate(labels):
        if lab:
            rr = r * (1.0 if i % 2 == 0 else 1.25)
            sh.append(dict(t="circle", c=(0, 0), r=rr, a=(starts[i], starts[i] + meas[i]), fill="none"))
            sh.append(_arc_label(starts[i], starts[i] + meas[i], rr * 1.15, lab))
    if names:
        for i, nm in enumerate(names):
            if nm:
                sh.append(_arc_label(starts[i], starts[i] + meas[i], R * 0.55, nm, push=0.0))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def triangle_exterior(A, B, l_A=None, l_B=None, l_C=None, l_ext=None, fs=22, pt=9.5, inches=3.0, base=6.0):
    """A triangle with interior angles A (bottom left) and B (top), the third angle C at the bottom right, and the
    bottom side extended past C to show the exterior angle at C (= A + B). Numeric labels must be the true measures."""
    Cdeg = 180 - A - B
    if not (A > 0 and B > 0 and Cdeg > 0):
        raise ValueError(f"triangle_exterior({A}, {B}): not a triangle")
    for lab, m in ((l_A, A), (l_B, B), (l_C, Cdeg), (l_ext, A + B)):
        if lab is not None and _num(lab) is not None and "x" not in str(lab) and abs(_num(lab) - m) > 1e-9:
            raise ValueError(f"triangle_exterior({A}, {B}): an angle is {m}°, not {lab}")
    # bottom side from P (angle A) to Q (angle C); apex T from the law of sines
    P, Q = (0.0, 0.0), (base, 0.0)
    side_PT = base * math.sin(math.radians(Cdeg)) / math.sin(math.radians(B))
    T = (side_PT * math.cos(math.radians(A)), side_PT * math.sin(math.radians(A)))
    ext = (base * 1.45, 0.0)
    sh = [dict(t="poly", pts=[P, Q, T]), dict(t="seg", a=Q, b=ext)]
    r = base * 0.12
    # arcs: A at P from 0 to A; C at Q from (180 - C) to 180; exterior at Q from 0 to (180 - C); B at T
    angTP = math.degrees(math.atan2(P[1] - T[1], P[0] - T[0])) % 360
    angTQ = math.degrees(math.atan2(Q[1] - T[1], Q[0] - T[0])) % 360
    lo, hi = sorted((angTP, angTQ))
    arcs = [(P, 0, A, l_A), (Q, 180 - Cdeg, 180, l_C), (Q, 0, 180 - Cdeg, l_ext), (T, lo, hi, l_B)]
    for (cpt, a0, a1, lab) in arcs:
        if lab is None:
            continue
        rr = r * (1.35 if (cpt == Q and a0 == 0) else 1.0)
        if cpt == T:                       # the top angle is the narrowest: a bigger arc, the label well inside it
            rr = r * 1.6
        sh.append(dict(t="circle", c=cpt, r=rr, a=(a0, a1), fill="none"))
        sh.append(_arc_label(a0, a1, rr * (1.25 if cpt == T else 1.1), lab, centre=cpt,
                             push=0.9 if cpt == T else 0.55))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)


def rays(dirs, arcs, R=3.0, fs=22, pt=9.5, inches=2.6, line=None):
    """Rays from one vertex at the origin, at the directions `dirs` (degrees, counterclockwise from the right).
    `arcs` is a list of (i, j, label) — the angle from ray i to ray j, counterclockwise; a numeric label must be its
    true measure, and a label of "ra" draws the square mark of a right angle instead of an arc. `line` = (i, j) draws
    rays i and j as one straight line through the vertex (a linear pair)."""
    for (i, j, lab) in arcs:
        m = (dirs[j] - dirs[i]) % 360
        if lab == "ra":
            if abs(m - 90) > 1e-9:
                raise ValueError(f"rays: the angle from ray {i} to ray {j} is {m}°, not a right angle")
        elif lab and "\u00b0" in lab and not re.search(r"[a-z]", lab) and _num(lab) is not None \
                and abs(_num(lab) - m) > 1e-9:
            raise ValueError(f"rays: the angle from ray {i} to ray {j} is {m}°, not {lab}")   # a bare '1' names an angle
    sh = [dict(t="seg", a=(0.0, 0.0), b=_ray(d, R)) for d in dirs]
    r = R * (0.27 if any(lab == "ra" for _, _, lab in arcs) else 0.2)     # arcs stand clear of a right-angle mark
    for k, (i, j, lab) in enumerate(arcs):
        a0, a1 = dirs[i], dirs[i] + (dirs[j] - dirs[i]) % 360
        if lab == "ra":
            sh.append(dict(t="ra", xy=(0.0, 0.0), u=_ray(a0, 1.0), v=_ray(a1, 1.0), s=R * 0.12))
            continue
        rr = r * (1.0 + 0.22 * (k % 2))
        sh.append(dict(t="circle", c=(0, 0), r=rr, a=(a0, a1), fill="none"))
        if lab:
            sh.append(_arc_label(a0, a1, rr * 1.15, lab))
    return dict(kind="shapes", fs=fs, pt=pt, **{"in": inches}, shapes=sh)
