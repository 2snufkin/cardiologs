import unittest
import pandas as pd
import os

from tools.file_tools import dict_to_excel

class TestFileTools(unittest.TestCase):
    """
    Test the functions inside file_tools
    """


    def test_dict_to_excel(self):
        # Test data
        measurements = {
            'Number of Premature P-Waves': 10,
            'Number of Premature QRS-Waves': 20,
            'Mean Heart Rate': 70,
            'Min Heart Rate': 60,
            'Min Date': '2024-02-17',
            'Min Time': '08:30:00',
            'Max Heart Rate': 80,
            'Max Date': '2024-02-17',
            'Max Time': '09:30:00'
        }
        file_name = 'test_output.xlsx'

        # Call the function
        dict_to_excel(measurements, file_name)

        # Check if file exists
        self.assertTrue(os.path.exists(file_name))

        # Read the Excel file back into a DataFrame
        df = pd.read_excel(file_name)

        # Check DataFrame shape: That it has  1 row and 9 columns.
        self.assertEqual(df.shape, (1, 9))

        # Check column names
        expected_columns = ['Number of Premature P-Waves', 'Number of Premature QRS-Waves', 'Mean Heart Rate',
                            'Min Heart Rate', 'Min Date', 'Min Time', 'Max Heart Rate', 'Max Date', 'Max Time']
        self.assertListEqual(list(df.columns), expected_columns)

        # Clean up: delete the test Excel file
        os.remove(file_name)



if __name__ == '__main__':
    unittest.main()
