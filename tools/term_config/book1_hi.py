"""Book 1 (Primary and Middle School, grades 1-9) -- hi. Curation only; the rules live in tools/termlink/.

Curated by the Book 1 `hi` agent (2026-10-25) from this edition's own harvest
(`--terms`), an inflection scan of the Hindi corpus, the frequency and
chapter-set censuses against the English twin, and a reading of every
flagged term in its Hindi contexts -- not translated from book1_en.py.

Hindi homographs found, each handled below:
  * ऊँचाई -- the grade-4 box defines altitude, but the same word is every
    height (of a dune, a tower, the Pole Star above the horizon, a school
    site above its river): it doubled English's count. STOP: it links in its
    own chapter, and altitude is reached after it through समुद्र तल (sea
    level), the other term of the same box. The sea FLOOR is written
    समुद्री तल throughout, so समुद्र तल is only sea level.
  * स्तर -- "stratum" in the grade-7 box, but "level" everywhere else (the
    level of a river, of the sea, of the tide). STOP.
  * सूखा -- the grade-5 drought, but also the adjective "dry" (सूखा/सूखे:
    dry season, dry ground). STOP, so only its own chapter links it, as
    English does outside one recall.
  * मौसम -- weather, but also season: "बरसात का मौसम", "सूखे मौसम",
    "हर मौसम", "मौसमों" (grade 6 groundwater, 14 false links) are masked,
    and so is "मौसम वैज्ञानिक" (a meteorologist: Wegener, grade 7).
  * मैदान -- the plain (grade 1), but also a field: "खेल/स्कूल/फ़ुटबॉल के
    मैदान", "घास का मैदान" (a meadow), the field that receives rain in a
    grade-4 exercise.
  * कीचड़ -- mud (the sand box), but "कीचड़ प्रवाह" is the volcano's
    mudflow, one word in English and unlinked there.
  * पायरो -- the etymology emph of grade 7 (English STOPs "Pyro").
  * ध्रुव -- the Pole Star (ध्रुव तारा) is not a pole.
  * मापनी -- a graph's stretched vertical scale (ऊर्ध्वाधर मापनी) is not a
    map's scale (English protects "vertical scale").
English-only reach restored through EXTRA: the tectonic plate (the bodies say
प्लेट, the box defines विवर्तनिक प्लेट), the date line (the bodies drop
अंतरराष्ट्रीय), the two tropics by name (English links "Tropic of Cancer"), and
English's "the tropics" of grade 8 (the pair of lines, or the zone).
Hindi does not inflect by suffix rules the linker knows (lang_hi.py: no
WORD_TAIL, no DERIVE), so every oblique/plural form the bodies write is
declared in DERIVED, read off the corpus one by one; derivations that are a
different word or sense (सूखे "dry", मौसमों "seasons", स्तरों "levels") are
not there.
"""

