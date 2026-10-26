"""Book 2 (High School, grades 10-12) -- pt. Curation only; the rules live in tools/termlink/.

Curated 2026-10-25 by the Book 2 `pt` agent from this edition's own harvest
(`link_defined_terms.py --book 2 --lang pt --terms`) and the frequency and
chapter-set censuses against English (translation_instruction.md). The English
homographs of `book2_en.py` are mirrored where Portuguese has them too:

- olho: the cyclone's eye (g10.05) and "a olho nu", the observer's eye (g10.01,
  g10.02, g11.08, g12.03) -- STOP, as English STOPs "eye".
- fluxo: a flow of water (g10.09) and the net flux of energy (g10.03, g12.10),
  "fusão por fluxo" (flux melting, g12.04) -- STOP, as English STOPs "flux";
  "fluxo de calor" is its own term and still links.
- saturado, saturação; estável, instável: of air (g10.04) and of minerals,
  isotopes, cratons -- STOP, as English; "ar estável", "ar instável" link.
- vulcânica: the adjective is everywhere (gases, arcs, ash) -- STOP, as English;
  the term is reached through "rocha vulcânica".
- armadilha: of oil and gas (g11.09) only; Portuguese has no verb to collide.
Portuguese homographs of its own, each against its target:

- raio: lightning (g10.05), and the radius of the Earth, the Sun's rays and
  the seismic rays (g10.01-03, g11.02, g12.01, g12.06) -- STOP, so it links in
  its defining chapter, where "raio \\qty{665}{km}" (a radius) is protected.
- dique: a dyke (g11.08, sheeted dykes in g11.05) and a river levee (g10.08,
  "Barragens e diques") -- the levee phrases are protected.
- raiz: a mountain root (g12.01) and the square and fourth roots of
  mathematics, and the roots of plants (g10.07) -- protected phrase by phrase.
- dobra: a fold (g12.02) and the verb "dobra" (doubles; bends down) in g10.04
  and g11.06 -- protected.
- brilho: the lustre of a mineral (g11.07) and the brightness of the Sun
  (g12.10), the silky sheen of a phyllite (g12.03) -- protected.
- intermediário: the rock composition (g11.08) and intermediate-depth
  earthquakes (g11.06), the intermediate scenario (g12.10 table) -- protected,
  as English.
- fratura: a mineral's fracture (g11.07) and the fracture zones of the ocean
  floor (g11.05) -- protected.
- oceano profundo: the layer below the thermocline (g10.06), not the deep
  ocean floor -- protected, as English.
"""

