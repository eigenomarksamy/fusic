# fusic plan

fusic is a factory of music. Its development starts from scratch: nothing is
built yet, and nothing is planned beyond this repository's ecosystem
onboarding (EO1–EO6), of which only EO5 is open: it waits on the first code,
and its adoption of the ecosystem's standards (DOC1, SCM1). The first release's tickets go here, in a lane of their
own, once they are planned.

## How this plan works

- **Tickets.** Every ticket has an id, a lane prefix and a number, which is
  never reused or renumbered. A split ticket keeps its number and adds a
  letter (EO4a, EO4b). Each ticket has a stable anchor, its id in lowercase
  (`#eo1`), above its heading, which doesn't change when the heading does.
- **Lanes.**

  | Prefix | Lane |
  | --- | --- |
  | EO | Ecosystem onboarding |
  | DOC | The product's documents: vision, architecture, design, testing strategy, and verification and validation |
  | SCM | Source control and delivery: CI, branching, protection, releases and versioning |

  The session that plans the first release adds its lane to this table, with
  a prefix other than EO. The ecosystem's shared rules, which `CLAUDE.md`
  imports, say what to check before adding a lane.
- **Each ticket** says what to do, what it needs, and when it is done. Its
  "done when" is its acceptance criteria. Its size is on the ecosystem's
  scale, the same value as its issue's `Size` in the ecosystem's GitHub
  Project: xxs takes minutes, xs under an hour, s an hour or two, m about a
  session, l two or three, xl four to six and xxl more. tbd means an open
  decision or work not yet planned decides it. A change to one is made to the
  other in the same session.
