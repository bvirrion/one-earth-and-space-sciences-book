# Translation score — Earth and Space Sciences Book 1 · Spanish (`es`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 1 (Primary and Middle School, Years 1–9) |
| **Language** | Spanish (`es`), peninsular |
| **Quality bar** | **native school prose at every level**: a Spanish children's book read aloud in the first years (Lena and her window), a Spanish *Ciencias Naturales* textbook in the middle years, and a Spanish ESO *Biología y Geología* / *Geografía* book in the last three. English is the source of truth for content, structure, labels, numbers, mathematics and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); the shipped Spanish editions of One Biology Book 1 and One Chemistry Book 1 (`../one-biology-book/parts/*/es/`, `../one-chemistry-book/parts/*/es/`) for typography (``…'' quotes, `---` incisos and dialogue dashes, the *tú* imperative in exercise stems) and settled vocabulary |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-25 |
| **Scope of this pass** | A full first translation, drafted directly at native register with no machine draft: 32 chapters + 32 solution twins = **64 files**. Also: `frontmatter/preface.es.tex` and `frontmatter/image-credits.es.tex`; the `\bookline`/`\author` lines of the entry file (*Libro 1: Primaria y secundaria – Años 1 a 9*); the aside-box block of `styles/lang/es.tex` (*Lo que ya sabes*, *Sobre el terreno*, *En el laboratorio*, *Historia*, *Seguridad*, *Datos de*); a curated `tools/term_config/book1_es.py`; the defined-term link layer; Spanish index keys with ASCII sort keys; a 130-dpi check of every figure page; and this score |

## Verdict in one line

This Spanish Book 1 reads as one Spanish school course in Earth sciences from
the first year to the ninth:

- short *tú* sentences and dialogue dashes for six-year-olds;
- the impersonal *se* of the ESO textbook;
- the *tú* imperative in every exercise stem;
- inverted question marks throughout (¿ 1026 = ? 1026);
- Spanish exonyms and the compass N E S O.

