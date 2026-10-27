# Pairing workflow — v5

Backlog splits feature intent into a short list and records accepted work; story refines one selected slice just before implementation; pair drives it. Refactor and review are optional unless explicitly required by the navigator or project rules. The navigator controls direction and validation; the AI driver works in small understandable steps.

## Skill activation

Only the human explicitly invokes skills, for example with `$story` or `$pair`. Every skill disables implicit invocation in its `agents/openai.yaml`. The driver may suggest a next skill but must not activate it, chain skills, or interpret a workflow handoff as permission to invoke one. Optional refactoring through the refactor skill requires its own human invocation. Normal steps within an already invoked skill remain authorized within its scope and approval gates.

| From | Required evidence | To |
| --- | --- | --- |
| Proposed | Navigator accepts scope and criteria | Accepted |
| Accepted | Baseline inspected; automated criteria mapped to tests and manual criteria to checks | RED |
| RED | Expected missing-behavior failures, exact diff and commands presented | Awaiting test approval |
| Awaiting test approval | Explicit approval of exact tests and paths, separate test commit, sealed contract verifies | Tests committed |
| Tests committed | Verified contract and approved command/collection evidence | GREEN |
| GREEN | Agreed closing set passes on delivered state, optional refactor checked, unchanged contract; human checks and remaining risks supplied | Awaiting human validation |
| Awaiting human validation | Human validates behavior, separate implementation commit exists, contract verifies | Done |
| Any active state | Invalid tests, changed scope, missing prerequisite, integrity failure | Blocked |

Record actual approval messages/references and exact approved revision. Silence and general implementation authorization never approve tests. The human commits or explicitly authorizes the AI. Stage only intended files. Normal delivery has two commits: RED tests, then implementation after human validation. Documentation and evidence may accompany the appropriate commit. Record final hashes afterward to avoid self-referential hashes inside a commit.

Prepare one concrete test-approval package: exact diff, criterion coverage, protected paths, iteration and closing commands, collection, expected RED failures and human checks/remaining risks. Approve it together, without separate rounds for test names or evidence formatting. This workflow remains slice-wide RED then GREEN; small GREEN steps do not authorize writing a new test between implementation steps.

## Test quality and pairing pace

Test each behavior at the lowest-cost level that detects its relevant failures. Default to fast unit tests of public domain/application behavior. Use focused integration when the risk depends on a boundary (for example SQL semantics or request serialization) that a unit test cannot establish. Do not duplicate coverage at every layer or require automated E2E because a story is vertical. Expected values come from criteria or independent examples, never the implementation's own calculation.

The human validates complete user flows by default, with concrete steps and expected results. Criteria may have automated checks, human checks or both. State which integration/deployment/visual risks automation does not cover; passing unit tests must not be presented as proof of the entire flow. If a material risk warrants more automation, propose the smallest useful check. Existing accepted project requirements remain binding.

## Execution plan and reusable evidence

Approve the execution plan with the RED tests. Record the working directory and exact focused iteration commands, the mandatory closing set, and human checks. The closing set includes every approved story test plus relevant regressions and checks required by the project's accepted rules; it is not automatically the whole repository suite. Defaults:

| Check | Normal use |
| --- | --- |
| Fast unit tests | Relevant subset during GREEN; agreed set at closing |
| Focused integration | Only for an identified boundary risk; include in closing if approved |
| Docker builds, full stacks, deployment checks, automated E2E | Outside the normal loop; only on explicit request or when accepted project rules require them |
| Contract verifier regression tests | When the verifier or its dependencies change, or explicitly required; not for every product story |
| Contract integrity verification | At entry to GREEN, around closing checks, after optional refactor and immediately before implementation commit |
| Complete user flows | Human validation before the implementation commit |

Do not start containers or rebuild images as a hidden side effect of a supposedly fast command. If infrastructure is needed, explain the cost and obtain acceptance unless already required. Document expensive commands separately in the project guide rather than chaining them into normal unit tests. When slow checks are required, measure the slow phases before proposing optimizations; reuse services only when isolation/reset rules preserve correctness. No new verification skill or infrastructure is required by this workflow.

For projects using Docker Compose, the optional [Docker preset](../presets/docker-compose.md) defines the reusable environment model: development with reload for human validation, isolated reusable integration dependencies, and separate production-style checks. Adopt it into applicable guides when the navigator selects it; its existence does not authorize Docker startup. An approved integration command may start its documented test-only dependencies without an extra approval per run. Keep dev settings/data untouched, validate test targets before reset/cleanup, and never make tests depend on the manually used dev process or stale image code. Rebuild only affected images when inputs require it; production-style checks follow the agreed trigger and scope.

