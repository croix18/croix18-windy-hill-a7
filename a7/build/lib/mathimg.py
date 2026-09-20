"""Expression images. Every fraction, radical or exponent expression that appears on a page is
rendered here from LaTeX (matplotlib mathtext, STIX) at ONE font size per surface, cropped to
its own ink, and recorded in figs/index.json with its natural size. Printed size = natural size,
so every digit in a document is the same size (HOUSE STYLE §8) by construction.

The index is MERGED, never rebuilt (HOUSE STYLE §2: "No generator rebuilds an index. Ever.").
A figure is fingerprinted by its LaTeX + size; editing one character re-renders exactly one file.
"""
import os, json, hashlib, re
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["mathtext.fontset"] = "stix"
matplotlib.rcParams["font.family"] = "STIXGeneral"
import matplotlib.pyplot as plt
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.normpath(os.path.join(HERE, "..", "figs"))
INDEX = os.path.join(FIGS, "index.json")
DPI = 300
# One digit size per surface. Documents: 13 pt (body is 11 pt; larger on purpose, §8).
# Slides: whiteboard display 40 pt, inline 26 pt.
SIZES = {"doc": 13, "docbig": 16, "slide": 26, "slidebig": 40, "slidemid": 32}


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


def m(latex, surface="doc", color="1A1A1A"):
    """Return (path, width_in, height_in) for a rendered expression."""
    pt = SIZES[surface]
    key = hashlib.sha1(f"{latex}|{pt}|{color}".encode()).hexdigest()[:16]
    idx = _load()
    path = os.path.join(FIGS, key + ".png")
    if key in idx and os.path.exists(path):
        e = idx[key]
        return path, e["w"], e["h"]
    w, h = _render(latex, pt, path, "#" + color)
    idx = _load()  # reload: another writer may have added entries
    idx[key] = {"latex": latex, "pt": pt, "color": color, "w": w / DPI, "h": h / DPI}
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
