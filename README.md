# Sample Inspection App

## Overview

This desktop application validates inspection sample data against regulatory standards and detects exceeded values.

The application reads CSV files, merges inspection data with standard values, and flags samples that exceed regulatory thresholds.

## Features

* CSV-based data import
* Data merge using a common key
* Automatic exceedance detection
* Simple GUI interface (tkinter)
* macOS desktop application packaging (.app)

## Technologies Used

* Python 3.11
* pandas
* openpyxl
* tkinter
* PyInstaller

## Processing Flow

1. Load sample data (CSV)
2. Load standard reference data (CSV)
3. Merge datasets using a common key
4. Compare measured values against standards
5. Flag exceeded records
6. Output processed results

## How to Run (Development)

```bash
python3 app.py
```

## How to Build macOS App

```bash
pyinstaller --windowed app.py
```

## Project Structure

```
sample-inspection-app/
├── app.py
├── requirements.txt
├── README.md
```

## Author

Jawame

