# Translation score — One Earth and Space Sciences Book 4 · Spanish (`es`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 4 (University Year 2, `bachelor-2`) |
| **Language** | Spanish (`es`), peninsular; impersonal *se* in course text, impersonal *-se* imperative in exercise stems; terms as in this series' Spanish Books 1–3 and the Spanish University Year 2 editions of the sister series |
| **Model** | `claude-opus-5-5` (Opus 5.5, effort high), **one agent for the whole edition**, in stints (drafting A, finishing B, reading C, measuring and scoring D; the context was compacted between stints, PROGRESS.md carried the state); coordinator `claude-opus-5-5` |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95: **met** |
| **Date** | 2026-10-30 |
| **Scope** | 31 chapters + 31 solution files = **62 files**, written through `tools/id_apply.py` line-range patches over the numbered English (one cumulative patch per file, `draft/b4-run/es4/pNN/`); `frontmatter/image-credits-book4.es.tex`; a curated `tools/term_config/book4_es.py`; the term layer; one commented `ALLOWED_BY_LANG["es"]` entry in `tools/check_latin_prose.py`; this score |

## Verdict in one line

A Spanish Book 4 in the university register of Books 1–3, structurally identical to
English line for line (29,781 lines on both sides), all gates green, built 0 errors /
0 undefined / 0 overfull, and **read end to end, every chapter and every solution file,
against its English twin by one reader** (Phase C: about 120 fixes, all through the
patches). What keeps it below 97: the figures were render-checked where text changed
and on the run file's list, not one page per figure; English titles of works and
agencies are kept in credits; a few terms remain English loans by choice.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Counted over the 62 files against their twins: 372 `exercise`, 31 `problem`, 403 `solution`, 204 `omfigure`, 171 `tikzpicture`, 104 `axis`, 59 `\includegraphics`, 30 `tabular`, 616 `\emph`, 449 `\index`, 999 `\label`, 857 `\item`, 1,066 `% ledger:`, 512 `\ce`, 230 `definition`, 109 `proposition`, 99 `proof`, 6,162 `\qty`, all equal to English. `\node` 866 against 864: the explicit supercontinent (ch. 15) and extinction (ch. 19) labels, drawn as the French edition does. Every file has English's line count (three patch ranges that had come out one line short were split in Phase B) |
| Terminology | **96** | One glossary (`draft/b4-run/es4/GLOSSARY.md`), one word per notion: *coeficiente de reparto global, isla oceánica, ultra alta presión, peraluminoso, planetesimal, trayectoria P--T--t, facies de esquistos azules, mapa de peligrosidad, ley de corte, yacimiento*; palaeogeography as Spanish geology writes it (*Pangea* and *Gondwana* without article, *el Tetis, el océano Rheico, el Iapetus, las Caledónides*). The display-drift list (64 targets with two displays) was read: 58 vary in English too, the other six are inflection, capitalisation or a definition that names two terms (*factor de seguridad*, *flujos de derrubios*) |
| Register / tone | **96** | Course text in the present with impersonal *se*; history boxes in the preterite; exercise stems in the impersonal *-se* imperative: **484 / 0 / 0** (*-se* / *usted* / *tú*; the three hits for *Compara, Muestra, Demuestra* are third-person indicatives). Article before every `\cref` (*del \cref{ch}*, *la \cref{exo}*, *de la \cref{prop}*): `crefart` 0 doubled nouns in 31 chapters |
| Typography | **97** | Spanish opening marks (¿ ¡), «comillas» throughout (28 pairs; the 11 TeX ``…'' pairs left from drafting were unified in Phase D), decimal point (series setting), 0 straight double quotes, 0 lines ending on an apostrophe or a hyphen, 0 lines opening with punctuation, every `\index` key on one line; keys that start with an accented letter carry a sort key (*indice ...@índice ...*) so the printed index files them under I |
| Fidelity / accuracy | **96** | Every solution recomputed along the printed rounded path in Phase A and re-read against its question in Phase C. Four canon reports, three confirmed and fixed by the coordinator, one withdrawn (list below). Ranges phrased so they cannot be misread: `de \qtyrange`, *entre X y Y* after a verb of change (*bajó/subió/se calentó entre ...*: "de X a Y" there would read as a change from X to Y) |
| Figures | **94** | Every visible label translated, data-file labels replaced by explicit nodes (ICS periods, extinctions, supercontinents); rendered and read: the run file's list (table caption and `\cref{tab}`, the supercontinent and extinction charts, the ICS bars, the PETM label, the ch. 19 OAE node) and every figure whose labels were re-laid (`!draw` list); not one page per figure |
| Links | **96** | **2,087 `\omterm` links on 195 targets** (def 2,062, prop 25) against English's 2,019 on 191: every English target reached; four Spanish-only targets, each a definition whose Spanish term occurs in prose where the English phrasing does not harvest (*tierras raras*, *tsunami*, the open-system differentiation definition, *saturación en sílice*). Homographs curated by census in `book4_es.py` (docstring lists each sense): *ley* is ore grade only in ch. 29 (laws masked by `EXTRA_PROTECT`), *exposición, detección, atribución* STOPped outside their defining chapters, *razón de mezcla que minimiza* protected. Dry run: **links to insert: 0** |

