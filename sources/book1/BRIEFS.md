# Book 1 (grades 1--9) --- chapter briefs (Phase A, 2026-10-22)

Owned by the Book 1 writer. One brief per chapter, outline order. The term
list (one row per term, with labels) is `DEFINITIONS.md`; open questions for
the sync are marked **[SYNC]**.

Legend for figures: **S** schematic (TikZ/pgfplots, no external data),
**F** figdata (a tested script `figdata/grade-N/<name>.py` -> `figdata/out/`),
**AI** generated illustration (generic scene, JPEG, reviewed),
**P** photograph (public domain or verified CC; credited). Targets count the
course text only (schematics); AI images and photographs come on top.

Conventions for the whole book:
- Label stems `def:gN:<slug>:<name>`; recalls of earlier chapters with
  `\cref{ch:...}`; of another volume or series in prose only.
- Math guard: whole numbers only in grades 1--3 (no decimals, no fractions,
  no "half" written as 1/2 --- words like "half" are fine); fractions from
  grade 4; percentages from grades 6--7; powers of ten from grade 8;
  scientific notation from grade 9; no equation with an unknown beyond one
  step before grade 8.
- Calibration: grades 1--5: 10--11 exercises, mostly one star, never
  decreasing, no problem; grades 6--9: exactly 12 exercises, never
  decreasing, one weekend problem of 10--14 questions in Parts I--III.
- Page targets: grades 1--5 ~7 pp of course text per chapter, grades 6--9
  ~10 pp (the pilot is 9 pp + 2 pp of solutions). Course text 12x7 + 20x10
  = 284 pp; with solutions, front matter, part pages and index the book
  lands near 330--350 pp.
- The youngest readers first: grades 1--5 short sentences, one idea per
  paragraph, an illustration on almost every page, every number a whole
  number a child can picture ("about as tall as 3 school buses").
- Observation only. Gate traps to avoid in the wording: the phrase "at home"
  (gate 7 fails: write "indoors", "in the house"), and the verb "collect"
  near riverbed / cliff / cave / quarry (gate 7b: write "pebbles lie in the
  river", never "pebbles collect in riverbeds").
- Every real-world number: a row in `sources/ledger/book1.md` (or a shared /
  Book 2 row cited read-only) and a `% ledger:` comment.

---

## Grade 1

### g1.1 `watching-the-weather` --- Watching the Weather (~7 pp)

- **Hook**: a child wakes up, looks out of the window: grey sky, drops on
  the glass. What to wear today? The window is the first weather station.
- **Sections**: (1) What is the weather? --- sunny, cloudy, rainy, windy,
  snowy, foggy; warm and cold. (2) Weather symbols and the weather chart
  kept for a week (one row a day, morning and afternoon). (3) The weather
  changes: from morning to night, from day to day, from season to season
  (day and night and the seasons are recalled from the physics books).
  (4) Dressing for the weather; safety: storms, and never looking at the Sun
  (`safety` box).
- **Definitions**: weather; weather chart (with weather symbol).
- **Recall**: day and night, the Sun's journey (physics, grade 1: prose);
  the seasons named only (physics, grade 3: prose).
- **Figures**: S the weather symbols (sun, sun-and-cloud, cloud, rain,
  snow, wind, storm, fog) with their names [needs style icons, see report
  item 4]; S a week's weather chart (Monday--Sunday x morning/afternoon,
  icons + "warm/cold"); S a windsock / flag showing where the wind comes
  from; AI x5: child at a rainy window; a sunny park; a snowy street with
  children in coats; kites on a windy hill; a foggy morning at the school
  gate; AI x1: a row of coat pegs with a raincoat, a sun hat, a scarf
  (dressing for the weather).
- **Ledger**: none expected (no real-world number).
- **Exercises**: 10 (8 star, 2 two-star): read the chart (count sunny/rainy
  days, compare mornings and afternoons), match clothes to weather, draw
  the symbol, order a day's sky pictures.

### g1.2 `landscapes-around-us` --- Landscapes Around Us (~7 pp)

- **Hook**: from the top of a hill, a child and her grandfather look down
  at the village, the river, the fields, and far away a line of blue sea.
- **Sections**: (1) What a landscape is (what we see in one look, near and
  far: foreground, middle, background). (2) The shapes of the land:
  mountains, hills, valleys, plains. (3) Water in the landscape: rivers,
  lakes, the coast. (4) Natural and built parts of a landscape. (5)
  Describing and drawing a landscape (method: three bands, then the
  shapes, then the water, then the built parts).
- **Definitions**: landscape; landform (mountain, hill, valley, plain);
  river, lake, coast (one definition "Water in a landscape"); natural part,
  built part (one definition).
- **Recall**: none (first chapter of its strand).
- **Figures**: S a side view from mountain to sea with every landform
  labelled; S the three bands of a landscape drawing (foreground, middle,
  background) as a method sketch; S natural/built sorting chart; AI x4:
  a mountain valley with a village; a wide plain with a river and fields;
  a coast with a beach and a harbour; a lake among hills (all generic, no
  named place); P x1: a real valley seen from above, public domain (e.g. a
  U.S. National Park Service photograph; to verify), labelled with
  mountain / valley / river.
- **Ledger**: the photograph's credit only (CREDITS.md).
- **Exercises**: 10: name the landform in a picture, natural or built,
  which is higher, describe a picture in three bands.

## Grade 2

### g2.1 `water-on-earth` --- Water on Earth (~7 pp)

- **Hook**: a photograph of the whole Earth from space: mostly blue.
- **Sections**: (1) The blue planet: about 7 parts out of 10 of the Earth's
  surface are covered by water (whole-number picture: 7 squares out of
  10). (2) Salt water: oceans and seas; the sea tastes salty (about 35 g of
  salt in each litre). (3) Fresh water: rivers, lakes, ice and snow,
  water under the ground (told; the underground is grade 6). (4) Out of
  100 buckets of all the water on Earth: about 97 salty, 2 of ice, 1 under
  the ground, rivers and lakes less than one bucket. (5) Where rain goes:
  it soaks into the ground, runs into rivers and back to the sea, or rises
  again into the air (recall evaporating and condensing from the physics
  books).
- **Definitions**: ocean, sea; salt water, fresh water.
- **Recall**: water as ice, liquid and steam; evaporating and condensing
  (physics, grade 2, prose); rivers and lakes (`\cref{ch:g1:landscapes-around-us}`).
- **Figures**: P the Earth from space (NASA, public domain: an Apollo 17
  "Blue Marble" AS17-148-22727 or a Pacific-centred NASA Blue Marble; to
  verify); F `ocean_fraction.py` -> a 10 x 10 grid with the computed number
  of blue cells (and the 7-out-of-10 strip); F `water_shares.py` -> 100
  buckets coloured by where the water is (largest-remainder rounding so the
  total is exactly 100); S where rain goes (cloud, rain, soaking in, a
  river to the sea, arrows back up); AI x4: a beach and the open sea; a
  river through meadows; a lake with a boat; snowy mountains with a
  glacier tongue (generic).
- **Ledger**: share of the surface covered by ocean (USGS Water Science
  School or NOAA: "about 71 percent") and the computed check; the world's
  water distribution table (USGS, Shiklomanov 1993, oceans 96.5 %, ice
  1.74 %, groundwater 1.69 %, fresh lakes and rivers); mean salinity about
  35 g per kg (NOAA).
- **Datasets**: `data/derived/etopo-1deg.csv` (shared).
- **Exercises**: 10: salt or fresh, count the blue cells, where does the
  rain go, order buckets.

### g2.2 `drawing-to-map` --- From a Drawing to a Map (~7 pp)

- **Hook**: a bird flies over the school and sees only roofs, the yard and
  the paths: the view from above.
- **Sections**: (1) Seen from the side, seen from above (toy blocks). (2)
  The plan of a room, drawn smaller on squared paper: 1 square for 1 metre
  (the scale). (3) The plan of a street; symbols and the legend; the title.
  (4) The four cardinal directions and the compass rose; north at the top
  of most maps. (5) A map of a real-looking place: the Varden Hills, the
  invented region of the series, simplified (hills, river, road, bridge,
  farm, wood), read with its legend and compass rose.
- **Definitions**: plan; map; legend (map symbols); scale **[SYNC: proposed
  here, see report item 2]**; cardinal directions and compass rose.
- **Recall**: the Sun rises in the east and sets in the west (physics,
  grade 1, prose; never look at the Sun).
- **Figures**: S blocks seen from the side and from above; S a classroom
  plan on a grid with a legend (1 square = 1 metre); S the compass rose
  [style pic requested]; F `varden_plan.py` -> simplified map of the Varden
  Hills (areas above 350 m shaded as "hills", the river, a road, the bridge
  where it crosses the river, a farm on dry ground, a wood), with legend
  and compass rose; AI x2: a child drawing a plan of her bedroom on squared
  paper; a hot-air balloon view down on fields and a village.
- **Ledger**: none (the region is in the shared ledger).
- **Exercises**: 11: count squares to find lengths, place a symbol, which
  direction is the river from the farm, read the legend.

