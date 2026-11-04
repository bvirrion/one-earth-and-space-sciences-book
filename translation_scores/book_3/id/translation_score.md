# Translation score — One Earth and Space Sciences Book 3 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 3 (University Year 1, `bachelor-1`) |
| **Language** | Indonesian (`id`), Bahasa Indonesia modern lecture register |
| **Overall score** | **95 / 100** (ship threshold ≥ 95 — met; see "Open items") |
| **Date** | 2026-10-27 (stint 3, the final reading: ch23–29 course text and sol18–29) |
| **Model** | `claude-haiku-5-5` (Haiku 5.5), effort high; coordinator `claude-opus-5-5` |
| **Scope** | 58 files (29 chapters + 29 solution twins) written through `tools/id_apply.py` line-range patches over the English twin; `frontmatter/image-credits-book3.id.tex` (every credit, author, dataset and licence kept exactly; frame and descriptions translated); `tools/term_config/book3_id.py`; the defined-term link layer; this score |

## Verdict in one line

A complete Indonesian Book 3 that reads as one Indonesian first-year course in
the Earth and space sciences. Every chapter and every solution has now been read
side by side with its English twin, from ch01 to ch29 and sol01 to sol29. The
final reading of this stint found and fixed a small number of real defects:
two wrong-sense term links (a geological-map *kontak* on grain contacts, and
*penurunan* read as a basin subsidence where the text means a sea-level fall),
one duplicated pgfplots option, one garbled phrase, one dropped problem heading
in the solutions, and about twenty meaning and calque fixes in ch23–28. None of
the fixes changed a number, a label, a reference or the mathematics.

## Measured

| Measure | Value |
|---|---|
| Files | 58 (`.fls` = 58 on disk) |
| Pages | 495 (English 475) |
| Links | 4,599 `\omterm` inserted by the term layer (last run: `--unwrap --apply` removed 3,904 and inserted 4,599; then `--apply`); dry run after the last edit: **links to insert: 0** (688 linkable terms, 13 stop-listed) |
| Build | `one_earth_and_space_sciences_book_3_university_year_1_id rc=0 pages 495 | errors 0 | undefined 0 | overfull 0 | nullfont 0 | missing-char(non-backtick) 0 | invalid-in-math 0 | fls 58 | zero-height 0` (build `id-16`) |
| Gates | `check_translation.sh bachelor-1 id`: **PASSED**; `engsweep.py id`: empty; `[MG]yr` grep outside comments and "gyre": empty |
| numdiff (`solutions`) | one file differs: `01-spherical-astronomy`. The English writes the clock times 20:02 and 23:57; the Indonesian writes 20.02 and 23.57, which is the Indonesian clock notation (*pukul 20.02*). No spelled-out number differs |

## Corrections made in stint 3

Every change went into the chapter's `id_apply` patch; `cmp.py` = TOTAL 0 for
ch18, 23, 24, 25, 26, 28 and 29 after the last write, and the other chapters
were not touched in this stint.

- **ch23:**
  - the duplicated pgfplots option `xmin=0, xmax=140, …` (the English line
    copied in front of the translated range) removed from the figure (b) axis;
  - *dipicu* ("triggered") → *lebih mudah terjadi* (the English "favoured");
  - *yang makin dalam kelaparan* → *yang makin dalam mengalami kekurangan
    sedimen* (a starved basin);
  - *lembaran es yang terdasar* → *lembaran es darat* (grounded ice);
  - *digaris tepinya* → *dibatasi tepinya*;
  - term config: *kontak* of grain contacts and *penurunan* of a sea-level fall
    (*penurunan muka laut*, *penurunan glasial*) are protected from the links
    they had picked up (`book3_id.py`, `EXTRA_PROTECT`).
- **ch24:** *batuan tumbuk ke atmosfer* → *batuan yang hancur menjadi serbuk*
  (pulverised rock); *lempung batu kapur* → *lempung pada batu kapur*.
- **ch25:** ex. 1 *Berapa waktu paruh umurnya?* → *Berapa banyak waktu paruh
  umurnya?* (how many half-lives old); ex. 12 *yang menjadi kekurangan* →
  *selisih … terhadap* (the calque "fall short").
- **ch26:** *sondir* (a geotechnical word, cone penetration test) → *profil* at
  all 13 sites, and *oleh sondir* → *oleh radiosonde*; two problem sentences
  that said *pengukuran* for the CTD cast rewritten (*berada pada pengukuran?*
  → *termasuk pada profil ini?*; *dalam pengukuran air* → *pada profil ini
  terdapat air*).
- **ch28:** the Alaska caption *seperti udara sebuah depresi* → *seperti yang
  dilakukan udara dalam depresi* (calque).
- **ch29:** the introduction's garbled *tempat-tempat tempat sebagian di
  antaranya* → *lokasi-lokasi tempat sebagian di antaranya*.
- **ch27:** read in full, no fix.
- **sol24:** the English problem heading `\subsection*{Problem: Correlating three
  sections across a basin}` had been dropped from the Indonesian solutions file;
  restored as `\subsection*{Masalah: mengorelasikan tiga penampang melintasi
  sebuah cekungan}`.
- **sol18:** read in full, no fix. **sol19–23, sol25–29:** read in full, no fix.

## Read coverage in this stint

- ch23: full side-by-side read (prose, definitions, figure captions and axes,
  exercises 1–12, the problem with all four parts).
