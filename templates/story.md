# <ID>: <Observable outcome>

Status: Proposed

## User value
As a <user>, I want <capability>, so that <outcome>.

## In Scope
- <Small end-to-end behavior>

## Out of Scope
- <Explicit adjacent exclusions>

## Acceptance criteria
- AC1 [automated: <public interface/test>]: Given <context>, when <action>, then <observable result>.
- AC2 [manual, only when useful]: <Steps and expected observable result>.

## Plan
- <Smallest implementation approach; a few bullets, not a task specification>

Add dependencies, unresolved decisions or relevant guide exceptions only when needed. Record navigator acceptance before applying an exception. Remove unused sections rather than filling them with None.

## Delivery evidence

Fill these three short entries as the work progresses. Link durable output or use concise summaries; do not paste complete logs. The driver maintains the evidence.

- RED: <commands, baseline/new-test collection and expected failures; explicit approval reference and approved revision; full test commit hash>
- Contract: <manifest path and independently recorded SHA-256; verification result; protected paths live in the manifest>
- Delivery: <GREEN/regression commands and results; human validation reference including manual criteria; full implementation commit hash>

Criteria above provide the coverage mapping and manual demonstration steps. Record limitations, blockers or renewed approvals only when they occur. Never assume future approvals or fill future gates with invented evidence.
