import csv
import os


def show_summary():

    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "..", "data", "machine_log.csv")

    with open(csv_path, "r") as file:
        reader = csv.DictReader(file)

        temperatures = []
        rpms = []
        healths = []
        normal = 0
        warning = 0
        critical = 0
        latest_status = {}
        for row in reader:
            temperatures.append(float(row["Temperature"]))
            rpms.append(int(row["RPM"]))
            healths.append(int(row["Health"]))

            latest_status[row["Machine"]] = row["Condition"]

        normal = 0
        warning = 0
        critical = 0    
        for condition in latest_status.values():
            if condition == "Normal":
                normal += 1
            elif condition == "Warning":
                     warning += 1
            else:
                    critical += 1    

    average_temperature = sum(temperatures) / len(temperatures)
    average_rpm = sum(rpms) / len(rpms)
    average_health = sum(healths) / len(healths)
    print("\n========== DASHBOARD ==========")
    print(f"Average Temperature : {average_temperature:.1f} °C")
    print(f"Average RPM         : {average_rpm:.0f} RPM")
    print(f"Average Health      : {average_health:.0f}%")

    print(f"Machines Normal     : {normal}")
    print(f"Machines Warning    : {warning}")
    print(f"Machines Critical   : {critical}")
    print("===============================\n")