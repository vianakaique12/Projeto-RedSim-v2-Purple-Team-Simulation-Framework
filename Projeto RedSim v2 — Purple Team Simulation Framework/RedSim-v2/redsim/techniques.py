"""MITRE ATT&CK technique mapping used by simulations."""

from typing import Dict

TECHNIQUES: Dict[str, Dict[str, str]] = {
    "T1071": {
        "name": "Application Layer Protocol",
        "tactic": "Command and Control",
    },
    "T1082": {
        "name": "System Information Discovery",
        "tactic": "Discovery",
    },
    "T1547": {
        "name": "Boot or Logon Autostart Execution",
        "tactic": "Persistence",
    },
}


def get_technique(technique_id: str) -> Dict[str, str]:
    data = TECHNIQUES.get(technique_id)
    if data:
        return {"id": technique_id, **data}
    return {"id": technique_id, "name": "Unknown Technique", "tactic": "Unknown"}
