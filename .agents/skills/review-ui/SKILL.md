---
name: review-ui
disable-model-invocation: true
description: Review a rendered interface, user flow or UI change for usability, accessibility, responsive behavior, states and consistency; report evidence without editing.
---

# Review UI

Run only when explicitly invoked by the human. Do not activate other skills automatically. Follow the [workflow](../../../docs/workflow.md) and applicable project guidance. Review supplies findings, not human validation or authorization to implement them.

## Resolve scope and evidence

Identify the screen, complete flow or exact change under review. State In Scope and Out of Scope. For a diff, distinguish introduced issues, regressions and pre-existing problems. Inspect relevant product requirements, components, tokens and accepted design direction before judging consistency.

Inspect the rendered interface and interactions whenever the claim depends on appearance or behavior. Source inspection can reveal implementation defects but cannot prove rendered quality. Screenshots support visible findings, not keyboard behavior or hidden states. Mark unavailable evidence as not verified; never claim complete accessibility coverage from screenshots or automated checks alone.

## Review the task before the polish

- Task and comprehension: clear entry point, hierarchy, reading order, navigation, action labels, feedback and recoverable errors. Include confirmation or undo where consequences warrant it.
- Accessibility: semantic controls and names, keyboard access, visible focus, contrast, meaning beyond color, zoom/reflow and motion preferences. Use applicable authoritative criteria when making conformance claims; distinguish measured failures from concerns requiring verification.
- Layout and adaptability: supported viewport sizes, content lengths, translations where relevant, clipping, overlap, touch targets and information density suitable for the task.
- States: relevant loading, empty, error, success, disabled and active/selected conditions. Check transitions and recovery, not just static happy-path screens.
- Craft and consistency: typography, grouping, spacing, surfaces, icons, copy and motion against accepted project choices. A personal preference about density, radius or font is not a defect.

Use representative data and realistic interactions. Run only relevant checks permitted by the project's approval rules. Do not add or change tests during review; do not run tests without the explicit approval required by the workflow.

## Report

Consolidate repeated symptoms under their shared cause. Prioritize blocked tasks, inaccessible controls and misleading behavior, then comprehension and efficiency, then isolated polish. Do not pad a report to a fixed count.

Each finding includes location (screen/component and file:line when inspected), severity, observed evidence, user consequence and the smallest useful correction. Separate confirmed defects, inconsistencies with accepted direction and optional improvements. End with coverage, checks actually performed, verification limits and concrete manual checks still needed. If no actionable findings exist, say so.

Remain read-only unless the human separately requests edits. Corrections follow normal implementation gates. Questions about generic visual identity belong to review-slop when explicitly invoked; do not duplicate a full identity audit or switch skills automatically.
