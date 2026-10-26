# Pairing workflow — v5

Story proposes work; backlog records accepted work; pair drives it; refactor is optional; review reports findings. The navigator controls direction and validation; the AI driver works in small understandable steps.

## Skill activation

Only the human explicitly invokes skills, for example with `$story` or `$pair`. Every skill disables implicit invocation in its `agents/openai.yaml`. The driver may suggest a next skill but must not activate it, chain skills, or interpret a workflow handoff as permission to invoke one. Optional refactoring through the refactor skill requires its own human invocation. Normal steps within an already invoked skill remain authorized within its scope and approval gates.

| From | Required evidence | To |
| --- | --- | --- |
| Proposed | Navigator accepts scope and criteria | Accepted |
| Accepted | Baseline inspected and criterion-to-test mapping agreed | RED |
| RED | Expected missing-behavior failures, exact diff and commands presented | Awaiting test approval |
| Awaiting test approval | Explicit approval of exact tests and paths, separate test commit, sealed contract verifies | Tests committed |
| Tests committed | Verified contract and approved command/collection evidence | GREEN |
| GREEN | Approved tests and regressions pass, optional refactor passes, unchanged contract | Awaiting human validation |
| Awaiting human validation | Human validates behavior, separate implementation commit exists, contract verifies | Done |
| Any active state | Invalid tests, changed scope, missing prerequisite, integrity failure | Blocked |

Record actual approval messages/references and exact approved revision. Silence and general implementation authorization never approve tests. The human commits or explicitly authorizes the AI. Stage only intended files. Normal delivery has two commits: RED tests, then implementation after human validation. Documentation and evidence may accompany the appropriate commit. Record final hashes afterward to avoid self-referential hashes inside a commit.

## Executable contract gate

After the approved RED commit, from the target Git repository root:

```sh
python scripts/test_contract.py seal --base <full-red-commit> --path tests --path pyproject.toml --output .test-contracts/S-001.json
python scripts/test_contract.py verify --manifest .test-contracts/S-001.json --base <full-red-commit> --contract-sha256 <recorded-manifest-digest>
```

Paths above are examples. Protect whole test directories including future additions, fixtures/helpers/snapshots, runner/discovery configuration, dependency and lock files, and CI scripts affecting execution. Absent paths may be protected against creation. Do not protect production directories that GREEN must change. Protect a whole mixed test/production configuration file; necessary edits require renewed approval.

Seal from a clean tracked worktree and index matching the RED commit. Unrelated untracked files outside protected paths are allowed. Keep the manifest outside protected paths. Record its location and the full RED hash independently in the story. Also record the manifest SHA-256 printed by seal independently in the story. Every verify command must use that digest and the RED hash, never values read only from a replaceable manifest. This protects the path list as well as file hashes.

The verifier compares Git bytes and modes to the manifest, index and working files. Protected edits, additions (including ignored/untracked files), deletions, staged changes and symlink changes fail. Baselines outside current history and tampered manifests fail. Verify before and after tests, after refactor, and immediately before the implementation commit; a failure blocks delivery. Run the exact approved test commands separately and compare collection with RED evidence. Never bypass assertions via flags, skips, mocks, runner changes or production special cases.

The tool verifies integrity, not approval, test quality or coverage. Use it as a local/CI gate with the independently recorded baseline. It is not a tamper-proof security boundary against someone who can edit the verifier or CI itself.

## Incorrect tests or changed scope

Stop GREEN and mark Blocked. Explain the defect and preserve implementation separately without committing it as accepted delivery. Return to RED, propose corrected tests and paths, rerun, and obtain fresh explicit approval. Commit revised tests separately; record superseded evidence, reseal against the new full test commit, verify, then resume GREEN. Never quietly amend tests, reuse approval for changed bytes, or mix test repair into implementation. Corrections may require extra RED commits; the normal two-commit rule never justifies rewriting history.

## Lightweight documentation

Keep scope, coverage, commands/results, approvals, hashes, blockers and demonstration steps in the story. Keep the backlog a linked index. Update usage documentation when behavior changes; propose adjacent improvements separately. Review and automation never substitute for navigator validation.

## Evolving project guidance

Read the target project's `docs/project-guide.md` and any applicable module instructions when preparing a story and before implementation. Consult linked decisions only when relevant. If the guide is absent, inspect existing instructions and configuration; propose a minimal guide using the [template](../templates/project-guide.md) when useful. Missing documentation alone is not a blocker. Do not invent a stack or convert observed code patterns into accepted rules.

Keep three kinds of guidance distinct: restrictions are mandatory boundaries; conventions are agreed defaults; experiments are accepted trials with a limited scope and a review trigger. Ask only about unresolved decisions that affect the work. If sources conflict, surface the conflict to the navigator before the affected step; do independent work where possible. Do not silently choose a convenient interpretation or relax a rule.

When the navigator changes direction or development reveals a useful lesson, present a concrete proposal: current rule (if any), evidence or reason, replacement or exception, scope, impact on pending stories and existing code, and a practical check where available. The navigator's explicit request for that exact change can supply acceptance; do not ask twice. Otherwise wait for acceptance before treating it as guidance. Record proposals in the conversation or affected story, not as active rules. Do not require a proposal or guide update on every story.

After acceptance, update the active rule in the same bounded change and retain a short reason/acceptance reference for consequential decisions. Distinguish project-wide changes from story-specific exceptions. State whether the rule applies to new work, touched code, or an accepted migration; never infer permission for a repository-wide rewrite. Backlog records migration stories only after acceptance. Create separate decision files only when their rationale warrants them.

Use stable rule IDs to reference relevant guidance from stories without copying it. Revisit an experiment at its stated trigger; the navigator decides whether to retain, revise, or end it. Flag obsolete or conflicting rules when encountered rather than scheduling mandatory guide reviews. Prefer existing formatters, linters, tests, or dependency checks to enforce machine-checkable rules; adding or changing tools must fit accepted scope. A technical rule change that affects approved tests, protected dependencies, or acceptance criteria still follows the contract revision path above.

On Windows, executable bits are checked through the Git index; working-file mode checks apply on POSIX. Raw byte comparison deliberately fails on line-ending conversion: configure test files with stable Git attributes before RED approval.
