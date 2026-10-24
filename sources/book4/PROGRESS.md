# PROGRESS --- Book 4 (University Year 2, `bachelor-2`, prefix `b2`)

Resumable state of the Book 4 agent. Read this file, then `BRIEFS.md` and
`DEFINITIONS.md` in this directory, then `sources/BATCH_BOOKS_1-5.md`
(binding), before doing anything.

## State

- **2026-10-23 Phase A done.** `BRIEFS.md` (31 briefs + homograph table),
  `DEFINITIONS.md` (439 planned term rows, contested cases, recall table,
  forward owners), this file. Entry file rebuilt: 0 errors / 0 undefined /
  0 overfull, 43 pp (placeholders); `bash tools/gates.sh bachelor-2` OK.
  Phase A report returned to the main session.
- **2026-10-23 Sync 2 received** (batch file "Sync 2" section, binding):
  contested terms granted as planned; ice--albedo feedback moved to ch. 18;
  DEM is Book 3's; lith styles migmatite, marble, quartzite, serpentinite,
  tuff, rhyolite, andesite, chert, banded iron, reef limestone appended;
  skew-T stays local (axis option); the SHARED `tools/ai_images.py` has no
  fallback any more: use it (not a private copy); **NO Wikipedia/Wikibooks
  ledger rows, ever** (landing check greps the ledger for "wiki"); do not use
  Book 3's hotspot table until it is re-sourced (or derive from Morgan &
  Morgan 2007). Phase B started. Nothing written in `parts/bachelor-2/`,
  `figdata/`, `tests/`, `images/book4/`, `sources/ledger/book4.md` or
  `tools/` yet.
- Sync rulings applied to `DEFINITIONS.md`/`BRIEFS.md`.
- **Ch. 1, 2 and 3 done** (see table). Ch. 3 traps: GERM pages give the UCC majors as oxide values labelled as elements, and core Co in ppm (should be wt %): defects to report; Wiley (Gale 2013) 403 -> Harvard DASH copy; McDonough & Sun 1995 PDF 404 -> GERM; Lodders 2021 Springer cookie-walled -> Lodders 2003; KdD app JS-only -> Budahn 1991 USGS OFR. Lodders 2003 now cited from the paper
  itself (doi 10.1086/375492, full text via the ADS PUB_PDF gateway).
  Bot-walled: A&A (Neumann 2012) and the Meteoritical Bulletin site (Cloudflare);
  used Gail et al. 2014 (arXiv) and the NASA legacy meteorite CSV instead.
  Defects to report: NASA Dawn page gives Vesta departure "Sept. 5, 2017"
  (should be 2012); Book 2/3 ledgers hold wiki rows; check_ledger shows 25
  problems in Book 2's files (dye12 rows).
- **2026-10-23 coordinator notices:** (1) `figdata/shared/region.py`
  `contact_elevation(name, x, y)` now returns nan in the gap cut out by the
  normal fault: handle nan whenever Book 4 calls it (not used yet). (2) Landing
  check: `grep -iE 'wikipedia|wikibooks|\| *WIKI|wiki:' sources/ledger/book4.md |
  grep -viE 'commons\.wikimedia|wikimedia commons' | wc -l` must be 0 (it is 0).
