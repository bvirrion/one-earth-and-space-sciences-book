"""figdata/shared/region.py: the invented region is geologically consistent."""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "shared"))
import region as R  # noqa: E402


def _plane(p1, p2, p3):
    """Dip direction (azimuth) and dip of the plane through three points."""
    v1, v2 = np.subtract(p2, p1), np.subtract(p3, p1)
    n = np.cross(v1, v2)
    if n[2] < 0:
        n = -n
    a, b, c = n                     # plane: a x + b y + c z = d -> grad z = (-a/c, -b/c)
    gx, gy = -a / c, -b / c
    return math.degrees(math.atan2(-gx, -gy)) % 360, math.degrees(math.atan(math.hypot(gx, gy)))


def test_limb_attitude():
    az, dip = R.limb_attitude(5000)          # east limb: dips east, plunge north
    assert abs(dip - math.degrees(math.atan(math.hypot(math.tan(math.radians(12)),
                                                       math.tan(math.radians(2)))))) < 1e-9
    assert 80 < az < 82
    az, dip = R.limb_attitude(2000)          # west limb: dips west
    assert 278 < az < 280


def test_three_point_problem_is_exact_on_a_limb():
    pts = [(4000.0, 6000.0), (4600.0, 7200.0), (5100.0, 6400.0)]
    for x, y in pts:                          # all in the footwall
        assert not R.hanging_wall(x, y, R.contact_elevation("limestone", x, y))
    p = [(x, y, R.contact_elevation("limestone", x, y)) for x, y in pts]
    az, dip = _plane(*p)
    az0, dip0 = R.limb_attitude(4500)
    assert abs(az - az0) < 1e-6 and abs(dip - dip0) < 1e-6


def _outcrop_x(name, y_of, lo, hi):
    """x where the ground meets the base of `name` along the curve y = y_of(x)."""
    f = lambda x: R.topo(x, y_of(x)) - R.contact_elevation(name, x, y_of(x))  # noqa: E731
    a, b = lo, hi
    assert f(a) * f(b) < 0
    for _ in range(80):
        m = (a + b) / 2
        a, b = (m, b) if f(a) * f(m) > 0 else (a, m)
    return (a + b) / 2


def test_v_rule():
    # east limb (dips east, downstream, more steeply than the river): the
    # outcrop of a contact makes a V pointing DOWNSTREAM (east) in the valley
    xv = _outcrop_x("limestone", R.river_y, 3600, 5600)
    xh = _outcrop_x("limestone", lambda x: R.river_y(x) - 1500, 3600, 5600)
    assert xv > xh + 100
    # west limb (dips west, upstream): the V points UPSTREAM (west)
    xv = _outcrop_x("limestone", R.river_y, 1500, 3400)
    xh = _outcrop_x("limestone", lambda x: R.river_y(x) - 1500, 1500, 3400)
    assert xv < xh - 50


def test_fault_is_normal_and_oriented():
    # the hanging wall (ESE) is lower: a contact is lower just east of the fault
    y = 3000.0
    fx = R.FAULT_POINT[0] + (y - R.FAULT_POINT[1]) * math.tan(math.radians(30))
    zw = R.contact_elevation("shale", fx - 300, y)
    ze = R.contact_elevation("shale", fx + 300, y)
    assert ze < zw - 50
    t30 = math.tan(math.radians(30))
    line = [(R.FAULT_POINT[0] + (yy - R.FAULT_POINT[1]) * t30, yy) for yy in (2000.0, 3000.0)]
    a = R.orient_fault(line, z_of=R.topo)
    b = R.orient_fault(line[::-1], z_of=R.topo)
    assert a == b                              # one orientation, whatever the input


def test_contact_in_the_fault_gap():
    # along a line across the fault, every contact value lies in the block it
    # was computed for, and the normal fault leaves a gap where a vertical
    # meets no base of the sandstone (nan), with the contact on both sides
    y = 4150.0
    found = []
    for i in range(400):
        x = 5000.0 + 5.0 * i
        z = R.contact_elevation("sandstone", x, y)
        if math.isnan(z):
            found.append("gap")
            continue
        restored = R._restore(x, y, z + 1e-6)
        assert abs(restored[2] - R._contact_unfaulted("sandstone", restored[0], restored[1]) - 1e-6) < 1e-9
        found.append("hw" if R.hanging_wall(x, y, z + 1e-6) else "fw")
    runs = [k for i, k in enumerate(found) if i == 0 or k != found[i - 1]]
    assert runs == ["fw", "gap", "hw"]


def test_succession_and_trace():
    assert R.unit(3500, R.river_y(3500), R.river_z(3500) - 50) in (R.UNIT["schist"], R.UNIT["granite"])
    assert R.unit(7500, 2000, R.topo(7500, 2000) - 1) == R.UNIT["chalk"]
    xs = np.linspace(0, 1, 11)
    lines = R.trace(np.add.outer(xs * 0, xs), xs, xs, 0.55)   # field = x, level 0.55
    assert len(lines) == 1 and all(abs(x - 0.55) < 1e-12 for x, _ in lines[0])


def test_section_fault_stops_at_the_ground():
    # the section's fault line ends ON the ground profile, not above it
    out = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "out")
    rows = [l.split() for l in open(os.path.join(out, "shared-region-section-fault.dat"))][1:]
    (s_bot, z_bot), (s_top, z_top) = [(float(a), float(b)) for a, b in rows]
    a, b = R.SECTION_AB
    L = math.hypot(b[0] - a[0], b[1] - a[1])
    t = s_top * 1000 / L
    ground = R.topo(a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    assert abs(z_top - ground) < 1.0
    # dip 60 ESE seen obliquely along A-B: the fault rises westward up-section
    assert s_top < s_bot and z_top > z_bot
