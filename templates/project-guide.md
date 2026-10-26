# Project guide

Use this template to create `docs/project-guide.md` in the target project. Keep only confirmed, useful guidance. Remove these setup instructions after initialization. An empty category is not a prerequisite for development: omit it until there is a real decision.

## Purpose and scope

Record product context only when it changes engineering decisions. Identify any modules with different requirements. Link existing authoritative documentation rather than copying it.

If the navigator selects a stack preset, follow the [preset procedure](../presets/README.md): snapshot its accepted rules here or in the relevant package guide, record the source revision and overrides, and keep the guide self-contained. Catalog presets do not apply merely because their files are present. Remove this setup instruction when initializing the target guide.

For a monorepo, keep shared rules here and link scoped guides only where packages have meaningful differences. State each guide's package/path scope and any accepted exceptions to shared conventions. Do not create a guide per package by default or duplicate shared rules. For a single repository, this file may be sufficient. Keep stack, layout, language/style, testing commands, and security choices here or in those linked guides rather than adding them to the reusable AGENTS.md agreement.

## Scoped guide index (only when needed)

In the root guide, list each local guide with its repository-root-relative path scope, relative Markdown link, and purpose. For example, a guide at `apps/web/docs/project-guide.md` could cover `apps/web/**` and describe frontend-specific tests. Link paths are relative to this document; scope paths are relative to the Git repository root. Add real links only after the guides exist.

In a local guide, state its scope and link back to the shared root guide. Record only local differences and accepted exceptions (shared rule ID, replacement, scope and acceptance reference). Do not copy the shared rules or assume local guidance automatically overrides them. Cross-package work reads all affected guides, including shared-package and integration guidance; follow relevant linked scopes rather than loading every guide.

A nested independent Git repository or submodule has its own entry point and project guide so it can be used alone. The container may index its integration contract and link its guide, but that is not a substitute for instructions inside the child repository. See the shared workflow's repository-boundary procedure. Remove this optional section for a single project without scoped guides.

## Restrictions

Record mandatory boundaries such as confirmed stack choices, security requirements, or compatibility constraints. For each rule, give a stable ID, scope, concise instruction, and reason. Include an enforcement command or configuration link where practical. Changes or exceptions require explicit navigator acceptance before affected work proceeds.

## Conventions

Record defaults that help keep code homogeneous: module layout, naming, error handling, testing practices, and documentation placement where relevant. Use the same small rule format. The driver follows them and presents a concrete reason and bounded alternative before deviating; the navigator accepts the exception or revised rule. A one-story exception does not redefine the project default.

Testing defaults to fast unit tests, focused integration where a real boundary needs it, and human full-flow validation. Record actual fast commands and working directories; list costly Docker/deployment/E2E commands separately with their explicit execution triggers. State accepted stronger requirements by scope rather than silently adding them to the default test command. A story approves its iteration/closing selection and any reuse follows the shared workflow; no exhaustive suite is mandatory merely because it exists.

## Experiments

Record only accepted trials. Include a rule ID, limited scope, approach, success/stop criteria, and a review trigger such as a story outcome or date. At that trigger, ask the navigator to retain, revise, or end the trial. Do not silently promote it to a convention or extend it beyond scope. Unresolved trials do not authorize expansion.

## Accepted changes

For consequential changes, retain a short entry: rule ID, old/new direction, reason, navigator acceptance reference, applicability to new work, and treatment of existing code. Link a migration story if one has been accepted. Use `docs/decisions/` only when the rationale is substantial enough to warrant a separate document; create no empty decision directory.

Keep active rules in their categories; remove superseded wording there so obsolete rules cannot be mistaken for current instructions. Do not turn this section into a transcript or duplicate Git history.
