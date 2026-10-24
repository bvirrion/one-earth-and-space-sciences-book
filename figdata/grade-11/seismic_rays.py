"""Seismic rays through a spherical Earth with the PREM speeds (grade 11,
seismic-structure).

The Earth is cut into thin spherical shells (STEP_KM thick) of constant speed
(PREM, linearly interpolated at the middle of each shell; ledger data:prem). A ray
leaves a surface source with the ray parameter p = r sin(i) / v (seconds per
radian), which stays the same along the ray (Snell's law on a sphere). In a shell of
constant speed v the ray is a straight segment whose closest approach to the centre
is b = p v; between radii r1 < r2 (both > b) it sweeps the angle
acos(b/r2) - acos(b/r1) and has the length sqrt(r2^2 - b^2) - sqrt(r1^2 - b^2). If b
lies inside a shell, the ray turns there and comes back up symmetrically. S rays stop
at the outer core (no S speed). Distances and times of the rays give the travel-time
curves and the shadow zone.

  part praysmantle, prayscore, srays   x y   ray paths in a disc of radius 1 (the
                                     Earth), source at the top, P to the right, S
                                     mirrored to the left, rays separated by empty lines
  part ttp, tts           delta_deg t_min   travel times of P and S (direct branches)
  part ttpkp, ttpkikp     delta_deg t_min   P waves through the outer core only, and
                                     through the inner core (ordered by ray parameter)
  part observed           delta_deg p_min s_min   empirical times (ledger auspass:surftim)
  part numbers            key value
"""
import functools
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

import prem_profiles  # noqa: E402

R = 6371.0
STEP_KM = 2.0


def shells(col):
    """[(r_top, r_bot, v)] from the surface to the centre; col 1 = P, 2 = S."""
    rows = prem_profiles.prem()
    out = []
    for a, b in zip(rows[:-1], rows[1:]):
        if b[0] <= a[0]:
            continue
        n = max(1, int(math.ceil((b[0] - a[0]) / STEP_KM)))
        for k in range(n):
            d1 = a[0] + (b[0] - a[0]) * k / n
            d2 = a[0] + (b[0] - a[0]) * (k + 1) / n
            dm = 0.5 * (d1 + d2)
            v = a[col] + (b[col] - a[col]) * (dm - a[0]) / (b[0] - a[0])
            out.append((R - d1, R - d2, v))
    return out


SHELLS = {"P": shells(1), "S": shells(2)}


def trace(p, phase="P", path=False):
    """Epicentral distance (degrees), travel time (s), deepest radius (km), whether the
    ray entered the outer core and the inner core, and optionally the down-going half
    path as (theta, r) points. None if an S ray reaches the outer core, or if the ray
    is reflected at a discontinuity where the speed jumps up (those reflected
    waves are left out: only refracted rays are drawn and timed)."""
    dth, t = 0.0, 0.0
    pts = [(0.0, R)] if path else None
    core = inner = False
    rmin = R
    vprev = None
    for r2, r1, v in SHELLS[phase]:
        if v <= 0.0:
            return None
        b = p * v
        if b >= r2:                                   # cannot enter this shell
            if vprev is not None and v - vprev > 0.05:
                return None                           # reflected at a discontinuity
            break                                     # turns at the top of the shell
        vprev = v
        if r2 < 3480.0 + 1e-6:                        # the shell lies in the core
            core = True
        if r2 < 1221.5 + 1e-6:
            inner = True
        if b > r1:                                    # turns inside this shell
            dth += math.acos(b / r2)
            t += math.sqrt(r2 * r2 - b * b) / v
            rmin = b
            if path:
                pts.append((dth, b))
            break
        dth += math.acos(b / r2) - math.acos(b / r1) if r1 > 0 else math.acos(b / r2)
        t += (math.sqrt(r2 * r2 - b * b) - math.sqrt(max(r1 * r1 - b * b, 0.0))) / v
        rmin = r1
        if path:
            pts.append((dth, r1))
    return 2 * math.degrees(dth), 2 * t, rmin, core, inner, pts


def p_max(phase="P"):
    return R / SHELLS[phase][0][2]


def p_core(phase="P"):
    """Smallest ray parameter of a ray that turns in the mantle: r_cmb / v just above."""
    return 3480.0 / prem_profiles.value_at(2891.0, 1 if phase == "P" else 2, below=False)


@functools.lru_cache(maxsize=None)
def branches(phase="P", n=3000):
    """(delta, t, p, rmin, core, inner) for p from 0 to p_max (exclusive)."""
    out = []
    for k in range(1, n):
        p = p_max(phase) * k / n
        r = trace(p, phase)
        if r is not None:
            out.append((r[0], r[1], p, r[2], r[3], r[4]))
    return out


@functools.lru_cache(maxsize=None)
def direct_curve(phase="P", n=3000, step=0.5):
    """Direct (mantle) branch: rays turning above the core, the first arrival at each
    distance on a grid of `step` degrees. Where the speed jumps (near 400 and 670 km)
    the travel-time curve folds back on itself; between each pair of neighbouring
    rays (in ray-parameter order) the time is interpolated, and at each distance the
    earliest of all the segments that cover it is kept (the first-arrival envelope)."""
    rows = sorted((b for b in branches(phase, n) if not b[4]), key=lambda b: -b[2])
    segs = [(a[0], a[1], b[0], b[1]) for a, b in zip(rows[:-1], rows[1:])
            if abs(b[2] - a[2]) < 3 * p_max(phase) / n]
    out = []
    k = 1
    while k * step <= max(r[0] for r in rows):
        d = k * step
        best = None
        for d1, t1, d2, t2 in segs:
            if min(d1, d2) <= d <= max(d1, d2) and d2 != d1:
                t = t1 + (t2 - t1) * (d - d1) / (d2 - d1)
                if best is None or t < best:
                    best = t
        if best is not None:
            out.append((d, best))
        k += 1
    return out


