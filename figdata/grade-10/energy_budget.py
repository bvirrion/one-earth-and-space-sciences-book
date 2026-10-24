"""Sunlight received by latitude and season, the global energy budget and the
photosynthesis share (grade 10, earth-energy-budget).

Sources (ledger): solar irradiance and Bond albedo, obliquity, mean radius,
perihelion and aphelion (earth:TSI, earth:albedo, earth:obliquity,
earth:Rmean, earth:peri, earth:aph); the AR6 global energy budget, Figure 7.2
(ipcc:budget-toa, ipcc:budget-surface, ipcc:budget-clearsky); enthalpy of
vaporization of water (nist:water-latent); global net primary production
(field:npp); enthalpy of combustion of glucose (nist:glucose-combustion).

The orbit is taken circular (the distance varies by 3 % over the year, the
sunlight by 7 %: the `numbers` part gives both); the Sun's declination is
sin(delta) = sin(eps) sin(lambda), with the Sun's longitude lambda advancing
uniformly from the March equinox, taken as day 80.

  part daily    day Q0 Q30 Q60 Q90     daily-mean insolation (W/m2) at 0, 30, 60, 90 N
  part annual   lat Qann               annual-mean insolation (W/m2) by latitude
  part numbers  key value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

S0 = 1361.0                 # earth:TSI, W/m2
ALBEDO = 0.294              # earth:albedo
EPS = 23.44                 # earth:obliquity, deg
R_EARTH = 6371.0e3          # earth:Rmean, m
PERI, APH = 147.095, 152.100  # earth:peri, earth:aph, 1e6 km
YEAR_DAYS = 365.242         # earth:Ptrop
EQUINOX_DAY = 80            # March equinox, day of the year (about 21 March)

# AR6 WG1 Figure 7.2, all sky, W/m2 (ipcc:budget-toa, ipcc:budget-surface)
BUDGET = {
    "incoming": 340.0, "reflected": 100.0, "olr": 239.0, "imbalance": 0.7,
    "abs_atm": 80.0, "refl_surface": 25.0, "solar_down": 185.0, "abs_surface": 160.0,
    "latent": 82.0, "sensible": 21.0, "lw_up": 398.0, "lw_down": 342.0,
}
CLEAR = {"reflected": 53.0, "olr": 267.0}       # ipcc:budget-clearsky

L_VAP_15C = 2465.5e3        # nist:water-latent, J/kg at 288.12 K
RHO_WATER = 1000.0          # kg/m3 (999.1 at 15 degC; rounded)
NPP_PGC = 104.9             # field:npp, Pg C per year
H_GLUCOSE = 2805.0e3        # nist:glucose-combustion, J/mol (6 mol C)
M_C = 12.011                # g/mol, standard atomic weight of carbon
SECONDS_PER_YEAR = 365.25 * 86400.0


def declination(day):
    """Sun's declination (deg) on a day of the year (circular orbit)."""
    lam = 2 * math.pi * (day - EQUINOX_DAY) / YEAR_DAYS
    return math.degrees(math.asin(math.sin(math.radians(EPS)) * math.sin(lam)))


def daily_insolation(lat, decl, s0=S0):
    """Daily-mean insolation (W/m2) at the top of the atmosphere on a
    horizontal surface: (S0/pi)(h0 sin(phi) sin(delta) + cos(phi) cos(delta) sin(h0)),
    with h0 the hour angle of sunset (0 in polar night, pi in polar day)."""
    phi, d = math.radians(lat), math.radians(decl)
    x = -math.tan(phi) * math.tan(d) if abs(lat) < 90 else (-1.0 if decl * lat > 0 else 1.0)
    if x >= 1:
        return 0.0
    h0 = math.pi if x <= -1 else math.acos(x)
    q = (s0 / math.pi) * (h0 * math.sin(phi) * math.sin(d) + math.cos(phi) * math.cos(d) * math.sin(h0))
    return max(q, 0.0)


def annual_mean(lat, steps=3652):
    return sum(daily_insolation(lat, declination(1 + i * YEAR_DAYS / steps)) for i in range(steps)) / steps


