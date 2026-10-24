"""The eight planets compared (grade 6, earth-a-planet).

Every value is read from the shared NASA planetary fact-sheet rows of
sources/data_ledger.md (ids planet:<Name>.<field>), so that the book and the
ledger cannot drift apart.

  part sizes   : name kind d_km d_cm x_cm      (circles to scale, one row)
  part density : idx name kind density_gcm3     (bar chart, g per cm3)
  part temp    : idx name dist_Mkm tmean_C      (in order of distance)
  part trio    : name psurf_bar tmean_C dist_Mkm water   (Venus, Earth, Mars)
  part dist    : name dist_Mkm x_cm x_inner_cm   (distances to scale on a 13.6 cm line;
                 x_inner_cm: the four rocky planets on a line ten times longer)
  part model   : name d_cm dist_m                   (a model in which the Earth is 1 cm wide)
  main table   : name kind d_km d_vs_earth_pct density_gcm3 dist_Mkm tmean_C
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLANETS = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
ROW_WIDTH_CM = 13.6      # the row of circles fills about the text width
GAP_CM = 0.3


def ledger():
    """{id: float} for every planet:* row of the shared data ledger."""
    out = {}
    path = os.path.join(ROOT, "sources", "data_ledger.md")
    for line in open(path, encoding="utf8"):
        m = re.match(r"\|\s*(planet:[A-Za-z]+\.[A-Za-z]+)\s*\|[^|]*\|\s*([-0-9.]+)\s*\|", line)
        if m:
            out[m.group(1)] = float(m.group(2))
    return out


def value(name, field, led=None):
    led = led or ledger()
    return led["planet:%s.%s" % (name, field)]


def density_gcm3(name, led=None):
    return value(name, "density", led) / 1000.0


def kind(name, led=None):
    """Rocky above 3 g/cm3, giant below 2 g/cm3: the eight planets fall in two
    groups with nothing in between."""
    d = density_gcm3(name, led)
    if d > 3.0:
        return "rocky"
    if d < 2.0:
        return "giant"
    raise ValueError(name)


def percent_of_earth(name, field="diameter", led=None):
    return 100.0 * value(name, field, led) / value("Earth", field, led)


def sun_cm(led=None):
    """Width of the Sun drawn at the scale of the row of circles (ledger sun:R)."""
    path = os.path.join(ROOT, "sources", "data_ledger.md")
    r = [float(l.split("|")[3]) for l in open(path, encoding="utf8") if l.startswith("| sun:R |")][0]
    return 2 * r * circles(led)[1]


def circles(led=None):
    led = led or ledger()
    d = [value(p, "diameter", led) for p in PLANETS]
    scale = (ROW_WIDTH_CM - GAP_CM * (len(d) - 1)) / sum(d)     # cm per km
    rows, x = [], 0.0
    for p, dk in zip(PLANETS, d):
        dc = dk * scale
        rows.append((p, kind(p, led), int(dk), round(dc, 3), round(x + dc / 2, 3)))
        x += dc + GAP_CM
    return rows, scale


def distance_line(led=None, width_cm=ROW_WIDTH_CM, inner_factor=10.0):
    """Each planet's distance from the Sun on a line of width_cm (Neptune at
    the end), and on a line inner_factor times longer for the rocky planets."""
    led = led or ledger()
    far = value("Neptune", "dist", led)
    return [(p, value(p, "dist", led), round(width_cm * value(p, "dist", led) / far, 3),
             round(inner_factor * width_cm * value(p, "dist", led) / far, 3)) for p in PLANETS]


def scale_model(earth_cm=1.0, led=None):
    """[(name, diameter in cm, distance from the Sun in m)] for a model in which
    the Earth is earth_cm wide; the Sun first (distance 0)."""
    led = led or ledger()
    k = earth_cm / value("Earth", "diameter", led)          # cm per km
    path = os.path.join(ROOT, "sources", "data_ledger.md")
    r_sun = [float(l.split("|")[3]) for l in open(path, encoding="utf8") if l.startswith("| sun:R |")][0]
    rows = [("Sun", 2 * r_sun * k, 0.0)]
    rows += [(p, value(p, "diameter", led) * k, value(p, "dist", led) * 1e6 * k / 100.0) for p in PLANETS]
    return rows


if __name__ == "__main__":
    led = ledger()
    rows, scale = circles(led)
    write_table(__file__, ("name", "kind", "d_km", "d_cm", "x_cm"), rows, part="sizes")
    write_table(__file__, ("idx", "name", "kind", "density_gcm3"),
                [(i, p, kind(p, led), "%.2f" % density_gcm3(p, led)) for i, p in enumerate(PLANETS)],
                part="density")
    write_table(__file__, ("idx", "name", "dist_Mkm", "tmean_C"),
                [(i, p, "%.1f" % value(p, "dist", led), "%.0f" % value(p, "Tmean", led))
                 for i, p in enumerate(PLANETS)], part="temp")
    write_table(__file__, ("name", "psurf_bar", "tmean_C", "dist_Mkm", "water"),
                [(p, value(p, "psurf", led), "%.0f" % value(p, "Tmean", led), value(p, "dist", led), w)
                 for p, w in (("Venus", "no"), ("Earth", "yes"), ("Mars", "no"))], part="trio")
    write_table(__file__, ("name", "dist_Mkm", "x_cm", "x_inner_cm"), distance_line(led), part="dist")
    write_table(__file__, ("name", "d_cm", "dist_m"),
                [(n, "%.2f" % d, "%.0f" % m) for n, d, m in scale_model(led=led)], part="model")
    main = []
    for p in PLANETS:
        main.append((p, kind(p, led), int(value(p, "diameter", led)), "%.1f" % percent_of_earth(p, led=led),
                     "%.2f" % density_gcm3(p, led), "%.1f" % value(p, "dist", led),
                     "%.0f" % value(p, "Tmean", led)))
        print(main[-1])
    write_table(__file__, ("name", "kind", "d_km", "d_vs_earth_pct", "density_gcm3", "dist_Mkm", "tmean_C"),
                main)
    print("scale: 1 cm =", round(1 / scale), "km; the Sun would be", round(sun_cm(led), 1), "cm")
