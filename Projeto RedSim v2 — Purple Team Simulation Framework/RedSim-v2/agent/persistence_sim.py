from redsim.models import SimEvent, utc_now_iso
from redsim.techniques import get_technique


def simulate_persistence(method: str = "Startup Folder (SIMULATED)") -> SimEvent:
    technique = get_technique("T1547")
    return SimEvent(
        event_id="persistence_attempt",
        timestamp=utc_now_iso(),
        side="red",
        tactic=technique["tactic"],
        technique_id=technique["id"],
        technique_name=technique["name"],
        description="Simulated persistence attempt",
        metadata={"method": method},
    )
