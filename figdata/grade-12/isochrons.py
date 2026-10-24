"""Radiometric dating (grade 12): the rubidium-strontium isochron of the Varden granite,
Patterson's lead isochron of the meteorites, and the history of the estimates of the
Earth's age.

Rb-Sr: 87Sr/86Sr = (87Sr/86Sr)_0 + 87Rb/86Sr (e^(lambda t) - 1), lambda(87Rb) =
1.3972e-11 per year (IUGS-IUPAC 2022, ledger villa22:rb87). The Varden Hills are the
series' invented region (figdata/shared/region.py): granite intruded at 310 Ma into a
schist of 480 Ma. The "measured" ratios below are exercise data computed for those ages
and rounded to five decimals, as a laboratory would report them; the minerals and their
Rb/Sr ratios are chosen for the exercise (plagioclase lowest, biotite highest); isochron
method as in the Tulane notes (ledger tulane:radiometric). The initial ratios are invented too (granite 0.7080,
schist 0.7120, a basalt of the region 0.7035): exercise data, no row.

Pb-Pb: Patterson (1956), Table 1 (ledger patterson56:table): 206Pb/204Pb and 207Pb/204Pb
of three stony and two iron meteorites, and of a modern ocean sediment (19.0, 15.5).
The slope of the line through the meteorites gives the age through
  slope = (1/k) (e^(l5 t) - 1) / (e^(l8 t) - 1),
with Patterson's own constants k = 137.8, l5 = 9.72e-10, l8 = 1.537e-10 per year
(ledger patterson56:constants); he found 4.55 +- 0.07 Ga.

Estimates of the age of the Earth against the year they were made (Phillips 1860 is
left out of the chart: its bar would sit on Kelvin's two years later): Kelvin 1862 (20-400) and 1897 (20-40), Joly 1899 (80-100), Holmes 1913
(oldest rocks dated, 1600 Myr) from Holmes (1913), ledger holmes13:estimates; Holmes
1927 (1600-3000 Myr, holmes27:age); Patterson 1956; today 4.54 Ga to within 1 %
(Book 1 row usgs:age-earth).

  part granite   mineral idx rbsr srsr          the Varden granite samples
  part schist    idx rbsr srsr                  the Varden schist samples
  part graniteln x y                            the fitted granite isochron, x 0-30
  part pbpb      idx r206 r207                  Patterson's meteorites (1-5) and the sediment (6)
  part pbln      x y                            the fitted meteorite isochron, x 8-55
  part history   year lo hi mid idx             estimates (years), lo = hi for one value
  part numbers   key value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

LAMBDA_RB = 1.3972e-11                   # per year, 87Rb
GRANITE_AGE_MA, SCHIST_AGE_MA = 310.0, 480.0
GRANITE_SR0, SCHIST_SR0, BASALT_SR0 = 0.7080, 0.7120, 0.7035
GRANITE = (("plagioclase", 0.35), ("hornblende", 1.20), ("whole rock", 3.10),
           ("K-feldspar", 6.40), ("biotite", 24.0))
SCHIST = (0.90, 2.60, 5.10, 9.40)

PATTERSON = (("Nuevo Laredo", 50.28, 34.86), ("Forest City", 19.27, 15.95),
             ("Modoc", 19.48, 15.76), ("Henbury", 9.55, 10.38), ("Canyon Diablo", 9.46, 10.34))
SEDIMENT = (19.0, 15.5)
K_P, L5_P, L8_P = 137.8, 9.72e-10, 1.537e-10
PATTERSON_AGE_GA = 4.55

# (year, low, high) in years; a single value has low = high
HISTORY = (("Kelvin", 1862, 20e6, 400e6),
           ("Kelvin", 1897, 20e6, 40e6),
           ("Joly", 1899, 80e6, 100e6),
           ("Holmes", 1913, 1.6e9, 1.6e9),
           ("Holmes", 1927, 1.6e9, 3.0e9),
           ("Patterson", 1956, 4.48e9, 4.62e9),
           ("today", 2026, 4.50e9, 4.58e9))


def growth(t_ma, lam=LAMBDA_RB):
    """e^(lambda t) - 1 for an age in millions of years."""
    return math.expm1(lam * t_ma * 1e6)


def srsr(rbsr, t_ma, sr0):
    return round(sr0 + rbsr * growth(t_ma), 5)


def granite_samples():
    return [(name, x, srsr(x, GRANITE_AGE_MA, GRANITE_SR0)) for name, x in GRANITE]


def schist_samples():
    return [(x, srsr(x, SCHIST_AGE_MA, SCHIST_SR0)) for x in SCHIST]


def fit(xs, ys):
    """Least-squares line y = a + b x; returns (a, b)."""
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my - b * mx, b


def age_from_slope_ma(slope, lam=LAMBDA_RB):
    """t = ln(1 + slope) / lambda, in millions of years."""
    return math.log1p(slope) / lam / 1e6


def pb_slope(t_ga, k=K_P, l5=L5_P, l8=L8_P):
    t = t_ga * 1e9
    return math.expm1(l5 * t) / math.expm1(l8 * t) / k


def pb_age_ga(slope):
    lo, hi = 0.1, 6.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if pb_slope(mid) < slope:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def patterson_fit():
    return fit([p[1] for p in PATTERSON], [p[2] for p in PATTERSON])


def numbers():
    n = {}
    g = granite_samples()
    a, b = fit([s[1] for s in g], [s[2] for s in g])
    n["granite_intercept"], n["granite_slope"] = a, b
    n["granite_age_Ma"] = age_from_slope_ma(b)
    s = schist_samples()
    a2, b2 = fit([x for x, y in s], [y for x, y in s])
    n["schist_intercept"], n["schist_slope"] = a2, b2
    n["schist_age_Ma"] = age_from_slope_ma(b2)
    n["growth_310"] = growth(GRANITE_AGE_MA)
    n["growth_480"] = growth(SCHIST_AGE_MA)
    n["rb_half_life_Ga"] = math.log(2) / LAMBDA_RB / 1e9
    a3, b3 = patterson_fit()
    n["pb_intercept"], n["pb_slope"] = a3, b3
    n["pb_age_Ga"] = pb_age_ga(b3)
    n["pb_slope_455"] = pb_slope(PATTERSON_AGE_GA)
    # the sediment: how far from the meteorite line (in 207/204 units)
    n["sediment_residual"] = SEDIMENT[1] - (a3 + b3 * SEDIMENT[0])
    # two-point slopes, Canyon Diablo to each stone
    cd = PATTERSON[4]
    for name, x, y in PATTERSON[:3]:
        key = name.split()[0].lower()
        n["pb_slope_cd_" + key] = (y - cd[2]) / (x - cd[1])
        n["pb_age_cd_" + key] = pb_age_ga((y - cd[2]) / (x - cd[1]))
    # ratios of the estimates to today's 4.54 Ga
    n["ratio_kelvin1897_hi"] = 4.54e9 / 40e6
    n["ratio_buffon"] = 4.54e9 / 74832.0
    return n


if __name__ == "__main__":
    write_table(__file__, ("mineral", "idx", "rbsr", "srsr"),
                [(name.replace(" ", "-"), i, x, y) for i, (name, x, y) in enumerate(granite_samples(), 1)],
                part="granite", digits=6)
    write_table(__file__, ("idx", "rbsr", "srsr"),
                [(i, x, y) for i, (x, y) in enumerate(schist_samples(), 1)], part="schist", digits=6)
    g = granite_samples()
    a, b = fit([s[1] for s in g], [s[2] for s in g])
    write_table(__file__, ("x", "y"), [(0.0, a), (30.0, a + 30.0 * b)], part="graniteln", digits=6)
    write_table(__file__, ("idx", "r206", "r207"),
                [(i, x, y) for i, (nm, x, y) in enumerate(PATTERSON, 1)] + [(6, SEDIMENT[0], SEDIMENT[1])],
                part="pbpb", digits=5)
    a3, b3 = patterson_fit()
    write_table(__file__, ("x", "y"), [(8.0, a3 + 8.0 * b3), (55.0, a3 + 55.0 * b3)], part="pbln", digits=5)
    write_table(__file__, ("year", "lo", "hi", "mid", "idx"),
                [(yr, lo, hi, math.sqrt(lo * hi), i) for i, (nm, yr, lo, hi) in enumerate(HISTORY, 1)],
                part="history", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=6)