## Grade 3

### g3.1 `stones-pebbles-sand` --- Stones, Pebbles and Sand (~7 pp)

- **Hook**: on a river bank a child picks up a smooth, round pebble;
  higher up the valley the stones are sharp-edged. Why?
- **Sections**: (1) Rock is the solid ground under the soil (the bedrock;
  seen in mountains and road cuttings --- observation only). (2) From rock
  to pebbles: broken pieces of rock, rounded as rivers and waves roll them
  (sharp in the mountains, round near the sea). (3) Sand is broken rock in
  tiny grains; mud is finer still: a size ladder (boulder, pebble, gravel,
  sand, mud). (4) Hard and soft rocks: some scratch glass, some crumble in
  the hand (told; the scratch test is grade 6). (5) The stones we build
  with: walls, roofs, pavements; old towns built of the rock under them.
- **Definitions**: rock and bedrock; pebble (and gravel); sand (and mud);
  building stone.
- **Recall**: soil (the biology books, prose); rivers and the coast
  (`\cref{ch:g1:landscapes-around-us}`).
- **Figures**: S grain-size ladder drawn at true size up to 2 cm (boulder
  shown off-scale with a note); S a cut through the ground: soil on top,
  bedrock below, a river with pebbles; S a pebble's journey: sharp in the
  mountain stream, rounder downstream, round on the beach (sequence of
  outlines); AI x3: round pebbles in a clear stream; sand grains under a
  magnifying glass on a beach; an old stone village street; P x2: building
  stones (a granite wall, a slate roof; Commons or agency, to verify).
- **Ledger**: grain-size limits (sand up to 2 mm, Wentworth 1922 /
  USGS sediment-size page).
- **Exercises**: 10: order by size, sharp or round and why, natural or made
  (stone vs brick), which grains are sand.

### g3.2 `continents-and-oceans` --- The Globe: Continents and Oceans (~7 pp)

- **Hook**: spinning the classroom globe with a finger and stopping it with
  eyes closed: land or sea?
- **Sections**: (1) The globe, a small model of the round Earth. (2) The
  equator, the two poles, the northern and southern hemispheres. (3) Seven
  continents and five oceans (names, where, biggest and smallest, with
  whole-number comparisons). (4) A world map is a flattened globe (the peel
  of an orange cannot lie flat without tearing).
- **Definitions**: globe; equator and hemisphere; pole (North Pole, South
  Pole); continent; world map. (The five oceans are named here; "ocean"
  itself is defined in g2.1 --- see report item 9.)
- **Recall**: ocean and sea (`\cref{ch:g2:water-on-earth}`); the Earth turns
  on itself (physics, prose).
- **Figures**: F `globe.py` -> two orthographic globes (the Atlantic side
  and the Pacific side) from Natural Earth land, with the equator and the
  poles; S the two hemispheres (north and south halves); S world map with
  the continents and oceans labelled (shared land table); F `globe.py`
  (part `gores`) -> the globe cut into 12 gores to show why a flat map
  tears or stretches; AI x2: a child spinning a classroom globe; an orange
  peel laid flat on a table; P x1: the Earth from space showing one
  hemisphere (NASA, to verify).
- **Ledger**: number of continents by the common seven-continent
  convention and the five oceans (NOAA "How many oceans"); areas of the
  oceans (NOAA or the CIA World Factbook, public domain) and ranks of the
  continents (largest Asia, smallest Australia; a sourced table).
- **Datasets**: `ne-land-110m` (shared).
- **Exercises**: 10: name the hemisphere, the ocean between two continents,
  biggest/smallest, is a place near a pole hot or cold (told).

## Grade 4

### g4.1 `clouds-rain-snow` --- Clouds, Rain and Snow (~7 pp)

- **Hook**: a summer afternoon: small white clouds swell into a tower, the
  sky darkens, a shower falls, then the sun returns.
- **Sections**: (1) A cloud is made of tiny droplets of water or crystals of
  ice floating in the air (recall evaporating/condensing; fog is a cloud on
  the ground). (2) Three cloud families: heaped (cumulus), layered
  (stratus), wispy (cirrus), and the towering storm cloud (cumulonimbus);
  how high they float. (3) Rain, snow and hail fall from clouds:
  precipitation. (4) Measuring the weather: the rain gauge (millimetres of
  rain), the thermometer (recalled), the wind vane; a class weather station
  in the schoolyard (observation only); keeping a record and drawing a bar
  chart of a week's rain.
- **Definitions**: cloud (and fog); cloud families (cumulus, stratus,
  cirrus, cumulonimbus); precipitation (rain, snow, hail); rain gauge; wind
  vane; weather station.
- **Recall**: weather and weather chart (`\cref{ch:g1:watching-the-weather}`);
  evaporating, condensing, freezing (physics, grade 2); the thermometer and
  degrees Celsius (physics, grade 3).
- **Figures**: S cloud families by height (low, middle, high) with a km
  scale; S reading a rain gauge (a tube marked in millimetres, the water
  level); S a week's rain as a bar chart (exercise data); S the weather
  station's instruments (shelter at the height the guidance gives, rain
  gauge in the open, wind vane on a mast); P x4: cumulus, stratus, cirrus,
  cumulonimbus (NOAA Photo Library, public domain; to verify each);
  P x1: hailstones (NOAA/NWS, public domain); AI x2: a class reading the
  rain gauge in the schoolyard; children in a snowy street catching
  snowflakes.
- **Ledger**: cloud levels (WMO International Cloud Atlas: low/middle/high
  étages for temperate regions); thermometer screen height and rain-gauge
  exposure (WMO Guide to Instruments, WMO-No. 8); 1 mm of rain = 1 litre
  per square metre (computed).
- **Exercises**: 11 (fractions allowed): name the cloud, read the gauge,
  read and draw the bar chart, which month was wettest.

### g4.2 `volcanoes-earthquakes-first-look` --- Volcanoes and Earthquakes: A First Look (~7 pp)

- **Hook**: night-time pictures of a lava fountain on the news, and the
  same week, a town where the ground shook.
- **Sections**: (1) An eruption: lava, ash and gas come out of a volcano
  (molten rock from deep below --- the chamber and the vent are grade 7).
  (2) What an earthquake does: the ground shakes for seconds, cracks,
  buildings may fall; most are too weak to feel. (3) Some regions far more
  than others: the map of volcanoes and large earthquakes; most around the
  Pacific Ocean (computed share). (4) Staying safe: drop, cover and hold
  on; following the instructions to leave when a volcano wakes.
- **Definitions**: volcano; eruption (lava, volcanic ash); earthquake.
- **Recall**: mountains (`\cref{ch:g1:landscapes-around-us}`); continents and
  oceans (`\cref{ch:g3:continents-and-oceans}`).
- **Figures**: F `ring_of_fire.py` -> world map of Holocene volcanoes and
  M >= 7 earthquakes (shared tables, decimated) with the computed
  circum-Pacific shares; S a volcano drawn simply (mountain, molten rock
  rising, lava flow, ash cloud) without the grade-7 terms; S drop, cover,
  hold on (three-panel pictogram); P x3: a Hawaiian lava flow (USGS HVO,
  public domain); Mount St. Helens, 18 May 1980 (USGS, public domain);
  earthquake damage (USGS, public domain; to verify); AI x1: a class
  practising an earthquake drill under the tables.
- **Ledger**: number of volcanoes active in the last 12 000 years and the
  number of M >= 6 earthquakes per year (computed from the shared
  datasets: data:gvp, data:usgs-comcat); the circum-Pacific shares
  (computed); "drop, cover and hold on" (USGS / ShakeOut guidance page);
  the photos' events (USGS pages).
- **Exercises**: 11: lava, ash or gas; where on the map; what to do; how
  many per year (whole numbers, simple fractions "about 3 out of 4").

### g4.3 `world-physical-map` --- The Physical Map of the World (~7 pp)

- **Hook**: unfolding a physical map of the world on the floor: green
  lowlands, yellow and brown mountains, pale and deep blue seas.
- **Sections**: (1) Reading a physical map: altitude above sea level and
  depth below it, shown by colours (the legend's colour steps). (2) The
  great mountain ranges and the highest summits. (3) The great rivers and
  lakes. (4) Deserts and the great ice. (5) The highest, the longest, the
  largest, with scale comparisons (Everest vs the deepest trench vs a jet's
  cruising height; the Sahara as a fraction of Africa, computed).
- **Definitions**: altitude and sea level; relief; physical map (colours
  for altitude and depth); mountain range.
- **Recall**: map, legend (`\cref{ch:g2:drawing-to-map}`); continents and
  oceans (`\cref{ch:g3:continents-and-oceans}`); landforms
  (`\cref{ch:g1:landscapes-around-us}`).
- **Figures**: F `physical_map.py` -> world physical map from ETOPO1 at 1
  degree, filled altitude and depth bands (5 land, 3 sea steps) with the
  great rivers and lakes (Natural Earth 1:110m, new small dataset) and the
  names of the main ranges, rivers, deserts; S the colour legend as a
  "staircase" from the deepest trench to the highest summit (to scale,
  ledger values); S the highest/deepest comparison column; P x2: the
  Himalaya seen from the International Space Station (NASA, public
  domain); the Amazon from space (NASA); AI x1: two children kneeling over
  a large unfolded map (the map itself blurred, no readable geography ---
  if the generator draws a recognisable continent wrongly, drop it).
- **Ledger**: Everest's height (8 848.86 m, the 2020 survey; primary
  source to find), the Challenger Deep (book1 `usgs:trench-depth` or a
  NOAA value), the longest rivers (Nile, Amazon: a primary compilation,
  e.g. USGS Water Science School; lengths are disputed --- print "about"
  and say so), the largest lake (Caspian Sea area), the deepest lake
  (Baikal), the Sahara's area; the Sahara-to-Africa fraction computed.
