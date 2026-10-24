# PROGRESS --- Book 5 (University Year 3, `bachelor-3`, prefix `b3`)

Written by the Book 5 agent. A fresh agent resumes from this file alone,
plus `sources/BATCH_BOOKS_1-5.md` (binding), `BRIEFS.md` and
`DEFINITIONS.md` in this directory.

## State

- **Phases B, C and D done (2026-10-23).** All 31 chapters written, built
  0/0/0, gated green, figure-checked; Phase C (linker, full FIGCHECK pass,
  scripted solutions re-read, AI stubs) closed; the Phase D report went to the
  coordinator. Final build: **456 PDF pages** (444 printed: text 1--368,
  solutions 369--439, index 440--444), 0 errors, 0 undefined, 0 overfull.
- AI images: 21 JPEGs in `images/book5/ai/`, 19 used; `ai_stubs.py --book 5
  --list` empty; no PNG. Two generated images are unused alternates
  (`b3-rotating-table.jpg`, `b3-modelling-centre.jpg`; the chapters use
  `b3-rotating-tank.jpg` and `b3-model-centre.jpg`), left in place for the
  user to delete or keep.
- Ledger `sources/ledger/book5.md`: 220 source rows, 340 data rows;
  `check_ledger.py` OK (2432 rows in all); Wikipedia landing check = 0.
- Web searches/fetches: **~605** after ch. 31 (budget ~600; ch. 31 used ~30).
- Scratch: `/tmp/claude-1000/-home-bvirrion-repositories-one-course/073e8d3d-6c62-4a98-8f56-8a0346dd7a8a/scratchpad/book5/`
  (`calc/chNN.py` = the per-chapter calculators; `tools/findpage.sh` = find
  the PDF page holding a phrase; `renders/` = per-page 130-dpi checks, one
  fresh subdirectory per round; `src/` = downloaded sources; `fc2/rows.json`
  = the 209 figure objects with their pages in the final build).

## Sync 3 rulings (resolved)

Phase rule recalled from chemistry (Y3 defines the mineralogical phase rule
and the pseudosection); Walther's law mine (ch. 17); stereographic and
equal-area projection (of the sphere) mine (ch. 8); re-derived owned notions
in unindexed theorems; magnetostratigraphy, Darcy's law, Glen's flow law,
radar interferometry new; heat equation recalled as "the diffusion
equation"; style has groupplots, \Msun \Mearth \Rearth \Mjup \Rjup, \dex,
\darcy (no stereonet pic); datasets approved for my `# Book 5:` block
(IGRF-14, USGS splib07, Exoplanet Archive PSComp, Eilers 2019, Asplund 2021,
optional NSIDC; IMBIE tables for ice mass); read-only use of
`grade-11-seafloor-age.csv` and `grade-8-nsidc-sep-extent.csv`; Varden
dolerite dyke allowed in my figdata only (buried, below the unconformity);
`region.contact_elevation` returns nan in the fault gap (guard every call).

## Chapter status

| # | slug | brief | ledger | text | exos | problem | solutions | figures | FIGCHECK | pp |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | seismology-imaging | done | done | done | 12 | 26 q | done | 9 (4 S, 4 F, 1 AI) | 9 rows | ~18 |
| 2 | exploration-seismology | done | done | done | 12 | 23 q | done | 11 (5 S, 4 F, 2 AI) | 11 rows | ~15 |
| 3 | gravity-geodesy | done | done | done | 12 | 24 q | done | 8 (3 S, 3 F, 1 photo, 1 AI) | 8 rows | ~15 |
| 4 | palaeomagnetism | done | done | done | 12 | 24 q | done | 8 (3 S, 4 F, 1 AI) | 8 rows | ~16 |
| 5 | lithosphere-thermal-models | done | done | done | 12 | 23 q | done | 5 (1 S, 3 F, 1 AI) | 5 rows | ~13 |
| 6 | mantle-convection | done | done | done | 12 | 26 q | done | 7 (3 S, 3 F, 1 photo) | 7 rows | ~14 |
| 7 | deformation-mechanisms | done | done | done | 12 | 24 q | done | 7 (3 S, 2 F, 1 photo, 1 AI) | 7 rows | ~13 |
| 8 | structural-analysis | done | none needed | done | 12 | 27 q | done | 8 (3 S, 4 F, 1 AI) | 8 rows | ~15 |
| 9 | extension-strike-slip | done | done | done | 12 | 23 q | done | 6 (3 S, 2 F, 1 photo) | 6 rows | ~12 |
| 10 | orogenic-wedges | done | done | done | 12 | 25 q | done | 6 (2 S, 3 F, 1 AI) | 6 rows | ~13 |
| 11 | petrological-thermodynamics | done | done | done | 12 | 22 q | done | 4 (3 F, 1 AI) | 4 rows | ~11 |
| 12 | trace-element-modelling | done | done | done | 12 | 23 q | done | 4 (1 S, 3 F) | 4 rows | ~11 |
| 13 | advanced-geochronology | done | done | done | 12 | 25 q | done | 5 (1 S, 4 F) + 1 AI | 5 rows + AI | ~13 |
| 14 | stable-isotopes | done | done | done | 12 | 22 q | done | 4 (1 S, 3 F) + 1 AI | 4 rows + AI | ~11 |
| 15 | water-rock-interaction | done | done | done | 12 | 24 q | done | 4 (1 S, 3 F) + 1 P | 4 rows + P | ~12 |
| 16 | sequence-stratigraphy | done | done | done | 12 | 24 q | done | 5 (2 S, 3 F) + 1 P | 5 rows + P | ~12 |
| 17 | facies-models | done | done | done | 12 | 24 q | done | 6 (5 S, 1 F) + 1 P + 1 AI | 6 rows + P + AI | ~12 |
| 18 | quantitative-geomorphology | done | done | done | 12 | 24 q | done | 5 (2 S, 3 F) + 1 P | 5 rows + P | ~11 |
| 19 | gfd-foundations | done | done | done | 12 | 25 q | done | 6 (3 S, 3 F) + 1 AI | 6 rows + AI | ~12 |
| 20 | atmospheric-dynamics | done | done | done | 12 | 23 q | done | 5 (2 S, 3 F) + 1 P | 5 rows + P | ~10 |
| 21 | ocean-dynamics | done | done | done | 12 | 26 q | done | 7 (3 S, 4 F) + 1 P | 9 rows + P | ~13 |
| 22 | climate-models | done | done | done | 12 | 24 q | done | 7 (2 S, 3 F) + 1 P + 1 AI | 18 rows + P | ~12 |
| 23 | hydrogeology | done | done | done | 12 | 22 q | done | 7 (2 S, 4 F) + 1 AI | 11 rows | ~11 |
| 24 | glaciology | done | done | done | 12 | 22 q | done | 6 (2 S, 2 F) + 1 P + 1 AI | 15 rows + P | ~12 |
| 25 | remote-sensing-gis | done | done | done | 12 | 22 q | done | 8 (2 S, 4 F) + 1 P + 1 AI | 17 rows + P | ~14 |
| 26 | planetary-interiors-surfaces | done | done | done | 12 | 24 q | done | 6 (2 S, 2 F) + 2 P | 27 rows + 2 P | ~11 |
| 27 | planetary-atmospheres | done | done | done | 12 | 25 q | done | 7 (1 S, 4 F) + 2 P | 26 rows + 2 P | ~12.5 |
| 28 | exoplanets | done | done | done | 12 | 25 q | done | 9 (2 S, 6 F) + 1 P | 21 rows + 1 P | ~13 |
| 29 | milky-way-galaxies | done | done | done | 12 | 25 q | done | 9 (3 S, 4 F) + 2 P | 24 rows + 2 P | ~16 |
| 30 | origin-of-elements | done | done | done | 12 | 25 q | done | 6 F + 2 P | 33 rows + 2 P | ~14 |
| 31 | field-lab-methods-3 | done | done | done | 12 | 25 q | done | 6 (1 S, 5 F) + 1 AI | 7 rows | ~14 |

## Page projection

Target: 31 chapters x ~12 pp (course ~8.5, exercises ~1.5, solutions ~2) =
**~372 pp** + front matter. Projection at Phase A: 372 pp (briefs sized at
5--6 sections, ~4 schematics + 3--4 figdata plots per chapter). Re-project
after chapters 8, 16, 24 and 31 from the build's page count; more than 10 %
under (< 335 pp at the end, or < 10.8 pp/chapter at a checkpoint) means
restoring depth (derivations, worked examples, the `inthefield` boxes) before
moving on.

| checkpoint | chapters | pp so far | pp/chapter | projection | action |
|---|---|---|---|---|---|
| Phase A | 0 | 43 (placeholders) | --- | 372 | --- |
| after ch. 8 | 1--8 | 120 (text pp. 10--110 = 101, solutions pp. 135--153 = 19) | 15.0 (text 12.6, solutions 2.4) | ~465 at this rate | 25 % OVER, not under: no depth to restore. Tighten the rest to ~12--13 pp (text ~10.5): fewer schematics per chapter (3--4 figures + 1 box), shorter prose around the theorems; expected end ~410 pp |
| after ch. 16 | 1--16 | 216 (text pp. 1--180 = 180, solutions pp. 197--232 = 36) | 13.5 overall; ch. 9--16 alone 10.9 (text 8.75, solutions 2.1) | 216 + 15 x 11.5 = ~390 + front matter | on target (372 x 1.05); ch. 9--16 near the 10.8 floor: keep the remaining chapters at 11.5--12 pp (5 sections, a worked example or box each), do not tighten further |
| after ch. 24 | 1--24 | 321 (text pp. 1--270 = 270, PDF 13--281; solutions PDF 290--341 = 52) | 13.4 overall; ch. 17--24 alone 13.4 (text 11.25, solutions 2.1) | 321 + 7 x 12.5 = ~409 + front matter | 10 % OVER target, not under: no depth to restore; keep ch. 25--31 at 11.5--12.5 pp (5 sections, 4--6 figures, one box) |
| after ch. 31 (final) | 1--31 | 439 (text pp. 1--368, PDF 13--380; solutions pp. 369--439 = 71) + index 5 = 444 printed, 456 PDF | 14.2 overall; ch. 25--31 alone 14.0 text+solutions | --- | 18 % over the 372 target, never under: no depth to restore |

