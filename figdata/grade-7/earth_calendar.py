"""The Earth's history squeezed into one calendar year (grade 7, the ages of
the Earth).

The year (365 days, no leap day) runs from the Earth's formation, 1 January at
midnight, to today, 31 December at midnight. The age of the Earth is the
U.S. Geological Survey's 4.54 billion years (ledger usgs:age-earth). Events
and their ages, in millions of years (Ma):

  oldest rocks found           4030    usgs:age-earth (Acasta gneisses, 4.03 Ga)
  oldest known fossils         3500    usgs:numeric-scale ("about 3.5 billion years")
  shells become common         538.8   ics:base.Cambrian (start of the Paleozoic)
  the dinosaurs are gone       66.00   ics:base.Paleogene (end of the Cretaceous)
  our species, Homo sapiens    0.3     hublin:jebel-irhoud (315 +- 34 ka, "about 300 000 years")

  main table  : idx label age_ma day month date hh mm tag   (one row per event;
                tag = "date: label" for the figure)
  part days   : day                                     (one tick per month start)
  part months : mid name                                (the middle of each month,
                                                         its short name)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

AGE_EARTH_MA = 4540.0
DAYS = 365
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December")
MONTH_DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
EVENTS = (
    ("{the Earth forms}", 4540.0),
    ("{oldest rocks found}", 4030.0),
    ("{oldest known fossils}", 3500.0),
    ("{shells become common}", 538.8),
    ("{the dinosaurs are gone}", 66.0),
)
HOMO_SAPIENS_MA = 0.3


def elapsed_days(age_ma, total=AGE_EARTH_MA):
    """Days from 1 January 00:00 to the moment of the event."""
    return DAYS * (1.0 - age_ma / total)


def calendar(age_ma, total=AGE_EARTH_MA):
    """(month name, date, hour, minute) of an event of the given age."""
    d = elapsed_days(age_ma, total)
    day = int(d)
    minutes = int(round((d - day) * 24 * 60))
    if minutes == 24 * 60:
        day, minutes = day + 1, 0
    m = 0
    while day >= MONTH_DAYS[m]:
        day -= MONTH_DAYS[m]
        m += 1
    return MONTHS[m], day + 1, minutes // 60, minutes % 60


def tag(label, age_ma, total=AGE_EARTH_MA):
    """The figure's label: '{11 February: oldest rocks found}'."""
    month, date, _, _ = calendar(age_ma, total)
    return "{%d %s: %s}" % (date, month, label.strip("{}"))


def myr_per_day(total=AGE_EARTH_MA):
    return total / DAYS


def minutes_before_midnight(age_ma, total=AGE_EARTH_MA):
    return age_ma / total * DAYS * 24 * 60


if __name__ == "__main__":
    rows = []
    for i, (label, age) in enumerate(EVENTS):
        month, date, hh, mm = calendar(age)
        rows.append((i, label, age, round(elapsed_days(age), 2), month, date, hh, mm, tag(label, age)))
    write_table(__file__, ("idx", "label", "age_ma", "day", "month", "date", "hh", "mm", "tag"), rows)
    starts, mids, d = [], [], 0
    for name, n in zip(MONTHS, MONTH_DAYS):
        starts.append((d,))
        mids.append((d + n / 2.0, name[:3]))
        d += n
    starts.append((d,))
    write_table(__file__, ("day",), starts, part="days")
    write_table(__file__, ("mid", "name"), mids, part="months")