- **Datasets**: shared `etopo-1deg`, `ne-land-110m`; **new**
  `grade-4-ne-rivers`, `grade-4-ne-lakes` (Natural Earth 1:110m rivers and
  lake centrelines, lakes; public domain; 38 KB + 37 KB raw).
- **Exercises**: 11: colour to altitude, highest/lowest on the map, order
  rivers by length, fractions of a range.

## Grade 5

### g5.1 `water-shapes-the-land` --- Water Shapes the Land (~7 pp)

- **Hook**: after a night of storm, the stream behind the school runs
  brown: it is carrying the land away, grain by grain.
- **Sections**: (1) Weathering breaks rock where it stands (frost, roots,
  rain water). (2) Erosion carries the pieces away (running water above
  all; also wind, ice, waves). (3) Deposition lays them down where the
  water slows. (4) A river from its source to its mouth: the steep upper
  course and its V-shaped valley, the meanders, the floodplain, the delta
  or estuary. (5) Floods: a river that leaves its bed is doing what rivers
  do; the floodplain is its territory.
- **Definitions**: weathering; erosion; deposition; source and mouth (with
  tributary); meander; delta; flood (with floodplain).
- **Recall**: pebbles and sand (`\cref{ch:g3:stones-pebbles-sand}`); rivers
  (`\cref{ch:g1:landscapes-around-us}`); where rain goes
  (`\cref{ch:g2:water-on-earth}`).
- **Figures**: S the long profile of a river from source to mouth with the
  three courses; S a meander: erosion on the outer bank, deposition on the
  inner bank (map view and cut); S V-shaped valley and floodplain cuts; S a
  delta growing out into the sea; P x2: a delta from space (NASA, public
  domain: the Nile or the Mississippi); meanders from space (NASA/USGS
  Landsat, public domain); AI x3: a brown stream after rain; a frost-
  shattered slope of sharp stones (generic); a meadow under flood water.
- **Ledger**: sediment carried to the sea by the world's rivers per year
  (Milliman and Syvitski 1992 or a later compilation; printed only as
  "billions of tonnes" if a primary source is fetched); the delta and
  meander photographs' places.
- **Exercises**: 11: name the process, where on the meander, order the
  river's parts, fractions of a river's length.

### g5.2 `weather-and-climate` --- Weather and Climate (~7 pp)

- **Hook**: two postcards in the same week of January: children on a sunny
  beach, children building a snowman.
