# Translation score — Earth and Space Sciences Book 2 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 2 (High School, Grades 10–12) |
| **Language** | Indonesian (`id`) |
| **Quality bar** | **native SMA prose**: an Indonesian upper-secondary Earth-science / geography textbook, *kamu* register. English is the source of truth for content, structure, labels, mathematics and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); this series' Indonesian Book 1 (`parts/grade-{1..9}/id/`, its score file, `book1_id.py`) for every convention it owns (U/T/S/B, LU/LS/BT/BB, weather-map T/R, town K, the IPCC calibrated terms of g9); the French Book 2 edition for sense where the English is terse; the shipped Indonesian Biology Book 2 (`../one-biology-book/parts/grade-1{0,1,2}/id/`) for the SMA register of exercise stems |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-26 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 28 chapters + 28 solution twins = **56 files**, every one written through `tools/id_apply.py` from patch files kept in the agent's private scratch directory; `frontmatter/image-credits-book2.id.tex` (*Kredit Gambar*, 59 items = English 59; frame and descriptions translated, every credit, author, dataset, identifier and licence kept exactly — checked by script); the entry file's `\bookline` / `\author` (the coordinator's Indonesian, kept); a curated `tools/term_config/book2_id.py`; the defined-term link layer; Indonesian index keys; append-only allow-list entries (below); this score. The preface is shared with Book 1 and was not touched |

## Verdict in one line

