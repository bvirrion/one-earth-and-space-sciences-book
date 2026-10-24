"""Tests for the melting-model figdata script (Year 3, ch. 12)."""
import os
import sys

import numpy as np
import pytest
from scipy.integrate import quad, solve_ivp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import melting_models as mm  # noqa: E402


@pytest.mark.parametrize("d", [0.001, 0.01, 0.1, 1.0, 3.0, 10.0])
@pytest.mark.parametrize("f", [0.001, 0.05, 0.2, 0.5])
def test_batch_melting_conserves_mass(d, f):
    cl = mm.batch(f, d)
    assert f * cl + (1 - f) * mm.batch_residue(f, d) == pytest.approx(1.0, rel=1e-12)


@pytest.mark.parametrize("d", [0.01, 0.1, 2.0])
def test_fractional_melting_integrates_the_residue_mass_balance(d):
    # d[(1-F) Cs]/dF = -Cs/D, integrated numerically from Cs = 1
    sol = solve_ivp(lambda f, y: [y[0] * (1 - 1 / d) / (1 - f)], (0, 0.3), [1.0],
                    rtol=1e-10, atol=1e-14, dense_output=True)
    for f in (0.05, 0.15, 0.3):
        assert sol.sol(f)[0] == pytest.approx(mm.fractional_residue(f, d), rel=1e-6)
        assert mm.fractional_instant(f, d) == pytest.approx(mm.fractional_residue(f, d) / d,
                                                            rel=1e-12)


@pytest.mark.parametrize("d", [0.01, 0.1, 2.0])
def test_aggregate_is_the_mean_of_the_instantaneous_melts_and_mass_balances(d):
    for f in (0.01, 0.1, 0.3):
        mean = quad(lambda x: mm.fractional_instant(x, d), 0, f)[0] / f
        assert mm.fractional_aggregate(f, d) == pytest.approx(mean, rel=1e-8)
        # pooled melt + residue hold the source
        total = f * mm.fractional_aggregate(f, d) + (1 - f) * mm.fractional_residue(f, d)
        assert total == pytest.approx(1.0, rel=1e-10)


def test_limits():
    assert mm.batch(0.0, 0.05) == pytest.approx(20.0)
    assert mm.batch(0.1, 1e-12) == pytest.approx(10.0, rel=1e-9)
    assert mm.fractional_aggregate(0.1, 1e-3) == pytest.approx(10.0, rel=1e-9)
    assert mm.batch(0.2, 1.0) == pytest.approx(1.0)
    assert mm.fractional_aggregate(0.2, 1.0) == pytest.approx(1.0)


def test_nonmodal_reduces_to_modal_and_balances():
    assert mm.nonmodal_batch(0.1, 0.05, 0.05) == pytest.approx(mm.batch(0.1, 0.05))
    d0, p = mm.ex73()
    # residue D times residue mass + melt mass, all times C_L = C_0
    for f in (0.02, 0.1, 0.2):
        cl = mm.nonmodal_batch(f, d0["La"], p["La"])
        cs = mm.nonmodal_residue_d(f, d0["La"], p["La"]) * cl
        assert f * cl + (1 - f) * cs == pytest.approx(1.0, rel=1e-12)
    assert d0["La"] == pytest.approx(0.007374, abs=1e-9)
    assert p["Sm"] == pytest.approx(0.16601, abs=1e-9)


def test_dynamic_melting_tends_to_fractional():
    assert mm.dynamic_instant(0.1, 0.01, 0.0) == pytest.approx(mm.fractional_instant(0.1, 0.01))
    assert mm.dynamic_effective_d(0.001, 0.01) == pytest.approx(0.01099)


def test_bulk_d_and_lava_inversions():
    assert sum(mm.MODE_SP) == pytest.approx(1.0)
    assert mm.bulk_d("La", mm.MODE_SP) == pytest.approx(0.00784)
    assert mm.bulk_d("Yb", mm.MODE_GT) == pytest.approx(0.96684)
    d = mm.bulk_d("La", mm.MODE_SP)
    f = mm.f_batch(9.6 / 0.648, d)
    assert mm.batch(f, d) * 0.648 == pytest.approx(9.6)
    fa = mm.f_aggregate(9.6 / 0.648, d)
    assert mm.fractional_aggregate(fa, d) * 0.648 == pytest.approx(9.6)
    assert fa > f


def test_ratio_line_is_exact_for_a_perfectly_incompatible_element():
    slope, icpt = mm.ratio_line(0.5, 1.0, 0.4)
    for f in (0.01, 0.05, 0.2):
        ch = 1.0 / f                       # D_H = 0
        cm = 0.4 * mm.batch(f, 0.5)
        assert ch / cm == pytest.approx(slope * ch + icpt, rel=1e-12)


def test_garnet_raises_la_yb_and_spinel_cannot_make_lava_b():
    dla, dyb = mm.bulk_d("La", mm.MODE_SP), mm.bulk_d("Yb", mm.MODE_SP)
    max_sp = (0.648 / dla) / (0.441 / dyb)
    assert max_sp < 40.0
    # the spinel melt with La/Yb of lava B is far richer in La than lava B
    target = 15.6 / 0.45
    f = np.exp(np.linspace(np.log(1e-5), np.log(0.3), 20001))
    lay = (0.648 * mm.batch(f, dla)) / (0.441 * mm.batch(f, dyb))
    i = np.argmin(abs(lay - target))
    assert 0.648 * mm.batch(f[i], dla) > 60.0