Every structural, prose and link gate is green for all nine years. A forced
build gives **0 errors / 0 undefined / 0 overfull**, nullfont 6633 (the
English baseline), 0 non-backtick missing characters and 0 invalid-in-math,
over 339 pages, with 64/64 files in the `.fls`.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | The edition mirrors English exactly. Counted over all 64 files against their 64 twins, these counts all equal English: **370 `exercise`**, **20 `problem`**, **390 `solution`**, **40 `[resume]`**, **234 `omfigure`**, **161 `tikzpicture`**, **73 `axis`**, **120 `\includegraphics`**, **455 `\emph`**, **237 `\index`**, **816 `\label`** (set diff **0 / 0**), **468 `\item`**, **834 `\qty`**, **588 `% ledger:`**, **150 `\foreach`**. Per environment, also equal: **140 `definition`**, **60 `example`**, **24 `remark`**, **30 `recall`**, **7 `inthefield`**, **9 `inthelab`**, **10 `history`**, **42 `method`**, **4 `proposition`**, **2 `dated`**, **7 `safety`**. Every file went through `tools/id_apply.py`, so every unnamed line is byte-identical to English. Two counts differ on purpose. `\node` is 677 → 741: label text that English pulls from figdata tables is written as inline nodes inside `!draw` ranges. `\cref` is 103 → 105: in two places Spanish writes *El \cref* where English writes `\Cref`. A scripted per-file **number census** finds no numeric difference except where Spanish writes a number another way: *12 000 millones*, *6000 millones*, *siglo XIX*, *crecida de cien años*. Exercise-part and solution-part structure: 0 mismatches |
| Terminology | **96** | One Spanish school word per notion across the nine years. **Weather and climate:** *el tiempo* (weather) / *el clima*, *borrasca* and *anticiclón*, *isobara*, *frente frío / cálido / ocluido*, *masa de aire*, *previsión meteorológica*, *pluviómetro*, *veleta*, *climograma*, *gradiente térmico vertical*, *brisa marina / terrestre*, *alisios*, *vientos del oeste*. **Solid Earth:** *placa tectónica*, *límite divergente / convergente / transformante*, *dorsal*, *fosa*, *punto caliente*, *cámara magmática*, *boca eruptiva*, *flujo piroclástico*, *hipocentro / epicentro*, *sismómetro / sismograma*, *magnitud / intensidad*, *corteza, manto, núcleo externo / interno*. **Water:** *nivel freático*, *acuífero*, *manantial*, *pozo*, *infiltración*, *escorrentía*, *llanura de inundación*, *crecida de cien años*. **Ice:** *inlandsis* (not *casquete glaciar*, which is the smaller ice cap), *plataforma de hielo*, *glaciación*, *valle en U*, *morrena*. **Geological time:** *principio de superposición / intersección / inclusión / sucesión faunística*, *discordancia*, *escala de tiempo geológico*. **Maps:** *curva de nivel*, *equidistancia*, *curva maestra*, *cota*, *escala numérica / gráfica*, *rosa de los vientos*, *meridiano de origen*, *huso horario*, *línea internacional de cambio de fecha*. **Resources:** *yacimiento mineral*, *factor de concentración*, *áridos*, *reservas*. Index keys: 237 = 237 per file. The keys identical to English are true cognates (*lava, delta, mineral, magma, tsunami, iceberg, permafrost, karst, era, placer, permeable, impermeable*); 0 broken keys |
| Fluency / native feel | **96** | Openings are written as a Spanish teacher would tell them (*Es muy temprano. Lena se despierta, se sube a la silla que hay junto a la ventana de su cuarto y mira fuera.*). Definitions use the *es … que* pattern of Spanish textbooks. Correlatives are idiomatic (*Cuanto más hondo, más denso.*). There are no calqued possessives and no English word order in subordinate clauses. Register count: 0 *usted / ustedes / vosotros* forms and 0 *Calcule / Explique* forms. The *tú* imperatives are *Usa* 36, *Escribe* 20, *Explica* 19, *Mira* 16, *Busca* 16, *Di* 16, *Nombra* 15, *Calcula* 15, … |
| Register gradient | **96** | Grades 1–2: short present-tense sentences, a child character, diminutives used sparingly (*gotitas*). Grades 3–6: the explanatory *se* and second-person invitations (*Mira con una lupa…*). Grades 7–9: ESO-textbook density, with data credits and ledger-backed figures given in full sentences (*Datos: catálogo de terremotos del U.S. Geological Survey*) |
| Term-link layer | **97** | **6084 links** (English 6102) over **137 distinct targets**: all 136 English targets, plus `def:g7:geological-time:time-scale` (1 link, *escala de tiempo geológico* used literally in a later chapter). **No English target is missing.** The linker reports `--check`: *every file matches*, and the dry run reports *links to insert: 0*. The chapter-set census leaves only legitimate residue (*coladas de barro* = mud flows; *precipitación* used once in its everyday sense). The frequency differences are explained under "Curation" below |
| Figures | **95** | Every figure page was rendered at 130 dpi and read. Label collisions in eleven figures were found and fixed, all caused by longer Spanish labels: g5/01 meander section; g6/05 water table and clay pores; g7/02 hotspot chain; g7/04 delta; g7/05 Earth calendar; g8/03 cold front; g8/05 old U-valley; g9/03 coal stages and copper flow; g9/05 hill profile. Each fix was made in both the edition file and its patch, and re-verified on the final build. Figdata tables that carry English text cannot be translated in place (see canon defects), so those labels are written inline under `!draw` |

## Curation of `tools/term_config/book1_es.py`

These are the Spanish homographs, each found by the two censuses:

* **tiempo** is both *weather* and *time*. About forty `EXTRA_PROTECT`
  patterns mask the time sense: *mucho / poco / más tiempo*, *a tiempo*,
  *con el tiempo*, *escala de tiempo*, *eje del tiempo*, *tiempo que tarda*,
  and so on. The weather target therefore has 77 links against English's
  99: English *weather* is never *time*.
* **escala** is both map scale and any other scale (*escala de Mohs*,
  *escala de magnitudes*, *a gran escala*, *a nuestra escala de tiempo*);
  the non-map senses are masked.
* **frente** is a weather front, but also *frente a* (facing), and the
  snout of a glacier or the face of a dune. The non-weather senses are
  masked in the glacier and dune chapters.
* **plano** is both the defined plan (map) and *flat* / *plane*
  (*fondo plano*, *primer plano*, *planos horizontales*).
* **era** is both the geological era and the imperfect of *ser*.
* **longitud** is both longitude and length.
* **globo** is both the globe and a balloon (*globo sonda*).
* **placa** is a plate and also *placa de hielo* (an ice sheet in the
  everyday sense).
* **canto** is a pebble (*canto rodado*) and also *de canto* (on edge).
* **Ecuador** written with a capital letter is the country
  (`NO_CAPITAL`).
* **Proper names** are masked: *Colinas de Varden*, *mar Caspio*,
  *Río de Janeiro*. So are data credits: *costas de Natural Earth*,
  *relieve ETOPO1*.
* **Morphology.** Spanish plurals whose accent shifts are added as `EXTRA`
  entries, because the linker's `WORD_TAIL` cannot generate them:
  *volcanes, inundaciones, erupciones, anticiclones, glaciaciones,
  estaciones meteorológicas, globos terráqueos*. So are the usual synonyms:
  *crecida* and *zona inundable* for flood, *boca* for vent, *giro* for gyre,
  *escala de intensidad*.

