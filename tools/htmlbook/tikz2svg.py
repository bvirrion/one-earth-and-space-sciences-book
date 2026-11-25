"""Compile a tikzpicture to SVG (text as paths, so no font dependencies).

Each figure is compiled with the book's own style file (see PREAMBLE),
then converted with dvisvgm --pdf --no-fonts, falling back to
pdftocairo -svg. Figures are keyed by a content hash so identical
pictures across language editions build once.
"""

import hashlib
import os
import re
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .lexer import ParseError

# Earth and space sciences books: as in the chemistry books, every picture
# compiles against the book's own style file (styles/oneearth.sty: lithologies,
# map symbols, fronts, celestial sphere…), loaded with the edition's script
# language, so a figure looks exactly as printed and nothing has to be mirrored
# here. `preview` crops each picture (the style draws the brand logo at load
# time, which a standalone class would turn into an extra page); dvisvgm
# --exact-bbox then trims the border.
PREAMBLE = r"""
\documentclass{book}
\newcommand{\booklang}{@LANG@}
\usepackage{styles/oneearth}
\usepackage[active,tightpage]{preview}
\setlength\PreviewBorder{1.5cm}
\begin{document}
@DIR@\begin{preview}
"""
POSTAMBLE = "\n\\end{preview}\n\\end{document}\n"
# Book directories the style file and the pictures read, relative to the
# compile directory (fonts under assets/fonts, photos, figdata tables)
BOOK_DIRS = ("styles", "assets", "images", "figdata")
REPO_ROOT = Path(__file__).resolve().parents[2]

# Script detection picks the edition's style set-up: Devanagari text →
# XeLaTeX with \\booklang hi, Arabic text → LuaLaTeX with \\booklang ar (the
# style file loads their bundled Noto faces from assets/fonts), anything
# else → pdfLaTeX, T1 Latin Modern, as in print.
DEVANAGARI = re.compile(r"[ऀ-ॿ]")
ARABIC = re.compile(r"[؀-ۿ]")


def tikz_hash(tikz):
    normalized = re.sub(r"\s+", " ", tikz).strip()
    # pictures embedded in the tikz (\\includegraphics inside a node, the
    # biology label overlays) are part of the figure: key on their bytes too
    for m in RASTER_RE.finditer(tikz):
        path = Path(m.group(2).strip())
        if path.exists():
            normalized += hashlib.sha1(path.read_bytes()).hexdigest()
    # so are the data files a pgfplots \addplot table reads (the quant
    # books' figdata/…csv): regenerated data rebuilds the figure
    for m in DATA_FILE_RE.finditer(tikz):
        # a figure-local macro may build the name from its argument
        # (figdata/out/…-#1.dat): key on every file the pattern matches
        for path in sorted(Path().glob(re.sub(r"#\d", "*", m.group(1)))):
            normalized += hashlib.sha1(path.read_bytes()).hexdigest()
    return hashlib.sha1(normalized.encode("utf-8")).hexdigest()[:12]


# Data files read by pgfplots tables, relative to the book repo root.
DATA_FILE_RE = re.compile(r"\{(figdata/[^{}]+)\}")


def absolute_data_paths(tikz):
    """The compile runs in a temp dir: point figdata/… at the repo copy."""
    def repl(m):
        path = Path(m.group(1)).resolve()
        if not path.exists():
            raise ParseError(f"figure data file not found: {m.group(1)}")
        return "{" + str(path) + "}"
    return DATA_FILE_RE.sub(repl, tikz)


def stage_rasters(tikz, tmp):
    """Rewrite \\includegraphics inside a tikzpicture to web-sized JPEGs
    copied beside fig.tex (the compile runs in a temp dir, and the
    embedded bitmap should be as light as a standalone photo)."""
    def repl(m):
        opts, path = m.group(1), m.group(2).strip()
        data, _, _ = build_raster(path, "")
        name = f"img-{hashlib.sha1(data).hexdigest()[:12]}.jpg"
        (tmp / name).write_bytes(data)
        return "\\includegraphics" + (f"[{opts}]" if opts else "") \
            + "{" + name + "}"
    return RASTER_RE.sub(repl, tikz)


def _run(cmd, cwd, env=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                          errors="replace", env=env)


# A dense spectrum (thousands of pgfplots points) boxed whole by preview
# overflows the default main memory (pdfTeX, and XeTeX for the Hindi
# NMR panels); extra_mem_bot extends it at run time (no format rebuild).
# extra_mem_top is the same for tokens: pgfplots' 10,000-cell matrix plots.
TEX_ENV = dict(os.environ, extra_mem_bot="100000000",
               extra_mem_top="100000000")


