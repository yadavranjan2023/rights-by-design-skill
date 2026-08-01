# Example Review: Automated Resume Screening

## 1. System summary

A large employer uses an AI system to rank applicants for professional roles. Recruiters generally review only the top 15 percent of ranked candidates. The model uses resumes, application responses, education history, employment history, and assessment results. Applicants are not told that AI materially influences interview selection. The vendor reports overall accuracy but has not supplied subgroup results, accessibility testing, override data, or appeal outcomes.

Unknowns include the exact target variable, job-analysis methodology, training-data period, treatment of employment gaps, accommodation process, recruiter authority, and retention of applicant data.

## 2. Impact tier

**High impact.** The system materially controls access to employment and livelihood because ranking determines which applicants receive human consideration.

Principal foreseeable harm: qualified applicants may be systematically excluded without notice, explanation, correction, or meaningful review.

## 3. Applicable sector overlays

**Employment.** The system affects candidate ranking and interview access.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Partial | The stated inputs are employment-related, but necessity, inference, retention, vendor access, and secondary use are not established. | Data categories identified; no data-flow map, retention schedule, inference inventory, or vendor-access record. | Approve a data inventory and necessity assessment; prohibit unsupported personality, emotion, health, and intent inference; set retention and deletion controls. |
| Due process and algorithmic dignity | Gap | Applicants receive no notice and have no opportunity to correct data before ranking controls interview access. Recruiter review may be nominal because only the top-ranked group is visible. | No notice, correction workflow, or evidence that recruiters can inspect excluded candidates. | Provide pre-use notice, correction, accommodation, and a documented review process that includes candidates below the threshold where uncertainty or edge cases exist. |
| Equal protection and nondiscrimination | Not enough information | Overall performance does not establish equal performance or equal selection effects. | No subgroup, intersectional, accessibility, or proxy analysis. | Complete job-related validation, subgroup and intersectional testing, accessibility review, proxy analysis, and selection-rate monitoring. |
| Transparency and contestability | Gap | Applicants cannot know AI is materially involved, understand key reasons, challenge inaccurate data, or obtain reconsideration. | No applicant-facing notice, reason, or appeal materials. | Provide notice, useful factors, correction, accommodation, and qualified human reconsideration with authority to advance a candidate. |
| Accountability and democratic control | Partial | A vendor and employer operate the system, but ownership, approval, logging, monitoring, and suspension authority are not established. | Vendor identity and general workflow known; no named accountable owner, model-change record, override log, or audit right. | Name executive, HR, model-risk, data, and vendor owners; require logs, audit rights, change approval, complaint monitoring, and suspension authority. |

## 5. Mission and sector findings

- The employer cannot rely on the label "ranking tool" to reduce the risk tier because recruiters ordinarily see only the top 15 percent.
- Employment-gap, school, ZIP code, name, language, assessment, and career-path variables may operate as proxies.
- Accessibility and accommodation must be tested before using assessments or video, voice, timing, or interaction signals.
- Recruiter override is meaningful only if recruiters can see sufficient evidence, review excluded cases, depart from the score, and document reasons.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | The system shall be validated against documented, job-related criteria for each job family and use context. | Industrial-Organizational Psychology / HR Compliance | Approved job analysis and validation report | Yes |
| 2 | The organization shall test selection rates, error rates, ranking distributions, and outcomes across relevant and intersectional groups. | Model Risk / Civil Rights / Data Science | Independent subgroup analysis and remediation record | Yes |
| 3 | Applicants shall receive accessible notice, correction, accommodation, and human reconsideration. | Talent Acquisition / Accessibility / Legal | Live workflow, templates, service levels, and test records | Yes |
| 4 | Recruiters shall have authority and information to depart from the ranking, including review of uncertain and excluded cases. | Talent Acquisition Operations | Reviewer interface, training, override policy, and logs | Yes |
| 5 | Unsupported emotion, personality, health, disability, and intent inference shall be prohibited. | Privacy / HR / Product | Approved prohibited-use specification and test results | Yes |
| 6 | Vendor contracts shall provide documentation, audit rights, incident notice, model-change notice, and data-deletion obligations. | Procurement / Legal / Vendor Risk | Executed contract controls | No, if completed before production |
| 7 | The employer shall monitor selection, interview, offer, complaint, appeal, and override outcomes on a defined schedule. | HR Compliance / Model Risk | Monitoring dashboard, thresholds, escalation plan | Yes |

## 7. Open questions

- What outcome was used as the model target?
- Were historical hiring decisions used as labels?
- Which groups and job families were represented in development data?
- Can recruiters review candidates outside the top 15 percent?
- What accommodations and alternative assessments exist?
- What applicant data is inferred, retained, or shared with the vendor?
- Who can suspend the system?

## 8. Bottom line

**Not ready for deployment.** The absence of job-related validation evidence, subgroup testing, applicant notice, meaningful human reconsideration, and accountable governance creates material employment-rights risks and multiple deployment blockers.