- ch24: full read (prose, definitions, tables, the GSSP and chart figures,
  the 2026 and 2024 boxes, exercises 1–12, the problem with parts I–IV).
- ch25: full read (decay systems, isochrons, K–Ar, U–Pb, radiocarbon, closure
  temperatures, bracketing ages, exercises 1–12, the problem with parts I–IV).
- ch26: full read (atmosphere, potential temperature, stability, ocean layers,
  equation of state, T–S diagrams and water masses, exercises 1–12, the problem).
- ch27: full read (insolation, the radiative budget, the reanalysis figures,
  transport, latent heat, the surface budget, exercises 1–12, the problem); all
  numbers in the exercises and the problem checked against the English.
- ch28: full read (forces, geostrophic wind, friction, depressions, three cells,
  angular momentum, jets, ITCZ, Walker, exercises 1–12, the problem with parts
  I–IV).
- ch29: full read (wind stress, gyres, Ekman transport and spiral, upwelling,
  western boundary currents, Stommel, the overturning circulation, exercises
  1–12, the problem with parts I–IV).
- sol18–29: every solution and every problem item read against the English twin.
- Earlier stints: ch01–22 and sol01–17 (see the stint-2 record in the progress
  log of the work directory).

## Dimension scores

| Dimension | /100 | Notes |
|---|---:|---|
| Structural fidelity | 98 | Every census passes; the two structural defects found on reading (a duplicated option inside a `!draw` range, a dropped heading in the solutions) were fixed |
| Terminology | 95 | Density is *massa jenis* throughout; *tahap*, *seri*, *sistem* and *gyre* are used consistently; kept English terms per coordinator ruling |
| Register | 94 | Modern lecture register; a few calques remain where the English is itself literal |
| Typography | 95 | Decimal point kept; clock times written 20.02 (Indonesian notation); Ma/Ga units |
| Fidelity | 95 | Chapters 1–29 and solutions 1–29 read against the English; meaning drift fixed in ch23–29; no further meaning defect found |
| Figures | 95 | Figure captions and axis labels read in every chapter; the one defect found (the duplicated axis option) fixed |
| Links | 94 | 4,599 links; every target reached; wrong-sense links (*kontak*, *penurunan*) protected; optical *relief* under-linked (accepted) |

Mean of the seven dimensions: 95.1, reported as **95**.

## Open items

1. **Optical relief** (ch08) under-linked: 7 links against English's 35
   (coordinator ruling 3, accepted).
2. **Kept English terms and acronyms**, as ruled: *forearc*, *rake*, *foreset*,
   *tropopause*, *AAIW*, *AABW*, *CCD*, *ICB*, *CMB*, *IntCal20*, *Moho*,
   *Coriolis*, *Basin and Range*, *gyre*. Proper names stay.
3. **English-canon observations** (not changed here; for the coordinator):
   - ch23 "the sand of the opening has lost more than half its pores": the
     phrase *the opening* is unclear in English, and the Indonesian *pasir
     pembukaan* copies it;
   - *parcel* is linked zero times in English; three *mean orientation*
     occurrences are unlinked in English but linked in id (ruled not a defect).
4. **Gates that did not catch what a reader found.** Two defects of this stint
   passed every gate: a duplicated pgfplots option inside a `!draw` range
   (ch23), and a dropped `\subsection*` in a solutions file (sol24). The
   solution-heading census and a duplicate-axis-option census would have caught
   them. This is a tooling note for the coordinator; the shared tools were not
   edited.
5. **Register.** A few sentences keep the English's literal shape (for example
   the calques left in the solution prose of ch19 and ch25). They are readable
   and natural enough to ship; they are the first place to look in a later
   polish pass.

## Build

`bash …/build.sh one_earth_and_space_sciences_book_3_university_year_1_id id-16`
(forced `-g`, TeX Live 2026, memory-capped), after the last edit and the term
layer:

`one_earth_and_space_sciences_book_3_university_year_1_id rc=0 pages 495 | errors 0 | undefined 0 | overfull 0 | nullfont 0 | missing-char(non-backtick) 0 | invalid-in-math 0 | fls 58 | zero-height 0` (build `id-16`)

## Coordinator verification (claude-opus-5-5, 2026-10-27)

Accepted at 95 after the coordinator's own checks:

- Canon edits mirrored in the files and in `patches/`: ch22 Darwin box *sekitar 37 hingga 55 m* (edit 6), ch29 *39 % lebih banyak* (edit 7), ch23 *pasir pantai di awal bab* (edit 8, the English "the sand of the opening" made explicit). All three print in the PDF.
- Earlier coordinator rulings: density is *massa jenis* (*rapat* the adjective only), units Ma/Ga throughout, the kept English terms and the *optical relief* under-linking are not deductions.

Checks: `numdiff` over the 29 solution files differs only in the clock times of solution 1 (20.02, 23.57, Indonesian notation). The English-function-word sweep is empty, and the PDF-text sweep shows no word that is not in the verified id-7 sweep. Final build (TeX Live 2026, forced, `coord-id-1`): 495 pp | 0 errors | 0 undefined | 0 overfull | nullfont 0 | missing-char 0 | invalid-in-math 0 | zero-height 0 | 58 translated files read. `check_translation.sh bachelor-1 id` PASSED, linker dry run 0.
