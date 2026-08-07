import streamlit as st
import pandas as pd

from backend.machine import generate_machine


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

for machine_name in machines:

    machine = generate_machine(machine_name)
    machine_data.append(machine)


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