"""Refraction over a dipping interface: the reversed spread on the west limb of
the Varden anticline (Year 3, exploration-seismology).

The spread runs along section A-B from s = 300 m (shot W) to s = 1500 m
(shot E), on ground idealised as level at DATUM_REFR = 440 m. The refractor is
the top of the limestone (base of the shale), a plane on the fold limb, read
from figdata/shared/region.py at the two shot points (nan-guarded). Above it,
the chalk and the shale are lumped into one layer of speed V1 (the shale, slower
than the chalk, is a velocity inversion that refraction cannot see); below it,
V2 is the limestone speed of seismic_model.PROPS.

With i_c = asin(V1 / V2), dip theta, and perpendicular depths h_W, h_E under
the shots, the head-wave times are
    shot E, shooting down-dip:  t = x sin(i_c + theta) / V1 + 2 h_E cos(i_c) / V1
    shot W, shooting up-dip:    t = x sin(i_c - theta) / V1 + 2 h_W cos(i_c) / V1
valid beyond the critical distance; the direct wave is t = x / V1.

  part west, east   x tdir thead   first-arrival branches (x from the shot, m;
                                   t in ms; thead = nan before the critical distance)
  part values       what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
import seismic_model as M  # noqa: E402

V1 = 2400.0
V2 = M.PROPS["limestone"][0]


def geometry():
    sw, se = M.S_REFR
    zw, ze = M.contact("shale", sw), M.contact("shale", se)
    length = se - sw
    theta = math.atan((ze - zw) / length)           # refractor rises towards E
    dw, de = M.DATUM_REFR - zw, M.DATUM_REFR - ze     # vertical depths below the datum
    return length, theta, dw * math.cos(theta), de * math.cos(theta)


def head_time(x, h, ic, sign_theta, theta, v1=V1):
    return x * math.sin(ic + sign_theta * theta) / v1 + 2.0 * h * math.cos(ic) / v1


def critical_distance(h, ic, sign_theta, theta):
    """Offset beyond which the head wave exists. In a frame where the refractor
    is horizontal, the perpendicular depth under a receiver at offset x is
    h + s x sin(theta) (s = +1 shooting down-dip), its projection on the
    refractor x cos(theta); the two critical legs project h tan(ic) and
    (h + s x sin(theta)) tan(ic), so
        x_c = 2 h tan(ic) / (cos(theta) - s sin(theta) tan(ic))."""
    return 2.0 * h * math.tan(ic) / (math.cos(theta) - sign_theta * math.sin(theta) * math.tan(ic))


def branches(sign_theta, h, theta, ic, length):
    xc = critical_distance(h, ic, sign_theta, theta)
    rows = []
    for x in np.arange(0.0, length + 0.1, 20.0):
        th = head_time(x, h, ic, sign_theta, theta) * 1000.0 if x >= xc else "nan"
        rows.append((x, x / V1 * 1000.0, th))
    return rows, xc


if __name__ == "__main__":
    length, theta, hw, he = geometry()
    ic = math.asin(V1 / V2)
    west, xcw = branches(-1.0, hw, theta, ic, length)   # shot W shoots up-dip
    east, xce = branches(+1.0, he, theta, ic, length)   # shot E shoots down-dip
    write_table(__file__, ("x", "tdir", "thead"), west, part="west")
    write_table(__file__, ("x", "tdir", "thead"), east, part="east")
    v_up = V1 / math.sin(ic - theta)
    v_down = V1 / math.sin(ic + theta)
    ti_w = 2.0 * hw * math.cos(ic) / V1
    ti_e = 2.0 * he * math.cos(ic) / V1
    recip_w = head_time(length, hw, ic, -1.0, theta)
    recip_e = head_time(length, he, ic, +1.0, theta)
    vals = [("length_m", length), ("theta_deg", round(math.degrees(theta), 3)),
            ("ic_deg", round(math.degrees(ic), 3)), ("hw_perp_m", round(hw, 1)), ("he_perp_m", round(he, 1)),
            ("v_up", round(v_up, 1)), ("v_down", round(v_down, 1)),
            ("ti_w_ms", round(ti_w * 1000, 2)), ("ti_e_ms", round(ti_e * 1000, 2)),
            ("t_reciprocal_w_ms", round(recip_w * 1000, 2)), ("t_reciprocal_e_ms", round(recip_e * 1000, 2)),
            ("xcrit_w", round(xcw, 1)), ("xcrit_e", round(xce, 1))]
    write_table(__file__, ("what", "value"), vals, part="values")
