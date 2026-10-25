"""Book 1 (Primary and Middle School, grades 1-9) -- fr. Curation only; the rules live in tools/termlink/.

Curated by the Book 1 `fr` agent (2026-10-25) from this edition's own harvest,
with the frequency and chapter-set censuses against the English twin.
"""

# STOP (ordinary word outside its defining chapter, where it still links):
# - plan(s): g2's drawing; later "plan de prévention", "au premier plan";
# - intensité: physics owns light/sound intensity; the seismic sense is
#   reached through "échelle d'intensité" (EXTRA), as in English;
# - moule/moulage: kitchen or casting objects outside the fossil definition;
# - Pyro: an etymology emph (g7.2), not a term;
# - symbole(s): English defines "map symbol" (two words); the bare French word
#   also names weather-front symbols (g8.3) and trail signs (g6.5);
# - front(s): English links it only in g8.3; g8.5 uses "front" for the snout
#   of a glacier, g9.4 for the face of a cliff.
STOP = {"plan", "plans", "intensité", "Intensité", "moule", "moules", "moulage",
        "moulages", "Pyro", "symbole", "symboles", "front", "fronts", "Fronts"}
NO_CAPITAL = set()
EXTRA = {
    # g7 defines "plaque tectonique (ou simplement une plaque)": the short form
    # is the one the later chapters use (English: EXTRA "plate")
    "plaque": "def:g7:plate-tectonics:plate",
    "plaques": "def:g7:plate-tectonics:plate",
    "Plaques": "def:g7:plate-tectonics:plate",
    # English "intensity scale"
    "échelle d'intensité": "def:g7:earthquakes:intensity",
    # the plural of "minéral" is not a WORD_TAIL form
    "minéraux": "def:g6:rocks-and-minerals:mineral",
    "Minéraux": "def:g6:rocks-and-minerals:mineral",
    # English links "weather" (weather map, weather services); French says
    # "le temps", a homograph of time, so the sense is reached through météo
    "météo": "def:g1:watching-the-weather:weather",
    "Météo": "def:g1:watching-the-weather:weather",
    "météorologique": "def:g1:watching-the-weather:weather",
    "météorologiques": "def:g1:watching-the-weather:weather",
    # the volcano's "bouche" (short for bouche éruptive) in g7.2 and after
    "bouche": "def:g7:volcanoes:vent",
    "bouches": "def:g7:volcanoes:vent",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
EXTRA_PROTECT = [
    # run-in paragraph headings stay unlinked, like section titles
    r'\\paragraph\{[^{}]*\}',
    # the bold Part headings of a weekend problem: the shared list masks
    # "\textbf{Part I ...}" only, not its translation
    r'\\textbf\{Partie\s+[IVX]+\b(?:[^{}]|\{[^{}]*\})*\}',
    # \pageref and inline \tikz are not in the shared protect list
    r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
    # proper name: the invented Varden Hills (a region, not the landform)
    r'\bcollines\s+de\s+Varden\b',
    # échelle: drawn to scale, scale of a graph, time scales, "at the scale
    # of" (English protects to scale, time/vertical/same/left/right scale...)
    r"(?<!maquette )\b[àÀ]\s+l'échelle\b", r"\bd'échelle\b", r"\bde\s+l'échelle\b",
    r"\b[Ll]'échelle\s+(?:de\s+(?:gauche|droite)|verticale|des)\b",
    r'\b(?:mêmes?|grande|notre|cette)\s+échelles?\b',
    r'\b[Uu]ne\s+échelle\s+(?:de\s+couleurs|où|verticale)\b',
    r'\béchelles?\s+verticales?\b',
    r'\béchelle\s*~?:\s*les\s+planètes\b',
    # météorologique: an institution's name
    r'\bOrganisation\s+météorologique\s+mondiale\b',
    # côte: the Natural Earth credit lines (English "coastlines", one word)
    r'\b[Cc]ôtes\b(?=[^.]{0,30}?Natural\s+Earth)',
    # légende: the verb ("légende les couches")
    r'\blégende\s+les\b',
    # carte: a postcard
    r'\bcartes?\s+postales?\b',
    # Équateur: the country
    r"\bl'Équateur\b",
    # boue: a mudflow (English "mudflow", one word)
    r'\bcoulées?\s+de\s+boue\b',
    # relief: the name of a dataset
    r'\brelief\s+ETOPO1\b',
    # parallèle: the adjective
    r'\b(?:lignes|droites|stries|rayures)\s+parallèles\b', r'\bparallèles?\s+(?:à|au|aux)\b',
    # source: of heat, of an air mass, hot springs on the sea floor
    r'\bsources?\s+de\s+chaleur\b', r'\brégions?\s+sources?\b', r'\bsources\s+chaudes\b',
    # ère: the industrial era
    r'\bère\s+industrielle\b',
    # risque: the verb ("risque de s'y développer")
    r"\brisque(?:nt)?\s+de\s+(?:s'|se\b)",
    # gisement: of oil, gas or coal (an ore deposit is of a metal or mineral)
    r'\bgisements?\s+de\s+(?:pétrole|gaz|charbon)\b',
    # plaque: of ice, of glass
    r'\bplaques?\s+de\s+(?:glace|verre)\b',
]
