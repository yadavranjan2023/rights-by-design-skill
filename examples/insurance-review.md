# Example Review: Insurance Underwriting, Pricing, and Claims-Triage Model

## 1. System summary

An insurer uses AI to underwrite and price policies and to triage claims, flagging some for denial or special investigation. Models use application data plus alternative and third-party data. Declines and claim denials issue standard letters; flagged claims face delay and heightened scrutiny.

Unknowns include proxy-discrimination testing, reason specificity for adverse actions, human review of denials, use of alternative data that infers protected traits, and appeal timeliness.

## 2. Impact tier

**High impact.** Insurance pricing and claims decisions affect access to essential financial protection and can encode protected-class proxies.

Principal foreseeable harm: applicants are priced or declined, or claims denied, via proxies correlated with protected class, with reasons too generic to contest.

## 3. Applicable sector overlays

**Insurance**, with **banking-and-finance** fair-treatment considerations.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Partial | Alternative and third-party data may infer health, behavior, or protected traits. | No inference inventory or minimization. | Inventory and minimize inferred attributes; bar prohibited proxies. |
| Due process and algorithmic dignity | Gap | Declines and claim denials can stand without meaningful human review. | No human-review step documented. | Require human review and appeal for declines and denials. |
| Equal protection and nondiscrimination | Not enough information | Pricing/underwriting may produce disparate impact via proxies. | No disparate-impact or less-discriminatory-alternative testing. | Test for disparate impact; search and document less-discriminatory alternatives. |
| Transparency and contestability | Gap | Adverse-action reasons are generic, defeating a real challenge. | Standard letters only. | Provide specific, accurate reasons and an accessible appeal. |
| Accountability and democratic control | Partial | Model risk management and monitoring maturity are unproven. | No independent validation or monitoring record. | Independent model validation, documentation, and scheduled fairness monitoring. |

## 5. Mission and sector findings

- Alternative data is the main proxy-discrimination vector; each feature needs a documented, lawful justification.
- Generic adverse-action reasons block contestability; specificity is a right, not a courtesy.
- Claims triage that delays or denies needs human review and a fast appeal.
- Fairness and performance require ongoing monitoring, not a one-time check.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Test underwriting/pricing for disparate impact; document less-discriminatory alternatives. | Actuarial / Compliance | Fairness test and LDA record | Yes |
| 2 | Provide specific adverse-action reasons and an accessible appeal. | Legal / Customer Care | Reason codes and appeal path | Yes |
| 3 | Require human review for declines and claim denials. | Underwriting / Claims | Review workflow and logs | Yes |
| 4 | Inventory and remove prohibited proxies from features. | Data Science / Legal | Feature governance record | Yes |
| 5 | Establish independent validation and scheduled fairness monitoring. | Model Risk | Validation and monitoring plan | No |

## 7. Open questions

- Was disparate impact tested and a less-discriminatory alternative sought?
- Are adverse-action reasons specific enough to contest?
- Is there human review for declines and denials?
- What alternative data is used, and what does it infer?

## 8. Bottom line

**Not ready for deployment.** Untested proxy discrimination and generic adverse-action reasons are blockers for consequential insurance decisions.
