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

def register_customer(username, password, full_name, phone, delivery_addr):
    conn = get_db_connection()
    if not conn:
        return False, "Database connection failed."

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            return False, "Username already taken. Please choose another."

        store_id, partner_id = 1, 1

        user_query = "INSERT INTO users (username, password_hash, role, is_active, created_at) VALUES (%s, %s, 'CUSTOMER', 1, CURDATE())"
        cursor.execute(user_query, (username, password))
        new_user_id = cursor.lastrowid

        cust_query = "INSERT INTO customers (user_id, store_id, partner_id, full_name, phone, delivery_addr, is_active) VALUES (%s, %s, %s, %s, %s, %s, 1)"
        cursor.execute(cust_query, (new_user_id, store_id, partner_id, full_name, phone, delivery_addr))

        conn.commit()
        return True, "Account created successfully! You can now log in."
    except Exception as e:
        conn.rollback()
        return False, f"Registration failed: {e}"
    finally:
        cursor.close()
        conn.close()