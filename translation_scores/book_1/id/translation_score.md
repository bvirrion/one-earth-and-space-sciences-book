# Translation score — Earth and Space Sciences Book 1 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 1 (Primary and Middle School, Grades 1–9) |
| **Language** | Indonesian (`id`) |
| **Quality bar** | **native school prose at every level**: an Indonesian children's science book in grades 1–5 and an SMP *IPA* textbook (Earth and space strand) in grades 6–9. English is the source of truth for content, structure, labels, mathematics and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); the shipped Indonesian editions of One Biology Book 1 and One Chemistry Book 1 (`../one-biology-book/parts/grade-*/id/`, `../one-chemistry-book/parts/grade-*/id/`) for the *kamu* register, the bare-imperative exercise stems (*Sebutkan*, *Jelaskan*, *Hitunglah*, *Gambarlah*, *Tentukan*) and the solution header; the workspace `indonesian_style_card.md` for the Latin-script prose gate |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-25 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 32 chapters + 32 solution twins = **64 files**, every one written through `tools/id_apply.py`; `frontmatter/preface.id.tex` (*Kata Pengantar*) and `frontmatter/image-credits.id.tex` (*Kredit Gambar*, 32 items = English 32); the aside-box block of `styles/lang/id.tex` (coordinator wording kept, comment settled); a curated `tools/term_config/book1_id.py`; the defined-term link layer; Indonesian index keys; the overfull sweep; a page-by-page check of **every figure page** of the build (170 pages), with every collision fixed and re-rendered; and this score |

## Verdict in one line

