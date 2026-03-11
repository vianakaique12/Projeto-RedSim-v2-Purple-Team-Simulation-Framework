"""Scenario orchestration for RedSim."""

from __future__ import annotations

from pathlib import Path
from typing import Callable, Dict, Iterable, List, Union

from agent import collect_system_info, simulate_c2, simulate_credential_access, simulate_persistence
from blue_team import detect

from .models import SimEvent, SimulationResult
from .scenarios import ScenarioDefinition, ScenarioStep, load_scenario_file


ACTION_REGISTRY: Dict[str, Callable[..., SimEvent]] = {
    "collect_system_info": collect_system_info,
    "simulate_persistence": simulate_persistence,
    "simulate_credential_access": simulate_credential_access,
    "simulate_c2": simulate_c2,
}


def _run_basic() -> SimulationResult:
    return run_steps(
        "basic",
        [
            ScenarioStep(action="collect_system_info", params={}),
            ScenarioStep(action="simulate_persistence", params={}),
            ScenarioStep(action="simulate_c2", params={}),
        ],
    )


SCENARIOS: Dict[str, Callable[[], SimulationResult]] = {
    "basic": _run_basic,
}


def run_scenario(name: str) -> SimulationResult:
    scenario = SCENARIOS.get(name)
    if not scenario:
        raise ValueError(f"Unknown scenario: {name}")
    return scenario()


def run_steps(name: str, steps: Iterable[ScenarioStep]) -> SimulationResult:
    red_events: List[SimEvent] = []
    for step in steps:
        action = ACTION_REGISTRY.get(step.action)
        if not action:
            raise ValueError(f"Unsupported action: {step.action}")
        red_events.append(action(**step.params))

    blue_events = detect(red_events)
    return SimulationResult(scenario=name, red_events=red_events, blue_events=blue_events)


def run_scenario_file(path: Union[str, Path]) -> SimulationResult:
    scenario = load_scenario_file(path)
    return run_steps(scenario.name, scenario.steps)
