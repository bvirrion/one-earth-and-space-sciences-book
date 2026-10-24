"""Earthquake sections across subduction zones (grade 11, subduction-zones).

Data: the USGS ComCat catalogue of earthquakes of magnitude 6 or more, 1976-2025
(data/derived/usgs-m6.csv, ledger data:usgs-comcat); the PB2002 boundary steps
with their relative plate velocities (data/derived/pb2002-steps.csv, ledger
data:pb2002); the age of the ocean floor (data/derived/grade-11-seafloor-age.csv,
ledger data:b2-seafloor-age).

A profile starts at a point of the trench (the PB2002 subduction step nearest to a
chosen point) and runs perpendicular to the trench, toward the overriding plate.
For a step `A/B` B sinks under A, for `A\\B` A sinks under B; the first-named plate
lies on the left of the step's direction (lon0, lat0) -> (lon1, lat1). Each
earthquake within HALF_WIDTH km of the profile line is placed at its distance x
along the profile (azimuthal equidistant about the trench point) and its depth.

  part <name>      x depth mag           events of a profile (tonga, japan, andes)
  part world-<c>   lon lat depth mag     M >= 6.5 events by depth class c:
                                         shallow (< 70 km), mid (70-300), deep (> 300)
  part speeds      idx rms slab          published RMS plate speeds (from
                                         plate_velocities), sorted, for a bar chart
  part numbers     key value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402
import plate_velocities as pv  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DERIVED = os.path.join(ROOT, "data", "derived")
R_KM = 6371.0
HALF_WIDTH = 150.0               # km on each side of the profile line
SHALLOW, DEEP = 70.0, 300.0      # depth classes (km)

# chosen points near the trench (lon, lat) and the step names to search
PROFILES = {
    "tonga": ((-173.3, -20.4), "TO/PA"),
    "japan": ((143.95, 38.3), "PA\\OK"),
    "andes": ((-71.3, -21.0), "NZ\\AP"),
}
XMAX = {"tonga": 900.0, "japan": 1500.0, "andes": 900.0}


def read(name):
    with open(os.path.join(DERIVED, name + ".csv"), newline="") as f:
        return list(csv.DictReader(f))


def quakes():
    return [(float(e["lon"]), float(e["lat"]), float(e["depth_km"]), float(e["mag"]))
            for e in read("usgs-m6")]


def dist_bearing(lon0, lat0, lon, lat):
    """Great-circle distance (km) and initial bearing (degrees) from point 0."""
    p0, p1 = math.radians(lat0), math.radians(lat)
    dl = math.radians(lon - lon0)
    c = math.sin(p0) * math.sin(p1) + math.cos(p0) * math.cos(p1) * math.cos(dl)
    d = math.acos(max(-1.0, min(1.0, c)))
    b = math.atan2(math.sin(dl) * math.cos(p1),
                   math.cos(p0) * math.sin(p1) - math.sin(p0) * math.cos(p1) * math.cos(dl))
    return R_KM * d, math.degrees(b) % 360.0


def sinking_plate(name):
    a, b = (name.split("/") if "/" in name else name.split("\\"))
    return b if "/" in name else a


def trench(name):
    """Trench point, strike azimuth, azimuth toward the overriding plate, rate (mm/yr)."""
    (lon, lat), step = PROFILES[name]
    steps = [s for s in read("pb2002-steps") if s["class"] == "SUB" and s["name"] == step]
    best = min(steps, key=lambda s: dist_bearing(lon, lat, float(s["lon"]), float(s["lat"]))[0])
    t_lon, t_lat = float(best["lon"]), float(best["lat"])
    _, strike = dist_bearing(float(best["lon0"]), float(best["lat0"]),
                             float(best["lon1"]), float(best["lat1"]))
    # the first-named plate is on the left of the step; it overrides for "/" steps
    over_left = "/" in step
    az = (strike - 90.0) % 360.0 if over_left else (strike + 90.0) % 360.0
    near = [float(s["vel_mm_a"]) for s in steps
            if dist_bearing(t_lon, t_lat, float(s["lon"]), float(s["lat"]))[0] <= 100.0]
    return (t_lon, t_lat), strike, az, sum(near) / len(near)


def project(name, events=None):
    (t_lon, t_lat), _, az, _ = trench(name)
    rows = []
    for lon, lat, depth, mag in (events if events is not None else quakes()):
        d, b = dist_bearing(t_lon, t_lat, lon, lat)
        x = d * math.cos(math.radians(b - az))
        y = d * math.sin(math.radians(b - az))
        if abs(y) <= HALF_WIDTH and -200.0 <= x <= XMAX[name]:
            rows.append((x, depth, mag))
    return sorted(rows)


def dip_fit(rows, zmin=100.0, zmax=600.0):
    """Least-squares line depth = a + s x over events between zmin and zmax km deep."""
    pts = [(x, z) for x, z, _ in rows if zmin <= z <= zmax]
    n = len(pts)
    mx = sum(p[0] for p in pts) / n
    mz = sum(p[1] for p in pts) / n
    s = sum((x - mx) * (z - mz) for x, z in pts) / sum((x - mx) ** 2 for x, _ in pts)
    return mz - s * mx, s, n


def seafloor_age_before(name, lo=100.0, hi=400.0):
    """Median age (Myr) of the ocean floor 100-400 km seaward of the trench point."""
    (t_lon, t_lat), _, az, _ = trench(name)
    ages = []
    for c in read("grade-11-seafloor-age"):
        d, b = dist_bearing(t_lon, t_lat, float(c["lon"]), float(c["lat"]))
        x = d * math.cos(math.radians(b - az))
        y = d * math.sin(math.radians(b - az))
        if -hi <= x <= -lo and abs(y) <= HALF_WIDTH:
            ages.append(float(c["age"]))
    ages.sort()
    return ages[len(ages) // 2], len(ages)


def depth_class(z):
    return "shallow" if z < SHALLOW else ("mid" if z <= DEEP else "deep")


def numbers():
    n = {}
    for name in PROFILES:
        rows = project(name)
        (t_lon, t_lat), strike, az, rate = trench(name)
        a, s, k = dip_fit(rows)
        n[name + "_trench_lon"], n[name + "_trench_lat"] = t_lon, t_lat
        n[name + "_azimuth"] = az
        n[name + "_rate"] = rate
        n[name + "_n"] = len(rows)
        n[name + "_maxdepth"] = max(z for _, z, _ in rows)
        n[name + "_dip"] = math.degrees(math.atan(s))
        n[name + "_fit_a"], n[name + "_fit_s"], n[name + "_fit_n"] = a, s, k
        x670 = (670.0 - a) / s
        n[name + "_x670"] = x670
        n[name + "_path670"] = math.hypot(x670, 670.0)
        n[name + "_time670"] = n[name + "_path670"] / rate     # km / (mm/yr) = Myr
        n[name + "_age"] = seafloor_age_before(name)[0]
    q = quakes()
    n["world_n_m65"] = sum(1 for e in q if e[3] >= 6.5)
    n["world_deep_n"] = sum(1 for e in q if e[3] >= 6.5 and e[2] > DEEP)
    n["catalogue_maxdepth"] = max(e[2] for e in q)
    n["catalogue_n"] = len(q)
    n["frac_deeper_70"] = sum(1 for e in q if e[2] >= SHALLOW) / len(q)
    n["frac_deeper_300"] = sum(1 for e in q if e[2] > DEEP) / len(q)
    return n


def speed_rows():
    rows = sorted(((pv.POLES[c][4], pv.SLAB[c], c) for c in pv.SLAB), reverse=True)
    return [(i, r, s) for i, (r, s, _) in enumerate(rows)], [c for _, _, c in rows]


if __name__ == "__main__":
    for name in PROFILES:
        write_table(__file__, ("x", "depth", "mag"), project(name), part=name, digits=5)
    q = [e for e in quakes() if e[3] >= 6.5]
    for c in ("shallow", "mid", "deep"):
        write_table(__file__, ("lon", "lat", "depth", "mag"),
                    [e for e in q if depth_class(e[2]) == c], part="world-" + c, digits=6)
    rows, _ = speed_rows()
    write_table(__file__, ("idx", "rms", "slab"), rows, part="speeds")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")
