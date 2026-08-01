# Example Review: Clinical Prior-Authorization and Care-Prioritization Model

## 1. System summary

A payer-provider organization uses AI in two linked functions. First, it auto-adjudicates prior-authorization requests for procedures and medications: low-approval-probability requests are auto-denied or pended for review. Second, it stratifies patients into risk tiers that route scarce care-management and nursing resources. Clinicians see a tier and a denial probability; denials issue a standard letter citing policy criteria. Part of the risk model was trained on prior healthcare spend as a proxy for need.

Unknowns include the training objective and label definition, subgroup and ancestry performance, clinician override rates, the timeliness of appeals, whether care is preserved during appeal, accessibility of notices, and post-deployment drift monitoring.

## 2. Impact tier

**High impact.** The system gates access to treatment and allocates clinical attention; errors can delay or deny necessary care and disproportionately harm under-served groups.

Principal foreseeable harm: patients with genuine need are denied or de-prioritized based on a model that encodes cost as need or underperforms for their subgroup, before a clinician meaningfully intervenes.

## 3. Applicable sector overlays

**Healthcare.** Clinical safety, subgroup performance, meaningful clinician override, and post-market surveillance apply. Coverage denial also implicates due-process and contestability duties.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Not enough information | Clinical, claims, pharmacy, and possibly social data may be combined and inferred beyond the stated purpose. | No data inventory, minimization record, or inferred-attribute list. | Complete a data-and-inference inventory; minimize to the clinical purpose; bar sensitive inference without necessity. |
| Due process and algorithmic dignity | Gap | Care can be denied before a clinician meaningfully reviews, and patients are not told AI was material. | High auto-denial rate; standard letter only; override authority and time unknown. | Require a qualified clinician with time and authority to overturn any care-affecting denial before it takes effect. |
| Equal protection and nondiscrimination | Gap | A cost-as-need objective and unvalidated subgroup performance risk systematically under-serving disadvantaged groups. | Training label uses spend; no ancestry/subgroup validation on file. | Retrain on a clinical-need label; validate and report performance by ancestry, disability, sex, and age before use. |
| Transparency and contestability | Gap | Patients cannot understand the model's role, see the criteria applied, or reach a fast, reversible appeal. | Policy-criteria letter only; no AI-specific notice or expedited appeal. | Provide plain-language notice, the material factors, and an expedited clinical appeal with authority to reverse. |
| Accountability and democratic control | Partial | An organizational owner exists, but audit access, drift monitoring, and a suspension authority are unproven. | Ownership known; audit rights, monitoring thresholds, and stop authority undocumented. | Name an accountable clinical owner; require audit access, subgroup drift monitoring, and pause authority. |

## 5. Mission and sector findings

- A training objective built on prior spend imports historical access inequities as if they were clinical need; this is the single highest-risk design choice.
- Aggregate accuracy can look acceptable while subgroup performance is unsafe; only stratified validation reveals it.
- "Clinician in the loop" is not meaningful control if the clinician lacks time, context, uncertainty, and real authority to override.
- Denial before appeal in a clinical setting can cause irreversible harm; the practical denial rate, not the model's advisory label, defines the impact.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Replace cost-proxy labels with a validated clinical-need objective. | Chief Medical Officer / Data Science | Model card with label definition and validation | Yes |
| 2 | Require meaningful clinician review with authority and time before any care-affecting denial. | Clinical Operations | Workflow, authority matrix, override logs | Yes |
| 3 | Validate and report performance by ancestry, disability, sex, and age; remediate gaps. | Clinical / Equity / Independent review | Stratified validation report and thresholds | Yes |
| 4 | Provide AI-specific notice, material factors, and an expedited reversible appeal; preserve care where appropriate during appeal. | Legal / Member Services | Notices, appeal SLAs, restoration procedure | Yes |
| 5 | Stand up post-market drift and subgroup monitoring with defined action thresholds. | Model Risk / Quality | Monitoring plan and dashboards | Yes |
| 6 | Establish audit access and a named authority to pause or disable the system. | Governance / Compliance | Audit protocol and governance charter | Yes |

## 7. Open questions

- What exactly does the risk label predict, and was cost used as a proxy for need?
- What are the subgroup and ancestry performance results?
- How often do clinicians override, and do they have the time and authority to?
- How fast is an appeal, and is care preserved meanwhile?
- Who can pause the system, and what triggers a pause?

## 8. Bottom line

**Not ready for deployment.** The cost-proxy objective, unvalidated subgroup performance, denial-before-review workflow, and weak contestability are each independently disqualifying until remediated.
