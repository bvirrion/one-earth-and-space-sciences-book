# BRIEFS --- Book 5 (University Year 3, `bachelor-3`, prefix `b3`)

Phase A plan, written 2026-10-23 by the Book 5 agent. One brief per chapter,
in outline order: hook; sections; definitions (term, label, owner check);
recall boxes; planned figures tagged **[S]** schematic (TikZ/pgfplots typed),
**[F]** figdata (tested script, `figdata/bachelor-3/<name>.py`, test
`tests/bachelor-3/test_<name>.py`), **[AI]** AI illustration (generic scene),
**[P]** photograph (PD or verified CC); ledger needs; datasets; the weekend
problem's story and its named final number. `DEFINITIONS.md` is the term
table (labels); `PROGRESS.md` the state and the traps.

Numbers quoted in these briefs are *planning orders of magnitude only*: none
goes into the book until it is fetched from its source into
`sources/ledger/book5.md` (or computed by a tested figdata script).

## Conventions binding on this book

- **Register (Year 3).** Every law owned here is a `theorem`/`proposition`
  with a derivation at Year-3 mathematics: stress and strain tensors
  (eigenvectors, invariants, Mohr construction), Fourier series and
  transforms, convolution, separation of variables and similarity solutions
  of the diffusion equation, rotating-frame fluid equations with scale
  analysis, linear inverse problems (G m = d, weighted and damped least
  squares, covariance and resolution of the estimate), statistics with
  uncertainties (Fisher statistics, MSWD, error propagation), ODEs
  integrated numerically in figdata. What the level cannot reach is
  `\admitted` with a prose pointer ("the physics books' Year 3 volume").
  Standard techniques go in `method` boxes (label `met:`).
- **Labels** `<type>:b3:<slug>:<name>`. A term only in its owner chapter,
  inside a `definition`, as `\emph{term}\index{term}`; laws owned here are
  indexed in their theorem/proposition. Never a bare homograph: the
  qualified form is defined and indexed ("equal-area projection (of the
  sphere)", "seismic migration", "fold (of seismic coverage)", "saturation
  index (of a mineral)", "Jeans escape", "intrinsic permeability",
  "retardation factor (sorption)", "magnetic inclination", "tectonic
  underplating", "Kelvin wave (oceanic)"). Never `\cref{fig:...}` (omfigure
  has no counter: "the figure below / opposite"). No `\cref` across books:
  prose only ("the Year 1 volume, in its chapter on isostasy"). Within the
  book, `\cref{ch:b3:...}`, `\cref{def:b3:...}` are fine.
