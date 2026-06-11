# python-workbench

A minimal Python workspace template for experiments: data parsing, modelling, automation POCs, and one-off scripts.

## Get started

### Prerequisites

- [uv](https://docs.astral.sh/uv/) — installs Python, manages the virtualenv, and resolves dependencies

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Environment setup

Clone the repo, then sync the project:

```bash
git clone <repo-url> python-workbench
cd python-workbench
uv sync
```

`uv sync` will:

- Install Python 3.12 (from `.python-version`) if it is not already available
- Create a `.venv` in the project root
- Install the `python-workbench` package in editable mode
- Install dev dependencies (pytest)

Activate the virtualenv manually when you need it outside `uv run`:

```bash
source .venv/bin/activate   # macOS / Linux
```

Add a runtime dependency when an experiment needs it:

```bash
uv add pandas          # adds to [project].dependencies
uv add --dev ruff      # adds to [dependency-groups].dev
```
`
### How to run scripts

Put experiment entry points in `scripts/`. Each script is a standalone file you run directly.

```bash
uv run python scripts/example.py
```

Copy `scripts/example.py` when starting a new experiment:

```bash
cp scripts/example.py scripts/parse_weather_data.py
```

Scripts can import shared code from the installed package:

```python
from python_workbench.config import INPUT_DIR, OUTPUT_DIR
```

Run any script the same way:

```bash
uv run python scripts/parse_weather_data.py
```

In VS Code / Cursor, use the **Python: Example Script** launch config, or **Python: Current File** for any open script.

### How to organize modules

Reusable logic lives under `src/python_workbench/`. Scripts in `scripts/` should stay thin — parse args, call library code, write output.

```
python-workbench/
├── src/python_workbench/   # importable library code
│   ├── config/             # paths, settings
│   └── ...                 # add domains as needed (parsing/, models/, etc.)
├── scripts/                # one-off experiment entry points
├── tests/                  # pytest tests for library code
├── input/                  # local input data (gitignored contents)
└── output/                 # generated artifacts (gitignored contents)
```

Guidelines:

- **Library code** → `src/python_workbench/<domain>/` — anything you want to import and test
- **Experiment scripts** → `scripts/<descriptive_name>.py` — run once or iterate on an idea
- **Input / output data** → `input/` and `output/` at the repo root (contents are gitignored; directories are tracked)
- **Config and paths** → `python_workbench.config` exposes `PROJECT_ROOT`, `INPUT_DIR`, `OUTPUT_DIR`

Example layout after a few experiments:

```
src/python_workbench/
├── config/
├── parsing/
│   ├── __init__.py
│   └── geojson.py
└── models/
    ├── __init__.py
    └── baseline.py

scripts/
├── example.py
├── parse_geojson.py
└── train_baseline.py
```

### How to run tests

Tests cover library code in `src/`, not individual scripts.

```bash
uv run pytest
```

Run a single file or test:

```bash
uv run pytest tests/test_paths.py
uv run pytest -k test_project_root
```

Add tests alongside new modules: `tests/test_parsing.py` for `src/python_workbench/parsing/`.

## Quick reference

| Task | Command |
|------|---------|
| Install / update env | `uv sync` |
| Run a script | `uv run python scripts/<name>.py` |
| Run tests | `uv run pytest` |
| Add a dependency | `uv add <package>` |
| Add a dev dependency | `uv add --dev <package>` |
| Update lock file | `uv lock` |
