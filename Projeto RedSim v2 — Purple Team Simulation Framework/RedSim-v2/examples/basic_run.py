"""Example usage: run the basic scenario and print events."""

from redsim.simulator import run_scenario


def main() -> None:
    result = run_scenario("basic")
    for event in result.all_events():
        print(event.to_dict())


if __name__ == "__main__":
    main()
