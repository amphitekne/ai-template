---
name: review
description: Review code, stories, or instructions for correctness, scope, contract integrity and readability; report findings without edits unless requested.
---

# Review

Run only when explicitly invoked by the human. Never activate another skill automatically; suggest the next skill and wait for the human to invoke it.

Read requested artifacts and necessary references in full. Compare with confirmed intent, conventions and [workflow](../../../docs/workflow.md). Do not convert examples or assumptions into requirements.

For slices, inspect coverage, RED failures, explicit approval, test commit, contract verification, collection, GREEN results, scope, validation and separate implementation commit. Execute the verifier when available; state missing evidence. Prioritize concrete defects and readable minimal design over style.

For templates, check objectives, inputs/outputs, contradictions, dependencies, triggers, frontmatter, and relative links. Reason through representative and nearby excluded requests; label reasoning as reasoning, not executed tests.

Check applicable project-guide rules and accepted exceptions. Flag concrete violations, conflicting or obsolete guidance, and experiments whose review trigger has been reached. Distinguish accepted rules from proposals; suggest bounded updates rather than silently promoting conventions or requesting broad cleanup.

Report actionable findings with location, severity, consequence and correction. If none, say so and identify verification limits. Review never supplies human approval or waives gates. Edit only when requested; recheck corrections.
