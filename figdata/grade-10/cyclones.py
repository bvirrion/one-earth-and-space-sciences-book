"""Tropical-cyclone tracks, genesis points and the pressure--wind relation from
IBTrACS; thunder, surge and hurricane-energy numbers (grade 10,
storms-and-cyclones).

Sources (ledger): IBTrACS v04r01 (data:b2-ibtracs; derived tables
data/derived/grade-10-ibtracs*.csv written by tools/fetch_data.py); the
Saffir-Simpson thresholds (nhc:sshws); the AOML energy estimate
(aoml:energy); seawater density 1025 kg/m3 (noaa:seawater-1025); const:R,
const:gn, earth:Mmol for the speed of sound sqrt(gamma R T / M) with
gamma = 7/5 (ideal diatomic gas, admitted).

  part tracks    lon lat           tracks of the 2015-2024 seasons, daily, a nan row between storms
  part genesis   lon lat           where each storm of 1980-2024 first reached 34 kt (tropical storm)
  part scatter   wind_ms pmin_hpa  lifetime maximum wind and minimum pressure, 2000-2024
  part fit       wind_ms pmin_hpa  least-squares line through the scatter
  part numbers   key value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DERIVED = os.path.join(ROOT, "data", "derived")
KT = 1852.0 / 3600.0            # m/s per knot (exact)
SSHWS_KT = (64, 83, 96, 113, 137)   # nhc:sshws
R, G, M_AIR = 8.314462618, 9.80665, 28.97e-3
RHO_SEA = 1025.0                # noaa:seawater-1025
L_V = 2.5e6                     # J/kg, nist:water-latent (2.50 MJ/kg at 0 degC, rounded)
AOML_RAIN_CM, AOML_RADIUS_KM, AOML_KE_W = 1.5, 665.0, 1.5e12   # aoml:energy


def storms():
    with open(os.path.join(DERIVED, "grade-10-ibtracs-storms.csv"), encoding="utf8") as f:
        out = []
        for r in csv.DictReader(f):
            out.append(dict(sid=r["sid"], season=int(r["season"]), basin=r["basin"], name=r["name"],
                            lat0=float(r["lat34"]), lon0=float(r["lon34"]), wmax=float(r["wmax_kt"]),
                            pmin=float(r["pmin_hpa"]) if r["pmin_hpa"] else None))
        return out


def positions():
    tracks = {}
    with open(os.path.join(DERIVED, "grade-10-ibtracs.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            tracks.setdefault(r["sid"], (int(r["season"]), []))[1].append((float(r["lon"]), float(r["lat"])))
    return tracks


def split_dateline(points):
    out, cur = [], []
    for p in points:
        if cur and abs(p[0] - cur[-1][0]) > 180:
            out.append(cur)
            cur = []
        cur.append(p)
    if cur:
        out.append(cur)
    return out


def category(w_kt):
    c = 0
    for i, t in enumerate(SSHWS_KT):
        if w_kt >= t:
            c = i + 1
    return c


def fit(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my - b * mx, b


def speed_of_sound(t_c):
    return math.sqrt(1.4 * R * (t_c + 273.15) / M_AIR)


def surge_per_hpa():
    return 100.0 / (RHO_SEA * G)            # metres of water per hPa


def numbers():
    st = storms()
    n = {}
    full = [s for s in st if 1980 <= s["season"] <= 2024]
    n["storms_1980_2024"] = len(full)
    n["per_year_1991_2020"] = sum(1 for s in st if 1991 <= s["season"] <= 2020) / 30.0
    n["hurricane_share"] = sum(1 for s in full if s["wmax"] >= 64) / len(full)
    n["nh_share"] = sum(1 for s in full if s["lat0"] > 0) / len(full)
    n["genesis_within_5deg"] = sum(1 for s in full if abs(s["lat0"]) < 5)
    n["genesis_within_10deg"] = sum(1 for s in full if abs(s["lat0"]) < 10)
    n["genesis_beyond_30deg"] = sum(1 for s in full if abs(s["lat0"]) > 30)
    n["genesis_share_10_30deg"] = sum(1 for s in full if 10 <= abs(s["lat0"]) <= 30) / len(full)
    n["south_atlantic_genesis"] = sum(1 for s in full if s["lat0"] < 0 and -70 < s["lon0"] < 20)
    n["cat5_count"] = sum(1 for s in full if s["wmax"] >= 137)
    lowest = min((s for s in full if s["pmin"]), key=lambda s: s["pmin"])
    n["lowest_pressure"] = lowest["pmin"]
    n["lowest_pressure_season"] = lowest["season"]
    strongest = max(full, key=lambda s: s["wmax"])
    n["max_wind_kt"] = strongest["wmax"]
    n["max_wind_ms"] = strongest["wmax"] * KT
    n["max_wind_season"] = strongest["season"]
    sc = [(s["wmax"] * KT, s["pmin"]) for s in st if 2000 <= s["season"] <= 2024 and s["pmin"] and s["pmin"] > 850]
    a, b = fit([x for x, _ in sc], [y for _, y in sc])
    n["fit_intercept"], n["fit_slope"] = a, b
    n["fit_p_at_70ms"] = a + b * 70
    for i, t in enumerate(SSHWS_KT):
        n["sshws_%d_ms" % (i + 1)] = t * KT
        n["sshws_%d_kmh" % (i + 1)] = t * KT * 3.6
    for t in (0, 20, 30):
        n["sound_%d" % t] = speed_of_sound(t)
    n["surge_cm_per_hpa"] = surge_per_hpa() * 100
    area = math.pi * (AOML_RADIUS_KM * 1e3) ** 2
    vol = AOML_RAIN_CM / 100 * area
    n["rain_area_m2"] = area
    n["rain_volume_m3"] = vol
    n["rain_mass_kg"] = vol * 1000
    n["latent_J_day"] = vol * 1000 * L_V
    n["latent_W"] = n["latent_J_day"] / 86400
    n["ke_W"] = AOML_KE_W
    n["efficiency_ratio"] = n["latent_W"] / AOML_KE_W
    n["air_density_1000hPa_300K"] = 1e5 * M_AIR / (R * 300.0)
    return n


if __name__ == "__main__":
    tr = positions()
    rows = []
    for sid, (season, pts) in tr.items():
        if 2015 <= season <= 2024:
            for piece in split_dateline(pts):
                if len(piece) < 2:
                    continue
                if rows:
                    rows.append(("nan", "nan"))   # a jump (unbounded coords=jump); a blank
                rows += piece                     # line makes pgfplots log nullfont noise
    write_table(__file__, ("lon", "lat"), rows, part="tracks", digits=5)
    st = storms()
    write_table(__file__, ("lon", "lat"), [(s["lon0"], s["lat0"]) for s in st if 1980 <= s["season"] <= 2024],
                part="genesis", digits=5)
    sc = [(s["wmax"] * KT, s["pmin"]) for s in st if 2000 <= s["season"] <= 2024 and s["pmin"] and s["pmin"] > 850]
    write_table(__file__, ("wind_ms", "pmin_hpa"), sc, part="scatter", digits=5)
    a, b = fit([x for x, _ in sc], [y for _, y in sc])
    write_table(__file__, ("wind_ms", "pmin_hpa"), [(x, a + b * x) for x in (17, 85)], part="fit", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=7)
