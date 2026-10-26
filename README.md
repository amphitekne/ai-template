# templating-ai — v5

Five English-language skills for human-led pair programming. The human navigates; the AI drives. No custom subagents.

Skills are user-invoked only: use `$story`, `$backlog`, `$pair`, `$refactor`, or `$review`. Each skill's `agents/openai.yaml` sets `policy.allow_implicit_invocation: false`; copy these files with the skills. The AI may recommend another skill but waits for your explicit invocation. These `agents/` directories contain skill configuration, not custom subagents. Start a new session to reload changed invocation settings if needed.

| Skill | Purpose |
| --- | --- |
| [backlog](.agents/skills/backlog/SKILL.md) | Split ideas into a short backlog and record accepted work |
| [story](.agents/skills/story/SKILL.md) | Refine one selected slice with criteria, scope and a small plan |
| [pair](.agents/skills/pair/SKILL.md) | RED approval and commit, GREEN, validation and implementation commit |
| [refactor](.agents/skills/refactor/SKILL.md) | Optionally simplify passing code |
| [review](.agents/skills/review/SKILL.md) | Check correctness, scope, integrity, and clarity |

Copy all five skills, docs/, templates/, scripts/, and the relevant AGENTS.md agreement into a target repository, preserving relative paths and merging existing conventions. Reopen a Codex session if new skills are not discovered.

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
  cp -ai "$template_dir/content/." .
)

git status --short
```

`cp -ai` asks before overwriting existing files. Answer `n` for files whose content you want to preserve, then merge the relevant instructions manually, especially AGENTS.md, README.md, `.gitignore`, and any existing skills or documentation. The trailing `/.` copies the contents directly into the destination root rather than creating a template folder. Review the resulting diff before committing and adapt the project guide to your product.

`git clone` has no option to omit `.git`, and cloning into a nonempty repository root is not supported. The temporary clone plus `git archive` avoids copying the template's Git metadata; cleanup removes only the temporary clone and export. Do not run this block in PowerShell: `cp` there is a different command. Use a Git Bash terminal for these commands on Windows.

Typical flow: `$backlog` → `$story` → `$pair`. Example requests: “Use $backlog to split this feature”; “Use $story to refine S-001”; “Use $pair for S-001”; “Use $refactor on this passing implementation”; “Use $review on this diff.” Each skill still requires its own human invocation. Proposals do not authorize implementation.

Keep the backlog to one line per accepted item; expand only the next selected story. Use a few observable criteria, a small plan, and three compact delivery-evidence entries. Tests exercise public behavior with independent expected values; visual or otherwise unsuitable automated checks get explicit manual validation steps. Pause after two fix attempts on the same failure without meaningful progress. There are no fixed line/file quotas or mandatory review/refactor rounds. Explicit test approval, the committed RED contract, human validation and the separate implementation commit remain required.

Read the [workflow](docs/workflow.md). Use the [backlog](templates/backlog.md) and [story](templates/story.md) templates in the target project. No product requirements or backlog entries are invented here.

The contract verifier requires Python 3 and Git, with no third-party packages. Run regression checks with `python -m unittest discover -s tests -v`. It verifies content integrity, not human approval or test quality.

## Evolving technical guidance

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

The driver proposes rule changes from real evidence; the navigator accepts direction and exceptions. Follow the [evolution procedure](docs/workflow.md#evolving-project-guidance). Changes specify how existing code is treated and do not start automatic migrations. Keep substantial decision rationale in separate files only when needed. The five existing skills handle this; no additional phase or skill is required.
