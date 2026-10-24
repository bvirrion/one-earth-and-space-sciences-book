"""Day length through the year at five latitudes, and the equation of time
(Year 1, spherical-astronomy). The Sun's declination comes from the Kepler
model of _solar.py (ledger values: eccentricity, obliquity, longitude of
perihelion, tropical year, the 2026 March equinox); the day length from
cos H0 = -tan phi tan delta (geometric rising of the Sun's centre, no
refraction).

  part lengths   day lat0 lat30 lat45 lat60 lat70   hours, every 2 days of 2026
  part eot       day eot_min dec_deg                every 2 days
  part extremes  what day value                     EoT extremes and zeros
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402
import _solar as S  # noqa: E402

LATS = (0, 30, 45, 60, 70)


def length(lat_deg, t):
    return S.day_length(math.radians(lat_deg), S.declination(t))


def eot_series(step=0.25):
    n = int(365 / step)
    return [(k * step, S.equation_of_time(k * step)) for k in range(n + 1)]


def eot_extremes():
    s = eot_series()
    mx = max(s, key=lambda r: r[1])
    mn = min(s, key=lambda r: r[1])
    zeros = [s[i][0] for i in range(1, len(s)) if (s[i - 1][1] > 0) != (s[i][1] > 0)]
    return mx, mn, zeros


if __name__ == "__main__":
    days = [d + 0.5 for d in range(0, 366, 2)]
    write_table(__file__, ("day",) + tuple("lat%d" % L for L in LATS),
                [(t,) + tuple(length(L, t) for L in LATS) for t in days], part="lengths", digits=5)
    write_table(__file__, ("day", "eot_min", "dec_deg"),
                [(t, S.equation_of_time(t), math.degrees(S.declination(t))) for t in days],
                part="eot", digits=5)
    mx, mn, zeros = eot_extremes()
    rows = [("max", mx[0], mx[1]), ("min", mn[0], mn[1])] + [("zero", z, 0) for z in zeros]
    rows.append(("perihelion", S.perihelion_time(), 0))
    write_table(__file__, ("what", "day", "value"), rows, part="extremes", digits=5)
