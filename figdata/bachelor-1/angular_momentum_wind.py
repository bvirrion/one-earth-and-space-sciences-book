"""The zonal wind of a ring of air that leaves the equator at rest relative to the ground
and conserves its angular momentum about the Earth's axis (Year 1,
atmospheric-circulation).

Constants: sidereal rotation period 23.9345 h (earth:Trot), mean radius 6371 km
(earth:Rmean). A ring at latitude phi, of radius a cos(phi), has the angular momentum
per unit mass M = (Omega a cos(phi) + u) a cos(phi); with M = Omega a^2 at the equator,

    u(phi) = Omega a sin^2(phi) / cos(phi).

  part curve   lat u           (0 to 40 deg, every 0.5 deg)
  part values  what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

T_ROT = 23.9345 * 3600.0          # s, earth:Trot
A = 6371.0e3                      # m, earth:Rmean
OMEGA = 2 * math.pi / T_ROT


def u_ring(lat_deg, u0=0.0, lat0=0.0):
    """Zonal wind (m/s) of a ring that starts at latitude lat0 with zonal wind u0 and
    keeps its angular momentum."""
    p, p0 = math.radians(lat_deg), math.radians(lat0)
    m = (OMEGA * A * math.cos(p0) + u0) * A * math.cos(p0)
    return m / (A * math.cos(p)) - OMEGA * A * math.cos(p)


def u_closed(lat_deg):
    p = math.radians(lat_deg)
    return OMEGA * A * math.sin(p) ** 2 / math.cos(p)


def values():
    return [("Omega", OMEGA), ("Omega_a", OMEGA * A), ("u_10", u_closed(10.0)),
            ("u_20", u_closed(20.0)), ("u_30", u_closed(30.0)), ("u_40", u_closed(40.0)),
            ("ground_speed_0", OMEGA * A), ("ground_speed_30", OMEGA * A * math.cos(math.radians(30)))]


if __name__ == "__main__":
    write_table(__file__, ("lat", "u"), [(0.5 * k, u_closed(0.5 * k)) for k in range(0, 81)], part="curve")
    write_table(__file__, ("what", "value"), values(), part="values", digits=7)
