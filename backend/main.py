from machine import generate_machine
from display import show_dashboard
from logger import log_machine
from analytics import generate_temperature_graph
import time

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
        show_dashboard(machine)
        log_machine(machine)
    generate_temperature_graph()   
    time.sleep(2)