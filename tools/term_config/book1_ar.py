"""Book 1 (Primary and Middle School, grades 1-9) -- ar. Curation only; the rules live in tools/termlink/.

Curated by the Book 1 `ar` agent (2026-10-25) from this edition's own harvest,
with the frequency and chapter-set censuses against the English twin.

lang_ar.py has no WORD_TAIL: the article and the one-letter prepositions are
a HEAD (ال، وال، بال، لل ...), so an indefinite term ("زلزال") also links
its definite forms ("الزلزال", "للزلزال"), but nothing reaches a broken
plural (زلازل), a dual (القطبين), a sound plural (كثبان is broken too) or an
accusative with tanween (زلزالًا). Those are declared below, term by term,
each one a form this edition really uses.
"""

# STOP (ordinary word outside its defining chapter, where it still links):
# - مخطط: g2.2's "plan" (of a room); everywhere else it is a chart or graph
#   ("مخطط الأعمدة", "مخطط درجة الحرارة"), which English never links;
# - ارتفاع: kept (it is the altitude of every later chapter), but its
#   other senses -- a rise, an uplift, a star's elevation -- are masked in
#   EXTRA_PROTECT below.
STOP = {"مخطط", "المخطط"}
NO_CAPITAL = set()

_P = "def:g7:plate-tectonics:"
EXTRA = {
    # g7 defines "الصفيحة التكتونية (أو الصفيحة اختصارًا)": the short form
    # is the one every later chapter uses (English: EXTRA "plate")
    "صفيحة": _P + "plate", "صفائح": _P + "plate",
    "حدود صفائح": _P + "plate-boundary", "حد صفائح": _P + "plate-boundary",
    "حدود متباعدة": _P + "plate-boundary", "حدود متقاربة": _P + "plate-boundary",
    "حدود تحويلية": _P + "plate-boundary",
    # English "date line" (5 links): the short form of خط التاريخ الدولي
    "خط تاريخ": "def:g6:latitude-longitude:date-line",
    # broken plurals, duals and accusatives of single-word terms
    "زلازل": "def:g4:volcanoes-earthquakes-first-look:earthquake",
    "زلزالًا": "def:g4:volcanoes-earthquakes-first-look:earthquake",
    "براكين": "def:g4:volcanoes-earthquakes-first-look:volcano",
    "بركانًا": "def:g4:volcanoes-earthquakes-first-look:volcano",
    "ثورانات": "def:g4:volcanoes-earthquakes-first-look:eruption",
    "حممًا": "def:g4:volcanoes-earthquakes-first-look:eruption",
    "سحب": "def:g4:clouds-rain-snow:cloud",
    "غيوم": "def:g4:clouds-rain-snow:cloud",
    "صخور": "def:g3:stones-pebbles-sand:rock",
    "صخرًا": "def:g3:stones-pebbles-sand:rock",
    "صخور رسوبية": "def:g6:rocks-and-minerals:rock-families",
    "صخور نارية": "def:g6:rocks-and-minerals:rock-families",
    "صخور متحولة": "def:g6:rocks-and-minerals:rock-families",
    "حصى": "def:g3:stones-pebbles-sand:pebble",
    "رملًا": "def:g3:stones-pebbles-sand:sand",
    "حجارة بناء": "def:g3:stones-pebbles-sand:building-stone",
    "حجر بناء": "def:g3:stones-pebbles-sand:building-stone",
    "معادن": "def:g6:rocks-and-minerals:mineral",
    "أحافير": "def:g7:sediments-and-fossils:fossil",
    "قوالب": "def:g7:sediments-and-fossils:fossil",
    "مصبوبات": "def:g7:sediments-and-fossils:fossil",
    "جبال": "def:g1:landscapes-around-us:landform",
    "تلال": "def:g1:landscapes-around-us:landform",
    "سهول": "def:g1:landscapes-around-us:landform",
    "أودية": "def:g1:landscapes-around-us:landform",
    "وديان": "def:g1:landscapes-around-us:landform",
    "الوادي": "def:g1:landscapes-around-us:landform",
    "وادي": "def:g1:landscapes-around-us:landform",
    "واديًا": "def:g1:landscapes-around-us:landform",
    "أشكال تضاريسية": "def:g1:landscapes-around-us:landform",
    "أنهار": "def:g1:landscapes-around-us:water",
    "بحيرات": "def:g1:landscapes-around-us:water",
    "سواحل": "def:g1:landscapes-around-us:water",
    "فيضانات": "def:g5:water-shapes-the-land:flood",
    "ينابيع": "def:g6:water-underground:spring",
    "آبار": "def:g6:water-underground:spring",
    "قطبين": "def:g3:continents-and-oceans:poles",
    "كثبان": "def:g9:landforms:dune",
    "جروف": "def:g9:landforms:cliff",
    "شواطئ": "def:g9:landforms:beach",
    "كهوف": "def:g9:landforms:karst",
    "بالوعات": "def:g9:landforms:karst",
    "أنهار جليدية": "def:g8:ice-on-earth:glacier",
    "منعطف": "def:g5:water-shapes-the-land:meander",
    "منعطفات": "def:g5:water-shapes-the-land:meander",
    "سلاسل جبلية": "def:g4:world-physical-map:range",
    "كواكب صخرية": "def:g6:earth-a-planet:planet-types",
    "كواكب عملاقة": "def:g6:earth-a-planet:planet-types",
    "خلايا حمل": "def:g8:winds-global-circulation:convection-cell",
    "خطوط تساوي ضغط": "def:g8:fronts-and-weather-maps:isobar",
    "خط تساوي ضغط": "def:g8:fronts-and-weather-maps:isobar",
    "دوامات محيطية": "def:g8:the-oceans:current",
    "تيارات محيطية": "def:g8:the-oceans:current",
    "محطة أرصاد": "def:g4:clouds-rain-snow:weather-station",
    "محطات أرصاد": "def:g4:clouds-rain-snow:weather-station",
    "محطة أرصاد جوية": "def:g4:clouds-rain-snow:weather-station",
    "محطات أرصاد جوية": "def:g4:clouds-rain-snow:weather-station",
    "جدول طقس": "def:g1:watching-the-weather:weather-chart",
    "رموز طقس": "def:g1:watching-the-weather:weather-chart",
    "رمز طقس": "def:g1:watching-the-weather:weather-chart",
    "مقاييس الزلازل": "def:g7:earthquakes:seismometer",
    "مقاييس المطر": "def:g4:clouds-rain-snow:rain-gauge",
    "مناطق زمنية": "def:g6:latitude-longitude:time-zone",
    "نطاقات مناخية": "def:g5:weather-and-climate:climate-zone",
    "عصور جليدية": "def:g8:ice-on-earth:ice-age",
    "غابات مطيرة": "def:g5:weather-and-climate:rainforest",
    "مخططات مناخية": "def:g5:weather-and-climate:climate-chart",
    # the globe: "مجسم" alone is the globe throughout this book
    "مجسم": "def:g3:continents-and-oceans:globe",
    "مجسمات": "def:g3:continents-and-oceans:globe",
    "مجسم كرة أرضية": "def:g3:continents-and-oceans:globe",
    "مجسمات كرة أرضية": "def:g3:continents-and-oceans:globe",
    # the legend: "المفتاح" and its possessives (English links "legend")
    "مفتاح": "def:g2:drawing-to-map:legend",
    "مفتاحه": "def:g2:drawing-to-map:legend",
    "مفتاحها": "def:g2:drawing-to-map:legend",
    # latitude and longitude: the lines and the degrees
    "دوائر عرض": "def:g6:latitude-longitude:latitude",
    "خط عرض": "def:g6:latitude-longitude:latitude",
    "خطوط عرض": "def:g6:latitude-longitude:latitude",
    "درجة عرض": "def:g6:latitude-longitude:latitude",
    "درجات عرض": "def:g6:latitude-longitude:latitude",
    # the bare definite forms, as English links bare "latitude"/"longitude";
    # their width and length senses are masked in EXTRA_PROTECT
    "العرض": "def:g6:latitude-longitude:latitude",
    "الطول": "def:g6:latitude-longitude:longitude",
    "خطوط زوال": "def:g6:latitude-longitude:longitude",
    "خط طول": "def:g6:latitude-longitude:longitude",
    "خطوط طول": "def:g6:latitude-longitude:longitude",
    "درجة طول": "def:g6:latitude-longitude:longitude",
    "درجات طول": "def:g6:latitude-longitude:longitude",
    # second census pass: more plurals, possessives and indefinite forms
    "مقياس رسم": "def:g2:drawing-to-map:scale",
    "مقياس رسمه": "def:g2:drawing-to-map:scale",
    "مقياس رسمها": "def:g2:drawing-to-map:scale",
    "قارات": "def:g3:continents-and-oceans:continent",
    "قدره": "def:g7:earthquakes:magnitude",
    "قدرها": "def:g7:earthquakes:magnitude",
    "قدرين": "def:g7:earthquakes:magnitude",
    "حقب": "def:g7:geological-time:era-period",
    "دوامة": "def:g8:the-oceans:current",
    "دوامات": "def:g8:the-oceans:current",
    "مصب": "def:g5:water-shapes-the-land:source-mouth",
    "مصبات": "def:g5:water-shapes-the-land:source-mouth",
    "منبعه": "def:g5:water-shapes-the-land:source-mouth",
    "أغطية جليدية": "def:g8:ice-on-earth:ice-sheet",
    "رفوف جليدية": "def:g8:ice-on-earth:ice-sheet",
    "نفوذة": "def:g6:water-underground:permeability",
    "كتيمة": "def:g6:water-underground:permeability",
    "خريطة للعالم": "def:g3:continents-and-oceans:world-map",
    "وردة رياح": "def:g2:drawing-to-map:directions",
    "صحارى": "def:g5:weather-and-climate:desert",
    "صحاري": "def:g5:weather-and-climate:desert",
    "صلادته": "def:g6:rocks-and-minerals:hardness",
    "صلادتها": "def:g6:rocks-and-minerals:hardness",
    "احتياطيات": "def:g9:earth-resources:reserve",
    "أخطار طبيعية": "def:g5:natural-hazards:hazard",
    "تدفقات فتاتية": "def:g7:volcanoes:pyroclastic-flow",
    "ألسنة رملية": "def:g9:landforms:beach",
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
    # \pageref and inline \tikz are not in the shared protect list
    r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
    # ارتفاع: a rise (of the sea, of a temperature, of a river), an uplift,
    # the elevation of a star, the height of a tower, a rise over a run
    r'ارتفاع\s+(?:متوسط|سطح|البحر|عام|درجة|صغير|الشمس|النجم|نجم)',
    # (lookaheads: a protect that CONSUMES a $ or a \qty puts the math
    # mask out of phase for the rest of the file)
    r'ارتفاع(?=\s+\$)', r'الارتفاع\s+(?:البطيء|الثاني|أبطأ|مقسوم)',
    r'(?:هذا|هل|كان|تسارع|تواصل)\s+الارتفاع', r'متوسط\s+الارتفاع\s+في\s+السنة',
    r'ارتفاع(?:\s+الأرض)?\s+(?:على\s+مسافة|لكل)',
    r'متساوي\w*\s+في\s+الارتفاع', r'نقطة\s+الارتفاع',
    r'قياس\s+الارتفاع\s+بالأقمار',
    # مقياس الرسم: "drawn to scale" (English protects "to scale")
    r'(?<=مرسومة )بمقياس', r'(?<=ليست )بمقياس', r'(?<=ليسا )بمقياس',
    r'(?<=الشمس، )بمقياس', r'(?<=الرسم\s)بمقياس', r'(?<=\\emph\{)بمقياس',
    r'(?<=مقطوعة، )بمقياس', r'(?<=شيء )بمقياس',
    r'(?<=ليس )بمقياس', r'(?<=بلا )مقياس', r'(?<=وسماكاتها )بمقياس',
    # العرض / الطول: a width and a length
    r'(?:معظم|نصف)\s+العرض', r'(?<=\$ )العرض',
    r'الطول(?=\s+(?:\$\\times|\\babelsublr|الكلي|التقريبي|نفسه))',
    r'بالطول\s+نفسه', r'بهذا\s+الطول', r'في\s+الطول\s+إلى',
    r'(?<=\} )الطول', r'(?<=& )الطول',
    # قدر: "as far as" (قدر ما)
    r'قدر\s+ما',
    # حقبة: the named eras (English links only "era" itself)
    r'حقبة\s+الحياة',
    # تسرب: a leak of pollutant, not infiltration
    r'تسرب\w*\s+من\s+الحقل', r'أي\s+تسرب', r'التسرب\s+الملو',
    # برد: cold ("الحر والبرد", "برد شديد") and the verb "cooled"
    r'(?:الحر|حر)\s+و?البرد', r'برد\s+(?:شديد|الغرانيت)',
    # مدار: an orbit
    r'مدار\s+حول', r'كل\s+مدار',
    # شدة: "strongly"
    r'بشدة',
    # معادن: the title of a book
    r'علم\s+المعادن',
    # صفائح: thin sheets of mica, flat slabs
    r'صفائح\s+(?:رقيقة|مسطحة)',
    # مفتاح: an identification key for rocks (g6.3), not a map legend
    r'مفتاح\s+لتعر', r'المفتاح\s+قائمة', r'استعمل\s+المفتاح\.',
    # لب: an ice core, not the Earth's core
    r'(?:لب|ألباب)\s+(?:ال)?جليد',
    # ك + تلة, ال + سهل: the HEAD manufactures "mass" and "easy"
    r'كتلة(?!\s+(?:ال)?هوائي)', r'(?:من|العدد)\s+السهل', r'بقدر',
    # قدره: "amounting to" before a quantity, not a magnitude
    r'قدره(?=\s+\\qty)', r'بمقياس\s+رسم\s+واحد',
    # credit lines and datasets (English "coastlines", one word; ETOPO1 relief)
    r'خطوط\s+السواحل', r'تضاريس\s+ETOPO1',
    # Antarctica, the flat face of a half ball, a stratovolcano, upstream,
    # hot springs on the sea floor, a sheet of sediment (a bed)
    r'القارة\s+القطبية', r'المستوي\s+لنصف', r'البركان\s+الطبقي',
    r'نحو\s+المنبع', r'اتجاه\s+المصب', r'ينابيع\s+حارة', r'صفيحة\s+من',
    # the kinds of moraine are named inside the moraine definition itself
    r'ركام\s+جليدي\s+(?:جانبي|طرفي)',
    # دوامة: an eddy of air or cloud, not an ocean gyre
    r'دوامات\s+(?:السحب|الهواء)',
    # proper name: the invented Varden Hills (a region, not the landform)
    r'تلال\s+فاردن',
]
