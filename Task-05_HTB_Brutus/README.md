# Task 5 — HTB Sherlock Brutus DFIR Investigation

## Objective

Reconstruct an SSH compromise from host-based `auth.log` and `wtmp` artifacts and answer the eight Brutus investigation questions with evidence-backed timestamps, accounts, sessions, persistence activity, and sudo commands.

## Work performed

- Correlated failed and successful SSH authentication events by source and username.
- Parsed `wtmp` to establish terminal-session timing alongside `auth.log` authentication and sudo records.
- Reconstructed the sequence from brute-force activity through root access, local-account creation, sudo-group membership, and later sudo commands.
- Mapped the persistence behavior to MITRE ATT&CK T1136.001, Local Account.
- Documented the timeline, findings, methodology, lessons learned, and evidence appendix.

## Results

The investigation identifies the attacker source, compromised root account, interactive session, persistence account, session closure, and sudo download command from the supplied artifacts. It also explains the difference between authentication timestamps and terminal-login timestamps.

The report does not claim that the downloaded script executed because no endpoint, disk, memory, or network evidence was supplied for that question.

## Tools and technologies

Linux `grep`, `less`, `column`, Python-based `utmp/wtmp` parsing, `auth.log`, `wtmp`, and MITRE ATT&CK mapping.

## Deliverables and evidence

- [Investigation report](reports/HTB_Sherlock_Brutus_Investigation_Report.pdf)
- [Renamed evidence archive](evidence/Brutus_Task5_Evidence_Renamed.zip)
- [Attacker-IP evidence](evidence/screenshots/Task1_Brute_Force_Attacker_IP.png)
- [Authentication correlation](evidence/screenshots/Task1_Attacker_IP_AuthLog_Correlation.png)
- [Successful root login](evidence/screenshots/Task2_Successful_Root_Login.png)
- [WTMP root session](evidence/screenshots/Task3_WTMP_Root_Session.png)
- [Session creation](evidence/screenshots/Task4_Session_37_Creation.png)
- [Persistence-account creation](evidence/screenshots/Task5_Cyberjunkie_Creation.png)
- [Sudo privileges](evidence/screenshots/Task5_Cyberjunkie_Sudo_Privileges.png)
- [Session closure](evidence/screenshots/Task7_Session_37_Closure.png)
- [Sudo download command](evidence/screenshots/Task8_Sudo_Curl_Command.png)
- [Full WTMP output](evidence/screenshots/WTMP_Full_Output.png)
- [WTMP parsing evidence](evidence/screenshots/WTMP_Parsing_Tool_Investigation.png)

## Limitations

No packet capture, endpoint image, memory image, or downloaded script was supplied. The report flags a tooling discrepancy between the documented parser name and the parser shown in the supporting evidence. Whether the downloaded script executed, and whether the host was remediated, cannot be established from the retained artifacts.
