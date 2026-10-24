"""Hotspots and the motion of the plates over them (Year 1, hotspots).

Data:
  * hotspot positions, track azimuths (with their uncertainty and weight) and rates,
    Table 1 of the electronic supplement of W. J. Morgan and J. P. Morgan (2007)
    (dataset bachelor-1-hotspots.csv, ledger data:b3-hotspots); a hotspot that the table
    rates with a quality letter (A, B) instead of a weight has no weight and stays out of
    the fit;
  * land from Natural Earth (shared figdata/out/shared-geo-land.dat, read by the figure);
  * depths from ETOPO1 at one degree (shared etopo-1deg.csv, ledger data:etopo1).

1. The Pacific plate in the hotspot frame. If the hotspots are fixed with respect to one
   another and the Pacific plate turns about an Euler pole E at the rate omega, each track
   runs, at its hotspot, along the velocity omega x r: perpendicular to the great circle
   joining the hotspot to E, and at the speed omega R sin(Delta). The pole is the point of
   the sphere that minimises sum w (az_obs - az_pred)^2 / s_az^2 over the Pacific
   hotspots (grid search, 0.5 degree then 0.02 degree); omega is the least-squares slope
   of the observed rates against R sin(Delta), through the origin.

2. The Hawaiian swell. Along a profile perpendicular to the Hawaiian track, the median
   ETOPO1 depth of the cells met by lines parallel to the track (0 to 1000 km downstream
   of the hotspot) gives the cross-section of the swell; the reference is the mean of the
   medians 1000 to 1500 km from the axis, on both sides. Inside 150 km of the axis the
   chain itself stands up; there the swell is interpolated between +-150 km. Its area A
   gives the buoyancy flux B = (rho_m - rho_w) A v (proposition in the text).

  part map-hs      lon lat                     every hotspot of the list
  part map-arrows  lon lat dx dy               hotspots with a rate: arrow along the track,
                                               0.15 degree per mm/yr (dx in degrees of
                                               longitude, so that the azimuth is true)
  part map-pole    lon lat                     the fitted Pacific pole
  part rates       name x rate srate pred      Pacific hotspots with a rate (x = R sin Delta, km)
  part rates-fit   x rate                      the line through the origin
  part swell       d med q25 q75               profile across the swell (d > 0 to the NE)
  part swell-ref   d ref swell                 the reference level and the interpolated swell
  part values      what value
"""
import csv
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
DERIVED = os.path.join(ROOT, "data", "derived")
R_KM = 6371.0
ARROW = 0.15                 # degrees per mm/yr on the map
HAWAII = (-155.2, 19.0)      # lon, lat of the hotspot (Morgan and Morgan 2007)
HAWAII_AZ = 304.0            # azimuth of its track
SWELL_DOWN = (0.0, 1000.0)   # km downstream of the hotspot along the track
SWELL_FAR = (1000.0, 1500.0)  # km from the axis: the reference
SWELL_CHAIN = 150.0          # km: inside this, the chain itself
RHO_M, RHO_W = 3300.0, 1000.0


