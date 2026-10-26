# <ID>: <Observable outcome>

Status: Proposed

## User value
As a <user>, I want <capability>, so that <outcome>.

## In Scope
- <Small end-to-end behavior>

## Out of Scope
- <Explicit adjacent exclusions>

## Acceptance criteria
- AC1 [fast automation: <public function/boundary test>]: Given <context>, when <action>, then <observable result>.
- AC2 [human full-flow check; may complement AC1]: <Steps and expected observable result>.

## Plan
- <Smallest implementation approach; a few bullets, not a task specification>

Test execution: <working directory; focused iteration command; mandatory lightweight closing commands; human checks and material risks left uncovered>. Default to unit tests, adding focused integration for identified boundary risks. Docker/E2E need an explicit request or an accepted project requirement. The closing set covers all approved story tests; it need not include every repository suite.

Add dependencies, unresolved decisions or relevant guide exceptions only when needed. Record navigator acceptance before applying an exception. Remove unused sections rather than filling them with None.

## Delivery evidence

Fill these three short entries as the work progresses. Link durable output or use concise summaries; do not paste complete logs. The driver maintains the evidence.

- RED: <baseline run or valid prior evidence; approved iteration/closing plan and collection; expected failures; explicit approval reference and approved revision; full test commit hash>
- Contract: <manifest path and independently recorded SHA-256; verification result; protected paths live in the manifest>
- Delivery: <closing results on delivered state; reused results and why still valid, if any; human validation reference; checks not run/remaining risks; full implementation commit hash>

Criteria above provide the coverage mapping and manual demonstration steps. Record limitations, blockers or renewed approvals only when they occur. Never assume future approvals or fill future gates with invented evidence.
