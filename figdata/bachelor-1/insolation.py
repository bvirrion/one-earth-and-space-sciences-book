"""Daily-mean insolation at the top of the atmosphere against latitude and day of the
year (Year 1, radiation-heat-transport).

The Sun's declination and distance come from the Kepler model of _solar.py (ledger
earth:ecc, earth:obliquity, nasa:earth-perihelion-longitude, usno:tropical-year,
usno:seasons-2026); the solar irradiance at the mean distance is S0 = 1361 W/m2
(earth:TSI). The daily mean integrates the instantaneous insolation of ch. 1,
S0 (a/r)^2 sin h, over the hours the Sun is up:

    Q = (S0/pi) (a/r)^2 (h0 sin(phi) sin(delta) + cos(phi) cos(delta) sin(h0)),
    cos(h0) = -tan(phi) tan(delta)  (h0 = 0 in the polar night, pi in the polar day).

  part grid       day lat Q                   (every 5 days x every 2.5 deg, matrix plot)
  part annual     lat Q_ann Q_jun Q_dec       (annual mean and the two solstices)
  part sun        day decl night_n night_s    (the subsolar latitude, which is the Sun's
                                               declination, and the edge of the polar night
                                               in each hemisphere, nan when there is none)
  part values     what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402
import _solar  # noqa: E402

S0 = 1361.0
DAYS = 365


def hour_angle_sunset(phi, delta):
    """h0 (radians) from cos h0 = -tan(phi) tan(delta), clipped for polar day and night."""
    x = -math.tan(phi) * math.tan(delta)
    if x <= -1:
        return math.pi
    if x >= 1:
        return 0.0
    return math.acos(x)


def daily_mean(lat_deg, t, s0=S0):
    """Daily-mean insolation (W/m2) at latitude lat_deg on day t (days after 1 Jan 0 h)."""
    phi = math.radians(lat_deg)
    if abs(lat_deg) >= 90:
        phi = math.copysign(math.pi / 2 - 1e-12, lat_deg)
    d = _solar.declination(t)
    h0 = hour_angle_sunset(phi, d)
    f = (1.0 / _solar.distance_ratio(t)) ** 2
    return s0 / math.pi * f * (h0 * math.sin(phi) * math.sin(d) + math.cos(phi) * math.cos(d) * math.sin(h0))


def instantaneous_mean(lat_deg, t, n=2000, s0=S0):
    """The same daily mean by brute force: average of S0 (a/r)^2 max(sin h, 0) over n
    instants of the day (declination and distance held at their value on day t)."""
    phi = math.radians(lat_deg)
    d = _solar.declination(t)
    f = (1.0 / _solar.distance_ratio(t)) ** 2
    tot = 0.0
    for k in range(n):
        H = 2 * math.pi * (k + 0.5) / n - math.pi
        sinh = math.sin(phi) * math.sin(d) + math.cos(phi) * math.cos(d) * math.cos(H)
        tot += max(sinh, 0.0)
    return s0 * f * tot / n


def annual_mean(lat_deg, n=365):
    return sum(daily_mean(lat_deg, _solar.YEAR * (k + 0.5) / n) for k in range(n)) / n


def global_annual_mean(nlat=180, n=73):
    """Area-weighted mean over the sphere of the annual mean (midpoint rule in sin(lat))."""
    tot = 0.0
    for j in range(nlat):
        mu = -1 + (j + 0.5) * 2.0 / nlat
        lat = math.degrees(math.asin(mu))
        tot += sum(daily_mean(lat, _solar.YEAR * (k + 0.5) / n) for k in range(n)) / n
    return tot / nlat


def solstice_days():
    """t of the June and December solstices (Sun's longitude 90 and 270 deg)."""
    def find(target):
        lo, hi = 0.0, _solar.YEAR
        best = min(range(0, 366), key=lambda k: abs(((_solar.longitude(k) - target + math.pi)
                                                     % (2 * math.pi)) - math.pi))
        lo, hi = best - 2.0, best + 2.0
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            e = ((_solar.longitude(mid) - target + math.pi) % (2 * math.pi)) - math.pi
            if e > 0:
                hi = mid
            else:
                lo = mid
        return 0.5 * (lo + hi)
    return find(math.pi / 2), find(3 * math.pi / 2)


def polar_night_edge(t):
    """(northern edge, southern edge) of the polar night on day t, in degrees: the
    polar night covers |lat| > 90 - |delta| in the winter hemisphere."""
    d = math.degrees(_solar.declination(t))
    if d < 0:
        return 90.0 + d, float("nan")
    return float("nan"), -(90.0 - d)


def values():
    tj, td = solstice_days()
    te = _solar.T_EQUINOX
    return [
        ("S0_over_pi", S0 / math.pi), ("S0_over_4", S0 / 4),
        ("equator_equinox", daily_mean(0.0, te)),
        ("pole_june", daily_mean(90.0, tj)), ("equator_june", daily_mean(0.0, tj)),
        ("pole_dec_south", daily_mean(-90.0, td)), ("lat45_june", daily_mean(45.0, tj)),
        ("lat45_dec", daily_mean(45.0, td)), ("lat40_june", daily_mean(40.0, tj)),
        ("lat40_dec", daily_mean(40.0, td)), ("lat40_equinox", daily_mean(40.0, te)),
        ("ann_0", annual_mean(0.0)), ("ann_40", annual_mean(40.0)), ("ann_90", annual_mean(90.0)),
        ("ann_m90", annual_mean(-90.0)), ("global", global_annual_mean()),
        ("t_june", tj), ("t_dec", td),
    ]


if __name__ == "__main__":
    grid = []
    for k in range(0, 74):
        t = 5.0 * k
        for j in range(0, 73):
            lat = -90.0 + 2.5 * j
            grid.append((t, lat, daily_mean(lat, t)))
    write_table(__file__, ("day", "lat", "Q"), grid, part="grid", digits=5)
    tj, td = solstice_days()
    write_table(__file__, ("lat", "Q_ann", "Q_jun", "Q_dec"),
                [(lat, annual_mean(lat), daily_mean(lat, tj), daily_mean(lat, td))
                 for lat in [-90.0 + 2.5 * j for j in range(73)]], part="annual", digits=5)
    write_table(__file__, ("day", "decl", "night_n", "night_s"),
                [(float(t), math.degrees(_solar.declination(t))) + polar_night_edge(t)
                 for t in range(0, 366)], part="sun", digits=5)
    write_table(__file__, ("what", "value"), values(), part="values", digits=7)
