import json
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

url = "http://localhost:9200/task3-apt-simulation/_search"
evidence_dir = Path.home() / "Documents/internship/task3/evidence"
evidence_dir.mkdir(parents=True, exist_ok=True)

query = {
    "size": 50,
    "sort": [{"@timestamp": {"order": "asc"}}],
    "query": {
        "bool": {
            "filter": [
                {"term": {"lab.simulation": True}},
                {"exists": {"field": "lab.stage"}},
                {"terms": {"event.severity.keyword": ["high", "critical"]}}
            ]
        }
    }
}

request = urllib.request.Request(
    url,
    data=json.dumps(query).encode(),
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(request, timeout=10) as response:
    result = json.load(response)

hits = result["hits"]["hits"]

print("========== HIGH/CRITICAL DETECTION RESULTS ==========")
print(f"Matching events: {len(hits)}")

for hit in hits:
    event = hit["_source"]
    lab = event.get("lab", {})
    threat = event.get("threat", {})
    print(
        f"Stage {lab.get('stage')} | "
        f"{event.get('event', {}).get('severity')} | "
        f"{threat.get('technique', {}).get('id')} | "
        f"{event.get('message', 'No message')}"
    )

output = {
    "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    "classification": "synthetic simulation telemetry",
    "query_purpose": "Retrieve high and critical severity simulation events",
    "matching_event_count": len(hits),
    "events": [hit["_source"] for hit in hits]
}

path = evidence_dir / "task3_high_critical_detection.json"
path.write_text(json.dumps(output, indent=2) + "\n")
print(f"\nEvidence saved: {path}")
print("Reminder: these are synthetic events, not proof of a real attack.")
