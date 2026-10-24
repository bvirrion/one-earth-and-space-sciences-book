"""The Eady model of baroclinic instability (Year 3, atmospheric dynamics).

A Boussinesq fluid on an f-plane between rigid lids at z = 0 and z = H, with
uniform buoyancy frequency N and a basic westerly U(z) = Lambda z. Normal modes
exp(i(kx + ly - k c t)) of the quasi-geostrophic equations have

    c = U(H)/2 +- (U(H)/mu) sqrt[(mu/2 - coth(mu/2)) (mu/2 - tanh(mu/2))],

with mu = K L_d, K = sqrt(k^2 + l^2) and L_d = N H / f. They grow, for
mu < mu_c (coth(mu_c/2) = mu_c/2, mu_c = 2.3994), at the rate

    sigma = (f Lambda / N) sqrt[(coth(mu/2) - mu/2)(mu/2 - tanh(mu/2))]   (l = 0),

whose maximum is 0.3098 f Lambda / N at mu = 1.6061.

Dimensional example: f at 45 N; Lambda from the January zonal-mean wind at
45 N between 850 and 250 hPa (NCEP-NCAR R1, shared derived table, ledger
data:b5-ncep-uwnd) divided by the height difference of those pressures in the
NASA standard atmosphere (nasa:grc-atmos); N the mean tropospheric value of
buoyancy_frequency.py; H = 11 km, the model's tropopause.

  part curve    mu s lam sday     s = sigma N/(f Lambda); lam the wavelength 2 pi L_d/mu (km);
                                  sday the growth rate (1/day) of the example
  part values   what value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402
import buoyancy_frequency as bf  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
UWND = os.path.join(ROOT, "data", "derived", "bachelor-1-ncep-uwnd-p.csv")
OMEGA = 7.292115e-5
LAT = 45.0
H_TROP = 11000.0


def growth(mu):
    """Nondimensional growth rate sigma N / (f Lambda) for l = 0."""
    if mu <= 0:
        return 0.0
    h = mu / 2
    a = (1 / math.tanh(h) - h) * (h - math.tanh(h))
    return math.sqrt(a) if a > 0 else 0.0


def argmax_growth():
    """Golden-section search for the fastest-growing mu."""
    lo, hi = 0.5, 2.3
    g = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        a = hi - g * (hi - lo)
        b = lo + g * (hi - lo)
        if growth(a) > growth(b):
            hi = b
        else:
            lo = a
    m = 0.5 * (lo + hi)
    return m, growth(m)


def critical_mu():
    lo, hi = 2.0, 3.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if 1 / math.tanh(m / 2) - m / 2 > 0:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def height_of_p(p_kpa):
    """Height (m) of a pressure in the NASA standard troposphere."""
    t = 288.08 * (p_kpa / 101.29) ** (1 / 5.256) - 273.1
    return (15.04 - t) / 0.00649


def coriolis(lat=LAT):
    return 2 * OMEGA * math.sin(math.radians(lat))


def observed_shear(lat=LAT):
    u = {}
    with open(UWND, encoding="utf8") as f:
        for r in csv.DictReader(f):
            if int(r["month"]) == 1 and float(r["lat"]) == lat:
                u[int(r["level"])] = float(r["value"])
    dz = height_of_p(25.0) - height_of_p(85.0)
    return (u[250] - u[850]) / dz, dz


def n_trop():
    hs = range(500, 11000, 500)
    return sum(math.sqrt(bf.n2_atm(h)) for h in hs) / len(hs)


def main():
    f = coriolis()
    lam, dz = observed_shear()
    n = n_trop()
    ld = n * H_TROP / f
    scale = f * lam / n * 86400.0
    rows = []
    for i in range(1, 241):
        mu = i / 100
        rows.append([mu, growth(mu), 2 * math.pi * ld / mu / 1e3, growth(mu) * scale])
    write_table(__file__, ("mu", "s", "lam", "sday"), rows, part="curve")
    mmax, smax = argmax_growth()
    sig = smax * f * lam / n
    write_table(__file__, ("what", "value"),
                [["mu_max", mmax], ["s_max", smax], ["mu_c", critical_mu()],
                 ["f", f], ["Lambda", lam], ["dz_850_250", dz], ["N", n], ["Ld_km", ld / 1e3],
                 ["sigma_max", sig], ["efold_days", 1 / sig / 86400],
                 ["lambda_max_km", 2 * math.pi * ld / mmax / 1e3],
                 ["lambda_c_km", 2 * math.pi * ld / critical_mu() / 1e3]],
                part="values")


if __name__ == "__main__":
    main()
