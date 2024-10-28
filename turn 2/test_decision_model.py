import unittest
from decision_model import decision_model


class TestDecisionModel(unittest.TestCase):
    def setUp(self):
        # Initialize the decision model function
        self.decision_model = decision_model

    # Existing test cases...

    def test_unexpected_input_type(self):
        input_data = {'age': 'twenty-five'}  # Unexpected input type (string instead of int)
        with self.assertRaises(TypeError):
            self.decision_model(input_data)

    def test_missing_input_key(self):
        input_data = {}  # Missing 'age' key
        with self.assertRaises(KeyError):
            self.decision_model(input_data)

    def test_extra_input_key(self):
        input_data = {'age': 25, 'extra_key': 'some value'}  # Extra input key
        with self.assertRaises(KeyError):
            self.decision_model(input_data)

    def test_non_dict_input(self):
        input_data = ['list', 'of', 'values']  # Non-dict input
        with self.assertRaises(TypeError):
            self.decision_model(input_data)

    def test_null_input(self):
        input_data = None
        with self.assertRaises(TypeError):
            self.decision_model(input_data)


if __name__ == '__main__':
    unittest.main()
