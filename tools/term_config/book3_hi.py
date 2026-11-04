"""Book 3 (University, Year 1) -- hi. Curation only; the rules live in tools/termlink/.

Curated by the Book 3 `hi` finishing run (2026-10-28) from this edition's own
harvest (`--terms`), the per-target link census against the English twin
(frequency and chapter set), and a reading of every flagged Hindi context.
Not translated from book3_en.py, book3_es.py or book2_hi.py.

Hindi homographs found, each handled below:
  * स्थायी -- "stable" in ordinary use (स्थायी स्तरीकरण, ch18, ch25-28), and the
    bare word of the stable triple junction (स्थायी त्रि-संधि). The bare word is
    STOPped; the full key stays. (59 wrong links removed.)
  * उभार -- optical relief (ch08) but also the topographic swell or bulge of
    rifts, hotspots and margins (ch11, 13, 14, 15, 22). STOP both keys
    (under-linked in ch08, acceptable).
  * कोटि -- the optical order (प्रथम/तृतीय/चौथी कोटि of interference colours,
    ch08) but also order of magnitude (परिमाण की कोटि), a Taylor order (पहली/
    दूसरी कोटि) and "to first order" in a derivation (ch08, ch15). The bare word
    is STOPped; the three optical ordinals are EXTRA; the math "प्रथम कोटि तक" is
    protected.
  * विस्थापन -- throw of a fault (ch05, 13, 17: linked) but also the
    displacement of a parcel (ch26), of a plate or continent (ch12), an
    earthquake slip (ch18) and an equilibrium shift (ch07). Linked; the wrong
    senses are protected by phrase.
  * फ़्लक्स -- astronomical flux (ch02: linked) but sediment flux (ch20), heat
    flux (ch27, ch29) and a Taylor-style "flux" in ch21 are not the defined sense.
    The non-astronomical phrases are protected.
  * पार्श्व -- fold limb (ch16-17: linked); the lateral side of a bedform (ch21),
    lateral continuity (ch24) and a bed's lateral extent are not limbs.
  * सहसंबंध -- borehole log correlation (ch05) but biostratigraphic and sectional
    correlation (ch24) are not the log key. STOP both keys (2 links lost).
  * प्रसार -- strain as extension (ch16) but "spread", Taylor expansion and the
    spread of a distribution (ch18, ch21, ch26). STOP both keys.
  * संरचना, सदस्य, समूह -- lithostratigraphic formation, member, group (ch24);
    structure, voting members, working and nanofossil groups elsewhere. The
    non-stratigraphic senses are protected.
  * तंत्र, चरण -- chronostratigraphic system and stage (ch24); closed system,
    climate system, decay system, step of step-heating, and the "system" of a
    thermodynamic model (ch25-28) are protected.
  * संपीड़न -- compaction of sediments (ch23) but adiabatic compression of air
    (ch26, ch28). The adiabatic phrases are protected.
  * संपर्क -- geological contact (ch06, 13, 23, 24) but physical contact with the
    atmosphere (ch26) and a contact of the heat balance (ch27). Protected.
  * अभिविन्यास -- geological attitude (ch04-07, 17: linked) but generic
    "orientation" of a crystal section or a rotation (ch08, ch12). Protected.
  * विदलन -- foliation (cleavage of rock) but the good cleavage of a mineral
    (ch21). Protected by phrase.

EXTRA aliases (the Hindi form the text uses, right sense): धँसते स्लैब (the
sinking slab, ch18), GSSP (ch24), कण-आकार (grain size, ch21 on), and the optical
ordinals प्रथम/तृतीय/चौथी कोटि.

Left unlinked on purpose: diachronous (its Hindi use is the defining line
itself), moc (the same), airy (the Hindi chapter 20 does not name Airy), sample
(the Hindi word is generic), seismic parameter (defined only in ch09), facies
(no Hindi occurrence of the defined form in ch24).

AMBIG_POLICY = "drop", as the University books.
"""

