"""Book 3 (University, Year 1) -- ar. Curation only; the rules live in tools/termlink/.

Curated by the Book 3 `ar` agent (2026-10-28) from this edition's own harvest,
with the frequency and chapter-set censuses against the English twin
(translation_instruction.md), never by translating book3_en.py. AMBIG_POLICY is
"drop", as in English.

lang_ar.py has no WORD_TAIL: the article and the one-letter prepositions are a
HEAD, so an indefinite term also links its definite forms. Indefinite and plural
forms that the harvest cannot reach are declared in EXTRA, each one a form this
edition really uses in the right sense.

Every STOP entry below is an Arabic word that is also an ordinary word, and
whose target sense appears in a few chapters only (the census of 2026-10-28
found 9 of 184 targets unreached in Arabic, and the wrong senses listed here):
- الميل: the celestial declination (ch. 1, 27) and the slope of a line,
  an inclination or a tilt in ch. 2, 4, 13, 14, 16, 21, 24: STOP;
- الارتفاع: the altitude of a star (ch. 1) and the height or elevation of land,
  of a wave or of a piston everywhere else: STOP;
- الاتجاه: the trend of a line (ch. 6) and every ordinary direction (fast or
  slow direction of a crystal, the opposite direction, a vergence): STOP;
  "الغوص" (plunge) still links;
- الأصل: the parent isotope (ch. 25) and the ordinary "original": STOP;
- الإشعاعية: the luminosity of ch. 2 and the radiant or radiative quantities of
  ch. 3, 10, 25, 27 and the radiogenic daughter: STOP; "الدفق" (flux) still links;
- النظام: the system of ch. 24, and the closed or climate system of ch. 25-28:
  STOP.

Protects (EXTRA_PROTECT) keep the right sense of a homograph and mask the wrong one:
- رتبة: the order of interference (ch. 8) keeps "الرتبة الأولى" etc. (ordinals
  not masked); the order of magnitude, the rank of a stratigraphic unit and
  "من رتبة" (of the order of) are masked;
- الانحدار: dip (the attitude) keeps its links; "شديد الانحدار" (steep), the
  slope of a channel and of a region, "حجم الانحدار" are masked;
- المطابقة بالمربعات: the least-squares fit (ch. 18), not a log correlation;
- الامتداد المنقّط: a dotted extension line (ch. 9), not the strike;
- مستقرًا: a stable phase (ch. 21), not the stable triple junction;
- لجنة الخريطة الجيولوجية: the commission's name (ch. 24), not a geological map;
- المجموعة الشمسية: the solar system (ch. 25), not a stratigraphic group;
- نحو الشمال تدفّق الحرارة: a heat transport by overturning (ch. 29), not the
  heat flow of the Earth.
"""

AMBIG_POLICY = "drop"

STOP = {
    "الميل", "الارتفاع", "الاتجاه", "الأصل",
}

NO_CAPITAL = set()

