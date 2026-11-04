# Wave 1 findings — Book 3 (`bachelor-1`) in nl, es, pt, id (2026-10-27)

What the first wave of the six-language Book 3 run (`sources/TRANSLATION_BOOK_3.md`)
found, written for wave 2 (`hi`, `ar`) and for any later edition. Read it after the run
file and before writing a line. Edition agents ran on `claude-haiku-5-5` at effort high,
one agent per edition at a time, in successive stints; the coordinator ran on
`claude-opus-5-5`.

## 1. English canon edits (all made in English and mirrored in fr; line counts unchanged)

| # | file:line | old | new |
|---|---|---|---|
| 1 | `02-observing-the-sky.tex:77` | `4/1 \textmu m, 6/100 \textmu m,` | `4/1 \unit{\micro m}, 6/100 \unit{\micro m},` (the hi/ar fonts lack µ as `\textmu`) |
| 2 | `solutions/13-rifts-ridges-margins.tex:51–52` | "…follows the smaller constant; the eastern Pacific, with / \num{350} against \num{390}, is an example." | "…follows the smaller constant. The fitted \num{350} of the / chapter is not such a case: it lies within the uncertainty of the parameters." |
| 3 | `14-active-margins.tex:863` | `so that in all \omterm{…}{mantle}` | `so that, in all, \omterm{…}{mantle}` |
| 4 | `10-heat-budget.tex:217` | `\qty{60}{mW.m^{-2}}` (after 2.7 × 25 K/km) | `\qty{70}{mW.m^{-2}}` (2.7 × 25 = 67.5) |
| 5 | `20-erosion-transport.tex:700` | "cleaned in acids of the beryllium made in the air" | "cleaned in acids to remove the beryllium made in the air" |
| 6 | `22-chemical-biogenic-sediments.tex:193` | "between 20 and 30 fathoms, about 40 to \qty{55}{m}" | "… about 37 to \qty{55}{m}" (20 fathoms = 36.6 m; mirrored in fr, nl, es, pt, id, in files and patches; sent to hi/ar) |
| 7 | `29-ocean-circulation.tex:809` | "\qty{173.3}{\sverdrup}, \qty{30}{\percent} more than that long-used value" | "… \qty{39}{\percent} more …" (173.3/125 = 1.39; the source's 30 % is against its own canonical value, not the 125 Sv printed here; mirrored in fr, nl, es, pt, id; sent to hi/ar) |
| 8 | `23-diagenesis-basins.tex:92` | "the sand of the opening has lost more than half its pores" | "the beach sand of the opening paragraph …" (wording: fr, es and pt had read *opening* as an aperture; fixed in fr, es, pt, id; nl was right) |
| 9 | `05-cross-sections.tex:315, 351` | "every borehole crosses the limestone over 180 m"; "Each log gives the same thicknesses" | "a borehole that enters the limestone from above crosses it over"; "B1 and B3 give the same thicknesses" (B2 starts in the limestone on the anticline crest: 100.48 m of it, no shale; reported by the ar reading stint; mirrored in all seven editions, files and patches) |

Wave 2 translates from the current English, so all nine are already in its source (edits 6–9 landed during wave 2 and was sent to both agents).

**Reported and checked, LEFT as correct** (do not re-report): sol11 ex 12(c) −4 mGal;
sol10 problem item 10 5.46; 393√122 → 4340; 849/82 → 10.3; 141.9; ch14 ex 4(b); the ICB
4.5 % (recent studies, compared with PREM's 4.9 % in ex 9); 0.06 %; 4.7 GPa/100 km;
sol11 10(b) −2.80; ch04 9.6°; ch05 46.7°; the Arabia–Nubia pole "in north-eastern
Libya"; ch15 item 24 8.5 cm/yr; ch18 problem item 10 0.07; ch26 sol 6 56010 Pa;
"the physics volumes" in ch26 (the series' name for the sister physics books);
**the ch27 cap figure** — the proof takes the cap south of φ and the figure is drawn,
as its caption says, for the cap north of φ: that is the proposition's second form, on
purpose. Keep the caption faithful. Check a reported slip unrounded and along the
printed path before calling it one.

## 2. Defects that every gate missed (and the two scripts that found them)

The coordinator's checks found English still printed in two editions that passed
`check_translation.sh`, and a doubled half-sentence in a third:

- **Mixed lines.** `es/09:617` repeated a clause that began with the English words
  "inner-core boundary". The twin gate compares whole lines, so a line that is mostly
  translated passes.
- **Figure legends and nodes split by `\\`**: nl ch04 strike/dip legend and lithology
  legend (`\textcolor{…}{\rule…} strike: a horizontal line of the plane;\\`), nl ch21
  node "bars along the flow", nl ch19 "Al or Mg", a nl `inthelab` title, a pt table
  header row made of single English words (ch12:817), a pt sentence fragment (ch18:71).
- **Whole passages never translated** inside a chapter an agent had marked done: nl
  solutions 13 from exercise 12 to the end (53 lines) and the ch21 weekend problem
  (Parts I–IV). The orphan-line gate caught these; check it per chapter, not at the end.

Run these two coordinator scripts on your tree before handing back (they live in the
run scratchpad, `…/scratchpad/coord/`):

- `engsweep.py <lang>` — English function words (the, of the, which, with the, …) in
  the text a reader sees, after stripping comments, labels, cross-reference keys, math
  and drawing code. Control: it fires on 11,716 English lines; fr, es and id give 0.
- `numdiff.py <lang> solutions` (and `numdiff.py <lang> ''` for the course text) — the
  number tokens of each file against its English twin. In the solutions every
  difference must be explained (a number spelt out at a sentence start; clock times
  20.02 in id).

## 3. Overfull boxes: the same sites in every edition

es and pt each started at 20 overfull boxes, nl at 16 and id at 17, mostly at the same
places: the ch12 Euler-vector paragraph (a long inline vector, ~60–73 pt), sol12 (a),
sol15, sol18 vectors, the ch01 proof, sol04/07/10/11; and `[][]` boxes in ch21, ch22,
ch23, ch24 and ch29, which are **figures and tables widened by longer translated node
labels or headers**. Hindi and Arabic will meet the same sites. Every edition cleared
them with `translation_instruction.md` §"Clearing overfull boxes": probe one chapter in
the book's preamble; add short words BEFORE a frozen formula; break a long node label
with `align=center` + `\\`; `\shortstack` table headers; hyphenation hints `\-` in
narrow table cells (a hinted cell loses its link — accepted).

## 4. Link layer

English: 4,650 links on 184 targets. es 4,538 / 187, pt 4,688 / 185, id 4,608 / 186,
nl ~3,840 / 187. Every edition reaches every English target. The extras are
right-sense links English never makes: *parcel* (air parcel), *mean orientation*,
*circumpolar*, *ridge classes*.

Homographs found (each linked dozens of times in the wrong sense before curation):
- *altura* / *hoogte* / *tinggi* = altitude (of a star) and height; *longitud* = length
  and longitude (~120 wrong links in es); *direção* / *dirección* / *richting* /
  *arah* = strike and any direction (~250 in pt); *relevo* / *reliëf* = topography and
  relief; *declinación* = magnetic and celestial; *grupo* / *miembros* = the
  stratigraphic units and a working group's voting members; *helling* (nl) = dip and
  slope; *extensão* = strain and extension; *fluxo* / *flujo* = flux and flow.
- The linker cannot restrict a surface form to a set of chapters: a term that is
  ambiguous across the book stays STOPped and under-linked. Under-linking is
  acceptable; a wrong sense is not.
- Re-running the term layer rewrites all 58 files: **never run it while a build of the
  same edition is queued or running** (an nl build died "File ended while scanning use
  of \qty" with 3,581 undefined).

## 5. Conventions settled in wave 1

- **Booklines** follow the series pattern: *Libro 3: Universidad -- Primer año*,
  *Livro 3: Universidade -- Ano 1*, *Buku 3: Universitas — Tahun 1* (two agents had
  invented their own).
- **Titles of books and papers** stay as English prints them (Smith 1815, Ferrel 1856,
  *Coral Reefs*, …); a gloss in parentheses is allowed. Credits are copied exactly —
  never shorten one to satisfy a gate (an agent had cut "MODIS/LANCE" to "MODIS"); add
  an allow-list entry instead. Place names may be translated (*Tanjung Hatteras*,
  *Laut Tengah*).
- **Units**: id converted every `Myr`/`Gyr` to Ma/Ga, including axis labels, legends
  and `\qty` arguments the first pass missed (ch10, ch13, ch16, sol10). Grep
  `[MG]yr` (excluding comments and "gyre") after the conversion.
- **The ICS chart labels in ch24 come from figdata** and print English: replace them
  with explicit nodes under a per-range `!draw`, as fr does.
- The orphan-line gate now has a per-language allow-list (`ALLOWED_ORPHAN_LINES`,
  added for the Smith title).

## 6. How the agents worked (for the coordinator of a later run)

- A resumed agent starts with a full context and does about one chapter; a **fresh
  agent per stint**, reading only its PROGRESS file and a few run-file sections, is the
  shape that works (user ruling).
- Telling an agent to "stop near its context limit" made it stop after one or two
  chapters. Context is compacted automatically; the brief must say so, and say to stop
  only when the work is done.
- Builds queue on one machine-wide lock; a build started before an edit, or while the
  linker rewrites files, is worthless.
- Every edition's first "finished" hand-back still had English in it, a self-score of
  92–93, and 16–20 overfull boxes. Budget a finishing stint and a quality stint after
  the translation stints.
