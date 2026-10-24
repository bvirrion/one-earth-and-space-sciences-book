"""A flow net: steady seepage under a dam on a permeable foundation
(Year 3, hydrogeology). Invented geometry.

A layer of sand 20 m thick (homogeneous, isotropic, conductivity K) rests on
impermeable rock. A dam 20 m wide stands on it; the reservoir upstream holds
the head h1 = 10 m above the downstream water level (datum). The domain runs
60 m either side of the dam axis, its vertical sides being no-flow
boundaries. With the head h(x, z) obeying Laplace's equation:

    h = h1 on the upstream bed (z = 0, x < -10), h = 0 downstream (x > 10);
    dh/dn = 0 on the dam base (|x| < 10, z = 0), the floor (z = -20) and the sides.

The stream function psi obeys Laplace's equation with the conjugate
conditions: psi = 0 on the floor and the sides, psi = 1 on the dam base (one
streamline), dpsi/dn = 0 on the two beds. Both are solved by successive
over-relaxation on a 0.5 m grid (ghost nodes for the Neumann conditions).
The seepage per metre of dam is computed from the head gradient across the
downstream bed and compared with the flow-net estimate q = K h1 N_f / N_d.

  part h-<k>    x z         equipotential h = k h1/10, k = 1..9
  part psi-<k>  x z         streamline psi = k/5, k = 1..4
  part values   what value
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
from region import trace  # noqa: E402

H1 = 10.0
HALF_W, HALF_DAM, DEPTH = 60.0, 10.0, 20.0
DX = 0.5
XS = np.arange(-HALF_W, HALF_W + DX / 2, DX)
ZS = np.arange(-DEPTH, DX / 2, DX)          # rows from the floor (z = -20) to the bed (z = 0)
NX, NZ = len(XS), len(ZS)
UP = XS < -HALF_DAM - 1e-9
DOWN = XS > HALF_DAM + 1e-9
DAM = ~(UP | DOWN)


def _sor(fixed_mask, fixed_val, init, omega=1.9, tol=1e-9, itmax=40000):
    """Laplace by red-black SOR; mirror (Neumann) on every boundary node that
    is not fixed."""
    f = init.copy()
    f[fixed_mask] = fixed_val[fixed_mask]
    jj, ii = np.meshgrid(np.arange(NZ), np.arange(NX), indexing="ij")
    colour = (jj + ii) % 2
    for _ in range(itmax):
        delta = 0.0
        for c in (0, 1):
            p = np.pad(f, 1, mode="reflect")       # ghost nodes mirror the inner ones
            avg = 0.25 * (p[1:-1, :-2] + p[1:-1, 2:] + p[:-2, 1:-1] + p[2:, 1:-1])
            upd = (colour == c) & ~fixed_mask
            new = f[upd] + omega * (avg[upd] - f[upd])
            delta = max(delta, float(np.max(np.abs(new - f[upd]))) if new.size else 0.0)
            f[upd] = new
        if delta < tol:
            break
    return f


def solve_head():
    mask = np.zeros((NZ, NX), bool)
    val = np.zeros((NZ, NX))
    mask[-1, UP] = True
    val[-1, UP] = H1
    mask[-1, DOWN] = True
    val[-1, DOWN] = 0.0
    return _sor(mask, val, np.full((NZ, NX), H1 / 2))


def solve_psi():
    mask = np.zeros((NZ, NX), bool)
    val = np.zeros((NZ, NX))
    mask[0, :] = True              # floor
    mask[:, 0] = True              # sides
    mask[:, -1] = True
    mask[-1, DAM] = True           # dam base
    val[-1, DAM] = 1.0
    return _sor(mask, val, np.full((NZ, NX), 0.5))


def seepage(h, k=1.0):
    """Flow per metre of dam (K = k) up through the downstream bed and down
    through the upstream bed, from one-sided gradients."""
    dhdz = (h[-1, :] - h[-2, :]) / DX          # z upward: h decreases upward downstream
    qz = -k * dhdz                              # upward Darcy flux
    w = np.full(NX, DX)
    w[0] = w[-1] = DX / 2
    out = float(np.sum((qz * w)[DOWN]) + 0.5 * DX * qz[DOWN][0])
    inn = float(-np.sum((qz * w)[UP]) - 0.5 * DX * qz[UP][-1])
    return inn, out


def lines(field, level):
    rows = []
    for line in trace(field, XS, ZS, level):
        if len(line) < 3:
            continue
        rows += list(line) + [("nan", "nan")]
    return rows[:-1]


def main():
    h = solve_head()
    psi = solve_psi()
    for k in range(1, 10):
        write_table(__file__, ("x", "z"), lines(h, k * H1 / 10), part="h-%d" % k)
    for k in range(1, 5):
        write_table(__file__, ("x", "z"), lines(psi, k / 5), part="psi-%d" % k)
    qin, qout = seepage(h)
    vals = [["q_in_per_K", qin], ["q_out_per_K", qout],
            ["shape_factor", qout / H1], ["h_toe_down", float(h[-1, np.argmax(DOWN)])],
            ["h_heel_floor", float(h[0, NX // 2])]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