def read(name):
    with open(os.path.join(DERIVED, name + ".csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


def hotspots():
    out = []
    for r in read("bachelor-1-hotspots"):
        f = lambda k: float(r[k]) if r[k] != "" else None  # noqa: E731
        out.append(dict(name=r["name"], plate=r["plate"], lat=float(r["lat"]), lon=float(r["lon"]),
                        w=f("w"), az=f("az"), saz=f("saz"), rate=f("rate"), srate=f("srate")))
    return out


def unit(lon, lat):
    lo, la = np.radians(lon), np.radians(lat)
    return np.stack([np.cos(la) * np.cos(lo), np.cos(la) * np.sin(lo), np.sin(la)], -1)


def lonlat(v):
    v = np.asarray(v, dtype=float)
    v = v / np.linalg.norm(v)
    return math.degrees(math.atan2(v[1], v[0])), math.degrees(math.asin(max(-1.0, min(1.0, v[2]))))


def east_north(lon, lat):
    lo, la = math.radians(lon), math.radians(lat)
    e = np.array([-math.sin(lo), math.cos(lo), 0.0])
    n = np.array([-math.sin(la) * math.cos(lo), -math.sin(la) * math.sin(lo), math.cos(la)])
    return e, n


def track_vector(lon, lat, az):
    """Unit vector, tangent to the sphere at (lon, lat), pointing to the azimuth az."""
    e, n = east_north(lon, lat)
    a = math.radians(az)
    return math.sin(a) * e + math.cos(a) * n


def predicted(pole_vec, lon, lat):
    """Azimuth of omega x r at (lon, lat) and angular distance to the pole, in degrees.
    pole_vec may be an array of unit vectors (n, 3)."""
    r = unit(lon, lat)
    v = np.cross(pole_vec, r)
    e, n = east_north(lon, lat)
    az = np.degrees(np.arctan2(v @ e, v @ n)) % 360.0
    delta = np.degrees(np.arccos(np.clip(pole_vec @ r, -1.0, 1.0)))
    return az, delta


def misfit(pole_vecs, rows):
    s = np.zeros(len(pole_vecs))
    for h in rows:
        az, _ = predicted(pole_vecs, h["lon"], h["lat"])
        d = (az - h["az"] + 180.0) % 360.0 - 180.0
        s += h["w"] * (d / h["saz"]) ** 2
    return s


def fit_pole(rows):
    """Pole (lon, lat) minimising the weighted azimuth misfit, and the minimum."""
    best = None
    for step, half in ((0.5, None), (0.02, 0.6)):
        if best is None:
            lons = np.arange(-180.0, 180.0, step)
            lats = np.arange(-90.0, 90.0 + 1e-9, step)
        else:
            lons = np.arange(best[0] - half, best[0] + half + 1e-9, step)
            lats = np.arange(max(-90.0, best[1] - half), min(90.0, best[1] + half) + 1e-9, step)
        g = np.stack(np.meshgrid(lons, lats), -1).reshape(-1, 2)
        s = misfit(unit(g[:, 0], g[:, 1]), rows)
        i = int(np.argmin(s))
        best = (float(g[i, 0]), float(g[i, 1]), float(s[i]))
    lon = (best[0] + 180.0) % 360.0 - 180.0
    return lon, best[1], best[2]


def fit_omega(rows, pole):
    """Least-squares omega (degrees per Myr) of rate = omega R sin(Delta), through 0."""
    pv = unit(*pole)
    x = np.array([R_KM * math.sin(math.radians(float(predicted(pv, h["lon"], h["lat"])[1])))
                  for h in rows])
    y = np.array([h["rate"] for h in rows])                  # mm/yr = km/Myr
    k = float(x @ y / (x @ x))                               # 1/Myr
    return math.degrees(k), x, y


def pole_from_two(h1, h2):
    """Euler pole from two track directions: perpendicular to both track vectors, on the
    side that turns the plate the right way (anticlockwise about the pole)."""
    t1 = track_vector(h1["lon"], h1["lat"], h1["az"])
    t2 = track_vector(h2["lon"], h2["lat"], h2["az"])
    p = np.cross(t1, t2)
    p = p / np.linalg.norm(p)
    if np.dot(np.cross(p, unit(h1["lon"], h1["lat"])), t1) < 0:
        p = -p
    return lonlat(p)


def destination(lon, lat, az, d_km):
    p, lam, a, dd = math.radians(lat), math.radians(lon), math.radians(az), d_km / R_KM
    p2 = math.asin(math.sin(p) * math.cos(dd) + math.cos(p) * math.sin(dd) * math.cos(a))
    l2 = lam + math.atan2(math.sin(a) * math.sin(dd) * math.cos(p), math.cos(dd) - math.sin(p) * math.sin(p2))
    return (math.degrees(l2) + 180.0) % 360.0 - 180.0, math.degrees(p2)


def etopo():
    return {(float(r["lat"]), float(r["lon"])): float(r["elev_m"]) for r in read("etopo-1deg")}


def swell_profile(grid=None, step=50.0, half=1500.0):
    grid = grid if grid is not None else etopo()
    out = []
    across = (HAWAII_AZ + 90.0) % 360.0
    for d in np.arange(-half, half + 1e-9, step):
        vals = []
        for s in np.arange(SWELL_DOWN[0], SWELL_DOWN[1] + 1e-9, step):
            lo, la = destination(*HAWAII, HAWAII_AZ, s)
            lo, la = destination(lo, la, across, d)
            vals.append(grid[(math.floor(la) + 0.5, math.floor(lo) + 0.5)])
        out.append((float(d), float(np.median(vals)), float(np.percentile(vals, 25)),
                    float(np.percentile(vals, 75))))
    return out


def swell_numbers(prof):
    d = np.array([p[0] for p in prof])
    m = np.array([p[1] for p in prof])
    far = (np.abs(d) >= SWELL_FAR[0]) & (np.abs(d) <= SWELL_FAR[1])
    ref = float(m[far].mean())
    # replace the chain by a straight line between -SWELL_CHAIN and +SWELL_CHAIN
    lo = int(np.argmin(np.abs(d + SWELL_CHAIN)))
    hi = int(np.argmin(np.abs(d - SWELL_CHAIN)))
    sw = m.copy()
    sw[lo:hi + 1] = np.interp(d[lo:hi + 1], [d[lo], d[hi]], [m[lo], m[hi]])
    inner = np.abs(d) < SWELL_FAR[0]
    h = np.clip(sw - ref, 0.0, None)
    area = float(np.trapezoid(h[inner], d[inner] * 1e3))     # m^2
    height = float(h[inner].max())
    return ref, height, area, sw


def buoyancy_flux(area_m2, v_mm_yr):
    """B = (rho_m - rho_w) A v, in kg/s."""
    return (RHO_M - RHO_W) * area_m2 * v_mm_yr * 1e-3 / (365.25 * 86400.0)


def analysis():
    hs = hotspots()
    pac = [h for h in hs if h["plate"] == "Pacific" and h["az"] is not None and h["w"] is not None]
    plon, plat, chi2 = fit_pole(pac)
    rated = [h for h in pac if h["rate"] is not None]
    omega, x, y = fit_omega(rated, (plon, plat))
    pv = unit(plon, plat)
    haw = next(h for h in pac if h["name"] == "Hawaii")
    lou = next(h for h in pac if h["name"] == "Louisville")
    az_h, d_h = predicted(pv, haw["lon"], haw["lat"])
    two = pole_from_two(haw, lou)
    prof = swell_profile()
    ref, height, area, sw = swell_numbers(prof)
    vals = {
        "n_all": len(hs), "n_pacific": len(pac), "n_rated": len(rated),
        "pole_lon": plon, "pole_lat": plat, "chi2": chi2, "omega_deg_myr": omega,
        "hawaii_pred_az": float(az_h), "hawaii_delta": float(d_h),
        "hawaii_pred_rate": math.radians(omega) * R_KM * math.sin(math.radians(float(d_h))),
        "two_pole_lon": two[0], "two_pole_lat": two[1],
        "rms_rate": float(np.sqrt(np.mean((y - math.radians(omega) * x) ** 2))),
        "swell_ref": ref, "swell_height": height, "swell_area_m2": area,
        "swell_B_kg_s": buoyancy_flux(area, haw["rate"]),
    }
    return hs, pac, rated, x, y, prof, sw, vals


if __name__ == "__main__":
    hs, pac, rated, x, y, prof, sw, vals = analysis()
    write_table(__file__, ("lon", "lat"), [(h["lon"], h["lat"]) for h in hs], part="map-hs")
    arrows = []
    for h in hs:
        if h["rate"] is None or h["az"] is None:
            continue
        L = ARROW * h["rate"]
        a = math.radians(h["az"])
        arrows.append((h["lon"], h["lat"], round(L * math.sin(a) / math.cos(math.radians(h["lat"])), 4),
                       round(L * math.cos(a), 4)))
    write_table(__file__, ("lon", "lat", "dx", "dy"), arrows, part="map-arrows")
    write_table(__file__, ("lon", "lat"), [(round(vals["pole_lon"], 2), round(vals["pole_lat"], 2))],
                part="map-pole")
    k = math.radians(vals["omega_deg_myr"])
    write_table(__file__, ("name", "x", "rate", "srate", "pred"),
                [(h["name"].split("/")[0].replace(" ", "-"), round(float(xi), 1), h["rate"], h["srate"],
                  round(k * float(xi), 1)) for h, xi in zip(rated, x)], part="rates")
    write_table(__file__, ("x", "rate"), [(0, 0), (R_KM, round(k * R_KM, 2))], part="rates-fit")
    write_table(__file__, ("d", "med", "q25", "q75"), prof, part="swell")
    write_table(__file__, ("d", "ref", "swell"),
                [(p[0], round(vals["swell_ref"], 1), round(float(s), 1)) for p, s in zip(prof, sw)],
                part="swell-ref")
    write_table(__file__, ("what", "value"), sorted(vals.items()), part="values", digits=6)
