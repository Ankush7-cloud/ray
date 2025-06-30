import streamlit as st
from db import init_db

def signup():
    st.title("Signup")
    conn = init_db()

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    role = st.radio("Select Role", ["admin", "user"])

    if st.button("Sign Up"):
        if password != confirm_password:
            st.error("Passwords do not match.")
        elif not username or not password or not email:
            st.error("All fields are required.")
        else:
            try:
                conn.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (username, email, password, role))
                st.success("Signup successful! Please login.")
            except:
                st.error("Username already exists.")
