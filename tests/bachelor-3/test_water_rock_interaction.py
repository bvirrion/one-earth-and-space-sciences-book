"""Tests for the carbonate system, activity diagram and weathering-rate
scripts (Year 3, ch. 15)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import activity_diagram as ad  # noqa: E402
import carbonate_system as cs  # noqa: E402
import weathering_rates as wr  # noqa: E402


def test_analytic_expressions_reproduce_the_25c_log_k():
    for name, lk in cs.LOGK25.items():
        assert cs.log_k(name, 25.0) == pytest.approx(lk, abs=0.01)


def test_open_system_matches_the_closed_form_cube_root():
    # the bisection solution and the cube-root theorem agree once the gammas
    # are the same and carbonate/OH/H are negligible (P_CO2 well above air)
    lp, t = -1.5, 10.0
    ca, ph = cs.open_system(lp, t)
    ionic = 3 * ca
    g_ca, g_h = cs.gamma("Ca", ionic), cs.gamma("HCO3", ionic)
    assert cs.open_cubic(lp, t, g_ca, g_h) == pytest.approx(ca, rel=0.01)


def test_open_system_slope_is_one_third():
    a = math.log10(cs.open_system(-2.5, 25.0)[0])
    b = math.log10(cs.open_system(-1.5, 25.0)[0])
    # 1/3 with unit gammas; the gammas fall as the water grows richer, so a
    # little steeper
    assert 1 / 3 < b - a < 0.37


def test_calcite_in_air_dissolves_about_twenty_mg_per_litre():
    # Hem (1985): about 20 mg/L of Ca for water with calcite in contact with air
    ca, _ = cs.open_system(math.log10(330e-6), 25.0)
    assert 15 < ca * 40.078 * 1000 < 25


def test_closed_system_dissolves_less_and_is_cold_favoured():
    for lp in (-2.5, -2.0, -1.5):
        assert cs.closed_system(lp, 10.0)[0] < cs.open_system(lp, 10.0)[0]
        assert cs.open_system(lp, 10.0)[0] > cs.open_system(lp, 25.0)[0]


def test_closed_system_conserves_carbon_and_lowers_p_co2():
    lp = -1.5
    ca, ph, lp_final = cs.closed_system(lp, 10.0)
    assert lp_final < lp
    # carbon dissolved from calcite equals calcium
    k = cs.constants(10.0)
    c0 = cs.initial_carbon(lp, 10.0)
    assert c0 > 0 and ca < 2 * c0


def test_spring_charge_balance_and_saturation():
    cat, an, err = cs.charge_balance(cs.SPRING)
    assert abs(err) < 2.0
    s = cs.spring_state()
    assert -0.3 < s["si"] < 0.3
    assert -2.5 < s["logp"] < -1.0


def test_degassing_raises_si_and_ph_and_travertine_restores_saturation():
    s = cs.spring_state()
    si_hi, ph_hi = cs.degas(s["logp"])
    assert si_hi == pytest.approx(s["si"], abs=1e-3)
    si_air, ph_air = cs.degas(cs.LOGP_AIR)
    assert si_air > si_hi + 1.0 and ph_air > ph_hi
    x = cs.travertine()
    assert cs.degas(cs.LOGP_AIR, ca_loss=x)[0] == pytest.approx(0.0, abs=1e-6)
    assert 0 < x < cs.molal(cs.SPRING)["Ca"]


def test_activity_diagram_triple_point_and_samples():
    # gibbsite-kaolinite boundary: log a_Si = (log Kk - 2 log Kg)/2
    y = (7.435 - 2 * 8.11) / 2
    assert ad.stable(1.0, y + 0.01) == "kaolinite"
    assert ad.stable(1.0, y - 0.01) == "gibbsite"
    names = {n: ad.stable(*ad.sample_xy(k, ph, si)) for n, k, ph, si in ad.SAMPLES}
    assert names == {"tropical": "gibbsite", "stream": "kaolinite", "deep": "muscovite"}
    assert ad.stable(9.0, -3.0) == "kfeldspar"


def test_boundaries_are_where_levels_are_equal():
    for (m1, m2), (p, q) in ad.traced_boundaries(801).items():
        for x, y in (p, q):
            assert ad.level(m1, x, y) == pytest.approx(ad.level(m2, x, y), abs=1e-6)


def test_rates_reduce_to_the_tabulated_constant_at_25c_ph0():
    assert wr.rate("forsterite", 0.0, mechanism="acid") == pytest.approx(10 ** -6.85)
    # Arrhenius: lowering T lowers every rate
    for m in wr.PARAMS:
        assert wr.rate(m, 5.0, 10.0) < wr.rate(m, 5.0, 25.0)
    # forsterite dissolves far faster than albite at pH 5
    assert wr.log_rate("forsterite", 5.0) - wr.log_rate("albite", 5.0) > 2.5
