# Translation score — Earth and Space Sciences Book 2 · Spanish (`es`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 2 (High School, Years 10–12) |
| **Language** | Spanish (`es`), peninsular |
| **Quality bar** | **native academic prose of a Spanish *Bachillerato* textbook** (*Biología, Geología y Ciencias Ambientales*, *Geología y Ciencias Ambientales*, *Ciencias de la Tierra*): the impersonal *se* in the course text, the *tú* imperative in every exercise stem, and the vocabulary of Spanish university geology where the book reaches it. English is the source of truth for content, structure, labels, numbers, mathematics and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); the Spanish Book 1 of this series (`parts/grade-*/es/`, `translation_scores/book_1/es/`) for every convention it settled; the shipped Spanish editions of One Physics Book 2–3, One Chemistry Book 1–2 and One Biology Book 2 for typography and settled vocabulary; the Spanish versions of the IPCC AR6 summaries for the calibrated likelihood and confidence language |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-25 |
| **Scope of this pass** | A full first translation, drafted directly at native register through `tools/id_apply.py`, with no machine draft: 28 chapters + 28 solution twins = **56 files**. Also: `frontmatter/image-credits-book2.es.tex` (the frame and every item); a curated `tools/term_config/book2_es.py`; the defined-term link layer; Spanish index keys with ASCII sort keys; a check of every figure page at 110 dpi (zoomed at 250 dpi where a collision was suspected); and this score. The entry file's `\bookline` / `\author` lines were already right (*Libro 2: Bachillerato – Años 10 a 12*) |

## Verdict in one line

This Spanish Book 2 reads as one Spanish *Bachillerato* course in Earth and
space sciences, from the habitable planet and the oceans (year 10) through
plate tectonics, minerals and rocks (year 11) to mountains, deep time and
climate (year 12):

- the impersonal *se* and the *es … que* definition of Spanish textbooks;
- the *tú* imperative in every exercise stem (*Calcula* 179, *Explica* 43,
  *Da* 27, *Comprueba* 20, *Halla* 17, …), with 0 *usted / ustedes /
  vosotros* forms;
- inverted question marks throughout (¿ 960 = ? 960 outside comments);
- the IPCC's own Spanish calibrated language (*muy probable*, *confianza
  alta*) in the climate chapter.

