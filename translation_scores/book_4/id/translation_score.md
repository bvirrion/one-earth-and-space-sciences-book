# Translation score — One Earth and Space Sciences Book 4 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 4 (University Year 2, `bachelor-2`) |
| **Language** | Indonesian (`id`), Bahasa Indonesia modern lecture register (*kamu*/*-mu*) |
| **Overall score** | **95 / 100** (ship threshold ≥ 95 — met) |
| **Date** | 2026-10-30 |
| **Model** | `claude-opus-5-5` (Opus 5.5), effort high; one agent for the whole edition |
| **Scope** | 62 files (31 chapters + 31 solution twins), first written through `tools/id_apply.py` line-range patches over the numbered English, then finished and read by editing the `.tex` directly (the patches are stale; never re-apply them); `frontmatter/image-credits-book4.id.tex` (every credit, author, dataset and licence kept exactly; frame and descriptions translated); `tools/term_config/book4_id.py`; the `\bookline` and `\author` lines of the entry file; the term layer; append-only, commented allow-list entries in two prose gates; this score |

## Verdict in one line

A complete Indonesian Book 4 that reads as one second-year university course,
structurally identical to English, every gate green, built 0 errors /
0 undefined / 0 overfull. Every chapter and every solution was read sentence by
sentence against its English twin (Phase C, ch01–31 and sol01–31), with a
number-token diff per file; about forty meaning, register and consistency fixes
came out of that reading, none of which changed a number, label, reference or
formula.

## Measured

| Measure | Value |
|---|---|
| Files | 62 (`.fls` = 62 on disk) |
| Pages | 518 (English 484, French 509) |
| Links | 2,246 `\omterm` over 197 distinct targets (English 2,019 / 191). Every English target is reached. Six targets English never reaches, one link each, all checked right: *rayapan tsunami* (ch28), *asimilasi kerak* (ch12), *lewat jenuh silika* (ch09), *tafonomi* (ch20 caption), *seri metamorfik* (ch11), *unsur tanah jarang* (ch09). Last cycle `--unwrap --apply` (2,245 removed) then `--apply` (2,246 inserted, 464 linkable terms); dry run after the last edit: **links to insert: 0** |
| Build | `one_earth_and_space_sciences_book_4_university_year_2_id` latexmk exit 0 | pages 518 | errors 0 | undefined 0 | overfull 0 | nullfont 0 | missing-char 0 (incl. backtick 0) | invalid-in-math 0 | zero-height 0 | fls 62 / 62 on disk |
| Gates | `check_translation.sh bachelor-2 id`: **PASSED** (Indonesian prose OK 62 files; latin prose: no multi-word finding, the one-word advisory tier read; chemistry twin OK); `gates.sh bachelor-2`: OK; `check_orphan_lines.py`: 0 |
| Structure | Counted over the 62 files against their twins: 372 `exercise`, 31 `problem`, 403 `solution`, 204 `omfigure`, 171 `tikzpicture`, 104 `axis`, 59 `\includegraphics`, 30 `tabular`, 449 `\index`, 999 `\label`, 857 `\item`, 1,066 `% ledger:`, 512 `\ce`, 230 `definition`, 109 `proposition`, 6,188 `\qty`, 616 `\emph`, 315 `\cref`: all equal. `\node` 875 against 864: the explicit label nodes of the supercontinent (ch15) and extinction (ch19) charts, whose figdata tables carry English names |
| numdiff | Seven files differ, each explained: ch02/ch03/ch04 (a figure-label `0:` anchor and cross-volume glosses), ch15 and ch19 (explicit chart nodes), ch17 (the drilling report's comma-thousand feet, 4,158 → 4158, because a comma is a decimal sign in Indonesian), ch28 (two slope-sketch labels shifted, see `!draw`) |
| English sweep | one line: Lyell's title *Principles of Geology* (20:201), a published title, kept |

## Conventions (kept from id Books 1–3, or decided here)

- **Units:** *Ma*/*Ga*/*ka* for every age and duration, in prose and in math
  (`\qty{10}{ka}` for kyr; `\per\Ga` for the siunitx prefix form, as fr);
  `yr` and `\day` kept. Decimal point kept.
- **Coordinates:** latitudes and longitudes *LU/LS/BT/BB* (id Books 1–2; Book 3
  mixed bare U/S/T/B), swept book-wide in Phase C; bearings and the compass
  strings untouched.
- **Terms:** *retas* for dyke, glossed *(dike)* at its definition (Book 2 id
  defines *retas*; **Book 3 id wrote *dike*: a departure from Book 3, chosen
  for Book 2's defined term**); *celah* for rift (*pembentukan celah*,
  *sin-celah*, *pascacelah*, as Book 3 id's *celah benua*); *mikroprobe
  elektron*; *waktu e-folding* kept as the technical term; spaced rock names
  (*batu gamping*, *batu pasir*, *batu lumpur*, *batu bara*, as Book 3 id) and
  *batu dolomit* for dolostone.
- **ch21 subscripts:** `\text{parcel}`/`\text{env}` → `\text{parsel}`/`\text{ling}`
  (8 sites; fr translates them too).
- **Question references:** *pertanyaan~N* throughout (*soal* also names the
  weekend problem).
- **Register:** *kamu*/*-mu*; seven *Anda* slips were corrected; 0 left.
- **Institutions** in prose and credits in Indonesian where the English names an
  institution generically (*Survei Geologi AS*, *Pusat Prediksi Iklim NOAA*,
  *Korps Zeni Angkatan Darat AS*); proper names, datasets and licences exact.
- **Credits:** the English's mixed *(Photograph: …)* / *Photograph X, licence.*
  forms are mirrored as they stand.
- **Figure labels:** two-line labels by `\shortstack` where a translated label
  collided (03:102 legend *tanpa isotop stabil*, ch30 hot-spring label).
- **`east:` → `0:`:** the TikZ label anchor `label={[..]east:…}` at 03:103 is
  read by the Indonesian prose gate as the English word *east*; it is written
  `0:` (the same angle) under `!draw` 101–103 (coordinator ruling).

## `!draw` ranges

02c 373–377 (`\foreach` dust-to-planets labels); 03c 101–103 (Goldschmidt class
labels, `east:` → `0:`); 11c 63–69 (Barrovian zone labels); 15c 346 (two-line
label) and 416–422 (supercontinent chart, explicit nodes, as fr); 16c 333
(two-line column label); 19c 468–470 (extinction chart, explicit nodes);
23c 100, 206 and 24c 156 (`\foreach` panel titles); 28c 368–369 (the slope
sketch's *muka air tanah* and *bidang gelincir* shifted left 0.15 and 0.1 units,
the longer labels touched the column and the frame). No `--force-classes`.

## Dimension scores

| Dimension | /100 | Notes |
|---|---:|---|
| Structural fidelity | 98 | Every census equal except the documented explicit nodes |
| Terminology | 95 | One word per notion across the book from a per-chapter glossary; display-drift list (66 multi-form targets) read, all inflection or distinct terms under one definition |
| Register | 94 | Modern lecture register, *kamu*; a few sentences keep the English's literal shape |
| Typography | 96 | Decimal point, *Ma*/*Ga*/*ka*, *LU/LS/BT/BB*, no thousands comma |
| Fidelity | 95 | Every chapter and solution read against the English; number tokens diffed per file |
| Figures | 94 | Translated figures rendered and viewed chapter by chapter during writing, and the changed pages re-rendered after the last build; not every figure checked one per page by a second reader |
| Links | 95 | Every English target reached, six extra, all right; wrong senses STOPped or protected (*deteksi* outside ch27, two *rasio campuran* sites) |

Mean 95.3, reported as **95**.

## Canon observations (reported, not edited)

- 21 line-broken `\index` keys remain in the English canon of `bachelor-2`
  (gate 5 only checks translations): 02:499, 03:53, 03:157, 06:469, 08:153,
  08:296, 08:636, 10:74, 10:99, 11:91, 12:96, 15:394, 18:249, 21:334, 27:191,
  27:352, 28:197, 28:200, 30:323, 30:495. The id keys are joined.
- Unrounded-path values (sol03:5 4259, sol05:154 58) and the empty-unit `\qty`
  at sol05:197: not reportable under the coordinator's rule, kept.
- Coordinator canon fixes mirrored: sol23 ex. 11 (6.17e12, 5.05e21), 28:493,
  26:533, sol28:104–105 (0.0672), sol31:123 (0.36 %).

## Build

`bash draft/b4-run/tools/build.sh one_earth_and_space_sciences_book_4_university_year_2_id id4` (TeX Live 2026, forced `-g`, memory-capped, into the scratchpad), started after the last edit and the term layer:

`one_earth_and_space_sciences_book_4_university_year_2_id` latexmk exit 0 | pages 518 | errors 0 | undefined 0 | overfull 0 | nullfont 0 | missing-char 0 (incl. backtick 0) | invalid-in-math 0 | zero-height 0 | fls 62 / 62 on disk

Pages re-rendered and viewed after this build (110 dpi): the ch03 Goldschmidt legend (p. 34, `\shortstack`, clear of the B cell), the ch13 Alps profile axis (p. 178, *LU*/*BT*), the ch14 swath profiles (p. 188), the ch15 supercontinent chart (p. 205), the ch19 extinction chart (p. 259), the ch20 Varden log (p. 274), the ch22 Rossby rings (p. 299, *LU*), the ch28 slope sketch (p. 378) and the ch30 burial/events chart (p. 402, the long tick labels fit). All clean. One layout note: p. 177 (ch13) is about two-thirds full because the two-panel figure that follows does not fit below it; the same non-floating `omfigure` behaviour as in the English, left as is.

Phase D fix after the reading: 04:34 *(Buku 2, kelas 12; …* (an id Book 3 habit, where the English says "Book 2, grade 12") → *(volume sekolah menengah atas, tahun terakhir; …*, mirroring this book's English "high-school volume, final year".
