# Example Review: Production Model Update


> **Use note:** This is a representative example for training, implementation, and evaluation. It is not a legal determination, regulatory approval, safety certification, or assessment of a named organization.


## 1. Scenario

A vendor proposes upgrading a production language model from version 4.2 to 4.3 for a high-impact customer-service workflow.

## 2. Change review

The update must be treated as a material system change, not routine maintenance.

## 3. Required comparison

- Intended use and capability changes
- Safety and policy behavior
- Accuracy and calibration
- Subgroup performance
- Explanation quality
- Data handling
- Latency and reliability
- Tool and action behavior
- Security and prompt-injection resistance
- Logging compatibility
- Appeal and human-review impact

## 4. Go/no-go controls

| Requirement | Evidence | Decision |
|---|---|---|
| Regression suite passes | Test report | Required |
| No unresolved critical subgroup regression | Comparative analysis | Required |
| Human workflow remains effective | Usability test | Required |
| Logs remain reconstructable | Audit test | Required |
| Rollback is tested | Recovery exercise | Required |
| Documentation is updated | Release package | Required |
| Owners approve residual risk | Signed decision | Required |

## 5. Deployment blockers

- Material regression
- Unknown behavior change
- No rollback
- Incompatible logging
- Unreviewed data-use change
- Human-review degradation
- Vendor cannot explain update scope

## 6. Bottom line

**Proceed only with specified conditions.** No production rollout should occur until comparative testing, rollback, documentation, and approvals are complete.
