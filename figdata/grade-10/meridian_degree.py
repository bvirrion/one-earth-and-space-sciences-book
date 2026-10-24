"""Lengths on the reference ellipsoid (grade 10, measuring-the-earth).

WGS 84: a = 6378137 m, 1/f = 298.257223563 (ledger wgs84:ellipsoid).

  part (main)  lat_deg deg_km par_km     length of one degree of latitude (along
                                         the meridian) and of longitude (along the
                                         parallel) at each latitude, in km
  part numbers key value                 the numbers the chapter prints
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

A = 6378137.0
INV_F = 298.257223563
F = 1.0 / INV_F
E2 = F * (2.0 - F)
B = A * (1.0 - F)

# Eratosthenes redone with modern coordinates (ledger geonames:aswan, geonames:alexandria)
LAT_SYENE = 24.09082
LAT_ALEXANDRIA = 31.20176
# The meridian of the metre (ledger geonames:dunkirk, geonames:barcelona)
LAT_DUNKIRK = 51.03442
LAT_BARCELONA = 41.38879


def meridian_radius(lat_deg):
    """Radius of curvature of the meridian, m."""
    s = math.sin(math.radians(lat_deg))
    return A * (1.0 - E2) / (1.0 - E2 * s * s) ** 1.5


def normal_radius(lat_deg):
    s = math.sin(math.radians(lat_deg))
    return A / math.sqrt(1.0 - E2 * s * s)


def degree_length(lat_deg):
    """Length (km) of one degree of latitude centred on lat_deg."""
    return meridian_arc(lat_deg - 0.5, lat_deg + 0.5)


def parallel_degree(lat_deg):
    """Length (km) of one degree of longitude along the parallel lat_deg."""
    return normal_radius(lat_deg) * math.cos(math.radians(lat_deg)) * math.pi / 180.0 / 1000.0


def meridian_arc(lat1, lat2, n=2000):
    """Length (km) of the meridian between two latitudes (Simpson's rule)."""
    if n % 2:
        n += 1
    h = (lat2 - lat1) / n
    s = meridian_radius(lat1) + meridian_radius(lat2)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * meridian_radius(lat1 + i * h)
    return s * h / 3.0 * math.pi / 180.0 / 1000.0


def quarter_meridian():
    return meridian_arc(0.0, 90.0)


def numbers():
    q = quarter_meridian()
    d = LAT_ALEXANDRIA - LAT_SYENE
    arc = meridian_arc(LAT_SYENE, LAT_ALEXANDRIA)
    return {
        "a_km": A / 1000.0,
        "b_km": B / 1000.0,
        "a_minus_b_km": (A - B) / 1000.0,
        "deg_equator_km": degree_length(0.0),
        "deg_45_km": degree_length(45.0),
        "deg_66_km": degree_length(66.0),
        "deg_pole_km": meridian_radius(90.0) * math.pi / 180.0 / 1000.0,
        "deg_equator_exact_km": meridian_radius(0.0) * math.pi / 180.0 / 1000.0,
        "par_equator_km": parallel_degree(0.0),
        "par_60_km": parallel_degree(60.0),
        "quarter_meridian_km": q,
        "meridian_circumference_km": 4.0 * q,
        "equator_circumference_km": 2.0 * math.pi * A / 1000.0,
        "metre_short_by_mm": (q * 1000.0 / 1.0e7 - 1.0) * 1000.0,
        "syene_alexandria_dlat_deg": d,
        "syene_alexandria_arc_km": arc,
        "eratosthenes_modern_km": arc * 360.0 / d,
        "dunkirk_barcelona_dlat_deg": LAT_DUNKIRK - LAT_BARCELONA,
        "dunkirk_barcelona_arc_km": meridian_arc(LAT_BARCELONA, LAT_DUNKIRK),
    }


if __name__ == "__main__":
    rows = [(lat, degree_length(min(max(lat, 0.5), 89.5)) if 0 < lat < 90 else
             meridian_radius(lat) * math.pi / 180.0 / 1000.0, parallel_degree(lat))
            for lat in range(0, 91, 2)]
    write_table(__file__, ("lat_deg", "deg_km", "par_km"), rows)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=9)
