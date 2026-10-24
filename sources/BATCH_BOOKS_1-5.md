# Rolling batch: One Earth and Space Sciences Books 1–5, English (set up 2026-10-22)

The five books are written in this one working tree, **one agent per book,
at most three agents at a time, on a rolling basis** (user ruling
2026-10-22). Books 1, 2 and 3 start together. When a book lands and the main
session has verified and closed it (send-backs included), the next book takes
its slot: Book 4 first, then Book 5. This file is owned by the main session;
book agents read it and never edit it.

| Book | Entry file | Years (`parts/…`) | Label prefixes | Ledger | Linker policy | Chapters | Target |
|---|---|---|---|---|---|---|---|
| 1 Grades 1–9 | `one_earth_and_space_sciences_book_1_primary_middle_school.tex` | `grade-1` … `grade-9` | `g1`–`g9` | `sources/ledger/book1.md` | `nearest-preceding` | 32 (1 pilot done) | ~300 pp |
| 2 Grades 10–12 | `one_earth_and_space_sciences_book_2_high_school.tex` | `grade-10` … `grade-12` | `g10`–`g12` | `sources/ledger/book2.md` | `nearest-preceding` | 28 (1 pilot done) | ~330 pp |
| 3 University Year 1 | `one_earth_and_space_sciences_book_3_university_year_1.tex` | `bachelor-1` | `b1` | `sources/ledger/book3.md` | `drop` | 29 (1 pilot done) | ~350 pp |
| 4 University Year 2 | `one_earth_and_space_sciences_book_4_university_year_2.tex` | `bachelor-2` | `b2` | `sources/ledger/book4.md` | `drop` | 31 | ~370 pp |
| 5 University Year 3 | `one_earth_and_space_sciences_book_5_university_year_3.tex` | `bachelor-3` | `b3` | `sources/ledger/book5.md` | `drop` | 31 | ~370 pp |

Note the offset: **Book 3 is `bachelor-1` / `b1`**, Book 4 `bachelor-2`,
Book 5 `bachelor-3`. Targets count schematics; illustrations and photographs
come on top and make chapters longer, as they should.

## Read before anything

1. `../CLAUDE.md` (workspace) and `../book_style.md` (the family style ---
   read **Visuals** and **Quality gates** twice); this repo's `CLAUDE.md`,
   `CONTRIBUTING.md`, `OUTLINE.md` (the chapter list of record and the three
   ownership maps), `sources/SERIES_DEFINITIONS.md`, this file.
2. **The three pilots, approved by the user on 2026-10-22 as the reference** for register,
   density, boxes, figures, data use and calibration:
   `parts/grade-7/01-plate-tectonics.tex`,
   `parts/grade-12/10-climate-change.tex`,
   `parts/bachelor-1/04-geological-maps.tex` (and their `solutions/` twins).
3. University agents also read one Year-1 chapter of a sister series for the
   theorem-with-derivation register:
   `../one-physics-book/parts/bachelor-1/22-first-law.tex`.
4. `styles/oneearth.sty`'s Earth section (boxes, lithologies, map symbols,
   the celestial sphere, plot styles), `figdata/shared/geo.py` and
   `figdata/shared/region.py` --- use what exists before inventing.

## User rulings in force

- One subagent per book, never per-chapter agents; at most three at a time;
  rolling. No review pause: the syncs are internal to the main session.
- **Second writer for Book 4** (user, 2026-10-23): when Book 3 lands, its
  slot goes to a second Book 4 agent that writes the tail of Book 4's
  chapters (range fixed by the main session from Book 4's chapter table at
  that moment) while the first agent continues in order; the cap of three
  agents still holds. Both use Book 4's frozen `DEFINITIONS.md`; the main
  session reconciles the terms where the two ranges meet before Book 4's
  Phase C.
- The outline is approved as it stands (2026-10-22). Chapter numbering and
  slugs are frozen: other books and the ownership maps point at them.
- **Mountain ranges** (main-session choice, user delegated it): the Alps are
  the type collision orogen (Y2 ch. 13 `alpine-orogen`); the Himalaya--Tibet
  and the Andes are compared in ch. 14; ch. 15 `wilson-cycle` uses the
  Appalachian--Caledonian--Variscan belts as the old orogens. No national
  regional geology.
- **Exercise calibration as chemistry** (below).
- **Climate change: physical science only** --- forcing, records, attribution
  and projections as IPCC Working Group I states them, with its calibrated
  language (*likely*, *very likely*, *high confidence*), each statement with a
  ledger row (report, chapter, section). No policy, no costs, no advice.
- **Overlaps: recall, then build.** A notion owned by the physics, biology or
  chemistry series is recalled in prose and never re-defined here.
- **Observation only**: never a quarry, cliff, cave, river in flood or
  volcano for the reader; never a hammer; never the Sun.
- **Maps**: exercise maps and sections only from the invented region
  (`figdata/shared/region.py`, the Varden Hills); world maps from
  `figdata/shared/geo.py`; real maps only if public domain, credited.
- Printed text never names a curriculum, a school system, a country's
  programme, a university or an exam. Provenance lives in comments and
  `sources/` only. Real places are named freely.
- Never use the user's e-mail address anywhere: not in a User-Agent, a request
  or a file. If a source asks for one, use another source.

## Calibration (binding; `tools/check_exercise_calibration.py` enforces it)

