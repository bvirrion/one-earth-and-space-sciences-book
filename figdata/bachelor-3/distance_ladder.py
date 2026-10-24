"""The Leavitt law of the Large Magellanic Cloud's Cepheids, and the rungs of the distance
ladder (Year 3, Milky Way and galaxies).

Data: the OGLE-IV classical Cepheids of the LMC (Soszynski et al. 2015, Acta Astron. 65, 297,
2019 update; CDS J/AcA/65/297, data/derived/bachelor-3-ogle-lmc-cep.csv, ledger
data:b5-ogle-lmc-cep): mean I and V magnitudes and periods. Only fundamental-mode
pulsators (mode F) are used. The reddening-free Wesenheit index is
W_I = I - 1.55 (V - I) (as defined in that paper).

Fit: W_I = alpha log10(P/d) + beta by ordinary least squares, then iteratively without the
points more than 3 standard deviations from the line, until no point is removed. The
published fit (Table 2 of the paper: alpha = -3.314, beta = 15.888, sigma = 0.077) is
written beside it for comparison. Absolute magnitudes use the LMC distance modulus
mu = 18.477 (Pietrzynski et al. 2019, as quoted by Freedman et al. 2019 and Riess et al.
2022; ledger freedman19:lmc).

Ladder rungs (part ladder): for each method, the range of distances in kpc over which the
chapter uses it, each end computed from a ledger value:
  parallax      from 1 pc (a plotting floor) to the distance where a parallax error of
                0.025 mas is 10 % (gaia:dr3)
  Cepheids      LMC (mu 18.477) to the farthest calibrator host, z = 0.011 (riess22)
  TRGB          LMC to z = 0.011 (the same supernova hosts, freedman19)
  SNe Ia        z = 0.0233 to 0.15 (the Hubble-flow sample of riess22)
Redshifts are turned into distances by d = c z / H0 with H0 = 73.04 (riess22).

  part pl        logp w i v                    all F-mode stars
  part clipped   logp w                        the ones the clipping removed
  part fit       logp w_fit w_pub              lines over the range of the data
  part ladder    rung method d_lo d_hi         kpc (rung 1-4, bottom to top)
  part anchors   name mu d                     distance modulus, kpc
  part values    what value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DATA = os.path.join(ROOT, "data", "derived", "bachelor-3-ogle-lmc-cep.csv")
R_W = 1.55                       # Wesenheit coefficient (Soszynski et al. 2015)
PUBLISHED = (-3.314, 15.888, 0.077)
MU_LMC = 18.477
H0 = 73.04                       # km/s/Mpc
C_KMS = 299792.458
SIGMA_PLX = 0.025                # mas, Gaia DR3, G < 15 (0.02-0.03)
Z_CAL, Z_FLOW = (0.011, (0.0233, 0.15))
# distance moduli of three anchors: the LMC (above), M31 (McConnachie 2012, ledger
# mcconn12:local-group) and NGC 4258 (masers, as used by Riess et al. 2022)
ANCHORS = (("lmc", MU_LMC), ("m31", 24.47), ("n4258", 29.398))


def load_fundamental(path=DATA):
    """(log10 P, W_I, I, V) for every F-mode Cepheid with both magnitudes."""
    out = []
    with open(path, encoding="utf8") as f:
        for r in csv.DictReader(f):
            if r["mode"] != "F":
                continue
            i, v, p = float(r["i_mag"]), float(r["v_mag"]), float(r["period_d"])
            out.append((math.log10(p), wesenheit(i, v), i, v))
    return out


def wesenheit(i, v, r=R_W):
    return i - r * (v - i)


def ols(xy):
    n = len(xy)
    mx = sum(x for x, _ in xy) / n
    my = sum(y for _, y in xy) / n
    sxx = sum((x - mx) ** 2 for x, _ in xy)
    sxy = sum((x - mx) * (y - my) for x, y in xy)
    a = sxy / sxx
    b = my - a * mx
    s = math.sqrt(sum((y - a * x - b) ** 2 for x, y in xy) / (n - 2))
    return a, b, s


def clipped_fit(xy, k=3.0, max_iter=50):
    """OLS, then refit without points beyond k sigma until none is removed.
    Returns (a, b, sigma, kept, removed)."""
    kept = list(xy)
    for _ in range(max_iter):
        a, b, s = ols(kept)
        new = [(x, y) for x, y in kept if abs(y - a * x - b) <= k * s]
        if len(new) == len(kept):
            break
        kept = new
    a, b, s = ols(kept)
    removed = [p for p in xy if abs(p[1] - a * p[0] - b) > k * s]
    return a, b, s, kept, removed


def distance_kpc(mu):
    return 10 ** (mu / 5 + 1) / 1000


def z_to_kpc(z, h0=H0):
    return C_KMS * z / h0 * 1000


def ladder():
    lmc = distance_kpc(MU_LMC)
    plx_max = 1 / (10 * SIGMA_PLX)          # parallax 10 x its error, kpc (1/mas)
    return [(1, "parallax", 0.001, plx_max), (2, "cepheids", lmc, z_to_kpc(Z_CAL)),
            (3, "trgb", lmc, z_to_kpc(Z_CAL)),
            (4, "snia", z_to_kpc(Z_FLOW[0]), z_to_kpc(Z_FLOW[1]))]


def main():
    stars = load_fundamental()
    xy = [(x, w) for x, w, _, _ in stars]
    a, b, s, kept, removed = clipped_fit(xy)
    write_table(__file__, ("logp", "w", "i", "v"), sorted(stars), part="pl")
    write_table(__file__, ("logp", "w"), sorted(removed), part="clipped")
    lo, hi = min(x for x, _ in xy), max(x for x, _ in xy)
    write_table(__file__, ("logp", "w_fit", "w_pub"),
                [(x, a * x + b, PUBLISHED[0] * x + PUBLISHED[1]) for x in (lo, hi)], part="fit")
    write_table(__file__, ("rung", "method", "d_lo", "d_hi"), ladder(), part="ladder")
    write_table(__file__, ("name", "mu", "d"), [(n, mu, distance_kpc(mu)) for n, mu in ANCHORS],
                part="anchors")
    ai, bi, si = ols([(x, i) for x, _, i, _ in stars])
    vals = [["n_F", len(stars)], ["n_kept", len(kept)], ["n_removed", len(removed)],
            ["alpha", a], ["beta", b], ["sigma", s],
            ["alpha_pub", PUBLISHED[0]], ["beta_pub", PUBLISHED[1]],
            ["alpha_I_unclipped", ai], ["beta_I_unclipped", bi], ["sigma_I_unclipped", si],
            ["logp_min", lo], ["logp_max", hi],
            ["d_lmc_kpc", distance_kpc(MU_LMC)],
            ["M_W_at_10d", a * 1 + b - MU_LMC], ["M_W_at_1d", b - MU_LMC]]
    for _, name, d0, d1 in ladder():
        vals += [["%s_lo" % name, d0], ["%s_hi" % name, d1]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
