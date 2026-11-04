"""Book 4 (University, Year 2) -- hi. Curation only; the rules live in tools/termlink/.

Curated by the Book 4 `hi` edition agent (2026-10-30) from this edition's own
harvest (`--terms`: 448 harvested, 461 linkable), the per-target link census
against the English twin (frequency and chapter set), and a reading of every
flagged Hindi context. Not translated from book4_en.py / book4_fr.py and not
copied from book3_hi.py.

Hindi homographs found, each handled below:
  * संसूचन -- "detection" of the detection-and-attribution definition (ch27),
    but also the detection limit of an instrument (ch31, sol31) and the
    detection of an earthquake by an early-warning network (ch28). English
    links only "attribution", so the bare word is STOPped (8 wrong links).
  * आरोपण -- attribution (ch27: linked), but the verb "can be attributed" in
    the method's last step (ch27 enumerate) is protected, as English does not
    link "attributed".
  * सिल -- the sill (ch05, 08, 12: linked), but "सिल दिया" (stitched, of the
    orogenies that sewed Pangaea, ch19) is the verb सिलना: protected.
  * स्वस्थानिक -- autochthonous rock unit (ch13) and autochthonous fossil
    (ch20): defined twice, dropped by the harvest as in English; the two full
    index keys still link.
  * कायांतरी श्रेणी (metamorphic series) -- ch14 had used it for "metamorphic
    grade"; the text now says कायांतरण श्रेणी there, as ch10-11 do, so no
    protect is needed.

DERIVED: Hindi has no -s tail (lang_hi DERIVE = False), so the oblique plural
(-ों) and the direct plural (-ियाँ, -ें) of the nouns the text uses are declared
here, only where every occurrence is the defined sense. उल्कापिंडों is left
out: the meteorite target is already above English (32 vs 21).

EXTRA: प्रावार का विभव तापमान (the recall form of ch18; the bare विभव तापमान is
also the atmospheric potential temperature of ch21 and is not linked).

AMBIG_POLICY = "drop", as the University books.
"""

