"""Temperature and pressure against altitude in the U.S. Standard Atmosphere,
1976 (grade 8, the atmosphere).

Defining values (NOAA-S/T 76-1562, ledger ussa76:*): sea-level temperature
288.15 K and pressure 101 325 Pa; g0 = 9.80665 m/s2; R* = 8314.32 J/(kmol K);
M0 = 28.9644 kg/kmol; r0 = 6356.766 km (geopotential conversion); Table 4:
the seven layers below 86 km, bases at geopotential heights 0, 11, 20, 32,
47, 51, 71 and 84.852 km' with gradients -6.5, 0, +1.0, +2.8, 0, -2.8, -2.0
K/km'; Table 5 and eq. (27): 86--91 km isothermal at 186.8673 K, 91--110 km
an ellipse T = Tc + A sqrt(1 - ((Z - 91)/a)^2), Tc = 263.1905 K,
A = -76.3232 K, a = -19.9429 km.
Below 86 km the molecular-scale temperature is used as the temperature (they
differ by less than 0.1 K there).

  part temp      : z_km T_C           (0--100 km)
  part pressure  : z_km p_hPa         (0--30 km)
  part layers    : name base_km top_km mid_km lx_C   (the four layers, 0--100 km;
                   lx_C: where the figure puts the name, clear of the curve)
  part band-<name>: T_C z_km           (a closed band behind the profile,
                                        T from -100 to +30 degC)
  part levels    : z_km p_hPa label    (the half and quarter levels)
  part guides    : p_hPa z_km          (dashed guides to the two levels)
  part sonde     : z_km p_hPa T_C share   (every 2 km to 30 km, for the problem)
  main table     : item value          (quoted numbers)
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

T0 = 288.15                 # K
P0 = 101325.0               # Pa
G0 = 9.80665                # m/s2
RSTAR = 8314.32             # J/(kmol K)
M0 = 28.9644                # kg/kmol
R0 = 6356.766               # km
H_BASE = (0.0, 11.0, 20.0, 32.0, 47.0, 51.0, 71.0, 84.852)     # km'
L_BASE = (-6.5, 0.0, 1.0, 2.8, 0.0, -2.8, -2.0)                 # K/km'
T7 = 186.8673
TC, A_ELL, A_AX, Z8 = 263.1905, -76.3232, -19.9429, 91.0
GMR = G0 * M0 / RSTAR * 1000.0      # K per km': g0 M0 / R*


def geopotential(z_km):
    return R0 * z_km / (R0 + z_km)


def geometric(h_km):
    return R0 * h_km / (R0 - h_km)


def _bases():
    """Temperature and pressure at each layer base (below 86 km)."""
    ts, ps = [T0], [P0]
    for i, lb in enumerate(L_BASE):
        dh = H_BASE[i + 1] - H_BASE[i]
        t1 = ts[-1] + lb * dh
        if lb == 0:
            p1 = ps[-1] * math.exp(-GMR * dh / ts[-1])
        else:
            p1 = ps[-1] * (ts[-1] / t1) ** (GMR / lb)
        ts.append(t1)
        ps.append(p1)
    return ts, ps


TB, PB = _bases()


def _layer(h):
    i = 0
    while i + 1 < len(L_BASE) and h >= H_BASE[i + 1]:
        i += 1
    return i


def temperature(z_km):
    """Temperature (K) at geometric altitude z (km), 0--110 km."""
    if z_km < 86.0:
        h = geopotential(z_km)
        i = _layer(h)
        return TB[i] + L_BASE[i] * (h - H_BASE[i])
    if z_km <= Z8:
        return T7
    return TC + A_ELL * math.sqrt(1.0 - ((z_km - Z8) / A_AX) ** 2)


def pressure(z_km):
    """Pressure (Pa) at geometric altitude z (km), 0--86 km."""
    h = geopotential(z_km)
    i = _layer(h)
    tb, pb, lb = TB[i], PB[i], L_BASE[i]
    if lb == 0:
        return pb * math.exp(-GMR * (h - H_BASE[i]) / tb)
    return pb * (tb / (tb + lb * (h - H_BASE[i]))) ** (GMR / lb)


def level(fraction):
    """Altitude (km) where the pressure is the given fraction of P0."""
    lo, hi = 0.0, 86.0
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if pressure(mid) > fraction * P0:
            lo = mid
        else:
            hi = mid
    return lo


def share_below(z_km):
    """Share (per cent) of the atmosphere's mass below z: 1 - p(z)/p0
    (hydrostatic, g taken as constant)."""
    return 100.0 * (1.0 - pressure(z_km) / P0)


def layers():
    """The four layers with their limits (km): the tropopause where the
    cooling stops (11 km'), the stratopause in the middle of the 47--51 km'
    isothermal layer, the mesopause at 86 km (the coldest air)."""
    tropo = geometric(H_BASE[1])
    strato = (geometric(H_BASE[4]) + geometric(H_BASE[5])) / 2.0
    return [("troposphere", 0.0, tropo), ("stratosphere", tropo, strato),
            ("mesosphere", strato, 86.0), ("thermosphere", 86.0, 100.0)]


def c(t_k):
    return t_k - 273.15


if __name__ == "__main__":
    write_table(__file__, ("z_km", "T_C"),
                [(z / 2.0, round(c(temperature(z / 2.0)), 3)) for z in range(0, 201)], part="temp")
    write_table(__file__, ("z_km", "p_hPa"),
                [(z / 4.0, round(pressure(z / 4.0) / 100.0, 3)) for z in range(0, 121)], part="pressure")
    write_table(__file__, ("name", "base_km", "top_km", "mid_km", "lx_C"),
                [(n, round(b, 2), round(t, 2), round((b + t) / 2.0, 2),
                  -97 if c(temperature((b + t) / 2.0)) > -70 else -60) for n, b, t in layers()], part="layers")
    for n, b, t in layers():
        write_table(__file__, ("T_C", "z_km"), [(-100, b), (30, b), (30, t), (-100, t), (-100, b)],
                    part="band-" + n)
    lv = [(level(0.5), "half"), (level(0.25), "quarter")]
    write_table(__file__, ("z_km", "p_hPa", "label"),
                [(round(z, 2), round(pressure(z) / 100.0, 1), lab) for z, lab in lv], part="levels")
    rows = []
    for z, _ in lv:
        pz = round(pressure(z) / 100.0, 1)
        rows += [(), (0, round(z, 2)), (pz, round(z, 2)), (pz, 0)]
    write_table(__file__, ("p_hPa", "z_km"), rows[1:], part="guides")
    write_table(__file__, ("z_km", "p_hPa", "T_C", "share"),
                [(z, round(pressure(z) / 100.0), round(c(temperature(z))), round(share_below(z)))
                 for z in range(0, 31, 2)], part="sonde")
    lay = layers()
    write_table(__file__, ("item", "value"), [
        ("tropopause_km", round(lay[0][2], 2)),
        ("stratopause_km", round(lay[1][2], 2)),
        ("T_sea_C", round(c(temperature(0.0)), 2)),
        ("T_tropopause_C", round(c(temperature(lay[0][2])), 2)),
        ("T_stratopause_C", round(c(temperature(lay[1][2])), 2)),
        ("T_mesopause_C", round(c(temperature(86.0)), 2)),
        ("T_100km_C", round(c(temperature(100.0)), 2)),
        ("half_km", round(level(0.5), 2)),
        ("quarter_km", round(level(0.25), 2)),
        ("eighth_km", round(level(0.125), 2)),
        ("share_below_11km", round(share_below(lay[0][2]), 1)),
        ("share_below_30km", round(share_below(30.0), 2)),
        ("p_30km_hPa", round(pressure(30.0) / 100.0, 2)),
        ("p_50km_hPa", round(pressure(50.0) / 100.0, 3)),
        ("p_80km_hPa", round(pressure(80.0) / 100.0, 4)),
    ])
