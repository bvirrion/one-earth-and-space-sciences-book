"""Tests for the hotspot figure data: the parsed hotspot table, the Euler pole of a
plate from track azimuths (least squares and from two tracks), the angular speed,
and the Hawaiian swell numbers printed in chapter 15."""
import math
import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import hotspots as hs  # noqa: E402


def synthetic_rows(pole, omega_deg_myr, sites, noise_az=0.0, noise_rate=0.0, seed=15):
    rng = random.Random(seed)
    pv = hs.unit(*pole)
    rows = []
    for lon, lat in sites:
        az, delta = hs.predicted(pv, lon, lat)
        rate = math.radians(omega_deg_myr) * hs.R_KM * math.sin(math.radians(float(delta)))
        rows.append(dict(name=f"{lon},{lat}", lon=lon, lat=lat, w=1.0, saz=5.0,
                         az=float(az) + rng.gauss(0.0, noise_az),
                         rate=rate + rng.gauss(0.0, noise_rate), srate=5.0))
    return rows


SITES = [(-155.0, 19.0), (-138.0, -50.0), (-130.0, 46.0), (-148.0, -18.0),
         (-129.0, -25.0), (-140.0, -29.0), (-170.0, -14.0), (-160.0, -10.0)]


def test_the_velocity_is_perpendicular_to_the_pole_and_to_r():
    pole = (110.0, -60.0)
    pv = hs.unit(*pole)
    for lon, lat in SITES:
        az, _ = hs.predicted(pv, lon, lat)
        t = hs.track_vector(lon, lat, float(az))
        assert abs(t @ pv) < 1e-9                       # omega x r is normal to the pole
        assert abs(t @ hs.unit(lon, lat)) < 1e-12       # tangent to the sphere
        v = np.cross(pv, hs.unit(lon, lat))
        assert abs(np.cross(v, t) @ hs.unit(lon, lat)) < 1e-9   # same direction as omega x r


def test_least_squares_pole_recovers_a_synthetic_pole():
    pole = (110.0, -60.0)
    rows = synthetic_rows(pole, 0.9, SITES)
    lon, lat, chi2 = hs.fit_pole(rows)
    assert abs(lon - pole[0]) < 0.05 and abs(lat - pole[1]) < 0.05
    assert chi2 < 1e-2


def test_pole_from_two_tracks_is_exact_on_exact_tracks():
    pole = (124.0, -56.2)
    rows = synthetic_rows(pole, 0.78, SITES[:2])
    lon, lat = hs.pole_from_two(rows[0], rows[1])
    assert abs(lon - pole[0]) < 1e-6 and abs(lat - pole[1]) < 1e-6
    # swapping the two tracks keeps the same pole (the sign check, not the order, sets it)
    lon2, lat2 = hs.pole_from_two(rows[1], rows[0])
    assert abs(lon2 - pole[0]) < 1e-6 and abs(lat2 - pole[1]) < 1e-6


def test_omega_is_recovered():
    pole = (110.0, -60.0)
    rows = synthetic_rows(pole, 0.85, SITES, noise_rate=0.0)
    omega, x, y = hs.fit_omega(rows, pole)
    assert abs(omega - 0.85) < 1e-9
    rows = synthetic_rows(pole, 0.85, SITES * 20, noise_rate=5.0)
    omega, x, y = hs.fit_omega(rows, pole)
    assert abs(omega - 0.85) < 0.02


def test_parsed_hotspot_table():
    rows = hs.hotspots()
    assert len(rows) == 71                  # Table 1 of Morgan and Morgan (2007), Samoa once
    haw = next(h for h in rows if h["name"] == "Hawaii")
    assert haw["plate"] == "Pacific"
    assert abs(haw["az"] - 304.0) < 1e-9 and abs(haw["rate"] - 92.0) < 1e-9
    assert abs(haw["lat"] - 19.0) < 0.5 and abs(haw["lon"] + 155.2) < 0.5
    # Heard has its own line and does not overwrite Kerguelen
    names = [h["name"] for h in rows]
    assert "Kerguelen" in names and "Heard" in names
    k = next(h for h in rows if h["name"] == "Kerguelen")
    hd = next(h for h in rows if h["name"] == "Heard")
    assert (k["lat"], k["lon"]) != (hd["lat"], hd["lon"])
    # Samoa is listed twice in the table; the supplement's own entry gives 168.2 W
    sam = [h for h in rows if h["name"] == "Samoa"]
    assert len(sam) == 1 and abs(sam[0]["lon"] + 168.2) < 1e-9
    # a quality letter instead of a weight: no weight, so out of the fit
    na = next(h for h in rows if h["name"] == "N.Austral")
    assert na["w"] is None and na["az"] == 293.0
    # two plates over one hotspot: Iceland on both sides of the ridge
    ice = sorted(h["plate"] for h in rows if h["name"] == "Iceland")
    assert ice == ["Eurasian", "North American"]


def test_pacific_numbers_printed_in_the_text():
    _, pac, rated, x, y, prof, sw, v = hs.analysis()
    assert v["n_pacific"] == 15 and v["n_rated"] == 13
    assert -70.0 < v["pole_lat"] < -55.0 and 100.0 < v["pole_lon"] < 130.0
    assert 0.8 < v["omega_deg_myr"] < 1.0
    assert 80.0 < v["hawaii_pred_rate"] < 110.0
    assert abs(v["hawaii_pred_az"] - 304.0) < 10.0
    # the two-track pole (Hawaii, Louisville) of the weekend problem
    assert abs(v["two_pole_lat"] + 56.18) < 0.01 and abs(v["two_pole_lon"] - 124.01) < 0.01


def test_swell_numbers():
    _, _, _, _, _, prof, sw, v = hs.analysis()
    assert 400.0 < v["swell_height"] < 1500.0       # measured on ETOPO1 (690 m printed in ch. 15)
    assert 2e8 < v["swell_area_m2"] < 1e9
    assert 1000.0 < v["swell_B_kg_s"] < 10000.0
    # the swell curve leaves the median untouched outside the chain
    for (d, m, _, _), s in zip(prof, sw):
        if abs(d) > hs.SWELL_CHAIN:
            assert s == m


def test_buoyancy_flux_formula():
    # 1 km^2 cross-section moving at 1 m/yr: (3300 - 1000) * 1e6 * 1 / yr
    b = hs.buoyancy_flux(1e6, 1000.0)
    assert abs(b - 2300.0 * 1e6 / (365.25 * 86400.0)) < 1e-9
