# Wave 2 findings and closing record — Earth & space Book 2 (hi, ar, id)

Written by the coordinator on 2026-10-26, when the run closed. It follows
`TRANSLATION_BOOK_2.md` (the run file) and `WAVE1_FINDINGS_B2.md` (wave 1).
The coordinator's scratch log of canon edits was lost when the machine
restarted (`/tmp` cleared). This file is now the only record of what changed
after wave 1, so it lists every edit.

## Result

All seven editions are delivered:

- one agent each, in two waves (fr/nl/es/pt, then hi/ar/id);
- each verified on the coordinator's own forced build in a fresh output
  directory, then rebuilt once more after the last edit (see "Final check");
- each with every gate green for grades 10–12, linker `--check` clean, and a
  linker dry run of 0.

| Edition | Pages | Links | Targets | Score |
|---|---:|---:|---:|---:|
| `en` | 362 | 2,208 | 136 | — |
| `fr` | 380 | 2,263 | 138 | 96 |
| `nl` | 374 | 2,094 | 136 | 96 |
| `es` | 375 | 2,168 | 138 | 96 |
| `pt` | 373 | 2,249 | 137 | 96 |
| `hi` | 345 | 2,250 | 138 | 96 |
| `ar` | 334 | 2,137 | 137 | 95 |
| `id` | 379 | 2,345 | 139 | 96 |

Every edition now reaches every English target. Dutch reached 135 until the
closing pass (see §2). The extra targets are legitimate:

- *Saffir–Simpson scale*: English uses the term only inside its own
  definition. Its other uses say "categories", and some translations say
  "scale".
- *magnetic anomaly*: the figure caption (see `WAVE1_FINDINGS_B2.md` §2).

## 1. English-canon fixes after wave 1

Each was made in English and mirrored into every edition, with line counts
unchanged.

| File | Fix | Found by |
|---|---|---|
| `grade-11/solutions/08` answer 16 | "Between the two: a few years, at the long end of a lava flow, in the months-to-years of shallow intrusions" → "About 950 days, some 2.6 years: far longer than a lava flow, within the months to years of shallow intrusions". Answer 15 gives about 950 days for the sill centre, which lies inside the intrusion range, not between the two ranges | hi |
| `grade-11/01` l.192 | "Motonari" → "**Motonori** Matuyama" (松山基範). The hi and ar editions already had it right | ar |
| `grade-12/02` fold-shortening chart | "Varden: 2.2 %" (anchor south east at 12,4) ran past x = 0 and was clipped to "2.2 %". Now `anchor=south, align=center` at (12,6), on two lines. That put "Varden:" beside "13 %", so the 13 % label moved to `anchor=west` at (32,10). Rendered and checked. Each edition keeps its own Varden wording in the same node | ar |

Checked and left as they are:

- g11/01 ex. 15 item 2, "how far from the axis would floor of that age lie":
  readable, and every edition carries the intended sense (floor 10 million
  years old).
- "English never links the Saffir–Simpson scale": see above.
- The g12/10 problem has 19 questions: an observation, not a defect.

## 2. Link-layer changes at closing

- **hi**: a protect for the parenthesised gloss of Vine and Matthews's paper
  title (g11/01:268). It linked to *magnetic anomaly*, and a title never
  links. Links went from 2,251 to 2,250.
- **nl**: EXTRA "trek van de wegzakkende slab" and "slabtrek" → *slab pull*.
  This is the capital-harvest trap again: the definition opens on
  `\emph{Slabtrek}`. The g11 solutions/06 phrase is the one English links
  through its own EXTRA, "pull of the sinking slab". The link count stays
  2,094, because the phrase linked to *slab* before.

## 3. Arabic: right-to-left findings (new in Book 2)

The Arabic agent found these on its rendered pages. The coordinator then
re-checked both Arabic editions after the run (§3a).

- **A leading multi-character run reverses its glyphs.** This happens at the
  start of `\foreignlanguage{arabic}{…}`, of a pgfplots axis label or title,
  of a tick label and of a legend entry: 15 → 51, PETM → MTEP, 1996 → 6991.
  The fix is `\mbox{\textdir TLT …}`, the same as `\omve`.
- **A table cell that starts with a Latin word is laid out left to right.**
  The fix is the same, with one box per number in a range.
- **A ")" at the end of Arabic text inside a node or axis label stays
  unmirrored**, and "(III)" renders as ")III(". A second label line holding
  only "(°C)" mirrors its parentheses.
