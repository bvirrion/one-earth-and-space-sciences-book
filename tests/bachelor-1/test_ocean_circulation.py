"""Tests for the ocean-circulation figures: Ekman's spiral and transport, and Stommel's
gyre with and without a northward increase of the Coriolis parameter."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import ekman_hodograph as ek  # noqa: E402
import stommel_gyre as sg  # noqa: E402


# ------------------------------------------------------------ Ekman
def test_surface_current_45_degrees_right_of_the_wind():
    u, v = ek.velocity(0.0)
    assert abs(ek.angle_right_of_wind(u, v) - 45.0) < 1e-9
    # at the Ekman depth the current is reversed and e^-pi times weaker
    t, f, d, a, az, v0 = ek.spiral_constants(ek.U10, ek.LAT)
    ud, vd = ek.velocity(-d)
    assert abs(math.hypot(ud, vd) / v0 - math.exp(-math.pi)) < 1e-12
    assert abs(ek.angle_right_of_wind(ud, vd) - (45.0 - 180.0)) < 1e-6


def test_spiral_solves_ekman_equations():
    """f v + A_z u'' = 0 and -f u + A_z v'' = 0, by finite differences."""
    t, f, d, a, az, v0 = ek.spiral_constants(ek.U10, ek.LAT)
    h = 0.01
    for z in (-5.0, -30.0, -80.0):
        (um, vm), (u0, w0), (up, vp) = ek.velocity(z - h), ek.velocity(z), ek.velocity(z + h)
        upp, vpp = (um - 2 * u0 + up) / h ** 2, (vm - 2 * w0 + vp) / h ** 2
        assert abs(f * w0 + az * upp) < 1e-6 * f * v0
        assert abs(-f * u0 + az * vpp) < 1e-6 * f * v0


def test_transport_is_tau_over_f_at_90_degrees():
    mx, my = ek.transport()
    t, f = ek.spiral_constants(ek.U10, ek.LAT)[:2]
    assert abs(mx - t / f) < 1e-4 * t / f
    assert abs(my) < 1e-4 * t / f
    assert abs(ek.angle_right_of_wind(mx, my) - 90.0) < 0.01


def test_spiral_matches_ekman_empirical_surface_current():
    v = dict(ek.values())
    assert abs(v["V0"] / v["V0_empirical"] - 1) < 0.01
    assert abs(v["D_E"] - 100.35) < 0.01


def test_bulk_formula():
    assert abs(ek.drag_coefficient(10.0) - 1.31e-3) < 1e-12
    assert abs(ek.drag_coefficient(6.0) - (0.29 + 3.1 / 6 + 7.7 / 36) * 1e-3) < 1e-12
    assert abs(ek.stress(8.0) - 1.3 * 1.168e-3 * 64) < 1e-12


# ------------------------------------------------------------ Stommel
def test_uniform_rotation_gives_a_symmetric_gyre():
    psi = sg.solve(0.0)
    assert (psi[1:-1, 1:-1] > 0).all()                       # clockwise everywhere
    assert abs(psi - psi[:, ::-1]).max() < 1e-9 * psi.max()


def test_beta_gives_western_intensification():
    v = dict(sg.values())
    assert v["xmax_beta"] < 0.2 * sg.L
    assert abs(v["xmax_uniform"] - sg.L / 2) < 0.02
    assert v["vnorth_beta"] > 8 * v["vsouth_beta"]           # fast narrow northward current
    assert v["xvnorth_beta"] < 0.05 * sg.L
    # the interior follows the (frictional) Sverdrup balance, close to the pure one
    assert abs(v["psi_mid_beta"] / v["interior_mid_beta"] - 1) < 0.01
    assert abs(v["psi_mid_beta"] / v["sverdrup_mid_beta"] - 1) < 0.15
