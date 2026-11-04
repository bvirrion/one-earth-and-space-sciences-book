# Translation run: Earth and space Book 5 into seven languages, by the pilot method

The brief for every edition agent. User request, 2026-11-03: *"do the one earth and space sciences book 5 remaining
translations using the pilot method. Do not do more than 3 books in parallel for now."*

**Scope:** Book 5 (University Year 3, `parts/bachelor-3`), 31 chapters and 31 solution files, 62 files, 280 sections.
**Editions:** `fr`, `es`, `pt`, then `nl`, `id`, then `hi`, `ar`; one agent per edition, at most three at once.
**Tier:** pilot tier throughout. Nothing is committed, by anyone.

You are the coordinator of **one edition** in the sense of `../pilot_translation_instruction.md`. Another agent coordinates
the whole run and owns every shared file. It is your only contact, through your final report.

## Your job: the doc's steps 2 to 8, for your language

Read `../pilot_translation_instruction.md` in full; it is the process. This file says only what differs or what the doc
leaves open. Step 1 (infrastructure) is already done: your entry file, credits stand-in, term-config stub, directories,
`latexmkrc`, `release.yml` and `tools/termlink/books.py`.

**Other reading, and no more than this.** Use `grep -n` and `sed -n` for the rest; don't read whole files:
- `draft/b4-run/coord/brief-<lang>.md` is the old agent brief. Use it only as background: its rules on stints and reading
  every sentence do not apply here.
- `translation_scores/book_4/<lang>/translation_score.md`, the Conventions section: keep every convention it records.
- `../hindi_style_card.md` (hi), `../arabic_style_card.md` (ar, §6 above all), `../indonesian_style_card.md` (id).
- `../translation_instruction.md`, these parts only: "Term linking" (from line 730, the part on curating a config) and
  the lessons of the six-language Book 4 run (lines 1774–1833).
- `tools/term_config/book4_<lang>.py`, as a model of what a curated config looks like.

## The order of work

1. **Language pack** (fr has one). Write `pilot_translation/langs/<lang>.md`, `<lang>.py` and, if needed,
   `langs/series/one-earth-and-space-sciences-book.<lang>.md`. Keep the conventions of your language's Books 1–4: time
   units, compass letters, the article before `\cref`, likelihood words, solution headers.
   - **`ar`:** Book 4 added about 300 each of `\foreignlanguage`, `\babelsublr`, `\mbox`, `\textdir`. Declare what your
     prompt lets the model write in `ALLOWED_MACROS`, and state in the prompt exactly when to use each.
   - **`hi`:** declare `ALLOWED_MACROS` only if your prompt needs them.
2. **Glossary:** `sources/GLOSSARY_BOOK_5_<LANG>.md`, about 500 terms, from your language's Books 1–4. Write it yourself:
   every call obeys it, so this is where your effort pays most. For a term a sister series owns, grep your language's
   edition of physics, chemistry or biology.
3. **Trial chapter, every language except fr.** Run `run.py $ARGS --chapters 15 --workers 3 --book-desc "$DESC"`, then read
   `sample.py $ARGS --chapters 15 --n 8 --seed 1`. Correct the pack or the glossary before the book runs. If you change
   them materially, delete that chapter's outputs and its `sections/15-*` files **by name** and repeat it.
   - **`hi`, `ar`:** also probe-build this chapter (`probe.sh`) and render **every** figure page of it at 130 dpi. If
     right-to-left or Devanagari defects are systematic, fix the prompt first. A defect the prompt can't prevent becomes a
     documented coordinator pass.
4. **The whole book:** `python3 run.py $ARGS --workers 3 --book-desc "$DESC" > $RUN/run.log 2>&1`, in the background. Chapter
   15's accepted sections cost no second call.
5. **The rest of the doc:** steps 5, 6, 7, 8. Their exit conditions are binding.

Use `$DESC` = `university textbook (Earth and space sciences, third university year)`.

## What the first editions found (es finished 2026-11-03: 507 pp, score 91)

Read this before you start; it replaces rediscovering it.

- **Several `run.py` passes are normal.** `es` had 17, then 12, then 2, then 0 files with a rejected section, and retries were about
  half of its calls. Re-run first; reach for `redo.py` or a hand fix only for what a re-run leaves.
- **A clean trial chapter says little about the rejection load.** Use it to check the prose and the pack, nothing else.
- **`run.py` and `common.py` are fixed** for `\\[-1pt]` section cuts and for false "left in English" on math-continuation lines,
  `\foreach` and pgfplots options. You need no wrapper.
- **The English is fixed too.** `\text{ days}` in math and `\num{x}~days` in prose are both yours to translate directly; the math
  census ignores the words in `\text`. You don't need a unit-word `convert()` for this.
