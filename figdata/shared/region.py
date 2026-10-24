"""The series' invented exercise region: one analytic geological model.

Every geological or topographic map, cross-section, three-point problem and
outcrop-pattern exercise in the five books is drawn from this one region, so a
reader who meets it in Book 1 recognises it in Book 5. Nothing here is a real
place; the name is REGION_NAME (checked not to be a real place, see
sources/data_ledger.md row region:name). Units are metres; x runs east, y north,
z is elevation above sea level; the map is 10 km x 8 km.

The model, oldest event first:
  1. schist basement (metamorphosed, about 480 Ma);
  2. a granite intruded into it (about 310 Ma), a body of elliptical plan;
  3. erosion, then an unconformity, then the cover, deposited flat:
       sandstone (Triassic, 120 m), limestone (Jurassic, 180 m),
       shale (Jurassic, 100 m), chalk (Cretaceous, top eroded);
  4. folding into a chevron anticline (axis x = 3.5 km) and syncline
     (x = 7.5 km), axes N-S, plunging 2 degrees north, limbs dipping 12 degrees:
     the limbs are PLANES, so three-point problems on them are exact;
  5. a normal fault striking 030, dipping 60 degrees to the ESE (azimuth 120),
     with 200 m of dip-slip throw (the hanging wall, ESE side, moved down);
  6. erosion to today's relief: hills of 300-500 m cut by a river flowing
     east, with a flat alluvial floor (Quaternary alluvium).

Pure functions (tested in tests/shared/test_region.py): topo(x, y),
unit(x, y, z), contact_elevation(name, x, y), limb attitude, and the
marching-squares tracer that turns fields into polylines. When run, the script
writes the map and section tables listed in write_all() into figdata/out/.
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

REGION_NAME = "Varden Hills"

# ----------------------------------------------------------------------------
# the model
# ----------------------------------------------------------------------------
WIDTH, HEIGHT = 10000.0, 8000.0

# units, oldest first (code, name, lithology style, period colour, age in Ma)
UNITS = [
    (1, "schist", "schist", "icsOrdovician", 480),
    (2, "granite", "granite", "icsCarboniferous", 310),
    (3, "sandstone", "sandstone", "icsTriassic", 245),
    (4, "limestone", "limestone", "icsJurassic", 180),
    (5, "shale", "shale", "icsJurassic", 165),
    (6, "chalk", "limestone", "icsCretaceous", 90),
    (7, "alluvium", "alluvium", "icsQuaternary", 0.01),
]
UNIT = {u[1]: u[0] for u in UNITS}
THICK = {"sandstone": 120.0, "limestone": 180.0, "shale": 100.0}

# folding: base of the cover (the unconformity) before faulting
AXIS_ANTI, AXIS_SYN = 3500.0, 7500.0
LIMB_DIP = 12.0               # degrees
PLUNGE = 2.0                  # degrees, toward the north
Z_AXIS = 230.0                # base of the cover on the anticline axis at y = 4000

# faulting
FAULT_POINT = (4300.0, 1000.0, 250.0)
FAULT_DIP_AZ = 120.0          # dip direction (azimuth)
FAULT_DIP = 60.0
FAULT_THROW = 200.0           # vertical component of the slip, hanging wall down

# granite: elliptical in plan, steep-sided, below the unconformity only
GRANITE = (3500.0, 4150.0, 380.0, 560.0)

# relief
RIVER_Z0, RIVER_GRAD = 170.0, 0.007   # m at x = 0, and m per m eastward
FLOOR_HALF = 150.0                    # half-width of the flat alluvial floor


def river_y(x):
    return 4000.0 + 600.0 * math.sin(2 * math.pi * x / 7000.0)


def river_z(x):
    return RIVER_Z0 - RIVER_GRAD * x


def _hills(x, y):
    return (250.0 + 70.0 * math.sin(2 * math.pi * x / 5200.0 + 0.7)
            + 60.0 * math.cos(2 * math.pi * y / 6100.0) + 40.0 * math.sin(2 * math.pi * (x + y) / 3300.0)
            + 0.012 * abs(y - 4000.0))


def topo(x, y):
    """Ground elevation (m): a flat floor along the river, hills either side."""
    d = abs(y - river_y(x))
    if d <= FLOOR_HALF:
        return river_z(x)
    t = (d - FLOOR_HALF) / 1100.0
    rise = 1.0 - math.exp(-t * t * 1.6)
    return river_z(x) + _hills(x, y) * rise


def _tri(x):
    """Distance (m) below the crest line: 0 on the anticline axis, rising
    linearly to the syncline and back, period 2 * (syncline - anticline)."""
    half = AXIS_SYN - AXIS_ANTI
    u = (x - AXIS_ANTI) % (2 * half)
    return u if u <= half else 2 * half - u


def base_cover(x, y):
    """Elevation of the unconformity (base of the sandstone), unfaulted."""
    return (Z_AXIS - math.tan(math.radians(LIMB_DIP)) * _tri(x)
            - math.tan(math.radians(PLUNGE)) * (y - 4000.0))


def _contact_unfaulted(name, x, y):
    z = base_cover(x, y)
    for n in ("sandstone", "limestone", "shale"):
        if n == name:
            return z
        z += THICK[n]
    if name == "chalk":
        return z
    raise KeyError(name)


def _fault_u():
    a = math.radians(FAULT_DIP_AZ)
    return math.sin(a), math.cos(a)


def hanging_wall(x, y, z):
    """True on the ESE side of the fault plane (the block that moved down)."""
    ux, uy = _fault_u()
    fx, fy, fz = FAULT_POINT
    s = (x - fx) * ux + (y - fy) * uy
    return s + (z - fz) / math.tan(math.radians(FAULT_DIP)) > 0


def _slip():
    """Slip vector of the hanging wall: down the dip, vertical part = throw."""
    ux, uy = _fault_u()
    h = FAULT_THROW / math.tan(math.radians(FAULT_DIP))
    return ux * h, uy * h, -FAULT_THROW


def _restore(x, y, z):
    """Where the point (x, y, z) was before faulting."""
    if hanging_wall(x, y, z):
        sx, sy, sz = _slip()
        return x - sx, y - sy, z - sz
    return x, y, z


def unit(x, y, z, with_alluvium=True):
    """Unit code at (x, y, z); 0 above the ground."""
    if z > topo(x, y) + 1e-6:
        return 0
    if with_alluvium and abs(y - river_y(x)) <= FLOOR_HALF and z >= river_z(x) - 6.0:
        return UNIT["alluvium"]
    x0, y0, z0 = _restore(x, y, z)
    zb = base_cover(x0, y0)
    if z0 < zb:
        gx, gy, a, b = GRANITE
        r = ((x0 - gx) / a) ** 2 + ((y0 - gy) / b) ** 2
        return UNIT["granite"] if r <= 1.0 + (zb - z0) / 4000.0 else UNIT["schist"]
    for n in ("sandstone", "limestone", "shale"):
        zb += THICK[n]
        if z0 < zb:
            return UNIT[n]
    return UNIT["chalk"]


def contact_elevation(name, x, y):
    """Elevation of the BASE of a cover unit at (x, y), faulting included.

    The footwall value counts only if it lies in the footwall, the hanging-wall
    value (restored through the slip) only if it lies in the hanging wall. Near
    the fault a vertical can meet neither: the normal fault has cut the contact
    out between its two cut-offs, and the result is nan (a former fixed-point
    iteration oscillated there and returned a footwall value lying in the
    hanging wall)."""
    z_fw = _contact_unfaulted(name, x, y)
    if not hanging_wall(x, y, z_fw):
        return z_fw
    sx, sy, sz = _slip()
    z_hw = _contact_unfaulted(name, x - sx, y - sy) + sz
    if hanging_wall(x, y, z_hw):
        return z_hw
    return math.nan


def limb_attitude(x):
    """(dip direction azimuth, dip) of the cover at a footwall point of
    abscissa x: the limbs are planes, the plunge adds a northward component."""
    half = AXIS_SYN - AXIS_ANTI
    u = (x - AXIS_ANTI) % (2 * half)
    east = 1.0 if u < half else -1.0              # east of the anticline axis: dips east
    gx = -east * math.tan(math.radians(LIMB_DIP))   # dz/dx
    gy = -math.tan(math.radians(PLUNGE))            # dz/dy
    dip = math.degrees(math.atan(math.hypot(gx, gy)))
    az = math.degrees(math.atan2(-gx, -gy)) % 360.0  # steepest descent
    return az, dip


# ----------------------------------------------------------------------------
# marching squares
# ----------------------------------------------------------------------------
def trace(field, xs, ys, level=0.0):
    """Polylines where field (ny x nx, rows = ys) crosses `level`, interpolated
    linearly on the cell edges. Closed loops end on their first point."""
    f = np.asarray(field, dtype=float) - level
    ny, nx = f.shape
    above = f > 0

    def pt(edge):
        kind, j, i = edge
        if kind == "h":            # between (j, i) and (j, i + 1)
            a, b = f[j, i], f[j, i + 1]
            t = a / (a - b)
            return xs[i] + t * (xs[i + 1] - xs[i]), ys[j]
        a, b = f[j, i], f[j + 1, i]
        t = a / (a - b)
        return xs[i], ys[j] + t * (ys[j + 1] - ys[j])

    nbr = {}

    def link(e1, e2):
        nbr.setdefault(e1, []).append(e2)
        nbr.setdefault(e2, []).append(e1)

    cells = np.argwhere((above[:-1, :-1] != above[:-1, 1:]) | (above[:-1, :-1] != above[1:, :-1])
                        | (above[1:, 1:] != above[:-1, 1:]))
    for j, i in cells:
        b, r, t, l = ("h", j, i), ("v", j, i + 1), ("h", j + 1, i), ("v", j, i)
        c = (above[j, i] << 0) | (above[j, i + 1] << 1) | (above[j + 1, i + 1] << 2) | (above[j + 1, i] << 3)
        pairs = {1: [(l, b)], 2: [(b, r)], 3: [(l, r)], 4: [(r, t)], 6: [(b, t)], 7: [(l, t)],
                 8: [(t, l)], 9: [(t, b)], 11: [(t, r)], 12: [(r, l)], 13: [(r, b)], 14: [(b, l)],
                 5: [(l, t), (b, r)], 10: [(t, r), (l, b)]}.get(int(c), [])
        for e1, e2 in pairs:
            link(e1, e2)
    seen, lines = set(), []
    starts = [e for e, n in nbr.items() if len(n) == 1] + list(nbr)
    for s in starts:
        if s in seen:
            continue
        chain, prev, cur = [s], None, s
        seen.add(s)
        while True:
            nxt = [e for e in nbr[cur] if e != prev and e not in seen]
            if not nxt:
                if len(chain) > 2 and chain[0] in nbr[cur]:
                    chain.append(chain[0])
                break
            prev, cur = cur, nxt[0]
            seen.add(cur)
            chain.append(cur)
        lines.append([pt(e) for e in chain])
    return lines


def orient_fault(points, z_of=None):
    """Reverse a fault trace if needed so that the hanging wall lies on its
    LEFT (the `normal fault` style puts its ticks on the left)."""
    if len(points) < 2:
        return points
    k = len(points) // 2
    (x0, y0), (x1, y1) = points[k - 1], points[k]
    n = math.hypot(x1 - x0, y1 - y0)
    lx, ly = (x0 + x1) / 2 - (y1 - y0) / n * 30.0, (y0 + y1) / 2 + (x1 - x0) / n * 30.0
    zl = z_of(lx, ly) if z_of else 0.0
    return points if hanging_wall(lx, ly, zl) else points[::-1]


def simplify(points, tol):
    """Douglas-Peucker."""
    if len(points) < 3:
        return list(points)
    (x0, y0), (x1, y1) = points[0], points[-1]
    dx, dy = x1 - x0, y1 - y0
    n = math.hypot(dx, dy)
    best, k = -1.0, 0
    for i, (x, y) in enumerate(points[1:-1], 1):
        d = abs(dy * (x - x0) - dx * (y - y0)) / n if n else math.hypot(x - x0, y - y0)
        if d > best:
            best, k = d, i
    if best <= tol:
        return [points[0], points[-1]]
    return simplify(points[:k + 1], tol)[:-1] + simplify(points[k:], tol)


# ----------------------------------------------------------------------------
# grids and products
# ----------------------------------------------------------------------------
STEP = 10.0


def map_grid(step=STEP):
    xs = np.arange(0.0, WIDTH + step / 2, step)
    ys = np.arange(0.0, HEIGHT + step / 2, step)
    return xs, ys


def topo_grid(xs, ys):
    return np.array([[topo(x, y) for x in xs] for y in ys])


def unit_grid(xs, ys, z):
    return np.array([[unit(x, y, z[j, i]) for i, x in enumerate(xs)] for j, y in enumerate(ys)])


def unit_polygons(codes, xs, ys, tol=4.0):
    """{code: [rings]} -- each unit's outcrop as closed rings (holes included:
    fill with the even-odd rule)."""
    out = {}
    pad_x = np.concatenate(([xs[0] - (xs[1] - xs[0])], xs, [xs[-1] + (xs[1] - xs[0])]))
    pad_y = np.concatenate(([ys[0] - (ys[1] - ys[0])], ys, [ys[-1] + (ys[1] - ys[0])]))
    for code in sorted(set(int(c) for c in np.unique(codes)) - {0}):
        ind = np.zeros((codes.shape[0] + 2, codes.shape[1] + 2))
        ind[1:-1, 1:-1] = (codes == code)
        rings = trace(ind, pad_x, pad_y, 0.5)
        # clip the half-cell padding back to the map frame
        clipped = [[(min(max(x, xs[0]), xs[-1]), min(max(y, ys[0]), ys[-1])) for x, y in r] for r in rings]
        out[code] = [simplify(r, tol) for r in clipped if len(r) > 3]
    return out


def section(a, b, zmin=-700.0, zmax=650.0, ds=10.0, dz=5.0):
    """Cross-section from map point a to b: (s along the line in m, z) grids,
    unit codes, and the ground profile."""
    L = math.hypot(b[0] - a[0], b[1] - a[1])
    ss = np.arange(0.0, L + ds / 2, ds)
    zs = np.arange(zmin, zmax + dz / 2, dz)
    pts = [(a[0] + (b[0] - a[0]) * s / L, a[1] + (b[1] - a[1]) * s / L) for s in ss]
    codes = np.array([[unit(px, py, z) for (px, py) in pts] for z in zs])
    ground = [(s, topo(px, py)) for s, (px, py) in zip(ss, pts)]
    return ss, zs, codes, ground


SECTION_AB = ((500.0, 2500.0), (9500.0, 5500.0))


def write_all():
    xs, ys = map_grid()
    z = topo_grid(xs, ys)
    km = lambda pts: [(round(x / 1000, 4), round(y / 1000, 4)) for x, y in pts]  # noqa: E731
    jumps = lambda lines: [r for line in lines for r in ([()] + km(line))][1:]   # noqa: E731
    # topographic contours every 50 m (index contours every 250 m in a table of their own)
    for kind, levels in (("contours", [lv for lv in range(100, 700, 50) if lv % 250]),
                         ("index-contours", [250, 500])):
        rows = []
        for lv in levels:
            for line in trace(z, xs, ys, lv):
                line = simplify(line, 3.0)
                if len(line) > 1:
                    rows += ([()] if rows else []) + km(line)
        write_table(__file__, ("x_km", "y_km"), rows, part=kind)
    # river
    write_table(__file__, ("x_km", "y_km"),
                km([(x, river_y(x)) for x in np.arange(0.0, WIDTH + 1, 50.0)]), part="river")
    # geological map: one ring table per unit
    codes = unit_grid(xs, ys, z)
    polys = unit_polygons(codes, xs, ys)
    for code, name, *_ in UNITS:
        write_table(__file__, ("x_km", "y_km"), jumps(polys.get(code, [])), part="unit-" + name)
    # the fault trace on the ground
    ux, uy = _fault_u()
    fx, fy, fz = FAULT_POINT
    g = np.array([[(x - fx) * ux + (y - fy) * uy + (z[j, i] - fz) / math.tan(math.radians(FAULT_DIP))
                   for i, x in enumerate(xs)] for j, y in enumerate(ys)])
    write_table(__file__, ("x_km", "y_km"), jumps([orient_fault(simplify(l, 3.0), z_of=topo)
                                                   for l in trace(g, xs, ys, 0.0)]), part="fault")
    # the cross-section A-B
    a, b = SECTION_AB
    ss, zs, sc, ground = section(a, b)
    write_table(__file__, ("s_km", "z_m"), [(round(s / 1000, 4), round(zz, 1)) for s, zz in ground],
                part="section-ground")
    spolys = unit_polygons(sc, ss, zs, tol=2.0)
    for code, name, *_ in UNITS:
        rings = spolys.get(code, [])
        rows = [r for ring in rings for r in ([()] + [(round(s / 1000, 4), round(zz, 1)) for s, zz in ring])][1:]
        write_table(__file__, ("s_km", "z_m"), rows, part="section-unit-" + name)
    # the fault in the section plane: where s + (z - zf)/tan(dip) = 0 along A-B
    L = math.hypot(b[0] - a[0], b[1] - a[1])

    def plane(sv, zz):
        px, py = a[0] + (b[0] - a[0]) * sv / L, a[1] + (b[1] - a[1]) * sv / L
        return (px - fx) * ux + (py - fy) * uy + (zz - fz) / math.tan(math.radians(FAULT_DIP))

    # bottom of the section: the plane is linear in s along a straight line
    g0, g1 = plane(0.0, zs[0]), plane(L, zs[0])
    fl = [(round(-g0 / (g1 - g0) * L / 1000, 4), round(zs[0], 1))]
    # top: where the plane meets the GROUND (it once ran on to the highest
    # ground of the profile, above the surface; Book 1/2 reports, 2026-10-23)
    def on_ground(sv):
        px, py = a[0] + (b[0] - a[0]) * sv / L, a[1] + (b[1] - a[1]) * sv / L
        return plane(sv, topo(px, py))
    lo, hi = 0.0, L
    if on_ground(lo) * on_ground(hi) < 0:
        for _ in range(80):
            mid = (lo + hi) / 2
            if on_ground(lo) * on_ground(mid) <= 0:
                hi = mid
            else:
                lo = mid
        sg = (lo + hi) / 2
        pg = (a[0] + (b[0] - a[0]) * sg / L, a[1] + (b[1] - a[1]) * sg / L)
        fl.append((round(sg / 1000, 4), round(topo(*pg), 1)))
    write_table(__file__, ("s_km", "z_m"), fl, part="section-fault")
    write_table(__file__, ("x_km", "y_km", "label"),
                [(a[0] / 1000, a[1] / 1000, "A"), (b[0] / 1000, b[1] / 1000, "B")], part="section-line")


if __name__ == "__main__":
    write_all()
