"""Reading past climates (grade 12, past-climates): the Antarctic ice-core records, the LR04
ocean record, the Sunda shelf at the Last Glacial Maximum, an invented pollen diagram and the
reference periods of the deep past.

Data (data/derived/, tools/fetch_data.py):
  * EPICA Dome C temperature anomaly, relative to the mean of the last thousand years, EDC3
    age scale (Jouzel et al. 2007; ledger data:edc-jouzel);
  * the Antarctic ice-core CO2 composite (Bereiter et al. 2015; ledger data:co2-bereiter);
  * the LR04 benthic d18O stack, 0-5.32 Ma (Lisiecki and Raymo 2005; ledger data:lr04). The
    derived file data/derived/lr04.csv continues after the stack with two further numeric
    blocks of the raw file (its age column starts again at small values): only the first
    block, up to the first decrease of age, is the stack, and only it is read here;
  * ETOPO1 every 0.1 degree over 11 S-24 N, 92-122 E (ledger data:b2-etopo-sunda) and the
    shared 1-degree grid (data:etopo1);
  * GISTEMP v4 global annual anomaly (data:gistemp), for today's rate of warming.

Sourced constants (ledger rows in the chapter's comments):
  * LGM global mean sea level 125-134 m below present (AR6 WG1 ch. 2, 2.3.3.3, Lambeck et al.
    2014: -134 m at 21 ka); the map uses 130 m, the middle of the range, over today's sea
    floor (the floor itself has moved a little since, which the caption says);
  * LGM 23-19 ka, Last Deglacial Transition (LDT) 18-11 ka; LGM global surface temperature
    5-7 degC below 1850-1900 (AR6 ch. 2 Cross-Chapter Box 2.1 and 2.3.1.1.1); the mean rate
    over the LDT is computed as 6 degC over 7000 years;
  * the reference periods of AR6 ch. 2, Figure 2.34 (DEEP below).

The pollen diagram is invented exercise data (a lake of the Varden Hills, the series' invented
region), said so in its caption; the succession it shows (open herbs, then birch, pine, hazel
and oak) is the textbook one.

  part edc        age_kyr temp_C              Dome C, 2-kyr means, 0-800 kyr
  part co2        age_kyr co2_ppm             CO2, 2-kyr means, 0-800 kyr
  part pairs      temp_C co2_ppm              each CO2 sample (2-800 kyr) with the Dome C
                                              temperature at its age, interpolated
  part fit        temp_C co2_ppm              the least-squares line through the pairs
  part edc30      age_kyr temp_C              Dome C, every sample, 0-30 kyr
  part co230      age_kyr co2_ppm             CO2, every sample, 0-30 kyr
  part lr04       age_Ma d18O                 the stack, every sample, 0-5.32 Ma
  part lr04mean   age_Ma d18O                 the means of 0-1 Ma and 3-5.32 Ma, as segments
  part pollen     depth_cm age_ka herbs birch pine hazel oak   (percent, invented)
  part pol-<taxon> pct depth_cm               the closed outline of one taxon's curve, for filling
  part deep       idx name age tlo thi co2lo co2hi slo shi      AR6 reference periods
  part numbers    key value
The map: grade-12-ice_age_records-sunda.png (one pixel per 0.1 degree, north up).
"""
import csv
import math
import os
import struct
import sys
import zlib

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import out_path, write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
DERIVED = os.path.join(ROOT, "data", "derived")
EARTH_RADIUS_KM = 6371.0                      # ledger earth:Rmean
KM_PER_DEG = math.pi * EARTH_RADIUS_KM / 180.0

