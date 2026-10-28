# Working agreement

Apply this agreement to work in this repository, whether it contains one application or multiple packages. Do not create custom agents or delegate to subagents.

Use the same instructions, guides, presets and `.agents/skills/` with Codex or Pi Coding Agent. Human skill invocation uses `$name` in Codex and `/skill:name` in Pi; translate examples to the active agent's syntax. Never interpret a command example or a workflow handoff as a human invocation. Resolve document links relative to the containing file, and run project commands from their documented Git root/package working directory rather than the skill directory.

The human is the navigator; the AI is the driver. Follow [the workflow](docs/workflow.md). Use small end-to-end stories with explicit In Scope and Out of Scope. Prefer readability and KISS over optimization, speculative abstractions, or unrelated cleanup. Preserve useful content and user edits; inspect files before changing them. Distinguish confirmed requirements from assumptions.

Tests require explicit human approval every time, then a separate RED commit before GREEN. Approved tests and their execution dependencies are immutable during GREEN and optional refactoring. Incorrect tests block GREEN until corrected, explicitly reapproved, and committed. Human behavioral validation precedes the second, implementation commit. General implementation authorization, silence, and passing checks do not replace these gates. The human commits or authorizes the AI to commit. Stage only intended files.

Keep collaboration rules here and in the workflow, task procedures in skills, and repository-specific decisions in the project guide. Keep documentation lightweight and add resources only for concrete uses. Run checks appropriate to the change and report verification limits. Reviews report findings; edit only when requested.

Default to fast unit tests and focused integration only where a relevant failure requires it. Docker builds, full deployment stacks and automated E2E are outside the normal loop unless explicitly requested or required by accepted project rules. Agree iteration and closing checks with the tests; the human validates complete user flows. Follow the workflow's execution/evidence rules instead of repeatedly running every available suite.

Consult the [project guide](docs/project-guide.md) for technical rules relevant to the task. Apply the [guide evolution procedure](docs/workflow.md#evolving-project-guidance): propose evidence-based changes, obtain navigator acceptance, and update the active rules without triggering automatic migrations. Technical guidance does not override the collaboration or test-contract gates.

Keep stack choices, repository layout, language/style conventions, test commands, and security requirements in that guide or linked scoped guides. In a monorepo, consult only the shared guidance and the package guides relevant to the task. Do not assume all packages share the same stack or conventions. Missing guidance is not permission to invent requirements; resolve only decisions that affect the current work.

Use the root guide's scope index to find applicable package guides. Consult guidance for every affected package, including shared code and integration boundaries; revisit the selection if the change reaches another package. Local guides complement shared rules; a narrower scope alone does not authorize overriding them. Resolve conflicts with the navigator before the affected step. For independent Git repositories, use each repository's own entry point and workflow as described in [repository boundaries](docs/workflow.md#repository-boundaries).
