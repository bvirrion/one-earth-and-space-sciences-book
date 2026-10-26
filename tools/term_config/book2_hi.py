"""Book 2 (High School, grades 10-12) -- hi. Curation only; the rules live in tools/termlink/.

Curated by the Book 2 `hi` agent (2026-10-26) from this edition's own harvest
(`--terms`), an inflection scan of the Hindi corpus, the frequency and
chapter-set censuses against the English twin, and a reading of every flagged
term in its Hindi contexts -- not translated from book2_en.py or book1_hi.py.

Hindi homographs found, each handled below:
  * आँख -- the cyclone's eye (g10.05), but also the naked eye (g11.08,
    g12.03), exactly as English STOPs "eye". STOP.
  * अभिवाह -- the flux of water of the stock-and-flux box (g10.09), but also
    the energy fluxes of g10.03; English STOPs "flux". STOP.
  * भंडार -- the water stock (g10.09), but also the short form of the oil
    reservoir (भंडार चट्टान, g11.09), a store of elements in a soil (g10.07)
    and Kelvin's store of heat (g12.07). STOP.
  * कोटि -- the rank of coal (g11.09), but also "of the same order"
    (उसी कोटि, four solutions and g11.07). STOP.
  * मूल -- the root of a mountain range (g12.01), but also a fourth root
    (g12.08), the original length of a folded layer (g12.02), the original
    layers of a schist (g12.03) and the basic response of the climate
    (g12.10). Linked, with those four uses protected -- as English protects
    "square/fourth root". (The g10-g11 uses, मूल-बिंदु and भूकंप-मूल, come
    before the definition and are never reached.)
  * स्थिर / अस्थिर -- the stability of air (g10.04), but also constant,
    steady, stable isotopes and minerals; English STOPs stable/unstable.
    STOP; "स्थिर वायु" and "अस्थिर वायु" still link, as in English.
  * संतृप्त / संतृप्ति -- of air (g10.04), but also a peridotite saturated
    with water (g12.04); English STOPs both. STOP.
  * ज्वालामुखीय -- the adjective is everywhere (gases, arcs, ash); the term
    is reached through ज्वालामुखीय चट्टान, as English. STOP.
  * मध्यवर्ती -- the rock composition (g11.08), but also intermediate-depth
    earthquakes (g11.06) and the intermediate emission scenario (g12.10
    table), both protected exactly where English protects them.
  * प्रणोद -- the thrust (g12.02); the forcing प्रणोदन is a different word
    and the boundary rule leaves it alone. The named Glarus and McConnell
    thrusts are protected, as in English.
  * अंतर्हिमनदीय काल -- the Last Interglacial, an AR6 reference period, is a
    proper name (अंतिम अंतर्हिमनदीय काल), protected as in English.
English short forms restored through EXTRA, as in book2_en.py: the forcing
(प्रणोदन), the feedbacks (प्रतिपुष्टि), the scenarios (परिदृश्य) and climate
sensitivity.
Hindi does not inflect by suffix rules the linker knows (lang_hi.py: no
WORD_TAIL, no DERIVE), so every oblique/plural form the bodies write is
declared in DERIVED, read off the corpus one by one.
"""

STOP = {"आँख", "अभिवाह", "भंडार", "कोटि", "स्थिर", "अस्थिर",
        "संतृप्त", "संतृप्ति", "ज्वालामुखीय"}
