"""The Sun's daily path across the sky at latitude 45 deg N (Year 1,
spherical-astronomy): altitude against azimuth at the June solstice
(delta = +23.44 deg), the equinoxes (0) and the December solstice (-23.44 deg),
from sin h = sin phi sin delta + cos phi cos delta cos H (ch. 1). Obliquity
from the ledger (earth:obliquity). Only the part above the horizon is written.

  part june | equinox | december   az_deg alt_deg   one point per 5 min of H
  part noon                         case alt_deg    noon altitudes
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402
import _solar as S  # noqa: E402

LAT = 45.0
CASES = {"june": 23.44, "equinox": 0.0, "december": -23.44}


def path(dec_deg, lat_deg=LAT, step_min=5):
    phi, dec = math.radians(lat_deg), math.radians(dec_deg)
    rows = []
    for k in range(-144, 145):
        H = math.radians(k * step_min / 4.0)
        h = S.altitude(phi, dec, H)
        if h >= 0:
            rows.append((math.degrees(S.azimuth(phi, dec, H)), math.degrees(h)))
    return rows


def noon_altitude(dec_deg, lat_deg=LAT):
    return math.degrees(S.altitude(math.radians(lat_deg), math.radians(dec_deg), 0.0))


if __name__ == "__main__":
    for name, d in CASES.items():
        write_table(__file__, ("az_deg", "alt_deg"), path(d), part=name, digits=5)
    write_table(__file__, ("case", "alt_deg"),
                [(n, noon_altitude(d)) for n, d in CASES.items()], part="noon", digits=4)
