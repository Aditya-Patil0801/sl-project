import streamlit as st
import serial
import pandas as pd
from datetime import datetime
import time
import mysql.connector   # 🔥 NEW

# Config
PORT = 'COM5'
BAUD = 9600

# 🔥 MySQL INSERT FUNCTION
def insert_data(air, co, temp, hum):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aditya@369",   
            database="air_quality"
        )

        cursor = conn.cursor()

        query = """
        INSERT INTO sensor_data (time, air, co, temp, humidity)
        VALUES (NOW(), %s, %s, %s, %s)
        """

        cursor.execute(query, (air, co, temp, hum))
        conn.commit()

        cursor.close()
        conn.close()

    except Exception as e:
        print("DB Error:", e)

# Serial connection
@st.cache_resource
def get_serial():
    return serial.Serial(PORT, BAUD, timeout=1)

try:
    ser = get_serial()
except:
    st.error("⚠️ Could not connect to Arduino (Check COM port / close Serial Monitor)")
    st.stop()

# Session state
if "data" not in st.session_state:
    st.session_state.data = []

# UI
st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

st.title("🌍 Smart Air Quality Monitoring System")
st.markdown("### Real-time Environmental Monitoring Dashboard")

# Reset button
if st.button("🔄 Reset Data"):
    st.session_state.data.clear()

# Read data from Arduino
line = ser.readline().decode('utf-8').strip()

if line:
    values = line.split(',')

    if len(values) == 4:
        try:
            air = int(values[0])
            co = int(values[1])
            temp = float(values[2])
            hum = float(values[3])

            record = {
                "Time": datetime.now().strftime("%H:%M:%S"),
                "Air": air,
                "CO": co,
                "Temp": temp,
                "Humidity": hum
            }

            # Store locally
            st.session_state.data.append(record)

            # 🔥 STORE IN DATABASE
            insert_data(air, co, temp, hum)

        except:
            pass

# Convert to DataFrame
df = pd.DataFrame(st.session_state.data)

# Layout
col1, col2, col3, col4 = st.columns(4)

if not df.empty:
    latest = df.iloc[-1]

    col1.metric("Air Quality", latest["Air"])
    col2.metric("CO Level", latest["CO"])
    col3.metric("Temperature (°C)", latest["Temp"])
    col4.metric("Humidity (%)", latest["Humidity"])

    # Status
    st.subheader("Air Quality Status")
    if latest["Air"] < 200:
        st.success("🟢 Good")
    elif latest["Air"] < 400:
        st.warning("🟡 Moderate")
    else:
        st.error("🔴 Dangerous")

    # Alerts
    st.subheader("🚨 Alerts")
    if latest["Air"] > 400:
        st.error("⚠️ Dangerous Air Quality!")
    if latest["CO"] > 300:
        st.warning("⚠️ High CO Level!")

    # Graph
    st.subheader("📊 Live Graph")
    st.line_chart(df[["Air", "CO", "Temp", "Humidity"]])

    # Table
    st.subheader("📂 All Data")
    st.dataframe(df, height=400)

    # Download CSV
    st.download_button(
        label="📥 Download CSV",
        data=df.to_csv(index=False),
        file_name="sensor_data.csv",
        mime="text/csv"
    )

# Auto refresh
time.sleep(3)
st.rerun()