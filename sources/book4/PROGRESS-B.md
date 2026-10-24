# PROGRESS-B --- Book 4, second writer (chapters 26--31)

Resumable state of the second Book 4 agent (user ruling 2026-10-23, batch file
"Second writer for Book 4"). The first Book 4 agent writes ch. 1--25 and owns
`PROGRESS.md`, Phases C and D. This file is owned by the second writer.

Read before resuming: `sources/BATCH_BOOKS_1-5.md` (binding), `BRIEFS.md`
(briefs of ch. 26--31 and the homograph table), `DEFINITIONS.md` (FROZEN),
`PROGRESS.md` (traps), `FIGCHECK.md`, then this file.

## Range and rules

- Range: ch. 26 `deep-time-climate`, 27 `anthropogenic-climate-change`,
  28 `geological-hazards`, 29 `ore-deposits`, 30 `energy-geology`,
  31 `field-lab-methods-2`, in this order, each with its solutions file.
- Own files: those 12 .tex files; new `figdata/bachelor-2/<name>.py` and
  `tests/bachelor-2/test_<name>.py` (names checked free with
  `find figdata tests -name '<name>*'`); new images `images/book4/b2-2[6-9]-*`,
  `b2-3[01]-*`; this file.
- Shared Book 4 files are APPEND-ONLY (re-read before each write):
  `sources/ledger/book4.md` (my tool `tools/ledger.py` in scratch inserts
  sources before the first `## Rows` and rows at the end, and refuses to write
  if the file changed during the run), `images/book4/CREDITS.md`,
  `images/book4/ai/PROMPTS.md`, `frontmatter/image-credits-book4.tex` (items
  inserted just before `\end{itemize}`), `sources/book4/FIGCHECK.md`,
  `sources/book4/PROGRESS.md` (only the "Term changes after the split notice"
  section, if ever).
- Build ONLY into my outdir:
  `scratch/book4b/tools/build.sh [-g]` (latexmk -outdir=scratch/book4b/build
  under nice + systemd-run caps). Never `build/`.
- References into ch. 19--25: chapter labels `\cref{ch:b2:<slug>}` only.
- Scoped checks only: `bash tools/gates.sh bachelor-2`, my own tests, my own
  figdata scripts one by one. No `make figdata/test Y=bachelor-2`, no linker.

## Scratch (`/tmp/claude-1000/-home-bvirrion-repositories-one-course/073e8d3d-6c62-4a98-8f56-8a0346dd7a8a/scratchpad/book4b/`)

- `tools/build.sh [-g]`, `tools/render.sh <dir> <dpi> pages...` (fresh dir under
  `renders/`), `tools/where.sh <pattern> [first last]`, `tools/ledger.py spec`,
  `tools/commons.py`, `tools/photo.py`, `tools/shrink.sh`.
- `calc/chNN.py` --- the solution calculators (every printed answer).
- `harvest_series.tsv`, `harvest_sister.tsv` --- index harvests (2026-10-23).
- `ledger/chNN.spec` --- the ledger specs as appended.

## State

- 2026-10-23: started. Read the batch file, BRIEFS, DEFINITIONS, PROGRESS,
  FIGCHECK, CONTRIBUTING, book_style, OUTLINE, SERIES_DEFINITIONS, ch. 8 and
  18, the g12 pilot. Harvest check of my 96 DEFINITIONS rows: only the planned
  re-founds collide (ECS, attribution g12; return period g10; concentration
  factor, ore deposit, placer g9). Biology b2 owns reservoir, flux, residence
  time, steady state, box model, relaxation time, carbon cycle, airborne
  fraction, carbon sink, cumulative emissions, carbon budget, global warming,
  mitigation, net zero: recall only. Book 5 owns carbon isotope excursion,
  organic carbon burial fraction, energy-balance model, two-layer EBM,
  weathering-limited regime, mineral dissolution rate law, wireline log,
  Darcy's law, intrinsic permeability, sea-level equivalent: prose only.

- 2026-10-23: RANGE COMPLETE. Ch. 26-31 all written and verified; image credits for ch. 26-31
  appended to frontmatter/image-credits-book4.tex (after the first agent's ch. 20 item; their
  ch. 21-25 items, if any, will land after mine: reorder at Phase C). Final report sent.

