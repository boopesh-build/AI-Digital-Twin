import csv
import os
import matplotlib.pyplot as plt

def generate_temperature_graph():

    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "..", "data", "machine_log.csv")

    cnc_temp = []
    robot_temp = []
    lathe_temp = []

    with open(csv_path, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Machine"] == "CNC-01":
                cnc_temp.append(float(row["Temperature"]))

            elif row["Machine"] == "Robot-02":
                robot_temp.append(float(row["Temperature"]))

            elif row["Machine"] == "Lathe-03":
                  lathe_temp.append(float(row["Temperature"]))

    plt.figure(figsize=(10, 5))

    plt.plot(cnc_temp, marker="o", label="CNC-01")
    plt.plot(robot_temp, marker="s", label="Robot-02")
    plt.plot(lathe_temp, marker="^", label="Lathe-03")

    plt.title("Machine Temperature")

    plt.xlabel("Reading Number")

    plt.ylabel("Temperature (°C)")
    plt.legend()

    plt.grid(True)

    graph_path = os.path.join(base_dir, "..", "data", "graphs", "temperature.png")

    plt.savefig(graph_path)

    print("Temperature graph updated.")

    plt.close()