---
name: rights-by-design
description: "Assess or design an AI system for citizen rights at the design stage: privacy, due process, equal protection, contestability, accountability, and mission-critical safeguards. Produces a rights-by-design scorecard and concrete fixes."
version: "2.0"
---

# Rights by Design: AI Governance Review

## What this does

Applies the Rights by Design method to an AI system: engineer citizen protections into the architecture before deployment rather than retrofitting them after harm.

Give it a system, feature, specification, PRD, model card, procurement document, operational concept, or mission profile. It returns a structured assessment across five universal rights dimensions, plus sector-specific safeguards where applicable.

It works in three modes:

- **Review mode:** assess an existing or planned system.
- **Design mode:** generate rights, governance, safety, and accountability requirements for something new.
- **Comparison mode:** compare systems, vendors, architectures, or policies.

## First, set the impact tier

Ask what the system actually decides, recommends, controls, or enables. Calibrate scrutiny to the consequences.

- **High impact:** systems affecting liberty, livelihood, safety, legal rights, civic participation, reputation, access to essential services, national security, critical infrastructure, communications, or mission success. Apply every dimension fully. Require meaningful human control, traceability, testing, independent review, and a defined stop or override authority.
- **Moderate impact:** systems that materially influence people, operations, resource allocation, or institutional decisions but ordinarily do not make the final consequential decision. Apply every dimension with controls proportionate to foreseeable harm.
- **Limited impact:** lower-risk personalization, convenience, administrative support, or content functions whose errors are unlikely to materially impair rights, safety, access, or mission outcomes.

Tier by what a wrong, biased, insecure, unexplained, or unaccountable decision could cost an affected person, institution, population, mission, or public system—not by the size of the model.

## The five universal dimensions

For each dimension, state whether it is **met**, **partial**, **gap**, **not enough information**, or **not applicable**. Give the finding, supporting evidence or missing information, and one concrete build-in fix.

1. **Privacy and cognitive liberty.** What is collected, inferred, retained, shared, or repurposed? Are sensitive attributes, behavior, location, beliefs, relationships, vulnerabilities, or intentions inferred without necessity or meaningful consent? Are collection and inference minimized and verifiable? Does the system protect decisional and cognitive autonomy, not only data?

2. **Due process and algorithmic dignity.** Before a consequential decision stands, is there notice, an understandable basis, a chance to correct facts, and meaningful human judgment rather than nominal review? Is the person treated as a person, with a real opportunity to be heard?

3. **Equal protection and nondiscrimination.** Has the system been tested for disparate treatment and disparate impact across protected and affected groups, using representative data, before deployment and on a defined schedule afterward? Are accessibility, language, geography, disability, and intersectional effects evaluated? Are results documented and acted on?

4. **Transparency and contestability.** Can an affected person know that AI is materially involved, understand its role, inspect or correct relevant inputs, challenge the outcome, submit contrary evidence, reach a qualified human reviewer, and obtain reversal or remedy? Transparency without contestability is notice, not a right.

5. **Accountability and democratic control.** Is a specific human or organizational role accountable for the outcome? Are decisions, data access, model changes, overrides, incidents, and approvals recorded? Can authorized reviewers reach the system, documentation, data lineage, and relevant evidence? Is there independent oversight proportionate to the stakes?

## Sector and mission overlay

After applying the five universal dimensions, determine whether one or more sector overlays apply.

Use the applicable module when the system operates in:

- telecommunications or communications infrastructure;
- defense, intelligence, homeland security, or national security;
- NASA, civil space, commercial space, launch, satellite, or mission-control environments;
- other critical infrastructure or safety-critical environments.

Sector overlays supplement the five dimensions. They do not replace them.

### Telecommunications overlay

Evaluate:

- communications privacy, metadata, location information, and inferred relationships;
- network neutrality, equitable access, digital inclusion, and discriminatory throttling;
- automated suspension, denial, prioritization, routing, or quality-of-service decisions;
- emergency communications, 911/E911, public warning, and outage resilience;
- lawful-interception authorization, separation of duties, logging, and misuse prevention;
- fraud, robocall, identity, SIM-swap, and account-takeover controls;
- spectrum, satellite, roaming, interconnection, and cross-border data risks;
- supply-chain, vendor, cloud, and network-management security;
- rollback, graceful degradation, manual operation, and customer remedy.

### Defense and national-security overlay

Evaluate:

- compliance with applicable law, policy, command authority, and rules of engagement;
- meaningful human command and control over consequential or force-related decisions;
- civilian protection, distinction, proportionality, escalation, and fratricide risks;
- target identification, sensor fusion, uncertainty, provenance, and data integrity;
- autonomous-function boundaries and prohibited actions;
- adversarial robustness, deception, spoofing, cyber compromise, and contested operations;
- operator workload, automation bias, training, and interface clarity;
- classified-data handling, coalition sharing, compartmentation, and insider risk;
- traceability, after-action reconstruction, accountability through the chain of command;
- fail-safe behavior, abort, disengagement, fallback, and mission-assurance requirements.

### NASA and space-systems overlay

