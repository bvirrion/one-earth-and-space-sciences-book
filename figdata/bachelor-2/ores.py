"""Ore deposits (Year 2, ore-deposits): the grade and tonnage of the world's porphyry
copper deposits, and the grade--tonnage curve of a deposit whose grades are log-normal.

  Data: data/derived/bachelor-2-porphyry-cu.csv (ledger data:b4-porphyry-cu), derived by
  tools/fetch_data.py from Singer, Berger and Moring (2008), USGS Open-File Report
  2008-1155, public domain: 422 deposits with tonnage (Mt, total production + reserves +
  resources at the lowest available cut-off) and copper grade (%) both positive.

  hist_t    histogram of log10 tonnage (bins of 0.25 from 0.5 to 5.0) and the count
            expected from the fitted normal distribution of log10 tonnage (same mean and
            standard deviation as the sample), evaluated at the bin centres.
  hist_g    the same for log10 copper grade (bins of 0.1 from -1.2 to 0.6).
  scatter   tonnage and grade of every deposit.
  iso       lines of constant contained copper M = T g / 100 (Mt) for M = 0.1, 1, 10, 100:
            grade = 100 M / T over the tonnage axis (log-spaced, "nan" outside 0.05-5 %).
  gtcurve   the grade--tonnage curve of an illustrative deposit (not a real one): a
            mineralised body of T0 = 1000 Mt whose block grades are log-normal with median
            0.40 % Cu and sigma(ln g) = 0.60. Tonnage above the cut-off c and mean grade
            of that tonnage:
              T(c)    = T0 Phi((mu - ln c)/s)
              gbar(c) = exp(mu + s^2/2) Phi((mu + s^2 - ln c)/s) / Phi((mu - ln c)/s)
            for c from 0.05 to 1.20 %.
  numbers   sample statistics (logs to base 10, population standard deviations).

  part hist_t   log10_t count fit
  part hist_g   log10_g count fit
  part scatter  tonnage_mt cu_pct
  part iso      tonnage_mt g01 g1 g10 g100
  part gtcurve  cutoff_pct tonnage_mt grade_pct metal_mt
  part numbers  key value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")
CSV = os.path.join(DERIVED, "bachelor-2-porphyry-cu.csv")

T0_DEMO, MED_DEMO, S_DEMO = 1000.0, 0.40, 0.60


def read_deposits():
    """(name, tonnage_Mt, cu_pct) of the 422 deposits, file order."""
    out = []
    with open(CSV, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out.append((r["name"], float(r["tonnage_Mt"]), float(r["cu_pct"])))
    return out


def stats(x):
    """Mean and population standard deviation."""
    n = len(x)
    m = sum(x) / n
    return m, math.sqrt(sum((v - m) ** 2 for v in x) / n)


def corr(x, y):
    mx, sx = stats(x)
    my, sy = stats(y)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (len(x) * sx * sy)


def Phi(z):
    return 0.5 * math.erfc(-z / math.sqrt(2.0))


def normal_pdf(x, m, s):
    return math.exp(-0.5 * ((x - m) / s) ** 2) / (s * math.sqrt(2 * math.pi))


def quantile(xs, p):
    """Linear-interpolation quantile (numpy default) of a list."""
    v = sorted(xs)
    h = (len(v) - 1) * p
    i = int(math.floor(h))
    return v[i] if i + 1 >= len(v) else v[i] + (h - i) * (v[i + 1] - v[i])


def histogram(values, lo, width, nbins):
    counts = [0] * nbins
    for v in values:
        k = int(math.floor((v - lo) / width))
        if 0 <= k < nbins:
            counts[k] += 1
    return counts


def tonnage_above(c, t0, med, s):
    """Tonnage with block grade above the cut-off c (log-normal grades)."""
    return t0 * Phi((math.log(med) - math.log(c)) / s)


def grade_above(c, med, s):
    """Mean grade of the blocks above the cut-off c (log-normal grades)."""
    mu = math.log(med)
    return math.exp(mu + s * s / 2) * Phi((mu + s * s - math.log(c)) / s) / Phi((mu - math.log(c)) / s)


def r_factor(c0, d, r):
    """Campbell and Naldrett (1979): metal concentration in the sulfide liquid."""
    return c0 * d * (r + 1) / (r + d)


def log_data():
    deps = read_deposits()
    lt = [math.log10(t) for _, t, _ in deps]
    lg = [math.log10(g) for _, _, g in deps]
    lm = [a + b - 2 for a, b in zip(lt, lg)]
    return deps, lt, lg, lm


def numbers():
    deps, lt, lg, lm = log_data()
    mt, st = stats(lt)
    mg, sg = stats(lg)
    mm, sm = stats(lm)
    rho = corr(lt, lg)
    ts = [t for _, t, _ in deps]
    gs = [g for _, _, g in deps]
    ms = [t * g / 100 for _, t, g in deps]
    return {
        "n": len(deps),
        "mean_log10_t": mt, "sd_log10_t": st, "median_t_fit": 10 ** mt,
        "mean_log10_g": mg, "sd_log10_g": sg, "median_g_fit": 10 ** mg,
        "rho_log": rho,
        "mean_log10_m": mm, "sd_log10_m": sm, "median_m_fit": 10 ** mm,
        "sd_log10_m_prop": math.sqrt(st ** 2 + sg ** 2 + 2 * rho * st * sg),
        "sd_log10_m_indep": math.sqrt(st ** 2 + sg ** 2),
        # deposit percentiles in the USGS sense: the "10th" is exceeded by 10 % of deposits
        "t_p90": quantile(ts, 0.9), "t_p50": quantile(ts, 0.5), "t_p10": quantile(ts, 0.1),
        "g_p90": quantile(gs, 0.9), "g_p50": quantile(gs, 0.5), "g_p10": quantile(gs, 0.1),
        "m_p50": quantile(ms, 0.5), "m_total": sum(ms),
        "frac_above_1gt": sum(1 for t in ts if t >= 1000) / len(ts),
        "demo_t03": tonnage_above(0.3, T0_DEMO, MED_DEMO, S_DEMO),
        "demo_g03": grade_above(0.3, MED_DEMO, S_DEMO),
        "demo_mean_all": MED_DEMO * math.exp(S_DEMO ** 2 / 2),
    }


def main():
    deps, lt, lg, lm = log_data()
    mt, st = stats(lt)
    mg, sg = stats(lg)
    n = len(deps)

    lo, w, nb = 0.5, 0.25, 18
    c = histogram(lt, lo, w, nb)
    rows = [(lo + (k + 0.5) * w, c[k], n * w * normal_pdf(lo + (k + 0.5) * w, mt, st)) for k in range(nb)]
    write_table(__file__, ("log10_t", "count", "fit"), rows, part="hist_t")

    lo, w, nb = -1.2, 0.1, 18
    c = histogram(lg, lo, w, nb)
    rows = [(lo + (k + 0.5) * w, c[k], n * w * normal_pdf(lo + (k + 0.5) * w, mg, sg)) for k in range(nb)]
    write_table(__file__, ("log10_g", "count", "fit"), rows, part="hist_g")

    write_table(__file__, ("tonnage_mt", "cu_pct"), [(t, g) for _, t, g in deps], part="scatter")

    rows = []
    for k in range(0, 61):
        t = 10 ** (0.0 + k * 0.08)  # 1 Mt to 63,000 Mt
        row = [t]
        for m in (0.1, 1, 10, 100):
            g = 100 * m / t
            row.append(g if 0.05 <= g <= 5 else "nan")
        rows.append(tuple(row))
    write_table(__file__, ("tonnage_mt", "g01", "g1", "g10", "g100"), rows, part="iso")

    rows = []
    for k in range(0, 116):
        cut = 0.05 + 0.01 * k
        t = tonnage_above(cut, T0_DEMO, MED_DEMO, S_DEMO)
        g = grade_above(cut, MED_DEMO, S_DEMO)
        rows.append((cut, t, g, t * g / 100))
    write_table(__file__, ("cutoff_pct", "tonnage_mt", "grade_pct", "metal_mt"), rows, part="gtcurve")

    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")


if __name__ == "__main__":
    main()
