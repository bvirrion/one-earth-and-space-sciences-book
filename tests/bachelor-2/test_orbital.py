"""Tests for figdata/bachelor-2/orbital.py (ch. 25 orbital-forcing)."""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "bachelor-2"))
import orbital as ob  # noqa: E402


def test_reproduces_the_tabulated_july_insolation_at_65n():
    rows = [r for r in ob.orbit() if r["age"] <= 1000]
    assert len(rows) == 1001
    worst = max(abs(ob.daily_insolation(65, ob.JULY, r["e"], r["om"], r["eps"]) - r["jul"])
                for r in rows)
    assert worst < 0.02


def test_climatic_precession_column_is_e_sin_omega():
    for r in ob.orbit()[:200]:
        assert abs(r["e"] * math.sin(math.radians(r["om"])) - r["prec"]) < 6e-5


def test_perihelion_falls_early_january_today():
    r = ob.orbit()[0]
    # the Sun's longitude at perihelion is omega + 180 deg: 11 deg past the December solstice
    assert 280 < r["om"] + 180 < 283
    assert ob.distance_factor(r["om"] + 180, r["e"], r["om"]) > ob.distance_factor(r["om"], r["e"], r["om"])


def test_global_annual_mean_is_s0_over_4_sqrt():
    e, eps = 0.05, 23.0
    n = 72
    tot = 0.0
    for k in range(n):
        lat = -90 + (k + 0.5) * 180.0 / n
        tot += ob.annual_mean(lat, e, eps, n=720) * math.cos(math.radians(lat))
    tot *= (math.pi / n) / 2.0
    assert abs(tot - ob.S0 / (4 * math.sqrt(1 - e * e))) < 0.5


def test_pole_annual_mean_formula_and_obliquity():
    for eps in (22.1, 24.5):
        assert abs(ob.annual_mean(90, 0.0167, eps) - ob.pole_annual(0.0167, eps)) < 0.2
    assert ob.pole_annual(0.0167, 24.5) > ob.pole_annual(0.0167, 22.1)


def test_lag_model_exact_response_to_a_step():
    v = ob.lag_model([1.0] * 30, tau=10.0)
    assert abs(v[9] - (1 - math.exp(-1.0))) < 1e-12


def test_spectral_peaks():
    n = ob.numbers()
    assert 19 <= n["peak_ins"] <= 24
    assert 80 <= n["peak_young"] <= 120
    assert 39 <= n["peak_old"] <= 43
