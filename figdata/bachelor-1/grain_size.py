"""Grain-size statistics and palaeocurrents (Year 1, clastic-sediments).

The phi scale of Krumbein turns the Udden-Wentworth classes into equal steps:

    phi = -log2(d / 1 mm).

Two invented sieve analyses (weight per cent per class) illustrate the statistics:
a beach sand sieved at half-phi intervals and a glacial till analysed at whole-phi
intervals (the fine part by settling). For each sample the script computes

  * the cumulative curve, weight per cent coarser than each class boundary;
  * the percentiles phi_5, phi_16, phi_50, phi_84, phi_95 by linear interpolation
    of that curve in phi;
  * Folk's graphic mean Mz = (phi16 + phi50 + phi84)/3 and inclusive graphic
    standard deviation sigma_I = (phi84 - phi16)/4 + (phi95 - phi5)/6.6
    (Folk 1980, ledger folk:graphic-measures), and the verbal sorting class
    (folk:sorting-classes);
  * the mean and standard deviation by the method of moments, the classes being
    represented by their mid-points.

It also holds the plane vector mean of palaeocurrent azimuths (the resultant of
unit vectors, ch. 6 in three dimensions), used by the exercises and the problem.

  part hist-beach  phi_lo phi_hi phi_mid wt          (histogram bars)
  part hist-till   phi_lo phi_hi phi_mid wt
  part step-beach  phi wt    (class lower edges, then the last upper edge with
  part step-till   phi wt     the last weight: a closed step for pgfplots)
  part cum-beach   phi cum                            (cumulative % coarser)
  part cum-till    phi cum
  part values      what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

# Invented sieve analyses (weight per cent per class, lower phi edge, upper phi edge).
BEACH = [(0.5, 1.0, 0.2), (1.0, 1.5, 1.3), (1.5, 2.0, 17.5), (2.0, 2.5, 62.0),
         (2.5, 3.0, 17.8), (3.0, 3.5, 1.2)]
TILL = [(-5.0, -4.0, 4.0), (-4.0, -3.0, 6.0), (-3.0, -2.0, 7.0), (-2.0, -1.0, 8.0),
        (-1.0, 0.0, 8.0), (0.0, 1.0, 9.0), (1.0, 2.0, 10.0), (2.0, 3.0, 10.0),
        (3.0, 4.0, 9.0), (4.0, 5.0, 8.0), (5.0, 6.0, 6.0), (6.0, 7.0, 5.0),
        (7.0, 8.0, 4.0), (8.0, 9.0, 3.0), (9.0, 10.0, 3.0)]

# Folk's verbal scale for sigma_I (upper limits, phi units).
SORTING = [(0.35, "very well sorted"), (0.50, "well sorted"), (0.71, "moderately well sorted"),
           (1.00, "moderately sorted"), (2.00, "poorly sorted"), (4.00, "very poorly sorted"),
           (math.inf, "extremely poorly sorted")]


def phi_of(d_mm):
    """Phi value of a diameter in millimetres."""
    return -math.log2(d_mm)


def d_of(phi):
    """Diameter (mm) of a phi value."""
    return 2.0 ** (-phi)


def cumulative(sample):
    """[(phi, weight per cent coarser than phi)] at every class boundary, from the
    coarse end (0 %) to the fine end (100 %)."""
    total = sum(w for _, _, w in sample)
    pts = [(sample[0][0], 0.0)]
    acc = 0.0
    for lo, hi, w in sample:
        acc += w
        pts.append((hi, 100.0 * acc / total))
    return pts


def percentile(sample, p):
    """The phi value at which p per cent of the sample is coarser (linear interpolation)."""
    pts = cumulative(sample)
    for (x0, c0), (x1, c1) in zip(pts, pts[1:]):
        if c0 <= p <= c1 and c1 > c0:
            return x0 + (p - c0) * (x1 - x0) / (c1 - c0)
    raise ValueError("percentile out of range")


def folk(p5, p16, p50, p84, p95):
    """(graphic mean, inclusive graphic standard deviation) from five percentiles."""
    return (p16 + p50 + p84) / 3.0, (p84 - p16) / 4.0 + (p95 - p5) / 6.6


def folk_measures(sample):
    ps = [percentile(sample, p) for p in (5, 16, 50, 84, 95)]
    return folk(*ps), ps


def sorting_class(sigma):
    for lim, name in SORTING:
        if sigma < lim:
            return name
    return SORTING[-1][1]


def step(sample):
    """[(phi, wt)]: each class's lower edge with its weight, closed by the last
    class's upper edge, so that a ybar interval or const plot draws every class."""
    return [(lo, w) for lo, _, w in sample] + [(sample[-1][1], sample[-1][2])]


def moments(sample):
    """(mean, standard deviation) in phi by the method of moments (class mid-points)."""
    total = sum(w for _, _, w in sample)
    mids = [((lo + hi) / 2.0, w / total) for lo, hi, w in sample]
    m = sum(x * f for x, f in mids)
    var = sum(f * (x - m) ** 2 for x, f in mids)
    return m, math.sqrt(var)


def vector_mean(azimuths_deg):
    """(mean azimuth in degrees 0-360, mean resultant length) of directions."""
    s = sum(math.sin(math.radians(a)) for a in azimuths_deg)
    c = sum(math.cos(math.radians(a)) for a in azimuths_deg)
    n = len(azimuths_deg)
    return math.degrees(math.atan2(s, c)) % 360.0, math.hypot(s, c) / n


def normal_quantile_check(mu=2.0, sigma=0.5):
    """Folk's measures of an exactly normal distribution in phi: (Mz, sigma_I).
    Uses the normal quantiles z(0.84) = 0.99446 and z(0.95) = 1.64485."""
    z84, z95 = 0.994458, 1.644854
    return folk(mu - z95 * sigma, mu - z84 * sigma, mu, mu + z84 * sigma, mu + z95 * sigma)


if __name__ == "__main__":
    vals = []
    for name, s in (("beach", BEACH), ("till", TILL)):
        write_table(__file__, ("phi_lo", "phi_hi", "phi_mid", "wt"),
                    [(lo, hi, (lo + hi) / 2.0, w) for lo, hi, w in s], part="hist-" + name)
        write_table(__file__, ("phi", "cum"), cumulative(s), part="cum-" + name)
        write_table(__file__, ("phi", "wt"), step(s), part="step-" + name)
        (mz, si), ps = folk_measures(s)
        m, sd = moments(s)
        for k, p in zip((5, 16, 50, 84, 95), ps):
            vals.append(("%s_phi%d" % (name, k), p))
        vals += [(name + "_Mz", mz), (name + "_sigmaI", si), (name + "_mom_mean", m),
                 (name + "_mom_sd", sd)]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)
