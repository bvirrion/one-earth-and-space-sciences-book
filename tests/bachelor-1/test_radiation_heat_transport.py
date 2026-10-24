"""Tests for the radiation-heat-transport figures: daily-mean insolation by latitude
and season, and the zonal radiation budget with the implied poleward heat transport."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import insolation as ins  # noqa: E402
import energy_balance as eb  # noqa: E402
import _solar  # noqa: E402


# ------------------------------------------------------------ insolation
def test_equator_at_equinox_is_s0_over_pi():
    t = _solar.T_EQUINOX
    f = (1.0 / _solar.distance_ratio(t)) ** 2
    assert abs(math.degrees(_solar.declination(t))) < 0.01
    assert abs(ins.daily_mean(0.0, t) - ins.S0 / math.pi * f) < 0.05
    assert abs(ins.daily_mean(0.0, t, s0=1.0) * math.pi / f - 1) < 1e-3


def test_daily_mean_formula_matches_brute_force():
    for lat in (-80.0, -45.0, 0.0, 23.0, 40.0, 66.0, 70.0, 89.0):
        for t in (10.0, 80.0, 171.4, 250.0, 354.9):
            assert abs(ins.daily_mean(lat, t) - ins.instantaneous_mean(lat, t, n=4000)) < 0.05


def test_pole_at_solstice_exceeds_equator():
    tj, td = ins.solstice_days()
    assert ins.daily_mean(90.0, tj) > ins.daily_mean(0.0, tj) * 1.3
    assert ins.daily_mean(-90.0, td) > ins.daily_mean(90.0, tj)   # perihelion in January
    # at the pole the daily mean is S0 (a/r)^2 sin(delta)
    d = _solar.declination(tj)
    f = (1.0 / _solar.distance_ratio(tj)) ** 2
    assert abs(ins.daily_mean(90.0, tj) - ins.S0 * f * math.sin(d)) < 0.01


def test_polar_night_is_dark():
    tj, td = ins.solstice_days()
    assert ins.daily_mean(80.0, td) == 0.0
    assert ins.daily_mean(-70.0, tj) == 0.0
    n, s = ins.polar_night_edge(td)
    assert abs(n - (90 + math.degrees(_solar.declination(td)))) < 1e-9 and math.isnan(s)


def test_global_annual_mean_is_a_quarter_of_s0():
    g = ins.global_annual_mean()
    assert abs(g / (ins.S0 / 4) - 1) < 0.005
    # exactly S0 / (4 sqrt(1 - e^2)) for a Keplerian orbit
    assert abs(g - ins.S0 / 4 / math.sqrt(1 - _solar.ECC ** 2)) < 0.02


def test_annual_mean_is_symmetric_between_hemispheres():
    for lat in (20.0, 50.0, 90.0):
        assert abs(ins.annual_mean(lat) - ins.annual_mean(-lat)) < 0.05


def test_insolation_values_as_printed():
    v = dict(ins.values())
    assert round(v["equator_equinox"], 1) == 436.7
    assert round(v["pole_june"]) == 524 and round(v["equator_june"]) == 385
    assert round(v["ann_0"]) == 416 and round(v["ann_90"]) == 172
    assert round(v["lat40_june"]) == 483 and round(v["lat40_dec"]) == 156


# ------------------------------------------------------------ energy balance
def test_band_weights_cover_the_sphere():
    la = eb.lats()
    assert len(la) == 94
    assert abs(sum(eb.weights(la)) - 1) < 1e-12


def test_transport_vanishes_at_both_poles():
    la, down, up, asr, olr, net, alb = eb.toa()
    T = eb.transport(net, la)
    assert T[0][1] == 0.0 and abs(T[-1][1]) < 1e-9
    # without removing the global mean, the reanalysis' imbalance leaves a residue
    assert abs(eb.transport(net, la, remove_mean=False)[-1][1]) > 1.0


def test_transport_peaks_in_mid_latitudes():
    v = dict(eb.values())
    assert 30 < v["peak_N_lat"] < 45 and -40 < v["peak_S_lat"] < -25
    assert round(v["peak_N_PW"], 1) == 4.1 and round(v["peak_S_PW"], 1) == -4.5
    assert round(v["T_40N"], 2) == 4.11
    # the peaks sit where the net radiation (mean removed) changes sign
    zeros = [x for k, x in eb.values() if k == "net_zero_lat"]
    assert len(zeros) == 2
    assert abs(zeros[1] - v["peak_N_lat"]) < 2 and abs(zeros[0] - v["peak_S_lat"]) < 2


def test_global_means_as_printed():
    v = dict(eb.values())
    assert round(v["global_olr"]) == 238 and round(v["global_asr"]) == 225
    assert round(v["global_albedo"], 3) == 0.342
    assert round(v["global_net"], 1) == -12.9
    assert round(v["global_lh"]) == 82 and round(v["global_sh"]) == 15


def test_bands_reproduce_the_transport():
    """Summing the 10-degree band means over the cap north of 40 N gives the same
    transport as the fine integration."""
    b = eb.bands()
    la, down, up, asr, olr, net, alb = eb.toa()
    m = eb.global_mean(net, la)
    cap = sum((n - m) * 2 * math.pi * eb.A ** 2 * (math.sin(math.radians(hi)) - math.sin(math.radians(lo)))
              for lo, hi, d, a, s, o, n in b if lo >= 40)
    assert abs(-cap / 1e15 - eb.interp(eb.transport(net, la), 40.0)) < 1e-6
    for lo, hi, d, a, s, o, n in b:
        assert abs(d * (1 - a) - s) < 1e-9 and abs(s - o - n) < 1e-9


def test_rain_energy_proposition():
    year = 365.25 * eb.DAY
    assert abs(1000.0 * eb.L_V / year - 78.1) < 0.05
