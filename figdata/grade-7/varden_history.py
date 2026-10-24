"""A west-east section of the Varden Hills through the granite, to put the
region's history in order (grade 7, the ages of the Earth).

The rocks come from the series' region model (figdata/shared/region.py,
imported, never copied). The section E--F runs due east at y = 4.15 km, through
the middle of the granite (the shared section A--B misses it), across the
anticline, the fault and the syncline.

  part unit-<name> : s_km z_m   (rock polygons, rings separated by blank lines)
  part ground      : s_km z_m   (today's ground)
  part fault       : s_km z_m   (the fault plane in the section, up to the ground)
  part base        : s_km z_m   (the base of the sandstone, the unconformity,
                                 drawn only where it is below the ground and
                                 not faulted away)
  part line        : x_km y_km label   (E and F on the map)
  main table       : order event clue  (the history, oldest first)
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))
from _table import write_table  # noqa: E402
import region as R  # noqa: E402

Y = R.GRANITE[1]
A, B = (0.0, Y), (R.WIDTH, Y)
ZMIN, ZMAX = -500.0, 650.0

# the history the method rebuilds, oldest first, with the clue that places it
EVENTS = (
    ("schist", "{the schist forms (the oldest rock)}", "{cut by the granite}"),
    ("granite", "{the granite pushes into the schist and cools}", "{cuts the schist}"),
    ("erosion", "{erosion wears the schist and granite flat}", "{the flat base of the sandstone}"),
    ("cover", "{sandstone, limestone, shale and chalk are laid down}", "{one on top of the other}"),
    ("folding", "{the layers are folded}", "{tilted, although laid down flat}"),
    ("fault", "{the fault breaks the folded layers}", "{cuts all the layers}"),
    ("today", "{erosion carves today's hills; the river lays down its sand}", "{cuts everything}"),
)


def section():
    ss, zs, codes, ground = R.section(A, B, zmin=ZMIN, zmax=ZMAX, ds=10.0, dz=5.0)
    return ss, zs, codes, ground


def units_present(codes):
    names = {u[0]: u[1] for u in R.UNITS}
    return sorted({names[int(c)] for c in set(codes.flatten()) if int(c) in names})


def fault_s(z):
    """Distance along the section (m) where the fault plane is at height z."""
    ux, uy = R._fault_u()
    fx, fy, fz = R.FAULT_POINT
    # along the line: x = s, y = Y; solve (s - fx) ux + (Y - fy) uy + (z - fz)/tan(dip) = 0
    return fx - ((Y - fy) * uy + (z - fz) / math.tan(math.radians(R.FAULT_DIP))) / ux


def fault_line():
    """The fault in the section, from the bottom of the section up to the
    ground (s in m, z in m): two points."""
    lo, hi = ZMIN, ZMAX
    for _ in range(60):     # bisection on z: below the ground, or above it
        mid = (lo + hi) / 2.0
        if mid < R.topo(fault_s(mid), Y):
            lo = mid
        else:
            hi = mid
    return [(fault_s(ZMIN), ZMIN), (fault_s(lo), lo)]


def base_line(step=20.0):
    """Base of the sandstone along the section, split where it is cut by the
    ground or by the fault; [[(s, z), ...], ...]."""
    lines, cur = [], []
    s = 0.0
    while s <= R.WIDTH + 1e-6:
        z = R.contact_elevation("sandstone", s, Y)
        ok = z < R.topo(s, Y) and R.unit(s, Y, z + 1.0) == R.UNIT["sandstone"]
        if ok:
            cur.append((s, z))
        elif cur:
            lines.append(cur)
            cur = []
        s += step
    if cur:
        lines.append(cur)
    return [ln for ln in lines if len(ln) > 2]


if __name__ == "__main__":
    ss, zs, codes, ground = section()
    km = lambda pts: [(round(a / 1000, 4), round(b, 1)) for a, b in pts]  # noqa: E731
    polys = R.unit_polygons(codes, ss, zs, tol=2.0)
    for code, name, *_ in R.UNITS:
        rows = [r for ring in polys.get(code, []) for r in ([()] + km(ring))][1:]
        write_table(__file__, ("s_km", "z_m"), rows, part="unit-" + name)
    write_table(__file__, ("s_km", "z_m"), km(ground), part="ground")
    write_table(__file__, ("s_km", "z_m"), km(fault_line()), part="fault")
    write_table(__file__, ("s_km", "z_m"), [r for ln in base_line() for r in ([()] + km(ln))][1:], part="base")
    write_table(__file__, ("x_km", "y_km", "label"), [(A[0] / 1000, Y / 1000, "E"), (B[0] / 1000, Y / 1000, "F")],
                part="line")
    write_table(__file__, ("order", "event", "clue"), [(i + 1, e, c) for i, (_, e, c) in enumerate(EVENTS)])
