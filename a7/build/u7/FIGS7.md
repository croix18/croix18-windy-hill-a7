# figs7 — how to call Unit 7's figures (read this, not the source)

**Load it** at the top of a spec, as Unit 11 does (its own name, so no other unit's `figs` is handed to you):
```python
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs7 as figs
S = figs.slide            # S(spec, inches=, pt=, reserve=): the same figure sized for a slide
```
**Placing it.** A slide figure is `S(figs.plane(..., inches=4.2, pt=18), inches=4.2, pt=18, reserve=0.75)` and goes in
a board's `fig`/`fig_a`, a worked entry's `fig`, a Your Turn's `fig`/`fig_a`, a notes slide. Give `plane` the same
`inches` and `pt` as `S` so it thins its numbers for that size. A paper (Independent Set, test, keys) uses the figure
bare, print size: `figs.plane(..., inches=3.2)` (pt 9.5), with `fig_key` for the key's drawn version. Labels stay at
`pt` whatever size the deck draws the figure; on a question slide keep pt >= 18 and a graph >= 2.6 in tall
(a 4.2-in plane of 6 to 10 cells a side stands 3.9 to 4.2 in).

## Functions
- `plane(xr, yr, lines=(), points=(), xs=1, ys=1, xname="x", yname="y", step=None, xstep=None, ystep=None, inches=3.0, pt=9.5, label=True, solution=None, curves=(), letters=None)`
  — xr, yr in the story's numbers, edges on grid lines; `xs`/`ys` each axis's own scale (1, 2, 4, 5, 10, 20);
  long `xname`/`yname` go under the plane and over its top-left corner. At most 4 lines: solid blue, dashed orange,
  solid green, dashed purple. A line is `(m, b)`, `(m, b, text)`, `(m, b, text, (x, where))`; text default its
  equation (in `letters=("p", "c")` → c = 2.5p), "" none, "A" a letter. Points `(x, y)` → dot + "(x, y)";
  `(x, y, "on")` the same but REFUSED unless on a line; `(x, y, "")` bare dot; `(x, y, name, where)` where = ur/ul/dl/dr/r/l/u/d.
  `aspect=0.65` draws each grid cell 0.65 as tall as it is wide (default 1, square) — for a row of four graphs that must
  each be 2 in wide in a short row (7.01 board 6); give a window one square past the last number you want printed
  (x to 9, numbered to 8) so one graph's last number does not stand beside the next graph's 0.
- `prop(p, text=None, at=None)` — the line y = px for `lines=`. `square(a, x1)` — points of y = a·x² for `curves=`.
- `pair(xr, yr, lines=, points=, **plane-args)` → `(empty, drawn)`: the student's grid and the key's, one window.
- `table(rows, head=("x","y"), cw=1.25, rh=1.0, titles=None, hw=None, inches=None)` — rows = [(xs, ys), …];
  `figs.BLANK` ("▢") draws an empty box; money as strings ("6.40").
- `row(specs, gap=3.0, titles=None, captions=None, inches=6.0, pt=9.5)` — figures side by side, one picture.
- `choices4(specs, letters="ABCD", inches=14.0, pt=18)` — four small planes lettered over each, for "which graph?".
- `eq(m, b, y="y", x="x")` — the printed equation (y = 0.4x, y = (2/7)x, y = −1.5x, y = ½x). `match_grid` as Unit 11.

## One call for each kind
```python
# 1. first quadrant, named and scaled axes: a line through the origin, two points on it
G1 = S(figs.plane((0, 6), (0, 24), lines=[figs.prop(4, "")], ys=4, xname="pounds of grapes", yname="cost in dollars",
                  points=[(1, 4, "on"), (3, 12, "on")], inches=4.2, pt=18), inches=4.2, pt=18, reserve=0.75)
#    points only (no line): points=[(2, 30), (4, 60), (6, 90)], xs=1, ys=10
#    the contrast (not proportional), two lines lettered:
G1B = S(figs.plane((0, 5), (0, 12), lines=[figs.prop(2, "A"), (2, 2, "B")], ys=2, inches=4.2, pt=18), inches=4.2, pt=18)
#    four lines on one grid:
G1C = S(figs.plane((0, 8), (0, 8), lines=[figs.prop(4, "A"), figs.prop(2, "B"), figs.prop(1, "C"), figs.prop(Fr(1, 4), "D")],
                   xname="seconds", yname="meters", inches=4.2, pt=18), inches=4.2, pt=18, reserve=0.75)
# 2. four quadrants, a negative constant
G2 = S(figs.plane((-4, 4), (-8, 8), lines=[figs.prop(Fr(-3, 2))], ys=2, points=[(2, -3, "on")], inches=4.2, pt=18),
       inches=4.2, pt=18, reserve=0.75)
# 3. ratio table with blanks
T3 = S(figs.table([([0, 2, 4, 6], [0, figs.BLANK, 30, figs.BLANK])], head=("hours", "pay ($)")), inches=6.0, pt=24)
# 4. four lettered graphs for a choice board (options are then "A" … "D")
g = dict(xname="tickets", yname="cost ($)", inches=2.6, pt=18)
C4 = S(figs.choices4([figs.plane((0, 4), (0, 24), lines=[figs.prop(6, "")], ys=6, **g),
                      figs.plane((0, 4), (0, 24), lines=[(6, 6, "")], ys=6, **g),
                      figs.plane((0, 24), (0, 4), lines=[figs.prop(Fr(1, 6), "")], xs=6, xname="cost ($)", yname="tickets", inches=2.6, pt=18),
                      figs.plane((0, 4), (0, 12), lines=[figs.prop(3, "")], ys=3, **g)]), inches=14.0, pt=18, reserve=0.75)
# 5. the handout's empty grid, and the key's (item: fig=GRID5, fig_key=KEY5)
GRID5, KEY5 = figs.pair((0, 4), (0, 20), lines=[figs.prop(5, "")], points=[(1, 5, ""), (2, 10, ""), (3, 15, "")],
                        ys=5, xname="minutes", yname="boxes filled", inches=3.2)
# 6. three small pictures for one notes slide
P6 = S(figs.row([figs.plane((0, 4), (0, 8), lines=[figs.prop(2, "")]),
                 figs.plane((0, 4), (0, 8), lines=[(1, 2, "")]),
                 figs.plane((0, 4), (0, 8), curves=[figs.square(Fr(1, 2), 4)])],
                captions=["proportional", "not: from (0, 2)", "not: a curve"]), inches=11.0, pt=18, reserve=0.5)
```
**Refusals** (fix the call, not the module): a point "on" no line; a `solution` off a line; a window edge off a grid
line; two line labels leaving one edge less than a cell apart (use `(x, where)`); and the kit's own — any line
through a label, labels on each other. Every number on the picture must be one the words give (ruling 44).
