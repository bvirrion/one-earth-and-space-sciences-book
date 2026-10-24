"""What has been found: the NASA Exoplanet Archive's confirmed planets (Year 3, exoplanets).

Data: Planetary Systems Composite Parameters, one row per confirmed planet, fetched
2026-10-23 (data/derived/bachelor-3-pscomp.csv, ledger data:b5-pscomp); model
mass-radius curves of Zeng et al. 2016/2019 (data/derived/bachelor-3-zeng-*.csv, ledger
data:b5-zeng); the Solar System's planets from the NASA fact sheet (planet:*.mass,
planet:*.diameter, planet:*.dist; Earth mass 5.97e24 kg, Earth radius 6378 km).

Selections (all written to the tables, all tested):
* mass-radius: transiting planets (transit = 1) whose mass is a measured true mass
  (mass_prov = "Mass"), with relative uncertainties below 25 % on the mass and 10 % on
  the radius (mean of the two published error bars);
* period-radius: transiting planets with a radius known to better than 10 %, around
  stars smaller than 2 solar radii (no giants), periods 1-100 days; the histogram counts
  them in 20 equal bins of log R between 0.8 and 4 Earth radii. No correction is made
  for the detection efficiency, so the counts show what was found, not how common
  planets are;
* mass-distance by method: planets with a mass (true or minimum, not one predicted from a
  mass-radius relation) and a semi-major axis, for the four main methods.

  part mr           mass radius
  part pr           period radius
  part hist         r_lo r_hi r_mid n
  part histstep     r n                         bin edges, last count repeated (step plot)
  part zeng-<k>     mass radius                 k = iron, earthlike, water50, h2
  part solar        name mass radius a_au
  part ma-<m>       a_au mass                   m = rv, tr, ml, im
  part values       what value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(ROOT, "data", "derived")
METHODS = {"rv": "Radial Velocity", "tr": "Transit", "ml": "Microlensing", "im": "Imaging"}
ZENG = ("iron", "earthlike", "water50", "h2-2pc")
M_EARTH = 5.97  # 1e24 kg
D_EARTH = 12756.0  # km
SOLAR = (("Mercury", 0.330, 4879, 57.9), ("Venus", 4.87, 12104, 108.2),
         ("Earth", 5.97, 12756, 149.6), ("Mars", 0.642, 6792, 228.0),
         ("Jupiter", 1898, 142984, 778.5), ("Saturn", 568, 120536, 1432.0),
         ("Uranus", 86.8, 51118, 2867.0), ("Neptune", 102, 49528, 4515.0))
AU_MKM = 149.597870700  # 1e6 km
HIST_LO, HIST_HI, HIST_N = 0.8, 4.0, 20


def num(x):
    return float(x) if x not in ("", None) else None


def load_planets():
    with open(os.path.join(DERIVED, "bachelor-3-pscomp.csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


def rel_err(row, key):
    """Mean of the two published error bars over the value, or None."""
    v, e1, e2 = num(row[key]), num(row[key + "_e1"]), num(row[key + "_e2"])
    if v is None or e1 is None or v <= 0:
        return None
    e2 = e1 if e2 is None else e2
    return (abs(e1) + abs(e2)) / 2 / v


def mass_radius(rows):
    out = []
    for r in rows:
        if r["transit"] != "1" or r["mass_prov"] != "Mass":
            continue
        em, er = rel_err(r, "masse"), rel_err(r, "rade")
        if em is None or er is None or em >= 0.25 or er >= 0.10:
            continue
        out.append((num(r["masse"]), num(r["rade"])))
    return sorted(out)


def period_radius(rows):
    out = []
    for r in rows:
        if r["transit"] != "1":
            continue
        p, er, sr = num(r["period_d"]), rel_err(r, "rade"), num(r["st_rad"])
        if p is None or er is None or sr is None:
            continue
        if er < 0.10 and sr < 2.0 and 1.0 <= p <= 100.0:
            out.append((p, num(r["rade"])))
    return sorted(out)


def radius_histogram(pr):
    lo, hi = math.log10(HIST_LO), math.log10(HIST_HI)
    w = (hi - lo) / HIST_N
    counts = [0] * HIST_N
    for _, rad in pr:
        x = math.log10(rad)
        if lo <= x < hi:
            counts[min(HIST_N - 1, int((x - lo) / w))] += 1
    return [(10 ** (lo + i * w), 10 ** (lo + (i + 1) * w), 10 ** (lo + (i + 0.5) * w), c)
            for i, c in enumerate(counts)]


def mass_distance(rows, method):
    out = []
    for r in rows:
        if r["method"] != METHODS[method] or r["mass_prov"] not in ("Mass", "Msini"):
            continue
        a, m = num(r["a_au"]), num(r["masse"])
        if a is not None and m is not None and a > 0 and m > 0:
            out.append((a, m))
    return sorted(out)


def zeng_curve(key, m_lo=0.1, m_hi=30.0):
    with open(os.path.join(DERIVED, "bachelor-3-zeng-%s.csv" % key), encoding="utf8") as f:
        pts = [(float(r["mass"]), float(r["radius"])) for r in csv.DictReader(f)]
    return [(m, rad) for m, rad in pts if m_lo <= m <= m_hi]


def solar_system():
    return [(n, m / M_EARTH, d / D_EARTH, a / AU_MKM) for n, m, d, a in SOLAR]


def method_counts(rows):
    c = {}
    for r in rows:
        c[r["method"]] = c.get(r["method"], 0) + 1
    return c


def main():
    rows = load_planets()
    mr = mass_radius(rows)
    write_table(__file__, ("mass", "radius"), mr, part="mr")
    pr = period_radius(rows)
    write_table(__file__, ("period", "radius"), pr, part="pr")
    hist = radius_histogram(pr)
    write_table(__file__, ("r_lo", "r_hi", "r_mid", "n"), hist, part="hist")
    step = [(lo, n) for lo, _, _, n in hist] + [(hist[-1][1], hist[-1][3])]
    write_table(__file__, ("r", "n"), step, part="histstep")
    for k in ZENG:
        write_table(__file__, ("mass", "radius"), zeng_curve(k), part="zeng-" + k)
    write_table(__file__, ("name", "mass", "radius", "a_au"), solar_system(), part="solar")
    vals = [["n_total", len(rows)], ["n_mr", len(mr)], ["n_pr", len(pr)]]
    for m in METHODS:
        ma = mass_distance(rows, m)
        write_table(__file__, ("a_au", "mass"), ma, part="ma-" + m)
        vals.append(["n_ma_" + m, len(ma)])
    for name, n in sorted(method_counts(rows).items(), key=lambda kv: -kv[1]):
        vals.append(["count_" + name.replace(" ", "_"), n])
    vals.append(["n_mr_small", sum(1 for _, rad in mr if rad < 4)])
    years = [int(r["year"]) for r in rows if r["year"]]
    vals += [["first_year", min(years)], ["n_since_2014", sum(1 for y in years if y >= 2014)]]
    for m, name in METHODS.items():
        ys = [int(r["year"]) for r in rows if r["method"] == name and r["year"]]
        vals.append(["first_" + m, min(ys)])
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
