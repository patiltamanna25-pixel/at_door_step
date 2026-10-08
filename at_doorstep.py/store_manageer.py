from db import get_db_connection
from tabulate import tabulate

def show_dashboard(user_id):
    while True:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM dark_stores WHERE user_id = %s", (user_id,))
        hub = cursor.fetchone()

        print("\n" + "="*70)
        print(f"             DARK STORE MANAGER PORTAL - {hub['hub_name'].upper()}")
        print("="*70)
        print(" [1] View Local Assigned Delivery Riders")
        print(" [2] View Low Stock Inventory Alerts")
        print(" [3] Logout")

        choice = input("\n Enter Choice [1-3]: ").strip()

        if choice == '1':
            cursor.execute("SELECT partner_id, full_name, phone, daily_target, is_active FROM delivery_partners WHERE store_id = %s", (hub['store_id'],))
            riders = cursor.fetchall()
            print(tabulate(riders,headers=cursor.column_names,tablefmt='grid'))
            print("-" * 60)
            for r in riders:
                status = "ACTIVE" if r['is_active'] == 1 else "INACTIVE"
                print(tabulate(status,headers=cursor.column_names,tablefmt='grid'))

        elif choice == '2':
            cursor.execute("SELECT product_name, stock_quantity, reorder_level FROM inventory WHERE stock_quantity <= reorder_level")
            alerts = cursor.fetchall()
            print(tabulate(alerts,headers=cursor.column_names,tablefmt='grid'))
            print("-" * 60)
            for a in alerts:
                print(f"{a['product_name']:<30} {a['stock_quantity']:<15} {a['reorder_level']}")

        elif choice == '3':
            cursor.close()
            conn.close()
            break

        cursor.close()
        conn.close()