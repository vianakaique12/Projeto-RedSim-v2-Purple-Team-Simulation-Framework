"""Red team simulation modules."""

from .c2_beacon_sim import simulate_c2
from .enum_system import collect_system_info
from .persistence_sim import simulate_persistence

__all__ = [
    "simulate_c2",
    "collect_system_info",
    "simulate_persistence",
]
