# Worked Examples

These abbreviated examples demonstrate the expected reasoning pattern. They are not substitutes for a full assessment.

## Example 1: Resume screening

### Facts supplied

A company uses a model to rank applicants. Recruiters normally interview only the top 15 percent. Applicants are not told about the model. The vendor reports 82 percent overall validation accuracy but provides no subgroup results.

### Correct approach

- Tier: high impact.
- Do not treat the system as merely advisory because ranking largely determines access to interviews.
- Mark equality as "not enough information" or "gap," not "met."
- Mark transparency and contestability as gaps.
- Require job-related validation, subgroup testing, applicant notice, correction, human review, override documentation, and monitoring.
- Identify Talent Acquisition, HR Compliance, Data Science, and Legal as possible owners.
- Treat lack of subgroup validation and meaningful review as deployment blockers.

## Example 2: Credit underwriting

### Facts supplied

A lender uses alternative data to approve small-business credit. Declined applicants receive standardized reason codes. A manual appeal exists, but reviewers cannot change the model score and may approve only when a data error is proven.

### Correct approach

- Tier: high impact.
- Due process is partial because factual correction exists.
- Contestability is a gap because reviewers cannot depart from the score on substantive grounds.
- Privacy requires analysis of alternative-data necessity and inferred sensitive attributes.
- Equality requires fair-lending and geographic testing.
- Require specific adverse-action reasons, substantive reconsideration authority, data correction, proxy testing, and governance thresholds.

## Example 3: Benefits eligibility

### Facts supplied

A public agency uses AI to flag cases for benefit termination. Staff receive a risk score and three factors. Recipients receive a termination notice but are not told AI was involved. Benefits stop before the hearing.

### Correct approach

- Tier: high impact.
- Government overlay applies.
- Due process is a gap if deprivation occurs before a meaningful opportunity to contest, subject to applicable law.
- Transparency and contestability are gaps.
- Human review may be nominal if staff cannot inspect evidence or reject the score.
- Require pre-deprivation review where required, evidence disclosure, correction, accessible notice, rapid hearing, benefits-preservation rules, logs, and public accountability.

## Example 4: Telecom fraud suspension

### Facts supplied

A carrier automatically blocks outbound service when a SIM-swap model exceeds a threshold. Emergency calls remain available. Customers must visit a retail store with identification to restore service.

### Correct approach

- Tier: high impact because communications access may be materially impaired.
- Telecom overlay applies.
- Emergency-call preservation is a positive control but not sufficient.
- Assess disability, geography, mobility, language, and access burdens created by in-person restoration.
- Require alternative restoration channels, rapid human review, false-positive monitoring, action logging, and customer remedy.

## Example 5: Defense sensor fusion

### Facts supplied

A system fuses radar and imagery and recommends tracks for operator attention. It cannot issue commands or control weapons. Operators see a confidence score but not sensor conflicts.

### Correct approach

- Tier: moderate or high depending on downstream use.
- Defense overlay applies.
- Lack of conflict and provenance display creates automation-bias and misclassification risk.
- Require source provenance, conflict display, uncertainty calibration, adversarial testing, defined use boundaries, and after-action reconstruction.
- Do not describe the system as low risk merely because it does not directly control a weapon.

## Example 6: Space autonomy

### Facts supplied

A satellite may autonomously enter safe mode and reorient solar arrays during communication loss. The logic has been simulation-tested but not hardware-in-the-loop tested.

### Correct approach

- Tier: high impact.
- Space overlay applies.
- Safe mode is a positive design feature.
- Verification remains partial because the deployed hardware and interfaces have not been validated.
- Require hardware-in-the-loop testing, fault injection, communication-loss testing, configuration traceability, recovery tests, and mission-authority approval.
