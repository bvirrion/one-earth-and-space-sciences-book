"""The climate records of grade 9, chapter 1 (the Earth's climate, past and present).

All from the shared datasets (data/derived/, tools/fetch_data.py):
  * GISTEMP v4 global annual temperature anomaly, base 1951-1980 (data:gistemp);
  * Mauna Loa annual mean CO2, 1959-2025 (data:co2-mlo);
  * the Antarctic ice-core CO2 composite, last 800 000 years (data:co2-bereiter);
  * EPICA Dome C temperature anomaly (relative to the mean of the last
    thousand years), last 800 000 years (data:edc-jouzel);
  * satellite global mean sea level since 1993 (data:gmsl-lsa).

The ice-core series are averaged in 2000-year bins so that TeX draws a few
hundred points; the year 2025 is the last complete year used.

  part decades   : label start mean_C       (1880s ... 2010s, then 2020-2025)
  part annual    : year anomaly_C           (every year 1880-2025)
  part periods   : year mean_C              (two segments, the means of 1880-1899 and 2015-2024)
  part co2       : year co2_ppm
  part icecore   : age_kyr co2_ppm          (binned)
  part edc       : age_kyr temp_C           (binned)
  part sea       : year gmsl_mm             (yearly means, 1993-2024 complete years + 2025 partial omitted)
  part sea-trend : year gmsl_mm             (least-squares line)
  main table     : item value               (the numbers printed in the chapter)
"""
import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LAST = 2025
BIN_YR = 2000.0
T_BB_K, T_SURF_K = 254.0, 288.0      # ledger earth:Tbb, earth:Tsurf


