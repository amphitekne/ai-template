# Project guide

Use this template to create `docs/project-guide.md` in the target project. Keep only confirmed, useful guidance. Remove these setup instructions after initialization. An empty category is not a prerequisite for development: omit it until there is a real decision.

## Purpose and scope

Record product context only when it changes engineering decisions. Identify any modules with different requirements. Link existing authoritative documentation rather than copying it.

For a monorepo, keep shared rules here and link scoped guides only where packages have meaningful differences. State each guide's package/path scope and any accepted exceptions to shared conventions. Do not create a guide per package by default or duplicate shared rules. For a single repository, this file may be sufficient. Keep stack, layout, language/style, testing commands, and security choices here or in those linked guides rather than adding them to the reusable AGENTS.md agreement.

## Restrictions

Record mandatory boundaries such as confirmed stack choices, security requirements, or compatibility constraints. For each rule, give a stable ID, scope, concise instruction, and reason. Include an enforcement command or configuration link where practical. Changes or exceptions require explicit navigator acceptance before affected work proceeds.

## Conventions

Record defaults that help keep code homogeneous: module layout, naming, error handling, testing practices, and documentation placement where relevant. Use the same small rule format. The driver follows them and presents a concrete reason and bounded alternative before deviating; the navigator accepts the exception or revised rule. A one-story exception does not redefine the project default.

## Experiments

Record only accepted trials. Include a rule ID, limited scope, approach, success/stop criteria, and a review trigger such as a story outcome or date. At that trigger, ask the navigator to retain, revise, or end the trial. Do not silently promote it to a convention or extend it beyond scope. Unresolved trials do not authorize expansion.

## Accepted changes

For consequential changes, retain a short entry: rule ID, old/new direction, reason, navigator acceptance reference, applicability to new work, and treatment of existing code. Link a migration story if one has been accepted. Use `docs/decisions/` only when the rationale is substantial enough to warrant a separate document; create no empty decision directory.

Keep active rules in their categories; remove superseded wording there so obsolete rules cannot be mistaken for current instructions. Do not turn this section into a transcript or duplicate Git history.
