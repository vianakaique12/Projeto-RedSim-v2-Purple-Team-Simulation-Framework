"""Rule-based detection stubs for simulated red events."""

from typing import Dict, List

from redsim.models import SimEvent, utc_now_iso


DETECTION_RULES: Dict[str, Dict[str, str]] = {
    "T1071": {
        "rule_id": "DET-001",
        "name": "Outbound C2 beacon detected",
    },
    "T1082": {
        "rule_id": "DET-002",
        "name": "System information discovery observed",
    },
    "T1547": {
        "rule_id": "DET-003",
        "name": "Persistence technique observed",
    },
}


def detect(events: List[SimEvent]) -> List[SimEvent]:
    alerts: List[SimEvent] = []
    for event in events:
        rule = DETECTION_RULES.get(event.technique_id)
        if not rule:
            continue

        alerts.append(
            SimEvent(
                event_id=rule["rule_id"],
                timestamp=utc_now_iso(),
                side="blue",
                tactic="Detection",
                technique_id=event.technique_id,
                technique_name=event.technique_name,
                description=rule["name"],
                metadata={"source_event_id": event.event_id},
            )
        )

    return alerts
