# FIGCHECK --- Book 5 (University Year 3)

One row per figure object, each checked on its own page rendered at 130 dpi
(`pdftoppm -r 130 -f P -l P -singlefile`), never from a contact sheet. `page`
is the PDF page of the English build at the time of the check.

| ch | figure | page | layout | science | note |
|---|---|---|---|---|---|
| 1 | fig:b3:seismology-imaging:shells | 10 | fixed | fixed | first draft: angle pics drawn reflex (full circles), move-to O inflated the bbox (half-page gap); ray now computed by Snell's law through 3 shells (calc/shells_fig.py), label moved off the ray |
| 1 | fig:b3:seismology-imaging:rays | 12 | fixed | ok | core labels moved off the boundaries (leader line for the inner core); shadow arc 98.5-143.8 deg matches values table |
| 1 | fig:b3:seismology-imaging:tt | 13 | fixed | fixed | S branch first included ScS (S stopped at the CMB counted as mantle): branch_of now labels those 'cmb' and a test guards it; caption rewritten for the lid/LVZ branch to 39 deg and the 220-km reflections; legend moved off the S curve; figure moved after the ak135 paragraph to remove a half-page gap |
| 1 | fig:b3:seismology-imaging:particle-motion | 14 | ok | ok | Rayleigh top-of-ellipse arrows point backwards (retrograde) for propagation to the right; Love arrows transverse |
| 1 | fig:b3:seismology-imaging:love | 15 | fixed | ok | beta labels moved off the curves, legend moved; c -> beta1 at short and beta2 at long periods, U < c, Airy minimum 3.384 at 19.2 s as in values |
| 1 | fig:b3:seismology-imaging:inverse-loop | 18 | ok | ok | |
| 1 | fig:b3:seismology-imaging:checkerboard | 20 | fixed | fixed | caption claimed vertical smearing; grid compared numerically with the truth (corr 0.95 at eps 60): amplitude loss at the side edges, caption corrected; sources/stations now plotted from tables |
| 1 | fig:b3:seismology-imaging:tradeoff | 20 | fixed | fixed | axes relabelled with the script's real units (s, per cent); eps 3 and 60 marked from the values table (first draft marked eps 40); labels moved off the curve |
| 1 | images/book5/ai/b3-seismic-vault.jpg | 21 | ok | ok | AI image reviewed: buried vault, sensor on pier, solar mast; generic, no text or logos |
| 2 | fig:b3:exploration-seismology:refraction | 26 | fixed | ok | legend covered the E head wave at x=0 and the W/E corner labels sat on the axis: ymax raised to 660, corner labels removed, reciprocal-time label moved above the dots; branches start at the computed critical distances (493 m, 300 m), both end at 486.1 ms |
| 2 | fig:b3:exploration-seismology:synthetic | 28 | ok | fixed | the reflectivity stems were drawn vertically from t=0 (ycomb): changed to xcomb, stems now point right for +R; checked at 300 dpi that all four are red (130-dpi rendering thinned one); trace polarity matches R signs |
| 2 | fig:b3:exploration-seismology:wedge | 29 | ok | fixed | normalised by 2R in the script, which put thick beds at 0.5: plotted 2*amp against "peak amplitude / R" (thick beds 1, tuning 1.45 at 19.5 m); caption reworded |
| 2 | fig:b3:exploration-seismology:fresnel | 29 | fixed | ok | the arc label and r_F arrow overlapped the dashed arc: label removed (arc explained in caption), r_F arrow moved below the reflector with extension lines; move-to bbox trap avoided (arc from a polar start point) |
| 2 | fig:b3:exploration-seismology:cmp | 30 | ok | ok | four pairs symmetric about the midpoint, single reflection point; foreach variables renamed from \d/\c (LaTeX accent commands) |
| 2 | fig:b3:exploration-seismology:gather | 32 | ok | ok | four reflections, the chalk-shale one faint as R=0.028 says; NMO panel flat to ~1 km, stretch beyond; caption adds the mute |
| 2 | fig:b3:exploration-seismology:velocities | 32 | fixed | ok | legend covered the 4500 m/s step, then the RMS curve: moved below the axis in two columns; first layer's step drawn from 0.4 s; Dix points within 1.5 % of the model |
| 2 | images/book5/ai/b3-vibroseis.jpg | 33 | ok | ok | AI image reviewed: three vibrator trucks in convoy, geophone cable on the ground; generic, no text or logos |
| 2 | fig:b3:exploration-seismology:migration | 34 | fixed | fixed | migration arrow first pointed down-dip to the reflector end: retargeted to the foot of the normal from the rightmost recording point (4.13,-3.39); labels moved off the reflector and arrow; apparent dip 29.8 deg = atan(sin 35 deg) |
| 2 | fig:b3:exploration-seismology:terminations | 34 | ok | ok | truncation, onlap, toplap/downlap each against the coloured surface |
| 2 | images/book5/ai/b3-streamer-vessel.jpg (inthefield) | 35 | ok | ok | AI image reviewed: survey vessel towing parallel streamers with tail buoys; generic, no text or logos |
| 3 | fig:b3:gravity-geodesy:equipotential | 40 | fixed | fixed | first draft: arbitrary arrow lengths, gravity not the vector sum, labels overlapping; now attraction (to the centre), centrifugal (horizontal) and their sum drawn along the inward normal of the ellipse, lengths solved in calc/ch03_fig.py; labels separated |
| 3 | fig:b3:gravity-geodesy:hydrostatic | 42 | fixed | ok | curve clipped at MoI 0.30 (1/f = 335 > ymax 330): ymax 340; Earth point 0.3308 -> 1/f 299.9, observed 298.26, uniform 231.9 = 1/(1.25 m) |
| 3 | fig:b3:gravity-geodesy:grace | 44 | fixed | fixed | first draft put the mass excess under the satellites, so the leading one was pulled backward: mass moved ahead of the leading satellite, which is now pulled forward (JPL principle, geod5:grace) |
| 3 | images/book5/b3-grace-fo-concept.jpg | 44 | ok | ok | NASA/JPL artist's concept PIA22441, PD verified by Commons API; caption says the separation is shortened and the beam stands for the laser link |
| 3 | fig:b3:gravity-geodesy:ice-mass | 45 | ok | ok | IMBIE 2021 monthly cumulative, 1-sigma bands; end values -4892/-2671 Gt and trends match ice_mass-values; GRACE window marked |
| 3 | fig:b3:gravity-geodesy:flexure | 47 | fixed | ok | forebulge and outer-rise labels clipped by ymax: ymax raised (700 and 280); legend colours checked at 300 dpi; Te 10/25/40 bulges at 112/222/316 km, broken-plate rise 67 m at 167 km as in flexure-values |
| 3 | fig:b3:gravity-geodesy:moat | 48 | fixed | ok | forebulge barely visible: raised in the schematic, Moho kept parallel |
| 3 | images/book5/ai/b3-gravimeter.jpg (inthefield) | 48 | ok | ok | AI image reviewed: geophysicist with notebook, box gravimeter on a levelling base, GNSS antenna on a pole; generic, no text or logos |
| 4 | fig:b3:palaeomagnetism:elements | 54 | fixed | ok | first draft carried two empty draw commands and a D arc to 12.2 deg while H lies at 9.46 deg in the oblique frame: arc set to the H direction, H label moved off the dashed construction line; F = H + Z checked on the dashed box |
| 4 | fig:b3:palaeomagnetism:igrf-maps | 55 | fixed | ok | contour labels first printed as text (no thin space, hyphen minus): numeric meta now (55 000, -20); panel gap raised (titles touched the tick labels); dip equator 11.3 S-12.1 N and Fmin 27 S 60 W, Fmax 59 S 134 E as in igrf_field-values; plate carree on the shared land file (not Mollweide: the land file is lon/lat) |
| 4 | fig:b3:palaeomagnetism:dipole | 56 | ok | ok | moment 8.32 -> 7.69 e22 A m2 and pole latitude 78.61 -> 80.79 N match igrf_field-values; 26 epochs every 5 yr |
| 4 | fig:b3:palaeomagnetism:zijderveld | 58 | fixed | ok | legend first hid the 20 C end of the vertical projection, then the horizontal one: moved to the empty lower-left; 580 label clipped (clip=false); N label of the stereonet clipped (clip=false); horizontal steps 20-300 C at constant E (overprint has no east component), both projections straight to the origin above 300 C; site-A dots, mean star (34.2, 37.2) and a95 9.0 deg circle from palaeomag_stats |
| 4 | fig:b3:palaeomagnetism:vgp | 59 | fixed | ok | the D mark was an arrow crossing its own label: plain arc; sides labelled 90-lambda_s, 90-lambda_p, p; angle beta at N, D at S, as in the theorem |
| 4 | fig:b3:palaeomagnetism:apw | 60 | fixed | ok | Kesta labels overlapped the 120 E meridian label and the Kesta series was the same blue as the reference: Kesta in red, labels moved east of the triangles; poles (A 51.9 N 136.6 E, B 66.5 N, C 87.1 N) and reference path match the problem; outer circle 45 N (r = 0.5412) |
| 4 | fig:b3:palaeomagnetism:magstrat | 61 | fixed | ok | timescale first drawn at 1.6 cm/Myr, chron labels on top of the tick labels and the rotated axis title: 4.2 cm/Myr, labels moved right, title merged into the header; tick labels zero-filled (3.0); tie lines join 4.2/14.8/19.7/24.6/29.2/54.0 m to 3.596/3.330/3.207/3.116/3.032/2.581 Ma as printed in the problem |
| 4 | images/book5/ai/b3-palaeomag-lab.jpg (inthelab) | 62 | ok | ok | AI image reviewed: specimen tray, long sample-handler track into a horizontal magnetometer, shielded metal-walled room; generic, no text or logos |
| 5 | fig:b3:lithosphere-thermal-models:columns | 68 | fixed | ok | 'cooled plate rho_m(1 + alpha dT)' overflowed the column: right column widened to 2.2 cm; equal-mass columns above a common compensation depth, d(t) > d_r |
| 5 | fig:b3:lithosphere-thermal-models:isotherms | 70 | fixed | ok | xlabel of (a) collided with the title of (b): sep 2.3 cm; legend moved to the empty lower left; 'base of the plate' label first sat on the 1400 C lines, moved to the free band t 48-90 Myr; hs and plate isotherms coincide young, plate flattens above 95 km; heat flow levels at 47.3 mW/m2 (plate_cooling-values) |
| 5 | fig:b3:lithosphere-thermal-models:depth-age | 71 | ok | ok | 36 bins of 5 Myr (n >= 63 each), medians 3051 m (0-5) to 5081 m (90-95) as in plate_cooling-values; legend below the axis; caption states no correction |
| 5 | fig:b3:lithosphere-thermal-models:geotherms | 72 | fixed | ok | two blues for 40 and 60 mW/m2: 40 now black; 1300 C crossings at 129/84/61 km as in continental_geotherm-values; legend clear of the curves |
| 5 | images/book5/ai/b3-heatflow-probe.jpg (inthefield) | 73 | ok | ok | AI image (batch 2) reviewed: weighted lance with a side sensor tube hanging from the stern A-frame, two crew with ropes, winch drum; generic, no text or logos |
| 6 | fig:b3:mantle-convection:cell | 77 | fixed | ok | first draft's circulation arrows did not match the up/downwellings: redrawn as four cells alternating in sense (counter-clockwise left of each upwelling), hot rising at 1/4 and 3/4, cold sinking at mid-width; delta marks moved outside the box off the cells |
| 6 | fig:b3:mantle-convection:scaling | 79 | fixed | ok | 'conduction' clipped by the axis and on Ra_c: moved; the law was drawn from Ra_c where it gives Nu = 0.4 (a false jump): now from 16 Ra_c (Nu = 1), caption says so; title of (b) collided with xlabel of (a): sep 2.5 cm; mantle band 4.9e6-4.9e7 and plate band 1.06-7.46 cm/yr from convection_scaling-values/plates; u = 1.21 cm/yr at 4.9e7 |
| 6 | fig:b3:mantle-convection:forces | 80 | fixed | ok | ridge-push arrow crossed the plate edge with its label on the outline: arrow inside the young plate, label in the water; overriding plate was the mantle's colour: grey, mantle filled; slab resistance moved to the slab's underside; plate motion right, basal drag left, slab pull down-dip |
| 6 | fig:b3:mantle-convection:ridge-push | 81 | fixed | ok | legend centred: left-aligned; half-space linear to 6.1e12 at 160 Myr, plate levels at 2.26e12 (ridge_push-values 2.11e12 at 100, 2.26e12 at 160); hs at 100 Myr 3.82e12 as in the text |
| 6 | fig:b3:mantle-convection:plume | 82 | fixed | ok | 'plate motion' sat on the topography line: moved into the lithosphere band; 'tail' labels on the arrows: set beside; 'mantle' and the basal-layer label crossed the right tail: moved, basal layer drawn as a band; 'Not to scale' in caption |
| 6 | fig:b3:mantle-convection:gia | 83 | fixed | ok | title of (b) collided with xlabel of (a): sep 2.5 cm; tau at 3000 km = 0.41/4.1/41 kyr as in gia_relaxation-values (curves at e^-1 at those times); (b) slopes -1 in log-log |
| 6 | images/book5/b3-raised-beach-malin.jpg (inthefield) | 84 | ok | ok | Commons photo, CC BY-SA 4.0, credit in caption and front matter; shingle ridges and green raised platforms above the shore, no people or text; caption follows the file description (raised beaches from isostatic rebound) |
| 7 | fig:b3:deformation-mechanisms:dislocation | 89 | fixed | ok | first draft did not show an extra half-plane (11 columns above and 11 below): redrawn with 10 columns below and 11 squeezed above, the red half-plane ending on the slip plane at the core symbol; panel (b) upper half shifted one spacing right with b marked at the step, consistent with tau top-right; 'slip plane' label moved off the atoms |
| 7 | fig:b3:deformation-mechanisms:diffusion | 90 | fixed | ok | lattice paths first went top-to-right and bottom-to-left only: now from both compressed faces to both free faces; boundary paths along the faces; sigma vertical, extension horizontal |
| 7 | fig:b3:deformation-mechanisms:flow-laws | 91 | fixed | ok | legends hung far below the panels: moved inside lower right; slopes 4 and 3.5 (straight lines on log-linear axes with log stress); 1e-14 line crosses quartz 400 C at 65 MPa and olivine 1100 C at 3 MPa as in flow_laws-values |
| 7 | fig:b3:deformation-mechanisms:map | 92 | fixed | ok | 'diffusion creep' label sat on a contour: moved to the empty lower right; contour labels moved off the boundary; 1e-10 label clipped at the frame: moved left; boundary 5.0 MPa at 1 mm and 79 MPa at 100 um as in flow_laws-values, slope -1.2 |
| 7 | fig:b3:deformation-mechanisms:kinematic | 93 | ok | ok | all three panels dextral (top to the right): S leaning '/' towards stretching between horizontal C; sigma-clast tails leave the upper side to the right and the lower side to the left without crossing the centre line; mica fish leans like S with stepped tails |
| 7 | images/book5/ai/b3-deformation-press.jpg (inthelab) | 94 | ok | ok | AI image (batch 1) reviewed: four-column press with a large pressure vessel, hydraulic gauges and lines, technician holding a foil-wrapped jacketed sample assembly; generic, no text or logos |
| 7 | images/book5/b3-augen-mylonite.jpg (inthelab) | 94 | ok | ok | Commons photo CC BY-SA 4.0 (Mikenorton): sawn augen mylonite, large pink K-feldspar porphyroclasts with dark mica-rich foliation wrapping them; credit in caption and front matter |
| 8 | fig:b3:structural-analysis:geometry | 99 | ok | ok | (a) Z, O, nadir, P at theta 60 from the nadir; ZP crosses the plane at r = 2 tan 30 = 1.155 cm; theta/2 marked at Z; (b) chord from the nadir to P swung about the nadir onto the tangent plane at 2R sin 30 = 2 cm; labels clear |
| 8 | fig:b3:structural-analysis:nets | 100 | ok | ok | Wulff and Schmidt nets from stereonet.py: great circles of N-S striking planes every 10 deg meet at N and S; small circles about the N-S axis; Wulff small circles are circles, Schmidt ones ovals; primitive and E-W diameter drawn |
| 8 | fig:b3:structural-analysis:pi | 102 | fixed | ok | poles of the east limb plot west of the centre and vice versa (labels say so); girdle E-W through both clusters; beta triangle on the primitive at N (359.6/1.9); mean-limb great circles hug the primitive and meet at beta; zoom box in (a) matches panel (b) range; labels moved closer to the clusters |
| 8 | fig:b3:structural-analysis:fry | 103 | fixed | ok | (a) frame clipped the right-most centres: limits widened to +-10; (b) Fry void elliptical, long axis at 30 deg; red fit through the inner edge, ratio 1.89, angle 30.4 as in fry-values |
| 8 | fig:b3:structural-analysis:flinn | 103 | fixed | ok | b-axis label collided with the tick 4: moved right of the arrow; double-ellipse pancake replaced by one oblate outline; cigar in k > 1 field (a 2.9, b 1.6), pancake in k < 1 field |
| 8 | fig:b3:structural-analysis:faults | 105 | ok | ok | five great circles; main fault 120/60 slip point at trend 120, r 0.37 (down-dip); sigma1 square at the centre, sigma2 diamonds at 030/210, sigma3 triangles at 120/300 on the primitive |
| 8 | fig:b3:structural-analysis:restoration | 106 | fixed | ok | first draft (limbs 25 deg) did not balance (weak layer 9.0 vs 3.3 in area): redrawn to balance with limbs 50 deg, h = A/S = 2.14, weak-layer area 9.61 in both panels, competent layers 0.3 thick (0.47 vertically on the limbs); A label moved off the axial trace; pin labels off the layer corners |
| 8 | images/book5/ai/b3-compass-clinometer.jpg (inthefield) | 107 | ok | ok | AI image (batch 1) reviewed: hand pressing an open compass-clinometer on an inclined grey rock face, notebook and pencil beside; generic, no text, no place, no hammer |
| 9 | fig:b3:extension-strike-slip:models | 112 | fixed | ok | (a) faults first drawn in the air above the rift floor: now the two border faults from the shoulders down; crust and mantle thin symmetrically; (b) the mantle notch under the breakaway was left white: filled; arrow removed; shear zone from the breakaway through the lithosphere, crust thinned near its trace, mantle thinned under the upper plate, flank bulge labelled |
| 9 | fig:b3:extension-strike-slip:domino | 113 | fixed | ok | (a) beta = sin theta0 / sin theta, 1 at theta = theta0, 1.73 at 60->30 as in domino_extension-values; (b) y ticks were 10^0.5 etc.: fixed-point ticks 1-40; minima 3.12 at 60.5 deg and 4.68 at 65.2 deg; curves diverge at the lock-up dips 31 and 40 deg |
| 9 | fig:b3:extension-strike-slip:rollover | 114 | fixed | ok | legend sat on the deeper bed: moved between the bed and the detachment; 'half-graben' label sat on the fault: moved into the sag; fault dips 60 at the surface, flat at 5 km; sag areas 10 and 6 km2 as in rollover-values |
| 9 | fig:b3:extension-strike-slip:core | 115 | fixed | ok | upper-plate blocks crossed the detachment: blocks drawn first, footwall over them; dome, mylonite carapace, rolling hinge, isostatic rise and opposite transport arrows |
| 9 | fig:b3:extension-strike-slip:strike-slip | 116 | fixed | ok | (b) step labels ran into panel (c): shortened; dextral: sigma1 NW-SE (135 deg), R at -15 deg, P at +15 deg, R' at 105 deg, T parallel to sigma1; right step releasing (basin), left step restraining (ridge); positive flower under a ridge, negative under a sag |
| 9 | images/book5/b3-basin-and-range.jpg (inthefield) | 117 | ok | ok | Commons photo CC BY-SA 2.0 (Ken Lund): hazy aerial view of parallel ranges and alluvial basins south of Death Valley; caption follows the Commons description; credit in caption and front matter |
| 10 | fig:b3:orogenic-wedges:thrusts | 113 | fixed | ok | first a 3-panel figure that could not break and left half a page blank: duplex split off; panel heights cut to the data; (a) labels boxed off the bed lines; (b) 'excess area' label clipped by the panel title: moved right with a leader; footwall label between two beds; fault-parallel flow from fault_bend.py: back limb 30 deg, crest lifted by r = 1, excess area S r = 2.5 (tested) |
| 10 | fig:b3:orogenic-wedges:duplex | 114 | fixed | ok | 'horse' label sat on an imbricate: moved below the floor with a leader; four horses between floor and roof, frontal ramp, uncut footwall ahead, cover folded over the rear ramp; transport arrow inside the cover |
| 10 | fig:b3:orogenic-wedges:wedge | 114 | fixed | ok | 'wedge' label collided with F(x+dx), sigma_n label on the slice line, alpha/beta arcs crowded F(x): arcs shrunk, labels moved; base 6 deg, surface 8 deg (exaggerated); friction on the wedge towards the hinterland, normal stress leaning towards the hinterland, F(x) pushing towards the hinterland, F(x+dx) towards the toe |
| 10 | fig:b3:orogenic-wedges:taper | 115 | fixed | ok | 'supercritical' label sat on the 12-13 deg band: moved; alpha at beta = 0: 7.22, 5.79, 3.23 deg as in critical_taper-values; the three lines meet alpha = 0 at beta* = mu_b/K = 9.59 deg (exercise 10); bands alpha = T - beta clipped at 0 |
| 10 | images/book5/ai/b3-sandbox-lab.jpg (inthelab) | 117 | ok | ok | AI image (batch 1) reviewed: scientist at a glass-sided sand box with flat coloured layers, motor-driven wall at the left, camera on a tripod; generic, no text, no brand; caption says 'before shortening' |
| 10 | fig:b3:orogenic-wedges:age-elevation | 118 | fixed | ok | (a) legend sat on the 3 mm/yr curve: legend dropped, styles taken from (b); (b) legend over the isotherms: ymin lowered to -3.3, legend in the empty band; slopes 0.59, 2.5, 13.9 mm/yr = v/(1-f) as in age_elevation-values; 65 C isotherm at -1.61, -1.21, -0.62 km mean depth; figure moved before the deflection paragraph so it no longer left a half page blank |
| 11 | fig:b3:petrological-thermodynamics:gasp | 124 | ok | ok | three GASP lines: experimental 22.80 T - 1093 (red, extrapolated below 900 C), tables with constant dH/dS/dV (dashed, slope 19.8 bar/K) and tables with heat capacities at 100 K steps (dots, within 0.12 kbar of the dashed line); experimental line 0.9 and 1.9 kbar above the tables at 627 and 927 C as in gasp_tables-values; shaded box = the experimental range 900-1250 C; field labels clear of the lines; legend clear of the data |
| 11 | fig:b3:petrological-thermodynamics:bundle | 126 | fixed | ok | two sector labels (A+B/B+D, A+C/C+D) were crossed by the metastable extensions: moved left of the dashed lines; four rays from schreinemakers.py, each stable on one side only; every metastable extension lies in a sector where its omitted phase is stable (B ext. in ABD, C ext. in ACD, A and D ext. in AD); no sector over 180 deg; reactions in the caption balance (exercise 7); figure could not fit on p. 125 and left about a quarter page blank there (accepted) |
| 11 | fig:b3:petrological-thermodynamics:solvus | 127 | ok | ok | (a) G_mix at 1500, Tc = 1203 and 900 K, common tangent at x = 0.111/0.889 at -0.635 kJ/mol (exercise 6); (b) binodal and spinodal meet at Tc = 1203 K, x = 0.5; X0 = 0.3 line crosses the solvus at 1136 K and the spinodal at 1010 K (exercise 10); dashed isopleths on the solvus limbs; labels and legends clear |
| 11 | images/book5/ai/b3-petrology-desk.jpg (inthelab) | 128 | ok | ok | AI image reviewed: petrologist at a polarising microscope, a wooden box of thin sections, a monitor showing a thin section in cross-polarised light, a hand specimen; generic, no text, no brand, no unsafe practice; caption matches |
| 12 | fig:b3:trace-element-modelling:curves | 134 | fixed | ok | ticks printed as 5x10^-2 and 10^k: fixed decimal ticks; figure moved before the aggregated-melt definition (it left 40 % of p. 134 blank), text now points to the dashed curves; batch and aggregated (a) and instantaneous fractional (b) for D = 0.01, 0.1, 1, 10 from melting_models.py; batch -> 1/D at F = 0, aggregated above batch for D < 1 and below for D = 10, both 1 for D = 1; D = 0.01 instantaneous melt below 0.01 C0 by F = 0.09 |
| 12 | fig:b3:trace-element-modelling:modes | 135 | ok | ok | three boxes: batch with melt kept in the residue then leaving at once, fractional with an empty residue and drops leaving, dynamic with a few pore-melt drops kept; captions under each box; no overlap |
| 12 | fig:b3:trace-element-modelling:ree | 136 | fixed | ok | legend sat on the spinel 1 % curve: ymax raised to 1000, legend above the data; y ticks plain numbers; nine REE with Budahn D only (Pr, Dy, Ho, Er, Tm omitted, stated in caption); garnet melts cross below the source at Lu (D_Lu > 1), spinel patterns gentle; source flat at 2.7-2.8 x chondrite |
| 12 | fig:b3:trace-element-modelling:ratios | 137 | ok | ok | log-log La/Yb vs La; spinel and garnet batch trajectories with F ticks at 1, 2, 5, 10, 20 % (traj and ticks parts); lava A (9.6, 5.65) on the spinel curve near 6 %, B (15.6, 34.7) on the garnet curve near 3 %; labels clear of the lines; legend colours checked on a 300 dpi crop |
| 13 | fig:b3:advanced-geochronology:concordia | 142 | fixed | ok | (a) concordia with age dots 100-350 Ma (tick 50 removed: its label sat on the y tick 0.01), five zircons (diamonds) on the discordia meeting the concordia near 311 and 100 Ma; 2-sigma ellipses are ~0.03 cm at this scale, so markers only, caption says so; (b) TW: concordia, age dots 100-250 (300+ removed, crowding the zircons), straight discordia (twline part, tested as the transformed Wetherill line) crossing the concordia at ~100 Ma; plain decimal ticks |
| 13 | images/book5/ai/b3-mass-spec-lab.jpg (inthelab) | 143 | fixed | ok | AI image reviewed: clean-room technician loading a sample turret, long flight tube, blue electromagnet, electronics racks; generic, no text, no brand; caption matches; box moved to the end of section 13.1 (at the end of 13.6 it left half a page blank) |
| 13 | fig:b3:advanced-geochronology:spectrum | 144 | fixed | ok | single axis showed the 2-sigma band as a line and clipped the plateau label: split into (a) whole spectrum 130-320 Ma (staircase 150, 228, 279 then plateau; "argon loss" clear of the risers) and (b) plateau enlarged 290-300 Ma with fill-between 2-sigma band and red plateau line 296.1, label (296.1 +- 0.8) Ma below the boxes; 82 % of 39Ar in steps 4-10 |
| 13 | fig:b3:advanced-geochronology:model-age | 145 | fixed | ok | legend covered first the granite line, then the T_DM label: moved above the axis in one row; DM line +4.5 at 2.5 Ga to +10.0 today, granite -14.4 today, meets CHUR at 1.30 Ga and DM at 1.84 Ga (dotted markers at those ages, labels readable); reversed time axis |
| 13 | fig:b3:advanced-geochronology:low-t | 146 | fixed | ok | TikZ schematic: (a) hexagonal apatite section with seven etched tracks; (b) grain with the 20 um ejection rim dashed, decay near the rim losing He, interior decay keeping it; "U" label moved off the "He lost" arrow; a stray zero-length arrow removed |
| 14 | fig:b3:stable-isotopes:rayleigh | 154 | fixed | ok | (a) vapour dashed and snow solid against condensation temperature 0 to -55 C, three station dots at -10/-20/-30 on the snow curve (-17.0, -31.3, -48.4); (b) dD vs d18O with the model snow and the dotted MWL dD = 8 d18O + 10, dots on the curve; legends clear of the curves; the d-excess block moved before the figure (a blank half page above it before) |
| 14 | fig:b3:stable-isotopes:lr04 | 155 | fixed | ok | LR04 stack 0-800 ka, reversed y; dotted Holocene 3.25 and LGM 5.02 levels; with clip=false the red ice-volume bar (1.4) and black cooling bar sit right of the axis at 830 ka, labels readable, no overlap with the record; width 0.8 |
| 14 | fig:b3:stable-isotopes:carbon | 156 | fixed | ok | (a) d13C_carb vs f_org for Delta_B -25/-30, crossing 0 near 0.2; (b) carbon added vs source composition for -2.5/-4.0 per mil in 50 000 Gt (was empty: y expr negated the values; now y=m25/m40, ymax 14000), 2000-12 500 Gt range; legends top-left clear of the curves |
| 14 | fig:b3:stable-isotopes:three-isotope | 157 | fixed | ok | TikZ schematic: slope 0.515 line, younger sulfide dot on it, Archean pyrite 1.5 above it with the Delta-33S arrow; x label moved to a node below the ticks (it sat on tick 5) |
| 14 | images/book5/ai/b3-ice-core-tent.jpg (inthelab) | 157 | ok | ok | AI image reviewed: two people in red parkas handling an ice core in a cradle under a drilling tent, drill tower behind; generic, no text or brand; caption matches |
| 15 | fig:b3:water-rock-interaction:calcite | 163 | fixed | ok | merged two figures into one two-panel figure (the separate degassing plot left a third of a page blank); (a) Ca vs log P_CO2 open (solid) and closed (dashed) at 10 and 25 C, cold above warm, closed below open, air dotted line at -3.37 with its label clear of the title, ground-water range as a light band behind the curves (a thin band with a label overlapped the closed curves and then the panel title); legend at 0.14 clear of the air line; (b) SI along the degassing path, x reversed, outlet (+0.04) and air (+1.61) dots from the ends part, labels moved off the line |
| 15 | images/book5/b3-palette-spring-travertine.jpg (inthefield) | 164 | ok | ok | PD NPS photo (Commons API verified): travertine terraces, orange microbial stripes, boardwalk with visitors for scale; caption and credit under the image; box third person, observation only |
| 15 | fig:b3:water-rock-interaction:rates | 165 | fixed | ok | log r vs pH at 25 C for forsterite, albite, K-feldspar, kaolinite from P&K parameters; V/U shapes, forsterite flat above pH 10 (no base mechanism, caption says so); legend outside right, colours checked on a 300 dpi crop (look black at 130 dpi); field-rate paragraph moved above the figure to fill the page it left blank |
| 15 | fig:b3:water-rock-interaction:activity | 166 | fixed | ok | log(aK/aH) vs log aH4SiO4 at 25 C: gibbsite/kaolinite at -4.39, kaolinite/muscovite at 1.55, gibbsite/muscovite and muscovite/K-feldspar slanted lines meeting the triple point; quartz (dashed) and amorphous silica (dotted) labels moved above the axis (rotated labels sat on the lines), K-feldspar and kaolinite labels moved off the dotted line; samples A (gibbsite), B (kaolinite), C (muscovite) |
| 15 | fig:b3:water-rock-interaction:box | 167 | fixed | ok | TikZ box model: rock box with initial/final delta, water in (blue) and out (red, d_r - Delta) arrows, open-system note below; inner label shortened (it ran out of the box) |
| 16 | fig:b3:sequence-stratigraphy:anatomy | 173 | fixed | ok | TikZ dip section: older deposits grey with two clinoforms; FSST red wedge with three downstepping clinoforms (they ran below the old slope: endpoints moved onto it); LST orange wedge; incised valley cut into the SB; thin TST green; HST blue with three clinoforms downlapping on the MFS; SB thick red, correlative conformity dashed, TS green, MFS blue passing into the condensed section; labels moved off the lines (basinward arrow overlapped the TST label, condensed/correlative conformity sat on the lines); stray empty node removed |
| 16 | fig:b3:sequence-stratigraphy:stacking | 174 | ok | ok | three grain-size logs of three coarsening-upward parasequences: tops 1.4/1.8/2.2 (progradational), 1.8 x 3 (aggradational), 2.2/1.8/1.4 (retrogradational); FS lines blue, mud-to-coarser axis on top |
| 16 | images/book5/b3-book-cliffs-helper.jpg (inthefield) | 174 | ok | ok | PD photo (Commons API verified), cropped to the cliff: pale sandstone ledges over grey mudrock slopes; caption descriptive, does not claim the Kenilworth Member; box third person, observation only |
| 16 | fig:b3:sequence-stratigraphy:series | 175 | fixed | ok | (top) E = -30 cos(2 pi t/400); (bottom) shoreline position every 2 kyr coloured by tract (scatter classes; colours distinct at 130 dpi), labels LST/TST/HST/FSST beside their segments; turning points at 118.5, 439.5, 559 kyr, the TST2 jump over the flat coastal plain near 540-556 kyr; moved before the section figure and heights reduced so both fit one page (the section figure first left half a page blank) |
| 16 | fig:b3:sequence-stratigraphy:section | 175 | fixed | ok | present-day section 0-70 km, -150 to +40 m (VE about 165-170): seven tract polygons coloured, older ramp + spin-up wedge grey (\closedcycle filled to y=0: replaced by an explicit polygon to -300), time lines every 40 kyr, shoreline trajectory dots with its loops at the turnarounds; tract labels added and the upper TST label moved off the trajectory; width 0.95 (overfull 9 pt at \linewidth) |
| 16 | fig:b3:sequence-stratigraphy:periodogram | 176 | fixed | ok | LR04 periodograms 0-1000 ka and 1250-2500 ka, detrended, Hann, normalised; (a) peak at 91 kyr in the 100-kyr band, 41 at 0.36; (b) 41.7 kyr dominant, 100 band 0.17; dotted 100/41/23/19 lines labelled above the axis; spurious x10^-2 scale label removed (scaled x ticks=false); figure moved before the periodogram definition and height reduced (it left a quarter page blank) |
| 17 | fig:b3:facies-models:walther | 182 | ok | ok | (a) four belts coastal plain/beach/shoreface/offshore mud with a seaward arrow; (b) the coarsening-upward log at one place in the same order, labels right of the log, up arrow; caption explains width = grain size |
| 17 | fig:b3:facies-models:rivers | 183 | ok | ok | (a) braided channels around two bars; (b) meandering channel with point bars on the inner banks of the three bends, dashed abandoned course, floodplain label; logs: braided cylinder with slight steps, point bar bell with scoured base and rooted mud cap |
| 17 | fig:b3:facies-models:shoreface | 183 | fixed | ok | profile beach-shoreface-offshore transition-offshore mud with sea level, FWWB and SWB dashed; y scale raised to 1.6 cm (wave-base labels sat on the dashed lines), labels below the lines; 'land' arrow overlapped 'beach' and was removed; storm-bed label moved off the profile; figure moved up after the shoreface definition (it left a quarter page blank) |
| 17 | images/book5/b3-hummocky-cross-stratification.jpg (inthefield) | 184 | ok | ok | CC BY-SA 3.0 (Commons API verified), cropped above the hammer held for scale (observation-only rule); grey mudstone and pale sandstone beds; caption repeats the Commons description only |
| 17 | fig:b3:facies-models:deep | 185 | fixed | ok | (a) Bouma log Ta-Te with grading/laminae/ripples symbols and labels to the right; (b) fan plan: canyon, channel, three distributaries ending in lobes, lower fan, basin floor; 'levees' label moved off the channel line |
| 17 | fig:b3:facies-models:platforms | 185 | fixed | ok | (a) ramp with tidal flat, shoal grains, bioclastic sand, lime mud; labels moved below the floor line (they sat on it and overlapped one another) and set tiny; (b) rimmed shelf with lagoon, orange reef rim, steep slope, basin label moved off the floor line |
| 17 | fig:b3:facies-models:logs | 187 | fixed | ok | GR, RHOB, DT tracks 700-1200 m from well_logs.py: chalk densifying 2.03-2.36, shale 110 API/2.45/100 us/ft, limestone 18/2.573/58.9, sandstone sawtooth, schist 85/2.75/50; a fourth GR panel enlarging the sandstone (1040-1172 m) shows the eleven bells and the 60 API cutoff (the sandstone was unreadable at full scale); 'sandstone' label was cut at the axis edge, moved; widths 0.28 (overfull 24 pt at 0.3) |
| 17 | images/book5/ai/b3-core-store.jpg (inthelab) | 187 | ok | ok | AI image reviewed: core repository, trays of split sand and mud cores, a geologist with a hand lens, shelving with boxes; generic, no text or brand; caption says AI-generated |
| 18 | fig:b3:quantitative-geomorphology:hillslope | 192 | fixed | ok | (a) scarp of 5 m offset on slope 0.05, initial step dashed, erf profiles at 2, 10, 40 kyr (kappa 5e-3) from hillslope.py; legend 'initial' (was '0'); (b) steady parabolic hills, half-width 150 m, relief 48/97/194 m for 0.0215/0.043/0.086 mm/yr; rate labels moved under the crests (the top one sat on the curve); right ylabel shortened and the panels set 1.6 cm apart (it touched the left panel); width 0.48 (overfull 1.4 pt at 0.5) |
| 18 | images/book5/b3-niagara-gorge.jpg (inthefield) | 197 | ok | ok | CC BY-SA 2.0 (Commons API verified), Niagara Gorge with the Horseshoe Falls mist at its head and the American Falls at the left edge; recropped tighter (two thirds of the first crop was water); casino sign excluded; no people in view; caption from the Commons description only |
| 18 | fig:b3:quantitative-geomorphology:regimes | 194 | fixed | ok | schematic: (a) detachment-limited, old profile dashed, two later profiles with a step (the first draft had the upper reach above the old profile: redrawn from one function f(x) and f(x) - 1.1 below the step); arrow upstream; (b) transport-limited, f(x) - 1.1 exp(-(L - x)/l) for two l, lowering most near the outlet |
| 18 | fig:b3:quantitative-geomorphology:profile | 194 | fixed | ok | (a) steady profile from the channel head (405 m) to the outlet (170 m) from stream_profile.py; (b) log S - log A, model line, twelve noisy reach gradients and their least-squares line (slope -0.47); panels 1.7 cm apart (ylabel 'gradient S' touched the left panel); moved after the steady-state proof (it left a third of a page blank) |
| 18 | fig:b3:quantitative-geomorphology:knick | 196 | fixed | ok | merged from two figures (each left a third of a page blank): (a) profiles before the fall and at 300/600/900 kyr, steps at 10.25, 8.73, 7.40 km from the divide, 25 m high; (b) chi plot, trunk as a grey band, tributaries as sparse marks (the four lines coincided and hid one another), steady line dashed, knickpoint triangle at chi 900 m; tributary 3 step visible, tributaries 1 and 2 entirely on the old line |
| 18 | fig:b3:quantitative-geomorphology:rebound | 198 | fixed | ok | schematic: plateau before; after, two V valleys, summits raised by delta, base of the crust raised by delta, old surface and old base dashed grey; delta labels moved right of the block (the first label sat on the dashed line) |
| 19 | fig:b3:gfd-foundations:frame | 213 | fixed | ok | (a) schematic: Earth section, axis, point at 40 deg, tangent plane, Omega split into Omega sin(phi) (up) and Omega cos(phi) (north), x east into the page; 'x, east' label moved off the tangent line and the 'north' label given a white fill (the rotation axis crossed it); (b) f = 2 Omega sin(phi) and its beta-plane tangent at 45 deg from inertial_oscillation.py, point at 1.031e-4 |
| 19 | fig:b3:gfd-foundations:inertial | 215 | ok | ok | paths over 4 days at 45 N from inertial_oscillation.py (RK4, tested against the closed form): circle radius 1.94 km, friction spiral (e-folding 4 d), loops drifting 17 km with a 0.05 m/s current; axis equal image, legend at the bottom right clear of the loops |
| 19 | fig:b3:gfd-foundations:taylor | 216 | ok | ok | schematic: (a) side view, obstacle, grey column to the surface, flow arrows stopping at the column, Omega above; (b) top view, streamlines parting round the column footprint, symmetric |
| 19 | fig:b3:gfd-foundations:buoyancy | 217 | ok | ok | (a) N(z) of the standard atmosphere 0-30 km, steps at 11 and 25 km, tropopause dashed; (b) N in cycles per hour vs depth for the WOA23 40.5 N 30.5 W column, maximum 6.1 cph at 32.5 m, below 2.2 cph under 200 m; both from buoyancy_frequency.py |
| 19 | fig:b3:gfd-foundations:geometry | 218 | fixed | ok | schematic: four pressure surfaces sloping down to the cold (north) side, slopes proportional to height (0.9k to 0.675k), warm-cold shading, eastward-wind circles growing with height; the first draft's top layers nearly met (quadratic slopes), redrawn linear; u_g label moved off the p4 line; figure moved before the theorem and shrunk (it left a third of a page blank) |
| 19 | fig:b3:gfd-foundations:jets | 219 | fixed | ok | (a) January zonal-mean u vs log p at 30/45/60 N (NCEP R1 1991-2020), 30 N max 43.9 at 200 hPa; (b) poleward temperature drop 850-250 hPa from the shear, January and July, |lat| >= 25 deg, each hemisphere drawn separately (no line across the gap); legend moved to the empty equatorial gap (it touched the July curve) |
| 19 | images/book5/ai/b3-rotating-tank.jpg (inthelab) | 220 | ok | ok | AI image reviewed: acrylic tank on a turntable, co-rotating camera frame, blue dye spiralling round a cylinder, researcher at a monitor; generic, no text or brand; caption says AI-generated |
| 20 | fig:b3:atmospheric-dynamics:restoring | 226 | fixed | ok | schematic: sinusoidal chain of parcels about latitude phi0 (one declared function), clockwise arcs at crests (zeta < 0), anticlockwise at troughs (zeta > 0), induced southward arrows at descending nodes and northward at ascending nodes, consistent with a westward shift (sin(x + delta)); the bottom zeta > 0 label collided with 'the pattern moves west': compass and arrow moved down |
| 20 | fig:b3:atmospheric-dynamics:rossby | 227 | fixed | ok | (a) c and c_g vs n at 45 N, U = 0 and 15 m/s from rossby_waves.py (n = 4.7 crossing for U = 15, c_g > c everywhere); legend first had split entries (commas in \legend) and then black legend lines (a forget-plot zero line before the plots): rewritten with \addlegendentry, zero line last; (b) n_s vs latitude for 10/15/20 m/s and the January 300 hPa zonal-mean dots (~4 from 35 to 55 N); moved after the theorem proof (it left half a page blank) |
| 20 | fig:b3:atmospheric-dynamics:eady | 229 | ok | ok | (a) Eady growth rate per day vs wavelength (2-16 thousand km) for the observed 45 N January shear 1.93e-3, N 0.0113, H 11 km: cut-off 3160 km dashed, maximum 0.47/day at 4720 km (e-folding 2.1 d); (b) MODIS photo of the low off Iceland, 4 Sep 2003, NASA PD (Commons API verified), anticlockwise spiral, no text in image |
| 20 | fig:b3:atmospheric-dynamics:heatflux | 230 | fixed | ok | schematic plan view: streamline sin(x) and isotherm 0.9 sin(x + 1) - 0.15 (lagging), warm arrows north at ascending streamline, cold south; 'warm'/'cold' labels sat on the curves and the compass under an arrow: labels moved to the arrow tips and the compass to the left |
| 20 | fig:b3:atmospheric-dynamics:held-hou | 231 | fixed | ok | (a) theta_E and theta_M (Delta 1/3, H 15 km) meeting at phi_H 35.3 deg (dashed), equal areas (tested); long legend crossed the phi_H line: shortened to theta_E/theta_M; (b) psi at 500 hPa, year/DJF/JJA from held_hou.py, winter cells straddling the equator, edges ~30 deg |
| 21 | fig:b3:ocean-dynamics:pumping | 225 | fixed | ok | schematic meridional section, east into the page: trades as dots (westward, out of page), westerlies as crosses, Ekman transports to the right of each wind converging, w_E < 0 arrows, squashed column moving equatorward; 'Ekman layer', 'base of the wind-driven flow' and 'column squashed' labels overlapped arrows or the box edge: moved below the dashed lines, box widened |
| 21 | fig:b3:ocean-dynamics:sverdrup | 227 | fixed | ok | three meridional profiles from wind_driven_gyre.py: tau (-0.1 at 20 N, 0 at 35 N, +0.1 at 50 N), w_E (-34.7 m/yr at 35 N, minimum ~-41 near 28 N, positive north of 47 N) and total Sverdrup transport (-29.4 Sv at 35 N, positive north of 48.3 N); the first draft clipped both at 0 and its caption said 'pushed down everywhere': axes extended to positive values, zero lines added, caption and text corrected |
| 21 | fig:b3:ocean-dynamics:boundary | 228 | fixed | ok | (a) northward transport per unit width vs distance from the west wall: Stommel 546 m2/s at the wall, e-folding 53 km, zero at 252 km; Munk zero at the wall (no slip), peak ~245 m2/s at 78 km, zero at 233 km, countercurrent ~-45; (b) cumulative transport: Stommel plateau 27.9 Sv, Munk peak 33.0 Sv, interior 29.4 Sv dashed; caption first said the Munk peak was at 60 km and that both layers return 29.4 Sv: corrected to 80 km and to the computed 27.9/33.0 Sv |
| 21 | fig:b3:ocean-dynamics:stommel-arons | 230 | fixed | ok | schematic plan view of a sector basin: source near the pole on the west, DWBC along the west wall towards the equator, interior arrows poleward, upwelling dots; the DWBC label overlapped the wall and then the source label, and the side labels touched the east wall: labels moved off the walls ; the 'source S0' label still touched the east wall at the next build: reduced to 'S0' beside the dot, 'source S0' named in the caption (re-checked at 130 dpi, clear) |
| 21 | images/book5/b3-argo-deploy.jpg (inthefield) | 231 | ok | ok | NOAA GOMO photo, public domain (Commons API), 762 x 432 px at 0.44 linewidth (~260 dpi): yellow Argo float lowered on a line by two crew in hard hats and life jackets over the side of a ship; no text, no brand; box moved after the dynamic method (it left a third of a page blank in the tides section) |
| 21 | fig:b3:ocean-dynamics:equilibrium-tide | 232 | fixed | ok | (a) equilibrium bulge r = 1 + 0.12 P2(cos theta) (exaggeration ~2e6) round the unit Earth, symmetric 1.12 along the Moon line, 0.94 across; 'to the Moon' label was clipped and overlapped the bulge: clip=false, label above the arrow; (b) 48 h at 45 N: delta 0 gives equal highs 0.089 m and lows -0.178 m; delta 20 gives highs 0.261 and -0.083 (diurnal inequality); legend placed over the low at 12.4 h |
| 21 | fig:b3:ocean-dynamics:amphidromes | 233 | fixed | ok | two opposing Kelvin waves in a 400 km x 50 m channel at 55 N from tides.py: amphidromes at 248, 743, 1238 km on the centre line (|Z| = 0, tested), cotidal lines every 30 deg radiating from them, co-range lines circling; the 0/180 deg lines run along the centre line and on the meridians k x = n pi (Z is real there, as the formula requires); anticlockwise arrow (tested rotation sense); first draft 5.6 pt overfull: width 0.96 linewidth |
| 22 | fig:b3:climate-models:zero-d | 239 | fixed | ok | (a) absorbed sunlight 340(1-alpha(T)) with the -10/+10 C ramp vs OLR 211.9 + 1.816 T from budyko_sellers.py: crossings at -45.6 (129.2), 7.8 (226.1, open), 14.4 (238.0); (b) equilibria vs S0 1000-2200: warm branch from 1314.6 (10 C), snowball to 2039.4 (-10 C), unstable branch dashed joining them, arrows of the hysteresis jumps; 'unstable' label first overlapped the ramp line, then the legend: moved below-right with a leader; 'today' label given a white fill over the dotted line; 'warm' moved off the green line |
| 22 | fig:b3:climate-models:budyko | 241 | fixed | ok | (a) Q/Q0 for an ice line at each latitude (Budyko relaxation model, NCEP OLR fit and insolation shape): stable branch 47.65-90 deg (0.9713 to 1.0069), unstable 0-47.65 (1.2249 to 0.9713), snowball line at 0 for q < 1.2249, no-ice line at 90 for q > 1.0069; today (1, 72) stable, (1, 30.15) open; first build's 'glaciation threshold' label collided with the y tick labels and axis title, and 'snowball' sat on the dashed branch: moved, with a leader; (b) model T profile (jump at the 72 deg ice line) vs NCEP annual zonal means, Tc = -12.26 dashed |
| 22 | fig:b3:climate-models:two-layer | 242 | ok | ok | (a) abrupt 4xCO2: T 3.69 at 10 yr, 4.59 at 100, 5.62 at 500 vs equilibrium 5.91 dashed, Td 5.02 at 500 yr; (b) 1 %/yr ramp to 140 yr: T, Td and -F/lambda dashed; dots at year 70: TCR 1.99, ECS 2.95; legend colours checked zoomed (blue, red, grey dashed) |
| 22 | fig:b3:climate-models:grid | 243 | fixed | ok | schematic slice of a global grid: 5 columns x 6 levels over ocean and land, one column shaded, resolved-wind arrows in the others, inside the column sunlight down (red wavy), infrared up (blue wavy), cloud, convective updraft, surface eddy, leader lines to the right; cloud was drawn under the wavy arrows and the eddy was a speck: cloud drawn last, eddy enlarged; cell 'about 100 km' (ar6ch1:faq-resolution) |
| 22 | fig:b3:climate-models:ladder | 244 | fixed | ok | five rungs (0-D EBM, Budyko-Sellers, two-layer EBM, GCM, ESM) with what each computes, arrow 'more processes, more computing'; 'Earth sys-tem model' hyphenated in the first build: forced line breaks; caption 'run millions of times / a few times' changed to the sourced 'a million times / need supercomputers' |
| 22 | fig:b3:climate-models:supercomputer | 244 | ok | ok | photo P: NCCS supercomputer racks, NASA GSFC 2010, PD (Commons API checked), cropped 1920x1040 from 150 px, 1400 px JPEG; no readable text or logos at print size |
| 22 | inthelab: A modelling centre (AI b3-model-centre.jpg) | 246 | ok | ok | AI image reviewed: two people seen from behind at desks before a curved wall of screens with a global field map (cyclone swirls, warm tropics); generic, no readable text, no brand or real place; caption says AI-generated |
| 23 | fig:b3:hydrogeology:head | 250 | fixed | ok | schematic piezometer: tube open at its screen at P, water rising to h above the water table (upward flow); z, p/rho g and h arrows from the datum; first build put the arrows right of the tube, crossed by the screen label: arrows moved left, label shortened; ground fill extended down to the datum |
| 23 | fig:b3:hydrogeology:aquifers | 252 | fixed | ok | schematic W-E section of the Varden cover (region.py probe along y = 5000: limestone outcrops at x 4000, shale at Varden-3 (4500), chalk from 5000 east): limestone outcrop with recharge arrow, shale confining layer, chalk with water table, potentiometric surface below ground and above the limestone top at the well, well open to the limestone with water to that surface; first draft put chalk over the well (wrong: shale outcrops there) and crowded the left labels: redrawn with clipped dipping bands; chalk label moved twice off the water table and the potentiometric label |
| 23 | fig:b3:hydrogeology:flow-net | 253 | fixed | ok | flow_net.py: SOR solutions for h and psi under a 20 m dam on 20 m of sand, 9 equipotentials (thin red, antisymmetric about the axis, tested) and 4 streamlines (thick green, nested arcs under the dam); q = 0.512 K H computed vs 0.50 from 5 channels / 10 drops; first build: reservoir 6 m deep against a 10 m head (drawn water depths now differ by 10 m), H arrow and dashed level crossed the dam (removed, said in the label), 'impermeable rock' overlapped the x ticks (moved inside) |
| 23 | fig:b3:hydrogeology:theis | 254 | fixed | ok | (a) W(u) vs 1/u (exp1) and -gamma - ln u, merging right of u = 0.05 (dotted), W above the line at small 1/u as the series requires; (b) Varden-3 record (22 points, Theis + 4 mm noise, rounded to 1 cm) and the Cooper-Jacob line slope 0.872, t0 0.973 min, fitted to the 16 points with u <= 0.05 (after 11.5 min, dotted); early points above the line; rotated 'u = 0.05' label crossed the curve: unrotated, moved right |
| 23 | fig:b3:hydrogeology:cone | 255 | fixed | ok | (a) Theis drawdown (downward) vs r at 1, 10, 100 d, Q 2160, T 450, S 2e-4: equal deepening per decade; (b) two wells 400 m apart at 10 d: dashed singles, black sum 5.46 m midway (2 x 2.73), spikes at the wells clipped; legends first sat on the curves: (a) bottom right, (b) one row at the top; legend colours checked at 800 dpi (blue, green dashed) |
| 23 | inthefield: A pumping test (AI b3-pumping-test.jpg) | 255 | ok | ok | AI image reviewed: field, wellhead discharging into a ditch, generator, a person at a folding table with a laptop and logger, cable into a white observation-well casing; generic, no readable text, logos or real place; caption says AI-generated |
| 23 | fig:b3:hydrogeology:transport | 256 | fixed | ok | advection_dispersion.py (Ogata-Banks, erfcx form, tested against the PDE): (a) C/C0 at 100 m vs t for alpha 1, 3, 10 m (t50 198.0, 194.2, 182.0 d; water at 200 d dotted) and the retarded R = 3 curve (t50 582.6); (b) profiles at 150 d, all crossing near the advective front 75 m; R = 3 legend entry overlapped the dashed curve: replaced by a direct two-line label, legend kept to three entries bottom right |
| 24 | fig:b3:glaciology:flow | 262 | ok | ok | ice_flow.py: (a) slab velocity u/u_s vs z/H for n = 3, n = 1 and n = 3 with sliding (shear concentrated near the bed for n = 3; sliding shifts the whole profile); (b) ETOPO1 Ice Surface transect along 72.5 N, 58 W to 20 W (max 3229 m at 679.5 km) with the two Nye profiles fitted for h > 1000 m, tau0 72 kPa west and 108 kPa east, labels in the free corners, legend bottom centre off the curves; sea-level line grey |
| 24 | fig:b3:glaciology:zones | 263 | ok | ok | schematic valley glacier: accumulation arrows down above the dashed ELA, ablation arrows up below, grey flow lines dipping then rising, bedrock fill, snout labelled at the tip; labels clear of arrows and of each other |
| 24 | fig:b3:glaciology:grounding | 264 | fixed | ok | schematic marine ice sheet: bed deepening inland to a grounding line (red dot + arrow), floating shelf, calving front, iceberg, sea and bed fills, buttressing note; first build: flow arrow crossed 'floating ice shelf', buttressing arrow sat beside 'calving front', 'sea level' touched the iceberg: arrows moved, sea-level label moved to the left end, iceberg shifted right, 'grounded ice sheet' raised off the sea-level label; re-rendered at 130 dpi |
| 24 | fig:b3:glaciology:outlet (photo b3-greenland-outlet.jpg) | 265 | ok | ok | NASA/Jim Yungel IceBridge 2014, PD: outlet glacier between mountains, broken blue calving front across the middle, ice-choked fjord in front; aircraft wing cropped out; caption matches the Commons description; credit in caption, CREDITS.md and image-credits |
| 24 | inthefield: A camp on the ice (AI b3-glaciology-camp.jpg) | 266 | ok | ok | AI image reviewed: three tents, two loaded sledges, a snowmobile, a GNSS antenna on a guyed mast on flat snow; generic, no readable text, logos or real place; caption says AI-generated |
| 24 | fig:b3:glaciology:sea-ice | 267 | fixed | ok | sea_ice.py: (a) NSIDC March and September extent 1979-2026 with dashed least-squares trends (-0.38 and -0.74 Mkm2/dec); (b) Stefan growth 20 K, bare ice (2.14 m at 200 d) vs 20 cm of snow (1.18 m); first build: (a) legend covered the 1980s September points: moved up to the gap between the series; legend colours checked (blue March, red September; green solid, blue dashed) |
| 25 | fig:b3:remote-sensing-gis:spectra | 272 | fixed | ok | spectral_signatures.py from five ECOSTRESS spectra (grass, tap water, sand, kaolinite, haematite) 0.4-2.5 um, Landsat 8 OLI bands B2-B7 shaded grey and labelled; grass red edge, water dark beyond 0.7 um, kaolinite dip at 2.20 um inside band 7; first build: legend covered kaolinite and band 7: moved below the axis in 5 columns; colours checked |
| 25 | fig:b3:remote-sensing-gis:thermal | 274 | fixed | ok | thermal_ir.py: (a) Planck B_lambda at 300 K, 400 K and 1443 K on log axes 1-25 um with band 10 marked and Wien peaks; (b) mixed-pixel brightness temperature vs hot fraction (370 K in 290 K) above the mean-temperature line; first build: with clip=false the log curves spilled below the axis: clip restored |
| 25 | fig:b3:remote-sensing-gis:sar | 275 | ok | ok | TikZ side-looking geometry: flight track into the page, incidence angle, slant range R, ground range, swath, nadir; labels clear of the beam lines |
| 25 | fig:b3:remote-sensing-gis:insar | 277 | fixed | ok | insar_mogi.py: (a) wrapped phase over a Mogi source (z0 4 km, dV 1e7 m3, C band, 35 deg, satellite to the east), 4.4 cycles, rings shifted east and crowded west; (b) uz, uE, LOS east-west and north-south profiles; first build: legend covered the peak (ymax 240, two columns at the top) and 'to satellite' touched the border (moved inside); re-rendered at 130 dpi |
| 25 | fig:b3:remote-sensing-gis:three-sisters (photo b3-three-sisters-insar.jpg) | 278 | ok | ok | USGS (Wicks et al. 2002), PD: draped interferogram of the Three Sisters with the colour bar (28.3 mm per cycle) and the unwrapped relief below; caption matches the Commons description; credit in caption, CREDITS.md and image-credits |
| 25 | inthelab: A ground station (AI b3-ground-station.jpg) | 278 | ok | ok | AI image reviewed: large white dish on a pedestal, small lit operations building, hills at dusk with the sun below the horizon behind them; generic, no readable text, logos or real place; caption says AI-generated |
| 25 | fig:b3:remote-sensing-gis:raster-vector | 279 | fixed | ok | TikZ: vector panel (lake polygon, river line, two wells) and the same map as a 10 x 7 raster (lake cells pale, river cells blue, well cells red); first build: grid lines mis-stepped under x=0.5cm: step=1 added; cells checked against the vector features |
| 25 | fig:b3:remote-sensing-gis:varden | 280 | fixed | ok | varden_gis.py on region.py 100 m grid: (a) slope (max 23.0 deg) with colorbar, (b) aspect, (c) the two layers, (d) overlay: shale within the 1 km buffer (traced) and the 0.32 km2 selected; first build overfull 12.8 pt (panels 0.43 linewidth); slope colorbar label collided with (b): moved into the title; squashed categorical colorbars replaced by area-legend entries below (c) and (d) |
| 26 | fig:b3:planetary-interiors-surfaces:two-layer | 286 | fixed | ok | two_layer_planet.py: x against rho_c for the Earth, Mars, the Moon (dashed) and Mercury from mean density and C, dots at the measured core radii (PREM 3480, InSight 1830, Moon 330, Mercury about 2000 km); first build: the Moon's curve stopped short of its dot (sampling in rho_m too coarse near the singular end): resampled in x; labels clear of curves |
| 26 | fig:b3:planetary-interiors-surfaces:craters | 287 | fixed | ok | TikZ cross-sections: simple crater (bowl, breccia lens, dashed transient crater, raised rim, ejecta wedges) and complex crater (terraces, faults, flat floor, central uplift, uplifted layers); first build: white over-fills left a notch at the right rim and the terrace and layer lines ran into the air; redrawn as filled profiles with clipped layers; 'faults' arrow crossed the rim and 'flat floor' sat on the wall: both moved into the ground |
| 26 | fig:b3:planetary-interiors-surfaces:barringer (photo b3-barringer-crater.jpg) | 287 | fixed | ok | USGS/D. Roddy aerial photograph, PD: the bowl, raised rim and ejecta blanket on the plateau; caption matches the Commons description and French (1998); width reduced to 0.66 linewidth so that it fits under the cross-sections instead of leaving half a page empty |
| 26 | fig:b3:planetary-interiors-surfaces:sfd | 289 | fixed | ok | crater_sfd.py: (a) Mars isochrons 0.1, 1, 3.5, 4 Ga (Ivanov PF x Hartmann-Neukum CF) and Hartmann's equilibrium (dashed), the 4 Ga isochron crossing it at 0.66 km as the caption says; (b) chronology functions of Mars and the Moon; first build: the 3 and 4 Ga labels and 'equilibrium' crowded the curves: 3 Ga replaced by 3.5 Ga, labels moved below their curves, 'equilibrium' above its line |
| 26 | fig:b3:planetary-interiors-surfaces:lids | 290 | ok | ok | TikZ schematic of mobile lid (plates, ridge upwelling, slab), stagnant lid (thick shell over two cells, one volcano) and heat pipes (thick lid, three conduits, downward burial arrows); labels clear |
| 26 | fig:b3:planetary-interiors-surfaces:olympus (photo b3-olympus-mons.jpg) | 291 | ok | ok | NASA/JPL/USGS Viking mosaic PIA00300, PD: calderas, flanks and the scarp ring; black edge at the left cropped; caption matches the photojournal description |
| 27 | fig:b3:planetary-atmospheres:structure | 297 | fixed | ok | TikZ schematic: temperature profile with troposphere (adiabat), stratosphere, thermosphere, tropopause, homopause and exobase lines; exosphere panel with a ballistic and an escaping trajectory; first build: the grey right panel covered the line labels 'exobase', 'homopause', 'tropopause', and the profile crossed 'troposphere: convection': profile moved right, lines and labels lengthened, panel shifted right; no number on the schematic |
| 27 | fig:b3:planetary-atmospheres:jeans | 299 | fixed | ok | jeans_escape.py: (a) lambda against particle mass at the exobases of Venus (290 K, 200 km), the Earth (1000 K, dashed 800 and 1600 K, 500 km), Mars (270 K, 200 km), Titan (180 K, 1500 km) with the hydrodynamic band below 2.5; (b) (1+lambda)exp(-lambda) with H, D, He at the Earth's exobase; first build: 11 pt overfull and the Earth/Mars labels sat on the dashed lines: widths reduced to 0.47 linewidth, labels replaced by a legend (colours checked at 300 dpi); values match Gronoff Table 2 at the planetary radius (test) |
| 27 | fig:b3:planetary-atmospheres:runaway | 301 | fixed | ok | runaway_greenhouse.py (illustrative grey model, flagged in the caption): OLR rises from 215 to 258 W/m2 between 250 and 288 K and levels off at 291 W/m2 above about 450 K; horizontal lines at 525 (Venus today, albedo 0.193), 367 (young Venus, Sun at 70 %), 238 (Earth, albedo 0.3) and the line-by-line limit 291; first build: the curve label sat on the Earth line: moved below the curve |
| 27 | fig:b3:planetary-atmospheres:valleys (photo b3-mars-valley-network.jpg) | 302 | ok | ok | ESA/DLR/FU Berlin Mars Express HRSC nadir view, CC BY-SA 3.0 IGO, credit line and 20 km scale bar burnt in; branching valleys visible across the centre; caption matches the ESA description (14 m/px, 17 S 66 E, north to the right); the caption's first draft attributed the valleys to rain or snowmelt, an interpretation the source does not make: reworded to 'the pattern of a drainage network' |
| 27 | fig:b3:planetary-atmospheres:ligeia (photo b3-ligeia-mare.jpg) | 303 | fixed | ok | Cassini radar mosaic PIA10008 crop, NASA/JPL/USGS, PD; liquid blue-black, ground brown; caption from the photojournal text (400 lakes and seas, 70 % of the area in seas above 26,000 km2); a Lake Superior comparison area (from another PIA) removed as unsourced for this image; width 0.6 left half a page empty: reduced to 0.5 so the phase diagram follows on the same page |
| 27 | fig:b3:planetary-atmospheres:phases | 303 | fixed | ok | habitability.py: IAPWS liquid-vapour and ice sublimation curves, NIST Antoine curve of methane 91-190 K, triple and critical points, surface states of Venus (737 K, 92 bar), the Earth (288 K, 1 bar), Mars (214 K, 6.36 mbar), Titan (94 K, 1.6 bar); first build: 'methane' and 'critical point' labels on their curves: moved beside the end points |
| 27 | fig:b3:planetary-atmospheres:hz | 304 | fixed | ok | habitability.py: Kopparapu (2013) Table 3 fits, moist and maximum greenhouse (shaded between), runaway (dashed), recent Venus and early Mars (dotted), 2600-7200 K; Venus 1.91, Earth 1.00, Mars 0.43 at 5780 K; the Earth lies just inside the moist-greenhouse line (1.014), as it should; first build: Earth and Mars labels on the lines: moved into the shaded zone |
| 28 | fig:b3:exoplanets:rv | 310 | fixed | ok | rv_transit.py: circular (K = 30 m/s, P = 10 d) and e = 0.3, omega = 60 deg curves over two orbits; extremes K(1 +- e cos omega) = +34.5 / -25.5 match the theorem; first build: the K label sat on the dashed curve and the legend entries ran together: label moved left of the arrow at phase 1, legend column separation and left alignment added |
| 28 | fig:b3:exoplanets:transit (left, TikZ geometry) | 312 | fixed | ok | star of radius 2 cm shaded darker to the limb, path at b = 0.3, planet p = 0.1 drawn at the four contacts (x = +-2.117 and +-1.697 cm, checked against sqrt((1 +- p)^2 - b^2)); first build: labels 2 and 3 sat under discs 3 and 4: 2 and 3 moved above the path |
| 28 | fig:b3:exoplanets:transit (right, light curve) | 312 | ok | ok | rv_transit.py numerical quadratic limb darkening (u1 0.40, u2 0.25) against the uniform disc (depth exactly 1 %); contact lines at +-2.698 h (T14 5.40 h) and +-2.162 h (T23 4.32 h) fall on the start of ingress and of the flat bottom; first build crashed (TeX input stack) on a \foreach with \edef: replaced by four explicit lines |
| 28 | fig:b3:exoplanets:hip65426 (photo b3-hip65426b.jpg) | 313 | fixed | ok | JWST NIRCam/MIRI composite with Digitized Sky Survey field, NASA/ESA/CSA, A Carter (UCSC), ERS 1386 team, A. Pagan (STScI), CC BY 4.0; caption from Carter et al. abstract and the Commons description; first draft interpreted the bars around the planet (unsourced): removed; the sky-survey upper half now named in the caption |
| 28 | fig:b3:exoplanets:microlensing (left, TikZ geometry) | 314 | fixed | ok | source, lens with Einstein ring, observer, two bent rays and the apparent image direction (collinear with the observer and the upper ray point); not to scale (stated); first build: the 'lens' label was crossed by the ring: moved below, distance arrows lowered |
| 28 | fig:b3:exoplanets:microlensing (right, magnification) | 314 | ok | ok | rv_transit.py A(u) for u0 = 0.1, 0.3, 1: peaks 10.04, 3.44, 1.34 (A(1) = 3/sqrt5 tested); log axis 0.8-12 |
| 28 | fig:b3:exoplanets:methods | 315 | fixed | ok | exoplanet_archive.py: mass (true or minimum, not M-R-predicted) against semi-major axis for 1691 transit, 1151 RV, 286 microlensing, 94 imaging planets; Solar System from the fact-sheet ledger; first build: Jupiter and Saturn labels on the microlensing points, Earth/Venus labels stacked, Mercury clipped at ymin 0.05: labels given white fills and placed beside the squares, ymin 0.02, Mercury and Mars labelled, legend marks enlarged |
| 28 | fig:b3:exoplanets:valley | 316 | ok | ok | exoplanet_archive.py: (a) 2370 transiting planets (radius error < 10 %, star < 2 R_sun, P 1-100 d); (b) step histogram in 20 log bins 0.8-4 R_E: 61 planets at 1.79-1.94 against 80-83 at 1.4-1.65 and 168 at 2.47-2.67, the valley visible (tested); caption says the counts are uncorrected |
| 28 | fig:b3:exoplanets:mass-radius | 317 | fixed | ok | 1078 planets (mass < 25 %, radius < 10 %) with Zeng tables: iron, Earth-like rock (1.03 R_E at 1.115 M_E), 50 % water 500 K, Earth-like + 2 % H2 500 K; Solar System squares; first build: Uranus/Neptune, Saturn and Jupiter labels in the point cloud and legend cells centred: labels moved with white fills, legend cells left-aligned |
| 29 | fig:b3:milky-way-galaxies:panorama | 323 | ok | ok | ESO/S. Brunier whole-sky panorama (CC BY 4.0), 1800 x 900 px; plane horizontal, centre at the middle; the two patches below the band at right checked against the Magellanic Clouds' Galactic coordinates (l 280.5/302.8, b -32.9/-44.3: x 867/790, y 410/447 of 1200 x 600) and the smudge at left against Andromeda (l 121.2, b -21.6: x 197, y 372) before the caption names them |
| 29 | fig:b3:milky-way-galaxies:sketch (a, edge-on) | 324 | fixed | ok | to scale at 0.17 cm/kpc: thin/thick disc bands, box bulge, halo circle 17 kpc, Sun at 8.2 kpc; first build: the face-on panel was shifted by 235 cm (xshift given as 40cm/0.17, unscaled; 6387 pt overfull) and a halo dot sat on the 'bulge' label: shift set to 7.6 cm, dot moved |
| 29 | fig:b3:milky-way-galaxies:sketch (b, face-on) | 324 | fixed | ok | bar half-length 5 kpc at 27 deg to the Sun-centre line, near end at positive longitude (left, l = 90 to the left with the centre up); first build: bar drawn at 27 deg from the horizontal, arms running out of the disc to 16 kpc, 'rotation' label on its arrow: bar rotated to 63 deg, arms stopped at 13.3 kpc and started from the bar ends, clockwise arrow moved outside the halo on the right with its label |
| 29 | fig:b3:milky-way-galaxies:tangent | 326 | fixed | ok | geometry exact for l = 40 deg: T = (-1.970, -1.653) cm, |CT| = 2.571 = 4 sin 40; V(R) along the line of sight, V0 at the Sun to the left (clockwise rotation); first build: 'R0 sin l', 'tangent point', 'V(R)' and 'line of sight' crossed by lines or circles: white fills, label positions moved, line of sight extended |
| 29 | fig:b3:milky-way-galaxies:rotation | 327 | fixed | ok | Eilers Table 1 (38 points, asymmetric error bars) with Pouliasis Model I components and the NFW fitted here (rho0 1.056e7, Rs 14.75, tested against Eilers 1.06e7/14.8 and on synthetic data); total 229.4 at R0; halo crosses baryons at 14.3 kpc as stated; first build: thick disc grey like the baryon curve and the legend far below the axis: thick disc violet, legend raised |
| 29 | fig:b3:milky-way-galaxies:mass | 329 | ok | ok | R v^2/G for the model total, the stars, and the 38 measured bins; stars level at 8.7e10 (8.96e10 total model mass, caption 'about 9e10'); at 20 kpc total 20.4 (model) and 18.6 (data) against 8.37: 'more than twice' (caption corrected from 'twice'); legend renamed 'stars, model' (the model has no gas) |
| 29 | fig:b3:milky-way-galaxies:fork | 330 | ok | ok | schematic tuning fork: E0, E3 (b/a 0.7), E7 (b/a 0.3) drawn with the En rule, S0, Sa-Sc and SBa-SBc with shrinking bulges and opening log-spiral arms (rate 0.16-0.45), arms of barred types starting at the bar ends, Irr blobs; labels clear |
| 29 | fig:b3:milky-way-galaxies:m101 | 330 | ok | ok | ESA/NASA Hubble M101 (CC BY 4.0), 1400 x 1094 px from the 3840 px thumbnail; the image is cropped at its edges (outer arms cut), which the caption says; colours described only as seen (yellowish bulge, bluer knotted arms, brown dust lanes) |
| 29 | fig:b3:milky-way-galaxies:leavitt | 332 | fixed | ok | 2315 OGLE F-mode Cepheids, W_I against log P, y reversed; 92 clipped points in red; fit -3.3147/15.8887, sigma 0.0776 (published -3.314 +- 0.008, 15.888 +- 0.005, 0.077; tested); first build: legend far below the axis: raised |
| 29 | fig:b3:milky-way-galaxies:ladder-rungs | 333 | ok | ok | bars read from distance_ladder.py (parallax 4 kpc; Cepheids/TRGB 49.6 kpc-45.1 Mpc; SNe Ia 95.6-615.7 Mpc for z 0.0233-0.15 at H0 73.04); anchors LMC 49.6 kpc, M31 783 kpc, NGC 4258 7.58 Mpc from distance moduli; log axis labels 1 pc-1 Gpc |
| 30 | fig:b3:origin-of-elements:curve | 339 | fixed | ok | solar_abundances.py: 83 elements, photospheric where available else CI (Asplund 2021 Table 2), even and odd lines; first build: the even line ran straight from Pb (82) to Th (90) across the missing elements, 'Li, Be, B' sat on the y axis, Te/Xe and Ba labels overlapped, U label below the axis: line split at Z 84, labels moved, ymin -1.8 |
| 30 | fig:b3:origin-of-elements:sun-ci | 340 | ok | ok | 72 elements with both values; 58 black (weighted mean difference 0.000 +- 0.007 dex, tested against the paper), 9 depleted in CI (squares, labelled) and Li (triangle, 2.29 dex); labels clear of the points |
| 30 | fig:b3:origin-of-elements:crab | 341 | fixed | ok | NASA/ESA Hester and Loll mosaic, public domain, 1400 px; first build at 0.62 linewidth left half a page blank before it: 0.5 linewidth; caption facts (24 exposures, 1054, 30 pulses per second) from the Commons description row |
| 30 | fig:b3:origin-of-elements:chart | 342 | fixed | ok | neutron_capture.py classes for Cd-Ba, N 62-84 (s-only 110Cd, 116Sn, 122-124Te, 128/130Xe, 134/136Ba blue; r-only 116Cd, 122/124Sn, 123Sb, 128/130Te, 134/136Xe red; p orange), s path arrows with the 134Cs/135Cs split, r-chain arrows ending on 128Te, 130Te, 134Xe; first build: nodes near coords overrode the scatter classes (all black dots, labels with a dot in them) and 108Cd was drawn outside the axis (clip=false): squares and labels split into separate plots, x restricted |
| 30 | fig:b3:origin-of-elements:sigma-n | 344 | fixed | ok | 30 s-only sigma N (KADoNiS x proto-solar abundance), classical model fitted to 22 points A > 90 (tau0 0.306/mb, rms 0.064 dex, tested); steps at N 50, 82, 126 visible; first build: Lu label overlapped the x axis: moved right of the point; text 'within two per cent' corrected to three (31.48/30.75 = 2.4 %) |
| 30 | fig:b3:origin-of-elements:kilonova | 346 | ok | ok | NASA/ESA heic1717a (CC BY 4.0), 1365 x 1458 px; insets dated Aug 22, 26, 28 2017 as the caption says; box on the kilonova beside the galaxy core |
| 30 | fig:b3:origin-of-elements:g-dwarf | 347 | fixed | ok | 6670 GCS irfm stars and 902 of at most 1 Msun in 0.1-dex bins; closed box (mu 0.291) scaled to 6670; 26 stars below -1 in both samples; first build: bar legend entries drawn as dashed lines: area legend |
| 30 | fig:b3:origin-of-elements:alpha | 348 | ok | ok | two-phase model, plateau 0.4 to the knee at -1 then down to 0 at [Fe/H] 0 (x_sun 3.98, K 2.02; Ia share 0.602 tested); the model continues to [Fe/H] 0.2 below zero as drawn; labels clear |

