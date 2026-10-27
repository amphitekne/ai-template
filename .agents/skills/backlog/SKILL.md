---
name: backlog
description: Split feature intent into a short backlog of vertical stories and maintain accepted work; leave detailed criteria and implementation to story and pair.
---

# Backlog

Run only when explicitly invoked by the human. Never activate another skill automatically; suggest the next skill and wait for the human to invoke it.

Read the [workflow](../../../docs/workflow.md), relevant project guidance, and existing backlog. Use the [backlog template](../../../templates/backlog.md). Preserve IDs, useful decisions, and user edits.

From the user's intent, propose a short list of one-line stories delivering independent end-to-end value. Start with the smallest usable slice; add infrastructure inside the first slice that needs it. Ask about consequential unknowns when relevant, without inventing requirements or designing the architecture. Do not expand every item into criteria or implementation plans. For maintenance work, state its concrete outcome rather than inventing a fictional user.

Present proposals in the conversation; record only navigator-accepted items in the backlog with stable IDs and real dependencies. Priorities are optional and follow the navigator. Create a detailed story file only when that item is selected for refinement through an explicit invocation of story; link it then. The story owns delivery status once it exists; the backlog need not mirror every intermediate state.

No GREEN without explicit approval and a committed verified RED contract; no Done without human validation and the separate implementation commit. Record blockers and next decisions. Never invent requirements, approvals, or evidence. Backlog maintenance does not authorize implementation or external actions.

When an accepted technical-guide change affects pending work, reconcile affected stories and dependencies. Record migration stories only when the navigator accepts them; a new convention does not automatically authorize rewriting existing code.

When the human asks to review captured ideas, read the existing ideas inbox (default `docs/ideas.md`). Do not sweep it or promote entries automatically on every backlog invocation. Present the selected ideas for acceptance, deferral or dismissal without treating them as requirements. Accepted ideas become appropriately small backlog items with a source idea ID/link; only after that decision mark the inbox entry Promoted with its backlog reference. Keep deferred entries Pending and mark Dismissed only on the navigator's decision. Preserve notes and IDs rather than deleting history. Check existing references before creating duplicate work. This updates the inbox and backlog within the requested review; it does not invoke capture or authorize implementation.
