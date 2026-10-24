"""A GIS session on the Varden Hills (Year 3, remote sensing and GIS): slope, aspect
and hillshade from the elevation grid, then an overlay.

The digital elevation model is the series' invented region (figdata/shared/region.py,
read only): z = topo(x, y) sampled every STEP metres. Derivatives by central
differences inside the grid and one-sided differences on its edges (numpy.gradient):

    slope  = atan(|grad z|)                                (degrees)
    aspect = the azimuth of steepest DESCENT, atan2(-dz/dx, -dz/dy)   (0 = N, 90 = E)
    hillshade = cos Z cos S + sin Z sin S cos(A_light - aspect), clipped at 0,
                for a light from the azimuth A_light = 315 (north-west), 45 degrees
                above the horizon (Z = 45 degrees from the zenith).

Overlay (a screening for landslide-prone ground above the river): cells whose slope
exceeds 15 degrees AND whose bedrock at the surface is the Jurassic shale AND which
lie within a 1 km buffer of the river (the shortest distance to the river's centre
line, sampled every 5 m).

  part grid     x y z slope aspect shade layers class   km, km, m, deg, deg, 0-1, two codes
                layers: 0 neither, 1 slope > 15 only, 2 shale only, 3 both
                class: 0 other, 1 shale outside the buffer, 2 shale in the buffer,
                3 selected (shale, buffer, slope > 15)
  part buffer   x y                               the 1 km buffer line (km), blank-separated
  part values   what value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import region  # noqa: E402

STEP = 100.0
SLOPE_MIN = 15.0
BUFFER = 1000.0
LIGHT_AZ, LIGHT_ALT = 315.0, 45.0


def grid(step=STEP):
    xs = np.arange(0.0, region.WIDTH + step / 2, step)
    ys = np.arange(0.0, region.HEIGHT + step / 2, step)
    z = np.array([[region.topo(x, y) for x in xs] for y in ys])
    return xs, ys, z


def derivatives(z, step=STEP):
    """(dz/dx, dz/dy): rows of z are y (north), columns x (east)."""
    dzdy, dzdx = np.gradient(z, step)
    return dzdx, dzdy


def slope_deg(dzdx, dzdy):
    return np.degrees(np.arctan(np.hypot(dzdx, dzdy)))


def aspect_deg(dzdx, dzdy):
    a = np.degrees(np.arctan2(-dzdx, -dzdy))
    return np.where(a < 0, a + 360.0, a)


def hillshade(slope, aspect, az=LIGHT_AZ, alt=LIGHT_ALT):
    zen = math.radians(90.0 - alt)
    s, a = np.radians(slope), np.radians(aspect)
    h = math.cos(zen) * np.cos(s) + math.sin(zen) * np.sin(s) * np.cos(math.radians(az) - a)
    return np.clip(h, 0.0, 1.0)


def river_distance(xs, ys):
    rx = np.arange(0.0, region.WIDTH + 1, 5.0)
    ry = np.array([region.river_y(x) for x in rx])
    return np.array([[np.min(np.hypot(rx - x, ry - y)) for x in xs] for y in ys])


def overlay(slope, units, dist):
    shale = units == region.UNIT["shale"]
    inbuf = dist <= BUFFER
    cls = np.zeros(slope.shape, dtype=int)
    cls[shale] = 1
    cls[shale & inbuf] = 2
    cls[shale & inbuf & (slope > SLOPE_MIN)] = 3
    return cls


def layers(slope, units):
    steep = slope > SLOPE_MIN
    shale = units == region.UNIT["shale"]
    return steep.astype(int) + 2 * shale.astype(int)


def main():
    xs, ys, z = grid()
    dzdx, dzdy = derivatives(z)
    s = slope_deg(dzdx, dzdy)
    a = aspect_deg(dzdx, dzdy)
    hs = hillshade(s, a)
    units = np.array([[region.unit(x, y, z[j, i]) for i, x in enumerate(xs)]
                      for j, y in enumerate(ys)])
    d = river_distance(xs, ys)
    cls = overlay(s, units, d)
    lay = layers(s, units)
    rows = []
    for j, y in enumerate(ys):
        for i, x in enumerate(xs):
            rows.append((x / 1e3, y / 1e3, z[j, i], s[j, i], a[j, i], hs[j, i], lay[j, i],
                         cls[j, i]))
    write_table(__file__, ("x", "y", "z", "slope", "aspect", "shade", "layers", "class"), rows,
                part="grid")
    lines = region.trace(d, xs, ys, BUFFER)
    out = []
    for line in lines:
        line = region.simplify(line, 5.0)
        out += ([()] if out else []) + [(round(x / 1e3, 4), round(y / 1e3, 4)) for x, y in line]
    write_table(__file__, ("x", "y"), out, part="buffer")
    cell = STEP * STEP / 1e6
    vals = [["slope_max", s.max()], ["slope_mean", s.mean()],
            ["frac_slope_gt15", float((s > SLOPE_MIN).mean())],
            ["shale_km2", float((cls >= 1).sum() * cell)],
            ["shale_buffer_km2", float((cls >= 2).sum() * cell)],
            ["selected_km2", float((cls == 3).sum() * cell)],
            ["steep_shale_km2", float((lay == 3).sum() * cell)],
            ["selected_cells", int((cls == 3).sum())], ["cells", int(cls.size)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()
