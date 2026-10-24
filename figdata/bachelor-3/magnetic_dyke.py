"""Total-field magnetic anomaly of a buried two-dimensional dyke (Year 3, field and lab
methods III).

A 2-D body (infinitely long along strike) of uniform induced magnetisation M = kappa F /
mu0 along the main field. In the plane of a profile across strike (x along the profile,
z positive DOWN) only the components of M in that plane matter: the end faces at
infinity carry no field. The body is replaced by its surface "charges" sigma = M . n
(outward normal n) on the four faces of a rectangle x1 < x < x2, z1 < z < z2; a uniformly
charged straight segment has a closed-form 2-D field, H = sigma / (2 pi) * integral of
(r - r') / |r - r'|^2 dl. The anomaly field is Delta B = mu0 H, and the total-field
anomaly is its projection on the main-field direction, Delta T = Delta B . F_hat (the
change of |B| when the anomaly is small against F).

Geometry of the main field: inclination I (down positive), the profile at azimuth alpha
from magnetic north (alpha = 0 for a profile running north, i.e. an E-W strike; alpha =
90 deg for an E-W profile across a N-S strike). In the profile plane the field direction
is (cos I cos alpha, sin I) along (x, down).

Thin-dyke limit (width t, top at depth z, infinite depth extent, vertical): the top face
alone, a line of charge -M_z t; for a N-S strike Delta T = kappa F t sin^2 I z / (2 pi
(x^2 + z^2)): the anomaly falls to half its peak at x = z (tested).

The Varden dolerite dyke (Sync 3 ruling: allowed in Book 5's figdata only, buried and
confined to the basement below the unconformity; region.py unchanged): striking N-S at
x = DYKE_X, WIDTH thick, susceptibility KAPPA (inside the mafic range of ledger
gpg:susceptibility), its top the unconformity of region.py, which the dyke does not
cross. Field F_T at inclination I_DEG (a mid-latitude field: the IGRF of ch. 4).

  part generic   x_m  dT_I90  dT_I60  dT_I60ns      a dyke 20 m wide, top 100 m deep,
                                                     kappa 0.01, F 50000 nT: E-W strike at
                                                     I = 90 and 60 deg, N-S strike at 60
  part varden    x_km dT_nT                          the Varden profile (y = PROFILE_Y)
  part line      x_km t_min T_obs              the walked line (problem): stations every
                                                 50 m from 1.70 to 2.70 km, one every 2 min
                                                 from 10:00, total field = F_T + anomaly +
                                                 a daytime variation DIURNAL_AMP sin(pi t /
                                                 120 min) (exercise values; daily variations
                                                 20-50 nT in ledger gpg:mag-field), to 0.1 nT
  part base      t_min T_base                     the base-station record at the same minutes
  part values    what value
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

DEPTH_BOTTOM = 2.0e4     # m, the dyke's "infinite" depth extent in the generic model
# the Varden dyke (exercise values)
DYKE_X = 2200.0          # m, centre of the dyke (N-S strike)
WIDTH = 25.0             # m
KAPPA = 0.03             # SI, dolerite (mafic range of gpg:susceptibility)
F_T = 48000.0            # nT
I_DEG = 65.0             # deg
PROFILE_Y = 4150.0       # m, the E-W magnetic line, the same as the gravity profile
DIURNAL_AMP = 14.0       # nT
LINE_X = [1700.0 + 50.0 * i for i in range(21)]


def segment_field(p1, p2, sigma, xo, zo):
    """2-D field (Hx, Hz) at (xo, zo) of a straight segment p1 -> p2 carrying a uniform
    charge density sigma; z down; arrays broadcast. With s measured along the segment from
    the foot of the perpendicular and d the signed distance of its line,
    H = -(sigma / 2 pi) [u ln(r2 / r1) + n (atan(s2 / d) - atan(s1 / d))], the angle
    difference written with atan2 so that a station on the line's extension (d = 0)
    gives 0."""
    x1, z1 = p1
    x2, z2 = p2
    L = math.hypot(x2 - x1, z2 - z1)
    ux, uz = (x2 - x1) / L, (z2 - z1) / L
    nx, nz = -uz, ux
    dx, dz = x1 - np.asarray(xo, dtype=float), z1 - np.asarray(zo, dtype=float)
    s1 = dx * ux + dz * uz
    s2 = s1 + L
    d = dx * nx + dz * nz
    along = 0.5 * np.log((s2 * s2 + d * d) / (s1 * s1 + d * d))
    across = np.arctan2(d * (s2 - s1), d * d + s1 * s2)
    hx = -sigma / (2 * math.pi) * (along * ux + across * nx)
    hz = -sigma / (2 * math.pi) * (along * uz + across * nz)
    return hx, hz


def field_direction(inc_deg, alpha_deg):
    """Unit vector of the main field in the profile plane, (along x, down), and the
    full 3-D unit vector's components there (the along-strike part does not enter)."""
    i, a = math.radians(inc_deg), math.radians(alpha_deg)
    return math.cos(i) * math.cos(a), math.sin(i)


