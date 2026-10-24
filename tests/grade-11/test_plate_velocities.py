"""figdata/grade-11/plate_velocities.py: velocities from the NNR-MORVEL56 poles."""
import math
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import plate_velocities as pv  # noqa: E402

LEDGER = os.path.join(os.path.dirname(__file__), "..", "..", "sources", "ledger", "book2.md")


def test_point_on_the_pole_does_not_move():
    for code, (_, lat, lon, _, _) in pv.POLES.items():
        ve, vn = pv.velocity(code, lon, lat)
        assert math.hypot(ve, vn) < 1e-9


def test_speed_at_ninety_degrees_from_the_pole():
    # one degree per Myr at 90 degrees from the pole is 6371 * pi / 180 = 111.2 mm/yr
    _, lat, lon, w, _ = pv.POLES["pa"]
    # a point on the great circle 90 degrees from the pole: rotate the pole by 90 degrees
    plat = lat + 90 if lat <= 0 else lat - 90
    ve, vn = pv.velocity("pa", lon, plat)
    assert abs(math.hypot(ve, vn) - w * 6371 * math.pi / 180) < 1e-6


def test_motion_is_counter_clockwise_about_the_pole():
    # just 'south' of a north-hemisphere pole the motion of a counter-clockwise rotation
    # (seen from above the pole) is towards the east
    _, lat, lon, _, _ = pv.POLES["eu"]
    ve, vn = pv.velocity("eu", lon, lat - 10)
    assert ve > 0 and abs(vn) < 1e-6


def test_pacific_at_hawaii_seven_cm_toward_the_west_north_west():
    s, az = pv.speed_azimuth(*pv.velocity("pa", *pv.MKEA))
    assert 65 < s < 75 and 285 < az < 310


def test_model_agrees_with_the_two_stations():
    sys.path.insert(0, os.path.dirname(pv.__file__))
    import gnss_series as gs
    for site, code, lonlat in (("mkea", "pa", pv.MKEA), ("wtzr", "eu", (12.879, 49.144))):
        be, bn, _ = gs.rates(site)
        ve, vn = pv.velocity(code, *lonlat)
        assert math.hypot(be - ve, bn - vn) < 5.0          # mm/yr


def test_relative_motion_is_antisymmetric():
    a = pv.relative("sa", "nb", -13.5, -30.0)
    b = pv.relative("nb", "sa", -13.5, -30.0)
    assert abs(a[0] + b[0]) < 1e-12 and abs(a[1] + b[1]) < 1e-12


def test_ridges_open_at_published_scale():
    n = pv.numbers()
    assert 25 < n["atl30s_speed"] < 40           # slow Atlantic
    assert 130 < n["epr30s_speed"] < 160         # fast East Pacific Rise
    assert 35 < n["in_eu_speed"] < 50            # India into Eurasia


def test_plates_with_slabs_are_faster():
    n = pv.numbers()
    assert n["rms_slab_mean"] > 2 * n["rms_noslab_mean"]


def test_poles_match_the_ledger():
    text = open(LEDGER, encoding="utf8").read()
    row = [l for l in text.splitlines() if l.startswith("| nnr56:poles ")][0]
    for code in ("pa", "na", "eu", "in", "nz"):
        _, lat, lon, w, _ = pv.POLES[code]
        assert ("%.2f" % lat) in row and ("%.2f" % lon) in row and ("%.3f" % w) in row
    row = [l for l in text.splitlines() if l.startswith("| nnr56:rms ")][0]
    for code in pv.SLAB:
        assert ("%.1f" % pv.POLES[code][4]) in row
