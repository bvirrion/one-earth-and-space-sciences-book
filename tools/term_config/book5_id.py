"""Book 5 (University, Year 3) -- id. Curation only; the rules live in tools/termlink/.

Curated 2026-11-03 by the Book 5 `id` coordinator (pilot method) from this edition's own harvest and the frequency and
chapter-set census against English (pilot_translation/census.py). A STOPped term still links in the chapter that pins its one
sense, and nowhere else.

- kutub: the pole of a plane on a stereonet (ch. 8) against the Earth's pole, the geomagnetic pole, the Euler pole, everywhere
  else (116 links against English's 43, most in ch. 19-29).
- tanjakan, bagian datar: the thrust ramp and flat of ch. 10 against any slope or flat part (62 against 1).
- keadaan tunak: the steady river profile of ch. 18 against any steady state of a climate or an aquifer.
- pemulihan: recovery in crystal plasticity (ch. 7) against the recovery of vegetation (ch. 25).

Accepted as they are: umur model (ch. 26: the crater model age, English writes no link there); CMP, GIA, SI and similar, which
Indonesian writes out where English abbreviates, so they link more often than English; eddy (ch. 21: ocean eddies, same notion).
"""

STOP = {"kutub", "Kutub", "kutub-kutub", "kutub-kutubnya", "kutubnya",
        "tanjakan", "Tanjakan", "bagian datar", "Bagian datar",
        "keadaan tunak", "Keadaan tunak",
        "pemulihan", "Pemulihan"}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"
EXTRA_PROTECT = []