- **Sections**: (1) Weather is today; climate is the weather's usual
  pattern over many years (30 years by the meteorologists' rule). (2) The
  climate chart: temperature curve and rainfall bars (method). (3) Hot,
  temperate and cold zones, between the tropics, the polar circles and the
  poles (the seasons recalled from the physics books). (4) Three extreme
  climates: deserts, rainforests, polar regions.
- **Definitions**: climate; climate chart; climate zone (hot, temperate,
  cold); tropic and polar circle; desert; rainforest.
- **Recall**: weather (`\cref{ch:g1:watching-the-weather}`); rain gauge,
  thermometer (`\cref{ch:g4:clouds-rain-snow}`); the year and the seasons
  (physics, grade 3, prose); equator, poles (`\cref{ch:g3:continents-and-oceans}`).
- **Figures**: F `climate_charts.py` -> four climate charts from the NOAA
  1991--2020 monthly normals: a hot desert (Phoenix), a rainforest (Hilo),
  a temperate city (Seattle), a polar town (Utqiaġvik); S how to read a
  climate chart (one chart annotated); F `climate_zones.py` -> world map
  with the hot, temperate and cold zones bounded by the tropics and polar
  circles computed from the obliquity (shared row earth:obliquity); P x3:
  a desert (U.S. National Park Service, public domain), a rainforest
  (USDA Forest Service, El Yunque, public domain), a polar landscape
  (NOAA/NSF, public domain), each to verify; AI x2: the two postcards of
  the hook (a beach, a snowman).
- **Ledger**: the 30-year normal (WMO); obliquity (shared); the station
  normals (new dataset rows).
- **Datasets**: **new** `grade-5-noaa-normals` (NOAA NCEI U.S. Climate
  Normals 1991--2020, monthly, four stations USW00023183 Phoenix,
  USW00021504 Hilo, USW00024233 Seattle, USW00027502 Utqiaġvik; public
  domain; ~145 KB raw, ~2 KB derived).
- **Exercises**: 11: weather or climate sentence, read a chart (wettest
  month, coldest month), which chart is which place, which zone.

### g5.3 `natural-hazards` --- Natural Hazards (~7 pp)

- **Hook**: on the radio, a warning: a strong storm will reach the coast
  tonight; families bring in the garden chairs and check their torches.
- **Sections**: (1) What a natural hazard is. (2) Hazards from the air:
  storms, tropical cyclones (a description, not a definition: Book 2 owns
  the term --- report item 3), droughts, heat waves. (3) Hazards from
  water: floods (recalled). (4) Hazards from the ground: earthquakes,
  eruptions (recalled), landslides. (5) A hazard becomes a disaster where
  people live; warnings and safety rules (staying indoors in a storm,
  moving to high ground in a flood, drop-cover-hold on).
- **Definitions**: natural hazard; storm; drought; landslide; natural
  disaster.
- **Recall**: volcanoes and earthquakes
  (`\cref{ch:g4:volcanoes-earthquakes-first-look}`); floods
  (`\cref{ch:g5:water-shapes-the-land}`); climate zones
  (`\cref{ch:g5:weather-and-climate}`).
- **Figures**: S the same valley twice: a flood with no one there (a
  hazard) and with a village (a disaster); S a chart of hazards by origin
  (air, water, ground); F `cyclone_tracks.py` (**optional**, if the IBTrACS
  "last 3 years" file is light enough) -> map of tropical cyclone tracks
  showing that none forms on the equator; S a warning-level ladder (green,
  yellow, orange, red, generic --- no country's scheme); P x2: a
  hurricane seen from the International Space Station (NASA, public
  domain); a landslide (USGS, public domain); AI x2: a family listening to
  a warning on the radio; a field of cracked earth in a drought.
- **Ledger**: tropical cyclone names by ocean (hurricane, typhoon,
  cyclone: NOAA); the UN definition of a hazard / disaster (UNDRR
  terminology, read for wording only); cyclone counts if the map is drawn.
- **Datasets**: optional **new** `grade-5-ibtracs` (NOAA NCEI IBTrACS v04,
  last-3-years CSV; public domain with citation; size to check).
- **Exercises**: 11: hazard or disaster, which family, what to do, read the
  map.

## Grade 6

### g6.1 `earth-a-planet` --- The Earth, a Planet of the Solar System (~10 pp)

- **Hook**: three robot probes send postcards home: from Venus (hot enough
  to melt lead, under a crushing sky), from Mars (a cold red desert), from
  the Earth (blue and white, with oceans).
- **Sections**: (1) The Solar System recalled; rocky planets and giant
  planets (size and density from the NASA fact sheets, computed table).
  (2) Earth, Venus and Mars compared: temperature, air pressure, water.
  (3) What makes life possible on the Earth: liquid water, a temperature
  range, an atmosphere, the right distance from the Sun (told; the
  habitable zone is Book 2's). (4) The Earth seen from space.
- **Definitions**: rocky planet; giant planet.
- **Recall**: star, planet, the Solar System (physics, grade 4); orbit and
  axis (physics, grade 6); air pressure (physics, grade 5); density
  (physics, grade 6); water on Earth (`\cref{ch:g2:water-on-earth}`).
- **Figures**: F `planets.py` -> the eight planets as circles to scale
  (diameters) and a bar chart of densities (rocky vs giant), values from
  the shared NASA rows (test re-reads `sources/data_ledger.md`); F
  `planets.py` (part `temp`) -> mean temperature against distance from
  the Sun; S a comparison panel Venus / Earth / Mars (pressure, mean
  temperature, liquid water yes/no); P x4: the Earth (Apollo 17 or
  Earthrise), Venus (NASA Mariner 10 or Magellan), Mars (NASA/Hubble),
  Jupiter (NASA/Hubble), public domain, to verify.
- **Ledger**: shared `planet:*` rows (diameter, density, Tmean, psurf,
  dist, moons); Venus's clouds of sulfuric acid and Mars's ancient water
  (NASA pages, book1 rows).
- **Exercises**: 12: rocky or giant from density, compare, percentages
  (e.g. Mars's diameter as a percentage of the Earth's).
- **Problem**: *Postcards from three planets* (Parts: the planets compared;
  the air; water and life), 12 questions; named final number: **92 --- how
  many times the Earth's surface pressure presses on the ground of Venus**.

### g6.2 `latitude-longitude` --- Latitude, Longitude and Time Zones (~10 pp)

- **Hook**: a sailor in 1750 could find his latitude from the stars but
  not his longitude; ships were lost. Today a phone does both in a second.
- **Sections**: (1) Parallels and latitude (an angle from the equator,
  0--90 degrees north or south). (2) Meridians and longitude (0--180
  degrees east or west of the prime meridian). (3) Locating any place by
  its two angles (method, with a gridded world map of cities). (4) The
  Earth turns 360 degrees in 24 hours: 15 degrees an hour, and time zones;
  the date line opposite the prime meridian (a history box: Harrison's
  marine chronometer).
- **Definitions**: parallel and latitude; meridian, longitude and prime
  meridian; time zone; international date line.
- **Recall**: globe, equator, poles, hemispheres
  (`\cref{ch:g3:continents-and-oceans}`); day and night and the Earth's turning
  (physics, grades 1 and 6, prose).
- **Figures**: S latitude as an angle at the Earth's centre (cut through the
  globe); S longitude as an angle seen from above the North Pole; F
  `cities.py` -> world map with a 30-degree graticule and a dozen cities
  (Natural Earth populated places) for the exercises; F `time_zones.py` ->
  the 24 ideal time zones of 15 degrees with their hour offsets, and the
  date line (real zones follow borders: told); P x1: the prime meridian
  line at Greenwich (Commons, to verify) or Harrison's H4 (public domain);
  AI x1: an 18th-century ship's navigator with a sextant at night
  (generic, no named ship).
- **Ledger**: 24 h rotation (shared planet:Earth.day); the prime meridian
  adopted in 1884 (a primary history source); Harrison's H4 trial
  (Royal Museums Greenwich page); city coordinates (new dataset).
- **Datasets**: **new** `grade-6-ne-places` (Natural Earth 1:110m
  populated places, public domain; 166 KB raw, ~10 KB derived).
- **Exercises**: 12: read coordinates, place a city, hour difference
  between two longitudes, latitude of the poles, which hemisphere.
- **Problem**: *A video call around the world* (Parts: where the friends
  live; what time it is; crossing the date line), 12 questions; named
  final number: **the local time in the friend's city when the call
  starts** (ideal zones).

### g6.3 `rocks-and-minerals` --- Rocks and Minerals (~10 pp)

- **Hook**: a granite kitchen worktop under a magnifying glass: pink, white,
  grey and black specks, each with flat shiny faces.
- **Sections**: (1) A rock is made of minerals (granite: quartz, feldspar,
  mica). (2) Crystals: regular shapes with flat faces. (3) Three rock
  families by how they form: igneous (molten rock cools), sedimentary
  (grains and shells laid down in layers, then hardened), metamorphic
  (transformed by heat and pressure deep underground). (4) The rock cycle.
  (5) Recognising common rocks (granite, basalt, limestone, sandstone,
  clay, marble, slate: a key) and scratch hardness (Mohs scale; fingernail,
  copper coin, steel, glass, quartz).
- **Definitions**: mineral; crystal; igneous, sedimentary and metamorphic
  rock (one definition "The three rock families"); rock cycle; hardness and
  the Mohs scale. (Rock names are described in a table, not defined: Book
  2's grade-11 chapters own igneous rock names --- report item 3.)
- **Recall**: rock, pebble, sand, building stones
  (`\cref{ch:g3:stones-pebbles-sand}`); lava (`\cref{ch:g4:volcanoes-earthquakes-first-look}`);
  weathering, erosion, deposition (`\cref{ch:g5:water-shapes-the-land}`).
  The word "magma" is not used before g7.2 ("molten rock" here); the word
  "sediment" not before g7.4 ("grains of sand and mud").
- **Figures**: S the rock cycle; S granite as a mosaic of three minerals
  (a drawn enlargement, not a photograph stand-in); S the Mohs ladder with
  the everyday testers; S an identification key (flowchart); P x7--9:
  granite, basalt, limestone, sandstone, marble, slate, clay; quartz
  crystal, mica (Commons: e.g. James St. John CC BY 2.0, or agency
  public-domain specimens; each licence verified through the API); AI x1:
  a child with a hand lens over a speckled stone worktop (generic, no
  readable mineral identity beyond "specks").
- **Ledger**: Mohs hardness of the ten minerals and of the testers
  (fingernail about 2.5, copper about 3.5, steel and glass about 5.5:
  a mineralogical source, e.g. Mindat or a USGS page); granite's three main
  minerals (USGS).
- **Exercises**: 12: which family, read the key, scratch test ordering,
  rock-cycle arrows, percentage of a granite made of quartz (exercise
  data).
- **Problem**: *The stones of the town square* (Parts: the fountain, the
  paving, the roof; a hardness test; the rock cycle), 12 questions; named
  final number: **the Mohs hardness of the hardest stone in the square**
  (quartz, 7), plus the count of rock families present.

### g6.4 `inside-the-earth` --- Inside the Earth (~10 pp)

- **Hook**: the deepest hole ever drilled went down about 12 km and
  stopped: the rock was too hot. The centre of the Earth is more than 500
  times deeper.
- **Sections**: (1) How deep have we been? Mines, boreholes, the record
  borehole, compared with the radius (percentages). (2) Crust, mantle and
  core (thin crust: thicker under continents than under oceans; the
  solid, hot mantle; the liquid outer and solid inner core). (3) How
  earthquake waves tell us the rest (told; history box: Inge Lehmann and
  the inner core, 1936). (4) Temperature rises with depth (deep mines;
  about 25--30 degrees per kilometre near the surface; thousands of
  degrees at the centre).
- **Definitions**: crust, mantle and core (outer and inner) in one
  definition "The layers of the Earth".
- **Recall**: rock families (`\cref{ch:g6:rocks-and-minerals}`); volcanoes
  (`\cref{ch:g4:volcanoes-earthquakes-first-look}`).
- **Figures**: F `earth_layers.py` -> the Earth cut open, to scale, from
  PREM's boundaries (crust drawn at true scale is a hairline: an inset
  enlarges it), the record borehole marked; F `earth_layers.py` (part
  `geotherm`) -> temperature with depth in the first few kilometres at the
  ledger gradient; S the borehole, Everest and the radius on one strip
  (scale break); S continental vs oceanic crust thickness; P x1: Inge
  Lehmann (Commons, licence to verify; drop if not free); AI x1: miners in
  a hot, deep mine gallery (generic).
- **Ledger**: record borehole depth (Kola SG-3, 12 262 m, a primary
  source); crust thicknesses (book1 `usgs:crust-thickness`); PREM radii
  (shared data:prem; earth:Rmean); near-surface geothermal gradient
  (USGS/BGS page); temperature at the centre (a primary paper, e.g.
  Anzellini et al. 2013, printed "about 5 000 to 6 000 degrees" only if
  sourced); Lehmann 1936 (primary history source).
- **Datasets**: shared `prem`.
- **Exercises**: 12: percentages of depth, layer order, thickness compare,
  temperature at a depth from the gradient, solid or liquid.
- **Problem**: *A journey to the centre, to scale* (Parts: the model; the
  layers; the hot inside), 12 questions; named final number: **the
  thickness of the oceanic crust, in millimetres, on a 2-metre model
  Earth**.

### g6.5 `water-underground` --- Water Underground (~10 pp)

- **Hook**: on a hot summer day a spring still runs cold and clear at the
  foot of the hill: where does its water come from?
- **Sections**: (1) Rain soaks in: infiltration (and what runs off).
  (2) Porous and permeable rocks (sand and sandstone vs clay and shale;
  porosity as a percentage). (3) Groundwater and the water table. (4)
  Springs and wells: where the water table meets the ground; a well below
  the water table. (5) Aquifers: the Varden Hills sandstone under the shale
  (the water cycle recalled from the physics books).
- **Definitions**: infiltration; porosity (porous rock); permeability
  (permeable and impermeable rock); groundwater; water table; aquifer;
  spring; well.
- **Recall**: fresh water and where rain goes (`\cref{ch:g2:water-on-earth}`);
  rock families, sandstone, clay (`\cref{ch:g6:rocks-and-minerals}`); the water
  cycle as a ledger (physics, grade 6, prose).
- **Figures**: F `water_table.py` -> a section through the Varden Hills (a
  new section line or A--B) with the water table, the river, a spring and
  two wells (one dry, one wet), importing `figdata/shared/region.py`; S
  pores between grains: sand (connected, permeable) vs clay (tiny, not
  connected) at the grain scale; S infiltration vs run-off on a slope; S a
  well and its water level in the dry and the wet season; P x1: a real
  spring (USGS or NPS, public domain, to verify); AI x1: a village hand pump
  with children filling a bucket.
- **Ledger**: porosity ranges of sand, clay, sandstone, granite (USGS Water
  Science School or Heath 1983 USGS WSP 2220); groundwater's share of
  fresh water (USGS table already used in g2.1).
- **Exercises**: 12: porous/permeable sort, porosity percentage of a
  volume, where to dig a well, does the spring dry up.
- **Problem**: *The farm well of the Varden Hills* (Parts: the rocks under
  the farm; the water in the sandstone; how long it lasts), 12 questions;
  named final number: **the number of days the stored water would supply
  the farm without rain** (porosity x volume / daily use, exercise data).

## Grade 7

### g7.1 `plate-tectonics` --- Plate Tectonics: The Moving Puzzle (pilot, approved)

Written 2026-10-22, 9 pp + 2 pp of solutions, 12 exercises, a 12-question
problem, 9 figures FIGCHECKed. Keep as is; Phase B fixes only the defect in
report item 9 (exercise 12 restates the proposition's numbers) if the sync
agrees.

### g7.2 `volcanoes` --- Volcanoes (~10 pp)

- **Hook**: 18 May 1980, 8:32 in the morning: the north side of Mount St.
  Helens slides away and the volcano explodes sideways; months earlier the
  mountain had been swelling.
- **Sections**: (1) Anatomy of a volcano: magma, magma chamber, vent,
  crater (cut-away). (2) Effusive and explosive eruptions, and why:
  runny or sticky magma, little or much gas (a bottle of fizzy water as an
  illustration of a correct term, not a name). (3) What comes out: lava
  flows, ash, bombs, pyroclastic flows, gases. (4) Where volcanoes are:
  along ridges, where a plate sinks under another (a gloss, not a term),
  above hotspots (Hawaii) --- the map coloured by setting, with counts.
- **Definitions**: magma; magma chamber; vent and crater; effusive
  eruption; explosive eruption; pyroclastic flow; hotspot.
- **Recall**: volcano, eruption, lava, ash
  (`\cref{ch:g4:volcanoes-earthquakes-first-look}`); plates and boundaries
  (`\cref{ch:g7:plate-tectonics}`); mantle (`\cref{ch:g6:inside-the-earth}`);
  igneous rocks (`\cref{ch:g6:rocks-and-minerals}`).
- **Figures**: S a volcano cut-away (magma chamber, vent, crater, lava flow,
  ash column); S effusive (shield, runny lava) vs explosive (steep cone,
  ash column) side by side; F `volcano_settings.py` -> map of the Holocene
  volcanoes coloured by tectonic setting (subduction, rift, intraplate) and
  a bar chart of the counts; S a hotspot under a moving plate (the island
  chain ages older away from the hotspot --- no "track" term, Book 2's);
  P x4: Kilauea lava (USGS HVO), Mount St. Helens 1980 (USGS, Austin Post),
  Pinatubo 1991 (USGS), Mauna Loa's broad shield (USGS), public domain,
  each to verify; AI x1: a volcanologist in a heat suit sampling lava
  (generic, no named volcano).
- **Ledger**: Mount St. Helens 1980 facts (date, height before/after, ash
  column height, devastated area: USGS); Kilauea lava temperatures (USGS
  HVO, about 1 100--1 200 degrees); Hawaiian island ages (USGS); counts
  computed from data:gvp.
- **Datasets**: shared `gvp-holocene` (setting column).
- **Exercises**: 12: label the cut, effusive or explosive, read the map
  counts (percentages), why Hawaii is far from any boundary.
- **Problem**: *The day the mountain lost its top* (Parts: before the
  eruption; 18 May 1980; after), 12 questions; named final number:
  **the height Mount St. Helens lost, in metres** (from the USGS
  before/after heights).

### g7.3 `earthquakes` --- Earthquakes (~10 pp)

- **Hook**: 26 December 2004: a magnitude 9 earthquake off Sumatra; hours
  later the sea rushes onto shores thousands of kilometres away.
- **Sections**: (1) Rocks break along faults; the two blocks slip
  suddenly. (2) Focus and epicentre. (3) Seismic waves (told) and the
  seismometer; the seismogram's trace. (4) Magnitude (one number per
  earthquake; each step about 32 times more energy) and intensity (what
  people felt and saw, place by place). (5) Earthquakes along plate
  boundaries (recall the pilot's map; how many per year by magnitude). (6)
  Tsunamis.
- **Definitions**: fault; focus and epicentre; seismometer; magnitude;
  intensity; tsunami.
- **Recall**: earthquake (`\cref{ch:g4:volcanoes-earthquakes-first-look}`);
  plate boundaries and the earthquake map (`\cref{ch:g7:plate-tectonics}`).
  P and S waves are physics' (later volume): told as "waves through the
  rock", not named.
- **Figures**: S a block diagram of a fault with focus, epicentre and waves
  spreading; S a seismometer's principle (a heavy mass that stays still
  while the frame shakes) and a drawn trace; F `quake_counts.py` -> number
  of earthquakes per year in magnitude classes 6, 7, 8, 9 (1976--2025,
  shared catalogue), roughly ten times fewer per step; S a tsunami born at
  a fault under the sea, slow and tall near the coast; F `epicentre.py`
  for the problem (three circles meeting at the epicentre on a grid map);
  P x2: a fence offset across the 1906 San Andreas rupture (USGS, G. K.
  Gilbert, public domain) or the 1959 Hebgen Lake scarp (USGS); tsunami
  damage, 2004 (USGS or U.S. Navy, public domain); AI x1: a quiet
  seismometer vault with instruments on a concrete pier (generic).
- **Ledger**: magnitude-energy factor (USGS); the 2004 and 2011 events
  (magnitude, date: USGS event pages); the largest recorded (Chile 1960,
  9.5: USGS); tsunami speed in the deep ocean (NOAA, about 800 km/h);
  intensity scale (USGS Modified Mercalli page); counts computed from
  data:usgs-comcat.
- **Exercises**: 12: focus vs epicentre, read the counts, magnitude vs
  intensity, tsunami arrival time.
- **Problem**: *Where did the ground shake?* (Parts: three stations;
  finding the epicentre; the wave reaches the coast), 12 questions; named
  final number: **the minutes left before the tsunami reaches the harbour
  town** (exercise data at the NOAA deep-ocean speed).

### g7.4 `sediments-and-fossils` --- Sediments and Fossils (~10 pp)

- **Hook**: in the walls of a canyon, layer after layer of rock, hundreds
  of metres of them; in one layer, the shell of a creature that lived in a
  sea.
- **Sections**: (1) Sediments settle in layers (in lakes and seas, fine on
  coarse, layer on layer). (2) From sediment to rock (squeezed and cemented:
  told). (3) How a fossil forms (quick burial, hard parts, replacement;
  moulds, casts, tracks) and why most living things leave none. (4) Layers
  and fossils as a record of past environments (coral -> warm shallow sea;
  ripple marks -> shallow water; coal -> swamp forest).
- **Definitions**: sediment; sedimentary layer (stratum); fossil (with
  mould, cast, trace fossil).
- **Recall**: weathering, erosion, deposition
  (`\cref{ch:g5:water-shapes-the-land}`); sedimentary rocks and the rock cycle
  (`\cref{ch:g6:rocks-and-minerals}`). Fossils as evidence of evolution are
  the biology books' (prose).
- **Figures**: S layers settling in a lake through the seasons; S the steps
  of fossilisation (four panels: death, burial, hardening, uncovering by
  erosion); F `varden_column.py` -> the stratigraphic column of the Varden
  Hills cover (sandstone, limestone, shale, chalk) with thicknesses and
  lithology ornaments, imported from `region.py`; S mould and cast; P x4:
  Grand Canyon layers (NPS, public domain); an ammonite and a trilobite
  (Commons CC or agency, to verify); dinosaur footprints (NPS, public
  domain); AI x1: an ancient shallow sea floor with shells settling into
  mud (generic reconstruction, no named species).
- **Ledger**: Grand Canyon thickness and age range (NPS/USGS); deep-sea
  sedimentation rates (a primary source, order of a few millimetres per
  thousand years) --- printed only if sourced.
- **Exercises**: 12: order the steps, which environment, read the column
  (thickness differences), which has a better chance to fossilise.
- **Problem**: *The column of the Varden Hills* (Parts: reading the
  layers; the fossils in them; how long it took), 12 questions; named final
  number: **the number of years to lay down the 180 m of limestone at the
  given rate** (exercise data; region thicknesses).

### g7.5 `geological-time` --- The Ages of the Earth (~10 pp)

- **Hook**: James Hutton at a rocky coast in 1788 looks at tilted layers
  under flat layers and feels "the abyss of time" (history, observation by
  a scientist).
- **Sections**: (1) Relative dating: the principles of superposition,
  cross-cutting relationships, inclusion and fossil succession; the
  unconformity. (2) Method: putting events in order in a cross-section (the
  Varden Hills section A--B: schist, granite, unconformity, cover, fault,
  erosion). (3) Eras and periods: the geological time scale (international
  chart's names and colours). (4) 4.6 billion years as one calendar year.
  (5) Absolute ages exist (the method is in the physics books; told).
- **Definitions**: relative dating and absolute age; principle of
  superposition; principle of cross-cutting relationships; principle of
  inclusion; principle of fossil succession; unconformity; era and period
  (geological); geological time scale.
- **Recall**: sedimentary layers and fossils (`\cref{ch:g7:sediments-and-fossils}`);
  faults (`\cref{ch:g7:earthquakes}`); granite as an igneous rock
  (`\cref{ch:g6:rocks-and-minerals}`).
- **Figures**: S three small sketches, one per principle; F the region's
  section A--B from the shared tables (`shared-region-section-*`), labelled
  for the ordering method; F `time_scale.py` -> eras and periods bar in the
  chart's colours (values in functions; the test re-reads the shared
  ledger); F `earth_calendar.py` -> the Earth's year with events placed on
  their dates; P x1: a portrait of James Hutton (Raeburn, public domain) or
  a Grand Canyon unconformity (NPS); AI none.
- **Ledger**: shared `ics:base.*` and `ics:colour.*`; the age of the Earth
  (about 4.54 billion years: USGS "Age of the Earth" / Dalrymple 2001);
  oldest fossil evidence (a primary source), the end of the dinosaurs
  (shared ics:base.Paleogene, 66.00 Ma), the first Homo sapiens (about
  300 000 years: Hublin et al. 2017); Hutton 1788 (primary history).
- **Exercises**: 12: apply each principle, order a section, era of an
  event, calendar dates (percentages and large numbers in millions).
- **Problem**: *The Earth's year* (Parts: scaling time; placing events;
  the last minutes), 12 questions; named final number: **the time on 31
  December when our species appears** (computed: about 23:25).

## Grade 8

### g8.1 `the-atmosphere` --- The Atmosphere (~10 pp)

- **Hook**: a weather balloon rises from a meteorological station at
  dawn, swelling as it climbs, until it bursts near 30 km.
- **Sections**: (1) A thin envelope (half the air below about 5.5 km;
  composition recalled from the chemistry books). (2) Pressure falls with
  altitude (halving every few kilometres; powers of ten for the very high
  air). (3) Temperature and the layers: troposphere, stratosphere,
  mesosphere, thermosphere; the tropopause higher at the equator than at
  the poles. (4) The ozone layer (told: it absorbs most of the Sun's
  ultraviolet; the chemistry is the chemistry books').
- **Definitions**: troposphere, stratosphere, mesosphere, thermosphere
  (one definition "The layers of the atmosphere", with tropopause); ozone
  layer.
- **Recall**: the atmosphere and air pressure, the barometer (physics,
  grade 5); the composition of air (chemistry, grade 4: shared rows
  air:N2, air:O2); clouds (`\cref{ch:g4:clouds-rain-snow}`).
- **Figures**: F `standard_atmosphere.py` -> temperature against altitude,
  0--100 km, with the four layers shaded (US Standard Atmosphere 1976);
  F same script (part `pressure`) -> pressure against altitude, 0--30 km,
  with the half and quarter levels; S the atmosphere to scale on the
  Earth's curve (a 100 km band on a 6 371 km radius); S a radiosonde's
  climb (balloon, parachute, instrument box); P x2: the Earth's limb from
  the ISS (NASA, public domain); a radiosonde launch (NOAA/NWS, public
  domain); AI x1: climbers with oxygen bottles on a high snowy ridge
  (generic, no named mountain).
- **Ledger**: US Standard Atmosphere 1976 layer bases and lapse rates
  (NOAA-S/T 76-1562; base values cited in the script); tropopause height
  range (NOAA JetStream); ozone layer altitude and UV absorption (NOAA/NASA
  ozone pages); the share of the atmosphere's mass below a height (computed
  from the standard).
- **Exercises**: 12: read the profile, layer of an aircraft / a balloon,
  pressure halving, temperature drop per kilometre (powers of ten allowed).
- **Problem**: *Following a weather balloon* (Parts: the climb; the
  temperature; the pressure), 12 questions; named final number: **the
  altitude where the pressure is a quarter of its sea-level value**.

### g8.2 `winds-global-circulation` --- Winds and the Global Circulation (~10 pp)

- **Hook**: sailing ships of the 1500s found a belt of steady winds that
  carried them west across the Atlantic every time: the trade winds.
- **Sections**: (1) Uneven heating with latitude (the same beam of sunlight
  spread over a larger area near the poles; the seasons recalled). (2)
  Rising and sinking air: low and high pressure at the ground; a
  convection cell; the sea breeze and the land breeze. (3) The global
  winds: trade winds, westerlies, polar easterlies, and the belts of high
  and low pressure. (4) The Earth's rotation deflects winds (told: to the
  right in the northern hemisphere, to the left in the southern). (5) The
  global circulation explains the climate zones (rising air and rain near
  the equator, sinking dry air and deserts near 30 degrees).
- **Definitions**: convection cell (atmospheric, descriptive: the outline
  map gives "convection cells (descriptive)" to this chapter; Book 2 g12
  `internal-heat` owns mantle convection and should recall this one --- report
  item 2); sea breeze and land breeze; trade
  winds and westerlies (one definition "The global winds"); global
  circulation of the atmosphere.
- **Recall**: wind (physics, grade 2); air pressure (physics, grade 5);
  climate zones, deserts, rainforests (`\cref{ch:g5:weather-and-climate}`);
  the troposphere (`\cref{ch:g8:the-atmosphere}`).
- **Figures**: S a beam of sunlight at the equator and near a pole; S sea
  breeze by day and land breeze by night; S the three-cell globe with
  surface winds (north-east trades north of the equator, south-east trades
  south of it, westerlies, polar easterlies) and the pressure belts; F
  `trade_route.py` for the problem (great-circle and rhumb distances of a
  sailing route, tested); F `rain_by_latitude.py` (**optional**, if a
  public-domain zonal precipitation climatology reads with the tools at
  hand: GPCP at NOAA PSL) -> annual rainfall against latitude, peaks at the
  equator and near 50 degrees, minima near 25--30; P x1: a full-disk
  satellite image with the equatorial cloud band (NOAA GOES, public
  domain); AI x2: a sailing ship running before the trade wind (generic,
  no named ship); kites on a beach in the afternoon sea breeze.
- **Ledger**: latitudes of the cells' boundaries (about 30 and 60 degrees:
  NOAA JetStream); the trade winds' history (a primary history source);
  Earth's rotation (shared).
