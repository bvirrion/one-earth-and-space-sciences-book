"""Stommel's wind-driven gyre in a rectangular basin (Year 1, ocean-circulation).

Stommel (1948; ledger stommel:1948, stewart:stommel): a homogeneous ocean of constant depth
in a rectangular basin 0 <= x <= L (east), 0 <= y <= 1 (north), driven by a zonal wind
stress tau_x = -cos(pi y) (easterlies in the south, westerlies in the north) and slowed by a
bottom friction proportional to the velocity. In non-dimensional form, with the transport
streamfunction psi (northward transport v = d psi / dx, eastward u = -d psi / dy),

    eps * laplacian(psi) + delta * d psi / dx = -pi sin(pi y),   psi = 0 on the walls,

where eps is the friction and delta the northward increase of the Coriolis parameter
(beta), both scaled. delta = 0: no rotation, or a uniform one; delta = 1: a Coriolis
parameter that grows northward. The values of eps, delta and L are exercise values, not
those of a real ocean. Solved by finite differences (central, second order) on a 301 x 101
grid with a sparse direct solver.

  part seg-<case>    x y        (contours of psi / max psi at 0.1, 0.3, 0.5, 0.7, 0.9;
                                 segments separated by nan rows; case uniform or beta)
  part vsec-<case>   x v        (northward velocity along y = 0.5, scaled by its maximum)
  part values        what value
"""
import math
import os
import sys

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

L = 1.5
EPS = 0.03
NX, NY = 301, 101
CASES = {"uniform": 0.0, "beta": 1.0}
LEVELS = (0.1, 0.3, 0.5, 0.7, 0.9)


def grid():
    return np.linspace(0.0, L, NX), np.linspace(0.0, 1.0, NY)


def solve(delta, eps=EPS):
    """psi[j, i] on the grid (j along y, i along x)."""
    x, y = grid()
    dx, dy = x[1] - x[0], y[1] - y[0]
    nx, ny = NX - 2, NY - 2                       # interior points
    n = nx * ny

    def idx(i, j):
        return j * nx + i

    rows, cols, vals = [], [], []
    rhs = np.empty(n)
    for j in range(ny):
        for i in range(nx):
            k = idx(i, j)
            rows.append(k); cols.append(k); vals.append(-2 * eps / dx ** 2 - 2 * eps / dy ** 2)
            for di, coef in ((-1, eps / dx ** 2 - delta / (2 * dx)), (1, eps / dx ** 2 + delta / (2 * dx))):
                if 0 <= i + di < nx:
                    rows.append(k); cols.append(idx(i + di, j)); vals.append(coef)
            for dj in (-1, 1):
                if 0 <= j + dj < ny:
                    rows.append(k); cols.append(idx(i, j + dj)); vals.append(eps / dy ** 2)
            rhs[k] = -math.pi * math.sin(math.pi * y[j + 1])
    a = sp.csr_matrix((vals, (rows, cols)), shape=(n, n))
    inner = spla.spsolve(a, rhs).reshape(ny, nx)
    psi = np.zeros((NY, NX))
    psi[1:-1, 1:-1] = inner
    return psi


def northward_velocity(psi):
    """v = d psi / dx on the grid (one-sided at the walls)."""
    x, _ = grid()
    return np.gradient(psi, x, axis=1)


def sverdrup_interior(x, y, delta):
    """The interior balance delta d psi/dx = -pi sin(pi y), with psi = 0 on the eastern wall."""
    return math.pi * (L - x) * math.sin(math.pi * y) / delta


def interior(x, y, delta, eps=EPS):
    """The interior with the friction kept but d2 psi/dx2 dropped:
    delta d psi/dx - eps pi^2 psi = -pi sin(pi y), psi(L) = 0. Tends to the Sverdrup
    interior as eps -> 0."""
    k = eps * math.pi ** 2
    return math.sin(math.pi * y) / (eps * math.pi) * (1 - math.exp(-k * (L - x) / delta))


def contour_segments(psi, level):
    x, y = grid()
    segs = []
    for j in range(NY - 1):
        for i in range(NX - 1):
            c = [(x[i], y[j], psi[j, i]), (x[i + 1], y[j], psi[j, i + 1]),
                 (x[i + 1], y[j + 1], psi[j + 1, i + 1]), (x[i], y[j + 1], psi[j + 1, i])]
            pts = []
            for k in range(4):
                (xa, ya, va), (xb, yb, vb) = c[k], c[(k + 1) % 4]
                va -= level
                vb -= level
                if (va < 0) != (vb < 0):
                    t = va / (va - vb)
                    pts.append((xa + t * (xb - xa), ya + t * (yb - ya)))
            if len(pts) == 2:
                segs.append(pts)
            elif len(pts) == 4:
                segs += [[pts[0], pts[1]], [pts[2], pts[3]]]
    return segs


def values():
    x, y = grid()
    out = []
    jm = NY // 2
    for name, delta in CASES.items():
        psi = solve(delta)
        j, i = np.unravel_index(np.argmax(psi), psi.shape)
        v = northward_velocity(psi)[jm]
        out += [("psimax_%s" % name, psi[j, i]), ("xmax_%s" % name, x[i]), ("ymax_%s" % name, y[j]),
                ("vnorth_%s" % name, v.max()), ("vsouth_%s" % name, -v.min()),
                ("xvnorth_%s" % name, x[int(np.argmax(v))])]
        if delta > 0:
            out.append(("sverdrup_mid_%s" % name, sverdrup_interior(L / 2, 0.5, delta)))
            out.append(("interior_mid_%s" % name, interior(L / 2, 0.5, delta)))
            out.append(("psi_mid_%s" % name, psi[jm, NX // 2]))
    return out


if __name__ == "__main__":
    x, _ = grid()
    for name, delta in CASES.items():
        psi = solve(delta)
        m = psi.max()
        rows = []
        for lev in LEVELS:
            for a, b in contour_segments(psi / m, lev):
                rows += [a, b, (float("nan"), float("nan"))]
        write_table(__file__, ("x", "y"), rows, part="seg-" + name, digits=5)
        v = northward_velocity(psi)[NY // 2]
        write_table(__file__, ("x", "v"), list(zip(x, v / np.abs(v).max())), part="vsec-" + name, digits=5)
    write_table(__file__, ("what", "value"), values(), part="values", digits=7)
