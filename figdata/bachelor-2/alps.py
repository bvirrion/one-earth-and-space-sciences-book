"""The Alps (Year 2, alpine-orogen): relief map, a profile with the Moho, and the
arithmetic of balanced sections.

  relief    ETOPO1 every 3rd node (0.05 degree) over 43.5-48.5 N, 5-14 E
            (data/derived/bachelor-2-etopo-alps.csv; ledger data:b4-etopo-alps). Contours at
            0, 1000 and 2000 m traced by marching squares (figdata/shared/region.py) and
            simplified (Douglas-Peucker); loops of fewer than MIN_PTS points dropped.
  profile   a swath 0.25 degree either side of the 8 E meridian, 45.3-48.0 N: mean and
            maximum elevation of the nodes at each latitude; distance in km from 45.3 N
            (111.19 km per degree of latitude).
  moho      the Moho depth picks of Michailos et al. (2023) on the 8 E meridian
            (data/derived/bachelor-2-alps-moho.csv; ledger data:b4-alps-moho), and the Airy
            root of the swath-mean relief, r = h rho_c / (rho_m - rho_c), with the densities
            of the Year-1 isostasy chapter (2700 and 3300 kg/m3) under a reference crust
            REF_KM = 30 km thick (the typical continental value of Michailos et al. 2023,
            ledger michailos23:moho). Root areas: the trapezoid integral, over the stretch
            where picks exist, of the observed root (picks interpolated, minus REF_KM, floored
            at 0) and of the Airy root.
  balance   line-length and area balance (book's own model section, labelled as such):
            bed length of segments (dx, dip), shortening e = 1 - l/l0, area balance
            l0 = A/t, depth to the decollement from the excess area d = Ae/S.

  part c0, c1000, c2000   lon lat (blank line between polylines)
  part swath              lat km mean_m max_m
  part moho               lat km moho_km
  part airy               lat km airy_km
  part chevron            x_km y_km   deformed marker bed of the balanced-section figure
  part chevron0           x_km y_km   the same bed restored
  part numbers            key value
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")
KM_PER_DEG = 111.19
LON0, HALF = 8.0, 0.25
LAT0, LAT1 = 45.3, 48.0
RHO_C, RHO_M = 2700.0, 3300.0
MIN_PTS = 12
REF_KM = 30.0


def grid():
    """lats (ascending), lons (ascending), Z (ny x nx, m)."""
    with open(os.path.join(DERIVED, "bachelor-2-etopo-alps.csv"), encoding="utf8") as f:
        rows = [(float(r["lat"]), float(r["lon"]), float(r["elev_m"])) for r in csv.DictReader(f)]
    lat = np.array([r[0] for r in rows])
    lon = np.array([r[1] for r in rows])
    z = np.array([r[2] for r in rows])
    lats, lons = np.unique(lat), np.unique(lon)
    zz = np.full((len(lats), len(lons)), np.nan)
    zz[np.searchsorted(lats, lat), np.searchsorted(lons, lon)] = z
    return lats, lons, zz


def contours(level, tol=0.012):
    import region
    lats, lons, zz = grid()
    out = []
    for line in region.trace(zz, lons, lats, level=level):
        if len(line) < MIN_PTS:
            continue
        out.append(region.simplify(line, tol))
    return out


def km(lat):
    return (lat - LAT0) * KM_PER_DEG


def swath():
    """(lat, km, mean, max) on the 8 E swath, 45.3-48.0 N."""
    lats, lons, zz = grid()
    sel = (lons >= LON0 - HALF - 1e-9) & (lons <= LON0 + HALF + 1e-9)
    out = []
    for j, la in enumerate(lats):
        if LAT0 - 1e-9 <= la <= LAT1 + 1e-9:
            row = zz[j, sel]
            out.append((round(float(la), 3), km(la), float(row.mean()), float(row.max())))
    return out


def moho_picks(lon0=LON0):
    with open(os.path.join(DERIVED, "bachelor-2-alps-moho.csv"), encoding="utf8") as f:
        rows = [(float(r["lon"]), float(r["lat"]), float(r["moho_km"])) for r in csv.DictReader(f)]
    return sorted((la, z) for lo, la, z in rows if abs(lo - lon0) < 1e-6)


def moho_profile():
    return [(la, km(la), z) for la, z in moho_picks() if LAT0 <= la <= LAT1]


def ref_crust():
    return REF_KM


def airy_root(h_m):
    """root (km) under relief h (m): r = h rho_c / (rho_m - rho_c)."""
    return max(h_m, 0.0) * RHO_C / (RHO_M - RHO_C) / 1000.0


def airy_profile():
    ref = ref_crust()
    return [(la, k, ref + airy_root(m)) for la, k, m, _ in swath()]


# --- balanced sections -------------------------------------------------------
def bed_length(segments):
    """segments: (dx_km, dip_deg); length along the bed."""
    return sum(dx / math.cos(math.radians(d)) for dx, d in segments)


def shortening(l, l0):
    """e = 1 - l/l0 (fraction)."""
    return 1.0 - l / l0


def restored_length_area(area_km2, thickness_km):
    return area_km2 / thickness_km


def decollement_depth(excess_area_km2, shortening_km):
    return excess_area_km2 / shortening_km


def chevron(l0=30.0, dip=40.0, n=6, y0=0.0):
    """a marker bed folded into n equal chevron limbs of the given dip, starting at the
    pin line x=0; returns the deformed polyline and its horizontal length."""
    limb = l0 / n
    dx, dy = limb * math.cos(math.radians(dip)), limb * math.sin(math.radians(dip))
    pts, x, y = [(0.0, y0)], 0.0, y0
    for i in range(n):
        x += dx
        y += dy if i % 2 == 0 else -dy
        pts.append((x, y))
    return pts, x


def root_areas():
    """(observed, Airy) root cross-sections (km2) between the first and last pick."""
    sw = swath()
    mp = moho_profile()
    k = np.array([r[1] for r in sw])
    h = np.array([r[2] for r in sw])
    mk = np.array([r[1] for r in mp])
    mz = np.array([r[2] for r in mp])
    sel = (k >= mk.min()) & (k <= mk.max())
    obs = np.clip(np.interp(k[sel], mk, mz) - REF_KM, 0.0, None)
    airy = np.array([airy_root(x) for x in h[sel]])
    return float(np.trapezoid(obs, k[sel])), float(np.trapezoid(airy, k[sel]))


def numbers():
    lats, lons, zz = grid()
    j, i = np.unravel_index(np.nanargmax(zz), zz.shape)
    sw = swath()
    top = max(sw, key=lambda r: r[2])
    mp = moho_profile()
    deep = max(mp, key=lambda r: r[2])
    ref = ref_crust()
    ap = airy_profile()
    adeep = max(ap, key=lambda r: r[2])
    _, xc = chevron()
    return {
        "max_node_m": float(zz[j, i]), "max_node_lat": float(lats[j]), "max_node_lon": float(lons[i]),
        "swath_top_mean_m": top[2], "swath_top_lat": top[0],
        "moho_deep_km": deep[2], "moho_deep_lat": deep[0],
        "ref_crust_km": ref, "airy_deep_km": adeep[2], "airy_deep_lat": adeep[0],
        "root_obs_km": deep[2] - ref, "root_airy_km": adeep[2] - ref,
        "chevron_present_km": xc, "chevron_e": shortening(xc, 30.0),
        "n_moho_8E": len(mp),
        "root_area_obs_km2": root_areas()[0], "root_area_airy_km2": root_areas()[1],
        "moho_at_top_km": [z for la, k, z in mp if abs(la - 46.486) < 0.01][0],
    }


def _lines(polylines):
    rows = []
    for k, line in enumerate(polylines):
        if k:
            rows.append(())
        rows.extend((round(x, 3), round(y, 3)) for x, y in line)
    return rows


if __name__ == "__main__":
    for lev in (0, 1000, 2000):
        write_table(__file__, ("lon", "lat"), _lines(contours(lev)), part="c%d" % lev)
    write_table(__file__, ("lat", "km", "mean_m", "max_m"),
                [(la, round(k, 2), round(m, 1), round(x, 1)) for la, k, m, x in swath()], part="swath")
    write_table(__file__, ("lat", "km", "moho_km"),
                [(round(la, 3), round(k, 2), round(z, 2)) for la, k, z in moho_profile()], part="moho")
    write_table(__file__, ("lat", "km", "airy_km"),
                [(la, round(k, 2), round(z, 2)) for la, k, z in airy_profile()], part="airy")
    pts, _ = chevron(y0=0.0)
    write_table(__file__, ("x_km", "y_km"), [(round(x, 3), round(y, 3)) for x, y in pts], part="chevron")
    write_table(__file__, ("x_km", "y_km"), [(0.0, -6.0), (30.0, -6.0)], part="chevron0")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")
