"""Relative plate velocities on a sphere from Euler vectors (Year 1, plate-kinematics).

Euler vectors used (ledger):
  * MORVEL, DeMets, Gordon and Argus (2010), Table 1: Eurasia relative to North America,
    pole 61.8 N, 139.6 E, 0.210 deg/Myr (geological, spreading rates since about 3 Ma)
    -- ledger morvel:eu-na; Nubia relative to North America 79.2 N, 40.2 E,
    0.233 deg/Myr -- morvel:nb-na.
  * the same paper, Table 6: Eurasia relative to North America from GPS station
    velocities in the plate interiors alone, 74.2 N, 134.1 E, 0.237 deg/Myr
    -- ledger morvel:gps-eu-na.

v = omega x r, resolved into east and north components on a sphere of radius
6371 km. The PB2002 boundary steps (shared dataset data/derived/pb2002-steps.csv,
ledger data:pb2002) carry Bird's relative velocity for each step: the figure
compares them with the MORVEL prediction along the Eurasia--North America ridges.

  part mar     delta pb2002 morvel gps lat lon   (delta: angular distance from the
               MORVEL pole, degrees; velocities in mm/yr) -- spreading steps only
  part curve   delta v                            (omega R sin delta, MORVEL)
  part values  what value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
STEPS = os.path.join(ROOT, "data", "derived", "pb2002-steps.csv")
R_KM = 6371.0
MYR = 1e6

MORVEL_EU_NA = (61.8, 139.6, 0.210)       # lat, lon, deg/Myr
MORVEL_NB_NA = (79.2, 40.2, 0.233)
GPS_EU_NA = (74.2, 134.1, 0.237)           # MORVEL paper, Table 6 (GPS only)


def unit(lat, lon):
    la, lo = math.radians(lat), math.radians(lon)
    return (math.cos(la) * math.cos(lo), math.cos(la) * math.sin(lo), math.sin(la))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


def euler_vector(lat, lon, rate_deg_myr):
    """Angular velocity vector in rad/yr."""
    w = math.radians(rate_deg_myr) / MYR
    return tuple(w * c for c in unit(lat, lon))


def pole(omega):
    """(lat, lon, rate in deg/Myr) of an angular velocity vector in rad/yr."""
    w = norm(omega)
    return (math.degrees(math.asin(omega[2] / w)),
            math.degrees(math.atan2(omega[1], omega[0])),
            math.degrees(w) * MYR)


def relative(a, b):
    """Angular velocity of plate a relative to plate b."""
    return tuple(x - y for x, y in zip(a, b))


def velocity_en(omega, lat, lon):
    """(east, north) velocity in mm/yr at (lat, lon) for omega in rad/yr."""
    r = tuple(R_KM * 1e6 * c for c in unit(lat, lon))          # mm
    v = cross(omega, r)
    la, lo = math.radians(lat), math.radians(lon)
    e = (-math.sin(lo), math.cos(lo), 0.0)
    n = (-math.sin(la) * math.cos(lo), -math.sin(la) * math.sin(lo), math.cos(la))
    return dot(v, e), dot(v, n)


def speed_azimuth(omega, lat, lon):
    ve, vn = velocity_en(omega, lat, lon)
    return math.hypot(ve, vn), math.degrees(math.atan2(ve, vn)) % 360.0


def angular_distance(lat1, lon1, lat2, lon2):
    c = dot(unit(lat1, lon1), unit(lat2, lon2))
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def speed_formula(plat, plon, rate_deg_myr, lat, lon):
    """omega R sin(delta), mm/yr."""
    d = math.radians(angular_distance(plat, plon, lat, lon))
    return math.radians(rate_deg_myr) / MYR * R_KM * 1e6 * math.sin(d)


def eu_na_steps():
    """PB2002 spreading steps between Eurasia and North America."""
    out = []
    with open(STEPS, encoding="utf8") as f:
        for r in csv.DictReader(f):
            if r["name"] in ("EU-NA", "NA-EU") and r["class"] == "OSR":
                out.append((float(r["lat"]), float(r["lon"]), float(r["vel_mm_a"])))
    return out


def gps_eu_na():
    return euler_vector(*GPS_EU_NA)


def morvel_eu_na():
    return euler_vector(*MORVEL_EU_NA)


def mar_rows():
    wm, wi = morvel_eu_na(), gps_eu_na()
    rows = []
    for lat, lon, v in eu_na_steps():
        d = angular_distance(MORVEL_EU_NA[0], MORVEL_EU_NA[1], lat, lon)
        rows.append((d, v, speed_azimuth(wm, lat, lon)[0], speed_azimuth(wi, lat, lon)[0], lat, lon))
    rows.sort()
    return rows


def mean_relative_difference():
    rows = mar_rows()
    return sum(abs(m - p) / p for _, p, m, _, _, _ in rows) / len(rows)


POINTS = {"iceland": (64.5, -18.0), "reyk": (64.139, -21.955), "hofn": (64.267, -15.198),
          "atj": (39.44, -29.83)}


if __name__ == "__main__":
    write_table(__file__, ("delta", "pb2002", "morvel", "gps", "lat", "lon"), mar_rows(),
                part="mar", digits=6)
    w_mm = math.radians(MORVEL_EU_NA[2]) / MYR * R_KM * 1e6
    curve = [(d, w_mm * math.sin(math.radians(d))) for d in [k * 0.5 for k in range(0, 181)]]
    write_table(__file__, ("delta", "v"), curve, part="curve", digits=6)
    wm, wi = morvel_eu_na(), gps_eu_na()
    vals = []
    for k, (la, lo) in POINTS.items():
        sm, am = speed_azimuth(wm, la, lo)
        si, ai = speed_azimuth(wi, la, lo)
        vals += [("morvel_speed_" + k, sm), ("morvel_az_" + k, am),
                 ("gps_speed_" + k, si), ("gps_az_" + k, ai),
                 ("delta_morvel_" + k, angular_distance(MORVEL_EU_NA[0], MORVEL_EU_NA[1], la, lo))]
    pl = pole(relative(euler_vector(*MORVEL_NB_NA), wm))
    vals += [("nb_eu_pole_lat", pl[0]), ("nb_eu_pole_lon", pl[1]), ("nb_eu_rate", pl[2]),
             ("mean_rel_diff_morvel_pb2002", mean_relative_difference())]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)
