# Task 6 Finalization Audit

Date: 2026-10-16

## Final decision

Report B was used as the base. A new corrected copy was created at:

`Task-06_Custom-SIEM-Dashboard/reports/Task6_Custom_SIEM_Dashboard_Report_FINAL.docx`

The original Report A and Report B were not overwritten, renamed, moved, or deleted.

## Original report hashes

| File | SHA-256 | Status |
|---|---|---|
| `Task-06_Custom-SIEM-Dashboard/reports/Task6_Custom_SIEM_Dashboard_Report.docx` | `9d08d598d8e7a4e83ca4de38e3af1f8f81115d6a6f0f542368e7a743139dfed9` | Unchanged; matches previous audit |
| `task 6/Task6_Custom_SIEM_Dashboard_Report (1).docx` | `2f502d0f4d717c1a22dec5d7f12ef8748048eeb2aa50db9f44381f3c0b612fd3` | Unchanged; matches previous audit |

Final report SHA-256:

`1e1f86c1bb073811344a6277856e8bdf635140029cbc3faf5c07a942c43ba5ec`

The backup `/home/karna/internship-backup-before-reorganisation.tar.gz` was present and was not modified. Its observed SHA-256 was `795755a464ecfd507ba643bf639306810af6c181a403a559ad102cfe5a6d9597`.

## Evidence reviewed

The retained Task 6 evidence consists of:

- `evidence/01_Task6_Dashboard_Overview.png`
- `evidence/02_Task6_Dashboard_Security_Events.png`
- `evidence/03_Task6_Visualization_Library.png`

The three images are embedded in both original reports and in the new final report. Their bytes and SHA-256 values are unchanged.

No Task 6 Filebeat configuration, Elasticsearch response, Kibana export, raw authentication log, runtime-field definition, SCP query, or command-output transcript was present in the Task 6 folder.

## Technical claim audit

| Claim or issue | Classification | Result |
|---|---|---|
| Final dashboard contains 9 failed-password documents and three count cards of 3 | Verified from available evidence | Confirmed by the dashboard overview screenshot |
| Source-IP table displays 9, 3, and 1 values, including a malformed extraction value | Verified from available evidence | Confirmed by the security-events screenshot |
| Cause of the 9-document versus 9+3+1 source-IP discrepancy | Unresolved | No retained filter, query, or raw-event data explains it |
| Approximately 1,893 indexed documents and an earlier count of 6 failed-password events | Reported in the original document but not independently verified | No Elasticsearch response or query output was retained |
| `filebeat test config` and `filebeat test output` passed | Reported in the original document but not independently verified | No command output was retained |
| Elasticsearch 9.5.4 API result and yellow cluster health | Reported in the original document but not independently verified | No API or cluster-health evidence was retained |
| SCP indicator count of 3 | Verified from available evidence | The displayed count is visible in the security-events screenshot |
| Underlying SCP-related log records, exact query/filter, and SHA-256 transfer output | Reported in the original document but not independently verified | No raw records, query, or command output was retained |
| Exact `ssh_source_ip` runtime-field expression | Unresolved | The report describes the pattern but no exact expression was retained |
| Controlled SSH failures, sudo activity, and local SCP transfer are not confirmed attacks | Verified from available evidence and report scope | The report and final wording explicitly state these limitations |
| Confirmed brute-force attack, privilege escalation, or real network exfiltration | Not demonstrated | The retained evidence does not support those claims |

## Corrections made to the final copy

- Preserved Report B’s corrected Section 14 subsection numbering.
- Preserved the clearer malformed-source-IP explanation.
- Marked unsupported command-level and infrastructure claims as reported but not independently verified.
- Documented the source-IP count discrepancy as unresolved rather than inventing an explanation.
- Clarified that the screenshot verifies the displayed SCP indicator count, but not the underlying records or query.
- Added the missing-evidence limitation for the runtime-field expression, Filebeat configuration, verification outputs, and SCP query.
- Reworded the Results and Conclusion sections to distinguish documented lab validation from confirmed attack detection.
- Explicitly stated that the controlled tests did not demonstrate confirmed brute force, privilege escalation, or real network exfiltration.

## Validation performed

- Confirmed the final DOCX is a valid ZIP/DOCX package with no corrupt members.
- Confirmed the final document contains three embedded figures.
- Confirmed all 17 main sections remain present.
- Confirmed Section 14 subsections are numbered `14.1` through `14.4`.
- Confirmed the old `13.1`–`13.5` subsection numbering is absent.
- Extracted final text and checked for the unresolved-discrepancy and evidence-limitation wording.
- Confirmed all three embedded figure hashes match the retained evidence files.
- Attempted temporary PDF rendering with LibreOffice. It failed because the environment prevented LibreOffice from writing its dconf runtime file; no PDF was created. The original documents were not affected.
- Recalculated Report A and Report B hashes after editing; both remain unchanged.

## Portfolio structure review

The six expected task folders exist. The organized folders contain the expected reports and available evidence for Tasks 1–6. Task 1 has separate Red, Blue, and Purple reports. Tasks 2–6 contain their observed reports and evidence/scripts/notes as applicable. The `elevance/` folder remains present for programme materials.

Additional legacy folders (`task 1 & 4`, `task 5`, `task 6`, `task2`, and `task3`) remain present. They were not modified or cleaned up. The alternate Task 6 report remains in `task 6/` pending a separately approved cleanup plan.

## Git and safety status

No Git repository was initialized, no commit or push was performed, and nothing was uploaded. No original report, evidence file, or backup archive was modified.

## Remaining work before portfolio publication

Before README creation and a single GitHub push, decide whether to retain or archive the legacy folders, review any private or machine-specific details, and perform a final portfolio-wide consistency and disclosure review. Task 6 would be stronger if the missing raw/configuration artifacts were recovered, but the final report now labels those gaps instead of asserting independent verification.