## Chapter table

| ch. | slug | status | pp | notes |
|---|---|---|---|---|
| 26 | deep-time-climate | DONE 2026-10-23 | 12 + 1.5 sol. (printed 251-262, sol. 316) | 6 figures (2 TikZ, 4 data), 1 AI (b2-tropical-weathering), 0 photos; 9 sources, 20 ledger rows; figdata deeptime.py, tests test_deeptime.py (5); calc/ch26.py; problem 24 q., named number 137 kyr |
| 27 | anthropogenic-climate-change | DONE 2026-10-23 (full build 0/0/0 once ch. 21 compiled; FIGCHECK lines appended) | 11 + 2.5 sol. (printed 274-284 in the 370-p build) | 5 figures (ERF series, energy schematic, feedback bars, TCRE, sea-level stack), 0 AI, 0 photos; 5 sources, 22 ledger rows; figdata anthropogenic.py, tests test_anthropogenic.py (5); calc/ch27.py; problem 24 q., named number 512 Gt CO2 |
| 28 | geological-hazards | DONE 2026-10-23 | 11 + 2 sol. (printed 295-305 in the 380-p build) | 6 figures (risk circles, Poisson + interval survival, hazard curve, infinite slope + F chart; 2 photos: Caraballeda debris flow, Banda Aceh mosque), 0 AI; 10 sources, 22 ledger rows; figdata hazards.py, tests test_hazards.py (5); calc/ch28.py; problem 24 q., named number 0.303 g |
| 29 | ore-deposits | DONE 2026-10-23 | 12 + 1.7 sol. (printed 307-318, sol. 378-380, 396-p build) | 7 figures (porphyry section, supergene profile + VMS mound, histograms, scatter + grade-tonnage curve; 2 photos: Bingham Canyon from ISS, Flambeau gossan; 1 AI: b2-core-shed in inthefield), 13 sources, 26 ledger rows; figdata ores.py, tests test_ores.py (5); calc/ch29.py; problem 24 q., named number 4.44 Mt |
| 30 | energy-geology | DONE 2026-10-23 (full build 0 err / 0 undef; the 2 overfull boxes are in ch. 24, first agent) | 11 + 2.5 sol. (printed 341-351, sol. 417-419, 436-p build) | 4 figures (van Krevelen + transformation ratio, burial history + events chart, geothermal schematic + Geyserville photo, CO2 density + trapping bands), 1 photo (b2-30-geyserville, US DoD PD), 1 AI (b2-rig-night in inthefield); 20 sources, 31 ledger rows; figdata maturation.py + co2_density.py, tests test_maturation.py (6) + test_co2_density.py (3); calc/ch30.py (+ fix30.py, text fixes); problem 25 q., named number 19.0 Mt |
| 31 | field-lab-methods-2 | DONE 2026-10-23 (full build 0/0/0, 461 pp) | 12 + 2 sol. (printed 362-373, sol. 443-444) | 4 figures (two thin-section photos, inclusion-trail TikZ, point-counting error + USGS XRF SiO2 accuracy, Varden inlier map with 30 stations) + 1 photo in the inthelab box (b2-31-microprobe) + 1 AI in inthefield (b2-field-camp, prompt already in PROMPTS.md); 3 photos total; 17 sources, 25 ledger rows; figdata labmethods.py (parts pc, xrf, stations, numbers; imports figdata/shared/region.py read-only), tests test_labmethods.py (6); calc/ch31.py; problem 25 q., named number 247 ppm |

## Seam with ch. 19--25 (first agent)

Chapter labels pointed to, and what I assume they define (prose recalls only):