Evaluate:

- crew, public, vehicle, payload, and mission safety;
- launch, flight, rendezvous, docking, landing, robotics, and autonomous-navigation risks;
- fault detection, isolation, recovery, redundancy, graceful degradation, and safe modes;
- communication delay, intermittent connectivity, and long-duration autonomy;
- radiation, extreme-environment, hardware, software, and sensor resilience;
- orbital-debris mitigation, conjunction assessment, and collision avoidance;
- telemetry, command authentication, data provenance, and ground-segment security;
- explainability and operator intervention under time-critical conditions;
- scientific integrity, reproducibility, data-quality controls, and research independence;
- planetary protection and contamination controls where applicable;
- configuration control, verification, validation, simulation, test coverage, and mission assurance.

## Mission-critical requirements

For any high-impact, safety-critical, defense, telecommunications, or space system, verify:

- clearly bounded autonomy;
- human override or command authority appropriate to the mission;
- fail-safe behavior and graceful degradation;
- rollback, recovery, and manual fallback;
- redundancy and fault tolerance;
- uncertainty estimates visible to decision-makers;
- adversarial robustness and cybersecurity;
- immutable or protected audit logging;
- configuration and change control;
- simulation, verification, validation, and red-team testing;
- incident response and after-action reconstruction;
- named authority to pause, disable, abort, or shut down the system.

Do not treat a nominal human-in-the-loop as meaningful control. Identify who the human is, what information they receive, how much time they have, what authority they possess, and whether they can depart from or reverse the system.

## Sector module library

The overlays above cover the mission-critical sectors inline. The full module library ships beside this file in `references/sectors/`. When the system fits one or more sectors below, load the matching module and apply its scope, rights-specific review, sector controls, required evidence, and deployment blockers on top of the five universal dimensions. More than one may apply. If none fits, run the universal core alone and say so.

| Sector | Load |
|---|---|
| Employment & HR | `references/sectors/employment.md` |
| Lending & Credit | `references/sectors/lending.md` |
| Insurance | `references/sectors/insurance.md` |
| Healthcare | `references/sectors/healthcare.md` |
| Government & Public Services | `references/sectors/government.md` |
| Law Enforcement | `references/sectors/law-enforcement.md` |
| Biometrics | `references/sectors/biometrics.md` |
| Telecommunications | `references/sectors/telecommunications.md` |
| Defense & National Security | `references/sectors/defense-national-security.md` |
| NASA & Space Systems | `references/sectors/nasa-space-systems.md` |
| Critical Infrastructure | `references/sectors/critical-infrastructure.md` |
| Energy & Utilities | `references/sectors/energy.md` |
| Transportation | `references/sectors/transportation.md` |
| Robotics | `references/sectors/robotics.md` |
| Manufacturing | `references/sectors/manufacturing.md` |
| Smart Cities | `references/sectors/smart-cities.md` |
| Education | `references/sectors/education.md` |

## Output

Return, in this order:

1. **System summary:** what the system does, who operates it, who or what is affected, and what remains unknown.
2. **Impact tier:** tier, rationale, and principal foreseeable harm.
3. **Applicable sector overlays:** identify each applicable module and why.
4. **Rights-by-Design scorecard:** dimension, status, finding, evidence or missing information, and build-in safeguard.
5. **Mission and sector findings:** the most important sector-specific safety, resilience, command, infrastructure, or operational gaps.
6. **Build in before ship:** prioritized requirements, hardest-to-retrofit and most consequential first. For each, name the responsible role, evidence of completion, and whether it is a deployment blocker.
7. **Open questions:** unresolved facts that could materially change the assessment.
8. **Bottom line:** ready to proceed, proceed only with conditions, not ready, or insufficient information.

Be specific and practical. Name the control, owner, test, evidence, and decision authority—not merely the principle.

Do not invent facts. A policy statement is not proof that a safeguard operates. When a material fact is unknown, mark it as unknown and list the evidence needed before deployment.

## Principle

Rights retrofitted after harm are rights in name only. Move protections upstream into architecture, product requirements, operational concepts, procurement, testing, training, governance, and command structures, where they are cheaper to build and harder to remove.

## Use and limits

This is a design and governance aid, not legal advice, operational authorization, safety certification, an airworthiness or flight-readiness determination, a weapons review, or a finding of compliance with any law, regulation, policy, contract, or technical standard.

Defense, intelligence, telecommunications, aviation, and space systems require review by the appropriate legal, civil-rights, privacy, cybersecurity, safety, engineering, mission-assurance, accessibility, acquisition, and command authorities.

## About this skill

This skill operationalizes the **Rights by Design** framework from the book *Constitutional Democracy in the Algorithmic Age: A Practical Framework for Preserving Citizen Rights* by **Rani Yadav-Ranjan** (Springer Nature, 2026).

The book provides the broader legal and governance foundation spanning algorithmic decision-making, surveillance, biometrics, digital identity, discrimination, and emerging AI regulation.

**Author:** Rani Yadav-Ranjan  
**Framework:** Rights by Design  
**Version:** 2.0
