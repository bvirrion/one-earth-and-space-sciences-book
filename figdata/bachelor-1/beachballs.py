"""Focal mechanisms drawn as beach balls (Year 1, earthquake-source).

Vectors are written in (east, north, up) components. A plane of strike phi and
dip delta (right-hand rule: it dips toward phi + 90) has
  the strike vector     s = (sin phi, cos phi, 0),
  the up-dip vector     u = (-cos delta sin a, -cos delta cos a, sin delta), a = phi + 90,
  the upward normal     n = (sin delta sin a, sin delta cos a, cos delta),
and the slip of the hanging wall relative to the footwall, of rake r, is the unit
vector d = cos r s + sin r u (the convention of the chapter on faults).

For a slip d on a plane of normal n, the first motion of the P wave leaving the
source in the direction x is a push (compression) where (n.x)(d.x) > 0 and a pull
where (n.x)(d.x) < 0. The two nodal planes are the planes of normals n and d; the
P and T axes are (n - d)/sqrt 2 and (n + d)/sqrt 2.

A direction x pointing into the lower hemisphere (up component U <= 0) is drawn
on the equal-area projection at
  (X, Y) = (E, N) / sqrt(1 - U),
which puts the vertical at the centre and the horizontal on the unit circle, at
radius sqrt 2 sin(theta / 2) for an angle theta from the vertical.

The two compressional quadrants are spherical lunes between the null axis
b = n x d and -b; each is written as a closed polygon clipped to the lower
hemisphere, the clipped part of its outline following the unit circle.

  part <name>-c1, <name>-c2  X Y    compressional regions (may be empty)
  part <name>-p1, <name>-p2  X Y    the two nodal planes
  part <name>-P, <name>-T  X Y     where to print the letters P and T: the projected
                                   axis, pulled in to radius LABEL_RMAX at most
  part values  what value          the auxiliary planes, and the axes' trend/plunge
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

# strike, dip, rake in degrees
MECHANISMS = {
    "normal": (0.0, 60.0, -90.0),
    "reverse": (0.0, 30.0, 90.0),
    "strikeslip": (0.0, 90.0, 180.0),
    # Tohoku 2011: USGS W-phase moment tensor (ledger usgs:tohoku-mt)
    "tohoku": (192.0, 8.0, 78.0),
}
EPS = 1e-9
LABEL_RMAX = 0.8


def _r(x):
    return math.radians(x)


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def unit(a):
    m = math.sqrt(dot(a, a))
    return (a[0] / m, a[1] / m, a[2] / m)


def plane_vectors(strike, dip):
    """Strike vector, up-dip vector and upward normal of a plane."""
    p, d, a = _r(strike), _r(dip), _r(strike + 90.0)
    s = (math.sin(p), math.cos(p), 0.0)
    u = (-math.cos(d) * math.sin(a), -math.cos(d) * math.cos(a), math.sin(d))
    n = (math.sin(d) * math.sin(a), math.sin(d) * math.cos(a), math.cos(d))
    return s, u, n


def normal_and_slip(strike, dip, rake):
    s, u, n = plane_vectors(strike, dip)
    r = _r(rake)
    d = tuple(math.cos(r) * s[i] + math.sin(r) * u[i] for i in range(3))
    return n, d


def plane_from_normal_and_slip(n, d):
    """Strike, dip, rake of the plane of normal n with slip d (the pair may be flipped)."""
    if n[2] < 0 or (abs(n[2]) < EPS and (n[0] < 0 or (abs(n[0]) < EPS and n[1] < 0))):
        n, d = tuple(-c for c in n), tuple(-c for c in d)
    dip = math.degrees(math.acos(max(-1.0, min(1.0, n[2]))))
    dipdir = math.degrees(math.atan2(n[0], n[1])) % 360.0
    strike = (dipdir - 90.0) % 360.0
    s, u, _ = plane_vectors(strike, dip)
    rake = math.degrees(math.atan2(dot(d, u), dot(d, s)))
    return strike, dip, rake


def auxiliary_plane(strike, dip, rake):
    """The other nodal plane: its normal is the slip, its slip the normal."""
    n, d = normal_and_slip(strike, dip, rake)
    return plane_from_normal_and_slip(d, n)


def trend_plunge(x):
    """Trend and plunge of a line, taken pointing downward."""
    if x[2] > 0:
        x = tuple(-c for c in x)
    trend = math.degrees(math.atan2(x[0], x[1])) % 360.0
    plunge = math.degrees(math.asin(max(-1.0, min(1.0, -x[2]))))
    return trend, plunge


def pt_axes(strike, dip, rake):
    n, d = normal_and_slip(strike, dip, rake)
    p = unit(tuple(n[i] - d[i] for i in range(3)))
    t = unit(tuple(n[i] + d[i] for i in range(3)))
    return p, t


def first_motion(strike, dip, rake, x):
    """+1 for a push (compression), -1 for a pull, 0 on a nodal plane."""
    n, d = normal_and_slip(strike, dip, rake)
    v = dot(n, x) * dot(d, x)
    return 0 if abs(v) < 1e-12 else (1 if v > 0 else -1)


def project(x):
    """Lower-hemisphere equal-area projection of a unit vector (taken pointing down;
    a vector on the horizon, within EPS, is kept as it is)."""
    if x[2] > EPS:
        x = tuple(-c for c in x)
    f = 1.0 / math.sqrt(1.0 - min(x[2], 0.0))
    return x[0] * f, x[1] * f


def label_point(x, rmax=LABEL_RMAX):
    """Where to print the letter of an axis: its projection, moved toward the centre
    to the radius rmax at most so that the letter stays inside the ball."""
    X, Y = project(x)
    r = math.hypot(X, Y)
    return (X, Y) if r <= rmax else (X * rmax / r, Y * rmax / r)


def nodal_curve(normal, n=91):
    """The lower half of the great circle of a plane of given normal, projected."""
    st, dp, _ = plane_from_normal_and_slip(normal, (1.0, 0.0, 0.0))
    s, u, _ = plane_vectors(st, dp)
    w = tuple(-c for c in u)                    # down-dip
    pts = []
    for i in range(n):
        t = math.pi * i / (n - 1)
        x = tuple(math.cos(t) * s[k] + math.sin(t) * w[k] for k in range(3))
        pts.append(project(x))
    return pts


def _lune(n, d, m=90):
    """Closed outline of {n.x >= 0, d.x >= 0}: from b to -b through n, back through d."""
    b = unit(cross(n, d))
    out = []
    for i in range(m + 1):
        t = math.pi * i / m
        out.append(tuple(math.cos(t) * b[k] + math.sin(t) * n[k] for k in range(3)))
    for i in range(m, -1, -1):
        t = math.pi * i / m
        out.append(tuple(math.cos(t) * b[k] + math.sin(t) * d[k] for k in range(3)))
    return out


def _horizon_arc(p, q, inside, m=60):
    """Points of the horizon from p to q (both on it), along the arc where inside() holds."""
    a0 = math.atan2(p[1], p[0])
    a1 = math.atan2(q[1], q[0])
    ccw = (a1 - a0) % (2 * math.pi)
    cw = ccw - 2 * math.pi
    for span in (ccw, cw):
        mid = a0 + span / 2
        if inside((math.cos(mid), math.sin(mid), 0.0)):
            break
    else:
        return []                       # the region only touches the horizon
    k = max(2, int(abs(span) / (2 * math.pi) * 4 * m))
    return [(math.cos(a0 + span * i / k), math.sin(a0 + span * i / k), 0.0) for i in range(1, k)]


def compressional_regions(strike, dip, rake):
    """The projected outlines of the two compressional quadrants (lists of (X, Y))."""
    n, d = normal_and_slip(strike, dip, rake)
    regions = []
    for sign in (1.0, -1.0):
        ns = tuple(sign * c for c in n)
        ds = tuple(sign * c for c in d)

        def inside(x, ns=ns, ds=ds):
            return dot(ns, x) > -1e-9 and dot(ds, x) > -1e-9

        ring = _lune(ns, ds)
        clipped = []                        # Sutherland-Hodgman against U <= 0
        for i in range(len(ring)):
            a, b = ring[i - 1], ring[i]
            ain, bin_ = a[2] <= EPS, b[2] <= EPS
            if bin_:
                if not ain:
                    t = a[2] / (a[2] - b[2])
                    clipped.append(unit(tuple(a[k] + t * (b[k] - a[k]) for k in range(3))))
                clipped.append(b)
            elif ain:
                t = a[2] / (a[2] - b[2])
                clipped.append(unit(tuple(a[k] + t * (b[k] - a[k]) for k in range(3))))
        if len(clipped) < 3:
            continue
        # replace straight jumps between two horizon points by the arc of the horizon
        poly = []
        for i in range(len(clipped)):
            a, b = clipped[i - 1], clipped[i]
            if abs(a[2]) < 1e-7 and abs(b[2]) < 1e-7 and dot(a, b) < math.cos(_r(3.0)):
                poly.extend(_horizon_arc(a, b, inside))
            poly.append(b)
        pts = [project(x) for x in poly]
        area = 0.5 * sum(pts[i - 1][0] * pts[i][1] - pts[i][0] * pts[i - 1][1] for i in range(len(pts)))
        if abs(area) > 1e-6:
            regions.append(pts)
    return regions


def main():
    values = []
    for name, (st, dp, rk) in MECHANISMS.items():
        regs = compressional_regions(st, dp, rk)
        for i in range(2):
            rows = regs[i] + [regs[i][0]] if i < len(regs) else []
            write_table(__file__, ("X", "Y"), rows, part="%s-c%d" % (name, i + 1))
        n, d = normal_and_slip(st, dp, rk)
        write_table(__file__, ("X", "Y"), nodal_curve(n), part="%s-p1" % name)
        write_table(__file__, ("X", "Y"), nodal_curve(d), part="%s-p2" % name)
        p, t = pt_axes(st, dp, rk)
        write_table(__file__, ("X", "Y"), [label_point(p)], part="%s-P" % name)
        write_table(__file__, ("X", "Y"), [label_point(t)], part="%s-T" % name)
        a = auxiliary_plane(st, dp, rk)
        values += [("%s_aux_strike" % name, a[0]), ("%s_aux_dip" % name, a[1]),
                   ("%s_aux_rake" % name, a[2])]
        for lab, v in (("P", p), ("T", t)):
            tr, pl = trend_plunge(v)
            values += [("%s_%s_trend" % (name, lab), tr), ("%s_%s_plunge" % (name, lab), pl)]
    values = [(k, round(v, 6) + 0.0) for k, v in values]     # no -1e-15 noise
    write_table(__file__, ("what", "value"), values, part="values")


if __name__ == "__main__":
    main()
