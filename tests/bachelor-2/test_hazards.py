"""Tests of figdata/bachelor-2/hazards.py (Year 2, geological-hazards)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import hazards as hz  # noqa: E402


def test_poisson_and_building_code_return_periods():
    # 10 % in 50 years is 474.6 years and 2 % in 50 years 2475.9 years (USGS table, exact)
    assert abs(hz.return_period(0.10, 50) - 474.56) < 0.01
    assert abs(hz.return_period(0.02, 50) - 2474.9) < 0.1
    assert abs(hz.exceed(50, hz.return_period(0.10, 50)) - 0.10) < 1e-12
    # small-probability limit: P ~ t/T
    assert abs(hz.exceed(1, 1000) - 1e-3) < 1e-6


def test_gmpe_matches_bjf93_and_bjf97():
    # BJF93 log10 coefficients are the BJF97 natural-log ones divided by ln 10
    assert abs(0.527 / math.log(10) - hz.B2) < 5e-4
    assert abs(-0.242 / math.log(10) - hz.B1) < 5e-4
    # at M 6 and d = 0 the distance term uses the fictitious depth h; class C amplifies by
    # 10^0.251
    mu = hz.gmpe_log10(6.0, 0.0)
    assert abs(mu - (hz.B1 + hz.B5 * math.log10(hz.H))) < 1e-12
    assert abs(10 ** (hz.gmpe_log10(6, 10, "C") - hz.gmpe_log10(6, 10)) - 1.782) < 1e-3
    # PGA decreases with distance and grows with magnitude
    assert hz.gmpe_log10(7, 10) > hz.gmpe_log10(6, 10) > hz.gmpe_log10(6, 50)


def test_hazard_curve():
    # at a tiny PGA every event exceeds it: the curve tends to the rate of M >= 5
    assert abs(hz.hazard(1e-4) - hz.gr_rate(5.0)) < 1e-4
    # the curve decreases, and the scatter raises the rare-level hazard
    assert hz.hazard(0.1) > hz.hazard(0.2) > hz.hazard(0.4)
    assert hz.hazard(0.3) > hz.hazard(0.3, sigma=0.0)
    # truncated GR: bins add up to the M >= 5 rate
    assert abs(hz.gr_rate(5) - (0.09 + 0.009 + 0.001 - 10 ** -3.5)) < 1e-12
    a475 = hz.pga_for_rate(1 / hz.return_period(0.1, 50), hz.hazard)
    assert abs(hz.hazard(a475) * hz.return_period(0.1, 50) - 1) < 1e-6
    assert 0.2 < a475 < 0.25


def test_infinite_slope():
    # dry and cohesionless: F = tan(phi) / tan(beta)
    f = hz.factor_of_safety(30, 0.0, c=0.0)
    assert abs(f - math.tan(math.radians(35)) / math.tan(math.radians(30))) < 1e-12
    # F falls linearly with r_u and with a horizontal pseudo-static load
    f0, f1, f2 = (hz.factor_of_safety(30, r) for r in (0.0, 0.1, 0.2))
    assert abs((f0 - f1) - (f1 - f2)) < 1e-12 and f1 < f0
    assert hz.factor_of_safety(30, 0.0, k=0.1) < f0


def test_catalogue_intervals():
    dates = hz.read_dates(7.0)
    dt = hz.intervals(dates)
    assert len(dates) == 696 and len(dt) == 695 and min(dt) >= 0
    mean = sum(dt) / len(dt)
    assert abs(mean - (dates[-1] - dates[0]).days / 695) < 1e-9
    # close to Poisson: coefficient of variation near 1
    sd = math.sqrt(sum((x - mean) ** 2 for x in dt) / len(dt))
    assert 1.0 < sd / mean < 1.15
