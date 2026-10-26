# Translation score — Earth and Space Sciences Book 2 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 2 (High School, Grades 10–12) |
| **Language** | French (`fr`) |
| **Quality bar** | **native lycée textbook prose**: a French high-school course in the sciences of the Earth (géologie, océan et atmosphère, climat), clear and precise, no longer the collège voice of Book 1. English is the source of truth for content, structure, labels, mathematics and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); this series' French Book 1 (`parts/grade-{1..9}/fr/`, its score file and `book1_fr.py`) for every convention and every term it owns; the shipped French Biology Book 2 (`../one-biology-book/parts/grade-1{0,1,2}/fr/`) for the lycée register of exercise stems; the French physics and chemistry editions for shared physical and chemical vocabulary |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-25 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 28 chapters + 28 solution twins = **56 files**, every one written through `tools/id_apply.py` from patch files kept in the agent's private directory; `frontmatter/image-credits-book2.fr.tex` (frame and descriptions translated, every credit, author, dataset and licence kept exactly); the entry file's `\bookline` / `\author` (the coordinator's French, kept); a curated `tools/term_config/book2_fr.py`; the defined-term link layer; French index keys with ASCII sort keys; one append-only allow-list entry; this score |

## Verdict in one line

A French Book 2 that reads as one French lycée course in the sciences of the
Earth, continuing Book 1 with its conventions intact (N/E/S/O, spaced
punctuation, guillemets, the GIEC and its calibrated likelihood words, the
decimal point of the series' siunitx setting) and the instruction register of
the French Biology Book 2 (infinitive exercise stems), with every structural
and prose gate green over the three years and a forced build of
**0 errors / 0 undefined / 0 overfull** (numbers below).

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 56 files against their 56 twins: **420 `exercise`**, **28 `problem`**, **448 `\begin{solution}`**, **205 `omfigure`**, **141 `tikzpicture`**, **104 `axis`**, **100 raster includes**, **24 `tabular`**, **371 `\emph`**, **219 `\index`**, **132 `\cref`**, **764 `\label`**, **752 `\item`**, **658 `\node`**, **561 `% ledger:`** comments, **141 `\ce`**, and per environment **141 `definition`, 58 `proposition`, 38 `proof`, 1 `theorem`, 34 `method`, 43 `example`, 14 `remark`, 28 `recall`, 1 `inthefield`, 1 `inthelab`, 12 `history`, 5 `dated`, 2 `safety`** — all equal to English. `\qty` is 3,685 against 3,686: the canon's unit-less `\qty{35} to \qty{40}{km}` (g12/02 l. 511, reported) is written *de 35 à \qty{40}{km}* because `\qty{35} à` crashes the build (siunitx reads *à* as the unit) |
| Terminology | **96** | French lycée geology and climate vocabulary, consistent across three years and with Book 1: *ellipsoïde de référence, aplatissement, géodésie, triangulation*; *température d'équilibre, albédo, insolation, bilan énergétique, chaleur latente/sensible*; *humidité relative, point de rosée, gradient adiabatique sec, niveau de condensation, air stable/instable*; *orage, éclair, tornade, cyclone tropical, œil, mur de l'œil, onde de tempête, échelle de Saffir–Simpson*; *thermocline, halocline, pycnocline, couche de mélange, remontée d'eau*; *saprolite, latérite, hydrolyse*; *bassin versant, débit, débit de base, hydrogramme, période de retour*; *stock, flux, temps de résidence*; *aimantation rémanente, inversion magnétique, expansion des fonds océaniques*; *onde P/S, onde conique, distance de croisement, hodochrone, Moho, zone d'ombre, zone à faible vitesse*; *isostasie (d'Airy), profondeur de compensation, lithosphère, asthénosphère, géotherme*; *panneau plongeant, traction du panneau plongeant, poussée à la dorsale, zone de Wadati–Benioff, éclogite*; *clivage, cassure, éclat, habitus, lame mince, microscope polarisant*; *roche volcanique/plutonique, mafique/felsique/intermédiaire, phénocristal, porphyrique, dyke, sill, pluton, batholite*; *roche mère, roche réservoir, roche couverture, piège, fenêtre à huile/à gaz, houillification, rang*; *craton, croissance continentale, racine, nappe de charriage, chevauchement, suture, ophiolite*; *métamorphisme de contact/régional, auréole, schistosité, foliation, minéral index, isograde, polymorphe, degré métamorphique*; *fusion hydratée, arc volcanique, avant-arc, arrière-arc*; *taux de dénudation, charge de fond/en suspension/dissoute, diagenèse, rebond isostatique*; *flux géothermique, production de chaleur radiogénique, refroidissement séculaire, convection mantellique*; *système clos, isochrone (fém.), âge de la Terre*; *dégazage, atmosphère primitive, paradoxe du jeune Soleil faible, stromatolithe, formation de fer rubané, Grande Oxydation, couches rouges*; *archive climatique, indicateur climatique («~proxy~»), carotte de glace, névé, cycle glaciaire, dernier maximum glaciaire, diagramme pollinique*; *forçage radiatif (effectif), rétroaction climatique, sensibilité climatique à l'équilibre, scénario d'émissions, projection, attribution*. All 219 `\index{}` keys in French with ASCII sort keys (`andesite@andésite`); the 25 keys identical to English are words French spells the same (*craton, sill, dyke, subduction, thermocline* …). Place names take French exonyms (*Groenland, mont Saint Helens, monts Hamersley*) |
| Register / tone | **96** | Measured, not assumed. The French Biology Book 2 (same grades) opens its 574 exercise stems with infinitives (*Expliquer* ×48, *Définir* ×21, *Nommer* ×16, *Donner* ×10) and nominal openers; Book 1 fr used the collège 2sg imperative (*Utilise, Nomme, Range*). This edition follows the lycée register of Biology Book 2: *Définir* ×23, *Donner* ×12, *Expliquer* ×9, *Calculer* ×8, *Nommer* ×7, *Ranger* ×6, and nominal openers (*Un/Une …, À partir de …, Dans …, Sur …*); **0** *tu*; two *vous* in questions that ask an opinion (*selon vous*, *Êtes-vous d'accord~?*), as French textbooks do. History narrated in the passé simple; course text in the present with impersonal *on*. Physical science only on climate: no policy wording added |
| Typography | **97** | French spaced punctuation (`~:` `~;` `~?` `~!`) and guillemets `«~…~»`; the decimal point and `\,` thousands kept as the series' siunitx setting does (as Book 1); *million(s) de* agreement; final sweeps: **0** lines ending on an elision apostrophe, **0** prose lines opening on punctuation (the hits are TikZ `.. controls` continuations), **0** dangling hyphens, **0** straight quotes |
| Fidelity / accuracy | **95** | Every course paragraph, proof, worked example, exercise and solution translated against its twin, with every solution re-read against its question in French and recomputed along the rounded path a student follows. Five English-canon slips found and reported, not silently fixed (below). Math spans are byte-frozen: the `\text{}` inside them is translated (*\text{ an}, \text{ par an}, \text{auj}, \text{ à }, \text{glace}, \text{ millions de }*), the units inside `\qty` are not |
| Figures | **94** | Every visible label translated (nodes, legends, tick labels, titles, multi-line `\\` labels); the `\foreach` lists with visible words translated under per-range `!draw` (list below); the one figdata table whose keys reach the page (`grade-10/02`, `symbolic x coords`) kept its ASCII keys with an explicit French `xticklabels`. Ten overfull boxes from longer French labels cleared with a single-chapter probe (two tables and a bar chart shortened, a tikz label shortened to *feldspath K*, a proof paragraph reworded). Not every rendered figure page was re-read one per page at 130 dpi in this pass |
| Links | **95** | **2,263 `\omterm` links on 138 targets** (def 2,222, ex 26, prop 15) against English's **2,208 on 136**: every English target is linked (**0 missing**), plus two English never reaches (below). Dry run: **links to insert: 0**; `--check`: every file matches what the config generates |

## Gates

`bash tools/check_translation.sh grade-N fr` for N = 10, 11, 12: **3 / 3 PASSED**
(structural censuses, duplicate labels, ledger ids, `\ce` freeze and balance,
the twin-comparison prose gate — **no multi-word finding**; the advisory
one-word tier is cognates and proper names only: *Moho, continent, biotite,
gabbro, sillimanite, granite, pluton, sill, dyke, Craton, Suture, Ophiolite,
Attribution, Insolation, Triangulation, Stratification, Brunhes, Matuyama,
Jaramillo, Olduvai, Kelvin 1862, Mauna Kea, Zagros, Himalaya, Proxima b* …).
`bash tools/gates.sh grade-N` for N = 10, 11, 12: **rc 0** each.
`tools/check_orphan_lines.py`: **0** over the edition.
`tools/check_term_display_drift.py`: every multi-display target is
inflection (singular/plural, capital) or one of the several terms a definition
introduces (*stock/flux, roche réservoir/couverture, mafique/felsique/
intermédiaire, sill/dyke/pluton/intrusion* …).
Drawing census (`coord/drawcensus.py fr`): 3 files differ, all in node text,
none in drawing code: `grade-11/04` *circle* 6→5 (the English node *a small
circle* is *un petit cercle*), `grade-11/06` *arc* 2→3 (English *forearc* is
one word, French *avant-arc*), `grade-12/07` *circle* 1→0 (the English node
*ocean sediment (circle)* is *(cercle)*); node counts equal in all three.

Build (`build.sh`, forced `-g`, under the wrapper's memory cap, 23:05,
after the last edit): `grep -ac '^!'` **0**,
`grep -aci undefined` **0**, `grep -ac Overfull` **0**, nullfont **3,291** (the
English baseline), non-backtick "Missing character" **0**, invalid-in-math
**0**; **380 pages**; the `.fls` lists **56** French chapter and solution files
= **56** on disk.

## Conventions recorded

* **Book 1 conventions kept**: N, E, S, **O**; latitudes `\ang{21}~S`;
  spaced French punctuation and guillemets; the decimal point; *au \cref{…}*;
  *(livre~1, année~N)*, *(les livres de physique / de chimie / de biologie)*
  for the sister series; *\section{Exercices}*; *Problème du week-end ---
  …*; *\noindent\textbf{Partie I --- …}*; solution headers
  `\section*{Chapitre \ref{…} --- Titre}` (all 28 checked against the chapter
  titles); *Données~:*; *(domaine public)*; *et ses collègues*; *Illustration
  générée par IA.*; *la région imaginaire de la série*, *données d'exercice*;
  *GIEC*; *Dôme~C*; *calotte glaciaire* (ice sheet), *glaciation* (ice age);
  the Book 1 likelihood words (*très probable, probable* …) and *degré de
  confiance moyen / élevé / très élevé*.
* **Units in prose**: *m/Ma*, *mm/an*, *cm par an*; inside math the frozen
  `\qty` units stay *m/Myr*, *cm/yr*, *mm/yr* (four sites, reported as a tool
  limit). In two tables *Ma* replaces *millions d'années* for width.
* **English acronyms** of climate periods (PETM, EECO …) are kept and glossed
  in the caption as *Sigles anglais*, since French texts use them so.
* **Image credits**: items written *Chap.~N (titre)~: …* with plain chapter
  numbers, where Book 1 used `\ref`; the Chap. 25 item follows the
  coordinator's canon fix (Holmes 1913, 1927; Patterson 1956; USGS).
* **Exercise register**: infinitive stems (lycée), a departure from Book 1's
  collège 2sg imperative, measured against Biology Book 2 (above).

### `!draw` ranges (each checked by eye)

* `grade-10/02-habitable-planet` 133–134 (explicit `xticklabels` for the ASCII
  `symbolic x coords`), 299 (planet names);
* `grade-10/03-earth-energy-budget` 226–229 (surface names of the albedo list);
* `grade-10/05-storms-and-cyclones` 58 (the stage titles);
* `grade-11/08-igneous-rocks` 153–155 (rock names), 162–172 (mineral names;
  colours untouched);
* `grade-12/01-continental-crust` 122 (the *environ 70* point label);
* `grade-12/05-destruction-of-mountains` 272 (`\lab`, `$e$` kept);
* `grade-12/06-internal-heat` 286–288 (*fosse* labels).

## Link layer

`tools/term_config/book2_fr.py` was curated from this edition's own harvest
(234 terms harvested, 245 linkable) and the frequency and chapter-set censuses
against English, with a context read of every flagged site:

* **STOP** (linked only in the defining chapter): *stable/instable/stabilité*,
  *saturé/saturation*, *flux*, *piège*, *volcanique*, *œil*, *aplatissement*
  (as English), and French-only ones: *stock* (a store of heat, g12/07),
  *orage* (French *orage* for the English "storm" of a rainstorm, g10/07–08),
  *éclair* (*crues éclair*, flashes from a pebble), *cassure* (a fault is
  *une cassure*; obsidian's conchoidal fracture).
* **EXTRA**: the climate short forms *forçage(s), rétroaction(s),
  scénario(s), sensibilité climatique* (as English); *indicateur(s)* for the
  proxy (English links "proxy" 9 times); *couverture(s)* for the seal (English
  links "seal" 18 times); *panneau(x)* for the slab (English links "slab"
  everywhere; French shortens *panneau plongeant*).
* **DERIVED**: irregular plurals the shared morphology does not form —
  *cyclones tropicaux, panneaux plongeants, minéraux argileux, minéraux index,
  phénocristaux*.
* **EXTRA_PROTECT**: *par l'intermédiaire*, the *intermédiaires* scenario
  column; *racine carrée/quatrième*; *océan profond de \qty* (an ocean floor's
  depth); *lame mince de magma*; *débit massique*; the three *roche mère* of
  g12/03 (the protolith: English links them to the soil parent rock of g10/07,
  but *nearest-preceding* would send them to the petroleum source rock of
  g11/09 — left unlinked); the sedimentary and cloud *couverture*; *dernier
  interglaciaire*, *chevauchements de Glaris / de McConnell*; the bold *Partie*
  headings.

Targets French reaches that English does not: *anomalie magnétique* (1, a
caption opening *Anomalies magnétiques*) and *isostasie d'Airy* (1, a
caption). Counts above English, each read and in the defined sense: *clivage*
35 vs 24, *orage* 20 vs 12 and *éclair* 15 vs 10 (all in their own chapter),
*migration* 6 vs 4. French has no wrong-sense link at the sites English now
protects: the g11/09 specimen is *une plaque d'argilite* (unlinked) and g12/06
says *la chaleur sort / va du chaud vers le froid* (no link).

## English-canon defects reported

Items 2–3 and the two link items were fixed in the canon by the coordinator
during the run and mirrored here (with the g12/06 solution total 56.6 → 56.7
and the g12/05 comment 51.6 → 55.8 found by other editions).

1. `parts/grade-12/02-mountain-building.tex` l. 511: `\qty{35} to
   \qty{40}{km}` — the first `\qty` has no unit argument, so siunitx takes the
   "t" of "to" as its unit (tonne); it prints right by accident.
2. `parts/grade-12/solutions/04-subduction-magmatism.tex` ll. 129–130:
   `(144.1 - 143.7) × 86.4 ≈ 33 km` — the printed expression gives 34.6 km.
3. `parts/grade-12/solutions/05-destruction-of-mountains.tex` l. 138:
   `29 × ln 10 ≈ 68` — gives 66.8 (68 comes from the unrounded 29.3).
4. `parts/grade-11/09-fossil-fuel-geology.tex` l. 10: "a slab of black shale"
   is linked to the subducting-slab definition (homograph).
5. `parts/grade-11/09-fossil-fuel-geology.tex` l. 221: `\emph{Migration}`
   opens its sentence, so English never links the 20 lowercase "migration"
   (the capitalised-harvest trap the coordinator fixed for "cleavage").

## Coordinator amendments

- 2026-10-26: g11 solutions/08 answer 16 rewritten by the coordinator after an English canon fix (reported by hi): ≈ 950 days, 2.6 years, within the intrusion range, not "between the two". Gates for grade 11 re-run, green; linker dry run 0.
- 2026-10-26: g11/01 "Motonari" → "Motonori" Matuyama, and the g12/02 fold-shortening chart labels (Varden label no longer clipped, 13 % label moved below-right of its point), both English-canon fixes after the Arabic report; mirrored by the coordinator.
- 2026-10-26: three formulas (g12/05:179, g12 solutions/05:102, 108) changed from m/Myr to m/Ma, so the pages no longer mix the two (user question about units); grade-12 gate green, rebuilt 380 pp 0/0/0.
