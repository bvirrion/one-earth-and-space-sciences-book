"""Book 5 (University, Year 3) -- ar. Curation only; the rules live in tools/termlink/.

STOP: one-word Arabic forms whose ordinary sense is far commoner than the term's. المنحدر is any slope, not the thrust ramp;
القطب is a magnetic or geographic pole more often than a stereonet pole; التراكب is any overlap, not only the GIS overlay;
الاستعادة is any recovery. Under-linking is accepted: a wrong sense is worse than a missing link.
"""

_S = {"منحدر", "قطب", "تراكب", "استعادة", "نطاق عازل", "طور التهيئة", "مقطع زائف", "سطح مستو",
      "حالة مستقرّة", "خط النظر"}  # the last two: any steady state, any line of sight (ch. 28, 29), not the defining sense
STOP = _S | {"ال" + w for w in _S}
NO_CAPITAL = set()
# Indefinite and plural forms the harvest can't reach, one target each: every English target this edition can reach.
EXTRA = {
    "جداول أزمنة الانتقال": "def:b3:seismology-imaging:tables", "جدول أزمنة انتقال": "def:b3:seismology-imaging:tables",
    "درجات الحجب": "def:b3:palaeomagnetism:blocking", "درجات حرارة الحجب": "def:b3:palaeomagnetism:blocking",
    "انحناءة مقيِّدة": "def:b3:extension-strike-slip:bends", "انحناءة محرِّرة": "def:b3:extension-strike-slip:bends",
    "بنية زهرية": "def:b3:extension-strike-slip:flower",
    "رصيف ذو حافة": "def:b3:facies-models:ramp",
    "المحدود بالنقل": "def:b3:quantitative-geomorphology:limited", "المحدود بالاقتلاع": "def:b3:quantitative-geomorphology:limited",
    "نماذج النظام الأرضي": "def:b3:climate-models:esm",
    "عامل تأخير": "def:b3:hydrogeology:retardation",
    "غطاء راكد": "def:b3:planetary-interiors-surfaces:stagnant-lid", "غطاءً راكدًا": "def:b3:planetary-interiors-surfaces:stagnant-lid",
    "عنقود مجرّات": "def:b3:milky-way-galaxies:groups",
    "عناصر ألفا": "def:b3:origin-of-elements:alpha",
    "الارتفاعات الديناميكية": "def:b3:ocean-dynamics:dynamic-height", "الطريقة الديناميكية": "def:b3:ocean-dynamics:dynamic-height", "الشذوذات الجهدية": "def:b3:ocean-dynamics:dynamic-height",
    "بيانات شبكية": "def:b3:remote-sensing-gis:data-models", "بيانات متجهية": "def:b3:remote-sensing-gis:data-models",
    "تغيّرات توقيت العبور": "def:b3:exoplanets:ttv", "تغيّر توقيت العبور": "def:b3:exoplanets:ttv",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"
EXTRA_PROTECT = [
    # الحالة المستقرّة outside ch. 18 is any steady state (climate, wells, ice, s-process), not the river profile;
    # العمر النموذجي in ch. 26 is a crater-count model age, not the isotopic model age.
    r'(?<!\w)أعطِ\s+العمر\s+النموذجي',
    r'(?<!\w)أو\s+الحالة\s+المستقرّة',
    r'(?<!\w)احسب\s+العمر\s+النموذجي',
    r'(?<!\w)النسبي،\s+والعمر\s+النموذجي',
    r'(?<!\w)تستغرق\s+الحالة\s+المستقرّة',
    r'(?<!\w)حول\s+الحالة\s+المستقرّة',
    r'(?<!\w)في\s+الحالة\s+المستقرّة\s+لنموذج', r'(?<!\w)في\s+الحالة\s+المستقرّة،\s+يساوي',
    r'(?<!\w)في\s+العمر\s+النموذجي\s+لسطح',
    r'(?<!\w)وفي\s+الحالة\s+المستقرّة\s+يتلاشى',
    r'(?<!\w)يبلغ\s+العمر\s+النموذجي',
    r'(?<!\w)يُستنتج\s+العمر\s+النموذجي',
]
