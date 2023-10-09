import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='tiger')
c1=conn.cursor()
if conn.is_connected:
             c1.execute("create database hotel;")
             print("database created successfully")
