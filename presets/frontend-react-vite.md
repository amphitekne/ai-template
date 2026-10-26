# frontend-react-vite

Apply through the [preset procedure](README.md). Scope: the selected web frontend. Restrictions are mandatory once adopted; conventions are defaults whose exceptions need navigator acceptance.

## Restrictions

- WEB-R1 — Use React, Vite, Zod and pnpm. Record compatible Node, pnpm and dependency versions in the scoped guide/configuration when adopting or initializing; do not guess current versions or add a second package manager. Commit `pnpm-lock.yaml`. In a pnpm monorepo, use the existing root workspace/lockfile rather than generating competing package-local lockfiles.
- WEB-R2 — Validate untrusted external data with Zod at the boundary: API responses, form submissions and relevant persisted/browser inputs. Infer types from schemas instead of maintaining duplicate shape definitions. Do not replace validation with type assertions or parse the same validated data at every layer. Frontend validation improves feedback; backend validation and authorization remain required.
- WEB-R3 — Organize by feature/business module, separating `domain`, `application`, `infrastructure` and `presentation` responsibilities. Domain/application contain business decisions and use cases without React, browser transport or Vite imports. Infrastructure owns HTTP/storage adapters; presentation owns components, hooks and screens. Wire dependencies at composition. Only add ports/adapters for actual boundaries; do not force a use-case class for every click.
- WEB-R4 — Define palette, semantic colors, radii, typography, spacing and other shared visual tokens in one canonical source file, such as `src/design-system/tokens.css`. Components consume semantic CSS custom properties rather than repeating raw theme values. Changing that file must propagate throughout the interface. Theme variants live in the same source. If a chosen tool needs another format, derive it from the canonical source; do not hand-maintain a second palette or JS theme. Shared tokens do not require every content-specific measurement to become a global token.
- WEB-R5 — Build reusable UI primitives and feature components with explicit props, semantic HTML, keyboard support and visible focus states. Keep business-specific behavior in its feature; shared design-system components must not depend on feature internals. Extract a reusable component when there is a real repeated pattern or coherent UI responsibility, not speculative future reuse.
- WEB-R6 — Features expose explicit public entry points; do not reach into another feature's private components, state or adapters. Resolve genuine cross-feature interactions through small public contracts/composition, keeping business layers independent of React. Do not create an event bus, global store or shared dependency cycle by default.

## Conventions

- WEB-C1 — Prefer TypeScript with strict checking to make schema-derived contracts useful throughout the code. This is a preset default, not a claim that the project already uses TypeScript. Record an accepted JavaScript exception if required by the target project.
- WEB-C2 — Keep design-system tokens and primitives centralized. For one frontend, keep them local; extract a shared workspace package only when multiple consumers need it. Make loading, empty, error and validation states explicit where applicable. Do not select a UI library, styling framework, router or state library without a concrete need and an accepted choice.
- WEB-C3 — Default to fast unit tests of logic/schemas and focused component interaction tests where useful. Human checks cover complete browser flows, theme-token propagation and visual quality by default; record steps and remaining risks. Browser E2E and deployment builds are separate explicit/accepted-project checks, not automatic prerequisites for each edit. Record lightweight iteration/closing commands; choose tools only when needed, without snapshot-heavy coverage by default.
- WEB-C4 — Run project scripts with pnpm and document their working directory. A build succeeding does not replace type checks or tests. Define only the scripts required by selected tools and accepted work.

## Layout example

```text
src/
  app/                            # Composition and screen wiring
  modules/<feature>/
    domain/
    application/
    infrastructure/
    presentation/
    index.ts                      # Public feature entry point
  design-system/
    tokens.css                    # Canonical visual tokens
    components/
```

This is an ownership example, not an instruction to scaffold empty directories. Exact versions, test runner, styling approach, routing, state management and backend contract integration are resolved only when needed.

## Technical references

Check current requirements when applying: [Vite](https://vite.dev/guide/), [Zod validation and inferred types](https://zod.dev/basics), [pnpm workspaces](https://pnpm.io/workspaces), [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties). Architecture and canonical-token rules are this preset's choices.