An Indonesian Book 2 that reads as one SMA course from *elipsoid referensi*
and *neraca energi* in grade 10 to *gaya radiatif* and *sensitivitas iklim
kesetimbangan* in grade 12, with Book 1's compass, coordinate and IPCC
conventions carried through, every structural and prose gate green over the
three years, and a forced build of **0 errors / 0 undefined / 0 overfull**,
379 pages (English 362), `.fls` 56 = 56 files on disk.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror over the 56 files against their 56 twins: **420 `exercise`**, **28 `problem`**, **448 `\begin{solution}`**, **205 `omfigure`**, **141 `tikzpicture`**, **104 `axis`**, **100 `\includegraphics`**, **371 `\emph`**, **219 `\index`** (219 distinct keys, no duplicate), **132 `\cref`**, **764 `\label`** (set diff **0** both ways), **752 `\item`**, **3,685 `\qty`**, **446 `\num`**, **141 `\ce`**, **658 `\node`**, **561 `% ledger:`** (byte-identical), and per environment **141 `definition`, 58 `proposition`, 34 `method`, 43 `example`, 28 `recall`, 12 `history`, 5 `dated`, 1 `inthefield`, 1 `inthelab`, 2 `safety`** — all equal to English |
| Terminology | **96** | SMA geoscience Indonesian, consistent over three years and with Book 1: *elipsoid referensi, penggepengan, geodesi, triangulasi*; *suhu kesetimbangan, zona layak huni, albedo, insolasi, kalor laten/sensibel*; *kelembapan relatif, titik embun, laju adiabatik kering, aras kondensasi, udara stabil/tidak stabil*; *badai guntur, petir, tornado, siklon tropis, mata, dinding mata, gelombang badai, skala Saffir--Simpson*; *termoklin, haloklin, piknoklin, lapisan tercampur, penaikan massa air*; *saprolit, laterit, hidrolisis, mineral lempung*; *daerah aliran sungai, garis pemisah air, debit, hidrograf, aliran dasar, periode ulang*; *stok, fluks, waktu tinggal, air tanah fosil*; *magnetisasi remanen, pembalikan magnetik, pemekaran dasar samudra*; *gelombang P/S, gelombang kepala, jarak silang, kurva waktu tempuh, Moho, zona bayangan, zona kecepatan rendah*; *isostasi (Airy), kedalaman kompensasi, litosfer, astenosfer, geoterm*; *lempengan, tarikan lempengan, dorongan punggung, zona Wadati--Benioff, eklogit, sekis biru*; *belahan, pecahan, habitus, kilap, sayatan tipis, mikroskop polarisasi*; *batuan vulkanik/plutonik, mafik/intermediet/felsik, fenokris, porfiritik, retas, sill, pluton, batolit*; *batuan sumber, batuan reservoir, batuan penutup, perangkap, jendela minyak/gas, pembatubaraan, peringkat*; *kraton, pertumbuhan benua, akar, nappe, sesar anjak/naik, sutura, ofiolit*; *metamorfisme kontak/regional, aureol, foliasi, skistositas, mineral indeks, isograd, polimorf*; *pelelehan hidrus, busur gunung api, front vulkanik, baji mantel*; *laju denudasi, muatan dasar/suspensi/terlarut, diagenesis, pantulan isostatik*; *aliran panas, produksi panas radiogenik, pendinginan sekuler, konveksi mantel, energi panas bumi*; *sistem tertutup, isokron, umur Bumi*; *pelepasan gas, atmosfer purba, masalah Matahari muda yang redup, stromatolit, formasi besi berpita, Peristiwa Oksidasi Besar, lapisan merah*; *arsip iklim, proksi, inti es, firn, siklus glasial, Maksimum Glasial Terakhir, analisis/diagram polen*; *gaya radiatif (efektif), umpan balik iklim, sensitivitas iklim kesetimbangan, skenario emisi, proyeksi, atribusi*. All 219 `\index{}` keys in Indonesian; place names in their Indonesian form where one exists (*Kalimantan, Jawa, Laut Cina Selatan, Samudra Hindia, Paparan Sunda, Semenanjung Malaya*) |
| Register / tone | **96** | The *kamu* register throughout (**0** *Anda*, **0** *kalian*); measured over the 156,673 words of the edition: *dapat* 1.52, *bisa* 0.00, *kamu* 0.13, *kita* 0.11 per 1000 words — the SMA textbook profile (impersonal, *dapat*), against Book 1's children's-to-SMP slope. Exercise stems are bare imperatives (*Hitung* 188, *Bandingkan* 76, *Jelaskan* 51, *Sebutkan* 29, *Definisikan* 24, *Tentukan* 21), as Indonesian Biology Book 2 does; numbered `method` steps keep the *-lah* form (*Ambillah, Bacalah, Periksalah, Ukurlah*). Defined terms stay lowercase mid-sentence in the definition frame *Yang disebut \emph{x}\index{x} adalah …*. Observation only: no imperative sends the reader to a quarry, cliff, outcrop or the Sun (gate 7b green). Climate chapters are physical science only; IPCC calibrated language as Book 1 g9 (*hampir pasti, amat sangat mungkin, sangat mungkin, mungkin, sama mungkinnya dengan tidak, kecil kemungkinannya, sangat kecil kemungkinannya*; *keyakinan rendah/sedang/tinggi*), italic only where English has `\emph`; interval acronyms and SSP codes in English |
| LaTeX hygiene | **99** | Final forced build through the run's `build.sh` (`latexmk -g`): **0 errors, 0 undefined, 0 overfull**, 0 `invalid in math mode`, 0 non-backtick *Missing character*; `nullfont` **3,291** = the English baseline; `.fls` Indonesian sources **56** = 56 on disk. Overfull boxes met during the run (a tabular in g12/09, earlier five in grades 10–11) fixed by rewording, never with `%` or `\hbox`. Two line-broken `\index` keys (g12/05, g12/08) caught by gate 4 and rejoined. Final line-edge sweeps: no line ending on an apostrophe, no prose line opening on `. , ; : ) ? !` (the only hits are TikZ `.. controls` continuations), no dangling hyphen; `\text{}` census all Indonesian (*tahun, juta, sampai, kini, udara, …*) |
| Cross-refs / rule compliance | **99** | Labels, `\cref` targets, solution keys, `[resume]`, math spans (byte-for-byte, internal line breaks included, except the two forced spans below), image paths, `% ledger:` lines, `\ce{}` and drawing code identical to English outside the `!draw` ranges listed below. No programme, curriculum or school-system name in visible text. No English source, style file, Book 1 file or other edition touched; shared tools touched only by append-only, commented allow-list entries placed before the `__main__` guard, each confirmed to change the gate's verdict. No git command run, no commit |
| Figures | **95** | Every visible label translated (nodes, legends, tick labels, titles); `\foreach` tuples and `yticklabels`/`xticklabels` with visible words under per-range `!draw` (list below). Figure pages of grade 12 rendered at 100–130 dpi and read; four collisions found and fixed, then re-rendered: the melt label overflowing its ellipse (g12/04: *pelelehan* → *lelehan*), the *lempengan dingin tenggelam* label crossing the slab (g12/06, three lines), and the two isochron slope labels running over the y axis (g12/07, `\shortstack[r]`). Grades 10–11 figure pages were checked when those chapters were written, not re-read one per page in this final pass |
| Solutions | **97** | All 420 exercise solutions and 28 weekend-problem solutions present and native; solution header `\section*{Bab \ref{…} --- Judul}` matching each chapter title; every number recomputed along the rounded path (the canon fixes of g12/04s 35 km, g12/05s 67 Myr and g12/06s 56.7 TW are mirrored) |
| Defined-term links (`\omterm`) | **96** | **2,345 links over 139 distinct targets** (def 2,302, ex 26, prop 17) against English's **2,208 over 136**: every English target reached (**0 missing**), plus three English never reaches, each a single in-chapter occurrence (*Inti kondensasi* g10/04, *Anomali magnetik* g11/01, *isostasi Airy* g11/03). `book2_id.py` curated from this edition's own harvest (below). Frequency and chapter-set censuses run after the last edit: no target below 0.67× or above 1.7× English except the three above and *geodesi* (5 vs 2: Indonesian repeats *ahli geodesi* where English says "geodesists"); chapter-set differences are six single sites, each a correct link. `--apply` twice changes nothing; dry run **links to insert: 0**; `--check` clean |
| MT-artifact freedom | **96** | Indonesian prose gate (gate 8): 0 findings in all three years. Twin-comparison gate (gate 9): 0 multi-word findings; the advisory one-word tier read in full: proper names (*Moho, Zagros, Himalaya, Kelvin, Joly, Holmes, Patterson, Nuevo Laredo, Sumatra, Varden*), the eon name *Hadean*, and three words Indonesian uses as is (*garnet*, *nappe*, *birch/hazel* as pollen-diagram taxa) |

