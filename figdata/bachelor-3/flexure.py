"""Flexure of an elastic lithosphere under a line load and at a trench (Year 3,
gravity-geodesy).

Thin-plate equation (the chapter's theorem): D w'''' + drho g w = q(x), with the
flexural rigidity D = E Te^3 / (12 (1 - nu^2)) and the flexural parameter
alpha = (4 D / (drho g))^(1/4). Analytic solutions (x >= 0, w positive down):
  continuous plate, line load V0 at x = 0:
      w = w0 exp(-x/alpha) (cos(x/alpha) + sin(x/alpha)),  w0 = V0 alpha^3 / (8 D)
  broken plate, end load at x = 0 (a trench):
      w = w0 exp(-x/alpha) cos(x/alpha)
Elastic constants E = 100 GPa, nu = 0.25 (the values of the Hawaiian-Emperor study,
ledger watts25:te); mantle 3300 kg/m3 and sea water 1030 kg/m3 (a water-filled moat).
The load is the chapter's Oru ridge: a triangle 80 km wide and 6 km high of
density 2800 kg/m3 in water (V0 = (2800 - 1030) g A).

  part profiles  x w10 w25 w40      x (km, both sides), deflection (m, down positive)
                                    under the Oru load for Te = 10, 25, 40 km
  part broken    x w                broken plate, Te = 25 km, w0 = 1000 m
  part values    what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

E = 100e9
NU = 0.25
G = 9.81
RHO_M = 3300.0
RHO_W = 1030.0
RHO_V = 2800.0
RIDGE_WIDTH = 80e3
RIDGE_HEIGHT = 6e3
TE_LIST = (10e3, 25e3, 40e3)


def rigidity(te, e=E, nu=NU):
    return e * te ** 3 / (12.0 * (1.0 - nu ** 2))


def flexural_parameter(d, drho=RHO_M - RHO_W, g=G):
    return (4.0 * d / (drho * g)) ** 0.25


def elastic_thickness(d, e=E, nu=NU):
    return (12.0 * (1.0 - nu ** 2) * d / e) ** (1.0 / 3.0)


def ridge_load(width=RIDGE_WIDTH, height=RIDGE_HEIGHT, rho=RHO_V, rho_w=RHO_W, g=G):
    """Line load (N/m) of a triangular ridge in water."""
    return (rho - rho_w) * g * 0.5 * width * height


def line_load(x, v0, d, drho=RHO_M - RHO_W):
    a = flexural_parameter(d, drho)
    w0 = v0 * a ** 3 / (8.0 * d)
    u = abs(x) / a
    return w0 * math.exp(-u) * (math.cos(u) + math.sin(u))


def broken_plate(x, w0, a):
    u = x / a
    return w0 * math.exp(-u) * math.cos(u)


if __name__ == "__main__":
    v0 = ridge_load()
    ds = [rigidity(t) for t in TE_LIST]
    rows = []
    for k in range(-400, 401, 2):
        x = k * 1e3
        rows.append((k,) + tuple(line_load(x, v0, d) for d in ds))
    write_table(__file__, ("x", "w10", "w25", "w40"), rows, part="profiles")
    a25 = flexural_parameter(ds[1])
    rows = [(k, broken_plate(k * 1e3, 1000.0, a25)) for k in range(0, 401, 2)]
    write_table(__file__, ("x", "w"), rows, part="broken")
    vals = [("V0_N_per_m", v0)]
    for t, d in zip(TE_LIST, ds):
        a = flexural_parameter(d)
        vals += [("D_%d" % (t / 1e3), d), ("alpha_km_%d" % (t / 1e3), a / 1e3),
                 ("w0_m_%d" % (t / 1e3), v0 * a ** 3 / (8 * d)),
                 ("xbulge_km_%d" % (t / 1e3), math.pi * a / 1e3),
                 ("bulge_m_%d" % (t / 1e3), v0 * a ** 3 / (8 * d) * math.exp(-math.pi))]
    vals += [("broken_x0_km", math.pi / 2 * a25 / 1e3), ("broken_xb_km", 0.75 * math.pi * a25 / 1e3),
             ("broken_bulge_m", 1000 * math.exp(-0.75 * math.pi) * math.cos(0.75 * math.pi))]
    write_table(__file__, ("what", "value"), vals, part="values")