EXTRA = {
    # accretionary prism (ch. 14): the indefinite form
    "كومة تراكمية": "def:b1:active-margins:accretionary",
    # evaporites (ch. 22-23): the plural and indefinite forms
    "الرسوبات التبخّرية": "def:b1:chemical-biogenic-sediments:evaporite",
    "رسوبات تبخّرية": "def:b1:chemical-biogenic-sediments:evaporite",
    "رسوب تبخّري": "def:b1:chemical-biogenic-sediments:evaporite",
    # sedimentary basin (ch. 23): the indefinite and plural forms
    "حوض رسوبي": "def:b1:diagenesis-basins:basin",
    "أحواض رسوبية": "def:b1:diagenesis-basins:basin",
    "الأحواض الرسوبية": "def:b1:diagenesis-basins:basin",
    # oriented samples (ch. 6): the plural and indefinite forms
    "العينات الموجّهة": "def:b1:field-lab-methods-1:sample",
    "عينات موجّهة": "def:b1:field-lab-methods-1:sample",
    "عينة موجّهة": "def:b1:field-lab-methods-1:sample",
    # temperature inversion (ch. 26)
    "انعكاس حراري": "def:b1:fluid-envelopes-structure:stability",
    # altitude of a star or the sun (ch. 1, 2, 27): the phrases only; the bare
    # word also means the height of land, a wave, a scale, so it stays STOPped
    "ارتفاع الشمس": "def:b1:spherical-astronomy:horizontal",
    "ارتفاع القطب": "def:b1:spherical-astronomy:horizontal",
    "ارتفاع القطب السماوي": "def:b1:spherical-astronomy:horizontal",
    "ارتفاع النجم": "def:b1:spherical-astronomy:horizontal",
    "ارتفاع النجوم": "def:b1:spherical-astronomy:horizontal",
    "ارتفاع الظهر": "def:b1:spherical-astronomy:horizontal",
    "ارتفاع سيريوس": "def:b1:spherical-astronomy:horizontal",
    "ارتفاع كانوبس": "def:b1:spherical-astronomy:horizontal",
    "الارتفاع والسمت": "def:b1:spherical-astronomy:horizontal",
    # declination (ch. 1, 27): the solar and stellar phrases; the bare word also
    # means a slope, an inclination, a mile
    "الميل الشمسي": "def:b1:spherical-astronomy:equatorial",
    "ميل الشمس": "def:b1:spherical-astronomy:equatorial",
    "ميل النجم": "def:b1:spherical-astronomy:equatorial",
    "ميل النجوم": "def:b1:spherical-astronomy:equatorial",
    "الميل السماوي": "def:b1:spherical-astronomy:equatorial",
    "الميل والمطلع المستقيم": "def:b1:spherical-astronomy:equatorial",
    # indefinite, plural and prepositional forms the matcher cannot reach from the
    # definite display (an EXTRA alias, checked in context; see the census of 2026-10-28)
    "معدن": "def:b1:rock-forming-minerals:mineral",
    "معادن": "def:b1:rock-forming-minerals:mineral",
    "المعادن": "def:b1:rock-forming-minerals:mineral",
    "أوليفين": "def:b1:rock-forming-minerals:groups",
    "بلاجيوكلاز": "def:b1:rock-forming-minerals:groups",
    "جارنيت": "def:b1:rock-forming-minerals:groups",
    "فلسبار": "def:b1:rock-forming-minerals:groups",
    "ميكا": "def:b1:rock-forming-minerals:groups",
    "بيروكسين": "def:b1:rock-forming-minerals:groups",
    "أمفيبول": "def:b1:rock-forming-minerals:groups",
    "طية": "def:b1:geological-maps:fold",
    "طيّة": "def:b1:geological-maps:fold",
    "طيات": "def:b1:geological-maps:fold",
    "طيّات": "def:b1:geological-maps:fold",
    "بقعة ساخنة": "def:b1:hotspots:hotspot",
    "بقع ساخنة": "def:b1:hotspots:hotspot",
    "البقع الساخنة": "def:b1:hotspots:hotspot",
    "كاولينيت": "def:b1:weathering-clays:clay-mineral",
    "سميكتيت": "def:b1:weathering-clays:clay-mineral",
    "إيليت": "def:b1:weathering-clays:clay-mineral",
    "كلوريت": "def:b1:weathering-clays:clay-mineral",
    "تدفّقات الحرارة": "def:b1:heat-budget:heat-flow",
    "انكشاف": "def:b1:geological-maps:geological-map",
    "انكشافات": "def:b1:geological-maps:geological-map",
    "تماس": "def:b1:geological-maps:geological-map",
    "تماسات": "def:b1:geological-maps:geological-map",
    "خريطة جيولوجية": "def:b1:geological-maps:geological-map",
    "مستوى محوري": "def:b1:faults-folds-fabrics:fold-elements",
    "زاوية أجنحة": "def:b1:faults-folds-fabrics:fold-elements",
    "أجنحة": "def:b1:faults-folds-fabrics:fold-elements",
    "قشرة": "def:b1:layered-earth:layers",
    "وشاح": "def:b1:layered-earth:layers",
    "لب خارجي": "def:b1:layered-earth:layers",
    "لب داخلي": "def:b1:layered-earth:layers",
    "عرض جغرافي": "def:b1:spherical-astronomy:geographic",
    "طول جغرافي": "def:b1:spherical-astronomy:geographic",
    "خط العرض": "def:b1:spherical-astronomy:geographic",
    "خطوط العرض": "def:b1:spherical-astronomy:geographic",
    "خط الطول": "def:b1:spherical-astronomy:geographic",
    "خطوط الطول": "def:b1:spherical-astronomy:geographic",
    "إزاحة رأسية": "def:b1:cross-sections:throw",
    "إزاحة أفقية": "def:b1:cross-sections:throw",
    "الإزاحة الأفقية": "def:b1:cross-sections:throw",
    "شعاب مرجانية": "def:b1:chemical-biogenic-sediments:reef",
    "جدار معلّق": "def:b1:faults-folds-fabrics:fault-elements",
    "جدار مرتكز": "def:b1:faults-folds-fabrics:fault-elements",
    "انزلاق صافي": "def:b1:faults-folds-fabrics:fault-elements",
    "متجهة انزلاق": "def:b1:faults-folds-fabrics:fault-elements",
    "غلاف صخري": "def:b1:layered-earth:lithosphere",
    # radiogenic daughter (ch. 25): the right sense of "إشعاعية" after a noun
    "الابنة الإشعاعية": "def:b1:radiometric-methods:radiogenic",
    "ابنة إشعاعية": "def:b1:radiometric-methods:radiogenic",
    "ابنته الإشعاعية": "def:b1:radiometric-methods:radiogenic",
    # azimuth (ch. 1, 12, 15, 28): the phrases only; the bare word is also the
    # zenith ("سمت الرأس") and a dip direction
    "سمت النجم": "def:b1:spherical-astronomy:horizontal",
    "سمت القطب": "def:b1:spherical-astronomy:horizontal",
    "سمت الشمس": "def:b1:spherical-astronomy:horizontal",
    "سمت الحركة النسبية": "def:b1:spherical-astronomy:horizontal",
    # trend of a line (ch. 5, 6): the phrases, the protect below lets them through
    "اتجاه خط": "def:b1:field-lab-methods-1:trend-plunge",
    "اتجاه الخط": "def:b1:field-lab-methods-1:trend-plunge",
    "اتجاه خطّ": "def:b1:field-lab-methods-1:trend-plunge",
    "اتجاه الخطّ": "def:b1:field-lab-methods-1:trend-plunge",
    # luminosity (ch. 2): the indefinite and plural forms ("إشعاعية الشمس"); the
    # wrong senses of the feminine are protected below
    "إشعاعية": "def:b1:observing-the-sky:flux",
    "الإشعاعيات": "def:b1:observing-the-sky:flux",
    "إشعاعيات": "def:b1:observing-the-sky:flux",
    # finite rotations (ch. 12): the section title and the plural
    "الدورانات المنتهية": "def:b1:plate-kinematics:finite-rotation",
    "دورانات منتهية": "def:b1:plate-kinematics:finite-rotation",
    # closure temperatures and cooling ages (ch. 25)
    "درجات الإغلاق": "def:b1:radiometric-methods:closure",
    "درجتي الإغلاق": "def:b1:radiometric-methods:closure",
    "درجة إغلاق": "def:b1:radiometric-methods:closure",
    "درجات إغلاق": "def:b1:radiometric-methods:closure",
    "درجتي إغلاق": "def:b1:radiometric-methods:closure",
    "أعمار التبريد": "def:b1:radiometric-methods:closure",
    "أعمار تبريد": "def:b1:radiometric-methods:closure",
    "عمر تبريد": "def:b1:radiometric-methods:closure",
}

