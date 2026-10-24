"""The geological time scale in two bars (grade 7, the ages of the Earth).

All ages and colours are read from the shared data ledger
(sources/data_ledger.md, rows ics:base.<unit> and ics:colour.<unit>, from the
International Chronostratigraphic Chart), so the book and the ledger cannot
drift apart. Ages are in millions of years (Ma).

  part long    : name start end colour     (the whole history: Hadean,
                                            Archean, Proterozoic, then the
                                            last three eras together)
  part eras    : name start end colour     (Paleozoic, Mesozoic, Cenozoic)
  part periods : name start end colour     (Cambrian ... Quaternary)
  part bar-<name>    : age y   (one closed rectangle per unit, for a fill in
                                 its chart colour; y from 0 to 1, the figure
                                 scales it)
  part labels-<group>: age y name   (the middle of each unit, for its label;
                                     group long, eras, periods)
  main table   : quoted numbers (shares in per cent of the age of the Earth,
                 4540 million years: ledger usgs:age-earth; the chart itself
                 starts at the base of the Hadean, 4567 Ma)
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AGE_EARTH_MA = 4540.0
LONG = ("Hadean", "Archean", "Proterozoic", "Phanerozoic")
ERAS = ("Paleozoic", "Mesozoic", "Cenozoic")
PERIODS = ("Cambrian", "Ordovician", "Silurian", "Devonian", "Carboniferous", "Permian",
           "Triassic", "Jurassic", "Cretaceous", "Paleogene", "Neogene", "Quaternary")


def ledger():
    """({unit: base in Ma}, {unit: colour hex}) from the ics:* rows."""
    base, colour = {}, {}
    path = os.path.join(ROOT, "sources", "data_ledger.md")
    for line in open(path, encoding="utf8"):
        m = re.match(r"\|\s*ics:base\.([A-Za-z]+)\s*\|[^|]*\|\s*([0-9.]+)", line)
        if m:
            base[m.group(1)] = float(m.group(2))
        m = re.match(r"\|\s*ics:colour\.([A-Za-z]+)\s*\|[^|]*\|\s*#([0-9A-Fa-f]{6})", line)
        if m:
            colour[m.group(1)] = m.group(2).upper()
    return base, colour


def spans(names, base=None):
    """[(name, start, end)] for consecutive units: each ends where the next starts."""
    base = base or ledger()[0]
    out = []
    for i, n in enumerate(names):
        end = base[names[i + 1]] if i + 1 < len(names) else 0.0
        out.append((n, base[n], end))
    return out


def ring(start, end):
    """A closed rectangle from start to end (ages), y from 0 to 1."""
    return [(start, 0), (end, 0), (end, 1), (start, 1), (start, 0)]


def middle(start, end):
    return (start + end) / 2.0


def share(start, end, total=AGE_EARTH_MA):
    """Percentage of the Earth's history between two ages (start capped at the
    age of the Earth)."""
    return 100.0 * (min(start, total) - end) / total


if __name__ == "__main__":
    base, colour = ledger()
    for part, names in (("long", LONG), ("eras", ERAS), ("periods", PERIODS)):
        write_table(__file__, ("name", "start", "end", "colour"),
                    [(n, s, e, colour[n]) for n, s, e in spans(names, base)], part=part)
    for group, names in (("long", LONG), ("eras", ERAS), ("periods", PERIODS)):
        sp = spans(names, base)
        for n, st, en in sp:
            write_table(__file__, ("age", "y"), ring(st, en), part="bar-" + n)
        write_table(__file__, ("age", "y", "name"), [(middle(st, en), 0.5, n) for n, st, en in sp],
                    part="labels-" + group)
    write_table(__file__, ("item", "value"), [
        ("before_paleozoic_pct", round(share(base["Hadean"], base["Paleozoic"]), 1)),
        ("cenozoic_pct", round(share(base["Cenozoic"], 0.0), 1)),
        ("mesozoic_myr", round(base["Mesozoic"] - base["Cenozoic"], 1)),
    ])
