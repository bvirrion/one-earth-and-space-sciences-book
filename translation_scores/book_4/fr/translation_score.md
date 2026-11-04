# Translation score — Earth and Space Sciences Book 4 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 4 (University Year 2, `bachelor-2`) |
| **Language** | French (`fr`) |
| **Quality bar** | native French university-course prose (second year: milieu interstellaire, formation planétaire, géochimie élémentaire et isotopique, magmatisme, volcanisme, fusion du manteau, différenciation, séries magmatiques, métamorphisme et thermobarométrie, fusion crustale, chaînes de montagnes, cycle de Wilson, bassins, îles océaniques, histoire de la Terre, paléontologie, thermodynamique de l'atmosphère, systèmes météorologiques, variabilité et archives climatiques, forçage orbital, changement climatique, aléas, gisements, énergie, méthodes de terrain et de laboratoire). English is the source of truth for content, structure, labels, mathematics and drawing code |
| **Sense / register references** | the English canon; this series' French Books 1–3 and their term configs; a per-chapter glossary of every defined term of Book 4, shared by all agents |
| **Overall score** | **95 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-28 |
| **Model** | translation agents `claude-haiku-5-5` (Haiku 5.5, effort high), **one per chapter**, at most eight at once; coordinator `claude-opus-5-5` (Opus 5.5) |
| **Scope** | 31 chapters + 31 solution twins = **62 files**, each chapter written by its own agent through `tools/id_apply.py` line-range patches over the numbered English; `frontmatter/image-credits-book4.fr.tex`; a curated `tools/term_config/book4_fr.py`; the term layer; one documented allow-list entry in `tools/check_latin_prose.py`; this score |

## Verdict in one line

A French Book 4 in the university register of Books 1–3 (impersonal *on*,
infinitive exercise stems, *Ma*/*Ga*/*ka*/*an* throughout, N/E/S/O, spaced
punctuation), structurally identical to English, all gates green, built
0 errors / 0 undefined / 0 overfull. It was written chapter by chapter by 31
agents and never read whole by one reader: that, and a figure check that was
sampled rather than exhaustive, keep it at 95.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Counted over the 62 files against their twins: 372 `exercise`, 31 `problem`, 403 `solution`, 204 `omfigure`, 171 `tikzpicture`, 104 `axis`, 59 `\includegraphics`, 30 `tabular`, 616 `\emph`, 449 `\index`, 999 `\label`, 857 `\item`, 1,066 `% ledger:`, 512 `\ce`, 230 `definition`, 109 `proposition`, 99 `proof`, 8 `history`, all equal to English. `\node` 866 against 864: the extinction labels of ch. 19 and the supercontinent labels of ch. 15, drawn as explicit French nodes instead of data-file labels. `\qty` 6,175 against 6,162: thirteen sites where French writes a quantity English gives as a word (one the other way, `\num{10}~heures`) |
| Terminology | **96** | One glossary for all 31 agents, so one word per notion across the book (*nappe de charriage, coefficient de partage global, île océanique, ultra-haute pression, hyperalumineux, planétésimal, chemin P--T--t, faciès des schistes bleus, cellule de Hadley, TCRE, GIEC*…); palaeogeography with its French article (*la Pangée, le Gondwana, la Téthys, l'océan Rhéique, l'Iapetus*) and orogenies as adjectives (*calédonienne, varisque*). 449 `\index` keys in French |
| Register / tone | **95** | Course text in the present with *on*, exercise stems in the infinitive, history in the passé simple, 0 *tu*/*vous*. A coordinator sweep added the missing article before 55 cross-references (*de la \cref{prop}*, *du \cref{ch}*, *l'\cref{exo}*) and turned four *problème de week-end* into *du week-end*. Sampled pages read as native French; the whole book was not re-read sentence by sentence by one reader |
| Typography | **97** | `~:` `~;` `~?` `~!`, guillemets, decimal point (series setting), 0 lines ending on an elision, 0 straight double quotes |
| Fidelity / accuracy | **95** | Every agent recomputed its solutions along the printed rounded path and reported slips. The coordinator verified each report three ways (unrounded, along the printed path, against figdata/ledger/source); about half were the agents' own errors and were rejected, **53 were real** and were fixed in English and French together (list below) |
| Figures | **93** | Every visible label translated; data-file labels (ICS periods, extinction names, supercontinents) replaced by explicit French nodes; each chapter's probe build was 0 overfull. Rendered pages were **sampled** (supercontinent and extinction charts, the disc-fraction and TCRE charts), not checked one per page; *Trapezium* → *Trapèze* and a pink band called *grisée* were found that way |
| Links | **96** | **2,262 `\omterm` links on 199 targets** (def 2,238, prop 24) against English's 2,019 on 191: every English target reached. Homographs curated by census (`book4_fr.py`): *gisement, teneur, détection, attribution* STOPped outside their defining chapters; *nappe* linked only as a thrust sheet, its groundwater/pumice/debris senses masked. Dry run: **links to insert: 0** |

## Gates and build

- `bash tools/check_translation.sh bachelor-2 fr`: **PASSED**. The twin prose gate
  has no multi-word finding after one documented `ALLOWED_BY_LANG["fr"]` entry (hole
  names, style keys, mineral and cloud words spelt the same in French, `Mg/Ca`,
  `grt`). The advisory one-word tier (152 hits) was read: cognates, minerals,
  place names.
- `bash tools/gates.sh bachelor-2`: **gates OK**.
- Final build (TeX Live 2026, forced `-g`, into `build/`, after the last edit):
  **509 pages**, errors 0, undefined 0, overfull 0, nullfont 0, missing-char 0,
  invalid-in-math 0, zero-height 0, `.fls` 62 = files on disk (English: 484 pages,
  same zeros).

## Conventions

- Units: *Ma* for dates and durations, *Ga*, *ka*, *an* (`mm/an`), *jours*,
  *heures*. The coordinator converted every unit argument, prose and math, by
  script after the agents finished (`\Myr`→`\Ma`, `\mega\year`→`\Ma`,
  `}{days}`→`}{jours}`…). Table keys such as `t_Myr` and comments were left alone.
- Series wording: *Problème du week-end*, *Données~:*, *(livre~3, chapitre~N)*,
  *le volume de première année*, *île océanique*, *coefficient de partage global*.
- Credits: authors, licences and sources kept exactly; *domaine public*;
  *Illustration générée par IA.*

## English-canon edits (53, mirrored into French)

The full list, with old and new text, is in the coordinator's run log. The
classes:
- arithmetic along the printed path: about 35 values (e.g. sol09 30.4 → 30.3,
  sol18 0.409 → 0.4088, sol21 1.1 % → 1.2 %, sol28 0.273 → 0.272);
- wrong physics or wording: *less dense* → *denser* (ch. 10), pyroclastic flows
  "hotter than 800 °C" → 200–700 °C (ch. 6), a reversed pause order (ch. 17),
  "of the age" → "of the time a section spans" (ch. 24, checked against
  Svensson et al. 2008);
- a sourced value: the Hawaiian–Emperor volume (ch. 17) reworded to what
  Clague and Sherrod (2014) say, and its ledger row rewritten;
- code: a chapter macro `\up` that clashed with babel-french (renamed), a
  unit-less `\qty{0.311}{}` → `\num{0.311}`, 13 line-broken `\index` keys joined.

## Open (not done in this pass)

- A rendered figure check of every figure, one per page, at 130 dpi.
- A sentence-by-sentence reading pass by one reader across the 31 chapters.
- The shared solution head prints *Solution de Exercice 10.1* (string
  `\omsolutionof` in `styles/lang/fr.tex`, the same in every One Course
  series and in es/pt); *Solution de l'exercice 10.1* needs a style change
  that touches every shipped French edition, so it is left to the user.
