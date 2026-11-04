"""Book 5 (University, Year 3) -- fr. Curation only; the rules live in tools/termlink/.

Curated 2026-11-03 by the edition's coordinator from this edition's own harvest, with the frequency census
against the English twin (translation_instruction.md). Each entry is a French homograph, judged against its target.
"""

# STOP: ordinary words outside their defining chapter (the term still links in it), each against its target:
# - pôle(s): the pole of a plane on a stereonet (ch08); elsewhere the geographic and magnetic poles, and the end-members
#   of a solid solution (ch11, 12, 13);
# - palier(s), rampe(s): the flat and the ramp of a thrust (ch10); elsewhere the heating steps of an age spectrum
#   (ch13), a plateau of a curve, a CO2 ramp in a climate model (ch22), a carbonate ramp (ch17);
# - état(s) stationnaire(s): the steady profile of a river (ch18); elsewhere any steady state (ch22, 23, 27, 30);
# - ligne de visée: the radar line of sight (ch25); elsewhere the astronomer's line of sight (ch28, 29);
# - âge(s) modèle(s): a Nd or Hf model age (ch13); ch26's crater model age is not that definition;
# - superposition: the GIS overlay (ch25); elsewhere the principle of superposition, and any superposition.
STOP = {"pôle", "Pôle", "pôles", "Pôles",
        "palier", "Palier", "paliers", "Paliers",
        "rampe", "Rampe", "rampes", "Rampes",
        "état stationnaire", "État stationnaire", "états stationnaires", "États stationnaires",
        "ligne de visée", "Ligne de visée", "lignes de visée",
        "âge modèle", "Âge modèle", "âges modèles", "Âges modèles",
        "superposition", "Superposition", "superpositions"}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"
EXTRA_PROTECT = []
