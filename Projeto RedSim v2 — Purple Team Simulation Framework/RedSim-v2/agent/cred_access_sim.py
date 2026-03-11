from redsim.models import SimEvent, utc_now_iso
from redsim.techniques import get_technique


def simulate_credential_access(source: str = "Browser Password Store (SIMULATED)") -> SimEvent:
    technique = get_technique("T1555")
    return SimEvent(
        event_id="credential_access",
        timestamp=utc_now_iso(),
        side="red",
        tactic=technique["tactic"],
        technique_id=technique["id"],
        technique_name=technique["name"],
        description="Simulated credential access",
        metadata={"source": source},
    )
