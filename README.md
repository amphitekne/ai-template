# templating-ai — v5

Six skills for human-led pair programming and lightweight idea capture. The human navigates; the AI drives. No custom subagents.

Compatible with Codex and Pi Coding Agent using the same files. Skills are user-invoked only. Each SKILL.md sets `disable-model-invocation: true` for Pi; each skill's `agents/openai.yaml` retains `policy.allow_implicit_invocation: false` for Codex. Copy both with the skills. The AI may recommend another skill but waits for your explicit invocation. These `agents/` directories contain skill configuration, not custom subagents.

## Codex and Pi Coding Agent

| Skill | Codex | Pi |
| --- | --- | --- |
| Capture | `$capture` | `/skill:capture` |
| Backlog | `$backlog` | `/skill:backlog` |
| Story | `$story` | `/skill:story` |
| Pair | `$pair` | `/skill:pair` |
| Refactor | `$refactor` | `/skill:refactor` |
| Review | `$review` | `/skill:review` |

Examples below use Codex notation; substitute Pi's command from this table. For example, enter `/skill:pair Implement S-001` or `/skill:capture Add colored labels later` in Pi's interactive input. These are agent commands, not shell commands. Normal approval replies resume the current workflow without reinvoking the skill.

Launch Pi from the target Git repository root with `pi`, grant project trust only after reviewing its content, and run `/reload` if resources changed during a session. Pi discovers `.agents/skills/` and reads AGENTS.md as context; inspect startup diagnostics and the `/skill:` commands. There is no need to copy skills to `.pi/skills/`, add a second instruction file, or replace Pi's system prompt. Existing user settings or duplicate skill names can affect discovery. In Codex, reopen the session if updated skills are not available.

Both agents explicitly read the linked guides and use documented project commands. Presets, stories, backlog and the Python/Git contract verifier are agent-independent; Pi still needs Python 3 and Git available to run that verifier. Choose a shell appropriate to the command: the Bash import block below is not PowerShell. In monorepos, starting at the root makes shared resources available; independent nested Git repositories need their own resources as described under repository boundaries.

