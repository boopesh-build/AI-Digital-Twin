from machine import generate_machine
import time


def display_machine(machine):
    print("-" * 40)
    print(f"Machine      : {machine['name']}")
    print(f"Status       : {machine['status']}")
    print(f"Temperature  : {machine['temperature']} °C")
    print(f"RPM          : {machine['rpm']}")
    print(f"Health       : {machine['health']}%")
    print(f"Condition    : {machine['condition']}")
    print(f"Maintenance  : {machine['maintenance']}")


machines = [
    "CNC-01",
    "Robot-02",
    "Lathe-03"
]


while True:

    print("\n" + "=" * 45)
    print("AI DIGITAL TWIN MONITOR")
    print("=" * 45)

    for machine_name in machines:
        machine = generate_machine(machine_name)
        display_machine(machine)

    time.sleep(2)