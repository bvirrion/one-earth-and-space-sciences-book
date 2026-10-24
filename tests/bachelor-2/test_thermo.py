"""Tests for the atmospheric-thermodynamics figure data (figdata/bachelor-2/thermo.py)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import thermo as th  # noqa: E402


def test_constants():
    assert th.RD == pytest.approx(287.0, abs=0.05)
    assert th.RV == pytest.approx(461.5, abs=0.05)
    assert th.EPS == pytest.approx(0.622, abs=0.001)
    assert th.CP == pytest.approx(1004.5, abs=0.1)
    # the dry adiabatic lapse rate of the Year 1 volume
    assert th.G / th.CP * 1000 == pytest.approx(9.76, abs=0.01)


def test_saturation_vapour_pressure():
    assert th.es(th.TT) == pytest.approx(th.PT)
    assert th.es_ice(th.TT) == pytest.approx(th.PT)
    for t, p in th.NIST:
        T = t + 273.15
        # constant-L Clausius--Clapeyron: within 5 % up to 40 degC, always above (L falls with T)
        assert 1.0 - 1e-4 <= th.es(T) / p < 1.05
        # the empirical formula: within 0.5 %
        assert th.es_emp(T) / p == pytest.approx(1.0, abs=0.005)
    # about 7 % per kelvin near 0 degC, 6 % near 25 degC
    assert 100 * th.L / (th.RV * 273.15 ** 2) == pytest.approx(7.26, abs=0.01)
    assert 100 * th.L / (th.RV * 298.15 ** 2) == pytest.approx(6.10, abs=0.01)
    # over supercooled water the vapour pressure is about 10 % above that over ice at -10 degC
    assert th.es_emp(263.15) / th.es_ice(263.15) == pytest.approx(1.10, abs=0.01)
    for T in (250.0, 270.0, 290.0):
        assert th.dew_point(th.es(T)) == pytest.approx(T)


def test_moist_adiabat():
    # dT/dp and the lapse rate are the same law through the hydrostatic balance
    for T, p in ((290.0, 9.0e4), (260.0, 5.0e4)):
        assert th.gamma_s(T, p) == pytest.approx(th.dTdp_moist(T, p) * p * th.G / (th.RD * T))
    # textbook range: about 4 K/km warm and moist, approaching the dry rate when cold
    assert 4.0 < th.gamma_s(293.15, 1.0e5) * 1000 < 4.5
    assert th.gamma_s(213.15, 2.0e4) * 1000 == pytest.approx(th.G / th.CP * 1000, abs=0.3)
    # theta_e-like check: the pseudo-adiabat conserves T exp(L r_s/(c_p T)) * (p0/p)^k roughly
    T1 = th.moist(293.15, 1.0e5, 5.0e4)
    def thetae(T, p):
        return th.theta(T, p) * math.exp(th.L * th.rs(T, p) / (th.CP * T))
    assert thetae(T1, 5.0e4) == pytest.approx(thetae(293.15, 1.0e5), rel=0.01)


def test_lcl():
    p0, T0, Td0 = 97109.0, 292.15, 291.65
    plcl, Tlcl = th.lcl(T0, Td0, p0)
    r0 = th.mixing_ratio(th.es(Td0), p0)
    assert th.rs(Tlcl, plcl) == pytest.approx(r0, rel=1e-6)
    assert th.theta(Tlcl, plcl) == pytest.approx(th.theta(T0, p0))
    # the 125-metre rule
    z = th.lcl_height_rule(T0, Td0)
    assert z / (T0 - Td0) == pytest.approx(125.0, abs=2.0)


def test_sounding_cape():
    d = th.numbers()
    assert d["sfc_p"] == pytest.approx(971.09)
    assert 850 > d["lfc_p"] > 700
    # the equilibrium level lies near the reported tropopause (235.3 hPa)
    assert d["el_p"] == pytest.approx(235.3, abs=10)
    assert 1500 < d["cape"] < 2500 and d["cape_v"] > d["cape"]
    assert d["cin"] < 0 and d["cin_v"] > d["cin"]
    assert d["w_max"] == pytest.approx(math.sqrt(2 * d["cape"]))
    assert d["lcl_z_agl"] == pytest.approx(d["lcl_rule_agl"], abs=3)
    # the lifted index from the table levels
    assert d["lifted_index"] == pytest.approx(d["Te500"] - d["Tp500"])
    rows = th.problem_table()
    assert rows[0][2] == rows[0][4] == 19.0
    assert [r[0] for r in rows] == list(th.TABLE_P)


def test_kohler():
    for dd in (30, 50, 100):
        Dc, sc = th.kohler_critical(dd * 1e-9)
        Dca, sca = th.kohler_critical_approx(dd * 1e-9)
        assert sca == pytest.approx(sc, rel=0.01)
        assert Dca == pytest.approx(Dc, rel=0.01)
    # s_c scales as Dd^(-3/2)
    s30 = th.kohler_critical_approx(30e-9)[1]
    s100 = th.kohler_critical_approx(100e-9)[1]
    assert s30 / s100 == pytest.approx((100 / 30) ** 1.5)
    # kappa = 0 gives the Kelvin equation
    assert th.kohler_S(1e-6, 1e-8, kappa=0.0) == pytest.approx(math.exp(th.kohler_A() / 1e-6), rel=1e-5)
