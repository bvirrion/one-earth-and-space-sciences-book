# Translating ONE chapter of Earth and space Book 4 into French

Per-chapter run of 2026-10-28. You are one of up to eight agents working at the
same time, each on a different chapter. You translate exactly one chapter of
Book 4 (University, Year 2): its course file and its solution file. Agents run
on `claude-haiku-5-5` (effort high); the coordinator runs on `claude-opus-5-5`
and does all book-wide work afterwards (full builds, term links, unit pass,
scoring).

**This file is the only document you read.** Do not open `CLAUDE.md`,
`translation_instruction.md`, style cards, other run files or other chapters:
everything you need is here or in your chapter folder. Your context is small on
purpose: read each English file once, write the French once, and look at
specific lines with `grep -n` or `sed -n` afterwards instead of re-reading whole
files. Context is compacted automatically if needed; stop only when the chapter
is done.

Paths below: `R` = `/home/bvirrion/repositories/one-course/one-earth-and-space-sciences-book`,
`S` = `/tmp/claude-1000/-home-bvirrion-repositories-one-course/a9157bf7-58d5-404b-ae29-1d263a897841/scratchpad/b4fr`,
`NN` = your chapter number (two digits), `SLUG` = its file name without `.tex`.

## Your inputs (already prepared in `S/chNN/`)

- `en_course.txt`, `en_sol.txt`: the English course and solution files, with
  term links removed and every line numbered (`  12| text`). These numbers are
  the ones the patch tool uses.
- `glossary.txt`: the French term for every defined term of Book 4 that occurs
  in your chapter. **Use these terms exactly** (inflect for number and article).
  Every chapter uses the same glossary, so the book says one word for one
  notion. If a glossary term is wrong in your context, use it anyway and report
  it.
- `sites.txt`: the lines of drawing code whose visible words need care (below).

## What you write, and nothing else

- `R/parts/bachelor-2/fr/SLUG.tex` and `R/parts/bachelor-2/solutions/fr/SLUG.tex`;
- scratch files (patches) in `S/chNN/` only.

Never edit the English files, the glossary, `styles/`, `tools/`, another
chapter's files, or any other file. Never run a repo-wide git command
(`git checkout -- .`, `restore`, `stash`, `clean`, `reset`), never commit, never
`rm` with a wildcard. Never run `make`, `latexmk`, `check_translation.sh`,
`link_defined_terms.py` or pytest: they work on the whole book and would disturb
the seven other agents. Your one build command is the probe inside `check.sh`.

## How to write: patches applied by `id_apply`

You write only the French text, as replacements for numbered English lines. The
tool copies every line you do not name byte for byte from English, and refuses
to write a file whose labels, environments, math, `\ce{}` formulas, drawing code,
image paths, `\emph`/`\index` pairs or braces differ from the English.

Patch format (the first line names target and source; then ranges):

```
### parts/bachelor-2/fr/SLUG.tex <<< parts/bachelor-2/SLUG.tex
@@ 1
\chapter{Titre français}\label{ch:b2:…}
@@ 3-8
Six lignes françaises remplacent les lignes 3 à 8.
@@ 40 !draw
\foreach \n/\t in {1/granite, 2/basalte} …
```

- A range `@@ a-b` replaces lines a..b with the lines that follow, up to the
  next `@@`. **Keep the same number of lines** as the range you replace (one
  French line per English line); the build of the whole book relies on equal
  line counts.
- Ranges ascending, never overlapping. Copy every label, `\cref{…}`, math span,
  `\ce{…}`, `\qty{…}{…}`, `% ledger: …` comment, `\index{…}` and code token
  exactly as it is in the English line.
- `!draw` after a range only when that range translates words inside drawing
  code that the tool compares (a `\foreach` word list, symbolic coordinates,
  labels that come from a data file). Node text, axis labels, titles and
  legends do NOT need `!draw`.
- The file is rebuilt from English on every apply, so **all ranges of one target
  must be applied together**. Write the course translation in parts of 150–250
  lines: `S/chNN/c1.patch` (starting with the `###` line), `c2.patch`,
  `c3.patch` … (ranges only), then
  `cat S/chNN/c*.patch > S/chNN/course.patch` and
  `python3 R/tools/id_apply.py S/chNN/course.patch --dry-run`; repeat for the
  solution file (`s1.patch` … → `sol.patch`). Without `--dry-run` it writes.
- After the first successful write, fix things with the **Edit tool directly on
  the French file**, never by re-applying the patches. `check.sh` re-runs the
  structural comparison on the file on disk.

## Your check (run after every write or edit)

```
bash S/tools/check.sh NN
```

It prints, for your chapter only:
- `TWIN`: the structure compared with English; it must print `TWIN: OK`;
- the prose gates' hits (English words, untranslated lines, orphan lines);
- `ENGLISH?`, `EDGE`, `UNIT` and `NUMBERS` lines from the sweeps;
- the one-chapter build: `errors`, `overfull`, `undefined-refs`,
  `missing-char` and `nullfont`, which must all be 0, with the source lines of
  each overfull box.

The probe takes about a minute and queues if three are already running. Fix
every hit. A `NUMBERS` difference is fine only when you can explain it, for
example a number spelt out in words, or a thousands separator (French writes
`4~610`, or `\num{4610}`). A `draw` line in `TWIN` is fine only where you used
`!draw`.

## Translation rules

