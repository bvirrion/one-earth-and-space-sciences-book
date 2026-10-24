"""Density of CO2 with depth (Year 2, energy-geology), and the storage capacity of a formation.

  Data: data/derived/bachelor-2-co2-density.csv (ledger data:b4-co2-density), derived by
  tools/fetch_data.py from the NIST Chemistry WebBook (Span and Wagner 1996 equation of state)
  along the conditions of IPCC SRCCS (2005) Figure 5.2: surface at 15 degC, gradient 25 degC/km,
  hydrostatic pressure (fresh water, plus one atmosphere). Depths 0 to 3000 m every 100 m.

  CO2 critical point (NIST WebBook, Suehiro et al. 1996): 304.18 K, 7.380 MPa (ledger
  nist:co2-critical).

  profile   depth_m, t_c, p_mpa, rho (kg/m3), vrel (volume of one tonne relative to its volume
            at the surface, rho_surface / rho).
  critical  the depth at which the profile crosses the critical temperature and the critical
            pressure (both found by linear interpolation in depth: exact for the linear T and p).
  numbers   key values quoted in the text.

  part profile   depth_m t_c p_mpa rho vrel
  part critical  key value
  part numbers   key value
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

CSV = os.path.join(HERE, "..", "..", "data", "derived", "bachelor-2-co2-density.csv")
TC_K, PC_MPA = 304.18, 7.380


def read_profile():
    with open(CSV, newline="", encoding="utf-8") as f:
        return [(float(r["depth_m"]), float(r["t_c"]), float(r["p_mpa"]), float(r["rho"]))
                for r in csv.DictReader(f)]


def rho_at(z, prof=None):
    """Density (kg/m3) at depth z by linear interpolation in the table."""
    prof = prof or read_profile()
    for (z1, _, _, r1), (z2, _, _, r2) in zip(prof, prof[1:]):
        if z1 <= z <= z2:
            return r1 + (z - z1) * (r2 - r1) / (z2 - z1)
    raise ValueError("depth outside the table")


def critical_depths(prof=None):
    """Depths (m) where the temperature reaches Tc and the pressure reaches pc."""
    prof = prof or read_profile()
    tc_c = TC_K - 273.15
    out = {}
    for (z1, t1, p1, _), (z2, t2, p2, _) in zip(prof, prof[1:]):
        if t1 <= tc_c <= t2 and "z_tc" not in out:
            out["z_tc"] = z1 + (tc_c - t1) * (z2 - z1) / (t2 - t1)
        if p1 <= PC_MPA <= p2 and "z_pc" not in out:
            out["z_pc"] = z1 + (PC_MPA - p1) * (z2 - z1) / (p2 - p1)
    return out


def storage_capacity(area_m2, h_m, phi, rho, e):
    """Mass (kg) of CO2 stored in a formation: M = A h phi rho E."""
    return area_m2 * h_m * phi * rho * e


def numbers():
    prof = read_profile()
    r0 = prof[0][3]
    d = {"rho_%d" % z: rho_at(z, prof) for z in (0, 500, 700, 800, 900, 1000, 1500, 2000, 3000)}
    d["vol_ratio_0_over_1000"] = r0 / rho_at(1000, prof)
    d["vol_ratio_0_over_2000"] = r0 / rho_at(2000, prof)
    d.update(critical_depths(prof))
    return d


def main():
    prof = read_profile()
    r0 = prof[0][3]
    write_table(__file__, ("depth_m", "t_c", "p_mpa", "rho", "vrel"),
                [(z, t, p, r, r0 / r) for z, t, p, r in prof], part="profile")
    write_table(__file__, ("key", "value"), sorted(critical_depths(prof).items()), part="critical")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")


if __name__ == "__main__":
    main()
