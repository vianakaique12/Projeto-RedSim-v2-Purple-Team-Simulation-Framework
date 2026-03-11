import getpass
import platform
import socket

from redsim.models import SimEvent, utc_now_iso
from redsim.techniques import get_technique


def collect_system_info() -> SimEvent:
    system_info = {
        "os": platform.system(),
        "hostname": socket.gethostname(),
        "user": getpass.getuser(),
        "architecture": platform.machine(),
    }

    technique = get_technique("T1082")
    return SimEvent(
        event_id="system_info_discovery",
        timestamp=utc_now_iso(),
        side="red",
        tactic=technique["tactic"],
        technique_id=technique["id"],
        technique_name=technique["name"],
        description="Collected basic host information",
        metadata=system_info,
    )
