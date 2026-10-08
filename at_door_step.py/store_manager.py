import streamlit as st
import pandas as pd
from db import get_db_connection

def render_dashboard(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dark_stores WHERE user_id = %s", (user_id,))
    hub = cursor.fetchone()
    cursor.close()
    conn.close()

    st.header(f"🏬 Dark Store Manager - {hub['hub_name']}")

    tab1, tab2 = st.tabs(["🚴 Assigned Delivery Riders", "⚠️ Low Stock Alerts"])

    with tab1:
        conn = get_db_connection()
        df_riders = pd.read_sql(f"SELECT partner_id, full_name, phone, daily_target, is_active FROM delivery_partners WHERE store_id = {hub['store_id']}", conn)
        conn.close()
        st.dataframe(df_riders, use_container_width=True)

    with tab2:
        conn = get_db_connection()
        df_alerts = pd.read_sql("SELECT product_name, stock_quantity, reorder_level FROM inventory WHERE stock_quantity <= reorder_level", conn)
        conn.close()
        if df_alerts.empty:
            st.info("No low-stock alerts at this time.")
        else:
            st.warning("Low stock items detected:")
            st.dataframe(df_alerts, use_container_width=True)