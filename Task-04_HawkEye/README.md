# Task 4 — HawkEye Lab Investigation

## Objective

Investigate the CyberDefenders HawkEye `stealer.pcap` packet capture and document the observed network activity, indicators, attack-chain interpretation, defensive detections, and response recommendations.

## Work performed

- Established the capture baseline and endpoint context in Wireshark.
- Investigated DNS, HTTP executable transfer, repeated public-IP lookup traffic, and recurring SMTP sessions.
- Extracted the HTTP object and recorded its MD5 with Kali Linux tooling.
- Reviewed SMTP authentication, message submission, timing, and the reported decoded message content without reproducing credentials.
- Produced Red Team, Blue Team, and Purple Team analysis within one consolidated investigation report.

## Results

The report documents 4,003 packets over 01:03:41, an HTTP executable transfer, repeated external lookup traffic, and recurring authenticated SMTP submission from the captured host. It turns those observations into proposed detection logic, response steps, and visibility improvements.

## Tools and technologies

Wireshark, Kali Linux, `md5sum`, packet-capture filters, HTTP object export, TCP-stream analysis, SMTP/DNS inspection, and contextual IP geolocation.

## Deliverables and evidence

- [HawkEye investigation report](reports/HawkEye_Lab_Investigation_Report.docx)
- [Capture properties](evidence/hawkeye-screenshots/01_capture_properties.png)
- [Ethernet endpoints](evidence/hawkeye-screenshots/02_ethernet_endpoints.png)
- [IPv4 endpoints](evidence/hawkeye-screenshots/04_ipv4_endpoints.png)
- [HTTP-filtered packet view](evidence/hawkeye-screenshots/06_dns_query_204.png)
- [HTTP object export](evidence/hawkeye-screenshots/09_HTTP_Export_Object_tkraw_Protected99.png)
- [Extracted-file hash](evidence/hawkeye-screenshots/10_Malware_File_MD5_Hash.png)
- [Server geolocation context](evidence/hawkeye-screenshots/07_Malware_Server_IP_Geolocation.png)
- [Retained screenshot archive](evidence/hawkeye-screenshots.zip)

## Limitations and publication note

The PCAP does not prove executable execution, persistence, lateral movement, command-and-control, or the original delivery mechanism. Endpoint, memory, disk, and reverse-engineering evidence were outside scope. Some findings come from investigation notes rather than directly from a screenshot.

The SMTP authentication screenshots and ZIP archive contain sensitive authentication material in the retained working evidence and require redaction or access restriction before public GitHub publication. No credentials are reproduced in this README.
