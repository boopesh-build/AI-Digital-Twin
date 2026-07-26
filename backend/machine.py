from sensors import get_temperature, get_rpm, get_status
from health import calculate_health


def generate_machine(name):
    """
    Generate a complete digital twin of a machine.
    """

    temperature = get_temperature()
    rpm = get_rpm()
    status = get_status()

    health, condition, maintenance = calculate_health(temperature)

    machine = {
        "name": name,
        "status": status,
        "temperature": temperature,
        "rpm": rpm,
        "health": health,
        "condition": condition,
        "maintenance": maintenance
    }

    return machine