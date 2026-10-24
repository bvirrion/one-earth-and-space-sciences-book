"""Stocks, fluxes and residence times of the Earth's water (grade 10,
freshwater-resources).

Sources (ledger): the global water cycle of the 1990s, stocks in thousand km3 and
fluxes in thousand km3 per year (trenberth:water-cycle); the volume of water in
river channels (usgs:water-stocks); measured ages of deep Nubian groundwater
(sturchio:nubian-age).

At steady state the residence time of a reservoir is its stock divided by the flux
through it (in, or out: they are equal).

  part times    idx days                residence times in days (log chart)
  part ages     lo_days hi_days         the measured age range of the Nubian water
  part numbers  key value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

DAYS_PER_YEAR = 365.25
# trenberth:water-cycle (thousand km3; thousand km3 per year)
STOCK = {"ocean": 1335040.0, "ice": 26350.0, "groundwater": 15300.0, "lakes_rivers": 178.0,
         "soil": 122.0, "permafrost": 22.0, "atmosphere": 12.7}
FLUX = {"ocean_evaporation": 413.0, "ocean_precipitation": 373.0, "land_precipitation": 113.0,
        "land_evapotranspiration": 73.0, "vapour_to_land": 40.0, "runoff": 40.0}
RIVERS_KM3 = 2120.0                      # usgs:water-stocks (river channels)
NUBIAN_YEARS = (2.0e5, 1.0e6)            # sturchio:nubian-age


def residence_years(stock, flux):
    """Residence time (years) of a reservoir of `stock` crossed by `flux` per year."""
    return stock / flux


def times():
    """[(name, years)] in the order of the chart."""
    atmos_out = FLUX["ocean_precipitation"] + FLUX["land_precipitation"]
    return [
        ("atmosphere", residence_years(STOCK["atmosphere"], atmos_out)),
        ("rivers", residence_years(RIVERS_KM3 / 1000.0, FLUX["runoff"])),
        ("lakes_rivers", residence_years(STOCK["lakes_rivers"], FLUX["runoff"])),
        ("ocean", residence_years(STOCK["ocean"], FLUX["ocean_evaporation"])),
    ]


def balances():
    """In minus out for the ocean, the atmosphere and the land (all should be 0)."""
    f = FLUX
    return {
        "ocean": f["ocean_precipitation"] + f["runoff"] - f["ocean_evaporation"],
        "atmosphere": f["ocean_evaporation"] + f["land_evapotranspiration"]
                      - f["ocean_precipitation"] - f["land_precipitation"],
        "land": f["land_precipitation"] - f["land_evapotranspiration"] - f["runoff"],
    }


def numbers():
    n = {"t_%s_years" % k: v for k, v in times()}
    n.update({"t_%s_days" % k: v * DAYS_PER_YEAR for k, v in times()})
    n.update({"balance_%s" % k: v for k, v in balances().items()})
    n["atmos_flux"] = FLUX["ocean_precipitation"] + FLUX["land_precipitation"]
    n["land_rain_returned_share"] = FLUX["land_evapotranspiration"] / FLUX["land_precipitation"]
    n["ocean_over_nubian_lo"] = NUBIAN_YEARS[0] / (STOCK["ocean"] / FLUX["ocean_evaporation"])
    return n


if __name__ == "__main__":
    write_table(__file__, ("idx", "days"),
                [(i, y * DAYS_PER_YEAR) for i, (_, y) in enumerate(times())], part="times")
    write_table(__file__, ("lo_days", "hi_days"),
                [(NUBIAN_YEARS[0] * DAYS_PER_YEAR, NUBIAN_YEARS[1] * DAYS_PER_YEAR)], part="ages")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")
