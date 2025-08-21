# Log Analysis Using Machine Learning

This project performs anomaly detection on system log files using machine learning techniques. The script processes raw log data, extracts features, and applies an Isolation Forest model to identify abnormal patterns.

## Overview

- **Log Data Processing:**  
  Load raw system logs, parse timestamps, severity levels, and log messages into a structured format.

- **Feature Engineering:**  
  Convert log levels into numerical scores and compute message lengths for anomaly detection.

- **Anomaly Detection:**  
  Train an **Isolation Forest** model to identify unusual log entries that deviate from normal patterns.

- **Results Visualization:**  
  Flag each log entry as either normal or anomalous and print detected anomalies for further inspection.

## Project Structure
├── README.md                        # Project documentation  
├── ai_log_analysis_script.py        # Python script for log anomaly detection  
├── system_logs.txt                  # Dataset

## Requirements

- Python 3.x
- Libraries:
  - pandas
  - numpy
  - scikit-learn

You can install the required packages with:
pip install -r requirements.txt


<img width="1758" height="446" alt="Screenshot 2025-08-09 143554" src="https://github.com/user-attachments/assets/9f2c85b0-c2f5-45f0-8250-513a429fc1a0" />
