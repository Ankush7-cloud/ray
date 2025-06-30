import streamlit as st
from db import init_db

def admin_dashboard():
    st.title("Admin Dashboard - Device Table")
    conn = init_db()

    st.subheader("Device Inventory")
    rows = conn.execute("SELECT * FROM devices").fetchall()
    st.table(rows)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Insert"):
            st.session_state["page"] = "Insert Device"
    with col2:
        if st.button("❌ Delete"):
            st.session_state["page"] = "Delete Device"
    with col3:
        if st.button("✏ Update"):
            st.session_state["page"] = "Update Device"
