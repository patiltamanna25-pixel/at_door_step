# import mysql.connector
# conn=mysql.connector.connect(host='localhost',user='root',password='Tamanna@2512',database='mysql_930')
# if conn.is_connected():
#     print("connection is connected succesfully")
# cursor=conn.cursor()
# cursor.execute('Show Tables;')
# print(cursor.fetchall())
# q='SELECT * FROM EMPLOYEE;'
# cursor.execute(q)
# print(cursor.fetchall())
# q='SELECT * FROM EMPLOYEE where emp_id =101;'
# cursor.execute(q)
# print(cursor.fetchall())
# q='SELECT * FROM EMPLOYEE where emp_id =%s;'
# i=int(input("Enter the id you want to fetch:"))
# cursor.execute(q,(i,))
# print(cursor.fetchall())
# q='CREATE TABLE user(id int,name varchar(30),Password int);'
# cursor.execute(q)
# print("Table")
# cursor.execute('Show Tables;')
# # print(cursor.fetchall())
# q="insert into user values(1,'Mani',1234);"
# cursor.execute(q)
# conn.commit()
# q='SELECT * FROM user;'
# cursor.execute(q)
# print(cursor.fetchall())
# u_name=input("Enter your Name:")
# password=int(input("Enter your Password:"))
# q="SELECT * FROM user WHERE name =%s AND Password=%s"
# cursor.execute(q,(u_name,password))
# if cursor.fetchone():
#     print("Welcome to Dashboard")
# import random 
# import streamlit as st
# st.title('')
# user=st.text_input("Enter your name")
# Password=st.number_input("Enter your Password")
# if st.button('submit',type='Primary'):
#     print(user,)