**Overall: 96.**

## Gate output summary

```
bash tools/check_translation.sh grade-10 id ... TRANSLATION GATE: PASSED
bash tools/check_translation.sh grade-11 id ... TRANSLATION GATE: PASSED
bash tools/check_translation.sh grade-12 id ... TRANSLATION GATE: PASSED

forced build (scratchpad build.sh), build/one_earth_and_space_sciences_book_2_high_school_id.log
  '^!' ................. 0        undefined ............ 0
  Overfull ............. 0        nullfont ............. 3291 (English 3291)
  'invalid in math mode' 0        Missing character .... 0 (non-backtick)
  pages ................ 379 (English 362)
  .fls Indonesian .tex . 56 (on disk 56)

python3 tools/link_defined_terms.py --book 2 --lang id      (plain dry run)
  links to insert: 0 across 0 files
links 2345 over 139 targets (English 2208 over 136; 0 English targets missed)

coordinator's draw census (drawcensus.py id): 4 files differ, all in node TEXT
  g11/04 'circle' 6->5   node "small circle about the pole" translated
  g11/06 'arc'    2->0   nodes "volcanic arc", "back-arc" translated
  g12/02 'arc'    1->0   node "volcanic arc" translated
  g12/07 'circle' 1->0   node "ocean sediment (circle)" translated
  node counts equal everywhere (658 = 658)
```

## Conventions

* **Compass and coordinates** (Book 1): U/T/S/B; `\ang{x}~LU/LS/BT/BB`.
* **Numbers**: decimal point kept (math spans byte-identical); *setahun*,
  *per sejuta tahun*, *miliar* for billion.
* **Cross-book references**: "(Buku 1, kelas N)"; sister series as
  "buku-buku fisika / kimia / biologi / matematika".
* **Headings**: `\section{Latihan}`; weekend problem
  `[{Soal akhir pekan --- …}]`; Part headings `\textbf{Bagian I --- …}`.
* **Definitions**: `Yang disebut \emph{x}\index{x} adalah …`; "admitted" =
  *diterima tanpa bukti*; "and others" = *dan kawan-kawan*; photographs
  *Foto*, *domain publik*, AI images *(ilustrasi AI)*.
* **IPCC**: Book 1 g9 terms (above); *sangat kecil kemungkinannya* for "very
  unlikely" (new in Book 2).

## Departures from Book 1 conventions, and why

1. **Bare-imperative exercise stems** (*Hitung, Jelaskan*) instead of Book 1's
   *-lah* stems (*Hitunglah*): the SMA register of the shipped Indonesian
   Biology Book 2; method steps keep *-lah*.
2. **`\unit{m/Ma}` for m/Myr in ch. 12.5** (g12/05 l. 161 display, g12/05s
   exercise 15 and problem Q1): *Ma* is the unit Indonesian geology writes, as
   the French edition does in prose; it changes three math spans, applied with
   `--force-classes math` after a dry run showed it was the only divergence.
3. **Kalimantan** for Borneo (the Indonesian name of the island; the map label
   too), **Jawa**, **Semenanjung Malaya** (*Smj. Malaya* on the map).
4. **Terms**: *batuan sumber* for the petroleum source rock, because
   *batuan induk* is the soil's parent rock in g10/07; *hidrus* (not
   *hidrous*) for hydrous melting.

## `!draw` ranges (English line numbers)

g10/02 133–134, 299 · g10/03 226–229 · g10/05 58 · g11/08 153, 162–169 ·
g11/09 542 · g12/01 117–118, 122 · g12/05 85–88, 272 · g12/06 170–171,
286–287 · g12/09 270–271 · g12/10 200–203, 396–399.

## Forced classes

