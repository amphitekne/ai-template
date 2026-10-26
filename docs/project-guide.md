# Project guide

This guide applies to the reusable instruction templates in this repository. Target products define their own stack and rules using the [guide template](../templates/project-guide.md); no application stack is selected here.

## Restrictions

- R1 — ...

## Conventions

- C1 — Instructions and resources: prefer concise, self-contained guidance, readable minimal solutions, and resources with concrete uses. Keep shared rules in AGENTS.md and the workflow; link rather than duplicate them. Reason: reduce drift and unnecessary context.
- C2 — Template maintenance: use lowercase hyphenated folder names. Each skill needs frontmatter with `name` matching its folder and a distinct `description`. Check relative links, distinguishable triggers, and absence of unfinished instructions. Execute changed scripts and meaningful failure-path checks. Reason: keep discovery and reuse reliable.
- C3 — Python tooling: keep the contract verifier dependency-free beyond Python 3 and Git; use standard-library regression tests for meaningful integrity behavior. Reason: keep adoption lightweight. Relevant check: `python -m unittest discover -s tests -v`.

## Accepted changes

The navigator accepted adding an evolving technical guide in this chat on 2026-10-26, following the proposal for restrictions, conventions, bounded experiments, and explicit acceptance of rule changes. It applies to new work and maintenance of touched instructions. No bulk migration is authorized by this decision.

The navigator clarified that AGENTS.md must remain repository-agnostic so this template can initialize individual repositories and monorepos. Template-maintenance rules belong in this guide; target projects replace them with their own accepted decisions.
