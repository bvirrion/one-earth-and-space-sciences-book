"""figdata/grade-11/dyke_cooling.py: conductive cooling of a sheet of basaltic magma."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import dyke_cooling as dc  # noqa: E402


def test_without_latent_heat_matches_the_error_function_solution():
    # centre of a sheet of half-thickness h: T = T_host + dT erf(h / (2 sqrt(kappa t)))
    from scipy.special import erfinv
    h = 10.0
    x = erfinv((dc.T_SOLIDUS - dc.T_HOST) / (dc.T_MAGMA - dc.T_HOST))
    t_exact = h * h / (4 * dc.KAPPA * x * x)
    t_model = dc.cool(20.0, latent=False)[0]
    assert abs(t_model / t_exact - 1) < 0.01


def test_doubling_the_thickness_quadruples_the_time():
    t10 = dc.cool(10.0)[0]
    t20 = dc.cool(20.0)[0]
    assert abs(t20 / t10 - 4.0) < 0.04


def test_heat_of_crystallization_slows_solidification_by_up_to_three():
    n = dc.numbers()
    assert 1.5 < n["latent_factor"] < 3.2          # Delaney 1986: by a factor of as much as three
    assert 2.0 < n["t20_yr"] < 3.5


def test_the_margin_solidifies_first():
    _, front, _ = dc.cool(20.0)
    times = [t for _, t in front]
    assert all(math.isfinite(t) for t in times)
    assert all(a > b for a, b in zip(times, times[1:]))   # from the centre outward, earlier and earlier
    assert times[-1] < 0.01 * times[0]


def test_grid_converged():
    assert abs(dc.cool(20.0, n_half=20)[0] / dc.cool(20.0)[0] - 1) < 0.005


def test_contact_temperature_matches_delaney():
    # Delaney (1986), analytical early-time solution: about 690 degC at the contact with the
    # heat of crystallization, about 600 degC without
    import numpy as np
    for latent, expected in ((True, 690.0), (False, 600.0)):
        _, _, snaps = dc.cool(20.0, latent=latent, snapshots=[30 * 86400])
        x, T = list(snaps.values())[0]
        h = 10.0
        t_contact = np.interp(h, x, T)
        assert abs(t_contact - expected) < 15
