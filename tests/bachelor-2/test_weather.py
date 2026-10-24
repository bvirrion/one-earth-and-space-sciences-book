"""Tests for the Lorenz-system figure data (figdata/bachelor-2/weather.py)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import weather as w  # noqa: E402


def test_fixed_points_and_symmetry():
    for p in w.fixed_points():
        assert np.allclose(w.deriv(np.array(p)), 0.0, atol=1e-12)
    c = w.fixed_points()[1]
    assert c[0] == pytest.approx(math.sqrt(72.0)) and c[2] == pytest.approx(27.0)
    # the system is unchanged by (x, y, z) -> (-x, -y, z)
    s = np.array([3.0, -2.0, 15.0])
    m = np.array([-1.0, -1.0, 1.0])
    assert np.allclose(w.deriv(s * m), w.deriv(s) * m)


def test_divergence_constant():
    h = 1e-6
    for s in (np.array([1.0, 2.0, 3.0]), np.array([-8.0, 5.0, 30.0])):
        div = sum((w.deriv(s + h * e)[i] - w.deriv(s - h * e)[i]) / (2 * h)
                  for i, e in enumerate(np.eye(3)))
        assert div == pytest.approx(w.divergence(), abs=1e-6)
    assert w.divergence() == pytest.approx(-(10 + 1 + 8 / 3))


def test_rk4_order():
    s0 = np.array([1.0, 1.0, 20.0])
    ref = w.run(s0, 1.0, dt=0.000625)[-1]
    e1 = np.linalg.norm(w.run(s0, 1.0, dt=0.01)[-1] - ref)
    e2 = np.linalg.norm(w.run(s0, 1.0, dt=0.005)[-1] - ref)
    assert 12 < e1 / e2 < 40          # fourth order: 16 asymptotically (about 28 here)


def test_lyapunov_and_growth():
    lam = w.lyapunov(tmax=600.0)
    assert lam == pytest.approx(0.906, abs=0.03)
    g = w.growth(npairs=60, tmax=20.0)
    slope, _ = w.fit(g)
    assert slope == pytest.approx(lam, rel=0.1)
    # errors stop growing at the size of the attractor
    g2 = w.growth(npairs=40, tmax=30.0)
    assert g2[-1][1] / math.log(10) == pytest.approx(1.15, abs=0.25)
