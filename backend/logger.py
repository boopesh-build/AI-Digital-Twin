from datetime import datetime
import os
import csv


def log_machine(machine):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Path to the data folder
    base_dir = os.path.dirname(__file__)
    log_path = os.path.join(base_dir, "..", "data", "machine_log.csv")
    file_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Machine",
                "Status",
                "Temperature",
                "RPM",
                "Health",
                "Condition",
                "Maintenance"
            ])
        writer.writerow([
            current_time,
            machine["name"],
            machine["status"],
            machine["temperature"],
            machine["rpm"],
            machine["health"],
            machine["condition"],
            machine["maintenance"]
        ])