Establish a relevant baseline once. During GREEN, run only the approved subset related to the change/failure; do not rerun a full closing set before and after every edit. Run the closing set after the final relevant code change and optional refactor. Check collection against the approved closing set, not the smaller iteration subset. A required check that cannot run is reported as blocked, never passed. Reducing an already approved closing set requires explicit navigator acceptance; changes to protected tests/configuration still require renewed RED approval and commit.

Reuse a passing result only when its relevant code (including transitive dependencies/shared configuration), tests, dependency lockfiles, command/selection, runtime and relevant environment inputs are demonstrably unchanged. Record a compact source/result reference plus the input state and environment sufficient to justify reuse; a timestamp or unchanged test file alone is insufficient. If validity cannot be established, rerun the focused baseline or affected closing checks. A final-state result can be reused after documentation-only edits or committing unchanged bytes when the command does not depend on those edits or Git state. Code, environment or fixtures changed during manual validation invalidate affected results. Never reuse an expected RED failure as a passing baseline or carry approval forward to modified tests. This is a lightweight evidence rule, not a requirement to build a cache system.

Changing this template does not retroactively reduce contracts or closing requirements in active stories. Propose and explicitly accept those execution-plan changes in the target project; preserve its existing tests and approval evidence.

Use a short plan and brief progress updates. Continue ordinary edits and checks within the approved scope without asking permission at every step. Stop at established gates, unplanned design decisions, scope changes or test defects. After two consecutive unsuccessful fix attempts on the same failure without meaningful progress, pause for navigator direction with evidence and the smallest next option. Expected RED failures are not unsuccessful fix attempts. Size limits are prompts to consider splitting, not mandatory counts of criteria, lines or files.

## Executable contract gate

After the approved RED commit, from the target Git repository root:

```sh
python scripts/test_contract.py seal --base <full-red-commit> --path tests --path pyproject.toml --output .test-contracts/S-001.json
python scripts/test_contract.py verify --manifest .test-contracts/S-001.json --base <full-red-commit> --contract-sha256 <recorded-manifest-digest>
```

Paths above are examples. Protect whole test directories including future additions, fixtures/helpers/snapshots, runner/discovery configuration, dependency and lock files, and CI scripts affecting execution. Absent paths may be protected against creation. Do not protect production directories that GREEN must change. Protect a whole mixed test/production configuration file; necessary edits require renewed approval.

Seal from a clean tracked worktree and index matching the RED commit. Unrelated untracked files outside protected paths are allowed. Keep the manifest outside protected paths. Record its location and the full RED hash independently in the story. Also record the manifest SHA-256 printed by seal independently in the story. Every verify command must use that digest and the RED hash, never values read only from a replaceable manifest. This protects the path list as well as file hashes.

The verifier compares Git bytes and modes to the manifest, index and working files. Protected edits, additions (including ignored/untracked files), deletions, staged changes and symlink changes fail. Baselines outside current history and tampered manifests fail. Verify at GREEN entry, around the closing run, after refactor and immediately before the implementation commit; one verification can satisfy coincident checkpoints when no intervening change invalidates it. A failure blocks delivery. Run the approved iteration/closing commands separately and compare closing collection with the approved set. Never bypass assertions via flags, skips, test-only mocks that hide the behavior under test, runner changes or production special cases. Ordinary unit-test doubles at real external boundaries remain appropriate.

The tool verifies integrity, not approval, test quality or coverage. Use it as a local/CI gate with the independently recorded baseline. It is not a tamper-proof security boundary against someone who can edit the verifier or CI itself.

## Incorrect tests or changed scope

Stop GREEN and mark Blocked. Explain the defect and preserve implementation separately without committing it as accepted delivery. Return to RED, propose corrected tests and paths, rerun, and obtain fresh explicit approval. Commit revised tests separately; record superseded evidence, reseal against the new full test commit, verify, then resume GREEN. Never quietly amend tests, reuse approval for changed bytes, or mix test repair into implementation. Corrections may require extra RED commits; the normal two-commit rule never justifies rewriting history.

## Lightweight documentation

Keep one source for each fact: the story owns scope, status and compact delivery evidence; criteria name their tests or manual checks; the manifest owns protected paths and file hashes; the backlog is a one-line index. Existing backlogs may retain useful status/priority columns, but do not require synchronization of intermediate states. Create detailed files only for selected stories. Do not generate reports, raw log archives, empty sections or decision records by default.

