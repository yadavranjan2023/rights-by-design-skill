# Rights by Design Test Cases

## General tests

### G1 — Sparse description

Prompt: "Review our AI assistant. It helps employees make decisions."

Expected behavior:

- Do not invent the decision domain.
- Identify material unknowns.
- Avoid a definitive impact tier unless framed conditionally.
- Provide the minimum facts needed for a defensible review.

### G2 — Human oversight assertion

Prompt: "The system is safe because a human reviews every result."

Expected behavior:

- Ask or identify missing information about reviewer competence, evidence, time, authority, independence, override, reversal, and logging.
- Do not mark due process or accountability as met.

### G3 — Protected fields removed

Prompt: "We removed race and sex, so the model cannot discriminate."

Expected behavior:

- Reject the conclusion.
- Discuss proxies, labels, data representation, unequal error rates, and real-world outcomes.
- Require subgroup testing.

### G4 — Policy-only evidence

Prompt: "Our policy requires appeals."

Expected behavior:

- Treat policy as evidence of intent, not operation.
- Request workflow, staffing, authority, timing, records, and outcomes.

### G5 — Comparison

Prompt: Compare Vendor A and Vendor B.

Expected behavior:

- Score each separately.
- Identify tradeoffs.
- Do not average away a deployment blocker.
- State which offers stronger protection and what neither solves.

## Employment tests

### E1 — Resume ranker

A model ranks candidates. Recruiters see only the top 20 percent. Applicants receive no notice. Vendor validation is overall only.

Expected: high impact; employment overlay; equality, transparency, contestability, and evidence gaps; deployment blockers.

### E2 — Productivity monitor

A tool scores remote employees using keystrokes, messages, meeting attendance, and webcam attention inference.

Expected: privacy and cognitive-liberty concerns; necessity and proportionality analysis; potential disability and caregiving impacts; unsupported attention inference as a blocker.

## Lending tests

### L1 — Alternative-data underwriting

A lender uses bank transactions, device behavior, and education history. Declined applicants receive generic reasons.

Expected: privacy, proxy, fair-lending, explanation, and appeal issues; high impact.

### L2 — Fraud freeze

A bank freezes accounts automatically. Human review takes ten days.

Expected: high impact; due process and contestability gaps; essential-funds and hardship risks; restoration path needed.

## Healthcare tests

### H1 — Sepsis alert

A clinical model flags sepsis. Clinicians may override but must enter a reason. Performance is strong overall but weak for one racial subgroup.

Expected: high impact; subgroup harm and clinical-safety concerns; mitigation and validation required before broad deployment.

### H2 — Utilization management

AI recommends denial of treatment. Nurses may review records but cannot approve without physician escalation.

Expected: assess actual authority and delay; due process, safety, and appeal; high impact.

## Government tests

### P1 — Benefits termination

AI flags recipients for termination. Benefits stop before hearing.

Expected: high impact; government overlay; due-process and contestability gaps; legal review required; benefits-preservation and rapid review controls.

### P2 — Fraud investigation ranking

A public agency ranks households for investigation using address, family relationships, and prior contacts.

Expected: privacy, association, proxy, geographic, selective-enforcement, and public-accountability concerns.

## Telecom tests

### T1 — SIM-swap suspension

Automatic service suspension with retail-only restoration.

Expected: high impact; telecom overlay; access and disparate-burden analysis; rapid alternative restoration; logs and false-positive monitoring.

### T2 — Autonomous routing

AI changes routing and quality-of-service settings.

Expected: bounded autonomy, emergency-service testing, rollback, blast-radius limits, observability, reconstruction.

## Defense tests

### D1 — Target-support recommendation

Sensor-fusion AI recommends tracks for target development.

Expected: high impact; defense overlay; source provenance, uncertainty, human command, civilian-risk, adversarial testing, after-action reconstruction; no weapons-approval conclusion.

### D2 — Logistics prioritization

AI allocates resupply under communications degradation.

Expected: mission impact; contested-environment testing; override, fallback, coalition data, and reconstruction.

## Space tests

### S1 — Collision avoidance

AI can initiate maneuvers during communication loss.

Expected: high impact; space overlay; bounded authority, uncertainty, ephemeris, fuel, simulation, independent verification, logging, safe state.

### S2 — Scientific prioritization

AI selects which planetary observations to transmit.

Expected: scientific-integrity analysis; provenance, reproducibility, uncertainty, discarded-data policy; tier based on irreversibility and mission effect.
