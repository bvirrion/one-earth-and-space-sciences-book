# Book 2 (Grades 10--12) --- chapter briefs (Phase A, 2026-10-22)

Binding run file: `sources/BATCH_BOOKS_1-5.md`. Chapter list and slugs:
`OUTLINE.md` (frozen). Term table: `DEFINITIONS.md` (this directory). The
g12 `climate-change` pilot is written and approved; it is the reference for
register, density, boxes, data use and calibration.

Conventions for every chapter below (not repeated per chapter):

- Opens with a provenance comment (never printed), then `\chapter`, a
  concrete hook scene, a `recall` box when it builds on an earlier notion,
  3--5 sections, `\section{Exercises}` with exactly 15 exercises (5 ★, 6 ★★,
  4 ★★★, in that order), `\section{Problem: ...}` with one weekend problem of
  18--22 questions in Parts I--IV ending on a named number; solutions file
  in the same order. Target ~11.5 pp per chapter including solutions.
- Tags for figures: **S** = schematic (TikZ), **F** = figdata (computed
  table read by pgfplots, tested), **AI** = generic illustration (JPEG),
  **P** = photograph (public domain or verified CC; "candidate" = to verify
  through the Commons API or the agency page before use).
- Every real-world number gets a ledger row in `sources/ledger/book2.md`
  (ids unique across ledgers; reuse shared and other books' rows read-only).
  "Ledger" lists name the rows to mint; "(shared)" = already in
  `sources/data_ledger.md`.
- Math level: grade 10 sine/cosine/tangent of an angle, powers, linear
  equations; grade 11 adds derivatives (not used for rates); grade 12 adds a
  rate written as a derivative, `exp` and `ln`.
- Observation only; climate physical science only; no curriculum named.

---

## Grade 10

### g10.01 `measuring-the-earth` --- Measuring the Earth

**Hook.** A ship sails out of a harbour; its hull disappears first, then the
sails, the top of the mast last. Twenty-two centuries ago a librarian in
Alexandria turned a shadow into the size of the planet.

**Sections.**
1. *A round Earth* --- the evidence: ships over the horizon, the round shadow
   of the Earth on the Moon in a lunar eclipse (eclipses recalled from the
   physics books), stars that rise higher as one travels north,
   circumnavigation, photographs from space.
2. *Eratosthenes* --- parallel sunlight, the angle at the centre equals the
   shadow angle (alternate angles), circumference = (360°/α) × d. Method
   box. The uncertain length of the stadion, honest about it.
3. *Triangulation* --- a baseline, angles, a chain of triangles. The sine
   rule is **derived** from right-triangle trigonometry (height of a
   triangle written two ways), a proposition with proof. The meridian of
   Delambre and Méchain (Dunkirk--Barcelona, 1792--1798) and the metre.
4. *A flattened Earth* --- Newton (rotation flattens) against the Cassinis;
   the Lapland (1736--37) and Peru (1735--44) expeditions; a degree of
   latitude is longer near the poles (computed curve); the reference
   ellipsoid; equatorial bulge of 21 km.
5. *Geodesy today* --- satellite positioning (recalled from Book 1, grade 9),
   millimetre precision, the reference frames; the geoid told in one
   sentence (no definition: Year 1 owns it).

**Definitions.** geodesy (`def:g10:measuring-the-earth:geodesy`);
triangulation (`...:triangulation`); reference ellipsoid, flattening
(`...:ellipsoid`).
**Statements.** prop. Eratosthenes' relation (derived); prop. the sine rule
(derived); prop. the Earth's dimensions (WGS84 a, b, f; ledger); method:
measuring a circumference from two shadows; method: a triangulation chain;
example: Eratosthenes' numbers; example: the Delambre--Méchain arc;
history box: the two expeditions; inthefield: a geodetic survey today.
**Recall.** latitude, longitude, meridians and parallels (Book 1, grade 6);
map projections and satellite positioning (Book 1, grade 9); the Sun's light
travels in straight lines, eclipses (the physics books).

**Figures.** S ship over the curved horizon; S Eratosthenes' geometry
(Syene, Alexandria, parallel rays, angle α at the centre); S a triangulation
chain with baseline and measured angles; F `meridian_degree` (length of 1° of
latitude against latitude on the reference ellipsoid, with the historic
measurements as points); S circle versus ellipse (exaggerated), a and b;
P the Earth from space (candidate: NASA "The Earth seen from Apollo 17", PD);
P a historic geodetic instrument or a Struve Geodetic Arc marker (candidate,
Commons, verify licence); AI a surveyor with a theodolite on a hilltop.

**Ledger.** WGS84 defining parameters (NGA TR8350.2); earth:Req, earth:Rpol,
earth:flattening (shared); Eratosthenes' angle (1/50 of a circle) and 5000
stadia, and the stadion uncertainty (a history-of-science source); the
Delambre--Méchain arc and the 1791/1799 definitions of the metre (BIPM
history pages); the Lapland and Peru degree lengths (historical source with
DOI); GNSS precision (agency page).
**Datasets.** none (ellipsoid formula).

**Weekend problem --- "The metre and the meridian".** I Eratosthenes redone
with the modern Aswan--Alexandria distance and latitudes; II a small
triangulation chain (sine rule) to a measured arc; III degree lengths at the
equator and at 66° N from the ellipsoid, and the flattening they imply;
IV the quarter meridian computed from the ellipsoid, and the metre of 1799.
**Named final number:** *the 1799 metre is about 0.2 mm shorter than one ten
-millionth of the quarter meridian.*

---

### g10.02 `habitable-planet` --- A Habitable Planet

**Hook.** Three rocky planets side by side: Venus, hot enough to melt lead
under a crushing atmosphere; Mars, cold and nearly airless; the Earth, with
oceans. Same family, three fates.

**Sections.**
1. *The temperature set by the star* --- sunlight spreads over a sphere
   (inverse square); the equilibrium temperature with the albedo (formula
   admitted, "derived in the physics books, Year 2"); computed values for
   Mercury--Mars against the measured means: the gap is the greenhouse effect
   (recalled from the chemistry books).
2. *Holding an atmosphere* --- mass and gravity; escape speed (recalled from
   the physics books, values from the fact sheet); the Moon and Mercury
   bare, Mars thin, Venus thick.
3. *Liquid water* --- the phase diagram of water (computed curves through the
   triple point); Earth's surface inside the liquid field, Mars near the
   triple point, Venus above the critical point.
4. *The habitable zone* --- definition; the Sun's zone from the published
   limits; the Earth inside, Mars at the outer edge, Venus inside the inner
   edge.
5. *Planets of other stars* --- exoplanet; how they are found (transits and
   the star's wobble, told: Year 3 owns the methods); the numbers known
   (`dated` box); Proxima b and the TRAPPIST-1 planets.

**Definitions.** equilibrium temperature (`def:g10:habitable-planet:
equilibrium-temperature`); habitable zone (`...:habitable-zone`); exoplanet
(`...:exoplanet`).
**Statements.** prop. inverse-square law of sunlight (admitted, physics);
prop. equilibrium temperature formula T = 278.6 K × (1−A)^{1/4}/√d (admitted;
tested against the fact sheet's 254 K for the Earth); example: Venus, Earth,
Mars; dated box: confirmed exoplanets.
**Recall.** rocky and giant planets, conditions for life (Book 1, grade 6);
the Solar System, light from the Sun (physics); greenhouse gases (chemistry);
states of water (physics); pressure (physics, grade 10).

**Figures.** F `planet_temperatures` (equilibrium versus measured mean
temperature, Mercury to Mars); F water phase diagram with the surface
conditions of Venus, Earth and Mars (same script); F habitable zone of the
Sun with the planets, plus a scaled panel for Proxima Centauri; S sunlight
spreading over spheres (inverse square); P Venus (candidate: NASA Mariner 10
or Magellan, PD); P Mars surface (candidate: NASA Curiosity, PD); P Earthrise
(candidate: NASA Apollo 8, PD).

**Ledger.** Bond albedos of Mercury, Venus, Earth, Mars (NASA per-planet fact
sheets); planet distances, mean temperatures, surface pressures, escape
speeds (shared); water triple point and critical point (IAPWS); habitable
zone limits (Kopparapu et al. 2013, ApJ, DOI); confirmed exoplanet count
(NASA Exoplanet Archive, `dated`); Proxima b semi-major axis, Proxima
luminosity (NASA Exoplanet Archive; discovery paper DOI); TRAPPIST-1 (same).
**Datasets.** none.

**Weekend problem --- "Could Proxima b hold an ocean?".** I the star's light
at the planet (L/d² relative to the Earth); II the equilibrium temperature
for an Earth-like albedo; III is the planet in its star's habitable zone
(limits scaled by √L)?; IV an atmosphere and water: what else must hold?
**Named final number:** *the equilibrium temperature of Proxima b, about
230 K.*

---

### g10.03 `earth-energy-budget` --- The Earth's Energy Budget

**Hook.** At the North Pole in June the Sun never sets and the ground
receives more sunlight in a day than the equator --- yet it stays frozen.

**Sections.**
1. *Sunlight received* --- 1361 W/m² at the top of the atmosphere; a disc
   intercepts, a sphere spreads: S/4 = 340 W/m²; insolation by latitude and
   season (computed; seasons recalled from the physics books).
2. *Albedo* --- definition; albedos of snow, cloud, desert, forest, ocean;
   the planet's albedo 0.29--0.30: absorbed ≈ 240 W/m².
3. *The global energy budget* --- the AR6 picture: reflected, absorbed by
   the air and the surface, surface emission, back radiation, latent and
   sensible heat, outgoing infrared, the small imbalance; definitions of the
   energy budget and of latent and sensible heat; the greenhouse effect
   recalled (its quantitative model belongs to the physics books).
4. *Surplus and deficit* --- the tropics absorb more than they emit, the
   poles less: poleward heat transport by the atmosphere and the ocean; this
   drives winds, currents and the water cycle (recalled from Book 1, grade 8).
5. *Where the energy goes* --- less than 1 % into photosynthesis (computed).

**Definitions.** insolation (`def:g10:earth-energy-budget:insolation`);
albedo (`...:albedo`); energy budget (`...:energy-budget`); latent heat,
sensible heat (`...:latent-heat`); poleward heat transport
(`...:heat-transport`).
**Statements.** prop. the mean insolation is S/4 (derived: disc versus
sphere); prop. the global budget balances to within the imbalance (AR6
numbers, checked in the script); method: reading an energy-budget diagram;
example: absorbed sunlight; example: the photosynthesis share.
**Recall.** seasons and their cause, the Sun's height (physics); global
winds, convection cells (Book 1, grade 8); greenhouse gases (chemistry);
photosynthesis (biology).

**Figures.** S disc versus sphere (S/4); F `insolation` (daily-mean
insolation against day of the year at 0°, 30°, 60°, 90° N; tested: S0/π at
the equator at an equinox, the polar maximum at the June solstice above the
equator's); S the energy-budget diagram with the AR6 values; bar chart of
albedos (ledger coordinates typed, as the pilot's forcing bars); S surplus
and deficit by latitude with heat-transport arrows (qualitative unless a
zonal radiation table is sourced, see the Phase A report); P the Earth from
space with clouds and ice (candidate: NASA DSCOVR EPIC, PD); AI a sunlit
snowfield beside a dark ploughed field.

**Ledger.** earth:TSI, earth:albedo (shared); AR6 WG1 Figure 7.2 values
(IPCC-AR6-CH7, a row per flux); albedos of surfaces (a fetched primary
source); peak poleward heat transport (Trenberth and Caron 2001, J. Climate,
DOI); global gross primary production (AR6 WG1 ch. 5 or a DOI paper); energy
stored per gram of carbon fixed (chemistry handbook value via NIST).
**Datasets.** none.

**Weekend problem --- "Following a sunbeam".** I the geometry (S/4); II
albedo and absorbed sunlight; III closing the surface budget and the
imbalance; IV photosynthesis.
**Named final number:** *the share of absorbed sunlight stored by
photosynthesis, about 0.1 %.*

---

### g10.04 `why-clouds-form` --- Why Clouds Form

**Hook.** A glass of iced water ``sweats'' on a summer terrace; the same
physics builds the cumulus over the plain in the afternoon.

**Sections.**
1. *Water vapour and saturation* --- saturation content rises steeply with
   temperature (computed); relative humidity; dew point; method: relative
   humidity and dew point from a table.
2. *Rising air cools* --- expansion cools without heat exchange: adiabatic
   cooling, the dry rate about 9.8 °C/km (admitted, value from the source);
   the dew point of a rising parcel falls about 1.8 °C/km; the condensation
   level 125 m per degree of dew-point spread (**derived** from the two
   rates: a linear equation).
3. *Stable and unstable air* --- the parcel compared with its surroundings
   (the environmental lapse recalled from Book 1, grade 8); the saturated
   rate about 5--6 °C/km (told: the moist adiabat is Year 2's); conditional
   instability told; stratus and cumulus.
4. *Four ways to lift air* --- surface heating, mountains, fronts (recalled
   from Book 1, grade 8), convergence; the warm dry wind in the lee of a
   mountain (computed example).
5. *From droplets to rain and snow* --- condensation nuclei, droplet and
   raindrop sizes (a million droplets per raindrop, computed); the warm-rain
   and ice-crystal processes.

**Definitions.** saturation, relative humidity
(`def:g10:why-clouds-form:humidity`); dew point (`...:dew-point`); adiabatic
cooling, dry adiabatic rate (`...:adiabatic`); condensation level
(`...:condensation-level`); stable air, unstable air (`...:stability`);
condensation nucleus (`...:nucleus`); warm-rain process, ice-crystal process
(`...:rain-processes`).
**Statements.** prop. the condensation level (derived); method: is this air
stable?; method: following a parcel over a mountain; examples throughout.
**Recall.** cloud families, precipitation, rain gauge (Book 1, grade 4);
atmospheric layers and the fall of temperature with height (Book 1,
grade 8); fronts (Book 1, grade 8); evaporation and condensation (physics);
latent heat (\cref{ch:g10:earth-energy-budget}).

**Figures.** F `saturation` (saturation content against temperature, with a
parcel marked); F `parcel` (height against temperature: dry adiabat,
dew-point line, condensation level, saturated branch, two environmental
profiles, stable and unstable; tested: 125 m per °C); S mountain section with
the parcel's temperatures on both sides (numbers from the `parcel` script);
S droplet, nucleus and raindrop sizes; P cumulus, cumulonimbus and stratus
(candidates: NOAA Photo Library, PD); AI fog filling a valley at dawn;
AI a cold glass with condensation on a café table.

**Ledger.** saturation vapour pressure formula (Alduchov and Eskridge 1996,
DOI, or WMO-No. 8); dry adiabatic lapse rate and the specific heat of dry air
(AMS Glossary); dew-point lapse rate (AMS Glossary or a textbook source);
droplet, nucleus and raindrop sizes (AMS Glossary); the standard-atmosphere
lapse 6.5 °C/km (reuse Book 1's row if minted, else the U.S. Standard
Atmosphere 1976).
**Datasets.** none.

**Weekend problem --- "A summer afternoon over the plain".** A morning
sounding and the forecast surface temperature and dew point. I humidity and
dew point; II the rising parcel and its condensation level; III stability
against the sounding, how high the cloud grows; IV the evening and the dew.
**Named final number:** *the base of the afternoon cumulus, about 1.5 km.*

---

### g10.05 `storms-and-cyclones` --- Storms and Tropical Cyclones

**Hook.** A summer storm: the flash, then counting the seconds to the
thunder (a `safety` box: indoors, never under a tree).

**Sections.**
1. *Thunderstorms* --- the cumulonimbus, its updraughts and downdraughts,
   three stages; lightning and thunder; distance from the delay (speed of
   sound recalled from the physics books).
2. *Tornadoes* --- definition; supercells told; size, winds, rotation;
   where they are most frequent.
3. *Tropical cyclones* --- anatomy (eye, eyewall, rain bands, warm core,
   central pressure); where and when (warm sea surface, away from the
   equator: the Earth's rotation, told); tracks (computed map); the energy
   source: latent heat released by condensation (a heat engine, told).
4. *Intensity, winds and surges* --- the Saffir--Simpson scale; the storm
   surge (wind set-up plus the low-pressure bulge, about 1 cm per hPa,
   computed from the density of seawater); records (sourced).

**Definitions.** thunderstorm (`def:g10:storms-and-cyclones:thunderstorm`);
lightning (`...:lightning`); tornado (`...:tornado`); tropical cyclone, eye,
eyewall (`...:tropical-cyclone`); Saffir--Simpson scale (`...:scale`); storm
surge (`...:storm-surge`).
**Statements.** prop. the energy source of a tropical cyclone (latent heat);
prop. the pressure bulge of a surge (derived from the weight of a water
column); method: distance of a storm from flash to thunder; safety box.
**Recall.** air mass, front, depression, anticyclone, isobar (Book 1,
grade 8); natural hazard (Book 1, grade 5); humidity, dew point,
instability, latent heat (this year).

**Figures.** S the three stages of a thunderstorm; S cross-section of a
tropical cyclone (Northern Hemisphere: inflow anticlockwise seen from above,
outflow aloft, sinking air in the eye); F `cyclone_tracks` (world map of
tropical-cyclone tracks from IBTrACS, decimated; tested: no genesis within
a few degrees of the equator; almost none in the South Atlantic); F
pressure--wind scatter (same script; tested: lower pressure, stronger wind);
S storm-surge schematic; P a hurricane seen from orbit (candidate: NASA
"Hurricane Isabel from ISS", PD); P a tornado (candidate: NOAA Photo
Library, PD); P lightning (candidate: NOAA, PD); AI a flooded street after a
storm.

**Ledger.** Saffir--Simpson thresholds (NHC); the 26.5 °C sea-surface
threshold and the hurricane energy estimates (NOAA AOML Hurricane Research
Division FAQ); global flash rate (Christian et al. 2003, DOI); latent heat of
vaporisation (a physics or NIST source); speed of sound in air; density of
seawater (reuse g10.06 row); record storms (NHC tropical cyclone reports);
IBTrACS (dataset row).
**Datasets.** `grade-10-ibtracs` (new; see the Phase A report).

**Weekend problem --- "The heat engine of a hurricane".** I a day's rain over
the storm (volume, mass); II the latent heat released per day; III the
power, compared with the world's electricity generation; IV the kinetic
energy of the winds and the storm's efficiency.
**Named final number:** *about one part in 400 of the heat released by
condensation becomes wind.*

---

### g10.06 `layered-ocean` --- The Layered Ocean

**Hook.** In a summer sea, the swimmer's feet suddenly find cold water a few
metres down.

**Sections.**
1. *Measuring the ocean* --- instruments lowered from ships, profiling floats
   (`dated` box with the number of floats).
2. *Temperature with depth* --- the mixed layer, the thermocline, the deep
   ocean; three latitudes compared (computed profiles); the seasonal
   thermocline.
3. *Salinity and density* --- seawater density from temperature and salinity
   (computed); halocline and pycnocline; a stratified ocean is stable; the
   cold, dense deep water (recalled from Book 1, grade 8).
4. *Upwelling* --- along coasts and at the equator, the wind and the Earth's
   rotation push surface water away, cold deep water rises (told: Ekman
   transport is Year 1's); nutrients and productive seas (biology recalled);
   the ocean-colour map.

**Definitions.** mixed layer (`def:g10:layered-ocean:mixed-layer`);
thermocline, halocline, pycnocline, deep ocean (`...:thermocline`);
stratification (`...:stratification`); upwelling (`...:upwelling`).
**Statements.** prop. seawater density grows with salinity and falls with
temperature (computed table, values from the equation of state); method:
reading an ocean profile; example: three profiles.
**Recall.** salinity, surface and deep currents, seafloor features (Book 1,
grade 8); density (physics); photosynthesis and productivity (biology).

**Figures.** F `ocean_profiles` (temperature, salinity and density against
depth at a tropical, a mid-latitude and a polar site, from WOA23; tested:
tropical surface warmer than at 1000 m by more than 20 °C, polar profile
within a few degrees); F density against temperature for three salinities
(equation of state; tested: 1028.1 kg/m³ at 0 °C and 35); S summer and winter
mixed layer; S coastal upwelling (Southern Hemisphere, off Peru: wind from
the south, surface water pushed offshore, cold water rising); P an ocean
colour map (candidate: NASA SeaWiFS or MODIS chlorophyll, PD); P a
profiling float or a sampling rosette (candidate: NOAA, PD); AI optional.

**Ledger.** WOA23 (dataset row); the equation of state of seawater (UNESCO
1981 / Millero and Poisson 1981, DOI); number of profiling floats (Argo,
`dated`); mean ocean depth and volume (Charette and Smith 2010, Oceanography,
DOI); upwelling regions (a NOAA page).
**Datasets.** `grade-10-woa23` (new: three profiles and one section through
an ERDDAP or THREDDS subset).

**Weekend problem --- "A cast off Peru".** Profiles off Peru and in the
subtropical gyre. I read the mixed layer and the thermocline; II densities at
the surface and at 200 m; III stratification compared; IV why the Peruvian
waters are productive.
**Named final number:** *the density difference between the surface and
200 m in the gyre, compared with off Peru (in kg/m³; value from the
profiles).*

---

### g10.07 `soil-formation` --- Soil, a Slow-Forming Resource

**Hook.** A road cutting in the tropics: red earth above rotten granite that
crumbles in the hand but still shows its crystals (a photograph).

**Sections.**
1. *From rock to soil* --- the soil recalled from the biology books; parent
   rock, saprolite, the profile (horizons recalled, never re-taught);
   physical and chemical weathering (weathering recalled from Book 1,
   grade 5).
2. *Chemical weathering* --- hydrolysis of feldspar into kaolinite (\ce
   balanced); dissolution of calcite; oxidation of iron (redox recalled
   from the chemistry books); the order of mineral stability (told).
3. *Clays and humus* --- clay minerals as tiny sheet silicates; the
   clay--humus complex holds nutrients (humus recalled from the biology
   books).
4. *Soils and climate* --- warm and wet speeds weathering; laterites of the
   humid tropics, thin soils of cold and dry lands; depth of weathering with
   latitude.
5. *Slow to form, quick to lose* --- soil production 0.01--0.1 mm per year
   against erosion of ploughed fields near 1 mm per year (sourced
   compilation); time scales.

**Definitions.** chemical weathering (`def:g10:soil-formation:chemical-
weathering`); hydrolysis (`...:hydrolysis`); clay mineral (`...:clay`);
parent rock, saprolite (`...:weathering-profile`); laterite (`...:laterite`).
**Statements.** prop. the hydrolysis of feldspar (balanced equation); prop.
dissolution of calcite (balanced); method: comparing a formation rate with an
erosion rate; example: the weathering of a granite.
**Recall.** weathering, erosion, deposition (Book 1, grade 5); soil, humus,
decomposers (biology); soil horizons (biology, recalled only); minerals
(Book 1, grade 6); redox reactions (chemistry).

**Figures.** S a weathering profile (bedrock, saprolite, soil) with
thicknesses typical of a humid tropical and a temperate site; S depth of
weathering along a pole-to-equator transect (qualitative); bar chart (log
scale) of soil production and erosion rates (ledger coordinates); S a clay
sheet holding cations (schematic); P a laterite (candidate, Commons CC);
P a soil profile (candidate: USDA NRCS, PD); P saprolite (candidate: USGS,
PD); AI a ploughed field with rills after a storm.

**Ledger.** soil production and erosion rates (Montgomery 2007, PNAS, DOI);
kaolinite and orthoclase formulas (Mindat); the mineral stability order
(Goldich 1938, DOI, told); weathering-depth examples (a fetched source).
**Datasets.** none.

**Weekend problem --- "The lifetime of a soil".** I a profile read from a
photograph; II the chemistry of a weathering granite (balanced reactions,
mass of clay formed); III formation against erosion; IV the soil's lifetime.
**Named final number:** *the time to lose a metre of soil under
conventional ploughing (net loss rate from the compilation), a few
centuries.*

---

### g10.08 `drainage-basins` --- Drainage Basins, Rivers and Floods

**Hook.** A river rises two days after the rain stopped, at a town where it
never rained.

**Sections.**
1. *The drainage basin* --- definition and divide; the basin of the Varden
   river computed on the region's map; the largest basins of the world.
2. *Discharge* --- volume per second, velocity times cross-section; method:
   the velocity--area method; the largest rivers (sourced).
3. *The hydrograph* --- rain, runoff, peak, lag time, baseflow; what makes a
   flood flashy (steep, small, paved basins); a real flood hydrograph.
4. *Floods and their return period* --- annual maxima, ranking, T = (n+1)/m;
   probability 1/T in any year; chance of at least one in N years
   1 − (1 − 1/T)^N (powers only).
5. *Dams and levees* --- storage lowers the peak downstream; levees confine
   the flow and raise its level (physical effects only).

**Definitions.** drainage basin, drainage divide
(`def:g10:drainage-basins:drainage-basin`); discharge (`...:discharge`);
hydrograph, baseflow, lag time (`...:hydrograph`); return period
(`...:return-period`).
**Statements.** prop. discharge = mean velocity × cross-section area
(derived); prop. probability of at least one event in N years (derived);
method: velocity--area; method: return periods from a record.
**Recall.** the water cycle (physics); permeability, aquifer (Book 1,
grade 6); meander, delta, floods (Book 1, grade 5); contours and the
Varden Hills (Book 1, grades 2 and 9).

**Figures.** F `varden_basin` (the drainage basin of the Varden river,
computed by routing every grid cell downhill on `figdata/shared/region.py`'s
topography, imported, never edited; tested: every basin cell drains to the
outlet); S cross-section of a channel with velocity measurements; F
`flood_frequency` (a real flood hydrograph from USGS daily values, and the
annual peaks against return period, from the USGS peak-flow record of one
station; tested: the largest peak has T = n+1); S dam storage and levee
effects on a hydrograph; P a flooded river (candidate: USGS or NOAA, PD);
P a stream-gauging station (candidate: USGS, PD); AI a river in flood across
meadows seen from a bridge.

**Ledger.** USGS peak-flow and daily-value records (dataset rows); largest
basins and discharges (Amazon, Congo, Mississippi: primary sources with
DOI or agency pages).
**Datasets.** `grade-10-usgs-flow` (new: one station's annual peaks and one
water year of daily discharge; candidate station with a long record).

**Weekend problem --- "The hundred-year flood".** A town on a river with 90
years of annual peaks. I the basin and the discharge; II reading the flood
hydrograph; III ranking the peaks, return periods; IV probabilities over
time.
**Named final number:** *the chance of at least one 100-year flood in 30
years, 26 %.*

---

### g10.09 `freshwater-resources` --- Freshwater Resources

**Hook.** From space, the Aral Sea of 1989 and of 2014: a lake the size of
Ireland has mostly gone (NASA images).

**Sections.**
1. *Where the water is* --- the stocks: ocean, ice, groundwater, lakes, soil,
   air, rivers; fresh water about 2.5 %, most of it frozen or underground.
2. *Flows* --- the water cycle recalled (physics): evaporation,
   precipitation, runoff; stock and flux; renewable fresh water is a flux.
3. *Residence time* --- stock divided by flux (computed for each reservoir:
   days for the air, weeks for rivers, millennia for the ocean and deep
   groundwater).
4. *Aquifers as reservoirs* --- recharge, fossil groundwater, the falling
   water tables of heavily pumped aquifers (sourced records); satellites that
   weigh water (told).
5. *Overuse as a physical fact* --- the Aral Sea's budget: inflow cut,
   evaporation unchanged, the level falls. No policy.

**Definitions.** stock, flux (`def:g10:freshwater-resources:stock`);
residence time (`...:residence-time`); renewable freshwater
(`...:renewable`); fossil groundwater (`...:fossil-groundwater`).
**Statements.** prop. residence time = stock / flux at steady state
(derived); method: a water budget; example: the residence time of water in
the atmosphere.
**Recall.** the water cycle as a mass balance (physics); porosity,
permeability, water table, aquifer (Book 1, grade 6); salt and fresh water
(Book 1, grade 2); drainage basin, discharge (\cref{ch:g10:drainage-basins}).

**Figures.** F `residence_times` (stocks and residence times, log scale;
tested: the ocean's residence time near 3000 years from the sourced stock
and flux); S the global water cycle with stocks and fluxes; S an aquifer
section: recharge area, unconfined and confined parts, fossil water;
F the Aral Sea level and area against time (ledger table plotted by a small
script, tested against its rows); P the Aral Sea 1989 and 2014 (candidate:
NASA Earth Observatory, PD); P centre-pivot irrigation from orbit
(candidate: NASA, PD); AI a hand-pump well in a dry landscape.

**Ledger.** stocks of water (USGS Water Science School table, after
Shiklomanov; or Gleick 1996); global fluxes (Trenberth et al. 2007, J.
Hydrometeorology, DOI); residence times cross-check (Oki and Kanae 2006,
Science, DOI); Aral Sea area, level, inflow (Micklin 2007, Annu. Rev. Earth
Planet. Sci., DOI; NASA Earth Observatory); a pumped aquifer's decline
(USGS report); the age of a fossil aquifer (sourced).
**Datasets.** none (ledger tables).

**Weekend problem --- "The Aral Sea's budget".** I area, depth, volume; II
inflow and evaporation before 1960; III after the rivers were diverted, the
imbalance; IV the yearly fall of the level and the salinity rise.
**Named final number:** *the yearly fall of the Aral Sea's level in the
1980s, close to 1 m (value computed from the sourced budget).*

---

## Grade 11

### g11.01 `drift-to-spreading` --- From Continental Drift to Seafloor Spreading

**Hook.** 1950s: a ship's echo sounder pings every few seconds across the
Atlantic and draws, on a paper roll, a mountain range no one has seen.

**Sections.**
1. *Why drift was rejected* --- recalled from Book 1, grade 7 (Wegener,
   Jeffreys); what was missing: a mechanism and the ocean floor.
2. *Mapping the ocean floor* --- echo sounding (echo recalled from the
   physics books); the ridge system around the globe (65 000 km), its rift
   valley, high heat flow and shallow earthquakes.
3. *Seafloor spreading* --- Hess's idea; definition; full and half rates.
4. *Magnetic reversals and the striped seafloor* --- remanent magnetisation
   (geomagnetic field recalled from the physics books); reversals; the
   polarity time scale (0--5 Ma); the magnetic anomaly; Vine and Matthews;
   a computed profile; symmetric stripes give the rate.
5. *Ages from the sediments* --- deep-sea drilling: basement ages grow with
   distance from the ridge; no ocean floor older than about 180--200 Ma.

**Definitions.** seafloor spreading (`def:g11:drift-to-spreading:spreading`);
spreading rate (`...:spreading-rate`); remanent magnetisation, Curie
temperature (`...:remanence`); magnetic reversal, normal and reversed
polarity (`...:reversal`); magnetic anomaly (`...:anomaly`).
**Statements.** prop. a stripe's distance = half rate × age (derived);
method: a spreading rate from a magnetic profile; history boxes: Hess 1962;
Vine and Matthews 1963; Marie Tharp's maps (text only).
**Recall.** continental drift, plates, boundaries (Book 1, grade 7);
seafloor features (Book 1, grade 8); the Earth's magnetic field, magnetic
poles (physics); echoes and sonar (physics).

**Figures.** S lava cooling records the field (remanence); S block diagram of
the striped seafloor; F `magnetic_stripes` (anomaly profiles across a slow
and a fast ridge from the polarity time scale; tested: symmetric, boundaries
at half rate × age); F `seafloor_age` (map of the age of the ocean floor;
tested: oldest below 200 Ma, ages increasing away from ridges); F
`sediment_ages` (basement age against distance at the South Atlantic drill
sites; tested: fitted slope gives the published rate); P the drilling ship
Glomar Challenger or JOIDES Resolution (candidate, PD/agency); P a portrait
of Harry Hess (candidate, verify).

**Ledger.** polarity chron boundaries 0--5 Ma (Ogg 2020 in GTS2020, or Cande
and Kent 1995, DOI); Curie temperature of magnetite; ridge-system length
(NOAA Ocean Exploration); Hess 1962 and Vine--Matthews 1963 (DOIs); DSDP
Leg 3 site distances and basement ages (Maxwell et al. 1970, Science, DOI);
oldest seafloor (from the age grid, computed; Seton et al. 2020 / Müller et
al. 2008, DOI).
**Datasets.** `grade-11-seafloor-age` (new: a 1° or coarser age grid).

**Weekend problem --- "The age of the South Atlantic".** I the drill sites
and their ages; II the rate from the sediments; III the rate from the
magnetic stripes; IV extrapolating to the continental margins.
**Named final number:** *the age of the oldest South Atlantic floor beside
Africa, about 130 million years.*

---

### g11.02 `seismic-structure` --- Seismic Waves Reveal the Interior

**Hook.** October 1909, the Kupa valley: Andrija Mohorovičić reads two P
arrivals where there should be one.

**Sections.**
1. *Seismic waves and travel times* --- earthquakes recalled (Book 1,
   grade 7); P and S waves (defined from their arrival order and what they
   cross; their mechanics recalled from the physics books); speeds;
   travel-time curves; method: distance from the S--P delay.
2. *Refraction and the Moho* --- refraction recalled (physics); the
   refracted wave along the Moho; the crossover distance; Moho depths under
   continents and oceans.
3. *The core* --- Oldham, Gutenberg (2900 km); the P shadow zone between
   about 103° and 142°; no S beyond 103°: a liquid outer core; Lehmann and
   the inner core (1936).
4. *A reference Earth model* --- PREM (1981): velocities and density with
   depth; the discontinuities (Moho, 410, 660 told, core--mantle boundary
   2891 km, inner-core boundary 5150 km).

**Definitions.** P wave, S wave (`def:g11:seismic-structure:body-waves`);
travel-time curve (`...:travel-time`); seismic discontinuity
(`...:discontinuity`); Moho (`...:moho`); shadow zone (`...:shadow-zone`);
core--mantle boundary, outer core, inner core (`...:core`); reference Earth
model (`...:reference-model`).
**Statements.** prop. travel time of the head wave (derived with the critical
angle: right-triangle trigonometry and Snell's law recalled); prop. the
crossover distance (derived); method: locating the Moho from a travel-time
diagram; history boxes: Mohorovičić, Lehmann.
**Recall.** focus, epicentre, magnitude, seismometer (Book 1, grade 7);
crust, mantle, core (Book 1, grade 6); waves, refraction and Snell's law
(physics, grade 10).

**Figures.** F `prem_profiles` (P and S speeds and density against depth;
tested: core--mantle boundary at 2891 km, S speed zero in the outer core,
inner-core boundary at 5150 km); F `seismic_rays` (ray paths through a
spherical Earth with PREM speeds, the P shadow zone; tested: shadow from
about 98--103° to about 142°; P travel time at 60° within 2 % of the
published reference table); F travel-time curves of P and S (same script);
F `moho_refraction` (direct and refracted arrivals for a two-layer crust;
tested: crossover formula); S refraction at the Moho, the head wave; P a
seismometer (candidate: USGS, PD); P Inge Lehmann (candidate, verify PD);
AI a seismology observatory room.

**Ledger.** PREM (shared dataset); reference travel times for the test
(iasp91 or ak135 tables, DOI); history: Mohorovičić 1909, Oldham 1906,
Gutenberg 1913, Lehmann 1936 (DOIs or institutional history pages); typical
Moho depths (USGS or IRIS); shadow-zone limits (IRIS/USGS education page).
**Datasets.** PREM (shared).

**Weekend problem --- "Finding the Moho".** Arrival times at stations 20 to
300 km from a local earthquake. I the direct wave and the crust's speed; II
the refracted wave and the mantle's speed; III the crossover; IV the
intercept time and the depth.
**Named final number:** *the depth of the Moho beneath the region, about
30 km.*

---

### g11.03 `lithosphere-asthenosphere` --- Lithosphere and Asthenosphere

**Hook.** Nine tenths of an iceberg is under water. Mountains, too, float on
something --- but on what, when the mantle is solid rock?

**Sections.**
1. *Two ways to layer the Earth* --- chemical layers (crust, mantle, core,
   recalled) and mechanical layers (lithosphere, asthenosphere).
2. *The low-velocity zone* --- S speeds drop below the lithosphere (PREM
   computed); a little melt and hot, weak rock.
3. *The geotherm* --- temperature with depth; the surface gradient 25--30 °C
   per km; the geotherm approaches the mantle's melting curve near
   100 km; the lithosphere's base near 1300 °C.
4. *Isostasy* --- definition; the Airy model **derived** from equal pressures
   at the compensation depth (pressure of a column recalled from the
   physics books); the root of a range; why continents stand high: the
   hypsometric curve has two peaks.
5. *A flexible lid* --- the lithosphere carries loads (islands, ice) and
   bends (told; rebound is g12's).

**Definitions.** lithosphere (`def:g11:lithosphere-asthenosphere:
lithosphere`); asthenosphere (`...:asthenosphere`); low-velocity zone
(`...:lvz`); geotherm, geothermal gradient (`...:geotherm`); isostasy,
compensation depth (`...:isostasy`); hypsometric curve (`...:hypsometry`).
**Statements.** prop. Airy isostasy (derived; indexed here as the named
model, owner chapter for the school books) (`prop:g11:lithosphere-
asthenosphere:airy`); prop. continents and ocean floors (hypsometry,
computed fractions); method: computing a root.
**Recall.** crust, mantle, core (Book 1, grade 6); Moho and PREM
(\cref{ch:g11:seismic-structure}); density, floating, pressure (physics);
temperature rises with depth (Book 1, grade 6).

**Figures.** S chemical and mechanical layers side by side, depths to scale
for the upper 400 km; F PREM S speed 0--400 km (from `prem_profiles`;
tested: low-velocity zone between 80 and 220 km); F `geotherm_solidus`
(a geotherm and the peridotite solidus; tested: surface gradient = q/k,
solidus at zero pressure from the source); S Airy columns with a mountain,
a plain and an ocean; F `hypsometry` (elevation distribution of the Earth
from ETOPO1 at 1°; tested: two modes, land fraction near 29 %); P an
iceberg (candidate: NOAA, PD).

**Ledger.** densities of crust and mantle (PREM computed, or a DOI source);
lithosphere thickness under oceans and continents (USGS and a DOI review);
temperature at the base of the lithosphere; surface geothermal gradient
(USGS/BGS); peridotite solidus (Hirschmann 2000, G³, DOI); Tibet crustal
thickness (a DOI seismic study).
**Datasets.** PREM, ETOPO1 (shared).

**Weekend problem --- "Why Tibet stands five kilometres high".** I the
plateau's elevation and the crust of a lowland; II Airy's balance written
for two columns; III the root and the total crust; IV comparison with the
seismic measurements, and the asthenosphere's role.
**Named final number:** *the thickness of the crust under Tibet, about
70 km.*

---

### g11.04 `plate-motions` --- Plates and Their Motions

**Hook.** A satellite-positioning antenna on Mauna Kea moves about 7 cm a
year toward the north-west, every year, without stopping.

**Sections.**
1. *Rigid plates on a sphere* --- plates move as rigid caps; deformation
   gathers at the boundaries; a motion on a sphere is a rotation about an
   axis through the centre (told: Year 1 owns Euler poles); transform faults
   follow small circles (told).
2. *Measuring the motions* --- from magnetic stripes (recalled) and from
   satellite positioning (time series, computed rates); relative and
   absolute motion; adding velocities as arrows (method box; vectors).
3. *Hotspot tracks* --- a plume fixed under a moving plate; the Hawaiian--
   Emperor chain: ages grow with distance; the bend at 47 Ma; the plate's
   absolute speed.
4. *The predictive power of the model* --- earthquakes on boundaries,
   seafloor ages, mountain belts, rates that agree across methods (computed
   comparison).

**Definitions.** rigid plate (`def:g11:plate-motions:rigid-plate`); relative
motion, absolute motion (`...:relative-motion`); hotspot track
(`...:hotspot-track`).
**Statements.** prop. relative velocities add as arrows (vector sum); prop.
hotspot age--distance gives the plate's absolute speed (derived); method:
a rate from a positioning time series; method: closing a velocity triangle.
**Recall.** plate, boundaries, speeds (Book 1, grade 7); hotspot (Book 1,
grade 7); satellite positioning (Book 1, grade 9); stripes and spreading
rates (\cref{ch:g11:drift-to-spreading}).

**Figures.** F `plate_velocities` (world map with plate velocities computed
from a published set of rotation poles, decimated arrows; tested: Pacific
near Hawaii 7--8 cm/yr toward the north-west; also mean speeds of plates
with and without slabs, used in g11.06); F `gnss_series` (east and north
positions of two stations against time; tested: fitted rates near the
published); F `hawaii_chain` (age against distance from Kīlauea; tested:
slope near 9 cm/yr along the Hawaiian segment); S a plate moving over a
fixed plume, ages increasing; S a velocity triangle; P the Hawaiian--Emperor
chain on a bathymetric map (candidate: NOAA, PD); P a positioning station
(candidate: USGS, PD).

**Ledger.** plate rotation poles (Argus et al. 2011, NNR-MORVEL56, G³, DOI);
station positions (Nevada Geodetic Laboratory, Blewitt et al. 2018, DOI);
Hawaiian--Emperor volcano ages (Clague and Dalrymple 1987 / USGS; the bend
at 47 Ma, Sharp and Clague 2006, Science, DOI); volcano coordinates (GVP
shared dataset or USGS).
**Datasets.** `grade-11-gnss` (new: two NGL station time series);
rotation-pole table (ledger rows, no download).

**Weekend problem --- "Reading the Hawaiian--Emperor chain".** I ages and
distances; II the plate's speed over the hotspot; III the bend and the
change of direction; IV comparison with today's satellite measurement.
**Named final number:** *the speed of the Pacific plate over the Hawaiian
hotspot, about 9 cm per year.*

---

### g11.05 `ocean-ridges` --- Ocean Ridges and the Oceanic Lithosphere

**Hook.** February 1977, 2500 m down on the Galápagos Rift: the submersible
Alvin finds warm springs, clams and tube worms where no one expected life
(history box).

**Sections.**
1. *The oceanic lithosphere* --- sediments, pillow basalts, sheeted dykes,
   gabbro, peridotite; thicknesses; the rock names peridotite and gabbro
   defined here (basalt recalled from Book 1, grade 6).
2. *Melting without heating* --- partial melting; a rising mantle crosses
   its melting curve (decompression, computed); basalt from peridotite.
3. *Fast and slow ridges* --- rates from the plate model; the axial valley
   and its normal faults at slow ridges, a smooth high at fast ones.
4. *Hydrothermal vents* --- seawater circulates through hot crust; black
   smokers at 350--400 °C; chemistry of the vents told.
5. *Cooling, thickening, sinking* --- the lithosphere cools and thickens
   with age; depth grows as the square root of age (admitted, computed
   check against the age grid); old lithosphere is dense (leads to g11.06).

**Definitions.** oceanic lithosphere, oceanic crust (`def:g11:ocean-ridges:
oceanic-lithosphere`); peridotite (`...:peridotite`); gabbro (`...:gabbro`);
partial melting, decompression melting (`...:partial-melting`);
hydrothermal circulation, black smoker (`...:hydrothermal`); normal fault
(`...:normal-fault`).
**Statements.** prop. depth of the ocean floor against age (admitted law
with the published coefficients, checked on data); method: where does the
rising mantle melt?; example: a slow and a fast ridge.
**Recall.** seafloor spreading, stripes (\cref{ch:g11:drift-to-spreading});
lithosphere, geotherm (\cref{ch:g11:lithosphere-asthenosphere}); magma,
basalt (Book 1, grades 6--7); fault (Book 1, grade 7).

**Figures.** S section of a ridge axis (magma lens, crustal layers, upwelling
mantle, isotherms deepening away from the axis); F `ridge_melting` (an
adiabat and the solidus; tested: melting starts at the published depth range);
F depth against age (binned medians from ETOPO1 and the age grid, with the
square-root law; tested: coefficient near the published one); S hydrothermal
circulation; S axial valley with normal faults (fault ticks on the
downthrown side); P a black smoker (candidate: NOAA, PD); P pillow lava
(candidate: NOAA "Pillow basalt", PD); P peridotite or gabbro hand specimen
(candidate, Commons).

**Ledger.** oceanic crust thickness (White et al. 1992, JGR, DOI); vent
temperatures (NOAA/WHOI); the 1977 discovery (WHOI); depth--age law (Parsons
and Sclater 1977, JGR, DOI); mantle potential temperature and melting depth
(a DOI review); melt fraction (same).
**Datasets.** ETOPO1 (shared), `grade-11-seafloor-age` (from g11.01).

**Weekend problem --- "The life of a piece of Pacific floor".** I born at
the East Pacific Rise (rate); II distance travelled with time; III depth with
age; IV its density and its fate.
**Named final number:** *the depth of 64-million-year-old ocean floor, about
5.3 km.*

---

### g11.06 `subduction-zones` --- Subduction Zones

**Hook.** Earthquakes under Tonga happen 600 km deep, where rock should be
too hot and soft to break.

**Sections.**
1. *Trenches and dipping earthquake zones* --- Wadati and Benioff; computed
   sections across Tonga, Japan and the Andes; depths to about 700 km.
2. *Why old lithosphere sinks* --- density grows as the plate cools; the
   slab; slab pull and ridge push; plates attached to slabs move fastest
   (computed from the plate model).
3. *The slab transformed at depth* --- blueschist, then eclogite: basalt
   becomes denser than the mantle around it; this pulls harder.
4. *The anatomy of a subduction zone* --- trench, forearc, scraped sediments
   (told), volcanic arc (named; defined in g12), back-arc.

**Definitions.** subduction, subduction zone (`def:g11:subduction-zones:
subduction`); Wadati--Benioff zone (`...:benioff`); slab (`...:slab`); slab
pull, ridge push (`...:slab-pull`); blueschist, eclogite (`...:eclogite`).
**Statements.** prop. the dip of a slab from an earthquake section (tangent);
prop. plates with slabs are fast (computed comparison); method: reading an
earthquake section.
**Recall.** convergent boundary, trench (Book 1, grades 7--8); oceanic
lithosphere, ageing and sinking (\cref{ch:g11:ocean-ridges}); magnitude,
tsunami (Book 1, grade 7).

**Figures.** F `slab_sections` (earthquakes projected on profiles across
Tonga and Japan, depth against distance; tested: deepest events below
600 km in Tonga); F world map of earthquakes coloured by depth (decimated
M ≥ 6.5; tested: deep events only near subduction lines); F mean plate speed
with and without slabs (from `plate_velocities`); S cross-section of a
subduction zone (trench, wedge, slab, arc, isotherms bent down); P eclogite
and blueschist (candidates, Commons CC); P the 2011 tsunami or its effects
(candidate: US Navy/USGS, PD).

**Ledger.** maximum earthquake depth (USGS); the 2011 Tōhoku event (USGS
event page); densities of basalt and eclogite (a DOI source or Mindat
aggregates); the slab-pull correlation (Forsyth and Uyeda 1975, DOI);
history of Wadati 1928 and Benioff (sourced).
**Datasets.** USGS M ≥ 6 catalogue with depths (shared).

**Weekend problem --- "The Tonga slab".** I the earthquake section and the
dip; II the convergence rate at the trench; III the slab's path to 660 km;
IV the slab's fate.
**Named final number:** *the time for Pacific floor to sink from the Tonga
Trench to 660 km, about 5 million years.*

---

### g11.07 `minerals` --- Minerals

**Hook.** A granite pebble under a hand lens: grey glassy grains, pink
blocky ones, black flakes that peel.

**Sections.**
1. *Telling minerals apart* --- habit; colour (unreliable) and lustre;
   cleavage and fracture; hardness and the Mohs scale; density (recalled).
2. *Silicates* --- oxygen and silicon make three quarters of the crust's
   mass; the silicon--oxygen tetrahedron; isolated, chains, double chains,
   sheets, frameworks (told structurally; crystal lattices are the chemistry
   books'); the six rock-forming silicates.
3. *Minerals make rocks* --- granite, basalt, peridotite by their minerals.
4. *Thin sections* --- 30 µm slices; plane and crossed polarised light
   (photographs); identification told (birefringence is Year 1's).

**Definitions.** silicate, silicon--oxygen tetrahedron (`def:g11:minerals:
silicate`); rock-forming silicates (`...:rock-forming`); habit
(`...:habit`); cleavage, fracture (`...:cleavage`); hardness, Mohs scale
(`...:hardness`); lustre (`...:lustre`); thin section, polarising microscope
(`...:thin-section`).
**Statements.** method: identifying a mineral in hand specimen; prop. the
density of a rock from its minerals (weighted mean, derived); example:
granite.
**Recall.** mineral, crystal, rock families, scratch hardness (Book 1,
grade 6); density (physics); ions and formulas (chemistry); peridotite,
gabbro (\cref{ch:g11:ocean-ridges}).

**Figures.** S the tetrahedron and the four structures; S cleavage of
pyroxene (about 87°/93°) and amphibole (about 56°/124°) in cross-section;
chart Mohs number against absolute hardness (ledger coordinates, log axis);
P quartz, orthoclase, biotite, olivine specimens (candidates: Commons CC or
USGS PD); P a granite and a basalt in thin section, plane and crossed light
(candidates, Commons CC); AI a geologist examining a specimen with a hand
lens.

**Ledger.** crustal abundances of O and Si (Rudnick and Gao 2003, DOI);
Mohs scale and absolute hardness (a fetched source); mineral densities and
formulas (Mindat or RRUFF, properties only); thin-section thickness (a
fetched methods source); cleavage angles (Mindat).
**Datasets.** none.

**Weekend problem --- "The density of a granite".** I identifying the
minerals; II their proportions from a point count; III the rock's density;
IV the mass of a block and a check against measurement.
**Named final number:** *the density of the granite, about 2.64 g/cm³.*

---

### g11.08 `igneous-rocks` --- Igneous Rocks

**Hook.** Basalt columns by the sea, a granite cliff in a mountain valley:
the same kind of molten rock, cooled at different speeds and depths
(photographs).

**Sections.**
1. *Volcanic and plutonic rocks* --- cooling rate and crystal size;
   glassy, microlitic, granular textures; phenocrysts and porphyritic
   rocks (two-stage cooling).
2. *Naming igneous rocks* --- silica content, felsic and mafic; the pairs
   basalt--gabbro, andesite--diorite, rhyolite--granite (a chart).
3. *The order of crystallisation* --- Bowen's series, told (fractional
   crystallisation is Year 2's); olivine first, quartz last; linked to the
   minerals of \cref{ch:g11:minerals}.
4. *Intrusions* --- dykes, sills, plutons; chilled margins; cooling time
   grows as the square of thickness (computed model, admitted law).

**Definitions.** volcanic rock, plutonic rock (`def:g11:igneous-rocks:
volcanic-plutonic`); texture (`...:texture`); phenocryst, porphyritic
(`...:porphyritic`); felsic, mafic (`...:felsic-mafic`); andesite, diorite,
rhyolite (`...:rock-names`); dyke, sill, pluton (`...:intrusion`).
**Statements.** prop. cooling time ∝ thickness² (admitted; computed table);
method: naming an igneous rock from texture and minerals; example: two
basalts.
**Recall.** magma, effusive and explosive eruptions (Book 1, grade 7);
basalt, granite (Book 1, grade 6); peridotite, gabbro, partial melting
(\cref{ch:g11:ocean-ridges}); minerals (\cref{ch:g11:minerals}).

**Figures.** S classification chart (silica axis, textures, mineral bands);
S Bowen's series; S block diagram of intrusions (dyke, sill, pluton, feeding
a volcano); F `dyke_cooling` (conductive cooling of sheets of several
thicknesses: time to solidify against thickness; tested: doubling the
thickness quadruples the time); P granite, gabbro, andesite, rhyolite,
basalt, obsidian specimens (candidates: USGS or Commons); P a granular and a
microlitic texture in thin section (candidates, Commons CC); P basalt columns
(candidate: Giant's Causeway, Commons CC).

**Ledger.** silica boundaries (IUGS: Le Bas and Streckeisen 1991, DOI, or Le
Maitre 2002); rock thermal diffusivity (a DOI source); the history of Bowen
1928 (sourced).
**Datasets.** none.

**Weekend problem --- "A sill and its crystals".** I textures across a sill
(chilled margin to centre); II naming the rock; III cooling times; IV what
the crystal sizes tell about depth.
**Named final number:** *the time a 20-m sill takes to solidify (from the
computed model), of the order of a few decades.*

---

### g11.09 `fossil-fuel-geology` --- The Geology of Coal, Oil and Gas

**Hook.** A lump of coal split open shows the imprint of a fern leaf.

**Sections.**
1. *Preserving organic matter* --- most is recycled; still, anoxic waters;
   source rock and kerogen.
2. *Burial and maturation* --- sedimentary basins sink and fill; the geotherm
   (recalled) cooks the kerogen: the oil window and the gas window (computed
   depths).
3. *From source to trap* --- migration upward; reservoir rock and seal
   (porosity and permeability recalled from Book 1, grade 6); four kinds of
   trap; the petroleum system.
4. *Where hydrocarbons gather* --- rifts and passive margins: subsiding,
   restricted, salt-sealed (plate settings recalled).
5. *Coal* --- peat in swamps; burial; rank (lignite, bituminous coal,
   anthracite) and carbon content; compaction.

**Definitions.** sedimentary basin (`def:g11:fossil-fuel-geology:basin`);
source rock, kerogen (`...:source-rock`); maturation, oil window
(`...:oil-window`); migration (`...:migration`); reservoir rock, seal
(`...:reservoir`); trap (`...:trap`); petroleum system
(`...:petroleum-system`); coal, coalification, coal rank (`...:coal`).
**Statements.** prop. depth of the oil window from the geotherm (derived:
linear); method: reading a burial-history diagram; example: a trap in an
anticline.
**Recall.** fossil fuel (chemistry); fossil-fuel origin, ore deposits
(Book 1, grade 9); porosity, permeability (Book 1, grade 6); geotherm
(\cref{ch:g11:lithosphere-asthenosphere}); normal fault
(\cref{ch:g11:ocean-ridges}).

**Figures.** S a petroleum system section (source, migration, reservoir,
seal, trap); F `oil_window` (burial history of a basin with isotherms;
tested: the source rock enters the window when its temperature passes the
lower limit); S four traps (anticline, fault, salt dome, stratigraphic);
S a passive margin with salt and source rocks; chart carbon content by coal
rank (ledger coordinates); P a coal seam (candidate: USGS, PD); P a fossil
fern in coal (candidate, Commons); AI an offshore platform at sea.

**Ledger.** oil-window and gas-window temperatures (USGS); coal-rank carbon
contents (USGS fact sheet / ASTM via USGS); peat-to-coal compaction (a DOI
source); Carboniferous ages (shared ICS rows).
**Datasets.** none.

**Weekend problem --- "When did the source rock make oil?".** An invented
basin's burial history. I the stratigraphy and the source rock; II burial
against time; III temperature against time; IV entering and leaving the oil
window, and the trap's age.
**Named final number:** *the age at which the source rock entered the oil
window (from the computed history), in millions of years.*

---

## Grade 12

### g12.01 `continental-crust` --- The Continental Crust

**Hook.** On the banks of the Acasta River in northern Canada, a grey banded
rock 4.03 billion years old --- and older zircon grains from Western
Australia.

**Sections.**
1. *Granite and its relatives* --- granitoids; the average composition of
   the continental crust (about 60 % silica).
2. *A thick crust* --- thickness map (computed); 35--40 km on average, 70 km
   under the highest ranges.
3. *A light crust* --- densities of continental crust, oceanic crust and
   mantle; why continents do not subduct.
4. *An old crust* --- ages up to 4 Ga; cratons and shields; oceanic crust
   never older than about 200 Ma (computed from g11's age grid).
5. *Mountain roots* --- the root defined; Airy recalled; roots seen by
   seismology.

**Definitions.** continental crust (`def:g12:continental-crust:continental-
crust`); granitoid (`...:granitoid`); craton, shield (`...:craton`);
mountain root (`...:root`).
**Statements.** prop. the root of a range (Airy recalled, applied); method:
comparing continental and oceanic crust; example: the Alps' root.
**Recall.** isostasy, hypsometry (\cref{ch:g11:lithosphere-asthenosphere});
igneous rock names (\cref{ch:g11:igneous-rocks}); radiometric ages (the
physics books; \cref{ch:g12:age-of-the-earth} later this year).

**Figures.** F `crust_thickness` (world map from CRUST1.0; tested: maxima
above 65 km under Tibet and the Andes, ocean median near 7 km); S two
columns compared (thickness, density, age, composition); S a range and its
root; F age of the oceanic floor versus continental ages (histogram from the
age grid and sourced continental ages, optional); P the Acasta gneiss
(candidate, Commons CC); P a granite landscape (candidate: NPS, PD).

**Ledger.** continental crust area, thickness, density (Christensen and
Mooney 1995, JGR, DOI; Cogley 1984); composition (Rudnick and Gao 2003,
DOI); Acasta gneiss (Bowring and Williams 1999, DOI); Jack Hills zircon
(Wilde et al. 2001; Valley et al. 2014, DOIs); Alpine root (a DOI seismic
study).
**Datasets.** `grade-12-crust1` (new: CRUST1.0 1° thickness).

**Weekend problem --- "How heavy is the continental crust?".** I area; II
thickness and volume; III density and mass; IV compared with the Earth and
with the oceanic crust.
**Named final number:** *the continental crust is about 0.4 % of the Earth's
mass.*

---

### g12.02 `mountain-building` --- Building Mountains

**Hook.** Near the summit of Everest the rock is a grey limestone full of
fossils of sea creatures.

**Sections.**
1. *From subduction to collision* --- an ocean closes; buoyant continental
   crust cannot sink; collision, suture, ophiolites as stranded ocean floor.
2. *Shortening the crust* --- folds (anticline, syncline, fold axis; the
   Varden Hills section as an example), reverse faults and thrusts, nappes;
   shortening measured from a section (computed).
3. *Thickening and uplift* --- a thick crust floats high: the root
   (recalled).
4. *Two ranges* --- the Himalaya (India's journey north, collision about 50
   million years ago, the Indus--Tsangpo suture, the great thrusts; today's
   convergence from the plate model) and the Alps (Europe and Adria, their
   ophiolites and nappes, briefly: the Year 2 volume studies them in depth).

**Definitions.** continental collision (`def:g12:mountain-building:
collision`); fold, anticline, syncline, fold axis (`...:fold`); reverse
fault, thrust (`...:thrust`); nappe (`...:nappe`); ophiolite
(`...:ophiolite`); suture (`...:suture`); shortening (`...:shortening`).
**Statements.** prop. shortening of a folded layer from its length (derived:
original length is the length along the layer); method: reading a
cross-section for shortening; example: the Varden folds; example: India's
speed.
**Recall.** subduction, slab pull (\cref{ch:g11:subduction-zones}); oceanic
lithosphere (\cref{ch:g11:ocean-ridges}); continental crust, root
(\cref{ch:g12:continental-crust}); fault, convergent boundary (Book 1,
grade 7).

**Figures.** S three stages from subduction to collision; F the Varden Hills
section A--B (shared region tables) showing the anticline and the syncline;
S block diagram of an anticline--syncline pair (axis, limbs); S thrust and
nappe section; F `india_drift` (India's latitude against time from sourced
reconstructions; tested: speeds before and after collision); F
`fold_shortening` (a folded layer, measured and restored; tested: the
shortening formula); F the Alpine--Himalayan belt (shared geo tables,
regional window); P folded strata in the Alps (candidate, Commons CC);
P Everest from orbit (candidate: NASA, PD); P the Oman ophiolite or pillow
lavas in an ophiolite (candidate, Commons CC).

**Ledger.** Everest's height (2020 survey announcement); the summit
limestone (a DOI source); collision age (Book 1's usgs:himalaya, read-only,
plus a DOI source); India's palaeolatitudes and speeds (USGS This Dynamic
Earth figure, Patriat and Achache 1984, DOI); India--Eurasia convergence
today (computed from the rotation poles of g11.04).
**Datasets.** shared geo and region tables.

**Weekend problem --- "India's journey".** I palaeolatitudes and speeds;
II the slowdown at collision; III convergence absorbed by shortening; IV the
crust thickened.
**Named final number:** *the distance India has travelled north since the
end of the Cretaceous, several thousand kilometres (from the sourced
latitudes).*

---

### g12.03 `metamorphic-rocks` --- Metamorphic Rocks

**Hook.** The same mud can become a slate roof, a glittering garnet schist
or a banded gneiss, depending on how deep it was buried.

**Sections.**
1. *Transformed in the solid state* --- metamorphism; pressure,
   temperature, fluids; lithostatic pressure (**derived** as the weight of
   the overlying column: P = ρgz; about 1 GPa at 35 km).
2. *Index minerals and grade* --- polymorphs (kyanite, andalusite,
   sillimanite); the P--T diagram (computed); index minerals and isograds;
   metamorphic grade.
3. *Foliation* --- slate, schist, gneiss with rising grade; foliation forms
   across the direction of shortening.
4. *Contact and regional metamorphism* --- the aureole around a pluton; whole
   belts in mountain ranges; the cold path of subduction zones (blueschist
   and eclogite recalled); three geotherms on one diagram.

**Definitions.** metamorphism (`def:g12:metamorphic-rocks:metamorphism`);
lithostatic pressure (`...:lithostatic`); polymorph (`...:polymorph`);
index mineral, isograd, metamorphic grade (`...:index-mineral`); foliation,
schistosity (`...:foliation`); contact metamorphism, regional metamorphism,
aureole (`...:contact-regional`).
**Statements.** prop. lithostatic pressure (derived); method: reading a P--T
diagram; example: the kyanite--sillimanite transition.
**Recall.** blueschist, eclogite (\cref{ch:g11:subduction-zones});
geotherm (\cref{ch:g11:lithosphere-asthenosphere}); minerals
(\cref{ch:g11:minerals}); rock cycle, marble, slate (Book 1, grade 6);
pressure (physics).

**Figures.** F `al2sio5` (P--T diagram of the three polymorphs with a
subduction, a mountain-belt and a contact geotherm; tested: triple point at
the source's values); S a Barrovian sequence of zones; S foliation forming
under shortening (platy minerals rotating); S contact aureole around a pluton
(schematic, not the Varden granite); P slate, mica schist with garnet,
gneiss, marble (candidates: USGS PD or Commons CC).

**Ledger.** Al2SiO5 triple point and reaction slopes (Holdaway 1971 or
Pattison 1992, DOI); crustal density for the pressure (reuse g11.03 row);
Barrow 1893 (history, DOI).
**Datasets.** none.

**Weekend problem --- "The history of a kyanite schist".** I the minerals
and the polymorph; II reading the pressure and temperature; III the burial
depth; IV the geotherm it implies, and how it came back up.
**Named final number:** *the depth at which the kyanite schist formed, about
25 km.*

---

### g12.04 `subduction-magmatism` --- Magmatism at Subduction Zones

**Hook.** 18 May 1980: the north flank of Mount St. Helens slides away and a
column of ash rises 24 km (USGS photographs).

**Sections.**
1. *Volcanic arcs* --- a line of volcanoes above the slab at about 100 km;
   the Pacific Ring of Fire (computed map).
2. *Water melts the mantle* --- the slab dehydrates; water lowers the
   mantle's melting temperature by hundreds of degrees (computed solidi);
   hydrous melting in the wedge.
3. *Andesites and granodiorites* --- arc magmas are richer in silica and
   water: explosive eruptions (viscosity and gas recalled from Book 1,
   grade 7); granodiorite and batholiths.
4. *How continents grow* --- arcs add new crust; rates (sourced); collisions
   weld arcs to continents.

**Definitions.** volcanic arc (`def:g12:subduction-magmatism:arc`); hydrous
melting (`...:hydrous-melting`); granodiorite (`...:granodiorite`);
batholith (`...:batholith`); continental growth
(`...:continental-growth`).
**Statements.** prop. the slab depth beneath arcs (computed from the
catalogue); method: finding the slab under a volcano; example: Japan.
**Recall.** subduction, slab, eclogite (\cref{ch:g11:subduction-zones});
partial melting (\cref{ch:g11:ocean-ridges}); andesite, rock names
(\cref{ch:g11:igneous-rocks}); continental crust
(\cref{ch:g12:continental-crust}); explosive eruptions (Book 1, grade 7).

**Figures.** F `wet_dry_solidus` (dry and water-saturated peridotite solidi
with a wedge geotherm; tested: the wet solidus lies several hundred degrees
lower at 3 GPa as the source says); S an arc section (slab dehydration,
melting wedge, rising magma, plutons and volcanoes); F `arc_slab_depth`
(earthquakes and volcanoes across north-east Japan; tested: the slab lies
80--130 km below the volcanic front); F the Ring of Fire (shared volcano and
subduction tables); P Mount St. Helens 1980 (candidate: USGS, PD); P a
granodiorite batholith landscape (candidate: Half Dome, NPS PD); P andesite
(candidate, USGS).

**Ledger.** Mount St. Helens 1980 facts (USGS); slab depths beneath arcs
(Syracuse and Abers 2006, G³, DOI); dry and wet solidi (Grove et al. 2006
or another DOI source); arc crust growth rates (Clift et al. 2009, DOI);
granodiorite composition (a fetched source).
**Datasets.** shared catalogue and volcanoes.

**Weekend problem --- "Beneath the volcanoes of Japan".** I the volcanic
front on the map; II the earthquake section; III the slab's depth and dip;
IV where the water comes from.
**Named final number:** *the depth of the slab beneath the volcanic front,
about 100 km.*

---

### g12.05 `destruction-of-mountains` --- The Destruction of Mountains

**Hook.** The Appalachians and the Scottish Highlands were once as high as
the Alps; today they are rounded hills (NASA images). The Varden Hills'
schist and granite are the roots of such a range.

**Sections.**
1. *Weathering and erosion attack relief* --- recalled (Book 1, grade 5;
   \cref{ch:g10:soil-formation}); denudation rates rise with relief and
   rainfall (sourced compilation).
2. *Transport* --- bedload, suspended and dissolved loads; the great rivers'
   sediment fluxes.
3. *Sedimentation and diagenesis* --- detrital rocks; compaction and
   cementation; the sedimentary basin recalled.
4. *Isostatic rebound* --- erosion unloads, the root rises: removing 1 km
   lowers the surface by only about 180 m (**derived** from Airy); deep
   rocks reach the surface (metamorphic rocks exposed); glacial rebound as
   a measured analogue.
5. *The crust recycled* --- the rock cycle at plate scale; relief decays
   exponentially (computed, grade-12 exp); the Varden unconformity read as
   an old range eroded flat before the Triassic.

**Definitions.** denudation rate (`def:g12:destruction-of-mountains:
denudation`); sediment load (bedload, suspended load, dissolved load)
(`...:load`); isostatic rebound (`...:rebound`); detrital rock, diagenesis
(`...:diagenesis`).
**Statements.** prop. rebound fraction (derived: Δh = ρc/ρm × erosion); prop.
exponential decay of relief (derived from a rate proportional to elevation,
grade-12 derivative); method: an erosion budget; example: the Ganges.
**Recall.** weathering, erosion, deposition (Book 1, grade 5); landforms,
uplift--erosion balance (Book 1, grade 9); hydrolysis, clays
(\cref{ch:g10:soil-formation}); discharge (\cref{ch:g10:drainage-basins});
isostasy (\cref{ch:g11:lithosphere-asthenosphere}); root
(\cref{ch:g12:continental-crust}); sedimentary basin
(\cref{ch:g11:fossil-fuel-geology}); metamorphism
(\cref{ch:g12:metamorphic-rocks}).

**Figures.** S erosion and rebound in three steps; F `relief_decay` (mean
elevation against time, with and without rebound; tested: e-folding time
equals the model's); F the Varden section with the unconformity (shared
region tables); bar chart of river sediment loads (ledger coordinates);
P a river's sediment plume (candidate: NASA, PD); P old ranges from orbit
(candidate: Appalachian ridges, NASA PD); P a conglomerate (candidate,
USGS); AI a braided river in a mountain valley.

**Ledger.** denudation rates (Portenga and Bierman 2011, GSA Today, DOI);
river sediment fluxes (Milliman and Farnsworth 2011 or Milliman and Syvitski
1992, DOI); glacial rebound rates (a DOI geodetic study); densities (reuse
g11.03).
**Datasets.** shared region tables.

**Weekend problem --- "How long to flatten a mountain range?".** I the
erosion rate; II without rebound; III with rebound (the factor); IV the
exponential law and its time constant.
**Named final number:** *the half-life of the range's mean elevation, in
millions of years (computed).*

---

### g12.06 `internal-heat` --- The Earth's Internal Heat

**Hook.** At the bottom of the deepest gold mines, 4 km down, the rock is
hot enough to burn the skin.

**Sections.**
1. *Gradient and heat flow* --- the geotherm recalled; heat flow
   q = k × gradient (the rock's thermal conductivity k used, not defined:
   the physics books); units; continental and oceanic means; the total.
2. *Where the heat comes from* --- radiogenic heat production (uranium,
   thorium, potassium; radioactivity recalled from the physics books);
   granite against peridotite; secular cooling; geoneutrinos measure the
   radiogenic part; more heat in the past (computed, exp).
3. *Conduction and convection* --- conduction too slow to empty the mantle
   (time scale computed); mantle convection; plates and slabs as its upper
   part; plumes told.
4. *Geothermal energy* --- hot reservoirs near volcanoes and ridges, warm
   aquifers elsewhere (physical description only).

**Definitions.** heat flow (`def:g12:internal-heat:heat-flow`); radiogenic
heat production (`...:heat-production`); secular cooling
(`...:secular-cooling`); thermal convection, mantle convection
(`...:convection`); geothermal energy (`...:geothermal`).
**Statements.** prop. Fourier's law in its simplest form (admitted, physics
Year 2); prop. the decline of radiogenic heat (derived from the decay law,
exp); method: a heat budget; example: a borehole.
**Recall.** geotherm, gradient (\cref{ch:g11:lithosphere-asthenosphere});
radioactivity, half-life, decay law (physics); heat conductors (physics);
convection cells in the air (Book 1, grade 8).

**Figures.** F `heat_production` (radiogenic heat against time back to
4.5 Ga by isotope; tested: ratios from the decay law); F heat flow against
seafloor age with the continental mean (published law; tested); S the heat
budget (bars: radiogenic, secular cooling, totals); S mantle convection
(plates, slabs, plumes); P a geothermal power plant (candidate: Iceland,
Commons CC); P Larderello (candidate, Commons CC); AI a steaming hot spring
in a snowy landscape.

**Ledger.** global heat flow and means (Davies and Davies 2010, Solid Earth,
DOI); geoneutrino radiogenic heat (KamLAND 2011, Nature Geoscience, DOI);
heat production of rocks (a DOI compilation); half-lives of U-238, U-235,
Th-232, K-40 (NNDC or LNHB; check Book 3's ledger first); deep-mine rock
temperatures (a fetched source); heat flow versus age (Stein and Stein 1992,
Nature, DOI).
**Datasets.** none.

**Weekend problem --- "The Earth's heat budget".** I heat flow and areas;
II the total; III radiogenic heat from the geoneutrinos; IV the rest,
secular cooling.
**Named final number:** *the share of the Earth's heat loss supplied by
radioactivity today, about 40 %.*

---

### g12.07 `age-of-the-earth` --- Radiometric Dating and the Age of the Earth

**Hook.** 1862: William Thomson, later Lord Kelvin, computes from cooling
that the Earth is at most a few hundred million years old; the geologists
need more. The answer came from a source of heat he did not know.

**Sections.**
1. *A history of estimates* --- Buffon's cooling balls, sediment piles,
   Kelvin's cooling, Joly's salt; what each assumed (method box); radioactivity
   ends the debate (timeline computed from ledger rows).
2. *The decay law, recalled* --- the physics books' law and the dating
   equation; the closed system; relative dating recalled (Book 1, grade 7).
3. *The isochron* --- **derived**: present ratio = initial ratio + parent
   ratio × (e^{λt} − 1), a straight line; slope gives the age; the Varden
   granite dated.
4. *The age of the Earth* --- meteorites, the lead--lead isochron, 4.55 Ga
   (Patterson 1956); the oldest solids 4.567 Ga; the oldest terrestrial
   minerals recalled (\cref{ch:g12:continental-crust}).

**Definitions.** closed system (`def:g12:age-of-the-earth:closed-system`);
isochron (`...:isochron`); age of the Earth (`...:age`).
**Statements.** thm. the isochron equation (derived from the decay law,
grade-12 exp); prop. age from the slope (t = ln(1 + slope)/λ); method:
dating a rock with an isochron; example: the Varden granite; history boxes:
Kelvin; Holmes; Patterson.
**Recall.** isotopes, half-life, decay law, the dating equation (physics);
superposition, cross-cutting, eras (Book 1, grade 7).

**Figures.** F `isochron` (Rb--Sr isochron of the Varden granite, data
computed for 310 Ma, consistent with `figdata/shared/region.py`; tested:
slope gives 310 Ma; also Patterson's meteorite lead points with their
isochron; tested: 4.55 Ga); F the estimates of the Earth's age against the
year they were made (log scale; ledger values); S closed and open systems;
P Kelvin (candidate, Commons PD); P an iron meteorite (candidate: Canyon
Diablo, Commons CC); AI a mass-spectrometer laboratory (inthelab box).

**Ledger.** the ⁸⁷Rb decay constant (Villa et al. 2015, GCA, DOI);
Patterson 1956 (GCA, DOI) data and age; historical estimates (Dalrymple
2001, GSL Special Publication, DOI; USGS page); oldest solids (Connelly et
al. 2012, Science, DOI; shared ics:base.Hadean); Varden granite 310 Ma
(region model, no row: exercise data).
**Datasets.** none.

**Weekend problem --- "Dating the Varden granite".** I the samples and their
ratios; II the isochron line; III the slope and the age; IV the initial
ratio and what it says about the source.
**Named final number:** *the age of the Varden granite, 310 million years.*

---

### g12.08 `early-earth` --- The Early Earth and Its Atmosphere

**Hook.** In north-western Australia, cliffs of rock striped red and black
like a layer cake: iron rusted in a sea 2.5 billion years ago (photograph).

**Sections.**
1. *The young Earth* --- accretion, the Moon-forming impact (told), a magma
   ocean, cooling; zircons 4.4 Ga old point to early liquid water.
2. *The primitive atmosphere* --- outgassing; carbon dioxide, nitrogen,
   water vapour, no free oxygen; the faint young Sun (luminosity computed)
   and its problem; a stronger greenhouse as the answer.
3. *Life and oxygen* --- stromatolites; oxygen-producing photosynthesis
   (biology recalled).
4. *The rise of oxygen* --- the Great Oxidation Event; banded iron
   formations (\ce balanced oxidation of dissolved iron); red beds; what
   disappears from the rocks (told).

**Definitions.** outgassing, primitive atmosphere (`def:g12:early-earth:
primitive-atmosphere`); faint young Sun problem (`...:faint-young-sun`);
stromatolite (`...:stromatolite`); Great Oxidation Event (`...:goe`); banded
iron formation (`...:bif`); red beds (`...:red-beds`).
**Statements.** prop. the young Sun's luminosity (admitted law, computed);
prop. iron oxidation removes oxygen (balanced equation); method: reading a
geological timeline.
**Recall.** age of the Earth (\cref{ch:g12:age-of-the-earth}); zircons
(\cref{ch:g12:continental-crust}); equilibrium temperature
(\cref{ch:g10:habitable-planet}); photosynthesis, cyanobacteria (biology);
air composition, greenhouse gases, redox (chemistry).

**Figures.** F `young_sun` (luminosity and equilibrium temperature against
time; tested: about 70 % at 4.57 Ga); F timeline of the early Earth (eon
colours from the ICS rows; events from the ledger); S oxygen through time
(schematic with the sourced bounds); S how a banded iron formation forms;
P a banded iron formation (candidate, Commons CC); P stromatolites at Shark
Bay (candidate, Commons CC); P red beds (candidate: NPS/USGS PD).

**Ledger.** the young Sun's luminosity law (Gough 1981, Solar Physics,
DOI); GOE timing (a DOI review, e.g. Lyons et al. 2014; Gumsley et al.
2017); oldest stromatolites (a DOI source); BIF ages (Bekker et al. 2010,
DOI); volcanic gas composition (USGS); Archean oxygen bound (Farquhar et al.
2000 / Pavlov and Kasting 2002, DOI); zircon ages (reuse g12.01 rows).
**Datasets.** none.

**Weekend problem --- "The faint young Sun".** I the Sun's luminosity 4 Ga
ago; II the young Earth's equilibrium temperature; III evidence of liquid
water; IV the greenhouse warming needed.
**Named final number:** *the equilibrium temperature of the Earth four
billion years ago, about 235 K.*

---

### g12.09 `past-climates` --- Reading Past Climates

**Hook.** At Dome C, in Antarctica, a drill brings up ice from 3 km down;
its bubbles hold air 800 000 years old.

**Sections.**
1. *Archives and proxies* --- ice, ocean sediments, pollen, corals, tree
   rings, cave deposits (told); definitions.
2. *Ice cores* --- bubbles keep the air; the isotopes of the ice measure the
   temperature (told; δ values are not defined here); 800 000 years of
   temperature and carbon dioxide together (computed); glacial cycles; the
   Last Glacial Maximum (sea level, temperature, the exposed shelves mapped).
3. *Pollen* --- pollen analysis; reading a pollen diagram (invented exercise
   data, labelled as such).
4. *Ocean sediments and the astronomical rhythm* --- foraminifera and the
   five-million-year record (computed); cooling and the change from 41 000-
   to 100 000-year cycles; astronomical cycles told (Year 2 owns them).
5. *Climates of deep time* --- warm and cold periods of the past (sourced
   reference values); a bridge to \cref{ch:g12:climate-change}.

**Definitions.** climate archive, proxy (`def:g12:past-climates:proxy`);
ice core (`...:ice-core`); glacial period, interglacial, glacial cycle
(`...:glacial-cycle`); pollen analysis (`...:pollen`); Last Glacial Maximum
(`...:lgm`).
**Statements.** prop. temperature and CO2 vary together over 800 000 years
(computed correlation); method: reading a pollen diagram; method: reading a
proxy record; example: the last deglaciation.
**Recall.** glacier, ice sheet, ice age (Book 1, grade 8); past climates
first look (Book 1, grade 9); isotopes (physics); greenhouse gases
(chemistry); ICS periods (Book 1, grade 7).

**Figures.** F `ice_age_records` (EPICA temperature and Antarctic CO2 on
one time axis, 800 kyr; tested: correlation above 0.8, glacial--interglacial
amplitudes); F LR04 over 5.3 Myr (same script; tested: later mean heavier
than earlier); F the exposed shelves at the Last Glacial Maximum (ETOPO1
regional window, coastline at today's level and at the sourced lowstand;
tested: land area increase); a pollen diagram (invented exercise data);
deep-time reference periods (ledger coordinates); P an ice core section
(candidate: NSF/NOAA, PD); P foraminifera (candidate: NOAA or Commons);
P pollen grains (candidate: Dartmouth SEM, Commons PD); AI an ice-coring camp
on a flat ice sheet.

**Ledger.** EDC, Bereiter, LR04 (shared datasets); LGM sea level and
temperature (AR6 WG1 ch. 2 or 9; Lambeck et al. 2014, DOI; Tierney et al.
2020, DOI); astronomical periods (Hays, Imbrie and Shackleton 1976, DOI);
AR6 palaeoclimate reference periods (AR6 WG1 ch. 2 table); rate comparison
statement (AR6 SPM A.2).
**Datasets.** shared.

**Weekend problem --- "800 000 years of Antarctic ice".** I reading the two
curves; II glacial and interglacial values; III the last deglaciation, its
duration and rate; IV today's rate compared.
**Named final number:** *today's global warming is about twenty times faster
than the warming out of the last ice age (ratio computed from sourced
values).*

---

### g12.10 `climate-change` --- Climate Change: Observations, Causes and Projections

Pilot, written and approved (2026-10-22). Keep. Phase C: full FIGCHECK pass
again after the term links; scripted solutions re-read; fix only defects
found. Recall box already points to \cref{ch:g10:earth-energy-budget} (albedo)
and \cref{ch:g12:past-climates}: both labels will exist.

---

## Contested and cross-book points (for the sync)

1. **P wave, S wave** --- physics owns the seismic waves in the cross-series
   table (g12 `mechanical-waves`) but its harvest defines no "P wave" or
   "S wave" term (it mentions them); its g12 chapter comes a year after
   g11 `seismic-structure`. Case: g11 defines them as the two body waves of
   an earthquake by arrival order and the media they cross, and recalls the
   wave mechanics from the physics books.
2. **exoplanet** --- not in any map; Book 1 g6 `earth-a-planet` may mention
   planets of other stars. Case: g10 `habitable-planet` is the outline's
   "planets of other stars (first look)"; Book 1 uses the plain words.
3. **chemical weathering** --- Book 1 g5 owns "weathering". Case: g5 keeps
   weathering (and, if it wants, a mechanical/chemical split as plain
   words); g10 defines chemical weathering with hydrolysis and clays.
4. **adiabatic cooling, dry adiabatic rate** --- Book 1 g8 owns the fall of
   temperature with height (environmental lapse). Case: g10 owns the
   adiabatic rates.
5. **normal fault; reverse fault, thrust** --- Book 1 g7 owns "fault". If
   Book 1 defines fault types, g11/g12 recall them; otherwise g11
   `ocean-ridges` owns normal fault and g12 `mountain-building` reverse
   fault and thrust.
6. **convection** --- Book 1 g8 likely defines convection (descriptive
   cells). Case: g12 `internal-heat` defines thermal convection only if
   Book 1 does not; it owns mantle convection in any case.
7. **denudation rate** --- Y1 `erosion-transport` re-founds g5; g12
   `destruction-of-mountains` needs the quantity. Case: g12 owns it in the
   school books unless Book 1 g5 defines it.
8. **detrital rock, diagenesis** --- Book 1 g7 says sediments harden into
   rock. Case: g12 owns the terms; g7 keeps the plain description.
9. **silicate** --- chemistry b1 owns silicate units (a later year). Case:
   g11 `minerals` defines the silicate mineral and the tetrahedron from the
   Earth angle.
10. **hardness, Mohs scale** --- Book 1 g6 uses scratch hardness. Case: g11
    owns the Mohs scale unless Book 1 g6 defines it.
11. **humidity** --- biology g6 defines humidity (everyday sense); the map
    gives humidity to g10. Book 2 defines saturation and relative humidity.
12. **equilibrium temperature** --- physics b2 owns the black body and the
    effective temperature; g10 defines the planet's equilibrium temperature
    with the formula admitted.
13. **δ¹⁸O** --- chemistry b3 owns the δ value; Y2 owns δ notation. g12
    `past-climates` reads isotope curves as told, without a definition.
14. **lithostatic pressure** --- Y1 owns stress; g12 defines lithostatic
    pressure at school level.
15. **sedimentary basin** --- Y1 owns basin types; g11 `fossil-fuel-geology`
    defines the basin at school level.
16. **latent heat** --- no sister series defines it (checked); claimed by
    g10 `earth-energy-budget`; Book 1 g8 may want it for clouds --- it is
    grade 10 material.