## Gates and build

- `bash tools/check_translation.sh bachelor-2 es`: **PASSED** (no multi-word finding;
  80 advisory one-word hits read: cognates, proper names, units, style keys).
- `bash tools/gates.sh bachelor-2`: **OK**.
- `tools/check_orphan_lines.py`: 0 orphan English lines.
- Run sweeps over all 31 chapters: `engsweep` 5 lines, all credits or titles
  (*Volcanoes of the World*, *Principles of Geology*, U.S. Army Corps of Engineers ×2,
  U.S. Department of Defense); `numdiff` only spelt-out small numbers (*Year 1* →
  *primer año*), *1960s* → *años sesenta*, thousands without comma (4158 ft), billions as
  *millones* (2.7 Ga → 2700 millones), *Niño 3.4*, and the explicit chart nodes;
  `crefart` 0.
- **Final build** (TeX Live 2026, forced, `draft/b4-run/tools/build.sh`, build `es-2`):
  latexmk rc 0, **511 pages**; errors 0; undefined 0 (font-shape warnings 1, the
  babel-spanish `T1/lmr/bx/sc` baseline); **overfull 0**; nullfont 0; missing characters 0;
  invalid-in-math 0; zero-height 0; `.fls` lists **62** translated files = the 62 on disk.
  Rendered and read on this build: the ch. 3 Goldschmidt table (legend *sin isótopo /
  estable* on two lines, coordinator msg4: it had touched the B cell), the table caption
  (*Tabla 1.1*; Book 4 has no `\cref{tab:…}`), the supercontinent chart (ch. 15), the
  extinction chart with its ICS period bar and OAE diamonds (ch. 19), the PETM figure with
  its *más cálido ↑* label (ch. 26), the printed index (*índice …* filed under I).

## Conventions recorded

- **Units:** English's Ma / Myr / Gyr / kyr / yr kept byte-identical in prose and math,
  as in Spanish Books 1–3 (only fr and id convert). A word after `\qty[...]{624}{}` is
  translated (*mil años*).