def global_mean(steps_lat=180):
    """Area-weighted mean of the annual insolation over the sphere (checks S0/4)."""
    tot = w = 0.0
    for i in range(steps_lat):
        lat = -90 + (i + 0.5) * 180 / steps_lat
        c = math.cos(math.radians(lat))
        tot += c * annual_mean(lat, steps=365)
        w += c
    return tot / w


def closure():
    """Imbalances of the three budgets of Figure 7.2 (W/m2)."""
    b = BUDGET
    toa = b["incoming"] - b["reflected"] - b["olr"]
    surface = b["abs_surface"] + b["lw_down"] - b["latent"] - b["sensible"] - b["lw_up"]
    # the atmosphere absorbs 80 of sunlight, the latent and sensible heat and the part of the
    # surface emission that does not pass through the window W; it emits 342 down and olr - W up:
    # W cancels.
    atmosphere = b["abs_atm"] + b["latent"] + b["sensible"] + b["lw_up"] - b["lw_down"] - b["olr"]
    solar = b["incoming"] - b["reflected"] - b["abs_atm"] - b["abs_surface"]
    surface_solar = b["solar_down"] - b["refl_surface"] - b["abs_surface"]
    return {"toa": toa, "surface": surface, "atmosphere": atmosphere, "solar": solar,
            "surface_solar": surface_solar}


def numbers():
    n = {}
    n["S_over_4"] = S0 / 4
    n["absorbed"] = S0 / 4 * (1 - ALBEDO)
    n["global_mean_check"] = global_mean()
    n["eq_equinox"] = daily_insolation(0, 0)
    dj = declination(EQUINOX_DAY + YEAR_DAYS / 4)
    n["decl_june"] = dj
    for lat in (0, 30, 60, 90):
        n["june_%d" % lat] = daily_insolation(lat, dj)
        n["dec_%d" % lat] = daily_insolation(lat, -dj)
        n["annual_%d" % lat] = annual_mean(lat)
    n["june_pole_kWh_day"] = n["june_90"] * 24 / 1000
    n["june_eq_kWh_day"] = n["june_0"] * 24 / 1000
    n["polar_night_starts_lat"] = 90 - EPS
    n["distance_ratio"] = APH / PERI
    n["sunlight_ratio"] = (APH / PERI) ** 2
    c = closure()
    n.update({"closure_" + k: v for k, v in c.items()})
    b = BUDGET
    n["albedo_ar6"] = b["reflected"] / b["incoming"]
    n["absorbed_ar6"] = b["incoming"] - b["reflected"]
    n["atm_share_reflected"] = b["reflected"] - b["refl_surface"]
    n["clouds_solar"] = CLEAR["reflected"] - b["reflected"]
    n["clouds_thermal"] = CLEAR["olr"] - b["olr"]
    n["clouds_net"] = n["clouds_solar"] + n["clouds_thermal"]
    evap = b["latent"] / L_VAP_15C * SECONDS_PER_YEAR      # kg/m2 per year
    n["evap_kg_m2_yr"] = evap
    n["evap_m_yr"] = evap / RHO_WATER
    area = 4 * math.pi * R_EARTH ** 2
    n["earth_area"] = area
    n["absorbed_total_W"] = n["absorbed"] * area
    n["imbalance_total_W"] = b["imbalance"] * area
    e_per_gC = H_GLUCOSE / 6 / M_C                        # J per gram of carbon fixed
    n["energy_per_gC"] = e_per_gC
    n["npp_power_W"] = NPP_PGC * 1e15 * e_per_gC / SECONDS_PER_YEAR
    n["npp_per_m2"] = n["npp_power_W"] / area
    n["photosynthesis_share_pct"] = 100 * n["npp_power_W"] / n["absorbed_total_W"]
    return n


if __name__ == "__main__":
    rows = []
    for day in range(1, 366, 2):
        d = declination(day)
        rows.append((day,) + tuple(daily_insolation(lat, d) for lat in (0, 30, 60, 90)))
    write_table(__file__, ("day", "Q0", "Q30", "Q60", "Q90"), rows, part="daily", digits=5)
    write_table(__file__, ("lat", "Qann"), [(lat, annual_mean(lat)) for lat in range(0, 91, 5)],
                part="annual", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=7)
