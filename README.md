# templating-ai — v5

Five English-language skills for human-led pair programming. The human navigates; the AI drives. No custom subagents.

Skills are user-invoked only: use `$story`, `$backlog`, `$pair`, `$refactor`, or `$review`. Each skill's `agents/openai.yaml` sets `policy.allow_implicit_invocation: false`; copy these files with the skills. The AI may recommend another skill but waits for your explicit invocation. These `agents/` directories contain skill configuration, not custom subagents. Start a new session to reload changed invocation settings if needed.

| Skill | Purpose |
| --- | --- |
| [story](.agents/skills/story/SKILL.md) | Propose small end-to-end stories |
| [backlog](.agents/skills/backlog/SKILL.md) | Record accepted stories and priorities |
| [pair](.agents/skills/pair/SKILL.md) | RED approval and commit, GREEN, validation and implementation commit |
| [refactor](.agents/skills/refactor/SKILL.md) | Optionally simplify passing code |
| [review](.agents/skills/review/SKILL.md) | Check correctness, scope, integrity, and clarity |

Copy all five skills, docs/, templates/, scripts/, and the relevant AGENTS.md agreement into a target repository, preserving relative paths and merging existing conventions. Reopen a Codex session if new skills are not discovered.

Use this repository as a starting template for a single repository or a monorepo. Keep AGENTS.md as the reusable working agreement. Replace `docs/project-guide.md` with the target project's accepted decisions using the guide template; its current template-maintenance rules do not transfer to the new product. Adapt this README to the new project. Keep the shared workflow, skill procedures, and contract tooling available at their linked paths.

Example requests: “Use $story to propose slices”; “Use $backlog to record these accepted stories”; “Use $pair for S-001”; “Use $refactor on this passing implementation”; “Use $review on this diff.” Proposals do not authorize implementation.

Read the [workflow](docs/workflow.md). Use the [backlog](templates/backlog.md) and [story](templates/story.md) templates in the target project. No product requirements or backlog entries are invented here.

The contract verifier requires Python 3 and Git, with no third-party packages. Run regression checks with `python -m unittest discover -s tests -v`. It verifies content integrity, not human approval or test quality.

## Evolving technical guidance

AGENTS.md defines collaboration; `docs/project-guide.md` holds the project's technical restrictions, conventions, and bounded experiments. This repository's [guide](docs/project-guide.md) describes template maintenance. When adopting the system, replace it with product-specific confirmed rules using the [guide template](templates/project-guide.md), and merge links into the target AGENTS.md. Define stack, style, tests, and security only as decisions are made; no complete up-front specification is required.

For a monorepo, the project guide links package-specific guides when needed and identifies their scope. Keep common rules centralized and load only guidance relevant to the affected packages. A single repository can use just the project guide. No package-guide directory is required until there is distinct guidance to store.

The driver proposes rule changes from real evidence; the navigator accepts direction and exceptions. Follow the [evolution procedure](docs/workflow.md#evolving-project-guidance). Changes specify how existing code is treated and do not start automatic migrations. Keep substantial decision rationale in separate files only when needed. The five existing skills handle this; no additional phase or skill is required.
