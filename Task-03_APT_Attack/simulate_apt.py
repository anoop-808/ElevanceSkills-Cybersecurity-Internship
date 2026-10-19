import json
import urllib.request
from datetime import datetime, timezone, timedelta

URL = "http://localhost:9200/task3-apt-simulation/_doc"

scenario = [
    {
        "stage": 1,
        "name": "Initial access indicator",
        "action": "suspicious_login",
        "technique": "T1078",
        "description": "Synthetic indicator: unusual successful login",
        "severity": "medium"
    },
    {
        "stage": 2,
        "name": "Persistence indicator",
        "action": "account_persistence_indicator",
        "technique": "T1136",
        "description": "Synthetic indicator: unexpected account creation",
        "severity": "high"
    },
    {
        "stage": 3,
        "name": "Privilege escalation indicator",
        "action": "privilege_escalation_indicator",
        "technique": "T1068",
        "description": "Synthetic indicator: suspicious privilege escalation",
        "severity": "high"
    },
    {
        "stage": 4,
        "name": "Discovery activity",
        "action": "system_discovery",
        "technique": "T1082",
        "description": "Synthetic indicator: host and system discovery",
        "severity": "low"
    },
    {
        "stage": 5,
        "name": "Lateral movement indicator",
        "action": "lateral_movement_indicator",
        "technique": "T1021",
        "description": "Synthetic indicator: attempted remote-service movement",
        "severity": "high"
    },
    {
        "stage": 6,
        "name": "Exfiltration indicator",
        "action": "exfiltration_indicator",
        "technique": "T1041",
        "description": "Synthetic indicator: suspicious outbound transfer",
        "severity": "critical"
    }
]

now = datetime.now(timezone.utc)
print("Task 3 APT simulation — synthetic telemetry only")
print("No real login, account change, privilege change, or data transfer is performed.\n")

for item in scenario:
    event_time = now + timedelta(seconds=item["stage"] * 10)
    document = {
        "@timestamp": event_time.isoformat(),
        "event": {
            "kind": "event",
            "category": ["intrusion_detection"],
            "action": item["action"],
            "severity": item["severity"]
        },
        "message": item["description"],
        "lab": {
            "task": "ElevanceSkills Task 3",
            "simulation": True,
            "scenario": "APT-01",
            "stage": item["stage"],
            "stage_name": item["name"],
            "evidence_type": "synthetic"
        },
        "threat": {
            "framework": "MITRE ATT&CK",
            "technique": {
                "id": item["technique"]
            }
        }
    }

    request = urllib.request.Request(
        URL + "?refresh=true",
        data=json.dumps(document).encode(),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            result = json.loads(response.read())
            print(
                f"Stage {item['stage']}: {item['name']} "
                f"| indexed={result.get('result')}"
            )
    except Exception as exc:
        print(f"FAILED at stage {item['stage']}: {exc}")
        raise

print("\nSimulation event generation complete.")
