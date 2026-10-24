"""Two plateaus (Year 2, himalaya-andes): relief maps and swath profiles of Tibet and of
the Central Andes, with the arithmetic of thick crust.

  relief    ETOPO1 every 6th node (0.1 degree): Tibet and the Himalaya 25-40 N, 75-100 E
            (data/derived/bachelor-2-etopo-tibet.csv, ledger data:b4-etopo-tibet); Central
            Andes 30-10 S, 75-60 W (data/derived/bachelor-2-etopo-andes.csv, ledger
            data:b4-etopo-andes). Contours by marching squares (figdata/shared/region.py),
            simplified (Douglas-Peucker); loops of fewer than MIN_PTS points dropped.
  swaths    Tibet: nodes 86-90 E, mean / maximum / minimum elevation at each latitude,
            distance north of 25 N (111.19 km per degree). Andes: nodes 21-19 S, at each
            longitude, distance east of 75 W (111.19 cos 20 deg km per degree).
  plateau   the stretch of a swath around its highest mean where the swath-mean elevation
            stays above PLATEAU_M = 3000 m: its width and the mean of the swath means.
  isostasy  Airy (Year 1 volume): crust of normal thickness H at sea level; under a mean
            elevation h the root is r = h rho_c / (rho_m - rho_c) and the crust is
            H + h + r thick. Excess gravitational potential energy per unit area of the
            high column over the normal one, both to the compensation depth:
            dF = rho_c g h (H + h/2 + r/2) (the chapter's proposition).
  shortening area balance of a crust thickened from H to T over a width W: it was
            W T / H wide, so S = W (T - H) / H.
  plates    velocity of one plate relative to another at a point, v = (w_A - w_B) x r,
            from the NNR-MORVEL56 angular velocities (Argus et al. 2011, Table 1; ledger
            nnr56:poles, cited from the Book 2 ledger): India relative to Eurasia at
            28 N 85 E, Nazca relative to South America at 20 S 71 W.

  part tc2000, tc4000          lon lat (Tibet window, no coast in it; blank line between polylines)
  part ac2000, ac4000, ac0     lon lat (Andes window)
  part tswath                  lat km mean_m max_m min_m
  part aswath                  lon km mean_m max_m min_m
  part pressure                z_km p_high_MPa p_ref_MPa (h = 4.8 km, H = 35 km)
  part numbers                 key value
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")
KM_PER_DEG = 111.19
R_EARTH_KM = 6371.0
MIN_PTS = 16
PLATEAU_M = 3000.0
G = 9.8
RHO_C, RHO_M = 2700.0, 3300.0
H_KM = 35.0
TIBET_LON = (86.0, 90.0)
ANDES_LAT = (-21.0, -19.0)
ANDES_KM_PER_DEG = KM_PER_DEG * math.cos(math.radians(20.0))

# NNR-MORVEL56 (Argus et al. 2011, Table 1): pole latitude N, longitude E, deg/Myr
POLES = {"India": (50.37, -3.29, 0.544), "Eurasia": (48.85, -106.50, 0.223),
         "Nazca": (46.23, -101.06, 0.696), "South America": (-22.62, -112.83, 0.109)}


def grid(name):
    """lats (ascending), lons (ascending), Z (ny x nx, m) of bachelor-2-etopo-<name>."""
    path = os.path.join(DERIVED, "bachelor-2-etopo-%s.csv" % name)
    with open(path, encoding="utf8") as f:
        rows = [(float(r["lat"]), float(r["lon"]), float(r["elev_m"])) for r in csv.DictReader(f)]
    lat = np.array([r[0] for r in rows])
    lon = np.array([r[1] for r in rows])
    z = np.array([r[2] for r in rows])
    lats, lons = np.unique(lat), np.unique(lon)
    zz = np.full((len(lats), len(lons)), np.nan)
    zz[np.searchsorted(lats, lat), np.searchsorted(lons, lon)] = z
    return lats, lons, zz


def contours(name, level, tol=0.03):
    import region
    lats, lons, zz = grid(name)
    return [region.simplify(line, tol) for line in region.trace(zz, lons, lats, level=level)
            if len(line) >= MIN_PTS]


def tibet_swath():
    """(lat, km north of 25 N, mean, max, min) over 86-90 E."""
    lats, lons, zz = grid("tibet")
    sel = (lons >= TIBET_LON[0] - 1e-9) & (lons <= TIBET_LON[1] + 1e-9)
    return [(round(float(la), 3), (la - 25.0) * KM_PER_DEG, float(zz[j, sel].mean()),
             float(zz[j, sel].max()), float(zz[j, sel].min())) for j, la in enumerate(lats)]


def andes_swath():
    """(lon, km east of 75 W, mean, max, min) over 21-19 S."""
    lats, lons, zz = grid("andes")
    sel = (lats >= ANDES_LAT[0] - 1e-9) & (lats <= ANDES_LAT[1] + 1e-9)
    return [(round(float(lo), 3), (lo + 75.0) * ANDES_KM_PER_DEG, float(zz[sel, i].mean()),
             float(zz[sel, i].max()), float(zz[sel, i].min())) for i, lo in enumerate(lons)]


def plateau(swath, threshold=PLATEAU_M):
    """(first, last, width_km, mean_m): the run of swath means above threshold that holds
    the highest mean."""
    means = [r[2] for r in swath]
    k = int(np.argmax(means))
    i = k
    while i > 0 and means[i - 1] > threshold:
        i -= 1
    j = k
    while j < len(means) - 1 and means[j + 1] > threshold:
        j += 1
    return swath[i][0], swath[j][0], swath[j][1] - swath[i][1], float(np.mean(means[i:j + 1]))


def airy_root(h_km, rho_c=RHO_C, rho_m=RHO_M):
    return h_km * rho_c / (rho_m - rho_c)


def airy_thickness(h_km, H=H_KM, rho_c=RHO_C, rho_m=RHO_M):
    """crustal thickness (km) under a mean elevation h (km): H + h + r."""
    return H + h_km + airy_root(h_km, rho_c, rho_m)


def crust_density_for(T_km, h_km, H=H_KM, rho_m=RHO_M):
    """the crustal density that makes Airy give thickness T: r = T - H - h = h rc/(rm - rc)."""
    r = T_km - H - h_km
    return rho_m * r / (r + h_km)


def gpe_excess(h_km, H=H_KM, rho_c=RHO_C, rho_m=RHO_M, g=G):
    """excess potential energy per unit area (J/m2 = N/m) of an Airy-compensated column of
    elevation h over the normal column: rho_c g h (H + h/2 + r/2), lengths in metres."""
    h, Hm, r = h_km * 1e3, H * 1e3, airy_root(h_km, rho_c, rho_m) * 1e3
    return rho_c * g * h * (Hm + h / 2 + r / 2)


def gpe_by_integration(h_km, H=H_KM, rho_c=RHO_C, rho_m=RHO_M, g=G, n=20000):
    """the same, by integrating the two lithostatic pressure profiles numerically."""
    h, Hm, r = h_km * 1e3, H * 1e3, airy_root(h_km, rho_c, rho_m) * 1e3
    L = Hm + r
    z = np.linspace(-h, L, n + 1)
    p_high = rho_c * g * (z + h)
    p_ref = np.where(z < 0, 0.0, np.where(z <= Hm, rho_c * g * z, rho_c * g * Hm + rho_m * g * (z - Hm)))
    return float(np.trapezoid(p_high - p_ref, z))


def pressure_profiles(h_km, H=H_KM, rho_c=RHO_C, rho_m=RHO_M, g=G, step_km=0.5):
    """(z_km below sea level, p_high_MPa, p_ref_MPa) from the top of the high column down to
    the base of its root (the compensation depth): the lithostatic pressures of the thick
    and of the normal column; the area between them is the excess potential energy."""
    r = airy_root(h_km, rho_c, rho_m)
    L = H + r
    n = int(round((L + h_km) / step_km))
    rows = []
    for k in range(n + 1):
        z = -h_km + k * (L + h_km) / n
        ph = rho_c * g * (z + h_km) * 1e3 / 1e6
        if z < 0:
            pr = 0.0
        elif z <= H:
            pr = rho_c * g * z * 1e3 / 1e6
        else:
            pr = (rho_c * g * H + rho_m * g * (z - H)) * 1e3 / 1e6
        rows.append((z, ph, pr))
    return rows


def shortening_from_thickening(width_km, T_km, H=H_KM):
    """area balance: crust T thick over a width W was W T / H wide; S = W (T - H)/H."""
    return width_km * (T_km - H) / H


def _vec(lat, lon):
    la, lo = math.radians(lat), math.radians(lon)
    return np.array([math.cos(la) * math.cos(lo), math.cos(la) * math.sin(lo), math.sin(la)])


def relative_velocity(a, b, lat, lon):
    """(speed mm/yr, azimuth deg) of plate a relative to plate b at (lat, lon)."""
    def omega(p):
        la, lo, w = POLES[p]
        return _vec(la, lo) * math.radians(w) / 1e6          # rad/yr
    v = np.cross(omega(a) - omega(b), _vec(lat, lon) * R_EARTH_KM * 1e6)   # mm/yr
    la, lo = math.radians(lat), math.radians(lon)
    east = np.array([-math.sin(lo), math.cos(lo), 0.0])
    north = np.array([-math.sin(la) * math.cos(lo), -math.sin(la) * math.sin(lo), math.cos(la)])
    ve, vn = float(v @ east), float(v @ north)
    return math.hypot(ve, vn), math.degrees(math.atan2(ve, vn)) % 360.0


def numbers():
    ts, as_ = tibet_swath(), andes_swath()
    t0, t1, tw, tm = plateau(ts)
    a0, a1, aw, am = plateau(as_)
    th = round(tm / 1000.0, 1)          # printed mean elevations, rounded once
    ah = round(am / 1000.0, 1)
    vin, ain = relative_velocity("India", "Eurasia", 28.0, 85.0)
    vnz, anz = relative_velocity("Nazca", "South America", -20.0, -71.0)
    deepest = min(as_, key=lambda r: r[4])
    return {
        "tibet_plateau_from": t0, "tibet_plateau_to": t1, "tibet_plateau_width_km": tw,
        "tibet_plateau_mean_m": tm, "tibet_max_mean_m": max(r[2] for r in ts),
        "andes_plateau_from": a0, "andes_plateau_to": a1, "andes_plateau_width_km": aw,
        "andes_plateau_mean_m": am, "andes_trench_min_m": deepest[4], "andes_trench_lon": deepest[0],
        "tibet_airy_T_km": airy_thickness(th), "andes_airy_T_km": airy_thickness(ah),
        "tibet_root_km": airy_root(th), "andes_root_km": airy_root(ah),
        "tibet_gpe_Npm": gpe_excess(th), "andes_gpe_Npm": gpe_excess(ah),
        "v_india_eurasia_mmyr": vin, "az_india_eurasia": ain,
        "v_nazca_southamerica_mmyr": vnz, "az_nazca_southamerica": anz,
    }


def _lines(polylines):
    rows = []
    for k, line in enumerate(polylines):
        if k:
            rows.append(())
        rows.extend((round(x, 3), round(y, 3)) for x, y in line)
    return rows


if __name__ == "__main__":
    for name, tag, levels in (("tibet", "t", (2000, 4000)), ("andes", "a", (0, 2000, 4000))):
        for lev in levels:
            write_table(__file__, ("lon", "lat"), _lines(contours(name, lev)), part="%sc%d" % (tag, lev))
    write_table(__file__, ("lat", "km", "mean_m", "max_m", "min_m"),
                [(la, round(k, 2), round(m, 1), round(x, 1), round(n, 1)) for la, k, m, x, n in tibet_swath()],
                part="tswath")
    write_table(__file__, ("lon", "km", "mean_m", "max_m", "min_m"),
                [(lo, round(k, 2), round(m, 1), round(x, 1), round(n, 1)) for lo, k, m, x, n in andes_swath()],
                part="aswath")
    write_table(__file__, ("z_km", "p_high_MPa", "p_ref_MPa"),
                [(round(z, 3), round(ph, 2), round(pr, 2)) for z, ph, pr in pressure_profiles(4.8)],
                part="pressure")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")
