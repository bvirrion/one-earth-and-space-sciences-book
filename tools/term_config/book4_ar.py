"""Book 4 (University, Year 2) -- ar. Curation only; the rules live in tools/termlink/.

Curated by the Book 4 `ar` agent (2026-10-30) from this edition's own harvest,
with the frequency and chapter-set censuses against the English twin
(draft/b4-run/tools/census.py), never by translating book4_en.py. AMBIG_POLICY is
"drop", as in English.

lang_ar.py has no WORD_TAIL: the article and the one-letter prepositions are a
HEAD, so an indefinite term also links its definite forms, but a term harvested
in its definite form (most of this book's \\emph{} terms) does not reach the
indefinite, plural or possessive forms the text uses elsewhere. Those forms are
declared in EXTRA, each one a form this edition really uses in the right sense;
the first census (stub, 2026-10-30) found 28 English targets unreached, all of
them for that reason.

STOP (ordinary words outside their defining chapter; the term still links in it):
- التحوّل: metamorphism (ch10), but in ch18 a tipping point (نقطة التحوّل), in
  ch24 the firn-to-ice transformation, in ch25 the mid-Pleistocene transition and
  in ch30 the conversion of kerogen (نسبة التحوّل = transformation ratio): STOP;
  the metamorphic phrases of ch11 and ch18 are declared in EXTRA;
- الكشف: detection of climate change (ch27), but the detection limit of ch31
  (حدّ الكشف) and the detection time of an early-warning system (ch28): STOP.

Protects (EXTRA_PROTECT) keep the right sense of a homograph and mask the wrong one:
- العتبة: a sill (ch05), but the anomaly threshold of the stream-sediment
  exercise 29.9 and its solution, and the CO2 threshold of the snowball
  Earth in ch18: masked there;
- أنماط صخرية: petrologic types of chondrites (ch02), but "three rock types"
  in ch07: masked there;
- نسبة الخلط: the mixing ratio of water vapour (ch21), but the CO2 mole
  fraction of exercise 26 (English protects the same site).
"""

_MET = "def:b2:metamorphic-facies:metamorphism"

AMBIG_POLICY = "drop"

STOP = {"التحوّل", "الكشف"}

NO_CAPITAL = set()

