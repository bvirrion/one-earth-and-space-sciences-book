"""Tests for the synthetic Varden-2 logs (Year 3, ch. 17)."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import well_logs as wl  # noqa: E402


def test_tops_follow_the_region_model_thicknesses():
    t = wl.tops()
    assert t["limestone"] - t["shale"] == pytest.approx(100.0, abs=0.01)
    assert t["sandstone"] - t["limestone"] == pytest.approx(180.0, abs=0.01)
    assert t["schist"] - t["sandstone"] == pytest.approx(120.0, abs=0.01)
    assert 0 < t["shale"] < t["schist"] < wl.TD


def test_column_is_unfaulted_at_the_site():
    x, y = wl.SITE
    t = wl.tops()
    g = wl.region.topo(x, y)
    for d in range(1, int(t["schist"]), 5):
        assert not wl.region.hanging_wall(x, y, g - d)


def test_channels_fill_the_sandstone():
    assert sum(c[0] for c in wl.CHANNELS) == pytest.approx(120.0)
    assert all(fs + ff < 1 for _, fs, ff in wl.CHANNELS)


def test_density_porosity_inverts_density():
    for phi in (0.05, 0.2, 0.35):
        for m in ("quartz", "calcite"):
            assert wl.porosity(wl.density(phi, m), m) == pytest.approx(phi)


def test_time_average_limits():
    assert wl.transit(0.0, "sandstone") == pytest.approx(52.6)
    assert wl.transit(1.0, "limestone") == pytest.approx(189.0)


def test_net_sand_matches_the_channel_geometry():
    frac = (wl.GR_CUT - wl.GR_SAND) / (wl.GR_MUD - wl.GR_SAND)
    expect = sum(th * (fs + frac * ff) for th, fs, ff in wl.CHANNELS)
    net, gross = wl.net_sand()
    assert net == pytest.approx(expect, abs=0.05)
    assert gross == pytest.approx(120.0, abs=0.01)


def test_each_channel_fines_upward():
    t = wl.tops()
    h0 = 0.0
    for th, fs, ff in wl.CHANNELS:
        grs = [wl.logs_at(t["schist"] - (h0 + th * u), t)[0] for u in (0.05, fs + ff / 2, 0.98)]
        assert grs[0] < grs[1] < grs[2]
        h0 += th


def test_shale_reads_hot_and_carbonates_cold():
    t = wl.tops()
    gr_sh = wl.logs_at(t["shale"] + 50, t)[0]
    gr_ls = wl.logs_at(t["limestone"] + 50, t)[0]
    gr_ch = wl.logs_at(100, t)[0]
    assert gr_sh > 3 * max(gr_ls, gr_ch)