- **Punctuation lands on the wrong side.** A plain node line ending in Arabic
  punctuation puts it there; wrap the line in `\foreignlanguage{arabic}`.
- **Prose needs wraps.** Number tuples such as "(0.90, 0.71806)" need
  `\babelsublr`, and numbers with thin spaces need `\num{}`.
- **Intervals.** g12/10 writes intervals as `$[x \text{, } y]$`, because math
  runs left to right.
- **Names in Latin script are transliterated.** Ship, journal and paper names
  are written in Arabic letters, because the Arabic prose gate rejects Latin
  even inside `\babelsublr`.
- **A tcolorbox label can be lost at a page break.** The g10/07 weekend
  problem lost `pb:g10:soil-formation:1` (2 undefined references): tcolorbox
  dropped a zero-height first part ("Discard zero height first box part")
  with the label in it. The label now follows the problem's opening photo. No
  build log of any Book 1 or Book 2 edition shows the message now; grep for it
  in every new build.

## 3a. The leading-run reversal: probe, rule and sweep (2026-10-26, after the run)

A probe built with the series' own Arabic preamble tested each context once.
Each case started with a number or Latin word.

| Context | Result |
|---|---|
| Single-line node, tick label or legend entry inside `\foreignlanguage{arabic}{…}` | **reversed**: 23 → 32, PETM → MTEP |
| The same text without `\foreignlanguage` | correct |
| `align=center` node without `text width` | **reversed**: it is still one box |
| Node with `text width` | correct: it is set as a paragraph |
| Axis label or title starting with a number or Latin word | **reversed**, even a bare number: 1996 → 6991 |
| `\ang{73}` or `\qty{73}{\degree}` first, then Arabic | **broken**: "°73" |
| `$60^\circ$` or `\num{10000}` first | correct: math is boxed |

The fix is `\mbox{\textdir TLT …}` around the leading run only, never around
the Arabic word after it. Boxing "25 مارس" whole would lay the month out left
to right. `\babelsublr` is not enough here.

**Sweep.** A script (in the coordinator's scratchpad) scanned both editions
for those contexts. Every flagged site was rendered, and each table cell was
checked by `pdftotext -bbox` word positions.

- **Book 1 Arabic, 9 sites fixed:**
  - g7/05, the calendar of Earth's history: "52 مارس", "81 نوفمبر" and
    "62 ديسمبر" printed for 25 March, 18 November and 26 December. The 11
    February label was boxed too, for consistency.
  - g8/02, the wind-belt latitudes: four `\ang` labels printed "°60 ش".
  - g9/01, a table cell: `\qty{3.2}{mm} في السنة` printed "mm 3.2".
  - Checked and left alone: the g6/04 cell "6371 (المركز)" was already right,
    and the g6/01 pressure cards are set with `text width`.
- **Book 2 Arabic, 4 sites the agent missed:** g10/03, two legend entries and
  two nodes with `\qty{N}{\degree} ش`, printed "°30 ش" and "°35 ش". The
  `\num{10000} سنة` tick label in g10/09 was correct.
- **Both editions were rebuilt after the fixes:** Book 1 at 303 pp, Book 2 at
  334 pp, both 0/0/0. Every fixed label was re-read on its page. All grade
  gates pass.

## 4. Tools

- **EXTRA is global.** An `EXTRA` entry links in every chapter. Only harvested
  `STOP` words can be confined to their own chapter. And because `EXTRA` is
  applied after `STOP`, a form listed in both links everywhere.
- **A protect needs a word-start anchor.** Without `(?<!\w)`, the Arabic
  protect for الدفق الحراري ("heat flux") also matched inside التدفق الحراري
  ("heat flow") and silently removed all 22 *heat flow* links.
- **The id_apply math census is exact, spaces included.**
- **`--force-classes math`** let the Indonesian edition write m/Ma inside
  formulas as well as in prose, so Indonesian is consistent. French wrote
  m/Ma in prose but had left three formulas in English's m/Myr (g12/05:179,
  g12 solutions/05:102 and 108). They now read m/Ma, after the user asked,
  on 2026-10-26. nl, es, pt, hi and ar keep English's convention: Ma for a
  date, Myr for a duration.
