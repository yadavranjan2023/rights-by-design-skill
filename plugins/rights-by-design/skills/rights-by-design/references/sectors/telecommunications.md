# Telecommunications Sector Module

## Scope

Apply this module to AI used by telecommunications carriers, internet service providers, network operators, mobile providers, satellite-communications providers, cloud communications platforms, emergency communications systems, and communications-equipment vendors.

## Review domains

### 1. Communications privacy

Assess content, metadata, call-detail records, precise location, device identifiers, browsing or traffic data, relationship graphs, inferred behavior, and cross-service linkage.

Verify purpose limitation, minimization, retention, access controls, encryption, customer notice, vendor restrictions, and deletion.

### 2. Access and nondiscrimination

Assess whether automated systems can block, suspend, throttle, deprioritize, price, route, or degrade service.

Test for disparate effects by geography, income, disability, language, race, age, rural status, tribal status, or other relevant populations.

### 3. Emergency and public-safety communications

Verify that AI cannot silently impair 911/E911, emergency alerts, priority services, disaster communications, or accessibility functions.

Require deterministic fallback behavior, redundant routing, manual control, and tested outage procedures.

### 4. Lawful interception and government access

Verify authorization, scope limitation, separation of duties, tamper-evident logging, retention controls, auditability, and misuse detection.

AI must not expand the legal or operational scope of surveillance merely because broader inference is technically possible.

### 5. Network autonomy and resilience

Define which routing, optimization, congestion, spectrum, anomaly-detection, or remediation actions AI may execute autonomously.

Require rollback, safe configuration states, blast-radius limits, staged deployment, change approval, and real-time observability.

### 6. Fraud and identity

Evaluate false-positive harms in robocall blocking, spam classification, SIM-swap prevention, identity verification, account suspension, and payment or device-financing controls.

Provide rapid human review and service restoration for erroneous restrictions.

### 7. Supply chain and vendors

Document model, data, cloud, chipset, network-equipment, managed-service, and subcontractor dependencies.

Require security obligations, incident notification, audit rights, update controls, provenance, and exit or replacement plans.

## Deployment blockers

Treat the following as presumptive blockers:

- untested impact on emergency communications;
- autonomous network changes without rollback;
- service denial without meaningful review;
- location or metadata inference without defined necessity and controls;
- lawful-interception access without tamper-evident logging;
- no accountable owner for outage, routing, or access decisions;
- inability to reconstruct automated network actions.
