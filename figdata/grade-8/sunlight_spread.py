"""How far a beam of sunlight spreads on the ground at noon on an equinox
(grade 8, chapter 2): the Sun is overhead at the equator, and at latitude L
its rays arrive at the angle L from the vertical, so the same beam covers
1 / cos(L) times the area it covers at the equator (pure geometry).

  main table : lat spread share   (spread = area factor; share = energy per
                                   square metre as a percentage of the equator's)
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

LATS = (0, 30, 45, 60, 75)


def spread(lat_deg):
    return 1.0 / math.cos(math.radians(lat_deg))


def share(lat_deg):
    return 100.0 / spread(lat_deg)


if __name__ == "__main__":
    write_table(__file__, ("lat", "spread", "share"), [(lat, round(spread(lat), 2), round(share(lat))) for lat in LATS])
