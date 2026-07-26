import random
import time


def generate_machine(name):
    status = random.choice(["Running", "Idle", "Maintenance"])
    temperature = round(random.uniform(35.0, 60.0), 1)
    rpm = random.randint(800, 3000)

    print("=" * 35)
    print(f"Machine     : {name}")
    print(f"Status      : {status}")
    print(f"Temperature : {temperature} °C")
    print(f"RPM         : {rpm}")


while True:
    print("\n" + "=" * 40)
    print("AI DIGITAL TWIN LIVE MONITOR")
    print("=" * 40)

    generate_machine("CNC-01")
    generate_machine("Robot-02")
    generate_machine("Lathe-03")

    time.sleep(2)