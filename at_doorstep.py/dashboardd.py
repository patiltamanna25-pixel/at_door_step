import streamlit as st
from db import get_db_connection
conn = st.connection("mysql", type="sql")
cursor=conn.cursor()
import sys

# Optional: Set page configuration
st.set_page_config(
    page_title="At Doorstep",
    page_icon="🛍️",
    layout="centered"
)

# Application Header
st.title("🛍️ AT DOORSTEP")
st.subheader("Quick Commerce Platform")
st.divider()

# Sidebar Navigation (replaces the terminal options 1, 2, 3)
st.sidebar.title("Navigation Menu")
choice = st.sidebar.radio(
    "Choose an option:",
    ["Existing User Login", "New Customer Sign-Up", "Exit Platform"]
)

# Option 1: Existing User Login
if choice == "Existing User Login":
    st.header("🔑 Customer Login")
    
    with st.form("login_form"):
        username = st.text_input("Username / Email")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")
        if submit_button:
            cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
                        print("\n[ERROR] Username already taken. Please choose another one.")
        
        
        if submit_button:
            if username and password:
                # Integrate your actual login check function here
                # Example: auth.login_customer(username, password)
                st.success(f"Welcome back, {username}!")
            else:
                st.error("Please enter both username and password.")

# Option 2: New Customer Sign-Up
elif choice == "New Customer Sign-Up":
    st.header("📝 Register New Account")
    
    with st.form("signup_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
        signup_button = st.form_submit_button("Sign Up")
        
        if signup_button:
            if full_name and email and password:
                # Integrate your actual registration function here
                # Example: auth.register_customer(full_name, email, phone, password)
                st.success("Account created successfully! You can now log in.")
            else:
                st.error("Please fill in all required fields.")

# Option 3: Exit Platform
elif choice == "Exit Platform":
    st.info("Thank you for using At Doorstep Quick Commerce Platform!")
    st.stop()
# import hashlib
# import streamlit as st
# from db import get_db_connection

# # Function to hash passwords using Python's built-in hashlib
# def hash_pass(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# def authenticate_user(username, password):
#     conn = get_db_connection()
#     if not conn:
#         st.error("Database connection failed.")
#         return None

#     cursor = conn.cursor(dictionary=True)
#     try:
#         query = "SELECT * FROM users WHERE username = %s AND password_hash = %s AND is_active = 1"
#         cursor.execute(query, (username, hash_pass(password)))
#         return cursor.fetchone()
#     finally:
#         cursor.close()
#         conn.close()

# def register_customer(username, password, full_name, phone, delivery_addr):
#     conn = get_db_connection()
#     if not conn:
#         return False, "Database connection failed."

#     cursor = conn.cursor(dictionary=True)
#     try:
#         # Check if username exists
#         cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
#         if cursor.fetchone():
#             return False, "Username already taken."

#         # Insert into users
#         user_query = """
#             INSERT INTO users (username, password_hash, role, is_active, created_at)
#             VALUES (%s, %s, 'CUSTOMER', 1, CURDATE())
#         """
#         cursor.execute(user_query, (username, hash_pass(password)))
#         new_user_id = cursor.lastrowid

#         # Insert into customers
#         cust_query = """
#             INSERT INTO customers (user_id, store_id, partner_id, full_name, phone, delivery_addr, is_active)
#             VALUES (%s, 1, 1, %s, %s, %s, 1)
#         """
#         cursor.execute(cust_query, (new_user_id, full_name, phone, delivery_addr))

#         conn.commit()
#         return True, "Account created successfully!"
#     except Exception as e:
#         conn.rollback()
#         return False, f"Registration failed: {e}"
#     finally:
#         cursor.close()
#         conn.close()


# # --- STREAMLIT APP ---

# st.title("Customer Portal")

# if "user" not in st.session_state:
#     st.session_state.user = None

# # If logged in
# if st.session_state.user:
#     st.write(f"### Welcome, {st.session_state.user['username']}!")
#     if st.button("Logout"):
#         st.session_state.user = None
#         st.rerun()

# # If logged out
# else:
#     tab1, tab2 = st.tabs(["Login", "Register"])

#     with tab1:
#         st.subheader("Login")
#         username = st.text_input("Username", key="login_user").strip()
#         password = st.text_input("Password", type="password", key="login_pass").strip()
        
#         if st.button("Login"):
#             if username and password:
#                 user = authenticate_user(username, password)
#                 if user:
#                     st.session_state.user = user
#                     st.success("Login successful!")
#                     st.rerun()
#                 else:
#                     st.error("Invalid credentials.")
#             else:
#                 st.warning("Please fill all fields.")

#     with tab2:
#         st.subheader("Register")
#         reg_username = st.text_input("Username", key="reg_user").strip()
#         reg_password = st.text_input("Password", type="password", key="reg_pass").strip()
#         reg_full_name = st.text_input("Full Name").strip()
#         reg_phone = st.text_input("Phone Number").strip()
#         reg_address = st.text_area("Delivery Address").strip()

#         if st.button("Register"):
#             if reg_username and reg_password and reg_full_name:
#                 ok, msg = register_customer(reg_username, reg_password, reg_full_name, reg_phone, reg_address)
#                 if ok:
#                     st.success(msg)
#                 else:
#                     st.error(msg)
#             else:
#                 st.warning("Username, Password, and Full Name are required.")


