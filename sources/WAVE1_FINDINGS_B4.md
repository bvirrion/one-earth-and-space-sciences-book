# Book 4, the six-language run (nl, es, pt, hi, ar, id), 2026-10-30: findings

Run file: `sources/TRANSLATION_BOOK_4.md`. Six `claude-opus-5-5` agents at effort high, one per
edition, **all six at once** (user rule for this run), each in one stint (context compacted
automatically); coordinator `claude-opus-5-5`. The run directory `draft/b4-run/` (gitignored)
holds the coordinator's tools (`tools/build.sh`, `probe.sh`, `engsweep.py`, `numdiff.py`,
`crefart.py`, `census.py`, `pdfsweep.py`, `unitaudit.py`), the canon log `coord/canon_edits.md`
and each agent's `PROGRESS.md`. Read this file before translating Book 4 into another language,
or Book 5 into any.

## 1. Canon edits (English, mirrored into fr and every edition)

Every report was checked three ways: unrounded, along the printed rounded path, and against the
figdata, ledger and source. Line counts never changed.

| # | Site | Old → new | Why |
|---|---|---|---|
| 1 | 06:868; 23:481, 511; sol23:32, 33, 134 | `\qty{…}{hours}`/`{days}` → `{\hour}`/`{\day}` | unit words print English in every edition (fr keeps its own *heures*/*jours*) |
| 2 | 03:412–413 | `\index` key joined onto one line | line-broken key |
| 3 | sol23:87–88 | 6.18e12 → 6.17e12 (twice), 5.06e21 → 5.05e21 | area 6.1743e12 on both paths (nl, es) |
| 4 | 28:493 | `$U = 1 - G(X)$ … $1 - G$ is increasing` → `$U = G(X)$ … $G$ is decreasing` | $G$ is the exceedance probability (nl) |
| 5 | 26:533 | PETM "warmer ↑" node `(axis cs:55.52,1.4)` → `(…,-2.9)` | under `y dir=reverse` it hung below the axis, clipped, invisible in English (es, pt) |
| 6 | sol28:104–105 | 0.0673 → 0.0672 (twice) | 1 − Φ(1.497) = 0.06720; the printed product already used 0.0672 (es) |
| 7 | sol31:123 | 0.37 % → 0.36 % | true double rounding: 0.7286/2 = 0.3643 (pt) |
| 8 | fr/03:102 only | legend "aucun isotope stable" → `\shortstack` | ran into the B cell (pt saw the same in its edition) |
| 9 | 18:648 | Marinoan "at least `\qty{5}{Myr}`" → `{3}` | the paragraph's own brackets give ≥ 639.0 − 636.0 = 3.0; sol18 7(c) says 3 to 15 (hi) |
| 10 | sol18:46, 73, 119 | 0.933 → 0.932 | quoted, never derived; course 0.932 / 93.2 %, figdata 0.9323 (hi) |
| 11 | sol28:107 | 9.24e-3 → 9.23e-3 | left stale by edit 6: 6.05e-3 + 2.77e-3 + 4.08e-4 (hi) |
| 12 | 31:665 | `\label{sec:b2:field-lab-methods-2:problem}` removed | unreferenced; it sat between `\section*{Weekend problem}` and `\begin{problem}`, so `\om@sec@peek` missed the problem and the heading was stranded at the foot of the exercise page in every edition (hi) |

**Edit 11 is a coordinator slip.** A rounded value changed in one line of a chain; the sum two
lines below still used the old one. After any arithmetic canon fix, recompute everything
downstream of it in the same answer.

**Checked and left** (the correct unrounded value, which the printed rounded path cannot
reproduce; not a double rounding): sol03 Eu/Eu* 0.72; sol02 5.5 Earth masses; sol01 7.90e16 and
314 au; sol03 4259 ppm; sol05 58 m; sol06 1.67 + 2.02 = 3.68; ch05 129 vs ch06 127 MPa (each
matches its own printed *s*); sol31 q6 6.9; sol16 pb 17 1445 + 729 = 2173 (unrounded 2173.3).

**Left in the canon:** 21 line-broken `\index` keys (02:499, 03:53, 03:157, 06:469, 08:153,
08:296, 08:636, 10:74, 10:99, 11:91, 12:96, 15:394, 18:249, 21:334, 27:191, 27:352, 28:197,
28:200, 30:323, 30:435, 30:495). They build correctly; gate 5 checks translations only, so each
edition joins its own. The ch31 station map's north arrow at (4.45, 4.75) is invisible in English
too (ar).

## 2. Tool changes

- **`\index` reducer of `check_arabic_prose.py` / `check_hindi_prose.py`** (inherited by the
  Indonesian gate): the makeindex encap `key|see{target}` now keeps key and target and drops the
  word *see*. Arabic had removed a see-reference to pass. Lenient; tested on a control file.
- **Allow-list entries**, append-only and commented, by each agent: credit names and titles as
  exact phrases (hi `CREDIT_PHRASES`, ar `CREDIT_TITLE_PHRASES`, id `ATTRIBUTION`), mineral and
  site subscripts in math (`ky/and/sil`, `Mg,grt`, `An` before a subscript), code keys in
  `check_latin_prose.py`. The id agent narrowed the split-number rule so a control word before a
  number (`\times\, 370.7`) is exempt; prose "ribu\, 370" still fires.
- **Open bugs.** `check_latin_prose.py` given a file path prints "OK (0 files)" and checks
  nothing. The Indonesian gate reads the TikZ anchor `label={[..]east:…}` as the English word
  *east* (worked around with the angle `0:`). `id_apply` does not check a range's line count:
  hi found 18 ranges one line short. `\om@sec@peek` does not skip a `\label` (edit 12 removed
  the only site).
- **Shared scratchpad.** Six agents rendered pages into one session scratchpad; es overwrote an
  id render of the same name. Prefix render files with the edition.

## 3. Arabic right-to-left traps (new in Book 4)

None of these produces a log message; each was found on a rendered page.
- A parenthesis whose content is Latin only, after Latin or a digit ("OIB (BHVO-2)",
  "Team (STScI/AURA)"), is **mirrored** (`bidi=basic` has no bracket-pair rule). Wrap the whole
  Latin run in `\babelsublr{…}` in prose, `\mbox{\textdir TLT …}` in table cells.
- A Latin word next to math in Arabic prose ("Th $= 1.414$", "VEI $\ge 3$") prints as two
  runs, the math on the wrong side. Box `word $math$` together.
- A table cell "SiO$_2$" prints "₂SiO"; a pure-Latin axis label "math (unit)" prints
  "(unit) math". Box them.
- `\foreignlanguage{arabic}{…}` in an axis label of a two-axis picture placed with
  `at={(name.east)}` **mirrors the panel order**. Plain Arabic labels keep it.
- "Latin: digits" lists ("Sr: 0.000063 / 0.157") and "Rb (10 و20)" print reversed. Write
  "An$_{83.3}$ (1465 و1521)" or put the element's Arabic name first.
- A credit in `\babelsublr` breaks across lines in a narrow caption ("(Mike Davis," / "CC0)");
  `\mbox{\textdir TLT …}` keeps it whole. A breakable `\babelsublr{X $=…$}` was replaced 41 times.
- A node that starts with «(أ)» puts its bracket at the far end; `\raggedright` and
  `\raggedleft` both give flush-left in a right-to-left caption.
- A caption parenthesis that starts with `\qty` and ends with a Latin code puts its brackets on
  the wrong sides: start and end it with Arabic.
- Latin `;` and `,` between math spans become `؛` and `،` (33 sites).

## 4. Other findings

- **Cross-volume glosses.** hi writes "पुस्तक 3 (स्नातक वर्ष 1)" where English says "the Year 1
  volume" (Hindi Book 3's convention); id reverted one "Buku 2, kelas 12" to English's wording.
  Both are fine if the book numbers are right; check them.
- **Data-file labels.** The ch15 supercontinent and ch19 extinction charts print names from
  figdata: every edition draws explicit nodes, as fr does (`!draw` ranges in each score file).
- **Units.** nl/es/pt/hi/ar keep Ma/Myr/Gyr/yr; id writes Ma/Ga/ka everywhere (`\per\Ga`
  included), leaving `Myr` only in table keys (`t_Myr`) and comments.
- **Links.** Arabic is at 65 % of English (1,318 / 2,019): two STOPs (التحوّل, الكشف) and the
  definite/indefinite split. Hindi is 99 %, the Latin editions and id 97–111 %.
