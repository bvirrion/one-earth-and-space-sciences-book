"""The rotation curve of the Milky Way and its mass model (Year 3, Milky Way and galaxies).

Data: the circular velocity of the Galaxy from 5 to 25 kpc measured by Eilers, Hogg, Rix
and Ness (2019, ApJ 871, 120; arXiv:1810.09466, Table 1), 38 bins, copied below
(ledger eilers19:table1). The Sun at R0 = 8.122 kpc as in that paper.

Baryons (ledger pouliasis17:model1): Model I of Pouliasis, Di Matteo and Haywood (2017,
A&A 598, A66, Table 1), as used by Eilers et al.: a Plummer bulge (M = 460, b = 0.3), a thin
Miyamoto-Nagai disc (M = 1700, a = 5.3, b = 0.25) and a thick one (M = 1700, a = 2.6,
b = 0.8), masses in units of 2.32e7 solar masses, lengths in kpc. In the plane z = 0:
  Plummer          v^2 = G M R^2 / (R^2 + b^2)^(3/2)
  Miyamoto-Nagai   v^2 = G M R^2 / (R^2 + (a + b)^2)^(3/2)
Dark halo: a Navarro-Frenk-White profile rho = rho0 / (x (1 + x)^2), x = r / Rs, whose
circular velocity is v^2 = 4 pi G rho0 Rs^3 [ln(1 + x) - x / (1 + x)] / r. Its two
parameters are fitted here to the data by weighted least squares (weights 1/sigma^2,
sigma the mean of the two published error bars), with the baryons held fixed, as in
Eilers et al. (who sampled the posterior by MCMC instead: Rs = 14.8 kpc,
rho0 = 1.06e7 Msun/kpc^3). The fit is tested on synthetic data built from known
parameters (tests/bachelor-3/test_rotation_curve.py).

Enclosed mass: M(<R) = R v^2 / G, exact for a spherical distribution and used here, as in
the chapter, as the "dynamical mass" of a flattened one too.

  part data      R vc sig_lo sig_hi
  part model     R v_bulge v_thin v_thick v_bar v_halo v_tot
  part mass      R m_bar m_tot                        (1e10 solar masses)
  part mdata     R m_dyn                              R v^2 / G of each measured bin (1e10 Msun)
  part values    what value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

G_SI = 6.67430e-11          # const:G
M_SUN = 1.9884e30           # sun:mass
KPC = 3.085677581e19        # iau:parsec x 1000
G = G_SI * M_SUN / KPC / 1e6   # kpc (km/s)^2 per solar mass, about 4.30e-6
MASS_UNIT = 2.32e7          # Pouliasis et al. / Allen & Santillan mass unit, solar masses
R0 = 8.122                  # kpc, the Sun, as adopted by Eilers et al.

BULGE = (460.0, 0.3)               # M, b (Plummer)
THIN = (1700.0, 5.3, 0.25)         # M, a, b (Miyamoto-Nagai)
THICK = (1700.0, 2.6, 0.8)

# Eilers et al. 2019, Table 1: R (kpc), vc, sigma-, sigma+ (km/s)
EILERS = (
    (5.27, 226.83, 1.91, 1.90), (5.74, 230.80, 1.43, 1.35), (6.23, 231.20, 1.70, 1.10),
    (6.73, 229.88, 1.44, 1.32), (7.22, 229.61, 1.37, 1.11), (7.82, 229.91, 0.92, 0.88),
    (8.19, 228.86, 0.80, 0.67), (8.78, 226.50, 1.07, 0.95), (9.27, 226.20, 0.72, 0.62),
    (9.76, 225.94, 0.42, 0.52), (10.26, 225.68, 0.44, 0.40), (10.75, 224.73, 0.38, 0.41),
    (11.25, 224.02, 0.33, 0.54), (11.75, 223.86, 0.40, 0.39), (12.25, 222.23, 0.51, 0.37),
    (12.74, 220.77, 0.54, 0.46), (13.23, 220.92, 0.57, 0.40), (13.74, 217.47, 0.64, 0.51),
    (14.24, 217.31, 0.77, 0.66), (14.74, 217.60, 0.65, 0.68), (15.22, 217.07, 1.06, 0.80),
    (15.74, 217.38, 0.84, 1.07), (16.24, 216.14, 1.20, 1.48), (16.74, 212.52, 1.39, 1.43),
    (17.25, 216.41, 1.44, 1.85), (17.75, 213.70, 2.22, 1.65), (18.24, 207.89, 1.76, 1.88),
    (18.74, 209.60, 2.31, 2.77), (19.22, 206.45, 2.54, 2.36), (19.71, 201.91, 2.99, 2.26),
    (20.27, 199.84, 3.15, 2.89), (20.78, 198.14, 3.33, 3.37), (21.24, 195.30, 5.99, 6.50),
    (21.80, 213.67, 15.38, 12.18), (22.14, 176.97, 28.58, 18.57), (22.73, 193.11, 27.64, 19.05),
    (23.66, 176.63, 18.67, 16.74), (24.82, 198.42, 6.50, 6.12),
)


def v_plummer(r, m, b):
    m = m * MASS_UNIT
    return math.sqrt(G * m * r * r / (r * r + b * b) ** 1.5)


def v_miyamoto_nagai(r, m, a, b):
    m = m * MASS_UNIT
    return math.sqrt(G * m * r * r / (r * r + (a + b) ** 2) ** 1.5)


def v_baryons(r):
    """bulge, thin disc, thick disc and their quadrature sum, km/s."""
    vb = v_plummer(r, *BULGE)
    vt = v_miyamoto_nagai(r, *THIN)
    vk = v_miyamoto_nagai(r, *THICK)
    return vb, vt, vk, math.sqrt(vb * vb + vt * vt + vk * vk)


def nfw_mass(r, rho0, rs):
    """Mass of an NFW halo within radius r (solar masses; rho0 in Msun/kpc^3, kpc)."""
    x = r / rs
    return 4 * math.pi * rho0 * rs ** 3 * (math.log(1 + x) - x / (1 + x))


def v_nfw(r, rho0, rs):
    return math.sqrt(G * nfw_mass(r, rho0, rs) / r)


def v_total(r, rho0, rs):
    return math.sqrt(v_baryons(r)[3] ** 2 + v_nfw(r, rho0, rs) ** 2)


def enclosed_mass(r, v):
    """Dynamical mass R v^2 / G, solar masses."""
    return r * v * v / G


def fit_nfw(data, start=(1e7, 15.0)):
    """Weighted least-squares fit of (rho0, Rs) to rows (R, v, sigma), baryons fixed.
    Returns rho0, Rs, chi2. Parameters fitted in logarithms (both stay positive)."""
    from scipy.optimize import least_squares

    def resid(p):
        rho0, rs = math.exp(p[0]), math.exp(p[1])
        return [(v_total(r, rho0, rs) - v) / s for r, v, s in data]

    sol = least_squares(resid, [math.log(start[0]), math.log(start[1])], method="lm",
                        xtol=1e-12, ftol=1e-12)
    rho0, rs = math.exp(sol.x[0]), math.exp(sol.x[1])
    chi2 = sum(x * x for x in sol.fun)
    return rho0, rs, chi2


def eilers_rows():
    return [(r, v, (lo + hi) / 2) for r, v, lo, hi in EILERS]


def linear_slope(rows):
    """Least-squares slope (km/s per kpc) and intercept of v against R."""
    n = len(rows)
    sx = sum(r for r, _ in rows)
    sy = sum(v for _, v in rows)
    sxx = sum(r * r for r, _ in rows)
    sxy = sum(r * v for r, v in rows)
    k = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    return k, (sy - k * sx) / n


def main():
    data = eilers_rows()
    rho0, rs, chi2 = fit_nfw(data)
    write_table(__file__, ("R", "vc", "sig_lo", "sig_hi"), EILERS, part="data")
    model, mass = [], []
    r = 0.25
    while r <= 30.0001:
        vb, vt, vk, vbar = v_baryons(r)
        vh = v_nfw(r, rho0, rs)
        vtot = math.sqrt(vbar * vbar + vh * vh)
        model.append((r, vb, vt, vk, vbar, vh, vtot))
        mass.append((r, enclosed_mass(r, vbar) / 1e10, enclosed_mass(r, vtot) / 1e10))
        r = round(r + 0.25, 2)
    write_table(__file__, ("R", "v_bulge", "v_thin", "v_thick", "v_bar", "v_halo", "v_tot"),
                model, part="model")
    write_table(__file__, ("R", "m_bar", "m_tot"), mass, part="mass")
    write_table(__file__, ("R", "m_dyn"), [(r, enclosed_mass(r, v) / 1e10) for r, v, _, _ in EILERS],
                part="mdata")
    vals = [["G_kpc_kms2_per_msun", G], ["rho0_fit", rho0], ["rs_fit", rs], ["chi2", chi2],
            ["ndata", len(data)]]
    for rr in (R0, 10.0, 14.0, 20.0, 25.0):
        vb, vt, vk, vbar = v_baryons(rr)
        vh = v_nfw(rr, rho0, rs)
        vtot = math.sqrt(vbar * vbar + vh * vh)
        vals += [["v_bar_%g" % rr, vbar], ["v_halo_%g" % rr, vh], ["v_tot_%g" % rr, vtot],
                 ["m_bar_%g" % rr, enclosed_mass(rr, vbar)],
                 ["m_tot_%g" % rr, enclosed_mass(rr, vtot)],
                 ["dark_frac_%g" % rr, 1 - (vbar / vtot) ** 2]]
    # radius beyond which the halo term exceeds the baryons
    r = 5.0
    while v_nfw(r, rho0, rs) < v_baryons(r)[3]:
        r += 0.01
    vals.append(["r_halo_dominates", r])
    k, c = linear_slope([(r, v) for r, v, _ in data if r <= 24.9])
    vals += [["slope_all", k], ["v_at_r0_linear", c + k * R0]]
    vals.append(["m_stellar_total", (BULGE[0] + THIN[0] + THICK[0]) * MASS_UNIT])
    vals.append(["m_discs_total", (THIN[0] + THICK[0]) * MASS_UNIT])
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
