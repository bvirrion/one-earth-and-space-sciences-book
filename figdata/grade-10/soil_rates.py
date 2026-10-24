"""Soil production against erosion, the lifetime of a ploughed soil, and the mass
balance of the hydrolysis of orthoclase (grade 10, soil-formation).

Sources (ledger): Montgomery (2007) Table 1 medians and the critical time
Tc = S / (E - P) (montgomery:rates, montgomery:lifetime); molar masses and the
potassium content of orthoclase, 14.05 % (webmineral:formulas).

  part rates    idx rate_mm_yr     medians (order of RATES) of the global compilation (log-scale bars)
  part numbers  key value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

RATES = (  # montgomery:rates, Table 1 medians, mm/yr
    ("soil production", 0.017),
    ("native vegetation", 0.013),
    ("geological erosion", 0.029),
    ("conservation agriculture", 0.082),
    ("conventional agriculture", 1.537),
)
M_ORTHOCLASE, M_KAOLINITE = 278.33, 258.16     # g/mol, webmineral:formulas
K_FRACTION_ORTHOCLASE = 0.1405                 # webmineral:formulas


def lifetime(thickness_mm, erosion, production):
    """Critical time (years) to erode through a soil profile: S / (E - P)."""
    return thickness_mm / (erosion - production)


def formation_time(thickness_mm, production):
    return thickness_mm / production


def hydrolysis_kaolinite_per_kg():
    """2 KAlSi3O8 + 2 H+ + 9 H2O -> Al2Si2O5(OH)4 + 2 K+ + 4 H4SiO4:
    grams of kaolinite formed from 1 kg of orthoclase."""
    return 1000.0 / M_ORTHOCLASE / 2.0 * M_KAOLINITE


def numbers():
    r = dict(RATES)
    e, p = r["conventional agriculture"], r["soil production"]
    n = {
        "ratio_conv_to_production": e / p,
        "ratio_conv_to_native": e / r["native vegetation"],
        "ratio_conservation_to_production": r["conservation agriculture"] / p,
        "net_loss_conv_mm_yr": e - p,
        "lifetime_1m_conv_yr": lifetime(1000, e, p),
        "lifetime_30cm_conv_yr": lifetime(300, e, p),
        "lifetime_1m_conservation_yr": lifetime(1000, r["conservation agriculture"], p),
        "form_1m_yr": formation_time(1000, p),
        "form_30cm_yr": formation_time(300, p),
        "form_1cm_yr": formation_time(10, p),
        "loss_1cm_conv_yr": 10 / e,
        "kaolinite_g_per_kg_orthoclase": hydrolysis_kaolinite_per_kg(),
        "potassium_g_per_kg_orthoclase": 1000 * K_FRACTION_ORTHOCLASE,
        "mol_orthoclase_per_kg": 1000.0 / M_ORTHOCLASE,
        "mol_silicic_per_kg": 1000.0 / M_ORTHOCLASE * 2.0,
        "loss_t_per_ha_conv": e / 1000 * 10000 * 1200 / 1000,   # mm/yr -> t/ha/yr at 1200 kg/m3
    }
    return n


if __name__ == "__main__":
    write_table(__file__, ("idx", "rate_mm_yr"), [(i, b) for i, (_, b) in enumerate(RATES)], part="rates", digits=4)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=6)
