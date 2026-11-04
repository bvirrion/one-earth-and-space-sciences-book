"""Book 5 (University, Year 3) -- hi. Curation only; the rules live in tools/termlink/.

Curated by the pilot-edition coordinator (claude-opus-5-5, 2026-11-04) from this edition's harvest and the per-target census
against English. Hindi homographs found, each STOPped (a STOP keeps the defining chapter's own links, as harvest.py falls through):
  * ध्रुव -- the pole of a plane (ch08), but also every geographic and magnetic pole (ch19-22, 26-31).
  * रैंप -- a thrust ramp (ch10), but also the carbonate ramp (ch16-17) and the ice-albedo ramp (ch22).
  * समतल खंड -- a thrust flat (ch10), read also as a flat section (ch28-29).
  * दृष्टि-रेखा -- InSAR line of sight (ch25), but the astronomical line of sight in ch28-29.
  * स्थायी अवस्था -- the steady river profile (ch18), but every other steady state (ch22-30).
  * मॉडल आयु -- the isotopic model age (ch13), but the crater model ages of ch26.
  * पलटाव बिंदु -- a seismic ray (ch01), but a shoreline turning point in ch16.
  * पुनर्प्राप्ति -- recovery of a deformed crystal (ch07), but recovering a signal in ch25.
  * भँवर -- the atmospheric eddy (ch20), but the ocean eddies of ch21.
EXTRA: targets English reaches and whose Hindi form the harvest misses (hyphenated or named forms, oblique plurals).
AMBIG_POLICY = "drop", as the University books.
"""

STOP = {"ध्रुव", "रैंप", "समतल खंड", "दृष्टि-रेखा", "स्थायी अवस्था", "मॉडल आयु", "पलटाव बिंदु", "पुनर्प्राप्ति", "भँवर"}
NO_CAPITAL = set()
EXTRA = {
    "पिन रेखा": "def:b3:structural-analysis:restoration",
    "पिन रेखाओं": "def:b3:structural-analysis:restoration",
    "पिन रेखाएँ": "def:b3:structural-analysis:restoration",
    "डार्सी का नियम": "thm:b3:hydrogeology:darcy",
    "डार्सी के नियम": "thm:b3:hydrogeology:darcy",
    "बंद-पेटिका मॉडल": "thm:b3:origin-of-elements:closed-box",
    "समुद्री-हिम विस्तार": "def:b3:glaciology:sea-ice",
    "रैस्टर आँकड़े": "def:b3:remote-sensing-gis:data-models",
    "सदिश आँकड़े": "def:b3:remote-sensing-gis:data-models",
    "रैस्टर आँकड़ों": "def:b3:remote-sensing-gis:data-models",
    "समुद्री-हिम का माध्य विस्तार": "def:b3:glaciology:sea-ice",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"
EXTRA_PROTECT = []
