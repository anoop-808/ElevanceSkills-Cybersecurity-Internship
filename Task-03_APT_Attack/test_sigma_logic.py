import json
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

base = "http://localhost:9200/task3-apt-simulation/_search"
out = Path.home() / "Documents/internship/task3/evidence"
out.mkdir(parents=True, exist_ok=True)

query = {
    "size": 100,
    "query": {
        "bool": {
            "filter": [
                {"term": {"lab.simulation": True}},
                {"term": {"lab.evidence_type.keyword": "synthetic"}},
                {"terms": {"event.severity.keyword": ["high", "critical"]}}
            ]
        }
    }
}

req = urllib.request.Request(
    base,
    data=json.dumps(query).encode(),
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(req, timeout=10) as response:
    result = json.load(response)

hits = result["hits"]["hits"]
events = [h["_source"] for h in hits]

print("========== SIGMA LOGIC TEST ==========")
print(f"Matching records: {len(events)}")
print(f"Unique stages: {len(set(e.get('lab', {}).get('stage') for e in events))}")

for event in events:
    lab = event.get("lab", {})
    print(
        f"Stage {lab.get('stage')} | "
        f"{event.get('event', {}).get('severity')} | "
        f"{event.get('message', '')}"
    )

evidence = {
    "tested_at_utc": datetime.now(timezone.utc).isoformat(),
    "test_type": "Elasticsearch equivalent filter; not Sigma parser validation",
    "synthetic_telemetry_only": True,
    "matching_record_count": len(events),
    "unique_stage_count": len(set(e.get('lab', {}).get('stage') for e in events)),
    "events": events
}

path = out / "task3_sigma_logic_test.json"
path.write_text(json.dumps(evidence, indent=2) + "\n")
print(f"\nEvidence saved: {path}")
