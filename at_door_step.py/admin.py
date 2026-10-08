import streamlit as st
import pandas as pd
from db import get_db_connection

def render_dashboard(user_id):
    st.header("🛠️ System Admin Dashboard")
    
    conn = get_db_connection()
    if not conn:
        st.error("Database connection failed.")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(CASE WHEN is_active=1 THEN 1 END), COUNT(*) FROM customers")
    act_c, tot_c = cursor.fetchone()
    cursor.execute("SELECT COUNT(CASE WHEN is_active=1 THEN 1 END), COUNT(*) FROM dark_stores")
    act_s, tot_s = cursor.fetchone()
    cursor.execute("SELECT COUNT(CASE WHEN is_active=1 THEN 1 END), COUNT(*) FROM delivery_partners")
    act_r, tot_r = cursor.fetchone()
    cursor.close()
    conn.close()

    col1, col2, col3 = st.columns(3)
    col1.metric("Active Customers", f"{act_c} / {tot_c}")
    col2.metric("Dark Stores", f"{act_s} / {tot_s}")
    col3.metric("Riders", f"{act_r} / {tot_r}")

    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs([
        "📦 Product Inventory", 
        "➕ Restock Inventory", 
        "🚫 Deactivate User", 
        "👥 All User Info"
    ])

    with tab1:
        conn = get_db_connection()
        df = pd.read_sql("SELECT product_id, sku_code, product_name, unit_price, stock_quantity FROM inventory", conn)
        conn.close()
        st.dataframe(df, use_container_width=True)

    with tab2:
        with st.form("restock_form"):
            p_id = st.number_input("Product ID", min_value=1, step=1)
            qty = st.number_input("Additional Quantity", min_value=1, step=1)
            submitted = st.form_submit_button("Restock Product")
            if submitted:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE inventory SET stock_quantity = stock_quantity + %s WHERE product_id = %s", (qty, p_id))
                conn.commit()
                cursor.close()
                conn.close()
                st.success("Inventory stock updated successfully!")

    with tab3:
        with st.form("deactivate_form"):
            u_id = st.number_input("User ID to Deactivate", min_value=1, step=1)
            deact_submitted = st.form_submit_button("Soft-Deactivate User")
            if deact_submitted:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET is_active = 0 WHERE user_id = %s", (u_id,))
                conn.commit()
                cursor.close()
                conn.close()
                st.success(f"User account {u_id} soft-deactivated.")

    with tab4:
        conn = get_db_connection()
        df_users = pd.read_sql("SELECT customer_id, user_id, store_id, partner_id, full_name, phone, delivery_addr, is_active FROM customers", conn)
        conn.close()
        st.dataframe(df_users, use_container_width=True)