| Band | Exercises per chapter | Weekend problem | Pages per chapter |
|---|---|---|---|
| grades 1–5 | 10–11, mostly ★, never decreasing | none | ~7 |
| grades 6–9 | exactly 12, never decreasing | one, 10–14 questions, Parts I–III | ~10 |
| grades 10–12 | exactly 15: 5★, 6★★, 4★★★ in order | one, 18–22 questions, Parts I–IV, ending on a named number | ~11.5 |
| bachelor 1–3 | exactly 12: 4★, 5★★, 3★★★ in order | one, 22–28 questions, Parts I–IV, ending on a named number | ~12 |

**University register.** Laws are `theorem` / `proposition` with a derivation
at the year's mathematics level; what is not derived gets `\admitted` and a
prose pointer to where it is proved ("derived in the Year 3 volume"). Each
standard technique is a `method`. Classic discoveries go in `history` boxes;
professional practice in `inthefield` / `inthelab` boxes.

**Math level guard** (never beyond the matching year of the math series):
- Book 1: whole numbers only in grades 1–3; fractions from grade 4;
  percentages from grades 6–7; powers of ten from grade 8, scientific notation
  from grade 9; proportionality and reading graphs throughout; no equations
  with unknowns beyond one step before grade 8.
- Book 2: trigonometry (sine, cosine, tangent of an angle) from grade 10 for
  latitudes, slopes, dips; vectors as arrows; derivatives only from grade 11,
  a rate written as a derivative only in grade 12; `exp` and `log` only in
  grade 12 (radioactive decay is physics', recalled; isotope ratios).
- Year 1 (Book 3): derivatives and integrals, first-order linear ODEs, vectors
  and the dot and cross products, spherical trigonometry (taught in ch. 1),
  basic statistics (mean, standard deviation, least-squares line).
- Year 2 (Book 4): partial derivatives, gradients, simple PDEs (the heat
  equation recalled from physics), matrices 3x3, exponential decay chains,
  log-normal and power laws.
- Year 3 (Book 5): tensors (stress and strain), Fourier analysis, the
  rotating-frame fluid equations, linear inverse problems and least squares
  with errors, statistics with uncertainties.

## Ownership rules (in force at all times)

1. **Write only your own files:**
   - `parts/<your years>/` (chapters, `solutions/`; `part.tex` only if a
     comment needs it --- the `\ominput` list is frozen);
   - `figdata/<your year>/` and `tests/<your year>/`;
   - `data/derived/<your year>-*` (a dataset only your book uses: add its
     fetch and derive to `tools/fetch_data.py` in ONE appended block marked
     `# Book <N>:`, ids starting with your year, terms verified; report it);
   - `images/book<N>/` (incl. `CREDITS.md`, `ai/PROMPTS.md`);
   - `sources/book<N>/` (`BRIEFS.md`, `DEFINITIONS.md`, `PROGRESS.md`,
     `FIGCHECK.md`, scratch notes) and `sources/ledger/book<N>.md`;
   - `tools/term_config/book<N>_en.py`;
   - `frontmatter/image-credits-book<N>.tex` (Book 1:
     `frontmatter/image-credits.tex`) --- remove its "(none yet)" item when
     the first photograph lands;
   - your entry file, only if unavoidable (report it).
2. **Never edit** another book's files. Defects you find there go in your
   report with file:line and the fix.
3. **`styles/oneearth.sty` is append-only**, and only when unavoidable:
   append at the end under a `% Book <N>:` comment; never change or reorder
   existing lines; re-read the file just before editing (other agents append
   too); prefix new macros or scope them clearly; build your book right after.
   **Prefer asking at the sync** (Phase A report) over appending.
4. **Do not edit** `tools/` (except your term config and your fetch block),
   `figdata/shared/`, `figdata/_table.py`, `data/derived/` files that are not
   yours, `Makefile`, `latexmkrc`, `pytest.ini`, `OUTLINE.md`,
   `CONTRIBUTING.md`, any `CLAUDE.md`, `THEME.md`, `frontmatter/` pages that
   are not yours, `styles/lang/`, `sources/data_ledger.md`,
   `sources/SERIES_DEFINITIONS.md`, `requirements.txt`, `.venv`, or this
   file. If a shared tool or table is buggy or a shared value is missing,
   report it and work around it locally if you can; new traps go in your
   `PROGRESS.md`.
5. **Git is read-only**: `git status`, `git diff`, `git log`. Never
   `checkout`, `stash`, `reset`, `clean`, `restore`, `add` or `commit` --- a
   repo-wide checkout once destroyed a whole batch of shared uncommitted work
   in the sister series. Nothing here is committed: this tree is the only copy.
6. **Build only your own entry file**: `nice -n 10 latexmk <entry>` (with
   `-g` after creating a new chapter file). Never a bare `latexmk`, `make` or
   `make gates`; never two `latexmk` on your entry at once; never a short
   timeout around it (a killed run corrupts `.aux`/`.toc`: recover by deleting
   your entry's `.aux .toc .out .fdb_latexmk` in `build/`). Do not rebuild
   another agent's entry file.
7. **Scoped checks only:** `bash tools/gates.sh <your year>`;
   `make test Y=<your year>`; `make figdata Y=<your year>`;
   `python3 tools/link_defined_terms.py --book <N>`. If a check fails on a
   path that is not yours, note it and carry on.
8. **Cross-book references are prose only**, never `\cref` into another book.
9. **Terms**: follow `sources/SERIES_DEFINITIONS.md`. Before each chapter's
   definitions, grep the harvest of the books already written and of the
   sister series (commands in that file).
10. **No bulk deletes** (user rule 2026-10-22): never `rm` with a wildcard,
    not even in scratch; write new renders into a fresh subdirectory. Delete a
    single named file only when necessary (a rejected AI image being
    regenerated) and say so in `PROGRESS.md`.
11. **Figure renders and image work** go to your own scratch directory:
    `/tmp/claude-1000/-home-bvirrion-repositories-one-course/073e8d3d-6c62-4a98-8f56-8a0346dd7a8a/scratchpad/book<N>/`.
    Check the running header of every render (it names the book).

## Resource limits (user rule, binding from the first command)

The machine is the user's laptop (22 logical cores, 19 GB RAM, WSL2), shared
with their own work and with two other agents.
- Every process under ~1.5 GB RSS and one core; BLAS threads 1
  (`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1`); no multiprocessing, no
  `make -j`; one heavy job per agent at a time.
- Long jobs under `nice -n 19` **and** a cgroup cap:
  `systemd-run --user --scope -q -p MemoryHigh=2G -p MemoryMax=4G <cmd>`.
- `latexmk` only when a chapter is ready, under `nice -n 10`. World maps are
  heavy for TeX: use the 1:110m land table, decimate catalogues you plot
  (e.g. M ≥ 6.5 or one year in five), and never plot the 1:50m land on a
  world map.
- Check `free -g` before anything heavy; leave alone every process that is
  not yours.

## Sources and the ledger

- **A model's memory is not a source.** Every number about the real world (a
  radius, a plate speed, a heat flow, a magnitude, a date, a sea-level rise, a
  CO2 value, a planet's property, a mineral's density, an isotope's
  half-life used as data, a record) has a row in `sources/ledger/book<N>.md`
  with a source key from that file's Sources table and an access date; the
  chapter cites it with `% ledger: <id>[, <id>]`. `tools/check_ledger.py`
  (gate 9) checks every id. Ids are unique across all ledgers: grep
  `sources/data_ledger.md sources/ledger/` before minting one, and cite
  another book's row read-only rather than duplicating it.
- Shared rows (constants, NASA Earth/Sun/planet fact sheets, the ICS time
  scale and colours, the datasets, the region) are in `sources/data_ledger.md`
  --- read-only.
- Values invented for an exercise are data of the exercise and need no row;
  values presented as facts about the world do. Computed numbers (a mean, a
  trend, a spreading rate from a distance and an age, a hypsometric fraction)
  are computed in a `figdata/` script or a calculator script in your scratch,
  never typed from memory.
- Fetch primary pages directly: USGS (earthquakes, minerals, volcanoes),
  NOAA (GML, NCEI, NHC), NASA (fact sheets, GISS, JPL), the ICS chart, IPCC
  AR6 WG1 (chapter PDFs, SPM), the Smithsonian GVP, IRIS/EarthScope, the
  RRUFF and Mindat mineral pages (properties only), journal articles with a
  DOI. Wikipedia `?action=raw` is a map to primary references, not a source.
  Never fill a row from a search snippet. When a database lists several
  values, take the consensus or the most recent compilation, not the first;
  never print more digits than the source's uncertainty.
- **Search budget**: plan ~600 web searches per book; keep a running count in
  `PROGRESS.md`.

## Figures and images

- **Schematics: ~4 per chapter** (the series budget; it does not shrink
  because a chapter is illustrated): cross-sections and block diagrams,
  geological and topographic maps, plate-boundary sketches, the rock cycle,
  P–T grids, phase and ternary diagrams, stereonets, weather maps with fronts,
  atmospheric and oceanic circulation cells, the celestial sphere, orbits,
  graphs. Use the style's pics and line styles; a side-dependent symbol goes
  on the LEFT of the path's direction (fault ticks on the downthrown side,
  trench teeth on the overriding plate, front symbols toward the air mass the
  front advances into).
