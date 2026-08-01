# Repository Architecture

## Governing layer

- `FRAMEWORK_SPEC.md` is the canonical, platform-neutral specification.
- `SKILL.md` is the compact portable AI implementation.
- `chatgpt/INSTRUCTIONS.md` configures the ChatGPT implementation.

## Knowledge layer

- `knowledge/methodology.md` explains the analytical method.
- `knowledge/glossary.md` controls terminology.
- Sector modules add domain-specific requirements without replacing the five universal dimensions.

## Application layer

- `templates/` provides reusable governance artifacts.
- `examples/` demonstrates expected output.
- `research/assessment-schema.json` supports structured integrations.

## Assurance layer

- `evals/` contains tests, expected findings, scoring, edge cases, and release gates.
- `.github/workflows/` performs lightweight repository validation.

## Documentation layer

- `docs/` supports installation and use.
- `research/` contains non-authoritative standards crosswalks.
- `book/` preserves publication attribution and citation context.
- `assets/` contains diagrams and visual materials.
