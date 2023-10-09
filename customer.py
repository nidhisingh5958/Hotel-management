import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='tiger',database='hotel')
c1=conn.cursor()
c1.execute('create table custdata(cid integer not null PRIMARY KEY,name varchar(100) not null,addr varchar(200) not null,indate datetime not null,outdate datetime not null);')
conn.commit()
print("Table created successfully")
