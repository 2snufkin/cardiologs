def count_tagged_waves(df, wave_name, tag):
    """
     Count the occurrences of a given wave with a given tag.

     Parameters:
     - df (pandas.DataFrame): The DataFrame containing wave data.
     - wave_name (str): The name of the wave to count. Should be one of 'P', 'QRS', 'T', or 'INV'.
     - tag (str): The tag to search for within the specified wave type.

     Returns:
     - count (int): The number of occurrences of the specified wave type tagged with the given tag.

     Raises:
     - ValueError: If the wave_name provided is not one of the following: 'P', 'QRS', 'T', or 'INV'.
     """
    # Check if the wave name is valid
    valid_wave_names = ["P", "QRS", "T", "INV"]
    if wave_name not in valid_wave_names:
        raise ValueError("Invalid wave name. Please provide one of 'P', 'QRS', 'T', or 'INV'.")

    # Filter the DataFrame based on the wave name and tag
    filtered_df = df[(df['Wave type'] == wave_name) &
                     ((df['Tag1'] == tag) | (df['Tag2'] == tag) | (df['Tag3'] == tag))]

    # Count the occurrences of the filtered waves
    return len(filtered_df)


def clean_QRS_data(df):
    """
    Filter only QRS records
    For each: 1. Calculate the difference between two Onsets - 'Time interval'
              2. Calculate the heart rate 60/Time interval in seconds.

    Parameters:
    - df (DataFrame): The DataFrame containing ECG delineation data.

    Returns:
    - qrs_records (DataFrame): The processed DataFrame containing QRS records with addition data on the Time interval
    between two wave onset and calculated Heart Rate in beats per minute (bpm).
    """
    # Filter QRS complexes and create a copy to avoid SettingWithCopyWarning
    qrs_records = df[df['Wave type'] == 'QRS'].copy()

    # Calculate time intervals between consecutive QRS complexes
    qrs_records['Time interval'] = qrs_records['Wave onset'].diff()

    # Convert the time intervals from milliseconds to seconds
    time_in_seconds = qrs_records['Time interval'] / 1000

    # Convert time intervals to heart rates (beats per minute)
    qrs_records['Heart rate'] = 60 / time_in_seconds

    return qrs_records


def calculate_mean_heart_rate(qrs_records):
    """
        Calculates the mean heart rate from a DataFrame dat contains only  QRS records and heart rate data.

        Parameters:
        - df (DataFrame): The DataFrame containing heart rate data.

        Returns:
        - mean_heart_rate (float): The mean heart rate (BPM)
        """
    # Check if 'Heart rate' column exists in the DataFrame
    if 'Heart rate' not in qrs_records.columns:
        raise ValueError("'Heart rate' column does not exist in the DataFrame.")

    # Calculate mean heart rate
    mean_heart_rate = qrs_records['Heart rate'].mean()

    return mean_heart_rate


def calculate_min_max_heart_rate_with_time(qrs_records):
    # Check if 'Heart rate' column exists in the DataFrame
    if 'Heart rate' not in qrs_records.columns:
        raise ValueError("'Heart rate' column does not exist in the DataFrame.")

    # Find the index of the row with the minimum and maximum heart rates
    min_index = qrs_records['Heart rate'].idxmin()
    max_index = qrs_records['Heart rate'].idxmax()

    # Extract the minimum and maximum heart rates and their corresponding times
    min_heart_rate = qrs_records.loc[min_index, 'Heart rate']
    min_time = qrs_records.loc[min_index, 'Wave onset']
    max_heart_rate = qrs_records.loc[max_index, 'Heart rate']
    max_time = qrs_records.loc[max_index, 'Wave onset']

    # Construct and return a dictionary with the results
    result_dict = {
        'min_heart_rate': min_heart_rate,
        'min_time': min_time,
        'max_heart_rate': max_heart_rate,
        'max_time': max_time
    }

    return result_dict