## `!draw` opt-outs

Every opt-out follows the documented pattern: translatable text that the
draw census cannot blank. These are table-driven tick labels, `\foreach`
label lists, nodes-near-coords tables, and node options widened to fit
Spanish. Each figure was then checked on the rendered page. The ranges, in
English line numbers, are:

| File | Ranges |
|---|---|
| grade-1/01 | 92–93, 97–98, 122–127, 136–138, 187–189, 204–207 |
| grade-1/02 | 228 |
| grade-3/01 | 104–109 |
| grade-3/02 | 63–67, 77–79 |
| grade-4/01 | 378–383 |
| grade-4/03 | 87–88, 93–95 |
| grade-5/01 | 57–59 |
| grade-5/03 | 168–169 |
| grade-6/01 | 76, 207–208, 219–220, 329–330 |
| grade-6/02 | 251–256 |
| grade-6/03 | 323–324, 328 |
| grade-6/05 | 224–225, 271–273 |
| grade-7/02 | 476–477 |
| grade-7/03 | 342–343, 620–621 |
| grade-7/04 | 163, 322 |
| grade-7/05 | 421–423, 436–444, 510–520 |
| grade-8/01 | 131–133, 209–211 |
| grade-8/02 | 142, 263, 268 |
| grade-8/05 | 263–269 |
| grade-9/01 | 214 |
| grade-9/03 | 77–78, 244–247, 450–458 |
| grade-9/05 | 179–181 |

## Samples (Spanish, with verdict)

1. **Grade 1, opening.** «Es muy temprano. Lena se despierta, se sube a la
   silla que hay junto a la ventana de su cuarto y mira fuera. El cielo está
   gris.» → **Native.** These are read-aloud sentences, with the reflexive
   verbs a Spanish picture book uses.
2. **Grade 6, interior of the Earth.** «Cuanto más hondo, más denso.»
   → **Native.** It renders a whole English sentence as a Spanish verbless
   correlative.
3. **Grade 7, definition.** «Una \emph{falla} es una rotura de las rocas a
   lo largo de la cual los dos bloques situados a cada lado se han
   desplazado uno respecto al otro.» → **Native.** This is ESO-textbook
   phrasing.
4. **Grade 8, ice.** «Una plataforma de hielo o un iceberg ya flotan en el
   mar: ya han desplazado su propio peso de agua.» → **Native.**
5. **Grade 9, risks.** «Se la llama \emph{crecida de cien años}, pero no es
   una crecida que llegue una vez por siglo: puede llegar dos años
   seguidos.» → **Native.** It uses the Spanish hydrological term and the
   subjunctive after a negated antecedent.

No sample in the edition reads as machine translation. The draft was written
in Spanish against the English twin, range by range, and never post-edited
from a machine pass.

## Why not 100

* **English-canon defects** (reported to the coordinator). Several figdata
  tables carry English label text, so Spanish labels had to be written
  inline under `!draw`. `grade-9/solutions/03-earth-resources.tex:111`
  has `\textbf{20 years}` inside a math span. The grade-8 Pedersen
  photograph has English text embedded in the image itself.
* **Hyphenation patterns are English.** This TeX Live has no `spanish.ldf`,
  so `oneearth.sty` builds the Spanish edition without babel, and TeX
  hyphenates Spanish with English patterns. The prose breaks are mostly
  acceptable, but not all of them fall on Spanish syllables.
* **Many `!draw` opt-outs** (above). In each of them, only the rendered page
  guards the figure.
* **Decimal point in prose**, chosen for consistency with siunitx.
* **Term-link density on *tiempo***. Masking the time sense is
  conservative, so a few weather occurrences in time-ambiguous phrasing are
  left unlinked.

## Coordinator addendum (2026-10-25, after wave 1)

Re-verified by the coordinator after the wave-1 canon fixes and tool changes:
- a forced build: 339 pp, 0 errors / 0 undefined / 0 overfull, nullfont 6,633, `.fls` 64 = 64;
- `check_translation.sh` 9/9 PASSED under the stricter gates (per-range `!draw`, the 12-character dup tier, the whole-word tokenizer);
- relinked with the multilingual Part-heading protect: **6071 links**, 138 targets (English's 137 plus the time-scale definition, which English never links), dry run 0. The date-line EXTRA was added by the coordinator, to match English's new EXTRA (5 links).

The coordinator mirrored the canon fixes listed in `sources/WAVE1_FINDINGS.md` §1 into this edition, among them the problem-6 date (**25** March, which reverts the first fix to 26) and the three rainy afternoons. The score is unchanged.
