---
name: rights-by-design
description: "Assess or design an AI system for citizen rights at the design stage: privacy, due process, equal protection, contestability, accountability. Produces a rights-by-design scorecard and fixes."
---

# Rights by Design: AI Governance Review

*Version 1.0*

## What this does
Applies the rights-by-design method to an AI system: engineer citizen protections into the architecture before deployment, rather than retrofitting them after harm. Give it a system, feature, spec, PRD, or model card, and it returns a structured assessment across five protection dimensions with concrete fixes to build in before ship. It works two ways: as a review of an existing or planned system, or as a design aid that generates rights requirements for something new.

## First, set the impact tier
Ask what the system actually decides, and calibrate scrutiny to the stakes.
- High stakes: decisions touching liberty, livelihood, safety, or access to essential services, such as credit, employment, benefits, housing, healthcare, justice, or a border. Apply every dimension fully, and require human control and independent review.
- Everyday: lower-stakes personalization or convenience. Apply the same dimensions proportionally.
A system causes real harm while working exactly as designed, so tier by what a wrong or unaccountable decision costs a person, not by the size of the model.

## The five dimensions
For each, state whether it is met, partial, or a gap, give the finding, and give one concrete build-in fix.

1. **Privacy and cognitive liberty.** What is collected, and more importantly what is inferred. Are sensitive attributes inferred without consent. Are collection and inference minimized to the stated purpose. Are retention and processing limited and verifiable. Does it protect decisional autonomy, not only data.

2. **Due process and algorithmic dignity.** Before a consequential decision stands, is there notice, a basis the person can understand, and meaningful human judgment rather than nominal review. Is the person treated as a person, with a real path to be heard.

3. **Equal protection.** Has it been tested for disparate impact across protected groups, on representative data, before deployment and on a schedule afterward. Are the results documented and acted on.

4. **Transparency and contestability.** Can an affected person not only be told about a decision but challenge it. Is there a genuine appeal with the power to reverse. Is the system explainable enough that a challenge can actually succeed. Transparency without contestability is a notice, not a right.

5. **Accountability.** Is a specific human accountable for the outcome. Are there records of who decided what and when. Can an auditor reach the algorithm and the training data. For high-stakes systems, is there independent oversight, and does human control scale with the stakes.

## Output
Return, in this order:
- A one-line impact tier and why.
- A five-row scorecard: dimension, status (met, partial, or gap), and a one-line finding.
- A prioritized "build in before ship" list: the gaps to close at the design stage, hardest-to-retrofit first.
- One honest bottom line: is this system ready to deploy against the rights it touches, or not yet.

Be specific and practical. Name the fix, not just the principle. Do not invent facts about the system; if something is unknown, list it as an open question to resolve before ship.

## Principle
Rights retrofitted after harm are rights in name only. The whole method is to move the protections upstream into the design, where they are cheap to build and hard to remove, instead of downstream into litigation, where they are expensive and too late.

## Use and limits
This is a design and review aid, not legal advice. Its findings reflect only the information provided and do not certify compliance with any law, regulation, or standard. Treat a clean scorecard as a prompt for human judgment, not a guarantee.

---

*Based on the rights-by-design framework in Rani Yadav-Ranjan's* Constitutional Democracy in the Algorithmic Age *(Springer Nature, 2026). More at yadav-ranjan.com.*
