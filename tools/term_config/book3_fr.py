"""Book 3 (University, Year 1) -- fr. Curation only; the rules live in tools/termlink/.

Curated 2026-10-26 by the Book 3 `fr` agent from this edition's own harvest,
with the frequency and chapter-set censuses against the English twin
(translation_instruction.md). Never copied from book3_en.py or book2_fr.py: each
entry is a French homograph judged against its own target.
"""

# STOP: ordinary words outside their defining chapter (the term still links in
# it), each against its target. Most mirror the English STOP list, in French:
# - stable, stables, stabilité: of a triple junction (ch12); elsewhere stable
#   minerals, isotopes, air and water columns (ch07, 19, 25, 26, 29); the
#   multi-word "point triple stable", "stabilité statique", "stratification
#   stable" still link;
# - extension, étirement: the strain e (ch16); elsewhere the amount of rifting
#   or the stretching of the crust (ch13, 23), "co-extension" of a biozone
#   (ch24) and "son extension dans l'hémisphère Nord" (ch28);
# - ordre: of an interference colour (ch08); elsewhere "dans cet ordre", "de
#   l'ordre de", "au premier ordre" (every chapter);
# - relief: optical relief (ch08); elsewhere the topographic relief (ch10, 11,
#   14, 15, 17, 20, 21);
# - série, système, étage, groupe, formation, membre: the stratigraphic units
#   (ch24); elsewhere "une série de", the solar system, a closed isotopic
#   system, "à ce stade", deep-water formation, "un membre de";
# - flux: of a source (ch02); elsewhere heat, buoyancy, sediment and carbon
#   fluxes (ch15, 19, 20, 27);
# - direction, directions: the strike of a plane (ch04); elsewhere the
#   direction of a wind, of vibration, of a plate motion or of a transport
#   (every chapter), which English never links ("strike" is its own word);
# - hauteur, hauteurs, mi-hauteur: of a star above the horizon (ch01);
#   elsewhere the height of a scale, of a wave or of a column (ch11, 26).
STOP = {"stable", "Stable", "stables", "Stables", "stabilité", "Stabilité",
        "extension", "Extension", "extensions", "étirement", "Étirement",
        "étirements", "ordre", "Ordre", "ordres", "relief", "Relief", "reliefs",
        "série", "Série", "séries", "système", "Système", "systèmes",
        "étage", "Étage", "étages", "groupe", "Groupe", "groupes",
        "formation", "Formation", "formations", "membre", "Membre", "membres",
        "flux", "Flux", "direction", "Direction", "directions",
        "hauteur", "Hauteur", "hauteurs", "mi-hauteur"}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

EXTRA_PROTECT = [
    # déclinaison: the magnetic declination of a compass (ch06), not the
    # celestial coordinate (English protects the same senses)
    r'\bdéclinaison\s+magnétique\b', r'\bréglage\s+de\s+déclinaison\b',
    r'\bcorrection\s+de\s+déclinaison\b', r'\bpour\s+la\s+déclinaison\b',
    r'\brégler\s+la\s+déclinaison\b', r'\bdéclinaison\s+a\s+varié\b',
    r'\bCorriger\s+de\s+la\s+déclinaison\b',
    # chevauchement: the overlap of two stratigraphic units (ch24), not a thrust
    r'\bnon\s+attribué\s+ou\s+un\s+chevauchement\b',
    # flancs: the slopes of oceanic islands (ch22), not the limbs of a fold
    r'\bsur\s+les\s+flancs\s+de\s+nombreuses\b',
    # clivage: the cleavage of a mineral (ch21), not of a rock
    r'\bde\s+bon\s+clivage\b',
    # grand cercle: the largest inscribed circle of a grain (ch21)
    r'\bplus\s+grand\s+cercle\s+inscrit\b',
    # groupe, membre: a working group and the voting members of a commission
    # (ch24 body and the 2024 box), not a lithostratigraphic group or member
    r'(?<!\w)groupe\s+de\s+travail\b', r'(?<!\w)groupe\s+a\s+proposé\b',
    r'(?<!\w)membres\s+votants\b', r'(?<!\w)membres\s+ne\s+votant\b',
    # carte géologique: institutions' names (ch08, ch24)
    r'\bService\s+de\s+la\s+carte\s+géologique\b',
    r'\bCommission\s+de\s+la\s+carte\s+géologique\b',
    # contacts: grain contacts (ch23), not geological contacts on a map
    r'\baux\s+contacts\s+entre\s+grains\b',
    # points triples: the two dots of the Shields curve (ch21), not triple junctions
    r'\bles\s+points\s+triples\s+près\s+de\b',
    # masse d'air: the mass of air in a mass-flux (ch28), not the air mass of
    # an observation
    r"\bmasse\s+d'air\s+(?:par\s+seconde|comprise|entrant)",
    r"\bla\s+masse\s+d'air\s+par\s+seconde\b",
]