- **Curves and maps are computed**: a script `figdata/<year>/<name>.py` whose
  values live in functions, writing `figdata/out/<year>-<name>.dat` via
  `figdata/_table.py`, read by `\addplot table`, and a test
  `tests/<year>/test_<name>.py` asserting the defining points (the Mauna Loa
  seasonal maximum in May, the CO2 rise per decade against the ledger, the
  Gutenberg–Richter slope near 1, the core–mantle boundary at 2891 km in
  PREM, a geotherm's surface gradient equal to q/k, an orbit's period from
  Kepler's third law, a spreading rate equal to distance over age). Datasets
  are read from `data/derived/`, never from the network at figure time.
  `make figdata Y=<year>` must leave no diff in `figdata/out/`.
- **World maps**: `figdata/out/shared-geo-*.dat` (land, ridges, transforms,
  subduction lines oriented with the overriding plate on the left and their
  precomputed `teeth`, collision zones, M ≥ 6 earthquakes, Holocene
  volcanoes). School books use the `shared-geo-school-*` boundary set. Credit
  Natural Earth, Bird (2003), USGS, GVP in the caption or the credits page.
- **Exercise maps and sections**: `figdata/out/shared-region-*.dat` (the
  Varden Hills: 50 m contours, river, unit polygons to fill with
  `even odd rule`, the fault oriented for `normal fault`, section A–B). A book
  that needs another view of the region (another section line, a
  three-point problem, a borehole log, a younger-than diagram) writes its own
  `figdata/<year>/` script that IMPORTS `figdata/shared/region.py` and never
  edits it. The region's model is in that file's docstring: keep every
  exercise consistent with it.
- **AI illustrations**: `python3 tools/ai_images.py --book <N> batch.txt
  --work <your scratch>/ai`, launched **from the repo root**, run
  **detached** (it sleeps 30 min on a usage limit; three agents share one
  Codex limit --- expect waits; make grey stubs with `tools/ai_stubs.py`
  meanwhile; never wait with `pgrep -f ai_images.py`). Generic scenes only (a
  child watching rain, a geologist with a map case, a seismograph room, a
  rainy street, a glacier-like valley without a name): **never a real named
  place, volcano, planet, mineral specimen or person**, and **never a
  geological structure the reader is meant to read** (strata, folds, faults,
  unconformities are schematics or photographs). JPEG only. Each image is
  reviewed for scientific accuracy (cloud types, lightning, lava colour,
  snow, strata that make no sense, a Moon phase that cannot be, the Sun and a
  rainbow on the same side) before insertion; reject and regenerate if wrong.
  Prompts logged in `PROMPTS.md` with the model.
- **Photographs**: public domain (NASA, USGS, NOAA, ESA where stated) or CC
  verified through the Commons API (`prop=imageinfo&iiprop=extmetadata`) with
  a User-Agent carrying **no e-mail**; a row in `images/book<N>/CREDITS.md`
  and an item on the credits page; attribution-required licences credited at
  the caption's end. Real volcanoes, landscapes, outcrops, thin sections,
  minerals, planets, scientists, historic instruments --- never a generated
  stand-in for a real thing.
- **Every figure is checked on its own page at 130 dpi** (find its page with
  `pdftotext`, render with `pdftoppm -png -r 130 -f P -l P -singlefile`),
  twice: **layout** (no label on a label, line or arrow; nothing outside its
  box; caption clear of the drawing; no letters inside an AI image; legends
  off the data) and **geoscience** (dip directions and dip angles match the
  strike-and-dip symbols; younging and superposition; fault senses; trench
  teeth on the overriding plate; fronts on the right side; cyclone rotation
  and Coriolis deflection by hemisphere; isobars and winds consistent;
  geotherms and isotherms in the right sense; curves at their ledger values;
  orbits and phases geometrically possible). One line per figure in
  `sources/book<N>/FIGCHECK.md` (`ch | figure | page | layout ok/fixed |
  science ok/fixed | note`). **Never from a contact sheet, never at 72 dpi.**
  Thin lines can look black at 130 dpi: zoom to 300 dpi before "fixing" a
  colour.

## Agent lifecycle

**Phase A --- plan, no prose; report, then stop.**
Write `sources/book<N>/BRIEFS.md` --- per chapter: sections; definitions
(term, label, owner checked against `SERIES_DEFINITIONS.md` and the outline
maps); recall boxes (same book, other volume, other series); planned figures
tagged *schematic / figdata / AI / photo*; ledger needs; datasets; the weekend
problem's story and its named final number. Also `sources/book<N>/DEFINITIONS.md`
(the term list, one row per term with chapter and label) and
`sources/book<N>/PROGRESS.md` (state, page projection, search count, traps).
Then return the **Phase A report**:

1. Paths written; the entry file still builds 0/0/0.
2. **Re-founded terms** (university books: school notions you define again)
   and **contested terms** (anything not in the outline's maps that another
   book might also claim), with your case for each.
3. **Terms you use but do not define**, with their owner (this series or a
   sister series).
4. **Style-file needs** (packages, macros, pics) --- the main session adds
   them at the sync.
5. **figdata scripts** planned (name, what they compute or read, the test's
   defining points) and **new datasets** (source, licence, size).
6. **Image plan**: AI batch sizes per grade/part; photograph list with the
   Commons or agency file names you intend to verify.
7. **Source plan**: the ledger-heavy chapters and your search estimate.
8. **Chapter changes** proposed (split, merge, reorder) with the reason.
   Default: none.
9. **Defects** found in the pilots, the tooling, the shared data or the
   outline.

**Sync (main session).** Merge the map into `SERIES_DEFINITIONS.md`, rule on
collisions, make the style-file additions, write "Sync decisions" below, and
resume the agent with `SendMessage`.

**Phase B --- write, in outline order.** Per chapter, the cycle:
1. ledger rows first;
2. course text: a concrete hook scene; 3–5 sections; every environment titled
   and labelled `<type>:<yr>:<slug>:<name>`; new terms as
   `\emph{term}\index{term}` inside a `definition`, **only in the owner
   chapter**; a `recall` box when a notion owned earlier or elsewhere is used;
   derive what the level allows, `\admitted` otherwise; `` ``…'' `` quotes,
   never `"`; `\dots`, never `...`; `\ce` for formulas, balanced;
3. exercises and the weekend problem at the band's calibration (gate 10); mix
   computation, map and graph reading, reasoning, orders of magnitude; no
   exercise asks the reader to go anywhere or try anything outdoors beyond
   looking;
4. solutions: one `\begin{solution}{key}` per `exo:`/`pb:` in order, problem
   answers `\textbf{1.}`…; every number computed (figdata or a calculator
   script in your scratch) and **each answer re-read against its own
   question** --- past runs shipped answer permutations, an answer
   contradicting its own question's data, rounded-intermediate chains, and a
   question asking about the wrong object; gate 5 cannot see these;
5. figures (above), with their FIGCHECK lines;
6. `latexmk <entry>`, then `bash tools/gates.sh <year>`; fix to 0/0/0 and
   green before the next chapter.

**Checkpoints.** Every 8 chapters (Books 1–2: also at the end of each grade),
write a page projection in `PROGRESS.md`. A projection more than 10 % under
target means chapters are being compressed: restore depth before going on
(the chemistry books landed ~14 % thin until nudged). `PROGRESS.md` must
always let a **fresh agent resume your book** from it alone (chapter status
table, open items, conventions you settled).

**Phase C --- finish.**
1. Term links: `python3 tools/link_defined_terms.py --book <N> --unwrap
   --apply`, then `--apply`. Curate `tools/term_config/book<N>_en.py` for the
   Earth homographs listed in its docstring, after checking each target; watch
   the capitalised-harvest trap. Never write `\omterm` by hand, never inside
   `\ce{}`, `\qty{}` or a figure. The idempotence dry run over the wrapped
   tree must print `links to insert: 0`.
2. The full per-figure double-check again over **every** figure (the links
   move text), FIGCHECK complete: one line per `omfigure` / `includegraphics`.
3. **A scripted solutions re-read**: for every exercise and problem question,
   print the question and its answer side by side (a small script in your
   scratch) and re-read each pair; log the slips fixed in `PROGRESS.md`.
4. No grey stubs left (`python3 tools/ai_stubs.py --book <N> --list` empty),
   no PNG in `images/book<N>/ai/`.

**Phase D --- report** to the main session: pages vs target and chapter
count; counts of schematics, figdata scripts and tests, AI images,
photographs, ledger rows, term links and distinct targets; gate results
(`gates.sh` for each of your years, `make test Y=…`, `make figdata Y=…` no
diff, the log 0/0/0, the idempotence dry run); EXCLUDED facts (values you
could not source and therefore did not print); defects found in other books,
the shared data or the tooling; new traps and calibration for the shared docs.

## Book notes

**Book 1 (grades 1–9)** --- the provenance sources for grades 1–5 (the old
primary programmes) were not fetched during setup: fetch and note them in
`sources/book1/` (comments only, never in print). The youngest readers first: grades 1–5 short,
warm, illustration-rich, whole numbers first, one AI batch per grade; real
photographs of the sky and the Earth from NASA/USGS where they show the real
thing (the blue marble, a named volcano, a real glacier). The g7 pilot is the
reference for grades 6–9. Datasets: the world map and catalogues (g4
`world-physical-map` and `volcanoes-earthquakes-first-look`, g7, g9),
GISTEMP and Mauna Loa (g9 `climate-past-and-present`, simplified), and the
region's topographic map (a simplified view in g2 `drawing-to-map`, contours
and scale in g9 `maps-of-the-earth`). Sky chapters recall physics (day and night, the Moon, the seasons, the
Solar System) and add only the Earth view.

