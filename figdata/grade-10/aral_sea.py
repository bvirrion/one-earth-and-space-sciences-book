"""The water budget of the Aral Sea, 1960-2010 (grade 10, freshwater-resources).

Source (ledger): Gaybullaev, Chen and Gaybullaev (2012), Table 1, river runoff,
evaporation, water volume, precipitation and salinity of the Aral Sea
(gaybullaev:aral-table), and the 1960 surface area and level
(gaybullaev:aral-1960). The rows are copied from the table; the test checks them
against the ledger row.

The level change of a lake with no outlet is (R + P - E)/A per year. If the
evaporation per unit area e = E/A keeps its 1960 value, the area in a later year is
E/e, and the level change is (R + P)/A - e.

  part record   year runoff evap volume precip salinity
  part numbers  key value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

# year: (river runoff, evaporation, volume, precipitation) in km3, salinity in g/L
TABLE = {
    1960: (42.0, 71.1, 1093.0, 9.4, 10.0),
    1973: (0.9, 60.0, 824.2, 4.4, 13.4),
    1977: (0.2, 45.7, 749.2, 5.0, 15.4),
    1982: (1.3, 38.5, 579.8, 8.5, 18.8),
    1984: (0.3, 47.9, 502.7, 3.5, 21.9),
    1987: (1.0, 36.8, 345.6, 6.2, 25.0),
    1989: (3.1, 35.3, 327.2, 5.3, 30.0),
    1992: (10.6, 31.9, 260.5, 5.4, 35.0),
    1995: (4.7, 28.5, 239.0, 2.5, 38.0),
    1996: (6.6, 25.7, 217.4, 3.0, 39.0),
    1998: (31.5, 24.6, 195.4, 6.0, 42.0),
    2001: (3.1, 23.1, 149.1, 2.5, 58.6),
    2002: (13.1, 37.1, 129.2, 4.0, 82.0),
    2003: (20.6, 36.7, 117.0, 5.4, 86.0),
    2004: (15.8, 24.8, 115.9, 3.0, 91.0),
    2005: (7.4, 14.0, 112.3, 3.5, 98.0),
    2006: (5.0, 11.8, 105.3, 2.8, 109.0),
    2007: (7.0, 11.9, 104.3, 3.0, 112.0),
    2008: (6.1, 10.1, 103.1, 2.5, 117.0),
    2009: (5.2, 8.3, 102.0, 3.2, 120.0),
    2010: (4.5, 11.4, 98.1, 3.0, 130.0),
}
AREA_1960_KM2 = 68000.0                    # gaybullaev:aral-1960
LEVEL_1960_M = 53.4


def evaporation_rate_1960():
    """Evaporation per unit area in 1960 (m per year): km3 / km2 = km, times 1000."""
    return TABLE[1960][1] / AREA_1960_KM2 * 1000.0


def area_from_evaporation(year):
    """Area (km2) if the evaporation per unit area kept its 1960 value."""
    return TABLE[year][1] / (evaporation_rate_1960() / 1000.0)


def level_change(year):
    """Level change (m per year) from that year's budget, (R + P - E)/A."""
    r, e, _, p, _ = TABLE[year]
    return (r + p - e) / area_from_evaporation(year) * 1000.0


def salinity_if_salt_kept(year):
    return TABLE[1960][4] * TABLE[1960][2] / TABLE[year][2]


def numbers():
    n = {"e_1960_m": evaporation_rate_1960(),
         "mean_depth_1960_m": TABLE[1960][2] / AREA_1960_KM2 * 1000.0,
         "residence_1960_yr": TABLE[1960][2] / TABLE[1960][1],
         "residence_2010_yr": TABLE[2010][2] / TABLE[2010][1],
         "salt_1960_tonnes": TABLE[1960][2] * 1e9 * TABLE[1960][4] / 1000.0,
         "need_inflow_1960": TABLE[1960][1] - TABLE[1960][3],
         "rain_depth_1960_m": TABLE[1960][3] / AREA_1960_KM2 * 1000.0,
         "river_depth_1960_m": TABLE[1960][0] / AREA_1960_KM2 * 1000.0,
         "net_1987": TABLE[1987][0] + TABLE[1987][3] - TABLE[1987][1],
         "area_1987_km2": area_from_evaporation(1987),
         "area_1987_share": area_from_evaporation(1987) / AREA_1960_KM2,
         "level_change_1987_m": level_change(1987),
         "level_change_1989_m": level_change(1989),
         "volume_loss_1984_1989_per_yr": (TABLE[1984][2] - TABLE[1989][2]) / 5.0,
         "volume_share_1987": TABLE[1987][2] / TABLE[1960][2],
         "volume_share_2010": TABLE[2010][2] / TABLE[1960][2],
         "salinity_if_kept_1987": salinity_if_salt_kept(1987),
         "salinity_if_kept_2010": salinity_if_salt_kept(2010)}
    return n


if __name__ == "__main__":
    write_table(__file__, ("year", "runoff", "evap", "volume", "precip", "salinity"),
                [(y,) + TABLE[y] for y in sorted(TABLE)], part="record")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")
