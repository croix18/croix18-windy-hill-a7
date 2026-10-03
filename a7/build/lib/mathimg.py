"""Expression images. Every fraction, radical or exponent expression that appears on a page is
rendered here from LaTeX (matplotlib mathtext, STIX) at ONE font size per surface, cropped to
its own ink, and recorded in figs/index.json with its natural size. Printed size = natural size,
so every digit in a document is the same size (HOUSE STYLE §8) by construction.

The index is MERGED, never rebuilt (HOUSE STYLE §2: "No generator rebuilds an index. Ever.").
A figure is fingerprinted by its LaTeX + size; editing one character re-renders exactly one file.
"""
import re, os, json, hashlib, warnings
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["mathtext.fontset"] = "stix"
matplotlib.rcParams["font.family"] = "STIXGeneral"
import matplotlib.pyplot as plt
from matplotlib.mathtext import MathTextParser
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Rectangle
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.normpath(os.path.join(HERE, "..", "figs"))
INDEX = os.path.join(FIGS, "index.json")
DPI = 300
# One digit size per surface. Documents: 13 pt (body is 11 pt; larger on purpose, §8).
# Slides: whiteboard display 40 pt, inline 26 pt.
SIZES = {"doc": 13, "docbig": 16, "slide": 26, "slidebig": 40, "slidemid": 32}

# ---- the slot colour code (HOUSE STYLE §2a), slides only ---------------------------------------
# One colour per slot in the expression: the BASE is the first slot, the EXPONENT is the second.
# Everything else — operators, equals signs, fraction bars, coefficients — has no slot and stays
# INK (rule 3). The slots are read off mathtext's own layout, never off the LaTeX source, so a
# base is whatever the renderer actually set a superscript on.
CB1, CB2, SLOT_INK = "1E5AA8", "C05A00", "1A1A1A"
SLOTS_VERSION = "slots-v2"
_PARSER = MathTextParser("path")
_OPEN, _CLOSE = "([{", ")]}"


def _slot_colors(glyphs, pt, scale=1.0):
    """One colour per glyph. A glyph is EXPONENT-level when the renderer set it below the run
    size; grown delimiters (STIXSize*) are structural and never count as exponents. `scale` is
    the parse resolution over 72 (positions arrive in pixels at that resolution)."""
    n = len(glyphs)
    col = [SLOT_INK] * n
    small = [g[1] < pt * 0.95 and not g[0].family_name.startswith("STIXSize") for g in glyphs]
    for g, sm in zip(glyphs, small):
        if sm and chr(g[2]) in "√∛∜":
            raise RuntimeError("slot colour: a radical set small — a root index is not an exponent; render this one black")
    i = 0
    while i < n:
        if not small[i]:
            i += 1
            continue
        j = i
        while j + 1 < n and small[j + 1]:
            j += 1
        if j + 1 < n and chr(glyphs[j + 1][2]) == "√":
            i = j + 1                                # a root INDEX (the 3 of a cube root) is set small
            continue                                 # before the radical: not an exponent, no slot — INK
        for k in range(i, j + 1):
            col[k] = CB2
        k = i - 1                                    # the base is what sits to its left
        if k >= 0 and not small[k]:
            ch = chr(glyphs[k][2])
            if ch in _CLOSE:                         # a bracketed base: back to its partner
                depth = 0
                while k >= 0:
                    c = chr(glyphs[k][2])
                    if c in _CLOSE:
                        depth += 1
                    elif c in _OPEN:
                        depth -= 1
                        if depth == 0:
                            break
                    k -= 1
                if k >= 0:
                    for t in range(k, i):
                        if not small[t]:
                            col[t] = CB1
            elif ch.isalpha():                       # a variable is one letter: in 3x², 3 is
                col[k] = CB1                         # a coefficient and is NOT raised
            elif ch.isdigit() or ch == ".":          # a number: the whole numeral, digits only,
                t = k                                # walked ON THE PAGE — same baseline, touching
                while t - 1 >= 0 and not small[t - 1] and (chr(glyphs[t - 1][2]).isdigit() or chr(glyphs[t - 1][2]) == ".") \
                        and abs(glyphs[t - 1][4] - glyphs[t][4]) < 0.5 * scale \
                        and 0 < glyphs[t][3] - glyphs[t - 1][3] <= 0.75 * glyphs[t][1] * scale:
                    t -= 1                           # (list order alone would join a numerator's
                                                     # last digit to the denominator's base: 1/5²)
                for u in range(t, k + 1):
                    col[u] = CB1
            else:
                raise RuntimeError(f"slot colour: an exponent sits on '{ch}', which is not a base")
        else:
            raise RuntimeError("slot colour: an exponent with nothing to its left to be its base")
        i = j + 1
    return col


