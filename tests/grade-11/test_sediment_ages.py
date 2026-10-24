"""figdata/grade-11/sediment_ages.py: the DSDP Leg 3 table and its spreading rate."""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import sediment_ages as sd  # noqa: E402

LEDGER = os.path.join(os.path.dirname(__file__), "..", "..", "sources", "ledger", "book2.md")


def test_table_matches_the_ledger_row():
    with open(LEDGER, encoding="utf8") as f:
        line = next(l for l in f if l.startswith("| dsdp3:table5 |"))
    for site, (_, _, age, age_err, dist, dist_err) in sd.TABLE5.items():
        m = re.search(r"\b%d: [^;]*?, (\d+) \+- ([\d.]+), (\d+) \+- (\d+)" % site, line)
        assert m, site
        assert (float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))) == \
            (age, age_err, dist, dist_err)


def test_rate_is_slightly_less_than_2_cm_per_year():
    # published: 'slightly less than 2 cm/yr' for the nearest-axis distances
    u = sd.rate_through_origin(sd.palaeo_pairs())
    assert 1.8 < u < 2.0
    assert 1.7 < sd.rate_through_origin(sd.magnetic_pairs()) < 2.0


def test_fit_through_origin_is_exact_on_a_line():
    assert abs(sd.rate_through_origin([(20.0, 1.0), (200.0, 10.0)]) - 2.0) < 1e-12
