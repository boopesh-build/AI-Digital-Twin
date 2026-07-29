import csv
import os
import matplotlib.pyplot as plt

def generate_temperature_graph():

    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "..", "data", "machine_log.csv")

    temperatures = []

    with open(csv_path, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            temperatures.append(float(row["Temperature"]))

    plt.figure(figsize=(10, 5))

    plt.plot(temperatures)

    plt.title("Machine Temperature")

    plt.xlabel("Reading Number")

    plt.ylabel("Temperature (°C)")

    plt.grid(True)

    graph_path = os.path.join(base_dir, "..", "data", "graphs", "temperature.png")

    plt.savefig(graph_path)

    print("Temperature graph updated.")

    plt.close()