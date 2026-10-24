"""Tests for the mantle-melting figure data (melting.py)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import melting as mm  # noqa: E402


def test_bowen_andersen_peritectic():
    # MgSiO3 melts to 5.5 % forsterite + 94.5 % liquid (Bowen and Andersen 1914, p. 492)
    assert abs(mm.peritectic_forsterite_fraction() - 0.055) < 0.001
    # compositions in the right order along the SiO2 axis
    assert mm.SIO2_FO < mm.FO_LIQ_117[0] < mm.SIO2_EN < mm.PERITECTIC[0] < mm.EUTECTIC_EN_CR[0]
    # the liquidus falls from forsterite to the eutectic
    temps = [mm.FO_MELT, mm.FO_LIQ_117[1], mm.FO_LIQ_EN[1], mm.PERITECTIC[1], mm.EUTECTIC_EN_CR[1]]
    assert all(a > b for a, b in zip(temps, temps[1:]))


def test_di_an_eutectic():
    # the liquidus has its minimum at the eutectic, and each datum lies in its bracket
    xs = [i / 2 for i in range(201)]
    tmin = min(xs, key=mm.di_an_liquidus)
    assert tmin == 42.0 and mm.di_an_liquidus(42.0) == 1270.0
    for x, lo, hi in mm.DI_AN_BRACKETS:
        assert lo < mm.di_an_liquidus(x) < hi
    # lever rule: Di70An30 at the eutectic has crystallised 1 - 30/42 of its mass as diopside
    assert abs(1 - mm.lever(30, 0, 42) - 0.2857) < 1e-4


def test_onset_and_adiabat():
    # gradient alpha T/(rho cp) near 20 K/GPa (Katz et al.: about 18 K/GPa at 1500 K)
    assert abs(mm.adiabat_gradient(1350) - 19.7) < 0.1
    assert abs(mm.adiabat_gradient(1500 - 273.15) - 18.2) < 0.1
    # straight and exponential adiabats give the same onset; hotter mantle melts deeper
    assert abs(mm.onset_pressure(1350) - mm.onset_linear(1350, 20.0)) < 0.01
    assert mm.onset_pressure(1300) < mm.onset_pressure(1350) < mm.onset_pressure(1450)
    p0 = mm.onset_pressure(1350)
    assert abs(mm.adiabat(1350, p0) - mm.t_solidus(p0)) < 1e-6


def test_productivity_matches_isentrope():
    # the productivity formula equals the slope of the conserved-entropy solution (T' model)
    tp, p = 1350, 1.5
    f1 = mm.melt_fraction(tp, p + 0.005, beta=1.0, m_cpx=1.0)
    f2 = mm.melt_fraction(tp, p - 0.005, beta=1.0, m_cpx=1.0)
    fm = mm.melt_fraction(tp, p, beta=1.0, m_cpx=1.0)
    slope = (f2 - f1) / 0.01
    assert abs(slope - mm.productivity(p, fm, beta=1.0)) < 0.002
    assert 0.08 < mm.productivity(1.5, 0.1) < 0.15


def test_triangle_and_crust():
    # constant productivity: h = int F dz = F_max H / 2
    fmax, height, n = 0.24, 82.0, 10000
    integ = sum(fmax * (1 - (i + 0.5) / n) for i in range(n)) * height / n
    assert abs(integ - mm.triangle_crust(fmax, height)) < 1e-6
    # crust thickens with potential temperature; a normal mantle makes crust of order 7 km
    h = [mm.column(tp, n=300)[3] for tp in (1300, 1350, 1450)]
    assert h[0] < h[1] < h[2]
    assert 5 < h[1] < 11 and 15 < h[2] < 25


def test_water():
    # 13 wt % water at saturation at 1 GPa (Katz et al., section 1, item 7)
    assert abs(mm.x_saturation(1.0) - 13.0) < 1e-12
    assert mm.x_saturation(0.0) == 0.0
    assert abs(mm.delta_t_water(1.0) - 43.0) < 1e-12
    assert mm.delta_t_water(mm.x_saturation(2.0)) > mm.delta_t_water(mm.x_saturation(1.0))
