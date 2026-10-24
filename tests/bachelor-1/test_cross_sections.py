"""Ch. 5 (cross-sections): apparent dips measured in the model equal the
theorem's, logs and tunnel agree with region.py, the fault crossing lies on
the fault plane."""
import math
import os
import sys

HERE = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
import region as R  # noqa: E402
import varden_sections as V  # noqa: E402


def test_apparent_dip_theorem_matches_model():
    az, dip = R.limb_attitude(4300.0)
    for sec_az in (90.0, 71.5651, 45.0, 120.0, 180.0):
        measured = V.section_slope(4300.0, 6000.0, sec_az)
        assert abs(measured - V.apparent_dip(dip, az, sec_az)) < 1e-6


def test_apparent_dip_in_true_dip_direction_is_true_dip():
    assert abs(V.apparent_dip(30.0, 120.0, 120.0) - 30.0) < 1e-12
    assert abs(V.apparent_dip(30.0, 120.0, 30.0)) < 1e-12           # along strike


def test_exaggeration():
    assert abs(math.tan(math.radians(V.exaggerated(12.0, 2))) - 2 * math.tan(math.radians(12.0))) < 1e-12


def test_logs_equal_model():
    for _, x in V.LOGS:
        zg, d = V.log(x)
        for name, depth in zip(("chalk", "shale", "limestone", "sandstone"), d):
            if not math.isnan(depth):
                assert abs(zg - depth - R.contact_elevation(name, x, V.Y_CD)) < 1e-9


def test_tunnel_limestone_length():
    expected = 2 * R.THICK["limestone"] / math.tan(math.radians(R.LIMB_DIP))
    assert abs(V.limestone_length() - expected) < 0.01


def test_fault_crossing_on_plane():
    x = V.fault_x_at(V.Y_CD, V.Z_TUNNEL)
    assert not R.hanging_wall(x - 0.01, V.Y_CD, V.Z_TUNNEL)
    assert R.hanging_wall(x + 0.01, V.Y_CD, V.Z_TUNNEL)


def test_structure_contours_respect_fault_blocks():
    """Each contour vertex lies on the surface of its own fault block, at its level."""
    sx, sy, sz = R._slip()
    for lv, run in V.structure_contours(step=100.0):
        for x, y in run:
            zf = R._contact_unfaulted("limestone", x, y)
            zh = R._contact_unfaulted("limestone", x - sx, y - sy) + sz
            foot = abs(zf - lv) < 3.0 and not R.hanging_wall(x, y, zf - 1.0)
            hang = abs(zh - lv) < 3.0 and R.hanging_wall(x, y, zh + 1.0)
            assert foot or hang, (lv, x, y, zf, zh)
