"""Tests for the erosion-transport figure data: settling velocity (Stokes and the
combined law), the threshold of motion (Soulsby and Whitehouse), the depth-slope
product, Keulegan's mean-velocity law and the suspension limit (u* = w_s) of the
Hjulstrom-type diagram."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import settling as st  # noqa: E402
import threshold as th  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
LEDGER = os.path.join(ROOT, "sources", "ledger", "book3.md")


def ledger_row(row_id):
    with open(LEDGER, encoding="utf8") as f:
        for line in f:
            if line.startswith("| %s |" % row_id):
                return line
    raise KeyError(row_id)


def test_constants_equal_the_ledger():
    row = ledger_row("nist:water")
    assert "1.0016" in row and "998.207" in row
    assert abs(st.MU - 1.0016e-3) < 1e-12
    assert st.RHO_W == 998.207
    assert "2.65" in ledger_row("hom:quartz") and st.RHO_Q == 2650.0
    row = ledger_row("hecras:thresholds")
    for c in ("0.3", "1.2", "0.055", "0.02"):
        assert c in row
    row = ledger_row("keulegan:mean-velocity")
    assert "6.25 + 5.75 log10(R/k_s)" in row
    assert "18 and 1.0" in ledger_row("fc:settling")


def test_stokes_value_and_validity_limit():
    # R g d^2 / (18 nu) for 10 micrometres
    d = 10e-6
    assert abs(st.stokes(d) - st.R_Q * st.G * d * d / (18 * st.NU)) < 1e-15
    assert abs(st.stokes(d) - 8.99e-5) < 0.01e-5
    dl = st.stokes_limit_diameter()
    assert abs(st.reynolds(dl, st.stokes(dl)) - 1.0) < 1e-9
    assert 0.10e-3 < dl < 0.11e-3


def test_combined_law_agrees_with_stokes_for_fine_grains_and_is_slower_for_coarse():
    for d in (1e-6, 2e-6, 4e-6, 10e-6):
        assert abs(st.ferguson_church(d) / st.stokes(d) - 1) < 0.01
    for d in (1e-4, 1e-3, 1e-2):
        assert st.ferguson_church(d) < st.stokes(d)
    # monotonic in grain size
    ds = st.log_grid(1e-6, 1e-2, 50)
    ws = [st.ferguson_church(d) for d in ds]
    assert all(b > a for a, b in zip(ws, ws[1:]))


def test_soulsby_curve():
    d = 1e-3
    D = th.dstar(d)
    expected = 0.3 / (1 + 1.2 * D) + 0.055 * (1 - math.exp(-0.02 * D))
    assert abs(th.theta_cr(d) - expected) < 1e-12
    assert abs(th.theta_cr(d) - 0.0314) < 0.0005
    assert abs(th.theta_cr(0.2) - 0.055) < 0.001          # coarse limit
    taus = [th.tau_cr(x * 1e-3) for x in st.log_grid(0.0625, 64.0, 60)]
    assert all(b > a for a, b in zip(taus, taus[1:]))


def test_depth_slope_product_and_threshold_velocity():
    assert abs(th.bed_shear(2.0, 1e-3) - st.RHO_W * st.G * 2.0e-3) < 1e-12
    d, h = 1e-3, 1.0
    ustar = math.sqrt(th.tau_cr(d) / st.RHO_W)
    assert abs(th.u_cr(d, h) - (6.25 + 5.75 * math.log10(h / d)) * ustar) < 1e-9


def test_suspension_limit_is_ustar_equal_ws():
    us = 0.12
    d = th.suspended_limit(us)
    assert abs(st.ferguson_church(d) / us - 1.0) < 1e-6
    # fine grains go into suspension before they would start rolling coarse
    assert th.u_susp(0.01e-3) < th.u_cr(0.0625e-3)
