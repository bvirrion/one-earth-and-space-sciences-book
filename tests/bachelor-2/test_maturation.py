"""Tests of figdata/bachelor-2/maturation.py (Year 2, energy-geology)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import maturation as m  # noqa: E402


def test_single_energy_approximation():
    # the proposition: x = exp(-(A T^2/(beta E/R)) exp(-E/RT)), valid when E/RT >> 1;
    # its exponent differs from the exact integral by a relative 2RT/E to first order
    for t in (120.0, 140.0, 160.0):
        xa = float(m.x_single_approx(t, 1.0))
        xn = m.x_single_numeric(t, 1.0)
        rel = math.log(xa) / math.log(xn) - 1.0
        two_rt_e = 2 * (t + 273.15) / m.GR_ER
        assert 0 < rel < 1.5 * two_rt_e


def test_heating_rate_shift():
    # a tenfold faster heating shifts the half-conversion temperature by about (T^2/(E/R)) ln 10
    t1, t10 = m.t_half(1.0), m.t_half(10.0)
    pred = (t1 + 273.15) ** 2 / m.GR_ER * math.log(10.0)
    assert abs((t10 - t1) - pred) / pred < 0.1
    # at T_half the approximate unconverted fraction is one half
    assert abs(float(m.x_single_approx(t1, 1.0)) - 0.5) < 1e-6


def test_daem_limits():
    # a very narrow energy distribution reproduces the single-energy reaction
    for t in (130.0, 150.0):
        tr = float(m.tr_constant_rate([t], 1.0, s_r=1e-6)[0])
        assert abs((1 - tr) - m.x_single_numeric(t, 1.0, dt=0.05)) < 2e-3
    # TR rises with temperature, lies in [0, 1], and slower heating converts more at the same T
    ts = [100.0 + 5 * k for k in range(21)]
    tr1 = m.tr_constant_rate(ts, 1.0)
    tr10 = m.tr_constant_rate(ts, 10.0)
    assert all(0 <= a <= 1 for a in tr1) and all(b >= a - 1e-12 for a, b in zip(tr1, tr1[1:]))
    assert all(a >= b - 1e-12 for a, b in zip(tr1, tr10))


def test_easy_ro():
    # Ro starts at exp(-1.6) and tends to exp(-1.6 + 3.7 * 0.85) after complete conversion
    ro = m.easy_ro([0.0, 1.0, 2.0], [20.0, 20.0, 20.0])
    assert abs(ro[0] - math.exp(-1.6)) < 1e-12 and ro[0] < ro[1] < ro[2] < 0.3
    ro = m.easy_ro([0.0, 100.0], [400.0, 400.0])
    assert abs(ro[-1] - math.exp(-1.6 + 3.7 * 0.85)) < 1e-3
    assert sum(m.RO_W) == 85 and len(m.RO_E) == len(m.RO_W)
    # monotone along a heating history
    _, _, _, r = m.horizon_ro(100.0)
    assert all(b >= a for a, b in zip(r, r[1:]))


def test_burial_geometry():
    assert m.depth(100.0, 0.0) == 100 * 30 + 35 * 70
    assert m.depth(70.0, 70.0) == 0.0 and m.depth(100.0, 70.0) == 3000.0
    # the 1.3 % front lies below the 0.6 % front whenever both exist
    for row in m.fronts():
        if row[1] != "nan" and row[2] != "nan":
            assert row[2] > row[1]


def test_van_krevelen_points():
    # the average formula C100H150N3O8S1 of Green River kerogen: H/C 1.50, O/C 0.08
    hc, oc = m.atomic_ratios(*m.GR39[0][1:])
    assert abs(hc - 1.50) < 0.02 and abs(oc - 0.08) < 0.005
    # heating removes hydrogen: H/C of the char falls between 400 and 525 degC
    hcs = [m.atomic_ratios(c, h, o)[0] for t, c, h, o in m.GR39]
    assert hcs[1] < hcs[0] and hcs[-1] < 0.6 < hcs[0]
