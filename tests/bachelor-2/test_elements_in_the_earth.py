"""Tests for the element-abundance figure data (geochem.py)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import geochem as g  # noqa: E402


def test_oxide_conversions():
    # K2O 1 wt % holds 0.830 wt % K; TiO2 1 wt % holds 0.599 wt % Ti
    assert abs(g.K_IN_K2O - 0.8301) < 2e-4
    assert abs(g.TI_IN_TIO2 - 0.5993) < 2e-4


def test_refractory_lithophiles_are_chondritic_relative_to_each_other():
    # refractory lithophile elements keep the same ratios as in CI: Mg-normalised
    # values within a narrow band; volatile and siderophile elements far below
    refr = [g.mg_normalised(e) for e in ("Al", "Ca", "Ti", "Sc", "Y", "Zr", "La", "Yb", "Lu")]
    assert max(refr) / min(refr) < 1.2
    assert all(g.mg_normalised(e) < 0.25 for e in ("K", "Na", "Rb", "Mn"))
    assert all(g.mg_normalised(e) < 0.01 for e in ("Ir", "Os", "Pt", "Au", "Re"))


def test_eu_anomaly_definition():
    # a smooth pattern has no anomaly: Eu_N = sqrt(Sm_N Gd_N) gives exactly 1
    comp = {"Sm": 2 * g.CI["Sm"], "Gd": 8 * g.CI["Gd"], "Eu": 4 * g.CI["Eu"]}
    assert abs(g.eu_anomaly(comp) - 1) < 1e-12
    assert g.eu_anomaly(g.UCC) < 0.75 < 0.95 < g.eu_anomaly(g.MORB)


def test_bulk_d_is_mode_weighted():
    assert abs(g.bulk_d("La") - (0.65 * 0.058 + 0.18 * 0.001 + 0.17 * 0.001)) < 1e-12
    assert sum(g.MODES) == 1.0
    # garnet makes the heavy rare earths compatible in the rock
    assert g.bulk_d("Lu") > 1 > g.bulk_d("Gd")


def test_core_fraction_mass_balance():
    x = g.core_fraction("Fe")
    # Fe balance closes: bulk Fe/Mg equals CI Fe/Mg
    bulk_fe = (1 - x) * g.PM["Fe"] + x * g.CORE["Fe"] * 1e4
    bulk_mg = (1 - x) * g.PM["Mg"]
    assert abs(bulk_fe / bulk_mg - g.CI["Fe"] / g.CI["Mg"]) < 1e-12
    assert abs(x - 0.3033) < 2e-4
    assert abs(g.core_fraction("Ni") - 0.3098) < 2e-4
    # least squares lies between the two estimates, nearer Fe (larger weight)
    xl = g.core_fraction_lsq()
    assert x <= xl <= g.core_fraction("Ni") and xl - x < g.core_fraction("Ni") - xl


def test_prem_core_fraction():
    xp, m = g.prem_core_fraction()
    assert abs(m / 5.9722e24 - 1) < 0.002          # NASA mass of the Earth
    assert abs(xp - 0.325) < 0.002


def test_normalised_patterns():
    ree = dict(zip(g.REE, g.normalised(g.UCC, g.CI, g.REE)))
    assert ree["La"] > 100 and ree["La"] / ree["Yb"] > 10
    morb = dict(zip(g.REE, g.normalised(g.MORB, g.CI, g.REE)))
    assert morb["La"] / morb["Sm"] < 1                 # light rare earths slightly depleted
    assert math.isclose(g.MORB["Ti"], 1.68e4 * g.TI_IN_TIO2)


def test_core_share():
    x = 0.325
    assert g.core_share("Al", x) == 0
    # gold: 0.325 x 0.5 ppm in the core against 0.675 x 0.001 ppm in the silicate Earth
    assert abs(g.core_share("Au", x) - 0.1625 / (0.1625 + 0.000675)) < 1e-12
    shares = [g.core_share(e, x) for e in g.BUDGET]
    assert shares == sorted(shares, reverse=True)
