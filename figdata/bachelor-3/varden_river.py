"""Chi plot of the upland river west of the Varden Hills and three of its
tributaries (Year 3, quantitative geomorphology). Invented network, built on
stream_profile.py: trunk area C_HACK d^H_HACK, tributary areas
C_TRIB s^H_HACK (s from each tributary's own divide), the same K, U, THETA,
outlet at region.river_z(0).

At steady state every channel of the network lies on one line of slope
ks A0^-THETA in the (chi, z) plane. For n = 1 a knickpoint travels the same
chi in the same time on every branch, so at a time t all knickpoints sit at
chi_k = K A0^THETA t, and above them the profile is the old one, DROP higher.

  part trunk    chi z d            trunk at the time T_FALL (d in km)
  part tribN    chi z s            tributary N at T_FALL (s in km)
  part knicks   chi zlo zhi        the knickpoints (lip zhi, foot zlo)
  part values   what value
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from _table import write_table  # noqa: E402
import stream_profile as sp  # noqa: E402

C_TRIB = 1.5
# (junction distance from the trunk divide, tributary length), metres
TRIBS = [(4000.0, 3000.0), (7000.0, 4000.0), (9500.0, 5000.0)]
S_HEAD = 300.0


def trib_area(s):
    return C_TRIB * np.asarray(s, dtype=float) ** sp.H_HACK


def trib_chi(j, s):
    dj, lt = TRIBS[j]
    s = np.asarray(s, dtype=float)
    return sp.chi(dj) + sp.A0 ** sp.THETA * C_TRIB ** -sp.THETA * (lt ** sp.P - s ** sp.P) / sp.P


def trib_z_ss(j, s):
    dj, lt = TRIBS[j]
    s = np.asarray(s, dtype=float)
    return sp.z_ss(dj) + sp.ks() * C_TRIB ** -sp.THETA * (lt ** sp.P - s ** sp.P) / sp.P


def chi_knick(t):
    return sp.K * sp.A0 ** sp.THETA * t


def z_on_chi(c, t, drop=sp.DROP):
    """Elevation at chi c anywhere in the network at time t after the fall."""
    base = sp.Z_OUT + sp.ks() * sp.A0 ** -sp.THETA * np.asarray(c, dtype=float)
    return np.where(np.asarray(c) > chi_knick(t), base + drop, base)


def trib_knick(j, t):
    """Distance s from the tributary divide of its knickpoint, or None if
    the knickpoint has not reached the junction."""
    dj, lt = TRIBS[j]
    ck = chi_knick(t)
    if ck <= sp.chi(dj):
        return None
    x = lt ** sp.P - (ck - sp.chi(dj)) * sp.P * C_TRIB ** sp.THETA / sp.A0 ** sp.THETA
    return x ** (1.0 / sp.P)


def main(t=sp.T_FALL):
    d = np.arange(sp.D_HEAD, sp.L + 1e-9, 50.0)
    c = sp.chi(d)
    write_table(__file__, ("chi", "z", "d"),
                [[a, b, x / 1000] for a, b, x in zip(c, sp.profile_at(d, t), d)], part="trunk")
    knicks = [[chi_knick(t), float(z_on_chi(chi_knick(t), t)), float(z_on_chi(chi_knick(t), t)) + sp.DROP]]
    for j, (dj, lt) in enumerate(TRIBS):
        s = np.arange(S_HEAD, lt + 1e-9, 50.0)
        cj = trib_chi(j, s)
        write_table(__file__, ("chi", "z", "s"),
                    [[a, b, x / 1000] for a, b, x in zip(cj, z_on_chi(cj, t), s)], part="trib%d" % (j + 1))
    vals = [["chi_knick", chi_knick(t)], ["ks_over_A0theta", sp.ks() * sp.A0 ** -sp.THETA],
            ["chi_head_trunk", float(sp.chi(sp.D_HEAD))]]
    for j, (dj, lt) in enumerate(TRIBS):
        vals.append(["chi_junction_%d" % (j + 1), float(sp.chi(dj))])
        vals.append(["chi_head_%d" % (j + 1), float(trib_chi(j, S_HEAD))])
        sk = trib_knick(j, t)
        vals.append(["knick_s_%d" % (j + 1), sk if sk is not None else -1.0])
    write_table(__file__, ("chi", "zlo", "zhi"), knicks, part="knicks")
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
