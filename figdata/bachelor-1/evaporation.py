"""The evaporation of seawater (Year 1, chemical-biogenic-sediments).

Composition. The Reference Composition of seawater (Millero et al. 2008, as
tabulated in the TEOS-10 manual, Table D.3; ledger teos10:reference-composition):
the mass fraction W_j of each solute in sea salt and its molar mass M_j, for a
Reference Salinity S_R = 35.16504 g of salt per kg of seawater
(teos10:reference-salinity).

Thresholds. The concentration factors (brine concentration / seawater
concentration) at which each mineral begins to precipitate, measured in the
salt ponds of Great Inagua and in the laboratory by McCaffrey, Lazar and Holland
(1987; ledger mccaffrey:thresholds): calcium carbonate 1.8, gypsum 3.8, halite
10.6, magnesium sulfate about 70, potassium salts above 90. The fraction of the
water left at each onset is 1/CF (the salt removed before is a negligible part
of the mass).

Masses. An idealised evaporation to dryness in a closed system, each mineral
taking all of the ion that limits it, in the order of the sequence:

  * calcium carbonate takes the carbonate alkalinity:
        Ca2+ + 2 HCO3-  -> CaCO3 + CO2 + H2O   and   Ca2+ + CO3^2- -> CaCO3,
    so n(CaCO3) = n(CO3) + n(HCO3)/2;
  * gypsum CaSO4.2H2O takes the rest of the calcium (sulfate is in excess);
  * halite NaCl takes all the sodium (chloride is in excess);
  * the bittern salts (Mg and K sulfates and chlorides) take what is left; their
    anhydrous mass is the salinity minus the ions already used.

  part curve    CF f_left                         (CF from 1 to 100, log-spaced)
  part steps    mineral CF f_left                (onsets)
  part masses   mineral grams_per_kg              (idealised to dryness)
  part values   what value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

S_R = 35.16504  # g of sea salt per kg of seawater

# solute: (charge, molar mass g/mol, mass fraction of sea salt)  TEOS-10 Table D.3
COMPOSITION = {
    "Na": (+1, 22.98976928, 0.3065958),
    "Mg": (+2, 24.3050, 0.0365055),
    "Ca": (+2, 40.078, 0.0117186),
    "K": (+1, 39.0983, 0.0113495),
    "Sr": (+2, 87.62, 0.0002260),
    "Cl": (-1, 35.453, 0.5503396),
    "SO4": (-2, 96.0626, 0.0771319),
    "HCO3": (-1, 61.01684, 0.0029805),
    "Br": (-1, 79.904, 0.0019134),
    "CO3": (-2, 60.0089, 0.0004078),
    "BOH4": (-1, 78.8404, 0.0002259),
    "F": (-1, 18.9984032, 0.0000369),
    "OH": (-1, 17.00733, 0.0000038),
    "BOH3": (0, 61.8330, 0.0005527),
    "CO2": (0, 44.0095, 0.0000121),
}

# concentration factor at the onset of each mineral (McCaffrey et al. 1987)
ONSETS = [("calcium carbonate", 1.8), ("gypsum", 3.8), ("halite", 10.6),
          ("magnesium sulfate", 70.0), ("potassium salts", 90.0)]

# molar masses of the products from those of the ions (TEOS-10 Table D.3) and of
# water, so that the mass balance closes exactly (webmineral rounds them to
# 100.09, 172.17, 136.14 and 58.44)
M_H2O = 18.01528
M_CACO3 = 40.078 + 60.0089
M_ANHYDRITE = 40.078 + 96.0626
M_GYPSUM = M_ANHYDRITE + 2 * M_H2O
M_HALITE = 22.98976928 + 35.453


def grams(ion, salinity=S_R):
    """Mass (g) of an ion in 1 kg of seawater."""
    return salinity * COMPOSITION[ion][2]


def moles(ion, salinity=S_R):
    return grams(ion, salinity) / COMPOSITION[ion][1]


def charge_balance(salinity=S_R):
    """Sum of z_j n_j (mol per kg of seawater): zero for a neutral solution."""
    return sum(z * moles(j, salinity) for j, (z, _, _) in COMPOSITION.items())


def remaining_fraction(cf):
    """Fraction of the original water left when the brine is cf times concentrated."""
    return 1.0 / cf


def sequence(salinity=S_R):
    """Idealised masses (g per kg of seawater) laid down by complete evaporation.
    Returns a dict with the moles and grams of each product."""
    n_caco3 = moles("CO3", salinity) + moles("HCO3", salinity) / 2.0
    n_ca = moles("Ca", salinity)
    n_gyp = n_ca - n_caco3
    n_hal = moles("Na", salinity)
    assert n_gyp < moles("SO4", salinity) and n_hal < moles("Cl", salinity)
    used = (grams("Ca", salinity) + grams("CO3", salinity) + grams("HCO3", salinity)
            + n_gyp * COMPOSITION["SO4"][1] + grams("Na", salinity)
            + n_hal * COMPOSITION["Cl"][1])
    bittern = salinity - used
    return {
        "n_caco3": n_caco3, "n_gypsum": n_gyp, "n_halite": n_hal,
        "caco3": n_caco3 * M_CACO3,
        "gypsum": n_gyp * M_GYPSUM,
        "anhydrite": n_gyp * M_ANHYDRITE,
        "halite": n_hal * M_HALITE,
        "bittern": bittern,
    }


def anhydrous_total(seq):
    """Mass of the dry precipitate (anhydrite counted for gypsum), g per kg."""
    return seq["caco3"] + seq["anhydrite"] + seq["halite"] + seq["bittern"]


def bittern_charge(salinity=S_R):
    """Charge (mol per kg) of the ions left for the bittern salts: zero if the
    sequence keeps the brine neutral."""
    seq = sequence(salinity)
    left = {j: moles(j, salinity) for j in COMPOSITION}
    for j in ("Ca", "CO3", "HCO3", "Na"):
        left[j] = 0.0
    left["SO4"] -= seq["n_gypsum"]
    left["Cl"] -= seq["n_halite"]
    # the carbonate reaction releases CO2 and H2O, not charge; the Ca it used was
    # balanced by the alkalinity it consumed
    return sum(COMPOSITION[j][0] * left[j] for j in COMPOSITION)


def layer_thickness(grams_per_kg, column_m, rho_sw, rho_mineral):
    """Thickness (m) of a mineral layer from a column of seawater of height
    column_m: mass per m2 of the salt, divided by the density of the mineral."""
    return column_m * rho_sw * grams_per_kg / 1000.0 / rho_mineral


if __name__ == "__main__":
    seq = sequence()
    write_table(__file__, ("CF", "f_left"),
                [(10 ** (i / 50.0), remaining_fraction(10 ** (i / 50.0))) for i in range(101)],
                part="curve")
    write_table(__file__, ("mineral", "CF", "f_left"),
                [(m.replace(" ", "_"), cf, remaining_fraction(cf)) for m, cf in ONSETS],
                part="steps")
    write_table(__file__, ("idx", "mineral", "g_per_kg"),
                [(1, "calcium_carbonate", seq["caco3"]), (2, "gypsum", seq["gypsum"]),
                 (3, "halite", seq["halite"]), (4, "bittern", seq["bittern"])],
                part="masses")
    vals = [("charge_balance", charge_balance()), ("anhydrous_total", anhydrous_total(seq)),
            ("halite_share", seq["halite"] / anhydrous_total(seq))]
    vals += [(k, v) for k, v in seq.items()]
    for name, rho in (("halite", 2170.0), ("gypsum", 2300.0), ("caco3", 2710.0)):
        vals.append(("thick_1000m_" + name, layer_thickness(seq[name], 1000.0, 1030.0, rho)))
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)
