# Series definition map --- One Earth and Space Sciences Book

Which book and chapter **owns** each defined term, i.e. carries its
`\emph{term}\index{term}` pair inside a `definition`. Owned by the main
session; book writers read it and never edit it (they report at their sync).

Term links are generated **per book**, so a book can only link a term it
defines itself. The rules:

1. **Books 1 and 2 (grades 1--12) never repeat themselves.** Together they
   follow `OUTLINE.md`, "Notion-ownership map, Books 1--2": one owner chapter
   per notion across the twelve school years. A later chapter, in the same
   book or in Book 2, opens with a `recall` box (Book 1's notions are named in
   prose in Book 2: "as Book 1 showed, in grade 7") and uses the word without
   a new `\emph{}\index{}` pair. Book 2 therefore does not link the Book 1
   words it recalls; that is the price of never re-teaching.
2. **Books 3--5 (Years 1--3)**: each notion has exactly **one owner across the
   three university books** (`OUTLINE.md`, "Years 1--3"). A university book
   may **re-found** a school notion --- define it again, rigorously, in the
   chapter the outline names ("Re-founds" column) --- because the school
   books' definitions do not link inside a university book. It never defines a
   notion owned by another university book: it uses the owner's word with a
   prose pointer ("defined in the Year 1 volume"), never a `\cref`.
