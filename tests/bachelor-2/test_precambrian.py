"""Tests for the Precambrian figure data (figdata/bachelor-2/precambrian.py)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import precambrian as pc  # noqa: E402


def test_heat_production_today_and_back_in_time():
    # per kg of element (Dye 2012): U 98.5, Th 26.3 microW/kg; our isotope sum must agree
    u_per_kg = (pc.heat("U238") + pc.heat("U235")) / pc.U
    assert u_per_kg == pytest.approx(98.5e-6, rel=0.01)
    assert pc.heat("Th232") / pc.TH == pytest.approx(26.3e-6, rel=0.01)
    # each isotope grows back in time as exp(lambda t); after one half-life it doubles
    for n in pc.ISO:
        assert pc.heat(n, pc.ISO[n][2]) == pytest.approx(2 * pc.heat(n))
    # today about 4.9 pW/kg; 3 Ga ago more than twice as much, with K-40 the leader
    assert pc.heat_total() * 1e12 == pytest.approx(4.907, abs=0.002)
    assert pc.heat_total(3.0) / pc.heat_total() == pytest.approx(2.319, abs=0.002)
    h3 = {n: pc.heat(n, 3.0) for n in pc.ISO}
    assert max(h3, key=h3.get) == "K40"
    assert max(pc.ISO, key=pc.heat) == "Th232"


def test_komatiite_line_passes_through_both_experiments():
    assert pc.liquidus(32.2) == pytest.approx(1616.0)
    assert pc.liquidus(23.0) == pytest.approx(1450.0)
    assert pc.SLOPE == pytest.approx(18.04, abs=0.01)
    assert pc.liquidus(32.2) - pc.liquidus(12.0) == pytest.approx(364.5, abs=0.1)


def test_energy_balance_today_has_three_equilibria_and_the_right_stability():
    snow, mid, warm = pc.equilibria(1.0)
    assert warm == pytest.approx(288.0)
    assert snow < pc.T1 < mid < pc.T2 < warm
    for T in (snow, mid, warm):
        assert pc.absorbed(T) == pytest.approx(pc.emitted(T), rel=1e-9)
    # stable where emission rises faster than absorption, unstable in the middle
    h = 0.01
    slope = lambda T: (pc.absorbed(T + h) - pc.emitted(T + h) - pc.absorbed(T - h) + pc.emitted(T - h)) / (2 * h)
    assert slope(snow) < 0 and slope(warm) < 0 and slope(mid) > 0


def test_tipping_points_and_the_faint_young_sun():
    sf, sm = pc.s_freeze(), pc.s_melt()
    assert 0.93 < sf < 0.94 and 1.22 < sm < 1.23
    assert pc.equilibria(sf - 1e-4)[2] is None and pc.equilibria(sf + 1e-4)[2] is not None
    assert pc.equilibria(sm + 1e-4)[0] is None and pc.equilibria(sm - 1e-4)[0] is not None
    # Gough: 0.741 four billion years ago (Book 2), the warm state lost before about 0.83 Ga
    assert pc.lum(4.0) == pytest.approx(0.7406, abs=1e-4)
    assert pc.lum(pc.ago_for_lum(sf)) == pytest.approx(sf)
    assert pc.equilibria(pc.lum(4.0))[1:] == (None, None)
    # a snowball under 0.94 S0 melts once its emissivity falls to eps_to_melt
    e = pc.eps_to_melt(0.94)
    assert pc.equilibria(0.94, e)[0] == pytest.approx(pc.T1)


def test_co2_build_up():
    # the 1981 estimate quoted by Hoffman et al.: 1 bar in about 20 Myr at today's rate
    assert pc.one_bar_time() / 1e6 == pytest.approx(20.0, abs=0.1)
    assert pc.M_CO2 == pytest.approx(44.009)
    assert pc.co2_time(0.1) / pc.co2_time(0.01) == pytest.approx(10 * 0.99 / 0.9)
    assert pc.co2_time(0.01) / 1e6 == pytest.approx(0.301, abs=0.001)
