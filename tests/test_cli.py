import subprocess
import sys

import pytest

from fusic import __version__
from fusic.cli import main


def test_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exit_info:
        main(["--version"])
    assert exit_info.value.code == 0
    assert capsys.readouterr().out.strip() == f"fusic {__version__}"


def test_help_without_arguments(capsys: pytest.CaptureFixture[str]) -> None:
    assert main([]) == 0
    out = capsys.readouterr().out
    assert out.startswith("usage: fusic")
    assert "--version" in out


def test_python_m_runs_the_same_entry_point() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "fusic", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == f"fusic {__version__}"
