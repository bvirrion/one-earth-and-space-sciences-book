"""Thermal infrared (Year 3, remote sensing): Planck's law, its inversion into a
brightness temperature, and the brightness temperature of a surface of emissivity
below one or of a pixel that mixes a hot and a cool part.

Constants: h, c, k exact (ledger const:h, const:c, const:kB). The band is taken as
one wavelength, the centre of Landsat TIRS band 10 (10.6-11.19 um, ledger
usgs:landsat8-bands), 10.895 um; the atmosphere is neglected (an atmospherically
corrected radiance).

  B(lam, T)        spectral radiance, W m^-2 sr^-1 m^-1
  t_bright(lam, L) the temperature of the black body of radiance L at lam
  part planck   um b300 b400 b1443     radiance in W m^-2 sr^-1 um^-1 (log axis)
  part mixed    f tb                   pixel with a fraction f at 370 K in a 290 K
                                       background: its brightness temperature
  part values   what value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23
C1 = 2 * H * C ** 2          # W m^2 sr^-1 (radiance form)
C2 = H * C / KB              # m K
LAM10 = 0.5 * (10.6 + 11.19) * 1e-6
T_LAVA = 1170.0 + 273.15   # K, Kilauea eruption temperature (ledger usgs:kilauea-temp)


def planck(lam, t):
    """Spectral radiance of a black body, W m^-2 sr^-1 per metre of wavelength."""
    return C1 / lam ** 5 / math.expm1(C2 / (lam * t))


def t_bright(lam, rad):
    """Brightness temperature (K) of the radiance rad at wavelength lam."""
    return C2 / (lam * math.log1p(C1 / (lam ** 5 * rad)))


def t_grey(lam, t, eps):
    """Brightness temperature of a surface at t with emissivity eps (no reflected sky)."""
    return t_bright(lam, eps * planck(lam, t))


def t_mixed(lam, f, t_hot, t_bg):
    return t_bright(lam, f * planck(lam, t_hot) + (1 - f) * planck(lam, t_bg))


def wien_peak_um(t):
    """Wavelength of the maximum of B_lambda, by Newton on 5(1 - e^-x) = x."""
    x = 5.0
    for _ in range(50):
        g = 5 * (1 - math.exp(-x)) - x
        dg = 5 * math.exp(-x) - 1
        x -= g / dg
    return C2 / (x * t) * 1e6


def main():
    lam = np.round(np.arange(1.0, 25.001, 0.1), 1)
    write_table(__file__, ("um", "b300", "b400", "b1443"),
                [(u, planck(u * 1e-6, 300) * 1e-6, planck(u * 1e-6, 400) * 1e-6,
                  planck(u * 1e-6, T_LAVA) * 1e-6) for u in lam], part="planck")
    fs = np.round(np.arange(0.0, 1.0001, 0.01), 2)
    write_table(__file__, ("f", "tb"), [(f, t_mixed(LAM10, f, 370.0, 290.0)) for f in fs],
                part="mixed")
    vals = [["lam10_um", LAM10 * 1e6], ["c2_mK", C2],
            ["L300_W_m2_sr_um", planck(LAM10, 300) * 1e-6],
            ["tb_300_e095", t_grey(LAM10, 300, 0.95)], ["tb_300_e098", t_grey(LAM10, 300, 0.98)],
            ["tb_300_e099", t_grey(LAM10, 300, 0.99)],
            ["tb_mix_f005", t_mixed(LAM10, 0.05, 370, 290)],
            ["tb_mix_f010", t_mixed(LAM10, 0.10, 370, 290)],
            ["tmean_f005", 0.05 * 370 + 0.95 * 290],
            ["wien_300_um", wien_peak_um(300)], ["wien_lava_um", wien_peak_um(T_LAVA)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
