"""Cross-sections, boreholes, structure contours and the tunnel of the
Varden Hills (Year 1, cross-sections). Everything comes from the model of
figdata/shared/region.py (invented region; no real-world value).

Section C-D runs due east along y = 6 km from x = 0 to x = 10 km. The tunnel
of the chapter's problem runs along C-D at the constant elevation
Z_TUNNEL = 200 m.

  part cd-ground      s_km z_m          ground profile along C-D
  part cd-unit-<u>    s_km z_m          unit polygons in the section plane
  part cd-fault       s_km z_m          the fault in the section plane
  part logs           id x_km ground_m base_chalk base_shale base_limestone base_sandstone
                      three boreholes on C-D: depths (m below ground) of the
                      base of each unit (NaN if that contact is above ground)
  part sc             x_km y_km         structure contours of the base of the
                      limestone every 50 m (pgfplots jumps between lines)
  part sc-labels      x_km y_km z_m     one label point per contour
  part tunnel         unit s0_km s1_km  units met by the tunnel, 1 m steps
  part values         what value        apparent dips, fault crossing, lengths
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))
from _table import write_table  # noqa: E402
import region as R  # noqa: E402

Y_CD = 6000.0
C, D = (0.0, Y_CD), (10000.0, Y_CD)
Z_TUNNEL = 200.0
LOGS = (("B1", 1500.0), ("B2", 3500.0), ("B3", 5500.0))
NAMES = {u[0]: u[1] for u in R.UNITS}


def apparent_dip(dip, dipdir, section_az):
    """tan(beta) = tan(delta) cos(gamma), in degrees; gamma = angle between the
    dip direction and the section line (signed result: positive = the plane
    goes down in the direction section_az)."""
    g = math.radians(dipdir - section_az)
    return math.degrees(math.atan(math.tan(math.radians(dip)) * math.cos(g)))


def exaggerated(beta, e):
    """Angle drawn in a section with vertical exaggeration e."""
    return math.degrees(math.atan(e * math.tan(math.radians(beta))))


def section_slope(x, y, az, name="limestone", h=1.0):
    """Measured slope (degrees, positive downward along az) of a contact in a
    vertical section of azimuth az, by finite difference in the model."""
    ux, uy = math.sin(math.radians(az)), math.cos(math.radians(az))
    z0 = R.contact_elevation(name, x - ux * h, y - uy * h)
    z1 = R.contact_elevation(name, x + ux * h, y + uy * h)
    return math.degrees(math.atan((z0 - z1) / (2 * h)))


def fault_x_at(y, z):
    """x of the fault plane at (y, z)."""
    a = math.radians(R.FAULT_DIP_AZ)
    fx, fy, fz = R.FAULT_POINT
    return fx - ((y - fy) * math.cos(a) + (z - fz) / math.tan(math.radians(R.FAULT_DIP))) / math.sin(a)


def log(x, y=Y_CD):
    """Ground elevation and depths below it of the base of chalk, shale,
    limestone and sandstone (NaN where that contact lies above the ground)."""
    zg = R.topo(x, y)
    out = []
    for n in ("chalk", "shale", "limestone", "sandstone"):
        zc = R.contact_elevation(n, x, y)
        out.append(zg - zc if zc <= zg else float("nan"))
    return zg, out


def _u(x):
    return NAMES.get(R.unit(x, Y_CD, Z_TUNNEL, with_alluvium=False), "air")


def tunnel_runs(step=5.0, x0=1000.0, x1=9000.0):
    """Units met by the tunnel from x0 to x1, boundaries refined by bisection."""
    xs = np.arange(x0, x1 + step / 2, step)
    cuts = []
    for a, b in zip(xs[:-1], xs[1:]):
        if _u(a) != _u(b):
            lo, hi = a, b
            for _ in range(40):
                m = (lo + hi) / 2
                if _u(m) == _u(lo):
                    lo = m
                else:
                    hi = m
            cuts.append((lo + hi) / 2)
    edges = [x0] + cuts + [x1]
    return [(_u((p + q) / 2), p, q) for p, q in zip(edges[:-1], edges[1:])]


def limestone_length():
    return sum(b - a for u, a, b in tunnel_runs() if u == "limestone")


def _clip_runs(line, valid, iters=30):
    """Split a polyline into its runs where valid(x, y) holds, each run ending
    on the boundary (found by bisection along the crossing segment)."""
    runs, cur = [], []
    prev = None
    for p in line:
        ok = valid(*p)
        if prev is not None and ok != prev[1]:
            a, b = (prev[0], p) if prev[1] else (p, prev[0])   # a valid, b not
            for _ in range(iters):
                m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
                if valid(*m):
                    a = m
                else:
                    b = m
            cur.append(a)
            if prev[1]:
                runs.append(cur)
                cur = []
        if ok:
            cur.append(p)
        prev = (p, ok)
    if cur:
        runs.append(cur)
    return [r for r in runs if len(r) > 1]


def _arc_point(line, f):
    """Point at the fraction f of the arc length of a polyline."""
    seg = [math.dist(p, q) for p, q in zip(line[:-1], line[1:])]
    target = f * sum(seg)
    for (p, q), d in zip(zip(line[:-1], line[1:]), seg):
        if target <= d and d > 0:
            t = target / d
            return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))
        target -= d
    return line[-1]


def structure_contours(step=50.0, levels=range(-400, 451, 100), name="limestone"):
    """Structure contours of the base of a unit, contoured block by block: the
    footwall surface where it lies in the footwall, the hanging-wall surface
    (moved by the slip) where it lies in the hanging wall. Between the two
    cutoff lines of the normal fault the surface is absent (the heave gap)."""
    xs = np.arange(0.0, R.WIDTH + step / 2, step)
    ys = np.arange(0.0, R.HEIGHT + step / 2, step)
    sx, sy, sz = R._slip()

    def z_foot(x, y):
        return R._contact_unfaulted(name, x, y)

    def z_hang(x, y):
        return R._contact_unfaulted(name, x - sx, y - sy) + sz

    blocks = (
        (z_foot, lambda x, y: not R.hanging_wall(x, y, z_foot(x, y))),
        (z_hang, lambda x, y: R.hanging_wall(x, y, z_hang(x, y))),
    )
    out = []
    for zf, valid in blocks:
        z = np.array([[zf(x, y) for x in xs] for y in ys])
        for lv in levels:
            for line in R.trace(z, xs, ys, lv):
                for run in _clip_runs(line, valid):
                    run = R.simplify(run, 2.0)
                    if len(run) > 1:
                        out.append((lv, run))
    return out


if __name__ == "__main__":
    km = lambda v: round(v / 1000.0, 4)  # noqa: E731
    ss, zs, codes, ground = R.section(C, D, zmin=-500.0, zmax=650.0)
    write_table(__file__, ("s_km", "z_m"), [(km(s), round(z, 1)) for s, z in ground], part="cd-ground")
    polys = R.unit_polygons(codes, ss, zs, tol=2.0)
    for code, name, *_ in R.UNITS:
        rings = polys.get(code, [])
        rows = [r for ring in rings for r in ([()] + [(km(s), round(z, 1)) for s, z in ring])][1:]
        write_table(__file__, ("s_km", "z_m"), rows, part="cd-unit-" + name)
    write_table(__file__, ("s_km", "z_m"),
                [(km(fault_x_at(Y_CD, z)), z) for z in (-500.0, R.topo(fault_x_at(Y_CD, 400.0), Y_CD))],
                part="cd-fault")
    rows = []
    for i, x in LOGS:
        zg, d = log(x)
        rows.append((i, km(x), zg) + tuple(d))
    write_table(__file__, ("id", "x_km", "ground_m", "base_chalk", "base_shale", "base_limestone",
                           "base_sandstone"), rows, part="logs", digits=5)
    sc = structure_contours()
    rows, labels = [], []
    for lv, line in sc:
        rows += ([()] if rows else []) + [(km(x), km(y)) for x, y in line]
        mid = _arc_point(line, 0.5)
        labels.append((km(mid[0]), km(mid[1]), lv))
    write_table(__file__, ("x_km", "y_km"), rows, part="sc")
    write_table(__file__, ("x_km", "y_km", "z_m"), labels, part="sc-labels")
    write_table(__file__, ("unit", "s0_km", "s1_km"), [(u, km(a), km(b)) for u, a, b in tunnel_runs()],
                part="tunnel", digits=6)
    az_e, dip_e = R.limb_attitude(4300.0)
    az_w, dip_w = R.limb_attitude(2000.0)
    ab = math.degrees(math.atan2(R.SECTION_AB[1][0] - R.SECTION_AB[0][0], R.SECTION_AB[1][1] - R.SECTION_AB[0][1]))
    write_table(__file__, ("what", "value"), [
        ("east_dipdir", az_e), ("east_dip", dip_e), ("west_dipdir", az_w), ("west_dip", dip_w),
        ("app_east_cd", apparent_dip(dip_e, az_e, 90.0)), ("app_west_cd", apparent_dip(dip_w, az_w, 270.0)),
        ("ab_azimuth", ab), ("app_east_ab", apparent_dip(dip_e, az_e, ab)),
        ("app_fault_cd", apparent_dip(R.FAULT_DIP, R.FAULT_DIP_AZ, 90.0)),
        ("fault_x_tunnel", fault_x_at(Y_CD, Z_TUNNEL)),
        ("limestone_length", limestone_length()),
        ("true_thickness_limestone", R.THICK["limestone"] * math.cos(math.radians(dip_e))),
    ], part="values", digits=6)
