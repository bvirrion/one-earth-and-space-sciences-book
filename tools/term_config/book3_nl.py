"""Book 3 (University, Year 1) -- nl. Curated from this edition's own harvest.

The Dutch surfaces that collide with ordinary words are DROPped, not STOPped:
harvest.py keeps a STOPped term in the per-chapter map, so a STOP alone leaves
it linking wherever a chapter pins exactly one sense (checked against the
chapter-set census, 2026-10-27). Derived forms are listed too, because
morphology.derive runs before DROP and would otherwise re-create them.
"""

STOP = {
    # ordinary words that carry one sense in their defining chapter only (trend
    # of a line in ch. 06, optical relief in ch. 08, the order of an interference
    # colour in ch. 08); elsewhere they are the ordinary words
    "richting", "richtingen", "reliëf", "reliëfs", "orde", "ordes", "orden",
    "helling", "hellingen",
    # "hoogte" is the ordinary word for height (a station, a cliff, a column of
    # air, a stratigraphic level): the altitude of a star (horizontal
    # coordinate) is linked only in the chapter that defines it (ch. 01).
    # Linked everywhere it collided with the height of 40+22 passages of ch. 11
    # and 26 (checked against the chapter-set census, 2026-10-27).
    "hoogte", "Hoogte", "hoogten", "Hoogten",
}
NO_CAPITAL = set()
# EXTRA: the attributive inflection "drievoudige" is not reached by the head-only
# morphology, so "het drievoudige knooppunt" would lose its link (EN links 10x).
EXTRA = {
    "drievoudige knooppunt": "def:b1:plate-kinematics:triple-junction",
    # the Dutch text uses the English word "heave" and the Dutch word "worp" for
    # the throw of a fault (EN links both forms to the same definition)
    "heave": "def:b1:cross-sections:throw",
    "worp": "def:b1:cross-sections:throw",
    "worpen": "def:b1:cross-sections:throw",
    # plurals and welded compounds of the targets that EN links more often
    "gasreuzen": "def:b1:comparative-planetology:planet-types",
    "ijsreuzen": "def:b1:comparative-planetology:planet-types",
    "reuzenplaneten": "def:b1:comparative-planetology:planet-types",
    "aardachtige planeten": "def:b1:comparative-planetology:planet-types",
    "planetoïden": "def:b1:comparative-planetology:small-bodies",
    "sluitingstemperaturen": "def:b1:radiometric-methods:closure",
    "afkoelingsleeftijden": "def:b1:radiometric-methods:closure",
    "drievoudige knooppunten": "def:b1:plate-kinematics:triple-junction",
    "slijpplaten": "def:b1:field-lab-methods-1:thin-section",
    # hyphenated and welded forms of "hellingrichting" (dip direction): the
    # attitude definition, which EN links as "dip direction"
    "helling-richting": "def:b1:geological-maps:attitude",
    "hellingsrichting": "def:b1:geological-maps:attitude",
    "hellingsrichtingen": "def:b1:geological-maps:attitude",
    "hellingrichtingen": "def:b1:geological-maps:attitude",
    "tweelingen": "def:b1:optical-mineralogy:twin",
    # the sentence-initial plural of "oriented samples" (EN links it once)
    "Georiënteerde monsters": "def:b1:field-lab-methods-1:sample",
    # "referentiemodel" alone: the reference Earth model, in every chapter from
    # ch. 09 on (EN writes "the reference Earth model" once)
    "referentiemodel": "def:b1:layered-earth:reference-model",
    "dunne slijpplaten": "def:b1:field-lab-methods-1:thin-section",
    "interferentiekleuren": "def:b1:optical-mineralogy:interference-colour",
    # bare "slijpplaat" is the thin section of ch. 06-08 (31 uses; EN links "thin section" 24x);
    # the defined term is "dunne slijpplaat", and "slijpplaten" is listed above
    "slijpplaat": "def:b1:field-lab-methods-1:thin-section",
    # twinning (the process of forming twins, ch. 08): EN links "polysynthetic twinning" to twin
    "tweelingvorming": "def:b1:optical-mineralogy:twin",
    # singular of "drievoudige knooppunt" (ch. 12 body; EN links "triple junction" 5x)
    "drievoudig knooppunt": "def:b1:plate-kinematics:triple-junction",
}
DROP = {
    # trend and dip: ordinary words for direction and slope; the attitude
    # definition keeps hellingrichting and strijk
    "Clapeyron-helling",
    "oriëntatie", "oriëntaties", "Oriëntatie",
    # "stable" (ordinary adjective); "stabiel drievoudig knooppunt" keeps the sense
    "stabiel", "stabiele", "stabielen", "stabiels",
    # the bare order of an interference colour (the ordinary word "orde" and
    # "grootte-orde" are not the term); the hyphenated orders stay
    "grootte-orde", "grootte-orden",
    # "closed system" in thermodynamics; the chronostratigraphic system keeps
    # "systeem (chronostratigrafisch)" and "Jura-systeem"
    "systeem", "systemen",
    # sediment flux in prose ("warmteflux" and the rest); the source flux keeps
    # "flux (van een bron)"
    "flux", "fluxen", "Fluxen",
    # the verb "to touch"; the rake keeps the English form "rake"
    "raken",
    # two spellings of the same ooze; the welded form "kalkslijk" is the term
    "kalk slijk",
}
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

EXTRA_PROTECT = [
    # raken: the Dutch verb "to touch" ("de bodem raken"), which the morphology
    # reads as the plural of the English word "rake" ("rake" + "n")
    r'(?<!\w)raken(?!\w)',
    # declinatie: the magnetic declination of a compass (ch06), not the
    # celestial coordinate (English protects the same senses)
    r'\bmagnetische\s+declinatie\b', r'\bvoor\s+de\s+declinatie\b',
    r'\bde\s+declinatie\s+in\s+te\s+stellen\b', r'\bde\s+declinatie\s+met\b',
    r'\bdeclinatie-instelling\b',
    # groep: a group of nannofossils (ch. 24), and the working group of the
    # subcommission that proposed a stage (ch. 24 body and its box); English
    # protects the same two senses ("nannofossil group", "the group proposed")
    r'\bgroep\s+nannofossielen\b', r'\bstelde\s+de\s+groep\b',
    # helling: the SLOPE of the ground (ch. 04: "helling van de grond", "steilste
    # helling", "helt als de helling"), not the dip of a plane; English keeps
    # "slope" and "dip" apart, Dutch writes "helling" for both
    r'\bhelling\s+van\s+de\s+grond\b', r'\bsteilste\s+helling\b',
    r'\bhelt\s+als\s+de\s+helling\b',
    # worp: the CTD cast of ch. 26 (a vertical profile of a sensor), not the throw
    # of a fault; the throw of a fault is linked everywhere else
    r'CTD-worp', r'\bgeeft\s+de\s+worp\b', r'\bworp\s+geeft\b',
    r'\bde\s+worp\s+tussen\s+het\b', r'\bvan\s+de\s+worp\s+ligt\b',
    r'\bop\s+de\s+worp\?',
]
