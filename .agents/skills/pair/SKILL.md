---
name: pair
description: Implement an accepted slice as AI driver with a human navigator, through RED approval and test commit, GREEN, human validation and separate implementation commit.
---

# Pair

Run only when explicitly invoked by the human. Never activate another skill automatically; suggest the next skill and wait for the human to invoke it. Optional refactor requires the human's explicit invocation of that skill.

Read the story, agreement, and [workflow](../../../docs/workflow.md). Inspect the worktree and baseline. Explain small reviewable steps and consequential decisions. Stop at unresolved decisions or gates while completing independent preparation.

## RED

Map criteria to meaningful end-to-end tests and negative cases. Run existing tests first. Write tests without implementing the feature; demonstrate failures caused by missing behavior rather than broken setup. Protect tests, helpers, fixtures, snapshots, runner configuration and execution dependencies.

Present exact diff, protected paths, commands, collection evidence, coverage mapping and expected failures for explicit human approval. Wait. The human commits or authorizes the AI to commit tests separately. Verify that commit matches approved content and excludes implementation and unrelated work. Record approval and full hash; seal and verify the contract before GREEN.

## GREEN and delivery

Implement only the accepted slice with readable minimal code. Never edit, skip, weaken, delete, relocate, or bypass approved tests or execution dependencies. Verify the contract before and after checks and immediately before the implementation commit. Run approved commands and relevant regressions; compare collection with RED evidence.

Incorrect tests or changed scope block GREEN and require renewed approval per the workflow. Optional refactor preserves behavior and contract. Report results, limitations, and human demonstration steps. Wait for human validation and commit authorization, or the human's commit. Only after validation make the separate implementation commit; verify content and record evidence. Passing tests alone never means Done.

Apply relevant target-project guide rules before editing. If development reveals a reusable lesson, propose the smallest rule change with evidence and impact using the workflow's evolution procedure. Obtain navigator acceptance before adopting it or making an exception. Update guidance only when it adds a useful decision; do not require documentation changes on every slice. Guide changes never bypass protected tests or expand scope.
