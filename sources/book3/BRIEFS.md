# BRIEFS --- Book 3 (University Year 1, `bachelor-1`, prefix `b1`)

Phase A plan, written 2026-10-22 by the Book 3 agent. One brief per chapter, in
outline order: sections; definitions (term, label, owner check); recall boxes;
planned figures tagged **[S]** schematic (TikZ/pgfplots typed), **[F]** figdata
(tested script), **[AI]** AI illustration, **[P]** photograph; ledger needs;
datasets; the weekend problem's story and its named final number.

Conventions for every chapter (binding on this book):

- University register: each law is a `theorem`/`proposition` with a derivation
  at Year-1 mathematics (derivatives, integrals, first-order linear ODEs,
  vectors with dot and cross products, spherical trigonometry from ch. 1, mean /
  standard deviation / least-squares line); otherwise `\admitted` plus a prose
  pointer ("derived in the physics books' Year 2 volume", "the Year 3 volume").
- Labels `<type>:b1:<slug>:<name>`. Terms only in the owner chapter, inside a
  `definition`, as `\emph{}\index{}`. Never a bare homograph as a defined term
  (see "Homographs" at the end): `apparent magnitude`, never `magnitude`;
  `extinction angle`, never `extinction`; `volcanic arc`, never `arc`.
- Calibration: 12 exercises (4★, 5★★, 3★★★), weekend problem 22--28
  questions in Parts I--IV ending on a **named number**; ~12 pp per chapter
  including solutions (pilot ch. 4: ~14 pp).
- Ledger ids are `<source-family>:<topic-name>` (e.g. `usgs:tohoku-2011-mw`,
  `simbad:sirius-v`); grep `sources/data_ledger.md sources/ledger/` before
  minting. Shared rows (earth:, planet:, sun:, const:, ics:, data:) are cited,
  never duplicated.
- Exercise maps/sections: the Varden Hills only (`figdata/shared/region.py`,
  imported, never edited).
