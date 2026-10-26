---
name: story
description: Propose or refine small end-to-end stories from feature intent before acceptance; not for backlog status or implementation.
---

# Story

Run only when explicitly invoked by the human. Never activate another skill automatically; suggest the next skill and wait for the human to invoke it.

Read the project agreement and [workflow](../../../docs/workflow.md). Inspect existing behavior and stories. Ask only for missing decisions affecting acceptance or scope.

Use the [story template](../../../templates/story.md). Each story delivers an independently demonstrable vertical slice from user entry point to observable outcome. Include explicit In Scope and Out of Scope, testable criteria and edge cases, dependencies, and human validation steps. Label assumptions as proposals. Prefer the smallest readable solution.

Present proposals for navigator acceptance or revision. Do not silently accept them or start tests. Hand accepted stories to backlog.

Consult the target project's technical guide through the workflow. Identify rules relevant to the proposed slice and surface conflicts or needed exceptions before acceptance. Do not prescribe a new stack or turn a local pattern into a project rule. Link rule IDs in the story only when useful.
