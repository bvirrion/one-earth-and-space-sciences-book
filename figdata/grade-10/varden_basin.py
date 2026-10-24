"""The drainage basin of the Varden river on the map of the Varden Hills
(grade 10, drainage-basins).

The topography is figdata/shared/region.py's topo(x, y), imported and never
edited. On a 50 m grid:
  1. the closed hollows are filled by a priority flood from the map edges (each
     filled cell is raised a hair, EPS, above the cell it was reached from, so
     that every cell has a lower neighbour and water can always move on);
  2. each cell sends its water to the neighbour of steepest descent among its
     eight neighbours (the "D8" rule; a diagonal step is sqrt(2) cells long);
  3. a cell belongs to the basin if the path of its water reaches the river's
     flat floor (|y - river_y(x)| <= FLOOR_HALF) before leaving the map; the
     floor carries the water east, to the outlet where the river leaves the map.
The river also brings water from upstream, west of the map: the basin computed
here is the part of its basin that lies on the map.

  part fill     x_km y_km              basin outline (closed rings; map edges included)
  part divide   x_km y_km              the drainage divides (open lines, empty-row jumps)
  part path1-4  x_km y_km              four raindrop paths: to the river floor, or off the map
  part numbers  key value
"""
import heapq
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import region  # noqa: E402

STEP = 50.0
EPS = 1e-3
NBRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
DROPS = ((2000.0, 7400.0), (4000.0, 1800.0), (8600.0, 6600.0), (2500.0, 700.0))


def grid(step=STEP):
    xs = np.arange(0.0, region.WIDTH + step / 2, step)
    ys = np.arange(0.0, region.HEIGHT + step / 2, step)
    z = np.array([[region.topo(x, y) for x in xs] for y in ys])
    return xs, ys, z


def priority_flood(z):
    """Filled surface: closed hollows raised to their spill level (plus EPS steps)."""
    ny, nx = z.shape
    filled = z.copy()
    done = np.zeros(z.shape, dtype=bool)
    heap = []
    for j in range(ny):
        for i in range(nx):
            if j in (0, ny - 1) or i in (0, nx - 1):
                heapq.heappush(heap, (filled[j, i], j, i))
                done[j, i] = True
    while heap:
        h, j, i = heapq.heappop(heap)
        for dj, di in NBRS:
            jj, ii = j + dj, i + di
            if 0 <= jj < ny and 0 <= ii < nx and not done[jj, ii]:
                filled[jj, ii] = max(z[jj, ii], h + EPS)
                done[jj, ii] = True
                heapq.heappush(heap, (filled[jj, ii], jj, ii))
    return filled


def d8(filled):
    """Receiver of each cell, (j, i), or None where the water leaves the map: an edge
    cell with no lower neighbour on the map (an inner cell always has one)."""
    ny, nx = filled.shape
    rec = {}
    for j in range(ny):
        for i in range(nx):
            best, arg = 0.0, None
            for dj, di in NBRS:
                jj, ii = j + dj, i + di
                if 0 <= jj < ny and 0 <= ii < nx:
                    s = (filled[j, i] - filled[jj, ii]) / math.hypot(dj, di)
                    if s > best:
                        best, arg = s, (jj, ii)
            assert arg is not None or j in (0, ny - 1) or i in (0, nx - 1)
            rec[(j, i)] = arg
    return rec


def on_floor(xs, ys, j, i):
    return abs(ys[j] - region.river_y(xs[i])) <= region.FLOOR_HALF


def path(rec, start):
    out = [start]
    while rec[out[-1]] is not None:
        out.append(rec[out[-1]])
        assert len(out) < 100000
    return out


def basin(xs, ys, rec):
    """Boolean grid: the cell's water reaches the river floor before leaving the map."""
    ny, nx = len(ys), len(xs)
    known = {}
    for j in range(ny):
        for i in range(nx):
            trail, c = [], (j, i)
            while c is not None and c not in known and not on_floor(xs, ys, *c):
                trail.append(c)
                c = rec[c]
            hit = True if c is not None and (c not in known) else (known[c] if c is not None else False)
            if c is not None and c not in known:
                known[c] = True                     # a floor cell
            for t in trail:
                known[t] = hit
    mask = np.zeros((ny, nx), dtype=bool)
    for (j, i), v in known.items():
        mask[j, i] = v
    return mask


