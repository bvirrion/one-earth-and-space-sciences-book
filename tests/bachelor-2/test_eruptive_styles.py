"""Tests for the eruption figure data (eruptions.py)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import eruptions as er  # noqa: E402


def test_volume_formulas():
    # one segment: 2 T0 / k^2 equals the numerical integral of T 2x dx
    t0, k = 2.0, 0.3
    dx = 0.001
    num = sum(t0 * math.exp(-k * (i + 0.5) * dx) * 2 * (i + 0.5) * dx * dx for i in range(200000))
    assert abs(num - er.volume_one(t0, k)) < 1e-6 * er.volume_one(t0, k)
    # two segments with equal slopes reduce to one; the formula matches a numerical integral
    assert abs(er.volume_two(t0, k, k, 5.0) - er.volume_one(t0, k)) < 1e-12
    k1, k2, x = 0.4, 0.15, 6.0
    t02 = t0 * math.exp(-(k1 - k2) * x)
    num = 0.0
    for i in range(200000):
        xi = (i + 0.5) * dx
        t = t0 * math.exp(-k1 * xi) if xi < x else t02 * math.exp(-k2 * xi)
        num += t * 2 * xi * dx
    assert abs(num - er.volume_two(t0, k1, k2, x)) < 1e-5 * num


def test_layer5_matches_authors():
    # Biass et al. (2019): two-segment volume 0.29 km3, bt_A 1.9 and 5.3 km
    t01, k1, t02, k2, x_ip, v = er.layer5()
    assert abs(v - 0.29) < 0.01
    assert abs(math.log(2) / k1 - 1.9) < 0.05
    assert abs(math.log(2) / k2 - 5.3) < 0.4
    assert 7.0 < x_ip < 12.3                 # the lines cross between the 2nd and 3rd isopachs
    # VEI 4: bulk volume between 1e8 and 1e9 m3
    assert 0.1 < v < 1.0


def test_frequency_law():
    e = er.load_eruptions()
    assert len(e) > 7000
    rates = [er.rate(e, v, er.WINDOWS[v])[0] for v in sorted(er.WINDOWS)]
    assert all(r1 > r2 for r1, r2 in zip(rates, rates[1:]))       # bigger is rarer
    a, b = er.frequency_fit(e)
    assert 0.7 < b < 1.0                     # close to a factor ten per VEI step
    # the fit predicts the separately counted VEI >= 7 rate within a factor of two
    lam7, n7 = er.rate(e, 7, er.WINDOW7)
    assert n7 == 2 and 0.5 < 10 ** (a - 7 * b) / lam7 < 2
    p = er.poisson_at_least_one(10 ** (a - 6 * b), 100)
    assert 0.6 < p < 0.9
    # the record of small eruptions is the least complete: since 1500, the fraction of
    # VEI >= 3 eruptions recorded by 1800 is below that of VEI >= 6
    def frac(v):
        tot = sum(1 for y, x in e if x >= v and 1500 <= y <= er.END)
        return sum(1 for y, x in e if x >= v and 1500 <= y <= 1800) / tot
    assert frac(3) < frac(6)


def test_column_height():
    # the two empirical fits agree within 15 per cent near 1e7 kg/s and give St Helens' 15 km
    assert abs(er.mastin(1e7) - 15) < 1 and abs(er.aubry(1e7) / er.mastin(1e7) - 1) < 0.15
    # a factor 16 in Q raises H by about a factor 2 (H ~ Q^(1/4))
    assert abs(er.mastin(16e6) / er.mastin(1e6) - 2) < 0.05


def test_mogi():
    z0, dv = 3000.0, 2e6
    u0 = er.mogi_uz(0, z0, dv)
    assert abs(u0 - 0.75 * dv / (math.pi * z0 ** 2)) < 1e-12
    w = er.mogi_half_width(z0)
    assert abs(er.mogi_uz(w, z0, dv) - u0 / 2) < 1e-9
    assert abs(w / z0 - 0.766) < 0.001
    # deeper source: smaller and broader bulge
    assert abs(er.mogi_uz(0, 2 * z0, dv) - u0 / 4) < 1e-12


def test_gas_fraction():
    rh, ba = er.RHYOLITE_GAS, er.BASALT_GAS
    psat = (rh["w0"] / rh["s"]) ** 2
    assert er.gas_fraction(psat * 1.01, **rh) == 0.0          # nothing exsolved above saturation
    fr = [er.gas_fraction(p, **rh) for p in (100, 30, 10, 3, 1, 0.1)]
    assert all(a < b for a, b in zip(fr, fr[1:]))              # the froth grows on decompression
    p85 = er.pressure_at_fraction(0.85, **rh)
    assert abs(er.gas_fraction(p85, **rh) - 0.85) < 1e-6 and 5 < p85 < 12
    # a basalt with a fifth of the water reaches the same froth only near the surface
    assert er.pressure_at_fraction(0.85, **ba) < p85 / 3
    # hand check at 10 MPa: x = (5 - 0.444 sqrt 10)/100, ideal gas, melt 2300 kg/m3
    x = (5 - 0.444 * 10 ** 0.5) / 100
    vg = x * 8.314 * 1123.15 / (0.018015 * 10e6)
    assert abs(er.gas_fraction(10, **rh) - vg / (vg + (1 - x) / 2300)) < 1e-12
