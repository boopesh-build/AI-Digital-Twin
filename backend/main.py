import random

print("=" * 40)
print("AI DIGITAL TWIN v0.2".center(40))
print("=" * 40)

machine_name = "CNC-01"
status = random.choice(["Running", "Idle", "Maintenance"])

temperature = round(random.uniform(35.0, 60.0), 1)
rpm = random.randint(1200, 1800)
health = random.randint(90, 100)

print(f"Machine Name : {machine_name}")
print(f"Status       : {status}")
print(f"Temperature  : {temperature}°C")
print(f"RPM          : {rpm}")
print(f"Health       : {health}%")

print("=" * 40)