- Observation only; climate physical science only; no curriculum names (gate 7
  also rejects the words *French*/*France*: no French place is named).

---

## Ch. 1 Spherical Astronomy --- `spherical-astronomy`

**Hook.** On a clear night the stars wheel round one fixed point; a star rises
four minutes earlier each night; the noon Sun climbs higher in June. Three
numbers --- a latitude, a date, an hour --- fix where every star stands.

**Sections.**
1. Triangles on a sphere: great and small circles; the spherical triangle;
   cosine rule (theorem, proof with the dot product of unit vectors); sine
   rule (theorem, proof with the triple product); great-circle distance
   (method; flight route example).
2. Coordinates on the sphere: geographic coordinates re-founded; the celestial
   sphere; horizontal coordinates (altitude, azimuth); equatorial coordinates
   (declination, right ascension, hour angle); the astronomical triangle
   pole--zenith--star: $\sin h = \sin\varphi\sin\delta + \cos\varphi\cos\delta\cos H$
   (proposition, from the cosine rule); altitude of the pole = latitude.
3. Time: sidereal time (LST = RA + H); sidereal vs solar day (proposition: the
   difference is one day per year, derived); apparent and mean solar time; the
   equation of time (told, ledger amplitude); time zones recalled.
4. Rising, setting and the Sun: hour angle of rising $\cos H_0 = -\tan\varphi\tan\delta$
   (proposition); circumpolar stars; day length; the ecliptic and the Sun's
   declination $\sin\delta = \sin\varepsilon\sin\lambda$; instantaneous insolation at the top of
   the atmosphere $I = S_0 (a/r)^2\cos\theta_z$; polar day and night.
5. Calendars: the tropical year; Julian and Gregorian rules; the mean Gregorian
   year 365.2425 d and its drift (proposition); `history` box: the 1582 reform.

**Definitions** (owner: this chapter, per OUTLINE Y1 map "spherical
trigonometry, celestial coordinates, sidereal time"):
- great circle, small circle, spherical triangle --- `def:b1:spherical-astronomy:spherical-triangle`
- latitude, longitude (re-founds g6 `latitude-longitude`) --- `def:b1:spherical-astronomy:geographic`
- celestial sphere, celestial pole, celestial equator, zenith, local meridian --- `def:b1:spherical-astronomy:celestial-sphere`
- altitude (of a star), azimuth --- `def:b1:spherical-astronomy:horizontal`
- declination (celestial), right ascension, hour angle --- `def:b1:spherical-astronomy:equatorial`
- ecliptic, obliquity of the ecliptic, vernal equinox point --- `def:b1:spherical-astronomy:ecliptic`
- sidereal time --- `def:b1:spherical-astronomy:sidereal-time`
- apparent solar time, mean solar time, equation of time --- `def:b1:spherical-astronomy:solar-time`
- circumpolar star --- `def:b1:spherical-astronomy:circumpolar`
- insolation --- `def:b1:spherical-astronomy:insolation` (used again in ch. 27)
- tropical year --- `def:b1:spherical-astronomy:tropical-year`

**Recall.** Physics: the seasons and their cause (physics g3/g6); Kepler's laws
and the sidereal day (physics g12 `satellites-kepler`); spherical coordinates
(physics b1 `point-kinematics`); stars and constellations (physics g5). Book 1
grade 6: latitude, longitude, time zones. Math: dot and cross products.

**Figures.** [S] a spherical triangle on a sphere with its sides and angles
(tdplot); [S] the celestial sphere at latitude 45° N (`celestialsphere` pic)
with a star's altitude, azimuth, declination and hour angle; [F]
`sun_paths.py`: the Sun's altitude against azimuth at 45° N at both solstices
and the equinox (test: noon altitude $90° - \varphi + \delta$; equinox rising
at azimuth 90°); [F] `day_length.py`: day length against date at 0, 30, 45,
60, 70° N (test: 12 h at the equinoxes; 24 h at 70° N in June; symmetry
$\varphi \to -\varphi$, date + half a year); [P] star trails round the
celestial pole (ESO or NASA, CC BY / PD); [AI] a navigator's sextant beside a
folded star chart on a chart table (generic, no readable text).

**Ledger.** shared `earth:obliquity`, `earth:Trot`, `earth:Ptrop`,
`earth:Psid`, `earth:ecc`, `earth:TSI`; equation-of-time extremes (+16 min
early November, −14 min mid-February; NOAA/USNO); the Gregorian reform date
(papal bull 1582); Paranal Observatory latitude/longitude (ESO); Sirius RA and
Dec J2000 (SIMBAD); one or two city coordinates for the great-circle example.

**Problem.** *A night at a mountain observatory* (Paranal, 24.6° S). Part I
the great-circle distance and initial heading from the observatory to a
city; Part II Sirius's culmination altitude, circumpolar test for Canopus;
Part III the local sidereal time when Sirius transits, and the clock time
that night; Part IV the Sun at the June solstice: rising hour angle, sunrise
azimuth, day length. Named number: **the length of the longest night of the
year at the observatory** (h min, computed).

---

## Ch. 2 Telescopes, Detectors and Photometry --- `observing-the-sky`

**Hook.** From a dark site the eye sees a few thousand stars; a 2.4-m space
telescope sees galaxies thirty magnitudes fainter; X-ray telescopes work only
above the air.

**Sections.**
1. The atmosphere's windows: absorption by ozone, water vapour and carbon
   dioxide; optical and radio windows; atmospheric extinction: Bouguer's law
   derived from $\mathrm dI = -\kappa I\,\mathrm ds$ (first-order ODE), airmass
   $X = \sec z$ for a plane-parallel atmosphere (proposition); the extinction
   line $m = m_0 + kX$ (method); seeing.
2. Telescopes and resolution (recall physics b1 `optical-instruments`):
   collecting area; diffraction limit $1.22\lambda/D$ recalled; seeing limit;
   adaptive optics told.
3. Detectors: photon detectors, quantum efficiency; the CCD principle; photon
   noise and the signal-to-noise ratio $\propto\sqrt{t}$ (proposition; the
   Poisson standard deviation $\sqrt N$ admitted).
4. Fluxes and magnitudes: flux and luminosity, the inverse-square law
   (proposition, from energy conservation over a sphere); apparent magnitude
   (Pogson); parallax and the parsec; absolute magnitude and distance modulus
   $m - M = 5\log_{10}(d/10\,\mathrm{pc})$ (derived); photometric bands and
   colour index; colour and temperature (Planck recalled, admitted).
5. Spectrographs: dispersing light (grating recalled from physics); spectral
   resolving power recalled; what a spectrum gives (composition, temperature,
   radial velocity --- pointer to the Year 3 volume).
6. Observing from space: what needs space and why; `dated` box: Hubble, JWST,
   Gaia (mirror sizes, orbits).

**Definitions** (owner: this chapter, OUTLINE "magnitudes, photometry,
telescopes" --- telescopes themselves recalled from physics):
- atmospheric window --- `def:b1:observing-the-sky:window`
- airmass, atmospheric extinction coefficient --- `def:b1:observing-the-sky:extinction`
- seeing --- `def:b1:observing-the-sky:seeing`
- quantum efficiency, signal-to-noise ratio --- `def:b1:observing-the-sky:detector`
- flux (of a source), luminosity --- `def:b1:observing-the-sky:flux` (contested: see report)
- apparent magnitude, photometric band --- `def:b1:observing-the-sky:magnitude`
- parallax (annual), parsec --- `def:b1:observing-the-sky:parallax` (contested with Y3 `milky-way-galaxies`, "distance ladder")
- absolute magnitude, distance modulus --- `def:b1:observing-the-sky:absolute`
- colour index --- `def:b1:observing-the-sky:colour-index`

**Recall.** Physics b1 `optical-instruments` (telescope, angular resolution,
Rayleigh criterion); physics g10 `light-spectra`, b2 `gratings` (spectra,
grating resolving power); physics b2 `thermal-radiation` (black body, Wien,
Stefan--Boltzmann: admitted, pointer); physics g8 light-year; chemistry
absorbance (Beer--Lambert) as the same law.

**Figures.** [S] atmospheric transmission against wavelength, windows shaded
(boundaries from the ledger); [F] `blackbody_bands.py`: Planck curves of the
Sun (5772 K) and a 10 000 K star normalised, with U, B, V, R band centres
(test: Wien peak at $b/T$; the ratio B/V flux rises with T); [F]
`extinction_line.py`: an extinction line from exercise data (test:
least-squares slope = k); [S] light path telescope → spectrograph → detector;
[P] a large ground observatory (ESO VLT, CC BY 4.0) and [P] the JWST primary
mirror (NASA, PD); [AI] an observatory dome opening at dusk (no readable sky).

**Ledger.** Sun $T_\mathrm{eff}$ 5772 K (IAU 2015 B3); Sun apparent
magnitude −26.74 (NASA Sun fact sheet), shared `sun:Mabs`, `sun:L`; Sirius V
magnitude and parallax (SIMBAD); Vega V ≈ 0.03 (SIMBAD); Hubble 2.4 m, JWST
6.5 m (NASA); typical median seeing at a major site (ESO); atmospheric window
limits (a NASA or ESA page); Pogson 1856 (history).

**Problem.** *Weighing the light of Sirius.* Part I parallax → distance;
Part II flux ratio Sirius/Vega/Sun from magnitudes; Part III absolute
magnitude and luminosity in solar units; Part IV exposure time for a given
SNR with a 1-m telescope (photon rate estimate given). Named number:
**Sirius's luminosity in suns (V band)** (≈ 23, computed).

---

## Ch. 3 Comparative Planetology --- `comparative-planetology`

**Hook.** Venus and the Earth are nearly twins in size and mass; one has
oceans and plate tectonics, the other a 90-bar carbon-dioxide atmosphere and a
surface hotter than a kitchen oven.

**Sections.**
1. Masses, radii, densities: a planet's mass from a moon's orbit (Kepler III
   recalled, method); mean density; the moment-of-inertia factor and what it
   says about concentration (0.4 for a uniform sphere, recalled from physics).
2. Bulk composition: terrestrial planets (rock and iron), gas giants
   (hydrogen and helium), ice giants (water, ammonia, methane ices); a
   two-layer model: core radius from mean density and the moment of inertia
   (proposition, derived).
3. Atmospheres and surfaces: Bond albedo; equilibrium temperature
   $T_\mathrm{eq} = [S(1-A)/4\sigma]^{1/4}$ (proposition; Stefan--Boltzmann
   admitted from physics); greenhouse warming as $T_\mathrm{surf} - T_\mathrm{eq}$
   (Venus, Earth, Mars); surface pressures; surfaces: craters, volcanoes,
   tectonics (plates only on the Earth).
4. Moons and small bodies: the Moon, Io, Europa, Titan; asteroids, comets,
   trans-Neptunian objects; meteorites as samples (classes: Year 2 volume).

**Definitions:**
- terrestrial planet, giant planet, gas giant, ice giant (re-found g6 `earth-a-planet` "rocky and giant planets") --- `def:b1:comparative-planetology:planet-types`
- moment-of-inertia factor --- `def:b1:comparative-planetology:moi`
- Bond albedo (re-founds g10 `earth-energy-budget` "albedo"; see report) --- `def:b1:comparative-planetology:albedo`
- equilibrium temperature --- `def:b1:comparative-planetology:equilibrium-temperature`
- asteroid, comet, trans-Neptunian object --- `def:b1:comparative-planetology:small-bodies` (contested: physics g4 `solar-system` may teach them unindexed)

**Recall.** Physics g4 `solar-system` (planet, Solar System); physics b1
`central-forces` (Kepler, eccentricity), moment of inertia (physics b1); black
body (physics b2); Book 1 g6 `earth-a-planet`; Book 2 g10 `habitable-planet`.

**Figures.** [F] `planet_table.py`: density against radius (log) for the
eight planets, Moon, Pluto, from the shared `planet:` rows (test: every
plotted value equals its ledger row, parsed from `data_ledger.md`); [F] same
script: equilibrium vs mean surface temperature bars (test: Earth $T_\mathrm{eq}$
= 254 K = `earth:Tbb` within 1 K); [S] interiors to scale (Earth, Mars,
Jupiter, Neptune; layer radii from the ledger); [P] NASA montage (PD): Venus
(Magellan radar), Earth (Blue Marble), Mars, Jupiter, Saturn (Cassini),
Neptune (Voyager 2); [P] Titan's surface or Europa (NASA, PD).

**Ledger.** shared `planet:*` (mass, diameter, density, gravity, Tmean,
psurf, dist), `earth:MoI`; Mars and Moon moment-of-inertia factors (NASA fact
sheets); Phobos orbit (NASA Mars satellite sheet); Mars core radius from
InSight (Stähler et al. 2021, via NASA/JPL or the paper); Jupiter helium mass
fraction (Galileo probe, von Zahn et al. 1998); albedos (NASA fact sheets).

**Problem.** *Weighing and sounding Mars.* Part I Mars's mass from Phobos's
orbit; Part II density, comparison with the Earth; Part III a two-layer model
with the moment-of-inertia factor → core radius; Part IV equilibrium
temperature vs measured mean. Named number: **the radius of Mars's core**
(≈ 1800 km from the model, compared with the InSight value).

---

## Ch. 4 Geological Maps --- `geological-maps` (PILOT, approved; keep)

Written and approved 2026-10-22. Definitions: `def:b1:geological-maps:geological-map`
(geological map, contact (geological), map unit, outcrop), `:dem` (digital
elevation model), `:attitude` (strike, dip, dip direction, attitude),
`:fold` (fold, anticline, syncline, fold axis; Sync 0). Notation
`not:b1:geological-maps:rhr` (right-hand rule, not indexed).

**Phase B work on it (my files only):**
1. The open layout item: the weekend problem's unbreakable data table is
   pushed to the next page leaving ~⅓ page blank (pilot build p. 20). Fix:
   put the table and the map side by side, or move the table out of the
   first lines of the problem box after a short paragraph; re-render the page
   at 130 dpi; FIGCHECK line.
2. Q17 asks for "the trend and the plunge" before those words are defined
   (ch. 6 owns them): add a one-clause gloss in the question.
3. Q18 extrapolates "8 km farther north", beyond the 8-km map: harmless but
   odd; keep unless the user objects (answer stays −50 m).
4. Re-run its term links in Phase C (they are already wrapped).

---

## Ch. 5 Cross-Sections --- `cross-sections`

**Hook.** A tunnel is to be driven under the Varden Hills: which rocks will it
cross, where will it meet the fault, and how much limestone must it bore?

**Sections.**
1. From map to section: the topographic profile; projecting contacts; vertical
   exaggeration (method: constructing a section).
2. Apparent dip: $\tan\beta = \tan\delta\cos\gamma$ (theorem, from the plane
   equation of ch. 4); the effect of vertical exaggeration
   $\tan\beta' = e\tan\beta$ (proposition).
3. Thickness: true and vertical thickness; thickness from outcrop width and
   slope (proposition, derived); apparent thickness in a vertical borehole
   $t = h\cos\delta$.
4. Boreholes: the borehole log; correlation; structure contours and the
   structure-contour map (method; recall the three-point problem).
5. From section to history: unconformities in section; fault throw and heave;
   restoring a fault offset; `history` box: Hutton's unconformity at Siccar
   Point (1788).

**Definitions:**
- geological cross-section, topographic profile, vertical exaggeration --- `def:b1:cross-sections:section`
- apparent dip --- `def:b1:cross-sections:apparent-dip`
- true thickness, vertical thickness --- `def:b1:cross-sections:thickness`
- borehole log, correlation (of logs) --- `def:b1:cross-sections:log`
- structure contour, structure-contour map --- `def:b1:cross-sections:structure-contour`
- unconformity, angular unconformity, disconformity --- `def:b1:cross-sections:unconformity` (not in any map; ch. 4 uses the word in its recall/proposition --- earliest Y1 definition here)
- fault throw, heave --- `def:b1:cross-sections:throw`

**Recall.** Ch. 4 (plane equation, three-point theorem, V-rule); Book 1 g9
(contours, scale); Book 1 g7 (relative dating principles).

**Figures.** [F] `varden_sections.py` (imports `region.py`): section A--B from
the shared tables and a new east--west section C--D at y = 6 km across the
fold, with vertical exaggeration ×2 and ×1 (tests: the dips in section equal
the apparent dips of the theorem; contacts agree with `region.unit`); [S] the
construction of a section from a map (projection lines); [S] apparent dip in a
block diagram; [S] thickness geometry (true, vertical, outcrop width, slope);
[F] same script: three borehole logs correlated (test: contact depths =
model); [P] Siccar Point (Commons, CC, verify); [AI] an engineer's drawing
table with a tunnel profile in progress (no readable text).

**Ledger.** Hutton 1788 (*Theory of the Earth*, Trans. R. Soc. Edinburgh) and
Siccar Point; photo credit.

**Problem.** *A tunnel under the Varden Hills.* Part I the profile and the
units along the tunnel line; Part II apparent dips of the limbs in the
section; Part III true and along-tunnel thickness of the limestone; Part IV
where the tunnel meets the fault, throw and heave. Named number: **the length
of limestone the tunnel bores through** (m, from `varden_sections.py`).

---

## Ch. 6 Field and Lab Methods I --- `field-lab-methods-1`

**Hook.** A mapping day: a notebook, a satellite receiver, a
compass-clinometer and a hand lens; that evening, rock chips leave for the
thin-section laboratory.

**Sections.**
1. The field notebook and the map: stations, sketches, sample numbers;
   positions from satellite receivers and their accuracy.
2. Measuring orientations: planes (strike/dip, dip direction/dip) and lines
   (trend and plunge); the magnetic declination correction (magnetic
   declination recalled from physics g11); repeated measurements: mean,
   standard deviation; the vector mean of orientations (proposition: the mean
   of unit normals; derived).
3. The hand lens and field identification (lustre, cleavage, hardness, grain
   size, the dilute-acid test on carbonates by professionals).
4. Sampling: representative and oriented samples, labelling, chain of custody.
5. Thin sections and the polarising microscope (`inthelab`): cutting,
   grinding to 30 µm, mounting; the microscope (polariser, analyser, rotating
   stage, accessory slot); plane-polarised light and crossed polars (the
   optics: ch. 8).
6. Safety (`safety` box): professional field and laboratory safety.

**Definitions:**
- field station, field notebook --- `def:b1:field-lab-methods-1:station`
- trend, plunge --- `def:b1:field-lab-methods-1:trend-plunge` (ch. 4 uses them; gloss there)
- (magnetic declination is physics' notion: recalled, never defined here)
- oriented sample --- `def:b1:field-lab-methods-1:sample`
- thin section --- `def:b1:field-lab-methods-1:thin-section`
- polarising microscope, plane-polarised light, crossed polars --- `def:b1:field-lab-methods-1:microscope`
- mean orientation (vector mean) --- `def:b1:field-lab-methods-1:mean-orientation`

**Recall.** Ch. 4 (attitude, right-hand rule); physics g11 magnetic
declination; Book 2 g11 `minerals` (field properties); math: mean, standard
deviation.

**Figures.** [S] the compass-clinometer laid along strike and down dip (two
panels); [F] `attitude_stats.py`: 25 seeded synthetic readings of the Varden
east-limb bedding (noise σ = 3°), histogram of dip directions and of dips with
mean ± sd (test: the vector mean is within 1° of 081/12; the printed means and
sd equal those computed); [S] light path of a polarising microscope; [P]
compass-clinometer (Commons, CC, verify), polarising microscope (Commons, CC),
a thin section slide (Commons); [AI] a geologist writing in a notebook on a
grassy hillside (no readable page); [AI] a technician at a thin-section
grinding wheel.

**Ledger.** standard thickness of a petrographic thin section, 30 µm (a
published lab manual or USGS); consumer satellite-receiver accuracy (GPS.gov
performance page); a `dated` magnetic declination value for one place (NOAA
WMM calculator, year stated).

**Problem.** *A field season on the Varden east limb.* Part I a table of 12
bedding readings → mean dip direction and dip by the vector mean; Part II
standard deviations; Part III the declination correction of a raw compass
set; Part IV comparison with the three-point attitude of ch. 4, and how many
readings halve the uncertainty of the mean. Named number: **the mean attitude
of the east limb** (dip direction/dip, computed: ≈ 081/12).

---

## Ch. 7 Rock-Forming Minerals --- `rock-forming-minerals`

**Hook.** A granite worktop shows three or four kinds of grain; a beach sand is
almost all quartz; the green crystals in a basalt are olivine.

**Sections.**
1. What a mineral is: definition re-founded; crystal lattices, unit cells and
   coordination recalled from chemistry; polymorphs (graphite--diamond,
   calcite--aragonite, quartz--coesite, the Al₂SiO₅ trio named only).
2. The silicate tetrahedron and its linkages: recall the SiO₄ unit
   (chemistry b1); classes by polymerisation; the Si:O ratio of each class
   (proposition, by counting shared oxygens).
3. Ionic substitution and solid solutions: the substitution rules (radius
   within ~15 %, charge); coupled substitution (NaSi ⇌ CaAl in plagioclase);
   end-members; olivine Fo--Fa, plagioclase Ab--An; properties linear in
   composition between end-members (proposition for molar volume / density of
   an ideal mixture, derived).
4. Mineral formulas: the structural formula; recalculation of an analysis in
   oxide weight per cent on a fixed number of oxygens (method, worked olivine
   example); site occupancy; Mg number.
5. The main rock-forming minerals: olivine, garnet, pyroxenes, amphiboles,
   micas, feldspars, quartz, carbonates, iron oxides; formula, structure class,
   density, hardness, cleavage, where they occur (table; clays in ch. 19).

**Definitions:**
- mineral (re-founds g6 `rocks-and-minerals` / g11 `minerals`) --- `def:b1:rock-forming-minerals:mineral`
- polymorph --- `def:b1:rock-forming-minerals:polymorph`
- nesosilicate, sorosilicate, cyclosilicate, inosilicate, phyllosilicate, tectosilicate --- `def:b1:rock-forming-minerals:silicate-classes`
- ionic substitution, coupled substitution --- `def:b1:rock-forming-minerals:substitution`
- solid solution, end-member (OUTLINE owner; contested with chemistry b2) --- `def:b1:rock-forming-minerals:solid-solution`
- structural formula, Mg number --- `def:b1:rock-forming-minerals:formula`
- olivine, garnet, pyroxene, amphibole, mica, feldspar, plagioclase, alkali feldspar --- `def:b1:rock-forming-minerals:groups`

**Recall.** Chemistry b1 `crystals-*` (lattice, unit cell, coordination
number, tetrahedral site), b1 `periodicity` (ionic radius), b1 `p-block-13-15`
(silicate units); Book 2 g11 `minerals` (habit, cleavage, hardness, lustre,
the six silicates); molar mass and the mole (chemistry).

**Figures.** [S] the SiO₄ tetrahedron and six linkage classes (six small
panels); [S] coupled substitution in plagioclase (site diagram); [F]
`solid_solution.py`: density and molar volume of olivine against forsterite
content (test: end-points equal the ledger densities; linearity of molar
volume); [P] six mineral specimens (Commons, CC BY / BY-SA, verify each:
olivine, plagioclase, quartz, biotite, garnet, hornblende); [P] calcite
cleavage rhomb (Commons).

**Ledger.** densities, hardness and formulas of the end-members and main
minerals (RRUFF / Mindat / webmineral, consensus value); ionic radii in their
coordination (Shannon 1976 via the Imperial College database); molar masses
(IUPAC standard atomic weights).

**Problem.** *An olivine from a basalt.* Part I oxide analysis → cations on
4 oxygens; Part II the structural formula and the charge check; Part III
forsterite content and Mg number; Part IV density by interpolation and the
mass of olivine in a cubic metre of the rock (modal % given). Named number:
**the forsterite content of the olivine** (Fo, %, computed).

---

## Ch. 8 Optical Mineralogy --- `optical-mineralogy`

**Hook.** Between crossed polars a thin section of gabbro lights up like
stained glass: quartz grey, olivine vivid, plagioclase striped.

**Sections.**
1. Light in crystals (recall physics refractive index and linear
   polarisation): isotropic and anisotropic minerals; the optic axis, uniaxial
   and biaxial minerals (the indicatrix told).
2. Observations in plane-polarised light: colour and pleochroism; relief
   (proposition: relief grows with $|n - n_\mathrm{mount}|$) and the Becke line
   (method); cleavage and habit.
3. Crossed polars: retardation $\Delta = d\,(n_1 - n_2)$ (proposition, from
   the phase difference); transmitted intensity
   $I = I_0\sin^2 2\theta\,\sin^2(\pi\Delta/\lambda)$ (theorem, derived by
   projecting the field vector onto the two vibration directions and then onto
   the analyser); extinction positions; interference colours in white light
   and their orders; the Michel-Lévy chart computed; the first-order red
   accessory plate.
4. Identifying minerals in thin section: a method (PPL then XPL);
   extinction angle; twinning (plagioclase polysynthetic twins); key
   minerals table.

**Definitions:**
- isotropic mineral, anisotropic mineral --- `def:b1:optical-mineralogy:anisotropic`
- optic axis, uniaxial, biaxial --- `def:b1:optical-mineralogy:optic-axis`
- pleochroism --- `def:b1:optical-mineralogy:pleochroism`
- relief, Becke line --- `def:b1:optical-mineralogy:relief`
- birefringence (of a mineral) (OUTLINE owner; contested with physics b2) --- `def:b1:optical-mineralogy:birefringence`
- retardation (in a crystal plate) --- `def:b1:optical-mineralogy:retardation`
- extinction position, extinction angle --- `def:b1:optical-mineralogy:extinction`
- interference colour, order (of an interference colour), Michel-Lévy chart --- `def:b1:optical-mineralogy:interference-colour`
- twin, polysynthetic twinning --- `def:b1:optical-mineralogy:twin`

**Recall.** Ch. 6 (thin section, polarising microscope, PPL, crossed polars);
physics b1 `rays-reflection-refraction` (refractive index), physics b2
`plane-waves-polarization` (linear polarisation, wave plates; birefringence
treated there in its Year 2 volume), physics `light-as-wave` (path difference,
interference), Malus's law.

**Figures.** [S] light through a crystal plate between polariser and analyser
(vectors of the two vibration directions); [F] `michel_levy.py`: interference
colours computed from the CIE 1931 colour-matching functions and the sRGB
transform, 0--1800 nm, with birefringence lines for d = 30 µm (tests: Δ = 0 is
black; the first-order red near 550 nm has its green channel at a minimum;
colours repeat with decreasing saturation by order); [S]
$I(\theta)$ for a stage rotation (pgfplots of the formula); [P] PPL/XPL pairs
of thin sections (Commons, CC, verify: granite, olivine basalt or gabbro); [P]
Auguste Michel-Lévy (PD, history box); [AI] a student at a polarising
microscope.

**Ledger.** refractive indices and birefringence of quartz, calcite, olivine
(Fo90), plagioclase, biotite, muscovite, garnet (Mindat/webmineral, consensus);
mounting medium index ≈ 1.54; Michel-Lévy and Lacroix 1888 (history); CIE 1931
CMF (dataset); the sRGB matrix and gamma (IEC 61966-2-1 via an open
specification page).

**Dataset.** `bachelor-1-cie1931.csv`: CIE 1931 2° colour-matching functions,
360--830 nm (CIE, CC BY-SA 4.0, DOI 10.25039/CIE.DS.xvudnb9b; ~15 KB). To add
in a `# Book 3:` block of `tools/fetch_data.py`; URL verified in Phase B.

**Problem.** *Identifying the minerals of an unknown thin section.* Part I
relief and pleochroism observations; Part II measuring retardation from the
colour order of quartz → the real section thickness; Part III birefringence
of an unknown mineral from its highest colour; Part IV extinction angle and
twinning → the mineral. Named number: **the real thickness of the section**
(µm, computed from quartz).

---

## Ch. 9 The Layered Earth --- `layered-earth`

**Hook.** In 1909 Andrija Mohorovičić noticed two sets of P waves on the
seismograms of a Croatian earthquake; a century of such records gives today's
reference Earth.

**Sections.**
1. Seismic velocities with depth: P and S waves recalled (physics g12; their
   speeds from the elastic moduli admitted, physics b3); travel-time curves;
   refraction at a layer boundary: head waves and the crossover distance
   (theorem, two-layer, Snell recalled); method: the depth of the Moho.
2. A reference Earth model: PREM; the discontinuities (Moho, 410, 660, CMB
   2891 km, ICB); liquid outer core, solid inner core; `history`: Lehmann 1936.
3. Density from seismic data: the Adams--Williamson equation
   $\mathrm d\rho/\mathrm dr = -\rho g/\Phi$, $\Phi = v_P^2 - \tfrac43 v_S^2$
   (theorem, derived from hydrostatics and adiabatic compression); mass and
   moment of inertia as constraints (proposition: integrals); $g(r)$ and $P(r)$
   computed from PREM.
4. Mantle mineralogy with depth: peridotite of the upper mantle; olivine →
   wadsleyite (410) → ringwoodite (520) → bridgmanite + ferropericlase (660);
   the transition zone; D″ told; Clapeyron slopes and discontinuity topography
   (pointer to the Year 2 volume).
5. The core: iron--nickel plus light elements (density deficit, told with
   ledger); inner-core growth told.
6. Mechanical layers: lithosphere and asthenosphere re-founded (the
   low-velocity zone; strength told, ch. 16).

**Definitions:**
- crust, mantle, outer core, inner core (re-found g6 `inside-the-earth`) --- `def:b1:layered-earth:layers`
- seismic discontinuity, Mohorovičić discontinuity (Moho), core--mantle boundary, inner-core boundary (re-found g11 `seismic-structure`) --- `def:b1:layered-earth:discontinuity`
- head wave, crossover distance --- `def:b1:layered-earth:head-wave`
- reference Earth model (OUTLINE owner) --- `def:b1:layered-earth:reference-model`
- seismic parameter --- `def:b1:layered-earth:seismic-parameter`
- mantle transition zone (OUTLINE "mantle phase transitions") --- `def:b1:layered-earth:transition-zone`
- lithosphere, asthenosphere, low-velocity zone (re-found g11 `lithosphere-asthenosphere`; see report: the OUTLINE puts that row's re-founding in ch. 11) --- `def:b1:layered-earth:lithosphere`

**Recall.** Physics g12 `mechanical-waves` (P and S waves), physics b3
`continuum-elasticity` (velocities from moduli), Snell's law (physics b1),
hydrostatic relation (physics b1 `fluid-statics`), gravitation (physics);
Book 2 g11 `seismic-structure` (travel times, shadow zones, Moho).

**Figures.** [F] `prem_profiles.py`: $v_P$, $v_S$, ρ against depth (test: CMB
at 2891 km; $v_S = 0$ in the outer core; ICB at 5149.5 km); [F] same script:
$g(r)$, $P(r)$, enclosed mass (tests: total mass within 0.5 % of `earth:mass`;
$I/MR^2$ within 0.002 of `earth:MoI`; central pressure within 1 % of the PREM
paper's value); [F] `refraction.py`: two-layer travel-time lines (test:
crossover distance equals the theorem); [S] ray paths of direct and head waves
over a crust/mantle model; [S] mantle mineralogy with depth (volume fractions
of a pyrolite mantle, sourced, schematic); [P] Inge Lehmann and Andrija
Mohorovičić (PD, verify); [AI] a seismometer vault (generic).

**Ledger.** `data:prem`; PREM central pressure and discontinuity depths
(Dziewonski & Anderson 1981); Mohorovičić 1909, Lehmann 1936 (history); depths
and minerals of the mantle phase changes (an open review); core density deficit
(open source); continental crust mean thickness (CRUST1.0 or a review).

**Problem.** *Weighing the Earth's shells with PREM.* Part I layer volumes;
Part II layer masses from rounded mean densities; Part III moment of inertia
of the layered model vs the measured factor; Part IV gravity at the CMB and
pressure at the centre from a two-layer integral. Named number: **the
fraction of the Earth's mass in the core** (%, ≈ 32.5).

---

## Ch. 10 The Earth's Heat Budget --- `heat-budget`

**Hook.** At the bottom of the deepest gold mines, some 4 km down, the rock is
hot enough to burn a hand; the whole planet leaks about 47 terawatts.

**Sections.**
1. Heat sources: radiogenic heat production of U, Th, K and of rocks; secular
   cooling and the core; the global budget; geoneutrinos told.
2. Measuring heat flow: Fourier's law recalled (physics b2, admitted);
   gradient × conductivity in boreholes; marine probes; continental and oceanic
   averages (method).
3. The steady conductive geotherm: the energy balance of a slab gives
   $k\,T'' + A = 0$ (derived); uniform production in a layer (proposition);
   exponential production $A_0 e^{-z/D}$ → the linear heat-flow--heat-production
   relation $q_0 = q_m + A_0 D$ (theorem); the temperature at the Moho.
4. Convection versus conduction: the conductive time scale $L^2/\kappa$ against
   the age of the Earth (proposition, κ recalled); the mantle adiabat and the
   mantle's potential temperature (told; the notion of potential temperature
   is defined in ch. 26); mantle convection recalled (Book 2 g12).
5. The lithosphere as a thermal boundary layer: thermal lithosphere; oceanic
   heat flow decreasing with age (told; ch. 13 and the Year 3 volume).

**Definitions:**
- heat flow (surface heat-flow density) (re-found g12 `internal-heat`) --- `def:b1:heat-budget:heat-flow`
- radiogenic heat production --- `def:b1:heat-budget:heat-production`
- geotherm (re-found g11; OUTLINE row "conductive geotherm with heat production") --- `def:b1:heat-budget:geotherm`
- secular cooling --- `def:b1:heat-budget:secular-cooling`
- mantle adiabat --- `def:b1:heat-budget:adiabat`
- thermal boundary layer, thermal lithosphere --- `def:b1:heat-budget:boundary-layer`

**Recall.** Physics b2 `heat-conduction` (Fourier's law, conductivity,
diffusivity, heat equation: admitted, pointer); radioactive decay (physics
g12); Book 2 g12 `internal-heat` (heat flow, mantle convection); ch. 9
(lithosphere).

**Figures.** [F] `geotherms.py`: continental geotherms for three surface heat
flows with exponential heat production, and an oceanic one (tests: surface
gradient = $q_0/k$; the analytic profile equals a numerical integration of
$kT'' = -A$; $q_0 - q_m = A_0D$); [S] a bar chart of the global heat budget
(ledger values, typed with `% ledger:`); [S] heat-flow measurement in a
borehole and with a marine probe; [S] the thermal boundary layer over a
convecting mantle (cross-section); [AI] a marine heat-flow probe lowered from a
research vessel.

**Ledger.** global heat loss 47 ± 2 TW and continental/oceanic means (Davies &
Davies 2010, Solid Earth, open); heat production per kg of U, Th, K and typical
A of granite, basalt, peridotite (Hasterok et al. 2018, open, or an equivalent
open compilation); conductivity of granite (open source); geoneutrino
radiogenic estimate (KamLAND 2011, arXiv version); deepest mine depth and rock
temperature (mine operator or a peer-reviewed source); mantle potential
temperature and adiabatic gradient (open review); the D of the linear relation
(~10 km; Lachenbruch 1968/Roy et al. 1968, AGU free archive).

**Problem.** *Hot rocks under the plutons.* Part I heat flow from borehole
gradients; Part II five plutons: $q_0$ against $A_0$, least-squares line →
$D$ and $q_m$; Part III the geotherm under one pluton; Part IV the temperature
at the Moho (35 km) and the depth of the 1300 °C isotherm. Named number:
**the temperature at the Moho beneath the plutons** (°C, computed).

---

## Ch. 11 Isostasy and Gravity Anomalies --- `isostasy-gravity`

**Hook.** In the 1840s the Himalaya deflected the surveyors' plumb lines less
than their mass should have: the mountains were "compensated" (Pratt and Airy,
1855).

**Sections.**
1. Gravity and its measurement: normal gravity on the reference ellipsoid
   (formula admitted, coefficients in the ledger; the ellipsoid itself is the
   Year 3 volume's); units (mGal); absolute and relative gravimeters.
2. Isostasy: compensation depth; Airy (root $r = h\rho_c/(\rho_m - \rho_c)$,
   proposition derived) and Pratt models (proposition); the Earth's bimodal
   hypsometry as evidence (computed).
3. Gravity anomalies: the free-air gradient $2g/R$ (derived from $g = GM/r^2$);
   the Bouguer slab $2\pi G\rho h$ (derived by integrating rings); free-air and
   Bouguer anomalies; anomalies over compensated and uncompensated relief
   (proposition, method).
4. The geoid: an equipotential (physics' potential recalled); geoid height and
   its first-order relation to the potential anomaly (proposition); the marine
   geoid maps the seafloor; isostatic rebound after ice loss (told; viscosity:
   Year 3).

**Definitions:**
- normal gravity (contested lightly with Y3 `gravity-geodesy`, which owns the ellipsoid and J₂) --- `def:b1:isostasy-gravity:normal-gravity`
- isostasy, compensation depth (re-found g11 `lithosphere-asthenosphere`) --- `def:b1:isostasy-gravity:isostasy`
- Airy isostasy, Pratt isostasy --- indexed in `prop:b1:isostasy-gravity:airy`, `prop:b1:isostasy-gravity:pratt` (SERIES rule 5)
- gravity anomaly, free-air correction, free-air anomaly, Bouguer correction, Bouguer anomaly (OUTLINE owner) --- `def:b1:isostasy-gravity:anomalies`
- geoid, geoid height (OUTLINE owner) --- `def:b1:isostasy-gravity:geoid`
- hypsometric curve --- `def:b1:isostasy-gravity:hypsometry`

**Recall.** Physics gravitation, gravitational field and potential (physics
g9/g10/b1); Archimedes and hydrostatics (physics b1 `fluid-statics`); ch. 9
(lithosphere, asthenosphere, densities); Book 2 g11 (isostasy, Airy, first
look).

**Figures.** [F] `hypsometry.py`: the Earth's hypsometric curve and elevation
histogram from ETOPO1 at 1° with cos-latitude weights (tests: fraction below
sea level within 0.01 of the ledger ocean fraction; area weights sum to
$4\pi R^2$); [S] Airy and Pratt columns with computed roots; [F]
`gravity_profiles.py`: free-air and Bouguer anomalies over a 2D model range,
uncompensated and Airy-compensated, by numerical integration of 2D line masses
(tests: the far-field Bouguer anomaly over a broad compensated block tends to
$-2\pi G\Delta\rho\,r$; the Bouguer slab constant 0.0419 mGal per metre per
1000 kg/m³); [S] geoid, ellipsoid and topography; [P] a field gravimeter or
the GOCE satellite (USGS PD / ESA CC BY-SA IGO, verify); [AI] a gravity survey
team with a tripod instrument in farmland.

**Ledger.** GRS80 normal gravity constants (NGA/Moritz 2000 open text);
standard Bouguer density 2670 kg/m³ (source); ocean area fraction (NOAA or a
peer-reviewed hypsometry); Pratt 1855 and Airy 1855 (Phil. Trans., history);
geoid extremes (EGM2008 / GOCE source); post-glacial uplift rate of a shield
(e.g. Fennoscandia, open source).

**Problem.** *The root of a mountain range.* Part I a 4-km plateau: Airy root
and crustal thickness; Part II Pratt alternative; Part III free-air and
Bouguer anomalies over the centre and their meaning; Part IV erode 1 km and
let isostasy act: rock uplift and net lowering. Named number: **the net
lowering of the surface for 1 km of rock eroded** (m, ≈ 180).

---

## Ch. 12 Plate Kinematics on a Sphere --- `plate-kinematics`

**Hook.** A satellite-positioning station in Iceland and another in Norway
draw apart by about two centimetres a year; the same rate is written in the
seafloor's magnetic stripes over ten million years.

**Sections.**
1. Rigid plates on a sphere: rigid plates re-founded; Euler's rotation theorem
   (stated, partial proof via the fixed point of a rotation); the Euler pole and
   the angular velocity vector.
2. Relative velocities: $\vec v = \vec\omega\times\vec r$ (theorem); speed
   $\omega R\sin\Delta$ (proposition; Δ from ch. 1's cosine rule) and azimuth;
   transforms lie on small circles about the pole (proposition); method:
   velocity at a point.
3. Combining motions, triple junctions: $\vec\omega_{AC} = \vec\omega_{AB} +
   \vec\omega_{BC}$ (proposition); velocity triangles; triple junction types
   and stability (RRR always stable; told for the others).
4. Finite rotations: rotation about an axis (matrix, Rodrigues' formula
   derived with dot and cross products); reconstructing the South Atlantic;
   non-commutativity.
5. Measuring motions: magnetic anomalies and the polarity timescale (reversals
   recalled from Book 2 g11); half and full spreading rates from anomaly
   distance and age (method); satellite geodesy and agreement with geological
   rates.

**Definitions:**
- rigid plate (re-found g11 `plate-motions`) --- `def:b1:plate-kinematics:rigid-plate`
- Euler pole, Euler vector (OUTLINE owner) --- `def:b1:plate-kinematics:euler-pole`
- triple junction, stable triple junction (OUTLINE owner) --- `def:b1:plate-kinematics:triple-junction`
- finite rotation --- `def:b1:plate-kinematics:finite-rotation`
- marine magnetic anomaly, polarity chron, geomagnetic polarity timescale --- `def:b1:plate-kinematics:magnetic-anomaly`
- half spreading rate, full spreading rate --- `def:b1:plate-kinematics:spreading-rate`

**Recall.** Ch. 1 (spherical trigonometry, great and small circles); physics
b1 angular velocity; Book 2 g11 `drift-to-spreading` (reversals, stripes),
`plate-motions` (rigid plates, rates); Book 1 g7 (plates).

**Figures.** [S] Euler pole geometry: small circles and velocity growing away
from the pole (tdplot); [F] `euler_velocities.py`: relative velocities along
the Mid-Atlantic Ridge from a published Euler vector, against the PB2002 step
velocities (tests: $|v| = \omega R\sin\Delta$; zero at the pole; mean
difference with PB2002 below 15 %); [F] `south_atlantic_fit.py`: South
America's coastline rotated onto Africa by a published finite rotation (tests:
the matrix is orthogonal with determinant 1; the pole is fixed; a point moves
along a small circle); [F] `gpts_stripes.py`: the polarity timescale 0--10 Ma
and the striped seafloor it makes at two spreading rates (test: block widths =
rate × duration); [S] velocity triangles for a ridge--ridge--ridge junction;
[P] a permanent GNSS station (USGS/NASA PD, verify).

**Ledger.** Euler vectors (ITRF2014 plate motion model, Altamimi et al. 2017,
GJI open access; or MORVEL, DeMets et al. 2010); a South America--Africa
finite rotation (Bullard et al. 1965 or a modern reconstruction); polarity
chron boundaries 0--10 Ma (Cande & Kent 1995, AGU free archive, or the
current GPTS); GNSS velocities of two Icelandic/Norwegian stations (JPL or NGL
time-series pages); Morgan/McKenzie--Parker 1967--68 (history).

**Problem.** *Iceland splits.* Part I the North America--Eurasia Euler vector
→ the spreading rate and azimuth at Reykjanes; Part II the anomaly 5 distance
and age → geological rate; Part III two GNSS stations → geodetic rate;
Part IV a finite rotation of 10 Myr, and the Azores triple junction's velocity
triangle. Named number: **the full spreading rate across Iceland** (mm/yr,
≈ 19, three ways).

---

## Ch. 13 Rifts, Ridges and Passive Margins --- `rifts-ridges-margins`

**Hook.** In Afar the ground opened by metres in 2005; in Iceland one can stand
in a valley that widens every year; the Atlantic began as such a rift.

**Sections.**
1. Continental rifting: normal faults, grabens, half-grabens; volcanic and
   magma-poor rifts; the East African Rift (stretching quantified: Year 2
   volume).
2. Break-up and passive margins: thinned crust, tilted blocks, the break-up
   unconformity, seaward-dipping reflectors, the ocean--continent transition,
   subsidence.
3. Ocean ridges, fast and slow: axial valley vs axial high; spreading-rate
   classes; the oceanic crust (pillow lavas, sheeted dykes, gabbro, mantle
   peridotite; Book 2 g11 recalled, ophiolites named only).
4. The depth--age law: $d(t) = d_r + C\sqrt t$ (theorem: isostasy + a cooling
   profile admitted from the Year 3 volume gives the √t subsidence); constants
   from data; flattening of old seafloor (told).
5. Transform faults and fracture zones: active segment and inactive scar; sense
   of slip opposite to the apparent offset (proposition); transforms on small
   circles (ch. 12).

**Definitions:**
- continental rift, graben, half-graben --- `def:b1:rifts-ridges-margins:rift`
- passive margin, ocean--continent transition, break-up unconformity (OUTLINE owner; re-found g11 `ocean-ridges`) --- `def:b1:rifts-ridges-margins:passive-margin`
- fast-spreading ridge, slow-spreading ridge, ultraslow-spreading ridge --- `def:b1:rifts-ridges-margins:ridge-classes`
- oceanic crust, pillow lava, sheeted dyke complex --- `def:b1:rifts-ridges-margins:oceanic-crust`
- depth--age law (OUTLINE owner) --- indexed in `thm:b1:rifts-ridges-margins:depth-age`
- transform fault, fracture zone (re-found g7 "transform boundary") --- `def:b1:rifts-ridges-margins:transform`

**Recall.** Ch. 10 (thermal boundary layer), ch. 11 (isostasy), ch. 12
(spreading rates, small circles); Book 2 g11 `ocean-ridges`; normal faults
(Book 1 g7; geometry in ch. 17).

**Figures.** [F] `depth_age.py`: the √t law with sourced constants against an
ETOPO1 1° profile across the South Atlantic ridge, ages from distance / half
rate (tests: $d(0) = d_r$; the formula at 25 and 100 Ma; profile symmetry
within tolerance); [S] rift → break-up → passive margin (three sections); [S]
fast vs slow ridge axial profiles and an oceanic crust column (`lith basalt`,
gabbro, peridotite fills); [S] ridge--transform--fracture zone in map view
with `dextral`/`sinistral` pics; [P] the East African Rift or Afar from space
(NASA PD), Þingvellir (Commons CC, verify), pillow lavas on the seafloor (NOAA
PD); [AI] a research vessel deploying an instrument at sea.

**Ledger.** depth--age constants (Parsons & Sclater 1977, AGU free archive);
ridge axis depth; spreading-rate class limits (Dick et al. 2003 or an open
review); oceanic crust thickness (White et al. 1992, AGU free archive); Afar
2005 dyking event (USGS or peer-reviewed open source); South Atlantic half
rate (PB2002 steps, computed).

**Problem.** *The birth of an ocean.* Part I a rift's normal faults and
extension; Part II the Red Sea's spreading rate from an anomaly; Part III time
to reach the Atlantic's width; Part IV depth of the new seafloor with age and
the subsidence of its margins. Named number: **the depth of 80-million-year-old
seafloor** (km, computed from the law).

---

## Ch. 14 Active Margins --- `active-margins`

**Hook.** On 11 March 2011 the seafloor off north-east Japan lurched tens of
metres; behind the coast stands a chain of volcanoes 100 km above the sinking
plate.

**Sections.**
1. Morphology: trench, forearc, volcanic arc, back-arc; the deepest trench.
2. Gravity and heat flow: the paired anomaly (trench low, arc high); low
   forearc heat flow, high arc and back-arc heat flow, and why (the cold slab;
   ch. 10 recalled).
3. Seismicity and slab geometry: the Wadati--Benioff zone from the catalogue;
   slab dip by least squares; earthquakes to 700 km.
4. Accretionary and erosive margins: accretionary prisms (offscraping,
   underplating); tectonic erosion.
5. Volcanic arcs: the arc front above the slab at ~100 km depth; the
   arc--trench gap $h/\tan\alpha$ (proposition); flux melting recalled (Book 2
   g12; Year 2 volume); back-arc basins.

**Definitions:**
- active margin, oceanic trench, forearc, back-arc basin (re-found g8 trench, g11 `subduction-zones`) --- `def:b1:active-margins:active-margin`
- subducting slab (re-found g11 "subduction"; see report) --- `def:b1:active-margins:slab`
- Wadati--Benioff zone --- `def:b1:active-margins:wadati-benioff`
- accretionary prism, tectonic erosion --- `def:b1:active-margins:accretionary`
- volcanic arc, arc--trench gap --- `def:b1:active-margins:volcanic-arc`

**Recall.** Book 2 g11 `subduction-zones`, g12 `subduction-magmatism`; ch. 10,
11, 12; Book 1 g7 (earthquakes).

**Figures.** [F] `slab_seismicity.py`: hypocentres projected on a profile
across the Tonga (or NE Japan / central Chile) margin from the USGS catalogue,
with a least-squares slab line (tests: the great-circle projection of a point
on the profile line is exact; the fitted dip on synthetic points recovers the
input dip); [S] a subduction-zone cross-section (prism, forearc, arc, back-arc,
slab, isotherms bending down with the slab, the 100-km slab contour); [S]
gravity and heat-flow profiles across a margin (amplitudes from the ledger);
[F] `margins_map.py`: the western Pacific from `shared-geo-*` (subduction teeth
on the overriding plate, volcanoes); [P] an arc volcano (USGS AVO PD, verify);
[AI] a tsunami-warning operations room (generic, no readable screens).

**Ledger.** Tohoku 2011 Mw and slip (USGS); Challenger Deep depth (NOAA or
peer-reviewed survey); depth of the slab beneath arc fronts (England et al.
2004 or Syracuse & Abers 2006, open); maximum earthquake depth (USGS); forearc
and arc heat-flow ranges (open source); convergence rates (PB2002, computed).

**Dataset.** possibly `bachelor-1-usgs-<region>.csv`: USGS ComCat M ≥ 5,
1976--2025, one box (PD, ~0.5 MB), if M ≥ 6 events are too few for a clean
slab (decided in Phase B; appended to `fetch_data.py` as a Book 3 block).

**Problem.** *Reading a subduction zone from its earthquakes.* Part I a table
of hypocentres (rounded from the catalogue) → least-squares slab dip; Part II
the slab's depth under the arc → arc--trench gap; Part III convergence rate ×
time → length of slab subducted in 10 Myr; Part IV heat-flow and gravity
profile reading. Named number: **the arc--trench gap predicted by the slab**
(km, computed and compared with the map).

---

## Ch. 15 Hotspots and Intraplate Volcanism --- `hotspots`

**Hook.** Kīlauea erupts in the middle of the Pacific plate, thousands of
kilometres from any plate boundary; north-west of it, the islands grow older
one by one.

**Sections.**
1. Hotspots and mantle plumes: hotspot re-founded; the plume hypothesis
   (Morgan 1971); swells; imaging told (Year 3 volume).
2. Hotspot tracks and plate motion: age progression; rates by least squares;
   the Hawaiian--Emperor bend; hotspots as a reference frame and their own
   motion (told).
3. Large igneous provinces: definition, areas, volumes, durations (Deccan,
   Siberian Traps, CAMP, Ontong Java); coincidences with mass extinctions
   (recalled from biology).
4. Intraplate volcanism without plumes (told): cracks, edge-driven convection;
   oceanic islands' later life (Year 2 volume).

**Definitions:**
- hotspot (re-found g7 `volcanoes`) --- `def:b1:hotspots:hotspot`
- mantle plume --- `def:b1:hotspots:plume`
- hotspot track, age progression --- `def:b1:hotspots:track`
- large igneous province --- `def:b1:hotspots:lip`

**Recall.** Ch. 12 (Euler vectors), ch. 11 (isostasy, swells); Book 1 g7
(hotspot first look); biology (mass extinctions).

**Figures.** [F] `hawaii_track.py`: age against distance from Kīlauea for
dated volcanoes, two least-squares lines (Hawaiian, Emperor) (tests: the fit
recovers a synthetic rate; slopes and bend age as printed); [F]
`hotspots_map.py`: world map (shared land) with hotspots and LIP centroids
from ledger coordinates; [S] plume head and tail under a moving plate → a
chain; [P] Kīlauea lava (USGS HVO PD), Deccan Traps (Commons CC, verify).

**Ledger.** ages and positions of Hawaiian--Emperor volcanoes (Clague &
Dalrymple 1987, USGS PD; O'Connor et al. 2013, AGU free); bend age; LIP areas,
volumes, ages (Coffin & Eldholm 1994, AGU free archive; Burgess & Bowring
2015, open); Morgan 1971 (history).

**Problem.** *The Pacific plate's speedometer.* Part I distances and ages →
Hawaiian rate; Part II Emperor rate and bend angle; Part III the Pacific Euler
vector's magnitude from the rate and the distance to the pole (ch. 12);
Part IV volume of a shield volcano and the plume's magma supply. Named number:
**the Pacific plate's speed over Hawaii** (cm/yr, computed).

---

## Ch. 16 Stress, Strain and Rheology --- `stress-strain-rheology`

**Hook.** A granite column carries a cathedral for centuries; a glacier of
crystalline ice flows; a fault holds for a century then slips in seconds.

**Sections.**
1. Stress in two dimensions: traction on a plane; normal and shear stress;
   the transformation formulas from the equilibrium of a triangular prism
   (derived); principal stresses (theorem: where $\mathrm d\sigma_n/\mathrm d\theta = 0$
   the shear stress vanishes and the directions are perpendicular); the Mohr
   circle (proposition); lithostatic stress $\rho g z$; differential stress.
2. Strain: extension, stretch, shear strain; homogeneous strain as a linear
   map; the strain ellipse; pure and simple shear (rotational vs not);
   finite and infinitesimal strain.
3. Rheology: elastic (Hooke recalled, physics); viscous (viscosity recalled,
   physics b2); brittle failure: the Coulomb criterion and the failure angle
   $45° - \phi/2$ (theorem, from the Mohr circle); Byerlee's law (proposition,
   ledger); ductile creep (power law admitted; flow laws: Year 3).
4. The strength envelope of the lithosphere: brittle strength growing with
   depth (Byerlee, hydrostatic pore pressure), ductile strength falling with
   temperature (geotherm of ch. 10); the brittle--ductile transition;
   seismogenic depth; oceanic vs continental envelopes; competing models told.

**Definitions** (OUTLINE owner "stress, strain, strength envelope"; contested
with physics b2/b3 tensors, see report):
- traction, normal stress, shear stress (in rocks) --- `def:b1:stress-strain-rheology:stress`
- principal stresses, differential stress --- `def:b1:stress-strain-rheology:principal`
- lithostatic pressure, pore-fluid pressure --- `def:b1:stress-strain-rheology:lithostatic`
- extension, stretch, shear strain, strain ellipse --- `def:b1:stress-strain-rheology:strain`
- pure shear, simple shear --- `def:b1:stress-strain-rheology:shear-types`
- rheology, elastic, brittle, ductile behaviour --- `def:b1:stress-strain-rheology:rheology`
- Coulomb failure criterion, cohesion, coefficient of internal friction --- `def:b1:stress-strain-rheology:coulomb`
- strength envelope, brittle--ductile transition --- `def:b1:stress-strain-rheology:strength-envelope`
- Byerlee's law --- indexed in `prop:b1:stress-strain-rheology:byerlee`

**Recall.** Physics Hooke's law (b1/b3), viscosity and shear stress in fluids
(physics b2 `viscous-flows`), stress and strain tensors (physics b3, the 3D
theory); ch. 10 (geotherm); math: derivatives, 2×2 symmetric forms.

**Figures.** [S] force balance on a triangular prism (traction on an inclined
plane); [S] the Mohr circle with a Coulomb envelope (computed geometry in
TikZ); [S] pure and simple shear of a square and its inscribed circle (exact
linear maps in TikZ); [F] `strength_envelope.py`: continental and oceanic
envelopes from Byerlee + power-law creep (quartz, olivine) on the ch. 10
geotherm (tests: brittle slope = $(\ldots)\rho g(1-\lambda)$ as derived; the
transition depth is where the two curves cross; creep strength decreases with
T); [P] a deformed rock-mechanics sample or a triaxial press (USGS PD or
Commons, verify); [AI] a rock-deformation laboratory press (generic).

**Ledger.** Byerlee 1978 coefficients (find an open copy or authoritative
restatement); creep parameters for quartz and olivine (Kohlstedt, Evans &
Mackwell 1995, AGU free archive); continental seismogenic depth (open review);
rock densities (ch. 9 rows).

**Problem.** *Will the fault slip?* Part I the stress state at 5 km (vertical
σ1, horizontal stresses given); Part II normal and shear stress on a fault of
given dip; Part III the Mohr circle and Byerlee's criterion; Part IV the pore
pressure rise (fluid injection) that brings the fault to failure. Named
number: **the critical pore-pressure increase** (MPa, computed).

---

## Ch. 17 Faults, Folds and Fabrics --- `faults-folds-fabrics`

**Hook.** A road cutting shows polished, grooved fault surfaces; across the
valley, beds crumple into chevrons; a roofing slate splits along a plane that
is not its bedding.

**Sections.**
1. Faults: geometry and kinematics: hanging wall, footwall, slip vector, net
   slip, rake; normal, reverse, thrust, strike-slip (dextral, sinistral),
   oblique; fault rocks (breccia, gouge, cataclasite; mylonite named).
2. Anderson's theory: a free surface makes one principal stress vertical
   (proposition); three regimes; dips from the Coulomb angle (≈60° normal,
   ≈30° thrust, vertical strike-slip; derived from ch. 16); regimes and plate
   settings.
3. Fold geometry (recall ch. 4 `def:b1:geological-maps:fold`): hinge, hinge
   line, limb, axial plane, interlimb angle; classification (gentle to
   isoclinal; upright to recumbent; plunging); cylindrical folds; parallel and
   similar folds (told).
4. Fabrics: foliation, schistosity, slaty cleavage; axial-planar cleavage;
   lineation (stretching, intersection); cleavage--bedding relations and
   vergence.
5. Microstructures: undulose extinction (ch. 8), pressure solution, dynamic
   recrystallisation; shear-sense indicators (told; Year 3 volume).

**Definitions:**
- hanging wall, footwall, slip vector, net slip, rake --- `def:b1:faults-folds-fabrics:fault-elements`
- normal fault, reverse fault, thrust fault, strike-slip fault, dextral, sinistral, oblique-slip fault (re-found g7 "fault") --- `def:b1:faults-folds-fabrics:fault-types`
- fault breccia, fault gouge, cataclasite, mylonite (contested: Y3 `deformation-mechanisms` owns shear zones) --- `def:b1:faults-folds-fabrics:fault-rocks`
- Anderson's theory of faulting --- indexed in `thm:b1:faults-folds-fabrics:anderson` (OUTLINE owner)
- hinge, hinge line, limb, axial plane, interlimb angle (OUTLINE "fold geometry") --- `def:b1:faults-folds-fabrics:fold-elements`
- gentle, open, close, tight, isoclinal; upright, inclined, recumbent fold --- `def:b1:faults-folds-fabrics:fold-classes`
- foliation, schistosity, slaty cleavage (contested: g12 owns foliation in school; Y2 `pt-paths`) --- `def:b1:faults-folds-fabrics:foliation`
- lineation --- `def:b1:faults-folds-fabrics:lineation`
- vergence --- `def:b1:faults-folds-fabrics:vergence`

**Recall.** Ch. 4 (fold, anticline, syncline, fold axis; map patterns), ch. 5
(throw, heave), ch. 16 (principal stresses, Coulomb), ch. 8 (extinction);
Book 2 g12 `mountain-building`, `metamorphic-rocks`.

**Figures.** [S] three block diagrams: normal, reverse, strike-slip faults
with their Anderson stress axes (`blockdiagram` pic); [S] fault elements in 3D
(slip vector, rake); [S] fold elements in 3D (hinge line, axial plane,
interlimb angle); [S] fold classification profiles (interlimb angle row;
axial-plane dip row); [S] cleavage--bedding relations across an anticline and
syncline (vergence); [P] chevron folds, slickensides, slaty cleavage, a
mylonite (Commons CC, verify each).

**Ledger.** Anderson 1905/1951 (history); interlimb-angle class limits (Fleuty
1964 or an open authoritative restatement); friction coefficient (ch. 16 row).

**Problem.** *The Varden Hills' structures, measured.* Part I the anticline's
limbs (12°) → interlimb angle and class; Part II the axial plane and plunge;
Part III the fault (attitude 120/60 from `region.py`, strike 030) → Anderson
regime, σ1 vertical and σ3 horizontal along 120°;
Part IV slip vector, rake and net slip from the 200-m throw. Named number:
**the net slip on the Varden fault** (m, ≈ 231).

---

## Ch. 18 The Earthquake Source --- `earthquake-source`

**Hook.** After 1906, Harry Reid surveyed fences and roads offset by metres
along the San Andreas fault and understood that the ground had been bent for
decades before it snapped back.

**Sections.**
1. Elastic rebound and the seismic cycle: interseismic loading, coseismic
   slip, postseismic relaxation; recurrence $T = D/\dot s$ (proposition);
   palaeoseismology told.
2. Seismic moment and magnitudes: $M_0 = \mu A D$; moment magnitude
   $M_w = \tfrac23(\log_{10}M_0 - 9.1)$; energy and moment grow ×31.6 per
   magnitude unit (proposition, derived); saturation of older magnitudes (told);
   rupture size scaling (ledger).
3. Focal mechanisms: first-motion quadrants; nodal and auxiliary planes; P
   and T axes; beach balls (lower-hemisphere projection admitted: Year 3);
   method: reading the fault type.
4. Geodetic measurement of active deformation: GNSS; interseismic profile
   $v(x) = (V/\pi)\arctan(x/D)$ (admitted, Savage & Burford) and the locking
   depth; InSAR told (Year 3 volume).
5. The Gutenberg--Richter law: $\log_{10}N = a - bM$; b ≈ 1 from the
   catalogue; completeness; the largest events dominate the moment release
   (proposition, geometric series).

**Definitions:**
- elastic rebound, seismic cycle, recurrence interval --- `def:b1:earthquake-source:seismic-cycle`
- seismic moment (OUTLINE owner) --- `def:b1:earthquake-source:moment`
- moment magnitude (re-found g7 "magnitude") --- `def:b1:earthquake-source:mw`
- focal mechanism, nodal plane, auxiliary plane, P axis, T axis (OUTLINE owner) --- `def:b1:earthquake-source:focal-mechanism`
- locking depth --- `def:b1:earthquake-source:locking-depth`
- b-value --- `def:b1:earthquake-source:b-value`; the Gutenberg--Richter law indexed in `prop:b1:earthquake-source:gutenberg-richter`

**Recall.** Book 1 g7 (focus, epicentre, magnitude, intensity); ch. 16
(stress, elasticity, rigidity), ch. 17 (fault types); physics b3 (shear
modulus).

**Figures.** [F] `gutenberg_richter.py`: cumulative frequency--magnitude of
the USGS M ≥ 6 catalogue 1976--2025 with a least-squares b (tests: counts
equal the dataset; b within 0.8--1.2; the fit recovers b on a synthetic
catalogue); [F] `beachballs.py`: lower-hemisphere equal-area beach balls for
normal, reverse, strike-slip and the Tohoku mechanism (tests: the auxiliary
plane formula on known cases; quadrant signs); [F] `interseismic.py`: the
arctan profile across the San Andreas (test: $v(0) = 0$, limits $\pm V/2$);
[S] elastic rebound as a fence across a fault (three stages); [S] first-motion
quadrants around a strike-slip source; [P] the 1906 fence offset (USGS, G. K.
Gilbert, PD); [AI] a seismological observatory (generic, no readable screens).

**Ledger.** $M_w$ formula (IASPEI standard / Hanks & Kanamori 1979, AGU free);
Tohoku and Sumatra 2004 $M_w$, $M_0$, mechanism (USGS, Global CMT); San
Andreas slip rate and locking depth (Savage & Burford 1973, AGU free archive);
rigidity 30 GPa convention (source); 1906 slip (USGS); Reid 1910 (history);
rupture scaling (Wells & Coppersmith 1994, open?).

**Problem.** *The next great earthquake on a locked fault.* Part I loading
rate and elapsed time → slip deficit; Part II locked area → $M_0$ and $M_w$;
Part III the Gutenberg--Richter recurrence of such events and the energy
compared with a magnitude-6 event; Part IV the GNSS profile → locking depth.
Named number: **the magnitude of the earthquake that would release the
deficit** (Mw, computed).

---

## Ch. 19 Weathering and Clays --- `weathering-clays`

**Hook.** The lettering of an old gravestone fades; a granite outcrop crumbles
to gritty sand; tropical soils are red and deep.

**Sections.**
1. Physical and chemical weathering: frost, heating, salt; dissolution,
   hydrolysis, oxidation; controls (temperature, water, surface area).
2. Hydrolysis of silicates: feldspar → kaolinite (`\ce`, balanced); degrees:
   bisiallitisation (smectite), monosiallitisation (kaolinite), allitisation
   (gibbsite); leaching; the weathering stability series (Goldich 1938) and
   Bowen recalled.
3. The ionic-potential diagram: $z/r$; soluble cations, hydrolysates, soluble
   oxyanions (computed diagram).
4. Clay minerals: T--O and T--O--T layers; kaolinite, illite, smectite,
   chlorite; swelling and cation exchange (told); clays as climate indicators
   (zonation with latitude; palaeoclimate).
5. Silicate weathering and carbon dioxide: the Urey reactions (balanced); net
   transfer of CO₂ to carbonate; time scale (the thermostat: Year 2 volume).

**Definitions:**
- physical weathering, chemical weathering (re-found g5 `water-shapes-the-land`; contested with biology b2 `living-soil` "weathering") --- `def:b1:weathering-clays:weathering`
- hydrolysis (of silicates) (OUTLINE owner; homograph of biology b1 "hydrolysis") --- `def:b1:weathering-clays:hydrolysis`
- bisiallitisation, monosiallitisation, allitisation --- `def:b1:weathering-clays:hydrolysis-degree`
- ionic potential (OUTLINE owner) --- `def:b1:weathering-clays:ionic-potential`
- clay mineral, kaolinite, illite, smectite, chlorite (OUTLINE "clay and climate"; biology b2 defines "clay" the soil material) --- `def:b1:weathering-clays:clay-mineral`
- laterite --- `def:b1:weathering-clays:laterite`

**Recall.** Ch. 7 (silicates, phyllosilicates), chemistry (solubility,
acid--base, ionic radius), biology (soil, horizons, pedogenesis), Book 2 g10
`soil-formation`.

**Figures.** [F] `ionic_potential.py`: charge against ionic radius with the
boundaries $z/r$ = 3 and 12 nm⁻¹-equivalents (tests: Na⁺ soluble, Al³⁺
hydrolysate, Si⁴⁺/P⁵⁺ oxyanion side; radii equal the ledger); [S] T--O and
T--O--T clay structures with basal spacings 0.7, 1.0, 1.4 nm; [S] pole-to-
equator weathering profile and clay zones (schematic after Strakhov, sourced);
[S] hydrolysis degrees vs leaching intensity; [P] weathered granite (grus or
tor) and a laterite (Commons CC, verify); [P] kaolinite SEM (USGS PD,
verify).

**Ledger.** ionic radii (Shannon 1976 via the Imperial College database);
ionic-potential boundaries (source); clay basal spacings (USGS Open-File Report
01-041, PD); Goldich 1938 (history); CO₂ consumption by silicate weathering
(open source); expansion of water on freezing (CRC/NIST).

**Problem.** *From granite to clay.* Part I balance the hydrolysis of albite
and anorthite; Part II mass of kaolinite and silica released per tonne of
feldspar; Part III CO₂ consumed and bicarbonate exported; Part IV a river's
bicarbonate flux → the area of granite weathering it represents. Named
number: **the carbon dioxide drawn down by weathering one tonne of
anorthite** (kg, computed).

---

## Ch. 20 Erosion and Transport --- `erosion-transport`

**Hook.** After a storm the river runs brown: tonnes of mud pass each second;
a reservoir behind a dam loses a fraction of its volume to silt every year.

**Sections.**
1. Solute and particle fluxes: dissolved, suspended and bed load; flux = CQ;
   catchment sediment budget; global fluxes (ledger).
2. Settling velocity: force balance; Stokes drag admitted (physics b2) →
   $w = (\rho_s - \rho)gd^2/18\mu$ (proposition, derived from the balance);
   validity (Reynolds number recalled); coarse grains and a combined formula
   (admitted, ledger).
3. Threshold of motion and the Hjulström diagram: bed shear stress
   $\tau = \rho g h S$ (derived for steady uniform flow); the Shields criterion
   (admitted); the Hjulström diagram (erosion, transport, deposition; cohesion
   of fine grains).
4. Denudation rates: definition and lowering rate; methods (river loads,
   reservoirs, cosmogenic nuclides told); ranges by setting; isostatic
   response to erosion (ch. 11).

**Definitions:**
- dissolved load, suspended load, bed load --- `def:b1:erosion-transport:load`
- settling velocity --- `def:b1:erosion-transport:settling`
- bed shear stress --- `def:b1:erosion-transport:bed-shear`
- threshold of motion, Shields parameter --- `def:b1:erosion-transport:threshold`
- Hjulström diagram (OUTLINE owner) --- `def:b1:erosion-transport:hjulstrom`
- denudation rate (OUTLINE owner; re-found g5) --- `def:b1:erosion-transport:denudation`

**Recall.** Physics b2 `viscous-flows` (viscosity, Stokes' law, Reynolds
number; admitted, pointer); Book 1 g5 (erosion, transport, deposition); ch.
11 (isostasy), ch. 19 (dissolved products).

**Figures.** [F] `settling.py`: settling velocity against grain size (Stokes
and the combined law) (tests: the two agree for fine silt; Stokes formula
values); [F] `threshold.py`: critical bed shear stress against grain size from
the Shields curve (tests: the formula at 1 mm; monotonic for sand); [S] the
Hjulström diagram, after Hjulström (1935), fields labelled (schematic,
sourced shape); [S] load types in a channel and forces on a grain; [P] a
sediment plume at a river mouth from space (NASA PD, verify); [AI] a muddy
river in spate seen from a bridge (observation only).

**Ledger.** global suspended sediment and solute fluxes to the ocean (open
sources); water viscosity and density at 20 °C (NIST/IAPWS); quartz density
(ch. 7 row); Shields threshold constants (Soulsby & Whitehouse 1997 or an open
equivalent); combined settling law constants (Ferguson & Church 2004);
denudation ranges (Portenga & Bierman 2011, GSA Today, open); Hjulström 1935
(history).

**Problem.** *How fast are the Varden Hills wearing away?* Part I discharge and
concentrations at the region's outlet → fluxes; Part II the catchment's
denudation rate (80 km²); Part III settling of the grain sizes in a planned
reservoir; Part IV time to lower the hills by 100 m, without and with isostatic
rebound. Named number: **the time to lower the Varden Hills by 100 m with
isostasy** (Myr, computed).

---

## Ch. 21 Clastic Sediments and Their Environments --- `clastic-sediments`

**Hook.** On a beach the sand is all one size; a glacial deposit mixes boulders
and mud; each sorting tells how the grains travelled.

**Sections.**
1. Grain size and sorting: the Udden--Wentworth scale and φ; mean and sorting
   (standard deviation in φ); roundness; textural and compositional maturity.
2. Bedforms and sedimentary structures: ripples, dunes, plane beds,
   antidunes; their stability fields (schematic); cross-bedding and
   palaeocurrents (vector mean, ch. 6); graded beds; younging criteria.
3. Fluvial and deltaic deposits: braided and meandering rivers; point bars
   and fining-upward successions; river-, wave- and tide-dominated deltas.
4. Shoreline and shelf: beaches, barriers, tidal flats.
5. Deep-sea clastics: turbidity currents, turbidites and the Bouma sequence;
   contourites told; pelagic sediments in ch. 22.

**Definitions:**
- grain-size scale, phi scale --- `def:b1:clastic-sediments:grain-size` (sand/silt/clay as classes in a table, NOT emphasised, to avoid the "clay" homograph)
- sorting, mean grain size --- `def:b1:clastic-sediments:sorting`
- textural maturity, compositional maturity --- `def:b1:clastic-sediments:maturity`
- bedform, ripple, dune --- `def:b1:clastic-sediments:bedform`
- cross-bedding, palaeocurrent --- `def:b1:clastic-sediments:cross-bedding`
- sedimentary facies, depositional environment (contested: Y2 metamorphic facies, Y3 facies models) --- `def:b1:clastic-sediments:facies`
- river-dominated, wave-dominated, tide-dominated delta (re-found g5 "delta") --- `def:b1:clastic-sediments:delta`
- turbidity current, turbidite, graded bed --- `def:b1:clastic-sediments:turbidite`

**Recall.** Ch. 20 (transport, settling), ch. 6 (vector mean); Book 1 g5
(meanders, deltas), g7 (sediments, layers).

**Figures.** [F] `grain_size.py`: cumulative curves and histograms in φ for a
beach sand and a till (exercise data; tests: printed mean and sorting equal
the computed moments); [S] bedform stability diagram (velocity vs grain size,
sourced schematic); [S] cross-bedding from migrating ripples/dunes; [S]
meandering river block with point bar and a fining-upward log (lith styles);
[S] delta classification triangle; [S] Bouma sequence log; [P] cross-bedded
sandstone, ripple marks (Commons CC or USGS PD, verify), a delta from space
(NASA PD); [AI] a sediment-core laboratory (generic).

**Ledger.** Wentworth 1922, Krumbein 1934 (history; scale limits); Bouma 1962;
Galloway 1975; the bedform diagram's source (Southard & Boguchwal 1990).

**Problem.** *Reading a core from a delta.* Part I grain-size data → mean and
sorting of four beds; Part II coarsening-upward → prograding delta;
Part III cross-bed dip directions → mean palaeocurrent (vector mean);
Part IV progradation rate from ages given. Named number: **the mean
palaeocurrent azimuth** (degrees, computed).

---

## Ch. 22 Carbonate, Siliceous and Evaporite Sediments --- `chemical-biogenic-sediments`

**Hook.** White chalk is made of microscopic plates of algae; a reef seen from
a boat is a limestone in the making.

**Sections.**
1. The carbonate factory: calcite, aragonite, dolomite (ch. 7); precipitation
   (`\ce`, balanced); carbonate chemistry of seawater recalled (chemistry b3,
   biology); the tropical shallow factory and its producers; ooids.
2. Reefs and platforms: fringing, barrier, atoll (Darwin, history; subsidence
   story in the Year 2 volume); rimmed shelves and ramps; growth vs sea level.
3. Pelagic oozes and the CCD: calcareous ooze; lysocline and carbonate
   compensation depth; why calcite dissolves at depth (told, chemistry);
   ocean-to-ocean differences.
4. Siliceous oozes and cherts: diatoms, radiolarians; silica undersaturation;
   chert, diatomite; upwelling zones (ch. 29).
5. Evaporites: the evaporation sequence (calcite, gypsum, halite, K--Mg
   salts) computed; sabkhas and barred basins; the thickness problem
   (Messinian, told).

**Definitions:**
- carbonate factory --- `def:b1:chemical-biogenic-sediments:factory`
- reef, carbonate platform, ooid --- `def:b1:chemical-biogenic-sediments:reef`
- calcareous ooze, siliceous ooze --- `def:b1:chemical-biogenic-sediments:ooze`
- lysocline, carbonate compensation depth (OUTLINE owner) --- `def:b1:chemical-biogenic-sediments:ccd`
- chert --- `def:b1:chemical-biogenic-sediments:chert`
- evaporite, evaporation sequence, sabkha (OUTLINE owner) --- `def:b1:chemical-biogenic-sediments:evaporite`

**Recall.** Chemistry b3 `environmental-toxicology` (ocean carbonate chemistry,
alkalinity), biology b2 (carbon cycle, carbonate system), ch. 7 (carbonate
minerals), ch. 26/29 forward pointers.

**Figures.** [F] `evaporation.py`: fraction of the brine remaining at the
onset of each mineral and the mass precipitated per kg of seawater (tests:
total precipitated ≤ the salinity; the ions balance); [S] CCD and lysocline
on a ridge flank with the oozes above and red clay below; [S] reef types and a
rimmed platform cross-section; [S] barred-basin evaporite model; [P] a
coccolith (SEM), planktonic foraminifera, diatoms (Commons CC / NOAA PD,
verify), a coral reef (NOAA PD), a salt flat from space (NASA PD).

**Ledger.** CCD depths by ocean (open source); seawater major-ion composition
(open reference composition); evaporation thresholds (Usiglio 1849 via an open
restatement, or a USGS source); reef accretion rates; Messinian salt volume
(open source); Darwin 1842 (history).

**Problem.** *Salt from a vanished sea.* Part I gypsum and halite from a
1000-m column of seawater; Part II the brine fractions at each threshold;
Part III refills needed for 1.5 km of salt; Part IV the time at a given inflow
and the sea-level fall of a closed basin. Named number: **the number of times
the basin must be refilled** (computed).

---

## Ch. 23 Diagenesis and Sedimentary Basins --- `diagenesis-basins`

**Hook.** Beach sand buried three kilometres down comes back up in a drill
core as hard sandstone, its pores filled with quartz.

**Sections.**
1. Compaction: porosity with depth (Athy's law, empirical, ledger); solid
   volume conserved: decompaction (method); mechanical and chemical
   compaction (pressure solution).
2. Cementation and other changes: quartz overgrowths, calcite, clay cements;
   dissolution and secondary porosity; dolomitisation; diagenetic stages.
3. Sedimentary basins: what a basin is; types by setting (rift, passive
   margin, foreland, intracratonic, strike-slip) --- their comparison and
   subsidence analysis are the Year 2 volume's.
4. Subsidence, accommodation and sea level: accommodation; eustasy and
   relative sea level; $\Delta A = \Delta E + S$ (proposition); sediment loading
   amplifies subsidence by $\rho_m/(\rho_m - \rho_s)$ (derived, ch. 11); the
   last glacial lowstand.

**Definitions:**
- diagenesis --- `def:b1:diagenesis-basins:diagenesis`
- compaction, decompaction --- `def:b1:diagenesis-basins:compaction`
- cementation, cement --- `def:b1:diagenesis-basins:cement`
- sedimentary basin --- `def:b1:diagenesis-basins:basin`
- subsidence, tectonic subsidence --- `def:b1:diagenesis-basins:subsidence`
- accommodation (OUTLINE owner) --- `def:b1:diagenesis-basins:accommodation`
- eustasy, relative sea level (OUTLINE owner) --- `def:b1:diagenesis-basins:eustasy`

**Recall.** Ch. 11 (isostasy), ch. 13 (passive margins), ch. 21--22
(sediments); Book 1 g6 (porosity, permeability).

**Figures.** [F] `compaction.py`: porosity against depth for sand and shale
and the decompaction of a buried layer (tests: solid thickness conserved;
$\varphi(0) = \varphi_0$); [S] accommodation diagram (sea level, datum, basin
floor, subsidence + eustasy); [S] basin types (four small sections); [F]
`sea_level.py`: sea level over the last 140 kyr or 800 kyr from a published
stack (test: the last-glacial minimum within the ledger range); [P] a
sandstone thin section with quartz overgrowths (Commons CC, verify); [AI] a
drilling rig (generic) unless used in ch. 10.

**Ledger.** Athy-law parameters (Sclater & Christie 1980, AGU free archive);
last-glacial sea level (Lambeck et al. 2014, PNAS open); the stack (Spratt &
Lisiecki 2016, NOAA NCEI, PD with citation).

**Dataset.** possibly `bachelor-1-sealevel-stack.csv` (Spratt & Lisiecki 2016,
NOAA NCEI Paleoclimatology, ~100 KB).

**Problem.** *Decompacting a basin's fill.* Part I today's column (sand and
shale) and porosities; Part II solid thicknesses; Part III thickness of each
unit when it was deposited; Part IV accommodation created and the share of
eustasy. Named number: **the thickness of the shale unit at deposition**
(m, computed). (No backstripping: the Year 2 volume owns it.)

---

## Ch. 24 The Stratigraphic Scale --- `stratigraphic-scale`

**Hook.** In a gully a bronze disc is set into the rock: the golden spike that
fixes, for the whole planet, where one stage of geological time begins.

**Sections.**
1. Three stratigraphies: lithostratigraphy (formation, member, group);
   biostratigraphy (biozones, index fossils, first appearance datum);
   chronostratigraphy and geochronology (stage/age, series/epoch, system/period,
   erathem/era, eonothem/eon).
2. The principles revisited: superposition, original horizontality, lateral
   continuity, cross-cutting, faunal succession (re-founded); correlation;
   diachronous lithological boundaries.
3. Boundary stratotypes: the GSSP and its criteria; examples (ledger); unit
   stratotypes, historically.
4. Mass extinctions as global markers: recalled from biology; the K--Pg
   iridium layer (Alvarez et al. 1980) and Chicxulub; the end-Permian.
5. The international chart: structure, colours, calibration by radiometric
   ages (ch. 25); `dated` box: the status of the Anthropocene proposal.

**Definitions:**
- formation, member, group (lithostratigraphic units) --- `def:b1:stratigraphic-scale:lithostratigraphy`
- biozone, index fossil, first appearance datum --- `def:b1:stratigraphic-scale:biozone`
- chronostratigraphic unit, geochronologic unit, stage, system, series (OUTLINE owner "chronostratigraphy"; re-found g7 "eras and periods") --- `def:b1:stratigraphic-scale:chronostratigraphy`
- principles of stratigraphy: superposition, original horizontality, lateral continuity, cross-cutting relationships, faunal succession (re-found g7 `geological-time`) --- `def:b1:stratigraphic-scale:principles`
- diachronous boundary --- `def:b1:stratigraphic-scale:diachronous`
- global boundary stratotype section and point (GSSP), boundary stratotype, unit stratotype (OUTLINE owner "stratotype") --- `def:b1:stratigraphic-scale:gssp`

**Recall.** Biology g9/g10/b2 (fossils, mass extinctions); Book 1 g7
`geological-time`; ch. 4--5 (map/section chronology); ch. 21 (facies).

**Figures.** [F] `ics_chart.py`: Phanerozoic bar with period colours and base
ages parsed from the shared `ics:` rows (tests: bases decreasing, equal to the
ledger; colours equal the `ics:colour.*` rows); [S] range chart and
correlation of two sections by biozones (invented taxa); [S] a diachronous
sandstone in a transgression (time lines vs formation boundaries); [P] a GSSP
golden spike (Commons CC, verify), the K--Pg boundary clay (USGS/Commons,
verify).

**Ledger.** shared `ics:*`; GSSP examples (place, ratification year) and the
number ratified (`dated`) (ICS GSSP table); Alvarez et al. 1980; Chicxulub
age; Anthropocene vote 2024 (IUGS/ICS statement); extinction magnitudes recalled
(biology series or a primary source).

**Problem.** *Correlating three sections across a basin.* Part I biozone
ranges → correlation; Part II a diachronous sandstone; Part III two dated ash
beds → sedimentation rates; Part IV interpolated age of a stage boundary.
Named number: **the interpolated age of the boundary** (Ma, computed from the
exercise's ash ages).

---

## Ch. 25 Radiometric Dating Methods --- `radiometric-methods`

**Hook.** A zircon grain smaller than a sand grain, from Western Australia,
crystallised 4.4 billion years ago; volcanic ash beds date the extinction of
the dinosaurs to 66.0 million years.

**Sections.**
1. Decay systems: the decay law recalled (physics); radiogenic growth
   $D^* = P(e^{\lambda t} - 1)$ (derived); the age equation; systems table
   (K--Ar, Rb--Sr, U--Pb, ¹⁴C; Sm--Nd named).
2. Isochrons: Rb--Sr isochron (theorem, derived); least-squares fit (method);
   initial ratio meaning (re-founds g12).
3. K--Ar, U--Pb and radiocarbon: branching decay of ⁴⁰K (formula derived);
   argon loss; U--Pb's two chronometers (concordia: Year 3); radiocarbon
   production, decay and calibration (IntCal).
4. Closure temperature: definition; values by system and mineral; cooling
   ages and cooling rates (thermochronology: Year 3).
5. Dating sedimentary sequences, calibrating the scale: ash beds and zircon,
   bracketing ages, interpolation; the K--Pg example; precision of the chart.

**Definitions:**
- parent isotope, radiogenic daughter --- `def:b1:radiometric-methods:radiogenic`
- isochron, initial ratio (re-found g12 `age-of-the-earth`) --- `def:b1:radiometric-methods:isochron`
- branching decay (of potassium-40) --- `def:b1:radiometric-methods:branching`
- closure temperature, cooling age (OUTLINE owner) --- `def:b1:radiometric-methods:closure`
- radiocarbon age, calibration curve --- `def:b1:radiometric-methods:radiocarbon`
- bracketing age --- `def:b1:radiometric-methods:bracketing`

**Recall.** Physics g12 `radioactive-decay` (decay law, half-life, decay
constant), physics g11 (isotopes), chemistry mass spectrometry; Book 2 g12
`age-of-the-earth`; ch. 24 (chart), ch. 7 (zircon, micas).

**Figures.** [F] `isochron.py`: a Rb--Sr isochron of the Varden granite
(exercise data consistent with 310 Ma) with least squares (tests: slope →
310 Ma; the fit recovers a synthetic age); [F] `decay_curves.py`: parent and
daughter against time in half-lives (test: $P + D^* = P_0$); [F]
`radiocarbon.py`: IntCal20 vs the 1:1 line over 0--12 kyr (tests: values at
chosen points equal the dataset; monotonic overall); [S] closure temperatures
by system and mineral (bar chart, ledger values); [S] ash beds bracketing a
boundary; [P] zircon cathodoluminescence image (Commons CC, verify), a mass
spectrometer (USGS PD or Commons, verify).

**Ledger.** decay constants / half-lives (⁸⁷Rb, ⁴⁰K with branching, ²³⁸U,
²³⁵U, ¹⁴C) from NNDC NuDat and the geochronology conventions (Steiger &
Jäger 1977; Villa et al. 2015 for Rb); Libby half-life convention (Stuiver &
Polach 1977, Radiocarbon, open); closure temperatures (open review); Jack
Hills 4.4 Ga (Wilde et al. 2001 or an open restatement); K--Pg 66.0 (shared
`ics:base.Paleogene`).

**Dataset.** possibly `bachelor-1-intcal20.csv` (Reimer et al. 2020,
Radiocarbon, open; ~0.4 MB); otherwise ledger points only.

**Problem.** *Dating the Varden granite and its cover.* Part I Rb--Sr
whole-rock isochron → crystallisation age and initial ratio; Part II K--Ar on
biotite → a younger age; Part III closure temperatures → cooling rate; Part IV
an ash bed in the Triassic sandstone → the time gap at the unconformity. Named
number: **the granite's cooling rate** (°C per Myr, computed).

---

## Ch. 26 Structure of the Atmosphere and the Ocean --- `fluid-envelopes-structure`

**Hook.** At dawn a weather balloon rises to 30 km while, far out at sea, a
ship lowers a rosette of bottles to the abyss: two profiles of the planet's
fluid envelopes.

**Sections.**
1. The vertical structure of the atmosphere: the standard atmosphere;
   troposphere, tropopause, stratosphere (recalled from Book 1 g8, made
   quantitative); hydrostatic balance and scale height recalled (physics b1).
2. Lapse rates and potential temperature: environmental lapse rate; dry
   adiabatic lapse rate $\Gamma_d = g/c_p$ (theorem, from the first law and
   hydrostatics, physics recalled); potential temperature
   $\theta = T(p_0/p)^{R/c_p}$ (proposition, from the adiabatic relation).
3. Static stability: the parcel method; stable iff $\Gamma < \Gamma_d$ iff
   $\mathrm d\theta/\mathrm dz > 0$ (theorem); inversions; the moist case
   (Year 2 volume).
4. The layered ocean: mixed layer, thermocline, halocline, pycnocline;
   salinity (recalled); profiles by latitude.
5. Seawater density and T--S diagrams: the equation of state; linear form with
   α and β; σ; the T--S diagram with isopycnals (computed); water masses;
   mixing lines are straight (proposition); cabbeling (told).

**Definitions:**
- standard atmosphere --- `def:b1:fluid-envelopes-structure:standard-atmosphere`
- environmental lapse rate, dry adiabatic lapse rate (re-found g8; contested with biology b2 "lapse rate") --- `def:b1:fluid-envelopes-structure:lapse-rate`
- air parcel --- `def:b1:fluid-envelopes-structure:parcel`
- potential temperature (OUTLINE owner) --- `def:b1:fluid-envelopes-structure:potential-temperature`
- static stability, stable, unstable, neutral stratification, temperature inversion (OUTLINE owner; re-found g10 `why-clouds-form`) --- `def:b1:fluid-envelopes-structure:stability`
- mixed layer, thermocline, halocline, pycnocline (re-found g10 `layered-ocean`) --- `def:b1:fluid-envelopes-structure:ocean-layers`
- equation of state of seawater, haline contraction coefficient, density anomaly σ --- `def:b1:fluid-envelopes-structure:eos`
- T--S diagram, water mass (OUTLINE owner) --- `def:b1:fluid-envelopes-structure:ts-diagram`

**Recall.** Physics b1 `fluid-statics` (hydrostatic relation, scale height),
`first-law` (adiabatic transformation, Laplace's relation, $c_p$), `kinetic-
theory` (thermal expansion), physics b1 `phase-changes` (humidity, dew point);
Book 1 g8 (atmospheric layers, salinity), Book 2 g10 (stability, mixed layer,
thermocline).

**Figures.** [F] `standard_atmosphere.py`: T(z) and p(z) of the 1976 standard
atmosphere to 86 km (tests: T(11 km) = 216.65 K; p(11 km) = 22 632 Pa;
hydrostatic integration matches the closed form); [S] parcel diagram
(environmental vs dry adiabat; stable/unstable); [F] `seawater_eos.py`: EOS-80
density, σ isopycnals on a T--S diagram with water-mass points (tests: the
UNESCO check values; linearised α, β at a reference point); [S] typical ocean
T, S, ρ profiles in three latitude bands (sourced shapes); [P] a radiosonde
launch (NOAA PD), a CTD rosette (NOAA PD, verify).

**Ledger.** US Standard Atmosphere 1976 defining values (NOAA/NASA/USAF, PD);
$c_p$ and $R$ of dry air (source); EOS-80 coefficients and check values
(UNESCO technical papers 44, open); water-mass T--S characteristics (open
source; or derived from World Ocean Atlas if Phase B finds a CSV route).

**Problem.** *A radiosonde and a CTD on the same day.* Part I radiosonde
levels → lapse rates and the tropopause; Part II potential temperatures and
stable/unstable layers; Part III CTD → mixed layer, thermocline, σ by the
linear EOS; Part IV mixing of two water masses and the density of the mixture.
Named number: **the potential temperature at the tropopause** (K, computed).

---

## Ch. 27 Radiation and Heat Transport --- `radiation-heat-transport`

**Hook.** The tropics receive far more sunlight than the poles, yet they do
not grow hotter year after year: the winds and currents carry some five
petawatts towards the poles.

**Sections.**
1. Insolation with latitude and season: daily-mean insolation
   $\bar Q = (S_0/\pi)(a/r)^2(h_0\sin\varphi\sin\delta + \cos\varphi\cos\delta\sin h_0)$
   (theorem: integrate ch. 1's instantaneous insolation over the day); polar
   summer maximum; annual mean by latitude; the global mean $S_0/4$.
2. Absorbed and emitted radiation: planetary albedo by latitude; outgoing
   longwave radiation (Stefan--Boltzmann admitted); the tropical surplus and
   polar deficit.
3. Meridional heat transport: energy conservation over a polar cap gives the
   transport as an integral of the net radiation (proposition); its peak near
   35--40°; ocean and atmosphere shares (ledger).
4. Latent heat: evaporation and condensation (physics latent heat recalled);
   latent and sensible heat fluxes; the Bowen ratio; precipitation as an energy
   flux (proposition: 1 m/yr of rain ≈ 78 W/m²).
5. The surface energy budget by component (global values, the assessments;
   recall Book 2 g10).

**Definitions:**
- daily-mean insolation --- `def:b1:radiation-heat-transport:daily-insolation`
- net radiation, radiative surplus, radiative deficit --- `def:b1:radiation-heat-transport:net-radiation`
- outgoing longwave radiation --- `def:b1:radiation-heat-transport:olr`
- meridional heat transport (OUTLINE owner; re-found g10) --- `def:b1:radiation-heat-transport:mht`
- latent heat flux, sensible heat flux, Bowen ratio --- `def:b1:radiation-heat-transport:surface-fluxes`

**Recall.** Ch. 1 (insolation, declination, hour angle); ch. 3 (Bond albedo,
equilibrium temperature); physics (seasons; black body; latent heat); Book 2
g10 `earth-energy-budget`, g12 `climate-change` (energy budget values).

**Figures.** [F] `insolation.py`: daily-mean insolation against latitude and
day of year (contours) (tests: equator at equinox $S_0/\pi$; the North Pole at
June solstice exceeds the equator; the global annual mean is $S_0/4$ within
0.5 %); [F] `energy_balance.py`: zonal absorbed solar and OLR from sourced
zonal profiles or a sourced linear-OLR model, and the transport by
integration (tests: the global net integral vanishes by construction; the peak
latitude and value as printed); [S] heat-transport arrows (atmosphere, ocean)
on a meridional section; [S] surface energy budget diagram (AR6 WG1 values,
citing Book 2 rows read-only if they exist); [P] the Earth from deep space
(NASA DSCOVR/EPIC, PD).

**Ledger.** shared `earth:TSI`, `earth:ecc`, `earth:albedo`; peak meridional
transport and its ocean/atmosphere partition (Trenberth & Caron 2001 or an open
equivalent); AR6 WG1 ch. 7 energy-budget fluxes (section cited); latent heat of
vaporisation (NIST/IAPWS); global mean precipitation (source).

**Problem.** *How much heat crosses the 40th parallel?* Part I insolation at
several latitudes; Part II absorbed (given albedos) and emitted (given OLR)
fluxes; Part III the net radiation of the cap north of 40° N; Part IV the
transport and the latent share. Named number: **the heat transport across
40° N** (PW, computed).

---

## Ch. 28 The General Circulation of the Atmosphere --- `atmospheric-circulation`

**Hook.** Sailors feared the doldrums and blessed the trade winds; today an
eastbound transatlantic flight is an hour shorter, carried by the jet stream.

**Sections.**
1. Forces on moving air: the pressure-gradient force $-(1/\rho)\nabla p$
   (derived); the Coriolis force recalled (physics b1), the Coriolis parameter
   $f = 2\Omega\sin\varphi$; friction.
2. The geostrophic wind: balance; $v_g = |\nabla p|/(\rho f)$ along the isobars,
   low pressure on the left in the Northern Hemisphere (theorem); friction and
   cross-isobar inflow (proposition, qualitative); gradient wind told.
3. Depressions and anticyclones: rotation by hemisphere; convergence and
   ascent; Buys Ballot's law.
4. The three-cell circulation: the Hadley cell, trade winds, subtropical
   highs; angular-momentum conservation and the subtropical jet
   $u = \Omega a\sin^2\varphi/\cos\varphi$ (proposition, derived); Ferrel and
   polar cells; westerlies.
5. The ITCZ and the Walker circulation: seasonal migration; the equatorial
   Pacific's zonal cell (ENSO, monsoons: Year 2 volume).
6. Jet streams: subtropical and polar-front jets, speeds (thermal wind: Year 3
   volume).

**Definitions:**
- pressure-gradient force --- `def:b1:atmospheric-circulation:pgf`
- Coriolis parameter --- `def:b1:atmospheric-circulation:coriolis-parameter`
- geostrophic wind, geostrophic balance (OUTLINE owner) --- `def:b1:atmospheric-circulation:geostrophic`
- cyclone, anticyclone (re-found g8 "depression, anticyclone") --- `def:b1:atmospheric-circulation:cyclone`
- Hadley cell, Ferrel cell, polar cell, subtropical high (OUTLINE owner) --- `def:b1:atmospheric-circulation:cells`
- trade winds, westerlies (re-found g8) --- `def:b1:atmospheric-circulation:winds`
- intertropical convergence zone (OUTLINE owner) --- `def:b1:atmospheric-circulation:itcz`
- Walker circulation --- `def:b1:atmospheric-circulation:walker`
- jet stream, subtropical jet, polar-front jet --- `def:b1:atmospheric-circulation:jet`

**Recall.** Physics b1 `non-inertial-frames` (Coriolis force, Foucault);
Book 1 g8 (winds, fronts, isobars); ch. 26 (stability), ch. 27 (heat
transport).

**Figures.** [S] the three cells on a meridional section with surface winds on
a globe (deflection to the right in the north, to the left in the south); [S]
geostrophic balance on a Northern-Hemisphere isobar map, with friction
inflow; [S] a weather map of a depression and an anticyclone (isobars,
`windbarb` pics consistent with the pressure field, `pressure high/low`); [F]
`angular_momentum_wind.py`: u(φ) of a ring conserving angular momentum vs the
observed subtropical jet (tests: u(0) = 0; u(30°) = 134 m/s from Ω and a);
[P] the ITCZ cloud band (NOAA GOES, PD), a Northern-Hemisphere cyclone from
space (NASA, PD; rotation checked anticlockwise).

**Ledger.** Ω from shared `earth:Trot`; Earth radius shared; observed jet core
speeds and positions (source); Hadley cell extent (AR6 WG1 or an open review);
Hadley 1735 and Ferrel 1856 (history).

**Problem.** *Reading a mid-latitude weather map.* Part I isobar spacing →
geostrophic wind at 50° N; Part II direction and hemisphere checks; Part III
the surface wind with friction; Part IV the angular-momentum wind of a ring
leaving the equator, and why the real jet is slower. Named number: **the
geostrophic wind speed on the map** (m/s, computed).

---

## Ch. 29 Ocean Circulation --- `ocean-circulation`

**Hook.** In 1992 a container of bath toys fell into the North Pacific; years
later the toys were washing up on beaches thousands of kilometres apart,
mapping the gyre.

**Sections.**
1. Wind-driven surface currents: wind stress (bulk formula, ledger); the
   subtropical and subpolar gyres; equatorial currents; the Antarctic
   Circumpolar Current.
2. Ekman transport and upwelling: the Ekman layer; the transport
   $M = \tau/(\rho f)$ at 90° to the right of the wind in the north (theorem,
   from the depth-integrated balance; the spiral itself admitted and computed,
   derived in the Year 3 volume); coastal and equatorial upwelling; Ekman
   pumping in the gyres (told).
3. Western boundary currents: the Gulf Stream and the Kuroshio; westward
   intensification (Stommel 1948, told; Sverdrup balance: Year 3).
4. The meridional overturning circulation: deep-water formation (cooling,
   brine rejection; ch. 26); the AMOC's strength measured at 26° N; residence
   and ventilation times.
5. Water masses: NADW, AABW, AAIW, Mediterranean outflow on the T--S diagram
   (ch. 26).

**Definitions:**
- wind stress --- `def:b1:ocean-circulation:wind-stress`
- gyre, subtropical gyre, subpolar gyre (re-found g8) --- `def:b1:ocean-circulation:gyre`
- Ekman layer, Ekman transport, Ekman spiral (OUTLINE owner) --- `def:b1:ocean-circulation:ekman`
- upwelling, downwelling, coastal upwelling (re-found g10 `layered-ocean`) --- `def:b1:ocean-circulation:upwelling`
- western boundary current --- `def:b1:ocean-circulation:wbc`
- meridional overturning circulation, thermohaline circulation, deep-water formation, sverdrup (unit) (OUTLINE owner) --- `def:b1:ocean-circulation:moc`

**Recall.** Ch. 28 (Coriolis parameter, geostrophy), ch. 26 (T--S, water
masses, density); physics b1 (Coriolis force); Book 1 g8 (currents), Book 2
g10 (upwelling).

**Figures.** [S] world map (shared land) with gyres and major surface
currents (arrows placed by hand from the ledgered pattern); [F] `ekman.py`:
the Ekman spiral hodograph and the transport arrow (tests: surface current 45°
to the right of the wind in the north; transport at 90°; magnitude
$\tau/(\rho f)$); [S] coastal upwelling cross-section (Northern Hemisphere
eastern boundary: equatorward wind, Ekman transport offshore to the right of
the wind, checked against the theorem); [S] the
overturning as a zonal-mean sketch; [P] the Gulf Stream in sea-surface
temperature (NASA PD), an Argo float or CTD (NOAA PD, verify); [AI] a CTD
rosette being lowered from a ship, if no photograph is suitable.

**Ledger.** drag coefficient and air density for the bulk formula (source);
Florida Current transport (NOAA AOML WBTS page); AMOC at 26° N mean (RAPID
programme); ACC transport (Donohue et al. 2016, AGU free); the 1992 toy spill
(NOAA or peer-reviewed); Ekman 1905 and Nansen's *Fram* (history).

**Problem.** *An upwelling coast.* Part I wind speed → wind stress; Part II
Ekman transport per metre of coast and its direction; Part III upwelled volume
along 1000 km; Part IV the Ekman depth and the temperature of the upwelled
water's effect on the coastal air. Named number: **the upwelling transport
along 1000 km of coast** (Sv, computed).

---

## Homographs to curate in Phase C (same book)

| word | senses in this book | plan |
|---|---|---|
| declination | celestial (ch. 1, defined) / magnetic (ch. 6, physics) | write "magnetic declination" always; EXTRA_PROTECT `magnetic\s+declination` |
| altitude | of a star (defined ch. 1) / elevation | defined as "altitude (of a star)"; STOP outside ch. 1 |
| extinction | atmospheric (ch. 2) / extinction position, angle (ch. 8) / mass extinction (biology) | no bare "extinction" term; EXTRA_PROTECT `mass\s+extinctions?` |
| magnitude | apparent/absolute (ch. 2) / moment magnitude (ch. 18) / order of magnitude | no bare term |
| flux | of a source (ch. 2) / heat flow (ch. 10) / sediment fluxes (ch. 20) | define "flux (of a source)" with qualifier; DROP bare if harvested |
| core | Earth's (ch. 9) / fold core (ch. 4) / sediment and ice cores | define "outer core", "inner core" only; EXTRA_PROTECT `core\s+of\s+the\s+(anticline|syncline|fold)`, `ice\s+cores?`, `sediment\s+cores?` |
| plate | tectonic / wave plate, accessory plate (ch. 8) / Bouguer plate (ch. 11) | "rigid plate" defined; EXTRA_PROTECT accessory/red/Bouguer plate |
| arc | of a circle (ch. 1) / volcanic arc (ch. 14) | define "volcanic arc" only; STOP "arc" |
| cell | Hadley cell / unit cell (chemistry) | define the named cells only |
| basin | sedimentary basin (ch. 23) / back-arc basin (ch. 14) / ocean basin / drainage basin | multi-word terms only |
| facies | sedimentary (ch. 21) / metamorphic (Year 2) | define "sedimentary facies" |
| clay | clay mineral (ch. 19) / grain-size class (ch. 21) | only "clay mineral" defined |
| front | weather front (not defined here) / ice front / wavefront | none defined |
| scale | stratigraphic, map, grain-size, magnitude | multi-word only |
| limb | of a fold (ch. 17) / of the Sun | STOP outside ch. 17 if needed |
| hinge, cement, load, sorting, stage, member, group, formation | ordinary words | STOP outside owner chapters; EXTRA_PROTECT for "stage of" etc. |
