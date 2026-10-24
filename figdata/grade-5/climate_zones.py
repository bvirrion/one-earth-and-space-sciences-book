"""The hot, temperate and cold zones on a world map (grade 5).

The zones are bounded by the tropics and the polar circles, whose latitudes
follow from the tilt of the Earth's axis (ledger earth:obliquity, 23.44 deg):
the tropics lie at +-obliquity, the polar circles at +-(90 - obliquity).
Equirectangular, as the `ommap` axis.

  part bands    : zone lat_min lat_max (one row per band, north to south)
  part lines    : lon lat of the four circles (blank line between them)
  part hot, temperate, cold : the bands as closed rectangles (for fills)
  part stations : lon lat name zone  (the four climate-chart stations)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

OBLIQUITY = 23.44   # deg; ledger earth:obliquity (shared data ledger)

# lat, lon of the stations as printed in the NOAA normals files (STATION,
# LATITUDE, LONGITUDE columns; ledger data:b1-noaa-normals)
STATIONS = [
    ("Phoenix", 33.4278, -112.0039),     # USW00023183
    ("Hilo", 19.7192, -155.0531),        # USW00021504
    ("Seattle", 47.4444, -122.3139),     # USW00024233
    ("Utqiagvik", 71.2833, -156.7814),   # USW00027502
]


def tropic():
    return OBLIQUITY


def polar_circle():
    return 90.0 - OBLIQUITY


def zone(lat):
    a = abs(lat)
    if a < tropic():
        return "hot"
    if a < polar_circle():
        return "temperate"
    return "cold"


def bands():
    t, p = tropic(), polar_circle()
    return [("cold", p, 90.0), ("temperate", t, p), ("hot", -t, t),
            ("temperate", -p, -t), ("cold", -90.0, -p)]


def area_share(lat_min, lat_max):
    """Fraction of the Earth's surface between two latitudes (sphere)."""
    import math
    return (math.sin(math.radians(lat_max)) - math.sin(math.radians(lat_min))) / 2.0


if __name__ == "__main__":
    write_table(__file__, ("zone", "lat_min", "lat_max"),
                [(z, "%.2f" % a, "%.2f" % b) for z, a, b in bands()], part="bands")
    lines = []
    for lat in (polar_circle(), tropic(), -tropic(), -polar_circle()):
        if lines:
            lines.append(())
        lines += [(lon, "%.2f" % lat) for lon in (-180, 180)]
    write_table(__file__, ("lon", "lat"), lines, part="lines")
    for name in ("hot", "temperate", "cold"):      # closed rectangles, one per band
        poly = []
        for z, a, b in bands():
            if z == name:
                if poly:
                    poly.append(())
                poly += [(-180, "%.2f" % a), (180, "%.2f" % a), (180, "%.2f" % b),
                         (-180, "%.2f" % b), (-180, "%.2f" % a)]
        write_table(__file__, ("lon", "lat"), poly, part=name)
    write_table(__file__, ("lon", "lat", "name", "zone"),
                [("%.2f" % lo, "%.2f" % la, n, zone(la)) for n, la, lo in STATIONS],
                part="stations")
    for z, a, b in bands():
        print(z, a, b, round(area_share(a, b), 3))
