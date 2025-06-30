import streamlit as st
from signup import signup
from login import login2
from home import home
from admin_dashboard import admin_dashboard
from user_management import user_management
from resource_management import resource_management
from insert_device import insert_device
from delete_device import delete_device
from update_device import update_device

st.set_page_config(page_title="Device Management App", layout="wide")

if "username" not in st.session_state:
    st.session_state["username"] = None
    st.session_state["role"] = None
    st.session_state["page"] = "Home"

if st.session_state["username"]:
    st.sidebar.markdown(f"👤 Logged in as: {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.experimental_rerun()

    role = st.session_state["role"]
    if role == "admin":
        menu = st.sidebar.selectbox("Admin Menu", [
            "Dashboard",
            "Insert Device",
            "Delete Device",
            "Update Device",
            "User Management",
            "Resource Management"
        ])
        st.session_state["page"] = menu
    else:
        menu = st.sidebar.selectbox("User Menu", [
            "User Management",
            "Resource Management"
        ])
        st.session_state["page"] = menu
else:
    menu = st.sidebar.selectbox("Menu", ["Home", "Signup", "Login"])
    st.session_state["page"] = menu

# Page Routing
page = st.session_state["page"]

if page == "Home":
    home()
elif page == "Signup":
    signup()
elif page == "Login":
    login()
elif page == "Dashboard":
    admin_dashboard()
elif page == "Insert Device":
    insert_device()
elif page == "Delete Device":
    delete_device()
elif page == "Update Device":
    update_device()
elif page == "User Management":
    user_management()
elif page == "Resource Management":
    resource_management()
