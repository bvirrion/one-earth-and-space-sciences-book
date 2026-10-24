"""figdata/grade-4: the ring around the Pacific and its shares."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-4"))
import ring_of_fire as rf  # noqa: E402


def test_places_on_the_ring():
    for name, lon, lat in (("Tokyo", 139.7, 35.7), ("Santiago", -70.7, -33.4),
                           ("Anchorage", -149.9, 61.2), ("Jakarta", 106.8, -6.2),
                           ("Mount St. Helens", -122.2, 46.2), ("Tonga", -175.2, -21.1),
                           ("Wellington", 174.8, -41.3), ("Guatemala", -90.5, 14.6),
                           ("Guam", 144.8, 13.4)):
        assert rf.in_ring(lon, lat), name


def test_places_off_the_ring():
    for name, lon, lat in (("Hawaii", -155.3, 19.4), ("Iceland", -19.0, 64.9),
                           ("Etna", 15.0, 37.7), ("Kathmandu", 85.3, 27.7),
                           ("Tehran", 51.4, 35.7), ("Kilimanjaro", 37.4, -3.1),
                           ("Mid-Atlantic", -30.0, 0.0), ("Yellowstone", -110.7, 44.4)):
        assert not rf.in_ring(lon, lat), name


def test_distance_to_a_segment():
    # a point 1 degree of latitude north of a segment along the equator: ~111 km
    rf_ring = rf.RING
    try:
        rf.RING = [[(0.0, 0.0), (10.0, 0.0)]]
        assert abs(rf.dist_to_ring_km(5.0, 1.0) - 111.2) < 0.5
        # beyond the end of the segment the distance is to the end point
        assert abs(rf.dist_to_ring_km(12.0, 0.0) - 222.4) < 0.5
    finally:
        rf.RING = rf_ring


def test_shares_and_rates():
    s = rf.shares()
    n_v, in_v = s["volcanoes"]
    n6, in6 = s["quakes6"]
    n7, in7 = s["quakes7"]
    assert n_v == 1214 and n6 == 7031
    assert 0.62 < in_v / n_v < 0.72                 # "about 2 out of 3"
    assert 0.70 < in7 / n7 < 0.80                   # "about 3 out of 4"
    assert round(n6 / rf.YEARS) == 141              # M >= 6 per year
    assert round(n7 / rf.YEARS) == 14               # M >= 7 per year
