"""Command-line interface for RedSim."""

import argparse
import json
from pathlib import Path
from typing import List, Optional

from .exporters import to_metrics, to_siem, to_sigma
from .simulator import SCENARIOS, run_scenario, run_scenario_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="RedSim v2 - Purple Team Simulation Framework")
    parser.add_argument(
        "--scenario",
        default="basic",
        choices=sorted(SCENARIOS.keys()),
        help="Scenario to run",
    )
    parser.add_argument("--scenario-file", help="Load scenario from JSON/YAML file")
    parser.add_argument(
        "--format",
        default="redsim",
        choices=["redsim", "siem", "sigma", "metrics"],
        help="Output format",
    )
    parser.add_argument("--out", help="Write JSON output to file")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    parser.add_argument("--list-scenarios", action="store_true", help="List available scenarios")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list_scenarios:
        for name in sorted(SCENARIOS.keys()):
            print(name)
        scenario_dir = Path(__file__).resolve().parent.parent / "scenarios"
        if scenario_dir.exists():
            for item in sorted(scenario_dir.glob("*.json")) + sorted(scenario_dir.glob("*.yml")) + sorted(
                scenario_dir.glob("*.yaml")
            ):
                print(item.name)
        return 0

    if args.scenario_file:
        result = run_scenario_file(args.scenario_file)
    else:
        result = run_scenario(args.scenario)

    if args.format == "redsim":
        payload = result.to_dict()
    elif args.format == "siem":
        payload = to_siem(result)
    elif args.format == "sigma":
        payload = to_sigma(result)
    elif args.format == "metrics":
        payload = to_metrics(result)
    else:
        raise ValueError(f"Unsupported format: {args.format}")
    output = json.dumps(payload, indent=2 if args.pretty else None)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(output)
    else:
        print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
