# Task 3 — Incident Response Plan

## Scenario
APT-01 is a controlled scenario represented by synthetic Elasticsearch
events. The associated DNS and TCP observations came from a separate
pre-existing packet capture and have not been linked to APT-01.

## 1. Detection and triage
- Review the alert and preserve the original event data.
- Record timestamps, event IDs, severity, host identity, and data source.
- Deduplicate repeated synthetic records before counting distinct stages.
- Treat synthetic events as test indicators, not proof of an intrusion.

## 2. Containment
- For a confirmed real incident, isolate the affected endpoint using
  approved containment procedures while preserving forensic evidence.
- Disable or restrict compromised accounts only after validating the
  account and authorization with the incident owner.
- Do not block observed domains or IPs solely because they appear in
  the supplied packet capture.

## 3. Investigation and eradication
- Correlate endpoint, authentication, network, and identity-provider logs.
- Validate suspected persistence, privilege escalation, and lateral movement.
- Remove confirmed malicious persistence and remediate the initial access
  vector under an approved change plan.
- Record each action, timestamp, operator, and supporting evidence.

## 4. Recovery
- Restore affected systems from trusted sources where necessary.
- Rotate credentials and revoke sessions when compromise is established.
- Monitor authentication, endpoint, and network telemetry for recurrence.
- Verify service health and obtain incident-owner approval before closure.

## 5. Validation and lessons learned
- Re-run the detection query against the controlled test dataset.
- Confirm expected matching records and document duplicate handling.
- Record limitations: synthetic telemetry, unverified IOC reputation,
  and no demonstrated real-world compromise or containment.
- Recommend improvements to log coverage, alert deduplication,
  correlation, and evidence retention.

## Outcome
This document defines a response procedure. It does not claim that
containment, eradication, or recovery actions were executed on a
compromised system.