- **Exercises**: 12: draw the breeze, name the wind belt, why deserts near
  30 degrees, deflection direction by hemisphere.
- **Problem**: *Sailing with the trade winds* (Parts: the route; the wind;
  the crossing), 12 questions; named final number: **the number of days of
  the crossing** at the given speed.

### g8.3 `fronts-and-weather-maps` --- Air Masses, Fronts and Weather Maps (~10 pp)

- **Hook**: a sunny morning; by noon a veil of high cloud; by evening rain;
  the next day clear, cold and gusty: a depression has passed.
- **Sections**: (1) Air masses (cold or warm, moist or dry, by where they
  formed). (2) Fronts: the warm front (gentle slope, layered cloud, long
  rain) and the cold front (steep, towering clouds, showers). (3)
  Depressions and anticyclones: the winds turn around them (anticlockwise
  around a depression in the northern hemisphere, told) and the weather
  each brings. (4) Isobars and reading a weather map (close isobars, strong
  wind). (5) How a forecast is made (observations, computer models; a
  forecast of a few days is good, beyond about ten days it fades).
- **Definitions**: air mass; front (warm front, cold front); depression;
  anticyclone; isobar; weather forecast.
- **Recall**: air pressure and the barometer (physics, grade 5); clouds and
  precipitation (`\cref{ch:g4:clouds-rain-snow}`); global winds
  (`\cref{ch:g8:winds-global-circulation}`).
