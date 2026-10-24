"""The Preliminary Reference Earth Model against depth (grade 11, seismic-structure;
reused in lithosphere-asthenosphere).

Source (ledger data:prem): Dziewonski and Anderson (1981), isotropic tabulation,
data/derived/prem.csv (depth_km, vp, vs, rho; a discontinuity appears as two rows at
the same depth).

  part profile   depth vp vs rho           every node, for the whole-Earth plot
  part upper     depth vs                  0-400 km, S speed (lithosphere chapter)
  part numbers   key value
"""
import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EARTH_RADIUS_KM = 6371.0


def prem():
    with open(os.path.join(ROOT, "data", "derived", "prem.csv"), encoding="utf8") as f:
        return [(float(r["depth_km"]), float(r["vp_km_s"]), float(r["vs_km_s"]), float(r["rho_g_cm3"]),
                 r["region"]) for r in csv.DictReader(f)]


def discontinuities(rows=None, jump=0.05):
    """Depths where a node is repeated with a different P speed."""
    rows = rows or prem()
    out = []
    for a, b in zip(rows[:-1], rows[1:]):
        if a[0] == b[0] and abs(a[1] - b[1]) > jump:
            out.append((a[0], a[4], b[4], a[1], b[1], a[2], b[2]))
    return out


def boundary(region_above, region_below, rows=None):
    for x in discontinuities(rows):
        if x[1] == region_above and x[2] == region_below:
            return x[0]
    return None


def value_at(depth, col, rows=None, below=True):
    """Linear interpolation of column col (1 vp, 2 vs, 3 rho) at depth; at a
    discontinuity, the value just below (below=True) or just above."""
    rows = rows or prem()
    for a, b in zip(rows[:-1], rows[1:]):
        if a[0] == b[0] == depth:
            return b[col] if below else a[col]
    for a, b in zip(rows[:-1], rows[1:]):
        if a[0] <= depth <= b[0] and b[0] > a[0]:
            return a[col] + (b[col] - a[col]) * (depth - a[0]) / (b[0] - a[0])
    raise ValueError(depth)


def mean_density(rows=None):
    """Mean density of the model (g/cm3): mass / volume, integrating 4 pi r^2 rho dr."""
    rows = rows or prem()
    m = 0.0
    for a, b in zip(rows[:-1], rows[1:]):
        if b[0] > a[0]:
            r1, r2 = EARTH_RADIUS_KM - b[0], EARTH_RADIUS_KM - a[0]
            n = 50
            for k in range(n):
                ra = r1 + (r2 - r1) * (k + 0.5) / n
                rho = b[3] + (a[3] - b[3]) * (ra - r1) / (r2 - r1)
                m += rho * ra * ra * (r2 - r1) / n
    return m * 3.0 / EARTH_RADIUS_KM ** 3


def numbers():
    rows = prem()
    return {"moho_km": boundary("crust", "mantle", rows),
            "cmb_km": boundary("mantle", "outer-core", rows),
            "icb_km": boundary("outer-core", "inner-core", rows),
            "vp_above_cmb": value_at(2891.0, 1, rows, below=False),
            "vp_below_cmb": value_at(2891.0, 1, rows),
            "vs_outer_core_max": max(r[2] for r in rows if r[4] == "outer-core"),
            "vp_surface": rows[0][1], "vs_surface": rows[0][2],
            "vp_upper_mantle": value_at(24.4, 1, rows), "vs_upper_mantle": value_at(24.4, 2, rows),
            "rho_crust": rows[0][3], "rho_centre": rows[-1][3],
            "mean_density": mean_density(rows),
            "core_radius_km": EARTH_RADIUS_KM - boundary("mantle", "outer-core", rows),
            "inner_core_radius_km": EARTH_RADIUS_KM - boundary("outer-core", "inner-core", rows)}


if __name__ == "__main__":
    rows = prem()
    write_table(__file__, ("depth", "vp", "vs", "rho"), [r[:4] for r in rows], part="profile")
    write_table(__file__, ("depth", "vs"), [(r[0], r[2]) for r in rows if r[0] <= 400.0], part="upper")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")
