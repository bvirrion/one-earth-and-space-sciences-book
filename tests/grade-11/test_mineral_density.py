"""figdata/grade-11/mineral_density.py: crust elements and rock densities."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import mineral_density as md  # noqa: E402


def test_oxide_masses_and_pure_silica():
    assert abs(md.oxide_mass("SiO2") - 60.083) < 0.01
    f = md.element_fractions({"SiO2": 100.0})
    assert abs(f["Si"] - 46.74) < 0.02 and abs(f["O"] - 53.26) < 0.02   # webmineral quartz


def test_fractions_sum_to_100_and_oxygen_silicon_three_quarters():
    f = md.element_fractions(md.BULK)
    assert abs(sum(f.values()) - 100.0) < 1e-9
    assert 45 < f["O"] < 48 and 27 < f["Si"] < 30
    assert 73 < f["O"] + f["Si"] < 77
    order = sorted(f, key=lambda k: -f[k])
    assert order[:4] == ["O", "Si", "Al", "Fe"]


def test_rock_density_is_the_volume_weighted_mean():
    assert abs(md.rock_density({"quartz": 1.0}) - 2.62) < 1e-12
    half = md.rock_density({"quartz": 0.5, "olivine": 0.5})
    assert abs(half - (2.62 + 3.32) / 2) < 1e-12


def test_example_rocks():
    n = md.numbers()
    assert abs(n["rho_granite"] - 2.64) < 0.005
    assert 2.95 < n["rho_basalt"] < 3.05 and 3.25 < n["rho_peridotite"] < 3.4
    # granite lighter than the measured mean of granitic plutons (2.69), heavier than 2.6
    assert 2.6 < n["rho_granite"] < 2.69


def test_point_count():
    fr = md.from_count(md.GRANITE_COUNT)
    assert sum(md.GRANITE_COUNT.values()) == 500 and abs(sum(fr.values()) - 1) < 1e-12
    assert abs(fr["quartz"] - 0.30) < 1e-12


def test_density_order_light_silica_rich_heavy_iron_magnesium():
    order = md.density_order()
    assert order[0] == "orthoclase" and order[-1] == "augite"
    light = {"quartz", "orthoclase", "oligoclase", "labradorite"}
    heavy = {"olivine", "augite", "hornblende", "biotite"}
    assert max(md.MINERALS[m][1] for m in light) < min(md.MINERALS[m][1] for m in heavy)