STOP = {
    "स्थायी",
    "उभार", "उभार (प्रकाशिक)",
    "कोटि", "कोटि (व्यतिकरण वर्ण की)",
    "प्रसार", "प्रसार (विकृति)",
    "सहसंबंध", "सहसंबंध (लॉगों का)",
}
NO_CAPITAL = set()
EXTRA = {
    "धँसते स्लैब": "def:b1:active-margins:slab",
    "GSSP": "def:b1:stratigraphic-scale:gssp",
    "कण-आकार": "def:b1:clastic-sediments:grain-size",
    "प्रथम कोटि": "def:b1:optical-mineralogy:interference-colour",
    "तृतीय कोटि": "def:b1:optical-mineralogy:interference-colour",
    "चौथी कोटि": "def:b1:optical-mineralogy:interference-colour",
}
DROP = set()
DERIVED = {
    "कार्बोनेट कारखाना": ("कार्बोनेट कारखाने", "कार्बोनेट कारखानों"),
}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

EXTRA_PROTECT = [
    # --- throw / displacement in its ordinary senses (not a fault's throw) ---
    r'साम्य\s+का\s+विस्थापन',
    r'(?:दृढ़\s+प्लेट\s+का\s+हर|महाद्वीपीय|महाद्वीपों\s+का|बाहरी|यह|11\s+के)\s+विस्थापन',
    r'कुरील\s+विस्थापन',
    r'(?:वही|सह-भूकंपीय|औसत|जिनके|हर|वह|भूकंपों\s+के|भूकंपों\s+में\s+जमा)\s+विस्थापन',
    r'और\s+विस्थापन\s+\\qtyrange',
    r'भ्रंश\s+पर\s+विस्थापन',
    r'खंदक-विस्थापन',
    r'तेज़\s+विस्थापन', r'छोटे\s+(?:ऊर्ध्वाधर\s+)?विस्थापन',
    r'विस्थापन\s+घातांकीय', r'उसमें\s+विस्थापन',
    # --- homographs of the ordinary sense ---
    r'कार्य\s+समूह', r'नैनोजीवाश्म\s+समूह',                 # working / nanofossil groups
    r'मतदान\s+सदस्यों', r'सदस्य\s+मतदान',                  # ICS voting members
    r'अपनी\s+संरचना', r'ऊर्ध्वाधर\s+संरचना',                   # structure, not formation
    r'पार्श्व\s+सातत्य', r'ऊर्ध्व-धारा\s+पार्श्व', r'अनुप्रवाह\s+पार्श्व',
    r'अग्र-पार्श्व', r'परतों\s+का\s+पार्श्व',                  # lateral side, not a fold limb
    r'अच्छा\s+विदलन',                                       # a mineral's cleavage
    r'बंद\s+तंत्र', r'क्षय-तंत्र', r'तंत्रों\s+को', r'तंत्र\s+बंद',   # closed / decay system
    r'जलवायु[\s-]+तंत्र', r'(?<!कालस्तरिक, )एक\s+तंत्र',           # climate, model system
    r'हर\s+चरण\s+(?:पर|एक)', r'चरणों\s+में', r'जो\s+चरण', r'चरण-सीमा',  # steps, not stages
    r'स्थैतिक\s+चरण',
    r'संपीड़न\s+से', r'तापन\s+संपीड़न',                         # adiabatic compression
    r'वायुमंडल\s+से\s+संपर्क', r'उसके\s+संपर्क\s+की',           # physical contact
    r'सभी\s+अभिविन्यासों', r'अनुकूल\s+अभिविन्यास', r'कण\s+के\s+अभिविन्यास',
    r'एक\s+अभिविन्यास\s+म', r'जिनके\s+अभिविन्यास', r'कौन-सा\s+अभिविन्यास',
    r'विशेष\s+अभिविन्यास', r'अपने\s+अभिविन्यास', r'अंतरिक्ष\s+का\s+अभिविन्यास',
    r'अभिविन्यास\s+बन', r'दिशा\s+और\s+अभिविन्यास',          # orientation, not attitude
    r'(?:में|अतः|जो)\s+प्रथम\s+कोटि\s+तक',                     # "to first order" in a derivation
    r'(?:निलंबित|घुले|घुला|ऊष्मा|ऊर्जा|भार|वार्षिक|उत्तर-वाही|मॉडल|गुप्त|संवेदी|वैश्विक|विकिरण|तात्कालिक|इसलिए|अतः)[^।\n]{0,30}?फ़्लक्स',  # sediment / heat flux
]