def build_svg(tikz):
    """Compile one tikzpicture; returns (svg_text, width_px, height_px)."""
    with tempfile.TemporaryDirectory(prefix="omfig-") as tmp:
        tmp = Path(tmp)
        lang, engine, direction = "en", "pdflatex", ""
        if DEVANAGARI.search(tikz):
            lang, engine = "hi", "xelatex"
        elif ARABIC.search(tikz) or "\\babelsublr" in tikz \
                or "\\textdir" in tikz:
            # (\\babelsublr, \\textdir: an Arabic-edition LTR run, even
            # without Arabic letters in the picture)
            # the Arabic edition's own set-up (LuaLaTeX, babel bidi), with
            # a left-to-right page: an RTL paragraph shifts the picture
            # out of the preview box
            lang, engine = "ar", "lualatex"
            direction = "\\pagedir TLT\\bodydir TLT\\pardir TLT\\textdir TLT\n"
        preamble = PREAMBLE.replace("@LANG@", lang).replace("@DIR@", direction)
        for d in BOOK_DIRS:
            os.symlink(REPO_ROOT / d, tmp / d)
        has_raster = bool(RASTER_RE.search(tikz))
        if has_raster:
            tikz = stage_rasters(tikz, tmp)
        # (figdata/ is symlinked beside fig.tex: relative paths resolve)
        (tmp / "fig.tex").write_text(preamble + tikz + POSTAMBLE,
                                     encoding="utf-8")
        res = _run([engine, "-interaction=nonstopmode", "fig.tex"], tmp,
                   TEX_ENV)
        if re.search(r"\\chemmove|remember picture", tikz):
            # \\chemmove draws between remembered nodes: their positions
            # come from the .aux of a first run (which may complain)
            res = _run([engine, "-interaction=nonstopmode", "fig.tex"], tmp,
                       TEX_ENV)
        if engine == "xelatex" and "TeX capacity exceeded" in res.stdout:
            # XeTeX's fixed memory overflows on the Hindi NMR panel grid
            # (pdfTeX copes with the Latin twin): LuaTeX allocates memory
            # dynamically; its HarfBuzz renderer shapes Devanagari as
            # XeTeX does (the default node mode breaks the conjuncts)
            engine = "lualatex"
            (tmp / "fig.tex").write_text(
                preamble.replace("\\newcommand{\\booklang}{hi}",
                                 "\\newcommand{\\booklang}{hi}\n"
                                 "\\usepackage{fontspec}\n"
                                 "\\defaultfontfeatures{Renderer=HarfBuzz}")
                + tikz + POSTAMBLE, encoding="utf-8")
            for _ in range(2 if re.search(r"\\chemmove|remember picture",
                                          tikz) else 1):
                res = _run([engine, "-interaction=nonstopmode", "fig.tex"],
                           tmp, TEX_ENV)
        if res.returncode != 0 or not (tmp / "fig.pdf").exists():
            tail = res.stdout[-2500:]
            raise ParseError(f"{engine} failed for a figure:\n{tail}")

        svg_path = tmp / "fig.svg"
        res = _run(["dvisvgm", "--pdf", "--no-fonts", "--exact-bbox",
                    "-o", str(svg_path), "fig.pdf"], tmp)
        if has_raster and svg_path.exists() \
                and "<image" not in svg_path.read_text(encoding="utf-8"):
            # dvisvgm dropped the embedded bitmap: let cairo embed it
            svg_path.unlink()
            res = _run(["pdftocairo", "-svg", "fig.pdf", str(svg_path)], tmp)
        if res.returncode != 0 or not svg_path.exists():
            res = _run(["pdftocairo", "-svg", "fig.pdf", str(svg_path)], tmp)
            if res.returncode != 0 or not svg_path.exists():
                raise ParseError(
                    "both dvisvgm and pdftocairo failed to convert a "
                    f"figure:\n{res.stderr[-2000:]}")
        svg = _tight_crop(svg_path.read_text(encoding="utf-8"),
                          tmp / "fig.pdf")
        return svg, *_svg_size(svg)


