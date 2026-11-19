"""Book 3 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md); refined at the book's close against the
link census (pilot_translation/census.py). Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han
text, so a word that is also part of a common compound must be stopped or dropped here. One-character terms never link.
"""

# result names are never terms
NOT_A_TERM = ("定理", "引理", "公式", "判据", "准则", "原理", "法则", "定律", "问题")

# the English STOP list (stable, stability, extension, flux…): kept in their own chapter only
STOP = {"稳定", "稳定性", "伸展", "流量", "通量", "地形起伏", "系列", "体系"}
# ordinary words that are not the defined sense anywhere: 环流 is any circulation (not only a gyre), 对比 is "compare"
# (not a log correlation); vergence is 倒向, so 转向 ("turn") is not a term
DROP = {"环流", "对比"}
EXTRA = {"古登堡–里克特定律": "prop:b1:earthquake-source:gutenberg-richter", "参考地球模型": "def:b1:layered-earth:reference-model"}          # manual {term: label}, added at the book's close (index-only keys have no space in Chinese)
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