STOP = {
    "संसूचन", "संसूचन (जलवायु परिवर्तन का)",
}
NO_CAPITAL = set()
EXTRA = {
    "प्रावार का विभव तापमान": "def:b2:mantle-melting:tp",
}
DROP = set()
DERIVED = {
    "कॉन्ड्राइट": ("कॉन्ड्राइटों",),
    "CI कॉन्ड्राइट": ("CI कॉन्ड्राइटों",),
    "कार्बनमय कॉन्ड्राइट": ("कार्बनमय कॉन्ड्राइटों",),
    "एकॉन्ड्राइट": ("एकॉन्ड्राइटों",),
    "लौह उल्कापिंड": ("लौह उल्कापिंडों",),
    "ग्रहाणु": ("ग्रहाणुओं",),
    "आद्यतारा": ("आद्यतारे", "आद्यतारों"),
    "संघनन तापमान": ("संघनन तापमानों",),
    "दुर्गलनीय तत्त्व": ("दुर्गलनीय तत्त्वों",),
    "वाष्पशील तत्त्व": ("वाष्पशील तत्त्वों",),
    "असंगत तत्त्व": ("असंगत तत्त्वों",),
    "अनुरेखी तत्त्व": ("अनुरेखी तत्त्वों",),
    "महासागरीय द्वीप": ("महासागरीय द्वीपों",),
    "महासागरीय द्वीप बेसाल्ट": ("महासागरीय द्वीप बेसाल्टों",),
    "प्रावार अंत्य-सदस्य": ("प्रावार अंत्य-सदस्यों",),
    "डाइक": ("डाइकों",),
    "सिल": ("सिलों",),
    "प्लूटॉन": ("प्लूटॉनों",),
    "डायापिर": ("डायापिरों",),
    "सिलिकेट गलित": ("सिलिकेट गलितों",),
    "शीतित किनारा": ("शीतित किनारे",),
    "क्यूम्यूलेट": ("क्यूम्यूलेटों",),
    "मैग्मीय श्रेणी": ("मैग्मीय श्रेणियाँ",),
    "क्षारीय श्रेणी": ("क्षारीय श्रेणियाँ", "क्षारीय श्रेणियों"),
    "कैल्क-क्षारीय श्रेणी": ("कैल्क-क्षारीय श्रेणियाँ", "कैल्क-क्षारीय श्रेणियों"),
    "पायरोक्लास्ट": ("पायरोक्लास्टों",),
    "पायरोक्लास्टिक प्रवाह": ("पायरोक्लास्टिक प्रवाहों",),
    "विस्फोटक उद्गार": ("विस्फोटक उद्गारों",),
    "लाहार": ("लाहारों",),
    "पेरिडोटाइट": ("पेरिडोटाइटों",),
    "गलन-अंश": ("गलन-अंशों",),
    "मेटापेलाइट": ("मेटापेलाइटों",),
    "उत्खनन-दर": ("उत्खनन-दरें",),
    "मिग्मेटाइट": ("मिग्मेटाइटों",),
    "ल्यूकोसोम": ("ल्यूकोसोमों",),
    "ल्यूकोग्रेनाइट": ("ल्यूकोग्रेनाइटों",),
    "नैप": ("नैपों",),
    "ओफ़ियोलाइट": ("ओफ़ियोलाइटों",),
    "पर्वतजनक पट्टी": ("पर्वतजनक पट्टियाँ", "पर्वतजनक पट्टियों"),
    "अग्रभूमि द्रोणी": ("अग्रभूमि द्रोणियाँ", "अग्रभूमि द्रोणियों"),
    "संतुलित अनुप्रस्थ काट": ("संतुलित अनुप्रस्थ काटें",),
    "टक्कर-पट्टी": ("टक्कर-पट्टियाँ", "टक्कर-पट्टियों"),
    "महामहाद्वीप": ("महामहाद्वीपों",),
    "टेरेन": ("टेरेनों",),
    "दरार-द्रोणी": ("दरार-द्रोणियाँ",),
    "अंतःक्रेटॉनिक द्रोणी": ("अंतःक्रेटॉनिक द्रोणियाँ", "अंतःक्रेटॉनिक द्रोणियों"),
    "एटॉल": ("एटॉलों",),
    "समुद्री पर्वत": ("समुद्री पर्वतों",),
    "क्रेटॉन": ("क्रेटॉनों",),
    "कोमैटिआइट": ("कोमैटिआइटों",),
    "हरितप्रस्तर पट्टी": ("हरितप्रस्तर पट्टियाँ", "हरितप्रस्तर पट्टियों"),
    "चिह्न जीवाश्म": ("चिह्न जीवाश्मों",),
    "काय जीवाश्म": ("काय जीवाश्मों",),
    "आभासी तापमान": ("आभासी तापमानों",),
    "रॉस्बी तरंग": ("रॉस्बी तरंगें", "रॉस्बी तरंगों"),
    "स्पेलियोथेम": ("स्पेलियोथेमों",),
    "वार्व": ("वार्वों",),
    "हिमनदीय काल": ("हिमनदीय कालों",),
    "अंतर्हिमनदीय काल": ("अंतर्हिमनदीय कालों",),
    "पुनरावृत्ति काल": ("पुनरावृत्ति कालों",),
    "पोर्फ़िरी ताँबा निक्षेप": ("पोर्फ़िरी ताँबा निक्षेपों",),
    "गॉसन": ("गॉसनों",),
}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

EXTRA_PROTECT = [
    r'(?<!\w)सिल\s+(?:दिया|दी|दिए|कर)',          # the verb सिलना (ch19), not a sill
    r'(?<!\w)परिवर्तन\s+का\s+आरोपण\s+अंशतः',      # "can be attributed" (ch27 method step)
]
