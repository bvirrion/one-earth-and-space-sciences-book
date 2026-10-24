"""Interference colours of a crystal plate between crossed polars, computed from first
principles (Year 1, optical-mineralogy): the Michel-Levy chart.

A plate of retardation D (nm), at 45 degrees from extinction between crossed polars,
transmits the fraction T(lambda) = sin^2(pi D / lambda) of each wavelength. The light is
CIE standard illuminant D65 (data/derived/bachelor-1-cie-d65.csv, CIE, CC BY-SA 4.0);
the colour is integrated with the CIE 1931 2-degree colour-matching functions
(data/derived/bachelor-1-cie1931.csv, CIE, CC BY-SA 4.0) and converted to sRGB with the
matrix and the transfer function of the CSS Color 4 specification (W3C). The colours are
normalised to the light that parallel polars would pass (Y = 1 for D65): a plate of half a
wavelength passes that wavelength entirely, and the high-order white, which passes half the
light on average, is a light grey. Values outside the sRGB gamut are clipped.

  part chart     delta d r g b          colour of the chart (columns of constant retardation)
                                        on a mesh of 2 rows: d = 0 and d = 50 micrometres
  part lines     delta x1 y1            birefringence lines delta = D/d, clipped to the chart
  part segments  x y                    the same lines as segments from the origin, separated
                                        by a row of nan (pgfplots: unbounded coords=jump)
  part strip     delta r g b            the colours alone, one row per 5 nm of retardation
  part rotation  theta I100 I270 I540   I/I0 against the stage angle theta (degrees, from
                                        extinction) for retardations 100, 270 and 540 nm, at
                                        the wavelength 550 nm: sin^2(2 theta) sin^2(pi D/lambda)
  part values    what value             minima of the linear green channel (the red-violet
                                        tints that end each order) and their saturation
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
DERIVED = os.path.join(ROOT, "data", "derived")

# CSS Color Module Level 4, sample code XYZ_to_lin_sRGB (D65, exact rationals)
M_XYZ_TO_RGB = (
    (12831 / 3959, -329 / 214, -1974 / 3959),
    (-851781 / 878810, 1648619 / 878810, 36519 / 878810),
    (705 / 12673, -2585 / 12673, 705 / 667),
)
DISPLAY_GAIN = 1.0
D_MAX = 1800.0          # nm, right edge of the chart
T_MAX = 50.0            # micrometres, top of the chart
# birefringences drawn on the chart (ledger hom:*, rounded): mineral, delta
LINES = (("orthoclase", 0.005), ("quartz", 0.009), ("plagioclase", 0.012), ("hornblende", 0.020),
         ("diopside", 0.030), ("forsterite", 0.035), ("muscovite", 0.040), ("fayalite", 0.052),
         ("calcite", 0.172))


def _read(name):
    with open(os.path.join(DERIVED, name), encoding="utf8") as f:
        return list(csv.DictReader(f))


def tables():
    """wavelengths (nm), D65 power, xbar, ybar, zbar on the common 1-nm grid 360-830 nm."""
    d65 = {int(r["nm"]): float(r["s"]) for r in _read("bachelor-1-cie-d65.csv")}
    cmf = {int(r["nm"]): (float(r["xbar"]), float(r["ybar"]), float(r["zbar"]))
           for r in _read("bachelor-1-cie1931.csv")}
    nm = sorted(set(d65) & set(cmf))
    return nm, [d65[k] for k in nm], [cmf[k] for k in nm]


_T = None


def _tab():
    global _T
    if _T is None:
        _T = tables()
    return _T


def xyz(transmission):
    """XYZ (white Y = 1) of D65 light through a filter transmission(lambda_nm)."""
    nm, s, c = _tab()
    norm = sum(si * ci[1] for si, ci in zip(s, c))
    acc = [0.0, 0.0, 0.0]
    for lam, si, ci in zip(nm, s, c):
        t = transmission(lam)
        for k in range(3):
            acc[k] += si * t * ci[k]
    return [a / norm for a in acc]


def linear_rgb(XYZ):
    return [sum(m * v for m, v in zip(row, XYZ)) for row in M_XYZ_TO_RGB]


def gamma(v):
    v = min(1.0, max(0.0, v))
    return 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055


def transmission(delta_nm):
    return lambda lam: math.sin(math.pi * delta_nm / lam) ** 2


def colour(delta_nm, gain=DISPLAY_GAIN):
    """sRGB (0..1) of a plate of retardation delta_nm at 45 degrees between crossed polars."""
    X, Y, Z = xyz(transmission(delta_nm))
    return [gamma(gain * v) for v in linear_rgb((X, Y, Z))]


def saturation(delta_nm):
    """Distance in the CIE xy chromaticity diagram from the white point of D65."""
    X, Y, Z = xyz(transmission(delta_nm))
    Xw, Yw, Zw = xyz(lambda lam: 1.0)
    s, sw = X + Y + Z, Xw + Yw + Zw
    return math.hypot(X / s - Xw / sw, Y / s - Yw / sw)


def green_minima(lo=300.0, hi=1800.0, step=1.0):
    """Retardations of the local minima of the linear (unclipped) green channel: the
    red-violet tints that end the first, second and third orders."""
    xs = [lo + i * step for i in range(int((hi - lo) / step) + 1)]
    g = [linear_rgb(xyz(transmission(x)))[1] for x in xs]
    return [xs[i] for i in range(1, len(xs) - 1) if g[i] < g[i - 1] and g[i] <= g[i + 1]]


def intensity(theta_deg, delta_nm, lam_nm=550.0):
    """I/I0 between crossed polars: sin^2(2 theta) sin^2(pi delta / lambda)."""
    return math.sin(math.radians(2 * theta_deg)) ** 2 * math.sin(math.pi * delta_nm / lam_nm) ** 2


def lines():
    out = []
    for _, d in LINES:
        x1 = min(D_MAX, d * T_MAX * 1000.0)
        out.append((d, x1, x1 / (d * 1000.0)))
    return out


if __name__ == "__main__":
    xs = [i * 5.0 for i in range(int(D_MAX / 5) + 1)]
    cols = [colour(x) for x in xs]
    rows = []
    for d in (0.0, T_MAX):
        rows += [(x, d) + tuple(round(v, 4) for v in c) for x, c in zip(xs, cols)]
    write_table(__file__, ("delta", "d", "r", "g", "b"), rows, part="chart", digits=6)
    write_table(__file__, ("delta", "x1", "y1"), lines(), part="lines", digits=6)
    seg = []
    for _, x1, y1 in lines():
        seg += [(0.0, 0.0), (x1, y1), ("nan", "nan")]
    write_table(__file__, ("x", "y"), seg[:-1], part="segments", digits=6)
    rot = [(th, intensity(th, 100.0), intensity(th, 270.0), intensity(th, 540.0)) for th in range(0, 361, 2)]
    write_table(__file__, ("theta", "I100", "I270", "I540"), rot, part="rotation", digits=5)
    mins = green_minima()
    vals = [("n_wavelengths", len(_tab()[0]))]
    vals += [("green_min_%d" % (i + 1), m) for i, m in enumerate(mins)]
    vals += [("saturation_at_min_%d" % (i + 1), saturation(m)) for i, m in enumerate(mins)]
    vals += [("saturation_5000", saturation(5000.0))]
    strip = [(x,) + tuple(round(v, 4) for v in colour(x)) for x in xs]
    write_table(__file__, ("delta", "r", "g", "b"), strip, part="strip", digits=6)
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)
