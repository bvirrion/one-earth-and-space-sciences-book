# DEFINITIONS --- Book 5 (University Year 3, `bachelor-3`, prefix `b3`)

Phase A term map, 2026-10-23. One row per term: the chapter that defines it
(`\emph{term}\index{term}` inside the `definition` with that label, or indexed
in its theorem/proposition), the label, the status (**new** = defined nowhere
else in the series or the sister series; **re-founded** = a school notion
defined again at university level), and the owner check. Generated from the
Phase A plan; checked on 2026-10-23 by exact and qualified-form matching
against every `\index` entry of the written chapters of this series and of
the physics, chemistry, biology and mathematics series, and against
`sources/book{1,2,3,4}/DEFINITIONS.md` (Book 3 ch. 21--29 and Book 4 are still
being written: re-check at Phase C). Status and labels may move during
Phase B; this file is updated with every chapter.

Rules: a term is defined only here; another chapter of this book recalls it
with `\cref`; another volume recalls it in prose. A theorem that derives a
notion owned elsewhere (Ekman spiral, Rossby wave, normal gravity, AFC) is
titled by its content and does **not** index the owned term.

## Terms defined in this book

### Ch. 1 `seismology-imaging`

| term | ch | label | status | note |
|---|---|---|---|---|
| ray parameter | 1 | `def:b3:seismology-imaging:ray-parameter` | new |  |
| turning point (of a seismic ray) | 1 | `def:b3:seismology-imaging:ray-parameter` | new | qualified |
| Herglotz--Wiechert inversion | 1 | `prop:b3:seismology-imaging:herglotz` | new | indexed in its proposition |
| travel-time table | 1 | `def:b3:seismology-imaging:tables` | new |  |
| Rayleigh wave | 1 | `def:b3:seismology-imaging:surface-waves` | new |  |
| Love wave | 1 | `def:b3:seismology-imaging:surface-waves` | new |  |
| surface-wave dispersion | 1 | `def:b3:seismology-imaging:dispersion` | new | qualified; physics owns dispersion relation, phase and group velocity |
| forward problem | 1 | `def:b3:seismology-imaging:inverse` | new |  |
| inverse problem | 1 | `def:b3:seismology-imaging:inverse` | new |  |
| weighted least-squares estimate | 1 | `thm:b3:seismology-imaging:wls` | new | indexed in its theorem; theorem with derivation and covariance; math owns least squares |
| damped least squares | 1 | `def:b3:seismology-imaging:damped` | new |  |
| trade-off curve | 1 | `def:b3:seismology-imaging:damped` | new |  |
| model resolution matrix | 1 | `def:b3:seismology-imaging:resolution` | new |  |
| seismic tomography | 1 | `def:b3:seismology-imaging:tomography` | new | OUTLINE Y3 owner |
| travel-time residual | 1 | `def:b3:seismology-imaging:tomography` | new |  |
| checkerboard test | 1 | `def:b3:seismology-imaging:checkerboard` | new |  |

### Ch. 2 `exploration-seismology`

| term | ch | label | status | note |
|---|---|---|---|---|
| seismic refraction survey | 2 | `def:b3:exploration-seismology:surveys` | new | Book 3 ch. 9 owns head wave, crossover distance |
| seismic reflection survey | 2 | `def:b3:exploration-seismology:surveys` | new |  |
| seismic wavelet | 2 | `def:b3:exploration-seismology:wavelet` | new |  |
| Ricker wavelet | 2 | `def:b3:exploration-seismology:wavelet` | new |  |
| reflectivity series | 2 | `def:b3:exploration-seismology:synthetic` | new |  |
| synthetic seismogram | 2 | `prop:b3:exploration-seismology:synthetic` | new | indexed in its proposition; convolutional model; math owns convolution |
| tuning thickness | 2 | `def:b3:exploration-seismology:resolution` | new |  |
| Fresnel zone | 2 | `def:b3:exploration-seismology:fresnel` | new |  |
| common midpoint | 2 | `def:b3:exploration-seismology:cmp` | new |  |
| fold (of seismic coverage) | 2 | `def:b3:exploration-seismology:cmp` | new | qualified: fold (structural) is Book 3's |
| normal moveout | 2 | `thm:b3:exploration-seismology:nmo` | new | indexed in its theorem; hyperbola derived |
| stacking velocity | 2 | `def:b3:exploration-seismology:velocities` | new |  |
| root-mean-square velocity | 2 | `def:b3:exploration-seismology:velocities` | new |  |
| interval velocity | 2 | `def:b3:exploration-seismology:velocities` | new |  |
| Dix equation | 2 | `thm:b3:exploration-seismology:dix` | new | indexed in its theorem |
| stacking (seismic) | 2 | `def:b3:exploration-seismology:stack` | new | qualified |
| seismic migration | 2 | `def:b3:exploration-seismology:migration` | new | qualified: Book 2 g11 owns migration (of oil and gas) |
| seismic stratigraphy | 2 | `def:b3:exploration-seismology:seismic-stratigraphy` | new |  |
| seismic facies | 2 | `def:b3:exploration-seismology:seismic-stratigraphy` | new |  |
| reflection termination | 2 | `def:b3:exploration-seismology:terminations` | new |  |
| onlap | 2 | `def:b3:exploration-seismology:terminations` | new | ch. 16 recalls |
| downlap | 2 | `def:b3:exploration-seismology:terminations` | new |  |
| toplap | 2 | `def:b3:exploration-seismology:terminations` | new |  |
| erosional truncation | 2 | `def:b3:exploration-seismology:terminations` | new |  |

### Ch. 3 `gravity-geodesy`

| term | ch | label | status | note |
|---|---|---|---|---|
| geopotential | 3 | `def:b3:gravity-geodesy:geopotential` | new | physics owns gravitational potential energy |
| spherical-harmonic expansion of the geopotential | 3 | `prop:b3:gravity-geodesy:harmonics` | new | indexed in its proposition; physics/chemistry own spherical harmonics |
| dynamical form factor | 3 | `def:b3:gravity-geodesy:j2` | new | J2 indexed here; OUTLINE Y3 owner; Sync 1: Y3 keeps J2 |
| MacCullagh's formula | 3 | `thm:b3:gravity-geodesy:maccullagh` | new | indexed in its theorem |
| reference ellipsoid | 3 | `def:b3:gravity-geodesy:ellipsoid` | re-founded | g10 owner; Sync 1: Y3 keeps the ellipsoid |
| Somigliana's formula | 3 | `prop:b3:gravity-geodesy:somigliana` | new | indexed in its proposition; normal gravity is Book 3's: recalled |
| satellite gravimetry | 3 | `def:b3:gravity-geodesy:satgrav` | new |  |
| equivalent water height | 3 | `def:b3:gravity-geodesy:satgrav` | new |  |
| lithospheric flexure | 3 | `def:b3:gravity-geodesy:flexure` | new | OUTLINE Y3 owner ('flexure') |
| flexural rigidity | 3 | `def:b3:gravity-geodesy:flexure` | new |  |
| effective elastic thickness | 3 | `def:b3:gravity-geodesy:flexure` | new |  |
| flexural parameter | 3 | `def:b3:gravity-geodesy:flexure` | new |  |
| forebulge | 3 | `def:b3:gravity-geodesy:flexure` | new | check Book 4 ch. 13 at writing (foreland basin) |
| regional isostatic compensation | 3 | `def:b3:gravity-geodesy:flexure` | new | Book 3 owns isostasy, Airy, Pratt |

### Ch. 4 `palaeomagnetism`

| term | ch | label | status | note |
|---|---|---|---|---|
| main geomagnetic field | 4 | `def:b3:palaeomagnetism:main-field` | new | physics g4/g11 own the Earth as a magnet, magnetic declination |
| geocentric axial dipole | 4 | `def:b3:palaeomagnetism:gad` | new |  |
| magnetic inclination | 4 | `def:b3:palaeomagnetism:gad` | new | qualified form, as 'magnetic declination' |
| dipole formula | 4 | `thm:b3:palaeomagnetism:dipole-formula` | new | indexed in its theorem; tan I = 2 tan(lambda) derived |
| secular variation | 4 | `def:b3:palaeomagnetism:secular` | new |  |
| International Geomagnetic Reference Field | 4 | `def:b3:palaeomagnetism:igrf` | new |  |
| geodynamo | 4 | `def:b3:palaeomagnetism:geodynamo` | new | told; descriptive |
| natural remanent magnetisation | 4 | `def:b3:palaeomagnetism:remanence` | new | check Book 2 g11 at writing |
| thermoremanent magnetisation | 4 | `def:b3:palaeomagnetism:remanence` | new |  |
| detrital remanent magnetisation | 4 | `def:b3:palaeomagnetism:remanence` | new |  |
| chemical remanent magnetisation | 4 | `def:b3:palaeomagnetism:remanence` | new |  |
| blocking temperature | 4 | `def:b3:palaeomagnetism:blocking` | new | physics owns Curie temperature |
| stepwise demagnetisation | 4 | `def:b3:palaeomagnetism:demag` | new |  |
| Zijderveld diagram | 4 | `def:b3:palaeomagnetism:demag` | new |  |
| characteristic remanent magnetisation | 4 | `def:b3:palaeomagnetism:demag` | new |  |
| Fisher distribution | 4 | `prop:b3:palaeomagnetism:fisher` | new | indexed in its proposition |
| alpha95 (confidence cone) | 4 | `def:b3:palaeomagnetism:fisher` | new |  |
| virtual geomagnetic pole | 4 | `def:b3:palaeomagnetism:vgp` | new |  |
| palaeolatitude | 4 | `def:b3:palaeomagnetism:vgp` | new | Book 3 ch. 15 uses the word in a pointer only |
| apparent polar wander | 4 | `def:b3:palaeomagnetism:apw` | new | OUTLINE Y3 owner |
| apparent polar wander path | 4 | `def:b3:palaeomagnetism:apw` | new |  |
| true polar wander | 4 | `def:b3:palaeomagnetism:tpw` | new |  |
| magnetostratigraphy | 4 | `def:b3:palaeomagnetism:magstrat` | new | OUTLINE says re-founds g11 but no school book names it; Book 3 ch. 12 owns polarity chron, GPTS |
| geomagnetic excursion | 4 | `def:b3:palaeomagnetism:excursion` | new |  |