LGM = (23.0, 19.0)                            # ka, AR6 Cross-Chapter Box 2.1
LDT = (18.0, 11.0)
LGM_GLOBAL_COOLING = (5.0, 7.0)               # degC below 1850-1900, AR6 2.3.1.1.1
LDT_FAST_RATE = (1.0, 1.5)                    # degC per kyr, rapid warming, AR6 2.3.1.1.1
LOWSTAND_M = 130.0                            # middle of 125-134 m, AR6 2.3.3.3
EARLY_HOLOCENE = (11.0, 9.0)                  # ka, the 2000 years after the LDT

# AR6 WG1 ch. 2, Figure 2.34: (name, age label, temperature range relative to 1850-1900,
# CO2 range in ppm, sea level range relative to 1900 in m); None = not given there.
DEEP = (("PETM", "56 Ma", (10.0, 25.0), (900.0, 2000.0), None),
        ("EECO", "53-49 Ma", (10.0, 18.0), (1150.0, 2500.0), (70.0, 76.0)),
        ("MPWP", "3.3-3.0 Ma", (2.5, 4.0), (360.0, 420.0), (5.0, 25.0)),
        ("LIG", "129-116 ka", (0.5, 1.5), (266.0, 282.0), (5.0, 10.0)),
        ("LGM", "23-19 ka", (-7.0, -5.0), (188.0, 194.0), (-134.0, -125.0)),
        ("MH", "6.5-5.5 ka", (0.2, 1.0), (260.0, 268.0), (-3.5, 0.5)))

# invented pollen counts for a lake core of the Varden Hills (percent of the tree and herb
# pollen of each level); ages from an invented, smooth depth-age line
POLLEN_DEPTHS = (600, 580, 560, 540, 520, 500, 480, 460, 440, 420, 400, 380, 360, 340, 320, 300)
POLLEN = {  # depth: (herbs, birch, pine, hazel, oak)
    600: (86, 8, 5, 1, 0), 580: (84, 10, 5, 1, 0), 560: (80, 13, 6, 1, 0),
    540: (62, 28, 8, 2, 0), 520: (40, 46, 11, 3, 0), 500: (28, 52, 16, 4, 0),
    480: (20, 44, 30, 6, 0), 460: (14, 30, 46, 8, 2), 440: (10, 20, 50, 16, 4),
    420: (8, 12, 38, 32, 10), 400: (7, 8, 26, 39, 20), 380: (6, 7, 18, 38, 31),
    360: (6, 6, 14, 36, 38), 340: (6, 6, 12, 34, 42), 320: (7, 6, 12, 33, 42),
    300: (8, 6, 12, 32, 42)}
POLLEN_AGE = {600: 14.0, 300: 6.0}            # ka at the bottom and top, linear between


