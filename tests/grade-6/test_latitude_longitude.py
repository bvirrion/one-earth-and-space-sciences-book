"""figdata/grade-6: ideal time zones, the cities of the map, the graticule globe."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-6"))
import cities as ci  # noqa: E402
import graticule as gr  # noqa: E402
import time_zones as tz  # noqa: E402


def test_fifteen_degrees_an_hour():
    assert tz.degrees_per_hour() == 15.0


def test_offsets_and_the_date_line():
    assert tz.offset(0) == 0 and tz.offset(7.4) == 0 and tz.offset(7.6) == 1
    assert tz.offset(-7.6) == -1 and tz.offset(179.9) == 12 and tz.offset(-179.9) == -12
    b = tz.bands()
    assert len(b) == 25 and b[0][0] == -180 and b[-1][1] == 180
    assert all(abs(b[i][1] - b[i + 1][0]) < 1e-9 for i in range(len(b) - 1))
    assert sum(hi - lo for lo, hi, _ in b) == 360


def test_cities_zones_used_in_the_problem():
    p = ci.load()
    z = {n: tz.offset(p[n][0]) for n in p}
    assert z["London"] == 0 and z["Rio de Janeiro"] == -3 and z["Tokyo"] == 9
    assert z["Auckland"] == 12 and z["Los Angeles"] == -8
    # Friday 20:00 in London -> Saturday 08:00 in Auckland, Friday 12:00 in Los Angeles
    assert tz.local_time(20, p["Auckland"][0]) == (8, 1)
    assert tz.local_time(20, p["Los Angeles"][0]) == (12, 0)
    assert tz.local_time(20, p["Tokyo"][0]) == (5, 1)
    assert tz.local_time(20, p["Rio de Janeiro"][0]) == (17, 0)


def test_rounded_coordinates_quoted():
    assert ci.rounded("Cairo") == (30, "N", 31, "E")
    assert ci.rounded("Sydney") == (34, "S", 151, "E")
    assert ci.rounded("New York") == (41, "N", 74, "W")
    assert ci.rounded("Quito")[0] == 0              # almost on the equator


def test_graticule_point_is_on_the_disk():
    for lo, la in ((0, 90), (60, 30), (10, 25)):
        x, y, d = gr.point(lo, la)
        assert abs(x * x + y * y + d * d - 1) < 1e-9 and d > 0
    x, y, d = gr.point(10, 25)
    assert abs(x) < 1e-12 and abs(y) < 1e-12        # the view centre
    assert math.isclose(gr.point(0, 90)[1], math.cos(math.radians(25)), abs_tol=1e-9)
