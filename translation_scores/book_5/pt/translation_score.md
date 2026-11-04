# Translation score: One Earth and Space Sciences Book 5, Brazilian Portuguese (`pt`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 5 (University Year 3, `bachelor-3`) |
| **Language** | Brazilian Portuguese (`pt`); impersonal *se* in course text, *você* imperative in exercises; terms as in Portuguese Books 1–4 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5); finishing pass `claude-sonnet-5-5` |
| **Overall score** | **90 / 100**, sampled: 20 passages, seed 1, not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures sampled |
| **Canon** | English not verified: Book 5 predates the verification pass of `book_style.md`, and solutions were not recomputed. |
| **Tokens** | `all: 626 calls, prompt 3843K + cache read 2384K, output 7144K (thinking 5161K), list price $4.36`. Coordinator (Opus 5.5), from its transcript: 16.0M cache read, 1.35M cache write, 132K output, 188 tool calls |
| **Date** | 2026-11-03 |
| **Scope** | 31 chapters + 31 solution files = 62 files, 288 sections |

## Verdict in one line

A complete Portuguese Book 5 that reads natively in the sample and is structurally identical to English, all gates green
and clean in the log. It was not read sentence by sentence, so it carries the defect rate its sample shows: small language
and terminology slips, about one per four passages before the sweeps, none changing the science.

## What the score rests on

- **Read:** the 20 passages of `sample.py --n 20 --seed 1` against English (`draft/pilot-bachelor-3-pt/sample.txt`), and the
  openings of chapters 1, 16 and 29.
- **Figures:** `sample.py --pages` listed 50 pages. **All 50 were rendered and read**: the 35 that carry figures or
  solutions at 130 dpi, the 15 with neither at 90 dpi. Pages come from the build before the last edits, so they may be off by one.
  The edited figures (ch. 7, 17, 18, 20, 22, 26, 27, 30) were read again after the fixes. `pdfsweep.py` was read over the whole book.

## Finishing pass (`claude-sonnet-5-5`, 2026-11-03): what it found and fixed

Sweeps over the whole edition, edits in `parts/` only; line counts, labels, image paths and `\index` counts re-audited equal to English.
- **Wind direction (7 lines):** ch. 20:414 *vento de leste* for *eastward wind* (now *vento para leste*); ch. 20:210, 224, 237 *em um oeste*
  (now *em um vento de oeste*); ch. 3:317 and ch. 19:125 compass letters in prose (*para O*, *para L*) spelt out as *para oeste*, *para leste*.
  Every other `easterl|westerl|eastward|westward` line and the lines named in the brief were read against English: correct.
- **Definitions opening on a bare noun (50):** 46 at line start and 4 mid-line (*recozimento de traços*, *underplating tectônico*, *avulsão*,
  *desprendimento de icebergs*): each now has *O/A/Os* before `\emph{}`; only the first letter's case changed inside it.
- **Stranded article across a line break (1):** sol. 02:15 *O / A aproximação*. No other doubled word or uncontracted *de/em/por + o/a*
  survived a scan of the comment-stripped text, with math blanked and every hit read.
- **English left in a heading (1):** ch. 5:566 `Part II --- Subsidence.` (now *Parte II --- A subsidência.*).
- **`\cref` with no article:** none; none has an article of the wrong gender.
- **Compass letters:** no W in prose or figures; four subscripts in sol. 02 (`t_{i,W}`, `t_{i,E}`, `h_W`, `h_E`) now O and L.
- **Figure:** ch. 17 carbonate-platform sub-captions (a) and (b) were as wide as their panels and touched; both nodes now wrap to two lines
  (re-rendered and read after the build).
- **Links:** the new articles changed linker output (1343 to 1348 links); `--unwrap --apply`, `--apply` re-run, `--check` OK.

Rebuilt after the pass (TeX Live 2026, `pilot_translation/build.sh`, into `build/`): latexmk 0, **504 pages**, errors 0, undefined 0, overfull 0,
nullfont 0, missing characters 0, invalid-in-math 0, zero-height 0, `.fls` 62 / 62. `check_translation.sh bachelor-3 pt` PASSED, linker `--check` OK,
`gates.sh bachelor-3` OK. **Score left unchanged:** the pass fixed what it found and the sample-based dimensions are untouched.

