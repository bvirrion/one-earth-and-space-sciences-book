"""Seismic rays and travel times in a spherically symmetric Earth (Year 3,
seismology-imaging).

Data: data/derived/prem.csv (shared dataset, ledger data:prem): PREM, isotropic,
velocities given at depths, linearly interpolated in between.

Method (the chapter's theorems): the Earth is cut into thin spherical shells of
constant velocity (thickness <= DR km, velocity of the shell's mid-depth). In a
shell of constant velocity v a ray is a straight line; a straight line passes at
the distance d from the centre, and Snell's law between shells keeps
p = r sin(i) / v constant, so that d = p v in every shell. Between the radii
r1 > r2 (both >= d) the ray turns about the centre by
    arccos(d / r1) - arccos(d / r2)
and travels sqrt(r1^2 - d^2) - sqrt(r2^2 - d^2); in the shell where d >= r2 it
turns (bottoms) and the path is mirrored. Summing gives the epicentral distance
Delta(p) and the time T(p); dT/dDelta = p (Benndorf's relation) is a test, not an
input. Exact for the shell model; the shell model converges to the continuous
one as DR -> 0.

  part rays-mantle, rays-core
                 ray x y           P ray paths for the take-off angles RAY_ANGLES,
                                   split by where they bottom (every 20th shell
                                   point kept)
                                   (x, y in km, source at the top; 'ray' numbers
                                   the path; one blank-free table, paths separated
                                   by a row 'nan nan nan')
  part tt        phase delta_deg t_min    travel-time curves (P mantle branch,
                                   PKP and PKIKP, S mantle branch), parametrised
                                   by p; delta folded into 0-180 deg
  part values    what value
"""
import csv
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
PREM = os.path.join(ROOT, "data", "derived", "prem.csv")
R_EARTH = 6371.0
DR = 2.0  # km, maximum shell thickness


def read_prem(path=PREM):
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            rows.append((float(r["depth_km"]), float(r["vp_km_s"]), float(r["vs_km_s"])))
    return rows


def shells(phase="P", dr=DR, rows=None):
    """Arrays (r_top, r_bot, v) from the surface down to the centre."""
    rows = rows if rows is not None else read_prem()
    k = 1 if phase == "P" else 2
    rt, rb, vv = [], [], []
    for (z1, *a), (z2, *b) in zip(rows[:-1], rows[1:]):
        if z2 <= z1:
            continue  # a discontinuity: two values at one depth
        v1, v2 = a[k - 1], b[k - 1]
        n = max(1, int(math.ceil((z2 - z1) / dr)))
        for j in range(n):
            za = z1 + (z2 - z1) * j / n
            zb = z1 + (z2 - z1) * (j + 1) / n
            zm = 0.5 * (za + zb)
            v = v1 + (v2 - v1) * (zm - z1) / (z2 - z1)
            rt.append(R_EARTH - za)
            rb.append(R_EARTH - zb)
            vv.append(v)
    return np.array(rt), np.array(rb), np.array(vv)


def homogeneous_shells(v, n=1000, radius=R_EARTH):
    r = np.linspace(radius, 0.0, n + 1)
    return r[:-1], r[1:], np.full(n, float(v))


def trace(p, sh):
    """Delta (rad), T (s), bottoming radius (km) of the ray of parameter p (s/rad)."""
    rt, rb, v = sh
    d = p * v
    # first shell the ray cannot cross: it bottoms there (d >= r_bot) or cannot
    # enter it at all (d >= r_top, or a liquid layer for S)
    stop = (d >= rb) | (v <= 0.0)
    k = int(np.argmax(stop)) if stop.any() else len(v) - 1
    a = slice(0, k)
    dd = d[a]
    delta = np.sum(np.arccos(dd / rt[a]) - np.arccos(dd / rb[a]))
    t = np.sum((np.sqrt(rt[a] ** 2 - dd ** 2) - np.sqrt(rb[a] ** 2 - dd ** 2)) / v[a])
    bottom = rb[k - 1] if k > 0 else rt[0]
    if v[k] > 0.0 and d[k] < rt[k]:  # the ray enters shell k and bottoms in it
        delta += math.acos(d[k] / rt[k])
        t += math.sqrt(rt[k] ** 2 - d[k] ** 2) / v[k]
        bottom = d[k]
    return 2.0 * delta, 2.0 * t, bottom


def path(p, sh):
    """(x, y) points of the ray of parameter p, source at (0, R)."""
    rt, rb, v = sh
    d = p * v
    th, pts = 0.0, [(rt[0], 0.0)]
    for i in range(len(v)):
        if v[i] <= 0.0 or d[i] >= rt[i]:
            break
        if d[i] >= rb[i]:
            th += math.acos(d[i] / rt[i])
            pts.append((d[i], th))
            break
        th += math.acos(d[i] / rt[i]) - math.acos(d[i] / rb[i])
        pts.append((rb[i], th))
    total = 2.0 * th
    down = [(r, a) for r, a in pts]
    up = [(r, total - a) for r, a in reversed(pts[:-1])]
    return [(r * math.sin(a), r * math.cos(a)) for r, a in down + up]


