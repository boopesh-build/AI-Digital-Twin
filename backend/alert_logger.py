import csv
import os

FILE_NAME = "data/alerts_log.csv"


def log_alert(machine_name, alert):

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Machine",
                "Severity",
                "Type",
                "Message",
                "Value",
                "Timestamp"
            ])

        writer.writerow([
            machine_name,
            alert["severity"],
            alert["type"],
            alert["message"],
            alert["value"],
            alert["timestamp"]
        ])