"""figdata/grade-11/geotherm_solidus.py: the model geotherm and the dry solidus."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import geotherm_solidus as gs  # noqa: E402


def test_surface_gradient_is_heat_flow_over_conductivity():
    assert abs(gs.surface_gradient() - gs.Q0 / gs.K * 1e3) < 0.01
    assert 25.0 < gs.surface_gradient() < 30.0          # the measured 25-30 degC/km


def test_heat_flow_splits_into_crust_and_below():
    assert abs(gs.QM + gs.a0() * gs.B_KM * 1e3 - gs.Q0) < 1e-12


def test_solidus_at_zero_pressure_is_hirschmanns_c():
    assert gs.t_solidus(0.0) == 1120.661
    assert abs(gs.t_solidus(1.0) - (1120.661 + 132.899 - 5.104)) < 1e-9


def test_geotherm_is_continuous_at_the_base_of_the_lithosphere():
    z = gs.lab_depth()
    assert abs(gs.t_cond(z) - gs.t_adiabat(z)) < 1e-6
    assert 70.0 < z < 130.0


def test_geotherm_stays_below_the_dry_solidus_and_comes_closest_near_100_km():
    z, gap = gs.closest_approach()
    assert gap > 0
    assert 80 <= z <= 130


def test_pressure_of_a_uniform_column():
    rows = [(0.0, 1, 1, 3.0, "a"), (1000.0, 1, 1, 3.0, "a")]
    # 3000 kg/m3 x 9.82 m/s2 x 100 km = 2.946 GPa
    assert abs(gs.pressure_gpa(100.0, rows) - 2.946) < 1e-9