- **Whole figures pass the reply checks in English**, because a node-only line has no function words. In `es`, ch. 9 and parts of 13 and 27
  were caught only later by the prose gate, and `\foreach` labels in ch. 7 and 26 by hand. Expect them.
- **Sweep your language's own slips**, which no check sees: a word doubled across a line break (`es` found it in 4 files), uncontracted
  forms split across lines (`es`: *a el*, *de el*), and calques.
- **`post.py`'s `NUMDIFF` found real losses:** `pt` lost 6 bold answer numbers and duplicated 2. Most of its other noise is `Year N`/`Book N`
  written in words; look at every file anyway.
- **`sample.py` reads the run directory, not `parts/`,** so it doesn't show your hand fixes.
- **Render every page `sample.py --pages` lists.** Exit condition of step 7, no shortcut: `es` read 20 of 50 pages and 7 of the 20 had a
  real defect. A low-resolution legend can look black: check at higher resolution before calling it a defect.

- **After any bulk sweep, audit labels, image paths and ledger ids against English.** `pt`'s *kilonova→quilonova* sweep changed an image
  path and a ledger id, and only the ledger id tripped a gate.
- **No `*word*` markdown in your pack or glossary.** Haiku copies it into LaTeX, and it prints (`pt` had about 56). The reply check now
  refuses it, and also refuses a dropped `\textbf{N.}` answer number, but every refusal costs a retry. Write examples in plain text.
- **`pt` finished too: 504 pp, score 90.** Its `run.py --chapters` log prints "written 62 of 4 files", which is only a wrong count.

- **`fr` finished: 509 pp, score 88.** Its sweeps found what no check sees. **Run these on `parts/` after installing, with one script:**
  - **Wind direction, compared with English.** *eastward wind* means blowing towards the east, *easterly* from it. `fr`, `es` and `pt` all got
    ch. 20:414 backwards. List every English line with `easterl|westerl|eastward|westward` beside yours (about 73). `pt` also wrote *em um oeste*
    for *in a westerly*, dropping the noun.
  - **Definitions opening on a bare noun.** `\emph{Névé} est…` is wrong in a language that needs an article there (39 in fr, 44 in es, 47 in pt).
  - **An article stranded before another article or an elided form, including across a line break** (`Dans une\nl'épaisseur`): the elision rule's
    retries cause it. Also doubled words, `\cref` with no article, and compass letters in figures.
  - **More from the `es`/`pt` repair pass:** bare-noun definitions also start mid-line and in lowercase, so read each hit. A whole `Part I --- The
    strain.` head stayed in English in `es` ch. 7 and `pt` ch. 5: grep `Part [IVX]+ ---`. The ch. 17 carbonate-platform sub-captions (a) and (b)
    overprint each other once translated, so wrap them.
  - **Don't use `pkill` or `killall`.** The other editions' builds run under the same names: one edition's careless `pkill` killed a build. Stop
    only a process you started, by its PID.
- **Never delete a file in `rejected/`.** `run.py` then reports "0 files to do" with English still in the file. A section re-runs can't clear after
  about four passes: take its last reply, fix it, and save it through `C.Run.save_section`, leaving every check but the false one in force.
- **The reply check now also refuses a new `\qty` with no unit**, which crashed the French build.
- **`nl` finished: 504 pp, score 90, 13.3M cache read and 120K output for its coordinator, the lowest so far.**
  - **The reply check now refuses comment damage.** The model had overwritten text lines with copied `% ledger:` lines, written a wrong ledger id and dropped another. Translated comments are still allowed.
  - **A bulk decimal-comma replace changed `axis cs:12,56` and killed a build.** Skip coordinates in any number sweep, and audit afterwards.
  - **File-level `NUMDIFF` is too coarse.** Compare line by line when a file's numbers differ: that found the real decimal, thousands and unit-less `\qty` cases.
  - **A picture-wide `font=` beats a node-level size fix.** Only re-reading the page shows it, so re-read every page you repair.
  - **`sample.py --pages` lists pages with no figure.** A listed page with at most 3 strokes, or none `crop.py` can find, can be recorded as not read, with its number in the score file.
- **`id` finished: 505 pp, score 89, 3 `run.py` passes.** Two more sweeps, for `parts/` after installing:
  - **Doubled words across a line break.** Looking at one line at a time misses them. Compare each line's first word with the last words of the line before, math stripped (`id`: about 100 hits, 16 real; `es` and `nl` had them too).
  - **A parenthesis stranded at a line end,** from a dropped word after it: grep `\($`. It prints "( x".
  - **Crop figure regions instead of rendering whole pages:** `draft/pilot-bachelor-3-id/figcrop2.py` saved a lot of image tokens. Whole pages at low resolution can't be proofread, so say so in the score file.

