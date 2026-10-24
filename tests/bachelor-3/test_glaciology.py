"""Tests for the glaciology scripts (Year 3, ch. 24)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import ice_flow as fl  # noqa: E402
import sea_ice as si  # noqa: E402


def test_softness_paterson_budd():
    # continuous enough at -10 degC (the two branches agree within a factor 1.1)
    lo = fl.softness(263.15 - 1e-6)
    hi = fl.softness(263.15 + 1e-6)
    assert hi / lo == pytest.approx(1.0, abs=0.1)
    # about 1e-16 Pa^-3 a^-1 at the melting point (the isothermal Glen value of PISM)
    assert fl.softness(273.15) * fl.SEC_YR == pytest.approx(3.1689e-24 * 3.156e7, rel=0.5)


def test_slab_profile_obeys_glen_and_integrates_to_the_flux():
    h, alpha, a = 500.0, 0.02, 1e-24
    dz = 1e-3
    for z in (10.0, 250.0, 450.0):
        dudz = (fl.slab_velocity(z + dz, h, alpha, a) - fl.slab_velocity(z - dz, h, alpha, a)) / (2 * dz)
        tau = fl.RHO_I * fl.G * (h - z) * math.sin(alpha)
        assert dudz == pytest.approx(2 * a * tau ** 3, rel=1e-6)
    n = 4000
    q = sum(fl.slab_velocity((i + 0.5) * h / n, h, alpha, a) for i in range(n)) * h / n
    assert q == pytest.approx(fl.slab_flux(h, alpha, a), rel=1e-5)
    assert fl.slab_velocity(0.0, h, alpha, a) == 0.0


def test_nye_profile_is_plastic_and_cap_volume():
    tau0 = 1e5
    x, dx = 7000.0, 1e-2
    h = fl.nye(x, tau0)
    dhdx = (fl.nye(x + dx, tau0) - fl.nye(x - dx, tau0)) / (2 * dx)
    assert fl.RHO_I * fl.G * h * dhdx == pytest.approx(tau0, rel=1e-6)
    # cap volume by direct integration
    n = 20000
    r = fl.CAP_R
    v = sum(2 * math.pi * ((i + 0.5) * r / n) * fl.nye(r - (i + 0.5) * r / n, tau0) for i in range(n)) * r / n
    assert v == pytest.approx(fl.cap_volume(), rel=1e-4)


def test_greenland_fit_is_of_order_one_bar():
    rows = fl.transect()
    assert max(h for _, h in rows) == 3229
    for side in ("w", "e"):
        tau0, xm, top, rms, n = fl.fit_side(rows, side)
        assert 50e3 < tau0 < 150e3
        assert n > 100


def test_stefan_growth():
    t = 100 * 86400.0
    g = si.grow(days=100)
    assert g[-1][1] == pytest.approx(si.stefan(t), rel=1e-3)
    # h^2 grows linearly in time
    assert si.stefan(4 * t) == pytest.approx(2 * si.stefan(t))
    # snow slows the growth
    assert si.grow(days=100, hs=0.2)[-1][1] < 0.6 * g[-1][1]
    assert si.L_FUS == pytest.approx(3.34e5)


def test_sea_ice_trends_negative():
    bm, _ = si.trend(si.read("mar"))
    bs, _ = si.trend(si.read("sep"))
    assert bs < bm < 0
