import unittest
from dataclasses import dataclass
from prime_sdk.base_response import BaseResponse

# Create a test response class that inherits from BaseResponse
@dataclass
class TestResponse(BaseResponse):
    field1: str = None
    field2: int = None
    nested_data: dict = None

class TestBaseResponse(unittest.TestCase):
    def test_initialization(self):
        # Test basic field initialization
        test_response = TestResponse(
            field1='value1',
            field2=123,
            nested_data={'nested_field': 'nested_value'}
        )

        self.assertEqual(test_response.field1, 'value1')
        self.assertEqual(test_response.field2, 123)
        self.assertEqual(test_response.nested_data['nested_field'], 'nested_value')

    def test_str_representation(self):
        test_response = TestResponse(field1='value1', field2=123)
        str_repr = str(test_response)
        # Should be JSON representation
        self.assertIn('"field1": "value1"', str_repr)
        self.assertIn('"field2": 123', str_repr)

    def test_empty_initialization(self):
        # Test that BaseResponse can be initialized with default values
        test_response = TestResponse()
        self.assertIsNone(test_response.field1)
        self.assertIsNone(test_response.field2)
        self.assertIsNone(test_response.nested_data)

if __name__ == '__main__':
    unittest.main() 