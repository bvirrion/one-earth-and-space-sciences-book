"""figdata/grade-5: climate charts from the NOAA normals, and the climate zones."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-5"))
import climate_charts as cc  # noqa: E402
import climate_zones as cz  # noqa: E402


def test_unit_conversion_matches_a_hand_value():
    # Phoenix, July: 95.5 deg F and 0.91 in in the NOAA file -> 35.3 deg C, 23.1 mm
    m, t, p = cc.load("phoenix")[6]
    assert m == 7 and abs(t - 35.3) < 0.05 and abs(p - 23.1) < 0.05


def test_the_four_climates_are_what_the_text_says():
    ph, hi, se, ut = (cc.summary(s) for s in cc.STATIONS)
    assert ph["total_mm"] < 250 and ph["warmest_C"] > 35          # hot desert
    assert hi["total_mm"] > 3000 and hi["range_C"] < 4              # rainforest
    assert hi["coldest_C"] > 21
    assert 900 < se["total_mm"] < 1100 and se["coldest_C"] > 5      # temperate, mild winter
    assert se["wettest_month"] == 11 and se["driest_month"] == 7
    assert ut["mean_C"] < -10 and ut["warmest_C"] < 6               # polar
    assert [m for m, t, _ in cc.load("utqiagvik") if t > 0] == [6, 7, 8, 9]  # Jun to Sep only


def test_zones_from_the_tilt():
    assert abs(cz.tropic() - 23.44) < 1e-9 and abs(cz.polar_circle() - 66.56) < 1e-9
    assert cz.zone(0) == "hot" and cz.zone(-30) == "temperate" and cz.zone(80) == "cold"
    shares = [cz.area_share(a, b) for _, a, b in cz.bands()]
    assert abs(sum(shares) - 1) < 1e-12
    assert 0.39 < shares[2] < 0.40          # the hot zone is about two fifths of the Earth


def test_stations_and_their_zones():
    z = {n: cz.zone(la) for n, la, _ in cz.STATIONS}
    assert z == {"Phoenix": "temperate", "Hilo": "hot", "Seattle": "temperate",
                 "Utqiagvik": "cold"}
