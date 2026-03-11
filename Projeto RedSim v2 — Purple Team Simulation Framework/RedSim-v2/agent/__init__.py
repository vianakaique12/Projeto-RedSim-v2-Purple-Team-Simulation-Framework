"""Red team simulation modules."""

from .c2_beacon_sim import simulate_c2
from .cred_access_sim import simulate_credential_access
from .enum_system import collect_system_info
from .persistence_sim import simulate_persistence

__all__ = [
    "simulate_c2",
    "simulate_credential_access",
    "collect_system_info",
    "simulate_persistence",
]
