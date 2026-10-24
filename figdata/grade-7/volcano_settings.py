"""Where the volcanoes are (grade 7, volcanoes).

The Smithsonian Global Volcanism Program's list of Holocene volcanoes
(data/derived/gvp-holocene.csv, ledger data:gvp) gives each volcano a
tectonic setting such as "Subduction zone / Continental crust (> 25 km)". The
first half is kept and printed in plain words:

  Subduction zone -> where one plate sinks under another
  Rift zone       -> where plates move apart
  Intraplate      -> inside a plate, far from its edges
  (blank)         -> not known

  main table      : idx key label n pct              (counts, all volcanoes)
  part map-<key>  : lon lat                      (one table per setting)
  part types      : key n strato shield other    (cone shapes per setting)
  part strato     : n_strato n_strato_sub pct    (share of steep cones above sinking plates)
"""
import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GVP = os.path.join(ROOT, "data", "derived", "gvp-holocene.csv")

SETTINGS = (
    ("sub", "Subduction zone", "where one plate sinks under another"),
    ("rift", "Rift zone", "where plates move apart"),
    ("intra", "Intraplate", "inside a plate"),
    ("unknown", "", "not known"),
)


def rows():
    with open(GVP, encoding="utf8") as f:
        return list(csv.DictReader(f))


def setting_key(row):
    first = row["setting"].split(" / ")[0].strip()
    for key, name, _ in SETTINGS:
        if first == name:
            return key
    raise ValueError("unexpected setting %r" % row["setting"])


def shape(row):
    """'strato' (steep cone of lava and ash layers), 'shield' (broad, gentle
    cone) or 'other' (fields of small cones, calderas, domes, submarine...)."""
    t = row["type"]
    if t.startswith("Stratovolcano"):
        return "strato"
    if t.startswith("Shield"):
        return "shield"
    return "other"


def counts(data=None):
    """[(key, label, n, percent of all volcanoes)] in SETTINGS order."""
    data = data or rows()
    n = {k: 0 for k, _, _ in SETTINGS}
    for r in data:
        n[setting_key(r)] += 1
    total = len(data)
    return [(k, lab, n[k], 100.0 * n[k] / total) for k, _, lab in SETTINGS]


def types_by_setting(data=None):
    data = data or rows()
    out = {k: {"strato": 0, "shield": 0, "other": 0} for k, _, _ in SETTINGS}
    for r in data:
        out[setting_key(r)][shape(r)] += 1
    return out


def strato_share(data=None):
    """(all steep cones, those above a sinking plate, percent)."""
    t = types_by_setting(data)
    n = sum(v["strato"] for v in t.values())
    return n, t["sub"]["strato"], 100.0 * t["sub"]["strato"] / n


if __name__ == "__main__":
    data = rows()
    write_table(__file__, ("idx", "key", "label", "n", "pct"),
                [(i, k, "{%s}" % lab, n, round(p, 1)) for i, (k, lab, n, p) in enumerate(counts(data))])
    for key, _, _ in SETTINGS[:3]:
        write_table(__file__, ("lon", "lat"),
                    [(float(r["lon"]), float(r["lat"])) for r in data if setting_key(r) == key],
                    part="map-" + key)
    t = types_by_setting(data)
    write_table(__file__, ("key", "n", "strato", "shield", "other"),
                [(k, sum(t[k].values()), t[k]["strato"], t[k]["shield"], t[k]["other"]) for k, _, _ in SETTINGS],
                part="types")
    n, ns, p = strato_share(data)
    write_table(__file__, ("n_strato", "n_strato_sub", "pct"), [(n, ns, round(p, 1))], part="strato")
