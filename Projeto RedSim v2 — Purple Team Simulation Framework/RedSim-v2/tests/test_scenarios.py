import unittest

from redsim.scenarios import ScenarioDefinition, load_scenario_file, validate_scenario


class TestScenarios(unittest.TestCase):
    def test_load_json_scenario(self) -> None:
        scenario = load_scenario_file("scenarios/basic.json")
        self.assertIsInstance(scenario, ScenarioDefinition)
        self.assertEqual(scenario.name, "basic")
        self.assertGreaterEqual(len(scenario.steps), 1)

    def test_load_enterprise_scenario(self) -> None:
        scenario = load_scenario_file("scenarios/enterprise.json")
        self.assertEqual(scenario.name, "enterprise")
        self.assertGreaterEqual(len(scenario.steps), 3)

    def test_validation_errors(self) -> None:
        with self.assertRaises(ValueError):
            validate_scenario({"name": "", "steps": []})

        with self.assertRaises(ValueError):
            validate_scenario({"name": "bad", "steps": [{"params": {}}]})


if __name__ == "__main__":
    unittest.main()
