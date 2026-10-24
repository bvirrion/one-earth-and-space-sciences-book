"""figdata/grade-7: plate speeds, earthquakes on boundaries, the South Atlantic."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-7"))
import plate_speeds  # noqa: E402
import quakes_on_boundaries as qb  # noqa: E402
import south_atlantic as sa  # noqa: E402


def test_speeds_ordered_and_plausible():
    s = dict(plate_speeds.speeds_cm_a())
    assert s["North-Atlantic-ridge"] < s["South-Atlantic-ridge"] < s["East-Pacific-Rise"]
    assert 1.5 < s["North-Atlantic-ridge"] < 3.5          # "about 2.5 cm/yr" on average (USGS)
    assert s["East-Pacific-Rise"] > 10
    assert 3.5 < s["San-Andreas"] < 6                      # "about 5 cm/yr" (USGS)


def test_most_large_quakes_lie_on_boundaries():
    n, near, pct = qb.share_near()
    assert n == 7031 and 85 < pct < 99


def test_exercise_12_bands():
    # exercise 12 quotes these three counts; they must grow with the distance
    counts = [qb.share_near(d)[1] for d in qb.BANDS_KM]
    assert counts == sorted(counts)
    assert counts == [4578, 6472, 6786]


def test_distance_function():
    # one degree of latitude along a meridian
    d = qb.nearest_boundary_km([0.0], [0.0], [1.0], [0.0])[0]
    assert abs(d - 2 * math.pi * qb.R_KM / 360) < 1e-6


def test_south_atlantic():
    am, af, kpd, width, rate, age = sa.summary()
    assert -44 < am < -42.5 and 13.5 < af < 15.5          # near Rio de Janeiro and Walvis Bay
    assert abs(kpd - 2 * math.pi * 6371 * math.cos(math.radians(23)) / 360) < 1e-9
    assert abs(age - width / (10 * rate)) < 1e-9
    assert 150 < age < 200
