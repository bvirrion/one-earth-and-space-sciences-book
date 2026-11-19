#!/usr/bin/env python3
"""Simplified Chinese hygiene gate for a translated tree (gate 9 of check_translation.sh).

Like Hindi and Arabic, Chinese is written in a script that is not Latin, so
residual English is visibly foreign and a gate can flag any Latin word in the
visible text. The LaTeX reduction is imported from check_hindi_prose.py, not
copied (translation_instruction.md: "import it, do not copy it").

Classes:

  english       a Latin word in visible text: prose, \\text{...} in math, TikZ
                node text, axis labels, environment optional titles. People's
                names are written in Chinese in this edition (欧拉, 柯西), so a
                Latin name is flagged too. Acronyms of up to four capitals and
                unit symbols are allowed, as in the Hindi gate.
  legend        a Latin word in \\legend{...} or \\addlegendentry{...}, which the
                imported reduction does not read (the macro form of a legend:
                see "\\legend{...} is the other blind spot" in
                translation_instruction.md).
  ascii-punct   an ASCII , . ; : ? ! after a Chinese character, or an ASCII
                parenthesis opening or closing on Chinese text: Chinese prose
                takes the full-width forms ，。；：？！（）.

Usage:
    python3 tools/check_chinese_prose.py parts/grade-3/zh parts/grade-3/solutions/zh

Exit status is 1 if anything was flagged.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from check_hindi_prose import (  # noqa: E402
    ALLOWED_UNITS, ALLOWED_WORDS, DOTTED_ABBREV, LATIN_WORD, SHORT_ENGLISH,
    _locate, strip_comments, visible_text)

HAN = r"\u3400-\u4dbf\u4e00-\u9fff"
ASCII_PUNCT = re.compile(rf"[{HAN}][ \t]*[,;:?!]|[{HAN}]\.(?=\s|$|[{HAN}])|\((?=[{HAN}])|(?<=[{HAN}])\)")
LEGEND = re.compile(r"\\(?:legend|addlegendentry)\s*(\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\})")
MATHLESS = re.compile(r"\$[^$]*\$|\\[A-Za-z]+")

# Latin that may stay in a Chinese line: the series and product names.
AMINO = {"Gly", "Ala", "Val", "Leu", "Ile", "Phe", "Tyr", "Trp", "Ser", "Thr", "Cys", "Met", "Asp", "Glu", "Asn",
         "Gln", "Lys", "Arg", "His", "Pro"}   # amino-acid codes (chemistry grade 12)
# Earth zh Book 3 (University Year 1): credited people, places, fossil genera and species, data sets, kept Latin terms
ALLOWED_HERE_B3 = {"gakkel", "gloria", "rodrigues", "reykjanes", "traps", "kef", "arizona", "lavinsky", "twyla", "baker", "andrija", "even", "neuhaus", "majorite", "bullard", "broodt", "alpsdake", "sandwell", "courtillot", "renne", "gleason", "tullis", "hirth", "kohlstedt", "darryl", "peroni", "csiro", "james", "jackson", "pitch", "savage", "burford", "shannon", "laterite", "joshua", "stevens", "phi", "southard", "aztec", "becke", "oese", "acropora", "emiliania", "huxleyi", "alison", "north", "carolina", "wilmington", "orbulina", "universa", "takagi", "stony", "brook", "mccaffrey", "lazar", "holland", "athy", "sclater", "christie", "pybacktrack", "rygel", "lambeck", "spratt", "josugoni", "trichophycus", "pedum", "monograptus", "uniformis", "hindeodus", "parvus", "vardenoceras", "medium", "ultimum", "primum", "ostreola", "libby", "taylor", "teos", "caron", "lance", "schmitz", "yelland", "nesdis"}
# Earth zh Book 4 (University Year 2): the same classes
ALLOWED_HERE_B4 = {"vsmow", "kora", "vel", "asha", "bhvo", "grt", "rosenberg", "nereites", "skolithos", "cruziana", "zoophycos", "ferrière", "bergin", "tafalla", "heritage", "stsci", "haisch", "lada", "tauri", "aldra", "chiang", "youdin", "lodders", "lugaro", "john", "gail", "alais", "orgueil", "tonk", "ivuna", "revelstoke", "mcdonough", "sun", "budahn", "gale", "villa", "white", "stracke", "edwards", "kendall", "caldwell", "mattey", "densityx", "iacovino", "till", "shiprock", "trident", "novarupta", "griggs", "austin", "post", "dave", "harlow", "newhall", "self", "katz", "tegner", "kevin", "walsh", "parícutin", "streckeisen", "bas", "irvine", "baragar", "vermeesch", "pease", "peccerillo", "pearce", "cann", "robie", "hemingway", "sil", "holdaway", "mukhopadhyay", "day", "kbar", "an", "smyth", "lachlan", "aptychus", "bündnerschiefer", "verrucano", "transalp", "alparray", "michailos", "chasseral", "siw", "eniwetok", "enewetak", "liq", "hoffman", "nuccaleena", "cryochrons", "cryochron", "haq", "merdith", "mollweide", "miller", "kominz", "kaiho", "picenus", "lagerstätten", "konservat", "lagerstätte", "waptia", "phyllopod", "marrella", "amada", "iapws", "stephen", "corfidi", "eniac", "niño", "anthony", "gow", "crrel", "northgrip", "svensson", "berger", "loutre", "tmol", "cenogrid", "tom", "bingham", "sedex", "flambeau", "singer", "moring", "fletcher", "pugmire", "stoiip", "bangombé", "sleipner", "eq", "dew", "taggart", "siems", "halemaumau", "ciaaw"}
# Earth zh Book 5 (University Year 3): the same classes, filled at the book's close
ALLOWED_HERE_B5 = {"amarsi", "asplund", "berlin", "boussinesq", "bushnell", "california", "carnegie", "carter", "casagrande", "chrm", "chi", "ecostress", "eilers", "fox", "fruchter", "fry", "grace", "gaia", "grevesse", "hann", "hubble", "icesat", "imbie", "insar", "insight", "jim", "kadonis", "kappa", "kepler", "kepos", "llsvps", "llsvp", "levan", "mars", "maven", "messenger", "oru", "pagan", "pcp", "peaco", "pegasi", "pouliasis", "roddy", "sbb", "sbc", "schmidt", "sentinel", "sgr", "soszynski", "sverdrup", "trappist", "tanvir", "wasp", "wicks", "wulff", "yungel", "zeng", "zijderveld", "alpha", "app", "dex", "heic"}
ALLOWED_HERE = {"chemistry", "book", "one", "course", "git", "contributing", "md", "url",
                # unit and function symbols kept in Latin in Chinese texts (physics zh Book 4): rpm, ppm, sinc, erfc
                "rpm", "ppm", "sinc", "erfc",
                # kept in Latin in Chinese texts (physics zh Book 5): lattice and quark-content symbols, units
                "fcc", "bcc", "hcp", "ppb", "p--n", "n--p",
                # organic-chemistry group symbols and the bar (pressure unit) kept in Latin (chemistry zh Book 2)
                "ots", "oet", "tscl", "rnu", "bar", "e--ph", "a--b--c--d",
                # IUPAC process subscripts kept in Latin by Chinese physical-chemistry textbooks (Δ_fus H, Δ_vap H, Δ_trs H),
                # NMR experiment names, data sources, ligand and group abbreviations, toxicology limits (chemistry zh Books 3-4)
                "fus", "vap", "trs", "sub", "mix", "dept", "corr", "cat", "atgcgt", "acgcat", "c--oh", "noesy", "cosy", "hsqc", "janaf", "codata", "webbook", "pubchem",
                "bpy", "binap", "dipamp", "ome", "arx", "r--br", "pd--ph", "l-dopa", "homo--lumo", "noael", "loael", "cgs",
                "cativa", "cdcl",
                # the sibling series, named in a cross-reference ("参见 One Physics Book"), and Latin element names (钠 natrium)
                "physics", "math", "biology", "natrium", "kalium", "ferrum", "cuprum", "argentum", "aurum", "plumbum", "stannum",
                "hydrargyrum", "stibium",
                # function names a display line can leave outside the blanked math (\cos\theta = \frac{\text{邻边}}{…})
                "sin", "cos", "tan", "cot", "log", "exp", "lim", "max", "min", "sup", "inf", "det", "gcd", "lcm",
                "arg", "ker", "dim", "deg", "diag", "sinh", "cosh", "tanh", "arcsin", "arccos", "arctan",
                # math names the blanking leaks from a formula split over lines (Book 5); not theta/zeta, which
                # Haiku also writes in prose ("theta 函数", "zeta 值")
                "delta", "limsup", "liminf",
                # roman numerals of item labels
                "ii", "iii", "iv", "vi", "vii", "viii", "ix", "xi", "xii",
                # physics: unit symbols the Hindi list lacks, integral names a split display leaks, and the Latin
                # subscripts physics writes in \text{} (I_enc, E_int, F_ext, P_eff, E_tot)
                "ev", "kev", "mev", "gev", "tev", "int", "iint", "iiint", "oint", "oiint",
                "enc", "ext", "eff", "tot", "rms", "th", "max", "min",
                # Latin kept on purpose in the Chinese text of this series: added per book at its close,
                # each after a grep of the whole file (the gate's line numbers can be wrong)
                # Book 1 (2026-11-19): data sources and credits kept in Latin as the licence names them (Natural Earth,
                # ETOPO, the Smithsonian Global Volcanism Program, the USGS earthquake catalogue, MODIS Rapid Response,
                # Operation IceBridge, ISS Expedition 23, GOES-16, Aqua, Mariner, Apollo, NASA/JPL-Caltech, This Dynamic
                # Earth), photographers and painters in credits, fossil genera in italics, and the Latin roots the text
                # explains (cumulus 意为“堆”, pyro 意为火)
                "natural", "earth", "etopo", "smithsonian", "global", "volcanism", "program", "geological", "survey",
                "earthquake", "catalogue", "kresge", "collection", "mariner", "apollo", "jpl-caltech", "jpl", "caltech",
                "this", "dynamic", "bird", "expedition", "goes-", "aqua", "modis", "rapid", "response", "team",
                "operation", "icebridge", "challenger", "herdman", "founders", "oceanography", "jacques", "descloitres",
                "tetreau", "kurtz", "philip", "mcdaniel", "henry", "raeburn",
                "mesosaurus", "cynognathus", "lystrosaurus", "glossopteris",
                "cumulus", "stratus", "cirrus", "nimbus", "pyro", "clastic",
                "goes", "nsidc", "sea", "ice", "index", "fetterer", "paleoclimatology", "dome", "epica", "jouzel", "bereiter",
                "gistemp", "version", "circular", "coast", "guard", "perkins", "mineralogy", "earle", "environmental",
                "geology", "aster", "japan", "space", "systems", "science", "lagoa", "dos", "barros", "national", "park",
                "service", "landsat", "data", "center", "visible", "s--b--w--t",
                # Book 2 (2026-11-19): authors cited in credits, data sets, instruments, ships and drilling programmes (the titles
                # of works cited are whole phrases in CITED below, so that `for` or `over` stays an English word everywhere else)
                "o'nions", "angus", "academy", "ahnert", "allen", "alvin", "archive", "argo", "argus",
                "atlas", "beyond", "bierman", "blewitt", "cande", "canyon", "chart", "chert", "christensen",
                "chronostratigraphic", "clague", "concordia", "dalrymple", "dartmouth", "davies", "demets", "diablo",
                "drilling", "dye", "electron", "exoplanet", "facility", "gplates", "gao", "gaybullaev", "geodetic",
                "glomar", "gordon", "gough", "hirschmann", "holloway", "ibtracs",
                "institution", "international", "iwate", "joides", "jaramillo", "jesse", "jet", "jizzi", "johnson", "kamland",
                "karplus", "kawamoto", "kent", "knorr", "kreemer", "laboratory", "laredo", "lisiecki", "mosaic",
                "magnetic", "marci", "mckenzie", "meade", "megata", "microscope", "mike", "montgomery", "moody",
                "mooney", "müller", "nevada", "nuevo", "observatory", "oldham", "patterson",
                "pool", "portenga", "proceedings", "project", "propulsion", "proxima", "raymo",
                "resolution", "robert", "robinson", "rudnick", "sciences", "scripps", "seton", "shiklomanov", "simmon",
                "strelley", "sturchio", "syvitski", "terra", "trenberth", "trenchard", "university", "wadi",
                "wang", "web",
}


# A word made only of element symbols and counts is a formula the English writes as plain text (HCl 1.09, HBr 0.83):
# it stays as written (chemistry zh trial, 2026-11-18).
ELEMENTS = set("""H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y
Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg
Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm""".split())
FORMULA_PART = re.compile(r"[A-Z][a-z]?\d*")


def _is_formula(word):
    parts = FORMULA_PART.findall(word)
    return "".join(parts) == word and all(re.sub(r"\d", "", q) in ELEMENTS for q in parts) and len(parts) >= 2


def _flag_latin(text, body, rel, cls, findings, occ):
    for m in LATIN_WORD.finditer(text):
        word = m.group(0)
        low = word.lower().rstrip("-")   # `NIST-4`: the instrument name runs on into its number
        if (_is_formula(word) or word.rstrip("-") in ELEMENTS   # HCl; Am-241, an isotope
                or all(w in ELEMENTS or w in AMINO for w in word.split("--"))   # He--Ne, a laser; Gly--Ala, a dipeptide
                or re.fullmatch(r"[a-z]--[a-z]", word)):   # a sub-question range, (b--c) (physics zh Book 5)
            continue
        if low in ALLOWED_WORDS or low in ALLOWED_UNITS or low in ALLOWED_HERE or low in ALLOWED_HERE_B3 or low in ALLOWED_HERE_B4 or low in ALLOWED_HERE_B5:
            continue
        if word.islower() and low in SHORT_ENGLISH:
            findings.append((rel, _locate(body, word, occ), cls, f"English in visible text: {word!r}"))
            continue
        if word.isupper() and len(word) <= 4:
            continue
        if len(word) < 3:
            continue
        findings.append((rel, _locate(body, word, occ), cls, f"English in visible text: {word!r}"))


LIST_KEY = re.compile(r"(?:[xyz]ticklabels|symbolic [xyz] coords|legend entries)\s*=\s*\{|\\foreach\s[^{}]*?\bin\s*\{")


def _blank_list_commas(body):
    """The top-level commas of a pgf list or a \\foreach list are code, over however many lines the list runs
    (`\\foreach \\d in {星期一, 星期二,` then `星期五, 星期六}` on the next line: Earth zh Book 1)."""
    t = list(body)
    for m in LIST_KEY.finditer(body):
        j, d = m.end(), 1
        while j < len(body) and d:
            c = body[j]
            if c == "\\":
                j += 2
                continue
            d += (c == "{") - (c == "}")
            if c == "," and d == 1:
                t[j] = "\x00"
            j += 1
    return "".join(t)


# Titles of works and programmes cited in Latin, blanked as whole phrases (a line break may fall inside one)
CITED = ["GRACE Follow-On", "NCEP--NCAR Reanalysis", "Journal of Marine Research", "ECOSTRESS Spectral Library", "Jet Propulsion Laboratory, California Institute of Technology", "Mars Global Surveyor", "Exoplanet Exploration", "Geneva--Copenhagen", "ETOPO1 Ice Surface", "NCEP--NCAR", "Magnetic anomalies over oceanic ridges", "History of Ocean Basins", "The Evolution of the Igneous Rocks",
         "IPCC Sixth Assessment Report", "IPCC Sixth Assessment", "IPCC Sixth", "Assessment Report", "Summary for Policymakers",
         "Working Group", "World Ocean Atlas", "NOAA Global Ocean Monitoring and Observing",
         "Earth Sciences and Image Analysis", "Geology Digital Image Library", "Nature", "Deep Sea Drilling Project",
         "Physical Geology", "Little Dome", "White、", "NOAA Global Monitoring Laboratory",
         "The Structure and Distribution of Coral Reefs", "World Data Service for Paleoclimatology", "NOAA NCEI", "Philosophical Transactions", "An essay on the winds and currents of the ocean", "World Magnetic Model", "Popular Science Monthly", "NCEP-NCAR Reanalysis", "https://psl.noaa.gov", "Goddard Space Flight", "Nationalparks", "T--O--T", "K--Pg", "Becke-Oese", "University of North Carolina Wilmington", "A Neoproterozoic Snowball Earth", "Volcanoes of the World", "Global Volcanism Program", "Annex~III extended data", "Carbon Dioxide Capture and Storage", "Meteoritical Bulletin Database", "Meteoritical Society", "Tuolumne Intrusive Suite", "Navajo Volcanic Field", "Army Corps of Engineers", "Monument Rocks", "Merensky Reef", "Batu Hijau", "Kilbourne Hole", "schistes lustrés", "Advanced Chemistry Basins Project", "Chacay Melehue", "Principles of", "IUPAC--IUGS", "Span--Wagner", "ECORS--CROP", "Fe--FeS", "Konservat-Lagerstätte"]
CITED_RE = re.compile("|".join(r"\s+".join(map(re.escape, c.split())) for c in sorted(CITED, key=len, reverse=True)))


def check_file(path: pathlib.Path, findings: list) -> None:
    raw = path.read_text(encoding="utf-8")
    rel = str(path)
    body = strip_comments(raw)
    body = CITED_RE.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), body)
    # an \includegraphics path on the line after its options is a file name, not prose (physics, 2026-11-18)
    # a TikZ `label={[options]east:text}` names an anchor, not prose (Earth zh Book 4)
    body = re.sub(r"(label=\{\[[^\]]*\])(?:north|south|east|west|above|below|left|right)(?: (?:east|west))?:", r"\1:", body)
    body = re.sub(r"(\\includegraphics(?:\[[^\]]*\])?\s*)\{[^{}]*\}", r"\1{}", body)
    # a figdata table path is a file name, not prose (Earth zh Book 5: `-stereonet-beta.dat`, `-curve-Mars.dat`)
    body = re.sub(r"\{figdata/[^{}]*\}", "{}", body)
    # a photographer's name in a caption credit stays in Latin script, as the licence attributes it: blank the
    # Latin inside \emph{照片：…} (the frame words 照片 and 裁剪 are Chinese; zh_sweeps fixes Photo:/cropped)
    body = re.sub(r"(\\emph\{照片：)((?:[^{}]|\{[^{}]*\})*)\}",
                  lambda m: m.group(1) + re.sub(r"[^\n]", " ", m.group(2)) + "}", body)
    # the same credit written plainly at a caption's end, `照片：Olga Khomitsevich，CC~BY~2.0。}` (physics Book 3)
    body = re.sub(r"(照片：)([^{}\n\\]*)", lambda m: m.group(1) + re.sub(r"[^\n]", " ", m.group(2)), body)
    # and its other lead words (摄影：, 图片：, 肖像：, 照片来源：, 照片由 N. Perscheid 摄), which may run over a line
    # break, up to the closing ）, 。 or brace (chemistry zh Book 3)
    body = re.sub(r"((?:照片|摄影|图片|肖像)(?:来源)?：|照片由)([^{}\\。）]*)",
                  lambda m: m.group(1) + re.sub(r"[^\n]", " ", m.group(2)), body)
    seen = visible_text(body, findings, rel)
    occ: dict = {}

    _flag_latin(seen, body, rel, "english", findings, occ)
    for m in DOTTED_ABBREV.finditer(seen):
        findings.append((rel, _locate(body, m.group(0), occ), "english",
                         f"English abbreviation in visible text: {m.group(0)!r}"))

    for m in LEGEND.finditer(body):
        _flag_latin(MATHLESS.sub(" ", m.group(1)), body, rel, "legend", findings, occ)

    body = _blank_list_commas(body)
    for k, line in enumerate(body.split("\n"), 1):
        line = re.sub(r"\$[^$]*\$", "\x00", line)
        # pgfplots lists are code: the comma separates keys (xticklabels={1月,2月}, symbolic x coords={…})
        line = re.sub(r"(?:[xyz]ticklabels|symbolic [xyz] coords)\s*=\s*\{[^{}]*\}", "\x00", line)
        # \foreach lists are code too: `{0/视觉, 2.4/听觉,` (physics zh, 2026-11-18)
        line = re.sub(r"(?:[\d.]+/)+(?:[^,{}]|\{[^{}]*\})*,", "\x00", line)
        line = re.sub(r"\\legend\{(?:[^{}]|\{[^{}]*\})*\}?", "\x00", line)   # one brace level: \legend{\qty{100}{mL} 纯水, …}
        line = re.sub(r"\bl[_^]?=[^,\]]*,", "\x00", line)   # circuitikz `to[generic, l=偶极子, v=…]`: the comma is code   # \legend{无摩擦, 有摩擦}: the comma separates entries
        # an index key never prints its `!` (sub-entry); `\text{ (或 } \C)` in display math pairs with a math `)`
        line = re.sub(r"\\index\{[^{}]*(?:\}|$)|\\text\{ \(", "\x00", line)  # a key may run on to the next line
        for m in ASCII_PUNCT.finditer(line):
            findings.append((rel, k, "ascii-punct",
                             f"ASCII punctuation in Chinese text: {line[max(0, m.start() - 6):m.end() + 4]!r}"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dirs", nargs="+", help="directories (or single .tex files)")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--max-detail", type=int, default=8)
    args = ap.parse_args()

    findings: list = []
    files = []
    for d in args.dirs:
        p = pathlib.Path(d)
        files += sorted(p.glob("*.tex")) if p.is_dir() else ([p] if p.suffix == ".tex" and p.exists() else [])
    if not files:
        print("  chinese prose gate: no .tex file found in the arguments")
        return 1
    for f in files:
        check_file(f, findings)

    if not findings:
        print(f"  chinese prose gate: OK ({len(files)} files)")
        return 0
    by_class: dict = {}
    for rel, line, cls, msg in findings:
        by_class.setdefault(cls, []).append((rel, line, msg))
    print(f"  chinese prose gate: {len(findings)} issue(s) in {len(files)} files")
    for cls in sorted(by_class):
        hits = by_class[cls]
        print(f"    {cls:<14} {len(hits):>5} hit(s) in {len({h[0] for h in hits})} file(s)")
        if not args.quiet:
            for rel, line, msg in hits[:args.max_detail]:
                print(f"        {rel}:{line}: {msg}")
            if len(hits) > args.max_detail:
                print(f"        ... {len(hits) - args.max_detail} more")
    return 1


if __name__ == "__main__":
    sys.exit(main())
