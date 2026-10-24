"""Palaeomagnetic statistics, poles and the invented Kesta terrane (Year 3,
palaeomagnetism).

Directions (declination D, inclination I, degrees; I positive down) become unit
vectors x = cos I cos D (north), y = cos I sin D (east), z = sin I (down).
Fisher statistics (the chapter's proposition): resultant length R of N unit
vectors, precision k = (N - 1)/(N - R), and the 95 % cone
    cos a95 = 1 - (N - R)/R [ (1/0.05)^(1/(N - 1)) - 1 ].
Dipole formula tan I = 2 tan(lat); virtual geomagnetic pole by the spherical
triangle (palaeocolatitude p, cot p = tan I / 2); dp = a95 (1 + 3 cos^2 p)/2,
dm = a95 sin p / cos I. Expected direction at a site from a pole: the inverse
triangle.

The Kesta terrane, its three formations (A oldest) and the reference apparent
polar wander path of the stable continent are invented. Sample directions are
Fisher draws (seeded) about chosen means, rounded to whole degrees, which is
what the problem prints; all statistics below are computed from the rounded
directions.

The Zijderveld specimen: a characteristic remanence (D 35, I 38) carried up to
580 C, plus a viscous overprint along the present field (D 0, I 65) removed by
300 C (synthetic unblocking spectra, linear in temperature).

  part dirs      fm D I x y               the sample directions of the three formations
                                          and their equal-area plot coordinates
                                          (x east, y north, lower hemisphere, radius 1)
  part means     fm D I N R k a95 x y     site means and plot coordinates
  part dirsA     x y                      formation A only; part meanA its mean
  part cone      x y                      the a95 circle of formation A (equal-area)
  part zij       T N E Down H             the demagnetisation steps (mA/m): north, east,
                                          down components and horizontal projection
  part apw       id age plat plon a95 x y    reference poles and the Kesta VGPs, polar
                                          azimuthal equal-area (x, y; radius 1 = equator)
  part apwref, apwkesta  x y             the same, split for plotting
  part apwcircles id x y                  their a95 circles, rows 'nan nan nan' between
  part graticule id x y                   latitude circles 50-80 N, meridians every 30 deg
  part lonlabels lon x y                 meridian label positions (43 N)
  part values    what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

SITE = (47.0, 15.0)                    # Kesta, lat N, lon E (invented)
FORMATIONS = {                         # name: (age Ma, true D, true I, N, kappa, seed)
    "A": (60.0, 35.0, 38.0, 6, 90.0, 11),
    "B": (30.0, 21.0, 55.0, 7, 70.0, 23),
    "C": (4.0, 4.0, 64.0, 8, 60.0, 37),
}
REFERENCE = [(60.0, 78.0, 190.0, 3.0), (30.0, 83.5, 175.0, 2.5), (4.0, 87.5, 150.0, 2.0)]
P95 = 0.05


def to_xyz(d, i):
    d, i = math.radians(d), math.radians(i)
    return np.array([math.cos(i) * math.cos(d), math.cos(i) * math.sin(d), math.sin(i)])


def to_di(v):
    v = np.asarray(v, dtype=float)
    v = v / np.linalg.norm(v)
    return math.degrees(math.atan2(v[1], v[0])) % 360.0, math.degrees(math.asin(v[2]))


def fisher_mean(dirs):
    s = sum(to_xyz(d, i) for d, i in dirs)
    r = float(np.linalg.norm(s))
    n = len(dirs)
    d, i = to_di(s)
    k = (n - 1) / (n - r)
    c = 1 - (n - r) / r * ((1 / P95) ** (1 / (n - 1)) - 1)
    return d, i, n, r, k, math.degrees(math.acos(c))


def fisher_draw(d0, i0, kappa, n, rng):
    """n directions from a Fisher distribution of precision kappa about (d0, i0)."""
    out = []
    mean = to_xyz(d0, i0)
    a = np.array([0.0, 0.0, 1.0]) if abs(mean[2]) < 0.9 else np.array([1.0, 0.0, 0.0])
    e1 = np.cross(mean, a)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(mean, e1)
    for _ in range(n):
        u = rng.random()
        cos_t = 1 + math.log(u + (1 - u) * math.exp(-2 * kappa)) / kappa
        sin_t = math.sqrt(max(0.0, 1 - cos_t ** 2))
        ph = 2 * math.pi * rng.random()
        v = cos_t * mean + sin_t * (math.cos(ph) * e1 + math.sin(ph) * e2)
        out.append(to_di(v))
    return out


def rounded_dirs(name):
    age, d0, i0, n, kappa, seed = FORMATIONS[name]
    rng = np.random.default_rng(seed)
    return [(round(d) % 360, round(i)) for d, i in fisher_draw(d0, i0, kappa, n, rng)]


def palaeolatitude(inc):
    return math.degrees(math.atan(math.tan(math.radians(inc)) / 2))


def vgp(d, i, site=SITE):
    ls, ps = math.radians(site[0]), site[1]
    p = math.radians(90.0 - palaeolatitude(i))
    dr = math.radians(d)
    lp = math.asin(math.sin(ls) * math.cos(p) + math.cos(ls) * math.sin(p) * math.cos(dr))
    beta = math.degrees(math.asin(math.sin(p) * math.sin(dr) / math.cos(lp)))
    if math.cos(p) >= math.sin(ls) * math.sin(lp):
        lon = ps + beta
    else:
        lon = ps + 180.0 - beta
    return math.degrees(lp), lon % 360.0


def dp_dm(a95, inc):
    p = math.radians(90.0 - palaeolatitude(inc))
    return (a95 / 2 * (1 + 3 * math.cos(p) ** 2),
            a95 * math.sin(p) / math.cos(math.radians(inc)))


def expected_direction(plat, plon, site=SITE):
    ls, lp = math.radians(site[0]), math.radians(plat)
    dl = math.radians(plon - site[1])
    cp = math.sin(ls) * math.sin(lp) + math.cos(ls) * math.cos(lp) * math.cos(dl)
    p = math.acos(cp)
    inc = math.degrees(math.atan(2 / math.tan(p)))
    cd = (math.sin(lp) - math.sin(ls) * cp) / (math.cos(ls) * math.sin(p))
    d = math.degrees(math.acos(max(-1.0, min(1.0, cd))))
    if math.sin(dl) < 0:
        d = 360.0 - d
    return d, inc, 90.0 - math.degrees(p)


LON0 = 160.0  # meridian pointing down on the polar plot


def equal_area(d, i):
    """Lower-hemisphere equal-area plot of a direction: x east, y north, radius 1."""
    r = math.sqrt(2) * math.sin(math.radians(90.0 - abs(i)) / 2)
    return r * math.sin(math.radians(d)), r * math.cos(math.radians(d))


def polar_equal_area(lat, lon, lon0=0.0):
    """North-polar azimuthal equal-area: radius 1 at the equator; lon0 points down."""
    r = math.sqrt(2) * math.sin(math.radians(90.0 - lat) / 2)
    a = math.radians(lon - lon0)
    return r * math.sin(a), -r * math.cos(a)


def small_circle(lat, lon, radius, n=72):
    """Points of a small circle of angular radius about (lat, lon)."""
    c = to_xyz_geo(lat, lon)
    a = np.array([0.0, 0.0, 1.0]) if abs(c[2]) < 0.9 else np.array([1.0, 0.0, 0.0])
    e1 = np.cross(c, a)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(c, e1)
    r = math.radians(radius)
    pts = []
    for k in range(n + 1):
        t = 2 * math.pi * k / n
        v = math.cos(r) * c + math.sin(r) * (math.cos(t) * e1 + math.sin(t) * e2)
        pts.append((math.degrees(math.asin(v[2])), math.degrees(math.atan2(v[1], v[0]))))
    return pts


def to_xyz_geo(lat, lon):
    la, lo = math.radians(lat), math.radians(lon)
    return np.array([math.cos(la) * math.cos(lo), math.cos(la) * math.sin(lo), math.sin(la)])


def cone_points(d, i, a95, n=72):
    """The a95 circle about a direction, as (D, I) points (directions, not poles)."""
    c = to_xyz(d, i)
    a = np.array([0.0, 0.0, 1.0]) if abs(c[2]) < 0.9 else np.array([1.0, 0.0, 0.0])
    e1 = np.cross(c, a)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(c, e1)
    r = math.radians(a95)
    return [to_di(math.cos(r) * c + math.sin(r) * (math.cos(2 * math.pi * k / n) * e1
                                                    + math.sin(2 * math.pi * k / n) * e2))
            for k in range(n + 1)]


def zijderveld(steps=(20, 100, 150, 200, 250, 300, 350, 400, 450, 500, 530, 560, 580)):
    """Remaining NRM vector (mA/m) after each heating step: ChRM 40 mA/m unblocking
    linearly from 300 to 580 C, viscous overprint 15 mA/m unblocking from 20 to 300 C."""
    ch, vo = 40.0 * to_xyz(35.0, 38.0), 15.0 * to_xyz(0.0, 65.0)
    rows = []
    for t in steps:
        fc = 1.0 if t <= 300 else max(0.0, (580 - t) / 280.0)
        fv = max(0.0, (300 - t) / 280.0) if t >= 20 else 1.0
        v = fc * ch + fv * vo
        rows.append((t, v[0], v[1], v[2], math.hypot(v[0], v[1])))
    return rows


def kesta():
    """Fisher means (from the rounded directions), palaeolatitudes and VGPs."""
    out = {}
    for name in FORMATIONS:
        dirs = rounded_dirs(name)
        d, i, n, r, k, a95 = fisher_mean(dirs)
        out[name] = dict(dirs=dirs, D=d, I=i, N=n, R=r, k=k, a95=a95,
                         lat=palaeolatitude(i), vgp=vgp(d, i), dpdm=dp_dm(a95, i))
    return out


if __name__ == "__main__":
    ks = kesta()
    rows, mrows = [], []
    for name, v in ks.items():
        for d, i in v["dirs"]:
            rows.append((name, d, i) + equal_area(d, i))
        mrows.append((name, v["D"], v["I"], v["N"], v["R"], v["k"], v["a95"]) + equal_area(v["D"], v["I"]))
    write_table(__file__, ("fm", "D", "I", "x", "y"), rows, part="dirs")
    write_table(__file__, ("fm", "D", "I", "N", "R", "k", "a95", "x", "y"), mrows, part="means")
    a = ks["A"]
    write_table(__file__, ("x", "y"), [equal_area(d, i) for d, i in a["dirs"]], part="dirsA")
    write_table(__file__, ("x", "y"), [equal_area(a["D"], a["I"])], part="meanA")
    write_table(__file__, ("x", "y"), [equal_area(d, i) for d, i in cone_points(a["D"], a["I"], a["a95"])],
                part="cone")
    write_table(__file__, ("T", "N", "E", "Down", "H"), zijderveld(), part="zij")
    prow, crow, grow = [], [], []
    for lat in (50, 60, 70, 80):
        grow += [(lat,) + polar_equal_area(lat, lo, LON0) for lo in range(0, 361, 5)]
        grow.append(("nan", "nan", "nan"))
    for lo in range(0, 360, 30):
        grow += [(1000 + lo,) + polar_equal_area(la, lo, LON0) for la in (45, 90)]
        grow.append(("nan", "nan", "nan"))
    write_table(__file__, ("id", "x", "y"), grow[:-1], part="graticule")
    lrow = [(lo,) + polar_equal_area(43.0, lo, LON0) for lo in range(0, 360, 30)]
    write_table(__file__, ("lon", "x", "y"), lrow, part="lonlabels")
    for k, (age, plat, plon, a95) in enumerate(REFERENCE):
        prow.append(("ref", age, plat, plon, a95) + polar_equal_area(plat, plon, LON0))
        crow += [(k,) + polar_equal_area(la, lo, LON0) for la, lo in small_circle(plat, plon, a95)]
        crow.append(("nan", "nan", "nan"))
    for k, name in enumerate(FORMATIONS):
        v = ks[name]
        plat, plon = v["vgp"]
        prow.append(("kesta" + name, FORMATIONS[name][0], plat, plon, v["a95"]) + polar_equal_area(plat, plon, LON0))
        crow += [(10 + k,) + polar_equal_area(la, lo, LON0) for la, lo in small_circle(plat, plon, v["a95"])]
        crow.append(("nan", "nan", "nan"))
    write_table(__file__, ("id", "age", "plat", "plon", "a95", "x", "y"), prow, part="apw")
    write_table(__file__, ("x", "y"), [r[5:] for r in prow if r[0] == "ref"], part="apwref")
    write_table(__file__, ("x", "y"), [r[5:] for r in prow if r[0] != "ref"], part="apwkesta")
    write_table(__file__, ("id", "x", "y"), crow[:-1], part="apwcircles")
    vals = []
    for name, v in ks.items():
        vals += [("%s_D" % name, v["D"]), ("%s_I" % name, v["I"]), ("%s_R" % name, v["R"]),
                 ("%s_k" % name, v["k"]), ("%s_a95" % name, v["a95"]), ("%s_lat" % name, v["lat"]),
                 ("%s_vgp_lat" % name, v["vgp"][0]), ("%s_vgp_lon" % name, v["vgp"][1]),
                 ("%s_dp" % name, v["dpdm"][0]), ("%s_dm" % name, v["dpdm"][1])]
    for age, plat, plon, a95 in REFERENCE:
        d, i, lat = expected_direction(plat, plon)
        vals += [("exp%d_D" % age, d), ("exp%d_I" % age, i), ("exp%d_lat" % age, lat)]
    write_table(__file__, ("what", "value"), vals, part="values")
    for name, v in ks.items():
        print(name, v["dirs"])