**Book 2 (grades 10–12)** --- the provenance texts for the lycée-level
general-science course were not fetched during setup: fetch and note them in
`sources/book2/` (comments only). The g12 pilot is the reference; climate, energy
budget and the fluid envelopes carry most of the datasets (energy budget from
AR6 WG1 ch. 7 figure values; the Keeling curve; ice cores; LR04 if the
grade-12 `past-climates` chapter needs it). Plate-tectonics chapters in
grade 11 use the full PB2002 set and the step velocities
(`data/derived/pb2002-steps.csv`). Radiometric dating's law is physics' (g12):
`age-of-the-earth` recalls it and applies it.

**Book 3 (bachelor-1)** --- open item from the pilot: in ch. 4's weekend
problem the breakable problem box pushes its unbreakable data table to the
next page and leaves about a third of a page blank (p. 20 of the pilot
build); fix it in your own files (e.g. place the table before the box or let
it float) and check the page at 130 dpi. --- The Year-1 foundation Books 4–5 build on, so its
definitions are the series' Year-1 vocabulary. Ch. 1 teaches spherical
trigonometry (absent from the math series) and coordinates on the sphere;
ch. 4–5 (maps, sections) build on the region; ch. 6 is the first field and
lab methods chapter. PREM, heat flow, isostasy and gravity, plate kinematics
(Euler poles, finite rotations, computed and tested), stress and strain in
2D, the stratigraphic scale (ICS rows), radiometric methods (decay recalled,
isochrons derived), and the fluid envelopes.

