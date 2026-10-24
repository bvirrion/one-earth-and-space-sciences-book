# PROGRESS --- Book 2

Resume from this file alone: read `sources/BATCH_BOOKS_1-5.md` (binding), then
`BRIEFS.md` (per-chapter plan), `DEFINITIONS.md` (term table), this file.

## State (2026-10-23)

- **Phase A done**; **Sync 1 received** (rulings in "Sync 1 rulings" below).
  **Phase B done** (all 28 chapters). **Phase C done** (2026-10-23): term
  links unwrapped, applied, idempotent (dry run 0); 2199 links, 281 linkable
  terms, 135 distinct targets; `tools/term_config/book2_en.py` curated (STOP
  + EXTRA_PROTECT, capitalised harvest checked); the defined-twice
  "batholith" resolved (g12.04 owns it); whole book re-checked on contact
  sheets (16 sheets, 362 pages) with no new defect; solutions spot re-read
  (g11.03, g12.09) correct; 0 AI stubs, every AI image JPEG; gates green for
  grades 10--12; nullfont log noise diagnosed (blank lines in pgfplots tables;
  own cyclone tracks fixed, the rest comes from shared geo tables).
- Entry file builds 0/0/0, **362 pp** (target ~330, +10 %).
- **SEND-BACK (2026-10-23, coordinator, binding; Sync 2 in the batch file)**
  — Phase C reopened, three items, in this order:
  1. re-source every WIKI*/WIKIBOOKS* ledger source/row (36 sources, ~37
     rows; ids `b2wiki:*`, `wiki:*`, `wb:*` renamed, references in
     g12.02--g12.09 tex comments and figdata docstrings updated) to a fetched
     primary/agency/open-textbook source, or drop the number and list it
     EXCLUDED; landing check `grep -ci wiki sources/ledger/book2.md` (Commons
     photo-credit lines also match "wiki": flag in the addendum);
  2. scripted re-read of ALL 448 exercise/problem solutions against their
     questions, every number recomputed; slips logged below ("Solutions
     re-read log");
  3. per-figure 130-dpi check of every page with a figure (not contact
     sheets), 300 dpi for side-dependent symbols; FIGCHECK one line per
     omfigure and per includegraphics (201 lines for 205 omfigures: 4
     missing); fixes logged;
  then rebuild 0/0/0, gates g10--g12, link dry run 0, Phase D addendum.
- **Send-back status (2026-10-23): items 1--3 DONE** (logs: "Sync 2
  re-sourcing log", "Solutions re-read log", "Figure check log"); rebuilt
  0/0/0 362 pp; linker dry run 0 (2198 links, 281 terms); gates g10--g12
  OK; tests g10--g12 181 pass; ai_stubs 0; check_ledger OK (Book 2: 282
  sources, 367 rows); problem numbering OK. **Phase D addendum sent
  (handback) — Book 2 is waiting for the coordinator.** Unused file left in
  place for the user: `images/book2/ai/g10-research-ship.jpg` (replaced by a
  NOAA photograph in Phase B).
- Search budget used: **~59 web searches, ~440 fetches** (of ~600; GWS: 44 tiny API answers).

## Chapter status

| ch | status | pages | notes |
|---|---|---|---|
| g10.01 `measuring-the-earth` | **done** | 11 + sol. | 15 exos, 20-q problem (~0.2 mm); 8 figures FIGCHECKed |
| g10.02 `habitable-planet` | **done** | 8 + sol. | 15 exos, 18-q problem (about 60 K); 6 figures FIGCHECKed |
| g10.03 `earth-energy-budget` | **done** | 11 + sol. | 15 exos, 20-q problem (about 0.1 %); 9 figures FIGCHECKed |
| g10.04 `why-clouds-form` | **done** | 10 + sol. | 15 exos, 20-q problem (about 1.5 km); 7 figures FIGCHECKed |
| g10.05 `storms-and-cyclones` | **done** | 9 + sol. | 15 exos, 20-q problem (one part in 400); 9 figures FIGCHECKed; IBTrACS `# Book 2:` block in tools/fetch_data.py |
| g10.06 `layered-ocean` | **done** | 10 + sol. | 15 exos, 20-q problem (2.3 times, Peru vs gyre); 8 figures FIGCHECKed; WOA23 columns in the `# Book 2:` block |
| g10.07 `soil-formation` | **done** | 10 + sol. | 15 exos, 20-q problem (about 660 years); 8 figures FIGCHECKed; EXCLUDED: Goldich stability order (no primary source fetchable; only 'quartz survives' told) and tropical weathering depths (no fetchable source: schematic only) |
| g10.08 `drainage-basins` | **done** | 11 + sol. | 15 exos, 20-q problem (26 % in 30 years); 10 figures FIGCHECKed; USGS 01646500 peaks + 1996 daily values in the `# Book 2:` block; Varden basin by priority flood + D8 on region.py (50 m, tested); Amazon from Callede 2010 (Crossref abstract), Mississippi from Kammerer 1990; EXCLUDED: world basin areas (Amazon, Congo: no primary source fetched; only the Mississippi's is printed), gauging durations and logging intervals (unsourced, removed) |
| g10.09 `freshwater-resources` | **done** | 9 + sol. | 15 exos, 20-q problem (Aral level fell ~0.8 m in 1987, close to a metre); 8 figures FIGCHECKed; stocks USGS/Shiklomanov, cycle Trenberth 2007 via Trenberth & Asrar 2014 (WCRP copy), Aral table Gaybullaev 2012 (open access), Nubian ages Sturchio 2004, High Plains McGuire 2017; EXCLUDED: Trenberth 2007 original (AMS/OpenSky bot-walled: the WCRP reprint figure used), Gleeson 2016 modern-groundwater share (no abstract fetchable), groundwater flow speeds (unsourced, removed), Aral 1960 'steady' claim (the 1960 row is not in balance: not asserted) |
| g11.01 `drift-to-spreading` | **done** | 12 + 2 sol. | 15 exos, 20-q problem (oldest floor beside Africa at 30 S about 130 Myr; 140 by constant-rate extrapolation); 9 figures FIGCHECKed; `grade-11-seafloor-age` (Seton 2020, CC BY 4.0) in the `# Book 2:` block; CK95 table via the WHOI deep-tow file (Internet Archive); DSDP Leg 3 Table 5 (IR vol. 3 ch. 13, free PDF); EXCLUDED: Earth's field strength in nT and typical anomaly amplitudes (no fetched source: dropped), Hess's ship command (unsourced, removed), 'lavas everywhere agree' (unsourced), heat flow at ridges (not sourced; left to g11.05) |
| g11.02 `seismic-structure` | **done** | 10 + 2 sol. | 15 exos, 20-q problem (Moho about 30 km); 7 figures FIGCHECKed; PREM ray tracer (2 km shells) gives P shadow 98.5-143.8 deg (Gutenberg 105-143), P/S times within 2 % of AuSPASS empirical times (tested); history via Kayal (GSI, USGS-hosted PDF), SRL 2007 + geotech.hr for Mohorovicic, Herak 2010 (Crossref); DEVIATION from brief: no Lehmann history box or portrait (Book 1 g6 already prints both): recalled, then the inner-core rays computed; EXCLUDED: Mohorovicic's own 54 km depth (only on Wikipedia; not printed), the 410/660 'phase change' cause (no source fetched: steps only told), Oldham's and Gutenberg's first names (not in a fetched source) |
| g11.03 `lithosphere-asthenosphere` | **done** | 10 + 2 sol. | 15 exos, 20-q problem (crust under Tibet about 70 km: Airy 67.8, receiver functions ~70); 6 figures FIGCHECKed; geotherm model (Davies 2010 continental mean, Roy 1972 eastern-US a/b and conductivity, Porter-Reid 1300 C adiabat, Katsura 2010 0.45 K/km) and Hirschmann 2000 solidus (Crossref abstract); hypsometry from ETOPO1; Christensen-Mooney 1995 crust 41.1 km / 2830 kg/m3; heat flow, Fourier's law and radiogenic heat left to g12.06 (forward ref, no definitions); EXCLUDED: CRUST1.0 (no licence statement on the distribution page: dropped per Sync 1 ruling, also for g12.01), an Airy prediction of ocean depth (simple Airy with these densities gives ~7 km, not 3.7: not printed), flexure numbers (none sourced: told only), Moho 'thousands of years' asthenosphere time scale (unsourced: 'long spans of time') |
| g11.04 `plate-motions` | **done** | 11 + 4 sol. | 15 exos, 20-q problem (Pacific over the Hawaiian hotspot about 9 cm a year; through-origin fit 91 km/Myr); 8 figures FIGCHECKed; `grade-11-gnss-mkea`/`-wtzr` (NGL IGS20 tenv3, monthly means) in the `# Book 2:` block; NNR-MORVEL56 Table 1 (Argus 2011, McGill course copy of the PDF) as ledger rows nnr56:poles/rms/data; Clague-Dalrymple 1987 Table 1.4 read from the scanned USGS PDF (no text layer: rendered and read); bend from Sharp-Clague 2006 abstract (Crossref): about 50 Ma near Kimmei, NOT the brief's 47 Ma; plate speeds with/without slabs (nnr56:rms, India left out of both groups) printed for g11.06; India-Eurasia 45 mm/yr at 85E 28N computed for g12.02; EXCLUDED: 'stations on one plate keep their distances to a mm or two' (unsourced, replaced by the model-vs-station comparison), 'argon-argon' as the 2006 method (only in a search snippet, not in the fetched abstract), azimuth of the chain's trend (no coordinates sourced: told as west-north-west), hotspot motion (not sourced: not claimed) |
| g11.05 `ocean-ridges` | **done** | 10 + 3 sol. | 15 exos, 20-q problem (a piece of East Pacific Rise floor at 64 Myr lies about 5.3 km down); 8 figures FIGCHECKed; figdata `ridge_melting` (Katsura adiabat 0.45 C/km + Hirschmann 2000 dry solidus: onset 54 km for Tp 1300, 85 km for Tp 1400) and `depth_age` (ETOPO1 1-degree x Seton 2020 ages, 5-Myr medians and quartiles); sources: WHOI 1977 history page and vents page, White-McKenzie-O'Nions 1992 (Crossref abstract), IODP Exp 309/312 summary (tamu copy; publications.iodp.org 403), Parsons-Sclater 1977 (UCSD PDF), Buck-Lavier-Poliakov 2005 (LDEO PDF), USGS EHP glossary, geology.com rock pages, Asimow et al. 2001 (Caltech PDF), four Commons photos; DEVIATION: the onset depth of melting is printed as the model's result (no fetched source gives a published onset depth), tested for consistency; EXCLUDED: 'thirteen frames', 'evening of 15 February', ANGUS thermometer sensitivity, black smokers 'two years later' (all from memory, not in the fetched page: removed), abyssal hills 'most common landform' (unsourced, removed), height of the fast-ridge axial high (no number fetched: told without one), melt fractions (not sourced: 'a small fraction'), heat flow at ridges (owned by g12.06) |
| g11.06 `subduction-zones` | **done** | 10 + 3 sol. | 15 exos, 20-q problem (Pacific floor takes about 6 million years from the Tonga Trench to 670 km); 6 figures FIGCHECKed; figdata `slab_sections` (ComCat M>=6 sections across Tonga, Andes, Japan, profiles from PB2002 steps, ages from Seton 2020, world map by depth class, plate-speed bars from NNR-MORVEL56); sources: Forsyth-Uyeda 1975 (OUP abstract), Frohlich 1987 (McGill PDF; Wadati/Benioff history), USGS Tohoku event GeoJSON (tectonic summary and impact text), Hacker et al. 2003 (Crossref abstract: eclogite ~6 % denser than harzburgite), Bevis 1995 (Crossref title only), three Commons photos; DEVIATIONS: 670 km (PREM, as g11.02) instead of the brief's 660; named number about 6 Myr, not 5 (PB2002 Tonga rate 168 mm/yr over a 1015 km straight path); the Japan section is too sparse at M>=6 (5 events between 100 and 600 km): Tonga + Andes printed, Japan used only for its rate and floor age; EXCLUDED: 'fastest convergence on Earth' (unsourced), 'largest earthquakes on Earth happen on the plate-boundary fault' (unsourced: replaced by the 2011 example), arc 'where the slab is about 100 km deep' (owned and to be sourced in g12.04), 'back-arc opening into a new ocean' (Bevis title only says extension), the caption claim that the shallow far events are back-arc events (unsourced) |
| g11.07 `minerals` | **done** | 11 + 3 sol. | 15 exos, 20-q problem (the density of the granite, about 2.64 g/cm3); 7 figures FIGCHECKed; figdata `mineral_density` (element mass shares of the crust from Rudnick-Gao 2014 oxides and CIAAW weights; rock densities as volume-weighted means of webmineral mean densities; tests 6); sources: Rudnick-Gao 2014 (georefdatar CSV; the UMD PDF was 404), Tulane EENS 2110 pages (silicates, physical properties, inosilicates, optics), webmineral (formulas, densities), USGS OFR 91-570-A (Sierra Nevada densities, weighing formula), seven Commons photos (GeoDIL CC0, Chmee2 and Rygel CC BY-SA 3.0); DEVIATIONS: hardness and the Mohs scale are Book 1's (def:g6:rocks-and-minerals:hardness): recalled, not redefined (the brief listed `...:hardness`); a second proposition added (counting the oxygens, 4 - n/2 per silicon); the hand-specimen example uses another granite (2.59) so the problem's number is not given away; EXCLUDED: the chart of Mohs number against absolute hardness (no fetched source gave absolute values: only Wikipedia-derived pages, mutually inconsistent), 'holes left by gas bubbles' in the basalt thin section (the specks are black in plane light: told as opaque), felsic/mafic (g11.08's terms) |
| g11.08 `igneous-rocks` | **done** | 9 + 2 sol. | 15 exos, 20-q problem (the 20-m sill solidifies in about 2.6 years); 7 figures FIGCHECKed; figdata `dyke_cooling` (explicit enthalpy finite differences of a basaltic sheet cooling by conduction, Delaney 1986 parameters: 1150 degC magma, 950 degC solidus, 50 degC host, 900 MJ/m3 heat of crystallisation, rhoC 2.5 MJ/m3/K, kappa 1e-6; tests 6: erf solution without latent heat, b^2 scaling, factor ~3 from latent heat as Delaney says, margin first, grid convergence, contact 690 degC = Delaney's analytic value); sources: Tulane EENS 1110 igneous notes (silica classes, textures, cooling times, intrusions), USGS OFR 86-444 (Delaney), Earle Physical Geology 3.3 (CC BY 4.0; Bowen series, magma oxide table), Carnegie GL history (Bowen), 11 Commons photos (GeoDIL CC0, USGS CC0, Bishop CC BY-SA 3.0); DEVIATIONS: named number about 2.6 years, NOT the brief's 'a few decades' (the conduction model with Delaney's parameters gives 2.61 yr for 20 m; decades only from ~60 m up); silica classes from Tulane/Earle (45-55-65-75 %), not IUGS TAS boundaries (no IUGS text fetched); 'microlitic' (a French term) told as fine-grained; Bowen series from Earle (CC BY) rather than Bowen 1928 itself; EXCLUDED: 'tens of thousands of columns, mostly six-sided' (only in another photo's description, not used), granite crystal size at El Capitan, El Capitan among the USGS-sampled plutons (not in the source) |
| g11.09 `fossil-fuel-geology` | **done** | 10 + 2 sol. | 15 exos, 20-q problem (the source rock entered the oil window about 117 million years ago); 6 figures FIGCHECKed; figdata `oil_window` (burial history of the invented Merrow Basin: seven sedimentation episodes incl. 500 m of erosion since 20 Ma, no compaction, constant geotherm 30 degC/km from 20 degC; exact crossings of 60/120 degC on the piecewise-linear history: 116.97 / 51.24 Ma, Tmax 140 degC at 20 Ma, 125 today; a hotter basin at 40 degC/km for an exercise: 127.5 / 86.7 Ma, before the 80-Ma trap; tests 7); sources: Earle Physical Geology 20.3 (CC BY 4.0; organic preservation, coal formation and rank depths, oil window 60-120 degC, migration, traps, salt domes, coal-bed methane), EIA 'Coal explained' (carbon by rank), Ryer and Langer 1980 via USGS record 70012373 (peat:coal 11:1), USGS DDS-60 ch. PS (Magoon and Schmoker 2000: petroleum system, overburden, burial history chart, 3-km maturity rule), USGS PP 1713 ch. 12 (kerogen definition), USGS Fact Sheet 2023-3028 (West-Central Coastal Province: rift, lake shales TOC to 20 % and 600 m, sag, >1 km Aptian salt seal), 5 Commons photos (St. John CC BY 2.0 x4, USGS PD), the AI platform from the g11 batch; DEVIATIONS: the hook shows plant fossils in carbon-rich shale from a coal mine, not a fern in a lump of coal (no such free photo found; the brief's candidate); 'anticline' told in prose with a forward reference, not defined (Sync 0: g12 mountain-building owns folds); 'passive margin' and 'rift' told in prose, not defined (no school owner; b1 owns them); the critical moment is named in prose, not defined; EXCLUDED: 'water and gases driven off as rank rises' (not in a fetched source), 'the bottom of a deep lake is poor in oxygen' (not in the fact sheet), the USGS undiscovered-resource figure (12.1 billion barrels; volatile, dated estimate, not needed), 'source rocks are dark because of their kerogen' (unsourced) |
| g12.01 `continental-crust` | **done** | 8 + 2 sol. | 15 exos, 20-q problem (the continental crust is about 0.4 % of the Earth's mass: 210.4e6 km2 x 41.1 km x 2830 kg/m3 = 2.45e22 kg = 0.41 %); 6 figures FIGCHECKed; figdata `crust_ages` (area-weighted histogram of the Seton 2020 1-degree ages, Mediterranean left out as in g11.01; oldest 192.5 Myr, 76 % younger than 100; tests 3, one checking agreement with grade 11); sources: Cogley 1984 (Crossref abstract: 210.4e6 km2, 41 %, 30.6 % submerged, 36 km, 7.2e9 km3, mean height 120 m), Bowring-Williams 1999 and Wilde 2001 (Crossref titles), UW-Madison 2014 news on Valley et al. (Jack Hills 4.4 Gyr), Tulane EENS 1110 deform/lect1/pltect (roots 35-40 vs 50-70 km, gravity anomalies, cratons, no subduction of continents), already-ledgered CM95, Rudnick-Gao, White 1992, Karplus 2019, Earle oxides, PREM; 3 Commons photos; DEVIATIONS: no thickness map (CRUST1.0 dropped per Sync 1: no licence) -> a bar chart of sourced thicknesses; the proposition is 'the mass of a thin layer' (m/M = 3f(H/R)(rho/rhobar)) instead of re-stating Airy, which g11.03 owns and proves (recalled by \cref); the example is a shelf identified with the method, not the Alps' root (no fetched source gives an Alpine Moho depth number: three Crossref abstracts checked, none quantitative); no separate root figure (g11.03's Airy figure); EXCLUDED: 'granitoid' (no fetched source defines it), 'shield' (Britannica bot-walled; only Wikipedia-derived pages), 'composition estimated from thousands of analyses' (unsourced), 'polished by the ice' (unsourced), the 'Acasta gneiss among lakes' scene (unsourced) |
| g12.02 `mountain-building` | **done** | 11 + 2 sol. | 15 exos, 20-q problem (India has travelled about 4,400 km north since the end of the Cretaceous: 39.38 deg x 111.2 = 4379 km, MULLER2022; 4530 in MULLER2019); 11 figures FIGCHECKed; figdata `india_drift` (GPlates Web Service past positions of 78E 20N and Lhasa in MULLER2022 + MULLER2019, 0-100 Ma every 5 Myr + 66, `grade-12-gws-*` keys in the `# Book 2:` block of tools/fetch_data.py, derived grade-12-gws-india.csv; 13 cm/yr 65-50 Ma, 4 cm/yr since 40 Ma, India-Lhasa convergence 1354 km since 50 Ma; today 45 mm/yr from grade-11 plate_velocities; tests 4), `fold_shortening` (e = 1 - cos theta, sine-fold arc length checked against the elliptic integral, Varden profile from region.py gives 2.19 %; tests 4), `alpine_belt` (ETOPO1 cells > 1500/3500 m and shallow M>=6 quakes in a -12..105 E, 18..52 N window; tests 2); sources: USGS This Dynamic Earth Himalaya page, Sakai et al. 2005 (summit limestone: trilobites, ostracods, crinoids, Ordovician; tectonic stacking), Liu et al. 2020 (ITSZ ophiolites = Neo-Tethys, 243 Ma gabbro), Najman and Li 2021 EGU abstract (collision 60/54/34 Ma debate), Earle 10.4/12.2/12.3 (CC BY), Tulane deform notes, Wikibooks Historical Geology (ophiolites, orogeny, suture), NGU terminology (nappe), Mueller 2019/2022 (Crossref abstracts), 4 Commons photos (NASA PD, Hullot CC BY 2.0, Heine CC BY-SA 3.0, Duchoiselle CC BY-SA 3.0); DEVIATIONS: palaeolatitudes from two published plate models through the GPlates Web Service instead of the USGS figure and Patriat-Achache 1984 (no abstract; the USGS figure is an artist's conception); the Alps are told through Earle (Africa-Eurasia) and the Glarus Thrust photo, not Europe-Adria (no fetched source names Adria); the Everest photo is the Columbia shuttle view, not an ISS view (its NASA description names Everest); a second statement (thickening H = H0/(1-e)) is told in prose; EXCLUDED: 'grey' summit limestone (not in the abstract), the Himalayas 'rising more than 1 cm a year' (USGS page claim, old and not needed), 'faster than any plate today' (rms speeds are plate means), 'dry valley' (wadi: not in the photo description), Adria and the Alpine oceans (unsourced), 'nappes stacked' in the Alps (only NGU's general statement used), magnetic stripes as the basis of the reconstructions (not in the fetched abstracts: 'many kinds of evidence, among them hotspot tracks') |
| g12.03 `metamorphic-rocks` | **done** | 10 + 2 sol. | 15 exos, 21-q problem (the kyanite schist crystallised about 25 km down: 0.70 GPa / (2830 x 9.81) = 25.2 km); 5 figures FIGCHECKed (P-T diagram, zones, foliation, 4 photos, aureole); figdata `al2sio5` (Holdaway and Mukhopadhyay 1993 Table 11, read from the rendered page since pdftotext garbled it: boundaries as straight lines between tabulated points, triple point recomputed 504.2 degC 3.758 kbar vs printed 504/3.75; lithostatic P = rho g z with 2830 kg/m3 and 9.81; geotherms 10/30/50 degC/km from 10 degC (Earle 7.3), crossings 574 degC 18.8 km, 340/6.6 and 553/10.9; tests 4); sources: Holdaway-Mukhopadhyay 1993 (minsocam PDF), Holdaway 1971 and Barrow 1893 (Crossref), Earle 7.1-7.5 (CC BY), Tulane metamorphic notes, Wikipedia Metamorphic zone (Barrovian sequence, rev 1369100779), 4 Commons photos (Geoloshe CC0, Churchard CC BY 2.0, St. John CC BY 2.0 x2); kyanite/andalusite/sillimanite densities from Book 3's row webmineral:polymorphs (comment only); DEVIATIONS: Holdaway-Mukhopadhyay 1993 instead of Holdaway 1971/Pattison 1992 (the 1993 paper is free and tabulates the boundaries; 1971 cited for history only); no marble photo (Book 1 g6 prints one): a slate micrograph and a kyanite schist instead; 'parent rock' is g10.07's term: recalled in prose, not \\emph'd; EXCLUDED: Barrow's date as 1912 (Wikipedia) -- the 1890s of Earle and the 1893 paper are used; 'micas need aluminium and potassium' (no fetched source gives mica compositions); 'growing is easiest across the push' (mechanism not in the sources); water 'escapes upwards'; Tulane's '300 MPa' lower pressure limit of metamorphism (not used) |
| g12.04 `subduction-magmatism` | **done** | 9 + 2 sol. | 15 exos, 20-q problem (the slab lies about 100 km beneath the volcanic front of NE Japan: 98 km by H = d tan(theta) and by the median depth of the deep events); 7 figures FIGCHECKed (St. Helens plume, world volcano map, NE Japan section, dry/wet solidus, arc schematic, andesite + granodiorite, Sierra Nevada panorama); figdata `arc_magmatism` (GVP 838 of 1214 Holocene volcanoes in a subduction setting; new Book 2 dataset grade-12-usgs-ne-japan, ComCat M>=4.5 1976-2025, 4155 events; slab fitted to 232 events deeper than 70 km, dip 19.98 deg; front Iwate 141.0 E, trench 144.12 E from the shared PB2002 table, 269 km; bin medians 116.4/98.15/80.35 km; dry solidus imported from grade-11 geotherm_solidus; tests 5); sources: USGS MSH 1980 page, Syracuse-Abers 2006, Kawamoto-Holloway 1997, Wang et al. 2020, Scholl-von Huene 2009, Stern-Scholl 2009 (abstracts via Crossref/OpenAlex), Earle 3.2, 4.3, 10.4, Tulane igneous/plate-tectonics notes, Wikipedia Granodiorite and Batholith (revision ids in the ledger), 4 Commons photos; DEVIATIONS: Kawamoto-Holloway 1997 and Wang 2020 for the wet solidus instead of Grove 2006 (MTU PDF redirected to a homepage); Scholl-von Huene and Stern-Scholl 2009 for the crustal budget instead of Clift 2009 (PDF served as HTML); no wedge geotherm drawn (no fetched source), the wet solidus drawn as the measured brackets only; Swanson's plume photo instead of the Austin Post photo (printed in Book 1 g4); Half Dome not called granodiorite (Wikipedia: quartz monzonite), Moro Rock specimen used; mantle wedge and solidus told in bold, not defined (wedge is a location, solidus a sister-series-style notion used once); the Pacific Plate speed of exercise 12 reuses g11.06's row usgs:tohoku (83 mm/yr); EXCLUDED: 'arc accretion welds island arcs to continents' (no fetched source: the paragraph now tells only continent collision and cratons, Tulane/Earle); 'composite cones built of alternating lava and ash' (not in Earle 4.3's fetched text); ash column '20-25 km above sea level' (only 'more than 24 km' is sourced); 'the shallow cloud is mostly the 2011 aftershocks' (replaced by the computed share: 1451 of 3622 shallow events east of 141.5 E are from 2011); Japan crustal thickness (the problem says 'taking the crust to be about 35 km') |
| g12.05 `destruction-of-mountains` | **done** | 9 + 2 sol. | 15 exos, 20-q problem (the mean elevation of a range halves in about 20 million years with rebound: tau = 1/(0.163 x 0.209) = 29 Myr); 7 figures FIGCHECKed (ISS Appalachians, rates bar chart, braided river AI, conglomerate, rebound schematic, decay curves, Varden unconformity); figdata `relief_decay` (rebound fraction 1 - 2830/3380 = 0.163; k = ln10/11 per Myr from Ahnert 1970; Mississippi budgets 52 and 19 m/Myr; world 43 m/Myr from 15.5 Gt/yr over 29.04 % of the sphere; Varden unconformity sampled from region.contact_elevation; tests 4); sources: Portenga-Bierman 2011 (GSA Today PDF), Ahnert 1970, Milliman-Syvitski 1992, Syvitski 2005, Meade-Moody 2010, Sella 2007 (abstracts via OpenAlex/Crossref), Earle 6.1 and 13.3, Wikipedia Mississippi River and Appalachian Mountains (revision ids), 2 Commons photos; DEVIATIONS: Ahnert 1970 calibrates the decay law (the brief named no source for it); the Mississippi replaces the Ganges as the worked budget (no free per-river table for the Ganges; Meade-Moody abstract and Wikipedia basin area are fetchable); the river bar chart became a chart of denudation rates (10Be compilation + two budgets) for the same reason; no sediment-plume photo; rebound 163 m per km eroded (g11.03's densities 2830/3380) instead of the brief's ~180 m (2700/3300, kept as exercise 8); the world budget uses Book 1's row syvitski:modern-flux (15.5 Gt/yr prehuman with bed load) to agree with Book 1, rather than Milliman-Syvitski's 20 Gt/yr (row ms92:global kept); EXCLUDED: 'the Appalachians were once as high as the Alps' (not in the fetched Wikipedia text; NASA caption says only 'much higher than the present range'); 'denudation rises with rainfall' (Portenga-Bierman: slope is the main regressor, Ahnert: precipitation has no noticeable effect); Ahnert's 'at least 18.5 Myr with isostatic compensation' (a partial-rebound model, not comparable with the printed full-Airy model; kept in the ledger only); 'the ice melted thousands of years ago' (no date in Sella's abstract); a precise age for the Sharon conglomerate |
| g12.06 `internal-heat` | **done** | 7 + 3 sol. | 15 exos, 20-q problem (radioactivity supplies about half of the Earth's heat loss today: 23.9/46.7 = 0.51); 6 figures FIGCHECKed (half-space heat flow, budget bars, isotopes back to 4.5 Ga, convection schematic, hot spring AI, Nesjavellir photo); figdata `internal_heat` (KamLAND 20.0 TW U+Th scaled by the mantle heat-release ratios of the Wikipedia isotope table: K-40 3.50, U-235 0.40, total 23.9 TW; secular 22.8; x4.54 at 4.5 Ga with U-235 + K-40 70 %; q = 490/sqrt(t) of Davies 2010 under 66.5 Myr; conduction across 2891 km at 1e-6 m2/s 265 Gyr; tests 4); sources: Davies-Davies 2010 (PDF), Vila-Fernandez 2010 (EGU abstract PDF), Wikipedia heat budget, geoneutrino, mantle convection, thermal diffusivity, KTB, Kola, geothermal energy, Nesjavellir (revision ids), 1 Commons photo; DEVIATIONS: KTB hook (9101 m, > 260 C against 250-300 expected at 10-14 km) instead of a deep mine, because Book 1 g6 owns the Kola hook; the named number is 'about half' (51 %) instead of the brief's ~40 % (the fetched KamLAND figure gives 23.9 of 46.7 TW); isotope half-lives and heat release from the Wikipedia table plus KamLAND, not the NNDC; no plate-model curve (Stein and Stein not fetched): the half-space law only, dotted beyond 66.5 Myr; no Larderello photo (Commons candidates carry the operator's logo); EXCLUDED: 'drill heads designed for rock hot enough to boil water' (flourish, removed), the Sun's 173,000 TW (not in a fetched source: problem question replaced), mantle mass and specific heat for a cooling-rate exercise (no ledger row: exercise replaced by the core heat-flow one), Kelvin's conduction age (left to g12.07), a Rayleigh number in print (row kept, not needed at this level), 'magma brings heat close to the surface' (fetched text says high-temperature resources approach the surface) |
| g12.07 `age-of-the-earth` | **done** | 7 + 3 sol. | 15 exos, 20-q problem (the Varden granite is 310 million years old: slope 0.004341, ln(1.004341)/1.3972e-11); 6 figures FIGCHECKed (Kelvin portrait, estimates chart, Varden Rb-Sr isochron, mass spectrometer AI, Canyon Diablo photo, Patterson lead isochron); figdata `isochrons` (Varden granite 310 Ma and schist 480 Ma exercise ratios rounded to 5 decimals, tested against region.UNITS; Patterson 1956 Table 1 with his constants, LS slope 0.6026 -> 4.58 Ga within his 4.55 +- 0.07; history of estimates; tests 5); sources: Wikipedia Age of Earth, Rb-Sr dating, Pb-Pb dating (revision ids), Patterson 1956 (ASU scan, fetched), Villa et al. 2022 IUPAC report (abstract: lambda 87Rb 1.3972e-11), Connelly 2012 (abstract: CAIs 4567.30 +- 0.16 Myr), Kelvin 98 Myr from the heat-budget row, 2 Commons photos; DEVIATIONS: Villa et al. 2022 (IUGS-IUPAC technical report) instead of Villa 2015, same recommended constant and openly abstracted; Dalrymple read through the Wikipedia summary (book not fetched); Phillips and G. H. Darwin told without a year (none in the fetched text) and left off the chart; the brief's 'S closed and open systems' schematic replaced by exercise 9 (open biotite) to hold the page budget; the lead slope-age relation admitted with a table rather than derived; EXCLUDED: Newton's 1687 '50,000 years' (garbled sentence in the fetched article), the Rutherford-Kelvin anecdote's direct quote beyond the clause 'provided no new source was discovered', numeric mantle and crust 87Sr/86Sr values (none fetched: the basalt's 0.7035 is region exercise data), Kelvin's conduction formula (Book 3 b1 works it with England et al. 2007) |
| g12.08 `early-earth` | **done** | 8 + 3 sol. | 15 exos, 20-q problem (the Earth's equilibrium temperature four billion years ago was about 237 K: 255 x 0.741^(1/4)); 6 figures FIGCHECKed (Dales Gorge BIF, young Sun twin-axis chart, Shark Bay stromatolites, BIF schematic, Sedona red beds, oxygen timeline with ICS eons); figdata `early_earth` (Gough 1981 eq. 1 with t_sun 4.567 Gyr, Teq from the grade-10 rows; oxygen schematic through the sourced bounds; eons via grade-7 time_scale.ledger(); tests 4); sources: Gough 1981 (ADS scan, equation read from the page image), Pavlov-Kasting 2002, Farquhar 2000, Gumsley 2017 (abstracts via OpenAlex), Wikipedia GOE, BIF, stromatolite, faint young Sun, red beds, prebiotic atmosphere, Karijini (revision ids), Book 1 row usgs:volcanic-gases, 3 Commons photos; DEVIATIONS: named number 'about 237 K' instead of the brief's 235 K (the computed value with t_sun 4.567 Gyr and today's albedo is 236.7 K); Gough's t_sun is 4.7 Gyr, the book uses 4.567 (the CAI age of g12.07), same 0.714 at birth; no Bekker 2010 or Lyons 2014 rows (no abstract text fetched for Lyons; Bekker's abstract adds nothing printed): BIF ages from Wikipedia; oldest stromatolites from Wikipedia (Allwood 2006 has no open abstract); 'oxygen through time' and the 'timeline' merged into one figure to hold the page budget; EXCLUDED: 'stacked by the thousand' (unsourced), 'above all by iron' (the GOE article lists iron, sulfur, hydrogen sulfide and methane together), the Moon-forming impactor's name and the 8000 K surface (not needed), ammonia and haze hypotheses, tidal heating (told nowhere), a date for the first red beds (Cloud's 'about this time' is too loose to print a number) |
| g12.09 `past-climates` | **done** | 13 + 3 sol. | 15 exos, 20-q problem (today's global warming is about twenty times faster than the warming out of the last ice age: 0.20 degC/decade = 20 degC/kyr against 6 degC/7 kyr = 0.86, ratio 23; 13-20 against the fastest phase); 11 figures FIGCHECKed (ice-coring camp AI, ice bubbles, 800-kyr twin-axis record, CO2-temperature scatter, Sunda shelf map, last 30 kyr, pollen SEM, Varden pollen diagram, forams, LR04, reference periods) + 2 tables; figdata `ice_age_records` (EDC x CO2 1639 pairs r = 0.917, 7.83 ppm/degC; EDC period 97.5 kyr; LR04 periods 98.5 and 41.0 kyr, means 4.15 vs 3.03 permil; LGM/early-Holocene means -9.39/-0.36 degC, 189.7/264.1 ppm; Sunda land 4.11 -> 7.16 million km2 at -130 m, world 29.0 -> 33.5 %; GISTEMP 1970-2025 trend 0.201 degC/decade; invented pollen; AR6 reference periods; tests 8); new Book 2 dataset grade-12-etopo-sunda (ETOPO1 0.1 deg via ERDDAP); sources: AR6 WG1 SPM A.2.1/A.2.2/A.2.4 and ch. 2 (Cross-Chapter Box 2.1, 2.3.1.1.1, 2.3.3.3, Table 2.1, Figure 2.34), Lambeck 2014, Hays-Imbrie-Shackleton 1976, Lisiecki-Raymo 2005, Jouzel 2007 (abstracts via OpenAlex), Wikipedia EPICA, Ice core, Proxy, Palynology, Foraminifera, Oxygen isotope ratio cycle, MPT, Milankovitch, Sundaland (revision ids), 3 Commons photos; DEVIATIONS: no ice-core section photo (Book 1 g9 prints the GISP2 layers; a bubbles photo instead); Tierney 2020 not used (AR6's assessed 5-7 degC range is the printed value); the 800-kyr record drawn as one twin-axis panel plus a scatter and a 30-kyr zoom so as not to repeat Book 1 g9's stacked panels; LGM map over the Sunda shelf with -130 m (middle of AR6's 125-134 m) and a new 0.1-degree ETOPO subset; named number 'about twenty times' kept, computed 23 (mean) and 13-20 (fastest phase); 13 pp of text instead of ~10 (11 figures): no cut, the chapter closes the book; EXCLUDED: 'CO2 amplified the orbital changes' (no fetched source: the text says only that a correlation cannot tell cause), 'eight glacial cycles' as a printed count (the text says 'eight or nine' from the warm peaks of the figure, EPICA's '8 previous cycles' was for 740 kyr), Greenland's Younger Dryas jump, Tierney's 6.1 degC, the 52 million km3 of extra ice (kept in the ledger only), the snowball Earth and Cretaceous hothouse (not AR6 reference periods) |
| g12.10 `climate-change` | pilot written 2026-10-22 (main session) | ~13 + 2 solutions | 15 exos 5/6/4 + 19-q problem; 56 term links; 10 figures FIGCHECKed |

Order of writing in Phase B: grade 10 → 11 → 12 (owner chapters before the
chapters that recall them). Gates after each chapter: `bash tools/gates.sh
grade-N`, `make test Y=grade-N`, `make figdata Y=grade-N`, latexmk on the
Book 2 entry file only (`nice -n 10`, never two at once).

## Page projection

28 chapters × ~11.5 pp ≈ 322 pp + ~16 pp front matter, credits and index ≈
338 pp, against the ~330 target. Checkpoints: after g10.08, at the end of
grade 10, after g11.07, at the end of grade 11, after g12.06, at the end. More
than 10 % under target at a checkpoint → restore depth before going on.

| checkpoint | chapters done | pages | projection | verdict |
|---|---|---|---|---|
| Phase A | 1 (pilot) | 55 (with placeholders) | 338 | --- |
| g10.02 | 3 | 76 | +23 pp for 2 ch. (11.5 each incl. sol.) -> ~345 | on target |
| g10.08 | 9 | 144 | +68 pp for 6 ch. (11.3 each incl. sol.) -> 144 + 19 x 11.3 ~ 359 | above target by ~9 %, not under: keep later chapters near 10 pp + sol. |
| end of grade 10 | 10 | 154 | +10 pp for g10.09 -> 154 + 18 x ~10.8 ~ 348 | on target (+5 %) |
| g11.07 | 17 (with the pilot) | 242 | +88 pp for g11.01-07 (12.6 each incl. sol., placeholders ~1 pp) -> 11 chapters left to write (g11.08, g11.09, g12.01-09; climate pilot done) at ~12 net -> ~374 | above target by ~13 %, not under: no depth to restore; aim the remaining chapters at ~9-10 pp + 3 sol. |
| end of grade 11 | 19 (with the pilot) | 263 | g11.08 + g11.09 added ~21 pp (10 + 9 pp of text, ~2 sol. each); 9 chapters left (g12.01-09) at ~11 net each over their 1-pp placeholders -> 263 + 99 ~ 362 | above target by ~10 %, not under: no depth to restore; keep g12 chapters at ~9-10 pp + 2-3 sol. |
| g12.06 | 25 (with the pilot) | 329 | g12.01-06 added ~66 pp (about 11 each incl. sol.); 3 chapters left (g12.07-09) at ~11 net -> ~362 | above target by ~10 %, not under: no depth to restore; keep g12.07-09 at ~9-10 pp + 2-3 sol. |
| g12.07 | 26 (with the pilot) | 339 | +10 pp for g12.07; 2 chapters left (g12.08-09) at ~10-11 net -> ~360 | above target by ~9 %, not under: no depth to restore |
| g12.08 | 27 (with the pilot) | 347 | +8 pp for g12.08; 1 chapter left (g12.09) at ~10 net -> ~357 | above target by ~8 %, not under: no depth to restore |
| end of Phase B (g12.09) | 28 (with the pilot) | 362 | +15 pp for g12.09 (13 text + 3 sol. over its 1-pp placeholder); all 28 chapters written | above target by ~10 %, not under: no depth to restore; Phase C only links, curates and re-reads |

## Conventions settled by the pilot

- Every climate statement with a likelihood or confidence is an AR6 WG1 sentence with its ledger row (SPM statement or chapter table); calibrated terms in italics.
- Record figures read `figdata/out/grade-12-climate_records-*.dat`; printed numbers come from its `numbers` table.
- `dated{2025}` box for the latest annual values.
- Physical science only: the one remark on choices says they are not questions of physics; no advice anywhere.
- `term_config/book2_en.py` EXTRA links the short forms (forcing, feedback, scenario, climate sensitivity).

## Conventions and traps for Phase B

- Math level: the math series has **no sine in grade 10** (sine/cosine are
  defined in math g11). The batch file allows trigonometry from grade 10 and
  physics g10 refraction already uses sine: g10 recalls sine/cosine/tangent of
  an angle in a right triangle as known, and **derives** the sine rule (not in
  the math series) from a triangle's height written two ways.
- Physics owns: density, pressure, waves/echo/refraction/Snell (g10), magnetic
  field (g11), isotope/half-life/decay law and the dating equation (g11/g12),
  black body/effective temperature/greenhouse effect/thermal conductivity (b2).
  Recall them; never define. Thermal conductivity is *used* in g12.06 as "the
  rock's thermal conductivity k" with no definition (physics defines it only
  in b2).
- Chemistry owns fossil fuel, greenhouse gas (g8), redox (g11), δ value (b3),
  aerosol (b3), residence time (b2, reactors: Book 2 defines the *water*
  residence time as stock/flux, a homograph to watch in the linker).
- Biology owns soil, humus, decomposer (g6), humidity everyday sense (g6),
  photosynthesis, ecosystem (g10), fossil (g9).
- Sync 0: g12 `mountain-building` owns fold/anticline/syncline (+ collision,
  nappe, ophiolite, suture). Book 3's b1 `geological-maps` also defines fold
  terms (re-found at university level).
- Varden Hills: import `figdata/shared/region.py`, never edit it. Granite
  310 Ma, schist 480 Ma; the isochron data in g12.07 must agree.
- Balanced equations already checked: feldspar hydrolysis
  `\ce{2KAlSi3O8 + 2CO2 + 11H2O -> Al2Si2O5(OH)4 + 4H4SiO4 + 2K+ + 2HCO3-}`;
  iron oxidation `\ce{4Fe^2+ + O2 + 10H2O -> 4Fe(OH)3 + 8H+}`.
- g12 AI batch launched 2026-10-22 (4 images: braided river, hot spring, mass spectrometer, ice-coring camp; `<scratch>/ai/batch-g12.txt`, log `batch-g12.log`).
- AI images: `python3 tools/ai_images.py --book 2 batch.txt --work <scratch>/ai`
  from the repo root, detached; one batch per grade (~2 per chapter); JPEG only;
  grey stubs via `tools/ai_stubs.py` until then.
- Scratch: `/tmp/claude-1000/-home-bvirrion-repositories-one-course/073e8d3d-6c62-4a98-8f56-8a0346dd7a8a/scratchpad/book2/`
  (`sister_harvest.tsv` = sister-series term harvest, 3218 rows; `prov/`).
  Renders go to fresh subdirectories; never wildcard-delete.

## Sync 1 rulings (2026-10-22)

- Book 1 keeps, Book 2 recalls: hardness/Mohs (g11.07 adds cleavage,
  structure, silicate tetrahedron); crust/mantle/core/outer/inner core (g11.02
  owns Moho, CMB, seismic evidence incl. Lehmann); fault, unconformity,
  seismometer (B1 g7); temperature anomaly, topographic map, contour line,
  contour interval (g9); convection cell, environmental lapse rate, ice age
  (g8); weathering (g5).
- Granted to Book 2: P/S wave (g11.02); normal fault (g11); reverse fault,
  thrust (g12); fold/anticline/syncline (g12); mantle convection (g12, recall
  convection cell first); chemical weathering, hydrolysis, clay (g10);
  adiabatic cooling, dry rate (g10); glacial/interglacial (g12); exoplanet,
  latent heat (g10); lithostatic pressure (g12), sedimentary basin (g11),
  denudation rate, detrital rock, diagenesis (g12); all else in DEFINITIONS.md.
- No definition: δ18O read as told; equilibrium temperature fine, black-body
  law admitted.
- Homographs for term config: humidity, dew point, residence time (phrase
  level only).
- `tools/fetch_data.py`: ONE `# Book 2:` block at the end, ids start with the
  year, licences verified and recorded; CRUST1.0 and seafloor age: small
  derived tables only; unclear terms -> drop, use a sourced table/schematic.
- Style (end of `styles/oneearth.sty`): `lith gabbro|peridotite|eclogite`,
  `omHypsLandA-F`, `omHypsSeaA-D`, `\omwx[scale]{name}` / `pic {omwx=name}`,
  `pic {puffycloud}`, `pic {compassrose}`.

## Traps met in Phase B

- Gate 7 bans "France/French" in printed text (also in captions/history
  boxes): say "an expedition from Paris", "the Academy of Sciences".
- Photo credits: row in `images/book2/CREDITS.md` + `\item Ch.~N` in
  `frontmatter/image-credits-book2.tex`, inserted before the `Ch.~28 (climate
  change)` item. Chapter numbers: g10.0k = k, g11.0k = 9+k, g12.0k = 18+k.
- Ledger rows: `scratch/bin/ledger_add.py add.txt` (S|key|source|url and
  R|id|qty|value|unit|key|date) from the repo root; grep all ledgers before
  minting a `nasa:` id (another book uses `nasa:earth-perihelion-longitude`).
- `\parsec` is a unit macro: `\qty{1.30}{\parsec}`.
- Commons thumbnails can come back larger than requested: check size,
  downscale with ffmpeg -q:v 3.
- IAPWS: `iapws.org/documents/release/*.download` URLs work; SuppSat is
  scanned (coefficients read from a 300-dpi render).
- Solutions use the ROUNDED numbers the chapter prints.
- `omfigure` has NO counter: never `\label{fig:...}` / `\cref` a figure (it
  prints the section number). Refer to figures in prose ("the diagram above").
- Scaled pics (`\pic[scale=..]`) need `transform shape` (gate check_pic_scaling).
- No booktabs: tables use `\hline` (as the pilot).
- `\qty{x}{}` with an empty unit: use `\num{x}`.
- AMS Glossary blocks fetches (403): derive rates from first principles
  (g/c_p; dew-point fall from the IAPWS curve) in the figdata script instead.
- AI images for grade 10 are generated (`images/book2/ai/g10-*.jpg`, 9);
  reviewed and used: surveyor, snow-and-ploughed-field, cold-glass,
  valley-fog, flooded-street. Still to review: research-ship, ploughed-rills,
  river-flood-meadows, hand-pump-well.
- IBTrACS: the FIRST record of a storm is often its disturbance stage (153
  "genesis" points within 5 deg of the equator). Genesis = first fix with USA
  wind >= 34 kt (lat34/lon34 in the derived storms table): 24 within 5 deg.
- AMS journals and PubMed pages are 403/cookie-walled: abstracts via the
  Crossref API (`api.crossref.org/works/<doi>`) or Europe PMC REST.
- TikZ spirals: `cos(a+t)` with a shrinking radius is an ANTICLOCKWISE inflow
  (NH); the first draft used `a-t` and drew a Southern-Hemisphere storm.
- pgfplots `\legend{a, 5.5 N, b}` splits at every comma: brace each entry.
- WOA23 via THREDDS OPeNDAP ASCII: brackets must be URL-encoded (%5B %5D),
  else curl returns nothing; one column per site and variable (~3 kB).
- pgfplots bars on a log axis hang from 10^0 unless `log origin=infty`.
- A pgfplots table column with quoted labels containing spaces breaks the
  parser: write numeric indices and put the labels in xticklabels.
- Mindat and encyclopedia.com are 403/cookie-walled; webmineral.com works for
  formulas and molar masses; PNAS 403, PMC article pages work.
- Unsourced throwaway clauses ("most of them over land", "surges cause most
  of the damage") creep into prose: grep each new chapter's sentences with a
  number or a superlative against its ledger rows before the build.
- `\foreach \x/\y in {...} {\fill (axis cs:\x,\y) ...}` inside an axis dies
  with "Undefined control sequence" (expansion is deferred): write the
  commands out, or use `\pgfplotsinvokeforeach`.
- D8 routing on a cropped map: if every edge cell is a sink, a one-cell strip
  along the edges falls outside the basin and the traced divide runs along the
  frame. Let an edge cell drain inward when it has a lower neighbour; only an
  edge cell with none sends its water off the map.
- A boolean basin mask traced at 100 m gives staircase divides that
  Douglas-Peucker cannot smooth; 50 m with tolerance 30 m reads well.
- Érudit (doi 10.7202/...) serves a bot wall; Crossref's API returns the
  abstract (`api.crossref.org/works/<doi>`, field `abstract`).
- `omfigure` is a minipage, not a float: a `\label` after its caption takes
  the current section's number, and `\cref` prints "Section 13.1". Refer to
  in-text figures in words ("the map below"), never by label.
- Dense monthly GNSS points hide a dashed fit line drawn over them: state the
  rates in the text instead of drawing the line.
- The NGL IGS14 tenv3 path is dead; the IGS20 path is
  `geodesy.unr.edu/gps_timeseries/IGS20/tenv3/IGS20/<ST>.tenv3`; position =
  integer part (e0, n0) + fraction (east, north) columns, in metres.
- USGS PP1350 chapter PDFs are scans with no text layer: render the table page
  with pdftoppm at 150 dpi and read it; write the transcription into the
  ledger row and test the script's table against it.
- Two pgfplots/TikZ polygons that meet along a line (crust over sea, two
  rock layers) leave a white hairline seam at 130 dpi: draw each section as
  ONE polygon from the surface down.
- Water's critical temperature is 374 C: a question asking whether 400 C
  vent water "can boil" at some depth is ill-posed (supercritical at any
  pressure). Ask about the pressure instead (above 22.064 MPa nothing boils).
- Memory-filled history details (frame counts, dates of the evening, sensor
  sensitivity, "two years later") slip into history boxes: check every one
  against the fetched page, as for numbers.
- PB2002 steps carry the relative plate velocity of each boundary step
  (`vel_mm_a`): the convergence rate at a trench comes straight from the shared
  data (Tonga 104-237 mm/yr, increasing northward). The step's first-named
  plate lies on its left: for `A/B` (B sinks) the overriding side is strike - 90.
- At M >= 6 the Japan slab below 100 km holds only five events in a 300-km
  band: a slab section needs a dense deep zone (Tonga, Andes) at this catalogue
  threshold.
- My own ledger rows can carry memory errors too: the Frohlich figure caption
  says January 1927, I had typed July. Re-read the fetched text when writing a
  row, not only when writing the chapter.
- pgfplots `ybar` with two series offsets them side by side: `bar shift=0pt`
  when the series are complementary (one is zero where the other is not).
- USGS ComCat event GeoJSON (`fdsnws/event/1/query?eventid=...&format=geojson`)
  carries the event page's tectonic summary (`general-text`) and impact text:
  usable when the event page itself is JavaScript.
- USGS NWIS: site metadata (drainage area) from
  `waterservices.usgs.gov/nwis/site/?format=rdb&sites=<id>&siteOutput=expanded`;
  annual peaks are by water year (October-September): label them so.
- pgfplots `nodes near coords` on a LOG axis print ln(value): use
  `point meta=rawx` (or rawy), and `nodes near coords align={horizontal}` for
  xbar charts.
- Never wait for a build with `pgrep -f latexmk...`: the other agents' builds
  match too. Run latexmk in the foreground with the long tool timeout.
- The Book 2 log carries ~4200 harmless lines "Missing character: There is no
  ` in font nullfont!" after PGFPlots table reads (from g10.05 on): nothing
  printed, gates clean; to look at in Phase C.
- Source keys are per ledger file: a key another book already has
  (SYVITSKI-2005 in book1.md) must get a Book 2 twin (SYVITSKI-2005-B2);
  ledger_add skips it silently and check_ledger then fails.

## Open items (for the sync or early Phase B)

- New datasets to add under `# Book 2:` in `tools/fetch_data.py` (ownership
  per the batch file; licence and size to verify on fetch): IBTrACS v04r01
  since 1980 (g10.05), WOA23 three profiles (g10.06), USGS NWIS peaks + one
  water year of daily values for one station (g10.08), seafloor age grid
  (g11.01, g11.05, g12.01), NGL GNSS tenv3 for two stations (g11.04),
  CRUST1.0 1° thickness (g12.01). Optional: CERES EBAF zonal means (g10.03;
  fallback a qualitative schematic).
- Style requests: `lith peridotite`, `lith gabbro` (perhaps `lith eclogite`)
  in `styles/oneearth.sty` for cross-book consistency; until then inline
  `om lith={...}{...}`.
- Contested terms: see BRIEFS.md, last section (16 points), awaiting the sync.
- Weekend-problem final numbers marked "computed" in BRIEFS.md are fixed when
  the chapter's script runs; the named quantity is fixed now.
- A thin vertically magnetised layer gives EDGE-dominated anomalies over wide
  blocks (an infinite uniform sheet has no external field): the profile's sign
  still follows the polarity (tested at block midpoints) but the text must say
  so. Sample a fast-ridge profile at <= 0.5 km or it looks jagged.
- A colour bar drawn with `addplot graphics` in an axis with `height=1.6cm`
  came out as a hairline (labels eat the height): use `scale only axis` and an
  explicit small height.
- Wiley/AGU PDFs are bot-walled; the CK95 chron table is the WHOI deep-tow
  `ck95.txt` (Internet Archive `id_` URL gives the raw file). DSDP Initial
  Reports chapters are free PDFs at deepseadrilling.org.
- EarthByte age grid 2020.1: the 6' `.grd` is NetCDF-3 (scipy reads it); the
  NetCDF-4 `.nc` would need netCDF4/h5py (not in the venv).
- Ray tracing in thin shells (g11.02): flag a ray as "core" by the shell TOP
  (r2 < 3480), not the bottom, or rays turning in the lowest mantle shell count
  as core rays; drop rays reflected where the speed jumps up (return None), or
  ICB reflections fake a PKP minimum at 116.6 deg. A first-arrival curve taken by
  rounding distances shows spikes at the 220/400/670 km triplications: take the
  envelope over segments between neighbouring rays instead.
- check_ledger wants every source key in the SAME ledger file's Sources table:
  citing another book's key (e.g. NBI-LEHMANN, in book1.md) from a book2 row
  fails. Cite the other book's ROW id in a `% ledger:` comment instead.
- Overlap with Book 1: g6 `inside-the-earth` already tells Lehmann's story with
  her 1932 portrait and plots PREM P/S speeds; g11.02 recalls it (no second
  portrait) and adds the rays, the shadow zone and the density. Reported as a
  cross-book note for the Phase D report (SERIES_DEFINITIONS assigns
  "Lehmann's argument" to g11).
- g11.02's text said the continental Moho averages 30 km (USGS); g11.03 uses
  Christensen-Mooney's weighted 41.1 km. g11.02 now prints 41 km on average
  (30 stretched, >45 orogens, ~100 under the highest ranges) so the two agree.
- check_ledger: row ids are global across ledger files (katsura:adiabat was
  Book 3's): prefix new ids (katsura10:, b2dd10:, b2roy:).

## Sync 2 re-sourcing log (send-back, 2026-10-23)

Removed rows are kept verbatim in the scratch log `scratchpad/book2/ledger/removed/`;
new entries in `scratchpad/book2/ledger/resource/`.

- **g12.09 done**: 9 WIKI sources + 9 rows removed; 12 sources + 12 rows added
  (IPEV Concordia, Parrenin 2007 EDC3, KU and IPEV Beyond EPICA 2025, Freitag 2013,
  NASA EO oxygen balance, UCMP forams, Clark 2006 MPT, NASA Milankovitch, NCEI proxy
  and pollen pages, Rull 2018 editorial). Text changes: hook now 3233 m, about -55 °C,
  drill stopped at 3260 m about 15 m above the rock (was -54.5 °C, 25 mm/yr, December
  2004, 3270 m, 5 m: Wikipedia only); close-off 820-830 kg/m3 at 50-120 m; pollen
  "survives acids" and "5-500 µm" dropped; von Post "first modern quantitative pollen
  diagram in 1916"; forams "often of calcite"; Little Dome C "about 35 km"; Sunda
  "30 to 40 m" replaced by the computed 36 m (new `link_level` minimax path in
  ice_age_records.py, 2 new tests; Sumatra 1 m, Java 5 m on the 0.1-degree grid);
  ex. 9(b) and 15 and their solutions follow (15: -36 m passed about 9800 years ago,
  3000 years). EXCLUDED: Dome C accumulation 25 mm/yr and the December 2004 date
  (Wikipedia only), pollen-wall acid resistance and grain sizes (no agency source).
- **g12.08 done**: 7 WIKI sources + 7 rows removed; 9 sources + 10 rows added (DBCA
  Karijini and Hamelin Pool, Earle 6.2, Holland 2006, Kasting and Ji 2025, Feulner 2012,
  Noffke and Awramik 2013, Allwood 2006, NASA Moon formation; Wilde 4404 Myr; Book 1's
  usgs:age-earth cited). Text: Dales Gorge "more than 2.5 billion years", no band
  thickness; Moon impact "about 60 million years after the Solar System began to form"
  (was 30-50 Myr after the Earth formed; ex. 15 and its solution redone: 4507 Ma, 103 Myr);
  faint-Sun paragraph rewritten on Feulner (0.1 bar with a little methane, 3 times more
  without; not solved); stromatolites 3430 Myr (Allwood), Hamelin Pool twice as salty;
  ex. 10 rewritten (no grazers); BIF "almost all older than 1.8 Ga", common 2.4-1.8 Ga
  (Earle), red bar of the oxygen timeline now 2.4-1.8 Ga; detrital grains: pyrite absent
  after the rise of oxygen (Kasting), ex. 4 follows. EXCLUDED: BIF band thickness, size
  of a formation (hundreds of m / km), "most of the iron ore mined", Hamersley 2470-2450
  Ma, BIF peak at 2.5 Ga, stromatolite peak at 1.25 Ga and the grazing explanation, the
  magma-ocean and steam-atmosphere details, "30-50 Myr" (all Wikipedia only).
- **g12.07 done**: 3 WIKI sources + 5 rows removed (age-history, age-earth, kelvin-98,
  rbsr, pbpb); 3 sources + 3 rows added (Holmes 1913, Holmes 1927, Tulane radiometric
  dating notes); Book 3's england:kelvin and Book 1's usgs:age-earth cited read-only.
  Text: Kelvin 1862 is 96 Myr (20-400), not 98 (Wikipedia; Holmes and England agree on
  96), 1897 "between 20 and 40"; "Charles Darwin with them" dropped; table: Buffon row
  dropped, Phillips 1860 38-96 Myr, G. H. Darwin "at least 56 Myr since the Moon
  separated", Joly 1899 80-100; Curie-Laborde "melts its own weight of ice" dropped;
  clock paragraph now Boltwood 1907 (constant Pb/U), Holmes 1913 oldest rocks 1600 Myr,
  Holmes 1927 1.6-3.0 Ga, Patterson 4.55, today 4.54 "to within one per cent"; chart:
  Buffon and Phillips out (Phillips would sit on Kelvin's bar), Holmes 1911 -> 1913,
  x from 1840, y from 1e7, today's bar 4.50-4.58. Ex. 2 rewritten on the Varden table
  (biotite highest), ex. 5 on Joly's upper end (45 times), ex. 10 and 15 on 96 Myr
  (47 times; 190 Myr). EXCLUDED: Buffon's 74,832 years, Rutherford's 40-Myr helium date,
  Boltwood's 26 samples, Holmes's 1911 Ceylon sample, closure temperature 650 °C, Rb
  substituting for K and the mineral order of Rb/Sr, accretion "30 to 100 Myr",
  "+- 0.05" (all Wikipedia only).
- **g12.06 done**: 8 WIKI sources + 9 rows removed; 13 sources + 14 rows added (GFZ KTB
  lab and 30-year release, KamLAND 2011 paper, Dye 2012, NNDC NuDat 3 half-lives, Earle
  9.2 and 4.1, EIA geothermal pages x3, Enel historical archive, CPUC EIR on The Geysers,
  ON Power); Book 3's england:kelvin cited for kappa = 1e-6 m2/s. Text: KTB bottom "about
  265 °C, too hot to drill deeper" (was "hotter than 260"), gradient 28 °C/km (ex. 6 redone:
  76 mW/m2, 7 % above the continents); radiogenic model rebuilt in internal_heat.py on
  KamLAND (U+Th 20.0 TW, Th/U 3.9, K-40 4 TW) and Dye's isotopic heat table: Th 10.4,
  U-238 9.6, K-40 4.0, U-235 0.42 TW, total 24.4 (was 23.9), secular 22.3 (was 22.8),
  4.5 Ga ago 116 TW (was 108); half-lives NNDC 4.468 and 1.248; problem Q11-12 rewritten
  on the per-kg heat of uranium and thorium, Q18 on Dye's 11-38 TW (was 15-41); ex. 12,
  13 (Nesjavellir now ON's 1640 L/s for 300 MW: 44 K), 15 (core 10 TW as a supposition)
  and g12.07 ex. 15 (2.1 times, 200 Myr) follow; Larderello 1904 lit FIVE bulbs (Enel
  archive; Wikipedia said four). EXCLUDED: KTB expected 250-300 °C at 10-14 km, the
  Kola/KTB comparison, sandstone and quartz diffusivities, the planform of today's
  convection (sinks beneath the Americas, rises beneath the Pacific and Africa), loop
  times 50 and 200 Myr (now a supposition in ex. 14), core heat flow 5-15 TW, "80 % by
  convection", 4 July 1904, dry-steam 240-300 °C, decline of Larderello and Wairakei,
  Nesjavellir 1100 L/s at 82-85 °C (all Wikipedia only).
- **g12.05 done**: 2 WIKI sources + 2 rows removed; 3 sources + 3 rows added (USGS OFR
  01-188B and 2009-1153 on the Alleghanian orogeny, North Carolina State Parks for Mount
  Mitchell 6684 ft); the Mississippi basin is now the 1,150,000 mi2 (2.98 million km2) of
  Kammerer 1990 already used in g10.08 (was Wikipedia's 3,224,000 km2, an inconsistency
  between the two chapters): example 56 m/Myr (was 52), 1987-2006 20 m/Myr (was 19),
  ex. 14 follows, and the Mississippi bar now sits above the basin median in the rates
  chart (labels reordered). Hook: collision "in the Carboniferous and Permian, more than
  250 Myr ago" (was 320-260 Ma); Mount Mitchell "the highest point east of the
  Mississippi". Appalachian test rewritten: after 250 Myr the model leaves 0.4 m, yet
  Mitchell stands 2037 m, so the model alone does not fit (problem Q19 and solution
  follow; new value h_after_250myr in relief_decay.py). EXCLUDED: the collision at 270 Ma,
  the end-Mesozoic plain, the Cenozoic uplift and rejuvenated rivers, length 2050 mi,
  "fourth largest basin, 32 states" (all Wikipedia only).
- **g12.04 done**: 2 WIKI sources + 2 rows removed; 3 sources + 3 rows added (BGS Rock
  Classification Scheme "Granodiorite", Earle 3.5, NPS Yosemite geology). Text:
  granodiorite "20 to 60 % of its light minerals are quartz, 65-90 % of its feldspar
  plagioclase; often biotite or hornblende" (BGS); upper crust "about 67 % SiO2: felsic,
  like the granites arcs make" (was "has the composition of a granodiorite"); batholith
  definition per Earle (> 100 km2 exposed, coalesced plutons); Coast Plutonic Complex
  "from the Vancouver region to south-eastern Alaska"; Sierra Nevada batholith formed
  above a subduction zone, Yosemite granites Cretaceous 105-85 Ma, exposed by erosion
  (NPS); figure caption follows. EXCLUDED: "more dark minerals than granite", "the
  upper crust has the composition of a granodiorite", plutons solidified "5 to 30 km
  down", Coast Plutonic Complex 1800 km, "the roots of a line of volcanoes" (all
  Wikipedia only).
- **g12.03 done**: 1 WIKI source + 1 row removed; 1 source + 1 row added (IUGS
  Commission on Geoheritage, "Metamorphic Barrow Zones in Scottish Highlands": chlorite,
  then biotite, garnet, staurolite, kyanite, sillimanite in metamorphic mudstones). The
  four citations re-keyed; the text was already supported (sequence by IUGS, burial and
  heating by Earle 7.4). Nothing EXCLUDED.
- **g12.02 done**: 3 WIKIBOOKS sources + 3 rows removed; 2 sources + 2 rows added (Tulane
  EENS 2120 "Ocean basins" for the ophiolite and its sequence; USGS OFR 78-118 for the
  continental suture). Text: suture "joined by a collision once subduction between them
  has stopped: the trace of a former plate boundary" (the island-arc case dropped);
  ophiolite "pushed onto continental crust"; "mountains raised by a collision commonly
  hold some ocean crust and upper mantle" (Earle 10.4) replaces the list Alps, Himalaya,
  Urals, Appalachians; Himalaya "sediments laid down on India's northern edge, then
  stacked, folded and faulted" (Sakai 2005). EXCLUDED: "ophiolites a tiny part of all
  ocean floor", the four-belt list, 10-17 km of marine sediments, "many folds turned
  over on their sides" (all Wikibooks only).
- **Also**: g12.08's red-beds photo caption ("Permian red sandstones" of Cathedral
  Rock) had come from the Wikipedia caption; now sourced to the Arizona Geological
  Survey (azgs:cathedral, Permian Schnebly Hill Sandstone).
- **Landing check**: `grep -i wiki sources/ledger/book2.md | grep -vci commons` = 0.
  The literal `grep -ci wiki` gives 60: every one is a Wikimedia Commons photo-credit
  source (URL commons.wikimedia.org/wiki/File:...), which cannot be written without the
  string. Total re-sourcing: 35 WIKI/WIKIBOOKS sources and 38 rows removed, 47 sources
  and 49 rows added across g12.02-g12.09 (counts from the scratch removed/ and
  resource/ logs).

## Solutions re-read log (send-back item 3, 2026-10-23)

All 448 items (28 chapters x 15 exercises + 1 problem) were extracted as
question/solution pairs by a script (scratchpad `bin/qa_pairs.py`: no question
without a solution, no orphan solution), each pair read against its question,
and every number recomputed in Python from the data the chapter prints (and,
for figure readings, from the `figdata/out` table behind the figure: the
Potomac hydrograph dates, the polarity boundaries under five million years,
the flood-frequency peaks over 9500 m3/s, the D8 flow grid of g10.08 ex 15,
the Pb isochron slope table of g12.07). Problem lengths checked against the
18--22 rule (g12.03 has 21, g12.10 19). Slips fixed (9, in 5 chapters; 23
chapters clean):

- g10.03 ex 6 / pb Q5: 1361 sin 30 printed 681 in one place and 680 in the
  other; both now 680.5 (exact).
- g10.03 ex 13: lambda printed 53.2 deg (asin 0.800 = 53.13; exact 53.15) and
  the chain 126.8 / 73.6; now 53.15, 126.85, 73.7 deg (still about 75 days).
- g11.04 pb Q5: scatter described as "Laysan a little below, Colahan a little
  above"; against t = d/91, Laysan lies on the line (19.98 vs 19.9) while
  Kauai, Nihoa and Necker lie below and Colahan and Abbott above: rewritten.
- g12.02 ex 9: distance printed 1210 km then divided as 1206/14; now 1207 km
  and 1207/14 (still 86 km/Myr).
- g12.02 ex 15: 40/0.18 printed "approx 230"; it is 222: now "approx 220".
- g12.06 ex 12: total printed 56.7 TW, the sum of four rounded terms; from the
  raw terms 56.6 (round once): now 56.6 (share still 52 %).
- g12.06 ex 14: the question quotes 260 billion years (as the chapter, 2.6e11)
  but the solution used 2.65e11 / "265 billion": now 2.6e11/1e8 = 2600 and
  1300, matching the question.
- g12.06 pb Q8 -> Q15--Q20: Q8 computes 46.6 TW while Q15--Q20 use 46.7 TW
  with no word; Q8 now says the chapter's global mean gives 46.7 TW, the value
  used below.
- g12.08 ex 3: 29 % dimmer called "roughly a third"; now "nearly a third".

No wrong object, no permuted answers, no answer contradicting its data
beyond the above.

## Figure check log (send-back item 2, 2026-10-23)

Every figure object was enumerated by a script from the sources (scratchpad
`bin/figlist.py`: each `omfigure`, each `includegraphics` outside one, each
`tikzpicture` outside one; 210 objects = 205 + 3 + 2 on 167 pages), located in
the PDF by its caption, and checked on its own page rendered at 130 dpi, one
page at a time; side-dependent symbols (trench teeth on the four world maps,
fault ticks and arrows on the Varden sections, the cyclone spiral, the
upwelling wind symbol) and small legends and leaders on 300-dpi crops.
`FIGCHECK.md` rebuilt: **one row per object, 210 rows** (was 201: the 4 g12.10
omfigures it lacked plus g12.10's other 6 objects, the 3 standalone
includegraphics and the 2 problem tikzpictures now all listed; two table rows
dropped, a merged g12.04 row split), printed pages of the current build, the
Phase C note kept beside the new one, the two stale encyclopedia notes
(Nesjavellir, red beds) replaced. Fixes (22 objects; every fixed page rebuilt
and re-checked at 130 dpi):

- science:
  - g10.04 cloud parcel: invented sounding A cooled at 6.5 degC/km above its
    4 km warm layer, so the parcel became warmer than A again from 4.5 km,
    against the caption (cumulus stops at the warm layer): A now 4.5 degC/km
    above 4 km (`clouds.py`), new test that the parcel stays colder above the
    cloud top; the problem's table (0--4 km) is unchanged.
  - g10.06 upwelling: with west left and east right the reader faces north;
    the equatorward wind off Peru blows north, INTO the page, but the symbol
    was a dot and the label "out of the page": now a cross, label and caption
    "northward, into the page".
  - g11.03 Airy columns: oceanic crust drawn in a different (gabbro) fill
    while Airy's model has one crustal density: same fill.
  - g12.02 Varden section A--B: the syncline axis was drawn at 7.379 km, its
    unfaulted position; the syncline lies wholly on the hanging wall and was
    carried 115 m towards 120 deg by the slip, so its hinges are at 7.484 km:
    axis moved, value computed in `fold_shortening.py` (`section_axis_s`) and
    tested against the lowest base of the chalk on the region grid.
  - g12.05 unconformity section: the red unconformity ran on past the fault
    into the hanging wall (ending in the limestone at 6.95 km):
    `region.contact_elevation`'s fixed-point iteration does not converge in
    the gap a normal fault opens in a horizon and returns a footwall value in
    the hanging wall (shared file: reported, not edited). `relief_decay.py`
    now keeps each block's value only inside its block (gap otherwise); new
    test that every plotted point has sandstone above and basement below.
- caption/text against the figure:
  - g10.08 hydrograph: "from about 360" beside the text's 330: now "from
    362 m3/s on 18 January to more than 9000 three days later".
  - g10.09 residence times: "each step on the axis is a hundredfold" while the
    marks are day, month, year, 100, 10 000, 1 million years: "from one year
    on, each marked step is a hundredfold".
  - g12.06 heat budget: top/bottom bars swapped in the caption.
  - g12.10 ice-core CO2: caption said "between about 180 and 300 ppm" with an
    unexplained spike to 368 ppm at the end: now explains it is the youngest
    ice (to 2001).
- layout:
  - g10.01 degree-length chart: 66 deg marker unlabelled: "111.51 km at 66
    deg (Lapland)".
  - g10.05 pressure-wind scatter: category limits merged with the grid:
    darker, dashed ("Grey dashed lines").
  - g11.04 Hawaiian ages: "Midway" label offset towards the wrong point.
  - g11.05 depth-age: square-root law drawn to 80 Myr, its stated range is
    0--70 (`depth_age.py`).
  - g11.09 burial history: "oil window" ran into "source rock".
  - g12.02 Alpine belt: "Zagros" sat on the Arabian side of the Gulf: label
    in the desert with a leader to the range.
  - g12.05 denudation bars: 5.4 printed as 5 (one decimal for measured
    values).
  - g12.06 convection: "cold slab sinks" far from its slab, into the plates.
  - g12.07 age estimates: "Kelvin 1862" over the 10^8 tick label, "Kelvin
    1897" on the axis; Rb--Sr isochron: "plagioclase, hornblende" over the y
    axis; Pb isochron: "Canyon Diablo, Henbury" label hanging 10 pt below its
    point.
  - g12.09 pollen diagram: panel titles on different baselines.
  - g12.10 forcing bars: two `\addplot` series in an `xbar` axis are shifted
    either side of the tick by default, so every bar sat off its label:
    `bar shift=0pt` (the other multi-series bar charts were checked: g11.06
    already had it, g12.01 is grouped on purpose).
