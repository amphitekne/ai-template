# backend-python-fastapi

Apply through the [preset procedure](README.md). Scope: the selected Python backend, not all packages in a repository. Restrictions are mandatory once adopted; conventions are defaults whose exceptions need navigator acceptance.

## Restrictions

- PY-R1 — Use Python 3.15, uv for environments/dependencies/commands, FastAPI for HTTP APIs, and Pydantic for structured API validation. Record the actual Python patch version and uv version on adoption/initial implementation; keep the supported Python range and development runtime consistent. Verify dependency and deployment compatibility before relying on them. Do not silently select another Python minor version.
- PY-R2 — Declare structured request bodies as Pydantic schemas. Use FastAPI's typed path, query, header and dependency validation for simple inputs. Do not manually read JSON and extract fields when a declarative schema expresses the contract. Raw request access is limited to a real protocol need, such as signature verification, streaming or passthrough; document that boundary and validate parsed structured data before use.
- PY-R3 — Every structured JSON success response has an explicit Pydantic output model, including typed collections/envelopes, declared through FastAPI's response model or a compatible return annotation. Do not expose bare `dict`, `dict[str, Any]`, `Any`, ORM objects or raw `JSONResponse` as an escape from a known output schema. Return explicit response models for structured results. Empty responses, files, streams and truly dynamic payloads have explicit documented contracts; exceptions to structured schema validation need a concrete reason. Separate input/output schemas when visibility differs; never expose secrets through serialization.
- PY-R4 — Organize by business module, with `domain`, `application`, `infrastructure`, and `presentation` responsibilities inside each module. Domain holds business rules and has no FastAPI, HTTP, ORM or infrastructure imports. Application orchestrates use cases and depends on domain and its own required ports. Infrastructure implements adapters; presentation validates/maps API input and output and calls use cases. Composition wires dependencies; dependencies point inward. Keep Pydantic API schemas in presentation and map to simple internal types instead of spreading HTTP models throughout domain.
- PY-R5 — Modules communicate only through explicitly exported public contracts/facades in the owning module's presentation boundary. Never import another module's private use cases, entities, repositories or tables, or access its persistence directly. A public facade is distinct from its HTTP router and does not require loopback HTTP calls. Keep domain/application isolated: when a use case needs another module, define a small application port and wire an adapter to the other module's facade. Public contracts must be transport-independent; no FastAPI request objects across modules. Avoid circular module dependencies.
- PY-R6 — Group related endpoints in module-owned `APIRouter` instances and register them at application composition. Endpoints handle transport and delegation; business logic belongs in domain/application. Keep authentication/authorization checks at appropriate boundaries and do not treat schema validation as authorization.

## Conventions

- PY-C1 — Use `pyproject.toml` and commit `uv.lock`; run project commands through `uv run`. Record the actual test, lint and type-check commands in the scoped guide once tools are selected. Do not add a second dependency manager or install tools globally as project dependencies.
- PY-C2 — Start with the first vertical slice. Layer names describe responsibilities, not a requirement for empty folders, base classes, generic repositories, a DI container or duplicate models with no boundary benefit. Use plain functions and explicit constructor/function dependencies where sufficient. Create ports only for real boundaries.
- PY-C3 — Validate external shape at the boundary and business invariants in domain; avoid re-parsing the same already validated object in every layer. Map expected domain/application failures to the API contract without leaking internal exceptions. Use precise types and readable names before clever abstractions.
- PY-C4 — Test observable API behavior and relevant domain rules with independent expected values. Cover invalid input, output shape/visibility, relevant error paths and module boundaries as required by the slice. Select a test runner in the project guide; this preset does not install one or replace RED approval.

## Layout example

```text
src/<package>/
  main.py                         # Composition and router registration
  modules/<business-module>/
    domain/
    application/
    infrastructure/
    presentation/
      router.py                   # HTTP adapter
      schemas.py                  # HTTP input/output models
      public.py                   # Explicit inter-module facade, when needed
```

This illustrates ownership; instantiate only the files a slice needs. Database, ORM, authentication mechanism, deployment and exact test/lint tools remain project decisions.

## Technical references

Check current compatibility when applying: [Python versions](https://devguide.python.org/versions/), [uv Python versions](https://docs.astral.sh/uv/concepts/python-versions/), [FastAPI response models](https://fastapi.tiangolo.com/tutorial/response-model/), [FastAPI routers](https://fastapi.tiangolo.com/tutorial/bigger-applications/). Architecture rules above are this preset's choices, not requirements imposed by FastAPI.
