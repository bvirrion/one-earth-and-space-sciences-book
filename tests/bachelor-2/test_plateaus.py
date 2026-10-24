"""Tests for the two-plateaus figure data (figdata/bachelor-2/plateaus.py)."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import plateaus  # noqa: E402


def test_airy_thickness_with_the_year1_densities():
    assert plateaus.airy_root(1.0) == pytest.approx(4.5)
    assert plateaus.airy_thickness(4.8) == pytest.approx(35 + 4.8 + 21.6)
    assert plateaus.airy_thickness(0.0) == pytest.approx(35.0)
    # the density that makes Airy reproduce a given thickness, and back
    rc = plateaus.crust_density_for(72.5, 4.8)
    assert plateaus.airy_thickness(4.8, rho_c=rc) == pytest.approx(72.5)


def test_excess_potential_energy_formula_matches_the_integral():
    for h in (1.0, 3.8, 4.8):
        assert plateaus.gpe_excess(h) == pytest.approx(plateaus.gpe_by_integration(h), rel=1e-6)
    # Tibet at 4.8 km: 2700 x 9.8 x 4800 x (35000 + 2400 + 10800)
    assert plateaus.gpe_excess(4.8) == pytest.approx(2700 * 9.8 * 4800 * 48200)
    assert plateaus.gpe_excess(0.0) == 0.0


def test_shortening_from_thickening_is_an_area_balance():
    W, T, H = 440.0, 60.0, 35.0
    S = plateaus.shortening_from_thickening(W, T, H)
    assert (W + S) * H == pytest.approx(W * T)
    assert S == pytest.approx(314.29, abs=0.01)


def test_relative_plate_velocities_from_nnr_morvel56():
    v, az = plateaus.relative_velocity("India", "Eurasia", 28.0, 85.0)
    assert v == pytest.approx(44.99, abs=0.01) and 15 < az < 30      # Book 2 gives 44.99
    v2, az2 = plateaus.relative_velocity("Nazca", "South America", -20.0, -71.0)
    assert 65 < v2 < 80 and 60 < az2 < 90                              # towards the ENE
    # antisymmetry
    v3, az3 = plateaus.relative_velocity("South America", "Nazca", -20.0, -71.0)
    assert v3 == pytest.approx(v2) and abs(((az3 - az2) % 360) - 180) < 1e-6


def test_swaths_and_plateaus():
    ts, as_ = plateaus.tibet_swath(), plateaus.andes_swath()
    assert len(ts) == 151 and len(as_) == 151
    assert all(n <= m <= x for _, _, m, x, n in ts + as_)
    t0, t1, tw, tm = plateaus.plateau(ts)
    assert (t0, t1) == (27.6, 38.2) and tw == pytest.approx(1178.6, abs=0.1)
    assert 4800 < tm < 4850
    a0, a1, aw, am = plateaus.plateau(as_)
    assert (a0, a1) == (-69.1, -64.9) and 3700 < am < 3800
    # the trench lies west of the plateau, kilometres below sea level
    assert min(r[4] for r in as_) < -7000


def test_contours_stay_in_their_windows():
    for name, box, levels in (("tibet", (75, 100, 25, 40), (2000, 4000)),
                              ("andes", (-75, -60, -30, -10), (0, 2000, 4000))):
        for lev in levels:
            lines = plateaus.contours(name, lev)
            assert lines
            for line in lines:
                for lon, lat in line:
                    assert box[0] <= lon <= box[1] and box[2] <= lat <= box[3]


def test_pressure_profiles_meet_at_the_compensation_depth():
    rows = plateaus.pressure_profiles(4.8)
    z0, ph0, pr0 = rows[0]
    zl, phl, prl = rows[-1]
    assert z0 == pytest.approx(-4.8) and ph0 == 0.0 and pr0 == 0.0
    assert zl == pytest.approx(35 + 21.6) and phl == pytest.approx(prl)
    # every level of the high column is at a higher pressure than the normal one
    assert all(ph >= pr - 1e-9 for _, ph, pr in rows)
    # the area between the curves is the excess potential energy (MPa km = 1e9 N/m)
    area = sum((rows[k + 1][0] - rows[k][0]) * ((rows[k][1] - rows[k][2]) + (rows[k + 1][1] - rows[k + 1][2])) / 2
               for k in range(len(rows) - 1))
    assert area * 1e9 == pytest.approx(plateaus.gpe_excess(4.8), rel=1e-3)
