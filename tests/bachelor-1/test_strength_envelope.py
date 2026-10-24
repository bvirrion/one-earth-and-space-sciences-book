"""Tests for the strength envelopes of chapter 16: Byerlee's law, the brittle strength
from a Mohr circle tangent to it (the chapter's proposition), the creep strength, and
the brittle-ductile transitions printed in the text."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import strength_envelope as se  # noqa: E402


def test_byerlee_is_continuous_at_200_mpa():
    assert abs(se.byerlee_tau(200.0) - 170.0) < 1e-9
    assert abs(0.85 * 200.0 - (50.0 + 0.6 * 200.0)) < 1e-9
    assert abs(se.byerlee_tau(100.0) - 85.0) < 1e-9          # low branch
    assert abs(se.byerlee_tau(400.0) - 290.0) < 1e-9         # high branch


def test_brittle_slopes_match_the_closed_form():
    # S = rho g (1 - lambda) per km; slope = 2 mu S / (sqrt(1 + mu^2) +- mu)
    mu, k = 0.85, math.sqrt(1 + 0.85 ** 2)
    s = 2700 * 9.81 * 1e3 * (1 - 1000 / 2700) * 1e-6
    _, _, v = se.analysis()
    assert abs(v["slope_normal_MPa_km"] - 2 * mu * s / (k + mu)) < 1e-9
    assert abs(v["slope_thrust_MPa_km"] - 2 * mu * s / (k - mu)) < 1e-9
    assert abs(v["slope_strike_MPa_km"] - 2 * mu * s / k) < 1e-9
    assert 13.0 < v["slope_normal_MPa_km"] < 13.2 and 61.2 < v["slope_thrust_MPa_km"] < 61.4


def test_the_failure_circle_touches_byerlee_line():
    for regime in ("normal", "thrust"):
        for s_eff in (10.0, 80.0, 300.0, 900.0):
            d = se.brittle_diff(s_eff, regime)
            r = d / 2
            if regime == "normal":
                c = s_eff - r          # sigma_1 = S fixed, sigma_3 = S - 2r
            else:
                c = s_eff + r          # sigma_3 = S fixed, sigma_1 = S + 2r
            # largest value of tau - envelope over the circle is zero (tangent, not cut)
            gap = max(r * math.sin(a) - se.byerlee_tau(c + r * math.cos(a))
                      for a in (i * math.pi / 2000 for i in range(2001)))
            assert abs(gap) < 1e-3 * max(1.0, r)


def test_the_tangent_point_gives_the_coulomb_angle():
    # tangent to tau = mu sigma: 2 theta = 90 deg + phi, theta = angle (normal, sigma_1)
    mu = 0.85
    phi = math.atan(mu)
    s_eff = 50.0
    r = se.brittle_diff(s_eff, "thrust") / 2
    c = s_eff + r
    best = max(range(1, 18000), key=lambda i: r * math.sin(i * math.pi / 18000)
               - mu * (c + r * math.cos(i * math.pi / 18000)))
    two_theta = best * 180.0 / 18000
    assert abs(two_theta - (90.0 + math.degrees(phi))) < 0.02


def test_creep_strength_falls_with_temperature_and_rises_with_rate():
    p = 5e8
    last = math.inf
    for t in range(200, 1200, 50):
        s = se.creep_diff(t, p, se.QUARTZ_WET)
        assert s < last
        last = s
    s1 = se.creep_diff(500.0, p, se.QUARTZ_WET, rate=1e-15)
    s2 = se.creep_diff(500.0, p, se.QUARTZ_WET, rate=1e-14)
    assert abs(s2 / s1 - 10 ** 0.25) < 1e-9


def test_creep_formula_inverts_the_flow_law():
    law, t, p = se.OLIVINE_DRY, 900.0, 2e9
    s = se.creep_diff(t, p, law)
    rate = law["A"] * s ** law["n"] * math.exp(-(law["E"] + p * law["V"]) / (se.R_GAS * (t + 273.15)))
    assert abs(rate / se.RATE - 1.0) < 1e-9


def test_transitions_are_where_the_curves_cross():
    cont, ocean, v = se.analysis()
    for rows, key, col in ((cont, "cont_bdt_thrust", 1), (cont, "cont_bdt_normal", 2),
                           (ocean, "ocean_bdt_thrust", 1)):
        z = v[key + "_km"]
        above = [r for r in rows if r[0] < z - 0.3]
        below = [r for r in rows if z + 0.3 < r[0] < z + 3]
        assert all(r[col] <= r[3] for r in above[1:])
        assert all(r[col] > r[3] for r in below)
    # figures printed in the chapter
    assert 13.0 < v["cont_bdt_thrust_km"] < 14.5 and 16.5 < v["cont_bdt_normal_km"] < 17.5
    assert 240.0 < v["T_cont_bdt_thrust"] < 260.0
    assert 37.0 < v["ocean_bdt_thrust_km"] < 39.0 and 630.0 < v["T_ocean_bdt_thrust"] < 650.0
    assert 44.0 < v["cont_mantle_bdt_thrust_km"] < 45.5
    assert v["olivine_moho_MPa"] > 1000 * v["quartz_moho_MPa"]
    # the strength is the lower of the two curves
    for d, th, no, du, st in cont + ocean:
        assert st == min(th, du)
