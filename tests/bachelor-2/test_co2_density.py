"""Tests of figdata/bachelor-2/co2_density.py (Year 2, energy-geology)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import co2_density as c  # noqa: E402


def test_profile():
    prof = c.read_profile()
    assert len(prof) == 31 and prof[0][0] == 0 and prof[-1][0] == 3000
    # the conditions of the IPCC SRCCS Figure 5.2: 15 degC + 25 degC/km, hydrostatic pressure
    for z, t, p, _ in prof:
        assert abs(t - (15 + 0.025 * z)) < 1e-3
        assert abs(p - (0.101325 + 9.80665e-3 * z)) < 1e-5
    # density rises with depth, steeply around 800 m, and levels off below 1.5 km
    rho = [r for *_, r in prof]
    assert all(b > a for a, b in zip(rho, rho[1:]))
    assert c.rho_at(900) - c.rho_at(700) > 300
    assert c.rho_at(3000) - c.rho_at(1500) < 0.05 * c.rho_at(1500)


def test_critical_crossing():
    d = c.critical_depths()
    assert abs(d["z_pc"] - (7.380 - 0.101325) / 9.80665e-3) < 0.5
    assert abs(d["z_tc"] - (304.18 - 273.15 - 15) / 0.025) < 0.5
    assert d["z_tc"] < d["z_pc"] < 800


def test_storage_capacity():
    # 1 km2, 10 m thick, porosity 0.2, 700 kg/m3, E = 2 %: 2.8e7 kg
    assert abs(c.storage_capacity(1e6, 10.0, 0.2, 700.0, 0.02) - 2.8e7) < 1e-3
