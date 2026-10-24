"""Weather systems (Year 2, weather-systems): the Lorenz (1963) system as a toy model of the
atmosphere's sensitivity to initial conditions.

  system       dx/dt = sigma (y - x), dy/dt = x (r - z) - y, dz/dt = x y - b z with the
               classical values sigma = 10, r = 28, b = 8/3 (nolitia22:lorenz), integrated by
               fourth-order Runge--Kutta with a time step of 0.01.
  start        the run starts at (1, 1, 1) and is integrated for 20 time units so that it lies
               on the attractor (the spin-up is not plotted).
  traj         two runs from that point and from the same point moved by 1e-5 in x.
  butterfly    one run, 40 time units, x and z every second step.
  growth       200 pairs of runs: the first members start at 200 points of a long run, 0.5
               time units apart; each second member starts 1e-8 away along (1, 1, 1)/sqrt 3.
               The distance between the members of each pair is averaged as a geometric
               mean (mean of the natural log), every 0.1 time units up to 30.
  fit          least-squares straight line through ln(mean distance) between t = 2 and 16,
               where the growth is exponential; its slope estimates the largest Lyapunov
               exponent.
  lyapunov     Benettin's method: a companion run 1e-8 away, renormalized every 0.1 time
               units over 2000 time units; the mean log stretching rate is the largest
               Lyapunov exponent (published value 0.906, nolitia22:lorenz).

  part traj      t x1 x2
  part butterfly x z
  part growth    t log10d fit         (log10 of the geometric-mean distance; fitted line,
                                       drawn up to t = 22 only)
  part numbers   key value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

SIGMA, R, B = 10.0, 28.0, 8.0 / 3.0
DT = 0.01


def deriv(s):
    """Right-hand side for states s of shape (..., 3)."""
    x, y, z = s[..., 0], s[..., 1], s[..., 2]
    return np.stack((SIGMA * (y - x), x * (R - z) - y, x * y - B * z), axis=-1)


def rk4(s, dt=DT):
    k1 = deriv(s)
    k2 = deriv(s + 0.5 * dt * k1)
    k3 = deriv(s + 0.5 * dt * k2)
    k4 = deriv(s + dt * k3)
    return s + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)


def run(s0, tmax, dt=DT):
    """States every dt from s0 (included) to tmax."""
    n = int(round(tmax / dt))
    out = np.empty((n + 1,) + np.shape(s0))
    s = np.array(s0, dtype=float)
    out[0] = s
    for i in range(n):
        s = rk4(s, dt)
        out[i + 1] = s
    return out


def fixed_points():
    c = math.sqrt(B * (R - 1.0))
    return [(0.0, 0.0, 0.0), (c, c, R - 1.0), (-c, -c, R - 1.0)]


def divergence():
    """d/dx + d/dy + d/dz of the vector field: constant, -(sigma + 1 + b)."""
    return -(SIGMA + 1.0 + B)


def start():
    return run(np.array([1.0, 1.0, 1.0]), 20.0)[-1]


def lyapunov(tmax=2000.0, d0=1e-8, every=0.1):
    s = start()
    u = s + d0 * np.ones(3) / math.sqrt(3.0)
    m = int(round(every / DT))
    total, t = 0.0, 0.0
    while t < tmax - 1e-9:
        for _ in range(m):
            s = rk4(s)
            u = rk4(u)
        d = float(np.linalg.norm(u - s))
        total += math.log(d / d0)
        u = s + (u - s) * (d0 / d)
        t += every
    return total / t


def growth(npairs=200, d0=1e-8, tmax=30.0, every=0.1):
    base = run(start(), 0.5 * npairs, dt=DT)
    a = base[::50][:npairs].copy()
    b = a + d0 * np.ones(3) / math.sqrt(3.0)
    m = int(round(every / DT))
    rows = [(0.0, math.log(d0))]
    t = 0.0
    for _ in range(int(round(tmax / every))):
        for _ in range(m):
            a = rk4(a)
            b = rk4(b)
        t += every
        d = np.linalg.norm(b - a, axis=1)
        rows.append((round(t, 6), float(np.mean(np.log(d)))))
    return rows


def fit(rows, t0=2.0, t1=16.0):
    pts = [(t, y) for t, y in rows if t0 - 1e-9 <= t <= t1 + 1e-9]
    n = len(pts)
    mt = sum(t for t, _ in pts) / n
    my = sum(y for _, y in pts) / n
    slope = sum((t - mt) * (y - my) for t, y in pts) / sum((t - mt) ** 2 for t, _ in pts)
    return slope, my - slope * mt


def numbers():
    lam = lyapunov()
    g = growth()
    slope, icpt = fit(g)
    c = fixed_points()[1]
    return {"lyapunov": lam, "doubling_time": math.log(2) / lam, "fit_slope": slope,
            "fit_doubling": math.log(2) / slope, "divergence": divergence(),
            "fixed_x": c[0], "fixed_z": c[2], "log10d_t0": g[0][1] / math.log(10),
            "log10d_t30": g[-1][1] / math.log(10), "fit_intercept": icpt}


if __name__ == "__main__":
    s0 = start()
    r1 = run(s0, 30.0)
    r2 = run(s0 + np.array([1e-5, 0.0, 0.0]), 30.0)
    write_table(__file__, ("t", "x1", "x2"),
                [(round(i * DT, 2), round(float(r1[i, 0]), 4), round(float(r2[i, 0]), 4))
                 for i in range(0, len(r1), 2)], part="traj")
    rb = run(s0, 40.0)
    write_table(__file__, ("x", "z"),
                [(round(float(p[0]), 3), round(float(p[2]), 3)) for p in rb[::2]],
                part="butterfly")
    g = growth()
    slope, icpt = fit(g)
    write_table(__file__, ("t", "log10d", "fit"),
                [(t, round(y / math.log(10), 4),
                  round((icpt + slope * t) / math.log(10), 4) if t <= 22.0 + 1e-9 else "nan")
                 for t, y in g], part="growth")
    write_table(__file__, ("key", "value"),
                [(k, round(v, 4)) for k, v in sorted(numbers().items())], part="numbers")
