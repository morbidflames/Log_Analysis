import pandas as pd
from collections import Counter
import re

# Read log file
log_file = "system_logs.txt"

log_entries = []
with open(log_file, "r") as file:     # Open file in read only mode
    for line in file:
        match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)", line.strip())
        if match:
            timestamp, level, message = match.groups()
            log_entries.append([timestamp, level, message])

# Converting the log_entries into a DataFrame
df = pd.DataFrame(log_entries, columns=["timestamp", "level", "message"])
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Counting the errors in the last 30s
error_counts = Counter(df[df["level"] == "ERROR"]["timestamp"].dt.floor("30S"))

# Allocating a suitable threshold for detecting an anamoly
threshold = 3

# Detecting spikes in error 
for time, count in error_counts.items():
    if count > threshold:
        print(f"⚠️ Anomaly detected! Spike of {count} ERROR logs in the last 30 seconds at {time}")

# Showing anamolies with the logs
print("\nFull Log Analysis:")
print(df)