"""Magmatism at subduction zones (grade 12): where the volcanoes are, how deep the slab is
beneath them, and how water lowers the melting temperature of the mantle.

World: the Holocene volcanoes of the shared GVP table (data/derived/gvp-holocene.csv;
ledger data:gvp) split by their tectonic setting, 'Subduction zone' or any other.

North-east Japan: USGS ComCat events of magnitude 4.5 or more, 1976-2025, in the band
37.5-40.5 N, 138-146 E (data/derived/grade-12-usgs-ne-japan.csv, Book 2 block of
tools/fetch_data.py; ledger data:b2-usgs-ne-japan), with the GVP volcanoes of the same
band. The volcanic front is the easternmost volcano of the band. The slab: a straight
line fitted (least squares) to depth against longitude for the events deeper than
70 km between 139.5 and 142.5 E (shallower events also include the plate-boundary
fault and the overriding plate). Distances east: 1 degree of longitude = 111.2 cos(39 N)
km.

Melting: the dry peridotite solidus of Hirschmann (2000), T = a P^2 + b P + c (ledger
hirschmann:solidus), with the pressure at a depth from the PREM densities, as in
grade-11 geotherm_solidus.py (imported). The water-saturated solidus is known only
roughly (published versions differ by 200-600 degC): between 950 and 1000 degC at 3 GPa
(Wang et al. 2020, ledger wang20:wet-solidus) and just above 1000 degC from 5 to 11 GPa
(Kawamoto and Holloway 1997, ledger kh97:wet-solidus).

  part world-sub    lon lat                  volcanoes in a subduction-zone setting
  part world-other  lon lat                  the other volcanoes
  part jp-quakes    x_km depth mag           events of the NE Japan band (x east of 138 E)
  part jp-volc      x_km                     volcanoes of the band
  part jp-slab      x_km depth               the fitted slab line, from x = 0 to the surface
  part jp-bins      lon n median_depth       events deeper than 70 km, 0.5-degree bins (problem table)
  part solidus      depth_km P_GPa T_dry     dry solidus, 0-250 km
  part wet          P_GPa depth_km T_lo T_hi T_mid   the bracketed wet values (3 GPa; 5 and 7 GPa)
  part numbers      key value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "grade-11"))
from _table import write_table  # noqa: E402
import geotherm_solidus as gs  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")
BAND = (37.5, 40.5, 138.0, 146.0)       # lat min, lat max, lon min, lon max
LON0, LAT_MID = 138.0, 39.0
KM_PER_DEG_LON = 2 * math.pi * 6371.0 / 360.0 * math.cos(math.radians(LAT_MID))
FIT = (70.0, 139.5, 142.5)              # depth min, lon min, lon max of the fitted events
WET = ((3.0, 950.0, 1000.0), (5.0, 1000.0, 1000.0), (7.0, 1000.0, 1000.0))
SYRACUSE_MEAN_H = 105.0                 # km, global average slab depth beneath arcs


GEO_SUB = os.path.join(HERE, "..", "out", "shared-geo-subduction.dat")
BINS = (140.0, 140.5, 141.0, 141.5)


def trench_lon(lat=LAT_MID, lon_range=(142.0, 146.0)):
    """Longitude of the Japan Trench (PB2002 subduction line, shared geo table) nearest lat."""
    best = None
    with open(GEO_SUB, encoding="utf8") as f:
        next(f)
        for line in f:
            s = line.split()
            if len(s) != 2 or s[0] == "nan":
                continue
            lo, la = float(s[0]), float(s[1])
            if lon_range[0] <= lo <= lon_range[1] and (best is None or abs(la - lat) < abs(best[1] - lat)):
                best = (lo, la)
    return best[0]


def bins():
    import statistics
    q = list(jp_quakes())
    out = []
    for c in BINS:
        ds = [d for lo, la, d, m in q if d >= FIT[0] and c - 0.25 <= lo < c + 0.25]
        out.append((c, len(ds), statistics.median(ds)))
    return out


def volcanoes():
    with open(os.path.join(DERIVED, "gvp-holocene.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            yield float(r["lon"]), float(r["lat"]), r["setting"], r["name"]


def in_band(lon, lat):
    return BAND[0] <= lat <= BAND[1] and BAND[2] <= lon <= BAND[3]


def x_km(lon):
    return (lon - LON0) * KM_PER_DEG_LON


def jp_quakes():
    with open(os.path.join(DERIVED, "grade-12-usgs-ne-japan.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            lon, lat = float(r["lon"]), float(r["lat"])
            if in_band(lon, lat):
                yield lon, lat, float(r["depth_km"]), float(r["mag"])


def jp_volcanoes():
    return [(lon, lat, name) for lon, lat, s, name in volcanoes() if in_band(lon, lat)]


def slab_fit():
    """depth = a + b * x_km for the events deeper than FIT[0] between FIT[1] and FIT[2] E."""
    pts = [(x_km(lon), d) for lon, lat, d, m in jp_quakes() if d >= FIT[0] and FIT[1] <= lon <= FIT[2]]
    n = len(pts)
    mx = sum(p[0] for p in pts) / n
    my = sum(p[1] for p in pts) / n
    b = sum((x - mx) * (y - my) for x, y in pts) / sum((x - mx) ** 2 for x, y in pts)
    return my - b * mx, b, n


def front_lon():
    return max(lon for lon, lat, name in jp_volcanoes())


def slab_depth_at(lon):
    a, b, n = slab_fit()
    return a + b * x_km(lon)


def numbers():
    n = {}
    vs = list(volcanoes())
    sub = [v for v in vs if v[2].startswith("Subduction zone")]
    n["n_volcanoes"], n["n_subduction"] = len(vs), len(sub)
    n["frac_subduction"] = len(sub) / len(vs)
    q = list(jp_quakes())
    n["jp_n_events"] = len(q)
    n["jp_n_deeper_70"] = sum(1 for e in q if e[2] >= 70)
    n["jp_n_volcanoes"] = len(jp_volcanoes())
    a, b, k = slab_fit()
    n["jp_fit_n"] = k
    n["jp_fit_slope_km_per_km"] = -b
    n["jp_dip_deg"] = math.degrees(math.atan(-b))
    lf = front_lon()
    n["jp_front_lon"] = lf
    n["jp_slab_depth_front"] = slab_depth_at(lf)
    n["jp_front_x_km"] = x_km(lf)
    n["km_per_deg_lon"] = KM_PER_DEG_LON
    lt = trench_lon()
    n["jp_trench_lon"] = lt
    n["jp_front_trench_km"] = (lt - lf) * KM_PER_DEG_LON
    n["jp_H_geom"] = n["jp_front_trench_km"] * math.tan(math.radians(n["jp_dip_deg"]))
    for c, k, med in bins():
        n["bin_%g_median" % c] = med
        n["bin_%g_n" % c] = k
    # melting
    n["dry_T_3gpa"] = gs.t_solidus(3.0)
    n["dry_T_5gpa"] = gs.t_solidus(5.0)
    n["wet_mid_3gpa"] = 975.0
    n["dry_minus_wet_3gpa"] = gs.t_solidus(3.0) - 975.0
    n["dry_minus_wet_5gpa"] = gs.t_solidus(5.0) - 1000.0
    n["z_3gpa_km"] = depth_at_pressure(3.0)
    n["z_5gpa_km"] = depth_at_pressure(5.0)
    n["P_105km_gpa"] = gs.pressure_gpa(SYRACUSE_MEAN_H)
    n["dry_T_105km"] = gs.t_solidus(gs.pressure_gpa(SYRACUSE_MEAN_H))
    n["P_100km_gpa"] = gs.pressure_gpa(100.0)
    n["dry_T_100km"] = gs.t_solidus(gs.pressure_gpa(100.0))
    return n


def depth_at_pressure(p_gpa):
    lo, hi = 0.0, 400.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if gs.pressure_gpa(mid) < p_gpa:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


if __name__ == "__main__":
    vs = list(volcanoes())
    write_table(__file__, ("lon", "lat"), [(lo, la) for lo, la, s, nm in vs if s.startswith("Subduction zone")],
                part="world-sub")
    write_table(__file__, ("lon", "lat"), [(lo, la) for lo, la, s, nm in vs if not s.startswith("Subduction zone")],
                part="world-other")
    write_table(__file__, ("x_km", "depth", "mag"), [(x_km(lo), d, m) for lo, la, d, m in jp_quakes()],
                part="jp-quakes", digits=5)
    write_table(__file__, ("x_km",), [(x_km(lo),) for lo, la, nm in jp_volcanoes()], part="jp-volc", digits=5)
    a, b, k = slab_fit()
    # the fitted line inside the section box: from x = 0 (depth a) up to the surface
    write_table(__file__, ("x_km", "depth"), [(0.0, a), (-a / b, 0.0)], part="jp-slab", digits=5)
    write_table(__file__, ("lon", "n", "median_depth"), bins(), part="jp-bins", digits=5)
    write_table(__file__, ("depth_km", "P_GPa", "T_dry"),
                [(z, gs.pressure_gpa(z), gs.t_solidus(gs.pressure_gpa(z))) for z in range(0, 251, 5)],
                part="solidus", digits=5)
    write_table(__file__, ("P_GPa", "depth_km", "T_lo", "T_hi", "T_mid"),
                [(p, depth_at_pressure(p), lo, hi, 0.5 * (lo + hi)) for p, lo, hi in WET], part="wet", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=5)