NO_CAPITAL = set()
EXTRA = {
    # g12 climate-change: the chapter uses the short forms of its terms
    "प्रणोदन": "def:g12:climate-change:forcing",
    "प्रतिपुष्टि": "def:g12:climate-change:feedback",
    "प्रतिपुष्टियाँ": "def:g12:climate-change:feedback",
    "प्रतिपुष्टियों": "def:g12:climate-change:feedback",
    "परिदृश्य": "def:g12:climate-change:scenario",
    "परिदृश्यों": "def:g12:climate-change:scenario",
    "जलवायु संवेदनशीलता": "def:g12:climate-change:ecs",
    # g11 subduction solutions: "the pull of the sinking slab", as English
    "डूबती स्लैब का खिंचाव": "def:g11:subduction-zones:slab-pull",
}
DROP = set()
DERIVED = {
    "P तरंग": ("P तरंगें", "P तरंगों"),
    "S तरंग": ("S तरंगें", "S तरंगों"),
    "अंतर्वेधन": ("अंतर्वेधनों",),
    "अंतर्हिमनदीय काल": ("अंतर्हिमनदीय कालों",),
    "अनाच्छादन दर": ("अनाच्छादन दरें",),
    "अपनति": ("अपनतियाँ",),
    "अभिनति": ("अभिनतियाँ",),
    "अपवाह द्रोणी": ("अपवाह द्रोणियाँ", "अपवाह द्रोणियों"),
    "अवसादी द्रोणी": ("अवसादी द्रोणियों",),
    "आवरण चट्टान": ("आवरण चट्टानें",),
    "उष्णकटिबंधीय चक्रवात": ("उष्णकटिबंधीय चक्रवातों",),
    "ओफ़ियोलाइट": ("ओफ़ियोलाइटों",),
    "कोयला": ("कोयले", "कोयला-परत", "कोयला-खान"),
    "क्रेटन": ("क्रेटनों",),
    "क्षेपण क्षेत्र": ("क्षेपण क्षेत्रों",),
    "खंडज चट्टान": ("खंडज चट्टानों",),
    "चुंबकीय विसंगति": ("चुंबकीय विसंगतियाँ",),
    "जल-विभाजक": ("जल-विभाजकों",),
    "जलवायु प्रतिपुष्टि": ("जलवायु प्रतिपुष्टियाँ",),
    "जलालेख": ("जलालेखों",),
    "ज्वालामुखीय चट्टान": ("ज्वालामुखीय चट्टानें",),
    "ट्रैप": ("ट्रैपों",),
    "डाइक": ("डाइकों",),
    "तड़ित-झंझा": ("तड़ित-झंझाओं",),
    "त्रिभुजन": ("त्रिभुजनों",),
    "दीर्घक्रिस्टल": ("दीर्घक्रिस्टलों",),
    "दृढ़ प्लेट": ("दृढ़ प्लेटें", "दृढ़ प्लेटों"),
    "निवास काल": ("निवास कालों",),
    "नैप": ("नैपों",),
    "पट्टित लौह संरचना": ("पट्टित लौह संरचनाएँ", "पट्टित लौह संरचनाओं"),
    "पतली काट": ("पतली काटें",),
    "पातालीय चट्टान": ("पातालीय चट्टानें", "पातालीय चट्टानों"),
    "पुनरावृत्ति काल": ("पुनरावृत्ति कालों",),
    "प्रक्षेपण": ("प्रक्षेपणों",),
    "प्रणोद": ("प्रणोदों",),
    "प्रसरण दर": ("प्रसरण दरें", "प्रसरण दरों"),
    "प्लूटॉन": ("प्लूटॉनों",),
    "बहुरूप": ("बहुरूपों",),
    "बैथोलिथ": ("बैथोलिथों",),
    "भूतापीय प्रवणता": ("भूतापीय प्रवणताएँ",),
    "मृत्तिका खनिज": ("मृत्तिका खनिजों",),
    "यात्रा-काल": ("यात्रा-कालों",),
    "यात्रा-काल वक्र": ("यात्रा-काल वक्रों",),
    "वलन": ("वलनों",),
    "विदलन": ("विदलनों",),
    "शैलकारी सिलिकेट": ("शैलकारी सिलिकेटों",),
    "समश्रेणी-रेखा": ("समश्रेणी-रेखाएँ",),
    "सापेक्ष गति": ("सापेक्ष गतियों",),
    "सामान्य भ्रंश": ("सामान्य भ्रंशों",),
    "सिलिकन--ऑक्सीजन चतुष्फलक": ("सिलिकन--ऑक्सीजन चतुष्फलकों",),
    "सिलिकेट": ("सिलिकेटों",),
    "सीवन": ("सीवनों",),
    "सूचक खनिज": ("सूचक खनिजों",),
    "सैफ़िर--सिम्पसन पैमाना": ("सैफ़िर--सिम्पसन पैमाने",),
    "स्ट्रोमैटोलाइट": ("स्ट्रोमैटोलाइटों",),
    "स्रोत चट्टान": ("स्रोत चट्टानें",),
    "स्लैब": ("स्लैबों", "स्लैबें"),
    "हिमनदीय काल": ("हिमनदीय कालों",),
    "हिमनदीय चक्र": ("हिमनदीय चक्रों",),
    "बर्फ़ का कोर": ("बर्फ़ के कोर", "बर्फ़ के कोरों"),
    "मूल": ("मूलों",),
    "नवीकरणीय मीठा जल": ("नवीकरणीय मीठे जल",),
    "तड़ित": ("तड़ित-चमकें", "तड़ित-नली"),
}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
_D = r'(?<![\u0900-\u097F])'   # no Devanagari letter or sign before
_E = r'(?![\u0900-\u097F])'    # ... nor after
EXTRA_PROTECT = [
    # run-in paragraph headings stay unlinked, like section titles
    r'\\paragraph\{[^{}]*\}',
    # the bold Part headings of a weekend problem: the shared list masks
    # "\textbf{Part I ...}" only, not its translation
    r'\\textbf\{भाग\s+[IVX]+\b(?:[^{}]|\{[^{}]*\})*\}',
    # \pageref and inline \tikz, as in English
    r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
    # the gloss of Vine and Matthews's paper title (g11.01): a title never
    # links, as English's \emph title (coordinator, 2026-10-26)
    r'\(महासागरीय\s+कटकों\s+के\s+ऊपर\s+चुंबकीय\s+विसंगतियाँ\)',
    # proper name: the invented Varden Hills (a region, not the landform)
    _D + r'वार्डन\s+पहाड़ि(?:याँ|यों)' + _E,
    # intermediate: the depth of earthquakes (g11.06) and an emission scenario
    # (g12.10 table), not the rock composition -- as English
    _D + r'मध्यवर्ती\s+और\s+गहरे' + _E, r'&\s*मध्यवर्ती\s*&',
    # proper names: the Last Interglacial (an AR6 reference period), the
    # Glarus and McConnell thrusts (named faults) -- as English
    _D + r'अंतिम\s+अंतर्हिमनदीय\s+काल' + _E,
    _D + r'(?:ग्लारुस|मैककॉनेल)\s+प्रणोद' + _E,
    # root: a fourth root (g12.08), an original length (g12.02), original
    # layers (g12.03), the basic response (g12.10) -- not a mountain root
    _D + r'चतुर्थ\s+मूल' + _E, _D + r'मूल\s+(?:लंबाई|परतें|प्रतिक्रिया)' + _E,
    # a stratovolcano (g12.04) is not the stratification of the ocean
    _D + r'स्तरित\s+ज्वालामुखी' + _E,
    # motion with respect to a hotspot (g11.04 solutions), not the relative
    # motion of two plates -- English writes "motion with respect to"
    _D + r'तप्त\s+स्थल\s+के\s+सापेक्ष\s+गति' + _E,
    # relief: the name of a dataset
    r'ETOPO1\s+उच्चावच' + _E,
]
