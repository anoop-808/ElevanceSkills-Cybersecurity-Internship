# Task 3 — Multi-Stage APT Simulation and Response

## Objective

Build and evaluate an open-source SIEM workflow for a controlled multi-stage APT scenario, validate query-driven detection logic, correlate events, document investigation and response procedures, and preserve evidence.

## Work performed

- Validated an Ubuntu 24.04 Azure VM and a Kali Linux evidence workflow.
- Used Docker-hosted Elasticsearch and Kibana for authentication telemetry and synthetic APT events.
- Generated explicitly labelled synthetic indicators for six APT stages and tested positive and negative cases.
- Queried high- and critical-severity synthetic events and recorded detection evidence.
- Added a controlled process-discovery check using a benign `sudo ps` command and tested negative controls.
- Documented investigation, response, evidence-integrity, and future-validation procedures.

## Results

The retained JSON evidence records two synthetic records for each of six stages and eight high/critical synthetic events. The process-discovery validation matched the known benign `ps` event and excluded the tested `grep` and `ls` controls. These are controlled query-validation results, not evidence of a real APT compromise.

Live Kibana alert generation was not verified. The report also records disabled SIEM security, a pending consolidated package, and a zero-byte refined-result JSON artifact that must not be cited as evidence.

## Tools and technologies

Microsoft Azure Ubuntu VM, Kali Linux, Docker, Elasticsearch 9.5.4, Kibana 9.5.4, Python, Elasticsearch HTTP APIs, JSON/CSV/TSV evidence, a Sigma-style YAML rule, and MITRE ATT&CK technique references.

## Deliverables

- [Technical report](reports/ElevanceSkills_Task3_Final_Technical_Report.docx)
- [PDF report](reports/ElevanceSkills_Task3_Final_Technical_Report.pdf)
- [High/critical simulation rule](rules/task3_high_critical_simulation.yml)
- [APT simulation script](simulate_apt.py)
- [Detection query script](run_detection_query.py)
- [Detection verification script](verify_detection.py)
- [Rule-logic test script](test_sigma_logic.py)

## Evidence

- [Detection coverage JSON](evidence/task3_detection_evidence.json)
- [High/critical detection JSON](evidence/task3_high_critical_detection.json)
- [Sigma-logic test JSON](evidence/task3_sigma_logic_test.json)
- [Detection evidence screenshot](evidence/Task3_Detection_Coverage.png)
- [High/critical detection screenshot](evidence/Task3_High_Critical_Detection.png)
- [IOC register](evidence/task3_ioc_register.csv)
- [Authentication review](evidence/task3_authentication_review.txt)
- [Incident-response plan](evidence/task3_incident_response_plan.md)
- [Network/DNS review](evidence/task3_network_dns_review.tsv)
- [TCP conversation review](evidence/task3_tcp_conversations.txt)

The organized folder contains a flattened retained evidence set. Some nested evidence paths referenced by the report’s original package are not present here, and the report’s E15–E17 inventory still requires reconciliation.

## Limitations

Synthetic APT events do not demonstrate a real intrusion, account change, privilege escalation, lateral movement, or data transfer. Query-driven validation is not a continuously running detection engine. The existing SIEM security configuration was lab-only, and response actions were documented rather than executed against a compromised system.