**Book 4 (bachelor-2)** --- starts in the first freed slot; reads Book 3's
actual chapters and harvest before Phase A. Thermodynamic phase diagrams
(Al2SiO5 triple point, solidi) from sourced experimental data; magmatic
differentiation (Rayleigh fractionation computed); the Alps as the type
orogen with ophiolites and HP rocks; the Himalaya and the Andes; orbital
forcing (Laskar-type insolation from orbital elements, computed and tested,
or a sourced table); anthropogenic climate change at AR6 depth.

**Book 5 (bachelor-3)** --- starts in the next free slot; checked against
Books 3–4's harvest. Seismology and inversion (ray tracing in a layered
model, tested), gravity and geodesy, palaeomagnetism, thermal models of the
lithosphere (plate cooling vs half-space, tested), mantle convection scaling,
deformation mechanisms, petrological thermodynamics, isotopes and
geochronology, sedimentology and sequence stratigraphy, GFD (geostrophy,
Ekman, Rossby waves, tested), climate models, hydrogeology, glaciology,
remote sensing and GIS, planets, exoplanets, galaxies, nucleosynthesis.

## Lessons from the pilots (2026-10-22, main session)

- A `\pic` is sized in centimetres: inside a pgfplots axis, draw scale bars
  and anything that must match map distances in `axis cs` units.
