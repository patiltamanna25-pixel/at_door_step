from db import get_db_connection

def show_dashboard(user_id):
    while True:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM delivery_partners WHERE user_id = %s", (user_id,))
        rider = cursor.fetchone()

        print("\n" + "="*70)
        print(f"               DELIVERY PARTNER PORTAL - {rider['full_name'].upper()}")
        print("="*70)
        print(" [1] View Assigned Deliveries")
        print(" [2] Update Order Status to DELIVERED & Collect Payment")
        print(" [3] Logout")

        choice = input("\n Enter Choice [1-3]: ").strip()

        if choice == '1':
            cursor.execute("SELECT order_id, order_number, total_amount, paid_amount, order_status, payment_status FROM orders WHERE partner_id = %s", (rider['partner_id'],))
            orders = cursor.fetchall()
            print("\n" + f"{'ID':<4} {'Order No':<15} {'Amount':<10} {'Order Status':<12} {'Payment Status'}")
            print("-" * 65)
            for o in orders:
                print(f"{o['order_id']:<4} {o['order_number']:<15} Rs.{o['total_amount']:<7} {o['order_status']:<12} {o['payment_status']}")

        elif choice == '2':
            o_id = input(" Enter Order ID to Mark as Delivered: ").strip()
            amt = input(" Enter Amount Collected: ").strip()
            
            # Update order status and collection status
            query = """
                UPDATE orders 
                SET paid_amount = paid_amount + %s,
                    order_status = 'DELIVERED',
                    payment_status = CASE WHEN (paid_amount + %s) >= total_amount THEN 'PAID' ELSE 'PARTIAL' END
                WHERE order_id = %s
            """
            cursor.execute(query, (amt, amt, o_id))
            conn.commit()
            print("[SUCCESS] Order delivered and payment updated.")

        elif choice == '3':
            cursor.close()
            conn.close()
            break

        cursor.close()
        conn.close()