STOP = {"ऊँचाई", "स्तर", "सूखा", "पायरो"}
NO_CAPITAL = set()
EXTRA = {
    "प्लेट": "def:g7:plate-tectonics:plate",
    "प्लेटें": "def:g7:plate-tectonics:plate",
    "प्लेटों": "def:g7:plate-tectonics:plate",
    "तिथि रेखा": "def:g6:latitude-longitude:date-line",
    "कर्क रेखा": "def:g5:weather-and-climate:tropics",
    "मकर रेखा": "def:g5:weather-and-climate:tropics",
    # English "the tropics" (grade 8, 8 links): Hindi writes the pair
    # "कर्क और मकर रेखाओं" or the zone "उष्णकटिबंध" (the noun only; the
    # adjective उष्णकटिबंधीय, as in a tropical cyclone or air mass, is
    # another word and the boundary rule leaves it alone)
    "कर्क और मकर रेखाओं": "def:g5:weather-and-climate:tropics",
    "उष्णकटिबंध": "def:g5:weather-and-climate:tropics",
}
DROP = set()
DERIVED = {
    "U-आकार की घाटी": ("U-आकार की घाटियाँ",),
    "अक्षांश": ("अक्षांशों",),
    "अक्षांश रेखा": ("अक्षांश रेखाएँ", "अक्षांश रेखाओं"),
    "अपसारी सीमा": ("अपसारी सीमाएँ",),
    "अभिसारी सीमा": ("अभिसारी सीमाएँ",),
    "अयन वृत्त": ("अयन वृत्तों",),
    "अवदाब": ("अवदाबों",),
    "अवसादी चट्टान": ("अवसादी चट्टानें", "अवसादी चट्टानों"),
    "अवसादी परत": ("अवसादी परतों",),
    "आग्नेय चट्टान": ("आग्नेय चट्टानें",),
    "इमारती पत्थर": ("इमारती पत्थरों",),
    "उद्गार": ("उद्गारों",),
    "कंकड़": ("कंकड़ों",),
    "कगार": ("कगारें", "कगारों"),
    "कायांतरित चट्टान": ("कायांतरित चट्टानें",),
    "कुआँ": ("कुएँ", "कुओं"),
    "कोहरा": ("कोहरे",),
    "खनिज": ("खनिजों",),
    "खाका": ("खाके",),
    "गुफा": ("गुफाएँ",),
    "गोलार्ध": ("गोलार्धों",),
    "ग्लोब": ("ग्लोबों",),
    "घाटी": ("घाटियाँ", "घाटियों"),
    "चट्टान": ("चट्टानें", "चट्टानों"),
    "चट्टानी ग्रह": ("चट्टानी ग्रहों",),
    "जलभृत": ("जलभृतों",),
    "जलवायु आलेख": ("जलवायु आलेखों",),
    "जीवाश्म": ("जीवाश्मों",),
    "जोखिम": ("जोखिमों",),
    "ज्वालामुखी": ("ज्वालामुखियों",),
    "झील": ("झीलें", "झीलों"),
    "टिब्बा": ("टिब्बे", "टिब्बों"),
    "डेल्टा": ("डेल्टाओं",),
    "तीव्रता": ("तीव्रताएँ",),
    "तूफ़ान": ("तूफ़ानों",),
    "ध्रुव": ("ध्रुवों",),
    "ध्रुवीय वृत्त": ("ध्रुवीय वृत्तों",),
    "नदी": ("नदियाँ", "नदियों"),
    "निकास-छिद्र": ("निकास-छिद्रों",),
    "पछुआ पवनें": ("पछुआ पवनों",),
    "परिमाण": ("परिमाणों",),
    "पर्वत": ("पर्वतों",),
    "पर्वत-श्रेणी": ("पर्वत-श्रेणियाँ", "पर्वत-श्रेणियों", "पर्वत श्रेणी",
                     "पर्वत श्रेणियाँ"),
    "पहाड़ी": ("पहाड़ियाँ", "पहाड़ियों"),
    "पुलिन": ("पुलिनों",),
    "प्रतिचक्रवात": ("प्रतिचक्रवातों",),
    "प्राकृतिक संकट": ("प्राकृतिक संकटों",),
    "प्लेट सीमा": ("प्लेट सीमाएँ", "प्लेट सीमाओं"),
    "बहिःस्रावी उद्गार": ("बहिःस्रावी उद्गारों",),
    "बाढ़": ("बाढ़ें", "बाढ़ों"),
    "बादल": ("बादलों",),
    "बारिश": ("बारिशों",),
    "भंडार": ("भंडारों",),
    "भू-जिह्वा": ("भू-जिह्वाएँ",),
    "भूकंप": ("भूकंपों",),
    "भूकंपमापी": ("भूकंपमापियों",),
    "भूकंपलेख": ("भूकंपलेखों",),
    "भूदृश्य": ("भूदृश्यों",),
    "भ्रंश": ("भ्रंशों",),
    "मरुस्थल": ("मरुस्थलों",),
    "महाकल्प": ("महाकल्पों",),
    "महाद्वीप": ("महाद्वीपों",),
    "महाद्वीपीय मग्नतट": ("महाद्वीपीय मग्नतटों",),
    "महासागर": ("महासागरों",),
    "महासागरीय कटक": ("महासागरीय कटकों",),
    "महासागरीय धारा": ("महासागरीय धाराओं",),
    "मानचित्र": ("मानचित्रों",),
    "मुहाना": ("मुहाने", "मुहानों"),
    "मैदान": ("मैदानों",),
    "मोह्स पैमाना": ("मोह्स पैमाने",),
    "मौसम केंद्र": ("मौसम केंद्रों",),
    "मौसम-चिह्न": ("मौसम-चिह्नों",),
    "याम्योत्तर": ("याम्योत्तरों",),
    "रंध्र": ("रंध्रों",),
    "रूपांतर सीमा": ("रूपांतर सीमाओं",),
    "वर्षावन": ("वर्षावनों",),
    "वलय": ("वलयों",),
    "वाताग्र": ("वाताग्रों",),
    "वायु राशि": ("वायु राशियाँ", "वायु राशियों"),
    "वितलीय मैदान": ("वितलीय मैदानों",),
    "विशाल ग्रह": ("विशाल ग्रहों",),
    "विसर्प": ("विसर्पों",),
    "विस्फोटक उद्गार": ("विस्फोटक उद्गारों",),
    "व्यापारिक पवनें": ("व्यापारिक पवनों",),
    "संवहन कोष्ठ": ("संवहन कोष्ठों",),
    "समदाब रेखा": ("समदाब रेखाएँ", "समदाब रेखाओं"),
    "समय-क्षेत्र": ("समय-क्षेत्रों",),
    "समुद्र": ("समुद्रों",),
    "समोच्च रेखा": ("समोच्च रेखाएँ", "समोच्च रेखाओं"),
    "साँचा": ("साँचे",),
    "सांद्रण गुणक": ("सांद्रण गुणकों",),
    "सुनामी": ("सुनामियाँ", "सुनामियों"),
    "सोता": ("सोते", "सोतों"),
    "हिम शेल्फ़": ("हिम शेल्फ़ों",),
    "हिमचादर": ("हिमचादरें", "हिमचादरों"),
    "हिमनद": ("हिमनदों",),
    "हिमशैल": ("हिमशैलों",),
    "तट": ("तटों",),
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
    # \pageref and inline \tikz are not in the shared protect list
    r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
    # proper name: the invented Varden Hills (a region, not the landform)
    _D + r'वार्डन\s+पहाड़ि(?:याँ|यों)' + _E,
    # मौसम as a season, and the meteorologist
    _D + r'(?:बरसात|सूखे|गर्मी|गर्मियों|सर्दी|सर्दियों|जाड़े|ठंडे)\s+(?:(?:के|का|की)\s+)?मौसम' + _E,
    _D + r'हर\s+मौसम' + _E, _D + r'मौसमों' + _E,
    _D + r'मौसम\s+वैज्ञानिक' + _E,
    # मैदान as a field or a meadow
    _D + r'(?:खेल|स्कूल|फ़ुटबॉल|घास)\s+(?:के|का)\s+मैदान' + _E,
    _D + r'वर्ग\s+मीटर\s+के\s+एक\s+मैदान' + _E,
    _D + r'कि\s+मैदान\s+पर' + _E,
    # the volcano's mudflow (one word in English, unlinked)
    _D + r'कीचड़\s+प्रवाह(?:ों)?' + _E,
    # सूखा the adjective "dry" inside the drought chapter (a house on high
    # ground "stays dry", grade 5 ch. 3 caption)
    _D + r'सूखा\s+रहत(?:ा|े|ी)' + _E,
    # the Pole Star
    _D + r'ध्रुव\s+तार(?:ा|े)' + _E,
    # a graph's vertical scale
    _D + r'ऊर्ध्वाधर\s+मापनी' + _E,
    # hot springs on the sea floor are not the groundwater spring
    _D + r'गरम\s+सोत(?:े|ों)' + _E,
    # relief: the name of a dataset
    r'ETOPO1\s+उच्चावच' + _E,
    # the Americas, a region (English "the Americas", unlinked)
    _D + r'अमेरिका\s+महाद्वीप(?:ों)?' + _E,
]
