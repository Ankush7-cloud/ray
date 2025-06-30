import streamlit as st
from db import init_db

def delete_device():
    st.title("Delete Device")
    conn = init_db()

    service_tag = st.text_input("Enter Service Tag to delete")

    if st.button("Delete"):
        result = conn.execute("DELETE FROM devices WHERE service_tag = ?", (service_tag,))
        if result.rowcount:
            st.success("Device deleted.")
        else:
            st.warning("No device found with that service tag.")