def _tight_crop(svg, pdf):
    """Crop the SVG to the marks on the page (Ghostscript's bbox device):
    the preview border leaves room for \\chemmove overlays drawn outside
    the picture's box, and neither converter trims it."""
    res = _run(["gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=bbox",
                str(pdf)], pdf.parent)
    m = re.search(r"%%HiResBoundingBox: ([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)",
                  res.stdout + res.stderr)
    root = re.search(r"<svg[^>]*>", svg)
    vb = root and re.search(r"viewBox=['\"]([-\d. ]+)['\"]", root.group(0))
    if not (m and vb):
        raise ParseError("could not measure a figure's bounding box")
    llx, lly, urx, ury = (float(v) for v in m.groups())
    vx, vy, _, height = (float(v) for v in vb.group(1).split())
    margin = 1.0                       # pt: keeps hairlines whole
    x0, y0 = vx + llx - margin, vy + (height - ury) - margin
    w, h = urx - llx + 2 * margin, ury - lly + 2 * margin
    new_root = re.sub(r"width=['\"][^'\"]*['\"]", f"width='{w:.3f}pt'",
                      root.group(0), count=1)
    new_root = re.sub(r"height=['\"][^'\"]*['\"]", f"height='{h:.3f}pt'",
                      new_root, count=1)
    new_root = new_root.replace(vb.group(0),
                                f"viewBox='{x0:.3f} {y0:.3f} {w:.3f} {h:.3f}'")
    return svg.replace(root.group(0), new_root, 1)


def _svg_size(svg):
    """Width/height in CSS px (1pt = 4/3 px), from the SVG root element."""
    m = re.search(r"<svg[^>]*>", svg)
    if not m:
        raise ParseError("no <svg> root element in converted figure")
    root = m.group(0)

    def dim(name):
        dm = re.search(rf"""{name}=["']([\d.]+)(pt|px)?["']""", root)
        if not dm:
            raise ParseError(f"figure SVG has no {name} attribute")
        value = float(dm.group(1))
        if dm.group(2) != "px":
            value *= 4.0 / 3.0
        return round(value)

    return dim("width"), dim("height")


RASTER_MAX_WIDTH = 1200   # px; photos are downscaled to at most this
RASTER_RE = re.compile(r"\\includegraphics(?:\[((?:[^\[\]{}]|\{[^{}]*\})*)\])?\s*\{([^{}]*)\}")


def is_raster(source):
    return source.lstrip().startswith("\\includegraphics")


def raster_sizing(source):
    """Print sizing hint carried into the HTML: `width=0.52\\linewidth` →
    {"rel_width": 0.52}; `height=3.1cm` → {"height_cm": 3.1}; else {}."""
    m = RASTER_RE.fullmatch(source.strip())
    opts = (m and m.group(1)) or ""
    mw = re.search(r"width\s*=\s*([\d.]+)\s*\\(?:line|text|column)width",
                   opts)
    if mw:
        return {"rel_width": float(mw.group(1))}
    mh = re.search(r"height\s*=\s*([\d.]+)\s*(cm|mm)", opts)
    if mh:
        h = float(mh.group(1)) / (10 if mh.group(2) == "mm" else 1)
        return {"height_cm": h}
    return {}


def raster_trim(opts):
    """`trim={l b r t}, clip` (bp; graphicx order left-bottom-right-top) →
    an ffmpeg crop filter. Photos carry no density, so 1 bp = 1 px, which
    is exactly how pdfTeX sizes them (a 1280 px jpg is 1280 bp wide)."""
    if not re.search(r"\bclip\b", opts or ""):
        return None
    m = re.search(r"trim\s*=\s*\{?\s*([\d.]+)bp\s+([\d.]+)bp\s+([\d.]+)bp"
                  r"\s+([\d.]+)bp\s*\}?", opts)
    if m:
        l, b, r, t = (float(v) for v in m.groups())
        return f"crop=iw-{l + r}:ih-{t + b}:{l}:{t}"
    # `viewport=llx lly urx ury` (bp, bottom-left origin): the kept box is
    # (urx-llx) x (ury-lly) with its top edge at ih-ury in ffmpeg's
    # top-left coordinates.
    m = re.search(r"viewport\s*=\s*\{?\s*([\d.]+)(?:bp)?\s+([\d.]+)(?:bp)?"
                  r"\s+([\d.]+)(?:bp)?\s+([\d.]+)(?:bp)?\s*\}?", opts)
    if not m:
        raise ParseError(f"unsupported clip/trim option: [{opts}]")
    llx, lly, urx, ury = (float(v) for v in m.groups())
    return f"crop={urx - llx}:{ury - lly}:{llx}:ih-{ury}"


def build_raster(path, opts=""):
    """Transcode a photo (jpg/png) to a web-sized JPEG with ffmpeg; returns
    (jpeg_bytes, width, height). Rasters are keyed by the hash of the
    source file (+ crop) so an unchanged photo is never re-encoded."""
    src = Path(path).resolve()
    if not src.exists():
        raise ParseError(f"raster figure not found: {path}")
    filters = [f for f in (raster_trim(opts),
                           f"scale='min({RASTER_MAX_WIDTH},iw)':-2") if f]
    with tempfile.TemporaryDirectory(prefix="omimg-") as tmp:
        out = Path(tmp) / "img.jpg"
        res = _run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(src),
                    "-vf", ",".join(filters),
                    "-q:v", "3", "-pix_fmt", "yuvj420p", str(out)], tmp)
        if res.returncode != 0 or not out.exists():
            raise ParseError(f"ffmpeg failed for {path}:\n{res.stderr[-1500:]}")
        data = out.read_bytes()
    return data, *_jpeg_size(data)