## Phase C full pass (2026-10-23)

Every figure object of the final build re-checked on its own page at 130 dpi (zoomed at 200 to 300 dpi where lines are thin), for layout and for the science; `page` is the PDF page of the 456-page build after the fixes. Fixed figures were re-rendered from the rebuilt PDF and checked again.

| ch | figure | page | layout | science | note |
|---|---|---|---|---|---|
| 1 | fig:b3:seismology-imaging:shells | 15 | ok | ok |  |
| 1 | fig:b3:seismology-imaging:rays | 17 | fixed | ok | "outer core" touched the core circle: label moved inside the shell |
| 1 | fig:b3:seismology-imaging:tt | 18 | ok | ok |  |
| 1 | fig:b3:seismology-imaging:particle-motion | 19 | ok | ok |  |
| 1 | fig:b3:seismology-imaging:love | 20 | ok | ok |  |
| 1 | fig:b3:seismology-imaging:inverse-loop | 23 | ok | ok |  |
| 1 | fig:b3:seismology-imaging:checkerboard | 25 | ok | ok |  |
| 1 | fig:b3:seismology-imaging:tradeoff | 25 | ok | ok |  |
| 1 | b3-seismic-vault.jpg | 26 | ok | ok |  |
| 2 | fig:b3:exploration-seismology:refraction | 31 | ok | ok |  |
| 2 | fig:b3:exploration-seismology:synthetic | 33 | ok | ok |  |
| 2 | fig:b3:exploration-seismology:wedge | 34 | ok | ok |  |
| 2 | fig:b3:exploration-seismology:fresnel | 34 | ok | ok |  |
| 2 | fig:b3:exploration-seismology:cmp | 35 | ok | ok |  |
| 2 | fig:b3:exploration-seismology:gather | 37 | ok | ok |  |
| 2 | fig:b3:exploration-seismology:velocities | 37 | ok | ok |  |
| 2 | fig:b3:exploration-seismology:vibroseis | 38 | ok | ok |  |
| 2 | fig:b3:exploration-seismology:migration | 39 | ok | ok |  |
| 2 | fig:b3:exploration-seismology:terminations | 39 | ok | ok |  |
| 2 | b3-streamer-vessel.jpg | 40 | ok | ok |  |
| 3 | fig:b3:gravity-geodesy:equipotential | 45 | fixed | ok | the rotation axis crossed "attraction": label anchored right of the axis |
| 3 | fig:b3:gravity-geodesy:hydrostatic | 47 | ok | ok |  |
| 3 | fig:b3:gravity-geodesy:grace | 49 | ok | ok |  |
| 3 | fig:b3:gravity-geodesy:grace-photo | 49 | ok | ok |  |
| 3 | fig:b3:gravity-geodesy:ice-mass | 50 | ok | ok |  |
| 3 | fig:b3:gravity-geodesy:flexure | 52 | ok | ok |  |
| 3 | fig:b3:gravity-geodesy:moat | 53 | ok | ok |  |
| 3 | b3-gravimeter.jpg | 53 | ok | ok |  |
| 4 | fig:b3:palaeomagnetism:elements | 58 | ok | ok |  |
| 4 | fig:b3:palaeomagnetism:igrf-maps | 59 | ok | ok |  |
| 4 | fig:b3:palaeomagnetism:dipole | 60 | ok | ok |  |
| 4 | fig:b3:palaeomagnetism:zijderveld | 62 | ok | ok |  |
| 4 | fig:b3:palaeomagnetism:vgp | 63 | fixed | ok | the D label sat on its angle arc: arc shortened, label moved out |
| 4 | fig:b3:palaeomagnetism:apw | 64 | fixed | ok | the Kesta C triangle had no label: C added beside it |
| 4 | fig:b3:palaeomagnetism:magstrat | 65 | ok | ok |  |
| 4 | b3-palaeomag-lab.jpg | 66 | ok | ok |  |
| 5 | fig:b3:lithosphere-thermal-models:columns | 72 | ok | ok |  |
| 5 | fig:b3:lithosphere-thermal-models:isotherms | 74 | ok | fixed | the 1000 and 1400 labels sat between isotherms, next to the wrong ones: placed on their own lines (computed depths at 28 and 22 Myr) |
| 5 | fig:b3:lithosphere-thermal-models:depth-age | 75 | ok | ok |  |
| 5 | fig:b3:lithosphere-thermal-models:geotherms | 76 | ok | ok |  |
| 5 | b3-heatflow-probe.jpg | 77 | ok | ok |  |
| 6 | fig:b3:mantle-convection:cell | 81 | ok | ok |  |
| 6 | fig:b3:mantle-convection:scaling | 83 | ok | ok |  |
| 6 | fig:b3:mantle-convection:forces | 84 | ok | ok |  |
| 6 | fig:b3:mantle-convection:ridge-push | 85 | ok | ok |  |
| 6 | fig:b3:mantle-convection:plume | 86 | ok | ok |  |
| 6 | fig:b3:mantle-convection:gia | 87 | ok | ok |  |
| 6 | b3-raised-beach-malin.jpg | 88 | ok | ok |  |
| 7 | fig:b3:deformation-mechanisms:dislocation | 93 | ok | ok |  |
| 7 | fig:b3:deformation-mechanisms:diffusion | 94 | ok | ok |  |
| 7 | fig:b3:deformation-mechanisms:flow-laws | 95 | ok | ok |  |
| 7 | fig:b3:deformation-mechanisms:map | 96 | ok | ok |  |
| 7 | fig:b3:deformation-mechanisms:kinematic | 97 | ok | ok |  |
| 7 | b3-deformation-press.jpg | 98 | ok | ok |  |
| 7 | b3-augen-mylonite.jpg | 98 | ok | ok |  |
| 8 | fig:b3:structural-analysis:geometry | 103 | ok | ok |  |
| 8 | fig:b3:structural-analysis:nets | 104 | ok | ok |  |
| 8 | fig:b3:structural-analysis:pi | 106 | ok | ok |  |
| 8 | fig:b3:structural-analysis:fry | 107 | ok | ok |  |
| 8 | fig:b3:structural-analysis:flinn | 107 | ok | ok |  |
| 8 | fig:b3:structural-analysis:faults | 109 | ok | ok |  |
| 8 | fig:b3:structural-analysis:restoration | 110 | ok | ok |  |
| 8 | b3-compass-clinometer.jpg | 111 | ok | ok |  |
| 9 | fig:b3:extension-strike-slip:models | 116 | fixed | ok | "shear zone" sat on the shear zone: moved to the lower plate side |
| 9 | fig:b3:extension-strike-slip:domino | 117 | ok | ok |  |
| 9 | fig:b3:extension-strike-slip:rollover | 118 | ok | ok |  |
| 9 | fig:b3:extension-strike-slip:core | 119 | ok | ok |  |
| 9 | fig:b3:extension-strike-slip:strike-slip | 120 | fixed | ok | the restraining-step arrow ran through the panel label: moved up onto the fault |
| 9 | b3-basin-and-range.jpg | 121 | ok | ok |  |
| 10 | fig:b3:orogenic-wedges:thrusts | 125 | ok | ok |  |
| 10 | fig:b3:orogenic-wedges:duplex | 126 | ok | ok |  |
| 10 | fig:b3:orogenic-wedges:wedge | 126 | ok | ok |  |
| 10 | fig:b3:orogenic-wedges:taper | 127 | ok | ok |  |
| 10 | b3-sandbox-lab.jpg | 128 | ok | ok |  |
| 10 | fig:b3:orogenic-wedges:age-elevation | 130 | ok | ok |  |
| 11 | fig:b3:petrological-thermodynamics:gasp | 136 | ok | ok |  |
| 11 | fig:b3:petrological-thermodynamics:schreinemakers | 138 | ok | ok |  |
| 11 | fig:b3:petrological-thermodynamics:solvus | 139 | ok | ok |  |
| 11 | b3-petrology-desk.jpg | 140 | ok | ok |  |
| 12 | fig:b3:trace-element-modelling:curves | 146 | ok | ok |  |
| 12 | fig:b3:trace-element-modelling:modes | 147 | ok | ok |  |
| 12 | fig:b3:trace-element-modelling:ree | 148 | ok | ok |  |
| 12 | fig:b3:trace-element-modelling:ratios | 149 | ok | ok |  |
| 13 | fig:b3:advanced-geochronology:concordia | 154 | ok | ok |  |
| 13 | b3-mass-spec-lab.jpg | 155 | ok | ok |  |
| 13 | fig:b3:advanced-geochronology:spectrum | 156 | ok | ok |  |
| 13 | fig:b3:advanced-geochronology:model-age | 157 | ok | ok |  |
| 13 | fig:b3:advanced-geochronology:low-t | 158 | ok | ok |  |
| 14 | fig:b3:stable-isotopes:rayleigh | 166 | ok | ok |  |
| 14 | fig:b3:stable-isotopes:lr04 | 167 | ok | ok |  |
| 14 | fig:b3:stable-isotopes:carbon | 168 | ok | ok |  |
| 14 | fig:b3:stable-isotopes:three-isotope | 169 | ok | ok |  |
| 14 | b3-ice-core-tent.jpg | 169 | ok | ok |  |
| 15 | fig:b3:water-rock-interaction:calcite | 175 | fixed | ok | "ground waters" crossed by the 10 C open curve, "outlet" on the SI line: both moved |
| 15 | b3-palette-spring-travertine.jpg | 176 | ok | ok |  |
| 15 | fig:b3:water-rock-interaction:rates | 177 | ok | ok |  |
| 15 | fig:b3:water-rock-interaction:activity | 178 | ok | ok |  |
| 15 | fig:b3:water-rock-interaction:box | 179 | ok | ok |  |
| 16 | fig:b3:sequence-stratigraphy:anatomy | 185 | ok | ok |  |
| 16 | fig:b3:sequence-stratigraphy:stacking | 186 | ok | ok |  |
| 16 | b3-book-cliffs-helper.jpg | 186 | ok | ok |  |
| 16 | fig:b3:sequence-stratigraphy:series | 187 | ok | ok |  |
| 16 | fig:b3:sequence-stratigraphy:section | 187 | ok | ok |  |
| 16 | fig:b3:sequence-stratigraphy:periodogram | 188 | ok | ok |  |
| 17 | fig:b3:facies-models:walther | 194 | ok | ok |  |
| 17 | fig:b3:facies-models:rivers | 195 | ok | ok |  |
| 17 | fig:b3:facies-models:shoreface | 195 | ok | ok |  |
| 17 | b3-hummocky-cross-stratification.jpg | 196 | ok | ok |  |
| 17 | fig:b3:facies-models:deep | 197 | ok | ok |  |
| 17 | fig:b3:facies-models:platforms | 197 | ok | ok |  |
| 17 | fig:b3:facies-models:logs | 199 | ok | ok |  |
| 17 | b3-core-store.jpg | 199 | ok | ok |  |
| 18 | fig:b3:quantitative-geomorphology:hillslope | 204 | ok | ok |  |
| 18 | fig:b3:quantitative-geomorphology:regimes | 206 | ok | ok |  |
| 18 | fig:b3:quantitative-geomorphology:profile | 206 | ok | ok |  |
| 18 | fig:b3:quantitative-geomorphology:knick | 208 | ok | ok |  |
| 18 | b3-niagara-gorge.jpg | 209 | ok | ok |  |
| 18 | fig:b3:quantitative-geomorphology:rebound | 210 | ok | ok |  |
| 19 | fig:b3:gfd-foundations:frame | 215 | fixed | ok | the component labels overlapped the rotation vector and the tangent line: redrawn at 30 deg with components computed (Omega sin, Omega cos), labels clear |
| 19 | fig:b3:gfd-foundations:inertial | 217 | ok | ok |  |
| 19 | fig:b3:gfd-foundations:taylor | 218 | ok | ok |  |
| 19 | fig:b3:gfd-foundations:buoyancy | 219 | ok | ok |  |
| 19 | fig:b3:gfd-foundations:geometry | 220 | ok | ok |  |
| 19 | fig:b3:gfd-foundations:jets | 221 | ok | ok |  |
| 19 | b3-rotating-tank.jpg | 222 | ok | ok |  |
| 20 | fig:b3:atmospheric-dynamics:restoring | 227 | ok | ok |  |
| 20 | fig:b3:atmospheric-dynamics:rossby | 228 | ok | ok |  |
| 20 | fig:b3:atmospheric-dynamics:eady | 230 | ok | ok |  |
| 20 | fig:b3:atmospheric-dynamics:heatflux | 231 | ok | ok |  |
| 20 | fig:b3:atmospheric-dynamics:held-hou | 232 | ok | ok |  |
| 21 | fig:b3:ocean-dynamics:pumping | 237 | ok | ok |  |
| 21 | fig:b3:ocean-dynamics:sverdrup | 239 | ok | ok |  |
| 21 | fig:b3:ocean-dynamics:boundary | 240 | ok | ok |  |
| 21 | fig:b3:ocean-dynamics:stommel-arons | 242 | ok | ok |  |
| 21 | b3-argo-deploy.jpg | 243 | ok | ok |  |
| 21 | fig:b3:ocean-dynamics:equilibrium-tide | 244 | ok | ok |  |
| 21 | fig:b3:ocean-dynamics:amphidromes | 245 | fixed | ok | y axis read only "(km)": now "across (km)" |
| 22 | fig:b3:climate-models:zero-d | 251 | ok | ok |  |
| 22 | fig:b3:climate-models:budyko | 253 | ok | ok |  |
| 22 | fig:b3:climate-models:two-layer | 254 | ok | ok |  |
| 22 | fig:b3:climate-models:grid | 255 | ok | ok |  |
| 22 | fig:b3:climate-models:ladder | 256 | ok | ok |  |
| 22 | fig:b3:climate-models:supercomputer | 256 | ok | ok |  |
| 22 | b3-model-centre.jpg | 257 | ok | ok |  |
| 23 | fig:b3:hydrogeology:head | 262 | ok | ok |  |
| 23 | fig:b3:hydrogeology:aquifers | 264 | ok | ok |  |
| 23 | fig:b3:hydrogeology:flow-net | 265 | ok | ok |  |
| 23 | fig:b3:hydrogeology:theis | 266 | ok | ok |  |
| 23 | fig:b3:hydrogeology:cone | 267 | ok | ok |  |
| 23 | b3-pumping-test.jpg | 267 | ok | ok |  |
| 23 | fig:b3:hydrogeology:transport | 268 | ok | ok |  |
| 24 | fig:b3:glaciology:flow | 274 | ok | ok |  |
| 24 | fig:b3:glaciology:zones | 275 | ok | fixed | flow lines ran above the ice surface and below the bed, ablation arrows started under the surface: flow lines recomputed inside the ice (sinking in the accumulation zone, rising in the ablation zone), arrows set on the computed surface |
| 24 | fig:b3:glaciology:grounding | 276 | ok | ok |  |
| 24 | fig:b3:glaciology:outlet | 277 | ok | ok |  |
| 24 | b3-glaciology-camp.jpg | 278 | ok | ok |  |
| 24 | fig:b3:glaciology:sea-ice | 279 | ok | ok |  |
| 25 | fig:b3:remote-sensing-gis:spectra | 284 | ok | ok |  |
| 25 | fig:b3:remote-sensing-gis:thermal | 286 | ok | ok |  |
| 25 | fig:b3:remote-sensing-gis:sar | 287 | ok | ok |  |
| 25 | fig:b3:remote-sensing-gis:insar | 289 | ok | ok |  |
| 25 | fig:b3:remote-sensing-gis:three-sisters | 290 | ok | ok |  |
| 25 | b3-ground-station.jpg | 290 | ok | ok |  |
| 25 | fig:b3:remote-sensing-gis:raster-vector | 291 | ok | ok |  |
| 25 | fig:b3:remote-sensing-gis:varden | 292 | fixed | ok | the aspect colour bar rendered with zero width (axis equal image inherited by the colour bar): axis equal=false in both colour bars; aspect bar N-E-S-W-N checked |
| 26 | fig:b3:planetary-interiors-surfaces:two-layer | 298 | ok | ok |  |
| 26 | fig:b3:planetary-interiors-surfaces:craters | 299 | ok | ok |  |
| 26 | fig:b3:planetary-interiors-surfaces:barringer | 299 | ok | ok |  |
| 26 | fig:b3:planetary-interiors-surfaces:sfd | 301 | ok | ok |  |
| 26 | fig:b3:planetary-interiors-surfaces:lids | 302 | ok | fixed | the mobile-lid slab descended from the middle of a plate: it now sinks from the leading edge of the right-hand plate, under the trench |
| 26 | fig:b3:planetary-interiors-surfaces:olympus | 303 | ok | ok |  |
| 27 | fig:b3:planetary-atmospheres:structure | 309 | ok | ok |  |
| 27 | fig:b3:planetary-atmospheres:jeans | 311 | fixed | ok | the Titan line crossed "hydrodynamic": label moved to the right of the band |
| 27 | fig:b3:planetary-atmospheres:runaway | 313 | ok | ok |  |
| 27 | fig:b3:planetary-atmospheres:valleys | 314 | ok | ok |  |
| 27 | fig:b3:planetary-atmospheres:ligeia | 315 | ok | ok |  |
| 27 | fig:b3:planetary-atmospheres:phases | 315 | ok | ok |  |
| 27 | fig:b3:planetary-atmospheres:hz | 316 | ok | ok |  |
| 28 | fig:b3:exoplanets:rv | 322 | ok | ok |  |
| 28 | fig:b3:exoplanets:transit | 324 | ok | ok |  |
| 28 | fig:b3:exoplanets:hip65426 | 325 | ok | ok |  |
| 28 | fig:b3:exoplanets:microlensing | 326 | ok | ok |  |
| 28 | fig:b3:exoplanets:methods | 327 | ok | ok |  |
| 28 | fig:b3:exoplanets:valley | 328 | ok | ok |  |
| 28 | fig:b3:exoplanets:mass-radius | 329 | ok | ok |  |
| 29 | fig:b3:milky-way-galaxies:panorama | 335 | ok | ok |  |
| 29 | fig:b3:milky-way-galaxies:sketch | 336 | ok | ok |  |
| 29 | fig:b3:milky-way-galaxies:tangent | 338 | ok | ok |  |
| 29 | fig:b3:milky-way-galaxies:rotation | 339 | ok | ok |  |
| 29 | fig:b3:milky-way-galaxies:mass | 341 | ok | ok |  |
| 29 | fig:b3:milky-way-galaxies:fork | 342 | ok | ok |  |
| 29 | fig:b3:milky-way-galaxies:m101 | 342 | ok | ok |  |
| 29 | fig:b3:milky-way-galaxies:leavitt | 344 | ok | ok |  |
| 29 | fig:b3:milky-way-galaxies:ladder-rungs | 345 | ok | fixed | caption said each rung is calibrated where it overlaps the one below, but parallaxes and Cepheids do not overlap on the plot: reworded to the objects both rungs measure |
| 30 | fig:b3:origin-of-elements:curve | 351 | ok | ok |  |
| 30 | fig:b3:origin-of-elements:sun-ci | 352 | ok | ok |  |
| 30 | fig:b3:origin-of-elements:crab | 353 | ok | ok |  |
| 30 | fig:b3:origin-of-elements:chart | 354 | ok | ok |  |
| 30 | fig:b3:origin-of-elements:sigma-n | 356 | ok | ok |  |
| 30 | fig:b3:origin-of-elements:kilonova | 358 | ok | ok |  |
| 30 | fig:b3:origin-of-elements:g-dwarf | 359 | ok | fixed | the closed box put about a tenth of its stars above the present gas metallicity (to +0.6): frac_below capped at [Fe/H] = 0 in chemical_evolution.py, test added, caption states it; the 16 % below -1 unchanged |
| 30 | fig:b3:origin-of-elements:alpha | 360 | ok | ok |  |
| 31 | fig:b3:field-lab-methods-3:survey | 368 | ok | ok |  |
| 31 | fig:b3:field-lab-methods-3:profile | 369 | ok | ok |  |
| 31 | fig:b3:field-lab-methods-3:magnetic | 370 | fixed | ok | the legends hid both peaks: ymax raised (28, 40), right legend moved to the upper left |
| 31 | fig:b3:field-lab-methods-3:arrays | 372 | fixed | ok | the array titles overlapped the spacing arrows: set to the left of each section |
| 31 | fig:b3:field-lab-methods-3:ves | 373 | fixed | ok | "k = 0.9" sat on the top curve: moved under it |
| 31 | fig:b3:field-lab-methods-3:radargram | 375 | ok | ok |  |
| 31 | b3-geophysics-crew.jpg | 376 | ok | ok |  |

