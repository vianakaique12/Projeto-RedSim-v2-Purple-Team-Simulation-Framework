"""Core data models used across the simulation."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List


def utc_now_iso() -> str:
    """Return current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


@dataclass(frozen=True)
class SimEvent:
    event_id: str
    timestamp: str
    side: str
    tactic: str
    technique_id: str
    technique_name: str
    description: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SimulationResult:
    scenario: str
    red_events: List[SimEvent]
    blue_events: List[SimEvent]

    def all_events(self) -> List[SimEvent]:
        return self.red_events + self.blue_events

    def to_dict(self) -> Dict[str, Any]:
        return {
            "scenario": self.scenario,
            "red_events": [event.to_dict() for event in self.red_events],
            "blue_events": [event.to_dict() for event in self.blue_events],
        }
