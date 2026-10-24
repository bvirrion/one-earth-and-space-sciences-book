# BRIEFS --- Book 4 (University Year 2, `bachelor-2`, prefix `b2`)

Phase A plan, written 2026-10-23 by the Book 4 agent. One brief per chapter,
in outline order: hook; sections; definitions (term, label, owner check);
recall boxes; planned figures tagged **[S]** schematic (TikZ/pgfplots typed),
**[F]** figdata (tested script), **[AI]** AI illustration (generic scene),
**[P]** photograph (PD or verified CC); ledger needs; datasets; the weekend
problem's story and its named final number. `DEFINITIONS.md` is the term
table; `PROGRESS.md` the state.

## Conventions binding on this book

- **Register (Year 2).** Each law is a `theorem`/`proposition` with a
  derivation at Year-2 mathematics: partial derivatives, gradients, the heat
  equation recalled from the physics books (solutions quoted, never a Fourier
  series --- that is Year 3), 3x3 linear systems and least squares, exponential
  decay chains, log-normal and power laws, simple ODEs integrated numerically
  in figdata. Otherwise `\admitted` plus a prose pointer ("derived in the
  physics books' Year 2 volume", "the Year 3 volume of this series").
  Standard techniques go in `method` boxes (label `met:`).
- **Labels** `<type>:b2:<slug>:<name>`. Terms only in their owner chapter,
  inside a `definition`, as `\emph{}\index{}`; named laws owned by this series
  are indexed in their theorem/proposition. Never a bare homograph (table at
  the end). Never `\cref{fig:...}` (omfigure has no counter: "the figure
  below"). No `\cref` across books: prose only ("the Year 1 volume, chapter
  on active margins").
- **Recall boxes.** Year-1 notions (Book 3) and school notions are recalled in
  a `recall` box or one clause; sister-series notions (physics, chemistry,
  biology) are recalled with the series named in prose ("the chemistry
  books' Year 2 volume"). Never redefine.
- **Calibration.** 12 exercises (4★, 5★★, 3★★★ in that order); a weekend
  problem of 22--28 questions in Parts I--IV ending on a **named number**
  printed bold (`\textbf{\qty[text-series-to-math=true]{..}{..}}`); ~12 pp per
  chapter including solutions. Solutions computed from the **rounded printed**
  data; every answer re-read against its question.
- **Ledger** ids `<family>:<topic>` (e.g. `usgs:bhvo2-sio2`,
  `ipcc:tcre`, `berger91:orbit-table`); grep `sources/data_ledger.md
  sources/ledger/` before minting; cite Book 2's `ipcc:*` rows and Book 3's
  rows read-only where they already carry the number. Every real number fetched
  directly from its source (never from memory or a search snippet).
- **Exercise maps and sections:** the Varden Hills only
  (`figdata/shared/region.py`, imported, never edited). Real orogens (Alps,
  Himalaya--Tibet, Andes, Appalachian--Caledonian--Variscan) are taught from
  sourced maps/sections redrawn as schematics with a ledger row for every
  number on them; no national regional geology.
- **Observation only** (`inthefield`/`inthelab` third person); **climate
  physical science only** (AR6 WG1 calibrated language, ledger row per
  statement with report, chapter, section); no curriculum, school system,
  university or exam named; no French place named (gate 7).
- **Figures:** ~4 schematics per chapter plus figdata plots; each figure
  checked on its own page at 130 dpi (layout + science), one FIGCHECK line in
  `sources/book4/FIGCHECK.md`.

---

## Ch. 1 The Interstellar Medium and Star Formation --- `ism-star-formation`

**Hook.** The Sun, the Earth and every atom of the rocks in this book were
once a cold, dark cloud of gas and dust between the stars. Why does such a
cloud, held up by its own heat, ever collapse?

**Sections.**
1. The interstellar medium: phases (cold neutral, warm, hot ionised, molecular),
   number densities and temperatures (ledger table); gas-to-dust mass ratio
   ~100; extinction and reddening by dust (descriptive); the 21-cm line and CO
   as tracers (descriptive, recall spectral lines from physics).
2. Molecular clouds: giant molecular clouds, cores, filaments; masses and sizes
   (ledger: Taurus, Orion A); cooling by line emission; why they are cold
   (~10 K).
3. Gravitational collapse: the virial theorem recalled from physics
   (`\admitted`, 2K + U = 0); thermal energy vs gravitational energy of a
   uniform sphere (U = -3GM^2/5R, derived by integrating shells); **Jeans
   criterion** (proposition, derived from the energy balance); Jeans mass and
   Jeans length as functions of T and n (proposition); free-fall time
   (proposition, from Kepler's third law applied to a degenerate orbit --- the
   classical argument; physics owns Kepler); fragmentation (descriptive).
4. Protostars: the Kelvin--Helmholtz time scale (proposition: E_grav / L);
   accretion rate ~ c_s^3/G (proposition from dimensional reasoning +
   free-fall); protostellar classes (descriptive); T Tauri stars; bipolar
   outflows and jets; arrival on the main sequence (recall HR diagram from
   physics b3).
5. Discs: angular momentum conservation forces a disc (proposition: radius of
   centrifugal balance r_c = j^2/GM); protoplanetary disc masses and lifetimes
   (ledger: ALMA HL Tau, disc fractions vs cluster age ~ few Myr);
   temperature profile of a passive disc T ∝ r^{-1/2} (proposition from
   radiative balance, black body recalled from physics).
6. `inthelab`: how radio and millimetre interferometers observe cold gas
   (third person; ALMA as the example).

**Definitions (owner check: OUTLINE Y2 map gives Jeans criterion and
protostellar disc to this chapter; nothing in school or Book 3).**
interstellar medium; interstellar dust; molecular cloud; dense core;
Jeans criterion (in its proposition); Jeans mass; Jeans length; free-fall time;
protostar; Kelvin--Helmholtz time scale; T Tauri star; bipolar outflow;
protoplanetary disc (series name for "protostellar disc"; both indexed, one
definition).

**Recall.** Main sequence, HR diagram, nucleosynthesis, stellar hydrostatic
equilibrium (physics b3 astrophysics); Kepler's laws, escape velocity
(physics b1 central forces); black body, Stefan--Boltzmann, Wien (physics b2
thermal radiation); ideal gas (physics); virial theorem (physics b3, admitted);
magnitude and stellar spectra (Book 3 astronomy chapters).

**Figures.** [S] ISM phases on a log T--log n plane (boxes, ledger numbers);
[S] collapse sequence: cloud -> core -> protostar + disc + outflow -> T Tauri
-> planetary system (five panels); [F] `jeans` Jeans mass vs n for T = 10, 20,
50 K with the observed core range shaded; [F] `jeans` free-fall time vs n;
[S] disc geometry with the centrifugal radius; [P] HL Tau ALMA image (ESO,
CC BY 4.0, verify) or a Hubble pillars image (ESA/Hubble CC BY 4.0, verify);
[AI] a radio-telescope array under a night sky (generic).

**Ledger.** ISM phase densities/temperatures (review source, open);
Taurus/Orion cloud masses; molecular core temperature/density; HL Tau disc
radius and age; disc fraction vs age (Haisch et al. 2001 or newer open
review); solar mass and luminosity (shared `sun:*`); mean molecular weight
2.33 for molecular gas (source).

**Datasets.** None (analytic figdata).

**Weekend problem: "A core in the Aldra cloud."** An invented dense core
(T = 10 K, n = 3e4 cm^-3, R = 0.1 pc, mass from a column density map read in
Part I). Part I: mass and mean density from the map; Part II: Jeans mass and
length, is it unstable; free-fall time; Part III: accretion rate and time to
assemble a 1 solar-mass star; Kelvin--Helmholtz time of the protostar; Part
IV: disc radius from the core's measured rotation (velocity gradient), disc
temperature at 1 au and 30 au, water snow line radius. **Named number: the
time to assemble a 1 solar-mass star at c_s^3/G (written: 624 thousand years,
against a core free-fall time of 145 kyr).**

---

## Ch. 2 Planet Formation and Meteorites --- `planet-formation-meteorites`

**Hook.** About fifty tonnes of rock fall on the Earth every day; a few
stones are old enough to date the birth of the Solar System to within a
million years.

**Sections.**
1. The solar nebula: minimum-mass solar nebula (descriptive with the surface
   density law Sigma ∝ r^{-3/2}, ledger); temperature decreasing outward.
2. The condensation sequence: 50% condensation temperatures (ledger table,
   Lodders 2003); refractory, moderately volatile, volatile elements; the snow
   line (proposition: radius where the passive-disc temperature from ch. 1
   reaches ~150--170 K); rock-forming vs ice-forming planets; bulk composition
   of planets recalled from Book 3.
3. From dust to planets: sticking and settling (descriptive); planetesimals
   (~1--100 km); runaway and oligarchic growth (descriptive); planetary
   embryos; giant impacts and the Moon (descriptive, ledger for timing);
   giant-planet formation and migration (descriptive only, no named model
   beyond a mention).
4. Meteorites: falls and finds; classification: chondrites (ordinary,
   carbonaceous, enstatite), achondrites, irons, stony-irons; chondrules and
   CAIs; petrologic types (thermal metamorphism vs aqueous alteration,
   descriptive); Widmanstätten pattern and cooling rate (descriptive); meteorite
   parent bodies (Vesta--HED link, ledger).
5. Dating the Solar System: Pb--Pb ages of CAIs (ledger: 4567 Ma) using the
   isochron recalled from Book 3; short-lived radionuclides (26Al, half-life
   0.717 Myr, ledger); relative chronology from 26Al/27Al (proposition:
   Delta t = ln(R0/R)/lambda).
6. Differentiation of planetesimals: heating by 26Al (proposition: adiabatic
   temperature rise ΔT = H0 e^{-λ t_acc}/(λ c) for a body accreted at t_acc);
   melting, metal--silicate segregation, iron cores; why chondrites escaped
   melting (late accretion); planetary differentiation of the Earth
   (descriptive, timing from Hf--W told in prose, ledger).
7. `inthelab`: how meteorites are curated and cut (third person; Antarctic
   collection programmes).

**Definitions.** solar nebula; condensation temperature; condensation sequence
(owner per OUTLINE); snow line; planetesimal; planetary embryo; meteorite fall;
meteorite find; chondrite; chondrule; calcium--aluminium-rich inclusion (CAI);
carbonaceous chondrite; achondrite; iron meteorite; stony-iron meteorite;
short-lived radionuclide; planetary differentiation (owner per OUTLINE / Book 3
forward list).

**Recall.** Isochron, initial ratio, parent isotope, radiogenic daughter
(Book 3 ch. 25); decay constant, half-life (physics g12); bulk composition of
the planets, Moon formation (Book 3 planetology chapters --- check as written);
core, mantle, crust (Book 3 ch. 9).

**Figures.** [S] radial structure of the nebula with snow line and
condensation zones; [F] `condensation` 50% condensation temperature bar chart
for ~20 elements, grouped; [F] `al26` temperature rise vs accretion time
(lines for bodies accreted at 0.5, 1, 2, 3 Myr after CAIs) with the
silicate-solidus line; [S] meteorite classification tree; [S] growth stages
dust -> pebbles -> planetesimals -> embryos -> planets with size and time
scales; [P] Allende chondrules (Commons, verify CC); [P] Widmanstätten pattern
in an iron (Commons, verify); [AI] a meteorite search team on Antarctic blue
ice (generic, no flags).

**Ledger.** Condensation temperatures (Lodders 2003, ApJ --- open access check);
CAI Pb--Pb age (Connelly et al. 2012, Science --- find an open restatement or
the abstract page); 26Al half-life, initial 26Al/27Al (5.2e-5); 26Al decay
energy per atom; chondrite heat capacity; Vesta/HED; daily meteoritic influx
(source); meteorite counts by class (Meteoritical Bulletin database
statistics, verify route); snow-line temperature.

**Datasets.** Optional: meteorite counts by class (Meteoritical Bulletin;
the NASA Socrata route is dead, see PROGRESS); fall back to a ledger table of
published fractions.

**Weekend problem: "The stone that fell on the frozen lake."** An invented
fall: fireball trajectory gives the time; Part I classify from a described
section (chondrules, metal, matrix); Part II Pb--Pb model age from three
measured ratios (isochron recall) ; Part III 26Al heating of its 20-km parent
body accreted at 2.4 Myr: did it melt?; Part IV compare with an achondrite
from a body accreted at 0.8 Myr; condensation temperature of its volatile
depletion. **Named number: the peak temperature reached in the chondrite's
parent body (°C).**

---

## Ch. 3 Elements in the Earth --- `elements-in-the-earth`

**Hook.** Gold is rare in the crust not because the Earth lacks it but
because almost all of it sank into the core 4.5 billion years ago.

**Sections.**
1. Goldschmidt's classification: lithophile, siderophile, chalcophile,
   atmophile; the link to bonding (recall electronegativity from chemistry);
   periodic table coloured by affinity (`\omperiodictable`-like pic from the
   style file if present, else a TikZ grid).
2. The chondritic Earth: CI chondrites as the reference; refractory lithophile
   elements in chondritic ratios; volatile depletion vs condensation
   temperature (recall ch. 2); bulk silicate Earth (primitive mantle); core
   composition by mass balance (proposition: Fe partition between core and
   mantle; density deficit of the core recalled from Book 3 PREM: light
   elements).
3. Mantle, oceanic crust, continental crust: average compositions (ledger:
   Rudnick & Gao 2003 crust, Gale et al. 2013 MORB, McDonough & Sun 1995
   pyrolite/primitive mantle); major element oxides; mass balance of
   extracting crust from mantle (proposition, linear system).
4. Trace elements: definition (< 0.1 wt%); the mineral--melt partition
   coefficient (definition, Nernst form; chemistry owns "partition
   coefficient" in general --- qualified form); compatible and incompatible
   elements; ionic radius and charge (Onuma-type argument, descriptive); large
   ion lithophile (LILE) and high field strength elements (HFSE); rare earth
   elements.
5. Normalised diagrams: chondrite-normalised REE patterns; primitive-mantle
   normalised multi-element ("spider") diagrams; Eu anomaly (proposition:
   Eu/Eu* = Eu_N / sqrt(Sm_N Gd_N)); reading MORB, OIB and continental crust
   patterns; MORB and OIB defined here as reference melts.
6. `inthelab`: how a whole-rock powder becomes a trace-element analysis (pointer
   to ch. 31).

**Definitions.** Goldschmidt classification (owner per OUTLINE); lithophile
element; siderophile element; chalcophile element; atmophile element;
refractory element; volatile element (qualified in prose "volatile element",
defined with refractory); CI chondrite; bulk silicate Earth; primitive mantle
(same definition); trace element (owner per OUTLINE); mineral--melt partition
coefficient (contested, see report); compatible element; incompatible element;
large-ion lithophile element; high-field-strength element; rare earth element
(check chemistry owner: lanthanides are chemistry's; "rare earth element" as
the geochemists' group --- grep before writing); normalised diagram; europium
anomaly; mid-ocean ridge basalt (MORB); ocean island basalt (OIB).

**Recall.** Abundance of elements, periodic table, electronegativity, ionic
radius (chemistry g9 / b1); partition coefficient (chemistry b1
lab-techniques-1); PREM, core density deficit, mantle, crust (Book 3 ch. 9,
10); Moho (Book 3); condensation sequence (ch. 2).

**Figures.** [S] periodic table coloured by Goldschmidt class; [F]
`normalised` CI-normalised REE patterns of MORB, OIB, upper continental crust;
[F] `normalised` primitive-mantle-normalised spider diagram of the same three;
[F] `volatility` CI- and Mg-normalised bulk silicate Earth abundances vs 50%
condensation temperature (lithophile only); [S] pie/bar of Earth mass in
core/mantle/crust with element budgets; [P] a mantle xenolith (peridotite in
basalt, Commons, verify); [AI] a clean-lab scene (generic).

**Ledger.** CI composition (Lodders 2021, Space Sci Rev, CC BY); primitive
mantle (McDonough & Sun 1995 via EarthRef GERM if fetched directly; fallback
Palme & O'Neill open version); MORB mean (Gale et al. 2013, open); OIB
(Sun & McDonough 1989 --- Geol. Soc. Spec. Pub., check access; fallback a
specific OIB reference material: USGS BHVO-2 as an ocean-island tholeiite);
upper crust (Rudnick & Gao 2003, check access); core mass fraction 0.325
(shared or PREM-derived); Earth mass (shared).

**Datasets.** None new (ledger tables written as figdata constants with ledger
ids in comments).

**Weekend problem: "Weighing the core with a chondrite."** Part I bulk Earth
from CI composition corrected for volatile loss (refractory ratios); Part II
Fe and Ni in the bulk silicate Earth vs the bulk Earth; Part III core mass by
mass balance on Fe and Ni (2x2 system, then 3x3 with Si); Part IV what light
element fraction is needed to explain the core density deficit. **Named
number: the core mass fraction of the Earth (per cent).**

---

## Ch. 4 Isotope Geochemistry --- `isotope-geochemistry`

**Hook.** A basalt from Hawaii and one from the East Pacific Rise look the
same in a hand specimen; their strontium and neodymium isotopes say they came
from two different mantles.

**Sections.**
1. Radiogenic tracers: Rb--Sr, Sm--Nd, U--Th--Pb systems (decay constants
   ledger); parent/daughter fractionation during melting (link to
   incompatibility, ch. 3); isotope ratios as fingerprints that melting does
   not change (proposition: isotope ratios are not fractionated measurably by
   melting, admitted for heavy elements).
2. Evolution of reservoirs: the growth equation recalled from Book 3 (isochron);
   CHUR; epsilon notation (definition: εNd); evolution lines of CHUR, depleted
   mantle and continental crust (proposition: εNd(t) linear approximation for
   small λt); complementary reservoirs (proposition: mass balance of εNd
   between crust and depleted mantle).
3. Mantle reservoirs: Sr--Nd isotope array; DMM, HIMU, EM1, EM2 end-members;
   Pb--Pb diagram and the geochron (recall); plume sources and recycling
   (descriptive).
4. Mixing: two-component mixing (proposition: mixing hyperbola, linear in
   ratio vs 1/concentration); assimilation signal (pointer to ch. 8).
5. Crustal growth: Nd model ages told in prose only (Year 3 owns "model age");
   crustal growth curves and their disagreement (ledger: two published
   curves); continental crust mass vs time (descriptive).
6. Stable isotopes: δ value and fractionation factor recalled from chemistry b3
   (statistical-thermo-applied); geological reference standards (VSMOW, VPDB);
   δ18O of the hydrosphere; δ13C of carbon reservoirs (organic vs carbonate,
   ledger); the meteoric water line (proposition: δD ≈ 8 δ18O + 10 from
   Rayleigh condensation --- Rayleigh distillation is Year 3's: state the line
   as an empirical result, ledger Craig 1961, explain qualitatively);
   temperature dependence of fractionation (descriptive, pointer to ch. 24).
7. `inthelab`: isotope-ratio mass spectrometry and clean chemistry (pointer
   to ch. 31).

**Definitions.** radiogenic isotope tracer; chondritic uniform reservoir
(CHUR); epsilon notation (εNd); depleted mantle; enriched mantle; mantle
end-member (DMM, HIMU, EM1, EM2 in one definition); mixing hyperbola (in its
proposition); crustal growth curve; isotope reference standard (VSMOW, VPDB);
meteoric water line (in its proposition). **Not** δ value or fractionation
factor (chemistry b3 owns them; contested with OUTLINE, see report); **not**
model age (Year 3).

**Recall.** δ value, fractionation factor, equilibrium isotope effect
(chemistry b3); isochron, initial ratio, decay chains, closure temperature
(Book 3 ch. 25); mass spectrometry (chemistry b2); incompatible elements,
MORB, OIB (ch. 3).

**Figures.** [F] `epsnd` εNd vs time for CHUR, depleted mantle, a crust
extracted at 2.7 Ga; [F] `mixing` Sr--Nd mantle array with the four
end-members and a mixing hyperbola (end-member values from ledger, labelled
approximate); [S] mantle reservoirs cartoon (ridge, plume, slab, crust); [F]
`deltas` bar chart of δ13C and δ18O of major reservoirs; [S] meteoric water
line with seasonal/latitudinal arrows (points from ledger values, not a
dataset); [AI] a thermal ionisation mass spectrometer lab (generic).

**Ledger.** Decay constants 87Rb, 147Sm, 238U, 235U (shared or Book 3 rows
--- grep first); CHUR present-day 143Nd/144Nd and 147Sm/144Nd (Bouvier et
al. 2008, check open); depleted mantle εNd ~ +10 (source); end-member Sr--Nd
values (review, Stracke 2012 or similar, check open); VSMOW/VPDB definitions
(IAEA pages); Craig 1961 line; δ13C of reservoirs (source); crustal growth
curves (two papers, check open).

**Datasets.** None.

**Weekend problem: "Three islands, three mantles."** Lavas from three invented
islands with Sr, Nd isotopes and concentrations. Part I compute εNd and place
on the mantle array; Part II mixing hyperbola between DMM and an EM-type
recycled sediment; Part III fraction of recycled material for each island;
Part IV εNd evolution of the recycled component since its subduction 2 Ga ago.
**Named number: the mass fraction of recycled sediment in the source of the
most enriched island (per cent).**

---

## Ch. 5 Magmas and Their Emplacement --- `magma-emplacement`

**Hook.** Basalt flows like honey; rhyolite flows like asphalt. The ten
orders of magnitude between their viscosities decide whether a magma reaches
the surface quietly, explodes, or freezes kilometres down.

**Sections.**
1. What a magma is: melt + crystals + bubbles; temperatures of basaltic to
   rhyolitic magmas (ledger); crystal mush.
2. Physical properties: density (proposition: density of a melt from oxide
   partial molar volumes --- or a ledger table, decide in Phase B); viscosity
   recalled from physics; temperature and silica dependence (Arrhenius-like,
   ledger: Giordano et al. 2008 model coefficients if open, else a table of
   measured values); effect of crystals (Einstein--Roscoe relation,
   proposition admitted).
3. Volatiles: H2O and CO2 solubility (Henry-type behaviour recalled from
   chemistry; square-root law for H2O, proposition from H2O -> 2OH speciation,
   admitted); exsolution on ascent; vesiculation; volatile saturation depth.
4. Ascent: buoyancy (recall fluid statics); dyke propagation (descriptive,
   fracture); flow in a dyke (plane Poiseuille recalled from physics b2:
   proposition for mean velocity); diapirs and Stokes ascent (Stokes recalled
   from physics, admitted); ascent rates (ledger).
5. Emplacement: dykes, sills, laccoliths, plutons, batholiths (re-founded with
   geometry and mechanics); level of neutral buoyancy; stoping; incremental
   pluton assembly (descriptive, ledger for a dated example).
6. Cooling and contact metamorphism: conductive cooling of a sill
   (proposition: contact temperature (Tm+T0)/2 from the erf solution of the
   heat equation, recalled; cooling time ~ L^2/κ); latent heat effect
   (descriptive); contact aureole width; hornfels; skarn (told).
7. `inthefield`: how geologists read chilled margins and baked contacts (third
   person).

**Definitions.** magma (re-founded, g4/g7 owner); silicate melt (in the same
definition); crystal mush; magmatic volatile; exsolution (of volatiles);
volatile saturation (pressure); dyke, sill (re-founded from Book 2 g11
igneous-rocks); laccolith; pluton (re-founded); batholith (re-founded from
Book 2 g12); diapir; level of neutral buoyancy; magmatic stoping; chilled
margin; contact aureole (re-founded, Book 2 g12 metamorphism); hornfels;
skarn.

**Recall.** Viscosity, Poiseuille flow, Stokes law (physics b2 viscous flows);
heat equation, diffusivity (physics b2 heat conduction); Henry's law
(chemistry b2); buoyancy (physics b1 fluid statics); lithostatic pressure
(Book 3); geotherm (Book 3); felsic/mafic, phenocryst, porphyritic (Book 2).

**Figures.** [F] `viscosity` viscosity vs temperature for basalt, andesite,
rhyolite (ledger-sourced values) on a log axis; [F] `solubility` H2O solubility
vs pressure (square-root law with sourced constant) and the saturation depth;
[F] `sill_cooling` temperature profiles through a cooling sill and its wall
rock at four times (erf solution); [S] emplacement block diagram: dyke, sill,
laccolith, pluton, batholith, stoped blocks, aureole; [S] neutral buoyancy
level vs depth (density profiles); [P] Shiprock radial dykes or a sill photo
(Commons, verify); [P] a chilled margin / xenolith photo (verify); [AI] a
geologist sampling a basalt dyke (generic, observation only).

**Ledger.** Magma temperatures; viscosities (basalt ~10--100 Pa s, rhyolite
~10^8 Pa s at eruption T; sourced); melt densities; H2O solubility constant;
thermal diffusivity (physics books or source); ascent rates of kimberlite and
basalt; Shiprock dyke dimensions if used; incremental pluton example ages.

**Datasets.** None.

**Weekend problem: "The sill under the plateau."** An invented 100-m dolerite
sill in shale. Part I buoyancy and ascent of the feeding dyke (width 2 m,
Poiseuille); Part II volatile exsolution depth; Part III contact temperature,
width of the zone above 300 °C; Part IV time to solidify (L^2/κ with latent
heat correction). **Named number: the time the sill takes to solidify
(years).**

---

## Ch. 6 Volcanic Eruptions --- `eruptive-styles`

**Hook.** In 1991 Pinatubo put ten cubic kilometres of magma into the sky in
nine hours and cooled the planet by half a degree; Kīlauea pours out lava for
decades and hardly anyone outside Hawaii notices.

**Sections.**
1. Effusive or explosive: role of viscosity and volatiles (recall ch. 5);
   fragmentation (descriptive criterion: gas volume fraction ~ 0.75, ledger);
   magma--water interaction.
2. Eruptive styles: Hawaiian, Strombolian, Vulcanian, Plinian (and
   sub-Plinian), phreatomagmatic, phreatic; dome growth; each with a type
   eruption (ledger dates and numbers).
3. Eruption columns: jet, convective and umbrella regions; column height vs
   mass eruption rate (proposition: H ∝ Q^{1/4} from plume theory admitted;
   empirical fit, ledger Mastin et al. 2009); column collapse.
4. Pyroclastic products: tephra, pyroclasts (ash, lapilli, bombs); fall
   deposits and thinning laws (proposition: exponential thinning, volume by
   integration, Pyle 1989 method); pyroclastic density currents (flows and
   surges), ignimbrites; lahars; calderas.
5. Measuring size: Volcanic Explosivity Index (definition with the volume
   steps); magnitude scale (descriptive); frequency--size law from the GVP
   catalogue (proposition: power law fitted, completeness discussed).
6. Monitoring: seismicity, deformation (Mogi point source, proposition admitted
   with uplift formula; InSAR told only: Year 3), gas fluxes (SO2), thermal;
   alert levels (descriptive, no policy); eruption forecasting limits.
7. `inthefield` volcano observatory work (third person).

**Definitions.** effusive eruption, explosive eruption (both re-founded, Book 1
g7 `volcanoes`); magma fragmentation;
Hawaiian eruption; Strombolian eruption; Vulcanian eruption; Plinian eruption;
phreatomagmatic eruption; phreatic eruption; lava dome; eruption column;
tephra; pyroclast; volcanic bomb; lapilli; pyroclastic density current;
pyroclastic flow (re-founded from g4/g7); pyroclastic surge; ignimbrite;
lahar; caldera; Volcanic Explosivity Index (owner per OUTLINE; re-founds g7
"eruptive styles" which Book 1 treats descriptively --- check g7 index:
`eruptive style` / `VEI` not indexed at school per harvest); Mogi source
(in its proposition).

**Recall.** Volcano, magma chamber, lava, crater, vent, volcanic ash (Book 1
g4); viscosity (physics); volatiles, exsolution (ch. 5); hazard vocabulary
(ch. 28 forward pointer); seismic moment (Book 3).

**Figures.** [S] eruptive styles panel (six styles, column heights to scale);
[S] eruption column anatomy; [F] `thinning` isopach thinning (ln T vs sqrt
area) for a sourced deposit (Pyle 1989 Mount St Helens or Pinatubo data,
ledger) and the volume; [F] `vei_frequency` cumulative number of Holocene
eruptions vs VEI from GVP (completeness window marked); [F] `column_height`
height vs mass eruption rate with sourced eruptions; [F] `mogi` uplift
profile; [P] Mount St Helens 18 May 1980 (USGS PD, verify file); [P] Pinatubo
1991 column (USGS PD, verify); [P] Kīlauea fountain (USGS PD); [AI]
observatory interior with seismograph drums (generic).

**Ledger.** Pinatubo 1991 volume, column height, cooling 0.5 °C (USGS/
literature); Mount St Helens 1980 numbers; Kīlauea 1983--2018 volume;
Tambora 1815; VEI definition table (Newhall & Self 1982); Mastin 2009
relation; fragmentation threshold; Mogi formula source; GVP dataset (shared
data row extended).

**Datasets.** `bachelor-2-gvp-eruptions` (GVP WFS Holocene eruptions CSV,
VEI, start year; Smithsonian GVP terms as for the shared `gvp` set).

**Weekend problem: "Reading a Plinian deposit."** Part I isopach thinning and
tephra volume of an invented deposit; Part II dense-rock equivalent and VEI;
Part III column height from the mass eruption rate (duration given); Part IV
frequency of such eruptions from the GVP power law; probability of at least
one in a century. **Named number: the probability of at least one VEI ≥ 6
eruption on Earth in the next 100 years (per cent).**

---

## Ch. 7 Melting the Mantle --- `mantle-melting`

**Hook.** The mantle is solid, yet 20 cubic kilometres of new oceanic crust
are made from it every year. Rocks melt not because they get hotter but
because the pressure on them drops.

**Sections.**
1. The mantle rock: peridotite (re-found), lherzolite, harzburgite, dunite;
   modal mineralogy (ledger); fertile vs depleted mantle.
2. Phase diagrams applied to rocks: binary eutectic (recall chemistry solidus,
   liquidus, eutectic, lever rule) with the Di--An system (Bowen 1915 data);
   binary with solid solution (Fo--Fa, recall); incongruent melting and the
   peritectic (Fo--SiO2, enstatite); ternary diagrams (definition: ternary
   phase diagram, cotectic line, ternary eutectic; reading with the lever rule)
   with Di--An--Fo (descriptive reading). Year 3 owns the phase rule and
   pseudosections: mention with a pointer.
3. Solidus and geotherm: peridotite solidus (dry, wet) vs depth (ledger /
   Katz et al. 2003 parametrisation); the mantle adiabat and potential
   temperature (recall Book 3; qualified "mantle potential temperature");
   three ways to melt: decompression, flux (hydrous), heating.
4. Decompression melting: adiabatic upwelling crossing the solidus
   (proposition: depth where melting starts); productivity dF/dP (proposition
   from an energy balance with latent heat; ~10%/GPa); melt column; crustal
   thickness from the triangular melting region (proposition: integral of F
   over the column, Year-2 integral).
5. Flux melting in subduction zones: water lowers the solidus (ledger); slab
   dehydration (recall Book 3 ch. 14); hydrous melting of the wedge.
6. Degree of melting and melt extraction: melt fraction; primary magma;
   porosity and melt segregation (descriptive); residues (harzburgite);
   Mg number of melts and residue (recall Book 3).
7. `inthefield` mantle xenoliths and ophiolite peridotites (third person).

**Definitions.** peridotite (re-founded, Book 2 g11.05); lherzolite;
harzburgite; dunite; fertile mantle; depleted mantle (rock, distinct from the
isotopic reservoir? --- one definition in ch. 4 serves; here "residual
mantle"): use **residual mantle** to avoid duplication; incongruent melting;
peritectic point; ternary phase diagram (contested with Y3
petrological-thermodynamics, see report); cotectic line; ternary eutectic
(in the same definition); partial melting (re-founded, Book 2 g11.05; OUTLINE
Y2 owner); decompression melting (re-founded); flux melting (re-founds Book 2
"hydrous melting"; both indexed); melt fraction; melt productivity (in its
proposition); primary magma; mantle potential temperature (qualified;
check Book 3 ch. 10 does not define "potential temperature" for the mantle ---
Book 3 defines atmospheric potential temperature ch. 26 and "mantle adiabat"
ch. 10).

**Recall.** Solidus, liquidus, eutectic point, lever rule, congruent melting,
binary diagram, solid solution (chemistry b2); solid solution (mineral),
end-member, Mg number, olivine, pyroxene, garnet, spinel (Book 3); mantle
adiabat, geotherm, lithosphere/asthenosphere (Book 3); latent heat (physics);
slab, Wadati--Benioff zone (Book 3).

**Figures.** [F] `bowen` Di--An binary from Bowen 1915 liquidus points;
[F] `fo_sio2` Fo--SiO2 with the peritectic (Bowen & Andersen 1914 points);
[S] ternary Di--An--Fo with cotectics and a crystallisation path (ternary
pgfplots, points from sourced data); [F] `katz_melting` solidus, liquidus,
adiabats for Tp = 1300, 1350, 1450 °C, melting onset; [F] `katz_melting` F vs
depth along the adiabat and crustal thickness vs Tp; [S] three ways to melt
(P--T sketch with arrows, curves from the same figdata where possible);
[S] triangular melting region under a ridge; [P] mantle xenolith (if not used
in ch. 3, else ophiolite peridotite); [AI] none.

**Ledger.** Bowen 1915 Di--An eutectic (1274 °C, An42 by mass) and liquidus
points; Bowen & Andersen 1914 Fo--SiO2 peritectic; Katz et al. 2003
parameters (A1, A2, A3 etc.; check open access); mantle potential temperature
1350 °C ± (source); oceanic crust thickness 6--7 km (White et al. 1992 or
newer); production rate of oceanic crust (km^3/yr, source); latent heat and
heat capacity of peridotite; wet solidus lowering.

**Datasets.** None (published parameters).

**Weekend problem: "Under the ridge."** Part I read the solidus/adiabat
diagram, onset depth for Tp = 1350 °C; Part II productivity and melt fraction
at the top; Part III triangular region and mean melt fraction; Part IV crustal
thickness; sensitivity to Tp (a plume 150 °C hotter: Iceland). **Named
number: the thickness of oceanic crust made at a normal ridge (km).**

---

## Ch. 8 Magmatic Differentiation --- `magmatic-differentiation`

**Hook.** From one basalt a volcano can erupt, over a few thousand years,
andesite, dacite and rhyolite. The magma did not change its source; it
changed itself.

**Sections.**
1. Crystallisation sequences: Bowen's reaction series revisited (discontinuous
   and continuous branches; descriptive with chemistry recall); equilibrium vs
   fractional crystallisation (definitions); liquid line of descent.
2. Fractional crystallisation of major elements: Harker diagrams; mass balance
   of crystal removal (proposition: lever rule in composition space; 3x3
   least-squares fit of a parent = daughter + minerals, method box).
3. Trace elements: bulk partition coefficient (proposition: D = Σ x_i K_i);
   **Rayleigh fractionation law** (theorem, derived from the differential mass
   balance, C_L/C_0 = F^{D-1}); equilibrium crystallisation law (proposition:
   C_L/C_0 = 1/(D + F(1-D))); compatible elements plunge, incompatible ones
   rise; ratio of two incompatible elements stays constant (corollary).
   Year 3 owns batch and fractional *melting* models: pointer only.
4. Cumulates and layered intrusions: cumulus crystals, cumulate textures,
   layering, Skaergaard and Bushveld (ledger facts, descriptive).
5. Open systems: magma mixing (proposition: linear mixing in concentration
   space; hyperbola in ratio space recalled from ch. 4); assimilation;
   assimilation--fractional crystallisation (AFC) told with the DePaolo 1981
   equation admitted; isotopic evidence of assimilation.
6. `inthelab` reading zoned crystals (third person, microprobe pointer ch. 31).

**Definitions.** equilibrium crystallisation; fractional crystallisation
(re-founded, Book 2 g11 igneous rocks; OUTLINE Y2 owner); liquid line of
descent; Harker diagram; bulk partition coefficient; Rayleigh fractionation law
(in its theorem); cumulate; layered intrusion; magma mixing; assimilation
(magmatic) --- qualified "crustal assimilation"; assimilation--fractional
crystallisation (AFC); zoned crystal (descriptive) --- "compositional
zoning".

**Recall.** Partition coefficient, compatible/incompatible element (ch. 3);
mixing hyperbola, εNd (ch. 4); Bowen's reaction series (Book 2 g11 --- check
indexed; harvest shows not indexed: define "Bowen's reaction series" here? It
is a school notion in prose only: **define here**, earliest formal use);
solid solution, plagioclase zoning (Book 3); lever rule (chemistry).

**Figures.** [S] Bowen's reaction series; [F] `rayleigh` C_L/C_0 vs F for D =
0.01, 0.1, 0.5, 1, 2, 5, 10 (fractional vs equilibrium dashed); [F] `harker`
Harker diagrams for a sourced volcanic suite (USGS reference materials or a
published suite; decide Phase B); [S] layered intrusion cross-section with
cumulate layers; [F] `afc` or mixing line Sr isotope vs 1/Sr; [P] Bushveld
chromitite layering or Skaergaard layering (Commons, verify); [P] zoned
plagioclase under crossed polars (Commons, verify); [AI] none.

**Ledger.** Bowen series sources (Bowen 1922 or 1928, PD pre-1929 check);
partition coefficients for Ni, Cr, Rb, Zr, Sr in olivine/plagioclase/
clinopyroxene (GERM / a cited compilation, open); Skaergaard and Bushveld facts
(ages, sizes); DePaolo 1981 equation.

**Datasets.** A volcanic suite analyses table (Phase B: a published open
dataset or USGS reference materials as stand-ins).

**Weekend problem: "The intrusion that wrote its own history."** An invented
layered gabbro with Ni and Zr measured up-section. Part I bulk D for Ni and Zr
from the mode; Part II Rayleigh curves; Part III least-squares mass balance of
the top liquid (3x3); Part IV fraction of liquid left at the sandwich horizon.
**Named number: the fraction of the original magma still liquid when the
uppermost layer crystallised (per cent).**

---

## Ch. 9 Magmatic Series and Tectonic Settings --- `magmatic-series`

**Hook.** Hand a petrologist a chemical analysis and no map, and she can often
say whether the lava erupted at a ridge, an island or above a subducting
plate.

**Sections.**
1. Classifying igneous rocks: modal classification (QAPF diagram, definition
   with field coordinates from the IUGS scheme, ledger); chemical
   classification: total alkali--silica (TAS) diagram (definition; field
   boundaries from Le Bas et al. 1986, ledger); silica saturation (normative
   quartz vs nepheline, descriptive; CIPW norm told, method box with a
   simplified recipe? decide Phase B, keep short).
2. Magmatic series: tholeiitic, calc-alkaline, alkaline (definitions); AFM
   diagram (Irvine & Baragar 1971 dividing line, ledger); FeO*/MgO vs SiO2
   (Miyashiro 1974, ledger); K2O--SiO2 subdivisions (Peccerillo & Taylor 1976,
   ledger); why the series differ (oxygen fugacity, water, magnetite
   crystallisation: descriptive, linked to ch. 8).
3. Settings: mid-ocean ridges (MORB tholeiites); oceanic islands (tholeiitic
   shield then alkaline caps, link ch. 17); arcs (calc-alkaline, Nb--Ta
   anomaly on spider diagrams, recall ch. 3); continental rifts (alkaline,
   bimodal); continental flood basalts (LIPs recalled from Book 3).
4. Isotopic signatures by setting (recall ch. 4): MORB depleted, OIB variable,
   arcs with slab and sediment input (10Be told, ledger optional).
5. Discrimination diagrams and their limits (one trace-element diagram, e.g.
   Ti--Zr--Y or Th/Yb vs Nb/Yb of Pearce 2008, ledger; method box "how to use
   and not abuse").
6. `inthelab` how a whole-rock analysis is checked (totals, LOI; pointer
   ch. 31).

**Definitions.** QAPF diagram; modal composition; total alkali--silica
diagram (owner per OUTLINE); silica saturation (silica-oversaturated,
-undersaturated in one definition); magmatic series (owner per OUTLINE);
tholeiitic series; calc-alkaline series; alkaline series; AFM diagram;
bimodal volcanism; discrimination diagram; normative mineralogy (CIPW norm)
--- only if section 1 keeps it.

**Recall.** Basalt, andesite, rhyolite, granite, gabbro (Book 2 g11/g12);
felsic, mafic (Book 2); MORB, OIB, normalised diagrams (ch. 3); isotope
reservoirs (ch. 4); fractional crystallisation, Harker diagram (ch. 8); LIP,
hotspot, volcanic arc (Book 3 ch. 14--15); continental rift (Book 3 ch. 12).

**Figures.** [F] `tas` TAS diagram with fields and USGS reference rocks
plotted (BHVO-2, BCR-2, AGV-2, RGM-2 and a phonolite/alkali basalt standard);
[F] `afm` AFM diagram with Irvine--Baragar line and the same samples; [S] QAPF
double triangle (field coordinates sourced); [F] `k2o_sio2` K2O vs SiO2
series fields; [S] world map of settings with the four series (shared geo
tables); [F] spider diagrams of a MORB, OIB, arc basalt (sourced analyses) to
show the Nb--Ta trough; [AI] none; [P] none (pages heavy with diagrams).

**Ledger.** Le Bas et al. 1986 TAS coordinates (check access; Le Maitre 2002
IUGS book table as fallback, not open: then quote coordinates from an open
restatement with the original cited); IUGS QAPF; Irvine & Baragar 1971;
Peccerillo & Taylor 1976; USGS reference material certificate values (SiO2,
Na2O, K2O, FeO*, MgO); arc basalt analysis; Pearce 2008 diagram line.

**Datasets.** None (certificate values via ledger as figdata constants).

**Weekend problem: "One volcano, three lavas."** Three invented analyses from
one stratovolcano. Part I recalculate anhydrous, plot on TAS; Part II AFM and
K2O--SiO2: which series; Part III spider diagram features: setting; Part IV
3x3 least-squares mass balance andesite = basalt − (olivine + plagioclase +
clinopyroxene). **Named number: the mass of crystals removed per 100 kg of
parent basalt to make the andesite (kg).**

---

## Ch. 10 Metamorphic Reactions and Facies --- `metamorphic-facies`

**Hook.** A blue rock found high in the Alps formed thirty kilometres down and
cold; a red-and-white rock found next to a granite formed one kilometre down
and hot. Their minerals are thermometers and barometers that never reset.

**Sections.**
1. Metamorphism re-founded: agents (T, P, fluids, deformation); protolith;
   types (regional, contact, burial, ocean-floor, shock, dynamic) with
   settings (recall Book 3 margins).
2. Metamorphic reactions: solid--solid, devolatilisation (dehydration,
   decarbonation); univariant reaction lines in P--T space; **Clapeyron slope
   of a reaction** (proposition: dP/dT = ΔS/ΔV, from dG = V dP − S dT along
   equilibrium; the Clausius--Clapeyron relation is physics', this is its
   solid--solid form); sign and steepness of solid--solid vs dehydration
   reactions (dehydration curves bend).
3. The Al2SiO5 system: kyanite, andalusite, sillimanite; computing the three
   reaction lines from thermodynamic data (Robie & Hemingway 1995, ΔH, S, V;
   method box: ΔG(P,T) ≈ ΔH − TΔS + PΔV at constant ΔCp=0, then the
   correction); the invariant (triple) point (proposition: intersection of two
   lines, 2x2 system); comparison with experiment (Holdaway 1971).
4. Mineral assemblages and equilibrium: an assemblage records the conditions;
   the phase rule as a Year-3 tool (pointer, not used); compatibility
   diagrams told only (AFM projection = Year 3).
5. Metamorphic facies: facies grid (definition; facies names: zeolite,
   prehnite--pumpellyite, greenschist, amphibolite, granulite, blueschist,
   eclogite, hornfels facies); diagnostic assemblages of metabasites and
   metapelites; facies series and gradients (pointer ch. 11).
6. Protolith matters: metapelite, metabasite, marble, quartzite, calc-silicate
   (descriptive names with their mineral sequences).
7. `inthelab` how reaction curves are bracketed in piston-cylinder experiments
   (third person).

**Definitions.** metamorphism (re-founded, Book 2 g12.03); protolith;
metamorphic reaction; devolatilisation reaction; univariant reaction (owner per
OUTLINE); Clapeyron slope (qualified: "Clapeyron slope (of a reaction)" ---
physics owns Clausius--Clapeyron; contested, see report); invariant point;
aluminosilicate polymorphs (kyanite, andalusite, sillimanite); mineral
assemblage; metamorphic facies (qualified form, owner per OUTLINE and Sync 1);
facies grid; metapelite; metabasite; ocean-floor metamorphism (or in ch. 11:
decide one; planned **ch. 11**).

**Recall.** Gibbs energy, enthalpy, entropy (chemistry b1/b2
thermochemistry; physics); Clausius--Clapeyron relation, triple point
(physics b1 phase changes); polymorph (Book 3 ch. 2 / Book 2); contact/
regional metamorphism, aureole, index mineral, isograd (Book 2 g12.03);
foliation, schistosity (Book 3 ch. 17); blueschist, eclogite (Book 2 g11.06);
lithostatic pressure (Book 3).

**Figures.** [F] `al2sio5` computed Al2SiO5 diagram with three lines and the
triple point, Holdaway point overplotted; [F] `al2sio5` ΔG vs T at 4 kbar for
the three polymorphs; [F] `dehydration` a dehydration reaction curve
(muscovite + quartz) from sourced data (curved); [S] facies grid
(boundaries from a sourced open diagram, anchor lines computed; caption says
approximate); [S] crystal structures of the three polymorphs (Al coordination
4/5/6, simplified); [P] kyanite blades or andalusite chiastolite (Commons,
verify); [P] blueschist outcrop or eclogite hand specimen (Commons, verify);
[AI] a piston-cylinder laboratory (generic).

**Ledger.** Robie & Hemingway 1995 data for kyanite, andalusite, sillimanite
(USGS Bull. 2131, PD); Holdaway 1971 triple point (AJS, verify access) and
Pattison 1992 alternative; muscovite + quartz reaction data; facies grid
source (open; Phase B search); typical metamorphic conditions (ledger rows for
each facies' P--T range quoted).

**Datasets.** None (thermodynamic constants via ledger).

**Weekend problem: "Building the triple point."** Part I Clapeyron slopes of
the three reactions from ΔS and ΔV; Part II ΔG at 25 °C, 1 bar; position of
each line; Part III the triple point by solving the 2x2 system, check the third
line passes through it; Part IV what a 1 kJ/mol error in ΔH does to the triple
point (sensitivity, partial derivatives). **Named number: the temperature of
the Al2SiO5 triple point computed from the data (°C).**

---

## Ch. 11 Thermobarometry and P--T--t Paths --- `pt-paths`

**Hook.** A single garnet a few millimetres across records how deep a rock was
buried, how hot it got and how fast it came back up --- if one knows how to
read it.

**Sections.**
1. Metamorphic zones re-founded: index minerals, isograds, Barrovian zones
   (chlorite, biotite, garnet, staurolite, kyanite, sillimanite; ledger for
   the Scottish type area, named as a real place); metamorphic field gradient.
2. Thermobarometry: exchange thermometers (proposition: ln K_D = −ΔH/RT +
   ΔS/R − PΔV/RT; garnet--biotite Ferry & Spear 1978 calibration, ledger);
   net-transfer barometers (GASP, ledger); intersection of a thermometer and a
   barometer (2x2 solve, method box); uncertainties (partial-derivative error
   propagation, Year-2 math).
3. P--T paths: prograde and retrograde paths; clockwise path after thickening
   (proposition: thermal relaxation of a thickened crust from the heat
   equation, numerical solution in figdata; England & Thompson 1984 told);
   anticlockwise paths (magmatic heating, descriptive); peak conditions vs peak
   temperature.
4. P--T--t paths: adding time with geochronology (closure temperatures
   recalled from Book 3); cooling and exhumation rates (proposition: dT/dt and
   dz/dt from ages and closure temperatures).
5. Metamorphic series: high P/T (subduction), medium P/T (Barrovian), low P/T
   (Buchan, contact); paired metamorphic belts (descriptive, ledger for Japan
   as a real place).
6. UHP metamorphism and exhumation: coesite and diamond (ledger: Dora Maira,
   Kokchetav); exhumation mechanisms (buoyancy, erosion, extension;
   descriptive); exhumation rates (ledger).
7. Ocean-floor metamorphism: hydrothermal circulation at ridges, greenschist
   facies basalts, serpentinisation (recall Book 3 oceanic crust).
8. `inthelab` reading inclusion trails and zoning (pointer ch. 31).

**Definitions.** metamorphic zone (re-founded, Book 2 g12.03 "metamorphic
grade/index mineral/isograd" --- those three recalled, not redefined; this
chapter defines "Barrovian zones" and "metamorphic field gradient");
Barrovian zones; metamorphic field gradient; geothermometer; geobarometer;
exchange reaction (thermometric); net-transfer reaction; prograde path;
retrograde path; P--T path; P--T--t path (owner per OUTLINE); peak metamorphic
conditions; metamorphic series; paired metamorphic belts; ultrahigh-pressure
metamorphism; exhumation; exhumation rate; ocean-floor metamorphism;
serpentinisation (check Book 3: serpentinite may be defined in ch. 13 ---
grep at writing).

**Recall.** Index mineral, isograd, metamorphic grade (Book 2); closure
temperature, cooling age (Book 3 ch. 25); heat equation, diffusivity
(physics b2); radiogenic heat production, geotherm (Book 3 ch. 10); facies,
univariant reactions, triple point (ch. 10); equilibrium constant (chemistry).

**Figures.** [F] `pt_path` geotherms after instantaneous doubling of crustal
thickness at 0, 10, 30, 60 Myr; [F] `pt_path` clockwise P--T path of a rock at
35 km with erosion, over the facies grid lines; [F] `thermobarometer`
garnet--biotite isopleths and GASP line intersecting; [S] Barrovian zone map
(Varden-style invented map? no: a schematic of the type area with ledger
isograds, simplified); [S] metamorphic series on P--T with three gradients;
[P] garnet porphyroblast in mica schist (Commons, verify); [P] coesite
inclusion (Commons, verify); [AI] none.

**Ledger.** Ferry & Spear 1978 calibration; GASP calibration (Koziol & Newton
1988); Barrovian zones (Barrow 1893, PD); Dora Maira coesite (Chopin 1984)
pressures, ages; exhumation rates (Rubatto & Hermann 2001 or open review);
closure temperatures (Book 3 rows if present); crustal conductivity and heat
production (Book 3 rows or source).

**Datasets.** None.

**Weekend problem: "A garnet's journey."** An invented schist with garnet core
and rim analyses and two ages. Part I garnet--biotite temperatures for core and
rim; Part II GASP pressures and depths; Part III the P--T path and its sense;
Part IV with a 40Ar/39Ar muscovite age and a garnet Sm--Nd age, cooling and
exhumation rates. **Named number: the average exhumation rate from peak to
the muscovite closure (mm per year).**

---

## Ch. 12 Crustal Melting: Migmatites and Granites --- `crustal-melting`

**Hook.** Granite makes the continents float, yet the mantle cannot make it
directly. Granite is the crust melting itself.

**Sections.**
1. Why the crust melts: wet granite solidus vs dehydration-melting reactions
   (muscovite, biotite, amphibole; ledger curves); heat sources (thickening and
   radiogenic heat ch. 11, mafic underplating, decompression).
2. Anatexis and migmatites: leucosome, melanosome, mesosome/palaeosome;
   metatexite vs diatexite; melt fractions vs temperature for a metapelite
   (proposition: melt fraction from a dehydration reaction stoichiometry, mass
   balance).
3. Melt segregation and ascent: compaction, dykes (recall ch. 5), granite
   plutons from migmatites (descriptive, ledger for the time scales).
4. Granite types: I, S, A (and M) types; aluminium saturation index (definition
   and proposition: ASI = Al2O3/(CaO + Na2O + K2O) molar); peraluminous,
   metaluminous, peralkaline; minerals that betray each (muscovite, cordierite,
   hornblende, aegirine); leucogranites of collision belts (link ch. 14).
5. Granites through time and the growth of continents (descriptive, link
   ch. 4 and ch. 18: TTG vs modern granites).
6. `inthefield` reading a migmatite outcrop (third person).

**Definitions.** anatexis; migmatite; leucosome; melanosome; metatexite;
diatexite; dehydration melting; fluid-present melting; aluminium saturation
index; peraluminous; metaluminous; peralkaline (three in one definition);
I-type granite; S-type granite; A-type granite (one definition: granite
typology); leucogranite; mafic underplating.

**Recall.** Granite, granitoid, granodiorite (Book 2 g12.01/g12.04); partial
melting (ch. 7); metapelite, facies (ch. 10); P--T path (ch. 11); felsic;
radiogenic heat production (Book 3).

**Figures.** [F] `crustal_solidi` wet granite solidus, muscovite and biotite
dehydration melting curves, geotherms (sourced points); [F] `asi` ASI
(A/CNK vs A/NK) diagram with USGS granites (G-2, GSP-2) and an invented
S-type; [S] migmatite structures (four sketches); [S] from migmatite to
pluton cartoon; [P] migmatite outcrop (Commons, verify); [P] leucogranite
(Himalaya, Commons, verify); [AI] none.

**Ledger.** Wet granite solidus (Tuttle & Bowen 1958 points; PD? check);
dehydration-melting curves (open experimental source); Chappell & White 1974/
2001 I/S types; Shand 1943 ASI; USGS G-2, GSP-2 certificates; Himalayan
leucogranite ages.

**Datasets.** None.

**Weekend problem: "A pluton from melted mica."** Part I muscovite
dehydration reaction stoichiometry: melt produced per kg of metapelite; Part
II temperature reached on the clockwise path of ch. 11 and which reactions
crossed; Part III ASI of the melt; classify; Part IV volume of crust that must
melt to build an invented 1000 km^3 leucogranite pluton. **Named number: the
volume of source crust melted to make the pluton (km^3).**

---

## Ch. 13 Anatomy of a Mountain Belt: The Alps --- `alpine-orogen`

**Hook.** At the top of the Matterhorn stands a piece of Africa; its base sits
on the floor of an ocean that closed fifty million years ago.

**Sections.**
1. A vanished ocean: the Alpine Tethys (Piemont--Liguria and Valais basins);
   rifting in the Jurassic (recall Book 3 passive margins); ophiolites as its
   relics (re-founded: Penrose sequence, ledger), their dating (ledger).
2. Building the belt: subduction of the ocean, then of the European margin;
   continental subduction and HP/UHP rocks (link ch. 11: Dora Maira, Zermatt--
   Saas eclogites, ledger); collision.
3. Nappes: definition re-founded; nappe stack of the Western/Central Alps
   (Helvetic, Penninic, Austroalpine, Southern Alps; ledger Schmid et al.
   2004); klippen and tectonic windows (Matterhorn klippe; Tauern and
   Engadine windows); thin- and thick-skinned tectonics; décollement; the
   Jura fold--thrust belt (descriptive).
4. Foreland basins: flexural loading told (flexure is Year 3: pointer;
   descriptive only); flysch and molasse; the Molasse basin and the Po plain.
5. Reading the history: from maps (recall geological maps, Book 3 ch. 4) and
   cross-sections (balanced section principles: line-length and area balance,
   proposition for shortening = 1 − l/l0); geophysics: deep seismic
   reflection (ECORS--CROP, NFP-20; ledger), Moho depth beneath the Alps
   (ledger), gravity (recall Bouguer anomalies Book 3).
6. Timeline: Jurassic rifting to present uplift (dated table, ledger).
7. `inthefield` reading a thrust contact (third person).

**Definitions.** ophiolite (re-founded, Book 2 g12.02); Penrose ophiolite
sequence (inside ophiolite definition); obduction; continental subduction;
nappe (re-founded, Book 2 g12.02); nappe stack; klippe; tectonic window;
décollement; thin-skinned tectonics; thick-skinned tectonics; fold--thrust
belt; foreland basin; flysch; molasse; balanced cross-section; shortening
(re-founded, Book 2 g12.02; recalled? --- Book 2 owns "shortening": recall,
define "balanced cross-section" only); suture (recalled from Book 2, not
redefined); orogen (check: "mountain belt"/"orogeny" owners --- grep
writing; Book 2 g12.02 likely owns "orogeny").

**Recall.** Geological map, cross-section, V-rule (Book 3 ch. 4); thrust,
reverse fault, fold elements (Book 3 ch. 16--17); passive margin, rift (Book 3
ch. 12); oceanic crust structure (Book 3 ch. 13); subduction, accretionary
prism (Book 3 ch. 14); eclogite, blueschist (Book 2); continental collision,
suture, shortening (Book 2 g12.02); Bouguer anomaly, isostasy (Book 3 ch. 11);
P--T paths (ch. 11).

**Figures.** [S] simplified tectonic map of the Alps (units coloured,
redrawn after Schmid et al. 2004, with ledger rows for every label; coastline
and borders from shared geo tables or ETOPO subset); [F] `alps_profile`
topographic profile across the Western Alps from ETOPO subset with mean
elevation and Moho depth (ledger points); [S] cross-section NW--SE (Jura --
Molasse -- Helvetic -- Penninic -- Austroalpine -- Southern Alps), simplified
from NFP-20/ECORS-CROP interpretation; [S] evolution in four stages (rift,
subduction, continental subduction, collision); [S] klippe and window block
diagram; [P] Matterhorn (Commons, verify); [P] ophiolite pillow basalts or
serpentinite in the Alps (Commons, verify); [AI] none.

**Ledger.** Schmid et al. 2004 (e-periodica, free) units and ages; ocean
opening/closure ages; Zermatt--Saas eclogite age and P--T; Dora Maira
coesite (ch. 11 row reuse); Moho depths beneath the Alps (open source); total
shortening estimates (sourced); Molasse basin thickness; peak elevations
(ledger, e.g. Mont Blanc 4806 m: check modern value).

**Datasets.** `bachelor-2-etopo-alps` (ERDDAP ETOPO 1-arc-minute subset,
45--48.5 N, 5--12 E, stride 2: ~200x400 points; NOAA PD).

**Weekend problem: "Restoring the section."** A simplified Alpine-type section
(invented geometry, labelled as a model) with marker beds. Part I measure bed
lengths (line-length balance); Part II area balance and depth to the
décollement; Part III shortening and rate given ages; Part IV width of the
vanished ocean from the ophiolite-bearing unit's restored length plus
subducted length (from convergence rate x time). **Named number: the total
shortening across the section (km).**

---

## Ch. 14 Collision and Andean Belts Compared --- `himalaya-andes`

**Hook.** Two plateaus stand higher than four kilometres over areas larger
than many countries: Tibet, made by two continents colliding, and the
Altiplano, made by an ocean sliding under a continent.

**Sections.**
1. India meets Asia: convergence history (ledger: India's northward drift,
   collision age ~50 Ma), the Indus--Yarlung suture, Himalayan units (Tethyan
   Himalaya, Greater Himalayan sequence, Lesser Himalaya, Siwaliks), the Main
   Central and Main Boundary Thrusts and the Main Frontal Thrust; leucogranites
   (link ch. 12); channel flow told as a hypothesis (no definition).
2. Tibet: crustal thickness (proposition: Airy root recalled, crust thickness
   from mean elevation; ledger seismic Moho 60--80 km); gravitational potential
   energy and gravitational collapse (proposition: excess potential energy per
   unit area of a thickened column, integral of lithostatic pressure
   difference); east--west extension (grabens); lateral extrusion (descriptive,
   GPS velocities ledger).
3. The Andes: Andean-type orogen; Nazca subduction (rate ledger); volcanic
   zones and flat-slab segments (link Book 3 ch. 14); Altiplano--Puna plateau;
   crustal thickening by shortening vs magmatic addition (proposition: crustal
   thickening from shortening, area balance); delamination (descriptive).
4. Comparing: table collision vs Andean (driving, magmatism, metamorphism,
   seismicity, plateau, basins); topographic profiles (figdata).
5. Mountain heights limited (proposition: maximum height from crustal
   strength or isostasy, simple estimate, ledger for Everest 8849 m).
6. `inthefield` GPS geodesy on plateaus (third person).

**Definitions.** collision orogen (qualified; check "continental collision"
owner Book 2 g12.02 --- recall it, define "collision orogen" only if not
owned); Andean-type orogen (cordilleran orogen); orogenic plateau; crustal
thickening; gravitational collapse (of an orogen); lateral extrusion
(escape tectonics); flat-slab subduction; lithospheric delamination;
foreland--hinterland (prose only).

**Recall.** Airy isostasy, isostasy (Book 3 ch. 11); continental collision,
suture, nappe, mountain root (Book 2); subduction, volcanic arc, slab dip,
active margin (Book 3 ch. 14); leucogranite (ch. 12); foreland basin, thrust
(ch. 13); GPS velocities (Book 3).

**Figures.** [F] `profiles` topographic swath profiles across the Himalaya--
Tibet and the Central Andes (ETOPO subsets) with mean elevation and Airy root
computed below; [S] simplified Himalayan cross-section (MFT, MBT, MCT, STDS,
suture); [S] Andean cross-section (trench, forearc, arc, Altiplano, Eastern
Cordillera, Subandean belt); [S] potential energy columns (normal vs
thickened); [S] India's northward drift map (positions from a sourced table:
redrawn on shared geo base) --- careful: APW is Year 3; plot positions only,
cite; [P] Himalaya from orbit (NASA PD, verify); [P] Altiplano (Commons,
verify); [AI] none.

**Ledger.** India--Asia collision age; convergence rates (GPS, ~40 mm/yr);
Tibet mean elevation, Moho depth; Altiplano mean elevation, Moho; Nazca
convergence rate; Everest height (2020 survey); Main Himalayan Thrust slip
rates; crust and mantle densities (Book 3 rows).

**Datasets.** `bachelor-2-etopo-tibet` (25--40 N, 75--100 E, 2-arc-min) and
`bachelor-2-etopo-andes` (10--30 S, 75--60 W, 2-arc-min), ERDDAP, PD.

**Weekend problem: "Two plateaus."** Part I mean elevations from the printed
profile figures; Part II Airy crustal thicknesses; compare with seismic Moho;
Part III shortening needed to thicken the Altiplano crust (area balance);
Part IV excess potential energy of Tibet and the extension it can drive.
**Named number: the crustal thickness of Tibet computed from its mean
elevation (km).**

---

## Ch. 15 Ancient Massifs and the Wilson Cycle --- `wilson-cycle`

**Hook.** On the cliffs of Siccar Point two sets of tilted beds meet at an
angle; between them lies the closing of a whole ocean, Iapetus, and the
making of a mountain belt now worn flat.

**Sections.**
1. Old orogens: the Caledonian, Appalachian and Variscan belts (per user
   ruling, together); their eroded roots (granulites, granites, metamorphic
   cores); how one recognises an orogen after 300 Myr of erosion (sutures,
   ophiolites, metamorphic belts, flysch/molasse, granites).
2. The Wilson cycle (definition and stages: rift, young ocean, mature ocean,
   subduction initiation, closing, collision, peneplain); reactivation of old
   sutures (Atlantic reopening near the Iapetus suture, ledger).
3. The Iapetus and Rheic oceans; Laurentia, Baltica, Avalonia, Gondwana;
   terranes; Caledonian closure; Variscan collision forming Pangaea.
4. Supercontinents: Pangaea re-founded, Rodinia, Columbia/Nuna, earlier
   candidates (ledger ages); supercontinent cycle (definition; periodicity
   debated, ledger review); zircon age peaks (descriptive, a sourced
   histogram if open data).
5. Erosion of mountains: denudation rates recalled (Book 3 ch. 19); time to
   erase a belt (proposition: exponential decay of relief with isostatic
   rebound: h(t) = h0 e^{-t/τ}, τ from rate and compensation factor).
6. `inthefield` reading an angular unconformity as an orogenic record (third
   person; Siccar Point, Hutton history box).

**Definitions.** Wilson cycle (owner per OUTLINE); supercontinent (re-founded,
Book 1 g7); supercontinent cycle; terrane; microcontinent (with terrane);
peneplain; tectonic reactivation (qualified "reactivation of a structure");
orogenic root (check Book 2 "mountain root": recall, do not define).

**Recall.** Pangaea (Book 1 g7); suture, ophiolite, nappe (Book 2/ch. 13);
unconformity, angular unconformity (Book 1/3); denudation rate (Book 3);
isostasy (Book 3); passive margin, rift (Book 3); granite (ch. 12).

**Figures.** [S] Wilson cycle in seven panels; [S] closing of Iapetus and Rheic
in three palaeogeographic sketches (labelled schematic, sources cited); [S]
present distribution of Caledonian--Appalachian--Variscan belts on a
North-Atlantic base reassembled (sketch from a sourced reconstruction; no
palaeomagnetic method); [F] `relief_decay` relief vs time with isostatic
rebound for two denudation constants; [F] `supercontinents` time chart of
supercontinent assembly/breakup ages (ledger); [P] Siccar Point (Commons,
verify); [AI] none.

**Ledger.** Ages of Caledonian, Acadian, Variscan phases; Iapetus opening/
closing ages; Pangaea assembly/breakup; Rodinia and Columbia ages; Siccar
Point beds ages; denudation constants; isostatic compensation factor (ρc/ρm
Book 3 rows).

**Datasets.** Optional zircon age database (Phase B; skip if no open table).

**Weekend problem: "Iapetus from birth to death."** Part I opening:
spreading rate and the width reached; Part II subduction initiation and
closure: convergence rate and time to close; Part III collision and
thickening: Airy root; Part IV erosion with isostatic rebound: time to bring
the relief below 500 m. **Named number: the maximum width the Iapetus-type
model ocean reached (km).**

---

## Ch. 16 Sedimentary Basins Compared --- `basins-compared`

**Hook.** In the North Sea a borehole can drill eight kilometres of sediment
before it hits basement; each kilometre is a page of the basin's subsidence
history, if one knows how to remove the weight of the sediment itself.

**Sections.**
1. Basin types: intracratonic, rift, passive-margin, foreland (recall ch. 13),
   strike-slip told (Year 3 extension-strike-slip); driving mechanisms
   (thermal, mechanical, flexural --- flexure Year 3, pointer).
2. Subsidence curves: from a well's stratigraphy to depth vs time; total
   subsidence; decompaction recalled (Book 3 ch. 23).
3. Backstripping: removing the sediment load (proposition: one-dimensional
   Airy backstripping formula, tectonic subsidence Y = S(ρm − ρs)/(ρm − ρw) +
   W_d − ΔSL ρm/(ρm − ρw)); method box for a multi-layer well.
4. The stretching model: uniform pure-shear stretching by β (McKenzie 1978);
   initial subsidence (proposition, isostatic balance of crust and
   lithosphere); thermal subsidence (proposition: exponential decay with time
   constant τ = a^2/(π^2 κ), first term only, admitted from the heat equation
   solution; Year 3 owns the Fourier series); fitting β to a curve.
5. Basins compared: intracratonic (Michigan, Paris-type --- name a non-French
   example: Michigan, Williston), rift (North Sea Viking Graben), passive
   margin, foreland (Molasse, Ganges); characteristic subsidence curves and
   time scales (table).
6. `inthelab` subsidence analysis software and data from wells (third person).

**Definitions.** intracratonic basin; rift basin; passive-margin basin;
subsidence curve; backstripping (owner per OUTLINE); stretching model (owner
per OUTLINE); stretching factor; syn-rift subsidence; post-rift (thermal)
subsidence; thermal time constant (of the lithosphere) --- inside the
post-rift proposition.

**Recall.** Sedimentary basin, subsidence, tectonic subsidence, accommodation,
decompaction, compaction (Book 3 ch. 23); isostasy, Airy (Book 3 ch. 11);
lithosphere, geotherm (Book 3 ch. 9--10); heat equation (physics b2); passive
margin, rift, graben (Book 3 ch. 12); foreland basin (ch. 13).

**Figures.** [F] `mckenzie` syn-rift and thermal subsidence vs time for β =
1.2, 1.5, 2, 4; [F] `backstrip` total vs tectonic subsidence of an invented
well with the best-fit McKenzie curve; [S] the four basin types in cross
section; [S] stretching model before/after diagram (crust, lithosphere,
asthenosphere upwelling); [S] backstripping column (sediment -> water/mantle
replacement); [P] a seismic section of a rift basin (open, e.g. USGS PD
seismic line, verify) or none; [AI] an offshore drilling platform at dusk
(generic).

**Ledger.** McKenzie 1978 parameters (a = 125 km, ρ, α, T1 = 1333 °C,
τ = 62.8 Myr; open restatement needed); North Sea well depths (open source);
Michigan basin thickness; densities (Book 3 rows); porosity--depth constants
(Book 3 rows from Sclater & Christie 1980 if present).

**Datasets.** None (invented well with sourced constants).

**Weekend problem: "Backstripping a well."** Part I decompact a four-unit
invented well; Part II backstrip to tectonic subsidence; Part III fit β from
the initial subsidence and check against thermal subsidence; Part IV predict
subsidence for the next 50 Myr. **Named number: the stretching factor β of
the basin.**

---

## Ch. 17 Oceanic Islands --- `oceanic-islands`

**Hook.** Darwin guessed in 1837 that a ring of coral in the open Pacific
marks the grave of a sunken volcano; in 1952 a drill on Enewetak went through
1.4 km of reef limestone and hit basalt.

**Sections.**
1. Growth of a volcanic island: shield stage, post-shield/alkaline cap,
   erosional stage, rejuvenated stage (Hawaiian sequence, ledger ages);
   volumes (ledger: Mauna Loa); link to hotspots (Book 3 ch. 15) and magmatic
   series (ch. 9).
2. Flank collapse: giant landslides (Nuuanu, ledger volumes), debris
   avalanches, tsunami potential (pointer ch. 28); rift zones.
3. Subsidence: plate cooling with age via the depth--age law (recall Book 3);
   loading subsidence (descriptive, flexure Year 3); the island sinks
   (proposition: subsidence rate from the depth--age law at the island's
   plate age, d(depth)/dt = k/(2 sqrt t)).
4. Reefs and atolls: fringing reef, barrier reef, atoll (Darwin's subsidence
   theory as a theorem-like proposition: reef keeps up if growth rate >
   subsidence + sea-level rise); guyots (drowned flat-topped seamounts); the
   Darwin point (latitude where reef growth fails, ledger); seamounts.
5. Erosion and sea level: wave-cut platforms, glacial sea-level changes (recall
   Book 3 eustasy; LGM −120 m ledger reuse).
6. `history` Darwin's coral reef theory and the Enewetak drilling.

**Definitions.** volcanic island (qualified "oceanic island"); shield stage
(and the volcano life stages in one definition); flank collapse; debris
avalanche; seamount; guyot; fringing reef; barrier reef; atoll; Darwin point;
wave-cut platform (check Book 1/2 owners: "wave-cut platform" may be g5/g8
coasts --- grep at writing).

**Recall.** Reef, carbonate platform, CCD, evaporite (Book 3 ch. 22);
hotspot, hotspot track, mantle plume (Book 3 ch. 15); depth--age law (Book 3
ch. 13); shield volcano (Book 1/2 --- check); landslide (Book 1 g5); eustasy
(Book 3 ch. 23); OIB (ch. 3).

**Figures.** [S] life stages of a Hawaiian-type island (five panels); [F]
`atoll` island top elevation vs age: subsidence + reef growth, drowning vs
keeping up (two reef growth rates), with the Darwin point line; [S] fringing
-> barrier -> atoll block diagrams; [F] `hawaii_ages` age vs distance along the
Hawaiian chain (sourced ages; Book 3 has `bachelor-1-hotspots.csv` --- reuse
read-only and report dependency, or ledger table); [P] an atoll from orbit
(NASA PD, verify); [P] Bora Bora (ISS photo, NASA PD, verify); [AI] a research
vessel over a seamount (generic).

**Ledger.** Enewetak drilling (1952: depth to basalt ~1.4 km, ages); Darwin
1842 book (PD); Mauna Loa volume; Nuuanu landslide volume; Hawaiian ages;
coral reef growth rates; Darwin point latitude (Grigg 1982); depth--age law
constants (Book 3 rows).

**Datasets.** None new (Book 3's hotspot table if used, read-only).

**Weekend problem: "From volcano to atoll."** An invented island born on
20-Myr-old lithosphere. Part I subsidence rate from the depth--age law; Part
II reef growth vs subsidence; Part III the island's summit drowns at age t:
compute; Part IV reef limestone thickness accumulated by the time the atoll is
40 Myr old; compare with Enewetak. **Named number: the thickness of reef
limestone above the volcanic basement (m).**

---

## Ch. 18 The Precambrian Earth --- `precambrian-earth`

**Hook.** Seven-eighths of the Earth's history lies before the first shelly
fossils; in that time the planet built its continents, oxygenated its air,
and froze over at least twice.

**Sections.**
1. The Hadean: the oldest minerals (Jack Hills zircons 4.4 Ga, ledger), the
   oldest rocks (Acasta gneiss, ledger), the magma ocean and the late heavy
   bombardment (descriptive, debated, calibrated wording).
2. The Archean: greenstone belts (definition; komatiites and their eruption
   temperatures: proposition MgO--liquidus relation, ledger empirical
   coefficient); TTG crust; cratons re-founded (Kaapvaal, Pilbara, Superior);
   a hotter mantle (proposition: radiogenic heat production back in time from
   the four isotopes, exponential decay chains: H(t) = Σ H_i e^{λ_i t}).
3. Life and the atmosphere: stromatolites (recall Book 2), the Great
   Oxidation Event re-founded (ledger ~2.4 Ga; sulfur MIF told, Year 3 owns
   the record), BIFs re-founded with redox chemistry recalled, red beds,
   detrital pyrite and uraninite; Neoproterozoic oxygenation.
4. The Proterozoic: supercontinents (link ch. 15), orogens, first eukaryotes
   (biology owns: recall); the "boring billion" (descriptive).
5. Snowball Earth: Sturtian and Marinoan glaciations (ledger ages), low-
   latitude glacial deposits (palaeolatitude from the Year 3 volume: pointer),
   cap carbonates, the escape by CO2 accumulation (proposition: time to build
   up the CO2 needed at a given volcanic outgassing rate); the ice--albedo
   feedback is told in prose (Year 3 owner, contested --- see report).
6. The faint young Sun problem re-founded (proposition: Gough's luminosity law,
   ledger; effective temperature of an early Earth with today's albedo).
7. `inthefield` reading a greenstone belt (third person).

**Definitions.** Hadean; Archean; Proterozoic (eon definitions with ICS
boundaries, ledger `ics:*`); greenstone belt (owner per OUTLINE); komatiite;
tonalite--trondhjemite--granodiorite (TTG); craton (re-founded, Book 2
g12.01); Great Oxidation Event (re-founded, Book 2 g12.08); banded iron
formation (re-founded, Book 2 g12.08); snowball Earth (owner per OUTLINE); cap
carbonate; faint young Sun problem (re-founded, Book 2 g12.08, same term).

**Recall.** Stromatolite, red beds, primitive atmosphere (Book 2 g12.08);
zircon, U--Pb, closure (Book 3); radioactive decay (physics); redox (chemistry);
first eukaryotes, photosynthesis, cyanobacteria (biology); supercontinent,
Wilson cycle (ch. 15); geological time scale, eon (Book 2 / Book 3 ICS).

**Figures.** [S] Precambrian timeline (eons and eras, ICS colours, ledger
ages, events); [F] `heat_production` mantle heat production vs time from U,
Th, K (exponential sum) with the contributions; [F] `faint_sun` solar
luminosity and early-Earth effective temperature vs time; [S] greenstone belt
map pattern (domes of TTG and keels of greenstones, schematic); [F]
`oxygen` atmospheric O2 history (sourced bounds as a band, Lyons et al. 2014
style; ledger points only, clearly approximate); [P] stromatolites at Shark
Bay (Commons, verify); [P] banded iron formation (Commons, verify); [AI] none.

**Ledger.** Jack Hills zircon age; Acasta gneiss; GOE timing; Sturtian/
Marinoan ages; heat production constants of U, Th, K (shared? grep;
Turcotte & Schubert values via an open source); Gough 1981 law; komatiite MgO
and temperatures; ICS eon boundaries (shared `ics:*`).

**Datasets.** None.

**Weekend problem: "A hotter young Earth."** Part I heat production 3 Ga ago
from present U, Th, K concentrations; Part II komatiite MgO -> liquidus
temperature -> mantle potential temperature (with the ch. 7 adiabat); Part III
faint Sun: effective temperature without extra greenhouse; Part IV CO2
build-up to escape a snowball at a given outgassing. **Named number: how much
hotter the Archean mantle was than today's, from the komatiite (°C).**

---

## Ch. 19 The Phanerozoic Earth --- `phanerozoic-earth`

**Hook.** Five times in the last 540 million years most species on Earth
vanished within a geological instant; at least three of those times the cause
came from inside the Earth.

**Sections.**
1. Palaeogeography: method in outline (palaeomagnetism Year 3, pointer;
   fossils, facies, orogens); maps at 500, 300, 200, 100, 50 Ma (schematic,
   from a sourced open reconstruction; no APW).
2. Sea level through the Phanerozoic: first-order curve (ledger: Haq &
   Al-Qahtani 2005 or Miller et al. 2005 for the Cenozoic/Cretaceous);
   epeiric seas; transgression and regression; causes: ridge volume
   (proposition: sea-level change from ridge volume change with the depth--
   age law and a change in spreading rate), ice volume, dynamic topography
   (told).
3. Orogenies through time (summary table, link ch. 13--15).
4. Mass extinctions: the big five (ledger ages and magnitudes); Earth causes:
   LIPs (Siberian Traps, CAMP, Deccan; ledger ages, volumes; link Book 3 LIPs),
   ocean anoxia (oceanic anoxic events), the Chicxulub impact (ledger);
   biology owns extinction itself: recall.
5. Hypsometry and flooding (proposition: flooded continental area from the
   hypsometric curve, ETOPO-derived).
6. `dated` box: GTS2020/ICS chart version cited.

**Definitions.** palaeogeography; palaeogeographic map; epeiric sea;
transgression; regression (qualified "marine regression"); first-order
sea-level cycle (check Year 3 "systems tract" ownership: only first-order
eustatic curve here); oceanic anoxic event; hypsometric curve (check Book 1/3
owners: hypsometry may be Book 3 ch. 9 or g11 --- grep at writing).

**Recall.** Mass extinction (biology); LIP (Book 3 ch. 15); eustasy, relative
sea level (Book 3 ch. 23); stratotype, GSSP, biozone (Book 3 ch. 24);
depth--age law (Book 3); Wilson cycle, supercontinent (ch. 15).

**Figures.** [S] five palaeogeographic snapshots (simple redrawn continents
from a sourced open reconstruction set, e.g. GPlates/EarthByte CC-BY
reconstructions --- check licence and whether figdata can read a GPlates
export; else schematic); [F] `sealevel` Phanerozoic/Cenozoic sea-level curve
from a sourced dataset; [F] `ridge_volume` sea-level change vs spreading-rate
change; [F] `hypsometry` hypsometric curve from shared ETOPO 1° and flooded
area vs sea level; [S] timeline of extinctions, LIPs and impacts (ledger);
[P] Deccan Traps (Commons, verify) or K--Pg boundary clay (USGS PD, verify);
[AI] none.

**Ledger.** Big five ages and genus/species losses (Raup & Sepkoski 1982 or
newer open); LIP ages and volumes; Chicxulub crater diameter and age;
sea-level curve dataset; ICS boundaries (shared).

**Datasets.** `bachelor-2-miller2005` (NOAA NCEI paleo
`contributions_by_author/miller2005/`, PD) for the Cenozoic--Cretaceous sea
level; shared `etopo-1deg` for hypsometry.

**Weekend problem: "When the ridges were fast."** Part I cross-section area of
a ridge from the depth--age law; Part II total ridge volume for a given
spreading rate and ridge length; Part III sea-level change when spreading rate
doubles (with ocean area); Part IV flooded continental area from the
hypsometric curve. **Named number: the sea-level rise caused by doubling the
spreading rate (m).**

---

## Ch. 20 Fossils and Palaeoenvironments --- `palaeoenvironments`

**Hook.** A trilobite, a ripple mark and a burrow: three clues that let a
geologist put a sea where there is now a wheat field.

**Sections.**
1. Taphonomy: from death to fossil; preservation potential; body fossils and
   trace fossils re-founded (ichnology); Lagerstätten (Burgess Shale,
   Solnhofen, ledger ages); biases.
2. Fossils as time markers: index fossils and biozones recalled (Book 3);
   ammonites, graptolites, forams, conodonts (descriptive with ages).
3. Fossils as environment markers: actualism; life vs death assemblages;
   autochthonous vs allochthonous; ichnofacies (Seilacher bathymetric
   sequence); salinity, oxygen, depth indicators (corals, stenohaline
   organisms); diversity gradients.
4. Facies and fossils together: Walther's law (SYNC 3 RULING: owned by the
   Year 3 volume, ch. 17 `facies-models`, as a theorem --- prose use with a
   pointer to the Year 3 volume only, no definition, no \index);
   reconstructing a palaeoenvironment from a log.
5. Reconstruction from map and section: the Varden Hills Jurassic sea
   (region.py units: sandstone, limestone, shale, chalk), facies interpretation,
   sedimentation rates (proposition: rate = thickness/duration with
   decompaction correction).
6. `inthefield` logging a section bed by bed (third person).

**Definitions.** taphonomy; preservation potential; body fossil; trace fossil
(re-founded, Book 1 g7); ichnofacies; Lagerstätte; life assemblage; death
assemblage (one definition); autochthonous; allochthonous (fossils);
actualism (principle; check Book 1/2 "uniformitarianism" owner --- recall if
owned); palaeoenvironment; stenohaline organism (or prose).

**Recall.** Fossil, mould, cast (Book 1 g7; biology); index fossil, biozone,
FAD (Book 3 ch. 24); sedimentary facies, depositional environment, turbidite,
reef (Book 3 ch. 21--22); decompaction (Book 3 ch. 23); Varden Hills geology
(Book 3 ch. 4).

**Figures.** [S] taphonomic pathway (death -> decay -> burial -> diagenesis ->
exhumation) with losses; [S] Seilacher ichnofacies along a shelf-to-basin
profile; [F] `varden_palaeo` Varden Hills Jurassic facies cross-section from
region.py with interpreted depths; [S] a stratigraphic log with fossils and
interpretation column; [P] Burgess Shale fossil (Commons, verify CC) or
Archaeopteryx Solnhofen (Commons, verify); [P] trace fossils (Commons,
verify); [AI] a geologist logging a cliff section (generic, observation only).

**Ledger.** Burgess Shale age; Solnhofen age; ichnofacies depth ranges
(sourced); ammonite zone durations (ledger: mean Jurassic ammonite zone
duration ~0.5--1 Myr, source); Varden constants (region.py, not ledger).

**Datasets.** region.py only.

**Weekend problem: "The Jurassic sea of the Varden Hills."** Part I read the
Varden map and section, units and thicknesses; Part II fossil content (given
as a list per unit): environments; Part III biozones give durations:
sedimentation rates with decompaction; Part IV relative sea-level history.
**Named number: the decompacted sedimentation rate of the Varden limestone
(m per million years).**

---

## Ch. 21 Atmospheric Thermodynamics --- `atmospheric-thermodynamics`

**Hook.** On a summer afternoon a cumulus grows into a thunderstorm twelve
kilometres tall in under an hour. The energy was in the morning sounding, if
one could read it.

**Sections.**
1. Moist air: vapour pressure, mixing ratio, specific humidity, virtual
   temperature (definitions; relations as propositions); relative humidity and
   dew point recalled (physics).
2. Saturation vapour pressure: Clausius--Clapeyron applied (proposition:
   integrated form with constant L; comparison with Bolton 1980 empirical
   formula, figdata test); 7%/K rule (corollary).
3. Adiabatic ascent: dry adiabatic lapse rate and potential temperature
   recalled (Book 3 ch. 26); lifting condensation level (proposition: z_LCL ≈
   125 m/K × (T − T_d)); saturated adiabatic lapse rate (proposition, derived
   from the first law with condensation); equivalent potential temperature
   (definition, approximate conserved quantity).
4. Thermodynamic diagrams: skew-T log-p and tephigram (definitions, lines on
   them); plotting a sounding (method box).
5. Stability: conditional instability; parcel method; level of free
   convection, equilibrium level; CAPE and CIN (definitions; proposition:
   maximum updraft w = sqrt(2 CAPE)); static stability recalled (Book 3).
6. Cloud microphysics: nucleation recalled (physics); supersaturation;
   Köhler curve (proposition admitted combining Kelvin and Raoult, both
   recalled from chemistry/physics); cloud condensation nuclei; droplet growth
   by diffusion vs collision--coalescence; ice processes (Bergeron, recall
   Book 2 g10 rain processes).
7. `inthefield` radiosonde launches (third person).

**Definitions.** vapour pressure (of water in air); mixing ratio; specific
humidity; virtual temperature; lifting condensation level (re-founds Book 2
"condensation level"; both indexed); saturated adiabatic lapse rate (moist
adiabat: owner per OUTLINE; re-founds g10 if g10 defined "moist adiabatic
rate" --- grep); equivalent potential temperature; thermodynamic diagram;
skew-T log-p diagram; tephigram (in same definition); sounding (atmospheric);
conditional instability; level of free convection; equilibrium level;
convective available potential energy (CAPE, owner per OUTLINE); convective
inhibition (CIN); supersaturation; Köhler curve (in its proposition); cloud
condensation nucleus (re-founds Book 2 "condensation nucleus").

**Recall.** Relative humidity, dew point, saturation vapour pressure,
Clausius--Clapeyron, latent heat, nucleation (physics b1 phase changes);
first law, adiabatic, heat capacities (physics b1); dry adiabatic lapse rate,
potential temperature, air parcel, static stability, inversion, standard
atmosphere (Book 3 ch. 26); Raoult's law (chemistry b2), Kelvin equation
(chemistry b3 colloids --- check owner); rain processes (Book 2 g10.04).

**Figures.** [F] `thermo` e_s(T) from integrated Clausius--Clapeyron vs Bolton
formula, with the 7%/K slope; [F] `thermo` skew-T diagram with dry adiabats,
moist adiabats, mixing-ratio lines, and a sourced sounding (IGRA or Wyoming
archive, check terms; else an idealised sounding labelled as such) with CAPE
shaded; [F] `kohler` Köhler curves for three CCN sizes; [S] parcel ascent
cartoon with LCL, LFC, EL; [S] cloud microphysics processes; [P] cumulonimbus
(NOAA PD, verify); [AI] a radiosonde balloon launch at dawn (generic).

**Ledger.** Physical constants (const:* shared: R_d, R_v, c_p, L_v --- grep;
mint if absent from a primary source such as WMO/NIST); Bolton 1980
coefficients; sounding data source; typical CAPE values for severe storms
(source); CCN concentrations maritime/continental.

**Datasets.** `bachelor-2-sounding` (IGRA v2 one station-day, NOAA NCEI PD;
or skip and use an idealised sounding).

**Weekend problem: "Reading the morning sounding."** An invented (or sourced)
sounding table. Part I mixing ratios, LCL; Part II lift along the moist
adiabat (numerical integration in a table given), LFC, EL; Part III CAPE by
the trapezium rule, CIN; Part IV maximum updraft and hail plausibility. **Named
number: the maximum updraft speed predicted by parcel theory (m/s).**

---

## Ch. 22 Weather Systems --- `weather-systems`

**Hook.** A forecast for tomorrow is right nine times in ten, one for ten days
ahead barely beats a coin. The atmosphere's chaos, not our computers, sets the
limit.

**Sections.**
1. Air masses and fronts re-founded at university level: frontal surfaces and
   slopes (proposition: Margules' frontal slope admitted, or descriptive),
   cold, warm, occluded, stationary fronts recalled (Book 1 g8).
2. Mid-latitude cyclones: polar-front (Norwegian) model, life cycle; Shapiro--
   Keyser told; conveyor belts (descriptive); cyclogenesis; energy source
   (baroclinic, descriptive: no thermal wind, Year 3).
3. Jet streams and Rossby waves (descriptive, as the outline asks): long
   waves, troughs and ridges (qualified: "upper-level trough"), phase speed
   formula admitted with pointer (c = U − β/k^2), blocking.
4. Tropical cyclones re-founded: genesis conditions (SST ≥ 26.5 °C, ledger),
   structure recalled (Book 2 g10), maximum potential intensity as a Carnot
   engine (proposition admitted from Emanuel 1986 with the heat-engine
   efficiency recalled from physics).
5. Numerical weather prediction: primitive equations told (no equations
   beyond naming), grids, data assimilation, ensembles, predictability; the
   Lorenz 1963 system as a toy (proposition: sensitivity to initial
   conditions, error doubling time from the largest Lyapunov exponent;
   numerically demonstrated).
6. `inthelab` a forecast centre's daily cycle (third person).

**Definitions.** frontal surface; occluded front; stationary front (if not at
school: grep); extratropical cyclone; polar-front model; cyclogenesis; jet
streak (or prose); Rossby wave (owner by rule 4, see report); upper-level
trough; upper-level ridge (one definition); atmospheric blocking; potential
intensity (of a tropical cyclone); numerical weather prediction; data
assimilation; ensemble forecast; predictability limit.

**Recall.** Air mass, front, cold front, warm front, depression, anticyclone
(Book 1 g8); tropical cyclone, eye, eyewall (Book 2 g10.05); geostrophic wind,
Coriolis parameter, jet streams, westerlies, Hadley cell (Book 3 ch. 28);
Carnot efficiency (physics b2 heat engines); CAPE, moist adiabat (ch. 21).

**Figures.** [S] Norwegian cyclone life cycle (four panels with fronts using
the style's front line styles); [S] cross-section through a warm and cold
front with cloud types; [S] Rossby wave pattern on a polar stereographic
sketch (schematic); [F] `lorenz63` two trajectories diverging (x vs t) and the
butterfly attractor projection; [F] `lorenz63` log error vs time with fitted
growth rate; [P] satellite image of a North Atlantic extratropical cyclone
(NASA/NOAA PD, verify); [P] a hurricane from the ISS (NASA PD, verify);
[AI] a forecast office with large weather maps (generic).

**Ledger.** Tropical cyclone SST threshold; Lorenz 1963 parameters (σ=10,
r=28, b=8/3) and largest Lyapunov exponent (~0.906, source); forecast skill vs
lead time (ECMWF open statement or WMO); Rossby wave typical wavelengths/
speeds; potential intensity values (Emanuel source).

**Datasets.** None.

**Weekend problem: "How far ahead?"** Part I front speed and arrival time from
an invented chart; Part II Rossby wave phase speed for given U and wavelength;
stationary wavelength; Part III Lorenz error growth: doubling time from the
figure; Part IV predictability horizon for initial error 0.1 °C growing to
3 °C with the doubling time. **Named number: the predictability horizon (days).**

---

## Ch. 23 Climate Variability --- `climate-variability`

**Hook.** In 1997--98 the eastern Pacific warmed by two degrees; Peru's
fisheries collapsed, Indonesia burned, and California flooded. One ocean, one
year, half a planet affected.

**Sections.**
1. Variability vs change: internal variability, modes, time scales; anomalies
   and indices (method box: climatology, anomaly, running mean).
2. Monsoons: land--sea heating contrast; seasonal migration of the ITCZ
   (recall Book 3); the Indian and West African monsoons (ledger rainfall);
   monsoon onset; variability.
3. ENSO: normal Walker circulation recalled (Book 3); El Niño and La Niña;
   thermocline tilt; Bjerknes feedback (definition and loop); recharge
   oscillator told; indices (Niño-3.4, ONI, SOI); ONI record 1950--present
   (figdata from CPC); event statistics.
4. NAO and other modes: the NAO index (CPC data), its winter impacts; PDO, IOD,
   SAM named (descriptive); teleconnections.
5. Coupled ocean--atmosphere: why the ocean gives memory (proposition: mixed
   layer heat capacity and damping time τ = ρ c_p h/λ; red-noise response
   admitted as a first-order ODE with random forcing, simulated in figdata).
6. `dated` box: current ENSO status statement (year noted).

**Definitions.** mode of climate variability; climate index; climatology
(statistical reference period, check Book 2/3 owner of "climate normal" ---
grep); monsoon (owner per OUTLINE); monsoon onset (prose); El Niño--Southern
Oscillation (ENSO, owner per OUTLINE); El Niño; La Niña; Southern
Oscillation; Bjerknes feedback; Niño-3.4 index; Oceanic Niño Index (one
definition with Niño-3.4); North Atlantic Oscillation; teleconnection.

**Recall.** Walker circulation, ITCZ, trade winds, Hadley cell, upwelling,
thermocline, mixed layer (Book 3 ch. 27--29); climate, weather (Book 1/2);
climate feedback (Book 2 g12.10).

**Figures.** [F] `oni` ONI 1950--present bar chart (red/blue) with event
thresholds; [F] `nao` winter NAO index with 5-year mean; [S] Walker circulation
normal vs El Niño vs La Niña sections (three panels); [S] monsoon circulation
summer/winter map sketch on shared geo base; [F] `red_noise` a red-noise time
series vs white noise, showing memory; [P] none (satellite SST anomaly maps
NOAA PD if one is open, verify); [AI] fishing boats on an upwelling coast
(generic).

**Ledger.** ONI thresholds and definition (CPC); NAO definition (CPC); 1997--98
and 2015--16 peak ONI values (from dataset); monsoon rainfall (IMD or source);
mixed layer depths; feedback parameter (ipcc rows reuse).

**Datasets.** `bachelor-2-oni` (CPC `oni.ascii.txt`, PD);
`bachelor-2-nao` (CPC monthly NAO, PD); `bachelor-2-soi` (CPC SOI, PD;
optional).

**Weekend problem: "Counting El Niños."** The ONI table (excerpt printed).
Part I compute 3-month running means from monthly Niño-3.4 values; Part II
identify events with the 5-season rule; Part III strong events (≥ 1.5);
intervals between them; Part IV mixed-layer damping time and why ENSO needs
the ocean. **Named number: the mean interval between strong El Niño events
since 1950 (years).**

---

## Ch. 24 Climate Archives and Proxies --- `climate-proxies`

**Hook.** A foraminifer the size of a sand grain carries in its shell the
temperature of the sea it lived in and the volume of ice on land 100 000 years
ago.

**Sections.**
1. Archives and proxies re-founded: marine sediments, ice cores, speleothems,
   tree rings, lake sediments (varves), corals; resolution, span, dating
   method (table).
2. Oxygen isotopes in carbonates: δ18O recalled (chemistry), the
   palaeotemperature equation (proposition, sourced calibration: e.g. Kim &
   O'Neil 1997 / Shackleton 1974 form; Year 3 owns "palaeothermometry" as a
   topic: we apply one equation without the term) --- check contested; the ice
   volume effect (proposition: δ18O of seawater from mass balance of ice
   volume with ice δ18O, ~1 permil for 120 m sea level); benthic stack LR04
   (shared data).
3. Ice cores: δD and δ18O of ice as temperature proxies (spatial slope,
   ledger); trapped air CO2 and CH4 (shared EDC data); annual layers.
4. Other proxies: Mg/Ca (proposition: exponential calibration Anand et al.
   2003); alkenones (told); pollen recalled (biology/Book 2); tree rings
   (dendroclimatology, cross-dating); speleothems (U--Th dating told, δ18O);
   varves.
5. Building an age model: annual layer counting, radiometric tie points,
   interpolation (method box); uncertainty growth (proposition: counting error
   accumulates as sqrt(n) for random errors).
6. Calibration and transfer functions: regression of proxy on instrumental
   data (least squares recalled), validation, limits.
7. `inthelab` ice-core processing in a cold lab (third person).

**Definitions.** climate proxy (re-founds Book 2 "proxy"); climate archive
(re-founded, Book 2 g12.09); proxy calibration ("transfer function" is physics b1's term: prose only, never
defined); ice-volume effect; benthic foraminiferal δ18O stack (prose; "LR04" named);
Mg/Ca palaeothermometer (qualified; contested with Year 3 "palaeothermometry"
--- propose the qualified form "Mg/Ca ratio (proxy)"); dendroclimatology;
cross-dating; speleothem; varve; age model; annual layer counting.

**Recall.** δ value, fractionation factor (chemistry b3); meteoric water
line, VSMOW, VPDB (ch. 4); ice core, glacial period, interglacial, LGM, pollen
analysis (Book 2 g12.09); radiocarbon, U-series told, calibration curve
(radiocarbon) (Book 3 ch. 25); foraminifera, coccolithophores (biology /
Book 3 oozes); least squares (math).

**Figures.** [F] `paleotemp` palaeotemperature equation curve with ±1σ; [F]
`lr04` LR04 stack over 5 Myr and zoom 800 kyr (shared data); [F] `epica` EDC
δD-derived temperature and CO2 over 800 kyr (shared data); [F] `mgca`
Mg/Ca--temperature calibration; [S] proxy archives time-span vs resolution
chart (log axes; ledger spans); [S] ice-volume effect cartoon; [P] ice core
section showing layers (NOAA/NSF PD, verify); [P] speleothem cross-section or
tree-ring cross-section (Commons, verify); [AI] a cold lab with ice cores
(generic).

**Ledger.** Calibration equations (sources); LR04 (shared data:lr04); EDC
(shared); ice δ18O of LGM ice sheets (source); sea level LGM (Book 2/3 rows);
Anand 2003 Mg/Ca; ice δD--temperature slope (Jouzel); archive spans.

**Datasets.** shared only (lr04, edc-temperature, co2-icecore); optional
speleothem record (Cheng et al. 2016, NOAA NCEI PD) as
`bachelor-2-speleothem`.

**Weekend problem: "One shell, two signals."** Part I ice-volume effect at
the LGM from sea level and ice δ18O; Part II benthic δ18O shift LGM--Holocene
from LR04 values given; Part III remove ice volume, convert the residual with
the palaeotemperature equation; Part IV cross-check with Mg/Ca. **Named
number: the deep-ocean cooling at the Last Glacial Maximum (°C).**

---

## Ch. 25 Orbital Forcing and the Ice Ages --- `orbital-forcing`

**Hook.** Ice ages are paced by the shape of the Earth's orbit and the tilt
of its axis --- changes that alter the planet's yearly sunlight by less than
one per cent but summer sunshine at 65°N by more than ten.

**Sections.**
1. Orbital elements recalled: eccentricity (physics), obliquity of the
   ecliptic (Book 3), longitude of perihelion; climatic precession (definition:
   e sin ϖ); periods 100/400 kyr, 41 kyr, 19/23 kyr (ledger, Berger 1978).
2. Insolation from orbital elements: distance--true-anomaly relation (Kepler
   recalled); daily-mean insolation recalled from Book 3 (proposition stated
   with the orbital factor (1 + e cos(λ − ϖ))^2/(1 − e^2)^2); annual global
   mean depends only on e (proposition: (1 − e^2)^{-1/2} factor, derived);
   seasonal contrast from precession; latitudinal pattern from obliquity
   (proposition: annual mean insolation at the pole increases with
   obliquity).
3. Computing the insolation curve: figdata from Berger & Loutre 1991 orbital
   elements (orbit91), tested against their 65°N July column; caloric
   half-years told.
4. Milankovitch theory: summer insolation at high northern latitudes controls
   ice-sheet growth; evidence from LR04 (shared data) and EDC; ice-sheet
   response time (proposition: first-order lag model dV/dt = (V_eq(I) − V)/τ,
   solved and plotted); feedbacks: CO2, ice--albedo (prose, Year 3 owns the
   term), dust; terminations; the 100-kyr problem and the mid-Pleistocene
   transition (calibrated, descriptive).
5. CO2 in glacial cycles: 180--280 ppm range (shared data); its radiative
   forcing (5.35 ln(C/C0) recalled from Book 2 g12, ipcc rows) vs orbital
   forcing locally.
6. `history` Milankovitch's hand computations; Hays, Imbrie & Shackleton
   1976.

**Definitions.** longitude of perihelion; climatic precession (precession
index); Milankovitch parameters (owner per OUTLINE; eccentricity, obliquity,
precession as the three --- eccentricity itself recalled from physics,
obliquity from Book 3); Milankovitch theory; glacial termination; glacial
period, interglacial (re-founded, Book 2 g12.09); mid-Pleistocene transition;
ice-sheet response time (inside the proposition).

**Recall.** Eccentricity, Kepler's laws, ellipse (physics b1); obliquity of
the ecliptic, insolation, daily-mean insolation, tropical year (Book 3 ch. 1,
27); spherical trigonometry (Book 3 ch. 1); LGM, glacial cycle (Book 2
g12.09); radiative forcing (Book 2 g12.10); proxies, LR04 (ch. 24).

**Figures.** [F] `insolation` e, obliquity, precession index over the last
1 Myr (orbit91); [F] `insolation` July 65°N insolation computed vs tabulated
(overlay + residual); [F] `insolation` insolation latitude--month contour map
today and difference 10 kyr ago (computed); [F] `ice_lag` insolation forcing
and lagged ice-volume response compared with LR04; [S] orbital geometry:
ellipse, perihelion, equinoxes, ϖ; [S] the three parameters in three panels;
[AI] none; [P] none.

**Ledger.** Berger & Loutre 1991 (NOAA NCEI, PD); Berger 1978 periods;
present e, ε, ϖ (shared earth:ecc, earth:obliquity; mint
`berger91:varpi-0` if absent); TSI (shared earth:TSI); Hays et al. 1976
(history); MPT timing (source); glacial CO2 (shared data:co2-bereiter).

**Datasets.** `bachelor-2-orbit91` (NOAA NCEI orbit91, 0 to −5000 kyr, 1 kyr
step; columns age, ECC, OMEGA, OBL, PREC, 65NJul, 65SJan, 15NJul, 15SJan;
PD).

**Weekend problem: "Sunlight at 65°N."** Part I orbital elements 115 kyr ago
from the printed table; Part II Earth--Sun distance at the summer solstice;
Part III daily-mean insolation at 65°N at the solstice, then and now; Part IV
the ice-sheet lag model's response. **Named number: the summer-solstice
insolation at 65°N 115 000 years ago (W/m^2).**

---

## Ch. 26 Climate over Geological Time --- `deep-time-climate`

**Hook.** Ninety million years ago crocodile relatives lived in the Arctic and
there was no permanent ice anywhere; the cause was carbon dioxide, and the cure
was rain falling on rock.

**Sections.**
1. The long-term carbon cycle: reservoirs and fluxes on Myr time scales
   (volcanic outgassing, silicate weathering, organic burial, carbonate
   deposition; ledger); biology owns "carbon cycle": qualified "long-term
   carbon cycle"; residence time of carbon in the ocean--atmosphere
   (proposition).
2. The carbonate--silicate cycle (Urey reaction with `\ce`; hydrolysis
   recalled Book 3); the silicate-weathering thermostat (definition;
   proposition: linearised box model dC/dt = V − W(T(C)), stable equilibrium,
   e-folding time; figdata integrates the non-linear form).
3. Greenhouse and icehouse worlds: Palaeozoic glaciations (Late Ordovician,
   Late Palaeozoic Ice Age), the Cretaceous greenhouse (CO2 estimates ledger,
   temperatures), Cenozoic cooling (CENOGRID or LR04 + Zachos, ledger;
   Antarctic glaciation 34 Ma; Northern Hemisphere glaciation 2.7 Ma).
4. Hyperthermals and the PETM: magnitude (5--8 °C, ledger), carbon release
   (range, ledger), duration of onset and recovery (ledger); recovery by
   weathering (link to the thermostat time constant); carbon isotope signature
   in prose (Year 3 owns "carbon isotope excursion" as a term).
5. Tectonics and climate: uplift--weathering hypothesis (Himalaya, told,
   debated), gateways (Drake Passage), position of continents (descriptive).
6. `dated` box: latest compilation of Cenozoic CO2 (CenCO2PIP 2023, year
   cited).

**Definitions.** long-term carbon cycle (qualified; biology owns "carbon
cycle"); volcanic outgassing (CO2); carbonate--silicate cycle;
silicate-weathering thermostat (owner per OUTLINE); greenhouse climate state;
icehouse climate state (one definition); hyperthermal event; Palaeocene--Eocene
Thermal Maximum (PETM); ocean gateway (prose or definition).

**Recall.** Chemical weathering, hydrolysis (of silicates), clay mineral
(Book 3 ch. 19); carbon cycle, reservoir, residence time? (biology b2 --- grep
"residence time" owner); greenhouse effect (physics b2); ocean acidification
(chemistry); CCD, lysocline (Book 3); radiative forcing, ECS (Book 2 g12.10);
proxies (ch. 24); faint young Sun (ch. 18); snowball Earth (ch. 18).

**Figures.** [F] `carbonate_silicate` CO2 and T response to a pulse and to a
step in outgassing (box model); [F] `cenozoic` Cenozoic benthic δ18O
(CENOGRID or Zachos 2008 from NCEI) with events marked; [F] `co2_proxies`
Phanerozoic CO2 estimates (Foster et al. 2017 CC-BY, sourced) on log axis;
[S] long-term carbon cycle box diagram with fluxes (ledger); [S] PETM schematic
timeline (onset, body, recovery durations from ledger); [P] PETM outcrop
(Commons, verify) or none; [AI] a tropical rainforest weathering landscape
with a river carrying sediment (generic).

**Ledger.** Volcanic CO2 outgassing (Gt C/yr range, source); silicate
weathering flux; organic burial; ocean--atmosphere C inventory; PETM warming,
carbon release, durations (open reviews); Cretaceous CO2 and temperatures;
Antarctic glaciation 34 Ma; NHG 2.7 Ma; Foster 2017; CENOGRID; temperature
sensitivity of weathering (activation energy, Berner GEOCARB parameters
--- open source).

**Datasets.** `bachelor-2-cenogrid` (Westerhold et al. 2020, PANGAEA child
dataset, CC-BY 4.0) or `bachelor-2-zachos2008` (NOAA NCEI, PD);
`bachelor-2-foster2017` (CC-BY 4.0, if the supplementary table is fetched
directly).

**Weekend problem: "How long does the thermostat take?"** Part I steady
state: outgassing = weathering; Part II linearise W(T(C)) using the ECS (log
CO2) and a weathering sensitivity; Part III e-folding time; Part IV apply to a
PETM-sized carbon release: time to remove 90% of the excess. **Named number:
the e-folding time of the silicate-weathering thermostat (thousand years).**

---

## Ch. 27 Anthropogenic Climate Change --- `anthropogenic-climate-change`

**Hook.** Human influence has warmed the climate at a rate unprecedented in at
least the last 2000 years (AR6 WG1 SPM A.2.3). This chapter quantifies how
much forcing, how much response, and what remains uncertain.

**Sections.** (Every statement with an AR6 WG1 ledger row: report, chapter,
section; calibrated language in italics as AR6 uses it.)
1. Forcing quantified: effective radiative forcing (definition) by agent
   1750--2019 (AR6 Annex III data, figdata), total 2.72 [1.96--3.48] W/m^2;
   CO2 log forcing re-derived (recall Book 2: 5.35 ln(C/C0) vs AR6
   formula); aerosols and their uncertainty.
2. The global energy budget: ΔN = ΔF + λΔT (proposition; λ the climate
   feedback parameter); Earth's energy imbalance (ledger); ocean heat uptake.
3. Feedbacks: water vapour + lapse rate, cloud, surface albedo, Planck (AR6
   Table 7.10 values, ledger); total feedback parameter; ECS re-founded:
   ECS = −F_2x/λ (proposition), AR6 best estimate 3 °C, likely 2.5--4 °C;
   transient climate response (definition).
4. Detection and attribution: definitions (re-founded); fingerprints
   (stratospheric cooling + tropospheric warming, ledger); attributed warming
   (ipcc rows); optimal fingerprinting told (regression, least squares
   recalled).
5. Scenarios: SSP1-1.9 ... SSP5-8.5 (definition re-founded); projected warming
   (ipcc:proj-temp); TCRE (definition; proposition: ΔT ≈ TCRE × cumulative
   CO2); the remaining carbon budget (definition; computed from TCRE with the
   AR6 values; ledger SPM D.1.2).
6. Sea level: components of the budget 1971--2018 / 1993--2018 (thermal
   expansion, glaciers, Greenland, Antarctica, land water; AR6 Table 9.5,
   ledger); thermal expansion computed (proposition: Δh = α ΔT H for a layer);
   committed rise (calibrated).
7. `dated` boxes: latest annual CO2 (shared data), latest GISTEMP year.

**Definitions.** effective radiative forcing; Earth's energy imbalance;
climate feedback parameter; Planck response (or "Planck feedback");
water-vapour feedback; lapse-rate feedback; cloud feedback; surface-albedo
feedback (qualified; ice--albedo is Year 3's term --- see report);
equilibrium climate sensitivity (re-founded, Book 2 g12.10); transient climate
response; transient climate response to cumulative CO2 emissions (TCRE);
remaining carbon budget (qualified; biology owns "carbon budget"); detection
(of climate change); attribution (re-founded, Book 2 g12.10); fingerprint
(climate); Shared Socioeconomic Pathway (new; Book 2 g12.10 owns "emission scenario",
physical-science use only); sea-level budget; thermosteric sea-level rise.

**Recall.** Greenhouse effect, black body (physics b2); radiative forcing,
climate feedback, ECS, scenario/projection, attribution (Book 2 g12.10 ---
those re-founded here are marked); carbon cycle, airborne fraction (biology
b2); ocean acidification (chemistry); thermal expansion (physics); GMSL,
GISTEMP (shared data, Book 2); IPCC likelihood language (Book 2 ipcc rows).

**Figures.** [F] `erf` ERF by agent 1750--2019 (bar chart with uncertainty,
AR6 Annex III); [F] `erf` ERF time series total/CO2/aerosol 1750--2019; [F]
`gistemp` (shared data) global temperature anomaly with 1850--1900 offset
(ledger); [F] `feedbacks` feedback parameters bar chart (AR6 Table 7.10
values); [F] `tcre` warming vs cumulative CO2 line with the remaining budget
read off; [F] `sealevel_budget` component stack (AR6 Table 9.5); [S] energy
budget diagram ΔF, λΔT, ΔN; [AI] none; [P] none.

**Ledger.** AR6 WG1 SPM A.1, A.2, A.4, B.1, D.1 statements; Chapter 7 tables
7.8 (ERF), 7.10 (feedbacks), section 7.5 (ECS); Chapter 9 Table 9.5 (sea
level); Chapter 3 attribution; Annex III data (Zenodo, CC-BY 4.0); TCRE
1.65 °C per 1000 GtC likely 1.0--2.3 (check); remaining budgets SPM Table
SPM.2; reuse Book 2 `ipcc:*` rows; energy imbalance 2006--2018 (AR6).

**Datasets.** `bachelor-2-ar6-erf` (AR6 Annex III ERF table, Zenodo record,
CC-BY 4.0); shared gistemp, co2-mlo, gmsl-altimetry.

**Weekend problem: "Reading the budget."** Part I sum the ERF components
(AR6 values printed); Part II energy imbalance and λ from ΔN, ΔF, ΔT (AR6
values): an observational ECS estimate; Part III TCRE from the printed
warming and cumulative emissions; Part IV remaining carbon budget for 1.5 °C
and 2 °C (50%), compared with AR6 SPM.2. **Named number: the remaining
carbon budget for 1.5 °C computed from the TCRE (Gt CO2).**

---

## Ch. 28 Geological Hazards and Risk --- `geological-hazards`

**Hook.** A building designed for the earthquake that happens once in 475
years has a one-in-ten chance of meeting it during a fifty-year life. Hazard
science is the science of such numbers.

**Sections.**
1. Hazard, exposure, vulnerability, risk (definitions re-founded with the
   product formula, recall Book 1 g9); natural vs geological hazard.
2. Probability tools: return period re-founded; Poisson process (proposition:
   P(at least one in t) = 1 − e^{−t/T}); exceedance probability; the 475-year
   = 10% in 50 years result (corollary); Gutenberg--Richter recalled (Book 3);
   checking Poisson on the USGS M≥6 catalogue (interevent times, figdata on
   shared data).
3. Seismic hazard: PSHA in outline (sources, recurrence, ground-motion
   prediction equations, hazard curve); PGA; site effects (descriptive);
   a toy PSHA in figdata (one source zone, GR, a sourced GMPE).
4. Volcanic hazard: hazard zones (link ch. 6), probabilistic eruption
   forecasting (event trees told).
5. Landslides: infinite slope model (proposition: factor of safety with
   cohesion, friction and pore pressure; Coulomb criterion recalled from
   Book 3); triggers (rain, earthquakes); debris flows.
6. Tsunamis: generation, shallow-water speed (proposition: c = sqrt(g h),
   recalled from physics waves if owned there), run-up (descriptive, ledger:
   2004, 2011); warning times.
7. Floods: flood frequency analysis (Gumbel told or empirical plotting
   positions; proposition: Weibull plotting position T = (n+1)/m).
8. Monitoring and early warning (descriptive; no policy).

**Definitions.** geological hazard (qualified: chemistry owns lab "hazard",
Book 1 g5 owns "natural hazard" --- recall it); exposure; risk (qualified:
"disaster risk" or "geological risk"; Book 1 g9 owns "risk" --- re-found as
"risk (geological)"? propose qualified "seismic risk"? see report); return
period (re-founded, Book 2 g10.08); exceedance probability; Poisson
recurrence model; probabilistic seismic hazard analysis (owner per OUTLINE:
"probabilistic hazard"); ground-motion prediction equation; peak ground
acceleration; hazard curve; factor of safety (slope); debris flow; tsunami
run-up; flood frequency curve; early warning system.

**Recall.** Natural hazard, landslide (Book 1 g5); risk, vulnerability,
prevention, hazard map (Book 1 g9); Gutenberg--Richter law, b-value, seismic
moment, moment magnitude, focal mechanism, Coulomb criterion, pore-fluid
pressure, effective stress (Book 3); tsunami (Book 1/2 --- check); hazard in
the lab sense (chemistry); Poisson distribution (math books: recall in prose).

**Figures.** [F] `poisson` exceedance probability vs exposure time for return
periods 50, 475, 2475 yr; [F] `interevent` USGS M≥6 interevent-time
distribution vs exponential (shared usgs-m6 data); [F] `psha` toy hazard curve
(annual exceedance vs PGA) with the 475-yr PGA read off; [S] infinite slope
force diagram; [F] `slope` factor of safety vs pore-pressure ratio for three
slope angles; [S] hazard × exposure × vulnerability diagram; [P] a landslide
(USGS PD, verify); [P] tsunami damage or run-up (NOAA/USGS PD, verify);
[AI] none.

**Ledger.** GMPE coefficients (a published, openly available simple GMPE);
2004 Indian Ocean and 2011 Tōhoku tsunami run-up (ledger; Book 3 may have
Tōhoku rows); building-code convention 475 yr (source); UNDRR definitions of
hazard/exposure/vulnerability (source); USGS catalogue (shared data:usgs-comcat).

**Datasets.** shared `usgs-m6`; none new.

**Weekend problem: "A town between a fault and a slope."** Part I GR
recurrence of M≥5, M≥6, M≥7 on a nearby source zone; Part II PGA at the town
from the GMPE for each magnitude; Part III hazard curve and the 475-yr PGA;
Part IV slope above the town: factor of safety dry and saturated, and the
earthquake that triggers failure (pseudo-static, admitted). **Named number:
the peak ground acceleration with a 10% chance of exceedance in 50 years
(g).**

---

## Ch. 29 Ore Deposits --- `ore-deposits`

**Hook.** Copper makes up 60 parts per million of the crust. A copper mine
needs about 5000. Every ore deposit is a natural concentrator that worked a
hundredfold.

**Sections.**
1. Ore and grade re-founded: ore, gangue, grade, cut-off grade, tonnage,
   concentration factor (proposition: CF = grade/crustal abundance);
   reserves vs resources (descriptive, ledger for definitions).
2. Magmatic deposits: chromite and PGE in layered intrusions (link ch. 8),
   Ni--Cu sulfides (sulfide saturation, R-factor proposition: Campbell &
   Naldrett 1979 mass balance); kimberlites and diamonds; pegmatites (Li).
3. Hydrothermal deposits: fluids, metal transport as chloride complexes
   (recall chemistry), precipitation by cooling/boiling/mixing; porphyry
   copper (link arcs ch. 9); epithermal Au; VMS at ridges (black smokers,
   Book 3 recall); SEDEX; MVT; orogenic gold.
4. Sedimentary and supergene deposits: placers re-founded (settling recall
   Book 3); BIF iron (link ch. 18); evaporites and potash; supergene enrichment
   and gossans; laterites (bauxite, Ni) recalled (Book 3).
5. Grade and tonnage: log-normal distributions of deposit size and grade
   (proposition: product of log-normals is log-normal; figdata on USGS
   porphyry copper data); grade--tonnage curves.
6. Exploration: geochemical anomalies (stream sediments, soils), geophysics
   (magnetics, IP, gravity: descriptive), drilling; resource estimation
   (descriptive).
7. `inthefield` exploration geologists logging drill core (third person).

**Definitions.** gangue ("ore" itself is chemistry g5's: recalled); ore grade; cut-off grade; tonnage
(of a deposit); concentration factor (re-founded, Book 1 g9); ore deposit
(re-founded, Book 1 g9); ore-deposit type (owner per OUTLINE: magmatic,
hydrothermal, sedimentary, supergene); R-factor; hydrothermal fluid; porphyry
copper deposit; epithermal deposit; volcanogenic massive sulfide deposit;
sedimentary exhalative deposit; Mississippi Valley-type deposit; orogenic gold
deposit; placer (re-founded, Book 1 g9); supergene enrichment; gossan;
grade--tonnage curve (owner per OUTLINE); geochemical anomaly.

**Recall.** Vein, placer, reserve, concentration factor (Book 1 g9);
settling, Stokes (Book 3 / physics); hydrothermal vents, black smokers
(Book 3 ch. 13); laterite (Book 3 ch. 19); evaporite (Book 3 ch. 22);
solubility, complexation, redox (chemistry); log-normal distribution (math).

**Figures.** [F] `grade_tonnage` porphyry Cu tonnage and grade histograms on
log axes with fitted log-normals (USGS data); [F] `grade_tonnage`
grade--tonnage scatter with contained-metal isolines; [S] porphyry system
cross-section (potassic, phyllic, propylitic zones, epithermal above); [S]
supergene profile (gossan, leached cap, enrichment blanket, protore); [S] VMS
mound section; [P] gossan (Rio Tinto, Commons, verify); [P] Bingham Canyon
open pit (Commons/NASA, verify); [AI] core shed with drill core trays
(generic).

**Ledger.** Crustal abundances (Rudnick & Gao rows from ch. 3); typical
cut-off grades; porphyry Cu dataset (Singer et al. 2008 USGS OFR 2008-1155,
PD); Bingham Canyon facts; R-factor equation source; examples' tonnages.

**Datasets.** `bachelor-2-porphyry-cu` (USGS OFR 2008-1155 grade--tonnage
table, PD; check format: .xls/.csv/.dbf).

**Weekend problem: "A porphyry prospect."** An invented prospect with drill
assays. Part I average grade and concentration factor; Part II tonnage above
several cut-offs (grade--tonnage curve given as a log-normal); Part III
contained copper; Part IV where the prospect sits in the USGS population
(percentile). **Named number: the copper contained above the 0.3% cut-off
(million tonnes).**

---

## Ch. 30 Energy Geology --- `energy-geology`

**Hook.** Oil is plankton cooked slowly for a few million years at 100 °C;
geothermal heat is the same Earth's warmth taken directly. Both obey the same
physics of temperature and time.

**Sections.**
1. The petroleum system quantified (recall Book 2 g11.09): kerogen types (I,
   II, III; van Krevelen diagram, sourced H/C, O/C), maturation kinetics
   (proposition: first-order Arrhenius conversion recalled from chemistry,
   with a burial history at constant heating rate; figdata); vitrinite
   reflectance and the oil window; TTI (Lopatin) told; generation, expulsion,
   migration, trapping; volumetrics (proposition: STOIIP formula).
2. Unconventional resources: shale oil/gas (descriptive); coal rank recalled
   (Book 2 g11.09 owns "coal" and "coal rank").
3. Geothermal energy: heat in place (proposition: volumetric heat in place),
   high- and low-enthalpy systems; hydrothermal convection (descriptive);
   enhanced geothermal systems; induced seismicity (observational, ledger).
4. Uranium: deposit types (unconformity-related, roll-front, ledger), Oklo
   natural reactors (history box; proposition: 235U abundance 2 Ga ago from
   decay, exponential).
5. Geological CO2 storage: trapping mechanisms (structural, residual,
   solubility, mineral); storage capacity (proposition: M = A h φ ρ_CO2 E,
   sourced efficiency factor); Sleipner as an observed case (ledger
   injected mass); leakage monitoring (descriptive). Physical science only, no
   policy.
6. `inthefield` reading a well log (third person; Book 3 borehole logs
   recalled).

**Definitions.** kerogen type; van Krevelen diagram; vitrinite reflectance;
time--temperature index (if kept); hydrocarbon generation; expulsion
(prose?); stock tank oil initially in place (STOIIP, in its proposition);
recovery factor; unconventional reservoir; geothermal system;
heat in place; high-enthalpy resource; low-enthalpy resource (one definition);
enhanced geothermal system; induced seismicity; unconformity-related uranium
deposit; roll-front uranium deposit; natural nuclear reactor (prose,
history); geological CO2 storage; CO2 trapping mechanisms (structural,
residual, solubility, mineral in one definition); storage efficiency factor.

**Recall.** Source rock, kerogen, oil window, maturation, migration,
reservoir rock, seal, trap, petroleum system, coal (Book 2 g11.09); geothermal
energy, heat flow (Book 2 g12.06 / Book 3); Arrhenius law, activation energy,
first-order reaction (chemistry); porosity, permeability (Book 1/3);
borehole log (Book 3 ch. 5); radioactive decay (physics); supercritical fluid
(chemistry/physics --- check owner).

**Figures.** [F] `maturation` transformation ratio vs temperature for two
heating rates (Arrhenius with a sourced activation-energy distribution);
[F] `maturation` burial history with isotherms and oil window; [S] petroleum
system events chart; [S] geothermal system cross-section; [S] CO2 trapping
mechanisms over time (contribution shares, after a sourced IPCC SRCCS figure:
redraw as schematic, ledger); [F] `co2_density` CO2 density vs depth along a
geotherm (from a sourced equation of state table, NIST webbook? check terms)
showing the 800 m supercritical threshold; [S] van Krevelen diagram with
kerogen paths (sourced points); [P] a geothermal power plant (Commons,
verify); [AI] a drilling rig on land at night (generic).

**Ledger.** Kerogen kinetic parameters (open source, e.g. Burnham 2017 or
Pepper & Corvi 1995 if open); vitrinite reflectance oil window bounds;
Oklo facts (age 2 Ga, 235U then 3.7%); Sleipner injected CO2 (Equinor or
open paper); IPCC SRCCS trapping; NIST CO2 densities (NIST webbook terms ---
check; else Span & Wagner via an open table); heat capacity of rocks;
geothermal plant capacities (example).

**Datasets.** Optional `bachelor-2-co2-density` (NIST webbook isotherm
fetch --- check terms; else analytic Peng--Robinson in figdata with sourced
constants).

**Weekend problem: "One basin, two uses."** An invented basin. Part I burial
history and the time the source rock enters the oil window; Part II
transformation ratio today (Arrhenius); Part III oil generated and in place
with recovery factor; Part IV the depleted reservoir as a CO2 store:
capacity. **Named number: the CO2 storage capacity of the depleted reservoir
(million tonnes).**

---

## Ch. 31 Field and Lab Methods II --- `field-lab-methods-2`

**Hook.** Every number in this book's petrology chapters began as a rock in
a bag, a thin section under a microscope and a powder in an instrument.

**Sections.**
1. Igneous and metamorphic petrography: polarising microscope and
   birefringence recalled (Book 3 ch. 3); textures (porphyritic, ophitic,
   cumulate, granoblastic, lepidoblastic); porphyroblasts and inclusion
   trails (timing relative to foliation); reaction textures (coronas,
   symplectites); modal analysis by point counting (proposition: binomial
   counting error σ = sqrt(p(1−p)/n)).
2. Whole-rock analysis: X-ray fluorescence (principle, Moseley's law recalled
   from physics if owned; fused beads; calibration with reference materials);
   ICP-MS recalled (chemistry b2) for trace elements; calibration curves, LOD,
   trueness, precision recalled (chemistry b2); reference materials (USGS
   BHVO-2 etc.).
3. Mineral analysis: electron microprobe (WDS, principle, spot size,
   ZAF corrections told); mineral formula recalculation (method box: oxygen
   normalisation, recall Book 3 structural formula).
4. Isotope analysis: TIMS and MC-ICP-MS; isotope dilution (proposition: the
   isotope dilution equation from mass balance); mass bias correction
   (exponential law told).
5. A mapping campaign: planning, traverses, notebooks, sampling strategy
   (third person, observation only), from map to section to report (link
   Book 3 ch. 4 and the Varden Hills: a crystalline-basement mapping
   exercise on the granite/schist inlier of the Varden Hills).
6. Data quality: totals, LOI, normalisation, error propagation with partial
   derivatives (Year 2 math).

**Definitions.** igneous texture names (ophitic, granoblastic etc. in one
definition: "rock texture" qualified); porphyroblast; poikiloblast (with
porphyroblast); inclusion trail; reaction texture (corona); modal analysis;
point counting (with modal analysis); X-ray fluorescence analysis; fused
bead; reference material (geochemical; chemistry b2 may own "reference
material"/"certified reference material" --- grep); loss on ignition;
electron microprobe; wavelength-dispersive spectrometry; mineral formula
recalculation (method, not definition); thermal ionisation mass spectrometry;
multi-collector ICP-MS; isotope dilution (in its proposition); mass bias.

**Recall.** Polarising microscope, crossed polars, birefringence,
interference colour, thin section, structural formula (Book 3 ch. 2--3);
foliation, schistosity (Book 3 ch. 17); ICP, ICP-MS, mass spectrometry,
calibration curve, LOD, trueness, precision (chemistry b2); XRD (chemistry b3);
X-rays, Moseley (physics --- check); Varden Hills (Book 3 ch. 4).

**Figures.** [F] `point_counting` relative error vs number of points for
p = 0.05, 0.2, 0.5; [F] `xrf_calibration` calibration line from USGS reference
materials certified SiO2 vs simulated intensities (tested regression); [S]
porphyroblast inclusion-trail sketches (pre-, syn-, post-tectonic); [S]
microprobe schematic (electron gun, sample, WDS crystal, detector); [S]
isotope dilution mixing diagram; [F] `varden_inlier` Varden Hills basement
inlier map (region.py granite/schist with contours) as the mapping-campaign
base; [P] thin-section photos under crossed polars (Commons, verify CC): a
garnet porphyroblast with inclusion trails, an ophitic texture; [P]
electron microprobe instrument (Commons, verify); [AI] a field party at a
camp table with maps and notebooks (generic, observation only).

**Ledger.** USGS reference material certificates (BHVO-2, BCR-2, AGV-2,
RGM-2, G-2, GSP-2, W-2a); microprobe spot size, detection limits (source);
isotope dilution spike example (source or invented clearly); Van der Plas &
Tobi 1965 (chart, check access).

**Datasets.** None (ledger certificate values).

**Weekend problem: "From outcrop to analysis."** Part I point counting a
Varden granite thin section (counts given): mode, error; Part II QAPF name;
Part III XRF calibration from three standards (least squares) and an unknown;
Part IV isotope dilution for Sr in the granite with a given spike, and the
propagated uncertainty. **Named number: the Sr concentration of the Varden
granite by isotope dilution (ppm).**

---

## Homographs (Phase C linker: `tools/term_config/book4_en.py`)

Bare words never defined; only qualified forms are terms. STOP or EXTRA_PROTECT
as needed at Phase C:

| bare word | meanings in this book | defined form(s) |
|---|---|---|
| front | weather front; thrust front; ore front (roll-front) | occluded front, stationary front, frontal surface |
| trough | upper-level trough; trench; tectonic trough | upper-level trough |
| ridge | upper-level ridge; ocean ridge; topographic ridge | upper-level ridge |
| facies | metamorphic facies; sedimentary facies; ichnofacies | metamorphic facies, ichnofacies |
| series | magmatic series; time series; metamorphic series; Bowen's series | magmatic series, tholeiitic series, metamorphic series |
| zone | metamorphic zone; biozone; hazard zone; fault zone | Barrovian zones |
| grade | ore grade; metamorphic grade (Book 2) | ore grade, cut-off grade |
| window | tectonic window; oil window (Book 2); atmospheric window (Book 3) | tectonic window |
| assimilation | crustal assimilation; data assimilation | crustal assimilation, data assimilation |
| exposure | hazard exposure; outcrop exposure | exposure (hazard) --- EXTRA_PROTECT outcrop uses |
| mixing | magma mixing; mixing ratio; mixed layer | magma mixing, mixing ratio, mixing hyperbola |
| reservoir | mantle reservoir; reservoir rock (Book 2); carbon reservoir (biology) | depleted mantle etc. (no bare "reservoir") |
| index | VEI; climate index; index mineral (Book 2) | climate index, Oceanic Niño Index |
| collapse | gravitational collapse (orogen); flank collapse; cloud collapse | gravitational collapse (of an orogen), flank collapse |
| core | dense core (cloud); Earth's core; drill core; ice core | dense core |
| disc | protoplanetary disc | protoplanetary disc |
| type | I-/S-/A-type; kerogen type | I-type granite... |
| budget | carbon budget; sea-level budget; energy budget | remaining carbon budget, sea-level budget |
| sensitivity | climate sensitivity | equilibrium climate sensitivity |
| fingerprint | isotopic fingerprint (ch. 4 prose); climate fingerprint | fingerprint (climate) --- protect ch. 4 |
| detection | detection of climate change; limit of detection (chemistry) | detection (of climate change) |
| risk / hazard | lab sense (chemistry); geological | geological hazard |
| precession | axial precession (Book 3?); climatic precession | climatic precession |
| stage | volcano stage; ICS stage; Wilson cycle stage | shield stage |
| plume | mantle plume (Book 3); eruption plume | eruption column |
| cycle | Wilson cycle; supercontinent cycle; carbon cycle; glacial cycle | Wilson cycle etc. |
| primary | primary magma; primary mineral | primary magma |
| depleted / enriched | depleted mantle (isotopic) | depleted mantle |
| stretching | stretching model; stretching lineation (Book 3) | stretching model, stretching factor |
| saturation | volatile saturation; silica saturation; relative humidity | silica saturation, volatile saturation |
