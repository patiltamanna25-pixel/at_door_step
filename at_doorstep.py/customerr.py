from db import get_db_connection
from tabulate import tabulate
import datetime

def show_dashboard(user_id):
    while True:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM customers WHERE user_id = %s", (user_id,))
        cust = cursor.fetchone()

        print("\n" + "="*70)
        print(f"             AT DOORSTEP GROCERY PORTAL - {cust['full_name'].upper()}")
        print("="*70)
        print(" [1] Browse Available Catalog")
        print(" [2] Place Instant Grocery Order")
        print(" [3] View Order History & Dues")
        print(" [4] Logout")

        choice = input("\n Enter Choice [1-4]: ").strip()

        if choice == '1':
            cursor.execute("SELECT product_id, product_name, unit_price, stock_quantity FROM inventory")
            prods = cursor.fetchall()
            print("\n" + f"{'ID':<4} {'Product Name':<30} {'Unit Price':<12} {'In Stock'}")
            print("-" * 55)
            for p in prods:
                print(f"{p['product_id']:<4} {p['product_name']:<30} Rs.{p['unit_price']:<9} {p['stock_quantity']}")

        elif choice == '2':
            p_id = input(" Enter Product ID to Order: ").strip()
            qty = int(input(" Enter Quantity: ").strip())

            # Verify stock underflow protection
            cursor.execute("SELECT product_name, unit_price, stock_quantity FROM inventory WHERE product_id = %s", (p_id,))
            prod = cursor.fetchone()

            if prod and prod['stock_quantity'] >= qty:
                total_cost = float(prod['unit_price']) * qty
                order_no = f"ORD-2026-{datetime.datetime.now().strftime('%M%S')}"
                today = datetime.date.today().strftime('%Y-%m-%d')

                # Atomic transaction: Create Order + Deduct Inventory Stock
                cursor.execute(
                    "INSERT INTO orders (order_number, customer_id, partner_id, total_amount, paid_amount, order_status, payment_status, order_date) VALUES (%s, %s, %s, %s, 0.00, 'PENDING', 'UNPAID', %s)",
                    (order_no, cust['customer_id'], cust['partner_id'], total_cost, today)
                )
                cursor.execute("UPDATE inventory SET stock_quantity = stock_quantity - %s WHERE product_id = %s", (qty, p_id))
                conn.commit()
                print(f"\n[SUCCESS] Order {order_no} placed successfully! Total Amount: Rs.{total_cost:.2f}")
            else:
                print("\n[ERROR] Order failed: Insufficient stock available.")

        elif choice == '3':
            cursor.execute("SELECT order_number, total_amount, paid_amount, order_status, payment_status FROM orders WHERE customer_id = %s", (cust['customer_id'],))
            history = cursor.fetchall()
            print(tabulate(history,headers=cursor.column_names,tablefmt='grid'))
            print("-" * 70)
            for h in history:
                print(f"{h['order_number']:<15} Rs.{h['total_amount']:<12} Rs.{h['paid_amount']:<12} {h['order_status']:<12} {h['payment_status']}")

        elif choice == '4':
            cursor.close()
            conn.close()
            break

        cursor.close()
        conn.close()