Every structural, prose and link gate is green for all three years. A forced
build gives **0 errors / 0 undefined / 0 overfull**, nullfont 3291 (the
English baseline), 0 missing characters and 0 invalid-in-math, over
**375 pages** (English 362), with **56/56** files in the `.fls`.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | The edition mirrors English exactly. Counted over all 56 files against their 56 twins, these counts all equal English: **420 `exercise`**, **28 `problem`**, **448 `solution`**, **84 `[resume]`**, **205 `omfigure`**, **141 `tikzpicture`**, **104 `axis`**, **100 `\includegraphics`**, **371 `\emph`**, **219 `\index`**, **764 `\label`**, **752 `\item`**, **658 `\node`**, **132 `\cref`**, **3686 `\qty`**, **141 `\ce`**, **74 `\foreach`**, **561 `% ledger:`**. Per environment, also equal: **141 `definition`**, **43 `example`**, **14 `remark`**, **28 `recall`**, **1 `inthefield`**, **1 `inthelab`**, **12 `history`**, **34 `method`**, **58 `proposition`**, **38 `proof`**, **5 `dated`**, **2 `safety`**. Every file went through `tools/id_apply.py`, so every unnamed line is byte-identical to English. One count differs on purpose: `\shortstack` 0 → 11, used to break long Spanish table headers and figure labels onto two lines (overfull and collision fixes, below). The solution numerics of the two climate chapters were re-done by hand; no discrepancy |
| Terminology | **96** | One Spanish word per notion across the three years. **Atmosphere and ocean:** *efecto invernadero*, *balance energético*, *albedo*, *temperatura de equilibrio*, *termoclina*, *afloramiento* (upwelling; the outcrop sense is *afloramiento* too and is masked from the link layer), *giro*, *corriente de contorno occidental*, *borrasca*, *ciclón tropical*. **Solid Earth:** *litosfera / astenosfera*, *Moho*, *onda de cabeza*, *ángulo crítico*, *dorsal*, *zona de subducción*, *losa* (slab), *tirón de la losa / empuje de la dorsal*, *cuña del manto*, *frente volcánico*, *arco insular*, *ofiolita*, *sutura*, *manto de corrimiento*, *cabalgamiento*, *falla inversa*, *isóstasia* written *isostasia*, *rebote isostático*. **Rocks and minerals:** *exfoliación* (cleavage), *dureza*, *roca plutónica / volcánica*, *félsica / máfica / intermedia*, *dique / filón capa / plutón*, *batolito*, *granodiorita*, *isógrada*, *mineral índice*, *grado metamórfico*, *esquistosidad*, *corneana*, *aureola*. **Resources:** *roca generadora* (source rock; *roca madre* would read as parent rock), *roca almacén*, *roca sello*, *trampa*, *ventana del petróleo*, *querógeno*, *migración*. **Time and climate:** *isócrona*, *sistema cerrado*, *edad de la Tierra*, *formación de hierro bandeado*, *Gran Evento de Oxidación*, *capas rojas*, *testigo de hielo*, *neviza*, *inlandsis*, *indicador indirecto* (proxy), *análisis polínico / diagrama polínico*, *Último Máximo Glacial*, *forzamiento radiativo*, *retroalimentación*, *sensibilidad climática de equilibrio*, *escenario de emisiones*, *atribución*. Index keys: 219 = 219; every non-ASCII key carries an ASCII sort key (`querogeno@querógeno`), so the index sorts in Spanish order |
| Fluency / native feel | **96** | Definitions use the *es … que* pattern (*Un \emph{cratón} es un núcleo antiguo y estable de un continente*). Inversions and subordinate clauses follow Spanish order, not English (*Donde la corteza se comprime estando fría y frágil, se rompe a lo largo de fallas de un tipo distinto*). Correlatives are idiomatic (*Cuanto más empinada es una cuenca, más deprisa se erosiona*). Long English noun stacks are unpacked into Spanish prepositional phrases (*la producción de calor radiogénico de una roca*). There are no calqued possessives and no *siendo* gerunds of result |
| Register | **96** | Course text: the explanatory *se* and the occasional first-person plural of a Spanish teacher (*Tomemos el modelo más sencillo que lo expresa*). Exercises: the *tú* imperative. Data credits in full Spanish sentences (*Datos: catálogo de terremotos del USGS; límites de placas de Bird (2003)*). Climate: observation and physical science only; the IPCC calibrated terms in their official Spanish form, in italics as English has them; no policy wording |
| Term-link layer | **96** | **2168 links** (English **2185**) over **138 distinct targets** (English **134**). **No English target is missing.** The four es-only targets are all reached in the right sense: `def:g11:drift-to-spreading:anomaly` (1), `def:g11:fossil-fuel-geology:migration` (4), `prop:g11:lithosphere-asthenosphere:airy` (1), and `def:g11:subduction-zones:slab-pull` (1, *el tirón de la losa que se hunde* = English's *the pull of the sinking slab*, a noun phrase in the defined sense, not the verb phrase English now protects). The dry run reports *links to insert: 0*. The frequency differences are explained under "Curation" below |
| Figures | **95** | Every figure page was rendered and read. Label collisions or overruns caused by longer Spanish labels were found and fixed in: g11/06 (dip labels on the fit line), g11/09 (oil-window labels; one clipped at the axis), g12/01 (ytick label causing a 7.8 pt overfull), g12/04 (*corteza continental* against *plutones*; *la peridotita seca empieza a fundirse* against the pressure axis), g12/06 (continental-mean label past the axis), g12/07 (two isochron slope labels over the y axis), g12/08 (*el Fe²⁺ sube* over a particle dot), g12/09 (*Plataforma de la Sonda* against the rotated *Pen. Malaya*; the CO₂ label across the y axis; two table headers, overfull). Each fix was made in both the edition file and its patch, and re-checked on the final build. Minor overlaps that English has in the same place were left as English draws them |

## Curation of `tools/term_config/book2_es.py`

The two censuses (per-target frequency and chapter set, against English)
found these Spanish homographs, each masked by `STOP` or `EXTRA_PROTECT`:

* **rayo** is a seismic ray in the harvested definition and also lightning
  and any light ray; the seismic sense never needs a link in running text
  that English does not have, so *rayo / rayos* are in `STOP` (27 wrong
  links before).
* **flujo** is the defined flux and also any flow (*flujo de lava*,
  *flujo de agua*); `STOP` on the bare word, the multi-word *flujo de
  calor* still links.
* **reserva(s)** is a reservoir (carbon cycle) and also *reservas* of a
  resource; `STOP`.
* **estable / inestable / saturado / saturación / estratificación /
  estratificado** are atmospheric-stability terms that Spanish also uses in
  their everyday and geological senses (*estratificación* of rock layers);
  `STOP`.
* **afloramiento** is upwelling and also a rock outcrop; `STOP`.
* **brillo** is brightness (astronomy) and also the lustre of a mineral;
  `STOP`.
* **volcánica** on its own is mostly *ceniza volcánica*, *actividad
  volcánica*; `STOP` on the bare feminine adjective, *roca volcánica* still
  links.
* **ojo** (eye of a cyclone) is also the everyday eye; `STOP`.
* **raíz** is the crustal root and also a square / fourth / cube root;
  `\braíz\s+(?:cuadrada|cuarta|cúbica)\b` is protected.
* **fractura**: *por las fracturas* (cracks in rock) is protected.
* **intermedia(s)** is the composition class but also *muestras
  intermedias* and a table column; both protected.
* **Último Interglacial** is a proper name of an IPCC reference period, not
  the defined *interglacial*; protected.
* **Morphology.** `EXTRA` adds the feminine composition adjectives (*máfica,
  félsica, intermedia* and plurals), the plural *formaciones de hierro
  bandeado*, the short forms the climate chapter uses (*forzamiento*,
  *retroalimentación*, *escenario*, *sensibilidad climática*), and the
  plurals *filones capa* and *plutones*, which the shared morphology does
  not derive.

Residual frequency differences, all deliberate:

* **thunderstorm** 2 against English 12: *tormenta* is generic Spanish for
  any storm, and it is the genus inside the definition itself (*una
  tormenta eléctrica es una tormenta…*); only *tormenta eléctrica* links.
* **cleavage** 25 against English 1: an **English** linker gap. English
  harvests only the capitalised *Cleavage* (from the definition head), so
  lowercase *cleavage* never links in English; Spanish *exfoliación* links
  wherever the mineral property is meant.

## `!draw` opt-outs

Each opt-out is translatable label text inside drawing code that the draw
census cannot blank, or a node option or coordinate changed to fit Spanish
text. Each figure was checked on the rendered page. The ranges, in English
line numbers, are:

| File | Ranges |
|---|---|
| grade-10/02 | 133–134, 299 |
| grade-10/03 | 226–229 |
| grade-10/05 | 58 |
| grade-11/06 | 124–125, 133–134 |
| grade-11/08 | 153, 162–169 |
| grade-12/01 | 122 |
| grade-12/05 | 272 |
| grade-12/06 | 286–288 |
| grade-12/09 | 279 |

The draw census finds differences in four files, all of them words inside
node text (*circle*, *arc* in a node label), and 0 differences outside
nodes.

## Conventions recorded

These follow the Spanish Book 1 wherever it settled a question; the
departures and the new decisions are:

* **Cross-references to Book 1** are written *(Libro 1, año 7)*, matching
  the *Años 10 a 12* of the book line (37 uses).
* **IPCC acronyms** (PETM, EECO, MPWP, LIG, LGM, MH; SSP1-1.9 …) are kept
  as the IPCC prints them, also in its Spanish reports; the caption says
  *Siglas en inglés del IPCC* and expands each one in Spanish (*Máximo
  Térmico del Paleoceno–Eoceno*, …).
* **Calibrated language**: the IPCC's Spanish terms, in italics —
  *prácticamente seguro*, *extremadamente probable*, *muy probable*,
  *probable*, *tan probable como improbable*, *improbable*, *muy
  improbable*; *confianza muy baja … muy alta*, written after the noun
  (*confianza alta*).
* **Proxy** is *indicador indirecto*; **ice core** *testigo de hielo*;
  **firn** *neviza*; **ice sheet** *inlandsis* (as in Book 1).
* **Source rock** is *roca generadora*, not *roca madre*.
* **LGM** is *Último Máximo Glacial*, capitalised as a proper period name.
* **Decimal point** kept in prose, as Book 1 does, for consistency with
  siunitx.
* **`\shortstack`** is used to break a long Spanish label or table header
  where English fits on one line; it keeps the drawing code identical.
* **Units inside `\unit`** stay as English writes them (*mm/yr*, *Myr*):
  no words or non-ASCII inside `\qty` / `\unit` / `\num`.

## Samples (Spanish, with verdict)

1. **Year 12, the continental crust.** «Los continentes son más grandes que
   las tierras emergidas.» → **Native.** A short thesis
   sentence as a Spanish textbook opens a section.
2. **Year 11, subduction.** «Las placas se mueven más deprisa cuando de
   ellas cuelga una losa: el tirón de la losa que se hunde es la fuerza más
   intensa que mueve las placas, como concluyeron Forsyth y Uyeda.»
   → **Native.** Fronted adverbial clause, *cuelga* before its subject.
3. **Year 12, mountain building.** «Un manto de corrimiento puede
   transportar rocas formadas muy lejos, incluso láminas de fondo oceánico;
   él mismo puede estar plegado, con sus capas invertidas.» → **Native.**
   The Spanish tectonics vocabulary (*manto de corrimiento*, *láminas*).
4. **Year 12, early Earth.** «La radiactividad era más intensa en el
   pasado. Cada isótopo se desintegra, así que hace mucho había más: un
   periodo de semidesintegración atrás, el doble, y el doble de calor.»
   → **Native.** A verbless Spanish ellipsis where English has a full
   clause.
5. **Year 12, climate.** «Una proyección no es una predicción: dice lo que
   ocurriría \emph{si} el escenario se cumpliera.» → **Native.**
   Conditional with the imperfect subjunctive.

No sample in the edition reads as machine translation. The draft was
written in Spanish against the English twin, range by range.

## Why not 100

* **Hyphenation patterns are English.** As in Book 1, this TeX Live has no
  `spanish.ldf`, so Spanish is hyphenated with English patterns. Most
  prose breaks are acceptable; not all fall on Spanish syllables.
* **`!draw` opt-outs** (above): in those ranges only the rendered page
  guards the figure.
* **Figures at 110 dpi.** Pages were read at 110 dpi, zooming only where a
  collision was suspected; a hairline overlap that English also has was
  left as English draws it.
* **Term-link density on *tormenta***: deliberately conservative (above).
* **Decimal point in prose**, kept for consistency with siunitx.

## Coordinator amendments

- 2026-10-26: g11 solutions/08 answer 16 rewritten by the coordinator after an English canon fix (reported by hi): ≈ 950 days, 2.6 years, within the intrusion range, not "between the two". Gates for grade 11 re-run, green; linker dry run 0.
- 2026-10-26: g11/01 "Motonari" → "Motonori" Matuyama, and the g12/02 fold-shortening chart labels (Varden label no longer clipped, 13 % label moved below-right of its point), both English-canon fixes after the Arabic report; mirrored by the coordinator.
