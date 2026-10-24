"""figdata/grade-3: the globe seen from the Atlantic and from the Pacific."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-3"))
import globe  # noqa: E402


def test_view_centre_maps_to_the_disk_centre():
    for v in globe.VIEWS.values():
        x, y, d = globe.project(globe.xyz(*v), v)
        assert abs(x) < 1e-12 and abs(y) < 1e-12 and abs(d - 1) < 1e-12


def test_north_is_up_and_east_is_right():
    v = (0.0, 0.0)
    x, y, _ = globe.project(globe.xyz(0.0, 30.0), v)
    assert abs(x) < 1e-12 and y > 0
    x, y, _ = globe.project(globe.xyz(30.0, 0.0), v)
    assert x > 0 and abs(y) < 1e-12


def test_clipped_land_stays_inside_the_disk():
    for v in globe.VIEWS.values():
        for p in globe.land(v):
            assert all(math.hypot(x, y) <= 1 + 1e-9 for x, y in p)
            assert globe.polygon_area(p) > 0        # anticlockwise: land on the left


def test_a_square_ring_cut_by_the_limb_closes_along_it():
    # a 20 x 20 degree box astride the limb of the view at (0, 0): half visible
    box = [(80.0, -10.0), (100.0, -10.0), (100.0, 10.0), (80.0, 10.0), (80.0, -10.0)]
    polys = globe.clip(globe.oriented(box), (0.0, 0.0))
    assert len(polys) == 1
    assert max(math.hypot(x, y) for x, y in polys[0]) > 0.999


def test_atlantic_side_shows_more_land_than_pacific_side():
    rs = globe.rings()
    a = globe.land_fraction(globe.VIEWS["atlantic"], rs)
    p = globe.land_fraction(globe.VIEWS["pacific"], rs)
    assert 0.25 < a < 0.5 and 0.03 < p < 0.2 and a > 2 * p


def _inside(poly, x, y):
    c = False
    for (x0, y0), (x1, y1) in zip(poly, poly[1:]):
        if (y0 > y) != (y1 > y) and x < x0 + (y - y0) * (x1 - x0) / (y1 - y0):
            c = not c
    return c


def test_labels_sit_on_land_or_on_sea_as_they_should():
    rs = globe.rings()
    for v in globe.VIEWS.values():
        polys = globe.land(v, rs)
        for name, x, y in globe.labels(v):
            on_land = any(_inside(p, x, y) for p in polys)
            assert on_land == (not name.endswith("Ocean")), name


def test_each_view_names_its_own_ocean():
    a = [n for n, _, _ in globe.labels(globe.VIEWS["atlantic"])]
    p = [n for n, _, _ in globe.labels(globe.VIEWS["pacific"])]
    assert "Atlantic Ocean" in a and "Pacific Ocean" not in a
    assert "Pacific Ocean" in p and "Atlantic Ocean" not in p
