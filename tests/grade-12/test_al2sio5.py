import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12"))
import al2sio5 as al  # noqa: E402


def test_triple_point_at_the_source_values():
    t, p = al.triple_point()
    pt, pp = al.PRINTED_TRIPLE
    assert t == pytest.approx(pt, abs=1.0)            # 504 degC
    assert p == pytest.approx(pp, abs=0.02)           # 3.75 kbar
    # the third boundary passes through the same point
    assert al.p_and_sil(t) == pytest.approx(p, abs=0.02)


def test_slopes_and_fields():
    # kyanite = andalusite and kyanite = sillimanite rise with temperature,
    # andalusite = sillimanite falls
    assert al.AND_KY[600] > al.AND_KY[500] and al.KY_SIL[600] > al.KY_SIL[500]
    assert al.AND_SIL[600] < al.AND_SIL[500]
    assert al.stable(400, 6.0) == "kyanite"
    assert al.stable(500, 1.0) == "andalusite"
    assert al.stable(750, 3.0) == "sillimanite"
    assert al.stable(600, 7.0) == "kyanite"


def test_lithostatic_pressure():
    assert al.pressure_gpa(35.0) == pytest.approx(0.972, abs=0.001)    # about 1 GPa at 35 km
    assert al.depth_km(al.pressure_gpa(17.3)) == pytest.approx(17.3)
    assert al.depth_km(0.70) == pytest.approx(25.2, abs=0.05)          # the problem's named number


def test_geotherms_cross_the_fields_as_drawn():
    # typical gradient: kyanite then sillimanite, near 19 km
    c30 = al.crossings(30.0)
    assert [w for *_, w in c30] == ["kyanite->sillimanite"]
    assert c30[0][2] == pytest.approx(18.8, abs=0.1)
    # volcanic gradient: kyanite, andalusite, sillimanite
    assert [w for *_, w in al.crossings(50.0)] == ["kyanite->andalusite", "andalusite->sillimanite"]
    # subduction gradient: kyanite all the way to 45 km
    assert al.crossings(10.0) == []
