# Translation score: Earth and Space Sciences Book 5, Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 5 (University Year 3, `bachelor-3`) |
| **Language** | Indonesian (`id`) |
| **Overall score** | **89 / 100**, sampled: 20 passages, seed 1, not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures sampled |
| **Date** | 2026-11-03 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 510 calls; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Canon** | English not verified: Book 5 predates the verification pass of `book_style.md`, and solutions were not recomputed. |
| **Tokens** | `all: 510 calls, prompt 2929K + cache read 2653K, output 7123K (thinking 5676K), list price $4.17`. Coordinator, from its transcript: about 13.5M cache read, 1.48M cache write, 131K out, a lower bound because the context compaction is not in that file |
| **Scope** | 31 chapters + 31 solution files; `frontmatter/image-credits-book5.id.tex`; glossary `sources/GLOSSARY_BOOK_5_ID.md`; term config `tools/term_config/book5_id.py` |

## Verdict

Clear modern lecture Indonesian with occasional calques, in the register of Books 1 to 4. The score is a sample's score. A late
sweep found a whole class that the sample and every gate had missed, words doubled across a line break, so the unread remainder
certainly holds other defects. A sentence-by-sentence pass is what would lift it to the 95 tier.

## Build and gates

- `build/one_earth_and_space_sciences_book_5_university_year_3_id.pdf`: 505 pp. Errors 0, undefined 0, overfull 0, nullfont 0,
  missing characters 0, invalid-in-math 0, zero-height 0, `.fls` 62 / 62 on disk. TeX Live 2026, through `pilot_translation/build.sh`.
- `tools/check_translation.sh bachelor-3 id` and `tools/gates.sh bachelor-3` pass. Linker `--check` clean. Orphan lines 0. Line counts equal English.
- Links: id 1507 on 241 targets, en 1191 on 216; every English target reached. Accepted over-frequency, right sense:
  `thrust-geometry` 60 against 1 (held to ch. 10 by the STOP list), model age in ch. 26, the written-out forms of CMP, GIA and SI.
- `pdfsweep.py`: after the credits were translated, cognates and technical terms only.

## What was read

- Text: 20 passages (seed 1) and the openings of chapters 9, 14 and 28.
- Figures and pages: the 50 pages listed by `sample.py --pages 505`. Those with figures were cropped at 130 dpi, the rest
  looked at in full at 70 to 85 dpi: enough to see a collision or leftover English in a figure, not to proofread the text.
- Credits pages v and vi looked at. The whole wind vocabulary read by grep: 74 lines.

## Defects found and fixed, by class

None of these was caught by a reply check or a gate.

| Class | Count | Example |
|---|---:|---|
| Sentence-opening `\emph` left lowercase | 33 | now "Yang disebut \emph{...}" or capitalised; a capitalised display can lose its link |
| Word doubled or stranded across a line break | 16 | `sejak terbentuk\nterbentuk` (9:513), `cahaya bintangnya.\nbintangnya.` (28:311), `umur plato\numur` (13:226), `gesekan batuan\ngesekan` (9) |
| `-lah` imperative, against the pack's ruling | about 20 | *Hitunglah*, *Ubahlah*, *Taksirlah*, *Tinjaulah* |
| English figure labels left | about 14 | foreach labels 7:141, 26:398; legends 10:345, 29:351; axis labels 27:394, 20:325 |
| Compass W and E for B and T | 16 lines | ch. 2 and solutions, shot points, with $t_{i,B}$, $t_{i,T}$ |
| Overfull lines | 10 | one local `\emergencystretch` per box, one relabelled node |
| Fixed term forms | about 8 | *pelat samudra*, IGRF, Sesar transform Laut Mati, *kolom es* for *inti es*, *horison* |
| Hyphen before `-nya` on an Indonesian word | 8 | *tren-nya*, *persen-nya*, *es-nya* |
| Number lost or misprinted | 2 | 12:557 a `\qty{3}{\percent}` and its clause; 26: 50,000 as 50.000 |
| Sense reversal, easterly and eastward | 1 | 20:414, *angin timur* for a wind blowing eastward, the line `fr`, `es` and `pt` also got wrong |
| Parenthesis stranded at a line end, prints "( x" | 2 | 31:155, 3:440 |
| Literal rendering | 2 | 23:637 *piezometer disaring* for "screened", 27:731 *berapa lapisan ... setebal berapa* |
| Figure collision | 1 | 2:116, the legend hid "waktu resiprokal" |
| Credits page left in English | 1 | the file was still the English stand-in at pdf pp. 5 and 6 |

In the 20 sample passages (60 lines): 2 defects, the literal *disaring* and *tren-nya*. In the three openings: 1 stranded word and 1 verbless
sentence with the wrong term (*Kolom es ... termometer*, 14). The rest came from sweeps.

## `NUMDIFF` differences accepted

4 files. One real loss fixed (ch. 12, the `3`). One misprint fixed (ch. 26, `50\,000`). Accepted: ch. 1 *19:11* written 19.11, the
Indonesian time form; ch. 25 *1,500* written 1500. A line-window check over the book gave 3 hits, all benign (31:971 from a label digit).

## Conventions

Book 4's are kept: *Ma*/*Ga*/*ka* for every age and duration in prose and math, `yr` and `\per\year` as printed in Books 1 to 4, `\ang{20}~LU/LS/BT/BB`,
compass U T S B, decimal point, bare imperative, *kamu*/*-mu* and never *Anda*, no noun before `\cref`, `dari \qtyrange`. Rulings: *tegangan*,
*regangan*, *rasio*, *lelehan*, *umur*, *penanggalan*, *massa jenis*, *keseimbangan* and *kesetimbangan* by sense, *taksiran*, *lempeng*,
*jari-jari*, *sesar dorong*, *lembaran es*, *orogenesis*, *landaian karbonat*. Hyphen kept before `-nya` on foreign words and names only.

## Upgrade path

A sentence-by-sentence pass over all 62 files, then re-score and update the `Model` row.
