"""Rossby waves on a beta-plane (Year 3, atmospheric dynamics).

Linearising the barotropic vorticity equation about a uniform westerly U gives
the dispersion relation

    omega = U k - beta k / (k^2 + l^2),

with phase speed c = U - beta/K^2 and zonal group velocity
c_g = U + beta (k^2 - l^2)/K^4. A wave with l = 0 is stationary when
K = K_s = sqrt(beta/U); round a latitude circle its zonal wavenumber is
n_s = a cos(lat) K_s = sqrt(2 Omega a cos^3(lat) / U).

Omega is the GRS80 value (geod5:grs80-defining), a the mean radius
(earth:Rmean). The observed stationary wavenumber uses the January zonal-mean
wind at 300 hPa of the NCEP-NCAR Reanalysis 1, 1991-2020 (shared derived table
data/derived/bachelor-1-ncep-uwnd-p.csv, ledger data:b5-ncep-uwnd).

  part disp     n c0 cg0 c15 cg15     phase speed and group velocity (m/s) of zonal
                                      wavenumber n at LAT, l = 0, for U = 0 and 15 m/s
  part stat     lat n10 n15 n20       stationary zonal wavenumber for U = 10, 15, 20 m/s
  part statobs  lat u300 ns           January zonal-mean u at 300 hPa and n_s from it
  part values   what value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
UWND = os.path.join(ROOT, "data", "derived", "bachelor-1-ncep-uwnd-p.csv")
OMEGA = 7.292115e-5
A_EARTH = 6371.0e3
LAT = 45.0
U_JET = 15.0


def beta(lat):
    return 2 * OMEGA * math.cos(math.radians(lat)) / A_EARTH


def coriolis(lat):
    return 2 * OMEGA * math.sin(math.radians(lat))


def k_of_n(n, lat=LAT):
    """Zonal wavenumber (1/m) of n waves round the latitude circle."""
    return n / (A_EARTH * math.cos(math.radians(lat)))


def omega(k, l, u, lat=LAT):
    return u * k - beta(lat) * k / (k * k + l * l)


def phase_speed(k, l, u, lat=LAT):
    return u - beta(lat) / (k * k + l * l)


def group_velocity(k, l, u, lat=LAT):
    kk = k * k + l * l
    return u + beta(lat) * (k * k - l * l) / kk ** 2


def stationary_n(u, lat):
    if u <= 0:
        return float("nan")
    return math.sqrt(2 * OMEGA * A_EARTH * math.cos(math.radians(lat)) ** 3 / u)


def stationary_wavelength(u, lat):
    return 2 * math.pi * math.sqrt(u / beta(lat))


def load_u300():
    d = {}
    with open(UWND, encoding="utf8") as f:
        for r in csv.DictReader(f):
            if int(r["month"]) == 1 and int(r["level"]) == 300:
                d[float(r["lat"])] = float(r["value"])
    return d


def main():
    rows = []
    for i in range(10, 121):
        n = i / 10
        k = k_of_n(n)
        rows.append([n, phase_speed(k, 0, 0.0), group_velocity(k, 0, 0.0),
                     phase_speed(k, 0, U_JET), group_velocity(k, 0, U_JET)])
    write_table(__file__, ("n", "c0", "cg0", "c15", "cg15"), rows, part="disp")
    write_table(__file__, ("lat", "n10", "n15", "n20"),
                [[lat, stationary_n(10, lat), stationary_n(15, lat), stationary_n(20, lat)]
                 for lat in range(20, 76)], part="stat")
    u300 = load_u300()
    write_table(__file__, ("lat", "u300", "ns"),
                [[lat, u, stationary_n(u, lat)] for lat, u in sorted(u300.items())
                 if 20 <= lat <= 75 and u > 2], part="statobs")
    vals = [["beta45", beta(LAT)], ["f45", coriolis(LAT)],
            ["ns_45_15", stationary_n(U_JET, LAT)],
            ["lambda_s_45_15_km", stationary_wavelength(U_JET, LAT) / 1e3],
            ["circ_45_km", 2 * math.pi * A_EARTH * math.cos(math.radians(LAT)) / 1e3]]
    for n in range(3, 9):
        k = k_of_n(n)
        vals.append(["c15_n%d" % n, phase_speed(k, 0, U_JET)])
        vals.append(["cg15_n%d" % n, group_velocity(k, 0, U_JET)])
    for lat in (40.0, 45.0, 50.0, 55.0):
        vals.append(["u300_jan_%d" % lat, u300[lat]])
        vals.append(["ns_obs_%d" % lat, stationary_n(u300[lat], lat)])
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
