# PROGRESS --- Book 3

Book 3 = University Year 1, `bachelor-1`, prefix `b1`, entry file
`one_earth_and_space_sciences_book_3_university_year_1.tex`. Binding run file:
`sources/BATCH_BOOKS_1-5.md`. Plan: `sources/book3/BRIEFS.md` (one brief per
chapter). Vocabulary: `sources/book3/DEFINITIONS.md`. Figure checks:
`sources/book3/FIGCHECK.md`. Ledger: `sources/ledger/book3.md`.

## State (2026-10-23)

- Phase A done; Syncs 1-3 received (rulings in `sources/BATCH_BOOKS_1-5.md`).
  **Phase B DONE 2026-10-23 (all 29 chapters written, table below). Phase C
  DONE 2026-10-23** (see "## Phase C" below). NEXT: Phase D report only. Units `\sverdrup`, `\gal`, `\mag` exist in the
  style file: never declare units locally.
- Helper scripts (scratch, re-creatable): `tools/commons.py` (Commons
  metadata + download, UA without e-mail), `tools/shrink.sh` (JPEG at 1400 px),
  `tools/ledger.py` (append sources/rows), `tools/render.sh`, `tools/where.sh`,
  `tools/prog.py`; per-chapter calculators in `calc/chNN.py`.
- **SYNC 2 SOURCING RULING (2026-10-23, binding; read "Sync 2" in the batch
  file):** Wikipedia/Wikibooks is NOT a source. Mint no `WIKI*` key, no
  wikipedia.org/wikibooks.org URL, no `wiki:` row id. EVERY existing wiki row
  must be re-keyed to a fetched primary/agency/open-textbook source (or the
  number removed from the text and listed EXCLUDED in the Phase D report)
  before Phase C ends; the landing check greps the ledger for "wiki" (case-
  insensitive: row ids `wiki:...` must be RENAMED too, and the `% ledger:`
  comments in the chapters updated). `data/derived/bachelor-1-hotspots.csv`
  (pinned Wikipedia table) must be rebuilt from Morgan & Morgan 2007 or
  another primary compilation, tests green (Book 4 reads it). Hypsometric
  curve marked re-founded (done). Progress of the re-sourcing: see
  "## Re-sourcing (Sync 2)" below. Landing check (refined by the
  coordinator): `grep -iE 'wikipedia|wikibooks|\| *WIKI|wiki:'
  sources/ledger/book3.md | grep -viE 'commons\.wikimedia|wikimedia commons'
  | wc -l` must be 0: **0 since ch. 19's re-sourcing (2026-10-23)**; keep it 0 in ch. 21-29 (no wiki source at all). Hotspots CSV: DONE in ch. 15.
- Coordinator notice (2026-10-23): `figdata/shared/region.py`
  `contact_elevation()` now returns nan in the gap the normal fault cuts out of
  a contact (no iteration); our varden tables are byte-identical and their
  tests pass; any NEW code calling it must handle nan.
- Coordinator note (2026-10-23, from Book 1): ch. 4 fault clipped (done, see
  FIGCHECK b1.04); `\cref` never on a figure; round once from raw values;
  scan capitalised `\omterm` inside proper names before Phase C ends; keep
  DEFINITIONS.md accurate (Book 4 reads it).