- **Ranges:** `de \qtyrange{a}{b}{u}` (a bare *entre el \qtyrange* printed "entre el 10 a
  15 %"; 4 + 1 + 17 sites fixed); prose ranges *entre X y Y* or *de X a Y*, never *de X a
  Y* after a verb of change.
- **Series wording:** *(libro 2, año 11)*, *el volumen de primer año*, *los libros de
  física*; *Problema de fin de semana*; *\section{Problema: título en minúscula}*;
  *(ilustración generada por IA)*; *Fotografía:*; *dominio público*; compass N, E, S, O.
- **Acronyms:** English acronyms kept where Spanish literature uses them, with *por sus
  siglas en inglés* at first use (MORB, OIB, OAE, ERF, ECS, TCR, TCRE, SSP, STOIIP, TTI,
  EGS, TIMS); Spanish ones where they are standard (ENOS, NCA/NCL/NE for LCL/LFC/EL), IPCC
  kept. Seasons DEF/EFM/NDE; H/L → A/B on maps.
- **Calibrated language** as in g12 es: *probable, muy probable, prácticamente seguro,
  confianza alta*.
- **Solution head:** `\section*{Capítulo \ref{…} --- Título}`; the shared
  `\omsolutionof` still prints *Solución de Ejercicio N* (open item of every edition).

## `!draw` ranges (per range, each checked on the rendered page)

- 02 course 373–377: `\foreach` dust-to-planets labels.
- 03 course 101–102: Goldschmidt class legend fields (keys `lith/sid/chal/atm/none` kept).
- 11 course 63–70: isograd `\foreach` names, *zona de* node, arrow label.
- 14 course 171–173, 275–278, 385–389: MHT, Ganges and sea-level labels on two lines.
- 15 course 343–347 (*empieza la expansión*, anchor south west), 416–422 (supercontinent
  names as explicit `\foreach` nodes, *Pangea*).
- 17 course 200: slump label on two lines.
- 19 course 468–470: extinction labels as explicit `\foreach` nodes (the `.dat` carries
  English).
- 21 course 618–619: vapour label moved `right=4pt` → `8pt`, clear of the dashed arrow.
- 23 course 100, 206–208: panel titles (*verano/invierno*, *neutro*).
- 24 course 156: panel titles (*hoy*, *un máximo glaciar*).

No `--force-classes` was used.

## English-canon reports (with arithmetic)

1. **solutions/23 exo 11** (lines 86–88): area of Niño-3.4 printed 6.18e12 m²;
   R²·Δλ·(sin 5° − sin(−5°)) = (6.371e6)² × 0.872665 × 0.174311 = 6.1743e12 → 6.17e12
   (printed path 6.1742e12); then Q = 1025 × 3992 × 100 × 2 × 6.17e12 = 5.05e21 J, not
   5.06e21. **Confirmed**, fixed in English, mirrored.
2. **26:533** (PETM figure, lower panel): the *warmer ↑* node at y = 1.4 with
   `anchor=north east` and `y dir=reverse` falls below the axis and is clipped: it printed
   in no edition. **Confirmed**, moved to y = −2.9, mirrored.
3. **solutions/28 problem q12** (line 104): 1 − Φ(1.4967) = 0.06724 → 0.0672, printed
   0.0673 (wrong unrounded); the printed product 0.09 × 0.0672 = 6.05e−3 already used 0.0672.
   **Confirmed**, fixed, mirrored (both sites).
4. **solutions/31 problem q6**: reported 6.9 → 6.8; **withdrawn**, my division was wrong
   (0.132143 / 0.019276 = 6.855 → 6.9).

Also mirrored from the coordinator: the ch. 28 Weibull proof (G decreasing), sol31 0.37 →
0.36 %, the sol16 values kept as printed.

## Fixes made in the reading pass (Phase C)

About 120 (93 while reading, plus the range and `\qtyrange` sweeps), all in the patches, then every chapter re-applied (no REJECT) and relinked.
Among them: *peníndicos* → *penínicos* (6 sites); *los* → *las Caledónides*; the OAE
acronym and its ch. 19 figure node; 14 ambiguous ranges in ch. 26; problem headings in
lowercase after *Problema:*; carbon-cycle arrow labels as `\shortstack` (they overflowed
4 cm arrows); a `:` line left by a joined `\index` key (ch. 3, ch. 8).

## Departures from Books 1–3 (Spanish)

- **Articles before `\cref`** everywhere (run file rule); Book 3 es often omitted them.
- **Explicit chart labels** in ch. 15 and ch. 19 (`\foreach` nodes), as the French Book 4
  does, because their figdata tables print English.
- **Model:** one Opus 5.5 agent for the whole edition (Book 3 es: Haiku 5.5 in stints).

## Open items (why 96, not higher)

- Figures were checked on the rendered pages listed above, not one per page.
- English titles of works and agency names are kept in credits and history boxes.
- Accepted under-linking where a homograph cannot be linked safely (*ley* outside ch. 29).
