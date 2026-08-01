# Example Review: Alternative-Data Lending

## 1. System summary

A lender uses an AI underwriting model for small-dollar consumer loans. Inputs include bureau data, bank-account cash flow, device characteristics, education, occupation, and application behavior. Declined applicants receive standardized adverse-action reasons. A manual review process permits correction of factual data but does not allow reviewers to depart from the model score on substantive grounds.

Unknowns include the exact decision threshold, geographic distribution, protected-class testing, reason-generation method, data retention, vendor access, and pricing effects.

## 2. Impact tier

**High impact.** The system determines access to credit and may affect financial stability and opportunity.

Principal foreseeable harm: applicants may be denied or priced unfairly based on opaque, inaccurate, or proxy-laden data without meaningful reconsideration.

## 3. Applicable sector overlays

**Lending.** The system performs credit underwriting and adverse-action explanation.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Partial | Cash-flow data may be relevant, but device, education, occupation, and behavioral data require necessity and sensitive-inference analysis. | Data categories identified; no necessity assessment, inference inventory, or retention controls. | Restrict inputs to demonstrably predictive and permissible data; prohibit unrelated behavioral and vulnerability inference; document retention and access. |
| Due process and algorithmic dignity | Partial | Applicants can correct factual errors, but reviewers cannot reconsider the decision on substantive grounds. | Correction workflow exists; no substantive exception authority. | Establish qualified reconsideration authority with documented criteria, evidence review, and ability to change the outcome. |
| Equal protection and nondiscrimination | Not enough information | No fair-lending, proxy, geographic, or pricing-impact results were supplied. | Overall model operation described; subgroup evidence absent. | Complete fair-lending validation, proxy testing, geographic analysis, pricing analysis, and remediation. |
| Transparency and contestability | Partial | Standardized reasons may not accurately describe the actual drivers of each decision. | Reason codes exist; fidelity testing absent. | Validate that reasons are specific, accurate, stable, and useful; identify source data and provide correction and appeal. |
| Accountability and democratic control | Partial | The lender owns the decision, but model, policy, vendor, monitoring, and appeal accountability are not established. | Manual review exists; ownership and logs are incomplete. | Name model, credit-policy, fair-lending, data, compliance, and vendor owners; preserve decision and override records. |

## 5. Mission and sector findings

- Device and behavioral variables may introduce socioeconomic, disability, age, geography, or other proxy effects.
- Standard adverse-action codes are insufficient unless they faithfully reflect the applicant-specific decision.
- A review limited to data correction is not full contestability.
- Pricing, limits, approval, denial, and account-management outcomes require separate testing.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Complete independent fair-lending and proxy analysis across approval, pricing, limits, and error outcomes. | Fair Lending / Model Risk | Validation report, findings, and remediation | Yes |
| 2 | Validate applicant-specific adverse-action reasons against actual decision logic. | Compliance / Model Risk / Engineering | Reason-fidelity test suite and results | Yes |
| 3 | Create substantive reconsideration by a qualified reviewer authorized to change the decision. | Credit Policy / Operations | Workflow, authority matrix, training, and appeal records | Yes |
| 4 | Approve a necessity and permissible-purpose assessment for alternative data. | Privacy / Legal / Data Governance | Data inventory, necessity analysis, approved sources | Yes |
| 5 | Preserve model version, data, policy rules, reasons, decision, human actions, and outcome. | Engineering / Records / Model Risk | Reconstruction test and audit logs | Yes |
| 6 | Monitor complaints, appeals, overrides, geographic effects, and drift. | Compliance / Model Risk | Dashboard, thresholds, escalation and reporting | No, if operational before launch |

## 7. Open questions

- How are adverse-action reasons generated?
- Which variables materially drive approval, pricing, and limits?
- What subgroup and geographic analyses have been completed?
- Can protected or sensitive traits be reconstructed from device or behavioral data?
- Who can approve exceptions?
- How quickly are corrected decisions restored?
- What vendor audit rights exist?

## 8. Bottom line

**Not ready for deployment.** Fair-lending evidence, accurate explanation, substantive reconsideration, alternative-data governance, and decision reconstruction are not yet established.