- **Register**: the university register of the French sister volumes. Course
  text uses *on*; exercise stems use the infinitive (*Calculer…*, *Montrer
  que…*); history boxes use the passé simple. Write natural French at a native
  level. Do not calque English word order, and do not machine-translate.
- **Translate every visible word**: prose, section titles, box titles
  (`\begin{history}[…]`, `[…]` of `method`, `inthelab`, `keyidea` …),
  captions, table cells, TikZ node text, axis labels, legends, `\text{…}`
  inside math, exercise stems, solutions. Leave nothing in English except
  proper names, titles of papers and books (copied as printed; a French gloss
  in parentheses is allowed), and dataset, mission, model and institution names
  (USGS, NOAA, PREM, ERA5, IPCC→**GIEC**).
- **Never translate**: `\label{…}`, `\cref{…}`/`\ref{…}` targets, the key of
  `\begin{solution}{…}`, file and image paths, `% ledger: …` comments (keep them
  on the same line, unchanged), TikZ node names, colours, styles, macro names,
  anything inside math except `\text{…}`, anything inside `\ce{…}`, and the
  arguments of `\qty`, `\unit`, `\num`, `\ang`.
- **Never put a word or an accented letter inside `\qty{}{}`, `\unit{}` or
  `\num{}`.** Never end a source line on an elision (`l'`, `d'`, `qu'`…): TeX
  prints `d' entropie`.
- **Typography**: non-breaking space before `:` `;` `?` `!` written `~:` `~;`
  `~?` `~!`; guillemets `«~…~»`; the decimal point stays a point (siunitx
  prints numbers); *au \cref{…}*, *la \cref{…}*.
- **Units in prose**: *Ma* for both dates and durations (English writes Ma for
  a date and Myr for a duration), *Ga* for a billion years, *an* for a year,
  *ka* for a thousand years. Write *jours*, *heures*, *ans* as words outside
  `\qty`. **Do not change the units inside `\qty`, `\unit` or math** (`Myr`,
  `\Myr`, `yr`, `kyr`): the coordinator converts all of them by script at the
  end.
- **Compass and coordinates**: N, E, S, **O** for west (`\ang{50}~N`,
  `\ang{20}~O`); hemisphere letters on tick labels likewise.
- **Place names** take their French exonym (*Alpes*, *Himalaya*, *Andes*,
  *Islande*, *Hawaï*, *Groenland*, *Massif central*); people's names are never
  translated.
- **Definitions**: keep `\emph{terme}\index{terme}` adjacent, exactly as in the
  English (the term layer finds definitions this way). The `\index{…}` argument
  is translated with the term (same French word as the `\emph`).
- **Observation only**: the book never sends the reader to a quarry, a cliff, a
  volcano or a river in flood. Keep that true (do not turn *a geologist
  measures* into an instruction to the reader to go and measure).
- **No curriculum names** (no *licence*, *L2*, *BCPST*, *CPGE*, *programme*).
- **Sister series**: *(livre~3, chapitre~N)* style references stay as English
  gives them, translated; *the physics volumes* → *les volumes de physique*.
- Solutions: `\section*{Chapitre \ref{…} --- Titre}`-style headers as in the
  English, translated; *Données~:*. **Recompute every answer along the rounded
  path a student follows.** If the English has a slip, **report it with your
  arithmetic**. Do not change the number in French; the coordinator checks and
  fixes the English and the French together.
- **Series wording** (the same in every chapter): *Problème du week-end ---
  …* (never *de week-end*); `\section{Exercices}`; *Données~:*; *(livre~3,
  chapitre~N)*; *Year 1 / 2 / 3 volume* → *le volume de première / deuxième /
  troisième année*; *ocean island* → *île océanique*; *bulk partition
  coefficient* → *coefficient de partage global*.
- **Palaeogeography** takes French forms, with the article: *la Pangée*, *le
  Gondwana*, *la Laurasia*, *la Téthys*, *la Panthalassa*, *l'océan Rhéique*,
  *l'Iapetus*; orogenies are adjectives (*orogenèse calédonienne, varisque,
  acadienne*). Plain numbers in prose keep the decimal point (`1.6~Ga`).
- Credits inside captions: copy author, licence and source exactly (*public
  domain* → *domaine public*, *via Wikimedia Commons* → *via Wikimedia Commons*);
  *AI-generated illustration* → *Illustration générée par IA.*

## Drawing code (see `sites.txt`)

- `\foreach` lists that carry visible words: translate the words, keep numbers,
  colours and node names, and mark the range `!draw`. Translate only the
  fields that print. Keys used as code stay as they are: style names, colours,
  keys such as `lith`/`atm` that name a style, and element symbols.
- `symbolic x coords` / `symbolic y coords`: the keys must stay as they are
  (the data file uses them). Add an explicit `xticklabels={…}` (or
  `yticklabels`) in French on the same line, under `!draw`.
- Labels that come from a `.dat` file (`meta=`, `nodes near coords`): the data
  file is shared, so do not edit it. Report the site in your final message
  instead. The coordinator replaces them with explicit nodes.
- French labels are longer. If the probe shows an overfull box in a figure, or
  a label collides with another, shorten the French or break it with `\\` in a
  node that has `align=center`.

## When you are done: your final message (at most 15 lines)

1. The two files written, and the last summary lines of `check.sh` (TWIN,
   SWEEPS, probe).
2. English-canon slips you found: `file:line`, what is wrong, your arithmetic.
3. Glossary terms that did not fit, with your suggestion.
4. Your `!draw` ranges, and any `.dat` label site you left for the coordinator.
5. Anything not done, and why.