- A TikZ decoration (teeth, ticks) misplaces its marks on a path with jumps:
  use the precomputed `shared-geo-*teeth.dat` polygons, or one path per line.
- Lines traced by marching squares have an arbitrary direction: orient any
  line that carries side symbols before writing it (see `orient_fault`).
- An arc in `tdplot_main_coords` lies in the horizontal plane: draw a dip arc
  as a parametric plot in the vertical plane.
- pgfplots error bars: `error bars/.cd, x dir=both, x explicit` goes on the
  `\addplot`, not on the axis.
- Map labels: `\scriptsize`, white fill at 75–80 % opacity, off the lines;
  labels near the frame are clipped: place them inward (`below right`...).
- The linker links short forms only through `EXTRA` (plate, forcing,
  feedback...); problem Part headings are masked by `protect.py`.
- AI images were rejected twice in three pilots (South America shown twice;
  a compass straddling a rock edge): look at every image for its science.
- Solutions are computed from the ROUNDED data the chapter prints.

## Sync decisions

(Written by the main session after each Phase A report; binding.)

### Sync 0 (2026-10-22, before launch)

- The user approved the three pilots and asked for all five books, at most
  three agents at a time.
- **fold, anticline, syncline, fold axis** are defined in Y1 ch. 4
  `geological-maps` (`def:b1:geological-maps:fold`); Y1 ch. 17 recalls them
  and owns fold geometry proper. School: g12 `mountain-building` owns folds.
  (Also in `SERIES_DEFINITIONS.md` and the OUTLINE map.)
- The invented region keeps its name, the **Varden Hills**.

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

## Reconciliation to-do

(Main session; collected as books land.)

- **Book 1 closed 2026-10-23** (main-session verification): 32 ch., 324 pp
  (course text ~250 pp, 12 % under the per-chapter guide, but the book is
  above its ~300-pp target; grades 1--5 short by design; not padded),
  234 figures, 54 AI, 66 photos, 285 ledger rows, ~6,100 links. Forced
  build 0/0/0; gates g1--g9 OK; 183 tests pass; figdata byte-stable (261
  tables); linker idempotent. Recomputed by hand: g8.2 and g7.3 problems
  (exact), g6.4 and g9.1 final numbers. 16 pages checked at 130 dpi (weather
  map rotation and fronts zoomed to 300 dpi; E--F section; Pole-Star
  geometry; physical map); all 54 AI images looked at: no defect. Fixed by
  the main session: g9.1 problem printed -0.23 (double rounding of -0.2245)
  -> -0.22 and the warming 1.21 -> 1.20; g6.2 caption "through her" ->
  "through the observer".
- Shared tooling fixed after Book 1: `protect.py` now masks `\pageref`,
  `\nameref`, `\omwx{}` and inline `\tikz`.
- To do at reconciliation: `check_ledger.py` resolves source keys per file
  (Book 1 report); pgfplotstable/groupplots not loaded (load only if a book
  needs them); an `omfigure` has no counter, so `\cref` to a figure prints
  "Section": grep all books for `\cref{fig:` at the end.
- Book 1's one Wikipedia row re-sourced by the main session (2026-10-23):
  `nhm:challenger-voyage` (NHM + RSGS pages).
- Final grep at reconciliation: `grep -iE 'wikipedia|wikibooks|\| *WIKI|wiki:' sources/ledger/*.md | grep -viE 'commons\.wikimedia|wikimedia commons'`
  must be empty.
- Shared fixes after Book 2's report (main session, 2026-10-23): the cover
  title is set on two lines (it was wider than the page); `derive_lr04` keeps
  only the stack (the NOAA file appends other blocks; figdata unchanged);
  `region.py` section fault now ends on the ground (new test), changing only
  `shared-region-section-fault.dat` (used by Book 2 g12.02).
- To do at reconciliation: nullfont noise ("Missing character ... nullfont",
  thousands per build) comes from blank-line separators in pgfplots tables
  (`shared-geo-*`, `jumps()` in region.py); harmless; consider `nan nan`
  rows + `unbounded coords=jump` only if all books are rebuilt and checked.
- **Book 2 closed 2026-10-23** after one send-back (wiki rows, per-page
  figure check, all-solutions re-read): 28 ch., 362 pp (10 % over ~330),
  210 figure objects with one FIGCHECK row each (22 fixed in the send-back,
  5 of them science), 15 AI, 84 photos, 367 ledger rows (0 Wikipedia rows by
  the refined grep; the 60 "wiki" hits are Commons credits), 2,198 links,
  9 solution slips fixed. Main-session verification: forced build 0/0/0,
  gates g10--g12 OK, 193 tests (g10--g12 + shared) pass, figdata byte-stable
  (198 tables), linker idempotent, no stubs or PNGs, check_ledger OK.
  Recomputed by hand: g10.1 (Eratosthenes, triangulation, first metre) and
  g12.7 (Rb--Sr isochron) problems, g12.6 heat budget final numbers: exact.
  15 pages at 130 dpi (sounding, cyclone, Peru upwelling, basin map,
  polarity scale and striped floor at 300 dpi for symmetry, Airy columns,
  velocity triangle, slab sections, Varden sections with the moved syncline
  and the red unconformity, shortening, wet solidus, isochron, pollen,
  forcing bars against AR6 Table 7.8); 15 AI images looked at: no defect.
  Left in place (no-delete rule): unused `images/book2/ai/g10-research-ship.jpg`.
