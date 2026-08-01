# Rights by Design Skill

A portable AI-governance review framework for ChatGPT, Claude, and other capable AI assistants.

Rights by Design moves civil-rights, accountability, safety, resilience, and mission-assurance requirements upstream—into product design, architecture, procurement, operations, testing, and command structures before deployment.

## Version 2.0

Version 2.0 adds sector overlays for:

- Telecommunications and communications infrastructure
- Department of Defense and national-security systems
- NASA and civil or commercial space systems
- Mission-critical and critical-infrastructure environments

The five universal dimensions remain:

1. Privacy and cognitive liberty
2. Due process and algorithmic dignity
3. Equal protection and nondiscrimination
4. Transparency and contestability
5. Accountability and democratic control

## Use in any AI assistant

1. Open `SKILL.md`.
2. Copy the complete file.
3. Paste it into a new conversation as the governing instructions.
4. Provide a system description, PRD, model card, procurement package, operational concept, architecture, or mission profile.
5. Ask: `Run a Rights by Design review.`

## Use in ChatGPT

For a reusable custom GPT:

1. Create a custom GPT.
2. Paste `chatgpt/INSTRUCTIONS.md` into the GPT Instructions field.
3. Upload `SKILL.md` and the files in `sector-modules/` as Knowledge.
4. Add representative evaluation cases from `evals/`.
5. Enable web access when current laws, standards, agency policies, or regulations must be verified.
6. Test in Preview before sharing.

Suggested conversation starters:

- Review this AI system using Rights by Design.
- Turn this product concept into testable rights and safety requirements.
- Assess this telecom AI system and identify deployment blockers.
- Review this defense AI concept for command, accountability, and civilian-risk gaps.
- Review this space-system autonomy design for safety and mission-assurance gaps.
- Compare these two vendors using Rights by Design.

## Repository structure

```text
rights-by-design-skill/
├── README.md
├── SKILL.md
├── chatgpt/
│   ├── INSTRUCTIONS.md
│   ├── CONFIGURATION.md
│   ├── CONVERSATION_STARTERS.md
│   └── KNOWLEDGE_GUIDE.md
├── knowledge/
│   ├── methodology.md
│   ├── glossary.md
│   ├── worked-examples.md
│   └── sector-modules/
│       ├── employment.md
│       ├── lending.md
│       ├── healthcare.md
│       └── government.md
├── sector-modules/
│   ├── telecommunications.md
│   ├── defense-national-security.md
│   └── nasa-space-systems.md
├── evals/
│   ├── test-cases.md
│   ├── expected-findings.md
│   ├── regression-checklist.md
│   └── sector-test-cases.md
└── examples/
    ├── resume-screening-review.md
    ├── lending-review.md
    └── benefits-eligibility-review.md
```

## Limits

Rights by Design is a design and governance aid. It does not provide legal advice or certify compliance. It is not a substitute for agency, command, legal, privacy, cybersecurity, safety, engineering, acquisition, accessibility, civil-rights, weapons, airworthiness, flight-readiness, or mission-assurance review.

## Attribution

Rights by Design operationalizes the framework developed by Rani Yadav-Ranjan in *Constitutional Democracy in the Algorithmic Age: A Practical Framework for Preserving Citizen Rights* (Springer Nature, 2026).


## Canonical specification

See `FRAMEWORK_SPEC.md` for platform-neutral conformance requirements. `SKILL.md` is the portable AI implementation.


## Documentation and tools

- `docs/` — installation and methodology guides
- `templates/` — reusable assessment and governance forms
- `research/` — standards crosswalks and machine-readable schema
- `book/` — publication context and citation
- `assets/` — diagrams and visual assets