def _jpeg_size(data):
    """(width, height) from the first SOF marker of a JPEG stream."""
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        seg = int.from_bytes(data[i + 2:i + 4], "big")
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                      0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            h = int.from_bytes(data[i + 5:i + 7], "big")
            w = int.from_bytes(data[i + 7:i + 9], "big")
            return w, h
        i += 2 + seg
    raise ParseError("could not read JPEG dimensions")


class FigureBuilder:
    """Builds each distinct picture once: tikzpictures compile to SVG,
    \\includegraphics photos transcode to JPEG; both land in svg_dir."""

    def __init__(self, svg_dir, url_prefix):
        self.svg_dir = Path(svg_dir)
        self.url_prefix = url_prefix.rstrip("/")
        self.cache = {}    # tikz source -> figure info dict
        self.built = {}    # tikz hash -> build_svg() result (prebuild)

    def prebuild(self, tikzs, jobs=None):
        """Compile a chapter's pictures in parallel (each build_svg runs in
        its own temp dir, so the output is byte-identical to a serial run);
        figure_info() then only writes the files. OM_FIG_JOBS overrides
        the worker count."""
        jobs = jobs or int(os.environ.get("OM_FIG_JOBS", "0")) \
            or min(8, os.cpu_count() or 1)
        todo = {}
        for tikz in tikzs:
            # Arabic pictures (lualatex) stay serial: under concurrent
            # load luaotfload shapes their labels differently run to run
            if not is_raster(tikz) and not ARABIC.search(tikz):
                h = tikz_hash(tikz)
                if not self.published(h):
                    todo.setdefault(h, tikz)
        if jobs < 2 or len(todo) < 2:
            return
        with ThreadPoolExecutor(max_workers=jobs) as pool:
            for h, result in zip(todo, pool.map(build_svg, todo.values())):
                self.built[h] = result

    def published(self, h):
        """OM_FIG_REUSE=1: the figure already in the output directory, for a
        rebuild that changes text only (a converter fix in the fragments).
        The file name is the hash of the picture's source, so a published
        file is that picture — unless the style file or the figure toolchain
        changed since, which the hash does not see: leave the variable unset
        for those."""
        path = self.svg_dir / f"fig-{h}.svg"
        if os.environ.get("OM_FIG_REUSE") == "1" and path.exists():
            return path
        return None

    def figure_info(self, tikz):
        if tikz in self.cache:
            return self.cache[tikz]
        if is_raster(tikz):
            return self.raster_info(tikz)
        h = tikz_hash(tikz)
        # identical picture, differently keyed source (whitespace): reuse
        for info in self.cache.values():
            if info["hash"] == h:
                self.cache[tikz] = info
                return info
        filename = f"fig-{h}.svg"
        if self.published(h):
            width, height = _svg_size(
                self.published(h).read_text(encoding="utf-8"))
        else:
            svg, width, height = self.built.pop(h, None) or build_svg(tikz)
            self.svg_dir.mkdir(parents=True, exist_ok=True)
            (self.svg_dir / filename).write_text(svg, encoding="utf-8")
        info = {"hash": h, "file": filename, "width": width,
                "height": height, "url": f"{self.url_prefix}/{filename}"}
        self.cache[tikz] = info
        return info

    def raster_info(self, source):
        m = RASTER_RE.fullmatch(source.strip())
        if not m:
            raise ParseError(f"malformed \\includegraphics: {source!r}")
        opts = m.group(1) or ""
        path = Path(m.group(2).strip())   # relative to the book repo root
        if not path.exists():
            raise ParseError(f"raster figure not found: {path}")
        crop = raster_trim(opts) or ""
        h = hashlib.sha1(path.read_bytes() + crop.encode()).hexdigest()[:12]
        sizing = raster_sizing(source)
        for info in self.cache.values():
            if info["hash"] == h:
                info = {k: v for k, v in info.items()
                        if k not in ("rel_width", "height_cm")}
                info.update(sizing)
                self.cache[source] = info
                return info
        filename = f"img-{h}.jpg"
        target = self.svg_dir / filename
        if target.exists():
            width, height = _jpeg_size(target.read_bytes())
        else:
            data, width, height = build_raster(path, opts)
            self.svg_dir.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        info = {"hash": h, "file": filename, "width": width,
                "height": height, "url": f"{self.url_prefix}/{filename}",
                **sizing}
        self.cache[source] = info
        return info
