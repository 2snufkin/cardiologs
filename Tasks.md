# Task
Write a simple HTTP server that provides the following measurements to a physician when a delineation file is sent to `POST /delineation`:
- V The number of P waves tagged "premature" as well as the number of QRS complexes tagged "premature"
- V The mean heart rate of the recording (Frequency at which QRS complexes appear).
- The minimum and maximum heart rate, each with the time at which they happened. As the date and the time of the recording are not included in the file, the client should be able to set them.
Cardiologs should be able to recover your work, understand it, trust it easily, maintain it, make changes to it, etc.
Bonus question: We want to efficiently host delineations online and be able to quickly request a range of it (e.g.,the record between 2 and 3 pm on the third day). How would you achieve that?




##  csv: 24H of monitoring
Contain data from a Holter monitor, The data is recorded in terms of intervals and waveforms corresponding to various stages of the cardiac cycle. 

Each row in the CSV file represents an interval or a waveform, and each row consists of three values separated by commas. Here's what each value typically represents:

1. **Interval/Event Type**: The first value indicates the type of interval or event being recorded. Common types include:
   - P: Represents the P wave, which corresponds to atrial depolarization.
   - QRS: Represents the QRS complex, which corresponds to ventricular depolarization.
   - T: Represents the T wave, which corresponds to ventricular repolarization.
   - INV: Represents an interval of no specific waveform or an invalid interval.
   

2. **Start Time**: The second value indicates the start time of the interval or event, typically in milliseconds from the start of the recording.
3. **End Time**: The third value indicates the end time of the interval or event, also typically in milliseconds from the start of the recording.

The comments included in some rows provide additional information or annotations about the events being recorded

## Steps

### V create a flask app
### V load the data into a dataframe 
### V write a method that returns a number of waves with the parameters: wave type, tag name v
### V write a function that returns The mean heart rate 
The heart rate is typically calculated based on the intervals between consecutive QRS complexes. Each QRS complex represents a single heartbeat
and the calculation is done bases on the  wave onsets 
### V create a function that given a time in milliseconds and a date and time returned the a date time representation of the times passed 
### V write a function that returns The min and max heart data

