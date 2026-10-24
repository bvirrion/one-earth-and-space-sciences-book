"""Inertial oscillations on an f-plane (Year 3, geophysical fluid dynamics).

A parcel moving horizontally with no force but the Coriolis force obeys
du/dt = f v, dv/dt = -f u: it turns clockwise (northern hemisphere) on a
circle of radius U/f, once every 2 pi / f. With a linear friction -r u the
circles shrink into a spiral; carried by a steady current (u0, 0) the path
becomes a train of loops, like the tracks of drifting buoys after a storm
(ledger stewart:inertial).

The numerical solution (RK4) is checked against the closed form by the tests.
Latitude LAT and speeds are invented; Omega is the GRS80 value
(geod5:grs80-defining).

  part circle   t x y          free oscillation, x y in km, t in h
  part spiral   t x y          with friction R_FRIC
  part loops    t x y          with friction, carried by the current U0
  part fbeta    lat f fb       f(lat) and its beta-plane tangent at LAT, in 1e-4 1/s
  part values   what value

The beta-plane tangent uses the mean radius A_EARTH (earth:Rmean).
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

OMEGA = 7.292115e-5        # rad/s
LAT = 45.0
U_START = 0.20             # m/s, initial velocity, eastward
R_FRIC = 1.0 / (4 * 86400.0)   # 1/s, e-folding time of four days
U0 = 0.05                  # m/s, the steady current of the 'loops' case
T_END = 4 * 86400.0
DT = 60.0
A_EARTH = 6371.0e3         # m


def coriolis(lat=LAT):
    return 2 * OMEGA * math.sin(math.radians(lat))


def rhs(state, f, r, u0):
    x, y, u, v = state
    # velocity relative to the current decays and turns; the parcel moves with u + u0
    return np.array([u + u0, v, f * v - r * u, -f * u - r * v])


def beta(lat=LAT):
    return 2 * OMEGA * math.cos(math.radians(lat)) / A_EARTH


def f_beta_plane(lat, lat0=LAT):
    """f0 + beta y, y the northward distance from lat0 on the sphere."""
    return coriolis(lat0) + beta(lat0) * A_EARTH * math.radians(lat - lat0)


def integrate(f=None, r=0.0, u0=0.0, u_start=U_START, t_end=T_END, dt=DT):
    f = coriolis() if f is None else f
    s = np.array([0.0, 0.0, u_start, 0.0])
    out = [(0.0, *s)]
    n = int(round(t_end / dt))
    for i in range(n):
        k1 = rhs(s, f, r, u0)
        k2 = rhs(s + dt / 2 * k1, f, r, u0)
        k3 = rhs(s + dt / 2 * k2, f, r, u0)
        k4 = rhs(s + dt * k3, f, r, u0)
        s = s + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        out.append(((i + 1) * dt, *s))
    return np.array(out)


def exact(t, f=None, u_start=U_START):
    """Closed form of the free oscillation: u = U cos ft, v = -U sin ft;
    x = (U/f) sin ft, y = (U/f)(cos ft - 1)."""
    f = coriolis() if f is None else f
    t = np.asarray(t, dtype=float)
    return (u_start / f) * np.sin(f * t), (u_start / f) * (np.cos(f * t) - 1.0)


def radius(u=U_START, f=None):
    return u / (coriolis() if f is None else f)


def period_hours(f=None):
    return 2 * math.pi / (coriolis() if f is None else f) / 3600.0


def main():
    for part, r, u0 in (("circle", 0.0, 0.0), ("spiral", R_FRIC, 0.0), ("loops", R_FRIC, U0)):
        a = integrate(r=r, u0=u0)[::10]
        write_table(__file__, ("t", "x", "y"), [[t / 3600, x / 1000, y / 1000] for t, x, y, _, _ in a],
                    part=part)
    write_table(__file__, ("lat", "f", "fb"),
                [[lat, coriolis(lat) * 1e4, f_beta_plane(lat) * 1e4] for lat in range(0, 91, 2)],
                part="fbeta")
    write_table(__file__, ("what", "value"),
                [["f", coriolis()], ["beta", beta()], ["radius_km", radius() / 1000], ["period_h", period_hours()],
                 ["period_h_30", period_hours(coriolis(30.0))], ["period_h_60", period_hours(coriolis(60.0))]],
                part="values")


if __name__ == "__main__":
    main()
