import streamlit as st
from db import init_db

def update_device():
    st.title("Update Device Memory")
    conn = init_db()

    service_tag = st.text_input("Enter Service Tag to update")
    new_memory = st.text_input("New Memory")

    if st.button("Update"):
        result = conn.execute("UPDATE devices SET memory = ? WHERE service_tag = ?", (new_memory, service_tag))
        if result.rowcount:
            st.success("Device updated.")
        else:
            st.warning("No device found with that service tag.")
