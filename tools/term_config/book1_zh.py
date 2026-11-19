"""Book 1 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md); refined at the book's close against the
link census (pilot_translation/census.py). Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han
text, so a word that is also part of a common compound must be stopped or dropped here. One-character terms never link.
"""

# result names are never terms
NOT_A_TERM = ("定理", "引理", "公式", "判据", "准则", "原理", "法则", "定律", "问题")

STOP = set()
DROP = set()
EXTRA = {          # manual {term: label}, added at the book's close (index-only keys have no space in Chinese)
    # 沙, 泥, 云 and 雾 are one character and never link; English links sand/mud 282 times, cloud 93 (close, 2026-11-19)
    **{t: "def:g3:stones-pebbles-sand:sand" for t in ("沙子", "沙粒", "泥沙", "淤泥")},
    **{t: "def:g4:clouds-rain-snow:cloud" for t in ("云层", "云团")},
}
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
