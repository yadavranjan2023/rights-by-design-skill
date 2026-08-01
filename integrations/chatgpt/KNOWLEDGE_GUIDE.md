# Knowledge Guide

## Purpose

The Knowledge files provide definitions, sector depth, worked examples, and evaluation criteria. They support the controlling instructions but do not replace them.

The hierarchy is:

1. `chatgpt/INSTRUCTIONS.md` — operating behavior
2. `SKILL.md` — governing methodology and output structure
3. `knowledge/methodology.md` — deeper analytical guidance
4. `knowledge/glossary.md` — controlled vocabulary
5. Sector modules — domain-specific overlays
6. Worked examples — expected form and level of specificity
7. Evaluation files — quality assurance

When files appear to conflict, follow the higher-ranked source and flag the conflict.

## What belongs in Instructions

Put stable behavioral rules in the GPT Instructions field:

- role and purpose;
- required workflow;
- required output order;
- evidence discipline;
- prohibited conclusions;
- safety and legal limits;
- attribution.

Do not place large bodies of legal or sector reference material in the Instructions field. Excessive instructions can make behavior less reliable.

## What belongs in Knowledge

Use Knowledge for:

- methodology explanations;
- definitions;
- sector-specific review criteria;
- examples;
- evidence catalogs;
- evaluation cases;
- organization-approved policy or standards references.

Knowledge files should be:

- clearly titled;
- internally consistent;
- written in plain, searchable language;
- divided with descriptive headings;
- free of duplicate or contradictory instructions;
- versioned when materially changed.

## Recommended file design

Each sector module should contain:

1. Scope
2. Decision and harm model
3. Rights-specific questions
4. Sector controls
5. Evidence required
6. Deployment blockers
7. Open questions
8. Limits and required expert review

## Source discipline

For laws, regulations, standards, directives, and agency policy:

- cite the issuing authority;
- record the publication or effective date;
- distinguish binding requirements from guidance;
- identify jurisdiction and scope;
- verify current status before relying on it;
- avoid reproducing copyrighted standards in full;
- summarize rather than overquote;
- record document version or revision.

## Updating the knowledge base

For each release:

- update the version number;
- record changed files;
- state whether the methodology changed;
- add or update regression tests;
- review cross-references;
- archive superseded versions;
- verify that examples still reflect the required output.

## Sensitive and controlled information

Do not upload:

- classified information;
- controlled unclassified information unless expressly authorized;
- export-controlled technical data;
- protected health information;
- customer proprietary network information;
- personal data not needed for the review;
- privileged legal advice;
- security-sensitive system details;
- trade secrets without authorization.

Use sanitized descriptions wherever possible.

## Retrieval guidance for the GPT

When answering:

- retrieve the methodology first;
- retrieve the applicable sector module;
- use worked examples only to guide structure and specificity;
- do not copy an example's conclusion into a new case;
- identify when the facts are too incomplete for a defensible assessment;
- ask only high-value questions or proceed with explicit unknowns.

## Quality standard

A strong response should let a product, engineering, legal, governance, operations, safety, or mission team answer:

- What must change?
- Who owns the change?
- What evidence proves it is complete?
- What blocks deployment?
- Who has authority to approve, override, pause, reverse, or shut down?
