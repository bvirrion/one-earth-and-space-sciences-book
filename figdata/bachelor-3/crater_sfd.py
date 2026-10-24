"""Crater size-frequency distributions and crater dating on Mars (Year 3, planetary
interiors and surfaces).

Production function (Ivanov 2001, ledger craterstats:mars-pf): the cumulative number of
craters per km2 at least D km across,

    log10 N(D) = sum_{n=0..11} a_n (log10 D)^n,

whose shape F(D) = N(D)/N(1) is the same for every age. Chronology function (Hartmann
and Neukum 2001, craterstats:mars-cf), the number of craters of 1 km and more per km2
accumulated in T Ga:

    N1(T) = a (exp(b T) - 1) + c T,    a = 3.22e-14, b = 6.93, c = 4.875e-4.

An isochron is N(D, T) = N1(T) F(D). The lunar chronology function (Neukum,
craterstats:moon-cf) is drawn for comparison, and the equilibrium density of Hartmann
(1984, craterstats:equilibrium), log10 N = -1.14 - 1.83 log10 D.

Two invented Martian surfaces (counts drawn once from a Poisson law, seeded):
  plain A, 80,000 km2, a lava plain 1.5 Ga old;
  plain B, 120,000 km2, an old plain of 3.6 Ga whose craters smaller than 2 km were
  buried by lava 1.0 Ga ago (they record only the time since).
Bins are root-2 wide from 1 km; the problem gives the incremental counts.

  part iso        D N_0.1 N_0.3 N_1 N_3 N_3.5 N_4 eq     (km, per km2)
  part chron      T mars moon                             (Ga, N(1) per km2)
  part bins       Dlo Dhi nA nB                           incremental counts
  part cumA       D N err                                 cumulative per km2, sqrt(n) error
  part cumB       D N err
  part values     what value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

PF = (-3.383677, -3.197453, 1.256814, 7.915374e-01, -4.860814e-01, -3.630098e-01,
      1.015683e-01, 6.755923e-02, -1.180639e-02, -4.753462e-03, 6.232845e-04,
      5.805492e-05)
CF_MARS = (3.22e-14, 6.93, 4.875e-4)
CF_MOON = (5.44e-14, 6.93, 8.38e-4)
EQ = (-1.14, -1.83)

AREA_A, AGE_A = 80000.0, 1.5
AREA_B, AGE_B, AGE_B_RESURF, D_BURIED = 120000.0, 3.6, 1.0, 2.0
EDGES = [2 ** (k / 2) for k in range(0, 10)]  # 1 ... 22.6 km
SEED = 26


def pf_log(d):
    ld = math.log10(d)
    return sum(a * ld ** n for n, a in enumerate(PF))


def shape(d):
    """F(D) = N(>= D) / N(>= 1 km)."""
    return 10 ** (pf_log(d) - pf_log(1.0))


def n1(t, cf=CF_MARS):
    a, b, c = cf
    return a * (math.exp(b * t) - 1.0) + c * t


def dn1(t, cf=CF_MARS):
    a, b, c = cf
    return a * b * math.exp(b * t) + c


def isochron(d, t, cf=CF_MARS):
    return n1(t, cf) * shape(d)


def equilibrium(d):
    return 10 ** (EQ[0] + EQ[1] * math.log10(d))


def age(n1_obs, cf=CF_MARS):
    """Invert the chronology function by bisection (it increases with T)."""
    lo, hi = 0.0, 4.6
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if n1(mid, cf) < n1_obs:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def age_error(t, n_count, cf=CF_MARS):
    """One-sigma age error from Poisson counting: dT = N1 / (sqrt(n) dN1/dT)."""
    return n1(t, cf) / (math.sqrt(n_count) * dn1(t, cf))


def expected_bins(area, t_old, t_young=None, d_buried=0.0):
    """Expected incremental counts in the EDGES bins."""
    out = []
    for lo, hi in zip(EDGES[:-1], EDGES[1:]):
        t = t_young if (t_young is not None and hi <= d_buried) else t_old
        out.append(area * n1(t) * (shape(lo) - shape(hi)))
    return out


def counts():
    rng = np.random.default_rng(SEED)
    ea = expected_bins(AREA_A, AGE_A)
    eb = expected_bins(AREA_B, AGE_B, AGE_B_RESURF, D_BURIED)
    return [int(v) for v in rng.poisson(ea)], [int(v) for v in rng.poisson(eb)]


def cumulative(nbins, area):
    rows = []
    for i, lo in enumerate(EDGES[:-1]):
        n = sum(nbins[i:])
        if n > 0:
            rows.append((lo, n / area, math.sqrt(n) / area, n))
    return rows


def main():
    ds = np.logspace(-1, 2, 121)
    ages = (0.1, 0.3, 1.0, 3.0, 3.5, 4.0)
    write_table(__file__, ("D", "N_0.1", "N_0.3", "N_1", "N_3", "N_3.5", "N_4", "eq"),
                [(d, *[isochron(d, t) for t in ages], equilibrium(d)) for d in ds],
                part="iso")
    ts = np.round(np.arange(0.0, 4.5001, 0.025), 3)
    write_table(__file__, ("T", "mars", "moon"),
                [(t, n1(t), n1(t, CF_MOON)) for t in ts[1:]], part="chron")
    na, nb = counts()
    write_table(__file__, ("Dlo", "Dhi", "nA", "nB"),
                [(round(lo, 3), round(hi, 3), a, b)
                 for lo, hi, a, b in zip(EDGES[:-1], EDGES[1:], na, nb)], part="bins")
    ca, cb = cumulative(na, AREA_A), cumulative(nb, AREA_B)
    write_table(__file__, ("D", "N", "err"), [r[:3] for r in ca], part="cumA")
    write_table(__file__, ("D", "N", "err"), [r[:3] for r in cb], part="cumB")
    nA1 = sum(na)
    tA = age(nA1 / AREA_A)
    # plain B: the craters of 2 km and more date the old plain, the 1-2 km bins the lava
    nB2 = sum(nb[2:])
    tB = age(nB2 / AREA_B / shape(2.0))
    nBsmall = nb[0] + nb[1]
    tR = age(nBsmall / AREA_B / (shape(1.0) - shape(2.0)))
    vals = [["F2", shape(2.0)], ["F1.41", shape(EDGES[1])], ["F4", shape(4.0)],
            ["F8", shape(8.0)], ["F10", shape(10.0)],
            ["n1_1Ga", n1(1.0)], ["n1_3Ga", n1(3.0)], ["n1_3.5Ga", n1(3.5)],
            ["n1_4Ga", n1(4.0)], ["moon_1Ga", n1(1.0, CF_MOON)],
            ["moon_3.8Ga", n1(3.8, CF_MOON)],
            ["A_n1", nA1], ["A_N1", nA1 / AREA_A], ["A_age", tA],
            ["A_err", age_error(tA, nA1)],
            ["B_n2", nB2], ["B_N2", nB2 / AREA_B], ["B_age", tB],
            ["B_err", age_error(tB, nB2)],
            ["B_nsmall", nBsmall], ["B_resurf", tR], ["B_resurf_err", age_error(tR, nBsmall)],
            ["eq_1km", equilibrium(1.0)], ["eq_0.1km", equilibrium(0.1)],
            ["iso4_0.1km", isochron(0.1, 4.0)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