- **Issues.** Every open ticket gets one GitHub issue in this repository. The
  issue's title starts with the ticket's id, and its body links the ticket's
  anchor here without copying it. The ticket holds the scope and history, and
  the issue holds status, priority and blockers ([EO6](#eo6)).
- **Adding work.** New work goes here as a ticket in a lane, or as a row under
  [Parked](#parked) until it is ready to plan. This repository is public, so
  confidential work never goes in this file. The ecosystem's shared rules say
  where it goes.
- **When work ships,** update the ticket's status in the index, add a result
  with the commit to the ticket, and add a line to the [log](#log).

## Index

| Ticket | Title | Size | Needs | Status |
| --- | --- | --- | --- | --- |
| [EO1](#eo1) | `project.yaml` | s | none | done |
| [EO2](#eo2) | `CLAUDE.md` with the shared rules | s | none | done |
| [EO3](#eo3) | Confidential work stays out | s | none | done |
| [EO4](#eo4) | `.gitattributes` with LF line endings | s | none | done |
| [EO5](#eo5) | Linux and the lowercase drive letter | tbd | the first ticket that adds code | todo |
| [EO6](#eo6) | An issue for every open ticket | s | the owner's approval | done |
| [DOC1](#doc1) | The product's documents | tbd | `meta-eigenomar` ST1 | todo |
| [SCM1](#scm1) | The ecosystem's SCM strategy | tbd | `meta-eigenomar` ST2 | todo |

## Parked

Ideas, not tickets: a row has no id and no issue until it is promoted to a
ticket. Nothing is parked yet.

## Ecosystem onboarding

fusic is one of the eigenomar ecosystem's repositories, which share a
contract: a `project.yaml` manifest, shared Claude rules that `CLAUDE.md`
imports, and one issue per open ticket on the ecosystem's GitHub Project.

**Goal.** Make fusic discoverable and coordinated in the ecosystem without
changing how it is built or delivered.

**Stays as it is.**

- **Build, tests, CI, releases and deployment:** none yet. The first tickets
  choose the stack, and how fusic builds, tests, releases and deploys stays
  this repository's own choice.
- **Branching:** work lands on `main`.
- **Documents:** `README.md`, this plan and `CLAUDE.md`, where they are.

### Steps

Each step is small and independent, and can be done between feature work.

<a id="eo1"></a>

#### EO1 · `project.yaml` · done

- **Done when:** a manifest at the root points at the documents that exist,
  and the ecosystem's validator passes it.
- **Result:** done 2026-11-14. It points at this plan, with status `active`
  and no CI, releases or deployment, and `links.deployment` stays `null`
  until fusic is deployed. Update it in the same change that adds a document,
  CI or a deployment. `a743c2f`.

<a id="eo2"></a>

#### EO2 · `CLAUDE.md` with the shared rules · done

- **Done when:** the first line of `CLAUDE.md` imports the ecosystem's shared
  rules, and the rest says what the repository is and where the plan is. Once
  there is code, it also says how to build and test without the import.
- **Result:** done 2026-11-14, from the ecosystem's template. Sessions here
  haven't committed, so it grants no standing approval for commits.
  `a743c2f`.

<a id="eo3"></a>

#### EO3 · Confidential work stays out · done

- **Done when:** [How this plan works](#how-this-plan-works) says that
  confidential work never goes in this file.
- **Result:** done 2026-11-14. Nothing in this repository is confidential, so
  nothing moved. `a743c2f`.

<a id="eo4"></a>

#### EO4 · `.gitattributes` with LF line endings · done

- **Do:** add `.gitattributes` with `* text=auto eol=lf`, then run
  `git add --renormalize .`. `README.md` is already LF in the index, so this
  should stage nothing. If it stages anything, commit that on its own.
- **Needs:** nothing.
- **Done when:** `.gitattributes` is committed, and `git ls-files --eol` shows
  every tracked text file as `i/lf`.
- **Result:** done 2026-11-14. `.gitattributes` holds `* text=auto eol=lf`,
  and `git ls-files --eol` shows all four tracked files as `i/lf`, so
  `git add --renormalize .` has nothing to stage.

<a id="eo5"></a>

#### EO5 · Linux and the lowercase drive letter · todo

- **Do:** there is nothing to run yet. Once the first ticket adds code and
  tests, record here what covers Linux: a CI job on `ubuntu-latest`, a Linux
  deployment build, or an accepted gap. Also check that the tests pass when
  started from a lowercase drive letter (`c:\`), as VS Code opens folders,
  since some tools break on the difference. The ecosystem's conventions give
  the known fixes.
- **Needs:** the first ticket that adds code. It isn't planned yet, so until
  it is, this ticket's issue stays in the backlog with no blocked-by link.
- **Done when:** this section says what runs the tests on Linux, and the
  tests pass when started from `c:\` as well as from `C:\`.

<a id="eo6"></a>

#### EO6 · An issue for every open ticket · done

- **Do:** open one issue in this repository for every open ticket (EO4 and
  EO5 on 2026-11-14, and the first release's tickets once they are planned)
  and add each to the ecosystem's GitHub Project. The title is
  `<id>: <title>`, as in `EO4: .gitattributes with LF line endings`. The
  body's first line links the ticket's anchor on `main` and copies nothing.
  Each need becomes a blocked-by link, EO5's to the first ticket that adds
  code.
- **Needs:** the owner's approval. This repository is public, so the owner
  sees each issue's text before it is written.
- **Done when:** every open ticket has exactly one issue in the Project, with
  its status, priority and work type set, and its needs are blocked-by links.
- **Result:** done 2026-11-14, with the owner's approval of the text. EO5 is
  #1, in the Project as `backlog` at P2, `infra`. EO4 was done first, so it
  needed none. EO5's need isn't a ticket yet, so #1 has no blocked-by link:
  the session that plans the first code ticket adds it. Tickets added later
  get their issues as they are added ([How this plan works](#how-this-plan-works)).

### Open questions

Answered by the owner on 2026-11-14:

1. **When to run EO6:** now. EO4 was done first, so only EO5 got an issue,
   #1, which gets its blocked-by link once the first code ticket exists.
2. **Fields for EO6:** EO5 at P2, as `infra`, in the backlog.

## Ecosystem standards

The ecosystem's contract, in `meta-eigenomar`, is adding two standards that
every repository adopts: the documents each one keeps, and how each one
manages its source and delivers it. DOC1 and SCM1 adopt them here, each once
its standard is designed. Until then, their issues stay in the backlog. With
no code yet, both can land before the first release is planned, so its first
code starts with them.

<a id="doc1"></a>

### DOC1 · The product's documents · tbd

- **Do:** write this repository's product vision, architecture, design,
  testing strategy, and verification and validation (V&V) documents, in the
  shape the ecosystem's document standard sets. Nothing exists yet beyond the
  README's line that fusic is a factory of music, so the vision comes first,
  and the architecture, design and testing strategy say what the first
  release will build and how it will be checked. A document the first
  release can't settle yet says so, and what settles it.
- **Needs:** the ecosystem's document standard (`meta-eigenomar` ST1).
- **Done when:** each of the five documents exists, or names the file or
  section that holds it, and follows the standard's outline. `project.yaml`
  names them under the standard's keys, and the ecosystem's validator passes.
  Nothing in them is confidential, since this repository is public.

<a id="scm1"></a>

### SCM1 · The ecosystem's SCM strategy · tbd

- **Do:** adopt the ecosystem's SCM strategy through its adoption checklist:
  CI, branching, protection of `main`, versioning and releases, the health
  report and dependency updates. There is no code, CI or deployment yet, so
  what needs code, such as the CI job, is set up with the first ticket that
  adds code, and the CI job is what [EO5](#eo5) records as covering Linux.
- **Needs:** the ecosystem's SCM strategy (`meta-eigenomar` ST2).
- **Done when:** every item on the checklist is applied here, recorded here as
  an exception the strategy allows, with its reason, or, where it needs code,
  named in the first code ticket's done-when. `project.yaml`'s `delivery` and
  `CLAUDE.md` say what runs, and the ecosystem's validator passes.

## Log

- 2026-11-18 · plan · Added DOC1 and SCM1, in two new lanes, at the owner's
  request: this repository's adoption of the ecosystem's document standard and
  SCM strategy, which are designed in `meta-eigenomar`. Each needs its
  standard, so its issue waits in the backlog.
- 2026-11-14 · EO4, EO6 · EO4 is done: `.gitattributes` with LF line endings,
  which staged nothing. EO6 is done: EO5, the one open ticket, is issue #1 in
  the ecosystem's Project, in the backlog until the first code ticket exists.
  EO1–EO3's results name `a743c2f`. Only EO5 is left of the onboarding.
- 2026-11-14 · plan · Created by the ecosystem onboarding run. It holds
  EO1–EO6. EO1–EO3 are done: `project.yaml`, which validates, `CLAUDE.md`,
  which imports the shared rules, and the confidential-work line above.
  Nothing else in the repository changed.
