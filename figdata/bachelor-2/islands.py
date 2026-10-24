"""Oceanic islands (Year 2, oceanic-islands): the thermal sinking of an island carried by its
plate, the rates that compete at a reef, and the deep holes drilled on Pacific atolls.

  depth--age  Parsons and Sclater (1977), Book 2 row ps77:depth-age and Book 3 row
              parsons:plate-model: d = 2500 + 350 t^1/2 m (t in Myr, 0 to 70 Myr) and
              d = 6400 - 3200 exp(-t / 62.8) m beyond 20 Myr. The two branches cross twice;
              `depth` uses the root law up to the first crossing above 20 Myr and the
              exponential beyond, so that the floor never jumps.
  rates       loading subsidence 2.6 m/kyr off Hawaii and thermal 0.01 m/kyr along the ridge
              (cs14:subsidence); reef accretion 4.2 mm/yr (Book 3 row perry:chagos); mean
              deglacial sea-level rise about 10 mm/yr and Meltwater Pulse 1A 24-44 mm/yr
              (Book 2 row ipcc:lgm-sea).
  holes       deep holes on atolls, total depth and depth to basalt, in feet (ls60:holes,
              ls60:enewetak), converted to metres (1 ft = 0.3048 m exactly).
  petrel      the INVENTED island of the chapter's problem: built on a plate 10 Myr old, its
              volcanic summit 1000 m above sea level when growth ends, the last volcanic rock
              gone below sea level 12 Myr later, then an atoll until the plate is 70 Myr old.

  part sink     dt_Myr  t2 t10 t30 t60          (thermal subsidence since birth, m)
  part rates    t_Myr  thermal_mm_yr             (thermal subsidence rate on the plate)
  part holes    name year td_m basalt_m         (deep holes on atolls)
  part petrel   t_Myr  summit_m                  (volcanic summit of the invented island)
  part numbers  key value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

D0, C = 2500.0, 350.0            # root law: d = D0 + C sqrt(t), m and m / Myr^0.5
DINF, DE, TAU = 6400.0, 3200.0, 62.8   # exponential law: d = DINF - DE exp(-t / TAU)
FT = 0.3048

HOLES = [("Funafuti", 1898, 1114.0, None), ("Kita-daito-jima", 1936, 1416.0, None),
         ("Bikini", 1947, 2556.0, None), ("Eniwetok K-1B", 1951, 1280.0, None),
         ("Eniwetok F-1", 1952, 4630.0, 4610.0), ("Eniwetok E-1", 1952, 4222.0, 4158.0)]

PETREL_T0, PETREL_H, PETREL_GONE, PETREL_DROWN = 10.0, 1000.0, 22.0, 70.0


def depth_root(t):
    return D0 + C * math.sqrt(t)


def depth_exp(t):
    return DINF - DE * math.exp(-t / TAU)


def switch_age():
    """First crossing of the two branches above 20 Myr (bisection on their difference)."""
    f = lambda t: depth_root(t) - depth_exp(t)
    # the difference changes sign between 20 and 30 Myr
    lo, hi = 20.0, 30.0
    assert f(lo) * f(hi) < 0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


T_SW = switch_age()


def depth(t):
    return depth_root(t) if t <= T_SW else depth_exp(t)


def rate(t):
    """Thermal subsidence rate of the floor at plate age t (m/Myr)."""
    return C / (2 * math.sqrt(t)) if t <= T_SW else DE / TAU * math.exp(-t / TAU)


def sink(t0, dt):
    """Thermal subsidence of an island built on a plate of age t0, dt Myr later (m)."""
    return depth(t0 + dt) - depth(t0)


def sink_root(t1, t2):
    """The same with the root law alone: C (sqrt t2 - sqrt t1)."""
    return C * (math.sqrt(t2) - math.sqrt(t1))


def age_for_rate(r):
    """Plate age at which the exponential branch sinks at r m/Myr."""
    return TAU * math.log(DE / TAU / r)


def petrel_summit(t):
    """Volcanic summit of the invented island against plate age: falls linearly by erosion
    from PETREL_H at PETREL_T0 and by thermal subsidence (root law), reaching sea level at
    PETREL_GONE; after that, the top of the drowned volcanic platform under the reef."""
    s = sink_root(PETREL_T0, PETREL_GONE)
    e = (PETREL_H - s) / (PETREL_GONE - PETREL_T0)          # mean erosion rate, m/Myr
    if t <= PETREL_GONE:
        return PETREL_H - e * (t - PETREL_T0) - sink_root(PETREL_T0, t)
    return -sink_root(PETREL_GONE, t)


def numbers():
    s = sink_root(PETREL_T0, PETREL_GONE)
    d = {"t_switch": round(T_SW, 2), "d_switch": round(depth(T_SW), 1),
         "rate_100": round(rate(100.0), 2), "age_rate10": round(age_for_rate(10.0), 1),
         "petrel_floor": round(depth_root(PETREL_T0), 1),
         "petrel_sink": round(s, 1), "petrel_erosion": round(PETREL_H - s, 1),
         "petrel_erosion_rate": round((PETREL_H - s) / (PETREL_GONE - PETREL_T0), 2),
         "petrel_cap": round(sink_root(PETREL_GONE, PETREL_DROWN), 1),
         "petrel_guyot_sink": round(depth_exp(120.0) - depth_exp(PETREL_DROWN), 1)}
    for name, _y, td, b in HOLES:
        key = name.split()[-1].replace("-", "_")
        d["td_%s" % key] = round(td * FT, 1)
        if b is not None:
            d["basalt_%s" % key] = round(b * FT, 1)
    return d


if __name__ == "__main__":
    dts = [0.5 * i for i in range(0, 201)]
    write_table(__file__, ("dt_Myr", "t2", "t10", "t30", "t60"),
                [(dt,) + tuple(round(sink(t0, dt), 1) for t0 in (2.0, 10.0, 30.0, 60.0))
                 for dt in dts], part="sink")
    ts = [1.0 + 0.5 * i for i in range(0, 299)]
    write_table(__file__, ("t_Myr", "thermal_mm_yr"),
                [(t, round(rate(t) / 1000.0, 5)) for t in ts], part="rates")
    write_table(__file__, ("name", "year", "td_m", "basalt_m"),
                [(n.replace(" ", "-"), y, round(td * FT, 1), round(b * FT, 1) if b else "nan")
                 for n, y, td, b in HOLES], part="holes")
    tp = [PETREL_T0 + 0.5 * i for i in range(0, 121)]
    write_table(__file__, ("t_Myr", "summit_m"), [(t, round(petrel_summit(t), 1)) for t in tp],
                part="petrel")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")
