"""The Ekman spiral and the Ekman transport (Year 1, ocean-circulation).

Ekman's solution for a steady wind blowing towards the north over a deep, homogeneous
ocean with a constant vertical eddy viscosity A_z, in the Northern Hemisphere (ledger
stewart:ekman-solution), with z the height (z <= 0 in the water):

    u = V0 exp(a z) cos(pi/4 + a z),   v = V0 exp(a z) sin(pi/4 + a z),
    a = sqrt(f / (2 A_z)) = pi / D_E,   V0 = T / (rho sqrt(f A_z)),

and Ekman's constants (stewart:ekman-constants): rho = 1027 kg/m3, rho_air = 1.25 kg/m3,
C_D = 2.6e-3, D_E = 7.6 U10 / sqrt(sin|phi|); A_z follows from D_E. Omega from the
sidereal day (earth:Trot).

The modern bulk formula of the chapter (stewart:wind-stress, stewart:drag-coefficient):
T = 1.3 C_D U10^2 with the drag coefficient of Yelland and Taylor.

  part arrows    z u v        (velocity at the depths 0, D_E/10, ..., D_E: hodograph arrows)
  part tips      u v          (the tips of the velocity vectors from 0 to 1.25 D_E)
  part profile   z u v speed  (components against depth, 0 to 2 D_E)
  part values    what value
for U10 = 10 m/s at 35 N.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

T_ROT = 23.9345 * 3600.0
OMEGA = 2 * math.pi / T_ROT
RHO_W = 1027.0                  # Ekman's seawater density
RHO_AIR_EKMAN = 1.25
CD_EKMAN = 2.6e-3
RHO_AIR = 1.3                   # bulk formula of the chapter
U10, LAT = 10.0, 35.0


def coriolis(lat):
    return 2 * OMEGA * math.sin(math.radians(lat))


def drag_coefficient(u10):
    """Yelland and Taylor (1996): C_D for 3 <= U10 <= 26 m/s."""
    if not 3.0 <= u10 <= 26.0:
        raise ValueError("outside 3-26 m/s")
    if u10 <= 6.0:
        return (0.29 + 3.1 / u10 + 7.7 / u10 ** 2) * 1e-3
    return (0.60 + 0.071 * u10) * 1e-3


def stress(u10):
    """Wind stress (Pa) from the bulk formula with the Yelland-Taylor drag coefficient."""
    return RHO_AIR * drag_coefficient(u10) * u10 ** 2


def ekman_depth(u10, lat):
    return 7.6 * u10 / math.sqrt(math.sin(math.radians(abs(lat))))


def surface_current_empirical(u10, lat):
    return 0.0127 * u10 / math.sqrt(math.sin(math.radians(abs(lat))))


def spiral_constants(u10, lat):
    """(T, f, D_E, a, A_z, V0) with Ekman's constants."""
    t = RHO_AIR_EKMAN * CD_EKMAN * u10 ** 2
    f = coriolis(lat)
    d = ekman_depth(u10, lat)
    a = math.pi / d
    az = f / (2 * a * a)
    v0 = t / (RHO_W * math.sqrt(f * az))
    return t, f, d, a, az, v0


def velocity(z, u10=U10, lat=LAT):
    """(u, v) in m/s at height z (m, negative below the surface), wind towards the north."""
    _, _, _, a, _, v0 = spiral_constants(u10, lat)
    e = v0 * math.exp(a * z)
    return e * math.cos(math.pi / 4 + a * z), e * math.sin(math.pi / 4 + a * z)


def transport(u10=U10, lat=LAT, n=20000):
    """Mass transport (M_x, M_y) in kg/(m s), integrated by the trapezium rule to 10 D_E."""
    d = spiral_constants(u10, lat)[2]
    zs = [-10 * d * k / n for k in range(n + 1)]
    mx = my = 0.0
    for z1, z2 in zip(zs, zs[1:]):
        (u1, v1), (u2, v2) = velocity(z1, u10, lat), velocity(z2, u10, lat)
        mx += 0.5 * (u1 + u2) * (z1 - z2)
        my += 0.5 * (v1 + v2) * (z1 - z2)
    return RHO_W * mx, RHO_W * my


def angle_right_of_wind(u, v):
    """Angle (deg) of the vector (u, v) to the right of a wind blowing towards the north."""
    return math.degrees(math.atan2(u, v))


def values():
    t, f, d, a, az, v0 = spiral_constants(U10, LAT)
    mx, my = transport()
    u0, w0 = velocity(0.0)
    ud, wd = velocity(-d)
    return [("T_ekman", t), ("f", f), ("D_E", d), ("A_z", az), ("V0", v0),
            ("V0_empirical", surface_current_empirical(U10, LAT)),
            ("surface_angle", angle_right_of_wind(u0, w0)),
            ("speed_ratio_at_DE", math.hypot(ud, wd) / v0),
            ("angle_at_DE", angle_right_of_wind(ud, wd)),
            ("Mx", mx), ("My", my), ("T_over_f", t / f),
            ("transport_angle", angle_right_of_wind(mx, my)),
            ("T_bulk_10", stress(10.0)), ("CD_10", drag_coefficient(10.0))]


if __name__ == "__main__":
    d = spiral_constants(U10, LAT)[2]
    write_table(__file__, ("z", "u", "v"),
                [(-d * k / 10, *velocity(-d * k / 10)) for k in range(11)], part="arrows")
    write_table(__file__, ("u", "v"), [velocity(-1.25 * d * k / 200) for k in range(201)], part="tips")
    rows = []
    for k in range(201):
        z = -2 * d * k / 200
        u, v = velocity(z)
        rows.append((z, u, v, math.hypot(u, v)))
    write_table(__file__, ("z", "u", "v", "speed"), rows, part="profile")
    write_table(__file__, ("what", "value"), values(), part="values", digits=7)
