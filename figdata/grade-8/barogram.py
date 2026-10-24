"""A barometer's record at a weather station as the weather map of grade 8,
chapter 3 drifts east (an invented situation, like the map itself).

The whole pressure field of figdata/grade-8/weather_map.py (anticyclone,
depression and its two fronts) is moved east at the cold front's speed of the
chapter's problem (SPEED_KMH, exercise data), and the pressure is read every
half hour at a station S east of the map's fronts, for 60 hours. The station
first sits under the anticyclone, then sees the pressure fall as the
depression comes, the warm front pass, the lowest pressure near the cold
front, and the pressure rise behind it. (The town of the chapter's problem
is a different place: its numbers are not used here.)

  part trace  : hour p_hPa
  part fronts : hour name p_hPa     (when each front passes the station)
  main table  : item value
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402
import weather_map as wm  # noqa: E402

STATION = (2300.0, 750.0)            # km on the map at the map hour
HOURS = 60.0


def p_at(h):
    """Pressure at the station h hours after the map, the field moved east."""
    return float(wm.pressure(STATION[0] - wm.SPEED_KMH * h, STATION[1]))


def trace(step=0.5):
    n = int(HOURS / step)
    return [(k * step, p_at(k * step)) for k in range(n + 1)]


def warm_front_x(y):
    line = wm.warm_front(n=400)
    for (x0, y0), (x1, y1) in zip(line, line[1:]):
        if (y0 - y) * (y1 - y) <= 0 and y0 != y1:
            return x0 + (x1 - x0) * (y - y0) / (y1 - y0)
    raise ValueError("warm front does not reach y")


def front_hours():
    """Hours at which the warm and the cold front pass the station."""
    y = STATION[1]
    return {"warm": (STATION[0] - warm_front_x(y)) / wm.SPEED_KMH,
            "cold": (STATION[0] - wm.front_x_at(y)) / wm.SPEED_KMH}


def summary():
    tr = trace()
    hi = max(tr, key=lambda r: r[1])
    lo = min(tr, key=lambda r: r[1])
    fh = front_hours()
    return {"max_hour": hi[0], "max_hPa": hi[1], "min_hour": lo[0], "min_hPa": lo[1],
            "warm_hour": fh["warm"], "cold_hour": fh["cold"], "fall_hPa": hi[1] - lo[1],
            "end_hPa": tr[-1][1]}


if __name__ == "__main__":
    write_table(__file__, ("hour", "p_hPa"), [(h, round(p, 2)) for h, p in trace()], part="trace")
    fh = front_hours()
    write_table(__file__, ("hour", "name", "p_hPa"),
                [(round(h, 2), n, round(p_at(h), 2)) for n, h in sorted(fh.items(), key=lambda kv: kv[1])],
                part="fronts")
    s = summary()
    write_table(__file__, ("item", "value"), [(k, round(v, 2)) for k, v in s.items()])
    for k, v in s.items():
        print(k, round(v, 2))