## Sources

- Search estimate: **~560--600** fetches (≈ 18 per chapter on average;
  ledger-heavy chapters 1, 3, 4, 6, 7, 13, 14, 22, 24, 26--30 at 25--30,
  the Varden-based and analytic chapters 8, 9, 12, 16--19, 23, 31 at 8--12).
  Count every WebSearch/WebFetch here as it happens.
- Every number: a ledger row with a directly fetched source (URL + access
  date); never memory, never a search snippet, **never Wikipedia/Wikibooks**
  (Commons only for photo credits). No source reachable: drop the number,
  list it under EXCLUDED below.
- Never put the user's e-mail anywhere (no User-Agent, no request, no file);
  a source that demands one is not used (e.g. some data portals, NCBI-style
  APIs; Earthdata login = use another source).

| date | searches+fetches (cumulative) | note |
|---|---|---|
| 2026-10-23 | 0 | Phase A: planning only |
| 2026-10-23 | ~120 | after ch. 8 (estimate; ch. 8 used none: Varden data invented, everything derived) |
| 2026-10-23 | ~140 | after ch. 9 (OpenAlex x 13, USGS page 1, Commons x 6) |
| 2026-10-23 | ~150 | after ch. 10 (OpenAlex x 7, J-STAGE PDF x 2) |
| 2026-10-23 | ~165 | after ch. 11 (USGS Robie-Hemingway PDF, OpenAlex x 8, minsocam 404) |
| 2026-10-23 | ~171 | after ch. 12 (White ch. 7 PDF, OpenAlex x 3, Wiley PDF blocked, Springer PDF) |
| 2026-10-23 | ~185 | after ch. 13 (White ch. 8 PDF, OSTI Schaen 2020, UCL Kohn 2024, Zeigler 2023, Zech 2004, Balco 2008, OpenAlex x 6) |
| 2026-10-23 | ~200 | after ch. 14 (White ch. 9 PDF, Dansgaard 1964, Gkinis 2014, isogeochem docs, Planavsky 2022, Dickens 2011; OpenAlex out of budget, WebSearch + curl) |
| 2026-10-23 | ~212 | after ch. 15 (PHREEQC dat x2, Hem WSP 2254, P&K OFR 2004-1068, USGS record White and Brantley, West 2005 search + PDF, Commons search x2, NPS/USGS travertine search + 2 pages) |
| 2026-10-23 | ~226 | after ch. 16 (Laskar 2004 A&A x2 captcha-blocked, HAL record + PDF, Miller 2020 PMC x2, OSTI Pattison 1995, Commons search x3 + API + 2 downloads, LR04 header read from data/raw) |
| 2026-10-23 | ~236 | after ch. 17 (USGS TWRI 2-E2 landing + PDF list + PDF, WebSearch wave base, GSA abstract, Commons search x3 + API x5 + 1 download) |
| 2026-10-23 | ~256 | after ch. 18 (WebSearch x5: scarp diffusivity, Cook 2020, Harel 2016, hillslope D, Niagara; USGS pubs page, Cook PMC x2, IJC x2, MIT OCW page x3 + 3 PDFs, Commons search x3 + API x3 + 3 downloads) |
| 2026-10-23 | ~264 | after ch. 19 (NASA GRC atmosmet + specheat, Stewart LibreTexts 9.1, 8.5, 8.3, WebSearch x3 for the Stewart sections) |
| 2026-10-23 | ~270 | after ch. 20 (WebSearch x2: Rossby 1939, Charney 1950; EliScholar x3 (two blocked), Crossref x2, Tellus page + PDF, Commons search + API + thumbnail) |
| 2026-10-23 | ~284 | after ch. 21 (Stewart LibreTexts 17.4, 10.4, 11.1, 11.2, 11.3, 13.3, 17.5; NASA Moon fact sheet; Commons search + API + download; NCEP air.sig995 OPeNDAP fetch for ch. 22) |
| 2026-10-23 | ~292 | after ch. 22 (Budyko 1969 Tellus landing + PDF; AR6 WGI ch. 1, ch. 7, ch. 7 SM PDFs; Commons API + thumbnail for the NCCS photo, one rate-limited retry) |
| 2026-10-23 | ~300 | after ch. 23 (Heath 1983 WSP 2220 PDF, chart read at 200 dpi; EPA CEAM on-site dispersivity page; USGS TWRI 08-A3 landing + PDF) |
| 2026-10-23 | ~312 | after ch. 24 (PISM rheology docs, CICE index/constants, AR6 WGI ch. 9 PDF; ERDDAP etopo180 transect; NSIDC N_03/N_09 v4.0 CSVs; Commons search + API + thumbnail) |
| 2026-10-23 | ~342 | after ch. 25 (USGS Landsat 8 x2, ESA Sentinel-1/-2 pages, NASA EO NDVI, ICESat-2 x3, ECOSTRESS ~25 list/file fetches, ScienceBase splib07 x3 blocked (403), USGS FS 2005-3025, VHP InSAR page, TM 13-B1 PDF; Commons search + API + thumbnail) |
| 2026-10-23 | ~392 | after ch. 26 (LPI CB-954 PDF; Craterstats functions.txt; arXiv 0903.5137, 1212.4630, 1810.00725; NTRS x3 (Yoder 2003, Veeder 1994, Gronoff); JPL InSight and Juno-Europa, AGU Mercury, NASA Moon facts, moonquakes, Io, Io facts, Europa, Enceladus, Venus facts, Tharsis; NSSDCA Jovian satellites; Commons search x3 + API x4 + 2 thumbnails; failed: NASA moon-core 2011 (404), JPL curl (403), ADS (405), Paris Observatory (refused), Lainey HDR (timeout), IOP/DOAJ (403)) |
| 2026-10-23 | ~425 | after ch. 27 (arXiv 1301.6674v2, 1804.05889, 1809.06960, 1306.3266, 1507.02569, 2505.16692 PDFs; arXiv API x4; ORFEO Gronoff 2020 PDF; NTRS 19820047738 and 20210017415; LASP MAVEN release; NASA Titan facts; NIST WebBook methane; Commons search x6 + API x8 (one rate-limit refusal, retried) + 3 downloads; failed: IMCCE and Paris Observatory Mars obliquity (timeout, refused), HAL (Anubis)) |
| 2026-10-23 | ~470 | after ch. 28 (Exoplanet Archive TAP x3 (one test, two fetches), acknowledgement page; Zeng planet-models page + 4 tables (+1 table not used); arXiv abstracts x12 (1703.10375, 1311.6806, 1205.2273, 2208.11692, 1512.08827, astro-ph/9911436, 2303.14849, astro-ph/0404309, 0811.2606, 2208.14990, 1705.10810, 1708.01621) + Wright 2012 PDF; Nobel 2019 press release and scientific background PDF; ESO ESPRESSO page; ESA/Webb image page (wrong id, unused); Commons search x5 + API x5 + 1 download) |
| 2026-10-23 | ~535 | after ch. 29 (arXiv abstracts/PDFs: Eilers 2019, Pouliasis 2017, GRAVITY 2019 and 2021, Reid 2020, Bovy 2017, Bland-Hawthorn and Gerhard 2016, Liu 2011, Buta 2011, Dobbs and Baba 2014, McConnachie 2012, Kravtsov and Borgani 2012, Soszynski 2015, Freedman 2019, Riess 2022, Planck 2018, McGaugh 2000; CDS ReadMe, directory, lmccep.dat.gz, VizieR licence x2; OGLE pages x3 (cepF.dat unused); ESA Gaia DR3 page; NRAO ERA ch. 7; BIPM frequencies page (no H line, unused); OpenStax x4 (unused); Commons search x3 + API x4 + 2 downloads) |
| 2026-10-23 | ~575 | after ch. 30 (arXiv e-print tar 2105.01661 and abstracts/PDFs: Kaeppeler 2011, Cowan 2021, LIGO 2017, MMA 2017, Matteucci 2021, Kobayashi 2020, McKee 2015, Casagrande 2011; exp-astro.de KADoNiS table (kadonis.org parked); IAEA LiveChart API; CDS J/A+A/530/A138 ReadMe and catalog; PDG BBN review 2024 and 2025; NIST neutron mass; aanda.org x3 (403); Commons search + API + 2 downloads) |
| 2026-10-23 | ~605 | after ch. 31 (GPG, Geophysics for Practicing Geoscientists, UBC-GIF: the gravity, magnetics, physical-property, DC-resistivity and GPR pages behind ledger rows gpg 556--574, about 25 page fetches; no image search: the crew scene is an AI image) |

### EXCLUDED (numbers dropped for lack of a citable source)

(none yet)

## figdata and tests planned (one tested script per name; tests in `tests/bachelor-3/`)

ray_tracing, love_dispersion, tomo_checkerboard (ch. 1); cmp_nmo,
synthetic_seismogram, refraction_dip (2); j2_figure, grace_mass, flexure
(3); igrf_field, palaeomag_stats, apw_path (4); plate_cooling,
continental_geotherm (5); convection_scaling, gia_relaxation, ridge_push (6);
flow_laws, deformation_map (7); stereonet, palaeostress (8);
domino_extension (9); critical_taper, age_elevation (10); reaction_line,
gx_solvus, al2sio5 (11); melting_models (12); concordia, arar_spectrum,
model_ages, cosmogenic (13); rayleigh_distillation, lr04_d18o,
carbon_mass_balance (14); carbonate_system, activity_diagram,
weathering_rates (15); shelf_model, lr04_periodogram (16); well_logs (17);
hillslope, stream_profile, varden_river (18); inertial_oscillation,
thermal_wind, buoyancy_frequency (19); rossby_waves, eady, held_hou (20);
ekman_spiral, stommel_gyre, sverdrup_transport, equilibrium_tide (21);
ebm_0d, budyko_sellers, two_layer (22); theis, flow_net,
advection_dispersion (23); ice_flow, sea_ice (24); spectral_signatures,
insar_mogi, varden_gis (25); two_layer_planet, crater_sfd (26);
jeans_escape, runaway, planet_atmospheres (27); rv_transit,
exoplanet_archive (28); rotation_curve, distance_ladder (29);
solar_abundances, s_process, gce (30); gravity_granite, magnetic_anomaly,
ves (31). ~75 scripts. Test defining points are listed in the Phase A
report (item 5) and repeated in each script's docstring when written.