def prism_dT(x1, x2, z1, z2, kappa, f_nt, inc_deg, alpha_deg, xo, zo=0.0):
    """Total-field anomaly (nT) of a 2-D rectangular body, induced magnetisation only."""
    fx, fz = field_direction(inc_deg, alpha_deg)
    # mu0 M = kappa F (in nT); work with mu0 * charge so that mu0 H comes out in nT
    mx, mz = kappa * f_nt * fx, kappa * f_nt * fz
    faces = [((x1, z1), (x2, z1), -mz),     # top, outward normal up (-z)
             ((x2, z2), (x1, z2), mz),      # bottom
             ((x1, z2), (x1, z1), -mx),     # west face, outward normal -x
             ((x2, z1), (x2, z2), mx)]      # east face
    bx = np.zeros_like(np.asarray(xo, dtype=float))
    bz = np.zeros_like(bx)
    for p1, p2, sig in faces:
        if sig == 0.0:
            continue
        hx, hz = segment_field(p1, p2, sig, xo, zo)
        bx = bx + hx
        bz = bz + hz
    return bx * fx + bz * fz


def thin_dyke_dT(x, z, t, kappa, f_nt, inc_deg):
    """Thin vertical dyke, N-S strike, infinite depth extent: the line-pole formula."""
    s = math.sin(math.radians(inc_deg))
    return kappa * f_nt * t * s * s * z / (2 * math.pi * (x * x + z * z))


def half_width(xs, ys):
    """Half of the full width at half the peak (positive peak), linear interpolation."""
    ys = np.asarray(ys)
    k = int(np.argmax(ys))
    half = ys[k] / 2.0

    def cross(rng):
        for i in rng:
            a, b = ys[i], ys[i + 1]
            if (a - half) * (b - half) <= 0 and a != b:
                return xs[i] + (half - a) / (b - a) * (xs[i + 1] - xs[i])
        return math.nan
    left = cross(range(k - 1, -1, -1))
    right = cross(range(k, len(ys) - 1))
    return 0.5 * (right - left), xs[k], ys[k]


def varden_dyke():
    """Top elevation, ground elevation and depth of the top of the Varden dyke on the
    profile, from region.py (the top is the unconformity)."""
    top = region.base_cover(DYKE_X, PROFILE_Y)
    ground = region.topo(DYKE_X, PROFILE_Y)
    return top, ground, ground - top


def varden_profile(xs):
    """Total-field anomaly along the Varden line; stations on the ground (their height
    above the dyke top varies with the topography)."""
    top, _, _ = varden_dyke()
    zo = np.array([-region.topo(x, PROFILE_Y) for x in xs])     # z down: station at -elevation
    return prism_dT(DYKE_X - WIDTH / 2, DYKE_X + WIDTH / 2, -top, DEPTH_BOTTOM, KAPPA, F_T,
                    I_DEG, 90.0, np.asarray(xs, dtype=float), zo)


def diurnal(t_min):
    return DIURNAL_AMP * math.sin(math.pi * t_min / 120.0)


def line_readings():
    """[(x, t, T_obs)] and [(t, T_base)] of the walked line."""
    dT = varden_profile(LINE_X)
    line = [(x, 2.0 * i, round(F_T + d + diurnal(2.0 * i), 1)) for i, (x, d) in enumerate(zip(LINE_X, dT))]
    base = [(t, round(F_T + diurnal(t), 1)) for _, t, _ in line]
    return line, base


def main():
    xs = np.arange(-600.0, 600.1, 5.0)
    g90 = prism_dT(-10, 10, 100, DEPTH_BOTTOM, 0.01, 50000, 90, 0, xs)
    g60 = prism_dT(-10, 10, 100, DEPTH_BOTTOM, 0.01, 50000, 60, 0, xs)
    g60ns = prism_dT(-10, 10, 100, DEPTH_BOTTOM, 0.01, 50000, 60, 90, xs)
    write_table(__file__, ("x_m", "dT_I90", "dT_I60", "dT_I60ns"),
                list(zip(xs, g90, g60, g60ns)), part="generic")
    vx = np.arange(1200.0, 3200.1, 10.0)
    vt = varden_profile(vx)
    write_table(__file__, ("x_km", "dT_nT"), [(x / 1000, t) for x, t in zip(vx, vt)],
                part="varden")
    line, base = line_readings()
    write_table(__file__, ("x_km", "t_min", "T_obs"), [(x / 1000, t, v) for x, t, v in line],
                part="line", digits=7)
    write_table(__file__, ("t_min", "T_base"), base, part="base", digits=7)
    top, ground, depth = varden_dyke()
    xh, xpk, pk = half_width(vx, vt)
    vals = [["dyke_x_m", DYKE_X], ["width_m", WIDTH], ["kappa", KAPPA], ["F_nT", F_T],
            ["I_deg", I_DEG], ["top_elev_m", top], ["ground_m", ground], ["top_depth_m", depth],
            ["peak_nT", pk], ["peak_x_km", xpk / 1000], ["half_width_m", xh],
            ["thin_peak_nT", thin_dyke_dT(0.0, depth, WIDTH, KAPPA, F_T, I_DEG)],
            ["generic_I90_peak", float(g90.max())], ["generic_I60_max", float(g60.max())],
            ["generic_I60_min", float(g60.min())], ["generic_I60ns_peak", float(g60ns.max())]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