- **2026-10-23 coordinator Sync 3 (Book 5) items:** (1) Walther's law is owned by Y3 ch. 17 `facies-models` (theorem): ch. 20 `palaeoenvironments` uses it in prose with a pointer to the Year 3 volume, NO definition, NO `\index` under that name. (2) `styles/oneearth.sty` appended `% Sync 3 (Book 5)` block: groupplots loaded; `\Msun \Mearth \Rearth \Mjup \Rjup \dex \darcy` available. (3) Book 5 recalls AFC, geobarometer, Clapeyron slope, Rossby wave, ice-albedo feedback, ERF/ECS/TCR and the other Sync 2 terms: keep their labels stable (as in DEFINITIONS.md).
- **Ch. 4 done.** Traps: Wiley/AGU (Stracke 2005) 403, Bouvier 2008 closed, degruyter (Villa 2022, Brand 2014) returns 202 with an empty body, Caltech JW80 restricted -> White's open textbook chapters (imwa.info), Villa 2020 author copy, Kendall & Caldwell 1998 (USGS), Stracke 2022 GRO.data table, Edwards 2019 and Dhuime 2018 via NSF-PAR / PMC. White's draft eq. 9.02 inverts the SMOW/PDB conversion (external defect): VPDB on VSMOW derived from KC98 absolute ratios instead. A 'C3 range' row once misread a fractionation as a delta value: removed.
- **Ch. 5 done.** Traps: siunitx rejects `\qty{e10.9}` (fatal 'Invalid number'): write `$10^{10.9}$\,\unit{Pa.s}`; the GRD model needs the anhydrous oxides renormalised to 100 - H2O before mol % (the authors' worked example then reproduces B 7720, C 334, log 3.67); `\num{..}{s}` prints an italic s, use `\qty`; AJS (Delaney 1986) and the GRD journal version are closed, author copies / the GRD tutorial are open; Tulane notes cited read-only, not re-sourced; Shiprock dykes not stated as basaltic in any accepted source, so the caption says only 'dyke'. Stefan problem uses dt = 1050 K (Tm 1150, T0 100).
- **Ch. 6 done.** Traps: pdflatex has no U+02BB okina (fatal): write Pu`u~`\=O`\=o; ledger tool refused id usgs:pinatubo-1991 (Book 1 owns it): mine is usgs:pinatubo-deposits with only the extra facts, Book 1 rows cited read-only; the NPS VEI table is JS-loaded (empty fetch): the USGS VEI criteria image (PD) viewed directly; the Mastin 2009 JVGR PDF is 404: fits from Aubry 2023 (CC BY), examples from USGS OFR 2009-1133 Table 2, whose text layer drops superscripts (1105 = 1x10^5); USGS MSH 1980 / alert-level / tephra pages 404: MSH FAQ, volcanic-ash site and HVO Volcano Watch used; USGS sources disagree on the MSH landslide (2.3 vs 2.8 km3) and duration (8 vs 9 h), Book 1 uses 2.8; nodes near coords labels collide on a crowded log-log plot: label by hand. Solution 6c recomputed from the printed k = 0.139 (38 %, not 39 %).
- **Ch. 7 done.** Traps: Katz et al. 2003 via the Harvard DASH DSpace 7 API (pid/find?id=hdl:1/<handle> -> item -> bundles -> ORIGINAL bitstream content); pdftotext dropped the minus signs of Katz's coefficients (A3 -5.1, B3 -3.2, C3 -2.0 checked on a rendered page); Workman & Hart 2005 closed -> DMM mode from Liang et al. 2021 (NSF-PAR); BGS RR 99-06 does not number the 5 % strips; `photo.py` takes a bare output name; Katz model gives 9.0 km of crust at Tp 1350 (7.1 observed), so the problem inverts the crust to Tp = 1315 degC (named number changed from the brief's crust thickness); solution values re-derived from the rounded P0 (Q21/Q22: 1373.1, 1440 degC, excess 125).
- **Ch. 8 done.** Traps: Wilcox 1954 OCR shifted table rows: every value re-read from page images at 200-220 dpi; Bowen 1913 OCR garbled: summary table read from archive.org page image n617; Hart & Davis 1978 (EarthRef) and the Matzen thesis unreachable -> Matzen EMC2012 abstract for D_Ni; Geologinen Seura PDF site down; Tegner 2023 GEUS Dataverse xlsx read with a stdlib zip/XML reader (`_b4_xlsx_rows` in fetch_data.py, no openpyxl), derive must break on the next heading row (`a and not r.get("B")`), drill-core sample names are not digits; round(x,4)+0.0 to avoid "-0.0000"; Commons 'Plagioklas1' shows twinning not zoning -> zoning figure computed instead; `\foreach` with `\x` or a colour variable inside a pgfplots axis fails (undefined \x / colours lost at visualization): write explicit addplots; a non-floating omfigure right after a short definition left half a page blank: move it below the next block; `render.sh` takes a bare dir name (an absolute path nests it); siunitx `\qty{2043 \pm 11}{Ma}` prints 2043(11): use `separate-uncertainty=true`; 'Wilcox concluded convection' is NOT in the source: the heat argument is printed as the book's own inference.
- **Ch. 9 done.** Traps: OUP (Le Bas 1986) 403 -> TAS vertices from BGS RR 99-06 Fig. 20b page images, cross-checked with GeoplotR's polygons; Vermeesch & Pease 2021 regression reproduced exactly (test); GeoplotR data files are GPL-3 (factual data; flag in report); usgs.gov needs `www.`; a magnetite mass balance on an FeOT basis gave sums > 100 % (abandoned); Ti-Zr-Y field letters: compute polygon centroids before placing labels; a TAS `\foreach` field list silently omitted F; unsourced interpretive claims (arc K-h zoning, crustal-melt rhyolites, LIP = tholeiitic, classification trees 'do better') cut or turned into stated inference.
- **Ch. 10 done.** Traps: booktabs is NOT loaded (`\toprule` fatal): use `\hline`, then delete the entry's .aux/.toc/.out/.fdb_latexmk as single files; opengeology.org is behind an Anubis bot wall (respected, not used); BGS SCMR metamorphic papers 404 (also on Wayback): the SCMR recommendations cited from the Granada mirror (Spanish translation of the English original, flagged); science.smith.edu SSL error; check_ledger resolves source keys per file: HM-1993-AMMIN added to book4.md although Book 2 already lists it; ΔG plot at 4 kbar showed an andalusite window (below the method-B triple point 4.20 kbar): 6 kbar; ch. 11 terms kept out (no 'facies series', prograde/retrograde not emphasised; ex. 12(c) reworded); solutions recomputed from the rounded printed data with the 1 of P-1 neglected (786.92 K, 3880 / 3882 bar; 4885/5782/1799 bar).
- **Ch. 11 done.** Traps: the Ferry & Spear (1978) paper is closed, but Holdaway et al. 1997 (MSA free) tabulates its 12 brackets (Table 1, minus signs OCR'd as '2': read the page image) and the ideal dH/dS (Table 2) -> refit reproduces 52635/20.20 (test); science.smith.edu has a broken certificate chain (curl and WebFetch both fail; not bypassed); Holdaway 2000 AmMin is not in the MSA free archive (404); GASP from Koziol & Newton 1988 (eq. 5a, dV -6.210 J/bar, appendix B); closure temperature of muscovite from the Harrison 2009 abstract on the ANU portal; Chopin 1984 / Sobolev & Shatsky 1990 publisher abstracts; paired belts: Elements 2024 summary + JpGU 2017 abstract + FU Berlin teaching page (whose 'high-pressure/high-temperature' continental-side wording is a slip: noted in the row); author first names not in a source were dropped ('Christian' Chopin); pgfplots legend colours look black at 130 dpi but are right (check at 300 dpi); the thickening model's base-of-crust temperature must be read in material coordinates (909 C, not the 969 C of the 70-km present depth); `photo.py` prefixes 'b2' to the section field (fix CREDITS rows by hand); a hot gradient starts in the kyanite field below ~280 C (caption wording); ledger author lists checked against Crossref.
- **Projection after ch. 8 (2026-10-23):** course text pp. 2-106 for 8 chapters = 13.1 pp/ch, solutions ~2.4 pp/ch -> ~15.5 pp/ch, projected ~31 x 15.5 + ~15 = ~495 pp against the ~370 target (+34 %, OVER, not under: no depth restoration needed; aim later chapters at ~12-13 pp of course text without thinning exercises).
- **Ch. 12 done.** Traps: no open source gives a muscovite/biotite dehydration-melting curve: the figure shows the published brackets as boxes (PD&H 1998, Berger & Kalt 1999, Skjerlie & Johnston 1996, all via OpenAlex abstracts; OUP 403) and the wet solidus as the published points (Stern & Wyllie 1981 via OpenAlex, Boettcher & Wyllie 1968 Caltech record); water solubility from Holtz 1995 (MSA free, Table 3 read on the page image); USGS G-2/GSP-2 sheets not on usgs.gov (403/404), Yukon copy 403, GSJ gbank under maintenance, IAG GMN-1 (ORO) 403, MDPI 403 to scripts: Shand diagram uses BHVO-2, AGV-2 (usgs.gov sheet) and NIST SRM 278 obsidian (scanned certificate, page images); Frost 2001's ASI formula mixes cation and oxide notation (Ca - 1.67P): the book defines A/CNK as Shand's molar oxide ratio (Moyen 2017) and only says Frost corrects for phosphorus; OpenAlex gave Pickering & Johnston's second author as 'David A.' and Skjerlie & Johnston's as 'Arthur': Crossref says D. A. and A. Dana: author lists from Crossref; pgfplots clip=false with path points outside the axis gave a 206 pt overfull box (restrict x to domain); unsourced segregation claims (boudin necks, shear bands, fold hinges, diatexite flow, 'type example', I-types mostly metaluminous, peralkaline A-types) replaced by Sawyer 2001, Rosenberg & Handy 2005 and Moyen 2017 statements.
- **Ch. 13 done.** Traps: `omfigure` is a NON-floating minipage without a counter, so `\label{fig:...}` + `\cref` prints the SECTION number: no figure/table labels, say 'the figure below/above'; TikZ `yshift=`/`xshift=` in cm are absolute, not in scope units (stacked panels overlapped, a two-panel figure went 103 pt overfull); a 9-11 cm non-floating figure after a paragraph near the page foot leaves half a page blank: move it before the preceding paragraph or flatten it; UNESCO whc.unesco.org 403 (not used); ICS epoch boundaries are not in the ledger, so the chapter gives no numerical epoch ages; Halama et al. 2020 abstract prints '2.8 +- 1.0 GPa' (the paper body has the tighter value; we quote 'about 2.8 GPa'); B of profile A-B (48 N, 8 E) is not on the Rhine; ETOPO1 Alps window and AlpArray Moho picks (Michailos 2023, Zenodo CC BY 4.0) fetched in the `# Book 4:` block. Unsourced claims removed or rewritten during the sourcing pass (Chenaillet location, first names, 'since the 1980s', a 250-Myr figure, '70 km' -> about a hundred km).
- **Ch. 14 done** (gates, calibration, numbering, 95 tests, check_ledger 1745 rows, wiki check 0). Traps: schematic sections drawn piece by piece left white gaps and floating blocks: redraw each section on ONE set of absolute shared vertices (MHT one polyline, slab one polygon); siunitx `\qty{a \pm b}` prints the compact 'a(b)' form: write `$a \pm \qty{b}{unit}$` (or `$(12.4 \pm 4.7) \times 10^{-9}$`); unsourced statements (370 kg/m3 'inferred', levelling, arc chemistry change, Puna->Altiplano lower-crust flow) removed during the sourcing pass; Altiplano photo has conflicting altitude metadata on Commons (no altitude printed); NNR-MORVEL India--Asia 72.5 mm/yr vs Gauthier's '5 cm/yr' (both cited as such).
- **Ch. 15 done** (same checks green, 0/0/0, 253 pp). Traps: lyellcollection.org 403, essopenarchive.org Cloudflare, sciencedirect.com PDFs 403 (all respected); OpenAlex free budget exhausted (a key needs an e-mail: not used) -> Crossref, HAL API, Europe PMC fullTextXML, ORA Oxford; a two-line pgfplots node anchored south near ymax is cut by the frame (one-line labels, raise ymax); Book 2 row ahnert70:decay ('with isostatic compensation at least 18.5 Myr' to 10 %) is inconsistent with Book 2's own model (tau 29.4 Myr -> ~68 Myr) and its 'about six times longer': report; Book 2 row usgs:alleghanian says the Iapetus closed in the Alleghanian collision (the Rheic, strictly): report; Nance 2022 spells 'Pangea', the book 'Pangaea' (figure data follow the book).
- **2026-10-23 coordinator notice (split):** a second Book 4 writer joins when Book 3 lands and takes the TAIL of the chapter list; the coordinator fixes the range from the chapter table below and messages it. From then on: do not touch that range's .tex/solutions/figdata/tests/images; DEFINITIONS.md is FROZEN (no label renames; any move/add logged under "Term changes after the split notice" below); shared per-book files (ledger book4.md, images/book4/CREDITS.md, FIGCHECK.md, PROGRESS.md) are append-only, small atomic edits, re-read before each write. Phases C and D stay mine after both ranges are written and the seam is reconciled.
- **Ch. 16 done** (0/0/0, 266 pp; gates, calibration, numbering, 100 tests, check_ledger, wiki 0). Traps: McKenzie 1978 (EPSL) has no open copy and no Crossref abstract: parameters from Sheplev & Reverdatto 1998 (Geophysica, open; Table 1) and the pyBacktrack code at a pinned commit (formulas, alpha 3.28e-5, kappa 1e-6, rho_w 1030), Crossref record only for the citation; the first-term thermal formula differs from the full series by a CONSTANT up to ~80 m after 10 Myr (higher terms reach their asymptote fast), so the text says 'less than 100 m', tested against the series and finite differences; sea-level term of backstripping is rho_m/(rho_m - rho_w) (pyBacktrack), equal to the brief's form; datapages.com archives behind Cloudflare (not used); the invented well was forward-designed from beta 1.5 (calc/ch16design.py) then rounded, so the problem's rounded chain gives 1441 m where the script gives 1442.1: the text prints the rounded-chain values; a lone section heading at a page foot before an unbreakable definition box: give the section a two-line opening paragraph.
- **Projection after ch. 16 (2026-10-23):** PDF 266 pp with 16 chapters written + 15 placeholders (~1 p each) + front/back matter. Written chapters 1-16 average ~(196 - 9 front - 0)/16 = ~11.7 pp of course text + ~2.4 pp of solutions = ~14 pp/ch; projected ~31 x 14 + ~15 = ~450 pp vs ~370 target (+22 %, OVER, falling from +34 % after ch. 8). No depth restoration; keep later chapters at ~11 pp of course text.
- **Ch. 17 done** (0/0/0, 278 pp; gates, calibration, numbering, 104 tests, check_ledger 1848 rows, wiki 0). Sources: Clague & Sherrod 2014 and Denlinger & Morgan 2014 (USGS PP 1801 ch. 3-4 PDFs, PD), ODP Leg 200 IR Nuuanu summary, Ladd & Schlanger 1960 (USGS PP 260-Y, Enewetak holes), NOAA Papahanaumokuakea pages (Kure, Darwin point), ICS chart.ttl (Eocene 56.00-33.9). Traps: there is no `lith breccia` style (fatal pgfkeys): use `lith conglomerate`; pgfplots ybar legend draws odd glyphs for bars + mark=- : drop the legend, say it in the caption; a marker placed at a plate age implies a claim (Hawaiian Ridge age): draw a horizontal 'measured' line instead; the two depth-age branches cross at 26.3 Myr (root < exp before, > after, within 20 m to 50 Myr): figures switch there, exercises use the root law to 70 Myr and only differences of the exponential beyond; Book 3 ch. 22 already describes fringing/barrier/atoll (no \index) with Darwin's history box and the Bora Bora photo, so ch. 17 recalls them and gives the indexed definitions in terms of the island underneath (SEAM ITEM for the coordinator: Book 3 prose + Book 4 owner definitions), uses the drilling history (Funafuti to Enewetak) instead of Darwin's, and Kure instead of Bora Bora; 'thermal subsidence' and 'lithospheric flexure' are Book 5 terms: prose only; volcano volumes of Robinson & Eakins: say 'estimated', not 'above the sea floor' (they include the flexural root); Mauna Loa row duplicated in Book 3 (pp1801:volumes) - mine is cs14:volumes from the PDF.
- **Ch. 18 done** (0/0/0, 292 pp; gates, calibration, numbering, pic scaling, 109 tests, check_ledger OK, wiki 0). Sources: Hoffman et al. 2017 (Sci Adv, Europe PMC full text: Cryogenian ages Table 1, hysteresis Fig. 1, 1981 '1 bar in 20 Myr' quote, CO2 threshold 0.01-0.1, history from its reference list), Cawood et al. 2018 (Phil Trans A: dome-and-keel, 3.2-2.5 Ga transition, cratons), Smithies et al. 2019 (TTG), Luo et al. 2016 (GOE 2.33 Ga), Lyons et al. 2021 (boring billion), Catling & Zahnle 2020 (Archean air, impacts), Pierru et al. 2022 + Asimow 2022 (komatiites), Sossi & O'Neill 2016 (ANU portal abstract: 1616 degC at 32.2 % MgO, 1450 at 23 %), Helz & Hearn 1998 USGS OFR 98-511 (glass thermometer: 0.15 % MgO = 3 degC), USGS VHP volcanic CO2 0.26 Gt/yr, ICS chart.ttl (eras, periods). Book 2 g12.06 ALREADY has 'radiogenic heat in the past' with per-isotope curves (prop:g12:internal-heat:past) and g12.08 the luminosity curve and an O2 chart: so no heat or O2 figure here; heat back in time is an exercise and problem Part I with BSE concentrations; the faint Sun is deepened with a 0-D energy-balance model (ice-albedo ramp 263-283 K stated as a model choice, eps fitted to 288 K) that gives tipping points 0.932/1.227 S0 and the hysteresis figure. Traps: x=-3.4cm reverses a TikZ timeline nicely (coordinates in Ga) but labels above bars in rows 0.6 cm apart collide: side labels, rows >= 0.65 cm; the siunitx `\qty{1350 \pm 50}` trap again (renders 1350(50)); strike-dip symbols placed by loop around touching ellipses land in neighbour domes: place by hand; a komatiite >18 % MgO definition needs a classification source I did not have: dropped the threshold; Commons descriptions (e.g. 'named after the Komati River') are not ledger sources: dropped the naming. Named number deviation logged in the table row. Term owners as DEFINITIONS.md, labels unchanged.
- **Ch. 19 done** (0/0/0, 306 pp; gates, calibration, numbering, pic scaling, 115 tests, check_ledger 1929 rows, wiki 0). Palaeogeography from real reconstructions: GPlates Web Service (gws.gplates.org) `reconstruct/coastlines` and `reconstruct_points` with MERDITH2021 (CC BY 4.0, Zenodo record cited) -- works without a key; Sydney is not in the model at 500 Ma (handled as absent). Sea level from Miller et al. 2005 NOAA files (Haq 1987 and Kominz 2008, GTS2012). Traps: a `\foreach` with `axis cs:\x` inside a pgfplots axis is fatal (undefined control sequence): wrap each command as `\edef\tmp{\noexpand\node[font=\noexpand\tiny] at (axis cs:\x,..) {\t};}\tmp`; a `ybar interval` plot needs `area legend` or its legend shows a line; on a reversed x axis `anchor=east` puts a label on the older side (it overlapped the Chicxulub star); the shared ETOPO1 row is `data:etopo1` (shared data_ledger.md), not `data:etopo-1deg`; first Commons pick for an OAE showed an identifiable person and a Niobrara close-up was uninformative: both deleted (single files), rows removed; Stanley 2016 (PNAS) is not open via NCBI efetch (abstract only), its numbers via Marshall 2023 (PMC) and Kaiho 2022 (BG); unsourced locality claims removed in the sourcing pass. Solutions re-derived from the rounded printed chain (problem Q22 cumulated 117.9 -> 390 m; ex. 7 8.7e22 J, 59 years).
- **2026-10-23 SPLIT IN EFFECT (coordinator):** my range is **ch. 19-25**; a second Book 4 agent writes **ch. 26-31** (notes in `sources/book4/PROGRESS-B.md`, builds into its own scratch outdir; `build/` stays mine). Do not touch ch. 26-31 .tex/solutions/figdata/tests/images. Errors/undefined inside ch. 26-31 in my build: wait ~10 min and rebuild, never edit; persisting > 1 h: tell the coordinator. Do NOT run `make figdata Y=bachelor-2` or `make test Y=bachelor-2` until both ranges are written: run my scripts/tests by file. Keep ch. 19-25 labels exactly as DEFINITIONS.md (the other agent cites `ch:b2:` labels). Shared files append-only, re-read before each write. **After ch. 25: report 'range 19-25 done' to the coordinator and do NOT start Phase C**; Phases C and D (linker, whole-book per-page figure pass, scripted all-solutions re-read, report) stay mine over all 31 chapters after the seam is reconciled. Book 3 landing traps: the whole-book per-page figure pass after the linker found 11 defects missed per chapter; plain-text 'exercise N' references must be `\cref`. The `data:etopo-1deg` ledger id in ch. 19 (which failed `test_repo_ledger_is_clean`) is already fixed to the shared `data:etopo1`.
- **2026-10-23 cref sweep (ch. 1-19):** 53 plain-text same-chapter 'exercise N' references converted to `\cref{exo:b2:<slug>:N}` (`\Cref` at sentence start) by a script that asserts each label exists; 'question N' references inside problems stay plain (no labels). New chapters write `\cref` directly.
- **Ch. 20 done** (0/0/0, 333 pp with the other agent's chapters; gates, calibration, numbering, pic scaling, 10 tests by file, check_ledger 1977 rows OK, wiki 0, palaeoenv.py re-run with no diff). Taphonomy, Lagerstätten (Burgess, Solnhofen), actualism, assemblages, ichnofacies, and the Varden cover read as a transgression with compaction-corrected rates (Athy constants from pyBacktrack; limestone Turer and Maynard 2003). Invented ages on the real chart: limestone = Toarcian 184.2-174.7 Ma, shale = Aalenian-Callovian 174.7-161.5 Ma; the syncline depths 766/866/1046/1166 m match Book 5's Varden-2 well (porosity 0.08 from 2573 kg/m3). Traps: the system grep is ugrep and fails on complex alternations ("pattern too complex"): use `$S/bin/find.py FILE REGEX`; Commons file titles/descriptions serve only to identify a photo, never as a source (a caption's "scale bar in centimetres" had no source and was cut); Athy's limestone law predicts 0.41 at 956 m against the measured 0.08: cementation, made an exercise rather than hidden; Zoophycos moved from shelf (Palaeozoic) to slope (Mesozoic) to deep sea (Cenozoic), so ichnofacies depth must use the rock's age; unsourced flourishes removed in the sourcing pass (Burgess "most without shells", "most of what is known", "ammonite zones last a million years", a claim that no radiometric method dates that finely, contradicted by the +-0.11 Myr U-Pb ages). Defect found elsewhere (not used as a source): Nature Commun 2026 (PMC13161362) writes "In the 1830s, James Hutton proposed..." -- Hutton died in 1797.
- **Ch. 21 done** (0/0/0, 358 pp with the other agent's chapters; gates, calibration, numbering, pic scaling, 6 tests by file, check_ledger 2063 rows OK, wiki 0, thermo.py re-run with no diff). Humidity variables, C-C with constant L against NIST IAPWS-95 (+1.1 % at 20 degC), LCL rule derived (Gamma_dew 1.8 K/km), Gamma_s with proof, theta_e, skew-T (equal-area by unit Jacobian), conditional instability, LFC/EL/CAPE/CIN on the real Norman sounding (CAPE 2096 / 2227 virtual, CIN -199 / -130, LI -9.5), kappa-Koehler with the critical point, CCN numbers, Bergeron. Traps: journals.ametsoc.org 403, so Bolton (1980) cannot be cited: the empirical e_s formula is cited from Su et al. 2026 (Sci Data, PMC) without naming Bolton; NIST values typed from memory were wrong in the last digits (872.58, 5629.0): always paste fetched values; the IGRA2 'y2d' zip renames its member each year, use the 'data-por' URL; `write_table` blank separators must be `()`, never `("","","")` (whitespace lines break pgfplots); colour names are ocBlue/ocRed/omMeth (no omBlue/omRed/omGreen; build error); no booktabs (\toprule undefined): use \hline; a curve under 6 hPa disappears on a 0-80 hPa axis (ice curve moved to the ratio panel); unsourced flourishes cut in the sourcing pass ('several hundred per cent' for pure-water nucleation replaced by a computed Kelvin factor, 'most mid-latitude precipitation starts as ice', 'INPs much rarer than CCN', 'operator checks the profile', 'air forced up a slope / convergence' replaced by the ledger's front and disturbance aloft).
- **Ch. 22 done** (0/0/0, 383 pp with the other agent's chapters; gates, calibration, numbering, pic scaling 0, test_weather 4 passed, check_ledger OK, every cited ledger id exists, wiki 0, weather.py re-run byte-identical). Frontal slope derived from pressure continuity + hydrostatic + geostrophic (not named after Margules), polar-front life cycle, conveyor belts and dry intrusion, Rossby phase speed admitted (Year 3 derives it), stationary wavelength computed only (Book 5 owns the term), blocking, genesis conditions, potential intensity with the T_s/T_o dissipative-heating factor vs Carnot, Lorenz 63 (fixed points, divergence, lambda 0.909 computed vs 0.906 published), predictability (2.4 d doubling, Selz 4-5 d). EXCLUDED, no fetchable source: the Shapiro-Keyser model, the Bergen school / Bjerknes attribution, 'forecasts right nine times in ten', Margules by name, 'cold-water upwelling caps storm intensity' (replaced by Gilford's shear/subsidence and AOML's dry air), 'cyclones form preferentially under jet streaks', Lorenz 1963 'from a convection model' (only a reservoir-computing paper says so). The NWS glossary has no 'frontal surface', 'warm conveyor belt', 'Norwegian cyclone model', 'polar front theory' or 'frontal wave' entries. Traps: a `decorations.markings` arrow decoration on a 241-sample smooth plot dies with 'Dimension too large': draw arrows as short chords between two parameter values; never name a \foreach variable \ang (it overwrites siunitx's \ang and prints numbers); the first sourcing pass of a finished chapter still found 8 unsourced flourishes (katafront cloud, WCB rain share, dry slot = dry intrusion, cyclones under jet streaks, cold-water cap, model step in minutes, 'no agreed explanation' of blocks reworded to the source's 'not well understood').
- **Ch. 23 done** (0/0/0, 410 pp with the other agent's chapters; gates, calibration, numbering, pic scaling 0, test_climvar 7 + test_weather 4 passed, check_ledger OK, every cited ledger id exists, wiki 0, climvar.py re-run byte-identical). Modes/index/climatology, method from observations to an index, monsoon (NWS def, IMD heat low 160 W/m2, LPA 88 cm +-9, Kerala onset criteria), ENSO (CPC FAQ features and timing, Bjerknes feedback after Thirumalai 2024, recharge oscillator after Stuecker 2025), ONI and the relative ONI, NAO and teleconnections (IOD, SAM, PDV named), damping time tau = rho c_p h/alpha with alpha 16.1 (Wang 2024) and red noise (Shi 2022). Traps: CPC made the RELATIVE ONI official on 1 Feb 2026 (PNS 26-05) and the October 2026 discussion's 'Nino-3.4 +2.1' is the relative monthly anomaly (Rnino34 2.08), not the traditional 2.56: the text explains both; the two-decimal ONI file cannot reproduce the CPC one-decimal table (5-season rule loses 3 episodes incl. 2026), so the census runs on the parsed v6 HTML table; origin.cpc host does not resolve (use www.cpc.ncep.noaa.gov); Met Office monsoon page 404. EXCLUDED, unsourced in the first draft and cut on the sourcing pass: West African rain belt at 5 N in May-June and its 'jump' (exercise rewritten as the 2.5 mm/day domain criterion), ENSO jet-stream shift and Atlantic hurricane suppression, 'NAO mostly atmospheric noise / not predictable', 'stochastic model explains most extratropical persistence', 'one of the richest fisheries in the world', Walker's pressure-record provenance and date, 'missionary who crossed the Atlantic', 'Indonesia and northern Australia' kept (FAQ) but 'Siberia' reach cut, the AO as 'hemispheric counterpart'. Days-in-math bug fixed in ch. 22 solutions too (`$... = 11.8~days$` set 'days' in math italic; now `$...$~days`).
- **Ch. 24 done** (0/0/0, 436 pp with the other agent's chapters; gates, calibration, numbering, pic scaling 0, test_proxies 6 passed, check_ledger OK, every cited ledger id exists, wiki 0, proxies.py re-run byte-identical). Archives and proxies re-founded; benthic calibration T = 16.1 - 4.76[db - (dsw - 0.27)] (Miller 2020, admitted); ice-volume effect by mass balance on the mean ocean depth 3682.2 m (1.46 per mil for 130 m of ice at -40, 0.0109 per mil/m against White's 0.011; pore water 1.0 +- 0.1, Wharton 2026); LR04 1.69 per mil (19-23 ka vs today); EDC dD -396.6 -> -441.7, dT -0.09 -> -9.39; CO2 189.7 vs 279.4 ppm (new part co2 in proxies.py, row data:b4-proxies-co2); Mg/Ca 0.4 exp(0.09T) vs fit 0.372 exp(0.0936T) (Morley 2024); dendro/cross-dating (Bebchuk 2026 yews), speleothem/varve (NCEI, Crawford Lake), age model with the GICC05 table and the linear vs sqrt(n) counting error; inthelab from the NSF Ice Core Facility page (-36/-24 degC, CPL 30-35 m/day). Traps: Crawford Lake's bottom water is WELL OXYGENATED (no bioturbation because of salinity/alkalinity) -- my first draft said anoxic, caught on the sourcing pass; `\num{1.0 \pm 0.1}` prints 1.0(1) (use plain math); Svensson 2008 gives no rationale for treating the MCE as 2 sigma: the text calls the linear sum 'the cautious choice' in its own voice and quotes the two-counter comparison instead; author first names not in a source dropped (Urey, Shackleton, Opdyke); White eq. 9.58 is NOT used (with Delta ~30 it gives the wrong sign of dT/dDelta -- a slip in the posted draft chapter, Phase D note); the pore-water 1.0 per mil and the mass balance with realistic ice (1.28-1.83) disagree: the text and ex. 5 present the gap as an uncertainty, not a resolution. EXCLUDED, unsourced in the first draft and cut: 'thermometers for less than two centuries', archive resolutions/spans and the coral row of the table, 'shells grown in culture', 'flowstones', 'usually of calcite', speleothem calcite 'contains uranium', 'doubled rings', the 'which is why counting stops at 60 ka' causal claim, Hulu Cave 'in China', the arrows' meaning on the GISP2 slide, alkenones (no source fetched).
- **Projection after ch. 24 (2026-10-23):** PDF 436 pp with ch. 1-24 and 26-30 written, 25 and 31 placeholders: ~14.3 pp per written chapter; projected ~464 pp vs ~370 target (+25 %, OVER, stable since ch. 16). No restoration.
- **Ch. 25 done** (0/0/0 at 461 pp with the second writer's ch. 26-31; gates, calibration, numbering, pic scaling 0, test_orbital 7 + test_proxies 6 passed, check_ledger OK, every cited ledger id exists, wiki 0, orbital.py re-run byte-identical). New dataset bachelor-2-orbit91 (Berger and Loutre 1991 via NCEI, my fetch_data block) and figdata/bachelor-2/orbital.py: daily-mean insolation from e, omega, eps with the Sun's true longitude (June solstice 90 deg; the tables' mid-July is lambda = 120 deg, which reproduces the 1001 rows of the last Myr within 0.012 W/m2 and insol91.jun at 0 kyr). Berger's omega is HELIOCENTRIC (longitude of perihelion seen from the Sun, from the moving equinox): the Sun's longitude at perihelion is omega + 180 (281.4 deg today, ~3 January); r/a = (1 - e^2)/(1 - e cos(lambda - omega)). Contents: elements (def longitude of perihelion + climatic precession), Milankovitch parameters/theory, periods (La2004 + NASA), distance proposition, Kepler-II proof that annual means do not depend on omega and pole annual = S0 sin eps/(pi sqrt(1-e^2)), method, history box (EO 2000, no university), spectra vs LR04 (24 / 95.5 / 41 kyr), glacials/interglacial/termination re-founded (Barker 2021, Koehler 2020), linear lag model (tau 10 kyr a stated model choice; r 0.42 vs 0.23), MPT (Clark 2006, Koehler 2020), CO2 2.2 W/m2 vs 0.54 global orbital vs ~109 at 65 N. Traps: pgfplots prints a '10^-2' multiplier on small fixed-format ticks that collides with the panel above in a groupplot -- `scaled y ticks=false`; panel labels top-right sat on the 960 ka eccentricity peak; 'about 100,000-year problem', 'Jupiter and Saturn', 'equatorial bulge', 'in the direction opposite', 'almost every obliquity cycle', 'critical size' were checked against the sources: the first, the fourth and the last two were cut or reworded, the second and third are now in row nasa:milank-causes; the June maximum before the last interglacial is at 128 ka, not 127. EXCLUDED: the '100,000-year problem' label (no fetched source names it), any claim about why the axial precession is retrograde, the regolith hypothesis beyond 'perhaps' (Koehler lists it as a candidate only).
- (2026-10-23): range 19-25 done, reported to the coordinator; the coordinator's GO for Phase C and D over all 31 chapters followed (the second writer stopped; ch. 26-31 are mine to edit). Original plan:
  coordinator's go (Phase C then runs over all 31 chapters: linker unwrap/apply, term_config curation,
  idempotence 0, whole-book per-page figure pass, scripted Q/A re-read, AI stubs of ch. 1-4 replaced,
  `make figdata Y=bachelor-2` no diff, `make test Y=bachelor-2`; then the "after 31" projection row).

## Phase C (2026-10-23, all 31 chapters)

- Seam: ch. 13 index entries `allochthonous (rock unit)` / `autochthonous (rock unit)` (the bare words collided
  with the ch. 26 weathering-flux sense); `tools/term_config/book4_en.py` curated (EXTRA_PROTECT `exposure time`
  (ch. 28 is about exposure as assets), `what mixing ratio`); ch. 29 ex. 4 "has a grade of" (the verb "grades" had
  linked to the noun); credits page and CREDITS.md in chapter order (ch. 21-25 items added, 29 items).
- Linker: `--unwrap --apply`, `--apply`, dry run "links to insert: 0" after every edit: 516 linkable terms, 2019
  links, 191 distinct targets, 2 terms dropped as defined twice.
- Scripted Q/A re-read of every question against its solution, ch. 1-31 (`$S/phc/qa.py NN`): ch. 8 problem
  data lacked the olivine/plagioclase/clinopyroxene SiO2 that Q18 needs (added: 39.19 / 50.54 / 51.5); ch. 1 sol.
  "well inside the orbit of Mercury"; ch. 23 Q10 "four seasons before" (was two); ch. 25 ex. 9 1.2199/0.2732 = 4.47;
  ch. 27 "0.989 to 2.31" (twice) and correlation -0.95 (was -0.99). The others re-derived clean.
- Whole-book per-page figure pass: 228 objects on single-page 130-dpi renders of the linked build, FIGCHECK
  section "Phase C full pass": 20 objects fixed (8 in layout, 15 in science or caption), among them three captions that said the
  opposite of their curve (ch. 8 AFC "falls more slowly", ch. 24 GICC05 "steepens", ch. 17 "hundreds of times"),
  a threshold line below the critical value it was meant to exceed (ch. 21 Köhler 0.4 % vs s_c 0.42 %), a
  text number off its own model (ch. 8 albite at 82 %, not 78 %), a satellite misnamed (ch. 22 Terra -> Aqua,
  from the Commons/Visible Earth description) and an interpolated data gap read as a slow onset (ch. 26 PETM).
- Checks at the end: build 0/0/0, 461 pp; gates.sh bachelor-2 OK; calibration OK; numbering OK (31); pic
  scaling 0; check_ledger OK with every cited id existing (836 distinct ids cited, 637 Book 4 rows); wiki grep 0;
  curriculum/university grep clean ("University Year N" only as book titles, "program" only for software);
  figdata unchanged since `make figdata Y=bachelor-2` (no diff) and `make test Y=bachelor-2` (205 passed).

### New traps (Phase C)
- A caption written before the figure was final can state the opposite of what the curve shows: read every
  caption's comparative words ("faster", "steepens", "hundreds of times") against the plotted values.
- A dashed or threshold line placed at a round number can sit on the wrong side of a computed critical value.
- A spliced dataset's interpolated steps look like data: check the count columns before describing a ramp.
- Lengthening one caption by one line pushed a whole TikZ figure to the next page and left half a page empty:
  after any caption change, re-render the page AND the next one.
- qa.py strips `%` comments without honouring `\%`: text after `wt\%` is cut (read the source there).
- `figs.py` synctex maps a table float to its `\begin{table}` line, which can sit on the page before the float.

## Chapter table

| ch. | slug | status | pp | notes (exos/pb q./figs/ledger rows/FIGCHECK) |
|---|---|---|---|---|
| 1 | ism-star-formation | written, 0/0/0, gates OK | ~15 (13 + 2 sol.) | 12 exos (4/5/3), 24 pb q. (named: 624 kyr), 4 TikZ/pgf + 2 photos + 1 AI (stub), figdata jeans.py + 5 tests, 26 ledger rows, FIGCHECK 7 lines |
| 2 | planet-formation-meteorites | written, 0/0/0, gates OK | ~17 (14 + 3 sol.) | 12 exos (4/5/3), 24 pb q. (named: 707 degC), 4 TikZ/pgf + 1 table-figure + 2 photos + 1 AI (stub), figdata nebula/condensation/al26/meteorites + 7 tests, ~27 ledger rows, 1 dataset (bachelor-2-meteorites), FIGCHECK 8 lines |
| 3 | elements-in-the-earth | written, 0/0/0, gates OK | ~17 (14 + 3 sol.) | 12 exos (4/5/3), 24 pb q. (named: 30.3 %), 1 TikZ periodic table + 5 pgf + 1 table + 1 photo + 1 AI (stub), figdata geochem.py + 8 tests, 13 ledger rows + 6 sources (GERM, Gale 2013 via Harvard DASH, USGS BHVO-2, Budahn 1991), FIGCHECK 9 lines; 'bulk partition coefficient' moved here from ch. 8 (ch. 8 recalls) |
| 4 | isotope-geochemistry | written, 0/0/0, gates OK | ~16 (13 + 3 sol.) | 12 exos (4/5/3), 24 pb q. (named: 1.2 %), 5 pgf + 1 TikZ cartoon + 1 table + 1 AI (stub), figdata isotopes.py + 6 tests, 6 sources + 15 ledger rows, 1 dataset (bachelor-2-oib-isotopes, Stracke 2022 GRO.data CC BY), FIGCHECK 8 lines |
| 5 | magma-emplacement | written, 0/0/0, gates OK | ~15 (13 + 2 sol.) | 12 exos (4/5/3), 26 pb q. (named: 67 years), 3 pgf + 2 TikZ + 1 table + 1 photo + 1 AI (stub), figdata magma.py + 6 tests, 14 sources + 21 ledger rows, FIGCHECK 8 lines |
| 6 | eruptive-styles | written, 0/0/0, gates OK | ~16 (13 + 3 sol.) | 12 exos (4/5/3), 26 pb q. (named: 78 %), 6 pgf + 1 TikZ + 1 table + 3 photos + 1 AI (stub), figdata eruptions.py + 6 tests, 17 sources + 18 ledger rows, 1 dataset (bachelor-2-gvp-eruptions), FIGCHECK 9 lines |
| 7 | mantle-melting | written, 0/0/0, gates OK | ~14 (11 + 3 sol.) | 12 exos (4/5/3), 26 pb q. (named: 1315 degC), 5 pgf + 3 TikZ + 1 photo, figdata melting.py + 6 tests, 5 sources + 8 ledger rows, FIGCHECK 9 lines |
| 8 | magmatic-differentiation | written, 0/0/0, gates OK | ~15 (13 + 2 sol.) | 12 exos (4/5/3), 26 pb q. (named: 40 %), 6 pgf (incl. groupplot) + 2 TikZ + 2 photos, figdata differentiation.py + 6 tests, 7 sources + 14 ledger rows (+2 Book 2 rows read-only), 1 dataset (bachelor-2-skaergaard, Tegner 2023 GEUS CC BY 4.0), FIGCHECK 9 lines |
| 9 | magmatic-series | written, 0/0/0, gates OK | ~13 (10 + 3 sol.) | 12 exos (4/5/3), 23 pb q. (named: 48 kg per 100 kg), 1 TikZ QAPF + 5 pgf (TAS, AFM+log-ratio, K2O, spider, Ti-Zr-Y), figdata series.py + 7 tests, 5 sources + 14 ledger rows, 2 datasets (bachelor-2-cath, bachelor-2-basalt-settings, GeoplotR GPL-3 factual data), FIGCHECK 6 lines |
| 10 | metamorphic-facies | written, 0/0/0, gates OK | ~13 (10 + 3 sol.) | 12 exos (4/5/3), 24 pb q. (named: 514 °C), 2 pgf (Al2SiO5 computed vs HM93/Day73, ΔG at 6 kbar) + 1 TikZ facies grid + 2 photos (CC BY 2.0), 2 tables, figdata facies.py + 7 tests, 4 sources + 12 ledger rows (Book 2 hm93/iugs rows cited read-only), FIGCHECK 4 lines |
| 11 | pt-paths | written, 0/0/0, gates OK | ~11 (8 + 3 exos/pb + 3 sol.) | 12 exos (4/5/3), 24 pb q. (named: 1.0 mm/yr), 1 TikZ (Barrovian schematic) + 5 pgf (FS fit, GB+GASP, geotherms, P-T path, series) + 2 photos (CC BY 2.0, CC BY-SA 1.0), figdata ptpaths.py + 7 tests, 11 sources + 17 ledger rows (Book 2 iugs/barrow/earle and Book 3 delaney/roy/vila/prem/kelley/dick rows cited read-only), FIGCHECK 8 lines |
| 12 | crustal-melting | written, 0/0/0, gates OK | ~12 (10 + 2.5 sol.) | 12 exos (4/5/3), 24 pb q. (named: 9.5e3 km3), 3 pgf + 2 TikZ + 2 photos, figdata anatexis.py (+ ptpaths paths) + 6 tests, 20 sources + 22 ledger rows, FIGCHECK 7 lines |
| 13 | alpine-orogen | written, 0/0/0, gates OK | ~17 (14 + 3 sol.) | 12 exos (4/5/3), 24 pb q. (named: 133 km), 3 pgf (relief map, chevron, profile groupplot) + 5 TikZ (stages, klippe/window, foreland, crustal section, model bar) + 2 tables + 2 photos (CC BY-SA 3.0/4.0), figdata alps.py + 6 tests, 2 datasets (bachelor-2-etopo-alps, bachelor-2-alps-moho), 19 sources + 31 ledger rows (+2 Book 4 rows reused), FIGCHECK 12 lines |
| 14 | himalaya-andes | written, 0/0/0, gates OK | ~14 (12 + 2 sol.) | 12 exos (4/5/3), 24 pb q. (named: 62 km), 3 pgf (map, swath groupplot, pressure) + 2 TikZ sections (redrawn on shared vertices) + 1 table + 2 photos (CC BY-SA 4.0/2.5), figdata plateaus.py + 7 tests, 2 datasets (bachelor-2-etopo-tibet, -andes), 25 ledger ids cited (19 Book 4 rows, 6 read-only), FIGCHECK 8 lines |
| 15 | wilson-cycle | written, 0/0/0, gates OK | ~13 (11 + 2 sol.) | 12 exos (4/5/3), 24 pb q. (named: 2880 km), 2 pgf (model ocean, supercontinent chart) + 2 TikZ (Iapetus/Rheic 3 panels, Wilson 8 panels) + 1 table + 1 photo (Siccar Point, CC BY-SA 4.0), figdata wilson.py + 5 tests, 6 sources + 10 ledger rows (+8 shared/Book 2 rows read-only), FIGCHECK 6 lines |
| 16 | basins-compared | written, 0/0/0, gates OK | ~13 (11 + 2 sol.) | 12 exos (4/5/3), 24 pb q. (named: beta = 1.50), 2 pgf (backstripped well, McKenzie curves) + 3 TikZ (basin families, backstrip columns, stretching) + 2 tables + 1 photo (CC BY-SA 3.0), figdata basins.py + 5 tests (isostatic integral, full series, finite differences), 11 sources + 11 ledger rows (+ Book 3 pybacktrack:compaction and ch. 13 Molasse rows read-only), FIGCHECK 8 lines |
| 17 | oceanic-islands | written, 0/0/0, gates OK | ~12.5 (11 + 1.5 sol.) | 12 exos (4/5/3), 24 pb q. (named: reef cap 1287 m), 3 pgf (sinking curves, drilled holes bars, log rates) + 2 TikZ (life along a chain, flank collapse) + 1 photo (Kure Atoll, NASA PD), figdata islands.py + 4 tests, 7 sources + 22 ledger rows (+ Book 2 ps77:depth-age, lambeck14:lgm, ipcc:lgm-sea, cd87:rate, Book 3 parsons:plate-model, perry:chagos, Book 1 usgs:lgm read-only), FIGCHECK 6 lines |
| 18 | precambrian-earth | written, 0/0/0, gates OK | ~13.5 (12 + 1.5 sol.) | 12 exos (4/5/3), 24 pb q. (named: komatiite lava 364 degC hotter than a primary MORB; brief asked for the mantle excess: the text gives the 200-300 K mantle excess from Pierru 2022 in prose and Q23 explains the difference), 3 pgf (komatiite line, energy balance, hysteresis) + 2 TikZ (timeline, dome-and-keel map+section) + 2 photos (spinifex komatiite, cap carbonate; James St. John CC BY 2.0), figdata precambrian.py + 5 tests, 12 sources + 28 ledger rows, FIGCHECK 7 lines |
| 19 | phanerozoic-earth | written, 0/0/0, gates OK | ~14 (12 + 2 sol.) | 12 exos (4/5/3), 24 pb q. (named: about 390 m, the rise from doubling the spreading rate once the sea spreads over the land), 5 pgf (6-panel palaeomaps, sea level, age histogram + rise vs f, hypsometry + flooding, extinction timeline) + 1 table + 2 photos (Monument Rocks CC BY 2.0, Bonarelli level CC BY-SA 4.0), figdata phanerozoic.py + 6 tests, fetch block +12 datasets (Miller 2005 NOAA, MERDITH2021 coastlines and city positions via GWS), 17 sources + 29 ledger rows, FIGCHECK 8 lines |
| 20 | palaeoenvironments | written, 0/0/0, gates OK | ~14 (12 + 2 sol.) | 12 exos (4/5/3), 24 pb q. (named: about 36 m per million years, the lime mud of the Varden limestone when laid down), 3 TikZ (taphonomic path, ichnofacies profile, Varden log) + 1 pgf groupplot (Athy porosity + restoration factor) + 3 photos (Burgess Waptia/Marrella CC BY 2.0, Berlin Archaeopteryx CC BY-SA 3.0, Zoophycos CC BY 4.0), figdata palaeoenv.py + 4 tests, 19 sources + 23 ledger rows, FIGCHECK 7 lines |
| 21 | atmospheric-thermodynamics | written, 0/0/0, gates OK | ~15 (13 + 2.3 sol.) | 12 exos (4/5/3), 24 pb q. (named: about 63 m/s, the parcel-theory updraft of the Norman surface air), 2 pgf (e_s + water/ice ratio groupplot; Koehler curves) + skew-T of the real Norman 16 Apr 2026 12 UTC sounding (IGRA2) + 1 TikZ (warm/ice precipitation roads) + 1 photo (Corfidi anvil, NOAA PD) + 1 AI (radiosonde launch), figdata thermo.py + 6 tests, dataset bachelor-2-sounding in fetch_data Book 4 block, 10 sources + 21 ledger rows, FIGCHECK 6 lines |
| 22 | weather-systems | written, 0/0/0, gates OK | ~13 (11 + 1.8 sol.) | 12 exos (4/5/3), 24 pb q. (named: about 12 days, the useful horizon of a forecast whose errors double every 2.4 days), 4 TikZ (front cross-section, polar-front life cycle 2x2, Rossby waves polar view, tropical-cyclone heat engine) + 2 pgf (Lorenz runs/butterfly groupplot; error growth with fit) + 2 photos (Iceland low MODIS PD, Isabel eye ISS PD) + 1 AI (forecast centre), figdata weather.py + 4 tests, 12 sources + 23 ledger rows, FIGCHECK 9 lines |
| 23 | climate-variability | written, 0/0/0, gates OK | ~13.5 (12 + 1.6 sol.) | 12 exos (4/5/3), 23 pb q. (named: about 7 years, 6.9, the mean interval between the starts of the 11 strong El Ninos, MAM 1957 - MAM 2026), 4 TikZ (monsoon section, ENSO three phases, Bjerknes loop) + 3 pgf (ONI/RONI fill, NAO winters, red noise + acf) + 1 AI (fishing harbour, history box), figdata climvar.py + 7 tests, 5 CPC datasets in fetch_data Book 4 block, 17 sources + 34 ledger rows, FIGCHECK 7 lines |
| 24 | climate-proxies | written, 0/0/0, gates OK | ~15 (13 + 2.3 sol.) | 12 exos (4/5/3), 24 pb q. (named: about 3.3 degC, the LGM deep-ocean cooling left in the LR04 change after the pore-water ice-volume correction), 1 TikZ (ice-volume cartoon) + 4 pgf (ice-volume lines, LR04/EDC/CO2 three panels, calibrations groupplot, GICC05 groupplot) + 1 table + 2 photos (GISP2 layers PD, speleothem CC BY 2.0) + 1 AI (cold lab), figdata proxies.py + 6 tests, 17 sources + 30 ledger rows, FIGCHECK 9 lines |
| 25 | orbital-forcing | written, 0/0/0, gates OK | ~14 (11 + 3 sol.) | 12 exos (4/5/3), 24 pb q. (named: about 439 W/m2, the June-solstice daily-mean insolation at 65 N 116,000 years ago when the last interglacial ended), 1 TikZ (orbit geometry) + 5 pgf (elements three panels, latitude two panels, 65 N curve + residual, spectra, lag model), figdata orbital.py + 7 tests, new dataset bachelor-2-orbit91, 5 sources + 10 ledger rows, FIGCHECK 6 lines |
| 26 | deep-time-climate | written by the second writer (see PROGRESS-B.md), 0/0/0; Phase C re-read here | see PROGRESS-B.md | Phase C: solutions re-read, figures re-checked (FIGCHECK 'Phase C full pass') |
| 27 | anthropogenic-climate-change | written by the second writer (see PROGRESS-B.md), 0/0/0; Phase C re-read here | see PROGRESS-B.md | Phase C: solutions re-read, figures re-checked (FIGCHECK 'Phase C full pass') |
| 28 | geological-hazards | written by the second writer (see PROGRESS-B.md), 0/0/0; Phase C re-read here | see PROGRESS-B.md | Phase C: solutions re-read, figures re-checked (FIGCHECK 'Phase C full pass') |
| 29 | ore-deposits | written by the second writer (see PROGRESS-B.md), 0/0/0; Phase C re-read here | see PROGRESS-B.md | Phase C: solutions re-read, figures re-checked (FIGCHECK 'Phase C full pass') |
| 30 | energy-geology | written by the second writer (see PROGRESS-B.md), 0/0/0; Phase C re-read here | see PROGRESS-B.md | Phase C: solutions re-read, figures re-checked (FIGCHECK 'Phase C full pass') |
| 31 | field-lab-methods-2 | written by the second writer (see PROGRESS-B.md), 0/0/0; Phase C re-read here | see PROGRESS-B.md | Phase C: solutions re-read, figures re-checked (FIGCHECK 'Phase C full pass') |

## Term changes after the split notice

(none yet)

## Page projection

Target ~370 pp. Plan: 31 chapters x ~12 pp (course ~8.5, exercises ~1.5,
problem ~1, solutions ~1.5 in the back) = ~372 pp + front matter/index ~18 =
**~390 pp**. Book 3 runs ~13.3 pp/chapter at mid-book (its PROGRESS). Check
after chapters 8, 16, 24 and 31: if the running mean is > 10 % under 12 pp per
chapter, restore depth (worked examples, a method box, a figure) before going
on. Calibration: ~70 source lines of course text ~ 1 page.

| checkpoint | chapters | pages (PDF) | pp/chapter | action |
|---|---|---|---|---|
| after 8 | 8 written | course text pp. 2-106 | ~15.5 (13.1 text + 2.4 sol.) | over target (+34 %): no restoration |
| after 16 | 16 written | 266 (incl. 15 placeholders) | ~14 (11.7 text + 2.4 sol.) | over target (+22 %): no restoration |
| after 24 | 29 written (1-24 mine, 26-30 the second writer's), 25 and 31 placeholders | 436 | ~14.3 ((436 - ~20 front/back - 2 placeholder pp.)/29) | projected ~436 + 2 x 14 = ~464 pp vs ~370 target (+25 %, OVER): no restoration |
| after 31 | 31 written (1-25 mine, 26-31 the second writer's) | 461 | ~14.2 ((461 - ~20 front/back)/31) | final: 461 pp vs ~370 target (+25 %, OVER, stable since ch. 16): no restoration; depth kept, nothing cut to fit |

## Searches and fetches

- Search budget ~600 for the book (batch file). **Used: ~38 web searches** (Kauffmann arXiv id, Lodders table; ch. 2: Gail 2014, Lugaro 2018, Chiang--Youdin 2010, Rojas 2021, Folco 2006, meteorite CSV route; ch. 3: ~6 for GERM, Gale 2013, BHVO-2, partition coefficients; ch. 4: ~6 for Stracke data, Sm decay constant, Edwards 2019, Dhuime 2018); everything else direct fetches.
- Direct probes (not searches) in Phase A: 8 (listed below with results).
- Estimate for Phase B: ~250--300 searches (heaviest: ch. 27 AR6 statements
  ~40 rows, ch. 3/9 compositions and reference materials, ch. 6 eruption
  numbers, ch. 13--15 orogen ages, ch. 18--19 dates, ch. 24--26 proxy
  calibrations, ch. 28--30 hazard and resource numbers), plus direct fetches.

Phase A probes:

| probe | result |
|---|---|
| IMCCE La2004 (`http(s)://vo.imcce.fr/...`) | timed out both schemes: use Berger & Loutre 1991 instead |
| NOAA NCEI `pub/data/paleo/climate_forcing/orbital_variations/insolation/orbit91` | reachable; columns age, ECC, OMEGA, OBL, PREC, 65NJul, 65SJan, 15NJul, 15SJan; 0 to -5000 kyr; also `insol91.jun`, `huybers2006insolation/`, `zeebe*` dirs |
| CPC `oni.ascii.txt` | reachable (PD) |
| CPC NAO monthly `norm.nao.monthly.b5001.current.ascii` | reachable (PD) |
| GVP WFS Holocene eruptions CSV (`webservices.volcano.si.edu/geoserver/GVP-VOTW/ows?...typeName=GVP-VOTW:Smithsonian_VOTW_Holocene_Eruptions&outputFormat=csv`) | works; columns incl. ExplosivityIndexMax, StartDateYear, GeoLocation |
| NASA meteorite landings (data.nasa.gov Socrata) | 404 (portal moved to CKAN): find a new route or drop the dataset (ch. 2 can use published class fractions) |
| PANGAEA CENOGRID collection 10.1594/PANGAEA.917503 | collections have no textfile: fetch a child dataset (Phase B) or use Zachos 2008 at NCEI |
| USGS geochemical reference materials page (`crustal.usgs.gov/geochemical_reference_standards/basaltbhvo2.html`) | reachable |

## Datasets planned (one `# Book 4:` block appended to `tools/fetch_data.py`)

Ids start `bachelor-2-`; derived CSVs in `data/derived/`; terms in
`data/MANIFEST.md` by the tool; ledger `data:b4-...` rows in `book4.md`.

| id | source (direct URL) | licence | size | used in |
|---|---|---|---|---|
| bachelor-2-orbit91 | NOAA NCEI orbit91 (above) | US gov PD | ~400 kB | ch. 25 |
| bachelor-2-oni | CPC oni.ascii.txt | PD | ~30 kB | ch. 23 |
| bachelor-2-nao | CPC NAO monthly | PD | ~20 kB | ch. 23 |
| bachelor-2-soi (optional) | CPC SOI | PD | ~20 kB | ch. 23 |
| bachelor-2-gvp-eruptions | GVP WFS CSV (above) | Smithsonian GVP terms as for shared `gvp` | ~3 MB raw, ~300 kB derived | ch. 6, 28 |
| bachelor-2-etopo-alps | ERDDAP `etopo180.csv` 45--48.5 N, 5--12 E, stride 2 | NOAA PD | ~1 MB raw | ch. 13 |
| bachelor-2-etopo-tibet | ERDDAP 25--40 N, 75--100 E, stride 2 | NOAA PD | ~3 MB raw | ch. 14 |
| bachelor-2-etopo-andes | ERDDAP 10--30 S, 75--60 W, stride 2 | NOAA PD | ~2 MB raw | ch. 14 |
| bachelor-2-ar6-erf | AR6 WG1 Annex III ERF table (Zenodo record 5705391) | CC BY 4.0 | ~100 kB | ch. 27 |
| bachelor-2-miller2005 | NOAA NCEI paleo `contributions_by_author/miller2005/` | PD | ~100 kB | ch. 19 |
| bachelor-2-cenogrid or -zachos2008 | PANGAEA child of 10.1594/PANGAEA.917503 (CC BY 4.0) or NCEI Zachos 2008 (PD) | as stated | ~1 MB | ch. 26 |
| bachelor-2-foster2017 (optional) | Foster et al. 2017 supplementary (CC BY 4.0) | CC BY | ~100 kB | ch. 26 |
| bachelor-2-porphyry-cu | USGS OFR 2008-1155 grade--tonnage (Singer et al.) | PD | ~200 kB | ch. 29 |
| bachelor-2-sounding (optional) | IGRA v2 one station-day (NCEI) | PD | ~50 kB | ch. 21 |
| bachelor-2-speleothem (optional) | Cheng et al. 2016 (NCEI) | PD | ~200 kB | ch. 24 |

Shared sets read: lr04, edc-temperature, co2-icecore, co2-mlo, gistemp,
gmsl-altimetry, usgs-m6, etopo-1deg, pb2002, ne-land, prem. Other books'
sets (read-only, report the dependency if used): `bachelor-1-hotspots.csv`
(ch. 17).

## figdata scripts planned (`figdata/bachelor-2/<name>.py`, tests `tests/bachelor-2/test_<name>.py`)

See the Phase A report (item 5) and each brief's **Figures** line. Every
script: values in functions, writes `figdata/out/bachelor-2-<name>*.dat` with
`figdata/_table.py`; `make figdata Y=bachelor-2` must leave no diff; tests at
defining points.

## Conventions decided in Phase A

- Ledger ids `<family>:<topic>`; families planned: `ipcc:` (reuse Book 2's
  rows; mint new ones in the same family after grepping), `usgs:` (reference
  materials `usgs:bhvo2-sio2`, eruptions, hazards), `berger91:`, `bowen:`,
  `robie95:`, `lodders:`, `gale13:`, `schmid04:`, `mckenzie78:`, `cpc:`,
  `gvp:`, `noaa:`, `lit:` for single papers (`lit:<author><year>-<topic>`).
  Grep `sources/data_ledger.md sources/ledger/` before minting.
- **check_ledger trap (Book 2):** every source KEY must be in the SAME ledger
  file's Sources table. To use another book's number, cite its ROW id in a
  `% ledger:` comment; never cite its key from a `book4.md` row.
- Labels `<type>:b2:<slug>:<name>`; methods `met:` (not `meth`).
- Qualified forms for sister-series homographs (Sync 1 rule): see
  `DEFINITIONS.md` contested table and the BRIEFS homograph table.
- Varden Hills: `from figdata.shared import region` (never edited); ch. 20
  and ch. 31 use it.
- Weekend problems: invented settings, named final numbers listed in each
  brief; final values fixed when the chapter's figdata runs.

## Scratch layout (`/tmp/claude-1000/-home-bvirrion-repositories-one-course/073e8d3d-6c62-4a98-8f56-8a0346dd7a8a/scratchpad/book4/`)

- `harvest/` --- Phase A term harvests (school, bachelor, sister series).
- `gen/defs.txt`, `gen/defs_table.md`, `gen/allindex.tsv` (7,063 sister/series
  index entries), `gen/planidx.tsv` (Book 2/3 plans) --- re-run the cross-check
  loop in the transcript if terms change.
- `tools/` --- copied from Book 3's scratch and retargeted to Book 4:
  `render.sh <outdir> <dpi> pages...` (fresh dir per render),
  `where.sh <pattern>` (pages containing text), `shrink.sh in out [w]`,
  `commons.py` (Commons imageinfo/extmetadata, UA without e-mail),
  `ledger.py` (appends to `sources/ledger/book4.md`), `prog.py`.
  Read each before first use (they were written for Book 3).
- `ai/ai_nofallback.py` --- OBSOLETE since Sync 2: use the SHARED
  `tools/ai_images.py` (its fallback was removed).
- `build-phaseA.txt` --- latexmk output of the Phase A build.

## Traps (inherited; add new ones as met)

From the batch file, Book 1 reconciliation and Book 3's PROGRESS:

- omfigure has no counter: never `\cref{fig:...}` (prints "Section");
  write "the figure below". No `\cref` across books.
- Pics are sized in cm: inside an axis use axis cs units for scale bars;
  decorations misplace marks on paths with jumps (precompute teeth); orient
  traced lines before side symbols; dip arcs as parametric plots; error-bar
  options on `\addplot`; map labels `\scriptsize` with 75--80 % white fill.
- siunitx: bold named number `\textbf{\qty[text-series-to-math=true]{..}{..}}`;
  `\qty[uncertainty-mode=separate]{7 \pm 1}{km}`; `$\ang{304}\pm\ang{3}$`;
  `\qtyproduct{500 x 200}{km}`; inline 3-vectors overflow -> aligned display.
- `\pgfmathsetmacro{\mu}` overwrites math `\mu`; TikZ `"$\theta$"` quotes trip
  gate 7 -> `pic text={$\theta$}`.
- `tools/chem.py` cannot read decimal subscripts -> `% ce-unbalanced-ok` + a
  test.
- pgfplots xticklabels with `$\to$` fail; nodes near coords inner sep vs
  marks; `booktabs`, `pgfplotstable`, `groupplots` NOT loaded (use `\hline`,
  separate axes).
- Non-floating omfigures leave half-page gaps: move the following paragraph
  before the figure; unbreakable boxes with photos cause gaps; a breakable
  problem box pushing a table -> blank page.
- Map fills with several rings: `nan nan` rows + `unbounded coords=jump`.
- Never LaTeX through an unquoted bash heredoc (use `<<'EOF'`).
- Index of exactly one page -> transient Overfull \vbox 21.8pt (goes away).
- Solutions from ROUNDED printed data; re-read each answer against its
  question; "CCD" homograph (charge-coupled device vs carbonate compensation
  depth).
- Gate 7 rejects curriculum words incl. "programme(s)", "collège", "lycée",
  "French"/"France" + school words; 7b imperative field activities; 7c policy
  wording (warning); 7d `dated` box needs its year. Never name a scientist's
  university ("a Geological Survey", "a research institute").
- Wiley/AGU PDFs are bot-walled (Book 2): Katz et al. 2003 (G-cubed),
  Ferry & Spear, AGU papers -> find an open restatement, an author copy on a
  public repository, or the publisher's open abstract page with the numbers;
  else drop to another open source. DSDP Initial Reports are free PDFs.
- protect.py masks `\pageref`, `\nameref`, `\omwx{}`, inline `\tikz`.
- Killed latexmk: delete the entry's `.aux .toc .out .fdb_latexmk` in
  `build/` (single files, no wildcard) and rebuild.
- No wildcard `rm`, ever, even in scratch: write renders into a fresh
  subdirectory.

## Open items for the sync (from the Phase A report)

1. Contested: δ value/fractionation factor (recall chemistry); partition
   coefficient + compatible/incompatible in ch. 3; ternary diagram in ch. 7;
   Clapeyron slope (of a reaction); Rossby wave in ch. 22; ice--albedo feedback
   (Y3) vs Book 4 needs; Mg/Ca (proxy) vs palaeothermometry; remaining carbon
   budget; disaster risk / geological hazard / exposure.
2. Chapter change proposed: compatible/incompatible element moves from ch. 8
   (OUTLINE text) to ch. 3 (term ownership only; ch. 8 keeps the
   fractionation laws).
3. Style-file requests (append-only, at the sync): see the Phase A report
   item 4.
4. Defects to report: see the Phase A report item 9.