Script skeleton: `sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))`,
`from _table import write_table`, `write_table(__file__, header, rows,
part=None, digits=6)` → `figdata/out/bachelor-3-<name>[-part].dat`; datasets
read only from `data/derived/`. Run with `make figdata Y=bachelor-3`, tests
with `make test Y=bachelor-3`, both under the resource caps.

## Traps (read before every chapter)

1. **region.py nan:** `contact_elevation(name, x, y)` returns `nan` where a
   vertical meets no contact (the gap the normal fault cuts out). Guard
   every call (`np.isfinite`) in ch. 2, 8, 17, 18, 23, 25, 31 scripts; test
   that no nan reaches a `.dat` file.
2. **omfigure has no counter:** never `\cref{fig:...}`; "the figure below".
3. **No `\cref` across books**; prose pointers only ("the Year 1 volume").
4. **Double rounding:** compute every printed answer from the raw value and
   round once; solutions computed from the *printed* (rounded) data.
5. **A term defined twice is dropped by the linker:** never index an owned
   term in a theorem that re-derives it (Ekman spiral, Rossby wave, normal
   gravity, AFC, depth--age law): title the theorem by content.
6. Blank lines inside a pgfplots `table` give nullfont noise; `bar shift=0pt`
   for single-series bars; `\permil` only inside siunitx (`\qty{..}{\permil}`).
7. `% ledger: <id>` comments go **after** their paragraph; no hyphen in a
   ledger source-key prefix; ids unique across `sources/data_ledger.md` and
   `sources/ledger/*.md` (grep first).
8. **Wikipedia numbers have contradicted primary sources** (Books 1--3):
   never a wiki row; the landing check must stay 0.
9. groupplots and pgfplotstable are **not loaded** by the style (asked at
   the sync); until then, side-by-side `axis` environments.
10. Observation only (`inthefield`/`inthelab`, third person; gate 7b);
    policy wording warning (gate 7c); `dated` box needs its year (7d).
11. Printed text never names a curriculum, school system, university or exam
    (gate 7); institutions only in data and photo credits.
12. Qualified homographs (DEFINITIONS.md, last table); "magnetic
    declination" always in full.
13. AI images: `python3 tools/ai_images.py --book 5 batch.txt --work
    <scratch>/ai` from the repo root, detached; stubs via `tools/ai_stubs.py`;
    never wait with pgrep; JPEG only; review each image.
14. Photos: verify licence via the Commons API (no e-mail in the
    User-Agent); NASA/USGS/NOAA PD; ESA/ESO/Hubble CC BY 4.0 credited.
15. Resource caps: one core, ≤ 1.5 GB per process,
    `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1`; long jobs under `nice -n 19`
    and `systemd-run --user --scope -q -p MemoryHigh=2G -p MemoryMax=4G`;
    `latexmk` only on my entry, `nice -n 10`, never two at once, no short
    timeout. Scoped checks only (`tools/gates.sh bachelor-3`,
    `make test Y=bachelor-3`, `make figdata Y=bachelor-3`,
    `tools/link_defined_terms.py --book 5`).
16. Git read-only (`status`, `diff`, `log`); never commit/checkout/stash/
    reset/restore/clean/add. No wildcard `rm`, even in scratch: render into
    fresh subdirectories.
17. Own files only: `parts/bachelor-3/**`, `figdata/bachelor-3/**`,
    `tests/bachelor-3/**`, `sources/book5/**`, `sources/ledger/book5.md`,
    `tools/term_config/book5_en.py`, one `# Book 5:` block in
    `tools/fetch_data.py`; `styles/oneearth.sty` append-only and preferably
    via the sync.

Ch. 2 note: the named number changed from the brief. The basement crops out at
the anticline crest of the Varden model, so the problem's named number is the
depth of the basement unconformity below CMP S on the syncline axis (hanging
wall), 1011 m from the rounded printed times (model 1009.8 m).

Ch. 3 notes: dataset added in the `# Book 5:` block of tools/fetch_data.py
(IMBIE 2021 Greenland and Antarctica, UK Polar Data Centre RAMADDA, OGL v3, no
login); the brief's GRACE-only series replaced by the IMBIE reconciled series
(hard rule). One photo (NASA/JPL PIA22441); a second candidate (PIA22340, clean
room, carried manufacturer logos) was downloaded and deleted
(images/book5/b3-grace-fo-cleanroom.jpg, single named file). EXCLUDED: GRACE
spatial resolution (no direct source fetched); geoid highs over subduction
zones and hotspots (unsourced, dropped); a foreland-basin Te (not sourced).

Ch. 4 notes: dataset added in the `# Book 5:` block (IGRF-14 coefficients,
NOAA NCEI, ledger data:b5-igrf; product facts geomag5:igrf). The brief's
`apw_path` script is folded into `palaeomag_stats.py` (parts apw*, graticule);
`magnetostratigraphy.py` added. The IGRF maps are plate carree, not Mollweide
(the shared land file is lon/lat). Reused other books' rows read-only:
tarduno:curie (Book 2), tarduno:emperor and iodp:gpts2004 (Book 3). The
problem has Parts I-IV with the drift in Part IV (named number 2918 +- 355 km,
1 sigma from the I +- a95 palaeolatitude interval / 1.96). EXCLUDED: core flow
speed (no source fetched; the geodynamo told without numbers); westward drift
(no direct source); Laschamp and other excursion ages (no primary source
fetched; excursion defined without ages); a true-polar-wander rate (debated,
not quoted). Page budget: ch. 1-4 run at ~16 pp each against a 12-pp target:
later chapters must be leaner (~12-13 pp including solutions).

Ch. 5 notes: no new dataset (read-only use of grade-11-seafloor-age.csv per the
Sync 3 ruling, plus the shared ETOPO 1 deg). Book 3 had already proved the
depth--age law (admitting the erf profile), so ch. 5 derives the erf profile by
similarity and recalls the law. New sources: Honda and Yuen 2004 (GDH1 values
95 km, 1450 C, alpha 3.1e-5, k 3.1), Davies and Davies 2010 (hydrothermal
deficit). The [S] heat-flow probe schematic of the brief dropped (the AI image
and the box suffice; page budget). EXCLUDED: binned heat-flow data (Stein and
Stein 1992 closed, no open table fetched; the heat-flow panel shows models
only); xenolith geotherm values (no source fetched; told without numbers);
Richards et al. 2018 plate parameters (not fetched). AI batch 2 (heat-flow
probe) generated and reviewed. The problem's ocean is invented (corrected
depths 5700 m at 120 Myr, 4800 m at 40 Myr; named number L = 102.9 km).

Ch. 6 notes: no new dataset (PREM read only, for the mean mantle density 4476
kg/m3, g 9.8-10.7 m/s2 by integration, and mu = rho vS^2 = 7.7e10 Pa at 300
km). New sources: Mitrovica 1996, Milne et al. 2004, Zhao et al. 2012, Vestol
et al. 2019, Sleep 1990, Steinberger and Torsvik 2012 (abstracts via OpenAlex),
one Commons photo (Ballyhillin raised beach, Borchert, CC BY-SA 4.0). Reused
read-only: sella07:gia, fu75:slab-pull, nnr56:rms, b2dd10:half-space and
:continents (Book 2), honda04:gdh1, delaney86:properties. The brief's ledger
shoreline points for the GIA figure were not fetched: the figure shows the
model curves only. Ra_c = 27 pi^4/4 and 1708 are mathematical results (no ledger
row). The mantle Ra uses dT = 1450 K, the plate model's (a stated model choice).
Hook moved from Hudson Bay to the Gulf of Bothnia (the "ice gone 10 ka" date is
sourced for Fennoscandia only; Hudson Bay keeps its rate). EXCLUDED: a Hudson
Bay deglaciation date (not fetched); Forsyth-Uyeda per-plate table (only the
abstract's ratio 10 used); plume-head sizes (told only via an exercise with
invented values). Problem: invented Lake Ardo (250 km, 300 m, 50 kyr stand,
drained 14 kyr ago); named number log10 eta = 20.48.

Ch. 7 notes: no dataset. New sources: Azuma and Katayama 2017 (EPS, CC BY;
Table 3 of olivine flow laws after Hirth and Kohlstedt 2003), Stipp and Tullis
2003 (quartz piezometer), Mei and Kohlstedt 2000a,b, Karato and Wu 1993
(abstracts via OpenAlex); one Commons photo (augen mylonite, Mikenorton, CC
BY-SA 4.0). Reused read-only: lopez:flow-laws and codata:R (Book 3),
bowen14:mgo-sio2 (forsterite 1890 C; Book 4), morvel:range (Book 3). The
brief's strength-versus-depth figure dropped: Book 3 already draws the strength
envelope with the same laws (recalled in prose; page budget). Wet olivine and
the Hirth et al. 2001 quartz law not used (both need a water-fugacity term the
fetched sources do not give consistently); water weakening told by the
Mei-Kohlstedt factors. Mica-fish and sigma-clast geometries drawn for dextral
shear from the vorticity argument (clockwise rotation, tails dragged by the
faster layer). EXCLUDED: Peierls stress values, Burgers vector lengths (told
without numbers); delta-clast drawing (defined only). Problem: invented Varden
shear zone at 15 km, 450 C, 400 m wide, psi 84 deg; named number 1190 kyr.

Ch. 8 notes: no dataset, no ledger rows (the Varden readings and faults are
invented from figdata/shared/region.py; projections, orientation tensor,
Wallace--Bott, Fry and depth-to-detachment are derived). Figdata:
stereonet.py (nets, pi-diagram, girdle/beta, fault planes and slips, stress
axes; the brief's separate `palaeostress` script folded into it, with the
grid-search inversion and phi_from_rake) and fry.py (random-sequential-addition
population, strain R 2 at 30 deg, void fitted by 36 sector minima: 1.89 at
30.4 deg). Tests: tests/bachelor-3/test_structural_analysis.py (6). Rake
convention is Book 3's (from the strike, -90 normal, +90 reverse, 0 sinistral);
the hanging wall slips along -tau with compression positive (checked on normal
and reverse cases). Recalls: Book 3's hinge-from-limbs proposition and fold
classes (gentle 180--170, open 170--90), Anderson, rake, P/T; the balanced
cross-section and decollement recalled from the Year 2 volume's Alps chapter
(a placeholder at the time of writing: the recall sentence states only the
standard definition). Problem: twelve readings, five faults; named number:
plunge of the Varden fold axis 1.9 deg (the 2 deg of region.py, +-0.3).
Excess-area result (19 km) used as a teaching point (gentle folds over a deep
detachment, or synclines below the regional). EXCLUDED: none.

