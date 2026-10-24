"""Tests for the hydrogeology scripts (Year 3, ch. 23)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import advection_dispersion as ad  # noqa: E402
import flow_net as fn  # noqa: E402
import theis  # noqa: E402


def test_well_function_series_and_table():
    # Heath's table: W(1) = 0.219, W(0.1) = 1.82, W(0.01) = 4.04
    assert theis.well_function(1.0) == pytest.approx(0.219, abs=1e-3)
    assert theis.well_function(0.1) == pytest.approx(1.82, abs=5e-3)
    assert theis.well_function(0.01) == pytest.approx(4.04, abs=5e-3)
    u = 0.02
    series = -theis.EULER - math.log(u) + u - u * u / 4 + u ** 3 / 18 - u ** 4 / 96
    assert theis.well_function(u) == pytest.approx(series, rel=1e-9)


def test_theis_solves_the_radial_flow_equation():
    T, S, r, t = theis.T_TRUE, theis.S_TRUE, 80.0, 0.3
    dr, dt = 1e-2, 1e-6
    s = lambda rr, tt: theis.drawdown(rr, tt)  # noqa: E731
    lap = (s(r + dr, t) - 2 * s(r, t) + s(r - dr, t)) / dr ** 2 + (s(r + dr, t) - s(r - dr, t)) / (2 * dr * r)
    dsdt = (s(r, t + dt) - s(r, t - dt)) / (2 * dt)
    assert S * dsdt == pytest.approx(T * lap, rel=1e-4)
    # the flow towards the well at small r carries Q: -2 pi r T ds/dr -> Q
    r0 = 0.05
    flux = 2 * math.pi * r0 * T * (s(r0 - 1e-5, t) - s(r0 + 1e-5, t)) / 2e-5
    assert flux == pytest.approx(theis.Q, rel=1e-3)


def test_cooper_jacob_fit_and_site():
    T, S, slope, t0, n = theis.fit_jacob(theis.test_record())
    assert T == pytest.approx(theis.T_TRUE, rel=0.03)
    assert S == pytest.approx(theis.S_TRUE, rel=0.2)
    assert n >= 10
    # Jacob is within a few millimetres of Theis once u <= 0.05
    assert theis.jacob(60.0, 2.0) == pytest.approx(theis.drawdown(60.0, 2.0), abs=0.01)
    g, top, base = theis.site()
    assert top - base == pytest.approx(180.0)
    assert 60.0 < g - top < 100.0   # the shale confines the limestone at Varden-3


def test_flow_net_is_harmonic_conservative_and_symmetric():
    h = fn.solve_head()
    p = np.pad(h, 1, mode="reflect")
    avg = 0.25 * (p[1:-1, :-2] + p[1:-1, 2:] + p[:-2, 1:-1] + p[2:, 1:-1])
    free = np.ones_like(h, bool)
    free[-1, fn.UP | fn.DOWN] = False
    assert np.max(np.abs(avg - h)[free]) < 1e-6
    # antisymmetry about the dam axis: h(x) + h(-x) = h1
    assert np.max(np.abs(h + h[:, ::-1] - fn.H1)) < 1e-6
    qin, qout = fn.seepage(h)
    assert qin == pytest.approx(qout, rel=1e-6)
    # five flow channels and ten head drops: q close to K h1 / 2
    assert qout / fn.H1 == pytest.approx(0.5, abs=0.05)
    psi = fn.solve_psi()
    assert psi.min() >= -1e-9 and psi.max() <= 1 + 1e-9


def test_advection_dispersion_solution():
    a, v = 3.0, ad.V
    D = a * v
    x, t = 90.0, 160.0
    dx, dt = 1e-2, 1e-3
    c = lambda xx, tt: ad.conc(xx, tt, a)  # noqa: E731
    dcdt = (c(x, t + dt) - c(x, t - dt)) / (2 * dt)
    dcdx = (c(x + dx, t) - c(x - dx, t)) / (2 * dx)
    d2 = (c(x + dx, t) - 2 * c(x, t) + c(x - dx, t)) / dx ** 2
    assert dcdt == pytest.approx(D * d2 - v * dcdx, abs=1e-6)
    assert ad.conc(0.0, 50.0, a) == pytest.approx(1.0, abs=1e-12)
    # retardation slows the front by R exactly: C(x, t; R) = C(x, t/R; 1)
    assert ad.conc(100.0, 600.0, a, r=3.0) == pytest.approx(ad.conc(100.0, 200.0, a), rel=1e-12)
    # the median arrival approaches x/v as the dispersivity shrinks
    assert ad.time_at(0.5, 0.01) == pytest.approx(ad.X_OBS / v, rel=1e-3)
