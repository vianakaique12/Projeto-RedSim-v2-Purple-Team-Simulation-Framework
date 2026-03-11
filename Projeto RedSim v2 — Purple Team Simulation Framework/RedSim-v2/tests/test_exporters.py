import unittest

from redsim.exporters import to_metrics, to_siem, to_sigma
from redsim.simulator import run_scenario


class TestExporters(unittest.TestCase):
    def test_metrics(self) -> None:
        result = run_scenario("basic")
        metrics = to_metrics(result)
        self.assertIn("total_events", metrics)
        self.assertIn("by_technique", metrics)

    def test_siem(self) -> None:
        result = run_scenario("basic")
        events = to_siem(result)
        self.assertGreaterEqual(len(events), 1)
        self.assertIn("@timestamp", events[0])

    def test_sigma(self) -> None:
        result = run_scenario("basic")
        rules = to_sigma(result)
        self.assertGreaterEqual(len(rules), 1)
        self.assertIn("detection", rules[0])


if __name__ == "__main__":
    unittest.main()
