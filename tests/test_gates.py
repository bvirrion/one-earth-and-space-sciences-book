"""The ledger gate and the exercise-calibration gate."""
import os
import pathlib
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
import check_exercise_calibration as cal  # noqa: E402
import check_ledger  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent


def test_repo_ledger_is_clean():
    errors, nrows = check_ledger.check([str(ROOT / "parts")])
    assert errors == []
    assert nrows > 100


def test_ledger_unknown_id_and_free_text(tmp_path):
    f = tmp_path / "x.tex"
    f.write_text("% ledger: const:G, earth:mass (rounded; see text)\n"
                 "% ledger: nosuch:row\n"
                 "% ledger: not an id\n")
    errors, _ = check_ledger.check([str(f)])
    assert len(errors) == 2
    assert "nosuch:row has no row" in errors[0]
    assert "not a ledger id" in errors[1]


def _chapter(stars, problem_items=None):
    s = "".join("\\begin{exercise}[$%s$]\\label{exo:x:%d}\\end{exercise}\n"
                % ("\\star" * k, i) for i, k in enumerate(stars))
    if problem_items is not None:
        s += ("\\begin{problem}[{Weekend problem}]\\begin{enumerate}"
              + "\\item q\n" * problem_items
              + "\\item with parts \\begin{enumerate}\\item a \\item b\\end{enumerate}\n"
              + "\\end{enumerate}\\end{problem}\n")
    return s


def test_calibration_bands(tmp_path):
    f = tmp_path / "01-x.tex"
    f.write_text(_chapter([1] * 4 + [2] * 5 + [3] * 3, 24))     # 25 questions
    assert cal.check_file(f, cal.band("bachelor-2")) == []
    assert cal.check_file(f, cal.band("grade-11"))               # 12 exercises, wrong ramp
    f.write_text(_chapter([1] * 4 + [3] + [2] * 5 + [3] * 2, 24))
    assert any("decrease" in m for m in cal.check_file(f, cal.band("bachelor-1")))
    f.write_text(_chapter([1] * 8 + [2] * 2, 5))
    assert cal.check_file(f, cal.band("grade-3")) == ["this band has no weekend problem"]
    f.write_text("\\chapter{x}\n\\noindent\\emph{To be written.}\n")
    assert cal.check_file(f, cal.band("bachelor-3")) == []       # placeholder skipped


def _run_gates(tmp_path, body):
    """Run tools/gates.sh on a one-chapter grade-7 tree built in tmp_path."""
    import subprocess
    import tempfile
    tmp_path = pathlib.Path(tempfile.mkdtemp(dir=tmp_path))
    for d in ("tools", "sources", "styles"):
        (tmp_path / d).symlink_to(ROOT / d)
    (tmp_path / "images" / "book1" / "ai").mkdir(parents=True)
    sol = tmp_path / "parts" / "grade-7" / "solutions"
    sol.mkdir(parents=True)
    (tmp_path / "parts" / "grade-7" / "01-x.tex").write_text(
        "\\chapter{X}\\label{ch:g7:x}\n" + body + "\n\\noindent\\emph{To be written.}\n")
    (sol / "01-x.tex").write_text("\\section*{x}\n")
    r = subprocess.run(["bash", "tools/gates.sh", "grade-7"], cwd=tmp_path,
                       capture_output=True, text=True)
    return r.returncode, r.stdout


def test_gate_observation_only(tmp_path):
    code, out = _run_gates(tmp_path, "Go to the quarry and hammer the limestone.")
    assert code == 1 and "field activity" in out


def test_gate_observation_only_allows_warnings_and_professionals(tmp_path):
    code, out = _run_gates(tmp_path, "Never climb a cliff. Geologists visit outcrops with a hammer.\n"
                                     "Never look at the Sun.")
    assert code == 0, out


def test_gate_sun(tmp_path):
    code, out = _run_gates(tmp_path, "At noon, look at the Sun through the window.")
    assert code == 1 and "Sun" in out


def test_gate_dated_box_needs_its_year(tmp_path):
    code, out = _run_gates(tmp_path, "\\begin{dated}\nx\n\\end{dated}")
    assert code == 1 and "dated box" in out


def test_gate_pgf_lists_are_not_drafty_dots(tmp_path):
    code, out = _run_gates(tmp_path, "\\begin{axis}[xtick={-180,-90,...,180}]\\end{axis}")
    assert code == 0, out
    code, out = _run_gates(tmp_path, "And then...")
    assert code == 1 and "drafty" in out
