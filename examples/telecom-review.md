# Example Review: Telecom Customer Deposit, Service-Denial, and Fraud-Suspension System

## 1. System summary

A carrier uses AI to set required deposits and approve or deny new service based on a risk score, and separately to detect fraud and suspend accounts automatically. Scores draw on payment history, address, device, and third-party data. Denied or suspended customers receive a generic message; fraud suspensions cut service immediately.

Unknowns include disparate-impact testing across geography and protected groups, reason specificity, human review before suspension, CPNI/location-data handling, and restoration speed for wrongful suspensions.

## 2. Impact tier

**High impact.** Connectivity is close to an essential service; denial, deposits, and wrongful suspension can cut off emergency and essential communication.

Principal foreseeable harm: customers are redlined via location/payment proxies into denial or high deposits, or wrongly fraud-suspended and left without essential connectivity with no fast recourse.

## 3. Applicable sector overlays

**Telecommunications.** Service access, metadata/CPNI, emergency communications, and network resilience apply.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Partial | CPNI, location, and third-party data may be used and shared beyond consented purposes. | No CPNI minimization or access-logging record. | Minimize and purpose-limit CPNI/location; log and audit access. |
| Due process and algorithmic dignity | Gap | Fraud suspension cuts service before human review; denials lack specific reasons. | Generic message only; no review-before-suspension. | Require human review before suspension where feasible; give specific, contestable reasons. |
| Equal protection and nondiscrimination | Not enough information | Deposit and denial scoring may redline neighborhoods via location/payment proxies. | No disparate-impact testing on file. | Test scoring for geographic and demographic disparity; remove unjustified proxies. |
| Transparency and contestability | Gap | Customers cannot learn why they were denied, charged a deposit, or suspended, or appeal fast. | No specific reasons or expedited appeal. | Provide specific reasons and an expedited appeal with restoration authority. |
| Accountability and democratic control | Partial | Ownership exists, but audit logging and a suspension-reversal authority are unproven. | No audit trail or restoration SLA. | Log decisions; define a rapid restoration path and accountable owner. |

## 5. Mission and sector findings

- Wrongful fraud suspension is a safety issue given emergency-communication needs; restoration must be rapid and prioritized.
- Location and payment proxies can reproduce redlining; disparity testing is essential.
- Specific, contestable reasons are required for a real right to challenge; a generic message is notice, not contestability.
- CPNI and location data warrant heightened minimization and logging.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Require human review before suspension and provide rapid restoration for wrongful ones. | Fraud Ops / Customer Care | Workflow and restoration SLA | Yes |
| 2 | Test deposit/denial scoring for geographic and demographic disparity. | Risk / Compliance | Disparity report | Yes |
| 3 | Provide specific, contestable reasons and an expedited appeal. | Customer Advocacy / Legal | Notice templates and appeal SLAs | Yes |
| 4 | Minimize and log CPNI/location access; bar unconsented secondary use. | Privacy / Security | Data map and access logs | Yes |
| 5 | Log decisions and name an accountable owner. | Governance | Audit design | No |

## 7. Open questions

- Was scoring tested for disparity across geography and protected groups?
- Is there human review before suspension, and how fast is restoration?
- Are reasons specific enough to contest?
- How are CPNI and location data minimized and logged?

## 8. Bottom line

**Not ready for deployment.** Suspension-before-review, untested redlining risk, and non-specific reasons are blockers given connectivity's essential-service status.
