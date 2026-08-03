from datetime import datetime


def check_alerts(machine):
    """
    Analyze machine data and return structured alerts.
    """

    alerts = []
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Temperature Alerts
    if machine["temperature"] >= 75:
        alerts.append({
            "severity": "HIGH",
            "type": "TEMPERATURE",
            "message": "High Temperature",
            "value": machine["temperature"],
            "timestamp": timestamp
        })

    elif machine["temperature"] >= 65:
        alerts.append({
            "severity": "MEDIUM",
            "type": "TEMPERATURE",
            "message": "Temperature Rising",
            "value": machine["temperature"],
            "timestamp": timestamp
        })

    # RPM Alerts
    if machine["rpm"] == 0:
        alerts.append({
            "severity": "HIGH",
            "type": "RPM",
            "message": "Machine Stopped",
            "value": machine["rpm"],
            "timestamp": timestamp
        })

    elif machine["rpm"] < 500:
        alerts.append({
            "severity": "LOW",
            "type": "RPM",
            "message": "Low RPM",
            "value": machine["rpm"],
            "timestamp": timestamp
        })

    # Health Alerts
    if machine["health"] < 50:
        alerts.append({
            "severity": "HIGH",
            "type": "HEALTH",
            "message": "Critical Health",
            "value": machine["health"],
            "timestamp": timestamp
        })

    elif machine["health"] < 70:
        alerts.append({
            "severity": "MEDIUM",
            "type": "HEALTH",
            "message": "Health Dropping",
            "value": machine["health"],
            "timestamp": timestamp
        })

    return alerts