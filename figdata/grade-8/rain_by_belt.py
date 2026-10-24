"""Four towns, four belts of the global circulation (grade 8, chapter 2).

Re-reads the four NOAA 1991-2020 normals stations of grade 5 (ledger
data:b1-noaa-normals, via figdata/grade-5/climate_charts.py and
climate_zones.py) and places each one's yearly precipitation against its
latitude, with the belts of the global circulation of the chapter (about
0-30, 30-60 and 60-90 degrees north; ledger mo:three-cells).

  part stations : lat total_mm name belt
  part belts    : lat_min lat_max label
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "grade-5"))
from _table import write_table  # noqa: E402
import climate_charts as cc  # noqa: E402
import climate_zones as cz  # noqa: E402

BELTS = [(0, 30, "trade winds"), (30, 60, "westerlies"), (60, 90, "polar easterlies")]


def belt(lat):
    for lo, hi, name in BELTS:
        if lo <= abs(lat) < hi:
            return name
    return BELTS[-1][2]


def stations():
    """(lat, yearly precipitation in mm, name, belt), from the equator up."""
    out = []
    for name, lat, _lon in cz.STATIONS:
        total = cc.summary(name.lower())["total_mm"]
        out.append((lat, total, name, belt(lat)))
    return sorted(out)


if __name__ == "__main__":
    st = stations()
    write_table(__file__, ("lat", "total_mm", "name", "belt"),
                [(round(a, 2), round(t), n, b.replace(" ", "~")) for a, t, n, b in st], part="stations")
    write_table(__file__, ("lat_min", "lat_max", "label"), [(a, b, n.replace(" ", "~")) for a, b, n in BELTS], part="belts")
    for row in st:
        print(row)
