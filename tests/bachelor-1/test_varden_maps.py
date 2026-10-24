"""figdata/bachelor-1/varden_maps.py agrees with the region's model."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "shared"))
import region as R  # noqa: E402
import varden_maps as VM  # noqa: E402


def test_boreholes_reach_the_contact_in_the_footwall():
    for _, x, y in VM.BOREHOLES:
        zg, d, zc = VM.borehole(x, y)
        assert d > 0 and not R.hanging_wall(x, y, zc)


def test_limb_attitudes_are_the_model():
    att = VM.attitudes()
    for name, x in (("E", 4500.0), ("W", 2000.0)):
        az, dip = R.limb_attitude(x)
        assert abs(att[name][0] - az) < 1e-6 and abs(att[name][1] - dip) < 1e-6


def test_fold_axis_trends_north_and_plunges_2_degrees():
    trend, plunge = VM.attitudes()["axis"]
    assert abs(trend) < 1e-6 or abs(trend - 360) < 1e-6
    assert abs(plunge - R.PLUNGE) < 1e-9


def test_fault_from_three_trace_points():
    az, dip = VM.attitudes()["F"]
    assert abs(az - R.FAULT_DIP_AZ) < 0.01 and abs(dip - R.FAULT_DIP) < 0.01


def test_hillshade_range():
    xs, ys, sh = VM.hillshade()
    assert sh.shape == (len(ys), len(xs)) and 0 <= sh.min() and sh.max() <= 1
