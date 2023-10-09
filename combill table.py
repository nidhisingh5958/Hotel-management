import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='tiger',database='hotel')
c1=conn.cursor()

c1.execute('create table combill(cid integer not null ,FOREIGN KEY(cid) REFERENCES custdata(cid),rno integer not null,room_rent integer not null,restaurent_bill integer, laundry_bill integer,total_bill integer not null);')
conn.commit()
print("table created successfully")
