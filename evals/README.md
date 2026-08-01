# Rights by Design — Evaluation Harness

Machine-runnable checks that the skill produces the right assessment: correct impact tier,
correct sector overlay, the seeded rights gaps flagged (not marked "met"), the right bottom
line, and coverage of the key substantive findings. Deterministic checks gate regressions;
an optional LLM judge scores substance against a rubric.

## Layout

```
cases/       structured test cases (system description + expected findings)
expected/    human-readable scoring rubrics, one per case
schemas/     assessment-schema.json — the structured output the skill must emit
run-evals.py the harness
reports/     generated results (safe to gitignore)
```

## Run

```
pip install anthropic jsonschema
export ANTHROPIC_API_KEY=sk-...
export RBD_EVAL_MODEL=<a model id you have access to>
python run-evals.py            # deterministic checks (exits non-zero on failure)
RBD_JUDGE=1 python run-evals.py # also run the rubric judge
```

The harness loads the shipping skill from
`plugins/rights-by-design/skills/rights-by-design/SKILL.md`, so it tests exactly what users install.

## Add a case

1. Add `cases/<sector>-NNN.json` with a `system_description` and an `expected` block
   (`impact_tier`, `sector_overlays_include`, `dimensions_not_met`, `bottom_line`, `must_mention`).
2. Optionally add a rubric at `expected/<sector>-NNN.md` for the judge.

`run-evals.py` exits non-zero if any case fails, so it can gate CI.
