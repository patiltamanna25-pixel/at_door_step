import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Tamanna@2512", 
            database="at_doorstep_db"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"\n[ERROR] Database Connection Failed: {err}")
        return None