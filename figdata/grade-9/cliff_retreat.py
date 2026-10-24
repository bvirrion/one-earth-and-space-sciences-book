"""Landforms, grade 9, chapter 4: the weekend problem "The cliff and the coast
road" and one computed rate of the course text.

The survey (exercise data): a survey team measures, every few years, the
distance from the seaward edge of a coast road to the edge of a chalk cliff,
along the same line, from fixed markers set well back from the edge. The
retreat comes in jumps (a storm winter between 2012 and 2014 takes a large
bite), as on the real chalk coast of Birling Gap (ledger nt:birling-2014,
sdnp:birling: up to about one metre a year), but the numbers are invented.

The course text's net-rise example: the Tibetan Plateau, about 4600 m high,
gained most of its height in the last 10 million years (ledger
usgs:himalaya): 4600 m / 10 Myr, in millimetres a year.

  main table   : year dist_m            (the survey points)
  part problem : item value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

# year of the survey: distance from the cliff edge to the road, in metres
SURVEY = [
    (2004, 46.0),
    (2008, 43.1),
    (2012, 41.0),
    (2014, 36.2),
    (2016, 35.5),
    (2020, 33.0),
    (2024, 30.4),
]
SAFETY_MARGIN_M = 10.0          # the road is moved before the edge comes this close
STORM_FACTOR = 2.0              # "if storms doubled the rate"
LIGHTHOUSE_MOVE_M = 17.0        # Belle Tout moved 17 m back in 1999 (sdnp:birling)

TIBET_HEIGHT_M = 4600.0         # usgs:himalaya
TIBET_TIME_YR = 10e6            # usgs:himalaya, most of the uplift in 10 Myr


def tibet_rate_mm_yr():
    return TIBET_HEIGHT_M * 1000.0 / TIBET_TIME_YR


def intervals():
    """(start, end, retreat m, rate m/yr) for each pair of successive surveys."""
    out = []
    for (y0, d0), (y1, d1) in zip(SURVEY, SURVEY[1:]):
        out.append((y0, y1, round(d0 - d1, 3), (d0 - d1) / (y1 - y0)))
    return out


def average_rate():
    (y0, d0), (y1, d1) = SURVEY[0], SURVEY[-1]
    return (d0 - d1) / (y1 - y0)


def year_reached(distance_left_m, rate):
    """Calendar year (rounded to the nearest) when distance_left_m more is lost."""
    return SURVEY[-1][0] + distance_left_m / rate


def problem():
    p = {}
    (y0, d0), (y1, d1) = SURVEY[0], SURVEY[-1]
    p["total_retreat_m"] = d0 - d1
    p["span_yr"] = y1 - y0
    p["rate_m_yr"] = average_rate()
    fast = max(intervals(), key=lambda t: t[3])
    p["fast_start"], p["fast_end"], p["fast_retreat_m"], p["fast_rate_m_yr"] = fast
    p["fast_ratio"] = fast[3] / p["rate_m_yr"]
    p["rate_cm_yr"] = p["rate_m_yr"] * 100
    p["rate_m_century"] = p["rate_m_yr"] * 100
    p["lighthouse_years"] = LIGHTHOUSE_MOVE_M / p["rate_m_yr"]
    p["margin_years"] = (d1 - SAFETY_MARGIN_M) / p["rate_m_yr"]
    p["margin_year"] = year_reached(d1 - SAFETY_MARGIN_M, p["rate_m_yr"])
    p["storm_years"] = d1 / (STORM_FACTOR * p["rate_m_yr"])
    p["storm_year"] = year_reached(d1, STORM_FACTOR * p["rate_m_yr"])
    p["road_years"] = d1 / p["rate_m_yr"]
    p["road_year"] = year_reached(d1, p["rate_m_yr"])
    return p


if __name__ == "__main__":
    write_table(__file__, ("year", "dist_m"), SURVEY)
    p = problem()
    write_table(__file__, ("item", "value"), [(k, round(v, 3)) for k, v in p.items()], part="problem")
    for t in intervals():
        print("%d-%d  %.1f m  %.2f m/yr" % t)
    for k, v in p.items():
        print(k, round(v, 3))
    print("tibet mm/yr", tibet_rate_mm_yr())
