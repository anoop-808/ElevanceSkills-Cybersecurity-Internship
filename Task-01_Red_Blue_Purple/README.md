# Task 1 — Red, Blue, and Purple Team Perspectives

## Objective

Analyze the CyberDefenders HawkEye packet capture from three complementary perspectives: reconstruct the observed attack-like sequence, identify defensive detection and response opportunities, and hand the findings from Red Team to Blue Team through a Purple Team plan.

## Work performed

- Reconstructed the network sequence visible in `stealer.pcap`, including DNS/HTTP activity, executable transfer, repeated public-IP lookups, and authenticated SMTP submission.
- Produced a Red Team assessment focused on evidence-backed attack-chain interpretation.
- Produced a Blue Team report focused on telemetry, detection opportunities, triage, response, and visibility gaps.
- Produced a Purple Team handover mapping observations to proposed detections, response actions, and controlled validation steps.

## Tools and technologies

Wireshark, Kali Linux, `md5sum`, packet-capture analysis, SMTP/HTTP/DNS inspection, and contextual IP geolocation.

## Deliverables

- [Red Team Assessment](reports/Red-Team-Assessment.docx)
- [Blue Team Detection and Incident Response Report](reports/Blue-Team-Detection-Response.docx)
- [Purple Team Handover Report](reports/Purple-Team-Handover.docx)

This task intentionally remains separate from [Task 4’s standalone HawkEye investigation](../Task-04_HawkEye-Lab/README.md). Task 1 is organized around role-specific Red/Blue/Purple deliverables; Task 4 is a separate consolidated lab investigation report.

## Results

The reports document a coherent network-level sequence and turn it into defensive hunt ideas, proposed correlation logic, response guidance, and a future validation plan. The strongest directly observed areas are packet-level HTTP transfer, repeated outbound activity, and SMTP authentication/message-submission traffic.

## Limitations

The PCAP does not independently prove executable execution, persistence, lateral movement, command-and-control, or the original delivery mechanism. Some host details and decoded-message findings are attributed to investigation notes rather than directly shown in every screenshot. Credentials and authentication values are intentionally not reproduced in the reports.

## Evidence

Task 1 has no separate organized `evidence/` directory; the reports contain or reference the supplied screenshots and investigation notes used for the role-based analysis.