Ch. 9 notes: no dataset. New sources: McQuarrie 2005 (Basin and Range
reconstruction), Weber et al. 2009 (Dead Sea Transform), ten Brink et al. 1993
(Dead Sea basin gravity), the USGS San Andreas general-interest page (Schulz
and Wallace), Spotila et al. 1998 (San Bernardino transpression), Cooper et
al. 2010 (Snake Range footwall P-T), abstracts via OpenAlex; one Commons photo
(Basin and Range from the air, Ken Lund, CC BY-SA 2.0). Reused read-only:
byerlee:1975 (Book 3). Figdata: domino_extension.py (beta and the frictional
lock-up ratio; the brief's `pullapart` data plot dropped: Aydin and Nur 1982
not fetched, the pull-apart taught analytically with the Dead Sea numbers) and
rollover.py (listric fault, constant-heave rollover, sag area = H (D - z0)
tested). The brief's core-complex/Basin-and-Range photo: an aerial
basin-and-range view used (no free core-complex photo found in two Commons
searches). Hook uses the Snake Range 23-30 km (sourced) instead of the brief's
"15 km". Big Bend told through Spotila 1998's San Bernardino transpression
(no Big Bend geometry number). EXCLUDED: Aydin-Nur pull-apart aspect ratios;
Big Bend convergence angle; San Andreas slip-rate by segment (only the USGS
"up to 2 inches per year" drift). Problem: invented Merrow half-graben;
named number 8.7 km.

Ch. 10 notes: no dataset. New sources: Davis, Suppe and Dahlen 1983 (the
critical taper, Taiwan mu = 1.03 and mu_b = 0.85, the 15 km breakdown), Sueoka
and Tagami 2019 (closure-temperature table, J-STAGE PDF), von Hagke et al. 2014
(Central Alps basal strength), Deville 2021 (Jura 3-4 deg vs 12-13 deg tapers);
reused read-only: earle:settings (Book 2, 30 C/km), england:kelvin (Book 3,
kappa), ussa76:layers (Book 1, lapse rate). Figdata: fault_bend.py
(fault-parallel flow; excess area = slip x ramp height, tested), critical_taper.py
(small-angle Coulomb wedge, lambda inversion, beta* = mu_b/K), age_elevation.py
(steady advective geotherm + first-order topographic perturbation of the
closure isotherm; slope v/(1-f), tested against the PDE by finite differences).
Brief changes: the problem's wedge renamed Kestrel (the brief's 'Tessin' is a
real Alpine name); Suppe's constant-thickness relations named but not used
(fault-parallel flow drawn instead; no unsourced formula printed); closure
temperatures given as a table, not a figure; no real age-elevation profile
(none fetched). Trap: a fault-bend fold's excess area is S x ramp height, not
S x depth to detachment (the first test assumed the latter and failed).
EXCLUDED: Taiwan surface slope and basal dip values (not in the Davis et al.
abstract); a real age-elevation profile; sandbox shortening speeds.

Ch. 11 notes: no dataset. New source: Robie and Hemingway 1995 (USGS Bulletin
2131: 298 K properties and the 800-1200 K Gibbs energies of grossular,
anorthite, kyanite and quartz, with uncertainties). Reused read-only from Book 4:
kn88:gasp (experimental GASP line), h97:ideal and h97:fs-reaction (the
garnet-biotite thermometer), rh95:ab-jd-qz and rh95:al2sio5. Figdata:
gasp_tables.py (constant-property and tabulated lines, KN88 barometer,
thermometer-barometer intersection), schreinemakers.py (a binary four-phase
bundle from invented properties, by hull minimisation), regular_solution.py
(G_mix, binodal, spinodal, isobaric section). Not repeated from the Year 2
volume: the Al2SiO5 diagram, the triple point and the GASP/GB iteration as a
method; the chapter adds the heat-capacity theorem, calorimetry versus
experiment, the mineralogical phase rule, Schreinemakers, the regular solution
and pseudosections. Phase rule recalled from chemistry (Sync 3 ruling). Trap:
a garnet-biotite exchange built from Robie entropies of annite and phlogopite
gives absurd temperatures; the calibrated thermometer of the Year 2 volume is
used instead. Trap: \num{1/3} is a fatal siunitx error. Problem: the Varden
schist; named number 9.6 kbar (about 35 km). EXCLUDED: the experimental Al2SiO5
triple point (Holdaway 1971 abstract gives no numbers, Holdaway-Mukhopadhyay
1993 page 404); the Ferry-Spear calibration itself (no abstract; only Book 4's
rows are used); a real pseudosection.

Ch. 12 notes: no dataset. New sources: White, Geochemistry ch. 7 (Example 7.3:
spinel-lherzolite mode, melting proportions, La/Sm coefficients, non-modal
batch equation; the 60-90 km spinel-garnet transition), Rodrigues, Yaxley and
Kamber 2025 (garnet lherzolite GKR-001 subsolidus mode at 5 GPa, CC BY).
Reused read-only from Book 4: budahn91:d-ree (cpx / garnet / ol+opx+sp REE
coefficients), ms95:pm-trace, lodders:ci-table. Figdata: melting_models.py
(batch, fractional instantaneous / residue / aggregated, non-modal batch and
residue D, dynamic, inversions, ratio line; tested against a numerical ODE
integration and quadrature, and mass balance). Brief changes: Book 4 already
proves equilibrium crystallisation, the Rayleigh law and the AFC equation
(prop:b2:magmatic-differentiation:afc), so section 4 recalls them and only
composes melting with crystallisation (no re-derivation of AFC, no in-situ
crystallisation formula, which would need an unfetched source); the AFC box
schematic was replaced by a batch / fractional / dynamic schematic. REE
pattern figure limited to the nine REE with Budahn coefficients. Problem:
lavas A and B invented; named number 6.0 %. EXCLUDED: a garnet-lherzolite
mode from McKenzie and O'Nions 1991 (paywalled; replaced by the 2025 open
experiment); in-situ crystallisation (Langmuir 1989) formula; real porosities
for dynamic melting.

Ch. 13 notes: no dataset. New sources: White, Geochemistry ch. 8 (model ages,
DM 0.51315 / 0.2137, crustal Sm/Nd 0.13), Schaen et al. 2020 (Ar monitors,
plateau criteria, MSWD and its critical value; OSTI copy), Kohn et al. 2024
(fission-track physics and age equations; UCL repository), Zeigler et al. 2023
(alpha stopping distances, F_T), Zech 2004 (10Be production, muons, attenuation,
granite density), Balco et al. 2008 (Lambda = 160 g/cm2, P_SLHL = 4.96).
Reused read-only: Book 3 amherst:constants, amherst:arar, nmgrl:arar,
tulane:upb-zircon, iaea:isotopes, portenga:method/rates; Book 4 white:chur,
villa20:sm147, lugaro:slr-table; Book 5 sueoka19:closure. Figdata:
concordia.py (curve, ticks, zircons, ellipses, line, twline), arar_spectrum.py,
model_ages.py, cosmogenic.py; 15 tests (lead loss explicit vs chord, TW
straightness and transformed line, intercepts, MSWD expectation by Monte
Carlo, model ages, cosmogenic closed form vs path integration). The Varden
granite story is kept consistent with the Year 1 volume (Rb-Sr 310 Ma, zircon
~310.6, biotite K-Ar ~296): upper intercept 311 +- 10 Ma, Ar plateau 296.1 Ma,
lower intercept ~100 Ma (invented burial-time event), AHe 43-52 Ma, 10Be 20
m/Myr. The concordia ellipses part is written but not drawn (sub-millimetre at
print scale). Named number 311 +- 10 Ma. EXCLUDED: CA-TIMS chemistry details;
the apatite He partial-retention temperature range (concept only, closure
50-80 C used); a modern (post-2015) 10Be production rate and altitude/latitude
scaling factors; 26Al half-life and the 26Al/10Be production ratio (burial
dating told without numbers); a granite crystallisation temperature (700 C is
given as problem data); a zircon CL photo (the Year 1 volume has one).

Ch. 14 notes: dataset LR04 (shared, data:lr04). New sources: White, Isotope
Geochemistry ch. 9 (Rayleigh, mass-dependent fractionation, photosynthesis,
ice volume 0.011 per mil per m, S-MIF record), Dansgaard 1964 (temperature,
amount and continental effects; 0.69 t - 13.6 and 5.6 t - 100), Gkinis et al.
2014 (ice-vapour alpha for 18O and D after Majoube/Merlivat-Nief), the
isogeochem package (Kim and O'Neil 1997 calcite-water, Anderson 2021 unified
Delta47), Planavsky et al. 2022 (f_org debate), Dickens 2011 (PETM onset,
carbon masses). Reused read-only: Book 4 kc98:alpha, kc98:mwl, kc98:standards,
white:d13c; Book 2 iapws:melt-subl. Figdata: rayleigh_distillation.py (exact
variable-alpha Rayleigh along the IAPWS sublimation curve, stepwise variant),
carbon_mass_balance.py, lr04_d18o.py; 7 tests. Stations moved from -45 C to
-10/-20/-30 C: an isobaric Rayleigh model to -45 C gave -80 per mil and a
d-excess of 103, unrealistic. The model slope (1.6 per mil per K of
condensation temperature) vs Dansgaard's 0.69 per K of surface temperature is
explained qualitatively. Named number -48.3 per mil. EXCLUDED: the Majoube
liquid-vapour temperature equation (only two points sourced); the Mook/IAEA
isotope-hydrology volumes (host unreachable); White's palaeotemperature
equation 9.58 (sign inconsistent: T rises with Delta), replaced by KO97; an
Antarctic dD-T spatial slope; the seawater freezing point (stated
qualitatively in Q13); a Delta33S time series (schematic only); an ice-core
photo (an AI drilling-tent scene instead).