An Indonesian Book 1 that reads as one Indonesian school course in the Earth
and space sciences from *bentuk muka bumi* in grade 1 to *profil topografi*
and *penentuan posisi dengan satelit* in grade 9: *bisa* and short
sentences for the youngest readers, *dapat* and the SMP definition frame
(*Yang disebut \emph{x} adalah ...*) in grades 6–9, Indonesian compass and
coordinate letters (U/T/S/B; LU/LS/BT/BB), the 24-hour clock with a dot
(*10.15.25*), with every structural and prose gate green over the nine years
and a forced build of **0 errors / 0 undefined / 0 overfull**, 344 pages
(English 324), `.fls` 64 = 64 files on disk.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror over the 64 files against their 64 twins: **370 `exercise` / 370**, **20 `problem` / 20**, **390 `\begin{solution}` / 390**, **234 `omfigure` / 234**, **161 `tikzpicture` / 161**, **73 `axis` / 73**, **120 `\includegraphics` / 120**, **455 `\emph` / 455**, **237 `\index` / 237** (no duplicate key), **105 `\cref` / 105**, **816 `\label` / 816** (set diff **0** both ways), **468 `\item` / 468**, **834 `\qty` / 834**, **110 `\num` / 110**, **588 `% ledger:` / 588**, and per environment 140 `definition`, 42 `method`, 60 `example`, 30 `recall`, 7 `inthefield`, 9 `inthelab`, 10 `history`, 2 `dated`, 7 `safety` — all exact. `\node` 741 against 677: the five figures whose labels English reads from a `\foreach` or pgfplots table are written as explicit nodes, exactly as the `fr` and `es` editions do (741 each). A number cross-check of every chunk (English vs Indonesian) leaves only time-format conversions (*1~jam~43~menit*, *10.15.25*) and `!draw` labels |
| Terminology | **96** | Indonesian school geoscience: *bentuk muka bumi* (g1) and *bentuk lahan* (the g9 geomorphology word, the recall box naming both), *dataran / dataran tinggi / dataran rendah*, *lereng*, *lembah*, *muara*, *hulu / hilir*, *pelapukan*, *erosi*, *pengendapan*, *batuan beku / sedimen / metamorf*, *batu kapur* (limestone, unified; *kapur* = chalk), *batu pasir*, *serpih*, *sekis*, *skala Mohs*, *kerak / mantel / inti luar / inti dalam*, *lempeng tektonik*, *batas divergen / konvergen / transform*, *punggung samudra*, *palung*, *dapur magma*, *lubang letusan*, *kawah*, *aliran piroklastik*, *hiposentrum / episentrum*, *seismometer / seismogram*, *magnitudo / intensitas*, *tsunami*, *fosil jejak*, *cetakan / tuangan*, *penanggalan relatif*, *ketidakselarasan*, *Paleozoikum / Mesozoikum / Kenozoikum*, *troposfer / tropopause*, *laju penurunan suhu lingkungan*, *sel konveksi*, *angin pasat / angin baratan / angin timuran kutub*, *massa udara*, *front dingin / hangat / oklusi*, *depresi / antisiklon*, *isobar*, *salinitas*, *pilin samudra*, *sabuk konveyor samudra global*, *gletser*, *daerah akumulasi / ablasi*, *moncong*, *morena*, *lapisan es / paparan es / gunung es / es laut*, *permafrost*, *anomali suhu*, *gas rumah kaca*, *bahaya alam / kerentanan / risiko / pencegahan*, *peta bahaya*, *endapan bijih / plaser*, *akuifer*, *cadangan*, *gumuk pasir / barkan / lereng luncur*, *dataran abrasi*, *gisik / lidah pasir*, *karst / dolina*, *proyeksi Mercator*, *skala angka / batang skala*, *garis kontur / interval kontur*, *penginderaan jauh / citra satelit / warna semu*. All 237 `\index{}` keys rewritten in Indonesian |
| Register / tone | **96** | The *kamu* register throughout (0 *Anda* over course and solutions), measured against the Indonesian biology and chemistry editions: over the whole book *dapat* 1.72, *bisa* 0.54, *kamu* 0.52, *kita* 1.16 per 1000 words; grades 1–3 lean on *bisa* (3.33) as a children's reader does, grades 7–9 on *dapat* (1.83), as an SMP textbook does. Exercise stems are bare imperatives with *-lah* where Indonesian textbooks use it (*Hitunglah*, *Gambarlah*, *Perhatikan*). Defined terms stay lowercase mid-sentence (the definition frame), so the harvest has no capitalised doubles |
| LaTeX hygiene | **99** | Forced build through the run's `build.sh` (`latexmk -g`): **0 errors, 0 undefined, 0 overfull**, 0 `invalid in math mode`, 0 non-backtick *Missing character*; `nullfont` 6633, the same count as every Latin-script edition of this book (the TikZ/pgfplots font-free measuring passes); `.fls` Indonesian source count **64** = 64 on disk. Nine overfull boxes found on the first build (an unbreakable credit line, a 45 pt *khatulistiwa* tick label in a `width=\linewidth` pgfplots axis, legend entries, two-line node labels) were fixed by rewording, rewrapping or `\allowbreak`, never with `%` or `\hbox`. Line-edge sweeps after the last file: no line-end word hyphen, no line starting on `. , ; : ) ? !`, no doubled word, every file valid UTF-8; `\text{}` census 14 = 14, all translated |
| Cross-refs / rule compliance | **99** | Labels, `\cref` targets, solution keys, `[resume]`, math spans (byte-for-byte, including internal line breaks), image paths, `% ledger:` lines and drawing code identical to English outside the `!draw` ranges listed below. No programme, curriculum or school-system name in visible text. No English source, style file or other edition touched; shared tools touched only by append-only, commented allow-list entries (listed below), each run once to confirm it changes the gate's verdict. No git command run, no commit |
| Figures | **95** | Drawing code byte-identical outside **68 `!draw` ranges** (listed below): `\foreach` label lists, pgfplots `xticklabels`/`yticklabels` that English reads from a table (made explicit), `symbolic coords` renamed, compass letters (N → U), the town T renamed K on the weather map (T is *tekanan tinggi*), markers R → B (*batu*) and H → P (*pondok*), and label repositioning where a longer Indonesian label collided. **Every figure page of the build (170 pages) was rendered and read**; collisions found and fixed by rewrapping or moving the label: the meander section, the Mohs scale note, the deepest-mine and borehole labels, the porosity panels, the convergent-boundary label, the time-scale *Fanerozoikum* / *Kenozoikum* boxes, the cold-front warm-air label, the sea-ice legend, the greenhouse *Matahari* and infrared labels, the coal-formation captions, the building-frame captions, the cooling magma body, the barchan labels, the contour-section slope labels, plus the nine first-build overfulls. Every fixed figure re-rendered from a probe build |
| Solutions | **97** | All 370 exercise solutions and all 20 weekend-problem solutions present and native; solution header *Bab \ref{..} --- Judul* matching each chapter title; every number cross-checked against English (no numeric slip); one double rounding found in the English canon (below) |
| Defined-term links (`\omterm`) | **96** | **6639 links over 137 distinct targets** against English's **6103 over 137**: every English target reached (**0 missing**). `book1_id.py` curated from **this edition's own harvest**: 1 STOP (*Piro*, an etymology emph), 19 EXTRA short, reduplicated and affixed forms (*lempeng*, *garis batas tanggal*, *daerah tropis*, *Garis Balik*, *zona-zona iklim*, *bermagnitudo*, *pilin*, *gumuk*, *bentuk lahan*, *gunung-gunung api*...), 33 homograph protections (compass *timur/barat laut*, *batu pasir*, *badai petir*, *aliran lumpur*, *dataran tinggi/rendah/abrasi*, *hulu angin*, *inti es*, *mata air panas*, the many *skala* of graphs and time, *Gunung Everest*-type proper names, *Perbukitan Varden*...). Frequency and chapter-set censuses run after the last edit; the residual outliers are explained: *ketinggian* covers both height and altitude (176 vs 68), *pegunungan* both mountains and mountain range (49 vs 10), *massa udara* and *prakiraan* within g8.3 itself. `--apply` twice changes nothing; plain dry run **links to insert: 0** |
| MT-artifact freedom | **96** | Indonesian prose gate (gate 8): 0 findings in all nine years. Twin-comparison gate (gate 9): 0 findings; the advisory tier read in full (cognates such as *magma*, *lava*, *tsunami*, *permafrost*, *isobar*; proper names and credits). Orphan-line gate (gate 10): 0 |

