"""Scenario file loading and validation."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List


@dataclass(frozen=True)
class ScenarioStep:
    action: str
    params: Dict[str, Any]


@dataclass(frozen=True)
class ScenarioDefinition:
    name: str
    steps: List[ScenarioStep]


def _validate_step(raw: Dict[str, Any], index: int) -> ScenarioStep:
    if not isinstance(raw, dict):
        raise ValueError(f"Step {index} must be an object")

    if "action" not in raw:
        raise ValueError(f"Step {index} missing required field 'action'")

    action = raw["action"]
    if not isinstance(action, str) or not action.strip():
        raise ValueError(f"Step {index} field 'action' must be a non-empty string")

    params = raw.get("params", {})
    if params is None:
        params = {}
    if not isinstance(params, dict):
        raise ValueError(f"Step {index} field 'params' must be an object")

    extra_keys = set(raw.keys()) - {"action", "params"}
    if extra_keys:
        extras = ", ".join(sorted(extra_keys))
        raise ValueError(f"Step {index} contains unsupported keys: {extras}")

    return ScenarioStep(action=action, params=params)


def validate_scenario(data: Dict[str, Any]) -> ScenarioDefinition:
    if not isinstance(data, dict):
        raise ValueError("Scenario must be a JSON/YAML object")

    name = data.get("name")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Scenario 'name' must be a non-empty string")

    steps_raw = data.get("steps")
    if not isinstance(steps_raw, list) or not steps_raw:
        raise ValueError("Scenario 'steps' must be a non-empty list")

    steps = [_validate_step(step, index) for index, step in enumerate(steps_raw, start=1)]
    return ScenarioDefinition(name=name, steps=steps)


def load_json(path: Path) -> ScenarioDefinition:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return validate_scenario(payload)


def load_yaml(path: Path) -> ScenarioDefinition:
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "PyYAML is required to load YAML scenarios. Install with 'pip install pyyaml'."
        ) from exc

    with path.open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle)
    return validate_scenario(payload)


def load_scenario_file(path: str | Path) -> ScenarioDefinition:
    scenario_path = Path(path)
    if not scenario_path.exists():
        raise FileNotFoundError(f"Scenario file not found: {scenario_path}")

    suffix = scenario_path.suffix.lower()
    if suffix == ".json":
        return load_json(scenario_path)
    if suffix in {".yaml", ".yml"}:
        return load_yaml(scenario_path)

    raise ValueError("Scenario file must be .json, .yaml, or .yml")
