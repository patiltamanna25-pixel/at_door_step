import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='Tamanna@2512',database='at_doorstep')
cursor=conn.cursor()
# cursor.execute('''CREATE TABLE user(user_id INT AUTO_INCREMENT PRIMARY KEY,
# username VARCHAR(50),
# NOT NULL UNIQUE ,
# password_hash VARCHAR(255) NOT NULL,
# role ENUM('ADMIN','STORE_MANAGER','DELIVERY_PARTNER','CUSTOMER') NOT NULL,
# is_active TINYINT(1) NOT NULL DEFAULT 1,
# created_at DATE NOT NULL);
# ''')
q='select * from company_info ;'
cursor.execute(q)
print(cursor.fetchall())