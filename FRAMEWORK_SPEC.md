# Rights by Design Framework Specification

**Specification version:** 1.0.0  
**Framework author:** Rani Yadav-Ranjan  
**Status:** Initial public specification

## 1. Purpose

This document is the canonical, platform-neutral specification for Rights by Design. It defines the minimum requirements for an implementation that claims compatibility with the framework.

Rights by Design moves rights, accountability, safety, resilience, and remedy upstream into system architecture, product requirements, procurement, testing, operations, and governance.

## 2. Conformance language

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** describe implementation requirements.

An implementation is conformant only when it:

1. applies all five universal dimensions;
2. assigns an impact tier;
3. activates all applicable sector overlays;
4. distinguishes facts, inferences, unknowns, and recommendations;
5. identifies owners, evidence, and deployment blockers;
6. avoids unsupported compliance or certification conclusions;
7. provides a bottom-line deployment determination.

## 3. Unit of analysis

The system under review MUST include the relevant sociotechnical environment:

- intended purpose and prohibited uses;
- models, software, hardware, and interfaces;
- training, validation, and operating data;
- inferred attributes and derived signals;
- operators and decision-makers;
- vendors, subcontractors, and infrastructure;
- affected people, communities, institutions, and missions;
- downstream actions and consequences;
- notices, correction, appeal, and remedy;
- logs, monitoring, audits, incidents, and shutdown authority.

## 4. Impact tiers

### 4.1 High impact

A system MUST be classified high impact when it can materially affect liberty, safety, livelihood, legal rights, civic participation, reputation, essential services, communications, critical infrastructure, national security, or mission success.

### 4.2 Moderate impact

A system SHOULD be classified moderate impact when it materially influences consequential decisions, operations, resource allocation, or opportunity but does not ordinarily impose the final outcome.

### 4.3 Limited impact

A system MAY be classified limited impact when foreseeable errors are unlikely to materially impair rights, safety, essential access, or mission outcomes.

### 4.4 Tiering rule

Impact MUST be based on reasonably foreseeable consequence, not model size, marketing label, nominal human involvement, or the absence of explicit protected-class fields.

## 5. Evidence classes

Every material statement MUST be identified as one of:

- **Confirmed fact:** directly supported by supplied evidence.
- **Reasonable inference:** supported by facts but not directly established.
- **Unknown:** material information is absent or inadequate.
- **Recommendation:** a proposed control or requirement.

A written policy MUST NOT be treated as proof that a safeguard operates.

## 6. Status values

Each universal dimension MUST receive one status:

- **Met**
- **Partial**
- **Gap**
- **Not enough information**
- **Not applicable**

“Met” requires operational evidence. “Not applicable” MUST be explained and used sparingly.

## 7. Universal dimensions

### 7.1 Privacy and cognitive liberty

The implementation MUST assess collection, inference, retention, sharing, purpose limitation, surveillance, sensitive attributes, manipulation, location, behavior, relationships, and decisional autonomy.

### 7.2 Due process and algorithmic dignity

The implementation MUST assess notice, factual accuracy, opportunity to correct, opportunity to be heard, meaningful human judgment, consistency, timing, and protection against arbitrary outcomes.

### 7.3 Equal protection and nondiscrimination

The implementation MUST assess representation, historical labels, proxies, subgroup and intersectional performance, accessibility, disparate treatment, disparate impact, monitoring, thresholds, and remediation.

### 7.4 Transparency and contestability

The implementation MUST assess disclosure, explanation, input access, correction, challenge, contrary evidence, qualified review, timeliness, reversal, and remedy.

### 7.5 Accountability and democratic control

The implementation MUST assess accountable ownership, authority, logs, documentation, vendors, audits, incidents, change control, oversight, and suspension or shutdown authority.

## 8. Meaningful human control

A claim of human oversight MUST be tested for:

- identity and role;
- competence and training;
- evidence and uncertainty presented;
- time available;
- independence;
- authority to reject, modify, reverse, pause, or stop;
- documentation and monitoring of decisions.

Nominal confirmation MUST NOT be treated as meaningful human control.

## 9. Sector overlays

Sector overlays supplement, but MUST NOT replace, the universal dimensions. Multiple overlays MAY apply simultaneously.

Supported overlays include:

- employment;
- lending;
- healthcare;
- government and public services;
- telecommunications;
- defense and national security;
- NASA and space systems;
- education;
- insurance;
- law enforcement;
- critical infrastructure;
- energy;
- transportation;
- robotics;
- manufacturing;
- biometrics;
- smart cities.

## 10. Required output schema

A conformant review MUST include:

1. System summary
2. Impact tier
3. Applicable sector overlays
4. Five-dimension scorecard
5. Sector and mission findings
6. Build-in-before-ship requirements
7. Open questions
8. Bottom line

Each build-in requirement MUST identify:

- required change;
- responsible role;
- evidence of completion;
- acceptance test where useful;
- deployment blocker status.

## 11. Deployment decisions

The bottom line MUST use one of:

- **Ready to proceed**
- **Proceed only with specified conditions**
- **Not ready for deployment**
- **Insufficient information for a defensible determination**

## 12. Deployment blockers

Presumptive blockers include:

- absent legal or operational authority where required;
- unbounded consequential autonomy;
- no meaningful human review;
- no correction, appeal, or remedy for consequential decisions;
- no subgroup or safety validation for a high-impact use;
- no decision reconstruction;
- no accountable owner;
- no safe state, rollback, abort, or shutdown where necessary;
- use beyond validated scope;
- vendor secrecy that prevents governance or audit.

## 13. Machine-readable compatibility

Compatible machine-readable assessments SHOULD implement the schema in `research/assessment-schema.json`.

## 14. Limits

Conformance with this specification is not legal advice, regulatory compliance, safety certification, weapons approval, airworthiness approval, flight readiness, clinical authorization, or operational command authority.
