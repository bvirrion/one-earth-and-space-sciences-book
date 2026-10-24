"""Carbon isotope mass balance and the mass of a carbon isotope excursion
(Year 3, stable isotopes).

Steady state (ledger planavsky22:forg): the carbon entering the ocean and
atmosphere, of composition d_in (about -5 permil, the mantle value), leaves
buried as carbonate (d_carb) and organic carbon (d_org = d_carb + Delta_B,
Delta_B between -32 and -25 permil), so

    f_org = (d_in - d_carb) / (d_org - d_carb),   d_carb = d_in - f_org Delta_B.

Excursion: a mass m of carbon of composition d_s mixed into an exogenic
reservoir M of composition d_0 shifts it by Delta (negative):

    (M + m)(d_0 + Delta) = M d_0 + m d_s   =>   m = M Delta / (d_s - d_0 - Delta).

The published estimates (ledger dickens11:petm-mass: a -2.5 to -4.0 permil
excursion needs about 2000-3500 Gt C at -60 permil or 6000-12000 Gt C at -25
permil) imply M of about 4.6e4 to 6.3e4 Gt for d_0 = 0; the curves use the
round value M = 5e4 Gt, d_0 = 0.

  part forg     f dcarb25 dcarb30          (d_in = -5)
  part mass     ds m25 m40                 (Gt C, for Delta = -2.5 and -4.0)
  part implied  what value                 M implied by each published pair
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

D_IN = -5.0
M_EXO = 5.0e4
PUBLISHED = ((-2.5, -60.0, 2000.0), (-4.0, -60.0, 3500.0),
             (-2.5, -25.0, 6000.0), (-4.0, -25.0, 12000.0))


def d_carb(f_org, delta_b, d_in=D_IN):
    return d_in - f_org * delta_b


def f_org(d_carb_, delta_b, d_in=D_IN):
    return (d_in - d_carb_) / delta_b


def mass_added(delta, d_s, m_res=M_EXO, d_0=0.0):
    return m_res * delta / (d_s - d_0 - delta)


def implied_reservoir(delta, d_s, m, d_0=0.0):
    return m * (d_s - d_0 - delta) / delta


def main():
    rows = [[f, d_carb(f, -25.0), d_carb(f, -30.0)] for f in np.linspace(0.0, 0.4, 41)]
    write_table(__file__, ("f", "dcarb25", "dcarb30"), rows, part="forg")
    rows = [[ds, mass_added(-2.5, ds), mass_added(-4.0, ds)] for ds in np.linspace(-70.0, -20.0, 51)]
    write_table(__file__, ("ds", "m25", "m40"), rows, part="mass")
    write_table(__file__, ("what", "value"),
                [["M_%g_%g" % (d, s), implied_reservoir(d, s, m)] for d, s, m in PUBLISHED],
                part="implied")


if __name__ == "__main__":
    main()
