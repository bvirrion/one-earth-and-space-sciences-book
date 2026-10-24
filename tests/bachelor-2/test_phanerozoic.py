"""Tests for the Phanerozoic figure data (figdata/bachelor-2/phanerozoic.py)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import phanerozoic as ph  # noqa: E402


def test_depth_laws_join_and_mean_depth_is_exact():
    # the half-space law at 0 and 100 Myr, the plate law far out
    assert ph.depth_hs(0) == pytest.approx(2500.0)
    assert ph.depth_hs(100) == pytest.approx(6000.0)
    assert ph.depth_plate(1e4) == pytest.approx(6400.0)
    # the two laws cross near 26 Myr, so the plate curve has no step
    assert ph.T_X == pytest.approx(26.3, abs=0.1)
    assert ph.depth_plate(ph.T_X + 1e-6) == pytest.approx(ph.depth_plate(ph.T_X - 1e-6), abs=0.01)
    # numerical mean of the half-space law equals the closed form d0 + 2/3 c sqrt(tau)
    n = 20000
    num = sum(ph.depth_hs((i + 0.5) * 100.0 / n) for i in range(n)) / n
    assert num == pytest.approx(ph.mean_depth(100.0), rel=1e-5)
    # the plate law is shallower than the half-space law for old floor
    assert ph.mean_depth(ph.TAU, ph.depth_plate) < ph.mean_depth(ph.TAU)


def test_sea_rise_from_doubling_the_spreading_rate():
    af = ph.floor_area()
    assert af / 1e6 == pytest.approx(293.1, abs=0.1)
    # closed form for the half-space law and a doubled rate
    dd = 2.0 / 3.0 * ph.C_HS * math.sqrt(ph.TAU) * (1 - 1 / math.sqrt(2))
    expect = (ph.RHO_M - ph.RHO_W) / ph.RHO_M * af / ph.A_OCEAN * dd
    assert ph.sea_rise(2.0, a_floor=af) == pytest.approx(expect, rel=1e-9)
    assert ph.sea_rise(2.0, a_floor=af) == pytest.approx(432.5, abs=0.1)
    assert ph.sea_rise(1.0, a_floor=af) == pytest.approx(0.0, abs=1e-9)
    # a faster rate always raises the sea, and the plate law gives less
    assert ph.sea_rise(2.0, ph.depth_plate, a_floor=af) < ph.sea_rise(2.0, a_floor=af)
    # the rate increase that gives 100 m
    f = ph.factor_for(100.0, a_floor=af)
    assert ph.sea_rise(f, a_floor=af) == pytest.approx(100.0, abs=0.01)
    assert f == pytest.approx(1.151, abs=0.001)


def test_age_histogram_covers_the_grid_and_young_floor_dominates():
    hist = ph.age_hist()
    assert sum(hist.values()) == pytest.approx(ph.floor_area(), rel=1e-9)
    # more young floor than old: the first bin is the largest of the first 13
    assert max(range(13), key=lambda b: hist.get(b, 0.0)) in (0, 1, 2)


def test_hypsometry_and_flooding():
    cs = ph.cells()
    # land is about 29 per cent of the surface on the one-degree grid
    assert ph.land_fraction(cs) == pytest.approx(0.29, abs=0.01)
    h = ph.hypsometry()
    pcts = [p for p, _ in h]
    assert all(a >= b for a, b in zip(pcts, pcts[1:]))       # decreasing with elevation
    assert pcts[0] == pytest.approx(100.0, abs=0.01)
    # flooding grows with the rise and is nothing for no rise
    assert ph.flooded_pct(0, cs) == 0.0
    assert ph.flooded_pct(100, cs) < ph.flooded_pct(200, cs) < ph.flooded_pct(1000, cs)


def test_maps_and_cities_are_on_the_projection():
    lim = 2 * math.sqrt(2)
    for t in ph.TIMES:
        rings = ph.map_rings(t)
        assert len(rings) > 100
        for ring in rings:
            for x, y in ring:
                assert (x / lim) ** 2 + (y / math.sqrt(2)) ** 2 <= 1 + 1e-9
    # Paris near the equator 300 Myr ago, far south 500 Myr ago; Sydney not in the model then
    c300 = {n: lat for n, _, lat in ph.cities(300)}
    assert abs(c300["Paris"]) < 10
    c500 = {n: lat for n, _, lat in ph.cities(500)}
    assert c500["Paris"] < -50 and c500["Sydney"] is None


def test_sea_level_records_and_running_mean():
    haq = ph.sealevel("bachelor-2-miller2005-haq87", "haq")
    kom = ph.sealevel("bachelor-2-miller2005-kominz08", "backstrip-low")
    assert haq[0][0] < 1 and haq[-1][0] > 240
    assert 9 < kom[0][0] < 10 and kom[-1][0] < 101
    lt = ph.running_mean([(float(t), 5.0) for t in range(0, 50)])
    assert all(v == pytest.approx(5.0) for _, v in lt)
    assert lt[0][0] == 5 and lt[-1][0] == 44
