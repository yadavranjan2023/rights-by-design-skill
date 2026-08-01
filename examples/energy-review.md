# Example Review: Utility Disconnection, Restoration, and Dynamic Pricing System

## 1. System summary

A utility uses AI across three functions: prioritizing accounts for disconnection on non-payment, sequencing outage restoration, and setting dynamic time-of-use prices. High-risk accounts are queued for automated disconnection; restoration order follows a reliability-optimizing model; prices adjust with forecast demand. Smart-meter interval data feeds all three.

Unknowns include protections for medically vulnerable customers, whether restoration or pricing were tested for geographic and demographic disparity, meter-data minimization, and human review before disconnection.

## 2. Impact tier

**High impact.** Power and, by extension, heating, cooling, and medical equipment are essential services; wrongful disconnection or deprioritized restoration can endanger life.

Principal foreseeable harm: vulnerable or protected households are disconnected, restored last, or priced out of usage they cannot shift, based on models never tested for equity.

## 3. Applicable sector overlays

**Energy and utilities**, with **critical-infrastructure** considerations for grid-control automation.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Partial | High-resolution interval data can reveal occupancy, appliances, and routines beyond billing need. | No meter-data minimization or secondary-use limits documented. | Minimize interval data to purpose; bar secondary use and sharing without consent; log access. |
| Due process and algorithmic dignity | Gap | Automated disconnection can proceed without human review or protection for medically dependent customers. | No medical-baseline safeguard or pre-disconnection review shown. | Block disconnection of protected/medically vulnerable accounts; require human review before any shutoff. |
| Equal protection and nondiscrimination | Not enough information | Restoration and pricing may disadvantage low-income, rural, or protected areas. | No geographic or demographic disparity testing on file. | Test restoration and pricing for geographic and demographic disparity; add equity constraints. |
| Transparency and contestability | Gap | Customers cannot see why they were disconnected, deprioritized, or priced, or appeal in time. | No specific reason or expedited appeal path. | Provide specific, contestable reasons and a fast appeal with restoration authority. |
| Accountability and democratic control | Partial | Grid-control autonomy and disconnection lack a clear stop authority and audit trail. | Ownership assumed; stop authority and logs undocumented. | Name a suspension authority; log decisions; verify operator override on grid actions. |

## 5. Mission and sector findings

- Disconnection is a safety decision, not merely a billing action; medically vulnerable protections must be technically enforced, not left to policy.
- Reliability-optimized restoration can silently encode "restore the profitable areas first" unless equity is an explicit constraint.
- Grid-control automation must remain bounded and operator-revertible within the physical time budget.
- Dynamic pricing shifts cost onto those least able to shift load; distributional effects need measurement.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Enforce medical-baseline and protected-customer safeguards; require human review before disconnection. | Regulatory / Customer Care | Rule, exception list, review logs | Yes |
| 2 | Test restoration and pricing for geographic and demographic disparity; add equity constraints. | Planning / Equity / Regulatory | Disparity report and constraints | Yes |
| 3 | Minimize meter data and bar secondary use without consent. | Data Governance | Data map and access logs | Yes |
| 4 | Provide specific reasons and an expedited, restoration-capable appeal. | Customer Advocacy | Notice templates and appeal SLAs | Yes |
| 5 | Bound grid-control autonomy with verified operator override and a named stop authority. | Grid Operations / Safety | Safety case and override test | Yes |

## 7. Open questions

- Are medically vulnerable customers technically protected from automated disconnection?
- Were restoration and pricing tested for disparity, and with what results?
- Is meter data minimized and access logged?
- Who can pause disconnection and grid automation?

## 8. Bottom line

**Not ready for deployment.** Automated disconnection without enforced vulnerable-customer protection and untested restoration/pricing equity are safety and rights blockers.
