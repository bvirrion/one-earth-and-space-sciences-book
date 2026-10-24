"""Tests for the isostasy-gravity figure data: the hypsometry of ETOPO1 at 1 degree
and the free-air and Bouguer anomalies of a two-dimensional mountain range."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import gravity_profiles as gp  # noqa: E402
import hypsometry as hy  # noqa: E402


def test_cell_weights_cover_the_sphere():
    assert abs(hy.total_area() / (4 * math.pi * hy.R ** 2) - 1.0) < 1e-9


def test_ocean_fraction_close_to_71_percent():
    # ledger wss:ocean-cover: about 71 % of the surface lies below sea level
    assert abs(hy.fraction_below(0.0) - 0.71) < 0.01


def test_hypsometric_curve_is_decreasing_and_crosses_zero_at_land_fraction():
    curve = hy.hypsometric_curve()
    elev = [e for _, e in curve]
    assert all(a >= b for a, b in zip(elev, elev[1:]))
    land_pc = 100.0 * (1.0 - hy.fraction_below(0.0))
    for pc, e in curve:
        if pc < land_pc - 0.5:
            assert e >= 0.0
        if pc > land_pc + 0.5:
            assert e < 0.0


def test_histogram_is_bimodal():
    hist = hy.histogram()
    assert abs(sum(p for _, p in hist) - 100.0) < 1e-9
    land, sea = hy.modes()
    assert 0.0 < land < 1000.0
    assert -5500.0 < sea < -3500.0
    # a trough between the two modes: the continental slope
    trough = min(p for e, p in hist if -2500.0 < e < -500.0)
    assert trough < 0.2 * max(p for _, p in hist)


def test_airy_root_and_slab_constant():
    assert abs(gp.airy_root() - 9000.0) < 1e-9
    # 2 pi G = 0.0419 mGal per metre per 1000 kg/m3 (computed from ledger const:G)
    assert abs(gp.bouguer_slab(1000.0, 1.0) / gp.MGAL - 0.0419) < 0.0001


def test_rectangle_formula_matches_line_masses():
    # body wholly below the observer
    a = gp.rect_gz(10e3, 0.0, 300.0, -20e3, 30e3, 5e3, 12e3)
    b = gp.line_mass_gz(10e3, 0.0, 300.0, -20e3, 30e3, 5e3, 12e3, nx=1000, nz=100)
    assert abs(a - b) / abs(a) < 1e-3
    # body wholly above the observer pulls upwards
    a = gp.rect_gz(0.0, 0.0, 300.0, -20e3, 30e3, -12e3, -5e3)
    b = gp.line_mass_gz(0.0, 0.0, 300.0, -20e3, 30e3, -12e3, -5e3, nx=1000, nz=100)
    assert a < 0.0 and abs(a - b) / abs(a) < 1e-3


def test_wide_block_tends_to_the_slab():
    # an observer on top of a very wide block feels 2 pi G rho h
    half_w = 5000e3
    fa, bg = gp.anomalies(0.0, False, half_w=half_w)
    assert abs(fa - gp.bouguer_slab(gp.RHO_C, gp.H)) / fa < 0.01
    assert abs(bg) < 0.01 * fa


def test_wide_compensated_block_has_no_free_air_anomaly():
    half_w = 5000e3
    fa, bg = gp.anomalies(0.0, True, half_w=half_w)
    slab = gp.bouguer_slab(gp.RHO_C, gp.H)
    assert abs(fa) < 0.02 * slab
    # Bouguer anomaly = attraction of the root, -2 pi G drho r
    root = gp.bouguer_slab(gp.RHO_M - gp.RHO_C, gp.airy_root())
    assert abs(bg + root) / root < 0.02


def test_profiles_are_symmetric_and_decay_away():
    for x in (30e3, 90e3, 150e3, 250e3):
        for comp in (False, True):
            l, r = gp.anomalies(-x, comp), gp.anomalies(x, comp)
            assert abs(l[0] - r[0]) < 1e-9 and abs(l[1] - r[1]) < 1e-9
    assert abs(gp.anomalies(300e3, True)[0]) < abs(gp.anomalies(120e3, True)[0])
