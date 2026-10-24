# Data ledger --- One Earth and Space Sciences Book (shared rows)

Every number the books quote about the real Earth, its oceans and atmosphere, the
planets, the Sun or the stars (a radius, a plate speed, a heat flow, a CO2
concentration, a period boundary, a magnitude) has a row in a ledger, with its
source and the date the source was read. **A value with no row is not printed.**
A chapter that uses a row says so in a source comment, `% ledger: <id>[, <id>...]`,
next to the first use (free text after `(` or `;`).

The ledger is split so that books written at the same time never edit the same file:

- **this file** holds the rows every book shares: fundamental constants (`const:`),
  the Earth, Sun and planets from the NASA fact sheets (`earth:`, `air:`, `sun:`,
  `planet:<Body>.<property>`), the international time scale (`ics:base.<unit>`,
  `ics:colour.<unit>`), the shared datasets of `tools/fetch_data.py` (`data:`) and
  the exercise region (`region:`). Book agents treat it as read-only; a missing
  shared value is reported to the main session.
- **`sources/ledger/book<N>.md`** holds each book's own rows, with its own Sources
  table. A book may cite another book's row (read-only) rather than duplicate it.

Row ids are unique across all ledger files; `tools/check_ledger.py` checks every
`% ledger:` id, every row's source key and access date.

Numbers a book *computes* (a mean, a trend, a speed from a distance and an age) are
computed from rows or datasets in a `figdata/` script, never typed. Values invented
for an exercise are data of the exercise and need no row; values presented as facts
about the world do. **Volatile values** (the latest annual CO2, the warmest year) are
printed in a `dated` box whose year matches the row. Climate statements with a
calibrated likelihood or confidence (*very likely*, *high confidence*) cite the IPCC
report chapter and section in a book row.

## Sources

| key | source | URL |
|---|---|---|
| CODATA-2022 | NIST, CODATA 2022 recommended values of the fundamental physical constants (ASCII table) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt |
| SI-2019 | BIPM, The International System of Units, 9th edition (2019, updated 2022), Table 8 (non-SI units accepted for use with the SI) | https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf |
| NASA-EARTH | NASA NSSDCA, Earth Fact Sheet (D. R. Williams) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html |
| NASA-SUN | NASA NSSDCA, Sun Fact Sheet (D. R. Williams) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html |
| NASA-PLANETS | NASA NSSDCA, Planetary Fact Sheet - Metric (D. R. Williams); Moon values marked * there are about the Earth | https://nssdc.gsfc.nasa.gov/planetary/factsheet/ |
| ICS-2026-06 | International Commission on Stratigraphy, International Chronostratigraphic Chart, machine-readable version 2026-06 (chart.ttl, CC BY 4.0), checked against the printed chart v2024/12; colours follow the CGMW | https://github.com/i-c-stratigraphy/chart (PDF: https://stratigraphy.org/ICSchart/ChronostratChart2024-12.pdf) |
| NATURAL-EARTH | Natural Earth, public domain vector data, physical layer ne_*_land (GeoJSON mirror nvkelso/natural-earth-vector) | https://www.naturalearthdata.com/ |
| PB2002 | P. Bird, An updated digital model of plate boundaries, Geochem. Geophys. Geosyst. 4(3), 1027 (2003); GeoJSON by H. Ahlenius, fraxen/tectonicplates, ODC-By 1.0 (credit in the caption) | https://github.com/fraxen/tectonicplates |
| ETOPO1 | C. Amante and B. W. Eakins, ETOPO1 1 Arc-Minute Global Relief Model, NOAA Technical Memorandum NESDIS NGDC-24 (2009); sampled every 60th node by NOAA CoastWatch ERDDAP (dataset etopo180) | https://coastwatch.pfeg.noaa.gov/erddap/griddap/etopo180.html |
| USGS-COMCAT | U.S. Geological Survey, ANSS Comprehensive Earthquake Catalog (ComCat), FDSN event web service, query in data/MANIFEST.md | https://earthquake.usgs.gov/fdsnws/event/1/ |
| GVP | Global Volcanism Program, Volcanoes of the World (Smithsonian Institution), Holocene volcano list via the GVP web feature service; positions and types only | https://volcano.si.edu/ |
| PREM | A. M. Dziewonski and D. L. Anderson, Preliminary reference Earth model, Phys. Earth Planet. Inter. 25, 297-356 (1981); isotropic 1 s tabulation from ObsPy's TauP model file prem.nd | https://github.com/obspy/obspy/blob/master/obspy/taup/data/prem.nd |
| NOAA-GML | NOAA Global Monitoring Laboratory (X. Lan, P. Tans, K. W. Thoning) and Scripps Institution of Oceanography (R. F. Keeling): Mauna Loa CO2 monthly and annual means | https://gml.noaa.gov/ccgg/trends/data.html |
| GISTEMP | GISTEMP Team, GISS Surface Temperature Analysis (GISTEMP) v4, NASA Goddard Institute for Space Studies; Lenssen et al., J. Geophys. Res. Atmos. 124, 6307 (2019) | https://data.giss.nasa.gov/gistemp/ |
| BEREITER-2015 | B. Bereiter et al., Revision of the EPICA Dome C CO2 record from 800 to 600 kyr before present, Geophys. Res. Lett. 42, 542 (2015): Antarctic composite, NOAA NCEI Paleoclimatology | https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/antarctica2015co2composite.txt |
| JOUZEL-2007 | J. Jouzel et al., Orbital and millennial Antarctic climate variability over the past 800,000 years, Science 317, 793 (2007): EPICA Dome C deuterium and temperature, NOAA NCEI Paleoclimatology | https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/epica_domec/edc3deuttemp2007.txt |
| LR04 | L. E. Lisiecki and M. E. Raymo, A Pliocene-Pleistocene stack of 57 globally distributed benthic d18O records, Paleoceanography 20, PA1003 (2005), NOAA NCEI Paleoclimatology | https://www.ncei.noaa.gov/pub/data/paleo/contributions_by_author/lisiecki2005/lisiecki2005.txt |
| NOAA-LSA | NOAA Laboratory for Satellite Altimetry, global mean sea level, TOPEX/Poseidon and Jason-1/2/3, Sentinel-6MF (acknowledgment: Altimetry data are provided by NOAA Laboratory for Satellite Altimetry) | https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/ |
| WEBSEARCH | exact-phrase web search, results recorded in the row | - |

