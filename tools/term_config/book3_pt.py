"""Book 3 (University, Year 1) -- pt. Curation only; the rules live in tools/termlink/.

Curated 2026-10-27 by the Book 3 pt agent from this edition's own harvest, read
against the English twin's term counts (per target), not copied from another
edition. The English homographs of this book are checked in the pt displays:

- "fluxo" / "fluxos": the generic word for heat, sediment and carbon fluxes (70
  and 22 uses) against the flux of a source (English 17 links in all); the flux
  of a source keeps its luminosidade links;
- "ordem" / "Ordem": the ordinary word "order" (95 uses, "de ordem", "em
  ordem") against the order of an interference colour (English 45 links for
  the target in all);
- "estável" / "Estável": stable of a triple junction (39 uses of "estável" in
  the mineral, isotope and water columns) against the stable triple junction,
  which keeps its junção tripla links.
"""

STOP = {"fluxo", "fluxos", "Fluxo", "ordem", "Ordem", "estável", "Estável"}
NO_CAPITAL = set()
EXTRA = {
    # the English twin links these once or twice; the pt text says these phrases
    "modelo de referência": "def:b1:layered-earth:reference-model",
    "rotações finitas": "def:b1:plate-kinematics:finite-rotation",
    # Book 3 pt (2026-10-27): the irregular plural (-al -> -ais) is not derived by
    # the link engine's plural rule, so "minerais" was unlinked (English links the
    # plural 180 times against 101 in pt); "curvas estruturais" is the plural of
    # the defined map term "mapa de curvas estruturais" (English links 7 times).
    "minerais": "def:b1:rock-forming-minerals:mineral",
    "curvas estruturais": "def:b1:cross-sections:structure-contour",
    # the English twin links the geomagnetic polarity timescale once (a figure caption); pt uses the phrase in a method
    "escala de tempo de polaridade": "def:b1:plate-kinematics:magnetic-anomaly",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# Book 3 pt (2026-10-27): homograph collisions measured by the chapter-set census.
# Each pattern masks an ORDINARY sense of a word that is the surface of a defined
# term elsewhere in the book: "direção" (strike) in geology chapters, but direction
# of vibration / propagation / wind / current / motion / toward everywhere else;
# "física mineral" (mineral physics) against the mineral; "clivagem" (mineral
# cleavage) against the slaty cleavage; "seleção" (natural selection) against the
# selection sense; "Sistema Solar" and "sistema fechado / de decaimento" (closed
# isotope system) against the chronostratigraphic system; "declinação magnética"
# against the celestial declination; "massa de ar" in the circulation chapter
# (mass flow) against the air mass of the extinction; "formação comum" (water
# mass) against the lithostratigraphic formation; "Grupo de Trabalho" (IPCC working
# group) against the group; "dobra" as the verb "to double". Lookaheads only:
# nothing here consumes a `$`.
EXTRA_PROTECT = [
    r'(?<!\w)em\s+direç(?:ão|ões)\b',
    r'(?<!\w)direç(?:ão|ões)(?=\s+(?:de\s+(?:vibra|propaga|movimento|espalhamento|campo|vento|ventos|corrente|correntes|fluxo|transporte|onda|ondas|luz|normal|cisalhamento|tensão|força|magnetiza|vetor|escoamento|\$|\\vec|\\mathbf|\\hat|σ|\\sigma|\\lambda|\\theta|\\varphi|\\phi)|do\s+(?:movimento|espalhamento|campo|vento|polo|fluxo|escoamento|transporte|ar)|da\s+(?:corrente|onda|luz|normal|tensão|força|placa|dorsal|extremidade)|dos\s+ventos|lenta|rápida|oposta|principal|principais))',
    r'(?<!\w)física\s+mineral',
    r'(?<!\w)clivagem(?=\s+(?:boa|perfeita|ruim|fraca|ótima|de\s+mineral))',
    r'(?<!\w)seleção(?=\s+(?:das\s+espécies|natural))',
    r'(?<!\w)[Ss]istemas?(?=\s+(?:Solar|fechado|de\s+decaimento|mais\s+usad|usad))',
    r'(?<!\w)declinaç(?:ão|ões)(?=\s+magnétic)',
    r'(?<!\w)massa\s+de\s+ar(?=\s+(?:por\s+segundo|entre\s+o\s+equador|que\s+(?:entra|cruza|sobe|desce|flui)))',
    r'(?<!\w)formação(?=\s+comum)',
    r'(?<!\w)Grupo(?=\s+de\s+Trabalho)',
    r'(?<!\w)(?:quase\s+)?dobra(?=\s+(?:a\s+[\\\w]|e\s+soma|para\s+baixo|enquanto|quase))',
    # Book 3 pt, second pass (2026-10-27), each from the chapter-set census:
    r'(?<!\w)[Gg]rupo(?=\s+(?:de\s+trabalho|de\s+nanofósseis|da\s+platina|propôs|da\s+Subcomissão))',
    r'(?<!\w)[Mm]embros?(?=\s+(?:votantes|não\s+votaram|da\s+Comissão|da\s+subcomissão))',
    r'(?<=ajuste de )declinaç(?:ão|ões)',
    r'(?<=ajuste da )declinaç(?:ão|ões)',
    r'(?<=ajustar a )declinaç(?:ão|ões)',
    r'(?<=ajustada para a )declinaç(?:ão|ões)',
    r'(?<=correção da )declinaç(?:ão|ões)',
    r'(?<=pela )declinaç(?:ão|ões)',
    r'(?<!\w)declinaç(?:ão|ões)(?=\s+(?:mudou|dela|errad|desatualizad))',
    r'(?<!\w)[Ss]érie(?=\s+de\s+(?:lavas|rochas|amostras|dados))',
    r'(?<=da )série(?!\w)',
    r'(?<!\w)[Ss]istemas?(?=\s+(?:é\s+)?(?:Solar|fechado|de\s+decaimento|de\s+previsão|mais\s+usad|usad))',
    r'(?<!\w)rumos?(?=\s+(?:de\s+uma\s+trilha|da\s+trilha|das\s+trilhas|sozinhos|de\s+rumos|menos|é\s+o))',
    r'(?<=ao longo do )rumo(?!\w)',
    r'(?<=perpendiculares ao seu )rumo(?!\w)',
    # Book 3 pt, step 1 (2026-10-27), second batch. "rumo" as "toward" (the
    # radiation leaves the top of the atmosphere rumo ao espaço; the current runs
    # rumo à Europa) and as the trend of a hotspot track (ch15, and its solution):
    # the trend-plunge definition covers a geological line, not a track's azimuth.
    r'(?<!\w)rumo(?=\}?\s+(?:ao|à)\s)',
    r'(?<!\w)rumo(?=\}?\s+de\s+uma\s+trilha)',
    r'(?<=de )rumos(?=\s+diferentes)',
    r'(?<=um )rumo(?=\s+\\ang\{6\.6\})',
    # "extensão" as spatial extent (not strain): ch17, ch21, ch24 (and solution), ch28;
    # the strain, extensional-regime and extension-of-a-line uses stay linked (ch16)
    r'(?<=toda a sua )extensão(?!\w)',
    r'(?<=à )extensão(?=\s+das\s+mudanças)',
    r'(?<=por sua )extensão(?=\s+no\s+Hemisf)',
    r'(?<=a )extensão(?=\s+lateral)',
    r'(?<=Dê a )extensão(?=\s+e\s+a\s+espessura)',
    # "sistema" as a climate system or an ocean gyre (not a chronostratigraphic system)
    r'(?<!\w)[Ss]istemas?(?=\s+climátic)',
    r'(?<=como )[Ss]istema(?!\w)',
    r'(?<=grande )[Ss]istema(?=\s+de\s+correntes)',
    # Book 3 pt, step 2 (drift and sense check, 2026-10-27): the English canon leaves
    # these two phrases unlinked. "ambiente de deposição" is the depositional
    # environment (a different notion from the facies it helps define; the facies
    # definition only indexes it). ("formação de água profunda" is NOT protected: the
    # English twin links deep-water formation to the overturning definition too.)
    r'(?<!\w)ambiente\s+de\s+deposição',
    # the solution to ch29 only: the English solution leaves "deep-water formation" unlinked
    r'(?<=depende da\s)formação\s+de\s+água\s+profunda',
    # step 3: the direction a wind comes from (na direção de onde o vento vem), not the strike
    r'(?<=na )direç(?:ão|ões)(?=\s+de\s+onde\s)',
    # Book 3 pt, step 1 (2026-10-27): "direção" in the ordinary sense (optical
    # vibration / propagation / refraction, wind, pressure-gradient force, plate
    # motion and rotation vectors, coordinate axes, traction, shear, transport)
    # where the strike definition was linked. Each pattern names its context; the
    # strike uses (faults, transform faults, rift and ridge trends) stay linked.
    # ch08 optical mineralogy
    r'(?<=ao longo da sua )direç(?:ão|ões)(?=, de modo)',
    r'(?<=outra )direç(?:ão|ões)',
    r'(?<=cada )direç(?:ão|ões)(?= é o índice)',
    r'(?<=nessa )direç(?:ão|ões)',
    r'(?<=a )direç(?:ão|ões)(?=\s+2\s+é)',
    r'(?<=na )direç(?:ão|ões)(?= do lado de maior índice)',
    r'(?<=uma )direç(?:ão|ões)(?= visível)',
    r'(?<=Em que )direç(?:ão|ões)(?=\s+sua\s)',
    # ch18 earthquakes: slip direction and P-axis directions; ch21: delta progradation
    r'(?<=em que )direç(?:ão|ões)(?= se moveu)',
    r'(?<=em que )direç(?:ões|ão)(?= ela jazeria)',
    r'(?<=Em que )direç(?:ão|ões)(?= geral)',
    # ch12 plate kinematics and the solution to ch12
    r'(?<=esta )direç(?:ão|ões)(?= e este sentido)',
    r'(?<=à direita da )direç(?:ão|ões)(?= em que vê o polo)',
    r'(?<=sua )direç(?:ão|ões)(?= é um dos dados)',
    r'(?<=ao longo desta )direç(?:ão|ões)',
    r'(?<=perpendicular a essa )direç(?:ão|ões)',
    r'(?<=A )direç(?:ão|ões)(?= está próxima dos)',
    # ch13 rifts: dip toward the other fault
    r'(?<=na )direç(?:ão|ões)(?= da outra)',
    # ch16 stress and strain: traction, axes, shear direction, the diagonal
    r'(?<=Sua )direç(?:ão|ões)(?= não é, em geral)',
    r'(?<=a )direç(?:ão|ões)(?= da normal)',
    r'(?<=na terceira )direç(?:ão|ões)',
    r'(?<=paralelamente a uma )direç(?:ão|ões)',
    r'(?<=, a )direç(?:ão|ões)(?= de cisalhamento)',
    r'(?<=que era a )direç(?:ão|ões)',
    # ch20 erosion, ch24 stratigraphy, ch25 radiometric dating
    r'(?<=em qualquer )direç(?:ão|ões)',
    r'(?<=em que )direç(?:ão|ões)(?= ela mudará)',
    r'(?<=da )direç(?:ão|ões)(?= da transgressão)',
    r'(?<=em que )direç(?:ão|ões)(?=, as)',
    # ch28 atmospheric circulation: pressure force, wind, barbs, isobars
    r'(?<=na )direç(?:ão|ões)(?= \$[+-]x)',
    r'(?<=Em que )direç(?:ão|ões)(?= ela aponta)',
    r'(?<=Em que )direç(?:ão|ões)(?=\s+a\s)',
    r'(?<=Em que )direç(?:ão|ões)(?= sopra)',
    r'(?<=De que )direç(?:ão|ões)(?= sopra)',
    r'(?<=girando a )direç(?:ão|ões)',
    r'(?<=a )direç(?:ão|ões)(?= da haste)',
    r'(?<=De que )direç(?:ão|ões)(?=\s+sopraria)',
    # ch29 ocean circulation: wind, Ekman transport
    r'(?<=apenas a )direç(?:ão|ões)',
    r'(?<=Em qual )direç(?:ão|ões)',
    r'(?<=Em )direç(?:ão|ões)(?=\s+à\s+terra)',
]