STOP = {
    "olho", "Olho", "olho (de um ciclone)",
    "fluxo", "Fluxo", "fluxo (de água)",
    "saturado", "Saturado", "saturação", "Saturação",
    "estável", "Estável", "instável", "Instável",
    "vulcânica", "Vulcânica",
    "raio", "Raio",
}
NO_CAPITAL = set()
EXTRA = {
    # g12 climate-change: the chapter uses the short forms of its terms, as English
    "forçamento": "def:g12:climate-change:forcing",
    "forçamentos": "def:g12:climate-change:forcing",
    "retroalimentação": "def:g12:climate-change:feedback",
    "retroalimentações": "def:g12:climate-change:feedback",
    "cenário": "def:g12:climate-change:scenario",
    "cenários": "def:g12:climate-change:scenario",
    "sensibilidade climática": "def:g12:climate-change:ecs",
    # g12 past-climates: the chapter says "indicador" for short, as English
    # says "proxy" (the defined phrase is "indicador indireto")
    "indicador": "def:g12:past-climates:proxy",
    "indicadores": "def:g12:past-climates:proxy",
    # phrasings of the text that put a word inside the defined phrase
    # (English: "mean denudation rate", "half spreading rate")
    "taxa média de denudação": "def:g12:destruction-of-mountains:denudation",
    "semitaxa de expansão": "def:g11:drift-to-spreading:spreading-rate",
    # "saturado" is STOPped (so linked in g10.04 only) and DERIVED cannot reach
    # a STOPped base: the feminine "parcela saturada" occurs in g10.04 only
    "saturada": "def:g10:why-clouds-form:humidity",
    "saturadas": "def:g10:why-clouds-form:humidity",
}
DROP = set()
DERIVED = {
    # feminine forms (rocha félsica, lava máfica) and the plurals the tail
    # "(?:e?s)?" cannot make (-al -> -ais, -ão -> -ões)
    "félsico": ["félsica", "félsicas"],
    "máfico": ["máfica", "máficas"],
    "intermediário": ["intermediária", "intermediárias"],
    "porfirítica": ["porfirítico", "porfiríticos", "porfiríticas"],
    "fenocristal": ["fenocristais"],
    "período glacial": ["períodos glaciais"],
    "ciclo glacial": ["ciclos glaciais"],
    "interglacial": ["interglaciais"],
    "formação ferrífera bandada": ["formações ferríferas bandadas"],
    "falha normal": ["falhas normais"],
    "argilomineral": ["argilominerais"],
    "ciclone tropical": ["ciclones tropicais"],
    "intrusão": ["intrusões"],
    "vazão": ["vazões"],
    "raiz": ["raízes"],
    "anticlinal": ["anticlinais"],
    "sinclinal": ["sinclinais"],
    "xisto azul": ["xistos azuis"],
    "mineral índice": ["minerais índice", "minerais índices"],
}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"

EXTRA_PROTECT = [
    # raio: a radius in the defining chapter (g10.05)
    r'\braio\s+\\qty\b',
    # dique: the river levees of g10.08
    r'\bBarragens\s+e\s+diques\b', r'\\emph\{dique\}',
    r'\b[Ee]ntre\s+(?:os\s+)?diques\b', r'\b[Ss]em(?:\s+|\\\\)diques\b',
    r'\b[Cc]om\s+diques\b', r'\bdos\s+diques\s+fica\b',
    r'\bos\s+diques\s+resistirem\b', r'\(b\)\s+diques\b',
    # raiz: mathematics and plants
    r'\braiz\s+(?:quadrada|quarta|cúbica)\b',
    r'\b[Uu]ma\s+raiz\s+(?:libera|troca|o\s+obtém)\b', r'\{raiz\}', r'\bpela\s+raiz\b',
    r'\bficam\s+as\s+raízes\b', r'\bas\s+raízes\s+(?:---|e\s+os\s+decompositores)',
    # dobra: the verb
    r'\bse\s+dobra\b', r'\bdobra\s+a\s+água\b',
    # brilho: the Sun's brightness, a silky sheen
    r'\bbrilho\s+(?:do\s+Sol|sedoso)\b',
    # intermediário: earthquake depth, the scenario table
    r'\bterremotos\s+intermediários\b', r'&\s*intermediárias\s*&',
    # fratura: the fracture zones of the ocean floor
    r'\bzonas?\s+de\s+fratura\b',
    # fratura: the fractures of a rock (weathering, g11.08)
    r'\bpelas\s+fraturas\s+e\s+alargando\b',
    # oceano profundo: the deep ocean floor (bathymetry)
    r'\bfundo\s+do\s+oceano\s+profundo\b',
    # proper names: the Last Interglacial (an AR6 reference period), the
    # Glarus and McConnell thrusts (named faults), the series' region
    r'\bÚltimo\s+Interglacial\b', r'\bcavalgamento\s+de\s+(?:Glarus|McConnell)\b',
    r'\bColinas\s+de\s+Varden\b',
    # the bold Part headings of a weekend problem: the shared rule matches the
    # English word "Part" only
    r'\\textbf\{Parte\s+[IVX]+\b(?:[^{}]|\{[^{}]*\})*\}',
    # run-in paragraph headings stay unlinked, like section titles
    r'\\paragraph\{[^{}]*\}',
    # \pageref and inline \tikz, as in English
    r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
]
