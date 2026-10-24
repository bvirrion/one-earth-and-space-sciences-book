"""Sm-Nd model ages (Year 3, advanced geochronology).

143Nd/144Nd(t ago) = I_now - R (exp(lambda t) - 1) for a closed reservoir of
present 147Sm/144Nd = R. CHUR: I = 0.512638, R = 0.1966 (ledger white:chur);
depleted mantle: I = 0.51315, R = 0.2137, a closed evolution from CHUR at
4.55 Ga (ledger white08:model-age); lambda(147Sm) = 6.524e-12 /yr (ledger
villa20:sm147). eps_Nd = (I_sample / I_CHUR - 1) 1e4 at the same time.

The granite sample is invented: 147Sm/144Nd = 0.1100, 143Nd/144Nd = 0.511900.

  part evolution  t eps_dm eps_sample          (t in Ga before present)
  part values     what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

LAMBDA = 6.524e-12
CHUR = (0.512638, 0.1966)
DM = (0.51315, 0.2137)
SAMPLE = (0.511900, 0.1100)
T_EARTH = 4.55


def ratio_at(res, t_ga):
    i, r = res
    return i - r * math.expm1(LAMBDA * t_ga * 1e9)


def eps(res, t_ga):
    return (ratio_at(res, t_ga) / ratio_at(CHUR, t_ga) - 1.0) * 1e4


def model_age(sample, ref):
    """Age (Ga) at which the sample's back-calculated ratio meets the reference's."""
    return math.log1p((sample[0] - ref[0]) / (sample[1] - ref[1])) / LAMBDA / 1e9


def main():
    ts = np.linspace(0, 4.55, 92)
    write_table(__file__, ("t", "eps_dm", "eps_sample"),
                [[t, eps(DM, t), eps(SAMPLE, t)] for t in ts], part="evolution")
    write_table(__file__, ("what", "value"), [
        ["T_CHUR", model_age(SAMPLE, CHUR)], ["T_DM", model_age(SAMPLE, DM)],
        ["eps_now", eps(SAMPLE, 0.0)], ["eps_dm_now", eps(DM, 0.0)],
        ["dm_at_4.55_minus_chur", ratio_at(DM, T_EARTH) - ratio_at(CHUR, T_EARTH)],
    ], part="values")


if __name__ == "__main__":
    main()
