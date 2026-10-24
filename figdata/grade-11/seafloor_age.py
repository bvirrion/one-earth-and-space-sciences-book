"""The age of the ocean floor (grade 11, drift-to-spreading; reused in ocean-ridges).

Source (ledger data:b2-seafloor-age): Seton et al. (2020) age grid, version 2020.1,
reduced by tools/fetch_data.py to data/derived/grade-11-seafloor-age.csv (1-degree
cells, the median age of each cell's 6' nodes) and grade-11-seafloor-age-30s.csv
(every 6' node on the parallel 30 S).

Writes
  grade-11-seafloor_age.png        the map raster, one pixel per degree, north up,
                                   180 W on the left (cells with no ocean floor grey)
  grade-11-seafloor_age-bar.png    the colour bar, one pixel per 20-Myr band
  part profile   lon dist_km age   the South Atlantic along 30 S, distance east of
                                   the ridge axis (negative to the west)
  part numbers   key value
"""
import csv
import math
import os
import struct
import sys
import zlib

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import out_path, write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DERIVED = os.path.join(ROOT, "data", "derived")
EARTH_RADIUS_KM = 6371.0          # mean radius (ledger earth:Rmean)
KM_PER_DEG = math.pi * EARTH_RADIUS_KM / 180.0

# 20-Myr bands, young (red) to old (blue, then purple beyond 180 Myr)
BANDS = [(20, "B2182B"), (40, "E34A33"), (60, "FC8D59"), (80, "FDCC8A"), (100, "FFFFBF"),
         (120, "D9EF8B"), (140, "91CF60"), (160, "4FA3C7"), (180, "2C6FB2"), (None, "5E3C99")]
NO_OCEAN = "E4E4E4"
# the eastern Mediterranean: small basins whose floor is older than the open oceans'
MEDITERRANEAN = (-6.0, 37.0, 30.0, 46.0)     # lon min, lon max, lat min, lat max


def cells():
    with open(os.path.join(DERIVED, "grade-11-seafloor-age.csv"), encoding="utf8") as f:
        return [(float(r["lat"]), float(r["lon"]), float(r["age"])) for r in csv.DictReader(f)]


def in_mediterranean(lat, lon):
    lo0, lo1, la0, la1 = MEDITERRANEAN
    return lo0 <= lon <= lo1 and la0 <= lat <= la1


def colour(age):
    for top, c in BANDS:
        if top is None or age < top:
            return c


def png(path, width, height, rgb_rows):
    raw = b"".join(b"\x00" + bytes(row) for row in rgb_rows)

    def chunk(tag, data):
        return (struct.pack(">I", len(data)) + tag + data
                + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff))
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)))
        f.write(chunk(b"IDAT", zlib.compress(raw, 9)))
        f.write(chunk(b"IEND", b""))


def rgb(hexcode):
    return [int(hexcode[0:2], 16), int(hexcode[2:4], 16), int(hexcode[4:6], 16)]


def raster(cs):
    grid = {(la, lo): a for la, lo, a in cs}
    rows = []
    for j in range(180):
        lat = 89.5 - j
        row = []
        for i in range(360):
            a = grid.get((lat, -179.5 + i))
            row += rgb(NO_OCEAN if a is None else colour(a))
        rows.append(row)
    return rows


def profile_30s(lon_min=-60.0, lon_max=20.0):
    """South Atlantic nodes on 30 S: (lon, distance east of the ridge in km, age).
    The ridge axis is the youngest node; distances are measured along the parallel."""
    with open(os.path.join(DERIVED, "grade-11-seafloor-age-30s.csv"), encoding="utf8") as f:
        pts = [(float(r["lon"]), float(r["age"])) for r in csv.DictReader(f)]
    pts = [p for p in pts if lon_min < p[0] < lon_max]
    ridge = min(pts, key=lambda p: p[1])[0]
    k = KM_PER_DEG * math.cos(math.radians(30.0))
    return [(lo, (lo - ridge) * k, a) for lo, a in pts], ridge


def numbers():
    cs = cells()
    w = [math.cos(math.radians(la)) for la, _, _ in cs]
    mean = sum(wi * a for wi, (_, _, a) in zip(w, cs)) / sum(w)
    young = sum(wi for wi, (_, _, a) in zip(w, cs) if a < 100) / sum(w)
    open_cells = [c for c in cs if not in_mediterranean(c[0], c[1])]
    oldest = max(open_cells, key=lambda c: c[2])
    med = max((c for c in cs if in_mediterranean(c[0], c[1])), key=lambda c: c[2])
    area = sum(EARTH_RADIUS_KM ** 2 * math.radians(1.0)
               * (math.sin(math.radians(la + 0.5)) - math.sin(math.radians(la - 0.5))) for la, _, _ in cs)
    prof, ridge = profile_30s()
    east = max(prof, key=lambda p: p[0])
    west = min(prof, key=lambda p: p[0])
    return {"mean_age_myr": mean, "ocean_floor_area_km2": area, "share_younger_100": young,
            "oldest_open_myr": oldest[2], "oldest_open_lat": oldest[0], "oldest_open_lon": oldest[1],
            "oldest_mediterranean_myr": med[2],
            "ridge_lon_30s": ridge, "km_per_deg_30s": KM_PER_DEG * math.cos(math.radians(30.0)),
            "east_edge_lon_30s": east[0], "east_edge_km_30s": east[1], "east_edge_age_30s": east[2],
            "west_edge_lon_30s": west[0], "west_edge_km_30s": -west[1], "west_edge_age_30s": west[2]}


if __name__ == "__main__":
    png(out_path(__file__, ext=".png"), 360, 180, raster(cells()))
    png(out_path(__file__, part="bar", ext=".png"), len(BANDS), 1, [sum((rgb(c) for _, c in BANDS), [])])
    prof, _ = profile_30s()
    write_table(__file__, ("lon", "dist_km", "age"), prof[::2], part="profile", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")
