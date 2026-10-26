---
name: refactor
description: Simplify passing code while preserving behavior and its approved test contract; for readability, not features or test repair.
---

# Refactor

Run only when explicitly invoked by the human. Never activate another skill automatically; suggest the next skill and wait for the human to invoke it.

Read the story and [workflow](../../../docs/workflow.md). Require a passing relevant baseline (focused run or valid reusable evidence) and verified committed test contract; otherwise propose returning to pair. Do not run every suite just to establish a baseline.

Explain a concrete readability problem and the smallest improvement. Preserve scope, observable behavior, tests and execution dependencies. Favor clear names and direct control flow. Avoid speculative abstractions, unrelated cleanup, and optimization without evidence.

Apply relevant project-guide conventions within the approved scope. Surface obsolete rules or useful lessons as proposals; obtain navigator acceptance before deviating or updating guidance. Do not use a changed convention as authorization for a broad migration.

Change in small steps using the approved focused iteration commands. After the final relevant change, verify integrity and run the agreed closing checks, reusing results only under the workflow's validity rules. Docker/E2E are not default refactor checks. Wrong tests block refactoring and require renewed approval. Return automated results, remaining risks and full-flow checks for human validation. Refactoring in an active slice belongs in its implementation commit. A later standalone refactor needs a bounded story and validation; do not manufacture failing tests for unchanged behavior or rewrite completed history.

Stop after two consecutive fix attempts on the same regression without meaningful progress; show the evidence and ask for navigator direction. Keep the handoff to a short description of the simplification, check results and remaining human validation; do not create a separate refactor report.
