from datetime import timedelta, datetime

# A utility that contains methods for manipulating and working with time-related data.

def calculate_time_passed(milliseconds, date_time_obj):
    """
    Calculate the datetime after adding milliseconds to a given datetime.

    Parameters:
    - milliseconds (int): Time elapsed in milliseconds.
    - date_time_obj (datetime.datetime): Datetime object representing the initial date and time.

    Returns:
    - dt (datetime.datetime): Python datetime object representing the time after adding milliseconds.
    """
    # Convert milliseconds to a regular Python integer
    milliseconds = int(milliseconds)

    # Add milliseconds to datetime
    date_time_obj += timedelta(milliseconds=milliseconds)

    return date_time_obj


def convert_string_to_date(date_time_string, format):
    """
     Convert a datetime string to a datetime object using the specified format.

     Parameters:
     - date_time_string (str): The datetime string to convert.
     - format (str): The format of the datetime string, following the conventions of datetime.strptime.

     Returns:
     - date_time_obj (datetime): The datetime object parsed from the provided datetime string.

     Note:
     - If the conversion fails due to an invalid format, a ValueError exception is raised.
     - In case of an error, an error message is logged using the logging module.

     Example:
     convert_string_to_date('2024-02-17T12:30', '%Y-%m-%dT%H:%M')
     """
    try:
        date_time_obj = datetime.strptime(date_time_string, format)
        return date_time_obj

    except ValueError:
        return None


def get_current_datetime():
    """
    Get the current date and time formatted as a string for use as a file name.

    Returns:
        str: Current date and time formatted as "YYYY-MM-DD_HH-MM-SS".
    """
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d-%m-%Y_%H-%M-%S")
    return formatted_datetime