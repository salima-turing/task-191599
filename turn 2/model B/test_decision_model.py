import unittest
from decision_model import decision_model


class TestDecisionModel(unittest.TestCase):
    def setUp(self):
        self.decision_model = decision_model

    # Existing test cases...

    def test_missing_input(self):
        # Test with missing 'age' input
        input_data = {}
        with self.assertRaises(KeyError):
            self.decision_model(input_data)

    def test_invalid_input_data_type(self):
        # Test with non-integer input value
        input_data = {'age': 'invalid'}
        with self.assertRaises(TypeError):
            self.decision_model(input_data)

    def test_null_input(self):
        # Test with null input value
        input_data = {'age': None}
        with self.assertRaises(TypeError):
            self.decision_model(input_data)

    def test_extra_input(self):
        # Test with an extra input field
        input_data = {'age': 25, 'gender': 'M'}
        expected_output = 'Adult'  # Assuming model ignores extra fields
        output = self.decision_model(input_data)
        self.assertEqual(output, expected_output, "Model failed to handle extra input field")


if __name__ == '__main__':
    unittest.main()
