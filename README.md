# fusic

factory of music

Nothing of the product is built yet: `fusic` runs, prints its version and its
help, and has the checks every later change runs.

## install

On Windows and Linux alike, install [uv](https://docs.astral.sh/uv/) and
nothing else. uv installs the Python version in `.python-version` and every
dependency.

- **Windows:** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`,
  or `winget install --id=astral-sh.uv -e`.
- **Linux:** `curl -LsSf https://astral.sh/uv/install.sh | sh`.

## set up and run

From the repository's root:

```sh
uv sync                        # the environment, from uv.lock
uv run fusic --version         # or: uv run python -m fusic --version
uv run fusic                   # prints the help
```

## test

```sh
uv run ruff check              # lint
uv run ruff format --check     # format, or `uv run ruff format` to apply it
uv run pytest                  # tests
```

CI runs the same three on Linux for every push and pull request
(`.github/workflows/ci.yml`).
