import time

from redsim.models import SimEvent, utc_now_iso
from redsim.techniques import get_technique


def simulate_c2(destination: str = "c2.fake-server.local", delay_seconds: float = 1.0) -> SimEvent:
    if delay_seconds:
        time.sleep(delay_seconds)

    technique = get_technique("T1071")
    return SimEvent(
        event_id="c2_beacon",
        timestamp=utc_now_iso(),
        side="red",
        tactic=technique["tactic"],
        technique_id=technique["id"],
        technique_name=technique["name"],
        description="Simulated C2 beacon activity",
        metadata={"destination": destination},
    )
