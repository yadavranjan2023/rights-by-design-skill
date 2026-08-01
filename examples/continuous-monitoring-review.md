# Example: Continuous Rights-by-Design Monitoring


> **Use note:** This is a representative example for training, implementation, and evaluation. It is not a legal determination, regulatory approval, safety certification, or assessment of a named organization.


## 1. Purpose

Continuous monitoring verifies that deployed AI systems remain within approved rights, safety, performance, and operational bounds.

## 2. Monitoring domains

- Accuracy and calibration
- Subgroup and intersectional performance
- Privacy incidents
- Appeals and reversals
- Human override rates
- Complaint patterns
- Drift
- Security events
- Availability and fallback
- Model and configuration changes
- Vendor incidents
- Use outside approved scope

## 3. Example monthly dashboard

| Metric | Threshold | Current | Status |
|---|---:|---:|---|
| Overall error rate | ≤ 5% | 4.2% | Met |
| Highest subgroup error gap | ≤ 3 points | 5.8 points | Breach |
| Appeal reversal rate | ≤ 10% | 14% | Breach |
| Unlogged decisions | 0 | 0 | Met |
| Unauthorized model changes | 0 | 1 | Critical |
| Median appeal response | ≤ 3 days | 2.4 days | Met |

## 4. Escalation rules

- Critical security or rights event: immediate pause review
- Threshold breach for two periods: corrective-action plan
- Material subgroup harm: deployment restriction or suspension
- Unauthorized change: rollback and investigation
- Loss of reconstruction capability: stop consequential use

## 5. Governance

Named owners must review results, approve corrective actions, document residual risk, and possess authority to restrict or stop the system.

## 6. Bottom line

Continuous monitoring is not passive reporting. Threshold breaches must trigger defined operational decisions, remediation, and accountability.
