# Example Review: Water-Utility SCADA Anomaly Detection and Automated Response

## 1. System summary

A municipal water utility deploys AI over its SCADA network to detect anomalies (pressure, flow, chemical dosing) and, in some cases, trigger automated responses such as pump adjustments, valve actuation, or dosing changes. Operators supervise a console; some responses execute automatically to react faster than manual control allows.

Unknowns include the bounds on automated actuation, operator override latency, adversarial-input robustness, equity of any service-reduction actions, and cross-system accountability.

## 2. Impact tier

**High impact.** Water safety and continuity are life-critical; an unsafe automated action or a masked real fault can endanger a population.

Principal foreseeable harm: automated control acts on manipulated or misread state and degrades water safety faster than operators can intervene, or optimization quietly reduces service to some areas.

## 3. Applicable sector overlays

**Critical infrastructure**, with **cybersecurity** and **equity-of-service** considerations.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Not applicable / limited | Primarily operational telemetry, not personal data, though customer usage may be linked. | Confirm whether personal usage data is in scope. | Keep operational and customer data separated and minimized. |
| Due process and algorithmic dignity | Not enough information | Service-affecting actions (e.g., localized shutoffs) may lack notice or recourse. | No affected-customer notice or remedy process shown. | Provide notice and remedy where automated actions reduce service to identifiable areas. |
| Equal protection and nondiscrimination | Not enough information | Optimization may deprioritize lower-income or peripheral areas for service or restoration. | No equity analysis of service-reduction actions. | Test service-affecting actions for geographic disparity; add equity constraints. |
| Transparency and contestability | Partial | Operators may not understand or be able to safely override automated actions in time. | Explainability and override latency unverified. | Provide explainable actions, verified override within the physical time budget, and manual fallback. |
| Accountability and democratic control | Gap | Bounds on autonomy, audit logging, and a named stop authority are unproven; attack surface unaddressed. | No safety case, immutable logs, or robustness testing on file. | Bound autonomy to verified safety limits; add immutable logging, adversarial testing, and a stop authority. |

## 5. Mission and sector findings

- Automated actuation must be bounded by verified physical safety limits and fail safe; anomaly detection must not mask genuine faults.
- The cyber-physical attack surface is central: manipulated sensor inputs can drive unsafe automated responses.
- Operators need explainable actions and the ability to revert to manual control within the real time budget.
- Any service-reduction action has distributional effects that require equity review.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Bound automated actuation to verified safety limits with fail-safe defaults and manual fallback. | Engineering / Safety | Safety case and functional-safety test | Yes |
| 2 | Test adversarial robustness of inputs and segregate AI advice from safety-critical actuation. | Security / Controls | Red-team and segregation evidence | Yes |
| 3 | Verify operator explainability and override latency against the physical time budget. | Operations / Human Factors | Override drills and latency data | Yes |
| 4 | Add immutable logging, incident reconstruction, and a named stop authority. | Audit / Incident Response | Log design and IR plan | Yes |
| 5 | Test service-affecting actions for geographic disparity. | Planning / Equity | Disparity report | No |

## 7. Open questions

- What actions can execute without a human, and within what bounds?
- Can operators override in time, and is manual fallback proven?
- Has the input path been tested against manipulation?
- Who can stop the system, and how is every action reconstructed?

## 8. Bottom line

**Not ready for deployment.** Unbounded automated actuation, unverified override latency, and an unaddressed attack surface are safety blockers for a life-critical system.
