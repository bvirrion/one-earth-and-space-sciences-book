"""The V-rule panels obey the theorem: the V points upstream (south, smaller y)
unless the contact dips downstream more steeply than the valley floor."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import v_rule as V  # noqa: E402


def apex_shift(case):
    """y on the axis minus y 400 m to the side: < 0 means the V points upstream."""
    return V.outcrop_y(case, 0.0) - V.outcrop_y(case, 400.0)


def test_cases():
    assert apex_shift("h") < -100          # horizontal: follows the contours, V upstream
    assert apex_shift("u") < 0             # dipping upstream: V upstream
    assert apex_shift("g") < 0             # downstream but gentler than the floor: V upstream
    assert apex_shift("d") > 0             # downstream, steeper than the floor: V downstream
    assert abs(apex_shift("v")) < 1e-6     # vertical: straight


def test_theorem_formula():
    # x_v - x_h = h / (a - s) with h the extra height of the side, a = tan(apparent dip
    # downstream), s = valley gradient (see the chapter's proof)
    h = V.SIDE * 400.0
    for case, (_, dip, sense) in V.CASES.items():
        if dip == 90.0:
            continue
        a = sense * math.tan(math.radians(dip))
        assert abs(apex_shift(case) - h / (a - V.GRAD)) < 1e-3
