import streamlit as st
from db import init_db

def signup():
    st.title("Signup")
    conn = init_db()

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.radio("Select Role", ["admin", "user"])

    if st.button("Sign Up"):
        try:
            conn.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (username, email, password, role))
            st.success("Signup successful! Please login.")
        except:
            st.error("Username already exists.")
