"""Book 2 (High School, grades 10-12) -- ar. Curation only; the rules live in tools/termlink/.

Curated by the Book 2 `ar` agent (2026-10-26) from this edition's own harvest,
with the frequency and chapter-set censuses against the English twin
(translation_instruction.md), never by translating book2_en.py.

lang_ar.py has no WORD_TAIL: the article and the one-letter prepositions are
a HEAD (ال، وال، بال، لل ...), so an indefinite term also links its definite
forms, but nothing reaches a broken plural, a dual, a sound plural or an
accusative with tanween, and nothing derives an indefinite form from a term
harvested only in the definite (a construct such as "نقطة الندى"). Those are
declared below, term by term, each one a form this edition really uses.
"""

# STOP (ordinary word outside its defining chapter, where it still links),
# each checked against its target:
# - العين: the cyclone's eye (g10.05); elsewhere "بالعين المجردة", the naked
#   eye (g11.08, g12.03) -- English STOPs "eye" for the same reason;
# - تشبع، مشبعًا: saturation of air (g10.04); elsewhere a rock or soil
#   "saturated with water" (g11.09, g12.04) -- English STOPs saturated;
# - مستقرًا، غير مستقر: stable air (g10.04); elsewhere a stable mineral or a
#   stable ocean (g10.06, g11.08, g12.03) -- English STOPs stable/unstable;
#   "هواء مستقر" and "هواء غير مستقر" are separate keys and still link;
# - تفلطح، تفلطحه: flattening of the ellipsoid (g10.01) -- English STOP;
# - متوسط، متوسطة: an intermediate rock (g11.08); everywhere else the ordinary
#   adjective "average/medium" (average speed, medium confidence, the average
#   continent, an intermediate scenario) -- 20 wrong links before the STOP;
# - رتبة: the rank of a coal (g11.09); elsewhere "من رتبة" (of the order of,
#   g12.01 solutions); "رتبة الفحم" is declared in EXTRA.
STOP = {"العين", "تشبع", "مشبعًا", "مستقرًا", "غير مستقر", "تفلطح", "تفلطحه",
        "متوسط", "متوسطة", "رتبة"}
NO_CAPITAL = set()

