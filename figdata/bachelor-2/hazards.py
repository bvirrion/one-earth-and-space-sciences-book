"""Geological hazards (Year 2, geological-hazards): the Poisson recurrence model, the
interevent times of the global M >= 7 catalogue, a toy probabilistic seismic hazard
analysis and the factor of safety of an infinite slope.

  poisson   probability of at least one exceedance in an exposure time t (years),
            P = 1 - exp(-t/T), for return periods T = 50, 475 and 2475 years.
  survival  interevent times of the earthquakes of magnitude >= 7.0 in the shared
            catalogue data/derived/usgs-m6.csv (data:usgs-comcat, 1976-2025, dates only,
            so intervals are whole days): the fraction of intervals longer than t days,
            against the exponential exp(-t/mean) of a Poisson process of the same rate.
  psha      a toy hazard curve: one source zone with every earthquake at a distance
            d = 15 km from the site, truncated Gutenberg-Richter recurrence
            N(>= m) = 10^(a - b m) - 10^(a - b Mmax), a = 4.0, b = 1.0, Mmin = 5.0,
            Mmax = 7.5, integrated in steps of 0.01 magnitude units; the ground-motion
            prediction equation of Boore, Joyner and Fumal (1993, USGS Open-File Report
            93-509, Table 9, random horizontal component, site class A):
              log10 PGA(g) = -0.105 + 0.229 (M - 6) - 0.778 log10 r,
              r = sqrt(d^2 + 5.57^2),   sigma(log10 PGA) = 0.230,
            valid 5.0 <= M <= 7.7 and d <= 100 km. Annual exceedance rate against PGA,
            with the scatter (lognormal) and without it (median only; "nan" where the
            median never reaches the level, so that pgfplots leaves a gap).
  slope     factor of safety of an infinite slope against the pore-pressure ratio
            r_u = u / (gamma z):
              F = [c' + gamma z (cos^2 b - r_u) tan phi'] / (gamma z sin b cos b)
            for c' = 5 kPa, phi' = 35 deg, gamma = 19 kN/m3, z = 2 m and slope angles
            b = 25, 30 and 35 deg (illustrative soil, not a sourced site).

  part poisson   t_yr P50 P475 P2475
  part survival  t_day observed poisson
  part psha      pga_g rate rate_median
  part slope     r_u F25 F30 F35
  part numbers   key value
"""
import csv
import datetime
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")

# Boore, Joyner and Fumal (1993), Table 9, random horizontal component (ledger bjf93:pga)
B1, B2, B5, H, SIGMA = -0.105, 0.229, -0.778, 5.57, 0.230
GB, GC = 0.162, 0.251


def exceed(t, T):
    """Poisson model: probability of at least one event in time t, return period T."""
    return 1.0 - math.exp(-t / T)


def return_period(p, t):
    """Return period whose exceedance probability in time t is p."""
    return -t / math.log(1.0 - p)


def gmpe_log10(m, d, site="A"):
    """Median log10 PGA (g) of BJF93 at magnitude m and distance d (km)."""
    r = math.sqrt(d * d + H * H)
    g = {"A": 0.0, "B": GB, "C": GC}[site]
    return B1 + B2 * (m - 6.0) + B5 * math.log10(r) + g


def q_normal(z):
    """Upper tail of the standard normal distribution."""
    return 0.5 * math.erfc(z / math.sqrt(2.0))


def p_exceed_pga(a, m, d, sigma=SIGMA):
    mu = gmpe_log10(m, d)
    if sigma == 0.0:
        return 1.0 if mu > math.log10(a) else 0.0
    return q_normal((math.log10(a) - mu) / sigma)


def gr_rate(m, a=4.0, b=1.0, mmax=7.5):
    """Truncated Gutenberg-Richter: annual rate of events of magnitude >= m."""
    return max(10 ** (a - b * m) - 10 ** (a - b * mmax), 0.0)


def hazard(a_g, d=15.0, a=4.0, b=1.0, mmin=5.0, mmax=7.5, dm=0.01, sigma=SIGMA):
    """Annual rate of PGA > a_g (g): sum over magnitude slices of rate x P(PGA > a | m)."""
    n = int(round((mmax - mmin) / dm))
    tot = 0.0
    for i in range(n):
        m0 = mmin + i * dm
        m1 = m0 + dm
        rate = gr_rate(m0, a, b, mmax) - gr_rate(m1, a, b, mmax)
        tot += rate * p_exceed_pga(a_g, 0.5 * (m0 + m1), d, sigma)
    return tot


