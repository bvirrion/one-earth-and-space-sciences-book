"""Hydrostatic flattening of a rotating planet against its moment of inertia
(Year 3, gravity-geodesy).

Data: GRS80 defining and derived constants (ledger geod5:grs80): m = w^2 a^2 b / GM
= 0.00344978600308, f = 0.00335281068118, J2 = 0.00108263; the Earth's moment-of-
inertia factor 0.3308 (shared earth:MoI), used as C/(M a^2).

Darwin-Radau relation (admitted in the chapter), for a planet in hydrostatic
equilibrium:  C/(M a^2) = (2/3) [1 - (2/5) sqrt(1 + eta)],  eta = (5/2) m/f - 2,
inverted:     f = (5/2) m / (2 + eta),  1 + eta = [ (5/2) (1 - (3/2) C/(M a^2)) ]^2.
First-order Clairaut relation: J2 = (2 f - m) / 3.

  part curve     moi f_inv          the hydrostatic flattening (as 1/f) for the
                                    Earth's m, moment-of-inertia factor 0.30-0.40
  part values    what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

M_GRS80 = 0.00344978600308
F_GRS80 = 0.00335281068118
J2_GRS80 = 0.00108263
MOI = 0.3308


def radau_flattening(moi, m=M_GRS80):
    s = 2.5 * (1.0 - 1.5 * moi)
    one_plus_eta = s * s
    return 2.5 * m / (1.0 + one_plus_eta)


def radau_moi(f, m=M_GRS80):
    eta = 2.5 * m / f - 2.0
    return 2.0 / 3.0 * (1.0 - 0.4 * math.sqrt(1.0 + eta))


def clairaut_j2(f, m=M_GRS80):
    return (2.0 * f - m) / 3.0


def clairaut_f(j2, m=M_GRS80):
    return (3.0 * j2 + m) / 2.0


if __name__ == "__main__":
    rows = []
    for k in range(0, 101):
        moi = 0.30 + 0.001 * k
        rows.append((moi, 1.0 / radau_flattening(moi)))
    write_table(__file__, ("moi", "f_inv"), rows, part="curve")
    fh = radau_flattening(MOI)
    vals = [("m", M_GRS80), ("f_hydro", fh), ("f_hydro_inv", 1 / fh), ("f_obs_inv", 1 / F_GRS80),
            ("f_uniform_inv", 1 / radau_flattening(0.4)), ("f_clairaut", clairaut_f(J2_GRS80)),
            ("j2_clairaut", clairaut_j2(F_GRS80)), ("H", J2_GRS80 / MOI)]
    write_table(__file__, ("what", "value"), vals, part="values")
