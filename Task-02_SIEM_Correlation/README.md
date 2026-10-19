# Task 2 — Custom SIEM Correlation Rules

## Objective

Implement and test custom correlation checks for credential-stuffing-like authentication activity, DNS tunnelling-like query patterns, and suspicious PowerShell command indicators using the existing ELK lab.

## Work performed

- Reused the Docker-hosted Elasticsearch and Kibana environment.
- Generated controlled synthetic events for authentication, DNS, and PowerShell cases.
- Implemented a Python rule runner that evaluated the conditions and wrote alert documents to Elasticsearch.
- Reviewed the results in Kibana Discover.

## Detection logic and results

- Credential stuffing: at least 8 failures involving at least 5 usernames from one source within five minutes; the controlled dataset triggered the rule.
- DNS tunnelling suspicion: at least 10 queries and 8 distinct names within five minutes; the controlled dataset triggered the rule.
- Suspicious PowerShell: indicator-based matching for strings such as `-EncodedCommand`, `DownloadString`, `Invoke-Expression`, `IEX`, and `FromBase64String`; the controlled dataset triggered the rule.

The final search returned three alert documents, one per rule, and the evidence screenshot shows them together in Kibana Discover.

## Tools and technologies

Kali Linux, Docker, Elasticsearch 9.5.4, Kibana 9.5.4, Python, Elasticsearch HTTP APIs, and Kibana Discover.

## Deliverables and evidence

- [Task 2 report](reports/ElevanceSkills_Task2_Custom_SIEM_Correlation_Report.docx)
- [Three correlation alerts](evidence/01_Kibana_Three_Correlation_Alerts.png)
- [Combined rule-test results](evidence/02_Correlation_Rule_Test_Results.png)
- [Credential-stuffing detection](evidence/03_Credential_Stuffing_Detection.png)
- [DNS tunnelling-suspicion detection](evidence/04_DNS_Tunnelling_Detection.png)
- [PowerShell detection](evidence/05_PowerShell_Detection.png)

## Limitations

The events were simulated and were not collected from a live attack or production endpoint. The DNS logic identifies volume and name diversity but does not inspect payload content or prove tunnelling. The PowerShell logic is indicator-based and can produce false positives. The rule runner was executed manually; recurring native Kibana Security detection rules were not configured, and the local lab used security-disabled Elasticsearch.
