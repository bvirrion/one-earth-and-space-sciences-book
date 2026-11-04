"""Book 4 (University, Year 2) -- id. Curation only; the rules live in tools/termlink/.

Curated 2026-10-30 by the Book 4 `id` agent from this edition's own harvest
(the first link pass with the empty stub: 2,246 links / 197 targets against
English's 2,019 / 191), with the frequency and chapter-set censuses against the
English twin (draft/b4-run/tools/census.py). Every flagged site was read and
judged by its target. No entry is copied from book4_en.py, book4_fr.py or
book3_id.py.

What the census flagged and why it stays:
- basal pulau samudra (ch09, 15 links vs English 4): English writes the
  abbreviation OIB there, Indonesian writes the term out; every site is the
  ocean-island basalt of def:b2:elements-in-the-earth:morb-oib;
- meteorit / meteorit jatuhan / meteorit temuan (ch02, 50 vs 21) and himpunan
  mineral (ch10-11, 15 vs 2): one sense each, all the defined one;
- pulau samudra (ch26), proksi iklim (ch26 recall), diagram ternormalisasi
  (ch09 recall), unsur jejak (ch04, ch18), fraksi lelehan (ch08), metamorfisme
  (ch14, ch29), orogen tumbukan (ch29): right target, chapters English happens
  not to link;
- six targets English never reaches, one link each, all right: rayapan tsunami
  (ch28 opening), asimilasi kerak (ch12), lewat jenuh silika (ch09), tafonomi
  (ch20 caption), seri metamorfik (ch11), unsur tanah jarang (ch09).
"""

# STOP: ordinary or other-sense words. A STOPped term still links inside the
# chapter that pins its one sense (the per-chapter map), and nowhere else:
# - deteksi: the detection of climate change (ch27, its defining chapter) keeps
#   its links; the detection of a hazard in an early-warning system (ch28) and
#   the detection limit of an analysis (ch31, "batas deteksi", four sites) are
#   other senses.
STOP = {"deteksi", "Deteksi", "deteksinya"}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

EXTRA_PROTECT = [
    # rasio campuran: the water-vapour mixing ratio of ch21. The mixture ratio
    # R_m of an isotope dilution (ch31, exercise 10) is another quantity.
    r'(?<!\w)rasio\s+campuran(?=\s+yang\s+meminimumkan)',
    # rasio campuran: the CO2 mole fraction of the air (ch26, exercise 11),
    # not the water-vapour mixing ratio (English protects the same site).
    r'(?<!\w)berapa\s+rasio\s+campurannya',
]
