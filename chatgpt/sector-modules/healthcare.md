# Healthcare Sector Module

## Scope

Apply to diagnosis, triage, risk scoring, treatment recommendation, imaging, clinical documentation, utilization management, scheduling, resource allocation, patient monitoring, remote care, population health, claims, and administrative decisions affecting care.

## Decision and harm model

Healthcare AI can affect life, bodily integrity, access to treatment, quality of care, disability, privacy, and trust. Administrative tools may be high impact when they delay or deny care.

## Rights-specific review

### Privacy and cognitive liberty

Assess:

- health data, genetic data, behavioral data, device data, location, voice, images, and inferred conditions;
- minimum necessary use;
- consent and authorization;
- research versus care use;
- vendor and cloud access;
- retention and secondary use;
- reidentification and linkage risks.

### Due process and dignity

Verify:

- clinician judgment;
- patient notice where appropriate;
- correction of records;
- escalation for atypical cases;
- review before denial or withdrawal of care;
- protection against dehumanizing or stigmatizing labels;
- continuity of care during disputes.

### Equal protection and nondiscrimination

Require:

- performance by race, ethnicity, sex, age, disability, language, geography, socioeconomic status, and relevant clinical subgroups;
- analysis of missing data and access bias;
- device and measurement bias;
- accessibility;
- monitoring of downstream care and resource allocation;
- remediation when unequal error rates produce unequal harm.

### Transparency and contestability

Provide:

- useful explanation to clinicians;
- patient-accessible explanation where consequential;
- correction of data;
- second review;
- clinician override;
- appeal for coverage or access decisions;
- documentation of disagreement.

### Accountability

Name clinical owner, safety owner, model owner, data owner, privacy owner, security owner, vendor owner, and deployment authority.

Track recommendations, confidence, inputs, clinician actions, overrides, outcomes, incidents, and model changes.

## Sector controls

- intended-use statement;
- clinical validation;
- human-factors testing;
- workflow integration testing;
- calibrated uncertainty;
- safe fallback;
- override and escalation;
- postdeployment surveillance;
- incident reporting;
- data-quality monitoring;
- independent safety review;
- change management.

## Evidence required

- clinical validation report;
- subgroup results;
- usability study;
- hazard analysis;
- workflow map;
- override logs;
- incident procedures;
- monitoring plan;
- data provenance;
- cybersecurity assessment;
- patient notice and appeal materials where applicable.

## Deployment blockers

- inadequate clinical validation;
- no safe fallback;
- hidden or unusable uncertainty;
- no clinician override;
- material subgroup underperformance without mitigation;
- automated care denial without meaningful review;
- inability to detect or investigate patient harm;
- use outside validated population or setting.
