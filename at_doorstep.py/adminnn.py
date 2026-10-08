from db import get_db_connection
from tabulate import tabulate
def show_dashboard(user_id):
    while True:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Dynamic ratio queries using aggregates
        cursor.execute("SELECT COUNT(CASE WHEN is_active=1 THEN 1 END), COUNT(*) FROM customers")
        act_c, tot_c = cursor.fetchone()

        cursor.execute("SELECT COUNT(CASE WHEN is_active=1 THEN 1 END), COUNT(*) FROM dark_stores")
        act_s, tot_s = cursor.fetchone()

        cursor.execute("SELECT COUNT(CASE WHEN is_active=1 THEN 1 END), COUNT(*) FROM delivery_partners")
        act_r, tot_r = cursor.fetchone()

        print("\n" + "="*70)
        print("                       SYSTEM ADMIN DASHBOARD")
        print("="*70)
        print(f" Network Status: Active Customers: {act_c}/{tot_c} | Dark Stores: {act_s}/{tot_s} | Riders: {act_r}/{tot_r}")
        print("-" * 70)
        print(" [1] View Complete Product Inventory Catalog")
        print(" [2] Restock Product Inventory")
        print(" [3] Soft-Deactivate User Account")
        print(" [4] View Complete user's Information")
        print(" [5] Logout")
        
        choice = input("\n Enter Choice [1-5]: ").strip()
        if choice == '1':
            cursor.execute("SELECT product_id, sku_code, product_name, unit_price, stock_quantity FROM inventory")
            items = cursor.fetchall()
            print(tabulate(items,headers=cursor.column_names,tablefmt='grid'))
            
        elif choice == '2':
            p_id = input(" Enter Product ID to Restock: ").strip()
            qty = input(" Enter Additional Quantity: ").strip()
            # Atomic update transaction
            cursor.execute("UPDATE inventory SET stock_quantity = stock_quantity + %s WHERE product_id = %s", (qty, p_id))
            conn.commit()
            print("[SUCCESS] Inventory stock updated successfully.")

        elif choice == '3':
            u_id = input(" Enter User ID to Deactivate: ").strip()
            cursor.execute("UPDATE users SET is_active = 0 WHERE user_id = %s", (u_id,))
            conn.commit()
            print("[SUCCESS] User account soft-deactivated.")
        elif choice =='4':
            cursor.execute("SELECT customer_id, user_id, store_id, partner_id, full_name, phone, delivery_addr, is_active FROM customers;")
            items2=cursor.fetchall()
            print(tabulate(items2,headers=cursor.column_names,tablefmt='grid'))
        elif choice == '5':
            print("=========LOGGED OUT=========== ")
            break
        else:
            cursor.close()
            conn.close()