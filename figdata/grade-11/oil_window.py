"""Burial history of an invented sedimentary basin, grade 11, the geology of coal, oil and gas.

The Merrow Basin is invented for the book. Its sediments pile up in episodes,
each at a steady rate; the last episode is an uplift during which the top of
the pile is eroded. Compaction is ignored: a layer keeps its thickness once
deposited, so the depth of a horizon at time t is the thickness laid down on
top of it between its own age and t (minus what erosion has removed).

The temperature grows linearly with depth (a constant geotherm, recalled from
the chapter on the lithosphere): T = T0 + G z, with T0 = 20 degC at the surface
and G = 30 degC/km in the basin (the conterminous-US mean is 29 degC/km; ledger
usgs:gradient-29). The oil window is 60-120 degC (Earle; ledger earle:oil-window);
beyond 120 degC the kerogen mostly gives methane.

  part history   age z165 z150 z120 z95 z66   depth (km) of five horizons, named by age (nan before deposition)
  part temp      age T                        temperature of the source rock (degC)
  part windows   G z_top z_base               depth (km) of the top and base of the oil window against the geotherm
  part numbers   key value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

T0 = 20.0            # degC, surface temperature of the basin
G = 30.0             # degC/km, geotherm of the basin
OIL_TOP = 60.0       # degC
OIL_BASE = 120.0     # degC
TRAP_AGE = 80.0      # Ma, folding of the anticline (invented)

# (start, end, thickness in m): ages in Ma, start older than end; negative = erosion
EPISODES = (
    (165.0, 150.0, 400.0),
    (150.0, 120.0, 800.0),
    (120.0, 95.0, 1100.0),
    (95.0, 66.0, 700.0),
    (66.0, 35.0, 700.0),
    (35.0, 20.0, 300.0),
    (20.0, 0.0, -500.0),
)
SOURCE_AGE = 165.0
HORIZONS = (165.0, 150.0, 120.0, 95.0, 66.0)   # source rock; tops of the black shale, sandstone, mudstone, chalk


def depth(age_deposit, t):
    """Depth (km) at time t (Ma) of the horizon deposited at age_deposit (Ma); None before deposition."""
    if t > age_deposit:
        return None
    z = 0.0
    for a, b, h in EPISODES:
        lo, hi = max(b, t), min(a, age_deposit)       # part of the episode between the deposit and t
        if hi > lo:
            z += h * (hi - lo) / (a - b)
    return z / 1000.0


def temperature(z_km, t0=T0, g=G):
    return t0 + g * z_km


def source_temperature(t, g=G):
    return temperature(depth(SOURCE_AGE, t), g=g)


def window_depths(g, t0=T0):
    """Depths (km) of the top and the base of the oil window for a geotherm g (degC/km)."""
    return (OIL_TOP - t0) / g, (OIL_BASE - t0) / g


def crossings(T_target, age_deposit=SOURCE_AGE, g=G):
    """Ages (Ma) at which the horizon's temperature passes T_target, with the sense (+1 heating, -1 cooling).

    The depth is piecewise linear in time (one piece per episode), so each crossing is found exactly."""
    out = []
    for a, b, h in EPISODES:
        if b >= age_deposit:
            continue
        a = min(a, age_deposit)
        Ta = temperature(depth(age_deposit, a), g=g)
        Tb = temperature(depth(age_deposit, b), g=g)
        if (Ta - T_target) * (Tb - T_target) < 0:
            t = a + (T_target - Ta) * (b - a) / (Tb - Ta)
            out.append((t, 1 if Tb > Ta else -1))
    return out


def numbers():
    n = {}
    n["enter_oil_Ma"] = crossings(OIL_TOP)[0][0]
    n["leave_oil_Ma"] = crossings(OIL_BASE)[0][0]
    n["z_top_km"], n["z_base_km"] = window_depths(G)
    zs = [depth(SOURCE_AGE, t) for t in range(165, -1, -1)]
    n["z_max_km"] = max(zs)
    n["T_max"] = temperature(n["z_max_km"])
    n["z_today_km"] = depth(SOURCE_AGE, 0.0)
    n["T_today"] = temperature(n["z_today_km"])
    n["oil_span_Myr"] = n["enter_oil_Ma"] - n["leave_oil_Ma"]
    n["after_trap_frac"] = (TRAP_AGE - n["leave_oil_Ma"]) / n["oil_span_Myr"]
    n["enter_oil_G40_Ma"] = crossings(OIL_TOP, g=40.0)[0][0]        # a hotter basin (exercise)
    n["leave_oil_G40_Ma"] = crossings(OIL_BASE, g=40.0)[0][0]
    return n


if __name__ == "__main__":
    nan = float("nan")
    rows = []
    for t in [165 - i * 0.5 for i in range(331)]:
        row = [t]
        for h in HORIZONS:
            z = depth(h, t)
            row.append(nan if z is None else z)
        rows.append(row)
    write_table(__file__, ("age", "z165", "z150", "z120", "z95", "z66"), rows, part="history", digits=5)
    write_table(__file__, ("age", "T"), [(r[0], temperature(r[1])) for r in rows], part="temp", digits=5)
    write_table(__file__, ("G", "z_top", "z_base"),
                [(g, *window_depths(g)) for g in range(15, 51)], part="windows", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=5)
    assert not math.isnan(numbers()["enter_oil_Ma"])