_CC = "def:g12:climate-change:"
EXTRA = {
    # g12 climate-change: the chapter uses the short forms of its terms, as
    # English does (book2_en.py EXTRA forcing/feedback/scenario); the senses of
    # "تأثير" that are not a forcing (human influence) are masked below
    "تأثير": _CC + "forcing", "تأثيرات": _CC + "forcing",
    "تأثيرًا": _CC + "forcing",
    "تغذية راجعة": _CC + "feedback", "تغذيات راجعة": _CC + "feedback",
    "تغذيتان راجعتان": _CC + "feedback", "تغذيتين راجعتين": _CC + "feedback",
    "سيناريو": _CC + "scenario", "سيناريوهات": _CC + "scenario",
    # constructs harvested only in the definite: their indefinite forms
    "نقطة ندى": "def:g10:why-clouds-form:dew-point",
    "زمن انتقال": "def:g11:seismic-structure:travel-time",
    "أزمنة انتقال": "def:g11:seismic-structure:travel-time",
    "أزمنة الانتقال": "def:g11:seismic-structure:travel-time",
    "زمني انتقال": "def:g11:seismic-structure:travel-time",
    "فترة عودة": "def:g10:drainage-basins:return-period",
    "فترات عودة": "def:g10:drainage-basins:return-period",
    "فترتا العودة": "def:g10:drainage-basins:return-period",
    "انفصام": "def:g11:minerals:cleavage",
    "انفصامات": "def:g11:minerals:cleavage",
    "انفصامًا": "def:g11:minerals:cleavage",
    "انفصامان": "def:g11:minerals:cleavage",
    "انفصامين": "def:g11:minerals:cleavage",
    "انفصاما": "def:g11:minerals:cleavage",
    "مكسر": "def:g11:minerals:cleavage",
    "مكسرًا": "def:g11:minerals:cleavage",
    "رتبة الفحم": "def:g11:fossil-fuel-geology:coal",
    "رتب الفحم": "def:g11:fossil-fuel-geology:coal",
    # broken and sound plurals, duals and accusatives
    "معادن طينية": "def:g10:soil-formation:clay",
    "أحواض رسوبية": "def:g11:fossil-fuel-geology:basin",
    "حركات نسبية": "def:g11:plate-motions:relative-motion",
    "عتبات": "def:g11:igneous-rocks:intrusion",
    "قواطع": "def:g11:igneous-rocks:intrusion",
    "قواطعَ": "def:g11:igneous-rocks:intrusion",
    "بلوتونات": "def:g11:igneous-rocks:intrusion",
    "بلوتونًا": "def:g11:igneous-rocks:intrusion",
    "أجسام متداخلة": "def:g11:igneous-rocks:intrusion",
    "متعدد أشكال": "def:g12:metamorphic-rocks:polymorph",
    "متعددات الأشكال": "def:g12:metamorphic-rocks:polymorph",
    "متعددات أشكال": "def:g12:metamorphic-rocks:polymorph",
    "متعددا أشكال": "def:g12:metamorphic-rocks:polymorph",
    "تكوينات الحديد الشريطية": "def:g12:early-earth:bif",
    "ستروماتوليتات": "def:g12:early-earth:stromatolite",
    "أوفيوليتات": "def:g12:mountain-building:ophiolite",
    "موجات P": "def:g11:seismic-structure:body-waves",
    "موجات S": "def:g11:seismic-structure:body-waves",
    "طيات": "def:g12:mountain-building:fold",
    "مصيدة": "def:g11:fossil-fuel-geology:trap",
    "مصائد": "def:g11:fossil-fuel-geology:trap",
    "مخزونات": "def:g10:freshwater-resources:stock",
    "صدوع عادية": "def:g11:ocean-ridges:normal-fault",
    "الصدوع العادية": "def:g11:ocean-ridges:normal-fault",
    "صدوع زاحفة": "def:g12:mountain-building:thrust",
    "صدوعًا زاحفة": "def:g12:mountain-building:thrust",
    "الصدوع الزاحفة": "def:g12:mountain-building:thrust",
    "عواصف رعدية": "def:g10:storms-and-cyclones:thunderstorm",
    "العواصف الرعدية": "def:g10:storms-and-cyclones:thunderstorm",
    "الأعاصير المدارية": "def:g10:storms-and-cyclones:tropical-cyclone",
    "المعادن الدليلية": "def:g12:metamorphic-rocks:index-mineral",
    "خطوط تساوي الدرجة": "def:g12:metamorphic-rocks:index-mineral",
    "خطوط تساوي درجة": "def:g12:metamorphic-rocks:index-mineral",
    "الصخور الجوفية": "def:g11:igneous-rocks:volcanic-plutonic",
    "صخور جوفية": "def:g11:igneous-rocks:volcanic-plutonic",
    "الصخور البركانية": "def:g11:igneous-rocks:volcanic-plutonic",
    "بلورات ظاهرة": "def:g11:igneous-rocks:porphyritic",
    "البلورات الظاهرة": "def:g11:igneous-rocks:porphyritic",
    "العينات الجليدية": "def:g12:past-climates:ice-core",
    "عينات جليدية": "def:g12:past-climates:ice-core",
    "دورات جليدية": "def:g12:past-climates:glacial-cycle",
    "الدورات الجليدية": "def:g12:past-climates:glacial-cycle",
    "الفترات الجليدية": "def:g12:past-climates:glacial-cycle",
    "فترتين جليديتين": "def:g12:past-climates:glacial-cycle",
    "الفترات بين الجليدية": "def:g12:past-climates:glacial-cycle",
    # bare "لوح/اللوح" is the slab in g11.06; its other senses (a glass plate,
    # a wooden board, a solar panel, a slab of shale) are masked below
    "لوح": "def:g11:subduction-zones:slab",
    "ألواح": "def:g11:subduction-zones:slab",
    "الألواح المندسة": "def:g11:subduction-zones:slab",
    "ألواح مندسة": "def:g11:subduction-zones:slab",
    "ألواحًا مندسة": "def:g11:subduction-zones:slab",
    "لوحًا مندسًا": "def:g11:subduction-zones:slab",
    "لوحها المندس": "def:g11:subduction-zones:slab",
    # stock and flux (g10.09): the indefinite and plural forms; "الدفق الحراري",
    # the other name of heat flow (g12.06), and the stored energy of g10.03
    # are masked below
    "مخزون": "def:g10:freshwater-resources:stock",
    "مخزونًا": "def:g10:freshwater-resources:stock",
    "دفق": "def:g10:freshwater-resources:stock",
    "دفقًا": "def:g10:freshwater-resources:stock",
    "دفوق": "def:g10:freshwater-resources:stock",
    "دفوقه": "def:g10:freshwater-resources:stock",
    # saturated (g10.04): the adjective, linked as English links "saturated"
    # and "the saturated rate"; "غير مشبع" (unsaturated, unlinked in English)
    # and the other saturations (with water, g10.08, g12.04; g10.05) are masked
    "مشبع": "def:g10:why-clouds-form:humidity",
    "مشبعة": "def:g10:why-clouds-form:humidity",
    "تشبعت": "def:g10:why-clouds-form:humidity",
    # possessive constructs of a harvested term (no suffix reaches them)
    "عتبة": "def:g11:igneous-rocks:intrusion",
    "جسمًا متداخلًا": "def:g11:igneous-rocks:intrusion",
    "أجسامًا متداخلة": "def:g11:igneous-rocks:intrusion",
    "المافيان": "def:g11:igneous-rocks:felsic-mafic",
    "الفلسيان": "def:g11:igneous-rocks:felsic-mafic",
    "زجاج بركاني": "def:g11:igneous-rocks:volcanic-plutonic",
    "نسيجه": "def:g11:igneous-rocks:texture",
    "نسيجها": "def:g11:igneous-rocks:texture",
    "أنسجة": "def:g11:igneous-rocks:texture",
    "بورفيرية": "def:g11:igneous-rocks:porphyritic",
    "الصدوع المعكوسة": "def:g12:mountain-building:thrust",
    "صدع ماكونيل الزاحف": "def:g12:mountain-building:thrust",
    "صدع غلاروس الزاحف": "def:g12:mountain-building:thrust",
    "غطاءً تكتونيًا": "def:g12:mountain-building:nappe",
    "الأغطية التكتونية": "def:g12:mountain-building:nappe",
    "معدل تجريد": "def:g12:destruction-of-mountains:denudation",
    "معدلات تجريد": "def:g12:destruction-of-mountains:denudation",
    "فترة عودته": "def:g10:drainage-basins:return-period",
    "فترة عودتها": "def:g10:drainage-basins:return-period",
    "فترات عودتها": "def:g10:drainage-basins:return-period",
    "جذرها": "def:g12:continental-crust:root",
    "بجذرها": "def:g12:continental-crust:root",
    "الجذور المشوهة": "def:g12:continental-crust:root",
    "درجة حرارة توازن": "def:g10:habitable-planet:equilibrium-temperature",
    "درجة حرارة توازنها": "def:g10:habitable-planet:equilibrium-temperature",
    "درجة حرارة توازنه": "def:g10:habitable-planet:equilibrium-temperature",
    "درجات حرارة التوازن": "def:g10:habitable-planet:equilibrium-temperature",
    "نقطة نداه": "def:g10:why-clouds-form:dew-point",
    "نقطة نداها": "def:g10:why-clouds-form:dew-point",
    "زمن مكوث": "def:g10:freshwater-resources:residence-time",
    "زمن مكوثه": "def:g10:freshwater-resources:residence-time",
    "زمن مكوثها": "def:g10:freshwater-resources:residence-time",
    "أزمنة مكوث": "def:g10:freshwater-resources:residence-time",
    "أزمنة المكوث": "def:g10:freshwater-resources:residence-time",
    # root: the mountain root only (bare "الجذور" is also plant roots, g10.07)
    "جذور الجبال": "def:g12:continental-crust:root",
    "جذور جبال": "def:g12:continental-crust:root",
    "الجذور العميقة": "def:g12:continental-crust:root",
    "الجذور المتآكلة": "def:g12:continental-crust:root",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
EXTRA_PROTECT = [
    # run-in paragraph headings and the bold Part headings of a weekend
    # problem stay unlinked, like section titles (English links neither)
    r'\\paragraph\{[^{}]*\}',
    r'\\textbf\{الجزء\s+(?:الأول|الثاني|الثالث|الرابع)(?:[^{}]|\{[^{}]*\})*\}',
    # \pageref and inline \tikz, as in English
    r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
    # تأثير: human influence (g12.10), not a forcing
    r'(?:ال)?تأثير(?:ات)?\s+(?:ال)?بشري(?:ة)?', r'كل\s+التأثيرات\s+البشرية',
    # deep ocean: the deep ocean floor (bathymetry), not the layer below the
    # thermocline (English protects "deep ocean floor")
    r'قاع\s+(?:ال)?محيط\s+(?:ال)?عميق',
    # stock: the heat stock of Kelvin's cooling Earth (g12.07 solutions)
    r'المخزون(?=\s+(?:حينئذ|نفسه))',
    # stratification: the original bedding of a mud (g12.03), not the ocean's
    r'التطبق\s+الأصلي',
    # felsic-mafic: ultramafic mantle rock (g12.06)
    r'فوق\s+(?:ال)?مافية',
    # root: the mathematical root (English protects square/fourth/cube root)
    r'(?:ال)?جذر\s+(?:ال)?(?:تربيعي|رابع|تكعيبي)',
    # metamorphism: "التحول" as a transition of rhythm (g12.09)
    r'(?:ال)?تحول\s+من\s+إيقاع', r'حدث\s+التحول',
    # لوح: the other senses of the word (the slab is linked bare, see EXTRA)
    r'لوح\s+(?:ال)?زجاج', r'لوح\s+خشبي', r'(?:وال|ال)لوح\s+الشمسي',
    r'لوح\s+من\s+السجيل', r'عرض\s+اللوح', r'كاللوح',
    # stock/flux: heat flow (g12.06), the energy stored in living things
    # (g10.03), a stock of heat (g12.07)
    r'(?<!\w)(?:ال)?دفق\s+(?:ال)?حراري', r'ينتهي\s+مخزونًا', r'مخزون\s+معين',
    # saturated: unsaturated, saturated with water, the storm chapter
    r'غير\s+(?:ال)?مشبع(?:ة)?', r'(?:ال)?مشبع(?:ة|ًا)?\s+بالماء',
    r'المشبعة\s+أصلًا', r'المشبع\s+كثيرًا', r'يحمله\s+الهواء\s+المشبع',
    # proper name: the invented Varden Hills (a region, not the landform)
    r'تلال\s+فاردن',
]
