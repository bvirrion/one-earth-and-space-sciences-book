"""The 24 ideal time zones (grade 6, latitude-longitude).

The Earth turns 360 degrees in 24 hours (ledger planet:Earth.day), so 15
degrees of longitude per hour (rmg:15deg-per-hour). An ideal zone is a band 15
degrees wide centred on a multiple of 15 degrees; its offset from the time at
Greenwich is longitude / 15 rounded to the nearest whole hour. The zone that
straddles 180 degrees is split by the date line: +12 on the west side
(172.5 E to 180), -12 on the east side (180 to 172.5 W). Real zones follow
borders (told in the text, not drawn).

  part bands  : lon_min lon_max offset parity   (25 bands, west to east)
  part labels : lon y offset_label  (one label per band; the half zones +-12 one row higher)
  part odd    : lon lat  closed rectangles of the odd-offset bands (for shading)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

DAY_H = 24.0      # ledger planet:Earth.day


def degrees_per_hour():
    return 360.0 / DAY_H


def offset(lon):
    """Ideal-zone offset (hours ahead of Greenwich) of a longitude in degrees."""
    if not -180.0 <= lon <= 180.0:
        raise ValueError(lon)
    h = lon / degrees_per_hour()
    return int(h + 0.5) if h >= 0 else -int(-h + 0.5)


def local_time(hour_greenwich, lon):
    """(hour 0-23, day shift -1/0/+1) at a longitude when it is hour_greenwich at Greenwich."""
    t = hour_greenwich + offset(lon)
    return t % 24, (t // 24)


def bands():
    out = [(-180.0, -172.5, -12)]
    for k in range(-11, 12):
        out.append((15.0 * k - 7.5, 15.0 * k + 7.5, k))
    out.append((172.5, 180.0, 12))
    return out


if __name__ == "__main__":
    write_table(__file__, ("lon_min", "lon_max", "offset", "parity"),
                [(a, b, o, abs(o) % 2) for a, b, o in bands()], part="bands")
    lab = []
    for a, b, o in bands():
        lab.append(((a + b) / 2, ("$+%d$" % o) if o > 0 else ("$%d$" % o if o < 0 else "$0$")))
    write_table(__file__, ("lon", "y", "label"), [(lo, 99 if abs(o) == 12 else 90, l)
                                                  for (lo, l), (_, _, o) in zip(lab, bands())], part="labels")
    poly = []
    for a, b, o in bands():
        if abs(o) % 2:
            poly += ([()] if poly else []) + [(a, -90), (b, -90), (b, 90), (a, 90), (a, -90)]
    write_table(__file__, ("lon", "lat"), poly, part="odd")
