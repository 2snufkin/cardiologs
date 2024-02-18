import os

import pandas as pd


# A utility that contains methods for manipulating and working with Excel files, and file in general


def dict_to_excel(data_dict, file_name):
    """
    Convert a dictionary to an Excel file.

    Parameters:
    - data_dict (dict): The dictionary containing the data.
    - file_name (str): The name of the Excel file to be created.

    Returns:
    - None
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame.from_dict(data_dict, orient='index')

    # Transpose the DataFrame to swap rows and columns
    df = df.transpose()

    # Write the DataFrame to an Excel file
    df.to_excel(file_name, index=False)


def delete_file(file_path):
    """
    Deletes a file at the specified path.

    Parameters:
        file_path (str): The path to the file to be deleted.

    Returns:
        bool: True if the file was successfully deleted, False otherwise.
    """
    try:
        os.remove(file_path)
        return True
    except OSError as e:
        # If the file doesn't exist or other OS-related errors occur
        # In a real app I would use a logger
        print(f"Error deleting file: {e}")
        return False
