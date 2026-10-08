import streamlit as st
import pandas as pd
import datetime
from db import get_db_connection

def render_dashboard(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers WHERE user_id = %s", (user_id,))
    cust = cursor.fetchone()
    cursor.close()
    conn.close()

    st.header(f"🛒 Welcome, {cust['full_name']}!")

    tab1, tab2, tab3 = st.tabs(["📋 Browse","Place Order","📜 Order History"])

    with tab1:
        conn = get_db_connection()
        df_prods = pd.read_sql("SELECT product_id, product_name, unit_price, stock_quantity FROM inventory", conn)
        conn.close()
        
        st.subheader("Available Products")
        st.dataframe(df_prods, use_container_width=True)

        st.subheader("Place Instant Order")
        with st.form("order_form"):
            p_id = st.number_input("Enter Product ID to Order", min_value=1, step=1)
            qty = st.number_input("Enter Quantity", min_value=1, step=1)
            order_btn = st.form_submit_button("Place Order")

            if order_btn:
                conn = get_db_connection()
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT product_name, unit_price, stock_quantity FROM inventory WHERE product_id = %s", (p_id,))
                prod = cursor.fetchone()

                if prod and prod['stock_quantity'] >= qty:
                    total_cost = float(prod['unit_price']) * qty
                    order_no = f"ORD-2026-{datetime.datetime.now().strftime('%M%S')}"
                    today = datetime.date.today().strftime('%Y-%m-%d')

                    cursor.execute(
                        "INSERT INTO orders (order_number, customer_id, partner_id, total_amount, paid_amount, order_status, payment_status, order_date) VALUES (%s, %s, %s, %s, 0.00, 'PENDING', 'UNPAID', %s)",
                        (order_no, cust['customer_id'], cust['partner_id'], total_cost, today)
                    )
                    cursor.execute("UPDATE inventory SET stock_quantity = stock_quantity - %s WHERE product_id = %s", (qty, p_id))
                    conn.commit()
                    st.success(f"Order {order_no} placed successfully! Total: Rs.{total_cost:.2f}")
                else:
                    st.error("Order failed: Insufficient stock available or invalid Product ID.")
                
                cursor.close()
                conn.close()

    with tab2:
        conn = get_db_connection()
        df_history = pd.read_sql(f"SELECT order_number, total_amount, paid_amount, order_status, payment_status FROM orders WHERE customer_id = {cust['customer_id']}", conn)
        conn.close()
        st.dataframe(df_history, use_container_width=True)