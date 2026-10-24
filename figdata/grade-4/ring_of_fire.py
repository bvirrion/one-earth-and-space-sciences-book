"""Volcanoes and large earthquakes around the Pacific (grade 4, first look).

Reads the shared catalogues (data/derived/gvp-holocene.csv, ledger data:gvp;
data/derived/usgs-m6.csv, ledger data:usgs-comcat) and counts how many lie in
the "ring around the Pacific": within RING_KM of the line of island arcs and
coastal mountain ranges that runs round the Pacific Ocean (RING below, drawn on
the book's map). The line follows the ocean trenches named in the comments; it
includes Indonesia, as most maps of the "Ring of Fire" do.

  part ring      : lon lat of the ring line (blank line between branches)
  part volcanoes : lon lat ring(0/1)
  part quakes7   : lon lat mag ring(0/1)   (magnitude 7 or more only)
  main table     : what, total, in_ring, percent, per_year
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RING_KM = 500.0
YEARS = 50          # the shared earthquake catalogue: 1976-01-01 to 2025-12-31

# (lon, lat) along the arcs; the Indonesian branch leaves the main line at New
# Guinea, the Mariana branch at Japan
RING = [
    [(175.0, -41.0),   # New Zealand, North Island
     (-178.0, -30.0),  # Kermadec
     (-174.0, -20.0),  # Tonga
     (168.0, -17.0),   # Vanuatu
     (157.0, -8.0),    # Solomon Islands
     (146.0, -6.0),    # New Guinea
     (128.0, 0.0),     # Molucca Sea
     (125.0, 10.0),    # Philippines
     (121.5, 23.0),    # Taiwan
     (129.0, 29.0),    # Ryukyu
     (140.0, 35.5),    # Japan
     (148.0, 44.0),    # Kuril Islands
     (159.0, 53.0),    # Kamchatka
     (172.0, 52.0),    # western Aleutians
     (-175.0, 51.5),
     (-160.0, 55.0),   # eastern Aleutians
     (-150.0, 60.5),   # southern Alaska
     (-137.0, 58.5),
     (-123.5, 46.0),   # Cascades
     (-121.0, 37.0),   # California
     (-115.0, 32.0),
     (-104.0, 19.0),   # Mexico
     (-91.0, 14.0),    # Central America
     (-84.0, 10.0),
     (-77.5, 3.0),     # Colombia
     (-78.5, -2.0),    # Ecuador
     (-77.0, -12.0),   # Peru
     (-70.5, -20.0),   # northern Chile
     (-71.0, -33.0),   # central Chile
     (-73.5, -42.0),
     (-74.0, -52.0)],  # southern Chile
    [(146.0, -6.0),    # from New Guinea west along Indonesia
     (130.0, -7.0),    # Banda
     (118.0, -9.0),    # Nusa Tenggara
     (108.0, -8.0),    # Java
     (100.0, -3.0),    # Sumatra
     (95.0, 4.0)],
    [(140.0, 35.5),    # from Japan south along the Izu, Bonin and Mariana islands
     (142.0, 27.0),
     (145.5, 18.0),
     (144.5, 13.0)],   # Guam
]


def read(name):
    with open(os.path.join(ROOT, "data", "derived", name + ".csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


def _xyz(lon, lat):
    lo, la = math.radians(lon), math.radians(lat)
    return (math.cos(la) * math.cos(lo), math.cos(la) * math.sin(lo), math.sin(la))


def _gc_dist_km(p, a, b, r=6371.0):
    """Distance from point p to the great-circle segment a-b (unit vectors), km."""
    n = (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
    nn = math.sqrt(sum(c * c for c in n))
    dot = lambda u, v: sum(x * y for x, y in zip(u, v))
    ang = lambda u, v: math.acos(max(-1.0, min(1.0, dot(u, v))))
    if nn > 1e-12:
        n = tuple(c / nn for c in n)
        s = dot(p, n)
        q = tuple(pc - s * nc for pc, nc in zip(p, n))
        qn = math.sqrt(sum(c * c for c in q))
        if qn > 1e-12:
            q = tuple(c / qn for c in q)
            if abs(ang(a, q) + ang(q, b) - ang(a, b)) < 1e-9:
                return r * abs(math.asin(max(-1.0, min(1.0, s))))
    return r * min(ang(p, a), ang(p, b))


def dist_to_ring_km(lon, lat):
    p = _xyz(lon, lat)
    best = 1e9
    for branch in RING:
        pts = [_xyz(*q) for q in branch]
        for a, b in zip(pts, pts[1:]):
            best = min(best, _gc_dist_km(p, a, b))
    return best


def in_ring(lon, lat):
    return dist_to_ring_km(lon, lat) <= RING_KM


def volcanoes():
    return [(float(v["lon"]), float(v["lat"])) for v in read("gvp-holocene")]


def quakes(min_mag=6.0):
    return [(float(e["lon"]), float(e["lat"]), float(e["mag"])) for e in read("usgs-m6")
            if float(e["mag"]) >= min_mag]


def shares():
    vs = volcanoes()
    q6 = quakes(6.0)
    q7 = quakes(7.0)
    out = {}
    for name, pts in (("volcanoes", vs), ("quakes6", q6), ("quakes7", q7)):
        n_in = sum(in_ring(p[0], p[1]) for p in pts)
        out[name] = (len(pts), n_in)
    return out


def _ring_rows():
    rows = []
    for branch in RING:
        if rows:
            rows.append(())
        prev = None
        for lon, lat in branch:
            if prev is not None and abs(lon - prev) > 180:      # crossing the 180th meridian
                rows.append(())
            rows.append((lon, lat))
            prev = lon
    return rows


if __name__ == "__main__":
    write_table(__file__, ("lon", "lat"), _ring_rows(), part="ring")
    write_table(__file__, ("lon", "lat", "ring"),
                [(lo, la, int(in_ring(lo, la))) for lo, la in volcanoes()], part="volcanoes")
    write_table(__file__, ("lon", "lat", "mag", "ring"),
                [(lo, la, m, int(in_ring(lo, la))) for lo, la, m in quakes(7.0)], part="quakes7")
    s = shares()
    rows = []
    for k, (n, n_in) in s.items():
        rows.append((k, n, n_in, round(100.0 * n_in / n, 1), round(n / YEARS, 1)))
    write_table(__file__, ("what", "total", "in_ring", "percent", "per_year"), rows)
    print(rows)
