"""The observed records of climate change (grade 12, climate-change).

Reads data/derived/ (tools/fetch_data.py) and writes the plotted tables and the
numbers the chapter prints, all computed here:

  part co2       decimal_year co2_ppm            Mauna Loa monthly means (data:co2-mlo)
  part co2annual year co2_ppm                    annual means
  part temp      year anomaly mean11             GISTEMP global annual anomaly (deg C, base
                                                 1951-1980) and its centred 11-year mean (data:gistemp)
  part sea       decimal_year gmsl_mm            satellite global mean sea level (data:gmsl-lsa)
  part icecore   age_kyr co2_ppm                 Antarctic ice-core CO2, last 800 kyr (data:co2-bereiter)
  part numbers   key value                       the printed numbers (see NUMBERS below)
"""
import collections
import csv
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read(name):
    with open(os.path.join(ROOT, "data", "derived", name + ".csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


def co2_annual():
    return {int(r["year"]): float(r["co2_ppm"]) for r in _read("co2-mlo-annual")}


def co2_rate(y0, y1):
    """Mean growth (ppm per year) between the annual means of y0 and y1."""
    a = co2_annual()
    return (a[y1] - a[y0]) / (y1 - y0)


def seasonal_cycle(y0=2015, y1=2024):
    """Mean monthly departure from the deseasonalised trend, ppm, month -> value."""
    d = collections.defaultdict(list)
    for r in _read("co2-mlo-monthly"):
        if y0 <= int(r["year"]) <= y1:
            d[int(r["month"])].append(float(r["co2_ppm"]) - float(r["co2_deseason_ppm"]))
    return {m: float(np.mean(v)) for m, v in sorted(d.items())}


def temperature():
    return [(int(r["year"]), float(r["anomaly_C_1951_1980"])) for r in _read("gistemp")]


def running_mean(values, half=5):
    out = []
    for i in range(len(values)):
        if i - half < 0 or i + half >= len(values):
            out.append(float("nan"))
        else:
            out.append(float(np.mean(values[i - half:i + half + 1])))
    return out


def mean_anomaly(y0, y1):
    return float(np.mean([a for y, a in temperature() if y0 <= y <= y1]))


def sea_level():
    return [(float(r["decimal_year"]), float(r["gmsl_mm"])) for r in _read("gmsl-altimetry")]


def sea_level_trend():
    t, h = np.array(sea_level()).T
    return float(np.polyfit(t, h, 1)[0])


def icecore():
    return [(float(r["age_yr_bp"]) / 1000.0, float(r["co2_ppm"])) for r in _read("co2-icecore")]


def icecore_range(min_age_kyr=2.0):
    v = [c for a, c in icecore() if a > min_age_kyr]
    return min(v), max(v)


def numbers():
    a = co2_annual()
    sc = seasonal_cycle()
    lo, hi = icecore_range()
    temp = temperature()
    warmest = max(temp, key=lambda t: t[1])
    return {
        "co2_last_year": max(a), "co2_last": a[max(a)],
        "co2_first_year": min(a), "co2_first": a[min(a)],
        "rate_1960s": co2_rate(1960, 1970), "rate_2015_2025": co2_rate(2015, 2025),
        "season_max_month": max(sc, key=sc.get), "season_min_month": min(sc, key=sc.get),
        "season_amplitude": max(sc.values()) - min(sc.values()),
        "icecore_min": lo, "icecore_max": hi,
        "warmest_year": warmest[0], "warmest_anomaly": warmest[1],
        "warming_2011_2020_vs_1880_1900": mean_anomaly(2011, 2020) - mean_anomaly(1880, 1900),
        "sea_trend_mm_a": sea_level_trend(),
    }


if __name__ == "__main__":
    write_table(__file__, ("decimal_year", "co2_ppm"),
                [(float(r["decimal_year"]), float(r["co2_ppm"])) for r in _read("co2-mlo-monthly")], part="co2")
    write_table(__file__, ("year", "co2_ppm"), sorted(co2_annual().items()), part="co2annual")
    temp = temperature()
    m11 = running_mean([a for _, a in temp])
    write_table(__file__, ("year", "anomaly", "mean11"),
                [(y, a, ("nan" if np.isnan(m) else round(m, 3))) for (y, a), m in zip(temp, m11)], part="temp")
    write_table(__file__, ("decimal_year", "gmsl_mm"), sea_level(), part="sea")
    write_table(__file__, ("age_kyr", "co2_ppm"), icecore(), part="icecore")
    write_table(__file__, ("key", "value"),
                [(k, round(v, 3) if isinstance(v, float) else v) for k, v in numbers().items()], part="numbers")
