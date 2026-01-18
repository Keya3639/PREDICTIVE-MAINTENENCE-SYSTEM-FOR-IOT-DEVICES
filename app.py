import streamlit as st
import numpy as np
import pandas as pd
import joblib
import plotly.graph_objects as go

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Predictive Maintenance System",
    page_icon="🛠️",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("models/pmd_model.pkl")

model = load_model()

# -----------------------------
# App Title
# -----------------------------
st.title("🛠️ Predictive Maintenance System for IoT Devices")
st.markdown(
    "Predict **machine failure in advance** using IoT sensor data."
)
st.divider()

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("🔧 Machine Sensor Inputs")

machine_id = st.sidebar.selectbox(
    "Machine ID", options=[0, 1, 2], key="machine_id"
)

vibration = st.sidebar.slider(
    "Vibration", 0.0, 2.0, 0.8, key="vibration"
)
acoustic = st.sidebar.slider(
    "Acoustic", 0.0, 1.5, 0.6, key="acoustic"
)
temperature = st.sidebar.slider(
    "Temperature (°C)", 20.0, 100.0, 65.0, key="temperature"
)
current = st.sidebar.slider(
    "Current (A)", 5.0, 20.0, 12.0, key="current"
)
hour = st.sidebar.slider("Hour", 0, 23, 10, key="hour")
minute = st.sidebar.slider("Minute", 0, 59, 30, key="minute")

# -----------------------------
# Input Vector
# -----------------------------
input_data = np.array([[
    machine_id,
    vibration,
    acoustic,
    temperature,
    current,
    hour,
    minute
]])

feature_names = [
    "machine_id",
    "vibration",
    "acoustic",
    "temperature",
    "current",
    "hour",
    "minute"
]

input_df = pd.DataFrame(input_data, columns=feature_names)

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Predict Failure Risk", key="predict_button"):

    # Predict probability
    probability = model.predict_proba(input_df)[0][1]

    # -----------------------------
    # Risk Level Indicator
    # -----------------------------
    if probability < 0.3:
        risk_level = "🟢 NORMAL"
        color = "green"
    elif probability < 0.6:
        risk_level = "🟡 WARNING"
        color = "orange"
    else:
        risk_level = "🔴 FAILURE LIKELY"
        color = "red"

    st.markdown(
        f"""
        <div style="
            padding: 15px;
            border-radius: 10px;
            background-color: {color};
            color: white;
            font-size: 20px;
            font-weight: bold;
            text-align: center;">
            Risk Level: {risk_level}
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------
    # Failure Probability Gauge
    # -----------------------------
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        title={"text": "Failure Probability (%)"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "darkblue"},
            "steps": [
                {"range": [0, 30], "color": "green"},
                {"range": [30, 60], "color": "yellow"},
                {"range": [60, 100], "color": "red"},
            ],
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # Numeric Probability (No key)
    # -----------------------------
    st.metric(
        label="Failure Probability",
        value=f"{probability:.2%}"
    )

    st.caption(
        "Prediction based on multi-sensor IoT data and trained ML model"
    )
st.markdown("---")
st.markdown("Developed by **Keya Das** | Predictive Maintenance System for IoT Devices")