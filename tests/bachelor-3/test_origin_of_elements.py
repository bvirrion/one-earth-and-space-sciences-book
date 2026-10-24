"""Tests for the solar abundances, the neutron-capture classification and sigma-N curve, and
the chemical-evolution models (Year 3, ch. 30, origin of the elements)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import chemical_evolution as ce  # noqa: E402
import neutron_capture as nc  # noqa: E402
import solar_abundances as sa  # noqa: E402


# --- solar abundances --------------------------------------------------------------------
def test_sun_and_meteorites_agree_as_published():
    """Asplund et al. 2021: the weighted mean photosphere - CI difference of the 58
    non-depleted elements is 0.000 +- 0.007 dex."""
    tab = sa.load()
    assert len(tab) == 83
    d, se, n = sa.weighted_mean_difference(tab, sa.METEORITE_DEPLETED | sa.SUN_DEPLETED)
    assert n == 58
    assert d == pytest.approx(0.0, abs=0.001)
    assert se == pytest.approx(0.007, abs=0.001)


def test_curve_prefers_the_photosphere_and_dex_scale():
    tab = sa.load()
    cur = {z: (v, s) for z, v, s in sa.curve(tab)}
    assert cur[1] == (12.0, 1) and cur[26] == (7.46, 1)
    assert cur[52][1] == 0                       # Te: meteorites only
    assert sa.number_ratio(7.46, 12.0) == pytest.approx(2.884e-5, rel=1e-3)
    assert sa.dex(10.0) == pytest.approx(1.0)


# --- neutron captures --------------------------------------------------------------------
@pytest.fixture(scope="module")
def nuclear():
    nat = nc.load_isotopes()
    decay = nc.load_decay()
    return nat, decay, nc.load_macs(), nc.classify(nat, decay)


def test_isotope_table_is_complete(nuclear):
    nat = nuclear[0]
    by_el = {}
    for (z, a), (el, frac, _) in nat.items():
        by_el.setdefault(z, 0.0)
        by_el[z] += frac
    assert all(abs(v - 1) < 2e-4 for v in by_el.values())
    assert (46, 102) in nat and (45, 103) in nat      # rows whose printed Z was shifted


def test_s_only_pairs_and_weak_component(nuclear):
    """Kaeppeler et al. 2011: the s-only pairs of their Table I and the six s-only nuclei
    below A = 90."""
    cls = nuclear[3]
    for z, a in ((36, 80), (36, 82), (52, 122), (52, 124), (54, 128), (54, 130), (56, 134),
                 (56, 136), (62, 148), (62, 150), (32, 70), (34, 76), (38, 86), (38, 87),
                 (60, 142), (71, 176), (76, 186), (76, 187)):
        assert cls[(z, a)] == 0, (z, a)


def test_r_only_and_p_nuclei(nuclear):
    cls = nuclear[3]
    for k in ((52, 128), (52, 130), (54, 134), (54, 136), (50, 122), (50, 124)):
        assert cls[k] == 2, k
    for k in ((34, 74), (36, 78), (38, 84), (42, 92), (42, 94), (52, 120), (54, 124),
              (54, 126), (56, 130), (56, 132), (62, 144), (80, 196)):
        assert cls[k] == 3, k
    assert sum(c == 0 for c in cls.values()) == 30
    assert sum(c == 3 for c in cls.values()) == 36     # 35 + 176Hf (isomer branch)


def test_long_lived_nuclei_capture_on_the_main_path(nuclear):
    nat, decay = nuclear[0], nuclear[1]
    steps, capturing = nc.s_path(nat, decay)
    assert (46, 107) in capturing and (40, 93) in capturing     # 107Pd, 93Zr
    assert (47, 107) not in capturing                           # so 107Ag is bypassed
    assert capturing[-1] == (83, 209)


def test_sigma_n_pairs_match_the_published_products(nuclear):
    """Kaeppeler et al. Table I uses 2.55/4.74 for 122Te/124Te and 11.24/7.38 for
    148Sm/150Sm with the KADoNiS cross sections; the plain products are 1.024 and 0.870."""
    nat, _, macs, cls = nuclear
    sn = {(z, a): v for a, v, z, _ in nc.sigma_n(nat, macs, cls)}
    assert sn[(52, 122)] / sn[(52, 124)] == pytest.approx(295 * 2.55 / (155 * 4.74), rel=0.01)
    assert sn[(62, 148)] / sn[(62, 150)] == pytest.approx(241 * 11.24 / (422 * 7.38), rel=0.01)
    # local equilibrium: the three s-only Te isotopes within 3 per cent
    te = [sn[(52, a)] for a in (122, 123, 124)]
    assert max(te) / min(te) < 1.03


def test_classical_model_on_a_toy_chain():
    """With equal cross sections the product falls geometrically, and the fit recovers its
    parameters."""
    chain = [(26, 56 + i) for i in range(40)]
    macs = {k: 100.0 for k in chain}
    out = nc.classical(chain, macs, 50.0, 0.2)
    q = 1 / (1 + 1 / (0.2 * 100.0))
    assert out[0][2] == pytest.approx(50.0 / 0.2 * q)
    assert out[10][2] / out[9][2] == pytest.approx(q)
    macs2 = {k: 50.0 + 10 * (i % 5) for i, k in enumerate(chain)}
    truth = nc.classical(chain, macs2, 30.0, 0.15)
    pts = [(a, z, v) for a, z, v in truth[5::4]]
    g, t, rms = nc.fit_classical(chain, macs2, pts)
    assert g == pytest.approx(30.0, rel=1e-4) and t == pytest.approx(0.15, rel=1e-4)


def test_solar_sigma_n_fit_shows_the_steps(nuclear):
    nat, decay, macs, cls = nuclear
    _, capturing = nc.s_path(nat, decay)
    sn = nc.sigma_n(nat, macs, cls)
    pts = [(a, z, v) for a, v, z, _ in sn if a > 90 and (z, a) not in nc.EXCLUDE_FIT]
    g, t, rms = nc.fit_classical(capturing, macs, pts)
    assert 0.2 < t < 0.4 and rms < 0.1
    model = {a: v for a, _, v in nc.classical(capturing, macs, g, t)}
    assert model[136] / model[142] > 3          # the drop across N = 82


# --- chemical evolution ------------------------------------------------------------------
def test_closed_box_distribution():
    assert ce.frac_below(0.0) == pytest.approx(1.0)
    assert ce.frac_below(-9.0) == pytest.approx(0.0, abs=1e-6)
    # no star of the closed box is richer than the present gas
    assert ce.frac_below(0.4) == pytest.approx(1.0)
    assert ce.density(0.1) == 0.0
    # the density integrates to the cumulative fraction
    n, lo, hi = 4000, -3.0, -0.5
    h = (hi - lo) / n
    s = sum(ce.density(lo + (k + 0.5) * h) for k in range(n)) * h
    assert s == pytest.approx(ce.frac_below(hi) - ce.frac_below(lo), rel=1e-5)
    assert ce.closed_box_z(math.exp(-1), 0.01) == pytest.approx(0.01)
    assert ce.effective_yield(0.01, math.exp(-2)) == pytest.approx(0.005)


def test_gcs_sample_matches_the_published_statistics():
    """Casagrande et al. 2011, Table 1 (irfm): mean -0.06, median -0.05, sigma 0.22."""
    feh = [f for f, _ in ce.load()]
    mean = sum(feh) / len(feh)
    srt = sorted(feh)
    med = srt[len(srt) // 2]
    sd = math.sqrt(sum((v - mean) ** 2 for v in feh) / len(feh))
    assert mean == pytest.approx(-0.06, abs=0.01)
    assert med == pytest.approx(-0.05, abs=0.01)
    assert sd == pytest.approx(0.22, abs=0.01)


def test_two_phase_alpha_model():
    feh, afe = ce.alpha_track(0.5)
    assert afe == pytest.approx(0.4) and feh == pytest.approx(math.log10(0.05))
    feh, afe = ce.alpha_track(1.0)
    assert feh == pytest.approx(-1.0) and afe == pytest.approx(0.4)
    c, k, x_sun = ce.two_phase()
    feh, afe = ce.alpha_track(x_sun)
    assert feh == pytest.approx(0.0, abs=1e-12) and afe == pytest.approx(0.0, abs=1e-12)
    assert ce.ia_share(x_sun) == pytest.approx(1 - 10 ** -0.4)
