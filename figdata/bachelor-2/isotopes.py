"""Isotope geochemistry (Year 2, isotope-geochemistry): epsilon-Nd evolution of CHUR, a
depleted mantle and a crust, Sr-Nd isotopes of ocean island basalts, two-component mixing
curves, and the water isotopes of the meteoric water line.

  CHUR today  143Nd/144Nd = 0.512638, 147Sm/144Nd = 0.1966          (ledger white:chur)
  lambda_147  6.524e-12 /yr                                         (ledger villa20:sm147)
  lambda_87   1.3972e-11 /yr                                        (ledger villa22:rb87, Book 2)
  ratio at time t ago   R(t) = R_now - P/D (exp(lambda t) - 1)
  epsilon     eps(t) = 1e4 (R_sample(t) / R_CHUR(t) - 1)
  linear      d eps / dt (forward in time) = Q f,  Q = 1e4 lambda (147/144)_CHUR / (143/144)_CHUR,
              f = (Sm/Nd)_sample / (Sm/Nd)_CHUR - 1
  depleted mantle: closed since 4.567 Ga with the f that brings it to the MORB mean today
              (143Nd/144Nd 0.513074, ledger gale13:isotopes)
  crust:      extracted from that mantle at 2.7 Ga with the upper crust's Sm/Nd (4.7/27,
              ledger rg03:ucc-trace) against the CI value (0.145/0.457, ledger lodders:ci-table)
  mixing      C_mix = f C_A + (1-f) C_B;  R_mix = (f C_A R_A + (1-f) C_B R_B) / C_mix
  water       delta_vapour = 1000/alpha - 1000 for liquid at delta 0       (ledger kc98:alpha)

  part chur, dm, crust   t_Ga eps          (t in Ga before present)
  part himu, em1         sr eps            (dataset bachelor-2-oib-isotopes)
  part morb              sr eps
  part mixK<k>           x y               (normalised mixing curves, K = 0.2, 1, 5)
  part mwl               d18O dD           (meteoric water line, -55 to +5)
  part values            what value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
DATA = os.path.join(ROOT, "data", "derived", "bachelor-2-oib-isotopes.csv")

R_CHUR = 0.512638           # white:chur
SMND_CHUR = 0.1966          # white:chur
LAM_SM = 6.524e-12          # villa20:sm147
LAM_RB = 1.3972e-11         # villa22:rb87
T_EARTH = 4.567e9           # lugaro:cai (CAI age 4567 Myr)
MORB_ND = 0.513074          # gale13:isotopes
MORB_SR = 0.702819          # gale13:isotopes
SMND_CI = 0.145 / 0.457     # lodders:ci-table (mass ratio)
SMND_UCC = 4.7 / 27.0       # rg03:ucc-trace (mass ratio)
T_CRUST = 2.7e9
ALPHA = {20: (1.0098, 1.084), 0: (1.0117, 1.111)}   # kc98:alpha (18O, 2H), liquid-vapour


def r_chur(t):
    """143Nd/144Nd of CHUR t years ago."""
    return R_CHUR - SMND_CHUR * (math.exp(LAM_SM * t) - 1)


def eps_nd(r, t=0.0):
    return 1e4 * (r / r_chur(t) - 1)


def q_factor():
    """Q in epsilon units per Gyr."""
    return 1e4 * LAM_SM * SMND_CHUR / R_CHUR * 1e9


def f_smnd(smnd_mass):
    return smnd_mass / SMND_CI - 1


def dm_smnd():
    """147Sm/144Nd of a mantle closed since T_EARTH, starting at CHUR, that reaches the MORB
    ratio today: R_now = R_CHUR(T) + P/D (exp(lam T) - 1)."""
    return (MORB_ND - r_chur(T_EARTH)) / (math.exp(LAM_SM * T_EARTH) - 1)


def r_dm(t):
    return MORB_ND - dm_smnd() * (math.exp(LAM_SM * t) - 1)


def crust_smnd():
    return SMND_CHUR * (1 + f_smnd(SMND_UCC))


def r_crust(t):
    """crust extracted from the depleted mantle at T_CRUST; ratio t years ago (t < T_CRUST)."""
    r0 = r_dm(T_CRUST)
    return r0 + crust_smnd() * (math.exp(LAM_SM * (T_CRUST - t)) - 1)


def mix(f, ca, ra, cb, rb):
    c = f * ca + (1 - f) * cb
    return c, (f * ca * ra + (1 - f) * cb * rb) / c


def mix_normalised(f, k):
    """Normalised isotope ratios of an A-B mixture with mass fraction f of A: each ratio is
    rescaled to 0 at B and 1 at A, so that it equals the share of the element that comes
    from A. With the x-element equally concentrated in A and B, x = f; the y-element is k
    times more concentrated, relative to the x-element, in A than in B:
    k = (C_y/C_x)_A / (C_y/C_x)_B, and y = f k / (f k + 1 - f)."""
    x = f
    y = f * k / (f * k + (1 - f))
    return x, y


def vapour(t_c):
    a18, ad = ALPHA[t_c]
    return 1000 / a18 - 1000, 1000 / ad - 1000


def oib(kind):
    out = []
    with open(DATA, encoding="utf8") as fh:
        for r in csv.DictReader(fh):
            if r["type"] == kind:
                out.append((float(r["sr87_86"]), eps_nd(float(r["nd143_144"]))))
    return sorted(out)


if __name__ == "__main__":
    ts = [T_EARTH / 1e9 * i / 60 for i in range(61)]
    write_table(__file__, ("t_Ga", "eps"), [(t, 0.0) for t in ts], part="chur")
    write_table(__file__, ("t_Ga", "eps"), [(t, eps_nd(r_dm(t * 1e9), t * 1e9)) for t in ts],
                part="dm")
    tc = [T_CRUST / 1e9 * i / 40 for i in range(41)]
    write_table(__file__, ("t_Ga", "eps"), [(t, eps_nd(r_crust(t * 1e9), t * 1e9)) for t in tc],
                part="crust")
    write_table(__file__, ("sr", "eps"), oib("HIMU"), part="himu")
    write_table(__file__, ("sr", "eps"), oib("EM1"), part="em1")
    write_table(__file__, ("sr", "eps"), [(MORB_SR, eps_nd(MORB_ND))], part="morb")
    fs = [i / 200 for i in range(201)]
    for k in (0.2, 1.0, 5.0):
        write_table(__file__, ("x", "y"), [mix_normalised(f, k) for f in fs],
                    part="mixK%02d" % int(round(k * 10)))
    write_table(__file__, ("d18O", "dD"), [(x, 8 * x + 10) for x in (-55, 5)], part="mwl")
    v20, v0 = vapour(20), vapour(0)
    vals = [
        ("Q_per_Gyr", q_factor()),
        ("eps_morb", eps_nd(MORB_ND)),
        ("chur_at_Tearth", r_chur(T_EARTH)),
        ("dm_smnd", dm_smnd()),
        ("f_dm", dm_smnd() / SMND_CHUR - 1),
        ("f_ucc", f_smnd(SMND_UCC)),
        ("crust_smnd", crust_smnd()),
        ("eps_dm_at_2.7Ga", eps_nd(r_dm(T_CRUST), T_CRUST)),
        ("eps_crust_now", eps_nd(r_crust(0))),
        ("vap20_d18O", v20[0]), ("vap20_dD", v20[1]), ("slope20", v20[1] / v20[0]),
        ("vap0_d18O", v0[0]), ("vap0_dD", v0[1]), ("slope0", v0[1] / v0[0]),
        ("vpdb_on_vsmow", (2.0672e-3 / 2.0052e-3 - 1) * 1000),   # kc98:standards
    ]
    write_table(__file__, ("what", "value"), vals, part="values")