def take_off_p(angle_deg, sh):
    """Ray parameter of a ray leaving the surface at angle_deg from the vertical."""
    return R_EARTH * math.sin(math.radians(angle_deg)) / sh[2][0]


RAY_ANGLES = (2, 5, 8, 11, 13, 13.4, 14, 16, 19, 23, 28, 34)  # take-off, deg
R_CMB = 3480.0
R_ICB = 1221.5


def branch_of(bottom):
    """Where a ray bottoms. An S ray cannot enter the liquid core: trace() then
    stops it at the core-mantle boundary, which is a reflection (ScS), not a
    turning ray, and is labelled 'cmb'."""
    if abs(bottom - R_CMB) < 1e-6:
        return "cmb"
    if bottom > R_CMB:
        return "mantle"
    if bottom >= R_ICB:
        return "outer"
    return "inner"


def curve(phase, sh, n=3000):
    pmax = R_EARTH / sh[2][0]
    out = []
    for j in range(1, n):
        p = pmax * j / n
        dl, t, b = trace(p, sh)
        out.append((p, dl, t, branch_of(b)))
    return out


def shadow_edge_deg(sh, n=4000):
    """Largest distance reached by a mantle-bottoming P ray (the edge of the shadow)."""
    best = 0.0
    for p, dl, t, br in curve("P", sh, n):
        if br == "mantle":
            best = max(best, math.degrees(dl))
    return best


def core_points(sh, n=3000):
    """Distances (deg) of the PKP caustic B (smallest distance reached by a ray
    turning inside the outer core), of the point C (the ray grazing the inner
    core) and the smallest distance reached by a ray through the inner core."""
    turn, inner = [], []
    for j in range(1, n):
        p = (R_EARTH / sh[2][0]) * j / n
        dl, t, b = trace(p, sh)
        if R_ICB + 1e-6 < b < R_CMB:
            turn.append((p, math.degrees(dl)))
        elif b < R_ICB:
            inner.append(math.degrees(dl))
    b_caustic = min(d for p, d in turn)
    c_point = min(turn)[1]  # smallest p turning in the outer core: grazes the ICB
    return b_caustic, c_point, min(inner)


def fold(delta_deg):
    d = delta_deg % 360.0
    return 360.0 - d if d > 180.0 else d


def p_time_at(delta_deg, sh, n=6000):
    """First-arriving mantle P time (s) at a distance, by interpolation along p."""
    c = [(math.degrees(dl), t) for p, dl, t, br in curve("P", sh, n) if br == "mantle"]
    best = None
    for (d1, t1), (d2, t2) in zip(c[:-1], c[1:]):
        lo, hi = min(d1, d2), max(d1, d2)
        if lo <= delta_deg <= hi and hi > lo:
            t = t1 + (t2 - t1) * (delta_deg - d1) / (d2 - d1)
            best = t if best is None else min(best, t)
    return best


if __name__ == "__main__":
    shp = shells("P")
    shs = shells("S")
    rays = {"mantle": [], "core": []}
    for k, ang in enumerate(RAY_ANGLES):
        p = take_off_p(ang, shp)
        br = "mantle" if branch_of(trace(p, shp)[2]) == "mantle" else "core"
        pts = path(p, shp)
        keep = [q for j, q in enumerate(pts) if j % 20 == 0 or j == len(pts) - 1]
        rays[br] += [(k, x, y) for x, y in keep] + [("nan", "nan", "nan")]
    for br, rows in rays.items():
        write_table(__file__, ("ray", "x", "y"), rows[:-1], part="rays-" + br, digits=6)
    tt = []
    for p, dl, t, br in curve("P", shp, 3000):
        name = {"mantle": 1, "outer": 2, "inner": 3}[br]
        tt.append((name, fold(math.degrees(dl)), t / 60.0))
    for p, dl, t, br in curve("S", shs, 2000):
        if br == "mantle":
            tt.append((4, fold(math.degrees(dl)), t / 60.0))
    # one table per branch keeps the curves continuous in pgfplots
    for b, nm in ((1, "P"), (2, "PKP"), (3, "PKIKP"), (4, "S")):
        sel = [(d, t) for k, d, t in tt if k == b]
        write_table(__file__, ("delta", "t"), sel, part="tt-" + nm, digits=6)
    vals = [("shadow_edge_deg", round(shadow_edge_deg(shp), 2))]
    b_c, c_p, i_min = core_points(shp)
    vals += [("pkp_B_deg", round(b_c, 1)), ("pkp_C_deg", round(c_p, 1)), ("pkikp_min_deg", round(i_min, 1))]
    for dd in (20, 30, 40, 60, 80, 90):
        vals.append(("P%d_s" % dd, round(p_time_at(dd, shp), 1)))
    shs_vals = [(math.degrees(d), t) for p, d, t, br in curve("S", shs, 3000) if br == "mantle"]
    write_table(__file__, ("what", "value"), vals, part="values")
