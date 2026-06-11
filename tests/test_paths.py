from pathlib import Path

from python_workbench.config import INPUT_DIR, OUTPUT_DIR, PROJECT_ROOT


def test_project_root_is_repo_root() -> None:
    assert (PROJECT_ROOT / "pyproject.toml").exists()
    assert (PROJECT_ROOT / "src" / "python_workbench").is_dir()


def test_data_dirs_are_under_project_root() -> None:
    assert INPUT_DIR == PROJECT_ROOT / "input"
    assert OUTPUT_DIR == PROJECT_ROOT / "output"
    assert isinstance(INPUT_DIR, Path)
    assert isinstance(OUTPUT_DIR, Path)
