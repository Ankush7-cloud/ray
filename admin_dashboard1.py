import streamlit as st
from db import init_db
import pandas as pd

def admin_dashboard():
    st.title("Admin Dashboard - Device Table")
    conn = init_db()

    st.subheader("Device Inventory")
    rows = conn.execute("SELECT * FROM devices").fetchall()
    df = pd.DataFrame(rows, columns=["Service Tag", "Employee ID", "Device Type", "Memory"])
    st.table(df)
