from db import get_db_connection

def authenticate_user(username, password):
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE username = %s AND password_hash = %s AND is_active = 1"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return user

def register_customer():
    print("\n" + "="*50)
    print("           NEW CUSTOMER REGISTRATION")
    print("="*50)
    
    username = input(" Enter New Username          : ").strip()
    password = input(" Enter New Password          : ").strip()
    full_name = input(" Enter Full Name             : ").strip()
    phone = input(" Enter Phone Number          : ").strip()
    delivery_addr = input(" Enter Delivery Address      : ").strip()

    conn = get_db_connection()
    if not conn:
        print("[ERROR] Database connection failed.")
        return

    cursor = conn.cursor(dictionary=True)

    try:
        # 1. Check if username already exists
        cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            print("\n[ERROR] Username already taken. Please choose another one.")
            return

        # 2. Assign default Dark Store Hub (Hub 1) and Delivery Partner (Rider 1)
        store_id = 1
        partner_id = 1

        # 3. Insert into users table
        user_query = """
            INSERT INTO users (username, password_hash, role, is_active, created_at)
            VALUES (%s, %s, 'CUSTOMER', 1, CURDATE())
        """
        cursor.execute(user_query, (username, password))
        new_user_id = cursor.lastrowid

        # 4. Insert into customers profile table
        cust_query = """
            INSERT INTO customers (user_id, store_id, partner_id, full_name, phone, delivery_addr, is_active)
            VALUES (%s, %s, %s, %s, %s, %s, 1)
        """
        cursor.execute(cust_query, (new_user_id, store_id, partner_id, full_name, phone, delivery_addr))

        conn.commit()
        print("\n[SUCCESS] Account created successfully! You can now log in.")

    except Exception as e:
        conn.rollback()
        print(f"\n[ERROR] Registration failed: {e}")
    finally:
        cursor.close()
        conn.close()