Ch. 15 notes: no dataset (PHREEQC as ledger rows only, per Sync 3); air
P_CO2 from the shared Mauna Loa row (2025 annual mean 427.35 ppm, log -3.37).
New sources: PHREEQC phreeqc.dat (USGS, PD; analytical log K of the carbonate
system, silicate log K, molar volumes), Hem 1985 WSP 2254 (extended
Debye-Hueckel A, B, ion sizes; SI uncertainty; soil and ground-water P_CO2;
calcite in air; conduit/diffuse springs; charge balance), Palandri and
Kharaka 2004 OFR 2004-1068 (rate law and parameters), White and Brantley 2003
(lab vs field rates, R = 3.1e-13 t^-0.61; USGS record abstract), West et al.
2005 (weathering regimes, 74 +- 29 kJ/mol; author-group copy), White ch. 9
sect. 9.7.1 (water-rock ratios), USGS YVO and NPS (travertine, 3 mm/day),
Commons PD photo of Palette Spring. Figdata: carbonate_system.py (open and
closed systems with extended DH, the spring, degassing, travertine),
activity_diagram.py, weathering_rates.py; 11 tests (analytic log K vs 25 C
values, cube-root theorem vs full solution, slope 1/3, Hem's 20 mg/L in air,
closed < open and cold > warm, spring balance and SI, degassing and
travertine, triple point and samples, boundaries, rate law). Named number SI
= +0.04. EXCLUDED: ion pairs (CaHCO3+, CaCO3 aq, CaSO4 aq; stated as
neglected); temperature dependence of A and B (25 C values used, Hem calls
the effect minor); the brief's soil P_CO2 ranges as numbers beyond Hem's
10-100 x air; a seawater carbonate-system calculation (recalled only); a
reaction-path calculation (principle only); named speciation software; field
rates as numbers (only "orders of magnitude"); lab dissolution rate of
quartz and calcite parameters (not plotted).

Ch. 16 notes: dataset LR04 (shared, data/derived/lr04.csv; sampling 1/2/2.5 kyr,
interpolated to 1 kyr per window). New sources: Laskar et al. 2004 (HAL
preprint; eccentricity Table 6, obliquity Table 7, p0 eq. 34, g_i Table 4;
precession periods derived), Miller et al. 2020 Sci. Adv. (EPR charts timing
vs amplitude factor 2-3, RSL controls and regression/transgression
definitions, Quaternary amplitudes, astronomical periods), Pattison 1995 AAPG
abstract on OSTI (Kenilworth Member facts), LR04 abstract in the NOAA file
header (tuning to an insolation-driven ice model), Commons PD photo of the
Book Cliffs above Helper. Figdata: shelf_model.py (2-D forward model with
spin-up, volume-conserving bisection fill, tract classification with a
centred-difference shoreline move and short-run merge, tract polygons in the
final geometry), lr04_periodogram.py (detrended Hann periodogram of two LR04
windows + a seeded synthetic 30-m core); 10 tests (volume per step, no
deposit above sea level, forced-regression formula within 2 % away from the
shelf-edge jump, tract order L-T-H-F-L-T-H, sign rules, basinward shift,
pure-sine peak, monotonic LR04, MPT windows, core rate). Named number
35.5 km. EXCLUDED: third-order cycle durations (no open source read; the
text speaks only of the hierarchy and its causes); Book Cliffs photo
location as the Kenilworth Member (not stated by the photo page); Exxon
chart history beyond Miller's sentence; eustatic amplitudes of named events
other than the 160 m Oligocene one; the Book 2 rows nasa:milankovitch and
hays76:periods (Laskar periods used instead).

Ch. 17 notes: no dataset (region.py for the unit tops of Varden-2 at
(7500, 7000), footwall, clean column chalk 766 / shale 100 / limestone 180 /
sandstone 120 m, schist at 1166 m). New sources: Keys 1990 USGS TWRI 2-E2
(density-porosity equation, grain densities 2.65/2.71, fluid 1.0-1.1, Table 6
transit times, time-average equation, API unit, relative radioactivity),
Loss and Peters 2010 GSA abstract (wave spectra unimodal, modal wavelengths
75 and 110 m), Commons CC BY-SA photo of hummocky cross-stratification
(Rygel; cropped above the hammer). Figdata: well_logs.py (synthetic GR,
RHOB, DT; eleven fining-upward channel fills; net sand by cutoff); 8 tests
(tops vs region thicknesses, footwall column, channel sum, porosity
inversion, time-average limits, net sand vs closed form, fining upward,
shale hot). Named number 72.2 m. EXCLUDED: dolomite grain density (Keys'
OCR reads 2.37, a misprint or OCR error for a value not checkable here:
dolomite left out); API values of particular lithologies (the logs are
synthetic, the text says only high/low); wave-base depths as numbers (only
the buoy wavelengths and the e^-2pi z/lambda decay); the date of Walther's
statement; Bouma's and Walker's names and dates for the sequence and the
facies-model functions; tidal-bundle periods (told qualitatively).

