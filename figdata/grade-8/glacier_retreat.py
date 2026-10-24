"""Glacier G: an invented valley glacier retreating, for the weekend problem of
grade 8, chapter 5 (ice on Earth). Exercise data, not a real glacier.

Positions of the glacier front, measured up the valley from a rock marker R
that stood at the front in 1960, every ten years. A hut H stands beside the
valley floor DIST_HUT metres up the valley from R. At the average speed of
1960--2020, the year the front would be level with the hut follows (the
problem warns that a past rate is not a forecast).

Map view, metres: x across the valley (0 on its axis), y up the valley.
The front is drawn as an arc bulging down the valley (a glacier tongue).

  part fronts  : x y   (one arc per year, separated by blank lines)
  part labels  : x y year
  part walls   : x y   (the two valley sides, separated by a blank line)
  part moraine : x y   (the ridge just down-valley of the 1960 front)
  part floor   : x y   (the valley floor between the two sides, closed)
  part ice     : x y   (the glacier in 2020, closed)
  main table   : item value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

POSITIONS = [(1960, 0), (1970, 180), (1980, 330), (1990, 520), (2000, 700), (2010, 880), (2020, 1080)]
DIST_HUT = 1980          # m up the valley from R
HALF_WIDTH = 450.0       # m, half the width of the valley floor at the ice
BULGE = 160.0            # m, how far the middle of the tongue reaches beyond its sides
LABEL_X = 220.0          # m across the valley where the year labels sit, just below each front
MORAINE_GAP = 110.0      # m between the 1960 front and the crest of its moraine


def retreat_per_decade():
    return [(y1, p1 - p0) for (y0, p0), (y1, p1) in zip(POSITIONS, POSITIONS[1:])]


def average_rate():
    """Metres per year, first to last measurement."""
    (y0, p0), (y1, p1) = POSITIONS[0], POSITIONS[-1]
    return (p1 - p0) / (y1 - y0)


def year_at_hut():
    y1, p1 = POSITIONS[-1]
    return y1 + (DIST_HUT - p1) / average_rate()


def arc(d, n=24):
    """Front at distance d: the middle of the tongue reaches d, the sides d + BULGE."""
    pts = []
    for k in range(n + 1):
        x = -HALF_WIDTH + 2 * HALF_WIDTH * k / n
        pts.append((x, d + BULGE * (x / HALF_WIDTH) ** 2))
    return pts


def floor():
    return wall(-1) + wall(1)[::-1]


def ice(d):
    """The glacier above the front at distance d, up to the top of the map."""
    top = 2600.0
    return arc(d) + [(HALF_WIDTH, top), (-HALF_WIDTH, top)]


def wall(side):
    """Valley side: a gentle curve, widening down the valley."""
    return [(side * (HALF_WIDTH + 40 + 0.06 * (2600 - y)), y) for y in range(-500, 2601, 100)]


if __name__ == "__main__":
    rows = []
    for _y, d in POSITIONS:
        rows += [(round(x, 1), round(y, 1)) for x, y in arc(d)] + [("", "")]
    write_table(__file__, ("x", "y"), rows[:-1], part="fronts")
    write_table(__file__, ("x", "y", "year"), [(LABEL_X, round(d + BULGE * (LABEL_X / HALF_WIDTH) ** 2 - 12, 1), y)
                                                for y, d in POSITIONS], part="labels")
    write_table(__file__, ("x", "y"), wall(-1) + [("", "")] + wall(1), part="walls")
    write_table(__file__, ("x", "y"), [(round(x, 1), round(y - MORAINE_GAP, 1)) for x, y in arc(0)], part="moraine")
    write_table(__file__, ("x", "y"), floor(), part="floor")
    write_table(__file__, ("x", "y"), [(round(x, 1), round(y, 1)) for x, y in ice(POSITIONS[-1][1])], part="ice")
    rows = [("retreat_%d" % y, r) for y, r in retreat_per_decade()]
    rows += [("total_m", POSITIONS[-1][1] - POSITIONS[0][1]), ("rate_m_per_year", average_rate()),
             ("rate_m_per_decade", 10 * average_rate()), ("left_to_hut_m", DIST_HUT - POSITIONS[-1][1]),
             ("year_at_hut", round(year_at_hut(), 1))]
    write_table(__file__, ("item", "value"), rows)
    for r in rows:
        print(r)
