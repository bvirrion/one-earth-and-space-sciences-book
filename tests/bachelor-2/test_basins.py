"""Tests for the sedimentary-basins figure data (figdata/bachelor-2/basins.py)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import basins  # noqa: E402


def test_time_constant_of_the_plate():
    # a^2 / (pi^2 kappa) with a = 125 km, kappa = 8e-7 m2/s
    assert basins.tau_myr() == pytest.approx(62.70, abs=0.01)
    # with kappa = 1e-6 m2/s the plate cools faster
    assert basins.tau_myr(kappa=1e-6) == pytest.approx(50.16, abs=0.01)


def test_syn_rift_subsidence_is_an_isostatic_balance():
    """Integrate the densities of the two columns down to the old base of the lithosphere and
    check that the formula balances them."""
    a, tc = basins.A, basins.TC
    al, t1 = basins.ALPHA, basins.T1
    rm, rc, rw = basins.RHO_M, basins.RHO_C, basins.RHO_W

    def column_mass(beta, si, n=20000):
        # water si, then crust tc/beta, mantle lithosphere to a/beta, asthenosphere at T1 to a
        lith = a / beta
        total = rw * si
        h = lith / n
        for i in range(n):
            z = (i + 0.5) * h
            temp = t1 * z / lith
            rho = rc if z < tc / beta else rm
            total += rho * (1 - al * temp) * h
        total += rm * (1 - al * t1) * (a - lith - si)
        return total

    before = column_mass(1.0, 0.0)
    for beta in (1.2, 1.5, 2.0, 4.0):
        si = basins.syn_rift(beta)
        assert column_mass(beta, si) == pytest.approx(before, rel=1e-7)
    assert basins.syn_rift(1.0) == 0.0
    assert basins.syn_rift_max() == pytest.approx(4333.8, abs=0.1)


def test_first_term_against_full_series_and_finite_differences():
    for beta in (1.5, 2.0, 4.0):
        series = basins.thermal_series(beta, 50.0, nterms=101, nquad=2000)
        assert basins.thermal_fd(beta, 50.0) == pytest.approx(series, rel=2e-3)
    # the dropped terms decay at least nine times faster: after 10 Myr the first term is
    # within 100 m of the full series for beta from 1.2 to 4
    for beta in (1.2, 1.5, 2.0, 4.0):
        for t in (10.0, 50.0, 200.0):
            series = basins.thermal_series(beta, t, nterms=101, nquad=2000)
            assert abs(series - basins.thermal(beta, t)) < 100.0
    # exact final subsidence of the plate: alpha rho_m T1 a (1 - 1/beta) / (2 (rho_m - rho_w))
    exact = (basins.ALPHA * basins.RHO_M * basins.T1 * basins.A * 0.5
             / (2 * (basins.RHO_M - basins.RHO_W)))
    assert basins.thermal_series(2.0, 1e5, nterms=201, nquad=4000) == pytest.approx(exact, rel=2e-3)


def test_compaction_conserves_solid_and_backstrip_formula():
    phi0, c = basins.LITH["sand"][1:]
    ts = basins.solid_thickness(4420.0, 6030.0, phi0, c)
    z2 = basins.decompacted_base(0.0, ts, phi0, c)
    assert basins.solid_thickness(0.0, z2, phi0, c) == pytest.approx(ts, abs=1e-4)
    assert z2 > 6030.0 - 4420.0
    # a water-filled 'basin' is its own tectonic subsidence
    assert basins.airy_backstrip(1000.0, basins.RHO_W, 0.0) == pytest.approx(1000.0)
    # Book 3's loading factor: sediment of 2300 fills 2.26 times the water-loaded depth
    s = 1000.0 * (basins.RHO_M - basins.RHO_W) / (basins.RHO_M - 2300.0)
    assert basins.airy_backstrip(s, 2300.0, 0.0) == pytest.approx(1000.0)
    # a sea standing 50 m higher than today: the correction is 50 rho_m / (rho_m - rho_w)
    assert (basins.airy_backstrip(s, 2300.0, 0.0) - basins.airy_backstrip(s, 2300.0, 0.0, dsl=50.0)
            == pytest.approx(50 * 3330 / 2300))


def test_the_invented_well_gives_back_its_design():
    st = basins.stages()
    ages = [r[0] for r in st]
    assert ages == [150.0, 100.0, 60.0, 0.0]
    # today no decompaction: S is the present depth of the basement
    assert st[-1][1] == pytest.approx(6030.0)
    # the tectonic subsidence grows with time and the fitted beta is close to the design 1.5
    ys = [r[5] for r in st]
    assert all(b > a for a, b in zip(ys, ys[1:]))
    assert basins.fitted_beta() == pytest.approx(1.499, abs=0.001)
    b = basins.fitted_beta()
    for age, _s, _r, _w, _t, y in st:
        assert basins.tectonic(b, 150.0 - age) == pytest.approx(y, abs=5.0)
    assert basins.beta_from_initial(basins.syn_rift(1.8)) == pytest.approx(1.8)
    assert math.isclose(st[0][5], basins.numbers()["Y_150"], abs_tol=0.05)
