"""Plate velocities from a published set of rotation poles (grade 11, plate-motions).

NNR-MORVEL56 (Argus, Gordon and DeMets 2011, G-cubed 12, Q11001, doi:10.1029/
2011GC003751, Table 1): for each plate, the latitude and longitude of its rotation
pole and its angular speed (degrees per million years), in the frame in which the
lithosphere as a whole has no net rotation. Each plate turns counter-clockwise
about its pole (ledger nnr56:poles, nnr56:rms).

The velocity of a point at position r on the plate is v = omega x r, with omega the
rotation vector (angular speed times the unit vector of the pole) and |r| the Earth's
mean radius, 6371 km (shared ledger earth:Rmean). One degree per million years times
6371 km is 111.2 km per million years, i.e. 111.2 mm per year.

  part arrows   lon lat dx dy ve vn speed   chosen interior points of 17 plates:
                ve, vn east and north (mm/yr), speed (mm/yr), dx dy the arrow
                drawn on the map (degrees; SCALE degrees per cm/yr)
  part hawaii   the same for the point MKEA (one row)
  part rms      plate code name rms slab   the published root-mean-square speed
                of each large plate; slab = 1 when a subducting slab hangs from a
                long stretch of its edge
  part numbers  key value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

R_KM = 6371.0
SCALE = 2.5                    # map degrees per cm/yr of speed (drawing choice)

# Argus et al. (2011) Table 1: pole latitude (N), longitude (E), angular speed (deg/Myr),
# RMS speed (mm/yr). MORVEL plates only.
POLES = {
    "am": ("Amur", 63.17, -122.82, 0.297, 28.1),
    "an": ("Antarctica", 65.42, -118.11, 0.250, 15.2),
    "ar": ("Arabia", 48.88, -8.49, 0.559, 47.6),
    "au": ("Australia", 33.86, 37.94, 0.632, 63.1),
    "cp": ("Capricorn", 44.44, 23.09, 0.608, 66.2),
    "ca": ("Caribbean", 35.20, -92.62, 0.286, 14.9),
    "co": ("Cocos", 26.93, -124.31, 1.198, 74.6),
    "eu": ("Eurasia", 48.85, -106.50, 0.223, 22.8),
    "in": ("India", 50.37, -3.29, 0.544, 57.6),
    "jf": ("Juan de Fuca", -38.31, 60.04, 0.951, 17.4),
    "lw": ("Lwandle", 51.89, -69.52, 0.286, 26.5),
    "mq": ("Macquarie", 49.19, 11.05, 1.144, 49.5),
    "nz": ("Nazca", 46.23, -101.06, 0.696, 70.0),
    "na": ("North America", -4.85, -80.64, 0.209, 19.8),
    "nb": ("Nubia", 47.68, -68.44, 0.292, 29.2),
    "pa": ("Pacific", -63.58, 114.70, 0.651, 65.5),
    "ps": ("Philippine Sea", -46.02, -31.36, 0.910, 52.6),
    "ri": ("Rivera", 20.25, -107.29, 4.536, 11.8),
    "sw": ("Sandwich", -29.94, -36.87, 1.362, 72.6),
    "sc": ("Scotia", 22.52, -106.15, 0.146, 16.2),
    "sm": ("Somalia", 49.95, -84.52, 0.339, 31.0),
    "sa": ("South America", -22.62, -112.83, 0.109, 10.6),
    "su": ("Sunda", 50.06, -95.02, 0.337, 32.2),
    "sr": ("Sur", -32.50, -111.32, 0.107, 11.0),
    "yz": ("Yangtze", 63.03, -116.62, 0.334, 36.5),
}

# Points well inside each plate (lon E, lat N), chosen on the PB2002 map.
POINTS = {
    "pa": [(-150, 30), (-120, 10), (-140, -10), (-125, -30), (-160, -30), (170, 30),
           (-150, -48), (160, 15), (-135, 45), (-160, 47)],
    "na": [(-100, 40), (-80, 33), (-110, 58), (-55, 35), (-150, 64), (-40, 72)],
    "sa": [(-60, -10), (-62, -35), (-28, -22), (-45, 3)],
    "eu": [(10, 50), (40, 56), (80, 60), (100, 62), (-20, 50), (62, 45)],
    "nb": [(0, 15), (20, 2), (20, -25), (-5, 0), (-25, 30)],
    "sm": [(48, 2), (60, -12)],
    "ar": [(45, 22)],
    "in": [(78, 20), (66, 12)],
    "au": [(135, -25), (120, -20), (145, -36), (110, -42)],
    "cp": [(80, -22)],
    "an": [(30, -72), (120, -76), (-90, -78)],
    "nz": [(-90, -15), (-95, -35)],
    "co": [(-96, 8)],
    "ca": [(-74, 15)],
    "ps": [(134, 20)],
    "su": [(110, 6)],
}

MKEA = (-155.4563, 19.8014)    # NGL station coordinates (lon E, lat N)

# Plates with (1) and without (0) a long subducting slab along their edge
# (from the PB2002 map: the plate is the one that sinks along a trench). India is left
# out of both groups: its northern edge is a collision, its eastern edge a short trench.
SLAB = {"pa": 1, "co": 1, "nz": 1, "au": 1, "ps": 1,
        "eu": 0, "na": 0, "sa": 0, "an": 0, "nb": 0, "sm": 0, "ar": 0, "ca": 0}


def unit(lon, lat):
    p, l = math.radians(lat), math.radians(lon)
    return (math.cos(p) * math.cos(l), math.cos(p) * math.sin(l), math.sin(p))


def omega(code):
    """Rotation vector in radians per million years."""
    _, plat, plon, w, _ = POLES[code]
    u = unit(plon, plat)
    k = math.radians(w)
    return tuple(k * c for c in u)


def velocity(code, lon, lat):
    """(east, north) velocity in mm/yr (= km/Myr) of the point (lon, lat) on the plate."""
    w = omega(code)
    r = tuple(R_KM * c for c in unit(lon, lat))
    v = (w[1] * r[2] - w[2] * r[1], w[2] * r[0] - w[0] * r[2], w[0] * r[1] - w[1] * r[0])
    l, p = math.radians(lon), math.radians(lat)
    east = (-math.sin(l), math.cos(l), 0.0)
    north = (-math.sin(p) * math.cos(l), -math.sin(p) * math.sin(l), math.cos(p))
    return (sum(a * b for a, b in zip(v, east)), sum(a * b for a, b in zip(v, north)))


def relative(a, b, lon, lat):
    """Velocity of plate a relative to plate b at (lon, lat), mm/yr (east, north)."""
    va, vb = velocity(a, lon, lat), velocity(b, lon, lat)
    return (va[0] - vb[0], va[1] - vb[1])


def speed_azimuth(ve, vn):
    """Speed (mm/yr) and azimuth (degrees clockwise from north)."""
    return math.hypot(ve, vn), math.degrees(math.atan2(ve, vn)) % 360.0


def arrow_rows(points=POINTS):
    rows = []
    for code in sorted(points):
        for lon, lat in points[code]:
            ve, vn = velocity(code, lon, lat)
            rows.append((lon, lat, SCALE * ve / 10, SCALE * vn / 10, ve, vn, math.hypot(ve, vn)))
    return rows


def numbers():
    ve, vn = velocity("pa", *MKEA)
    s, az = speed_azimuth(ve, vn)
    n = {"mkea_ve": ve, "mkea_vn": vn, "mkea_speed": s, "mkea_az": az}
    # spreading across the Mid-Atlantic Ridge near 30 S (South America away from Nubia)
    rv = relative("sa", "nb", -13.5, -30.0)
    n["atl30s_speed"], n["atl30s_az"] = speed_azimuth(*rv)
    # the East Pacific Rise near 30 S (Pacific away from Nazca)
    rv = relative("pa", "nz", -112.0, -30.0)
    n["epr30s_speed"], n["epr30s_az"] = speed_azimuth(*rv)
    # India towards Eurasia near the Himalaya (used again in grade 12)
    rv = relative("in", "eu", 85.0, 28.0)
    n["in_eu_speed"], n["in_eu_az"] = speed_azimuth(*rv)
    # Wettzell on Eurasia
    ve, vn = velocity("eu", 12.879, 49.144)
    n["wtzr_ve"], n["wtzr_vn"] = ve, vn
    n["wtzr_speed"], n["wtzr_az"] = speed_azimuth(ve, vn)
    slab = [POLES[c][4] for c in SLAB if SLAB[c]]
    noslab = [POLES[c][4] for c in SLAB if not SLAB[c]]
    n["rms_slab_mean"] = sum(slab) / len(slab)
    n["rms_noslab_mean"] = sum(noslab) / len(noslab)
    return n


if __name__ == "__main__":
    write_table(__file__, ("lon", "lat", "dx", "dy", "ve", "vn", "speed"), arrow_rows(), part="arrows",
                digits=5)
    ve, vn = velocity("pa", *MKEA)
    write_table(__file__, ("lon", "lat", "dx", "dy", "ve", "vn", "speed"),
                [(MKEA[0], MKEA[1], SCALE * ve / 10, SCALE * vn / 10, ve, vn, math.hypot(ve, vn))],
                part="hawaii", digits=5)
    write_table(__file__, ("code", "rms", "slab"),
                [(c, POLES[c][4], SLAB[c]) for c in sorted(SLAB, key=lambda c: -POLES[c][4])],
                part="rms")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")
