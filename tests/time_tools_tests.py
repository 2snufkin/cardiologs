import unittest
from datetime import datetime

from tools.time_tools import calculate_time_passed, convert_string_to_date


class TestTimeTools(unittest.TestCase):
    """
       Test the functions inside time_tools
       """

    def test_calculate_time_passed(self):
        # Define a base datetime object
        base_datetime = datetime(2022, 1, 1, 0, 0, 0)

        # Test case 1: Adding 1000 milliseconds
        result_datetime = calculate_time_passed(1000, base_datetime)
        self.assertEqual(result_datetime, datetime(2022, 1, 1, 0, 0, 1))

        # Test case 2: Adding 500 milliseconds
        result_datetime = calculate_time_passed(500, base_datetime)
        self.assertEqual(result_datetime, datetime(2022, 1, 1, 0, 0, 0, 500000))

    def test_convert_string_to_date(self):
        # Test case 1: Valid datetime string
        result_datetime = convert_string_to_date('2022-01-01T12:00', '%Y-%m-%dT%H:%M')
        self.assertEqual(result_datetime, datetime(2022, 1, 1, 12, 0))
        self.assertIsNotNone(result_datetime)

        # Test case 2: Invalid datetime string
        result_datetime = convert_string_to_date('2022-01-01 12:00', '%Y-%m-%dT%H:%M')
        self.assertIsNone(result_datetime)


if __name__ == '__main__':
    unittest.main()
