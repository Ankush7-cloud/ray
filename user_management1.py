import streamlit as st
from db import init_db
import pandas as pd

def user_management():
    st.title("User Management")
    conn = init_db()

    role = st.session_state.get("role")
    if role == "admin":
        users = conn.execute("SELECT username, email, role FROM users").fetchall()
    else:
        users = conn.execute("SELECT username, email, role FROM users WHERE role = 'user'").fetchall()

    df = pd.DataFrame(users, columns=["Username", "Email ID", "User"])
    st.table(df)
