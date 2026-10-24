"""The physical map of the world (grade 4, world-physical-map).

* A raster of altitude and depth bands from ETOPO1 sampled at 1 degree
  (data/derived/etopo-1deg.csv, ledger data:etopo1), written as a 360 x 180
  PNG (one pixel per degree, north up, 180 W on the left) in the book's
  hypsometric colours (styles/oneearth.sty, omHypsLandA-F and omHypsSeaA-D).
* The great rivers and lakes of Natural Earth 1:110m
  (data/derived/grade-4-ne-rivers.csv, grade-4-ne-lakes.csv; ledger
  data:b1-ne-rivers) as line and polygon tables.
* Africa's area, summed over the 1-degree land cells inside a hand-drawn
  outline of the continent (AFRICA, MADAGASCAR), and the Sahara's share of it
  from the Sahara's area (ledger natgeo:sahara).

  physical_map.png       : the raster
  part rivers            : lon lat (blank line between rivers)
  part lakes             : lon lat (blank line between lakes)
  part bands             : band, lower_m, upper_m, colour (the legend)
  main table             : quantity, value
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
R_EARTH_KM = 6371.0
SAHARA_MKM2 = 8.5            # ledger natgeo:sahara

# (upper limit in m, colour) from the deepest to the highest; the land bands
# start at sea level (0 m).
SEA = [(-4000, "5A9CCF"), (-2000, "84BCE0"), (-200, "B3D8EE"), (0, "DCEEF8")]
LAND = [(200, "9CC98A"), (500, "C9DE99"), (1000, "F1E7A8"), (2000, "E5C58A"),
        (4000, "C79E76"), (None, "ECE8E3")]

AFRICA = [(-6.5, 35.9), (-1.0, 35.9), (3.0, 36.9), (9.0, 37.4), (11.2, 37.4),
          (11.2, 35.0), (20.0, 33.0), (25.0, 32.2), (32.5, 31.6), (32.5, 29.8),
          (35.5, 24.0), (38.5, 18.0), (43.3, 12.6), (51.5, 12.2), (51.5, 10.0),
          (49.0, 5.0), (43.0, -1.0), (41.0, -4.0), (40.5, -10.5), (41.0, -15.0),
          (39.0, -18.0), (36.0, -22.0), (36.0, -25.5), (33.5, -27.0), (32.0, -29.5),
          (28.0, -34.0), (20.0, -35.5), (17.0, -33.0), (15.0, -27.0), (11.5, -18.0),
          (11.5, -12.0), (8.0, -1.5), (9.0, 4.0), (4.0, 5.5), (-1.0, 4.3),
          (-8.0, 4.0), (-13.0, 7.0), (-17.5, 14.5), (-18.0, 21.0), (-14.0, 27.0),
          (-10.5, 30.0), (-10.0, 33.0)]
MADAGASCAR = [(43.0, -25.8), (47.8, -25.8), (51.0, -15.5), (49.8, -11.5),
              (43.5, -16.0)]


def etopo():
    with open(os.path.join(ROOT, "data", "derived", "etopo-1deg.csv"), encoding="utf8") as f:
        return [(float(r["lat"]), float(r["lon"]), float(r["elev_m"])) for r in csv.DictReader(f)]


def colour(z):
    if z < 0:
        for top, c in SEA:
            if z < top:
                return c
        return SEA[-1][1]
    for top, c in LAND:
        if top is None or z < top:
            return c


def band_rows():
    rows, low = [], None
    for top, c in SEA:
        rows.append(("sea", "-inf" if low is None else low, top, c))
        low = top
    low = 0
    for top, c in LAND:
        rows.append(("land", low, "inf" if top is None else top, c))
        low = top
    return rows


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


def raster(cells):
    grid = {(la, lo): z for la, lo, z in cells}
    rows = []
    for j in range(180):
        lat = 89.5 - j
        row = []
        for i in range(360):
            c = colour(grid[(lat, -179.5 + i)])
            row += [int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)]
        rows.append(row)
    return rows


def inside(poly, x, y):
    c = False
    for (x0, y0), (x1, y1) in zip(poly, poly[1:] + poly[:1]):
        if (y0 > y) != (y1 > y) and x < x0 + (y - y0) * (x1 - x0) / (y1 - y0):
            c = not c
    return c


def cell_area_km2(lat, step=1.0):
    """Area of a step x step degree cell centred on latitude lat."""
    a = math.radians(lat - step / 2)
    b = math.radians(lat + step / 2)
    return R_EARTH_KM ** 2 * math.radians(step) * (math.sin(b) - math.sin(a))


def africa_area_mkm2(cells):
    s = 0.0
    for lat, lon, z in cells:
        if z >= 0 and (inside(AFRICA, lon, lat) or inside(MADAGASCAR, lon, lat)):
            s += cell_area_km2(lat)
    return s / 1e6


def lines(name):
    out = {}
    with open(os.path.join(ROOT, "data", "derived", name + ".csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            out.setdefault((r["name"], r["ring"]), []).append((float(r["lon"]), float(r["lat"])))
    return out


def rows_with_jumps(polys):
    rows = []
    for pts in polys:
        if rows:
            rows.append(())
        rows += [(round(x, 3), round(y, 3)) for x, y in pts]
    return rows


if __name__ == "__main__":
    cells = etopo()
    png(out_path(__file__, ext=".png"), 360, 180, raster(cells))
    write_table(__file__, ("lon", "lat"), rows_with_jumps(lines("grade-4-ne-rivers").values()),
                part="rivers")
    write_table(__file__, ("lon", "lat"), rows_with_jumps(lines("grade-4-ne-lakes").values()),
                part="lakes")
    write_table(__file__, ("kind", "lower_m", "upper_m", "colour"), band_rows(), part="bands")
    a = africa_area_mkm2(cells)
    write_table(__file__, ("quantity", "value"),
                [("africa_area_Mkm2", round(a, 2)), ("sahara_area_Mkm2", SAHARA_MKM2),
                 ("sahara_share", round(SAHARA_MKM2 / a, 3))])
    print(a, SAHARA_MKM2 / a)
