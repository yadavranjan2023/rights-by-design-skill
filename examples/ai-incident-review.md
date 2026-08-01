# Example Review: AI Benefits-Termination Incident


> **Use note:** This is a representative example for training, implementation, and evaluation. It is not a legal determination, regulatory approval, safety certification, or assessment of a named organization.


## 1. Incident summary

A public-benefits system incorrectly flagged eligible recipients for termination after a vendor model update. Benefits were suspended before human review. The agency received complaints after several days.

## 2. Timeline

1. Vendor released model version 4.3.
2. Agency deployed without full regression testing.
3. Error rate increased for households with irregular income.
4. Caseworkers relied on risk scores.
5. Benefits were suspended.
6. Complaints revealed the pattern.
7. Agency paused the model.

## 3. Root causes

- Inadequate model-update review
- No subgroup regression testing
- Nominal human review
- No pre-deprivation safeguard
- Weak monitoring and complaint escalation
- Incomplete decision reconstruction
- Vendor change notice without sufficient evidence

## 4. Rights impact

| Dimension | Incident finding |
|---|---|
| Privacy and cognitive liberty | Irregular-income patterns were inferred without adequate impact review. |
| Due process and dignity | Benefits stopped before meaningful review. |
| Equal protection | Households with irregular income were disproportionately affected. |
| Transparency and contestability | Recipients lacked timely explanation and restoration. |
| Accountability | Agency and vendor responsibilities were unclear. |

## 5. Immediate actions

- Restore benefits
- Suspend affected model
- Notify impacted recipients
- Preserve evidence
- Provide expedited review
- Investigate scope
- Report to oversight authorities where required

## 6. Corrective actions

- Formal update approval
- Regression and subgroup testing
- Pre-deprivation human review
- Complaint-based monitoring
- Restoration service levels
- Vendor accountability
- Independent postincident review

## 7. Bottom line

The incident was preventable. The system should remain suspended until corrective controls are independently verified.
