"""Threshold of motion and a Hjulstrom-type diagram (Year 1, erosion-transport).

Threshold of motion of quartz grains on a flat bed in water at 20 C, from the
expression of Soulsby and Whitehouse (1997) for the critical Shields parameter,
as given in the USACE HEC-RAS 2D sediment technical reference manual (ledger
hecras:thresholds):

    D* = d [(s - 1) g / nu^2]^(1/3),
    theta_cr = 0.3 / (1 + 1.2 D*) + 0.055 [1 - exp(-0.02 D*)],
    tau_cr = theta_cr (rho_s - rho) g d,

and the depth-averaged velocity that produces it in a wide flow of depth h, by
Keulegan's (1938) law for rough channels, U / u* = 6.25 + 5.75 log10(h / k_s),
with the sand roughness k_s taken equal to the grain diameter (ledger
keulegan:mean-velocity):

    U_cr = [6.25 + 5.75 log10(h / d)] sqrt(theta_cr (s - 1) g d).

The expressions are for non-cohesive grains: they are tabulated from 0.0625 mm
(the sand-silt boundary) up.

The diagram adds the velocity below which a grain carried in suspension settles
out. Suspension needs turbulent eddies whose upward velocities, of the order of
the shear velocity, exceed the settling velocity (Bagnold 1966, ledger
bagnold:suspension); the limit is taken at u* = w_s, so
U_s = [6.25 + 5.75 log10(h / d)] w_s (w_s by the combined law of settling.py).
For any grain, the flow erodes above U_cr and deposits below min(U_cr, U_s);
fine grains already moving stay in suspension between U_s and U_cr.

  part shields  d_mm dstar theta tau_cr             tau in Pa
  part hjul     d_mm u_cr u_s u_dep                 cm/s, h = 1 m (u_cr nan below 0.0625 mm)
  part values   what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402
import settling as st  # noqa: E402

H_DEMO = 1.0           # m, flow depth of the diagram
D_COHESIVE = 0.0625e-3  # m, the sand-silt boundary
SUSP_RATIO = 1.0       # the limit of suspension is taken at u* = SUSP_RATIO * w_s


def dstar(d, R=st.R_Q, nu=st.NU, g=st.G):
    return d * (R * g / (nu * nu)) ** (1.0 / 3.0)


def theta_cr(d, **kw):
    D = dstar(d, **kw)
    return 0.3 / (1.0 + 1.2 * D) + 0.055 * (1.0 - math.exp(-0.02 * D))


def tau_cr(d, rho_s=st.RHO_Q, rho=st.RHO_W, g=st.G):
    """Critical bed shear stress (Pa) for a quartz grain of diameter d (m)."""
    return theta_cr(d) * (rho_s - rho) * g * d


def shields(tau, d, rho_s=st.RHO_Q, rho=st.RHO_W, g=st.G):
    """Shields parameter of the bed shear stress tau (Pa) for grains of diameter d (m)."""
    return tau / ((rho_s - rho) * g * d)


def bed_shear(h, S, rho=st.RHO_W, g=st.G):
    """Depth-slope product: bed shear stress (Pa) of a steady, uniform, wide flow."""
    return rho * g * h * S


def log_factor(d, h):
    """U / u* for a wide rough channel of depth h with k_s = d (Keulegan 1938)."""
    return 6.25 + 5.75 * math.log10(h / d)


def u_cr(d, h=H_DEMO):
    """Depth-averaged velocity (m/s) at the threshold of motion."""
    return log_factor(d, h) * math.sqrt(theta_cr(d) * st.R_Q * st.G * d)


def u_susp(d, h=H_DEMO):
    """Depth-averaged velocity (m/s) at which the shear velocity equals the settling velocity."""
    ustar = SUSP_RATIO * st.ferguson_church(d)
    return log_factor(d, h) * ustar


def suspended_limit(ustar, lo=1e-6, hi=0.1):
    """The largest diameter (m) carried in suspension (w_s < u* / SUSP_RATIO) by u* (m/s)."""
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if SUSP_RATIO * st.ferguson_church(mid) < ustar:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def main():
    rows = []
    for d_mm in st.log_grid(0.0625, 100.0, 65):
        d = d_mm * 1e-3
        rows.append((round(d_mm, 6), dstar(d), theta_cr(d), tau_cr(d)))
    write_table(__file__, ("d_mm", "dstar", "theta", "tau_cr"), rows, part="shields")
    rows = []
    for d_mm in st.log_grid(0.001, 100.0, 101):
        d = d_mm * 1e-3
        us = 100.0 * u_susp(d)
        if d >= D_COHESIVE * 0.9999:
            uc = 100.0 * u_cr(d)
            rows.append((round(d_mm, 6), uc, us, min(uc, us)))
        else:
            rows.append((round(d_mm, 6), float("nan"), us, us))
    write_table(__file__, ("d_mm", "u_cr", "u_s", "u_dep"), rows, part="hjul")
    values = []
    for d_mm in (0.0625, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 64.0):
        d = d_mm * 1e-3
        values += [("theta_%g_mm" % d_mm, theta_cr(d)), ("tau_cr_%g_mm" % d_mm, tau_cr(d)),
                   ("u_cr_%g_mm" % d_mm, u_cr(d)), ("u_s_%g_mm" % d_mm, u_susp(d))]
    write_table(__file__, ("what", "value"), values, part="values")


if __name__ == "__main__":
    main()