Ch. 18 notes: no dataset (region.river_z(0) = 170 m is the outlet of an
invented upland river west of the map; the upland basin is 38.7 km2, kept
below the 80 km2 of the Varden river's whole basin in the Year 1 volume, and
its uplift rate is that volume's 43 m/Myr denudation rate). New sources: two
MIT OpenCourseWare 12.163 lecture notes (K. Whipple, 2004, CC BY-NC-SA):
hillslope evolution (scarp erf solution, Kc ranges 1e-3 to 1e-2 and 5e-3
m2/yr, Roering nonlinear form, exponential soil production, max ~0.5 mm/yr)
and bedrock channels (E = K A^m S^n, m/n ~ 0.5, Howard and Kerby
A^0.44 S^0.68, S = ks A^-theta, response time ~1 Myr, Vkp = U for n = 1);
Cook et al. 2020 Nature Communications (l = 0.65, K_G 1e-4, 38 glaciers);
IJC 2018 Niagara page (11 km since ~12,500 yr, ~1 m/yr average, ~0.1 m/yr
now); PREM crust/mantle ratio 0.80 from the shared data:prem table.
Figdata: hillslope.py (erf scarps + FTCS check, steady parabolic hills),
stream_profile.py (steady profile, slope-area samples, exact n = 1
kinematic-wave solution and an upwind check), varden_river.py (chi of trunk
and three tributaries); 11 tests. Named number 900 kyr (899 by the
calculation). Entry file: the index \parskip given 0.5 pt of shrink through
imakeidx's othercode hook (\indexsetup is preamble-only), because the new
index length left an overfull \vbox of 19-23 pt in multicol's final
balancing; \raggedcolumns and more \indexspace shrink did not help.
EXCLUDED: Fernandes and Dietrich 1997 and Heimsath et al. 1997 values (not
open; the lecture notes' ranges used instead); a critical gradient value
(S_c = 1.2 appears only as an exercise value, labelled so); Hack's-law
exponents as facts (the upland's A = 4.5 d^1.7 is invented, not called
Hack's law); Niagara's caprock lithology (the IJC page speaks only of the
rocks of the escarpment and of blocks breaking from the crest); glacial
buzzsaw examples and snowline altitudes; knickpoint celerities from a
primary paper other than the Niagara record.

Ch. 19 notes: data reused read-only from the shared derived tables
(bachelor-1-ncep-uwnd-p.csv, fetched by the Book 3 block; grade-10 WOA23
North Atlantic column, Book 2 block), with Book 5 ledger rows of their own
(data:b5-ncep-uwnd, data:b5-woa23-atlantic). New sources: NASA Glenn
standard-atmosphere model (metric) and specific-heat pages (gamma = 1.4);
Stewart, Introduction to Physical Oceanography, LibreTexts 9.1 (inertial
motion, the 1987 North Pacific drifter loops), 8.5 (stability E, N "a few
cycles per hour", Ri 0.25), 8.3 (Table 8.3.1 eddy viscosities); UNESCO 44
EOS-80 and THETA (check values 1028.1063 and 36.89073 tested). Figdata:
inertial_oscillation.py (RK4 checked against the closed form, friction,
drift, f and its beta-plane tangent), thermal_wind.py (layer dT/dy from
the 850-250 hPa shear of the zonal mean; poleward-drop column), and
buoyancy_frequency.py (standard atmosphere N; ocean N from potential
density); 9 tests. Ownership: Book 3 named the buoyancy frequency and the
gradient wind without indexing them (ch. 26 proof, ch. 28 remark); both
are defined and indexed here, Book 3's results recalled. Named number
31 m/s (31.3 by the calculation). EXCLUDED: a core-flow speed for the
brief's Part I "core" (no open source fetched; the five flows became
bathtub, tank, lake breeze, depression, gyre, invented); the claim that
deep currents follow depth contours (unsourced, cut); real Ekman depths
(only the problem's invented eddy viscosity of the steppe); Taylor's
experiment dates; observed eddy and depression sizes as numbers (the text
compares L_R with the depressions on a weather map without a number).

Ch. 20 notes: data reused read-only from the shared derived tables
bachelor-1-ncep-uwnd-p.csv and bachelor-1-ncep-vwnd-p.csv (new row
data:b5-ncep-vwnd; my streamfunction edges agree with the Year 1 volume's
script to 0.1 deg). New sources: Crossref record of Rossby et al. 1939 (JMR
2(1), 38-55; the EliScholar PDF is behind a Cloudflare challenge, so the
paper's content is taken from the 2020 JMR editor's commentary only, and
the text claims no more than the commentary says); Charney, Fjortoft and
von Neumann 1950 (Tellus, CC BY 4.0, PDF read: four 24-h forecasts at 500
mb on ENIAC, 736 km grid, ~24 h computing time); NASA MODIS image of a low
off Iceland, 4 Sep 2003 (public domain). Figdata: rossby_waves.py
(dispersion, group velocity, stationary n from uniform U and from the
January 300 hPa zonal mean), eady.py (growth curve, mu_max 1.6061, s_max
0.3098, mu_c 2.3994; observed 45 N shear over the NASA-model height of
850-250 hPa), held_hou.py (small-angle construction, equal areas, observed
psi at 500 hPa and Hadley edges); 6 tests. Named number 1.6 days (1.59).
Held-Hou H = 15 km and Delta = 1/6-1/3 are presented as illustrative model
parameters, not facts. EXCLUDED: the brief's observed count of "four to six"
winter waves (no open climatology fetched; the hook says "a few"); Rossby's
own formula and numerical example from the 1939 paper (PDF unreachable);
Eady's 1949 paper and Held and Hou's 1980 paper as citations (results
derived or admitted, no bibliographic claim); Lorenz's APE fraction of the
total potential energy; lee-cyclogenesis frequency (only the PV argument).

### Ch. 21 notes (ocean-dynamics, 2026-10-23)

- PDF 235-247 (printed 224-236), 0/0/0, gates OK, tests 212 pass (5 new in
  `tests/bachelor-3/test_ocean_dynamics.py`).
- Scripts: `wind_driven_gyre.py` (spherical curl, w_E, Sverdrup profiles for the
  invented basin; Stommel and Munk boundary-layer profiles, beta-plane at 35 N),
  `tides.py` (equilibrium tide, two-Kelvin-wave channel amphidromes, marching squares
  from `figdata/shared/region.py`, read-only).
- Sources: Stewart sections 10.4, 11.1, 11.3, 13.3, 17.4, 17.5 (LibreTexts), NASA Moon
  fact sheet; Book 3 rows reused (rapid:transports, stewart:north-atlantic,
  stewart:stommel, stommel:1948, stewart:heat-conveyor, stewart:deep-circulation,
  stewart:ekman-layer, argo:fleet, noaa:argo-25). Photo: NOAA GOMO Argo deployment, PD.
- Book 3's own Stommel gyre figure (numerical, uniform vs beta) is not repeated: this
  chapter shows the analytic boundary-layer profiles instead.
- Named number: 29 Sv (29.4).
- Dataset for ch. 22 added in the Book 5 block of `tools/fetch_data.py`:
  `bachelor-3-ncep-air-sfc` (NCEP R1 air.sig995 LTM 1991-2020, zonal means, via the
  Book 3 block's derive function, called not changed).
- EXCLUDED: "the Gulf Stream carries a hundred times all the world's rivers" (brief's
  hook; no direct source fetched); Gulf Stream speed "more than a metre per second"
  (no row; dropped); deep western boundary currents "along the western margins of the
  other basins" (no row; dropped); "sends its profile by satellite" (not in the Argo
  rows; dropped).

### Ch. 22 notes (climate-models, 2026-10-23)

- PDF 248-259 (printed 237-248), 0/0/0, gates OK, tests 216 pass (4 new in
  `tests/bachelor-3/test_climate_models.py`).
- Scripts: `budyko_sellers.py` (OLR = A + BT fitted, area-weighted, to the NCEP R1
  1991-2020 zonal means: A 211.9, B 1.816, rms 10.4 W/m2; 0-D model with a -10/+10 C
  albedo ramp: equilibria -45.6/7.8/14.4, warm branch lost at S0 1314.6 (3.34 %),
  snowball melts at 2039.4; Budyko's relaxation model with beta = 0.235 kcal/cm2/month/K
  and the NCEP insolation shape, Tc calibrated to the 72 deg ice edge: -12.26 C;
  glaciation threshold 0.97130 at 47.65 deg, a 2.87 % drop). The brief's separate
  `ebm_0d` script is folded into it. The mean albedo uses the exact cumulative
  sunlight (a grid-step version jittered the minimum by 1e-4).
  `two_layer.py` (AR6 emulator means, efficacy 1: tau 4.12 / 262 yr, a_f 0.67,
  ECS 2.95, TCR 1.99, F/(gamma - lambda) 2.02, F/(kappa - lambda) 1.81).
- Dataset: `bachelor-3-ncep-air-sfc` (Book 5 block); Book 3's ulwrf/dswrf derived
  files read.
- Sources: Budyko 1969 (Tellus, open PDF), AR6 WGI ch. 7 (7.5.1.2, 7.5.4, 7.5.5,
  7.5.6, ES), ch. 7 SM (7.SM.2), ch. 1 (1.3.4, 1.5.2.5, 1.5.3, 1.5.3.2, 1.5.4, FAQ 1.1).
  Book 4 rows reused: ipcc:ecs, ar6ch7:tcr, ipcc:erf-2xco2, hoffman17:hysteresis.
- Sign convention follows the Year 2 volume: lambda < 0 (the brief wrote F - lambda T).
- Named number: 2.9 % (2.87), against Budyko's 1.6 % and the 0-D 3.3 %.
- No small-ice-cap instability is claimed: the Budyko-form curve rises monotonically
  from 47.65 to 90 deg with this insolation.
- EXCLUDED: "a thunderstorm, a few kilometres across" (no row; replaced by an
  unnumbered statement); "the assessment kept the members consistent with the assessed
  sensitivities" (the SM says ECS/TCR were NOT formal constraints; text gives the four
  real constraints); "the upper rungs are run a few times" (no row; dropped);
  small-ice-cap instability (no source fetched, and not shown by this model);
  attribution of the diffusive form to Sellers (no source fetched; the model name only,
  via hoffman17:hysteresis).

### Ch. 23 notes (hydrogeology, 2026-10-23)

- PDF 260-270 (printed 249-259), solutions printed 316-319; 0/0/0, gates OK, tests
  221 pass (5 new in `tests/bachelor-3/test_hydrogeology.py`).
- Scripts: `theis.py` (W(u) = exp1; Varden-3 at (4500, 5000) from region.py: ground
  363.15, limestone 282.52-102.52 (b 180), shale 80.6 m; T 450, S 2e-4, Q 2160, r 60 m;
  synthetic record seed 23; Cooper-Jacob fit on u <= 0.05: T 453.3, S 1.91e-4,
  16 points; r0(30 d) 12.3 km; farm at 1 km, 30 d: 1.92 m; interference midpoint
  5.46 m), `flow_net.py` (red-black SOR, mirror Neumann; q/K H = 0.512, in = out),
  `advection_dispersion.py` (Ogata-Banks with erfcx; t16/t50/t84 for alpha 1, 3,
  10 m; R = 3 shifts the curve by exactly R).
- Sources: Heath 1983 (USGS WSP 2220; Darcy, K chart read off at 200 dpi, T, S,
  cone, Theis, Jacob, velocity, water levels), EPA CEAM on-site guide (dispersivity
  rules), USGS TWRI 08-A3 (pressure transducers); nist:water reused for the
  viscosity exercises.
- Named number: T = 450 m2/d (453 from the test).
- Recall checked: g6 owns porosity, permeability, aquifer, groundwater, water table,
  spring; g10 residence time and fossil groundwater; no school or Year 1/2 owner of
  confined aquifer or cone of depression.
- EXCLUDED: "the water is led away so that it cannot soak back into the aquifer" and
  "the recovery is recorded the same way" (pumping-test practice, no row; dropped);
  "a sand aquifer" for the Atlantic coastal plain (the row says the Cretaceous
  aquifer; reworded); the brief's clean-sand upper bound 200 m/d (chart reads
  10^2.2 = 160; printed 150).

### Ch. 24 notes (glaciology, 2026-10-23)

- PDF 271-281 (printed 260-270), solutions printed 329-331; 0/0/0, gates OK, tests
  227 pass (6 new in `tests/bachelor-3/test_glaciology.py`), ledger OK (2202 rows).
- Scripts: `ice_flow.py` (Paterson-Budd rate factor via PISM's constants: A(-10 C)
  1.40e-17, A(0 C) 1.43e-16 Pa^-3 yr^-1; slab velocity and flux; Nye profile fitted
  to the ETOPO1 Greenland transect at 72.5 N, h > 1000 m: tau0 72.5 kPa west, 108.3 kPa
  east; Arkel cap R 20 km, tau0 100 kPa: hmax 667 m, 447 km3, 410 Gt, 1.14 mm SLE),
  `sea_ice.py` (NSIDC G02135 v4 March/September 1979-2026: trends -0.384 and
  -0.741 Mkm2/dec, -2.49 and -11.56 %/dec of 1981-2010; Stefan 1.51 m at 100 d,
  2.14 m at 200 d, 0.68/1.18 m under 20 cm of snow).
- New fetch_data keys: `bachelor-3-etopo-greenland` (ERDDAP etopo180 transect),
  `bachelor-3-nsidc-mar-extent`, `bachelor-3-nsidc-sep-extent`.
- Sources: PISM rheology docs (Paterson-Budd constants, Glen n), CICE constants (k_i,
  k_s, latent heats), AR6 WGI ch. 9 (ice-sheet and glacier losses, sea ice, permafrost,
  MISI, projections, FAQ 9.1, Table 9.5); reused nsidc:*, firn:close-off, iapws, noaa,
  codata, gps:high-end, data:b5-imbie. Ledger source keys B5-IPCC-AR6-CH9 and
  B5-NSIDC-SII duplicate other books' keys because the source table is per file.
- Photo: NASA / Jim Yungel, IceBridge 15 Apr 2014, PD (aircraft wing cropped).
- Named number: 1.1 mm (Arkel ice cap sea-level equivalent).
- Recall checked: g8 owns glacier, ice sheet, permafrost; Book 4 owns the sea-level
  budget; the ice-albedo feedback is the Year 2 volume's.
- EXCLUDED: Schoof's flux-thickness exponent (no source fetched; the MISI argument
  uses the slab theorem's H^{n+2}); a linear extrapolation of the September extent to
  1 Mkm2 (dropped, AR6's assessed statement kept instead); ice-stream speeds (no
  number printed); "ice moves metres a year in the interior" (dropped); a shallow-core
  sentence (dropped); Larsen B speed-up kept as "up to eight times" (ar6ch9 row), not
  "eightfold".

### Ch. 25 notes (remote sensing and GIS, 2026-10-23)

- PDF 282-295 (printed 271-284, 14 pp, over the 12.5 target), solutions printed
  343-346; 0/0/0, gates OK, tests 233 pass (6 new in
  `tests/bachelor-3/test_remote_sensing.py`), ledger OK (2272 rows), landing 0.
- Scripts: `spectral_signatures.py` (five ECOSTRESS spectra; OLI band means; NDVI
  grass 0.815, water -0.006, sand 0.152; band-10 emissivity 0.983 / 0.991 / 0.966;
  kaolinite minimum 2.20 um), `thermal_ir.py` (Planck, inversion, grey body, mixed
  pixel 370 K in 290 K; Wien 9.66 um at 300 K, 2.01 um for lava),
  `insar_mogi.py` (Sentinel-1 C band, half wavelength 27.73 mm; z0 4 km, dV 1e7 m3:
  uz0 149.2 mm, LOS0 122.2 mm, 4.41 fringes), `varden_gis.py` (region.py read only:
  slope max 23.0 deg, selected 0.32 km2, steep shale 0.38 km2).
- New fetch_data keys: `bachelor-3-eco-{grass,water,soil,kaolinite,hematite}`.
- Photo: the Three Sisters interferogram, USGS (Wicks et al. 2002), PD.
- Problem volcano renamed Mount Halvren (Ossa is a real mountain). Named number
  15 million m3.
- Deviation from the brief: its overlay (limestone within 200 m of the river) is
  empty on region.py; the chapter uses shale within a 1 km buffer and slope > 15 deg
  (said in the chapter's provenance comment).
- Recall checked: g9 owns remote sensing and satellite image; Book 3 owns the
  digital elevation model and points to the first interferogram (Landers 1992).
- EXCLUDED: USGS splib07 spectra (ScienceBase fetch blocked, 403; the approved
  ECOSTRESS fallback used); "hundreds of bands" for hyperspectral sensors (no number
  printed); the Al-OH attribution of the 2.2 um dip and a band 6/7 clay ratio (no
  row, and the ratio is contradicted by the grass spectrum: dropped); the duration of
  a satellite pass over a ground station (not stated by ESA; dropped); "bull's eye
  west of the volcanoes" for the Three Sisters (not in the source; dropped).

### Ch. 26 notes (planetary interiors and surfaces, 2026-10-23)

- Printed 285-295 (11 pp, on target), solutions printed 356-358; 0/0/0, gates OK,
  tests 238 pass (5 new in `tests/bachelor-3/test_planetary_surfaces.py`), ledger OK
  (2309 rows), landing 0.
- Scripts: `two_layer_planet.py` (Earth x 0.546, rho_c 12,500; Mars 0.540, 6460;
  Moon 0.190, 10,900; Mercury 0.820, 7120; Mars with a 3500 mantle: 1624 km, 7447),
  `crater_sfd.py` (Ivanov 2001 PF and Hartmann-Neukum 2001 CF from Craterstats; plain
  A 80,000 km2 at 1.5 Ga and plain B 120,000 km2 at 3.6 Ga resurfaced below 2 km at
  1.0 Ga, Poisson draws with seed 26: A 54 craters >= 1 km, 1.38 +- 0.19 Ga; B 56
  craters >= 2 km, 3.54 +- 0.04 Ga; resurfacing 1.12 +- 0.15 Ga).
- Photos: Barringer Crater (USGS/D. Roddy, PD), Olympus Mons (NASA/JPL/USGS PIA00300,
  PD). Book 3 already printed Io, Europa and Venus: not repeated.
- Named number: 1.4 billion years (model age of plain A).
- The Year 1 volume already prints the two-layer proposition: recalled, not repeated;
  the chapter adds the family of solutions and its ill-conditioning for the Moon.
- EXCLUDED: Mars k2 0.169 (Konopliv, no open copy; Yoder 2003's 0.153 used); the
  InSight core density 5.7-6.3 g/cm3 (abstract not fetched); the InSight landing year
  (not on the fetched page); the claim that the Moon's core came from re-analysed
  Apollo seismograms (NASA's page does not say how; reworded); Io's heat flow from
  Veeder 2012 / Davies 2024 (no open page with the number; Veeder 1994's '> 2.5 W/m2'
  used); Io k2/Q from Lainey 2009 (abstract has no number; computed instead from the
  heat flow); Mercury core '85 percent of the volume' (AGU release, inconsistent with
  its own 4000 km diameter); Venus crater count; pi-group scaling exponents (laws
  admitted without numbers); the 'D = 20 d' rule kept as the handbook's convention.

### Ch. 27 notes (planetary atmospheres and habitability, 2026-10-23)

- Printed 296-308 (about 12.5 pp), solutions printed 370-372; 0/0/0, gates OK, tests
  245 pass (7 new in `tests/bachelor-3/test_planetary_atmospheres.py`), ledger OK, landing 0.
- Scripts: `jeans_escape.py` (lambda at the exobases; Gronoff Table 2 reproduced at the
  planetary radius in a test; the Jeans flux checked against a numerical integration of
  the Maxwellian), `runaway_greenhouse.py` (ILLUSTRATIVE grey model: saturated N2-H2O
  pseudo-adiabat, IAPWS saturation curves, L from Clausius-Clapeyron, kappa = 0.24
  (p/1 bar)^1/2 m2/kg chosen so that the plateau lands on Kopparapu's 291 W/m2; a
  pressure-independent kappa gave an unphysical OLR maximum above the plateau, so the
  broadening was introduced), `habitability.py` (Kopparapu Table 3 fits, IAPWS and NIST
  phase curves).
- Deviation from the brief: the [F] `planet_atmospheres` T(z) profiles were replaced by a
  phase diagram of water and methane with the surface states of the four bodies (no open
  profile data for Venus, Mars and Titan were fetched; the phase diagram carries the
  habitability argument with ledger values only), and an extra [F] habitable-zone figure
  (Teff against flux) was added. No Venus photograph (Book 3 already printed one).
- Photos: Mars valley network (ESA/DLR/FU Berlin, CC BY-SA 3.0 IGO), Ligeia Mare
  (NASA/JPL/USGS, PD). A Curiosity view of the Peace Vallis fan (PIA16052) was rejected
  (too hazy to show the valley); MOC Warrego Valles rejected (its own caption says the
  valleys are not resolved as a network at that scale).
- Kepos (invented): 5.2e24 kg, 6200 km, exobase 500 km / 1400 K / n_H 2e11 m-3,
  homopause 200 K CO2, f = 1e-3, star 0.30 L_sun, 4800 K, a = 0.60 au. Named number:
  11 billion years (diffusion-limited loss of an Earth ocean); cross-checked against
  Kopparapu's footnote (f = 3e-3 gives about the age of the Earth: 3.2 Gyr for the Earth
  in exercise 11, 3.7 Gyr for Kepos in question 24).
- EXCLUDED: Mars obliquity from Laskar (2004) directly (no open copy fetched; the range
  0-66 deg and mean 35 deg are quoted through Gilli et al. 2025); the Pioneer Venus date
  (1978) and Venus's water layer of 'a hundredth of a millimetre' (first draft; the
  ledger's 6e15 kg gives about 1.3 cm, now printed as 'about a centimetre'); Ligeia Mare's
  area (from PIA09184, not the image printed); the homopause altitude of the Earth; Titan's
  methane photochemical lifetime; Huygens surface values (NASA's -179 degC and 60 % used);
  the T(z) profiles of Venus, Mars and Titan; the H2-N2 binary diffusion coefficient
  (Kepos given a CO2 homopause to use Zahnle's b for H2-CO2).

### Ch. 28 notes (exoplanets, 2026-10-23)

- Printed 309-321 (about 13 pp), solutions printed 385-387; 0/0/0, gates OK, tests 252
  pass (7 new in `tests/bachelor-3/test_exoplanets.py`), ledger OK, landing 0.
- New datasets in the Book 5 block of `tools/fetch_data.py`: `bachelor-3-pscomp` (NASA
  Exoplanet Archive pscomppars by TAP, 6451 planets on 2026-10-23, 16 columns, derived
  CSV 0.6 MB with trailing zeros dropped) and `bachelor-3-zeng-{iron,earthlike,water50,
  h2-2pc}` (Zeng et al. model tables). Acknowledgement text printed in the methods
  caption and the credits.
- Scripts: `rv_transit.py` (Keplerian RV with a Newton Kepler solver; quadratic
  limb-darkened transit by numerical radial integration, checked against the closed-form
  overlap area; point-lens magnification and Einstein angle), `exoplanet_archive.py`
  (selections, histogram, mass-distance by method, model curves, Solar System).
- Deviations from the brief: an extra [F] figure, mass against semi-major axis by
  discovery method (the brief's 'which planets each method finds' as data); the
  microlensing [S] became a two-object figure with a magnification plot; the photo is the
  JWST image of HIP 65426 b (CC BY 4.0) rather than HR 8799 (HR 8799 kept in the text from
  Marois et al.); no transmission-geometry schematic (the proposition's proof suffices).
- Selene's Lamp (invented): 0.80 M_sun, 0.76 R_sun, 5000 K; planet P 12.0 d, K 2.59 m/s,
  depth 838 ppm, T14 3.23 h (designed from m = 8.0 M_E, R = 2.40 R_E, b = 0.40). Named
  number: 3.2 g/cm3; it lies above the radius valley and 1.38 times the Earth-like rocky
  radius at its mass (Zeng table), so a sub-Neptune.
- EXCLUDED: stellar RV jitter amplitudes (kept qualitative, from the Nobel background's
  pulsations-and-spots sentence); the Kepler mission's star count (Petigura's 42,000
  searched stars used instead); the measured TRAPPIST-1 b eclipse depth and day-side
  temperature (only the abstract was fetched; exercise 9 computes depths for given
  temperatures); HR 8799 and HIP 65426 distances; occurrence-rate boundaries for
  super-Earth/sub-Neptune beyond Fulton's regimes; the 'first planet-hunting space
  telescope' phrase (CoRoT preceded Kepler, Nobel background); journal volumes/pages for
  Fulton, Wright, Petigura and the JWST CO2 paper (not on the fetched abstract pages, left
  out of the ledger).

### Ch. 29 notes (milky-way-galaxies, 2026-10-23)

- Printed 322-337 (16 pp), solutions printed 402-404; 0/0/0, gates OK, tests 262 pass
  (10 new: `test_rotation_curve.py`, `test_distance_ladder.py`), ledger OK, landing 0.
- New dataset in the Book 5 block: `bachelor-3-ogle-lmc-cep` (CDS J/AcA/65/297
  lmccep.dat.gz, gzipped fixed-width read by the ReadMe byte ranges; 4429 stars with both
  magnitudes, 2315 F-mode). The Eilers et al. 2019 Table 1 is not on VizieR (the J/ApJ/871/120
  ReadMe 404s): its 38 rows are copied into `rotation_curve.py` with ledger row
  eilers19:table1.
- Scripts: `rotation_curve.py` (Plummer + two Miyamoto-Nagai discs of Pouliasis Model I,
  NFW fitted by weighted least squares in log parameters: rho0 1.056e7, Rs 14.75 against
  the paper's 1.06e7 and 14.8; halo dominates beyond 14.3 kpc, paper 'about 14');
  `distance_ladder.py` (W_I fit with iterative 3-sigma clipping reproduces Soszynski's
  Table 2 to 0.001; rung ranges computed from ledger values).
- Deviations: '21-cm line' is owned by the physics books (indexed in physics b3 ch. 12),
  so it is recalled, not defined; the Oort constants share the rotation-curve definition
  (label `def:...:rotation-curve`, no separate `:oort` label); 26 terms defined. The
  ladder diagram is an [F] from the script (not an [S]); one figure combines the
  rotation-curve data and model components, a second the enclosed mass. No density-wave
  figure (told, as the brief says).
- Problem: Part I invented survey (A 15.3, B -12.7, V0 229.2); Part II tangent-point
  velocities generated from the fitted model at l 40-70 deg; Parts III-IV with the
  measured 200 km/s at 20 kpc (Eilers 199.84 at 20.27): named number 55 % (54.98 %; the
  smooth model would give 59 %, explained in the solution).
- EXCLUDED: a light-year conversion (no ledger row; kpc used throughout); 'billions of
  solar masses' for supermassive black holes (only Sgr A* sourced; definition says 'a
  million or more'); the number of galaxies in a cluster (Kravtsov and Borgani give
  masses, not counts); the S2 semi-major axis (computed in exercise 12 from the mass and
  period instead); the Event Horizon Telescope image; OpenStax Astronomy as a source (its
  page forbids ingestion by AI systems: Buta 2011 and Dobbs and Baba 2014 used instead);
  M31's distance method (McConnachie's compilation does not say it in the fetched text, so
  the ladder caption no longer calls M31 a Cepheid/TRGB anchor); journal volumes of Reid
  2020, McConnachie 2012, Freedman 2019 and Riess 2022 (not on the fetched pages).

### Ch. 30 notes (origin-of-elements, 2026-10-23)

- Printed 338-351 (14 pp), solutions printed 419-422; 0/0/0, gates OK, tests 274 pass
  (12 new: `test_origin_of_elements.py`), ledger OK (2413 rows), landing 0.
- Four new datasets in the Book 5 block: `bachelor-3-asplund21` (arXiv e-print tar of
  2105.01661, sun_abund2.tex: 83 elements and 287 isotopes; Z taken from the symbol because
  six rows of Table B.1 print a Z shifted by one, and a row with an empty first cell, 238U,
  is kept), `bachelor-3-kadonis-macs` (KADoNiS v0.3 MACS at 30 keV, 357 nuclides, from
  exp-astro.de: kadonis.org is now a parked domain), `bachelor-3-gcs` (Casagrande et al.
  2011, CDS J/A+A/530/A138, 6670 irfm stars), `bachelor-3-iaea-gs` (IAEA LiveChart ground
  states, 1940 nuclides with Z <= 92, stable or t >= 1 s). Beyond the Sync 3 list:
  KADoNiS, GCS and IAEA (flag in Phase D).
- Scripts: `solar_abundances.py` (photosphere minus CI 0.000 +- 0.007 over 58 elements,
  as published), `neutron_capture.py` (s path with IAEA half-lives: capture where the
  nucleus is in nature or lives more than 1000 yr, and the 21 branch points of
  Kaeppeler's Table III; 30 s-only, 29 r-only, 36 p (35 + 176Hf, whose s feeding through
  the 176Lu isomer is not modelled); classical model fitted to 22 s-only nuclei A > 90:
  tau0 0.306/mb, G 0.054 %, rms 0.064 dex), `chemical_evolution.py` (closed box with mu
  0.291 from McKee 2015: 16.4 % of stars below [Fe/H] -1 against 0.39 % (all) and 2.9 %
  (<= 1 Msun) observed; two-phase [alpha/Fe] model, Ia share 0.602 at the Sun).
- Deviations: the Book 4 chapter on the elements in the Earth already draws BSE/CI
  against T_c, so ch. 30 recalls it with Lodders/McDonough values and draws the Sun
  against CI instead; the volatility trend is defined here. G-dwarf problem has its own
  label (`:g-dwarf`). "Gold" in the brief's hook became platinum, which the r-process
  peak row names (Au 197 is s+r in the classification). History box names Merrill 1952
  and Burbidge, Burbidge, Fowler, Hoyle and Cameron 1957 (both in the Kaeppeler row).
- Problem "A closed-box galaxy": Part I solar mixture, Part II tellurium sigma N
  (predicted 123Te within 0.3 %), Part III closed box with McKee's surface densities,
  Part IV metallicity distribution against the GCS: named number 16 % (16.38 %).
- Entry file: the index \parskip shrink raised from 0.5 to 1 pt (minus): the new
  index length gave a 6.5 pt overfull \vbox in multicol's final balancing.
- EXCLUDED: "within a few million years" for core-collapse supernovae (Matteucci says
  only "short-lived"); "lithium burnt at the base of the convective envelope" (not in
  Asplund's text); laboratory analysis "to a fraction of a per cent for every element";
  "the billions of years these stars had lived" (S stars' ages not in the source);
  potassium as a product of massive stars; the gold-as-r-process claim; the Sr detection in
  the kilonova spectrum (in Cowan, not needed); "dredge-up" kept only with the row's
  third-dredge-up text; AGB masses limited to Kaeppeler's "M <= 3 Msun".

### Ch. 31 notes (field-lab-methods-3, 2026-10-23)

- The Varden survey: gravity over the granite (`gravity_granite.py`, 5533 right prisms
  with closed-form attraction, granite 2620 and schist 2750 kg/m3, contrast -130, floor
  at -1500 m elevation, an exercise assumption stated in the text; closed low -2.29 mGal),
  the magnetic line over the buried dolerite dyke (`magnetic_dyke.py`, four charged faces,
  base-station drift), the VES on the valley floor (`resistivity_sounding.py`, granite
  20000 ohm m, not 5000, so that the s/S branch is clean), the GPR profile
  (`gpr_radargram.py`). 13 tests in `test_field_methods.py`.
- The dyke is Book 5's own: buried, confined to the basement below the unconformity,
  only in `figdata/bachelor-3/`; `region.py` untouched, `contact_elevation` guarded.
- Problem "Reducing the Varden survey": named number, the depth to the top of the
  dyke, **220 m** (half-width 221 m; unconformity at 222 m).
- Ledger: gpg rows 556--574 (19 rows, GPG/UBC-GIF pages).
- EXCLUDED: "the survey stopped when ..." (no source); Archie's law "for reservoir
  rocks" as the source's scope (not in the page); the water table as a seismic refractor
  claim (not in GPG); the Hammer chart's rings and sectors in detail (GPG gives only
  "a Hammer chart and tables"); the GPR probing depth in dry sand as a number.

## Phase C (2026-10-23)

- **Linker.** `--unwrap --apply`, then `--apply`: 1191 links across 57 files (def 1125,
  thm 54, prop 12), 216 distinct targets; the idempotence dry run inserts 0. Curation in
  `tools/term_config/book5_en.py`: STOP {pole, poles, line of sight, steady state, eddy,
  model age, model ages} (geographic poles were linked to the stereonet pole; "line of
  sight" in ch. 28--29 to InSAR; "steady state" of climate, aquifers, the s process and
  glaciers to one definition; "eddy" to eddy viscosity; crater "model ages" to the
  isotopic model age); EXTRA_PROTECT soil production rate(s) (was linked to the
  cosmogenic production rate).
- **Scripted solutions re-read** (every solution recomputed with `calc/chNN.py`, every
  printed number compared). Clean: ch. 1--15, 17, 18, 21, 27, 28, 30, 31. Slips fixed:
  ch. 16 A24 endpoints (17.37/52.84 km, giving the printed 35.5 km shift); ch. 19 ex. 9
  L_R 1207 -> 1206 km; ch. 20 Eady lengths 4550 -> 4540 and 4170 -> 4160 km (mu 1.61
  as printed), latitude circle 20020 -> 20015 km; ch. 22 the albedo-ramp sign (0.54 +
  0.016 T), B 1.82 -> 1.816 throughout, -45.6 -> -45.5, Q 328.6 -> 328.7; ch. 23 A8 t0
  0.97 -> 0.98 min; ch. 24 ex. 5 61 -> 60 m/yr; ch. 25 A19 13.5 -> 13.6 km3, A10 149.8
  -> 149.7; ch. 26 Mars k2 0.108 -> 0.109; ch. 29 bulge mass 1.072e10 -> 1.067e10 (text
  and solutions; figdata 460 x 2.32e7). Typesetting: ch. 27 ex. 14 and ch. 31 ex. 1
  overfull lines (display, split into parts); ch. 31 a booktabs rule (booktabs is not
  loaded). The common cause: a constant printed rounded and then reused unrounded (or the
  reverse) two steps later.
- **FIGCHECK full pass**: all 209 objects (183 omfigures, 26 photographs and AI images)
  on their own pages of the final build; 19 fixed (14 layout, 5 science, listed in
  `FIGCHECK.md`, section "Phase C full pass"). Science fixes: isotherm labels on the wrong
  lines (ch. 5), glacier flow lines outside the ice (ch. 24), mobile-lid slab sinking from
  mid-plate (ch. 26), the distance-ladder caption (ch. 29), the closed box making stars
  richer than its gas (ch. 30, `chemical_evolution.py` + test). A pgfplots trap: a colour
  bar inherits `axis equal image` from a groupplot and renders zero-width -- give the
  colour bar `axis equal=false`.
- **AI**: `ai_stubs.py --book 5 --list` empty; no PNG in `images/book5/ai/`.
- **Index**: the multicol balancing gave an overfull \vbox again at the final length;
  the entry file's `\imki@othercode` parskip shrink is now `minus 2pt`.
