def show_dashboard(machine):

    print("-" * 40)
    print(f"Machine      : {machine['name']}")
    print(f"Status       : {machine['status']}")
    print(f"Temperature  : {machine['temperature']} °C")
    print(f"RPM          : {machine['rpm']}")
    print(f"Health       : {machine['health']}%")
    print(f"Condition    : {machine['condition']}")
    print(f"Maintenance  : {machine['maintenance']}")