def outlet_cells(xs, ys):
    i = len(xs) - 1
    return {(j, i) for j in range(len(ys)) if on_floor(xs, ys, j, i)}


def compute():
    xs, ys, z = grid()
    filled = priority_flood(z)
    rec = d8(filled)
    mask = basin(xs, ys, rec)
    return xs, ys, z, filled, rec, mask


def cell_index(xs, ys, x, y):
    return int(round(y / (ys[1] - ys[0]))), int(round(x / (xs[1] - xs[0])))


def numbers(xs, ys, z, filled, mask):
    area_cell = (STEP / 1000.0) ** 2
    # each grid node stands for one cell of STEP x STEP; edge nodes for half a cell
    w = np.ones(z.shape)
    w[0, :] *= 0.5
    w[-1, :] *= 0.5
    w[:, 0] *= 0.5
    w[:, -1] *= 0.5
    n = {"map_km2": float(w.sum() * area_cell),
         "basin_km2": float((w * mask).sum() * area_cell)}
    n["basin_share"] = n["basin_km2"] / n["map_km2"]
    n["filled_cells"] = int((filled - z > 0.01).sum())
    n["max_fill_m"] = float((filled - z).max())
    zb = np.where(mask, z, -1.0)
    n["basin_highest_m"] = float(zb.max())
    n["outlet_z_m"] = region.river_z(region.WIDTH)
    n["inlet_z_m"] = region.river_z(0.0)
    n["river_drop_m"] = n["inlet_z_m"] - n["outlet_z_m"]
    xr = np.arange(0.0, region.WIDTH + 1, 10.0)
    yr = [region.river_y(x) for x in xr]
    n["river_length_km"] = sum(math.hypot(xr[k + 1] - xr[k], yr[k + 1] - yr[k])
                               for k in range(len(xr) - 1)) / 1000.0
    n["map_highest_m"] = float(z.max())
    return n


if __name__ == "__main__":
    xs, ys, z, filled, rec, mask = compute()
    km = lambda pts: [(round(x / 1000, 3), round(y / 1000, 3)) for x, y in pts]  # noqa: E731
    # filled outline: pad with "outside" so that rings close along the map edges
    pad_x = np.concatenate(([xs[0] - STEP], xs, [xs[-1] + STEP]))
    pad_y = np.concatenate(([ys[0] - STEP], ys, [ys[-1] + STEP]))
    ind = np.zeros((len(ys) + 2, len(xs) + 2))
    ind[1:-1, 1:-1] = mask
    rings = region.trace(ind, pad_x, pad_y, 0.5)
    rings = [[(min(max(x, xs[0]), xs[-1]), min(max(y, ys[0]), ys[-1])) for x, y in r] for r in rings]
    rows = []
    for r in rings:
        if len(r) > 3:
            rows += ([()] if rows else []) + km(region.simplify(r, 30.0))
    write_table(__file__, ("x_km", "y_km"), rows, part="fill")
    # divides: the outline traced without padding stops at the map edges
    rows = []
    for line in region.trace(mask.astype(float), xs, ys, 0.5):
        if len(line) > 3:
            rows += ([()] if rows else []) + km(region.simplify(line, 30.0))
    write_table(__file__, ("x_km", "y_km"), rows, part="divide")
    for n, (x0, y0) in enumerate(DROPS, start=1):
        p = path(rec, cell_index(xs, ys, x0, y0))
        k = next((k for k, (j, i) in enumerate(p) if on_floor(xs, ys, j, i)), len(p) - 1)
        write_table(__file__, ("x_km", "y_km"), km([(xs[i], ys[j]) for j, i in p[:k + 1]]),
                    part="path%d" % n)
    write_table(__file__, ("key", "value"), sorted(numbers(xs, ys, z, filled, mask).items()),
                part="numbers")
