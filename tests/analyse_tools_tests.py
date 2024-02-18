import unittest

import pandas as pd

from tools.analyse_tools import count_tagged_waves, clean_QRS_data, calculate_mean_heart_rate, \
    calculate_min_max_heart_rate_with_time



class TestAnalyseTools(unittest.TestCase):
    """
    Test the functions inside analyse_tools
    """

    def test_count_tagged_waves(self):
        # Create a sample DataFrame for testing
        data = {
            'Wave type': ['P', 'QRS', 'T', 'INV', 'QRS'],
            'Tag1': ['tag1', 'tag2', 'tag3', 'tag4', 'tag2'],
            'Tag2': ['tag2', 'tag2', 'tag7', 'tag8', None],  # Multiple occurrences of 'tag2' for 'QRS'
            'Tag3': ['tag9', 'tag10', 'tag11', 'tag12', None],
            'Wave onset': [100, 200, 300, 400, 100]  # Time in milliseconds
        }
        df = pd.DataFrame(data)

        self.assertEqual(count_tagged_waves(df, 'QRS', 'tag2'), 2)
        self.assertEqual(count_tagged_waves(df, 'T', 'tag11'), 1)
        self.assertEqual(count_tagged_waves(df, 'P', 'tag1'), 1)
        self.assertEqual(count_tagged_waves(df, 'INV', 'tag12'), 1)
        self.assertEqual(count_tagged_waves(df, 'QRS', 'non_existing_tag'), 0)
        with self.assertRaises(ValueError):
            count_tagged_waves(df, 'R', 'tag2')  # 'R' is not a valid wave namet a valid wave name

    def test_clean_QRS_data(self):
        # Create a sample DataFrame containing QRS records
        qrs_data = {
            'Wave type': ['QRS', 'QRS', 'QRS'],
            'Wave onset': [100, 200, 300]  # Time in milliseconds
        }
        qrs_df = pd.DataFrame(qrs_data)

        cleaned_df = clean_QRS_data(qrs_df)
        self.assertEqual(cleaned_df.shape[0], 3)
        self.assertTrue('Time interval' in cleaned_df.columns)
        self.assertTrue('Heart rate' in cleaned_df.columns)

    def test_calculate_mean_heart_rate(self):
        # Create a sample DataFrame containing QRS records
        qrs_data = {
            'Wave type': ['QRS', 'QRS', 'QRS'],
            'Wave onset': [100, 200, 300],  # Time in milliseconds
            'Heart rate': [60, 70, 80]  # Beats per minute
        }
        qrs_df = pd.DataFrame(qrs_data)
        mean_hr = calculate_mean_heart_rate(qrs_df)
        self.assertEqual(mean_hr, 70.0)

    def test_calculate_min_max_heart_rate_with_time(self):
        # Create a sample DataFrame containing QRS records
        qrs_data = {
            'Wave type': ['QRS', 'QRS', 'QRS'],
            'Wave onset': [100, 200, 300],  # Time in milliseconds
            'Heart rate': [60, 70, 80]  # Beats per minute
        }
        qrs_df = pd.DataFrame(qrs_data)
        result_dict = calculate_min_max_heart_rate_with_time(qrs_df)
        self.assertEqual(result_dict['min_heart_rate'], 60)
        self.assertEqual(result_dict['min_time'], 100)
        self.assertEqual(result_dict['max_heart_rate'], 80)
        self.assertEqual(result_dict['max_time'], 300)


if __name__ == '__main__':
    unittest.main()