Reference: [Pi skills and explicit invocation](https://pi.dev/docs/latest/skills), [Pi configuration and context files](https://pi.dev/docs/latest/configuration). This template does not install Pi, configure models/credentials or alter global agent settings.

| Skill | Purpose |
| --- | --- |
| [capture](.agents/skills/capture/SKILL.md) | Save future ideas without changing active scope or accepting work |
| [backlog](.agents/skills/backlog/SKILL.md) | Split ideas into a short backlog and record accepted work |
| [story](.agents/skills/story/SKILL.md) | Refine one selected slice with criteria, scope and a small plan |
| [pair](.agents/skills/pair/SKILL.md) | RED approval and commit, GREEN, validation and implementation commit |
| [refactor](.agents/skills/refactor/SKILL.md) | Optionally simplify passing code |
| [review](.agents/skills/review/SKILL.md) | Check correctness, scope, integrity, and clarity |

Copy all six skills, docs/, templates/, presets/, scripts/, and the relevant AGENTS.md agreement into a target repository, preserving relative paths and merging existing conventions. Reload Pi or reopen Codex if new skills are not discovered.

Use this repository as a starting template for a single repository or a monorepo. Keep AGENTS.md as the reusable working agreement. Replace `docs/project-guide.md` with the target project's accepted decisions using the guide template; its current template-maintenance rules do not transfer to the new product. Adapt this README to the new project. Keep the shared workflow, skill procedures, and contract tooling available at their linked paths.

## Copy into an existing repository

Run this from the root of your destination repository in Bash (Linux, macOS, or Git Bash on Windows). It clones into a unique temporary directory, exports tracked content without `.git`, copies it into the current directory including hidden files such as `.agents/`, and removes the temporary directory. Your destination repository's Git history and remote are preserved.

```bash
(
  set -euo pipefail
  template_dir="$(mktemp -d)"
  trap 'rm -rf -- "$template_dir"' EXIT

  git clone --depth 1 https://github.com/amphitekne/ai-template.git "$template_dir/source"
  mkdir "$template_dir/content"
  git -C "$template_dir/source" archive HEAD | tar -xf - -C "$template_dir/content"
  command cp -af "$template_dir/content/." .
)

git status --short
```

`command cp -af` overwrites matching files automatically without confirmation, including AGENTS.md, README.md, `.gitignore`, and the project guide. Commit or back up any local content you want to retain before running it. `command` bypasses a shell alias or function that might otherwise enable interactive copying. The trailing `/.` copies the contents directly into the destination root rather than creating a template folder. Review the resulting diff before committing and adapt the project guide to your product.

`git clone` has no option to omit `.git`, and cloning into a nonempty repository root is not supported. The temporary clone plus `git archive` avoids copying the template's Git metadata; cleanup removes only the temporary clone and export. Do not run this block in PowerShell: `cp` there is a different command. Use a Git Bash terminal for these commands on Windows.

Typical flow: `$backlog` → `$story` → `$pair`. Example requests: “Use $backlog to split this feature”; “Use $story to refine S-001”; “Use $pair for S-001”; “Use $refactor on this passing implementation”; “Use $review on this diff.” Each skill still requires its own human invocation. Proposals do not authorize implementation.

Keep the backlog to one line per accepted item; expand only the next selected story. Use a few observable criteria, a small plan, and three compact delivery-evidence entries. Tests exercise public behavior with independent expected values; visual or otherwise unsuitable automated checks get explicit manual validation steps. Pause after two fix attempts on the same failure without meaningful progress. There are no fixed line/file quotas or mandatory review/refactor rounds. Explicit test approval, the committed RED contract, human validation and the separate implementation commit remain required.

Read the [workflow](docs/workflow.md). Use the [backlog](templates/backlog.md) and [story](templates/story.md) templates in the target project. No product requirements or backlog entries are invented here.

The contract verifier requires Python 3 and Git, with no third-party packages. Run regression checks with `python -m unittest discover -s tests -v`. It verifies content integrity, not human approval or test quality.

## Capture ideas while development continues

Use `$capture Add colored labels to tasks later` to save a short unaccepted note with an ID in `docs/ideas.md` (created only on the first capture). No implementation, investigation, story changes or commits occur. In this chat, add “then continue where you were” to resume the prior authorized step without bypassing its gates. To keep a working pair chat focused, use a separate ideas chat in the same checkout; it edits only the inbox and does not control the pair chat. Serialize writes if more than one chat uses the inbox. A fork is optional for exploring an alternative, not necessary for saving a note, and a different worktree needs an explicit file transfer.

Later say `$backlog Review the pending ideas` to decide which to accept, defer or dismiss. Only accepted ideas become backlog work, with links back to their original notes. Current blockers and urgent risks must be raised in the active implementation chat rather than hidden in future ideas. See [capture boundaries](docs/workflow.md#capture-without-changing-scope).

## Fast checks by default

Use unit tests for logic and focused integration only where a real boundary needs it. A vertical story does not require automated E2E. Approve focused iteration commands and a lightweight mandatory closing set with the RED tests. Iterate on the relevant subset; run closing checks on the delivered state, reusing evidence only when relevant inputs are demonstrably unchanged. The closing set includes approved story tests and required regressions, not automatically every suite in the repository.

Docker images, full deployment stacks and automated E2E run only on explicit request or under accepted project requirements. Keep their commands separate in the project guide. The human validates complete flows with supplied steps; the driver reports what automation did and did not establish. Contract integrity remains mandatory; regression tests of the contract tool itself run when that tool changes or when required, not for every product story. See [execution and evidence rules](docs/workflow.md#execution-plan-and-reusable-evidence). Existing story contracts are not silently reduced by adopting this default.

## Agile Docker Compose development

Select the [docker-compose preset](presets/docker-compose.md) when the project uses Docker: “Apply docker-compose to this project's runtime.” Combine it with backend/frontend presets as needed; it adds guidance, not generated Compose files or a new skill.

- Development keeps application services running with mounted source and reload/HMR, plus persistent development data for human checks.
- Focused integration starts only isolated real dependencies such as a test database. Tests run application code in-process or in a one-off runner using current source; they do not repoint the running dev backend or require the frontend/proxy by default. Reuse dependencies during the session, reset between cases and remove only dedicated test storage at explicit cleanup.
- Production-style execution uses built images without source mounts/reload. Build and deployment checks run at explicit/accepted triggers, not per source edit.

The guide records actual `dev`, `test-unit`, `test-integration`, `test-integration-clean` and `check-deploy` commands using existing project tooling. These names describe responsibilities, not extra scripts supplied by the template. The preset proposes a small runtime Compose file, a dev override and a minimal independent integration file; preserve an existing equivalent setup. Do not create unnecessary services, files or task-runner dependencies.

## Evolving technical guidance

For reusable starting choices, use the [stack preset catalog](presets/README.md): [Python 3.15 + uv + FastAPI + Pydantic](presets/backend-python-fastapi.md) or [React + Vite + Zod + pnpm](presets/frontend-react-vite.md). For example: “Apply backend-python-fastapi to apps/api and frontend-react-vite to apps/web.” No new skill or script is needed. The driver snapshots accepted rules into the applicable guides; the catalog alone does not activate rules or install anything. Presets cover modular clean architecture, API validation and routers, or reusable UI and a single source of design tokens. Project-specific choices remain in the guide, and preset updates never migrate adopted projects automatically.

AGENTS.md defines collaboration; `docs/project-guide.md` holds the project's technical restrictions, conventions, and bounded experiments. This repository's [guide](docs/project-guide.md) describes template maintenance. When adopting the system, replace it with product-specific confirmed rules using the [guide template](templates/project-guide.md), and merge links into the target AGENTS.md. Define stack, style, tests, and security only as decisions are made; no complete up-front specification is required.

For a monorepo, the project guide links package-specific guides when needed and identifies their scope. Keep common rules centralized and load only guidance relevant to the affected packages. A single repository can use just the project guide. No package-guide directory is required until there is distinct guidance to store.

For example, packages in the same Git repository can use this layout (illustrative; create local guides only when needed):

```text
AGENTS.md
docs/project-guide.md                 # Shared rules and scope index
apps/web/docs/project-guide.md        # Scope: apps/web/**
apps/api/docs/project-guide.md        # Scope: apps/api/**
packages/shared/                      # No separate guide unless useful
```

In `docs/project-guide.md`, link the web guide with `[Web](../apps/web/docs/project-guide.md)` and its scope `apps/web/**`; the web guide links back with `[Shared guide](../../../docs/project-guide.md)`. These are example link paths, not files supplied by this template. Local rules complement shared rules; explicitly record accepted exceptions. Work touching both web and API consults both guides, plus guidance for any affected shared code. Recheck the applicable guides as the change expands.

If a child is a separate Git repository or submodule, give it its own AGENTS.md and project guide, with the workflow resources available when opened alone. The container documents integration and links to child guidance. Contracts and commits belong to each Git repository; see [repository boundaries](docs/workflow.md#repository-boundaries). A monorepo of ordinary folders needs no duplicate AGENTS.md, skills or verifier per package.

The driver proposes rule changes from real evidence; the navigator accepts direction and exceptions. Follow the [evolution procedure](docs/workflow.md#evolving-project-guidance). Changes specify how existing code is treated and do not start automatic migrations. Keep substantial decision rationale in separate files only when needed. Existing skills handle this; no additional phase or guide-maintenance skill is required.
