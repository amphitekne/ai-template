---
name: review-slop
disable-model-invocation: true
description: Detect generic, interchangeable patterns in an interface and propose specific changes that strengthen its identity; use for AI-slop concerns rather than a general usability audit.
---

# Review Slop

Run only when explicitly invoked by the human. Do not activate other skills automatically. Follow the [workflow](../../../docs/workflow.md) and applicable project guidance. Review without editing; proposals do not authorize implementation.

## Understand the interface

Resolve In Scope and Out of Scope to a screen, flow, page or change. Inspect its rendered appearance, real content, audience, primary task, existing design system and accepted direction. For redesigns, identify distinctive elements worth preserving. Separate confirmed intent from assumptions.

“Slop” describes a perceived lack of specificity and intentionality here. It does not establish AI authorship. Do not label a design generic from a font name, library, gradient, three-column grid or isolated screenshot fragment alone. If rendered evidence is unavailable, provide provisional concerns and mark visual judgment unverified.

## Look for combinations and repetition

- Composition: predictable section sequences, repeated equal-weight cards, redundant containers, uniformly centered content and no clear relationship between hierarchy and importance.
- Visual identity: interchangeable typography, palette, imagery and decoration; borrowed motifs that do not form a coherent direction; competing effects with no role.
- Content: headlines that fit any competitor, vague benefits, repetitive labels, filler and claims unsupported by supplied facts. Do not assume an unfamiliar claim is fabricated; verify or flag its provenance as unknown.
- Product specificity: missing real workflows, artifacts, terminology or material that could make this product recognizable. Ask what remains distinctive if its name and logo are removed.
- Consistency and restraint: random stylistic changes, ornamental icons, unnecessary motion and repeated emphasis that makes everything seem equally important.

Evaluate the combination against purpose and context. Familiar patterns can be the right choice, especially in working applications. An unusual font or asymmetric layout does not compensate for generic content. Do not replace one recognizable template with another, such as prescribing cream, serif headings and grain for every product.

## Propose changes with a reason

For each actionable finding, give:

1. Location and observed evidence, including the repeated pattern or relevant combination.
2. Why it makes this particular interface feel interchangeable; label subjective judgments and confidence honestly.
3. A concrete change tied to the product, its content or accepted direction, and what should remain.
4. Expected benefit, tradeoff and a practical way to compare before and after.

Prefer a few changes with substantial impact. Separate quick corrections within the current direction from structural or identity changes requiring a navigator decision. When facts or assets are missing, propose removing an unsupported section or obtaining real material rather than inventing proof. Any example copy must use confirmed facts or clearly marked placeholders.

Example: six equal icon cards give a central workflow the same weight as secondary utilities. Propose a real annotated workflow image for the main capability and a compact list for the utilities, preserving their content. This is justified by hierarchy and product material, not by a ban on cards.

Do not assign a pseudo-objective slop score or count prohibited motifs as a quality verdict. A short report or no findings is valid. Distinguish identity opportunities from usability defects and accepted-direction inconsistencies. Flag serious observed usability issues without claiming a full UI audit.

Finish with prioritized recommendations, preserved strengths, evidence limits and the smallest next comparison. If identity needs redefining, suggest design-ui; if usability needs deeper examination, suggest review-ui. Wait for explicit invocation. Selected corrections return to the normal story and pairing workflow.
