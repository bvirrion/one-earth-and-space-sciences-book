"""Zonal-mean circulation of the atmosphere from the NCEP-NCAR Reanalysis 1 (Year 1,
atmospheric-circulation).

Source (ledger data:b3-ncep-circ, data:b3-ncep): long-term monthly means 1991-2020,
zonal means derived by tools/fetch_data.py: zonal and meridional wind on the 12
pressure levels 1000-100 hPa and the zonal wind at sigma 0.995 (2.5-degree grid), the
sea-level pressure, and the precipitation rate (Gaussian grid, monthly zonal means).
Mean radius 6371 km (earth:Rmean), g = 9.80665 m/s2.

The mean meridional mass streamfunction (the Hadley, Ferrel and polar cells) is

    psi(p, phi) = (2 pi a cos(phi) / g) * integral from 0 to p of [v] dp',

in kg/s, integrated downwards from the top with the trapezium rule, the top level
(100 hPa; the file is cut there) taken to carry its own [v] between 0 and 100 hPa. Positive psi is a
clockwise circulation when the North Pole is on the right (rising near the equator,
northward aloft).

  part u200-<season>  lat u          (zonal-mean zonal wind at 200 hPa; ann, djf, jja)
  part usfc-<season>  lat u          (at sigma 0.995)
  part slp-<season>   lat slp        (hPa)
  part psi-<season>   lat p psi      (1e10 kg/s, grid for a colour plot; p in hPa)
  part psi0-<season>  lat p          (zero line of psi, from marching squares, |lat| <= 80)
  part itcz           month lat      (latitude of the zonal-mean precipitation maximum
                                      between 20 S and 20 N, month by month)
  part values         what value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DERIVED = os.path.join(ROOT, "data", "derived")
A = 6371.0e3
G = 9.80665
DAYS = (31, 28.25, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
SEASONS = {"ann": tuple(range(1, 13)), "djf": (12, 1, 2), "jja": (6, 7, 8)}


def _read(name):
    with open(os.path.join(DERIVED, "bachelor-1-ncep-%s.csv" % name), encoding="utf8") as f:
        return list(csv.DictReader(f))


def _season_mean(rows, months, keys):
    """Mean over the months (weighted by their length) of rows keyed by `keys`."""
    acc, wt = {}, {}
    for r in rows:
        m = int(r["month"])
        if m not in months:
            continue
        k = tuple(float(r[x]) for x in keys)
        acc[k] = acc.get(k, 0.0) + DAYS[m - 1] * float(r["value"])
        wt[k] = wt.get(k, 0.0) + DAYS[m - 1]
    return {k: acc[k] / wt[k] for k in acc}


def profile(name, season):
    """[(lat, value)] south to north for a single-level field."""
    d = _season_mean(_read(name), SEASONS[season], ("lat",))
    return sorted((k[0], v) for k, v in d.items())


def level_field(name, season):
    """{(level, lat): value} for a pressure-level field."""
    return _season_mean(_read(name), SEASONS[season], ("level", "lat"))


def levels_lats(field):
    levs = sorted({k[0] for k in field})
    lats = sorted({k[1] for k in field})
    return levs, lats


def streamfunction(season):
    """{(p hPa, lat): psi in kg/s}, integrated from the top down."""
    v = level_field("vwnd-p", season)
    levs, lats = levels_lats(v)
    out = {}
    for la in lats:
        c = 2 * math.pi * A * math.cos(math.radians(la)) / G
        acc = v[(levs[0], la)] * levs[0] * 100.0        # 0 to the top level
        out[(levs[0], la)] = c * acc
        for p1, p2 in zip(levs, levs[1:]):
            acc += 0.5 * (v[(p1, la)] + v[(p2, la)]) * (p2 - p1) * 100.0
            out[(p2, la)] = c * acc
    return out


def zero_lines(field, levs, lats):
    """Segments of the zero contour of field[(lev, lat)] by marching squares on the
    (lat, lev) grid; returned as a list of polylines [(lat, lev), ...]."""
    segs = []
    for i in range(len(lats) - 1):
        for j in range(len(levs) - 1):
            corners = [(lats[i], levs[j]), (lats[i + 1], levs[j]), (lats[i + 1], levs[j + 1]),
                       (lats[i], levs[j + 1])]
            vals = [field[(c[1], c[0])] for c in corners]
            pts = []
            for k in range(4):
                (x1, y1), (x2, y2) = corners[k], corners[(k + 1) % 4]
                v1, v2 = vals[k], vals[(k + 1) % 4]
                if (v1 < 0) != (v2 < 0):
                    t = v1 / (v1 - v2)
                    pts.append((x1 + t * (x2 - x1), y1 + t * (y2 - y1)))
            if len(pts) == 2:
                segs.append(pts)
            elif len(pts) == 4:                       # saddle: pair by the centre value
                segs.append([pts[0], pts[1]])
                segs.append([pts[2], pts[3]])
    return segs


def cell_edges(season, level=500.0):
    """Latitudes where psi at `level` changes sign, south to north."""
    psi = streamfunction(season)
    levs, lats = levels_lats({(k[0], k[1]): 0 for k in psi})
    out = []
    for a, b in zip(lats, lats[1:]):
        pa, pb = psi[(level, a)], psi[(level, b)]
        if pa == 0 or (pa < 0) != (pb < 0):
            out.append(a + (b - a) * pa / (pa - pb))
    return out


def extreme(season, lat_lo, lat_hi, sign):
    """(value, p, lat) of the largest psi of the given sign in a latitude range."""
    psi = streamfunction(season)
    pts = [(v * sign, k[0], k[1]) for k, v in psi.items() if lat_lo <= k[1] <= lat_hi]
    v, p, la = max(pts)
    return v * sign, p, la


def jet(season, lat_lo, lat_hi, level=200.0):
    """(u max, lat) of the zonal-mean zonal wind at `level` in a latitude range."""
    u = level_field("uwnd-p", season)
    pts = [(v, k[1]) for k, v in u.items() if k[0] == level and lat_lo <= k[1] <= lat_hi]
    return max(pts)


def itcz():
    """[(month, latitude of the zonal-mean precipitation maximum within 20 S - 20 N)],
    refined by a parabola through the maximum and its neighbours."""
    rows = _read("prate-monthly")
    out = []
    for m in range(1, 13):
        pr = sorted((float(r["lat"]), float(r["value"])) for r in rows if int(r["month"]) == m)
        idx = [i for i, (la, _) in enumerate(pr) if -20 <= la <= 20]
        i = max(idx, key=lambda k: pr[k][1])
        (x0, y0), (x1, y1), (x2, y2) = pr[i - 1], pr[i], pr[i + 1]
        den = (y0 - 2 * y1 + y2)
        dx = 0.5 * (y0 - y2) / den if den != 0 else 0.0
        out.append((m, x1 + dx * (x2 - x0) / 2))
    return out


def values():
    v = []
    for s in SEASONS:
        e = cell_edges(s)
        v += [("edges500_%s_%d" % (s, i), x) for i, x in enumerate(e)]
        hn = extreme(s, 0, 40, +1) if s != "jja" else extreme(s, -40, 20, -1)
        v += [("hadley_main_%s" % s, hn[0] / 1e10), ("hadley_main_p_%s" % s, hn[1]),
              ("hadley_main_lat_%s" % s, hn[2])]
        for name, lo, hi in (("N", 15, 50), ("S", -50, -15)):
            u, la = jet(s, lo, hi)
            v += [("jet%s_%s" % (name, s), u), ("jet%s_lat_%s" % (name, s), la)]
    na = extreme("ann", -10, 40, +1)
    sa = extreme("ann", -40, 10, -1)
    v += [("hadleyN_ann", na[0] / 1e10), ("hadleyN_ann_lat", na[2]), ("hadleyN_ann_p", na[1]),
          ("hadleyS_ann", sa[0] / 1e10), ("hadleyS_ann_lat", sa[2]), ("hadleyS_ann_p", sa[1])]
    for s in SEASONS:
        us = profile("uwnd-sfc", s)
        sl = profile("slp", s)
        for target in (-60.0, -45.0, -30.0, -15.0, 0.0, 15.0, 30.0, 45.0, 60.0):
            j = min(range(len(us)), key=lambda i: abs(us[i][0] - target))
            v += [("usfc_%s_%g" % (s, target), us[j][1]), ("slp_%s_%g" % (s, target), sl[j][1])]
    sl = profile("slp", "ann")
    nh = max((x for x in sl if 15 <= x[0] <= 45), key=lambda x: x[1])
    sh = max((x for x in sl if -45 <= x[0] <= -15), key=lambda x: x[1])
    v += [("slp_maxN_lat", nh[0]), ("slp_maxN", nh[1]), ("slp_maxS_lat", sh[0]),
          ("slp_maxS", sh[1])]
    it = itcz()
    v += [("itcz_%d" % m, la) for m, la in it]
    v += [("itcz_max", max(la for _, la in it)), ("itcz_min", min(la for _, la in it))]
    return v


if __name__ == "__main__":
    for s in SEASONS:
        u = level_field("uwnd-p", s)
        write_table(__file__, ("lat", "u"), sorted((k[1], val) for k, val in u.items() if k[0] == 200.0),
                    part="u200-" + s)
        write_table(__file__, ("lat", "u"), profile("uwnd-sfc", s), part="usfc-" + s)
        write_table(__file__, ("lat", "slp"), profile("slp", s),
                    part="slp-" + s)
        psi = streamfunction(s)
        levs, lats = levels_lats(psi)
        keep = [p for p in levs if p >= 100.0]
        # rows: for each level (top to bottom), every latitude (south to north)
        write_table(__file__, ("lat", "p", "psi"),
                    [(la, p, psi[(p, la)] / 1e10) for p in keep for la in lats], part="psi-" + s)
        sub = {k: val for k, val in psi.items() if k[0] >= 100.0}
        rows = []
        for seg in zero_lines(sub, keep, lats):
            # near the poles psi is ~0 and its sign is noise: keep the zero lines within 80 deg
            if all(abs(pt[0]) <= 80.0 for pt in seg):
                rows += [seg[0], seg[1], (float("nan"), float("nan"))]
        write_table(__file__, ("lat", "p"), rows, part="psi0-" + s)
    write_table(__file__, ("month", "lat"), itcz(), part="itcz")
    write_table(__file__, ("what", "value"), values(), part="values", digits=7)