- `ch:b2:precambrian-earth` (ch. 18): faint young Sun, snowball glaciations (ch. 26 recall box and §2).
- `ch:b2:phanerozoic-earth` (ch. 19): Gondwana at the South Pole in the Ordovician, Cretaceous high seas and oceanic anoxic events (ch. 26 §3).
- `ch:b2:climate-proxies` (ch. 24): benthic d18O, ice-volume effect, proxy CO2 (ch. 26 §4).
- `ch:b2:orbital-forcing` (ch. 25): orbital tuning of time scales, Milankovitch cycles (ch. 26 §4-5).
- `ch:b2:himalaya-andes` (ch. 14): uplift of Tibet (ch. 26 §4, tectonics and climate).
- `ch:b2:elements-in-the-earth` (ch. 3): chalcophile element, mineral--melt partition coefficient (ch. 29 recall box, R-factor paragraph).
- `ch:b2:magmatic-differentiation` (ch. 8): layered intrusion, cumulate, the Bushveld (ch. 29 recall box and chromite paragraph).
- `ch:b2:magmatic-series` (ch. 9): calc-alkaline arc magmatism (ch. 29 porphyry paragraph).
- `ch:b2:precambrian-earth` (ch. 18) also: banded iron formation, craton (ch. 29 recall box and section 4).
- `ch:b2:eruptive-styles` (ch. 6): volcanic eruptions (ch. 27 §1, volcanic forcing spikes); pyroclastic density currents, lahars, tephra fall (ch. 28 recall box and §4).

- `ch:b2:basins-compared` (ch. 16): subsidence curve (ch. 30 recall box).
- `ch:b2:magmatic-series` (ch. 9): modal composition, QAPF diagram (ch. 31 recall box and §1); its
  inthelab box already uses "loss on ignition" in prose before ch. 31 defines it (linker will link).
- `ch:b2:isotope-geochemistry` (ch. 4): radiogenic isotope tracer, isotope reference standard (ch. 31
  recall box, §4); ch. 4's lab box describes TIMS/MC-ICP-MS informally, ch. 31 defines them.
  Ch. 8 line 682 already crefs ch. 31 for the microprobe: matched. Book 3 ch. 16 (effective
  stress, Coulomb criterion) and ch. 5 (borehole log) recalled in prose.

## Term notes

(none yet)

## Datasets added (`# Book 4 (second writer):` sub-block in tools/fetch_data.py)

- `bachelor-2-co2-nist-z0000` ... `z3000` (31 single-point NIST Chemistry WebBook fluid.cgi
  queries for CO2, Span-Wagner EOS, NIST SRD 69 terms; ledger `data:b4-co2-density`) along
  T = 15 + 0.025 z degC, p = 0.101325 + 9.80665e-3 z MPa -> `data/derived/bachelor-2-co2-density.csv`
  (depth_m, t_c, p_mpa, rho, phase). NIST labels the 700 m point "vapor" although T > Tc
  (p < pc): the phase column is NIST's, not printed.

- `bachelor-2-porphyry-cu` (USGS OFR 2008-1155, Singer, Berger and Moring 2008, PD; ledger
  `data:b4-porphyry-cu`): PorCuTX2008.txt is Latin-1 with CR line endings, tab-separated ->
  `data/derived/bachelor-2-porphyry-cu.csv` (422 deposits with tonnage > 0 and Cu > 0; name,
  country, tonnage_Mt, cu_pct, mo_pct, au_gt, subtype).

- `bachelor-2-cenogrid` (PANGAEA 917717, Westerhold et al. 2020, CC BY 4.0; ledger
  `data:b4-cenogrid`) -> `data/derived/bachelor-2-cenogrid.csv` (100-kyr means, 671
  rows) and `bachelor-2-cenogrid-petm.csv` (55-57 Ma native, 401 rows). The PANGAEA
  collection 917503 returns HTTP 400: use the child dataset. Its header carries PI
  e-mails: never copied.
- `bachelor-2-foster2017` (Nature Comms 8:14845 supplementary xlsx, CC BY 4.0; ledger
  `data:b4-foster2017`) -> `bachelor-2-foster2017.csv` (sheet "LOESS Fit", columns
  A, B, D, E; 840 rows).

## EXCLUDED facts

- Ch. 30: AAPG kerogen H/C ranges (403), the IAEA Oklo page (stub to curl, 402 to WebFetch) and
  IAEA TECDOC-1842 (download failed) not used: kerogen data from the DOE ACBP report, Oklo from
  four OSTI abstracts, uranium deposits from USGS Bulletin 1693. O/C of the seven immature
  kerogens is not reported: the van Krevelen diagram plots only the Green River path and marks
  the others' H/C as ticks. Removed in review as unsourced: "land plants" for type III, vitrinite
  "woody", the 546 nm wavelength, oil shrinkage by dissolved gas, causes of low recovery (bypassed
  oil, capillarity), the clay cap of geothermal systems and cold-water short-circuiting, roll
  fronts "advancing", uranium "chiefly mined" from two types, mud logging in the field box,
  "since 2008" for Oklahoma, that today's uranium cannot go critical.

