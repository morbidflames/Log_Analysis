import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

# Reading the dataset
log_file_path = "system_logs.txt"
with open(log_file_path, "r") as file:
    logs = file.readlines()

# Structuring the logs into a DataFrame
data = []
for log in logs:
    parts = log.strip().split(" ", 3)
    if len(parts) < 4:
        continue
    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = parts[3]
    data.append([timestamp, level, message])

df = pd.DataFrame(data, columns=["timestamp", "level", "message"])

# Converting timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# Training the model
# Assigning numerical values to log levels for anomaly detection
level_mapping = {
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3,
    "CRITICAL": 4
}
df["level_score"] = df['level'].map(level_mapping)

# Feature engineering message length
df["message_length"] = df["message"].apply(len)

#Isolation Forest for anomaly detection
model = IsolationForest(contamination=0.1, random_state=42) # using 10% contamination for anomalies
df["anomaly"] = model.fit_predict(df[["level_score", "message_length"]])

# Converting to readable format
df['is_anomaly'] = df["anomaly"].apply(lambda x: "😵 Anamoly" if x == -1 else "✔️ Normal")

# Printing the detected anamoly
anomalies = df[df["is_anomaly"] == "😵 Anamoly"]
print("\n Detected Anomalies: \n", anomalies)