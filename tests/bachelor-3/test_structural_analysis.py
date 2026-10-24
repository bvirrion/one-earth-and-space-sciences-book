"""Tests for the stereonet, palaeostress and Fry figdata scripts (Year 3, ch. 8)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import fry  # noqa: E402
import stereonet as sn  # noqa: E402


def test_projection_radii_and_properties():
    # a horizontal line lands on the primitive, a vertical one at the centre, in both nets
    for kind in ("wulff", "schmidt"):
        assert math.hypot(*sn.project(sn.line_vec(37.0, 0.0), kind)) == pytest.approx(1.0)
        assert math.hypot(*sn.project(sn.line_vec(37.0, 90.0), kind)) == pytest.approx(0.0, abs=1e-12)
    # Schmidt: the area inside the projected cap theta < t is proportional to the cap's area
    for t in (20.0, 50.0, 80.0):
        r = math.hypot(*sn.project(sn.line_vec(0.0, 90.0 - t)))
        # cap area 2 pi (1 - cos t) on the unit sphere, half of it on the net of radius 1
        assert math.pi * r ** 2 == pytest.approx(math.pi * (1 - math.cos(math.radians(t))))
    # Wulff is conformal: a small circle of 10 deg about a line projects to a circle
    c = sn.line_vec(60.0, 30.0)
    e1 = np.cross(c, [0, 0, 1.0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(c, e1)
    pts = np.array([sn.project(math.cos(0.17) * c + math.sin(0.17) * (math.cos(u) * e1 + math.sin(u) * e2), "wulff")
                    for u in np.linspace(0, 2 * math.pi, 37)])
    ctr = (pts.max(axis=0) + pts.min(axis=0)) / 2
    rad = np.hypot(*(pts - ctr).T)
    assert rad.std() / rad.mean() < 1e-3


def test_great_circle_contains_the_plane_and_pole_is_90_deg_away():
    for dd, dip in ((120.0, 60.0), (80.7, 12.16), (300.0, 85.0)):
        n = sn.normal(dd, dip)
        for v in sn.plane_lines(dd, dip, 7):
            assert float(v @ n) == pytest.approx(0.0, abs=1e-12)
            assert v[2] <= 1e-12


def test_varden_fold_axis_recovered():
    reads = sn.readings()
    assert len(reads) == 12
    poles = [-sn.normal(a, d) for a, d in reads]
    w, b = sn.beta_from_tensor(poles)
    tr, pl = sn.vec_line(b)
    assert (tr + 180) % 360 - 180 == pytest.approx(0.0, abs=1.0)
    assert pl == pytest.approx(2.0, abs=0.3)
    # the two estimates agree, and the girdle is narrow (cylindrical fold)
    tr2, pl2 = sn.vec_line(sn.beta_from_means(reads))
    assert pl2 == pytest.approx(pl, abs=0.05)
    assert w[0] / w[1] < 0.02
    # without scatter, the limbs of region.py give exactly the 2 deg plunge
    import region
    e = sn.normal(*region.limb_attitude(region.AXIS_ANTI + 10.0))
    wv = sn.normal(*region.limb_attitude(region.AXIS_ANTI - 10.0))
    assert sn.vec_line(np.cross(e, wv))[1] == pytest.approx(region.PLUNGE, abs=1e-9)


def test_wallace_bott_senses_and_independence():
    # sigma1 vertical -> normal faulting; sigma1 horizontal across strike -> reverse
    s_normal = sn.reduced_stress(0.5, 90.0)
    assert sn.rake(90.0, 60.0, sn.hanging_wall_slip(s_normal, 90.0, 60.0)) == pytest.approx(-90.0)
    e = sn.line_vec(90.0, 0.0)
    s_rev = np.outer(e, e)
    assert sn.rake(90.0, 30.0, sn.hanging_wall_slip(s_rev, 90.0, 30.0)) == pytest.approx(90.0)
    # adding an isotropic part or scaling the tensor leaves the shear direction unchanged
    s = sn.reduced_stress()
    for dd, dp in ((150.0, 55.0), (200.0, 70.0)):
        u = sn.hanging_wall_slip(s, dd, dp)
        assert np.allclose(sn.hanging_wall_slip(3.0 * s + 7.0 * np.eye(3), dd, dp), u)
    # rake <-> slip round trip
    for rk in (-150.0, -90.0, -10.0, 45.0, 120.0):
        assert sn.rake(150.0, 55.0, sn.slip_from_rake(150.0, 55.0, rk)) == pytest.approx(rk)


def test_varden_fault_is_pure_dip_slip_and_inversion_recovers_stress():
    fl = sn.faults()
    assert fl[0] == (120.0, 60.0, -90)
    for phi in (0.0, 0.5, 1.0):
        u = sn.hanging_wall_slip(sn.reduced_stress(phi), 120.0, 60.0)
        assert sn.rake(120.0, 60.0, u) == pytest.approx(-90.0)
    m, phi, tr = sn.invert(fl)
    assert phi == pytest.approx(sn.PHI_TRUE, abs=0.02)
    assert tr == pytest.approx(sn.SIGMA3_TREND, abs=2)
    for f in fl[1:]:
        assert sn.phi_from_rake(*f) == pytest.approx(sn.PHI_TRUE, abs=0.02)


def test_fry_void_recovers_the_strain_ellipse():
    p = fry.undeformed()
    d = np.hypot(*(p[:, None, :] - p[None, :, :]).reshape(-1, 2).T)
    assert d[d > 0].min() >= 1.0
    # area preserved by the strain
    assert np.linalg.det(fry.strain_matrix()) == pytest.approx(1.0)
    ratio, theta, size = fry.fit_ellipse(fry.void_boundary(fry.fry_points(fry.deformed())))
    assert ratio == pytest.approx(fry.R_TRUE, rel=0.1)
    assert theta == pytest.approx(fry.THETA_TRUE, abs=3)
    assert size == pytest.approx(1.0, rel=0.1)