## Keep your own cost down

**The coordinator costs far more than the translation.** `es`'s Opus coordinator used at least 17M cache-read tokens, 1.5M cache-write and
116K output over 124 tool calls, against 12M Haiku tokens in all; `pt`'s used 16M, 1.35M and 132K over 188 calls. Every tool call re-reads your whole context, so **the number of calls and
the size of your context are what cost.** Aim for well under 100 calls.
- **Put several commands in one call**, and several edits in one script. Never make one call per file.
- **Send every long output to a file and read it with `grep` or a line range.** Never print a whole log, chapter or diff.
- **Wait for the background notification.** Never poll a run.
- **Figures:** only the pages `sample.py --pages` lists, plus the trial chapter for hi and ar.
- **Reading:** the seeded sample and three chapter openings, as the doc says. Don't widen it to raise your score: **the score
  states what you found.**
- **Term config:** curate the homographs that matter and reach every target `census.py` shows you can reach. Don't polish
  further.

## What you may write

- `parts/bachelor-3/<lang>/`, `parts/bachelor-3/solutions/<lang>/`
- `../pilot_translation/langs/<lang>.md`, `<lang>.py`, `langs/series/one-earth-and-space-sciences-book.<lang>.md`
- `tools/term_config/book5_<lang>.py`
- `frontmatter/image-credits-book5.<lang>.tex` (translate it; `frontmatter/image-credits-book4.<lang>.tex` shows the wording)
- the `\bookline` and `\author` lines of your entry file, if your language's Books 1–4 need a correction
- `sources/GLOSSARY_BOOK_5_<LANG>.md`, `sources/TRANSLATION_BOOK_5_<LANG>.md`, `translation_scores/book_5/<lang>/`
- `draft/pilot-bachelor-3-<lang>/`, with **`PROGRESS.md`** kept current, so that a fresh agent can resume from it
- an append-only, commented per-language allow-list entry in a prose gate, if one is really needed

## Bans, each from real damage in an earlier run

- No repo-wide git command (`git checkout -- .`, `git restore`, `git stash`, `git clean`, `git reset`), no commit, no wildcard `rm`.
- No `make`, no pytest. No whole-book build except through `pilot_translation/build.sh`, and only of your own edition.
- No edit of the English canon, `styles/`, shared `tools/`, the shared `pilot_translation/*.py`, `pilot_translation_instruction.md`,
  `translation_instruction.md`, any `CLAUDE.md`, or another language's files.
- Render files in the scratchpad start with your language code. Other agents render under the same directory.
- `--workers 3`, never more: three editions run at once on a 19 GB laptop that is also the user's.
- Never read or write the user's e-mail address, and write nothing personal into a repo file.

## When something goes wrong

- **A usage limit.** `run.py` stops by itself and keeps what it has. Update `PROGRESS.md`, and end with a report that says
  `LIMIT` on its first line. You will be resumed or replaced after the reset. Don't wait in a loop.
- **A bug in a shared script or a gate that blocks you.** Update `PROGRESS.md` and end with a report that says `BLOCKED` on
  its first line, with the command, the output and your diagnosis. It gets fixed and you get resumed.
- **A script bug that doesn't block you.** Work around it, and report it at the end.
- **An error in the English.** Translate what's there. Report it at the end with file, line and your arithmetic. If it breaks
  your build or a figure, treat it as `BLOCKED`. Don't recompute solutions looking for errors: the user ruled that out.

The English of Book 5 was edited just before this run: see `draft/pilot-bachelor-3-canon/canon_edits.md`.

## The score file

Follow the doc's step 8. Your `Canon` row says: *English not verified: Book 5 predates the verification pass of
`book_style.md`, and solutions were not recomputed.* Your `Model` row comes from `post.py`'s `== models` block, and names
`claude-opus-5-5` as glossary and coordinator.

## The final report (at most 40 lines)

- First line: `DONE`, `LIMIT` or `BLOCKED`.
- Pages; errors, undefined, overfull, nullfont, missing characters, `.fls`; gates; linker check.
- Links and targets against English (`census.py`). The score, and the sample it rests on.
- Calls, tokens and list price from `post.py`'s `all:` line. Rejected sections, and how they cleared.
- `NUMDIFF`: how many files, how many real losses fixed, which differences you accepted.
- Defects found in the sample and the figures, by class, with what the checks failed to catch.
- Script bugs, English errors (file, line, arithmetic), and anything the doc got wrong or left out.
