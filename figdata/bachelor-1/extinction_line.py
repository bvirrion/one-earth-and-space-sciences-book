"""An extinction line (Year 1, observing-the-sky): the magnitude of one star
measured at six airmasses through a night, and the least-squares line
m = m0 + k X. The measurements are invented for the exercise (printed in the
chapter's table); nothing here is a real-world value.

  part obs     X m
  part fit     X m        the fitted line from X = 0 to X = 2.5
  part values  what value  k, m0, rms
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

OBS = ((1.05, 8.024), (1.18, 8.031), (1.36, 8.072), (1.62, 8.104), (1.95, 8.171), (2.31, 8.216))


def fit(obs=OBS):
    """Least-squares slope k and intercept m0 of m against X."""
    n = len(obs)
    sx = sum(x for x, _ in obs)
    sy = sum(y for _, y in obs)
    sxx = sum(x * x for x, _ in obs)
    sxy = sum(x * y for x, y in obs)
    k = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    m0 = (sy - k * sx) / n
    return k, m0


def rms(obs=OBS):
    k, m0 = fit(obs)
    return (sum((y - m0 - k * x) ** 2 for x, y in obs) / len(obs)) ** 0.5


if __name__ == "__main__":
    k, m0 = fit()
    write_table(__file__, ("X", "m"), OBS, part="obs", digits=5)
    write_table(__file__, ("X", "m"), [(0.0, m0), (2.5, m0 + 2.5 * k)], part="fit", digits=5)
    write_table(__file__, ("what", "value"), [("k", k), ("m0", m0), ("rms", rms())], part="values", digits=5)
