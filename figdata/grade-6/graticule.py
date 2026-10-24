"""A globe with its parallels and meridians (grade 6, latitude-longitude).

Reuses the orthographic projection and land clipping of
figdata/grade-3/globe.py (Natural Earth land, ledger data:ne-land). View centre
lon 10 E, lat 25 N, so that the equator, the prime meridian and the North Pole
are all in sight.

  part land      : x y  land rings (blank line between rings)
  part parallels : x y  every 30 deg (60 S ... 60 N), equator excluded
  part equator   : x y
  part meridians : x y  every 30 deg, prime meridian excluded
  part prime     : x y  the prime meridian (visible half)
  part marks     : name x y  (the North Pole, the point at 30 N 60 E used in the text)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "grade-3"))
from _table import write_table  # noqa: E402
import globe  # noqa: E402

VIEW = (10.0, 25.0)


def meridian(lon, view=VIEW, step=2.0):
    seg, segs = [], []
    for k in range(int(180 / step) + 1):
        x, y, d = globe.project(globe.xyz(lon, -90 + k * step), view)
        if d >= 0:
            seg.append((x, y))
        elif seg:
            segs.append(seg); seg = []
    if seg:
        segs.append(seg)
    return segs


def point(lon, lat, view=VIEW):
    return globe.project(globe.xyz(lon, lat), view)


def _rows(segs):
    rows = []
    for s in segs:
        rows += ([()] if rows else []) + [(round(x, 4), round(y, 4)) for x, y in s]
    return rows


if __name__ == "__main__":
    rows = []
    for p in globe.land(VIEW):
        rows += ([()] if rows else []) + [(round(x, 4), round(y, 4)) for x, y in p]
    write_table(__file__, ("x", "y"), rows, part="land")
    write_table(__file__, ("x", "y"), _rows([s for la in (-60, -30, 30, 60) for s in globe.parallel(la, VIEW)]),
                part="parallels")
    write_table(__file__, ("x", "y"), _rows(globe.parallel(0.0, VIEW)), part="equator")
    write_table(__file__, ("x", "y"), _rows([s for lo in range(-180, 180, 30) if lo != 0 for s in meridian(lo)]),
                part="meridians")
    write_table(__file__, ("x", "y"), _rows(meridian(0.0)), part="prime")
    marks = []
    for name, lo, la in (("N", 0.0, 90.0), ("P", 60.0, 30.0)):
        x, y, d = point(lo, la)
        marks.append((name, round(x, 4), round(y, 4)))
    write_table(__file__, ("name", "x", "y"), marks, part="marks")
