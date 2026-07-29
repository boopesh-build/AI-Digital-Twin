import random

# Initial machine values
temperature = 45.0
rpm = 2000


def get_temperature():
    global temperature

    # Slowly increase or decrease temperature
    change = random.uniform(-0.5, 0.5)

    temperature += change

    # Keep temperature within realistic limits
    temperature = max(30.0, min(80.0, temperature))

    return round(temperature, 1)


def get_rpm():
    global rpm

    # Slowly change RPM
    change = random.randint(-100, 100)

    rpm += change

    # Keep RPM within machine limits
    rpm = max(800, min(3000, rpm))

    return rpm


def get_status():
    return random.choice([
        "Running",
        "Idle",
        "Maintenance"
    ])