"""Tests for the gravity-geodesy figdata scripts (Year 3, ch. 3)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import flexure as fx  # noqa: E402
import hydrostatic_figure as hf  # noqa: E402
import ice_mass as im  # noqa: E402


def test_rigidity_and_thickness_invert():
    for te in (5e3, 25e3, 60e3):
        assert fx.elastic_thickness(fx.rigidity(te)) == pytest.approx(te, rel=1e-12)


def test_line_load_solves_the_plate_equation():
    """Finite differences on D w'''' + drho g w = q with a narrow load of total V0."""
    d = fx.rigidity(25e3)
    k = (fx.RHO_M - fx.RHO_W) * fx.G
    v0 = fx.ridge_load()
    h = 1000.0
    x = np.arange(-1500e3, 1500e3 + h, h)
    n = len(x)
    a = np.zeros((n, n))
    for i in range(2, n - 2):
        a[i, i - 2:i + 3] = d / h ** 4 * np.array([1, -4, 6, -4, 1])
        a[i, i] += k
    for i in (0, 1, n - 2, n - 1):
        a[i, i] = 1.0  # far boundary: w = 0
    q = np.zeros(n)
    q[n // 2] = v0 / h
    w = np.linalg.solve(a, q)
    for xk in (0.0, 50e3, 150e3, 222e3):
        i = int(round((xk - x[0]) / h))
        assert w[i] == pytest.approx(fx.line_load(xk, v0, d), rel=2e-3, abs=0.5)


def test_forebulge_position_and_height():
    d = fx.rigidity(25e3)
    a = fx.flexural_parameter(d)
    v0 = fx.ridge_load()
    xs = np.linspace(a, 5 * a, 20001)
    w = np.array([fx.line_load(x, v0, d) for x in xs])
    i = int(np.argmin(w))
    assert xs[i] == pytest.approx(math.pi * a, rel=1e-3)
    w0 = fx.line_load(0.0, v0, d)
    assert -w[i] / w0 == pytest.approx(math.exp(-math.pi), rel=1e-6)
    # first zero of the continuous-plate solution at 3 pi alpha / 4
    assert fx.line_load(0.75 * math.pi * a, v0, d) == pytest.approx(0.0, abs=1e-6 * w0)


def test_broken_plate_zero_and_bulge():
    a = 70e3
    assert fx.broken_plate(0.5 * math.pi * a, 1000.0, a) == pytest.approx(0.0, abs=1e-9)
    xs = np.linspace(0.6 * a, 3 * a, 20001)
    w = np.array([fx.broken_plate(x, 1000.0, a) for x in xs])
    assert xs[int(np.argmin(w))] == pytest.approx(0.75 * math.pi * a, rel=1e-3)


def test_radau_inverts_and_uniform_limit():
    for moi in (0.30, 0.3308, 0.38):
        assert hf.radau_moi(hf.radau_flattening(moi)) == pytest.approx(moi, rel=1e-12)
    assert hf.radau_flattening(0.4) == pytest.approx(1.25 * hf.M_GRS80, rel=1e-12)


def test_earth_flattening_close_to_but_above_hydrostatic():
    fh = hf.radau_flattening(hf.MOI)
    assert 299.0 < 1 / fh < 301.0
    assert hf.F_GRS80 > fh
    assert hf.clairaut_j2(hf.F_GRS80) == pytest.approx(hf.J2_GRS80, rel=5e-3)


def test_imbie_series_and_trends():
    for s in im.SHEETS:
        d = im.read(s)
        assert d[0, 0] == pytest.approx(1992.0) and d[-1, 0] > 2020.8
        assert np.all(d[:, 2] > 0)
        r, b = im.trend(d, *im.WINDOWS[0])
        assert r < 0
    t = np.arange(2000, 2010, 1 / 12)
    synth = np.column_stack([t, -100 * (t - 2000) + 5, np.ones_like(t)])
    assert im.trend(synth, 2000, 2010)[0] == pytest.approx(-100.0, rel=1e-9)