### Ch. 5 `lithosphere-thermal-models`

| term | ch | label | status | note |
|---|---|---|---|---|
| half-space cooling model | 5 | `def:b3:lithosphere-thermal-models:half-space` | new | Book 3 ch. 10/13 forward pointer |
| error-function geotherm | 5 | `thm:b3:lithosphere-thermal-models:half-space` | new | indexed in its theorem; derived (similarity variable) |
| plate cooling model | 5 | `def:b3:lithosphere-thermal-models:plate-model` | new | OUTLINE Y3 owner |
| plate-model temperature series | 5 | `thm:b3:lithosphere-thermal-models:plate-model` | new | indexed in its theorem; Fourier series; math owns Fourier series |
| heat-flow--age relation | 5 | `prop:b3:lithosphere-thermal-models:heat-flow-age` | new | indexed in its proposition |
| thermal subsidence | 5 | `def:b3:lithosphere-thermal-models:thermal-subsidence` | new | Book 3 owns depth--age law; Book 4 post-rift subsidence |
| reduced heat flow | 5 | `def:b3:lithosphere-thermal-models:continental-geotherm` | new | check Book 3 ch. 10 |
| heat-production depth scale | 5 | `def:b3:lithosphere-thermal-models:continental-geotherm` | new |  |
| thermal Peclet number | 5 | `def:b3:lithosphere-thermal-models:peclet` | new | qualified; check physics |

### Ch. 6 `mantle-convection`

| term | ch | label | status | note |
|---|---|---|---|---|
| Rayleigh number | 6 | `def:b3:mantle-convection:rayleigh` | new | OUTLINE Y3 owner; check physics (Rayleigh--Benard) |
| critical Rayleigh number | 6 | `def:b3:mantle-convection:rayleigh` | new |  |
| Nusselt number | 6 | `def:b3:mantle-convection:nusselt` | new | check physics |
| boundary-layer scaling of convection | 6 | `thm:b3:mantle-convection:scaling` | new | indexed in its theorem; Nu ~ Ra^(1/3) |
| ridge-push force | 6 | `prop:b3:mantle-convection:ridge-push` | new | g11 owns ridge push (term); proposition gives the force, indexed under its own qualified name |
| basal drag | 6 | `def:b3:mantle-convection:drag` | new |  |
| plume buoyancy flux | 6 | `def:b3:mantle-convection:buoyancy-flux` | new |  |
| glacial isostatic adjustment | 6 | `def:b3:mantle-convection:gia` | new | g12 owns isostatic rebound |
| isostatic relaxation time | 6 | `def:b3:mantle-convection:gia` | new |  |
| mantle viscosity | 6 | `def:b3:mantle-convection:viscosity-mantle` | new | OUTLINE Y3 owner; physics owns viscosity |
| Maxwell time | 6 | `def:b3:mantle-convection:maxwell` | new | check physics |

### Ch. 7 `deformation-mechanisms`

| term | ch | label | status | note |
|---|---|---|---|---|
| dislocation (crystal defect) | 7 | `def:b3:deformation-mechanisms:dislocation` | new | qualified; chemistry b3 point defect indexed, dislocation in text only |
| dislocation creep | 7 | `def:b3:deformation-mechanisms:creep` | new |  |
| diffusion creep | 7 | `def:b3:deformation-mechanisms:creep` | new |  |
| grain-boundary sliding | 7 | `def:b3:deformation-mechanisms:creep` | new |  |
| pressure solution | 7 | `def:b3:deformation-mechanisms:creep` | new |  |
| dynamic recrystallisation | 7 | `def:b3:deformation-mechanisms:recrystallisation` | new |  |
| recovery (crystal plasticity) | 7 | `def:b3:deformation-mechanisms:recrystallisation` | new | qualified |
| subgrain | 7 | `def:b3:deformation-mechanisms:recrystallisation` | new |  |
| crystallographic preferred orientation | 7 | `def:b3:deformation-mechanisms:cpo` | new |  |
| flow law | 7 | `def:b3:deformation-mechanisms:flow-law` | new | OUTLINE Y3 owner; Book 3 ch. 16 states power-law creep admitted |
| stress exponent | 7 | `def:b3:deformation-mechanisms:flow-law` | new |  |
| homologous temperature | 7 | `def:b3:deformation-mechanisms:flow-law` | new |  |
| deformation mechanism map | 7 | `def:b3:deformation-mechanisms:deformation-map` | new | OUTLINE Y3 owner ('deformation map') |
| palaeopiezometer | 7 | `def:b3:deformation-mechanisms:piezometer` | new |  |
| shear zone | 7 | `def:b3:deformation-mechanisms:shear-zone` | new | check Book 3 ch. 17 |
| strain softening | 7 | `def:b3:deformation-mechanisms:shear-zone` | new |  |
| kinematic indicator | 7 | `def:b3:deformation-mechanisms:kinematic` | new | OUTLINE Y3 owner; Book 3 ch. 17 pointer |
| sense of shear | 7 | `def:b3:deformation-mechanisms:kinematic` | new |  |
| S--C fabric | 7 | `def:b3:deformation-mechanisms:kinematic` | new |  |
| porphyroclast system | 7 | `def:b3:deformation-mechanisms:kinematic` | new |  |
| mica fish | 7 | `def:b3:deformation-mechanisms:kinematic` | new |  |

### Ch. 8 `structural-analysis`

| term | ch | label | status | note |
|---|---|---|---|---|
| stereographic projection | 8 | `def:b3:structural-analysis:stereo` | new | Book 3 ch. 18 pointer (says 'Year 2': defect) |
| equal-angle net | 8 | `def:b3:structural-analysis:stereo` | new |  |
| equal-area projection (of the sphere) | 8 | `def:b3:structural-analysis:stereo` | new | qualified: g9 owns the map sense |
| pole (to a plane) | 8 | `def:b3:structural-analysis:stereo` | new | qualified |
| pi-diagram | 8 | `def:b3:structural-analysis:pi` | new |  |
| beta-axis | 8 | `def:b3:structural-analysis:pi` | new |  |
| orientation tensor | 8 | `def:b3:structural-analysis:orientation-tensor` | new | Book 3 ch. 6 owns mean orientation |
| finite strain analysis | 8 | `def:b3:structural-analysis:strain-analysis` | new |  |
| Fry method | 8 | `def:b3:structural-analysis:strain-analysis` | new |  |
| palaeostress | 8 | `def:b3:structural-analysis:palaeostress` | new |  |
| fault-slip inversion | 8 | `def:b3:structural-analysis:palaeostress` | new |  |
| Wallace--Bott hypothesis | 8 | `def:b3:structural-analysis:palaeostress` | new |  |
| stress ratio | 8 | `def:b3:structural-analysis:palaeostress` | new |  |
| section restoration | 8 | `def:b3:structural-analysis:restoration` | new | Book 4 owns balanced cross-section |
| pin line | 8 | `def:b3:structural-analysis:restoration` | new |  |
| kink-band method | 8 | `def:b3:structural-analysis:restoration` | new |  |

### Ch. 9 `extension-strike-slip`

| term | ch | label | status | note |
|---|---|---|---|---|
| simple-shear rift model | 9 | `def:b3:extension-strike-slip:rift-models` | new | Book 4 owns the (pure-shear) stretching model |
| detachment fault | 9 | `def:b3:extension-strike-slip:detachment` | new | Book 4 owns decollement |
| listric fault | 9 | `def:b3:extension-strike-slip:detachment` | new |  |
| rollover anticline | 9 | `def:b3:extension-strike-slip:detachment` | new |  |
| domino faulting | 9 | `def:b3:extension-strike-slip:domino` | new |  |
| metamorphic core complex | 9 | `def:b3:extension-strike-slip:core-complex` | new |  |
| rolling hinge | 9 | `def:b3:extension-strike-slip:core-complex` | new |  |
| transfer zone | 9 | `def:b3:extension-strike-slip:transfer` | new | avoid bare 'accommodation zone' (homograph with accommodation) |
| restraining bend | 9 | `def:b3:extension-strike-slip:bends` | new |  |
| releasing bend | 9 | `def:b3:extension-strike-slip:bends` | new |  |
| pull-apart basin | 9 | `def:b3:extension-strike-slip:pull-apart` | new |  |
| flower structure | 9 | `def:b3:extension-strike-slip:flower` | new |  |
| Riedel shear | 9 | `def:b3:extension-strike-slip:riedel` | new |  |
| transpression | 9 | `def:b3:extension-strike-slip:transpression` | new |  |
| transtension | 9 | `def:b3:extension-strike-slip:transpression` | new |  |

### Ch. 10 `orogenic-wedges`

| term | ch | label | status | note |
|---|---|---|---|---|
| critical taper | 10 | `def:b3:orogenic-wedges:critical-taper` | new | OUTLINE Y3 owner |
| critical-taper equation | 10 | `thm:b3:orogenic-wedges:critical-taper` | new | indexed in its theorem |
| frontal accretion | 10 | `def:b3:orogenic-wedges:accretion` | new |  |
| tectonic underplating | 10 | `def:b3:orogenic-wedges:accretion` | new | qualified: Book 4 owns mafic underplating |
| ramp (thrust) | 10 | `def:b3:orogenic-wedges:thrust-geometry` | new | qualified |
| flat (thrust) | 10 | `def:b3:orogenic-wedges:thrust-geometry` | new | qualified |
| duplex (thrust) | 10 | `def:b3:orogenic-wedges:thrust-geometry` | new |  |
| out-of-sequence thrust | 10 | `def:b3:orogenic-wedges:thrust-geometry` | new |  |
| fault-bend fold | 10 | `def:b3:orogenic-wedges:thrust-folds` | new |  |
| fault-propagation fold | 10 | `def:b3:orogenic-wedges:thrust-folds` | new |  |
| detachment fold | 10 | `def:b3:orogenic-wedges:thrust-folds` | new |  |
| thermochronology | 10 | `def:b3:orogenic-wedges:thermochronology` | new | Book 3 owns closure temperature, cooling age |
| thermochronometer | 10 | `def:b3:orogenic-wedges:thermochronology` | new |  |
| age--elevation relationship | 10 | `def:b3:orogenic-wedges:age-elevation` | new |  |