def _rows(name):
    with open(os.path.join(ROOT, "data", "derived", name + ".csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


def kelvin_to_celsius(k):
    return k - 273.15


def gistemp():
    return {int(r["year"]): float(r["anomaly_C_1951_1980"]) for r in _rows("gistemp") if int(r["year"]) <= LAST}


def mean_over(series, y0, y1):
    vals = [series[y] for y in range(y0, y1 + 1)]
    return sum(vals) / len(vals)


def decades():
    """[(label, first year, mean anomaly)] for the 1880s ... 2010s, then 2020-2025."""
    t = gistemp()
    out = [("%ds" % d, d, mean_over(t, d, d + 9)) for d in range(1880, 2020, 10)]
    out.append(("2020--25", 2020, mean_over(t, 2020, LAST)))
    return out


def warming(y0, y1, z0, z1):
    """Mean anomaly of years z0..z1 minus that of y0..y1 (deg C)."""
    t = gistemp()
    return mean_over(t, z0, z1) - mean_over(t, y0, y1)


def co2():
    return {int(r["year"]): float(r["co2_ppm"]) for r in _rows("co2-mlo-annual") if int(r["year"]) <= LAST}


def binned(rows, xkey, ykey, width=BIN_YR, xmin=0.0, xmax=800000.0):
    """Mean of y in bins of x (years before present); returns [(kyr, mean)]."""
    sums = {}
    for r in rows:
        x, y = float(r[xkey]), float(r[ykey])
        if xmin <= x < xmax:
            k = int(x // width)
            s = sums.setdefault(k, [0.0, 0])
            s[0] += y
            s[1] += 1
    return [((k + 0.5) * width / 1000.0, s[0] / s[1]) for k, s in sorted(sums.items())]


def icecore_co2():
    return binned(_rows("co2-icecore"), "age_yr_bp", "co2_ppm")


def edc_temperature():
    return binned(_rows("edc-temperature"), "age_yr_bp", "temp_anomaly_C")


def preindustrial_co2_range():
    """Lowest and highest single ice-core values older than 1000 years (ppm)."""
    v = [float(r["co2_ppm"]) for r in _rows("co2-icecore") if float(r["age_yr_bp"]) > 1000]
    return min(v), max(v)


def sea_level_yearly():
    by = {}
    for r in _rows("gmsl-altimetry"):
        y = int(float(r["decimal_year"]))
        by.setdefault(y, []).append(float(r["gmsl_mm"]))
    return [(y, sum(v) / len(v)) for y, v in sorted(by.items()) if 1993 <= y <= 2024]


def fit(points):
    n = len(points)
    mx = sum(x for x, _ in points) / n
    my = sum(y for _, y in points) / n
    a = sum((x - mx) * (y - my) for x, y in points) / sum((x - mx) ** 2 for x, _ in points)
    return a, my - a * mx


def sea_level_rate():
    """mm per year, least squares over every satellite point 1993 to the end of the record."""
    pts = [(float(r["decimal_year"]), float(r["gmsl_mm"])) for r in _rows("gmsl-altimetry")
           if float(r["decimal_year"]) >= 1993.0]
    return fit(pts)


if __name__ == "__main__":
    write_table(__file__, ("label", "start", "mean_C"), [(l, s, round(m, 3)) for l, s, m in decades()],
                part="decades")
    t = gistemp()
    write_table(__file__, ("year", "anomaly_C"), sorted(t.items()), part="annual")
    m0, m1 = mean_over(t, 1880, 1899), mean_over(t, 2015, 2024)
    write_table(__file__, ("year", "mean_C"), [(1880, round(m0, 3)), (1899, round(m0, 3)), ("", ""),
                                               (2015, round(m1, 3)), (2024, round(m1, 3))], part="periods")
    c = co2()
    write_table(__file__, ("year", "co2_ppm"), sorted(c.items()), part="co2")
    write_table(__file__, ("age_kyr", "co2_ppm"), [(round(a, 1), round(v, 1)) for a, v in icecore_co2()],
                part="icecore")
    write_table(__file__, ("age_kyr", "temp_C"), [(round(a, 1), round(v, 2)) for a, v in edc_temperature()],
                part="edc")
    sl = sea_level_yearly()
    write_table(__file__, ("year", "gmsl_mm"), [(y + 0.5, round(v, 1)) for y, v in sl], part="sea")
    a, b = sea_level_rate()
    write_table(__file__, ("year", "gmsl_mm"), [(1993, round(a * 1993 + b, 1)), (2025.1, round(a * 2025.1 + b, 1))],
                part="sea-trend")
    t = gistemp()
    lo, hi = preindustrial_co2_range()
    ed = edc_temperature()
    rows = [("T_bb_C", round(kelvin_to_celsius(T_BB_K), 1)), ("T_surf_C", round(kelvin_to_celsius(T_SURF_K), 1)),
            ("greenhouse_gap_C", T_SURF_K - T_BB_K),
            ("warmest_year", max(t, key=t.get)), ("warmest_value", t[max(t, key=t.get)]),
            ("mean_1880_1899", round(mean_over(t, 1880, 1899), 3)), ("mean_2015_2024", round(mean_over(t, 2015, 2024), 3)),
            ("warming_2015_2024_vs_1880_1899", round(warming(1880, 1899, 2015, 2024), 3)),
            ("co2_1959", c[1959]), ("co2_2025", c[LAST]), ("co2_rise_1959_2025", round(c[LAST] - c[1959], 2)),
            ("co2_rate_1960s", round((c[1969] - c[1959]) / 10, 2)), ("co2_rate_2015_2025", round((c[2025] - c[2015]) / 10, 2)),
            ("icecore_min_ppm", lo), ("icecore_max_ppm", hi),
            ("edc_min_C", round(min(v for _, v in ed), 1)), ("edc_max_C", round(max(v for _, v in ed), 1)),
            ("sea_rate_mm_per_yr", round(a, 2)), ("sea_rise_1993_2024_mm", round(sl[-1][1] - sl[0][1], 1))]
    rows += [("decade_%s" % l, round(m, 2)) for l, _s, m in decades()]
    write_table(__file__, ("item", "value"), rows)
    for r in rows:
        print(r)
