# Task 6 — Custom ELK SIEM Dashboard

## Objective

Design and implement a lightweight custom SIEM dashboard using Elasticsearch, Kibana, and Filebeat to visualize authentication failures, successful authentication, sudo activity, source-IP information, and a controlled file-transfer indicator.

## Work performed

- Collected `/var/log/auth.log` telemetry with Filebeat.
- Indexed the events into a single-node Docker-hosted Elasticsearch lab and used Kibana for investigation views and Lens visualizations.
- Built dashboard panels for SSH failures, authentication success/failure, sudo activity, source-IP aggregation, raw failure documents, and the controlled SCP indicator.
- Performed controlled local SSH, successful-authentication, sudo, and SCP tests.

## Results supported by retained evidence

The dashboard screenshots show 9 failed-password documents, three failure-count groups of 3, source-IP aggregation including a malformed extraction value, sudo-related panels, and a displayed file-transfer-indicator count of 3.

The tests were controlled lab activity. They did not demonstrate a confirmed brute-force attack, privilege-escalation incident, or real network exfiltration. The SCP copy stayed on `127.0.0.1`.

## Tools and technologies

Kali Linux, Docker, Elasticsearch 9.5.4, Kibana 9.5.4, Filebeat 9.5.4, `/var/log/auth.log`, Kibana runtime fields, Lens, Discover, and SHA-256 hashing as reported in the lab write-up.

## Deliverables and evidence

- [Final Task 6 report](reports/Task6_Custom_SIEM_Dashboard_Report_FINAL.docx)
- [Finalization audit](Task6_Finalization_Audit.md)
- [Dashboard overview](evidence/01_Task6_Dashboard_Overview.png)
- [Security-event dashboard view](evidence/02_Task6_Dashboard_Security_Events.png)
- [Kibana visualization library](evidence/03_Task6_Visualization_Library.png)

## Limitations and unresolved items

The retained evidence does not include the exact Filebeat configuration, runtime-field expression, Elasticsearch responses, verification command output, raw SCP records, or SCP query. The earlier reported index/document counts are therefore not independently verified.

The source-IP table displays values of 9, 3, and 1 while the raw failure panel shows 9 documents. The retained artifacts do not explain whether different filters or aggregation scopes caused this difference, so it remains unresolved and requires validation.

The setup is a single-host, single-node lab using only authentication telemetry. It is not a production SIEM and does not provide endpoint, network, or application-log coverage.