## Dimension scores (judged from the sample)

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **98** | Gates green; line counts equal English by construction; labels, images and ledger ids equal English; 8 answer-number slips fixed |
| Terminology | **89** | Glossary of 496 defined terms plus recall lines; three drifts from Books 1–4 in the sample, each fixed by a book-wide sweep |
| Register / tone | **90** | Impersonal *se* held; some calques remain, such as *uma lag* in ch. 17 |
| Typography | **92** | Decimal point, compass N/S/L/O, quotes; about 56 literal `*word*` asterisks found by grep and fixed |
| Fidelity / accuracy | **90** | No loss of meaning in the sample; solutions not recomputed |
| Figures | **88** | 50 of 50 listed pages read; figure defects below fixed. The rest of the book's figures were not read |
| Links | **95** | 1343 links on 233 targets against English's 1191 on 216; no English target missing |

## Gates and build

- `bash tools/check_translation.sh bachelor-3 pt`: **PASSED**. `bash tools/gates.sh bachelor-3`: **OK**. Linker `--check`: **OK**.
  `check_orphan_lines.py`: 0.
- Final build (TeX Live 2026, `pilot_translation/build.sh`, into `build/`): latexmk 0, **504 pages**; errors 0, undefined
  references 0, overfull 0, nullfont 0, missing characters 0, invalid-in-math 0, zero-height 0, `.fls` 62 / 62 on disk. No
  source file is newer than the PDF.

## Defects found (all fixed)

**In the sample and openings:** *$\beta$-plano* against the glossary's *plano $\beta$*; *lherzolita* against the earlier
*lherzolito*; *idades do gelo* for *eras glaciais*; *milhões de dessas ondas*.

**On the figure pages:**
- two labels colliding (ch. 17 box, ch. 18 next panel), and two overfull lines from a longer label and a math line;
- a definition without its article at the head of a sentence (six sites);
- *contra Teorema 1.3*; *a massa fração de fundido*; *pulverização catódica* for planetary sputtering;
- Title Case in four chapter titles, and solution heads differing from their chapter titles (six files);
- *3.º ano* and *2.º ano* for the book's *12º/11º ano* (ch. 6).

**Found by my sweeps, invisible to the gates and to `post.py`:**
- about 56 literal `*word*` from Markdown italics in my own pack and glossary;
- seven uncontracted or doubled forms across line breaks (*em / o nível*, *por o dobro*, *os de / os condritos*);
- real English on nodes and `\foreach` labels (ch. 7, 26 and others), which the reply checks passed;
- `=` on lines of prose, so a kept-English paragraph passed as "unchanged" (ch. 12, 13; sol. 26).

**Coordinator slip:** a terminology sweep (*kilonova* → *quilonova*) also changed an image path and a ledger id in ch. 30. The
ledger gate caught the id; I found the path by reading the same lines, and an id audit against English now shows 0 differences.

## `NUMDIFF`: 30 files differ, 8 real losses fixed

Real losses: bold answer numbers `\textbf{N.}` dropped at sol. 03:136, 07:130,133,141, 10:108, 26:126, and duplicated at
sol. 02:177,183. Accepted differences, all explained:
- `Year N` written *primeiro/segundo/terceiro ano* (111 lines), in nearly every file;
- 19:11 → 19h11; 1,500 → 1500 (ch. 25); *14.º IGRF* in ch. 4;
- number moved across a line by the reflow: ch. 7:248, 11:12, 12:22, 21:120, 27:32.

## Conventions recorded

Book 4 `pt` conventions kept: Ma/Myr/Gyr/yr as in English; *(livro N, ano M)*, *volume do primeiro ano*, *10º/11º/12º ano*;
compass N, S, L, O; `\cref` articles by printed noun (feminine prop, def, sec, tab; masculine ch, thm, exo, ex, pb). New
this book: *geoterma*, *deslocação* for dislocation, *lherzolito* (masc.), *plano $\beta$*, *quilonova*, *eras glaciais*.
`\omsolutionof` still prints *Solução de Exercício N* (`styles/lang/pt.tex`), the open item of every edition.

## English: words in units, translated in this edition and reported

Line numbers as in English. Bare in math: `\num{x}~years$`, `~days$` at sol. 22:21,62,64,99,100,150, ch. 19:782, sol.
23:109,188. Inside `\qty`: sol. 27:71,101 `billion~years`; sol. 20:160 `days`; sol. 20:146 `day^{-1}`; ch. 13:538,682,826 and
sol. 13:60,65,69 `atoms.g^{-1}`; ch. 30:584 `neutrons.cm^{-3}`; sol. 16:48,147,148 `cycles/…`.