### Ch. 11 `petrological-thermodynamics`

| term | ch | label | status | note |
|---|---|---|---|---|
| mineralogical phase rule | 11 | `def:b3:petrological-thermodynamics:goldschmidt` | new | chemistry owns variance and the phase rule: recall; Sync 2 must be amended |
| Gibbs energy--composition diagram | 11 | `def:b3:petrological-thermodynamics:gx` | new |  |
| internally consistent thermodynamic dataset | 11 | `def:b3:petrological-thermodynamics:database` | new |  |
| site-mixing activity model | 11 | `def:b3:petrological-thermodynamics:site-mixing` | new | chemistry owns activity |
| solvus | 11 | `def:b3:petrological-thermodynamics:solvus` | new | check chemistry (miscibility gap is chemistry's) |
| exsolution (mineral) | 11 | `def:b3:petrological-thermodynamics:solvus` | new | qualified; Book 4 owns volatile exsolution |
| Schreinemakers analysis | 11 | `def:b3:petrological-thermodynamics:schreinemakers` | new |  |
| pseudosection | 11 | `def:b3:petrological-thermodynamics:pseudosection` | new | OUTLINE Y3; Sync 2 |
| effective bulk composition | 11 | `def:b3:petrological-thermodynamics:pseudosection` | new |  |
| isopleth (pseudosection) | 11 | `def:b3:petrological-thermodynamics:pseudosection` | new | qualified |
| Gibbs energy minimisation | 11 | `def:b3:petrological-thermodynamics:minimisation` | new |  |

### Ch. 12 `trace-element-modelling`

| term | ch | label | status | note |
|---|---|---|---|---|
| batch melting | 12 | `thm:b3:trace-element-modelling:batch` | new | indexed in its theorem; Shaw equation derived; Sync 2 |
| fractional melting | 12 | `thm:b3:trace-element-modelling:fractional` | new | indexed in its theorem |
| aggregated fractional melt | 12 | `def:b3:trace-element-modelling:fractional` | new |  |
| non-modal melting | 12 | `def:b3:trace-element-modelling:nonmodal` | new |  |
| dynamic melting | 12 | `def:b3:trace-element-modelling:dynamic` | new |  |
| ratio--ratio diagram | 12 | `def:b3:trace-element-modelling:ratios` | new |  |

### Ch. 13 `advanced-geochronology`

| term | ch | label | status | note |
|---|---|---|---|---|
| concordia | 13 | `def:b3:advanced-geochronology:concordia` | new | OUTLINE Y3 |
| discordia | 13 | `def:b3:advanced-geochronology:concordia` | new |  |
| upper intercept | 13 | `def:b3:advanced-geochronology:concordia` | new |  |
| lower intercept | 13 | `def:b3:advanced-geochronology:concordia` | new |  |
| Tera--Wasserburg diagram | 13 | `def:b3:advanced-geochronology:concordia` | new |  |
| 40Ar/39Ar dating | 13 | `def:b3:advanced-geochronology:arar` | new |  |
| J factor | 13 | `def:b3:advanced-geochronology:arar` | new |  |
| age spectrum | 13 | `def:b3:advanced-geochronology:arar` | new |  |
| plateau age | 13 | `def:b3:advanced-geochronology:arar` | new |  |
| model age | 13 | `def:b3:advanced-geochronology:model-age` | new | Book 4 owns CHUR, depleted mantle, epsilon |
| cosmogenic nuclide | 13 | `def:b3:advanced-geochronology:cosmogenic` | new | check Book 3 ch. 20 proposition (indexed?) |
| exposure age | 13 | `def:b3:advanced-geochronology:cosmogenic` | new |  |
| production rate (cosmogenic) | 13 | `def:b3:advanced-geochronology:cosmogenic` | new | qualified |
| fission-track dating | 13 | `def:b3:advanced-geochronology:fission-track` | new |  |
| track annealing | 13 | `def:b3:advanced-geochronology:fission-track` | new |  |
| (U--Th)/He dating | 13 | `def:b3:advanced-geochronology:uthhe` | new |  |
| partial retention zone | 13 | `def:b3:advanced-geochronology:uthhe` | new |  |
| mean square of weighted deviates | 13 | `def:b3:advanced-geochronology:mswd` | new | MSWD |

### Ch. 14 `stable-isotopes`

| term | ch | label | status | note |
|---|---|---|---|---|
| isotopic difference (capital delta) | 14 | `def:b3:stable-isotopes:big-delta` | new | chemistry owns delta value, fractionation factor |
| Rayleigh distillation | 14 | `prop:b3:stable-isotopes:rayleigh-distillation` | new | indexed in its proposition; Book 4 owns the Rayleigh fractionation law (elements) |
| deuterium excess | 14 | `def:b3:stable-isotopes:d-excess` | new |  |
| temperature effect (isotopic) | 14 | `def:b3:stable-isotopes:effects` | new |  |
| amount effect | 14 | `def:b3:stable-isotopes:effects` | new |  |
| continental effect | 14 | `def:b3:stable-isotopes:effects` | new |  |
| palaeothermometry | 14 | `def:b3:stable-isotopes:palaeothermometry` | new | Sync 2 |
| palaeotemperature equation | 14 | `def:b3:stable-isotopes:palaeothermometry` | new |  |
| clumped isotopes | 14 | `def:b3:stable-isotopes:clumped` | new |  |
| carbon isotope excursion | 14 | `def:b3:stable-isotopes:cie` | new | OUTLINE Y3 |
| carbon isotope mass balance | 14 | `prop:b3:stable-isotopes:forg` | new | indexed in its proposition |
| organic carbon burial fraction | 14 | `def:b3:stable-isotopes:forg` | new |  |
| mass-dependent fractionation | 14 | `def:b3:stable-isotopes:mif` | new | check chemistry |
| mass-independent fractionation | 14 | `def:b3:stable-isotopes:mif` | new |  |

### Ch. 15 `water-rock-interaction`

| term | ch | label | status | note |
|---|---|---|---|---|
| saturation index (of a mineral) | 15 | `def:b3:water-rock-interaction:si` | new | qualified; chemistry owns saturation state |
| open carbonate system | 15 | `def:b3:water-rock-interaction:open-closed` | new |  |
| closed carbonate system | 15 | `def:b3:water-rock-interaction:open-closed` | new |  |
| activity diagram (mineral stability) | 15 | `def:b3:water-rock-interaction:activity-diagram` | new |  |
| mineral dissolution rate law | 15 | `def:b3:water-rock-interaction:tst-rate` | new | chemistry owns rate law, transition state |
| weathering-limited regime | 15 | `def:b3:water-rock-interaction:regimes` | new |  |
| supply-limited regime | 15 | `def:b3:water-rock-interaction:regimes` | new |  |
| water--rock ratio | 15 | `def:b3:water-rock-interaction:wr` | new |  |
| reaction-path model | 15 | `def:b3:water-rock-interaction:reaction-path` | new |  |

### Ch. 16 `sequence-stratigraphy`

| term | ch | label | status | note |
|---|---|---|---|---|
| depositional sequence | 16 | `def:b3:sequence-stratigraphy:sequence` | new |  |
| sequence boundary | 16 | `def:b3:sequence-stratigraphy:sequence` | new |  |
| systems tract | 16 | `def:b3:sequence-stratigraphy:systems-tract` | new | OUTLINE Y3 owner |
| lowstand systems tract | 16 | `def:b3:sequence-stratigraphy:systems-tract` | new |  |
| transgressive systems tract | 16 | `def:b3:sequence-stratigraphy:systems-tract` | new |  |
| highstand systems tract | 16 | `def:b3:sequence-stratigraphy:systems-tract` | new |  |
| falling-stage systems tract | 16 | `def:b3:sequence-stratigraphy:systems-tract` | new |  |
| maximum flooding surface | 16 | `def:b3:sequence-stratigraphy:surfaces` | new |  |
| transgressive surface | 16 | `def:b3:sequence-stratigraphy:surfaces` | new |  |
| parasequence | 16 | `def:b3:sequence-stratigraphy:parasequence` | new |  |
| flooding surface | 16 | `def:b3:sequence-stratigraphy:parasequence` | new |  |
| forced regression | 16 | `def:b3:sequence-stratigraphy:regressions` | new | Book 4 owns marine regression |
| normal regression | 16 | `def:b3:sequence-stratigraphy:regressions` | new |  |
| shoreline trajectory | 16 | `def:b3:sequence-stratigraphy:trajectory` | new |  |
| condensed section | 16 | `def:b3:sequence-stratigraphy:condensed` | new |  |
| incised valley | 16 | `def:b3:sequence-stratigraphy:incised` | new |  |
| cyclostratigraphy | 16 | `def:b3:sequence-stratigraphy:cyclostratigraphy` | new | OUTLINE Y3 |
| astronomical tuning | 16 | `def:b3:sequence-stratigraphy:cyclostratigraphy` | new |  |
| periodogram | 16 | `def:b3:sequence-stratigraphy:periodogram` | new | check math (Fourier transform b3) |

### Ch. 17 `facies-models`

| term | ch | label | status | note |
|---|---|---|---|---|
| facies model | 17 | `def:b3:facies-models:facies-model` | new | Book 3 owns sedimentary facies |
| Walther's law | 17 | `thm:b3:facies-models:walther` | new | indexed in its theorem |
| facies association | 17 | `def:b3:facies-models:association` | new |  |
| facies succession | 17 | `def:b3:facies-models:association` | new |  |
| fining-upward succession | 17 | `def:b3:facies-models:association` | new |  |
| coarsening-upward succession | 17 | `def:b3:facies-models:association` | new |  |
| braided river | 17 | `def:b3:facies-models:fluvial` | new | g5 owns meander |
| meandering river | 17 | `def:b3:facies-models:fluvial` | new |  |
| point bar | 17 | `def:b3:facies-models:fluvial` | new |  |
| avulsion | 17 | `def:b3:facies-models:fluvial` | new |  |
| shoreface | 17 | `def:b3:facies-models:shoreface` | new |  |
| fair-weather wave base | 17 | `def:b3:facies-models:shoreface` | new |  |
| storm wave base | 17 | `def:b3:facies-models:shoreface` | new |  |
| hummocky cross-stratification | 17 | `def:b3:facies-models:shoreface` | new |  |
| submarine fan | 17 | `def:b3:facies-models:fan` | new | Book 3 owns turbidite |
| Bouma sequence | 17 | `def:b3:facies-models:fan` | new |  |
| carbonate ramp | 17 | `def:b3:facies-models:platform-types` | new | Book 3 owns carbonate platform |
| rimmed shelf | 17 | `def:b3:facies-models:platform-types` | new |  |
| wireline log | 17 | `def:b3:facies-models:logs` | new | Book 3 owns borehole log |
| gamma-ray log | 17 | `def:b3:facies-models:logs` | new |  |
| sonic log | 17 | `def:b3:facies-models:logs` | new |  |
| density log | 17 | `def:b3:facies-models:logs` | new |  |
| neutron log | 17 | `def:b3:facies-models:logs` | new |  |
| net-to-gross ratio | 17 | `def:b3:facies-models:ntg` | new |  |

### Ch. 18 `quantitative-geomorphology`

| term | ch | label | status | note |
|---|---|---|---|---|
| hillslope diffusion | 18 | `def:b3:quantitative-geomorphology:hillslope` | new | physics owns diffusion equation |
| soil production function | 18 | `def:b3:quantitative-geomorphology:hillslope` | new |  |
| critical hillslope gradient | 18 | `def:b3:quantitative-geomorphology:hillslope` | new |  |
| stream-power law | 18 | `def:b3:quantitative-geomorphology:stream-power` | new | OUTLINE Y3 owner |
| steady-state river profile | 18 | `def:b3:quantitative-geomorphology:stream-power` | new |  |
| channel steepness index | 18 | `def:b3:quantitative-geomorphology:stream-power` | new |  |
| concavity index | 18 | `def:b3:quantitative-geomorphology:stream-power` | new |  |
| chi analysis | 18 | `def:b3:quantitative-geomorphology:chi` | new |  |
| knickpoint | 18 | `def:b3:quantitative-geomorphology:knickpoint` | new |  |
| base level | 18 | `def:b3:quantitative-geomorphology:knickpoint` | new | check g5/g9 |
| detachment-limited incision | 18 | `def:b3:quantitative-geomorphology:limited` | new |  |
| transport-limited incision | 18 | `def:b3:quantitative-geomorphology:limited` | new |  |
| glacial erosion law | 18 | `def:b3:quantitative-geomorphology:glacial-erosion` | new |  |
| glacial buzzsaw | 18 | `def:b3:quantitative-geomorphology:glacial-erosion` | new |  |
| topographic steady state | 18 | `def:b3:quantitative-geomorphology:topo-steady` | new |  |
| erosional isostatic rebound | 18 | `def:b3:quantitative-geomorphology:topo-steady` | new | g12 owns isostatic rebound |

### Ch. 19 `gfd-foundations`

| term | ch | label | status | note |
|---|---|---|---|---|
| Rossby number | 19 | `def:b3:gfd-foundations:numbers` | new | OUTLINE Y3; Sync 2 |
| Ekman number | 19 | `def:b3:gfd-foundations:numbers` | new |  |
| Boussinesq approximation | 19 | `def:b3:gfd-foundations:boussinesq` | new |  |
| hydrostatic approximation | 19 | `def:b3:gfd-foundations:hydrostatic` | new | physics owns the hydrostatic relation |
| f-plane | 19 | `def:b3:gfd-foundations:planes` | new | Book 3 owns Coriolis parameter |
| beta-plane | 19 | `def:b3:gfd-foundations:planes` | new |  |
| Taylor--Proudman theorem | 19 | `thm:b3:gfd-foundations:taylor-proudman` | new | bare \index after the theorem (a theorem name, not harvested) |
| thermal wind | 19 | `thm:b3:gfd-foundations:thermal-wind` | new | indexed in its theorem; OUTLINE Y3; Sync 2 |
| barotropic fluid | 19 | `def:b3:gfd-foundations:baroclinic` | new |  |
| baroclinic fluid | 19 | `def:b3:gfd-foundations:baroclinic` | new |  |
| buoyancy frequency | 19 | `def:b3:gfd-foundations:buoyancy` | new | Book 3 owns static stability; Book 3 ch. 26 names N unindexed in a proof, recalled |
| Rossby radius of deformation | 19 | `def:b3:gfd-foundations:rossby-radius` | new |  |
| inertial oscillation | 19 | `def:b3:gfd-foundations:inertial` | new |  |
| gradient wind | 19 | `def:b3:gfd-foundations:gradient` | new | Book 3 ch. 28 remark (unindexed), recalled |
| Taylor column | 19 | `thm:b3:gfd-foundations:taylor-proudman` | new | prose after the theorem |

### Ch. 20 `atmospheric-dynamics`

| term | ch | label | status | note |
|---|---|---|---|---|
| relative vorticity | 20 | `def:b3:atmospheric-dynamics:vorticity-kinds` | new | physics owns vorticity |
| planetary vorticity | 20 | `def:b3:atmospheric-dynamics:vorticity-kinds` | new |  |
| absolute vorticity | 20 | `def:b3:atmospheric-dynamics:vorticity-kinds` | new |  |
| potential vorticity | 20 | `def:b3:atmospheric-dynamics:pv` | new |  |
| barotropic vorticity equation | 20 | `thm:b3:atmospheric-dynamics:bve` | new | indexed in its theorem; potential vorticity conservation thm:b3:atmospheric-dynamics:pv |
| Rossby-wave dispersion relation | 20 | `thm:b3:atmospheric-dynamics:rossby` | new | indexed in its proposition; Book 4 owns the term Rossby wave |
| stationary Rossby wavelength | 20 | `prop:b3:atmospheric-dynamics:stationary` | new |  |
| baroclinic instability | 20 | `def:b3:atmospheric-dynamics:baroclinic-instability` | new |  |
| Eady model | 20 | `def:b3:atmospheric-dynamics:eady` | new |  |
| available potential energy | 20 | `def:b3:atmospheric-dynamics:ape` | new |  |
| eddy (atmospheric) | 20 | `def:b3:atmospheric-dynamics:eddy` | new |  |
| zonal mean | 20 | `def:b3:atmospheric-dynamics:eddy` | new |  |
| Held--Hou model | 20 | `def:b3:atmospheric-dynamics:held-hou` | new | Book 3 owns Hadley cell; extent theorem thm:b3:atmospheric-dynamics:held-hou |
| atmospheric angular momentum | 20 | `def:b3:atmospheric-dynamics:held-hou` | new |  |

### Ch. 21 `ocean-dynamics`

| term | ch | label | status | note |
|---|---|---|---|---|
| Ekman pumping | 21 | `def:b3:ocean-dynamics:ekman-pumping` | new | Book 3 owns Ekman layer/transport/spiral (spiral derived here, not re-indexed) |
| Ekman depth | 21 | `def:b3:ocean-dynamics:ekman-pumping` | new |  |
| Sverdrup balance | 21 | `thm:b3:ocean-dynamics:sverdrup` | new | indexed in its theorem; OUTLINE Y3 |
| western intensification | 21 | `def:b3:ocean-dynamics:western-intensification` | new | Book 3 owns western boundary current |
| Stommel model | 21 | `def:b3:ocean-dynamics:western-intensification` | new |  |
| Munk boundary layer | 21 | `def:b3:ocean-dynamics:western-intensification` | new |  |
| Stommel--Arons model | 21 | `def:b3:ocean-dynamics:abyssal` | new |  |
| dynamic method | 21 | `def:b3:ocean-dynamics:dynamic-height` | new |  |
| equilibrium tide | 21 | `def:b3:ocean-dynamics:tides` | new | physics owns tides |
| tidal constituent | 21 | `def:b3:ocean-dynamics:tides` | new |  |
| amphidromic point | 21 | `def:b3:ocean-dynamics:amphidrome` | new | own definition after the Kelvin wave |
| cotidal line | 21 | `def:b3:ocean-dynamics:amphidrome` | new |  |
| co-range line | 21 | `def:b3:ocean-dynamics:amphidrome` | new | added in writing |
| Kelvin wave (oceanic) | 21 | `def:b3:ocean-dynamics:kelvin-wave` | new | indexed as "Kelvin wave" |

Unindexed statements of ch. 21: `thm:b3:ocean-dynamics:ekman` (the spiral derived;
Book 3's terms recalled), `prop:b3:ocean-dynamics:pumping`,
`thm:b3:ocean-dynamics:stommel`, `prop:b3:ocean-dynamics:abyssal`,
`thm:b3:ocean-dynamics:equilibrium-tide`, `thm:b3:ocean-dynamics:kelvin`;
method `met:b3:ocean-dynamics:dynamic`.

### Ch. 22 `climate-models`

| term | ch | label | status | note |
|---|---|---|---|---|
| energy-balance model | 22 | `def:b3:climate-models:ebm` | new | OUTLINE Y3 |
| Budyko--Sellers model | 22 | `def:b3:climate-models:budyko-sellers` | new |  |
| multiple climate equilibria | 22 | `def:b3:climate-models:multiple-equilibria` | new | Book 4 owns ice-albedo feedback, snowball Earth |
| saddle-node bifurcation | 22 | `def:b3:climate-models:multiple-equilibria` | new | check math |
| two-layer energy-balance model | 22 | `def:b3:climate-models:two-layer` | new |  |
| general circulation model | 22 | `def:b3:climate-models:gcm` | new |  |
| dynamical core | 22 | `def:b3:climate-models:gcm` | new |  |
| parameterisation | 22 | `def:b3:climate-models:gcm` | new |  |
| Earth system model | 22 | `def:b3:climate-models:esm` | new |  |
| model intercomparison project | 22 | `def:b3:climate-models:cmip` | new |  |
| spin-up (of a model) | 22 | `def:b3:climate-models:spin-up` | new |  |
| emergent constraint | 22 | `def:b3:climate-models:evaluation` | new |  |
| large ensemble | 22 | `def:b3:climate-models:evaluation` | new | Book 4 owns ensemble forecast |

Unindexed statements of ch. 22: `thm:b3:climate-models:response` (response time
C/(-lambda); Book 4's lambda < 0 convention kept), `prop:b3:climate-models:three`,
`prop:b3:climate-models:iceline`, `thm:b3:climate-models:two-layer`. "Primitive
equations" is named in the GCM definition, not indexed (no owner in the series).

### Ch. 23 `hydrogeology`

| term | ch | label | status | note |
|---|---|---|---|---|
| hydraulic head | 23 | `def:b3:hydrogeology:head` | new |  |
| hydraulic gradient | 23 | `def:b3:hydrogeology:head` | new |  |
| Darcy's law | 23 | `thm:b3:hydrogeology:darcy` | new | indexed in its theorem; OUTLINE says re-founds g6 but g6 never names Darcy |
| specific discharge | 23 | `def:b3:hydrogeology:darcy` | new |  |
| hydraulic conductivity | 23 | `def:b3:hydrogeology:darcy` | new |  |
| intrinsic permeability | 23 | `def:b3:hydrogeology:darcy` | new | qualified: g6 owns permeability, physics magnetic permeability |
| seepage velocity | 23 | `def:b3:hydrogeology:seepage` | new |  |
| confined aquifer | 23 | `def:b3:hydrogeology:aquifer-types` | new | checked: no school owner (g6 owns aquifer) |
| unconfined aquifer | 23 | `def:b3:hydrogeology:aquifer-types` | new |  |
| aquitard | 23 | `def:b3:hydrogeology:aquifer-types` | new |  |
| transmissivity | 23 | `def:b3:hydrogeology:storage` | new |  |
| storativity | 23 | `def:b3:hydrogeology:storage` | new |  |
| specific yield | 23 | `def:b3:hydrogeology:storage` | new |  |
| groundwater-flow equation | 23 | `thm:b3:hydrogeology:flow-equation` | new | indexed in its theorem |
| Theis solution | 23 | `thm:b3:hydrogeology:theis` | new | indexed in its theorem |
| Cooper--Jacob approximation | 23 | `prop:b3:hydrogeology:cooper-jacob` | new | indexed in its proposition |
| cone of depression | 23 | `def:b3:hydrogeology:cone` | new | checked: no g10 owner |
| flow net | 23 | `def:b3:hydrogeology:flow-net` | new |  |
| advection--dispersion equation | 23 | `thm:b3:hydrogeology:ade` | new | indexed in its theorem |
| hydrodynamic dispersion | 23 | `def:b3:hydrogeology:ade` | new |  |
| dispersivity | 23 | `def:b3:hydrogeology:ade` | new |  |
| retardation factor (sorption) | 23 | `def:b3:hydrogeology:retardation` | new | qualified: Book 3 owns optical retardation |

Unindexed statements of ch. 23: `prop:b3:hydrogeology:thiem` (steady radial flow);
method `met:b3:hydrogeology:flow-net`. "Potentiometric surface", "piezometer",
"hydraulic diffusivity", "well function" and "distribution coefficient" are named in
definitions or theorems, not indexed.

### Ch. 24 `glaciology`

| term | ch | label | status | note |
|---|---|---|---|---|
| Glen's flow law | 24 | `thm:b3:glaciology:glen` | new | indexed in its theorem; OUTLINE says re-founds g8 but g8 never names Glen |
| rate factor (ice) | 24 | `def:b3:glaciology:glen` | new |  |
| basal sliding | 24 | `def:b3:glaciology:sliding` | new |  |
| shallow-ice approximation | 24 | `def:b3:glaciology:sia` | new |  |
| plastic ice-sheet profile | 24 | `prop:b3:glaciology:nye` | new | indexed in its proposition |
| glacier mass balance | 24 | `def:b3:glaciology:mass-balance` | new |  |
| surface mass balance | 24 | `def:b3:glaciology:mass-balance` | new |  |
| accumulation zone | 24 | `def:b3:glaciology:mass-balance` | new |  |
| ablation zone | 24 | `def:b3:glaciology:mass-balance` | new |  |
| equilibrium-line altitude | 24 | `def:b3:glaciology:mass-balance` | new |  |
| firn | 24 | `def:b3:glaciology:firn` | new |  |
| pore close-off | 24 | `def:b3:glaciology:firn` | new |  |
| ice stream | 24 | `def:b3:glaciology:ice-stream` | new |  |
| grounding line | 24 | `def:b3:glaciology:grounding-line` | new |  |
| calving | 24 | `def:b3:glaciology:grounding-line` | new |  |
| marine ice-sheet instability | 24 | `def:b3:glaciology:misi` | new |  |
| sea-level equivalent | 24 | `def:b3:glaciology:sle` | new | Book 4 owns sea-level budget |
| sea-ice extent | 24 | `def:b3:glaciology:sea-ice` | new | checked: g8 names sea ice, not extent |
| active layer | 24 | `def:b3:glaciology:permafrost` | new | g8 owns permafrost |

Unindexed statements of ch. 24: `thm:b3:glaciology:slab` (slab flow),
`prop:b3:glaciology:response` (glacier response time), `prop:b3:glaciology:flotation`,
`prop:b3:glaciology:sle` (sea-level equivalent of a mass of ice),
`thm:b3:glaciology:stefan` (Stefan's law).

### Ch. 25 `remote-sensing-gis`

| term | ch | label | status | note |
|---|---|---|---|---|
| spectral signature | 25 | `def:b3:remote-sensing-gis:signature` | new | g9 owns remote sensing, satellite image |
| spatial resolution | 25 | `def:b3:remote-sensing-gis:resolutions` | new |  |
| spectral resolution | 25 | `def:b3:remote-sensing-gis:resolutions` | new |  |
| revisit time | 25 | `def:b3:remote-sensing-gis:resolutions` | new |  |
| radiometric resolution | 25 | `def:b3:remote-sensing-gis:resolutions` | new | added while writing |
| multispectral sensor | 25 | `def:b3:remote-sensing-gis:sensors` | new |  |
| hyperspectral sensor | 25 | `def:b3:remote-sensing-gis:sensors` | new |  |
| atmospheric correction | 25 | `def:b3:remote-sensing-gis:atm-correction` | new |  |
| brightness temperature | 25 | `def:b3:remote-sensing-gis:brightness` | new | checked: the physics books quote it once in a solution, never index it |
| normalised difference vegetation index | 25 | `def:b3:remote-sensing-gis:ndvi` | new |  |
| synthetic-aperture radar | 25 | `def:b3:remote-sensing-gis:sar` | new |  |
| radar backscatter | 25 | `def:b3:remote-sensing-gis:sar` | new |  |
| radar interferometry | 25 | `def:b3:remote-sensing-gis:insar` | new | OUTLINE says re-founds g9 but g9 never names it; Book 3 ch. 18 pointer |
| interferogram | 25 | `def:b3:remote-sensing-gis:insar` | new |  |
| line of sight (radar) | 25 | `def:b3:remote-sensing-gis:insar` | new |  |
| phase unwrapping | 25 | `def:b3:remote-sensing-gis:insar` | new |  |
| lidar | 25 | `def:b3:remote-sensing-gis:lidar` | new |  |
| raster data | 25 | `def:b3:remote-sensing-gis:data-models` | new | Book 3 owns digital elevation model |
| vector data (GIS) | 25 | `def:b3:remote-sensing-gis:data-models` | new | qualified |
| georeferencing | 25 | `def:b3:remote-sensing-gis:georef` | new |  |
| map algebra | 25 | `def:b3:remote-sensing-gis:map-algebra` | new |  |
| buffer (GIS) | 25 | `def:b3:remote-sensing-gis:operations` | new |  |
| overlay (GIS) | 25 | `def:b3:remote-sensing-gis:operations` | new |  |
| supervised classification | 25 | `def:b3:remote-sensing-gis:classification` | new |  |
| confusion matrix | 25 | `def:b3:remote-sensing-gis:classification` | new | checked: the math books never index it |

Unindexed statements of ch. 25: `prop:b3:remote-sensing-gis:planck-inversion`
(brightness temperature from a radiance), `prop:b3:remote-sensing-gis:mixed` (a mixed
pixel looks hotter than its mean), `prop:b3:remote-sensing-gis:azimuth` (azimuth
resolution of a SAR), `prop:b3:remote-sensing-gis:tof` (time of flight),
`thm:b3:remote-sensing-gis:fringe` (one fringe), `prop:b3:remote-sensing-gis:mogi-los`,
`met:b3:remote-sensing-gis:slope` (slope and aspect from a grid).

### Ch. 26 `planetary-interiors-surfaces`

| term | ch | label | status | note |
|---|---|---|---|---|
| Love number | 26 | `def:b3:planetary-interiors-surfaces:love-number` | new | Book 3 owns moment-of-inertia factor |
| tidal heating | 26 | `def:b3:planetary-interiors-surfaces:tidal-heating` | new |  |
| simple crater | 26 | `def:b3:planetary-interiors-surfaces:crater-morphology` | new |  |
| complex crater | 26 | `def:b3:planetary-interiors-surfaces:crater-morphology` | new |  |
| transient crater | 26 | `def:b3:planetary-interiors-surfaces:crater-morphology` | new |  |
| ejecta blanket | 26 | `def:b3:planetary-interiors-surfaces:crater-morphology` | new |  |
| crater size--frequency distribution | 26 | `def:b3:planetary-interiors-surfaces:sfd` | new |  |
| crater dating | 26 | `def:b3:planetary-interiors-surfaces:crater-dating` | new | OUTLINE Y3 |
| crater chronology function | 26 | `def:b3:planetary-interiors-surfaces:crater-dating` | new |  |
| crater production function | 26 | `def:b3:planetary-interiors-surfaces:crater-dating` | new |  |
| crater equilibrium density | 26 | `def:b3:planetary-interiors-surfaces:crater-dating` | new |  |
| resurfacing | 26 | `def:b3:planetary-interiors-surfaces:resurfacing` | new |  |
| stagnant lid | 26 | `def:b3:planetary-interiors-surfaces:stagnant-lid` | new |  |
| heat-pipe volcanism | 26 | `def:b3:planetary-interiors-surfaces:heat-pipe` | new |  |
| cryovolcanism | 26 | `def:b3:planetary-interiors-surfaces:cryovolcanism` | new |  |
| subsurface ocean | 26 | `def:b3:planetary-interiors-surfaces:ocean-world` | new |  |

Unindexed statements of ch. 26: `prop:b3:planetary-interiors-surfaces:kelvin` (Love
number of a uniform elastic sphere), `prop:b3:planetary-interiors-surfaces:scaling`
(gravity-regime crater scaling), `prop:b3:planetary-interiors-surfaces:poisson`
(counting error of a model age), `prop:b3:planetary-interiors-surfaces:tidal-power`.
The two-layer proposition is the Year 1 volume's (recalled).

### Ch. 27 `planetary-atmospheres`

| term | ch | label | status | note |
|---|---|---|---|---|
| exobase | 27 | `def:b3:planetary-atmospheres:exobase` | new | physics text mentions it, not indexed |
| Jeans escape | 27 | `def:b3:planetary-atmospheres:jeans-escape` | new | qualified: Book 4 owns Jeans criterion/mass/length |
| escape parameter | 27 | `def:b3:planetary-atmospheres:jeans-escape` | new |  |
| hydrodynamic escape | 27 | `def:b3:planetary-atmospheres:hydrodynamic` | new |  |
| non-thermal escape | 27 | `def:b3:planetary-atmospheres:hydrodynamic` | new |  |
| diffusion-limited escape | 27 | `def:b3:planetary-atmospheres:hydrodynamic` | new |  |
| radiative--convective equilibrium | 27 | `def:b3:planetary-atmospheres:rce` | new |  |
| runaway greenhouse | 27 | `def:b3:planetary-atmospheres:runaway` | new |  |
| moist greenhouse | 27 | `def:b3:planetary-atmospheres:runaway` | new |  |
| runaway greenhouse limit | 27 | `def:b3:planetary-atmospheres:runaway` | new |  |
| planetary habitability | 27 | `def:b3:planetary-atmospheres:habitability` | new | qualified: chemistry b1 indexes habitability; g10 owns habitable zone |
| exosphere | 27 | `def:b3:planetary-atmospheres:exobase` | new (added at writing) | not indexed elsewhere: checked |
| homopause | 27 | `def:b3:planetary-atmospheres:hydrodynamic` | new (added at writing) | not indexed elsewhere: checked |

Unindexed statements of ch. 27: `prop:b3:planetary-atmospheres:grey` (grey radiative
equilibrium, skin temperature emphasised, not indexed), `prop:b3:planetary-atmospheres:exobase`,
`thm:b3:planetary-atmospheres:jeans`, `prop:b3:planetary-atmospheres:diffusion`,
`prop:b3:planetary-atmospheres:limit`, `prop:b3:planetary-atmospheres:dh`. Recalled:
optical depth (Book 3 ch. 2), OLR and emission temperature (Book 3 ch. 27), moist adiabat
(Book 4 ch. 21), silicate-weathering thermostat (Book 4 ch. 26), Rayleigh distillation (ch. 14).

### Ch. 28 `exoplanets`

| term | ch | label | status | note |
|---|---|---|---|---|
| radial-velocity method | 28 | `def:b3:exoplanets:rv` | new | physics owns radial velocity, Doppler |
| minimum mass | 28 | `def:b3:exoplanets:rv` | new |  |
| transit method | 28 | `def:b3:exoplanets:transit` | new | OUTLINE Y3 |
| transit depth | 28 | `def:b3:exoplanets:transit` | new |  |
| impact parameter (transit) | 28 | `def:b3:exoplanets:transit` | new |  |
| limb darkening | 28 | `def:b3:exoplanets:limb` | new | check physics |
| direct imaging | 28 | `def:b3:exoplanets:imaging` | new |  |
| coronagraph | 28 | `def:b3:exoplanets:imaging` | new |  |
| gravitational microlensing | 28 | `def:b3:exoplanets:microlensing` | new |  |
| Einstein radius | 28 | `def:b3:exoplanets:microlensing` | new | check physics |
| transit-timing variation | 28 | `def:b3:exoplanets:ttv` | new |  |
| hot Jupiter | 28 | `def:b3:exoplanets:classes` | new |  |
| super-Earth | 28 | `def:b3:exoplanets:classes` | new |  |
| sub-Neptune | 28 | `def:b3:exoplanets:classes` | new |  |
| occurrence rate | 28 | `def:b3:exoplanets:occurrence` | new |  |
| radius valley | 28 | `def:b3:exoplanets:radius-valley` | new |  |
| mass--radius relation | 28 | `def:b3:exoplanets:mass-radius` | new |  |
| transmission spectroscopy | 28 | `def:b3:exoplanets:transmission` | new |  |
| secondary eclipse | 28 | `def:b3:exoplanets:transmission` | new |  |

Ch. 28 written 2026-10-23: all nineteen terms defined and indexed as planned (Einstein
radius and limb darkening checked: neither is indexed in the physics books; gravitational
lensing is not in the physics books at all, so the point-lens magnification is admitted
from general relativity). Unindexed statements: `thm:b3:exoplanets:semi-amplitude`,
`thm:b3:exoplanets:duration`, `prop:b3:exoplanets:depth`, `prop:b3:exoplanets:probability`,
`prop:b3:exoplanets:magnification` (admitted), `prop:b3:exoplanets:transmission`,
`prop:b3:exoplanets:eclipse`. Recalled: Doppler effect, radial velocity, spectroscopic
binary (physics g12), Kepler's laws and Planck's law (physics), scale height (physics),
exoplanet and habitable zone (g10), flux and luminosity (Book 3 ch. 2), equilibrium
temperature (Book 3 ch. 3), snow line (Book 4 ch. 2), hydrodynamic escape and the
habitable-zone limits (ch. 27).

### Ch. 29 `milky-way-galaxies`

| term | ch | label | status | note |
|---|---|---|---|---|
| Galactic disc | 29 | `def:b3:milky-way-galaxies:structure` | new | physics owns Milky Way |
| Galactic bulge | 29 | `def:b3:milky-way-galaxies:structure` | new |  |
| stellar halo | 29 | `def:b3:milky-way-galaxies:structure` | new |  |
| thick disc | 29 | `def:b3:milky-way-galaxies:structure` | new |  |
| stellar population | 29 | `def:b3:milky-way-galaxies:populations` | new |  |
| Galactic coordinates | 29 | `def:b3:milky-way-galaxies:coordinates` | new |  |
| local standard of rest | 29 | `def:b3:milky-way-galaxies:lsr` | new |  |
| 21-cm line | 29 | `def:b3:milky-way-galaxies:21cm` | new |  |
| rotation curve | 29 | `def:b3:milky-way-galaxies:rotation-curve` | new | OUTLINE Y3 |
| Oort constants | 29 | `def:b3:milky-way-galaxies:oort` | new |  |
| dark-matter halo | 29 | `def:b3:milky-way-galaxies:halo` | new | physics owns dark matter |
| Hubble sequence | 29 | `def:b3:milky-way-galaxies:types` | new |  |
| spiral galaxy | 29 | `def:b3:milky-way-galaxies:types` | new |  |
| elliptical galaxy | 29 | `def:b3:milky-way-galaxies:types` | new |  |
| lenticular galaxy | 29 | `def:b3:milky-way-galaxies:types` | new |  |
| irregular galaxy | 29 | `def:b3:milky-way-galaxies:types` | new |  |
| density-wave theory | 29 | `def:b3:milky-way-galaxies:density-wave` | new |  |
| supermassive black hole | 29 | `def:b3:milky-way-galaxies:smbh` | new | check physics |
| Cepheid variable | 29 | `def:b3:milky-way-galaxies:cepheid` | new |  |
| Leavitt law | 29 | `def:b3:milky-way-galaxies:cepheid` | new |  |
| standard candle | 29 | `def:b3:milky-way-galaxies:ladder` | new | physics text only, not indexed |
| distance ladder | 29 | `def:b3:milky-way-galaxies:ladder` | new | OUTLINE Y3 |
| tip of the red giant branch | 29 | `def:b3:milky-way-galaxies:trgb` | new |  |
| Tully--Fisher relation | 29 | `def:b3:milky-way-galaxies:tully-fisher` | new |  |
| Hubble tension | 29 | `def:b3:milky-way-galaxies:tension` | new |  |
| Local Group | 29 | `def:b3:milky-way-galaxies:groups` | new |  |
| galaxy cluster | 29 | `def:b3:milky-way-galaxies:groups` | new |  |

Ch. 29 written 2026-10-23: 26 of the 27 planned terms defined and indexed. '21-cm
line' dropped from the plan: the physics books index it (b3 ch. 12,
`ex:b3:spin-two-level:hyperfine`), so it is recalled. The Oort constants are defined in
`def:b3:milky-way-galaxies:rotation-curve` (no separate `:oort` label). Standard candle
defined here (physics uses it unindexed). Unindexed statements:
`thm:b3:milky-way-galaxies:oort`, `thm:b3:milky-way-galaxies:tangent`,
`prop:b3:milky-way-galaxies:models`, `thm:b3:milky-way-galaxies:enclosed`. Recalled:
Milky Way, Doppler effect, Kepler's laws, Newton's shell theorem, dark matter, black hole,
Schwarzschild radius, supernova, white dwarf, 21-cm line, Hubble's law (physics); annual
parallax, parsec, flux, luminosity, magnitudes, distance modulus, photometric band, colour
index (Book 3 ch. 2); interstellar medium (Book 4 ch. 1).

### Ch. 30 `origin-of-elements`

| term | ch | label | status | note |
|---|---|---|---|---|
| solar abundance | 30 | `def:b3:origin-of-elements:abundance` | new | Book 4 owns CI chondrite |
| dex | 30 | `def:b3:origin-of-elements:abundance` | new |  |
| metallicity | 30 | `def:b3:origin-of-elements:metallicity` | new |  |
| neutron capture | 30 | `def:b3:origin-of-elements:s-process` | new | check physics |
| s-process | 30 | `def:b3:origin-of-elements:s-process` | new | OUTLINE Y3 |
| r-process | 30 | `def:b3:origin-of-elements:s-process` | new | OUTLINE Y3 |
| sigma-N relation | 30 | `prop:b3:origin-of-elements:sigma-n` | new | indexed in its proposition |
| p-nuclei | 30 | `def:b3:origin-of-elements:p-process` | new |  |
| neutron-star merger | 30 | `def:b3:origin-of-elements:kilonova` | new | physics owns neutron star |
| kilonova | 30 | `def:b3:origin-of-elements:kilonova` | new |  |
| alpha element | 30 | `def:b3:origin-of-elements:alpha` | new |  |
| stellar yield | 30 | `def:b3:origin-of-elements:yield` | new |  |
| galactic chemical evolution | 30 | `def:b3:origin-of-elements:gce` | new | OUTLINE Y3 |
| closed-box model | 30 | `thm:b3:origin-of-elements:closed-box` | new | indexed in its theorem |
| G-dwarf problem | 30 | `def:b3:origin-of-elements:g-dwarf` | new | own label (plan said closed-box) |
| volatility trend | 30 | `def:b3:origin-of-elements:volatility` | new | Book 4 owns Goldschmidt classes, condensation temperature |

Ch. 30 written 2026-10-23: all 16 planned terms defined and indexed (solar abundance and
dex share `:abundance`; neutron capture, s process and r process share `:s-process`,
indexed as "s-process@s process" and "r-process@r process"; neutron-star merger and
kilonova share `:kilonova`). The G-dwarf problem has its own label
`def:b3:origin-of-elements:g-dwarf`, not the closed-box label of the plan. The sigma N
relation is indexed in `prop:b3:origin-of-elements:sigma-n` and the closed-box model in
`thm:b3:origin-of-elements:closed-box`. "Odd-even effect", "shielded", "s-only",
"branching" and "yield per stellar generation" are emphasised in the text, not indexed.
Recalled: Big Bang nucleosynthesis, binding energy per nucleon, valley of stability, beta
decay, half-life, cross-section, red giant, white dwarf, neutron star, supernova,
Chandrasekhar mass, gravitational waves (physics); CI chondrite, condensation
temperature, refractory and volatile elements, bulk silicate Earth (Year 2 volume);
thin and thick discs, halo (ch. 29).

### Ch. 31 `field-lab-methods-3`

| term | ch | label | status | note |
|---|---|---|---|---|
| relative gravimeter | 31 | `def:b3:field-lab-methods-3:gravimeter` | new |  |
| instrumental drift | 31 | `def:b3:field-lab-methods-3:gravimeter` | new |  |
| terrain correction | 31 | `def:b3:field-lab-methods-3:terrain` | new | Book 3 owns free-air and Bouguer corrections |
| total-field anomaly | 31 | `def:b3:field-lab-methods-3:magnetic` | new |  |
| diurnal correction | 31 | `def:b3:field-lab-methods-3:magnetic` | new |  |
| reduction to the pole | 31 | `def:b3:field-lab-methods-3:magnetic` | new |  |
| apparent resistivity | 31 | `def:b3:field-lab-methods-3:resistivity` | new | physics owns resistivity |
| electrode array | 31 | `def:b3:field-lab-methods-3:resistivity` | new |  |
| vertical electrical sounding | 31 | `def:b3:field-lab-methods-3:resistivity` | new |  |
| electrical resistivity tomography | 31 | `def:b3:field-lab-methods-3:resistivity` | new |  |
| Archie's law | 31 | `prop:b3:field-lab-methods-3:archie` | new | indexed in its proposition |
| ground-penetrating radar | 31 | `def:b3:field-lab-methods-3:gpr` | new |  |
| radargram | 31 | `def:b3:field-lab-methods-3:gpr` | new |  |
| misfit (data) | 31 | `def:b3:field-lab-methods-3:inversion-practice` | new |  |

Ch. 31 written 2026-10-23: all 14 planned terms defined and indexed on their planned
labels (relative gravimeter and instrumental drift share `:gravimeter`; total-field
anomaly, diurnal correction and reduction to the pole share `:magnetic`; apparent
resistivity, electrode array, vertical electrical sounding and electrical resistivity
tomography share `:resistivity`; ground-penetrating radar and radargram `:gpr`; misfit
(data) `:inversion-practice`); Archie's law indexed in `prop:b3:field-lab-methods-3:archie`.
Unindexed results with their own labels: `thm:...:sphere` (sphere and horizontal cylinder,
half-width rules), `prop:...:vcyl`, `prop:...:gauss` (excess mass from a map),
`prop:...:dyke`, `thm:...:point-source`, `prop:...:layers`, `prop:...:conductance`,
`prop:...:radar`, `prop:...:hyperbola`, `met:...:loop`, `met:...:budget`. "Base station",
"Wenner array", "Schlumberger array", "formation factor" and "Hammer chart" are emphasised
or named in the text, not indexed. Recalled: gravity anomaly, free-air and Bouguer
corrections, normal gravity (Year 1 volume); IGRF, inclination (ch. 4); resistivity,
relative permittivity, magnetisation, susceptibility, Gauss's theorem, skin depth
(physics); seismic refraction (ch. 2); weighted least squares (ch. 1); porosity (school
books), wireline logs (ch. 17).

## Re-founded and contested terms (Phase A report, item 2)

| term | where | other claimant | case |
|---|---|---|---|
| reference ellipsoid | ch. 3 (re-founded) | Book 2 g10 | Sync 1: "Y3 keeps the ellipsoid and J2"; Year 3 gives the ellipsoid as the hydrostatic figure with J2 and Somigliana. |
| phase rule | ch. 11 recalls; defines only "mineralogical phase rule" | chemistry b2 `thm:b2:equilibrium-shifts:phase-rule`, `def:b2:equilibrium-shifts:variance` | Sync 2 says "Y3 keeps the phase rule"; chemistry already owns it. Proposed amendment: Y3 recalls the phase rule and variance, and defines Goldschmidt's mineralogical form. |
| Rossby-wave dispersion relation | ch. 20 (prop., own name) | Book 4 ch. 22 "Rossby wave" | Sync 2: Y3 owns the dynamics; the term is recalled, the relation indexed under its own name. |
| Ekman solution (spiral) | ch. 21 theorem, not indexed | Book 3 ch. 29 owns Ekman layer/transport/spiral | Book 3 says "derived in the Year 3 volume": derived here without a second definition. |
| magnetostratigraphy, Darcy's law, Glen's flow law, radar interferometry | ch. 4, 23, 24, 25 (status new) | OUTLINE says "re-founds g11/g6/g8/g9" | The school text never names them (checked by grep of `parts/grade-*`): new, not re-founded. |
| Walther's law | ch. 17 (thm.) | Book 4 ch. 20 brief cites it, "re-check Book 3 owner" | Not in Book 3's map or Book 4's DEFINITIONS; it is the law of facies models (OUTLINE Y3 ch. 17). Book 4 to recall it in prose ("the Year 3 volume") or the sync moves it. |
| stereographic projection | ch. 8 | Book 3 ch. 18 says "the projections of the sphere are studied in the Year 2 volume" | OUTLINE puts it in Y3 `structural-analysis`; Book 3's own forward list says Y3: Book 3's sentence is the defect. |
| thermochronology (ch. 10) before fission-track and (U--Th)/He dating (ch. 13) | ch. 10 / ch. 13 | --- | Same-book order: ch. 10 defines thermochronology and uses the methods with `\cref{ch:b3:advanced-geochronology}`; ch. 13 defines the methods. |
| cosmogenic nuclide | ch. 13 | Book 3 ch. 20 proposition "Cosmogenic nuclides and erosion" | Book 3 does not index the term (checked); ch. 13 defines it and recalls Book 3's steady-erosion result. |
| shear zone | ch. 7 | Book 3 ch. 16--17 use it in prose ("studied in the Year 3 volume") | Not indexed in Book 3 (checked). |
| saturation index (of a mineral) | ch. 15 | chemistry "saturation state" | Qualified form; Ω recalled, SI = log Ω defined. |
| planetary habitability | ch. 27 | chemistry b1 indexes "habitability" (another sense) | Qualified form. |
| Jeans escape, escape parameter | ch. 27 | Book 4 ch. 1 Jeans criterion/mass/length | Never bare "Jeans". |
| standard candle | ch. 29 | physics b3 uses it in text only | Not indexed by physics (checked). |
| geobarometer, assimilation--fractional crystallisation | --- | Book 4 ch. 11, ch. 8 | Dropped from Book 5's list after the check: recalled. |

## Terms used but not defined here (Phase A report, item 3)

| term(s) | owner | used in ch. |
|---|---|---|
| P wave, S wave, elastic waves, Hooke's law, Young's modulus, Poisson's ratio, stress tensor, strain tensor, dilatation | physics b3 `continuum-elasticity` | 1, 2, 3, 7, 8 |
| dispersion relation, phase velocity, group velocity, normal modes | physics b2 | 1, 20, 21 |
| acoustic impedance, reflection coefficient, Fresnel coefficients | physics b2 | 2, 31 |
| gravitational potential energy, centrifugal force, Coriolis force, tides, Kepler's laws, escape velocity, angular momentum | physics b1/b2 | 3, 19, 21, 26, 27, 28 |
| hydrostatic relation, barometric formula, scale height, buoyancy, Archimedes | physics b1 `fluid-statics` | 6, 19, 27 |
| vorticity, circulation (of velocity), Navier--Stokes, continuity equation, Reynolds number, viscosity, Stokes' law, Poiseuille flow | physics b2 | 6, 19, 20, 21, 23 |
| diffusion equation, thermal conductivity and diffusivity | physics b2 | 5, 18, 23 |
| black body, effective temperature, emissivity, greenhouse effect, Planck's law, reflectance | physics b2/g10 | 22, 25, 27 |
| remanence, Curie temperature, magnetic domain, hysteresis, magnetic dipole, magnetic declination | physics b3/b1/g11 | 4, 31 |
| resistivity, relative permittivity | physics b2/b3 | 31 |
| Doppler effect, radial velocity, redshift, spectroscopic binary | physics g12 | 28, 29 |
| Milky Way, light-year | physics g5/g8 | 29 |
| Hubble's law, dark matter, CMB, black hole, supernova, white dwarf, neutron star, main sequence, HR diagram, stellar and Big Bang nucleosynthesis | physics b3 | 29, 30 |
| binding energy, iron peak, valley of stability, beta decay, half-life | physics b3/g12 | 13, 30 |
| Fourier series and coefficients, Fourier transform, convolution | math b2/b3 | 2, 5, 16 |
| least squares, regression line, covariance, variance, standard deviation, Gaussian law, weighted mean | math b1/g8 | 1, 4, 13, 31 |
| Gibbs energy, chemical potential, activity, activity coefficient, ionic strength, equilibrium constant, variance and phase rule, miscibility gap, lever rule, binary diagrams, Henry's law | chemistry b1/b2 | 11, 15 |
| solubility product, alkalinity, chemical speciation, saturation state | chemistry b1/b3 | 15 |
| rate law, transition state, Arrhenius law, activation energy | chemistry b1/b3 | 7, 15, 24 |
| δ value, fractionation factor, equilibrium and kinetic isotope effects | chemistry b3 (Sync 2) | 14, 27 |
| point defect; uncertainty, standard deviation of the mean, confidence interval | chemistry b3; chemistry b1/b2 | 7; 13, 31 |
| sulfate reduction, photosynthesis | biology | 14 |
| porosity, permeability, aquifer, water table, groundwater, spring, well | Book 1 g6 | 17, 23 |
| glacier, ice sheet, ice shelf, sea ice, permafrost, iceberg, gyre | Book 1 g8 | 3, 21, 24 |
| map projection, equal-area projection (map), remote sensing, satellite image, satellite positioning, landforms, uplift--erosion balance | Book 1 g9 | 8, 18, 25 |
| meander, delta, weathering, erosion | Book 1 g5 | 17, 18 |
| geodesy, flattening, habitable zone, exoplanet, albedo, mixed layer, thermocline, upwelling, residence time, fossil groundwater | Book 2 g10 | 3, 21, 22, 23, 27, 28 |
| epicentral distance, travel time, travel-time curve, shadow zone, magnetic reversal, normal and reversed polarity, ridge push, slab pull, hydrothermal circulation, migration (of oil and gas) | Book 2 g11 | 1, 2, 4, 6, 15 |
| mantle convection, thermal convection, isostatic rebound, radiative forcing, shortening | Book 2 g12 | 6, 10, 18, 22 |
| celestial coordinates, great/small circle, spherical triangle, declination (celestial), annual parallax, parsec, luminosity, flux, magnitudes, distance modulus, atmospheric window, photometric band | Book 3 ch. 1--2 | 4, 8, 25, 28, 29 |
| moment-of-inertia factor, Bond albedo, equilibrium temperature, terrestrial/giant planet | Book 3 ch. 3 | 26, 27, 28 |
| digital elevation model, strike, dip, attitude, fold, anticline, syncline, fold axis; trend, plunge, mean orientation, thin section; borehole log, unconformity, cross-section | Book 3 ch. 4--6 | 8, 17, 18, 25 |
| solid solution (mineral), end-member, mineral groups | Book 3 ch. 7 | 11 |
| reference Earth model, head wave, crossover distance, LVZ, lithosphere, asthenosphere, transition zone, Adams--Williamson | Book 3 ch. 9 | 1, 2, 5, 6 |
| heat flow, heat production, geotherm, mantle adiabat, thermal boundary layer, thermal lithosphere | Book 3 ch. 10 | 5, 6, 10 |
| normal gravity, isostasy, Airy, Pratt, gravity anomaly, free-air and Bouguer corrections/anomalies, geoid, geoid height | Book 3 ch. 11 | 3, 6, 31 |
| Euler pole, finite rotation, marine magnetic anomaly, polarity chron, GPTS | Book 3 ch. 12 | 4 |
| graben, half-graben, continental rift, passive margin, oceanic crust, depth--age law, transform fault | Book 3 ch. 13 | 5, 9 |
| subducting slab, Wadati--Benioff zone, accretionary prism, volcanic arc; hotspot, mantle plume, hotspot track, LIP | Book 3 ch. 14--15 | 1, 4, 6, 10, 26 |
| traction, normal and shear stress, principal stresses, lithostatic and pore-fluid pressure, effective stress, strain ellipse, pure/simple shear, Coulomb, Byerlee, strength envelope, BDT | Book 3 ch. 16 | 7, 8, 9, 10 |
| fault types, dextral, sinistral, mylonite, Anderson, fold elements, foliation, schistosity, cleavage, lineation, vergence | Book 3 ch. 17 | 7, 8, 9, 10 |
| seismic moment, focal mechanism, P and T axes, nodal plane | Book 3 ch. 18 | 8 |
| weathering terms, clay minerals, kaolinite; settling velocity, Shields, denudation rate | Book 3 ch. 19--20 | 15, 18 |
| sedimentary facies, depositional environment, bedforms, deltas, turbidite; carbonate factory, reef, platform, lysocline, CCD, evaporite; diagenesis, subsidence, accommodation, eustasy, relative sea level; lithostratigraphy, GSSP | Book 3 ch. 21--24 (planned) | 2, 15, 16, 17 |
| parent isotope, radiogenic daughter, isochron, initial ratio, branching decay, closure temperature, cooling age, radiocarbon | Book 3 ch. 25 (planned) | 10, 13 |
| standard atmosphere, lapse rates, potential temperature, static stability, stratification, thermocline, EOS of seawater, water mass; OLR, meridional heat transport | Book 3 ch. 26--27 (planned) | 19, 21, 22 |
| PGF, Coriolis parameter, geostrophic wind/balance, Hadley/Ferrel/polar cells, jets, ITCZ; wind stress, gyres, Ekman layer/transport/spiral, upwelling, western boundary current, MOC, THC, sverdrup | Book 3 ch. 28--29 (planned) | 19, 20, 21 |
| ISM, molecular cloud, Jeans criterion/mass/length, protoplanetary disc, condensation temperature/sequence, snow line, chondrite, CI chondrite | Book 4 ch. 1--3 | 27, 29, 30 |
| partition coefficient, bulk D, compatible/incompatible, MORB, OIB, normalised diagram, europium anomaly; CHUR, epsilon, depleted mantle, VSMOW/VPDB, meteoric water line | Book 4 ch. 3--4 | 12, 13, 14 |
| Mogi source; partial melting, melt fraction, ternary diagram, cotectic; Rayleigh fractionation law, equilibrium/fractional crystallisation, AFC, Bowen's series | Book 4 ch. 6--8 | 11, 12, 25 |
| metamorphic facies, univariant reaction, invariant point, Clapeyron slope, geothermometer, geobarometer, P--T--t path, exhumation, exhumation rate | Book 4 ch. 10--11 | 9, 10, 11 |
| balanced cross-section, décollement, thin/thick-skinned, fold--thrust belt, foreland basin, nappe; stretching model, post-rift subsidence, thermal time constant, backstripping | Book 4 ch. 13--16 | 3, 5, 8, 9, 10 |
| marine transgression/regression, first-order cycle; ice--albedo feedback, snowball Earth, GOE | Book 4 ch. 18--19 | 14, 16, 22 |
| Rossby wave, extratropical cyclone, NWP, data assimilation, ensemble forecast; ENSO; climate proxy, ice-volume effect, Mg/Ca, age model; Milankovitch; PETM, carbon cycle | Book 4 ch. 22--26 | 14, 16, 20, 21, 22 |
| ERF, feedback parameter, Planck response, ECS, TCR, TCRE, sea-level budget, thermosteric | Book 4 ch. 27 | 22, 24 |
| TIMS, MC-ICP-MS, isotope dilution, mass bias, XRF, microprobe | Book 4 ch. 31 | 13, 31 |

## Homographs: always the qualified form

| bare word | owner of the bare word | this book writes |
|---|---|---|
| fold | Book 3 (structure) | fold (of seismic coverage) |
| migration | Book 2 (oil and gas), chemistry (electrode) | seismic migration |
| equal-area projection | Book 1 g9 (maps) | equal-area projection (of the sphere) |
| pole | g3 (geographic), physics (magnet), math | pole (to a plane); virtual geomagnetic pole |
| inclination | physics (optics) | magnetic inclination |
| retardation | Book 3 ch. 8 (optics) | retardation factor (sorption) |
| permeability | g6 (rock), physics (magnetic) | intrinsic permeability |
| buffer | biology / chemistry | buffer (GIS) |
| habitability | chemistry b1 | planetary habitability |
| underplating | Book 4 (mafic) | tectonic underplating |
| exsolution | Book 4 (volatile exsolution) | exsolution (mineral) |
| recovery | biology | recovery (crystal plasticity) |
| turning point | physics (energy) | turning point (of a seismic ray) |
| accommodation zone | Book 3 accommodation | transfer zone |
| Jeans | Book 4 (Jeans criterion) | Jeans escape |
| Kelvin wave | (none yet) | Kelvin wave (oceanic) |
| boundary layer, circulation, tides | physics | thermal boundary layer (Book 3), Munk boundary layer, "circulation (of velocity)" only as physics', tides recalled |
