# docker-compose

Apply through the [preset procedure](README.md). Scope: the selected application's local development, focused integration dependencies and production-style execution. Combine with backend/frontend presets; do not choose application technologies or introduce Docker into an existing project merely because this preset is present. These rules become active only when adopted in the project guide.

## Working model

| Purpose | Services | Data and lifecycle |
| --- | --- | --- |
| Development / human validation | Application services with code reload plus required dependencies | Persistent development data; keep running across edits |
| Focused integration | Only real dependencies required by approved tests, often a database | Isolated disposable test data; reuse services during the test session |
| Production-style execution | Built application images without source mounts or development servers | Persistent application data; verify deployment separately when requested/required |

## Restrictions

- DC-R1 — Keep development and production behavior distinct. Development uses mounted source and backend reload/frontend HMR where supported. Production uses built images, no source-code mounts, no reload and no development/debug server. Register differences explicitly in Compose configuration; production must not accidentally inherit development mounts or commands.
- DC-R2 — Preserve development data during tests. Integration has its own Compose project identity, networks and storage, test-only credentials/connection settings and clearly distinct database names. Do not share externally named volumes or fixed container names across environments. Bind host ports only when the runner needs them, using distinct local ports; project names alone do not prevent port collisions. Never retarget the running development application's database to run tests.
- DC-R3 — Integration runs the application code under test in the test process or a dedicated one-off runner, using the development runtime/image when useful. It does not depend on the manually used development backend process, frontend or proxy unless the approved test specifically needs that boundary. Keep test settings isolated from development configuration; verify the selected test target before migrations, resets or cleanup. Apply the same isolation to caches, queues and external side effects when tests use them.
- DC-R4 — Use the same relevant dependency versions and real migration path as the application. Start only dependencies required by the selected tests and wait for readiness with a bounded health/readiness check, not arbitrary sleeps. Prepare test schema/data once per session and reset test data between cases with a documented strategy. Transaction rollback is sufficient only when it covers all connections and committed work; otherwise use explicit cleanup/reset. Do not recreate the database container per test.
- DC-R5 — Test storage is dedicated and disposable. Default to a test-project-owned volume reused during the session and removed by explicit integration cleanup; stopping containers alone is not a guarantee that data is gone. Cleanup targets only the known test project and its owned storage, never development/production or global Docker resources. Do not use global prune/reset commands. Parallel sessions need unique project names/storage and nonconflicting ports or must run serially.
- DC-R6 — Normal source edits use reload; do not rebuild images or restart the whole stack per edit/test. Build initially and rebuild only affected images when dependencies, build inputs or configuration require it. Use current source in the test runner (mounted or explicitly synced); reusing an image must not silently test stale baked-in code. Ordinary unit tests require no database, full stack or image build.
- DC-R7 — Full deployment/image/proxy/persistence checks remain separate from unit and focused integration commands. Run them only on explicit request or under accepted project/story requirements. Infrastructure stories agree affected deployment checks before delivery; do not treat unit tests as evidence that an image or proxy works. Preserve the normal RED approval, contract and human-validation gates.

## Conventions

- DC-C1 — Prefer a small configuration: `compose.yaml` for runtime wiring without development-only settings, `compose.dev.yaml` for source mounts/reload/local settings, and a small independent `compose.integration.yaml` for test dependencies. Names and layout are examples; reuse an existing equivalent structure rather than renaming working files. Production overrides are added only if actual differences need them. Do not create a third full application stack for integration or add an elaborate YAML templating system.
- DC-C2 — Keep dependency image versions consistent across files, using a simple shared version setting where helpful. Keep runtime/test connections and secrets separate. Check the resolved Compose configuration when introducing or changing overrides so merge behavior does not retain unintended mounts, ports or dependencies. Store no real credentials in committed examples.
- DC-C3 — Start dev once for the working session; the human validates complete flows there. Start integration dependencies only when approved integration checks are needed; reuse them until explicit cleanup. Reusing a container does not by itself justify reusing a test result: apply the workflow's unchanged-input/environment rules. Do not share dirty fixtures between cases or assume an old session has the current schema.
- DC-C4 — Prefer source bind mounts and framework reload first. Adopt Compose Watch only when mounts have a demonstrated problem or synchronization need. Do not combine two mechanisms that compete to update the same source. Keep container-managed dependencies separate from incompatible host dependencies. `tmpfs` is an optional measured optimization, not required test infrastructure; its memory cost and platform support must fit the project.
- DC-C5 — Expose a few commands using the project's existing script mechanism. Do not add Make, a task runner, a verification skill or application services just to implement this preset. Measure build/startup/check/cleanup separately when an approved slow check needs optimization rather than guessing where time goes.

## Commands to record in the project guide

These are command responsibilities, not scripts supplied by this template. Record actual working directories, Compose files/project identities, services, connection selection and commands for the target project.

| Suggested name | Responsibility |
| --- | --- |
| `dev` | Start/reuse the development stack with reload; build only if needed |
| `test-unit` | Run fast tests without bringing up dependent services |
| `test-integration` | Start/reuse only isolated test dependencies, establish schema/readiness, run the approved selection and reset between cases |
| `test-integration-clean` | Remove only that test session's project and disposable storage after checking its identity |
| `check-deploy` | Explicit production-style image/startup/proxy/persistence checks limited to the requested risk |

Document whether tests run on the host or in a one-off container and how they reach dependencies. A one-off container must receive test-only settings; reusing the dev image does not mean inheriting development database credentials. Reuse cached images/dependencies when valid, not stale application code.

Adopting this preset is not permission to deploy to a live environment. Production-style local checks need separate data and nonconflicting ports; cleanup must never target real production data. State checks not run and prepare concrete human validation steps at story delivery.

## Technical references

[Compose file merging](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/), [Compose project names](https://docs.docker.com/compose/how-tos/environment-variables/envvars/), [Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/), [production configuration](https://docs.docker.com/compose/how-tos/production/), [tmpfs mounts](https://docs.docker.com/engine/storage/tmpfs/). The lifecycle and separation rules above are this preset's defaults, not a requirement to scaffold all files in advance.