- The landing grep was refined (2026-10-23): `| *WIKI` with `-i` also matched
  "| Wikimedia Commons"; Commons lines are now filtered out by a second grep.
- Shared fix after Book 2's report (main session, 2026-10-23):
  `region.contact_elevation` no longer iterates; it returns the footwall value
  if it lies in the footwall, the hanging-wall value if it lies in the hanging
  wall, else **nan** (the gap the normal fault cuts out of a contact; the old
  fixed-point iteration oscillated there and returned a footwall value inside
  the hanging wall). New test `test_contact_in_the_fault_gap`. Callers checked:
  only Book 1 `grade-7/varden_history.py` reached the gap (7 points), and its
  `unit()` check already dropped them; every table of `water_table`,
  `varden_history`, `varden_sections` and `varden_maps` is byte-identical.
  New callers must handle nan.
- **Book 3 closed 2026-10-23** (main-session verification after the Phase D
  report):
  - forced build 0/0/0, 452 pp (target ~350: +29 %, accepted, nothing padded);
  - `gates.sh bachelor-1` OK; 242 tests pass (bachelor-1 + shared); `make
    figdata Y=bachelor-1` byte-identical (275 tables); linker 0 to insert; no
    AI stubs or PNGs; check_ledger clean for bachelor-1; refined wiki grep 0;
    FIGCHECK "Phase C full pass" 184 rows for 182 figure objects.
  - Weekend problems recomputed in full: ch. 12 (Iceland, 19 mm/yr) exact;
    ch. 27 (cap north of 40 N) exact but one slip: band power -0.971 ->
    -0.972 PW (fixed). Named numbers of ch. 11 (182 m) and ch. 18 (Mw 7.95)
    exact.
  - 15 figures at 130 dpi: one science defect, fixed in the main session:
    ch. 29's overturning schematic drew Antarctic Bottom Water northward
    through the 3000-5000 m layer whose printed RAPID transport is -5.9 Sv
    (lower NADW, southward). Redrawn: basin 6 km, a lower-NADW southward
    arrow, AABW along the bottom beneath it; caption reworded without an
    unsourced depth; label clashes re-checked at 200 dpi; page layout
    unchanged (452 pp). One wording fix: ch. 16 "the slope falls a little"
    (61.3 -> 35.3 MPa/km in compression is not "a little") -> "falls, in
    compression, to about 35 MPa per kilometre". A flagged Moho value (ch. 10,
    "about 320 C") was correct (T0 = 10 C) and left.
  - All 21 AI images looked at: generic scenes. Three are unused
    (`b1-clean-lab`, `b1-rock-press`, `b1-trade-wind-ship`), left in place
    (no-delete rule): mention in the final report.
  - Defects reported by Book 3 for reconciliation: `test_repo_ledger_is_clean`
    fails on Book 4's `19-phanerozoic-earth.tex` (`data:etopo-1deg`, Book 4
    told); shared `windbarb` pic: the first full feather after a pennant
    touches it; `IPCC-AR6-SPM` source key duplicated in `book3.md`; Book 1
    Iceland-low image row says Terra, Commons says Aqua; Kuroshio transport
    unsourced in Book 1 g8 / Book 2 (Book 3 ch. 29 uses Lien 2015).
- **Book 4 split (user, 2026-10-23):** on Book 3's landing a second Book 4
  agent took ch. 26-31 (notes `sources/book4/PROGRESS-B.md`, builds into its
  scratch outdir); the first agent keeps ch. 19-25, then Phases C-D over all 31
  after the main session reconciles the seam.

### Book 4 seam reconciled 2026-10-23 (~16:40)
Both ranges were written: ch. 19–25 by the first agent, ch. 26–31 by the second, which then stopped. The second writer's notes and EXCLUDED list are in `sources/book4/PROGRESS-B.md`.

Seam check (main session):
- No term is defined in both ranges.
- Every reference from ch. 26–31 into ch. 19–25 resolves.
- `DEFINITIONS.md` labels are unchanged.

Items handed to Phase C:
- The `allochthonous`/`autochthonous` homograph: ch. 13 uses the nappe sense, ch. 20 the fossil sense.
- Forward uses to check after linking: LOI in ch. 9; TIMS/MC-ICP-MS in ch. 4; ch. 8's reference to ch. 31.
- Image-credit order: ch. 26–31 must come after ch. 21–25.

The first agent now runs Phases C and D over all 31 chapters. Agents alive: 2 (Book 4 first agent and Book 5).

### Book 4 closed 2026-10-23 (~18:05)
Main-session verification (Step 2.4), all green:
- forced build 0/0/0 at 461 pp (~370 target, +25 %, accepted as for Book 3);
- `gates.sh bachelor-2`; `check_ledger` 2355 rows; linker dry run 0;
- `make figdata Y=bachelor-2` with no md5 change over 274 tables; `make test Y=bachelor-2` 205 passed;
- no stubs or PNGs; wiki grep 0; curriculum grep clean;
- FIGCHECK "Phase C full pass" has 228 rows for 204 omfigure + 9 table floats + boxed images.

By hand:
- ch. 29 porphyry problem recomputed exactly (4.44 Mt; z 0.4298, Φ 0.6663, ḡ 0.555 %);
- ch. 28 PSHA problem recomputed exactly (λ(0.2/0.3/0.4 g) 9.24e-3/2.20e-3/6.41e-4, 0.303 g, F 1.33/0.727);
- named numbers: ch. 25's 439 W/m² reproduced from the Berger–Loutre elements, and July 65° N matches the tables (397.60 and 426.76); ch. 13's 133 km chain checked.

