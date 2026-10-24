"""The early Earth (grade 12): the faint young Sun, and oxygen through time with the eons.

Young Sun: Gough (1981), Solar Physics 74, 21-34, equation (1),
  L(t) = [1 + (2/5)(1 - t/t_sun)]^(-1) L_sun,   t the Sun's age,
(ledger gough81:luminosity), with t_sun = 4.567 Gyr, the age of the oldest solids of the
Solar System (ledger connelly12:cai). Measured back from today, 1 - t/t_sun = t_ago/t_sun.
Equilibrium temperature as in grade 10 (habitable-planet): T = (S (1 - A) / (4 sigma))^(1/4)
with S = 1361 W/m2 today, A = 0.294 (ledger earth:TSI, earth:albedo, const:sigma), the
albedo kept at today's value; surface temperature today 288 K (earth:Tsurf).

Oxygen: a schematic of the sourced bounds, in units of the present atmospheric level
(PAL, log scale): below 1e-5 PAL before 2.45 Ga (Pavlov and Kasting 2002, ledger
pk02:anoxic; Farquhar 2000, the sulfur signal ends between 2450 and 2090 Ma); the Great
Oxidation Event from 2.46-2.426 Ga (Gumsley 2017) to about 2.06 Ga, oxygen probably above
10 % of today's level (0.02 atm) at 2.0 Ga, 0.02-0.04 atm by 1.85 Ga (Holland 2006, ledger
holland06:stages); 1 PAL today. The curve joins these bounds: at most 1e-5 PAL until
2.46 Ga, 0.1 PAL at 2.06 Ga, flat until 0.85 Ga (Holland's stage 3, no significant
change), then up to 1 PAL today (stages 4-5). A
schematic, said so in the caption: the real curve oscillated.
Eons from the ICS rows of the shared ledger, read by grade-7 time_scale.ledger().

  part sun       t_Ga L S Teq                 0-4.567 Ga ago
  part oxygen    t_Ga pal                     the schematic curve, PAL
  part eons      name start end mid           eon spans (Ma) with the CGMW colours in the sty
  part numbers   key value
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "grade-7"))
from _table import write_table  # noqa: E402
import time_scale  # noqa: E402

T_SUN_GYR = 4.567
S0, ALBEDO, SIGMA = 1361.0, 0.294, 5.670374419e-8
T_SURF_TODAY = 288.0
T_FREEZE = 273.15


def luminosity(t_ago_gyr):
    """L / L_sun at a time t_ago (Gyr) before today (Gough 1981, eq. 1)."""
    return 1.0 / (1.0 + 0.4 * (t_ago_gyr / T_SUN_GYR))


def t_eq(t_ago_gyr=0.0, albedo=ALBEDO):
    s = S0 * luminosity(t_ago_gyr)
    return (s * (1.0 - albedo) / (4.0 * SIGMA)) ** 0.25


# schematic oxygen curve through the sourced bounds (t in Ga before present, PAL);
# straight between the points on the log scale
OXYGEN = ((4.0, 1e-5), (2.46, 1e-5), (2.06, 0.1), (0.85, 0.1), (0.0, 1.0))


def eons():
    base, colour = time_scale.ledger()
    return time_scale.spans(time_scale.LONG, base)


def numbers():
    n = {}
    n["L_at_formation"] = luminosity(T_SUN_GYR)
    n["L_4Ga"] = luminosity(4.0)
    n["L_3Ga"] = luminosity(3.0)
    n["L_2_45Ga"] = luminosity(2.45)
    n["S_4Ga"] = S0 * luminosity(4.0)
    n["Teq_today"] = t_eq(0.0)
    n["Teq_4Ga"] = t_eq(4.0)
    n["Teq_formation"] = t_eq(T_SUN_GYR)
    n["Teq_4Ga_C"] = t_eq(4.0) - T_FREEZE
    n["greenhouse_today"] = T_SURF_TODAY - t_eq(0.0)
    n["warming_to_freeze_4Ga"] = T_FREEZE - t_eq(4.0)
    n["warming_to_288_4Ga"] = T_SURF_TODAY - t_eq(4.0)
    n["ratio_L_quarter_4Ga"] = luminosity(4.0) ** 0.25
    # albedo that would give today's equilibrium temperature with the young Sun
    n["albedo_needed_4Ga"] = 1.0 - (1.0 - ALBEDO) / luminosity(4.0)
    return n


if __name__ == "__main__":
    rows = []
    for t in [i * 0.05 for i in range(0, 92)] + [T_SUN_GYR]:
        rows.append((t, luminosity(t), S0 * luminosity(t), t_eq(t)))
    write_table(__file__, ("t_Ga", "L", "S", "Teq"), rows, part="sun")
    write_table(__file__, ("t_Ga", "pal"), OXYGEN, part="oxygen")
    write_table(__file__, ("name", "start", "end", "mid"),
                [(nm, a, b, 0.5 * (a + b)) for nm, a, b in eons()], part="eons")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")
