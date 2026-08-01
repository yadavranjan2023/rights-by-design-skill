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

## Government 1: Benefits fraud flagging

A state auto-scores benefits cases for fraud; high scores route to caseworkers who terminate in most cases, and benefits stop before a hearing.

Expected findings:

- High impact; government overlay.
- Due-process gap: termination before meaningful review; no AI-specific notice.
- Require legal authority, subgroup/geographic testing, evidence access, and a suspension authority.

## Lending 1: Auto-decline underwriting

A lender auto-declines the bottom band of applicants using alternative data; declines issue a generic adverse-action letter.

Expected findings:

- High impact; banking/finance overlay.
- Specific adverse-action reasons required; disparate-impact and less-discriminatory-alternative testing required.
- Proxy features need documented justification; human appeal for declines.

## Employment 1: Resume ranking

A tool ranks applicants and only the top band reaches a recruiter; the model was trained on incumbent employees.

Expected findings:

- High impact; employment overlay.
- Adverse-impact (four-fifths) analysis required; job-relatedness for each scored feature.
- Candidate notice, human review, and accommodation paths required.

## Healthcare 1: Prior authorization

An AI auto-denies or pends prior-authorization requests; part of the risk model uses prior spend as a proxy for need.

Expected findings:

- High impact; healthcare overlay.
- Cost-as-need objective is a core equal-protection risk; require clinical-need labels.
- Subgroup/ancestry validation, clinician override with authority and time, and expedited reversible appeal required.

## Insurance 1: Underwriting and claims triage

An insurer prices policies and triages claims with alternative data; denials issue standard letters.

Expected findings:

- High impact; insurance overlay.
- Proxy-discrimination testing and less-discriminatory-alternative search required.
- Specific adverse-action reasons, human review of denials, and feature governance required.

## Law enforcement 1: Predictive policing + face match

Hot-spot predictions guide patrols; face matches justify some stops.

Expected findings:

- High impact; law-enforcement + biometrics overlays.
- Lead-only rule with independent corroboration before enforcement.
- Demographic match-error and feedback-loop testing; query logging, oversight, redress.

## Biometrics 1: Watchlist access control

Facial recognition matches entrants against a banned-persons list; a match triggers ejection.

Expected findings:

- High impact; biometrics overlay.
- Human corroboration before action; demographic accuracy testing.
- Lawful basis for non-consensual scanning; no retention of non-matched templates; redress.

## Education 1: Proctoring + early warning

Remote proctoring flags "suspicious" behavior and an early-warning model labels dropout risk; some subjects are minors.

Expected findings:

- High impact; education overlay; minors raise privacy/consent bars.
- Human adjudication of every flag; bias testing across disability, skin tone, neurodivergence.
- Minimization, consent, vendor secondary-use limits; prevent self-reinforcing labels.

## Energy 1: Disconnection and restoration

AI queues accounts for automated disconnection and sequences outage restoration.

Expected findings:

- High impact; energy overlay.
- Enforced medical-baseline/protected-customer safeguards; human review before disconnection.
- Restoration/pricing disparity testing; meter-data minimization; stop authority.

## Critical infrastructure 1: Water SCADA response

AI detects anomalies and triggers automated pump/valve/dosing responses.

Expected findings:

- High impact; critical-infrastructure overlay.
- Bounded, fail-safe actuation; verified operator override within the physical time budget.
- Adversarial-input testing; immutable logging; stop authority.

## Transportation 1: Automated driving

An automated driving system operates on public roads with a fallback to a minimal-risk condition.

Expected findings:

- High impact; transportation overlay.
- Documented ODD and validated fallback; perception equity across pedestrian groups and mobility aids.
- Tamper-evident event data with investigator/victim access.

## Robotics 1: Warehouse mobile robots

Autonomous robots share aisles with workers and their throughput informs human pace.

Expected findings:

- High impact; robotics + employment overlays.
- Verified safety separation/speed, fail-safes, accessible emergency stop.
- Safety-bounded pacing; accountability for robot actions.

## Manufacturing 1: Process control + productivity scoring

AI runs closed-loop control on hazardous equipment and scores worker productivity for discipline.

Expected findings:

- High impact; manufacturing overlay.
- Functional-safety bounds, interlocks, override, stop authority.
- Human review/appeal for scores; disparate-impact testing; protected safety reporting.

## Smart cities 1: Public-space sensing

City sensors track pedestrians and vehicles; fused data reaches code enforcement and police.

Expected findings:

- High impact; smart-cities + law-enforcement overlays.
- Re-identification assessment; minimization; purpose limitation against enforcement creep.
- Public consultation, placement equity, oversight, and suspension authority.
