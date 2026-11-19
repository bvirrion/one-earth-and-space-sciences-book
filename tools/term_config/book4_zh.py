"""Book 4 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md); refined at the book's close against the
link census (pilot_translation/census.py). Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han
text, so a word that is also part of a common compound must be stopped or dropped here. One-character terms never link.
"""

# result names are never terms
NOT_A_TERM = ("定理", "引理", "公式", "判据", "准则", "原理", "法则", "定律", "问题")

STOP = set()
# 检测 is any "test" or "detection", not detection-and-attribution
DROP = {"检测"}
EXTRA = {"潜在强度": "prop:b2:weather-systems:pi", "同位素稀释": "prop:b2:field-lab-methods-2:id",
         "柯勒曲线": "prop:b2:atmospheric-thermodynamics:kohler", "单变": "def:b2:metamorphic-facies:univariant"}          # manual {term: label}, added at the book's close (index-only keys have no space in Chinese)
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