- Entry file builds 0/0/0 (all 29 chapters; ch. 29 printed pp. 344--357,
  PDF page = printed + 13; solutions printed pp. 359--434; 452 PDF pages; build61),
  gates/calibration/numbering/ledger (1881 rows incl. shared) green, 229 Book 3
  tests pass, wiki grep 0, checked 2026-10-23 after ch. 29. NEXT: Phase C.
  (the repo-wide `test_repo_ledger_is_clean` fails only on other books' files:
  earlier Book 2's `parts/grade-11/04-plate-motions.tex:125` id `earth:R`, now
  Book 1's `parts/grade-7/05-geological-time.tex:455` `ics:base.*`; not ours). Datasets added by Book 3:
  `bachelor-1-cie1931`, `bachelor-1-cie-d65`, `bachelor-1-usgs-kuril`, `bachelor-1-hotspots`, `bachelor-1-grav-kuril`/`-topo-kuril`, `bachelor-1-sealevel-stack` (ch. 23, NOAA NCEI, 51.5 KB), `bachelor-1-intcal20` (ch. 25, IntCal20 from the rintcal GitHub repo pinned to commit e2e3db19, intcal.org unreachable from here; 9501 rows), `bachelor-1-woa23-{sa10,sa30}-{t,s}` (ch. 26, WOA23 annual columns at 10.5S and 30.5S, 25.5W, same template and derive as Book 2's), `bachelor-1-ncep-{dswrf-toa,uswrf-toa,ulwrf-toa,lhtfl,shtfl,prate}` (ch. 27, NCEP R1 LTM 1991-2020 Gaussian grid, zonal annual + `-monthly`, ledger data:b3-ncep), `bachelor-1-ncep-{uwnd-p,vwnd-p,uwnd-sfc,slp}` (ch. 28, NCEP R1 LTM 2.5-deg grid, zonal monthly, ledger data:b3-ncep-circ) (the `# Book 3:` block of
  `tools/fetch_data.py`; report in Phase D).

| ch | slug | status | pages | notes |
|---|---|---|---|---|
| 1 | spherical-astronomy | written 2026-10-22 | ~12 + 3 sol. | 12 exos 4/5/3 + 24-q problem (named: longest night 13 h 32 min); 6 figures + 1 photo + 1 AI; figdata _solar, sun_paths, day_length, celestial_sphere, spherical_triangle; 8 tests |
| 2 | observing-the-sky | written 2026-10-22 | ~12 + 2.5 sol. | 12 exos 4/5/3 + 24-q problem (named: Sirius ~23 L_sun in V); 7 figures (2 figdata, 3 TikZ schematics, 1 photo, 1 AI); figdata blackbody_bands, extinction_line; 5 tests |
| 3 | comparative-planetology | written 2026-10-22 | ~9 + 2.5 sol. | 12 exos 4/5/3 + 24-q problem (named: Mars core radius ~1660 km from the two-layer model); 6 figures (2 figdata, 1 TikZ, 3 photo panels, 5 PD photos); figdata planet_table (parses shared ledger); 3 tests; equilibrium temperature and Bond albedo re-founded from Book 2 g10 |
| 4 | geological-maps | pilot (main session), approved; Phase B fixes done 2026-10-22 | ~11 + 3 sol. | blank p. 20 fixed (table+map side by side after Part I); trend/plunge glossed in def:fold and Q17; hanging wall glossed in solution Q20 |
| 5 | cross-sections | written 2026-10-22 | ~10 + 2.5 sol. | 12 exos 4/5/3 + 23-q problem (named: ~1694 m of limestone bored by the tunnel); 6 figures (2 figdata, 4 TikZ) + 1 photo + 1 AI; figdata varden_sections (fault blocks contoured separately); 7 tests; unconformity re-founded from Book 1 g7; index overfull (21.8 pt, index exactly one page) is transient, entry file not mine |
| 6 | field-lab-methods-1 | written 2026-10-22 | ~9 + 2 sol. | 12 exos 4/5/3 + 24-q problem (named: mean attitude of the east limb 081/12); 5 figures (1 figdata, 2 TikZ, 1 photo) + 2 AI; figdata attitude_stats (seed 83); 4 tests; WMM-2025 declinations from the NOAA calculator (dated 2026); a branded Leica microscope photo was rejected (logo) |
| 7 | rock-forming-minerals | written 2026-10-22 | ~8 + 2.5 sol. | 12 exos 4/5/3 + 24-q problem (named: forsterite content Fo82); 4 figures (1 figdata, 2 TikZ, 1 photo panel) + 1 photo + 1 table; figdata solid_solution (invented olivine analysis OLIVINE_WT); 4 tests; Goldschmidt 15/30 % rule sourced (course notes); recalculation charge check is automatic (site totals are the test); no AI image |
| 8 | optical-mineralogy | written 2026-10-22 | ~11 + 2.5 sol. | 12 exos 4/5/3 + 25-q problem (named: real section thickness 38 um); 4 figures (2 figdata, 1 TikZ, 1 photo pair) + 1 portrait + 1 AI + 1 table; figdata michel_levy (CIE 1931 CMF + D65 via fetch_data '# Book 3:' block, sRGB from CSS Color 4); 6 tests; problem mineral B changed to diopside (forsterite + quartz incompatible) |
| 9 | layered-earth | written 2026-10-22 | ~12 + 2 sol. | PREM functionals (mass, I, g, P), Adams-Williamson, refraction theorem; 2 portraits, 1 AI; problem ends 32.5 %; 8 tests |
| 10 | heat-budget | written 2026-10-22 | ~12 + 2.3 sol. | 12 exos 4/5/3 + 24-q problem (named: Moho beneath pluton E 642 degC); 4 figures (2 figdata geotherms.py, 2 TikZ) + 1 AI; Perry history box; 9 tests; ledger dd10/katsura/england/roy/vila |
| 11 | isostasy-gravity | written 2026-10-22 | ~12 + 2.2 sol. | 12 exos 4/5/3 + 24-q problem (named: net lowering 182 m per km eroded); 4 figures (2 figdata hypsometry.py + gravity_profiles.py, 2 TikZ) + 1 AI + 1 photo (Vening Meinesz); 9 tests; ledger pratt:himalaya (Pratt 1855 scan), wiki isostasy/gravity/geoid/GOCE/PGR rows |
| 12 | plate-kinematics | written 2026-10-22 | ~13 + 2.5 sol. | 12 exos 4/5/3 + 25-q problem (named: full spreading rate across Iceland 19 mm/yr); 5 figures (3 figdata euler_velocities.py, south_atlantic_fit.py, gpts_stripes.py; 2 TikZ) + 1 photo (GNSS station); 16 tests; ledger MORVEL 2010 (Tables 1, 6; outward displacement; Azores; Nubia-Eurasia), NGL MIDAS IGS20 (REYK, STAS, HOFN), Heine 2013 (SAm-SAf rotations, read lat/lon), GTS2020 via Wikipedia, plate-tectonics history, triple junction, Iceland GIA, ATJ; Part II profile invented, corrected with the real 5.0 km Reykjanes outward displacement |
| 13 | rifts-ridges-margins | written 2026-10-22 | ~13 + 3.3 sol. | 12 exos 4/5/3 + 25-q problem (named: 80-Myr floor of the new ocean at 5.6 km); 5 figures (1 figdata depth_age.py vs Book 2's grade-11-seafloor-age.csv + ETOPO1, 2 TikZ margin/transform, 2 photos Thingvellir + NOAA pillows); 6 tests; depth-age theorem with erfc lemma, dyke-splitting and transform propositions; ledger MORVEL (AR-NB, SM-NB, range), Wikipedia raw pages (depth-age, MOR, oceanic crust, Afar, EAR, Red Sea, passive margin, half-graben, fracture zone, transform, Gakkel, EPR, OCC, Atlantis Massif, COB); fast/slow ridge + crust-column figure skipped (Book 2 g11 has both); no AI image |
| 14 | active-margins | written 2026-10-22 | ~12 + 2.6 sol. | 12 exos 4/5/3 + 24-q problem (named: Kuril arc-trench gap predicted by the slab line for 105 km, 162 km; re-sourced under Sync 2); 6 figures (2 figdata slab_seismicity.py on the new bachelor-1-usgs-kuril ComCat set + GVP + PB2002 + Book 2 seafloor age; 3 TikZ section/profiles/bent shell; 1 photo Sarychev ISS NASA PD); 5 tests; LSQ method with derivation, arc-trench gap prop, bent-shell prop (Kuril 21.9 vs 22.45), slab excess-weight prop from the depth-age theorem (8.8e13 N/m), Bouguer trench, slab thermal time scale; ledger +22 sources/31 rows (wiki trench/arc/back-arc/Tohoku/Kuril/Okhotsk/Sarychev/slab pull, Hyndman 2005 GSA Today); inthefield tsunami-warning box carries the AI image b1-tsunami-centre (added 2026-10-23 after the Codex limit cleared) |
| 15 | hotspots | written 2026-10-23 | 12 + 2.5 sol. | 12 exos 4/5/3 + 24-q problem 'The Pacific plate's speedometer' (named: speed of the Pacific plate over Hawaii predicted by the Hawaii+Louisville two-track pole and Louisville's rate, 8.5 cm/yr); 6 figures (3 figdata hotspots.py on the new bachelor-1-hotspots set = Morgan & Morgan 2007 via pinned Wikipedia revision 1381042014: world map with arrows + fitted Pacific pole, rates vs R sin Delta, Hawaiian swell from ETOPO1; 1 TikZ plume head/tail two panels; 2 photos Puu Oo USGS PD, Deccan Matheran CC BY-SA 2.5); 8 tests; defs hotspot (re-founded g7), mantle plume, hotspot track + age progression (re-founded g11), LIP; prop pole from two tracks (cross product + sign rule), method pole+rate fit (grid search, omega LSQ through origin), props buoyancy flux B=(rho_m-rho_w)Av and Q=c_p B/alpha; history box Wilson/Morgan; ledger +17 sources/27 rows (hotspot, plume, Hawaii, LIP table, Deccan, Siberian, CAMP, Ontong Java, Yellowstone/McDermitt/Island Park calderas, heat capacity, two Commons) |
| 16 | stress-strain-rheology | written 2026-10-23 | 13 + 2.6 sol. | 12 exos 4/5/3 + 24-q problem 'Will the fault slip?' (named: pore-pressure rise to slip a 60-deg normal fault at 5 km, 11.0 MPa); 5 figures (1 figdata strength_envelope.py two panels continent 55 mW/m2 wet quartzite + dry olivine / ocean 60 Myr, on geotherms.py; 3 TikZ prism, Mohr+Coulomb, pure/simple shear exact cm maps; 1 photo CSIRO triaxial cell CC BY 3.0 in an inthelab box); 7 tests; defs normal stress, principal/differential stress, lithostatic/pore/effective, extension/stretch/shear strain, strain ellipse, pure/simple shear, rheology/brittle/ductile, Coulomb/cohesion/internal friction, strength envelope/BDT/seismogenic layer; transformation prop (prism proof), principal-stress thm, Mohr prop, strain-ellipse and simple-shear props, failure-angle thm, Byerlee + creep admitted, brittle-gradient prop, slip-test method; ledger +12 sources/12 rows (Byerlee 1975 USGS record, Lopez-Sanchez flow laws pinned commit, CODATA R, Jackson 2002 GSA Today, Wikipedia BDT/seismogenic/induced/RMA/rheology/Mohr-Coulomb/Mohr circle, Commons) |
| 17 | faults-folds-fabrics | written 2026-10-23 | 14 + 3.3 sol. | 5 TikZ (fault elements, Anderson blocks, 3D fold, classes, chevron cleavage train) + 4 Commons photos; props: slip components, strike-slip sense, free surface, fold from limbs (cross product), intersection lineation, bedding-cleavage (proved for straight limbs); Anderson thm; problem named number 231 m |
| 18 | earthquake-source | written 2026-10-23 | 14 + 3.3 sol. | 12 exos 4/5/3 + 24-q problem 'The next great earthquake on a locked fault' (invented segment; named: Mw 7.95); figures: TikZ fence rebound, TikZ first-motion quadrants, 2 PD photos (1906 PSM fence, Wallace Creek USGS), beach balls (beachballs.py, lower-hemisphere equal-area, lune clipping), interseismic profiles (interseismic.py), Gutenberg-Richter + moment share (gutenberg_richter.py on usgs-m6.csv, b = 1.01 over 6.0-7.5), AI b1-seismic-analysis in an inthelab box; 13 tests in test_earthquake_source.py; props recurrence, moment steps, first-motion sign, two nodal planes, interseismic (admitted, Savage-Burford), profile (a-d, cycle closes), GR (admitted), largest-events geometric series; method reading a beach ball; ledger +19 sources/21 rows (USGS event JSON Tohoku/Sumatra, USGS PP1515 Wallace/Thatcher, Smith-Konter 2009 mu and locking depths, Wikipedia) |
| 19 | weathering-clays | written 2026-10-23 | 12 + 2.5 sol. | 12 exos 4/5/3 + 24-q problem 'From granite to clay' (invented river; named: 158 kg CO2 per tonne of anorthite); figures: degrees bar chart (hydrolysis.py), ionic-potential diagram (ionic_potential.py, Shannon VI radii), TikZ clay structures at proportional basal spacing, 3 Commons photos (grus Targassonne CC BY 2.5, bauxite Weipa CC BY-SA 2.5, kaolinite SEM USGS PD); 8 tests in test_weathering_clays.py; props surface 6/(rho d), feldspar hydrolysis (4 reactions), immobile-element mass balance, ionic-potential fields (admitted, Goldschmidt), 2:1 layer charge, weathering and CO2; method balancing a hydrolysis; table of clay families (XRD treatments, CEC); inthelab XRD; history laterite/kaolin; ledger +21 sources/28 rows |
| 20 | erosion-transport | written 2026-10-23 | 13 + 2.5 sol. | 12 exos 4/5/3 + 23-q problem 'How fast are the Varden Hills wearing away?' (invented river 80 km2; named: 12.8 Myr to lower the hills 100 m with isostasy); figures: TikZ loads + forces on a grain, AI muddy river + Commons Mississippi plume (NASA PD), settling.py (Stokes vs Ferguson-Church), threshold.py (Soulsby theta_c and tau_c; Hjulstrom-type diagram h = 1 m with Rouse-2.5 suspension limit, cohesive field schematic); 6 tests in test_erosion_transport.py; props flux (covariance), Stokes settling (derived), combined law (admitted), depth-slope (derived), Soulsby (admitted), suspension criterion (admitted), denudation from loads, cosmogenic steady state N = P0 Lambda/(rho eps) (derived); method yearly load from gauging; inthelab 10Be; history Hjulstrom 1935/Shields 1936; load and denudation rate RE-FOUND Book 2 g12 (rebound recalled, not re-derived); ledger rows ALL WIKI except syvitski/portenga/commons: re-source under Sync 2 |
| 21 | clastic-sediments | written 2026-10-23 | 13 + 2 sol. | 12 exos 4/5/3 + 24-q problem 'Reading a core from a delta' (invented 24 m borehole, 4 units; named: mean palaeocurrent 9 deg (8.6), R 0.948); figures: grain_size.py histograms + cumulative curves (step tables close the last class), TikZ bed phases + Southard-type phase diagram, climb geometry + Aztec Sandstone photo (CC BY-SA 2.0), meander + point-bar log, delta triangle + Lena Landsat (PD), Bouma log + Becke-Oese photo (CC BY-SA 3.0), AI core-lab; table of classes; 9 tests in test_clastic_sediments.py; props graphic measures of a normal (0.996 sigma), bedform migration flux, climbing (tan theta = a/c, T = L sin theta), vector mean of azimuths, progradation a = v tan alpha, turbidity-current speed (all derived); methods graphic/moments, palaeocurrent; history Grand Banks 1929 (Heezen-Ewing 1952 read from page images, NRCan); ledger +13 sources / 23 rows, no wiki; Walther's law and facies models left to Year 3 (Sync 3); stereographic rotation pointed to Year 3 |
| 22 | chemical-biogenic-sediments | written 2026-10-23 | 12 + 2 sol. | 12 exos 4/5/3 + 24-q problem 'Salt from a vanished sea' (invented sea 1e5 km2, 1000 m; named: 116 fillings for 1.5 km of halite); figures: TikZ reef types + Bora Bora ISS (PD), rimmed shelf/ramp, microfossil triptych (E. huxleyi CC BY 2.5, Orbulina CC BY 4.0, NOAA diatoms PD), ccd_flank.py ridge flank with CCD, evaporation.py onsets + masses, barred basin; table of seawater ions; 8 tests in test_chemical_biogenic_sediments.py; props accretion a = G/(rho_s(1-phi)), keep up or drown, crossing the CCD t_c = ((z_c - d_r)/C)^2, salt from a column, barred basin k = Qin/(Qin - EA) (all derived); method locating lysocline and CCD; history Darwin 1837/1842; ledger +16 sources / 19 rows (TEOS-10, McCaffrey 1987 abstract via Crossref, Warren, webmineral, Slotnick 2015, Britannica via Wayback, Zhang 2022, Perry 2015, Darwin Online, Treguer 2021, Vasiliev 2017, NASA EO, 4 Commons), no wiki; atoll subsidence left to Year 2 (oceanic-islands); 'compensation depth' (ch. 11 isostasy) is a homograph inside 'carbonate compensation depth': curate in Phase C |
| 23 | diagenesis-basins | written 2026-10-23 | 12 + 2.3 sol. | 12 exos 4/5/3 + 24-q problem 'Decompacting a basin's fill' (invented well: sandstone 0-800 m 15-0 Ma, shale 800-2600 m 55-15 Ma, chalk 2600-3200 m 75-55 Ma, assumed eustatic falls 60 and 30 m; named: shale thickness at deposition 2124 m); figures: compaction.py porosity curves + decompaction bars, Athy table, Potsdam quartz overgrowths (Rygel CC BY-SA 4.0, scale bar cropped), TikZ four basin types, AI drilling rig in an inthefield box, TikZ accommodation at two times, sea_level.py on the new dataset bachelor-1-sealevel-stack (Spratt & Lisiecki 2016, NOAA NCEI) with Lambeck -134 m; 8 tests in test_diagenesis_basins.py; props Athy (admitted), solid thickness (derived, uniqueness), dolomitisation volume -12.1 % (derived), accommodation budget dA = dE + S = dT + dW (derived), sediment loading h = Y(rho_m - rho_w)/(rho_m - rho_s) from ch. 11 equal masses; method decompaction (Newton); ledger +12 sources / 13 rows (Lambeck 2014 via PMC, Spratt 2016 + NOAA data, pyBacktrack pinned commit for Sclater-Christie parameters, SC80 abstract + reference list via Wayback, Oye 2020 OSTI, Walderhaug 1996 Crossref, W&S chapter L, Britannica Paris Basin via Wayback, Commons), no wiki; pressure solution left to Year 3 (prose), backstripping to Year 2 |
| 24 | stratigraphic-scale | written 2026-10-23 | 13 + 2.5 sol. | 12 exos 4/5/3 + 24-q problem 'Correlating three sections across a basin' (invented basin: sections A/B/C 25 and 20 km apart, Kell Sandstone under Mardon Shale, ashes 152.40(4) and 151.20(4) Ma, invented ammonites Vardenoceras primum/medium/ultimum and facies-bound bivalve Ostreola; values in calc/ch24.py; named: boundary (FAD V. medium) at 151.82(3) Ma); figures: Zumaia golden-spike photo (Josugoni CC BY-SA 4.0), TikZ range chart + biozone correlation, TikZ diachronous transgressive sandstone with time lines, GSSP table (8 rows), K-Pg boundary photo Trinidad Lake (Nationalparks CC BY-SA 2.5), ics_chart.py Phanerozoic chart from the shared ics rows (7 tests in test_stratigraphic_scale.py, incl. colours = style file); props: speed of a transgression u = R/s (derived), age between two dated levels + uncertainty propagation (derived); method: correlating by biozones; dated boxes 2026 (80 ratified GSSPs, 21 of 101 Phanerozoic stages without) and 2024 (Anthropocene vote 4/12/3); ledger +10 sources / 23 rows (ICS GSSP table, abridged International Stratigraphic Guide, OpenGeology ch. 7 via Wayback, IUGS 2024 statement via Wayback, Alvarez 1980 / Renne 2013 / Burgess 2014 via Europe PMC, chart.ttl, Commons x2); GSSP rows keyed gssp:*, not ics:* (shared prefix left to the shared ledger); no wiki; mass-extinction causes left to Year 2, magnetostratigraphy and facies models to Year 3 (prose) |
| 25 | radiometric-methods | written 2026-10-23 | 13 + 3.5 sol. | 12 exos 4/5/3 + 25-q problem 'Dating the Varden granite and its cover' (whole-rock Rb-Sr isochron 309.6(12) Ma, initial 0.70803; K-Ar biotite 296.0 and hornblende 304.0 Ma; zircon U-Pb 310.6 Ma concordant; closure 530/280 C (Leeds table); ash in the Triassic sandstone 247.30 Ma, base 248.2 Ma, gap ~62 Myr, erosion 0.19 mm/yr from 9 km; values in calc/ch25.py; named: cooling rate 31 C per Myr); figures: zircon CL photo (Roquette CC BY-SA 4.0), decay_curves.py, systems table, isochron.py (invented rhyolite 424.5(8) Ma, NOT the Varden granite so the problem is not solved in the course: deviation from the brief), TIMS photo in the lab box (Radiogenic CC0), radiocarbon.py (IntCal20 0-12 kyr + plateau zoom), closure-temperature bar chart (ledger values), TikZ bracketing schematic; 11 tests in test_radiometric_methods.py; props: radiogenic growth + age equation, precision of an age, least-squares line (derived; slope/intercept standard errors admitted), K-Ar age with branching, cooling rate between closures; thm: isochron (general D/S form); method: fitting an isochron; dated box 2020 (IntCal20); ledger +10 sources / 20 rows (IAEA LiveChart K-40/C-14/Rb-87/Sm-147, Amherst geochronology sheet = Steiger-Jaeger constants + closure temps, Leeds closure table via Wayback, Stuiver-Polach 1977, Reimer 2020 via Crossref, rintcal IntCal20 file, NMGRL K/Ar and Ar/Ar methods page, Tulane radiometric notes (qualitative only), Commons x2); concordia and thermochronology left to Year 3 (prose) |
| 26 | fluid-envelopes-structure | written 2026-10-23 | 13 + 3.5 sol. | 12 exos 4/5/3 + 25-q problem 'A radiosonde and a CTD on the same day' (invented CTD cast: mixed layer 52 m, linear EOS about (35, 10 C), AAIW min 34.32 at 800 m, NADW max 34.90 at 3000 m; mixing C (200 m) + I (800 m): cabbeling +0.14 kg/m3, mixture density near 500 m; invented sounding A-J with a superadiabatic surface layer over a warmer sea, a near-neutral B-C layer capped by an inversion at 1.5 km, tropopause G 12.5 km -59.0 C 186 hPa; N in H-I 0.0216 s-1 vs thermocline 0.0100; values in calc/ch26.py; named: theta at the tropopause 346 K); figures: CTD rosette photo (NASA GSFC PD, ICESCAPE), layers table (USSA76), atmosphere_profile.py (T and theta to 32 km + dry adiabat), TikZ parcel method, seawater_eos.py profiles (theta, S, sigma_theta: WOA23 10.5S/30.5S 25.5W new + Book 2's Canada Basin column) and theta-S diagram (isopycnals, water-mass cores, cabbeling example), density/alpha/beta table; 11 tests in test_fluid_envelopes_structure.py; props: pressure in a layer of constant gradient, potential temperature, linear EOS, mixing lines straight; thms: dry adiabatic lapse rate g/c_p (c_p = 3.5 R/M with gamma 1.4, NASA GRC), static stability (N^2 both forms); methods: reading a sounding, reading water masses; ledger +6 sources / 16 rows (NASA GRC gamma, NWS glossary x4, UNESCO 44 ATG/THETA, TEOS-10 x7, Tomczak water masses, WOA23 b3 columns, Commons CTD); moist adiabat left to Year 2 (prose); sigma_2 / reference pressure left to Year 2 (prose) |
| 27 | radiation-heat-transport | written 2026-10-23 | 12 + 3 sol. | 12 exos 4/5/3 + 25-q problem 'How much heat crosses the 40th parallel?' (five 10-degree bands 40-90 N of NCEP R1 insolation/albedo/OLR, global mean net -12.90 removed, cap deficit 4.108 PW; latent part from cap LE 42.4 and P 1.95 mm/day with global LE-LP 2.07 removed: 1.40 PW, 34 %; ocean via Trenberth-Caron 22 %; values in calc/ch27.py; named: transport across 40 N 4.11 PW); figures: EPIC Earth photo (NASA GSFC PD), insolation.py matrix plot (day x latitude, viridis, subsolar and polar-night lines) and solstice/annual curves, energy_balance.py TOA ASR/OLR vs sin(lat) with fill between, TikZ polar-cap control volume, transport curve (total + latent, Trenberth-Caron 5.0 PW square), surface LE/LP/H vs sin(lat), TikZ surface balance R_n = LE + H + G (AR6 values); 13 tests in test_radiation_heat_transport.py; thm: daily-mean insolation; props: polar summer (pi tan delta), global mean S0/(4 sqrt(1-e^2)), MHT from net radiation, precipitation energy 78.1 W/m2 per m/yr, surface energy balance; method: transport from zonal bands; ledger +5 sources / 6 rows (NCEP R1 PSL dataset + PSL metadata record, Kalnay 1996 Crossref, Trenberth-Caron 2001 in book3 + tc01:method, Commons EPIC); NCEP R1 radiation is biased (albedo 0.342, net -12.9): said in the text, transport ~20 % low vs T&C, said in the text; the brief's [S] transport-arrows schematic replaced by the data curve + cap control volume (Book 2 g10 already has the arrows schematic) |
| 28 | atmospheric-circulation | written 2026-10-23 | 14 + 3 sol. | 12 exos 4/5/3 + 25-q problem 'Reading a mid-latitude weather map' (station P at 50 N, isobars every 4 hPa 250 km apart, 1006 hPa, 10 C: rho 1.238, f 1.117e-4, 1/f = 2.49 h; surface wind 9.0 m/s at 25 deg: linear-drag tau 5.3 h; inflow 1.48e10 kg/s into a 500 km low, ascent 1.31 km/day; ring wind 134.1 vs DJF jet 42.3, M/M0 0.829; values in calc/ch28.py; named: geostrophic wind 11.6 m/s); figures: Gulf of Alaska cyclone photo (NASA MODIS/LANCE PD; the Iceland low was dropped because Book 1 g8 prints it), TikZ force balance with linear drag, weather_map.py invented map with windbarb pics (24 stations), general_circulation.py streamfunction DJF/JJA (NCEP R1 2.5-deg pressure levels, new datasets ncep-{uwnd-p,vwnd-p,uwnd-sfc,slp}), TikZ three cells (globe + section), angular_momentum_wind.py vs u200, ITCZ GOES-11 photo (NASA EO PD), monthly ITCZ latitude (prate-monthly), TikZ Walker; 8 tests in test_atmospheric_circulation.py; props: PGF, horizontal Coriolis -f k x v, friction with linear drag (tan a = 1/(f tau), V = Vg cos a), angular-momentum wind; thm: geostrophic wind; remark: gradient wind (told, used in exo 10); new definition 'mean meridional streamfunction' (added to DEFINITIONS); dated box 2021 (AR6 Hadley widening); history boxes Buys Ballot 1857, Hadley 1735 / Ferrel 1856; ledger +10 sources / 17 rows (NCEP R1 2.5-deg, NOAA JetStream jet + circulations via WebFetch, Hadley 1735 Crossref, MacTutor Ferrel, SKYbrary Buys Ballot, IPCC AR6 ch. 2 key now in book3, climate.gov Walker, NWS glossary x7, Commons x2); the zonal SLP / surface-wind figure of the plan left as numbers in the text |
| 29 | ocean-circulation | written 2026-10-23 | 14 + 2.5 sol. | 12 exos 4/5/3 + 25-q problem 'An upwelling coast' (invented coast at 38 N, ocean to the west, summer wind from the north at 8 m/s: C_D 1.168e-3, T 0.0972 Pa, f 8.979e-5, M 1082 kg/(m s), D_E 77.5 m, w 4.55 m/day over 20 km, heat 25.9 MW/m; values in calc/ch29.py; named: 1.05 Sv per 1000 km); figures: Gulf Stream SST photo (NOAA NESDIS PD), gyre world map (ommap + shared land, hand-placed arrows), ekman_hodograph.py hodograph + profiles (Ekman's constants, 10 m/s at 35 N: D_E 100 m, V0 0.17 m/s), TikZ coastal upwelling plan + section, stommel_gyre.py 2x2 (uniform vs beta, streamlines + v sections; eps 0.03, 301x101 sparse FD), TikZ Atlantic MOC section with RAPID layer transports, deep SOLO float photo (NOAA PD) in an inthelab box; 7 tests in test_ocean_circulation.py; defs wind stress (bulk formula, Yelland-Taylor C_D), gyre, Ekman layer/transport/spiral + sverdrup, upwelling/coastal upwelling, western boundary current, MOC/thermohaline/deep-water formation; thm Ekman transport (derived), props spiral (admitted, ex. 10 checks), coastal upwelling, Ekman pumping, heat of an overturning (all derived); history Nansen/Ekman, Stommel 1948; dated 2021 AR6 AMOC (calibrated); ledger +23 sources / 29 rows (Stewart LibreTexts, RAPID, Donohue 2016, Stommel 1948, Lien 2015, NOAA floatees/Argo, NOS, IPCC AR6 SPM + ch. 2, TEOS-10 cp0, Commons x2), no wiki; Sverdrup balance and vorticity left to Year 3 (prose) |

### Ch. 4 Phase B fixes (my files only)

1. Weekend-problem layout: the unbreakable data table is pushed to the next
   page, leaving about a third of a page blank (pilot build p. 20). Put the
   table beside the map or after a short paragraph; re-render at 130 dpi; add
   a FIGCHECK line.
2. Q17 uses "trend and plunge" (owner ch. 6) and the chapter uses "hanging
   wall" (owner ch. 17): add a one-clause gloss where each first appears.
3. Q18 extrapolates "8 km farther north", beyond the 8-km map: harmless; keep.

### Ch. 27 traps (2026-10-23)

- NOAA PSL THREDDS rate-limits (HTTP 429) after a few requests: fetch one key at a time
  with 60-120 s pauses in a background loop (see the ch. 28 fetch). noaa.gov
  (CloudFront) blocks curl from this machine: WebFetch reaches the NOAA JetStream pages.
- NCEP R1's TOA radiation is biased (global albedo 0.342 vs 0.294 assessed, net -12.9
  W/m2); NCEP R2 (tested on 2015) gives the same ~4.0 PW transport. Removing the mean is
  necessary but does not fix the too-weak meridional gradient: the chapter says so
  (Trenberth-Caron's abstract itself warns about model-generated fluxes).
- R1's incoming solar implies S0 = 1367 W/m2 (problem Q5 derives it); band means of the
  insolation exceed central values by 0.5-1.7 %.
- `pgrep -f "<pattern>"` inside a waiting loop matches the loop's own bash command line:
  wait on the build task's output file instead.
- `\degree` is not defined outside siunitx: write `\ang{90}`.
- `tools/fetch_data.py` Book 3 block: derive_b3_ncep_zonal now also writes
  `<key>-monthly.csv` (month, lat, value), used for the ITCZ of ch. 28.

### Ch. 25 traps (2026-10-23)

- The physics series owns "radioactive decay and radiometric dating's law":
  ch. 25 recalls the decay law and derives D* = P(e^{lambda t} - 1) as a
  proposition (no definition of decay, half-life or decay constant).
- Two sets of 40K constants: IAEA/ENSDF (1.248e9 yr, 10.72 % EC) vs the
  geochronology convention (Steiger-Jaeger, from the Amherst sheet: lambda
  5.543e-10, lambda_e 0.581e-10 -> 10.48 %). All ages are computed with the
  conventional values; the text says so. NMGRL gives 40K = 0.01167 %, IAEA
  0.0117 %: the problem uses IAEA's.
- A ledger row once said "irradiation turns 39K into 39Ar" citing the Amherst
  sheet, which does not say it: re-sourced to the NMGRL methods page
  (39K(n,p)39Ar). Read the source for every clause of a row.
- Unsourced first-draft claims removed: isotope dilution, ion-probe spot
  sizes and zircon cores/rims, "closure temperature depends on grain size and
  cooling rate", "a crystal that lost argon from its rims shows young first
  steps", "Devonian base with no close bracket", "ash beds date the K-Pg"
  (Renne 2013's abstract says 40Ar/39Ar, synchrony within 32 kyr).
- IntCal20 is not monotonic at every 1000-yr step beyond 50 cal kBP (53 -> 54
  kBP decreases): the test checks 0-50 kBP. At 2000 cal BP the radiocarbon
  age is 70 yr OLDER than the calendar age (ex. 7 asks the direction).
- pgfplots `yticklabels` splits on commas: brace each label; with
  `y dir=reverse` list the symbolic coordinates top first.
- Axis nodes outside [ymin, ymax] are clipped silently (the isochron's
  initial-ratio label vanished).
- Adding a credits line pushed the front matter one page: PDF page = printed
  + 12 from ch. 25 on (re-check with pdftotext before rendering).

### Ch. 26 traps (2026-10-23)

- Module names are global across years in one pytest session: Book 1 has
  `figdata/grade-8/standard_atmosphere.py`, so Book 3's is
  `atmosphere_profile.py` (never reuse another year's module name).
- The NCEI THREDDS server returns HTTP 502 intermittently: fetch the WOA
  columns one key at a time and retry (sa10-t and sa30-t needed a second run).
- ametsoc.org (AMS glossary) blocks this machine (Cloudflare): the NWS glossary
  (forecast.weather.gov/glossary.php?letter=x) gives the definitions instead;
  c_p from gamma = 1.4 (NASA GRC) and the USSA76 R*/M0.
- UNESCO 44 (phionics.com copy) prints ATG, THETA (RK4) and DEPTH with check
  values; all reproduced to the printed digits. WOA23 temperatures are scaled
  by 1.00024 (TEOS-10 s. 2.1) before the IPTS-68 formulas.
- sigma_theta referred to the surface puts the AABW at 30.5S (27.854) below
  the NADW (27.857) and decreases at the bottom at 10.5S: said in the text
  (alpha/beta varies with pressure, sigma_2 next year), not hidden.
- A first sounding put warm air (26 C) over a cooler sea (22.4 C) with a
  superadiabatic surface layer: physically inconsistent; fixed by making the
  air cooler than the sea (22.0 C).
- The first parcel figure drew the unstable case with the sounding on the
  warm side of the adiabat (i.e. stable): check the side of every schematic
  against the inequality it illustrates.
- Adding ch. 26's credit line pushed the front matter again: PDF page =
  printed + 13 from ch. 26 on.

## Phase C (DONE 2026-10-23)

1. **Term links.** `tools/link_defined_terms.py --book 3` with
   `tools/term_config/book3_en.py` (AMBIG_POLICY "drop"; STOP and
   EXTRA_PROTECT curated for the homographs of BRIEFS.md: CCD detector vs
   carbonate compensation depth, "compensation depth" inside "carbonate
   compensation depth", etc.). Result: **4654 links, 511 linkable terms, 184
   distinct targets**; a second run prints "links to insert: 0" (idempotent,
   re-checked after every Phase C edit). Trap: a STOP entry does not suppress
   the local defining-chapter sense of a term; protect the phrase
   (EXTRA_PROTECT) instead. The links moved no page (per-page pdftotext md5,
   build61 vs build62: only pp. 106 and 350 differ, both from Phase C fixes).
2. **Figure pass.** All 182 figures (160 `omfigure`, 22 standalone
   `\includegraphics`; 125 TikZ/pgfplots, 57 photographs/AI) re-checked on
   their own pages at 130 dpi, map from captions to pages by
   `scratch fc/figs.py`; FIGCHECK.md "## Phase C full pass" has one line per
   figure. 11 fixed (ch. 5 north arrow, ch. 10 caption, ch. 14 Okhotsk label,
   ch. 15 scale arrow, ch. 16 placement, ch. 22 two labels, ch. 23 Lambeck
   leader, ch. 25 labels 15/31, ch. 26 Central Water, ch. 27 latent label,
   ch. 28 JJA clipping), every one re-rendered and seen fixed. Lesson: the
   Phase B per-chapter checks missed 11 label/placement defects that a
   whole-book pass found.
3. **Solutions re-read** (all 29 chapters, every exercise and problem
   question recomputed in python, scratch `calc/chNN.py`, pairs from
   `phc/pairs.py`). Slips fixed: ch. 12 problem Q24 range (18.95 to 19.02
   mm/yr); ch. 16 Q24 rounding display (11.049 MPa, answer 11.0); ch. 19
   458.3 -> 458.2 kg (twice), 927.9 -> 928.0 kg, 1.9 -> 1.8 %; ch. 23 exercise
   12, half of 24370 moles printed 12190 -> 12180; ch. 27 exercise 8, -12.8
   (rounded terms) vs -12.9 W/m2 (unrounded, the course example) reconciled
   and 224.9 -> 224.8, 15.1 -> 15.2. Course text: ch. 9 missing verb ("its
   mantle by about 100 C per billion years at present"); 14 plain "exercise N"
   in chapters 6, 9, 10, 11, 12 and 3 in solutions 6, 7 turned into `\cref`.
4. No AI stubs; no PNG under images/book3 (JPEG only). Three generated AI
   images are unused (`b1-clean-lab`, `b1-rock-press`,
   `b1-trade-wind-ship`): left in place (no deletes), not printed.
5. DEFINITIONS.md checked: its 202 labels all exist and every `def:b1:`
   label has a row; the "planned" note replaced.
6. Final state: build65 **0/0/0, 452 PDF pages**; `gates.sh bachelor-1` OK;
   229 Book 3 tests pass (`make test` 249 pass, 1 fail =
   `test_repo_ledger_is_clean` on Book 4's `parts/bachelor-2/19-phanerozoic-earth.tex`
   `data:etopo-1deg`, not ours); `check_ledger` reports nothing in
   bachelor-1; wiki grep 0; `make figdata Y=bachelor-1` (52 scripts, 275
   tables) byte-identical (md5).

## Page projection

Target ~350 pp. Plan: 29 chapters × ~12 pp (course + exercises + problem +
solutions) ≈ 348 pp + ~18 pp front matter, credits, index ≈ 366 pp (pilot ch.
4 ≈ 14 pp). Projection to be re-measured after chapters 8, 16 and 24: more
than 10 % under the per-chapter target (below ~10.8 pp per chapter average)
means restoring depth before going on.

- **After ch. 8 (2026-10-22):** course pages (chapter openings from the
  `.aux`) 11, 12, 9, 11, 10, 9, 11, 11 = 84 pp; solutions of ch. 1--8 run
  PDF pp. 116--133, about 18 pp. Per chapter 102/8 = **12.75 pp**, above the
  12-pp plan (no depth to restore). Projection 29 x 12.75 = 370 pp + ~18 pp
  front matter, credits and index = **~388 pp**, about 6 % over the ~366 target:
  keep chapters at their current depth, do not pad; the thinnest (ch. 3, 6:
  9 pp) are still within 10 %.
- **After ch. 16 (2026-10-23):** chapter openings from the `.toc`: ch. 1--16
  occupy printed pp. 2--184, 183 pp, **11.4 pp of course per chapter** (ch.
  9--16: 12, 12, 12, 13, 13, 12, 12, 13); solutions of ch. 1--16 run printed
  pp. 199--228, about 30 pp, 1.9 per chapter. Per chapter **~13.3 pp** with
  solutions, well above the 12-pp plan: no depth to restore. Projection
  29 x 13.3 = 386 pp + ~18 pp front matter, credits and index = **~404 pp**,
  about 10 % over the ~366 target. Do not pad; do not cut either (the rule
  only guards against thin chapters); report the overrun in Phase D.
- **After ch. 24 (2026-10-23):** chapter openings from the `.toc`: ch. 1--24
  occupy printed pp. 2--291, 290 pp, **12.1 pp of course per chapter** (ch.
  17--24: 14, 14, 12, 13, 15, 12, 12, 13 = 105 pp, 13.1 per chapter);
  solutions of ch. 1--24 run printed pp. 298--359, about 62 pp, 2.6 per
  chapter. Per chapter **~14.6 pp** with solutions, above the 12-pp plan: no
  depth to restore. Projection 29 x 14.6 = 423 pp + ~18 pp = **~440 pp**, about
  20 % over the ~366 target; the overrun comes from the solutions (2.5 pp, not
  the planned ~1) and from ch. 17--24 running at 13 pp. Do not pad; do not cut;
  report in Phase D.

- **After ch. 29, end of Phase B (2026-10-23):** chapter openings from the
  `.toc`: ch. 1--29 occupy printed pp. 2--357, 356 pp, **12.3 pp of course per
  chapter** (ch. 25--29: 13, 13, 12, 14, 14); solutions printed pp. 359--434,
  76 pp, 2.6 per chapter; index pp. 435--439. Per chapter **~14.9 pp** with
  solutions; the PDF has **452 pages** (13 front-matter pages before printed
  p. 1), about 23 % over the ~366-page target, none of it thin (no chapter
  under 9 pp, the thinnest are the early ch. 3 and 6). Overrun reported in
  Phase D; nothing padded or cut.

## Counters

- Searches used: **~40** of ~600 (ch. 21--29: about fifteen, for Spratt-Lisiecki, Lambeck, Sclater-Christie, the GSSP table, IntCal20, the Leeds closure table, UNESCO 44, NCEP R1 paths, the AR6 AMOC wording and the Kuroshio transport (Lien 2015); direct fetches: Stewart LibreTexts chapters, RAPID, NOAA floatees/Argo/JetStream (WebFetch), NOS, Donohue 2016, Stommel 1948, Commons API; ch. 20: one, for Syvitski 2005 (WHOI PDF); direct fetches: Wikipedia raw sediment transport, Hjulstrom curve, Shields parameter, Filip Hjulstrom, Albert F. Shields, viscosity, water data page, dissolved load, grain size; CoastalWiki sand transport; Portenga 2011 GSA Today PDF; Commons API; ch. 19: about four, for the Goldschmidt boundaries and the silicate CO2 flux; direct fetches: Wikipedia raw pages weathering, Goldich, carbonate-silicate cycle, enhanced weathering, clay mineral, kaolinite, smectite, montmorillonite, laterite, ionic potential, fr alteration, Pedro/Nomade/Dangic/Formoso PDFs, USGS OFR 01-041 via Wayback, Dessert 2003 PDF, webmineral, Commons API; ch. 13--18: about three; ch. 18 direct fetches: USGS event GeoJSON Tohoku and Sumatra, USGS PP1515 PDF, Smith-Konter 2009 PDF, Commons API, ~15 Wikipedia raw pages; ch. 12: about four, for the MIDAS IGS20 path, the Heine 2013 rotation table and a GNSS station photo; direct fetches: MORVEL 2010 author PDF, PROJ ITRF2014 file, NGL MIDAS files, Wikipedia raw pages geomagnetic reversal, plate tectonics, triple junction, Azores triple junction, geology of Iceland, Mid-Atlantic Ridge, Vine-Matthews-Morley; ch. 11: none -- direct fetches: Pratt 1855 scan on Zenodo record 1432414, Wikipedia raw pages isostasy, Pratt, theoretical gravity, gravity anomaly, free-air anomaly, geoid, post-glacial rebound, gravimetry, GOCE, gal, Vening Meinesz, vertical deflection, bathymetry, satellite geodesy; Commons API; ch. 10: four -- Hasterok heat production
  (found the EGU2010 Vila abstract, used), mantle potential temperature (found
  Katsura 2022 open PDF at epub.uni-bayreuth.de, used), Hasterok 2018 title
  (Adelaide repository unreachable), linear heat-flow relation (found the SMU
  Roy-Blackwell-Decker 1972 text, used); ch. 10 direct fetches: Davies 2010 PDF,
  GSA Today England 2007 PDF, Wikipedia raw pages heat budget, geoneutrino,
  KamLAND, natural uranium, K-40, thorium, age of Earth, thermal conductivities;
  ch. 9 direct fetches: PREM PDF, ~20 Wikipedia raw pages, Commons API; ch. 6: one search for the thin-section
  thickness source; ch. 7: one search for Goldschmidt's 15 % rule -- results
  for the Phase D list: classes.colgate.edu/rapril/geol201/summaries/atsub.html
  (fetched, ledger COLGATE-SUB), pages.uoregon.edu/cashman/GEO311/311pages/L5_crystallization.htm,
  faculty.uml.edu Eby Chapt. 4 Crystal Structures pdf, socminpet.it Brixen 2018 Ardit pdf) (web searches; ch. 5 Siccar Point: Wikipedia,
  IUGS geoheritage, NCSE, Scottish Geology Trust geoguide -- list them in the
  Phase D report) + 1 WebFetch; direct URL fetches ~42 so far (USNO, MPC,
  SIMBAD x10, NASA fact sheets, CFHT manual, ESA Gaia, NASA EMS, LJMU pivot
  wavelengths, Commons API, IUGS). Phase A: ~8 direct probes.
- AI images: batch1 of 17 (log `scratch/ai/batch1.log`, may still be running:
  never wait on it with pgrep -f); used so far: compass-clinometer (ch. 4),
  sextant (ch. 1), observatory-dusk (ch. 2), tunnel-boring (ch. 5),
  field-notebook and thin-section-lab (ch. 6), microscope-student (ch. 8).
  All 17 reviewed 2026-10-22: heatflow-probe, gravity-survey, rock-press,
  gnss-station, muddy-river, core-lab, drilling-rig, clean-lab,
  trade-wind-ship, ctd-rosette OK; seismometer-vault was an UNRELATED image
  (a child on a beach) and was regenerated (scratch `ai2/ai_nofallback.py`,
  output reviewed OK, installed).
- **Tool defect (report in Phase D):** `tools/ai_images.py` falls back to the
  newest PNG under `~/.codex/generated_images` made since the call started;
  with several agents generating at once this picks up another book's image.
  Use the scratch copy `ai2/ai_nofallback.py` (AI_DEST=<dir>, no fallback),
  review, then copy into `images/book3/ai/`.
- Photographs: Smith 1815 map (ch. 4), Paranal star trails (ch. 1), JWST mirror
  segments (ch. 2), terrestrial planets, Venus radar globe, Mars Valles
  Marineris, Europa, Io (ch. 3), Siccar Point (ch. 5, PawełS CC BY-SA 4.0),
  granite XPL (ch. 6), six minerals + calcite rhombs (ch. 7), gabbro PPL/XPL
  pair (Chmee2) and Michel-Levy portrait (ch. 8).
  Credits in `images/book3/CREDITS.md` and `frontmatter/image-credits-book3.tex`.
- Ledger rows (`sources/ledger/book3.md`): `check_ledger.py` OK, 613 rows
  checked over parts/bachelor-1 incl. shared (after ch. 8).
- Traps noted for Phase C: "CCD" is both the detector (ch. 2, prose only) and
  the carbonate compensation depth (ch. 22 owner): do not index "CCD" as an
  alias in ch. 22, or STOP it in book3_en.py. Figures inside `omfigure` have
  no counter: refer to them in prose ("the figure below"), never \cref.
- Build trap: when the index is exactly one page long the log shows one
  "Overfull \vbox (21.8pt too high) while \output is active" at the .ind (seen
  after ch. 5, gone after ch. 6). It depends only on the index length; the entry
  file is not ours: if it comes back at the end, report it.
- Structure contours across a fault: never contour `contact_elevation` across
  the fault (marching squares piles lines along the step); contour each block
  with `_contact_unfaulted` and clip to the block (`varden_sections._clip_runs`).

## Resume instructions (for a fresh agent)

1. Read `sources/BATCH_BOOKS_1-5.md` (rules, phases), `CONTRIBUTING.md`,
   the repo `CLAUDE.md`, `OUTLINE.md` (Years 1--3 map), `SERIES_DEFINITIONS.md`,
   then `BRIEFS.md` and `DEFINITIONS.md` here. Read the pilot
   `parts/bachelor-1/04-geological-maps.tex` as the model chapter.
2. Find the first chapter whose status above is not "written"; write it from
   its brief: chapter `.tex`, `solutions/<nn>-<slug>.tex`, figdata scripts in
   `figdata/bachelor-1/` with tests in `tests/bachelor-1/`, ledger rows,
   images + credits. Update the row here at once.
3. Per chapter, before moving on: `make figdata Y=bachelor-1`,
   `make test Y=bachelor-1`, build the entry file (`nice -n 10 latexmk`, never
   two at once, never a short timeout), log 0/0/0, `bash tools/gates.sh
   bachelor-1`, `.venv/bin/python tools/check_ledger.py`, calibration check,
   every figure rendered alone at 130 dpi into a fresh scratch subdirectory and
   a FIGCHECK line written.
4. Term links in Phase C: `.venv/bin/python tools/link_defined_terms.py --book 3`
   with `tools/term_config/book3_en.py` (`AMBIG_POLICY = "drop"`), after
   curating the homographs listed at the end of BRIEFS.md.

Scratch: `/tmp/claude-1000/-home-bvirrion-repositories-one-course/073e8d3d-6c62-4a98-8f56-8a0346dd7a8a/scratchpad/book3/`
(write each render into a new subdirectory; never wildcard-rm).

## Conventions settled by the pilot

- University register: propositions and theorems with proofs (plane equation, three-point theorem, V-rule), methods for each technique.
- Every Varden Hills number comes from `figdata/bachelor-1/varden_maps.py` (which imports `figdata/shared/region.py`); printed data are the rounded values, and the solutions are computed from the rounded data.
- Fold, anticline, syncline and fold axis are defined in ch. 4 (`def:b1:geological-maps:fold`, Sync 0 ruling, supersedes the pilot's earlier note); ch. 17 recalls them and owns fold geometry proper (hinge, limb, axial plane, interlimb angle, classification).
- Map scale bars inside a pgfplots axis are drawn in axis units, never with the `scalebar` pic (a pic is sized in cm).
- Known typographic issue: a breakable problem box may move an unbreakable table to the next page, leaving part of a page blank (p. 20) --- Phase B fix listed above.

## Conventions settled in Phase A

- Ledger ids: `<source-family>:<topic>` (e.g. `simbad:sirius-v`,
  `usgs:tohoku-2011-mw`, `nndc:rb87-halflife`); grep both ledgers before
  minting; shared rows (`earth:`, `planet:`, `sun:`, `const:`, `ics:`,
  `data:`) are cited, never duplicated. Id regex
  `^[a-z][A-Za-z0-9]*:[A-Za-z0-9][A-Za-z0-9_.+\-]*$`.
- No bare homograph is ever a defined term: "apparent magnitude", "moment
  magnitude", "extinction angle", "atmospheric extinction coefficient",
  "volcanic arc", "clay mineral", "sedimentary facies", "hydrolysis (of
  silicates)", "birefringence (of a mineral)", "flux (of a source)".
- Physics/chemistry/biology notions (DEFINITIONS.md, last tables) are admitted
  with a prose pointer, never defined.
- Exercise maps and sections use the Varden Hills only.
- No French place is named in print: gate 7's regex rejects the words
  "French"/"France" (reported at the sync).

## Traps

- Ch. 7: chemistry defines "structural formula" (organic sense): ch. 7 indexes
  the qualified form "structural formula (mineral)" (series qualified-forms
  rule; report in Phase D). A figure of several TikZ panels drawn as scaled
  scopes in one picture overlapped: build such grids as a tabular of separate
  tikzpictures with `\useasboundingbox`. In a mineral recalculation the charge
  balance is automatic (each cation keeps its oxide's charge): the site totals
  are the real check -- never present the charge check as a test.

- Ch. 8 (resolved): the CIE 1931 CMF and D65 tables come from the CIE
  data-table DOIs 10.25039/CIE.DS.xvudnb9b and 10.25039/CIE.DS.hjfjmt59 (CC
  BY-SA 4.0), fetched by the `# Book 3:` block of `tools/fetch_data.py`
  (datasets `bachelor-1-cie1931`, `bachelor-1-cie-d65`). A display gain above 1
  saturates the computed Michel-Levy colours and the clipping shifts the
  first-order red: keep gain 1 (normalised to parallel polars) and find the
  order ends on the linear, unclipped G channel. A forsterite-bearing rock
  with quartz is petrologically wrong (problem mineral B is diopside).
- siunitx v3 typesets numbers in math mode: `\textbf{\qty{38}{...}}` prints
  a non-bold number with a bold µ. Named numbers use
  `\qty[text-series-to-math=true]{..}{..}` inside `\textbf` (fixed in the
  solutions of ch. 1, 3, 4, 5 and 8).
- NOAA PSL reanalysis `.nc` files are NetCDF4/HDF5 (scipy cannot read them, no
  h5py): no reanalysis data planned; ch. 27--28 use ledger values and computed
  models instead. CERES needs a login: not used.
- NGL `.tenv3` URL redirected to a malformed host: GNSS velocities for ch. 12
  come from a published table (ledger), not raw time series.
- Homographs to curate in Phase C: see the table at the end of BRIEFS.md
  (declination, altitude, extinction, magnitude, flux, core, plate, arc, cell,
  basin, facies, clay, front, scale, limb, relief, chlorite, formation, member,
  group, stage, sorting, cement, load).
- A pic inside a pgfplots axis is sized in cm; a decoration on a path with
  jumps misplaces its marks; orient traced lines that carry side symbols; dip
  arcs as parametric plots in the vertical plane; error-bar options go on
  `\addplot`; map labels `\scriptsize` with 75--80 % white fill.
- Ch. 12: booktabs is not loaded (`\toprule` is undefined): tables use
  `\hline`. NGL MIDAS IGS20 velocities live at
  `geodesy.unr.edu/gps_timeseries/IGS20/midas/midas.IGS.txt` (and `midas.NA.txt`
  for the North America-fixed frame; columns 9-11 ve/vn/vu in m/yr, 25-26
  lat/lon); the `velocities/` directory holds superseded IGS14 files. Heine et
  al. 2013 Table 2 prints the pole pairs under "Lon, Lat" headers but they read
  as lat, lon (the other reading sends Recife to the Southern Ocean; tested) --
  mention in Phase D. A continent cut from the Natural Earth ring by a lat/lon
  box gives several pieces and a fill that closes across the land: cut the arc
  between two land bridges instead (`south_atlantic_fit._arc`). The
  GPS-only Euler vector (MORVEL Table 6) agrees within 10 % with the geological
  one from the Azores to Iceland but not in the Arctic near the poles: never
  claim global agreement. The outward displacement on the Reykjanes Ridge is
  5.0 km two-sided (MORVEL sect. 4.2.2): any invented stripe profile there must
  include it.
- Ch. 13: `\qty{7(1)}{km}` and even `\qty{7 \pm 1}{km}` print compactly
  ("7(1)"): use `\qty[uncertainty-mode=separate]{7 \pm 1}{km}`. Labels:
  CONTRIBUTING's method prefix is `met:` (ch. 9--12 had `meth:`; renamed in
  ch. 9--13 and their solutions, none left; report in Phase D); lemmas `lem:`.
  The public-domain NOAA pillow shot expl6454 is near-identical to Book 2's:
  ch. 13 uses expl6453 (CC BY 2.0). The depth--age figure reads Book 2's
  `data/derived/grade-11-seafloor-age.csv` (a cross-book data dependency, read
  only; report in Phase D). The Passive margin Wikipedia page says "entire
  coasts of Africa, Australia": overclaim, printed as "nearly all".
- Ch. 14: omfigure has no counter, so `\cref{fig:...}` prints a SECTION
  number: never cross-reference a figure, say "figure below" / "map above".
  Map fills with several rings: write `nan nan` rows and read with
  `unbounded coords=jump` (empty lines left Hokkaido unfilled at low dpi).
  The Kuril strip uses exact spherical along/cross-track distances; a
  perpendicular must use the LOCAL bearing at its foot (the azimuth changes
  along a great circle; the first test failed on that). The bent-shell radius
  is sensitive to the stretch of trench fitted (21.9 deg whole Kuril trench,
  18.1 central only): both are printed. 147 of 478 shallow strip events sit at
  exactly 33 km: printed as a fact of the catalogue, no unsourced reason given.
  PB2002 step velocity (87.4 at azimuth 120) is printed as the Pacific moving
  towards 300 relative to Okhotsk (the line matters, not the sign). AI images:
  run only `$S/ai2/ai_nofallback.py` with `AI_DEST` (the shared tool falls back
  to the newest file in `~/.codex/generated_images`, possibly another agent's);
  `b1-tsunami-centre` waits on the Codex usage limit (log `$S/ai14/log2.txt`,
  output `$S/ai14/out`): if it arrives and reviews well, add it to the ch. 14
  tsunami `inthefield` box as a 0.42 minipage + PROMPTS.md; otherwise leave the
  box text-only. Never write LaTeX through an unquoted bash heredoc (`$L`,
  `$(...)` expand): use `<<'EOF'`.
- Ch. 15: Book 2 (g11) owns the Hawaiian age--distance fit, so ch. 15 fits the
  Pacific Euler pole from track DIRECTIONS (Morgan & Morgan 2007 list, parsed
  by `derive_b3_hotspots` from a pinned Wikipedia revision: `===X plate===`
  sections, `***` sub-hotspots such as Heard must start a new name or they
  overwrite Kerguelen's coordinates, and some coordinates are in the
  `{{Coord|d|m|N|d|m|W}}` form). The swell is read on ETOPO1 1-degree cells keyed
  (lat, lon), not (lon, lat). The two-track sign rule fixes the sense at the
  first hotspot only: check the second (problem Q8). Unsourced literature
  values (Sleep's buoyancy fluxes, published hotspot-frame poles) are NOT
  printed; our own fit is. The Hawaii "0.02 km3/yr per 1000 km of ridge" of the
  Wikipedia page disagrees with 2.7 km2/yr x 7 km (19 km3/yr over 60000 km):
  not used, the 19 km3/yr row is. Bruneau-Jarbidge has no coordinates on its
  page: the Yellowstone exercise uses McDermitt (16.4 Ma) and the caldera
  (631 ka, the caldera page; the hotspot page says 640 ka). Non-floating
  omfigures left half-page gaps: moved the Puu Oo photo to the magma paragraph,
  the bend paragraph before the figures, the rates figure before the map, the
  swell figure after the buoyancy proof. `\ang{304\pm3}` prints "304(3)": write
  `$\ang{304}\pm\ang{3}$`; inline 3-vectors overflow: put them in an aligned
  display.

- Ch. 16: the Wikipedia "Byerlee's law" page gives the high branch as
  "0.5 + 0.6 sigma_n" with MPa, which is wrong: Byerlee 1975 (USGS record
  70010990 abstract) writes it in kilobars, 0.5 kb = 50 MPa; the ledger cites
  the USGS record (report in Phase D). HK03 "wet olivine" from the
  Lopez-Sanchez file lacks its water-fugacity factor and comes out STRONGER
  than dry olivine: not used; the jelly-sandwich debate (Jackson 2002, GSA
  Today) is told in prose only. Effective vertical stress must be
  sigma_v - rho_w g z (hydrostatic), not p (1 - rho_w/rho_local): the latter
  jumps at the Moho. `\pgfmathsetmacro{\mu}` silently overwrites the math
  \mu (a label printed "0.6"): use \mmu, \pphi. A TikZ `"$\theta$"` angle
  label trips gate 7's straight-quote check: write `pic text={$\theta$}`.
  The `\cref`-on-omfigure trap again ("Section 16.1"): refer to figures in
  prose ("the figure below"). An unbreakable inthelab box with a photo and a
  late large figure each left half-page gaps: the box now ends section 3 and
  the envelope figure follows its definition.


### Ch. 28 traps
- The shared `windbarb` pic was never used before (Books 1-2 have no barbs): at scale 0.6 its 1 mm feather spacing makes unreadable combs; draw it full size with fewer stations, clip to the map frame (barbs are not clipped by the axis), and note the first feather after a pennant touches the pennant (shared style: reported, not edited).
- `y dir=reverse` on a pressure axis also inverts the colorbar: add `colorbar style={y dir=normal}`.
- Reanalysis pressure-level winds exist below the ground over Antarctica: cut the streamfunction plot at 70 S, and keep zero lines within 80 deg (psi ~ 0 near the poles is noise).
- Book 1 g8 already prints the Commons 'Low pressure system over Iceland' image: check other books' images before choosing a photo (`grep -rn <file> parts`).
- A gate (pic scaling) fires on any `\pic` without `[transform shape]` in a picture where any other pic is scaled, even an unscaled scale bar.
### Ch. 29 traps (2026-10-23)

- A pgfplots table of contour segments separated by `nan` rows draws as a filled
  hatching unless the axis has `unbounded coords=jump`.
- Stommel's gyre: with eps = 0.05 the bottom friction (eps pi^2) is not small and
  the interior is 18 % off the Sverdrup value; eps = 0.03 on 301 x 101 points, and
  test the interior against the frictional-interior formula (within 1 %), the
  Sverdrup value only within 15 %.
- Module names are global across years: Book 3's Ekman figure module is
  `ekman_hodograph.py` (not `ekman.py`).
- `\pic` scaling gate: every pic in a picture where any pic is scaled needs
  `[transform shape]` (it fired on ch. 28's barb map).
- "Argo programme" trips gate 7 (curriculum word): write "Argo array".
- Stewart's text has `|phi|` in its formulas: never put a pipe in a ledger
  spec field (write abs(phi)).
- NADW sources: ch. 26 says Greenland and Labrador Seas, Stewart says Greenland
  and Norwegian Seas: ch. 29 names all three (Labrador "as Chapter 26 noted").
- Denominators with `\num{a \times 10^b}` must be parenthesised after a slash.
- Label placement in the MOC and upwelling schematics: first drafts overlapped
  three times (AAIW over the upper-limb label, Canary over Gulf Stream, the
  "water rises" label on the arrow tail): render every schematic after each move.

### Ch. 20 traps (2026-10-23)

- Book 2 g12 (`destruction-of-mountains`) already defines sediment load
  (bed/suspended/dissolved), denudation rate (with the Portenga numbers) and
  isostatic rebound (with the Airy proposition, densities 2830/3380): check
  the school volumes before marking a row "new"; ch. 20 re-founds load and
  denudation rate and only recalls the rebound formula.
- `\toprule` etc.: booktabs is NOT loaded; use `\hline`.
- tools/gates.sh 7 flags the bare word "programme" (curriculum check): write
  "campaign", "plan".
- Exercises must not repeat the worked numbers of the text (ex. 2, 3, 6 were
  first duplicates of text examples; changed to 30 um / 2 m, h 0.5 m S 4e-4,
  and the 10 C viscosity).
- Hjulstrom diagram: computed velocities (Soulsby + 5.75 log10(2h/d)) differ
  from Book 2's Earle-based numbers (1 mm picked up at ~20 cm/s); the text
  says threshold velocities depend on depth and data, shape robust.
- CoastalWiki is a wiki: `coastalwiki:soulsby` also fails the Sync 2 grep.
- render.sh takes a NAME, not a path (a full path nests the output dir).

### Ch. 24 traps (2026-10-23)

- The ICS GSSP table (stratigraphy.org/gssps, HTML) parses with
  `calc/gssp_count.py`: 84 rows with coordinates = 80 ratified GSSPs + 2
  proposed (Anisian, Olenekian) + Chibanian SABS + chronometric Eoarchean.
  chart.ttl (ICS-2026-06) flags 80 Phanerozoic stages ratifiedGSSP, but not
  the same 80: the table has Ediacaran and Pridoli (not stage rank), the ttl
  has Valanginian and Wuliuan that the table does not list as ratified with
  coordinates (Phase D note: a small inconsistency between two ICS products).
- The IUGS Anthropocene statement moved (404); fetched via Wayback.
- Europe PMC search API gives abstracts of Science papers (Alvarez 1980,
  Renne 2013) that Crossref lacks.
- siunitx prints `\qty{251.941(37)}{\Ma}` as "251.941(37) Ma": use
  `[uncertainty-mode=separate]` (the chapter-10/15 convention).
- Do not mint `ics:` ids in the Book 3 ledger: the prefix is the shared
  ledger's and Book 1's tests parse it; the GSSP rows are `gssp:*`, chart
  facts `chart:*`, guide facts `isg:*`.
- Caption-vs-drawing check caught one false claim (LAD of taxon a "in the
  middle of zone c" when the bar ended near its base): compute every caption
  statement against the coordinates.
- "Transgression" is defined nowhere in the series (checked all parts/):
  explained in prose in ch. 24; Year 3 `sequence-stratigraphy` may own it.

## Re-sourcing (Sync 2)

Status: started 2026-10-23 after ch. 20. Plan: inventory with
`grep -n -i wiki sources/ledger/book3.md`; for each row find the primary
reference the article cites, fetch it, mint a new source key and a new row id
(no "wiki" in it), replace the id in every `% ledger:` comment and in tests
that read the ledger (`grep -rn '<old id>' parts/bachelor-1 tests/bachelor-1
figdata/bachelor-1`), then delete the old row and source. Text numbers that no
fetched source supports are removed and listed EXCLUDED below. Done chapters
are listed here.

Helpers (scratch): `tools/ledger_del.py R:<id> S:<KEY>` (refuses ids still cited
in parts/tests/figdata), `edits/apply.py <file> <edits.txt>` (blocks
`OLD\n====\nNEW` separated by `\n@@@@\n`, atomic). Fetched sources are kept
in scratch `src/<topic>/` (untrusted: read with pdftotext / python -I).
Inventory at the start: 189 rows / 149 sources (ch. 8: 1, 9: 4, 10: 10, 11: 17,
12: 5, 13: 23, 14: 28, 15: 25, 16: 8, 17: 12, 18: 14, 19: 13, 20: 13, unused
16) -- scratch `wiki_inventory.txt`. Commons photo-provenance URLs
(commons.wikimedia.org, 41 sources) are NOT Wikipedia; they still contain
"wiki": raised for the coordinator in the Phase D report (kept).

Good big sources found: USACE HEC-RAS 2D sediment technical reference manual
(Confluence pages, open), NIST WebBook fluid tables, USGS Professional Papers
(pubs.usgs.gov/pp/<nnnn>/report.pdf), NBS Journal of Research PDFs
(nvlpubs.nist.gov), HAL open archive. Blocked from this machine: mdpi.com,
publications.usace.army.mil, north-norfolk.gov.uk (DNS).

- **Ch. 20 DONE (2026-10-23).** New rows: fc:settling (Ferguson & Church 2004
  author PDF), hecras:thresholds (Soulsby-Whitehouse formula, theta def, 0.047,
  0.03), keulegan:mean-velocity (NBS RP1151: U/u* = 6.25 + 5.75 log10(R/k_s)),
  bagnold:suspension (USGS PP 422-I), nist:water, usgs:wentworth-phi (USGS OFR
  2006-1195 chart), livingstone:world-dissolved (USGS PP 440-G), hjulstrom:curve
  (1935 Bulletin scan), shields:1936 (TU Delft scan of the dissertation). The
  science changed: mean velocity now Keulegan's law with k_s = d (thresholds
  31-34 cm/s instead of 27-29; 3.1 m/s at 64 mm), suspension limit u* = w_s
  stated as Bagnold's criterion (Rouse numbers dropped); figdata, tests, text,
  solutions updated; 6 tests pass. EXCLUDED (text no longer states): Rouse
  ranges 2.5/7.5; Shields' 0.06; Sundborg 1956; Shields "American", "Albert";
  Hjulstrom "doctoral thesis"; world river discharge 37000 km3 and area 101e6
  km2 (replaced by Livingstone's 3.9 Gt and 120 mg/L; ex. 4 rewritten).
  Repo-wide `test_repo_ledger_is_clean` fails only on Book 2's g12.07
  (`holmes13:estimates`, `tulane:radiometric`...): not ours.
- **Ch. 8-11 DONE (2026-10-23).** Ch. 8: annales:michel-levy-director.
  Ch. 9: skoko/prem/hjortenberg/frost/sun/tschauner/badro/bellini rows (Moho 54 km
  Kupa valley; PREM 11/35 km; transition 410/520/660 km; pyrolite 75/17/8;
  Badro 5-10 % light elements, ICB 4.5 %; mantle cooling ~100 C/Gyr); cites
  Book 1's usgs:crust-thickness and usgs:age-earth read-only. Ch. 10: Dye 2012
  isotope heats (U 9.85e-5, Th 2.63e-5, K 3.40e-9 W/kg), IAEA LiveChart
  half-lives, KamLAND 2011, Delaney conductivity, Fischer lithosphere;
  calc/ch10.py keeps the frozen problem-data heats and uses the new ones for
  solutions. Ch. 11: Airy 1855, Pratt 1871, NIST gal, Moritz GRS80, NGS
  absolute gravity, USGS OFR73-98, swisstopo, EGS Vening Meinesz, NASA SVS
  geoid, JPL Seasat, ESA GOCE, Kierulf 2021 (rebound 10 mm/yr).
- **Ch. 12 DONE (2026-10-23).** GPTS now Lourens et al. (2004) via IODP Exp
  320/321 Table T6 (Wayback copy; row iodp:gpts2004): C1n base 0.781,
  Jaramillo 0.988-1.072, C2An.1n 2.581, C5n.1n 9.779, C5n.2n base 11.040;
  gpts_stripes.py rewritten (25 normal intervals, TMAX 11.040), figure axes
  +-110.4/+-441.6; problem Part II profile re-invented (C1n 9.7/10.1 km, C2An
  26.8/27.3 km) so corrected rates agree within 0.1; ch. 13 Red Sea profile
  C2An edge now 21.0/20.2 km. History box from bullard:fit (Crossref
  abstract), wilson:transform, mckenzie:sphere (Nature pages), morgan:blocks,
  lepichon:spreading (Crossref titles). Triple junctions: mckenzie:triple-
  junctions + FFF instability derived in text. Azores: morvel:azores (row
  extended) + data:pb2002 junction point. Iceland: spaans:iceland-gia.
- **Ch. 13 DONE (2026-10-23).** wright:afar, hofmann:traps, bastow:afar,
  roberts:ear, dick:ultraslow, michael:gakkel, kelley:lost-city, white:crust,
  christeson:crust, parsons:plate-model (own source key PS-1977-B3, same PDF
  as Book 2's PARSONS-SCLATER-1977). New figdata `ridge_budget.py` (+4 tests in
  test_rifts_ridges.py): PB2002 spreading steps give 3.0 km2/yr of new floor
  (21 km3 with 7.1 km), Charlie-Gibbs offset 356 km, Azores junction
  39.40 N 29.77 W all-OSR. depth_age.py values: c_book 392.9 replaces the
  wiki-based c_atlantic/c_pacific. Afar rate now MORVEL AR-NB at Dabbahu,
  18.5 mm/yr (ex. 1: 444 yr).
- EXCLUDED so far, ch. 9-13 (text no longer states): Mohorovicic "rounded to
  fifty", 39 km SE, 300/700 km; Moho 5-10/20-90 km ranges; inner-core 3 %
  deficit; T&S isotope heats; 140 km old-ocean lithosphere; 40-280 km
  continental lithosphere; Alps -150 mGal; 80/40 km crust; deflections <10"
  and 1'; Vening Meinesz 1929/1948 "same gravity at sea"; Bruns/Stokes 1849;
  GOCE 255 km; "183 reversals in 83 Myr", "one every 450000 years"; Morgan
  "twelve plates", Le Pichon "six plates", the 1965 London symposium;
  McKenzie-Morgan "16 kinds, 14 stable"; Iceland GIA 30 mm/yr, rifting-rate
  variation; EAR 4000 km, onset 22-25 Ma (now ~25), 33 Ma traps (now ~30);
  half-graben 50-150 km / 10 km; P-wave 7.0 and 7.1-7.8 km/s at margins; slow
  40 / fast 90 alternative limits; axis 2600 m / 2000 m (now PS77 2500 m and
  6400 - 2500); Gakkel 1800 km, <1 cm/yr, 3-29 E; core complexes 10-150 km,
  500-4000 m; Atlantis summit 700 m; layer thicknesses 0.4/0.5/1.5/5 km, 7 +- 1
  (now White 7.1 +- 0.8, Christeson 6.15/1.84); slow-ridge crust 4-5 km;
  pillows "up to a metre"; dykes "cm to m"; production 2.7 km2 / 19 km3 (now
  PB2002 3.0 / 21); Charlie-Gibbs ">2000 km long"; T1 1220/1120 C and C 390/350
  by ocean; old-floor heat flow 1e-6 cal (ex. 7 reworded).
- **Ch. 14 DONE (2026-10-23).** stern:subduction (55,000 km of convergent
  margins), usgs:okhotsk-2013 (Mww 8.3, 598.1 km, felt in Moscow; the 6400 km
  is a computed great-circle distance), usgs:deepest (735.8 km, Vanuatu 2004),
  jma:warning, syracuse:arc-depth (72-173 km, avg 105), wada:decoupling,
  clift:erosion (erosion > 6 cm/yr and < 1 km sediment), brudzinski:double,
  frank:arcs, forsyth:forces, karig:marginal-basins (titles), nasa:sarychev;
  Book 2's usgs:tohoku cited read-only (own duplicate dropped). New dataset
  `bachelor-1-grav-kuril` (Scripps gravity + topography, Book 3 block of
  fetch_data.py, ledger data:b3-grav-kuril) and figdata `trench_gravity.py`
  (Kuril free-air profile: rise +38 at -155 km, low -260 at the trench, high
  +218 at 160 km; trench 5226 -> 8698 m, relief 3.5 km), 2 tests in
  test_slab_seismicity.py. The gravity panel of the gravity/heat figure now
  plots the real profile (FIGCHECK p. 162 at 130 dpi: labels shortened to "free
  air"/"heat" after the two y labels collided; science OK). ridge_budget.py
  gained subduction_consumption (2.74 km2/yr over 51,471 km), backarc_rates
  (Mariana 18 N 32.4, Lau max 117.5 mm/yr), area_balance (3.511 made vs 3.519
  destroyed over all classes), +3 tests. Exercises 1, 4, 9 rewritten; problem
  Q12 (old floor 43 by the ch. 13 law), Q14 (h for -260 = 3.6 km), Q15
  (whole-plate slab 2300 kg/m3 -> 338 mGal), Q18/22-24 now 105 km: named
  number **162 km** (was 176).
- EXCLUDED ch. 14 (text no longer states): Tohoku 2.4 m / 0.6 m over 400 km /
  7 m uplift / 50 m ESE seabed; Challenger Deep 10935 +- 6 m; trench widths
  50-100 km and depth 3-4 km (replaced by Kuril data); slopes 8-20 / 5 deg;
  50,000 km of trenches; outer rise 20 km, twenty quakes a year, elastic
  thickness 20-30 km; gravity +50/-200 "relative to isostasy" (replaced by
  real free-air data); forearc 30-40 mW/m2 (now an exercise value 35);
  old-floor 42 (now computed 43); 300 km plastic limit; Honshu double zone
  30-40 km; Okhotsk 609 km and 7400 km (Wikipedia errors); "Forsyth and Uyeda
  found slab pull the strongest" (only the title fetched; now Stern's "excess
  density provides most of the power"); slab at 120 km, arc belt 50-200 km;
  trench-arc 200 km; Sarychev plume 12-18 km and "covers almost all of Matua";
  arc crust 80 km / 20-35 km; Karig "1970"; rollback 2-4 cm/yr; back-arc
  conditions 55 Myr / 30 deg; Mariana 1300 km / 240 km / half-rates 1.5-2.2;
  Lau 15 cm/yr and "< 5 Myr"; Japan basement "most of" accreted rocks.
- **Ch. 15 DONE (2026-10-23).** Hotspot dataset REBUILT from the primary table
  (coordinator ruling 3): `bachelor-1-hotspots` now fetches Table 1 of the
  Morgan & Morgan (2007) electronic supplement (Internet Archive copy of the
  mantleplumes.org PDF, whose TLS chain is incomplete) and parses it with
  pdftotext; new columns `quality` (A/B letters, w empty) and `az_model`,
  `rate_model`; 71 rows, 68 hotspots (Samoa listed twice in the table, at
  169.1 W and 168.2 W: the supplement's entry 168.2 W kept). Wikipedia's list
  had added C-quality features (Jan Mayen, Bouvet, Socorro, Anahim) the authors
  exclude. hotspots.py values now: 15 Pacific tracks, 13 rated, pole 63.78 S
  112.48 E, omega 0.9206, chi2 38.8, Hawaii 108.0 deg / 298 / 97.4 mm/yr;
  test_hotspots.py updated (71 rows, Samoa once, N.Austral letter, Iceland
  two plates; 8 pass). New sources: MM-2007-SUPP, USGS PP 1801 ch. 3 and 5
  (Hawaii volumes and supply), USGS FS 2005-3024 (Yellowstone), Henry 2017
  (McDermitt), Pierce & Morgan 1990 (track rates), Courtillot & Renne 2003
  (LIP table, open archive of the Academie), Bryan & Ernst 2008 (LIP
  definition, QUT ePrint), Schulte 2010, Tarduno 2003, Sharp & Clague 2006,
  Wei 2020 (eScholarship), French & Romanowicz 2015, Wolfe 2009, Herzberg 2007,
  Foulger & Natland 2003, Von Herzen 1989, Crossref classics (Dietz-Menard,
  Wilson, Morgan, Whitehead-Luther); OpenAlex abstracts via scratch
  `tools/oa.py`, Crossref via `tools/cr.py`. LIP table rebuilt from Courtillot
  & Renne Table 1. cp from Book 2's delaney86:properties (read-only). Exercises
  1, 2, 3, 4 (dT now 250 K), 8 (Pierce-Morgan 350 km / 5.8 Myr = 60 mm/yr), 9,
  10, 11 (40 mm/yr drift -> 1360 km, 118.4 mm/yr, 346.6 deg) and problem
  Q11 (9.5 deg, 15 %), Q18-20 rewritten; named number unchanged (8.5 cm/yr).
  FIGCHECK pp. 175 (rates), 176 (map), 179 (table) at 130 dpi: OK.
- EXCLUDED ch. 15: Kilauea 3.5 km3 by 2011 and the 2018 end; hotspot counts
  "20 to several thousand" and primary/secondary list; "early 1970s" tank
  date (now 1975 paper); models "several Myr"; Hawaiian magma 1500 vs MORB
  1325 degC (now Herzberg 1280-1400 + 200-300); Hawaii tomography 500-600 km
  / 2000 km; French-Romanowicz 273 events, 400 degC, 600-800 km, 2900 km, the
  hotspot list; Anderson/Hamilton names, Galapagos no age progression,
  Hawaii-Iceland relative motion; 64 hotspots (now 68); Island Park 80x65 km
  and 2500 km3 (now USGS 2,438 km3, >100 km); 631 ka (now USGS 640 ka);
  McDermitt coordinates and 16.4 vs 0.63 Myr exercise; stretched "since
  17 Ma"; swell heat 10 mW/m2 (now 5-10 or none); 3 MJ/m3/K "most solids";
  Hawaii 750000 km3 / 85 Myr / 0.009, 0.01, 0.095, 0.21 km3/yr; Mauna Loa
  65000-80000 (now 74000); Mauna Kea 10203 m; ridges 19 km3 (now 21);
  bend 60 deg, 40-50 Myr section, Emperor 81-45, Meiji 85 Ma, 800 km drift
  (now Tarduno > 40 mm/yr 81-47 Ma, Sharp-Clague 50 Ma, Wei Meiji > 81 Ma);
  LIP table values of the Wikipedia list (replaced); Deccan 17-24 N, > 2 km,
  1.5 Mkm2, 66-65 Ma; Ontong Java 1 % of Earth, 80 Mkm3, 22 km3/yr, 25/36 km,
  "largest event of 200 Myr"; CAMP 11 Mkm2 (now up to 7); Siberian 251.9 Ma
  and 2 Myr; "trap" Swedish etymology; North Atlantic-Iceland, Kerguelen and
  Ontong Java-Louisville pairs.
- **Ch. 16 DONE (2026-10-23).** New sources: USGS-COMCAT-OK (FDSN count and
  CSV queries, box 33.6-37.0 N, 94.4-103.0 W, M >= 3 per year; Prague
  usp000jadn is Mww 5.7, NOT 5.8; Pawnee us10006jxs Mww 5.8),
  HSIEH-BREDEHOEFT-1981 (Denver reservoir 3.7-7.0 km, 32 bar critical
  build-up; OpenAlex abstract), KERANEN-2014 (Crossref: four wells, 20 %,
  > 30 km). Rows usgs:oklahoma-rate, usgs:prague-pawnee, hb81:denver,
  keranen:oklahoma. Opening rewritten (1960s Denver, Oklahoma counts 1-5 /
  20 / 585 / 888), Mohr history reduced to the name, Bingham etymology cut,
  Coulomb paragraph now cites Byerlee (mu 0.6-0.85, 31-40 deg), induced
  paragraph cites Denver's 3.2 MPa, Moho 35 km = prem:moho-average (also in
  the strength_envelope.py and refraction.py docstrings), BDT published
  estimates cut, seismogenic paragraph rebuilt on jackson:jelly (600-800 degC,
  vs the model's 641) + usgs:deepest. Exercise 4 values (10 MPa, 30 deg) are
  exercise values. No solution or problem number changed. Build 0/0/0,
  148 tests pass.
- EXCLUDED ch. 16: Rocky Mountain Arsenal 1961, 3671 m, February 1966, "the
  army"; Oklahoma "one or two a day" (now the ComCat counts); Prague "5.8"
  (catalogue 5.7); Culmann; Bingham/Reiner 1920 and panta rhei; Coulomb 1776
  essay; cohesion 10 MPa / 30 deg rock / 20 deg clay "tables"; BDT near 20 km,
  250-400 degC, 10-20 / 20-30 km; seismogenic 40 km oceanic / 25 km
  continental.
- Wiki-hits after ch. 16: 114; refined landing count 73.
- **Ch. 17 DONE (2026-10-23).** Main new source: the open textbook of Waldron
  & Snyder (2020, Open Education Alberta, CC BY-NC, doi:10.29173/oer3), one
  source key per Pressbooks chapter (WS-ORIENTATION, WS-FOLDS, WS-FABRICS,
  WS-DYNAMIC, WS-FAULTS, WS-FAULT-ENV, WS-SHEAR-ZONES; fetched HTML in scratch
  `src/struct/`); plus USGS-EHP-GLOSSARY-B3 (own key, same URL as Book 2's),
  AKI-RICHARDS-UO (signed-rake convention quoted from Aki & Richards p. 106),
  ANDERSON-1905 (Crossref), HEALY-2012 (OpenAlex abstract), SIBSON-1977 and
  SIBSON-1981 (Crossref abstracts). Rows ws:rake, ar:rake, usgs:fault-types,
  ws:fault-terms, ws:fault-rocks, sibson:fault-rocks, sibson:alpine-fault,
  ws:anderson, anderson:1905, healy:anderson, ws:fold-elements,
  ws:fold-classes, ws:fabrics, ws:vergence, ws:microstructures.
  **Fold tightness classes CHANGED** to the scheme of the source (Davis et al.
  via W&S): gentle 180-170, open 170-90, tight 90-10, isoclinal 10-0; the
  "close fold" class is gone (DEFINITIONS row updated); axial-plane classes now
  quantitative (upright > 80, recumbent < 10). Solutions: ex3(b) 35 deg tight,
  ex8(d) tight folds, problem Q4 and Q9 "open" (155.9 deg). Figure row 1 is
  now 174/120/50/0 (FIGCHECK updated, p. 193). Fault rocks: breccia down to
  about 2 mm, cataclasite sand size, gouge clay-rich; mylonites below the
  frictional/plastic transition at 10-15 km (Sibson, vs the 13.7 km of ch.
  16's envelope). Rake definition now says it is the seismologists'
  convention and gives the field geologists' 0-180 one. Thrust: dip 45 deg
  or less (USGS).
- EXCLUDED ch. 17: Anderson 1877-1960, Survey 1903, war service, book year
  1951; breccia "> 2 mm at least 30 %"; gouge/cataclasite cohesion criterion;
  mylonite "no less than 4 km"; slickenside "polished"; slaty cleavage spacing
  0.01 mm and roofing; "most normal faults dip 60 or more"; undulose
  extinction "so common it helps recognise quartz"; stylolites; Fleuty
  tightness limits and the close class; Stille 1924 (was not printed).
- Wiki-hits after ch. 17: 91; refined landing count 50.
- **Ch. 18 DONE (2026-10-23).** New sources: USGS-MAGTYPES (Mw constant 9.1
  for N m; Ms_20 saturates near 8.3, mb near 6.5), USGS-COMCAT-HIST (1906 Mw
  7.9, Chile 1960 9.5, Alaska 1964 9.2, Parkfield 2004 5.97), KANAMORI-1977
  (saturation for ruptures above the 5-50 km wavelengths; W0 = M0/2e4; Chile
  Mw 9.5), HANKS-KANAMORI-1979 (2/3 log M0 - 10.7 dyne-cm -> 9.05 N m),
  REID-1910 (Internet Archive full text of vol. 2: 3.2 m since the 1851-1865
  surveys, a little more than half the ~6 m slip, half built 50 yr before),
  BAKUN-LINDH-1985, BAKUN-2005, USGS-YVO-BEACHBALL (focal mechanisms), GR-1944,
  FROHLICH-DAVIS-1993 (global b 0.72-1.34, 30 % scatter), MASSONNET-1993
  (InSAR, 100 m pixels), ATWATER-1987 (buried marshes, tsunami sands); more
  rows from USGS-PP1515 (ch. 5 and 6: 1906 rupture 430 km, Parkfield five M6
  at ~22 yr since 1881 over 30 km, central creeping section, Pallett Creek
  12 earthquakes, most slip with M >= 6) and from the existing Tohoku/Sumatra
  event JSONs (general-text: 83 mm/yr, 400 x 150 km, up to 50-60 m slip;
  Sumatra aftershock zone > 1300 km). CHANGED numbers: Tohoku average slip
  now 31 m (400 x 150 km), ex6 now 31.1 m / 374 / 468 / 749 yr at 83 mm/yr
  (the "260-880 yr" comparison dropped); 1906 rupture 430 km (was 476/470):
  text M0 7.7e20, ex5 7.74e20 / 7.86 / 7.74; Chile/Alaska Mw 9.5/9.2 (were
  9.6/9.3). Scratch calc/ch18.py "Sync 2" section. Sync 3 item: the
  projections of the sphere are studied in the Year~3 volume (was Year~2,
  l. 475). Book 3 defines no cosmogenic nuclide / shear zone / standard
  candle (checked); wiki:microstructures and wiki:insar rows are gone
  (ws:microstructures, massonnet:1993 replace them).
- EXCLUDED ch. 18: Reid's biography (1859-1944, platinum, Alaska glaciers
  1890/1892, USGS 1902, "only non-Californian"); Parkfield intervals 12-32 yr
  and "six"; Tohoku locking 0.5-0.8 and 260-880 yr; JMA 500 x 200 km;
  Pacific 85 mm/yr (now USGS 83); Ms 8.5 / 8.4 for Chile / Alaska and "the
  reference scale of the 1970s"; 1906 476 km (Wikipedia; PP 1515 has 430);
  GR "whole world in 1949"; b range 0.5-2; Sumatra "one-eighth of the moment
  1906-2005, almost half with Chile and Alaska"; trench colluvial wedge;
  "a few large earthquakes account for nearly all the movement" (now PP 1515:
  most historical slip with M >= 6); InSAR "to millimetres, over days to
  years", interseismic and postseismic maps.
- Ch. 19 DONE (2026-10-23): sources USGS water density (0.99987 g/cm3 at
  0 degC), IAPWS R10-06 ice Ih (916.721 kg/m3; the `.download` URL, the `.pdf`
  one serves HTML), WALDER-HALLET-1985 (frost cracking most effective
  -4 to -15 degC, doubts sealed-crack wedging), FORMOSO 2006 (hydrolysis;
  surface/soil water pH 5.5-7, 3.5 in podzol organic layers; oxisols, rain
  > 2000 mm), GOLDICH-1938, LASAGA-1984 (rates confirm the series),
  BISCAYE-1965 (deep-sea clay detrital; kaolinite + gibbsite off tropical
  South America), CARROLL CEC (kaolinite 3-15, illite 10-40, montmorillonite
  70-100, vermiculite 100-150 meq/100 g), USGS OFR 01-041 settings pages,
  USGS Bulletin 1228 (bauxite: gibbsite/boehmite, residual, mostly tropical,
  90 % to aluminium), BUCHANAN-1807 (laterite, brick-stone), WHK-1981
  (negative feedback). CHANGED: ice expansion 9.1 % (was 9.2; 999.87/916.72
  = 1.0907), ex4(a) 10.91 cm3 (was 10.92), ex4(b) is now "which temperature
  range and why" (was 14/4 = 3.5); CEC column 3-15 / 10-40 / 70-100 / -- for
  chlorite (was 3/25/85/40); clay settings column rewritten; ex12 orders by
  leaching intensity (was "driest or coolest" climate); history box laterite
  only, retitled "A word from the field". Net-weathering proof and the
  carbonate precipitation equation carry no ledger (derived). "Earth's
  thermostat" phrase dropped (now "a negative feedback").
- EXCLUDED ch. 19: frost pressures 200 MPa and 14 MPa, granite tensile
  strength 4 MPa, exfoliation stresses up to 35 MPa; rain pH 5.6 and soil CO2
  up to 30 %; temperate 500-1500 mm / 5-15 degC and equatorial 1000-10000 mm /
  20-30 degC ranges; Si/Al 2-2.4 (smectite) and 1.5 (illite) in the text;
  the illite-cooler / smectite-drier zoning (Biscaye's abstract does not
  support it); grain lifetimes 10^5.6 / 10^8.5 / 10^8.6 yr and the
  K-feldspar-plagioclase similar-rate claim; chlorite CEC 40 and the
  Na-swelling claim; "thickest on old, stable surfaces"; the Latin
  etymology of laterite; d'Entrecolles 1712 / Jingdezhen / Gaoling (kaolin).
- Wiki-hits after ch. 19: 41 (all Commons photo provenance); **refined
  landing count 0** (2026-10-23). check_ledger OK (1391 rows), 148 tests,
  gates OK, build 0/0/0.
- Wiki-hits after ch. 18: 64; refined landing count 23 (all ch. 19).
- Wiki-hits after ch. 15: 130; coordinator's refined landing count 89.
- Wiki-hits after ch. 14: 176 (was 224 after ch. 13) (`bash $S/tools/cleanup.sh` prints them; it
  deletes unused wiki rows, then orphan WIKI sources). More helpers: `inv.py`
  (id -> key -> using files), `get.sh DIR NAME URL` (fetch + text), `ctx.py
  FILE WIDTH regex`. Crossref API (`api.crossref.org/works/<doi>`, and
  `works?query.bibliographic=`) gives titles, dates and often abstracts; Nature
  article pages give abstracts; Europe PMC REST gives open full texts;
  topex.ucsd.edu/geodynamics hosts Parsons-Sclater 1977, Stein-Stein 1992,
  MORVEL. Blocked: Wiley/AGU and OUP (GJI) landing pages.

### Ch. 19 traps (2026-10-23)

- `tools/chem.py` cannot read decimal subscripts (`Na_{0.5}`, `Si3.5`): the
  albite-to-beidellite equation carries `% ce-unbalanced-ok` on its line and
  its balance is tested in `tests/bachelor-1/test_weathering_clays.py`.
- pgfplots `xticklabels` with `$\to$` inside fails ("Missing control sequence");
  plain text with `\\` inside braces and `align=center` works.
- Two `[t]` minipages (text + photo) after `\par\noindent` overprinted the next
  paragraph by the photo caption's depth; wrapping the pair in `omfigure`
  ([b] box) fixes it. Non-floating figures left 1/4-page gaps: fixed by moving
  the paragraph that follows a figure in front of it.
- `nodes near coords` labels with `inner sep=1.5pt` sat on 1.6 pt marks: 2.6 pt.
- Shannon table rows with a spin state shift the charge column in a naive
  parser: radii were read from the printed rows (Fe2+ HS 0.78, Fe3+ HS 0.645,
  Mn2+ HS 0.83).
- Brief's upper ionic-potential boundary "12" is unsupported: sources give 10
  (Si on it). "Urey reactions" naming unsourced, not printed. Wikipedia "Clay
  mineral" labels 7/10/14 basal spacings as nm (they are angstrom).
  pubs.usgs.gov returned 502 for OFR 01-041: Internet Archive copy used.

### Ch. 18 traps (2026-10-23)

- `beachballs.py`: a horizon point with a tiny positive vertical component
  (rounding) was flipped to the antipode and broke the polygons; `project()`
  now flips only if z > EPS (1e-9) and uses min(z, 0). A low-dip thrust's
  compressional lune may touch the horizon only at points: `_horizon_arc`
  returns [] when no arc midpoint is inside, and the degenerate region is
  dropped (`reverse-c2` is a header-only file, not plotted).
- pgfplots has no `text mark style={font=...}` here: letters at P and T use
  `nodes near coords={\textbf{P}}` + `every node near coord/.append style`.
- `\qty{500 x 200}{km}` errors: use `\qtyproduct{500 x 200}{km}`.
- USGS PP1515 credits "Savage and Burford (1970)" and labels a 0.8 urad/yr
  strain rate inconsistently (engineering vs tensor): not quoted. Wikipedia's
  Tohoku radiated energy (1.9e17 J) disagrees with Kanamori's M0/2e4: no
  Tohoku energy quoted. USGS Sumatra headline Mw 9.1 vs its W-phase M0
  6.68e22 (Mw 9.15, Mww 9.2): the text uses the catalogue value 9.1. All Phase D notes.
- The first AI seismic-analysis image had no moveout across the traces:
  regenerated as `b1-seismic-analysis.jpg`; look for physically plausible
  arrival order in any AI seismogram.

### Ch. 17 traps (2026-10-23)
- In the oblique TikZ frame (x, y, z vectors), a polar coordinate `(a:r)` is
  taken in the x--y plane, i.e. along the receding axis: draw arcs in the front
  plane as explicit `plot (r cos t, 0, r sin t)`.
- Cleavage--bedding "vergence points to the anticline" is FALSE on an
  overturned straight limb (the hinge at its top lies on the other side);
  proved instead: (a) same dip direction, bedding steeper <=> overturned;
  (b) the rotation sense reverses across every hinge, and points to the
  anticline only on right-way-up limbs. A sheared-sine figure was only locally
  overturned and hid this: replaced by exact chevrons (gamma 60, iota 40), the
  same geometry as exercise 11.
- Conjugate strike-slip senses: sigma1 lies 30 deg CLOCKWISE of the strike of
  the dextral fault (wedge argument; a traction sign slip gave the opposite).
- Fleuty's axial-plane dip classes have no open primary source: upright /
  inclined / recumbent defined qualitatively; tightness limits from Wikipedia.
- Anderson's employer/biography: say "Geological Survey", never his
  university (printed text never names a university).

