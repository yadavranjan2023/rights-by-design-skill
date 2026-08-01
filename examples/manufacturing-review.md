# Example Review: Factory-Floor Process Control and Worker-Productivity Monitoring

## 1. System summary

A manufacturer deploys AI for two purposes: closed-loop process control on hazardous equipment (temperature, pressure, robotic motion) and worker-productivity monitoring that scores pace, idle time, and defect attribution, feeding scheduling and discipline. Some control actions execute automatically; productivity scores are surfaced to supervisors.

Unknowns include safety bounds and override on the control side, whether monitoring penalizes protected activity or disability, defect-model error handling, and worker review of adverse scores.

## 2. Impact tier

**High impact.** Process control affects worker physical safety; productivity scoring affects livelihood and dignity.

Principal foreseeable harm: an unsafe automated control action injures a worker, or opaque productivity scoring penalizes disability, breaks, or protected activity and drives unfair discipline.

## 3. Applicable sector overlays

**Manufacturing**, with **robotics/functional-safety** and **employment** considerations.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Partial | Continuous floor monitoring may capture more than task data, including location and behavior. | No monitoring-scope or minimization record. | Disclose and minimize monitoring; bar off-task and biometric inference without necessity. |
| Due process and algorithmic dignity | Gap | Productivity scores can drive discipline without worker review or appeal. | No human-review or appeal path for scores. | Require human review and appeal before any adverse action based on a score. |
| Equal protection and nondiscrimination | Not enough information | Pace and idle metrics may penalize disability, restroom breaks, or protected activity. | No disparate-impact analysis of the metrics. | Test metrics for disparate impact; exclude protected-activity and disability-linked penalties. |
| Transparency and contestability | Partial | Workers may not know how they are scored or be able to contest defect attribution. | Score logic and dispute path unclear. | Explain the metrics; provide a dispute path for defect attribution and scores. |
| Accountability and democratic control | Gap | Automated control lacks proven safety bounds, override, and a stop authority. | No functional-safety case or override test. | Bound control to verified safety limits with interlocks, override, and a named stop authority. |

## 5. Mission and sector findings

- Safety-critical actuation must be bounded to functional-safety limits with interlocks and emergency stop; AI advice must be segregated from unsafe actuation.
- Productivity pace-setting can drive injury; targets need ergonomic and safety review, not just throughput optimization.
- Defect models carry asymmetric costs: false negatives ship unsafe product, false positives blame workers; both need human adjudication on consequential calls.
- Punitive monitoring chills safety reporting; reporting channels must be protected and independent.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Bound automated control to verified safety limits with interlocks, override, and stop authority. | Safety Engineering | Functional-safety case and tests | Yes |
| 2 | Require human review and appeal before discipline based on scores. | HR / Operations | Review workflow and appeal logs | Yes |
| 3 | Test productivity metrics for disparate impact; remove protected-activity penalties. | HR / Legal | Disparate-impact analysis | Yes |
| 4 | Add human adjudication for consequential defect calls with safety-weighted error analysis. | Quality | Adjudication procedure and error report | Yes |
| 5 | Protect independent safety reporting from monitoring-based retaliation. | Safety / Compliance | Reporting policy | Yes |

## 7. Open questions

- What control actions run automatically, and are they bounded and interlocked?
- Can workers review and appeal adverse scores?
- Were pace and idle metrics tested for disparate impact?
- Are safety-reporting channels protected from monitoring?

## 8. Bottom line

**Not ready for deployment.** Unbounded safety-critical actuation and disciplinary scoring without review or disparate-impact testing are safety and rights blockers.