## Main-session verification (2026-10-23)

15 PDF pages rendered at 130 dpi: 17, 45, 64, 74, 104, 116, 175, 215, 245, 266, 275, 302, 345, 359, 370 (pages from 302 on are before the reflow fix).

| ch | figure | page | layout | science | note |
|---|---|---|---|---|---|
| 15 | fig:b3:water-rock-interaction:calcite (b) | 175 | ok | fixed | The caption said "read from right to left". The axis is reversed (`x dir=reverse`), so degassing runs from the outlet (left) to air (right). The caption now reads "read from left to right, on a reversed axis". |
| 26 | fig:b3:planetary-interiors-surfaces:olympus | 302 | fixed | ok | The photo (0.58\linewidth) did not fit and was pushed to the next page, leaving PDF p. 302 about 45 % blank. It is now 0.48\linewidth and sits on p. 302. The book is 455 pp; later pages shift by one. |
| 4 | fig:b3:palaeomagnetism:vgp | 64 | fixed | ok | The Kesta C pole was labelled "C" with no age, while A and B carry theirs. It is now "C, 4". |
| 1, 3, 5, 8, 9, 19, 21, 23, 24, 29, 30, 31 | the other sampled pages | | ok | ok | Values checked: dyke peak 15.9 nT and half-width ±z; M2 half-wavelength 495 km at 50 m; f(45°) = 1.031e-4; plate heat flow 47 mW/m²; distance-ladder bars against 4 kpc, LMC–45 Mpc and 96–616 Mpc; closed box 16.38 %; Kelvin waves keep the coast on their right; NH amphidromes turn anticlockwise. |
