import random


def get_temperature():
    """Generate a random machine temperature."""
    return round(random.uniform(35.0, 60.0), 1)


def get_rpm():
    """Generate a random RPM."""
    return random.randint(800, 3000)


def get_status():
    """Generate a random machine status."""
    return random.choice([
        "Running",
        "Idle",
        "Maintenance"
    ])