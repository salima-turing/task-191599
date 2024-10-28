import unittest
from decision_model import decision_model


class TestDecisionModel(unittest.TestCase):
    def setUp(self):
        # Initialize the decision model function
        self.decision_model = decision_model

    def test_adult_input(self):
        # Test with an adult input
        input_data = {'age': 25}
        expected_output = 'Adult'
        output = self.decision_model(input_data)
        self.assertEqual(output, expected_output, "Model failed to classify adult input correctly")

    def test_minor_input(self):
        # Test with a minor input
        input_data = {'age': 17}
        expected_output = 'Minor'
        output = self.decision_model(input_data)
        self.assertEqual(output, expected_output, "Model failed to classify minor input correctly")


if __name__ == '__main__':
    unittest.main()
