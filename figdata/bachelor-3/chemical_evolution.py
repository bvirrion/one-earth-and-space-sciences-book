"""Galactic chemical evolution: the closed box against the metallicities of the solar
neighbourhood, and a two-phase model of [alpha/Fe] (Year 3, origin of the elements).

Closed box (the Simple Model as stated by Matteucci 2021, Sect. 3.1, ledger
matteucci21:simple): one zone, no inflow or outflow, primordial gas at the start,
instantaneous recycling. The metallicity of the gas is Z = y ln(1/mu), mu the gas fraction
of the mass. The mass of stars (and remnants) formed with metallicity below Z is
M (1 - exp(-Z/y)); so the fraction of all the stars formed so far that have Z < Z' is
  F(Z') = (1 - exp(-Z'/y)) / (1 - mu1),  with exp(-Z1/y) = mu1 at the present Z1.
With Fe proportional to Z and the present gas solar, [Fe/H] = log10(Z / Z1).
Present gas fraction of the solar neighbourhood: mu1 = 13.7 / 47.1 (gas over gas, stars
and stellar remnants, McKee, Parravano and Hollenbach 2015, ledger mckee15:surface).

Observed: [Fe/H] of the F and G dwarfs of the Geneva-Copenhagen survey, irfm sample
(Casagrande et al. 2011; data/derived/bachelor-3-gcs.csv, ledger data:b5-gcs), and the
subset with a median isochrone mass of at most one solar mass.

Two-phase [alpha/Fe] (the time-delay model, ledger matteucci21:time-delay): in the closed
box with a star formation rate proportional to the gas mass, core-collapse supernovae
return alpha elements and some iron at once, so Z_alpha and Z_Fe,cc both grow linearly
with time; Type Ia supernovae start a delay D later and, since their rate follows the
star formation of D earlier, add iron at a constant rate (the gas mass falls by the same
factor in both). With x = t / D:
  Z_alpha ~ x,   Z_Fe ~ x + K (x - 1) for x > 1.
The plateau P = [alpha/Fe] at x < 1 (+0.4 in halo stars), the knee at [Fe/H] = -1 and
[alpha/Fe] = 0 at [Fe/H] = 0 fix the model: [Fe/H] = log10(0.1 (x + K (x - 1))).

  part mdf        feh n_obs n_low model       0.1-dex bins: all irfm stars, those of at
                                              most 1 solar mass, closed-box prediction
                                              scaled to the number of irfm stars
  part curve      feh frac_cum                closed-box cumulative fraction
  part alpha      feh afe                     two-phase model
  part values     what value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DATA = os.path.join(ROOT, "data", "derived", "bachelor-3-gcs.csv")
SIGMA_GAS, SIGMA_ALL = 13.7, 47.1          # Msun/pc^2 (mckee15:surface)
MU1 = SIGMA_GAS / SIGMA_ALL
Z_SUN = 0.0154                              # proto-solar Z (asplund21:xyz)
PLATEAU, KNEE = 0.4, -1.0                   # matteucci21:time-delay
BIN = 0.1
LO, HI = -1.6, 0.7


def closed_box_z(mu, y):
    return y * math.log(1 / mu)


def effective_yield(z, mu):
    return z / math.log(1 / mu)


def frac_below(feh, mu1=MU1):
    """Closed-box fraction of the stars formed so far with [Fe/H] below feh (present gas
    solar). No star is richer than the present gas: the fraction is 1 from [Fe/H] = 0."""
    u = math.log(1 / mu1) * 10 ** min(feh, 0.0)   # Z / y
    return (1 - math.exp(-u)) / (1 - mu1)


def density(feh, mu1=MU1):
    """dF/d[Fe/H] of the closed box (zero above the present gas, [Fe/H] = 0)."""
    if feh > 0:
        return 0.0
    u = math.log(1 / mu1) * 10 ** feh
    return math.log(10) * u * math.exp(-u) / (1 - mu1)


def load(path=DATA):
    """[(feh, mass or None)] for the irfm stars."""
    out = []
    with open(path, encoding="utf8") as f:
        for r in csv.DictReader(f):
            m = float(r["mass_padova"])
            out.append((float(r["feh"]), m if m > 0 else None))
    return out


def histogram(values, lo=LO, hi=HI, step=BIN):
    n = int(round((hi - lo) / step))
    counts = [0] * n
    for v in values:
        k = int(math.floor((v - lo) / step + 1e-9))
        if 0 <= k < n:
            counts[k] += 1
    return [(lo + (k + 0.5) * step, counts[k]) for k in range(n)]


def two_phase(plateau=PLATEAU, knee=KNEE):
    """(c, K, x_sun): [Fe/H] = log10(c (x + K (x-1))), solar at x_sun."""
    c = 10 ** knee
    x_sun = 1 / (c * 10 ** plateau)
    k = (10 ** plateau - 1) * x_sun / (x_sun - 1)
    return c, k, x_sun


def alpha_track(x, plateau=PLATEAU, knee=KNEE):
    c, k, _ = two_phase(plateau, knee)
    ia = k * max(x - 1, 0.0)
    return math.log10(c * (x + ia)), plateau - math.log10(1 + ia / x)


def ia_share(x, plateau=PLATEAU, knee=KNEE):
    c, k, _ = two_phase(plateau, knee)
    ia = k * max(x - 1, 0.0)
    return ia / (x + ia)


def main():
    stars = load()
    feh = [f for f, _ in stars]
    low = [f for f, m in stars if m is not None and m <= 1.0]
    h_all, h_low = histogram(feh), histogram(low)
    n = len(feh)
    rows = []
    for (x, c), (_, cl) in zip(h_all, h_low):
        model = n * (frac_below(x + BIN / 2) - frac_below(x - BIN / 2))
        rows.append((x, c, cl, model))
    write_table(__file__, ("feh", "n_obs", "n_low", "model"), rows, part="mdf")
    xs = [LO + 0.02 * k for k in range(int((0.2 - LO) / 0.02) + 1)]
    write_table(__file__, ("feh", "frac_cum"), [(x, frac_below(x)) for x in xs], part="curve")
    c, k, x_sun = two_phase()
    track = []
    x = 0.05
    while x <= 6.0001:
        track.append(alpha_track(x))
        x = round(x + 0.05, 4)
    write_table(__file__, ("feh", "afe"), track, part="alpha")
    srt = sorted(feh)
    med = (srt[n // 2] + srt[(n - 1) // 2]) / 2
    mean = sum(feh) / n
    sd = math.sqrt(sum((v - mean) ** 2 for v in feh) / n)
    y = effective_yield(Z_SUN, MU1)
    vals = [["mu1", MU1], ["ln_inv_mu1", math.log(1 / MU1)], ["y_eff", y],
            ["y_over_zsun", y / Z_SUN],
            ["frac_below_m1", frac_below(-1.0)], ["frac_below_m05", frac_below(-0.5)],
            ["peak_feh_model", math.log10(1 / math.log(1 / MU1))],
            ["n_irfm", n], ["mean", mean], ["median", med], ["sd", sd],
            ["n_obs_below_m1", sum(v < -1 for v in feh)],
            ["obs_frac_below_m1", sum(v < -1 for v in feh) / n],
            ["n_low_mass", len(low)], ["n_low_below_m1", sum(v < -1 for v in low)],
            ["low_frac_below_m1", sum(v < -1 for v in low) / len(low)],
            ["c", c], ["K", k], ["x_sun", x_sun], ["ia_share_sun", ia_share(x_sun)],
            ["plateau_for_two_thirds", -math.log10(1 / 3)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
