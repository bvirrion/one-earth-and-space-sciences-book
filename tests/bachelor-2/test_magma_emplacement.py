"""Tests for the magma figure data (magma.py)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import magma as mg  # noqa: E402


def test_grd_worked_example():
    # the authors' tutorial, Table 2: B 7720, C 334, log eta 3.67 at 1273 K
    b, c = mg.grd_bc(mg.GRD_EXAMPLE)
    assert abs(b - 7720) < 10 and abs(c - 334) < 1.5
    assert abs(mg.log_viscosity(mg.GRD_EXAMPLE, 1273 - 273.15) - 3.67) < 0.01


def test_viscosity_order_and_water():
    # basalt < andesite < rhyolite at any temperature; water lowers rhyolite viscosity
    for t in (900, 1000, 1200):
        assert (mg.log_viscosity(mg.MORB, t) < mg.log_viscosity(mg.ANDESITE, t)
                < mg.log_viscosity(mg.RHYOLITE, t))
    assert 1 < mg.log_viscosity(mg.MORB, 1200) < 3          # tens to hundreds of Pa s
    dry, wet = mg.log_viscosity(mg.RHYOLITE, 800), mg.log_viscosity(mg.with_water(mg.RHYOLITE, 4), 800)
    assert dry - wet > 4                                    # four orders of magnitude or more
    # the hydrous rhyolite agrees with the independent Hess & Dingwell (1996) equation
    w, t = 4.0, 1073.15
    hd = (-3.545 + 0.833 * math.log(w)) + (9601 - 2368 * math.log(w)) / (t - (195.7 + 32.25 * math.log(w)))
    assert abs(hd - wet) < 0.5                              # within the 0.46 log-unit scatter


def test_density():
    rb = mg.density(mg.MORB, 1200)
    rr = mg.density(mg.RHYOLITE, 850)
    assert 2650 < rb < 2780 and 2250 < rr < 2400
    # 1 wt % water lowers density, as much as a few hundred degrees of heating (DensityX text)
    d_w = mg.density(mg.MORB, 1200) - mg.density(mg.with_water(mg.MORB, 1), 1200)
    d_t = mg.density(mg.MORB, 1200) - mg.density(mg.MORB, 1500)
    assert d_w > 0 and 0.5 < d_t / d_w < 2
    # pressure increases density
    assert mg.density(mg.MORB, 1200, 5000) > rb


def test_solubility_fit():
    sb, sr = mg.sqrt_fit(mg.BASALT_H2O), mg.sqrt_fit(mg.RHYOLITE_H2O)
    assert 0.30 < sb < 0.38 and 0.40 < sr < 0.50 and sr > sb
    # the fit passes within about 1 wt % of every measurement
    for data, s in ((mg.BASALT_H2O, sb), (mg.RHYOLITE_H2O, sr)):
        assert all(abs(s * math.sqrt(p / 10) - w) < 1.1 for p, _, w in data)
    assert abs(mg.saturation_pressure(5.0, sr) - (5.0 / sr) ** 2) < 1e-12


def test_sill_cooling():
    b, tm, t0 = 100.0, 1150.0, 100.0
    # the contact temperature is the mean of the two, from the first instant on
    for t in (1e5, 1e7, 1e8):
        assert abs(mg.sill_temperature(b / 2, t, b, tm, t0) - (tm + t0) / 2) < 0.6
    # symmetric, and the centre cools monotonically
    assert abs(mg.sill_temperature(30, 3e8, b, tm, t0) - mg.sill_temperature(-30, 3e8, b, tm, t0)) < 1e-9
    cs = [mg.sill_temperature(0, t, b, tm, t0) for t in (1e8, 1e9, 1e10)]
    assert cs[0] > cs[1] > cs[2] > t0


def test_stefan():
    lam = mg.stefan_lambda()
    lhs = mg.LATENT * math.sqrt(math.pi) / (mg.RHO_C * 1050)
    assert abs(math.exp(-lam ** 2) / (lam * (1 + math.erf(lam))) - lhs) < 1e-9
    assert abs(lam - 0.653) < 0.002
    years = mg.solidification_time(100.0, lam) / mg.YEAR
    assert 64 < years < 69          # the problem's named number, 67 years with lambda = 0.65
    # more latent heat, slower front
    assert mg.stefan_lambda(latent=1.0e9) < lam
