import streamlit as st
from db import init_db

def update_device():
    st.title("Update Device Info")
    conn = init_db()

    service_tag = st.text_input("Enter Service Tag to update")
    new_employee_id = st.text_input("New Employee ID")
    new_memory = st.text_input("New Memory")
    new_device_type = st.selectbox("New Device Type", ["GPU", "Desktop"])

    if st.button("Update"):
        result = conn.execute("""
            UPDATE devices
            SET employee_id = ?, memory = ?, device_type = ?
            WHERE service_tag = ?
        """, (new_employee_id, new_memory, new_device_type, service_tag))

        if result.rowcount:
            st.success("Device updated successfully.")
        else:
            st.warning("No device found with that service tag.")
