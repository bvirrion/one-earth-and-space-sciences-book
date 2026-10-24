"""A synthetic travel-time tomography: the checkerboard test (Year 3,
seismology-imaging). Everything here is synthetic.

A box 800 km wide and 400 km deep, background velocity V0 = 8 km/s, is cut
into NX x NY = 16 x 8 square cells of 50 km. Sources (earthquakes) sit on the
bottom edge, 20 of them, receivers (stations) on the top edge, 32 of them;
every pair whose ray is within 45 degrees of the vertical is a straight ray (velocity contrasts are small: the linearised problem). G[i, j]
is the length of ray i in cell j (rays sampled at 4000 points). The true model is
a checkerboard of slowness anomalies of +-3 % in blocks of 2 x 2 cells; the data
are d = G m_true + noise (Gaussian, sigma = 0.05 s, seed 5). The damped
least-squares estimate is
    m(eps) = (G^T G + eps^2 I)^-1 G^T d,
its misfit |G m - d| and its norm |m| trace the trade-off curve, and its
resolution matrix is R(eps) = (G^T G + eps^2 I)^-1 G^T G.

  part true, rec-low, rec-high   x y dv     cell centres (km) and velocity
                                            anomaly dv/v = -ds/s (per cent):
                                            truth, recovered with EPS_LOW and EPS_HIGH
  part hits      x y n           rays crossing each cell
  part tradeoff  eps misfit norm  eps in km (G in km); misfit |G m - d| in s;
                                 norm |m| / S0 in per cent (norm of dv/v)
  part rays      x y             a few of the rays (blank rows as nan)
  part sources, receivers  x y   the 20 sources and 32 receivers
  part values    what value
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

NX, NY, CELL = 16, 8, 50.0
V0 = 8.0
S0 = 1.0 / V0
AMP = 0.03
SIGMA = 0.05
SEED = 5
EPS_LOW, EPS_HIGH = 3.0, 60.0
NSAMP = 4000
MAXTAN = 1.0  # tan(45 deg)


def stations():
    w, h = NX * CELL, NY * CELL
    src = [(w * (k + 0.5) / 20, 0.0) for k in range(20)]
    rec = [(w * (k + 0.5) / 32, h) for k in range(32)]
    return src, rec


def ray_lengths(a, b, nsamp=NSAMP):
    (x1, y1), (x2, y2) = a, b
    length = np.hypot(x2 - x1, y2 - y1)
    t = (np.arange(nsamp) + 0.5) / nsamp
    x, y = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
    ix = np.clip((x // CELL).astype(int), 0, NX - 1)
    iy = np.clip((y // CELL).astype(int), 0, NY - 1)
    row = np.zeros(NX * NY)
    np.add.at(row, iy * NX + ix, length / nsamp)
    return row


def kernel():
    src, rec = stations()
    rays, rows = [], []
    for a in src:
        for b in rec:
            if abs(b[0] - a[0]) > MAXTAN * (b[1] - a[1]):
                continue  # steeper than MAXANGLE from the vertical only
            rays.append((a, b))
            rows.append(ray_lengths(a, b))
    return np.array(rows), rays


def checkerboard():
    m = np.zeros(NX * NY)
    for iy in range(NY):
        for ix in range(NX):
            m[iy * NX + ix] = AMP * S0 * (1 if ((ix // 2) + (iy // 2)) % 2 == 0 else -1)
    return m


def damped(g, d, eps):
    n = g.shape[1]
    return np.linalg.solve(g.T @ g + eps ** 2 * np.eye(n), g.T @ d)


def resolution(g, eps):
    n = g.shape[1]
    gg = g.T @ g
    return np.linalg.solve(gg + eps ** 2 * np.eye(n), gg)


def data(g, m, sigma=SIGMA, seed=SEED):
    rng = np.random.default_rng(seed)
    return g @ m + rng.normal(0.0, sigma, g.shape[0])


def centres():
    return [((ix + 0.5) * CELL, (iy + 0.5) * CELL) for iy in range(NY) for ix in range(NX)]


if __name__ == "__main__":
    g, rays = kernel()
    mt = checkerboard()
    d = data(g, mt)
    cc = centres()

    def grid(m):
        return [(x, y, -100.0 * mi / S0) for (x, y), mi in zip(cc, m)]

    write_table(__file__, ("x", "y", "dv"), grid(mt), part="true")
    write_table(__file__, ("x", "y", "dv"), grid(damped(g, d, EPS_LOW)), part="rec-low")
    write_table(__file__, ("x", "y", "dv"), grid(damped(g, d, EPS_HIGH)), part="rec-high")
    hits = (g > 0).sum(axis=0)
    write_table(__file__, ("x", "y", "n"), [(x, y, int(h)) for (x, y), h in zip(cc, hits)], part="hits")
    trade = []
    for e in np.logspace(-1, 3, 41):
        m = damped(g, d, e)
        trade.append((e, np.linalg.norm(g @ m - d), np.linalg.norm(m) / S0 * 100.0))
    write_table(__file__, ("eps", "misfit", "norm"), trade, part="tradeoff")
    show = [rays[k] for k in range(0, len(rays), 41)]
    rr = []
    for a, b in show:
        rr += [a, b, ("nan", "nan")]
    write_table(__file__, ("x", "y"), rr[:-1], part="rays")
    src, rec = stations()
    write_table(__file__, ("x", "y"), src, part="sources")
    write_table(__file__, ("x", "y"), rec, part="receivers")
    r_low = resolution(g, EPS_LOW)
    r_high = resolution(g, EPS_HIGH)
    vals = [("nrays", len(rays)), ("ncells", NX * NY),
            ("expected_misfit", round(SIGMA * np.sqrt(len(rays)), 3)),
            ("misfit_low", round(np.linalg.norm(g @ damped(g, d, EPS_LOW) - d), 3)),
            ("misfit_high", round(np.linalg.norm(g @ damped(g, d, EPS_HIGH) - d), 3)),
            ("norm_low", round(np.linalg.norm(damped(g, d, EPS_LOW)) / S0 * 100.0, 2)),
            ("norm_high", round(np.linalg.norm(damped(g, d, EPS_HIGH)) / S0 * 100.0, 2)),
            ("norm_true", round(np.linalg.norm(mt) / S0 * 100.0, 2)),
            ("trace_R_low", round(np.trace(r_low), 2)), ("trace_R_high", round(np.trace(r_high), 2))]
    write_table(__file__, ("what", "value"), vals, part="values")
