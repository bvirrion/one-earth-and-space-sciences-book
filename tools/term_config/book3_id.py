"""Book 3 (University, Year 1) -- id. Curation only; the rules live in tools/termlink/.

Curated 2026-10-27 by the Book 3 `id` agent from this edition's own harvest
(the first link pass with an empty config), with the frequency and
chapter-set censuses against the English twin (translation_instruction.md).
Book 2 id's configuration was read for the mechanisms only; no entry is copied
from it, and no entry is copied from book3_en.py or book3_fr.py.
"""

# STOP: ordinary or other-sense words. A STOPped term still links inside the
# chapter that pins its one sense (the per-chapter map), and nowhere else:
# - stabil, tidak stabil: of the air and the ocean (ch26, ch28-29); the
#   stable triple junction of ch12 keeps its links;
# - orientasi: the grain orientation of ch08 and the orientation of a fabric
#   elsewhere; the attitude (strike and dip) of ch04-06 keeps its links;
# - penurunan: of the isotope values, of the sea surface and of the AMOC
#   (ch24, ch26, ch29); the basin subsidence of ch23 keeps its links;
# - massa udara: of a mass flux of air (ch28); the airmass of ch02 keeps its
#   links;
# - fluks: a heat, radiative or sediment flux (ch15, ch19-22, ch27-29); the
#   flux of a source of ch02 keeps its links;
# - tinggi: the height of a hill, of a plateau (Dataran Tinggi) or of a
#   column (ch11, ch23); the altitude of ch01 keeps its links;
# - sistem: a closed isotopic system and the system of a rock (ch25); the
#   chronostratigraphic system of ch24 keeps its links;
# - orde: the order of an interference colour in general (ch26) and the
#   order of a theorem; the interference colour of ch08 keeps its links;
# - deklinasi: the magnetic declination of ch06; the astronomical declination
#   of ch01 keeps its links;
# - peregangan: the stretching of a basin or a margin (ch23); the strain of
#   ch16 keeps its links;
# - tahap: a heating step of an argon-argon run (ch25); the chronostratigraphic
#   stage of ch24 keeps its links;
# - seri: the series of a rock sequence (ch25, "seri ini" of the Varden granite);
#   the chronostratigraphic series of ch24 keeps its links.
STOP = {"stabil", "Stabil", "tidak stabil", "Tidak stabil",
        "orientasi", "Orientasi",
        "penurunan", "Penurunan", "penurunannya", "Penurunannya",
        "massa udara", "Massa udara",
        "fluks", "Fluks",
        "tinggi", "Tinggi",
        "sistem", "Sistem",
        "orde", "Orde",
        "deklinasi", "Deklinasi",
        "peregangan", "Peregangan",
        "tahap", "Tahap", "tahap-tahap", "Tahap-tahap",
        "seri", "Seri"}
NO_CAPITAL = set()
# EXTRA: a term harvested only with its capital (the definition opens its
# sentence, so the \emph is capitalised), or whose lowercase form is the one
# the Indonesian prose uses. Each entry is the same label as its definition.
EXTRA = {
    # the optical retardation (ch08): "Retardasi" is harvested capitalised
    "retardasi": "def:b1:optical-mineralogy:retardation",
    "Retardasi": "def:b1:optical-mineralogy:retardation",
    # the birefringence of a mineral (ch08): the same capital-only harvest
    "birefringensi": "def:b1:optical-mineralogy:birefringence",
    "Birefringensi": "def:b1:optical-mineralogy:birefringence",
    # trend, the azimuth of a line (ch06), as English writes "trend"
    "trend": "def:b1:field-lab-methods-1:trend-plunge",
    "Trend": "def:b1:field-lab-methods-1:trend-plunge",
    # hydrolysis of a silicate (ch19), capital-only harvest
    "hidrolisis": "def:b1:weathering-clays:hydrolysis",
    "Hidrolisis": "def:b1:weathering-clays:hydrolysis",
    # seeing, the atmospheric blur (ch02): its only sense
    "kekaburan": "def:b1:observing-the-sky:seeing",
    "Kekaburan": "def:b1:observing-the-sky:seeing",
    # the foliation of a rock (ch17): its only sense
    "foliasi": "def:b1:faults-folds-fabrics:foliation",
    "Foliasi": "def:b1:faults-folds-fabrics:foliation",
    # the vertical and horizontal throw of a fault (ch05); "lompatan" alone is
    # a jump in other senses (a density, a velocity, a rate), so only the
    # two-word forms are added
    # the altitude of a celestial body (ch01): "tinggi" alone is STOPped (it
    # is the adjective "high" everywhere else), so the altitude phrases are
    # added as whole terms; the altitude of a hill (ch02, ch11) is not one
    "tinggi Matahari": "def:b1:spherical-astronomy:horizontal",
    "Tinggi Matahari": "def:b1:spherical-astronomy:horizontal",
    "tinggi tengah hari": "def:b1:spherical-astronomy:horizontal",
    "tinggi terendah": "def:b1:spherical-astronomy:horizontal",
    "Tinggi terendah": "def:b1:spherical-astronomy:horizontal",
    "tinggi kutub": "def:b1:spherical-astronomy:horizontal",
    "Tinggi kutub": "def:b1:spherical-astronomy:horizontal",
    "tinggi bintang": "def:b1:spherical-astronomy:horizontal",
    "tinggi tersebut": "def:b1:spherical-astronomy:horizontal",
    "lompatan vertikal": "def:b1:cross-sections:throw",
    "Lompatan vertikal": "def:b1:cross-sections:throw",
    "lompatan horizontal": "def:b1:cross-sections:throw",
    "Lompatan horizontal": "def:b1:cross-sections:throw",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"
EXTRA_PROTECT = [
    # Pemadatan on a mixing of two waters densifies the water (cabbeling,
    # ch26); it is not the compaction of a sediment (ch23)
    r'\b[Pp]emadatan(?=\s+pada\s+pencampuran)',
    # anggota (member) of a committee or of a vote (ch24: the voting members of
    # the subcommission and of the Commission, and the three members who did
    # not vote); the lithostratigraphic member keeps its links
    r'\b[Aa]nggota(?=\s+(?:pemberi\s+suara|tidak\s+memberi\s+suara))',
    # kontak with the atmosphere (ch26: a water mass out of contact with the
    # air): a physical contact, not the geological contact of ch05 and ch13
    r'\b[Kk]ontak(?=\s+dengan\s+atmosfer)',
    # penurunan of a sea-level fall (ch23: the glacial fall of the sea, the
    # eustatic lowstand), not the subsidence of a basin floor
    r'\b[Pp]enurunan(?=\s+(?:muka\s+laut|glasial))',
    # kontak of two grains (ch23: quartz dissolves at the grain contacts), not
    # the geological contact of a map (ch04-05, ch13)
    r'\b[Kk]ontak(?=\s+butiran|\s*;)',
]
