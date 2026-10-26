---
name: refactor
description: Simplify passing code while preserving behavior and its approved test contract; for readability, not features or test repair.
---

# Refactor

Run only when explicitly invoked by the human. Never activate another skill automatically; suggest the next skill and wait for the human to invoke it.

Read the story and [workflow](../../../docs/workflow.md). Require a passing baseline and verified committed test contract; otherwise return to pair.

Explain a concrete readability problem and the smallest improvement. Preserve scope, observable behavior, tests and execution dependencies. Favor clear names and direct control flow. Avoid speculative abstractions, unrelated cleanup, and optimization without evidence.

Apply relevant project-guide conventions within the approved scope. Surface obsolete rules or useful lessons as proposals; obtain navigator acceptance before deviating or updating guidance. Do not use a changed convention as authorization for a broad migration.

Change in small steps; verify integrity and rerun approved tests plus relevant regressions. Wrong tests block refactoring and require renewed approval. Return results for human validation. Refactoring in an active slice belongs in its implementation commit. A later standalone refactor needs a bounded story and validation; do not manufacture failing tests for unchanged behavior or rewrite completed history.
