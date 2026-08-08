import streamlit as st
import pandas as pd

from backend.machine import generate_machine
from backend.alerts import check_alerts
from backend.alert_logger import log_alert
from backend.predictor import predict_maintenance


st.set_page_config(
    page_title="AI Digital Twin",
    page_icon="⚙️",
    layout="wide"
)


st.title("⚙️ AI Digital Twin")
st.subheader("Industrial Machine Monitoring System")


machines = [
    "CNC-01",
    "Robot-02",
    "Lathe-03"
]


# Refresh button

if st.button("🔄 Refresh Machine Data"):
    st.rerun()


# Generate current machine data

machine_data = []
current_alerts = []
predictions = []

for machine_name in machines:

    machine = generate_machine(machine_name)

    prediction = predict_maintenance(machine)

    alerts = check_alerts(machine)

    for alert in alerts:
        log_alert(machine["name"], alert)

    machine_data.append(machine)

    predictions.append({
        "machine": machine["name"],
        "prediction": prediction
    })

    for alert in alerts:

        alert_with_machine = alert.copy()
        alert_with_machine["machine"] = machine["name"]

        current_alerts.append(alert_with_machine)


# --------------------------------------------------
# MACHINE OVERVIEW
# --------------------------------------------------

st.write("### Machine Overview")


columns = st.columns(3)


for column, machine in zip(columns, machine_data):

    with column:

        st.markdown(f"## ⚙️ {machine['name']}")

        st.metric(
            "Temperature",
            f"{machine['temperature']} °C"
        )

        st.metric(
            "RPM",
            machine["rpm"]
        )

        st.markdown("**Machine Health**")

        health = machine["health"]

        st.progress(
            health / 100
        )

        st.write(f"**{health}%**")

        st.write(
            f"**Status:** {machine['status']}"
        )

        st.write(
            f"**Condition:** {machine['condition']}"
        )

        st.write(
            f"**Maintenance:** {machine['maintenance']}"
        )


# --------------------------------------------------
# ALERT CENTER
# --------------------------------------------------

st.divider()

st.header("🚨 Alert Center")


if current_alerts:

    st.write(
        f"Active alerts: **{len(current_alerts)}**"
    )

    for alert in current_alerts:

        severity = alert["severity"]

        if severity == "HIGH":

            st.error(
                f"🔴 {alert['machine']} — "
                f"{alert['message']} | "
                f"Value: {alert['value']} | "
                f"Time: {alert['timestamp']}"
            )

        elif severity == "MEDIUM":

            st.warning(
                f"🟠 {alert['machine']} — "
                f"{alert['message']} | "
                f"Value: {alert['value']} | "
                f"Time: {alert['timestamp']}"
            )

        else:

            st.info(
                f"🟡 {alert['machine']} — "
                f"{alert['message']} | "
                f"Value: {alert['value']} | "
                f"Time: {alert['timestamp']}"
            )

else:

    st.success(
        "✅ No active alerts. All machines are operating normally."
    )


# --------------------------------------------------
# PREDICTIVE MAINTENANCE
# --------------------------------------------------

st.divider()

st.header("🔧 Predictive Maintenance")


for item in predictions:

    machine_name = item["machine"]
    prediction = item["prediction"]

    st.subheader(f"⚙️ {machine_name}")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Remaining Maintenance",
            f"{prediction['remaining_days']} days"
        )

    with col2:

        st.metric(
            "Risk Level",
            prediction["risk"]
        )

    with col3:

        st.write("**Recommendation**")

        st.write(
            prediction["recommendation"]
        )
        

# --------------------------------------------------
# HISTORICAL ANALYTICS
# --------------------------------------------------

st.divider()

st.header("📊 Historical Analytics")


csv_path = "data/machine_log.csv"


try:

    data = pd.read_csv(csv_path)

    st.write(
        f"Total recorded readings: **{len(data)}**"
    )


    # Temperature history

    temperature_data = data[
        ["Machine", "Temperature"]
    ]


    temperature_chart = temperature_data.pivot(
        columns="Machine",
        values="Temperature"
    )


    st.subheader("🌡️ Temperature History")


    st.line_chart(
        temperature_chart
    )


except FileNotFoundError:

    st.warning(
        "Machine history file not found."
    )