3. **Notions owned by another series** (`OUTLINE.md`, "Owned by another series
   (recall, then build)") are never defined here at all: a `recall` box names
   the series in prose ("the physics books show that\dots"), states what is
   used, and the chapter takes the Earth or space angle. Before defining a
   term that sounds like physics, biology or chemistry, grep the sister
   series' harvest (commands below).
4. A term not in any map goes to the **earliest chapter** that needs it: in
   Books 1--2 by grade; across Books 3--5 in the lowest-numbered university
   book. Contested terms are settled at a sync by the main session, and the
   ruling is written below.
5. **Harvester rule** (from the chemistry run): `\index{}` appears only beside
   the `\emph{}` of a term the chapter owns, inside a `definition`, and
   nowhere else. Named laws and models this series owns (Darcy's law,
   Byerlee's law, the Gutenberg--Richter law, Walther's law, Airy and Pratt
   isostasy) may be indexed in their theorem or proposition, owner chapter
   only. Laws another series owns (Snell's law, Hubble's law, Kepler's laws)
   are recalled, never indexed here.

## Harvest commands

The terms the books already written define (multi-line `\emph`/`\index`):

```sh
# this series, one book's years at a time
perl -0777 -ne 'while(/\\emph\{([^}]*)\}\s*\\index\{([^}]*)\}/g){($t=$2)=~s/\s+/ /g; print "$ARGV\t$t\n"}' parts/grade-*/[0-9]*.tex
perl -0777 -ne 'while(/\\emph\{([^}]*)\}\s*\\index\{([^}]*)\}/g){($t=$2)=~s/\s+/ /g; print "$ARGV\t$t\n"}' parts/bachelor-*/[0-9]*.tex
# the sister series (read-only): what they own
for s in physics biology chemistry; do
  perl -0777 -ne 'while(/\\emph\{([^}]*)\}\s*\\index\{([^}]*)\}/g){($t=$2)=~s/\s+/ /g; print "$ARGV\t$t\n"}' \
    ../one-$s-book/parts/*/[0-9]*.tex
done | grep -i '<term>'
```

## Seed (2026-10-22)

The binding seed is `OUTLINE.md`'s three ownership tables, approved by the user
on 2026-10-22. They are not copied here, so that they cannot drift; the syncs
below add only what the tables do not say (terms the briefs found, contested
terms, splits).

Points the outline already settles and every writer must know:

- **Physics owns** (recall, never define): day and night, the Moon's phases,
  seasons and their cause, the Solar System as a list of bodies, stars and
  constellations, air pressure and the barometer, the water cycle as a mass
  balance, eclipses, the light-year, spectra, gravitation and tides,
  geomagnetism (the field itself), P and S waves and their speeds, Kepler's
  laws, radioactive decay and radiometric dating's law, the Coriolis force and
  Foucault's pendulum, the isothermal atmosphere, ocean swell, the heat
  equation and the soil's thermal wave, black-body radiation and the one-layer
  greenhouse model, elasticity, the liquid core from S-wave shadows, the cosmic
  microwave background, the HR diagram and Hubble's law.
- **Biology owns**: the soil as a living system and its horizons, fossils as
  evidence of evolution, mass extinctions, the carbon cycle and the other
  biogeochemical cycles, climate impacts on life.
- **Chemistry owns**: air composition, raw materials and resources as
  substances, greenhouse gases as molecules, element abundances and the iron
  core as chemistry, crystal lattices and silicate units, X-ray diffraction,
  stratospheric ozone chemistry (Chapman), ocean carbonate chemistry.
- **This series owns** everything else in the outline: plate tectonics, the
  rock cycle, minerals as Earth materials, petrology, volcano and earthquake
  mechanisms, stratigraphy and the time scale, the structure and circulation of
  the atmosphere and ocean, weather systems, landforms, past climates and the
  orbital theory of climate, geological maps, spherical astronomy and the five
  astronomy chapters of the outline.

## Sync decisions

(Written by the main session after each Phase A report; binding.)

### Sync 0 (2026-10-22, before launch)

- **fold, anticline, syncline, fold axis**: owned in the university books by
  Y1 `geological-maps` (`def:b1:geological-maps:fold`), because the map
  chapter needs them first. Y1 `faults-folds-fabrics` recalls them and owns
  fold geometry proper (hinge, limb, interlimb angle, axial plane,
  classification). In the school books, g12 `mountain-building` owns folds
  (with collision, nappe, ophiolite, suture); Y1 re-founds them.
- The invented exercise region keeps its name, the **Varden Hills**.

### Sync 1 (2026-10-22): Books 1 and 2

Term rulings (school volumes, earliest grade owns; later grades recall):
- **scale**: g2 `drawing-to-map` defines "scale" (1 square = 1 m, whole
  numbers); g9 `maps-of-the-earth` owns "numerical scale" and "scale bar".
- **ocean, sea**: g2 `water-on-earth` defines them; g3 only names the five
  oceans.
- **cardinal directions**: physics g4 owns the term (it indexes it). Book 1
  g2 explains north, south, east, west in prose and defines **compass rose**
  only (a map object). No `\emph`+`\index` of "cardinal directions".
- **hardness, Mohs scale**: Book 1 g6 `rocks-and-minerals`. Book 2 g11
  `minerals` recalls them and adds cleavage, structure, the silicate
  tetrahedron.
- **crust, mantle, core, outer core, inner core**: Book 1 g6
  `inside-the-earth` (the liquid outer core stated as a fact; its seismic
  evidence and Lehmann's argument belong to g11). Book 2 g11 owns the Moho,
  the core--mantle boundary and the seismic evidence.
- **P wave, S wave**: physics never defines them, so this series does, in
  Book 2 g11 `seismic-structure`. Book 1 g7 `earthquakes` describes "a faster
  wave that arrives first and a slower one" in prose, without defining terms.
- **fault**: Book 1 g7. **normal fault**: Book 2 g11 `ocean-ridges`;
  **reverse fault, thrust**: g12 `mountain-building`.
- **unconformity, seismometer, temperature anomaly, topographic map, contour
  line, contour interval**: Book 1 (g7, g7, g9, g9, g9, g9). Book 2's pilot
  recalls "temperature anomaly".
- **convection cell**: Book 1 g8 (descriptive). Book 2 g12 recalls it and
  defines "mantle convection" only.
- **weathering**: Book 1 g5. **chemical weathering, hydrolysis, clay**:
  Book 2 g10 `soil-formation` (Y1 `weathering-clays` re-founds).
- **environmental lapse rate**: Book 1 g8. **adiabatic cooling, dry adiabatic
  rate**: Book 2 g10.
- **ice age**: Book 1 g8. **glacial period, interglacial**: Book 2 g12
  `past-climates`.
- **exoplanet**: Book 2 g10 `habitable-planet`.
- Every other Phase A claim of Books 1 and 2 is accepted as written in their
  `DEFINITIONS.md` (a mechanical cross-check found only the four collisions
  above). **crystal** is chemistry's: Book 1 defines "mineral" and speaks of
  crystals in prose. **humidity, dew point, residence time** are homographs
  of sister-series terms: link only phrase-level, curate in the term config.

Other rulings:
- Book 2 g10 recalls right-triangle trigonometry (math grade 9 teaches it)
  and may derive the sine rule; fine.
- `tools/fetch_data.py`: each book may append ONE block `# Book <N>:` at the
  end (ownership rule 1); ids start with the year; licence verified and
  recorded; never touch another block.
- Book 1 fixes the g7 pilot's exercise 12 (a lookup, not a ★★★); Book 1 marks
  the rejected first puzzle-map prompt in `PROMPTS.md`.
- Provenance texts that cannot be fetched: note the attempt in
  `PROVENANCE.md` and move on (nothing about them is printed).

Style additions (appended to `styles/oneearth.sty`, rendered at 200 dpi):
- `\omwx[<scale>]{<name>}` inline weather icons and `pic {omwx=<name>}`
  (sun, suncloud, cloud, rain, shower, snow, storm, fog, wind); a 1 x 1 icon.
- `pic {puffycloud}`: a 2 x 1 fair-weather cloud, origin at the middle of
  its flat base.
- `pic {compassrose}`: radius 1, N/E/S/W labels, half-black points.
- Hypsometric palette `omHypsLandA`--`F` (0--200, 200--500, 500--1000,
  1000--2000, 2000--4000, > 4000 m) and `omHypsSeaA`--`D` (0--200,
  200--2000, 2000--4000, > 4000 m deep).
- `lith gabbro`, `lith peridotite`, `lith eclogite` (and `\omlith{...}`).

### Sync 1 (2026-10-22): Book 3

- **lithosphere, asthenosphere**: re-founded in Y1 ch. 9 `layered-earth`
  (seismic structure first); ch. 10--11 recall them.
- **Qualified forms against sister-series homographs** (series rule from now
  on): when physics, chemistry or biology defines a word in another sense,
  this series defines and indexes the qualified Earth form only ---
  "birefringence (of a mineral)", "solid solution (mineral)", "hydrolysis (of
  silicates)", "clay mineral", "weathering" (biology's sense is recalled),
  "sedimentary facies" (Y2 writes "metamorphic facies"), "declination
  (celestial)" (physics g11 owns magnetic declination: always write
  "magnetic declination" in full). The physics tensors, viscosity, Fourier's
  and Stokes' laws and the black-body laws are admitted with a prose pointer.
- **luminosity, annual parallax, parsec, normal gravity, potential
  temperature (ch. 26), reef (geological sense)**: Book 3's. Y3 recalls
  parallax and the parsec in its distance ladder; Y3 keeps the ellipsoid and
  J2.
- **asteroid, comet**: not defined by physics (checked): Book 3 may define
  them unless Book 1 g6 does (check Book 1's `DEFINITIONS.md`, then recall).
- **foliation, schistosity, mylonite**: descriptive definitions in ch. 17;
  mechanisms in Y3 `deformation-mechanisms`; Y2 recalls.
- Re-founded rows marked "(if indexed)" are confirmed against the school
  harvest at verification; write them as definitions now.
- Pilot ch. 4: fix the blank page, gloss "trend and plunge" and "hanging
  wall" at first use; Q18 may stay.
- **Gate 7** narrowed (main session): real places in France may be named;
  only French/France next to a school word fails.
- Units added to the style: `\sverdrup` (Sv), `\gal` (`\milli\gal` = mGal),
  `\mag`.
- Datasets: one `# Book 3:` block in `tools/fetch_data.py`; reanalysis and
  CERES dropped as proposed. Page projection ~366 pp is fine.

### Sync 2 (2026-10-23): Book 4, and a series-wide sourcing ruling

**Sourcing (binding on every book, effective now).** A ledger row whose
source is Wikipedia or Wikibooks (`WIKI*` keys, `wikipedia.org`,
`wikibooks.org`) is NOT sourced. The 2026-10-23 count: Book 1 1 row,
Book 2 ~70, Book 3 ~186. Rules:
- mint no new Wikipedia/Wikibooks rows;
- re-source every existing one before your book lands: fetch the primary
  reference the article cites (paper with DOI, agency page, survey report,
  data release, biography in a society obituary or a museum page) and re-key
  the row to it; for textbook-standard ranges (a Moho depth, a mineral
  proportion) an open textbook or an agency glossary (USGS, NOAA, BGS, NASA,
  an open university-press text) is acceptable;
- if no citable source can be fetched, change the text so that it no longer
  states the number (or drop the sentence), and list it as EXCLUDED;
- the landing check is `grep -iE 'wikipedia|wikibooks|\| *WIKI|wiki:' sources/ledger/book<N>.md | grep -viE 'commons\.wikimedia|wikimedia commons' | wc -l`
  (Wikimedia Commons photo credits are fine, hence the second grep); any hit sends the book back.

**Book 4 term rulings.**
- **δ value, fractionation factor**: chemistry's (b3); recall. Book 4 defines
  only VSMOW/VPDB and the meteoric water line.
- **mineral--melt partition coefficient, compatible element, incompatible
  element, MORB, OIB**: Y2 ch. 3 (qualified form). Y3 keeps batch and
  fractional melting models and recalls these.
- **ternary phase diagram, cotectic line**: Y2 ch. 7. Y3 keeps the phase rule
  and pseudosections and recalls them.
- **Clapeyron slope (of a reaction)**: Y2 ch. 10 (qualified; physics owns
  Clausius--Clapeyron).
- **Rossby wave (descriptive)**: Y2 ch. 22. Y3 owns Rossby number, thermal
  wind and the Rossby-wave dynamics, recalling the term.
- **ice--albedo feedback**: moved to Y2 ch. 18 (first need). Ch. 25 recalls
  it; ch. 27 uses AR6's "surface-albedo feedback" in prose as the same
  mechanism, no second definition. Y3 recalls.
- **Mg/Ca ratio (proxy)**: Y2 ch. 24; "palaeothermometry" stays Y3's.
- **remaining carbon budget**: Y2 ch. 27 (qualified; biology owns "carbon
  budget").
- **disaster risk, geological hazard, exposure (to a hazard)**: Y2 ch. 28
  (qualified; Book 1 owns natural hazard, risk, vulnerability, hazard map).
- **Bowen's reaction series**: Y2 ch. 8.
- **digital elevation model**: Book 3 ch. 4 owns it (the outline's Year-3
  row is superseded); Book 5 recalls it.
- All of Book 4's re-foundings of school terms are accepted.

**Book 4 other rulings.**
- Style additions (appended, rendered): `lith migmatite`, `marble`,
  `quartzite`, `serpentinite`, `tuff`, `rhyolite`, `andesite`, `chert`,
  `banded iron`, `reef limestone`. The skew-T is local to Book 4 (axis option
  in the chapter), no shared style.
- `tools/ai_images.py` no longer falls back to "the newest PNG under
  ~/.codex/generated_images" (it could take another agent's image); a
  private no-fallback copy is no longer needed.
- Book 4 may read `data/derived/bachelor-1-hotspots.csv` (Book 3) read-only;
  it does not use its Wikipedia-derived values until Book 3 re-sources them
  (or derives its own table from Morgan & Morgan 2007 directly).
- Datasets: one `# Book 4:` block; the list in the Phase A report is
  approved (CC BY sets credited).

### Sync 3 (2026-10-23): Book 5

- **Phase rule:** chemistry b2 owns the variance and the phase-rule theorem;
  Y3 ch. 11 recalls them and defines only the *mineralogical phase rule*
  (Goldschmidt) and the *pseudosection*. (Sync 2's "Y3 keeps the phase rule"
  meant the topic, not the definition.)
- **Walther's law:** Y3 ch. 17 `facies-models` owns it (theorem). Book 4
  ch. 20 uses it in prose with a pointer to the Year 3 volume and defines
  nothing under that name.
- **Stereographic and equal-area projection (of the sphere):** Y3 ch. 8.
  Book 3 ch. 18 (~line 475) must say "the Year~3 volume", not Year 2 (Book 3
  agent fixes it in its own file).
- **Re-derived owned notions** (Ekman solution, AFC, depth--age law, normal
  gravity, Rossby wave): derived in a theorem with no `\index` and no
  definition; the term links to its owner. "Rossby-wave dispersion relation"
  may be indexed under that full name.
- **Not re-founds:** magnetostratigraphy, Darcy's law, Glen's flow law and
  radar interferometry are new in Y3 (the school books never name them);
  OUTLINE map corrected. Reference ellipsoid is re-founded from g10.
- **Qualified forms approved:** saturation index (of a mineral), planetary
  habitability, Jeans escape, tectonic underplating, exsolution (mineral),
  fold (of seismic coverage), seismic migration, equal-area projection (of
  the sphere), intrinsic permeability, retardation factor (sorption), magnetic
  inclination.
- **Book 5 defines** cosmogenic nuclide, shear zone and standard candle (no
  owner indexes them); Book 3 must not add definitions of these terms.
- **Heat equation:** physics indexes it as "diffusion equation"; recalls name
  it so ("the diffusion equation, here for heat").
- **Style (appended `% Sync 3 (Book 5)` block):** pgfplots `groupplots`
  library loaded; `\Msun`, `\Mearth`, `\Rearth`, `\Mjup`, `\Rjup`; siunitx
  `\dex`, `\darcy`. No stereonet pic: Book 5 draws it from figdata.
- **Datasets approved** for one `# Book 5:` block: IGRF-14, USGS Spectral
  Library v7 (fallback ECOSTRESS), NASA Exoplanet Archive PSComp, Eilers et
  al. 2019 (VizieR), Asplund et al. 2021, NSIDC Sea Ice Index (optional).
  **Ice-mass series: IMBIE open tables only** --- no source that needs an
  Earthdata or any other account (an account means an e-mail; user rule).
  PHREEQC as ledger rows only. Read-only use of Book 2's
  `grade-11-seafloor-age` derived file and Book 1's NSIDC September-extent
  file is approved (both books are closed).
- **Varden dolerite dyke (ch. 31):** allowed in Book 5's own figdata only,
  as a buried dyke confined to the basement below the unconformity (so no
  map, section or history of Books 1--4 changes); described as found by the
  survey. `region.py` is not changed.
