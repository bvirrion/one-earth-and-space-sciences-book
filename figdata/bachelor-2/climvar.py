"""Climate variability (Year 2, climate-variability): the ENSO and NAO indices of the NOAA
Climate Prediction Center, and a red-noise model of ocean memory.

  oni          the Oceanic Nino Index (data:b4-oni) and the Relative ONI (data:b4-roni), one
               value per 3-month season from DJF 1950, as fetched on the access date of
               data/MANIFEST.md. The season is plotted at its middle month: t = year + (k +
               0.5)/12 with k = 0 for DJF (January) to 11 for NDJ (December).
  events       El Nino (La Nina) episodes: at least 5 consecutive overlapping seasons with the ONI
               >= +0.5 (<= -0.5) degC, applied as the CPC does to the one-decimal values of its
               own table (data/derived/bachelor-2-oni-table.csv); the two-decimal text file
               does not reproduce that rounding (it would lose three episodes). An episode
               still running at the last season is kept and flagged.
  strong       El Nino episodes whose peak ONI reaches 1.5 degC; intervals between their starts.
  nao          winter (DJF) mean of the monthly standardized NAO index (data:b4-nao), labelled by
               the year of its January, and its centred 5-winter running mean.
  rednoise     a mixed layer of depth h damped at alpha (W m-2 K-1) has the damping time
               tau = rho c_p h / alpha (rho 1025 kg m-3, noaa:seawater-1025; c_p 3991.868
               J kg-1 K-1, teos10:cp0; alpha 16.1, wang24:shff, the mid-latitude mean). The
               anomaly obeys dT/dt = -T/tau + white noise, integrated exactly over daily steps
               (AR(1) with phi = exp(-1 day/tau)), scaled to a standard deviation of 0.5 K. It is
               shown as monthly means against a white series of the same standard deviation;
               the lag autocorrelation of a 2000-year run against exp(-lag/tau).

  part oni        t oni pos neg roni
  part nao        year nao run5
  part rednoise   month white red
  part acf        lag_months theory sample
  part events     kind start_season start_year end_season end_year n peak peak_season peak_year running
  part numbers    key value
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")
SEASONS = "DJF JFM FMA MAM AMJ MJJ JJA JAS ASO SON OND NDJ".split()
RHO, CP, ALPHA = 1025.0, 3991.868, 16.1
DAY = 86400.0


def read_index(name):
    """[(season, year, anomaly)] in file order from data/derived/<name>.csv."""
    with open(os.path.join(DERIVED, name + ".csv"), encoding="utf8") as f:
        return [(r["season"], int(r["year"]), float(r["anom_C"])) for r in csv.DictReader(f)]


def table():
    return read_index("bachelor-2-oni-table")


def season_time(season, year):
    return year + (SEASONS.index(season) + 0.5) / 12.0


def episodes(series, sign, threshold=0.5, nmin=5):
    """Runs of at least nmin consecutive seasons with sign*value >= threshold."""
    out, run = [], []
    for s in list(series) + [None]:
        if s is not None and sign * s[2] >= threshold - 1e-9:
            run.append(s)
            continue
        if len(run) >= nmin:
            out.append(dict(run=run, running=s is None))
        run = []
    for e in out:
        pk = max(e["run"], key=lambda s: sign * s[2])
        e.update(start=e["run"][0], end=e["run"][-1], n=len(e["run"]), peak=pk)
    return out


def strong_intervals(elninos, level=1.5):
    starts = [season_time(e["start"][0], e["start"][1]) for e in elninos
              if e["peak"][2] >= level - 1e-9]
    return starts, [b - a for a, b in zip(starts, starts[1:])]


def nao_winters():
    """{year of January: DJF mean} for the complete winters of the monthly NAO index."""
    m = {}
    with open(os.path.join(DERIVED, "bachelor-2-nao.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            m[(int(r["year"]), int(r["month"]))] = float(r["nao"])
    out = {}
    for y in range(1951, 2100):
        k = [(y - 1, 12), (y, 1), (y, 2)]
        if all(x in m for x in k):
            out[y] = sum(m[x] for x in k) / 3.0
    return out


def running(values, n=5):
    h = n // 2
    return [sum(values[i - h:i + h + 1]) / n if h <= i < len(values) - h else float("nan")
            for i in range(len(values))]


def tau_seconds(h, alpha=ALPHA):
    return RHO * CP * h / alpha


def red_noise(ndays, tau_days, sd=0.5, seed=1):
    """Daily AR(1) series with stationary standard deviation sd."""
    phi = math.exp(-1.0 / tau_days)
    rng = np.random.default_rng(seed)
    e = rng.standard_normal(ndays) * sd * math.sqrt(1.0 - phi * phi)
    x = np.empty(ndays)
    x[0] = rng.standard_normal() * sd
    for i in range(1, ndays):
        x[i] = phi * x[i - 1] + e[i]
    return x


def acf(x, lags):
    x = np.asarray(x) - np.mean(x)
    v = float(np.dot(x, x))
    return [float(np.dot(x[:-k], x[k:]) / v) if k else 1.0 for k in lags]


MONTH = 365.25 / 12.0


def numbers():
    oni = read_index("bachelor-2-oni")
    roni = read_index("bachelor-2-roni")
    en, ln = episodes(table(), 1), episodes(table(), -1)
    starts, gaps = strong_intervals(en)
    tau = tau_seconds(50.0) / DAY
    w = nao_winters()
    last = oni[-1]
    return {"n_elnino": len(en), "n_lanina": len(ln), "n_strong": len(starts),
            "strong_mean_interval": sum(gaps) / len(gaps), "strong_span": starts[-1] - starts[0],
            "tau50_days": tau, "tau100_days": tau_seconds(100.0) / DAY,
            "acf1_theory": math.exp(-MONTH / tau), "last_oni": last[2], "last_roni": roni[-1][2],
            "last_year": last[1], "nao_max": max(w.values()), "nao_min": min(w.values()),
            "n_elnino_roni": len(episodes(roni, 1)), "n_lanina_roni": len(episodes(roni, -1))}


if __name__ == "__main__":
    oni = read_index("bachelor-2-oni")
    roni = {(s, y): a for s, y, a in read_index("bachelor-2-roni")}
    write_table(__file__, ("t", "oni", "pos", "neg", "roni"),
                [(round(season_time(s, y), 4), a, max(a, 0.0), min(a, 0.0), roni[(s, y)])
                 for s, y, a in oni], part="oni")
    w = nao_winters()
    ys = sorted(w)
    r5 = running([w[y] for y in ys])
    write_table(__file__, ("year", "nao", "run5"),
                [(y, round(w[y], 3), round(v, 3) if v == v else "nan") for y, v in zip(ys, r5)],
                part="nao")
    tau = tau_seconds(50.0) / DAY
    nd = int(round(30 * 365.25))
    red = red_noise(nd, tau, seed=1)
    rng = np.random.default_rng(2)
    nm = int(nd / MONTH)
    redm = [float(np.mean(red[int(i * MONTH):int((i + 1) * MONTH)])) for i in range(nm)]
    sdm = float(np.std(redm))
    white = rng.standard_normal(nm) * sdm
    write_table(__file__, ("month", "white", "red"),
                [(i, round(float(white[i]), 4), round(redm[i], 4)) for i in range(nm)],
                part="rednoise")
    long = red_noise(int(2000 * 365.25), tau, seed=3)
    lags = list(range(0, 25))
    sample = acf(long, [int(round(k * MONTH)) for k in lags])
    write_table(__file__, ("lag_months", "theory", "sample"),
                [(k, round(math.exp(-k * MONTH / tau), 4), round(s, 4)) for k, s in zip(lags, sample)],
                part="acf")
    rows = []
    for kind, sign in (("elnino", 1), ("lanina", -1)):
        for e in episodes(table(), sign):
            rows.append((kind, e["start"][0], e["start"][1], e["end"][0], e["end"][1], e["n"],
                         e["peak"][2], e["peak"][0], e["peak"][1], int(e["running"])))
    write_table(__file__, ("kind", "start_season", "start_year", "end_season", "end_year", "n",
                           "peak", "peak_season", "peak_year", "running"), rows, part="events")
    write_table(__file__, ("key", "value"),
                [(k, round(v, 4)) for k, v in sorted(numbers().items())], part="numbers")
