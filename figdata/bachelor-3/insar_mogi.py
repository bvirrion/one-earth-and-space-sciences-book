"""Radar interferometry over an inflating Mogi source (Year 3, remote sensing).

Surface displacement of a point source of volume change dV at depth z0 in an elastic
half-space of Poisson's ratio nu (ledger dmodels:mogi and b5 dmodels:mogi-radial, USGS
TM 13-B1 eqs. 16-17 in the point-source limit, dV = pi a^3 dP / mu):

    u_z = (1 - nu) dV/pi * z0 / (r^2 + z0^2)^(3/2),
    u_r = (1 - nu) dV/pi * r  / (r^2 + z0^2)^(3/2).

The radar looks down at the incidence angle theta from a satellite to the EAST of
the scene (a unit vector from the ground to the satellite: (sin theta, 0, cos theta)
in east, north, up). The line-of-sight change counted positive TOWARDS the satellite
(range shortening) is

    d_los = u_E sin theta + u_z cos theta,

and the interferometric phase is 4 pi d_los / lambda, wrapped to [0, 2 pi): one
fringe for each lambda/2 of motion along the line of sight. lambda = c / 5.405 GHz,
the Sentinel-1 C-band centre frequency (ledger esa:s1-sar).

Illustration: z0 = 4 km, dV = 1e7 m3, nu = 0.25, theta = 35 degrees (inside the
29.1-46.0 degree range of the wide-swath mode, ledger esa:s1-iw).

  part map      x y phase         km, km, radians (0 - 2 pi), 30 x 30 km, 0.3 km step
  part profile  x uz ue los ns    E-W profile through the centre (mm); ns = the
                                  LOS change along the N-S line at the same distance
  part values   what value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

C = 299792458.0
F_S1 = 5.405e9
LAM = C / F_S1                    # m
NU = 0.25
Z0 = 4000.0                       # m
DV = 1.0e7                        # m3
THETA = math.radians(35.0)


def mogi(r, z0=Z0, dv=DV, nu=NU):
    """(u_r, u_z) in metres at horizontal distance r (m) from the point above the source."""
    k = (1 - nu) * dv / math.pi / (r * r + z0 * z0) ** 1.5
    return k * r, k * z0


def los(x, y, z0=Z0, dv=DV, nu=NU, theta=THETA):
    """Line-of-sight change towards a satellite in the east, at (x, y) metres."""
    r = math.hypot(x, y)
    ur, uz = mogi(r, z0, dv, nu)
    ue = ur * x / r if r > 0 else 0.0
    return ue * math.sin(theta) + uz * math.cos(theta)


def phase(d, lam=LAM):
    """Wrapped interferometric phase (rad) of a line-of-sight change d (m)."""
    return (4 * math.pi * d / lam) % (2 * math.pi)


def half_radius(z0):
    """Distance at which u_z falls to half its central value."""
    return z0 * math.sqrt(2 ** (2.0 / 3.0) - 1)


def volume_from_peak(uz0, z0, nu=NU):
    return math.pi * uz0 * z0 * z0 / (1 - nu)


def main():
    g = np.round(np.arange(-15.0, 15.0001, 0.3), 1)
    rows = []
    for y in g:
        for x in g:
            rows.append((x, y, phase(los(1e3 * x, 1e3 * y))))
    write_table(__file__, ("x", "y", "phase"), rows, part="map")
    prof = []
    for x in np.round(np.arange(-15.0, 15.0001, 0.1), 1):
        ur, uz = mogi(abs(1e3 * x))
        ue = math.copysign(ur, x) if x != 0 else 0.0
        prof.append((x, 1e3 * uz, 1e3 * ue, 1e3 * los(1e3 * x, 0.0), 1e3 * los(0.0, 1e3 * x)))
    write_table(__file__, ("x", "uz", "ue", "los", "ns"), prof, part="profile")
    uz0 = mogi(0.0)[1]
    d0 = los(0.0, 0.0)
    xs = np.arange(-15000.0, 15000.1, 10.0)
    dl = np.array([los(x, 0.0) for x in xs])
    vals = [["lambda_m", LAM], ["half_lambda_mm", 500 * LAM], ["uz0_mm", 1e3 * uz0],
            ["los0_mm", 1e3 * d0], ["fringes_centre", d0 / (LAM / 2)],
            ["los_max_mm", 1e3 * dl.max()], ["x_los_max_km", xs[dl.argmax()] / 1e3],
            ["ur_max_mm", 1e3 * mogi(Z0 / math.sqrt(2))[0]],
            ["half_radius_km", half_radius(Z0) / 1e3],
            ["dv_check", volume_from_peak(uz0, Z0)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