## Rows

| id | quantity | value | unit | source | accessed |
|---|---|---|---|---|---|
| const:G | Newtonian constant of gravitation G (standard uncertainty 0.000 15 e-11) | 6.67430e-11 | m^3 kg^-1 s^-2 | CODATA-2022 | 2026-10-22 |
| const:c | speed of light in vacuum c (exact) | 299792458 | m s^-1 | CODATA-2022 | 2026-10-22 |
| const:h | Planck constant h (exact) | 6.62607015e-34 | J Hz^-1 | CODATA-2022 | 2026-10-22 |
| const:kB | Boltzmann constant k (exact) | 1.380649e-23 | J K^-1 | CODATA-2022 | 2026-10-22 |
| const:sigma | Stefan-Boltzmann constant sigma (exact) | 5.670374419...e-8 | W m^-2 K^-4 | CODATA-2022 | 2026-10-22 |
| const:NA | Avogadro constant N_A (exact) | 6.02214076e23 | mol^-1 | CODATA-2022 | 2026-10-22 |
| const:R | molar gas constant R (exact) | 8.314462618... | J mol^-1 K^-1 | CODATA-2022 | 2026-10-22 |
| const:e | elementary charge e (exact) | 1.602176634e-19 | C | CODATA-2022 | 2026-10-22 |
| const:gn | standard acceleration of gravity g_n (conventional) (exact) | 9.80665 | m s^-2 | CODATA-2022 | 2026-10-22 |
| const:b | Wien wavelength displacement constant b (exact) | 2.897771955...e-3 | m K | CODATA-2022 | 2026-10-22 |
| earth:mass | mass of the Earth (NASA Earth fact sheet) | 5.9722 | 1e24 kg | NASA-EARTH | 2026-10-22 |
| earth:Req | equatorial radius (NASA Earth fact sheet) | 6378.137 | km | NASA-EARTH | 2026-10-22 |
| earth:Rpol | polar radius (NASA Earth fact sheet) | 6356.752 | km | NASA-EARTH | 2026-10-22 |
| earth:Rmean | volumetric mean radius (NASA Earth fact sheet) | 6371.000 | km | NASA-EARTH | 2026-10-22 |
| earth:Rcore | radius of the core (NASA Earth fact sheet) | 3485 | km | NASA-EARTH | 2026-10-22 |
| earth:flattening | flattening (NASA Earth fact sheet) | 0.003353 | - | NASA-EARTH | 2026-10-22 |
| earth:density | mean density (NASA Earth fact sheet) | 5513 | kg/m3 | NASA-EARTH | 2026-10-22 |
| earth:gmean | mean surface gravity (NASA Earth fact sheet) | 9.820 | m/s2 | NASA-EARTH | 2026-10-22 |
| earth:geq | surface acceleration at the equator (NASA Earth fact sheet) | 9.780 | m/s2 | NASA-EARTH | 2026-10-22 |
| earth:gpole | surface acceleration at the poles (NASA Earth fact sheet) | 9.832 | m/s2 | NASA-EARTH | 2026-10-22 |
| earth:GM | GM of the Earth (NASA Earth fact sheet) | 0.39860 | 1e6 km3/s2 | NASA-EARTH | 2026-10-22 |
| earth:albedo | Bond albedo (NASA Earth fact sheet) | 0.294 | - | NASA-EARTH | 2026-10-22 |
| earth:TSI | solar irradiance at 1 au (total solar irradiance) (NASA Earth fact sheet) | 1361.0 | W/m2 | NASA-EARTH | 2026-10-22 |
| earth:Tbb | black-body (effective) temperature (NASA Earth fact sheet) | 254.0 | K | NASA-EARTH | 2026-10-22 |
| earth:topo | topographic range (NASA Earth fact sheet) | 20.4 | km | NASA-EARTH | 2026-10-22 |
| earth:MoI | moment of inertia factor I/(MR^2) (NASA Earth fact sheet) | 0.3308 | - | NASA-EARTH | 2026-10-22 |
| earth:J2 | J2 (NASA Earth fact sheet) | 1082.63 | 1e-6 | NASA-EARTH | 2026-10-22 |
| earth:a | semimajor axis of the orbit (NASA Earth fact sheet) | 149.598 | 1e6 km | NASA-EARTH | 2026-10-22 |
| earth:Psid | sidereal orbit period (NASA Earth fact sheet) | 365.256 | days | NASA-EARTH | 2026-10-22 |
| earth:Ptrop | tropical year (NASA Earth fact sheet) | 365.242 | days | NASA-EARTH | 2026-10-22 |
| earth:peri | perihelion distance (NASA Earth fact sheet) | 147.095 | 1e6 km | NASA-EARTH | 2026-10-22 |
| earth:aph | aphelion distance (NASA Earth fact sheet) | 152.100 | 1e6 km | NASA-EARTH | 2026-10-22 |
| earth:vorb | mean orbital velocity (NASA Earth fact sheet) | 29.78 | km/s | NASA-EARTH | 2026-10-22 |
| earth:ecc | orbit eccentricity (NASA Earth fact sheet) | 0.0167 | - | NASA-EARTH | 2026-10-22 |
| earth:Trot | sidereal rotation period (NASA Earth fact sheet) | 23.9345 | h | NASA-EARTH | 2026-10-22 |
| earth:obliquity | obliquity (NASA Earth fact sheet) | 23.44 | deg | NASA-EARTH | 2026-10-22 |
| earth:psurf | mean surface pressure (NASA Earth fact sheet) | 1014 | hPa (mb) | NASA-EARTH | 2026-10-22 |
| earth:Hscale | atmospheric scale height (NASA Earth fact sheet) | 8.5 | km | NASA-EARTH | 2026-10-22 |
| earth:Tsurf | average surface temperature (NASA Earth fact sheet) | 288 | K | NASA-EARTH | 2026-10-22 |
| earth:Mmol | mean molecular weight of air (NASA Earth fact sheet) | 28.97 | g/mol | NASA-EARTH | 2026-10-22 |
| earth:Matm | total mass of the atmosphere (NASA Earth fact sheet) | 5.1e18 | kg | NASA-EARTH | 2026-10-22 |
| earth:Mhyd | total mass of the hydrosphere (NASA Earth fact sheet) | 1.4e21 | kg | NASA-EARTH | 2026-10-22 |
| air:N2 | N2 in dry air, by volume (NASA Earth fact sheet) | 78.08 | % | NASA-EARTH | 2026-10-22 |
| air:O2 | O2 in dry air, by volume (NASA Earth fact sheet) | 20.95 | % | NASA-EARTH | 2026-10-22 |
| air:Ar | argon in dry air, by volume (NASA Earth fact sheet) | 9340 | ppm | NASA-EARTH | 2026-10-22 |
| sun:mass | mass of the Sun (NASA Sun fact sheet) | 1988400 | 1e24 kg | NASA-SUN | 2026-10-22 |
| sun:R | radius of the Sun (NASA Sun fact sheet) | 695700 | km | NASA-SUN | 2026-10-22 |
| sun:density | mean density of the Sun (NASA Sun fact sheet) | 1408 | kg/m3 | NASA-SUN | 2026-10-22 |
| sun:L | luminosity of the Sun (NASA Sun fact sheet) | 382.8 | 1e24 W | NASA-SUN | 2026-10-22 |
| sun:Mabs | absolute magnitude of the Sun (NASA Sun fact sheet) | +4.83 | - | NASA-SUN | 2026-10-22 |
| sun:massloss | mass conversion rate of the Sun (NASA Sun fact sheet) | 4260 | 1e6 kg/s | NASA-SUN | 2026-10-22 |
| planet:Mercury.mass | mass of Mercury (NASA planetary fact sheet) | 0.330 | 1e24 kg | NASA-PLANETS | 2026-10-22 |
| planet:Venus.mass | mass of Venus (NASA planetary fact sheet) | 4.87 | 1e24 kg | NASA-PLANETS | 2026-10-22 |
| planet:Earth.mass | mass of Earth (NASA planetary fact sheet) | 5.97 | 1e24 kg | NASA-PLANETS | 2026-10-22 |
| planet:Moon.mass | mass of Moon (NASA planetary fact sheet) | 0.073 | 1e24 kg | NASA-PLANETS | 2026-10-22 |
| planet:Mars.mass | mass of Mars (NASA planetary fact sheet) | 0.642 | 1e24 kg | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.mass | mass of Jupiter (NASA planetary fact sheet) | 1898 | 1e24 kg | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.mass | mass of Saturn (NASA planetary fact sheet) | 568 | 1e24 kg | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.mass | mass of Uranus (NASA planetary fact sheet) | 86.8 | 1e24 kg | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.mass | mass of Neptune (NASA planetary fact sheet) | 102 | 1e24 kg | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.mass | mass of Pluto (NASA planetary fact sheet) | 0.0130 | 1e24 kg | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.diameter | diameter of Mercury (NASA planetary fact sheet) | 4879 | km | NASA-PLANETS | 2026-10-22 |
| planet:Venus.diameter | diameter of Venus (NASA planetary fact sheet) | 12104 | km | NASA-PLANETS | 2026-10-22 |
| planet:Earth.diameter | diameter of Earth (NASA planetary fact sheet) | 12756 | km | NASA-PLANETS | 2026-10-22 |
| planet:Moon.diameter | diameter of Moon (NASA planetary fact sheet) | 3475 | km | NASA-PLANETS | 2026-10-22 |
| planet:Mars.diameter | diameter of Mars (NASA planetary fact sheet) | 6792 | km | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.diameter | diameter of Jupiter (NASA planetary fact sheet) | 142984 | km | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.diameter | diameter of Saturn (NASA planetary fact sheet) | 120536 | km | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.diameter | diameter of Uranus (NASA planetary fact sheet) | 51118 | km | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.diameter | diameter of Neptune (NASA planetary fact sheet) | 49528 | km | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.diameter | diameter of Pluto (NASA planetary fact sheet) | 2376 | km | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.density | density of Mercury (NASA planetary fact sheet) | 5429 | kg/m3 | NASA-PLANETS | 2026-10-22 |
| planet:Venus.density | density of Venus (NASA planetary fact sheet) | 5243 | kg/m3 | NASA-PLANETS | 2026-10-22 |
| planet:Earth.density | density of Earth (NASA planetary fact sheet) | 5514 | kg/m3 | NASA-PLANETS | 2026-10-22 |
| planet:Moon.density | density of Moon (NASA planetary fact sheet) | 3340 | kg/m3 | NASA-PLANETS | 2026-10-22 |
| planet:Mars.density | density of Mars (NASA planetary fact sheet) | 3934 | kg/m3 | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.density | density of Jupiter (NASA planetary fact sheet) | 1326 | kg/m3 | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.density | density of Saturn (NASA planetary fact sheet) | 687 | kg/m3 | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.density | density of Uranus (NASA planetary fact sheet) | 1270 | kg/m3 | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.density | density of Neptune (NASA planetary fact sheet) | 1638 | kg/m3 | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.density | density of Pluto (NASA planetary fact sheet) | 1850 | kg/m3 | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.gravity | gravity of Mercury (NASA planetary fact sheet) | 3.7 | m/s2 | NASA-PLANETS | 2026-10-22 |
| planet:Venus.gravity | gravity of Venus (NASA planetary fact sheet) | 8.9 | m/s2 | NASA-PLANETS | 2026-10-22 |
| planet:Earth.gravity | gravity of Earth (NASA planetary fact sheet) | 9.8 | m/s2 | NASA-PLANETS | 2026-10-22 |
| planet:Moon.gravity | gravity of Moon (NASA planetary fact sheet) | 1.6 | m/s2 | NASA-PLANETS | 2026-10-22 |
| planet:Mars.gravity | gravity of Mars (NASA planetary fact sheet) | 3.7 | m/s2 | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.gravity | gravity of Jupiter (NASA planetary fact sheet) | 23.1 | m/s2 | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.gravity | gravity of Saturn (NASA planetary fact sheet) | 9.0 | m/s2 | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.gravity | gravity of Uranus (NASA planetary fact sheet) | 8.7 | m/s2 | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.gravity | gravity of Neptune (NASA planetary fact sheet) | 11.0 | m/s2 | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.gravity | gravity of Pluto (NASA planetary fact sheet) | 0.7 | m/s2 | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.vesc | escape velocity of Mercury (NASA planetary fact sheet) | 4.3 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Venus.vesc | escape velocity of Venus (NASA planetary fact sheet) | 10.4 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Earth.vesc | escape velocity of Earth (NASA planetary fact sheet) | 11.2 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Moon.vesc | escape velocity of Moon (NASA planetary fact sheet) | 2.4 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Mars.vesc | escape velocity of Mars (NASA planetary fact sheet) | 5.0 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.vesc | escape velocity of Jupiter (NASA planetary fact sheet) | 59.5 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.vesc | escape velocity of Saturn (NASA planetary fact sheet) | 35.5 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.vesc | escape velocity of Uranus (NASA planetary fact sheet) | 21.3 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.vesc | escape velocity of Neptune (NASA planetary fact sheet) | 23.5 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.vesc | escape velocity of Pluto (NASA planetary fact sheet) | 1.3 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.Prot | rotation period of Mercury (NASA planetary fact sheet) | 1407.6 | h (negative: retrograde) | NASA-PLANETS | 2026-10-22 |
| planet:Venus.Prot | rotation period of Venus (NASA planetary fact sheet) | -5832.5 | h (negative: retrograde) | NASA-PLANETS | 2026-10-22 |
| planet:Earth.Prot | rotation period of Earth (NASA planetary fact sheet) | 23.9 | h (negative: retrograde) | NASA-PLANETS | 2026-10-22 |
| planet:Moon.Prot | rotation period of Moon (NASA planetary fact sheet) | 655.7 | h (negative: retrograde) | NASA-PLANETS | 2026-10-22 |
| planet:Mars.Prot | rotation period of Mars (NASA planetary fact sheet) | 24.6 | h (negative: retrograde) | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.Prot | rotation period of Jupiter (NASA planetary fact sheet) | 9.9 | h (negative: retrograde) | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.Prot | rotation period of Saturn (NASA planetary fact sheet) | 10.7 | h (negative: retrograde) | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.Prot | rotation period of Uranus (NASA planetary fact sheet) | -17.2 | h (negative: retrograde) | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.Prot | rotation period of Neptune (NASA planetary fact sheet) | 16.1 | h (negative: retrograde) | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.Prot | rotation period of Pluto (NASA planetary fact sheet) | -153.3 | h (negative: retrograde) | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.day | length of day of Mercury (NASA planetary fact sheet) | 4222.6 | h | NASA-PLANETS | 2026-10-22 |
| planet:Venus.day | length of day of Venus (NASA planetary fact sheet) | 2802.0 | h | NASA-PLANETS | 2026-10-22 |
| planet:Earth.day | length of day of Earth (NASA planetary fact sheet) | 24.0 | h | NASA-PLANETS | 2026-10-22 |
| planet:Moon.day | length of day of Moon (NASA planetary fact sheet) | 708.7 | h | NASA-PLANETS | 2026-10-22 |
| planet:Mars.day | length of day of Mars (NASA planetary fact sheet) | 24.7 | h | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.day | length of day of Jupiter (NASA planetary fact sheet) | 9.9 | h | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.day | length of day of Saturn (NASA planetary fact sheet) | 10.7 | h | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.day | length of day of Uranus (NASA planetary fact sheet) | 17.2 | h | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.day | length of day of Neptune (NASA planetary fact sheet) | 16.1 | h | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.day | length of day of Pluto (NASA planetary fact sheet) | 153.3 | h | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.dist | distance from sun of Mercury (NASA planetary fact sheet) | 57.9 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Venus.dist | distance from sun of Venus (NASA planetary fact sheet) | 108.2 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Earth.dist | distance from sun of Earth (NASA planetary fact sheet) | 149.6 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Moon.dist | distance from sun of Moon (the Moon: about the Earth) (NASA planetary fact sheet) | 0.384 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Mars.dist | distance from sun of Mars (NASA planetary fact sheet) | 228.0 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.dist | distance from sun of Jupiter (NASA planetary fact sheet) | 778.5 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.dist | distance from sun of Saturn (NASA planetary fact sheet) | 1432.0 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.dist | distance from sun of Uranus (NASA planetary fact sheet) | 2867.0 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.dist | distance from sun of Neptune (NASA planetary fact sheet) | 4515.0 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.dist | distance from sun of Pluto (NASA planetary fact sheet) | 5906.4 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.peri | perihelion of Mercury (NASA planetary fact sheet) | 46.0 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Venus.peri | perihelion of Venus (NASA planetary fact sheet) | 107.5 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Earth.peri | perihelion of Earth (NASA planetary fact sheet) | 147.1 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Moon.peri | perihelion of Moon (the Moon: about the Earth) (NASA planetary fact sheet) | 0.363 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Mars.peri | perihelion of Mars (NASA planetary fact sheet) | 206.7 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.peri | perihelion of Jupiter (NASA planetary fact sheet) | 740.6 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.peri | perihelion of Saturn (NASA planetary fact sheet) | 1357.6 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.peri | perihelion of Uranus (NASA planetary fact sheet) | 2732.7 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.peri | perihelion of Neptune (NASA planetary fact sheet) | 4471.1 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.peri | perihelion of Pluto (NASA planetary fact sheet) | 4436.8 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.aph | aphelion of Mercury (NASA planetary fact sheet) | 69.8 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Venus.aph | aphelion of Venus (NASA planetary fact sheet) | 108.9 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Earth.aph | aphelion of Earth (NASA planetary fact sheet) | 152.1 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Moon.aph | aphelion of Moon (the Moon: about the Earth) (NASA planetary fact sheet) | 0.406 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Mars.aph | aphelion of Mars (NASA planetary fact sheet) | 249.3 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.aph | aphelion of Jupiter (NASA planetary fact sheet) | 816.4 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.aph | aphelion of Saturn (NASA planetary fact sheet) | 1506.5 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.aph | aphelion of Uranus (NASA planetary fact sheet) | 3001.4 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.aph | aphelion of Neptune (NASA planetary fact sheet) | 4558.9 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.aph | aphelion of Pluto (NASA planetary fact sheet) | 7375.9 | 1e6 km | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.Porb | orbital period of Mercury (NASA planetary fact sheet) | 88.0 | days | NASA-PLANETS | 2026-10-22 |
| planet:Venus.Porb | orbital period of Venus (NASA planetary fact sheet) | 224.7 | days | NASA-PLANETS | 2026-10-22 |
| planet:Earth.Porb | orbital period of Earth (NASA planetary fact sheet) | 365.2 | days | NASA-PLANETS | 2026-10-22 |
| planet:Moon.Porb | orbital period of Moon (the Moon: about the Earth) (NASA planetary fact sheet) | 27.3 | days | NASA-PLANETS | 2026-10-22 |
| planet:Mars.Porb | orbital period of Mars (NASA planetary fact sheet) | 687.0 | days | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.Porb | orbital period of Jupiter (NASA planetary fact sheet) | 4331 | days | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.Porb | orbital period of Saturn (NASA planetary fact sheet) | 10747 | days | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.Porb | orbital period of Uranus (NASA planetary fact sheet) | 30589 | days | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.Porb | orbital period of Neptune (NASA planetary fact sheet) | 59800 | days | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.Porb | orbital period of Pluto (NASA planetary fact sheet) | 90560 | days | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.vorb | orbital velocity of Mercury (NASA planetary fact sheet) | 47.4 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Venus.vorb | orbital velocity of Venus (NASA planetary fact sheet) | 35.0 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Earth.vorb | orbital velocity of Earth (NASA planetary fact sheet) | 29.8 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Moon.vorb | orbital velocity of Moon (the Moon: about the Earth) (NASA planetary fact sheet) | 1.0 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Mars.vorb | orbital velocity of Mars (NASA planetary fact sheet) | 24.1 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.vorb | orbital velocity of Jupiter (NASA planetary fact sheet) | 13.1 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.vorb | orbital velocity of Saturn (NASA planetary fact sheet) | 9.7 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.vorb | orbital velocity of Uranus (NASA planetary fact sheet) | 6.8 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.vorb | orbital velocity of Neptune (NASA planetary fact sheet) | 5.4 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.vorb | orbital velocity of Pluto (NASA planetary fact sheet) | 4.7 | km/s | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.incl | orbital inclination of Mercury (NASA planetary fact sheet) | 7.0 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Venus.incl | orbital inclination of Venus (NASA planetary fact sheet) | 3.4 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Earth.incl | orbital inclination of Earth (NASA planetary fact sheet) | 0.0 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Moon.incl | orbital inclination of Moon (NASA planetary fact sheet) | 5.1 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Mars.incl | orbital inclination of Mars (NASA planetary fact sheet) | 1.8 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.incl | orbital inclination of Jupiter (NASA planetary fact sheet) | 1.3 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.incl | orbital inclination of Saturn (NASA planetary fact sheet) | 2.5 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.incl | orbital inclination of Uranus (NASA planetary fact sheet) | 0.8 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.incl | orbital inclination of Neptune (NASA planetary fact sheet) | 1.8 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.incl | orbital inclination of Pluto (NASA planetary fact sheet) | 17.2 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.ecc | orbital eccentricity of Mercury (NASA planetary fact sheet) | 0.206 | - | NASA-PLANETS | 2026-10-22 |
| planet:Venus.ecc | orbital eccentricity of Venus (NASA planetary fact sheet) | 0.007 | - | NASA-PLANETS | 2026-10-22 |
| planet:Earth.ecc | orbital eccentricity of Earth (NASA planetary fact sheet) | 0.017 | - | NASA-PLANETS | 2026-10-22 |
| planet:Moon.ecc | orbital eccentricity of Moon (NASA planetary fact sheet) | 0.055 | - | NASA-PLANETS | 2026-10-22 |
| planet:Mars.ecc | orbital eccentricity of Mars (NASA planetary fact sheet) | 0.094 | - | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.ecc | orbital eccentricity of Jupiter (NASA planetary fact sheet) | 0.049 | - | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.ecc | orbital eccentricity of Saturn (NASA planetary fact sheet) | 0.052 | - | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.ecc | orbital eccentricity of Uranus (NASA planetary fact sheet) | 0.047 | - | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.ecc | orbital eccentricity of Neptune (NASA planetary fact sheet) | 0.010 | - | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.ecc | orbital eccentricity of Pluto (NASA planetary fact sheet) | 0.244 | - | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.obliq | obliquity to orbit of Mercury (NASA planetary fact sheet) | 0.034 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Venus.obliq | obliquity to orbit of Venus (NASA planetary fact sheet) | 177.4 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Earth.obliq | obliquity to orbit of Earth (NASA planetary fact sheet) | 23.4 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Moon.obliq | obliquity to orbit of Moon (NASA planetary fact sheet) | 6.7 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Mars.obliq | obliquity to orbit of Mars (NASA planetary fact sheet) | 25.2 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.obliq | obliquity to orbit of Jupiter (NASA planetary fact sheet) | 3.1 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.obliq | obliquity to orbit of Saturn (NASA planetary fact sheet) | 26.7 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.obliq | obliquity to orbit of Uranus (NASA planetary fact sheet) | 97.8 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.obliq | obliquity to orbit of Neptune (NASA planetary fact sheet) | 28.3 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.obliq | obliquity to orbit of Pluto (NASA planetary fact sheet) | 119.5 | deg | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.Tmean | mean temperature of Mercury (NASA planetary fact sheet) | 167 | degC | NASA-PLANETS | 2026-10-22 |
| planet:Venus.Tmean | mean temperature of Venus (NASA planetary fact sheet) | 464 | degC | NASA-PLANETS | 2026-10-22 |
| planet:Earth.Tmean | mean temperature of Earth (NASA planetary fact sheet) | 15 | degC | NASA-PLANETS | 2026-10-22 |
| planet:Moon.Tmean | mean temperature of Moon (NASA planetary fact sheet) | -20 | degC | NASA-PLANETS | 2026-10-22 |
| planet:Mars.Tmean | mean temperature of Mars (NASA planetary fact sheet) | -65 | degC | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.Tmean | mean temperature of Jupiter (NASA planetary fact sheet) | -110 | degC | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.Tmean | mean temperature of Saturn (NASA planetary fact sheet) | -140 | degC | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.Tmean | mean temperature of Uranus (NASA planetary fact sheet) | -195 | degC | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.Tmean | mean temperature of Neptune (NASA planetary fact sheet) | -200 | degC | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.Tmean | mean temperature of Pluto (NASA planetary fact sheet) | -225 | degC | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.psurf | surface pressure of Mercury (NASA planetary fact sheet) | 0 | bar | NASA-PLANETS | 2026-10-22 |
| planet:Venus.psurf | surface pressure of Venus (NASA planetary fact sheet) | 92 | bar | NASA-PLANETS | 2026-10-22 |
| planet:Earth.psurf | surface pressure of Earth (NASA planetary fact sheet) | 1 | bar | NASA-PLANETS | 2026-10-22 |
| planet:Moon.psurf | surface pressure of Moon (NASA planetary fact sheet) | 0 | bar | NASA-PLANETS | 2026-10-22 |
| planet:Mars.psurf | surface pressure of Mars (NASA planetary fact sheet) | 0.01 | bar | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.psurf | surface pressure of Pluto (NASA planetary fact sheet) | 0.00001 | bar | NASA-PLANETS | 2026-10-22 |
| planet:Mercury.moons | number of moons of Mercury (NASA planetary fact sheet) | 0 | - | NASA-PLANETS | 2026-10-22 |
| planet:Venus.moons | number of moons of Venus (NASA planetary fact sheet) | 0 | - | NASA-PLANETS | 2026-10-22 |
| planet:Earth.moons | number of moons of Earth (NASA planetary fact sheet) | 1 | - | NASA-PLANETS | 2026-10-22 |
| planet:Moon.moons | number of moons of Moon (NASA planetary fact sheet) | 0 | - | NASA-PLANETS | 2026-10-22 |
| planet:Mars.moons | number of moons of Mars (NASA planetary fact sheet) | 2 | - | NASA-PLANETS | 2026-10-22 |
| planet:Jupiter.moons | number of moons of Jupiter (NASA planetary fact sheet) | 95 | - | NASA-PLANETS | 2026-10-22 |
| planet:Saturn.moons | number of moons of Saturn (NASA planetary fact sheet) | 274 | - | NASA-PLANETS | 2026-10-22 |
| planet:Uranus.moons | number of moons of Uranus (NASA planetary fact sheet) | 28 | - | NASA-PLANETS | 2026-10-22 |
| planet:Neptune.moons | number of moons of Neptune (NASA planetary fact sheet) | 16 | - | NASA-PLANETS | 2026-10-22 |
| planet:Pluto.moons | number of moons of Pluto (NASA planetary fact sheet) | 5 | - | NASA-PLANETS | 2026-10-22 |
| ics:base.Hadean | age of the base of the Hadean | 4567 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Hadean | chart colour of the Hadean (CGMW) | #AE027E | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Archean | age of the base of the Archean | 4031 +- 3 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Archean | chart colour of the Archean (CGMW) | #F0047F | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Proterozoic | age of the base of the Proterozoic | 2500 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Proterozoic | chart colour of the Proterozoic (CGMW) | #F73563 | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Phanerozoic | age of the base of the Phanerozoic | 538.8 +- 0.6 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Phanerozoic | chart colour of the Phanerozoic (CGMW) | #9AD9DD | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Paleozoic | age of the base of the Paleozoic | 538.8 +- 0.6 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Paleozoic | chart colour of the Paleozoic (CGMW) | #99C08D | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Mesozoic | age of the base of the Mesozoic | 251.902 +- 0.024 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Mesozoic | chart colour of the Mesozoic (CGMW) | #67C5CA | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Cenozoic | age of the base of the Cenozoic | 66.00 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Cenozoic | chart colour of the Cenozoic (CGMW) | #F2F91D | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Cambrian | age of the base of the Cambrian | 538.8 +- 0.6 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Cambrian | chart colour of the Cambrian (CGMW) | #7FA056 | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Ordovician | age of the base of the Ordovician | 486.85 +- 1.5 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Ordovician | chart colour of the Ordovician (CGMW) | #009270 | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Silurian | age of the base of the Silurian | 443.1 +- 1.0 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Silurian | chart colour of the Silurian (CGMW) | #B3E1B6 | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Devonian | age of the base of the Devonian | 419.62 +- 1.36 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Devonian | chart colour of the Devonian (CGMW) | #CB8C37 | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Carboniferous | age of the base of the Carboniferous | 358.86 +- 0.19 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Carboniferous | chart colour of the Carboniferous (CGMW) | #67A599 | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Permian | age of the base of the Permian | 298.9 +- 0.15 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Permian | chart colour of the Permian (CGMW) | #F04028 | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Triassic | age of the base of the Triassic | 251.902 +- 0.024 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Triassic | chart colour of the Triassic (CGMW) | #812B92 | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Jurassic | age of the base of the Jurassic | 201.4 +- 0.2 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Jurassic | chart colour of the Jurassic (CGMW) | #34B2C9 | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Cretaceous | age of the base of the Cretaceous | 143.1 +- 0.6 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Cretaceous | chart colour of the Cretaceous (CGMW) | #7FC64E | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Paleogene | age of the base of the Paleogene | 66.00 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Paleogene | chart colour of the Paleogene (CGMW) | #FD9A52 | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Neogene | age of the base of the Neogene | 23.04 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Neogene | chart colour of the Neogene (CGMW) | #FFE619 | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Quaternary | age of the base of the Quaternary | 2.58 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Quaternary | chart colour of the Quaternary (CGMW) | #F9F97F | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Pleistocene | age of the base of the Pleistocene | 2.58 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Pleistocene | chart colour of the Pleistocene (CGMW) | #FFEFAF | RGB hex | ICS-2026-06 | 2026-10-22 |
| ics:base.Holocene | age of the base of the Holocene | 0.0117 | Ma | ICS-2026-06 | 2026-10-22 |
| ics:colour.Holocene | chart colour of the Holocene (CGMW) | #FEEBD2 | RGB hex | ICS-2026-06 | 2026-10-22 |
| const:au | astronomical unit (exact, IAU 2012 Resolution B2, as listed in the SI brochure Table 8) | 149597870700 | m | SI-2019 | 2026-10-22 |
| data:ne-land | Natural Earth land polygons, 1:110m and 1:50m (v5, GitHub mirror) | dataset | - | NATURAL-EARTH | 2026-10-22 |
| data:pb2002 | PB2002 plate boundaries and boundary steps (52 plates; step class, relative velocity) | dataset | - | PB2002 | 2026-10-22 |
| data:etopo1 | ETOPO1 global relief, 1-degree sampling | dataset | m | ETOPO1 | 2026-10-22 |
| data:usgs-comcat | earthquakes M >= 6, 1976-01-01 to 2025-12-31 (7 031 events) | dataset | - | USGS-COMCAT | 2026-10-22 |
| data:gvp | Holocene volcanoes: number, name, position, type, setting, last eruption | dataset | - | GVP | 2026-10-22 |
| data:prem | PREM: P and S velocities and density against depth (isotropic, 1 s) | dataset | - | PREM | 2026-10-22 |
| data:co2-mlo | Mauna Loa CO2, monthly and annual means since 1958 | dataset | ppm | NOAA-GML | 2026-10-22 |
| data:gistemp | global annual mean surface temperature anomaly, base 1951-1980, since 1880 | dataset | degC | GISTEMP | 2026-10-22 |
| data:co2-bereiter | Antarctic ice-core CO2 composite, last 800 kyr | dataset | ppm | BEREITER-2015 | 2026-10-22 |
| data:edc-jouzel | EPICA Dome C deuterium and temperature anomaly, last 800 kyr (EDC3 age scale) | dataset | permil; degC | JOUZEL-2007 | 2026-10-22 |
| data:lr04 | LR04 benthic d18O stack, last 5.3 Myr | dataset | permil | LR04 | 2026-10-22 |
| data:gmsl-lsa | global mean sea-level anomaly from satellite altimetry since 1993 (annual signal removed) | dataset | mm | NOAA-LSA | 2026-10-22 |
| region:name | the exercise region's name, Varden Hills: an exact-phrase web search found no place of that name (only Norwegian viewpoints called Varden) | Varden Hills | - | WEBSEARCH | 2026-10-22 |