- **Figures**: F `weather_map.py` -> a computed northern-hemisphere weather
  map (an analytic pressure field: a depression and an anticyclone,
  isobars every 4 hPa traced and labelled, warm and cold fronts oriented so
  the symbols point where each front moves, wind arrows turning the right
  way); F same script (part `sequence`) -> the cold front's positions hour
  by hour for the problem; S a cold-front cross-section; S a warm-front
  cross-section; S air-mass source regions (schematic arrows on the shared
  land table); P x1: a satellite image of a mid-latitude depression
  (NASA/NOAA, public domain); AI x1: rain arriving over a town under a dark
  cloud base (generic).
- **Ledger**: isobar spacing convention (4 hPa, a national weather service
  page); standard sea-level pressure (1013.25 hPa, the US Standard
  Atmosphere); forecast skill gain (Bauer, Thorpe and Brunet 2015, Nature,
  "about a day per decade") --- printed only if fetched.
- **Exercises**: 12: label the map, which front, wind strength from
  isobar spacing, what weather next.
- **Problem**: *Will the match be rained off?* (Parts: reading the map;
  the front's speed; the forecast), 12 questions; named final number:
  **the hour at which the cold front reaches the town**.

### g8.4 `the-oceans` --- The Oceans (~10 pp)

- **Hook**: 1872--1876, a ship lowers a weighted rope again and again to
  measure the depth of the sea; today a ship maps the sea floor with sound.
- **Sections**: (1) Ocean basins and the seafloor: shelf, slope, abyssal
  plain, ridge, trench (a real profile). (2) Salinity (about 35 grams per
  kilogram; saltier where evaporation wins, fresher near rivers and ice).
  (3) Surface currents driven by the winds: gyres, the Gulf Stream. (4)
  Deep currents of cold, salty water (told: centuries to go round). (5)
  The ocean carries heat from the tropics towards the poles.
- **Definitions**: continental shelf, continental slope, abyssal plain,
  ocean ridge, ocean trench (one definition "The parts of the seafloor");
  salinity; ocean current; gyre.
- **Recall**: oceans and seas, salt water (`\cref{ch:g2:water-on-earth}`); plate
  boundaries, ridge and trench as places (`\cref{ch:g7:plate-tectonics}`);
  global winds (`\cref{ch:g8:winds-global-circulation}`).
- **Figures**: F `seafloor_profile.py` -> two real profiles from ETOPO1 at
  1 degree: across the South Atlantic (shelf, abyssal plain, Mid-Atlantic
  Ridge) and across the Peru--Chile trench, vertical exaggeration stated;
  S an idealised seafloor profile with every part labelled; S the main
  surface currents on the world map (warm red, cold blue arrows; gyres
  clockwise north of the equator, anticlockwise south of it) over the
  shared land table; S salinity: evaporation and rain over a sea; P x2:
  the Gulf Stream's warm water from space (NASA MODIS, public domain); a
  historic sounding (NOAA Photo Library, Challenger expedition, public
  domain) to verify; AI x1: a research ship with an echo sounder's fan of
  sound beams drawn as soft light (no text).
- **Ledger**: mean ocean depth (NOAA, about 3 700 m); salinity 35 g/kg and
  ranges (NOAA / NASA); the Challenger expedition dates (NOAA); Gulf
  Stream speed (NOAA); deep circulation time (NOAA, about 1 000 years).
- **Datasets**: shared `etopo-1deg`.
- **Exercises**: 12: label a profile, salinity calculations (percent),
  current direction from wind, warm or cold current.
- **Problem**: *A drifting buoy* (Parts: the launch; around the gyre; the
  journey's length), 12 questions; named final number: **the number of
  months for the buoy to go once round the gyre** (exercise data).

### g8.5 `ice-on-earth` --- Ice on Earth (~10 pp)

- **Hook**: two photographs of the same Alaskan valley, 1941 and 2004:
  the glacier that filled it has gone (USGS repeat photography).
- **Sections**: (1) Glaciers: snow becomes ice; where snow builds up and
  where ice melts. (2) How a glacier flows and erodes: U-shaped valleys,
  moraines, erratic blocks. (3) Ice sheets, ice shelves and icebergs
  (Antarctica, Greenland, their sea-level equivalent). (4) Sea ice (the
  Arctic's September minimum, 1979--2025). (5) Permafrost. (6) The ice ages
  (told: about 20 000 years ago ice sheets covered much of North America and
  northern Europe; sea level was much lower).
- **Definitions**: glacier; ice sheet (ice shelf, iceberg); sea ice;
  permafrost; U-shaped valley and moraine (one definition); ice age
  (map: "ice age" is g8's). "Glacial period", "interglacial" and "glacial
  cycle" are Book 2 g12 `past-climates`'s (its DEFINITIONS claims them): here
  "the ice ages and the warmer times between them", in prose.
- **Recall**: snow (`\cref{ch:g4:clouds-rain-snow}`); erosion and valleys
  (`\cref{ch:g5:water-shapes-the-land}`); the oceans
  (`\cref{ch:g8:the-oceans}`); water freezing and expanding (physics).
- **Figures**: S a valley glacier in long section (snow zone, melting zone,
  flow arrows, moraines); S V-shaped and U-shaped valleys; F `sea_ice.py`
  -> Arctic September sea-ice extent, 1979--2025, with its straight-line
  trend (NSIDC Sea Ice Index); S the ice sheets' sea-level equivalent as
  bars (ledger values); P x3: Muir Glacier 1941 and 2004 (USGS /
  NSIDC Glacier Photograph Collection, public domain); an Antarctic ice
  shelf edge (NASA, public domain); AI x1: tundra with patterned ground
  and a leaning house on thawing permafrost (generic).
- **Ledger**: Antarctic and Greenland sea-level equivalents (IPCC AR6 WG1
  ch. 9 or NSIDC Quick Facts); land area covered by ice (NSIDC/USGS, about
  a tenth); permafrost area (a primary source); Last Glacial Maximum
  timing and sea-level fall (about 120 m: a primary source); Muir Glacier
  facts (USGS repeat photography page); glacier flow speeds (USGS).
- **Datasets**: **new** `grade-8-nsidc-sea-ice` (NSIDC G02135 Sea Ice Index
  v4, Arctic September monthly extent, free with citation; 2 KB).
- **Exercises**: 12: label the glacier, V or U, read the sea-ice graph
  (decrease per decade), sea-level from a fraction of an ice sheet.
- **Problem**: *A glacier's long retreat* (Parts: the glacier front's
  positions; the speed of retreat; the valley it leaves), 12 questions;
  named final number: **the year the glacier front would reach the lake**
  at the measured rate (exercise data, with a caution that a rate is not a
  forecast).

## Grade 9

### g9.1 `climate-past-and-present` --- The Earth's Climate, Past and Present (~10 pp)

- **Hook**: without its atmosphere's greenhouse effect the Earth's surface
  would average about minus 19 degrees; it averages about 15.
- **Sections**: (1) The greenhouse effect and the Earth's temperature
  (recalled from the chemistry books, with the two temperatures from the
  shared NASA rows). (2) Past climates: the ice ages and the warm periods
  between them (Antarctic ice: temperature and carbon dioxide over 800 000
  years, simplified), and much warmer times long ago (told). (3) Today's
  records: temperature (decade by decade since 1880), carbon dioxide
  (Mauna Loa since 1959), sea level (satellites since 1993), ice (recall
  sea ice). (4) The causes as the scientific assessments state them, with
  their calibrated words (*unequivocal*, *very likely*, *likely*) ---
  physical science only.
- **Definitions**: climate change; global warming; temperature anomaly.
- **Recall**: climate (`\cref{ch:g5:weather-and-climate}`); ice ages and sea
  ice (`\cref{ch:g8:ice-on-earth}`); greenhouse gases and the greenhouse
  effect (chemistry, grade 8, prose); the atmosphere's layers
  (`\cref{ch:g8:the-atmosphere}`).
- **Figures**: F `climate_records.py` -> (a) decade mean temperature
  anomaly bars, 1880s--2010s and 2020--2025 (GISTEMP); (b) Mauna Loa annual
  CO2 1959--2025; (c) ice-core CO2 and temperature, 800 000 years (shared
  datasets, subsampled for TeX); (d) satellite sea level 1993--2025 with
  its rate; S the greenhouse effect, simply (sunlight in, infrared out, part
  sent back down); P x1: an ice-core section held up to the light
  (NOAA/NSF, public domain, to verify); AI x1: none or a weather-station
  thermometer screen in a field (generic). A `dated{2025}` box for the
  latest CO2 and the warmest year.
- **Ledger**: shared `earth:Tbb`, `earth:Tsurf`, data rows; IPCC AR6 WG1
  SPM statements (A.1 unequivocal; A.1.2 the 2011--2020 warming; A.1.7 sea
  level; A.2.1 CO2 highest in 2 million years) --- **cite Book 2's
  `ipcc:*` rows read-only where they exist, mint `ipcc:b1-*` rows only for
  statements Book 2 does not carry**.
- **Datasets**: shared `gistemp`, `co2-mlo-annual`, `co2-icecore`,
  `edc-temperature`, `gmsl-altimetry`.
- **Exercises**: 12: read the records, compute differences and rates
  (scientific notation for the 800 000 years), weather vs climate change,
  what the assessments say (calibrated words).
- **Problem**: *The planet's thermometer* (Parts: the decades; the carbon
  dioxide; the sea), 12 questions; named final number: **the warming of
  the decade 2015--2024 compared with 1880--1899, in degrees** (computed
  from GISTEMP; the AR6 1850--1900 baseline value quoted beside it).

### g9.2 `natural-risks` --- Living with Natural Risks (~10 pp)

- **Hook**: June 1991: scientists watching Mount Pinatubo raise the alert;
  tens of thousands leave; days later the largest eruption in decades
  buries the land around --- and most of the people are safe.
- **Sections**: (1) Risk depends on the hazard and on vulnerability
  (qualitative grid). (2) Forecasting versus prevention. (3) Monitoring
  volcanoes (seismometers, swelling of the ground, gases) and faults (GPS
  stations, recall). (4) Flood zones (the Varden Hills map). (5)
  Earthquake-safe building (principles: bracing, light roofs, flexible
  frames, isolation from the ground). (6) Warning systems (tsunami
  buoys).
- **Definitions**: risk; vulnerability; prevention; hazard map.
- **Recall**: natural hazard and disaster (`\cref{ch:g5:natural-hazards}`);
  volcanoes and eruptions (`\cref{ch:g7:volcanoes}`); earthquakes, tsunamis
  (`\cref{ch:g7:earthquakes}`); floods (`\cref{ch:g5:water-shapes-the-land}`);
  forecasts (`\cref{ch:g8:fronts-and-weather-maps}`).
- **Figures**: S the risk grid (hazard low/high x vulnerability
  low/high); F `flood_zone.py` -> the Varden Hills flood-zone map for a
  water level a few metres above the river floor, with houses as points,
  importing `region.py`; S earthquake-resistant building principles
  (bracing, base isolation); S volcano monitoring instruments around a
  cone; P x2: Pinatubo 1991 (USGS, public domain); a tsunami buoy (NOAA
  DART, public domain); AI x1: a family checking an emergency kit by a door
  (generic).
- **Ledger**: Pinatubo forecasts and lives saved (USGS Fact Sheet 115-97);
  Armero 1985 (USGS); DART buoys (NOAA); base isolation principle (USGS or
  FEMA page).
- **Exercises**: 12: hazard or vulnerability, read the flood map, which
  building is safer and why, forecasting vs prevention.
- **Problem**: *Where should the new school go?* (Parts: the flood map;
  the slopes and the fault; choosing), 12 questions; named final number:
  **the number of houses inside the flood zone** (computed).

### g9.3 `earth-resources` --- Resources from the Earth (~10 pp)

- **Hook**: a smartphone holds dozens of elements, every one dug from the
  ground; a house needs tens of tonnes of sand and gravel.
- **Sections**: (1) Resources recalled from the chemistry books; why a
  metal must be concentrated before it is worth mining (concentration
  factor). (2) How ore deposits form: from magma, from hot water in veins,
  in river gravels (placers). (3) Coal, oil and gas from buried organic
  matter (swamp forests -> peat -> coal; plankton -> oil and gas, which
  rise until stopped under an impermeable rock: told, the vocabulary is
  Book 2's). (4) Groundwater as a resource (recall). (5) Sand and
  aggregates: the most-extracted solid material. (6) Renewable and finite
  on human and geological time (scientific notation: millions of years to
  form, decades to use).
- **Definitions**: ore deposit (with concentration factor); aggregate;
  reserve.
- **Recall**: resource, renewable resource, ore, raw material (chemistry,
  grade 5); fossil fuels (chemistry, grade 8); element abundance (chemistry,
  grade 9); aquifer and groundwater (`\cref{ch:g6:water-underground}`);
  permeable rocks (same); sedimentary layers and geological time
  (`\cref{ch:g7:sediments-and-fossils}`, `\cref{ch:g7:geological-time}`).
- **Figures**: S a hydrothermal vein forming in a crack above a granite; S
  coal formation, swamp to coal seam (four stages); S oil and gas stopped
  under an impermeable fold (told); F `concentration.py` -> concentration
  factors (ore grade over crustal abundance) for iron, aluminium, copper,
  gold, as a bar chart on a scale of powers of ten; S formation vs use
  time arrow; P x2: a coal seam (USGS, public domain); an open-pit mine
  from space (NASA ISS photograph, public domain); AI x1: a building site
  with heaps of sand and gravel (generic).
- **Ledger**: crustal abundances (Rudnick and Gao 2003 or USGS); typical
  ore grades (USGS Mineral Commodity Summaries / fact sheets); aggregates
  extracted per year (UNEP 2019 "Sand and sustainability"; a `dated` box if
  volatile); coal formation times (USGS).
- **Exercises**: 12: concentration factor, ore type, coal stages, years a
  reserve lasts (scientific notation).
- **Problem**: *Concrete for a new town* (Parts: how much sand; the
  reserve; renewable or not), 12 questions; named final number: **the
  number of years the local sand reserve would last** (exercise data).

### g9.4 `landforms` --- Landforms (~10 pp)

- **Hook**: the white chalk cliffs of a coast lose a few metres in a single
  winter storm; the same chalk once lay on the floor of a warm sea.
- **Sections**: (1) Relief as a balance between uplift and erosion
  (millimetres a year up, millimetres a year away). (2) Landforms made by
  the wind: dunes. (3) Landforms made by the sea: cliffs, beaches, spits
  (longshore drift). (4) Landforms made by dissolution: karst, caves,
  sinkholes (limestone dissolves slowly in slightly acidic water ---
  acids recalled from the chemistry books). (5) Reading a landscape
  (method: shape -> process -> rock).
- **Definitions**: uplift; dune; cliff; beach and spit (with longshore
  drift); karst (cave, sinkhole).
- **Recall**: landforms (`\cref{ch:g1:landscapes-around-us}`); weathering,
  erosion, deposition (`\cref{ch:g5:water-shapes-the-land}`); relief
  (`\cref{ch:g4:world-physical-map}`); plates and mountains
  (`\cref{ch:g7:plate-tectonics}`); glaciers and U-shaped valleys
  (`\cref{ch:g8:ice-on-earth}`); limestone (`\cref{ch:g6:rocks-and-minerals}`).
- **Figures**: S uplift vs erosion as a balance; S a crescent dune in plan
  and profile (horns pointing downwind; gentle windward, steep lee slope);
  S cliff retreat (notch, collapse, wave-cut platform) and a spit grown by
  longshore drift (plan); S a karst block diagram (sinkhole, cave,
  stalactites, resurgence) with the `blockdiagram` pic; P x3: crescent
  dunes (NASA or NPS, public domain); a chalk cliff coast (Commons CC, to
  verify); a cave with stalactites (NPS Carlsbad Caverns, public domain);
  AI x1: a sandy spit seen from a low aircraft (generic).
- **Ledger**: uplift rates (e.g. Himalaya, a primary source); cliff retreat
  rates on a soft coast (British Geological Survey or a primary paper);
  dune migration speeds (USGS); dissolution facts.
- **Exercises**: 12: which agent made it, dune wind direction, cliff
  retreat rate, karst features.
- **Problem**: *The cliff and the coast road* (Parts: measurements of the
  cliff edge; the rate; the future road), 12 questions; named final
  number: **the year the cliff edge would reach the road** at the measured
  rate (exercise data; observation from a safe distance only, by the
  survey team in the story).

### g9.5 `maps-of-the-earth` --- Maps of the Whole Earth (~10 pp)

- **Hook**: on a classroom wall map Greenland looks as big as Africa; on
  the globe it is a fraction of it. Who is lying?
- **Sections**: (1) Why a flat map must distort; the Mercator projection
  (angles kept, areas stretched) and an equal-area projection (areas kept,
  shapes bent). (2) Scale: the numerical scale 1 : 25 000 (and the scale
  bar), from the grade-2 idea. (3) The topographic map: contour lines,
  contour interval, slope from spacing; drawing a topographic profile
  (method) on the Varden Hills map. (4) Satellite images of the Earth
  (remote sensing since 1972). (5) Satellite positioning: distances to
  several satellites fix a position (2-D principle computed).
- **Definitions**: map projection (Mercator projection, equal-area
  projection); numerical scale **[SYNC: if "scale" stays in g9, this is
  "scale" itself]**; topographic map; contour line (contour interval);
  remote sensing (satellite image); satellite positioning.
- **Recall**: plan, map, legend, scale (`\cref{ch:g2:drawing-to-map}`); the
  globe and the world map (`\cref{ch:g3:continents-and-oceans}`); latitude
  and longitude (`\cref{ch:g6:latitude-longitude}`); altitude and the
  physical map (`\cref{ch:g4:world-physical-map}`).
- **Figures**: F `projections.py` -> the world in Mercator and in an
  equal-area projection side by side, with equal circles on the globe
  drawn on both (Tissot's idea); F `varden_topo.py` -> the Varden Hills
  topographic map (shared contours, index contours, river, scale bar, north
  arrow, profile line C--D) and the profile along C--D computed from
  `region.topo`; S contour lines from a hill sliced at equal heights; F
  `trilateration.py` -> three circles meeting at the receiver; P x2: a
  Landsat image of a river delta or city (USGS/NASA, public domain); a GPS
  satellite (GPS.gov, public domain); AI x1: a surveyor with a satellite
  receiver on a tripod in a field (generic).
- **Ledger**: areas of Greenland and Africa (a primary source, or computed
  from Natural Earth rings if they separate cleanly); Landsat 1 launch
  (USGS); the GPS constellation (GPS.gov: at least 24 satellites).
- **Exercises**: 12: Mercator stretch at 60 degrees (factor 4 in area),
  map distance with scale, contour reading, slope, profile.
- **Problem**: *A footpath across the Varden Hills* (Parts: the route on
  the map; the climb; the walk), 12 questions; named final number: **the
  length of the footpath in kilometres and the total climb in metres**
  (computed from the region; the path is drawn by planners, the reader
  works on the map only).
