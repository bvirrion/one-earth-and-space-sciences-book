"""The gravity anomaly of the Varden granite (Year 3, field and lab methods III).

The body is the granite of the series' invented region (figdata/shared/region.py, used
read-only): elliptical in plan (centre 3500, 4150 m; semi-axes 380 m east and 560 m
north at the unconformity), widening downward by the factor 1 + depth/4000 below the
unconformity, as region.unit() defines it. region.py gives the granite no floor: this
chapter's survey model stops it at FLOOR (elevation, metres), an assumption of the
exercise. Its top is the unconformity, or the ground where the valley has cut into it.

Density contrast DRHO = -130 kg/m3: a granite of 2620 kg/m3 in a schist of 2750 kg/m3,
both inside the published ranges (granite 2.50-2.81, schist 2.39-2.80 g/cm3, ledger
gpg:densities; granitic plutons average 2.69, below 2.6 for high-silica granite, ledger
usgs91:sierra). The anomaly is the residual of the granite alone (the effect of the
sedimentary cover and the Bouguer and terrain corrections are taken as removed).

The body is cut into right rectangular prisms (CELL x CELL in plan, LAYER thick); the
vertical attraction of each prism is the closed-form expression for a rectangular prism
(sum over its eight corners of x ln(y + r) + y ln(x + r) - z atan(xy / zr)), evaluated at
stations on the ground surface. Tested against a point mass far away, a wide flat
prism against the Bouguer slab 2 pi G drho t, and the on-axis vertical cylinder.

  part map       x_km y_km dg_mGal            100-m grid around the granite
  part contours  x_km y_km level              contour lines of the map (nan rows separate)
  part stations  x_km y_km                    the survey grid stations (200 m)
  part profile   x_km dg_mGal sphere cyl      E-W line through the centre (y = 4150 m):
                                               the anomaly, the equivalent sphere from the
                                               half-width rule, the vertical cylinder of
                                               equal-area radius with the true top and floor
  part loop      x_km t_h h_m reading          a gravity loop on the profile (problem): the
                                               base station at BASE_X, read at 09:00 and
                                               11:00; readings in mGal = model anomaly
                                               - (0.3086 - 0.1119) x height above the base +
                                               linear drift DRIFT + a semi-diurnal tide of
                                               amplitude TIDE_AMP (exercise values; tides up
                                               to 0.3 mGal in ledger gpg:grav-sizes)
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

G = 6.67430e-11          # const:G
SI_TO_MGAL = 1e5         # 1 mGal = 1e-5 m/s2
DRHO = -130.0            # kg/m3, granite minus schist (exercise value, within gpg:densities)
FLOOR = -1500.0          # m, elevation of the granite floor (exercise assumption)
CELL = 50.0              # m, prism size in plan
LAYER = 100.0            # m, prism thickness
GX, GY, GA, GB = region.GRANITE
Y_LINE = 4150.0          # m, the E-W profile through the centre
BASE_X = 2000.0          # m, the base station of the loop
R0 = 2846.512            # mGal, the first base reading (arbitrary dial origin)
DRIFT = 0.040            # mGal/h, spring drift
TIDE_AMP = 0.12          # mGal
FA_MINUS_B = 0.3086 - 0.04191 * 2.67     # mGal/m, free-air minus Bouguer (2670 kg/m3)
LOOP = [(2000.0, 0.0), (3000.0, 0.5), (3500.0, 0.9), (4000.0, 1.3), (2000.0, 2.0)]


# --- prisms ---------------------------------------------------------------------------
def prism_gz(x1, x2, y1, y2, z1, z2, xo, yo, zo, drho):
    """Vertical attraction (m/s2, positive downward) at (xo, yo, zo) of a prism of density
    contrast drho; z is ELEVATION (up), z1 < z2. Arrays broadcast."""
    total = 0.0
    for i, xa in enumerate((x1, x2)):
        for j, ya in enumerate((y1, y2)):
            for k, za in enumerate((z1, z2)):
                x = np.asarray(xa - xo, dtype=float)
                y = np.asarray(ya - yo, dtype=float)
                z = np.asarray(zo - za, dtype=float)      # depth of the corner below the station
                r = np.sqrt(x * x + y * y + z * z)
                s = (-1) ** (i + j + k)
                with np.errstate(divide="ignore", invalid="ignore"):
                    term = (x * np.log(np.where(y + r > 0, y + r, 1e-300))
                            + y * np.log(np.where(x + r > 0, x + r, 1e-300))
                            - z * np.arctan2(x * y, z * r))
                total = total + s * term
    return -G * drho * total


def point_gz(m, x, z):
    """Point mass m at depth z, horizontal distance x."""
    return G * m * z / (x * x + z * z) ** 1.5


def sphere_from_halfwidth(peak, x_half):
    """Equivalent sphere: centre depth z = x_half / sqrt(2^(2/3) - 1) = 1.305 x_half, and the
    excess mass that gives the peak."""
    z = x_half / math.sqrt(2 ** (2.0 / 3.0) - 1.0)
    return z, peak * z * z / G


def vcyl_axis(radius, z_top, z_bot, drho):
    """On-axis attraction of a vertical cylinder whose top and bottom are at depths
    z_top < z_bot below the station."""
    return 2 * math.pi * G * drho * ((z_bot - z_top) + math.hypot(z_top, radius)
                                      - math.hypot(z_bot, radius))


def vcyl_profile(x, radius, z_top, z_bot, drho, n=24):
    """Off-axis attraction of a vertical cylinder by summing vertical prisms on a fine
    square grid inside the circle (used only to draw the model curve)."""
    h = 2 * radius / n
    out = np.zeros_like(np.asarray(x, dtype=float))
    for i in range(n):
        for j in range(n):
            cx = -radius + (i + 0.5) * h
            cy = -radius + (j + 0.5) * h
            if cx * cx + cy * cy <= radius * radius:
                out = out + prism_gz(cx - h / 2, cx + h / 2, cy - h / 2, cy + h / 2,
                                     -z_bot, -z_top, x, 0.0, 0.0, drho)
    return out


# --- the Varden granite ------------------------------------------------------------------
def granite_prisms(cell=CELL, layer=LAYER, floor=FLOOR):
    """[(x1, x2, y1, y2, z1, z2)] filling the granite between its top and the floor."""
    out = []
    smax = 1.0 + (region.Z_AXIS + 50.0 - floor) / 4000.0
    xs = np.arange(GX - GA * smax - cell, GX + GA * smax + cell, cell)
    ys = np.arange(GY - GB * smax - cell, GY + GB * smax + cell, cell)
    for x in xs:
        for y in ys:
            xc, yc = x + cell / 2, y + cell / 2
            zb = region.base_cover(xc, yc)
            top = min(zb, region.topo(xc, yc))
            r0 = ((xc - GX) / GA) ** 2 + ((yc - GY) / GB) ** 2
            z = top
            while z > floor + 1e-6:
                z_lo = max(z - layer, floor)
                zm = 0.5 * (z + z_lo)
                if r0 <= 1.0 + (zb - zm) / 4000.0:
                    out.append((x, x + cell, y, y + cell, z_lo, z))
                z = z_lo
    return out


def anomaly(prisms, xo, yo, zo, drho=DRHO):
    p = np.array(prisms)
    xo, yo, zo = (np.asarray(v, dtype=float) for v in (xo, yo, zo))
    g = np.zeros(xo.shape)
    for chunk in range(0, len(p), 400):
        q = p[chunk:chunk + 400]
        g += prism_gz(q[:, 0][:, None], q[:, 1][:, None], q[:, 2][:, None], q[:, 3][:, None],
                      q[:, 4][:, None], q[:, 5][:, None], xo[None, :], yo[None, :],
                      zo[None, :], drho).sum(axis=0)
    return g


def half_width(xs, gs):
    """Half of the full width at half the extreme value (linear interpolation)."""
    gs = np.asarray(gs)
    k = int(np.argmax(np.abs(gs)))
    half = gs[k] / 2.0
    def cross(rng):
        for i in rng:
            a, b = gs[i], gs[i + 1]
            if (abs(a) - abs(half)) * (abs(b) - abs(half)) <= 0 and a != b:
                return xs[i] + (half - a) / (b - a) * (xs[i + 1] - xs[i])
        return math.nan
    left = cross(range(k - 1, -1, -1))
    right = cross(range(k, len(gs) - 1))
    return 0.5 * (right - left), xs[k], gs[k]


def body_stats(prisms, drho=DRHO):
    vol = sum((p[1] - p[0]) * (p[3] - p[2]) * (p[5] - p[4]) for p in prisms)
    zc = sum((p[1] - p[0]) * (p[3] - p[2]) * (p[5] - p[4]) * 0.5 * (p[4] + p[5])
             for p in prisms) / vol
    return vol, drho * vol, zc


def tide(t_h):
    return TIDE_AMP * math.sin(2 * math.pi * (t_h - 1.0) / 12.42)


def loop_readings(prisms):
    """[(x, t, h, reading, true anomaly relative to the base)] of the gravity loop."""
    hb = region.topo(BASE_X, Y_LINE)
    xs = np.array([x for x, _ in LOOP])
    hs = np.array([region.topo(x, Y_LINE) for x in xs])
    g = anomaly(prisms, xs, np.full_like(xs, Y_LINE), hs) * SI_TO_MGAL
    gb = g[0]
    out = []
    for (x, t), h, gx in zip(LOOP, hs, g):
        r = R0 + (gx - gb) - FA_MINUS_B * (h - hb) + DRIFT * t + tide(t) - tide(0.0)
        out.append((x, t, round(h, 1), round(r, 3), gx - gb))
    return out


def main():
    prisms = granite_prisms()
    vol, mass, zc = body_stats(prisms)
    # map
    xs = np.arange(1.8, 5.21, 0.1) * 1000
    ys = np.arange(2.6, 5.71, 0.1) * 1000
    X, Y = np.meshgrid(xs, ys)
    Z = np.vectorize(region.topo)(X, Y)
    gmap = anomaly(prisms, X.ravel(), Y.ravel(), Z.ravel()).reshape(X.shape) * SI_TO_MGAL
    write_table(__file__, ("x_km", "y_km", "dg_mGal"),
                [(X[j, i] / 1000, Y[j, i] / 1000, gmap[j, i])
                 for j in range(len(ys)) for i in range(len(xs))], part="map")
    rows = []
    for level in (-0.5, -1.0, -1.5, -2.0, -2.5):
        for line in region.trace(gmap, xs / 1000, ys / 1000, level):
            rows.extend((x, y, level) for x, y in line)
            rows.append((math.nan, math.nan, level))
    write_table(__file__, ("x_km", "y_km", "level"), rows, part="contours")
    st = [(x / 1000, y / 1000) for y in np.arange(2800, 5501, 200) for x in np.arange(2000, 5001, 200)]
    write_table(__file__, ("x_km", "y_km"), st, part="stations")
    # profile
    px = np.arange(1500.0, 5501.0, 25.0)
    pz = np.array([region.topo(x, Y_LINE) for x in px])
    gp = anomaly(prisms, px, np.full_like(px, Y_LINE), pz) * SI_TO_MGAL
    xh, xpk, gpk = half_width(px, gp)
    z_s, m_s = sphere_from_halfwidth(gpk / SI_TO_MGAL, xh)
    sph = point_gz(m_s, px - xpk, z_s) * SI_TO_MGAL
    # vertical cylinder of equal-area radius, from the ground at the centre to the floor
    rad = math.sqrt(GA * GB)
    z_ground = region.topo(GX, Y_LINE)
    cyl = vcyl_profile(px - GX, rad, 0.0, z_ground - FLOOR, DRHO) * SI_TO_MGAL
    write_table(__file__, ("x_km", "dg_mGal", "sphere", "cyl"),
                [(x / 1000, g, s, c) for x, g, s, c in zip(px, gp, sph, cyl)], part="profile")
    write_table(__file__, ("x_km", "t_h", "h_m", "reading"),
                [(x / 1000, t, h, r) for x, t, h, r, _ in loop_readings(prisms)], part="loop",
                digits=7)
    vals = [["n_prisms", len(prisms)], ["volume_km3", vol / 1e9], ["mass_deficit_kg", mass],
            ["centre_of_mass_elev_m", zc], ["ground_at_centre_m", z_ground],
            ["centre_depth_m", z_ground - zc],
            ["map_min_mGal", float(gmap.min())], ["profile_peak_mGal", gpk],
            ["profile_peak_x_km", xpk / 1000], ["half_width_m", xh],
            ["sphere_depth_m", z_s], ["sphere_mass_kg", m_s],
            ["equal_area_radius_m", rad],
            ["cyl_axis_mGal", vcyl_axis(rad, 0.0, z_ground - FLOOR, DRHO) * SI_TO_MGAL],
            ["cyl_axis_inf_mGal", 2 * math.pi * G * DRHO * rad * SI_TO_MGAL]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
