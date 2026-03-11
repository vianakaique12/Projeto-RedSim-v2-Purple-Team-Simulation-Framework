"""Export simulation results into external-friendly formats."""

from collections import Counter
from typing import Dict, List

from .models import SimEvent, SimulationResult


def _event_to_siem(event: SimEvent) -> Dict[str, object]:
    category = "intrusion_detection" if event.side == "blue" else "malware"
    kind = "alert" if event.side == "blue" else "event"

    return {
        "@timestamp": event.timestamp,
        "event": {
            "id": event.event_id,
            "kind": kind,
            "category": [category],
            "type": ["info"],
            "action": event.description,
            "dataset": "redsim.simulation",
        },
        "attack": {
            "tactic": event.tactic,
            "technique": event.technique_name,
            "technique_id": event.technique_id,
        },
        "redsim": {
            "side": event.side,
            "metadata": event.metadata,
        },
    }


def to_siem(result: SimulationResult) -> List[Dict[str, object]]:
    return [_event_to_siem(event) for event in result.all_events()]


def to_sigma(result: SimulationResult) -> List[Dict[str, object]]:
    seen = {}
    for event in result.red_events:
        key = event.technique_id
        if key not in seen:
            seen[key] = event

    rules: List[Dict[str, object]] = []
    for technique_id, event in sorted(seen.items()):
        rules.append(
            {
                "title": f"RedSim {event.technique_name}",
                "id": f"redsim-{technique_id.lower()}",
                "status": "experimental",
                "description": f"Simulated detection for {event.technique_name}",
                "tags": [f"attack.{technique_id.lower()}", f"attack.{event.tactic.lower().replace(' ', '_')}"],
                "logsource": {"product": "redsim", "category": "simulation"},
                "detection": {
                    "selection": {"technique_id": technique_id},
                    "condition": "selection",
                },
            }
        )

    return rules


def to_metrics(result: SimulationResult) -> Dict[str, object]:
    technique_counts = Counter(event.technique_id for event in result.all_events())
    tactic_counts = Counter(event.tactic for event in result.all_events())
    side_counts = Counter(event.side for event in result.all_events())

    return {
        "scenario": result.scenario,
        "total_events": len(result.all_events()),
        "by_technique": dict(sorted(technique_counts.items())),
        "by_tactic": dict(sorted(tactic_counts.items())),
        "by_side": dict(sorted(side_counts.items())),
    }
