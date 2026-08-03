def show_dashboard(machine, alerts, prediction):

    print("-" * 50)
    print(f"Machine      : {machine['name']}")
    print(f"Status       : {machine['status']}")
    print(f"Temperature  : {machine['temperature']} °C")
    print(f"RPM          : {machine['rpm']}")
    print(f"Health       : {machine['health']}%")
    print(f"Condition    : {machine['condition']}")
    print(f"Maintenance  : {machine['maintenance']}")

    print("\nAlerts")
    print("\nPrediction")
    print("-" * 50)
    print(f"Remaining Days : {prediction['remaining_days']}")
    print(f"Risk Level     : {prediction['risk']}")
    print(f"Recommendation : {prediction['recommendation']}")
    
    if alerts:
        for alert in alerts:
            print(
                f"[{alert['severity']}] "
                f"{alert['type']} | "
                f"{alert['message']} | "
                f"Value: {alert['value']} | "
                f"Time: {alert['timestamp']}"
            )
    else:
        print("No Active Alerts ✅")