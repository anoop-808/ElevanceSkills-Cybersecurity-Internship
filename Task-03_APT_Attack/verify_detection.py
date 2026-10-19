import json
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

base = "http://localhost:9200/task3-apt-simulation"
out = Path.home() / "Documents/internship/task3/evidence"
out.mkdir(parents=True, exist_ok=True)

def query(body):
    req = urllib.request.Request(
        base + "/_search",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)

body = {
    "size": 100,
    "sort": [{"@timestamp": {"order": "asc"}}],
    "_source": [
        "@timestamp", "message", "event.action", "event.severity",
        "lab.simulation", "lab.stage", "lab.stage_name",
        "lab.evidence_type", "threat.technique.id"
    ],
    "query": {
        "bool": {
            "filter": [
                {"term": {"lab.simulation": True}},
                {"exists": {"field": "lab.stage"}}
            ]
        }
    }
}

data = query(body)
hits = data["hits"]["hits"]
stages = {}

for hit in hits:
    src = hit["_source"]
    stage = src.get("lab", {}).get("stage")
    if stage is not None:
        stages.setdefault(str(stage), []).append(src)

print("========== DETECTION COVERAGE ==========")
for stage in range(1, 7):
    records = stages.get(str(stage), [])
    print(f"Stage {stage}: {'FOUND' if records else 'MISSING'} ({len(records)} record(s))")

evidence = {
    "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    "dataset": "task3-apt-simulation",
    "classification": "synthetic simulation telemetry",
    "total_stage_records": len(hits),
    "distinct_stages_found": sorted(int(s) for s in stages),
    "stage_counts": {s: len(v) for s, v in stages.items()},
    "events": [h["_source"] for h in hits]
}

path = out / "task3_detection_evidence.json"
path.write_text(json.dumps(evidence, indent=2) + "\n")
print(f"\nEvidence saved: {path}")
print("Note: synthetic indicators are not proof of a real intrusion.")
