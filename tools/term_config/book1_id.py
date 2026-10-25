"""Book 1 (Primary and Middle School, grades 1-9) -- id. Curation only; the rules live in tools/termlink/.

Curated by the Book 1 `id` agent (2026-10-25) from this edition's own harvest,
with the frequency and chapter-set censuses against the English twin.
"""

# STOP (ordinary word outside its defining chapter, where it still links):
# - Piro: an etymology emph (g7.2, "Piro berarti api"), not a term.
STOP = {"Piro"}
NO_CAPITAL = set()
EXTRA = {
    # g7 defines "lempeng tektonik (atau singkatnya lempeng)": the short form
    # is the one the later chapters use (English: EXTRA "plate")
    "lempeng": "def:g7:plate-tectonics:plate",
    "Lempeng": "def:g7:plate-tectonics:plate",
    "lempeng-lempeng": "def:g7:plate-tectonics:plate",
    "Lempeng-lempeng": "def:g7:plate-tectonics:plate",
    # g6 defines "garis batas tanggal internasional"; the text mostly says
    # "garis batas tanggal" (English: EXTRA "date line")
    "garis batas tanggal": "def:g6:latitude-longitude:date-line",
    "Garis batas tanggal": "def:g6:latitude-longitude:date-line",
    # the tropics: English links "tropics" and "Tropic (of Cancer)"; the
    # Indonesian region is "daerah tropis", the lines "Garis Balik Utara/Selatan"
    "daerah tropis": "def:g5:weather-and-climate:tropics",
    "Garis Balik": "def:g5:weather-and-climate:tropics",
    # reduplicated plural, not a WORD_TAIL form
    "zona-zona iklim": "def:g5:weather-and-climate:climate-zone",
    # "an earthquake of magnitude 7" is one prefixed word in Indonesian
    "bermagnitudo": "def:g7:earthquakes:magnitude",
    # g8.4 defines "pilin samudra"; later sentences say "pilin" alone
    # (English links "gyre(s)")
    "pilin": "def:g8:the-oceans:current",
    "Pilin": "def:g8:the-oceans:current",
    # g9.4 defines "gumuk pasir"; the text then says "gumuk" alone (English
    # links "dune(s)")
    "gumuk": "def:g9:landforms:dune",
    "Gumuk": "def:g9:landforms:dune",
    "gumuk-gumuk": "def:g9:landforms:dune",
    "Gumuk-gumuk": "def:g9:landforms:dune",
    # g1 defines "bentuk muka bumi" (the primary-school word); g9.4, read at
    # fourteen, uses the geomorphologist's "bentuk lahan" and its recall box
    # names both (English links "landform(s)" there)
    "bentuk lahan": "def:g1:landscapes-around-us:landform",
    "Bentuk lahan": "def:g1:landscapes-around-us:landform",
    # reduplicated plural of "gunung api": without it, "gunung-gunung"
    # linked to the landform definition and "api" stayed bare
    "gunung-gunung api": "def:g4:volcanoes-earthquakes-first-look:volcano",
    "Gunung-gunung api": "def:g4:volcanoes-earthquakes-first-look:volcano",
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
    r'\\textbf\{Bagian\s+[IVX]+\b(?:[^{}]|\{[^{}]*\})*\}',
    # \pageref and inline \tikz are not in the shared protect list
    r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
    # proper name: the invented Varden Hills (a region, not the landform)
    r'\bPerbukitan\s+Varden\b',
    # proper names: "Gunung Everest", "Gunung St.~Helens" (English "Mount
    # Everest" is never linked to the landform definition)
    r'\bGunung\s+[A-Z][A-Za-z]*',
    # skala: drawn to scale, the scale of a graph or of a time line, "at the
    # scale of a human life / of the Earth", the intensity and magnitude
    # scales (English protects to scale, time/vertical/same/left/right/human/
    # magnitude scales and "the scale of")
    r'\bmenurut\s+skala\b',
    r'\b[Ss]kala(?:nya)?\s+(?:yang|kiri|kanan|tegak(?:nya)?|waktu|kotak|sepuluh'
    r'|hidup|kota|Bumi|ini|itu|seluruh|magnitudo|intensitas|tidak)\b',
    # laut: the compass points "timur laut" / "barat laut" (north-east,
    # north-west), not the sea
    r'\b(?:[Tt]imur|[Bb]arat)\s+laut\b',
    # benua: "the Americas" (English never links it)
    r'\b[Bb]enua\s+Amerika\b',
    # kutub: "polar regions" (English "polar" is an adjective, never linked)
    r'\b(?:daerah|wilayah|bukan)\s+kutub\b',
    # pasir: sandstone, a rock (English "sandstone", one word)
    r'\b[Bb]atu\s+pasir\b',
    # badai: a thunderstorm (English "thunderstorm", one word)
    r'\b[Bb]adai\s+petir\b',
    # lumpur: a mudflow (English "mudflow", one word)
    r'\baliran\s+lumpur(?:nya)?\b',
    # relief: the name of a dataset
    r'\brelief\s+ETOPO1\b',
    # hulu: "upstream" (English never links it); the source of a river is
    # "hulu sungai"
    r'\b(?:ke|di)\s+(?:arah\s+)?hulu\b(?!\s+sungai)', r'\barah\s+hulu\b',
    # dataran: a plateau or a lowland ("dataran tinggi/rendah") and a wave-cut
    # platform ("dataran abrasi", g9.4) are not the plain of g1's definition
    r'\b[Dd]ataran\s+(?:tinggi|rendah)(?:nya)?\b', r'\bdataran\s+abrasi\b',
    # hulu angin: "upwind" (g8.5); salju: a snowman (English "snowman", one word)
    r'\bhulu\s+angin(?:nya)?\b', r'\bboneka\s+salju\b',
    # inti: an ice core, not the Earth's core
    r'\b[Ii]nti\s+es\b',
    # mata air: hot springs on the sea floor (English protects hot springs)
    r'\bmata\s+air\s+panas\b',
    # era: the industrial era
    r'\bera\s+industri\b',
    # ketinggian: the height of water in a glass (g8.5 experiment) and the
    # level of a river (g9.2, English "river level"), not an altitude
    r'\bketinggian(?:nya)?\s+(?:yang\s+sama|air(?:nya)?)\b',
    r'\bgelas\s+[AB]\s+ketinggiannya\b', r'\bketinggian\s+(?:normal\s+)?sungai\b',
    # lempeng: plates of algae (coccoliths), a plate of ice, a stone slab
    r'\blempeng-lempeng\s+kecil\b', r'\blempeng\s+es\b', r'\blempengan\b',
]
