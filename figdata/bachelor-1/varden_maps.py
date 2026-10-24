"""Numbers and rasters for the Varden Hills chapters of Year 1 (geological-maps).

Everything comes from the model of figdata/shared/region.py:

  part boreholes  id x_km y_km ground_m depth_m contact_m
                  six boreholes, three on each limb of the anticline, each
                  reaching the BASE of the limestone (depth below the ground)
  part fault      id x_km y_km z_m   three points of the fault trace on the
                  ground (where the fault plane meets the topography)
  part attitude   name dipdir_deg dip_deg    planes through each triple
                  (east limb E, west limb W, fault F) and the fold axis
                  (trend, plunge) = intersection of the two limb planes
  part shade      x_km y_km shade   a 100 m DEM of the region, lit from the
                  north-west at 45 degrees (pgfplots matrix plot*, 101 x 81)
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))
from _table import write_table  # noqa: E402
import region as R  # noqa: E402

BOREHOLES = [("E1", 4000.0, 6000.0), ("E2", 4600.0, 7200.0), ("E3", 5100.0, 6400.0),
             ("W1", 1500.0, 6000.0), ("W2", 2200.0, 7200.0), ("W3", 2600.0, 5400.0)]
FAULT_Y = [("F1", 1000.0), ("F2", 3500.0), ("F3", 6500.0)]


def borehole(x, y):
    zg = R.topo(x, y)
    zc = R.contact_elevation("limestone", x, y)
    return zg, zg - zc, zc


def plane_attitude(p1, p2, p3):
    """(dip direction azimuth in degrees, dip in degrees) of the plane through
    three points (x east, y north, z up)."""
    n = np.cross(np.subtract(p2, p1), np.subtract(p3, p1))
    if n[2] < 0:
        n = -n
    dip = math.degrees(math.acos(n[2] / np.linalg.norm(n)))
    az = math.degrees(math.atan2(n[0], n[1])) % 360.0      # horizontal part of the upward normal points down-dip
    return az, dip


def normal(p1, p2, p3):
    n = np.cross(np.subtract(p2, p1), np.subtract(p3, p1))
    return n if n[2] > 0 else -n


def line_trend_plunge(v):
    """Trend (azimuth) and plunge of a line, pointing downwards."""
    v = np.asarray(v, dtype=float)
    if v[2] > 0:
        v = -v
    trend = math.degrees(math.atan2(v[0], v[1])) % 360.0
    plunge = math.degrees(math.atan2(-v[2], math.hypot(v[0], v[1])))
    return trend, plunge


def fault_point(y):
    """The point of the fault trace on the ground at northing y (bisection in x)."""
    ux, uy = R._fault_u()
    fx, fy, fz = R.FAULT_POINT
    g = lambda x: (x - fx) * ux + (y - fy) * uy + (R.topo(x, y) - fz) / math.tan(math.radians(R.FAULT_DIP))  # noqa: E731
    a, b = 0.0, R.WIDTH
    for _ in range(100):
        m = (a + b) / 2
        a, b = (m, b) if (g(a) > 0) == (g(m) > 0) else (a, m)
    x = (a + b) / 2
    return x, y, R.topo(x, y)


def attitudes():
    pts = {i: (x, y, borehole(x, y)[2]) for i, x, y in BOREHOLES}
    east = [pts["E1"], pts["E2"], pts["E3"]]
    west = [pts["W1"], pts["W2"], pts["W3"]]
    fault = [fault_point(y) for _, y in FAULT_Y]
    axis = np.cross(normal(*east), normal(*west))
    return {"E": plane_attitude(*east), "W": plane_attitude(*west),
            "F": plane_attitude(*fault), "axis": line_trend_plunge(axis)}


def hillshade(step=100.0, az=315.0, alt=45.0):
    xs = np.arange(0.0, R.WIDTH + 1, step)
    ys = np.arange(0.0, R.HEIGHT + 1, step)
    z = np.array([[R.topo(x, y) for x in xs] for y in ys])
    dzdy, dzdx = np.gradient(z, step)
    slope = np.arctan(np.hypot(dzdx, dzdy))
    aspect = np.arctan2(-dzdx, -dzdy)                      # azimuth of steepest descent
    a, h = math.radians(az), math.radians(alt)
    shade = np.cos(h) * np.cos(slope) + np.sin(h) * np.sin(slope) * np.cos(a - aspect)
    return xs, ys, np.clip(shade, 0, 1)


if __name__ == "__main__":
    rows = []
    for i, x, y in BOREHOLES:
        zg, d, zc = borehole(x, y)
        rows.append((i, x / 1000, y / 1000, round(zg), round(zg) - round(zc), round(zc)))   # depth = ground - contact as printed
    write_table(__file__, ("id", "x_km", "y_km", "ground_m", "depth_m", "contact_m"), rows, part="boreholes")
    write_table(__file__, ("id", "x_km", "y_km", "z_m"),
                [(i,) + tuple(round(v, 3 if k < 2 else 0) for k, v in
                              enumerate((fault_point(y)[0] / 1000, y / 1000, fault_point(y)[2])))
                 for i, y in FAULT_Y], part="fault")
    att = attitudes()
    write_table(__file__, ("name", "dipdir_deg", "dip_deg"),
                [(k, round(v[0], 1), round(v[1], 2)) for k, v in att.items()], part="attitude")
    xs, ys, sh = hillshade()
    write_table(__file__, ("x_km", "y_km", "shade"),
                [(round(x / 1000, 2), round(y / 1000, 2), round(float(sh[j, i]), 3))
                 for j, y in enumerate(ys) for i, x in enumerate(xs)], part="shade")
