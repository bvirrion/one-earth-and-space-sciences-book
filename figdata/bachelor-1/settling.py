"""Settling velocity of quartz grains in water (Year 1, erosion-transport).

Stokes' law (the drag 3 pi mu d w on a sphere of diameter d, physics books)
balanced against the submerged weight gives

    w_Stokes = R g d^2 / (18 nu),     R = (rho_s - rho) / rho,

valid while the grain Reynolds number w d / nu stays below about 1. The combined
law of Ferguson and Church (2004, ledger fc:settling) joins it to a turbulent
drag law for coarse grains:

    w = R g d^2 / (C1 nu + sqrt(0.75 C2 R g d^3)),

with C1 = 18, C2 = 1.0 for natural grains measured by sieving. Water at 20 C and
0.101325 MPa: density 998.207 kg/m3 and dynamic viscosity 1.0016 mPa s (NIST
WebBook, ledger nist:water); quartz 2650 kg/m3 (hom:quartz); g = 9.81 m/s2
(const:gn, rounded).

  part curves   d_mm w_stokes w_fc re_fc     velocities in m/s
  part values   what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

G = 9.81
RHO_W = 998.207        # kg/m3, water at 20 C (NIST)
MU = 1.0016e-3         # Pa s, water at 20 C
RHO_Q = 2650.0         # kg/m3, quartz
NU = MU / RHO_W        # m2/s
R_Q = (RHO_Q - RHO_W) / RHO_W
C1, C2 = 18.0, 1.0     # natural grains, sieve diameters


def stokes(d, R=R_Q, nu=NU, g=G):
    """Stokes settling velocity (m/s) of a sphere of diameter d (m)."""
    return R * g * d * d / (18.0 * nu)


def ferguson_church(d, R=R_Q, nu=NU, g=G, c1=C1, c2=C2):
    """Settling velocity (m/s) by the combined law, all grain sizes."""
    return R * g * d * d / (c1 * nu + math.sqrt(0.75 * c2 * R * g * d ** 3))


def reynolds(d, w, nu=NU):
    return w * d / nu


def stokes_limit_diameter(R=R_Q, nu=NU, g=G):
    """The diameter whose Stokes velocity gives a grain Reynolds number of 1."""
    return (18.0 * nu * nu / (R * g)) ** (1.0 / 3.0)


def log_grid(lo, hi, n):
    a, b = math.log10(lo), math.log10(hi)
    return [10 ** (a + (b - a) * i / (n - 1)) for i in range(n)]


def main():
    rows = []
    for d_mm in log_grid(1e-3, 10.0, 81):
        d = d_mm * 1e-3
        w = ferguson_church(d)
        rows.append((round(d_mm, 6), stokes(d), w, reynolds(d, w)))
    write_table(__file__, ("d_mm", "w_stokes", "w_fc", "re_fc"), rows, part="curves")
    values = [("R", R_Q), ("nu", NU), ("d_stokes_limit_mm", stokes_limit_diameter() * 1e3)]
    for d_mm in (0.002, 0.01, 0.063, 0.1, 0.5, 1.0, 2.0, 10.0):
        d = d_mm * 1e-3
        values.append(("w_stokes_%g_mm" % d_mm, stokes(d)))
        values.append(("w_fc_%g_mm" % d_mm, ferguson_church(d)))
    write_table(__file__, ("what", "value"), values, part="values")


if __name__ == "__main__":
    main()
