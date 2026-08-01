# Defense and National-Security Sector Module

## Scope

Apply this module to AI used by the Department of Defense, military services, intelligence organizations, combatant commands, defense agencies, homeland-security missions, contractors, coalition operations, and national-security systems.

## Review domains

### 1. Authority and mission

Identify the lawful mission, operational authority, commander or decision authority, approved use cases, prohibited uses, geographic scope, and conditions of employment.

The model's technical capability does not establish authority to use it.

### 2. Human command and control

For consequential decisions, identify:

- who receives the recommendation;
- what evidence and uncertainty are visible;
- how much time exists for review;
- whether the operator can reject or override;
- whether escalation is required;
- who bears responsibility for the final action.

### 3. Use of force and civilian protection

For systems supporting targeting, weapons, force protection, or operational planning, assess distinction, proportionality, precaution, civilian-harm mitigation, target verification, no-strike and restricted-target controls, fratricide risk, and escalation pathways.

This framework does not substitute for a formal legal or weapons review.

### 4. Data and sensor integrity

Assess source provenance, sensor limitations, fusion logic, stale or conflicting data, deception, spoofing, synthetic data, target drift, confidence calibration, and chain of custody.

### 5. Adversarial and contested environments

Test cyber compromise, electronic warfare, communications loss, GPS denial, adversarial examples, camouflage, decoys, poisoning, model extraction, insider threats, and supply-chain compromise.

### 6. Bounded autonomy

Specify actions the system may recommend, initiate, execute, or never perform.

Include time, geography, target class, mission phase, confidence, communications, and supervision constraints.

### 7. Operator factors

Evaluate automation bias, cognitive overload, alert fatigue, training, trust calibration, interface design, degraded-mode performance, and handoff between human and machine control.

### 8. Accountability and reconstruction

Preserve mission data, inputs, model version, rules, confidence, recommendations, human decisions, overrides, communications, and resulting actions as security and operational constraints permit.

### 9. Coalition and classified environments

Address classification, releasability, compartmentation, foreign disclosure, coalition interoperability, differing authorities, data residency, and model contamination across security domains.

### 10. Fail-safe and abort

Define safe states, disengagement, abort, retask, shutdown, loss-of-link behavior, recovery, and command succession.

## Deployment blockers

Treat the following as presumptive blockers:

- undefined command authority;
- unbounded autonomous consequential action;
- inability to display uncertainty or source provenance;
- no tested behavior under deception or communications loss;
- no abort, disengagement, or safe-state mechanism;
- operators unable to reject the recommendation;
- no after-action reconstruction;
- unresolved civilian-harm or escalation risk;
- use outside approved mission or legal review.