**Overall: 96.**

## Gate output summary

```
bash tools/check_translation.sh grade-1 … grade-9 id
  all nine years ............. TRANSLATION GATE: PASSED

forced build (scratchpad build.sh), build/one_earth_and_space_sciences_book_1_primary_middle_school_id.log
  '^!' ................. 0        undefined ............ 0
  Overfull ............. 0        nullfont ............. 6633
  'invalid in math mode' 0        Missing character .... 0 (non-backtick)
  pages ................ 344 (English 324)
  .fls Indonesian .tex . 64 (on disk 64)

python3 tools/link_defined_terms.py --book 1 --lang id      (plain dry run)
  links to insert: 0 across 0 files
links 6639 over 137 targets (English 6103 over 137; 0 English targets missed)
\index 237 = English 237 · \label set diff 0 · \qty 834 = 834 · % ledger: 588 = 588
```

## Conventions

* **Compass and coordinates**: U (utara), T (timur), S (selatan), B (barat) on
  every north arrow and in the text; latitude/longitude as LU / LS / BT / BB
  (*14.9° LU, 23.5° BB*). On the weather map T is *tekanan tinggi* and R
  *tekanan rendah*, so the English town T became K (*kota*).
* **Time**: 24-hour clock with a dot (*06.00*, *10.15.25*); durations as
  *1~jam~43~menit*.
* **Decimal point** kept as in English (the series keeps math spans
  byte-identical).

## `!draw` ranges (English line numbers)

g1/01 92–93, 97–98, 122–123, 136–138, 187–189, 204–207 · g1/02 228 ·
g3/01 104–109 · g3/02 63–65, 77–79, 250–251 · g4/01 378–379 · g4/03 87–88,
93–95 · g5/01 57–59 · g5/03 168–169 · g6/01 76, 149, 207–208, 219–220,
329–330, 366–367 · g6/02 54, 244–246, 251–256, 325–326 · g6/03 323–324, 328,
333 · g6/04 221 · g6/05 224–225, 271–273 · g7/01 342–344 · g7/02 474, 476 ·
g7/03 204, 206, 340, 342–343 · g7/04 163, 322 · g7/05 421–423, 436–444,
510–512, 515–520 · g8/01 131–133, 209–211 · g8/02 142, 263, 268, 391–392 ·
g8/03 73–74, 134 · g8/04 290–291, 358–359, 504–505 · g8/05 264–266, 269 ·
g9/01 56, 214 · g9/03 77, 244–247 · g9/05 72, 81, 179–181, 188, 192–193, 268.

## Shared-tool appends (append-only, each with a comment)