def time_at(delta, phase="P"):
    """First-arrival time (s) of the direct branch at delta (degrees), interpolated."""
    c = direct_curve(phase)
    for (d1, t1), (d2, t2) in zip(c[:-1], c[1:]):
        if d1 <= delta <= d2:
            return t1 + (t2 - t1) * (delta - d1) / (d2 - d1)
    raise ValueError(delta)


def shadow():
    """Edges of the P shadow zone: the farthest mantle P ray, and the nearest rays
    that cross the outer core only (PKP) and the inner core (PKIKP)."""
    b = branches("P")
    mantle = max(x[0] for x in b if not x[4])
    pkp = min(x[0] for x in b if x[4] and not x[5])
    pkikp = min(x[0] for x in b if x[5])
    s_max = max(x[0] for x in branches("S"))
    return mantle, pkp, pkikp, s_max


def ray_points(p, phase="P", n_max=400):
    """A ray path in a unit disc: source at the top (theta measured from the top)."""
    r = trace(p, phase, path=True)
    if r is None:
        return []
    half = r[5]
    total = math.radians(r[0])
    down = [(th, rr) for th, rr in half]
    up = [(total - th, rr) for th, rr in reversed(half)]
    pts = down + up
    step = max(1, len(pts) // n_max)
    pts = pts[::step] + [pts[-1]]
    return [(rr / R * math.sin(th), rr / R * math.cos(th)) for th, rr in pts]


# Observed first P and S times at the surface (s), ledger auspass:surftim: mean of the
# one-degree bins either side of each whole degree (None: no value in the file).
OBSERVED = {20: (274.3, 498.6), 30: (370.3, 668.5), 40: (456.4, 822.2), 50: (535.9, 967.1),
            60: (608.2, 1101.3), 70: (673.3, 1224.6), 80: (731.2, None), 90: (781.3, None)}

RAY_DEG_P = [20, 40, 60, 80, 98]          # chosen ray distances (mantle P)
RAY_DEG_S = [20, 40, 60, 80, 102]         # chosen ray distances (mantle S), drawn mirrored
CORE_P = [0.15, 0.45, 0.6, 0.8, 0.95]     # ray parameters as fractions of p_core (core P)


def p_for_delta(delta, phase="P"):
    """Ray parameter of the direct ray reaching delta (bisection on the mantle branch)."""
    lo = (3480.0 / prem_profiles.value_at(2891.0, 2, below=False) if phase == "S" else p_core()) * 1.0005
    hi = p_max(phase) * 0.9999
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        r = trace(mid, phase)
        k = 1
        while r is None:                      # a reflected ray: nudge p
            r = trace(mid * (1 + 1e-5 * k), phase)
            k += 1
        d = r[0]
        if d > delta:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def numbers():
    mantle, pkp, pkikp, s_max = shadow()
    return {"shadow_start_deg": mantle, "shadow_end_pkp_deg": pkp, "pkikp_min_deg": pkikp,
            "s_direct_max_deg": s_max,
            "p_60_s": time_at(60.0, "P"), "s_60_s": time_at(60.0, "S"),
            "p_30_s": time_at(30.0, "P"), "p_90_s": time_at(90.0, "P"),
            "sp_60_s": time_at(60.0, "S") - time_at(60.0, "P")}


if __name__ == "__main__":
    rows = []
    for d in RAY_DEG_P:
        rows += ray_points(p_for_delta(d)) + [()]
    write_table(__file__, ("x", "y"), rows, part="praysmantle", digits=5)
    rows = []
    for f in CORE_P:
        rows += ray_points(f * p_core()) + [()]
    write_table(__file__, ("x", "y"), rows, part="prayscore", digits=5)
    rows = []
    for d in RAY_DEG_S:
        rows += [(-x, y) for x, y in ray_points(p_for_delta(d, "S"), "S")] + [()]
    write_table(__file__, ("x", "y"), rows, part="srays", digits=5)
    for ph in ("P", "S"):
        c = direct_curve(ph)
        write_table(__file__, ("delta_deg", "t_min"), [(d, t / 60.0) for d, t in c],
                    part="tt" + ph.lower(), digits=5)
    br = sorted(branches("P"), key=lambda x: -x[2])          # by ray parameter
    pk = [(x[0], x[1] / 60.0) for x in br if x[4] and not x[5]]
    write_table(__file__, ("delta_deg", "t_min"), pk[::3], part="ttpkp", digits=5)
    pki = [(x[0], x[1] / 60.0) for x in br if x[5]]
    write_table(__file__, ("delta_deg", "t_min"), pki[::3], part="ttpkikp", digits=5)
    write_table(__file__, ("delta_deg", "p_min", "s_min"),
                [(d, p / 60.0, s / 60.0 if s else float("nan")) for d, (p, s) in sorted(OBSERVED.items())],
                part="observed", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")
