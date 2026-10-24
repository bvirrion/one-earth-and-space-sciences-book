"""Tests of figdata/bachelor-2/ores.py (Year 2, ore-deposits)."""
import math
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import ores  # noqa: E402


def test_dataset_matches_usgs_table1():
    # Singer, Berger and Moring (2008), Table 1, general porphyry Cu, n = 422:
    # tonnage 1500 / 240 / 33 Mt and Cu 0.75 / 0.44 / 0.24 % at the 10th / 50th / 90th
    # percentiles of deposits (the "10th" exceeded by 10 % of deposits); r = 0.1
    n = ores.numbers()
    assert n["n"] == 422
    assert abs(n["t_p90"] - 1500) / 1500 < 0.05
    assert abs(n["t_p50"] - 240) / 240 < 0.03
    assert abs(n["t_p10"] - 33) / 33 < 0.05
    assert abs(n["g_p50"] - 0.44) < 1e-9 and abs(n["g_p90"] - 0.75) < 1e-9
    assert abs(n["g_p10"] - 0.24) <= 0.011
    assert abs(n["rho_log"] - 0.1) < 0.01


def test_product_of_lognormals():
    # the log of contained metal is the sum of the logs: its variance obeys the proposition
    n = ores.numbers()
    assert abs(n["mean_log10_m"] - (n["mean_log10_t"] + n["mean_log10_g"] - 2)) < 1e-12
    assert abs(n["sd_log10_m"] - n["sd_log10_m_prop"]) < 1e-9
    assert n["sd_log10_m_prop"] > n["sd_log10_m_indep"]  # positive correlation widens it
    # Monte Carlo of independent log-normals: the product's log is normal with summed variance
    rng = random.Random(1)
    xs = [rng.gauss(0, 0.6) + rng.gauss(0, 0.2) for _ in range(20000)]
    m, s = ores.stats(xs)
    assert abs(m) < 0.02 and abs(s - math.sqrt(0.6 ** 2 + 0.2 ** 2)) < 0.01


def test_grade_tonnage_curve():
    t0, med, s = 1000.0, 0.4, 0.6
    # zero cut-off keeps all the tonnage at the mean grade median * exp(s^2/2)
    assert abs(ores.tonnage_above(1e-9, t0, med, s) - t0) < 1e-6
    assert abs(ores.grade_above(1e-9, med, s) - med * math.exp(s * s / 2)) < 1e-9
    # half the tonnage lies above the median grade
    assert abs(ores.tonnage_above(med, t0, med, s) - t0 / 2) < 1e-9
    # tonnage falls and mean grade rises with the cut-off; mean grade exceeds the cut-off
    cs = [0.1, 0.2, 0.3, 0.5, 0.8]
    ts = [ores.tonnage_above(c, t0, med, s) for c in cs]
    gs = [ores.grade_above(c, med, s) for c in cs]
    assert all(a > b for a, b in zip(ts, ts[1:])) and all(a < b for a, b in zip(gs, gs[1:]))
    assert all(g > c for g, c in zip(gs, cs))
    # numerical check of the partial expectation
    mu = math.log(med)
    c = 0.3
    acc_t = acc_m = 0.0
    dz = 1e-3
    z = (math.log(c) - mu) / s
    while z < 10:
        p = math.exp(-z * z / 2) / math.sqrt(2 * math.pi) * dz
        acc_t += p
        acc_m += p * math.exp(mu + s * (z + dz / 2))
        z += dz
    assert abs(acc_m / acc_t - ores.grade_above(c, med, s)) < 2e-3


def test_r_factor_limits():
    c0, d = 100.0, 1000.0
    # large R: the sulfide reaches equilibrium with an infinite magma, C = D C0
    assert abs(ores.r_factor(c0, d, 1e9) - d * c0) / (d * c0) < 1e-5
    # small R << D: the sulfide takes nearly all the metal of its R units of magma
    assert abs(ores.r_factor(c0, d, 10) - c0 * 11 * d / 1010) < 1e-9
    assert ores.r_factor(c0, d, 10) < (10 + 1) * c0
    # mass balance: (R + 1) C0 = R C_sil + C_sul with C_sil = C_sul / D
    r = 500.0
    cs = ores.r_factor(c0, d, r)
    assert abs((r + 1) * c0 - (r * cs / d + cs)) < 1e-9


def test_histograms_sum():
    deps, lt, lg, _ = ores.log_data()
    assert sum(ores.histogram(lt, 0.5, 0.25, 18)) == len(lt)
    assert sum(ores.histogram(lg, -1.2, 0.1, 18)) == len(lg)