The driver maintains three evidence entries: RED (iteration/closing plan, collection, baseline/expected failures, explicit approval and full test commit); contract (manifest path, independently recorded SHA-256 and verification result); delivery (closing results, any reused evidence with validity reason, human validation, checks not run/remaining risks and implementation commit). Concise summaries or durable links suffice. Keep the exact approved test revision identifiable; do not replace approval with an overall success summary. Record contract revisions or limitations only when they arise. The hashes and digest remain required for integrity checks, without duplicating manifest contents or terminal logs. No extra evidence-only commit is required: record final delivery references locally or in the next normal documentation update.

Update usage documentation when behavior changes; propose adjacent improvements separately. Review and automation never substitute for navigator validation.

## Evolving project guidance

Stack presets are optional starting points selected explicitly by the navigator. Follow the [preset procedure](../presets/README.md) to adopt a scoped snapshot in the project guide; do not read or apply unrelated presets, scaffold a stack automatically, or treat later catalog edits as active-rule changes. Selecting a preset is a normal user instruction and does not invoke a skill.

Read the target project's `docs/project-guide.md` and any applicable module instructions when preparing a story and before implementation. Consult linked decisions only when relevant. If the guide is absent, inspect existing instructions and configuration; propose a minimal guide using the [template](../templates/project-guide.md) when useful. Missing documentation alone is not a blocker. Do not invent a stack or convert observed code patterns into accepted rules.

For a monorepo, use the root guide's scope index to select local guides for the packages and shared code affected by the task, including integration boundaries. Local guides state their repository-root-relative scope and link back to the root guide. Follow relevant linked guides, and recheck applicability if the work reaches another package. A missing or stale index entry is not permission to ignore existing local guidance: inspect applicable instructions and nearby package documentation and propose a corrected link when useful. Do not create guides for packages without distinct rules.

Shared rules apply alongside local rules. A local exception must explicitly identify the shared rule, replacement, scope and navigator acceptance. Otherwise surface conflicts before the affected work rather than automatically preferring the narrower guide. Reading a guide does not invoke a skill or authorize additional work.

Keep three kinds of guidance distinct: restrictions are mandatory boundaries; conventions are agreed defaults; experiments are accepted trials with a limited scope and a review trigger. Ask only about unresolved decisions that affect the work. If sources conflict, surface the conflict to the navigator before the affected step; do independent work where possible. Do not silently choose a convenient interpretation or relax a rule.

When the navigator changes direction or development reveals a useful lesson, present a concrete proposal: current rule (if any), evidence or reason, replacement or exception, scope, impact on pending stories and existing code, and a practical check where available. The navigator's explicit request for that exact change can supply acceptance; do not ask twice. Otherwise wait for acceptance before treating it as guidance. Record proposals in the conversation or affected story, not as active rules. Do not require a proposal or guide update on every story.

After acceptance, update the active rule in the same bounded change and retain a short reason/acceptance reference for consequential decisions. Distinguish project-wide changes from story-specific exceptions. State whether the rule applies to new work, touched code, or an accepted migration; never infer permission for a repository-wide rewrite. Backlog records migration stories only after acceptance. Create separate decision files only when their rationale warrants them.

Use stable rule IDs to reference relevant guidance from stories without copying it. Revisit an experiment at its stated trigger; the navigator decides whether to retain, revise, or end it. Flag obsolete or conflicting rules when encountered rather than scheduling mandatory guide reviews. Prefer existing formatters, linters, tests, or dependency checks to enforce machine-checkable rules; adding or changing tools must fit accepted scope. A technical rule change that affects approved tests, protected dependencies, or acceptance criteria still follows the contract revision path above.

On Windows, executable bits are checked through the Git index; working-file mode checks apply on POSIX. Raw byte comparison deliberately fails on line-ending conversion: configure test files with stable Git attributes before RED approval.

## Repository boundaries

Folders in one Git repository share its root agreement and workflow. Nested independent repositories, including submodules, need their own AGENTS.md, project guide and available workflow/skill resources (adopted or explicitly linked at accessible paths). Their instructions must work when the repository is opened alone; do not depend on implicit discovery of the container's documents. The container guide describes integration boundaries, not the child's internal stack by default.

For work spanning independent repositories, identify the affected Git roots and read each one's instructions before editing. Keep scope and integration acceptance coordinated in the story. Each changed repository has its own RED baseline, contract and delivery evidence; record the repository root with its hashes and commands. The verifier operates within one Git root and does not protect files inside a submodule via the parent's Git entry. Verify the child contract inside the child repository. Preserve RED/implementation separation per changed repository and update container submodule references only after the corresponding child commits exist and are authorized. Do not introduce nested repositories or additional infrastructure merely to follow this documentation.
