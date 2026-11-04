# Translation score: One Earth and Space Sciences Book 5, Spanish (`es`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 5 (University Year 3, `bachelor-3`) |
| **Language** | Spanish (`es`), peninsular; impersonal *se* in course text, *-se* imperative in exercise stems; terms as in Spanish Books 1–4 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5); finishing pass `claude-sonnet-5-5` |
| **Overall score** | **91 / 100**, sampled: 20 passages, seed 1, not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures sampled |
| **Canon** | English not verified: Book 5 predates the verification pass of `book_style.md`, and solutions were not recomputed. |
| **Tokens** | `all: 585 calls, prompt 3324K + cache read 2141K, output 6752K (thinking 5140K), list price $4.06`. Coordinator (Opus 5.5): at least 17.0M cache read, 1.5M cache write, 116K output in the one transcript measured; a lower bound, and likely the larger share of the cost |
| **Date** | 2026-11-03 |
| **Scope** | 31 chapters + 31 solution files = 62 files, 288 sections |

## Verdict in one line

A complete Spanish Book 5 that reads as near-native in the sample and is structurally identical to English, all gates
green and clean in the log. It is not read sentence by sentence, so its score rests on a sample and it carries the defect
rate that sample shows: about one small language defect per four or five passages, none changing the science.

## What the score rests on

- **Read:** the 20 passages of `sample.py --n 20 --seed 1` against English (`draft/pilot-bachelor-3-es/sample.txt`), and
  the openings of chapters 1, 13 and 24.
- **Figures:** `sample.py --pages` listed 50 pages. **20 of the 50 were rendered and read at 130 dpi**, the richest by
  stroke count: 16, 33, 49, 53, 69, 108, 118, 131, 163, 196, 200, 242, 250, 278, 292, 303, 312, 352, 357, 370. The other 30
  (2, 5, 12, 14, 15, 61, 111, 137, 195, 217, 222, 229, 231, 254, 333, 334, 390-393, 404, 411, 428, 434, 452, 458, 462, 481, 484, 497)
  were rendered at 130 dpi and read in the finishing pass (2026-11-03, `claude-sonnet-5-5`), so all 50 are now read;
  `pdfsweep.py`'s top 150 was read over the whole book.

## Dimension scores (judged from the sample)

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **98** | Gates 1–13 green; line counts equal English by construction; `NUMDIFF` 0 real losses |
| Terminology | **92** | One glossary of 496 defined terms plus about 190 carried from Books 1–4; `lineación` chosen over the earlier editions' `linación` |
| Register / tone | **90** | Impersonal *se* held; a few calques in the sample; *Dése/Dénse* in old spelling left as they are |
| Typography | **93** | ¿…?, guillemets, decimal point, compass O; six *a el / de el* contractions split across lines found by sweep and fixed |
| Fidelity / accuracy | **90** | No loss of meaning in the sample; *casi* for *about* once; solutions not recomputed |
| Figures | **85** | Sampled. Seven figure defects found in 20 pages, all fixed; the rate says the 30 unread pages hold some more |
| Links | **95** | 1358 links on 234 targets against English's 1191 on 216; no English target missing; `FREQ` lines read and correct senses |

## Gates and build

- `bash tools/check_translation.sh bachelor-3 es`: **PASSED**. `bash tools/gates.sh bachelor-3`: **OK**. Linker `--check`: **OK**.
- Final build (TeX Live 2026, `pilot_translation/build.sh`, into `build/`): latexmk 0, **507 pages**; errors 0, undefined
  references 0 (one font-shape warning, the babel-spanish `T1/lmr/bx/sc` baseline), overfull 0, nullfont 0, missing
  characters 0, invalid-in-math 0, zero-height 0, `.fls` 62 / 62 on disk.
- `ENGSWEEP`: 4 lines, all titles and names. `pdfsweep.py` (reference Book 4 `fr`): cognates after the fixes.

## Defects found

**In the sample and openings (fixed):**
- doubled word across a line break (*millones de / de estas*); a sweep found 3 more (ch. 1, 3, 14, 28);
- calques: *veinte veces tan ancho como* (ch. 26), *puede fiarse cada edad* (ch. 13), *casi* for *about* (ch. 6).

**In the figures (fixed):**
- compass W left in a legend and an axis label (ch. 2, six lines);
- a missing article (*por fórmula de MacCullagh*, ch. 3) and *respecto a el plano* (ch. 7);
- *alcance el spin-up* (ch. 19);
- a caption translating the name of the NASA Exoplanet Archive (ch. 28, four lines; it stays a name);
- two labels on or past a boundary (ch. 15, ch. 27).

**Found by the gates or sweeps, not by the model's own checks (fixed):** whole figures left in English in ch. 9, parts of
ch. 13 and 27; `\foreach` labels in ch. 7 and 26; unit words in `\qty` (see below).

