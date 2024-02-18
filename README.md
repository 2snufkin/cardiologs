# Holter Record Summary HTTP Server

This HTTP server processes delineation files and provides various measurements to physicians.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your_username/holter-record-summary.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
python app.py
```

2. Navigate to `http://localhost:5000/delineation`.

3. Upload the csv file and provide with a date and time.

4. A csv file will be downloaded immediately. The file contains the following:
- The number of P waves tagged "premature" as well as the number of QRS complexes tagged "premature"
- The mean heart rate of the recording 
- The minimum and maximum heart rate, each with the time at which they happened. 

## Endpoints

- `POST /delineation`: Upload a delineation file.

