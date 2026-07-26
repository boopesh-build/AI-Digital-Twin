def calculate_health(temperature):
    """
    Calculate the machine health based on temperature.
    Returns:
        health (int)
        condition (str)
        maintenance (str)
    """

    if temperature < 45:
        return 100, "Normal", "Not Required"

    elif temperature < 53:
        return 80, "Warning", "Check Soon"

    else:
        return 50, "Critical", "Required"