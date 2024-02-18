# ECG Delineation Analysis Server
This app is a  HTTP server that analyzes electrocardiography (ECG) delineation data and provides measurements to a physician.

## Introduction
The server is designed to receive delineation files via a POST request to /delineation endpoint. Upon receiving a delineation file, the server performs the following analyses:

+ Counts the number of P waves tagged as "premature" and the number of QRS complexes tagged as "premature".
+ Calculates the mean heart rate of the recording based on the frequency at which QRS complexes appear.
+ Determines the minimum and maximum heart rates along with the time at which they occurred.

## How to use the application
For this application, you will need to have a Python on your machine
### Step 1: Clone the Flask Project
Clone the Flask project from the Git repository using the `git clone` command:
```bash
git clone <repository_url>
```
Replace `<repository_url>` with the URL of the Git repository containing the Flask project.

### Step 2: Navigate to the Project Directory
Navigate using with cmd to the cardiologs subfolder of the same directory where the cloned Flask project lie.

### Step 3: Create a Virtual Environment
Create a virtual environment using `virtualenv` or `venv`. Here, we'll use `venv`:
```bash
python -m venv venv
```
This command creates a virtual environment named `venv` in the project directory.

### Step 4: Activate the Virtual Environment
Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS and Linux:
```bash
source venv/bin/activate
```

### Step 5: Install Dependencies
Install the dependencies listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 6: Set Flask App
Set the Flask app environment variable (if required):
- On Windows:
```bash
set FLASK_APP=app.py
```
- On macOS and Linux:
```bash
export FLASK_APP=app.py
```

### Step 7: Run the Flask App
Run the Flask application using the `flask run` command:
```bash
flask run
```

### Step 8: Access the Application
[Access the Flask application in a web browser by navigating to the URL provided in the terminal.
](http://127.0.0.1:5000/delineation)http://127.0.0.1:5000/delineation
