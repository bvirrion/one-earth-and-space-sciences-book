"""Magnetic anomaly profiles across a spreading ridge (grade 11, drift-to-spreading).

The polarity time scale is Cande and Kent (1995) (ledger ck95:chrons): the intervals
of normal polarity of the last 10 million years. Crust formed at time t before
present lies at |x| = u t from the ridge axis, u being the half rate; it keeps the
polarity of the field at t. The magnetised layer is a sheet of blocks, top z1 and
bottom z2 below the sea surface, magnetised vertically (+M where the polarity is
normal, -M where it is reversed), as at high latitude where the field is vertical.

Field of one block (x1 < x < x2, z1 < z < z2) at a point x0 of the sea surface,
vertical component, from the magnetic 'charges' +-M on its top and bottom faces:

    dB(x0) = (mu0 M / 2 pi) [ (atan((x2-x0)/z1) - atan((x1-x0)/z1))
                            - (atan((x2-x0)/z2) - atan((x1-x0)/z2)) ]

An infinite uniform sheet gives no anomaly (the two angles are both pi); the sum over
the blocks is the anomaly. The model is a teaching model: its numbers (depth,
thickness, magnetisation) are chosen, not measured.

  part fast, slow       x_km anomaly_nT       profiles, half rates 7.5 and 1.25 cm/yr
  part fastblocks, slowblocks  x poly...      normal-polarity blocks as polygons
  part block            x y                   the block diagram: normal stripes on the
                                              top face (oblique projection), polygons
                                              separated by empty lines
  part timescale        x y                   normal intervals 0-5.5 Ma as rectangles
  part numbers          key value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import out_path, write_table  # noqa: E402

# Cande and Kent (1995): normal-polarity intervals (Ma), 0-10 Ma
NORMAL = [(0.000, 0.780), (0.990, 1.070), (1.770, 1.950), (2.140, 2.150), (2.581, 3.040),
          (3.110, 3.220), (3.330, 3.580), (4.180, 4.290), (4.480, 4.620), (4.800, 4.890),
          (4.980, 5.230), (5.894, 6.137), (6.269, 6.567), (6.935, 7.091), (7.135, 7.170),
          (7.341, 7.375), (7.432, 7.562), (7.650, 8.072), (8.225, 8.257), (8.699, 9.025),
          (9.230, 9.308), (9.580, 9.642), (9.740, 9.880), (9.920, 10.949)]
T_MAX = 10.0                  # Ma, end of the table used
MU0_OVER_2PI = 2e-7           # T m / A
M = 5.0                       # A/m, chosen
Z1, Z2 = 3.0, 4.0             # km below the sea surface, chosen
RATES = {"fast": 7.5, "slow": 1.25}   # half rates, cm/yr (= 10 km per Myr per cm/yr)
SPAN_MA = 5.0                 # each profile shows crust up to 5 Myr old on both sides


def polarity(t):
    """+1 if the field was normal at t (Ma), else -1."""
    return 1 if any(a <= t < b for a, b in NORMAL) else -1


def blocks(half_rate_cm_yr):
    """Blocks (x1, x2, sign) in km over |x| < half_rate * T_MAX, symmetric about 0."""
    u = 10.0 * half_rate_cm_yr                     # km per Myr
    edges = sorted({0.0, T_MAX} | {t for ab in NORMAL for t in ab if t < T_MAX})
    out = []
    for t0, t1 in zip(edges[:-1], edges[1:]):
        s = polarity(0.5 * (t0 + t1))
        out.append((u * t0, u * t1, s))
        out.append((-u * t1, -u * t0, s))
    return sorted(out)


def anomaly(x0, bl, z1=Z1, z2=Z2, m=M):
    """Vertical anomaly (nT) at x0 (km) above the blocks."""
    total = 0.0
    for x1, x2, s in bl:
        top = math.atan((x2 - x0) / z1) - math.atan((x1 - x0) / z1)
        bot = math.atan((x2 - x0) / z2) - math.atan((x1 - x0) / z2)
        total += s * (top - bot)
    return MU0_OVER_2PI * m * total * 1e9


def profile(name, n=None):
    u = 10.0 * RATES[name]
    bl = blocks(RATES[name])
    xm = u * SPAN_MA
    n = n or (1501 if name == "fast" else 801)
    return [(-xm + 2 * xm * k / (n - 1), anomaly(-xm + 2 * xm * k / (n - 1), bl)) for k in range(n)]


def boundary_distance(t_ma, half_rate_cm_yr):
    """Distance (km) from the axis of the polarity change at t_ma."""
    return 10.0 * half_rate_cm_yr * t_ma


def block_polygons(name, ylo, yhi):
    """Normal blocks of the profile's span as rectangles (for drawing under the plot)."""
    xm = 10.0 * RATES[name] * SPAN_MA
    rows = []
    for x1, x2, s in blocks(RATES[name]):
        if s > 0 and x2 > -xm and x1 < xm:
            a, b = max(x1, -xm), min(x2, xm)
            rows += [(a, ylo), (b, ylo), (b, yhi), (a, yhi), (a, ylo), ()]
    return rows


def block_diagram(span_km=300.0, depth=60.0, shear=0.45, rise=0.35, length=200.0):
    """Top face of a block of sea floor (fast ridge) in an oblique projection: a point
    (x across the ridge, y along it) goes to (x + shear*y, rise*y). Normal stripes
    as polygons, plus the front face (x, -depth..0)."""
    rows = []
    for x1, x2, s in blocks(RATES["fast"]):
        if s < 0 or x2 <= -span_km or x1 >= span_km:
            continue
        a, b = max(x1, -span_km), min(x2, span_km)
        top = [(a, 0.0), (b, 0.0), (b, length), (a, length)]
        rows += [(x + shear * y, rise * y) for x, y in top] + [(a, 0.0), ()]
        rows += [(a, 0.0), (b, 0.0), (b, -depth), (a, -depth), (a, 0.0), ()]
    return rows


def timescale_polygons(t_max=5.5, ylo=0.0, yhi=1.0):
    """Normal intervals younger than t_max (Ma) as rectangles, x = age."""
    rows = []
    for a, b in NORMAL:
        if a < t_max:
            b = min(b, t_max)
            rows += [(a, ylo), (b, ylo), (b, yhi), (a, yhi), (a, ylo), ()]
    return rows


def numbers():
    n = {}
    for name, u in RATES.items():
        p = profile(name)
        n[name + "_max_nT"] = max(a for _, a in p)
        n[name + "_bm_km"] = boundary_distance(0.780, u)
        n[name + "_gg_km"] = boundary_distance(3.580, u)
        n[name + "_jaramillo_width_km"] = boundary_distance(1.070 - 0.990, u)
    n["fast_full_rate_from_gg"] = 2 * n["fast_gg_km"] / 3.580 / 10.0
    return n


if __name__ == "__main__":
    for name in RATES:
        write_table(__file__, ("x_km", "anomaly_nT"), profile(name), part=name, digits=5)
        write_table(__file__, ("x", "y"), block_polygons(name, -1.0, 1.0), part=name + "blocks", digits=5)
    write_table(__file__, ("x", "y"), block_diagram(), part="block", digits=5)
    write_table(__file__, ("x", "y"), timescale_polygons(), part="timescale", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")
