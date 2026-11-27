# figs10 — how to call Unit 10's figures (read this, not the source)

**Load it** at the top of a spec (its own name, so no other unit's `figs` is handed to you):
```python
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import figs10 as figs; S = figs.slide      # S(spec, inches=, pt=, reserve=): the figure sized for a slide
```
**Placing it.** Slide: `S(figs.plane(..., inches=4.2, pt=18), inches=4.2, pt=18, reserve=0.75)` in a board's `fig`/`fig_a`,
a worked entry's `fig`, a Your Turn's, a notes slide (`plane` gets the same `inches`/`pt` as `S`). Paper: bare, print
size, `figs.plane(..., inches=3.2)` (pt 9.5), `fig_key` for the key. Question slides: pt >= 18, a graph >= 2.6 in tall
(a row of four: 2.2 in). Then run `figure_sheets.py u10` and look.

## Functions (figs7's, plus what Unit 10 added: marked NEW)
- `plane(xr, yr, lines=(), points=(), xs=1, ys=1, xname="x", yname="y", step=None, xstep=None, ystep=None, inches=3.0, pt=9.5, label=True, solution=None, curves=(), letters=None, aspect=1, triangles=(), first=False, key=None)`
  — edges on grid lines; at most 4 lines (solid blue, dashed orange, solid green, dashed purple). A line is `(m, b)`,
  `(m, b, text)`, `(m, b, text, (x, where))`, or NEW `(m, b, text, at, (x_from, x_to))`: drawn only on that stretch.
  text None = its equation (in `letters=("n", "c")` → c = 20n + 35), "" = none, "A" = a letter. Points `(x, y)` → dot +
  "(x, y)"; `(x, y, "on")` the same, REFUSED unless on a line; `(x, y, "")` bare dot; `(x, y, name, where)`, where =
  ur/ul/dl/dr/r/l/u/d (+ / ++ farther). NEW: an unplaced point name goes to the first corner no line, dot or label runs
  through. NEW `first=True`: every equation with b first. NEW `key`: "above" sets the equations over the plane's
  top-right corner, one row each, in the lines' colours (DEFAULT on a four-quadrant plane); "edge" = by the right/top
  edge (default in Quadrant I). `aspect=0.6` makes cells shorter than wide (a tall window: 0 to 400 by 50).
- NEW `tri(p, q, run=None, rise=None, side="under", run_at=None, rise_at=None)` for `triangles=[...]` (at most 2; first
  red, second brown, never a line's colour): the right triangle between lattice points p and q of one line, with its
  right-angle mark. None = the side's length; a string prints itself ("?", "run 2"); "" none. `*_at` "out"/"in". A
  second triangle whose run lies along the first's (nested from one corner) puts its run number INSIDE by itself.
- NEW `eq(m, b, y="y", x="x", first=False, frac="paren")` — y = −(2/3)x + 5 for `Fr(-2, 3)`; y = 1.5x for the float
  1.5 (a float prints as a decimal, a Fraction as (n/d)); y = 5 − (3/2)x with first; y = 4; c = 1.75t + 9.50 with b
  "9.50" as a string. `frac="glyph"` = figs7's ⅔. Numbers 1,000 and up print with the comma (3,000), ticks too.
- As figs7: `prop(p, text=None, at=None)`, `square(a, x1)`, `pair(xr, yr, lines=, points=, **plane-args)` → `(empty,
  drawn)`, `table(rows, head=, cw=1.25, rh=1.0, titles=, hw=)` (`figs.BLANK` = ▢), `row(specs, gap=3.0, titles=,
  captions=, inches=6.0, pt=9.5)`, `choices4(specs, letters="ABCD", gap=2.2, inches=14.0, pt=18)`, `match_grid`.

## One call for each kind
```python
# 1. slope triangles: one after another (10.02+03 Notes II), and nested from one corner, at print size
N2 = S(figs.plane((0, 8), (0, 6), lines=[(Fr(1, 2), 1, "")], points=[(0, 1, ""), (2, 2, ""), (6, 4, "")],
                  triangles=[figs.tri((0, 1), (2, 2)), figs.tri((2, 2), (6, 4))], inches=4.2, pt=18), inches=4.2, pt=18, reserve=0.75)
NEST = figs.plane((0, 10), (0, 6), lines=[(Fr(1, 2), 1, "")], points=[(0, 1, "")],
                  triangles=[figs.tri((0, 1), (2, 2)), figs.tri((0, 1), (8, 5), rise="?")], inches=3.2)
#    (start a triangle above the x-axis, or its numbers land on the axis numbers; a nested triangle exactly twice as
#    wide as the first puts its number on the first one's side — both are refused)
#    words on a side: triangles=[figs.tri((0, 1), (2, 5), "run 2", "rise 4")] on plane((0, 5), (0, 7)) with (0, 1, "")
# 2. scatter plot with its line of fit: bare dots, named axes, the equation in the story's letters
DOTS = [(1, 66), (2, 65), (2, 72), (3, 74), (4, 74), (5, 82), (5, 78), (6, 86), (7, 86), (7, 90), (8, 91), (9, 95)]
SC = S(figs.plane((0, 10), (0, 110), ys=10, ystep=2, xname="hours of practice", yname="test score", lines=[(4, 60)],
                  letters=("h", "s"), points=[(a, b, "") for a, b in DOTS], inches=4.2, pt=18), inches=4.2, pt=18, reserve=0.75)
# 3. four quadrants, equations keyed above (default); b first; a horizontal line; a context's letters
G3 = S(figs.plane((-6, 6), (-6, 6), lines=[(Fr(-3, 2), 5), (0, 4)], first=True,
                  points=[(0, 5, "on"), (2, 2, "on"), (4, -1, "on")], inches=4.2, pt=18), inches=4.2, pt=18, reserve=0.75)
G3C = S(figs.plane((0, 6), (0, 160), ys=20, xname="months", yname="cost ($)", lines=[(20, 35)], letters=("n", "c"),
                   points=[(0, 35, "on"), (3, 95, "on")], inches=4.2, pt=18), inches=4.2, pt=18, reserve=0.75)
# 4. Quadrant I off the origin: rising from (0, 150) (tall window: aspect); falling to (8, 0); big numbers
G4 = S(figs.plane((0, 5), (0, 400), ys=50, ystep=2, aspect=0.6, xname="hours", yname="miles", lines=[(50, 150, "")],
                  points=[(0, 150, "on"), (4, 350, "on")], inches=4.2, pt=18), inches=4.2, pt=18, reserve=0.75)
G4F = figs.plane((0, 10), (0, 140), ys=20, xname="days", yname="pages left", lines=[(-15, 120, "")],
                 points=[(0, 120, "on"), (8, 0, "on")], inches=3.2)        # clipped at the x-axis: it stops at (8, 0)
# 5. the handout's empty grid and the key's (item: fig=GRID, fig_key=KEY); a line that stops where the story ends
GRID, KEY = figs.pair((-6, 6), (-6, 6), lines=[(Fr(-1, 2), 3, "")], points=[(0, 3, ""), (4, 1, "")], inches=3.2)
GRIDQ1, KEYQ1 = figs.pair((0, 8), (0, 12), lines=[(-2, 12, "", None, (0, 6))], points=[(0, 12, ""), (6, 0, "")],
                          xname="minutes", yname="liters left", inches=3.2)
# 6. four lettered graphs (options "A".."D"): Quadrant I kinds, and four lines on a −4 to 6 window
g = dict(inches=2.6, pt=18, ystep=3); C4 = S(figs.choices4([figs.plane((0, 7), (0, 10), points=[(1, 3, ""), (2, 6, ""), (3, 9, "")], **g),
                      figs.plane((0, 7), (0, 10), lines=[(1, 3, "")], **g),
                      figs.plane((0, 7), (0, 10), curves=[figs.square(1, 3)], **g),
                      figs.plane((0, 7), (0, 10), points=[(2, 5, ""), (4, 6, ""), (6, 7, "")], **g)]), inches=14.0, pt=18, reserve=0.75)
g2 = dict(inches=2.6, pt=18, step=2)
C4B = S(figs.choices4([figs.plane((-4, 6), (-4, 6), lines=[(m, b, "")], **g2) for m, b in ((2, -3), (-3, 2), (Fr(1, 2), -3), (2, 3))],
                      gap=3.2), inches=14.0, pt=18, reserve=0.75)
# 7. a table beside its graph (a notes slide); cw/rh roomier than the default so 18 pt fits the cells
T7 = S(figs.row([figs.table([([-3, 0, 3, 6], [4, 2, figs.BLANK, -2])], head=("x", "y"), cw=2.0, rh=1.5),
                 figs.plane((-4, 7), (-4, 6), lines=[(Fr(-2, 3), 2)], points=[(-3, 4, ""), (0, 2, ""), (3, 0, ""), (6, -2, "")])],
                gap=2.5), inches=9.0, pt=18, reserve=0.75)
```

**Refusals** (fix the call): a point "on" no line; a `solution` off a line; an edge off a grid line; two edge labels
under a cell apart; a stretch outside the plane; over 4 lines or 2 triangles; a triangle corner off the lattice, two
corners not on one line or sharing an x or y; and the kit's own — a line through a label, labels on each other.
**Does not fit:** words on a one-cell side ("rise 1" on Notes II's 2-by-1 triangle hits "run 4") — print numbers, say
"rise"/"run" in the words (sides of 3+ cells take words). `key="edge"` on four quadrants shrinks the plane to ~2.4 in.
**The paper's numbers are the paper's:** the plan's "Reserved for the paper" lists what no lesson draws. A figure's
lettering is Lexend in every built page; build, then look — a label that clears a line in one face can touch it in another.