Fixed in the main session:
- ch. 11 (two figures): the experimental kyanite–andalusite line ran past the triple point through the sillimanite field; it is now cut at 504 °C;
- ch. 11: an "andalusite" label sat on a tick.

All 14 AI images were looked at: generic scenes, none unused. The 15-page sample at 130 dpi is otherwise clean.

Defects the agent reported for the final reconciliation:
- `tools/photo.py` given a full path writes it into CREDITS and doubles the author;
- the curriculum gate fires on "laboratory programme";
- `qa.py` ignores `\%`.

Agents alive: 1 (Book 5).

### Book 5 closed 2026-10-23 (~21:45)
Main-session verification (Step 2.4), all green:
- forced build 0/0/0, 456 pp, then 455 after the reflow fix (target ~372 + front matter, +18 %);
- `gates.sh bachelor-3`; `check_ledger` 2432 rows; linker dry run 0;
- `make figdata Y=bachelor-3` with no md5 change over 412 tables; `make test Y=bachelor-3` 288 passed;
- no stubs or PNGs; wiki grep 0; curriculum grep clean;
- FIGCHECK "Phase C full pass" has 209 rows for 183 omfigure + 26 images.

By hand:
- ch. 28 exoplanet problem recomputed exactly (a 0.0952 au, 7.99 M⊕, 2.40 R⊕, b 0.40, ρ 3.18 g/cm³, Teq 623 K, H 166 km, 18 ppm);
- ch. 6 rebound problem recomputed exactly (τ 7.40 kyr, η 3.0e20 Pa s, log10 η 20.48, Ra 1.65e6);
- named numbers: ch. 30's closed-box 16.38 % reproduced from μ = 13.7/47.1; ch. 6's 20.48 checked.

Fixed in the main session:
- ch. 15 caption: reading direction on the reversed axis;
- ch. 26: Olympus Mons photo resized, which removes a 45 %-blank page;
- ch. 4: the Kesta C pole labelled with its age.

All 21 AI files were looked at: generic scenes. Two are unused alternates: `b3-rotating-table.jpg` and `b3-modelling-centre.jpg`.

Defects the agent reported outside Book 5:
- "Reference Earth model" is defined in both g11 ch. 2 and b1 ch. 9. This is allowed: a university book may re-found a school notion.
- Book 3 names the buoyancy frequency (b1 ch. 26) and the gradient wind (b1 ch. 28) without an index entry.
- Source typos noted (Asplund 2021 Table B.1, Kopparapu 2013).

No agents are alive. Next: final reconciliation (Step 2.6).

## Final reconciliation (main session, 2026-10-23, no agents alive)

All five books were rebuilt with `latexmk -g`, all at 0/0/0:

| Book | Chapters | Pages |
|---|---|---|
| 1 | 32 | 324 |
| 2 | 28 | 362 |
| 3 | 29 | 452 |
| 4 | 31 | 461 |
| 5 | 31 | 455 |
| **Total** | **151** | **2,054** |

Checks over the whole tree:
- `make gates`: 15 years OK.
- `make figdata`: no md5 change over all 1,454 tables.
- `make test`: 1,046 passed.
- `check_ledger`: OK (2432 rows).
- Linker dry run: 0 to insert for every book.
- Wiki grep over all ledgers: 0.
- `\cref{fig:` grep: 0.

Fixed here:
- **Full test run:** `make test` without Y failed at collection because grade-11 and bachelor-1 both own figdata modules named `hypsometry` and `prem_profiles`. Without Y, each year now runs in its own pytest process. Per-year runs were never affected.
- **Duplicate definition:** "igneous rock" was defined in both g6 ch. 3 and g11 ch. 8, which breaks the rule that the school volumes never repeat. g11 now recalls it in its recall box and defines only volcanic and plutonic rock. Book 2's linker was re-run (2,198 → 2,187 links), and the book still builds at 0/0/0, 362 pp.
- **Wind barbs:** in the shared `windbarb` pic, the first full barb after a pennant touched the pennant. Barbs now start 0.12 further in. Checked at 300 dpi on Book 3's weather map, its only user.
- **Book 1 g8 Iceland-low caption:** Terra → Aqua, following the Commons/Visible Earth description that Books 3 and 4 checked.

Found already resolved:
- `IPCC-AR6-SPM` is defined once per ledger file; keys resolve per file by design.
- `test_repo_ledger_is_clean` passes.
- The Kuroshio transport no longer appears in Books 1–2.

Left as they are:
- Nullfont noise in the logs (harmless).
- The curriculum gate's catch of "programme": it is conservative on purpose, and writers say "study".
- `photo.py` and `qa.py` were agents' scratch scripts, not repo tools.
- Book 3's unindexed buoyancy frequency (b1 ch. 26) and gradient wind (b1 ch. 28): named in prose, not defined, and defined in Book 5.

Unused images, left in place under the no-delete rule:
- `images/book2/ai/g10-research-ship.jpg`;
- `images/book3/ai/b1-clean-lab.jpg`, `b1-rock-press.jpg`, `b1-trade-wind-ship.jpg`;
- `images/book5/ai/b3-rotating-table.jpg`, `b3-modelling-centre.jpg`.

Nothing is committed.
