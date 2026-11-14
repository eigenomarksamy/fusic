@../meta-eigenomar/standards/claude-ecosystem.md

# fusic: Claude instructions

fusic is a factory of music. Its development starts from scratch: nothing is
built yet, and nothing deploys.

## commands

There is no code yet, so there is nothing to build or test. The first ticket
that adds code chooses the stack. When it lands, list its setup, build, test
and run commands here, each working on Windows and Linux, along with what to
run before pushing.

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

There is no CI, no release process and no deployment yet. Once one exists,
record it here and in `project.yaml` in the same change.