- **A term owned elsewhere that a Year-3 theorem derives** (Ekman spiral,
  Rossby wave, normal moveout is mine but the Ekman spiral is Book 3's) is
  derived in a theorem **without** `\index` of the owned term (an indexed
  theorem counts as a definition for the linker): title the theorem by its
  content ("The Ekman solution", "Dispersion of Rossby waves").
- **Recall boxes.** Year 1 (Book 3) and Year 2 (Book 4) notions and school
  notions in a `recall` box or one clause; sister-series notions with the
  series named in prose ("the physics books' Year 2 volume, in the chapter on
  fluid kinematics"). Never redefine.
- **Calibration.** 12 exercises (4★, 5★★, 3★★★ in that order); one weekend
  problem of 22--28 questions in Parts I--IV, ending on a **named number**
  printed bold; ~12 pp per chapter including solutions. Solutions computed
  from the **rounded printed** data by a calculator script in scratch;
  every answer re-read against its own question (Phase D pairing script).
- **Ledger** ids `<family>:<topic>`; families planned: `seis5:`, `geod5:`,
  `pmag5:`, `therm5:`, `rheo5:`, `petro5:`, `geochron5:`, `iso5:`,
  `strat5:`, `geomorph5:`, `gfd5:`, `ocean5:`, `clim5:`, `hydro5:`,
  `glac5:`, `rs5:`, `planet5:`, `exo5:`, `gal5:`, `nuc5:`, `survey5:`
  plus source-named ids (`ak135:p-30deg`, `pattyn08:glen-A`). Grep
  `sources/data_ledger.md sources/ledger/` before minting; reuse shared rows
  (`const:*`, `earth:*`, `planet:<Body>.<prop>`, `ics:*`, `data:*`) and
  other books' rows read-only. No hyphen in a source-key prefix. **No
  Wikipedia/Wikibooks row** (Sync 2); Commons is for photo credits only.
- **Exercise region:** the Varden Hills (`figdata/shared/region.py`,
  imported, never edited). `contact_elevation()` returns **nan** in the
  fault gap: every call is guarded (`np.isfinite`). No new geological body is
  added to the Varden Hills without a sync ruling (ch. 31 asks).
- **Observation only** (`inthefield`/`inthelab`, third person); **climate:
  physical science only** (AR6 WG1 calibrated language, ledger row per
  statement with chapter and section; no policy); no curriculum, school
  system, university or exam named; institutions only in data and photo
  credits.
- **Figures:** ~4 schematics per chapter plus figdata plots; every curve and
  map from a tested figdata script; each figure object checked on its own
  page at 130 dpi (layout + science), one line in `sources/book5/FIGCHECK.md`.
  Rounding once, from the raw derived data.

---

## Ch. 1 Seismology and Earth Imaging --- `seismology-imaging`

**Hook.** A large earthquake on the far side of the planet: twenty minutes
later the ground under a station on the near side rings, and for days the
whole Earth rings like a bell. From the arrival times alone, seismologists
have built three-dimensional pictures of the mantle. How can a few thousand
arrival times be turned into a picture?

**Sections.**
1. Rays in a spherical Earth: Snell's law in spherical layers, the ray
   parameter p = r sin i / v conserved along a ray (theorem, derived from
   Snell's law between thin shells); turning point where r/v = p; travel-time
   curve T(Δ) and dT/dΔ = p (theorem: derivation by neighbouring rays);
   Herglotz--Wiechert inversion (proposition, Abel integral `\admitted` with
   pointer to math b3); shadow zone and triplications read off T(Δ); travel-time
   tables (ak135/iasp91 named as reference tables; ledger points).
2. Surface waves: Rayleigh and Love waves (particle motions, speeds relative
   to β); Love-wave dispersion over a layer on a half-space (theorem: the
   dispersion equation tan(...) derived from the two boundary conditions);
   phase and group velocity recalled from physics, read on the figdata curve;
   surface-wave dispersion as a depth probe.
3. Normal modes, told: the Earth's free oscillations recalled from physics'
   normal modes; spheroidal and toroidal families, the gravest mode period
   (ledger); a `history` box on the 1960 Chile record.
4. Linear inverse problems: forward vs inverse problem; G m = d; weighted
   least squares with data covariance (theorem: normal equations and the
   covariance of the estimate derived); under-determined and mixed problems;
   damped least squares (theorem: minimiser of the damped functional);
   trade-off curve; model resolution matrix R = G^-g G and its meaning.
5. Seismic tomography: travel-time residuals, slowness perturbations along
   rays, linearisation (Fermat: first-order path invariance, stated with a
   one-line argument); checkerboard test; what tomography sees (slabs, plume
   conduits: recall Book 3's hotspot chapter pointer) and what it cannot
   (resolution, ray coverage, amplitude damping).
6. `inthefield`: a broadband station and a temporary ocean-bottom
   deployment (third person).

**Definitions.** ray parameter; turning point (of a seismic ray); travel-time
table; Herglotz--Wiechert inversion (prop.); Rayleigh wave; Love wave;
surface-wave dispersion; forward problem; inverse problem; weighted
least-squares estimate (thm.); damped least squares; trade-off curve; model
resolution matrix; seismic tomography; travel-time residual; checkerboard
test. Owner check: OUTLINE Y3 owns tomography and surface-wave dispersion;
nothing in school, Book 3 or Book 4; physics owns dispersion relation, phase
and group velocity, normal modes, elastic waves; math owns least squares.

**Recall.** P and S waves, elastic moduli, wave equation in a solid (physics
b3 continuum elasticity); dispersion relation, phase and group velocity
(physics b2); normal modes (physics b2); least squares, covariance, Gaussian
law (math b1/g8); epicentral distance, travel time, travel-time curve, shadow
zone (Book 2 g11); reference Earth model, seismic discontinuities, LVZ, head
wave (Book 3 ch. 9); hotspot, mantle plume (Book 3 ch. 15); slab (Book 3
ch. 14).

**Figures.** [S] ray geometry in concentric shells (angles, p); [F]
`ray_tracing` rays through PREM from a surface source, every 5° of take-off,
with the core shadow; [F] `ray_tracing` T(Δ) for P and S against ledger
ak135 points; [F] `love_dispersion` phase and group velocity vs period for a
35 km crust on a mantle half-space; [S] Rayleigh vs Love particle motions;
[F] `tomo_checkerboard` true checkerboard, ray coverage, recovered model at
two damping values + the trade-off curve; [S] the inverse-problem flow
chart (data, G, misfit, regularisation, model); [AI] a broadband station in
a vault on a hillside (generic); [P] none planned (a Commons seismometer
photo if a verified CC/PD one exists).

**Ledger.** ak135 P and S travel times at 4--6 distances (Kennett, Engdahl &
Buland 1995 tables, via IRIS/EMC or the published table); gravest normal-mode
period 0S2 and 0T2 (primary paper); PREM (shared `data:prem`); typical crust
and upper-mantle β for the Love example (PREM values, shared); 1960 Chile
record facts (a primary source or USGS page).

**Datasets.** Shared `prem` only.

**Weekend problem: "The slab beneath Station K."** An invented station and
a 2-D model. Part I: rays in a linear-gradient layer (circular rays):
ray parameter, turning depth, travel time (exact integrals). Part II: Love
waves at the station: read dispersion, invert group velocities for the crust
thickness with the dispersion equation. Part III: a 4-cell tomography with 6
rays: write G, solve by least squares with data errors, covariance and
uncertainties. Part IV: damping, trade-off, resolution matrix; interpret the
fast cell as a slab. **Named number: the slab cell's P-velocity anomaly, in
per cent (with its 1σ).**

---

## Ch. 2 Exploration Seismology --- `exploration-seismology`

**Hook.** A survey vessel tows twelve kilometre-long cables; every ten
seconds an air-gun array fires. Weeks later, a geologist scrolls through a
section in which buried river channels and tilted fault blocks appear as if
cut open. How do echoes become a cross-section?

**Sections.**
1. Refraction surveys (re-using Book 3's head wave, intercept time and
   crossover distance): dipping-layer refraction (theorem: up-dip and
   down-dip apparent velocities give dip and true velocity), the hidden-layer
   and velocity-inversion blind spots.
2. Reflection at normal incidence: acoustic impedance and the reflection
   coefficient recalled from physics; the reflectivity series; the
   convolutional model s = w * r (proposition; convolution recalled from math
   b3); Ricker wavelet; synthetic seismogram from a log; vertical resolution
   and the tuning thickness λ/4 (proposition from two-spike interference);
   lateral resolution and the Fresnel zone (proposition, first-zone radius).
3. CMP acquisition and processing: common midpoint, fold of coverage;
   normal moveout (theorem: t² = t0² + x²/v² for a flat reflector, the
   dipping-reflector form as an exercise); velocity analysis (semblance told);
   stacking velocity ≈ RMS velocity (proposition, small-offset); interval
   velocities by the Dix equation (theorem, derived from RMS definitions);
   stacking and the √N noise gain (proposition: recall the standard deviation
   of the mean).
4. Migration (principle): why dipping reflectors appear shifted and less
   steep (theorem: sin θ_true = tan θ_apparent for zero offset), diffraction
   hyperbolae, migration as collapsing diffractions; time vs depth sections.
5. Seismic stratigraphy: seismic facies, reflection terminations (onlap,
   downlap, toplap, erosional truncation), reading a section (link forward to
   ch. 16).
6. `inthefield`: a land vibroseis crew and a marine streamer survey (third
   person; marine-mammal mitigation told factually).

**Definitions.** seismic refraction survey; seismic reflection survey;
seismic wavelet; Ricker wavelet; reflectivity series; synthetic seismogram
(prop.); tuning thickness; Fresnel zone; common midpoint; fold (of seismic
coverage); normal moveout (thm.); stacking velocity; root-mean-square
velocity; interval velocity; Dix equation (thm.); stacking (seismic);
seismic migration; seismic stratigraphy; seismic facies; reflection
termination; onlap; downlap; toplap; erosional truncation. Owner check:
nothing in school or Books 3--4 (Book 2 g11 owns "migration (of oil and
gas)", hence "seismic migration"; Book 3 owns "fold", hence the qualified
"fold (of seismic coverage)").

**Recall.** Head wave, intercept time, crossover distance, borehole log
(Book 3 ch. 5/9; Book 2 g11); acoustic impedance, reflection coefficient
(physics b2); convolution, Fourier transform (math b3); standard deviation of
the mean (chemistry/math); sedimentary basin, unconformity (Book 3).

**Figures.** [S] CMP geometry (sources, receivers, common midpoint, fold);
[F] `cmp_nmo` synthetic CMP gather over a 4-layer Varden-like model, before
and after NMO, with the hyperbolae; [F] `cmp_nmo` V_rms and Dix interval
velocities vs time; [F] `synthetic_seismogram` impedance log → reflectivity →
Ricker convolution, plus the wedge model (tuning curve); [S] Fresnel zone
geometry; [S] migration of a dipping reflector (zero-offset smile); [S]
reflection terminations on a sketched section; [F] `refraction_dip`
up-dip/down-dip travel-time branches; [AI] a seismic survey vessel towing
streamers at dusk (generic); [AI] a vibroseis truck line on a dirt road.

**Ledger.** Typical P velocities and densities of chalk, shale, limestone,
sandstone, schist and granite (an open agency/textbook source; the Varden
seismic model uses them); streamer lengths and air-gun firing intervals
(industry-neutral open source, e.g. a USGS/BOEM/NOAA report); marine-mammal
mitigation practice (agency page).

**Datasets.** None (analytic + `region.py` for layer depths).

**Weekend problem: "A seismic line across the Varden Hills."** A synthetic
CMP line along section A--B; depths from `region.section`. Part I: refraction
first breaks on the chalk--shale contact (dipping layer). Part II: NMO
velocities at three CMPs; Dix interval velocities of each unit. Part III:
time-to-depth conversion; tuning of the thin shale on the syncline limb.
Part IV: migrate a dipping reflector, locate the normal fault's reflection
offset. **Named number: the depth of the basement unconformity below the
CMP at the anticline crest, in metres** (checked against `region.py`).

---

## Ch. 3 Gravity and the Figure of the Earth --- `gravity-geodesy`

**Hook.** Two satellites a couple of hundred kilometres apart chase each other
round the Earth; their separation, measured to a few micrometres, has weighed
the ice lost by Greenland month by month. Gravity tells mass where the eye
sees only rock and ice.

**Sections.**
1. The geopotential: gravitational + centrifugal potential (physics recalled);
   equipotential surfaces; spherical-harmonic expansion of the external
   potential (proposition: degree-2 term, Legendre polynomials recalled from
   math/physics); the dynamical form factor J2 and the flattening.
2. The rotating ellipsoid: MacCullagh's formula (theorem, derived from the
   multipole expansion of a body's potential); J2 = (C − A)/(Ma²); the
   reference ellipsoid re-founded (school g10) with its parameters;
   Somigliana's normal gravity (proposition stated, closed form admitted;
   Book 3 owns normal gravity); hydrostatic flattening vs observed (the
   Earth's moment of inertia: shared `earth:MoI`).
3. The geoid and its anomalies recalled from Book 3; the geoid–gravity link
   (Bruns' formula, proposition); geoid heights over subduction zones and
   hotspots (descriptive, ledger).
4. Satellite gravimetry: orbit perturbations (J2 nodal precession,
   proposition derived to first order), GRACE/GRACE-FO principle,
   equivalent water height (definition + proposition σ = ρ_w h); ice-sheet
   and groundwater mass series (dataset).
5. Flexure of the lithosphere: the thin-plate equation D w'''' + Δρ g w = q
   (theorem from beam bending, elastic constants recalled from physics);
   flexural rigidity, effective elastic thickness, flexural parameter;
   solutions for a line load (forebulge position and height, proposition)
   and a broken plate at a trench; seamount moats and foreland basins
   (recall Book 4's foreland basin); regional compensation vs Airy.
6. `inthelab`/`inthefield`: an absolute gravimeter (falling corner cube) and a
   relative gravity survey loop (third person).

**Definitions.** geopotential; spherical-harmonic expansion of the
geopotential (prop.); dynamical form factor (J2); MacCullagh's formula
(thm.); reference ellipsoid (**re-founded**, g10); Somigliana's formula
(prop.); satellite gravimetry; equivalent water height; lithospheric
flexure; flexural rigidity; effective elastic thickness; flexural parameter;
forebulge; regional isostatic compensation. Owner check: J2 and flexure are
Y3's (OUTLINE; Sync 1 "Y3 keeps the ellipsoid and J2"); normal gravity,
isostasy, Airy, Pratt, geoid, geoid height, gravity anomaly, free-air and
Bouguer are Book 3's (recall); flattening and reference ellipsoid are g10's
(the ellipsoid re-founded, flattening recalled).

**Recall.** Gravitational potential (energy), centrifugal force, moment of
inertia, Legendre polynomials / spherical harmonics (physics b1--b3,
chemistry b3); Young's modulus, Poisson's ratio (physics b3); geodesy,
flattening (g10); isostasy, normal gravity, geoid (Book 3 ch. 11); foreland
basin (Book 4 ch. 13); ice sheet (g8).

**Figures.** [S] equipotentials of a rotating body vs a sphere; [F]
`j2_figure` hydrostatic flattening from MacCullagh and the Clairaut relation
(admitted) vs the observed values; [F] `grace_mass` Antarctic and Greenland
mass anomaly 2002--present with trends; [F] `flexure` deflection profiles for
three elastic thicknesses under a line load (forebulge marked) + broken-plate
trench profile; [S] seamount moat cross-section; [S] the GRACE
satellite-pair principle; [P] a NASA/JPL GRACE-FO artist view or the GRACE
geoid image (NASA PD, verify); [AI] a gravimeter on a tripod on a rocky
plateau with an operator noting values (generic).

**Ledger.** GRS80/WGS84 ellipsoid constants (a, 1/f, GM, J2, ω; NGA/IERS
documents; shared `earth:J2`, `earth:flattening` reused if they match);
geoid extremes (EGM2008 doc/NGA); GRACE mission facts (NASA/JPL page);
mass-loss trends (dataset + IMBIE paper, open access); Te values for Hawaii
and a foreland basin (primary papers, open where possible).

**Datasets.** NEW: GRACE/GRACE-FO Antarctic and Greenland mass time series
(NASA, PD; ~20 kB; via NASA's ice-sheet vital-signs text files; if they need
an Earthdata login, use the IMBIE 2018/2020 open-access tables instead).

**Weekend problem: "The moat around Oru seamount."** An invented volcanic
island on old oceanic lithosphere. Part I: J2 and flattening warm-up for a
planet (C, A given). Part II: the island's load, Airy compensation it would
need. Part III: flexure: fit the moat distance and forebulge position to
get α, then D, then T_e. Part IV: the gravity anomaly predicted over the
moat; what a satellite at 400 km would see (upward continuation of one
harmonic). **Named number: the effective elastic thickness of the plate, in
kilometres.**

---

## Ch. 4 Geomagnetism and Palaeomagnetism --- `palaeomagnetism`

**Hook.** A basalt flow erupted 60 million years ago cooled with its tiny
magnetite grains locked parallel to the field of the day. Drilled, oriented
and heated step by step in a shielded room, it still says how far it then
lay from the pole.

**Sections.**
1. The main field: dipole approximation, geocentric axial dipole; field
   components (F, H, Z, D, I); dipole formula tan I = 2 tan λ (theorem,
   derived from the dipole potential); IGRF (spherical-harmonic model, the
   g10 coefficient and the dipole moment from it); secular variation and
   westward drift (dataset IGRF); geomagnetic excursions and reversals
   (recall Book 2 g11); the geodynamo, told (`\admitted`: the dynamo
   equations; ledger for core flow speed order of magnitude).
2. Rock magnetism: remanence recalled from physics (domains, hysteresis,
   Curie temperature); magnetite and haematite; blocking temperature
   (Néel relaxation time stated, `\admitted`); NRM, TRM, DRM, CRM.
3. From sample to direction: stepwise demagnetisation (thermal and AF),
   Zijderveld diagrams, characteristic remanence; Fisher distribution
   (proposition: density on the sphere stated, mean direction, k and α95
   estimators); reliability tests (fold, reversal, baked-contact) in a method
   box.
4. Poles and plates: virtual geomagnetic pole (theorem: spherical-triangle
   formulas, recall Book 3 ch. 1); palaeolatitude; apparent polar wander
   path; continental reconstructions; true polar wander (descriptive, ledger).
5. Magnetostratigraphy: polarity zones in a section
   matched to the GPTS (Book 3 ch. 12), sedimentation rates; the Emperor
   seamounts' palaeolatitudes (Book 3 ch. 15 forward pointer honoured).
6. `inthelab`: a shielded palaeomagnetic laboratory with a cryogenic
   magnetometer (third person).

**Definitions.** main geomagnetic field; geocentric axial dipole; magnetic
inclination; dipole formula (thm.); secular variation; International
Geomagnetic Reference Field; geodynamo; natural / thermoremanent / detrital /
chemical remanent magnetisation; blocking temperature; stepwise
demagnetisation; Zijderveld diagram; characteristic remanent magnetisation;
Fisher distribution (prop.); alpha95 (confidence cone); virtual geomagnetic
pole; palaeolatitude; apparent polar wander; apparent polar wander path;
true polar wander; magnetostratigraphy; geomagnetic excursion. Owner check:
APW and magnetostratigraphy are Y3's (OUTLINE); the school text never names
magnetostratigraphy (status new, though the OUTLINE says "re-founds g11");
physics owns magnetic declination (always "magnetic declination" in full),
remanence, Curie temperature, domains, hysteresis; Book 2 g11 owns magnetic
reversal, normal/reversed polarity; Book 3 ch. 12 owns polarity chron and
GPTS, marine magnetic anomaly.

**Recall.** Earth as a magnet, magnetic declination (physics g4/g11);
remanence, Curie temperature, magnetic domains, hysteresis (physics b3);
magnetic dipole field (physics b1); great circle, spherical triangle (Book 3
ch. 1); magnetic reversal (g11); GPTS, polarity chron (Book 3 ch. 12);
hotspot track (Book 3 ch. 15); Euler pole, finite rotation (Book 3 ch. 12).

**Figures.** [F] `igrf_field` world map of inclination and total intensity
from IGRF (Mollweide, shared land); [F] `igrf_field` dipole moment and
north geomagnetic pole position 1900--2025; [S] field elements on a
compass block (F, H, Z, D, I); [F] `palaeomag_stats` a Zijderveld diagram
and an equal-area plot of a synthetic site (Fisher draws, α95 drawn); [S]
VGP spherical triangle; [F] `apw_path` synthetic APW path of an invented
continent with α95 circles; [S] magnetostratigraphic correlation (section
log ↔ GPTS); [AI] a shielded palaeomagnetic lab with a magnetometer (generic).

**Ledger.** IGRF-14 coefficients and dipole moment (NOAA NCEI / IAGA);
present north geomagnetic pole position (NOAA/BGS page); blocking/Curie
temperatures of magnetite and haematite (physics series ledger or an open
rock-magnetism source); Emperor seamount palaeolatitudes (Tarduno et al.
2003, Science; or an open ODP report); GPTS ages reused from Book 3 rows;
true polar wander rate (primary paper); excursion ages (Laschamp; primary).

**Datasets.** NEW: IGRF-14 coefficient table (NOAA NCEI, public domain/IAGA
open; ~80 kB). Optional: none for APW (synthetic, invented continent).

**Weekend problem: "The red beds of Kesta."** An invented terrane with
three sampled formations. Part I: Fisher means and α95 of three sites from
listed directions. Part II: palaeolatitudes and VGPs, with uncertainties
(dp, dm). Part III: compare to a reference APW path: latitude change and
vertical-axis rotation, with errors. Part IV: a magnetostratigraphic column
in the youngest formation matched to the GPTS: accumulation rate. **Named
number: the terrane's northward drift since the oldest formation, in
kilometres (with its 1σ).**

---

## Ch. 5 Thermal Models of the Lithosphere --- `lithosphere-thermal-models`

**Hook.** Sail away from a mid-ocean ridge and the sea floor deepens: about
2.5 km at the axis, more than 5 km beneath the oldest Pacific. The ocean
floor is a thermometer of the plate cooling beneath it.

**Sections.**
1. The heat equation recalled from physics (diffusion equation, thermal
   diffusivity); scales: diffusion time L²/κ, thermal Péclet number for
   advection vs conduction.
2. Half-space cooling: the similarity solution (theorem: erf profile derived
   by the similarity variable η = z/(2√(κt)); Book 3 ch. 10 and ch. 13
   forward pointers honoured); heat flow q = k ΔT/√(πκt) (corollary);
   subsidence ∝ √t from isostasy (theorem; Book 3's depth--age law is
   *derived* here).
3. The plate model: fixed-temperature base at depth L; the Fourier-series
   solution (theorem, separation of variables; math owns Fourier series);
   asymptotic flattening of depth and heat flow (proposition); half-space vs
   plate against data: depth vs age (dataset: seafloor age + ETOPO), heat
   flow vs age (ledger: compiled values, hydrothermal deficit near ridges).
4. Thermal subsidence of basins: recall Book 4's stretching model; the full
   series vs the first Fourier term (Book 4 used the first term only; Year 3
   owns the series).
5. Continental geotherms: steady conduction with exponentially decreasing
   heat production (proposition); heat-flow–heat-production relation and the
   reduced heat flow (proposition: linear relation from the exponential
   model); cratonic vs young geotherms; lithosphere thickness from xenolith
   geotherms (told, ledger).
6. `inthefield`: marine heat-flow probes (third person).

**Definitions.** thermal Péclet number; half-space cooling model;
error-function geotherm (thm.); plate cooling model; plate-model temperature
series (thm.); heat-flow--age relation (prop.); thermal subsidence; reduced
heat flow; heat-production depth scale. Owner check: plate cooling model is
Y3's (OUTLINE); Book 3 owns heat flow, heat production, geotherm, thermal
boundary layer, thermal lithosphere, depth--age law (recalled; the law is
derived, not re-defined); Book 4 owns stretching model, post-rift
subsidence, thermal time constant.

**Recall.** Diffusion equation, thermal conductivity and diffusivity
(physics b2); Fourier series, error function (math b2/b3); heat flow,
geotherm, thermal lithosphere (Book 3 ch. 10); depth--age law, oceanic crust
(Book 3 ch. 13); isostasy (Book 3 ch. 11); stretching model (Book 4 ch. 16).

**Figures.** [F] `plate_cooling` isotherms under a ridge for the half-space
and the plate model; [F] `plate_cooling` depth vs age and heat flow vs age,
both models, with the binned global data (seafloor age grid + ETOPO) and
ledger heat-flow bins; [F] `continental_geotherm` geotherms for three surface
heat flows; [S] column isostasy for subsidence (ridge vs old plate);
[S] heat-flow probe; [AI] a heat-flow probe being lowered from a research
ship (generic).

**Ledger.** Thermal parameters (k, κ, α, ρ_m, T_m: Turcotte & Schubert
values via an open source; or Stein & Stein 1992 GDH1, Nature --- open
abstract and table check); plate thickness and T_m of GDH1 and of a newer
model (e.g. Richards et al. 2018 JGR, open); heat-flow binned data (Stein &
Stein 1992; Hasterok 2013 if open); craton heat flows (Jaupart & Mareschal
review if open).

**Datasets.** Read-only: Book 2's `data/derived/grade-11-seafloor-age.csv`
(EarthByte 2020 age grid at 1°, CC BY 4.0, Seton et al. 2020) — **needs a
sync ruling**; shared ETOPO 1°.

**Weekend problem: "Forty million years off the ridge."** Part I:
half-space temperatures and heat flow at 10 and 40 Myr. Part II: subsidence
from isostasy; compare with binned depths. Part III: plate model with the
first three Fourier terms; the age where the two models differ by 100 m.
Part IV: fit L from the depth of 120-Myr floor. **Named number: the plate
thickness L that fits the old sea floor, in kilometres.**

---

## Ch. 6 Mantle Convection and Plate Driving Forces --- `mantle-convection`

**Hook.** Hudson Bay is still rising, about a centimetre a year, ten thousand
years after its ice sheet melted. The rate at which the ground springs back
weighs the viscosity of the mantle, and the mantle's viscosity sets how fast
plates can move.

**Sections.**
1. Why the mantle convects: the Rayleigh number (definition, derived as the
   ratio of buoyancy to diffusion and viscous times); critical Rayleigh
   number (stated, linear stability admitted with a pointer to physics);
   mantle Ra estimate; internal heating vs basal heating.
2. Boundary-layer scaling: the Nusselt number; theorem Nu ∝ Ra^{1/3} and
   the velocity scale from a thermal boundary layer that goes unstable at a
   local critical Ra (derived); plate speed and surface heat flow orders of
   magnitude; recall Book 3's thermal boundary layer.
3. Plate driving forces: ridge push (proposition: force from the
   half-space model of ch. 5), slab pull (excess mass of a cold slab),
   basal drag; force balance and plate speeds vs slab-attached fraction
   (ledger: Forsyth & Uyeda 1975 table or a newer open review).
4. Plumes: plume buoyancy flux from swell volume (proposition), plume
   heads vs tails (descriptive, recall LIP and hotspot from Book 3); Stokes
   rise of a sphere (physics' Stokes law recalled).
5. Glacial isostatic adjustment: viscous half-space relaxation (theorem:
   relaxation time τ = 4πη/(ρ g λ) derived for one harmonic of the load);
   uplift curves; mantle viscosity from Fennoscandia and Hudson Bay (ledger);
   Maxwell time and elastic vs viscous response.
6. Mantle structure and convection: whole-mantle vs layered, slabs in
   tomography (recall ch. 1), large low-shear-velocity provinces (ledger).

**Definitions.** Rayleigh number; critical Rayleigh number; Nusselt number;
boundary-layer scaling of convection (thm.); ridge-push force (prop.);
basal drag; plume buoyancy flux; glacial isostatic adjustment; isostatic
relaxation time; mantle viscosity; Maxwell time. Owner check: Rayleigh
number and mantle viscosity are Y3's (OUTLINE); g12 owns mantle and thermal
convection, isostatic rebound; g11 owns ridge push and slab pull (terms;
forces quantified here, indexed only under "ridge-push force"); physics owns
viscosity, Stokes' law, Reynolds number.

**Recall.** Viscosity, Stokes' law, Reynolds number, buoyancy (physics b1/b2);
thermal boundary layer, mantle adiabat (Book 3 ch. 10); isostatic rebound,
mantle convection (g12); ridge push, slab pull (g11); hotspot, plume, LIP
(Book 3 ch. 15); half-space model (ch. 5).

**Figures.** [S] Rayleigh--Bénard cell with boundary layers; [F]
`convection_scaling` Nu and velocity vs Ra (scaling law + critical Ra);
[F] `gia_relaxation` uplift vs time for three viscosities, with ledger
Ångermanland/Hudson Bay shoreline points; [S] force balance on a plate
(ridge push, slab pull, drag); [F] `ridge_push` ridge-push force vs age
from the ch. 5 model; [S] plume head and tail; [P] raised beaches (Commons,
PD/CC to verify: Hudson Bay or Svalbard raised beaches); [AI] none.

**Ledger.** Mantle parameters for Ra (α, ΔT, κ, η, depth); Rac values;
plate speeds vs slab fraction (open review); present uplift rates
(Fennoscandian GNSS, Hudson Bay; primary open papers); upper/lower mantle
viscosity estimates (Peltier or Mitrovica open papers); Hawaiian swell
buoyancy flux (Sleep 1990, or King & Adam 2014 open); LLSVP facts.

**Datasets.** None new (analytic; ledger points).

**Weekend problem: "Rebound of Lake Ardo."** An invented ice-dammed lake
drained 14 kyr ago, leaving tilted shorelines. Part I: load and isostatic
equilibrium depression. Part II: read uplift vs time, fit the relaxation
time. Part III: viscosity from τ for the lake's wavelength; compare the
Maxwell time. Part IV: Rayleigh number of the mantle with that viscosity,
velocity scale, heat flow. **Named number: the upper-mantle viscosity, as
log10 of η in Pa s.**

---

## Ch. 7 Deformation Mechanisms and Shear Zones --- `deformation-mechanisms`

**Hook.** At the surface, the granite of a mountain shatters along faults.
Twenty kilometres down, the same granite flows like toffee in a shear zone a
few hundred metres wide, its quartz grains stretched into ribbons. What lets
a crystal flow without breaking?

**Sections.**
1. Crystal defects: point defects recalled from chemistry; dislocations
   (edge, screw, Burgers vector, glide and climb); why dislocations make
   crystals weak (Peierls stress, told).
2. Creep mechanisms: dislocation creep, diffusion creep (Nabarro--Herring
   and Coble, the grain-size dependence derived by a flux argument),
   grain-boundary sliding, pressure solution; recovery and dynamic
   recrystallisation; subgrains; crystallographic preferred orientation.
3. Flow laws: the general Arrhenius power law (definition; Book 3 ch. 16's
   power-law creep proposition recalled and generalised); stress exponent,
   grain-size exponent, activation energy recalled from chemistry;
   homologous temperature; effective viscosity (proposition); strength
   profiles revisited (Book 3's strength envelope with real flow laws).
4. Deformation mechanism maps: boundary between dislocation and diffusion
   creep (proposition: equal strain rates); reading a map for olivine and
   quartz (figdata); palaeopiezometers (recrystallised grain size vs
   stress).
5. Shear zones: the shear-zone profile, strain softening, mylonites (recall
   Book 3's descriptive definition); kinematic indicators (S--C fabrics,
   σ/δ porphyroclast systems, mica fish, shear bands); sense of shear;
   strain from a deflected marker (γ = tan ψ, recall Book 3's simple shear).
6. `inthelab`: a gas-medium deformation apparatus (third person).

**Definitions.** dislocation (crystal defect); dislocation creep; diffusion
creep; grain-boundary sliding; pressure solution; dynamic recrystallisation;
recovery (crystal plasticity); subgrain; crystallographic preferred
orientation; flow law; stress exponent; homologous temperature; deformation
mechanism map; palaeopiezometer; shear zone; strain softening; kinematic
indicator; sense of shear; S--C fabric; porphyroclast system; mica fish.
Owner check: flow law, deformation map, kinematic indicators are Y3's
(OUTLINE); Sync 1 gives foliation, schistosity and mylonite (descriptive) to
Book 3 ch. 17 with mechanisms here (recalled, not re-defined); Book 3 uses
"shear zone" in prose only (ch. 16--17) with "studied in the Year 3 volume";
chemistry owns point defect and activation energy; "dislocation" appears in
chemistry text only (not indexed), hence the qualified "dislocation (crystal
defect)".

**Recall.** Stress and strain tensors, shear strain, simple shear, strength
envelope, BDT, power-law creep (Book 3 ch. 16); mylonite, foliation,
lineation, stretching lineation (Book 3 ch. 17); Arrhenius law, activation
energy, point defect (chemistry b1/b3); diffusion coefficient (physics b2).

**Figures.** [S] edge dislocation glide (lattice sketch); [S] diffusion
creep paths (Nabarro--Herring through grains, Coble along boundaries);
[F] `flow_laws` strain rate vs stress for quartz, olivine (wet/dry) at three
temperatures; [F] `deformation_map` olivine deformation mechanism map
(grain size vs stress, strain-rate contours); [F] `flow_laws` strength vs
depth for a quartz crust over an olivine mantle (two geotherms); [S]
kinematic indicators gallery (S--C, σ-clast, δ-clast, mica fish) with
sense arrows; [P] a mylonite thin section or a sheared outcrop (Commons,
CC to verify); [AI] a rock-deformation press in a laboratory (generic).

**Ledger.** Flow-law parameters: quartz (Hirth et al. 2001, open?), olivine
(Hirth & Kohlstedt 2003, AGU monograph; check open copy), wet/dry;
piezometer calibration (Stipp & Tullis 2003, GRL); homologous temperatures
(melting points from ledger); diffusion coefficients if quoted.

**Datasets.** None.

**Weekend problem: "The Varden shear zone."** A ductile shear zone at depth
under the Varden granite (invented, at 15 km in the past). Part I: γ from a
deflected dyke; strain ellipse axes. Part II: stress from recrystallised
quartz grain size (piezometer). Part III: strain rate from the quartz flow
law at that stress and 450 °C; effective viscosity. Part IV: time to
accumulate the observed γ; compare with a plate-boundary slip rate.
**Named number: the time the shear zone took to accumulate its strain, in
thousand years.**

---

## Ch. 8 Structural Analysis --- `structural-analysis`

**Hook.** A geologist has measured two hundred bedding planes on the limbs of
a fold too large to see whole. Plotted as poles on a stereonet, the points
fall on one great circle, whose pole is the fold axis, which has never been
seen.

**Sections.**
1. Stereographic projection: projecting the lower hemisphere; equal-angle
   (Wulff) and equal-area (of the sphere, Schmidt) projections (theorems:
   r = R tan(θ/2) and r = R√2 sin(θ/2), the conformal and area-preserving
   properties derived); planes as great circles, lines as points, poles to
   planes; angle between planes; rotation about an axis (method box). Book 3
   ch. 18's pointer is honoured here (its text says "Year 2": defect
   reported).
2. Fold analysis: π-diagram and β-axis; best fit by the orientation tensor
   (theorem: eigenvector of smallest eigenvalue for a girdle; recall Book 3's
   mean orientation); cylindrical fold test; the Varden folds (shared
   `limb_attitude`) as the worked case; axial plane from two limbs.
3. Finite strain analysis: strain ellipse from deformed objects (R_f/φ
   told, Fry method), strain ellipsoid and Flinn diagram; recall Book 3's
   stretch and strain ellipse.
4. Palaeostress: Wallace--Bott hypothesis; resolved shear stress direction
   on a plane (theorem, from the stress tensor); fault-slip inversion
   (least-squares, recall ch. 1); stress ratio; P/T axes recalled from
   Book 3's focal mechanisms; Andersonian regimes (recall).
5. Restoration: balanced cross-sections recalled from Book 4 (line length,
   area); section restoration, pin lines, kink-band construction; depth to
   detachment from excess area (proposition).
6. `inthefield`: measuring attitudes with a compass-clinometer and a phone
   (third person).

**Definitions.** stereographic projection; equal-angle net; equal-area
projection (of the sphere); pole (to a plane); pi-diagram; beta-axis;
orientation tensor; finite strain analysis; Fry method; palaeostress;
fault-slip inversion; Wallace--Bott hypothesis; stress ratio; section
restoration; pin line; kink-band method. Owner check: g9 owns
"equal-area projection" (map sense): qualified form; Book 3 owns great
circle, small circle, trend, plunge, mean orientation, fold elements;
Book 4 owns balanced cross-section, décollement; Book 3 owns P/T axes.

**Recall.** Great/small circle, spherical triangle (Book 3 ch. 1); strike,
dip, attitude, trend and plunge (Book 3 ch. 4/6); fold elements, Anderson's
theory (Book 3 ch. 17); strain ellipse, principal stresses, Coulomb (Book 3
ch. 16); P and T axes, focal mechanism (Book 3 ch. 18); balanced
cross-section, décollement (Book 4 ch. 13); eigenvectors of a symmetric
matrix (math b2).

**Figures.** [S] projection geometry (sphere, plane, projection point);
[F] `stereonet` Wulff and Schmidt nets drawn from the formulas (primitive,
great and small circles every 10°); [F] `stereonet` π-diagram of the Varden
limb poles (from `region.limb_attitude` + scatter) with the best-fit girdle
and β-axis; [F] `palaeostress` fault-slip data (tangent-lineation plot) and
the inverted σ1/σ3; [S] Flinn diagram; [S] kink-band restoration of a
fault-bend geometry; [AI] a geologist's compass-clinometer on a bedding
plane (generic, no recognisable place).

**Ledger.** None beyond formulas (Varden data are invented); one open source
for the stereographic projection's properties is not needed (derived).

**Datasets.** None.

**Weekend problem: "Folds and faults of the Varden Hills."** All data from
`region.py` (+ invented scatter). Part I: plot the limb poles, find the
π-girdle and the β-axis. Part II: orientation-tensor eigenvalues; is the
fold cylindrical? Part III: slip data on the normal fault and small faults:
invert for σ1, σ3 and the stress ratio. Part IV: restore section A--B across
the fault; shortening of the folded cover. **Named number: the plunge of the
Varden fold axis, in degrees** (exact from `region.py`: 2°, recovered from
the scattered data to the precision the data allow).

---

## Ch. 9 Extensional and Strike-Slip Tectonics --- `extension-strike-slip`

**Hook.** In the Basin and Range, mountain blocks tilt like fallen books; in
the cores of some ranges, rocks that flowed at 15 km depth now lie at the
surface under a single, gently dipping fault. How does a continent pull apart?

**Sections.**
1. Rift models: Book 4's stretching (pure-shear) model recalled; the
   simple-shear (detachment) model and its asymmetric margins; necking and
   depth-dependent stretching (told); rift-flank uplift.
2. Normal-fault geometry: planar domino faulting (theorem: extension
   β = sin(θ_0)/sin(θ) for rigid dominoes rotating from θ_0 to θ, derived);
   listric faults and rollover anticlines (constant-heave construction,
   method box); transfer zones; half-grabens (recall Book 3).
3. Metamorphic core complexes: detachment faults, footwall mylonites
   (recall ch. 7), rolling hinge (isostatic footwall rotation); low-angle
   normal fault paradox (Anderson recalled, friction argument).
4. Strike-slip systems: Riedel shears in a simple-shear zone (angles from
   Coulomb, derived); restraining and releasing bends, flower structures;
   pull-apart basins (geometry, length vs offset); transpression and
   transtension (strain partitioning told).
5. Real systems taught from sourced maps (ledger per number): the Basin and
   Range, the Dead Sea pull-apart, the San Andreas big bend.
6. `inthefield`: mapping a detachment fault surface (third person).

**Definitions.** simple-shear rift model; detachment fault; listric fault;
rollover anticline; domino faulting; metamorphic core complex; rolling
hinge; transfer zone; restraining bend; releasing bend; pull-apart basin;
flower structure; Riedel shear; transpression; transtension. Owner check:
Book 4 owns stretching model, rift basin, décollement; Book 3 owns graben,
half-graben, continental rift, strike-slip fault, dextral/sinistral,
transform fault; "accommodation zone" avoided (homograph of accommodation:
"transfer zone" used).

**Recall.** Normal, strike-slip and transform faults, Anderson (Book 3
ch. 13, 17); Coulomb criterion (Book 3 ch. 16); stretching model, rift basin
(Book 4 ch. 16); shear zone, mylonite (ch. 7 and Book 3); isostasy (Book 3).

**Figures.** [S] pure-shear vs simple-shear rift cross-sections; [F]
`domino_extension` extension β vs fault dip for initial dips 45°, 60°, 70°;
[S] listric fault with rollover (constant-heave construction); [S] core
complex anatomy with rolling hinge; [S] Riedel geometry in a dextral shear
zone (R, R', P, T); [S] restraining/releasing bends + pull-apart plan view;
[F] `pullapart` length-to-width data vs offset (ledger compilation) or
analytic geometry only; [P] a core-complex or Basin-and-Range aerial photo
(USGS/NASA PD, verify); [AI] none.

**Ledger.** Basin and Range extension (open review); Dead Sea basin size and
offset (Garfunkel; open source); San Andreas slip rates (USGS); pull-apart
aspect-ratio compilation (Aydin & Nur 1982; check open copy, else drop the
data plot).

**Datasets.** None.

**Weekend problem: "The Merrow half-graben."** An invented rift border. Part
I: domino blocks: β from rotated bedding. Part II: a listric fault: depth to
detachment from rollover geometry. Part III: core-complex footwall: exhumation
from mineral pressures (recall Book 4 geobarometry), rolling-hinge rotation.
Part IV: a releasing bend on a transfer fault: pull-apart length from offset
and rate. **Named number: the horizontal extension across the half-graben,
in kilometres.**

---

## Ch. 10 Thrust Belts and Orogenic Wedges --- `orogenic-wedges`

**Hook.** Push a bulldozer into wet sand: a wedge builds ahead of the blade,
always with the same surface slope. Mountain fronts from Taiwan to the Zagros
behave the same way, and the slope tells how weak their base is.

**Sections.**
1. Thrust geometry: ramps and flats, fault-bend folds (Suppe's relation
   stated, `\admitted` beyond the kink-band construction of ch. 8),
   fault-propagation and detachment folds; duplexes; in- and
   out-of-sequence thrusting (recall Book 4's thin-skinned tectonics).
2. Critical-taper theory: force balance on a wedge (theorem: the small-angle
   critical taper α + β = (β_b + ...) for a Coulomb wedge with pore-fluid
   ratios, derived from the stress state, Mohr construction); sub-, critical
   and supercritical wedges; frontal accretion vs tectonic underplating;
   what the observed taper says about basal friction and fluid pressure.
3. Exhumation and erosion: wedge flux balance (accretionary flux =
   erosional flux at steady state, proposition); exhumation recalled from
   Book 4.
4. Thermochronology: closure temperature and cooling age recalled (Book 3);
   thermochronometers ordered by closure temperature (ledger); age--elevation
   relationships (proposition: slope = exhumation rate under steady state);
   advection of isotherms (thermal Péclet number from ch. 5); fission-track
   and (U--Th)/He physics deferred to ch. 13 (same-book `\cref`).
5. Real wedges from sourced data: Taiwan, the Zagros or the Himalayan front
   (taper angles, ledger).

**Definitions.** critical taper; critical-taper equation (thm.); frontal
accretion; tectonic underplating; ramp (thrust); flat (thrust); duplex
(thrust); out-of-sequence thrust; fault-bend fold; fault-propagation fold;
detachment fold; thermochronology; thermochronometer; age--elevation
relationship. Owner check: critical taper is Y3's (OUTLINE); Book 4 owns
thin/thick-skinned tectonics, décollement, fold--thrust belt, nappe, klippe,
foreland basin, exhumation, exhumation rate, "mafic underplating" (hence
"tectonic underplating"); Book 3 owns closure temperature, cooling age.

**Recall.** Coulomb criterion, effective stress, pore-fluid pressure,
Byerlee (Book 3 ch. 16); thrust fault, vergence (Book 3 ch. 17); décollement,
fold--thrust belt, balanced cross-section (Book 4 ch. 13); exhumation
(Book 4 ch. 11); closure temperature, cooling age (Book 3 ch. 25); kink
method (ch. 8); thermal Péclet number (ch. 5).

**Figures.** [S] ramp--flat geometry and fault-bend fold; [S] duplex
development (three stages); [S] wedge geometry (α, β, stresses); [F]
`critical_taper` α vs β for three basal fluid-pressure ratios with ledger
wedges plotted; [F] `age_elevation` synthetic age--elevation profiles for
three exhumation rates (steady-state thermal model) + closure isotherm
deflection; [S] thermochronometer closure temperatures on a geotherm;
[P] a sandbox wedge experiment photo (Commons/USGS if a verified CC/PD one
exists) or none; [AI] an analogue sandbox model in a laboratory (generic).

**Ledger.** Davis, Suppe & Dahlen 1983 (JGR) parameters; Taiwan and other
wedge tapers (open sources); closure temperatures of AHe, AFT, ZHe, ZFT,
Ar--Ar mica (Reiners & Brandon 2006 review, open?); a real age--elevation
profile (primary open paper).

**Datasets.** None.

**Weekend problem: "The front of the Tessin wedge."** An invented thrust
wedge. Part I: thrust geometry: shortening from a fault-bend fold. Part II:
critical taper: from surface slope and décollement dip, infer the basal
fluid-pressure ratio. Part III: flux balance: accretion vs erosion. Part IV:
thermochronology: an apatite age--elevation transect gives the exhumation
rate; compare with the flux prediction. **Named number: the exhumation rate,
in millimetres per year.**

---

## Ch. 11 Thermodynamics of Rocks --- `petrological-thermodynamics`

**Hook.** A garnet in a schist grew zone by zone as its rock was buried. With
a table of Gibbs energies and a computer, petrologists turn its composition
into the pressure and temperature of each stage.

**Sections.**
1. Chemical potential and Gibbs energy recalled from chemistry; equilibrium
   of a mineral reaction ΔG(P,T) = 0; ΔG from tabulated ΔH, S, V (theorem:
   integration with constant ΔV, ΔCp neglected then included); the
   Clapeyron slope recalled (Book 4) and recomputed.
2. The phase rule in rocks: chemistry's variance and phase rule recalled
   (chemistry b2 owns them); Goldschmidt's mineralogical phase rule
   (proposition); Schreinemakers analysis of an invariant point (method).
3. Solid solutions: ideal site-mixing activity models (proposition a =
   X^n for one site); G--X diagrams; solvus and exsolution (regular solution,
   proposition: critical temperature W/2R); feldspar and pyroxene examples;
   ternary diagrams recalled from Book 4 (cotectic).
4. Thermobarometry: geothermometers and geobarometers recalled (Book 4);
   equilibrium constant of an exchange reaction (garnet--biotite Fe--Mg),
   internally consistent datasets; GASP barometer (stated with ledger
   coefficients).
5. Pseudosections (principle): Gibbs energy minimisation for a fixed bulk
   composition; isopleths; effective bulk composition; reading a published
   pelite pseudosection (redrawn schematic, ledger source).

**Definitions.** mineralogical phase rule; Gibbs energy--composition
diagram; internally consistent thermodynamic dataset; site-mixing activity
model; solvus; exsolution (mineral); Schreinemakers analysis; pseudosection;
effective bulk composition; isopleth (pseudosection); Gibbs energy
minimisation. Owner check: **chemistry b2 owns variance and the phase-rule
theorem** (`def:b2:equilibrium-shifts:variance`,
`thm:b2:equilibrium-shifts:phase-rule`): Sync 2's "Y3 keeps the phase rule"
is amended to "Y3 recalls the phase rule and defines Goldschmidt's
mineralogical form" (report item 2); Book 4 owns ternary phase diagram,
cotectic, Clapeyron slope (of a reaction), univariant reaction, invariant
point, geothermometer, **geobarometer**, metamorphic facies; chemistry owns
Gibbs energy, chemical potential, activity, miscibility gap, lever rule,
solid solution (chemistry sense).

**Recall.** Gibbs energy, chemical potential, activity, equilibrium constant,
variance and phase rule, miscibility gap, binary diagrams (chemistry b1/b2);
Clapeyron slope, univariant reaction, invariant point, facies grid,
geothermometer, geobarometer, P--T--t path (Book 4 ch. 10--11); ternary
diagram, cotectic (Book 4 ch. 7); solid solution (mineral), end-member
(Book 3 ch. 7).

**Figures.** [F] `reaction_line` ΔG(T) at three pressures and the P--T line of
albite = jadeite + quartz (or calcite + quartz = wollastonite + CO2) from
ledger data, with the Clapeyron slope; [F] `al2sio5` the Al2SiO5 triple point
diagram from a dataset (ledger), if the source is open, else schematic;
[F] `gx_solvus` G--X curves of a regular solution at three T and the solvus;
[S] Schreinemakers bundle around an invariant point; [S] redrawn pelite
pseudosection (fields + garnet isopleths, ledger source); [AI] a petrologist
at a polarising microscope beside a computer screen with a phase diagram
(generic).

**Ledger.** Thermodynamic data (Robie & Hemingway 1995, USGS Bulletin 2131,
PD) for albite, jadeite, quartz, kyanite, andalusite, sillimanite;
Al2SiO5 triple point (Holdaway 1971 or Pattison 1992; check access);
garnet--biotite calibration (Ferry & Spear 1978; check access); feldspar
solvus parameters (open source); a published pseudosection (open access).

**Datasets.** None (ledger values only).

**Weekend problem: "The garnet of Varden schist."** The 480-Ma Varden
schist basement carries garnet and biotite. Part I: ΔG of the jadeite
reaction at 300--700 °C; the boundary and its Clapeyron slope. Part II:
the mineralogical phase rule applied to an assemblage; variance. Part III:
garnet--biotite Fe--Mg exchange temperature from the rim compositions. Part
IV: GASP pressure at that temperature; depth of burial. **Named number: the
peak metamorphic pressure of the Varden schist, in kilobars (and its burial
depth).**

---

## Ch. 12 Trace-Element Modelling --- `trace-element-modelling`

**Hook.** Two basalts from the same island, one rich in lanthanum and one
poor. Did they melt from different mantles, or the same mantle melted by
different amounts? Trace elements, which barely notice the major minerals,
answer it.

**Sections.**
1. Partition coefficients and bulk D recalled from Book 4; the mass-balance
   bookkeeping of a melting system; modal and non-modal melting.
2. Batch melting: the Shaw equation C_L/C_0 = 1/(D + F(1 − D)) (theorem,
   derived from mass balance), limits F → 0 and D → 0; non-modal batch
   melting (proposition, `\admitted` details).
3. Fractional melting: instantaneous and aggregated melts (theorem, derived
   by integrating the residue's mass balance); dynamic (critical-porosity)
   melting (told, formula admitted).
4. Crystallisation: Book 4's equilibrium and fractional crystallisation and
   Rayleigh fractionation law recalled; in situ forms told; AFC: DePaolo's
   equation (theorem stated with derivation sketch; AFC term owned by
   Book 4).
5. Reading a spider diagram quantitatively: normalised diagrams and the
   europium anomaly recalled (Book 4); ratio--ratio diagrams (La/Yb vs La);
   inverting F and source composition from two lavas; REE patterns and
   garnet in the source.

**Definitions.** batch melting (thm.); fractional melting (thm.); aggregated
fractional melt; non-modal melting; dynamic melting; ratio--ratio diagram.
Owner check: Sync 2 keeps batch and fractional melting models in Y3; Book 4
owns partition coefficient (mineral--melt), bulk partition coefficient,
compatible/incompatible element, MORB, OIB, normalised diagram, europium
anomaly, partial melting, melt fraction, equilibrium/fractional
crystallisation, Rayleigh fractionation law, **assimilation--fractional
crystallisation** (Book 4 ch. 8 defines it: the DePaolo equation is a Y3
theorem titled by content, not indexed under the term).

**Recall.** Partition coefficients, bulk D, compatible/incompatible, MORB,
OIB, normalised (spider) diagrams, Eu anomaly (Book 4 ch. 3); partial melting,
melt fraction, mantle melting (Book 4 ch. 7); crystallisation models and AFC
(Book 4 ch. 8); CI chondrite (Book 4 ch. 3).

**Figures.** [F] `melting_models` C_L/C_0 vs F for batch and fractional
(instantaneous and aggregated) melting, D = 0.01, 0.1, 1, 10; [F]
`melting_models` chondrite-normalised REE patterns of spinel- vs garnet-
lherzolite melts at F = 1, 5, 20 %; [F] `melting_models` La/Yb vs La
melting trajectories with two invented lavas; [S] melting column with
residue and melt boxes (mass balance); [S] AFC box model; [AI] none (one
generic lava-sampling photo is not needed).

**Ledger.** Partition coefficients for La, Ce, Sm, Yb (olivine, opx, cpx,
garnet, spinel; GERM/earthref compilation or McKenzie & O'Nions 1991 ---
check access); primitive mantle and CI REE (shared or Book 4 rows: reuse);
mantle modes for spinel/garnet lherzolite (open source).

**Datasets.** None.

**Weekend problem: "Two lavas of Aldren Island."** Part I: bulk D for La and
Yb in spinel and garnet lherzolite. Part II: batch melting curves; F from the
La content of lava A. Part III: fractional vs aggregated melting: same
question. Part IV: La/Yb of lava B needs garnet: estimate the depth of
melting and F. **Named number: the degree of melting of lava A, in per cent.**

---

## Ch. 13 Advanced Geochronology --- `advanced-geochronology`

**Hook.** A zircon crystal a tenth of a millimetre long has kept two clocks
running since its granite crystallised, uranium-238 to lead-206 and
uranium-235 to lead-207. When the two disagree, the disagreement itself is
dated.

**Sections.**
1. U--Pb: the two decay chains (ledger λ238, λ235, 238U/235U); concordia
   (theorem: parametric curve derived); discordia from episodic lead loss
   (theorem: mixing line between two concordia points); upper and lower
   intercepts; Tera--Wasserburg diagram; zircon (recall mineral), CA-TIMS
   told (Book 4 owns TIMS).
2. 40Ar/39Ar: neutron activation, the J factor, age equation (theorem);
   step heating, age spectra, plateau ages; excess argon and loss
   (descriptive); recall K--Ar and branching decay (Book 3 ch. 25).
3. Sm--Nd and model ages: CHUR, ε_Nd, depleted mantle recalled (Book 4
   ch. 4); model age T_CHUR and T_DM (theorem: from the isotope evolution
   equation); crustal residence ages.
4. Low-temperature chronometers: fission-track dating (age equation
   derived, track annealing, length distributions); (U--Th)/He (production
   equation, α-ejection told, partial retention zone); closure temperature
   and cooling age recalled (Book 3); used in ch. 10.
5. Cosmogenic nuclides: production by spallation, production rate scaling
   with altitude and latitude (told, ledger); exposure age with decay
   (theorem: N(t) = P/λ (1 − e^{−λt}) and with erosion; Book 3's
   steady-erosion proposition recalled and generalised); burial dating told.
6. Statistics of ages: weighted mean, MSWD (definition + proposition:
   expectation 1), York regression of isochrons (method), propagating decay
   constant uncertainties.

**Definitions.** concordia; discordia; upper intercept; lower intercept;
Tera--Wasserburg diagram; 40Ar/39Ar dating; J factor; age spectrum; plateau
age; model age; cosmogenic nuclide; exposure age; production rate
(cosmogenic); fission-track dating; track annealing; (U--Th)/He dating;
partial retention zone; mean square of weighted deviates. Owner check:
concordia and model age are Y3's (OUTLINE; Book 4 forward list); Book 3
owns parent isotope, radiogenic daughter, isochron, initial ratio, branching
decay, closure temperature, cooling age, radiocarbon; Book 3 ch. 20 states
the steady-erosion cosmogenic proposition without defining "cosmogenic
nuclide" (checked: not indexed); Book 4 owns CHUR, epsilon notation,
depleted mantle, TIMS, MC-ICP-MS, isotope dilution, mass bias.

**Recall.** Radioactive decay, half-life (physics/g12); isochron, initial
ratio, branching decay, closure temperature, cooling age (Book 3 ch. 25);
CHUR, ε notation, depleted mantle, crustal growth curve (Book 4 ch. 4);
TIMS, isotope dilution (Book 4 ch. 31); weighted mean, χ² (math/chemistry);
weighted least squares (ch. 1); denudation rate and the steady-erosion
nuclide formula (Book 3 ch. 20).

**Figures.** [F] `concordia` Wetherill concordia 0--4.5 Ga with a discordia
for the Varden granite (310 Ma, lead loss at a later event) and error
ellipses; [F] `concordia` Tera--Wasserburg version; [F] `arar_spectrum`
synthetic step-heating spectrum with plateau and argon-loss shape; [F]
`model_ages` ε_Nd evolution with CHUR and DM lines, T_CHUR and T_DM read; [F]
`cosmogenic` 10Be concentration vs exposure time for erosion rates 0, 1, 10
m/Myr (steady state reached); [S] fission-track etching and counting; [P]
a CL image of zoned zircon (Commons/USGS, verify) or none; [AI] a clean lab
with a mass spectrometer (generic).

**Ledger.** Decay constants λ238, λ235, λ40K (branches), λ147Sm, λ10Be,
238U/235U (Steiger & Jäger 1977; Jaffey 1971; Hiess 2012 open?; Chmeleff
2010 / Korschinek 2010 for 10Be; check open copies; IUPAC-IUGS 2023
recommendation if open); CHUR and DM parameters (Book 4 rows reused);
10Be SLHL production rate (open source, e.g. CRONUS documentation);
fission-track ζ and annealing (open); closure temperatures (ch. 10 rows).

**Datasets.** None.

**Weekend problem: "Zircons of the Varden granite."** Part I: five zircon
analyses (invented, consistent with 310 Ma) on concordia; discordia fit.
Part II: upper intercept with uncertainty; MSWD. Part III: lower intercept
interpreted (a Cretaceous fluid event); Ar--Ar biotite plateau of the same
granite. Part IV: AHe ages vs elevation in the Varden hills; exhumation and
erosion rates; a 10Be erosion rate on the granite top as a cross-check.
**Named number: the upper-intercept age of the Varden granite, in millions
of years (with its 2σ).**

---

## Ch. 14 Stable-Isotope Geochemistry --- `stable-isotopes`

**Hook.** Snow falling on the centre of East Antarctica is the lightest water
on Earth. Each molecule has lost its heavy isotopes, step by step, since it
left the ocean, and how many it lost depends on how cold the air was.

**Sections.**
1. Fractionation recalled from chemistry (δ value, fractionation factor,
   equilibrium and kinetic isotope effects); capital Δ and 1000 ln α
   (proposition: Δ ≈ 1000 ln α ≈ δ_A − δ_B); temperature dependence
   (ledger calibrations); mass-dependent fractionation (three-isotope plot).
2. Rayleigh distillation in the water cycle: theorem R/R_0 = f^{α−1} for
   the vapour, the condensate's δ (derived); temperature, amount and
   continental effects; deuterium excess; the meteoric water line recalled
   (Book 4) and explained.
3. Palaeothermometry: carbonate--water fractionation and the
   palaeotemperature equation (ledger calibration); the ice-volume effect
   recalled (Book 4); Mg/Ca recalled (Book 4) as an independent check;
   clumped isotopes (Δ47, principle and calibration, ledger).
4. Carbon isotopes: biological fractionation (photosynthesis, ledger),
   carbon isotope mass balance (proposition: δ_in = f_org δ_org + (1 −
   f_org) δ_carb), organic burial fraction; carbon isotope excursions (PETM
   recalled from Book 4: input mass from the CIE size, proposition).
5. Sulfur isotopes and the oxygenation record: bacterial sulfate reduction
   recalled from biology; mass-independent fractionation of S (Δ33S) and its
   disappearance at the Great Oxidation Event (Book 4 ch. 18 recalled).
6. `inthelab`: a gas-source isotope-ratio mass spectrometer and an ice-core
   sampling line (third person).

**Definitions.** isotopic difference (capital delta); Rayleigh distillation
(prop.); deuterium excess; temperature effect (isotopic); amount effect;
continental effect; palaeothermometry; palaeotemperature equation; clumped
isotopes; carbon isotope excursion; carbon isotope mass balance (prop.);
organic carbon burial fraction; mass-dependent fractionation;
mass-independent fractionation. Owner check: palaeothermometry stays Y3's
(Sync 2); δ value and fractionation factor are chemistry's (Sync 2); VSMOW,
VPDB, meteoric water line are Book 4's; Book 4's Rayleigh fractionation law
is the elemental form (Book 4 notes "Y3 Rayleigh distillation is the
isotopic form"); Book 4 owns PETM, hyperthermal, GOE, ice-volume effect,
Mg/Ca, climate proxy, age model; biology owns sulfate reduction,
photosynthesis.

**Recall.** δ value, fractionation factor, equilibrium and kinetic isotope
effects (chemistry b3); isotope reference standard, meteoric water line
(Book 4 ch. 4); Rayleigh fractionation law (Book 4 ch. 8); climate proxy,
ice-volume effect, Mg/Ca (Book 4 ch. 24); PETM (Book 4 ch. 26); GOE (Book 4
ch. 18); sulfate reduction, photosynthesis (biology).

**Figures.** [F] `rayleigh_distillation` δ18O of vapour and condensate vs
remaining fraction f, with temperature along the path, for α(T); [F]
`rayleigh_distillation` the δD--δ18O plot of the modelled precipitation vs the
GMWL; [F] `lr04_d18o` LR04 benthic δ18O (shared) with the ice-volume share
marked; [F] `carbon_mass_balance` δ13C of carbonate vs f_org; PETM
excursion size vs source δ13C and mass; [S] three-isotope plot (MDF line vs
MIF); [F] `s_mif` Δ33S vs age schematic data from a ledger compilation, or
[S] if no open table; [AI] an ice-core drilling tent on a polar plateau
(generic); [P] an ice core section (NOAA/NSF PD, verify).

**Ledger.** Oxygen fractionation calibrations (water vapour--liquid
Majoube 1971; calcite--water Kim & O'Neil 1997; check open copies; else an
open review quoting them --- not Wikipedia); Dome C/Vostok δD and
temperature slopes (EPICA papers, open); GMWL (Craig 1961; Book 4 row
reused); Δ47 calibration (an open paper); photosynthetic ε (open review);
PETM CIE size and carbon mass (Book 4 rows or open papers; AR6 if quoted);
Δ33S record (Farquhar et al. 2000; check open).

**Datasets.** Shared `lr04` (and optionally `edc`).

**Weekend problem: "A raindrop's journey to Dome Ilse."** An invented
coast-to-dome traverse. Part I: Rayleigh distillation from ocean vapour;
δ18O at three stations given f. Part II: temperatures along the path and the
δ--T slope; deuterium excess. Part III: a foraminifer palaeotemperature: δ
of calcite, ice-volume correction, temperature. Part IV: carbon mass
balance of an excursion in the same core. **Named number: δ18O of the snow
at the dome, in per mil.**

---

## Ch. 15 Water--Rock Interaction --- `water-rock-interaction`

**Hook.** A spring at the foot of a limestone cliff leaves a crust of
travertine on every twig it touches; a stream draining granite carries silica
and sodium but no crust. The water's chemistry is a record of the rock it
crossed.

**Sections.**
1. Speciation in natural waters recalled from chemistry (activity, ionic
   strength, Debye--Hückel/Davies, speciation, alkalinity); a water analysis
   and its charge balance (method).
2. Saturation: chemistry's saturation state Ω recalled; saturation index
   SI = log(IAP/K) (definition, qualified); calcite, gypsum, quartz examples.
3. Carbonate equilibria applied to rocks: open and closed carbonate systems
   (theorems: calcite solubility vs P_CO2 derived for both); soil CO2 and
   karst; degassing and travertine; ocean carbonate chemistry recalled
   (chemistry b3), lysocline and CCD recalled (Book 3).
4. Silicate weathering kinetics: transition-state rate law for mineral
   dissolution (chemistry's rate theory recalled), far-from-equilibrium
   rates, lab vs field rates (ledger); weathering-limited and supply-limited
   regimes; activity diagrams (kaolinite--gibbsite--K-feldspar; recall Book
   3's bisiallitisation etc.).
5. Hydrothermal fluids: recall Book 4's hydrothermal fluid; water--rock
   ratios from isotope shifts (proposition: mass balance of 18O between rock
   and water), reaction-path models (principle).

**Definitions.** saturation index (of a mineral); open carbonate system;
closed carbonate system; activity diagram (mineral stability); mineral
dissolution rate law; weathering-limited regime; supply-limited regime;
water--rock ratio; reaction-path model. Owner check: chemistry owns
activity, activity coefficient, ionic strength, speciation, solubility
product, alkalinity, **saturation state**, rate law, transition state;
Book 3 owns weathering, hydrolysis (of silicates), clay minerals, lysocline,
CCD; Book 4 owns hydrothermal fluid; Book 2 owns hydrothermal circulation.

**Recall.** Activity, ionic strength, solubility product, speciation,
alkalinity, saturation state, Henry's law, rate law, Arrhenius (chemistry);
chemical weathering, hydrolysis (of silicates), kaolinite (Book 3 ch. 19);
lysocline, CCD (Book 3 ch. 22); hydrothermal fluid (Book 4 ch. 29); δ value
(chemistry); silicate-weathering thermostat (Book 4 ch. 26).

**Figures.** [F] `carbonate_system` calcite solubility (Ca) vs P_CO2 for open
and closed systems at 10 and 25 °C; [F] `carbonate_system` SI along a karst
spring's degassing path; [F] `activity_diagram` log(a_K/a_H) vs log a_SiO2
with kaolinite, gibbsite, muscovite, K-feldspar fields and invented water
samples; [F] `weathering_rates` lab dissolution rates vs pH for albite and
forsterite (ledger parameters); [S] water--rock box model; [P] travertine
terraces (USGS/NPS PD, verify, e.g. Mammoth Hot Springs); [AI] none.

**Ledger.** Equilibrium constants for calcite, CO2 hydration, carbonic acid
dissociation at 10/25 °C (Plummer & Busenberg 1982, or USGS PHREEQC
database file llnl/phreeqc.dat: PD, fetchable); mineral rate parameters
(Palandri & Kharaka 2004, USGS Open-File Report 2004-1068, PD); soil P_CO2
ranges (open source); kaolinite/gibbsite/K-feldspar log K (phreeqc.dat).

**Datasets.** NEW (small): the needed rows of PHREEQC `phreeqc.dat`
(USGS, PD) --- or ledger rows only; no download needed if the ledger cites
the file directly.

**Weekend problem: "The spring below Varden limestone."** The Jurassic
limestone feeds a spring (analysis invented, charge-balanced). Part I:
ionic strength, activity coefficients, charge balance. Part II: speciation
of DIC; P_CO2 of the water vs air. Part III: SI of calcite at the spring
and after degassing to air P_CO2; travertine mass per litre. Part IV: the
granite stream: activity-diagram position; weathering regime. **Named
number: the calcite saturation index of the spring water at its outlet.**

---

## Ch. 16 Sequence Stratigraphy --- `sequence-stratigraphy`

**Hook.** Across a seismic section of a continental margin, reflections lap
onto older ones, then build out, then retreat. The pattern repeats every few
hundred thousand years: sea level and sediment supply have written their
history in the geometry.

**Sections.**
1. Accommodation and supply recalled (Book 3: accommodation, eustasy, relative
   sea level, subsidence); the shoreline's response (proposition: shoreline
   trajectory from the rates of accommodation creation and sediment supply,
   A/S); normal vs forced regression; transgression (Book 4).
2. Stratal geometry: reflection terminations recalled from ch. 2;
   depositional sequence, sequence boundary, transgressive surface, maximum
   flooding surface; systems tracts (lowstand, transgressive, highstand,
   falling-stage); condensed sections; incised valleys.
3. Parasequences and flooding surfaces; stacking patterns
   (progradational, aggradational, retrogradational); a well-log reading
   (forward to ch. 17).
4. Models: a forward model of a shelf profile with sinusoidal sea level and
   steady subsidence (figdata) producing the systems tracts; limits of the
   method (non-uniqueness, the eustasy debate, told with sources).
5. Cyclostratigraphy: Milankovitch parameters recalled (Book 4); periodogram
   of a series (Fourier recalled from math), astronomical tuning; LR04
   (shared) as the worked case; sedimentation rates from cycle thickness.

**Definitions.** depositional sequence; sequence boundary; systems tract;
lowstand / transgressive / highstand / falling-stage systems tract; maximum
flooding surface; transgressive surface; parasequence; flooding surface;
forced regression; normal regression; shoreline trajectory; condensed
section; incised valley; cyclostratigraphy; astronomical tuning;
periodogram. Owner check: systems tract and cyclostratigraphy are Y3's
(OUTLINE; Book 4 brief defers them); Book 3 owns accommodation, eustasy,
relative sea level, subsidence, sedimentary basin; Book 4 owns marine
transgression/regression, first-order sea-level cycle, Milankovitch
parameters/theory, age model; math owns Fourier series/transform
("periodogram" not indexed there: checked).

**Recall.** Accommodation, eustasy, relative sea level, subsidence (Book 3
ch. 23); onlap, downlap, toplap, erosional truncation (ch. 2); marine
transgression/regression, first-order cycle (Book 4 ch. 19); Milankovitch
parameters, climatic precession (Book 4 ch. 25); age model (Book 4 ch. 24);
Fourier series/transform (math b2/b3).

**Figures.** [F] `shelf_model` a 2-D forward model: shoreline trajectory
and stratal surfaces through one sea-level cycle, systems tracts coloured;
[F] `shelf_model` the A/S trajectory diagram; [S] sequence anatomy (SB, TS,
MFS, tracts) on a dip section; [S] parasequence stacking patterns with logs;
[F] `lr04_periodogram` periodogram of LR04 0--1 Ma and 1.2--2.5 Ma (peaks
near the orbital periods; ledger for the La2004 periods); [AI] none; [P] a
coastal cliff of stacked parasequences (Book Cliffs, USGS PD if verified).

**Ledger.** Orbital periods (Laskar et al. 2004, A&A, open); Book Cliffs
facts if photo used (USGS); third-order cycle durations (open review,
cautious wording); eustatic amplitudes (Miller et al. 2005/2020 open?).

**Datasets.** Shared `lr04`.

**Weekend problem: "Sea levels of the Varden basin."** A synthetic
shelf with given subsidence and supply, sinusoidal sea level. Part I:
accommodation rates through the cycle. Part II: shoreline trajectory,
regression and transgression intervals. Part III: identify the systems
tracts on the model output; where the sequence boundary forms. Part IV:
cycle thicknesses in a core → periodogram → sedimentation rate. **Named
number: the maximum basinward shift of the shoreline, in kilometres.**

---

## Ch. 17 Facies Models --- `facies-models`

**Hook.** A core from a well three kilometres deep: a metre of coarse sand
with cross-beds, fining upwards into silt with roots, then sand again. The
geologist reads a river that wandered across its plain, though the nearest
river is now a thousand kilometres away.

**Sections.**
1. Facies, associations, successions: sedimentary facies and depositional
   environment recalled (Book 3); facies model as a summary of many examples;
   Walther's law (theorem with its hypotheses: conformable succession, no
   major break; proof by lateral migration).
2. Fluvial models: braided vs meandering rivers, point bars and
   fining-upward successions, avulsion, floodplain; channel-belt geometry.
3. Deltaic and shelf models: Book 3's delta classes recalled;
   coarsening-upward successions; shoreface, fair-weather and storm wave
   base, hummocky cross-stratification; tidal facies (told).
4. Deep water: turbidites recalled (Book 3); Bouma sequence; submarine fans
   (channel--levée--lobe); contourites (told).
5. Carbonate platforms: carbonate factory, reef, platform recalled (Book 3);
   ramp vs rimmed shelf; facies belts; peritidal cycles.
6. Cores and well logs: wireline logs (gamma-ray, sonic, density, neutron,
   resistivity recalled for ch. 31), log shapes (bell, funnel, cylinder),
   net-to-gross; borehole log recalled (Book 3 ch. 5); porosity from density
   (proposition).

**Definitions.** facies model; Walther's law (thm.); facies association;
facies succession; fining-upward succession; coarsening-upward succession;
braided river; meandering river; point bar; avulsion; shoreface;
fair-weather wave base; storm wave base; hummocky cross-stratification;
submarine fan; Bouma sequence; carbonate ramp; rimmed shelf; wireline log;
gamma-ray log; sonic log; density log; neutron log; net-to-gross ratio.
Owner check: Book 3 owns sedimentary facies, depositional environment,
bedform, cross-bedding, deltas, turbidite, graded bed, carbonate factory,
reef, carbonate platform, borehole log; g5 owns meander, delta; **Walther's
law**: Book 4 ch. 20 cites it in its brief ("re-check Book 3 owner"); no
book defines it --- contested, Y3 claims it as the facies-model chapter's
law (report item 2).

**Recall.** Sedimentary facies, depositional environment, bedforms,
cross-bedding, deltas, turbidite (Book 3 ch. 21); carbonate factory, reef,
platform (Book 3 ch. 22); borehole log, correlation of logs (Book 3 ch. 5);
porosity, permeability (g6); parasequence, systems tracts (ch. 16).

**Figures.** [S] Walther's law: lateral belts → vertical succession; [S]
fluvial block diagrams (braided vs meandering) with logs; [S] delta and
shoreface profile with wave bases; [S] Bouma sequence log + fan plan;
[S] carbonate ramp vs rimmed shelf profiles; [F] `well_logs` synthetic
gamma-ray, density and sonic logs through the Varden cover at a well site
(units and thicknesses from `region.py`) with log shapes; [P] hummocky
cross-stratification or a Bouma sequence outcrop (Commons CC, verify);
[AI] a core store with a geologist logging a split core on a table
(generic).

**Ledger.** Gamma-ray, density and sonic ranges for sandstone, shale,
limestone, chalk (open agency/textbook source); grain density of quartz and
calcite (shared or chemistry ledger); storm/fair-weather wave base depths
(open source, as ranges).

**Datasets.** None (`region.py`).

**Weekend problem: "Varden-2, a well through the cover."** A well in the
syncline. Part I: read the units from the logs (gamma-ray, density). Part
II: porosity from the density log in the sandstone and limestone. Part III:
facies of a cored interval (fining-upward channel fills) and Walther's law to
reconstruct the plain. Part IV: net sand and net-to-gross in the
sandstone. **Named number: the net sand thickness of the Triassic
sandstone at Varden-2, in metres.**

---

## Ch. 18 Quantitative Geomorphology --- `quantitative-geomorphology`

**Hook.** A river in a rising mountain range has a step in its long profile,
a waterfall that climbs upstream a few millimetres a year. Its position is a
clock that started when the uplift did.

**Sections.**
1. Hillslopes: mass conservation for soil; hillslope diffusion (theorem:
   linear transport gives the diffusion equation for elevation; physics'
   diffusion equation recalled); convex hilltops and curvature as an erosion
   rate gauge (proposition: E = −K ∇²z at steady state); soil production
   function; critical hillslope gradient and nonlinear transport (told).
2. River incision: the stream-power law E = K A^m S^n (definition);
   detachment-limited vs transport-limited incision; steady-state profile
   and the channel steepness and concavity indices (theorem: S = (U/K)^{1/n}
   A^{−m/n}); χ analysis (proposition, integral transform of the profile).
3. Transient landscapes: knickpoints migrating as kinematic waves (theorem
   for n = 1: celerity K A^m), base level; response time.
4. Glacial erosion: a glacial erosion law proportional to sliding speed
   (told, ledger), the glacial buzzsaw, U-shaped valleys (recall g8/g9).
5. Tectonics and erosion: topographic steady state; erosional isostatic
   rebound (proposition: peak uplift by unloading of valleys); rates from
   cosmogenic nuclides (ch. 13) and thermochronology (ch. 10).
6. `inthefield`: a terrestrial-lidar survey of a hillslope (third person).

**Definitions.** hillslope diffusion; soil production function; critical
hillslope gradient; stream-power law; steady-state river profile; channel
steepness index; concavity index; chi analysis; knickpoint; base level;
detachment-limited incision; transport-limited incision; glacial erosion law;
glacial buzzsaw; topographic steady state; erosional isostatic rebound.
Owner check: stream-power law is Y3's (OUTLINE); g5 owns weathering,
erosion, deposition, meander; g9 owns landforms, uplift--erosion balance;
g12 owns isostatic rebound; Book 3 owns denudation rate, Shields parameter,
bed shear stress; "base level" not indexed in the school books (checked);
Book 3 owns digital elevation model (recall).

**Recall.** Diffusion equation (physics b2); erosion, landforms (g5/g9);
isostatic rebound (g12); denudation rate, Shields parameter (Book 3 ch. 20);
digital elevation model (Book 3 ch. 4); cosmogenic nuclides (ch. 13);
thermochronology (ch. 10).

**Figures.** [F] `hillslope` diffusive evolution of a fault scarp (profiles
at three ages) + steady convex hill; [F] `stream_profile` steady-state long
profile and its log S--log A plot; [F] `stream_profile` knickpoint
migration after a base-level fall (profiles at four times); [F]
`varden_river` χ plot of the Varden river from `region.river_z` and an
invented tributary network; [S] stream-power regimes; [S] erosional isostasy
(peaks rise as valleys deepen); [P] a knickpoint waterfall (USGS/NPS PD,
verify); [AI] none.

**Ledger.** Hillslope diffusivity values (Fernandes & Dietrich 1997; open
review); stream-power exponents (m/n ≈ 0.45 typical; open review); knickpoint
celerities (a primary open paper); soil production rates (Heimsath et al.
1997, open?).

**Datasets.** None (`region.py` river).

**Weekend problem: "The waterfall of the Varden river."** An invented
base-level fall at the basin outlet. Part I: steady-state profile and
steepness from slope--area data. Part II: K from a known uplift rate. Part
III: knickpoint celerity with n = 1; position after a given time. Part IV:
invert the observed knickpoint position for the age of the base-level fall;
hillslope adjustment above and below. **Named number: the age of the
base-level fall, in thousand years.**

---

## Ch. 19 Geophysical Fluid Dynamics --- `gfd-foundations`

**Hook.** Stir a cup of tea and it stops in a minute. The ocean and the
atmosphere are stirred on a rotating planet, and rotation, with
stratification, makes them obey rules a teacup never sees: winds that blow
along isobars, columns that refuse to tilt.

**Sections.**
1. Equations in a rotating frame: Navier--Stokes, continuity, Coriolis and
   centrifugal terms recalled from physics; the momentum equation on the
   sphere; f and β (f-plane, β-plane); Boussinesq and hydrostatic
   approximations (justified by scale analysis).
2. Scales: Rossby number, Ekman number (definitions + scale analysis);
   geostrophic balance recalled from Book 3 and derived as the Ro → 0 limit;
   inertial oscillations (theorem: circles of radius U/f, period 2π/f);
   gradient wind (proposition: curvature correction).
3. Rotation without stratification: the Taylor--Proudman theorem (derived);
   Taylor columns (told, lab photograph or schematic).
4. Stratification: buoyancy frequency N (theorem: oscillation of a displaced
   parcel, recall Book 3's static stability and potential temperature);
   barotropic vs baroclinic fluids; thermal wind (theorem: ∂u_g/∂z =
   −(g/fT) ∂T/∂y derived from geostrophy + hydrostatics); jet streams
   (Book 3) explained.
5. The Rossby radius of deformation L_R = NH/f (proposition) and the scale of
   weather systems and ocean eddies.
6. `inthelab`: a rotating-tank experiment (third person).

**Definitions.** Rossby number; Ekman number; Boussinesq approximation;
hydrostatic approximation; f-plane; beta-plane; Taylor--Proudman theorem
(thm.); thermal wind (thm.); barotropic fluid; baroclinic fluid; buoyancy
frequency; Rossby radius of deformation; inertial oscillation; gradient
wind. Owner check: Rossby number and thermal wind are Y3's (OUTLINE, Sync 2);
Book 3 owns Coriolis parameter, geostrophic wind, geostrophic balance,
pressure-gradient force, potential temperature, static stability, jet
stream; physics owns Coriolis force, Navier--Stokes, vorticity, Reynolds
number, viscosity, hydrostatic relation; buoyancy frequency is listed in
Book 3's forward list to Y3.

**Recall.** Coriolis and centrifugal forces (physics b1 non-inertial
frames); Navier--Stokes, continuity equation, Reynolds number, viscosity
(physics b2); hydrostatic relation (physics b1 fluid statics); Coriolis
parameter, geostrophic wind, PGF, jet streams (Book 3 ch. 28); potential
temperature, static stability, stable stratification (Book 3 ch. 26).

**Figures.** [S] rotating frame and the local tangent plane (f, β); [F]
`inertial_oscillation` trajectory of a parcel released with velocity U on an
f-plane (+ drifting with weak friction); [S] Taylor column over an obstacle;
[S] thermal-wind geometry (sloping isobaric surfaces); [F] `thermal_wind`
zonal-mean u from a meridional temperature section (idealised, ledger-scaled)
compared with jet speed; [F] `buoyancy_frequency` N(z) from the standard
atmosphere and an ocean profile (ledger); [P] a rotating-tank Taylor column
(Commons CC, verify) or none; [AI] a rotating-table laboratory experiment
(generic).

**Ledger.** Earth rotation rate (shared `earth:Trot` or const); standard
atmosphere temperatures (Book 3 rows, reuse); a typical ocean density
profile (open source/WOA summary); jet speeds and meridional temperature
gradients (open source).

**Datasets.** None.

**Weekend problem: "Winds over the Steppe of Orrin."** An invented
mid-latitude section. Part I: Rossby and Ekman numbers for five flows (a
bathtub, a sea breeze, a cyclone, a gyre, the core). Part II: geostrophic
wind from a pressure map; gradient wind correction. Part III: buoyancy
frequency and Rossby radius. Part IV: thermal wind from the meridional
temperature gradient; wind at the tropopause. **Named number: the
geostrophic wind at 10 km derived by thermal wind, in metres per second.**

---

## Ch. 20 Atmospheric Dynamics --- `atmospheric-dynamics`

**Hook.** On a winter weather map the jet stream meanders around the
hemisphere in four to six great waves that drift slowly westward relative to
the wind. Why that many, and why do they move the wrong way?

**Sections.**
1. Vorticity: relative, planetary, absolute vorticity (physics' vorticity
   recalled); the barotropic vorticity equation (theorem from the
   shallow-water/2-D equations); potential vorticity and its conservation
   (theorem, shallow-water form; Ertel form told).
2. Rossby waves: the dispersion relation ω = Uk − βk/(k² + l²) derived
   (the Rossby wave term owned by Book 4 is recalled: theorem titled
   "Dispersion of Rossby waves"); westward phase speed; stationary
   wavelength (proposition); group velocity and downstream development;
   topographic forcing.
3. Baroclinic instability: available potential energy (definition, told
   with a two-layer argument); the Eady model (growth rate σ = 0.31 U_z f/N
   stated, derivation `\admitted` past the setup); fastest-growing
   wavelength ~ L_R; cyclones as eddies (recall Book 4's extratropical
   cyclone).
4. The general circulation: zonal means and eddies; eddy fluxes of heat
   and momentum; angular momentum and the Hadley cell (recall Book 3);
   the Held--Hou model (theorem: angular-momentum-conserving wind and the
   cell's poleward extent, derived in the small-angle limit).
5. `history`: from Rossby's 1939 paper to numerical prediction (ledger).

**Definitions.** relative vorticity; planetary vorticity; absolute
vorticity; potential vorticity; barotropic vorticity equation (thm.);
Rossby-wave dispersion relation (prop.); stationary Rossby wavelength;
baroclinic instability; Eady model; available potential energy; eddy
(atmospheric); zonal mean; Held--Hou model; atmospheric angular momentum.
Owner check: Sync 2: Book 4 ch. 22 owns "Rossby wave" (descriptive), Y3
owns the dynamics: the dispersion relation is indexed under its own name,
the term recalled; Book 3 owns Hadley/Ferrel/polar cells, jets, trade winds,
westerlies; Book 4 owns extratropical cyclone, cyclogenesis, upper-level
trough/ridge, blocking, NWP; physics owns vorticity and circulation.

**Recall.** Vorticity, circulation (physics b2); Rossby wave, upper-level
trough/ridge, extratropical cyclone (Book 4 ch. 22); Hadley cell, jet
streams, westerlies (Book 3 ch. 28); f, β, Rossby radius, thermal wind
(ch. 19); meridional heat transport (Book 3 ch. 27).

**Figures.** [S] vorticity of a parcel moving north (conservation of
absolute vorticity → Rossby restoring mechanism); [F] `rossby_waves`
dispersion relation ω(k) and phase/group velocities for U = 0 and U = 15 m/s;
stationary wavenumber vs latitude; [F] `rossby_waves` a meandering
streamfunction pattern on a β-plane (snapshot); [F] `eady` Eady growth rate
vs wavenumber; [F] `held_hou` angular-momentum wind and Hadley-cell edge vs
the observed (ledger); [S] eddy heat flux: warm poleward, cold equatorward;
[P] a satellite image of a baroclinic wave/cyclone (NASA/NOAA PD, verify);
[AI] none.

**Ledger.** Typical jet speed, β at 45°, scale height values (shared/Book 3
rows); observed Hadley-cell edge latitude (open source); Rossby 1939 (J.
Mar. Res., open archive) for the history box; an observed stationary
wavenumber climatology (open source, optional).

**Datasets.** None.

**Weekend problem: "The wave that stood still."** Part I: absolute
vorticity of a parcel displaced from 45°N to 50°N. Part II: Rossby dispersion:
phase speed of wavenumbers 3--8 at 45°N in a 15 m/s westerly. Part III:
stationary wavelength and number of waves round the latitude circle. Part
IV: Eady growth: e-folding time and wavelength of the fastest mode for given
shear and N. **Named number: the e-folding time of the fastest-growing
Eady mode, in days.**

---

## Ch. 21 Ocean Dynamics --- `ocean-dynamics`

**Hook.** The Gulf Stream carries a hundred times the flow of all the
world's rivers past Cape Hatteras, hugging the western edge of the
Atlantic. There is no matching current off Portugal. The asymmetry is a
consequence of the Earth being round and rotating.

**Sections.**
1. The Ekman layer derived: the Ekman solution (theorem titled by content:
   velocity spiral derived; Book 3 owns "Ekman spiral", "Ekman transport",
   "Ekman layer" --- recalled, not re-indexed); Ekman depth; transport at
   right angles to the wind (derived); Ekman pumping (proposition: w_E =
   curl(τ/ρf)); coastal upwelling recalled.
2. Sverdrup balance: theorem β V = curl(τ)/ρ derived from vorticity
   (ch. 20); the Sverdrup transport of a subtropical gyre (figdata with
   idealised zonal winds); Sverdrup units recalled (Book 3).
3. Western intensification: the Stommel model (theorem: streamfunction
   with bottom friction solved; boundary-layer width r/β); the Munk
   boundary layer (told, width (A/β)^{1/3}); why the boundary is western
   (vorticity balance argument).
4. The deep circulation: thermohaline circulation and MOC recalled
   (Book 3); the Stommel--Arons model (told with its prediction of western
   deep boundary currents and poleward interior flow); the dynamic method
   for geostrophic currents (method box).
5. Ocean tides: equilibrium tide (theorem: tidal potential and height
   derived from the tidal force recalled from physics); tidal constituents
   (M2, S2, K1, O1 with periods from ledger); amphidromic points and
   cotidal lines; Kelvin waves (theorem: the coastal-trapped solution,
   width L_R) as the reason tides rotate in basins.
6. `inthefield`: Argo floats and moorings (third person).

**Definitions.** Ekman pumping; Ekman depth; Sverdrup balance (thm.);
western intensification; Stommel model; Munk boundary layer; Stommel--Arons
model; dynamic method; equilibrium tide; tidal constituent; amphidromic
point; cotidal line; Kelvin wave (oceanic). Owner check: Sverdrup balance is
Y3's (OUTLINE); Book 3 owns wind stress, gyres, Ekman layer/transport/spiral
(with "derived in the Year 3 volume"), upwelling, downwelling, coastal
upwelling, western boundary current, MOC, THC, deep-water formation, the
sverdrup unit; physics owns tides (spring/neap told); Book 4 owns ENSO and
Bjerknes feedback.

**Recall.** Tides and the tidal force (physics b1); wind stress, gyres,
Ekman layer/transport/spiral, western boundary current, MOC, sverdrup (Book 3
ch. 29); upwelling (g10); potential vorticity, β-plane (ch. 19--20); ENSO
(Book 4 ch. 23).

**Figures.** [F] `ekman_spiral` the Ekman velocity hodograph and transport;
[F] `stommel_gyre` streamfunction of a Stommel gyre (β ≠ 0) vs the
symmetric f-plane gyre (β = 0); [F] `stommel_gyre` meridional velocity across
the basin (western boundary layer); [F] `sverdrup_transport` Sverdrup
transport vs latitude for an idealised wind profile (+ ledger Gulf Stream
transport point); [F] `equilibrium_tide` equilibrium tide height vs latitude
and the M2 bulge; [S] amphidromic system in a rectangular basin (Kelvin wave
round a basin), cotidal lines; [P] an Argo float being deployed (NOAA/Argo
PD/CC, verify); [AI] none.

**Ledger.** Gulf Stream transport at Florida Straits and Hatteras (NOAA
WBTS/open papers); wind stress magnitudes (open source); tidal constituent
periods and amplitudes (NOAA tide documentation, PD); Argo array facts
(argo.ucsd.edu, dated box).

**Datasets.** None (analytic).

**Weekend problem: "A gyre in the Sea of Ammar."** An invented rectangular
basin at 20--50°N with sinusoidal wind stress. Part I: Ekman transport and
pumping at the gyre centre. Part II: Sverdrup transport and the total
interior southward flow. Part III: Stommel boundary-layer width and the
western boundary current's speed. Part IV: tides in the basin: Kelvin
wave speed and the amphidromic point. **Named number: the transport of the
western boundary current, in sverdrups.**

---

## Ch. 22 Climate Models --- `climate-models`

**Hook.** Starting from the Sun's input and the Earth's albedo, a few lines of
algebra give a planet that could be either ice-free or frozen pole to
pole. Climate models, from those few lines to programs with millions of
lines of code, are tools for asking which.

**Sections.**
1. Zero-dimensional energy balance: black body, effective temperature and
   the one-layer greenhouse model recalled from physics; feedback parameter
   and ECS recalled (Book 4); the energy-balance model as an ODE C dT/dt =
   F − λT (theorem: response time C/λ).
2. Ice--albedo feedback and multiple equilibria: Book 4's ice--albedo
   feedback recalled; temperature-dependent albedo → three equilibria
   (proposition), stability by linearisation; saddle-node bifurcation and
   hysteresis in solar constant (figdata); snowball Earth recalled (Book 4).
3. The Budyko--Sellers model: latitudinal EBM with diffusive transport
   (definition); the ice-line solution (proposition, Legendre expansion
   `\admitted` details) and the small-ice-cap instability; meridional heat
   transport recalled (Book 3).
4. Two-layer models: surface + deep ocean (theorem: fast and slow time
   scales, eigenvalues of the 2×2 system); TCR vs ECS (recall Book 4); the
   pattern of warming in time.
5. General circulation models: dynamical core (discretised primitive
   equations of ch. 19), resolution and parameterisation (clouds,
   convection); Earth system models (carbon cycle, ice sheets); spin-up;
   evaluation: CMIP, large ensembles, emergent constraints, AR6 assessed
   ranges (calibrated language, ledger per statement).
6. `inthelab`: a modelling centre and its supercomputer (third person).

**Definitions.** energy-balance model; Budyko--Sellers model; multiple
climate equilibria; saddle-node bifurcation; two-layer energy-balance model;
general circulation model; dynamical core; parameterisation; Earth system
model; model intercomparison project; spin-up (of a model); emergent
constraint; large ensemble. Owner check: energy-balance model is Y3's
(OUTLINE); ice--albedo feedback moved to Book 4 ch. 18 (Sync 2: recalled);
Book 4 owns ERF, EEI, feedback parameter, Planck response, ECS, TCR, TCRE,
NWP, data assimilation, ensemble forecast, snowball Earth; g12 owns radiative
forcing, ECS (school form); physics owns black body, emissivity, effective
temperature, greenhouse effect; Book 3 owns OLR, meridional heat transport;
"saddle-node bifurcation" not indexed by math (checked at writing).

**Recall.** Black body, Stefan--Boltzmann, greenhouse effect, one-layer
model (physics b2); albedo (g10); ice--albedo feedback, snowball Earth
(Book 4 ch. 18); ERF, feedback parameter, ECS, TCR (Book 4 ch. 27); NWP,
ensemble (Book 4 ch. 22); OLR, meridional heat transport (Book 3 ch. 27);
primitive equations (ch. 19).

**Figures.** [F] `ebm_0d` energy in vs out with a temperature-dependent
albedo: three equilibria; [F] `ebm_0d` hysteresis loop of global T vs solar
constant (snowball and ice-free branches); [F] `budyko_sellers` ice-line
latitude vs solar constant (stable and unstable branches); [F] `two_layer`
response to an abrupt 4×CO2 forcing and to a 1 %/yr ramp; [S] a GCM grid
box with parameterised processes; [S] model hierarchy ladder; [P] a
supercomputer room (NOAA/NCAR/NASA PD, verify); [AI] a modelling centre's
control room with climate fields on screens (generic).

**Ledger.** Solar constant, albedo (shared/Book 3 rows); Budyko A, B, D
parameters (North 1975 / North et al. 1981 open? else derived from the
OLR--T fit to ledger data); two-layer parameters (Geoffroy et al. 2013,
open? or AR6 Ch. 7 supplementary); AR6 ECS/TCR assessed ranges (Book 4
`ipcc:*` rows reused); CMIP6 model count (dated).

**Datasets.** None new (shared `gistemp` for a comparison plot, optional).

**Weekend problem: "How close to a snowball?"** Part I: 0-D EBM with
linear OLR: equilibria for today's solar constant. Part II: stability of
each; response time. Part III: lower the solar constant until the warm
branch disappears (saddle-node). Part IV: Budyko--Sellers ice line at that
point; compare. **Named number: the fractional drop of the solar constant
that glaciates the model planet, in per cent.**

---

## Ch. 23 Hydrogeology --- `hydrogeology`

**Hook.** A farmer's well a kilometre from a new municipal pumping station
dries up a month after the pumps start. The water table had not moved
uniformly: it had sunk into a cone, and the cone had grown.

**Sections.**
1. Head and flow: hydraulic head (elevation + pressure head), hydraulic
   gradient; Darcy's law (theorem: stated as an empirical law and derived
   from Poiseuille flow in a bundle of tubes, physics' Poiseuille recalled);
   specific discharge vs seepage velocity; hydraulic conductivity vs
   intrinsic permeability (k = K μ/(ρ g)).
2. Aquifers: porosity, permeability, aquifer, water table recalled (g6);
   confined and unconfined aquifers, aquitards; transmissivity,
   storativity, specific yield; flow nets (method box); recharge and
   residence time recalled (g10).
3. The groundwater-flow equation: theorem S ∂h/∂t = T ∇²h derived from mass
   conservation + Darcy; steady 1-D and radial solutions (Thiem,
   proposition).
4. Pumping tests: the Theis solution (theorem, similarity solution derived;
   well function W(u) computed in figdata); Cooper--Jacob approximation
   (proposition); cone of depression; interference between wells.
5. Solute transport (principle): advection--dispersion equation (theorem
   from mass balance; physics' diffusion recalled); hydrodynamic dispersion,
   dispersivity; retardation factor (sorption); breakthrough curves (erf
   solution).
6. `inthefield`: a pumping test with pressure transducers (third person).

**Definitions.** hydraulic head; hydraulic gradient; Darcy's law (thm.);
specific discharge; hydraulic conductivity; intrinsic permeability; seepage
velocity; confined aquifer; unconfined aquifer; aquitard; transmissivity;
storativity; specific yield; groundwater-flow equation (thm.); Theis
solution (thm.); Cooper--Jacob approximation (prop.); cone of depression;
flow net; advection--dispersion equation (thm.); hydrodynamic dispersion;
dispersivity; retardation factor (sorption). Owner check: Darcy's law is
Y3's (OUTLINE says "re-founds g6", but g6 never names Darcy: status new);
g6 owns porosity, permeability, aquifer, water table, groundwater, spring,
well; g10 owns residence time, fossil groundwater; Book 3 owns optical
"retardation" (qualified form here); physics owns magnetic permeability,
viscosity, Poiseuille's law, diffusion equation.

**Recall.** Porosity, permeability, aquifer, water table, spring, well (g6);
residence time, fossil groundwater (g10); viscosity, Poiseuille flow,
diffusion equation (physics b2); erf (ch. 5); Varden units (`region.py`).

**Figures.** [S] head components in a piezometer; [S] confined vs
unconfined aquifer cross-section (Varden: chalk unconfined, limestone
confined under shale); [F] `theis` Theis well function W(u) and a drawdown
type curve with Cooper--Jacob line; [F] `theis` cone of depression at three
times + interference of two wells; [F] `flow_net` steady head and
streamlines under a dam/through a section (numerical Laplace solve on a
grid, tested); [F] `advection_dispersion` breakthrough curves for three
dispersivities and a retarded solute; [P] none; [AI] a pumping-test site
with a wellhead and a field laptop (generic).

**Ledger.** K ranges for gravel, sand, silt, clay, chalk, karst limestone,
granite (USGS/open textbook, e.g. Freeze & Cherry 1979 open edition via the
Groundwater Project, CC); storativity ranges; dispersivity scale
dependence (Gelhar et al. 1992, open?); water viscosity and density
(chemistry/physics ledgers).

**Datasets.** None.

**Weekend problem: "Pumping test at Varden-3."** A well in the Jurassic
limestone, confined under the Jurassic shale (Varden units). Part I:
heads in three piezometers: flow direction and specific discharge. Part II:
drawdown data → Cooper--Jacob T and S. Part III: Theis check; radius of
influence after 30 days. Part IV: contaminant travel time from a source
200 m away with retardation. **Named number: the transmissivity of the
Varden limestone aquifer, in square metres per day.**

---

## Ch. 24 Glaciology --- `glaciology`

**Hook.** The surface of the Greenland ice sheet rises from the coast to
more than 3 km at its summit in a profile that is almost a parabola. Treat
ice as a material that will not take more than a certain stress, and that
profile follows in a few lines.

**Sections.**
1. Ice as a material: polycrystalline ice and dislocation creep (ch. 7);
   Glen's flow law (theorem in tensor form; n ≈ 3, rate factor A(T) with
   Arrhenius dependence, ledger); internal deformation vs basal sliding.
2. Glacier flow: laminar flow down an inclined slab (theorem: velocity
   profile and surface speed u_s = 2A/(n+1) (ρ g sin α)^n H^{n+1});
   shallow-ice approximation; the plastic ice-sheet profile (Nye,
   proposition: h(x) = √(2τ_0 (L − x)/(ρ g))).
3. Mass balance: accumulation and ablation zones, ELA, surface mass balance,
   firn and pore close-off (recall ch. 14 for ice cores); glacier response
   time (proposition: H/b_terminus).
4. Ice sheets and ice shelves: grounding line, buttressing, calving, ice
   streams; marine ice-sheet instability (the flux--thickness argument,
   proposition from Schoof's scaling stated with ledger); sea-level
   equivalent (proposition: volume × ρ_i/ρ_w / ocean area).
5. Sea ice and permafrost: sea-ice extent (Book 1's NSIDC series recalled or
   NSIDC data), growth by conduction (Stefan's law, theorem); the active
   layer; permafrost thaw (told, AR6).
6. The cryosphere and sea level: sea-level budget recalled (Book 4); GRACE
   mass loss (ch. 3); AR6 contributions (ledger, calibrated language).

**Definitions.** Glen's flow law (thm.); rate factor (ice); basal sliding;
shallow-ice approximation; plastic ice-sheet profile (prop.); glacier mass
balance; surface mass balance; accumulation zone; ablation zone;
equilibrium-line altitude; firn; pore close-off; ice stream; grounding line;
calving; marine ice-sheet instability; sea-level equivalent; sea-ice extent;
active layer. Owner check: Glen's law is Y3's (OUTLINE says "re-founds
g8", but g8 never names it: status new); g8 owns glacier, ice sheet, ice
shelf, sea ice, permafrost, iceberg, ice age; Book 4 owns sea-level budget,
thermosteric rise; Book 1 g8 uses the NSIDC September extent (check its
indexed terms at writing: "sea-ice extent" not indexed).

**Recall.** Glacier, ice sheet, ice shelf, sea ice, permafrost (g8); flow
law, dislocation creep (ch. 7); sea-level budget (Book 4 ch. 27); satellite
gravimetry (ch. 3); ice cores, δ18O (ch. 14); latent heat, conduction
(physics).

**Figures.** [F] `ice_flow` velocity profile with depth for n = 1, 3 and
basal sliding; [F] `ice_flow` Nye plastic profile vs a measured Greenland/
Antarctic transect (ledger points, open data) ; [S] mass-balance zones on a
valley glacier (accumulation, ELA, ablation, flow lines); [S] grounding line,
ice shelf, calving front, buttressing; [F] `sea_ice` NSIDC Arctic September
and March extent 1979--present with trend; [F] `sea_ice` Stefan growth of
sea-ice thickness over a winter; [P] an Antarctic ice-shelf front or a
Greenland outlet glacier (NASA/USGS PD, verify); [AI] a glaciology field
camp on an ice sheet with a GNSS station (generic).

**Ledger.** Glen A(T) and n (Cuffey & Paterson values via an open source:
Pattyn et al. 2008, The Cryosphere, CC BY, ISMIP-HOM uses A, n; or Paterson
1994 tables quoted in an open paper); ice and seawater densities; Greenland
and Antarctic volumes and SLE (Morlighem et al. 2017 BedMachine, Fretwell
et al. 2013 Bedmap2, open); AR6 cryosphere sea-level contributions (Book 4
`ipcc:*` reuse or new AR6 WG1 Ch. 9 rows); permafrost facts (AR6).

**Datasets.** NSIDC Sea Ice Index monthly extents (G02135, public; ~10 kB):
either read Book 1's `grade-8-nsidc-sep-extent.csv` (needs a sync ruling)
or a `# Book 5:` fetch of the September and March series.

**Weekend problem: "The Arkel ice cap."** An invented ice cap on a
plateau. Part I: basal shear stress from surface slope and thickness at
three points; is the cap near plastic? Part II: Nye profile and volume.
Part III: Glen flow: surface speed and the internal-deformation flux; mass
balance at the ELA. Part IV: sea-level equivalent and the time to melt at a
given negative balance. **Named number: the ice cap's sea-level equivalent,
in millimetres.**

---

## Ch. 25 Remote Sensing and GIS --- `remote-sensing-gis`

**Hook.** In the months before an eruption, a volcano's flank rose by a few
centimetres, too little for anyone on the ground to notice. Two radar images
taken from 700 km up, a few weeks apart, showed the swelling as a bull's-eye
of coloured fringes.

**Sections.**
1. Radiation and sensors: the electromagnetic spectrum, Planck's law and
   reflectance recalled from physics; spectral signatures of water,
   vegetation, soils and minerals (dataset); atmospheric windows (Book 3
   ch. 2) and atmospheric correction; spatial, spectral, radiometric
   resolution and revisit time; multispectral vs hyperspectral sensors;
   band ratios and the NDVI.
2. Thermal infrared: brightness temperature (definition; Planck inversion,
   proposition) vs kinetic temperature and emissivity; volcanic and urban
   heat examples.
3. Radar: synthetic-aperture radar (azimuth resolution independent of
   range, proposition), backscatter and roughness; lidar (time of flight,
   proposition) and canopy-penetrating DEMs.
4. Radar interferometry: phase difference, interferogram, one fringe = λ/2
   of line-of-sight motion (theorem); phase unwrapping; topographic vs
   deformation phase; the Mogi source recalled (Book 4) and its fringe
   pattern (figdata); applications (earthquakes: recall Book 3 ch. 18's
   pointer; subsidence; volcanoes).
5. GIS: raster vs vector data; georeferencing and map projections (g9
   recalled); DEM (Book 3) derivatives: slope, aspect, hillshade (method:
   finite differences); map algebra; buffer and overlay; supervised
   classification and the confusion matrix (accuracy statistics).
6. `inthelab`: a ground station receiving a satellite pass (third person).

**Definitions.** spectral signature; spatial resolution; spectral
resolution; revisit time; multispectral sensor; hyperspectral sensor;
atmospheric correction; brightness temperature; normalised difference
vegetation index; synthetic-aperture radar; radar backscatter; radar
interferometry; interferogram; line of sight (radar); phase unwrapping;
lidar; raster data; vector data (GIS); georeferencing; map algebra; buffer
(GIS); overlay (GIS); supervised classification; confusion matrix. Owner
check: radar interferometry is Y3's (OUTLINE says "re-founds g9", but g9
names only remote sensing and satellite images: status new); **digital
elevation model is Book 3's** (Sync 2: recalled); g9 owns map projection,
remote sensing, satellite image, satellite positioning; physics owns
reflectance, black body, Planck's law, interference; Book 3 owns atmospheric
window, photometric band; Book 4 owns the Mogi source; biology owns "buffer"
(chemistry "buffer solution"): qualified forms; "brightness temperature" and
"confusion matrix" not indexed by physics/math (checked).

**Recall.** EM spectrum, Planck's law, reflectance, interference (physics);
remote sensing, satellite image, map projection (g9); atmospheric window
(Book 3 ch. 2); digital elevation model (Book 3 ch. 4); Mogi source (Book 4
ch. 6); focal mechanism and InSAR pointer (Book 3 ch. 18).

**Figures.** [F] `spectral_signatures` reflectance spectra of vegetation,
dry soil, water, kaolinite, haematite (USGS splib07) with Landsat-8/9 and
Sentinel-2 band positions (ledger); [S] SAR viewing geometry (azimuth,
range, look angle, LOS); [F] `insar_mogi` wrapped interferogram of a Mogi
source (fringe rings) and the LOS displacement profile; [F] `varden_gis`
slope and aspect maps of the Varden DEM (`region.topo`) and an overlay
(slope > 15° ∩ limestone ∩ 200 m from the river buffer); [S] raster vs
vector representation of the same map; [S] confusion matrix layout; [P] a
Landsat or Sentinel scene (USGS/ESA Copernicus, PD/CC BY-SA IGO --- verify
licence) and a real interferogram (NASA/JPL PD, verify); [AI] a satellite
ground station dish at dusk (generic).

**Ledger.** Landsat 8/9 OLI band limits (USGS page), Sentinel-2 bands (ESA
page); Sentinel-1 wavelength (C-band) and orbit (ESA); NDVI definition
(Rouse et al. 1974 or NASA page); lidar/ICESat-2 facts (NASA); spectra
(USGS splib07 data release, Kokaly et al. 2017, PD).

**Datasets.** NEW: 5--6 spectra from the USGS Spectral Library Version 7
(splib07a, Kokaly et al. 2017, USGS data release, PD; fetch the individual
ASCII spectra if available, ~50 kB each; else ECOSTRESS library (JPL,
public)).

**Weekend problem: "A swelling flank at Mount Ossa."** An invented volcano.
Part I: NDVI of lava flows of three ages (band values given): revegetation.
Part II: brightness temperature of a fumarole field from a TIR band. Part
III: count fringes on the interferogram: LOS uplift; Mogi fit for depth.
Part IV: volume change from the Mogi formula (recall Book 4). **Named
number: the volume change of the magma chamber, in millions of cubic
metres.**

---

## Ch. 26 Planetary Interiors and Surfaces --- `planetary-interiors-surfaces`

**Hook.** The lunar maria have a few craters, the highlands are saturated
with them. Counted and calibrated against the rocks brought back by the
Apollo crews, crater densities have become a clock for every surface in the
Solar System.

**Sections.**
1. Interiors from gravity and rotation: moment-of-inertia factor recalled
   (Book 3 ch. 3); a two-layer model from mass and MoI (theorem: core radius
   and density solved; figdata); J2 and MacCullagh (ch. 3) for planets; the
   Love number k2 and tidal response (definition; Mars's liquid core,
   ledger); seismology on the Moon and Mars (InSight, ledger).
2. Impact cratering: simple and complex craters, transient crater, ejecta
   blanket; crater scaling (told, π-group scaling admitted); Meteor Crater
   as the worked simple crater.
3. Crater dating: size--frequency distribution (power law), production
   function and chronology function (ledger: Neukum-type function), crater
   equilibrium density; the lunar calibration by sample ages; model ages
   and their uncertainties (Poisson statistics, proposition: σ_N = √N).
4. Planetary volcanism and tectonics: Mars (Tharsis, Olympus Mons:
   lithosphere flexure recalled from ch. 3), Venus (resurfacing, stagnant
   lid), Io (tidal heating: proposition for the dissipation scaling stated,
   heat-pipe volcanism), icy moons (subsurface oceans of Europa, Enceladus;
   cryovolcanism).
5. Mercury's large core and the Moon's small one (ledger), and what they
   say about formation (recall Book 4's planetary differentiation).

**Definitions.** Love number; tidal heating; simple crater; complex crater;
transient crater; ejecta blanket; crater size--frequency distribution;
crater dating; crater chronology function; crater production function;
crater equilibrium density; resurfacing; stagnant lid; heat-pipe
volcanism; cryovolcanism; subsurface ocean. Owner check: crater dating is
Y3's (OUTLINE); Book 3 owns moment-of-inertia factor, terrestrial/giant
planets, Bond albedo; Book 4 owns planetary differentiation, chondrite,
CAI (and uses "crater" in prose only); physics owns tides, Kepler.

**Recall.** Moment-of-inertia factor, terrestrial planets (Book 3 ch. 3);
J2, flexure (ch. 3); planetary differentiation, chondrites (Book 4 ch. 2);
mantle plume, LIP (Book 3 ch. 15); tidal force (physics b1); Poisson
statistics (math).

**Figures.** [F] `two_layer_planet` core radius vs core density for the
Earth, Mars, Moon, Mercury from mass, radius and MoI (ledger) with possible
solutions; [S] simple vs complex crater cross-sections; [F] `crater_sfd`
cumulative SFD of two invented surfaces with isochrons of a Neukum-type
production function; [F] `crater_sfd` chronology function N(1 km) vs age;
[S] stagnant lid vs mobile lid vs heat pipe; [P] Meteor Crater (USGS PD,
verify); Olympus Mons (NASA PD); Io (NASA/JPL PD); Europa (NASA PD); Venus
Magellan radar (NASA PD); [AI] none.

**Ledger.** Mass, radius, MoI factor of Mercury, Venus, Earth, Moon, Mars
(shared `planet:*` rows reused; MoI from NASA fact sheets or primary
papers); Mars k2 (Konopliv 2016 / InSight papers, open); Neukum chronology
coefficients (Neukum, Ivanov & Hartmann 2001; check open copy; else
Hartmann 2005 Icarus or a NASA/LPI open document); Meteor Crater diameter
and age (USGS); Io heat flow (open paper); Europa ice-shell thickness range
(open review); Venus surface age (open review).

**Datasets.** None.

**Weekend problem: "Two plains on Mars."** Part I: Mars two-layer model:
core radius from mass and MoI. Part II: crater counts on an invented lava
plain (bins given): cumulative SFD, N(1 km). Part III: model age from the
chronology function, with Poisson error; a second, older plain. Part IV: a
partially buried crater population: resurfacing age. **Named number: the
model age of the young lava plain, in billions of years.**

---

## Ch. 27 Planetary Atmospheres and Habitability --- `planetary-atmospheres`

**Hook.** Venus and the Earth are near twins in size and probably began with
similar water. Venus's atmosphere now has a deuterium-to-hydrogen ratio
about a hundred times the Earth's: the trace of an ocean lost to space.

**Sections.**
1. Atmospheric structure: isothermal atmosphere and scale height recalled
   (physics); radiative--convective equilibrium (definition; grey
   two-stream result stated); the exobase (definition; mean free path =
   scale height, proposition).
2. Atmospheric escape: Jeans escape (theorem: flux from the Maxwell--
   Boltzmann tail at the exobase, escape parameter λ = GMm/(kTr)); escape
   time scales; hydrodynamic escape, non-thermal escape (sputtering, ion
   pickup, photochemical), diffusion-limited escape (proposition stated).
3. Venus: the runaway greenhouse (definition; the radiation limit of a
   moist atmosphere, Simpson--Nakajima, ledger value), moist greenhouse,
   D/H enrichment as evidence (proposition: Rayleigh-type enrichment from
   escape with fractionation, recall ch. 14).
4. Mars: thin atmosphere, past water (valley networks, ledger), loss to
   space (MAVEN results, ledger), obliquity variations (told).
5. Titan: a methane cycle with lakes and rain, haze; scale height and
   surface pressure (ledger).
6. Habitability: habitable zone recalled (g10) and refined (runaway and
   maximum-greenhouse limits, ledger); planetary habitability factors; the
   long-term carbon cycle recalled (Book 4) as the thermostat.

**Definitions.** exobase; Jeans escape; escape parameter; hydrodynamic
escape; non-thermal escape; diffusion-limited escape; radiative--convective
equilibrium; runaway greenhouse; moist greenhouse; runaway greenhouse limit;
planetary habitability. Owner check: atmospheric escape is Y3's (OUTLINE);
Book 4 owns Jeans criterion/mass/length (hence "Jeans escape", never bare
"Jeans"); g10 owns habitable zone, equilibrium temperature (re-founded by
Book 3); chemistry indexes "habitability" (a different sense): qualified
"planetary habitability"; physics owns scale height, escape velocity,
Maxwell--Boltzmann distribution, greenhouse effect; Book 4 owns the
long-term carbon cycle and the silicate thermostat.

**Recall.** Scale height, barometric formula, Maxwell--Boltzmann, escape
velocity (physics b1/b2); greenhouse effect (physics); habitable zone (g10);
equilibrium temperature, Bond albedo (Book 3 ch. 3); snow line (Book 4
ch. 2); carbonate--silicate cycle (Book 4 ch. 26); Rayleigh distillation
(ch. 14).

**Figures.** [F] `jeans_escape` Jeans escape parameter and loss time scale vs
molecular mass for Earth, Mars, Venus, Titan exospheres (ledger T, r_exo);
[F] `runaway` OLR vs surface temperature for a moist atmosphere: the
plateau at the radiation limit (schematic from ledger values, or a
grey-model calculation flagged as illustrative); [S] atmospheric structure
with the exobase; [F] `planet_atmospheres` T(z) profiles of Venus, Earth,
Mars, Titan (ledger points); [P] Titan's lakes (Cassini radar, NASA PD);
Mars valley networks (NASA PD); Venus (NASA PD); [AI] none.

**Ledger.** Exobase temperatures and heights (open reviews); Venus D/H
(Donahue et al. 1982 / de Bergh 1991; check open); Simpson--Nakajima limit
(Goldblatt et al. 2013 Nature Geoscience, open?; Kopparapu et al. 2013 ApJ,
open); MAVEN escape rates (Jakosky et al. 2018, open); Titan surface
pressure and temperature (Huygens results, open); planet temperatures and
pressures (NASA fact sheets).

**Datasets.** None.

**Weekend problem: "Will Kepos keep its water?"** An invented Earth-size
planet. Part I: exobase temperature and the Jeans parameter for H, He, O.
Part II: Jeans flux of H and the time to lose an ocean's hydrogen. Part
III: diffusion-limited escape instead: which limits? Part IV: insolation
vs the runaway limit: is Kepos inside the habitable zone? **Named number:
the time for Kepos to lose an Earth ocean of hydrogen by diffusion-limited
escape, in billions of years.**

---

## Ch. 28 Exoplanets --- `exoplanets`

**Hook.** In 1995 a star in Pegasus was found to wobble with a four-day
period: a planet half Jupiter's mass, closer to its star than Mercury to the
Sun. Thirty years later more than five thousand planets are catalogued, and
the atmospheres of a few have been sampled.

**Sections.**
1. Radial velocity: Doppler and radial velocity recalled from physics;
   two-body orbit (Kepler recalled); the semi-amplitude K (theorem:
   derived for a circular orbit, eccentric form stated); minimum mass
   M_p sin i; detection limits (stellar jitter, ledger).
2. Transits: transit depth (R_p/R_*)², duration and impact parameter
   (theorem, circular orbit), limb darkening; combining with RV gives
   density (proposition); transit-timing variations; false positives.
3. Imaging and microlensing: direct imaging, contrast and the coronagraph;
   gravitational microlensing (Einstein radius stated, `\admitted` from
   general relativity with pointer to physics); which planets each method
   finds (selection effects).
4. What has been found: occurrence rates; hot Jupiters, super-Earths,
   sub-Neptunes; the radius valley (photoevaporation/core-powered loss
   recalled from ch. 27); mass--radius relation and compositions (figdata
   from the archive).
5. Atmospheres: transmission spectroscopy (proposition: signal 2 H R_p /
   R_*²), secondary eclipses and day-side temperatures; JWST detections
   (ledger, dated box).

**Definitions.** radial-velocity method; minimum mass; transit method;
transit depth; impact parameter (transit); limb darkening; direct imaging;
coronagraph; gravitational microlensing; Einstein radius; transit-timing
variation; hot Jupiter; super-Earth; sub-Neptune; occurrence rate; radius
valley; mass--radius relation; transmission spectroscopy; secondary
eclipse. Owner check: transit method is Y3's (OUTLINE); g10 owns exoplanet
and habitable zone; physics owns Doppler effect, radial velocity,
spectroscopic binary, Kepler's laws, gravitational lensing (check physics
b3 astrophysics at writing; "Einstein radius" and "limb darkening" not
indexed: checked); Book 3 owns flux, luminosity, magnitudes.

**Recall.** Doppler effect, radial velocity, spectroscopic binary (physics
g12); Kepler's laws (physics b1); exoplanet, habitable zone (g10);
luminosity, flux (Book 3 ch. 2); equilibrium temperature (Book 3 ch. 3);
scale height (physics), escape (ch. 27).

**Figures.** [F] `rv_transit` RV curve of an invented planet (circular and
e = 0.3) with K marked; [F] `rv_transit` transit light curve with limb
darkening (quadratic law) and the geometry; [S] transit geometry (b, R_p,
R_*); [F] `exoplanet_archive` mass--radius diagram from the NASA Exoplanet
Archive with composition curves (iron, rock, water) and Solar System
planets; [F] `exoplanet_archive` period--radius diagram with the radius
valley; [S] microlensing geometry; [P] HR 8799 direct image (NASA/JPL/Keck
or ESO, verify licence) or a JWST transmission spectrum (NASA/ESA/CSA,
verify); [AI] none.

**Ledger.** 51 Peg b discovery parameters (Mayor & Queloz 1995, Nature;
check open copy or the Exoplanet Archive row); archive counts (dated box,
fetched date); Kepler occurrence rates (Fulton et al. 2017 radius valley,
AJ, open); JWST detections (NASA/STScI press releases, primary papers);
RV precision of ESPRESSO-class instruments (ESO page).

**Datasets.** NEW: NASA Exoplanet Archive Planetary Systems Composite
Parameters (TAP query, public; ~1 MB raw → small derived CSV of planets with
both mass and radius; acknowledgement text in the credits).

**Weekend problem: "A planet around Selene's Lamp."** An invented K dwarf.
Part I: RV curve: period, K, minimum mass. Part II: transit: depth →
radius; duration → impact parameter, inclination. Part III: true mass and
density; place it on the mass--radius diagram. Part IV: equilibrium
temperature, scale height, and the transmission-spectrum signal of water.
**Named number: the planet's mean density, in grams per cubic centimetre.**

---

## Ch. 29 The Milky Way and Galaxies --- `milky-way-galaxies`

**Hook.** Stars far from the centre of the Galaxy circle it as fast as stars
near it. If the mass we see were all there is, they would be slower, the way
Neptune is slower than Mercury. Something unseen holds them.

**Sections.**
1. The structure of the Galaxy: the Milky Way recalled (physics); disc
   (thin and thick), bulge/bar, stellar halo; stellar populations; Galactic
   coordinates; the Sun's position (ledger: R_0 from GRAVITY).
2. Rotation: the local standard of rest; Oort constants (theorem: derived
   for nearby stars); the 21-cm line and the tangent-point method (theorem:
   v_max = V(R) − V_0 sin l ... derived); the rotation curve (dataset:
   Eilers et al. 2019); mass models: bulge + disc + halo; the dark-matter
   halo (dark matter recalled from physics).
3. Galaxies: the Hubble sequence (spiral, elliptical, lenticular,
   irregular), spiral arms as density waves (told), supermassive black
   holes (Sgr A*, ledger), groups and clusters (Local Group).
4. The distance ladder: parallax and parsec recalled (Book 3 ch. 2); Cepheid
   variables and the Leavitt law (ledger calibration); tip of the red giant
   branch; Type Ia supernovae as standard candles (recall physics'
   supernova); Tully--Fisher relation; Hubble's law recalled (physics) and
   the Hubble constant measurements; the Hubble tension (ledger, neutral).
5. `inthelab`: an astrometric satellite and its catalogue (Gaia; third
   person; dated box).

**Definitions.** Galactic disc; Galactic bulge; stellar halo; thick disc;
stellar population; Galactic coordinates; local standard of rest; 21-cm
line; rotation curve; Oort constants; dark-matter halo; Hubble sequence;
spiral galaxy; elliptical galaxy; lenticular galaxy; irregular galaxy;
density-wave theory; supermassive black hole; Cepheid variable; Leavitt law;
standard candle; distance ladder; tip of the red giant branch; Tully--Fisher
relation; Hubble tension; Local Group; galaxy cluster. Owner check: rotation
curve and distance ladder are Y3's (OUTLINE); physics owns Milky Way (g5),
light-year (g8), Hubble's law, redshift, supernova, white dwarf, neutron
star, black hole, HR diagram, main sequence, dark matter, CMB; physics uses
"standard candle" in text only (not indexed: defined here); Book 3 owns
annual parallax, parsec, luminosity, magnitudes, distance modulus,
right ascension, declination (celestial); Book 4 owns ISM, molecular cloud.
Check at writing whether physics indexes "galaxy" (not found in the
harvest).

**Recall.** Milky Way, light-year (physics g5/g8); parallax, parsec,
magnitudes, distance modulus, luminosity (Book 3 ch. 2); Hubble's law, dark
matter, supernova, black hole, HR diagram (physics b3); ISM (Book 4 ch. 1);
Doppler effect (physics g12); Kepler's third law (physics b1).

**Figures.** [S] edge-on and face-on sketches of the Galaxy (disc, bulge,
bar, halo, Sun at R_0); [S] tangent-point geometry; [F] `rotation_curve`
Eilers et al. 2019 data with an exponential-disc + bulge + NFW-halo model
(fit in figdata, tested on synthetic data); [F] `rotation_curve` enclosed
mass vs radius, visible vs total; [F] `distance_ladder` Leavitt law
(ledger calibration points) and a ladder diagram with distance ranges per
rung; [S] Hubble sequence tuning fork; [P] M51 or M101 (NASA/ESA Hubble,
PD/CC BY 4.0, verify); ESO Milky Way panorama (CC BY 4.0, verify); [AI]
none.

**Ledger.** R_0 and V_0 (GRAVITY Collaboration 2019/2021, A&A open;
Reid & Brunthaler 2020 for Sgr A* proper motion); Oort A, B (Bovy 2017,
MNRAS open); Eilers 2019 table (VizieR); Sgr A* mass (GRAVITY 2019);
Leavitt law calibration (Riess et al. 2022 ApJL open; Breuval et al.);
H0 values (Planck 2018 A&A open; SH0ES 2022) in a dated box; Local Group
members/mass (open review); disc scale lengths (Bland-Hawthorn & Gerhard
2016, ARA&A, open?).

**Datasets.** NEW: Eilers et al. 2019 circular-velocity curve (VizieR
J/ApJ/871/120, CDS terms: free use with citation; ~3 kB).

**Weekend problem: "Weighing the Galaxy."** Part I: Oort constants from
listed proper motions/radial velocities of nearby stars (invented
sample). Part II: tangent-point velocities from 21-cm maxima: inner
rotation curve. Part III: visible mass (disc + bulge) and its predicted
curve. Part IV: enclosed total mass at 20 kpc from the flat curve; dark
fraction. **Named number: the dark-matter fraction of the mass within
20 kpc, in per cent.**

---

## Ch. 30 Where the Elements Come From --- `origin-of-elements`

**Hook.** The calcium in a limestone cliff was made in a star that exploded
before the Sun formed; the gold in a ring probably comes from two neutron
stars that collided. The solar abundance curve is a record of all these
events.

**Sections.**
1. Solar abundances: photospheric and meteoritic scales (CI chondrites
   recalled from Book 4); the dex scale (log ε = 12 + log N_X/N_H); the
   abundance curve and its features (iron peak, odd--even effect,
   Li--Be--B deficit); metallicity and [Fe/H].
2. Primordial and stellar nucleosynthesis recalled from physics (BBN, H and
   He burning, binding energy and the iron peak); what each stage leaves.
3. Neutron captures: the s-process (theorem: σN ≈ constant along the path
   in local equilibrium, derived from the capture rate equations); branching
   points (told); the r-process (rapid capture, waiting points, peaks at
   N = 50, 82, 126); p-nuclei.
4. Sites: AGB stars (s), core-collapse supernovae, neutron-star mergers and
   kilonovae (GW170817, ledger); Type Ia supernovae and iron.
5. Galactic chemical evolution: stellar yields, the closed-box model
   (theorem: Z = y ln(1/μ) derived); the G-dwarf problem; α-elements and the
   [α/Fe] knee as a clock.
6. From solar abundances to the Earth: the volatility trend (Book 4's
   condensation temperature recalled), bulk silicate Earth recalled (Book 4),
   Goldschmidt classes recalled; why the Earth is iron-rich and
   volatile-poor.

**Definitions.** solar abundance; dex; metallicity; neutron capture;
s-process; r-process; sigma-N relation (prop.); p-nuclei; neutron-star
merger; kilonova; alpha element; stellar yield; galactic chemical evolution;
closed-box model (thm.); G-dwarf problem; volatility trend. Owner check:
s- and r-process and galactic chemical evolution are Y3's (OUTLINE);
physics owns stellar and Big Bang nucleosynthesis, binding energy, iron
peak, valley of stability, beta decay, neutron star, supernova, white dwarf;
chemistry g9 indexes "abundance" (generic): qualified "solar abundance";
Book 4 owns CI chondrite, condensation temperature and sequence,
Goldschmidt classes, BSE.

**Recall.** BBN, stellar nucleosynthesis, binding energy, neutron star,
supernova (physics b3); half-life, beta decay (physics); CI chondrite,
condensation temperature, Goldschmidt classes, BSE (Book 4 ch. 2--3); HR
diagram (physics b3).

**Figures.** [F] `solar_abundances` the solar abundance curve log ε vs Z
(Asplund et al. 2021 + Lodders meteoritic), features annotated; [S] chart
of nuclides strip with s-path and r-process decay back to stability; [F]
`s_process` σN along the s-path (ledger cross-sections and abundances for a
few nuclides) and the closed-box metallicity distribution vs an observed
G-dwarf histogram (ledger) ; [F] `gce` [α/Fe] vs [Fe/H] schematic from a
two-phase yield model; [F] `solar_abundances` CI-normalised Earth (BSE)
vs 50 % condensation temperature: the volatility trend (Book 4 rows +
Lodders 2003 T_c); [P] Crab Nebula (NASA/ESA Hubble, verify); kilonova
AT2017gfo image (NASA/ESO, verify); [AI] none.

**Ledger.** Asplund, Amarsi & Grevesse 2021 (A&A, CC BY 4.0) solar
abundances; Lodders 2003 condensation temperatures (ApJ; Book 4 may have
rows); s-process cross-sections (KADoNiS database, open); GW170817 facts
(LIGO/Virgo open papers); G-dwarf metallicity distribution (open paper,
e.g. Casagrande 2011 GCS); McDonough & Sun 1995 BSE (Book 4 rows reuse).

**Datasets.** NEW (small): Asplund et al. 2021 Table (VizieR or the A&A
table, CC BY 4.0; ~5 kB).

**Weekend problem: "A closed-box galaxy."** Part I: dex conversions; solar
Fe/H and the metallicity of a star. Part II: s-process σN: predict the
abundance of an s-only isotope from a neighbour's. Part III: closed-box
model: Z(μ), yield from the present gas fraction. Part IV: the predicted
metallicity distribution; fraction of long-lived stars with [Fe/H] < −1,
against the observed (G-dwarf problem). **Named number: the fraction of
long-lived stars with [Fe/H] < −1 predicted by the closed box, in per
cent.**

---

## Ch. 31 Field and Lab Methods III --- `field-lab-methods-3`

**Hook.** A geophysics crew spends a week walking lines across a valley with
a gravimeter, a magnetometer and a cable of electrodes. By Friday they can
draw the granite they never saw and say how deep it lies.

**Sections.**
1. Gravity surveys: relative gravimeters, drift and tide corrections
   (method), latitude, free-air and Bouguer corrections recalled (Book 3),
   terrain correction (Hammer zones, told); anomaly of a buried sphere and
   cylinder (theorems, derived); depth rules (half-width).
2. Magnetic surveys: total-field anomaly, diurnal correction (base
   station), IGRF removal (ch. 4); anomaly of a vertical dyke/contact
   (proposition, formula admitted beyond the 2-D setup); reduction to the
   pole (told).
3. Electrical methods: resistivity recalled from physics; apparent
   resistivity (theorem: point source over a half-space derived, Wenner and
   Schlumberger geometric factors); electrode arrays; vertical electrical
   sounding (two-layer curves, figdata); electrical resistivity tomography;
   Archie's law (proposition, empirical).
4. Seismic refraction in the field (ch. 2 recalled) and ground-penetrating
   radar: velocity from relative permittivity (proposition), radargram,
   depth of penetration vs conductivity.
5. Processing and uncertainty: error budgets and propagation (chemistry/
   math recalled), misfit and inversion (ch. 1 recalled), non-uniqueness
   and joint interpretation.
6. A mapping project (worked): the Varden granite from gravity +
   magnetics + resistivity; how the map of Book 3's pilot is completed at
   depth.

**Definitions.** relative gravimeter; instrumental drift; terrain
correction; total-field anomaly; diurnal correction; reduction to the pole;
apparent resistivity; electrode array; vertical electrical sounding;
electrical resistivity tomography; Archie's law (prop.); ground-penetrating
radar; radargram; misfit (data). Owner check: Book 3 owns gravity anomaly,
free-air and Bouguer corrections and anomalies, normal gravity; physics owns
resistivity, relative permittivity, electromagnetic waves; chemistry/math own
uncertainty terms; Book 4 owns XRF, microprobe (other methods chapters).

**Recall.** Gravity anomaly, free-air/Bouguer corrections (Book 3 ch. 11);
IGRF (ch. 4); resistivity, relative permittivity (physics b2/b3); seismic
refraction survey (ch. 2); uncertainty propagation (chemistry b1/b2, math);
weighted least squares (ch. 1); porosity (g6), wireline logs (ch. 17).

**Figures.** [F] `gravity_granite` Bouguer anomaly over the Varden granite
(granite modelled as a vertical elliptic cylinder below the unconformity;
`region.py` geometry; density contrast from ledger) as a map and a profile
along A--B; [F] `magnetic_anomaly` total-field anomaly over a 2-D contact
(and a dyke if the sync allows one) at two inclinations; [F] `ves` apparent
resistivity curves for two-layer models (Schlumberger), with an invented
field sounding; [S] Wenner/Schlumberger electrode layouts; [S] GPR
geometry and a schematic radargram with a hyperbola from a pipe; [S] survey
grid plan over the Varden map; [AI] a geophysics crew with a resistivity
cable and a gravimeter in a meadow (generic).

**Ledger.** Densities of granite, schist, sedimentary cover (open source;
reuse ch. 2/17 rows); magnetic susceptibilities (open source); resistivity
ranges of rocks and waters (USGS/open textbook); Archie parameters (Archie
1942 via an open source); GPR velocities/permittivities (open source);
gravimeter precision (manufacturer-neutral open source; dated).

**Datasets.** None (`region.py`).

**Weekend problem: "The hidden granite of the Varden Hills."** Part I:
gravity readings with drift and tide: reduce a loop. Part II: Bouguer
anomaly across the granite; half-width depth estimate. Part III: forward
model of the cylinder: fit the top depth (compare with `region.py`'s
unconformity depth at the granite). Part IV: resistivity sounding over the
alluvium: thickness of the alluvium and the water table; Archie porosity.
**Named number: the depth to the top of the Varden granite from its gravity
anomaly, in metres.**
