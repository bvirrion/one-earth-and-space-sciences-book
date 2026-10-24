# PROGRESS --- Book 1

**State (2026-10-23): Phases B and C done; Phase D report sent.** 32/32
chapters written; term links curated and idempotent (6102 links, 136
targets); every figure re-checked after linking (FIGCHECK: 248 rows, every
chapter's row count >= its figure count); solutions re-read; no AI stub or
PNG left. Entry file
`one_earth_and_space_sciences_book_1_primary_middle_school.tex` builds
0 errors / 0 undefined / 0 overfull, 324 pages (250 pp of chapters).
See 'Phase C log' below. Nothing left for this writer unless the main
session sends work back.

To resume from this file alone: read `sources/BATCH_BOOKS_1-5.md` (binding,
incl. its Sync decisions), then `BRIEFS.md` (one brief per chapter, outline
order), `DEFINITIONS.md` (labels), the pilot `parts/grade-7/01-plate-tectonics.tex`
(reference for grades 6--9), then pick up the first chapter not marked
written below. Ledger: `sources/ledger/book1.md`; figure checks:
`FIGCHECK.md`; scratch: the session scratchpad `book1/` (disposable).

AI review log: reviewed and accepted (2026-10-22) g1 (all but windy-kites),
g2 (all six), g3 (all five: stream-pebbles, sand-magnifier, spinning-globe,
orange-peel, stone-village). g1.2 exercise 9 solution aligned with the
plain-river image (foreground = tall grass). Reviewed and accepted 2026-10-22 (contact sheets): all g4--g9 images
(29), including g6-deep-mine and g6-hand-pump. run_all ended 20:09; fix1
(windy-kites redo) launched 20:1x, log `ai/fix1.log`; g5 batch has two extra prompts (g5-rainforest,
g5-polar-tundra) appended 2026-10-22.

## Chapter status

| ch | status | pages (target) | notes |
|---|---|---|---|
| g1.1 `watching-the-weather` | written, 0/0/0, gates OK | 7 (7) | 11 exos; FIGCHECK done for schematics; AI reviewed; windy-kites regenerated twice (scarves vs kites wind), third accepted 2026-10-22 |
| g1.2 `landscapes-around-us` | written, 0/0/0, gates OK | 6 (7) | 11 exos; AI reviewed |
| g2.1 `water-on-earth` | written, 0/0/0 | 6 (7) | 11 exos; figdata ocean_fraction (71), water_shares (96/2/2) |
| g2.2 `drawing-to-map` | written, 0/0/0 | 6 (7) | 11 exos; figdata varden_plan; compass rose defined, cardinal directions prose only (Sync 1) |
| g3.1 `stones-pebbles-sand` | written, 0/0/0, gates OK | 6 (7) | 10 exos; 2 Commons photos (granite wall, slate roofs) credited; method + magnified-rocks figure added for depth |
| g3.2 `continents-and-oceans` | written, 0/0/0, gates OK | 7 (7) | 10 exos; figdata globe.py (orthographic, Weiler-Atherton limb clip, 7 tests); NOAA/NatGeo ledger rows; no photo (the g2 Blue Marble is recalled), gores dropped (AI orange peel) |
| g4.1 `clouds-rain-snow` | written, 0/0/0, gates OK | 7 (7) | 11 exos; 5 NOAA photos; WMO cloud atlas + Met Office ledger; Everest row (tht:everest) shared with g4.3 |
| g4.2 `volcanoes-earthquakes-first-look` | written, 0/0/0, gates OK | 6 (7) | 11 exos; figdata ring_of_fire (ring line, 500 km band, shares 69 % / 76 %); 3 USGS photos; ShakeOut ledger |
| g4.3 `world-physical-map` | written, 0/0/0, gates OK | 6 (7) | 11 exos; figdata physical_map (PNG raster from ETOPO 1 deg, 10 bands, Africa area 29.85 Mkm2, Sahara share 0.28; 5 tests); 2 NASA ISS photos; AI floor-map image dropped (risk of wrong geography, as the brief allows) |
| g5.1 `water-shapes-the-land` | written, 0/0/0, gates OK | 8 (7) | 11 exos (6/4/1 stars); 7 schematics (frost, long profile, meander map+cut, valley cuts, delta) ; 2 NASA photos (Mamore ISS, Nile MODIS); sediment flux from Syvitski 2005 (12.6 BT/yr printed as 'more than 12 billion tonnes'); 3 AI |
| g5.2 `weather-and-climate` | written, 0/0/0, gates OK | 6 (7) | 11 exos (6/4/1); figdata climate_charts (NOAA normals, 4 stations) + climate_zones (obliquity), 4 tests; annotated Seattle chart; 1 NPS photo; 4 AI (2 postcards, rainforest, polar; the last two replace the brief's USDA/NOAA photos, not found quickly) |
| g5.3 `natural-hazards` | written, 0/0/0, gates OK | 7 (7) | 11 exos (6/4/1); 3 schematics (hazard families, hazard vs disaster valley, warning ladder); 2 photos (Isabel ISS, Oso landslide USGS); 2 AI; optional cyclone-track map NOT drawn (Book 2 g10 owns tropical cyclones and has the IBTrACS data; not duplicated) |
| g6.1 `earth-a-planet` | written, 0/0/0, gates OK | 9 (10) | 12 exos (4/6/2) + 12-q problem (final 92); figdata planets.py re-reads the shared planet:* rows (7 tests); 4 figures + 5 NASA/Hubble photos; no AI; DEEPENED after the grade-6 alarm: section 'How far apart are the planets?' (distances to scale, scale-model method/example/table from planets.py parts dist and model, 8 tests) and a Pale Blue Dot history box (NASA PIA23645) |
| g6.2 `latitude-longitude` | written, 0/0/0, gates OK | 8 (10) | 12 exos (4/6/2) + 12-q problem (final: 8 a.m. Saturday in Auckland); figdata cities.py, time_zones.py, graticule.py (imports grade-3 globe.py) with 5 tests; 6 figures; 1 photo (H4, CC BY-SA); 1 AI |
| g6.3 `rocks-and-minerals` | written, 0/0/0, gates OK | 8 (10) | 12 exos (4/6/2) + 12-q problem (final: quartz 7, three families); figdata granite_mosaic.py (2 tests); rock cycle, key, Mohs ladder; 9 Commons photos (8 CC BY 2.0 James St. John, 1 CC0); 1 AI; DEEPENED: grain size -> conglomerate/sandstone/shale figure (usgs:wentworth) and an in-the-field box (stones of a town) |
| g6.4 `inside-the-earth` | written, 0/0/0, gates OK | 8 (10) | 12 exos (4/6/2) + 12-q problem (final: oceanic crust 0.78 mm on a 2 m model); figdata earth_layers.py (PREM boundaries, profile, geotherm, model; 5 tests); 7 figures (strip, egg, disc+inset, density, wave speeds, geotherm, + photo), in-the-lab box (layers in a glass); Lehmann photo (PD); 1 AI; Kola from Scientific American, gradient USGS OFR 87-592, core 6000 C ESRF 2013, Lehmann NBI, deepest mine Guinness |
| g6.5 `water-underground` | written, 0/0/0, gates OK | 9 (10) | 12 exos (4/6/2) + 12-q problem (final: 100 days); figdata water_table.py (Varden Hills N-S section at x = 5.5 km via region.section, chalk on shale, spring on the contact, water table as a subdued replica K = 0.7 / 0.6, wells A always / B wet season only, fresh-water shares re-read from the ledger; 6 tests); 6 figures; Big Spring photo (CC BY-SA 4.0); 1 AI; Heath 1983 porosity/yield table; in-the-lab and in-the-field boxes; groundwater-quality section |
| g7.1 `plate-tectonics` | pilot written 2026-10-22 (main session) | ~10 + 2 solutions | 12 exos + 12-q problem; 82 term links; 9 figures FIGCHECKed; exercise 12 FIXED in Phase B (now 100/300/500 km bands from quakes_on_boundaries.py part bands, a reasoning question on slanting slabs; test_exercise_12_bands) |
| g7.2 `volcanoes` | written, 0/0/0, gates OK | 12 (10) | 12 exos (4/6/2) + 12-q problem (final: 401 m lost, 2950 - 2549, from FS 036-00 feet x 0.3048); figdata volcano_settings.py (GVP settings 838/221/149/6, 69/18/12 %, 564 of 660 stratovolcanoes = 85 % above sinking plates; 8 tests incl. Hawaii intraplate, St. Helens + Pinatubo subduction/strato); 10 figures (cut-away, effusive/explosive, hotspot, map by setting, counts bar, 5 USGS PD photos, 1 AI); tables of glow colours and products; in-the-lab (fizzy bottles, pumice), history (Wilson 1963); mudflow and safety remarks; 30 new ledger rows (USGS FS 036-00, FS 113-97, VHP pyro/gas/lava, HVO FAQ + Volcano Watch, TDE) |
| g7.3 `earthquakes` | written, 0/0/0, gates OK | 10 (10) | 12 exos (4/6/2) + 12-q problem (final: 13 minutes to reach high ground; 240 km at 800 km/h = 18 min, minus 5 min of warning); figdata quake_counts.py (USGS M>=6 1976--2025: 6335/656/38/2 by class, 79 % of foci <= 70 km, 483 deeper than 300 km, deepest 688 km; 2004 tsunami times to Colombo 1831 km / 2 h 17 min and Male 2495 km) and epicentre.py (PREM crust: 7.1 and 9.1 km per second of delay, 8 used; method example and problem map, least-squares locate back, stations on land, epicentre at sea; 11 tests); 11 figures (block diagram, seismometer + drawn trace, three circles, log bars, MMI table, tsunami schematic, problem map, 3 PD photos, 1 AI); defines fault, focus/epicentre, seismometer/seismogram, magnitude, intensity, tsunami; P and S waves in prose only; 20 new ledger rows (USGS EQ science/magnitude/MMI/largest, NWS tsunami FAQ x3); softened: rupture length, slip sizes, landslide cause, modern warning system |
| g7.4 `sediments-and-fossils` | written, 0/0/0, gates OK | 9 (10) | 12 exos (4/6/2) + 12-q problem (final: 1 800 000 years for the 180 m of limestone at 1 cm per century, 7.5 times the sandstone at 1 cm per 20 years; exercise rates); figdata varden_column.py (region THICK; chalk drawn as an 80 m stub, no thickness printed: the model gives the chalk no top; 5 tests); 10 figures (lake settling, sand to sandstone, four fossil steps, mould and cast, Varden column, 5 Commons photos: Grand Canyon NPS PD, ammonite + trilobite + ripples J. St. John CC BY 2.0, Dinosaur Ridge tracks CC0; 1 AI reused: g7-shallow-sea); tables sediment -> rock and clue -> environment; in-the-lab (layers in a jar), in-the-field (sediments laid down today), remark (look, photograph, leave it); defines sediment, sedimentary layer/stratum, fossil/mould/cast/trace fossil; superposition and fossil succession left to g7.5; 22 new ledger rows (USGS GIP "Fossils, Rocks, and Time", UCMP fossils x3, NPS Grand Canyon x3, NPS ripples x2, NPS paleo glossary, NOAA corals, USGS coal FAQ) |
| g7.5 `geological-time` | written, 0/0/0, gates OK | 9 (10) | 12 exos (4/6/2) + 12-q problem (final: our species appears at about 23:25 on 31 December, 35 minutes before midnight at 8 600 years per minute); figdata time_scale.py (re-reads the shared ics rows; bar rings + label tables), earth_calendar.py (dates + tags), varden_history.py (section E--F through the granite, fault stopped at the ground; event order); 11 tests; 6 figures (Hutton portrait Raeburn PD; four principles; unconformity in four steps; section E--F; two-bar time scale; the Earth's year); method (ordering a cross-section) + worked example on E--F; history box (William Smith); in-the-lab (ribbon of time, indoors); defines relative dating/absolute age, superposition, cross-cutting, inclusion, fossil succession, unconformity, era/geological period, geological time scale; radiometric dating told only; 13 new ledger rows (USGS geotime x2, USGS GIP x4, NPS cross-cutting, Earthlearningidea 238, NCSE Siccar Point, Hublin 2017, Commons) |
| g8.1 `the-atmosphere` | written, 0/0/0, gates OK | 8 (10) | 12 exos (4/6/2) + 12-q problem (final: the pressure is a quarter of its sea-level value at about 10.3 km, by interpolation in the standard-atmosphere table; script gives 10.29 km); figdata standard_atmosphere.py (USSA 1976 Tables 4--5 and eq. 27 read from the scanned PDF; 6 tests against the standard's tabulated pressures); 7 figures (radiosonde launch NOAA PD; ISS limb NASA PD; Earth slice to scale 1 cm = 100 km; pressure profile + balloon at launch/burst; AI climbers (g8-climbers); temperature profile 0--100 km with layers and ozone bar); method (reading a temperature profile), example (airliner at 11 km); in-the-field (radiosonde soundings); defines the layers (one definition with tropopause), environmental lapse rate (Sync 1 ruling, added to DEFINITIONS), ozone layer; 9 new ledger rows (USSA 1976 x3, NWS radiosonde factsheet, UCAR layers/troposphere/ozone, Commons x2) |
| g8.2 `winds-global-circulation` | written, 0/0/0, gates OK | 8 (10) | method (finding the global wind at a latitude) + example (40 S) + in-the-lab (paper spiral over a radiator) added after the g8.3 checkpoint; 12 exos (4/6/2) + 12-q problem (final: the Praia--Bridgetown crossing takes about 23 days, 3896 km at 168 km a day; the 7 km/h speed is exercise data); figdata trade_route.py (Natural Earth places + land clamped to the box, great circle 3896 km, school estimate 36.1 deg x 108 km = 3900 km, 27 sea-only trade arrows) and sunlight_spread.py (1/cos table); 5 tests; 7 figures (AI sailing ship; two beams; sea/land breeze loops; AI kites; globe with surface winds, pressure belts and a side view of the six cells; GOES-16 full disk NOAA PD, side by side with its caption; trade-wind map); defines convection cell, sea/land breeze, the global winds (trades, westerlies, polar easterlies), global circulation; Hadley/Ferrel/polar cells and the doldrums named in prose only, the ITCZ not named; the rotation told as deflection; 6 new ledger rows (NOS trade winds x2, Met Office x2, JetStream sea breeze, Commons). g8.1's problem was tightened (three questions shortened, two medskips dropped) so it sits on one page instead of spilling three lines |
| g8.3 `fronts-and-weather-maps` | written, 0/0/0, gates OK | 8 (10) | 12 exos (4/6/2) + 12-q problem (final: the cold front reaches the town at 13:30, 180 km at 40 km/h from 09:00; speed and shower length are exercise data; 15:00 if it slows to 30 km/h); figdata weather_map.py (analytic field: 1012 hPa background, low 980, high 1034, 3 hPa troughs along the fronts for the kinks; 4 hPa isobars by region.trace; fronts oriented for the left-side symbols; winds along the isobars, low on the left, turned 20 deg; parts seq-06/seq-09/town for the problem zoom); 8 tests; 7 figures (AI rain arriving; air-mass source regions on Natural Earth land; cold-front and warm-front sections; Terra MODIS low off Iceland NASA PD; the weather map; the problem zoom); method (reading a weather map), example (the weather at T), history (FitzRoy, first public forecast 1861), in-the-field (watching a front arrive); defines air mass, front (warm, cold), depression + anticyclone (one definition; anticyclone label by \phantomsection after it), isobar, weather forecast; occluded front named only; 11 new ledger rows (NOAA JetStream air masses, Met Office fronts / how forecasts / accuracy / FitzRoy, UCAR fronts x2, BoM weather map x2, Bauer 2015, Commons). The "4 hPa" step is a property of this book's maps (no fetched source gives it): the definition says "often" |
| g8.4 `the-oceans` | written, 0/0/0, gates OK | 8 (10) | 12 exos (4/6/2; ex 8 framed as hypothetical Sea A / Sea B) + 12-q problem (final: a drifting buoy goes round the North Atlantic gyre in 603 days, about 20 months, legs 3800 / 2100 / 3100 / 6100 km at 100 / 20 / 20 / 20 km a day; the batteries die 67 days into leg D); figdata seafloor_profile.py (ETOPO1 1-deg rows at 30.5 S and 20.5 S, VE from the printed panel sizes) and ocean_currents.py (five schematic gyres cut into four arrowed sides, warm/cold by side, wrap at 180, buoy great-circle legs); 7 tests; 8 figures (Challenger engraving PD; floor sketch; two real profiles; salinity schematic; AI research ship; gyre map; Aqua SST NASA PD; buoy map); method (reading a profile of the ocean floor) + example (across the South Atlantic); in-the-lab (a gyre in a dish, indoors); defines the parts of the ocean floor (one definition), salinity, ocean current + gyre (gyre by \phantomsection); the conveyor belt told in prose (global ocean conveyor belt, about 1000 years); 13 new ledger rows (Challenger dates / stations, NOS sonar / salinity varies / sea ice / gyres x2 / Gulf Stream / conveyor / drifter, DOSITS sound speed, Commons x2). Removed as unsourced: sounding time, top-few-hundred-metres currents, Red Sea / Baltic salinities, Bergen winters |
| g8.5 `ice-on-earth` | written, 0/0/0, gates OK | 10 (10) | 12 exos (4/6/2) + 12-q problem (final: Glacier G's snout, retreating 18 m a year on average 1960--2020, would be level with the hut in 2070; Glacier G is exercise data, with a not-a-forecast question); figdata sea_ice.py (NSIDC G02135 v4 September extent 1979--2025, least-squares trend -0.76 Mkm2/decade, decade means) and glacier_retreat.py (fronts, walls, floor, ice, moraine, labels); 6 tests; 8 figures (Pedersen 1990/2016 NPS PD; glacier long section; V and U valleys; ice shelf edge NASA PD; sea-level-equivalent bars; sea-ice graph; AI tilting house + permafrost sketch; problem map); method (reading a trend on a graph) + example (the Arctic's September ice); in-the-field (reading a valley shaped by ice, observation only); in-the-lab (floating ice and ice on land, indoors); defines glacier, U-shaped valley + moraine (one definition), ice sheet + ice shelf + iceberg (one definition), sea ice, permafrost, ice age; firn, accumulation/ablation area, snout, surge, erratic, active layer, trend line in prose; glacial/interglacial conceded to Book 2 g12 (prose: "the ice ages and the warmer times between them"); albedo not named (Book 2 g10). 21 new ledger rows (NSIDC x13, USGS LGM FAQ, USGS glacier glossary, NPS x2, UW Kenai 2022, Commons x2). Ex 11 was first an extrapolation to a zero-ice year (about 2080): replaced by decade means, so the book prints no ice-free date that could be read against the assessments |
| g9.1 `climate-past-and-present` | written, 0/0/0, gates OK | 9 (10) | 12 exos (4/6/2) + 12-q problem (final: 2015--2024 was 1.21 degC warmer than 1880--1899 in GISTEMP v4, about 1.2 degC; the AR6 1.09 degC for 2011--2020 vs 1850--1900 set beside it); figdata climate_records.py (GISTEMP decades / annual / period means, Mauna Loa annual, ice-core CO2 and Dome C temperature in 2000-year bins, satellite sea level + least-squares rate 3.18 mm/yr); 6 tests; 8 figures (greenhouse sketch; GISP2 ice core NOAA PD; 800 kyr temperature + CO2; AI weather screen; decade bars; annual series with period means; Mauna Loa CO2; sea level); methods (reading two records side by side; measuring a warming between two periods) + examples (the last ice age in the core; the warming since the 1970s); history (Keeling, 1958); dated{2025} (427.35 ppm; 2024 warmest at 1.28 degC); a table of the IPCC calibrated words; defines temperature anomaly, global warming, climate change; greenhouse effect/gases recalled from chemistry, infrared named only, glacial/interglacial not used. Book 2 rows cited read-only: ipcc:likelihood, unequivocal, gsat-2011-2020, decades, attribution, observed-2010-2019, sea-level-obs, co2-2myr, erf-2xco2, 3myr; minted ipcc:b1-ice (SPM A.1.5) with its own Sources key B1-IPCC-AR6-SPM (check_ledger resolves source keys per file). 5 new ledger rows (NASA EO ice cores, Commons GISP2, IPCC A.1.5, NOAA GML Keeling, GISTEMP method) |
| g9.2 `natural-risks` | written, 0/0/0, gates OK | 9 (10) | 12 exos (4/6/2) + 12-q problem (final: 17 of the 28 houses of the Varden village stand in the 5 m flood zone; sites A in the zone, B steep and on the fault, C chosen); figdata flood_zone.py (zones 2/5/10 m above the river by bisection on region.topo, contours, houses, sites, slopes, distance to the shared fault trace); 6 tests (houses at least 60 m from the zone edge); 8 figures (Ruiz hazard map USGS PD; risk grid; AI emergency kit; volcano instruments; flood zones; four frames; DART buoy USCG PD; problem map); method (reading a flood-zone map) + example (three houses beside the river); in-the-lab (a tower on a shaking tray, indoors); history (the DART network, 2001--2008); defines vulnerability, risk, prevention, hazard map; hook Armero 1985 (Pinatubo only recalled from g7.2; warning colours and safety rules left to g5.3); contour lines shown on the maps with a forward pointer to g9.5 (owner); "normal fault" (Book 2) avoided. 10 new ledger rows (USGS HVO Armero, USGS Circ. 1073 map, NDBC DART, IRIS Better Wall, Exploratorium isolators, USGS HVO toolkit, Commons x2, Ready.gov kit, FEMA flood zones) |
| g9.3 `earth-resources` | written, 0/0/0, gates OK | 8 (10) | 12 exos (4/6/2) + 12-q problem (final: the pit's sand reserve, 3.2e6 t, would last 20 years at 1.6e5 t a year; exercise data built on the USGS 100 / 300 t of aggregates per home); figdata concentration.py (factors from Perkins + Earle, time scales, copper reserves / 2024 production 42.6 years, the problem chain); 4 tests; 8 figures (factor bars; three ways to concentrate a metal; Chuquicamata ASTER PD; coal seam CC BY; swamp to coal; oil and gas under an upfold; AI building site; times of making and using); method (computing a concentration factor) + example (copper, two textbooks); dated{2025} (copper reserves 980 Mt / 23 Mt a year); defines ore deposit + concentration factor (one definition), aggregate, reserve; vein and placer named in prose; coal, oil and gas told only (ranks, source/reservoir/seal/trap left to Book 2 g11); groundwater recalled from g6. 20 new ledger rows (USGS smartphone, Perkins, Earle x6, USGS gold GIP x2, EIA x3, USGS OFR 02-206, TOS sand (UNEP), USGS MCS 2025 x2, Commons x2). Page count 8 of 10: the chapter is complete; the remaining pages go to g9.4/g9.5 if they need them |
| g9.4 `landforms` | written, 0/0/0, gates OK | 9 (10) | 12 exos (4/6/2) + 12-q problem (final: the cliff edge would reach the coast road in 2063, 30.4 m at the 2004--2024 average of 0.78 m a year; 2050 for the 10 m margin, 2043 if the rate doubled; the survey is exercise data, kept within sdnp:birling); figdata cliff_retreat.py (survey, intervals, forecasts, Tibetan net rise 0.46 mm a year); 4 tests; 10 figures (Seven Sisters CC BY-SA; uplift/erosion balance; barchan plan + profile; ISS barchans NASA PD; cliff retreat in three panels; longshore drift + spit plan; AI spit; karst block diagram (first use of the blockdiagram pic); Carlsbad stalactites NPS PD; survey chart); safety box (cliff edges and the tide); method (reading a landform: shape, agent and process, material) + table + example (a walk on a plateau); defines uplift, dune (slip face), cliff, beach + longshore drift + spit (one definition), karst + cave + sinkhole (one definition); barchan, notch, wave-cut platform, stalactite, stalagmite in prose; acids recalled from chemistry. 14 new ledger rows (NT Birling Gap x2, SDNP Birling Gap, NOS coastal currents, NPS karst / speleothems / aeolian / White Sands, USGS sinkholes, NMBGMR White Sands, NASA EO coccoliths, Commons x3). Wikipedia pages read only as maps to primary sources (Earle Physical Geology, BGS refused: 403 / 404); spit formation and the notch-to-platform sequence printed as qualitative process, with the NOAA and Birling Gap rows as anchors |
| g9.5 `maps-of-the-earth` | written, 0/0/0, gates OK | 9 (10) | 12 exos (4/6/2) + 12-q problem (final: the footpath S--B--W--T is 4.2 km long and climbs 401 m; legs 3.6 / 2.5 / 2.35 cm at 1 : 50 000, spot heights 296 / 143 / 335 / 544 m; Q10 1 h 43 min at 4 km/h + 1 min per 10 m of climb; Q11 the reverse walk climbs 153 m); figdata projections.py (Mercator + Mollweide of ne-land-50m; Greenland 2.135 vs African mainland, cut at Suez, 29.317 Mkm2: true ratio 13.7, 0.93 on Mercator; factor 1/cos^2: 4 at 60 deg, 10.5 at 72 deg; equal circles of 7 deg), varden_topo.py (1 : 50 000 window 2--8 x 1.8--6.2 km of the shared region; contour labels, profile C--D, crossings, footpath with monotonic legs), trilateration.py (beacons A/B/C, 5/10/5 km, false point F; GPS travel time 0.067 s); 11 tests; 7 figures (two projections with circles; hill sliced every 100 m; topographic map + profile C--D; Lena delta Landsat USGS PD; three circles on a flat map; GPS IIF NASA PD + AI surveyor; problem path map); methods (using a numerical scale; drawing a topographic profile) + examples (Greenland and Africa; a walk at 1 : 25 000); defines map projection (Mercator, equal-area in the definition), numerical scale + scale bar, topographic map, contour line + contour interval, remote sensing + satellite image, satellite positioning; spot height and index contour in prose (owner here; g9.2 used contours with a forward pointer). 4 new ledger rows (usgs:landsat1, gps:constellation via archive.gps.gov since gps.gov/systems/gps/space is 404, Commons x2); light speed from const:c |

## Page projection

- Course-text target: grades 1--5 12 x 7 = 84 pp; grades 6--9 20 x 10 =
  200 pp; **284 pp of course text**. Solutions ~52 pp (grades 1--5 ~1.5 pp
  per chapter, grades 6--9 ~2 pp + problem), front matter, part pages, index
  ~30 pp: **~340--360 pp in all** (the ~300 pp brief target refers to the
  course text).
- Alarm: course text under ~256 pp at a checkpoint (more than 10 % under)
  means restore depth before going on.
- Checkpoints (write the measured pages here): after g4.1 (8 ch.), at each
  grade end, after g7.3, g8.3, g9.5.

| checkpoint | chapters | measured body pp | projected | verdict |
|---|---|---|---|---|
| Phase A | pilot only | 9 (g7.1) | 284 | --- |
| grade 6 end | 17 written + pilot | 117 for 17 ch. (grades 1--6; grade 6: 38 pp for 5 ch., 7.6 per ch. vs 10) + 9 | 117 + 9 + 14 x 7.6 = 232 | **ALARM** (-18 %): grade-6 chapters ran 7--8 pp. Restored: g6.1 +2 pp, g6.3 +1 pp (grade 6 now 41 pp: 9/7/8/8/9, grades 1--6 = 121). Projection 121 + 9 + 14 x 10 = 270 (-5 %), PROVIDED the 14 remaining chapters reach 10 pp each: plan each with 5--7 figures, two boxes, a method and an example per main section |
| grade 5 end | 12 written + pilot | 78 for 12 ch. (target 84; 93 %) + 9 | 78 + 200 = 278 | ok (-2 %); grades 1--5 done: 78 pp vs 84 |
| grade 4 end | 9 written + pilot | 57 for 9 ch. (target 63; 90 %) + 9 | 57 + 21 + 200 = 278 | ok (-2 %); grades 1--4 run ~6.3 pp; grades 6--9 chapters must reach their 10 pp |
| after g7.3 | 19 written + pilot | 152 for 20 ch. (grades 1--6: 121; g7.1 9, g7.2 12, g7.3 10) | 152 + 12 x 10 = 272 | ok (-4 %); grade-7 chapters reach 10--12 pp; keep the 12 remaining chapters at 10 pp |
| after g8.3 | 24 written + pilot | 192 for 25 ch. (to g7.3: 152; g7.4 9, g7.5 9, g8.1 8, g8.2 7 -> 8, g8.3 7 -> 8: 194 after the depth pass) | 194 + 7 x 10 = 264 | ok (-7 %), but grade 8 runs 8 pp: g8.2 and g8.3 were each given a method / example / box (+1 pp each). The 7 remaining chapters (g8.4--g9.5) have to reach 10 pp: plan 6--7 figures, a method + example per main section, two boxes |
| grade 9 end = Phase B done (2026-10-23) | 32 of 32 | measured from the .toc, chapter pages only (part pages excluded): grades 1--5 74 (g1 13, g2 11, g3 12, g4 18, g5 20) vs 84; grades 6--9 174 (g6 40, g7 49, g8 41, g9 44) vs 200; **248 vs 284** | 248 (final) | **ALARM** (-12.7 %): grade-8 chapters stayed at 8 pp and g9.3 at 8. Depth pass before Phase C (target >= 256, i.e. +8 pp): one real addition (method + worked example, or a sourced box, or a figure from data already fetched; no new web sources: budget at 595/600) to g6.2, g6.3, g6.5, g8.1, g8.2, g8.3, g8.4, g9.3, chosen where the last page is short so that ~1 page adds a page. Status of the pass in the 'Depth pass' list below |
| after g4.1 | 7 written + pilot | 45 for 7 ch. (target 49; 92 %) + 9 | 45 + 35 + 200 = 280 | ok (-1.4 %); g1.2--g3.1 at 6 pp: keep later grade-4/5 chapters at 7+ |

### Depth pass (after Phase B, 2026-10-23)

One addition per chapter, ~1 page; each built, gated, tested and
FIGCHECKed like a chapter. **Done (2026-10-23), six additions:**
- g6.2: the Pole Star rule (height above the northern horizon = latitude),
  a geometry sketch, example "A navigator at night" (new source NSTA-POLARIS,
  row nsta:polaris-latitude: 1 web search + 1 fetch, budget now 597).
- g6.5: dissolved pollution drifts downhill with the groundwater: sketch,
  method "Is a well at risk?", example "A new fuel tank for the farm".
- g8.2: example "Four towns, four belts" + chart (figdata/grade-8/rain_by_belt.py,
  re-reads the grade-5 NOAA normals; 2 tests).
- g8.3: a barometer's record as the weather map drifts east + example
  (figdata/grade-8/barogram.py; 3 tests; a different station from the problem's town).
- g8.4: the conveyor belt as one loop on the world map + example "How slow is
  the deep water?" (~70 000 km in ~1000 years: ~70 km a year, ~200 m a day;
  figdata/grade-8/conveyor.py; 3 tests).
- g9.3: recycling (US 2024: ~35 % of copper from scrap, new row
  usgs:mcs-copper-scrap from the MCS 2025 PDF already fetched), flow sketch,
  example "The rock that recycling saves" (200 t of 0.5 % ore per tonne).
Considered and dropped for ownership: degree length (Book 2 g10 owns it),
crystal size and cooling (Book 2 g11), groundwater depletion (Book 2 g10),
hypsometry (Book 2 g11), the ozone hole (no source in hand).

**Result:** 248 -> 250 pp of chapters (-12 % vs 284): the additions (about
five pages of material) mostly filled white space left by non-floating
figures and problem pages, so the page count barely moved. The whole book is
324 pp (the batch table's ~300 pp). Left for the main session to rule on:
the thinnest chapters by page count are g2.2 and g4.3 (5 pp vs ~7) and the
grade-8 chapters (8 pp vs ~10).

## Phase C log (2026-10-23)

**Term links.** `--unwrap --apply`, then `--apply`, then a dry run that printed
"links to insert: 0": 6102 links, 136 distinct targets. Homographs and proper
names curated in `tools/term_config/book1_en.py` EXTRA_PROTECT (found by
reading every figure page, then by a scan of capitalised `\omterm` text):
Varden Hills (25 links to "hill"), Caspian Sea, Hawaiian Volcano Observatory,
"fresh lava crust" (the Earth's crust), National Snow and Ice Data Center,
Sea Ice Index, United States Coast Guard, National Weather Service, Panel on
Climate Change, White Sands, Big Spring, "gold hardly weathers" (the verb),
"a sea of snow-covered summits", the g6.3 table header "rock", and every
`\paragraph{...}` run-in heading (like section titles). Left linked on
purpose: Pacific/Indian/Atlantic Ocean, Mediterranean/Red/Norwegian Sea, X
Glacier, Y Desert (the proper name IS the defined thing).

**Post-link figure check** (each figure page at 130 dpi, 300 dpi zooms where
two marks met; FIGCHECK rows marked "post-link"). Fixed: g1.1 weather chart
(cells and row labels), g2.1 rain diagram (wind arrow into the cloud), g5.2
postcards (caption touching), g6.1 distances (dashed connector through
"Jupiter") and planet photos (labels on the caption), g6.3 rock cycle
("weathering" on its arrow) and seven rocks (caption touching), g6.4 strip
(mine label), g6.5 infiltration arrows into their label and well labels on the
ground line, g7.2 effusive ("long lava flows" on the lava), g7.3 seismometer
("mass" overflowing its box, drum label on the arrow), three circles
("epicentre" on circle M3), problem map (grid hidden under the land, so the
squares could not be counted on land: grid now drawn explicitly over land and
sea), g7.4 column (caption touching), g8.1 profile ("tropopause" over the
ozone bar), g8.3 warm front ("nimbostratus" overhanging the cloud), g8.4
ocean-floor sketch and South Atlantic profile (labels on the land), buoy map
(table touching), g8.5 U-valley (moraine label across the old V), bars (value
on grid line), g9.1 Mauna Loa CO2 (the 300 ppm reference line lay on the axis:
ymin 290), g9.4 spit (label out of the frame), g9.5 topographic map (scale
label under contours) and positioning (R, F labels; now read from
trilateration.py part points instead of typed in). Prose: "the borehole of
the hook" / "the question of the hook" (writer's jargon) rewritten.

**Solutions re-read** (scripted: each question printed beside its answer,
all 32 chapters). Slips fixed: g7.2 "more than about 160" -> "more than 160";
g8.1 ex. 10b answer clarified (11 km vs the 7--20 km range, middle latitudes);
g9.3 two divisions bracketed (`3e8 / (5e1)`, `3.2e6 / (1.6e5)`); g9.5 ex. 5a
rewritten (the area reasoning ran backwards); "must" softened twice (g2.1,
g4.1 solutions). Every other answer agrees with its question and with
`figdata/out` (quake counts, GISTEMP decades, footpath numbers).

**Gates.** `tools/gates.sh grade-1..9` all OK; `make test Y=grade-N` all
green (335 tests in 68 files); `make figdata Y=grade-N` regenerates all 261
`figdata/out/grade-*` files byte-identical (sha256 before/after);
`check_ledger.py` OK (1278 rows in all ledgers; Book 1: 285 rows, 215 source
keys); calibration OK for every grade; problem numbering OK (32 chapters);
`ai_stubs.py --book 1 --list` empty, no PNG in `images/book1/ai/`.
DEFINITIONS.md: all rows W (two labels changed when written: g4.3
`range`, g6.5 "well" merged into the `spring` box).

## Search budget (about 600 for the book)

| phase | web searches | page fetches | downloads / probes | running total |
|---|---|---|---|---|
| Phase A provenance | 2 | 2 | 1 | 5 |
| Phase A dataset URL probes (HEAD/size only) | 0 | 0 | 10 | 15 |
| Phase B g1--g2 (normals x4, NSIDC x2, NE x3, USGS water, NOS x3, Commons x2) | 0 | 15 | 0 | 30 |
| Phase B g3 (Commons search x2 + info/get x6, USGS grain, NOAA x3, CIA Factbook x2 (retired: redirects to a farewell page), NatGeo x4) | 4 | 16 | 0 | 50 |
| Phase B g5.3 (Commons search x4 + info/get x4, NOAA fetch x1) | 0 | 9 | 0 | 154 |
| Phase B g6.1 (Commons search x8, info/get x5, NASA pages x5) | 0 | 18 | 0 | 172 |
| Phase B g6.2 (RMG x4, Gutenberg x1, Commons x6) | 0 | 11 | 0 | 183 |
| Phase B g6.3 (NPS x5, USGS x3, geology.com x5, Commons x24) | 0 | 37 | 0 | 220 |
| Phase B g6.5 (Heath WSP 2220 PDF, USGS WSS x3, Commons search x2 + info/get) | 0 | 7 | 0 | 244 |
| Phase B g7.2 (web search x3, USGS FS 036-00 / FAQ x2 / FS 113-97 / VHP x3 / TDE x2 / Volcano Watch, Commons search x8 + info/get x10) | 3 | 29 | 0 | 276 |
| Phase B g7.3 (web search x3, USGS EQ science/magnitude/GIP severity/MMI/largest, NWS tsunami FAQ/about/during, Commons search x8 + info/get x8) | 3 | 30 | 0 | 309 |
| Phase B g7.4 (web search x2, USGS GIP x3, NPS GRCA x3, NPS ripples/NABR/glossary x6 incl. 404s, UCMP x6 incl. 404s, NOAA x2, USGS coal FAQ, Smithsonian x2 (blocked), Commons search x13 + info/get x12) | 2 | 36 | 0 | 347 |
| Phase B g8.1 (NOAA JetStream 403, NWS radiosonde, NASA ozonewatch 404, UCAR x3, USSA 1976 PDF, Commons search x2 + info x5 + get x2) | 0 | 16 | 0 | 391 |
| Phase B g8.2 (NOS trade winds, Met Office x2 (one 404), UCAR 404, JetStream sea breeze via WebFetch x2, Commons search x2 + info + get) | 0 | 9 | 0 | 400 |
| Phase B g8.3 (web search x3, Met Office x8 (four 404), NOAA JetStream via WebFetch x2 (one 404), NOAA stories 404, SciJinks (DNS fail) x3, BoM, MetService 404, UCAR fronts, Nature (Bauer 2015), Commons info + get) | 3 | 19 | 1 | 423 |
| Phase B g8.4 (web search x3, NOS ocean facts x9, Wikipedia Challenger, Edinburgh Challenger, DOSITS (refuses curl) x2, NOAA x3, Commons search x2 + info x2 + get x2) | 3 | 23 | 0 | 449 |
| Phase B g8.5 (web search x3, NSIDC x13 (five 404), USGS LGM FAQ, USGS glossary x4 (one 404), NPS x3 (one empty), UW News, Commons search x8 + allimages x3 + info x5 + get x5) | 3 | 30 | 0 | 482 |
| Phase B g9.1 (NASA EO ice cores, NOAA GML trends, GISTEMP page, Commons search x3 + info x2 + get x2 + raw x1; IPCC SPM text read from the scratch copy already fetched) | 0 | 12 | 0 | 494 |
| Phase B g9.2 (web search x3, USGS HVO x2, NDBC DART x2, IRIS, Exploratorium, USGS VHP (404) x2, Ready.gov (curl 403, then WebFetch), FEMA glossary, Commons search x4 + info x2 + get x2 + raw x2) | 3 | 13 | 10 | 520 |
| Phase B g9.3 (web search x5, Earle x3, Perkins, TOS, UNEP (403), USGS smartphone, USGS OFR, USGS gold GIP, EIA x3, KGS (TLS error) x3, MCS 2025 appendix + copper PDFs, Commons search x4 + info x4 + get x4) | 5 | 17 | 10 | 552 |
| Phase B g9.4 (web search x3, NT via WebFetch, Earle Physical Geology x4 (403, also via WebFetch and the usask mirror), BGS x2 (404), NPS x7 (three 404), USGS sinkholes, NMBGMR, NASA EO, BGS Earthwise (500), Commons info x3 + get x3; Wikipedia raw x7 read as maps only) | 3 | 22 | 6 | 583 |
| Depth pass (web search x1, NSTA fetch x1) | 1 | 1 | 0 | 597 |
| Phase B g9.5 (USGS Landsat 1, gps.gov (404) then archive.gps.gov x2, NASA/USGS Lena page, Commons search x2 + info x2 + get x2) | 0 | 12 | 0 | 595 |
| Phase B g7.5 (web search x3, USGS geotime x4, USGS GIP x5, NPS x3, NCSE, Nature (Hublin), Earthlearningidea PDF, OpenText/UCMP/other x5, Commons search x2 + info/get x2) | 3 | 24 | 1 | 375 |
| Phase B g6.4 (web search x3, SciAm, USGS OFR PDF, USGS TDE inside, Guinness, IIR, ESRF, APS, NBI, Commons x3) | 3 | 14 | 0 | 237 |
| Phase B g5.2 (Commons search x6 + info/get x6, web search x1, WMO/NCEI/USGS fetch x3) | 1 | 15 | 0 | 145 |
| Phase B g5.1 (Commons search x2 + info/get x8, web search x1, Syvitski PDF x1) | 1 | 11 | 0 | 129 |
| Phase B g4.2--g4.3 (Commons search x5 + info/get x13, ShakeOut, Britannica x6 (403), NatGeo x13, web search x2) | 7 | 33 | 0 | 117 |
| Phase B g4.1 (Commons search x8 + info x4 + get x8, WMO x3, Met Office x2, Everest search 1 + fetch 1) | 9 | 10 | 8 | 77 |

Estimate for Phases B--D: ~550 (ledger-heavy: g4.3, g6.4, g6.3, g7.2,
g7.3, g7.5, g8.1, g8.4, g8.5, g9.1, g9.2, g9.3, g9.4, g9.5).

## Recall, not define (terms used in Book 1, owned elsewhere)

- Physics: day and night, sunrise (g1); evaporating/condensing, melting/
  freezing, air, wind, Moon (g2); temperature, thermometer, degree Celsius,
  season, year (g3); compass, star, planet, Solar System (g4); atmosphere,
  air pressure, barometer (g5); changes of state, axis, orbit, density
  (g6/g7); light-year (g8); gravitation, order of magnitude (g9); P and S
  waves, seismogram reading (later volumes); radioactive decay; Coriolis
  effect (told as "deflection"); the water cycle; the greenhouse model.
- Chemistry: composition of air (g4); raw material, ore, resource,
  renewable resource (g5); greenhouse gas, fossil fuel (g8); element
  abundance, acids and pH (g9); ozone the molecule.
- Biology: soil and humus, species, extinct, biodiversity, living thing;
  fossils as evidence of evolution.
- Book 2: humidity, dew point, albedo, tropical cyclone, tornado, drainage
  basin, discharge, upwelling, thermocline (g10); subduction, hotspot track,
  lithosphere, asthenosphere, seafloor spreading, Moho, core--mantle
  boundary, igneous rock names (g11); metamorphism, heat flow, ice cores,
  glacial period, interglacial, glacial cycle, radiative forcing, feedback
  (g12).
- Wording rules: "molten rock" before g7.2 (magma); "grains of sand and
  mud" before g7.4 (sediment); "where one plate sinks under another"
  (never "subduction zone" as a term) in g7.2; a tropical cyclone is
  described in g5.3, not defined.

## Conventions (Book 1)

Settled by the pilot:
- World maps: `ommap` + `shared-geo-*`; school set for boundaries; teeth table, never a decoration on a jump path.
- Plate names on maps: `\scriptsize\bfseries`, white fill at 75 % opacity, placed off the boundary lines.
- `term_config/book1_en.py` EXTRA links the short form "plate(s)" and the plural boundary phrases.

Set in Phase A:
- Grades 1--5: 10--11 exercises, mostly one star, no problem; grades 6--9:
  exactly 12 exercises + a 10--14-question problem in Parts I--III (each
  problem's named final number is in BRIEFS).
- Math guard per grade (BRIEFS header).
- Varden Hills figures import `figdata/shared/region.py` (never copy its
  functions); grade-N scripts write `figdata/out/grade-N-<name>-*.dat`.
- New datasets go in ONE appended `# Book 1:` block in `tools/fetch_data.py`
  (ownership rule 1 allows it), ids `grade-N-*`, outputs
  `data/derived/grade-N-*.csv`, terms verified and reported.
- `\cref` to chapters of this book; other volumes and series in prose only.
- Ledger ids: `<source>:<item>`, grep `sources/data_ledger.md sources/ledger/`
  before minting; Book 1 prefixes in use: `usgs:`, `pb2002:`.

## Traps (met or foreseen)

- Gate 7 fails on "at home" (e.g. "stay at home" in storm advice): write
  "indoors".
- Gate 7b fails on the verb "collect" near riverbed / cliff / cave / quarry
  ("pebbles collect in riverbeds"): write "lie in", "gather on".
- `region.trace` returns lines in arbitrary direction: orient any line that
  carries side symbols (fronts in the g8.3 weather map too: symbols on the
  LEFT of the path).
- ETOPO is at 1 degree: no narrow feature (a trench's floor, a summit) is
  read from it --- profiles say "smoothed", heights come from the ledger.
- Book 2 g12 pilot already has `figdata/grade-12/climate_records`: Book 1's
  g9.1 script is its own (`figdata/grade-9/climate_records.py`, different
  name prefix in `figdata/out/`), reading the shared datasets; never import
  Book 2's script.
- Scratch builds of world maps need latexmkrc's raised memory flags.
- The CIA World Factbook is retired (2026): its URLs redirect to a farewell
  story. Ocean sizes come from NOAA (NOS "biggest ocean", Ocean Exploration
  "smallest ocean"); the continent order from National Geographic Education
  (`/resource/Continent/` with a capital C; lowercase is a 404).
- The style file has no `booktabs`: tables use `\hline`.
- `omfigure` has no counter: `\cref{fig:...}` prints "Section N.M". Refer to a
  figure as "the map below" or "on page~\pageref{fig:...}", never by \cref.
- No `omAccent` colour exists; pick from the om* list or plain xcolor.
- Orthographic clipping: orient NE rings by the lon/lat shoelace (they are cut
  at 180 and Antarctica runs to -90); a tangent-plane test fails on
  Afro-Eurasia (one ring, > 90 degrees across).
- Commons titles can lie: "File:Nile River Delta (MODIS 2016-01-03).jpg" shows
  Chesapeake Bay. Always look at a downloaded photo before using it.
- Non-floating `omfigure`: a tall figure that does not fit leaves a blank
  half page. Put two related images side by side in one omfigure, or shrink.
- TikZ `ellipse (\a and \b)` with macro radii breaks pgfmath ("0.2and"):
  write `ellipse [x radius=\a, y radius=\b]`.
- The quote gate fails on straight quotes inside `\pgfmathparse{... ? "c1" : "c2"}`:
  alternate colours with `\ifodd\i\def\c{..}\else\def\c{..}\fi`.
- `% ledger:` comments take ids only (no `ics:base.*` wildcard): list the ids,
  explain in the free text after "(".
- A fault line from a region section runs on above the ground if drawn between
  fixed heights: stop it at the ground (`varden_history.fault_line`).
- Search budget after g7.5: 375 of ~600 with 10 chapters left: keep each
  remaining chapter near 20 searches/fetches (reuse fetched pages, prefer
  one rich source per topic).

## Open items for the sync (Phase A report)

1. Owner of "scale" (g2 proposed; g9 keeps "numerical scale").
2. "Ocean" listed for both g2 and g3 in the map (g2 proposed).
3. Mohs scale and outer/inner core: Book 1 (g6) vs Book 2 (g11) claims.
4. Convection cell (g8, descriptive) to be recalled by Book 2 g12.
5. Style-file additions: weather icons, compass rose, hypsometric palette.
6. Four small new datasets for the `# Book 1:` block of `tools/fetch_data.py`
   (NOAA normals, NSIDC sea ice, Natural Earth places / rivers / lakes;
   IBTrACS optional) --- reported, no ruling needed.
7. g7.1 pilot exercise 12 fix in Phase B (the pilot is a Book 1 file; the
   brief allows fixing a defect).
