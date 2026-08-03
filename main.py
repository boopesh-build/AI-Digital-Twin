from backend.machine import generate_machine
from backend.logger import log_machine
from backend.analytics import generate_temperature_graph
from backend.alerts import check_alerts
from backend.alert_logger import log_alert
from backend.predictor import predict_maintenance

from ui.display import show_dashboard
from ui.dashboard import show_summary

import time


machines = [
    "CNC-01",
    "Robot-02",
    "Lathe-03"
]


while True:

    print("\n" + "=" * 45)
    print("AI DIGITAL TWIN MONITOR")
    print("=" * 45)

    for machine_name in machines:

        # Generate machine data
        machine = generate_machine(machine_name)

        # Check alerts
        alerts = check_alerts(machine)

        prediction = predict_maintenance(machine)

        # Save alerts
        for alert in alerts:
            log_alert(machine["name"], alert)

        # Display dashboard
        show_dashboard(machine, alerts, prediction)

        # Save machine data
        log_machine(machine)

    # Generate analytics
    generate_temperature_graph()


    # Display summary
    show_summary()

    time.sleep(2)