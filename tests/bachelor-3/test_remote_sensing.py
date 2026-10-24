"""Tests for the remote-sensing and GIS scripts (Year 3, ch. 25)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import insar_mogi as im  # noqa: E402
import spectral_signatures as ss  # noqa: E402
import thermal_ir as ti  # noqa: E402
import varden_gis as vg  # noqa: E402


def test_spectral_signatures_and_ndvi():
    m = ss.means()
    for name in ss.MATERIALS:
        for b in ss.OLI:
            assert 0.0 <= m[name][b] <= 1.0
    assert ss.ndvi(m["grass"]["B5"], m["grass"]["B4"]) > 0.7
    assert abs(ss.ndvi(m["water"]["B5"], m["water"]["B4"])) < 0.05
    assert ss.ndvi(m["soil"]["B5"], m["soil"]["B4"]) < 0.3
    # kaolinite is darker in band 7 than in band 6 (its 2.2 um absorption)
    assert m["kaolinite"]["B7"] < 0.8 * m["kaolinite"]["B6"]
    # thermal emissivities of the three long spectra are high, water the highest
    e = {n: 1 - m[n]["T10"] for n in ("grass", "water", "soil")}
    assert all(0.9 < v < 1.0 for v in e.values())
    assert e["water"] == max(e.values())


def test_planck_inversion_and_grey_body():
    lam = ti.LAM10
    for t in (250.0, 300.0, 370.0, 1443.15):
        assert ti.t_bright(lam, ti.planck(lam, t)) == pytest.approx(t, rel=1e-12)
    assert ti.t_grey(lam, 300.0, 0.95) < ti.t_grey(lam, 300.0, 0.99) < 300.0
    # Wien: the maximum of B_lambda
    t = 300.0
    peak = ti.wien_peak_um(t) * 1e-6
    for d in (0.99, 1.01):
        assert ti.planck(peak * d, t) < ti.planck(peak, t)
    assert ti.wien_peak_um(t) * t == pytest.approx(2897.77, rel=1e-4)


def test_mixed_pixel_is_hotter_than_its_mean():
    for f in (0.05, 0.1, 0.5, 0.9):
        mean = f * 370 + (1 - f) * 290
        assert ti.t_mixed(ti.LAM10, f, 370.0, 290.0) > mean
    assert ti.t_mixed(ti.LAM10, 0.0, 370.0, 290.0) == pytest.approx(290.0)


def test_mogi_line_of_sight_and_fringes():
    ur, uz = im.mogi(3000.0)
    assert ur / uz == pytest.approx(3000.0 / im.Z0)
    uz0 = im.mogi(0.0)[1]
    assert uz0 == pytest.approx((1 - im.NU) * im.DV / (math.pi * im.Z0 ** 2))
    assert im.mogi(im.half_radius(im.Z0))[1] == pytest.approx(uz0 / 2)
    assert im.volume_from_peak(uz0, im.Z0) == pytest.approx(im.DV)
    # on the north-south line the radar sees u_z cos(theta) only
    assert im.los(0.0, 2500.0) == pytest.approx(im.mogi(2500.0)[1] * math.cos(im.THETA))
    # east of the centre (towards the satellite) the line of sight shortens more
    assert im.los(3000.0, 0.0) > im.los(-3000.0, 0.0)
    # one fringe is half a wavelength
    assert im.phase(im.LAM / 2) == pytest.approx(0.0, abs=1e-9) or \
        im.phase(im.LAM / 2) == pytest.approx(2 * math.pi, abs=1e-9)
    assert im.phase(im.LAM / 8) == pytest.approx(math.pi / 2)
    assert im.LAM == pytest.approx(0.05547, rel=1e-3)


def test_slope_aspect_hillshade_on_a_plane():
    xs = np.arange(0.0, 1000.1, 100.0)
    ys = np.arange(0.0, 800.1, 100.0)
    # a plane z = a x + b y
    a, b = 0.15, -0.2
    z = np.array([[a * x + b * y for x in xs] for y in ys])
    dzdx, dzdy = vg.derivatives(z, 100.0)
    s = vg.slope_deg(dzdx, dzdy)
    asp = vg.aspect_deg(dzdx, dzdy)
    assert np.allclose(s, math.degrees(math.atan(math.hypot(a, b))))
    # steepest descent is along (-a, -b): east component -0.15, north +0.2
    assert np.allclose(asp, math.degrees(math.atan2(-a, -b)) % 360)
    flat = vg.hillshade(np.zeros((2, 2)), np.zeros((2, 2)))
    assert np.allclose(flat, math.cos(math.radians(45.0)))
    # a slope facing the light is brighter than flat ground, one facing away darker
    toward = vg.hillshade(np.array([20.0]), np.array([315.0]))
    away = vg.hillshade(np.array([20.0]), np.array([135.0]))
    assert toward[0] > flat[0, 0] > away[0]


def test_overlay_classes():
    slope = np.array([[20.0, 20.0, 5.0, 20.0]])
    units = np.array([[5, 5, 5, 4]])
    dist = np.array([[500.0, 1500.0, 500.0, 500.0]])
    assert vg.overlay(slope, units, dist).tolist() == [[3, 1, 2, 0]]
    assert vg.layers(slope, units).tolist() == [[3, 3, 2, 1]]