## Finishing pass (`claude-sonnet-5-5`, 2026-11-03): what it found and fixed

Rebuilt after the pass (TeX Live 2026, `pilot_translation/build.sh`, into `build/`): latexmk 0, **507 pages**, errors 0, undefined 0, overfull 0,
nullfont 0, missing characters 0, invalid-in-math 0, zero-height 0, `.fls` 62 / 62. `check_translation.sh bachelor-3 es` PASSED, linker `--check` OK,
`gates.sh bachelor-3` OK. The ch. 17 figure was re-rendered after the fix: the two sub-captions no longer touch.
**Score left at 91:** it was judged from a sample and already carried a defect rate of one per four or five passages; this pass found
one systematic class (articles missing from 54 definition sentences) that the sample had not shown, but the score is not raised, and
not lowered either, because the defects are fixed and the 30 newly read pages added only one figure defect.

Sweeps over the whole edition, edits in `parts/` only; line counts, labels, image paths and `\index` counts re-audited equal to English.
- **Wind direction (4 lines):** ch. 20:377 *momento hacia el oeste* for *westerly momentum* (now *momento de los vientos del oeste*);
  ch. 20:414 *viento del este* for *eastward wind* (now *viento hacia el este*); *hacia el O* spelt out as *hacia el oeste* in sol. 03 and sol. 20.
  Every other `easterl|westerl|eastward|westward` line and the lines named in the brief were read against English: correct.
- **Definitions opening on a bare noun (54):** 43 at line start, 4 mid-line (*recocido de trazas*, *subplacado tectónico*, *desenrollado de fase*,
  *avulsión*) and 7 whose term was lowercase (*arrastre basal*, *ajuste isostático glaciar*, *datación Ar/Ar*, *estratificación cruzada hummocky*,
  *intensificación occidental*, *capa límite de Munk*, *escape de Jeans*, *evolución química galáctica*): each now has *El/La/Los* before `\emph{}`;
  inside `\emph{}` only the first letter's case changed. Labels such as *Onlap:* were left bare on purpose.
- **Stranded or doubled article across a line break (4):** ch. 6:28 *La / El*, ch. 10:362 *La / Las*, ch. 22:30 *El / La*, ch. 25:523 *el hacia el este*.
- **English left in a heading (1):** ch. 7:581 `Part I --- The strain.` (found on page 111), now *Parte I --- La deformación.*; a scan for other English
  function words over all es text found nothing else.
- **`\cref` with no article:** none; all 130 references are either after an article or in parentheses, and none has an article of the wrong gender.
- **Compass W:** none in prose or figures; two subscripts in sol. 02 (`t_{i,W}`, `h_W`) now O.
- **Figure pages (30 newly read):** one defect, ch. 17 carbonate-platform figure, sub-captions (a) and (b) printed over each other; both nodes now `align=center` on two lines.
  No other collision or leftover English on the 30 pages. Pages 2 and 5 (front matter) were checked as text.
- **Links:** the new articles changed linker output (1358 to 1359 links); `--unwrap --apply` then `--apply` re-run, `--check` OK.

## `NUMDIFF`: 31 files differ, 0 real losses

Accepted differences, all explained:
- `Year 1`, `Year 2`, `Book N`, `grade N` written as words (*el volumen de primer año*), in nearly every file;
- ch. 14 *at 0* → *con composición cero*;
- ch. 16 *1970s/1980s* → *años setenta y ochenta*; ch. 24 *1990s* ×2 → *años noventa*;
- ch. 25 *1,500* → *1500*;
- sol. 31 *one per cent* → *el 1 por ciento*.

## Conventions recorded

Book 4 `es` conventions kept: Ma/Myr/Gyr/yr byte-identical; `de \qtyrange`; *(libro N, año M)*, *el volumen de primer
año*; `\section{Problema: …}`; *(ilustración generada por IA)*; compass N, E, S, O; A/B on maps; seasons DEF/MAM/JJA/SON.
New this book: `\num{x}~days` becomes `\num{x}~\text{días}` by script (`es.py`, `post.py --units`), including inside math;
*recubrimiento* for overburden; *casquete de hielo*; *geoterma*; *lineación*. The `\omsolutionof` head still prints
*Solución de Ejercicio N*, the open item of every edition.

## Reports on the English

Translated as printed, not fixed. Unit words inside `\qty`/`\unit`: `solutions/20-atmospheric-dynamics.tex:159` (`{days}`);
atoms (ch. 13, sol. 13); cycles (sol. 16:48, 147, 148); neutrons (ch. 30); day (ch. 20, sol. 20); `billion~years`
(sol. 27:101). About nine `\num{x}~days` left inside math spans (ch. 19 `$r^{-1} = \num{4}~days$`, sol. 22, sol. 23), which
print in math italics where the canon rule says `\text{ days}`.
