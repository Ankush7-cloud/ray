import streamlit as st
from db import init_db

def insert_device():
    st.title("Insert Device")
    conn = init_db()

    service_tag = st.text_input("Service Tag")
    employee_id = st.text_input("Employee ID")
    device_type = st.selectbox("Device Type", ["GPU", "Desktop"])
    memory = st.text_input("Memory")

    if st.button("Insert"):
        try:
            conn.execute("INSERT INTO devices VALUES (?, ?, ?, ?)", (service_tag, employee_id, device_type, memory))
            st.success("Device inserted successfully.")
        except:
            st.error("Service tag must be unique.")
