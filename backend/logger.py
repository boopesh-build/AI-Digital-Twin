from datetime import datetime
import os


def log_machine(machine):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Path to the data folder
    base_dir = os.path.dirname(__file__)
    log_path = os.path.join(base_dir, "..", "data", "machine_log.txt")

    log_entry = (
        f"{current_time} | "
        f"{machine['name']} | "
        f"{machine['status']} | "
        f"{machine['temperature']}°C | "
        f"{machine['rpm']} RPM | "
        f"{machine['health']}% | "
        f"{machine['condition']} | "
        f"{machine['maintenance']}\n"
    )

    with open(log_path, "a") as file:
        file.write(log_entry)