def _read(name):
    with open(os.path.join(DERIVED, name + ".csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


def edc():
    return np.array([(float(r["age_yr_bp"]) / 1000.0, float(r["temp_anomaly_C"]))
                     for r in _read("edc-temperature")])


def co2():
    return np.array([(float(r["age_yr_bp"]) / 1000.0, float(r["co2_ppm"]))
                     for r in _read("co2-icecore")])


def lr04():
    """The LR04 stack only: rows up to the first decrease of age (see the docstring)."""
    rows, prev = [], -1.0
    for r in _read("lr04"):
        a = float(r["age_ka"])
        if a < prev:
            break
        rows.append((a / 1000.0, float(r["d18O_permil"])))
        prev = a
    return np.array(rows)


def gistemp():
    return np.array([(int(r["year"]), float(r["anomaly_C_1951_1980"])) for r in _read("gistemp")])


def bins(rec, width=2.0, top=800.0):
    out = []
    for a in np.arange(0.0, top, width):
        s = (rec[:, 0] >= a) & (rec[:, 0] < a + width)
        if s.any():
            out.append((a + width / 2, float(rec[s, 1].mean())))
    return out


def pairs(min_age=2.0, max_age=800.0):
    e, c = edc(), co2()
    s = (c[:, 0] > min_age) & (c[:, 0] <= max_age)
    return np.interp(c[s, 0], e[:, 0], e[:, 1]), c[s, 1]


def correlation():
    t, c = pairs()
    return float(np.corrcoef(t, c)[0, 1])


def fit():
    t, c = pairs()
    b, a = np.polyfit(t, c, 1)
    return float(a), float(b)


def window_mean(rec, older, younger):
    s = (rec[:, 0] <= older) & (rec[:, 0] >= younger)
    return float(rec[s, 1].mean())


def dominant_period(rec, lo, hi, step=1.0, pmin=15.0, pmax=200.0):
    """Period (kyr) of the largest peak of the periodogram of a record (age in kyr) between lo
    and hi, interpolated to a regular step and detrended."""
    t = np.arange(lo, hi + step / 2, step)
    y = np.interp(t, rec[:, 0], rec[:, 1])
    y = y - np.polyval(np.polyfit(t, y, 1), t)
    periods = np.arange(pmin, pmax + 0.25, 0.5)
    power = [abs(np.sum(y * np.exp(-2j * np.pi * t / p))) ** 2 for p in periods]
    return float(periods[int(np.argmax(power))])


def warming_rate_today(y0=1970, y1=2025):
    g = gistemp()
    s = (g[:, 0] >= y0) & (g[:, 0] <= y1)
    return float(np.polyfit(g[s, 0], g[s, 1], 1)[0])     # degC per year


def sunda():
    """lat, lon, elevation arrays of the regional grid (north first)."""
    rows = [(float(r["lat"]), float(r["lon"]), float(r["elev_m"])) for r in _read("grade-12-etopo-sunda")]
    lats = sorted({r[0] for r in rows}, reverse=True)
    lons = sorted({r[1] for r in rows})
    li = {v: i for i, v in enumerate(lats)}
    lo = {v: i for i, v in enumerate(lons)}
    z = np.zeros((len(lats), len(lons)))
    for la, ln, h in rows:
        z[li[la], lo[ln]] = h
    return np.array(lats), np.array(lons), z


def land_areas(lats, z, step_deg, lowstand=LOWSTAND_M):
    """Area (km2) above today's sea level and above a sea level lowered by `lowstand`."""
    cell = (step_deg * KM_PER_DEG) ** 2 * np.cos(np.radians(lats))[:, None] * np.ones_like(z)
    return float(cell[z > 0].sum()), float(cell[z > -lowstand].sum())


def world_areas():
    rows = [(float(r["lat"]), float(r["lon"]), float(r["elev_m"])) for r in _read("etopo-1deg")]
    lats = np.array([r[0] for r in rows])
    z = np.array([r[2] for r in rows])
    cell = KM_PER_DEG ** 2 * np.cos(np.radians(lats))
    total = float(cell.sum())
    return total, float(cell[z > 0].sum()), float(cell[z > -LOWSTAND_M].sum())


def pollen_rows():
    a0, a1 = POLLEN_AGE[600], POLLEN_AGE[300]
    out = []
    for d in POLLEN_DEPTHS:
        age = a1 + (a0 - a1) * (d - 300) / 300.0
        out.append((d, age) + POLLEN[d])
    return out


TAXA = ("herbs", "birch", "pine", "hazel", "oak")


def pollen_outline(k):
    """Closed polygon of taxon k: down the curve, back up the zero line."""
    pts = [(POLLEN[d][k], d) for d in POLLEN_DEPTHS]
    return [(0, POLLEN_DEPTHS[0])] + pts + [(0, POLLEN_DEPTHS[-1]), (0, POLLEN_DEPTHS[0])]


def png(path, width, height, rgb_rows):
    raw = b"".join(b"\x00" + bytes(row) for row in rgb_rows)

    def chunk(tag, data):
        return (struct.pack(">I", len(data)) + tag + data
                + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff))
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)))
        f.write(chunk(b"IDAT", zlib.compress(raw, 9)))
        f.write(chunk(b"IEND", b""))


