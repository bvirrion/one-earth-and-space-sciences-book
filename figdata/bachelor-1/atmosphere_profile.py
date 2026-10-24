"""Temperature, pressure and potential temperature in the U.S. Standard Atmosphere,
1976, and the dry adiabat (Year 1, fluid-envelopes-structure).

Defining values (NOAA-S/T 76-1562; ledger ussa76:sea-level, ussa76:layers):
sea-level temperature 288.15 K and pressure 101 325 Pa; g0 = 9.80665 m/s2;
R* = 8314.32 J/(kmol K); M0 = 28.9644 kg/kmol; r0 = 6356.766 km; Table 4: layer
bases at geopotential heights 0, 11, 20, 32, 47, 51, 71 km' with gradients -6.5,
0, +1.0, +2.8, 0, -2.8, -2.0 K/km'. The specific heat of dry air at constant
pressure is c_p = gamma/(gamma - 1) R*/M0 with gamma = 1.4 for air (nasa:grc-gamma),
i.e. 7/2 of the specific gas constant (an ideal diatomic gas). The potential
temperature takes the reference pressure 1000 hPa (nws:potential-temperature).

Heights are geometric (km); the layers are defined in geopotential km' and
converted with h = r0 z / (r0 + z), as the standard does.

  part profile   z_km T_K theta_K p_hPa       0-32 km every 0.25 km
  part adiabat   z_km T_K                     dry adiabat from the surface, 0-12 km
  part tropo     z_km T_K theta_K             the tropopause point
  part values    what value
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
GAMMA = 1.4
P_REF = 100000.0            # Pa, reference pressure of the potential temperature

R_D = RSTAR / M0                        # J/(kg K), specific gas constant of dry air
CP = GAMMA / (GAMMA - 1.0) * R_D        # J/(kg K)
KAPPA = R_D / CP                        # = 2/7
GAMMA_D = G0 / CP * 1000.0              # K/km, dry adiabatic lapse rate
GMR = G0 * M0 / RSTAR * 1000.0          # K per km'


def geopotential(z_km):
    return R0 * z_km / (R0 + z_km)


def geometric(h_km):
    return R0 * h_km / (R0 - h_km)


def _bases():
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


def temperature_h(h):
    """Temperature (K) at geopotential height h (km'), 0-84.852 km'."""
    i = _layer(h)
    return TB[i] + L_BASE[i] * (h - H_BASE[i])


def pressure_h(h):
    """Pressure (Pa) at geopotential height h (km'): closed forms of the standard
    (exponential in an isothermal layer, power law in a layer of constant gradient)."""
    i = _layer(h)
    t = temperature_h(h)
    if L_BASE[i] == 0:
        return PB[i] * math.exp(-GMR * (h - H_BASE[i]) / TB[i])
    return PB[i] * (TB[i] / t) ** (GMR / L_BASE[i])


def temperature(z_km):
    return temperature_h(geopotential(z_km))


def pressure(z_km):
    return pressure_h(geopotential(z_km))


def theta(t_k, p_pa, p_ref=P_REF):
    """Potential temperature (K): T (p_ref / p)^(R/c_p)."""
    return t_k * (p_ref / p_pa) ** KAPPA


def theta_at(z_km):
    return theta(temperature(z_km), pressure(z_km))


def scale_height(t_k):
    """Scale height R T / (M g) in km."""
    return RSTAR * t_k / (M0 * G0) / 1000.0


def hydrostatic_pressure(h_top, n=20000):
    """Pressure (Pa) at geopotential height h_top (km') by integrating dp/dh = -p g M/(R T)
    numerically (RK4) from sea level: a check of the closed forms."""
    p, h, dh = P0, 0.0, h_top / n
    f = lambda hh, pp: -pp * GMR / temperature_h(hh)
    for _ in range(n):
        k1 = f(h, p)
        k2 = f(h + dh / 2, p + dh / 2 * k1)
        k3 = f(h + dh / 2, p + dh / 2 * k2)
        k4 = f(h + dh, p + dh * k3)
        p += dh / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        h += dh
    return p


def buoyancy_frequency(t_k, gamma_env):
    """N (1/s) for a layer of temperature t_k and environmental lapse rate gamma_env (K/km):
    N^2 = (g/T)(Gamma_d - Gamma)."""
    n2 = G0 / t_k * (GAMMA_D - gamma_env) / 1000.0
    return math.sqrt(n2) if n2 > 0 else float("nan")


def values():
    z_tp = geometric(11.0)
    return [
        ("R_d", R_D), ("c_p", CP), ("kappa", KAPPA), ("Gamma_d_K_per_km", GAMMA_D),
        ("T_11kmgp", temperature_h(11.0)), ("p_11kmgp", pressure_h(11.0)),
        ("p_20kmgp", pressure_h(20.0)), ("p_32kmgp", pressure_h(32.0)),
        ("z_tropopause_km", z_tp), ("theta_surface", theta(T0, P0)),
        ("theta_tropopause", theta(temperature_h(11.0), pressure_h(11.0))),
        ("theta_20kmgp", theta(temperature_h(20.0), pressure_h(20.0))),
        ("theta_32kmgp", theta(temperature_h(32.0), pressure_h(32.0))),
        ("H_surface_km", scale_height(T0)), ("H_tropopause_km", scale_height(TB[1])),
        ("N_troposphere", buoyancy_frequency(T0, 6.5)),
        ("N_stratosphere", buoyancy_frequency(TB[1], 0.0)),
        ("T_dry_adiabat_at_11kmgp", T0 - GAMMA_D * z_tp),
    ]


if __name__ == "__main__":
    rows = []
    for i in range(0, 129):
        z = 0.25 * i
        rows.append((z, temperature(z), theta_at(z), pressure(z) / 100.0))
    write_table(__file__, ("z_km", "T_K", "theta_K", "p_hPa"), rows, part="profile")
    write_table(__file__, ("z_km", "T_K"),
                [(z, T0 - GAMMA_D * z) for z in (0.0, 12.0)], part="adiabat")
    z_tp = geometric(11.0)
    write_table(__file__, ("z_km", "T_K", "theta_K"),
                [(z_tp, temperature(z_tp), theta_at(z_tp))], part="tropo")
    write_table(__file__, ("what", "value"), values(), part="values", digits=8)
