"""The Phanerozoic part of the international chart (Year 1, stratigraphic-scale).

Every base age and colour is read from the shared data ledger
(sources/data_ledger.md, rows ics:base.<unit> and ics:colour.<unit>, from the
International Chronostratigraphic Chart, source ICS-2026-06), so that the chart of
the chapter cannot drift from the ledger. The base ages are printed as the ledger
writes them (66.00, 251.902, ...), uncertainties dropped. The two boundaries that
are mass-extinction horizons (base of the Mesozoic, ledger burgess:end-permian;
base of the Cenozoic, ledger alvarez:iridium, renne:kpg) are marked.

  part eras         x age name              (label at the middle of each era)
  part periods      x age name              (label at the middle of each period)
  part bases        x age lab               (base age of each period, as printed)
  part bar-<unit>   x age                   (closed rectangle, era column x 0-1,
                                             period column x 1-3)
  part events       x age name              (the two extinction horizons)
  part values       what value
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
LEDGER = os.path.join(ROOT, "sources", "data_ledger.md")
STY = os.path.join(ROOT, "styles", "oneearth.sty")

ERAS = ("Paleozoic", "Mesozoic", "Cenozoic")
PERIODS = ("Cambrian", "Ordovician", "Silurian", "Devonian", "Carboniferous", "Permian",
           "Triassic", "Jurassic", "Cretaceous", "Paleogene", "Neogene", "Quaternary")
EXTINCTIONS = (("Mesozoic", "end-Permian"), ("Cenozoic", "end-Cretaceous"))  # bases at extinctions
X_ERA = (0.0, 1.0)
X_PERIOD = (1.0, 3.0)


def ledger(path=LEDGER):
    """({unit: base age string as printed in the ledger}, {unit: colour hex})."""
    base, colour = {}, {}
    with open(path, encoding="utf8") as f:
        for line in f:
            m = re.match(r"\|\s*ics:base\.([A-Za-z]+)\s*\|[^|]*\|\s*([0-9]+(?:\.[0-9]+)?)", line)
            if m:
                base[m.group(1)] = m.group(2)
            m = re.match(r"\|\s*ics:colour\.([A-Za-z]+)\s*\|[^|]*\|\s*#([0-9A-Fa-f]{6})", line)
            if m:
                colour[m.group(1)] = m.group(2).upper()
    return base, colour


def sty_colours(path=STY):
    """{unit: hex} of the \\definecolor{ics<Unit>}{HTML}{...} lines of the style file."""
    out = {}
    with open(path, encoding="utf8") as f:
        for line in f:
            m = re.match(r"\\definecolor\{ics([A-Za-z]+)\}\{HTML\}\{([0-9A-Fa-f]{6})\}", line.strip())
            if m:
                out[m.group(1)] = m.group(2).upper()
    return out


def spans(names, base):
    """[(name, start, end)] in Ma: each unit ends where the next begins, the last today."""
    out = []
    for i, n in enumerate(names):
        end = float(base[names[i + 1]]) if i + 1 < len(names) else 0.0
        out.append((n, float(base[n]), end))
    return out


def ring(x, start, end):
    return [(x[0], start), (x[1], start), (x[1], end), (x[0], end), (x[0], start)]


def durations(base):
    return {n: s - e for n, s, e in spans(PERIODS, base)}


if __name__ == "__main__":
    base, colour = ledger()
    ep, pp = spans(ERAS, base), spans(PERIODS, base)
    write_table(__file__, ("x", "age", "name"),
                [(sum(X_ERA) / 2, (s + e) / 2, n) for n, s, e in ep], part="eras")
    # the Quaternary is too thin for a label inside its box: it is labelled in the figure
    write_table(__file__, ("x", "age", "name"),
                [(sum(X_PERIOD) / 2, (s + e) / 2, n) for n, s, e in pp if n != "Quaternary"],
                part="periods")
    write_table(__file__, ("x", "age", "lab"),
                [(X_PERIOD[1], float(base[n]), base[n]) for n in PERIODS], part="bases")
    for n, s, e in ep:
        write_table(__file__, ("x", "age"), ring(X_ERA, s, e), part="bar-" + n)
    for n, s, e in pp:
        write_table(__file__, ("x", "age"), ring(X_PERIOD, s, e), part="bar-" + n)
    write_table(__file__, ("x", "age", "name"),
                [(X_PERIOD[1], float(base[n]), lab) for n, lab in EXTINCTIONS], part="events")
    d = durations(base)
    longest = max(d, key=d.get)
    pre_q = {k: v for k, v in d.items() if k != "Quaternary"}
    shortest = min(pre_q, key=pre_q.get)
    vals = [("phanerozoic_myr", float(base["Phanerozoic"])),
            ("longest_period_" + longest, d[longest]),
            ("shortest_period_before_quaternary_" + shortest, d[shortest]),
            ("quaternary_myr", d["Quaternary"]),
            ("mean_period_myr", sum(d.values()) / len(d)),
            ("paleozoic_myr", float(base["Paleozoic"]) - float(base["Mesozoic"])),
            ("mesozoic_myr", float(base["Mesozoic"]) - float(base["Cenozoic"]))]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)