SEA, SHELF, LAND = (207, 230, 245), (232, 201, 138), (156, 201, 138)


def sunda_raster(z, lowstand=LOWSTAND_M):
    rows = []
    for line in z:
        row = []
        for h in line:
            row.extend(LAND if h > 0 else SHELF if h > -lowstand else SEA)
        rows.append(row)
    return rows


def link_level(lats, lons, z, a, b):
    """Highest elevation on the best 8-neighbour path of grid points between
    places a and b (lat, lon): the sea must fall below minus this depth to
    join them by land (a minimax path, Dijkstra on the lowest point met)."""
    import heapq

    def idx(p):
        return int(np.argmin(abs(lats - p[0]))), int(np.argmin(abs(lons - p[1])))

    ny, nx = z.shape
    best = np.full(z.shape, -1e9)
    s, t = idx(a), idx(b)
    best[s] = z[s]
    heap = [(-z[s], s)]
    while heap:
        v, (i, j) = heapq.heappop(heap)
        v = -v
        if (i, j) == t:
            return float(v)
        if v < best[i, j]:
            continue
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                k, m = i + di, j + dj
                if 0 <= k < ny and 0 <= m < nx:
                    w = min(v, z[k, m])
                    if w > best[k, m]:
                        best[k, m] = w
                        heapq.heappush(heap, (-w, (k, m)))
    raise ValueError("no path")


# points inland of each landmass on the 0.1-degree grid (invented sampling points)
BORNEO, MALAYA, SUMATRA, JAVA = (0.5, 114.0), (4.0, 102.0), (-1.0, 102.0), (-7.3, 110.0)


def numbers():
    n = {}
    e, c = edc(), co2()
    n["r_temp_co2"] = correlation()
    a, b = fit()
    n["fit_intercept_ppm"], n["fit_slope_ppm_per_C"] = a, b
    n["n_pairs"] = len(pairs()[0])
    n["edc_min_C"], n["edc_max_C"] = float(e[:, 1].min()), float(e[:, 1].max())
    n["edc_min_age_kyr"] = float(e[int(e[:, 1].argmin()), 0])
    n["edc_max_age_kyr"] = float(e[int(e[:, 1].argmax()), 0])
    old = c[(c[:, 0] > 2.0)]
    n["co2_min_ppm"], n["co2_max_ppm"] = float(old[:, 1].min()), float(old[:, 1].max())
    n["edc_lgm_C"] = window_mean(e, *LGM)
    n["edc_holo_C"] = window_mean(e, *EARLY_HOLOCENE)
    n["co2_lgm_ppm"] = window_mean(c, *LGM)
    n["co2_holo_ppm"] = window_mean(c, *EARLY_HOLOCENE)
    n["edc_rise_C"] = n["edc_holo_C"] - n["edc_lgm_C"]
    n["co2_rise_ppm"] = n["co2_holo_ppm"] - n["co2_lgm_ppm"]
    n["edc_period_kyr"] = dominant_period(e, 1.0, 799.0)
    lr = lr04()
    lk = np.column_stack((lr[:, 0] * 1000.0, lr[:, 1]))
    n["lr04_period_0_700"] = dominant_period(lk, 0.0, 700.0)
    n["lr04_period_1300_2600"] = dominant_period(lk, 1300.0, 2600.0)
    n["lr04_mean_0_1Ma"] = window_mean(lr, 1.0, 0.0)
    n["lr04_mean_3_5Ma"] = window_mean(lr, 5.32, 3.0)
    n["lr04_lgm"] = window_mean(lr, 0.023, 0.019)
    n["lr04_today"] = float(lr[0, 1])
    # rates: global, over the LDT, from the AR6 central LGM cooling; today's from GISTEMP
    n["ldt_mean_rate_C_per_kyr"] = 0.5 * sum(LGM_GLOBAL_COOLING) / (LDT[0] - LDT[1])
    n["rate_1970_2025_C_per_decade"] = warming_rate_today() * 10.0
    n["rate_1970_2025_C_per_kyr"] = warming_rate_today() * 1000.0
    n["ratio_today_ldt_mean"] = n["rate_1970_2025_C_per_kyr"] / n["ldt_mean_rate_C_per_kyr"]
    n["ratio_today_ldt_fast_lo"] = n["rate_1970_2025_C_per_kyr"] / LDT_FAST_RATE[1]
    n["ratio_today_ldt_fast_hi"] = n["rate_1970_2025_C_per_kyr"] / LDT_FAST_RATE[0]
    lats, lons, z = sunda()
    now, lgm = land_areas(lats, z, 0.1)
    n["sunda_land_now_km2"], n["sunda_land_lgm_km2"] = now, lgm
    n["sunda_gain_km2"] = lgm - now
    n["sunda_ratio"] = lgm / now
    n["borneo_link_m"] = link_level(lats, lons, z, BORNEO, MALAYA)
    n["sumatra_link_m"] = link_level(lats, lons, z, SUMATRA, MALAYA)
    n["java_link_m"] = link_level(lats, lons, z, JAVA, MALAYA)
    total, wnow, wlgm = world_areas()
    n["world_land_now_frac"] = wnow / total
    n["world_land_lgm_frac"] = wlgm / total
    n["world_gain_km2"] = wlgm - wnow
    return n