- **The draw census has false positives.** It still counts `--`, `arc` and
  `circle` inside node text ("core--mantle", "volcanic arc", "small circle").
  Expect 4–7 files to differ, with nothing else.
- **The prose gates do not read the image-credit files**, by design (Latin
  author names). Read those files by eye.
- **The Indonesian prose gate's Texas A&M pattern** could never match in Book
  1. The id agent added a working pattern.
- **Arabic allow-list**: the gate now accepts `nnr`/`morvel` (NNR-MORVEL56),
  `chmee` (a Commons author) and `gplates`, each commented "Book 2 ar".

## Final check (2026-10-26)

- All eight editions were rebuilt with forced builds after the last edit:
  - **English, into `build-final2/`:** 362 pp, 0/0/0.
  - **The seven editions, into `build-final3/`:** results below.
- All 21 grade × language gates pass.
- The linker dry run is 0 and `--check` is clean in all eight languages.
- Book 1's 63 grade × language gates were re-run after this run's shared-tool
  and style changes, and still pass. Book 1 has no `\ce`, so the Arabic `\ce`
  wrap never reaches it.

## 5. After the run: problem pages and blank Arabic pages (2026-10-26)

- **Weekend problems now start on a fresh page** (user ruling; see the repo
  `CLAUDE.md`, "Weekend problems start on a fresh page"). This is done in
  `styles/oneearth.sty` only. Each "Solution p. N" link now stays with its
  exercise's last line.
- **Two blank pages in Arabic Book 2.** The rebuild showed two pages holding
  only the running header, before exercises 1.4 and 7.4. The cause was older
  than the new rule. Babel's tcolorbox hook sets `\textdir TLT` in vertical
  mode, so the empty paragraph a breakable box opens to apply `\parskip` kept
  a dir node and became a zero-height line. At a page foot that line moved to
  the next page, and the box's own `\pagebreak` shipped it alone.
  - Fixed in the style's Arabic block, item 7: the dir nodes are removed when
    the paragraph holds nothing else.
  - This also removes the extra `\baselineskip` that every Arabic box had
    above it.
- **Rebuilt after the fixes:**
  - all 19 builds (Books 1–2 in eight languages, Books 3–5 in English) are
    0/0/0 with zero-height 0;
  - no page holds only a header;
  - no problem heading is separated from its box.
  - Book 1 builds at 329 (en), 342, 340, 338, 339, 319, 307 (ar) and 351 pp.
  - Book 2 builds at 367 (en), 391, 387, 385, 382, 349, 334 (ar) and 393 pp.

## 6. The CI release failure and the TeX Live 2026 check (2026-10-26)

- **What failed.** The `v0.0.3` release (commit `e2b1436`, Book 1 editions)
  failed on the French Book 1 job only: "Package tikz Error: Giving up on this
  path" at `parts/grade-7/fr/05-geological-time.tex:557`. The 3,651 undefined
  references were fallout from that fatal error, and the release job was
  skipped.
- **Cause.** The TeX Live 2026 kernel's `\textsuperscript` runs
  `\check@mathfonts`. The calendar figure (`font=\footnotesize`) uses
  `1\textsuperscript{er}` in an axis node, after the prose above it used the
  same command. That fails in TeX Live 2026, in any language, and builds in
  the local TeX Live 2022. Fixed by bracing: `{1\textsuperscript{er}}`. A
  sweep found no other `\textsuperscript`/`\textsubscript` in an axis, in
  any book or language.
- **Why it was not caught.** Every local build used TeX Live 2022, which
  lacks the fr/nl/es/pt `.ldf`, so those editions built without babel.
- **Check.** All 19 CI editions (Books 1–2 × 8, Books 3–5 in English) were
  rebuilt with `~/texlive/2026` (scheme-full, as CI).
  - All 19 have 0 errors and 0 undefined references, and pass CI's own
    `grep "(Reference|Citation).*undefined"` check. Nullfont is 0.
  - Four overfull lines, hidden until now by the missing hyphenation, were
    fixed with line counts unchanged:
    - the Chuquicamata credit (Book 1 fr/es): `\allowbreak` after the
      slashes of NASA/METI/AIST/Japan;
    - g10 solutions/06 answer 14 (fr): "sont très semblables";
    - g11 solutions/07 answer 6 (es): "el oxígeno".
  - No header-only page, and no problem heading split from its box.
  - Page counts change only for Book 1 fr 340, es 339 and ar 306, and Book 2
    fr 387.
