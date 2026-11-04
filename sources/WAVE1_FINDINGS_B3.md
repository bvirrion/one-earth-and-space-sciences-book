# Findings of the first Book 3 translation (French) — for the other six languages

Written by the coordinator on 2026-10-26, when the French edition of Book 3
(University Year 1, `bachelor-1`) closed. It follows `TRANSLATION_BOOK_3_FR.md`
(the run file). Every later Book 3 edition (`nl`, `es`, `pt`, `hi`, `ar`, `id`)
**must read this file before starting**, and the run file for that edition should
be derived from `TRANSLATION_BOOK_3_FR.md`.

## Result

French: 29 chapters + 29 solutions = 58 files, one agent, self-score 96/100,
**496 pages** (English 475), forced TeX Live 2026 build 0 / 0 / 0, nullfont 0,
`.fls` 58, every gate green. Links: **4,468 on 185 targets** against English's
**4,650 on 184** (after the fixes below); every English target is reached, plus
*parcel* (French writes *parcelle d'air*, English never links "parcel").

## 1. English-canon changes made for this run

Line counts never changed. Any language that starts now inherits them.

| Where | Change |
|---|---|
| `15-hotspots` 48, 349, 590, 608, 609; `12-plate-kinematics` 721, 929; `solutions/12` 239; `05-cross-sections` 513; `image-credits-book3` | TeX accent escapes → UTF-8 (`Réunion`, `Paraná`, `Höfn`, `PawełS`, `Michel-Lévy`, `Mohorovičić`, `Þingvellir`, `Galápagos`) |
| `20-erosion-transport` 749, 866; `solutions/20` 5; `21-clastic-sediments` 1196, 1203; `solutions/10` 56, 57 | `\qty{365.25}{days}` etc. → `\num{365.25}~days` (words out of unit arguments) |
| `01-spherical-astronomy` 556; `solutions/20` 124; `solutions/21` 162 | the same inside math: `\num{…}\text{ days}`, `\text{ years}` |
| `solutions/02` l. 72 | `e^{-0.340} = 0.711` → **0.712** (0.7118) |
| `solutions/06` l. 47 | `p = 9.3°` → **9.2°** (arctan 0.1628 = 9.248°; a double rounding of 9.25) |
| `solutions/07` exercise 11 | Al 1.545 → **1.544** (1.5444); `2.453 + 1.544 = 3.997`; large site 1.010 → **1.009**; Al − 1 = **0.544**; An = 100×0.544/1.009 |
| `tools/term_config/book3_en.py` | protects for *voting members* and *members not voting* (they linked to the lithostratigraphic *member*; English 4,654 → 4,650 links) |
| `styles/oneearth.sty` | `\crefname{table}` (conditional on `\omnameTable`), and the `\year` unit symbol (conditional on `\omunitYear`) |

Reported by the agent and **checked and left**: 464.1 m in `solutions/05` (100/tan 12.16°
= 464.09, right unrounded), 58.5 km/Myr in `solutions/24` (right unrounded;
58.1 along the rounded path), −1.7 % in `solutions/09` (−1.749 unrounded), and the
forward reference "question 19" in `solutions/24` item 17 (deliberate: question 19
gives the 28 thousand years).

## 2. What every later edition must do that French needed

1. **Tables.** Book 3 is the first volume with numbered tables (12 `table`
   environments, 27 `\cref{tab:…}`). cleveref printed its English "table" and
   babel-french's own `\tablename` is *Table*, set again at `\begin{document}`.
   `styles/lang/fr.tex` now carries `\omnameTable`/`\omnameTables` and
   `\renewcommand{\tablename}` plus an `\addto\captionsfrench` hook. **The other six
   `styles/lang/<lang>.tex` need the same two strings** (and, for each babel
   language, a check of its own caption name and separator). Render one caption
   and one reference per edition.
2. **Time units — decide once, before anyone writes.** The run file told the
   French agent to freeze `Myr`/`yr`/`Gyr` inside math spans, which left a book
   that printed *Ma* in prose and *Myr* in formulas (166 lines). The coordinator
   then converted every unit argument, in prose and in math, with a script (a
   direct edit of the written tree; the `math` census runs only inside `id_apply`).
   `\year` can print a language's own year symbol through `\omunitYear`. For Spanish,
   Portuguese and Dutch, which keep English's Ma/Myr split in Books 1–2, say so in
   the brief; for Indonesian and French, convert after the write. **A rewrite of
   unit arguments by regex needs the lookbehind AFTER the optional backslash**: the
   first attempt turned `\per\Myr` into `\per\\Ma` and stopped the build, because
   `(?<![A-Za-z])\\?Myr` fails at the backslash (it follows the `r` of `\per`) and
   matches at the `M`. Grep for `\\\\(Ma|Ga|year)` after any such pass.
3. **Visible text outside the `.tex`**, all listed with lines in
   `TRANSLATION_BOOK_3_FR.md`: nine `\foreach` lists, 50 legend sites and the
   tick-label keys, `symbolic x coords={buried, surface}` (ch. 23) and **ten
   `symbolic y coords` keys in ch. 25** that are never printed (keep them; the
   French gate needed an allow-list entry for them), and the ICS chart of ch. 24
   whose era, period and event names come from `.dat` files (the agent replaced
   `meta=name` plots by explicit nodes under `!draw`).
4. **Gate 9 and siunitx options.** `\qty[text-series-to-math=true]{1660}{km}`
   put "text series math true" into the duplicate-line tier. Fixed in
   `check_latin_prose.py` (lenient). Whoever edits `check_arabic_prose.py`,
   `check_hindi_prose.py` or the Indonesian gate should check the same shape.
5. **`nullfont` is 0 for Book 3** (no blank-line map tables), so any nullfont line
   in any edition is a real defect.
6. **Elision at line end** reached 89 sites in the French first draft; Dutch (`'s`,
   `'t`), Indonesian and the others have far fewer. Run the three line-edge greps
   after the last file.

## 3. Link-layer findings

* **French-only wrong senses** (now protected in `book3_fr.py`): *groupe de travail*
  and *le groupe a proposé* linked to the lithostratigraphic *group*; *membres
  votants* to *member*. English already protects *working group* and *the group
  proposed*; the same two translations in another language will collide the same way.
* **English wrong sense found by translating**: *voting members*. The French edition
  found it (rendered page of the 2024 box); fixed in `book3_en.py`.
* **Capitalised-harvest audit of Book 3**: 25 definitions open with a capitalised
  term (*Olivine, Diagenesis, Compaction, Upwelling* …). All lowercase uses either
  link or are deliberately unlinked; no `EXTRA` was needed in English.
* **Do not copy `book2_fr.py`**: the French agent re-derived every protect; the
  frequency and chapter-set censuses flagged only sites that read correctly.
* A late `--apply` can leave a link span crossing a line break (*linéation
  d'intersection*): harmless for the build, but re-run the line-edge sweeps.

## 4. Process findings for the coordinator

* **Do not edit style, `fr.tex` or chapter files while a build runs.** A
  verification build started before my unit pass read some files before and some
  after, died on a half-converted file, and its numbers meant nothing. Edit, then
  build.
* The French agent worked for ~3 h 10 min and 826 tool calls; the machine was never
  loaded by more than one build at a time (the wrapper's lock).
* The coordinator's four preparatory audits (accent escapes, `\qty` words,
  capitalised definitions, macro inventory against Books 1–2) found nothing the
  agent had to fix, which is what they are for; the one defect class they missed
  was the table caption label, found by reading the rendered caption of the probe
  build ("Table 7.1 –" in a French book). **Read one rendered page of every new
  environment in the probe build, before the run.**
