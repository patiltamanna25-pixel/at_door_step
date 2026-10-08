import streamlit as st
import auth
import admin
import store_manager
import delivery_partner
import customer

st.set_page_config(page_title="At Doorstep Quick Commerce", page_icon="🛍️", layout="wide")

# Initialize session states
if "user" not in st.session_state:
    st.session_state.user = None

def logout():
    st.session_state.user = None
    st.rerun()

st.title("🛍️ At Doorstep - Quick Commerce Platform")

if st.session_state.user is None:
    tab1, tab2 = st.tabs(["🔑 Login", "📝 Register New Customer"])

    with tab1:
        st.subheader("Existing User Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login", type="primary"):
            user = auth.authenticate_user(username, password)
            if user:
                st.session_state.user = user
                st.success(f"Welcome, {user['username']}!")
                st.rerun()
            else:
                st.error("Invalid credentials or inactive account.")

    with tab2:
        st.subheader("New Customer Sign-Up")
        reg_username = st.text_input("New Username", key="reg_user")
        reg_password = st.text_input("New Password", type="password", key="reg_pass")
        reg_name = st.text_input("Full Name")
        reg_phone = st.text_input("Phone Number")
        reg_addr = st.text_area("Delivery Address")
        
        if st.button("Register Account"):
            if not all([reg_username, reg_password, reg_name, reg_phone, reg_addr]):
                st.warning("Please fill out all fields.")
            else:
                success, msg = auth.register_customer(reg_username, reg_password, reg_name, reg_phone, reg_addr)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
else:
    user = st.session_state.user
    st.sidebar.markdown(f"**Logged in as:** {user['username']}")
    st.sidebar.markdown(f"**Role:** `{user['role']}`")
    if st.sidebar.button("Logout"):
        logout()

    role = user['role']
    if role == 'ADMIN':
        admin.render_dashboard(user['user_id'])
    elif role == 'STORE_MANAGER':
        store_manager.render_dashboard(user['user_id'])
    elif role == 'DELIVERY_PARTNER':
        delivery_partner.render_dashboard(user['user_id'])
    elif role == 'CUSTOMER':
        customer.render_dashboard(user['user_id'])