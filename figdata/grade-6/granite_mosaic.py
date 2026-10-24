"""Granite as a mosaic of three minerals: a drawn enlargement (grade 6).

Not a photograph stand-in: a schematic, built as a Voronoi mosaic of grains
(fixed seed) in a W x H box, each grain given one of the three main minerals
of granite (ledger nps:granite-minerals): feldspar, quartz, mica. The counts
are exercise data (an invented sample), not a measured granite.

  part feldspar, quartz, mica : x y  closed grain polygons (blank line between)
  main table                  : mineral n_grains area_share_percent
"""
import os
import sys

import numpy as np
from scipy.spatial import Voronoi

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

W, H, N, SEED = 6.0, 4.0, 60, 7
MINERALS = ("feldspar", "quartz", "mica")
SHARES = (0.55, 0.35, 0.10)          # target proportions of grains


def grains():
    rng = np.random.default_rng(SEED)
    pts = rng.uniform((0.15, 0.15), (W - 0.15, H - 0.15), size=(N, 2))
    mirrored = np.vstack([pts, pts * (-1, 1), pts * (1, -1),
                          (2 * W - pts[:, 0])[:, None] * (1, 0) + pts * (0, 1),
                          pts * (1, 0) + (2 * H - pts[:, 1])[:, None] * (0, 1)])
    vor = Voronoi(mirrored)
    polys = []
    for i in range(N):
        reg = vor.regions[vor.point_region[i]]
        assert -1 not in reg and reg
        v = vor.vertices[reg]
        c = v.mean(axis=0)
        order = np.argsort(np.arctan2(v[:, 1] - c[1], v[:, 0] - c[0]))
        polys.append(np.clip(v[order], 0, (W, H)))
    counts = [round(s * N) for s in SHARES]
    labels = np.array(sum(([m] * k for m, k in zip(MINERALS, counts)), []))
    rng.shuffle(labels)
    return polys, list(labels)


def area(p):
    x, y = p[:, 0], p[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))


def summary():
    polys, lab = grains()
    tot = sum(area(p) for p in polys)
    out = []
    for m in MINERALS:
        out.append((m, lab.count(m), 100.0 * sum(area(p) for p, l in zip(polys, lab) if l == m) / tot))
    return out, tot


if __name__ == "__main__":
    polys, lab = grains()
    for m in MINERALS:
        rows = []
        for p, l in zip(polys, lab):
            if l == m:
                rows += ([()] if rows else []) + [(round(x, 4), round(y, 4)) for x, y in p] + \
                        [(round(p[0][0], 4), round(p[0][1], 4))]
        write_table(__file__, ("x", "y"), rows, part=m)
    s, tot = summary()
    write_table(__file__, ("mineral", "n_grains", "area_share_percent"), [(m, n, round(a, 1)) for m, n, a in s])
    print(s, tot)
