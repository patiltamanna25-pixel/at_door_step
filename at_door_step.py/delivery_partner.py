import streamlit as st
import pandas as pd
from db import get_db_connection

def render_dashboard(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM delivery_partners WHERE user_id = %s", (user_id,))
    rider = cursor.fetchone()
    cursor.close()
    conn.close()

    st.header(f"🚴 Delivery Partner Portal - {rider['full_name']}")

    tab1, tab2 = st.tabs(["📦 Assigned Deliveries", "💵 Update Order & Collect Payment"])

    with tab1:
        conn = get_db_connection()
        df_orders = pd.read_sql(f"SELECT order_id, order_number, total_amount, paid_amount, order_status, payment_status FROM orders WHERE partner_id = {rider['partner_id']}", conn)
        conn.close()
        st.dataframe(df_orders, use_container_width=True)

    with tab2:
        with st.form("deliver_form"):
            o_id = st.number_input("Order ID", min_value=1, step=1)
            amt = st.number_input("Amount Collected (Rs.)", min_value=0.0, step=10.0)
            submitted = st.form_submit_button("Mark as Delivered")

            if submitted:
                conn = get_db_connection()
                cursor = conn.cursor()
                query = """
                    UPDATE orders 
                    SET paid_amount = paid_amount + %s,
                        order_status = 'DELIVERED',
                        payment_status = CASE WHEN (paid_amount + %s) >= total_amount THEN 'PAID' ELSE 'PARTIAL' END
                    WHERE order_id = %s
                """
                cursor.execute(query, (amt, amt, o_id))
                conn.commit()
                cursor.close()
                conn.close()
                st.success("Order marked as delivered and payment recorded!")