- Ch. 29: nickel laterites not printed (Book 3 recalls bauxite only; SIR 2010-5070-H not read). No
  sourced density for "dense massive sulfides" in gravity surveys: sentence limited to plutons. The
  "mean + 2 sd" anomaly threshold is presented as one simple convention (exercise 29.9), not a fact.
  USGS OFR 2008-1155 Table 1 gives the 90th-percentile grade as 0.24 %; the 422-row file gives
  0.25 % by linear interpolation: the text prints the report's 0.24.

- Colbourn et al. 2013 state that the linearised weathering law is within 10 % of the
  Arrhenius law for -26 < T - T0 < 31 K; their own formula gives +30 % at +30 K
  (exact 11.97 against 15.50). Not printed; exercise 26.6 derives the true 10 %
  limit, 17.9 K.
- Derry 2024's abstract says volcanic + metamorphic degassing is about 23 % of
  inputs; his Table 1 gives (11.3 + 3)/36.7 = 39 %. The text says "little more
  than a third" (exercise 26.2), from the table.
- Judd et al. 2024 (PhanDA) data carry no licence statement: numbers quoted from
  the paper with ledger rows, no dataset fetched.
- Unsourced hooks and details removed in review: "fourteen drill sites", "some
  ninety researchers", Cretaceous sea level and black shales (now a cref to
  ch. 19), Tasman Gateway "before the glaciation", core colours and sampling
  interval in the inthelab box, "late Carboniferous" for the Serpukhovian.

- Ch. 28: undrr.org terminology pages sit behind a Cloudflare challenge (HTTP 403 to tools):
  the same definitions were taken from the UN document A/71/644 (documents.un.org PDF).
- Ch. 28: the USGS photo page of the Banda Aceh mosque (walrus.wr.usgs.gov) is gone; the
  caption facts come from its Internet Archive copy (2010).
- Ch. 28: NCEI "maxWaterHeight" is printed as "maximum water height", not as "run-up".

- Ch. 31: the SERC isotope-dilution sheet is gone (404), so the ID equation is derived from the
  isotope mass balance; the RSC 2014 article (403), the UCSC Sr page (login) and bgs.ac.uk report
  URLs (404) were not used (BGS reports read from the NORA eprints). The USGS diabase photo page
  has no texture description: not used. No fetched source gives WDS crystal d-spacings (LiF, PET,
  TAP), so there is no Bragg-angle calculation. Removed as unsourced: "the most common way" for
  point counting, lighter isotopes evaporating first from the TIMS ribbon, "nanograms", NBS 987
  as strontium carbonate, "several kilograms" of sample, spacing of microprobe points, porphyroblasts
  "nucleating rarely". The Delesse area = volume statement is proved (Cavalieri), not cited.
  Invented: sample VH-23, its point count, the bead intensities of the real reference materials
  (their recommended SiO2 is real), the other-oxide sum and all mixture ratios; the problem takes
  the CIAAW abundances for the granite (its 87Sr/86Sr 0.714 differs slightly), stated in the text.

## Defects found elsewhere

- Source-level only (Colbourn 2013 approximation claim, Derry 2024 abstract vs
  table): see EXCLUDED. None in the repo so far.

## Searches

Web searches used: about 14, none for ch. 31 (direct fetches only) (ch. 30: kerogen kinetics, Easy%Ro, TTI table, Oklo, CO2 storage efficiency; ch. 26: RokGeM weathering, sediment carbon inventory, Judd 2024, CenCO2PIP 2023; ch. 28: BJF97 GMPE, Newhall-Hoblitt event trees; ch. 29: USGS SIR 2010-5070 models, orogenic gold model, kimberlite source).

## Traps (new)

- While ch. 21 (first agent) does not compile, my scratch probe
  `tools/probe.sh <slug>...` builds only my chapters + solutions from a scratch
  entry file (layout identical within a chapter; page numbers and cross-chapter
  refs are not). Use it to check, then rebuild the whole book for FIGCHECK pages.