if __name__ == "__main__":
    e, c = edc(), co2()
    write_table(__file__, ("age_kyr", "temp_C"), bins(e), part="edc", digits=5)
    write_table(__file__, ("age_kyr", "co2_ppm"), bins(c), part="co2", digits=5)
    t, cc = pairs()
    write_table(__file__, ("temp_C", "co2_ppm"), list(zip(t, cc)), part="pairs", digits=5)
    a, b = fit()
    write_table(__file__, ("temp_C", "co2_ppm"), [(-11.0, a - 11.0 * b), (5.0, a + 5.0 * b)],
                part="fit", digits=5)
    write_table(__file__, ("age_kyr", "temp_C"), [tuple(r) for r in e if r[0] <= 30.0], part="edc30", digits=5)
    write_table(__file__, ("age_kyr", "co2_ppm"), [tuple(r) for r in c if 0.0 <= r[0] <= 30.0],
                part="co230", digits=5)
    lr = lr04()
    write_table(__file__, ("age_Ma", "d18O"), [tuple(r) for r in lr], part="lr04", digits=5)
    n = numbers()
    write_table(__file__, ("age_Ma", "d18O"),
                [(0.0, n["lr04_mean_0_1Ma"]), (1.0, n["lr04_mean_0_1Ma"]), ("nan", "nan"),
                 (3.0, n["lr04_mean_3_5Ma"]), (5.32, n["lr04_mean_3_5Ma"])], part="lr04mean", digits=5)
    write_table(__file__, ("depth_cm", "age_ka", "herbs", "birch", "pine", "hazel", "oak"),
                pollen_rows(), part="pollen")
    for k, taxon in enumerate(TAXA):
        write_table(__file__, ("pct", "depth_cm"), pollen_outline(k), part="pol-" + taxon)
    deep = []
    for i, (nm, age, tr, cr, sr) in enumerate(DEEP, 1):
        sl = sr if sr else ("nan", "nan")
        deep.append((i, nm, age.replace(" ", "~"), tr[0], tr[1], cr[0], cr[1], sl[0], sl[1]))
    write_table(__file__, ("idx", "name", "age", "tlo", "thi", "co2lo", "co2hi", "slo", "shi"),
                deep, part="deep")
    write_table(__file__, ("key", "value"), sorted(n.items()), part="numbers", digits=6)
    lats, lons, z = sunda()
    png(out_path(__file__, part="sunda", ext=".png"), len(lons), len(lats), sunda_raster(z))
