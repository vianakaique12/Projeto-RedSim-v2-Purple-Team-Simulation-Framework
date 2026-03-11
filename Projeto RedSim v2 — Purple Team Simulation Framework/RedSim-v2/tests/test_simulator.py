import unittest

from redsim.simulator import run_scenario


class TestSimulator(unittest.TestCase):
    def test_basic_scenario(self) -> None:
        result = run_scenario("basic")
        self.assertEqual(result.scenario, "basic")
        self.assertGreaterEqual(len(result.red_events), 3)
        self.assertGreaterEqual(len(result.blue_events), 1)

        for event in result.red_events + result.blue_events:
            self.assertTrue(event.event_id)
            self.assertTrue(event.timestamp.endswith("Z"))
            self.assertTrue(event.technique_id)
            self.assertTrue(event.technique_name)

    def test_unknown_scenario(self) -> None:
        with self.assertRaises(ValueError):
            run_scenario("does_not_exist")


if __name__ == "__main__":
    unittest.main()
