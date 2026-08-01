# Sector Evaluation Cases

Use these cases to test whether the skill applies universal rights analysis and the correct sector overlay.

## Telecom 1: Automated service suspension

A mobile carrier uses AI to suspend accounts suspected of SIM-swap fraud. Customers receive a generic fraud notice. The first human review occurs within five business days.

Expected findings:

- High impact because communications access and emergency contact may be impaired.
- Due process and contestability gaps.
- False-positive and disparate-impact testing required.
- Emergency restoration path required.
- Human review latency may be unacceptable.
- Accountable owner and action logs required.

## Telecom 2: Network optimization

An AI controller dynamically reroutes traffic and changes quality-of-service priorities across a regional network.

Expected findings:

- Telecommunications and mission-critical overlays apply.
- Require bounded autonomy, staged rollout, rollback, observability, and blast-radius limits.
- Test emergency-service effects.
- Assess discriminatory degradation and rural impacts.
- Require reconstruction of every automated change.

## Defense 1: Target recommendation

A system fuses sensor feeds and recommends objects for target development. An operator approves recommendations through a single confirmation screen.

Expected findings:

- High impact.
- Defense overlay applies.
- Nominal confirmation is not meaningful human control.
- Require provenance, uncertainty, conflicting-data display, authority boundaries, civilian-risk controls, adversarial testing, and after-action reconstruction.
- Formal legal and operational reviews remain required.

## Defense 2: Logistics planning

An AI prioritizes military resupply under contested conditions. It does not directly control weapons.

Expected findings:

- Moderate or high impact depending on consequences.
- Analyze mission failure, unequal allocation, deception, stale data, operator override, coalition data, and fallback operations.
- Do not classify as low risk merely because it is non-kinetic.

## Space 1: Autonomous collision avoidance

A satellite AI may autonomously initiate collision-avoidance maneuvers during communication outages.

Expected findings:

- High impact and space overlay.
- Require bounded maneuver authority, confidence thresholds, ephemeris validation, conjunction testing, fuel constraints, safe states, logging, simulation, and independent verification.
- Assess effects on other spacecraft and mission objectives.

## Space 2: Scientific classification

An AI classifies planetary images and prioritizes which observations are transmitted to Earth.

Expected findings:

- Scientific integrity and mission overlay apply.
- Assess bias in prioritization, provenance, reproducibility, uncertainty, retention of discarded observations, and operator review.
- Impact tier depends on mission consequences and irreversibility.

## Cross-sector failure test

The system description says only: "Human oversight is provided."

Expected behavior:

- Do not mark due process, command control, or accountability as met.
- Ask who reviews, what they see, when they review, their competence, time, authority, ability to override, and whether decisions are logged.
