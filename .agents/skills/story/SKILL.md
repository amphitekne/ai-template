---
name: story
description: Refine one selected story into observable acceptance criteria, explicit scope and a small plan for approval; not feature-wide backlog planning or implementation.
---

# Story

Run only when explicitly invoked by the human. Never activate another skill automatically; suggest the next skill and wait for the human to invoke it.

Read the project agreement and [workflow](../../../docs/workflow.md). Inspect existing behavior and stories. Ask only for missing decisions affecting acceptance or scope.

Refine one selected backlog item or user-supplied story just before implementation. Use the [story template](../../../templates/story.md). Keep it an independently demonstrable vertical slice from user entry point to observable outcome. Include explicit In Scope and Out of Scope and a few Given/When/Then criteria describing behavior, not implementation. Aim for two or three criteria and a short plan; these are sizing signals, not mandatory quotas. If the story contains several independent outcomes, propose a split rather than expanding the document.

Mark how each criterion will be checked: fast automation, human verification, or both. Prefer unit tests for logic and focused integration for risks requiring a real boundary; plan complete user flows and visual/deployment checks for human validation by default. Do not equate a vertical slice with automated E2E. Identify material risks left for the human; propose broader automation only when justified or required by project rules. Include dependencies or open decisions only when relevant. Present the story and minimal plan for navigator acceptance or revision. Save the approved story and link it from its backlog item if one exists, without invoking backlog. Do not write tests or implementation. Offer pair as the next step and wait for explicit invocation.

Consult the target project's technical guide through the workflow. Identify rules relevant to the proposed slice and surface conflicts or needed exceptions before acceptance. Do not prescribe a new stack or turn a local pattern into a project rule. Link rule IDs in the story only when useful.
