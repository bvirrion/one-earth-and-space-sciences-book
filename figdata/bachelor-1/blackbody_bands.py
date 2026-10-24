"""Planck curves of three black bodies and the pivot wavelengths of the
U, B, V, R, I filters (Year 1, observing-the-sky).

Constants h, c, k_B and Wien's b are exact (CODATA 2022; ledger const:h,
const:c, const:kB, const:b). 5772 K is the Sun's effective temperature
(nasa:sun-Teff); 3500 K and 10 000 K are round illustrative values. Pivot
wavelengths of the Bessell filters from baldry:bessell-pivot.

  part curves   lam_nm t3500 t5772 t10000   B_lambda / its own maximum
  part bands    name lam_nm
  part values   T peak_nm b_over_T_nm BV_ratio
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23
WIEN_B = 2.897771955e-3
TEMPS = (3500.0, 5772.0, 10000.0)
BANDS = (("U", 358.5), ("B", 437.1), ("V", 547.8), ("R", 650.4), ("I", 802.0))


def planck(lam_nm, T):
    """Spectral radiance B_lambda (W m^-3 sr^-1) at wavelength lam_nm (nm)."""
    lam = lam_nm * 1e-9
    return 2 * H * C ** 2 / lam ** 5 / math.expm1(H * C / (lam * KB * T))


def peak_nm(T, lo=50.0, hi=5000.0):
    """Wavelength of the maximum of B_lambda, by golden-section search."""
    g = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    for _ in range(200):
        c1, c2 = b - g * (b - a), a + g * (b - a)
        if planck(c1, T) > planck(c2, T):
            b = c2
        else:
            a = c1
    return (a + b) / 2


def bv_ratio(T):
    """B_lambda at the B pivot over B_lambda at the V pivot."""
    return planck(437.1, T) / planck(547.8, T)


def curves(lams):
    peaks = [planck(peak_nm(T), T) for T in TEMPS]
    return [(lam,) + tuple(planck(lam, T) / p for T, p in zip(TEMPS, peaks)) for lam in lams]


if __name__ == "__main__":
    lams = [200 + 5 * k for k in range(0, 261)]          # 200 to 1500 nm
    write_table(__file__, ("lam_nm", "t3500", "t5772", "t10000"), curves(lams), part="curves", digits=5)
    write_table(__file__, ("name", "lam_nm"), BANDS, part="bands", digits=5)
    write_table(__file__, ("T", "peak_nm", "b_over_T_nm", "BV_ratio"),
                [(T, peak_nm(T), WIEN_B / T * 1e9, bv_ratio(T)) for T in TEMPS], part="values", digits=5)