DROP = set()
DERIVED = {}
PRIMARY_OK = set()

EXTRA_PROTECT = [
    # order of interference (ch. 8) keeps its ordinals; the other senses of
    # "الرتبة" (order of magnitude, rank, "of the order of") are masked
    r'(?<!\w)(?:(?:و|ف|ب|ل)(?:ال)?|ال)?رتبة(?!\s+(?:ال)?(?:أولى|ثانية|ثالثة|رابعة))',
    # dip keeps its links; steep slopes, the slope of a channel, its size
    r'شدي[دة]\S{0,2}\s+(?:ال)?انحدار',
    r'تعود\s+إلى\s+(?:ال)?انحدار',
    r'جداء\s+العمق\s+و(?:ال)?انحدار',
    r'(?<!\w)حجم\s+(?:ال)?انحدار',
    # trend: every ordinary direction (the bare word is also an emphasis
    # of the trend-plunge definition, so STOP alone does not hold); "اتجاه
    # الانحدار" (dip direction), "اتجاه الغوص" and "الاتجاه الانقلابي" keep theirs
    r'(?<!\w)(?:(?:و|ف|ب|ل)(?:ال)?|ال)?اتجاه(?!\s+(?:ال)?(?:انحدار|غوص|انقلاب|خطّ?(?!\w)))',
    # plunge of the subsidence (ch. 23), not the plunge of a fold
    r'(?<!\w)(?:و|ف)?(?:ال)?غوص(?=\s+الناجم)',
    # extension of the calderas (ch. 15), not a strike
    r'(?<!\w)(?:و|ف)?(?:ال)?امتداد\s+فرّق',
    # the bare "original" and parent isotope (ch. 25): an emphasis of the
    # radiogenic definition, so STOP alone does not hold
    r'(?<!\w)(?:(?:و|ف|ب|ل)(?:ال)?|ال)?أصل(?!\w)',
    # "to first order" (ch. 8, 11, 15, 26), as in English: an approximation
    # ("from the first order in ...", "... من الرتبة الأولى، أي"); the colour
    # sense ("من الرتبة الثانية (640 nm)") keeps its link
    r'(?<!\w)(?:من|إلى|حتى|عند)\s+(?:ال)?رتبة(?:\s+(?:ال)?(?:أولى|ثانية))?'
    r'(?=\s*(?:في|ل|لـ|\$|،|:|\\\[|\.|$))',
    # sides of a figure or a page, not a sense of fault type
    r'(?:الطرف|الركن|الصندوق|الجانب|الجهة)\s+(?:ال)?(?:أيمن|أيسر)',
    r'(?:في|على)\s+(?:ال)?(?:أيمن|أيسر)(?!\w)',
    # least-squares fit (ch. 18), not a log correlation
    r'(?<!\w)(?:ال)?مطابقة\s+بالمربعات',
    # dotted extension line (ch. 9), not the strike
    r'(?<!\w)(?:و|ف)?(?:ال)?امتداد\s+المنقّط',
    # a stable phase (ch. 21), not the stable triple junction
    r'مستقرًا',
    # the commission's name (ch. 24)
    r'لجنة\s+(?:ال)?خريطة\s+(?:ال)?جيولوجية',
    # the solar system (ch. 25)
    r'(?<!\w)(?:ال)?مجموعة\s+(?:ال)?شمسية',
    # heat transport by the overturning (ch. 29), not heat flow
    r'نحو\s+الشمال\s+تدفّق\s+الحرارة',
    # luminosity (ch. 2) is linked bare; these feminine "إشعاعية" phrases are
    # other quantities: irradiance (ch. 3), radiogenic daughter (ch. 25),
    # radiogenic heat (ch. 10), radiative fluxes and power (ch. 27), a radiative
    # layer and the discovery of radioactivity (ch. 10)
    r'(?<!\w)(?:(?:و|ف|ب|ل)(?:ال)?|ال)?شدّ?ة\s+(?:ال)?إشعاعي',
    r'(?<!\w)(?:(?:و|ف|ب|ل)(?:ال)?|ال)?حرارة\s+(?:ال)?إشعاعي',
    r'(?<!\w)(?:(?:و|ف|ب|ل)(?:ال)?|ال)?قدرة\s+(?:ال)?إشعاعي',
    r'تدفّقات\S*\s+(?:ال)?إشعاعي',
    r'طبقة\s+إشعاعي',
    r'اكتشاف\s+(?:ال)?إشعاعي',
    r'التقديرات\s+(?:ال)?إشعاعي',
    # crust (layers): the mathematical spherical shells (ch. 3, 9, 14), the
    # glassy rind of pillow lava (ch. 13) and an ice shell (ch. 3) are not the crust
    r'(?<!\w)(?:(?:و|ف|ب|ل)(?:ال)?|ال)?قشر(?:ة|ات|ور)\s+(?:رقيقة\s+نصف|كروية|منحنية|مجوّفة|زجاجية|نصف)',
    r'(?<!\w)(?:(?:و|ف|ب|ل)(?:ال)?|ال)?قشر(?:ة|ات)\s+من\s+الجليد',
    r'نظرية\s+(?:ال)?قشرة',
    r'قضية\s+(?:ال)?قشرة',
    # system (ch. 25-28, 17): the closed and the climate system, the same
    # system (faults); the chronostratigraphic system is linked bare
    r'(?<!\w)(?:ال)?نظام\s+(?:ال)?(?:مغلق|المناخي|نفسه)',
]
