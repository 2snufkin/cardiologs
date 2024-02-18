import time

import pandas as pd
from flask import Flask, request, send_file, render_template, jsonify

from tools.analyse_tools import count_tagged_waves, calculate_mean_heart_rate, calculate_min_max_heart_rate_with_time, \
    clean_QRS_data
from tools.file_tools import dict_to_excel, delete_file
from tools.time_tools import convert_string_to_date, calculate_time_passed, get_current_datetime

app = Flask(__name__)


@app.get('/delineation')
def delineation_form():
    return render_template('analyse_result.html')


@app.post('/delineation')
def process_delineation():
    """
    Endpoint to process delineation data from a CSV file and provide relevant measurements as the form of an excel file

    From the form:
        file: CSV file containing delineation data.
        datetime: Datetime string indicating the reference time for heart rate measurements (format: %Y-%m-%dT%H:%M).

    Returns:
        - If successful, returns an Excel file containing measurements with status code 200.
        - If the request is incorrect or the file cannot be processed, returns an appropriate error response.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file was added'}), 400

    datetime_string = request.form['datetime']
    if not datetime_string:
        return jsonify({'error': 'Datetime parameter is missing'}), 400


    try:
        uploaded_file = request.files['file']

        if uploaded_file:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(uploaded_file, header=None,
                             names=['Wave type', 'Wave onset', 'Wave offset', 'Tag1', 'Tag2', 'Tag3'])

            # the number of P waves tagged "premature" as well as the number of QRS complexes tagged "premature"
            p_with_premature = count_tagged_waves(df, "P", "premature")
            qrs_with_premature = count_tagged_waves(df, "QRS", "premature")

            # filter only QRS records
            qrs_records = clean_QRS_data(df)

            #  the mean heart rate of the recording
            mean_heart_rate = calculate_mean_heart_rate(qrs_records)

            # the minimum and maximum heart rate, each with the time at which they happened.
            min_and_max_heart_rate = calculate_min_max_heart_rate_with_time(qrs_records)

            # create a dict to write to an Excel file
            measurements = {
                'Number of Premature P-Waves': p_with_premature,
                'Number of Premature QRS-Waves': qrs_with_premature,
                'Mean Heart Rate': mean_heart_rate,
                'Min Heart Rate': min_and_max_heart_rate.get("min_heart_rate"),
                'Max Heart Rate': min_and_max_heart_rate.get("max_heart_rate"),
            }
            # convert the date string from the form to a datetime object
            date_time_obj = convert_string_to_date(datetime_string, '%Y-%m-%dT%H:%M')

            # if date_time_obj is not None, do the following
            if date_time_obj:
                min_heart_rate_datetime = calculate_time_passed(min_and_max_heart_rate["min_time"], date_time_obj)
                max_heart_rate_datetime = calculate_time_passed(min_and_max_heart_rate["max_time"], date_time_obj)
                measurements['Min Heart Rate Time'] = min_heart_rate_datetime
                measurements['Max Heart Rate Time'] = max_heart_rate_datetime

            # the downloaded file name will contain heartbeat_analysis_ + the current date & time
            result_path = f"heartbeat_analysis_{get_current_datetime()}.xlsx"

            dict_to_excel(measurements, result_path)

            # Send the file to the user
            response = send_file(result_path, as_attachment=True, download_name=result_path)

            return response, 200
        else:
            return jsonify({'error': 'File upload failed or no file provided'}), 400

    except Exception as e:
        return str(e), 500



if __name__ == '__main__':
    app.run(debug=True)