def hazard_bins(a_g, bins, d, sigma=SIGMA):
    """Hazard from a few magnitude bins given as (rate, representative magnitude)."""
    return sum(rate * p_exceed_pga(a_g, m, d, sigma) for rate, m in bins)


def pga_for_rate(target, fn, lo=0.01, hi=3.0):
    """PGA (g) whose exceedance rate is target, by bisection on log PGA."""
    llo, lhi = math.log(lo), math.log(hi)
    for _ in range(200):
        mid = 0.5 * (llo + lhi)
        if fn(math.exp(mid)) > target:
            llo = mid
        else:
            lhi = mid
    return math.exp(0.5 * (llo + lhi))


def factor_of_safety(beta_deg, r_u, c=5.0, phi_deg=35.0, gamma=19.0, z=2.0, k=0.0):
    """Infinite slope (kPa, kN/m3, m); k = horizontal pseudo-static coefficient."""
    b, p = math.radians(beta_deg), math.radians(phi_deg)
    s, co = math.sin(b), math.cos(b)
    w = gamma * z
    resist = c + w * (co * co - r_u - k * s * co) * math.tan(p)
    drive = w * (s * co + k * co * co)
    return resist / drive


def read_dates(mmin=7.0):
    with open(os.path.join(DERIVED, "usgs-m6.csv"), encoding="utf8") as f:
        return sorted(datetime.date.fromisoformat(r["date"]) for r in csv.DictReader(f)
                      if float(r["mag"]) >= mmin)


def intervals(dates):
    return [(b - a).days for a, b in zip(dates, dates[1:])]


def main():
    rows = [(t, exceed(t, 50), exceed(t, 475), exceed(t, 2475)) for t in range(0, 201, 2)]
    write_table(__file__, ("t_yr", "P50", "P475", "P2475"), rows, part="poisson")

    dates = read_dates(7.0)
    dt = intervals(dates)
    mean = sum(dt) / len(dt)
    rows = [(t, sum(1 for x in dt if x > t) / len(dt), math.exp(-t / mean))
            for t in range(0, 121, 2)]
    write_table(__file__, ("t_day", "observed", "poisson"), rows, part="survival")

    pgas = [10 ** (-2 + 0.05 * i) for i in range(0, 47)]      # 0.01 to 2.0 g
    rows = []
    for a in pgas:
        med = hazard(a, sigma=0.0)
        rows.append((a, hazard(a), med if med > 0.0 else "nan"))
    write_table(__file__, ("pga_g", "rate", "rate_median"), rows, part="psha")

    rows = [(i / 100.0, factor_of_safety(25, i / 100.0), factor_of_safety(30, i / 100.0),
             factor_of_safety(35, i / 100.0)) for i in range(0, 51, 2)]
    write_table(__file__, ("r_u", "F25", "F30", "F35"), rows, part="slope")

    rate475 = 1.0 / return_period(0.10, 50.0)
    sd = math.sqrt(sum((x - mean) ** 2 for x in dt) / len(dt))
    nums = [
        ("T_10pc_50yr", return_period(0.10, 50.0)), ("T_2pc_50yr", return_period(0.02, 50.0)),
        ("P_50yr_T475", exceed(50, 475)), ("P_50yr_T2475", exceed(50, 2475)),
        ("m7_events", len(dates)), ("m7_intervals", len(dt)), ("m7_mean_days", mean),
        ("m7_cv", sd / mean), ("m7_same_day", sum(1 for x in dt if x == 0)),
        ("m7_frac_gt30", sum(1 for x in dt if x > 30) / len(dt)),
        ("m7_exp_gt30", math.exp(-30 / mean)),
        ("psha_rate_m5", gr_rate(5.0)), ("psha_pga475", pga_for_rate(rate475, hazard)),
        ("psha_pga475_median", pga_for_rate(rate475, lambda x: hazard(x, sigma=0.0))),
        ("psha_median_m75_15km", 10 ** gmpe_log10(7.5, 15.0)),
        ("psha_median_m6_15km", 10 ** gmpe_log10(6.0, 15.0)),
        ("F30_dry", factor_of_safety(30, 0.0)), ("F35_dry", factor_of_safety(35, 0.0)),
        ("F25_dry", factor_of_safety(25, 0.0)),
    ]
    write_table(__file__, ("key", "value"), nums, part="numbers")


if __name__ == "__main__":
    main()
