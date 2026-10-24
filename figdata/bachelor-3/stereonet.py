"""Stereonets, the pi-diagram of the Varden folds and the palaeostress of the
Varden faults (Year 3, structural analysis).

Vectors are (east, north, up). A line of trend t and plunge p (downward) is
    v = (cos p sin t, cos p cos t, -sin p);
lower-hemisphere projection, primitive radius 1, theta = 90 - p from the nadir:
    equal-angle (Wulff):    r = tan(theta / 2)
    equal-area (Schmidt):   r = sqrt(2) sin(theta / 2)
    point = (r sin t, r cos t).
A plane of dip direction a and dip d has the upward normal
    n = (sin d sin a, sin d cos a, cos d)       (Book 3's convention)
and its pole is the downward normal -n.

Varden data (invented; figdata/shared/region.py read only): the limbs dip
LIMB_DIP = 12 deg east and west of the N-S axes, with the PLUNGE = 2 deg
northward component, so each limb has the attitude region.limb_attitude(x);
twelve field readings are those attitudes plus fixed scatter, rounded to the
degree. Faults: the Varden normal fault (120/60, dip slip) and four small
faults whose slip is the Wallace-Bott direction of the reduced stress
sigma1 vertical, sigma3 horizontal toward 120, stress ratio PHI_TRUE, with the
measured rakes rounded to the degree (rake from the strike, positive when
the hanging wall moves up).

  part wulff, schmidt   x y   nets: great circles (N-S strike, dips every 10 deg)
                              and small circles about the N-S axis, nan-separated
  part poles            x y   the twelve limb poles (Schmidt)
  part girdle           x y   best-fit great circle of the poles
  part beta             x y   the beta axis
  part limbs            x y   great circles of the two mean limb planes, nan-separated
  part faults           x y   the five fault planes (great circles), nan-separated
  part slips            x y   the slip lineations (points)
  part s1, s2, s3       x y   the principal stress axes (Schmidt; horizontal ones at both ends)
  part values           what value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import region  # noqa: E402

NAN = float("nan")
PHI_TRUE = 0.3
SIGMA3_TREND = 120.0

# fixed scatter of the readings (deg): dip-direction and dip offsets
SCATTER_E = [(-6, 1.0), (3, -1.5), (8, 0.5), (-2, 2.0), (5, -0.5), (-9, -1.0)]
SCATTER_W = [(4, -1.0), (-7, 0.5), (2, 1.5), (9, -2.0), (-3, 1.0), (-5, 0.0)]
SMALL_FAULTS = [(150.0, 55.0), (90.0, 65.0), (200.0, 70.0), (60.0, 50.0)]


def line_vec(trend, plunge):
    t, p = math.radians(trend), math.radians(plunge)
    return np.array([math.cos(p) * math.sin(t), math.cos(p) * math.cos(t), -math.sin(p)])


def vec_line(v):
    v = np.asarray(v, dtype=float)
    v = v / np.linalg.norm(v)
    if v[2] > 1e-12:
        v = -v
    return math.degrees(math.atan2(v[0], v[1])) % 360.0, math.degrees(math.asin(max(-1.0, min(1.0, -v[2]))))


def normal(dipdir, dip):
    a, d = math.radians(dipdir), math.radians(dip)
    return np.array([math.sin(d) * math.sin(a), math.sin(d) * math.cos(a), math.cos(d)])


def project(v, kind="schmidt"):
    trend, plunge = vec_line(v)
    th = math.radians(90.0 - plunge)
    r = math.tan(th / 2) if kind == "wulff" else math.sqrt(2) * math.sin(th / 2)
    t = math.radians(trend)
    return r * math.sin(t), r * math.cos(t)


def plane_lines(dipdir, dip, n=91):
    a, d = math.radians(dipdir), math.radians(dip)
    s = np.array([math.sin(a - math.pi / 2), math.cos(a - math.pi / 2), 0.0])
    dv = np.array([math.sin(a) * math.cos(d), math.cos(a) * math.cos(d), -math.sin(d)])
    return [math.cos(u) * s + math.sin(u) * dv for u in np.linspace(0.0, math.pi, n)]


def great_circle(dipdir, dip, kind="schmidt", n=91):
    return [project(v, kind) for v in plane_lines(dipdir, dip, n)]


def small_circle_ns(cone, kind, n=91):
    """Lines at the angle `cone` (deg) from the north horizontal axis, lower hemisphere."""
    c = math.radians(cone)
    pts = []
    for u in np.linspace(0.0, math.pi, n):
        v = np.array([math.sin(c) * math.cos(u), math.cos(c), -math.sin(c) * math.sin(u)])
        pts.append(project(v, kind))
    return pts


def net(kind):
    rows = []
    for dip in range(10, 90, 10):
        for dd in (90.0, 270.0):
            rows += great_circle(dd, dip, kind) + [(NAN, NAN)]
    for cone in range(10, 90, 10):
        for sgn in (1, -1):
            pts = small_circle_ns(cone, kind)
            rows += [(x, sgn * y) for x, y in pts] + [(NAN, NAN)]
    rows += [(0.0, -1.0), (0.0, 1.0), (NAN, NAN)]     # N-S diameter (vertical plane)
    return rows


def readings():
    """The twelve limb readings (dip direction, dip), rounded to the degree."""
    east = region.limb_attitude(region.AXIS_ANTI + 1000.0)
    west = region.limb_attitude(region.AXIS_ANTI - 1000.0)
    out = []
    for (a0, d0), sc in ((east, SCATTER_E), (west, SCATTER_W)):
        for da, dd in sc:
            out.append((round(a0 + da) % 360, round(d0 + dd)))
    return out


def orientation_tensor(vectors):
    v = np.array([u / np.linalg.norm(u) for u in vectors])
    return v.T @ v / len(v)


def beta_from_tensor(vectors):
    w, e = np.linalg.eigh(orientation_tensor(vectors))
    return w, e[:, 0]


def beta_from_means(reads):
    """Beta axis as the cross product of the mean poles of the two limbs."""
    n = [normal(a, d) for a, d in reads]
    me = np.sum(n[:6], axis=0)
    mw = np.sum(n[6:], axis=0)
    return np.cross(me, mw)


# --- palaeostress -----------------------------------------------------------
def reduced_stress(phi=PHI_TRUE, s3_trend=SIGMA3_TREND):
    """Reduced stress tensor: sigma1 = 1 vertical, sigma2 = phi, sigma3 = 0
    horizontal toward s3_trend (compression positive)."""
    e1 = np.array([0.0, 0.0, 1.0])
    e3 = line_vec(s3_trend, 0.0)
    e2 = np.cross(e1, e3)
    return np.outer(e1, e1) + phi * np.outer(e2, e2)


def shear_direction(s, n):
    """Resolved shear traction on the plane of unit normal n."""
    t = s @ n
    return t - (n @ t) * n


def hanging_wall_slip(s, dipdir, dip):
    """Unit slip vector of the hanging wall (Wallace-Bott). With compression
    positive, the shear traction on the plane of upward normal n is
    tau = S n - (n.S n) n, and the hanging wall moves along -tau (checked:
    sigma1 vertical gives a normal fault, sigma1 horizontal across the strike
    a reverse fault)."""
    v = -shear_direction(s, normal(dipdir, dip))
    return v / np.linalg.norm(v)


def phi_from_rake(dipdir, dip, rk, s3_trend=SIGMA3_TREND):
    """Stress ratio from one measured rake, the principal directions being
    known: tau = tau0 + phi tau1 is linear in phi, and it must be parallel
    to the slip u, so (tau0 + phi tau1).w = 0 with w = n x u."""
    n = normal(dipdir, dip)
    u = slip_from_rake(dipdir, dip, rk)
    w = np.cross(n, u)
    t0 = shear_direction(reduced_stress(0.0, s3_trend), n)
    t1 = shear_direction(reduced_stress(1.0, s3_trend), n) - t0
    return -float(t0 @ w) / float(t1 @ w)


def rake(dipdir, dip, slip):
    """Rake (deg) of the hanging wall's slip vector, measured in the plane from
    the strike (dip direction - 90, right-hand rule), positive when the hanging
    wall moves up (Book 3's convention: -90 normal, +90 reverse)."""
    a, d = math.radians(dipdir), math.radians(dip)
    s = np.array([math.sin(a - math.pi / 2), math.cos(a - math.pi / 2), 0.0])
    dv = np.array([math.sin(a) * math.cos(d), math.cos(a) * math.cos(d), -math.sin(d)])
    return math.degrees(math.atan2(-np.dot(slip, dv), np.dot(slip, s)))


def slip_from_rake(dipdir, dip, rk):
    a, d, r = math.radians(dipdir), math.radians(dip), math.radians(rk)
    s = np.array([math.sin(a - math.pi / 2), math.cos(a - math.pi / 2), 0.0])
    dv = np.array([math.sin(a) * math.cos(d), math.cos(a) * math.cos(d), -math.sin(d)])
    return math.cos(r) * s - math.sin(r) * dv


def faults():
    """(dip direction, dip, measured rake) of the Varden fault and four small faults."""
    s = reduced_stress()
    out = []
    for dd, dp in [(region.FAULT_DIP_AZ, region.FAULT_DIP)] + SMALL_FAULTS:
        out.append((dd, dp, round(rake(dd, dp, hanging_wall_slip(s, dd, dp)))))
    return out


def misfit(phi, s3_trend, data):
    s = reduced_stress(phi, s3_trend)
    tot = 0.0
    for dd, dp, rk in data:
        pred = hanging_wall_slip(s, dd, dp)
        obs = slip_from_rake(dd, dp, rk)
        tot += math.degrees(math.acos(max(-1.0, min(1.0, float(np.dot(pred, obs)))))) ** 2
    return math.sqrt(tot / len(data))


def invert(data):
    best = None
    for phi in np.arange(0.0, 1.0001, 0.01):
        for tr in np.arange(90.0, 150.01, 1.0):
            m = misfit(phi, tr, data)
            if best is None or m < best[0]:
                best = (m, phi, tr)
    return best


if __name__ == "__main__":
    write_table(__file__, ("x", "y"), net("wulff"), part="wulff")
    write_table(__file__, ("x", "y"), net("schmidt"), part="schmidt")
    reads = readings()
    poles = [-normal(a, d) for a, d in reads]
    write_table(__file__, ("x", "y"), [project(p) for p in poles], part="poles")
    w, b = beta_from_tensor(poles)
    btr, bpl = vec_line(b)
    gd, gdip = (btr + 180.0) % 360.0, 90.0 - bpl    # the girdle is the plane normal to beta
    write_table(__file__, ("x", "y"), great_circle(gd, gdip), part="girdle")
    write_table(__file__, ("x", "y"), [project(b)], part="beta")
    fl = faults()
    rows, slips = [], []
    for dd, dp, rk in fl:
        rows += great_circle(dd, dp) + [(NAN, NAN)]
        slips.append(project(slip_from_rake(dd, dp, rk)))
    write_table(__file__, ("x", "y"), rows, part="faults")
    write_table(__file__, ("x", "y"), slips, part="slips")
    write_table(__file__, ("x", "y"), [project(line_vec(0.0, 90.0))], part="s1")
    write_table(__file__, ("x", "y"), [project(line_vec(SIGMA3_TREND - 90.0, 0.0)),
                                       project(line_vec(SIGMA3_TREND + 90.0, 0.0))], part="s2")
    write_table(__file__, ("x", "y"), [project(line_vec(SIGMA3_TREND, 0.0)),
                                       project(line_vec(SIGMA3_TREND + 180.0, 0.0))], part="s3")
    rows = []
    for half in (reads[:6], reads[6:]):
        m = np.sum([normal(a, d) for a, d in half], axis=0)
        mdd = math.degrees(math.atan2(m[0], m[1])) % 360.0
        mdip = math.degrees(math.acos(m[2] / np.linalg.norm(m)))
        rows += great_circle(mdd, mdip) + [(NAN, NAN)]
    write_table(__file__, ("x", "y"), rows, part="limbs")
    bm = beta_from_means(reads)
    mtr, mpl = vec_line(bm)
    inv = invert(fl)
    vals = [("beta_tensor_trend", btr), ("beta_tensor_plunge", bpl),
            ("beta_means_trend", mtr), ("beta_means_plunge", mpl),
            ("lambda1", w[2]), ("lambda2", w[1]), ("lambda3", w[0]),
            ("inv_misfit", inv[0]), ("inv_phi", inv[1]), ("inv_s3_trend", inv[2])]
    vals += [("reading_%d" % i, "%d/%d" % r) for i, r in enumerate(reads)]
    vals += [("fault_%d" % i, "%d/%d/%d" % f) for i, f in enumerate(fl)]
    write_table(__file__, ("what", "value"), vals, part="values")
