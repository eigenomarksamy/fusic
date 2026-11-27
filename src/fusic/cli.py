"""The `fusic` command."""

import argparse
from collections.abc import Sequence

from fusic import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fusic",
        description="fusic is a factory of music.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"fusic {__version__}",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command and return its exit code."""
    parser = build_parser()
    parser.parse_args(argv)
    # nothing to do yet: without arguments, the command prints its help.
    parser.print_help()
    return 0
