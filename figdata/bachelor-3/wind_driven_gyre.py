"""The wind-driven gyre: Ekman pumping, Sverdrup transport and the western
boundary layer (Year 3, ocean dynamics).

An invented ocean basin between 20 and 50 N, WIDTH = 6000 km wide, under the
zonal wind stress tau_x = -TAU0 cos(pi (lat - 20)/30): easterly trades at
20 N, westerlies at 50 N, no stress at 35 N. TAU0 = 0.1 Pa and the sea-water
density RHO = 1025 kg/m3 are exercise values. Omega is the GRS80 value
(geod5:grs80-defining), a the mean radius (earth:Rmean).

On the sphere (meridional profiles, part merid), for a purely zonal stress

    curl_z tau = -(1/(a cos lat)) d(tau cos lat)/d lat,
    w_E        = curl_z(tau / (rho f))                       (Ekman pumping),
    V          = curl_z tau / (rho beta),  beta = 2 Omega cos lat / a
                                                              (Sverdrup transport
                                                               per unit width).

The total interior transport is V * WIDTH.

On a beta-plane at 35 N (the basin of the weekend problem, part bl), with
L = a * 30 deg the basin length, the interior Sverdrup transport per unit
width at mid-basin is -A with A = TAU0 pi / (rho beta L), and near the western
wall the northward transport per unit width is, to leading order in the
boundary-layer width over the basin width X = WIDTH,

    Stommel (bottom friction r):  V = A [ (X/dS) exp(-x/dS) - 1 ],  dS = r/beta,
    Munk (lateral friction A_H):  V = A [ (X/dM)(2/sqrt 3) exp(-x/(2 dM))
                                         sin(sqrt 3 x/(2 dM)) - 1 ],
                                  dM = (A_H/beta)^(1/3),

which close the streamfunction psi = A [(X - x) - X (boundary term)] on the
wall x = 0. R_FRIC = 1e-6 /s is an exercise value; A_H = 5e3 m2/s is Munk's
value (ledger stewart:munk).

  part merid   lat tau wE V Vtot    stress (Pa), Ekman pumping (m/yr, upward
                                    positive), Sverdrup transport per unit width
                                    (m2/s, northward positive), total (Sv)
  part bl      x vS vM cS cM        northward transport per unit width (m2/s) of
                                    the Stommel and Munk layers, and cumulative
                                    transport from the wall (Sv), x in km
  part values  what value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

OMEGA = 7.292115e-5
A_EARTH = 6371.0e3
RHO = 1025.0
TAU0 = 0.1
LAT_S, LAT_N = 20.0, 50.0
LAT_C = 35.0
WIDTH = 6000.0e3
R_FRIC = 1.0e-6
A_H = 5.0e3
YEAR = 365.25 * 86400.0


def coriolis(lat):
    return 2 * OMEGA * math.sin(math.radians(lat))


def beta(lat):
    return 2 * OMEGA * math.cos(math.radians(lat)) / A_EARTH


def tau(lat):
    """Zonal wind stress (Pa), eastward positive."""
    return -TAU0 * math.cos(math.pi * (lat - LAT_S) / (LAT_N - LAT_S))


def dtau_dlat(lat):
    """d tau / d lat, lat in radians."""
    k = math.pi / math.radians(LAT_N - LAT_S)
    return TAU0 * k * math.sin(math.pi * (lat - LAT_S) / (LAT_N - LAT_S))


def curl_tau(lat):
    """Vertical curl of a zonal stress on the sphere (Pa/m)."""
    p = math.radians(lat)
    d = dtau_dlat(lat) * math.cos(p) - tau(lat) * math.sin(p)
    return -d / (A_EARTH * math.cos(p))


def ekman_pumping(lat):
    """w_E = curl(tau/(rho f)) (m/s, upward positive)."""
    p = math.radians(lat)
    f = coriolis(lat)
    dfdp = 2 * OMEGA * math.cos(p)
    # d/d lat of tau cos(lat) / (rho f)
    dg = (dtau_dlat(lat) * math.cos(p) - tau(lat) * math.sin(p)) / (RHO * f) \
        - tau(lat) * math.cos(p) * dfdp / (RHO * f * f)
    return -dg / (A_EARTH * math.cos(p))


def ekman_transport_y(lat):
    """Northward Ekman volume transport per unit width (m2/s): -tau_x/(rho f)."""
    return -tau(lat) / (RHO * coriolis(lat))


def sverdrup_v(lat):
    """Northward Sverdrup transport per unit width (m2/s)."""
    return curl_tau(lat) / (RHO * beta(lat))


def basin_length():
    return A_EARTH * math.radians(LAT_N - LAT_S)


def plane_amplitude(lat0=LAT_C):
    """A = TAU0 pi / (rho beta L): interior southward transport per unit width
    at mid-basin on the beta-plane (m2/s)."""
    return TAU0 * math.pi / (RHO * beta(lat0) * basin_length())


def stommel_width(lat0=LAT_C, r=R_FRIC):
    return r / beta(lat0)


def munk_width(lat0=LAT_C, ah=A_H):
    return (ah / beta(lat0)) ** (1.0 / 3.0)


def stommel_v(x, lat0=LAT_C, r=R_FRIC):
    a, d = plane_amplitude(lat0), stommel_width(lat0, r)
    return a * ((WIDTH / d) * math.exp(-x / d) - 1.0)


def munk_v(x, lat0=LAT_C, ah=A_H):
    a, d = plane_amplitude(lat0), munk_width(lat0, ah)
    s = x / d
    return a * ((WIDTH / d) * (2 / math.sqrt(3)) * math.exp(-s / 2)
                * math.sin(math.sqrt(3) * s / 2) - 1.0)


def stommel_cum(x, lat0=LAT_C, r=R_FRIC):
    """Northward transport between the wall and x (m3/s)."""
    a, d = plane_amplitude(lat0), stommel_width(lat0, r)
    return a * (WIDTH * (1 - math.exp(-x / d)) - x)


def munk_cum(x, lat0=LAT_C, ah=A_H):
    a, d = plane_amplitude(lat0), munk_width(lat0, ah)
    s = x / d
    q = math.sqrt(3) / 2
    bracket = 1 - math.exp(-s / 2) * (math.cos(q * s) + math.sin(q * s) / math.sqrt(3))
    return a * (WIDTH * bracket - x)


def munk_first_zero(lat0=LAT_C, ah=A_H):
    """Width of the northward Munk jet: first zero of its boundary term."""
    return 2 * math.pi / math.sqrt(3) * munk_width(lat0, ah)


def main():
    merid = []
    for i in range(0, 301):
        lat = LAT_S + i * 0.1
        if lat < LAT_S + 0.05 or lat > LAT_N - 0.05:
            continue
        v = sverdrup_v(lat)
        merid.append([lat, tau(lat), ekman_pumping(lat) * YEAR, v, v * WIDTH / 1e6])
    write_table(__file__, ("lat", "tau", "wE", "V", "Vtot"), merid, part="merid")
    bl = []
    for i in range(0, 401):
        x = i * 1.0e3
        bl.append([x / 1e3, stommel_v(x), munk_v(x), stommel_cum(x) / 1e6, munk_cum(x) / 1e6])
    write_table(__file__, ("x", "vS", "vM", "cS", "cM"), bl, part="bl")
    vmin = min(merid, key=lambda r: r[4])
    vals = [["beta35", beta(LAT_C)], ["f35", coriolis(LAT_C)],
            ["L_km", basin_length() / 1e3], ["A_m2s", plane_amplitude()],
            ["wbc_Sv", plane_amplitude() * WIDTH / 1e6],
            ["wE35_myr", ekman_pumping(LAT_C) * YEAR],
            ["sphere_Vtot_min_Sv", vmin[4]], ["sphere_Vtot_min_lat", vmin[0]],
            ["dS_km", stommel_width() / 1e3], ["dM_km", munk_width() / 1e3],
            ["munk_jet_km", munk_first_zero() / 1e3],
            ["stommel_wall_v", stommel_v(0.0)],
            ["stommel_cum_300_Sv", stommel_cum(300e3) / 1e6],
            ["munk_cum_jet_Sv", munk_cum(munk_first_zero()) / 1e6]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