* `g12-05`: `--force-classes math` — display l. 161, unit m/Myr → m/Ma.
* `g12-05s`: `--force-classes math` — exercise 15 and problem Q1,
  `\qty{..}{m/Myr}` → `m/Ma` inside `$…$`.

Both verified by dry run to be the only math divergence; logged in the
agent's `forced.txt`.

## Link layer (`tools/term_config/book2_id.py`)

* **STOP** (as English where English has the twin): *stabil / tidak stabil,
  jenuh, kejenuhan, fluks, stok, perangkap, mata, penggepengan*; plus
  *peringkat* (the flood-peak rank m in g10/08), *pecahan* (a meteorite
  fragment in g12/07), *proyeksi*, *gaya* (a force elsewhere), *vulkanik*.
* **EXTRA**: the climate chapter's short forms *gaya / gaya-gaya*,
  *umpan balik*, *skenario*, *sensitivitas iklim* (English EXTRA forcing,
  feedback, scenario, climate sensitivity; they link only from g12/10 on, the
  last chapter); the bare *plutonik / vulkanik* (English links bare
  "plutonic"/"volcanic"); *mineral-mineral lempung* (reduplicated plural).
* **EXTRA_PROTECT**: `\paragraph`, the `\textbf{Bagian …}` Part headings,
  `\pageref`, inline `\tikz`; *Perbukitan Varden*, *Gunung X*;
  *Interglasial Terakhir*, *Sesar Naik/Anjak Glarus/McConnell*; *Belahan
  Bumi* and *dua/satu/kedua belahan* (hemispheres, not cleavage); *akar
  kuadrat/pangkat/kubik/dari* and plant roots; *dasar samudra dalam*;
  *intrusi air laut/asin*; *front vulkanik*, *kawasan vulkanik*.
* Note for the toolkit: an EXTRA entry bypasses STOP (`terms.update(EXTRA)`
  runs after the STOP filter), so an EXTRA short form that is also STOPped
  links everywhere after its definition; the non-rock *vulkanik* had to be
  protected instead. Not a bug (the code says "manual entries win"), but the
  `book2_en.py` docstring's "STOP (ordinary word outside its defining chapter)"
  does not hold for EXTRA keys.

## Shared-tool entries (append-only, each confirmed to flip the gate)

`tools/check_indonesian_prose.py` (`ATTRIBUTION` extensions, each with its
reason and "Indonesian Earth & space Book 2 agent"): *Curiosity* (rover);
*Albedo Bond*; *History of Ocean Basins*, *Magnetic anomalies over oceanic
ridges*, *JOIDES Resolution*; *Texas A&M University* (tool fix, below);
*Giant's Causeway*, *The Evolution of the Igneous Rocks*; *White, McKenzie*,
*Chris Light*; *The Geysers*; *Russell and Sons*, *Forest City*; *Wendy from
Pennsylvania*; *Dartmouth Electron Microscope Facility*.

`tools/check_latin_prose.py`: `ALLOWED_BY_LANG["id"] |= {"bandB" … "bandF"}`
— the never-printed colour names of the g12/02 fold block diagram's two
`\foreach` lists (the es/pt/fr/nl editions appended the same entry); gate 9
went from exit 1 to exit 0.

## Tool bugs reported

1. `tools/check_indonesian_prose.py`: Book 1's institution entry
   `Texas\s+A\\?&M\s+University` can never match, because `visible_text()`
   drops the escaped ampersand and the gate sees "Texas AM University". Fixed
   by an appended alternative `Texas\s+A&?M\s+University`.

## English-canon defects

None new found in this edition's pass. The canon fixes made during the run
(g12/04s 35 km, g12/05s 67, g12/06s 56.7 TW, the g12/02 `\num{35} to`) are
mirrored. One cross-edition observation for the coordinator:
`parts/grade-12/fr/05-destruction-of-mountains.tex` l. 179 keeps
`\qty{56}{m/Myr}` inside the display while its prose writes m/Ma, and
`parts/grade-12/solutions/fr/05-destruction-of-mountains.tex` ll. 102 and 108
keep `\qty{100}{m/Myr}` and `\qty{418}{m/Myr}` inside `$…$` (the math gate
freezes those spans unless forced).

## Coordinator amendments

- 2026-10-26: g11 solutions/08 answer 16 rewritten by the coordinator after an English canon fix (reported by hi): ≈ 950 days, 2.6 years, within the intrusion range, not "between the two". Gates for grade 11 re-run, green; linker dry run 0.
- 2026-10-26: g11/01 "Motonari" → "Motonori" Matuyama, and the g12/02 fold-shortening chart labels (Varden label no longer clipped, 13 % label moved below-right of its point), both English-canon fixes after the Arabic report; mirrored by the coordinator.
