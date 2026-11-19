"""Book 5 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md); refined at the book's close against the
link census (pilot_translation/census.py). Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han
text, so a word that is also part of a common compound must be stopped or dropped here. One-character terms never link.
"""

# result names are never terms
NOT_A_TERM = ("定理", "引理", "公式", "判据", "准则", "原理", "法则", "定律", "问题")

STOP = {"视线", "稳态", "涡旋", "模式年龄"}   # mirrors book5_en.py: each kept to its own chapter
DROP = set()
EXTRA = {          # targets the harvest cannot reach from the Chinese displays (linkdiff at the close, 2026-11-19)
    "斜压": "def:b3:gfd-foundations:baroclinic",
    "正压流体": "def:b3:gfd-foundations:baroclinic",
    "位势": "def:b3:gravity-geodesy:geopotential",
    "海岸线轨迹": "def:b3:sequence-stratigraphy:trajectory",
    "岸线轨迹": "def:b3:sequence-stratigraphy:trajectory",
    "达西定律": "thm:b3:hydrogeology:darcy",
    "基底拖曳力": "def:b3:mantle-convection:basal-drag",
    "底部拖曳力": "def:b3:mantle-convection:basal-drag",
    "闭箱模型": "thm:b3:origin-of-elements:closed-box",
    "栅格数据": "def:b3:remote-sensing-gis:data-models",
    "矢量数据": "def:b3:remote-sensing-gis:data-models",
    "栅格图层": "def:b3:remote-sensing-gis:data-models",
    "矢量图层": "def:b3:remote-sensing-gis:data-models",
}
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
