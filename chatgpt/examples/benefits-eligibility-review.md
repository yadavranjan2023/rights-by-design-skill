# Example Review: Public-Benefits Eligibility and Fraud Flagging

## 1. System summary

A state agency uses AI to score public-benefits cases for possible ineligibility or fraud. High-scoring cases are routed to caseworkers, who receive the score and three contributing factors. In practice, caseworkers terminate benefits in most high-score cases. Recipients receive a standard termination notice but are not told that AI was materially involved. Benefits stop before an administrative hearing. The vendor treats model documentation as confidential.

Unknowns include legal authority, data sources, subgroup and geographic performance, caseworker override rates, evidence access, hearing time, accessibility, and public reporting.

## 2. Impact tier

**High impact.** The system materially influences access to essential government benefits and may cause immediate deprivation.

Principal foreseeable harm: eligible recipients may lose essential support based on inaccurate, biased, or undisclosed automated inferences before receiving a meaningful opportunity to be heard.

## 3. Applicable sector overlays

**Government and public services.** The system supports an exercise of public authority affecting benefits and potential fraud investigation.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Not enough information | The agency may combine administrative, household, address, relationship, and behavioral data, but the data scope and authority are unknown. | No data inventory, legal-authority record, sharing agreement, or inference list. | Complete legal-purpose, data-minimization, sharing, retention, and sensitive-inference review. |
| Due process and algorithmic dignity | Gap | Benefits stop before a hearing, recipients lack AI-specific notice, and caseworker review appears heavily deferential. | Termination precedes hearing; high-score termination rate is high; authority and evidence access unknown. | Require legally appropriate pre-deprivation review, evidence access, factual correction, impartial human judgment, and rapid hearing. |
| Equal protection and nondiscrimination | Not enough information | No subgroup, disability, language, geography, household, or selective-enforcement analysis is available. | Performance evidence absent. | Complete subgroup and geographic testing, accessibility review, and monitoring of referrals, terminations, reversals, and burdens. |
| Transparency and contestability | Gap | Recipients cannot understand the system's role, inspect relevant data, challenge the score, or obtain timely remedy before loss. | Standard termination notice only; vendor secrecy asserted. | Provide accessible notice, material factors, evidence access, correction, hearing, representation information, and authority to restore benefits. |
| Accountability and democratic control | Gap | Vendor confidentiality prevents meaningful audit, and no public owner, oversight mechanism, or suspension authority is identified. | Vendor secrecy and agency operation known; audit and public governance absent. | Require agency ownership, audit rights, records, public documentation, complaint reporting, independent review, and suspension authority. |

## 5. Mission and sector findings

- The practical effect of the score, not its formal label, determines impact. A high termination rate indicates that the system materially drives the decision.
- Vendor confidentiality cannot eliminate the agency's duty to understand, audit, explain, and govern the system.
- Benefits termination before meaningful review may create severe and difficult-to-repair harm.
- Disability, language, household structure, address instability, digital access, and geographic enforcement patterns require explicit analysis.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Establish and document legal authority, permissible purpose, and procedural requirements for every use. | Agency General Counsel / Program Authority | Approved legal-authority memorandum | Yes |
| 2 | Prevent termination from taking effect until required review and process protections are completed, except where law expressly permits otherwise. | Program Director / Hearings Office | Approved workflow, system rule, and test results | Yes |
| 3 | Provide accessible notice of AI involvement, material factors, evidence, correction, and hearing rights. | Program / Accessibility / Legal | Notices, translations, usability tests, and service levels | Yes |
| 4 | Give caseworkers evidence, uncertainty, training, time, and authority to reject the score. | Program Operations | Interface, training, authority matrix, override logs | Yes |
| 5 | Require vendor documentation, model and data audit rights, change notice, records preservation, and cooperation with appeals. | Procurement / Legal / Audit | Executed contract and audit protocol | Yes |
| 6 | Test referrals, terminations, reversals, delays, and burdens by relevant groups and geography. | Civil Rights / Data Science / Independent Audit | Test report, thresholds, remediation record | Yes |
| 7 | Name an official authorized to pause or disable the system and publish aggregate performance and complaint information. | Agency Executive / Oversight | Governance charter and public reporting plan | Yes |

## 7. Open questions

- What statute, regulation, or program rule authorizes the data use and decision process?
- Which data sources and inferred relationships are used?
- How often do caseworkers reject the score?
- How long until a hearing and restoration?
- Are benefits preserved during appeal?
- What accessibility and language supports exist?
- Can the agency reproduce every termination decision?
- Who can suspend the system?

## 8. Bottom line

**Not ready for deployment.** The current process lacks adequate evidence of legal authority, pre-deprivation protections, meaningful human judgment, equality testing, contestability, vendor auditability, and democratic accountability.