- `omfigure` + pgfplots with `clip=false`: anything placed outside xmin/xmax
  (a glaciation band at 445 Ma on a 0-430 axis) is drawn over the tick labels.
  Widen the axis instead.
- TikZ `\fill` after `\addplot` inside an axis paints over the curve: draw
  shading first.
- FIGCHECK uses PRINTED page numbers (physical page - 11 in this build).
- Pending for the end of my range: credit items for the CC BY datasets
  (CENOGRID, Foster 2017) and my photographs go into
  `frontmatter/image-credits-book4.tex` before `\end{itemize}` once ch. 21-25's
  items have landed, so that the list stays in chapter order.
- GMPE choice: Boore, Joyner and Fumal 1993 (USGS OFR 93-509, public domain) has a
  scanned table; its text layer was right but was checked on the page image. Its
  logarithms are decimal: B2 0.229 = 0.527/ln 10 of the 1997 natural-log version.
- Two pgfplots axes side by side: `width=0.5\linewidth` each plus `\hfill` wraps them one
  under the other (labels count). Put each in a 0.49 minipage with width about 0.93-0.97
  of it; `width=\linewidth` inside the minipage overflows by 1-8 pt.
- `\qty{..}{years}` and `{days}`: write numbers with words instead (siunitx units only).
- The first agent's chapters keep landing during my builds (ch. 22 brought 14 undefined
  solution refs for a while): rebuild before reading page numbers, and take printed page =
  physical - 11 from the current build only.
- Credits pending (end of range): ch. 28 photographs (Caraballeda, Lawson Smith / US ACE,
  PD; Banda Aceh mosque, USGS, PD) also go into frontmatter/image-credits-book4.tex.
- Ch. 29: the first agent's ledger already holds source USGS-SIR-2010-5070E and row usgs10:bushveld
  (ch. 8): my chromite row usgs10e:chromite reuses that key. Other SIR 2010-5070 chapters are keyed
  USGS-SIR-2010-5070A/B/C/I/L/N/O/Q (same convention).
- The printed page offset is now physical - 12 (front matter grew): read it from each build.
- A dual-axis pgfplots panel (axis y line*=right) in a 0.49 minipage overflows at 0.93 width: 0.80.
- Credits pending (end of range): ch. 29 photos (Bingham Canyon ISS, NASA PD; Flambeau gossan, James
  St. John CC BY 2.0) and the OFR 2008-1155 dataset (PD) go into frontmatter/image-credits-book4.tex.
- `tools/photo.py` takes a BASENAME for the output file: given a full path it wrote the path into
  CREDITS.md and doubled the author ("Unknown authorUnknown author"); the row was rewritten.
- OSTI API (osti.gov/api/v1/records) returns HTML unless the request sends `Accept: application/json`.
- Easy%Ro gives Ro about 0.24 % after 2 Myr at 20 degC (its floor is 0.20 %): tests must not
  expect Ro < 0.2 at low temperature.
- `\foreach` with `\y` or `\k` inside a pgfplots axis: "Undefined control sequence" at
  \end{axis} (coordinates are expanded late): unroll the loop.
- `stack plots=y` with `\closedcycle` and `area style` drew the top band over everything and hid
  the nodes: draw stacked bands as explicit `\fill` polygons from cumulative values.
- The gate "home experiment or curriculum mention" fires on the word "programme" (even "laboratory
  programme"): write "study".
- Credits pending (end of range): ch. 30 photograph (Geyserville, US DoD, PD) and the NIST WebBook
  CO2 data go into frontmatter/image-credits-book4.tex.
- Ch. 31: other agents run latexmk almost continuously; a loop that waits for "no latexmk" never
  returns. Run the capped probe/build directly (systemd-run memory cap) instead.
- Ch. 31: `\qty{27}{}` is not a dimension product: use `\qtyproduct{27 x 46}{mm}`.
- Ch. 31: a subset of marks in pgfplots (granite stations only) works with
  `x filter/.expression={\thisrow{unit}==2 ? x : nan}` on the same table.
- tools/check_problem_numbering.py and check_exercise_calibration.py need the directory argument
  (`parts/bachelor-2`); without it the first errors out and the second prints its usage text.
