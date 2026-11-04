#!/usr/bin/env python3
"""Indonesian-specific hygiene gate for a translated tree.

check_translation.sh proves *structure*: same files, same labels, same
environment census. Its prose gates prove almost nothing here -- gate 6 looks
for TeX accent escapes, which Indonesian never writes (the orthography is
plain ASCII), and the drafty-"..." gate is script-agnostic. So an Indonesian
tree can pass every existing gate and still be half English.

**Indonesian is the hard case, and it is hard for the opposite reason to
Hindi.** The Devanagari and Arabic gates can flag *any* Latin word in visible
text, because in those editions Latin script is itself the defect. Indonesian
is written in the same alphabet as the English source, so a forgotten
sentence, a forgotten TikZ node or a forgotten \\text{...} is invisible to
that rule. The only safe detector is the inverse: a **curated list of English
words that are not also Indonesian words**, plus a density heuristic for
sentences that were never touched at all.

This is the One Chemistry Book copy of the One Biology Book gate: the physics
gate plus a BIOLOGY block in each list (marked "biology" below), plus a
CHEMISTRY block in ENGLISH_CONTENT. The word lists are subject-specific, not
only language-specific, and copying one across subjects without re-tuning it
is how a gate starts firing on correct prose. The loudest example is "air",
which is Indonesian for WATER -- it is on nearly every page of a physics book
AND of a biology one. The biology-specific trap is the loanword: Indonesian
writes "organ", "protein", "virus", "vitamin", "habitat", "predator",
"larva", "nitrogen", "antigen", "insulin", "hormon" and "enzim" much as
English does, so those go to NOT_GATED and their ENGLISH PLURALS are gated
instead -- Indonesian pluralises by reduplication or not at all, never with
an -s.

Every entry in ENGLISH_WORDS below was checked against Indonesian. Words that
are spelled identically in both languages are deliberately absent and listed
in NOT_GATED with the reason -- "data", "total", "real", "ring", "limit",
"integral", "unit", "area", "set", "median", "mode" are ordinary Indonesian
and flagging them would make the gate unusable.

Failure classes this script detects:

  1. `english`      -- a listed English word in visible text: prose, TikZ node
                       text, \\text{...} inside math, chapter/section titles,
                       environment optional titles, \\index keys.
  2. `untranslated` -- a long visible sentence containing not one of the
                       commonest Indonesian function words. An Indonesian
                       sentence of eight words essentially always contains a
                       "yang", "dan", "di", "dari", "untuk", "adalah", ...;
                       one that does not was never translated.
  3. `math-space`   -- MT-injected spaces inside inline math ("$P $ dan $ Q $"),
                       detected by the shared reduction.
  4. `redup-space`  -- plural reduplication written with spaces around the
                       hyphen ("bilangan - bilangan"). Invisible in print,
                       fatal to the term linker's word boundaries.
  5. `enclitic`     -- the enclitic -nya written as a separate word
                       ("turunan nya"), which is not Indonesian and again
                       breaks term matching.
  6. `split-number` -- a thin space splitting a word from a thousands group
                       ("bilangan\\,000"), the class that damaged Hindi when
                       MT moved a number out of "Numbers up to 10\\,000".

The LaTeX reduction is imported from tools/check_hindi_prose.py rather than
copied: it is language-independent (it drops technical macro arguments, keeps
\\text{...} inside math, pulls visible strings out of tikz/pgfplots drawing
code) and one implementation is better than three.

Usage:
    python3 tools/check_indonesian_prose.py parts/grade-3/id parts/grade-3/solutions/id
    python3 tools/check_indonesian_prose.py --quiet <dir> ...

Exit status is 1 if anything was flagged. Called by check_translation.sh for
lang == id; safe to run by hand on a single directory while translating.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

from check_hindi_prose import (  # noqa: E402  -- shared, language-independent
    LATIN_WORD,
    _locate,
    strip_comments,
    visible_text,
)

# ---------------------------------------------------------------------------
# 1. Residual English.
# ---------------------------------------------------------------------------
# Grammar words. None of these is a word in Indonesian in any spelling, so the
# match is case-insensitive: "The" at the head of a forgotten sentence and
# "the" mid-line are the same defect.
ENGLISH_FUNCTION = {
    "the", "a", "an", "and", "or", "but", "if", "then", "else", "so", "thus",
    "hence", "therefore", "because", "since", "while", "when", "where",
    "which", "whose", "that", "this", "these", "those", "there", "here",
    "of", "to", "in", "on", "at", "by", "for", "from", "into", "onto",
    "with", "without", "within", "about", "above", "below", "under", "over",
    "between", "among", "through", "during", "after", "before", "until",
    "we", "us", "our", "you", "your", "they", "them", "their", "it", "its",
    "he", "she", "him", "her", "his", "who", "what", "how", "why",
    "is", "are", "was", "were", "be", "been", "being", "am",
    "has", "have", "had", "do", "does", "did", "can", "cannot", "could",
    "will", "would", "shall", "should", "must", "might", "may",
    "no", "yes", "all", "any", "both", "each", "every", "some",
    "many", "much", "more", "most", "less", "least", "few", "several",
    "same", "other", "another", "such", "only", "also", "even", "still",
    "first", "second", "third", "last", "next", "previous", "then",
    "let", "given", "using", "note", "recall", "suppose", "assume",
    "consider", "observe", "indeed", "conversely", "moreover", "however",
    "again", "always", "never", "often", "sometimes", "now", "once",
    "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    # Appended for Book 3 (University Year 1). A university book argues, so it
    # leans on a wider set of connectives and relational words than the school
    # books did; each of these was checked against KBBI. "as" is deliberately
    # ABSENT -- see NOT_GATED.
    "than", "along", "inside", "outside", "against", "across", "toward",
    "towards", "apart", "away", "out", "off", "alone", "own", "itself",
    "behind", "around", "beyond", "instead", "just", "too", "almost",
    "together", "whatever", "nothing", "well", "way", "like", "part",
    # "new" is NOT here: the set is matched case-insensitively and it fired on
    # "New York" in the shipped grade-10 id chapter on optical fibre.
    "whether", "unless", "whereas", "throughout", "everywhere", "anywhere",
    "twice", "once", "enough", "rather", "quite", "very", "already",
}
# "no" is kept out of the short-token pass below, because "No." for "nomor"
# is ordinary Indonesian in a table head; it is listed here and screened by
# NUMBER_ABBREV instead.

# Content words a maths translation leaves behind. Every one was checked not to
# be Indonesian (see NOT_GATED for the ones that are).
ENGLISH_CONTENT = {
    # book furniture
    "chapter", "section", "page", "pages", "exercise", "exercises",
    "problem", "problems", "solution", "solutions", "proof", "proofs",
    "theorem", "theorems", "definition", "definitions", "proposition",
    "lemma", "corollary", "example", "examples", "remark", "remarks",
    "method", "notation", "figure", "table", "answer", "answers", "hint",
    # arithmetic and number
    "number", "numbers", "integer", "integers",
    "fraction", "fractions", "decimal", "decimals", "sum", "difference",
    "product", "quotient", "remainder", "divisor", "multiple", "prime",
    "even", "odd", "add", "adds", "subtract", "multiply", "divide",
    "addition", "subtraction", "multiplication", "division", "count",
    "half", "quarter", "third", "double", "rounding", "round",
    "percentage", "percent", "average", "power", "powers", "root", "roots",
    "square", "cube", "squared", "negative", "positive",
    # geometry and measure
    "line", "lines", "point", "points", "segment", "angle", "angles",
    "circle", "triangle", "rectangle", "polygon", "shape", "shapes",
    "side", "sides", "vertex", "edge", "face", "faces", "length", "width",
    "height", "depth", "surface", "distance",
    "perpendicular", "symmetry", "rotation", "translation",
    "left", "right", "middle", "centre", "center", "scale",
    # algebra and analysis
    "equation", "equations", "inequality", "unknown", "variable",
    "function", "functions", "graph", "slope", "coefficient", "polynomial",
    "sequence", "series", "convergent", "convergence", "divergent",
    "continuous", "continuity", "derivative", "differentiable", "bounded",
    "increasing", "decreasing", "maximum",
    "neighbourhood", "neighborhood", "subset",
    "mapping", "matrix", "matrices", "vector", "vectors",
    "dimension", "kernel", "image", "eigenvalue", "eigenvector",
    "subspace", "orthogonal", "invertible", "determinant",
    "measure", "measurable", "probability", "random", "outcome", "event",
    "expectation", "variance", "distribution", "sample",
    # environment optional titles -- the class that shipped green (see
    # ENGLISH_SUFFIX_CAP and the `title` class below)
    "property", "properties", "characterization", "linearization",
    "invertibility", "expansion", "cofactor", "system", "systems",
    "isometry", "isometries", "plane", "case", "cases", "converse",
    "uniqueness", "existence", "criterion", "criteria",
    # place-value furniture, the commonest leftover in TikZ node text
    "thousand", "hundred", "tens", "ones", "metres", "meters",
    # verbs an exercise stem uses
    "compute", "calculate", "find", "show", "prove", "deduce", "explain",
    "justify", "draw", "write", "read", "complete", "check", "state",
    "simplify", "expand", "factor", "factorise", "factorize", "solve",
    "compare", "estimate", "measure", "order", "sort", "list", "give",
    # ---- physics -----------------------------------------------------------
    # Quantities and their names. Indonesian spells each of these differently
    # (gaya, massa, berat, kelajuan, kecepatan, energi, kalor, gelombang, ...),
    # so the English form in visible text is always a defect. Words ending in
    # -tion/-ght (motion, friction, reflection, refraction, acceleration,
    # radiation, light, weight, height, bright, night) are already caught by
    # ENGLISH_SUFFIX and are deliberately not repeated here.
    "force", "forces", "mass", "weight", "speed", "velocity", "energy",
    "heat", "work", "wave", "waves", "wavelength", "frequency", "amplitude",
    "period", "sound", "mirror", "mirrors", "lens", "lenses", "ray", "rays",
    "beam", "shadow", "shadows", "rainbow", "eclipse", "spectrum",
    "current", "voltage", "charge", "charges", "circuit", "circuits",
    "battery", "bulb", "lamp", "switch", "wire", "wires", "coil", "magnetic",
    "electric", "electron", "electrons", "photon", "photons", "nucleus",
    "nuclear", "radioactive", "isotope", "molecule", "molecules", "crystal",
    "vacuum", "pressure", "temperature", "density", "gravity", "inertia",
    "spring", "string", "rope", "pulley", "lever", "ramp", "block",
    "ball", "screen", "source", "object", "objects", "compass", "diode",
    "capacitor", "transformer", "turbine", "satellite", "comet",
    "quantum", "relativity", "efficiency", "resonance", "diffraction",
    "capacitance", "conductor", "insulator", "prism", "focus",
    # Sight/hearing/... : the five-senses chapter, and single-word TikZ node
    # labels generally -- a node text is too short for the sentence-density
    # class, so a word list is the only thing that sees it.
    "sight", "hearing", "touch", "smell", "taste", "eye", "eyes", "ear",
    "ears", "nose", "tongue", "skin", "hot", "cold", "warm", "cool",
    "north", "south", "east", "west", "up", "down", "top", "bottom",
    "front", "back", "near", "far", "fast", "slow", "heavy", "big",
    "small", "start", "stop", "time", "times", "sun", "moon", "earth",
    "star", "stars", "water", "ice", "steam", "glass", "wood", "metal",
    "iron", "copper", "sand", "stone", "float", "sink", "melt", "freeze",
    "boil", "push", "pull", "axis", "pole", "poles",
    # English plurals of nouns spelled the SAME in both languages. Indonesian
    # pluralises by reduplication (magnet-magnet), never with -s, so the plural
    # is unambiguously English even though the singular is unambiguously not.
    # The -s/-es stem rule cannot reach them: their stems are in NOT_GATED.
    "magnets", "gases", "atoms", "ions", "protons", "neutrons", "orbits",
    "planets", "lasers", "motors", "radios", "resistors", "meteors",
    # ---- biology -----------------------------------------------------------
    # Body, organism and ecology vocabulary. Indonesian spells every one of
    # these differently (sel, daun, akar, batang, darah, jantung, paru-paru,
    # tulang, otot, otak, telur, sarang, mangsa, ...), so the English form in
    # visible text is always a defect. Words already caught by ENGLISH_SUFFIX
    # (respiration, digestion, circulation, nutrition, reproduction,
    # pollination, germination, evolution, adaptation, growth, health, ...)
    # are deliberately not repeated here.
    "cell", "cells", "tissue", "tissues", "nucleus", "membrane", "cytoplasm",
    "chromosome", "chromosomes", "gene", "genes", "seed", "seeds", "leaf",
    "leaves", "root", "roots", "stem", "stems", "flower", "flowers", "petal",
    "petals", "stamen", "pistil", "pollen", "fruit", "fruits", "sap", "bud",
    "buds", "trunk", "branch", "branches", "bark", "sprout", "shoot",
    "blood", "heart", "lung", "lungs", "bone", "bones", "muscle", "muscles",
    "brain", "nerve", "nerves", "stomach", "gut", "liver", "kidney",
    "kidneys", "intestine", "intestines", "throat", "lip", "lips", "tooth",
    "teeth", "jaw", "jaws", "claw", "claws", "paw", "fur", "feather",
    "feathers", "wing", "wings", "beak", "gill", "gills", "fin", "fins",
    "scale", "scales", "shell", "shells", "tail", "egg", "eggs", "nest",
    "nests", "burrow", "hive", "web", "cocoon", "chrysalis", "tadpole",
    "seedling", "sapling", "offspring", "young", "male", "female", "breath",
    "breathe", "breathing", "digest", "swallow", "chew", "sweat", "urine",
    "waste", "germ", "germs", "microbe", "microbes", "bacterium", "bacteria",
    "fungus", "mould", "mold", "yeast", "spore", "spores", "vaccine",
    "antibody", "antibodies", "disease", "diseases", "illness", "wound",
    "prey", "predator's", "hunter", "grazer", "herbivore", "carnivore",
    "omnivore", "burrower", "swarm", "flock",
    "herd", "colony", "pond", "meadow", "forest", "wood", "desert", "swamp",
    "river", "shore", "soil", "burrowing", "flowering",
    "living", "non-living", "alive", "dead", "birth",
    "sunlight", "warm-blooded", "cold-blooded", "backbone", "vertebrate",
    "invertebrate", "mammal", "mammals", "bird", "birds", "fish", "insect",
    "insects", "spider", "spiders", "worm", "worms", "snail", "snails",
    "frog", "frogs", "butterfly", "caterpillar", "bee", "bees", "ant",
    "ants", "tree", "trees", "grass", "moss", "fern", "algae",
    # English plurals of biology nouns spelled the SAME in both languages.
    # Indonesian pluralises by reduplication (organ-organ) or not at all,
    # never with an -s, so the plural is unambiguously English even though
    # the singular is unambiguously not. The -s/-es stem rule cannot reach
    # them: their stems sit in NOT_GATED.
    "organs", "proteins", "viruses", "vitamins", "habitats", "predators",
    "larvae", "hormones", "enzymes", "fossils",
    "embryos", "parasites", "nutrients", "molecules",
    # ---- university physics (Book 3) ---------------------------------------
    # Harvested from the English bodies of parts/bachelor-1 and filtered
    # against KBBI: the Indonesian of each of these is a DIFFERENT string
    # (medan, hukum, tetapan, fase, entropi, momen, torsi, ...), so the
    # English form in visible text is always a defect. Words already caught
    # by ENGLISH_SUFFIX (-tion, -ance, -ence, -ous, -ly, -ght, -th: friction,
    # resistance, impedance, difference, continuous, length, ...) are not
    # repeated here, and neither are the ones Indonesian spells identically
    # (see NOT_GATED -- radius, uniform, loop, model, input, output, ...).
    "field", "fields", "law", "laws", "constant", "constants", "phase",
    "entropy", "enthalpy", "potential", "flux", "torque", "dipole",
    "moment", "moments", "cycle", "cycles", "frame", "frames", "value",
    "values", "ratio", "signal", "signals", "body", "bodies", "ground",
    "rest", "mean", "liquid", "vapour", "vapor", "fluid", "fluids",
    "particle", "particles", "displacement", "equilibrium", "magnitude",
    "oscillator", "oscillators", "pendulum-bob", "damping", "harmonic",
    "harmonics", "adiabatic", "reversible", "irreversible", "engine",
    "engines", "pump", "sphere", "spheres", "cylinder", "cylinders",
    "plate", "plates", "coil", "coils", "wall", "walls", "tube", "cable",
    "wheel", "wheels", "rod", "rods", "bar-magnet", "hull", "vessel",
    "bottle", "floor", "road", "car", "cars", "machine", "machines",
    "refrigerator", "thermostat", "telescope", "microscope", "eyepiece",
    "objective", "antenna", "receiver", "transmitter",
    "amplitude-gain", "cyclotron", "buoyancy", "curvature", "latitude",
    "tangent", "element", "elements", "index", "rule", "rules", "beat",
    "beats", "mole", "hydrogen", "atmosphere", "steel", "fuel", "sea",
    "bridge", "branch", "threshold", "peak", "gap", "drop", "drops",
    "load", "rate", "sign", "curve", "core", "thin", "turn", "turns",
    "zero", "size", "single", "free", "full", "change", "changes",
    "equal", "equals", "red", "blue", "green", "black", "white",
    "electricity", "uncertainty", "weekend", "week", "day", "year",
    "room", "house",
    # adjectives and adverbs: Indonesian writes kinetik, listrik, mekanis,
    # optis, relatif, sentral, vertikal, sirkular, aksial -- never these.
    "kinetic", "electrical", "mechanical", "optical", "inertial",
    "relative", "central", "vertical", "circular", "cylindrical",
    "spherical", "axial", "external", "independent", "infinite", "finite",
    "visible", "negligible", "dimensionless", "conservative", "critical",
    "steady", "maximal", "minimal", "partial", "extra", "little",
    "quadratic", "symmetric", "local", "initial", "stable", "unstable",
    "simple", "perfect", "common", "open", "closed", "opposite",
    "downward", "upward", "outward", "inward", "clockwise",
    # -ing and -ed forms. ENGLISH_SUFFIX deliberately gates neither ending
    # (penting, masing-masing; and -ed would fire on surnames), so the ones
    # a physics figure label actually uses are listed by hand.
    "boiling", "melting", "freezing", "cooling", "heating", "converging",
    "diverging", "falling", "sliding", "rolling", "charged", "closed-loop",
    # ---- university biology (Book 3) ---------------------------------------
    # Harvested from the English bodies of parts/bachelor-1 and validated
    # against 1.6 MB of the SHIPPED Indonesian prose of Books 1-2 (214 files,
    # reduced with visible_text): every word below occurs there exactly zero
    # times, and its Indonesian is a different string -- glukosa, spesies,
    # enzim, manusia, xilem, floem, asam, untai, pertukaran, karbon, gula,
    # heliks, tumbuhan, aliran, ikatan, fosfat, ekson, glikogen, oksigen,
    # piruvat, promotor, cahaya, sekunder, primer, liter, genom, polimerase,
    # faktor, relung, pohon ek, asal, kadal, zona, bukti, anggaran, kontrol,
    # aktif, metabolik, pati, sukrosa, selulosa, nukleotida, kodon, ribosom,
    # organel, substrat, gradien, membran, vakuola, lisosom, kloroplas,
    # mitokondria, karbohidrat, kromatin, nukleoid, tilakoid, telomer,
    # sentromer, histon, katalis, reseptor, difusi, glikolisis, biomassa,
    # bioma. The ones Indonesian DOES spell identically (lipid, intron,
    # amino, plasmid, operon, ...) are in NOT_GATED instead -- "lipid" was on
    # this list until it fired 46 times on correct shipped grade-10 prose.
    "glucose", "species", "enzyme", "human", "xylem", "phloem", "acid",
    "acids", "strand", "strands", "exchange", "carbon", "sugar", "sugars",
    "helix", "plant", "plants", "flow", "bond", "bonds", "phosphate",
    "exon", "exons", "glycogen", "oxygen", "pyruvate", "promoter", "light",
    "secondary", "primary", "lipids", "fatty", "fat", "litre", "genome",
    "polymerase", "factors", "niche", "oak", "origin", "hairs", "lizard",
    "digestive", "zone", "evidence", "budget", "control", "active",
    "metabolic", "starch", "sucrose", "cellulose", "nucleotide",
    "nucleotides", "codon", "codons", "ribosome", "ribosomes",
    "organelles", "substrates", "gradients", "membranes", "vacuoles",
    "lysosomes", "chloroplasts", "mitochondrion", "carbohydrate",
    "carbohydrates", "chromatin", "nucleoid", "thylakoid", "telomere",
    "centromere", "histone", "catalyst", "receptor", "gradient",
    "diffusion", "glycolysis", "biomass", "biome",
}

# ---- chemistry (One Chemistry Book, 2026-10-04) --------------------------
# English chemistry vocabulary that is NOT Indonesian: Indonesian respells the
# loan (klorida, oksida, karbonat, etanol, metana, amonia, kovalen, elektroda,
# kristal, netral, polimer, oktet), so the English spelling is unambiguous.
# Picked from the canon's own frequency list, by hand. Deliberately LEFT OUT
# because they are also Indonesian words: ester, molar, argon, sulfur,
# material, solid, aspirin, singlet, triplet, meso, anti, mol, ion, atom, gas,
# orbital, magnesium, aluminium, tetrahedral, anode (all four fired on the shipped
# biology `id` editions, the silent control), isomer (its English plural "isomers" is gated instead).
ENGLISH_CONTENT |= {
    "chloride", "bromide", "iodide", "oxide", "dioxide", "monoxide",
    "peroxide", "hydroxide", "carbonate", "nitrate", "sulfate",
    "permanganate", "sodium", "potassium", "calcium", "lithium", "chlorine", "bromine", "iodine", "silver",
    "zinc", "silicon", "dioxygen", "ammonia", "methane", "ethane",
    "ethanol", "methyl", "ethyl", "ether", "cyclohexane", "propanone",
    "ethanoic", "ethanoate", "hydrochloric", "sulfuric", "alkene",
    "ketone", "aldehyde", "carbonyl", "acetal", "alcohol", "alcohols",
    "salt", "solvent", "solvents", "solute", "mixture", "compound",
    "compounds", "reactant", "reactants", "reagent", "products",
    "react", "reacts", "reactions", "dissolve", "dissolves", "dissolved",
    "dissolving", "dilute", "diluted", "concentrated", "concentrations",
    "precipitate", "solubility", "acidic", "acidity", "covalent", "ionic",
    "atomic", "molecular", "equatorial", "chiral",
    "racemic", "enantiomers", "stereoisomers", "isomers", "nucleophile",
    "oxidant", "reductant", "oxidised", "titrated", "titrant", "buffer",
    "electrode", "subshell", "octet", "anions", "cations",
    "crystals", "flask", "flame", "flammable", "vinegar", "chemist",
    "chemical", "substances", "mechanism", "intermediate", "tertiary",
    "neutral", "balanced", "formulas", "conductivity", "colour",
    "weak", "strong", "pure", "layer", "chain", "chair", "polymer",
}

# Time adverbs (2026-10-04): an untranslated "later" in a grade-3 arrow label
# passed this gate and was caught only by gate 9's advisory tier (Indonesian
# chemistry Book 1 agent). None is an Indonesian word.
ENGLISH_FUNCTION |= {"later", "earlier", "soon", "meanwhile", "afterwards"}

ENGLISH_WORDS = ENGLISH_FUNCTION | ENGLISH_CONTENT

# Deliberately NOT gated -- identical or near-identical in Indonesian, so a
# hit would be a false alarm on correct prose. Kept as a list so the next
# agent does not "helpfully" add them.
NOT_GATED = {
    "data", "total", "real", "ring", "grup", "limit", "integral", "unit",
    "area", "set", "median", "modus", "mode", "faktor", "vektor", "matriks",
    "normal", "positif", "negatif", "final", "modul", "ideal", "kernel",
    "domain", "kompleks", "abstrak", "aljabar", "analisis", "geometri",
    # spelled identically in both languages -- KBBI has all of these. Each one
    # was in ENGLISH_CONTENT until it fired on correct Indonesian prose.
    # "not" is Indonesian for a MUSICAL note (from Dutch "noot"; "not balok" is
    # staff notation). It fired ~35 times on the correct grade-7 fractions
    # chapter, whose weekend problem is about note values. Losing English "not"
    # costs nothing: a forgotten English sentence containing "not" always
    # carries "is"/"the"/"does" as well, and the `untranslated` class sees it.
    "not",
    "minimum", "supremum", "infimum", "volume", "basis", "linear",
    "interval", "parallel", "perimeter", "digit", "digits", "meter",
    "koordinat", "gradien", "polinomial", "determinan", "ortogonal",
    "konvergen", "divergen", "kontinu", "dimensi", "variabel", "skala",
    "desimal", "persen", "segmen", "poligon", "kubus", "sampel",
    # ---- physics -----------------------------------------------------------
    # "air" is Indonesian for WATER. It is on nearly every page of Book 1
    # (air panas, air mendidih, permukaan air, air raksa) and gating the
    # English word "air" would fire hundreds of times on perfect prose. This is
    # the physics twin of "not" (a musical note) in the math copy: losing
    # English "air" costs nothing, because a forgotten English sentence about
    # air always carries "the"/"is"/"of" with it and the `untranslated` class
    # sees it.
    "air",
    # "bar" is the pressure unit, written the same in both languages.
    "bar",
    # Spelled identically in Indonesian and English -- KBBI has all of them.
    # Their ENGLISH PLURALS are gated instead (see ENGLISH_CONTENT).
    "magnet", "gas", "atom", "ion", "proton", "neutron", "orbit", "planet",
    "laser", "motor", "radio", "momentum", "plasma", "meteor", "resistor",
    "spektrum", "generator", "isolator", "konduktor", "kapasitor", "dioda",
    "transformator", "dinamo", "turbin", "satelit", "komet", "kompas",
    "prisma", "fokus", "lensa", "optik", "kuantum", "relativitas", "inersia",
    "isotop", "molekul", "kristal", "vakum", "nuklir", "radioaktif",
    "elektron", "foton", "amplitudo", "frekuensi", "periode", "resonansi",
    "difraksi", "interferensi", "polarisasi", "refraksi", "radiasi",
    "konveksi", "konduksi", "efisiensi", "gravitasi", "energi", "termometer",
    "barometer", "voltmeter", "amperemeter", "galvanometer", "spektroskop",
    # SI unit names, spelled the same in both languages wherever they are
    # written out rather than symbolised. (Unit SYMBOLS never reach visible
    # text: \qty, \unit, \num and \SI drop their arguments in the shared
    # reduction.)
    "newton", "joule", "watt", "volt", "ampere", "ohm", "kelvin", "hertz",
    "pascal", "tesla", "weber", "farad", "henry", "becquerel", "sievert",
    "candela", "lumen", "coulomb",
    # ---- biology -----------------------------------------------------------
    # Indonesian borrowed most of the life-science vocabulary with the
    # spelling intact, so each of these is a perfectly ordinary Indonesian
    # word AND an English one. Gating any of them fires on correct prose;
    # their ENGLISH PLURALS are gated instead (see ENGLISH_CONTENT), which is
    # unambiguous because Indonesian has no -s plural.
    "organ", "protein", "virus", "vitamin", "insulin", "habitat", "predator",
    "larva", "pupa", "nitrogen", "antigen", "alga", "fungi", "flora", "fauna",
    "urine", "sperma", "gen", "sel", "hormon", "enzim", "bakteri", "fosil",
    "spesies", "populasi", "ekosistem", "parasit", "nutrisi", "embrio",
    "kromosom", "mitokondria", "kloroplas", "glukosa", "oksigen", "karbon",
    "hidrogen", "kalsium", "antibodi", "vaksin", "mikroba", "reptil",
    "mamalia", "amfibi", "serangga", "nektar", "klorofil", "metabolisme",
    "fotosintesis", "respirasi", "evolusi", "adaptasi", "reproduksi",
    "nukleus", "membran", "sitoplasma", "jaringan", "organisme",
    # "biji" is a seed, "bibit" a seedling -- neither collides; listed only so
    # the next agent does not add the English "seed" twice.
    # ---- university physics (Book 3) ---------------------------------------
    # "as" is Indonesian for an AXLE (as roda, as putar) -- and Book 3 is half
    # mechanics. Gating English "as" would fire on correct prose exactly the
    # way "air" (water) and "not" (a musical note) would; the same argument
    # applies: a forgotten English sentence containing "as" always carries
    # "the"/"is"/"of" as well, and the `untranslated` class sees it.
    "as",
    # "per" is Indonesian too (meter per detik) -- and it is on every page of
    # a mechanics book.
    "per",
    # Loanwords KBBI spells exactly as English does. Every one of these was in
    # the block above until it fired on correct Indonesian physics prose;
    # re-adding any of them to ENGLISH_CONTENT will break a green gate.
    "radius", "uniform", "loop", "model", "input", "output", "pendulum",
    "amplifier", "horizontal", "radial", "pupil", "virtual", "sinusoidal",
    "solenoid", "solenoida", "filter", "level", "medium", "polar", "formula",
    "diagram", "spin", "sensor", "terminal", "fiber", "natural", "helium",
    "internal", "alternator", "starter", "diesel", "rigid", "rim", "net",
    "disk", "feedback", "emf", "ggl", "torsi", "kalor", "usaha",
    # "camera obscura" is a Latin phrase Indonesian keeps verbatim (it is in
    # the shipped grade-6 id chapter three times); the device itself is
    # "kamera", so gating the English spelling would cost a false alarm on
    # correct prose for no coverage.
    "camera",
    "kilogram", "sentimeter", "milimeter", "kilometer", "detik", "sekon",
    # Indonesian technical vocabulary that happens to be Latin-looking and
    # would otherwise trip the -s plural rule or a suffix.
    # ---- appended by the Indonesian Biology Book 2 agent, 2026-09-05 -------
    # "minimal" is ordinary Indonesian (KBBI; "medium minimal", "suhu
    # minimal", "biaya minimal") and fired on the correct grade-11 sentence
    # about Beadle and Tatum's minimal medium. Its neighbour "minimum" was
    # already in this set for the same reason; "minimal" was simply missed.
    "minimal",
    "impuls", "fluks", "entropi", "entalpi", "adiabatik", "isotermal",
    # ---- university biology (Book 3), 2026-09-05 ---------------------------
    # KBBI spells each of these exactly as English does, so gating any of them
    # fires on correct Indonesian prose. "lipid" is not hypothetical: it was in
    # ENGLISH_CONTENT above until it hit 46 times in the shipped grade-10 and
    # grade-11 chapters ("karbohidrat, lipid, protein, asam nukleat"). The rest
    # are listed so the next agent does not re-add them: check here first.
    # "kation" is ordinary Indonesian (KBBI) for the cation, and it ends in
    # -tion, so ENGLISH_SUFFIX gated it. There is no English homograph to
    # miss: English spells it "cation", with a c. Its partner "anion" was
    # never gated only because -on is not a listed suffix -- an accident, not
    # a decision. Reported by the Indonesian Biology Book 3 agent, 2026-09-06,
    # which had written "ion positif"/"ion negatif" to get past the gate;
    # kation/anion is the pair a lecture uses.
    "kation", "anion",
    "lipid", "intron", "amino", "basal", "plasmid", "operon", "steroid",
    "monomer", "dimer", "isomer", "inhibitor", "osmosis", "mitosis",
    "meiosis", "stroma", "grana", "optimum", "optimal", "nonpolar",
    "kodon", "genom", "organel", "substrat", "gradien", "ribosom",
    "nukleotida", "sitoskeleton", "vakuola", "lisosom", "tilakoid",
    "isobarik", "isokorik", "kapasitas", "resistansi", "impedansi",
    "induktansi", "kapasitansi", "reaktansi", "amplitudo", "fase",
    "harmonik", "osilator", "osilasi", "resonansi", "difraksi", "refleksi",
    "dioptri", "lensa", "cermin", "medan", "gaya", "massa", "berat",
    # "karbokation" is the Indonesian chemistry term for the carbocation
    # (karbo- + kation, already exempted above for the same reason); it ends
    # in -tion, so ENGLISH_SUFFIX gated it. English spells it "carbocation",
    # with a c, so no English word is lost. Appended by the Indonesian
    # Chemistry Book 1 agent, 2026-10-04 (grade-12 curly-arrows chapter).
    "karbokation",
    # The REDUPLICATED plurals of the two words above. LATIN_WORD keeps a
    # hyphen inside a word, so "kation-kation" (the cations, the ordinary
    # Indonesian plural) is looked up as ONE token, misses the singular's
    # NOT_GATED entry and fires ENGLISH_SUFFIX (-tion) on correct prose.
    # (A general fix -- test each half of a reduplication X-X against these
    # sets -- belongs in the logic; reported, not made.) Appended by the
    # Indonesian Chemistry Book 2 agent, 2026-10-04 (ch. 5, metallic bond).
    "kation-kation", "karbokation-karbokation",
    # "glutation" is the Indonesian spelling of the tripeptide glutathione
    # (Chemistry Book 4, ch. 19 solutions, the cell's sulfur ligands that
    # deactivate cisplatin); it ends in -tion, so ENGLISH_SUFFIX gated it.
    # English spells it "glutathione", so no English word is lost. Appended
    # by the Indonesian Chemistry Book 4 agent, 2026-10-06.
    "glutation",
}

# Brand, markup names and unit symbols that legitimately stay Latin.
ALLOWED = {
    # "ons" is the Indonesian hectogram (100 g), an ordinary noun -- but it is
    # not caught by this set alone: the PLURAL-STEM rule strips the "s", finds
    # "on" in ENGLISH_WORDS and fires. Reported by the Indonesian Book 4 agent,
    # 2026-09-16. Note the gate was right to be suspicious: "ons" is 100 g and
    # NOT the imperial ounce, so rendering Harvey's "2 ounces" as "2 ons" would
    # have falsified the arithmetic (that edition uses "auns").
    "ons",
    # A PROPER NAME that ends in an English suffix. "Lawrence Berkeley
    # Laboratory" is the institution credited for the Melvin Calvin
    # photograph, kept verbatim by all four wave-1 editions because a credit
    # line names a real body -- but "Lawrence" ends in -ence, so
    # ENGLISH_SUFFIX_CAP flagged it. Note the deliberate NON-entry beside it:
    # "Foundation" (in "Nobel Foundation") fires on the same rule and is NOT
    # exempted, because there translation IS correct -- wave 1 wrote
    # Fondation / Fundacion / Nobelstichting, and Indonesian writes "Yayasan
    # Nobel". The distinction is a name component versus a common noun, and it
    # cannot be drawn by suffix, only by listing. Reported by the Indonesian
    # Biology Book 3 agent, 2026-09-06.
    # ("lawrence" lived here briefly and was WITHDRAWN in favour of an
    # ATTRIBUTION entry for the whole phrase "Lawrence Berkeley Laboratory":
    # an ALLOWED token passes everywhere in the book, an ATTRIBUTION phrase
    # only where the institution is actually named.)
    "one", "course", "com", "www", "http", "https", "math", "book",
    "tex", "latex", "pdf", "html", "github", "md",
    "si", "iso", "cm", "mm", "km", "kg", "mg", "ml", "hz", "rad",
    # Appended by the Book 2 id edition. Chemical element symbols are
    # international and print unchanged in every language; they reach the
    # gate whenever a figure label sets the mass number in math and leaves
    # the symbol outside it ("{$^{4}$He}" in the binding-energy curve).
    # Only the symbol that actually collides with an English word is listed:
    # "he". A genuine English sentence containing "he" still fires on its
    # other words and on the sentence-density rule.
    "he",
    # A DROSOPHILA GENE NAME that is spelled like an English common noun.
    # parts/bachelor-3/02-rna-regulation.tex:326,330 print the gene
    # \emph{transformer} (tra) of the fly sex-determination cascade; it is a
    # proper name and cannot be translated in any edition. Only the SINGULAR
    # is exempted, deliberately: the ordinary English noun occurs in this
    # repository exactly once, as the PLURAL \emph{transformers}
    # (parts/grade-6/05-matter-from-food.tex:21), and the -s stem rule runs
    # after this test, so that use stays gated. Appended by the Indonesian
    # Biology Book 5 agent, 2026-09-17.
    "transformer",
    # "SOS" -- the bacterial SOS response (parts/bachelor-3/03-dna-repair.tex).
    # It is an international distress signal used as the name of a regulon and
    # is identical in every edition, but .lower() gives "sos", whose -s stem
    # "so" is in ENGLISH_FUNCTION, so the PLURAL rule fires on it. Appended by
    # the Indonesian Biology Book 5 agent, 2026-09-17.
    "sos",
    # "Ames" (the Ames mutagenicity test). The -es PLURAL-STEM rule strips it
    # to "am", which is in ENGLISH_FUNCTION, so a correct Indonesian
    # "\begin{method}[Uji Ames]" fires whenever the preceding word is
    # capitalised and the EPONYM exemption cannot apply. "ames" is not an
    # English word, so listing it costs no coverage. Appended by the
    # Indonesian Biology Book 5 agent, 2026-09-17.
    "ames",
    # XCOLOR NAMES inside a node's OPTION list -- a GATE BUG, reported, not
    # fixed here (the same entry the Hindi Book 2 agent had to append to
    # check_hindi_prose.py). Chemistry Book 2 ch. 6 draws every ion of its
    # crystal cells as \node[aX={green!55!black}{6.5mm}] at (0,0,0) {};
    # TIKZ_NODE (imported from check_hindi_prose.py) stops at the first "{",
    # which lies INSIDE the [...] options, so the colour argument is read as
    # the node's label: ~80 hits on a figure whose labels are all empty, and
    # the drawing code must stay byte-identical to English. The fix belongs in
    # TIKZ_NODE (skip a balanced [...] before looking for the label). Cost of
    # the entry: an untranslated colour word would pass gate 8 anywhere; the
    # Indonesian Book 2 agent greps its tree for these words outside node
    # options instead. Appended by the Indonesian Chemistry Book 2 agent,
    # 2026-10-04.
    "green", "black", "gray", "violet", "blue", "yellow", "orange",
    # A PLACE NAME: "Pegunungan Andes" (Chemistry Book 2 ch. 26, the lithium
    # salt flats). Indonesian keeps the name in Latin like every edition
    # (fr/es/pt/nl all print "Andes"); the -es PLURAL-STEM rule strips it to
    # "and", which is gated English, and no rewording can change a mountain
    # range's name. "andes" is not an English word, so listing it costs no
    # coverage. Appended by the Indonesian Chemistry Book 2 agent, 2026-10-04.
    "andes",
    # A PLACE NAME: Ascension Island, South Atlantic (Earth and Space Book 4,
    # ch. 4, the St. Helena (HIMU) island group). Indonesian keeps the island's
    # name in Latin, as every edition does; it ends in -sion, so
    # ENGLISH_SUFFIX_CAP fires and no rewording can change an island's name.
    # The English common noun "ascension" occurs nowhere in the series.
    # Appended by the Indonesian Earth and Space Book 4 agent, 2026-10-30.
    "ascension",
}

# A curated list cannot be complete, and the words it misses are exactly the
# ones nobody thought of ("thousands" in a place-value node, "metres" in a
# \text{}). Two generic rules close most of that gap without touching correct
# Indonesian:
#
#   * ENGLISH_SUFFIX -- endings Indonesian orthography does not produce. Applied
#     to LOWERCASE words only, which removes the proper-noun risk entirely: the
#     books are full of Smith-shaped surnames and Indonesian keeps them in
#     Latin. "-ing" is deliberately absent (penting, kucing, masing-masing are
#     ordinary Indonesian) and so is "-ed" (it would fire on names).
#   * the plural rule -- a listed noun with an English -s/-es on it.
ENGLISH_SUFFIX = re.compile(
    r"(?:tion|sion|ly|ness|ous|ful|ght|th|ance|ence|ship|hood|wise)$")
# Title-Case words need a NARROWER set. Environment optional titles are Title
# Case ("[Characterization]", "[Linearization]", "[Invertibility mod $n$]"),
# and the lowercase-only rule above let every one of them through a green gate
# -- the one defect class this edition could ship with. But the books are also
# full of surnames, so -th, -ght, -ly and -ous are dropped here: Smith, Booth,
# Wright, Knight would all fire. None of the series' mathematicians (Gauss,
# Cauchy, Riemann, Lebesgue, Frobenius, Legendre, Sylvester, ...) matches this.
ENGLISH_SUFFIX_CAP = re.compile(
    r"(?:tion|sion|ness|ance|ence|ship|hood|wise|ity)$")

# An English possessive is unambiguous: Indonesian has no 's, it writes the
# possessor after the noun (hukum Newton, medan Bumi). Book 3's English bodies
# are full of them ("Newton's third law", "the Earth's field", "Gauss's law"),
# and a forgotten two-word figure label is far too short for the
# sentence-density class to see. LATIN_WORD keeps the apostrophe inside the
# token, so the whole possessive is one match.
ENGLISH_POSSESSIVE = re.compile(r"^[a-z]{2,}'s$")

DOTTED_ABBREV = re.compile(r"\b(?:i\.e\.|e\.g\.|etc\.|cf\.|viz\.)")
# "No. 3" / "no. 3" is Indonesian for "nomor"; "no" elsewhere is English.
NUMBER_ABBREV = re.compile(r"\b[Nn]o\.\s*\d")

# Image attribution that EVERY edition must keep verbatim. A CC licence
# identifier is not a phrase, it is the licence's name; the repository holding
# a photograph is an institution's name. The French edition keeps
# "Wellcome Collection, CC~BY~4.0." unchanged and is right to. Left ungated
# this is unreachable: "Collection" fires on ENGLISH_SUFFIX_CAP (-tion),
# "Commons" on the -s stem rule (common), "BY" on ENGLISH_WORDS after .lower(),
# and there is no way to reword a licence identifier. Blanked here, the way
# NUMBER_ABBREV is, so the surrounding prose stays fully gated.
#
# NOTE "public domain" is deliberately NOT here: that one IS translatable
# (domain publik / domaine público / domínio público) and neither word fires
# on its own. Raised by the Indonesian Book 1 agent, 2026-09-04, which could
# not write its grade-9 Jenner credit at all.
ATTRIBUTION = re.compile(
    r"Wikimedia\s+Commons|Wellcome\s+Collection|Creative\s+Commons"
    r"|\bCC[~\s]?(?:BY(?:[~\s-](?:SA|NC|ND))*(?:[~\s]?\d+(?:\.\d+)?)?|0)"
    # INSTITUTION NAMES in a photo credit. These are proper names of real
    # bodies, kept byte-identical by every edition (checked: all four wave-1
    # editions of Book 3 carry "National Human Genome Research Institute"
    # verbatim, with the phrase WRAPPED ACROSS LINES in fr and pt -- so
    # normalise whitespace before looking for it, or you will conclude it is
    # absent). They belong here rather than in ALLOWED because ATTRIBUTION
    # blanks the PHRASE in context, leaving the surrounding credit prose fully
    # gated, whereas an ALLOWED token would pass anywhere in the book,
    # including inside a genuinely untranslated English sentence.
    #
    # "Human" and "Genome" are in ENGLISH_CONTENT and must stay there: their
    # Indonesian is manusia and genom. It is only this three-word name that is
    # exempt. Reported by the Indonesian Biology Book 3 agent, 2026-09-06,
    # which also proposed the ATTRIBUTION-over-ALLOWED reasoning.
    r"|National\s+Human\s+Genome\s+Research\s+Institute"
    r"|Lawrence\s+Berkeley\s+Laboratory"
    # Data-source credit in Chemistry Book 1 grade 8 (the Mauna Loa CO2
    # record): two institution names, kept verbatim like the ones above.
    # Appended by the Indonesian Chemistry Book 1 agent, 2026-10-04.
    r"|NOAA\s+Global\s+Monitoring\s+Laboratory"
    r"|Scripps\s+Institution\s+of\s+Oceanography"
    # Photo credit in Chemistry Book 2 ch. 26 (the Atacama evaporation ponds,
    # Landsat 8): an institution name, kept verbatim by every edition (fr, es,
    # pt and nl all print "NASA Earth Observatory"). "Earth" is gated English
    # and must stay gated (Indonesian: Bumi); only this phrase is blanked.
    # Appended by the Indonesian Chemistry Book 2 agent, 2026-10-04.
    r"|NASA\s+Earth\s+Observatory"
    # The AUTHOR NAME of a Wikimedia Commons photograph (Chemistry Book 2
    # ch. 27, white phosphorus, and the book-2 image-credits page): the
    # collection "Hi-Res Images of Chemical Elements" is credited as the
    # creator under CC BY 3.0 and must be printed as named (fr and nl keep it
    # verbatim). "of", "Chemical" and "Elements" stay gated everywhere else.
    # Appended by the Indonesian Chemistry Book 2 agent, 2026-10-04.
    r"|Hi-Res\s+Images\s+of\s+Chemical\s+Elements"
    # A PERSON'S NAME WITH ACCENTED LETTERS. LATIN_WORD (the shared reduction)
    # is ASCII-only, so "Léon Péan de Saint-Gilles" (Berthelot's co-worker,
    # Chemistry Book 1 grade 12, equilibrium chapter) tokenises to the
    # fragments "on" and "an", both gated English words, and no rewording can
    # change a name. Only this name is blanked; the surrounding prose stays
    # gated. Appended by the Indonesian Chemistry Book 1 agent, 2026-10-04.
    r"|(?:L[\u00e9e]on\s+)?P[\u00e9e]an\s+de\s+Saint-Gilles"
    # The PHOTOGRAPHER'S WEBSITE in a photo credit (Chemistry Book 4, ch. 6,
    # radio antennas: "ESO/B.~Tafreshi (twanight.org)", and the book-4
    # image-credits page): a domain name, printed as published by every
    # edition (fr, es, pt, nl keep it verbatim); "twanight" fires on the
    # English -ght suffix rule. Only this domain is blanked. Appended by the
    # Indonesian Chemistry Book 4 agent, 2026-10-06.
    r"|twanight\.org"
    # A PERSON'S NAME: "William Lawrence Bragg" (Chemistry Book 4, ch. 9,
    # opening and history box). "Lawrence" follows another capitalised name,
    # so the eponym exemption cannot apply, and the capitalised English-suffix
    # rule fires on "-ence"; a name cannot be reworded. Only the full name is
    # blanked. Appended by the Indonesian Chemistry Book 4 agent, 2026-10-06.
    r"|William\s+Lawrence\s+Bragg"
    # An EPONYM AT THE START OF A TITLE: the theorem "[Persamaan Young]"
    # (Chemistry Book 4, ch. 17, Young's equation of the contact angle). The
    # eponym exemption needs a LOWERCASE native word before the name, but a
    # title is sentence-initial, so its head noun is capitalised and "Young"
    # fires as the English adjective; in running prose ("persamaan Young")
    # the exemption already works. Only this two-word title phrase is blanked.
    # Appended by the Indonesian Chemistry Book 4 agent, 2026-10-06.
    r"|Persamaan\s+Young\b"
    # A PERSON'S NAME: "Benjamin List" (Chemistry Book 4, ch. 28, history
    # box on asymmetric organocatalysis, 2021 Nobel Prize). "List" follows
    # the capitalised first name, so the eponym exemption cannot apply, and it
    # fires as the English word "list"; a name cannot be reworded. Only the
    # full name is blanked. Appended by the Indonesian Chemistry Book 4 agent,
    # 2026-10-06.
    r"|Benjamin\s+List\b")

# The twenty standard THREE-LETTER AMINO-ACID SYMBOLS. These are international
# chemical symbols, identical in every language, and a genetic-code table has
# to print them: "CAU His" is as untranslatable as "Na" or "kg". The gate
# lower-cases before the membership test, so His becomes the English possessive
# "his" and fires; the eponym exemption cannot rescue it either, because the
# word before it in a code table is the codon, which is upper case. Blanked
# here the way NUMBER_ABBREV and ATTRIBUTION are, so the surrounding prose
# stays fully gated. Appended by the Indonesian Biology Book 2 agent,
# 2026-09-05, for parts/grade-11/04-gene-expression.tex.
AMINO_ACID = re.compile(
    r"\b(?:Ala|Arg|Asn|Asp|Cys|Gln|Glu|Gly|His|Ile|Leu|Lys"
    r"|Met|Phe|Pro|Ser|Thr|Trp|Tyr|Val)\b")

# Indonesian writes a decade as "1840-an" (EYD). The suffix tokenises as the
# bare word "an", which is gated English. Any agent writing a date will hit
# this and the hyphenated form is the correct one, so recognise it rather than
# forcing "dasawarsa 1840". Same shape for "tahun 1990-an", "abad ke-19".
# Appended by the Indonesian Chemistry Book 1 agent, 2026-10-04: the IUPAC
# KETONE ending after a locant, "butan-2-on", "heksan-2-on" (Indonesian drops
# the English final -e), tokenises as the bare word "on", gated English.
# Only the locant-hyphen form, and the ending cited alone as a suffix
# ("akhiran -on" in a nomenclature table), are exempt; a free-standing "on"
# is still caught.
DECADE_SUFFIX = re.compile(r"(?<=\d)-(?:an|nya|ke|on)\b|(?<![\w-])-on\b"
    # Appended by the Indonesian Chemistry Book 1 agent, 2026-10-04: the
    # redox-couple notation "Oks/Red", "Red$_1$", "\text{Red}" (Red =
    # reduktor, as Indonesian textbooks write it) is capitalised "Red", which
    # lower-cases to the gated colour word. Exempt only the notation shapes:
    # after "Oks/", or directly before a math subscript or a comma/bracket.
    r"|(?<=Oks/)Red\b|\bRed(?=\s*(?:\x00|[,)]))")

# The TITLE OF A CITED WORK inside an image credit. A credit line names the
# source work exactly as it is published -- "Illustration from OpenStax
# \\emph{Anatomy and Physiology}, CC~BY~3.0." -- and a title is not
# translatable prose: every other edition (fr, es, pt, nl) keeps it verbatim,
# and the licence itself is already exempted above by ATTRIBUTION. Left
# ungated this is unreachable: the conjunction "and" fires on ENGLISH_WORDS
# and there is no way to reword a bibliographic title. Blanked here the way
# ATTRIBUTION is, so the surrounding credit prose stays fully gated. Appended
# by the Indonesian Biology Book 2 agent, 2026-09-05, for
# parts/grade-12/14-brain-and-movement.tex.
WORK_TITLE = re.compile(r"Anatomy\s+and\s+Physiology"
    # The book that set out the twelve principles of green chemistry (Anastas
    # and Warner, 1998), cited by its published title in Chemistry Book 1,
    # grade 12, synthesis-strategy chapter; every wave-1 edition (fr, es, pt,
    # nl) keeps it verbatim. Appended by the Indonesian Chemistry Book 1
    # agent, 2026-10-04.
    r"|Green\s+Chemistry:\s+Theory\s+and\s+Practice"
    # Gibbs's memoir, cited by its published title in Chemistry Book 3, ch. 2
    # (history box), inside the canon's own \emph{}; every wave-1 Book 3
    # edition (fr, es, pt, nl) keeps it verbatim. Appended by the Indonesian
    # Chemistry Book 3 agent, 2026-10-06.
    r"|On\s+the\s+Equilibrium\s+of\s+Heterogeneous\s+Substances"
    # The periodical a portrait comes from, in a photo credit (Chemistry
    # Book 3, ch. 22, Friedel and Crafts history box), set in \textit{} by the
    # canon; the fr edition keeps it verbatim. "Science" is a gated word.
    # Appended by the Indonesian Chemistry Book 3 agent, 2026-10-06.
    r"|Popular\s+Science\s+Monthly"
    # Rachel Carson's book, cited by its published title in \textit{} in
    # Chemistry Book 4, ch. 32 (history box); the nl and pt Book 4 editions
    # keep it verbatim (fr and es use their own published translated titles).
    # "Spring" fires as a gated English word.
    # Appended by the Indonesian Chemistry Book 4 agent, 2026-10-07.
    r"|Silent\s+Spring")

# A CANONICAL GENE OR PROTEIN SYMBOL whose ALPHABETIC part is an English word.
# LATIN_WORD drops the digits, so "HER2" (the receptor amplified in breast
# cancer, parts/bachelor-3/11-cancer-biology.tex) reduces to "HER" and fires on
# ENGLISH_FUNCTION's "her". The symbol is nomenclature: it is identical in every
# edition and in the ENGLISH canon, which this gate would flag too -- a gate
# that fires on the untranslated source is describing the source. Blanked here
# the way ATTRIBUTION is, so the surrounding prose stays fully gated. Appended
# by the Indonesian Biology Book 5 agent, 2026-09-17.
GENE_SYMBOL = re.compile(r"\bHER2\b"
    # The generic COLOUR-INDICATOR NOTATION "HIn/In$^-$" (Chemistry Book 2,
    # ch. 15, indicator definition): "In" is the indicator anion's symbol,
    # identical in every edition and in the English canon, but it lower-cases
    # to the gated preposition "in", and the eponym exemption cannot help
    # because the token before it is "HIn". Only the couple notation is
    # blanked; a free-standing English "in" is still caught. Appended by the
    # Indonesian Chemistry Book 2 agent, 2026-10-04.
    r"|\bHIn/In\b"
    # The ELEMENT SYMBOL "At" (astatine) closing the halogen list
    # "(F, Cl, Br, I, At)" (Chemistry Book 2, ch. 28, halogen definition).
    # A symbol is international and the list is identical in every edition,
    # but "At" lower-cases to the gated preposition "at". Listing "at" in
    # ALLOWED (as "he" was for helium) would open the gate to one of the
    # commonest English words, so only the symbol in its element-list context
    # -- right after "I, " -- is blanked. Appended by the Indonesian Chemistry
    # Book 2 agent, 2026-10-04.
    r"|(?<=\bI, )At\b"
    # The Ox/Red NOTATION as SUBSCRIPTS inside mathematics (Chemistry Book 3,
    # ch. 10, wave equation of a fast couple): $D_{\text{Red}}$,
    # $c^s_{\text{Red}}$, $i = nFAD_{\text{Red}}(c^b_{\text{Red}} - ...)$.
    # The reduction keeps \text{} contents, so a display reads
    # "\x00 Red Red Red Ox Ox Ox \x00" -- byte-identical to the English canon,
    # which this gate would flag too, and frozen by id_apply's math census.
    # Only a run made solely of Ox/Red tokens between two math markers is
    # blanked; "Red" in prose is still gated (the DECADE_SUFFIX rule above
    # already exempts "Oks/Red" and "Red" before a comma or bracket).
    # Appended by the Indonesian Chemistry Book 3 agent, 2026-10-06.
    r"|(?<=\x00)(?:\s*(?:Red|Ox)\b)+(?=\s*\x00)"
    # The chemfig ANCHOR option of \schemestart[][west] (Chemistry Book 3,
    # ch. 21, hydroboration scheme): visible_text strips the command but keeps
    # its optional arguments, so the line reduces to "[west]" and fires on the
    # gated compass word -- in the English canon too. A layout key, never
    # prose; only a lone bracketed compass anchor is blanked, a free-standing
    # "west" in a sentence or node is still caught. Appended by the Indonesian
    # Chemistry Book 3 agent, 2026-10-06.
    r"|\[(?:north|south|east|west)\]")

# ---------------------------------------------------------------------------
# 2. Untranslated sentences.
# ---------------------------------------------------------------------------
# The commonest Indonesian function words. A visible sentence of any length
# worth reading contains at least one; a long one that contains none was never
# translated. Kept small on purpose -- a long list would excuse real defects.
ID_MARKERS = {
    "yang", "dan", "di", "ke", "dari", "untuk", "dengan", "adalah", "ialah",
    "itu", "ini", "pada", "atau", "tidak", "bukan", "jika", "maka", "kita",
    # "bila" (Book 5, 2026-09-17): the formal-register conditional, at least as
    # common in academic Indonesian as "jika", which was already listed. Its
    # absence produced an "untranslated" hit on correct prose and the Book 5
    # agent reworded around it -- which is a gate bug report, not a workaround.
    "bila",
    "setiap", "sebuah", "suatu", "akan", "sudah", "telah", "juga", "dapat",
    "bisa", "harus", "karena", "sehingga", "yaitu", "yakni", "oleh", "agar",
    "lalu", "kemudian", "hanya", "masih", "sama", "lebih", "kurang",
    "bilangan", "himpunan", "fungsi", "misalkan", "maka", "jadi", "ada",
    "semua", "banyak", "tiap", "bagi", "kali", "hasil", "nilai", "berapa",
    "hitung", "hitunglah", "tentukan", "buktikan", "gambar", "gambarlah",
    "tunjukkan", "carilah", "cari", "jawab", "solusi", "latihan", "soal",
    "bab", "halaman", "contoh", "definisi", "teorema", "bukti", "sifat",
    # Added after Book 1: a paragraph built out of noun phrases can go a long
    # way without any of the words above, and fired ~35 times on correct prose.
    # Every one of these is unambiguously Indonesian, so widening the list
    # cannot let an English sentence through.
    "tetapi", "namun", "sedangkan", "tanpa", "antara", "menjadi", "sesudah",
    "sebelum", "seperti", "sampai", "bahwa", "masing-masing", "saling",
    "sendiri", "mengapa",
    # Added after Book 4, same reason. "per" was proposed and REJECTED: English
    # writes "per" too ("per cent", "per second"), so it would excuse a real
    # English sentence. Every marker in this set must be unambiguously
    # Indonesian, or the class stops meaning anything.
    "daripada", "sebagaimana", "merupakan", "atas", "demi", "itulah",
    # ---- physics -----------------------------------------------------------
    # A physics paragraph can be built almost entirely out of quantity nouns
    # and still be perfectly Indonesian ("Gaya gesek pada benda bermassa ...").
    # Every word here is unambiguously Indonesian -- English spells each of
    # them differently -- so widening the list cannot excuse an English
    # sentence, which is the only rule this set has.
    "gaya", "benda", "massa", "berat", "arus", "medan", "energi", "daya",
    "usaha", "suhu", "kalor", "tekanan", "gelombang", "cahaya", "bunyi",
    "muatan", "kecepatan", "kelajuan", "percepatan", "waktu", "jarak",
    "panjang", "tinggi", "lebar", "besaran", "satuan", "pengukuran",
    "listrik", "rangkaian", "cermin", "sinar", "warna", "panas", "dingin",
    "bergerak", "diam", "jatuh", "matahari", "bumi", "bulan", "udara",
    "zat", "kawat", "pegas", "gesek",
    # ---- biology -----------------------------------------------------------
    # A biology sentence can be built almost entirely out of body-part and
    # organism nouns and still be flawless Indonesian ("Daun menyerap cahaya
    # matahari untuk membuat makanan"). Every word here is unambiguously
    # Indonesian -- English spells each of them differently -- so widening the
    # list cannot excuse an English sentence, which is this set's only rule.
    "tumbuhan", "hewan", "makhluk", "hidup", "tubuh", "darah", "jantung",
    "paru-paru", "daun", "akar", "batang", "bunga", "biji", "buah", "tulang",
    "otot", "otak", "kulit", "gigi", "lidah", "hidung", "telinga", "mata",
    "kaki", "tangan", "kepala", "perut", "usus", "hati", "ginjal", "telur",
    "sarang", "mangsa", "makanan", "makan", "minum", "bernapas", "napas",
    "tumbuh", "berkembang", "biak", "keturunan", "induk", "anak", "betina",
    "jantan", "burung", "ikan", "pohon", "rumput", "tanah", "cahaya",
    "matahari", "lingkungan", "manusia", "kuman", "penyakit", "sehat",
    "berbunga", "berbuah", "hutan", "kolam", "sungai", "laut", "musim",
    # ---- appended by the Physics Book 2 (id) agent, 2026-08-20 ----------
    # Each fired on correct Indonesian prose in the grade-10..12 solutions,
    # where a sentence built out of numerals and quantity nouns carries none
    # of the markers above. Every word here is unambiguously Indonesian --
    # English spells each of them differently -- so the class keeps its only
    # rule: it can still not excuse an English sentence.
    "sekitar", "kira-kira", "saat", "ketika", "seluruh", "setelah",
    "selama", "terhadap", "menurut", "sebesar", "sepanjang", "melalui",
    "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan",
    "sembilan", "sepuluh", "puluh", "ratus", "ribu", "juta", "miliar",
    "semesta", "bintang", "planet-planet", "sebagai", "supaya", "hingga",
    # ---- appended for Physics Book 3 (university), 2026-08-21 -------------
    # A university physics clause is noun-phrase-heavy and can run past eight
    # words on circuit and thermodynamics vocabulary alone ("tingkat pertamanya
    # hambatan Thevenin-nya tegangan keluarannya tak ..."). Same rule as every
    # block above: English spells each of these differently, so the class can
    # still not excuse an English sentence.
    "tegangan", "hambatan", "tingkat", "keluaran", "masukan", "penguat",
    "kumparan", "induktor", "kapasitor-nya", "rangkaiannya", "sumbu",
    "poros", "putaran", "simpangan", "amplitudonya", "getaran", "redaman",
    "tumbukan", "momentumnya", "kekekalan", "kelembaman", "acuan",
    "fluida", "zat-cair", "uap", "wujud", "peleburan", "penguapan",
    "entropinya", "siklus", "mesin", "pendingin", "kerja", "usahanya",
    "muatannya", "kapasitor", "dielektrik", "induksi", "fluksnya",
    "lintasan", "kelengkungan", "jari-jari", "sudut", "torsi-nya",
    "keseimbangan", "kesetimbangan", "tetapan", "besarnya", "arahnya",
    "terhitung", "berbanding", "sebanding", "berbalik", "terhadapnya",
    # ---- appended by the Physics Book 1 (id) agent, 2026-08-20 ----------
    # Same rule as above: every word here is unambiguously Indonesian (English
    # spells each of them differently), so the class can still not excuse an
    # English sentence. Each one fired on correct grade-1..9 prose, where a
    # list-heavy or subordinate-clause sentence runs past eight words without
    # touching any marker already listed.
    "dalam",        # "berada dalam kesetimbangan" (grade 2)
    "kalau",        # conditional, the young-book form of "jika"
    "begitu",       # "begitu jauh sehingga ..."
    "saja",         # "perabaan saja tidak dapat dipercaya"
    "sesuatu",      # "ada sesuatu yang terperangkap di dalamnya"
    "selalu",       # "bayang-bayang selalu berseberangan dengan sumbernya"
    "melainkan",    # "bukan tepi penggarisnya, melainkan angka 0"
    "walaupun",     # concessive
    "meskipun",     # concessive
    # ---- second block from the Physics Book 2 (id) agent, 2026-08-20 -----
    # Same rule again. Each fired on correct grade-10..12 prose: a sentence
    # built from a classifier plus optics/mechanics nouns can run past eight
    # words without touching any marker above. Every word is unambiguously
    # Indonesian, so the class still cannot excuse an English sentence.
    "seorang", "seekor", "sehelai", "sebutir", "sebatang", "selembar",
    "disebut", "dinamakan", "terletak", "berada", "titik", "garis",
    "sudut", "bidang", "lensa", "bayangan", "arah", "bentuk", "ukuran",
    "jumlah", "bagian", "keadaan", "getaran",
    # ---- chemistry (Indonesian Chemistry Book 1 agent, 2026-10-04) --------
    # Same rule as every block above: each word is unambiguously Indonesian
    # (English spells it differently: carbon, oxygen, acid, salt, metal,
    # reaction, ...), so the class still cannot excuse an English sentence.
    # Each fired on correct prose: a chemistry clause is built from substance
    # nouns ("Karbon (arang, batu bara) terbakar menghasilkan karbon
    # dioksida"), and SENTENCE_SPLIT's "\n" cuts list lines short of "dan".
    "karbon", "oksigen", "hidrogen", "dioksida", "monoksida", "asam",
    "basa", "garam", "logam", "unsur", "senyawa", "larutan", "pelarut",
    "pereaksi", "reaksi", "bereaksi", "menghasilkan", "terbakar",
    "pembakaran", "bahan", "batu", "kayu", "bensin", "minyak", "besi",
    "tembaga", "seng", "natrium", "klorida", "ikatan", "elektron",
    "persamaan", "rumus", "endapan", "kelarutan", "konsentrasi",
    # Table rows: a tabular line is a list of noun cells, not a sentence, and
    # can hold no function word at all ("PP, polipropilena & wadah yoghurt,
    # tutup botol, bemper mobil"). Indonesian-only object nouns.
    "botol", "wadah", "tutup", "kantong", "gelas", "tabung", "labu",
    "cawan", "serbuk", "padatan", "cairan", "kristal",
    # Safety-box clauses: a hazard sentence is a run of adjectives ("sangat
    # mudah menyala, uapnya menimbulkan kantuk, berbahaya ...") with no
    # function word; each of these is Indonesian-only.
    "sangat", "mudah", "berbahaya", "beracun", "menyala", "iritasi",
}
MIN_SENTENCE_WORDS = 8
SENTENCE_SPLIT = re.compile(r"[.!?;:\n]+")

# ---------------------------------------------------------------------------
# 3-6. Indonesian-specific spelling damage.
# ---------------------------------------------------------------------------
# "bilangan - bilangan" / "bilangan -bilangan": reduplication must be a single
# token joined by a bare hyphen.
REDUP_SPACE = re.compile(r"\b([a-z]{3,})\s+-\s*\1\b|\b([a-z]{3,})\s*-\s+\2\b",
                         re.IGNORECASE)
# The enclitic written as a word. "nya" never stands alone in Indonesian.
ENCLITIC_SPACE = re.compile(r"(?<=[a-zA-Z])\s+-?nya\b")
# A word glued to a thousands group by a thin space: "bilangan\,000".
SPLIT_NUMBER = re.compile(r"[A-Za-z]{2,}\s*\\,\s*\d{3}\b")


# ---------------------------------------------------------------------------
# 7. Titles left byte-identical to the English twin.
# ---------------------------------------------------------------------------
# Book 3 shipped seven untranslated environment titles -- [Characterization],
# [Properties], [Cofactor expansion], [Vandermonde determinant], [Square Cramer
# systems], [Linearization], [Invertibility mod $n$] -- through a FULLY GREEN
# prose gate. A title is short, Title-Cased and often a single word, so the
# word lists and the sentence-density rule all slide off it.
#
# The decisive check is not a word list at all: compare the title with the
# SAME title in the English twin file. If they are byte-identical and the
# title contains real words, it was never translated. Legitimately identical
# titles -- [Gram--Schmidt], [Bolzano--Weierstrass], [Rolle], [Ring],
# [$\arcsin$, $\arccos$] -- survive, because after math and macros are
# stripped they contain no lowercase word and no English-looking one.
TITLE_ENVS = ("definition", "theorem", "proposition", "lemma", "corollary",
              "example", "remark", "method", "notation", "exercise",
              "problem", "proof", "omfigure", "figure", "table")
TITLE_RE = re.compile(
    r"\\begin\{(?:" + "|".join(TITLE_ENVS) + r")\}"
    r"\[((?:[^\[\]]|\[[^\]]*\])*)\]"
    r"|\\(?:chapter|section|subsection)\*?\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")


def _titles(text: str):
    return [(m.group(1) if m.group(1) is not None else m.group(2))
            for m in TITLE_RE.finditer(text)]


def _looks_english(word: str) -> bool:
    low = word.lower()
    if low in ALLOWED or low in NOT_GATED:
        return False
    if low in ENGLISH_WORDS:
        return True
    if word.islower() and len(word) > 3 and ENGLISH_SUFFIX.search(low):
        return True
    if word[:1].isupper() and len(word) > 4 and ENGLISH_SUFFIX_CAP.search(low):
        return True
    # a lowercase word of real length that is not an Indonesian function word:
    # "Plane isometries" is caught here and by nothing else.
    return word.islower() and len(word) > 2 and low not in ID_MARKERS


# An ACCENT-AWARE word pattern, unlike LATIN_WORD. The shared LATIN_WORD is
# [A-Za-z]-only, so it splits "Caratheodory"-with-an-acute into "Carath" +
# "odory" -- and the second half is a lowercase non-Indonesian word, i.e. a
# false positive on a mathematician's name. Every accented surname in the
# series (Caratheodory, Poincare, Levy, Godel, Muller, ...) breaks the same way.
TITLE_WORD = re.compile(r"[^\W\d_]+", re.UNICODE)


def _title_has_words(title: str) -> bool:
    t = re.sub(r"\$[^$]*\$", " ", title)
    t = re.sub(r"\\[A-Za-z@]+", " ", t)
    return any(_looks_english(w) for w in TITLE_WORD.findall(t))


def check_titles(path: pathlib.Path, body: str, findings: list) -> None:
    twin = pathlib.Path(str(path).replace("/id/", "/"))
    if not twin.is_file():
        return
    en = _titles(strip_comments(twin.read_text(encoding="utf-8")))
    idt = _titles(body)
    if len(en) != len(idt):
        return          # a structural divergence; check_translation.sh owns it
    for e, i in zip(en, idt):
        if e.strip() == i.strip() and _title_has_words(i):
            findings.append(
                (str(path), body.count("\n", 0, body.find(i)) + 1, "title",
                 f"title identical to English (untranslated?): {i.strip()[:60]!r}"))


def check_file(path: pathlib.Path, findings: list) -> None:
    raw = path.read_text(encoding="utf-8")
    rel = str(path)
    body = strip_comments(raw)
    # visible_text also reports the shared `math-space` class into findings.
    seen = visible_text(body, findings, rel)
    _occ: dict = {}

    # --- 1. residual English -------------------------------------------
    for pat in (NUMBER_ABBREV, ATTRIBUTION, DECADE_SUFFIX, AMINO_ACID,
                WORK_TITLE, GENE_SYMBOL):
        for m in pat.finditer(seen):
            seen = seen[:m.start()] + " " * (m.end() - m.start()) + seen[m.end():]
    # An EPONYM is a capitalised proper noun sitting in native prose: "sindrom
    # Down", "hukum Mendel", "siklus Krebs". Its lowercase form is often an
    # ordinary English word (down, bell, green, hunter, ross, bright), so the
    # membership test below fires on a name that is CORRECT and, being a name,
    # cannot be reworded away -- the Indonesian agent had to abandon the
    # standard term "sindrom Down" for "trisomi 21".
    #
    # The exemption is deliberately narrow: a capitalised token is treated as a
    # name ONLY when the word before it is itself lowercase and NOT gated
    # English, i.e. the surrounding prose is already Indonesian. A forgotten
    # English sentence cannot buy the exemption, because its capitalised word is
    # either sentence-initial (no predecessor) or preceded by English ("the
    # Down syndrome" -> "the" fires and the sentence is still caught).
    # ENGLISH_SUFFIX_CAP still applies regardless, so an untranslated
    # Title-Case heading is untouched by this.
    prev_low_native = False
    for m in LATIN_WORD.finditer(seen):
        word = m.group(0)
        # A reduplicated plural (kation-kation, karbokation-karbokation) is the
        # Indonesian plural of its base: judge the base. LATIN_WORD keeps the
        # hyphen, so the whole token missed the base's NOT_GATED entry and the
        # -tion rule fired on correct Indonesian (chemistry Book 2 agent,
        # 2026-10-04). An English "x-x" token does not exist to hide behind this.
        _half = word.split("-")
        if len(_half) == 2 and _half[0] and _half[0].lower() == _half[1].lower():
            word = _half[0]
        low = word.lower()
        eponym = (word[:1].isupper() and prev_low_native)
        prev_low_native = (word.islower()
                           and low not in ENGLISH_WORDS
                           and not ENGLISH_POSSESSIVE.match(low))
        if low in ALLOWED or low in NOT_GATED:
            continue
        stem = low[:-2] if low.endswith("es") else low[:-1] if low.endswith("s") else None
        if ((low in ENGLISH_WORDS and not eponym)
                or ENGLISH_POSSESSIVE.match(low)
                or (stem and stem in ENGLISH_WORDS and stem not in NOT_GATED
                    and not eponym)
                or (word.islower() and len(word) > 3
                    and ENGLISH_SUFFIX.search(low))
                or (word[:1].isupper() and len(word) > 4
                    and ENGLISH_SUFFIX_CAP.search(low))):
            findings.append((rel, _locate(body, word, _occ), "english",
                             f"English in visible text: {word!r}"))
    for m in DOTTED_ABBREV.finditer(seen):
        findings.append((rel, _locate(body, m.group(0), _occ), "english",
                         f"English abbreviation: {m.group(0)!r}"))

    # --- 2. sentences that were never translated ------------------------
    for chunk in SENTENCE_SPLIT.split(seen):
        words = [w.lower() for w in LATIN_WORD.findall(chunk)]
        if len(words) < MIN_SENTENCE_WORDS:
            continue
        if any(w in ID_MARKERS for w in words):
            continue
        snippet = " ".join(words[:10])
        findings.append((rel, _locate(body, words[0], _occ), "untranslated",
                         f"no Indonesian function word in {len(words)} words: "
                         f"{snippet}..."))

    # --- 7. titles left identical to the English twin -------------------
    check_titles(path, body, findings)

    # --- 4-6. spelling damage, measured on the raw body -----------------
    for cls, rx, msg in (
            ("redup-space", REDUP_SPACE,
             "reduplication split by spaces (write bilangan-bilangan)"),
            ("enclitic", ENCLITIC_SPACE,
             "enclitic -nya written as a separate word"),
            ("split-number", SPLIT_NUMBER,
             "\\, between a word and a thousands group (split number?)"),
    ):
        for m in rx.finditer(body):
            findings.append((rel, body.count("\n", 0, m.start()) + 1, cls,
                             f"{msg}: {m.group(0)[:40]!r}"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("dirs", nargs="+", help="directories of .tex files")
    ap.add_argument("--quiet", action="store_true",
                    help="print only the per-class summary")
    ap.add_argument("--max-detail", type=int, default=8,
                    help="detail lines to show per class (default 8)")
    args = ap.parse_args()

    findings: list = []
    files = 0
    for d in args.dirs:
        p = pathlib.Path(d)
        # A PATH THAT IS NOT A DIRECTORY USED TO BE SKIPPED IN SILENCE, so the
        # gate handed a single .tex file printed "OK (0 files)" and exited 0 --
        # a clean pass that had checked nothing. That is how 561 residual-English
        # hits survived per-file checking during the Biology Book 5 run. Accept a
        # file, and refuse a path that is neither. Found by the Arabic Book 5
        # agent, 2026-09-17; fixed in all three script gates at once.
        if p.is_file():
            files += 1
            check_file(p, findings)
            continue
        if not p.is_dir():
            sys.stderr.write("  ERROR: not a file or directory: %s\n" % d)
            return 2
        for f in sorted(p.glob("*.tex")):
            files += 1
            check_file(f, findings)

    if not findings:
        print(f"  indonesian prose gate: OK ({files} files)")
        return 0

    by_class: dict = {}
    for rel, line, cls, msg in findings:
        by_class.setdefault(cls, []).append((rel, line, msg))

    print(f"  indonesian prose gate: {len(findings)} issue(s) in {files} files")
    for cls in sorted(by_class):
        hits = by_class[cls]
        bad_files = len({h[0] for h in hits})
        print(f"    {cls:<14} {len(hits):>5} hit(s) in {bad_files} file(s)")
        if not args.quiet:
            for rel, line, msg in hits[:args.max_detail]:
                print(f"        {rel}:{line}: {msg}")
            if len(hits) > args.max_detail:
                print(f"        ... {len(hits) - args.max_detail} more")
    return 1


# DATASET AND INSTITUTION NAMES in the captions and the image-credits page of
# Earth & space Book 1 (id): "Coastlines: Natural Earth (public domain)" and
# its siblings. A dataset's name is printed as published by every edition (fr,
# es, pt, nl keep "Natural Earth" verbatim); "Earth" is gated English (Indonesian:
# Bumi) and stays gated everywhere else -- only the whole name is blanked, as
# "NASA Earth Observatory" is above. Appended (append-only, by redefinition) by
# the Indonesian Earth & space Book 1 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Natural\s+Earth")

# MORE INSTITUTION, PROGRAMME AND DATASET NAMES from the captions of Earth &
# space Book 1 (id): "foto: U.S. National Park Service, Saguaro National Park,
# domain publik", "Data: Smithsonian Global Volcanism Program", "NOAA National
# Severe Storms Laboratory", ... Proper names of real bodies and data products,
# printed verbatim by every edition; the descriptive words around them
# ("catalogue", "and", "Report") are translated and stay gated. Same mechanism
# and reasoning as the "Natural Earth" entry above. Appended (append-only, by
# redefinition) by the Indonesian Earth & space Book 1 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
    + r"|National\s+Park\s+Service|Saguaro\s+National\s+Park"
    + r"|Global\s+Volcanism\s+Program|Deep\s+Sea\s+Drilling\s+Project"
    + r"|Ocean\s+Drilling\s+Program|Texas\s+A\\?&M\s+University"
    + r"|National\s+Centers\s+for\s+Environmental\s+Information"
    + r"|Global\s+Monitoring\s+Laboratory|Scripps\s+Institution\s+of\s+Oceanography"
    + r"|Sea\s+Ice\s+Index|Nevada\s+Geodetic\s+Laboratory|GPlates\s+Web\s+Service"
    + r"|Energy\s+Information\s+Administration|University\s+of\s+Colorado\s+Boulder"
    + r"|National\s+Snow\s+and\s+Ice\s+Data\s+Center|World\s+Ocean\s+Atlas"
    + r"|Earth\s+Sciences\s+and\s+Image\s+Analysis\s+Laboratory"
    + r"|Johnson\s+Space\s+Center|Goddard\s+Space\s+Flight\s+Center"
    + r"|National\s+Geophysical\s+Data\s+Center|National\s+Severe\s+Storms\s+Laboratory"
    + r"|Okeanos\s+Explorer|Photo\s+Library|Jet\s+Propulsion\s+Laboratory"
    + r"|Surface\s+Temperature\s+Analysis|Natural\s+Resources\s+Conservation\s+Service"
    + r"|Global\s+Ocean\s+Monitoring\s+and\s+Observing"
    + r"|Proceedings\s+of\s+the\s+National\s+Academy\s+of\s+Sciences"
    + r"|Earth\s+Observatory")

# TWO DRAWING-CODE BLIND SPOTS of the shared reduction, found in Earth & space
# Book 1 ch. 6.1 (id), both in lines the translator must copy byte-identically:
#  (1) \pgfplotstableread{figdata/out/x.dat}\macro -- the file path was read
#      as visible text and "out" fired as residual English. The argument is a
#      file name, technical in every language: drop it like \includegraphics.
#  (2) an inline \tikz legend swatch inside node text, "\tikz\fill[...] (0,0)
#      circle (2.2pt); planet batuan" -- the path operation "circle" fired.
#      Blank only the coordinate-circle-radius triple, so the label after the
#      semicolon stays gated.
# Neither can be reworded away. Appended (append-only; mutates the shared
# table only inside this Indonesian gate) by the Indonesian Earth & space
# Book 1 agent, 2026-10-25.
import check_hindi_prose as _chp_e1  # noqa: E402
_chp_e1.TECHNICAL_MACROS.setdefault("pgfplotstableread", 1)
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
    + r"|\(\s*-?[\d.]+\s*,\s*-?[\d.]+\s*\)\s*circle\s*\([^()]*\)")

# The same inline-\tikz swatch blind spot with the other path operation the
# book uses for legend keys: "\tikz\fill[...] (0,0) rectangle (0.25,0.18);
# feldspar" (Earth & space Book 1 ch. 6.3, granite legend). Only the
# coordinate-rectangle-coordinate triple is blanked. Appended (append-only)
# by the Indonesian Earth & space Book 1 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
    + r"|\(\s*-?[\d.]+\s*,\s*-?[\d.]+\s*\)\s*rectangle\s*\(\s*-?[\d.]+\s*,\s*-?[\d.]+\s*\)")

# PLACE NAMES printed in their own language: "Big Spring, Missouri" (Earth &
# space Book 1 ch. 6.5 photo caption). The eponym exemption cannot cover it
# (the gated word follows a capitalised one). Appended (append-only) by the
# Indonesian Earth & space Book 1 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Big\s+Spring")

# WORK TITLES printed in their original language: the USGS booklet
# "\emph{This Dynamic Earth}" credited under a map (Earth & space Book 1
# ch. 7.1). A title is a name; the credit words around it are translated and
# stay gated. Appended (append-only) by the Indonesian Earth & space Book 1
# agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|This\s+Dynamic\s+Earth")

# One more INSTITUTION name printed in English: "Smithsonian Institution"
# (Earth & space Book 1 ch. 7.2, the keeper of the volcano list). Same
# reasoning as the institution list above. Appended (append-only) by the
# Indonesian Earth & space Book 1 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Smithsonian\s+Institution")

# One more PLACE NAME printed in its own language: "Borah Peak" (Idaho; the
# 1983 earthquake, Earth & space Book 1 ch. 7.3 photo caption). Same reasoning
# as "Big Spring" above. Appended (append-only) by the Indonesian Earth & space
# Book 1 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Borah\s+Peak")

# One more PLACE NAME printed in its own language: "Hermits Rest" (the Grand
# Canyon viewpoint, Earth & space Book 1 ch. 7.4 photo caption). Same
# reasoning as "Big Spring" above. Appended (append-only) by the Indonesian
# Earth & space Book 1 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Hermits\s+Rest")

# DRAWING-CODE BLIND SPOT: a \tikzset{... /.pic={...}} block placed in an
# omfigure but OUTSIDE any tikzpicture is read as visible text, so the path
# operation "ellipse (0.13 and 0.085)" fires "and" (Earth & space Book 1
# ch. 7.5, trilobite pic). Blank only the ellipse-radii group. And one more
# PLACE NAME, "Siccar Point" (same chapter), as "Big Spring" above. Appended
# (append-only) by the Indonesian Earth & space Book 1 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
                         + r"|ellipse\s*\(\s*-?[\d.]+\s+and\s+-?[\d.]+\s*\)"
                         + r"|Siccar\s+Point")

# "front" is the Indonesian METEOROLOGICAL TERM for the boundary between two
# air masses (KBBI; "front dingin", "front hangat", "front oklusi" are the
# standard words of the national weather service) -- spelled exactly as the
# English word, like "air" and "not" above. Earth & space Book 1 ch. 8.3 (id)
# uses it some sixty times on correct prose. Losing English "front" costs
# little: a forgotten English sentence containing it carries "the"/"of"/"is"
# too. Its English plural "fronts" is gated explicitly (the -s stem rule
# would otherwise pass it, its stem now being NOT_GATED). Appended
# (append-only) by the Indonesian Earth & space Book 1 agent, 2026-10-25.
NOT_GATED.add("front")
ENGLISH_CONTENT.add("fronts")
ENGLISH_WORDS.add("fronts")

# One more WORK TITLE printed in its original language: the newspaper
# "\emph{The Times}" (FitzRoy's first public forecast, Earth & space Book 1
# ch. 8.3). Same reasoning as "This Dynamic Earth" above. Appended
# (append-only) by the Indonesian Earth & space Book 1 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|The\s+Times")

# One more WORK TITLE printed in its original language: W. A. Herdman's book
# "\emph{Founders of Oceanography}" (1923), the source of the Challenger
# engraving (Earth & space Book 1 ch. 8.4). Same reasoning as "This Dynamic
# Earth" above. Appended (append-only) by the Indonesian Earth & space Book 1
# agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Founders\s+of\s+Oceanography")

# One more INSTITUTION name printed in English: "NOAA Laboratory for
# Satellite Altimetry" (the sea-level record, Earth & space Book 1 ch. 9.1).
# Same reasoning as the institution list above. Appended (append-only) by the
# Indonesian Earth & space Book 1 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
                         + r"|Laboratory\s+for\s+Satellite\s+Altimetry")

# One more WORK TITLE (a publication series): "USGS Circular 1073", the
# source of the Nevado del Ruiz hazard map (Earth & space Book 1 ch. 9.2).
# Same reasoning as "This Dynamic Earth" above. Appended (append-only) by the
# Indonesian Earth & space Book 1 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|USGS\s+Circular")

# Two more INSTITUTION names printed in English in the Chuquicamata credit:
# "Japan Space Systems" and the "U.S./Japan ASTER Science Team" (Earth &
# space Book 1 ch. 9.3). Same reasoning as the institution list above.
# Appended (append-only) by the Indonesian Earth & space Book 1 agent,
# 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
                         + r"|Japan\s+Space\s+Systems|ASTER\s+Science\s+Team")

# Three more PLACE NAMES printed in their own language (Earth & space Book 1
# ch. 9.4): "Birling Gap" (East Sussex), "White Sands" (New Mexico) and
# "Lagoa dos Barros" (Brazil). Same reasoning as "Big Spring" above.
# Appended (append-only) by the Indonesian Earth & space Book 1 agent,
# 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
                         + r"|Birling\s+Gap|White\s+Sands|Lagoa\s+dos\s+Barros")

# Two more INSTITUTION / SERVICE names printed in English in the Lena delta
# credit: "USGS EROS Data Center" and "NASA Visible Earth" (Earth & space
# Book 1 ch. 9.5). Same reasoning as the institution list above. Appended
# (append-only) by the Indonesian Earth & space Book 1 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
                         + r"|EROS\s+Data\s+Center|Visible\s+Earth")

# A MISSION NAME printed as named: the Mars rover "Curiosity" (Earth & space
# Book 2 ch. 10.2, the Mount Sharp photograph). Case-sensitive, so the
# English noun "curiosity" stays gated (-ity). Appended (append-only) by the
# Indonesian Earth & space Book 2 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|\bCuriosity\b")

# A PERSON'S NAME inside a quantity name: the "Bond albedo" (after the
# astronomer G. P. Bond) is "albedo Bond" in Indonesian, and "Bond" fires
# the English word "bond" (ikatan) after .lower() (Earth & space Book 2
# ch. 10.2-10.3). Only the two-word phrase is blanked; "bond" stays gated.
# Appended (append-only) by the Indonesian Earth & space Book 2 agent,
# 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|[Aa]lbedo\s+Bond\b")

# WORK TITLES and a SHIP NAME printed as published (Earth & space Book 2
# ch. 11.1, the history of seafloor spreading): Hess's paper "\emph{History of
# Ocean Basins}" (1962), Vine and Matthews's "\emph{Magnetic anomalies over
# oceanic ridges}" (Nature, 1963) and the drilling ship "\emph{JOIDES
# Resolution}". Titles and names are not translatable prose; the words around
# them are translated and stay gated. Same reasoning as "This Dynamic Earth"
# above. Appended (append-only) by the Indonesian Earth & space Book 2 agent,
# 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
                         + r"|History\s+of\s+Ocean\s+Basins"
                         + r"|Magnetic\s+anomalies\s+over\s+oceanic\s+ridges"
                         + r"|JOIDES\s+Resolution")

# TOOL FIX for the Book 1 institution entry above: its pattern
# "Texas\s+A\\?&M\s+University" can never match, because visible_text()
# drops the escaped ampersand and the gate sees "Texas AM University". The
# name is printed by the canon in the JOIDES Resolution photo credit (Earth &
# space Book 2 ch. 11.1). This alternative accepts the reduced form; the
# words around it stay gated. Appended (append-only) by the Indonesian Earth &
# space Book 2 agent, 2026-10-25.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Texas\s+A&?M\s+University")

# Earth & space Book 3 id agent, 2026-10-27: the photograph credit of the
# Europa figure (ch. 3, "NASA/JPL/University of Arizona and NASA/JPL/DLR, public
# domain"). Institution and mission names, printed as named in the canon credit.
# Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|University\s+of\s+Arizona\s+(?:and|dan)\s+NASA/JPL/DLR")

# Earth & space Book 3 id agent, 2026-10-27: the title of William Smith's 1815
# map (ch. 4 history box), printed as named: a published work's title, not prose.
# Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|A\s+Delineation\s+of\s+the\s+Strata\s+of\s+England\s+and\s+Wales(?:,\s+with\s+part\s+of\s+Scotland)?")

# Earth & space Book 3 id agent, 2026-10-27: Hutton's Theory of the Earth and the
# learned society that heard it, printed as named (ch. 5 history box): a work's
# title and an institution's name. Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Theory\s+of\s+the\s+Earth|Royal\s+Society\s+of\s+Edinburgh")

# A PLACE NAME and a WORK TITLE printed as named (Earth & space Book 2
# ch. 11.8, igneous rocks): the "Giant's Causeway" (Northern Ireland), which
# has no established Indonesian name, and Bowen's book "\emph{The Evolution
# of the Igneous Rocks}" (1928). Same reasoning as "Birling Gap" and "History
# of Ocean Basins" above; the words around them stay gated. Appended
# (append-only) by the Indonesian Earth & space Book 2 agent, 2026-10-26.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
                         + r"|Giant's\s+Causeway"
                         + r"|The\s+Evolution\s+of\s+the\s+Igneous\s+Rocks")

# Two PERSONS' SURNAMES that are English words, printed in citations (Earth &
# space Book 2 ch. 12.1): the geophysicist R. S. White ("White, McKenzie dan
# O'Nions (1992)") and the photographer Chris Light. Only the name in its
# citation context is blanked; "white" and "light" stay gated everywhere else.
# Appended (append-only) by the Indonesian Earth & space Book 2 agent,
# 2026-10-26.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
                         + r"|\bWhite,\s+McKenzie\b|\bChris\s+Light\b")

# A PLACE NAME printed as named (Earth & space Book 2 ch. 12.6, internal
# heat): the geothermal field "The Geysers" in California, whose English
# article is part of the proper name. Only the two-word name is blanked; "the"
# stays gated everywhere else. Appended (append-only) by the Indonesian Earth &
# space Book 2 agent, 2026-10-26.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|\bThe\s+Geysers\b")

# Two PROPER NAMES printed as named (Earth & space Book 2 ch. 12.7, the age
# of the Earth): the photographic studio "Russell and Sons" credited for the
# 1906 portrait of Kelvin, and the "Forest City" meteorite of Patterson's lead
# isochron. Only the names are blanked; "and" and "forest" stay gated
# everywhere else. Appended (append-only) by the Indonesian Earth & space
# Book 2 agent, 2026-10-26.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
                         + r"|\bRussell\s+and\s+Sons\b|\bForest\s+City\b")

# A PHOTOGRAPHER'S NAME printed as credited (Earth & space Book 2 ch. 12.8,
# the early Earth): the Wikimedia Commons author "Wendy from Pennsylvania" of
# the Sedona red-beds photograph. Only the credited name is blanked; "from"
# stays gated everywhere else. Appended (append-only) by the Indonesian Earth &
# space Book 2 agent, 2026-10-26.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
                         + r"|\bWendy\s+from\s+Pennsylvania\b")

# AN INSTITUTION'S NAME printed as credited (Earth & space Book 2 ch. 12.9,
# past climates): the "Dartmouth Electron Microscope Facility", author of the
# public-domain pollen micrograph. Only the credited name is blanked; its words
# stay gated everywhere else. Appended (append-only) by the Indonesian Earth &
# space Book 2 agent, 2026-10-26.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern
                         + r"|\bDartmouth\s+Electron\s+Microscope\s+Facility\b")

# Earth & space Book 3 id agent, 2026-10-27: a float placement option such as
# \begin{table}[htbp] is captured by TITLE_RE (table is in TITLE_ENVS) and is
# identical to the English twin by design, so it is not a title. Appended
# (append-only): the word test is narrowed for placement strings only.
_title_has_words_base = _title_has_words
def _title_has_words(t):
    return _title_has_words_base(t) and t.strip() not in {
        "htbp", "htb", "hbp", "tbp", "htp", "ht", "hb", "tb", "h", "t", "b", "p", "!htbp"}

# Earth & space Book 3 id agent, 2026-10-27 (ch. 9-10): the province name "Basin and
# Range" (western United States), printed as named by the canon and by the
# French edition; no Indonesian exonym exists. Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Basin\s+and\s+Range")

# Earth & space Book 3 id agent, 2026-10-27 (ch. 12): the magnetic chron names of the
# polarity timescale (C1n, C2An, C5n, C2n ...) are names, not prose: "An" in
# "C2An" fires as the English article. Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|\bC\d+A?[nr]\b")

# Earth & space Book 3 id agent, 2026-10-27 (ch. 13): the photograph credit of the Galapagos
# Rift lava figure ("NOAA Okeanos Explorer Program, Galapagos Rift Expedition 2011"), printed
# as named in the canon credit. Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Rift\s+Expedition\s+2011")

# Earth & space Book 3 id agent, 2026-10-27 (ch. 14): two credit names printed as named in the
# canon: the dataset "Scripps Institution of Oceanography marine gravity model" (Kuril gravity
# figure) and the photograph subject "Sarychev Peak" (volcano, Kuril arc). Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Scripps\s+Institution\s+of\s+Oceanography\s+marine\s+gravity\s+model|Sarychev\s+Peak")

# Earth & space Book 3 id agent, 2026-10-27 (ch. 15): the photograph and table name "Columbia River"
# (Columbia River basalts, province name in the hotspot table), printed as named by the canon.
# Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Columbia\s+River")

# Earth & space Book 3 id agent, 2026-10-27 (ch. 15): the acronym LIP (large igneous province), defined
# in the text by its Indonesian term and used as the standard acronym in every figure key. Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|\bLIP\b")

# Earth & space Book 3 id agent, 2026-10-27 (ch. 17): proper names of the photographs and of a
# book title, printed as named in the canon: Corona Heights, Red Rock Canyon, Keystone Thrust, and
# "The Dynamics of Faulting and Dyke Formation" (Anderson 1905). Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Corona\s+Heights|Red\s+Rock\s+Canyon|Keystone\s+Thrust|Dynamics\s+of\s+Faulting\s+and\s+Dyke\s+Formation")

# Earth & space Book 3 id agent, 2026-10-27 (ch. 17): the district name "North Cornwall" in a photograph
# credit caption (Millook), printed as named in the canon. Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|North\s+Cornwall")

# Earth & space Book 3 id agent, 2026-10-27 (ch. 28): the photograph credit "NASA, MODIS/LANCE"
# (Gulf of Alaska cyclone, MODIS instrument, LANCE near-real-time data service), printed as named in
# the canon credit and kept byte-identical in the credits list. Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|\bMODIS\s*/\s*LANCE\b")

# Earth & space Book 3 id agent, 2026-10-27 (ch. 28): the title of Ferrel's 1856 essay, printed as the
# English title (a title is never translated; the Indonesian gloss follows in parentheses). Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|An\s+essay\s+on\s+the\s+winds\s+and\s+currents\s+of\s+the\s+ocean")

# Earth & space Book 4 id agent, 2026-10-30 (ch. 8, magmatic differentiation): the PLAGIOCLASE
# END-MEMBER NOTATION "An$_{70}$", "An$_{83.3}$" (mol per cent anorthite, as "Fo$_{80}$" for olivine),
# printed byte-identically to the English canon; the symbol lower-cases to the gated article "an".
# Only "An" written directly against a math marker (its subscript) is blanked; the word "an" in
# prose stays gated. Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|\bAn(?=\x00)")

# Earth & space Book 4 id agent, 2026-10-30 (ch. 10, metamorphic facies, proof of the
# aluminosilicate triple point): the standard MINERAL ABBREVIATIONS ky/and/sil as \text{}
# subscripts inside mathematics, $\Delta G_{\text{ky}\to\text{and}}$, $G_{\text{and}}$. The
# reduction keeps \text{} contents, so the display reads "\x00 ky sil ky and and sil \x00",
# byte-identical to the English canon and frozen by id_apply's math census; "and" fires as English.
# As for the Ox/Red rule above, only a run made solely of ky/and/sil tokens between two math
# markers is blanked; "and" in prose stays gated. Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|(?<=\x00)(?:\s*(?:ky|and|sil)\b)+(?=\s*\x00)")

# Earth & space Book 4 id agent, 2026-10-30 (ch. 11, thermobarometry): MINERAL
# AND SITE SUBSCRIPTS as \text{} inside math -- $X_{\text{an}}$ (anorthite
# fraction), $X_{\text{Mg,grt}}$, $a_{\text{pirop}}$ ... The reduction keeps
# \text{} contents, so a display reads "\x00 pirop anit ... Mg grt Fe bt \x00"
# ("an" is gated English; the run has no function word). Only a run made
# wholly of these tokens between two math markers is blanked, as for ky/and/sil
# (or ended by a translated "\text{ dalam ...}" gloss in the same display).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|(?<=\x00)(?:[\s,]*(?:an|pirop|anit|almandin|flogopit|grosular|anortit|garnet|biotit|Mg|Fe|Ca|grt|bt)\b)+(?=\s*\x00|\s+dalam\b)")

# Earth & space Book 4 id agent, 2026-10-30 (bachelor-2 ch. 12, migmatite
# photograph credit "Foto: Kevin M. Gill, CC BY 4.0"): the photographer's
# surname lower-cases to the gated "gill" and follows an initial, so the eponym
# rule cannot see it. The whole name is blanked, as for Natural Earth.
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Kevin\s+M\.\s+Gill\b")

# Earth & space Book 4 id agent, 2026-10-30 (bachelor-2 ch. 20, Lyell's book
# cited by its published title, \emph{Principles of Geology}, in the canon's
# own \emph{}; fr/es/pt/nl keep it verbatim). "of" fires as English; only the
# title phrase is blanked. Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Principles\s+of\s+Geology")

# Earth & space Book 4 id agent, 2026-10-30 (bachelor-2 solutions/29, problem
# answer 12): the canon's math "Tonnage $\times\, 370.7/799.6$" puts a thin
# space after the CONTROL WORD \times, frozen byte-identical by id_apply's math
# census; split-number read "times\, 370" as a word split from a thousands
# group. Only a letter run preceded by a backslash (a TeX control word) is
# exempted; "ribu\, 370" in prose still fires. Appended (append-only).
SPLIT_NUMBER = re.compile(r"(?<![\\A-Za-z])[A-Za-z]{2,}\s*\\,\s*\d{3}\b")

# Earth & space Book 4 id agent, 2026-10-30 (bachelor-2 ch. 30, energy
# geology): the Green River oil shale / kerogen of Utah, a formation's proper
# name kept in Latin by every edition (fr/es/pt/nl print "Green River"). "River"
# follows the capitalised "Green", so the eponym rule cannot see it, and it is
# gated English. Only the two-word name is blanked. Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Green\s+River\b")

# Earth & space Book 5 id coordinator, 2026-11-03 (bachelor-3 ch. 3, 4, 15, 20, 22, 24, 25, 28, 31): names printed in English in the canon
# and kept by every edition: reference systems, institutions, a journal, a dataset, a mission, a telescope and two named
# springs. Only the whole phrases are blanked; the bare words still fire. Appended (append-only).
ATTRIBUTION = re.compile(ATTRIBUTION.pattern + r"|Geodetic\s+Reference\s+System|International\s+Association\s+of\s+Geomagnetism\s+and\s+Aeronomy"
                         r"|Palette\s+Spring|Mammoth\s+Hot\s+Springs|NASA\s+Center\s+for\s+Climate\s+Simulation|ETOPO1\s+Ice\s+Surface"
                         r"|Operation\s+IceBridge|James\s+Webb\s+Space\s+Telescope|Journal\s+of\s+Marine\s+Research"
                         r"|California\s+Institute\s+of\s+Technology|National\s+Aeronautics\s+and\s+Space\s+Administration|Exoplanet\s+Exploration\s+Program|Li,\s+Be,\s+B\b")

if __name__ == "__main__":
    sys.exit(main())
