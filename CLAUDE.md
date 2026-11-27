@../meta-eigenomar/standards/claude-ecosystem.md

# fusic: Claude instructions

fusic is a factory of music. Its development starts from scratch: a Python
project managed with `uv` runs and is checked, with none of the product yet,
and nothing deploys.

## commands

Each works on Windows and Linux, from the repository's root, and needs only
`uv`.

- **Setup:** `uv sync`, which installs the Python in `.python-version` and the
  locked dependencies into `.venv/`.
- **Run:** `uv run fusic`, or `uv run python -m fusic`, the same entry point
  (`src/fusic/cli.py`). `--version` prints the version, and no arguments print
  the help.
- **Lint:** `uv run ruff check` and `uv run ruff format --check`.
  `uv run ruff format` applies the format.
- **Test:** `uv run pytest`.
- **Before pushing:** all three checks, `uv run ruff check`,
  `uv run ruff format --check` and `uv run pytest`, which CI runs too. After
  changing dependencies, commit `uv.lock` with `pyproject.toml`: CI runs
  `uv sync --locked`, which fails when they differ.

The tests pass when started from `c:\` as well as from `C:\`.

## plan

[docs/plan.md](docs/plan.md) is the plan. Ticket ids are a lane prefix and a
number (EO1) and are never reused or renumbered. Each ticket has a stable
anchor, its id in lowercase, above its heading. When work ships, update the
ticket's status in the index, add a result with the commit, and add a line to
the log. This repository is public, so confidential work never goes in the
plan or anywhere else here.

## design

There is no design yet. When the first tickets settle the stack and layout,
record them here or in a document under `docs/`, and point `project.yaml` at
that document in the same change.

## delivery

CI is GitHub Actions, `.github/workflows/ci.yml`: on every push and pull
request, one job on `ubuntu-latest` runs `uv sync --locked`, ruff's lint and
format check, and pytest, and ends with a summary of each step's outcome and
every failure. It covers Linux, and local development covers Windows.

There is no release process and no deployment yet. Once one exists, record it
here and in `project.yaml` in the same change.
