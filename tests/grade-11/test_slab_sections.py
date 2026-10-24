"""figdata/grade-11/slab_sections.py: earthquake sections across subduction zones."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import slab_sections as ss  # noqa: E402


def test_distance_and_bearing():
    d, b = ss.dist_bearing(0.0, 0.0, 1.0, 0.0)
    assert abs(d - 111.19) < 0.05 and abs(b - 90.0) < 1e-6
    d, b = ss.dist_bearing(0.0, 0.0, 0.0, -1.0)
    assert abs(b - 180.0) < 1e-6


def test_profiles_point_to_the_overriding_plate():
    # Tonga: the Pacific sinks westward; Andes: Nazca sinks eastward; Japan: westward
    assert 250 < ss.trench("tonga")[2] < 320
    assert 60 < ss.trench("andes")[2] < 110
    assert 250 < ss.trench("japan")[2] < 320


def test_tonga_section_reaches_below_600_km_and_deepens_away_from_the_trench():
    rows = ss.project("tonga")
    assert max(z for _, z, _ in rows) > 600
    deep = [x for x, z, _ in rows if z > 500]
    mid = [x for x, z, _ in rows if 100 < z < 300]
    assert min(deep) > max(mid) - 100 and sum(deep) / len(deep) > sum(mid) / len(mid) + 200
    # no event deeper than 70 km lies seaward of the trench
    assert all(x > 0 for x, z, _ in rows if z > 70)


def test_dips_and_rates():
    n = ss.numbers()
    assert 35 < n["tonga_dip"] < 60 and 25 < n["andes_dip"] < 45
    assert n["tonga_fit_n"] > 50
    # PB2002 convergence: fast at Tonga, slower in the Andes and Japan
    assert 140 < n["tonga_rate"] < 200 and 50 < n["andes_rate"] < 80 and 80 < n["japan_rate"] < 100
    assert 4.5 < n["tonga_time670"] < 7.5


def test_old_floor_reaches_the_tonga_and_japan_trenches():
    n = ss.numbers()
    assert n["japan_age"] > 100 and n["tonga_age"] > 80 and n["andes_age"] < 70


def test_deep_earthquakes_lie_near_subduction_zones():
    sub = [(float(s["lon"]), float(s["lat"])) for s in ss.read("pb2002-steps")
           if s["class"] == "SUB"][::5]
    deep = [e for e in ss.quakes() if e[2] > ss.DEEP and e[3] >= 6.5]
    near = 0
    for lon, lat, _, _ in deep:
        if min(ss.dist_bearing(lon, lat, a, b)[0] for a, b in sub) < 1200:
            near += 1
    assert near / len(deep) > 0.97


def test_catalogue_matches_ledger():
    n = ss.numbers()
    assert n["catalogue_n"] == 7031 and abs(n["catalogue_maxdepth"] - 688) < 1


def test_plates_with_slabs_are_faster():
    rows, codes = ss.speed_rows()
    slab = [r for _, r, s in rows if s]
    free = [r for _, r, s in rows if not s]
    assert min(slab) > max(free)
    assert codes[0] == "co"