EXTRA = {
    # metamorphism outside ch10 (the bare word is STOPped above)
    "درجة التحوّل": _MET,
    "التحوّل الإقليمي": _MET,
    "التحوّل عالي الضغط": _MET,
    "التحوّل عالي الحرارة": _MET,
    "التحوّل المزدوج": _MET,
    # klippe and tectonic window (ch13): the indefinite and plural forms
    "كليب": "def:b2:alpine-orogen:klippe",
    "كليبات": "def:b2:alpine-orogen:klippe",
    "الكليبات": "def:b2:alpine-orogen:klippe",
    "نافذة تكتونية": "def:b2:alpine-orogen:klippe",
    # balanced cross-sections (ch14): the plural
    "المقاطع العرضية المتوازنة": "def:b2:alpine-orogen:balanced",
    # thick-skinned tectonics (ch13 sol, ch14)
    "تكتونية سميكة الجلد": "def:b2:alpine-orogen:skin",
    "السميكة الجلد": "def:b2:alpine-orogen:skin",
    # equivalent potential temperature (ch21): the possessive form
    "درجة حرارته الكامنة المكافئة": "def:b2:atmospheric-thermodynamics:theta-e",
    # S-type granite (ch12): the indefinite and plural forms
    "غرانيتات النمط S": "def:b2:crustal-melting:types",
    "غرانيت من النمط S": "def:b2:crustal-melting:types",
    "غرانيتًا من النمط S": "def:b2:crustal-melting:types",
    # ocean gateways (ch26): the plural
    "الممرّات المحيطية": "def:b2:deep-time-climate:gateway",
    # normalised diagrams (ch03, ch08)
    "مخطّط مُعايَر": "def:b2:elements-in-the-earth:normalised",
    "المخطّطات المعايَرة": "def:b2:elements-in-the-earth:normalised",
    # refractory elements (ch03)
    "عناصر عصيّة": "def:b2:elements-in-the-earth:volatility",
    "العناصر العصيّة": "def:b2:elements-in-the-earth:volatility",
    # geothermal system, heat in place, low-enthalpy resource (ch30)
    "الأنظمة الحرارية الأرضية": "def:b2:energy-geology:geothermal",
    "نظام حراري أرضي": "def:b2:energy-geology:geothermal",
    "حرارتها المختزنة": "def:b2:energy-geology:geothermal",
    "حرارته المختزنة": "def:b2:energy-geology:geothermal",
    "مورد منخفض الإنثالبي": "def:b2:energy-geology:geothermal",
    # eruption column (ch06): the indefinite and plural forms
    "عمود ثوران": "def:b2:eruptive-styles:column",
    "أعمدة الثوران": "def:b2:eruptive-styles:column",
    # lahars (ch06, ch28): the plural
    "اللاهارات": "def:b2:eruptive-styles:lahar",
    "لاهارات": "def:b2:eruptive-styles:lahar",
    # explosive eruption (ch06, ch28)
    "الثورانات الانفجارية": "def:b2:eruptive-styles:regimes",
    "ثوران انفجاري": "def:b2:eruptive-styles:regimes",
    "ثورانًا انفجاريًا": "def:b2:eruptive-styles:regimes",
    # debris flow, factor of safety (ch28)
    "تدفّق حطام": "def:b2:geological-hazards:slope",
    "تدفّقات الحطام": "def:b2:geological-hazards:slope",
    "تدفّقات حطام": "def:b2:geological-hazards:slope",
    "معامل أمان": "def:b2:geological-hazards:slope",
    "معامل أمانه": "def:b2:geological-hazards:slope",
    # early warning system (ch28): the indefinite form
    "نظام إنذار مبكر": "def:b2:geological-hazards:warning",
    # mantle end-members (ch04): the plural as written
    "الطرفية للوشاح": "def:b2:isotope-geochemistry:end-members",
    # magmatic volatiles (ch06): the plural
    "المكوّنات الصهارية المتطايرة": "def:b2:magma-emplacement:volatiles",
    # Harker diagrams (ch08, ch09): the plural
    "مخطّطات هاركر": "def:b2:magmatic-differentiation:harker",
    # mineral assemblages (ch10, ch11): the plural
    "المجموعات المعدنية": "def:b2:metamorphic-facies:assemblage",
    # Lagerstätten (ch20): the plural
    "مواقع الحفظ الاستثنائي": "def:b2:palaeoenvironments:lagerstatte",
    # oceanic anoxic events (ch19, ch20, ch26): the plural
    "أحداث نقص الأكسجين المحيطي": "def:b2:phanerozoic-earth:oae",
    # meteorite classes (ch02): the plurals
    "الأكوندريتات": "def:b2:planet-formation-meteorites:classes",
    "أكوندريتات": "def:b2:planet-formation-meteorites:classes",
    "النيازك الحديدية": "def:b2:planet-formation-meteorites:classes",
    "نيازك حديدية": "def:b2:planet-formation-meteorites:classes",
    # planetesimals (ch02): the plural and indefinite forms
    "الكويكبات البدائية": "def:b2:planet-formation-meteorites:planetesimal",
    "كويكبات بدائية": "def:b2:planet-formation-meteorites:planetesimal",
    "كويكب بدائي": "def:b2:planet-formation-meteorites:planetesimal",
    # short-lived radionuclides (ch02): the plural
    "النويدات المشعة قصيرة العمر": "def:b2:planet-formation-meteorites:slr",
    # petrologic types (ch02): the plural
    "الأنماط الصخرية": "def:b2:planet-formation-meteorites:type",
    "أنماط صخرية": "def:b2:planet-formation-meteorites:type",
    # P--T--t paths (ch12, ch13): the plural
    "مسارات الضغط--الحرارة--الزمن": "def:b2:pt-paths:ptt",
    # peneplain (ch15): the indefinite form
    "شبه سهل": "def:b2:wilson-cycle:peneplain",
    # terranes and microcontinents (ch15, ch19)
    "رقع قشرية": "def:b2:wilson-cycle:terrane",
    "رقعة قشرية": "def:b2:wilson-cycle:terrane",
    "قارة صغرى": "def:b2:wilson-cycle:terrane",
    # serpentinisation (ch11): the indefinite form (لسربنتة)
    "سربنتة": "def:b2:pt-paths:ocean-floor",
}

DROP = set()
DERIVED = {}
PRIMARY_OK = set()

EXTRA_PROTECT = [
    # العتبة: the anomaly threshold of exercise 29.9 and its solution, not a sill
    r'(?<!\w)الخلفية\s+والعتبة', r'(?<!\w)فوق\s+العتبة', r'(?<!\w)والعتبة\s+\$',
    # العتبة: the CO2 threshold for leaving a snowball state (ch18 text and exercise)
    r'(?<!\w)أن\s+العتبة\s+كانت', r'(?<!\w)كانت\s+العتبة',
    # أنماط صخرية: the three peridotites are not three rock types (ch07), not the
    # petrologic type of a chondrite
    r'(?<!\w)ثلاثة\s+أنماط\s+صخرية',
    # نسبة الخلط: the CO2 mole fraction of the air (ch26), as English protects it
    r'(?<!\w)وما\s+نسبة\s+الخلط',
]
