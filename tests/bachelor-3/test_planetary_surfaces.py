"""Tests for the planetary interiors and surfaces scripts (Year 3, ch. 26)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import crater_sfd as cs  # noqa: E402
import two_layer_planet as tl  # noqa: E402


def test_two_layer_round_trip():
    for name, (rho_bar, c, _, _) in tl.BODIES.items():
        for rho_m in (2800.0, 3000.0, 3200.0):
            s = tl.solve(rho_bar, c, rho_m)
            if s is None:
                continue
            x, rho_c = s
            assert tl.mean_density(x, rho_c, rho_m) == pytest.approx(rho_bar)
            assert tl.moi(x, rho_c, rho_m) == pytest.approx(c)
            assert tl.mantle_for_core(rho_bar, c, x) == pytest.approx(rho_m)
    # a uniform planet has C = 2/5 whatever its core
    assert tl.moi(0.5, 4000.0, 4000.0) == pytest.approx(0.4)
    # no core can fit when the mantle is as dense as (5/2) C rho_bar
    assert tl.solve(3934.0, 0.366, 2.5 * 0.366 * 3934.0 + 1.0) is None


def test_two_layer_curves_are_monotone():
    for name in tl.BODIES:
        rows = tl.curve(name)
        xs = [r[2] for r in rows]
        rcs = [r[1] for r in rows]
        # a denser mantle leaves a smaller, denser core
        assert all(b < a for a, b in zip(xs, xs[1:]))
        assert all(b > a for a, b in zip(rcs, rcs[1:]))


def test_production_function_and_isochrons():
    assert cs.shape(1.0) == pytest.approx(1.0)
    ds = [0.1 * 1.2 ** k for k in range(40)]
    fs = [cs.shape(d) for d in ds]
    assert all(b < a for a, b in zip(fs, fs[1:]))
    # the coefficient a0 is log10 N(1 km) for 1 Ga in Ivanov's own chronology
    assert 10 ** cs.PF[0] == pytest.approx(2.68e-14 * (math.exp(6.93) - 1) + 4.13e-4, rel=2e-3)
    # isochrons are parallel: their ratio does not depend on D
    for d in (0.5, 2.0, 10.0):
        assert cs.isochron(d, 3.0) / cs.isochron(d, 1.0) == pytest.approx(cs.n1(3.0) / cs.n1(1.0))


def test_chronology_inversion_and_errors():
    for t in (0.2, 1.0, 2.5, 3.6, 4.1):
        assert cs.age(cs.n1(t)) == pytest.approx(t, abs=1e-9)
    # linear in the last 3 Ga: N1 doubles when T doubles
    assert cs.n1(2.0) / cs.n1(1.0) == pytest.approx(2.0, rel=1e-3)
    # the steep early flux shrinks the age error of an old surface
    assert cs.age_error(3.8, 100) < 0.2 * cs.age_error(1.0, 100)
    assert cs.age_error(1.0, 100) == pytest.approx(0.1 * cs.n1(1.0) / cs.dn1(1.0))


def test_invented_counts_recover_their_ages():
    na, nb = cs.counts()
    ta = cs.age(sum(na) / cs.AREA_A)
    assert abs(ta - cs.AGE_A) < 3 * cs.age_error(ta, sum(na))
    tb = cs.age(sum(nb[2:]) / cs.AREA_B / cs.shape(2.0))
    assert abs(tb - cs.AGE_B) < 3 * cs.age_error(tb, sum(nb[2:]))
    tr = cs.age((nb[0] + nb[1]) / cs.AREA_B / (cs.shape(1.0) - cs.shape(2.0)))
    assert abs(tr - cs.AGE_B_RESURF) < 3 * cs.age_error(tr, nb[0] + nb[1])
    assert cs.equilibrium(1.0) > cs.isochron(1.0, 4.0)
