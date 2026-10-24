"""Tests of figdata/bachelor-2/labmethods.py (Year 2, field-lab-methods-2)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import labmethods as L  # noqa: E402


def test_binomial_counting():
    # sigma = sqrt(p(1-p)/n), and the inverse formula gives back n
    assert abs(L.binomial_sigma(0.3, 500) - math.sqrt(0.21 / 500)) < 1e-15
    assert abs(L.points_needed(0.3, L.binomial_sigma(0.3, 500)) - 500) < 1e-9
    # quadrupling n halves the error; rare phases have the larger relative error
    assert abs(L.relative_error(0.2, 400) / L.relative_error(0.2, 1600) - 2) < 1e-12
    assert L.relative_error(0.05, 1000) > L.relative_error(0.5, 1000)
    # Monte Carlo check of the binomial standard error (fixed seed, pure python)
    import random
    rng = random.Random(31)
    p, n, trials = 0.2, 400, 4000
    est = [sum(rng.random() < p for _ in range(n)) / n for _ in range(trials)]
    m = sum(est) / trials
    sd = math.sqrt(sum((e - m) ** 2 for e in est) / (trials - 1))
    assert abs(sd / L.binomial_sigma(p, n) - 1) < 0.05


def test_xrf_table():
    assert len(L.XRF_SIO2) == 10
    for name, rec, meas, s in L.XRF_SIO2:
        # USGS Table 2: every SiO2 result within 1 wt% of the recommended value
        assert abs(meas - rec) < 1.0 and 0 < s < 0.25, name
    a, b = L.least_squares([1, 2, 3], [3, 5, 7])
    assert abs(a - 2) < 1e-12 and abs(b - 1) < 1e-12


def test_isotope_dilution_roundtrip():
    # forward-model a mixture, then recover the sample amount exactly
    n_s86, n_x86, r_s, r_x, r_m = L.id_example()
    assert abs(L.id_moles(n_s86, r_s, r_x, r_m) / n_x86 - 1) < 1e-12
    # the natural and spike 84/86 ratios
    assert abs(r_x - 0.0056 / 0.0986) < 1e-12
    assert abs(r_s - 561.4 / 0.7661) < 1e-9
    # spike isotope fractions sum to one and the spike is almost pure 84Sr
    assert abs(sum(L.spike_fraction(i) for i in (84, 86, 87, 88)) - 1) < 1e-12
    assert L.spike_fraction(84) > 0.996


def test_error_magnification_optimum():
    r_s, r_x = 732.8, 0.0568
    opt = math.sqrt(r_s * r_x)
    best = L.error_magnification(r_s, r_x, opt)
    for f in (0.3, 0.7, 1.5, 3.0):
        assert L.error_magnification(r_s, r_x, opt * f) > best
    # it is close to 1 at the optimum when the two end-members are far apart
    assert 1.0 < best < 1.05


def test_exponential_law():
    # a measured 86/88 equal to the reference gives no correction
    assert abs(L.exp_law_beta(0.1194)) < 1e-12
    # a light-isotope deficit (measured 86/88 low) also inflates 87/86: corrected downwards
    beta = L.exp_law_beta(0.11853)
    corr = L.exp_law_correct(0.71655, L.MASS[87], L.MASS[86], beta)
    assert beta < 0 and corr < 0.71655
    # self-consistency: correcting the normalising ratio returns the reference
    assert abs(L.exp_law_correct(0.11853, L.MASS[86], L.MASS[88], beta) - 0.1194) < 1e-12


def test_traverse_stations():
    st = L.stations()
    assert len(st) == 30
    units = {u for *_, u in st}
    # both traverses cross the granite of the basement inlier
    assert 2 in units and sum(1 for *_, u in st if u == 2) >= 8
    for x, y, z, u in st:
        assert 2800 <= x <= 4200 and y in (3700.0, 4400.0) and 100 < z < 300
