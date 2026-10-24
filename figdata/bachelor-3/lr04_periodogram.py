"""Periodograms of the LR04 benthic oxygen-isotope stack (Year 3, sequence
stratigraphy: cyclostratigraphy), and of a synthetic core for the weekend
problem.

LR04 is read from the shared derived table data/derived/lr04.csv (ledger
data:lr04); the stack is sampled every 1 kyr to 600 ka, 2 kyr to 1.5 Ma and
2.5 kyr beyond, so each window is interpolated linearly onto a uniform grid
of step DT_GRID before the transform. Method (the chapter's definition): remove
the mean and the least-squares line, multiply by a Hann taper, take the
discrete Fourier transform, and plot |X(f)|^2 normalised to its largest
value, against frequency in cycles per kyr.

The synthetic core: a series in depth, sampled every 1 cm over 30 m, built
from three sinusoids with periods 405, 100 and 41 kyr deposited at a constant
SED cm/kyr, plus a fixed pseudo-random noise (seeded). Its periodogram, in
cycles per metre, is what the reader of the problem works from.

  part young     f p              LR04, 0-1000 ka
  part old       f p              LR04, 1250-2500 ka
  part core      f p              synthetic core, f in cycles per metre
  part peaks     window period    periods (kyr, or m for the core) of the main peaks
"""
import csv
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

LR04 = os.path.join(HERE, "..", "..", "data", "derived", "lr04.csv")
DT_GRID = 1.0          # kyr
WINDOWS = {"young": (0.0, 1000.0), "old": (1250.0, 2500.0)}
F_MAX = 0.06           # cycles per kyr shown
SED = 2.0              # cm/kyr, synthetic core
CORE_PERIODS = (405.0, 100.0, 41.0)
CORE_AMPS = (0.6, 1.0, 0.7)
CORE_LEN_M = 30.0


def read_lr04(path=LR04):
    """Ages (ka) and d18O, up to the first non-increasing age."""
    ages, vals = [], []
    with open(path, newline="", encoding="utf8") as f:
        for row in csv.DictReader(f):
            a = float(row["age_ka"])
            if ages and a <= ages[-1]:
                break
            ages.append(a)
            vals.append(float(row["d18O_permil"]))
    return np.array(ages), np.array(vals)


def periodogram(y, dt):
    """Frequencies (cycles per unit of dt) and normalised power."""
    y = np.asarray(y, dtype=float)
    n = len(y)
    t = np.arange(n) * dt
    coef = np.polyfit(t, y, 1)
    r = (y - np.polyval(coef, t)) * np.hanning(n)
    spec = np.abs(np.fft.rfft(r)) ** 2
    f = np.fft.rfftfreq(n, dt)
    return f[1:], spec[1:] / spec[1:].max()


def window(ages, vals, lo, hi, dt=DT_GRID):
    grid = np.arange(lo, hi + 1e-9, dt)
    return grid, np.interp(grid, ages, vals)


def peaks(f, p, n=3, fmin=0.0):
    """Periods (1/f) of the n highest local maxima above fmin."""
    idx = [i for i in range(1, len(p) - 1)
           if p[i] > p[i - 1] and p[i] >= p[i + 1] and f[i] > fmin]
    idx.sort(key=lambda i: -p[i])
    return [1.0 / f[i] for i in idx[:n]]


def lr04_spectra():
    ages, vals = read_lr04()
    out = {}
    for name, (lo, hi) in WINDOWS.items():
        _, y = window(ages, vals, lo, hi)
        out[name] = periodogram(y, DT_GRID)
    return out


def core_series(dz_m=0.01):
    z = np.arange(0.0, CORE_LEN_M, dz_m)
    t = z * 100.0 / SED                      # kyr
    y = sum(a * np.sin(2 * np.pi * t / per + k)
            for k, (a, per) in enumerate(zip(CORE_AMPS, CORE_PERIODS)))
    rng = np.random.default_rng(16)
    return z, y + 0.3 * rng.standard_normal(len(z))


def main():
    spectra = lr04_spectra()
    for name, (f, p) in spectra.items():
        keep = f <= F_MAX
        write_table(__file__, ("f", "p"), np.column_stack([f[keep], p[keep]]), part=name)
    z, y = core_series()
    fc, pc = periodogram(y, 0.01)
    keep = fc <= 3.0
    write_table(__file__, ("f", "p"), np.column_stack([fc[keep], pc[keep]]), part="core")
    rows = []
    for name, (f, p) in spectra.items():
        for per in peaks(f, p, n=4, fmin=1 / 150.0):
            rows.append([name, per])
    for per in peaks(fc, pc, n=3, fmin=0.05):
        rows.append(["core", per])
    write_table(__file__, ("window", "period"), rows, part="peaks")


if __name__ == "__main__":
    main()
