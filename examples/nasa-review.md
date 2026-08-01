# Example Review: Spacecraft Onboard Autonomy and Fault Management

## 1. System summary

A spacecraft uses AI-supported onboard autonomy for fault detection, isolation, and recovery, and for some navigation decisions, operating under communication delay where ground intervention is slow or impossible. Operators supervise via telemetry and can command safe modes when in contact. Crew health monitoring is also in scope on crewed variants.

Unknowns include the bounds on autonomous action, the explainability and override of fault-management decisions, software-assurance level for learned components, and crew medical-data privacy.

## 2. Impact tier

**High impact.** Failures are often irreversible and remote; crew, vehicle, and mission safety are at stake.

Principal foreseeable harm: autonomy acts on a wrong state estimate during a comms gap and cannot be corrected in time, or an opaque fault response cannot be safely overridden.

## 3. Applicable sector overlays

**NASA and space systems**, with **safety-critical assurance** and, for crew, **medical-privacy** considerations.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Not enough information | Crew health and performance monitoring may compromise medical privacy and autonomy. | No separation of operational vs medical data. | Apply medical-grade privacy and consent; separate operational and medical data. |
| Due process and algorithmic dignity | Not applicable / limited | Primarily an engineering-safety context, though crew autonomy applies. | Confirm crew-facing decision scope. | Preserve crew authority and informed consent for monitoring. |
| Equal protection and nondiscrimination | Not enough information | Crew monitoring models may underperform across physiology; Earth-observation may affect populations. | No subgroup or data-governance analysis. | Validate monitoring across crew physiology; govern Earth-observation inference. |
| Transparency and contestability | Partial | Fault-management outputs may not be explainable or overridable in time. | Explainability and override latency unverified. | Provide explainable fault outputs and rehearsed operator override with graceful degradation. |
| Accountability and democratic control | Gap | Autonomy bounds and software assurance for learned components are unproven. | No V&V or independent technical-authority record. | Bound autonomy; meet software-assurance/V&V standards; independent technical-authority review. |

## 5. Mission and sector findings

- Deterministic safety envelopes and human-authority modes must bound autonomy, with graceful degradation under comms delay.
- Learned components must meet the applicable software-assurance and verification standard for safety-critical software.
- Fault-management outputs need to be explainable and overridable within the available time, with rehearsed contingencies.
- Crew medical data requires medical-grade privacy, separated from operational telemetry.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Define deterministic safety envelopes and human-authority modes; verify graceful degradation. | Systems Safety | Safety analysis and test | Yes |
| 2 | Meet software-assurance and V&V standards for learned components; independent technical-authority review. | Software Assurance / ITA | V&V record and ITA sign-off | Yes |
| 3 | Ensure fault outputs are explainable and overridable in time; rehearse contingencies. | Operations | Override drills | Yes |
| 4 | Protect crew medical data with consent and separation from operations. | Flight Medicine / Privacy | Data-handling policy | Yes |
| 5 | Govern Earth-observation inference affecting populations. | Data Governance | Governance policy | No |

## 7. Open questions

- What are the autonomy bounds and human-authority modes under comms delay?
- Do learned components meet the applicable assurance standard?
- Can operators understand and override fault responses in time?
- How is crew medical data protected?

## 8. Bottom line

**Not ready for deployment.** Unbounded autonomy, unmet software assurance for learned components, and unverified override are safety blockers for an irreversible, remote system.
