# Example Review: Vendor Model Card


> **Use note:** This is a representative example for training, implementation, and evaluation. It is not a legal determination, regulatory approval, safety certification, or assessment of a named organization.


## 1. Scenario

A vendor provides a model card for a classification model used in high-impact decisions. The card includes purpose, overall accuracy, and known limitations but omits subgroup results, operational monitoring, and appeal integration.

## 2. Rights-by-Design review

| Area | Status | Finding |
|---|---|---|
| Intended use | Partial | Purpose is described, but prohibited and out-of-scope uses are incomplete. |
| Data provenance | Partial | Sources are summarized but lineage and representativeness are incomplete. |
| Validation | Partial | Overall performance is reported without operational or subgroup evidence. |
| Equality | Gap | No subgroup or intersectional results. |
| Human control | Gap | Reviewer authority and override are not described. |
| Explainability | Partial | Feature importance is provided but may not support individual reasons. |
| Monitoring | Gap | No drift, incident, complaint, or appeal monitoring. |
| Change control | Gap | Versioning and update approval are not described. |
| Security | Not enough information | Adversarial, access, and supply-chain evidence are absent. |

## 3. Evidence request

- Intended and prohibited uses
- Data lineage
- Subgroup validation
- Calibration and uncertainty
- Human-control workflow
- Explanation fidelity
- Monitoring thresholds
- Incident process
- Version history
- Security testing
- Decision reconstruction

## 4. Bottom line

**Insufficient information for a defensible deployment determination.** The model card is useful but not adequate evidence for high-impact use.
