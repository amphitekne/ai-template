# Stack presets

Presets are reusable technical guidance, not skills, executable installers, or active project rules. Read only presets the navigator selects. Their presence does not select a stack or authorize scaffolding, dependency installation, migration, or changes to approved tests.

| Preset | Intended scope |
| --- | --- |
| [backend-python-fastapi](backend-python-fastapi.md) | Modular Python 3.15 backend with uv, FastAPI and Pydantic |
| [frontend-react-vite](frontend-react-vite.md) | Modular React frontend with Vite, Zod, pnpm and centralized design tokens |

## Apply a preset

The navigator can say: “Apply backend-python-fastapi to apps/api” or “Use both presets for this project, backend in apps/api and frontend in apps/web.” This is a normal instruction; no skill invocation or extra process phase is needed.

1. Read existing applicable guidance and configuration. Resolve the intended package/path scope; do not assume a particular repository layout. Surface only conflicts, compatibility problems or choices that materially affect the work. An explicit selection accepts the preset's stated defaults for that scope; obtain acceptance for proposed deviations instead of asking again about unchanged defaults.
2. Create or update the scoped project guide using the [template](../templates/project-guide.md). Copy the selected rules into it with stable IDs, scope, source preset path and revision (Git commit when available), and any accepted overrides. The guide is the active, self-contained snapshot; do not require opening the entire preset catalog for each story. In a monorepo, link this guide from the root scope index. In a single repository, the root guide may contain the rules directly.
3. Record known runtime/tool versions and actual check commands when available. Do not invent missing choices such as databases, authentication, deployment, UI libraries or test runners. Verify compatibility during the first relevant implementation step; report blockers rather than silently downgrading a selected stack.

Applying guidance does not create all proposed layers and components up front. Build only what the next accepted slice needs. Existing code is migrated only within accepted scope. Normal story, RED approval, contract and delivery gates still apply.

## Evolve a preset or a project

Project-specific exceptions belong in the project guide. Update a shared preset only when the navigator wants the change reused in future projects. Editing a preset does not alter previously adopted snapshots or migrate existing projects. Adopt later changes through the normal guide-evolution procedure with a concrete diff and scope. Do not keep competing versions of an active rule in the guide and a live preset include.
