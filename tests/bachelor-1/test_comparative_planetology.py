"""Ch. 3 (comparative-planetology): plotted values equal their ledger rows,
and the equilibrium temperatures agree with the NASA black-body values."""
import os
import re
import sys

HERE = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1")
sys.path.insert(0, HERE)
import planet_table as P  # noqa: E402


def test_bodies_equal_ledger_rows():
    text = open(P.LEDGER, encoding="utf-8").read()
    for _, name, R, rho in P.bodies():
        d = re.search(r"^\| planet:%s\.diameter \|[^|]*\| ([^|]+) \|" % name, text, re.M).group(1)
        r = re.search(r"^\| planet:%s\.density \|[^|]*\| ([^|]+) \|" % name, text, re.M).group(1)
        assert R == float(d) / 2 and rho == float(r)


def test_equilibrium_temperatures_match_nasa():
    # NASA fact-sheet black-body temperatures: Moon 270.4, Mars 209.8, Venus 226.6 K
    nasa = {"Moon": 270.4, "Mars": 209.8, "Venus": 226.6}
    for _, n, teq, _ in P.temps():
        if n in nasa:
            assert abs(teq - nasa[n]) < 0.2
    earth = [t for _, n, t, _ in P.temps() if n == "Earth"][0]
    assert abs(earth - 254.0) < 1.5      # earth:Tbb 254.0 (NASA uses its own albedo rounding)


def test_greenhouse_signs():
    d = {n: ts - teq for _, n, teq, ts in P.temps()}
    assert d["Venus"] > 500 and 30 < d["Earth"] < 36 and 0 < d["Mars"] < 6 and d["Moon"] < 0