`tools/check_indonesian_prose.py` allow-list entries: (1) *Natural Earth*;
(2) institution names in credits; (3) `pgfplotstableread` + `circle`;
(4) `rectangle`; (5) *Big Spring*; (6) *This Dynamic Earth*; (7) *Smithsonian
Institution*; (8) *Borah Peak*; (9) *Hermits Rest*; (10) ellipse radii in a
`\tikzset` outside a tikzpicture, and *Siccar Point*; (11) *front* not gated
(KBBI meteorological term; *fronts* stays gated); (12) *The Times*;
(13) *Founders of Oceanography*; (14) *Laboratory for Satellite Altimetry*;
(15) *USGS Circular*; (16) *Japan Space Systems* / *ASTER Science Team*;
(17) *Birling Gap* / *White Sands* / *Lagoa dos Barros*; (18) *EROS Data
Center* / *Visible Earth*. `tools/check_latin_prose.py`: (19)
`ALLOWED_BY_LANG["id"]` += *gran, bas, sand, slat, shal* (the g6/03 `\foreach`
node-name pairs).

## Samples (Indonesian, with verdict)

1. **grade 7, definition** — "Yang disebut \emph{lempeng tektonik} (atau
   singkatnya lempeng) adalah bongkah batuan yang besar dan kaku, yang menjadi
   bagian dari cangkang luar Bumi." → **native**: the SMP definition frame,
   *singkatnya* for "plate for short".
2. **grade 6, groundwater** — "Mata air itu mengalir di tempat dasar lapisan
   kapur bertemu dengan lereng bukit: air tidak dapat turun menembus serpih,
   jadi air mengalir di sepanjang permukaan atas serpih dan keluar di lereng."
   → **native**: *menembus*, *di sepanjang*, the *jadi* consequence clause.
3. **grade 8, glaciers** — "Jika keduanya seimbang, ujung depan gletser, yaitu
   moncongnya, tetap berada di tempat yang sama." → **native**: *yaitu*
   apposition and the possessive *-nya* where English says "its snout".
4. **grade 9, hazards** — "Pencegahan bekerja pada kedua sisi kisi risiko." →
   **native**: compact nominal sentence, *kisi risiko* for the risk grid.
5. **grade 9, landforms** — "Gumuk pasir bergerak. Angin menggulirkan dan
   melontarkan butir-butir pasir menaiki lereng yang landai" → **native**:
   *menggulirkan / melontarkan* (roll / bounce) and the reduplicated plural.

## Canon defects found (reported, not edited)

* `parts/grade-7/solutions/01-plate-tectonics.tex:71` — "$14.2 \div 2.2
  \approx 6.5$: about 6 times faster (6.45, rounded)": the displayed value is
  rounded twice (6.45 → 6.5 → "about 6", but 6.5 would round to 7). Suggest
  `\approx 6.45`. The Indonesian edition mirrors the math span.
* `frontmatter/image-credits.tex` writes *Viñas* as `Vi\~nas`; the Indonesian
  credits use UTF-8.

## Tool bugs found

* `tools/check_indonesian_prose.py` `check_titles`: a file whose path contains
  no `/id/` is compared with itself, so a scratch copy flags every title as
  identical to English.
* A pic defined in a `\tikzset` outside a tikzpicture is read by the prose
  gate as visible text (worked around by allow-list entry 10).
* `check_translation.sh` does not gate the front matter (preface, credits);
  those two files were checked by hand and by the build.

## Why not 100

* **No Indonesian hyphenation patterns in the TeX stack** (babel's *bahasa*
  falls back to English patterns). No bad break was noticed in the PDF, but the
  paragraph builder works with the wrong patterns; shared infrastructure.
* **68 `!draw` opt-outs** — each justified, but each a place where only the
  rendered page, not the census, guards the figure. The page check of every
  figure found 15 collisions after a 0-overfull build: the gates alone would
  not have caught them.
* **Shared prose gate extended** nineteen times (append-only, commented), most
  for English proper names in photo credits.
* **Link density +9 %** against English, mostly from *ketinggian* and
  *pegunungan*, each covering two English words; every class was read in
  context.

## Coordinator addendum (2026-10-25)

Re-verified by the coordinator:
- a forced build: 344 pp, 0 errors / 0 undefined / 0 overfull, nullfont 6,633, `.fls` 64 = 64;
- `check_translation.sh` 9/9 PASSED; linker dry run 0;
- the draw census differs from English only in five figdata label-table rewrites (the same files as fr/es);
- the time-scale page (p. 175) and a grade-8 solutions page read at 110 dpi.

The reported double rounding in grade-7 solution 11 was fixed in the canon and mirrored here ("$\approx 6.45$: kira-kira 6 kali lebih cepat."), and "Viñas" is now UTF-8 in every credits file. The score is unchanged.