def _render_slots(latex, pt, path):
    """Draw the expression glyph by glyph so each slot carries its own colour. The layout is
    mathtext's own, computed at the SAME resolution _render rasterises at (DPI), so every glyph
    and bar lands where the black render puts it — slotaudit.py --geometry compares the two."""
    r = _PARSER.parse(f"${latex}$", dpi=DPI, prop=FontProperties(size=pt))
    col = _slot_colors(r.glyphs, pt, scale=DPI / 72)
    # VectorParse geometry (matplotlib _mathtext.Output.to_vector), here in pixels: r.height is
    # the WHOLE box, height above the baseline plus depth below it; a glyph's y is its baseline's
    # height above the box baseline; a rect's y is its BOTTOM edge, rising by its own height.
    # (Drawing bars from y downward put every fraction bar one bar-thickness too low, onto the
    # denominators — seen on a phone, 28 Sep. slotaudit.py --geometry now guards it.)
    pad = 24.0
    Wp, Hp = r.width + 2 * pad, r.height + 2 * pad
    fig = plt.figure(figsize=(Wp / DPI, Hp / DPI), dpi=DPI)
    fig.patch.set_alpha(0)
    base = r.depth + pad
    for (font, size, num, ox, oy), c in zip(r.glyphs, col):
        fig.text((ox + pad) / Wp, (base + oy) / Hp, chr(num), color="#" + c,
                 fontproperties=FontProperties(fname=font.fname, size=size),
                 va="baseline", ha="left")
    for (rx, ry, rw, rh) in r.rects:                 # fraction bars and radical rules: structure
        # fill only: a Rectangle's default 1 pt edge stroke would thicken every bar by 1 pt
        fig.add_artist(Rectangle(((rx + pad) / Wp, (base + ry) / Hp), rw / Wp, rh / Hp,
                                 facecolor="#" + SLOT_INK, edgecolor="none", linewidth=0,
                                 transform=fig.transFigure))
    with warnings.catch_warnings():                  # the delimiter fonts carry no 'l'/'p' for the
        warnings.simplefilter("ignore")              # baseline probe; the drawn glyphs are right
        fig.savefig(path, dpi=DPI, transparent=True)
    plt.close(fig)
    im = Image.open(path)
    box = im.split()[-1].getbbox()
    if box is None:
        raise RuntimeError("blank render: " + latex)
    W, H = im.size
    if box[0] <= 1 or box[2] >= W - 1 or box[1] <= 1 or box[3] >= H - 1:
        raise RuntimeError("expression touched the canvas edge: " + latex)
    im = im.crop(box)
    im.save(path)
    return im.size



def _load():
    if os.path.exists(INDEX):
        with open(INDEX) as f:
            return json.load(f)
    return {}


def _save(idx):
    os.makedirs(FIGS, exist_ok=True)
    tmp = INDEX + ".tmp"
    with open(tmp, "w") as f:
        json.dump(idx, f, indent=0, sort_keys=True)
    os.replace(tmp, INDEX)


def _render(latex, pt, path, color):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig = plt.figure(figsize=(6, 2), dpi=DPI)
    fig.patch.set_alpha(0)
    t = fig.text(0.02, 0.5, f"${latex}$", fontsize=pt, color=color, va="center", ha="left")
    fig.canvas.draw()
    bb = t.get_window_extent()
    need_w = bb.width / DPI + 0.3
    need_h = bb.height / DPI + 0.3
    if need_w > 6 or need_h > 2:
        plt.close(fig)
        fig = plt.figure(figsize=(max(6, need_w), max(2, need_h)), dpi=DPI)
        fig.patch.set_alpha(0)
        t = fig.text(0.02, 0.5, f"${latex}$", fontsize=pt, color=color, va="center", ha="left")
        fig.canvas.draw()
        bb = t.get_window_extent()
    fig.savefig(path, dpi=DPI, transparent=True)
    plt.close(fig)
    im = Image.open(path)
    alpha = im.split()[-1]
    box = alpha.getbbox()
    if box is None:
        raise RuntimeError("blank render: " + latex)
    # measured width must fit inside the canvas with margin (trap 21: measure, do not infer)
    W, H = im.size
    if box[0] <= 1 or box[2] >= W - 1 or box[1] <= 1 or box[3] >= H - 1:
        raise RuntimeError("expression touched the canvas edge: " + latex)
    im = im.crop(box)
    im.save(path)
    return im.size


def m(latex, surface="doc", color="1A1A1A", slots=False):
    """Return (path, width_in, height_in) for a rendered expression.

    slots=True paints the base and the exponent in the slot colours (HOUSE STYLE §2a). It is
    honoured on the slide surfaces only: a printed page is black and white on a copier."""
    pt = SIZES[surface]
    if surface.startswith("slide"):
        # projected fractions are set display-size; text-style \frac reads small from the back row
        latex = re.sub(r"\\frac(?![A-Za-z])", r"\\dfrac", latex)
    else:
        slots = False
    # the slot renderer's version is part of the fingerprint: a render from an older drawing rule
    # can never be served again (v1 drew fraction bars one thickness low — removed 28 Sep)
    key = hashlib.sha1(f"{latex}|{pt}|{SLOTS_VERSION if slots else color}".encode()).hexdigest()[:16]
    idx = _load()
    path = os.path.join(FIGS, key + ".png")
    if key in idx and os.path.exists(path):
        e = idx[key]
        return path, e["w"], e["h"]
    w, h = _render_slots(latex, pt, path) if slots else _render(latex, pt, path, "#" + color)
    idx = _load()  # reload: another writer may have added entries
    idx[key] = {"latex": latex, "pt": pt, "color": SLOTS_VERSION if slots else color,
                "w": w / DPI, "h": h / DPI}
    _save(idx)
    return path, w / DPI, h / DPI


def check_index():
    """figstale: every indexed figure exists and its stored size matches the file."""
    idx = _load()
    bad = 0
    for k, e in idx.items():
        p = os.path.join(FIGS, k + ".png")
        if not os.path.exists(p):
            print("MISSING", k, e["latex"]); bad += 1; continue
        w, h = Image.open(p).size
        if abs(w / DPI - e["w"]) > 1e-6 or abs(h / DPI - e["h"]) > 1e-6:
            print("SIZE DRIFT", k, e["latex"]); bad += 1
    print(f"figs: {len(idx)} indexed, {bad} bad")
    return bad == 0


if __name__ == "__main__":
    import sys
    sys.exit(0 if check_index() else 1)
