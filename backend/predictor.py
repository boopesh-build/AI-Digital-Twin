def predict_maintenance(machine):
    """
    Predict remaining maintenance days based on machine health.
    """

    health = machine["health"]

    if health >= 90:
        return {
            "remaining_days": 30,
            "risk": "LOW",
            "recommendation": "Machine is in excellent condition."
        }

    elif health >= 75:
        return {
            "remaining_days": 20,
            "risk": "LOW",
            "recommendation": "Continue normal monitoring."
        }

    elif health >= 60:
        return {
            "remaining_days": 10,
            "risk": "MEDIUM",
            "recommendation": "Schedule maintenance soon."
        }

    elif health >= 40:
        return {
            "remaining_days": 5,
            "risk": "HIGH",
            "recommendation": "Maintenance required immediately."
        }

    else:
        return {
            "remaining_days": 1,
            "risk": "CRITICAL",
            "recommendation": "Stop the machine and inspect it."
        }